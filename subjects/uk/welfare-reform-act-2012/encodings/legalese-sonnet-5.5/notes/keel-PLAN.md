# PLAN: the Welfare Reform Act 2012 (United Kingdom), 2012 c. 5, for the four part agents

Status (4 November 2026): written by the keel agent, row `iaw-wra-k`.
What it says about the core was generated from `wra-core.l4` by a script, so it cannot disagree with it; `wra-core.l4` and `wra-core-tests.l4` run with 0 errors on the stable `l4` 1.6.98 and on the main build 1.6.108, and `srcrefs.py --strict` finds 0 problems in them.
What it says about the text was checked against `inputs/ukpga-2012-5.txt`, which is a plain-text rendering made by a converter script, not the official text; nothing here is verified against the official text.
The seams in section 8 are by reading, not proved: a part that finds one wrong, or finds a missing one, says so in its `NOTES.md`.

## 1. What the keel delivers, and what it does not

- `wra-core.l4`: the nouns, and only nouns (`DECLARE`), importing `prelude` and `daydate`.
  Your module starts `IMPORT prelude`, `IMPORT daydate`, `` IMPORT `wra-core` ``.
- `wra-core-tests.l4`: proves every type in the core can be built and read back, and gives you copyable construction shapes (`WITH`, positional `OF`, `CONSIDER` over `Claimants`).
- This `PLAN.md`, `NOTES.md` (the keel's own) and `PROGRESS.md`.
- `wra-definitions.l4`: imports only and a header, defines nothing, because the keel's range is line 1 of the text, the enacting formula, and no definition of the Act falls in it.
  Every definition of the Act is in a part's range; section 9 says which part holds which.
  A part does not import it (a part imports the core only).
- No shared numeric constants: every number the Act states belongs to one provision, and a part cites it from its own text.
  The one pair that looks shared is "child means a person under the age of 16", stated in s 40 (wra1, raw line 432) and again in the ESA text s 57 inserts (wra2, raw line 1108); each part encodes its own.
  The four annual limits in s 96(5A) (raw lines 1536-1537) are wra4's.

## 2. Rules every part follows

1. **Names.**
   A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name.
   Every top-level name a part defines (function, constant, constructor, type not in the core) begins with the label of the provision it implements, in the Act's own numbering: `s 4(2)(a) ...`, `sch 3 para 2 ...`.
   Section 6 gives the label for text the Act inserts into another Act and for Schedule paragraphs.
   The names in the core (section 4) are taken: do not define them again.
2. **The core is read-only and nobody waits for it.**
   A part needing a type or constructor the core lacks defines it in its own module under its own label, and writes it in `NEEDS-CORE.md` in its sandbox (name, type, the provision, what it replaces); the lead hoists it into the core at the merge.
   Do not edit `wra-core.l4`.
3. **File names.**
   Every module of part `X` begins with `X-` (`wra1-ss1-12.l4`, `wra1-ss1-12-tests.l4`, ...); every module of the keel begins with `wra-`.
   `IMPORT` finds only modules in the importing file's own folder; a part cannot import another part.
4. **Ranges.**
   Every line of the raw text belongs to exactly one agent (table in section 3).
   A provision whose heading is in your range is yours, whatever it cites.
   If a provision of yours needs an answer another part computes, take it as an input named for the provision it comes from (section 8).
5. **Dates.**
   Write `Date day month year`; never define a `YMD`.
6. **Language.**
   The target is `main`; the stable binary is what you run.
   No `REFUSE`, no `BECAUSE` outside `LEST BREACH`, no `#ASSERT REFUSED`; parenthesise every `NOT`; one line per `#ASSERT`.
   `SET OF` and the ledger are not available.
   The brief's section "Writing L4 that the stable binary accepts" says the rest.

## 3. The parts

The ranges are copied unchanged from `inputs/PARTS.md` (1-based, inclusive, lines of the raw file).
Every line is in exactly one row.

| agent | line ranges | words |
| --- | --- | --- |
| keel | 1-1 | 38 |
| wra1 | 2-517, 2630-2922, 3050-3173 | 14054 |
| wra2 | 518-1343, 2923-3000, 3174-3236 | 15275 |
| wra3 | 1344-1519, 2475-2629, 3001-3049, 3237-3960 | 14576 |
| wra4 | 1520-2474 | 17120 |

What is in each range (headings of the raw text), what it means for the individual in the seat, and which core types to expect to use.
Every boundary between ranges falls on a Part or Schedule heading, so no section is split between two agents.

### wra1: Universal credit, and the schedules that wire it to the other working-age benefits

- Lines 2-517: Part 1 (ss 1-43): universal credit, claims, entitlement (basic and financial conditions), awards and their elements, claimant responsibilities (work-related requirements, sanctions, hardship payments), abolition of benefits (s 33), capability for work (s 37), couples (s 39), interpretation (s 40), regulations.
- Lines 2630-2922: Schedule 1 (supplementary regulation-making powers) and Schedule 2 (amendments of other Acts to make room for universal credit).
- Lines 3050-3173: Schedule 5 (dual entitlement, movement between working-age benefits, hardship payments, earnings tapers) and Schedule 6 (migration to universal credit).
- Seat topics: whether I am entitled to universal credit; what conditions I must meet (commitment, requirements, which group I am in); what happens if I do not (sanctions, hardship payments); whether I am a couple; being moved to universal credit (Schedule 6).
- Core types to expect to use: `Person`, `Place`, `Claimants`, `Two people`, `Relationship of two people`, `Household`, `Period`, `Award`, `Payment`, `Benefit`, `Work-related requirement`, `Group of claimants by requirement`, `Provision that reduces an award`, `Authority`.

Sections whose heading is in these ranges: 1 (line 5), 2 (line 15), 3 (line 21), 4 (line 28), 5 (line 46), 6 (line 53), 7 (line 61), 8 (line 69), 9 (line 85), 10 (line 91), 11 (line 98), 12 (line 115), 13 (line 129), 14 (line 141), 15 (line 151), 16 (line 156), 17 (line 176), 18 (line 196), 19 (line 208), 20 (line 228), 21 (line 234), 22 (line 243), 23 (line 252), 24 (line 264), 25 (line 279), 26 (line 284), 27 (line 309), 28 (line 337), 29 (line 349), 30 (line 369), 31 (line 371), 32 (line 373), 33 (line 381), 34 (line 393), 35 (line 395), 36 (line 397), 37 (line 400), 38 (line 418), 39 (line 420), 40 (line 429), 41 (line 456), 42 (line 479), 43 (line 493).
Schedules: Schedule 1 (line 2630), Schedule 2 (line 2680), Schedule 5 (line 3050), Schedule 6 (line 3092).

### wra2: the other working-age benefits

- Lines 518-1343: Part 2 (ss 44-63: jobseeker's allowance, employment and support allowance and income support changes, claimant commitments, sanctions and hardship payments in the interim period and after universal credit, entitlement to work) and Part 3 (ss 64-76: industrial injuries benefit, housing benefit, the social fund, state pension credit, working tax credit).
- Lines 2923-3000: Schedule 3 (consequential amendments on the abolition of benefits).
- Lines 3174-3236: Schedules 7 and 8 (consequential amendments).
- Seat topics: the person on jobseeker's allowance, employment and support allowance or income support who is asked to commit, to work-related requirements, who is sanctioned, who needs hardship payments; entitlement to work (ss 61-63); industrial injuries, housing benefit, social fund, pension credit and working tax credit changes as they touch that person.
- Most of the text is inserted into the Jobseekers Act 1995 and the Welfare Reform Act 2007; section 6 gives the label.
- Core types to expect to use: `Person`, `Claimants`, `Benefit`, `Work-related requirement`, `Group of claimants by requirement`, `Provision that reduces an award`, `Payment`, `Kind of payment`, `Authority` (especially `an employment officer`), `Decision`, `Kind of decision`.

Sections whose heading is in these ranges: 44 (line 521), 45 (line 578), 46 (line 580), 47 (line 684), 48 (line 686), 49 (line 689), 50 (line 877), 51 (line 884), 52 (line 909), 53 (line 919), 54 (line 923), 55 (line 944), 56 (line 947), 57 (line 960), 58 (line 1134), 59 (line 1138), 60 (line 1160), 61 (line 1165), 62 (line 1179), 63 (line 1193), 64 (line 1239), 65 (line 1254), 66 (line 1262), 67 (line 1275), 68 (line 1278), 69 (line 1282), 70 (line 1291), 71 (line 1306), 72 (line 1311), 73 (line 1318), 74 (line 1321), 75 (line 1328), 76 (line 1337).
Schedules: Schedule 3 (line 2923), Schedule 7 (line 3174), Schedule 8 (line 3229).

### wra3: personal independence payment, miscellaneous, final provisions, and the schedules of amendment

- Lines 1344-1519: Part 4 (ss 77-95): personal independence payment (components and rates, the ability questions, the required period condition, terminal illness, pensionable age, care homes, hospitals, prisoners, claims, abolition of disability living allowance, transitional, regulations, interpretation).
- Lines 2475-2629: Part 6 (ss 135-146: Tell Us Once, child support maintenance, fees, individual voluntary arrangements, standards of decision-making, jobcentres and the sex industry, child poverty) and Part 7 (ss 147-151: repeals, financial provision, extent, commencement, short title).
- Lines 3001-3049: Schedule 4 (the housing credit element of state pension credit).
- Lines 3237-3960: Schedules 9 to 14 (personal independence payment amendments and transitional provision; consideration of revision before appeal; supersession; the Social Mobility and Child Poverty Commission; repeals).
- Seat topics: whether I am entitled to the daily living component or the mobility component and at which rate; terminal illness; when I am not paid (pensionable age, care home, hospital, prison); the effect of a fixed-term award; the person paying or receiving child support maintenance (Part 6), as the text reaches them.
- Core types to expect to use: `Person`, `Place`, `Component of personal independence payment`, `Rate of a component`, `Entitlement to a component`, `Benefit`, `Award`, `Period`, `Authority`, `Decision`, `Kind of decision`, `Step after a decision`.
- Schedule 14 is a long run of repeals (raw lines 3657-3959): disposition `repealed or blank in this text` is NOT automatically right; a repeal of an Act's text is machinery (inert reason 2: amendments of other Acts), and the coverage row must say so with the reason.

Sections whose heading is in these ranges: 77 (line 1346), 78 (line 1354), 79 (line 1369), 80 (line 1387), 81 (line 1409), 82 (line 1424), 83 (line 1436), 84 (line 1442), 85 (line 1447), 86 (line 1459), 87 (line 1465), 88 (line 1468), 89 (line 1473), 90 (line 1478), 91 (line 1480), 92 (line 1482), 93 (line 1490), 94 (line 1493), 95 (line 1509), 135 (line 2477), 136 (line 2492), 137 (line 2499), 138 (line 2514), 139 (line 2523), 140 (line 2529), 141 (line 2535), 142 (line 2543), 143 (line 2548), 144 (line 2551), 145 (line 2561), 146 (line 2563), 147 (line 2580), 148 (line 2582), 149 (line 2587), 150 (line 2599), 151 (line 2628).
Schedules: Schedule 4 (line 3001), Schedule 9 (line 3237), Schedule 10 (line 3357), Schedule 11 (line 3393), Schedule 12 (line 3493), Schedule 13 (line 3528), Schedule 14 (line 3657).

### wra4: the benefit cap, claims, appeals, recovery, fraud and information-sharing

- Lines 1520-2474: Part 5 (ss 96-134): the benefit cap (ss 96-97), claims and awards (98-99), payments (100-101), appeals (102-103: consideration of revision before appeal), electronic communications (104), recovery of benefit payments (105-109: overpayments, deduction from benefit and from earnings, court action), investigation and prosecution (110-112), penalties as an alternative to prosecution (113-115) and civil penalties (116), loss of benefit for benefit offences (117-121), tax credit fraud and transfer of functions (122-126), information-sharing (127-134).
- Seat topics: whether my benefits are capped and by how much (s 96); what can be recovered from me and how (ss 105-109); how a decision about me is revised or appealed (ss 102-103; the benefit cap decision carries no right of appeal, s 97(6)); penalties and loss of benefit (ss 113-121); what may be shared about me (ss 127-134).
- Core types to expect to use: `Person`, `Place` (`Greater London`), `Claimants`, `Household`, `Benefit`, `Award`, `Payment`, `Kind of payment`, `Period`, `Employer`, `Authority`, `Decision`, `Kind of decision`, `Step after a decision`, `Way of recovering an amount`.

Sections whose heading is in these ranges: 96 (line 1522), 96A (line 1572), 97 (line 1589), 98 (line 1600), 99 (line 1608), 100 (line 1618), 101 (line 1623), 102 (line 1631), 103 (line 1660), 104 (line 1666), 105 (line 1674), 106 (line 1781), 107 (line 1822), 108 (line 1826), 109 (line 1837), 110 (line 1844), 111 (line 1849), 112 (line 1853), 113 (line 1886), 114 (line 1902), 115 (line 1913), 116 (line 1918), 117 (line 1957), 118 (line 1965), 119 (line 1990), 120 (line 2026), 121 (line 2157), 122 (line 2165), 123 (line 2170), 124 (line 2179), 125 (line 2202), 126 (line 2204), 127 (line 2241), 128 (line 2286), 129 (line 2305), 130 (line 2333), 131 (line 2362), 132 (line 2422), 133 (line 2446), 134 (line 2468).
Schedules: .

## 4. The core, name by name

These names are taken.
Types are in backticks when they have spaces; every constructor and every field name is also taken.
(Generated from `wra-core.l4`.)

- type `Place` (enumeration): `Greater London`; `England outside Greater London`; `Scotland`; `Wales`; `Northern Ireland`; `outside the United Kingdom`
- type `Person` (record): `reference`; `age in years`; `date of birth`; `where the person is`; `where the person lives`
- type `Relationship of two people` (record): `married to each other or civil partners of each other`; `members of the same household`; `living together as if married or civil partners`
- type `Two people` (record): `the first person`; `the second person`; `their relationship`
- type `Claimants` (enumeration): `a single claimant`; field `the single claimant`; `joint claimants`; field `the joint claimants`
- type `Household` (record): `the claimants`; `the children and young persons`
- type `Employer` (record): `the employer's reference`
- type `Authority` (enumeration): `the Secretary of State`; `an authorised person`; `an employment officer`; `Her Majesty's Revenue and Customs`; `a local authority`; `the First-tier Tribunal`; `the Upper Tribunal`; `a court`; `the Director of Public Prosecutions`
- type `Benefit` (enumeration): `universal credit`; `contribution-based jobseeker's allowance`; `income-based jobseeker's allowance`; `contributory employment and support allowance`; `income-related employment and support allowance`; `income support`; `housing benefit`; `council tax benefit`; `child tax credit`; `working tax credit`; `state pension credit`; `housing credit`; `personal independence payment`; `disability living allowance`; `industrial injuries benefit`; `social fund payment`; `child benefit`; `guardian's allowance`; `bereavement allowance`; `incapacity benefit`; `maternity allowance`; `severe disablement allowance`; `widow's pension`; `widowed mother's allowance`; `widowed parent's allowance`
- type `Period` (record): `first day`; `last day`
- type `Award` (record): `the benefit awarded`; `who it is awarded to`; `the period awarded for`; `the amount awarded for the period, in pounds`
- type `Kind of payment` (enumeration): `a payment of an award`; `a payment on account`; `a hardship payment`
- type `Payment` (record): `the kind of payment`; `the benefit paid`; `the person it was paid to`; `the period paid for`; `the amount paid for the period, in pounds`
- type `Work-related requirement` (enumeration): `work-focused interview requirement`; `work preparation requirement`; `work search requirement`; `work availability requirement`
- type `Group of claimants by requirement` (enumeration): `no work-related requirements`; `work-focused interview requirement only`; `work-focused interview and work preparation requirements only`; `all work-related requirements`
- type `Provision that reduces an award` (enumeration): `universal credit higher-level sanction`; `universal credit other sanction`; `jobseeker's allowance higher-level sanction`; `jobseeker's allowance other sanction`; `jobseeker's allowance ceasing to be available`; `jobseeker's allowance higher-level sanction after universal credit`; `jobseeker's allowance other sanction after universal credit`; `employment and support allowance interim sanction`; `employment and support allowance sanction`; `income support sanction`
- type `Component of personal independence payment` (enumeration): `daily living component`; `mobility component`
- type `Rate of a component` (enumeration): `standard rate`; `enhanced rate`
- type `Entitlement to a component` (record): `the component`; `the rate`
- type `Kind of decision` (enumeration): `a decision on entitlement to a benefit or on its amount`; `a decision on limited capability for work or work-related activity`; `a decision on ability to carry out daily living or mobility activities`; `a decision to apply the benefit cap`; `a decision that an amount is recoverable or on how much`; `a decision on the amount payable after loss of benefit for an offence`
- type `Decision` (record): `the kind of decision`; `the decision-maker`; `the benefit concerned`; `the date it was made`
- type `Step after a decision` (enumeration): `revision`; `supersession`; `consideration of revision before an appeal`; `appeal to the First-tier Tribunal`; `appeal to the Upper Tribunal`
- type `Way of recovering an amount` (enumeration): `deduction from benefit`; `deduction from earnings`; `court action`; `adjustment of benefit`

Conventions the core fixes (comments at its head):

- money is a `NUMBER` of pounds sterling, and a rate is per week unless its name says otherwise;
- a span of days is a `Period` (both ends count);
- a record holds facts a witness could state; whether the Act's test is met is a rule, and belongs to a part;
- `Person` is used for every natural person, a child included: "child" (s 40, raw line 432: "a person under the age of 16") is a rule in wra1, not a type, and `age in years` is completed years;
- `Claimants` says how the claim is made, not what the people are: a member of a couple may claim as a single person (s 2(2));
- jobseeker's allowance and employment and support allowance are two constructors each, because s 33(1)-(2) separates the income-based and income-related forms from the allowance in general; "jobseeker's allowance" without a qualifier in the text means both constructors;
- for a Hohfeldian `Jural relations` row, name the individual by the person's role ("the claimant", "the employee") and the other party by an `Authority` constructor or `the employer`.

## 5. Reading the raw text

Facts about this rendering, each checked on the file; the first four are traps.

1. **Inserted text keeps its host Act's section numbers, and the quote marks are gone.**
   Where a section says "after section 19 there is inserted" the inserted section begins on a line `NN<tab>Title` and looks exactly like one of the Act's own sections (raw line 582: `19<tab>Higher-level sanctions` is section 19 of the Jobseekers Act 1995, inserted by s 46).
   The Act's own sections are exactly the lines `N<tab>Title` that run 1, 2, 3, ... 151 in order (with 96A); the lists in section 3 give them with their line numbers.
   Inserted text ends where the Act's next subsection of the amending section begins (raw line 1761: `(2) In section 71 of that Act` is s 105(2), after the inserted 71ZH ends at line 1760).
2. **Schedule paragraph numbers are not printed.**
   Only sub-paragraph numbers and cross-headings appear.
   Where a Schedule gives one paragraph per cross-heading, count them: the Act's own cross-references are consistent with the count for Schedules 1, 5, 6 and 10.
   s 43(3)(l) says "paragraph 4 of Schedule 1 (calculation of capital and income)", s 43(3)(m) says "paragraphs 4, 5 and 6 of [Schedule 6]", and Schedule 5 paragraph 4 cites "paragraph 2(3)(b) or 3(b)".
   So: **Schedule 1** paragraphs are Entitlement of joint claimants 1, Linking periods 2, Couples 3, Calculation of capital and income 4, Responsibility for children etc 5, Vouchers 6, Work-related requirements 7, Good reason 8; **Schedule 5** General 1, Dual entitlement 2, Movement between working-age benefits 3, Hardship payments 4, Earnings tapers 5; **Schedule 6** General 1, Claims before the appointed day 2, Claims after the appointed day 3, Awards 4, Work-related requirements and sanctions 5, Tax credits 6, Supplementary 7; **Schedule 10** General 1, Claims before the appointed day 2, Claims after the appointed day 3, Awards 4, Supplementary 5 (para 1(1) is cited in the text).
   For a Schedule not listed here, count the cross-headings, and in `NOTES.md` say the number is derived and that the raw text does not print it.
   The definition of "sanction" with the long list is therefore Schedule 6 **paragraph 5(4)** (raw lines 3144-3167).
3. **A line of dots is a repealed or blank subsection.**
   `(1A) . . . . . .` (s 10(1A), raw line 93; s 12(2)(a), line 118; s 21(5), line 242; s 39(2), line 424; s 96(6)-(8) and (11), lines 1544-1546 and 1571; s 96A(9), line 1588; s 97(3) and (5), lines 1592 and 1595) is "repealed or blank in this text"; say what the text shows and do not guess what it once said.
   A word replaced by dots inside a provision (s 10(4) "...", raw line 96; s 11(3)(a) "...", line 105) is a deletion: the sentence stands as printed.
4. **The text may carry two extent versions, and prospective provisions.**
   `ukpga-2012-5.meta.json` says so in terms.
   A provision that seems to say two things (for example a list with an item (aa) or (za) among lettered limbs) may be two versions, not a fork; say what you saw and encode the text as printed.
5. Headings: a leading tab with no number is a Part, Chapter or cross-heading (an italic heading in the official text); `SCHEDULE N — Title` begins a Schedule; a second `SCHEDULE 1` inside Schedule 13 (raw line 3565) is Schedule 1 to the Child Poverty Act 2010, inserted by Schedule 13, not Schedule 1 to this Act.
6. The enacting formula (line 1) says "Queen's"; the text elsewhere says "Her Majesty's Revenue and Customs" and "Welsh Ministers"; quote what is printed.
7. Stray marks: s 40's "secondary legislation" entry ends `”;` with an unmatched closing quote (raw line 444); some defined terms are closed with an opening-style quote (raw lines 277 and 788: `“victim of domestic violence“`, `“domestic violence“`). Quote them as they are.

## 6. Labels

The label is the first thing in every top-level name, so that no two parts can collide and a reader holding the text finds the rule.

| what you encode | label | example name |
| --- | --- | --- |
| a section, subsection, paragraph of the Act | `s 4(2)(a)` | `` `s 4(1)(a) the person is at least 18 years old` `` |
| a Schedule paragraph (number counted as in section 5) | `sch 6 para 5(4)` | `` `sch 6 para 5(4) the reduction is a sanction` `` |
| a Schedule paragraph whose number you derived but the Act does not cite | `sch 1 para 3(1)(a)` and say so in NOTES.md | |
| text the Act inserts into another Act | the Act's section, a short name for the host Act, the inserted provision's own number | `` `s 105 SSAA 71ZB(1)(a) the amount is recoverable` ``, `` `s 46 JSA 19(2)(a) the failure is sanctionable` ``, `` `s 57 WRA2007 11J(2)(a) the failure is sanctionable` `` |
| a definition | the section, then `means` or the term | `` `s 39(1) the two people are a couple` `` |

Short names for host Acts (use these, so that two parts name the same Act the same way): `JSA` Jobseekers Act 1995; `WRA2007` Welfare Reform Act 2007; `SSAA` Social Security Administration Act 1992; `SSCBA` Social Security Contributions and Benefits Act 1992; `SSA1998` Social Security Act 1998; `SSFA` Social Security Fraud Act 2001; `TCA` Tax Credits Act 2002; `SPCA` State Pension Credit Act 2002; `CSA1991` Child Support Act 1991; `CMOPA` Child Maintenance and Other Payments Act 2008; `WRA2009` Welfare Reform Act 2009.
Any other host Act: its initials and year, once, in the file's header.
The host Acts are not among the sources: what a host Act's own text says is a borrowed fact, asked as an input.
Labels of the shapes in this table, with parentheses and spaces inside a backtick name, parse on the stable binary and on main 1.6.108 (checked on nine sample names).
A function's name says what it answers and claims no more than the section says: `s 3(1) the single claimant is entitled to universal credit`, not `is the claimant entitled`.

## 7. Values the regulations supply

Most of this Act says "regulations may" or "as may be prescribed".
So a rule that depends on such a value:

- takes the value as a `GIVEN ... IS A MAYBE NUMBER` (or `MAYBE BOOLEAN`, `MAYBE Date`), named for the provision that points to it: `` `the age regulations prescribe under s 4(3)` ``;
- answers `NOTHING` when the value is `NOTHING` (the case "points outside the text"), and answers from the value when it is `JUST n`;
- never puts a number the Act does not state, and never reads a regulation from memory.

The amounts in s 96(5A) are the Act's own numbers and may be used by wra4; which of the two figures in each pair applies is left to regulations by s 96(5B)(a) (raw lines 1539-1541), so that choice is an input, not a guess.

## 8. The seams

A seam is a provision in one part whose answer another part's provision needs.
A part cannot import another part, so the dependent part takes the answer as an input, named for the section it comes from, and the lead wires it at the merge.
Each row: asking section (raw line), answering section (raw line), the input and its type.

| # | asking | answering | the input (name, type) |
| --- | --- | --- | --- |
| 1 | wra2: ESA text s 57 inserts: 11D(2)(c) "a single person responsible for a child under the age of 1" (line 1012), 11E(1)(a) (line 1020), and the definition of "single person" in WRA2007 s 24(1) (line 1109): "not a member of a couple (within the meaning of Part 1 of the Welfare Reform Act 2012)" | wra1: s 39(1) (lines 421-423) | `` `s 39(1) the person is a member of a couple` `` : `BOOLEAN` |
| 2 | wra4: s 96(2) (line 1524) "total entitlement to welfare benefits ... exceeds the relevant amount", and s 96(10) whose list includes "universal credit" (line 1567) | wra1: s 8(1) (lines 70-72) the amount of an award of universal credit | `` `s 8(1) the amount of the award of universal credit for the period` `` : `NUMBER` (pounds), one per `Award` of `universal credit` in the reference period |
| 3 | wra4: s 105 inserting SSAA 71ZB(1)(a) "universal credit ... paid in excess of entitlement" (lines 1678-1679) and 71ZB(5) (line 1691) | wra1: s 3 (lines 22-27) entitlement; s 8(1) the amount | `` `s 3 the claimant is entitled to universal credit for the period` `` : `BOOLEAN`; and the NUMBER of seam 2 |
| 4 | wra4: s 105 inserting SSAA 71ZH(1)(a) "a payment under section 28 ... which is recoverable under that section" (line 1750) | wra1: s 28(2)(f) (line 347): whether hardship payments are recoverable is left to regulations | `` `s 28(2)(f) the hardship payment is recoverable under section 28` `` : `BOOLEAN` (the regulations' answer, supplied) |
| 5 | wra4: s 105 inserting SSAA 71ZH(1)(b) "a payment under section 19C of the Jobseekers Act 1995 ... recoverable under that section" (line 1751) | wra2: s 46 inserting JSA 19C(2)(f) (line 670): left to regulations | `` `s 46 JSA 19C(2)(f) the hardship payment is recoverable under section 19C` `` : `BOOLEAN` |
| 6 | wra4: s 105 inserting SSAA 71ZH(1)(c)-(e) (lines 1752-1754): JSA Sch 1 paras 8, 8A, 9, 10 and SSFA sections | no part (the host Acts are not among the sources) | `` `s 105 SSAA 71ZH(1)(c) the payment is recoverable under paragraph 9 of Schedule 1 to the Jobseekers Act 1995` `` and its siblings : `BOOLEAN` each |
| 7 | wra4: ss 117-119 amend SSFA 6A, 6B, 7: the lists of "disqualifying benefit" (lines 1959-1961: adds child tax credit and working tax credit) and "sanctionable benefit" (1962-1964: adds the same two) and the conditions "where the sanctionable benefit is universal credit" | wra1: Schedule 2 amending the same SSFA sections (lines 2865-2916) adds universal credit to "disqualifying benefit" (za) and makes the 6B(5A), 7(2A), 9(2A) regulations | **a composite**: each part encodes only its own limb and answers `NOTHING` (list not closed) for a benefit named by the other part's limb; the lead writes the composite function at the merge (section 10) |
| 8 | wra4: s 102 (lines 1631-1659) inserts SSA1998 12(3A): a right of appeal only if the Secretary of State has considered whether to revise | wra3: Schedule 11 (lines 3393-3492) makes similar amendments to five other Acts; s 103 (lines 1660-1664) and Schedule 12 (lines 3493-3527) supersession | the shared reading (below), not an input; both parts take `` the regulations require consideration of revision before an appeal `` as `MAYBE BOOLEAN` and `` the Secretary of State has considered whether to revise `` as `BOOLEAN` |
| 9 | wra1: Schedule 5 para 1(2)-(3) (lines 3055-3062) and Schedule 6 para 5(4) (lines 3144-3167) define "work-related requirement" and "sanction" by naming sections that wra2's ss 46, 49, 57 insert | wra2: JSA 19, 19A, 19B, 6J, 6K; WRA2007 11J | no input: the list is the core's `Provision that reduces an award` and `Work-related requirement`; wra1 writes its definitions over the core types, wra2 maps each inserted section to one constructor in its own NOTES.md |
| 10 | wra1: Schedule 6 para 1(3) "appointed day" = the day appointed for s 1 (line 3098); wra2: which regime applies, "for interim period" (lines 520, 922) or "after introduction of universal credit" (lines 688, 959); wra3: Schedule 10 para 1(2) the day appointed for s 77 (line 3360) | wra3: s 150(3)-(4) (lines 2619-2627): appointed by order, different days for different areas | `` `s 150(3) the day appointed for the coming into force of section 1` `` : `MAYBE DATE` (wra1, wra2); the Act's own commencement is otherwise machinery, and every part assumes the provisions it encodes are in force |

The reading for seam 8, so that wra3 and wra4 do not diverge: where regulations say so, there is a right of appeal against a decision only if the Secretary of State has considered whether to revise it (SSA1998 12(3A), raw line 1638); "is there a right of appeal" is `NOTHING` when the input "the regulations require consideration of revision first" is `NOTHING` (no regulations among the sources) or `JUST FALSE` (the right to appeal then comes from SSA1998 s 12(2), which is not among the sources); it is `JUST FALSE` when that input is `JUST TRUE` and the Secretary of State has not considered revision (a failed "only if": a lawyer's reading (a), so list the branch under `## Marginal readings for a lawyer`); and `NOTHING` when that input is `JUST TRUE` and consideration was done (the "only if" is a necessary condition, and the Act does not say what else gives the right).

Two things that look like seams and are not:

- wra1 s 4(1)(b), s 4(4) (lines 31, 37) "the qualifying age for state pension credit" and wra3 s 83(2) (line 1438) "pensionable age ... or, if higher, 65" each borrow from another Act (SPCA 2002 s 1(6), Pensions Act 1995 Sch 4).
  Each part asks the borrowed fact as its own `BOOLEAN`; the lead may merge the two questions on the website.
- wra4 s 96(10) defines its own "couple" ("two persons of a prescribed description", line 1552) and "single person" (line 1555); wra1 s 39 defines "couple" differently.
  Do not connect them: s 96's couple is `NOTHING` unless the description is an input.

## 9. Which part holds which definition

Every definition of the Act is in a part's range.
(Census made by searching the raw text for "means", "has the meaning", "is to be construed", "has such meaning as may be prescribed" and mapping each hit to its range; repeal notes and amendments to a definition in another Act are not counted. A part that finds one the census missed adds it to its coverage table.)

- **wra1** (Part 1, Schedules 1, 2, 5, 6): s 7(2) assessment period (63); s 7(4) period of entitlement (68); s 4(6)(a) receiving education (43, left to regulations); s 10(5) qualifying young person (97); s 13(2) work-related requirement (131); s 14(1) claimant commitment (142); ss 15(1), 16(1), 17(1), 18(1) the four requirements (152, 157, 177, 197); s 16(5)-(6) work-focused health-related assessment, health care professional (168, 171); s 18(2) available for work (198); s 19(6) responsible carer (223); s 24(6) domestic violence, victim, recently a victim (276-278); s 27(6) compliance condition (324); s 33(2) income-based jobseeker's allowance, income-related employment and support allowance (390-391); s 37(1)-(2) limited capability for work, for work-related activity (401-406); s 39(1) couple (421); **s 40, the interpretation section (429-454)**; Schedule 5 para 1(1)-(3) (3051-3062); Schedule 6 paras 1(2)-(3) and 5(4) (3095-3098, 3144-3167); the definitions Schedule 2 inserts into other Acts (2750-2760, 2773, 2846).
- **wra2** (Parts 2 and 3, Schedules 3, 7, 8): JSA 9(1) claimant commitment (526); 19A(11) jobseeker's direction, training scheme, employment programme (637); JSA 6 and 6B-6E, the same four requirements (696-748); JSA 6H domestic violence (788-789); JSA 19A(6) and 6K compliance condition (621, 833); JSA 35(1) (867-872); ESA 1A(2) relevant maximum number of days (888); ESA 1C, 11, 11B-11D, 11H, 11J(5) (929-1072); **ESA 24(1) interpretation (1106-1113), including "child" and "single person"**; IS 124A (1147); s 64-67 industrial injuries benefit (1251, 1267, 1272); s 69 (AMHB, local authority); s 76(3) (1341-1343); Schedule 3 (2950, 2957); Schedule 7 (3190).
- **wra3** (Part 4, Parts 6-7, Schedules 4, 9-14): s 78(3)-(4) and 79(3)-(4) rates and activities (1362-1381); s 80(6) negative determination (1406); s 81(2)-(3) the relevant ability, assessed, the previous 3 months, the next 9 months (1413-1419); s 82(4) terminally ill (1430); s 83(2) the relevant age (1438); s 85 care home, qualifying services, specified enactment, enactment (1450-1458); s 92(3) (1488-1489); **s 95, the interpretation section (1509-1519)**; Schedule 10 para 1(2) the appointed day (3360); Schedules 11 and 12 appeal tribunal, Commissioner (3502-3527); Schedule 4 housing credit (3032); Part 6 and Schedule 13 definitions (3633-3635).
- **wra4** (Part 5): s 96(3) reference period (1525); s 96(5A) annual limit (1535); **s 96(10) couple, prescribed, regulations, single person, welfare benefit (1551-1570)**; 71ZD(2) earnings (1708) and its siblings (1784, 1803, 1820); 115C-D definitions (1936-1940); SSFA 6A (1958), 6B(14) relevant offence (1975); 6B(13) disqualifying event; 36A-36D (2013-2115); s 121 cautioned (2156); s 126 (2235-2238); s 127 (2263-2273); s 128 (2299-2301); s 131 (2400-2417); s 133 (2448-2457).

Every part writes its definitions as functions or tables returning "the term's meaning as the Act states it", with a test for each entry.
A definition that points at regulations ("has such meaning as may be prescribed": "disabled" 436, "regular and substantial caring responsibilities" 442, "severely disabled" 445, "work" 448, "domestic violence" 276) is `NOTHING`-kind (points outside the text); one that says "means" is `FALSE`-kind for what it excludes only if the text closes the list.

## 10. For the lead, at the merge

- Hoist what `NEEDS-CORE.md` files ask for, checking that no two parts asked for the same name.
- Write the composite functions the seams call for: the SSFA "disqualifying benefit" and "sanctionable benefit" lists (seam 7), and the shared reading of seam 8 if wra3 and wra4 differ.
- Check that no top-level name in two parts is the same, and that no name starts without a label.
- `check.sh` over the merged directory with the stable binary and the main build.
- The keel did not read any existing encoding of any Act; nor should the parts.

## 11. Difficulties the parts will meet

1. **"No" is rare.**
   The Act is mostly "regulations may", "such as may be prescribed", "as the Secretary of State thinks fit".
   Most functions answer `NOTHING` unless the caller supplies the regulation's value (section 7).
   A function that answers `JUST FALSE` needs a quoted FALSE-kind phrase in the text; "regulations may provide for exceptions to subsection (1)" (s 4(2), raw line 35) does not turn the basic conditions into `FALSE`: it makes the "no" provisional.
2. **Who is the individual.**
   Many provisions address the Secretary of State ("the Secretary of State may impose ...", s 15(4), s 24). Encode what they mean for the claimant (what may be done to them, what they must be given, by when) and take the Secretary of State's judgment ("in the opinion of the Secretary of State", s 15(3), s 16(1)) as a plain input.
3. **Two text-bearing layers.**
   ss 44-49, 50-57, 105-106, 113-121, Schedules 2, 3, 7, 9, 11, 12 are text inserted into or amended in other Acts; the host Act's other sections are not among the sources.
   What the host Act's other sections say is a borrowed fact, asked as an input.
4. **A Schedule of amendments can create a right.**
   Most amendment text is machinery (inert reason 2), but a Schedule that inserts a rule the individual meets (for example SSA1998 Sch 3 paras 6A and 6B, "a decision as to the amount of payment recoverable ... " lines 1776-1780, which says an appeal lies) is encoded for what it means, not skipped.
5. **The benefit cap's figures.**
   s 96(5A) has two pairs of figures; the Act does not say which of each pair applies to whom (s 96(5B)(a) leaves it to regulations).
   This is not a fork, since the text is unambiguous that regulations pick the figure: it is `NOTHING`-kind (points outside the text), and the answer is `NOTHING` unless an input names the figure.
   Seams 7 and 8 are likewise not forks: they are two parts that must agree, and each part says so in its `NOTES.md` without a fork-register entry.
6. **Terms that look alike across regimes are different.**
   "limited capability for work" is defined in s 37 (UC) and used without a definition in the ESA text s 57 inserts (WRA2007 11D(2)(a), whose own definition is not among the sources); "work-related requirement" is defined five times (s 13(2), JSA 6(2), ESA 11(2), Sch 5 para 1(2), Sch 6 para 5(4)); "claimant commitment" at least five times (s 14, JSA 9 and 6A, ESA 1C and 11A, IS 124A).
   Each part encodes the definition in its own range and says in `NOTES.md` that the others exist.
7. **Time.**
   "the previous 3 months ending with the prescribed date" and "the next 9 months" (s 81) and "13 weeks", "26 weeks", "three years" in the sanction sections are Act numbers; the prescribed date is an input.
   Use `Date day month year` and `Period` from the core; do not use `Days in a month` for a legal period.
8. **The seat is the individual.**
   No seat for the Secretary of State, a tribunal or a court.
   A provision that gives a tribunal power (SSA1998 12) is encoded for what the individual may do or have done to them.

## 12. Shapes: the FALSE and NOTHING answer, a prescribed value, a test

The module below was compiled and run on the stable binary and on the main build (6 assertions satisfied on each, 0 errors); "s 999" is an invented provision, so nothing in it is a reading of the Act.
Copy the shape: the label first in the name, a comment on every branch saying which kind of answer it is and why, a `MAYBE` input for the value regulations supply, expected values written from the text and not from the output.

```l4
IMPORT prelude
IMPORT daydate
IMPORT `wra-core`

-- Shape only. "s 999" is an invented provision, not part of the Act:
--   "(1) A person is not entitled to the widget payment while outside Great Britain, unless regulations provide otherwise.
--    (2) A person is entitled to the widget payment if the person is at least the prescribed age."

§ `s 999 -- shape only`

-- the label ("s 999(1)") comes first in every top-level name; the gloss in the name says what the function answers
GIVEN `the person` IS A Person
      `regulations provide that the person is entitled anyway` IS A MAYBE BOOLEAN  @desc Do regulations made under s 999(1) provide that this person is entitled anyway? Leave out if not known.
GIVETH A MAYBE BOOLEAN
`s 999(1) the person is not barred from the widget payment by being outside Great Britain` MEANS
    BRANCH
        -- FALSE-kind (the text says no in its own words): "is not entitled ... while outside Great Britain" (a flat negative, with "unless")
        IF   `s 999(1) the person is outside Great Britain` `the person`
        THEN CONSIDER `regulations provide that the person is entitled anyway`
             WHEN JUST TRUE  THEN JUST TRUE
             WHEN JUST FALSE THEN JUST FALSE
             -- NOTHING-kind (points outside the text): regulations are not among the sources
             WHEN NOTHING    THEN NOTHING
        OTHERWISE JUST TRUE

GIVEN `the person` IS A Person
GIVETH A BOOLEAN
`s 999(1) the person is outside Great Britain` MEANS
    CONSIDER `the person`'s `where the person is`
    WHEN `outside the United Kingdom` THEN TRUE
    WHEN `Northern Ireland`           THEN TRUE
    OTHERWISE FALSE

GIVEN `the person` IS A Person
      `the age regulations prescribe` IS A MAYBE NUMBER
GIVETH A MAYBE BOOLEAN
`s 999(2) the person has reached the prescribed age` MEANS
    CONSIDER `the age regulations prescribe`
    WHEN JUST n THEN JUST (`the person`'s `age in years` AT LEAST n)
    -- NOTHING-kind (points outside the text): the age is left to regulations
    WHEN NOTHING THEN NOTHING

`a person in Wales` MEANS Person WITH
    `reference` IS "P1"
    `age in years` IS 30
    `date of birth` IS Date 1 1 1996
    `where the person is` IS Wales
    `where the person lives` IS Wales

`a person in Northern Ireland` MEANS Person WITH
    `reference` IS "P2"
    `age in years` IS 17
    `date of birth` IS Date 1 1 2009
    `where the person is` IS `Northern Ireland`
    `where the person lives` IS `Northern Ireland`

-- expected values are written from the invented text above, not from the output
#ASSERT `s 999(1) the person is not barred from the widget payment by being outside Great Britain` `a person in Wales` NOTHING EQUALS JUST TRUE
#ASSERT `s 999(1) the person is not barred from the widget payment by being outside Great Britain` `a person in Northern Ireland` (JUST FALSE) EQUALS JUST FALSE
#ASSERT `s 999(1) the person is not barred from the widget payment by being outside Great Britain` `a person in Northern Ireland` NOTHING EQUALS NOTHING
#ASSERT `s 999(2) the person has reached the prescribed age` `a person in Wales` (JUST 18) EQUALS JUST TRUE
#ASSERT `s 999(2) the person has reached the prescribed age` `a person in Northern Ireland` (JUST 18) EQUALS JUST FALSE
#ASSERT `s 999(2) the person has reached the prescribed age` `a person in Wales` NOTHING EQUALS NOTHING
```

Quote lines and `@ref` locators: use `python3 -I srcrefs.py quote <raw text> N M` for the quote and `@ref s 4(1)(a) (src:N-M)` directly above the first declaration it supports, as `encoding-a-subject/references/source-locators.md` shows; the keel's `wra-core.l4` follows it and passes `srcrefs.py check --strict`.
