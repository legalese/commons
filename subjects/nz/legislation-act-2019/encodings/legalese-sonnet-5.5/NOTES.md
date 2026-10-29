# Legislation Act 2019 (New Zealand), 2019 No 58 -- an encoding in L4

Row `legalese-sonnet-5.5`. **Status: draft.** No domain expert has read this encoding against the text (see `encoding.json`, `not_reviewed`).
Target compiler: **`main`** (the stable build). Written and checked with `l4 1.6.98 (main, 7689b0d, 2026-10-19)`; every module was also run on `l4 1.6.102 (main, e4f2553, 2026-10-26)` and reads the same there (the `check.sh` output below).

## The text, and what it is

- The only source is `../../registers/source-bundle/act_public_2019_58.txt`: a **plain-text rendering made by a converter script** (`workbench harvest/fetch-nz.py`, from the Parliamentary Counsel Office's XML, retrieved 2026-10-13). **It is not the official text**, and nothing in this encoding has been verified against the official text. Its sha256 is `3c77363d72dfd8a46abc201658cce2b38b1ad43f1101aa0f4af78c3db8d19afa`.
- The rendering has 1,430 lines, every one non-blank. The converter **dropped the subsection numbers and paragraph labels** and **flattened the tables**. So a coverage row is keyed by its line range in the text (`src:N` always means line N of that file), and a subsection is cited as the subsection the Act's own cross-references name (for example "section 133(2)"), which I checked against those cross-references for every section the encoding cites.
- Every quotation in the modules was copied from the text by a script (not shipped; see "Generators and checkers used and not shipped"), and `srcrefs.py check --refs` confirms each `-- src:N` quotation and each `@ref ... (src:N)` locator against the text. The licence note is `SOURCE-LICENSE.md`, which points to `../../SOURCE-LICENSE.md` and does not repeat it.

## Seat

**A person who has a time limit to meet under New Zealand legislation, or who needs to know when legislation takes effect or how it is to be read, asking on which day their period ends and which of their days count.**

Why this seat: the Act is an interpretation Act. Nearly everything in it is a rule for reading other legislation, and the questions an individual brings to it are questions of time and of reading: *on which day does my period end? is this day a working day? when did the law I am relying on come into force, and is it still in force today? what happens to my rights if it is repealed? did my posted document arrive? may I read the legislation free of charge?* The seat is never an official: what the Act asks of the Minister, the Attorney-General, the Clerk of the House, the Chief Parliamentary Counsel and the PCO is encoded in layer 1, and appears in `nz-seat.l4` only as what it means for the person (a deadline for secondary legislation they rely on, a charge they may be refunded, a document that proves something).

Layer 2 is two files: `nz-seat.l4` (46 questions, each with `@export` and `@desc`, grouped under 8 `§` headings in the order of the text) and `nz-cases-seat.l4` (148 worked cases, at least two for every question). Plain inputs: one per fact, each `@desc` worded as that person would be asked. The seat imports the layer-1 modules and restates no rule; no layer-1 module was changed to suit it. The seat questions:

| # | Section heading | Question | Cases |
| --- | --- | --- | --- |
| 1 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Is this instrument secondary legislation (s 5(1))? | 3 |
| 2 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Do the Legislation Act's rules of reading apply to the legislation I am reading (s 9)? | 4 |
| 3 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Does the legislation govern what happened on my day (s 11)? | 4 |
| 4 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Does the legislation apply to something that happened before it came into force (s 12)? | 3 |
| 5 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Is this day a working day (s 13)? | 5 |
| 6 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Does my notice count as public notification (s 13)? | 3 |
| 7 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Is what I have prepared writing under the Act (s 13)? | 5 |
| 8 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Does the Act define the word I am relying on (s 13)? | 5 |
| 9 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Are my partner and I in a de facto relationship under the Act (s 14)? | 5 |
| 10 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Is my posted document taken to have been sent (s 17)? | 3 |
| 11 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | On what day is my posted document taken to have been received (s 17)? | 3 |
| 12 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Is the Crown bound by this Act or part of an Act (s 22)? | 2 |
| 13 | Reading and applying legislation (Part 1 and Part 2, ss 5 to 23) | Does an example in the legislation limit the provision it illustrates (s 23, Schedule 1 clause 4)? | 3 |
| 14 | When legislation takes effect, and when it stops (ss 25 to 39) | On what day does the Act, or my part of it, come into force (s 25)? | 3 |
| 15 | When legislation takes effect, and when it stops (ss 25 to 39) | Does a reference in the commencement section reach the provision I am looking at (s 25)? | 4 |
| 16 | When legislation takes effect, and when it stops (ss 25 to 39) | On what day does the secondary legislation, or my part of it, come into force (s 26)? | 4 |
| 17 | When legislation takes effect, and when it stops (ss 25 to 39) | At what moment does the legislation come into force (s 27)? | 4 |
| 18 | When legislation takes effect, and when it stops (ss 25 to 39) | On what day does the legislation come into force if it says a number of months after my event (s 28)? | 2 |
| 19 | When legislation takes effect, and when it stops (ss 25 to 39) | On what day does the legislation come into force if it says a number of days, weeks, months or years after my event (s 28)? | 4 |
| 20 | When legislation takes effect, and when it stops (ss 25 to 39) | Do my existing rights, and a proceeding I am in, survive the repeal or amendment (s 33)? | 3 |
| 21 | When legislation takes effect, and when it stops (ss 25 to 39) | Am I still liable for an offence I committed before the law was repealed or amended (s 34)? | 2 |
| 22 | When legislation takes effect, and when it stops (ss 25 to 39) | May the old law still be used to deal with my offence (s 34(2))? | 5 |
| 23 | When legislation takes effect, and when it stops (ss 25 to 39) | What does a reference to new legislation that is not yet in force refer to today (s 37)? | 3 |
| 24 | When legislation takes effect, and when it stops (ss 25 to 39) | What does a reference in legislation to repealed legislation mean now (s 38)? | 2 |
| 25 | When legislation takes effect, and when it stops (ss 25 to 39) | Is legislation that is repealed from a certain day still in force on my day (s 39)? | 2 |
| 26 | When legislation takes effect, and when it stops (ss 25 to 39) | Is legislation that is repealed on a certain day still in force on my day (s 39)? | 2 |
| 27 | When legislation takes effect, and when it stops (ss 25 to 39) | Does legislation that is to remain in force until a certain day still apply on my day (s 39)? | 2 |
| 28 | Counting a period of time (ss 54 to 58) | On which day does my period end (ss 54 and 56)? | 11 |
| 29 | Counting a period of time (ss 54 to 58) | On which day does my period end if the legislation names the closing day (s 54)? | 3 |
| 30 | Counting a period of time (ss 54 to 58) | On which day may I first do the second thing if at least so many working days must lie between (s 54 Item 7)? | 2 |
| 31 | Counting a period of time (ss 54 to 58) | Until which day may I do the thing if my last day is not a working day (s 55)? | 5 |
| 32 | Counting a period of time (ss 54 to 58) | Am I in time if I do the thing on this day (s 55)? | 2 |
| 33 | Counting a period of time (ss 54 to 58) | At what New Zealand time does my moment fall (s 57)? | 2 |
| 34 | Counting a period of time (ss 54 to 58) | Is my distance within the limit, measured in a straight line on a horizontal plane (s 58)? | 2 |
| 35 | Material that secondary legislation incorporates by reference (ss 64 to 66, Schedule 2) | Do the later changes to the material my regulation incorporates have legal effect (s 66)? | 3 |
| 36 | Material that secondary legislation incorporates by reference (ss 64 to 66, Schedule 2) | Is the chief executive's certified copy enough to prove the material that was incorporated (Schedule 2 clause 4)? | 2 |
| 37 | Publication and official versions (ss 69 to 81) | Am I entitled to read the legislation free of charge on the legislation website (s 72)? | 2 |
| 38 | Publication and official versions (ss 69 to 81) | What is the official version of the legislation taken to prove (s 79)? | 3 |
| 39 | Publication and official versions (ss 69 to 81) | Must the court take judicial notice of the legislation, so that I need not prove it (s 81)? | 2 |
| 40 | Parliament's oversight of secondary legislation (ss 114 to 127) | Is the secondary legislation I rely on disallowed because the House did not deal with the motion in time (s 117)? | 3 |
| 41 | Parliament's oversight of secondary legislation (ss 114 to 127) | On what day does the House's amendment of the secondary legislation I rely on take effect (s 119)? | 2 |
| 42 | Parliament's oversight of secondary legislation (ss 114 to 127) | By what day must the secondary legislation I rely on be confirmed by an Act (s 121)? | 2 |
| 43 | Parliament's oversight of secondary legislation (ss 114 to 127) | Will the secondary legislation I rely on be revoked on the confirmation deadline (ss 121 to 124)? | 4 |
| 44 | Parliament's oversight of secondary legislation (ss 114 to 127) | Am I entitled to a refund of a charge imposed under legislation that was not confirmed (s 125)? | 4 |
| 45 | Proceedings against the Parliamentary Counsel Office and its staff (s 146) | May I bring a proceeding against the Chief Parliamentary Counsel or an employee of the PCO (s 146)? | 2 |
| 46 | Transition from the earlier law (Schedule 1) | Does section 26 govern when the secondary legislation I rely on, made before the Act, came into force (Schedule 1 clause 5)? | 2 |

The seven calendars of named days (Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Matariki Observance Day, Labour Day) are **inputs** to every question that needs a working day: section 13 names them and the Act dates none of them. A question whose search for the next working day would leave the year the person gave answers NOTHING, not a guess.

## Layout

Layer 1 follows the Act's structure, one module for each part, with a test module beside it. Counts are assertions satisfied on `l4 1.6.98` (the `check.sh` table below).

| Module | What it holds | Tests | Assertions |
| --- | --- | --- | --- |
| `nz-nouns.l4` | shared nouns only (Instrument; kinds of enactment, person, number) | none | 0 |
| `nz-interpretation-time.l4` | the time rules, self-contained: imports only `prelude` and `daydate` (ss 13 month and working day; 17; 25 to 28; 39; 54 to 58) | `nz-tests-time.l4` | 165 |
| `nz-part1-preliminary.l4` | Part 1: ss 5 to 7 | `nz-tests-part1.l4` | 47 |
| `nz-part2-principles.l4` | Part 2, principles: ss 9 to 12 | `nz-tests-part2-principles.l4` | 40 |
| `nz-part2-definitions.l4` | Part 2, definitions and rules of reading: ss 13 to 23 | `nz-tests-part2-definitions.l4` | 177 |
| `nz-part2-commencement-repeal.l4` | Part 2, commencement, amendment and repeal: ss 24, 29 to 38 | `nz-tests-part2-commencement-repeal.l4` | 126 |
| `nz-part2-powers.l4` | Part 2, general empowering provisions: ss 40 to 53 | `nz-tests-part2-powers.l4` | 124 |
| `nz-part2-revision-incorporation.l4` | Part 2, revision Acts and incorporation by reference: ss 59 to 66 | `nz-tests-part2-revision-incorporation.l4` | 64 |
| `nz-part3-publication.l4` | Part 3 subpart 1: ss 67 to 83A | `nz-tests-part3-publication.l4` | 202 |
| `nz-part3-editorial-revision.l4` | Part 3 subparts 2 to 4: ss 84 to 100 | `nz-tests-part3-editorial-revision.l4` | 315 |
| `nz-part5-oversight.l4` | Part 5: ss 113 to 127 | `nz-tests-part5-oversight.l4` | 109 |
| `nz-part6-7-pco-regulations.l4` | Parts 6 and 7: ss 131, 133, 134, 146, 147, 147A | `nz-tests-part6-7-pco-regulations.l4` | 56 |
| `nz-schedules.l4` | Schedules 1, 2 and the opening rule and grounds of Schedule 3 | `nz-tests-schedules.l4` | 287 |
| `nz-glossary.l4` | every defined term, as a table: one entry per term (generated from the text by a script that is not shipped) | `nz-tests-glossary.l4` | 357 |
| `nz-seat.l4` | layer 2: the seat's questions | `nz-cases-seat.l4` | 148 |

Total assertions satisfied across the 29 modules: **2217** (the `TOTAL` line below). Other files: `check.sh`, `fetch-main-l4.sh` (the stock self-check), `srcrefs.py` (quotation and locator check), `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`, `PROGRESS.md`. The scripts and tables that generated the modules are not shipped; the `.l4` files are the source.

## What is encoded, and what is not

**Encoded:** the whole of Part 2 (interpretation and application of legislation: purposes, principles, definitions, commencement, amendment and repeal, the general empowering provisions, time and distance, revision Acts, incorporation by reference); the time rules in one self-contained module; what a person can take from Parts 3 and 5 (when legislation is published, what an official version proves, how a person may read legislation free of charge, when House action disallows, amends or revokes secondary legislation, what a refund of a charge looks like); the confidentiality, delegation and liability rules of Parts 6 and 7; Schedules 1 and 2 and the opening rule and the surviving grounds of Schedule 3; every defined term.

**Not encoded, and the reason, row by row, in the coverage table:** the Act's own title, commencement and short title (inert, reason 2); purpose, overview and outline clauses that create no rule (inert, reason 1); the Parliamentary Counsel Office as an office, its staffing and its employer powers (ss 128 to 130, 132, 135 to 145, inert reason 2); the regulation-making powers (s 147 paragraphs and conditions, s 147A(3) and (4), Schedule 1 clause 19, inert reason 2); the saving for an existing appointment (Schedule 1 clause 35, inert reason 2); and what the text itself shows blank (Part 4's twelve section headings with no body, section 148, Schedule 1 clauses 30 and 31, Schedule 1A, and the lists of Schedule 4).

**Not answerable from this text, and returned as an explicit "not covered" value that a test asserts:** a period counted in weeks or in years (the Act defines neither); commencement a number of days, weeks or years after a day (section 28 is about months); an anniversary; legislation repealed "from" a day; an official New Zealand language; words shown only on a screen (is that "writing"?); the order of precedence when section 27(b) and (c) both apply; which empowering provisions Schedule 3 exempts (the table lost its provision cells); the dates of the seven named days of section 13; the New Zealand offset from UTC (section 57 hands it to the Time Act 1974); the dates of the 21st sitting day (the House's sitting calendar is an input).

## Jural relations

Hohfeld's correlatives: a claim-right is the other party's duty; a privilege (liberty) is the other party's no-right; a power is the other party's liability; an immunity is the other party's disability. Each relation is stated once, from one side, between two neutrally named parties (a "Person" is a member of the public or a maker; a "Party" is an institution). The last column is the layer-1 rule that encodes it; a provision with no relation is listed once as `none` in the second table.

| Section | Relation | Holder of the right, privilege, power or immunity | Bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- | --- |
| s 7 | claim-right / duty | Person A (anyone with a claim under the Act) | Party B (the Crown) | `this Act binds the Crown` (nz-part1-preliminary.l4) |
| s 22(1) | immunity / disability | Party A (the Crown, bound by an Act only if the Act says so) | Person B (anyone who would bind the Crown by it) | `an Act or part of an Act binds the Crown` (nz-part2-definitions.l4) |
| s 17(2) to (4) | power / liability | Person A (the person who posts a document the legislation lets be sent by post) | Person B (the person it is sent to, who is taken to have had it sent, and received, unless the contrary is proved) | `whether the document is taken to be sent` (nz-interpretation-time.l4); `the day the document is taken to be received` (nz-interpretation-time.l4) |
| s 55 | privilege (liberty) / no-right | Person A (the person with a time limit, who may do the thing on the next working day) | Person B (the person it is done to, who cannot treat that day as late) | `the last day on which the thing may be done under section 55` (nz-interpretation-time.l4) |
| s 33 | immunity / disability | Person A (the holder of an existing right, interest, title, immunity, duty, status or capacity, or of a proceeding) | Party B (the repealing or amending legislation, which cannot undo it by the repeal alone) | `the completion of the matter or thing is unaffected by the repeal or amendment` (nz-part2-commencement-repeal.l4); `the commencing of the proceeding is unaffected by the repeal or amendment` (nz-part2-commencement-repeal.l4); `the completion of the proceeding is unaffected by the repeal or amendment` (nz-part2-commencement-repeal.l4) |
| s 34 | power / liability | Party A (the authority that proceeds under the old law) | Person B (the person who committed the offence or breach before the repeal or amendment) | `the liability for an offence or breach committed on` (nz-part2-commencement-repeal.l4); `repealed or amended legislation continues to have effect as if not repealed or amended for the purpose of` (nz-part2-commencement-repeal.l4) |
| ss 35 and 36 | immunity / disability | Person A (the holder of the benefit of a thing done under the old law) | Party B (anyone bound by it, and the repealing legislation) | `a thing done in the exercise of a power continues to have effect as if exercised under the other legislation` (nz-part2-commencement-repeal.l4); `legislation made under repealed legislation continues in force as if made under the other legislation` (nz-part2-commencement-repeal.l4); `legislation may be amended or revoked as if made under the replacing legislation` (nz-part2-commencement-repeal.l4) |
| ss 40 to 42 | power / liability | Person A (the maker of secondary legislation) | Person B (those the secondary legislation binds) | `it is necessary for the secondary legislation to refer to the preconditions for making it` (nz-part2-powers.l4); `a power to make secondary legislation includes the power to make a consequential amendment` (nz-part2-powers.l4); `later secondary legislation may amend, revoke or replace secondary legislation amended or replaced by an Act` (nz-part2-powers.l4) |
| ss 43 and 44 | power / liability | Person A (the person with the power, exercised before commencement) | Person B (those affected when the exercise takes effect) | `a power may be exercised before the legislation comes into force to do` (nz-part2-powers.l4); `something resulting from a pre-commencement exercise may take effect on` (nz-part2-powers.l4) |
| ss 45 to 51 | power / liability | Person A (the person with the power) | Person B (those whose position the exercise alters) | `the power to appoint a person to an office includes the power to` (nz-part2-powers.l4); `the power may be exercised again` (nz-part2-powers.l4); `a power conferred on an office holder may be exercised by` (nz-part2-powers.l4); `the power to make secondary legislation or an instrument includes the power to` (nz-part2-powers.l4); `the power includes the power to use it by` (nz-part2-powers.l4); `the person may identify the matter by referring to a class or classes of matters` (nz-part2-powers.l4); `it may be exercised or performed from time to time` (nz-part2-powers.l4) |
| ss 52 and 53 | power / liability | Person A (the person who may approve or prescribe a form) | Person B (those who must use the form) | `a form is invalid just because of its differences from the approved or prescribed form` (nz-part2-powers.l4); `power A includes the power to` (nz-part2-powers.l4) |
| s 64 | power / liability | Person A (the maker of secondary legislation, who may incorporate material by reference) | Person B (those the secondary legislation binds) | `section 64 is sufficient authority for secondary legislation to incorporate material that is` (nz-part2-revision-incorporation.l4) |
| s 66 | immunity / disability | Person A (those the secondary legislation binds, who are not bound by later changes to the incorporated material) | Party B (the originator of the material) | `what effect the amendments to the incorporated material have` (nz-part2-revision-incorporation.l4) |
| Schedule 2 cll 1 to 3 | claim-right / duty | Person A (anyone who wants to see or buy the incorporated material) | Party B (the chief executive and the maker) | `the chief executive has met the requirements before the secondary legislation incorporating material is made` (nz-schedules.l4); `the chief executive has met the requirements once the instrument incorporating material is made` (nz-schedules.l4); `the material is made publicly available as clause 3 requires` (nz-schedules.l4) |
| Schedule 2 cl 4 | immunity / disability | Person A (a party who produces the certified copy) | Person B (the other party, who must bring evidence to the contrary) | `the certified copy is sufficient evidence of the material incorporated` (nz-schedules.l4) |
| ss 67 to 71 | claim-right / duty | Person A (any person) | Party B (the PCO, which must draft and publish) | `it is a main drafting function of the PCO` (nz-part3-publication.l4); `the PCO must publish` (nz-part3-publication.l4); `the PCO must publish a consolidation` (nz-part3-publication.l4); `the event after which the PCO must publish electronically as soon as practicable` (nz-part3-publication.l4) |
| s 72 | claim-right / duty | Person A (any person) | Party B (the PCO, which must keep the legislation accessible free of charge as far as practicable) | `a person may access or download the legislation from the legislation website free of charge` (nz-part3-publication.l4); `the PCO has met section 72(1)` (nz-part3-publication.l4) |
| s 73 | claim-right / duty | Person A (the public) | Person B (the maker of secondary legislation the PCO does not publish) | `the maker has done what section 73(2) requires` (nz-part3-publication.l4) |
| ss 74 to 76 | claim-right / duty | Person A (the public) | Person B (the maker, and the Chief Parliamentary Counsel for the international transparency obligations) | `the applicable publication requirements come from` (nz-part3-publication.l4); `section 75 applies to the secondary legislation` (nz-part3-publication.l4); `the Chief Parliamentary Counsel has met section 76(1) for the link` (nz-part3-publication.l4); `the Chief Parliamentary Counsel has met section 76(2) for the secondary legislation` (nz-part3-publication.l4); `a direction of the Chief Parliamentary Counsel is secondary legislation` (nz-part3-publication.l4) |
| s 78 | power / liability | Party A (the PCO, which may give a version the status of an official version) | Person B (anyone, who must then treat it as official) | `is an official version of legislation` (nz-part3-publication.l4) |
| ss 79 and 80 | immunity / disability | Person A (the person who relies on the official version, or on the minimum legislative information) | Person B (the person who disputes it, and must show the contrary) | `what an official version of that kind is taken to prove` (nz-part3-publication.l4); `publication of the minimum legislative information is evidence` (nz-part3-publication.l4) |
| s 81 | claim-right / duty | Person A (a person who relies on legislation) | Party B (the court, which must take judicial notice) | `must take judicial notice` (nz-part3-publication.l4) |
| s 82 | power / liability | Party A (the Governor-General, on the Attorney-General's recommendation) | Person B (those who rely on the secondary legislation or instrument revoked) | `the Governor-General may revoke secondary legislation or another instrument under section 82` (nz-part3-publication.l4) |
| s 83 | power / liability | Party A (the Attorney-General) | Party B (the PCO, which carries out its functions subject to the direction) | `the PCO must carry out its functions subject to the direction` (nz-part3-publication.l4) |
| s 83A | claim-right / duty | Party A (the Attorney-General, then the House of Representatives) | Party B (the Chief Parliamentary Counsel, then the Attorney-General) | `the Chief Parliamentary Counsel has met section 83A(1)` (nz-part3-publication.l4); `the Attorney-General has met section 83A(2)` (nz-part3-publication.l4) |
| ss 86 to 91 | power / liability | Party A (the Chief Parliamentary Counsel, who authorises editorial changes) | Person B (users of the legislation, whose text changes without its effect changing) | `the PCO may make the change` (nz-part3-editorial-revision.l4); `the Governor-General may authorise the PCO to publish a renumbered or consequentially updated version` (nz-part3-editorial-revision.l4) |
| ss 95 to 99 | claim-right / duty | Party A (the House of Representatives) | Party B (the Attorney-General and the Chief Parliamentary Counsel, who prepare, certify and present revision programmes and Bills) | `the Attorney-General has complied with section 95(3)` (nz-part3-editorial-revision.l4); `the Chief Parliamentary Counsel must give the revision Bill and certificate to the Attorney-General` (nz-part3-editorial-revision.l4) |
| s 114 | claim-right / duty | Party A (the House of Representatives) | Person B (the maker, who must present the secondary legislation) | `the relevant Minister must present the secondary legislation to the House` (nz-part5-oversight.l4) |
| ss 115 to 117 | power / liability | Party A (the House of Representatives, by resolution or by not disposing of the motion in time) | Person B (the maker, and those who rely on the secondary legislation) | `the House of Representatives may disallow the secondary legislation or provision by resolution` (nz-part5-oversight.l4); `the day legislation disallowed by resolution ceases to have effect` (nz-part5-oversight.l4); `the secondary legislation is disallowed under section 117` (nz-part5-oversight.l4) |
| s 119 | power / liability | Party A (the House of Representatives) | Person B (those the secondary legislation binds) | `the House of Representatives may amend or replace the secondary legislation by resolution` (nz-part5-oversight.l4); `the day an amendment or replacement by resolution takes effect` (nz-part5-oversight.l4) |
| s 120(2) | claim-right / duty | Party A (the PCO, then the public) | Party B (the Clerk of the House, then the PCO) | `the Clerk of the House of Representatives must lodge a copy of the resolution or notice of the motion with the PCO` (nz-part5-oversight.l4) |
| ss 121 to 124 | power / liability | Party A (Parliament, by an Act that confirms) | Person B (the maker, whose secondary legislation is revoked on the deadline unless confirmed) | `the legislation is revoked on the deadline` (nz-part5-oversight.l4); `the legislation is confirmed by the deadline` (nz-part5-oversight.l4) |
| s 125 | claim-right / duty | Person A (a person who paid a duty, levy or road user charge imposed under the unconfirmed legislation) | Party B (the body that collected it, which must refund) | `a charge imposed under the unconfirmed legislation is cancelled and, if paid, refunded` (nz-part5-oversight.l4) |
| s 127 | claim-right / duty | Person A (the public) | Person B (the maker of confirmable secondary legislation, who must say so) | `the explanatory note complies with section 127` (nz-part5-oversight.l4) |
| s 131 | immunity / disability | Person A (a client of the PCO) | Person B (anyone who seeks to make the confidential communication known) | `the communication is subject to legal professional privilege` (nz-part6-7-pco-regulations.l4) |
| ss 133 and 134 | power / liability | Party A (the Chief Parliamentary Counsel, who delegates and revokes delegations) | Person B (those who deal with a delegate) | `the Chief Parliamentary Counsel may delegate the function, duty or power` (nz-part6-7-pco-regulations.l4); `the delegate's act has the same effect as if conferred directly by this Act` (nz-part6-7-pco-regulations.l4); `the delegation is revoked` (nz-part6-7-pco-regulations.l4) |
| s 146 | immunity / disability | Person A (the Chief Parliamentary Counsel and an employee of the PCO) | Person B (a person who would bring a proceeding for an act or omission in good faith) | `a proceeding may be brought against the person` (nz-part6-7-pco-regulations.l4) |
| Schedule 1 cll 15 and 16 | claim-right / duty | Party A (the PCO) | Person B (the maker, who must lodge the minimum legislative information or the secondary legislation by the deadline) | `clause 15 applies on` (nz-schedules.l4); `clause 16 applies on` (nz-schedules.l4) |
| Schedule 1 cl 17 | claim-right / duty | Person A (the public) | Party B (the PCO, which must publish when the regulations require) | `the PCO must publish lodged information on` (nz-schedules.l4) |
| Schedule 1 cl 21 | power / liability | Party A (the Attorney-General) | Person B (the maker, who is relieved when a department meets its obligation) | `the department may meet the maker's obligation in the maker's place` (nz-schedules.l4) |
| Schedule 1 cl 27A | claim-right / duty | Party A (the Attorney-General) | Party B (the Chief Parliamentary Counsel, for the first annual report) | `the first annual report meets clause 27A` (nz-schedules.l4) |
| Schedule 3 | immunity / disability | Person A (the maker of secondary legislation to which the tables give an exemption) | Party B (the House of Representatives, which cannot require presentation or disallow it) | `a presentation or disallowance exemption applies under Schedule 3` (nz-schedules.l4) |
| ss 128 to 130, 132, 135 to 145 | power and duty of an office and of its employer | the Chief Parliamentary Counsel and the PCO as an employer | employees and the public | not encoded: inert, reason 2 (office and staffing) |
| s 147, s 147A(3) and (4), Schedule 1 cl 19 | power / liability | the Governor-General, on the Attorney-General's recommendation | those the regulations bind | not encoded: inert, reason 2 (regulation-making power); what the regulations are, once made, is in ss 147(7) to (9) and 147A(1), (2), (5), which are encoded |

Every other section and clause creates no relation between two parties, or is not encoded. Each is listed once:

| Provision | Heading | Relation | Why |
| --- | --- | --- | --- |
| s 1 | Title | none | none encoded: machinery (inert, reason 2) |
| s 2 | Commencement | none | none encoded: machinery (inert, reason 2) |
| s 3 | Purpose of this Act | none | none: not operative (inert, reason 1) |
| s 4 | Overview of this Act | none | none: not operative (inert, reason 1) |
| s 5 | Interpretation | none | none: definitions (a table with a test per term) |
| s 6 | Transitional, savings, and related provisions | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 8 | Purposes of this Part | none | none: not operative (inert, reason 1) |
| s 9 | Application of this Part | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 10 | How to ascertain meaning of legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 11 | Legislation applies to circumstances as they arise | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 12 | Legislation does not have retrospective effect | none | none: a rule about when legislation applies or takes effect, or how a period is counted; no party holds a position against another (a fork row: see the fork register) |
| s 13 | Definitions of terms for all legislation | none | none: definitions (a table with a test per term) |
| s 14 | Meaning of de facto relationship | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 15 | Meaning of step-parent, etc | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 16 | References to specific gender or kind of person include others | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 18 | Parts of speech have corresponding meaning | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 19 | Words in singular include plural and vice versa | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 20 | Words used in secondary legislation or other instruments have same mea | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 21 | Anything done under secondary legislation or other instrument is also  | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 23 | Examples do not limit provision | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 24 | Outline of commencement provisions | none | none: not operative (inert, reason 1) |
| s 25 | Date on which Acts commence | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 26 | Date on which secondary legislation commences | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 27 | Time at which legislation commences | none | none: a rule about when legislation applies or takes effect, or how a period is counted; no party holds a position against another (a fork row: see the fork register) |
| s 28 | When legislation commences if calculated by number of months | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 29 | Power to make commencement order | none | none: a rule about when legislation applies or takes effect, or how a period is counted; no party holds a position against another (a fork row: see the fork register) |
| s 30 | Amendments part of, and construed with, legislation amended | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 31 | References to repeal or amendment extend to other ceasing of effect | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 32 | Effect of repeal or amendment generally | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 37 | How to apply references to new legislation that is not yet in force | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 38 | How to apply references to repealed legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 39 | Time of repeal of legislation on particular day | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 54 | When periods start and end | none | none: a rule about when legislation applies or takes effect, or how a period is counted; no party holds a position against another (a fork row: see the fork register) |
| s 56 | Calculating periods of months (except for commencement of legislation) | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 57 | Determining time generally | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 58 | Determining measurements of distance | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 59 | Meaning of revision Act and old law | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 60 | Revision Act is generally to have same effect as old law | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 61 | Using old law as interpretation guide for revision Act | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 62 | Exceptions: when revision Act changes effect of old law | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 63 | Interpretation | none | none: definitions (a table with a test per term) |
| s 65 | Schedule 2 applies if material incorporated by reference | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 77 | Definitions for purposes of international transparency obligations | none | none: definitions (a table with a test per term) |
| s 79A | Legislative status of publication notes and information | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 84 | Purpose of this subpart | none | none: not operative (inert, reason 1) |
| s 85 | Interpretation | none | none: definitions (a table with a test per term) |
| s 92 | Purpose of this subpart | none | none: not operative (inert, reason 1) |
| s 93 | Overview of this subpart | none | none: not operative (inert, reason 1) |
| s 94 | Interpretation | none | none: definitions (a table with a test per term) |
| s 100 | PCO’s annual report may address matters relating to revision and edito | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 101 | Purpose of this Part | none | none: blank in this text (only the heading survives) |
| s 102 | Interpretation in this Part | none | none: blank in this text (only the heading survives) |
| s 103 | Chief executives must prepare and publish disclosure statements for Go | none | none: blank in this text (only the heading survives) |
| s 104 | What must be contained, or linked to, in disclosure statements | none | none: blank in this text (only the heading survives) |
| s 105 | Disclosure statement requirements do not apply to certain Bills and am | none | none: blank in this text (only the heading survives) |
| s 106 | Chief executives must act independently and include statement of respo | none | none: blank in this text (only the heading survives) |
| s 107 | Government notice must be issued to support consistent approach across | none | none: blank in this text (only the heading survives) |
| s 108 | Government notice may be issued only with approval of House of Represe | none | none: blank in this text (only the heading survives) |
| s 109 | Factors to be considered in determining classes of legislation requiri | none | none: blank in this text (only the heading survives) |
| s 110 | Ministerial direction may be given to support consistent approach acro | none | none: blank in this text (only the heading survives) |
| s 111 | Disclosure relates only to information available to public under Offic | none | none: blank in this text (only the heading survives) |
| s 112 | Validity of legislation not affected by failure to comply with this Pa | none | none: blank in this text (only the heading survives) |
| s 113 | Purpose of this Part | none | none: not operative (inert, reason 1) |
| s 118 | Effect of disallowance on legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 126 | Effect on some legislation of not being confirmed by deadline (whether | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| s 148 | Review of revision programme provisions after 30 June 2020 | none | none: blank in this text (only the heading survives) |
| Schedule 1 clause 1 | General overview of this Part | none | none: not operative (inert, reason 1) |
| Schedule 1 clause 2 | Definitions for this Part | none | none: definitions (a table with a test per term) |
| Schedule 1 clause 3 | Part 2 of this Act applies to both existing and new legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 4 | Exception for examples in existing legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 5 | Exception for commencement of secondary legislation made before main c | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 6 | Saving of definitions for pre-1 November 1999 legislation | none | none: definitions (a table with a test per term) |
| Schedule 1 clause 7 | Saving of definitions for legislation made before main commencement da | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 8 | Savings of previous Proclamations | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 9 | Savings of material incorporated by reference under Legislation Act 20 | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 10 | How Abolition of Provinces Act 1875 affects provincial legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 11 | Purpose | none | none: not operative (inert, reason 1) |
| Schedule 1 clause 12 | Outline of transition to Part 3 publication | none | none: not operative (inert, reason 1) |
| Schedule 1 clause 13 | Definition of secondary legislation is effective on main commencement  | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 14 | Existing requirements continued as applicable publication requirements | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 18 | Application of subpart 1 of Part 3 of this Act | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 20 | Transitional application of publication responsibilities | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 22 | Commencement orders for existing Acts are secondary legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 23 | PCO’s responsibility for drafting secondary legislation | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 24 | PCO may continue to draft and publish other instruments | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 25 | How power to issue official versions applies to previous or existing l | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 26 | How legal status of previous official versions applies | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 27 | Previous printed official versions continue until new official version | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 27B | Publication statement taken not to have been required | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 28 | How power to make editorial changes applies to legislation published u | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 29 | Provisions on revision Bills apply also to previous revision Bills | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 30 | Disclosure requirements apply only to Bills introduced after Part 4 co | none | none: blank in this text (only the heading survives) |
| Schedule 1 clause 31 | Ministers may perform duties before Part 4 commencement date | none | none: blank in this text (only the heading survives) |
| Schedule 1 clause 32 | Limited application of presentation requirements to secondary legislat | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 33 | Old disallowance provisions continue to apply to existing notices of m | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 33A | New disallowance provisions apply to previously disallowable instrumen | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 1 clause 34 | Old confirmation provisions continue to apply to existing confirmable  | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 2 clause 5 | Material incorporated by reference need not be published under this Ac | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 2 clause 6 | Failure to comply does not invalidate | none | none: a rule about what words, days or periods mean, or where a rule applies; no party holds a position against another |
| Schedule 3 (the tables) | the rows of the tables | none beyond the Schedule 3 row above | each table row is a result cell whose provision cells did not survive; see the coverage table |
| Parts, subparts, schedule titles and the Act's title | headings | none | not operative (inert, reason 1) |

## Coverage

Method: `coverage.py` cuts the text into rows by script (a heading, a heading-only section, a subsection group, a paragraph run, a defined term, an Example, a row of s 54's examples, a row of s 71's table, a row of the Schedule 3 tables, a line of s 147(1)), then checks that **every non-blank line falls in exactly one row**. The disposition of each row is written in `coverage-spec.tsv` by `gen_coverage_spec.py`: a row is encoded only when an `@ref` in a layer-1 module cites its lines (or its example is a test case), and the script stops if any row has no disposition.

Audit: text lines **1,430**, non-blank **1430**, covered **1430**, uncovered **0**, covered twice **0**. Rows: **703**. Rows before and after: the first cut of the text had 700 rows. Reading five more definition lines as defined terms (Inland Revenue Bills and responsible Minister in s 68(4), Consumers Price Index in s 96(4), union in s 141(2), list deadline in Schedule 1 clause 2) gives **702**: the net change is two because two of the five (Consumers Price Index and union) were already rows of their own. The second pass made the definition on line 1048 (publication deadline), which the first pass had folded into publication exemption, a row of its own: **703**.

| Disposition | Rows |
| --- | --- |
| encoded | 503 |
| fork | 14 |
| inert (1: not operative) | 88 |
| inert (2: machinery) | 80 |
| repealed or blank in this text | 18 |
| **all rows** | **703** |

Notes on how to read the table. *Encoded* means a rule, definition or table in layer-1 L4 with a test, citing the provision with `@ref`; where a row is a lead-in ("In this Act, unless the context otherwise requires,--") the target names the function or the glossary field that carries it. *Fork* rows point at the fork register below and at the rule that encodes the chosen reading. *Inert* has only reasons 1 (not operative), 2 (machinery) and 3 (text shown repealed or blank); there is no row of reason 3, because the blank text is classed in the last disposition. The Schedule 3 table rows are encoded as one rule whose match against the tables is an input, because the converter kept only each row's result cell (and, for 6 grounds, the ground itself); the identifying cells are not in the deposited text (finding 14).

| Lines | Row | What | Disposition | Where / why |
| --- | --- | --- | --- | --- |
| 1 | title | Legislation Act 2019 | inert (1: not operative) | not operative -- the title line |
| 2-3 | s1.1 | 1 Title | inert (2: machinery) | machinery -- s 1: short title |
| 4-12 | s2.1 | 2 Commencement | inert (2: machinery) | machinery -- s 2(1): the Act's own commencement |
| 13 | s2.2 | One or more Orders in Council may set different dates for different pr | inert (2: machinery) | machinery -- s 2(2): the Act's own commencement (Orders in Council) |
| 14 | s2.3 | An Order in Council made under this section is secondary legislation ( | inert (2: machinery) | machinery -- s 2(3): the Act's own commencement (the Order is secondary legislation) |
| 15 | h15 | Part 1 — Preliminary provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 16-17 | s3.1 | 3 Purpose of this Act | inert (1: not operative) | not operative -- s 3(1): purpose clause, creates no rule |
| 18-24 | s3.2 | To that end, this Act— | inert (1: not operative) | not operative -- s 3(2): purpose clause (how the Act serves it), creates no rule |
| 25-27 | s4.1 | 4 Overview of this Act | inert (1: not operative) | not operative -- s 4: overview |
| 28-31 | s4.2 | Part 2 provides for the interpretation and application of legislation, | inert (1: not operative) | not operative -- s 4: overview |
| 32-35 | s4.3 | Part 3 provides for the drafting and publication of legislation, inclu | inert (1: not operative) | not operative -- s 4: overview |
| 36-38 | s4.4 | Part 5 supports parliamentary oversight and control over secondary leg | inert (1: not operative) | not operative -- s 4: overview |
| 39 | s4.5 | Part 6 continues the PCO with the functions of drafting and publishing | inert (1: not operative) | not operative -- s 4: overview |
| 40 | s4.6 | Part 7 contains regulation-making powers and miscellaneous provisions. | inert (1: not operative) | not operative -- s 4: overview |
| 41 | s4.7 | This section is only a guide to the general scheme and effect of this  | inert (1: not operative) | not operative -- s 4: says of itself that it is only a guide |
| 42-44 | s4.8 | See also— | inert (1: not operative) | not operative -- s 4: signposts to other Acts |
| 45-46 | s5.1 | 5 Interpretation | encoded | nz-glossary.l4: `a definition in the Act governs the use of the term` (unless the context otherwise requires: an input) -- lead-in words |
| 47 | s5.def.administering agency | defined term: administering agency | encoded | nz-glossary.l4: entry for administering agency (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definition of administering agency |
| 48 | s5.def.applicable publication requirements | defined term: applicable publication requirements | encoded | nz-glossary.l4: entry for applicable publication requirements (tested in nz-tests-glossary.l4) |
| 49 | s5.def.chief executive, in relation to an administering agency, | defined term: chief executive, in relation to an administering agency, | encoded | nz-glossary.l4: entry for chief executive, in relation to an administering agency, (tested in nz-tests-glossary.l4) |
| 50 | s5.def.Chief Parliamentary Counsel | defined term: Chief Parliamentary Counsel | encoded | nz-glossary.l4: entry for Chief Parliamentary Counsel (tested in nz-tests-glossary.l4) |
| 51 | s5.def.consolidation | defined term: consolidation | encoded | nz-glossary.l4: entry for consolidation (tested in nz-tests-glossary.l4) |
| 52 | s5.def.current drafting practice, in subpart 2 of Part 3, | defined term: current drafting practice, in subpart 2 of Part 3, | encoded | nz-glossary.l4: entry for current drafting practice, in subpart 2 of Part 3, (tested in nz-tests-glossary.l4) |
| 53 | s5.def.disallowance exemption | defined term: disallowance exemption | encoded | nz-glossary.l4: entry for disallowance exemption (tested in nz-tests-glossary.l4) |
| 54-56 | s5.def.empowering legislation, in relation to any secondary legislation or instrument, | defined term: empowering legislation, in relation to any secondary legislation or instrument, | encoded | nz-glossary.l4: entry for empowering legislation, in relation to any secondary legislation or instrument, (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definitions of empowering legislation and empowering provision |
| 57-59 | s5.def.empowering provision, in relation to any secondary legislation or instrument, | defined term: empowering provision, in relation to any secondary legislation or instrument, | encoded | nz-glossary.l4: entry for empowering provision, in relation to any secondary legislation or instrument, (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definitions of empowering legislation and empowering provision |
| 60 | s5.def.instrument | defined term: instrument | encoded | nz-glossary.l4: entry for instrument (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definition of instrument |
| 61 | s5.def.introduction, in relation to a Bill, | defined term: introduction, in relation to a Bill, | encoded | nz-glossary.l4: entry for introduction, in relation to a Bill, (tested in nz-tests-glossary.l4) |
| 62 | s5.def.legislation | defined term: legislation | encoded | nz-glossary.l4: entry for legislation (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definition of legislation |
| 63 | s5.def.legislation website | defined term: legislation website | encoded | nz-glossary.l4: entry for legislation website (tested in nz-tests-glossary.l4) |
| 64 | s5.def.maker, in relation to any secondary legislation or instrument, | defined term: maker, in relation to any secondary legislation or instrument, | encoded | nz-glossary.l4: entry for maker, in relation to any secondary legislation or instrument, (tested in nz-tests-glossary.l4) |
| 65-69 | s5.def.minimum legislative information | defined term: minimum legislative information | encoded | nz-glossary.l4: entry for minimum legislative information (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definition of minimum legislative information |
| 70 | s5.def.official version, in relation to legislation, | defined term: official version, in relation to legislation, | encoded | nz-glossary.l4: entry for official version, in relation to legislation, (tested in nz-tests-glossary.l4) |
| 71 | s5.def.PCO | defined term: PCO | encoded | nz-glossary.l4: entry for PCO (tested in nz-tests-glossary.l4) |
| 72 | s5.def.presentation exemption | defined term: presentation exemption | encoded | nz-glossary.l4: entry for presentation exemption (tested in nz-tests-glossary.l4) |
| 73 | s5.def.referential words, in subpart 2 of Part 3, | defined term: referential words, in subpart 2 of Part 3, | encoded | nz-glossary.l4: entry for referential words, in subpart 2 of Part 3, (tested in nz-tests-glossary.l4) |
| 74 | s5.def.release, in relation to an amendment to a Bill, | defined term: release, in relation to an amendment to a Bill, | encoded | nz-glossary.l4: entry for release, in relation to an amendment to a Bill, (tested in nz-tests-glossary.l4) |
| 75-77 | s5.def.secondary legislation | defined term: secondary legislation | encoded | nz-glossary.l4: entry for secondary legislation (tested in nz-tests-glossary.l4); nz-part1-preliminary.l4: s 5(1), definition of secondary legislation |
| 78-79 | s5.ex.78 | example: The ABC Act 2018 enables the Governor-General, by  | encoded | nz-tests-part1.l4 (the ABC Act example, quoted lines 75-79) -- an example, tested as a case |
| 80 | s5.def.sitting day | defined term: sitting day | encoded | nz-glossary.l4: entry for sitting day (tested in nz-tests-glossary.l4); nz-interpretation-time.l4: ss 5(1) and 13; nz-part5-oversight.l4: s 5(1), definition of sitting day |
| 81 | s5.2 | In this Act, a reference to the maker of any secondary legislation or  | encoded | nz-part1-preliminary.l4: s 5(2) |
| 82 | s5.3 | See also the definitions of terms for all legislation in section 13, w | encoded | nz-part1-preliminary.l4: s 5(3) |
| 83-84 | s6.1 | 6 Transitional, savings, and related provisions | encoded | nz-part1-preliminary.l4: s 6 |
| 85-86 | s7.1 | 7 Act binds the Crown | encoded | nz-part1-preliminary.l4: s 7 |
| 87 | h87 | Part 2 — Interpretation and application of legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 88 | h88 | Purposes and application | inert (1: not operative) | heading -- a heading creates no rule |
| 89-92 | s8.1 | 8 Purposes of this Part | inert (1: not operative) | not operative -- s 8: purposes clause, creates no rule |
| 93-96 | s9.1 | 9 Application of this Part | encoded | nz-part2-principles.l4: s 9(1) |
| 97 | s9.2 | The provisions of this Part also apply to the interpretation of this A | encoded | nz-part2-principles.l4: s 9(2) |
| 98 | h98 | General principles of interpretation | inert (1: not operative) | heading -- a heading creates no rule |
| 99-100 | s10.1 | 10 How to ascertain meaning of legislation | encoded | nz-part2-principles.l4: s 10(1) |
| 101 | s10.2 | Subsection (1) applies whether or not the legislation’s purpose is sta | encoded | nz-part2-principles.l4: s 10(2) |
| 102 | s10.3 | The text of legislation includes the indications provided in the legis | encoded | nz-part2-principles.l4: s 10(3) and (4) |
| 103 | s10.4 | Examples of those indications are preambles, a table of contents, head | encoded | nz-part2-principles.l4: s 10(3) and (4) |
| 104-105 | s11.1 | 11 Legislation applies to circumstances as they arise | encoded | nz-part2-principles.l4: s 11 |
| 106-107 | s12.1 | 12 Legislation does not have retrospective effect | fork | fork F7 -- s 12 is a provision of Part 2, so s 9(1)(a) lets the legislation provide otherwise: rule s 12 `legislation applies to a circumstance as it arises` and its reading in nz-part2-principles.l4 |
| 108 | h108 | General definitions and interpretation provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 109-110 | s13.1 | 13 Definitions of terms for all legislation | encoded | nz-glossary.l4: the scope 'in legislation' is the field `the provision that defines it` of each section 13 entry -- lead-in words |
| 111-113 | s13.def.Act | defined term: Act | encoded | nz-glossary.l4: entry for Act (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Act |
| 114 | s13.def.commencement, in relation to any legislation, | defined term: commencement, in relation to any legislation, | encoded | nz-glossary.l4: entry for commencement, in relation to any legislation, (tested in nz-tests-glossary.l4) |
| 115 | s13.def.Commonwealth country and part of the Commonwealth | defined term: Commonwealth country and part of the Commonwealth | encoded | nz-glossary.l4: entry for Commonwealth country and part of the Commonwealth (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Commonwealth country and part of the Commonwealth; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 116 | s13.def.consular officer | defined term: consular officer | encoded | nz-glossary.l4: entry for consular officer (tested in nz-tests-glossary.l4) |
| 117 | s13.def.de facto partner | defined term: de facto partner | encoded | nz-glossary.l4: entry for de facto partner (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of de facto partner |
| 118 | s13.def.department, in relation to any legislation, | defined term: department, in relation to any legislation, | encoded | nz-glossary.l4: entry for department, in relation to any legislation, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definitions of department and Ministry |
| 119 | s13.def.enactment | defined term: enactment | encoded | nz-glossary.l4: entry for enactment (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of enactment |
| 120 | s13.def.Gazette | defined term: Gazette | encoded | nz-glossary.l4: entry for Gazette (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Gazette |
| 121 | s13.def.Governor-General in Council or a similar expression | defined term: Governor-General in Council or a similar expression | encoded | nz-glossary.l4: entry for Governor-General in Council or a similar expression (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Governor-General in Council; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 122 | s13.def.legislation | defined term: legislation | encoded | nz-glossary.l4: entry for legislation (tested in nz-tests-glossary.l4) |
| 123 | s13.def.legislation website | defined term: legislation website | encoded | nz-glossary.l4: entry for legislation website (tested in nz-tests-glossary.l4) |
| 124 | s13.def.maker | defined term: maker | encoded | nz-glossary.l4: entry for maker (tested in nz-tests-glossary.l4) |
| 125 | s13.def.Minister, in relation to any legislation, | defined term: Minister, in relation to any legislation, | encoded | nz-glossary.l4: entry for Minister, in relation to any legislation, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Minister |
| 126 | s13.def.Ministry, in relation to any legislation, | defined term: Ministry, in relation to any legislation, | encoded | nz-glossary.l4: entry for Ministry, in relation to any legislation, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definitions of department and Ministry |
| 127 | s13.def.month | defined term: month | encoded | nz-glossary.l4: entry for month (tested in nz-tests-glossary.l4); nz-interpretation-time.l4: s 13, definition of month; nz-interpretation-time.l4: ss 5(1) and 13 -- month is the only unit of time s 13 defines; the Act is silent on day, week and year (forks F5 and F6) |
| 128-130 | s13.def.New Zealand or similar words | defined term: New Zealand or similar words | encoded | nz-glossary.l4: entry for New Zealand or similar words (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of New Zealand; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 131 | s13.def.North Island or Te Ika-a-Māui, both official alternative names, | defined term: North Island or Te Ika-a-Māui, both official alternative names, | encoded | nz-glossary.l4: entry for North Island or Te Ika-a-Māui, both official alternative names, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definitions of North Island and South Island; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 132 | s13.def.office | defined term: office | encoded | nz-glossary.l4: entry for office (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of office |
| 133 | s13.def.Order in Council | defined term: Order in Council | encoded | nz-glossary.l4: entry for Order in Council (tested in nz-tests-glossary.l4) |
| 134 | s13.def.person | defined term: person | encoded | nz-glossary.l4: entry for person (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of person |
| 135 | s13.def.prescribed | defined term: prescribed | encoded | nz-glossary.l4: entry for prescribed (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of prescribed |
| 136 | s13.def.presentation exemption | defined term: presentation exemption | encoded | nz-glossary.l4: entry for presentation exemption (tested in nz-tests-glossary.l4) |
| 137-139 | s13.def.proceeding | defined term: proceeding | encoded | nz-glossary.l4: entry for proceeding (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of proceeding |
| 140 | s13.def.Proclamation | defined term: Proclamation | encoded | nz-glossary.l4: entry for Proclamation (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of Proclamation |
| 141-144 | s13.def.public notification, public notice, or a similar expression in relation to an act, a matter, or a thing, | defined term: public notification, public notice, or a similar expression in relation to an act, a matter, or a thing, | encoded | nz-glossary.l4: entry for public notification, public notice, or a similar expression in relation to an act, a matter, or a thing, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of public notification; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 145-148 | s13.def.repeal, in relation to any legislation, | defined term: repeal, in relation to any legislation, | encoded | nz-glossary.l4: entry for repeal, in relation to any legislation, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of repeal |
| 149 | s13.def.rules of court, in relation to a court, | defined term: rules of court, in relation to a court, | encoded | nz-glossary.l4: entry for rules of court, in relation to a court, (tested in nz-tests-glossary.l4) |
| 150 | s13.def.secondary legislation | defined term: secondary legislation | encoded | nz-glossary.l4: entry for secondary legislation (tested in nz-tests-glossary.l4) |
| 151 | s13.def.South Island or Te Waipounamu, both official alternative names, | defined term: South Island or Te Waipounamu, both official alternative names, | encoded | nz-glossary.l4: entry for South Island or Te Waipounamu, both official alternative names, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definitions of North Island and South Island; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 152 | s13.def.territorial limits of New Zealand, limits of New Zealand, or a similar expression, when used as a territorial description, | defined term: territorial limits of New Zealand, limits of New Zealand, or a similar expression, when used as a territorial description, | encoded | nz-glossary.l4: entry for territorial limits of New Zealand, limits of New Zealand, or a similar expression, when used as a territorial description, (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of territorial limits of New Zealand; nz-part2-definitions.l4: s 13, definitions of public notification, Governor-General in Council, New Zealand, North Island, South Island, territorial limits of New Zealand, Commonwealth country |
| 153-158 | s13.def.working day | defined term: working day | encoded | nz-glossary.l4: entry for working day (tested in nz-tests-glossary.l4); nz-interpretation-time.l4: s 13, definition of working day, limbs (a) weekend; nz-interpretation-time.l4: s 13, definition of working day; nz-interpretation-time.l4: ss 5(1) and 13; nz-interpretation-time.l4: s 13, definition of working day, limb (b); nz-interpretation-time.l4: s 13, definition of working day, limbs (c) and (d); nz-interpretation-time.l4: s 13, definition of working day, limb (e) |
| 159 | s13.def.writing | defined term: writing | encoded | nz-glossary.l4: entry for writing (tested in nz-tests-glossary.l4); nz-part2-definitions.l4: s 13, definition of writing |
| 160-164 | s14.1 | 14 Meaning of de facto relationship | encoded | nz-part2-definitions.l4: s 14(1) and (2) |
| 165 | s14.2 | However, a relationship involving a person aged 16 or 17 years is not  | encoded | nz-part2-definitions.l4: s 14(1) and (2) |
| 166-168 | s14.3 | In determining whether 2 people live together as a couple in a relatio | encoded | nz-part2-definitions.l4: s 14(3) |
| 169-171 | s14.4 | A de facto relationship ends if— | encoded | nz-part2-definitions.l4: s 14(4) |
| 172-173 | s15.1 | 15 Meaning of step-parent, etc | encoded | nz-part2-definitions.l4: s 15 |
| 174-175 | s16.1 | 16 References to specific gender or kind of person include others | encoded | nz-part2-definitions.l4: s 16(1) |
| 176 | s16.2 | Words denoting a natural person by referring to a gender (for example, | encoded | nz-part2-definitions.l4: s 16(2) and (3) |
| 177 | s16.3 | Words denoting a corporation sole, a body corporate, or an unincorpora | encoded | nz-part2-definitions.l4: s 16(2) and (3) |
| 178-179 | s17.1 | 17 When sending by post is taken as done | encoded | nz-interpretation-time.l4: s 17(1), (2) and (4) |
| 180 | s17.2 | The document is taken to be sent if it is properly addressed, prepaid, | encoded | nz-interpretation-time.l4: s 17(1), (2) and (4) |
| 181 | s17.3 | The document is taken to be received at the time at which it would be  | encoded | nz-interpretation-time.l4: s 17(3) and (4) |
| 182 | s17.4 | However, subsection (2) or (3) does not apply if the contrary is prove | encoded | nz-interpretation-time.l4: s 17(1), (2) and (4); nz-interpretation-time.l4: s 17(3) and (4) |
| 183 | s17.5 | See also Part 4 of the Contract and Commercial Law Act 2017, which pro | encoded | nz-interpretation-time.l4: s 17(5) |
| 184-185 | s18.1 | 18 Parts of speech have corresponding meaning | encoded | nz-part2-definitions.l4: s 18 |
| 186-187 | s19.1 | 19 Words in singular include plural and vice versa | encoded | nz-part2-definitions.l4: s 19 |
| 188-189 | s20.1 | 20 Words used in secondary legislation or other instruments have same  | encoded | nz-part2-definitions.l4: s 20 |
| 190-191 | s21.1 | 21 Anything done under secondary legislation or other instrument is al | encoded | nz-part2-definitions.l4: s 21 |
| 192-193 | s21.ex.192 | example: An Act empowers regulations to authorise a regulat | encoded | nz-tests-part2-definitions.l4 (the regulator's notice example, quoted lines 190-193) -- an example, tested as a case |
| 194-195 | s22.1 | 22 Legislation not binding on the Crown | encoded | nz-part2-definitions.l4: s 22(1) |
| 196-198 | s22.2 | No secondary legislation, or part of secondary legislation, made under | encoded | nz-part2-definitions.l4: s 22(2) |
| 199-200 | s23.1 | 23 Examples do not limit provision | encoded | nz-part2-definitions.l4: s 23 |
| 201 | s23.2 | See section 10, which includes examples as part of the text of legisla | encoded | nz-part2-definitions.l4: s 23 |
| 202 | h202 | Commencement of legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 203-207 | s24.1 | 24 Outline of commencement provisions | inert (1: not operative) | not operative -- s 24(1): outline of ss 25 to 29 |
| 208 | s24.2 | Subsection (1) is a guide only to the general scheme and effect of the | inert (1: not operative) | not operative -- s 24(2): says it is a guide only |
| 209-210 | s25.1 | 25 Date on which Acts commence | encoded | nz-interpretation-time.l4: s 25 |
| 211 | s25.2 | If an Act does not state or provide for a commencement date for the Ac | encoded | nz-interpretation-time.l4: s 25 |
| 212 | s25.3 | However, an Act’s Title and commencement sections, and any principal l | encoded | nz-interpretation-time.l4: s 25; nz-interpretation-time.l4: s 25(3) |
| 213 | s25.4 | In subsection (3), principal legislation provision means a section or  | encoded | nz-interpretation-time.l4: s 25 |
| 214-215 | s26.1 | 26 Date on which secondary legislation commences | encoded | nz-interpretation-time.l4: s 26 |
| 216 | s26.2 | If it does not state or provide for that date, the legislation or part | encoded | nz-interpretation-time.l4: s 26 |
| 217 | s26.3 | However, the secondary legislation’s Title and commencement provisions | encoded | nz-interpretation-time.l4: s 26; nz-interpretation-time.l4: s 26(3) |
| 218-222 | s27.1 | 27 Time at which legislation commences | fork | fork F3 -- s 27(b) 'from a day' and (c) 'a particular time' both apply: the text does not say which prevails; NOTHING (nz-interpretation-time.l4) |
| 223-224 | s28.1 | 28 When legislation commences if calculated by number of months | encoded | nz-interpretation-time.l4: s 28 |
| 225-227 | s28.2 | The legislation comes into force in the month that is that number of m | encoded | nz-interpretation-time.l4: s 28 |
| 228 | s28.3 | This section applies instead of section 56 (on months generally). | encoded | nz-interpretation-time.l4: s 28 |
| 229-231 | s28.ex.229 | example: ABC Act 2020 states that it comes into force a mon | encoded | nz-interpretation-time.l4: s 28 |
| 232-237 | s29.1 | 29 Power to make commencement order | fork | fork F8 -- a re-exercise on the same day as the commencement: not before it unless the order states a time and the re-exercise takes effect before that time (nz-part2-commencement-repeal.l4) |
| 238-239 | s29.ex.238 | example: The Dogs and Cats Act 2020 states that it comes in | encoded | nz-tests-part2-commencement-repeal.l4 (the Dogs and Cats Act 2020 example, quoted lines 238-239) -- an example, tested as a case |
| 240 | s29.2 | If the power referred to in subsection (1)﻿(d) is exercised, the provi | encoded | nz-part2-commencement-repeal.l4: s 29(1)(d) and (2) |
| 241 | h241 | Amendment and repeal | inert (1: not operative) | heading -- a heading creates no rule |
| 242-243 | s30.1 | 30 Amendments part of, and construed with, legislation amended | encoded | nz-part2-commencement-repeal.l4: s 30(1) |
| 244 | s30.2 | Amending legislation must be construed with the legislation that it am | encoded | nz-part2-commencement-repeal.l4: s 30(2) |
| 245-249 | s31.1 | 31 References to repeal or amendment extend to other ceasing of effect | encoded | nz-part2-commencement-repeal.l4: s 31 |
| 250-256 | s32.1 | 32 Effect of repeal or amendment generally | encoded | nz-part2-commencement-repeal.l4: s 32 |
| 257-259 | s32.2 | The repeal of legislation does not revive— | encoded | nz-part2-commencement-repeal.l4: s 32 |
| 260-264 | s33.1 | 33 Effect of repeal or amendment on existing rights and proceedings | encoded | nz-part2-commencement-repeal.l4: s 33(1)(a); nz-part2-commencement-repeal.l4: s 33(1)(b); nz-part2-commencement-repeal.l4: s 33(1)(c) |
| 265 | s33.2 | Repealed or amended legislation continues to have effect for the purpo | encoded | nz-part2-commencement-repeal.l4: s 33(2) |
| 266-267 | s34.1 | 34 Effect of repeal or amendment on prior offences and breaches of leg | fork | fork F9 -- an offence on the day the repeal takes effect is not before it (repeal takes effect at the start of the day) (nz-part2-commencement-repeal.l4) |
| 268-271 | s34.2 | Repealed or amended legislation continues to have effect as if it had  | fork | fork F9 -- the same reading, for the continuing use of the old law (nz-part2-commencement-repeal.l4) |
| 272-275 | s35.1 | 35 Powers exercised under repealed or amended legislation have continu | encoded | nz-part2-commencement-repeal.l4: s 35 |
| 276-279 | s36.1 | 36 Legislation made under repealed legislation has continuing effect | encoded | nz-part2-commencement-repeal.l4: s 36(1) |
| 280 | s36.2 | Legislation that continues in force may be amended or revoked as if it | encoded | nz-part2-commencement-repeal.l4: s 36(2) |
| 281-284 | s37.1 | 37 How to apply references to new legislation that is not yet in force | encoded | nz-part2-commencement-repeal.l4: s 37 |
| 285 | s37.2 | A reference in legislation to the new legislation is, until that new l | encoded | nz-part2-commencement-repeal.l4: s 37 |
| 286-287 | s38.1 | 38 How to apply references to repealed legislation | encoded | nz-part2-commencement-repeal.l4: s 38 |
| 288 | s38.2 | A reference in legislation to repealed legislation is a reference to l | encoded | nz-part2-commencement-repeal.l4: s 38 |
| 289 | s38.3 | Subsection (1) is subject to subsection (2). | encoded | nz-part2-commencement-repeal.l4: s 38 |
| 290-291 | s39.1 | 39 Time of repeal of legislation on particular day | encoded | nz-interpretation-time.l4: s 39(1) |
| 292 | s39.2 | Legislation that is expressed to remain in force, or to continue to ha | encoded | nz-interpretation-time.l4: s 39(2) |
| 293 | h293 | General empowering provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 294-295 | s40.1 | 40 Authority to make secondary legislation | encoded | nz-part2-powers.l4: s 40(1) |
| 296 | s40.2 | Secondary legislation is not invalid just because the legislation unde | encoded | nz-part2-powers.l4: s 40(2) |
| 297-298 | s41.1 | 41 Secondary legislation may make consequential amendments to other se | encoded | nz-part2-powers.l4: s 41(1) and (2) |
| 299-301 | s41.2 | An amendment is consequential for the purposes of this section if it i | encoded | nz-part2-powers.l4: s 41(1) and (2) |
| 302 | s41.3 | The only facts, circumstances, or preconditions that must exist or be  | encoded | nz-part2-powers.l4: s 41(3) |
| 303-304 | s42.1 | 42 Amendments made to secondary legislation by Act do not prevent late | encoded | nz-part2-powers.l4: s 42 |
| 305 | h305 | Exercise of powers in legislation generally | inert (1: not operative) | heading -- a heading creates no rule |
| 306-313 | s43.1 | 43 When powers can be exercised before commencement | encoded | nz-part2-powers.l4: s 43(1) and (2) |
| 314-316 | s43.2 | However, the power may be exercised only if the exercise of the power  | encoded | nz-part2-powers.l4: s 43(1) and (2) |
| 317-319 | s43.3 | Subsection (1) applies as if— | encoded | nz-part2-powers.l4: s 43(3)(a); nz-part2-powers.l4: s 43(3)(b) |
| 320-321 | s44.1 | 44 Limit on when pre-commencement exercise of powers takes effect | encoded | nz-part2-powers.l4: s 44 |
| 322-325 | s44.2 | However, that limit does not apply if the exercise of the power is nec | encoded | nz-part2-powers.l4: s 44 |
| 326-335 | s45.1 | 45 Power to appoint person to an office includes related powers | encoded | nz-part2-powers.l4: s 45 |
| 336-337 | s46.1 | 46 Power to do things may be exercised to correct errors | encoded | nz-part2-powers.l4: s 46 |
| 338 | s46.2 | Subsection (1) applies even though the power is not generally capable  | encoded | nz-part2-powers.l4: s 46 |
| 339-342 | s47.1 | 47 Powers of office holder may be exercised by acting office holders | encoded | nz-part2-powers.l4: s 47 |
| 343-346 | s48.1 | 48 Power to make includes power to amend or revoke | encoded | nz-part2-powers.l4: s 48(1) |
| 347 | s48.2 | Requirements that apply in relation to making the secondary legislatio | encoded | nz-part2-powers.l4: s 48(2) |
| 348-349 | s49.1 | 49 Power to make different provision for classes of matters | encoded | nz-part2-powers.l4: s 49 |
| 350-352 | s49.2 | The power includes a power— | encoded | nz-part2-powers.l4: s 49 |
| 353-356 | s50.1 | 50 Power to identify matters using classes | encoded | nz-part2-powers.l4: s 50 |
| 357 | s50.2 | In exercising the power, the person may identify the matter by referri | encoded | nz-part2-powers.l4: s 50 |
| 358-359 | s51.1 | 51 Exercise or performance of powers, functions, and duties more than  | encoded | nz-part2-powers.l4: s 51 |
| 360 | s51.2 | A duty or function imposed by legislation may be performed from time t | encoded | nz-part2-powers.l4: s 51 |
| 361 | h361 | Forms | inert (1: not operative) | heading -- a heading creates no rule |
| 362-363 | s52.1 | 52 Use of approved or prescribed forms | encoded | nz-part2-powers.l4: s 52 |
| 364-365 | s53.1 | 53 Extension of power to approve or prescribe forms | encoded | nz-part2-powers.l4: s 53(1) and (2) |
| 366-369 | s53.2 | Power A includes a power (power B) to do any 1 or more of the followin | encoded | nz-part2-powers.l4: s 53(1) and (2) |
| 370 | s53.3 | Power B may be exercised in place of, or as well as, power A. | encoded | nz-part2-powers.l4: s 53(3) and (4) |
| 371 | s53.4 | Information supplied or made available under power B complies with leg | encoded | nz-part2-powers.l4: s 53(3) and (4) |
| 372-375 | s53.5 | Subsection (6) applies if— | encoded | nz-part2-powers.l4: s 53(5) and (6) |
| 376-378 | s53.6 | If this subsection applies,— | encoded | nz-part2-powers.l4: s 53(5) and (6) |
| 379 | h379 | Time and distance | inert (1: not operative) | heading -- a heading creates no rule |
| 380-381 | s54.1 | 54 When periods start and end | encoded | nz-interpretation-time.l4: ss 54 and 56 -- the table's rule cells are not in the deposited text (finding 1); the Act does not define a week or a year, so a period in weeks or years has no answer here (forks F5 and F6): NOTHING, asserted |
| 382 | s54.2 | Examples | encoded | nz-interpretation-time.l4: ss 54 and 56 |
| 383 | s54.tbl.383 | table row: Item 1: If the legislation states that a permissio | fork | fork F1 -- Item 1 'begins on' includes the day; the rule is read from the example (nz-interpretation-time.l4: `the first day of a period that is`) |
| 384 | s54.tbl.384 | table row: Item 2: If the legislation states that a variation | fork | fork F2 -- Item 2 'from' a day starts the next day, and s 56 example 3 equates 'after' (nz-interpretation-time.l4: `the first day of a period that is`) |
| 385 | s54.tbl.385 | table row: Item 3: If the legislation states that public noti | fork | fork F2 -- Item 3 'within N days of' an event excludes the event's day and ends at the close of the day N after it (nz-interpretation-time.l4: `the last day of a period of days`) |
| 386 | s54.tbl.386 | table row: Item 4: If the legislation states that a right to  | fork | fork F1 -- Item 4 'ends on' includes the day (nz-interpretation-time.l4: `the last day of a period that is`) |
| 387 | s54.tbl.387 | table row: Item 5: If the legislation states that a permissio | fork | fork F1 -- Item 5 'continues until' includes the day (nz-interpretation-time.l4: `the last day of a period that is`) |
| 388 | s54.tbl.388 | table row: Item 6: If the legislation states that a statement | fork | fork F1 -- Item 6 'before the start of' a day stops the day before (nz-interpretation-time.l4: `the last day of a period that is`) |
| 389 | s54.tbl.389 | table row: Item 7: If the legislation states that the period  | fork | fork F1 -- Item 7 'at least N working days between': neither end day is counted (nz-interpretation-time.l4: `the earliest day for the second event if at least`) |
| 390-391 | s55.1 | 55 Extension for doing thing if day or last day is not working day | fork | fork F4 -- s 55 says 'a limited period of time', so it reaches periods of months and years, not only days (nz-interpretation-time.l4) |
| 392-396 | s56.1 | 56 Calculating periods of months (except for commencement of legislati | encoded | nz-interpretation-time.l4: s 56; nz-interpretation-time.l4: ss 54 and 56 -- s 56 speaks only of months; the Act is silent on a period of weeks or years (forks F5 and F6): NOTHING, asserted |
| 397-400 | s56.ex.397 | example: If the legislation refers to a period of 1 month s | encoded | nz-interpretation-time.l4: s 56; nz-interpretation-time.l4: ss 54 and 56 |
| 401 | s56.2 | This section does not apply to commencement of legislation (see sectio | encoded | nz-interpretation-time.l4: s 56; nz-interpretation-time.l4: ss 54 and 56 |
| 402-403 | s57.1 | 57 Determining time generally | encoded | nz-interpretation-time.l4: s 57 |
| 404-405 | s58.1 | 58 Determining measurements of distance | encoded | nz-interpretation-time.l4: s 58 |
| 406 | h406 | Revision Acts | inert (1: not operative) | heading -- a heading creates no rule |
| 407-410 | s59.1 | 59 Meaning of revision Act and old law | encoded | nz-part2-revision-incorporation.l4: s 59, definition of old law; nz-part2-revision-incorporation.l4: s 59, definition of revision Act |
| 411-414 | s60.1 | 60 Revision Act is generally to have same effect as old law | encoded | nz-part2-revision-incorporation.l4: s 60 |
| 415 | s60.2 | This section is subject to section 62. | encoded | nz-part2-revision-incorporation.l4: s 60 |
| 416-417 | s61.1 | 61 Using old law as interpretation guide for revision Act | encoded | nz-part2-revision-incorporation.l4: s 61 |
| 418-422 | s62.1 | 62 Exceptions: when revision Act changes effect of old law | encoded | nz-part2-revision-incorporation.l4: s 62 |
| 423 | h423 | Power to incorporate by reference | inert (1: not operative) | heading -- a heading creates no rule |
| 424-425 | s63.1 | 63 Interpretation | encoded | nz-glossary.l4: `a definition in the Act governs the use of the term`; the scope 'sections 64 to 66 and Schedule 2' is in each entry's field -- lead-in words |
| 426-428 | s63.def.material | defined term: material | encoded | nz-glossary.l4: entry for material (tested in nz-tests-glossary.l4); nz-part2-revision-incorporation.l4: s 63, definition of material |
| 429-431 | s63.def.written material | defined term: written material | encoded | nz-glossary.l4: entry for written material (tested in nz-tests-glossary.l4); nz-part2-revision-incorporation.l4: s 63, definition of written material |
| 432-438 | s64.1 | 64 Power for secondary legislation to incorporate material by referenc | encoded | nz-part2-revision-incorporation.l4: s 64(1) |
| 439-441 | s64.2 | For the purposes of this section, secondary legislation incorporates m | encoded | nz-part2-revision-incorporation.l4: s 64(2) |
| 442 | s64.3 | Material incorporated by reference in reliance on this section has leg | encoded | nz-part2-revision-incorporation.l4: s 64(3) |
| 443-446 | s64.4 | This provision applies in addition to, and does not limit, any of the  | encoded | nz-part2-revision-incorporation.l4: s 64(4) |
| 447-448 | s65.1 | 65 Schedule 2 applies if material incorporated by reference | encoded | nz-part2-revision-incorporation.l4: s 65 |
| 449-450 | s66.1 | 66 Effect of amendments to material incorporated by reference | encoded | nz-part2-revision-incorporation.l4: s 66(1) and (2) |
| 451-453 | s66.2 | Those amendments have no legal effect as part of the secondary legisla | encoded | nz-part2-revision-incorporation.l4: s 66(1) and (2) |
| 454-457 | s66.3 | For the purposes of this section, material is amended if the material  | encoded | nz-part2-revision-incorporation.l4: s 66(3) |
| 458 | h458 | Part 3 — Drafting and publishing of legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 459 | h459 | Subpart 1 — Drafting and publishing legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 460 | h460 | Key drafting responsibilities | inert (1: not operative) | heading -- a heading creates no rule |
| 461-471 | s67.1 | 67 What legislation is drafted by PCO | encoded | nz-part3-publication.l4: s 67 |
| 472-473 | s68.1 | 68 Power to authorise IRD to draft Inland Revenue Bills | encoded | nz-part3-publication.l4: s 68(1) to (3) |
| 474 | s68.2 | The Order in Council may state exceptions to the authorisation. | encoded | nz-part3-publication.l4: s 68(1) to (3) |
| 475 | s68.3 | The Order in Council is secondary legislation (see this Part for publi | encoded | nz-part3-publication.l4: s 68(1) to (3); nz-part3-publication.l4: s 68(3) |
| 476 | s68.4 | In this section,— | encoded | nz-glossary.l4: the scope 'this section' is the field `the provision that defines it` of the two section 68(4) entries -- lead-in words |
| 477 | s68.def.Inland Revenue Bills | defined term: Inland Revenue Bills | encoded | nz-glossary.l4: entry for Inland Revenue Bills (tested in nz-tests-glossary.l4) |
| 478 | s68.def.responsible Minister | defined term: responsible Minister | encoded | nz-glossary.l4: entry for responsible Minister (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 68(1) to (3) |
| 479 | h479 | Key publishing responsibilities | inert (1: not operative) | heading -- a heading creates no rule |
| 480-485 | s69.1 | 69 PCO must publish all legislation | encoded | nz-part3-publication.l4: s 69(1) |
| 486 | s69.2 | The PCO must also notify the making of that secondary legislation by p | encoded | nz-part3-publication.l4: s 69(2) |
| 487-490 | s69.3 | The PCO may also publish secondary legislation that was not drafted by | encoded | nz-part3-publication.l4: s 69(3) |
| 491-494 | s70.1 | 70 PCO must publish consolidations of legislation that is amended | encoded | nz-part3-publication.l4: s 70(1) |
| 495 | s70.2 | A consolidation must incorporate the amendments made to the legislatio | encoded | nz-part3-publication.l4: s 70(2) and (3) |
| 496 | s70.3 | The consolidation may also show the law as it would be amended by amen | encoded | nz-part3-publication.l4: s 70(2) and (3) |
| 497-498 | s71.1 | 71 How and when PCO must publish legislation and consolidations of leg | encoded | nz-part3-publication.l4: s 71(1) |
| 499-500 | s71.tbl.499 | table row: What is required to be published | encoded | nz-part3-publication.l4: s 71(1) |
| 501-502 | s71.tbl.501 | table row: Bills | encoded | nz-part3-publication.l4: s 71(1) |
| 503-504 | s71.tbl.503 | table row: Amendments to Bills | encoded | nz-part3-publication.l4: s 71(1) |
| 505-506 | s71.tbl.505 | table row: Acts | encoded | nz-part3-publication.l4: s 71(1) |
| 507-508 | s71.tbl.507 | table row: Secondary legislation drafted by the PCO | encoded | nz-part3-publication.l4: s 71(1) |
| 509-510 | s71.tbl.509 | table row: Minimum legislative information for secondary legi | encoded | nz-part3-publication.l4: s 71(1) |
| 511-512 | s71.tbl.511 | table row: Consolidations of Acts | encoded | nz-part3-publication.l4: s 71(1) |
| 513-514 | s71.tbl.513 | table row: Consolidations of secondary legislation that is dr | encoded | nz-part3-publication.l4: s 71(1) |
| 515 | s71.2 | The PCO may also publish those things in printed form and make them av | encoded | nz-part3-publication.l4: s 71(2) |
| 516 | s71.3 | Legislation or proposed legislation is sufficiently published for the  | encoded | nz-part3-publication.l4: s 71(3) |
| 517 | s71.4 | Minimum legislative information is sufficiently published for the purp | encoded | nz-part3-publication.l4: s 71(4) |
| 518-521 | s72.1 | 72 How and when electronic versions of legislation must be available o | encoded | nz-part3-publication.l4: s 72(1)(b); nz-part3-publication.l4: s 72(1)(a) |
| 522 | h522 | Other provisions applying to secondary legislation not published by PC | inert (1: not operative) | heading -- a heading creates no rule |
| 523-524 | s73.1 | 73 Maker must publish secondary legislation not published by PCO (if r | encoded | nz-part3-publication.l4: s 73(1) |
| 525 | s73.2 | The maker of the secondary legislation must comply with the applicable | encoded | nz-part3-publication.l4: s 73(2) and (3); nz-part3-publication.l4: s 73(2) |
| 526 | s73.3 | For the purpose of this Act and any other legislation, the secondary l | encoded | nz-part3-publication.l4: s 73(2) and (3) |
| 527-531 | s74.1 | 74 Applicable publication requirements for secondary legislation not p | encoded | nz-part3-publication.l4: s 74(1) |
| 532 | s74.2 | In addition, if section 75 applies to the secondary legislation, the a | encoded | nz-part3-publication.l4: s 74(2) |
| 533-536 | s75.1 | 75 Additional applicable publication requirements for secondary legisl | encoded | nz-part3-publication.l4: s 75(1) |
| 537-541 | s75.2 | The additional applicable publication requirements for secondary legis | encoded | nz-part3-publication.l4: s 75(2) |
| 542-545 | s75.3 | Subsection (2)﻿(b) is taken to be satisfied if— | encoded | nz-part3-publication.l4: s 75(3) |
| 546-549 | s76.1 | 76 Chief Parliamentary Counsel must support international transparency | encoded | nz-part3-publication.l4: s 76(1) |
| 550-552 | s76.2 | The Chief Parliamentary Counsel must give all or any makers, and ensur | encoded | nz-part3-publication.l4: s 76(2) |
| 553 | s76.3 | The maker must, if required to do so in writing by the Chief Parliamen | encoded | nz-part3-publication.l4: s 76(3) |
| 554 | s76.4 | A direction under this section is secondary legislation (see this Part | encoded | nz-part3-publication.l4: s 76(4) |
| 555-556 | s77.1 | 77 Definitions for purposes of international transparency obligations | encoded | nz-glossary.l4: the scope 'this section and sections 74 to 76' is the field `the provision that defines it` of each section 77 entry -- lead-in words |
| 557 | s77.def.details, for any secondary legislation at any time, | defined term: details, for any secondary legislation at any time, | encoded | nz-glossary.l4: entry for details, for any secondary legislation at any time, (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 77, definition of details |
| 558-560 | s77.def.international transparency obligations | defined term: international transparency obligations | encoded | nz-glossary.l4: entry for international transparency obligations (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 77, definition of international transparency obligations |
| 561 | s77.def.links, in relation to any secondary legislation at any time, | defined term: links, in relation to any secondary legislation at any time, | encoded | nz-glossary.l4: entry for links, in relation to any secondary legislation at any time, (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 77, definition of links |
| 562 | s77.def.maker’s website | defined term: maker’s website | encoded | nz-glossary.l4: entry for maker’s website (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 77, definition of maker's website |
| 563-568 | s77.def.relevant central government entity | defined term: relevant central government entity | encoded | nz-glossary.l4: entry for relevant central government entity (tested in nz-tests-glossary.l4); nz-part3-publication.l4: s 77, definition of relevant central government entity |
| 569 | h569 | Official versions and related matters | inert (1: not operative) | heading -- a heading creates no rule |
| 570-573 | s78.1 | 78 Official versions of legislation | encoded | nz-part3-publication.l4: s 78 |
| 574 | s78.2 | A printed version of legislation that is produced directly from an off | encoded | nz-part3-publication.l4: s 78 |
| 575 | s78.3 | An electronic or a printed document that is identified as an official  | encoded | nz-part3-publication.l4: s 78 |
| 576-582 | s79.1 | 79 Legal status of official versions | encoded | nz-part3-publication.l4: s 79(1) and (3) |
| 583 | s79.2 | An official version of secondary legislation that states the date of p | encoded | nz-part3-publication.l4: s 79(2) and (3) |
| 584 | s79.3 | The presumptions in this section apply unless the contrary is shown. | encoded | nz-part3-publication.l4: s 79(1) and (3); nz-part3-publication.l4: s 79(2) and (3) |
| 585-590 | s79A.1 | 79A Legislative status of publication notes and information | encoded | nz-part3-publication.l4: s 79A |
| 591-592 | s80.1 | 80 Evidential status of minimum legislative information | encoded | nz-part3-publication.l4: s 80(1) |
| 593-597 | s80.2 | Publication of the minimum legislative information for secondary legis | encoded | nz-part3-publication.l4: s 80 |
| 598 | s80.3 | The presumptions in this section apply unless the contrary is shown. | encoded | nz-part3-publication.l4: s 80 |
| 599-600 | s81.1 | 81 Judicial notice of legislation | encoded | nz-part3-publication.l4: s 81 |
| 601-602 | s82.1 | 82 Power to revoke spent secondary legislation and other instruments | encoded | nz-part3-publication.l4: s 82(1) |
| 603 | s82.2 | Before making a recommendation, the Attorney-General must be satisfied | encoded | nz-part3-publication.l4: s 82(2) |
| 604 | s82.3 | This section is in addition to any other power to revoke the secondary | encoded | nz-part3-publication.l4: s 82(3) |
| 605 | s82.4 | An order under this section is secondary legislation (see this Part fo | encoded | nz-part3-publication.l4: s 82(4) |
| 606 | h606 | Attorney-General directions | inert (1: not operative) | heading -- a heading creates no rule |
| 607-612 | s83.1 | 83 Attorney-General directions under this Part | encoded | nz-part3-publication.l4: s 83 |
| 613 | s83.2 | A direction given by the Attorney-General under this Part must be give | encoded | nz-part3-publication.l4: s 83; nz-part3-publication.l4: s 83(2) |
| 614 | h614 | Annual report on exemptions from presentation and other drafting and p | inert (1: not operative) | heading -- a heading creates no rule |
| 615-618 | s83A.1 | 83A Annual report on exemptions from presentation and other drafting a | encoded | nz-part3-publication.l4: s 83A(1) |
| 619 | s83A.2 | The Attorney-General must present the report to the House of Represent | encoded | nz-part3-publication.l4: s 83A(2) |
| 620 | h620 | Subpart 2 — Correcting errors and making other editorial changes | inert (1: not operative) | heading -- a heading creates no rule |
| 621-624 | s84.1 | 84 Purpose of this subpart | inert (1: not operative) | not operative -- s 84: purpose clause |
| 625-626 | s85.1 | 85 Interpretation | encoded | nz-glossary.l4: `a definition in the Act governs the use of the term`; the scope 'this subpart' is in each entry's field -- lead-in words |
| 627 | s85.def.current drafting practice | defined term: current drafting practice | encoded | nz-glossary.l4: entry for current drafting practice (tested in nz-tests-glossary.l4); nz-part3-editorial-revision.l4: s 85, definition of current drafting practice |
| 628 | s85.def.referential words | defined term: referential words | encoded | nz-glossary.l4: entry for referential words (tested in nz-tests-glossary.l4); nz-part3-editorial-revision.l4: s 85, definition of referential words |
| 629-630 | s86.1 | 86 Power to make editorial changes | encoded | nz-part3-editorial-revision.l4: s 86(1) |
| 631 | s86.2 | Sections 87 and 89 do not permit any change to the text of a provision | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 632 | s86.3 | Nothing in this section limits the authority to make changes in relian | encoded | nz-part3-editorial-revision.l4: s 86(3) |
| 633-635 | s87.1 | 87 Editorial changes | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 636-639 | s87.ex.636 | example: The word he may be changed to they, or replaced wi | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 640-644 | s87.p.640 | language to which section 16 applies may be changed to reflect the eff | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 645-646 | s87.ex.645 | example: Schedule 1 to the Ombudsmen Act 1975 may be change | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 647-651 | s87.p.647 | unnecessary referential words may be omitted: | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 652-653 | s87.ex.652 | example: A reference in a form to this [blank] day of [blan | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 654-659 | s87.p.654 | obvious errors of the following kinds may be corrected: | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 660-663 | s87.ex.660 | example: In the following provision, the word in bold can b | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 664 | s87.p.664 | a reference to a method of setting or determining a date or time (for  | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 665-666 | s87.ex.665 | example: A commencement clause states that the Act commence | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 667-668 | s87.p.667 | a provision in the nature of a transitional, savings, validation, or o | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 669-670 | s87.ex.669 | example: The heading to a section may be changed to reflect | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 671 | s87.p.671 | changes may be made to the Title of secondary legislation, so as to be | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 672-674 | s87.ex.672 | example: The Cat Notice can be changed to the Cat Notice 20 | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 675 | s87.p.675 | changes may be made that are purely consequential on any other change  | encoded | nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 676-679 | s88.1 | 88 Changes to numbering | encoded | nz-part3-editorial-revision.l4: s 88(1) |
| 680 | s88.2 | An order under this section is secondary legislation (see this Part fo | encoded | nz-part3-editorial-revision.l4: s 88(2) |
| 681-682 | s89.1 | 89 Changes to format | encoded | nz-part3-editorial-revision.l4: s 89; nz-part3-editorial-revision.l4: s 86(2), s 87 and s 89 |
| 683-684 | s90.1 | 90 When changes take effect | fork | fork F10 -- changes take effect as if enacted by other legislation 'having effect immediately before' the changes: an amendment taking effect on the day itself sees them (nz-part3-editorial-revision.l4) |
| 685-688 | s91.1 | 91 Changes to legislation to be noted on legislation website | encoded | nz-part3-editorial-revision.l4: s 91 |
| 689 | h689 | Subpart 3 — Revision Bills | inert (1: not operative) | heading -- a heading creates no rule |
| 690-691 | s92.1 | 92 Purpose of this subpart | inert (1: not operative) | not operative -- s 92: purpose clause |
| 692 | s92.2 | To that end, this subpart enables revision Bills to re-enact legislati | inert (1: not operative) | not operative -- s 92(2): purpose clause |
| 693-694 | s93.1 | 93 Overview of this subpart | inert (1: not operative) | not operative -- s 93: overview |
| 695-697 | s93.2 | This subpart contains— | inert (1: not operative) | not operative -- s 93: overview |
| 698 | s93.3 | This section is only a general guide to this subpart. | inert (1: not operative) | not operative -- s 93: says it is only a guide |
| 699 | s93.4 | See also sections 59 to 62, which provide for the interpretation of re | inert (1: not operative) | not operative -- s 93: signpost to ss 59 to 62 |
| 700-701 | s94.1 | 94 Interpretation | encoded | nz-glossary.l4: `a definition in the Act governs the use of the term`; the scope 'this subpart' is in each entry's field -- lead-in words |
| 702 | s94.def.revision Bill | defined term: revision Bill | encoded | nz-glossary.l4: entry for revision Bill (tested in nz-tests-glossary.l4); nz-part3-editorial-revision.l4: s 94, definition of revision Bill |
| 703 | s94.def.revision programme | defined term: revision programme | encoded | nz-glossary.l4: entry for revision programme (tested in nz-tests-glossary.l4); nz-part3-editorial-revision.l4: s 94, definition of revision programme |
| 704 | h704 | Preparation of revisions | inert (1: not operative) | heading -- a heading creates no rule |
| 705-706 | s95.1 | 95 Three-yearly revision programme | encoded | nz-part3-editorial-revision.l4: s 95(1) |
| 707-710 | s95.2 | A draft revision programme must set out— | encoded | nz-part3-editorial-revision.l4: s 95(2) |
| 711-713 | s95.3 | The Attorney-General must— | encoded | nz-part3-editorial-revision.l4: s 95(3) |
| 714 | s95.4 | The Attorney-General may amend, or replace, the 3-yearly revision prog | encoded | nz-part3-editorial-revision.l4: s 95(4) |
| 715-716 | s96.1 | 96 Revision powers | encoded | nz-part3-editorial-revision.l4: s 96(1) |
| 717-727 | s96.2 | A revision Bill may— | encoded | nz-part3-editorial-revision.l4: s 96(2), (3), (5) and (6) |
| 728-735 | s96.3 | A revision Bill may also— | encoded | nz-part3-editorial-revision.l4: s 96(2), (3), (5) and (6) |
| 736 | s96.def.Consumers Price Index | defined term: Consumers Price Index | encoded | nz-glossary.l4: entry for Consumers Price Index (tested in nz-tests-glossary.l4) |
| 737 | s96.4 | A revision Bill must not change the effect of the law, except as autho | encoded | nz-part3-editorial-revision.l4: s 96(2), (3), (5) and (6) |
| 738 | s96.5 | The changes that may be made in a revision Bill include (without limit | encoded | nz-part3-editorial-revision.l4: s 96(2), (3), (5) and (6) |
| 739-740 | s97.1 | 97 Format of revision Bill | encoded | nz-part3-editorial-revision.l4: s 97(1) |
| 741 | s97.2 | A revision Bill’s explanatory note must include a statement setting ou | encoded | nz-part3-editorial-revision.l4: s 97(2) |
| 742 | s97.3 | A revision Bill may be structured so that it is able to be divided int | encoded | nz-part3-editorial-revision.l4: s 97(3) |
| 743-744 | s98.1 | 98 Certification of revision Bill | encoded | nz-part3-editorial-revision.l4: s 98(1) |
| 745 | s98.2 | The Chief Parliamentary Counsel must submit a revision Bill to the cer | encoded | nz-part3-editorial-revision.l4: s 98(2), (4) and (5) |
| 746-748 | s98.3 | The certifiers may certify a revision Bill if they are satisfied that— | encoded | nz-part3-editorial-revision.l4: s 98(3) |
| 749 | s98.4 | Before certifying a revision Bill, the certifiers may require the Chie | encoded | nz-part3-editorial-revision.l4: s 98(2), (4) and (5) |
| 750 | s98.5 | When a revision Bill has been certified, the Chief Parliamentary Couns | encoded | nz-part3-editorial-revision.l4: s 98(2), (4) and (5) |
| 751-752 | s99.1 | 99 Amendments proposed by revision Bills | encoded | nz-part3-editorial-revision.l4: s 99(1) |
| 753 | s99.2 | However, nothing in this Act affects the powers of the House of Repres | encoded | nz-part3-editorial-revision.l4: s 99(2) |
| 754-760 | s100.1 | 100 PCO’s annual report may address matters relating to revision and e | encoded | nz-part3-editorial-revision.l4: s 100 |
| 761 | h761 | Part 4 — Disclosure requirements for Government-initiated legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 762 | s101 | 101 Purpose of this Part | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 763 | s102 | 102 Interpretation in this Part | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 764 | s103 | 103 Chief executives must prepare and publish disclosure statements fo | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 765 | s104 | 104 What must be contained, or linked to, in disclosure statements | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 766 | s105 | 105 Disclosure statement requirements do not apply to certain Bills an | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 767 | s106 | 106 Chief executives must act independently and include statement of r | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 768 | s107 | 107 Government notice must be issued to support consistent approach ac | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 769 | s108 | 108 Government notice may be issued only with approval of House of Rep | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 770 | s109 | 109 Factors to be considered in determining classes of legislation req | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 771 | s110 | 110 Ministerial direction may be given to support consistent approach  | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 772 | s111 | 111 Disclosure relates only to information available to public under O | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 773 | s112 | 112 Validity of legislation not affected by failure to comply with thi | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 774 | h774 | Part 5 — Parliament’s oversight of secondary legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 775-776 | s113.1 | 113 Purpose of this Part | inert (1: not operative) | not operative -- s 113: purpose clause |
| 777 | h777 | Subpart 1 — Presentation to House of Representatives | inert (1: not operative) | heading -- a heading creates no rule |
| 778-779 | s114.1 | 114 Secondary legislation must be presented to House of Representative | encoded | nz-part5-oversight.l4: s 114 |
| 780-782 | s114.2 | However,— | encoded | nz-part5-oversight.l4: s 114 |
| 783 | h783 | Subpart 2 — Disallowance by House of Representatives | inert (1: not operative) | heading -- a heading creates no rule |
| 784-789 | s115.1 | 115 All secondary legislation subject to disallowance, with limited ex | encoded | nz-part5-oversight.l4: s 115 |
| 790-791 | s116.1 | 116 House of Representatives may disallow secondary legislation by res | encoded | nz-part5-oversight.l4: s 116(1) |
| 792-794 | s116.2 | Legislation disallowed by a resolution ceases to have effect on the la | encoded | nz-part5-oversight.l4: s 116(2) |
| 795-800 | s117.1 | 117 Secondary legislation disallowed if House of Representatives does  | encoded | nz-part5-oversight.l4: s 117(1) |
| 801 | s117.2 | Parliament is dissolved or expires. | encoded | nz-part5-oversight.l4: s 117(1) |
| 802-804 | s117.3 | Legislation disallowed under this section ceases to have effect on the | encoded | nz-part5-oversight.l4: s 117(2) |
| 805 | s117.4 | In this section, the deadline is the close of the 21st sitting day aft | encoded | nz-part5-oversight.l4: s 117(3) |
| 806-810 | s118.1 | 118 Effect of disallowance on legislation | encoded | nz-part5-oversight.l4: s 118 and s 125(1)(b); nz-part5-oversight.l4: s 118(1)(a); nz-part5-oversight.l4: s 118(1)(c) |
| 811 | s118.2 | This section alters the effect of section 32 (which relates to the eff | encoded | nz-part5-oversight.l4: s 118 and s 125(1)(b) |
| 812-813 | s119.1 | 119 House of Representatives may amend or replace secondary legislatio | encoded | nz-part5-oversight.l4: s 119(1) |
| 814-816 | s119.2 | The amendment or replacement takes effect on the later of— | encoded | nz-part5-oversight.l4: s 119(2) |
| 817 | s119.3 | Secondary legislation that is amended or replaced by resolution of the | encoded | nz-part5-oversight.l4: s 119(3) |
| 818-819 | s120.1 | 120 Resolution or motion is secondary legislation | encoded | nz-part5-oversight.l4: s 120(1) |
| 820 | s120.2 | For that purpose, the Clerk of the House of Representatives must lodge | encoded | nz-part5-oversight.l4: s 120(2) |
| 821 | s120.3 | However, sections 116(2) and 117(2) apply even if the copy or notice i | encoded | nz-part5-oversight.l4: s 120(3) |
| 822 | h822 | Subpart 3 — Confirmation | inert (1: not operative) | heading -- a heading creates no rule |
| 823-824 | s121.1 | 121 Definitions used in this subpart | encoded | nz-glossary.l4: the scope 'this subpart' is the field `the provision that defines it` of each section 121 entry -- lead-in words |
| 825-827 | s121.def.deadline | defined term: deadline | encoded | nz-glossary.l4: entry for deadline (tested in nz-tests-glossary.l4); nz-part5-oversight.l4: s 121, definition of deadline |
| 828 | s121.def.unconfirmed legislation | defined term: unconfirmed legislation | encoded | nz-glossary.l4: entry for unconfirmed legislation (tested in nz-tests-glossary.l4); nz-part5-oversight.l4: s 121, definition of unconfirmed legislation |
| 829-830 | s122.1 | 122 What secondary legislation must be confirmed under this subpart | encoded | nz-part5-oversight.l4: s 122 |
| 831 | s122.2 | However, if that schedule limits which matters require confirmation un | encoded | nz-part5-oversight.l4: s 122 |
| 832-833 | s123.1 | 123 Secondary legislation must be confirmed by deadline (or otherwise  | encoded | nz-part5-oversight.l4: s 123 |
| 834-837 | s124.1 | 124 How to confirm secondary legislation | encoded | nz-part5-oversight.l4: s 124 |
| 838 | s124.2 | The later repeal of the Act or provision does not affect the confirmat | encoded | nz-part5-oversight.l4: s 124; nz-part5-oversight.l4: s 124(2) |
| 839-844 | s125.1 | 125 Usual effect of revocation if not confirmed by deadline | encoded | nz-part5-oversight.l4: s 125(1)(c); nz-part5-oversight.l4: s 125(1)(a), (2) and (3); nz-part5-oversight.l4: s 118 and s 125(1)(b) ... |
| 845-848 | s125.2 | Subsection (1)﻿(a) does not apply to any of the following: | encoded | nz-part5-oversight.l4: s 125(1)(a), (2) and (3) |
| 849 | s125.3 | However, this section does not apply if the unconfirmed legislation is | encoded | nz-part5-oversight.l4: s 125(1)(a), (2) and (3) |
| 850-851 | s126.1 | 126 Effect on some legislation of not being confirmed by deadline (whe | encoded | nz-part5-oversight.l4: s 126 |
| 852 | s126.2 | The legislation is taken, on and from the deadline, to have been inval | encoded | nz-part5-oversight.l4: s 126 |
| 853-856 | s127.1 | 127 Confirmable secondary legislation must state this fact | encoded | nz-part5-oversight.l4: s 127 |
| 857 | s127.2 | However, a failure to include those statements does not affect the val | encoded | nz-part5-oversight.l4: s 127(2) |
| 858 | h858 | Part 6 — Parliamentary Counsel Office | inert (1: not operative) | heading -- a heading creates no rule |
| 859-860 | s128.1 | 128 Parliamentary Counsel Office continues | inert (2: machinery) | machinery -- s 128(1): the PCO continues (an office) |
| 861 | s128.2 | The Parliamentary Counsel Office is an instrument of the Crown and a s | inert (2: machinery) | machinery -- s 128(2): the PCO's status (an office) |
| 862 | s128.3 | During any period when there is no Minister of the Crown who is Attorn | inert (2: machinery) | machinery -- s 128(3): the PCO when there is no Attorney-General (an office) |
| 863 | h863 | Objective and functions of PCO | inert (1: not operative) | heading -- a heading creates no rule |
| 864-865 | s129.1 | 129 Objective of PCO | inert (1: not operative) | not operative -- s 129: the PCO's objective, creates no rule |
| 866-874 | s130.1 | 130 Functions of PCO | inert (2: machinery) | machinery -- s 130: the PCO's functions (an office) |
| 875-876 | s131.1 | 131 Confidentiality | encoded | nz-part6-7-pco-regulations.l4: s 131(1) and (2) |
| 877 | s131.2 | However, nothing in this section limits or affects the rules and pract | encoded | nz-part6-7-pco-regulations.l4: s 131(1) and (2) |
| 878 | s131.3 | In this section,— | encoded | nz-glossary.l4: the scope 'this section' is the field `the provision that defines it` of each section 131(3) entry -- lead-in words |
| 879 | s131.def.client | defined term: client | encoded | nz-glossary.l4: entry for client (tested in nz-tests-glossary.l4); nz-part6-7-pco-regulations.l4: s 131(3), definition of client |
| 880-882 | s131.def.confidential communications | defined term: confidential communications | encoded | nz-glossary.l4: entry for confidential communications (tested in nz-tests-glossary.l4); nz-part6-7-pco-regulations.l4: s 131(3), definition of confidential communications |
| 883 | s131.def.counsel | defined term: counsel | encoded | nz-glossary.l4: entry for counsel (tested in nz-tests-glossary.l4); nz-part6-7-pco-regulations.l4: s 131(3), definition of counsel |
| 884 | h884 | Powers of Chief Parliamentary Counsel | inert (1: not operative) | heading -- a heading creates no rule |
| 885-886 | s132.1 | 132 Powers of Chief Parliamentary Counsel | inert (2: machinery) | machinery -- s 132: the Chief Parliamentary Counsel's powers (an office) |
| 887-890 | s133.1 | 133 Delegation of functions, duties, and powers | encoded | nz-part6-7-pco-regulations.l4: s 133(1)(a); nz-part6-7-pco-regulations.l4: s 133(1)(b) |
| 891 | s133.2 | The person to whom any functions, duties, or powers are delegated may  | encoded | nz-part6-7-pco-regulations.l4: s 133(2) and (3) |
| 892 | s133.3 | Subsection (2) is subject to any general or special directions given o | encoded | nz-part6-7-pco-regulations.l4: s 133(2) and (3) |
| 893 | s133.4 | A person purporting to act under a delegation is, in the absence of pr | encoded | nz-part6-7-pco-regulations.l4: s 133(4) |
| 894-896 | s133.5 | A delegation may be made to— | encoded | nz-part6-7-pco-regulations.l4: s 133(5) |
| 897 | s133.6 | No delegation affects or prevents the exercise of any function, respon | encoded | nz-part6-7-pco-regulations.l4: s 133(6) |
| 898-899 | s134.1 | 134 Revocation of delegations | encoded | nz-part6-7-pco-regulations.l4: s 134(1) |
| 900 | s134.2 | A delegation made by a Chief Parliamentary Counsel who has ceased to h | encoded | nz-part6-7-pco-regulations.l4: s 134(2) |
| 901 | h901 | Chief Parliamentary Counsel and employees of PCO | inert (1: not operative) | heading -- a heading creates no rule |
| 902-906 | s135.1 | 135 Chief Parliamentary Counsel | inert (2: machinery) | machinery -- s 135(1): the Chief Parliamentary Counsel (office and staffing) |
| 907 | s135.2 | However, in matters relating to decisions on individual employees, the | inert (2: machinery) | machinery -- s 135(2): the Chief Parliamentary Counsel (office and staffing) |
| 908-913 | s135.3 | The Chief Parliamentary Counsel— | inert (2: machinery) | machinery -- s 135(3): the Chief Parliamentary Counsel (office and staffing) |
| 914 | s135.4 | The Chief Parliamentary Counsel may at any time be removed or suspende | inert (2: machinery) | machinery -- s 135(4): removal from office (staffing) |
| 915-916 | s136.1 | 136 Parliamentary counsel | inert (2: machinery) | machinery -- s 136(1): parliamentary counsel (staffing) |
| 917 | s136.2 | A parliamentary counsel must hold a legal qualification. | inert (2: machinery) | machinery -- s 136(2): parliamentary counsel (staffing) |
| 918 | s136.3 | A parliamentary counsel is an employee for the purposes of the Employm | inert (2: machinery) | machinery -- s 136(3): parliamentary counsel (staffing) |
| 919-923 | s137.1 | 137 Chief Parliamentary Counsel and parliamentary counsel to hold lega | inert (2: machinery) | machinery -- s 137: qualification of staff |
| 924-927 | s137.2 | A person meets the qualification requirement in section 136(2) for a p | inert (2: machinery) | machinery -- s 137: qualification of staff |
| 928 | s137.3 | To avoid doubt, sections 21 to 24 of the Lawyers and Conveyancers Act  | inert (2: machinery) | machinery -- s 137: qualification of staff |
| 929 | s137.4 | The Governor-General may, by Order in Council made on the recommendati | inert (2: machinery) | machinery -- s 137: qualification of staff (an Order in Council) |
| 930 | s137.5 | An order under this section is secondary legislation (see Part 3 for p | inert (2: machinery) | machinery -- s 137: the order is secondary legislation (staffing) |
| 931-932 | s138.1 | 138 Other employees of PCO | inert (2: machinery) | machinery -- s 138: other employees of the PCO |
| 933 | s138.2 | A person appointed under this section is an employee for the purposes  | inert (2: machinery) | machinery -- s 138: other employees of the PCO |
| 934-935 | s139.1 | 139 Remuneration and conditions of appointment of Chief Parliamentary  | inert (2: machinery) | machinery -- s 139: remuneration and conditions of appointment |
| 936 | s139.2 | The terms and conditions of appointment of the Chief Parliamentary Cou | inert (2: machinery) | machinery -- s 139: remuneration and conditions of appointment |
| 937-938 | s140.1 | 140 Chief Parliamentary Counsel acts as employer | inert (2: machinery) | machinery -- s 140: the Chief Parliamentary Counsel acts as employer |
| 939-942 | s141.1 | 141 Collective agreements | inert (2: machinery) | machinery -- s 141: collective agreements |
| 943 | s141.def.union | defined term: union | encoded | nz-glossary.l4: entry for union (tested in nz-tests-glossary.l4) |
| 944-945 | s142.1 | 142 Employment principles | inert (2: machinery) | machinery -- s 142: employment principles |
| 946-947 | s143.1 | 143 Appointments on merit | inert (2: machinery) | machinery -- s 143: appointments on merit |
| 948-952 | s144.1 | 144 Chief Parliamentary Counsel to establish procedure for notifying v | inert (2: machinery) | machinery -- s 144: procedure for notifying vacancies |
| 953-954 | s145.1 | 145 Secondments from elsewhere in State Services for developing senior | inert (2: machinery) | machinery -- s 145: secondments |
| 955-956 | s146.1 | 146 Protection from liability | encoded | nz-part6-7-pco-regulations.l4: s 146 |
| 957-959 | s146.2 | No proceeding may be brought against any person to whom this section a | encoded | nz-part6-7-pco-regulations.l4: s 146 |
| 960 | h960 | Part 7 — Regulations and miscellaneous provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 961 | h961 | Regulation-making powers | inert (1: not operative) | heading -- a heading creates no rule |
| 962-963 | s147.l.963 | 147 Regulations | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 964 | s147.l.964 | prescribing additional minimum legislative information for the purpose | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 965 | s147.l.965 | prescribing information for the purposes of the obligation for the PCO | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 966 | s147.l.966 | prescribing minimum requirements for the manner in which secondary leg | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 967 | s147.l.967 | are enacted on or after the main commencement date; or | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 968 | s147.l.968 | were enacted before the main commencement date and are specified in th | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 969 | s147.l.969 | are in this Act: | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 970 | s147.l.970 | prescribing any instrument of the Crown for the purposes of paragraph  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 971 | s147.l.971 | requiring makers of secondary legislation not drafted by the PCO to lo | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 972 | s147.l.972 | specifying, for the purposes of section 70(1)﻿(c), the secondary legis | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 973 | s147.l.973 | in respect of a consolidation required by regulations made under parag | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 974 | s147.l.974 | prescribing, for the purposes of any requirement for something to be l | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 975 | s147.l.975 | by whom, when, where, and how the thing must be lodged (including, in  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 976 | s147.l.976 | the form, format, method, or medium that must be used in connection wi | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 977 | s147.l.977 | what information or other evidence or documents must be provided in co | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 978 | s147.l.978 | requirements with which information, evidence, or documents that are p | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 979 | s147.l.979 | by whom, when, where, and how any updates or corrections must be made  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 980 | s147.l.980 | authorising the PCO to determine or prescribe, whether by notice or by | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 981 | s147.l.981 | determining what lodgement requirements imposed under the regulations  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 982 | s147.l.982 | exempting (on terms and conditions, if any) secondary legislation from | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 983 | s147.l.983 | the requirements to lodge and publish particular minimum legislative i | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 984 | s147.l.984 | the requirements relating to lodgement and publication that are prescr | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 985 | s147.l.985 | the prohibition on coming into force before publication under section  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 986 | s147.l.986 | any other requirements as to how or when to lodge or publish under thi | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 987 | s147.l.987 | prescribing, for the purpose of section 76, minimum requirements for t | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 988 | s147.l.988 | imposing requirements concerning the manner in which legislation and m | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 989 | s147.l.989 | specifying features by which an electronic document or a printed docum | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 990 | s147.l.990 | imposing requirements as to the form of official versions of legislati | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 991 | s147.l.991 | providing how official versions of legislation in an electronic form c | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 992 | s147.l.992 | requiring the payment of fees and charges to the PCO to perform or exe | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 993 | s147.l.993 | prescribing the amounts of those fees and charges or the manner in whi | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 994 | s147.l.994 | authorising the PCO to require payment of any costs incurred by the PC | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 995 | s147.l.995 | authorising the PCO to waive or refund, in whole or in part and with o | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 996 | s147.l.996 | providing for matters contemplated by subpart 2 of Part 1 of Schedule  | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 997 | s147.l.997 | deadlines and classes of secondary legislation to which those deadline | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 998 | s147.l.998 | dates and classes of secondary legislation (which may include all seco | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 999 | s147.l.999 | any matters set out in paragraphs (a) to (l) that are relevant to mini | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 1000 | s147.l.1000 | providing for any other matters contemplated by this Act, necessary fo | inert (2: machinery) | machinery -- s 147(1): a purpose for which regulations may be made (regulation-making power) |
| 1001 | s147.1 | The Attorney-General must, before making a recommendation to specify a | inert (2: machinery) | machinery -- s 147(2): the Attorney-General's consultation before a recommendation (regulation-making power) |
| 1002-1005 | s147.2 | The Attorney-General must, before making a recommendation in relation  | inert (2: machinery) | machinery -- s 147(3): the Attorney-General's conditions before an exemption (regulation-making power) |
| 1006 | s147.3 | If the Attorney-General makes a recommendation in relation to an exemp | inert (2: machinery) | machinery -- s 147(4): effect of an exemption recommendation (regulation-making power) |
| 1007 | s147.4 | The Attorney-General must, before making a recommendation in relation  | inert (2: machinery) | machinery -- s 147(5): consultation before regulations (regulation-making power) |
| 1008-1010 | s147.def.In this section, discretionary publication request | defined term: In this section, discretionary publication request | encoded | nz-glossary.l4: entry for In this section, discretionary publication request (tested in nz-tests-glossary.l4) |
| 1011 | s147.5 | Any fee, charge, or cost payable to the PCO is recoverable by the PCO  | encoded | nz-part6-7-pco-regulations.l4: s 147(7) |
| 1012 | s147.6 | Regulations made under this section are secondary legislation (see Par | encoded | nz-part6-7-pco-regulations.l4: s 147(8) |
| 1013-1015 | s147.7 | If regulations made under subsection (1)﻿(i) authorise the PCO to dete | encoded | nz-part6-7-pco-regulations.l4: s 147(9) |
| 1016 | s147.8 | References to sections of this Act (or to terms) in subsection (1)﻿(f) | inert (2: machinery) | machinery -- s 147: how the references in subsection (1)(f) to (l) are read (regulation-making power) |
| 1017 | s147.9 | In this section, main commencement date and publication commencement d | encoded | nz-glossary.l4: entries for main commencement date and publication commencement date (Schedule 1 clause 2) -- a cross-reference definition |
| 1018-1021 | s147A.1 | 147A Regulations may make consequential amendments to other secondary  | encoded | nz-part6-7-pco-regulations.l4: s 147A(1) and (2) |
| 1022 | s147A.2 | A failure to contain that statement does not affect the validity of ei | encoded | nz-part6-7-pco-regulations.l4: s 147A(1) and (2) |
| 1023-1025 | s147A.3 | However, the Governor-General may, by Order in Council, make regulatio | inert (2: machinery) | machinery -- s 147A(3): limits on the power to amend (regulation-making power) |
| 1026 | s147A.4 | The only facts, circumstances, or preconditions that must exist or be  | inert (2: machinery) | machinery -- s 147A(4): the only preconditions (regulation-making power) |
| 1027 | s147A.5 | Regulations made under this section are secondary legislation (see Par | encoded | nz-part6-7-pco-regulations.l4: s 147A(5) |
| 1028 | h1028 | Review of revision programme provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 1029 | s148 | 148 Review of revision programme provisions after 30 June 2020 | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 1030 | h1030 | Schedule 1 — Transitional, savings, and related provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 1031 | x1031 | Contents | inert (1: not operative) | not operative -- the contents line |
| 1032 | h1032 | Part 1 — Provisions relating to this Act as enacted | inert (1: not operative) | heading -- a heading creates no rule |
| 1033-1040 | sch1.1.1 | 1 General overview of this Part | inert (1: not operative) | not operative -- Schedule 1 clause 1: overview |
| 1041-1042 | sch1.2.1 | 2 Definitions for this Part | encoded | nz-glossary.l4: the scope 'this Part' is the field `the provision that defines it` of each Schedule 1 clause 2 entry -- lead-in words |
| 1043 | sch1.2.def.list deadline | defined term: list deadline | encoded | nz-glossary.l4: entry for list deadline (tested in nz-tests-glossary.l4) |
| 1044 | sch1.2.def.list exemption | defined term: list exemption | encoded | nz-glossary.l4: entry for list exemption (tested in nz-tests-glossary.l4) |
| 1045 | sch1.2.def.main commencement date | defined term: main commencement date | encoded | nz-glossary.l4: entry for main commencement date (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 2, definition of main commencement date |
| 1046 | sch1.2.def.publication commencement date | defined term: publication commencement date | encoded | nz-glossary.l4: entry for publication commencement date (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 2, definition of publication commencement date |
| 1047 | sch1.2.def.publication exemption | defined term: publication exemption | encoded | nz-glossary.l4: entry for publication exemption (tested in nz-tests-glossary.l4) |
| 1048 | sch1.2.def.publication deadline | defined term: publication deadline | encoded | nz-glossary.l4: entry for publication deadline (tested in nz-tests-glossary.l4) |
| 1049 | sch1.2.def.regulations | defined term: regulations | encoded | nz-glossary.l4: entry for regulations (tested in nz-tests-glossary.l4) |
| 1050 | h1050 | Subpart 1 — Interpretation and application of legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 1051 | h1051 | How provisions apply to existing and new legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 1052-1055 | sch1.3.1 | 3 Part 2 of this Act applies to both existing and new legislation | encoded | nz-schedules.l4: Schedule 1 clause 3 |
| 1056 | sch1.3.2 | This clause is subject to the rest of this subpart. | encoded | nz-schedules.l4: Schedule 1 clause 3(2) |
| 1057-1058 | sch1.4.1 | 4 Exception for examples in existing legislation | encoded | nz-schedules.l4: Schedule 1 clause 4 |
| 1059-1061 | sch1.4.2 | This clause applies unless— | encoded | nz-schedules.l4: Schedule 1 clause 4 |
| 1062-1063 | sch1.5.1 | 5 Exception for commencement of secondary legislation made before main | encoded | nz-schedules.l4: Schedule 1 clause 5 |
| 1064 | h1064 | Savings of previous definitions for certain legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 1065-1066 | sch1.6.1 | 6 Saving of definitions for pre-1 November 1999 legislation | encoded | nz-schedules.l4: Schedule 1 clause 6 |
| 1067 | sch1.6.def.Act | defined term: Act | encoded | nz-glossary.l4: entry for Act (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 6 |
| 1068 | sch1.6.def.Governor | defined term: Governor | encoded | nz-glossary.l4: entry for Governor (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 6 |
| 1069 | sch1.6.def.land | defined term: land | encoded | nz-glossary.l4: entry for land (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 6 |
| 1070 | sch1.6.def.person | defined term: person | encoded | nz-glossary.l4: entry for person (tested in nz-tests-glossary.l4); nz-schedules.l4: Schedule 1 clause 6 |
| 1071-1073 | sch1.6.2 | This clause applies to legislation unless— | encoded | nz-schedules.l4: Schedule 1 clause 6 |
| 1074-1075 | sch1.7.1 | 7 Saving of definitions for legislation made before main commencement  | encoded | nz-schedules.l4: Schedule 1 clause 7 |
| 1076-1078 | sch1.7.2 | This clause applies to legislation unless— | encoded | nz-schedules.l4: Schedule 1 clause 7 |
| 1079-1080 | sch1.8.1 | 8 Savings of previous Proclamations | encoded | nz-schedules.l4: Schedule 1 clause 8 |
| 1081-1084 | sch1.9.1 | 9 Savings of material incorporated by reference under Legislation Act  | encoded | nz-schedules.l4: Schedule 1 clause 9(1); nz-schedules.l4: Schedule 1 clause 9(1)(b) |
| 1085 | sch1.9.2 | The chief executive may make it publicly available in another way perm | encoded | nz-schedules.l4: Schedule 1 clause 9(2) |
| 1086-1087 | sch1.10.1 | 10 How Abolition of Provinces Act 1875 affects provincial legislation | encoded | nz-schedules.l4: Schedule 1 clause 10 |
| 1088 | h1088 | Subpart 2 — Transition for secondary legislation to new publication re | inert (1: not operative) | heading -- a heading creates no rule |
| 1089-1092 | sch1.11.1 | 11 Purpose | inert (1: not operative) | not operative -- Schedule 1 clause 11: purpose clause |
| 1093 | sch1.11.2 | See also section 147(1)﻿(s), which provides for regulations to be made | inert (1: not operative) | not operative -- Schedule 1 clause 11: signpost to s 147(1)(s) |
| 1094-1101 | sch1.12.1 | 12 Outline of transition to Part 3 publication | inert (1: not operative) | not operative -- Schedule 1 clause 12: outline |
| 1102-1110 | sch1.12.2 | Part 3’s requirements for makers to lodge secondary legislation and mi | inert (1: not operative) | not operative -- Schedule 1 clause 12: outline |
| 1111 | sch1.12.3 | This is a guide only to the general scheme and effect of this subpart. | inert (1: not operative) | not operative -- Schedule 1 clause 12: says it is a guide only |
| 1112-1115 | sch1.13.1 | 13 Definition of secondary legislation is effective on main commenceme | encoded | nz-schedules.l4: Schedule 1 clause 13(1) |
| 1116 | sch1.13.2 | An instrument made before that date that is in force under a provision | encoded | nz-schedules.l4: Schedule 1 clause 13(2) |
| 1117-1127 | sch1.13.ex.1117 | example: An order is made under section 100 of an Act befor | encoded | nz-tests-schedules.l4 (examples 1 to 3, quoted lines 1117-1127) -- an example, tested as a case |
| 1128-1130 | sch1.13.3 | For the purposes of this Act, a provision is an identified empowering  | encoded | nz-schedules.l4: Schedule 1 clause 13(3) |
| 1131-1134 | sch1.13.4 | The Chief Parliamentary Counsel may authorise the PCO to make the foll | encoded | nz-schedules.l4: Schedule 1 clause 13(4) |
| 1135-1137 | sch1.13.5 | Subpart 2 of Part 3 applies to those changes as if they were changes r | encoded | nz-schedules.l4: Schedule 1 clause 13(5) |
| 1138-1139 | sch1.14.1 | 14 Existing requirements continued as applicable publication requireme | encoded | nz-schedules.l4: Schedule 1 clause 14(1) and (2)(a) |
| 1140-1145 | sch1.14.2 | For the purposes of the applicable publication requirements under that | encoded | nz-schedules.l4: Schedule 1 clause 14(1) and (2)(a); nz-schedules.l4: Schedule 1 clause 14(2)(b) |
| 1146 | sch1.14.3 | Nothing in this clause limits the information that the PCO may record  | encoded | nz-schedules.l4: Schedule 1 clause 14(3) |
| 1147-1150 | sch1.15.1 | 15 Maker must lodge minimum legislative information before list deadli | encoded | nz-schedules.l4: Schedule 1 clause 15(1) |
| 1151-1156 | sch1.15.2 | Until the list deadline,— | encoded | nz-schedules.l4: Schedule 1 clause 15(2)(a); nz-schedules.l4: Schedule 1 clause 15(2)(b) |
| 1157 | sch1.15.3 | The maker must, before the list deadline, lodge the minimum legislativ | encoded | nz-schedules.l4: Schedule 1 clause 15(3) |
| 1158-1160 | sch1.15.4 | The secondary legislation is revoked on a date specified in the regula | encoded | nz-schedules.l4: Schedule 1 clause 15(4) |
| 1161-1164 | sch1.15.5 | The list deadline for secondary legislation is— | encoded | nz-schedules.l4: Schedule 1 clause 15(5); nz-interpretation-time.l4: s 2(1)(c) and Schedule 1 clause 15(5) |
| 1165-1168 | sch1.15.6 | For the purposes of subclause (2)﻿(b), in relation to the applicable p | encoded | nz-schedules.l4: Schedule 1 clause 15(6) |
| 1169-1172 | sch1.16.1 | 16 Maker must lodge secondary legislation for full publication before  | encoded | nz-schedules.l4: Schedule 1 clause 16(1) |
| 1173 | sch1.16.2 | A publication exemption applies to the secondary legislation until the | encoded | nz-schedules.l4: Schedule 1 clause 16(2) |
| 1174 | sch1.16.3 | The maker must, before the publication deadline, lodge the secondary l | encoded | nz-schedules.l4: Schedule 1 clause 16(3) |
| 1175-1177 | sch1.16.4 | The secondary legislation is revoked on a date specified in the regula | encoded | nz-schedules.l4: Schedule 1 clause 16(4) |
| 1178-1180 | sch1.16.5 | The publication deadline for secondary legislation is— | encoded | nz-schedules.l4: Schedule 1 clause 16(5) |
| 1181-1182 | sch1.17.1 | 17 Publication of information and secondary legislation to which this  | encoded | nz-schedules.l4: Schedule 1 clause 17 |
| 1183-1187 | sch1.18.1 | 18 Application of subpart 1 of Part 3 of this Act | encoded | nz-schedules.l4: Schedule 1 clause 18 |
| 1188 | h1188 | Other transitional matters | inert (1: not operative) | heading -- a heading creates no rule |
| 1189-1193 | sch1.19.1 | 19 Transitional regulation-making power | inert (2: machinery) | machinery -- Schedule 1 clause 19(1): purpose of the transitional regulation-making power |
| 1194-1201 | sch1.19.2 | The Governor-General may, by Order in Council made on the recommendati | inert (2: machinery) | machinery -- Schedule 1 clause 19(2) to (4): the transitional regulation-making power |
| 1202-1204 | sch1.19.3 | The Attorney-General may make a recommendation under this clause only  | inert (2: machinery) | machinery -- Schedule 1 clause 19(3): conditions on recommending regulations |
| 1205 | sch1.19.4 | Regulations made under this clause are secondary legislation (see Part | encoded | nz-schedules.l4: Schedule 1 clause 19(5) |
| 1206 | sch1.19.5 | This clause is repealed on the fifth anniversary of the publication co | encoded | nz-schedules.l4: Schedule 1 clause 19(6) |
| 1207-1208 | sch1.20.1 | 20 Transitional application of publication responsibilities | encoded | nz-schedules.l4: Schedule 1 clause 20(1) |
| 1209 | sch1.20.2 | Bills that were introduced before 5 August 2013 (or amendments to thos | encoded | nz-schedules.l4: Schedule 1 clause 20(1) |
| 1210-1212 | sch1.20.3 | Acts that ceased to be in force before 5 August 2013: | encoded | nz-schedules.l4: Schedule 1 clause 20(1) |
| 1213-1215 | sch1.20.4 | Section 69, and other publication responsibilities for the PCO under P | encoded | nz-schedules.l4: Schedule 1 clause 20(2) |
| 1216 | sch1.20.5 | Sections 75 to 77 (as in force on the main commencement date) do not a | encoded | nz-schedules.l4: Schedule 1 clause 20(3) |
| 1217 | sch1.20.6 | Section 73 (as inserted by Schedule 2 of the Legislation (Repeals and  | encoded | nz-schedules.l4: Schedule 1 clause 20(4) |
| 1218-1219 | sch1.21.1 | 21 Power to reassign responsibilities of secondary legislation’s maker | encoded | nz-schedules.l4: Schedule 1 clause 21(1) |
| 1220 | sch1.21.2 | An authorisation is made by written notice given to the department and | encoded | nz-schedules.l4: Schedule 1 clause 21(2) |
| 1221 | sch1.21.3 | Any authorisation under this section expires on the publication deadli | encoded | nz-schedules.l4: Schedule 1 clause 21(3) |
| 1222-1226 | sch1.22.1 | 22 Commencement orders for existing Acts are secondary legislation | encoded | nz-schedules.l4: Schedule 1 clause 22 |
| 1227 | sch1.22.2 | A commencement order made under the provision is secondary legislation | encoded | nz-schedules.l4: Schedule 1 clause 22 |
| 1228 | h1228 | Subpart 3 — General drafting and publication matters | inert (1: not operative) | heading -- a heading creates no rule |
| 1229 | h1229 | Drafting responsibilities | inert (1: not operative) | heading -- a heading creates no rule |
| 1230-1231 | sch1.23.1 | 23 PCO’s responsibility for drafting secondary legislation | encoded | nz-schedules.l4: Schedule 1 clause 23 |
| 1232 | sch1.23.2 | The administering agency and the Chief Parliamentary Counsel are assum | encoded | nz-schedules.l4: Schedule 1 clause 23 |
| 1233 | sch1.23.3 | Subclause (2) applies only until either party notifies the other that  | encoded | nz-schedules.l4: Schedule 1 clause 23 |
| 1234 | sch1.23.4 | This clause does not apply to secondary legislation to which section 5 | encoded | nz-schedules.l4: Schedule 1 clause 23 |
| 1235-1236 | sch1.24.1 | 24 PCO may continue to draft and publish other instruments | encoded | nz-schedules.l4: Schedule 1 clause 24 |
| 1237 | h1237 | Official versions | inert (1: not operative) | heading -- a heading creates no rule |
| 1238-1239 | sch1.25.1 | 25 How power to issue official versions applies to previous or existin | encoded | nz-schedules.l4: Schedule 1 clause 25 |
| 1240 | sch1.25.2 | An official electronic version of legislation that was issued under se | encoded | nz-schedules.l4: Schedule 1 clause 25 |
| 1241-1242 | sch1.26.1 | 26 How legal status of previous official versions applies | encoded | nz-schedules.l4: Schedule 1 clause 26 |
| 1243-1246 | sch1.27.1 | 27 Previous printed official versions continue until new official vers | encoded | nz-schedules.l4: Schedule 1 clause 27 |
| 1247 | sch1.27.2 | Sections 16C and 16D of the Acts and Regulations Publication Act 1989  | encoded | nz-schedules.l4: Schedule 1 clause 27 |
| 1248-1251 | sch1.27A.1 | 27A Annual report on exemptions from presentation and other drafting a | encoded | nz-schedules.l4: Schedule 1 clause 27A |
| 1252-1253 | sch1.27B.1 | 27B Publication statement taken not to have been required | encoded | nz-schedules.l4: Schedule 1 clause 27B |
| 1254 | h1254 | Correcting errors and making other editorial changes | inert (1: not operative) | heading -- a heading creates no rule |
| 1255-1256 | sch1.28.1 | 28 How power to make editorial changes applies to legislation publishe | encoded | nz-schedules.l4: Schedule 1 clause 28 |
| 1257 | h1257 | Revision Bill provisions | inert (1: not operative) | heading -- a heading creates no rule |
| 1258-1259 | sch1.29.1 | 29 Provisions on revision Bills apply also to previous revision Bills | encoded | nz-schedules.l4: Schedule 1 clause 29 |
| 1260 | sch1.29.2 | References in this Act to sections 59 to 62 or subpart 3 of Part 3 of  | encoded | nz-schedules.l4: Schedule 1 clause 29 |
| 1261 | h1261 | Subpart 4 — Disclosure requirements for Government-initiated legislati | inert (1: not operative) | heading -- a heading creates no rule |
| 1262 | sch1.30 | 30 Disclosure requirements apply only to Bills introduced after Part 4 | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 1263 | sch1.31 | 31 Ministers may perform duties before Part 4 commencement date | repealed or blank in this text | blank in this text -- the text shows the heading and no body |
| 1264 | h1264 | Subpart 5 — Parliament’s oversight of secondary legislation | inert (1: not operative) | heading -- a heading creates no rule |
| 1265 | h1265 | Presentation to House of Representatives | inert (1: not operative) | heading -- a heading creates no rule |
| 1266-1267 | sch1.32.1 | 32 Limited application of presentation requirements to secondary legis | encoded | nz-schedules.l4: Schedule 1 clause 32(1) and (2) |
| 1268-1273 | sch1.32.2 | Subpart 1 of Part 5 of this Act, which requires secondary legislation  | encoded | nz-schedules.l4: Schedule 1 clause 32(1) and (2) |
| 1274 | sch1.32.3 | This clause does not affect any requirement for the legislation to be  | encoded | nz-schedules.l4: Schedule 1 clause 32(3) |
| 1275 | h1275 | Disallowance | inert (1: not operative) | heading -- a heading creates no rule |
| 1276-1277 | sch1.33.1 | 33 Old disallowance provisions continue to apply to existing notices o | encoded | nz-schedules.l4: Schedule 1 clause 33 |
| 1278-1281 | sch1.33A.1 | 33A New disallowance provisions apply to previously disallowable instr | encoded | nz-schedules.l4: Schedule 1 clause 33A |
| 1282 | h1282 | Confirmation | inert (1: not operative) | heading -- a heading creates no rule |
| 1283-1284 | sch1.34.1 | 34 Old confirmation provisions continue to apply to existing confirmab | encoded | nz-schedules.l4: Schedule 1 clause 34 |
| 1285 | h1285 | Subpart 6 — Parliamentary Counsel Office | inert (1: not operative) | heading -- a heading creates no rule |
| 1286-1287 | sch1.35.1 | 35 Saving for existing appointment | inert (2: machinery) | machinery -- Schedule 1 clause 35: saving for an existing appointment (an office-holder) |
| 1288 | h1288 | Schedule 1A — Secondary legislation made by Royal prerogative | repealed or blank in this text | blank in this text -- Schedule 1A: the heading is all the text shows; the description of the instruments made by Royal prerogative is not in the deposited text |
| 1289 | h1289 | Schedule 2 — Incorporation by reference | inert (1: not operative) | heading -- a heading creates no rule |
| 1290-1298 | sch2.1.1 | 1 Requirements to be met on proposal to incorporate material by refere | encoded | nz-schedules.l4: Schedule 2 clause 1 |
| 1299-1302 | sch2.2.1 | 2 Access to material incorporated by reference | encoded | nz-schedules.l4: Schedule 2 clause 2 |
| 1303-1309 | sch2.3.1 | 3 What is required to make material publicly available | encoded | nz-schedules.l4: Schedule 2 clause 3(1); nz-schedules.l4: Schedule 2 clause 3(1)(c) |
| 1310 | sch2.3.2 | A chief executive must not rely on section 66 of the Copyright Act 199 | encoded | nz-schedules.l4: Schedule 2 clause 3(2) |
| 1311-1314 | sch2.4.1 | 4 Proof of material incorporated by reference | encoded | nz-schedules.l4: Schedule 2 clause 4(1) |
| 1315 | sch2.4.2 | The production in a proceeding of a copy of the material incorporated  | encoded | nz-schedules.l4: Schedule 2 clause 4(2) |
| 1316 | sch2.4.3 | See also Part 4 of the Contract and Commercial Law Act 2017, which ena | encoded | nz-schedules.l4: Schedule 2 clause 4(3) |
| 1317-1318 | sch2.5.1 | 5 Material incorporated by reference need not be published under this  | encoded | nz-schedules.l4: Schedule 2 clause 5 |
| 1319-1320 | sch2.6.1 | 6 Failure to comply does not invalidate | encoded | nz-schedules.l4: Schedule 2 clause 6 |
| 1321 | h1321 | Schedule 3 — Exemptions from presentation or disallowance under this A | inert (1: not operative) | heading -- a heading creates no rule |
| 1322-1324 | sch3.1 | A presentation or disallowance exemption applies to secondary legislat | encoded | nz-schedules.l4: Schedule 3 |
| 1325 | sch3.2 | Any term or expression that is used in this schedule in relation to an | encoded | nz-schedules.l4: Schedule 3 |
| 1326 | sch3.3 | See also clause 32 of Schedule 1 for transitional presentation exempti | inert (1: not operative) | not operative -- Schedule 3: signpost to Schedule 1 clause 32 |
| 1327 | sch3.tbl.1327 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1328-1330 | sch3.tbl.1328 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1331-1333 | sch3.tbl.1331 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1334-1336 | sch3.tbl.1334 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1337-1339 | sch3.tbl.1337 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1340-1342 | sch3.tbl.1340 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1343-1345 | sch3.tbl.1343 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1346-1348 | sch3.tbl.1346 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1349-1351 | sch3.tbl.1349 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1352-1354 | sch3.tbl.1352 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1355 | sch3.tbl.1355 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1356 | sch3.tbl.1356 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1357 | sch3.tbl.1357 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1358 | sch3.tbl.1358 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1359 | sch3.tbl.1359 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1360 | sch3.tbl.1360 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1361-1363 | sch3.tbl.1361 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1364-1367 | sch3.tbl.1364 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1368 | sch3.tbl.1368 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1369 | sch3.tbl.1369 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1370 | sch3.tbl.1370 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1371 | sch3.tbl.1371 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1372 | sch3.tbl.1372 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1373 | sch3.tbl.1373 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1374 | sch3.tbl.1374 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1375 | sch3.tbl.1375 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1376 | sch3.tbl.1376 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1377 | sch3.tbl.1377 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1378 | sch3.tbl.1378 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1379-1384 | sch3.tbl.1379 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1385 | sch3.tbl.1385 | table row: Exemption applies if exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1386-1387 | sch3.tbl.1386 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1388-1389 | sch3.tbl.1388 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1390 | sch3.tbl.1390 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1391 | sch3.tbl.1391 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1392 | sch3.tbl.1392 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1393 | sch3.tbl.1393 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1394 | sch3.tbl.1394 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1395 | sch3.tbl.1395 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1396 | sch3.tbl.1396 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1397 | sch3.tbl.1397 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1398 | sch3.tbl.1398 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1399 | sch3.tbl.1399 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1400 | sch3.tbl.1400 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1401 | sch3.tbl.1401 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1402 | sch3.tbl.1402 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1403-1405 | sch3.tbl.1403 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1406 | sch3.tbl.1406 | table row: Exemption applies while exemption ground is met | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` and `the exemption ground is met in the way the deposited text shows` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1407 | sch3.tbl.1407 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1408 | sch3.tbl.1408 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1409 | sch3.tbl.1409 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1410 | sch3.tbl.1410 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1411 | sch3.tbl.1411 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1412 | sch3.tbl.1412 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1413 | sch3.tbl.1413 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1414 | sch3.tbl.1414 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1415 | sch3.tbl.1415 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1416 | sch3.tbl.1416 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1417 | sch3.tbl.1417 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1418 | sch3.tbl.1418 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1419 | sch3.tbl.1419 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1420 | sch3.tbl.1420 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1421 | sch3.tbl.1421 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1422 | sch3.tbl.1422 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1423 | sch3.tbl.1423 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1424 | sch3.tbl.1424 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1425 | sch3.tbl.1425 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1426 | sch3.tbl.1426 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1427 | sch3.tbl.1427 | table row: Exemption applies | encoded | nz-schedules.l4: `a presentation or disallowance exemption applies under Schedule 3` -- the provision and type cells of this row did not survive the conversion: the match is an input (NOTES.md finding on Schedule 3) |
| 1428 | h1428 | Schedule 4 — Secondary legislation subject to confirmation by Act | inert (1: not operative) | heading -- a heading creates no rule |
| 1429 | x1429 | Legislation that needs to be confirmed by Act before deadline | repealed or blank in this text | blank in this text -- Schedule 4: the lists of empowering provisions are not in the deposited text; only the part heading survives |
| 1430 | x1430 | Legislation that has no previous effect if not confirmed by deadline | repealed or blank in this text | blank in this text -- Schedule 4: the lists of empowering provisions are not in the deposited text; only the part heading survives |

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes. Each row gives the readings seen, the one taken, the text that licenses it, and the rule that encodes it. The tests assert the reading taken; none asserts the other.

| Fork | The question | Readings seen | Taken | The text that licenses it | Encoded in |
| --- | --- | --- | --- | --- | --- |
| F1 | The converter dropped the rule cells of s 54's table. What are the rules? | (a) the rules as the Act's table states them, from memory; (b) the rule each Item's example shows | (b). Wording from memory is not an allowed source | lines 383-389 (Items 1 to 7) | `the first day of a period that is`, `the last day of a period that is`, `the last day of a period of days`, `the earliest day for the second event if at least` (nz-interpretation-time.l4) |
| F2 | Does a period "from" or "after" a day count that day? | the day counts; the day does not count and the period starts the next day | the next day. "Within N days of" an event leaves out the event's day and ends at the close of the Nth day after it | Item 2 (line 384: "operates from 30 June" starts on 1 July); Item 3 (line 385: "within 10 days of" 1 August, by the close of 11 August); s 56 example 3 (line 400: "after" 2 August starts on 3 August "under item 2") | `the first day of a period that is`, `the last day of a period of days` |
| F3 | s 27(b) (from a particular day: the start of the next day) and (c) (a stated time on the date it comes into force) both apply. Which prevails? | (b); (c); neither | neither: NOTHING | lines 218-222 list the three cases and give no precedence | `the moment at which legislation comes into force` |
| F4 | Does s 55 reach a period of months, or only a period of days? Must the thing be done on the next working day, or may it? | days only; any limited period, months included; "must" | any limited period; "may" | line 391: "within a limited period of time ... may ... be done on the next working day" | `the last day on which the thing may be done under section 55` |
| F5 | What is a period of years? | 12 months; a calendar year; 365 days; no answer | no answer: NOTHING | none. s 13 defines month only (line 127) and s 56 speaks only of months (lines 392-396) | `the last day of a described period`; the look-up `what the Act says of` |
| F6 | What is a period of weeks? | 7 days; no answer | no answer: NOTHING | none: the Act does not define week | the same |
| F7 | s 12 says legislation has no retrospective effect. Can legislation say otherwise? | no; yes | yes, because s 12 is a provision of Part 2 and s 9(1)(a) lets the legislation provide otherwise | lines 94-96 (s 9(1)); line 107 (s 12) | `legislation applies to a circumstance as it arises`; `whether the legislation applies to a circumstance that arose on` |
| F8 | s 29(1)(b): a re-exercise of a commencement power must take effect "before the commencement takes effect". On the commencement day itself? | before the day; before the moment | before the moment: a re-exercise that takes effect on the commencement day is not before it, unless the order states a time and the re-exercise is earlier than that time | line 235 (s 29(1)(b)); line 219 (s 27(a): the start of the day) | `a commencement order may be amended, revoked or replaced by a re-exercise of the power taking effect on` |
| F9 | s 34(1): an offence "committed before" the repeal or amendment. On the day the repeal takes effect? | before the day; before the moment | before the moment: a repeal takes effect at the start of its day, so an offence committed on that day is not before it | line 267 (s 34(1)); line 291 (s 39(1)); line 219 (s 27(a)) | `the liability for an offence or breach committed on ... is unaffected by a repeal or amendment taking effect on` |
| F10 | s 90: changes take effect as if enacted "having effect immediately before" the day they were made. An amendment taking effect on that day? | sees the changes; does not | sees the changes (on or after that day) | line 684 | `the changes are treated as already enacted for an amendment, incorporation or reference taking effect on` |
| F11 | When a case fails the section's own condition, or is off its closed list, does a function answer "this section does not give it" (JUST FALSE) or "the Act does not say" (NOTHING)? | (a) NOTHING for everything the section does not mention; (b) JUST FALSE for a case scoped to the section's OWN grant, duty or permission that fails that section's own "if", "only if" or "as long as" or is not on its closed list of grants, and NOTHING where the section only draws the edge of an extension or another authority is expressly preserved (the first version, a working instruction of the lead's on 2026-10-29); (c) JUST FALSE only where the text's own words say no ("means", "if", "only if", "as long as", "unless", or a list closed with "only"), and NOTHING for a list of grants the text does not close | (c), from 2026-10-29. **Assumed, not ruled by a lawyer**: (b) was replaced by (c) the same day, on a second opinion, because its "closed list of grants" with no closing word was the encoder inferring a no the text does not say; six functions changed, see "Replaced 2026-10-29" below | the sections' own words, for example s 43(1) and (2) (lines 306-319: a closed list of grants, then "only if"), s 34 (lines 266-271: three purposes), s 69, s 72(1)(a), s 87, s 95(2), s 131(1), s 133(5), Schedule 1 cll 13(4) and 15(6). The function-by-function answers are in the two tables below | every function in the tables below |
| F12 | What is the anniversary of a date, in particular of 29 February? | 28 February; 1 March; no answer | no answer: NOTHING, for every date | none. "Anniversary" is used in s 2(1)(c) (line 12) and Schedule 1 cl 15(5) (lines 1162-1163) and defined nowhere, and a year is not defined (F5) | `the anniversary of` (nz-interpretation-time.l4) |
| F13 | s 28 counts commencement "a number of months after" a day. What of "10 days after", "2 weeks after", "a year after"? | s 28's count extended to days, weeks and years; s 54 Items 2 and 3 (the period starts the next day); no rule | no rule: NOTHING for days, weeks and years; months go to s 28 | line 224 ("a number of months after"), line 228 ("instead of section 56 (on months generally)") | `the day of commencement when expressed as` |
| F14 | s 39(1) speaks of legislation repealed "on" a particular day. What of legislation expressed to be repealed "from" a day? | like "on": at the start of that day; like s 27(b): at the start of the next day; no rule | no rule: NOTHING, both for the moment of repeal and for whether the legislation is still in force | lines 291-292: s 39 speaks only of "on" and "until"; s 27(b) gives "from" for commencement only | `the moment of repeal of legislation expressed to be repealed from`; `legislation expressed to be repealed from ... is still in force on` |
| F15 | Schedule 2 cl 3(1)(c): which languages are "official New Zealand" languages? | English only; English, te reo Māori and New Zealand Sign Language; no answer | no answer: NOTHING for every language, because the Act does not say and the deposited sources contain no other law | line 1309 | `is an official New Zealand language` |
| F16 | s 2(1)(c): the rest of the Act comes into force "on 1 or more dates set by Order in Council; or, to the extent not brought into force earlier, on the fifth anniversary" of the Secondary Legislation Act 2021's Royal assent. What if an Order in Council sets a date later than that anniversary? | the Order's date stands; the fifth anniversary prevails for whatever was not brought into force earlier; the Order is ineffective for the later date | none taken: s 2 is the Act's own commencement (inert, reason 2) and is not encoded, so no test asserts any reading | lines 8-12 | not encoded; registered so that nobody reads the encoding as having decided it |
| F17 | s 119(2): at what moment on the day does an amendment or replacement by resolution take effect? | the start of the day (as s 27(a) for commencement and s 39(1) for repeal); the close of the day; a time the resolution states | the encoding answers with the DAY only and says nothing of the moment | lines 814-816: "takes effect on the later of the 28th day after a copy of the resolution is published and any date stated in the resolution" | `the day an amendment or replacement by resolution takes effect` |
| F18 | Schedule 2 cl 3(1)(a)(ii): material is made available for inspection "in any other case". Which other case? | only where (i) fails because Internet access would infringe copyright; any case where the material is not made available on the Internet site, for whatever reason | the first | lines 1305-1307: "free of charge, unless doing so would infringe copyright; or in any other case, available for inspection" | `the material is made publicly available as clause 3 requires` |
| F19 | s 135(4): the Chief Parliamentary Counsel may be removed for inability, bankruptcy, neglect of duty, "or misconduct proved to the satisfaction of the Governor-General". How far back does "proved to the satisfaction of the Governor-General" reach? | misconduct only; all four grounds | none taken: s 135 is machinery (inert, reason 2) and is not encoded | line 914 | not encoded |
| F20 | s 96(3)(b): "update any monetary amount (other than an amount specified for the purpose of jurisdiction or an offence or penalty) ... or provide for the amount to be prescribed by Order in Council". Does the exclusion also bar the Order in Council option? | the exclusion bars both; it bars only the update | both: "the amount" in the second limb is the amount of the first, which excludes those amounts | line 730 | `a revision Bill may make this change` (the three monetary-amount members) |
| F21 | Schedule 1 cl 15(5): the list deadline is an anniversary, that is, a day. Which moment of that day is the deadline? | the start of the day; the close of the day | "before the list deadline" (cl 15(3)) means on an earlier day, and an exemption "until the list deadline" (cl 15(2)) runs through the deadline day, reading "until" as s 39(2) does ("until the close of that day"), by analogy | lines 1149-1164 (cl 15), line 292 (s 39(2)) | `the minimum legislative information is lodged in time on`; `a list exemption applies on` |
| F22 | s 13 terms built on "includes" or "means ... and include": what of a candidate that is off the list? | not covered (FALSE); the Act does not say (NOTHING) | NOTHING, for instrument (line 60), Commonwealth country and part of the Commonwealth (line 115), North Island and South Island (lines 131 and 151), office (line 132), person (line 134) and repeal. "Gazette" (line 120) says "means", so it is closed and a journal that is not the Gazette is JUST FALSE | the verb each definition uses | the look-ups in nz-part2-definitions.l4 and `is an instrument` |
| F23 | Two terms are defined twice. "regulations": Schedule 1 cl 2 (line 1049: "has the meaning set out in clause 11(2)") and cl 7 (line 1075: the meaning in section 29 of the Interpretation Act 1999, for legislation enacted or made before the main commencement date). "person": s 13 (line 134) and Schedule 1 cl 6 (line 1070, for legislation enacted or made before 1 November 1999). | one glossary entry each, with the second as a rule; two entries | "person": two entries (one for s 13 and one for cl 6), each with its own look-up. "regulations": ONE entry (cl 2, pointing at cl 11(2)), with cl 7 as a rule in nz-schedules.l4 | the two places the Act defines each | the glossary (86 entries); `regulations has the meaning in section 29 of the Interpretation Act 1999 for legislation enacted or made on`; `counts as a person under section 13`; `is within the saved meaning of the pre-1 November 1999 term` |

**Fork F11 in detail.** (Superseded in part on 2026-10-29: the paragraph beginning "Replaced 2026-10-29" below states the rule now in force; where the two differ, that one governs.) FALSE here means "this section does not give it"; NOTHING means "the Act does not say". The rule applied: a function scoped to a section's own grant, duty or permission gives JUST FALSE when the case fails that section's own condition ("if", "only if", "as long as") or is not on its closed list. In practice that means: JUST FALSE when the section hands out a defined class (a closed list, or an "if", "only if" or "as long as") and the case is outside it; NOTHING when the section extends a power or a rule that has terms of its own (a power that "includes" more, a "may" added to a power, a scope clause naming the powers it reaches), because a case outside the extension is governed by the power's own terms, as the lead directed for s 53(2)(c); NOTHING where another authority is expressly preserved (s 47's Minister, s 86(3), s 96(6)); and NOTHING, as a judgment of mine, where the function asks the opposite of what a protection gives (below). Every function that returns a `MAYBE` and has a NOTHING branch was listed with `grep -nE '(THEN|OTHERWISE|ELSE) NOTHING' nz-*.l4` over the layer-1 modules (not the tests) and sorted into one of the two tables; the closed-"means" definitions of sections 5(1) and 13 are swept separately, by `sweep_lists.py` (section "Lists" below).

**Replaced 2026-10-29.** The rule in force for this row is: A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if", "as long as" or "unless", or a list the text closes with "only" or an equivalent. Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the function answers `NOTHING`, and a comment on that branch names which of those it is. The function's name carries the scope its `FALSE` claims ("under section 47 ...", not "may I ..."), and a seat question that asks Act-wide inherits `NOTHING` wherever the Act points outside itself.

Under it six functions moved from `JUST FALSE` back to `NOTHING`, each because the text lists grants, duties or recipients without closing the list: s 47 `someone else`, s 64(1) `something else`, s 87 `another change`, s 95(2) `anything else`, s 133(5) `anyone else` and Schedule 1 clause 13(4) `another change`. Twelve assertions were restated with them (eight in the encoder's test files, four in `tests-independent.l4`), each with a `-- RECONCILED 2026-10-29` comment that quotes the original. The other `JUST FALSE` sites were read against the text and kept, because each rests on the text's own "means", "if", "as long as", "unless" or "only": s 34(2), s 43(1) and (2), s 64(1)(c), s 69(1), s 72(1)(a), s 77, the conditions of s 87, s 131(1) and Schedule 1 clause 15(6). Two of those are marginal and are for a lawyer: s 69(1) (the Act speaks to the case in s 69(3), "may also publish", but does not say "no duty") and s 72(1)(a) ("as far as practicable" qualifies the duty; the function answers `JUST FALSE` both for legislation the PCO did not publish and for access that is not practicable). Function names were not changed to carry their section; the scope of each `FALSE` is in its `@ref` and the comment above it. This reading was made by the lead and a second reader, not by a lawyer.

Answers that are now JUST FALSE (the section's own grant, duty or permission; the answer was NOTHING before this pass):

| Provision | Module | Case that now gives JUST FALSE |
| --- | --- | --- |
| s 34(2) | nz-part2-commencement-repeal.l4 | `another purpose`: the old law is used for three purposes only |
| s 43(1), (2) | nz-part2-powers.l4 | `doing an act or thing that is not for the purposes of the legislation` |
| s 64(1)(c) | nz-part2-revision-incorporation.l4 | technical material that is neither impracticable nor too large |
| s 69(1) | nz-part3-publication.l4 | secondary legislation not drafted by the PCO (the PCO's duty to publish is listed) |
| s 72(1)(a) | nz-part3-publication.l4 | published but not practicable to access; not published |
| s 77 | nz-part3-publication.l4 | `any other body` (relevant central government entity); `another obligation` (international transparency obligations): both are "means" |
| s 87 | nz-part3-editorial-revision.l4 | the six kinds that attach a condition ("if", "as long as"), with the condition false |
| s 131(1) | nz-part6-7-pco-regulations.l4 | outside the rules of the House: not a confidential communication; not between a client and counsel |
| Schedule 1 cl 15(6) | nz-schedules.l4 | `anything else` |

Answers that stay NOTHING, and why. The first group is the lead's list (the section only draws the edge, or another authority is preserved); the rest are my sorting of the other NOTHING branches, **assumed, not ruled**.

| Provision | Case | Why NOTHING |
| --- | --- | --- |
| s 47 | the office holder is a Minister of the Crown | "other than a Minister of the Crown" only draws the edge of the section |
| s 47 | `someone else`, for an office holder who is not a Minister | "may be exercised by 1 or both of the following": the list is not closed with "only" (rule of 2026-10-29) |
| s 64(1) | `something else` | "sufficient authority ... to incorporate 1 or more of the following": not closed with "only", and subsection (4) preserves other powers (rule of 2026-10-29) |
| s 87 | `another change` | "The following changes may be made under this subpart": not closed with "only", and s 86(3) preserves other authority (rule of 2026-10-29) |
| s 95(2) | `anything else` | "must set out" three things: not closed with "only" (rule of 2026-10-29) |
| s 133(5) | `anyone else` | "may be made to" two kinds of recipient: not closed with "only" (rule of 2026-10-29) |
| Schedule 1 cl 13(4) | `another change` | "the following changes": not closed with "only" (rule of 2026-10-29) |
| s 53(1), (2) | power A is not a power to prescribe a form; `another part` | the section extends a power to prescribe a form and says nothing of any other power |
| s 86(1) | the Chief Parliamentary Counsel has not authorised the change | s 86(3) (line 632) preserves authority under s 38 or any other legislation, so the section does not say the PCO may NOT make the change. The comment above the function said more than that and was corrected |
| s 31 | `a change of another kind` | the section extends "repeal" and "amendment" to three further kinds (lines 245-249): an extension |
| s 32 | `has another effect` | the section says what a repeal or amendment does not do; any other effect is not its subject |
| s 37 | when the two conditions of s 37 are not met | the function returns what a reference is a reference to, not a yes or no; where s 37 does not deem, there is no value |
| s 45 | `another power`; appointing a replacement for someone incapacitated in a way that does not affect the performance of the duty | the power to appoint "includes" the listed powers: an open list |
| s 46 | the power is not exercised to correct an error | the function asks whether the power may be exercised again, with an input for the power's general capability; s 46 adds one case, and the general capability is governed by another authority (the power's own terms; s 51), so outside that case the answer is not s 46's to give |
| s 48(1), (2); s 49; s 50 | `something else`; `another way`; a power outside the section's scope (not one of declaring, prescribing or specifying, for s 50) | s 48 and s 49 say a power "includes" a further power, and s 50 adds a "may" to a power its scope clause names: each extends a power that has terms of its own, as s 53 does |
| s 79A | `another note or information` that is not clearly identified as not forming part of the legislation | the section says what an identified item is; it is silent about an unidentified one |
| s 96 | `another change` | s 96(6) says the changes "include (without limitation)" those of subpart 2: an open list |
| s 5(1) | `is an instrument` for an Act, a part of an Act or a Bill | "instrument includes ...": an open list |
| s 13 | the "includes" terms (fork F22) | the verb is "includes" |
| Schedule 1 cl 6 | `another term` | the look-up returns the saved meaning of one of four terms; for any other there is no value |
| Schedule 1 cl 18 | `any other section of subpart 1 of Part 3` | such sections are those "specified in the regulations", which are not among the sources |
| Schedule 1 cl 32(1), (2) | secondary legislation made on or after the publication deadline | the clause "applies to secondary legislation made before the publication deadline"; outside that scope it says nothing, and inside it the "only if" limbs give JUST FALSE when they fail |
| Schedule 2 cl 3(1)(c) | every language (fork F15) | the Act does not say which languages are official |
| Schedule 3 | the meaning of a term used in the tables | the tables lost their empowering-provision cells (finding 14) |

Three NOTHING branches are judgment calls about the **polarity of the question**, not about the ruling: s 40(2) ("secondary legislation is not invalid just because ... as long as its making is authorised by other legislation"), s 52 ("a form is not invalid just because of minor differences") and s 146 ("no proceeding may be brought"). Each is a protection, and the function asks the opposite of what the section gives (is it invalid? may a proceeding be brought?). Inside the protection the answer is JUST FALSE; outside it the section says nothing about invalidity or liability, so NOTHING. Read as "does the section protect it?", the same cases would give JUST FALSE. They are listed here for the lead to rule.

## What the text turns out to say

Each finding ends "Asserted." where a test or a seat case asserts it, and says which file.

1. **The table in s 54 reached the deposited text without its rule cells.** Only the lead-in (lines 380-381), the word "Examples" (382) and Items 1 to 7 (383-389) survive. Each rule is read from what its example shows (fork F1), and none is written from memory. Asserted: nz-tests-time.l4, one test for each Item.
2. **The Act defines "month", "working day" and "sitting day", and nothing else about time.** "month means a calendar month" (line 127); "working day" (lines 153-158); "sitting day" (line 80). It does not define day, week or year, and s 56 speaks only of months. A period of weeks or years therefore has no answer from this text (forks F5 and F6): the functions return NOTHING. Worked cases 1, 2, 3 and 7. Asserted: nz-tests-time.l4 and nz-cases-seat.l4.
3. **"From" or "after" a day starts the period on the next day; "within N days of" an event leaves out the event's day and ends at the close of the Nth day after it** (Items 2 and 3, s 56 example 3). Thirty days from 1 January 2026 start on 2 January and end at the close of 31 January 2026. Asserted.
4. **A period of months is counted by s 56, but commencement by months (s 28) is counted differently, and s 28 says it applies "instead of section 56".** Two months from 31 December 2025 start on 1 January 2026 (Item 2), the ending month is March, and the period ends immediately before 1 March: the close of 28 February 2026. One month from 31 January 2024 starts on 1 February, and ends immediately before 1 March: the close of 29 February 2024, a leap year. Counting from the 31st itself instead of from the next day gives the same last day for both (February has no 31st, so the period ends at the close of the last day of February). Under s 28, "a month after" 1 July 2020 is 1 August 2020 and "4 months after" 31 May 2020 is 30 September 2020: the legislation comes into force on the corresponding day, or on the last day of that month if there is none. Asserted.
5. **Section 55 only permits.** The thing "may ... be done on the next working day", and it reaches "a limited period of time", so months as well as days (fork F4). The thirty days from 1 January 2026 end on a Saturday, 31 January 2026, so the thing may be done on Monday 2 February 2026. Two months from 31 December 2025 end on Saturday 28 February 2026, so Monday 2 March 2026. One month from 31 January 2024 ends on Thursday 29 February 2024, a working day, so nothing moves. Asserted.
6. **"Working day" turns on seven days the Act names and does not date** (lines 153-158): Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Te Rā Aro ki a Matariki/Matariki Observance Day and Labour Day. It also leaves out 25 December to 2 January, the Monday after a Friday 1 January, the Monday and Tuesday after a Saturday or Sunday 1 January, and the Monday after Waitangi Day or Anzac Day on a weekend. The seven dates are inputs, and a question that needs a date outside the year supplied returns NOTHING. Asserted.
7. **Commencement (ss 25 to 27).** An Act comes into force on the date stated or provided for, else the day after Royal assent; its Title, commencement sections and any principal legislation provision come into force on Royal assent. Secondary legislation likewise, with "the day after it is published or first made available" and "on its making" for its Title and commencement provisions. An enactment comes into force at the start of the day, "from" a day at the start of the next day, or at a stated time; when the last two both apply the text does not say which prevails (fork F3): NOTHING. Asserted.
8. **A repeal on a particular day takes effect at the start of that day, and "until" a day runs to the close of that day** (s 39). Asserted.
9. **What a repeal or amendment leaves alone (ss 33 to 36).** Existing rights, interests, titles, immunities, duties, status and capacity, and proceedings started or in progress, survive; liability for an offence committed before the repeal survives, and the old law may still be used to investigate it, start or finish a proceeding for it, and impose a penalty or order; powers exercised and legislation made under the repealed legislation continue to have effect. A repeal takes effect at the start of its day, so an offence committed on the day itself is not committed "before" it (fork F9). Asserted.
10. **Posting (s 17).** A document that the legislation lets be sent by post is taken to be sent if properly addressed, prepaid and posted, and received when it would be delivered in the ordinary course of post (a fact the caller supplies), unless the contrary is proved. Section 17(5) points to Part 4 of the Contract and Commercial Law Act 2017 for electronic communications, which is not among the sources: whether it applies is an input. Asserted.
11. **Section 12 can be displaced.** It is a provision of Part 2, and s 9(1)(a) lets legislation provide otherwise (fork F7). Asserted.
12. **An example in legislation does not limit the provision it illustrates (s 23), except an example in legislation enacted or made before the main commencement date, or in a later amendment to it** (Schedule 1 clause 4), and that exception itself gives way where the legislation provides otherwise or the context requires a different reading. For the excepted case the text does not say what the example does, so the answer is NOTHING. Asserted.
13. **The Act dates none of its own commencement dates.** The main commencement date, the publication commencement date and the anniversaries and deadlines of Schedule 1 are dates the Act names but does not give; each is a `DATE` input. Asserted.
14. **Schedule 3's tables reached the deposited text with only their result cells.** Lines 1327-1427 are "Exemption applies" or "Exemption applies if exemption ground is met", with the text of six grounds; the cells that name the empowering provision and the kind of exemption are gone. So this encoding cannot say which provisions are exempt: the match against the tables is an input to `a presentation or disallowance exemption applies under Schedule 3`, and the six grounds are listed. Asserted: nz-tests-schedules.l4 (the rule, and each ground).
15. **Part 4 (ss 101 to 112), section 148, Schedule 1 clauses 30 and 31, Schedule 1A and the lists of Schedule 4 have headings and no body in the deposited text.** They are rows "repealed or blank in this text"; nothing is inferred about what they say.
16. **Section 54 Item 7 counts working days between two events and counts neither end day.** With ten working days required after Monday 2 February 2026, the working days between are 3, 4 and 5 February (Friday 6 February 2026 is Waitangi Day), 9 to 13 February, 16 and 17 February: ten days, so the earliest day for the second event is Wednesday 18 February 2026. The text does not require the second event to fall on a working day. Asserted: nz-cases-seat.l4.
17. **Disallowance and confirmation.** Secondary legislation is disallowed if a member of the review Committee gives notice of a motion to disallow it and none of withdrawal, disposal by the House, or dissolution happens before the deadline, which is the close of the 21st sitting day after the notice (s 117); the House's sitting days are an input, because the Act fixes none. Legislation to which the confirmation subpart applies (made under an empowering provision listed in Schedule 4, which the deposited text does not give) must be confirmed on or before the close of 30 June (if made from 1 January to 30 June) or 31 December (if made from 1 July to 31 December) of the next year, and is revoked on that deadline if it is not (ss 121 to 124); a duty, levy or road user charge imposed under it is cancelled and refunded, except the three listed kinds (s 125). Asserted.
18. **Borrowed facts are inputs.** The Acts the text refers to but does not contain (the Interpretation Act 1999, the Time Act 1974, the Contract and Commercial Law Act 2017, the Public Finance Act 1989, the Care of Children Act 2004 and others) are not among the sources; each fact taken from one of them is a plain input (for example: the New Zealand offset from UTC for s 57, whether Part 4 of the Contract and Commercial Law Act 2017 lets a written requirement be met electronically, whether a body is a department within the Public Finance Act 1989). Asserted.

19. **A closed definition answers JUST FALSE for what is off its list; an open one answers NOTHING.** "Means" closes the list: a journal that is not the Gazette, a body Schedule 2 of the Public Service Act 2020 does not name, any other body or another obligation in s 77 are JUST FALSE. "Includes" and "means ... and include" leave the list open (fork F22): NOTHING. Asserted: nz-tests-part2-definitions.l4, nz-tests-part1.l4, nz-tests-part3-publication.l4.
20. **Commencement counted in days, weeks or years has no rule** (forks F13, F5, F6). Section 28 applies "to legislation expressed to come into force a number of months after" a day, and says it applies instead of section 56 on months. Asserted: nz-tests-time.l4 and nz-cases-seat.l4.
21. **Three things the Act never defines return NOTHING:** an anniversary (F12), legislation repealed "from" a day (F14), and an official New Zealand language (F15). Asserted: nz-tests-time.l4 and nz-tests-schedules.l4.
22. **Section 25(3) and section 26(3) keep the Title, the commencement section and any principal legislation provision out of what a reference in the commencement section includes** (lines 212 and 217). For an ordinary provision the text says nothing, so the answer is NOTHING. Asserted: nz-tests-time.l4.
23. **Section 76(1) and 76(2) are two duties and are encoded as two functions.** (1) is about a link forwarded to the PCO under s 75 (published electronically as soon as practicable and, as far as practicable, accessible at or downloadable from the legislation website); (2) is about the directions the Chief Parliamentary Counsel must ensure are in force for secondary legislation with international transparency obligations. Section 76(4), that a direction under the section is secondary legislation, is its own function. Asserted: nz-tests-part3-publication.l4.
24. **A version that is both a consolidation and includes subpart 2 changes carries both statements (s 79(1)(b) and (c)(i)),** so it has a result of its own: the consolidation statement and the subpart 2 statement together. Asserted: nz-tests-part3-publication.l4 and nz-cases-seat.l4.
25. **Words shown only on a screen are neither in nor out of "writing".** Section 13 requires "a visible and tangible form and medium (for example, in print)" and does not say whether a screen is tangible. `is writing` returns NOTHING for them, JUST FALSE for words that are only spoken, and JUST TRUE for print and for words fixed on paper or an object; `a requirement to put something in writing is met` passes the NOTHING through. Asserted: nz-tests-part2-definitions.l4 and nz-cases-seat.l4.

## Worked cases

The seven cases of the brief, with the section that decides each. "Silent" means the Act has no provision and the encoding returns NOTHING. Every answer was decided from the text before the encoding was run; each is asserted in nz-tests-time.l4 (the section "Seven worked cases (brief)"), and again in nz-cases-seat.l4 (question `On which day does my period end`, with the s 55 step under `Until which day may I do the thing if my last day is not a working day`).

| # | Case | Answer | Sections |
| --- | --- | --- | --- |
| 1 | three years from 2025-07-16 | silent: the Act does not define a year | s 13 (defines month only), s 54, s 56 |
| 2 | five years from 2025-01-15 | silent | the same |
| 3 | five years from 2025-09-01 | silent | the same |
| 4 | thirty days from 2026-01-01 | the period starts on 2026-01-02 and its last day is 2026-01-31 (a Saturday); s 55 lets the thing be done on Monday 2026-02-02 | s 54 Items 2 and 3; s 55 |
| 5 | two months from 2025-12-31 | the period starts on 2026-01-01 and ends at the close of 2026-02-28 (a Saturday); s 55 lets the thing be done on Monday 2026-03-02 | s 54 Item 2; s 56; s 55 |
| 6 | one month from 2024-01-31 | the period starts on 2024-02-01 and ends at the close of 2024-02-29 (a Thursday, a working day) | s 54 Item 2; s 56 |
| 7 | one year from 2024-02-29 | silent | as 1 |

## Reading a result: FALSE and NOTHING

The rule in force for this row, from 2026-10-29 (assumed, not ruled by a lawyer; fork F11 and its "Replaced 2026-10-29" paragraph say how it came about):

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if", "as long as" or "unless", or a list the text closes with "only" or an equivalent. Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the function answers `NOTHING`, and a comment on that branch names which of those it is. The function's name carries the scope its `FALSE` claims ("under section 47 ...", not "may I ..."), and a seat question that asks Act-wide inherits `NOTHING` wherever the Act points outside itself.

In plain words: `JUST FALSE` is the Act's own "no"; `NOTHING` is "the Act does not say". A caller must not read `NOTHING` as "no".

## Known limits

Sorted by cause, so that nobody mistakes a gap in the text, a deliberate input and a rule left out for one another.

**(i) Machinery, not encoded (inert, reason 2; 80 rows of the coverage table).** The Act's own commencement (s 2) and title (s 1); the office, staffing and powers of the Chief Parliamentary Counsel and of the PCO as an employer (ss 128 to 145); the regulation-making powers, section 147 (one row for each purpose of regulations) and section 147A, Schedule 1 clause 19; and the saving for an existing appointment, Schedule 1 clause 35. A question about any of these has no function to ask, and a question that turns on what regulations say, once made, gets an input. Forks F16 (s 2(1)(c)) and F19 (s 135(4)) sit here: they are registered, not decided.

**(ii) Inputs by design.** The Act names things it does not give, and this encoding asks the caller for them: the calendar of the seven named days of section 13; the House's sitting-day list (section 117's 21st sitting day); the date of Royal assent for any commencement; the main commencement date, the publication commencement date and the anniversaries and deadlines of Schedule 1 (the Act dates none of them); the New Zealand offset from UTC (s 57); and every fact taken from an Act that is not among the sources. A question that needs a day outside the calendar supplied returns NOTHING.

**(iii) Lost in the rendering.** The deposited text is a converter rendering (finding 15 and the section "The text, and what it is"), and these gaps are the converter's, not the Act's:

- Schedule 1A is a bare heading (line 1288). Section 5(1)'s limb (b) of "secondary legislation" (an instrument made under the Royal prerogative in a form and for a purpose set out in Schedule 1A) therefore takes its form-and-purpose fact as an input.
- Schedule 3 kept only the result cells of its tables; the column that names the empowering provision is gone (finding 14), so which provisions are exempt is an input.
- Schedule 4 has two column headings (lines 1429 and 1430) and nothing else, so the list of empowering provisions to which the confirmation subpart applies is not available (finding 17).
- Part 4 (ss 101 to 112, lines 762-773), section 148 (line 1029) and Schedule 1 clauses 30 and 31 (lines 1262-1263) are headings with no body.
- Section 74 lost its paragraph letters (lines 527-532 carry no letters), so a citation of "section 74(1)(aa)" (line 968) or of "section 74(1)(a)" (line 1139) cannot be matched to a paragraph.
- Schedule 1 clause 18 (line 1186) calls section 73 "(secondary legislation does not commence until published)", and section 147 (line 985) calls it "the prohibition on coming into force before publication under section 73". The rendered section 73 (line 523) is headed "Maker must publish secondary legislation not published by PCO (if required)", and clause 15 (line 1153) speaks of section 73 "as in force immediately before the publication commencement date". The deposited text therefore holds the version of section 73 that applies before the publication commencement date; this encoding follows the rendered section 73 and does not encode the prohibition the other passages describe.

Each coverage row's disposition was re-checked after this pass: the table below still gives every one of the 1,430 lines exactly one row and every row exactly one disposition.

## Lists: what was split and what was left whole

Ruling C of the second pass: where a printed item names several things, the printed phrase **and** each thing it names must be answerable. `sweep_lists.py` checks this against `lists-decisions.tsv`; it fails on any enumeration member that names several things (an " or ", an " and ", a comma or a slash, after the fixed pairs listed there as DOUBLET rows are blanked) that has neither a SPLIT row (its constituents are constructors of the same type, and every one is named in a test) nor a WHOLE row (with a reason), on a stale row, and on any definition in section 5(1) or section 13 that lists things and has neither a LOOKUP row (a function that exists and is called in a test, closed for "means" and open for "includes" and "means ... and include") nor a WHOLE row. Its output, unedited:

```
enumerations: 84; constructors: 642; naming several things: 108 (SPLIT 75, WHOLE 33, undecided 0)
doublets blanked out before flagging: 30
definitions in sections 5(1) and 13 that list things: 32 (LOOKUP 27, WHOLE 5, undecided 0)
problems: 0
```

What it does not check: that the constituents named are the right ones (only that they exist), that a constructor without a list marker is not secretly a list, and the lists in definitions outside sections 5(1) and 13 (sections 63, 68(4), 77, 85, 94, 96(4), 121, 131(3), 141(2) and 147(6), and Schedule 1 clauses 2 and 6), which are covered where they are covered by enumerations. The "lead's named cases" all have SPLIT rows: s 45 related powers; the s 87 obvious errors (typographical, clerical, grammatical, spelling, punctuation, numbering, cross-referencing, alphabetical ordering, and the two amendment-related errors); s 96(2)(a) and (2)(f); s 64's international or national organisation; s 77's department and departmental agency; the Schedule 3 chief executive ground (four limbs); and the two alternative names of the islands (a look-up, `the headword of the section 13 definition that covers`, with `Te Ika-a-Māui` and `Te Waipounamu`, and `public notice` for public notification).

**Fixed pairs blanked before testing for a list** (DOUBLET rows):

| Phrase | Why it is one thing |
| --- | --- |
| done or suffered | the Act's own pair in sections 31 and 32 ("anything done or suffered"): one class of thing, and the Act draws no line inside it |
| offence or breach | section 34's own pair for one wrong: the Act treats an offence and a breach alike in every limb |
| name or title | section 87's own pair ("the name or title"): the Act treats the two as one |
| approve or prescribe | section 53's own pair of verbs for one power over a form, method, format or medium |
| whole or part | section 96(2)(a)'s "the whole or part of 1 or more Acts": the Act does not distinguish |
| Title or Titles | a singular and its plural; section 19 says the singular includes the plural |
| class or classes | a singular and its plural; section 19 says the singular includes the plural |
| holder or holders | a singular and its plural; section 19 says the singular includes the plural |
| new or additional | two words the Act uses for one inclusion in a revision Bill |
| legislation or provisions | the Act's pair for the thing a repeal recommendation is about: either alike |
| inserted, omitted or changed | the three operations of one editorial power in section 87(1)(g): the Act draws no line between them |
| recorded and published | clause 14 of Schedule 1 speaks of one act of recording and publishing |
| lapsing or ceasing of effect | the Act's own gloss on expiry in the definition of repeal |
| by or on behalf of | the Act's pair for one relationship of agency |
| fees or charges | the Act's pair, taken from section 270 of the Land Transport Act 1998 |
| secondary legislation or instrument | section 5(1)'s own pair: an instrument that is secondary legislation, or one that is not |
| standard, framework, code of practice, recommended practice or requirement | the Act's own bundle noun for the material that section 64(1)(c) covers; no rule distinguishes one kind of the five |
| supplying or making information available | section 53's own pair for one act of providing information |
| when the repeal or amendment takes effect | section 32's own phrase for the one moment a repeal or amendment takes effect |
| remedy or relief | section 34(2)'s own pair: the Act speaks of any other remedy or relief as one thing |
| 1 or more | the Act's idiom for 'at least one', not a list |
| Acts or parts of Acts | section 96(2)(a)'s recurring pair: no rule in the Act treats an Act and part of an Act differently |
| Acts or parts revised | section 96(2)'s recurring pair for the legislation being revised |
| a clear, consistent, gender-neutral and modern style | section 96(2)(b)'s one aim, written as a list of its qualities |
| accessibility and readability | section 96(2)(c)'s one purpose: aiding use |
| by or under | the Act's pair for how secondary legislation can prescribe something |
| enacted or made | the Act's pair for how legislation comes into being (an Act is enacted, secondary legislation is made) |
| setting or determining | section 87's pair for one act of fixing a date or time |
| set or determined | section 87's pair for one act of fixing a date or time |
| inserting, replacing or removing | the three operations of one power in clause 13(4) of Schedule 1: the Act draws no line between them |

**Extended: the phrase is a member and so is each thing it names** (SPLIT rows; the constituents are in `lists-decisions.tsv`):

| Module | Type | Printed phrase | Constituents |
| --- | --- | --- | --- |
| nz-part2-commencement-repeal | Kind of change to legislation | an implied repeal or amendment | 2 |
| nz-part2-commencement-repeal | Kind of change to legislation | a change that removes or limits the effect of the legislation | 2 |
| nz-part2-commencement-repeal | Kind of change to legislation | a change that disapplies the legislation to a person, subject matter or circumstance | 3 |
| nz-part2-commencement-repeal | Effect of a repeal or amendment | affects the validity, invalidity, effect or consequences of anything done or suffered | 4 |
| nz-part2-commencement-repeal | Effect of a repeal or amendment | affects an existing right, interest, title, immunity, duty, status or capacity | 7 |
| nz-part2-commencement-repeal | Effect of a repeal or amendment | affects the previous operation of the legislation or anything done or suffered under it | 2 |
| nz-part2-commencement-repeal | Effect of a repeal or amendment | revives a thing that is not in force or existing when the repeal or amendment takes effect | 2 |
| nz-part2-commencement-repeal | Purpose for which repealed legislation continues | commencing or completing a proceeding for the offence or breach | 2 |
| nz-part2-commencement-repeal | Purpose for which repealed legislation continues | imposing a penalty, or any other remedy or relief, or making or giving an order or a direction, for the offence or breach | 6 |
| nz-part2-definitions | Candidate for the term Act | an Act of the Parliament of New Zealand or of the General Assembly | 2 |
| nz-part2-definitions | Candidate for the term enactment | the whole or a part of an Act or any secondary legislation | 3 |
| nz-part2-definitions | Candidate for the term department | the department, departmental agency, or interdepartmental venture named in Part 1, 2 or 4 of Schedule 2 of the Public Service Act 2020 | 3 |
| nz-part2-definitions | Candidate for the term Minister | the Minister of the Crown who, under the authority of a warrant or with the authority of the Prime Minister, is responsible for the administration of the legislation | 2 |
| nz-part2-definitions | Words denoting | a corporation sole, a body corporate or an unincorporated body | 3 |
| nz-part2-powers | Kind of act done before commencement | making secondary legislation or another instrument | 2 |
| nz-part2-powers | Kind of act done before commencement | serving a notice or document | 2 |
| nz-part2-powers | Kind of act done before commencement | conferring or imposing a legal position on a person | 2 |
| nz-part2-powers | Related power of an appointer | remove or suspend a person from the office | 2 |
| nz-part2-powers | Related power of an appointer | reappoint or reinstate a person to the office | 2 |
| nz-part2-powers | Related power of an appointer | appoint another person in place of a person who is absent temporarily or permanently | 2 |
| nz-part2-powers | Related power of an appointer | appoint another person in place of a person who has been removed or suspended from the office | 2 |
| nz-part2-powers | Who exercises an office holder's power | a person for the time being lawfully holding, or performing the duties of, the office | 2 |
| nz-part2-powers | Power, duty or function | a duty or function imposed by legislation | 2 |
| nz-part2-powers | Part of power B | identify the information to be supplied or made available | 2 |
| nz-part2-powers | Part of power B | approve or prescribe a method, format or medium for supplying or making information available | 3 |
| nz-part2-powers | Part of power B | authorise a prescribed person to approve or prescribe a form or a method, format or medium | 4 |
| nz-part2-principles | Kind of indication | the organisation and format of the legislation | 2 |
| nz-part2-revision-incorporation | Kind of material | a standard, framework, code of practice, recommended practice or requirement of an international organisation or a national organisation | 2 |
| nz-part2-revision-incorporation | Kind of material | a standard, framework, code of practice, recommended practice or requirement prescribed in any country or jurisdiction, or by any group of countries | 3 |
| nz-part2-revision-incorporation | Other source of authority to incorporate | the ability of legislation to refer to or incorporate other legislation | 2 |
| nz-part2-revision-incorporation | Way material is amended | it is amended or replaced | 2 |
| nz-part2-revision-incorporation | Way material is amended | it expires or is revoked | 2 |
| nz-part3-editorial-revision | Kind of editorial change | a reference to a replaced body, office, person, place or thing changed to the replacement | 5 |
| nz-part3-editorial-revision | Kind of editorial change | numbering, renumbering and consequential amendments authorised by an Order in Council under section 88 | 3 |
| nz-part3-editorial-revision | Kind of editorial change | punctuation changed, omitted or inserted | 3 |
| nz-part3-editorial-revision | Kind of editorial change | conjunctives and disjunctives inserted, omitted or changed | 2 |
| nz-part3-editorial-revision | Kind of editorial change | the way numbers, dates, times, quantities, measurements and similar matters are expressed changed | 6 |
| nz-part3-editorial-revision | Kind of editorial change | the way similar matters, ideas or concepts are expressed changed | 3 |
| nz-part3-editorial-revision | Kind of editorial change | an obvious typographical or clerical error corrected | 2 |
| nz-part3-editorial-revision | Kind of editorial change | an obvious grammatical or spelling error, or error of punctuation, corrected | 3 |
| nz-part3-editorial-revision | Kind of editorial change | an obvious error in numbering, cross-referencing or alphabetical ordering corrected | 3 |
| nz-part3-editorial-revision | Kind of editorial change | an obvious error in or arising out of an amendment, by other legislation, to the legislation being changed corrected | 2 |
| nz-part3-editorial-revision | Kind of editorial change | a method of setting or determining a date or time replaced with the exact date or time once set or determined | 2 |
| nz-part3-editorial-revision | Kind of editorial change | a transitional, savings, validation or similar provision in amending legislation incorporated in the legislation it amends | 3 |
| nz-part3-editorial-revision | Kind of editorial change | changes made to show the effect of an amendment or repeal, or purely consequential on an amendment made by other legislation | 3 |
| nz-part3-editorial-revision | Kind of editorial change | the Title of secondary legislation changed to better identify it or distinguish it from other legislation | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | revising the whole or part of 1 or more Acts, combining or dividing Acts or parts of Acts | 3 |
| nz-part3-editorial-revision | Change in a revision Bill | omitting redundant and spent provisions | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | renumbering and rearranging provisions | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | changes in language, format and punctuation for a clear, consistent, gender-neutral and modern style | 3 |
| nz-part3-editorial-revision | Change in a revision Bill | including new purpose, outline or overview provisions, examples, diagrams, graphics, flowcharts, readers' notes, lists of defined terms and similar devices | 10 |
| nz-part3-editorial-revision | Change in a revision Bill | correcting typographical, punctuation and grammatical errors and similar errors | 4 |
| nz-part3-editorial-revision | Change in a revision Bill | making consequential amendments to legislation not incorporated, or incorporated only in part, in the revision | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | including necessary repeals, transitional, savings and related provisions | 4 |
| nz-part3-editorial-revision | Change in a revision Bill | making minor amendments to clarify Parliament's intent, resolve ambiguity or reconcile inconsistencies | 3 |
| nz-part3-editorial-revision | Change in a revision Bill | updating a monetary amount having regard to movements in the Consumers Price Index, or providing for it to be prescribed by Order in Council | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | making minor amendments to update how provisions can be complied with, or operate, to take account of changes in technology | 2 |
| nz-part3-editorial-revision | Change in a revision Bill | omitting forms, schedules or other matters of detail and authorising them to be prescribed by or under secondary legislation | 3 |
| nz-part3-editorial-revision | Change in a revision Bill | any other change necessary for implementing, or consequential on, the two changes above | 2 |
| nz-part3-editorial-revision | Matter the PCO's annual report may address | a recommendation for the repeal of obsolete or redundant legislation or provisions, if their repeal is not suitable for inclusion in a revision | 2 |
| nz-part3-publication | Thing to be drafted | Government Bills and amendments to them | 2 |
| nz-part3-publication | Thing to be drafted | local Bills and private Bills and amendments to them (to advise on or assist with) | 4 |
| nz-part3-publication | Thing to be drafted | an amendment to a local Bill or a private Bill | 2 |
| nz-part3-publication | Thing to be drafted | Members' Bills and amendments to them | 2 |
| nz-part3-publication | Kind of body | a department named in Part 1 of Schedule 2 of the Public Service Act 2020, including a departmental agency named in Part 2 of that schedule that is part of that department | 2 |
| nz-part3-publication | Kind of official version | an official version that is a consolidation and includes changes made under subpart 2 | 2 |
| nz-part3-publication | What an official version is taken to prove | It is taken to correctly state, as at its stated date, the law enacted or made by the legislation consolidated and by the amendments (paragraph (b)) and by the changes made (paragraph (c)(i)), and is evidence that those changes are authorised by subpart 2 | 2 |
| nz-part3-publication | Item inserted by the PCO | machine-readable text, links or other metadata inserted as an aid to users of electronic versions | 3 |
| nz-part3-publication | Item inserted by the PCO | information recorded and published under clause 14 of Schedule 1, or as an aid to understand how this Act applies to secondary legislation | 2 |
| nz-part5-oversight | Kind of charge | a duty, levy or road user charge | 3 |
| nz-part6-7-pco-regulations | Kind of client of the PCO | a promoter of a local or private Bill | 2 |
| nz-schedules | Change to a version of legislation under clause 13(4) | inserting, replacing or removing a statement relating to listing, notification, publication or presentation | 4 |
| nz-schedules | Thing that continues | any direction made under section 76 (or previously under section 36E or 36F of the Legislation Act 2012) | 3 |
| nz-schedules | Exemption ground shown in the deposited text | The relevant chief executive considers that compliance would result in disclosure of commercially sensitive information, disclosure of a trade secret, prejudice to New Zealand's position in negotiations for overseas market access, or prejudice to the international relations of New Zealand | 4 |
| nz-schedules | Exemption ground shown in the deposited text | The relevant chief executive considers that compliance would result in prejudice to New Zealand's position in current or future negotiations for overseas market access | 2 |

**Left whole, with the reason** (WHOLE rows):

| Module | Type | Printed phrase | Why it stays whole |
| --- | --- | --- | --- |
| nz-glossary | How a term is defined | Means and includes | the name of a form of definition (closed on one side, open on the other), not a list of things; the entry's `how` field is what nz-tests-glossary.l4 asserts |
| nz-interpretation-time | How a period is introduced | starting or beginning on the day named | section 54 item 1 pairs the two words under one rule and its examples do not tell them apart; they are one item (fork F2 reads them together) |
| nz-interpretation-time | How a period is introduced | from or after the day or the event named | section 54 item 2 pairs 'from' and 'after' under one rule; the next-day reading (fork F2) applies to both, so a member for each would carry the same answer and no separate rule |
| nz-part2-commencement-repeal | Extent of a commencement | The provision comes into force only for the stated purpose, and only the identified parts come into force | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part2-commencement-repeal | What a reference to new legislation is a reference to | The whole or the corresponding part of the existing legislation | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part2-commencement-repeal | What happens on repeal to a reference to the repealed legislation | The reference is a reference to the legislation that replaces, or corresponds to, the legislation repealed | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part2-definitions | Territory | another island or territory within the Realm of New Zealand | a catch-all that names what is off the list (another / any other), so it has no members of its own |
| nz-part2-definitions | Form and medium of words | written or typed on paper | a label of this encoding's own for a way words get onto paper; the Act's test is visibility and tangibility, which the two ways meet alike |
| nz-part2-definitions | Form and medium of words | spoken only, or otherwise not visible | a label of this encoding's own for the words that fail the Act's test (not visible); every way of being not visible gives the same answer |
| nz-part2-definitions | Candidate for the term Gazette | another gazette or journal | a catch-all that names what is off the list (another / any other), so it has no members of its own |
| nz-part2-definitions | Candidate for the term Governor-General in Council | the Governor-General acting on the advice and with the consent of the Executive Council | one description with two required elements (advice AND consent), not alternatives; an Act of the Executive Council needs both |
| nz-part2-definitions | Words denoting | a natural person by referring to a gender or to persons generally | section 16(2) describes one class and gives three examples in a parenthesis (he or she, someone, people); they are not alternatives a case could choose between |
| nz-part2-powers | Kind of act done before commencement | doing another act or thing for the purposes of the legislation | a catch-all that names what is off the list (another / any other), so it has no members of its own |
| nz-part2-powers | Kind of act done before commencement | doing an act or thing that is not for the purposes of the legislation | a catch-all that names what is off the list (another / any other), so it has no members of its own |
| nz-part3-editorial-revision | Kind of editorial change | an obvious error in an amendment, by other legislation, to the legislation being changed corrected | the commas set off a parenthesis, not a list |
| nz-part3-editorial-revision | Kind of editorial change | an obvious error arising out of an amendment, by other legislation, to the legislation being changed corrected | the commas set off a parenthesis, not a list |
| nz-part3-editorial-revision | Change in a revision Bill | making minor amendments to update how provisions can be complied with, to take account of changes in technology | the commas set off the technology purpose of one limb (the 'or operate' limb is its own member); no list remains |
| nz-part3-editorial-revision | Change in a revision Bill | making minor amendments to update how provisions operate, to take account of changes in technology | the commas set off the technology purpose of one limb (the 'can be complied with' limb is its own member); no list remains |
| nz-part3-editorial-revision | Change in a revision Bill | omitting forms and authorising them to be prescribed by or under secondary legislation | 'omitting X and authorising X to be prescribed' is one change in two steps (omit, then authorise); the second step is not an alternative |
| nz-part3-editorial-revision | Change in a revision Bill | omitting schedules and authorising them to be prescribed by or under secondary legislation | 'omitting X and authorising X to be prescribed' is one change in two steps (omit, then authorise); the second step is not an alternative |
| nz-part3-editorial-revision | Change in a revision Bill | omitting other matters of detail and authorising them to be prescribed by or under secondary legislation | 'omitting X and authorising X to be prescribed' is one change in two steps (omit, then authorise); the second step is not an alternative |
| nz-part3-editorial-revision | Matter the PCO's annual report may address | a recommendation for the repeal of obsolete legislation or provisions, if their repeal is not suitable for inclusion in a revision | the commas set off a parenthesis, not a list (the condition 'if their repeal is not suitable for inclusion in a revision' follows it) |
| nz-part3-editorial-revision | Matter the PCO's annual report may address | a recommendation for the repeal of redundant legislation or provisions, if their repeal is not suitable for inclusion in a revision | the commas set off a parenthesis, not a list (the condition 'if their repeal is not suitable for inclusion in a revision' follows it) |
| nz-part3-publication | Additional requirement on a maker | include its details in, or with, it as published on the maker's website | one requirement or one description whose 'or' / 'and' are routes to or parts of the same thing, not alternatives a case could choose between |
| nz-part3-publication | Additional requirement on a maker | make it and its details, as far as practicable, able to be accessed at, or downloaded from, the maker's website | one requirement or one description whose 'or' / 'and' are routes to or parts of the same thing, not alternatives a case could choose between |
| nz-part3-publication | Additional requirement on a maker | forward links to it to the PCO for publication without delay and in accordance with any applicable directions under section 76 | one requirement or one description whose 'or' / 'and' are routes to or parts of the same thing, not alternatives a case could choose between |
| nz-part3-publication | Kind of body | a decision-making person or body in or related to, or acting through or for, any of the above | a relationship to any body already listed ('in or related to, or acting through or for'): five relationships times the listed bodies would be a product, not a list; the phrase is answered as a whole and the bodies it refers to are each members |
| nz-part3-publication | Source of obligations | that provision as incorporated into the Comprehensive and Progressive Agreement for Trans-Pacific Partnership by Article 1.1 of that agreement | one requirement or one description whose 'or' / 'and' are routes to or parts of the same thing, not alternatives a case could choose between |
| nz-part3-publication | What an official version is taken to prove | It is taken to correctly state, as at its stated date, the law enacted or made by the legislation consolidated and by the amendments | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part3-publication | What an official version is taken to prove | It is taken to correctly state, as at its stated date, the law enacted or made by the legislation and by the changes made, and is evidence that those changes are authorised by subpart 2 | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part3-publication | Item inserted by the PCO | another note or information | a catch-all that names what is off the list (another / any other), so it has no members of its own |
| nz-part5-oversight | Whether earlier legislation is revived | Revived as it was immediately before it was amended, repealed or revoked: section 118 or 125 alters section 32 | a result type: the constructor states what the Act says happens, it is not a case someone is asked about, and the list inside it is the Act's own sentence |
| nz-part6-7-pco-regulations | Kind of communication | a communication between a client and a counsel in the PCO relating to the subject matter of the instructions | the 'and' joins the two parties to one communication; it is not a list of alternatives |

**Definitions of sections 5(1) and 13 that list things.** LOOKUP: a function that takes a candidate and says whether the definition covers it (closed: off the list is JUST FALSE; open: off the list is NOTHING). WHOLE: left as the glossary entry only.

| Provision | Term | Decision | Function, or why it stays whole |
| --- | --- | --- | --- |
| section 5(1) | administering agency | LOOKUP | closed: is the administering agency |
| section 5(1) | empowering legislation | LOOKUP | closed: is empowering legislation |
| section 5(1) | empowering provision | LOOKUP | closed: is the empowering provision |
| section 5(1) | instrument | LOOKUP | open: is an instrument |
| section 5(1) | introduction | WHOLE | one description: the introduction of the Bill 'in accordance with the rules and practice' of the House; 'rules and practice' is one standard, and the term has no list of things it covers |
| section 5(1) | legislation | LOOKUP | closed: is legislation |
| section 5(1) | legislation website | WHOLE | one description: an Internet site maintained by, or on behalf of, the PCO; 'by, or on behalf of' and '(or both)' are routes to the same status, and the one test is whether the site is maintained for the PCO for publishing legislation or supporting material |
| section 5(1) | maker | WHOLE | one description: the person empowered to make the secondary legislation or instrument; 'secondary legislation or instrument' is section 5(1)'s own pair, and the lookup `who is the maker of the secondary legislation or instrument` answers it by kind |
| section 5(1) | minimum legislative information | LOOKUP | closed: is minimum legislative information |
| section 5(1) | release | WHOLE | one description: 'circulation or release' is the Act's pair for one act of making an amendment to a Bill available to the House |
| section 5(1) | secondary legislation | LOOKUP | closed: is secondary legislation |
| section 13 | Act | LOOKUP | closed: counts as an Act under section 13 |
| section 13 | Commonwealth country and part of the Commonwealth | LOOKUP | open: counts as a Commonwealth country or part of the Commonwealth under section 13 |
| section 13 | department | LOOKUP | closed: counts as the department or Ministry under section 13 |
| section 13 | enactment | LOOKUP | closed: counts as an enactment under section 13 |
| section 13 | Gazette | LOOKUP | closed: counts as the Gazette under section 13 |
| section 13 | Governor-General in Council | LOOKUP | closed: counts as the Governor-General in Council under section 13 |
| section 13 | Minister | LOOKUP | closed: counts as the Minister under section 13 |
| section 13 | Ministry | LOOKUP | closed: counts as the department or Ministry under section 13 |
| section 13 | New Zealand | LOOKUP | closed: is within New Zealand as a territorial description |
| section 13 | North Island | LOOKUP | open: which island the place is, under the Act's definitions |
| section 13 | office | LOOKUP | open: counts as an office under section 13 |
| section 13 | person | LOOKUP | open: counts as a person under section 13 |
| section 13 | prescribed | LOOKUP | closed: counts as prescribed under section 13 |
| section 13 | proceeding | LOOKUP | closed: is a proceeding |
| section 13 | Proclamation | LOOKUP | closed: is a Proclamation |
| section 13 | public notification | LOOKUP | closed: is public notification |
| section 13 | repeal | LOOKUP | open: counts as repeal under section 13 |
| section 13 | rules of court | WHOLE | one description: rules regulating the practice and procedure of the court; 'practice and procedure' is the Act's pair for the subject of the rules, and the term has no list of things it covers |
| section 13 | South Island | LOOKUP | open: which island the place is, under the Act's definitions |
| section 13 | working day | LOOKUP | closed: is a working day |
| section 13 | writing | LOOKUP | closed: is writing |

## Changes to existing modules

Every pre-existing assertion whose expected value changed in this pass, and why. Each is a consequence of a ruling (A: a closed list answers JUST FALSE off the list; B: fork F11; C: lists), not of a correction to the text. No other pre-existing assertion changed: comparing the `#ASSERT` lines of each test module with the copy kept from the first pass (1,720 assertions), exactly 51 of those lines are absent from the modules now, and the 51 are the ones listed here (nz-cases-seat.l4 4, nz-tests-glossary.l4 16, nz-tests-part2-commencement-repeal.l4 1, nz-tests-part2-definitions.l4 7, nz-tests-part2-powers.l4 2, nz-tests-part2-revision-incorporation.l4 2, nz-tests-part3-editorial-revision.l4 8, nz-tests-part3-publication.l4 6, nz-tests-part6-7-pco-regulations.l4 3, nz-tests-schedules.l4 2; none in nz-tests-part1.l4, nz-tests-part2-principles.l4, nz-tests-part5-oversight.l4 or nz-tests-time.l4). The other 548 lines in the modules now are new, and 1,720 less 51 plus 548 is the 2,217 that check.sh counts.

- **nz-tests-part3-publication.l4:** s 69(1) `secondary legislation not drafted by the PCO`: NOTHING to JUST FALSE (B). s 72(1)(a), two cases (published but not practicable; not published but practicable): NOTHING to JUST FALSE (B). s 77 `any other body` and `another obligation`: NOTHING to JUST FALSE (A). s 79(1), a version that is a consolidation and includes subpart 2 changes: its expected value is now the new member that carries both statements (A3).
- **nz-tests-part3-editorial-revision.l4:** s 87, the six kinds that attach a condition, with the condition false: NOTHING to JUST FALSE; `another change`: NOTHING to JUST FALSE (B). s 95(2) `anything else`: NOTHING to JUST FALSE (B).
- **nz-tests-part2-powers.l4:** s 43 `doing an act or thing that is not for the purposes of the legislation`: NOTHING to JUST FALSE. s 47 `someone else` for an office holder who is not a Minister: NOTHING to JUST FALSE; the Minister case is a new assertion that stays NOTHING (B).
- **nz-tests-part2-revision-incorporation.l4:** s 64(1)(c), technical material that is neither impracticable nor too large; `something else` with both conditions TRUE: NOTHING to JUST FALSE (B).
- **nz-tests-part2-commencement-repeal.l4:** s 34(2) `another purpose`: NOTHING to JUST FALSE (B).
- **nz-tests-part2-definitions.l4:** `is writing` now takes whether the thing represents words and a `Form and medium of words`, and returns a `MAYBE BOOLEAN`: its four assertions are replaced by seven, and the case "visible but not tangible", which was FALSE, is now "shown only on a screen", which is NOTHING (C). `a requirement to put something in writing is met` takes that `MAYBE BOOLEAN` and returns one: its three assertions are restated with the same answers, and two NOTHING cases are added.
- **nz-tests-part6-7-pco-regulations.l4:** s 131(1), two cases (not a confidential communication; not between a client and counsel): NOTHING to JUST FALSE; the House-rules case stays NOTHING. s 133(5) `anyone else`: NOTHING to JUST FALSE (B).
- **nz-tests-schedules.l4:** Schedule 1 cl 13(4) `another change` and cl 15(6) `anything else`: NOTHING to JUST FALSE (B).
- **nz-cases-seat.l4:** `May the old law still be used to deal with my offence`, input `another purpose`: NOTHING to JUST FALSE (s 34(2)). `Am I entitled to read the legislation free of charge on the legislation website`, with access practicable FALSE: NOTHING to JUST FALSE (s 72(1)(a)). The question about writing takes the form and medium of the words and returns a `MAYBE BOOLEAN`: its two cases are replaced by five (C).
- **nz-tests-glossary.l4:** the field `where this encoding decides it` of fifteen entries changed from "glossary only: the Act gives the words and no rule beyond them" (or, for minimum legislative information, from a pointer to nz-part3-publication.l4) to the look-up that now decides it: Act, enactment, Gazette, Commonwealth country and part of the Commonwealth, office, Governor-General in Council, prescribed, department, Ministry, Minister (section 13), and administering agency, empowering legislation, empowering provision, minimum legislative information (section 5(1)), and regulations (Schedule 1 clause 2, now pointing at the rule for legislation enacted or made before the main commencement date; fork F23). The count is now 86 entries, with publication deadline (line 1048, folded into publication exemption before) an entry of its own.

- **2026-10-29, the rule replacing fork F11's second limb (see "Replaced 2026-10-29" above):** twelve assertions restated from `JUST FALSE` to `NOTHING`, each with a `-- RECONCILED 2026-10-29` comment quoting the original. nz-tests-part2-powers.l4 (s 47 `someone else`); nz-tests-part2-revision-incorporation.l4 (s 64 `something else`, three cases); nz-tests-part3-editorial-revision.l4 (s 87 `another change`; s 95(2) `anything else`); nz-tests-part6-7-pco-regulations.l4 (s 133(5)); nz-tests-schedules.l4 (Schedule 1 clause 13(4)); `tests-independent.l4` (four, below). Layer 1 changed in five modules: nz-part2-powers.l4, nz-part2-revision-incorporation.l4, nz-part3-editorial-revision.l4 (two functions), nz-part6-7-pco-regulations.l4 and nz-schedules.l4, one `JUST FALSE` branch each changed to `NOTHING` and its comment rewritten. `check.sh` after the change: 30 modules, 3,424 satisfied, 0 failed, 0 refused, every module `same` on 1.6.102.

## What the stable binary does not accept

These are the ways the stable build `l4 1.6.98` (main) refused or misread what I wrote in this run, each reproduced on a small file before it was written down here. "Loud" means it reported an error; "silent" means it accepted the text and the exit status is 0.

Loud (exit status 1, an error diagnostic):

- `length` is not defined ("I could not find a definition for the identifier"): count a list with `sum (map (GIVEN e YIELD 1) xs)`.
- `YMD` is not defined on `1.6.98` or on `1.6.102` (measured at the start of this run), and this encoding defines no shim for it: every module writes dates as `Date day month year`. During the run a one-line shim named `YearMonthDay` was defined in `nz-interpretation-time.l4` (renamed from `YMD` on 2026-10-29); after the second pass the lead removed it and rewrote every use as `Date`.
- A `GIVEN x YIELD ...` lambda split over two lines does not parse ("unexpected ("): write each lambda on one line.
- In a mixfix function the `GIVEN` parameters must come in the order the head names them, or the declaration is rejected ("The names in a type signature must match those in the definition"). This cost the most time.
- A mixfix function of one argument cannot end in a keyword: `` `double` x `times` MEANS ... `` fails with "I could not find a definition for the identifier `times`".
- One ill-typed `#ASSERT` (for example a `MAYBE BOOLEAN` compared with `TRUE`) makes the whole file report an error and evaluate none of its assertions: no `assertion` line is printed for any of them, so a tally of "satisfied" reads zero for the file. `check.sh` shows the error.

Silent (exit status 0):

- A failed `#ASSERT` still exits 0 on `1.6.98` (an `l4` built before legalese/l4-ide#518 does this; `check.sh`'s own header says so): read the diagnostics, not the exit code.
- `AND` and `OR` at one indent give a Warning only. `check.sh` counts errors and assertion lines, so it does not see it; I scanned the output of every module for `DiagnosticSeverity_Warning` separately, and parenthesised every such mix.
- `NOT a AND b` parses as `NOT (a AND b)`: `` `neg` TRUE FALSE `` for `NOT a AND b` returned `TRUE`. Every `NOT` is parenthesised.

Avoided as the brief says (not tested against the binary): `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section `GIVEN`, sets, `TYPICALLY`, `@lang`, hierarchy, ledger.

## What `check.sh` prints

Run as `env -u JL4_LIBRARY_PATH L4=<l4 1.6.98> L4_MAIN=<l4 1.6.102> ./check.sh`, so `JL4_LIBRARY_PATH` is unset. There was no earlier run of `check.sh` on this encoding: the baseline it replaced is none (this is a fresh encoding). Its output, unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.102 (main, e4f2553, 2026-10-26)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
nz-cases-seat.l4                               0       148       0        0         0 |      0       148       0        0  same
nz-glossary.l4                                 0         0       0        0         0 |      0         0       0        0  same
nz-interpretation-time.l4                      0         0       0        0         0 |      0         0       0        0  same
nz-nouns.l4                                    0         0       0        0         0 |      0         0       0        0  same
nz-part1-preliminary.l4                        0         0       0        0         0 |      0         0       0        0  same
nz-part2-commencement-repeal.l4                0         0       0        0         0 |      0         0       0        0  same
nz-part2-definitions.l4                        0         0       0        0         0 |      0         0       0        0  same
nz-part2-powers.l4                             0         0       0        0         0 |      0         0       0        0  same
nz-part2-principles.l4                         0         0       0        0         0 |      0         0       0        0  same
nz-part2-revision-incorporation.l4             0         0       0        0         0 |      0         0       0        0  same
nz-part3-editorial-revision.l4                 0         0       0        0         0 |      0         0       0        0  same
nz-part3-publication.l4                        0         0       0        0         0 |      0         0       0        0  same
nz-part5-oversight.l4                          0         0       0        0         0 |      0         0       0        0  same
nz-part6-7-pco-regulations.l4                  0         0       0        0         0 |      0         0       0        0  same
nz-schedules.l4                                0         0       0        0         0 |      0         0       0        0  same
nz-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
nz-tests-glossary.l4                           0       357       0        0         0 |      0       357       0        0  same
nz-tests-part1.l4                              0        47       0        0         0 |      0        47       0        0  same
nz-tests-part2-commencement-repeal.l4          0       126       0        0         0 |      0       126       0        0  same
nz-tests-part2-definitions.l4                  0       177       0        0         0 |      0       177       0        0  same
nz-tests-part2-powers.l4                       0       124       0        0         0 |      0       124       0        0  same
nz-tests-part2-principles.l4                   0        40       0        0         0 |      0        40       0        0  same
nz-tests-part2-revision-incorporation.l4       0        64       0        0         0 |      0        64       0        0  same
nz-tests-part3-editorial-revision.l4           0       315       0        0         0 |      0       315       0        0  same
nz-tests-part3-publication.l4                  0       202       0        0         0 |      0       202       0        0  same
nz-tests-part5-oversight.l4                    0       109       0        0         0 |      0       109       0        0  same
nz-tests-part6-7-pco-regulations.l4            0        56       0        0         0 |      0        56       0        0  same
nz-tests-schedules.l4                          0       287       0        0         0 |      0       287       0        0  same
nz-tests-time.l4                               0       165       0        0         0 |      0       165       0        0  same
TOTAL (29 modules)                             0      2217       0        0           |      0      2217       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
check.sh exit=0
```

Every module is clean on both builds. Besides what `check.sh` counts, I scanned the output of every module on both builds for `DiagnosticSeverity_Warning` and `DiagnosticSeverity_Error`: none on `1.6.98`, none on `1.6.102`.

Other checks run:

- `python3 -I srcrefs.py check --refs <text> nz-*.l4`: 0 problems (every `-- src:N` quotation and every `@ref ... (src:N)` locator agrees with the text). With `--strict`: 0 problems as well (each block's `@ref`s reach exactly the lowest and the highest raw line its quotations quote). Before this pass, `--strict` reported 138.
- `python3 -I coverage.py`: every one of the 1,430 non-blank lines is in exactly one row, and every row has a disposition.
- `python3 -I sweep_lists.py`: 0 problems (section "Lists" above).
- The glossary is generated from the text and tested against `glossary-expected.tsv`, typed by hand from reading the definition lines. The first run of the generator failed three assertions against the hand-typed rows (how a term is keyed when a definition names several terms, and how the provision named on a definition's opening line is read, for example "section 115(a) to (d)"); the generator was wrong in each case and was fixed, and the tests were not changed.
- A negative control on the tests: `mutate_tests.py` changes the expected value of an assertion (TRUE and FALSE swapped; JUST TRUE and JUST FALSE swapped; a number plus 1; the day of a `YearMonthDay` plus 1; an exclamation mark added to a string; a constructor swapped for another constructor expected of the same field or function; NOTHING replaced by a JUST of a type that fits, tried in turn as a Boolean, a date, a string, a number and a moment; a bare Boolean assertion negated), puts all the mutations of one test module into one scratch copy, runs it, and requires each mutated line to be reported as exactly one failed assertion and nothing else to fail or error. Result on the whole suite (2,217 assertions in the 14 test modules, `l4 1.6.98`, one run of the shipped tool): **2,206 mutated, of which 2,201 were detected exactly once and 0 were missed**; 5 stayed ill-typed when mutated (an expected NOTHING whose type none of the replacements fits: nz-tests-part2-commencement-repeal.l4 lines 228, 229 and 231, and nz-cases-seat.l4 lines 245 and 247, so those five have no negative control); and 11 were not mutated because the tool has no mutation for their expected value (a JUST of a constructor with no other to swap in, 3; a JUST of a number, 4; a LIST, 2; EMPTY, 1; a date written `Date d m y`, 1: nz-tests-part2-commencement-repeal.l4 lines 225 and 227, nz-cases-seat.l4 line 243, nz-tests-time.l4 lines 276, 277, 281 and 283, nz-tests-part2-definitions.l4 line 228, nz-tests-part2-powers.l4 lines 38 and 39, nz-tests-part5-oversight.l4 line 251). So 16 of the 2,217 assertions have no negative control. The 548 assertions that were added or changed after the first full pass (the lines that are not in that pass's copy of the module, selected with `--base`) were run on their own: all 548 were mutated and each was detected exactly once, with none skipped and none ill-typed. The tool must not run while `check.sh` does, because its scratch copies are `.l4` files in the same directory; these results were obtained in a copy of the directory. That run was made while dates were still written with the local shim `YearMonthDay y m d`, and the tool's date mutation ("the day of a `YearMonthDay` plus 1") is on that spelling; the lead has since rewritten every date as `Date d m y`, and the tool, which is not shipped, has not been run since.
- Two expectations of mine were wrong the first time and were corrected from the text, not from the output: the earliest day for the second event of s 54 Item 7 (I typed 17 February 2026; counting ten working days from the text gives 18 February, and the encoding already said so), and the word look-ups in the seat cases (I had used constructor names that do not exist).

## What would need doing before anyone relies on it

- **A domain expert must read it against the official text.** Nobody has. The deposited text is a converter rendering, not the official text; it dropped the subsection numbers, the paragraph labels and the cells of three tables (s 54, Schedule 3 and Schedule 4). Fetch a text that keeps them, then re-run `expand.py`, `coverage.py` and `check.sh`, and redo findings 1, 14 and 15.
- **Decide forks F1 to F23 with a lawyer.** F2 (the day after), F4 (s 55 reaches months), F5, F6 and F13 (the Act is silent on years, weeks and days after), F8 to F10 and F17 and F21 (the day itself), and above all **F11** (what an answer of FALSE means when a case fails a section's own condition), move answers. F11 is a working instruction, not a ruling.
- **Supply the calendars.** The seven named days of s 13 have no dates in the Act. The House's sitting days (s 117) and the New Zealand offset from UTC (s 57) are inputs for the same reason. Nothing here supplies them.
- **The Acts the text points to are not among the sources.** Each borrowed fact is an input. If a later row encodes the Interpretation Act 1999, the Time Act 1974, the Public Finance Act 1989 or the Contract and Commercial Law Act 2017, those inputs can be filled from it.
- **The negative control above covers the assertions this pass added or changed, not the whole suite.** The assertions of the first pass were mutated in the first pass only for boolean, number and date expectations.
- **Not done:** no run on the `unstable` compiler, no `l4 deploy` or `jl4-service` check of the `@export`ed questions, and no review of the wording of the seat questions by a person who is not the encoder.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage-spec.tsv`, `coverage.py`, `expand.py`, `gen_coverage_spec.py`, `gen_glossary.py`, `gen_notes.py`, `gen_seat.py`, `glossary-expected.tsv`, `lists-decisions.tsv`, `mutate_tests.py`, `src`, `sweep_lists.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 458 numbered scenarios over the Act (sections A to L) and expectations for the 43 seat questions (section M).
It then wrote `tests-independent.l4`: 1,207 assertions (98 glossary checks, 149 for the seat questions, and 14 in section N, which come from 8 further scenarios it wrote after reading the encoder's enumerations), and ran it against the first version of this encoding with the stable binary.
`ANSWERS.md` is not kept in this folder; the scenario numbers in the `-- S<n>` comments of `tests-independent.l4` refer to it, and the seat questions are numbered `ST<n>`.
The encoder answered a fix list written from the test author's report, and changed the encoding without reading the assertions (see the independence caveat below).

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the first version | 1,207 | 1,188 | 19 | 0 |
| after the second pass and the reconciliation below | 1,207 | 1,207 | 0 | 0 |

The 60 scenarios the encoding has no function for are the 25 `-- GAP` lines at the end of the test file, each in the test author's words; the lead added them from the author's report, and the count of 60 is checked against it.

**What the 19 first-run failures turned out to be.**

- **Four were encoder defects, repaired; the author's assertions stand unchanged (885, 891, 1655, 1909).**
  Two closed "means" definitions in s 77 (`relevant central government entity`, `international transparency obligations`) answered `NOTHING` for a case that is not on the list, where the text gives a closed list.
  "Publication deadline" was folded into the text of the "publication exemption" glossary entry and could not be looked up; it is now its own entry, so the glossary has 86 entries.
  The case in which an official version is both a consolidation and includes subpart 2 changes (s 79(1)(b) with (c)(i)) returned the changes-only wording; the result type now has a member that carries both.
- **Six were cases in which the encoder's second pass adopted a convention, fork F11, and the author's original assertion now holds (548, 738, 739, 803, 970, 1855).**
  The convention is "assumed, not ruled": a function scoped to a section's own grant, duty or permission answers `JUST FALSE` ("this section does not give it") for a case outside the section's own condition or closed list, and answers `NOTHING` ("the Act does not say") where the Act extends a power that has terms of its own or preserves other authority.
  The author's own verdict on 548 and 1855 was "my scenario is wrong"; it listed 738, 739 and 970 as forks leaning towards the encoder being wrong, and 803 as a fork with no lean.
  1855 had been reconciled to `NOTHING` before the second pass and is restored to the author's original `JUST FALSE`.
- **Seven were reconciled to the encoding's answer, `NOTHING` (161, 169, 574, 605, 962, 1250, 1893).**
  161 and 169 ask what an "includes" list does not name (a plain amendment as a "repeal", a natural person as a "person"), which the text leaves open (fork F22); the author's verdict was fork, leaning to its own error for 161.
  574 and 605 are cases in which the Act extends a power that has terms of its own (the deputy of a Minister of the Crown in s 47, a power that only approves a form in s 53(2)(c)); 962 is s 86(1): the author leaned towards the encoder being wrong because a comment above the function overstated the text, the encoder's second pass corrected that comment, and subsection (3) preserves other authority.
  1250 and 1893 are the same s 146(2)(b) scenario (an act done in bad faith), where the author accepted that s 146 only bars proceedings and never says one may be brought.
- **Two were glossary counts (1507, 1657), reconciled to 86 and 1 under fork F23.**
  The author counted a second "regulations" entry for Schedule 1 clause 7; the encoding keeps one entry (clause 2) and carries clause 7 as a rule in `nz-schedules.l4`.
  F23 records the other reading, and the text does not choose between them.

**Assertions that changed without being among the 19.**

- **Six that passed on the first run were restated from `NOTHING` to `JUST FALSE` after F11 was adopted** (S172c, S195b, S310c, S320, ST20, ST34b).
  In each the author had written `NOTHING`, reading the Act as not answering the case, and the first-pass encoding agreed; the author's reading is alternative (a) of F11.
  These are the cases in which the author and the convention disagree, so they are the first thing for a lawyer to look at.
- **Four of those and one more changed again on 2026-10-29**, when the rule that `JUST FALSE` needs the text's own words replaced F11's second limb. S195b, S310c and S320 are restored to the author's original `NOTHING`, and the s 64 `something else` assertion (line 748), which the author had written as `JUST FALSE`, now reads `NOTHING` with a `-- RECONCILED 2026-10-29` comment quoting it. S172c and ST20 (s 34(2), "three purposes only") and ST34b (s 72(1)(a), marginal) stay `JUST FALSE`.
- **Seven were restated for a new signature** (S72, S72b, S72c, ST7, ST7b, ST7c, ST7d).
  The second pass changed `is writing` and its seat question to take the s 13 form and medium as a choice and to return a `MAYBE BOOLEAN`, so the author's three-boolean calls no longer type-check.
  Five keep the author's answer.
  Two (S72c and ST7b, words shown only on a screen) changed from "not writing" to `NOTHING`, which is the answer the author's own gap 73 gives ("not covered"); the encoder's comment on the function says the text does not say whether a screen is a tangible medium.

Each reconciled assertion is rewritten in place with a `-- RECONCILED` comment that quotes the author's original and gives the reason; none is deleted.
The ST34 comment is two: the first-pass reconciliation, and the second-pass comment that supersedes it.

**Lists.**
The author checked the members of the lists the encoding stores as lists, one by one, and found that wherever the Act prints several things in one item the encoding held one member and could not answer for its parts.
The encoder's second pass split 75 such constructors into the printed phrase plus each thing it names (and added 27 look-ups for the lists in the definitions of s 5(1) and s 13); 33 constructors and 5 definitions were left whole, each with a reason in "Lists: what was split and what was left whole" above.
The encoder's own test modules name every part added in the second pass (its list checker requires it); `tests-independent.l4` was written against the first version and was not extended for them, so it does not by itself check the new members.

**Independence caveat.**
No file of the lead's session was delivered into the test author's session, and a search of its tool calls and attachments finds no read outside its own folder.
The encoder was given the paths only of two triage files (this row's and the Israeli row's), and a search of its tool calls finds no read of the author's folder while it made the second-pass changes.
After it had finished both rounds, answering a follow-up question from the lead, it ran a search over the author's folder that returned a line of `ANSWERS.md` (scenario 308), the s 86(1) heading in `tests-independent.l4` with the first 300 characters of the lead's comment on it, and line 52 of the triage, and it then read that line of the triage; its tool calls after that search contain no write, and the only other thing it did was send its reply.
The encoder's session was also given the text of the lead's date-conversion script.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 30 modules, 3,424 satisfied, 0 failed, 0 refused, and every module `same` on the 1.6.102 build, run on 2026-10-29.
Dates in the author's file are written `Date day month year`, as in the encoding.
