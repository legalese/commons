# NOTES: Unfair Contract Terms Act 1977 (Singapore), 2020 Revised Edition, informal consolidation, whole encoding in L4 (main)

Status: draft. Not reviewed: no domain expert has read this encoding against the text.
Method: a single Sonnet 5.5 agent working alone from the brief (encoding name `legalese-sonnet-5.5`).
Target: the `main` compiler, build 1.6.109 (also read identically by 1.6.108; see "What check.sh prints").
Source: `UCTA1977.txt`, 697 lines, sha256 `852b81e63e5c9b564953395dbeb958faa24e6c960b15837132ad63558802bb80`.
**The source is a plain-text rendering made by a converter script; it is not the official text, and nothing here is verified against the official text.**
The converter garbled the Part 3 entries of the Arrangement of Sections (lines 61 to 73: the section numbers and titles come out in separate columns); that block is an index and no operative provision is affected.

## Seat

The seat is: a person who contracted on another party's written standard terms, or as a consumer, asking on facts they can state whether a clause that excludes or limits liability is effective against them, and when it must satisfy the reasonableness test.
Why this seat: Parts 1 and 3 of the Act are all about what a party with the benefit of an exclusion clause can and cannot do to the other party, and the person who meets the clause is the one who asks.
There is no seat for a court or arbitrator: what they must consider (ss 11(2), 11(4), 11(5)) is asked as what the person can expect.
The seat is two files, `ucta-seat.l4` (58 exported questions under `§§` groups in the text's order, each with `@export` and a `@desc` on every input) and `ucta-cases-seat.l4` (159 cases, at least one per question).
It has three tiers: the Part 3 question (the contract kind and 14 facts) gives the answer to the scope question (9 facts and that answer, asked for the section in question), whose answer is one input ("do the scope rules take my case out of this section?") to each section question.
The seat restates no rule: it maps plain answers (yes, no, "I am not sure", a date, a choice from a list) to the layer-1 inputs and calls the layer-1 function.
"I am not sure" becomes `NOTHING`, and a function that cannot answer without it answers `NOTHING`.
One input differs: "has it been shown that the clause satisfies the requirement of reasonableness?". Section 11(5) puts the burden of showing it on the party who claims it, so "I am not sure" there means "not shown" and gives the same answer as No (fork F13); the input's `@desc` says so.
The consumer answer is different again: "I am not sure" there means "not known" and is not turned into a presumption of consumer status (fork F14, with F8).

### Reading a result: FALSE and NOTHING

A decision function in this row answers a yes-or-no proposition about what a person can do or what applies: "can the other party exclude this liability", "does section 3 apply", "is the contract an international supply contract".
`JUST FALSE` is a "no" the Act gives in its own words: a flat negative ("cannot", "do not extend", "is not bound", "not precluded"), a definition that "means" (a body that is not a court, arbitrator, Government department or public authority is not a "competent authority"), an "only if", a failed "if", "when" or "where" on a positive statement, and a date before the Act's 12 November 1993 day in s 30(2).
So in this row `JUST FALSE` to "can the other party exclude the liability?" means the Act says it cannot; to "does section 3 apply?" it means the Act's own condition is not met.
`NOTHING` is "not covered": the Act is silent, lists without closing the list ("includes"), leaves a term undefined (what is fair and reasonable, who deals as consumer on facts not given), points outside the text (the Minister's order, the Sale of Goods Act 1979, section 5 of the Civil Law Act 1909), or limits a grant or bar in its own wording and the case is outside the limit.
The most common `NOTHING` here is the lifted bar: where a section says a person "cannot" do something "except in so far as the term satisfies the requirement of reasonableness" and the term is reasonable, the exception is met, the bar is lifted, and the section grants nothing (ruling QA, by the text's spelling; see the judgment calls).
**A caller must never turn `NOTHING` into `FALSE`:** `NOTHING` to "can the other party exclude this liability?" does not mean the other party can; it means this provision does not answer.
Where a question is asked about a reasonable clause, the answer `NOTHING` for "can the other party rely on it?" is not a no and not a yes: the clause may be effective, and the Act says only that this section does not stop it.
**A section taken out of the case by a flat negative** (the First Schedule's "do not extend to", section 1(3)'s "only", a Part 3 provision; fork F15): the functions in the text's own polarity, "does a requirement of reasonableness apply under this section?", answer `JUST FALSE`.
The functions that ask whether the person CAN exclude, rely or be made to do something answer `NOTHING` there, because the Act then says nothing about whether they can.
Where the removal rests on something the text does not settle (whether the person protected deals as consumer is not known and the Schedule answers differently on either answer; the Minister's order; section 5 of the Civil Law Act 1909), every one of them answers `NOTHING`.
**Reasonableness nobody has shown** (fork F13): section 11(5) puts the burden of showing that a term satisfies the requirement on the party who claims it does.
Where the term is not shown reasonable (it is unreasonable, or nobody has shown it either way) the "can exclude / can rely / can be made to indemnify" functions of ss 2(2), 3(2), 4(1), 6(3), 7(3) and 7(4) answer `JUST FALSE`.
Where it is shown reasonable the bar is lifted: the "cannot ... except" sites (ss 2(2), 3(2), 4(1), 7(4)) answer `NOTHING` and the "can be excluded ... but only" sites (ss 6(3), 7(3)) answer `JUST TRUE`.
**A "where" on a negative statement** (fork F6): the function in the text's own words (for example `s 27(1) sections 2 to 7 do not operate as part of the proper law`) answers `JUST TRUE` inside the "Where" and `JUST FALSE` outside it; its positive partner (`... operate ...`) answers `NOTHING` outside, because a `JUST FALSE` there would be a yes the text does not give.

## What is encoded, and what is not

Layer 1 (the law, in the text's order; each module imports `ucta-nouns` and `ucta-logic`):

| module | provisions | tests |
|---|---|---|
| `ucta-nouns.l4` | the kinds of thing the Act speaks of (declarations only) | none needed |
| `ucta-logic.l4` | the three-valued readers `and also`, `or else`, `not so`, `known to be`, `is a yes`, `is a no`, `is unknown` | 22 assertions in the file |
| `ucta-p1-introductory.l4` | s 1 (negligence, business liability, immateriality) and the reach aggregator for ss 2 to 7 | `ucta-tests-introductory.l4`: 130 |
| `ucta-p1-avoidance.l4` | ss 2 to 4 | `ucta-tests-avoidance.l4`: 98 |
| `ucta-p1-goods.l4` | ss 5 to 7 | `ucta-tests-goods.l4`: 132 |
| `ucta-p1-other.l4` | ss 8 to 10 (s 8 is blank in this text) | `ucta-tests-other.l4`: 16 |
| `ucta-p1-explanatory.l4` | ss 11 to 14 (reasonableness, dealing as consumer, varieties of exemption clause, the definitions table) | `ucta-tests-explanatory.l4`: 109 |
| `ucta-part3.l4` | ss 26 to 30 and the Part 3 outcome for s 1(2) (Part 2, ss 15 to 25, is shown only as a note) | `ucta-tests-part3.l4`: 67 |
| `ucta-schedules.l4` | First Schedule paras 1 to 4, Second Schedule (a) to (e) | `ucta-tests-schedules.l4`: 42 |
| `ucta-fixtures.l4` | test constructors only (not law) | none |

Layer 2: `ucta-seat.l4` and `ucta-cases-seat.l4` (159 assertions).
Support files: `check.sh`, `srcrefs.py` (both as supplied), `coverage.py` and `coverage-rows.tsv` (the coverage audit), `encoding.json`, `SOURCE-LICENSE.md`, `PROGRESS.md`, `BRIEF.md`.
Every non-blank line of the text is in a coverage row (see the audit below).
Not encoded as law: the title page, headings, arrangement, long title, enactment date, short title (s 30(1)), editorial `[44/96]` markers, page furniture, the Legislative History and the Abbreviations (all `inert`); s 8 and the Part 2 note (shown blank in this text).
Source quotes in the modules are `-- src:N-M | text` lines copied mechanically from `UCTA1977.txt` by a build script that read the file; the script has been removed from the deposit (the deposit is flat), and `srcrefs.py check --refs` re-verifies that every quote is a slice of the raw lines and that every `@ref` locator is covered by quotes.

## Jural relations

Hohfeld's kinds: a right (claim) correlates with a duty; a privilege with a no-right; a power with a liability; an immunity with a disability.
Almost every operative provision of this Act is a **disability** of the party with the benefit of an exclusion clause (it cannot exclude) and the correlative **immunity** of the other party, or a **privilege** (the Act does not reach the case).
The Act creates no duty to act by a deadline, so there is no `SHANT` and no regulative rule: the kinds are recorded here and not typed into the answers (ruling N2).
`none` marks a provision that creates no relation between the parties (a definition, a test, a rule of reading, machinery).

| provision | holder | bearer of the correlative | kind | L4 rule |
|---|---|---|---|---|
| s 1(1) negligence | none | none | definition | `s 1(1) the breach is negligence` (ucta-p1-introductory.l4:31) |
| s 1(2) this Part subject to Part 3 and the First Schedule | none | none | ordering of rules | `s 1(2) and (3) whether an exception takes the section out of the case` (ucta-p1-introductory.l4:121) |
| s 1(3) business liability | none | none | scope and definition | `s 1(3) the liability is business liability` (ucta-p1-introductory.l4:48) |
| s 1(4) immaterial whether inadvertent or intentional, direct or vicarious | none | none | rule of reading | `s 1(4) it makes a difference for this Part` (ucta-p1-introductory.l4:61) |
| s 2(1) death or personal injury by negligence | the person injured (or the estate) | the person who would exclude liability | immunity / disability | `s 2(1) ...` (ucta-p1-avoidance.l4:40) |
| s 2(2) other loss by negligence | the person who suffers the loss | the person who would exclude liability (lifted so far as the term is reasonable) | immunity / disability | `s 2(2) ...` (ucta-p1-avoidance.l4:88) |
| s 2(3) agreement or awareness is not voluntary acceptance of risk | the person who agreed or knew | the person relying on the term or notice | immunity / disability | `s 2(3) ...` (ucta-p1-avoidance.l4:104); in its own words (ucta-p1-avoidance.l4:123) |
| s 3(1) section 3 applies between contracting parties | none | none | scope | `s 3(1) ...` (ucta-p1-avoidance.l4:147) |
| s 3(2) the other cannot exclude own breach, or claim different or no performance | the party dealing as consumer or on written standard terms | the other contracting party (lifted so far as the term is reasonable) | immunity / disability | `s 3(2) ...` (ucta-p1-avoidance.l4:222) |
| s 4(1) indemnity | the person dealing as consumer | the person who would make them indemnify (lifted so far as the term is reasonable) | immunity / disability | `s 4(1) ...` (ucta-p1-avoidance.l4:275) |
| s 4(2) direct or vicarious, owed to the consumer or another | none | none | extent of s 4(1) | `s 4(2) ...` (ucta-p1-avoidance.l4:291) |
| s 5(1) guarantee of consumer goods | the person whose consumer goods prove defective | the manufacturer or distributor relying on a term or notice in a guarantee | immunity / disability | `s 5(1) ...` (ucta-p1-goods.l4:94); in its own words (ucta-p1-goods.l4:135) |
| s 5(2) in consumer use; guarantee | none | none | definitions | ucta-p1-goods.l4:40; ucta-p1-goods.l4:56 |
| s 5(3) not between the parties to the contract under which the goods passed | none | none | limit on s 5 | `s 5(3) ...` (ucta-p1-goods.l4:69) |
| s 6(1) title obligations in sale and hire-purchase | the buyer or hirer | the seller or owner | immunity / disability | `s 6(1) ...` (ucta-p1-goods.l4:188) |
| s 6(2) quality and fitness against a consumer | the consumer buyer or hirer | the seller or owner | immunity / disability | `s 6(2) ...` (ucta-p1-goods.l4:217) |
| s 6(3) quality and fitness against a non-consumer | the seller or owner (a power to exclude by a reasonable term) | the non-consumer buyer or hirer (liability) | power / liability | `s 6(3) ...` (ucta-p1-goods.l4:279) |
| s 6(4) liabilities include those under sale and hire-purchase | none | none | scope | `s 6(4) ...` (ucta-p1-goods.l4:170) |
| s 7(1) goods pass under another contract | none | none | scope | `s 7(1) ...` (ucta-p1-goods.l4:321) |
| s 7(2) description, sample, quality, fitness against a consumer | the consumer transferee | the transferor | immunity / disability | `s 7(2) ...` (ucta-p1-goods.l4:339) |
| s 7(3) the same against a non-consumer | the transferor (a power to exclude by a reasonable term) | the non-consumer transferee (liability) | power / liability | `s 7(3) ...` (ucta-p1-goods.l4:403) |
| s 7(3A) section 2 Supply of Goods Act 1982 | the transferee | the transferor | immunity / disability | `s 7(3A) ...` (ucta-p1-goods.l4:445) |
| s 7(4) ownership and quiet possession | the transferee | the transferor (lifted so far as the term is reasonable) | immunity / disability | `s 7(4) ...` (ucta-p1-goods.l4:516) |
| s 8 | none (blank in this text) | none | repealed or blank | no rule |
| Part 2 (ss 15 to 25, Scotland) | none (not applicable in this text) | none | repealed or blank | no rule |
| s 9(1) a term may be found reasonable after termination | the party relying on the term | the other party | privilege / no-right | `s 9(1) ...` (ucta-p1-other.l4:27) |
| s 9(2) affirmation does not of itself exclude the requirement | the party against whom the term is relied on | the party relying on the term | immunity / disability | `s 9(2) ...` (ucta-p1-other.l4:45); in its own words (ucta-p1-other.l4:59) |
| s 10 secondary contract | the person whose rights against another are taken away | the party to the secondary contract who relies on the term | immunity / disability | `s 10 ...` (ucta-p1-other.l4:78) |
| s 11(1), (3) the reasonableness test | none | none | test | ucta-p1-explanatory.l4:32; ucta-p1-explanatory.l4:50 |
| s 11(2) first limb: regard to the Second Schedule for ss 6 and 7 | the parties (a claim that the court have regard) | the court or arbitrator (a duty) | claim / duty | `s 11(2) ...` (ucta-p1-explanatory.l4:82) |
| s 11(2) second limb: a term may be held not to be a term of the contract | the court or arbitrator (a power preserved) | the party relying on the term (liability) | power / liability | `s 11(2) ...` (ucta-p1-explanatory.l4:100) |
| s 11(4) a cap on liability: resources and insurance | the parties (a claim that the court have regard) | the court or arbitrator (a duty) | claim / duty | `s 11(4) ...` (ucta-p1-explanatory.l4:119; ucta-p1-explanatory.l4:138) |
| s 11(5) burden of showing reasonableness | none (a burden of proof, not a relation between the parties) | none | procedural | `s 11(5) ...` (ucta-p1-explanatory.l4:151) |
| s 12(1), (2) dealing as consumer | none | none | definition | ucta-p1-explanatory.l4:173; ucta-p1-explanatory.l4:200 |
| s 12(3) burden of showing a party does not deal as consumer | none (a burden of proof) | none | procedural | `s 12(3) ...` (ucta-p1-explanatory.l4:234) |
| s 13(1) varieties of exemption clause | the person protected by Part 1 | the party relying on a condition, a limit on remedies or evidence, or a term excluding the duty itself | immunity / disability | `s 13(1) ...` (ucta-p1-explanatory.l4:263) |
| s 13(2) arbitration agreement | none | none | rule of characterisation | `s 13(2) ...` (ucta-p1-explanatory.l4:300) |
| s 14 definitions | none | none | definitions | ucta-p1-explanatory.l4:345; ucta-p1-explanatory.l4:360; ucta-p1-explanatory.l4:377; ucta-p1-explanatory.l4:391; ucta-p1-explanatory.l4:400 |
| s 26(1), (2) international supply contracts | a party to such a contract (a privilege to exclude liability freely) | the other party (a no-right) | privilege / no-right | ucta-part3.l4:65; ucta-part3.l4:78 |
| s 26(3), (4) the description of such a contract | none | none | definition | `s 26(3) and (4) ...` (ucta-part3.l4:41) |
| s 27(1) Singapore law only by choice | a party (a privilege: Part 1 is not part of the chosen law) | the other party (a no-right) | privilege / no-right | `s 27(1) ...` (ucta-part3.l4:94); in its own words (ucta-part3.l4:108) |
| s 27(2) foreign-law term | the party who evaded the Act, or the Singapore consumer | the party relying on the foreign-law term | immunity / disability | `s 27(2) ...` (ucta-part3.l4:133) |
| s 28(1) sea carriage of a passenger | none | none | scope | `s 28(1) ...` (ucta-part3.l4:158) |
| s 28(2) exclusion as the Minister's order prescribes | the carrier (a privilege) | the passenger (a no-right) | privilege / no-right | `s 28(2) ...` (ucta-part3.l4:172) |
| s 29(1) provisions authorised by an enactment or an international agreement | the party relying on the provision (a privilege) | the other party (a no-right) | privilege / no-right | `s 29(1) ...` (ucta-part3.l4:235) |
| s 29(2) a term approved by a competent authority is taken as reasonable | none (a deeming rule) | none | deeming | `s 29(2) ...` (ucta-part3.l4:260) |
| s 29(3) definitions | none | none | definitions | ucta-part3.l4:196; ucta-part3.l4:208; ucta-part3.l4:220 |
| s 30(1) short title | none | none | machinery | no rule |
| s 30(2) before 12 November 1993 | the party relying on the contract or the liability (an immunity from the Act) | the other party (a disability to invoke the Act) | immunity / disability | `s 30(2) ...` (ucta-part3.l4:284) |
| First Schedule para 1 | a party to the listed kinds of contract (a privilege: ss 2 to 4 do not reach it) | the other party (a no-right) | privilege / no-right | `sch 1 para 1 ...` (ucta-schedules.l4:47); company: ucta-schedules.l4:68 |
| First Schedule para 2 | s 2(1) extends: the person injured (an immunity); otherwise a party (a privilege) except in favour of a consumer | the other party | immunity / disability; privilege / no-right | ucta-schedules.l4:83; ucta-schedules.l4:104 |
| First Schedule para 3 | a party to a contract of carriage by ship or hovercraft (a privilege) except in favour of a consumer | the other party (a no-right) | privilege / no-right | `sch 1 para 3 ...` (ucta-schedules.l4:132) |
| First Schedule para 4 | an employer (a privilege: s 2(1), (2) do not reach) except in favour of the employee | the employee (a no-right) | privilege / no-right | `sch 1 para 4 ...` (ucta-schedules.l4:161) |
| Second Schedule (a) to (e) | none (matters for the court under s 11(2)) | none | guidelines | ucta-schedules.l4:238 |

## Coverage

The table is built by `coverage.py` from `coverage-rows.tsv` and the raw text; it checks that every non-blank line of the text is in some row, that every row has exactly one disposition (`encoded`, `inert`, `fork` or `repealed-or-blank`), that an `inert` row gives reason 1, 2 or 3, and that the function an `encoded` or `fork` row names exists in the named file.
There is no out-of-scope row and no deferred row.

Audit, as the script printed it on the final run:

```
rows: 196
  encoded: 88
  fork: 39
  inert: 66
  repealed-or-blank: 3
    inert reason 1: 65
    inert reason 2: 1
non-blank text lines: 476; not in any row: 0
```

Rows before and after the audit: **180 rows before** (one per section, subsection, paragraph, schedule item, defined term, table row and heading, written from the structure of the text); the audit found 24 non-blank lines in no row (page running heads, dates and page numbers, the `[44/96]` markers and a Schedule caption), and **196 rows after** (16 added: 14 page-furniture rows and 2 amendment-marker rows, all `inert` reason 1); no operative row changed. Text units counted: 476 non-blank lines, all in a row after the audit.

No row changed disposition between the 180-row and the 196-row table. Rows moved out of `inert`: none in the tables; s 30(2) (the transitional date test) was decided at planning to be encoded and tested, because it can decide a case about a contract made before 12 November 1993, and never stood as an `inert` row. s 8 and the Part 2 note are `repealed-or-blank`, not `inert`. The reasons used for `inert` are 1 (not operative: titles, headings, arrangement, long title, enactment date, editorial markers, page furniture, the Legislative History, which the text itself says "is not part of the Act", and the Abbreviations) and 2 (machinery: the short title, s 30(1)). Reason 3 is not used.

| id | lines | unit | provision | disposition | where | fork |
|---|---|---|---|---|---|---|
| C001 | 1-14 | title page | Statute title, revised edition, publisher | inert | inert reason 1 |  |
| C002 | 16-50 | arrangement | Arrangement of sections, Part 1 entries 1 to 14 | inert | inert reason 1 |  |
| C003 | 52-55 | page furniture | Page break: page number, date and running header (pages 1 to 2) | inert | inert reason 1 |  |
| C004 | 57-59 | Part 2 entry | Arrangement entry: Sections 15 to 25 relating to Scotland not applicable | repealed-or-blank | the text shows a bracketed note that sections 15 to 25 (Scotland) are not applicable; there is no text |  |
| C005 | 61-73 | arrangement | Arrangement of sections, Part 3 entries 26 to 30 and the two Schedules (the converter garbled the columns) | inert | inert reason 1 |  |
| C006 | 75-77 | long title | An Act to impose further limits ... | inert | inert reason 1 |  |
| C007 | 79 | enactment date | [12 November 1993] | inert | inert reason 1 |  |
| C008 | 81-83 | heading | Part 1, Introductory | inert | inert reason 1 |  |
| C009 | 85 | heading | Scope of this Part | inert | inert reason 1 |  |
| C010 | 86-88 | subsection | s 1(1) chapeau, negligence means the breach | encoded | ucta-p1-introductory.l4::s 1(1) the breach is negligence |  |
| C011 | 90-92 | paragraph | s 1(1)(a) contractual duty of care | encoded | ucta-p1-introductory.l4::s 1(1) the breach is negligence |  |
| C012 | 94-95 | paragraph | s 1(1)(b) common law duty of care (not any stricter duty) | encoded | ucta-p1-introductory.l4::s 1(1) the breach is negligence |  |
| C013 | 97-99 | subsection | s 1(2) this Part subject to Part 3 and, for contracts, the First Schedule | encoded | ucta-p1-introductory.l4::s 1(2) and (3) whether an exception takes the section out of the case |  |
| C014 | 100 | page furniture | Page break: running header (page 3) | inert | inert reason 1 |  |
| C015 | 102-107 | subsection | s 1(3) sections 2 to 7 apply only to business liability (except s 6(4)) | fork | ucta-p1-introductory.l4::s 1(2) and (3) whether an exception takes the section out of the case | F5 |
| C016 | 102-107 | defined term | s 1(3) business liability | encoded | ucta-p1-introductory.l4::s 1(3) the liability is business liability |  |
| C017 | 109-111 | subsection | s 1(4) inadvertent or intentional, direct or vicarious, immaterial | encoded | ucta-p1-introductory.l4::s 1(4) it makes a difference for this Part |  |
| C018 | 113 | heading | Avoidance of liability for negligence, breach of contract, etc. | inert | inert reason 1 |  |
| C019 | 115 | heading | Negligence liability | inert | inert reason 1 |  |
| C020 | 117-120 | subsection | s 2(1) death or personal injury resulting from negligence | encoded | ucta-p1-avoidance.l4::s 2(1) the person can exclude or restrict liability for death or personal injury resulting from negligence |  |
| C021 | 122-124 | subsection | s 2(2) other loss or damage, except so far as reasonable | fork | ucta-p1-avoidance.l4::s 2(2) the person can exclude or restrict liability for other loss or damage resulting from negligence | F1,F11,F13,F15 |
| C022 | 126-129 | subsection | s 2(3) agreement or awareness not voluntary acceptance of risk | fork | ucta-p1-avoidance.l4::s 2(3) the person's agreement to or awareness of the term or notice is not of itself to be taken as indicating voluntary acceptance of the risk | F6 |
| C023 | 131 | heading | Liability arising in contract | inert | inert reason 1 |  |
| C024 | 133-135 | subsection | s 3(1) application between contracting parties | encoded | ucta-p1-avoidance.l4::s 3(1) this section applies as between the contracting parties |  |
| C025 | 137-138 | subsection | s 3(2) chapeau, as against that party the other cannot by reference to any contract term | fork | ucta-p1-avoidance.l4::s 3(2) the other party can rely on the contract term as against that party | F1,F7,F13,F15 |
| C026 | 140-141 | paragraph | s 3(2)(a) when himself in breach, exclude or restrict liability | fork | ucta-p1-avoidance.l4::s 3(2) the other party can rely on the contract term as against that party | F1,F6 |
| C027 | 143-144 | page furniture | Page break: date and running header (pages 3 to 4) | inert | inert reason 1 |  |
| C028 | 146 | paragraph | s 3(2)(b) claim to be entitled | fork | ucta-p1-avoidance.l4::s 3(2) the other party can rely on the contract term as against that party | F1 |
| C029 | 148-150 | paragraph | s 3(2)(b)(i) substantially different performance | fork | ucta-p1-avoidance.l4::s 3(2) the other party can rely on the contract term as against that party | F1 |
| C030 | 152-154 | paragraph | s 3(2)(b)(ii) no performance at all | fork | ucta-p1-avoidance.l4::s 3(2) the other party can rely on the contract term as against that party | F1 |
| C031 | 155-156 | subsection | s 3(2) closing words, except so far as reasonable | fork | ucta-p1-avoidance.l4::s 3(2) a requirement of reasonableness applies to the contract term | F1,F15 |
| C032 | 158 | heading | Unreasonable indemnity clauses | inert | inert reason 1 |  |
| C033 | 160-164 | subsection | s 4(1) indemnity by a person dealing as consumer | fork | ucta-p1-avoidance.l4::s 4(1) the person dealing as consumer can be made to indemnify the other person | F1,F7,F13,F15 |
| C034 | 166 | subsection | s 4(2) chapeau, this section applies whether the liability | encoded | ucta-p1-avoidance.l4::s 4(2) section 4 applies to the liability |  |
| C035 | 168-169 | paragraph | s 4(2)(a) directly or vicariously | encoded | ucta-p1-avoidance.l4::s 4(2) section 4 applies to the liability |  |
| C036 | 171 | paragraph | s 4(2)(b) to the person dealing as consumer or to someone else | encoded | ucta-p1-avoidance.l4::s 4(2) section 4 applies to the liability |  |
| C037 | 173 | heading | Liability arising from sale or supply of goods | inert | inert reason 1 |  |
| C038 | 175 | heading | Guarantee of consumer goods | inert | inert reason 1 |  |
| C039 | 177-178 | subsection | s 5(1) chapeau, goods of a type ordinarily supplied for private use or consumption | fork | ucta-p1-goods.l4::s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee | F6 |
| C040 | 180-181 | paragraph | s 5(1)(a) defective while in consumer use | encoded | ucta-p1-goods.l4::s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee |  |
| C041 | 183-184 | paragraph | s 5(1)(b) negligence of a person concerned in manufacture or distribution | encoded | ucta-p1-goods.l4::s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee |  |
| C042 | 186-188 | subsection | s 5(1) closing words, cannot be excluded by a term or notice in a guarantee | encoded | ucta-p1-goods.l4::s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee |  |
| C043 | 189 | page furniture | Page break: running header (page 5) | inert | inert reason 1 |  |
| C044 | 191 | subsection | s 5(2) chapeau, for these purposes | encoded | ucta-p1-goods.l4::s 5(2)(a) the goods are in consumer use |  |
| C045 | 193-196 | paragraph | s 5(2)(a) in consumer use | encoded | ucta-p1-goods.l4::s 5(2)(a) the goods are in consumer use |  |
| C046 | 198-202 | paragraph | s 5(2)(b) guarantee | fork | ucta-p1-goods.l4::s 5(2)(b) the writing is a guarantee | F18 |
| C047 | 204-206 | subsection | s 5(3) not between the parties to a contract under which the goods passed | encoded | ucta-p1-goods.l4::s 5(3) section 5 applies as between the parties |  |
| C048 | 208 | heading | Sale and hire-purchase | inert | inert reason 1 |  |
| C049 | 210 | subsection | s 6(1) chapeau | encoded | ucta-p1-goods.l4::s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions |  |
| C050 | 212-213 | paragraph | s 6(1)(a) section 12 Sale of Goods Act 1979 | encoded | ucta-p1-goods.l4::s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions |  |
| C051 | 215-216 | paragraph | s 6(1)(b) section 6 Hire-Purchase Act 1969 | encoded | ucta-p1-goods.l4::s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions |  |
| C052 | 218 | subsection | s 6(1) closing words, cannot be excluded by any contract term | fork | ucta-p1-goods.l4::s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions | F7 |
| C053 | 220-221 | subsection | s 6(2) chapeau, as against a person dealing as consumer | encoded | ucta-p1-goods.l4::s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions |  |
| C054 | 223-226 | paragraph | s 6(2)(a) sections 13, 14 or 15 Sale of Goods Act 1979 | encoded | ucta-p1-goods.l4::s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions |  |
| C055 | 228-229 | paragraph | s 6(2)(b) sections 6A, 6B or 6C Hire-Purchase Act 1969 | encoded | ucta-p1-goods.l4::s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions |  |
| C056 | 231 | subsection | s 6(2) closing words, cannot be excluded by any contract term | fork | ucta-p1-goods.l4::s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions | F7,F8 |
| C057 | 233-240 | subsection | s 6(3) against a non-consumer, only so far as reasonable | fork | ucta-p1-goods.l4::s 6(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability specified in subsection (2) | F2,F8,F13,F15 |
| C058 | 242-244 | subsection | s 6(4) the liabilities include those under a sale or hire-purchase | encoded | ucta-p1-goods.l4::s 6(4) the liability is one referred to in section 6 |  |
| C059 | 246 | heading | Miscellaneous contracts under which goods pass | inert | inert reason 1 |  |
| C060 | 248-253 | subsection | s 7(1) goods pass under a contract not governed by sale of goods or hire-purchase | encoded | ucta-p1-goods.l4::s 7(1) subsections (2) to (4) apply |  |
| C061 | 255-258 | subsection | s 7(2) against a consumer, description, sample, quality, fitness | fork | ucta-p1-goods.l4::s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness | F7,F8 |
| C062 | 260-262 | subsection | s 7(3) against a non-consumer, only so far as reasonable | fork | ucta-p1-goods.l4::s 7(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability in subsection (2) | F2,F8,F13,F15 |
| C063 | 264-267 | subsection | s 7(3A) section 2 Supply of Goods Act 1982 | encoded | ucta-p1-goods.l4::s 7(3A) the person can exclude or restrict liability for breach of the obligations arising under section 2 of the Supply of Goods Act 1982 |  |
| C064 | 269 | amendment marker | [44/96] editorial marker after s 7(3A): amended by Act 44 of 1996 | inert | inert reason 1 |  |
| C065 | 271 | subsection | s 7(4) chapeau, liability in respect of | fork | ucta-p1-goods.l4::s 7(4) the person can exclude or restrict liability for the right to transfer ownership or the assurance of quiet possession | F1,F13,F15 |
| C066 | 273-274 | paragraph | s 7(4)(a) the right to transfer ownership, or give possession | encoded | ucta-p1-goods.l4::s 7(4) the person can exclude or restrict liability for the right to transfer ownership or the assurance of quiet possession |  |
| C067 | 276-277 | paragraph | s 7(4)(b) assurance of quiet possession | encoded | ucta-p1-goods.l4::s 7(4) the person can exclude or restrict liability for the right to transfer ownership or the assurance of quiet possession |  |
| C068 | 279-281 | subsection | s 7(4) closing words, in a case to which (3A) does not apply, except so far as reasonable | fork | ucta-p1-goods.l4::s 7(4) a requirement of reasonableness applies to the contract term | F1,F15 |
| C069 | 283 | amendment marker | [44/96] editorial marker after s 7(4): amended by Act 44 of 1996 | inert | inert reason 1 |  |
| C070 | 284 | page furniture | Page break: running header (page 7) | inert | inert reason 1 |  |
| C071 | 286 | heading | Other provisions about contracts | inert | inert reason 1 |  |
| C072 | 288 | section | s 8 [Omitted in 1994 Revised Edition] | repealed-or-blank | the text shows the bracketed note [Omitted in 1994 Revised Edition]; there is no text |  |
| C073 | 290 | heading | Effect of breach | inert | inert reason 1 |  |
| C074 | 292-296 | subsection | s 9(1) termination of the contract | encoded | ucta-p1-other.l4::s 9(1) the contract term may be found to satisfy the requirement of reasonableness and be given effect |  |
| C075 | 298-300 | subsection | s 9(2) affirmation after breach | fork | ucta-p1-other.l4::s 9(2) affirming the contract does not of itself exclude the requirement of reasonableness in relation to the contract term | F6 |
| C076 | 302 | heading | Evasion by means of secondary contract | inert | inert reason 1 |  |
| C077 | 304-308 | section | s 10 evasion by means of secondary contract | fork | ucta-p1-other.l4::s 10 the person is bound by the contract term | F6 |
| C078 | 310 | heading | Explanatory provisions | inert | inert reason 1 |  |
| C079 | 312 | heading | Reasonableness test | inert | inert reason 1 |  |
| C080 | 314-319 | subsection | s 11(1) reasonableness for a contract term | fork | ucta-p1-explanatory.l4::s 11(1) the contract term satisfies the requirement of reasonableness | F7,F16 |
| C081 | 321-324 | subsection | s 11(2) first limb, regard to the Second Schedule for section 6 or 7 | fork | ucta-p1-explanatory.l4::s 11(2) the matters to which regard is had in determining reasonableness under section 6 or 7 | F10 |
| C082 | 324-327 | subsection | s 11(2) second limb, does not prevent holding that a term is not a term of the contract | fork | ucta-p1-explanatory.l4::s 11(2) the subsection prevents the court or arbitrator from holding that the term is not a term of the contract | F19 |
| C083 | 329-330 | page furniture | Page break: date and running header (pages 7 to 8) | inert | inert reason 1 |  |
| C084 | 332-336 | subsection | s 11(3) reasonableness for a notice | fork | ucta-p1-explanatory.l4::s 11(3) the notice satisfies the requirement of reasonableness | F7,F16 |
| C085 | 338-342 | subsection | s 11(4) chapeau, a sum of money cap | encoded | ucta-p1-explanatory.l4::s 11(4) regard is to be had in particular to the resources and insurance matters |  |
| C086 | 344-345 | paragraph | s 11(4)(a) resources | encoded | ucta-p1-explanatory.l4::s 11(4) the matters to which regard is had where liability is restricted to a specified sum |  |
| C087 | 347 | paragraph | s 11(4)(b) insurance | encoded | ucta-p1-explanatory.l4::s 11(4) the matters to which regard is had where liability is restricted to a specified sum |  |
| C088 | 349-350 | subsection | s 11(5) burden of showing reasonableness | fork | ucta-p1-explanatory.l4::s 11(5) the party must show that the term or notice satisfies the requirement of reasonableness | F13 |
| C089 | 352 | heading | Dealing as consumer | inert | inert reason 1 |  |
| C090 | 354-355 | subsection | s 12(1) chapeau, deals as consumer | encoded | ucta-p1-explanatory.l4::s 12(1) the party deals as consumer in relation to the other party |  |
| C091 | 354-366 | defined term | s 12(1) deals as consumer | encoded | ucta-p1-explanatory.l4::s 12(1) and (2) the party deals as consumer |  |
| C092 | 357-358 | paragraph | s 12(1)(a) neither in business nor holds out | encoded | ucta-p1-explanatory.l4::s 12(1) the party deals as consumer in relation to the other party |  |
| C093 | 360-361 | paragraph | s 12(1)(b) the other party makes the contract in business | encoded | ucta-p1-explanatory.l4::s 12(1) the party deals as consumer in relation to the other party |  |
| C094 | 363-366 | paragraph | s 12(1)(c) goods of a type ordinarily supplied for private use | fork | ucta-p1-explanatory.l4::s 12(1) the party deals as consumer in relation to the other party | F12 |
| C095 | 368-369 | subsection | s 12(2) auction or competitive tender | encoded | ucta-p1-explanatory.l4::s 12(2) the buyer is regarded as dealing as consumer |  |
| C096 | 371-372 | subsection | s 12(3) burden of showing a party does not deal as consumer | fork | ucta-p1-explanatory.l4::s 12(3) the party must show that a party does not deal as consumer | F14 |
| C097 | 373 | page furniture | Page break: running header (page 9) | inert | inert reason 1 |  |
| C098 | 375 | heading | Varieties of exemption clause | inert | inert reason 1 |  |
| C099 | 377-378 | subsection | s 13(1) chapeau, to the extent this Part prevents | encoded | ucta-p1-explanatory.l4::s 13(1) the person can use the exemption clause to avoid the liability |  |
| C100 | 380-381 | paragraph | s 13(1)(a) restrictive or onerous conditions | encoded | ucta-p1-explanatory.l4::s 13(1) the person can use the exemption clause to avoid the liability |  |
| C101 | 383-385 | paragraph | s 13(1)(b) rights or remedies, prejudice for pursuing them | encoded | ucta-p1-explanatory.l4::s 13(1) the person can use the exemption clause to avoid the liability |  |
| C102 | 387 | paragraph | s 13(1)(c) rules of evidence or procedure | encoded | ucta-p1-explanatory.l4::s 13(1) the person can use the exemption clause to avoid the liability |  |
| C103 | 389-391 | subsection | s 13(1) closing words, sections 2 and 5 to 7 and the relevant obligation or duty | encoded | ucta-p1-explanatory.l4::s 13(1) the person can use the exemption clause to avoid the liability |  |
| C104 | 393-395 | subsection | s 13(2) arbitration agreement | encoded | ucta-p1-explanatory.l4::s 13(2) the agreement is treated under this Part as excluding or restricting liability |  |
| C105 | 397 | heading | Interpretation of this Part | inert | inert reason 1 |  |
| C106 | 399 | section | s 14 chapeau, in this Part | encoded | ucta-p1-explanatory.l4::s 14 and ss 1, 5, 12 and 29(3) what the Act says the word means |  |
| C107 | 400-401 | defined term | s 14 business | encoded | ucta-p1-explanatory.l4::s 14 the activity is within "business" |  |
| C108 | 403 | defined term | s 14 goods | encoded | ucta-p1-explanatory.l4::s 14 the thing is "goods" |  |
| C109 | 405-406 | defined term | s 14 hire-purchase agreement | encoded | ucta-p1-explanatory.l4::s 14 the agreement is a "hire-purchase agreement" |  |
| C110 | 408 | defined term | s 14 negligence | encoded | ucta-p1-explanatory.l4::s 14 and ss 1, 5, 12 and 29(3) what the Act says the word means |  |
| C111 | 409-411 | defined term | s 14 notice | encoded | ucta-p1-explanatory.l4::s 14 the communication is within "notice" |  |
| C112 | 413-414 | defined term | s 14 personal injury | encoded | ucta-p1-explanatory.l4::s 14 the harm is within "personal injury" |  |
| C113 | 416-417 | page furniture | Page break: date and running header (pages 9 to 10) | inert | inert reason 1 |  |
| C114 | 419 | heading | Part 2 | inert | inert reason 1 |  |
| C115 | 421 | Part 2 note | Sections 15 to 25 relating to Scotland not applicable | repealed-or-blank | the text shows a bracketed note that sections 15 to 25 (Scotland) are not applicable; there is no text |  |
| C116 | 423-425 | heading | Part 3, Miscellaneous | inert | inert reason 1 |  |
| C117 | 427 | heading | International supply contracts | inert | inert reason 1 |  |
| C118 | 429-432 | subsection | s 26(1) limits do not apply to an international supply contract | fork | ucta-part3.l4::s 26(1) the limits imposed by this Act on excluding or restricting liability apply to liability under the contract | F6 |
| C119 | 434-435 | subsection | s 26(2) no requirement of reasonableness under section 3 or 4 | fork | ucta-part3.l4::s 26(2) the terms of the contract are subject to a requirement of reasonableness under section 3 or 4 | F6 |
| C120 | 437-438 | subsection | s 26(3) chapeau, subject to subsection (4) | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C121 | 440-442 | paragraph | s 26(3)(a) sale of goods or goods pass | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C122 | 444-446 | paragraph | s 26(3)(b) different States | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C123 | 448 | subsection | s 26(4) chapeau, only if either | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C124 | 450-452 | paragraph | s 26(4)(a) carriage from one State to another | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C125 | 454-455 | paragraph | s 26(4)(b) offer and acceptance in different States | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C126 | 457-459 | paragraph | s 26(4)(c) delivery to another State | encoded | ucta-part3.l4::s 26(3) and (4) the contract is an international supply contract |  |
| C127 | 460 | page furniture | Page break: running header (page 11) | inert | inert reason 1 |  |
| C128 | 462 | heading | Choice of law clauses | inert | inert reason 1 |  |
| C129 | 464-467 | subsection | s 27(1) Singapore law only by choice | fork | ucta-part3.l4::s 27(1) sections 2 to 7 do not operate as part of the proper law | F6 |
| C130 | 469-471 | subsection | s 27(2) chapeau, notwithstanding a foreign-law term | encoded | ucta-part3.l4::s 27(2) this Act has effect notwithstanding the term applying the law of a country outside Singapore |  |
| C131 | 473-475 | paragraph | s 27(2)(a) imposed to evade the Act | encoded | ucta-part3.l4::s 27(2) this Act has effect notwithstanding the term applying the law of a country outside Singapore |  |
| C132 | 477-481 | paragraph | s 27(2)(b) consumer habitually resident in Singapore, essential steps there | encoded | ucta-part3.l4::s 27(2) this Act has effect notwithstanding the term applying the law of a country outside Singapore |  |
| C133 | 483 | heading | Provision for sea carriage of passengers | inert | inert reason 1 |  |
| C134 | 485-486 | subsection | s 28(1) carriage by sea of a passenger | encoded | ucta-part3.l4::s 28(1) section 28 applies to the contract |  |
| C135 | 488-491 | subsection | s 28(2) not precluded as prescribed by the Minister's order | fork | ucta-part3.l4::s 28(2) this Act precludes the person from excluding or restricting liability for loss or damage | F6,F17 |
| C136 | 493 | heading | Saving for other relevant legislation | inert | inert reason 1 |  |
| C137 | 495-496 | subsection | s 29(1) chapeau, nothing in this Act removes the effect of a contractual provision | fork | ucta-part3.l4::s 29(1) this Act removes or restricts the effect of, or prevents reliance upon, the contractual provision | F6 |
| C138 | 498-499 | paragraph | s 29(1)(a) authorised or required by an enactment | encoded | ucta-part3.l4::s 29(1) this Act removes or restricts the effect of, or prevents reliance upon, the contractual provision |  |
| C139 | 501-504 | paragraph | s 29(1)(b) compliance with an international agreement | encoded | ucta-part3.l4::s 29(1) this Act removes or restricts the effect of, or prevents reliance upon, the contractual provision |  |
| C140 | 506-507 | page furniture | Page break: date and running header (pages 11 to 12) | inert | inert reason 1 |  |
| C141 | 509-514 | subsection | s 29(2) a term approved by a competent authority is taken as reasonable | encoded | ucta-part3.l4::s 29(2) the contract term is taken as satisfying the requirement of reasonableness |  |
| C142 | 516 | subsection | s 29(3) chapeau, in this section | encoded | ucta-part3.l4::s 29(3) the body is a competent authority |  |
| C143 | 518-519 | defined term | s 29(3) competent authority | encoded | ucta-part3.l4::s 29(3) the body is a competent authority |  |
| C144 | 521-523 | defined term | s 29(3) enactment | encoded | ucta-part3.l4::s 29(3) the instrument is an enactment |  |
| C145 | 525 | defined term | s 29(3) statutory | encoded | ucta-part3.l4::s 29(3) the jurisdiction or function is statutory |  |
| C146 | 527 | heading | Short title and transitional | inert | inert reason 1 |  |
| C147 | 529-530 | subsection | s 30(1) short title | inert | inert reason 2 |  |
| C148 | 532-535 | subsection | s 30(2) nothing applies to a contract made or a loss suffered before 12 November 1993 | fork | ucta-part3.l4::s 30(2) this Act applies in relation to the contract or the liability for loss or damage | F4 |
| C149 | 537-541 | heading | First Schedule, Scope of sections 2 to 4 and 7 (caption: Section 1(2)) | inert | inert reason 1 |  |
| C150 | 543 | paragraph | Sch 1 para 1 chapeau, sections 2 to 4 do not extend to | fork | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract | F9 |
| C151 | 545-546 | paragraph | Sch 1 para 1(a) contract of insurance | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C152 | 548-550 | paragraph | Sch 1 para 1(b) interest in land | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C153 | 552-555 | paragraph | Sch 1 para 1(c) intellectual property | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C154 | 556 | page furniture | Page break: running header (page 13) | inert | inert reason 1 |  |
| C155 | 558 | page furniture | Page break: caption FIRST SCHEDULE - continued | inert | inert reason 1 |  |
| C156 | 560 | paragraph | Sch 1 para 1(d) company | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C157 | 562-564 | paragraph | Sch 1 para 1(d)(i) formation or dissolution of a company | encoded | ucta-schedules.l4::sch 1 para 1(d)(i) the entity is a company |  |
| C158 | 562-564 | defined term | Sch 1 para 1(d)(i) company | encoded | ucta-schedules.l4::sch 1 para 1(d)(i) the entity is a company |  |
| C159 | 566-567 | paragraph | Sch 1 para 1(d)(ii) constitution or rights or obligations of corporators or members | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C160 | 569-570 | paragraph | Sch 1 para 1(e) securities | encoded | ucta-schedules.l4::sch 1 para 1 sections 2 to 4 extend to the contract |  |
| C161 | 572 | paragraph | Sch 1 para 2 chapeau, section 2(1) extends to | encoded | ucta-schedules.l4::sch 1 para 2 section 2(1) extends to the contract |  |
| C162 | 574 | paragraph | Sch 1 para 2(a) marine salvage or towage | encoded | ucta-schedules.l4::sch 1 para 2 section 2(1) extends to the contract |  |
| C163 | 576 | paragraph | Sch 1 para 2(b) charterparty of a ship or hovercraft | encoded | ucta-schedules.l4::sch 1 para 2 section 2(1) extends to the contract |  |
| C164 | 578 | paragraph | Sch 1 para 2(c) carriage of goods by ship or hovercraft | encoded | ucta-schedules.l4::sch 1 para 2 section 2(1) extends to the contract |  |
| C165 | 580-581 | paragraph | Sch 1 para 2 closing words, sections 2 to 4 and 7 do not extend except in favour of a consumer | fork | ucta-schedules.l4::sch 1 para 2 sections 2 to 4 and 7, subject to section 2(1), extend to the contract | F3 |
| C166 | 583-584 | paragraph | Sch 1 para 3 chapeau, goods carried by ship or hovercraft | encoded | ucta-schedules.l4::sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft |  |
| C167 | 586-587 | paragraph | Sch 1 para 3(a) specifies that means of carriage over part of the journey | encoded | ucta-schedules.l4::sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft |  |
| C168 | 589-590 | paragraph | Sch 1 para 3(b) makes no provision as to the means and does not exclude it | encoded | ucta-schedules.l4::sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft |  |
| C169 | 592-594 | paragraph | Sch 1 para 3 closing words, sections 2(2), 3 and 4 do not extend except in favour of a consumer | fork | ucta-schedules.l4::sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft | F3 |
| C170 | 596-597 | paragraph | Sch 1 para 4 contract of employment | fork | ucta-schedules.l4::sch 1 para 4 section 2(1) and (2) extend to the contract | F3 |
| C171 | 599-600 | page furniture | Page break: date and running header (pages 13 to 14) | inert | inert reason 1 |  |
| C172 | 602-606 | heading | Second Schedule, Guidelines for application of reasonableness test (caption: Section 11(2)) | inert | inert reason 1 |  |
| C173 | 608-609 | paragraph | Sch 2 chapeau, matters to which regard is had for sections 6(3), 7(3) and (4) | fork | ucta-schedules.l4::sch 2 regard is to be had in particular to the guideline | F10 |
| C174 | 611-613 | paragraph | Sch 2(a) bargaining positions | encoded | ucta-schedules.l4::sch 2 the guidelines |  |
| C175 | 615-617 | paragraph | Sch 2(b) inducement or opportunity to contract elsewhere | encoded | ucta-schedules.l4::sch 2 the guidelines |  |
| C176 | 619-622 | paragraph | Sch 2(c) knowledge of the term | encoded | ucta-schedules.l4::sch 2 the guidelines |  |
| C177 | 624-627 | paragraph | Sch 2(d) practicability of compliance with a condition | encoded | ucta-schedules.l4::sch 2 the guidelines |  |
| C178 | 629-630 | paragraph | Sch 2(e) goods made to the customer's special order | encoded | ucta-schedules.l4::sch 2 the guidelines |  |
| C179 | 631-635 | heading | Legislative History heading and statement that it is not part of the Act | inert | inert reason 1 |  |
| C180 | 637-650 | history entry | Legislative History 1: U.K. 1977, c. 50; commencement; application; note | inert | inert reason 1 |  |
| C181 | 652-654 | history entry | Legislative History 2: 1994 Revised Edition | inert | inert reason 1 |  |
| C182 | 656-665 | history entry | Legislative History 3: Act 44 of 1996 | inert | inert reason 1 |  |
| C183 | 667-668 | page furniture | Page break: date and page number (Legislative History) | inert | inert reason 1 |  |
| C184 | 670 | heading | Abbreviations | inert | inert reason 1 |  |
| C185 | 672 | table row | Abbreviation C.P. | inert | inert reason 1 |  |
| C186 | 674 | table row | Abbreviation G.N. No. S (N.S.) | inert | inert reason 1 |  |
| C187 | 676 | table row | Abbreviation G.N. No. | inert | inert reason 1 |  |
| C188 | 678 | table row | Abbreviation G.N. No. S | inert | inert reason 1 |  |
| C189 | 680 | table row | Abbreviation G.N. Sp. No. S | inert | inert reason 1 |  |
| C190 | 682 | table row | Abbreviation L.A. | inert | inert reason 1 |  |
| C191 | 684-686 | table row | Abbreviation L.N. | inert | inert reason 1 |  |
| C192 | 688 | table row | Abbreviation M. Act | inert | inert reason 1 |  |
| C193 | 690 | table row | Abbreviation M. Ordinance | inert | inert reason 1 |  |
| C194 | 692 | table row | Abbreviation Parl. | inert | inert reason 1 |  |
| C195 | 694-695 | table row | Abbreviation S.S.G.G. (E) No. | inert | inert reason 1 |  |
| C196 | 697 | table row | Abbreviation S.S.G.G. No. | inert | inert reason 1 |  |

## Fork register

### The rulings of 2026-11-04 and 2026-11-05, word for word

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### What the rulings mean for the work, word for word (the brief's "What they mean for your work")

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### How E1 was applied

Option C throughout: each section answers on its own, and no function gathers a legal effect ("this clause is ineffective") from every section that gives it. No module gathers the Act's effects.
Where I gathered by hand, in plain L4, to help a reader (option B as guidance only):
- `s 1(2) and (3) whether an exception takes the section out of the case` (ucta-p1-introductory.l4:121) gathers s 1(3), First Schedule paras 1 to 4 and the Part 3 outcome for one section;
- `s 1(2) whether Part 3 takes sections 2 to 7 out of the case` (ucta-part3.l4:315) gathers ss 26(1), 26(2), 27(1), 28(2), 29(1) and 30(2);
- `ss 11(1), 11(3) and 29(2) the term or notice satisfies the requirement of reasonableness` (ucta-p1-explanatory.l4:66);
- `s 6(2) and (3) ...` (ucta-p1-goods.l4:296) and `s 7(2) and (3) ...` (ucta-p1-goods.l4:421) combine two subsections when consumer status is not known; `s 12(1) and (2) the party deals as consumer` (ucta-p1-explanatory.l4:222).

### Judgment calls

One line per site: question id, provision, function name, file and line of the function, the answer taken, and the other reading. File and line are the line of the function's name in the built file.

| question | provision | function | file:line | answer taken | other reading |
|---|---|---|---|---|---|
| QA | s 2(2) "cannot ... except in so far as ... reasonableness" | `s 2(2) the person can exclude or restrict liability for other loss or damage resulting from negligence` | ucta-p1-avoidance.l4:88 | NOTHING when the term is shown reasonable (a lifted bar grants nothing); JUST FALSE when it is not shown reasonable (unreasonable, or nobody has shown it: s 11(5), fork F13) | JUST TRUE (the exception permits it); or NOTHING plus a yes/no twin (the twin `s 2(2) a requirement of reasonableness applies to the term or notice` also exists); for the unknown case, NOTHING (the reading before the fix round, fork F13) |
| QA | s 3(2) "cannot ... except in so far as" | `s 3(2) the other party can rely on the contract term as against that party` | ucta-p1-avoidance.l4:222 | NOTHING when shown reasonable; JUST FALSE when not shown reasonable (s 11(5), fork F13) | JUST TRUE when reasonable; NOTHING when unknown (the reading before the fix round) |
| QA | s 4(1) "cannot ... except in so far as" | `s 4(1) the person dealing as consumer can be made to indemnify the other person` | ucta-p1-avoidance.l4:275 | NOTHING when shown reasonable; JUST FALSE when not shown reasonable (s 11(5), fork F13) | JUST TRUE when reasonable; NOTHING when unknown (the reading before the fix round) |
| QA | s 7(4) "cannot ... except in so far as" | `s 7(4) the person can exclude or restrict liability for the right to transfer ownership or the assurance of quiet possession` | ucta-p1-goods.l4:516 | NOTHING when shown reasonable; JUST FALSE when not shown reasonable (s 11(5), fork F13) | JUST TRUE when reasonable; NOTHING when unknown (the reading before the fix round) |
| QA | s 6(3) "can be excluded ... but only in so far as" | `s 6(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability specified in subsection (2)` | ucta-p1-goods.l4:279 | JUST TRUE when shown reasonable, JUST FALSE when not shown reasonable (s 11(5), fork F13) (the text itself says "can" and closes with "only") | NOTHING when reasonable (as for the "cannot ... except" sites); the asymmetry between the two spellings is finding 4; NOTHING when unknown (the reading before the fix round) |
| QA | s 7(3) "can be excluded ... but only in so far as" | `s 7(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability in subsection (2)` | ucta-p1-goods.l4:403 | JUST TRUE when shown reasonable, JUST FALSE when not shown reasonable (s 11(5), fork F13) | NOTHING when reasonable; NOTHING when unknown (the reading before the fix round) |
| QA | s 30(2) "except in so far as ... section 5 of the Civil Law Act 1909" | `s 30(2) this Act applies in relation to the contract or the liability for loss or damage` | ucta-part3.l4:284 | NOTHING when the exception is met or unknown | JUST TRUE (the exception applies the Act) |
| QA | First Schedule para 2 "except in favour of a person dealing as consumer" | `sch 1 para 2 sections 2 to 4 and 7, subject to section 2(1), extend to the contract` | ucta-schedules.l4:104 | NOTHING in favour of a consumer (the bar is lifted and nothing is granted); JUST FALSE otherwise | JUST TRUE in favour of a consumer (the Schedule extends the sections to them) |
| QA | First Schedule para 3 "except in favour of a person dealing as consumer" | `sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft` | ucta-schedules.l4:132 | NOTHING in favour of a consumer; JUST FALSE otherwise | JUST TRUE in favour of a consumer |
| QA | First Schedule para 4 "except in favour of the employee" | `sch 1 para 4 section 2(1) and (2) extend to the contract` | ucta-schedules.l4:161 | NOTHING in favour of the employee; JUST FALSE otherwise | JUST TRUE in favour of the employee |
| QA | s 1(3) "(except where the contrary is stated in section 6(4))" | `s 1(2) and (3) whether an exception takes the section out of the case` | ucta-p1-introductory.l4:121 | for section 6 on a sale or hire-purchase, no exception takes it out although the liability is not business liability (s 6(4) says so positively); fork F5 | NOTHING (a lifted scope limit grants nothing), reaching "cannot be told" |
| QB | none: the Act has no bare "must"; ss 11(2) and 11(4) say "regard shall be had", encoded as "applies" questions, not compliance questions | `s 11(2) the matters to which regard is had in determining reasonableness under section 6 or 7` | ucta-p1-explanatory.l4:82 | JUST (the list) in the trigger, NOTHING outside it (s 11(2): scope limit with no "only"); JUST TRUE / JUST FALSE for s 11(4) (a failed "Where" on a positive requirement is JUST FALSE, ruling (b)) | a compliance function that asks whether the court did have regard |
| QC | "listed in" a Schedule: First Schedule para 1 lists contracts to which ss 2 to 4 do not extend | `sch 1 para 1 sections 2 to 4 extend to the contract` | ucta-schedules.l4:47 | a bare list: JUST FALSE for a contract the list names ("do not extend"), NOTHING for any other contract | the paragraph hands its definition to the list (JUST FALSE for a contract no paragraph describes); that would answer "ss 2 to 4 do not extend" for every unlisted contract, which para 1 does not say |
| QD | none: the Act imposes no duty of a named party, so there is no compliance function and no duty-arises companion | `-` | - | not applicable to any site in this range | - |
| QE | s 1(1)(b) "(but not any stricter duty)" | `s 1(1) the breach is negligence` | ucta-p1-introductory.l4:31 | JUST FALSE for a stricter duty (the parenthesis takes it out of a "means" definition) | NOTHING (a scope limit) |
| QE | s 11(3) "(not being a notice having contractual effect)" | `s 11(3) the notice satisfies the requirement of reasonableness` | ucta-p1-explanatory.l4:50 | NOTHING for a notice having contractual effect (the parenthesis limits what the requirement covers) | JUST FALSE for such a notice |
| QE | s 7(4) "(in a case to which subsection (3A) does not apply)" | `s 7(4) a requirement of reasonableness applies to the contract term` | ucta-p1-goods.l4:477 | NOTHING when (3A) applies | JUST FALSE |
| QF | a missing event in a ledger | `-` | - | not applicable: this encoding writes no events to the state ledger | - |

### Forks, with every reading and the text that licenses each

Ids F1 to F19 are those in the coverage table's `fork` column.

- **F1** the reasonableness exception once met, spelt "cannot ... except in so far as" (ss 2(2), 3(2), 4(1), 7(4)). Licence: s 2(2): "a person cannot so exclude or restrict his liability for negligence except in so far as the term or notice satisfies the requirement of reasonableness". Readings: (i) taken: NOTHING when the term is shown reasonable; JUST FALSE when it is not shown reasonable (unreasonable, or nobody has shown it: F13); (ii) JUST TRUE when reasonable; (iii) NOTHING plus a twin "the requirement applies" (the twin functions `... a requirement of reasonableness applies ...` are written for each site).
- **F2** the same exception spelt "can be excluded ... but only in so far as" (ss 6(3), 7(3)). Licence: s 6(3): "can be excluded or restricted by reference to a contract term, but only in so far as the term satisfies the requirement of reasonableness". Readings: (i) taken: JUST TRUE when shown reasonable, JUST FALSE when not shown reasonable (F13); (ii) NOTHING when reasonable, as for F1.
- **F3** "except in favour of a person dealing as consumer / the employee" (First Schedule paras 2, 3, 4). Licence: Sch 1 para 2: "sections 2 to 4 and 7 do not extend to any such contract except in favour of a person dealing as consumer". Readings: (i) taken: NOTHING when the exception is met; (ii) JUST TRUE (the sections extend in favour of a consumer or the employee). The reviewer of the fix round reads paragraphs 2(c) and 4 as (ii); checked, no change: it stays this encoding's judgment call (a lifted bar grants nothing, QA), and a case in favour of the consumer or the employee is not out of the case in the aggregator, so the section functions answer for it.
- **F4** s 30(2) "except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909". Licence: s 30(2). Readings: (i) taken: NOTHING when the exception is met or unknown; (ii) JUST TRUE.
- **F5** s 1(3) "(except where the contrary is stated in section 6(4))". Licence: s 6(4): the liabilities in section 6 "include those arising under any contract of sale of goods or hire-purchase agreement". Readings: (i) taken: no exception takes section 6 out of the case for a sale or hire-purchase although the liability is not business liability; (ii) a lifted scope limit grants nothing, so "cannot be told".
- **F6** a "where", "so far as" or a described subject that conditions a NEGATIVE statement or a limit (per site below). Licence: s 27(1): "Where the proper law of a contract is the law of Singapore only by choice of the parties ... sections 2 to 7 do not operate as part of the proper law". Readings: ruling of 2026-11-05 (b): a failed "where" answers JUST FALSE; (c): a scope limit with no "only", and a relative clause ("which ..."), answer NOTHING outside. How (b) is applied to a negative statement: the function in the text's own words (the provision's own statement, for example `s 27(1) sections 2 to 7 do not operate as part of the proper law`) answers JUST TRUE inside the "Where" and JUST FALSE outside it; its positive partner (`... operate ...`, `... can exclude ...`) keeps NOTHING outside, because (b) applied to the positive partner would say that sections 2 to 7 operate (or that liability can be excluded, or that agreement is of itself acceptance) for every case outside the "Where", a yes the text does not give. A "where" on a positive grant (ss 3(1), 7(1), 9(1), 11(4), 27(2)) and a "when" in a definition (s 5(2)(a)) are JUST FALSE when unmet, as ruled. Per-site list:
  - s 2(3), real "Where" ("Where a contract term or notice purports to exclude or restrict liability for negligence, a person's agreement to or awareness of it is not of itself to be taken as indicating his voluntary acceptance of any risk"): (b) applied. `s 2(3) the person's agreement to or awareness of the term or notice is not of itself to be taken as indicating voluntary acceptance of the risk` (ucta-p1-avoidance.l4:123) is JUST TRUE inside, JUST FALSE outside, JUST FALSE when a flat negative takes the section out (F15); tests on both sides. The positive `s 2(3) ... is of itself to be taken ...` (ucta-p1-avoidance.l4:104) stays JUST FALSE inside and NOTHING outside. Not in the reviewer's list of seven; found on re-reading every "where" in the text.
  - s 5(1), real "where" (limbs (a) and (b)): (b) applied. `s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee` (ucta-p1-goods.l4:135) is JUST TRUE inside, JUST FALSE when limb (a) or (b) fails, when s 5(3) disapplies the section, or when a flat negative takes the section out (F15), and NOTHING for the chapeau "In the case of goods of a type ordinarily supplied for private use or consumption" and for "any contract term or notice contained in or operating by reference to a guarantee" (a scope limit and a described subject, (c)). The positive `s 5(1) the person can exclude ...` (ucta-p1-goods.l4:94) keeps JUST FALSE inside and NOTHING outside.
  - s 9(2), real "Where" ("Where on a breach the contract is nevertheless affirmed by a party entitled to treat it as repudiated, this does not of itself exclude the requirement of reasonableness"): (b) applied. `s 9(2) affirming the contract does not of itself exclude the requirement of reasonableness in relation to the contract term` (ucta-p1-other.l4:59) is JUST TRUE inside and JUST FALSE outside. The positive `s 9(2) affirming the contract of itself excludes ...` (ucta-p1-other.l4:45) keeps JUST FALSE inside and NOTHING outside.
  - s 27(1), real "Where": (b) applied. `s 27(1) sections 2 to 7 do not operate as part of the proper law` (ucta-part3.l4:108) is JUST TRUE inside and JUST FALSE outside. Applying (b) to the positive `s 27(1) sections 2 to 7 operate as part of the proper law` (ucta-part3.l4:94) would make it JUST FALSE for every contract whose proper law is Singapore law for another reason, which says that sections 2 to 7 do not operate for ordinary Singapore-law contracts, and the text says no such thing; it keeps JUST FALSE inside and NOTHING outside.
  - s 3(2)(a), a "when" (delegated ruling (c): "when" counts as "where"): "(a) when himself in breach of contract, exclude or restrict any liability of his in respect of the breach" names the act the bar covers (excluding liability for the person's OWN breach), not a condition on a statement, so it is read as a scope limit and outside it the twin `s 3(2) a requirement of reasonableness applies to the contract term` answers NOTHING (ucta-p1-avoidance.l4:177). Other reading: the "when" is a "where", and the twin answers JUST FALSE when the person is not in breach. Kept; flagged here because the reviewer did not list it and the ruling could be read either way.
  - s 10, NOT a "where": "so far as those rights extend to the enforcement of another's liability which this Part prevents that other from excluding or restricting" is a measure (F11) and a relative clause ("which"), and "any contract term prejudicing or taking away rights of his which arise under ..." a described subject: (c), NOTHING outside. Checked, no change (ucta-p1-other.l4:78).
  - s 26(1) and s 26(2), NOT a "where": "such a contract as is described in subsection (3)" is a described subject, so a scope limit with no "only" (c): NOTHING for any other contract. The definition in subsections (3) and (4) is the part that answers JUST FALSE ("only if"). Checked, no change (ucta-part3.l4:65; ucta-part3.l4:78).
  - s 28(2), NOT a "where": "in such circumstances and to such extent as may be prescribed by order made by the Minister" is a limit that points outside the text, and section 28 "applies to a contract for carriage by sea of a passenger" (subsection (1)) is a scope limit: NOTHING outside (c). Checked, no change (ucta-part3.l4:172; see also F17).
  - s 29(1), NOT a "where": "any contractual provision which (a) ... or (b) ..." is a relative clause: NOTHING outside (c). Checked, no change (ucta-part3.l4:235).
- **F7** a notice having contractual effect, and the sections that speak only of "contract term" (ss 3(2), 4(1), 6, 7, 11(1)). Licence: s 11(1) "In relation to a contract term"; s 11(3) "In relation to a notice (not being a notice having contractual effect)". Readings: (i) taken: NOTHING for a notice having contractual effect, and NOTHING where ss 3, 4, 6, 7 are asked of a notice; (ii) treat a notice having contractual effect as a contract term; (iii) treat it as a notice for s 2 only.
- **F8** consumer status not known ("I am not sure"). Licence: s 12(1). Readings: (i) taken: work out the answer on both statuses and give it only if they agree (ss 1(2) and (3) reach, 6(2) and (3), 7(2) and (3)), else NOTHING; (ii) treat unknown as not a consumer; (iii) refuse to answer.
- **F9** First Schedule para 1 names "Sections 2 to 4" although the Schedule's title says "Scope of sections 2 to 4 and 7". Licence: Sch 1 para 1 "Sections 2 to 4 do not extend to"; s 1(2) "sections 2 to 4 and 7 is subject to the exceptions made by the First Schedule". Readings: (i) taken: para 1 does not take s 7 out of the case (only para 2 reaches s 7); (ii) para 1 also excludes s 7 (the title and s 1(2) say the Schedule's exceptions reach s 7).
- **F10** Second Schedule names "sections 6(3) and 7(3) and (4)"; s 11(2) says "section 6 or 7". Licence: Sch 2 opening words; s 11(2). Readings: (i) taken: both functions are written to their own words: `s 11(2) the matters ...` answers for section 6 or 7, and `sch 2 regard is to be had in particular to the guideline` only for ss 6(3), 7(3) and 7(4); (ii) read s 11(2) down to the Schedule's three subsections.
- **F11** "in so far as": reasonableness of part of a term. Licence: s 2(2) "in so far as the term or notice satisfies the requirement". Readings: (i) taken: the term (or the part the question concerns) is one unit and the court's judgment on it is the input; (ii) apportion: the term is effective in part.
- **F12** s 12(1)(c) for a contract not governed by the law of sale of goods, hire-purchase or s 7. Licence: s 12(1)(c): "in the case of a contract governed by the law of sale of goods or hire-purchase, or by section 7". Readings: (i) taken: limb (c) is required only for those contracts, and for any other kind (a) and (b) suffice; (ii) limb (c) is required of every contract, so that no one deals as consumer in a services contract.
- **F13** reasonableness nobody has shown: the burden of s 11(5) (the reviewer's scenarios 69, S2, S13). Licence: s 11(5): "It is for those claiming that a contract term or notice satisfies the requirement of reasonableness to show that it does". Readings: (i) taken: where the party who claims the term is reasonable has not shown it (the term is unreasonable, or nobody has shown either way), "the term satisfies the requirement of reasonableness" is not established for that party, so the bar of ss 2(2), 3(2), 4(1), 7(4) stands (JUST FALSE) and ss 6(3), 7(3) answer JUST FALSE; the seat's "has it been shown that the clause is reasonable?" treats "I am not sure" as not shown. Basis: the provision allocates the burden, and the delegated ruling of 2026-11-05 (b) treats "it is a defence ... to prove that X" the same way (X not proved: JUST FALSE for that provision's defence); shown reasonable keeps ruling QA (NOTHING at the "cannot ... except" sites, JUST TRUE at the "can be excluded ... only" sites). (ii) NOTHING when reasonableness is unknown (the reading before the fix round): the burden of proof is procedural, and the text says who must show, not what is concluded if nobody does. Not changed: `ss 11(1), 11(3) and 29(2) the term or notice satisfies the requirement of reasonableness` stays NOTHING when the court's judgment is unknown, because it asks what the court found, not who bears the burden; `s 11(5) the party must show ...` is unchanged.
- **F14** s 12(3): "no evidence the buyer acted in business" (the reviewer's 77). Licence: s 12(3): "Subject to this, it is for those claiming that a party does not deal as consumer to show that he does not". Readings: (i) taken: s 12(3) is encoded as the allocation of the burden only. The facts of s 12(1) are plain yes/no in both layers (`Dealing facts` are BOOLEAN; the seat asks "Did you make the contract in the course of a business?" as Yes/No), so "nobody has shown that the buyer acted in business" is not a state either layer can hold. The one "I am not sure" on consumer status (the seat's `consumer` answer) means "not known" and is handled as F8 (answer only if it is the same on both statuses); it is not turned into a presumption that the party is a consumer. (ii) presume consumer status when nobody has shown otherwise (the same step as F13): `consumer` unknown would become JUST TRUE for ss 4(1), 6 and 7, and F8 would change in every function that takes consumer status; this needs a "not shown" state in `Dealing facts` and a lawyer's decision. Not taken because the text says who must show, not what follows if nobody does.
- **F15** a flat negative takes a section out of the case (the reviewer's S14b). Licence: First Schedule para 1: "Sections 2 to 4 do not extend to" a contract of insurance and the other kinds named; s 1(3): sections 2 to 7 apply "only to business liability"; Part 3 (for example s 26(2): "not subject to any requirement of reasonableness under section 3 or 4"). Readings: (i) taken: the "requirement of reasonableness applies" twins of ss 2(2), 3(2), 4(1), 6(3), 7(3) and 7(4), and the own-words twins of F6 (ss 2(3), 5(1)), answer JUST FALSE, ahead of their scope limits (a flat negative counts as the text's no, ruling N2); the functions that ask whether the person CAN exclude, rely or be made to do something answer NOTHING when the section is out, because the Act then says nothing about whether they can (a JUST FALSE there would tell an insurer or an employer that it CANNOT exclude, the opposite of what the removal means). Where the removal rests on something the text does not settle (consumer status not known and the Schedule answers differently on either answer; Part 3 turning on the Minister's order or on section 5 of the Civil Law Act 1909) the reach is "cannot be told" and every function answers NOTHING. (ii) NOTHING in the twins as well (the reading before the fix round); (iii) JUST FALSE in the "can exclude" functions too: rejected for the reason given.
- **F16** the time of the reasonableness judgment in s 11(1) and s 11(3), and the purpose in section 3 of the Misrepresentation Act 1967 (the reviewer's gaps 59 to 62). Licence: s 11(1): "the requirement of reasonableness for the purposes of this Part and section 3 of the Misrepresentation Act 1967 is that the term shall have been a fair and reasonable one to be included having regard to the circumstances which were, or ought reasonably to have been, known to or in the contemplation of the parties when the contract was made"; s 11(3): "... all the circumstances obtaining when the liability arose or (but for the notice) would have arisen". Readings: (i) taken, checked, no change: the court's judgment is a plain input and its time is in the input's name ("... when the contract was made"; "... when the liability arose or (but for the notice) would have arisen"), repeated in the seat's `@desc`; no date is compared, because the text computes nothing from a date here. The purpose in section 3 of the Misrepresentation Act 1967 is not encoded (that Act is not among the sources): `s 11(1)` gives the test as the Act's definition for this Part and says nothing about the other purpose (finding 16). (ii) take two dates and compute the circumstances "known" at the first: not done; it would invent a judgment the text leaves to the court.
- **F17** who prescribes under s 28(2) (the reviewer's gap 104). Licence: s 28(2): "in such circumstances and to such extent as may be prescribed by order made by the Minister by reference to a term of the contract so prescribed". Readings: (i) taken, checked, no change: the order is an input (`the Minister's order prescribes this exclusion in these circumstances, to this extent, by this term`, a MAYBE BOOLEAN); "the Minister" is not defined in the sources, so no office is named and no function asks who prescribes; JUST FALSE ("not precluded") when the order prescribes it, NOTHING when it does not or is not known (points outside the text). (ii) a function returning the prescribing authority: not added, because a user asks whether an order prescribes the exclusion, not who the Minister is.
- **F18** s 5(2)(b) "in writing" (the reviewer's assertion 39). Licence: s 5(2)(b): "anything in writing is a guarantee if it contains or purports to contain some promise or assurance (however worded or presented) that defects will be made good ...". Readings: (i) taken, kept: "in writing" and the promise are both conditions of the "if" (`s 5(2)(b) the writing is a guarantee`: JUST TRUE if both, JUST FALSE if either fails; marginal reading (a)); (ii) "in writing" is the subject, not a condition: a document not in writing is not "anything in writing", so the question does not arise (NOTHING). The text does not point the other way, so no change.
- **F19** two things the text does not say: whether a void exclusion clause is an offence, and whether a term was incorporated into the contract at all (the reviewer's gaps 138 and 140). Licence: s 11(2): "this subsection does not prevent the court or arbitrator from holding, in accordance with any rule of law, that a term which purports to exclude or restrict any relevant liability is not a term of the contract"; the text contains no offence or penalty provision (checked with a search of the text for "offence", "crime" and "penalt": no hit). Readings: (i) taken, checked, no change: neither is encoded and no function is added. Incorporation is left to "any rule of law" (s 11(2) preserves the court's power to hold that a term is not a term of the contract, and `s 11(2) the subsection prevents ...` answers only that question); the encoding takes it for granted that the clause is a term or notice when it asks about ss 2 to 7. Whether a void exclusion clause is an offence is a question about another Act or the criminal law, which the text does not raise; a user would not plainly ask it of this Act. Any question about either would have to answer NOTHING (silent). (ii) a function "the term was incorporated" or "the clause is an offence": not added; it would invent an answer the text leaves open.

## Marginal readings for a lawyer

The rule of 2026-10-29 leaves two readings for a lawyer to decide: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Both are taken as the status quo. Every branch that rests on either is listed here, by file and line (the line of the branch's comment in the built file).

### Branches resting on reading (a): a failed condition is taken as the text's no

In each, the answer taken is `JUST FALSE`; the other reading is `NOTHING` (the text sets a condition for the positive statement and does not itself say what follows when the condition fails).

| file:line | function | the condition that failed |
|---|---|---|
| ucta-schedules.l4:245 | `sch 2 regard is to be had in particular to the guideline` | "which appear to be relevant" -- a matter that does not appear relevant is not one of those matters |
| ucta-p1-introductory.l4:52 | `s 1(3) the liability is business liability` | "business liability, that is liability for ..." -- a definition by "that is"; any other liability is not business liability |
| ucta-part3.l4:44 | `s 26(3) and (4) the contract is an international supply contract` | "that description of contract is one whose characteristics are the following: (a) either it is a contract of sale of goods or it is one under or in pursuance of which the |
| ucta-part3.l4:47 | `s 26(3) and (4) the contract is an international supply contract` | "(b) it is made by parties whose places of business (or, if they have none, habitual residences) are in the territories of different States" -- a definition by conditions |
| ucta-part3.l4:140 | `s 27(2) this Act has effect notwithstanding the term applying the law of a country outside Singapore` | the "where" fails -- neither (a) nor (b) is met (ruling of 2026-11-05: a failed "where" on a positive effect answers JUST FALSE) |
| ucta-part3.l4:264 | `s 29(2) the contract term is taken as satisfying the requirement of reasonableness` | the "if" is not met (marginal reading for a lawyer: a failed "if" is taken as the text's no for the deeming; the term may still satisfy the requirement under section 11) |
| ucta-part3.l4:112 | `s 27(1) sections 2 to 7 do not operate as part of the proper law` | the proper law is the law of Singapore for another reason (or is not Singapore law), so the subsection does not switch sections 2 to 7 off; it does not say they operate e |
| ucta-p1-explanatory.l4:123 | `s 11(4) regard is to be had in particular to the resources and insurance matters` | the "Where" is not met (ruling of 2026-11-05: a failed "where" on a positive requirement answers JUST FALSE) |
| ucta-p1-explanatory.l4:176 | `s 12(1) the party deals as consumer in relation to the other party` | "(a) he neither makes the contract in the course of a business nor holds himself out as doing so" |
| ucta-p1-explanatory.l4:179 | `s 12(1) the party deals as consumer in relation to the other party` | "(b) the other party does make the contract in the course of a business" |
| ucta-p1-explanatory.l4:190 | `s 12(1) the party deals as consumer in relation to the other party` | limb (c) is not met |
| ucta-p1-goods.l4:44 | `s 5(2)(a) the goods are in consumer use` | the goods are used exclusively for the purposes of a business |
| ucta-p1-goods.l4:60 | `s 5(2)(b) the writing is a guarantee` | not in writing, or no such promise or assurance |
| ucta-p1-goods.l4:150 | `s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee` | "where loss or damage (a) arises from the goods proving defective while in consumer use; and (b) results from the negligence of a person concerned in the manufacture or d |
| ucta-p1-goods.l4:325 | `s 7(1) subsections (2) to (4) apply` | the contract is a sale, hire-purchase or one under which no goods pass |
| ucta-p1-other.l4:30 | `s 9(1) the contract term may be found to satisfy the requirement of reasonableness and be given effect` | "Where for reliance upon it a contract term has to satisfy the requirement of reasonableness, it may be found to do so and be given effect accordingly" -- the term need n |
| ucta-p1-other.l4:63 | `s 9(2) affirming the contract does not of itself exclude the requirement of reasonableness in relation to the contract term` | there was no breach, or the contract was not affirmed by a party entitled to treat it as repudiated, so the subsection does not apply |
| ucta-p1-avoidance.l4:132 | `s 2(3) the person's agreement to or awareness of the term or notice is not of itself to be taken as indicating voluntary acceptance of the risk` | "Where a contract term or notice purports to exclude or restrict liability for negligence, a person's agreement to or awareness of it is not of itself to be taken as indi |
| ucta-p1-avoidance.l4:151 | `s 3(1) this section applies as between the contracting parties` | the "where" is not met |

### Branches resting on reading (b): a grant or bar limited by its own wording is not a no

In each, the answer taken is `NOTHING` (the case is outside what the wording covers, or the exception is met); the other reading is `JUST FALSE` (the text says no to a case outside its limit).
The branches for the reasonableness exception (F1, F2), the Schedule exceptions (F3) and the Civil Law Act exception (F4) are among them.

| file:line | function | the wording that limits |
|---|---|---|
| ucta-schedules.l4:59 | `sch 1 para 1 sections 2 to 4 extend to the contract` | para 1 says what sections 2 to 4 do not extend to; it does not say they extend to any other contract, and it does not mention section 7 |
| ucta-schedules.l4:109 | `sch 1 para 2 sections 2 to 4 and 7, subject to section 2(1), extend to the contract` | the bar is on "any such contract", that is a contract of marine salvage or towage, a charterparty or a contract for carriage of goods by ship or hovercraft |
| ucta-schedules.l4:114 | `sch 1 para 2 sections 2 to 4 and 7, subject to section 2(1), extend to the contract` | "except in favour of a person dealing as consumer" -- the exception is met, so the bar does not apply and the paragraph grants nothing (QA: a lifted bar grants nothing) |
| ucta-schedules.l4:135 | `sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft` | "Where goods are carried by ship or hovercraft in pursuance of a contract" -- the goods are not so carried; the paragraph says nothing about whether the sections extend ( |
| ucta-schedules.l4:138 | `sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft` | "a contract which either (a) specifies that as the means of carriage over part of the journey ...; or (b) makes no provision as to the means of carriage and does not excl |
| ucta-schedules.l4:141 | `sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft` | "the contract as it operates for and in relation to the carriage of the goods by that means" -- the term is outside that operation |
| ucta-schedules.l4:144 | `sch 1 para 3 sections 2(2), 3 and 4 extend to the contract as it operates for the carriage of the goods by ship or hovercraft` | "except in favour of a person dealing as consumer" -- the exception is met (QA: a lifted bar grants nothing) |
| ucta-schedules.l4:165 | `sch 1 para 4 section 2(1) and (2) extend to the contract` | "except in favour of the employee" -- the exception is met (QA: a lifted bar grants nothing) |
| ucta-schedules.l4:169 | `sch 1 para 4 section 2(1) and (2) extend to the contract` | para 4 is about "a contract of employment" |
| ucta-schedules.l4:240 | `sch 2 regard is to be had in particular to the guideline` | "for the purposes of sections 6(3) and 7(3) and (4)" -- a scope limit with no "only" |
| ucta-part3.l4:69 | `s 26(1) the limits imposed by this Act on excluding or restricting liability apply to liability under the contract` | subsection (1) speaks only of "such a contract as is described in subsection (3)"; for any other contract it says nothing (a scope limit with no "only") |
| ucta-part3.l4:82 | `s 26(2) the terms of the contract are subject to a requirement of reasonableness under section 3 or 4` | subsection (2) speaks only of "such a contract" |
| ucta-part3.l4:98 | `s 27(1) sections 2 to 7 operate as part of the proper law` | subsection (1) is a negative statement conditioned by "Where"; if the proper law is Singapore law for another reason it does not say that sections 2 to 7 operate (that wo |
| ucta-part3.l4:135 | `s 27(2) this Act has effect notwithstanding the term applying the law of a country outside Singapore` | subsection (2) speaks of "any contract term which applies or purports to apply the law of some country outside Singapore"; with no such term it says nothing |
| ucta-part3.l4:162 | `s 28(1) section 28 applies to the contract` | the section is about "a contract for carriage by sea of a passenger" (a scope limit with no "only") |
| ucta-part3.l4:174 | `s 28(2) this Act precludes the person from excluding or restricting liability for loss or damage` | section 28 applies to "a contract for carriage by sea of a passenger or of a passenger and his luggage" (subsection (1)) |
| ucta-part3.l4:179 | `s 28(2) this Act precludes the person from excluding or restricting liability for loss or damage` | the order does not prescribe this circumstance, extent and term, so the subsection does not lift the Act's limits |
| ucta-part3.l4:239 | `s 29(1) this Act removes or restricts the effect of, or prevents reliance upon, the contractual provision` | the subsection speaks only of a provision "which" is authorised or required by an enactment, or made to comply with an international agreement and not more restrictive th |
| ucta-part3.l4:286 | `s 30(2) this Act applies in relation to the contract or the liability for loss or damage` | "before 12 November 1993" -- both the contract and the loss fall on or after that day, and subsection (2) says nothing about them (a negative statement outside its period |
| ucta-part3.l4:289 | `s 30(2) this Act applies in relation to the contract or the liability for loss or damage` | "except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909" -- the exception is met, so the bar does not apply and the subsection grants noth |
| ucta-p1-explanatory.l4:36 | `s 11(1) the contract term satisfies the requirement of reasonableness` | "In relation to a contract term"; subsection (1) does not name a notice with contractual effect, and subsection (3) excludes it (see NOTES.md, fork Q-notice-with-contract |
| ucta-p1-explanatory.l4:38 | `s 11(1) the contract term satisfies the requirement of reasonableness` | "In relation to a contract term"; a notice without contractual effect is dealt with in subsection (3) |
| ucta-p1-explanatory.l4:52 | `s 11(3) the notice satisfies the requirement of reasonableness` | "In relation to a notice (not being a notice having contractual effect)"; this is a contract term |
| ucta-p1-explanatory.l4:54 | `s 11(3) the notice satisfies the requirement of reasonableness` | "(not being a notice having contractual effect)" |
| ucta-p1-explanatory.l4:86 | `s 11(2) the matters to which regard is had in determining reasonableness under section 6 or 7` | "for the purposes of section 6 or 7" -- a scope limit with no "only"; for sections 2, 3 and 4 the subsection is silent |
| ucta-p1-explanatory.l4:104 | `s 11(2) the subsection prevents the court or arbitrator from holding that the term is not a term of the contract` | the subsection speaks of "a term which purports to exclude or restrict any relevant liability" and a holding "in accordance with any rule of law" |
| ucta-p1-explanatory.l4:143 | `s 11(4) the matters to which regard is had where liability is restricted to a specified sum` | the "Where" of subsection (4) is not met; whether regard is had to these matters is then answered by `s 11(4) regard is to be had in particular to the resources and insur |
| ucta-p1-explanatory.l4:204 | `s 12(2) the buyer is regarded as dealing as consumer` | subsection (2) speaks only of "a sale by auction or by competitive tender"; for another sale it is silent |
| ucta-p1-explanatory.l4:237 | `s 12(3) the party must show that a party does not deal as consumer` | "Subject to this" -- subsection (2) governs a sale by auction or competitive tender, where the buyer is never a consumer, and subsection (3) says nothing about a burden t |
| ucta-p1-explanatory.l4:281 | `s 13(1) the person can use the exemption clause to avoid the liability` | "sections 2 and 5 to 7" -- sections 3 and 4 are not among them |
| ucta-p1-explanatory.l4:284 | `s 13(1) the person can use the exemption clause to avoid the liability` | subsection (1) speaks of an arbitration agreement only in subsection (2); this is not one of the varieties (a) to (c) or the exclusion of the obligation itself |
| ucta-p1-explanatory.l4:288 | `s 13(1) the person can use the exemption clause to avoid the liability` | "To the extent that this Part prevents the exclusion or restriction of any liability" -- this Part does not prevent it, so subsection (1) says nothing |
| ucta-p1-explanatory.l4:304 | `s 13(2) the agreement is treated under this Part as excluding or restricting liability` | subsection (2) speaks only of "an agreement in writing to submit present or future differences to arbitration" |
| ucta-p1-introductory.l4:65 | `s 1(4) it makes a difference for this Part` | subsection (4) speaks only of those two distinctions |
| ucta-p1-avoidance.l4:43 | `s 2(1) the person can exclude or restrict liability for death or personal injury resulting from negligence` | section 1(2) and (3) and the First Schedule take the section out of the case, or whether they do cannot be told |
| ucta-p1-avoidance.l4:46 | `s 2(1) the person can exclude or restrict liability for death or personal injury resulting from negligence` | subsection (1) speaks of "death or personal injury"; other loss or damage is subsection (2) |
| ucta-p1-avoidance.l4:49 | `s 2(1) the person can exclude or restrict liability for death or personal injury resulting from negligence` | subsection (1) speaks of liability "resulting from negligence" (s 1(1) defines it) |
| ucta-p1-avoidance.l4:68 | `s 2(2) a requirement of reasonableness applies to the term or notice` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-avoidance.l4:71 | `s 2(2) a requirement of reasonableness applies to the term or notice` | subsection (2) is "In the case of other loss or damage"; death or personal injury is subsection (1), which has no reasonableness exception |
| ucta-p1-avoidance.l4:74 | `s 2(2) a requirement of reasonableness applies to the term or notice` | subsection (2) speaks of liability "for negligence" |
| ucta-p1-avoidance.l4:93 | `s 2(2) the person can exclude or restrict liability for other loss or damage resulting from negligence` | the term or notice is shown to be reasonable, so the bar is lifted "in so far as" and the subsection grants nothing (ruling QA, by the text's spelling "cannot ... except" |
| ucta-p1-avoidance.l4:107 | `s 2(3) the person's agreement to or awareness of the term or notice is of itself to be taken as indicating voluntary acceptance of the risk` | section 1(2) and (3) and the First Schedule take the section out of the case, or whether they do cannot be told |
| ucta-p1-avoidance.l4:110 | `s 2(3) the person's agreement to or awareness of the term or notice is of itself to be taken as indicating voluntary acceptance of the risk` | "Where a contract term or notice purports to exclude or restrict liability for negligence" -- the subsection does not say that agreement or awareness IS acceptance of the |
| ucta-p1-avoidance.l4:129 | `s 2(3) the person's agreement to or awareness of the term or notice is not of itself to be taken as indicating voluntary acceptance of the risk` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told |
| ucta-p1-avoidance.l4:183 | `s 3(2) a requirement of reasonableness applies to the contract term` | subsection (2) operates "As against that party", the party subsection (1) describes |
| ucta-p1-avoidance.l4:186 | `s 3(2) a requirement of reasonableness applies to the contract term` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-avoidance.l4:189 | `s 3(2) a requirement of reasonableness applies to the contract term` | "by reference to any contract term"; a notice is not named (a notice having contractual effect is neither a contract term nor a notice not having contractual effect, a fo |
| ucta-p1-avoidance.l4:192 | `s 3(2) a requirement of reasonableness applies to the contract term` | subsection (2) names three cases, (a) exclusion of liability for the person's own breach, (b)(i) substantially different performance, (b)(ii) no performance |
| ucta-p1-avoidance.l4:195 | `s 3(2) a requirement of reasonableness applies to the contract term` | (a) speaks of the person "when himself in breach of contract" |
| ucta-p1-avoidance.l4:227 | `s 3(2) the other party can rely on the contract term as against that party` | the term is shown to be reasonable, so the bar is lifted "in so far as" and the subsection grants nothing (ruling QA, by the text's spelling "cannot ... except"); or the  |
| ucta-p1-avoidance.l4:249 | `s 4(1) a requirement of reasonableness applies to the contract term` | "A person dealing as consumer cannot ..."; section 12 says whether the person deals as consumer, and if it is not shown the subsection says nothing |
| ucta-p1-avoidance.l4:252 | `s 4(1) a requirement of reasonableness applies to the contract term` | "be made to indemnify another person ... in respect of liability that may be incurred by the other for negligence or breach of contract" |
| ucta-p1-avoidance.l4:255 | `s 4(1) a requirement of reasonableness applies to the contract term` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-avoidance.l4:258 | `s 4(1) a requirement of reasonableness applies to the contract term` | "by reference to any contract term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-avoidance.l4:280 | `s 4(1) the person dealing as consumer can be made to indemnify the other person` | the term is shown to be reasonable, so the bar is lifted "in so far as" and the subsection grants nothing (ruling QA, by the text's spelling "cannot ... except"); or the  |
| ucta-p1-avoidance.l4:296 | `s 4(2) section 4 applies to the liability` | (a) names two ways, direct and vicarious; any other way is not mentioned |
| ucta-p1-goods.l4:73 | `s 5(3) section 5 applies as between the parties` | subsection (3) disapplies the section only as between those parties |
| ucta-p1-goods.l4:97 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | section 1(2) and (3) take the section out of the case, or whether they do cannot be told |
| ucta-p1-goods.l4:100 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | subsection (3) says the section "does not apply as between the parties to a contract under or in pursuance of which possession or ownership of the goods passed" |
| ucta-p1-goods.l4:103 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | "In the case of goods of a type ordinarily supplied for private use or consumption"; whether they are is not shown |
| ucta-p1-goods.l4:106 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | limb (a), "while in consumer use" (subsection (2)(a)) |
| ucta-p1-goods.l4:109 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | limbs (a) "arises from the goods proving defective" and (b) "results from the negligence of a person concerned in the manufacture or distribution of the goods" |
| ucta-p1-goods.l4:112 | `s 5(1) the person can exclude or restrict liability for the loss or damage by a term or notice in a guarantee` | "any contract term or notice contained in or operating by reference to a guarantee of the goods" (subsection (2)(b)) |
| ucta-p1-goods.l4:141 | `s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee` | whether section 1(2) and (3) or Part 3 take the section out of the case cannot be told |
| ucta-p1-goods.l4:147 | `s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee` | "In the case of goods of a type ordinarily supplied for private use or consumption" is a scope limit with no "only" (ruling of 2026-11-05 (c)); whether the goods are of t |
| ucta-p1-goods.l4:156 | `s 5(1) liability for the loss or damage cannot be excluded or restricted by a term or notice in a guarantee` | "any contract term or notice contained in or operating by reference to a guarantee of the goods" describes the subject (subsection (2)(b)); not shown |
| ucta-p1-goods.l4:191 | `s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions` | section 1(2) and (3) take the section out of the case, or whether they do cannot be told |
| ucta-p1-goods.l4:194 | `s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions` | subsection (1) names section 12 of the Sale of Goods Act 1979 and section 6 of the Hire-Purchase Act 1969 |
| ucta-p1-goods.l4:197 | `s 6(1) the person can exclude or restrict liability for breach of the obligations arising from the title provisions` | "by reference to any contract term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:220 | `s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions` | section 1(2) and (3) take the section out of the case, or whether they do cannot be told |
| ucta-p1-goods.l4:223 | `s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions` | "As against a person dealing as consumer"; section 12 says whether the person deals as consumer |
| ucta-p1-goods.l4:226 | `s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions` | subsection (2) names sections 13, 14 and 15 of the Sale of Goods Act 1979 and sections 6A, 6B and 6C of the Hire-Purchase Act 1969 |
| ucta-p1-goods.l4:229 | `s 6(2) the person can exclude or restrict, as against a person dealing as consumer, liability for breach of the obligations arising from the quality provisions` | "by reference to any contract term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:252 | `s 6(3) a requirement of reasonableness applies to the contract term` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-goods.l4:255 | `s 6(3) a requirement of reasonableness applies to the contract term` | "As against a person dealing otherwise than as consumer"; section 12 says whether the person deals as consumer |
| ucta-p1-goods.l4:258 | `s 6(3) a requirement of reasonableness applies to the contract term` | "the liability specified in subsection (2)" |
| ucta-p1-goods.l4:261 | `s 6(3) a requirement of reasonableness applies to the contract term` | "by reference to a contract term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:282 | `s 6(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability specified in subsection (2)` | subsection (3) does not reach this case, or the section is taken out of the case (the twin `s 6(3) a requirement of reasonableness applies to the contract term` answers t |
| ucta-p1-goods.l4:342 | `s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness` | section 1(2) and (3) and the First Schedule take the section out of the case, or whether they do cannot be told |
| ucta-p1-goods.l4:345 | `s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness` | subsection (1), "Where the possession or ownership of goods passes under or in pursuance of a contract not governed by the law of sale of goods or hire-purchase" |
| ucta-p1-goods.l4:348 | `s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness` | "As against a person dealing as consumer"; section 12 says whether the person deals as consumer |
| ucta-p1-goods.l4:351 | `s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness` | subsection (2) names "the goods' correspondence with description or sample, or their quality or fitness for any particular purpose" |
| ucta-p1-goods.l4:354 | `s 7(2) the person can exclude or restrict, as against a person dealing as consumer, liability for the correspondence of the goods with description or sample, or their quality or fitness` | "by reference to any such term" (a contract term, subsection (1)); a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:375 | `s 7(3) a requirement of reasonableness applies to the contract term` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-goods.l4:378 | `s 7(3) a requirement of reasonableness applies to the contract term` | subsection (1) |
| ucta-p1-goods.l4:381 | `s 7(3) a requirement of reasonableness applies to the contract term` | "As against a person dealing otherwise than as consumer"; section 12 says whether the person deals as consumer |
| ucta-p1-goods.l4:384 | `s 7(3) a requirement of reasonableness applies to the contract term` | "that liability", the liability in subsection (2) |
| ucta-p1-goods.l4:387 | `s 7(3) a requirement of reasonableness applies to the contract term` | "by reference to such a term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:406 | `s 7(3) the person can exclude or restrict, as against a person dealing otherwise than as consumer, the liability in subsection (2)` | subsection (3) does not reach this case, or the section is taken out of the case (the twin `s 7(3) a requirement of reasonableness applies to the contract term` answers t |
| ucta-p1-goods.l4:448 | `s 7(3A) the person can exclude or restrict liability for breach of the obligations arising under section 2 of the Supply of Goods Act 1982` | section 1(2) and (3) and the First Schedule take the section out of the case, or whether they do cannot be told |
| ucta-p1-goods.l4:451 | `s 7(3A) the person can exclude or restrict liability for breach of the obligations arising under section 2 of the Supply of Goods Act 1982` | "any such term" refers to the terms of subsection (1) |
| ucta-p1-goods.l4:454 | `s 7(3A) the person can exclude or restrict liability for breach of the obligations arising under section 2 of the Supply of Goods Act 1982` | subsection (3A) names section 2 of the Supply of Goods Act 1982 |
| ucta-p1-goods.l4:457 | `s 7(3A) the person can exclude or restrict liability for breach of the obligations arising under section 2 of the Supply of Goods Act 1982` | "by reference to any such term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:483 | `s 7(4) a requirement of reasonableness applies to the contract term` | whether section 1(2) and (3), the First Schedule or Part 3 take the section out of the case cannot be told (whether the person protected deals as consumer is not known an |
| ucta-p1-goods.l4:486 | `s 7(4) a requirement of reasonableness applies to the contract term` | "any such term" refers to the terms of subsection (1) |
| ucta-p1-goods.l4:489 | `s 7(4) a requirement of reasonableness applies to the contract term` | subsection (4) names (a) the right to transfer ownership of the goods, or give possession, and (b) the assurance of quiet possession |
| ucta-p1-goods.l4:492 | `s 7(4) a requirement of reasonableness applies to the contract term` | "(in a case to which subsection (3A) does not apply)" |
| ucta-p1-goods.l4:495 | `s 7(4) a requirement of reasonableness applies to the contract term` | "by reference to any such term"; a notice is not named (a notice having contractual effect is a fork in NOTES.md) |
| ucta-p1-goods.l4:521 | `s 7(4) the person can exclude or restrict liability for the right to transfer ownership or the assurance of quiet possession` | the term is shown to be reasonable, so the bar is lifted "in so far as" and the subsection grants nothing (ruling QA, by the text's spelling "cannot ... except"); or the  |
| ucta-p1-other.l4:33 | `s 9(1) the contract term may be found to satisfy the requirement of reasonableness and be given effect` | subsection (1) speaks of a contract that "has been terminated either by breach or by a party electing to treat it as repudiated"; for a contract still in force it says no |
| ucta-p1-other.l4:49 | `s 9(2) affirming the contract of itself excludes the requirement of reasonableness in relation to the contract term` | subsection (2) speaks of a breach and of affirmation by a party entitled to treat the contract as repudiated; outside that "Where" it does not say that affirming DOES exc |
| ucta-p1-other.l4:81 | `s 10 the person is bound by the contract term` | "any contract term prejudicing or taking away rights of his which arise under, or in connection with the performance of, another contract" |
| ucta-p1-other.l4:84 | `s 10 the person is bound by the contract term` | "so far as those rights extend to the enforcement of another's liability" |
| ucta-p1-other.l4:89 | `s 10 the person is bound by the contract term` | this Part does not prevent the other from excluding or restricting the liability, or that is not known (the "so far as" limit); the section says nothing |

That is 104 branches in reading (b), and 19 in reading (a); flat negatives ("cannot", "do not", "is not bound") are not listed: they count as the text's no (ruling N2).

## What the text does not answer

Questions a reader may bring to this Act that the text leaves open; each is `NOTHING` if asked, and no function asks it (fork F19).

- Whether a void exclusion clause is an offence: the text has no offence or penalty provision.
- Whether a term was incorporated into the contract at all: s 11(2) leaves it to "any rule of law"; `s 11(2) the subsection prevents the court or arbitrator from holding that the term is not a term of the contract` is the only function that touches it.
- Who the Minister is, and what an order under s 28(2) says: outside the sources (fork F17).
- Whether the term is reasonable: the court's judgment, taken as a plain input (forks F13 and F16).

## What the text turns out to say

Numbered findings. A finding ends "Asserted." where a test or a seat case asserts it (the file is named).

1. Sections 2 to 7 reach only business liability (s 1(3)), and only section 6 is widened, to any contract of sale of goods or hire-purchase agreement (s 6(4)). A non-business liability under a sale is still caught by section 6 and is out of section 7 and section 5. Asserted (`ucta-tests-introductory.l4`, `ucta-cases-seat.l4`).
2. First Schedule para 1 says "Sections 2 to 4 do not extend to" insurance, land, intellectual property, companies and securities, although the Schedule's title and s 1(2) say "sections 2 to 4 and 7". The encoding follows para 1's own words, so para 1 does not take s 7 out of the case (only para 2 reaches s 7). This is fork F9. Asserted (`ucta-tests-introductory.l4`).
3. The Second Schedule names "sections 6(3) and 7(3) and (4)"; s 11(2) says "section 6 or 7", which also takes in ss 6(1), 6(2), 7(2) and 7(3A), none of which has a reasonableness test. Each function is written to its own words (fork F10). Asserted (`ucta-tests-schedules.l4`, `ucta-tests-explanatory.l4`).
4. The reasonableness exception is spelt two ways. "Cannot ... except in so far as the term satisfies the requirement" (ss 2(2), 3(2), 4(1), 7(4)) answers NOTHING when the term is shown reasonable and JUST FALSE when it is not shown reasonable; "can be excluded ... but only in so far as" (ss 6(3), 7(3)) answers JUST TRUE when it is shown reasonable and JUST FALSE when it is not (s 11(5), fork F13). The legal effect is the same, so a caller comparing the two sets of sites sees an asymmetry that comes from the drafting, not from the law. Asserted (`ucta-tests-avoidance.l4`, `ucta-tests-goods.l4`).
5. A notice having contractual effect is neither "a contract term" (s 11(1)) nor "a notice (not being a notice having contractual effect)" (s 11(3)), so the Act states no reasonableness test for it: both answer NOTHING (fork F7). Asserted (`ucta-tests-explanatory.l4`).
6. Sections 3, 4, 6 and 7 speak of "contract term" only; sections 2 and 5 name "contract term or notice". A notice answers NOTHING under ss 3, 4, 6 and 7. Asserted (`ucta-tests-avoidance.l4`, `ucta-tests-goods.l4`).
7. The last limb of s 13(1) says "sections 2 and 5 to 7" also prevent excluding the relevant obligation or duty itself; sections 3 and 4 are not named, so s 13 does not by itself stop a term that excludes the duty under those sections. Asserted (`ucta-tests-explanatory.l4`, `ucta-cases-seat.l4`).
8. Section 5(3) disapplies section 5 between the parties to a contract under which the goods passed, so section 5 matters where the person protected and the person bound are not the parties to that contract. Asserted (`ucta-tests-goods.l4`).
9. An international supply contract (s 26(3)) must be a contract of sale or one under which possession or ownership of goods passes, so a contract of services is never one. A hire-purchase agreement is counted because possession passes. Asserted (`ucta-tests-part3.l4`).
10. Section 30(2) turns on two dates, the contract's and the loss's, each tested against "before 12 November 1993"; a contract made on 12 November 1993 is not before that day. Asserted (`ucta-tests-part3.l4`).
11. Section 12(1)(c) (goods of a type ordinarily supplied for private use or consumption) applies only to a contract governed by the law of sale of goods or hire-purchase or by section 7 (fork F12). Asserted (`ucta-tests-explanatory.l4`).
12. Section 3(1) is the gate to s 3(2): a contracting party who neither deals as consumer nor on the other's written standard terms is outside section 3 (JUST FALSE). Asserted (`ucta-tests-avoidance.l4`).
13. Section 10 turns on whether Part 1 prevents the other person from excluding the liability, which is the answer to a question under ss 2 to 7; the seat asks it as an input and the questions on ss 2 to 7 give it. Asserted (`ucta-cases-seat.l4`).
14. Section 4(2) names two ways the liability can be incurred (directly or vicariously); to whom it is owed (the consumer or someone else) never changes the answer. Asserted (`ucta-tests-avoidance.l4`).
15. Section 27(2)(b) turns on the essential steps for making the contract having been taken in Singapore "whether by him or by others on his behalf"; the seat's question says so (the wording of the question is not asserted; limb (b) as a whole is, in `ucta-tests-part3.l4` and `ucta-cases-seat.l4`).
16. Section 11(1) gives the reasonableness test "for the purposes of this Part and section 3 of the Misrepresentation Act 1967". That Act is not among the sources, so the encoding gives the test for this Part only.
17. A flat negative that takes a section out of the case (the First Schedule's "do not extend to", section 1(3)'s "only", a Part 3 provision) is the text's own no for the question "does a requirement of reasonableness apply under this section?": an insurance policy's no-performance term is not subject to a requirement of reasonableness under section 3 (First Schedule para 1(a)). It is not an answer to "can the person exclude or rely?", which stays NOTHING (fork F15). Asserted (`ucta-tests-avoidance.l4`, `ucta-tests-goods.l4`, `ucta-cases-seat.l4`).
18. Section 11(5) decides what an unproved reasonableness means for the party who claims it: the bar stands (fork F13). The same sentence does not decide what "I am not sure" means for the court's own finding (s 11(1), (3), 29(2)), which stays NOTHING. Asserted (`ucta-tests-avoidance.l4`, `ucta-tests-goods.l4`, `ucta-cases-seat.l4`).
19. Where a "Where" conditions a negative statement (ss 2(3), 5(1), 9(2), 27(1)) the text's own sentence has a yes and a no, and the no is the "Where" failing (fork F6); the positive question the text does not ask ("can the person exclude?", "do sections 2 to 7 operate?") stays NOTHING outside the "Where". Asserted (`ucta-tests-avoidance.l4`, `ucta-tests-goods.l4`, `ucta-tests-other.l4`, `ucta-tests-part3.l4`, `ucta-cases-seat.l4`).
20. The Arrangement of Sections for Part 3 (lines 61 to 73) is garbled by the converter that made the text file; it is an index, and the sections themselves (lines 423 to 535) are intact.

## What the main binary does not accept

Found while writing this encoding on build 1.6.109 (the same files read the same on 1.6.108). I did not use `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`, and I did not test whether they are accepted.

- `JUST` inside an infix mixfix call needs brackets on both sides: `JUST TRUE `and also` JUST TRUE` reads as `JUST` applied to four arguments; write `((JUST TRUE) `and also` (JUST TRUE))`.
- A multi-line `IF NOT (a OR b)` with `THEN` on the next line, and an `ELSE IF ... THEN` chain at the same column, give "incorrect indentation"; write a `BRANCH` with `IF ... THEN ... OTHERWISE` arms, strictly to the right of `BRANCH`, and put shared tests in a `WHERE`.
- `length` is not defined; use `count`.
- A parameter written as an identifier followed by a backticked label (`relied `what is relied on` IS A ...`) is a parse error ("unexpected IS"); a parameter is one name.
- A function application cannot be followed directly by a genitive: `` `f` x's `y` `` is "unexpected 's"; write `` `f` (x's `y`) ``.
- A `LIST ...` given as a positional argument of `OF` swallows the arguments after it; `` `Definition entry` OF a, b, LIST "x", "y", "" `` is "expects 5 arguments but applying 4". Bracket it: `(LIST "x", "y")`.
- `l4 run` with a relative path from another directory gives "openFile: does not exist"; run it from the file's folder or give an absolute path.
- Names with parentheses inside backticks (for example `` `s 2(2) the person can exclude ...` ``) are accepted by both main builds.

## What check.sh prints

Both binaries, as `--version` prints them:

```
1.6.109 (main, 4c887e0, 2026-11-04)
1.6.108 (main, 2ae7c9b, 2026-11-02)
```

`L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` in this folder, final run:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ucta-cases-seat.l4                             0       159       0        0         0 |      0       159       0        0  same
ucta-fixtures.l4                               0         0       0        0         0 |      0         0       0        0  same
ucta-logic.l4                                  0        22       0        0         0 |      0        22       0        0  same
ucta-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
ucta-p1-avoidance.l4                           0         0       0        0         0 |      0         0       0        0  same
ucta-p1-explanatory.l4                         0         0       0        0         0 |      0         0       0        0  same
ucta-p1-goods.l4                               0         0       0        0         0 |      0         0       0        0  same
ucta-p1-introductory.l4                        0         0       0        0         0 |      0         0       0        0  same
ucta-p1-other.l4                               0         0       0        0         0 |      0         0       0        0  same
ucta-part3.l4                                  0         0       0        0         0 |      0         0       0        0  same
ucta-schedules.l4                              0         0       0        0         0 |      0         0       0        0  same
ucta-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ucta-tests-avoidance.l4                        0        98       0        0         0 |      0        98       0        0  same
ucta-tests-explanatory.l4                      0       109       0        0         0 |      0       109       0        0  same
ucta-tests-goods.l4                            0       132       0        0         0 |      0       132       0        0  same
ucta-tests-introductory.l4                     0       130       0        0         0 |      0       130       0        0  same
ucta-tests-other.l4                            0        16       0        0         0 |      0        16       0        0  same
ucta-tests-part3.l4                            0        67       0        0         0 |      0        67       0        0  same
ucta-tests-schedules.l4                        0        42       0        0         0 |      0        42       0        0  same
TOTAL (19 modules)                             0       775       0        0           |      0       775       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs UCTA1977.txt ucta-*.l4`, final run:

```
srcrefs check: 496 src: lines, 77 runs, 79 locators, 0 problems
```

There is no earlier run: the folder held only the supplied `check.sh`, `fetch-main-l4.sh` and `srcrefs.py`, so there are no baseline numbers it replaced.

## Dependencies

Nothing copied; `"dependencies": []` in `encoding.json`. The Interpretation Act modules staged for this text are not needed: no period is counted (s 30(2) compares two dates with `Date 12 11 1993`).
Other Acts the text depends on are not among the sources, so each is a named input citing its section, to fill when those Acts are encoded: the Sale of Goods Act 1979 (ss 12 to 15 as the obligations in s 6; "goods" in s 14), the Hire-Purchase Act 1969 (ss 6, 6A, 6B, 6C; "hire-purchase agreement" in s 14), the Supply of Goods Act 1982 s 2 (s 7(3A)), the Misrepresentation Act 1967 s 3 (s 11(1), not encoded), the Civil Law Act 1909 s 5 (s 30(2)), and the Minister's order under s 28(2).

## Unstable dialect

I looked at time (s 30(2) compares two dates and counts no period), versions (the `[44/96]` markers at lines 269 and 283 and the Legislative History at lines 637 to 665 record a 1996 amendment already in the text, and no earlier wording is to be encoded) and workarounds (the syntax limits above are not shapes that the unstable dialect would express better) and found none worth a second encoding.

## What would need doing before this encoding is worth relying on

- A lawyer should read it against the official text; the source here is a converter's plain-text rendering.
- A lawyer should decide the readings in the fork register, first F1 and F2 (the reasonableness exception and its two spellings), F13 (unproved reasonableness is the bar's case), F15 (a flat negative takes a section out: JUST FALSE in the twins, NOTHING in the "can exclude" functions), F6 (a "where" on a negative), F7 (a notice with contractual effect), F9 and F10 (the two Schedule mismatches), and the marginal readings.
- The Acts and the Minister's order listed under Dependencies should be encoded or supplied, and the inputs that stand for them replaced.
- Every reasonableness input (ss 11(1), 11(3)), "appears to the court" (s 27(2)(a)) and "which appear to be relevant" (Second Schedule) is the court's judgment, taken as a plain input; none is guessed.
- The seat asks up to 15 facts for the Part 3 question and 11 for the scope question; a form designer should decide whether to show them step by step.
- No regulative rule exists: the Act names no duty-bearer and no deadline. The burdens of proof in ss 11(5) and 12(3) are decision functions, not obligations.

## Files

See "What is encoded, and what is not". Quote lines (`-- src:N-M | text`) were expanded from `UCTA1977.txt` by a build script that read the file and is no longer in the deposit; `srcrefs.py` re-checks them.
`coverage.py` and `coverage-rows.tsv` build and check the coverage table (`python3 -I coverage.py UCTA1977.txt coverage-rows.tsv --md`).
