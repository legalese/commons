# NOTES -- keel, row iaw-ssc-k: Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4

**Status (2026-11-04).**
Checked, not proved: `check.sh` and `srcrefs.py check` were run on the files named below, and their numbers are in the section "What was run".
Nothing here is "verified against the official text".
The source is `inputs/ukpga-1992-4.txt`, a plain-text rendering made by a converter script from legislation.gov.uk (point in time 2026-07-08).
It is not the official text, and it has the hazards listed under "The converter text".

**Scope.**
This file covers the keel's own lines: line 1, and lines 4331-4453 (Part XIII, ss 172-177).
The other 5,000-odd lines belong to the nine part agents (`PLAN.md` lists their ranges).
The keel also wrote the shared core (`ssc-core.l4`), which holds nouns and two constants and encodes no provision.

## Files

| file | what it is |
| --- | --- |
| `ssc-core.l4` | the shared nouns; `DECLARE` and two constants; imports `prelude` and `daydate` only |
| `ssc-definitions.l4` | the Act's own definitions in the keel ranges: ss 172, 173, 174 and the rule of reading in s 177(2) |
| `ssc-definitions-tests.l4` | hand-written assertions for those, and a name-resolution smoke test of the core |
| `PLAN.md` | for the part agents: ranges, core names, seams, naming rule |
| `NOTES.md` | this file |
| `PROGRESS.md` | the keel's working log |

## Coverage table (the keel's range)

Every line of the keel range belongs to one row.
"Inert" is used only for the three reasons in the brief: not operative, machinery, repealed or blank.

| lines | provision | disposition | where, or why |
| --- | --- | --- | --- |
| 1 | enacting words | inert (not operative) | no rule |
| 4331-4332 | Part XIII heading, "Interpretation" heading | inert (not operative) | headings |
| 4333 | s 172 heading | inert (not operative) | heading |
| 4334-4336 | s 172(a), (b): territorial waters | encoded | `s 172(a) a reference to Great Britain includes the place`, `s 172(b) a reference to the United Kingdom includes the place` |
| 4337 | s 173 heading | inert (not operative) | heading |
| 4338-4340 | s 173(a), (b): over, under, between two ages | encoded | `s 173(a) the person is over the age`, `s 173(a) the person is under the age`, `s 173(b) the person is between the two ages` |
| 4341 | s 173, closing words: the time a person attains an age | encoded; fork F1 | `s 173 the person has attained the age`, `s 173 the day the person attains the age` |
| 4342 | s 174 heading | inert (not operative) | heading |
| 4343-4350 | s 174: seven short names for Acts | encoded | `s 174 the title of the Act meant by`, `s 174 the short name given to the Act titled` |
| 4351 | "Subordinate legislation" heading | inert (not operative) | heading |
| 4352 | s 175 heading | inert (not operative) | heading |
| 4353-4355 | s 175(1), (1A)(a): who makes regulations and orders | inert (machinery) | regulation-making power |
| 4356 | s 175(1A)(b) | repealed or blank in this text | the line reads `(b) . . . .`, a row of dots |
| 4357-4364 | s 175(2), (3): statutory instrument; how a power may be exercised | inert (machinery) | regulation-making power |
| 4365-4370 | s 175(4), (5): incidental provision; discretion | inert (machinery) | regulation-making power |
| 4371-4372 | s 175(6), (7): different areas; Treasury concurrence | inert (machinery) | regulation-making power |
| 4373-4375 | s 175(8), (9), (10): ss 116-120 powers; later enactments; meaning of "order or regulations" | inert (machinery) | regulation-making power |
| 4376 | s 176 heading | inert (not operative) | heading |
| 4377-4426 | s 176(1): instruments that need an affirmative resolution | inert (machinery) | Parliamentary control of regulation-making; ten lines read only `...` (4394, 4396, 4400, 4402, 4404, 4405, 4419, 4420, 4421, 4424) and are repealed or blank in this text |
| 4427-4430 | s 176(2): carve-outs from (1) | inert (machinery) | Parliamentary control |
| 4431-4437 | s 176(2A), (2B), (2C): 12-month limit for laying a draft | inert (machinery) | Parliamentary control |
| 4438-4442 | s 176(3), (4): annulment | inert (machinery) | Parliamentary control |
| 4443 | "Short title, commencement and extent" heading | inert (not operative) | heading |
| 4444 | s 177 heading | inert (not operative) | heading |
| 4445 | s 177(1): short title | inert (machinery) | short title |
| 4446 | s 177(2): read with the Administration Act and the Consequential Provisions Act | encoded | `s 177(2) this Act is to be read with the other Act` |
| 4447 | s 177(3): repeal of the consolidated enactments | inert (machinery) | an amendment or repeal of other enactments |
| 4448 | s 177(4): commencement, 1 July 1992 | inert (machinery) | the Act's own commencement |
| 4449-4452 | s 177(5): provisions that extend to Northern Ireland | inert (machinery) | extent |
| 4453 | s 177(6): no other extension to Northern Ireland | inert (machinery) | extent |

No row is "out of scope" or "deferred".
The inert rows under s 175 and s 176 are powers and procedure for making instruments, and they create no rule for a person who asks what they owe or what they may claim.
A part agent that finds a rule written as an instrument-making power in its own range follows the same reasoning and says so in its own table.

The Act's other definitions sit in the parts' ranges and are theirs: `PLAN.md` has the table of which part owns which defined term.
The keel encoded none of those.

## Fork register

| id | where | the readings | text that licenses each | what the encoding does |
| --- | --- | --- | --- | --- |
| F1 | s 173, closing words (src:4341) | A: a person born on 29 February attains an age in a year with no 29 February at the commencement of 28 February. B: at the commencement of 1 March. | The Act says the time of attaining an age "is the commencement of the relevant anniversary of the date of his birth" and does not say what the anniversary of 29 February is in a year without one. | `s 173 the person has attained the age` answers `NOTHING` on 28 February of that year only, because the two readings agree on every other day (before 28 February both say not yet; from 1 March both say yes). `s 173 the day the person attains the age` answers `NOTHING` for the date itself. |

Not forks, though they are judgments handed to the reader:

- `s 177(2)` "where appropriate": the Act hands the judgment to whoever reads it.
  It is a plain input, `the reading is appropriate`, a BOOLEAN.
  When it is true the answer is `JUST TRUE`; when it is false the answer is `NOTHING`, because a grant limited by its own wording is not a "no" (marginal reading (b) below).
- `s 172` "includes": the list the Act adds is not closed.
  A place it does not name is `NOTHING`, never `FALSE`.

Assumed, not ruled (a lawyer may wish to look):

- s 173's closing words name Scotland and England and Wales, and say nothing of Northern Ireland.
  The encoding takes a person's age as the input and asks no nation, so the same rule applies everywhere.
  Under s 177(5) and (6) the Act extends to Northern Ireland only for s 16 and Schedule 2, s 116(2) and s 177 itself.
- In this Act "over" an age means "has attained" it.
  A person on their sixteenth birthday is over 16, and a person the day before is under 16.
  This follows from s 173(a) and is tested on both sides of the boundary.

## What the keel chose in the core (assumed, not ruled)

These are the choices that a part agent, or a lawyer reading later, might trip over.

- **Sex has two values, Woman and Man.**
  Sections 37, 48B and 164 speak of a "woman" and a "man".
  Section 140A(5) defines "woman" for that section alone (src:2918), and no section defines "man".
  The core makes no ruling about how a person's legal sex is established, because the sources do not say, and the Gender Recognition Act 2004 is not among them.
- **"Pensionable age" is a fact about the person.**
  Four places define it (ss 122(1), 137(1), 150 and Schedule 11, at src:2597, 2825, 3070 and 5691), and each sends it to paragraph 1 of Schedule 4 to the Pensions Act 1995, which is not among the sources.
  The core's `Person` carries `date of attaining pensionable age`, so every part reads it as given.
- **"Week" has six meanings across the Act.**
  The core lists them in `Week convention`, with quotes: Sunday-start (src:2624), Monday-start (src:2833, 2995), any 7 days (src:3225 and others), 7 days from the day a stated period begins (src:3300, 3639), Sunday-start or another prescribed period (src:3369 and others), and such period of 7 days as may be prescribed (src:5421).
  Each part that uses one says which.
  There is no default week.
- **Two constants only.**
  The upper accrual point (£770, s 122(1), src:2623) and the 24 weeks of pregnancy in the stillbirth rule (ss 35(6), 171(1), 171ZA(5), 171ZZ15).
  Every other number that regulations or Schedule 4 supply is an input.
- **Severe disablement allowance and council tax benefit.**
  The sections for them (ss 68-69, s 131) are blank in this text.
  Section 123(1)(e) still names council tax benefit, so `Benefit` has it; severe disablement allowance is not named.

### Reading a result: FALSE and NOTHING

In this row a function that answers `JUST FALSE` is the Act saying no in its own words.
In the keel's range there are three such places, all in s 173: the person has not attained the age, so the person is not over it; the person has attained it, so the person is not under it; the person is not between the two ages unless they have attained the first but not the second.
Each carries a comment `FALSE-kind (the text says no in its own words)` that quotes the Act.

A `NOTHING` is "not covered": the Act has not answered, and a caller must never turn it into `FALSE`.
In the keel's range it means one of the following.

| case | kind |
| --- | --- |
| a place that s 172 does not name (the land of Northern Ireland asked of Great Britain, or anywhere else) | includes |
| an age that is not a whole non-negative number of years | limited by its own wording ("a particular age expressed in years") |
| the anniversary of 29 February in a year without one, on 28 February | silent (fork F1) |
| a title that s 174 gives no short name to | silent |
| an Act other than the Administration Act and the Consequential Provisions Act asked under s 177(2) | silent |
| the same two Acts when the reading is not appropriate | limited by its own wording ("where appropriate") |

For the parts, the same two words mean the same things for their own sections: a "no" is the Act's own `means`, `if`, `only`, or flat negative, and everything else is `NOTHING`.
`PLAN.md` repeats the instruction to the part agents.

## Marginal readings for a lawyer

The brief gives two readings to a lawyer: (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
The status quo is taken in both.
Every branch of the keel's range that rests on one of them is listed.

| function | branch | reading taken | the other reading |
| --- | --- | --- | --- |
| `s 173(a) the person is over the age` | answers `JUST FALSE` when the person has not attained the age | (a): s 173(a) says a person "is over or under a particular age if he has or, as the case may be, has not attained that age", and the failed "if" is counted as the text's no | `NOTHING`: "if A then B" does not itself say "if not A then not B" |
| `s 173(a) the person is under the age` | answers `JUST FALSE` when the person has attained the age | (a), the same words | `NOTHING` |
| `s 173(b) the person is between the two ages` | answers `JUST FALSE` unless the person has attained the first age but not the second | (a): "is between two particular ages if he has attained the first but not the second" | `NOTHING` |
| `s 173 the person has attained the age` | answers `JUST FALSE` before the anniversary, and `JUST TRUE` from it | (a) in a looser form: the Act says "the time at which a person attains a particular age ... is the commencement of the relevant anniversary", a statement with "is" and not "means" or "if", and the encoding treats a day before that moment as the text's no | `NOTHING` before the anniversary |
| `s 177(2) this Act is to be read with the other Act` | answers `NOTHING` when the reading is not appropriate | (b): "where appropriate" limits the grant in its own wording | `JUST FALSE` |
| `s 173 the day the person attains the age`, `s 173 the person has attained the age` | answer `NOTHING` for an age that is not whole years | (b): "expressed in years" limits the rule in its own wording | `JUST FALSE` |

No branch in the keel's range rests on a flat negative.

## Jural relations

Hohfeld's correlatives: right and duty, privilege and no-right, power and liability, immunity and disability.
This table covers the whole of the keel's range, one row per provision.
Most of this range creates no relation between parties: it defines words or counts ages, or it is machinery, and those rows say `none`.

| provision | holder of right, privilege, power or immunity | bearer of duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| enacting words (line 1) | none | none | none (inert) |
| s 172 | none: it says what two place names include | none | `s 172(a) a reference to Great Britain includes the place`, `s 172(b) a reference to the United Kingdom includes the place` (a definition, no relation) |
| s 173 | none: it counts ages | none | `s 173(a)`, `s 173(b)` functions and `s 173 the person has attained the age` (a counting rule, no relation) |
| s 174 | none: short names | none | `s 174 the title of the Act meant by`, `s 174 the short name given to the Act titled` (definitions, no relation) |
| s 175(1), (1A)(a), (2)-(9) | power: the Secretary of State (or the Treasury or the Commissioners of Inland Revenue where another provision says so) to make regulations, orders and schemes | liability: every person the instruments would reach, such as claimants, contributors and employers | none (inert: machinery; the powers are exercised outside the sources) |
| s 175(1A)(b) | none | none | none (blank in this text) |
| s 175(10) | none: it says what "order or regulations" includes | none | none (inert: machinery) |
| s 176(1), (2), (2A)-(2C) | immunity against an instrument made without an approving resolution of each House: the text does not name the holder, and those it would bind is one reading (for a lawyer) | disability: the Secretary of State or Treasury may not make a listed instrument unless a draft has been laid and approved; (2A) adds a duty to lay the draft within 12 months of the appropriate date | none (inert: machinery) |
| s 176(3), (4) | power: either House of Parliament to annul an instrument | liability: the maker of an instrument not subject to a draft requirement | none (inert: machinery) |
| s 177(1) | none: short title | none | none (inert) |
| s 177(2) | none: a rule of reading, not a relation between parties | none | `s 177(2) this Act is to be read with the other Act` |
| s 177(3) | none: a repeal of other enactments | none | none (inert) |
| s 177(4) | none: commencement | none | none (inert) |
| s 177(5), (6) | none: extent | none | none (inert) |

## What the stable binary does not accept

The binary is the stable build, version 1.6.98.
These constructs were probed on 2026-11-04 with one-line files; each fails on 1.6.98 as shown.
The skills describe some of them as available, and the binary governs.

| construct | what 1.6.98 does |
| --- | --- |
| a bodiless `DECLARE Opaque` (an opaque type) | parse error at the next token |
| `#ASSERT REFUSED f 2` | check error, "I could not find a definition for the identifier" |
| `TYPICALLY 3` on a record field | parse error at the next token |
| `YMD 2024 1 1` | check error, "I could not find a definition for the identifier" (use `Date day month year`) |
| a `GIVEN` that sits at section level, between `§` and `§§` lines | parse error at the next `§§` line |
| `setFromList (LIST 1, 2)` and the other set functions | check error, "I could not find a definition for the identifier" |
| `NOT TRUE AND FALSE` | accepted, and answers `TRUE`, which is `NOT (TRUE AND FALSE)`; this is why every `NOT` here is parenthesised |

Taken from the brief and not re-probed: `REFUSE` and `BECAUSE`, a continuation line on an `#ASSERT`, and a `•` bullet in a `LIST`.

Two further observations from writing the keel:

- `daydate` defines `Monday` to `Sunday`, `January` to `December` and `May` as NUMBER constants, so a constructor with one of those names fails to check ("There are multiple definitions for the identifier Monday", measured on 1.6.98 on 2026-11-04).
  The core uses none of them.
- `Date 29 2 2023` is 1 March 2023 (measured on 1.6.98 on 2026-11-04: `#EVAL Date 29 2 2023` prints `DATE OF 1, 3, 2023`): `Date` rolls an impossible date forward.
  A part that builds a 29 February anniversary with `Date` resolves fork F1 silently to reading B.
  The keel builds `Date 28 2 y` and `Date 1 3 y` and never `Date 29 2 y` in a non-leap year.

## The converter text

The text is a plain-text rendering by a converter script and not the official text.
What it does, as found in the keel's range and in a read of the headings of the whole file:

- **Tables are omitted.**
  The sentences that introduce them remain.
  Known cases, each a sentence that introduces a table and is followed at once by the next provision: s 9A(3) (src:324), s 21(2) (src:746), Schedule 3 Part I at src:4861, all of Schedule 4 (src:4901-4907, headings only), and Schedule 4A at src:4933-4935, 4960-4962 and 4978-4980.
  A rate that the Act gives only in a table is therefore not in the sources: it is an input.
- **Schedule paragraph numbers are dropped.**
  Lettered paragraphs (5A and the like) exist, so counting headings misnumbers.
  Use the number an in-text citation gives.
- **Some limb labels are dropped.**
  In s 176(1) the list of sections under `(a) regulations made by virtue of--` has no sub-labels.
- **Blank and omitted text.**
  A line of dots (`. . . .`) is text shown repealed or blank; a line reading `...` is an editorial omission.
  In the keel's range these are src:4356, and the ten `...` lines under s 176(1).
- **A revised text can carry more than one extent version** of a provision; the keel's range shows none.

## What was run

Run on 2026-11-04 from the deposit directory, with the stable build 1.6.98 as `L4` and the second build 1.6.108 (main, 2ae7c9b, 2026-11-02) as `L4_MAIN`.

- `check.sh` over `ssc-core.l4`, `ssc-definitions-tests.l4` and `ssc-definitions.l4`: 0 errors in each; 165 assertions satisfied, 0 failed, 0 refused; the main build agrees on all four counts; exit 0.
- `l4 run` on each of the three files shows no `DiagnosticSeverity_Error` or `DiagnosticSeverity_Warning`.
- `python3 -I srcrefs.py check --refs inputs/ukpga-1992-4.txt` over the three files, also with `--strict`: 30 `src:` lines, 9 runs, 28 locators, 0 problems.

The tests are hand-written from the text: `ssc-definitions-tests.l4` writes the expected value beside each assertion.
Of the 165 assertions, 84 are generated name-resolution checks (`#ASSERT c EQUALS c`) over every core constructor and prove only that the names resolve.
No test is kept to fail.

## Open questions for the lead

1. The brief gives the parts the core only.
   If `ssc-definitions.l4` is not in their sandboxes, every part that asks "over/under/between age" or "in Great Britain" takes the s 172 and s 173 answers as inputs (`PLAN.md` names them), and the lead wires them at the merge.
2. Whether the core's `Sex` should stay two-valued once a lawyer has read ss 37, 48B, 140A and 164 together.
3. Whether the 29 February fork should be resolved by a lawyer before the merge: it changes the answer on one day, 28 February, in each year of the person's life that is not a leap year, and only for a person born on 29 February.
