# PLAN -- the Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4: what the nine part agents share

**Status (2026-11-04).**
Written by the keel agent for row `iaw-ssc-k`.
The core and the keel's definitions compile on stable 1.6.98 and on 1.6.108 (`check.sh`: 0 errors, 165 assertions satisfied, 0 failed; `srcrefs.py check`: 0 problems), and `NOTES.md` has the numbers.
The ranges below are copied from `inputs/PARTS.md`.
The seams were found by reading the headings of the whole Act and by a pattern search for cross-references.
Section 5 says which seam sentences were read and which were found by pattern only.
Nothing here is "verified against the official text": the source is `inputs/ukpga-1992-4.txt`, a plain-text rendering by a converter script.

## 1. Rules every part follows

### 1.1 What you receive and how to import it

- You receive `ssc-core.l4` as a read-only file in your sandbox.
  You never edit it and you never wait for it.
- The keel's `ssc-definitions.l4` is not promised to your sandbox: the keel's brief says each part receives the core module, so treat the definitions module as absent.
  The keel's answers (ss 172, 173, 174, 177(2)) arrive as inputs, section 3.
- A module of yours starts with these three lines, and imports nothing else of the family:

```
IMPORT prelude
IMPORT daydate
IMPORT `ssc-core`
```

- Dates are written `Date day month year`.
  Never define `YMD`, and never name a constructor `Monday` to `Sunday` or `January` to `December` or `May` (`daydate` already defines them as NUMBERs, and the clash fails to check).
- Money is a NUMBER in pounds sterling.
  A figure is a weekly figure unless its name says otherwise.
- Every file of part `X` begins with `X-`, for example `ssc3-rules.l4`, `ssc3-tests.l4`.
  Every file of the keel begins with `ssc-`.

### 1.2 The naming rule

- A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name.
- **Every top-level name a part defines begins with the section label it implements, in the Act's own numbering.**
  That covers functions, constants, types and the constructors of types.
- Examples of labels: `s 4(2)(a) the claimant has reached the qualifying age`, `s 47(1) the increase is payable`, `sch 3 para 2 the amount is reduced`, `sch 3 pt I the contribution conditions are satisfied`.
- A constructor is a top-level name too.
  A type you declare for s 30A is `s 30A Kind of day` with constructors `s 30A a day of incapacity`, and so on.
- A Schedule paragraph takes its label from the in-text citation (`sch 3 para 5`).
  The converter dropped the paragraph numbers, so never count headings: lettered paragraphs (5A, 5B) exist.
- Where a name implements two sections, use the first one it implements and cite the other with `@ref`.
- A parameter (`GIVEN`) and a `WHERE` name are not top-level names and are not bound by the rule.
- Types and constructors shared across parts live only in the core.
  If you need one the core lacks, define it under your own prefix and record it in `NEEDS-CORE.md` in your sandbox, one line per need: your name for it, the section that needs it, and why the core's types do not serve.
- The keel owns every name that begins `s 172`, `s 173`, `s 174` and `s 177(2)`.
  Do not define any.

### 1.3 Seams: how you take another part's answer

A seam is a provision in one part whose answer another part's provision needs.
Parts are in separate sandboxes until the merge, so the asking part takes the answer as an INPUT.

- The input is a `GIVEN` parameter of the asking function, named with the label of the **answering** section followed by what it answers: `sch 3 pt I the contribution conditions for the benefit are satisfied`.
- At the merge the lead replaces the parameter by a call to the answering function.
  The name is how the lead finds it, so use the answering section's label and not your own.
- The type is `MAYBE BOOLEAN` for a yes-or-no that the answering section decides (so that `NOTHING` flows through and is never turned into `FALSE`), `MAYBE NUMBER` for an amount it decides, and a plain type for a fact a witness can state.
- Record each seam in your `NOTES.md` in a section `## Seams`, one line each: asking section, answering section, name and type of the input.
- Where this plan names a seam, use its input name.
  Where you find another, follow the same pattern and add it to your `## Seams`; do not wait for a ruling.

A shape that compiles (invented to show the pattern; it is not a reading of s 21 beyond what `src:747` says):

```
IMPORT prelude
IMPORT daydate
IMPORT `ssc-core`

-- src:747 | (3) The relevant contribution conditions in relation to the benefits specified in subsection (2) above are those specified in Part I of Schedule 3 to this Act.
@ref s 21(3) (src:747)
GIVEN `sch 3 pt I the contribution conditions for the benefit are satisfied` IS A MAYBE BOOLEAN
GIVETH A MAYBE BOOLEAN
`s 21(3) the relevant contribution conditions are those in Schedule 3 Part I` MEANS
    CONSIDER `sch 3 pt I the contribution conditions for the benefit are satisfied`
    WHEN NOTHING THEN NOTHING        -- NOTHING-kind (points outside the text): Schedule 3 answers, asked as an input
    WHEN JUST `satisfied` THEN JUST `satisfied`
```

### 1.4 FALSE and NOTHING

The brief's rule of 2026-10-29 applies to every row.
`JUST FALSE` (or a constructor meaning "the text says no") only where the text itself says no in its own words: a definition that says "means", an "if", "only if", "unless", "so long as", "while", "until", "except", "save" or "provided that", a list closed with "only", or a flat negative.
Everything else is `NOTHING` (or a named "not covered" constructor): the text lists without closing, says "includes", leaves a term undefined, is silent, points outside your sources, or limits a grant or prohibition in its own wording.
Each "no" branch carries `-- FALSE-kind (the text says no in its own words): "<quote>"`; each "not covered" branch carries `-- NOTHING-kind (<why>)` with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
Put a section `### Reading a result: FALSE and NOTHING` in your `NOTES.md`, in this Act's terms. `NOTES.md` (the keel's) has the model.
List every branch that rests on a lawyer's reading under `## Marginal readings for a lawyer`.

### 1.5 The hazards of this text

- **Tables are omitted.**
  The sentence that introduces a table is there and the table is not.
  Known cases, each a sentence that introduces a table and is followed at once by the next provision: s 9A(3) (src:324), s 21(2) (src:746), Schedule 3 Part I at src:4861, all of Schedule 4 (src:4901-4907, headings only, so every benefit rate), and Schedule 4A at src:4933-4935, 4960-4962 and 4978-4980.
  Every rate, and every figure the Act gives only in a table, is an input.
  Where a section says "the rate specified in Schedule 4", the input is the rate.
- **Figures regulations supply are inputs**: the s 5 earnings limits (use the core's `Earnings limits`), "prescribed" amounts and periods, and any rate "for the time being" in force.
- **Schedule paragraph numbers are dropped, and some limb labels too** (for example under s 176(1)).
  Use the number an in-text citation gives, and say in your `NOTES.md` where you inferred a label.
- **A line of dots (`. . . .`) is text shown repealed or blank; a line reading `...` is an editorial omission.**
  Give each its coverage row: `repealed or blank in this text`, with the line numbers.
- **A revised text can carry several extent versions** of one provision, such as a Great Britain and a Northern Ireland wording.
  Where you meet one, say which version you encoded.
- **`Date` rolls an impossible date forward** (`Date 29 2 2023` is 1 March 2023).
  Never construct a date by adding years to a 29 February.

### 1.6 What the Act means by "over", "under" and "between" an age

Section 173(a) says a person "is over or under a particular age if he has or, as the case may be, has not attained that age", and the time of attaining an age is the commencement of the relevant anniversary of the date of birth.
So **"over 16" means "has attained 16"**: a person on their sixteenth birthday is over 16, and the day before they are under 16.
Do not compare an age in years that you computed yourself.
Take s 173's answer as an input (section 3).

## 2. The core, `ssc-core.l4`: one line per name

Each part's block in section 4 says which of these it expects to use.

| name | what it is |
| --- | --- |
| `Sex` | Woman or Man, as the Act's words "woman" and "man" (ss 37, 48B, 140A(5), 164); the person states which applies |
| `Marital status` | five values: neither married nor in a civil partnership; married; in a civil partnership; widowed or a surviving civil partner; divorced or a former civil partner |
| `Person` | date of birth, sex, marital status, and the date the person attains pensionable age (borrowed from the Pensions Act 1995, so a fact) |
| `Couple` | two persons, married to each other, civil partners of each other, same household, living together as if married or civil partners (the facts s 137(1) reads) |
| `Child` | date of birth, and living with the person claiming for them; no age is built in, because "child" is under 16 in ss 137 and 142 and under 18 in Part 12ZD |
| `Kind of employer` | an individual; a company or other body corporate; a government department, public authority or other body of persons; the Crown |
| `Category of earner` | employed earner; self-employed earner |
| `Employment` | the employee, the kind of employer, start and end dates, held under a contract of service, held in an office, carried on in Great Britain |
| `Service for statutory pay` | weeks of continuous employment ending with the relevant week, normal weekly earnings, last day of the relevant week (the facts ss 164, 171ZA, 171ZB, 171ZL and 171ZU-171ZZ ask in one shape) |
| `Class of contribution` | Class 1 primary, Class 1 secondary, Class 1A, Class 1B, Class 2, Class 3, Class 3A, Class 4 (s 1(2)) |
| `Tax year` | the calendar year in which it begins |
| `Tax week` | a tax year and the number of the week in it |
| `Earnings limits` | for a tax year: lower earnings limit, primary threshold, upper earnings limit, secondary threshold (inputs, because regulations supply them) |
| `Earnings paid` | an amount in pounds and the tax week it was paid in |
| `the upper accrual point` | the constant 770 (s 122(1), src:2623) |
| `Benefit` | the 34 benefits and payments the Act names (Part II to Part X) |
| `Statutory payment` | statutory sick pay; maternity pay; paternity pay; adoption pay; shared parental pay; parental bereavement pay; neonatal care pay |
| `Claim` | the claimant, the benefit claimed, the date of the claim |
| `Authority` | the Secretary of State; the Treasury; the Commissioners of Inland Revenue; a local authority; a billing authority; a social fund officer; the Northern Ireland Department |
| `Kind of decision` | whether a contribution is payable; whether a person is entitled; how much is payable; for how long; whether it is disqualified, suspended, reduced or ended; how a person is treated, or what a term means |
| `Period` | first day and last day |
| `Week convention` | the six meanings of "week": Sunday-start; Monday-start; any 7 days; 7 days from the day a stated period begins; Sunday-start or another prescribed period; such period of 7 days as may be prescribed (Schedule 7, src:5421) |
| `Labour` | weeks of pregnancy when labour began, whether it resulted in the issue of a living child, the day of the issue of the child or of the last child (ss 35(6), 171(1)) |
| `the weeks of pregnancy named in the stillbirth rule` | the constant 24 (ss 35(6)(b), 171(1), 171ZA(5), 171ZZ15) |
| `Kind of placement` | placed for adoption under the law of a part of the United Kingdom; placed under s 22C of the Children Act 1989; placed under s 81 of the Social Services and Well-being (Wales) Act 2014 |
| `Placement` | kind of placement, the day the person was notified of the match, the day the child was or is expected to be placed |

What the core does not hold, on purpose: any rule, any rate, any limit a regulation supplies, any definition that is itself a rule (those are the owning section's).
Benefits that are blank in this text (severe disablement allowance, bereavement payment and allowance, unemployment, sickness and invalidity benefit) are not named in `Benefit`.

## 3. The keel's answers a part may need

The keel encoded these in `ssc-definitions.l4`, which is not in your sandbox.
A part that needs one of them takes the answer as an input, named exactly as below, and the lead wires it at the merge.

| id | asking part | answering section | input name | type |
| --- | --- | --- | --- | --- |
| K1 | any part that asks whether something is in Great Britain or in the United Kingdom | s 172(a), s 172(b) | `s 172(a) a reference to Great Britain includes the place`, `s 172(b) a reference to the United Kingdom includes the place` | `MAYBE BOOLEAN` |
| K2 | any part that asks whether a person is over, under or between an age | s 173(a), s 173(b) | `s 173(a) the person is over <N>`, `s 173(a) the person is under <N>`, `s 173(b) the person is between <N> and <M>`, with the ages written in the name | `MAYBE BOOLEAN` |
| K3 | any part that names an Act by a short name | s 174 | none: write the Act's title in a comment, and treat `the Administration Act` and the other six names as the Act s 174 says | none |

- The core's `Employment` has a BOOLEAN field `carried on in Great Britain`.
  It records the fact as a witness would state it.
  Whether adjacent territorial waters count is s 172(a)'s answer, K1.
  A part that depends on the waters takes K1.
- Section 177(2) ("to be read, where appropriate, with the Administration Act and the Consequential Provisions Act") is a rule of reading and asks nothing of a part.
- K2 returns `NOTHING` for a person born on 29 February on 28 February of a year with no 29 February (fork F1 in `NOTES.md`).
  A part passes that `NOTHING` on and never treats it as `FALSE`.

### Who owns which defined term

The Act's own definitions sit in the parts' ranges and are theirs.
Where a part needs a term another part defines, it takes the answer as an input (section 1.3) or, for a term that is only a fact (a plain noun), uses the core's field.
Do not re-implement another part's definition under your own prefix without recording it in `NOTES.md`: the same word has different meanings in different Parts.

| part | section (line) | terms defined there |
| --- | --- | --- |
| ssc1 | s 4A (138) | the applicable provisions of this Act; business; relevant payments or benefits; specified |
| ssc1 | s 4B (176) | relevant contributions legislation; the relevant time; the revised earnings |
| ssc1 | s 4C (228), s 10ZC (458) | the commencement day; enactment; statutory payment |
| ssc1 | s 12 (521), s 13 (530) | ordinary contribution; higher-rate contribution; the payment year; the contribution year |
| ssc2 | s 20 (731) | long-term benefit; short-term benefit |
| ssc2 | s 23A (839) | the contributor concerned; foster parent |
| ssc3 | s 45AA (1401), s 45B (1421), ss 55A and 55B (1712, 1738) | couple; relevant year; final relevant year; state scheme pension debit and credit; valuation day |
| ssc3 | s 52 (1667) | full amount |
| ssc5 | s 122(1) (2533) | the definitions for Parts I to VI: among them additional Class 4 percentage, age-related secondary percentage, benefit, the benefits code, child, deferred and period of deferment, pensionable age, the upper accrual point and week |
| ssc5 | s 137(1) (2806) | for Part VII: billing authority; child (under 16); couple; dwelling; family; income-based jobseeker's allowance; industrial injuries scheme; local authority; pensionable age; prescribed; the qualifying age for state pension credit |
| ssc5 | s 138 (2869), s 140A(5) (2916), s 145A (2975), s 147 (2992), s 150 (3056) | budgeting loan, community care grant, crisis loan; health professional, woman; civil partnership, cohabiting couple, married couple; voluntary organisation, week (Monday-start); the Part X terms and pensionable age |
| ssc6 | s 153 (3138), s 159A (3186), s 163 (3210) | confinement, disqualifying period, maternity allowance period, maternity pay period; contributions payments; contract of service, employee, employer, period of entitlement, period of incapacity for work, qualifying day, week |
| ssc6 | s 171 (3351), s 171ZE (3472), s 171ZJ (3520), s 171ZS (3673) | confinement, dismissed, employee, employer (Part 12); statutory pay week; employer and the other terms of Part 12ZA; adoption pay period and the terms of Part 12ZB (s 4AA(2), src:154, names "employee" and "employer" in ss 163, 171, 171ZJ, 171ZS, 171ZZ14 and 171ZZ24) |
| ssc7 | s 171ZZ and the supplementary sections of Parts 12ZC to 12ZE (3975 onward), s 171G (4329) | adoption pay period, employer, local authority, maternity allowance period, maternity pay period, statutory pay week, week, child (under 18 in Part 12ZD); prescribed, week |
| keel | s 174 (4344) | the seven short names for Acts |
| ssc8 | Schedule 1 (4506), Schedule 3 (4834), Schedule 4B (5057) | agreement, relevant earner; benefit; the contracted-out condition, the FRAA, the LET, the QEF, the pensioner's assumed earnings factor, relevant year |
| ssc9 | Schedule 5 (5086) | incremental period |

Borrowed, not defined here (ask them as facts): "pensionable age" (Pensions Act 1995, Schedule 4 paragraph 1; src:2597, 2825, 3070, 5691), and the Children Act 1989 and Social Services and Well-being (Wales) Act 2014 terms in ss 171ZB and 171ZJ.
The core's `Person` carries the date the person attains pensionable age.
The same word is defined differently across Parts and none of those definitions is shared: "week" (Sunday, Monday, any 7 days, from the day a period begins), "child" (16, 16, 18), "confinement" (ss 35(6) and 171(1)), "period of incapacity for work" (ss 30C, 152, 171B), "employer" and "employee" (ss 163, 171, 171ZJ, 171ZS and the 171ZZ series).

## 4. The parts

For each part: the line ranges (copied unchanged from `inputs/PARTS.md`), the sections they hold, the core names to expect, and the seams by id (section 5 defines each).
"Asks" means your function takes that input. "Answers" means your section is where another part's input comes from, so expose a function for it and name it by your own label.

### ssc1: lines 2-710

- Holds: Part I, Contributions, ss 1-19B (1 2 3 4 4A 4AA 4B 4C 5 6 6A 7 8 9 9A 9B 10 10ZA 10ZB 10ZBA 10ZC 10A 11 11A 12 13 13A 14 14A 14B 14C 15 16 17 18 18A 19 19A 19B).
- Core: `Class of contribution`, `Category of earner`, `Employment`, `Kind of employer`, `Earnings limits`, `Earnings paid`, `Tax year`, `Tax week`, `Person`, `Period`, `Week convention`.
- Asks: S8 (s 6A), S9 (s 13), S10 (s 14A(8)), K1 and K2 where used.
- Answers: S4 (ss 6, 11 and 13 answer s 22), S26 (s 5(1)(a) answers ss 164 and 171ZA).
- Watch: ss 9A(3) and the table in s 9A are omitted from the text, so the age-related secondary percentage is an input; Schedule 1 (ssc8) carries the supplementary rules for Classes 1 to 3A.

### ssc2: lines 711-1229

- Holds: Part II, Contributory Benefits, ss 20-42 (20 21 22 23 23A 24 25 25A 25B 26 27 28 29 30 30A 30B 30C 30D 30DD 30E 31 32 33 34 35 35A 35B 36 36A 37 38 39 39A 39B 39C 40 41 42).
- Core: `Benefit`, `Claim`, `Person`, `Couple`, `Marital status`, `Sex`, `Child`, `Class of contribution`, `Tax year`, `Period`, `Labour`, `the weeks of pregnancy named in the stillbirth rule`, `the upper accrual point` (ss 22, 23), `Week convention`.
- Asks: S1 (ss 21(3), 30A(2)(a), 37(1), 38(1), 39A(2)), S2 (s 30B(2)), S3 (s 30B(3)), S4 (s 22(1)), S5 (s 23(1)), S6 (s 35), S7 (s 35A), S35 (s 30A).
- Answers: S9 (s 22 purposes), S11 (s 22(5)), S13 (s 30DD(6)), S14 (s 23A(3)), S15 (ss 39, 39C), S16 (s 30B(7)), S17 (s 38), S23 (ss 30C, 42), S24 (s 35(2)), S27 (s 35(3A)), S29 (s 35(2)), S8 (s 21(5A)).
- Watch: s 35(6) defines "confinement" the same way as s 171(1) (ssc6).
  Do not share the function.

### ssc3: lines 1230-1911

- Holds: the rest of Part II, ss 43-62 (43 44 44A 44B 44C 45 45AA 45A 45B 46 47 48 48A 48AA 48B 48BB 48C 49 50 51 51ZA 51A 52 53 54 55 55A 55AA 55B 55C 56 57 58 59 60 60A 61 61ZA 61ZB 61ZC 61A 62): retirement pensions, additional pension, deferment.
- Core: `Person`, `Sex`, `Marital status`, `Couple`, `Benefit`, `Claim`, `Period`, `Child`, `the upper accrual point` (ss 44, 44B), `Tax year`.
- Asks: S1 (ss 44, 51), S11 (s 45), S12 (s 45AA), S13 (s 44A(6)), S14 (s 44C), S15 (s 46(2)), S16 (s 47(1)), S17 (s 48B), S18 (s 56), S19 (s 60).
- Answers: S3 (s 44(4)), S10 and S37 (s 55(3), s 55C(3)), S22 (s 60), S31 (s 44 relevant year).
- Watch: s 44(4) states £184.90 and £140.65 in its own words (src:1258), so those two figures are not omitted: encode them under your prefix and cite the line.
  Section 62 refers to ss 36 and 37 of the National Insurance Act 1965, which are not ss 36 and 37 of this Act.

### ssc4: lines 1912-2443

- Holds: Part III, Non-Contributory Benefits (ss 63-79), Part IV, Increases for dependants (ss 80-93), Part V, Benefit for Industrial Injuries (ss 94-111).
- Core: `Person`, `Child`, `Couple`, `Benefit`, `Claim`, `Authority`, `Employment`, `Kind of decision`, `Period`, `Week convention`.
- Asks: S18 (s 77), S20 (s 94(5)), S21 (s 103(5)), S22 (s 87), S23 (s 93).
- Answers: S19 (s 94(1)), S36 (s 94(6)).
- Watch: s 94(6) gives "work" a narrower meaning for "incapable of work" in Part V.
  Part V does not use ssc7's s 171A test (s 171G(1)(a)).
  Sections 68 and 69 (severe disablement allowance) are blank in this text (src:1978-1980).

### ssc5: lines 2444-3094

- Holds: Part VI, Miscellaneous Provisions relating to Parts I to V (ss 112-122); Part VII, Income-Related Benefits (ss 123-137); Part VIII, The Social Fund (ss 138-140); Part 8A, Health in pregnancy grant (ss 140A-140B); Part IX, Child Benefit (ss 141-147); Part X, Christmas bonus for pensioners (ss 148-150).
- Core: `Person`, `Couple`, `Child`, `Marital status`, `Benefit`, `Claim`, `Authority`, `Kind of decision`, `Earnings limits`, `Tax year`, `Week convention`, `Period`.
- Asks: S37 (s 122(1) on deferment).
- Answers: S12 (s 137(1) "couple"), S18 (s 143(1)(b)), S20 (ss 117, 119, 120), S25 (s 120(2)), S33 (s 143(1)).
- Watch: the s 122(1) definition of "the upper accrual point" is **already encoded by the core's constant**; mark that row `encoded` in your coverage table and cite the constant, and do not define it again.
  The core's `Week convention` already carries the s 122(1) and s 147 meanings of "week" with their quotes; cite it, and add a function only if you need one.
  Section 131 (council tax benefit) is blank in this text (src:2761), though s 123(1)(e) still names council tax benefit.

### ssc6: lines 3095-3717

- Holds: Part XI, Statutory Sick Pay (ss 151-163); Part XII, Statutory Maternity Pay (ss 164-171); Part 12ZA, Statutory Paternity Pay (ss 171ZA-171ZK); Part 12ZB, Statutory Adoption Pay (ss 171ZL-171ZT).
- Core: `Employment`, `Kind of employer`, `Service for statutory pay`, `Statutory payment`, `Labour`, `Placement`, `Kind of placement`, `the weeks of pregnancy named in the stillbirth rule`, `Period`, `Week convention`, `Person`, `Child`, `Earnings limits`.
- Asks: S24 (s 153), S25 (s 162), S26 (ss 164, 171ZA).
- Answers: S6 (s 165), S7 (s 166(1)(b)), S28 (s 171ZN(2A), (8)), S29 (s 171ZN(2), s 165(1)), S30 (ss 164, 171ZA(2), 171ZB(2), 171ZL(2)), S32 (s 153(12), s 171(1)).
- Watch: "week" has three of the core's meanings across these Parts: any 7 days (s 163, src:3225; s 171ZE, src:3473; s 171ZN(7), src:3638), 7 days from the day a stated period begins (s 165(8), src:3300; s 171ZN(8), src:3639; s 171ZP, src:3658) and Sunday-start or another prescribed period (s 171(1A), src:3369; s 171ZJ, src:3539; s 171ZS, src:3693); name the one each rule uses by a `Week convention` constructor.
  Sections 171ZB, 171ZE and 171ZJ mention s 81 of the Social Services and Well-being (Wales) Act 2014 and s 105 of the Children Act 1989: those are other Acts' sections, not seams. "Employer" and "employee" are defined four times (ss 163, 171, 171ZJ, 171ZS); s 4AA(2) (ssc1) lets the Treasury modify them.

### ssc7: lines 3718-4330

- Holds: Part 12ZC, Statutory shared parental pay (ss 171ZU-171ZZ5); Part 12ZD, Statutory parental bereavement pay (ss 171ZZ6-171ZZ15); Part 12ZE, Statutory neonatal care pay (ss 171ZZ16-171ZZ24); Part XIIA, Incapacity for work (ss 171A-171G).
- Core: as ssc6, with `Claim` and `Child`.
- Asks: S24 (s 171ZZ4), S25 (ss 171ZZ3, 171ZZ13), S27 (s 171ZU), S28 (s 171ZV), S29 (s 171ZZ4), S30 (s 171ZZ16).
- Answers: S35 (s 171A(1)).
- Watch: "child" is under 18 in Part 12ZD (src:4097).
  Section 171G(1) makes Part XIIA inapplicable for Part V (s 94(6), ssc4) and for Part XI (s 151(4), ssc6) purposes, so ssc2's incapacity-for-work rules ask s 171A and ssc6 and ssc4 do not.

### ssc8: lines 4454-5066

- Holds: Schedule 1 (4454), Schedule 2 (4747), Schedule 3 (4804), Schedule 4 (4901), Schedule 4A (4908), Schedule 4B (4996).
- Core: `Class of contribution`, `Tax year`, `Earnings limits`, `Earnings paid`, `Benefit`, `Person`, `Sex`, `Employment`.
- Asks: S11 (Schedule 3), S31 (Schedule 4A relevant year).
- Answers: S1 (Schedule 3 Part I), S2 (Schedule 4 Part I paragraph 2), S34 (Schedule 4 Part V).
- Watch: **all of Schedule 4 is omitted from this text**, and the three tables of Schedule 4A are omitted.
  The coverage rows for them are `repealed or blank in this text` with a note that the table is absent, and every rate is an input.
  Schedule 3's paragraph numbers are dropped; use the citing sentences (paragraphs 2, 5 and 5A are cited at src:870, 1073, 1087, 1251-1252, 1616-1617).

### ssc9: lines 5067-5745

- Holds: Schedules 5 (5067), 5A (5293), 6 (5339), 7 (5380), 8 (5623), 9 (5641), 10 (5655), 11 (5671), 12 (5695), 13 (5722).
- Core: `Benefit`, `Person`, `Child`, `Employment`, `Statutory payment`, `Authority`, `Claim`, `Period`, `Week convention`, `Labour`.
- Asks: S18 (Schedule 7), S32 (Schedule 11), S33 (Schedule 10), S34 (Schedule 7), S36 (Schedule 7).
- Answers: S21 (Schedule 6).
- Watch: Schedule 11 disqualifies a period of entitlement to statutory sick pay for listed reasons and sends two of them to s 153(12) and s 171(1) (ssc6).
  Schedule 13 takes "week" from the day the maternity pay period begins (src:5733: the core's fourth `Week convention`), and Schedule 7 says "week" means such period of 7 days as may be prescribed (src:5421: the core's sixth); name the one each rule uses.

## 5. The seam register

Each seam: asking section, answering section, input name, input type.
Every entry below was read by the keel at the line cited in the asking column, except where the type column says otherwise.
The appendix lists cross-references found by pattern search alone, whose sentences were not read.

| id | asking section | answering section | input name | type |
| --- | --- | --- | --- | --- |
| S1 | ssc2 s 21(3) (src:747), s 30A(2)(a) (870), s 37(1) (1073), s 38(1) (1087), s 39A(2) (1121); ssc3 s 44 (1251-1252), s 51 (1616-1617) | ssc8 Schedule 3 Part I | `sch 3 pt I para <N> the contribution conditions for <the benefit> are satisfied`, with the paragraph the asking sentence cites (2, 5 or 5A) | `MAYBE BOOLEAN` |
| S2 | ssc2 s 30B(2) (887) | ssc8 Schedule 4 Part I paragraph 2 | `sch 4 pt I para 2 the lower rate of short-term incapacity benefit in pounds`, `sch 4 pt I para 2 the higher rate of short-term incapacity benefit in pounds` (the table is omitted from this text) | `MAYBE NUMBER` |
| S3 | ssc2 s 30B(3) (889) | ssc3 s 44(4) (1258) | `s 44(4) the weekly rate of the basic pension in pounds` | `MAYBE NUMBER` |
| S4 | ssc2 s 22(1)(a) (767) | ssc1 ss 6, 11, 13 | `s 6 the earnings on which primary Class 1 contributions have been paid or treated as paid in the tax year`; `s 11 the number of weeks for which a Class 2 contribution was paid in the tax year`; `s 13 the number of weeks for which a Class 3 contribution was paid in the tax year` | `NUMBER` each (the section headings 11 and 13 were checked, the wording of those two sections was not read) |
| S5 | ssc2 s 23(1) (807) | outside the sources (section 148 of the Administration Act) | `s 23(1) the earnings factor as increased by an order under section 148 of the Administration Act` | `NUMBER`, an input in every case |
| S6 | ssc2 s 35(2) (993), s 35(3E) (1013) | ssc6 s 165 | `s 165(1) the maternity pay period if she were entitled to statutory maternity pay`; `s 165(3A) the woman would be entitled to statutory maternity pay for the week but for the reduction in the maternity pay period` | `Period`; `MAYBE BOOLEAN` |
| S7 | ssc2 s 35A (1028, 1037) | ssc6 s 166(1)(b) | `s 166(1)(b) the weekly rate prescribed in pounds` | `NUMBER`, because regulations prescribe it |
| S8 | ssc1 s 6A (270) | ssc2 s 21(5A) | `s 21(5A) the provision is one mentioned in section 21(5A)(a) to (c)` | `BOOLEAN` |
| S9 | ssc1 s 13(2) (526) | ssc2 s 22 | `s 22 the payment is with a view to acquiring the requisite earnings factor for the purposes described` | `BOOLEAN` |
| S10 | ssc1 s 14A(8) (590) | ssc3 s 55(3) | `s 55(3) the retirement pension is deferred` | `MAYBE BOOLEAN` |
| S11 | ssc3 s 45 (1384); ssc8 Schedule 3 (4836) | ssc2 s 22(5) | `s 22(5) the person was credited with contributions or earnings by regulations` | `BOOLEAN` |
| S12 | ssc3 s 45AA (1401) | ssc5 s 137(1) | `s 137(1) the two persons are a couple` | `MAYBE BOOLEAN` |
| S13 | ssc3 s 44A(6) (1314) | ssc2 s 30DD(6) | `s 30DD(6) the scheme is an occupational pension scheme`; `s 30DD(6) the scheme is a personal pension scheme` | `MAYBE BOOLEAN` each |
| S14 | ssc3 s 44C (1349) | ssc2 s 23A(3) | `s 23A(3) the person was a relevant carer in respect of the week` | `MAYBE BOOLEAN` |
| S15 | ssc3 s 46(2) (1426) | ssc2 ss 39(1), 39C(1); ssc3 s 48B(2) | `s 39(1) the additional pension falls to be calculated under section 45 by virtue of this section`; `s 39C(1) the additional pension falls to be calculated under section 45 by virtue of this section` | `MAYBE BOOLEAN` each |
| S16 | ssc3 s 47(1) (1444) | ssc2 s 30B(7) | `s 30B(7) the pensioner was entitled to an age addition to long-term incapacity benefit`; `s 30B(7) the weekly rate of the age addition in pounds` | `MAYBE BOOLEAN`; `MAYBE NUMBER` |
| S17 | ssc3 s 48B (1562, 1566) | ssc2 s 38 | `s 38 the late spouse was entitled, or treated as entitled, to a widow's pension`; `s 38 the weekly rate of that pension in pounds` | `MAYBE BOOLEAN`; `MAYBE NUMBER` |
| S18 | ssc3 s 56 (1772); ssc4 s 77 (2167); ssc9 Schedule 7 (5430) | ssc5 s 143(1)(b) | `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)` | `MAYBE BOOLEAN` |
| S19 | ssc3 s 60 (1797) | ssc4 s 94(1) | `s 94(1) the personal injury is of a kind mentioned in section 94(1)` | `MAYBE BOOLEAN` |
| S20 | ssc4 s 94(5) (2288) | ssc5 ss 117, 119, 120 | `s 117 the accident falls within the exception`; `s 119 the accident falls within the exception`; `s 120 the accident falls within the exception` | `MAYBE BOOLEAN` each |
| S21 | ssc4 s 103(5) (2357) | ssc9 Schedule 6 | `sch 6 the extent of the disablement assessed, as a percentage` | `MAYBE NUMBER` |
| S22 | ssc4 s 87 (2234, 2237) | ssc3 s 60 | `s 60(1) the retirement pension would be payable only by virtue of section 60` | `MAYBE BOOLEAN` |
| S23 | ssc4 s 93 (2269) | ssc2 ss 30C(5), 30C(6), 42 | `s 30C(5) the person is entitled to the higher rate of short-term incapacity benefit`; `s 42 the person is entitled to long-term incapacity benefit` | `MAYBE BOOLEAN` each |
| S24 | ssc6 s 153 (3142); ssc7 s 171ZZ4 (3983) | ssc2 s 35(2) | `s 35(2) the maternity allowance period` | `Period` |
| S25 | ssc6 s 162 (3202); ssc7 s 171ZZ3 (3967), s 171ZZ13 (4089) | ssc5 s 120(2) | `s 120(2) the employment is in connection with continental shelf operations` | `BOOLEAN` |
| S26 | ssc6 s 164(2)(b) (3246), s 171ZA (3394) | ssc1 s 5(1)(a) | `s 5(1)(a) the lower earnings limit in force at the time in pounds` (use the core's `Earnings limits`) | `NUMBER` |
| S27 | ssc7 s 171ZU (3783, 3787) | ssc2 s 35(3A); ssc6 s 165(3A), s 165(8); ssc5 s 122(1) | `s 35(3A) the number of weeks to which the maternity allowance period is reduced`; `s 165(3A) the number of weeks to which the maternity pay period is reduced`; the week convention is the core's `Week convention` | `NUMBER` each |
| S28 | ssc7 s 171ZV (3872, 3873) | ssc6 s 171ZN(2A), s 171ZN(8) | `s 171ZN(2A) the number of weeks to which the adoption pay period has been reduced` | `NUMBER` |
| S29 | ssc7 s 171ZZ4 (3975-3984) | ssc6 s 171ZN(2), s 165(1); ssc2 s 35(2) | `s 171ZN(2) the adoption pay period`; `s 165(1) the maternity pay period`; `s 35(2) the maternity allowance period` | `Period` each |
| S30 | ssc7 s 171ZZ16 (4148-4151) | ssc6 s 164, s 171ZA(2), s 171ZB(2), s 171ZL(2) | `s 164 the relevant week`; `s 171ZA(2) the relevant week`; `s 171ZB(2) the relevant week`; `s 171ZL(2) the relevant week` | `Period` each |
| S31 | ssc8 Schedule 4A (4925, 4943) | ssc3 s 44 | `s 44 the relevant year`; `s 44 the final relevant year` | `Tax year` each |
| S32 | ssc9 Schedule 11 (5685, 5694) | ssc6 s 153(12), s 171(1) | `s 153(12) the relevant date falls within the disqualifying period`; `s 171(1) the pregnancy terminated otherwise than by confinement` | `BOOLEAN` each |
| S33 | ssc9 Schedule 10 (5660) | ssc5 s 143(1)(a), (b) | `s 143(1)(a) the person is entitled for the week by virtue of paragraph (a)`; `s 143(1)(b) the person is entitled for the week by virtue of paragraph (b)` | `BOOLEAN` each |
| S34 | ssc9 Schedule 7 (5385, 5393) | ssc8 Schedule 4 Part V paragraphs 5 and 6 | `sch 4 pt V para 5 the increase of the disablement pension in pounds`; `sch 4 pt V para 6 the increase of the unemployability supplement in pounds` (the table is omitted) | `MAYBE NUMBER` each |
| S35 | ssc2 s 30A(2)(c) (877) | ssc7 s 171A(1) | `s 171A(1) the person is incapable of work` | `MAYBE BOOLEAN` |
| S36 | ssc9 Schedule 7 (5385) | ssc4 s 94(6) | `s 94(6) the person is incapable of work, "work" meaning work the person can reasonably be expected to do` | `MAYBE BOOLEAN` |
| S37 | ssc5 s 122(1) (2559-2560) | ssc3 s 55(3), s 55C(3) | `s 55(3) the pension is deferred`, `s 55C(3) the shared additional pension is deferred` | `MAYBE BOOLEAN` each |
| K1, K2, K3 | any part | keel ss 172, 173, 174 | section 3 | section 3 |

### Not seams, though they look like one

A pattern search for "section N" lands on these, and they refer to other Acts, so no input is needed.

- ssc3 s 62 (1889-1895) refers to ss 36 and 37 of the National Insurance Act 1965.
- ssc6 s 171ZB (3420, 3421) and s 171ZE (3478, 3479) refer to s 81 of the Social Services and Well-being (Wales) Act 2014; ssc6 s 171ZJ (3526, 3527) refers to s 105 of the Children Act 1989.
- ssc5 s 137 (2819) and s 150 (3062) refer to s 159 of the 1975 Act, which s 174 names.
- ssc5 s 122(1) (2548) refers to section 63(1) of ITEPA 2003.
- ssc1 s 4C (215) refers to section 43 of the Pensions Act.

### Appendix: cross-references found by pattern only (sentences not read)

The list is the output of a script that matches "section N" or "Schedule N" in one part's lines and looks N up among the sections of another part.
It is mechanical and has false positives (the section above names six).
Use it as a checklist for your own `## Seams`: read the sentence, and decide whether it asks for an answer.
Notation: `ssc2 -> ssc1: 21->1x2` means that in ssc2, s 21 mentions s 1 of ssc1 in two sentences.

```
ssc1 -> ssc2: 13->22, 4AA->24, 6A->21
ssc1 -> ssc3: 14A->55, 4C->43
ssc1 -> ssc4: 10ZB->84, 2->95
ssc1 -> ssc5: 1->116, 1->120, 19->130, 8->116, 8->120, 9->116, 9->120
ssc1 -> ssc6: 4AA->163, 4AA->171, 4AA->171ZJ, 4AA->171ZS
ssc1 -> ssc7: 4AA->171ZZx2
ssc1 -> ssc8: 1->Sch 1, 13A->Sch 3x3, 15->Sch 2, 16->Sch 2x2, 17->Sch 2, 18->Sch 1, 6->Sch 1
ssc1 -> ssc9: 3->Sch 8
ssc2 -> ssc1: 21->1x2, 22->1, 22->19, 22->2, 22->4x4, 23->1, 23->2x2, 23->8, 23A->5, 30A->1, 30B->2x2, 30C->2, 30C->3, 30D->2, 30D->4x2, 30D->5, 30DD->3, 35A->1x4, 39->4, 39A->1, 39C->4, 40->1, 40->4x2, 41->1
ssc2 -> ssc3: 21->55A, 21->55AA, 22->44A, 22->44B, 23A->48A, 23A->48AA, 23A->48B, 30A->54, 30B->51A, 39->44x3, 39->45Bx2, 39->46, 39C->44x4, 39C->45AAx3, 39C->46, 40->54, 41->54
ssc2 -> ssc6: 35->165x2, 35A->166x3
ssc2 -> ssc8: 21->Sch 3x3, 23A->Sch 3x2, 30A->Sch 3, 30B->Sch 4x2, 37->Sch 3, 38->Sch 3, 39A->Sch 3
ssc2 -> ssc9: 30B->Sch 5
ssc3 -> ssc1: 44->1, 44->14A, 44->3, 44A->6, 44B->6x2, 44C->3, 44C->4x2, 44C->6, 45->3, 45->5, 45AA->19, 45AA->4, 45AA->6, 45B->3, 46->1x5, 46->4x2, 47->14A, 47->3, 47->7x3, 48AA->4, 48B->4, 48BB->4, 48C->1x3, 48C->2x2, 51A->1, 51ZA->1, 51ZA->2x2, 52->1, 52->4, 55->1, 56->1, 60->1x2, 60A->1x2, 61->1x3, 61->3, 61ZA->14A, 61ZB->14A, 61ZC->2, 61ZC->3x2, 62->1, 62->4, 62->7
ssc3 -> ssc2: 44->30B, 44A->30DD, 44C->23Ax2, 44C->30DD, 45->22, 46->39, 46->39Cx4, 47->30Bx3, 48B->38x3, 48BB->39A, 48BB->39Bx2, 61->30B, 62->36x3, 62->37x6
ssc3 -> ssc4: 60->108, 60->94, 60A->108, 60A->94
ssc3 -> ssc5: 44->148, 45AA->137, 56->143
ssc3 -> ssc8: 44->Sch 3x2, 44->Sch 4A, 44A->Sch 3x2, 44C->Sch 3, 45->Sch 4A, 45->Sch 4B, 48A->Sch 3x3, 48A->Sch 4, 48AA->Sch 3x3, 48AA->Sch 4, 48B->Sch 3x4, 48B->Sch 4A, 48BB->Sch 4A, 51->Sch 3x4, 51A->Sch 4, 56->Sch 3, 56->Sch 4, 60->Sch 3x2, 60A->Sch 3x5, 61A->Sch 1
ssc3 -> ssc9: 47->Sch 5, 55->Sch 5, 55C->Sch 5A, 62->Sch 5x2
ssc4 -> ssc1: 109->1, 109->3, 65->1, 72->2, 73->1, 73->2, 74->13, 76->12, 76->5, 77->1, 87->1, 87->2, 93->5, 95A->4
ssc4 -> ssc2: 87->30A, 93->30C, 93->42
ssc4 -> ssc3: 87->60x2
ssc4 -> ssc5: 77->143, 94->117, 94->119, 94->120
ssc4 -> ssc8: 103->Sch 4, 104->Sch 4, 105->Sch 4x2, 107->Sch 4, 65->Sch 4, 70->Sch 4, 77->Sch 4, 78->Sch 4, 79->Sch 4, 86A->Sch 4
ssc4 -> ssc9: 103->Sch 6, 106->Sch 7, 107->Sch 7, 94->Sch 7
ssc5 -> ssc1: 116->2, 120->1, 120->6, 122->1x5, 122->14A, 122->15x2, 122->19B, 122->2x8, 122->3x4, 122->4, 122->5x2, 122->7, 122->8x2, 122->9, 122->9A, 127->1, 130A->1x2, 130A->2, 136->1, 136A->1, 136A->15, 136A->6, 136A->7, 137->2x2, 138->2, 139->1, 140->1x2, 149->1, 149->2, 150->1, 150->3
ssc5 -> ssc2: 122->20x3, 122->21, 122->25A
ssc5 -> ssc3: 114->56, 118->60, 122->55, 122->55C
ssc5 -> ssc4: 115->111, 122->63, 122->84, 145A->77, 150->104, 150->105
ssc5 -> ssc6: 137->159, 150->159
ssc5 -> ssc8: 122->Sch 3
ssc5 -> ssc9: 114->Sch 7, 122->Sch 8x2, 137->Sch 8, 144->Sch 10, 144->Sch 9, 149->Sch 7, 150->Sch 7, 150->Sch 8x2
ssc6 -> ssc1: 153->1x3, 153->2, 153->3, 153->6, 162->2, 163->1, 163->6x2, 164->1x2, 164->5, 166->1, 170->2, 171->1x4, 171->6x2, 171ZA->1, 171ZA->5, 171ZB->1, 171ZB->5, 171ZE->10, 171ZE->2x4, 171ZE->8, 171ZI->2, 171ZJ->1x3, 171ZJ->6x2, 171ZL->1, 171ZL->5, 171ZL->8, 171ZM->2, 171ZN->1, 171ZN->11, 171ZN->9, 171ZR->2, 171ZS->1x3, 171ZS->2, 171ZS->6x2, 171ZT->8
ssc6 -> ssc2: 153->35
ssc6 -> ssc4: 171ZB->81x5, 171ZE->81x2, 171ZJ->105x2, 171ZL->81x5, 171ZN->81, 171ZS->105x2
ssc6 -> ssc5: 162->120, 170->120, 171ZI->120, 171ZR->120
ssc6 -> ssc9: 153->Sch 11, 160->Sch 12, 168->Sch 13, 171->Sch 13
ssc7 -> ssc1: 171C->2, 171G->4, 171G->6, 171ZU->1x3, 171ZU->5x2, 171ZU->8, 171ZV->1x2, 171ZV->5x2, 171ZV->8, 171ZW->13x2, 171ZW->15x2, 171ZW->2x4, 171ZW->4x2, 171ZX->2, 171ZY->2x4, 171ZY->5x2, 171ZZ->1x10, 171ZZ->15, 171ZZ->16x9, 171ZZ->19, 171ZZ->2x11, 171ZZ->5x2, 171ZZ->6x13, 171ZZ->9
ssc7 -> ssc2: 171ZU->35, 171ZZ->35
ssc7 -> ssc4: 171G->94, 171ZV->81x3, 171ZZ->105x2
ssc7 -> ssc5: 171ZU->122, 171ZZ->120x3
ssc7 -> ssc6: 171G->151, 171ZU->165x2, 171ZV->171ZNx2, 171ZZ->164, 171ZZ->165, 171ZZ->171ZAx2, 171ZZ->171ZBx2, 171ZZ->171ZLx2, 171ZZ->171ZN
ssc8 -> ssc1: Sch 1->1x2, Sch 1->10x3, Sch 1->11x4, Sch 1->14, Sch 1->2x3, Sch 1->4x5, Sch 1->4Ax2, Sch 1->4Bx2, Sch 1->6x2, Sch 1->8x2, Sch 2->17x3, Sch 2->2x3, Sch 2->3x2, Sch 2->5x2, Sch 2->8, Sch 3->5, Sch 4A->1x2, Sch 4A->2x3, Sch 4A->5, Sch 4A->6, Sch 4B->2x7, Sch 4B->6
ssc8 -> ssc2: Sch 1->35, Sch 1->35B, Sch 3->22, Sch 3->23A, Sch 4A->39Cx2
ssc8 -> ssc3: Sch 3->48Ax2, Sch 3->51ZAx2, Sch 4A->44x4, Sch 4A->44Ax3, Sch 4A->45x3, Sch 4A->48BB, Sch 4B->44x2, Sch 4B->44A, Sch 4B->44B, Sch 4B->45x7
ssc8 -> ssc4: Sch 1->100x2, Sch 1->102, Sch 1->103, Sch 1->105, Sch 2->64, Sch 2->72, Sch 2->83, Sch 2->88, Sch 2->89, Sch 2->94
ssc8 -> ssc6: Sch 1->159A, Sch 1->167x2
ssc9 -> ssc1: Sch 11->1, Sch 11->12, Sch 11->2, Sch 12->1, Sch 12->2, Sch 12->3x3, Sch 5->1x3, Sch 5->2, Sch 6->6, Sch 7->1, Sch 7->14A, Sch 7->2x2, Sch 7->3x2, Sch 7->6x3, Sch 9->1
ssc9 -> ssc2: Sch 11->30A, Sch 12->30Ax2, Sch 12->30C, Sch 12->40, Sch 12->41, Sch 7->27x2
ssc9 -> ssc3: Sch 5->47x6, Sch 5->51A, Sch 7->44, Sch 7->46, Sch 7->52, Sch 7->58, Sch 7->62
ssc9 -> ssc4: Sch 5->85x2, Sch 6->103x4, Sch 6->104, Sch 7->103x2, Sch 7->104x2, Sch 7->108x2, Sch 9->83
ssc9 -> ssc5: Sch 10->143, Sch 7->143
ssc9 -> ssc6: Sch 11->153x2, Sch 11->171
ssc9 -> ssc8: Sch 7->Sch 4x12
```

The keel line of the matrix (s 175 and s 176 naming sections of the other parts) is omitted: those are regulation-making powers and parliamentary control, which the keel recorded as inert machinery.
