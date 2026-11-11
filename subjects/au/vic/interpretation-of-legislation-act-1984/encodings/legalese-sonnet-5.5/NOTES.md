# Notes: Interpretation of Legislation Act 1984 (Victoria), whole, in L4

Status: draft.
No domain expert has read this encoding against the text.
Every number below was produced by `check.sh` or by a script that reads only the text file, and is the state of the folder when this file was written.

## Source text

The text is `registers/source-bundle/interpretation-of-legislation-act-1984.txt`.
It is a plain-text rendering made by a converter script from the Word file the Victorian Legislation website publishes; it is not the official text and not an authorised version.
Its header says so, and says that only the authorised version published on that website is admissible as evidence under s 64.
The edition is Version No. 134, incorporating amendments as at 1 May 2026.
Nothing in this encoding claims to have been checked against the official text.
The terms the quoted text carries are in the subject folder's `SOURCE-LICENSE.md`, and this encoding's `SOURCE-LICENSE.md` points at that file.

## Target

The target is `main`.
The writing binary is the stable build `1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
`check.sh` also runs every module with the main build `1.6.110 (main, e51181d, 2026-11-11)`, and its output is under "What check.sh prints" below.
`JL4_LIBRARY_PATH` is unset for every run, so the standard library is the one compiled into each binary.

## Seat

The seat is a person with a time limit to meet under a Victorian Act or a statutory rule: someone who has been told "within 30 days", "within three years" or "by the day the Act comes into operation", and asks on which day the period really ends, whether the day they count from counts, what happens if the last day is a weekend or a public holiday, when the Act or rule they rely on took effect or stops having effect, and how a posted document is treated.
This Act is chosen as the seat's foundation because every other Victorian Act and statutory rule leaves these counting and reading rules to it, so a question form built on any of them needs the answers here.
The questions are in `vic-seat.l4`, with worked cases in `vic-cases-seat.l4`.
No question is asked from the position of an official.
Provisions that address an official (for example the Minister's duties in ss 38O and 38P, or the Chief Parliamentary Counsel's power in s 62) are encoded in layer 1 for what they decide, and appear in layer 2 only where they change what the person can do or must be given.

The fourteen exported questions are:

1. On which day does my period end, counting from the day I start (s 44(1), (6))?
2. Does the day I count from count in my period (s 44(1), (2))?
3. By which day may I do the thing if my last day is a Saturday, a Sunday or a public holiday (s 44(3), (4))?
4. By which day must I do the thing, counting my period from the day I start and allowing for weekends and public holidays (s 44)?
5. At which moment does the Act or provision I rely on come into operation (s 11)?
6. On which day does an Act that says nothing about its commencement come into operation (s 10A(3), (4))?
7. Until which moment does a temporary Act, provision or rule stay in operation (ss 12, 25)?
8. On which day is a document I posted taken to have been served on the person (s 49)?
9. Does the heading, note or other item printed with my Act form part of the Act (s 36)?
10. Is the decision about me ineffective only because the official was irregularly appointed (s 42C(1))?
11. Does the official have a choice whether to use the power my Act gives them (s 45(1))?
12. Must the official use the power my Act gives them (s 45(2))?
13. Must my matter be heard only by the Magistrates' Court (s 52)?
14. Is the form I used good enough even though it is not the prescribed form word for word (s 53)?

Each question takes plain inputs, one for each fact the person can state.
Public holidays are supplied by the caller as a list of days, because s 44(4)(b) refers to days appointed under the Public Holidays Act 1993, which is not among the sources.

## Folder layout

Layer 1 (the law, section by section, each rule carrying `@ref` locators into the text):

| module | what it holds | its tests |
| --- | --- | --- |
| `vic-nouns.l4` | the shared types | none of its own |
| `vic-interpretation-time.l4` | the time rules (ss 11, 12, 24, 25, 44, 49 and the helpers for s 10A(3) and (4) and s 55(2)) and every date the text states (ss 2, 9(2), 10(3), 21, 36, 38AA(2), 38EA(2), 55(2)(a), 64B(1)); self-contained: imports only the prelude | `vic-tests-time.l4` (134) |
| `vic-part1-preliminary.l4` | Part I, ss 4 and 5 (s 1 is inert; s 2 is in the time module) | `vic-tests-part1-2.l4` (180, shared with Part II) |
| `vic-part2-acts-a.l4`, `vic-part2-acts-b.l4` | Part II: ss 6 to 10A and 13; ss 14 to 21A | `vic-tests-part1-2.l4` |
| `vic-part3-subordinate.l4` | Part III: ss 22, 23 and 26 to 34 | `vic-tests-part3.l4` (154) |
| `vic-part4-a-aids.l4` | Part IV, ss 35 to 39B (aids to construction, ss 38M to 38P) | `vic-tests-part4-a.l4` (131) |
| `vic-part4-b-powers.l4` | Part IV, ss 40 to 43 (powers, appointments, delegation) | `vic-tests-part4-b.l4` (98) |
| `vic-part4-c-general.l4` | Part IV, ss 45 to 58 (general rules) | `vic-tests-part4-c.l4` (143) |
| `vic-part5-6-schedule1.l4` | ss 61 to 64B and Schedule 1 | `vic-tests-part5-6.l4` (64) |
| `vic-definitions.l4` | 135 definition rows: the defined terms of ss 3, 38 to 38E, 60 and 64B(1) | `vic-tests-definitions.l4` (409), `vic-tests-definitions-cases.l4` (23) |
| `vic-provisions.l4` | the provision index | tested through `vic-tests-xrefs.l4` |
| `vic-xrefs.l4` | the cross-reference rows | `vic-tests-xrefs.l4` (212) |

Layer 2 (the seat): `vic-seat.l4` and `vic-cases-seat.l4` (60 assertions).
The files `BRIEF.md`, `check.sh`, `fetch-main-l4.sh` and `srcrefs.py` were given and are unchanged.

`vic-provisions.l4` and `vic-xrefs.l4` are generated by a script that reads only the text file.
The other modules were written from templates by a script that copies the quoted source lines mechanically, so that `srcrefs.py` can check every quotation against the text.

## What is encoded and what is not

Every provision of the text has one row in the coverage table below: 1000 rows.
The encoded rules cover the whole of Parts I to VI and Schedule 1 as printed.
What is not encoded as a computed answer:

- Periods of weeks, and periods expressed with "after" or "before" a day: the text has no rule for them, and the functions return NOTHING (fork F2).
- A period of months or years whose two readings give different days: NOTHING (fork F1).
- Public holidays, the hours standard time is ahead of Coordinated Universal Time, the commencement of other Acts, and every other fact the text takes from another instrument: asked as inputs.
- Machinery that affects no one now (the short title, the Act's own amendments of other Acts, the saving in s 41(4), the transitional provision in s 59, the regulation-making power in s 65, the Minister's power to make guidelines in s 38O(1)): inert, reason 2.

## Jural relations

The kinds are Hohfeld's: duty and claim, privilege and no-claim, power and liability, immunity and disability.
Where the text names no holder of the correlative position, the table says so.

| provision | holder | correlative | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 38M(1), (2) | a person required to publish a notice in a print newspaper | the person entitled to the publication under the requiring Act (not named) | privilege / no-claim: publication on an approved site, in a prescribed manner or on a prescribed platform meets the requirement | `s38M(1) the requirement to publish in a print newspaper is taken by this subsection to have been met` |
| s 38N | the Minister | those who publish notices (not named) | power / liability: declaring an Internet site an approved alternative publication site | `s38N the Internet site is an approved alternative publication Internet site` |
| s 38O(2) | the Minister | the public (no holder named) | duty / claim: guidelines published in the Government Gazette and on an approved site | `s38O(2)(a) the guidelines have been published as the subsection requires` |
| s 38P | a Department, public statutory authority or prescribed entity responsible for publishing a notice | no holder named | duty / claim: to have regard to the guidelines | `s38P the entity has complied with the duty to have regard to the guidelines` |
| s 40(b) | the person for the time being holding, acting in or performing the duties of an office | those subject to the power or duty | power and duty | `s40(b) the person is the one by whom the power may be exercised and the duty shall be performed` |
| s 41(1) | the person with power to appoint to an office | the person appointed or acting | power / liability: to appoint to act, to remove, to suspend | `s41(1) the power to appoint includes the power` |
| s 41(2) | the person appointed to act | those affected by the acts | power / liability: the powers and functions of the holder | `s41(2) the incident follows from the appointment` |
| s 41AA | the acting appointee, and the appointer | each other | power / liability: terms and conditions, termination, continued acting | `s41AA the acting appointment has the incident` |
| s 42(1) | a person whose power depends on that person's opinion, belief or state of mind | the person affected | power / liability: a delegate acts on the delegate's own opinion | `s42(1) the delegate may act upon the delegate's own opinion, belief or state of mind` |
| s 42A | the person or body with a power to delegate | the delegate | power / liability: to delegate, with conditions or limitations | `s42A(1) the proposition about the delegation holds` |
| s 42C | a person appointed, or acting, and a delegate | anyone who would treat what was done as ineffective | immunity / disability: not ineffective only because of an irregularity in the making of the appointment or delegation | `s42C(1)`, `s42C(2)` |
| s 44(3) | the person with a time limited for doing an act or thing | the person who would receive the act earlier | privilege / no-claim: to do it on the next day that is not a holiday | `s44(3) day to which a time limited for doing an act or thing extends` |
| s 45(1) | the holder of a power conferred by "may" | no holder named | privilege / no-claim: to exercise it, or not, at discretion | `s45(1) the power may be exercised, or not, at discretion` |
| s 45(2) | the holder of a power conferred by "shall" | no holder named | duty / claim: the power must be exercised | `s45(2) the power must be exercised` |
| s 49 | the person who posts a document | the person on whom it is to be served | power / liability: service is deemed effected | `s49 service by post is deemed effected` |
| s 50 | the authority with power to make rules of court | those who use the court or tribunal | power / liability: to make rules or orders | `s50 the authority may make the rule or order` |
| s 51(1) | an offender under two or more laws | the prosecuting authority | liability to be prosecuted under any or all; immunity from being punished more than once | `s51(1) the offender is liable to be prosecuted under any or all of those laws`, `s51(1) the offender is liable to be punished more than once for the same act or omission` |
| s 53 | a person who uses a form to the like effect of the prescribed form | the person who would reject it | privilege / no-claim: the form is sufficient in law | `s53 the form used is sufficient in law` |
| s 54(2A) to (2C) | the party producing a copy printed by a government printer | the other party and the court | power / liability: admissibility on mere production | `s54(2A)`, `s54(2B)`, `s54(2C)` |
| s 57(4) | the courts of Victoria | persons in the offshore area | power / liability: jurisdiction in matters arising under the laws applied | `s57(4) the courts of Victoria have jurisdiction in the matter` |
| s 62(1) | the Chief Parliamentary Counsel | the public (no holder named) | power / liability: to authorise a version | `s62(1) the Chief Parliamentary Counsel may authorise the version` |
| s 64(1) | the party producing an authorised version | the other party and the court | power / liability: admissibility on mere production | `s64(1) the document is admissible on its mere production` |
| s 64A | a non-citizen | the appointing authority | immunity / disability: the status does not of itself affect eligibility or disqualify | `s64A the fact that the person is a non-citizen of itself affects eligibility ...` |
| s 64B(2) to (4), (6) | a person holding a purported appointment, and those who acted in reliance on it | anyone who would treat what was done as ineffective | immunity / disability | `s64B(2)`, `s64B(3)`, `s64B(4)`, `s64B(6)` |
| every other provision | none | none | none: definitions, counting rules, rules of reading, rules about what a reference means, statements of when a provision operates | the other rules in the modules |

## Coverage table

One row for each unit of the text: Front matter, Part, section, subsection, paragraph, defined term, Schedule, clause, table row, note, blank marker and endnote.
The table is produced by a script that reads the text, a list of the units, and the `@ref` locators in the rule modules.
A unit is `encoded` when a line of its own text lies inside a `src:` range of a rule; the "Where" column names the rule.
A unit that is only a heading takes `inert (1)`: not operative.
`inert (2)` is machinery.
`inert (3)` (text shown repealed or blank) is not used: the rows of that kind are under their own disposition, `repealed or blank in this text`.
A row marked `fork` points at the fork register below.

Totals: 1000 rows; 726 encoded; 236 inert (205 not operative, 31 machinery); 17 repealed or blank in this text; 21 fork.
Every non-blank line of the text falls inside at least one row.
No row is unassigned.

| Row | Kind | Lines | Text (opening words) | Disposition | Where |
| --- | --- | --- | --- | --- | --- |
| Front notice | front | 1-8 | Interpretation of Legislation Act 1984 (Victoria) Act No. 10096/1984 - | inert (1) | title, long title, notice or cover: not operative |
| Cover | front | 9-19 | ====================================================================== | inert (1) | title, long title, notice or cover: not operative |
| Long title | front | 20 | An Act to make fresh provision with respect to the construction and op | inert (1) | title, long title, notice or cover: not operative |
| Enacting words | front | 21 | BE IT ENACTED by the Queen's Most Excellent Majesty by and with the ad | inert (1) | title, long title, notice or cover: not operative |
| Part I | part | 23 | Part I—Preliminary | inert (1) | heading |
| s 1 | section | 25-26 | 1 Short title This Act may be cited as the Interpretation of Legislati | inert (2) | short title: machinery (the Act's own short title) |
| s 2 | section | 28-29 | 2 Commencement This Act shall come into operation on 1 July 1984. | encoded | s2 day the Act came into operation |
| s 3 | section | 31-32 | 3 Definitions In this Act, unless inconsistent with the context or sub | encoded | meaning of a term defined in a section |
| s 3 def "amended" | def | 33 | amended, in relation to a subordinate instrument, includes altered or  | encoded | s3 definition 001 of amended |
| s 3 def "made" | def | 34 | made, in relation to a subordinate instrument, includes issued or gran | encoded | s3 definition 002 of made |
| s 3 def "repealed" | def | 35 | repealed, in relation to a subordinate instrument, includes revoked or | encoded | s3 definition 003 of repealed |
| s 3 blank | blank | 36-37 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 3 def. of statutory rule substituted by No. 104/1994 s. 35(Sch. 2 item 3.1), repealed by No. 61) |
| s 3 blank#2 | blank | 38-39 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 3 def. of subordinate instrument repealed by No. 61/2004 s. 6(2).]) |
| s 4 | section | 41 | 4 Application, construction and repeal provisions | inert (1) | heading; the provisions of the section have their own rows |
| s 4(1) | item | 42 | (1) The provisions of this Act— | encoded | opening words of the paragraphs below, cited with them: s4(1)(a) the provisions of this Act extend and apply to the enactment; s4(1)(b) the provisions of this Act app |
| s 4(1)(a) | item | 43 | (a) unless a contrary intention appears in this Act or in the Act or s | encoded | s4(1)(a) the provisions of this Act extend and apply to the enactment |
| s 4(1)(b) | item | 44 | (b) apply to the interpretation of this Act. | encoded | s4(1)(b) the provisions of this Act apply to the interpretation of this Act |
| s 4(2) | item | 45 | (2) Nothing in this Act excludes the application to an Act or subordin | encoded | s4(2) this Act leaves the rule of construction applying |
| s 4(3) | item | 46 | (3) The provisions of this Act which are expressed to apply to Acts pa | encoded | s4(3) the provision affects the construction of the enactment |
| s 4(4) | item | 47 | (4) The Acts mentioned in the Schedule to the extent to which they are | inert (2) | machinery: amends or repeals the Acts mentioned in a Schedule; it affects no one now |
| s 5 | section | 49-50 | 5 Act to bind Crown This Act binds the Crown, not only in right of the | encoded | s5 this Act binds the Crown |
| Part II | part | 52 | Part II—Provisions applicable to Acts | inert (1) | heading |
| s 6 | section | 54 | 6 Construction of Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 6(1) | item | 55 | (1) Every Act shall be construed as operating to the full extent of, b | encoded | s6(1) how a provision of an Act is construed against the limit of the legislative power of Victoria |
| s 6(2) | item | 56 | (2) The provisions of this section are in addition to, and not in dero | encoded | s6(2) s 6 takes the place of a provision of the Act on its construction or extent of operation |
| s 7 | section | 58-59 | 7 Sections to be substantive enactments Every section of an Act has ef | encoded | s7 a section of an Act has effect as a substantive enactment |
| s 8 | section | 61-62 | 8 Amendment or repeal in same session An Act may be amended or repeale | encoded | s8 an Act may be amended or repealed in the session |
| s 9 | section | 63-65 | 9 Citation of Acts by number | inert (1) | heading; the provisions of the section have their own rows |
| s 9(1) | item | 66 | (1) The Acts passed in each calendar year shall be numbered in regular | encoded | s9(1) number of an Act among the Acts of its calendar year |
| s 9(2) | item | 67-72 | (2) It is sufficient to refer to an Act in— by— | encoded | s9(2) the way of referring to an Act is sufficient |
| s 9(2)(a) | item | 68 | (a) any other Act; | encoded | s9(2) the way of referring to an Act is sufficient |
| s 9(2)(b) | item | 69 | (b) a subordinate instrument; | encoded | s9(2) the way of referring to an Act is sufficient |
| s 9(2)(c) | item | 70 | (c) a deed or other instrument; or | encoded | s9(2) the way of referring to an Act is sufficient |
| s 9(2)(d) | item | 71 | (d) any other document whatsoever— | encoded | s9(2) the way of referring to an Act is sufficient |
| s 9(2)(e) | item | 73 | (e) in the case of an Act passed before 1 January 1986, the number of  | encoded | s9(2) the way of referring to an Act is sufficient; s9(2)(e) last day of the period in which an Act is cited by its number only |
| s 9(2)(f) | item | 74 | (f) in the case of an Act passed on or after 1 January 1986, the calen | encoded | s9(2) the way of referring to an Act is sufficient; s9(2)(f) first day of the period in which an Act is cited by year and number |
| s 9(3) | item | 75-76 | (3) A failure to comply with subsection (1) in a calendar year (whethe | encoded | s9(3) a failure to number the Acts of a year in a regular series affects the operation or effect of an Act passed that year |
| s 10 | section | 77-79 | 10 Citation of Acts by title | inert (1) | heading; the provisions of the section have their own rows |
| s 10(1) | item | 80-85 | (1) An Act may be cited in— by— | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(a) | item | 81 | (a) that Act or any other Act; | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(b) | item | 82 | (b) a subordinate instrument; | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(c) | item | 83 | (c) a deed or other instrument; | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(d) | item | 84 | (d) any other document whatsoever— | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(e) | item | 86 | (e) the short title authorized by that Act whether or not that Act or  | encoded | s10(1) this section permits citing the Act in that form |
| s 10(1)(f) | item | 87 | (f) if there is no short title authorized by that Act, the title appea | encoded | s10(1) this section permits citing the Act in that form |
| s 10(2) | item | 88 | (2) The title of an Act appearing before the enacting words or, if the | encoded | s10(2) the title before the enacting words forms part of the Act |
| s 10(2AA) | item | 89-90 | (2AA) A citation of an Act by the title appearing before the enacting  | encoded | s10(2AA) a citation by the title is sufficient for s 10(1) |
| s 10(2A) | item | 91-92 | (2A) The Clerk of the Parliaments must alter the title appearing befor | encoded | s10(2A) word the Clerk of the Parliaments substitutes for the word Bill in the title |
| s 10(2B) | item | 93-94 | (2B) The alteration of a Bill to give effect to subsection (2A) is not | encoded | s10(2B) the alteration to give effect to s 10(2A) is an amendment of the Bill |
| s 10(3) | item | 95 | (3) If an Act passed on or after 1 September 1985 does not authorize i | encoded | s10(3) first day on which an Act passed without a short title leaves its long title out of the Act; s10(3) the long title of the Bill forms  |
| s 10A | section | 96-98 | 10A Construction of power to fix commencement of Act | inert (1) | heading; the provisions of the section have their own rows |
| s 10A(1) | item | 99 | (1) If an Act provides for the Act or a provision of the Act to come i | encoded | s10A(1) the Act confers power on the Governor in Council to fix a day by proclamation |
| s 10A(2) | item | 100 | (2) If an Act provides for the Act or provisions of the Act to come in | encoded | s10A(2) the Act confers power to fix the days by proclamation in that way |
| s 10A(2)(a) | item | 101 | (a) a day for the Act or provisions to come into operation; or | encoded | s10A(2) the Act confers power to fix the days by proclamation in that way |
| s 10A(2)(b) | item | 102 | (b) different days for different provisions of the Act to come into op | encoded | s10A(2) the Act confers power to fix the days by proclamation in that way |
| s 10A(3) | item | 103-104 | (3) If an Act makes no provision for the commencement of a particular  | fork F9 | s10A first anniversary of the passing of an Act; s10A(3),(4) day an Act with no commencement provision is taken to come into operation |
| s 10A(4) | item | 105-106 | (4) If an Act makes no provision for the commencement of the Act or of | fork F9 | s10A(3),(4) day an Act with no commencement provision is taken to come into operation |
| s 11 | section | 108 | 11 Time of commencement and date of passing of Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 11(1) | item | 109-110 | (1) Subject to subsection (2) and to section 71 of the Constitution Ac | encoded | s11 moment an Act or provision comes into operation on a fixed day |
| s 11(2) | item | 111-112 | (2) If an Act confers power on the Governor in Council to fix by procl | encoded | s11 moment an Act or provision comes into operation on a fixed day |
| s 11(2A) | item | 113-114 | (2A) If a proclamation fixing a day for the coming into operation of a | encoded | s11 commencement once the proclamation is published; s11 moment an Act or provision comes into operation on a fixed day |
| s 11(3) | item | 115-116 | (3) The date of the passing of an Act is the date on which the Act rec | encoded | s11(3) date of the passing of an Act |
| s 11(4) | item | 117-118 | (4) A reference in an Act to the date of commencement of that Act or a | encoded | s11(4) date of commencement of an Act or portion whose provisions began on different days |
| s 12 | section | 120-121 | 12 Time of expiry of temporary Acts Where an Act or a provision of an  | encoded | s12 moment until which a temporary Act or provision continues in operation |
| s 13 | section | 122-124 | 13 Exercise of powers between passing and commencement of Act | inert (1) | heading; the provisions of the section have their own rows |
| s 13(1) | item | 125-132 | (1) This section applies where an Act or a provision of an Act which d | encoded | s13(1) s 13 applies |
| s 13(1)(a) | item | 126 | (a) make subordinate instruments or any other instruments of a legisla | encoded | s13(1) s 13 applies |
| s 13(1)(b) | item | 127 | (b) give notices; or | encoded | s13(1) s 13 applies |
| s 13(1)(c) | item | 128 | (c) make appointments; or | encoded | s13(1) s 13 applies |
| s 13(1)(d) | item | 129 | (d) establish a body; or | encoded | s13(1) s 13 applies |
| s 13(1)(e) | item | 130 | (e) prescribe forms; or | encoded | s13(1) s 13 applies |
| s 13(1)(f) | item | 131 | (f) do any other thing— | encoded | s13(1) s 13 applies |
| s 13(2) | item | 133 | (2) Unless the contrary intention appears, the power may be exercised  | encoded | s13(2) the exercise of the power confers a right or imposes an obligation before the commencement; s13(2) the power may be exercised after t |
| s 13(2)(a) | item | 134 | (a) bringing the Act or provision into operation; or | encoded | s13(2) the exercise of the power confers a right or imposes an obligation before the commencement; s13(2) the power may be exercised after t |
| s 13(2)(b) | item | 135 | (b) making the Act or provision or the other Act as amended fully effe | encoded | s13(2) the exercise of the power confers a right or imposes an obligation before the commencement; s13(2) the power may be exercised after t |
| s 13(3) | item | 136 | (3) Without limiting subsection (2), an appointee may exercise a power | encoded | s13(3) an appointee or body may exercise the power before the commencement as if the Act were in operation |
| s 13(4) | item | 137 | (4) For the purposes of any provision as to the duration of the term o | encoded | s13(4) the term of office cannot yet begin |
| s 14 | section | 139 | 14 Provision as to effect of repeal etc. of Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 14(1) | item | 140-143 | (1) Where an Act or a provision of an Act— any Act or provision of an  | encoded | s14(1) the Act or provision that the ending Act or provision had repealed is construed as revived |
| s 14(1)(a) | item | 141 | (a) is repealed; or | encoded | s14(1) the Act or provision that the ending Act or provision had repealed is construed as revived |
| s 14(1)(b) | item | 142 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s14(1) the Act or provision that the ending Act or provision had repealed is construed as revived |
| s 14(2) | item | 144-156 | (2) Where an Act or a provision of an Act— the repeal, amendment, expi | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(a) | item | 145 | (a) is repealed or amended; or | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(b) | item | 146 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(c) | item | 148 | (c) revive anything not in force or existing at the time at which the  | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(d) | item | 149 | (d) affect the previous operation of that Act or provision or anything | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(e) | item | 150 | (e) affect any right, privilege, obligation or liability acquired, acc | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(ea) | item | 151-152 | (ea) affect any immunity or indemnity conferred or given by or under t | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(f) | item | 153 | (f) affect any penalty, forfeiture or punishment incurred in respect o | encoded | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2)(g) | item | 154-155 | (g) affect any investigation, legal proceeding or remedy in respect of | fork F4 | s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed; s14(2)(c)-(f) t |
| s 14(2A) | item | 157-161 | (2A) Without limiting subsection (2), if a provision of an Act that is | encoded | s14(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 14(2A)(a) | item | 159 | (a) is repealed; or | encoded | s14(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 14(2A)(b) | item | 160 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s14(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 14(3) | item | 162-163 | (3) References in subsections (1), (2) and (2A) to the repeal of an Ac | encoded | s14(3) the way of repealing is within the references to repeal in s 14(1), (2) and (2A) |
| s 14(3)(a) | item | 164 | (a) a repeal effected by implication; and | encoded | s14(3) the way of repealing is within the references to repeal in s 14(1), (2) and (2A) |
| s 14(3)(b) | item | 165 | (b) a repeal effected by abrogating or limiting the effect of the Act  | encoded | s14(3) the way of repealing is within the references to repeal in s 14(1), (2) and (2A) |
| s 15 | section | 167 | 15 Effect of repeal etc. of amending Act | inert (1) | heading; the provisions of the section have their own rows |
| s 15(1) | item | 168-171 | (1) Where an Act or a provision of an Act, being an Act or provision t | encoded | s15(1) the ending of the amending Act or provision affects the direct amendments |
| s 15(1)(a) | item | 169 | (a) is repealed; or | encoded | s15(1) the ending of the amending Act or provision affects the direct amendments |
| s 15(1)(b) | item | 170 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s15(1) the ending of the amending Act or provision affects the direct amendments |
| s 15(2) | item | 172 | (2) Subsection (1) applies to a direct amendment made to a provision o | encoded | s15(2) s 15(1) applies to the amendment |
| s 16 | section | 174-175 | 16 Repeal and re-enactment Where an Act or a provision of an Act is re | inert (1) | heading; the provisions of the section have their own rows |
| s 16(a) | item | 176 | (a) any reference in any Act or subordinate instrument to the repealed | encoded | s16(a) a reference to the repealed Act or provision is construed as a reference to the re-enacted Act or provision |
| s 16(b) | item | 177 | (b) insofar as any subordinate instrument made or other thing done und | encoded | s16(b) the instrument made or thing done has effect as if made or done under the re-enacted Act or provision |
| s 17 | section | 178-180 | 17 Construction of references in Acts to other enactments | inert (1) | heading; the provisions of the section have their own rows |
| s 17(1) | item | 181 | (1) A reference in an Act to that Act or to any provision of that Act  | encoded | s17(1) a reference in an Act to another enactment is construed as a reference to |
| s 17(1)(a) | item | 182 | (a) if the Act, subordinate instrument or provision in question has be | encoded | s17(1) a reference in an Act to another enactment is construed as a reference to |
| s 17(1)(b) | item | 183 | (b) if the Act, subordinate instrument or provision in question has be | encoded | s17(1) a reference in an Act to another enactment is construed as a reference to |
| s 17(1)(c) | item | 184 | (c) if the Act, subordinate instrument or provision in question has be | encoded | s17(1) a reference in an Act to another enactment is construed as a reference to |
| s 17(1)(d) | item | 185 | (d) if the Act, subordinate instrument or provision in question has be | encoded | s17(1) a reference in an Act to another enactment is construed as a reference to |
| s 17(1A) | item | 186-187 | (1A) A reference in an Act to any provision of that or any other Act o | encoded | s17(1A) a reference in an Act to a provision that has been renumbered or relocated is construed as a reference to |
| s 17(2) | item | 188-189 | (2) In this section— | encoded | opening words of the paragraphs below, cited with them: s17(2)(a) a reference to an Act in s 17 includes; s17(2)(b) a reference to a subordinate instrument in s 17 in |
| s 17(2)(a) | item | 190 | (a) a reference to an Act includes a reference to— | encoded | s17(2)(a) a reference to an Act in s 17 includes |
| s 17(2)(a)(i) | item | 191 | (i) a Commonwealth Act; and | encoded | s17(2)(a) a reference to an Act in s 17 includes |
| s 17(2)(a)(ii) | item | 192 | (ii) an Act or Ordinance of another State or of a Territory; | encoded | s17(2)(a) a reference to an Act in s 17 includes |
| s 17(2)(b) | item | 193 | (b) a reference to a subordinate instrument includes a reference to an | encoded | s17(2)(b) a reference to a subordinate instrument in s 17 includes |
| s 17(2)(b)(i) | item | 194 | (i) a Commonwealth Act; and | encoded | s17(2)(b) a reference to a subordinate instrument in s 17 includes |
| s 17(2)(b)(ii) | item | 195 | (ii) an Act or Ordinance of another State or of a Territory. | encoded | s17(2)(b) a reference to a subordinate instrument in s 17 includes |
| s 18 | section | 196-199 | 18 References in Acts to provisions of subordinate instruments Where i | encoded | s18 the reference is construed as a reference to one contained in a subordinate instrument made under that Act |
| s 19 | section | 201 | 19 Citation of references in Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 19(1) | item | 202 | (1) Where a provision of an Act refers— | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(aaa) | item | 203-204 | (aaa) to a Chapter by a number, the reference shall, unless the contex | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(aa) | item | 205-206 | (aa) to a Part by a number, the reference shall, unless the context ot | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(aa)(i) | item | 207-208 | (i) if the Act contains Chapters and the Part number is not a decimal  | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(aa)(ia) | item | 209-210 | (ia) if the Act contains Chapters and the Part number is a decimal num | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(aa)(ii) | item | 211 | (ii) if the Act does not contain Chapters, as a reference to the Part, | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(a) | item | 212-213 | (a) to a section or Schedule by a number, the reference shall, unless  | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(b) | item | 214 | (b) to a Schedule but does not refer to it by a number, the reference  | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c) | item | 215-227 | (c) to a Division, Subdivision, subsection, paragraph, subparagraph, s | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(i) | item | 216 | (i) to the Division, designated by that number, of the Part in which t | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(ii) | item | 217 | (ii) to the Subdivision, designated by that number, of the Division in | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(iii) | item | 218 | (iii) to the subsection, designated by that number, of the section in  | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(iv) | item | 219 | (iv) to the paragraph, designated by that number, of the section, subs | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(v) | item | 220 | (v) to the paragraph, designated by that number, of the clause, subcla | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(vi) | item | 221 | (vi) to the subparagraph, designated by that number, of the paragraph  | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(vii) | item | 222 | (vii) to the sub-subparagraph, designated by that number, of the subpa | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(viii) | item | 223 | (viii) to the table, designated by that number, of or in the section o | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(ix) | item | 224 | (ix) to the clause, item, column, table or form, designated by that nu | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(x) | item | 225 | (x) to the subclause, designated by that number, of the clause in whic | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(1)(c)(xi) | item | 226 | (xi) to the sub-subclause, designated by that number, of the subclause | encoded | s19(1) a reference to a unit by number is construed as a reference to the unit |
| s 19(2) | item | 228 | (2) In subsection (1) number means— | encoded | s19(2) the designation is a number for s 19(1) |
| s 19(2)(a) | item | 229 | (a) a number expressed in words or figures; | encoded | s19(2) the designation is a number for s 19(1) |
| s 19(2)(b) | item | 230 | (b) a letter; or | encoded | s19(2) the designation is a number for s 19(1) |
| s 19(2)(c) | item | 231 | (c) a combination of a number so expressed and a letter. | encoded | s19(2) the designation is a number for s 19(1) |
| s 20 | section | 232-235 | 20 Construction of references in Acts to portions of Acts or subordina | encoded | s20 the division at a position is within the portion cited |
| s 21 | section | 237 | 21 Meaning of certain expressions in Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 21(1) | item | 238 | (1) Unless the contrary intention appears, a reference in an Imperial  | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(a) | item | 239 | (a) to the colony or the colony of New South Wales or the territory of | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(b) | item | 240 | (b) to the Governor of the colony of New South Wales shall be construe | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(c) | item | 241 | (c) to the Colonial Secretary of the colony of New South Wales or the  | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(d) | item | 242 | (d) to the Supreme Court of the colony of New South Wales or any judge | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(e) | item | 243 | (e) to a justice of the peace in and for the colony of New South Wales | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(f) | item | 244 | (f) to any officer or other person in the public service of the colony | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(1)(g) | item | 245 | (g) to the Government Gazette of the colony of New South Wales shall b | encoded | s21(1) a reference in an old Act is construed as a reference to; s21(1) day on which Imperial and New South Wales Acts are read as reference |
| s 21(2) | item | 246 | (2) Unless the contrary intention appears, a reference in any Act (by  | encoded | s21(2) a reference to the Legislative Council in an old Act is construed as a reference to; s21(2) day on which an Act is read as referring  |
| s 21(3) | item | 247-248 | (3) Unless the contrary intention appears, a reference in any Act to H | encoded | s21(3) a reference to naval or military forces or service includes |
| s 21A | section | 249-251 | 21A Incorporation of amendments | inert (1) | heading; the provisions of the section have their own rows |
| s 21A(1) | item | 252 | (1) If an Act has been amended then in any reprinting of the Act the G | encoded | s21A(1) the reprint of the Act is as amended |
| s 21A(2) | item | 253 | (2) There must be printed in a reprint of an Act— | encoded | s21A(2) the reprint must show the amending Acts and instruments and the amended provisions |
| s 21A(2)(a) | item | 254 | (a) a reference to each Act or subordinate instrument by which the rep | encoded | s21A(2) the reprint must show the amending Acts and instruments and the amended provisions |
| s 21A(2)(b) | item | 255 | (b) a reference (whether in a sidenote, footnote or endnote) to each p | encoded | s21A(2) the reprint must show the amending Acts and instruments and the amended provisions |
| s 21A(3) | item | 256-257 | (3) In reprinting an Act the Government Printer may omit the indorseme | encoded | s21A(3) the reprint may omit the indorsement of the date of passing |
| s 21A(4) | item | 258-259 | (4) Nothing in subsection (3) affects the status of the indorsement as | encoded | s21A(4) omitting the indorsement in a reprint affects its status as part of the Act |
| s 21A note | note | 260-261 | Note See Constitution Act 1975, section 69. | inert (1) | a note that points to another provision and creates no rule |
| Part III | part | 263 | Part III—Provisions applicable to subordinate instruments | inert (1) | heading |
| s 22 | section | 265 | 22 Subordinate instruments to be construed subject to legislative powe | inert (1) | heading; the provisions of the section have their own rows |
| s 22(1) | item | 266-269 | (1) Every subordinate instrument shall be construed as operating to th | encoded | s22(1) how a provision of a subordinate instrument is construed against the limit of its power |
| s 22(1)(a) | item | 267 | (a) the legislative power of the State of Victoria; or | encoded | s22(1) how a provision of a subordinate instrument is construed against the limit of its power |
| s 22(1)(b) | item | 268 | (b) the power to make the subordinate instrument conferred by the Act  | encoded | s22(1) how a provision of a subordinate instrument is construed against the limit of its power |
| s 22(2) | item | 270 | (2) The provisions of this section are in addition to, and not in dero | encoded | s22(2) s 22 takes the place of a provision on the construction or extent of operation of the instrument |
| s 23 | section | 272-273 | 23 Construction of subordinate instruments Where an Act confers power  | encoded | s23 an expression in the instrument has the same meaning as in the Act conferring the power |
| s 24 | section | 275-276 | 24 Time of commencement of subordinate instruments Where in respect of | encoded | s24 moment a subordinate instrument that is not a statutory rule comes into operation |
| s 25 | section | 278-279 | 25 Time of expiry of temporary subordinate instruments Where a subordi | encoded | s25 moment until which a temporary subordinate instrument or provision continues in operation |
| s 26 | section | 280-282 | 26 Exercise of powers between making and commencement of subordinate i | inert (1) | heading; the provisions of the section have their own rows |
| s 26(1) | item | 283-290 | (1) This section applies where a subordinate instrument or a provision | encoded | s26(1) s 26 applies |
| s 26(1)(a) | item | 284 | (a) make other subordinate instruments or any other instruments of a l | encoded | s26(1) s 26 applies |
| s 26(1)(b) | item | 285 | (b) give notices; or | encoded | s26(1) s 26 applies |
| s 26(1)(c) | item | 286 | (c) make appointments; or | encoded | s26(1) s 26 applies |
| s 26(1)(d) | item | 287 | (d) establish a body; or | encoded | s26(1) s 26 applies |
| s 26(1)(e) | item | 288 | (e) prescribe forms; or | encoded | s26(1) s 26 applies |
| s 26(1)(f) | item | 289 | (f) do any other thing— | encoded | s26(1) s 26 applies |
| s 26(2) | item | 291 | (2) Unless the contrary intention appears, the power may be exercised  | encoded | s26(2) the exercise of the power confers a right or imposes an obligation before the commencement; s26(2) the power may be exercised after t |
| s 26(2)(a) | item | 292 | (a) bringing the subordinate instrument or provision into operation; o | encoded | s26(2) the exercise of the power confers a right or imposes an obligation before the commencement; s26(2) the power may be exercised after t |
| s 26(2)(b) | item | 293 | (b) making the subordinate instrument or provision or the other subord | encoded | s26(2) the exercise of the power confers a right or imposes an obligation before the commencement; s26(2) the power may be exercised after t |
| s 26(3) | item | 294 | (3) Without limiting subsection (2), an appointee may exercise a power | encoded | s26(3) an appointee or body may exercise the power before the commencement as if the instrument were in operation |
| s 26(4) | item | 295 | (4) For the purposes of any provision as to the duration of the term o | encoded | s26(4) the term of office cannot yet begin |
| s 27 | section | 297-298 | 27 Implied power to repeal or amend subordinate instruments Where an A | encoded | s27 the power to make the instrument includes a power to repeal or amend it |
| s 28 | section | 300 | 28 Provisions as to effect of repeal etc. of subordinate instruments | inert (1) | heading; the provisions of the section have their own rows |
| s 28(1) | item | 301-304 | (1) Where a subordinate instrument or a provision of a subordinate ins | encoded | s28(1) the instrument or provision that the ending instrument or provision had repealed is construed as revived |
| s 28(1)(a) | item | 302 | (a) is repealed; or | encoded | s28(1) the instrument or provision that the ending instrument or provision had repealed is construed as revived |
| s 28(1)(b) | item | 303 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s28(1) the instrument or provision that the ending instrument or provision had repealed is construed as revived |
| s 28(2) | item | 305-314 | (2) Where a subordinate instrument or a provision of a subordinate ins | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(a) | item | 306 | (a) is repealed or amended; or | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(b) | item | 307 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(c) | item | 309 | (c) revive anything not in force or existing at the time at which the  | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(d) | item | 310 | (d) affect the previous operation of that subordinate instrument or pr | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(e) | item | 311 | (e) affect any right, privilege, obligation or liability acquired, acc | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(f) | item | 312 | (f) affect any penalty, forfeiture or punishment incurred in respect o | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2)(g) | item | 313 | (g) affect any investigation, legal proceeding or remedy in respect of | encoded | s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed; s28(2)(c |
| s 28(2A) | item | 315-319 | (2A) Without limiting subsection (2), if a provision of a subordinate  | encoded | s28(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 28(2A)(a) | item | 317 | (a) is repealed; or | encoded | s28(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 28(2A)(b) | item | 318 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s28(2A) the repeal, expiry or lapsing of the provision ends the effect it had |
| s 28(3) | item | 320-321 | (3) References in subsections (1), (2) and (2A) to the repeal of a sub | encoded | s28(3) the way of repealing is within the references to repeal in s 28(1), (2) and (2A) |
| s 28(3)(a) | item | 322 | (a) a repeal effected by implication; and | encoded | s28(3) the way of repealing is within the references to repeal in s 28(1), (2) and (2A) |
| s 28(3)(b) | item | 323 | (b) a repeal effected by abrogating or limiting the effect of the subo | encoded | s28(3) the way of repealing is within the references to repeal in s 28(1), (2) and (2A) |
| s 29 | section | 325 | 29 Effect of repeal etc. of amending subordinate instrument | inert (1) | heading; the provisions of the section have their own rows |
| s 29(1) | item | 326-329 | (1) Where a subordinate instrument or a provision of a subordinate ins | encoded | s29(1) the ending of the amending instrument or provision affects the direct amendments |
| s 29(1)(a) | item | 327 | (a) is repealed; or | encoded | s29(1) the ending of the amending instrument or provision affects the direct amendments |
| s 29(1)(b) | item | 328 | (b) expires, lapses or otherwise ceases to have effect— | encoded | s29(1) the ending of the amending instrument or provision affects the direct amendments |
| s 29(2) | item | 330 | (2) Subsection (1) applies to a direct amendment made to a provision o | encoded | s29(2) s 29(1) applies to the amendment |
| s 30 | section | 332-333 | 30 Repeal and re-making Where a subordinate instrument or a provision  | inert (1) | heading; the provisions of the section have their own rows |
| s 30(a) | item | 334 | (a) any reference in any subordinate instrument or Act to the repealed | encoded | s30(a) a reference to the repealed instrument or provision is construed as a reference to the re-made instrument or provision |
| s 30(b) | item | 335 | (b) insofar as any subordinate instrument made or other thing done und | encoded | s30(b) the instrument made or thing done has effect as if made or done under the re-made instrument or provision |
| s 31 | section | 336-338 | 31 Construction of references in subordinate instruments to other enac | inert (1) | heading; the provisions of the section have their own rows |
| s 31(1) | item | 339 | (1) A reference in a subordinate instrument to that subordinate instru | encoded | s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to |
| s 31(1)(a) | item | 340 | (a) if the subordinate instrument, Act or provision in question has be | encoded | s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to |
| s 31(1)(b) | item | 341 | (b) if the subordinate instrument, Act or provision in question has be | encoded | s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to |
| s 31(1)(c) | item | 342 | (c) if the subordinate instrument, Act or provision in question has be | encoded | s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to |
| s 31(1)(d) | item | 343 | (d) if the subordinate instrument, Act or provision in question has be | encoded | s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to |
| s 31(1A) | item | 344-345 | (1A) A reference in a subordinate instrument to any provision of that  | encoded | s31(1A) a reference in a subordinate instrument to a provision that has been renumbered or relocated is construed as a reference to |
| s 31(2) | item | 346-347 | (2) In this section— | encoded | opening words of the paragraphs below, cited with them: s31(2)(a) a reference to an Act in s 31 includes; s31(2)(b) a reference to a subordinate instrument in s 31 in |
| s 31(2)(a) | item | 348 | (a) a reference to an Act includes a reference to— | encoded | s31(2)(a) a reference to an Act in s 31 includes |
| s 31(2)(a)(i) | item | 349 | (i) a Commonwealth Act; and | encoded | s31(2)(a) a reference to an Act in s 31 includes |
| s 31(2)(a)(ii) | item | 350 | (ii) an Act or Ordinance of another State or of a Territory; | encoded | s31(2)(a) a reference to an Act in s 31 includes |
| s 31(2)(b) | item | 351 | (b) a reference to a subordinate instrument includes a reference to an | encoded | s31(2)(b) a reference to a subordinate instrument in s 31 includes |
| s 31(2)(b)(i) | item | 352 | (i) a Commonwealth Act; or | encoded | s31(2)(b) a reference to a subordinate instrument in s 31 includes |
| s 31(2)(b)(ii) | item | 353 | (ii) an Act or Ordinance of another State or of a Territory. | encoded | s31(2)(b) a reference to a subordinate instrument in s 31 includes |
| s 32 | section | 354-356 | 32 Prescribing matters by reference to other documents [endnote 1] | inert (1) | heading; the provisions of the section have their own rows |
| s 32(1) | item | 357 | (1) In this section— | encoded | opening words of the paragraphs below, cited with them: s32(1) the thing is a Code; s32(1) relevant day |
| s 32(1) def "Code" | def | 358-359 | Code means— | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(a) | item | 360 | (a) the Companies (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(b) | item | 361 | (b) the Companies (Acquisition of Shares) (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(c) | item | 362 | (c) the Futures Industry (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(d) | item | 363 | (d) the Securities Industry (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(e) | item | 364 | (e) the Companies and Securities (Interpretation and Miscellaneous Pro | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(f) | item | 365 | (f) any other Code to which the Companies and Securities (Interpretati | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(g) | item | 366 | (g) the ASIC Law of Victoria; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(h) | item | 367 | (h) the Corporations Law of Victoria; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(ha) | item | 368 | (ha) the National Electricity (Victoria) Law; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(i) | item | 369 | (i) the AFIC (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(j) | item | 370 | (j) the Financial Institutions (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(ja) | item | 371 | (ja) the National Gas (Victoria) Law; | encoded | s32(1) the thing is a Code |
| s 32 blank | blank | 372 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` |
| s 32(1) def "Code"(l) | item | 373 | (l) the Friendly Societies (Victoria) Code; | encoded | s32(1) the thing is a Code |
| s 32(1) def "Code"(m) | item | 374 | (m) a regulation or rule that has the force of law in Victoria made un | encoded | s32(1) the thing is a Code |
| s 32(1) def "relevant day" | def | 375 | relevant day means the day on which the Interpretation of Legislation  | encoded | s32(1) relevant day |
| s 32 blank#2 | blank | 376-377 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 32(1) def. of statutory rule repealed by No. 60/2000 s. 5(1).]) |
| s 32(2) | item | 378 | (2) If an Act (whether passed before or after the relevant day) author | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a) | item | 379-388 | (a) may make provision for or in relation to that matter by applying,  | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a)(i) | item | 380 | (i) an Act; or | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a)(ia) | item | 381-382 | (ia) a Commonwealth Act; or | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a)(ii) | item | 383 | (ii) a Code; or | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a)(iii) | item | 384-385 | (iii) a statutory rule; or | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(a)(iv) | item | 386-387 | (iv) a statutory rule (within the meaning of the Statutory Rules Publi | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(2)(b) | item | 389-390 | (b) must not make provision for or in relation to that matter by apply | encoded | s32(2) the subordinate instrument may apply, adopt or incorporate the matter |
| s 32(3) | item | 391-392 | (3) If a subordinate instrument made on or after the relevant day is a | encoded | opening words of the paragraphs below, cited with them: s32(3)(a) the Minister must cause the copy to be lodged, the notice published and the notice laid; s32(3)(b) w |
| s 32(3)(a) | item | 393-394 | (a) the Minister administering the Act under which the subordinate ins | encoded | s32(3)(a) the Minister must cause the copy to be lodged, the notice published and the notice laid |
| s 32(3)(a)(i) | item | 395 | (i) a copy of the matter so applied, adopted or incorporated to be lod | encoded | s32(3)(a) the Minister must cause the copy to be lodged, the notice published and the notice laid |
| s 32(3)(a)(ii) | item | 396 | (ii) notice of the documents containing the matter so applied, adopted | encoded | s32(3)(a) the Minister must cause the copy to be lodged, the notice published and the notice laid |
| s 32(3)(a)(iii) | item | 397 | (iii) a copy of the notice published in the Government Gazette to be l | encoded | s32(3)(a) the Minister must cause the copy to be lodged, the notice published and the notice laid |
| s 32(3)(b) | item | 398-399 | (b) a copy of the matter so applied, adopted or incorporated must be k | encoded | s32(3)(b) where a copy of the matter is kept available for inspection by the public without charge |
| s 32(3)(b)(i) | item | 400 | (i) in the case of a subordinate instrument that is a statutory rule,  | encoded | s32(3)(b) where a copy of the matter is kept available for inspection by the public without charge |
| s 32(3)(b)(ii) | item | 401 | (ii) in the case of a subordinate instrument that is not a statutory r | encoded | s32(3)(b) where a copy of the matter is kept available for inspection by the public without charge |
| s 32(4) | item | 402-403 | (4) If a subordinate instrument made on or after the relevant day is a | encoded | opening words of the paragraphs below, cited with them: s32(4)(a) the Minister must cause the amended copy to be lodged, the notice published and the notice laid; s32 |
| s 32(4)(a) | item | 404-405 | (a) the Minister administering the Act under which the subordinate ins | encoded | s32(4)(a) the Minister must cause the amended copy to be lodged, the notice published and the notice laid |
| s 32(4)(a)(i) | item | 406 | (i) a copy of the matter as so amended to be lodged with the Clerk of  | encoded | s32(4)(a) the Minister must cause the amended copy to be lodged, the notice published and the notice laid |
| s 32(4)(a)(ii) | item | 407 | (ii) notice of the amendment and the documents containing that amendme | encoded | s32(4)(a) the Minister must cause the amended copy to be lodged, the notice published and the notice laid |
| s 32(4)(a)(iii) | item | 408 | (iii) a copy of the notice published in the Government Gazette to be l | encoded | s32(4)(a) the Minister must cause the amended copy to be lodged, the notice published and the notice laid |
| s 32 blank#3 | blank | 409-410 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 32(4)(b) repealed by No. 104/1994 s. 30(2).]) |
| s 32(4)(c) | item | 411 | (c) a copy of the matter as amended must be kept available for inspect | encoded | s32(4)(c) where a copy of the amended matter is kept available for inspection by the public without charge |
| s 32(4)(c)(i) | item | 412 | (i) in the case of a subordinate instrument that is a statutory rule,  | encoded | s32(4)(c) where a copy of the amended matter is kept available for inspection by the public without charge |
| s 32(4)(c)(ii) | item | 413 | (ii) in the case of a subordinate instrument that is not a statutory r | encoded | s32(4)(c) where a copy of the amended matter is kept available for inspection by the public without charge |
| s 32(5) | item | 414 | (5) A failure to comply with subsection (3) or (4) does not affect the | encoded | s32(5) a failure to comply with s 32(3) or (4) affects the operation or effect of the instrument |
| s 32 blank#4 | blank | 415-416 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 32(6)–(8) amended by No. 95/1993 s. 6, repealed by No. 104/1994 s. 30(3).]) |
| s 32 blank#5 | blank | 417-418 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 32(9)–(11) repealed by No. 104/1994 s. 30(3).]) |
| s 32(12) | item | 419-423 | (12) Despite subsection (5), a person— a copy of any matter contained  | encoded | opening words of the paragraphs below, cited with them: s32(12)(a) the person may be convicted of the offence of contravening the instrument; s32(12)(b) the person is |
| s 32(12)(a) | item | 421 | (a) must not be convicted of an offence consisting of a contravention  | encoded | s32(12)(a) the person may be convicted of the offence of contravening the instrument |
| s 32(12)(b) | item | 422 | (b) is not prejudicially affected or made subject to any liability by  | encoded | s32(12)(b) the person is prejudicially affected or subject to a liability by the instrument |
| s 32(13) | item | 424-425 | (13) Despite any rule of law to the contrary, where salaries, wages, f | encoded | s32(13) the amounts may be prescribed by reference to those fixed under another Act |
| s 32(13A) | item | 426-427 | (13A) If a subordinate instrument may prescribe, determine or fix any  | encoded | s32(13A) the conditions of office may be prescribed by reference to those fixed under another Act |
| s 32(13A)(a) | item | 428 | (a) by or under any other Act; or | encoded | s32(13A) the conditions of office may be prescribed by reference to those fixed under another Act |
| s 32(13A)(b) | item | 429 | (b) by or under any Commonwealth Act. | encoded | s32(13A) the conditions of office may be prescribed by reference to those fixed under another Act |
| s 32(13B) | item | 430-431 | (13B) Subsection (13A) applies— | encoded | s32(13B) s 32(13A) applies |
| s 32(13B)(a) | item | 432 | (a) whether or not the power to prescribe, determine or fix by subordi | encoded | s32(13B) s 32(13A) applies |
| s 32(13B)(b) | item | 433 | (b) despite any rule of law to the contrary. | encoded | s32(13B) s 32(13A) applies |
| s 32(14) | item | 434 | (14) A document or matter is not applied, adopted or incorporated in a | encoded | s32(14) the document or matter is applied, adopted or incorporated |
| s 32 blank#6 | blank | 435-436 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 32(15) repealed by No. 104/1994 s. 30(3).]) |
| s 33 | section | 438 | 33 Citation of references in regulations, rules, by-laws and local law | inert (1) | heading; the provisions of the section have their own rows |
| s 33(1) | item | 439-440 | (1) Where a provision of a subordinate instrument containing a regulat | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(aaa) | item | 441-442 | (aaa) to a Chapter by a number, the reference shall, unless the contex | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(aa) | item | 443-444 | (aa) to a Part by a number, the reference shall, unless the context ot | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(aa)(i) | item | 445 | (i) if the subordinate instrument contains Chapters, as a reference to | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(aa)(ii) | item | 446 | (ii) if the subordinate instrument does not contain Chapters, as a ref | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(a) | item | 447-448 | (a) to a regulation, rule, by-law, local law or Schedule by a number,  | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(b) | item | 449 | (b) to a Schedule but does not refer to it by a number, the reference  | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c) | item | 450-465 | (c) to a Division, Subdivision, subregulation, subrule, clause of a by | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(i) | item | 451 | (i) to the Division, designated by that number, of the Part in which t | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(ii) | item | 452 | (ii) to the Subdivision, designated by that number, of the Division in | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(iii) | item | 453 | (iii) to the subregulation or clause, designated by that number, of th | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(iv) | item | 454 | (iv) to the subrule or clause, designated by that number, of the rule  | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(v) | item | 455-456 | (v) to the clause, designated by that number, of the by-law or local l | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(vi) | item | 457-458 | (vi) to the paragraph, designated by that number, of the regulation, r | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(vii) | item | 459 | (vii) to the paragraph, designated by that number, of the clause, subc | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(viii) | item | 460 | (viii) to the subparagraph, designated by that number, of the paragrap | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(ix) | item | 461 | (ix) to the sub-subparagraph, designated by that number, of the subpar | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(x) | item | 462 | (x) to the clause, item, column, table or form, designated by that num | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(xi) | item | 463 | (xi) to the subclause, designated by that number, of the clause in whi | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(1)(c)(xii) | item | 464 | (xii) to the sub-subclause, designated by that number, of the subclaus | encoded | s33(1) a reference to a unit by number is construed as a reference to |
| s 33(2) | item | 466 | (2) In subsection (1) number means— | encoded | s33(2) the designation is a number for s 33(1) |
| s 33(2)(a) | item | 467 | (a) a number expressed in words or figures; | encoded | s33(2) the designation is a number for s 33(1) |
| s 33(2)(b) | item | 468 | (b) a letter; | encoded | s33(2) the designation is a number for s 33(1) |
| s 33(2)(c) | item | 469 | (c) a combination of a number so expressed and a letter. | encoded | s33(2) the designation is a number for s 33(1) |
| s 34 | section | 470-473 | 34 Construction of references in subordinate instruments to portions o | encoded | s34 the division at a position is within the portion cited |
| Part IV | part | 475 | Part IV—Provisions applicable to Acts and subordinate instruments | inert (1) | heading |
| s 35 | section | 477-478 | 35 Principles of and aids to interpretation In the interpretation of a | inert (1) | heading; the provisions of the section have their own rows |
| s 35(a) | item | 479 | (a) a construction that would promote the purpose or object underlying | encoded | s35(a) the first construction is preferred to the second |
| s 35(b) | item | 480 | (b) consideration may be given to any matter or document that is relev | encoded | s35(b) consideration may be given to the matter or document |
| s 35(b)(i) | item | 481 | (i) all indications provided by the Act or subordinate instrument as p | encoded | s35(b)(i)-(iv) the matter or document is one the paragraph names |
| s 35(b)(ii) | item | 482 | (ii) reports of proceedings in any House of the Parliament; | encoded | s35(b)(i)-(iv) the matter or document is one the paragraph names |
| s 35(b)(iii) | item | 483 | (iii) explanatory memoranda or other documents laid before or otherwis | encoded | s35(b)(i)-(iv) the matter or document is one the paragraph names |
| s 35(b)(iv) | item | 484-485 | (iv) reports of Royal Commissions, Parliamentary Committees, Law Refor | encoded | s35(b)(i)-(iv) the matter or document is one the paragraph names |
| s 36 | section | 487 | 36 Headings, Schedules, marginal notes and footnotes | inert (1) | heading; the provisions of the section have their own rows |
| s 36(1) | item | 488-492 | (1) Headings to— form part of the Act or subordinate instrument. | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(1)(a) | item | 489-490 | (a) Chapters, Parts, Divisions or Subdivisions into which an Act or su | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(1)(b) | item | 491 | (b) Schedules to an Act or subordinate instrument— | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(1A) | item | 493-494 | (1A) Headings to Parts, Divisions or Subdivisions into which a Schedul | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(1A)(a) | item | 495 | (a) the Act is passed, or the subordinate instrument is made, on or af | encoded | s36 first day of the period in which headings, examples, notes, diagrams and punctuation form part of an Act; s36 the Act is passed or the i |
| s 36(1A)(b) | item | 496 | (b) the heading is inserted into an Act passed, or subordinate instrum | encoded | s36 the Act is passed or the instrument made on or after 1 January 2001, or the item is inserted by an enactment passed or made on or after  |
| s 36(2) | item | 497 | (2) A Schedule to an Act or subordinate instrument forms part of the A | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2A) | item | 498-502 | (2A) Headings to— form part of the Act or subordinate instrument if— | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2A)(a) | item | 500 | (a) sections, clauses, regulations, rules or items into which an Act o | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2A)(b) | item | 501 | (b) tables, columns, examples, diagrams, notes (being notes at the foo | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2A)(c) | item | 503 | (c) the Act is passed, or the subordinate instrument is made, on or af | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2A)(d) | item | 504 | (d) the heading is inserted into an Act passed, or subordinate instrum | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2B) | item | 505-509 | (2B) Headings to— form part of the subordinate instrument if— | fork F5 | s36 the item forms part of the Act or subordinate instrument |
| s 36(2B)(a) | item | 507 | (a) Orders into which a subordinate instrument containing rules or ord | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2B)(b) | item | 508 | (b) Parts into which an Order referred to in paragraph (a) is divided— | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2B)(c) | item | 510 | (c) the subordinate instrument is made on or after 1 January 2001; or | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(2B)(d) | item | 511 | (d) the heading is inserted into a subordinate instrument made before  | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3) | item | 512-513 | (3) No marginal note, footnote or endnote in an Act or subordinate ins | fork F5 | s36 the item forms part of the Act or subordinate instrument |
| s 36(3A) | item | 514-515 | (3A) An example (being an example at the foot of a provision under the | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3A)(a) | item | 516 | (a) the Act is passed, or the subordinate instrument is made, on or af | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3A)(b) | item | 517 | (b) the example, diagram or note is inserted into an Act passed, or su | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3B) | item | 518-519 | (3B) Punctuation in an Act or subordinate instrument forms part of the | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3B)(a) | item | 520 | (a) the Act is passed, or the subordinate instrument is made, on or af | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3B)(b) | item | 521 | (b) the punctuation is inserted into an Act passed, or subordinate ins | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3C) | item | 522-523 | (3C) A provision number in an Act or subordinate instrument (whether p | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3D) | item | 524-525 | (3D) An explanatory memorandum or table of provisions printed with an  | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(3E) | item | 526-527 | (3E) An index or other material printed with an Act or subordinate ins | encoded | s36 the item forms part of the Act or subordinate instrument |
| s 36(4) | item | 528-529 | (4) Nothing in subsection (3) shall be construed as preventing in the  | encoded | s36(4) subsection (3) prevents consideration under s 35(b) of the item |
| s 36A | section | 530-532 | 36A Examples | inert (1) | heading; the provisions of the section have their own rows |
| s 36A(1) | item | 533 | (1) If an Act or subordinate instrument includes at the foot of a prov | encoded | s36A(1) the example has the effect on the meaning of the provision |
| s 36A(1)(a) | item | 534 | (a) is not exhaustive; and | encoded | s36A(1) the example has the effect on the meaning of the provision |
| s 36A(1)(b) | item | 535 | (b) may extend, but does not limit, the meaning of the provision. | encoded | s36A(1) the example has the effect on the meaning of the provision |
| s 36A(2) | item | 536 | (2) This section applies to an example of a kind referred to in subsec | encoded | s36A(2) s 36A applies to the example |
| s 36A(2)(a) | item | 537 | (a) the Act is passed, or the subordinate instrument is made, on or af | encoded | s36A(2) s 36A applies to the example |
| s 36A(2)(b) | item | 538 | (b) the example is inserted into an Act passed, or subordinate instrum | encoded | s36A(2) s 36A applies to the example |
| s 36B | section | 539-541 | 36B Location of penalties, examples and notes | inert (1) | heading; the provisions of the section have their own rows |
| s 36B(1) | item | 542 | (1) In this section legislative item means a penalty, an example or a  | encoded | s36B(1) the thing is a legislative item |
| s 36B(2) | item | 543 | (2) A legislative item set out in an Act or subordinate instrument in  | encoded | s36B(2) the legislative item is taken to be at the foot of the provision |
| s 36B(3) | item | 544 | (3) This section applies in relation to a legislative item even if— | encoded | s36B(3) s 36B applies to the legislative item |
| s 36B(3)(a) | item | 545 | (a) that item was inserted by an amending Act or subordinate instrumen | encoded | s36B(3) s 36B applies to the legislative item |
| s 36B(3)(b) | item | 546 | (b) the amending Act or subordinate instrument by which it was inserte | encoded | s36B(3) s 36B applies to the legislative item |
| s 36B(4) | item | 547 | (4) Without limiting its application, this section has effect for the  | encoded | s36B(4) s 36B has effect for the purpose |
| s 37 | section | 549-550 | 37 Gender and number In an Act or subordinate instrument, unless the c | inert (1) | heading; the provisions of the section have their own rows |
| s 37(a) | item | 551-552 | (a) words importing a gender include every other gender; and | encoded | s37 the word includes the other |
| s 37 blank | blank | 553-554 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 37(b) repealed by No. 95/1993 s. 7.]) |
| s 37(c) | item | 555 | (c) words in the singular include the plural; and | encoded | s37 the word includes the other |
| s 37(d) | item | 556 | (d) words in the plural include the singular. | encoded | s37 the word includes the other |
| s 38 | section | 558-559 | 38 Definitions In all Acts and subordinate instruments, unless the con | encoded | kind of the definition of a term; meaning of a term defined in a section; meaning of a term in all Acts and subordinate instruments; members |
| s 38 def "Act" | def | 560 | Act means an Act passed by the Parliament of Victoria; | encoded | s38 definition 004 of Act |
| s 38 def "ADI" | def | 561-562 | ADI means authorised deposit-taking institution within the meaning of  | encoded | s38 definition 005 of ADI |
| s 38 def "approved alternative publication Internet site" | def | 563-564 | approved alternative publication Internet site means an Internet site  | encoded | s38 definition 006 of approved alternative publication Internet site |
| s 38 def "Attorney-General" | def | 565-566 | Attorney-General means Attorney-General of Victoria; | encoded | s38 definition 007 of Attorney-General |
| s 38 def "audio link" | def | 567-568 | audio link has the meaning given by Part IIA of the Evidence (Miscella | encoded | s38 definition 008 of audio link |
| s 38 def "audio visual link" | def | 569-570 | audio visual link has the meaning given by Part IIA of the Evidence (M | encoded | s38 definition 009 of audio visual link |
| s 38 def "Australia" | def | 571-572 | Australia, when used in a geographical sense, includes the Territory o | encoded | s38 definition 010 of Australia |
| s 38 def "Australian lawyer" | def | 573-574 | Australian lawyer has the same meaning as it has in the Legal Professi | encoded | s38 definition 011 of Australian lawyer |
| s 38 def "Australian legal practitioner" | def | 575-576 | Australian legal practitioner means— | encoded | s38 definition 012 of Australian legal practitioner |
| s 38 def "Australian legal practitioner"(a) | item | 577 | (a) an Australian legal practitioner within the meaning of the Legal P | encoded | s38 definition 012 of Australian legal practitioner |
| s 38 def "Australian legal practitioner"(b) | item | 578 | (b) a non-participant legal practitioner within the meaning of Schedul | encoded | s38 definition 012 of Australian legal practitioner |
| s 38 blank | blank | 579-580 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 38 def. of Children's Court inserted by No. 56/1989 s. 286(Sch. 2 item 10), repealed by 29/2006) |
| s 38 def "bail justice" | def | 581-582 | bail justice means— | encoded | s38 definition 013 of bail justice |
| s 38 def "bail justice"(a) | item | 583 | (a) a person appointed as a bail justice under section 14 of the Honor | encoded | s38 definition 013 of bail justice |
| s 38 def "bail justice"(b) | item | 584 | (b) a person re-appointed as a bail justice under section 15 of the Ho | encoded | s38 definition 013 of bail justice |
| s 38 def "bail justice"(c) | item | 585 | (c) a person who is a bail justice by virtue of holding a prescribed o | encoded | s38 definition 013 of bail justice |
| s 38 def "Central Plan Office" | def | 586-587 | Central Plan Office means the Central Plan Office maintained under sec | encoded | s38 definition 014 of Central Plan Office |
| s 38 def "Chief Commissioner of Police" | def | 588-589 | Chief Commissioner of Police means the person appointed under section  | encoded | s38 definition 015 of Chief Commissioner of Police |
| s 38 def "Chief Judge" | def | 590-591 | Chief Judge means Chief Judge of the County Court; | encoded | s38 definition 016 of Chief Judge |
| s 38 def "Chief Justice" | def | 592-593 | Chief Justice means Chief Justice of the Supreme Court; | encoded | s38 definition 017 of Chief Justice |
| s 38 def "Chief Magistrate" | def | 594-595 | Chief Magistrate means Chief Magistrate of the Magistrates' Court; | encoded | s38 definition 018 of Chief Magistrate |
| s 38 def "Children's Court" | def | 596-597 | Children's Court means The Children's Court of Victoria; | encoded | s38 definition 019 of Children's Court |
| s 38 def "Colonial Secretary" | def | 598 | Colonial Secretary and Chief Secretary mean the responsible Minister o | encoded | s38 definition 020 of Colonial Secretary |
| s 38 def "commencement" | def | 599 | commencement, in relation to an Act or subordinate instrument or a pro | encoded | s38 definition 021 of commencement |
| s 38 def "Commonwealth" | def | 600 | Commonwealth means the Commonwealth of Australia; | encoded | s38 definition 022 of Commonwealth |
| s 38 def "Commonwealth Act" | def | 601 | Commonwealth Act means an Act passed by the Parliament of the Commonwe | encoded | s38 definition 023 of Commonwealth Act |
| s 38 def "Consolidated Fund" | def | 602-603 | Consolidated Fund means the Consolidated Fund established under the Fi | encoded | s38 definition 024 of Consolidated Fund |
| s 38 def "contravention" | def | 604 | contravention, in relation to an Act or subordinate instrument or a pr | encoded | s38 definition 025 of contravention |
| s 38 def "coroner" | def | 605-606 | coroner has the same meaning as in section 3(1) of the Coroners Act 20 | encoded | s38 definition 026 of coroner |
| s 38 def "Coroners Court" | def | 607-608 | Coroners Court means the Coroners Court of Victoria; | encoded | s38 definition 027 of Coroners Court |
| s 38 def "Costs Court" | def | 609-610 | Costs Court has the same meaning as it has in the Supreme Court Act 19 | encoded | s38 definition 028 of Costs Court |
| s 38 def "Costs Judge" | def | 611-612 | Costs Judge has the same meaning as it has in the Supreme Court Act 19 | encoded | s38 definition 029 of Costs Judge |
| s 38 def "County Court" | def | 613 | County Court means The County Court in and for the State of Victoria; | encoded | s38 definition 030 of County Court |
| s 38 def "Court of Appeal" | def | 614-615 | Court of Appeal means the division of the Supreme Court called the Cou | encoded | s38 definition 031 of Court of Appeal |
| s 38 def "Criminal Code of the Commonwealth" | def | 616-617 | Criminal Code of the Commonwealth means the Schedule to the Criminal C | encoded | s38 definition 032 of Criminal Code of the Commonwealth |
| s 38 def "Crown" | def | 618 | Crown means the Crown in right of Victoria; | encoded | s38 definition 033 of Crown |
| s 38 def "Deputy State Coroner" | def | 619-620 | Deputy State Coroner means the Deputy State Coroner of the Coroners Co | encoded | s38 definition 034 of Deputy State Coroner |
| s 38 def "document" | def | 621 | document includes, in addition to a document in writing— | encoded | s38 definition 035 of document |
| s 38 def "document"(a) | item | 622 | (a) any book, map, plan, graph or drawing; | encoded | s38 definition 035 of document |
| s 38 def "document"(b) | item | 623 | (b) any photograph; | encoded | s38 definition 035 of document |
| s 38 def "document"(c) | item | 624 | (c) any label, marking or other writing which identifies or describes  | encoded | s38 definition 035 of document |
| s 38 def "document"(d) | item | 625 | (d) any disc, tape, sound track or other device in which sounds or oth | encoded | s38 definition 035 of document |
| s 38 def "document"(e) | item | 626 | (e) any film (including microfilm), negative, tape or other device in  | encoded | s38 definition 035 of document |
| s 38 def "document"(f) | item | 627 | (f) anything whatsoever on which is marked any words, figures, letters | encoded | s38 definition 035 of document |
| s 38 def "dual commission holder" | def | 628-629 | dual commission holder means— | encoded | s38 definition 036 of dual commission holder |
| s 38 def "dual commission holder"(a) | item | 630 | (a) in relation to the Chief Judge, a person who concurrently holds bo | encoded | s38 definition 036 of dual commission holder |
| s 38 def "dual commission holder"(b) | item | 631 | (b) in relation to the Chief Magistrate, a person who concurrently hol | encoded | s38 definition 036 of dual commission holder |
| s 38 def "electronic communication" | def | 632-633 | electronic communication has the same meaning as in the Electronic Tra | encoded | s38 definition 037 of electronic communication |
| s 38 def "enactment" | def | 634-635 | enactment means an Act or subordinate instrument or a provision of an  | encoded | s38 definition 038 of enactment |
| s 38 def "entity" | def | 636-637 | entity includes a person and an unincorporated body; | encoded | s38 definition 039 of entity |
| s 38 def "external Territory" | def | 638-639 | external Territory means a Territory, not being an internal Territory, | encoded | s38 definition 040 of external Territory |
| s 38 def "Family Court" | def | 640-641 | Family Court means Family Court of Australia; | encoded | s38 definition 041 of Family Court |
| s 38 def "Federal Court" | def | 642-643 | Federal Court means Federal Court of Australia; | encoded | s38 definition 042 of Federal Court |
| s 38 def "fee unit" | def | 644-645 | fee unit has the meaning given by section 4 of the Monetary Units Act  | encoded | s38 definition 043 of fee unit |
| s 38 def "First Peoples' Assembly" | def | 646-647 | First Peoples' Assembly means the First Peoples' Assembly of Victoria  | encoded | s38 definition 044 of First Peoples' Assembly |
| s 38 def "full name" | def | 648 | full name and proper full name, in relation to a person who has a chri | encoded | s38 definition 045 of full name |
| s 38 def "Gellung Warl" | def | 649-650 | Gellung Warl means Gellung Warl established by section 10 of the State | encoded | s38 definition 046 of Gellung Warl |
| s 38 def "Government Gazette" | def | 651 | Government Gazette means the Victoria Government Gazette published by  | encoded | s38 definition 047 of Government Gazette |
| s 38 def "Government Printer" | def | 652-653 | Government Printer means Government Printer for Victoria; | encoded | s38 definition 048 of Government Printer |
| s 38 note | note | 654-655 | Note See Constitution Act 1975 section 72. | inert (1) | a note that points to another provision and creates no rule |
| s 38 def "Governor" | def | 656 | Governor means the person for the time being administering the Governm | encoded | s38 definition 049 of Governor |
| s 38 def "Governor in Council" | def | 657 | Governor in Council means the Governor with the advice of the Executiv | encoded | s38 definition 050 of Governor in Council |
| s 38 def "GST" | def | 658-659 | GST has the same meaning as in the A New Tax System (Goods and Service | encoded | s38 definition 051 of GST |
| s 38 def "High Court" | def | 660-661 | High Court means High Court of Australia; | encoded | s38 definition 052 of High Court |
| s 38 def "IBAC" | def | 662-663 | IBAC means the Independent Broad-based Anti-corruption Commission esta | encoded | s38 definition 053 of IBAC |
| s 38 def "Imperial Act" | def | 664 | Imperial Act means an Act passed by— | encoded | s38 definition 054 of Imperial Act |
| s 38 def "Imperial Act"(a) | item | 665 | (a) the Parliament of England; | encoded | s38 definition 054 of Imperial Act |
| s 38 def "Imperial Act"(b) | item | 666 | (b) the Parliament of Great Britain; | encoded | s38 definition 054 of Imperial Act |
| s 38 def "Imperial Act"(c) | item | 667 | (c) the Parliament of the United Kingdom of Great Britain and Ireland; | encoded | s38 definition 054 of Imperial Act |
| s 38 def "Imperial Act"(d) | item | 668 | (d) the Parliament of the United Kingdom of Great Britain and Northern | encoded | s38 definition 054 of Imperial Act |
| s 38 def "individual" | def | 669-670 | individual means a natural person; | encoded | s38 definition 055 of individual |
| s 38 def "infamous offence" | def | 671 | infamous offence and infamous crime include— | encoded | s38 definition 056 of infamous offence |
| s 38 def "infamous offence"(a) | item | 672 | (a) perjury; and | encoded | s38 definition 056 of infamous offence |
| s 38 def "infamous offence"(b) | item | 673 | (b) the commission of an act of bestiality or an attempt to commit an  | encoded | s38 definition 056 of infamous offence |
| s 38 def "insolvent under administration" | def | 674-675 | insolvent under administration means— | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "insolvent under administration"(a) | item | 676 | (a) a person who is an undischarged bankrupt within the meaning of the | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "insolvent under administration"(b) | item | 677 | (b) a person who has executed a deed of arrangement under Part X of th | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "insolvent under administration"(c) | item | 678 | (c) a person whose creditors have accepted a composition under Part X  | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "insolvent under administration"(d) | item | 679 | (d) a person for whom a debt agreement has been made under Part IX of  | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "insolvent under administration"(e) | item | 680 | (e) a person who has executed a personal insolvency agreement under Pa | encoded | s38 definition 057 of insolvent under administration |
| s 38 def "internal Territory" | def | 681-682 | internal Territory means the Australian Capital Territory, the Jervis  | encoded | s38 definition 058 of internal Territory |
| s 38 def "Jervis Bay Territory" | def | 683-684 | Jervis Bay Territory means the Territory referred to in the Jervis Bay | encoded | s38 definition 059 of Jervis Bay Territory |
| s 38 def "justice" | def | 685 | justice means a justice of the peace; | encoded | s38 definition 060 of justice |
| s 38 def "land" | def | 686 | land includes buildings and other structures permanently affixed to la | encoded | s38 definition 061 of land |
| s 38 def "law officer" | def | 687 | law officer means the Attorney-General and includes any Minister of th | encoded | s38 definition 062 of law officer |
| s 38 def "Legislative Assembly" | def | 688 | Legislative Assembly means the Legislative Assembly of Victoria; | encoded | s38 definition 063 of Legislative Assembly |
| s 38 def "Legislative Council" | def | 689 | Legislative Council means the Legislative Council of Victoria; | encoded | s38 definition 064 of Legislative Council |
| s 38 def "magistrate" | def | 690-691 | magistrate has the same meaning as in section 3(1) of the Magistrates' | encoded | s38 definition 065 of magistrate |
| s 38 def "Magistrates' Court" | def | 692-693 | Magistrates' Court means the Magistrates' Court of Victoria; | encoded | s38 definition 066 of Magistrates' Court |
| s 38 def "Minister" | def | 694 | Minister means the responsible Minister of the Crown for the time bein | encoded | s38 definition 067 of Minister |
| s 38 def "Nginma Ngainga Wara" | def | 695-696 | Nginma Ngainga Wara means Nginma Ngainga Wara established by the State | encoded | s38 definition 068 of Nginma Ngainga Wara |
| s 38 def "Northern Territory" | def | 697-698 | Northern Territory means Northern Territory of Australia; | encoded | s38 definition 069 of Northern Territory |
| s 38 def "Nyerna Yoorrook Telkuna" | def | 699-700 | Nyerna Yoorrook Telkuna means Nyerna Yoorrook Telkuna established by t | encoded | s38 definition 070 of Nyerna Yoorrook Telkuna |
| s 38 def "oath" | def | 701 | oath and affidavit, in relation to persons for the time being allowed  | encoded | s38 definition 071 of oath |
| s 38 def "Parliament" | def | 702 | Parliament means the Parliament of Victoria; | encoded | s38 definition 072 of Parliament |
| s 38 def "penalty unit" | def | 703-704 | penalty unit shall be construed in accordance with section 110 of the  | encoded | s38 definition 073 of penalty unit |
| s 38 def "person" | def | 705 | person includes a body politic or corporate as well as an individual; | encoded | s38 definition 074 of person |
| s 38 def "police officer" | def | 706-707 | police officer has the same meaning as in the Victoria Police Act 2013 | encoded | s38 definition 075 of police officer |
| s 38 def "Premier" | def | 708-709 | Premier means Premier of Victoria; | encoded | s38 definition 076 of Premier |
| s 38 def "prescribed" | def | 710 | prescribed means prescribed by the Act in which the word is used or by | encoded | s38 definition 077 of prescribed |
| s 38 def "public service" | def | 711-712 | public service has the same meaning as in the Public Administration Ac | encoded | s38 definition 078 of public service |
| s 38 def "rules of court in relation to any court" | def | 713 | rules of court in relation to any court, means rules made by the autho | encoded | s38 definition 079 of rules of court in relation to any court |
| s 38 def "sheriff" | def | 714-715 | sheriff has the same meaning as in the Sheriff Act 2009; | encoded | s38 definition 080 of sheriff |
| s 38 def "sitting days" | def | 716 | sitting days, in relation to either House of Parliament, means days on | encoded | s38 definition 081 of sitting days |
| s 38 def "Standards Australia" | def | 717-718 | Standards Australia means Standards Australia International Limited (A | encoded | s38 definition 082 of Standards Australia |
| s 38 def "Standards Council of New Zealand" | def | 719-720 | Standards Council of New Zealand means the Standards Council continued | encoded | s38 definition 083 of Standards Council of New Zealand |
| s 38 def "State" | def | 721 | State means the State of Victoria; | encoded | s38 definition 084 of State |
| s 38 def "State Coroner" | def | 722-723 | State Coroner means the State Coroner of the Coroners Court; | encoded | s38 definition 085 of State Coroner |
| s 38 def "statutory declaration" | def | 724-725 | statutory declaration means a statutory declaration under Part 4 of th | encoded | s38 definition 086 of statutory declaration |
| s 38 def "statutory rule" | def | 726-727 | statutory rule has the same meaning as in the Subordinate Legislation  | encoded | s38 definition 087 of statutory rule |
| s 38 def "subordinate instrument" | def | 728-729 | subordinate instrument means an instrument made under an Act— | encoded | s38 definition 088 of subordinate instrument |
| s 38 def "subordinate instrument"(a) | item | 730 | (a) that is a statutory rule; or | encoded | s38 definition 088 of subordinate instrument |
| s 38 def "subordinate instrument"(b) | item | 731 | (b) that is not a statutory rule but— | encoded | s38 definition 088 of subordinate instrument |
| s 38 def "subordinate instrument"(b)(i) | item | 732 | (i) contains regulations, rules, by-laws, proclamations, Orders in Cou | encoded | s38 definition 088 of subordinate instrument |
| s 38 def "subordinate instrument"(b)(ii) | item | 733 | (ii) is of a legislative character; | encoded | s38 definition 088 of subordinate instrument |
| s 38 def "Supreme Court" | def | 734 | Supreme Court means The Supreme Court of the State of Victoria; | encoded | s38 definition 089 of Supreme Court |
| s 38 def "Territory" | def | 735-736 | Territory (when used in an Act passed, or subordinate instrument made, | encoded | s38 definition 090 of Territory |
| s 38 def "Treasurer" | def | 737 | Treasurer means the Treasurer of Victoria; | encoded | s38 definition 091 of Treasurer |
| s 38 def "VCAT" | def | 738-739 | VCAT means the Victorian Civil and Administrative Tribunal established | encoded | s38 definition 092 of VCAT |
| s 38 def "Victoria Police" | def | 740-741 | Victoria Police means the body established by section 6 of the Victori | encoded | s38 definition 093 of Victoria Police |
| s 38 def "waterway" | def | 742-743 | waterway means a waterway as defined in section 3(1) of the Water Act  | encoded | s38 definition 094 of waterway |
| s 38 def "writing" | def | 744 | writing includes all modes of representing or reproducing words, figur | encoded | s38 definition 095 of writing |
| s 38AAA | section | 745-751 | 38AAA References to Departments If— the reference is, from the date wh | encoded | s38AAA the reference is taken to be a reference to the Department by its new name for the day in question |
| s 38AAA(a) | item | 749 | (a) reference is made in an Act or subordinate instrument to a particu | encoded | s38AAA the reference is taken to be a reference to the Department by its new name for the day in question |
| s 38AAA(b) | item | 750 | (b) under the Public Administration Act 2004 the name of the Departmen | encoded | s38AAA the reference is taken to be a reference to the Department by its new name for the day in question |
| s 38AA | section | 752-754 | 38AA References to Australian Standards, etc. | inert (1) | heading; the provisions of the section have their own rows |
| s 38AA(1) | item | 755 | (1) In an Act or subordinate instrument, a reference consisting of the | encoded | s38AA(1),(1A) the publisher of the standard the reference points at |
| s 38AA(1A) | item | 756-757 | (1A) In an Act or subordinate instrument, a reference consisting of th | encoded | s38AA(1),(1A) the publisher of the standard the reference points at |
| s 38AA(2) | item | 758 | (2) In an Act or subordinate instrument, a reference to Standards Aust | encoded | s38AA(2) a reference to Standards Australia includes the Standards Association of Australia as constituted on the day; s38AA(2) day Standard |
| s 38AA(3) | item | 759 | (3) In an Act or subordinate instrument, a reference to the Standards  | encoded | s38AA(3) a reference to the Standards Association of Australia is a reference to Standards Australia on the day |
| s 38A | section | 760-763 | 38A References to Corporations legislation In an Act or subordinate in | inert (1) | heading; the provisions of the section have their own rows |
| s 38A def "ASC Law" | def | 764 | ASC Law has the same meaning as ASIC Law; | encoded | s38A definition 096 of ASC Law |
| s 38A def "ASC Regulations" | def | 765 | ASC Regulations has the same meaning as ASIC Regulations has when ASIC | encoded | s38A definition 097 of ASC Regulations |
| s 38A def "ASIC Law" | def | 766 | ASIC Law has the meaning provided for by Part 11 of the Corporations ( | encoded | s38A definition 098 of ASIC Law |
| s 38A def "ASIC Act" | def | 767 | ASIC Act means the Australian Securities and Investments Commission Ac | encoded | s38A definition 099 of ASIC Act |
| s 38A def "ASIC Regulations" | def | 768 | ASIC Regulations— | encoded | s38A definition 100 of ASIC Regulations |
| s 38A def "ASIC Regulations"(a) | item | 769 | (a) when used in relation to the ASIC Law, has the meaning provided fo | encoded | s38A definition 100 of ASIC Regulations |
| s 38A def "ASIC Regulations"(b) | item | 770 | (b) when used in relation to the ASIC Act, means regulations made, or  | encoded | s38A definition 100 of ASIC Regulations |
| s 38A def "Corporations Act" | def | 771 | Corporations Act means the Corporations Act 2001 of the Commonwealth; | encoded | s38A definition 101 of Corporations Act |
| s 38A def "Corporations Law" | def | 772 | Corporations Law has the meaning provided for by Part 3 of the Corpora | encoded | s38A definition 102 of Corporations Law |
| s 38A def "Corporations legislation" | def | 773 | Corporations legislation means the Corporations legislation to which P | encoded | s38A definition 103 of Corporations legislation |
| s 38A def "Corporations Regulations" | def | 774 | Corporations Regulations— | encoded | s38A definition 104 of Corporations Regulations |
| s 38A def "Corporations Regulations"(a) | item | 775 | (a) when used in relation to the Corporations Law, has the meaning pro | encoded | s38A definition 104 of Corporations Regulations |
| s 38A def "Corporations Regulations"(b) | item | 776 | (b) when used in relation to the Corporations Act, means regulations m | encoded | s38A definition 104 of Corporations Regulations |
| s 38AB | section | 777-780 | 38AB References to National Electricity Law In an Act or subordinate i | inert (1) | heading; the provisions of the section have their own rows |
| s 38AB def "National Electricity (Victoria) Law" | def | 781-782 | National Electricity (Victoria) Law means the provisions applying beca | encoded | s38AB definition 105 of National Electricity (Victoria) Law |
| s 38AB def "National Electricity (Victoria) Regulations" | def | 783-784 | National Electricity (Victoria) Regulations means the provisions apply | encoded | s38AB definition 106 of National Electricity (Victoria) Regulations |
| s 38B | section | 785-788 | 38B References to Financial Institutions legislation In an Act or subo | inert (1) | heading; the provisions of the section have their own rows |
| s 38B def "AFIC (Victoria) Code" | def | 789 | AFIC (Victoria) Code means the provision applying because of section 5 | encoded | s38B definition 107 of AFIC (Victoria) Code |
| s 38B def "AFIC (Victoria) Regulations" | def | 790 | AFIC (Victoria) Regulations means the provisions applying by reason of | encoded | s38B definition 108 of AFIC (Victoria) Regulations |
| s 38B def "Financial Institutions (Victoria) Code" | def | 791 | Financial Institutions (Victoria) Code means the provisions applying b | encoded | s38B definition 109 of Financial Institutions (Victoria) Code |
| s 38B def "Financial Institutions (Victoria) Regulations" | def | 792 | Financial Institutions (Victoria) Regulations means the provisions app | encoded | s38B definition 110 of Financial Institutions (Victoria) Regulations |
| s 38BA | section | 793-796 | 38BA References to National Gas Law In an Act or subordinate instrumen | inert (1) | heading; the provisions of the section have their own rows |
| s 38BA def "National Gas (Victoria) Law" | def | 797 | National Gas (Victoria) Law means the provisions applying because of s | encoded | s38BA definition 111 of National Gas (Victoria) Law |
| s 38BA def "National Gas (Victoria) Regulations" | def | 798 | National Gas (Victoria) Regulations means the provision applying becau | encoded | s38BA definition 112 of National Gas (Victoria) Regulations |
| s 38BA blank | blank | 799-800 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 38C inserted by No. 41/1995 s. 61, repealed by No. 11/2010 s. 52.]) |
| s 38D | section | 801-804 | 38D References to Friendly Societies legislation In an Act or subordin | inert (1) | heading; the provisions of the section have their own rows |
| s 38D def "Friendly Societies (Victoria) Code" | def | 805 | Friendly Societies (Victoria) Code means the provisions applying becau | encoded | s38D definition 113 of Friendly Societies (Victoria) Code |
| s 38D def "Friendly Societies (Victoria) Regulations" | def | 806 | Friendly Societies (Victoria) Regulations means the provisions applyin | encoded | s38D definition 114 of Friendly Societies (Victoria) Regulations |
| s 38E | section | 807-810 | 38E References to Health Practitioner Regulation National Law In an Ac | inert (1) | heading; the provisions of the section have their own rows |
| s 38E def "Health Practitioner Regulation National Law" | def | 811 | Health Practitioner Regulation National Law means— | encoded | s38E definition 115 of Health Practitioner Regulation National Law |
| s 38E def "Health Practitioner Regulation National Law"(a) | item | 812 | (a) the Health Practitioner Regulation National Law— | encoded | s38E definition 115 of Health Practitioner Regulation National Law |
| s 38E def "Health Practitioner Regulation National Law"(a)(i) | item | 813 | (i) as in force from time to time, set out in the Schedule to the Heal | encoded | s38E definition 115 of Health Practitioner Regulation National Law |
| s 38E def "Health Practitioner Regulation National Law"(a)(ii) | item | 814 | (ii) as it applies as a law of Victoria, another State or a Territory  | encoded | s38E definition 115 of Health Practitioner Regulation National Law |
| s 38E def "Health Practitioner Regulation National Law"(b) | item | 815 | (b) the law of another State or a Territory that substantially corresp | encoded | s38E definition 115 of Health Practitioner Regulation National Law |
| s 38E def "Health Practitioner Regulation National Law (Victoria)" | def | 816 | Health Practitioner Regulation National Law (Victoria) means the provi | encoded | s38E definition 116 of Health Practitioner Regulation National Law (Victoria) |
| s 38EA | section | 817-819 | 38EA Definition of registered medical practitioner | inert (1) | heading; the provisions of the section have their own rows |
| s 38EA(1) | item | 820 | (1) Unless the contrary intention appears, in an Act or a subordinate  | encoded | opening words of the paragraphs below, cited with them: s38EA(1) definition 117 of registered medical practitioner |
| s 38EA(1) def "registered medical practitioner" | def | 821 | registered medical practitioner means a person registered under the He | encoded | s38EA(1) definition 117 of registered medical practitioner |
| s 38EA(2) | item | 822 | (2) This section applies to— | encoded | s38EA(2) s 38EA applies to the Act or subordinate instrument |
| s 38EA(2)(a) | item | 823 | (a) an Act that is passed, or a subordinate instrument that is made, o | encoded | s38EA(2) first day on which registered medical practitioner is defined; s38EA(2) s 38EA applies to the Act or subordinate instrument |
| s 38EA(2)(b) | item | 824 | (b) an Act that is passed, or a subordinate instrument that is made, b | encoded | s38EA(2) s 38EA applies to the Act or subordinate instrument |
| s 38EA(2)(b)(i) | item | 825 | (i) into which a reference to registered medical practitioner is inser | encoded | s38EA(2) s 38EA applies to the Act or subordinate instrument |
| s 38EA(2)(b)(ii) | item | 826 | (ii) which does not contain a reference to registered medical practiti | encoded | s38EA(2) s 38EA applies to the Act or subordinate instrument |
| s 38F | section | 827-830 | 38F References to Australian Consumer Law In an Act or subordinate ins | inert (1) | heading; the provisions of the section have their own rows |
| s 38F def "Australian Consumer Law (Victoria)" | def | 831-832 | Australian Consumer Law (Victoria) means the provisions applying becau | encoded | s38F definition 118 of Australian Consumer Law (Victoria) |
| s 38FA | section | 833-836 | 38FA References to Rail Safety National Law In an Act or subordinate i | inert (1) | heading; the provisions of the section have their own rows |
| s 38FA def "Rail Safety National Law (Victoria)" | def | 837 | Rail Safety National Law (Victoria) means the provisions applying beca | encoded | s38FA definition 119 of Rail Safety National Law (Victoria) |
| s 38G | section | 838-841 | 38G References to Education and Care Services National Law In an Act o | inert (1) | heading; the provisions of the section have their own rows |
| s 38G def "Education and Care Services National Law (Victoria)" | def | 842 | Education and Care Services National Law (Victoria) means the provisio | encoded | s38G definition 120 of Education and Care Services National Law (Victoria) |
| s 38H | section | 843-846 | 38H References to Electronic Conveyancing National Law In an Act or su | inert (1) | heading; the provisions of the section have their own rows |
| s 38H def "Electronic Conveyancing National Law (Victoria)" | def | 847 | Electronic Conveyancing National Law (Victoria) means the provisions a | encoded | s38H definition 121 of Electronic Conveyancing National Law (Victoria) |
| s 38I | section | 848-851 | 38I References to Heavy Vehicle National Law In an Act or a subordinat | inert (1) | heading; the provisions of the section have their own rows |
| s 38I def "Heavy Vehicle National Law (Victoria)" | def | 852 | Heavy Vehicle National Law (Victoria) means the provisions applying be | encoded | s38I definition 122 of Heavy Vehicle National Law (Victoria) |
| s 38J | section | 853-856 | 38J References to Marine Safety (Domestic Commercial Vessel) National  | inert (1) | heading; the provisions of the section have their own rows |
| s 38J def "Marine Safety (Domestic Commercial Vessel) National Law" | def | 857 | Marine Safety (Domestic Commercial Vessel) National Law means— | encoded | s38J definition 123 of Marine Safety (Domestic Commercial Vessel) National Law |
| s 38J def "Marine Safety (Domestic Commercial Vessel) National Law"(a) | item | 858 | (a) the Commonwealth domestic commercial vessel national law within th | encoded | s38J definition 123 of Marine Safety (Domestic Commercial Vessel) National Law |
| s 38J def "Marine Safety (Domestic Commercial Vessel) National Law"(b) | item | 859 | (b) the applied provisions within the meaning of section 3 of the Mari | encoded | s38J definition 123 of Marine Safety (Domestic Commercial Vessel) National Law |
| s 38K | section | 860-863 | 38K References to Co-operatives National Law In an Act or subordinate  | inert (1) | heading; the provisions of the section have their own rows |
| s 38K def "Co-operatives National Law (Victoria)" | def | 864 | Co-operatives National Law (Victoria) means the provisions applying be | encoded | s38K definition 124 of Co-operatives National Law (Victoria) |
| s 38L | section | 865-868 | 38L References to the Legal Profession Uniform Law In an Act or subord | inert (1) | heading; the provisions of the section have their own rows |
| s 38L def "Legal Profession Uniform Law (Victoria)" | def | 869 | Legal Profession Uniform Law (Victoria) means the provisions applying  | encoded | s38L definition 125 of Legal Profession Uniform Law (Victoria) |
| s 38M | section | 870-872 | 38M Satisfying print newspaper publication requirements | inert (1) | heading; the provisions of the section have their own rows |
| s 38M(1) | item | 873 | (1) If an Act, a statutory rule or any other subordinate instrument re | encoded | s38M(1) the requirement to publish in a print newspaper is taken by this subsection to have been met |
| s 38M(1)(a) | item | 874 | (a) on an approved alternative publication Internet site; or | encoded | s38M(1) the requirement to publish in a print newspaper is taken by this subsection to have been met |
| s 38M(1)(b) | item | 875 | (b) in a prescribed manner; or | encoded | s38M(1) the requirement to publish in a print newspaper is taken by this subsection to have been met |
| s 38M(1)(c) | item | 876 | (c) on a prescribed platform. | encoded | s38M(1) the requirement to publish in a print newspaper is taken by this subsection to have been met |
| s 38M(2) | item | 877 | (2) Without limiting subsection (1), any requirement under an Act, a s | encoded | s38M(2) the requirement to provide, distribute or use a copy of the notice is taken to have been met |
| s 38M(2A) | item | 878 | (2A) For the avoidance of doubt, subsections (1) and (2) do not apply  | encoded | s38M(2A) subsections (1) and (2) apply to the requirement |
| s 38M(3) | item | 879 | (3) The regulations may exempt an entity or a class of entity or a doc | encoded | s38M(3) s 38M applies to the entity or document |
| s 38M(4) | item | 880 | (4) Nothing in this section— | encoded | s38M(4) s 38M limits or exempts the thing |
| s 38M(4)(a) | item | 881 | (a) limits the manner or form in which any notice required to be publi | encoded | s38M(4) s 38M limits or exempts the thing |
| s 38M(4)(b) | item | 882 | (b) exempts any entity from complying with any other obligation or req | encoded | s38M(4) s 38M limits or exempts the thing |
| s 38N | section | 883-886 | 38N Minister may approve alternative publications Internet site The Mi | encoded | s38N the Internet site is an approved alternative publication Internet site |
| s 38O | section | 887-889 | 38O Minister may make and publish guidelines | inert (1) | heading; the provisions of the section have their own rows |
| s 38O(1) | item | 890 | (1) The Minister may make guidelines on— | inert (2) | machinery: the Minister's power to make guidelines |
| s 38O(1)(a) | item | 891 | (a) the use of any approved alternative publication Internet site for  | inert (2) | machinery: the Minister's power to make guidelines |
| s 38O(1)(b) | item | 892 | (b) the requirements to be complied with in relation to the publicatio | inert (2) | machinery: the Minister's power to make guidelines |
| s 38O(1)(c) | item | 893 | (c) any other matter relating to the publication of notices under sect | inert (2) | machinery: the Minister's power to make guidelines |
| s 38O(2) | item | 894 | (2) The guidelines under subsection (1)— | encoded | s38O(2)(a) the guidelines have been published as the subsection requires |
| s 38O(2)(a) | item | 895 | (a) must be published in the Government Gazette and on an approved alt | encoded | s38O(2)(a) the guidelines have been published as the subsection requires |
| s 38O(2)(b) | item | 896 | (b) may also be published in any other manner that the Minister consid | encoded | s38O(2)(a) the guidelines have been published as the subsection requires |
| s 38P | section | 897-900 | 38P Entities to have regard to guidelines Any Department, public statu | encoded | s38P the entity has complied with the duty to have regard to the guidelines |
| s 39 | section | 902-903 | 39 Parts of speech and grammatical forms Where a word or phrase is giv | encoded | s39 the other part of speech or grammatical form has a corresponding meaning |
| s 39A | section | 904-907 | 39A Definitions inserted by amending Act or subordinate instrument If  | encoded | s39A the inserted definition is taken to be inserted in the appropriate alphabetical position |
| s 39B | section | 908-910 | 39B Numbering consequential on insertion of new provisions | inert (1) | heading; the provisions of the section have their own rows |
| s 39B(1) | item | 911 | (1) If a section that is not divided into subsections is amended by th | encoded | s39B the provision as in force immediately before the amendment is taken to be the first subdivision and to be amended by inserting the expr |
| s 39B(2) | item | 912 | (2) If a statutory rule containing regulations or rules includes a reg | encoded | s39B the provision as in force immediately before the amendment is taken to be the first subdivision and to be amended by inserting the expr |
| s 39B(3) | item | 913 | (3) If a clause of a Schedule to an Act or statutory rule that is not  | encoded | s39B the provision as in force immediately before the amendment is taken to be the first subdivision and to be amended by inserting the expr |
| s 39B(4) | item | 914 | (4) This section applies only to amendments made by an Act passed, or  | encoded | s39B the provision as in force immediately before the amendment is taken to be the first subdivision and to be amended by inserting the expr |
| s 40 | section | 916-917 | 40 Exercise of powers and performance of duties Unless the contrary in | inert (1) | heading; the provisions of the section have their own rows |
| s 40(a) | item | 918 | (a) from time to time as occasion requires; and | encoded | s40(a) the power may be exercised and the duty performed from time to time as occasion requires |
| s 40(b) | item | 919 | (b) if conferred or imposed on the holder of an office or position as  | encoded | s40(b) the person is the one by whom the power may be exercised and the duty shall be performed |
| s 41 | section | 920-922 | 41 Power to appoint | inert (1) | heading; the provisions of the section have their own rows |
| s 41(1) | item | 923 | (1) If an Act or subordinate instrument confers on a person or body (t | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(a) | item | 924-925 | (a) to appoint a person to act in the office— | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(a)(i) | item | 926-927 | (i) until a person is appointed to the office; or | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(a)(ii) | item | 928 | (ii) during a vacancy in the office; | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(b) | item | 929 | (b) to remove a person appointed to the office; | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(c) | item | 930 | (c) to suspend a person appointed to the office and to appoint another | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(d) | item | 931 | (d) if the holder of the office is absent or, for any other reason, un | encoded | s41(1) the power to appoint includes the power |
| s 41(1)(e) | item | 932 | (e) if the holder of the office is, for any reason, unable to perform  | encoded | s41(1) the power to appoint includes the power |
| s 41(2) | item | 933 | (2) The following paragraphs apply in relation to an appointment of a  | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(a) | item | 934 | (a) the appointer— | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(a)(i) | item | 935 | (i) may determine the terms and conditions of the appointment, includi | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(a)(ii) | item | 936 | (ii) may terminate the appointment at any time; | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(b) | item | 937 | (b) the appointment ceases to have effect if the appointee resigns in  | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(c) | item | 938 | (c) while the appointee is acting in the office under subsection (1) ( | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(c)(i) | item | 939 | (i) the appointee has and may exercise all the powers, and shall perfo | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(c)(ii) | item | 940 | (ii) this or any other Act applies in relation to the appointment as i | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(d) | item | 941 | (d) while the appointee is appointed to perform a function or duty on  | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(d)(i) | item | 942 | (i) the appointee has and may exercise all the powers of the holder of | encoded | s41(2) the incident follows from the appointment |
| s 41(2)(d)(ii) | item | 943 | (ii) this or any other Act applies in relation to the appointment as i | encoded | s41(2) the incident follows from the appointment |
| s 41(3) | item | 944 | (3) If the power of a person or body to make an appointment to an offi | fork F6 | s41(3) the power is only exercisable on the recommendation, or subject to the approval or consent, of that other person or body |
| s 41(4) | item | 945 | (4) Despite the substitution of section 41 of this Act by section 51 o | inert (2) | machinery: a saving for things done under the former s 41 before 1997; it affects no one now |
| s 41AA | section | 946-949 | 41AA Acting appointments If a provision of an Act (other than section  | encoded | s41AA the acting appointment has the incident |
| s 41AA(a) | item | 950 | (a) the appointment may be expressed to have effect only in the circum | encoded | s41AA the acting appointment has the incident |
| s 41AA(b) | item | 951 | (b) the appointer— | encoded | s41AA the acting appointment has the incident |
| s 41AA(b)(i) | item | 952 | (i) may determine the terms and conditions of the appointment, includi | encoded | s41AA the acting appointment has the incident |
| s 41AA(b)(ii) | item | 953 | (ii) may terminate the appointment at any time; | encoded | s41AA the acting appointment has the incident |
| s 41AA(c) | item | 954-957 | (c) if the office is, or becomes, vacant while the appointee is acting | fork F13 | s41AA the acting appointment has the incident; s41AA(c) the day on which the continued acting ends, whichever event first occurs; s41AA(c) w |
| s 41AA(c)(i) | item | 955 | (i) the appointer otherwise directs; or | encoded | s41AA the acting appointment has the incident; s41AA(c) the day on which the continued acting ends, whichever event first occurs; s41AA(c) w |
| s 41AA(c)(ii) | item | 956 | (ii) a person is appointed to the office or the vacancy is filled— | encoded | s41AA the acting appointment has the incident; s41AA(c) the day on which the continued acting ends, whichever event first occurs; s41AA(c) w |
| s 41AA(e) | item | 958 | (e) the appointment ceases to have effect if the appointee resigns in  | encoded | s41AA the acting appointment has the incident |
| s 41AA(f) | item | 959 | (f) while the appointee is acting in the office, then, subject to the  | encoded | s41AA the acting appointment has the incident |
| s 41AA(f)(i) | item | 960-963 | (i) the appointee has and may exercise— as the case requires; and | encoded | s41AA the acting appointment has the incident |
| s 41AA(f)(i)(A) | item | 961 | (A) all the powers, and shall perform all the functions and duties, of | encoded | s41AA the acting appointment has the incident |
| s 41AA(f)(i)(B) | item | 962 | (B) all the powers of the holder of the office necessary for performin | encoded | s41AA the acting appointment has the incident |
| s 41AA(f)(ii) | item | 964 | (ii) this or any other Act applies in relation to the appointment as i | encoded | s41AA the acting appointment has the incident |
| s 41A | section | 965-968 | 41A Power to make instrument includes power to revoke or amend If an A | encoded | s41A the power includes a power to repeal, revoke, rescind, amend, alter or vary an instrument made in the exercise of it |
| s 42 | section | 970 | 42 Exercise of delegated powers | inert (1) | heading; the provisions of the section have their own rows |
| s 42(1) | item | 971 | (1) Where the discharge, exercise or performance by a person of a resp | encoded | s42(1) the delegate may act upon the delegate's own opinion, belief or state of mind |
| s 42(2) | item | 972 | (2) Subsection (1) applies in relation to a delegation made under an A | encoded | s42(2) subsection (1) applies to the delegation |
| s 42A | section | 973-975 | 42A Construction of power to delegate | inert (1) | heading; the provisions of the section have their own rows |
| s 42A(1) | item | 976 | (1) If an Act or subordinate instrument confers on a person or body a  | encoded | s42A(1) the proposition about the delegation holds |
| s 42A(1)(aa) | item | 977-978 | (aa) the power to delegate does not include the power to delegate that | encoded | s42A(1) the proposition about the delegation holds |
| s 42A(1)(a) | item | 979 | (a) the delegation does not prevent the discharge, exercise or perform | encoded | s42A(1) the proposition about the delegation holds |
| s 42A(1)(b) | item | 980 | (b) the delegation may be made subject to such conditions or limitatio | encoded | s42A(1) the proposition about the delegation holds |
| s 42A(1)(c) | item | 981 | (c) a responsibility, power, authority, duty or function so delegated, | encoded | s42A(1) the proposition about the delegation holds |
| s 42A(2) | item | 982 | (2) If an Act or subordinate instrument confers power to delegate to t | encoded | s42A(2) a delegation may be made to the person |
| s 42A(3) | item | 983-987 | (3) If— on and after the commencement of the amendment, the delegation | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42A(3)(a) | item | 985 | (a) a person or body delegates all of the person's or the body's respo | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42A(3)(b) | item | 986 | (b) that Act or subordinate instrument is amended to confer one or mor | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42A(4) | item | 988-992 | (4) If— on and after the commencement of the amendment, the delegation | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42A(4)(a) | item | 990 | (a) a person or body delegates one or more of the person's or the body | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42A(4)(b) | item | 991 | (b) that Act or subordinate instrument is amended to alter the scope o | encoded | s42A(3),(4) the delegation includes the additional or altered function on the day |
| s 42C | section | 993-995 | 42C Procedural defect or irregularity | inert (1) | heading; the provisions of the section have their own rows |
| s 42C(1) | item | 996 | (1) A person's appointment to an office or position, and anything done | encoded | s42C(1) the appointment, or what the person did, is ineffective because of the irregularity |
| s 42C(2) | item | 997 | (2) A delegation, and anything done under the delegation (including an | encoded | s42C(2) the delegation, or what was done under it, is ineffective because of the irregularity |
| s 42C note | note | 998-999 | Note See also section 42. | inert (1) | a note that points to another provision and creates no rule |
| s 43 | section | 1001-1002 | 43 Measurement of distances In the measurement of a distance for the p | encoded | s43 length of the straight line on a horizontal plane between two positions; s43 the distance is measured in a straight line on a horizontal |
| s 44 | section | 1004 | 44 Time | inert (1) | heading; the provisions of the section have their own rows |
| s 44(1) | item | 1005 | (1) Where in an Act or subordinate instrument a period of time is expr | fork F1, F2 | s44 last day of a period counted forward from a day; s44 last day, start left out; s44(1) first day counted in a period expressed to begin o |
| s 44(2) | item | 1006 | (2) Where in an Act or subordinate instrument a period of time is expr | fork F2 | s44(1)-(2) the day a period is expressed to begin on or end on is counted in the period; s44(2) last day of a period expressed to end on or  |
| s 44(3) | item | 1007-1008 | (3) Where the time limited by an Act or subordinate instrument for the | fork F3 | s44(3) day to which a time limited for doing an act or thing extends; s44(3) first day on or after a day that is not a holiday |
| s 44(4) | item | 1009 | (4) In subsection (3) holiday means— | encoded | s44(4) a day is a holiday |
| s 44(4)(a) | item | 1010 | (a) a Saturday or Sunday; | encoded | s44(4) a day is a holiday |
| s 44(4)(b) | item | 1011-1012 | (b) a day appointed under the Public Holidays Act 1993 as a public hol | encoded | s44(4) a day is a holiday |
| s 44 blank | blank | 1013-1014 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 44(4)(c) repealed by No. 119/1993 s. 16(2).]) |
| s 44(5) | item | 1015-1016 | (5) Subject to section 4 of the Summer Time Act 1972, whenever an expr | encoded | s44(5) hours ahead of Coordinated Universal Time that an expression of time means |
| s 44(6) | item | 1017 | (6) In an Act or subordinate instrument, unless the contrary intention | encoded | opening words of the paragraphs below, cited with them: s44(6)(a) midnight in relation to a day is the point at which that day ends; s44(1),(6)(b) last day of n calen |
| s 44(6)(a) | item | 1018 | (a) a reference to midnight, in relation to a particular day, shall be | encoded | s44(6)(a) midnight in relation to a day is the point at which that day ends |
| s 44(6)(b) | item | 1019 | (b) a reference to a month shall be construed as a reference to a cale | fork F1 | s44(1),(6)(b) last day of n calendar months reckoned from a day; s44(1),(6)(b) last day of n calendar months reckoned from a day, reading A; |
| s 44(6)(c) | item | 1020 | (c) a reference, without qualification, to a year shall be construed a | fork F1 | s44(1),(6)(c) last day of n years reckoned from a day |
| s 44(6)(d) | item | 1021 | (d) a reference to a financial year shall be construed as a reference  | encoded | s44(6)(d) first day of the financial year ending on 30 June of a year; s44(6)(d) midnight at which the financial year ending in a calendar y |
| s 44(6)(e) | item | 1022 | (e) a reference to a calendar year shall be construed as a reference t | encoded | s44(6)(e) first day of the calendar year ending on 31 December of a year; s44(6)(e) midnight at which a calendar year ends |
| s 44(7) | item | 1023 | (7) In a provision of an Act or subordinate instrument the expression  | encoded | s44(7) the time that now, heretofore and hereafter refer to |
| s 45 | section | 1025 | 45 Construction of "may" and "shall" | inert (1) | heading; the provisions of the section have their own rows |
| s 45(1) | item | 1026 | (1) Where in this Act or any Act passed or subordinate instrument made | encoded | s45(1) the power may be exercised, or not, at discretion |
| s 45(2) | item | 1027 | (2) Where in this Act or any Act passed or subordinate instrument made | encoded | s45(2) the power must be exercised |
| s 45(3) | item | 1028 | (3) The provisions of this section shall have effect notwithstanding a | encoded | s45(3) the rule of construction to the contrary applies |
| s 46 | section | 1029-1031 | 46 References to the Sovereign | inert (1) | heading; the provisions of the section have their own rows |
| s 46(1) | item | 1032 | (1) In an Act or subordinate instrument a reference to the Sovereign r | encoded | s46(1) the reference is a reference to the Sovereign for the time being |
| s 46(2) | item | 1033-1034 | (2) Unless the contrary intention appears, in an Act or a subordinate  | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(a) | item | 1035 | (a) if the Sovereign for the time being is the Queen— | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(a)(i) | item | 1036 | (i) a reference to "His Majesty" is to be construed as a reference to  | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(a)(ii) | item | 1037 | (ii) a reference to "the King" is to be construed as a reference to "t | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(b) | item | 1038 | (b) if the Sovereign for the time being is the King— | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(b)(i) | item | 1039 | (i) a reference to "Her Majesty" is to be construed as a reference to  | encoded | s46(2) the expression is construed as a reference to |
| s 46(2)(b)(ii) | item | 1040 | (ii) a reference to "the Queen" is to be construed as a reference to " | encoded | s46(2) the expression is construed as a reference to |
| s 46A | section | 1041-1043 | 46A Construction of provisions relating to entities representing, or n | inert (1) | heading; the provisions of the section have their own rows |
| s 46A(1) | item | 1044 | (1) If, in an Act or subordinate instrument, it is provided that an en | encoded | s46A the entity has the status, privileges and immunities of the Crown |
| s 46A(2) | item | 1045 | (2) If, in an Act or subordinate instrument, it is provided that an en | encoded | s46A the entity has the status, privileges and immunities of the Crown |
| s 46A(3) | item | 1046 | (3) The fact that no provision of a kind referred to in subsection (1) | encoded | s46A the entity has the status, privileges and immunities of the Crown |
| s 46A(4) | item | 1047 | (4) In this section Crown includes the State. | encoded | s46A(4) the thing is within the Crown as the section uses the word |
| s 47 | section | 1049-1050 | 47 Reference to officer in general terms In an Act or subordinate inst | encoded | s47 the person is within the reference |
| s 48 | section | 1052-1053 | 48 References to officers, localities etc. In an Act or subordinate in | inert (1) | heading; the provisions of the section have their own rows |
| s 48(a) | item | 1054 | (a) a reference to an officer or office shall be construed as a refere | encoded | s48 the reference is a reference to the officer, office, locality, jurisdiction, matter or thing in and for or of Victoria |
| s 48(b) | item | 1055 | (b) a reference to a locality, jurisdiction or other matter or thing s | encoded | s48 the reference is a reference to the officer, office, locality, jurisdiction, matter or thing in and for or of Victoria |
| s 49 | section | 1057 | 49 Service by post | inert (1) | heading; the provisions of the section have their own rows |
| s 49(1) | item | 1058 | (1) Where an Act or subordinate instrument authorizes or requires a do | encoded | opening words of the paragraphs below, cited with them: s49 service by post is deemed effected; s49 day on which service by post is deemed effected |
| s 49(1)(a) | item | 1059 | (a) unless the contrary intention appears, be deemed to be effected by | encoded | s49 service by post is deemed effected |
| s 49(1)(b) | item | 1060 | (b) unless the contrary is proved, be deemed to have been effected at  | fork F10 | s49 day on which service by post is deemed effected; s49 service by post is deemed effected |
| s 49(2) | item | 1061-1062 | (2) Where an Act or subordinate instrument authorizes or requires a do | encoded | s49 day on which service by post is deemed effected; s49 service by post is deemed effected |
| s 49(2)(a) | item | 1063 | (a) unless the contrary intention appears, be deemed to be effected by | encoded | s49 day on which service by post is deemed effected; s49 service by post is deemed effected |
| s 49(2)(b) | item | 1064 | (b) unless the contrary is proved, be deemed to have been effected at  | fork F10 | s49 day on which service by post is deemed effected |
| s 50 | section | 1066-1067 | 50 Rules of court Where an Act or subordinate instrument confers any j | encoded | s50 the authority may make the rule or order |
| s 51 | section | 1069 | 51 Provisions as to offences under two or more laws | inert (1) | heading; the provisions of the section have their own rows |
| s 51(1) | item | 1070 | (1) Where an act or omission constitutes an offence under two or more  | encoded | s51(1) the offender is liable to be prosecuted under any or all of those laws; s51(1) the offender is liable to be punished more than once f |
| s 51(2) | item | 1071 | (2) In subsection (1) law means— | encoded | s51(2) the thing is a law |
| s 51(2)(a) | item | 1072 | (a) an Act or a provision of an Act; | encoded | s51(2) the thing is a law |
| s 51(2)(b) | item | 1073 | (b) a subordinate instrument or a provision of a subordinate instrumen | encoded | s51(2) the thing is a law |
| s 51(2)(c) | item | 1074 | (c) common law. | encoded | s51(2) the thing is a law |
| s 51 blank | blank | 1075-1076 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 51A inserted by No. 51/1989 s. 146(b), repealed by No. 49/1991 s. 119(7) (Sch. 4 item 10.2).]) |
| s 52 | section | 1077-1086 | 52 Summary proceedings If an Act or subordinate instrument— then, unle | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 52(a) | item | 1081 | (a) authorises or requires a proceeding or matter to be heard and dete | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 52(a)(i) | item | 1082 | (i) summarily; or | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 52(a)(ii) | item | 1083 | (ii) by or before the Magistrates' Court; or | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 52(b) | item | 1084 | (b) uses any other words that imply that a proceeding or matter is to  | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 52(c) | item | 1085 | (c) does not provide a form or mode of procedure for the hearing and d | encoded | s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court |
| s 53 | section | 1088-1089 | 53 Strict compliance with prescribed forms not necessary Where a form  | encoded | s53 the form used is sufficient in law |
| s 54 | section | 1091 | 54 Construction of references to Acts | inert (1) | heading; the provisions of the section have their own rows |
| s 54(1) | item | 1092 | (1) A reference in an Act or subordinate instrument to an Imperial Act | encoded | s54(1) the copy of the Imperial Act the reference points at |
| s 54(1)(a) | item | 1093 | (a) in the case of Acts included in any revised edition of the statute | encoded | s54(1) the copy of the Imperial Act the reference points at |
| s 54(1)(b) | item | 1094 | (b) in the case of Acts not so included but included in the edition pr | encoded | s54(1) the copy of the Imperial Act the reference points at |
| s 54(1)(c) | item | 1095-1096 | (c) in any other case, to a copy of the Act printed by the King's Prin | encoded | s54(1) the copy of the Imperial Act the reference points at |
| s 54(2) | item | 1097 | (2) A reference in an Act or subordinate instrument to an Act of an Au | encoded | s54(2) the reference is a reference to a copy printed by the government printer of that State |
| s 54(2A) | item | 1098-1099 | (2A) A document, whether made before, on or after the commencement of  | encoded | s54(2A) the document is admissible on its mere production |
| s 54(2B) | item | 1100-1101 | (2B) A document made after the commencement of section 28 of the Misce | encoded | s54(2B) the document is admissible on its mere production |
| s 54(2C) | item | 1102-1103 | (2C) A document, whether made before, on or after the commencement of  | encoded | s54(2C) the document is admissible on its mere production |
| s 54(3) | item | 1104-1105 | (3) In this section the expressions Act, Australasian State and govern | encoded | s54(3) where the meaning of the expression is found |
| s 54A | section | 1106-1108 | 54A Style changes | inert (1) | heading; the provisions of the section have their own rows |
| s 54A(1) | item | 1109 | (1) Schedule 1 sets out style changes in Acts and statutory rules. | encoded | s54A(2) the Chief Parliamentary Counsel may authorise the alteration |
| s 54A(2) | item | 1110 | (2) The Chief Parliamentary Counsel, in preparing an Act or statutory  | encoded | s54A(2) the Chief Parliamentary Counsel may authorise the alteration |
| s 54A(3) | item | 1111 | (3) An alteration made to an Act under subsection (2) has effect for a | encoded | s54A(3) the alteration to an Act has effect for the purpose as if it had been made by an Act |
| s 54A(4) | item | 1112 | (4) An alteration made to a statutory rule under subsection (2) has ef | encoded | s54A(4) the alteration to a statutory rule has effect for the purpose as if it had been made by a statutory rule |
| s 55 | section | 1114 | 55 Construction of references to British subjects etc. | inert (1) | heading; the provisions of the section have their own rows |
| s 55(1) | item | 1115 | (1) In this section— | encoded | opening words of the paragraphs below, cited with them: s55(1)(b) the thing is a law of Victoria |
| s 55 blank | blank | 1116-1117 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 55(1)(a) repealed by No. 61/1986 s. 4(a).]) |
| s 55(1)(b) | item | 1118 | (b) law of Victoria means— | encoded | s55(1)(b) the thing is a law of Victoria |
| s 55(1)(b)(i) | item | 1119 | (i) an Act; | encoded | s55(1)(b) the thing is a law of Victoria |
| s 55(1)(b)(ii) | item | 1120 | (ii) a subordinate instrument; and | encoded | s55(1)(b) the thing is a law of Victoria |
| s 55(1)(b)(iii) | item | 1121 | (iii) an instrument having effect by virtue of a subordinate instrumen | encoded | s55(1)(b) the thing is a law of Victoria |
| s 55(2) | item | 1122-1123 | (2) A reference in any law of Victoria to a British subject or to a na | encoded | s55(2) the person is one to whom a reference to a British subject is construed as referring |
| s 55(2)(a) | item | 1124 | (a) whose name was, at any time within the three months immediately be | encoded | s55(2) the person is one to whom a reference to a British subject is construed as referring; s55(2)(a) day before which the three months are |
| s 55(2)(a)(i) | item | 1125 | (i) an electoral roll for an electoral district of the Legislative Ass | encoded | s55(2) the person is one to whom a reference to a British subject is construed as referring; s55(2)(a) day before which the three months are |
| s 55(2)(a)(ii) | item | 1126 | (ii) an electoral roll maintained under any one of the Commonwealth Ac | encoded | s55(2) the person is one to whom a reference to a British subject is construed as referring; s55(2)(a) day before which the three months are |
| s 55(2)(b) | item | 1127 | (b) who had not attained the full age of 18 years before that date but | fork F8 | s55(2) day on which a person born on a day reaches eighteen years, taken as the eighteenth anniversary; s55(2) the person is one to whom a r |
| s 55(2)(c) | item | 1128 | (c) who had not attained the full age of 18 years before that date but | fork F8 | s55(2) the person is one to whom a reference to a British subject is construed as referring |
| s 55(2)(d) | item | 1129 | (d) whose name could have been so enrolled at any such time but before | encoded | s55(2) the person is one to whom a reference to a British subject is construed as referring |
| s 55(3) | item | 1130-1131 | (3) Where a rule of law applies to or in relation to or has effect wit | encoded | s55(3) the rule of law applies to the person as if the person were a British subject |
| s 55 blank#2 | blank | 1132-1133 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 55(4) repealed by No. 61/1986 s. 4(b).]) |
| s 56 | section | 1135-1136 | 56 Construction of provisions relating to bankrupt or insolvent member | encoded | s56 the incapacity extends to the person |
| s 57 | section | 1138 | 57 Application of laws of Victoria in certain off-shore areas [endnote | inert (1) | heading; the provisions of the section have their own rows |
| s 57(1) | item | 1139-1140 | (1) Subject to this section, the provisions of the laws in force in Vi | encoded | s57(1),(3) the law applies in the offshore area by force of s 57 |
| s 57(2) | item | 1141-1149 | (2) The provisions referred to in subsection (1) apply to and in relat | encoded | s57(1),(3) the law applies in the offshore area by force of s 57; s57(2) the provisions apply as if the offshore area were part of Victoria |
| s 57(2)(a) | item | 1143-1144 | (a) any act done or omitted to be done at a place in the offshore area | fork F11 | s57(1),(3) the law applies in the offshore area by force of s 57; s57(2) the provisions apply as if the offshore area were part of Victoria |
| s 57(2)(b) | item | 1145-1146 | (b) any act done or omitted to be done in the offshore area by a perso | encoded | s57(1),(3) the law applies in the offshore area by force of s 57; s57(2) the provisions apply as if the offshore area were part of Victoria |
| s 57(2)(c) | item | 1147-1148 | (c) any matter, thing or circumstance existing or arising in the offsh | encoded | s57(1),(3) the law applies in the offshore area by force of s 57; s57(2) the provisions apply as if the offshore area were part of Victoria |
| s 57(3) | item | 1150 | (3) This section does not operate— | encoded | s57(1),(3) the law applies in the offshore area by force of s 57 |
| s 57(3)(a) | item | 1151-1152 | (a) to apply in the offshore area the provisions of any law of the Com | encoded | s57(1),(3) the law applies in the offshore area by force of s 57 |
| s 57(3)(b) | item | 1153-1154 | (b) to apply the provisions of the criminal laws of the State to or in | encoded | s57(1),(3) the law applies in the offshore area by force of s 57 |
| s 57(3)(c) | item | 1155-1156 | (c) to apply the provisions of the criminal laws of the State to or in | encoded | s57(1),(3) the law applies in the offshore area by force of s 57 |
| s 57(4) | item | 1157 | (4) Subject to this section, the several courts of Victoria are invest | encoded | s57(4) the courts of Victoria have jurisdiction in the matter |
| s 57(5) | item | 1158-1163 | (5) For the purposes of proceedings for an offence against the law of  | encoded | s57(5) the weight of the averment that a person was a person connected with Victoria |
| s 57(5)(a) | item | 1160 | (a) a person was at a specified time or in respect of a specified peri | encoded | s57(5) the weight of the averment that a person was a person connected with Victoria |
| s 57 blank | blank | 1161-1162 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: S. 57(5)(b)(c) repealed by No. 56/1999 s. 10(2).]) |
| s 57(6) | item | 1164 | (6) In this section— | encoded | opening words of the paragraphs below, cited with them: s57(6) where the meaning of the expression is found; s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(a) | item | 1165-1166 | (a) offshore area means so much of the area described in item 2 of Sch | fork F11 | s57(6) where the meaning of the expression is found |
| s 57(6)(b) | item | 1167-1168 | (b) coastal waters of Victoria has the same meaning as the expression  | encoded | s57(6) where the meaning of the expression is found |
| s 57(6)(ba) | item | 1169-1170 | (ba) cooperative scheme has the same meaning as that expression has in | encoded | s57(6) where the meaning of the expression is found |
| s 57(6)(bb) | item | 1171-1172 | (bb) continental shelf has the same meaning as in the Seas and Submerg | encoded | s57(6) where the meaning of the expression is found |
| s 57(6)(bc) | item | 1173-1174 | (bc) criminal laws means the substantive criminal law, and the law of  | encoded | s57(6) where the meaning of the expression is found |
| s 57(6)(c) | item | 1175 | (c) person connected with Victoria means a person who— | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(c)(i) | item | 1176 | (i) is domiciled in Victoria; | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(c)(ii) | item | 1177 | (ii) is permanently or temporarily resident in Victoria; | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(c)(iii) | item | 1178 | (iii) being a body corporate has a place of business in or carries on  | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(c)(iv) | item | 1179 | (iv) is on or is operating from a ship, boat or vessel of any kind lic | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 57(6)(c)(v) | item | 1180 | (v) is on or operating from a rig or other structure or installation o | encoded | s57(6)(c) the person is a person connected with Victoria |
| s 58 | section | 1181-1183 | 58 Declaration of validity of certain laws | inert (1) | heading; the provisions of the section have their own rows |
| s 58(1) | item | 1184-1187 | (1) Each provision of an Act or subordinate instrument enacted or made | encoded | s58(1) the provision has the same effect, and is as effective, as it would have been if the Australia Acts had been in operation |
| s 58(1)(a) | item | 1185 | (a) has the same effect as it would have had; and | encoded | s58(1) the provision has the same effect, and is as effective, as it would have been if the Australia Acts had been in operation |
| s 58(1)(b) | item | 1186 | (b) is as valid as it would have been— | encoded | s58(1) the provision has the same effect, and is as effective, as it would have been if the Australia Acts had been in operation |
| s 58(2) | item | 1188 | (2) In this section, Australia Acts means— | encoded | s58(2) the thing is one of the Australia Acts |
| s 58(2)(a) | item | 1189 | (a) the Australia Act 1986 of the Commonwealth; and | encoded | s58(2) the thing is one of the Australia Acts |
| s 58(2)(b) | item | 1190 | (b) the Australia Act 1986 of the United Kingdom. | encoded | s58(2) the thing is one of the Australia Acts |
| s 59 | section | 1191-1194 | 59 Transitional provision—Interpretation of Legislation (Further Amend | inert (2) | machinery: a transitional provision about proceedings begun before the commencement of a 2006 amending Act |
| Part V | part | 1195-1197 | Part V—Authorised versions | inert (1) | heading |
| s 60 | section | 1199-1202 | 60 Definitions In this Part— | inert (1) | heading; the provisions of the section have their own rows |
| s 60 def "authorised electronic version" | def | 1203 | authorised electronic version means an electronic version authorised b | encoded | s60 definition 126 of authorised electronic version |
| s 60 def "authorised version" | def | 1204 | authorised version means— | encoded | s60 definition 127 of authorised version; s63 the document is an authorised version |
| s 60 def "authorised version"(a) | item | 1205 | (a) an authorised electronic version; | encoded | s60 definition 127 of authorised version; s63 the document is an authorised version |
| s 60 def "authorised version"(b) | item | 1206 | (b) a printed copy of an authorised electronic version in accordance w | encoded | s60 definition 127 of authorised version; s63 the document is an authorised version |
| s 60 def "electronic version" | def | 1207 | electronic version means a version of legislation published on the Vic | encoded | s60 definition 128 of electronic version; s63 the document is an authorised version |
| s 60 def "legislation" | def | 1208 | legislation means— | encoded | s60 definition 129 of legislation; s63 the document is an authorised version |
| s 60 def "legislation"(a) | item | 1209 | (a) an Act; | encoded | s60 definition 129 of legislation; s63 the document is an authorised version |
| s 60 note | note | 1210-1211 | Note Act is defined in section 38. | inert (1) | a note that points to another provision and creates no rule |
| s 60 def "legislation"(b) | item | 1212 | (b) a statutory rule; | encoded | s60 definition 129 of legislation; s63 the document is an authorised version |
| s 60 note#2 | note | 1213-1214 | Note Statutory rule is defined in section 38. | inert (1) | a note that points to another provision and creates no rule |
| s 60 def "legislation"(c) | item | 1215 | (c) a consolidation of an Act as amended from time to time prepared by | encoded | s60 definition 129 of legislation; s63 the document is an authorised version |
| s 60 def "legislation"(d) | item | 1216 | (d) a consolidation of a statutory rule as amended from time to time p | encoded | s60 definition 129 of legislation; s63 the document is an authorised version |
| s 60 def "Victorian Legislation Website" | def | 1217 | Victorian Legislation Website means www.legislation.vic.gov.au. | encoded | s60 definition 130 of Victorian Legislation Website; s63 the document is an authorised version |
| s 61 | section | 1218-1221 | 61 Effect of Part This Part is in addition to, and does not derogate f | encoded | s61 Part V derogates from s 54; s63 the document is an authorised version |
| s 62 | section | 1222-1224 | 62 Authorisation of electronic version | inert (1) | heading; the provisions of the section have their own rows |
| s 62(1) | item | 1225 | (1) The Chief Parliamentary Counsel may authorise an electronic versio | encoded | s62(1) the Chief Parliamentary Counsel may authorise the version; s63 the document is an authorised version |
| s 62(2) | item | 1226 | (2) An electronic version is an authorised electronic version if— | fork F7 | s62(2),(3) the electronic version is an authorised electronic version; s63 the document is an authorised version |
| s 62(2)(a) | item | 1227 | (a) it is in the format authorised by the Chief Parliamentary Counsel; | encoded | s62(2),(3) the electronic version is an authorised electronic version; s63 the document is an authorised version |
| s 62(2)(b) | item | 1228 | (b) the words "Authorised Version" appear at the beginning of the vers | encoded | s62(2),(3) the electronic version is an authorised electronic version; s63 the document is an authorised version |
| s 62(2)(c) | item | 1229 | (c) the words "Authorised by the Chief Parliamentary Counsel" appear a | encoded | s62(2),(3) the electronic version is an authorised electronic version; s63 the document is an authorised version |
| s 62(3) | item | 1230 | (3) An electronic version which does not comply with subsection (2) is | fork F7 | s62(2),(3) the electronic version is an authorised electronic version; s63 the document is an authorised version |
| s 63 | section | 1231-1234 | 63 Printed copy of authorised electronic version A printed copy of an  | encoded | s63 the document is an authorised version |
| s 64 | section | 1235-1237 | 64 Evidentiary provisions | inert (1) | heading; the provisions of the section have their own rows |
| s 64(1) | item | 1238 | (1) An authorised version is on the mere production of that authorised | encoded | s64(1) the document is admissible on its mere production |
| s 64(2) | item | 1239 | (2) It is presumed, unless the contrary is proved, that a document pur | encoded | s64(2) the document is presumed to be an authorised version |
| s 64 note | note | 1240-1241 | Note Document is defined in section 38. | inert (1) | a note that points to another provision and creates no rule |
| Part VI | part | 1242-1244 | Part VI—General | inert (1) | heading |
| s 64A | section | 1246-1248 | 64A Appointment of non-citizens to public office | inert (1) | heading; the provisions of the section have their own rows |
| s 64A(1) | item | 1249 | (1) Despite any rule of law to the contrary, the fact that a person is | encoded | s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person |
| s 64A(2) | item | 1250 | (2) Subsection (1) does not apply if— | encoded | s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person |
| s 64A(2)(a) | item | 1251 | (a) the power to appoint a person is conferred by or under an Act or a | encoded | s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person |
| s 64A(2)(b) | item | 1252 | (b) the contrary intention expressly appears in that Act or subordinat | encoded | s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person |
| s 64A(3) | item | 1253 | (3) In this section— | encoded | opening words of the paragraphs below, cited with them: s64A(3) definition 131 of non-citizen |
| s 64A(3) def "non-citizen" | def | 1254 | non-citizen includes a person who is not an Australian citizen or who  | encoded | s64A(3) definition 131 of non-citizen |
| s 64B | section | 1255-1257 | 64B Validation—appointment of non-citizens to public office | inert (1) | heading; the provisions of the section have their own rows |
| s 64B(1) | item | 1258 | (1) In this section— | encoded | s64B(1) the appointment is a purported appointment |
| s 64B(1) def "act or omission" | def | 1259 | act or omission means an act or thing done or omitted to be done by an | encoded | s64B(1) definition 132 of act or omission; s64B(1) the appointment is a purported appointment |
| s 64B(1) def "act or omission"(a) | item | 1260 | (a) whether before, on or after the commencement of section 64A; and | encoded | s64B(1) definition 132 of act or omission; s64B(1) the appointment is a purported appointment |
| s 64B(1) def "act or omission"(b) | item | 1261 | (b) whether or not under a power conferred by or under an Act or a sub | encoded | s64B(1) definition 132 of act or omission; s64B(1) the appointment is a purported appointment |
| s 64B(1) def "non-citizen" | def | 1262 | non-citizen has the same meaning as in section 64A; | encoded | s64B(1) definition 133 of non-citizen; s64B(1) the appointment is a purported appointment |
| s 64B(1) def "officer" | def | 1263 | officer means a person who was purportedly appointed to a public offic | encoded | s64B(1) definition 134 of officer; s64B(1) the appointment is a purported appointment |
| s 64B(1) def "purported appointment" | def | 1264 | purported appointment means a purported appointment of a non-citizen t | fork F12 | s64B(1) definition 135 of purported appointment; s64B(1) first day of the period of a purported appointment; s64B(1) last day of the period  |
| s 64B(2) | item | 1265 | (2) A purported appointment has, and is taken to always have had, the  | encoded | s64B(2) the purported appointment has the force and effect it would have had if s 64A had been in operation when it was made |
| s 64B(3) | item | 1266 | (3) An act or omission is not invalid, and is taken to never have been | encoded | s64B(3) the act or omission is ineffective because the officer was not lawfully appointed |
| s 64B(4) | item | 1267-1271 | (4) Without limiting subsection (2) or (3), an act or thing done or om | encoded | s64B(4) the act or thing done in reliance on the purported appointment is ineffective because the officer was not lawfully appointed |
| s 64B(4)(a) | item | 1268 | (a) in reliance, in whole or in part or directly or indirectly, on the | encoded | s64B(4) the act or thing done in reliance on the purported appointment is ineffective because the officer was not lawfully appointed |
| s 64B(4)(b) | item | 1269 | (b) whether or not under a power conferred by or under an Act or a sub | encoded | s64B(4) the act or thing done in reliance on the purported appointment is ineffective because the officer was not lawfully appointed |
| s 64B(4)(c) | item | 1270 | (c) before, on or after the commencement of section 64A— | encoded | s64B(4) the act or thing done in reliance on the purported appointment is ineffective because the officer was not lawfully appointed |
| s 64B(5) | item | 1272 | (5) The acts and things referred to in subsection (4) include (but are | encoded | s64B(5) the act or thing is one the acts and things referred to in subsection (4) include |
| s 64B(5)(a) | item | 1273 | (a) a judgment or order of a court or an order of a tribunal; and | encoded | s64B(5) the act or thing is one the acts and things referred to in subsection (4) include |
| s 64B(5)(b) | item | 1274 | (b) the issue of a warrant, summons or other process. | encoded | s64B(5) the act or thing is one the acts and things referred to in subsection (4) include |
| s 64B(6) | item | 1275 | (6) For the purposes of a proceeding before a court or tribunal, the f | encoded | s64B(6) the fact that the officer was not lawfully appointed is to be disregarded in determining the question |
| s 64B(6)(a) | item | 1276 | (a) evidence obtained (directly or indirectly) as a result of an act o | encoded | s64B(6) the fact that the officer was not lawfully appointed is to be disregarded in determining the question |
| s 64B(6)(b) | item | 1277 | (b) a right, privilege, obligation or liability has been acquired, acc | encoded | s64B(6) the fact that the officer was not lawfully appointed is to be disregarded in determining the question |
| s 65 | section | 1278-1280 | 65 Regulations | inert (2) | machinery: regulation-making power |
| s 65(1) | item | 1281 | (1) The Governor in Council may make regulations for or with respect t | inert (2) | machinery: regulation-making power |
| s 65(1)(a) | item | 1282 | (a) exempting an entity or a class of entity or a document (including  | inert (2) | machinery: regulation-making power |
| s 65(1)(b) | item | 1283 | (b) prescribing matters relating to the location or format of electron | inert (2) | machinery: regulation-making power |
| s 65(1)(c) | item | 1284 | (c) any matter or thing required to be prescribed by this Act or neces | inert (2) | machinery: regulation-making power |
| s 65(2) | item | 1285 | (2) The regulations may— | inert (2) | machinery: regulation-making power |
| s 65(2)(a) | item | 1286 | (a) be of general or limited application; | inert (2) | machinery: regulation-making power |
| s 65(2)(b) | item | 1287 | (b) differ according to differences in time, place or circumstance; | inert (2) | machinery: regulation-making power |
| s 65(2)(c) | item | 1288 | (c) apply to different classes of entities or documents; | inert (2) | machinery: regulation-making power |
| s 65(2)(d) | item | 1289 | (d) leave any matter or thing to be from time to time determined or ap | inert (2) | machinery: regulation-making power |
| s 65(2)(e) | item | 1290 | (e) confer powers or discretions or impose duties on any specified ent | inert (2) | machinery: regulation-making power |
| s 65(2)(f) | item | 1291 | (f) provide in a specified case or class of cases for the exemption of | inert (2) | machinery: regulation-making power |
| s 65(2)(f)(i) | item | 1292 | (i) whether unconditionally or on specified conditions; and | inert (2) | machinery: regulation-making power |
| s 65(2)(f)(ii) | item | 1293 | (ii) either wholly or to the extent specified in the regulations. | inert (2) | machinery: regulation-making power |
| s 65(3) | item | 1294 | (3) A power conferred by this Act to make regulations may be exercised | inert (2) | machinery: regulation-making power |
| s 65(3)(a) | item | 1295 | (a) in relation to— | inert (2) | machinery: regulation-making power |
| s 65(3)(a)(i) | item | 1296 | (i) all cases to which the power extends; or | inert (2) | machinery: regulation-making power |
| s 65(3)(a)(ii) | item | 1297 | (ii) all those cases subject to specified exceptions; or | inert (2) | machinery: regulation-making power |
| s 65(3)(a)(iii) | item | 1298 | (iii) any specified case or class of case; and | inert (2) | machinery: regulation-making power |
| s 65(3)(b) | item | 1299 | (b) so as to make, in relation to any provision for which the power is | inert (2) | machinery: regulation-making power |
| s 65(3)(b)(i) | item | 1300 | (i) the same provision for all cases; or | inert (2) | machinery: regulation-making power |
| s 65(3)(b)(ii) | item | 1301 | (ii) different provisions for different cases or classes of case; or | inert (2) | machinery: regulation-making power |
| s 65(3)(b)(iii) | item | 1302 | (iii) different provisions for the same case or class of case for diff | inert (2) | machinery: regulation-making power |
| Sch 1 | schedule | 1303-1305 | Schedule 1—Style changes | inert (1) | heading |
| Sch 1 head note | note | 1307 | Section 54A | inert (1) | a note that points to another provision and creates no rule |
| Sch 1 cl 1 | clause | 1308 | 1 For an expression specified in column 1 of the Table substitute the  | encoded | Sch 1 cl 1 the expression substituted for the expression |
| Sch 1 table | table | 1309 | Table | encoded | Sch 1 cl 1 the expression substituted for the expression |
| Sch 1 table header | tablerow | 1310 | \| column 1 old style \| column 2 new style \| | encoded | Sch 1 cl 1 the expression substituted for the expression |
| Sch 1 table header#2 | tablerow | 1311 | \| Sub-division \| Subdivision \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 1 |
| Sch 1 table header#3 | tablerow | 1312 | \| sub-section \| subsection \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 2 |
| Sch 1 table header#4 | tablerow | 1313 | \| sub-paragraph \| subparagraph \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 3 |
| Sch 1 table header#5 | tablerow | 1314 | \| sub-sub-paragraph \| sub-subparagraph \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 4 |
| Sch 1 table header#6 | tablerow | 1315 | \| sub-clause \| subclause \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 5 |
| Sch 1 table header#7 | tablerow | 1316 | \| sub-sub-clause \| sub-subclause \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 6 |
| Sch 1 table header#8 | tablerow | 1317 | \| sub-regulation \| subregulation \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 7 |
| Sch 1 table header#9 | tablerow | 1318 | \| sub-rule \| subrule \| | encoded | Sch 1 cl 1 the expression substituted for the expression; Sch 1 table row 8 |
| Sch 1 cl 2 | clause | 1319-1320 | 2 For a Part, Division or Subdivision heading that is not formatted us | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 2A | clause | 1321-1322 | 2A In the case of a Schedule that has a heading designating the number | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 2B | clause | 1323-1324 | 2B For a Schedule heading (other than a Schedule heading to which clau | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 2C | clause | 1325-1326 | 2C In the case of a Form that has a heading designating the number of  | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 3 | clause | 1327 | 3 For a note at the foot of a provision that is not formatted under th | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 4 | clause | 1328 | 4 In a note that is reformatted in accordance with clause 3 omit the e | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 5 | clause | 1329 | 5 Omit any double quotation marks around a defined word or defined exp | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 5 note | note | 1330-1331 | Note Defined words and expressions are printed in bold italics. | inert (1) | a note that points to another provision and creates no rule |
| Sch 1 cl 6 | clause | 1332 | 6 Omit the full stop immediately following the provision number at the | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 7 | clause | 1333-1334 | 7 For a title of an Act or a statutory rule that is not formatted in i | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 cl 8 | clause | 1335-1336 | 8 Omit the line appearing at the end of a Part indicating the end of t | encoded | Sch 1 cl 2 to 8 the style change |
| Sch 1 blank | blank | 1337-1338 | * * * * * | repealed or blank in this text | the text shows only the marker `* * * * *` (side note: [Side note: Sch. repealed by No. 104/1994 s. 35(Sch. 2 item 3.2).]) |
| Endnotes rule | endnote-head | 1339 | ═══════════════ | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes | endnote-head | 1341 | Endnotes | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1 | endnote | 1343 | 1 General information | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: See www.legislation.vic.gov.au for Victo | endnote-part | 1344-1345 | See www.legislation.vic.gov.au for Victorian Bills, Acts and current a | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: INTERPRETATION OF LEGISLATION ACT 1984 ( | endnote-part | 1346 | INTERPRETATION OF LEGISLATION ACT 1984 (ILA) | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: Style changes | endnote-part | 1347-1348 | Style changes Section 54A of the ILA authorises the making of the styl | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: References to ILA s. 39B | endnote-part | 1349-1350 | References to ILA s. 39B Sidenotes which cite ILA s. 39B refer to sect | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: Interpretation | endnote-part | 1351-1352 | Interpretation As from 1 January 2001, amendments to section 36 of the | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Headings | endnote-part | 1353-1354 | • Headings All headings included in an Act which is passed on or after | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Examples, diagrams or notes | endnote-part | 1355-1356 | • Examples, diagrams or notes All examples, diagrams or notes included | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Punctuation | endnote-part | 1357-1358 | • Punctuation All punctuation included in an Act which is passed on or | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Provision numbers | endnote-part | 1359-1360 | • Provision numbers All provision numbers included in an Act form part | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Location of "legislative items" | endnote-part | 1361-1362 | • Location of "legislative items" A "legislative item" is a penalty, a | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 1: • Other material | endnote-part | 1363-1364 | • Other material Any explanatory memorandum, table of provisions, endn | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2 | endnote | 1366 | 2 Table of Amendments | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: This publication incorporates  | endnote-part | 1367 | This publication incorporates amendments made to the Interpretation of | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: –––––––––––––––––––––––––––––– | endnote-part | 1368 | ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Further Amendment) Act 1985, No. 10214/1985 | endnote-part | 1369-1372 | Interpretation of Legislation (Further Amendment) Act 1985, No. 10214/ | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Penalties and Sentences Act 1985, No. 10260/1985 | endnote-part | 1373-1376 | Penalties and Sentences Act 1985, No. 10260/1985 \| Assent Date: \| 10.1 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 1986, No. 4/1986 | endnote-part | 1377-1380 | Interpretation of Legislation (Amendment) Act 1986, No. 4/1986 \| Assen | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Constitution (British Subjects) Act 1986, No. 61/1986 | endnote-part | 1381-1384 | Constitution (British Subjects) Act 1986, No. 61/1986 \| Assent Date: \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Local Government (Consequential Provisions) Act 1989, No. 12/1989 (as amended by No. 13/1990) | endnote-part | 1385-1388 | Local Government (Consequential Provisions) Act 1989, No. 12/1989 (as  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Magistrates' Court Act 1989, No. 51/1989 | endnote-part | 1389-1392 | Magistrates' Court Act 1989, No. 51/1989 \| Assent Date: \| 14.6.89 \| \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Children and Young Persons Act 1989, No. 56/1989 | endnote-part | 1393-1396 | Children and Young Persons Act 1989, No. 56/1989 \| Assent Date: \| 14.6 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Magistrates' Court (Consequential Amendments) Act 1989, No. 57/1989 | endnote-part | 1397-1400 | Magistrates' Court (Consequential Amendments) Act 1989, No. 57/1989 \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Water (Consequential Amendments) Act 1989, No. 81/1989 | endnote-part | 1401-1404 | Water (Consequential Amendments) Act 1989, No. 81/1989 \| Assent Date:  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Corporations (Victoria) Act 1990, No. 80/1990 | endnote-part | 1405-1408 | Corporations (Victoria) Act 1990, No. 80/1990 \| Assent Date: \| 11.12.9 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 1991, No. 6/1991 | endnote-part | 1409-1412 | Interpretation of Legislation (Amendment) Act 1991, No. 6/1991 \| Assen | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Sentencing Act 1991, No. 49/1991 | endnote-part | 1413-1416 | Sentencing Act 1991, No. 49/1991 \| Assent Date: \| 25.6.91 \| \| Commence | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Financial Institutions (Victoria) Act 1992, No. 48/1992 | endnote-part | 1417-1420 | Financial Institutions (Victoria) Act 1992, No. 48/1992 \| Assent Date: | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 1993, No. 95/1993 | endnote-part | 1421-1424 | Interpretation of Legislation (Amendment) Act 1993, No. 95/1993 \| Asse | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Public Holidays Act 1993, No. 119/1993 | endnote-part | 1425-1428 | Public Holidays Act 1993, No. 119/1993 \| Assent Date: \| 7.12.93 \| \| Co | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Financial Management Act 1994, No. 18/1994 | endnote-part | 1429-1432 | Financial Management Act 1994, No. 18/1994 \| Assent Date: \| 10.5.94 \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Subordinate Legislation Act 1994, No. 104/1994 | endnote-part | 1433-1436 | Subordinate Legislation Act 1994, No. 104/1994 \| Assent Date: \| 13.12. | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Constitution (Amendment) Act 1994, No. 108/1994 | endnote-part | 1437-1440 | Constitution (Amendment) Act 1994, No. 108/1994 \| Assent Date: \| 20.12 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Constitution (Court of Appeal) Act 1994, No. 109/1994 | endnote-part | 1441-1444 | Constitution (Court of Appeal) Act 1994, No. 109/1994 \| Assent Date: \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Consumer Credit (Victoria) Act 1995, No. 41/1995 | endnote-part | 1445-1448 | Consumer Credit (Victoria) Act 1995, No. 41/1995 \| Assent Date: \| 14.6 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Miscellaneous Acts (Omnibus Amendments) Act 1995, No. 100/1995 | endnote-part | 1449-1452 | Miscellaneous Acts (Omnibus Amendments) Act 1995, No. 100/1995 \| Assen | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Friendly Societies (Victoria) Act 1996, No. 83/1996 | endnote-part | 1453-1456 | Friendly Societies (Victoria) Act 1996, No. 83/1996 \| Assent Date: \| 2 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 1997, No. 6/1997 | endnote-part | 1457-1460 | Interpretation of Legislation (Amendment) Act 1997, No. 6/1997 \| Assen | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: National Electricity (Victoria) Act 1997, No. 29/1997 | endnote-part | 1461-1464 | National Electricity (Victoria) Act 1997, No. 29/1997 \| Assent Date: \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Law and Justice Legislation (Further Amendment) Act 1997, No. 84/1997 | endnote-part | 1465-1468 | Law and Justice Legislation (Further Amendment) Act 1997, No. 84/1997  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Gas Pipelines Access (Victoria) Act 1998, No. 31/1998 | endnote-part | 1469-1472 | Gas Pipelines Access (Victoria) Act 1998, No. 31/1998 \| Assent Date: \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Financial Sector Reform (Victoria) Act 1999, No. 37/1999 | endnote-part | 1473-1476 | Financial Sector Reform (Victoria) Act 1999, No. 37/1999 \| Assent Date | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Crimes at Sea Act 1999, No. 56/1999 | endnote-part | 1477-1480 | Crimes at Sea Act 1999, No. 56/1999 \| Assent Date: \| 21.12.99 \| \| Comm | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 2000, No. 60/2000 | endnote-part | 1481-1484 | Interpretation of Legislation (Amendment) Act 2000, No. 60/2000 \| Asse | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Corporations (Consequential Amendments) Act 2001, No. 44/2001 | endnote-part | 1485-1488 | Corporations (Consequential Amendments) Act 2001, No. 44/2001 \| Assent | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law (Further Revision) Act 2002, No. 11/2002 | endnote-part | 1489-1492 | Statute Law (Further Revision) Act 2002, No. 11/2002 \| Assent Date: \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Criminal Justice Legislation (Miscellaneous Amendments) Act 2002, No. 35/2002 | endnote-part | 1493-1496 | Criminal Justice Legislation (Miscellaneous Amendments) Act 2002, No.  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Fair Trading (Amendment) Act 2003, No. 30/2003 (as amended by No. 106/2003) | endnote-part | 1497-1500 | Fair Trading (Amendment) Act 2003, No. 30/2003 (as amended by No. 106/ | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Amendment) Act 2004, No. 61/2004 | endnote-part | 1501-1504 | Interpretation of Legislation (Amendment) Act 2004, No. 61/2004 \| Asse | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: National Electricity (Victoria) Act 2005, No. 8/2005 | endnote-part | 1505-1508 | National Electricity (Victoria) Act 2005, No. 8/2005 \| Assent Date: \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation (Further Amendment) Act 2006, No. 13/2006 | endnote-part | 1509-1512 | Interpretation of Legislation (Further Amendment) Act 2006, No. 13/200 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law (Further Revision) Act 2006, No. 29/2006 | endnote-part | 1513-1516 | Statute Law (Further Revision) Act 2006, No. 29/2006 \| Assent Date: \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation Amendment Act 2007, No. 2/2007 | endnote-part | 1517-1520 | Interpretation of Legislation Amendment Act 2007, No. 2/2007 \| Assent  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Motor Car Traders Amendment Act 2008, No. 4/2008 | endnote-part | 1521-1524 | Motor Car Traders Amendment Act 2008, No. 4/2008 \| Assent Date: \| 4.3. | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: National Gas (Victoria) Act 2008, No. 30/2008 | endnote-part | 1525-1528 | National Gas (Victoria) Act 2008, No. 30/2008 \| Assent Date: \| 17.6.08 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Coroners Act 2008, No. 77/2008 | endnote-part | 1529-1532 | Coroners Act 2008, No. 77/2008 \| Assent Date: \| 11.12.08 \| \| Commencem | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Courts Legislation Amendment (Costs Court and Other Matters) Act 2008, No. 78/2008 | endnote-part | 1533-1536 | Courts Legislation Amendment (Costs Court and Other Matters) Act 2008, | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Sheriff Act 2009, No. 9/2009 | endnote-part | 1537-1540 | Sheriff Act 2009, No. 9/2009 \| Assent Date: \| 24.3.09 \| \| Commencement | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Criminal Procedure Amendment (Consequential and Transitional Provisions) Act 2009, No. 68/2009 | endnote-part | 1541-1544 | Criminal Procedure Amendment (Consequential and Transitional Provision | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Amendment (Evidence Consequential Provisions) Act 2009, No. 69/2009 | endnote-part | 1545-1548 | Statute Law Amendment (Evidence Consequential Provisions) Act 2009, No | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Offshore Petroleum and Greenhouse Gas Storage Act 2010, No. 10/2010 | endnote-part | 1549-1552 | Offshore Petroleum and Greenhouse Gas Storage Act 2010, No. 10/2010 \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Credit (Commonwealth Powers) Act 2010, No. 11/2010 | endnote-part | 1553-1556 | Credit (Commonwealth Powers) Act 2010, No. 11/2010 \| Assent Date: \| 30 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Amendment (National Health Practitioner Regulation) Act 2010, No. 13/2010 | endnote-part | 1557-1560 | Statute Law Amendment (National Health Practitioner Regulation) Act 20 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Further Amendment Act 2010, No. 64/2010 | endnote-part | 1561-1564 | Justice Legislation Further Amendment Act 2010, No. 64/2010 \| Assent D | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Bail Amendment Act 2010, No. 70/2010 | endnote-part | 1565-1568 | Bail Amendment Act 2010, No. 70/2010 \| Assent Date: \| 19.10.10 \| \| Com | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Fair Trading Amendment (Australian Consumer Law) Act 2010, No. 72/2010 | endnote-part | 1569-1572 | Fair Trading Amendment (Australian Consumer Law) Act 2010, No. 72/2010 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Children's Services Amendment Act 2011, No. 80/2011 | endnote-part | 1573-1576 | Children's Services Amendment Act 2011, No. 80/2011 \| Assent Date: \| 2 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Australian Consumer Law and Fair Trading Act 2012, No. 21/2012 | endnote-part | 1577-1580 | Australian Consumer Law and Fair Trading Act 2012, No. 21/2012 \| Assen | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Revision Act 2012, No. 43/2012 | endnote-part | 1581-1584 | Statute Law Revision Act 2012, No. 43/2012 \| Assent Date: \| 27.6.12 \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Resources Legislation Amendment (General) Act 2012, No. 64/2012 | endnote-part | 1585-1588 | Resources Legislation Amendment (General) Act 2012, No. 64/2012 \| Asse | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Electronic Conveyancing (Adoption of National Law) Act 2013, No. 7/2013 | endnote-part | 1589-1592 | Electronic Conveyancing (Adoption of National Law) Act 2013, No. 7/201 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Rail Safety National Law Application Act 2013, No. 22/2013 | endnote-part | 1593-1596 | Rail Safety National Law Application Act 2013, No. 22/2013 \| Assent Da | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Heavy Vehicle National Law Application Act 2013, No. 30/2013 | endnote-part | 1597-1600 | Heavy Vehicle National Law Application Act 2013, No. 30/2013 \| Assent  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Marine (Domestic Commercial Vessel National Law Application) Act 2013, No. 36/2013 | endnote-part | 1601-1604 | Marine (Domestic Commercial Vessel National Law Application) Act 2013, | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Consumer Affairs Legislation Amendment Act 2013, No. 57/2013 | endnote-part | 1605-1608 | Consumer Affairs Legislation Amendment Act 2013, No. 57/2013 \| Assent  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Revision Act 2013, No. 70/2013 | endnote-part | 1609-1612 | Statute Law Revision Act 2013, No. 70/2013 \| Assent Date: \| 19.11.13 \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Legal Profession Uniform Law Application Act 2014, No. 17/2014 (as amended by No. 8/2015) | endnote-part | 1613-1616 | Legal Profession Uniform Law Application Act 2014, No. 17/2014 (as ame | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Honorary Justices Act 2014, No. 32/2014 | endnote-part | 1617-1620 | Honorary Justices Act 2014, No. 32/2014 \| Assent Date: \| 13.5.14 \| \| C | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Courts Legislation Miscellaneous Amendments Act 2014, No. 62/2014 | endnote-part | 1621-1624 | Courts Legislation Miscellaneous Amendments Act 2014, No. 62/2014 \| As | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Inquiries Act 2014, No. 67/2014 | endnote-part | 1625-1628 | Inquiries Act 2014, No. 67/2014 \| Assent Date: \| 23.9.14 \| \| Commencem | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Interpretation of Legislation Amendment Act 2015, No. 5/2015 | endnote-part | 1629-1632 | Interpretation of Legislation Amendment Act 2015, No. 5/2015 \| Assent  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Revision Act 2015, No. 21/2015 | endnote-part | 1633-1636 | Statute Law Revision Act 2015, No. 21/2015 \| Assent Date: \| 16.6.15 \|  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Further Amendment Act 2016, No. 3/2016 | endnote-part | 1637-1640 | Justice Legislation Further Amendment Act 2016, No. 3/2016 \| Assent Da | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Amendment (Court Security, Juries and Other Matters) Act 2017, No. 38/2017 | endnote-part | 1641-1644 | Justice Legislation Amendment (Court Security, Juries and Other Matter | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Parks and Crown Land Legislation Amendment Act 2017, No. 53/2017 | endnote-part | 1645-1648 | Parks and Crown Land Legislation Amendment Act 2017, No. 53/2017 \| Ass | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Oaths and Affirmations Act 2018, No. 6/2018 | endnote-part | 1649-1652 | Oaths and Affirmations Act 2018, No. 6/2018 \| Assent Date: \| 27.2.18 \| | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Amendment (System Enhancements and Other Matters) Act 2021, No. 11/2021 | endnote-part | 1653-1656 | Justice Legislation Amendment (System Enhancements and Other Matters)  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Amendment (Criminal Procedure Disclosure and Other Matters) Act 2022, No. 1/2022 | endnote-part | 1657-1660 | Justice Legislation Amendment (Criminal Procedure Disclosure and Other | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Regulatory Legislation Amendment (Reform) Act 2022, No. 13/2022 | endnote-part | 1661-1664 | Regulatory Legislation Amendment (Reform) Act 2022, No. 13/2022 \| Asse | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statute Law Amendment (References to the Sovereign) Act 2023, No. 25/2023 | endnote-part | 1665-1668 | Statute Law Amendment (References to the Sovereign) Act 2023, No. 25/2 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Statewide Treaty Act 2025, No. 45/2025 | endnote-part | 1669-1672 | Statewide Treaty Act 2025, No. 45/2025 \| Assent Date: \| 13.11.25 \| \| C | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 2: Justice Legislation Amendment (Police and Other Matters) Act 2025, No. 55/2025 | endnote-part | 1673-1676 | Justice Legislation Amendment (Police and Other Matters) Act 2025, No. | encoded | endnote 2 day sections 57, 58, 60 and 61 of Act No. 55/2025 came into operation |
| Endnotes 2: ––––––––––––––––––––––––––––––#2 | endnote-part | 1677 | ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnotes 3 | endnote | 1679 | 3 Explanatory details | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) | endnote-block | 1681-1682 | [Endnote 1] S. 32: Section 4 of the Interpretation of Legislation (Ame | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) s 4 | endnote-sec | 1684 | 4 Validation of existing subordinate instruments | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) s 4(1) | item | 1685 | (1) Subject to subsection (4) and despite anything to the contrary in  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) s 4(2) | item | 1686 | (2) The Legal and Constitutional Committee may report a failure referr | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) s 4(3) | item | 1687 | (3) Section 32 of the Interpretation of Legislation Act 1984 (as amend | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 1 (quoted text) s 4(4) | item | 1688 | (4) A question concerning the validity of a subordinate instrument ari | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 2 (quoted text) | endnote-block | 1690-1691 | [Endnote 2] S. 38 def. of Court of Appeal: Sections 29 and 30 of the C | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 2 (quoted text) s 29 | endnote-sec | 1693 | 29 Proceedings before Full Court | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 2 (quoted text) s 29(1) | item | 1694 | (1) The Constitution Act 1975, the Supreme Court Act 1986 and the Crim | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 2 (quoted text) s 29(2) | item | 1695 | (2) If the Court of Appeal so orders, anything required to be done by  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 2 (quoted text) s 30 | endnote-sec | 1697-1698 | 30 References to Full Court A reference in an Act or an instrument mad | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) | endnote-block | 1700-1701 | [Endnote 3] S. 44(5): Section 43 of the Supreme Court Act 1986, No. 11 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) s 43 | endnote-sec | 1702-1708 | 43 Standard time in Victoria Note Under section 8AA of the National Me | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) s 43(1) | item | 1705-1706 | (1) Standard time throughout Victoria is the time that is 10 hours in  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) s 43(2) | item | 1709-1712 | (2) If— the time is standard time as provided in subsection (1) unless | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) s 43(2)(a) | item | 1710 | (a) an expression of time occurs in an instrument; or | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 3 (quoted text) s 43(2)(b) | item | 1711 | (b) the doing or not doing of anything at a certain time has an effect | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) | endnote-block | 1714-1715 | [Endnote 4] S. 57: Section 11 of the Crimes at Sea Act 1999, No. 56/19 | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) s 11 | endnote-sec | 1717 | 11 Application of repeal and amendments | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) s 11(1) | item | 1718 | (1) In this section commencement day means the day on which this Act c | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) s 11(2) | item | 1719 | (2) Although section 9 repeals the Crimes (Offences at Sea) Act 1978,  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) s 11(3) | item | 1720 | (3) The amendments of the Interpretation of Legislation Act 1984 made  | inert (1) | endnote: does not form part of the Act (s 36(3)) |
| Endnote 4 (quoted text) s 11(4) | item | 1721 | (4) For the purposes of this section, if an act or omission is alleged | inert (1) | endnote: does not form part of the Act (s 36(3)) |

## Fork register

Each entry gives the provision, the readings seen, the one taken, and the text that licenses it.
The conventions for `JUST FALSE` and `NOTHING` are those of the Commons guide's rulings of 4 and 5 November 2026, and are summarised under F14.

**F1. Periods of months or years reckoned from a day (s 44(1), (6)(b), (c)).**
Reading A: count the whole calendar months (or twelve-month years) starting with the month that begins on the day after the day counted from, and take the last day of the last month that fits, so one month from 31 January 2024 ends on 29 February 2024.
Reading B: the day with the same number in the n-th following month (or year), which does not exist when that month is shorter.
Taken: both readings are computed, and the answer is given only where they give the same day; where they differ or reading B has no day, the answer is NOTHING.
Licence: s 44(1) leaves out the day counted from; s 44(6)(b) and (c) say that a month is a calendar month and a year is a period of twelve months; no provision says on which day a period of months or years ends.
Rules: `s44(1),(6)(b) last day of n calendar months reckoned from a day` and `s44(1),(6)(c) last day of n years reckoned from a day`.
Cases: two months from 31 December 2025, one month from 31 January 2024 and one year from 29 February 2024 are NOTHING; one month from 15 January 2025 is 15 February 2025.

**F2. Weeks, and periods expressed with "after" or "before" a day (s 44(1), (2)).**
Reading: the text speaks only of a period "expressed to begin on, or to be reckoned from" a day and one "expressed to end on, or to be reckoned to" a day.
Taken: a period in weeks, and a period expressed with "after" or "before" a day, are not covered, and the functions answer NOTHING.
Licence: the text has no rule for them; the word "week" does not occur in it.

**F3. Whether the extension in s 44(3) depends on the unit.**
Readings: the extension applies to a time limited for doing an act or thing whatever its unit; it applies only to a time counted in days.
Taken: it applies whatever the unit, and not to a time that is not limited for the doing of an act or thing (an input says which).
Licence: the wording of s 44(3) ("the time limited by an Act or subordinate instrument for the doing of any act or thing") mentions no unit.
A holiday is a Saturday, a Sunday, or a day in the list of public holidays the caller supplies (s 44(4)(a), (b)).

**F4. "Paragraphs (e) to (f)" in s 14(2)(g).**
Readings: paragraphs (e) and (f) only; or (e), (ea) and (f), in the order printed.
Taken: (e), (ea) and (f).
Licence: the text prints paragraph (ea) between (e) and (f), and does not say whether a range spans an inserted paragraph.

**F5. Headings to Orders and Parts of Orders (s 36(2B)) and the list in s 36(3).**
Readings: s 36(3) refers to "subsection (1), (1A) or (2A)" and not to (2B); the headings in (2B) are excluded by (3), or they form part under (2B) on its own words.
Taken: s 36(2B) states its own rule, and s 36(3) is encoded as printed.
Licence: s 36(2B) says that those headings "form part of the subordinate instrument if" its conditions hold.

**F6. Powers named in s 41(3).**
Readings: s 41(3) names the power "to make an appointment to act in the office, or to remove or suspend"; the same rule applies to the other powers in s 41(1), or only to the three it names.
Taken: the three named powers; for a power to appoint a person to perform a particular function on a particular occasion and for any other related power the answer is NOTHING.
Licence: s 41(3) names three powers and no others.

**F7. Section 62(2)(a) to (c): no connector.**
Readings: all three conditions must hold; any one is enough.
Taken: all three must hold.
Licence: the text prints neither "and" nor "or" between (a), (b) and (c); the paragraphs describe one version (the format, the opening words, and the closing words of each page).

**F8. The age of 18 years in s 55(2)(b) and (c).**
Reading: a person attains an age on the anniversary of the birth.
Taken: the eighteenth anniversary of the birth is the day with the same date; for a person born on 29 February there is none in a year without a 29 February, and the answer is NOTHING.
Other reading: a person born on 29 February attains the age on 28 February, or on 1 March, in a year without a 29 February.
Licence: the text defines no rule for attaining an age.

**F9. "The first anniversary of the passing of the Act" (s 10A(3), (4)).**
Taken: the day with the same date one year on; for an Act passed on 29 February the answer is NOTHING in a year without a 29 February.
Other reading: the anniversary is 28 February, or 1 March, in a year without a 29 February.
Licence: the text says "the first anniversary" and does not define it.

**F10. Delivery "in the ordinary course of post" (s 49(1)(b), (2)(b)).**
Taken: the day on which the letter would be delivered in the ordinary course of post (or by registered post or certified mail) is asked as an input and returned as the day of deemed service.
Other reading: a fixed number of days after posting, which the text does not print and the encoding does not adopt.
Licence: the text states no period for delivery.

**F11. The offshore area and the coastal waters (s 57(2)(a), (6)(a), (b)).**
Taken: whether a place is within the outer limits of the coastal waters of Victoria, and whether it is within the outer limits of the continental shelf, are separate inputs; neither is derived from the other.
Other reading: derive the coastal waters from the offshore area, or the offshore area from the coastal waters.
Licence: the definitions point to the Coastal Waters (State Powers) Act 1980 and the Offshore Petroleum and Greenhouse Gas Storage Act 2006 of the Commonwealth, which are not among the sources.

**F12. The end of the period of a purported appointment (s 64B(1)).**
Taken: the period ends on the day before the day s 64A came into operation; that day is an input to the rule; the time module holds the day endnote 2 prints for the sections of the amending Act that inserted s 64A (10 December 2025), so the last day is 9 December 2025.
Other reading: ask the day as an input only, with no constant in the time module.
Licence: s 64B(1) says "ending immediately before section 64A came into operation" and the body of the Act does not give that day.
Endnotes do not form part of the Act (s 36(3)).

**F13. Section 41AA(c): the two events on the same day.**
Readings: the acting continues until whichever of the appointer's direction and the filling of the vacancy first occurs; when both occur on the same day neither is first.
Taken: the answer names the tie (`VicBothHappenOnTheSameDay`), and the day of ending is that day.
Licence: the words "whichever first occurs" do not say which when the days are equal.

**F14. Unless-clauses, and conditions that fail.**
Rules of the text that begin "Where", "If" or "When" return `JUST FALSE` when the condition fails, for a question asked in the direction of the rule's consequence whose answer is a Boolean, as the guide's ruling of 5 November 2026 requires; a scope limit with no "only", and a grant limited in its own wording, return `NOTHING` outside the limit.
For an "unless the contrary intention appears" clause (and its variants "unless the context otherwise requires", "unless the Chief Parliamentary Counsel otherwise approves" and "unless the contrary is proved") the guide leaves the choice to each site, with one line per site.
The table below has one line for each site.
Class A: a Boolean question asked in the direction of the rule's consequence; the answer taken when the clause is met is `JUST FALSE` (the section does not give the consequence), and the other reading is `NOTHING`.
Class B: a Boolean question asked in the opposite direction to the rule's consequence ("is the repealed Act revived", "does the repeal affect the proceeding"); the section's own answer is `JUST FALSE` and the answer taken when the clause is met is `NOTHING`, because the text then says nothing about the proposition; the other reading is `JUST TRUE`.
Class C: the answer is not a Boolean (what a reference is read as, a copy, a number, a day); the answer taken when the clause is met is `NOTHING`, and no Boolean other reading exists.
Where one limb of a rule is conditional and the function asks about all the limbs together (s 32(3)(a), (4)(a)), the answer is `NOTHING` when the conditional limb does not apply.
For a class B question, the answer when the section's own "where" or "if" condition fails is `NOTHING` as well (s 13(2), s 15(1), s 26(2), s 29(1)), for the same reason.

| provision | function | answer when the clause is met | other reading |
| --- | --- | --- | --- |
| s44(5) | `s44(5) hours ahead of Coordinated Universal Time that an expression of time means` | NOTHING | none: the answer is not a Boolean |
| s49 | `s49 service by post is deemed effected` | JUST FALSE | NOTHING |
| s49 | `s49 day on which service by post is deemed effected` | NOTHING | none: the answer is not a Boolean |
| s4(1)(a) | `s4(1)(a) the provisions of this Act extend and apply to the enactment` | JUST FALSE | NOTHING |
| s13(2) | `s13(2) the power may be exercised after the passing and before the commencement` | JUST FALSE | NOTHING |
| s13(2) | `s13(2) the exercise of the power confers a right or imposes an obligation before the commencement` | NOTHING | JUST TRUE |
| s14(1) | `s14(1) the Act or provision that the ending Act or provision had repealed is construed as revived` | NOTHING | JUST TRUE |
| s14(2)(c)-(f) | `s14(2)(c)-(f) the repeal, amendment, expiry or lapsing revives or affects the thing` | NOTHING | JUST TRUE |
| s14(2)(g) | `s14(2)(g) the repeal, amendment, expiry or lapsing affects an investigation, legal proceeding or remedy` | NOTHING | JUST TRUE |
| s14(2) | `s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed` | JUST FALSE | NOTHING |
| s14(2A) | `s14(2A) the repeal, expiry or lapsing of the provision ends the effect it had` | NOTHING | JUST TRUE |
| s15(1) | `s15(1) the ending of the amending Act or provision affects the direct amendments` | NOTHING | JUST TRUE |
| s16(a) | `s16(a) a reference to the repealed Act or provision is construed as a reference to the re-enacted Act or provision` | JUST FALSE | NOTHING |
| s16(b) | `s16(b) the instrument made or thing done has effect as if made or done under the re-enacted Act or provision` | JUST FALSE | NOTHING |
| s17(1) | `s17(1) a reference in an Act to another enactment is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s17(1A) | `s17(1A) a reference in an Act to a provision that has been renumbered or relocated is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s18 | `s18 the reference is construed as a reference to one contained in a subordinate instrument made under that Act` | JUST FALSE | NOTHING |
| s19(1) | `s19(1) a reference to a unit by number is construed as a reference to the unit` | NOTHING | none: the answer is not a Boolean |
| s20 | `s20 the division at a position is within the portion cited` | JUST FALSE | NOTHING |
| s21(1) | `s21(1) a reference in an old Act is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s21(2) | `s21(2) a reference to the Legislative Council in an old Act is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s21(3) | `s21(3) a reference to naval or military forces or service includes` | JUST FALSE | NOTHING |
| s21A(1) | `s21A(1) the reprint of the Act is as amended` | JUST FALSE | NOTHING |
| s23 | `s23 an expression in the instrument has the same meaning as in the Act conferring the power` | JUST FALSE | NOTHING |
| s26(2) | `s26(2) the power may be exercised after the making and before the commencement` | JUST FALSE | NOTHING |
| s26(2) | `s26(2) the exercise of the power confers a right or imposes an obligation before the commencement` | NOTHING | JUST TRUE |
| s27 | `s27 the power to make the instrument includes a power to repeal or amend it` | JUST FALSE | NOTHING |
| s28(1) | `s28(1) the instrument or provision that the ending instrument or provision had repealed is construed as revived` | NOTHING | JUST TRUE |
| s28(2)(c)-(f) | `s28(2)(c)-(f) the repeal, amendment, expiry or lapsing revives or affects the thing` | NOTHING | JUST TRUE |
| s28(2)(g) | `s28(2)(g) the repeal, amendment, expiry or lapsing affects an investigation, legal proceeding or remedy` | NOTHING | JUST TRUE |
| s28(2) | `s28(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the instrument had not been repealed` | JUST FALSE | NOTHING |
| s28(2A) | `s28(2A) the repeal, expiry or lapsing of the provision ends the effect it had` | NOTHING | JUST TRUE |
| s29(1) | `s29(1) the ending of the amending instrument or provision affects the direct amendments` | NOTHING | JUST TRUE |
| s30(a) | `s30(a) a reference to the repealed instrument or provision is construed as a reference to the re-made instrument or provision` | JUST FALSE | NOTHING |
| s30(b) | `s30(b) the instrument made or thing done has effect as if made or done under the re-made instrument or provision` | JUST FALSE | NOTHING |
| s31(1) | `s31(1) a reference in a subordinate instrument to another enactment is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s31(1A) | `s31(1A) a reference in a subordinate instrument to a provision that has been renumbered or relocated is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s32(2) | `s32(2) the subordinate instrument may apply, adopt or incorporate the matter` | JUST FALSE | NOTHING |
| s33(1) | `s33(1) a reference to a unit by number is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s34 | `s34 the division at a position is within the portion cited` | JUST FALSE | NOTHING |
| s37 | `s37 the word includes the other` | JUST FALSE | NOTHING |
| s39 | `s39 the other part of speech or grammatical form has a corresponding meaning` | JUST FALSE | NOTHING |
| s40(a) | `s40(a) the power may be exercised and the duty performed from time to time as occasion requires` | JUST FALSE | NOTHING |
| s40(b) | `s40(b) the person is the one by whom the power may be exercised and the duty shall be performed` | JUST FALSE | NOTHING |
| s41(1) | `s41(1) the power to appoint includes the power` | JUST FALSE | NOTHING |
| s41(3) | `s41(3) the power is only exercisable on the recommendation, or subject to the approval or consent, of that other person or body` | JUST FALSE | NOTHING |
| s41AA | `s41AA the acting appointment has the incident` | JUST FALSE | NOTHING |
| s41A | `s41A the power includes a power to repeal, revoke, rescind, amend, alter or vary an instrument made in the exercise of it` | JUST FALSE | NOTHING |
| s42(1) | `s42(1) the delegate may act upon the delegate's own opinion, belief or state of mind` | JUST FALSE | NOTHING |
| s42A(1) (aa), (a) | `s42A(1) the proposition about the delegation holds` | NOTHING | JUST TRUE |
| s42A(1) (b), (c) | `s42A(1) the proposition about the delegation holds` | JUST FALSE | NOTHING |
| s42A(2) | `s42A(2) a delegation may be made to the person` | JUST FALSE | NOTHING |
| s43 | `s43 the distance is measured in a straight line on a horizontal plane` | JUST FALSE | NOTHING |
| s46(1) | `s46(1) the reference is a reference to the Sovereign for the time being` | JUST FALSE | NOTHING |
| s46(2) | `s46(2) the expression is construed as a reference to` | NOTHING | none: the answer is not a Boolean |
| s46A | `s46A the entity has the status, privileges and immunities of the Crown` | JUST FALSE | NOTHING |
| s47 | `s47 the person is within the reference` | JUST FALSE | NOTHING |
| s48 | `s48 the reference is a reference to the officer, office, locality, jurisdiction, matter or thing in and for or of Victoria` | JUST FALSE | NOTHING |
| s50 | `s50 the authority may make the rule or order` | JUST FALSE | NOTHING |
| s51(1) | `s51(1) the offender is liable to be prosecuted under any or all of those laws` | JUST FALSE | NOTHING |
| s51(1) | `s51(1) the offender is liable to be punished more than once for the same act or omission` | NOTHING | JUST TRUE |
| s52 | `s52 the proceeding or matter must be heard and determined only by or before the Magistrates' Court` | JUST FALSE | NOTHING |
| s53 | `s53 the form used is sufficient in law` | JUST FALSE | NOTHING |
| s54(1) | `s54(1) the copy of the Imperial Act the reference points at` | NOTHING | none: the answer is not a Boolean |
| s54(2) | `s54(2) the reference is a reference to a copy printed by the government printer of that State` | JUST FALSE | NOTHING |
| s64(2) | `s64(2) the document is presumed to be an authorised version` | JUST FALSE | NOTHING |
| s64A | `s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person` | NOTHING | JUST TRUE |

## What the Act turns out to say

Each statement is backed by an assertion in a test or case file, named in brackets.

1. Section 44(1) leaves out the day a period is counted from, so thirty days from 1 January 2026 end on 31 January 2026 (`vic-tests-time.l4`, `s44(1) last day of a period of n days reckoned from a day`; `vic-cases-seat.l4`, `On which day does my period end`). Asserted.
2. Section 44(2) counts the day a period is expressed to end on, and s 44(1) does not count the day a period is expressed to begin on or be reckoned from (`vic-cases-seat.l4`, `Does the day I count from count in my period`). Asserted.
3. Three years from 16 July 2025 end on 16 July 2028, and five years from 15 January 2025 end on 15 January 2030 (`vic-cases-seat.l4`, `On which day does my period end`). Asserted.
4. A period of months or years reckoned from a day has a last day only where the two readings give the same day: two months from 31 December 2025, one month from 31 January 2024 and one year from 29 February 2024 are not answered (`vic-cases-seat.l4`, `On which day does my period end`). Asserted.
5. A period of weeks, and a period "after" a day, are not answered (`vic-cases-seat.l4`, `On which day does my period end`). Asserted.
6. Under s 44(3) and (4), a time limited for doing an act or thing that ends on Sunday 16 July 2028 extends to Monday 17 July 2028, and to Tuesday 18 July 2028 when 17 July 2028 is a listed public holiday (`vic-cases-seat.l4`, `By which day may I do the thing`). Asserted.
7. Thirty days from 1 January 2026 end on Saturday 31 January 2026, and as a time limited for doing something the limit extends to Monday 2 February 2026 (`vic-cases-seat.l4`, `By which day must I do the thing`). Asserted.
8. Under s 44(5), a time in an Act is standard time in Victoria; the number of hours ahead of Coordinated Universal Time is taken from another Act and is returned as supplied, and is not answered when the contrary intention appears (`vic-tests-time.l4`, `s44(5) hours ahead of Coordinated Universal Time that an expression of time means`). Asserted.
9. Under s 44(6)(a), (d) and (e), midnight on a day is the point at which the day ends, the financial year ending in 2026 begins on 1 July 2025 and ends at midnight on 30 June 2026, and a calendar year ends at midnight on 31 December (`vic-tests-time.l4`, `s44(6)(d) first day of the financial year ending on 30 June of a year`). Asserted.
10. Under s 11(1), an Act or provision with a fixed day comes into operation at the beginning of that day (`vic-cases-seat.l4`, `At which moment does the Act or provision come into operation`). Asserted.
11. Under s 11(4), where the provisions of an Act began on 1 March 2020, 1 July 2021 and 1 January 2021, the date of commencement is 1 July 2021 (`vic-tests-time.l4`, `s11(4) date of commencement of an Act or portion whose provisions began on different days`). Asserted.
12. Under s 10A(3) and (4), an Act passed on 10 March 2026 with no commencement provision and no proclaimed day comes into operation on 10 March 2027, and a day proclaimed earlier than that anniversary prevails (`vic-cases-seat.l4`, `On which day does an Act that says nothing about its commencement come into operation`). Asserted.
13. Under ss 12 and 25, a temporary Act, provision or rule expressed to expire on 30 June 2027 continues until the last moment of that day (`vic-cases-seat.l4`, `Until which moment does a temporary Act, provision or rule stay in operation`). Asserted.
14. Under s 24, a subordinate instrument that is not a statutory rule and fixes a day comes into operation at the beginning of that day (`vic-tests-time.l4`, `s24 moment a subordinate instrument that is not a statutory rule comes into operation`). Asserted.
15. Under s 49(1), a document properly addressed, prepaid and posted is deemed served on the day it would be delivered in the ordinary course of post, and there is no answer when it was not prepaid, when the contrary is proved, or when the contrary intention appears (`vic-cases-seat.l4`, `On which day is a document I posted taken to have been served`). Asserted.
16. Under s 14(1), an Act or provision that the ending Act had repealed is not revived (`vic-tests-part1-2.l4`, `s14(1) the Act or provision that the ending Act or provision had repealed is construed as revived`). Asserted.
17. Under s 14(2), a proceeding may be instituted, continued or enforced, and a penalty imposed, as if the Act had not been repealed (`vic-tests-part1-2.l4`, `s14(2) the proceeding may be instituted, continued or enforced, or the penalty imposed, as if the Act had not been repealed`). Asserted.
18. Under s 21(1), a reference to the colony or to the territory or district of Port Phillip in an Act in force on 1 July 1851 is read as a reference to "Victoria" (`vic-tests-part1-2.l4`, `s21(1) a reference in an old Act is construed as a reference to`). Asserted.
19. Under s 36, headings to Chapters, Parts, Divisions and Subdivisions form part of the Act whatever its date; a heading to a section forms part of an Act passed on or after 1 January 2001 and of an earlier Act only if inserted by a later one; a marginal note never forms part (`vic-tests-part4-a.l4`, `s36 the item forms part of the Act or subordinate instrument`; `vic-cases-seat.l4`, `Does the item printed with my Act form part of the Act`). Asserted.
20. Under s 41AA(c), the continued acting ends on the earlier of the appointer's direction and the filling of the vacancy, and the tie is named (`vic-tests-part4-b.l4`, `s41AA(c) which event ends the continued acting`). Asserted.
21. Under s 42C(1), an appointment, and what the person did, is not ineffective only because of an irregularity in the making of the appointment (`vic-cases-seat.l4`, `Is the decision about me ineffective only because the official was irregularly appointed`). Asserted.
22. Under s 45, "may" in conferring a power means the power may be exercised or not, at discretion, and "shall" means it must be exercised (`vic-cases-seat.l4`, `Does the official have a choice whether to use the power`; `Must the official use the power`). Asserted.
23. Under s 46(2), when the Sovereign for the time being is the Queen, a reference to "His Majesty" is read as "Her Majesty" (`vic-tests-part4-c.l4`, `s46(2) the expression is construed as a reference to`). Asserted.
24. Under s 51(1), an offender under two or more laws is liable to be prosecuted under any or all of them and is not liable to be punished more than once for the same act or omission (`vic-tests-part4-c.l4`, `s51(1) the offender is liable to be punished more than once for the same act or omission`). Asserted.
25. Under s 53, a form to the like effect of the prescribed form is sufficient in law unless the contrary intention appears (`vic-cases-seat.l4`, `Is the form I used good enough`). Asserted.
26. Under s 54(1), a reference to an Imperial Act included in a revised edition printed by authority is a reference to that edition, even when the Act is also in the Record Commission edition (`vic-tests-part4-c.l4`, `s54(1) the copy of the Imperial Act the reference points at`). Asserted.
27. Under s 55(2)(a), a person enrolled on 25 January 1984, within the three months immediately before 26 January 1984, is within the reference to a British subject (`vic-tests-part4-c.l4`, `s55(2)(a) the name was enrolled on the day within the three months immediately before 26 January 1984`). Asserted.
28. Under s 64A, that a person is a non-citizen does not of itself affect eligibility for appointment to a public office or disqualify the person (`vic-tests-part5-6.l4`, `s64A the fact that the person is a non-citizen of itself affects eligibility for appointment to a public office or disqualifies the person`). Asserted.
29. Under s 64B(1), a purported appointment is one made from 3 March 1986 until immediately before s 64A came into operation; with 10 December 2025 as that day, the last day of the period is 9 December 2025 (`vic-tests-time.l4`, `s64B(1) last day of the period of a purported appointment`). Asserted.
30. Under s 64B(3), an act or omission is not ineffective because the officer was not lawfully appointed (`vic-tests-part5-6.l4`, `s64B(3) the act or omission is ineffective because the officer was not lawfully appointed`). Asserted.
31. Under s 9(2), an Act may be cited by its number alone until 31 December 1985, and by its calendar year and number from 1 January 1986 (`vic-tests-time.l4`, `s9(2)(e) last day of the period in which an Act is cited by its number only`). Asserted.
32. Under s 10(3), the long title of the Bill for an Act passed on or after 1 September 1985 that does not authorise citation by a short title does not form part of the Act (`vic-tests-part1-2.l4`, `s10(3) the long title of the Bill forms part of the Act`). Asserted.
33. Under s 4(3), a provision expressed to apply only to Acts passed on or after the commencement does not affect the construction of an Act passed before it (`vic-tests-part1-2.l4`, `s4(3) the provision affects the construction of the enactment`). Asserted.

## Worked cases

| case | answer | section | where asserted |
| --- | --- | --- | --- |
| three years from 2025-07-16 | 16 July 2028 (a Sunday); as a time limited for doing an act or thing, extended to Monday 17 July 2028, and to Tuesday 18 July 2028 if 17 July 2028 is a listed public holiday | s 44(1), (6)(c); s 44(3), (4) | `vic-cases-seat.l4`, `On which day does my period end` and `By which day may I do the thing` |
| five years from 2025-01-15 | 15 January 2030 (a Tuesday); no extension | s 44(1), (6)(c) | `vic-cases-seat.l4`, `On which day does my period end` |
| five years from 2025-09-01 | 1 September 2030 (a Sunday); as a time limited for doing an act or thing, extended to Monday 2 September 2030 | s 44(1), (6)(c); s 44(3), (4) | `vic-cases-seat.l4`, `On which day does my period end` and `By which day must I do the thing` |
| thirty days from 2026-01-01 | 31 January 2026 (a Saturday); as a time limited for doing an act or thing, extended to Monday 2 February 2026, and to Tuesday 3 February 2026 if 2 February 2026 is a listed public holiday | s 44(1); s 44(3), (4) | `vic-cases-seat.l4`, `On which day does my period end` and `By which day must I do the thing` |
| two months from 2025-12-31 | not covered: reading A gives 28 February 2026, and reading B has no 31 February; the answer is NOTHING | s 44(1), (6)(b) | `vic-cases-seat.l4`; `vic-tests-time.l4` |
| one month from 2024-01-31 | not covered: reading A gives 29 February 2024, and reading B has no 31 February; the answer is NOTHING | s 44(1), (6)(b) | `vic-cases-seat.l4`; `vic-tests-time.l4` |
| one year from 2024-02-29 | not covered: reading A gives 28 February 2025, and reading B has no 29 February 2025; the answer is NOTHING | s 44(1), (6)(c) | `vic-cases-seat.l4`; `vic-tests-time.l4` |

The text is silent on the weekday of a day and on which days are public holidays; the weekdays above are calendar facts, and the holiday lists in the cases are supplied by the case.

## Cross-references

`vic-provisions.l4` holds 118 entries, one for each Part, section, Schedule and Schedule clause the text prints (identifier, number as printed, heading as printed, line in the text), and a list of every identifier down to paragraph level.
`vic-xrefs.l4` holds 212 rows: 108 rows for references from one provision of this Act to another provision of this Act, which come from 78 citations, since a citation that names several provisions gives one row for each; and 104 rows for references to provisions of other Acts and instruments, from 104 citations.
Each row has a test in `vic-tests-xrefs.l4`: for a reference within this Act, that the identifier cited is in the index and that the row's heading is the heading the index prints; for a reference to another instrument, that the instrument is named.
A reference to another instrument is not resolved here; where a rule needs the fact, it is an input.

The script that builds both modules reads only the text file.
It stops at the rule that opens the endnotes.
It finds a reference by matching the words "section", "subsection", "paragraph", "subparagraph", "Part", "Schedule 1", "the Schedule" and "clause" (singular or plural) followed by a number, letter or list, resolves a relative reference ("subsection (3)", "paragraph (b)") against the provision that holds it, expands a range ("paragraphs (e) to (f)") through the siblings in the order printed, and reads a following "of the ... Act", "... Law" or "... Code" with its year as the name of another instrument.
It gives no row to "this Act", "this section" or "this Part", to "that section" referring back to a section already named, or to the words "the Schedule" where no Schedule number is printed in the citation.

## What the stable binary does not accept

- `x NOT EQUALS y` and `NOT x EQUALS y` do not parse ("unexpected NOT"); the encoding writes `NOT (x EQUALS y)`.
- A one-line `CONSIDER` inside parentheses is rejected; the encoding writes the `CONSIDER` on its own lines.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used (the Commons guide rules them out); a case outside the encoding returns an explicit not-covered value and is asserted.
- No module is read differently by the main build 1.6.110: every module has the same four counts on both builds.

## What check.sh prints

The command, from the encoding folder, is `L4=<stable l4> L4_MAIN=<main l4> ./check.sh`.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
vic-cases-seat.l4                              0        60       0        0         0 |      0        60       0        0  same
vic-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
vic-interpretation-time.l4                     0         0       0        0         0 |      0         0       0        0  same
vic-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
vic-part1-preliminary.l4                       0         0       0        0         0 |      0         0       0        0  same
vic-part2-acts-a.l4                            0         0       0        0         0 |      0         0       0        0  same
vic-part2-acts-b.l4                            0         0       0        0         0 |      0         0       0        0  same
vic-part3-subordinate.l4                       0         0       0        0         0 |      0         0       0        0  same
vic-part4-a-aids.l4                            0         0       0        0         0 |      0         0       0        0  same
vic-part4-b-powers.l4                          0         0       0        0         0 |      0         0       0        0  same
vic-part4-c-general.l4                         0         0       0        0         0 |      0         0       0        0  same
vic-part5-6-schedule1.l4                       0         0       0        0         0 |      0         0       0        0  same
vic-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
vic-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
vic-tests-definitions-cases.l4                 0        23       0        0         0 |      0        23       0        0  same
vic-tests-definitions.l4                       0       409       0        0         0 |      0       409       0        0  same
vic-tests-part1-2.l4                           0       180       0        0         0 |      0       180       0        0  same
vic-tests-part3.l4                             0       154       0        0         0 |      0       154       0        0  same
vic-tests-part4-a.l4                           0       131       0        0         0 |      0       131       0        0  same
vic-tests-part4-b.l4                           0        98       0        0         0 |      0        98       0        0  same
vic-tests-part4-c.l4                           0       143       0        0         0 |      0       143       0        0  same
vic-tests-part5-6.l4                           0        64       0        0         0 |      0        64       0        0  same
vic-tests-time.l4                              0       134       0        0         0 |      0       134       0        0  same
vic-tests-xrefs.l4                             0       212       0        0         0 |      0       212       0        0  same
vic-xrefs.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (25 modules)                             0      1608       0        0           |      0      1608       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `srcrefs.py check --refs --strict` on all `vic-*.l4` files each report: `1115 src: lines, 599 runs, 599 locators, 0 problems`.
The `#ASSERT` lines written in the test and case files total 1608, and 1608 are satisfied.

## What would need doing before this encoding is worth relying on

1. A lawyer who knows Victorian legislation reads the encoding against the authorised version of the Act, not against the converted text.
2. The two readings of a period of months or years (F1) and the neighbouring silences (F2, F8, F9) are settled by the authorities that decide them, and the NOTHING answers replaced where they do.
3. The facts taken from other instruments (the public holidays of the Public Holidays Act 1993, standard time in s 43 of the Supreme Court Act 1986, the commencement of the Australia Acts, the commencement of s 28 of the Miscellaneous Acts (Omnibus Amendments) Act 1995, the Coastal Waters (State Powers) Act 1980 and the Offshore Petroleum and Greenhouse Gas Storage Act 2006) are replaced by the results of those instruments' encodings when they exist.
4. The choices recorded under F14 are reviewed site by site.
5. The seat questions are reworded and extended by someone who talks to people with a time limit, and more questions are added from the rules in layer 1 (for example ss 14 and 28 on what a repeal leaves in place).
6. `check.sh` is run again against the current main build.
