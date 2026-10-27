# NOTES: State Pension Credit Act 2002 (2002 c. 16), encoding `legalese-sonnet-5.5`

**Status: draft.**
Not reviewed: no domain expert has read this encoding against the text, and no one other than the encoder (a single Sonnet 5.5 agent working alone from the brief, run `porridge-uk-spc-b`) has run it.

**The source text is a converter rendering, not the official text.**
`../../registers/source-bundle/ukpga-2002-16.txt` was made by a converter script from the legislation.gov.uk XML (`ukpga/2002/16`, point in time 2026-07-01, text sha256 `4d2d31656101f648c285a1b12de66d93b56ad3e69d125edb70e214293c877bf6`; `inputs/SOURCES.md`).
Nothing here is verified against the official text.
The meta file lists one outstanding effect the register has not applied ("s. 3A(5)(a) words omitted by Welfare Reform and Work Act 2016 s. 20(8), in force 2018-04-06") and 24 prospective effects.
There is no section 3A in the deposited text; the only mention of a "section 3A" is the Jobseekers Act 1995's, inside Schedule 2 paragraph 38, which the text shows as repealed, so I have not been able to place that effect and have applied nothing for it.

The edition encoded is the deposited text exactly as it stands; where the text itself shows `{repealed: ...}` or a row of dots, that is what the coverage table says.
Layer-1 modules quote the text mechanically (`-- src:N | ...` lines copied by `srcrefs.py quote`), and `srcrefs.py check` reports 0 problems.

## Seat

**The seat is a person who is, or is about to be, of an age to claim State Pension Credit, asking whether they are entitled to it, how much, and what they must do or tell the authorities.**

Why this seat: state pension credit is a benefit one claims, so the natural reader is the claimant, a person of or near the qualifying age (a woman's pensionable age; for a man, the age that is pensionable age for a woman born the same day).
The Act speaks mostly to the Secretary of State (he "shall specify", he "need not", regulations "may"); the seat layer asks what each of those means for the person: whether the duty applies to them, whether it can be done to them, what they are owed and from when.
There is no seat for an official.
A partner is not a second seat: the partner's facts enter as inputs (the Act counts a couple together), because the Act's entitlement is the claimant's.

The seat layer is `spc-seat.l4` (28 `@export` questions, plain inputs with `@desc`, built from the Act's records inside each question) and `spc-cases-seat.l4` (a real person's facts through every question).
It calls the layer-1 rules and states no rule of the Act; no layer-1 module was changed to suit it, with one exception recorded as fork F-23: while writing the seat I found that two layer-1 rules answered an amount where the Act is silent, and corrected the rules (and their tests, before rerunning) in layer 1.
The seat questions are listed under "Seat questions" below.

### Hohfeld pairs in the seat layer

The person's claim is the Secretary of State's duty, and the Act's duties fall on the Secretary of State (to pay, to specify a period, to pay the changed amount without a new decision).
Each is asked from the person's side: "Am I entitled...", "How much...", "Must the Secretary of State fix an assessed income period for me?", "What am I paid ... once my income element changes?".
The facts about the other party that the text makes the claim depend on are plain inputs: what the Secretary of State decided, determined or considers (`the Secretary of State considers my pension particulars are not likely to be typical`), what the regulations prescribe, whether a decision was made and when.
Where the Act gives the Secretary of State a power over the person, the paired question is asked: "Can the savings credit be refused me as a member of a mixed-age couple?" (s 3ZA(1)), "Can fresh determinations of my retirement provision be made during my period?" (s 8), "Am I excluded because of my partner?" (s 4), "Can I be asked for evidence about likely future changes?" (Sch 1 para 3(3A)), "On what day does my period stop being in force?" (s 9).
The Act puts no duty of its own on a claimant (finding 25): what he "must do or tell the authorities" is the claim itself (an input to "entitled") and the evidence the regulations may require.

## What is encoded, and what is not

**Encoded (layer 1, objectively, in ten modules):** the whole of sections 1 to 10, 12(1), 15 to 17, 18A and 22, with Schedule 1 paragraphs 3(3), 12 and 13 and Schedule 2 paragraphs 2, 4, 17, 26 and 30.
Entitlement (s 1), the guarantee credit (s 2), the savings credit (s 3), the mixed-age couple (s 3ZA), the exclusions and the minimum payable (s 4), aggregation (s 5), the assessed income period (ss 6 to 10), the definitions that carry a test (ss 15 to 17), the 12-month pilot limit (s 18A(1)), the dates and extent (s 22) and the schedule paragraphs that state a test.

**Not encoded, and why:** the coverage table gives a reason for each.
In short: powers to make regulations and their procedure (ss 3(6), 7(7), 12(2) to (4), 13, 15(3) to (7), 16(2), 17(2), 18A(2) to (11), 19), the financial and repeal provisions (ss 20, 21, Schedule 3), amendments of other Acts that insert a name into a list (Schedule 1 paras 2 to 11; Schedule 2 almost throughout), and the rules of other Acts the text mentions without stating (the Pensions Act 1995 rules for pensionable age; section 173 of the Contributions and Benefits Act; section 115 of the Immigration and Asylum Act 1999; the Administration Act's claim requirement; section 27 of the Social Security Act 1998).

**Amounts, rates, thresholds and periods are plain inputs.**
The Act states no figure for the standard minimum guarantee, the additional amounts, the savings credit threshold, the percentages for amounts A and B and the maximum savings credit, the minimum payable (s 4(3)), the rate at which capital is deemed to yield income (s 15(2)) or the amount for a part week (Sch 1 para 13).
The regulations that set them are not among the inputs, so each is a plain input with a comment, never invented in layer 1.
The tests supply round invented figures (standard minimum guarantee 300 for a couple and 200 alone, a threshold of 150, 50 per cent for amounts A and B, 60 per cent for the maximum savings credit, a minimum of 1) and say so at the top of each test file.

**Files** (all in this folder, all `spc-` prefixed):

| file | what it holds |
|---|---|
| `spc-nouns.l4` | the shared types: `Person`, `Income`, `Household`, `Case`, `Prescribed`, `Answer`; the `YMD` shim |
| `spc-dates.l4` | s 22, the title-page date (NOTHING), the dates and ages the Act states, attaining an age (s 17(3)) |
| `spc-part-interpretation.l4` | ss 15 to 17 definitions that carry a test |
| `spc-part-misc.l4` | ss 11 to 14 (s 12(1) only encoded) |
| `spc-part-final.l4` | ss 18 to 21 and 18A |
| `spc-part-entitlement.l4` | ss 1 to 5, 3ZA and s 17(1) "entitled"; the four answer rules the seat calls |
| `spc-part-retirement.l4` | ss 6 to 10 |
| `spc-sch1.l4`, `spc-sch2.l4`, `spc-sch3.l4` | Schedules 1 to 3 |
| `spc-tests-layer1.l4` | layer-1 tests |
| `spc-seat.l4`, `spc-cases-seat.l4` | layer 2 |
| `check.sh`, `srcrefs.py` | the self-check and the citation checker (copies from the skill; `expected_failed` is empty) |
| `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md` | this record |

## Jural relations

One row per provision that creates a relation (holder of the claim, privilege, power or immunity; bearer of the correlative duty, no-right, liability or disability); a provision that creates none (a definition, a counting rule) is listed as `none`.
Each relation is stated once in layer 1 and neutrally; the seat asks both faces from the person's side.

| provision | relation | holder | bearer | L4 rule |
|---|---|---|---|---|
| s 1(2), (3), (4) | claim to state pension credit (the benefit "shall be payable", s 1(1)) | the claimant | the Secretary of State, who pays it (the Act names no payer in s 1; s 6 and s 20 name him and the Exchequer) | `s 1(4) -- entitled to state pension credit under sections 1 to 5`, `s 1(3)(a)`, `s 1(3)(b)`, `The Act's answer on whether the conditions for entitlement are met` |
| s 1(5) | power to prescribe who is in Great Britain and a continuing entitlement during absence; the claimant's liability to it | the Secretary of State (by regulations) | the claimant | none (its outcomes are inputs to `s 1(2)(a)`) |
| s 2(1), (2) | claim to the guarantee credit, the difference between the appropriate minimum guarantee and income | the claimant | the Secretary of State | `s 2(2) -- the guarantee credit to which the claimant is entitled` |
| s 2(3) to (9) | none: they define the amount (the appropriate minimum guarantee and its parts) | none | none | `s 2(3)`, `s 2(5)`, `s 2(3)(a)`, `s 2(3)(b)`, `s 2(8)` (counting rules) |
| s 3(1) to (3), (7) | claim to the savings credit, the amount by which amount A exceeds amount B | the claimant | the Secretary of State | `s 3(3) -- the savings credit to which the claimant is entitled` |
| s 3(4), (5), (7) | none: they define amounts A and B and the maximum savings credit | none | none | `s 3(4) -- amount A`, `s 3(4) -- amount B`, `s 3(5)`, `s 3(7)` |
| s 3ZA(1) | power: regulations may deny a savings credit to a member of a mixed-age couple; the claimant's liability to it | the Secretary of State (by regulations) | the member of a mixed-age couple | `s 3ZA(1) -- not entitled to a savings credit as a member of a mixed-age couple` |
| s 3ZA(3) | none: defines a mixed-age couple | none | none | `s 3ZA(3) -- the claimant is a member of a mixed-age couple` |
| s 4(1), (1A) | no-right of the claimant to the benefit (and the Secretary of State's privilege not to pay) where the other member of the couple is entitled or has not attained the qualifying age | the Secretary of State (privilege) | the claimant (no-right) | `s 4(1) -- excluded because the other member of the couple is entitled`, `s 4(1A) -- excluded because the other member of the couple has not attained the qualifying age` |
| s 4(2) | disability: section 115 of the Immigration and Asylum Act 1999 as amended bars a person within it from state pension credit | the Secretary of State (immunity from the claim) | the person within section 115 | `s 4(2) -- excluded under section 115 of the Immigration and Asylum Act 1999` (a fact, F-26) |
| s 4(3) | no-right to a sum below the prescribed amount, except in prescribed circumstances | the Secretary of State (privilege) | the claimant (no-right) | `s 4(3) -- state pension credit is payable`, `s 4(3) -- the amount of state pension credit to which the claimant is entitled` |
| s 5 | none: a counting rule (the other member's income and capital count as the claimant's) | none | none | `s 5 -- the income treated as the claimant's` and its two siblings |
| s 6(1) | duty to specify an assessed income period on the relevant decision, and the claimant's correlative claim that he do (arguable: the Act does not say whom the duty is owed to) | the claimant (claim) | the Secretary of State (duty) | `s 6(1) -- what section 6 requires of the Secretary of State on the decision` |
| s 6(2) | disability of the Secretary of State to specify a period where one is already in force or other circumstances are prescribed; the claimant's immunity from a second period | the claimant (immunity) | the Secretary of State (disability) | `s 6(2) -- the Secretary of State is prevented from specifying a period` |
| s 6(3), (4), (5); s 7(1) to (6); s 9(1), (3) to (6) | none: they define the cases, the amount of an element, retirement provision, the length and the end of a period | none | none | `s 6(3)`, `s 6(4)`, `s 7(3) to (5)`, `s 7(6)`, `s 9(1)`, `s 9(4), (5)`, `s 9(6)`, `s 9` |
| s 8(1), (2) | power of the Secretary of State to make fresh determinations of the claimant's retirement provision during the period; the claimant's liability to it | the Secretary of State (power) | the claimant (liability) | `s 8(1), (2) -- fresh determinations may be made` |
| s 8(3) | none: a counting rule (which determination governs from the new decision's day) | none | none | `s 8(3) -- which determination governs on` |
| s 9(2) | privilege of the Secretary of State not to specify a period where he considers the particulars not typical; the claimant's no-right to one | the Secretary of State (privilege) | the claimant (no-right) | `s 6(1)` (the `need not` outcome), `s 9(2)(b) -- the period specified complies` |
| s 10(2), (3) | claim to the changed amount from the commencing date without a further decision; and the Secretary of State's disability to withhold it for want of one | the claimant (claim; immunity from a new decision) | the Secretary of State (duty; disability) | `s 10(2), (3) -- the amount of state pension credit payable on`, `s 10(2) -- whether a further decision ... is needed` |
| s 12(1) | power of the Secretary of State to displace the Act by regulations in a polygamous case; the household's liability to it | the Secretary of State (power) | the persons in the polygamous household | `s 12(1) -- section 12 applies to the case` |
| s 15(2) | power to deem capital to yield income at a prescribed rate; the claimant's liability to it | the Secretary of State (power) | the claimant | `s 15(2) -- income deemed to be yielded by capital` |
| s 15(1), s 16(1), s 17(1) definitions, s 17(3) | none: definitions (income, retirement pension income, couple, the war and foreign pensions, working tax credit, PPF periodic payments, attaining an age) | none | none | `s 15(1)`, `s 16(1)`, `s 17(1)` (each), `the day on which the age is attained` |
| s 17(1) "entitled" | none: states what entitlement is construed in accordance with (this Act, the claim requirement of the Administration Act, restrictions of the Social Security Act 1998) | none | none | `s 17(1) -- entitled to state pension credit` |
| s 18A | power to make a pilot scheme for up to 12 months that displaces provisions of the Act; the liability of persons to whom it applies | the Secretary of State (power) | the persons within the scheme | `s 18A(1)`, `s 18A(5)` |
| s 22 | none: commencement and extent | none | none | `s 22(2)`, `s 22(3)`, `s 22(6)` |
| Sch 1 para 3(3A) | power: regulations may require information or evidence of likely future changes in circumstances (to decide on an assessed income period); the claimant's liability to be asked | the Secretary of State (power, by regulations) | the claimant (liability) | `Sch 1 para 3(3A) -- the information or evidence is within what the regulations may require for state pension credit` |
| Sch 1 para 12 | power of the claimant to appeal against the four decisions about an assessed income period; the Secretary of State's liability to have the decision reviewed | the claimant (power) | the Secretary of State (liability) | `Sch 1 para 12 -- an appeal lies against` |
| Sch 1 para 13 | claim to a prescribed amount (possibly nil) for a period of less than a week | the person entitled | the Secretary of State | `Sch 1 para 13 -- the amount payable for a period of` |
| Sch 2 para 2 | no-right of a claimant of income support to it unless not at the qualifying age and (for a couple) the other member is not entitled to state pension credit; the Secretary of State's privilege to refuse | the Secretary of State (privilege) | the claimant of income support (no-right) | `Sch 2 para 2 -- the conditions inserted into section 124(1) of the Contributions and Benefits Act are met` |
| Sch 2 para 4 | none: the definition of the qualifying age (repeats s 1(6)) | none | none | `Sch 2 para 4 -- the day the person attains the qualifying age for state pension credit` (delegates to `s 1(6)`) |
| Sch 2 para 17 | claim to the changed amount from the commencing date when an alteration affects it, without a further decision | the recipient | the Secretary of State | `Sch 2 para 17 -- the amount of state pension credit payable on` |
| Sch 2 para 26 | claim to a payment under s 70(2) of the Transport Act 1982 for those in receipt of guarantee state pension credit or whose partner is (whether it is a power or a duty depends on s 70(2), which is not in the text) | the person within the class | the Secretary of State | `Sch 2 para 26 -- the Secretary of State makes the payment under section 70(2) of the Transport Act 1982 for` |
| Sch 2 para 30 | immunity from a charge under s 29(1) of the Children Act 1989 for a service under s 18(2) or (6) while in receipt of guarantee state pension credit, or a partner is | the person (immunity) | the local authority (disability) | `Sch 2 para 30 -- the person is not liable to pay a charge under section 29(1) of the Children Act 1989 for a service under section 18(2) or (6) when` |

## Coverage table

One row per section (or group of subsections), and per paragraph or group of paragraphs of each Schedule.

| provision | disposition | where, or why |
|---|---|---|
| Long title and enacting formula | not applicable | States no rule and applies to nobody: the long title says what the Act is for, and the enacting words say who enacted it. |
| s 1(1) | inert | Introduces the benefit ("shall be payable in accordance with the following provisions"); the conditions are in s 1(2) onwards, and the sentence itself adds no test. |
| s 1(2), (3), (4), (6) | encoded | spc-part-entitlement: `s 1(2)(a)`, `s 1(2)(b)`, `s 1(2)(c)`, `s 1(2)`, `s 1(3)(a)`, `s 1(3)(b)`, `s 1(4)`, `s 1(6)`. |
| s 1(5) | encoded | The two kinds of regulation it permits are inputs: `in Great Britain` and `temporarily absent ... entitlement continued by regulations` (forks F-02). The power itself is not encoded. |
| s 2(1) to (8) | encoded | spc-part-entitlement: the guarantee credit condition, the credit, the appropriate minimum guarantee, its parts and the allowance addition. |
| s 2(9) | inert | Says the powers to prescribe amounts include power to prescribe nil, except for the standard minimum guarantee; it grants a power to regulation-makers and tests nothing in a claimant's facts, so every prescribed amount is simply a number that may be 0. |
| s 3(1) to (5), (7), (8) | encoded | spc-part-entitlement: the two savings credit conditions, amounts A and B, the maximum savings credit, the savings credit. |
| s 3(6) | inert | A power to make regulations about which income is qualifying income; its outcome, the person's qualifying income, is an input to every rule that reads it. |
| s 3ZA(1), (3) | encoded | spc-part-entitlement: the mixed-age couple test and the refusal of a savings credit (fork F-03). |
| s 3ZA(2) | inert | An example of what regulations could say ("for example, the regulations could provide"); it is not itself a rule, and the regulations are an input. |
| s 4(1), (1A), (2), (3) | encoded | spc-part-entitlement: the two exclusions, the Immigration and Asylum Act exclusion (as a fact, F-26) and the minimum payable. |
| s 5 | encoded | spc-part-entitlement: income, qualifying income and capital of the other member counted as the claimant's. |
| s 6(1) to (5) | encoded | spc-part-retirement: the duty to specify an assessed income period, the prevention, the two cases and the relevant decision. |
| s 6(6), (7) | inert | Cross-references ("This section is subject to section 9"; "This section and sections 7 to 10 shall be construed as one"): instructions on how to read the sections, with no test of their own. |
| s 7(1) to (6) | encoded | spc-part-retirement: the amount of an element on a day, and what counts as retirement provision. |
| s 7(7) | inert | A power to make regulations treating income of one description as another, or from different sources as one source; not among the inputs. |
| s 7(8) | inert | A saving: subsections (3) to (5) do not prevent revision of the relevant decision under section 9 of the Social Security Act 1998. It permits something the encoding does not forbid, so nothing needs a rule. |
| s 7(9) | inert | A cross-reference ("This section is subject to section 8"); section 8 is encoded. |
| s 8 | encoded | spc-part-retirement: when fresh determinations may be made, and which determination governs. |
| s 9(1), (2), (4), (5), (6) | encoded | spc-part-retirement: the length of the period, the compliance of a shorter period, the ending events and the 80-or-over rule. |
| s 9(3) | inert | An assumption the Secretary of State makes in forming the view of s 9(2) (that the section 7(4) variations of a five-year period would apply). The view is a judgment handed to him, so it is an input ("considers ... not likely to be typical"). |
| s 10 | encoded | spc-part-retirement: the amount payable on a day, and whether a further decision is needed (fork F-23). |
| s 11 | inert | A signpost: "Schedule 1 shall have effect" and a summary of its three Parts. The rules are in Schedule 1. |
| s 12(1) | encoded | spc-part-misc: the three conditions that put a case within section 12; the encoding then answers `Not covered by this encoding` (fork F-15). |
| s 12(2) to (4) | inert | Powers to make regulations for polygamous marriages (different amounts, aggregation, displacing provisions of the Act). No such regulations are among the inputs, so nothing can be decided for such a case. |
| s 13 | inert | A power to make transitional provision and savings, and a description of what it may include. The appointed day it refers to is not among the inputs (fork F-20). |
| s 14 | inert | A signpost to Schedule 2, which is dealt with paragraph by paragraph below. |
| s 15(1), (2) | encoded | spc-part-interpretation: income (the ten descriptions, summed), and income deemed to be yielded by capital at a prescribed rate. |
| s 15(3) to (7) | inert | (3) to (6) are powers to prescribe how income and capital are calculated or estimated, the rules for income over a period, averaging, and circumstances in which income or capital is deemed, disregarded or re-characterised; (7) says (2) to (6) have effect for the purposes of the Act. The outcomes enter as inputs (the income figures the person states). |
| s 16(1) | encoded | spc-part-interpretation: the descriptions of retirement pension income, with the court-order proviso of paragraph (l). |
| s 16(2), (3) | inert | (2) a power to amend the list; (3) points at definitions in other Acts that are not among the inputs. |
| s 17(1) | encoded | spc-part-interpretation: couple, foreign social security benefit, foreign war disablement pension, foreign war widow's or widower's pension, war disablement pension, war widow's or widower's pension, working tax credit, PPF periodic payments; spc-part-entitlement: "entitled" (fork F-22). The other definitions point at a section of this Act ("appropriate minimum guarantee", "capital", "income", "retirement provision" and the like, each encoded where the section is), at another Act, or say what "prescribed" and "regulations" mean; "pensionable age" is borrowed from the Pensions Act 1995 and asked as a fact (fork F-27). |
| s 17(1A) | repealed or blank in this text | Rendered in the text as a row of dots (`(1A) . . . .`), where a subsection has been repealed or omitted. |
| s 17(2) | inert | A power to make regulations about when persons are, or are not, treated as members of the same household and as severely disabled; the regulations are not among the inputs, so each of those two facts is an input. |
| s 17(3) | encoded | spc-dates: attaining an age (fork F-04). Section 172 of the Contributions and Benefits Act, which it also applies, concerns territorial waters and is not among the inputs. |
| s 18 | inert | Amends section 47(1) of the Pension Schemes Act 1993 (equal treatment of widows and widowers); it is an amendment to another Act and creates nothing between a claimant and anyone. |
| s 18A(1), (5) | encoded | spc-part-final: the 12-month limit on a pilot scheme (fork F-14) and the displacement of the Act's provisions (fork F-15). |
| s 18A(2) to (4), (6) to (11) | inert | The purposes of a pilot scheme, the definition of one, the meaning of "relevant provision", and powers to make regulations (tax and benefit disregards, areas and classes, consequential provision, replacement, Treasury consent). They address the Secretary of State; a person to whom a scheme applies is asked as one yes-or-no fact. |
| s 19 | inert | Parliamentary procedure for regulations and orders (affirmative and negative resolution); it concerns the regulation-making process and nothing about a claimant. |
| s 20 | inert | Financial provisions: payment of benefit and costs out of money provided by Parliament, and payment into the Consolidated Fund. A budgetary provision between Parliament and the Exchequer. |
| s 21 | inert | Gives effect to Schedule 3 (the repeals); see Schedule 3 below. |
| s 22(2), (3), (6) | encoded | spc-dates: in force on the passing for ss 19, 20 and 22; the rest on a day appointed by order (an input); extent England and Wales and Scotland (fork F-20). |
| s 22(1), (4), (5) | inert | (1) the short title; (4) transitional provision in a commencement order; (5) extent follows the enactment amended. None decides anything for a claimant. |
| Sch 1 paras 1, 2, 3(1), 3(2) | inert | Para 1 introduces the Part; para 2 adds state pension credit to the benefits whose entitlement depends on a claim (carried by the input `a claim has been made` in the s 17(1) rule); para 3(1) and (2) add it to the list of benefits in s 5 of the Administration Act. Each inserts a name into a list in another Act. |
| Sch 1 para 3(3) | encoded | spc-sch1: `Sch 1 para 3(3A)`, the evidence about future changes that the regulations may require. |
| Sch 1 paras 4 to 11 | inert | Each adds state pension credit or this Act to a list in the Social Security Act 1998 (use of computers, decisions, regulations, suspension, restrictions on entitlement, correction of errors, decisions with no appeal). They state no test of their own; the facts they bear on (a decision under s 8, 9 or 10; a s 27 restriction) are asked where the encoded rules need them. |
| Sch 1 para 12 | encoded | spc-sch1: `Sch 1 para 12`, the four decisions against which an appeal lies. |
| Sch 1 para 13 | encoded | spc-sch1: `Sch 1 para 13`, the amount payable for less than a week (fork F-17). |
| Sch 2 para 1 | inert | Introduces the Part (amendments of the Contributions and Benefits Act). |
| Sch 2 para 2 | encoded | spc-sch2: the two conditions inserted into s 124(1) (income support): not at the qualifying age, and, for a couple, the other member not entitled (fork F-18). |
| Sch 2 para 3 | inert | Inserts section 136A: powers to make regulations about housing benefit and council tax benefit for a person at the qualifying age. Nothing is decided without those regulations. |
| Sch 2 para 4 | encoded | spc-sch2: the definition of the qualifying age, which delegates to s 1(6) so that the relation is stated once. |
| Sch 2 paras 5 to 7 | inert | Amend the Christmas bonus provisions (ss 148 to 150 of the Contributions and Benefits Act), which are not in this text; the conditions of the bonus cannot be stated from it. |
| Sch 2 para 8 | inert | Introduces the Part (amendments of the Administration Act). |
| Sch 2 para 9 | repealed or blank in this text | The text shows the heading "Payment out of benefit of sums in respect of mortgage interest etc" and then a row of dots where the body should be. |
| Sch 2 paras 10 to 16 | inert | Each adds state pension credit or this Act to a list in the Administration Act (overpayments, recovery, enforcement, registers of births and deaths, notification of death, personal representatives' information, up-rating). None states a test. |
| Sch 2 para 17 (s 159B(1) to (3)) | encoded | spc-sch2: `Sch 2 para 17`, the effect of an alteration on the amount payable (fork F-23). |
| Sch 2 para 17 (s 159B(4) to (6)) | inert | Lets an award made after a statement in the House of Commons take either of two forms ("may"), which is the Secretary of State's choice, and repeats definitions already held. It creates no test on a claimant's facts. |
| Sch 2 paras 18 to 24 | inert | Each adds this Act or state pension credit to a list in the Contributions and Benefits Act or the Administration Act (the National Insurance Fund, social fund adjustments, the Advisory Committee, reciprocal agreements, travelling expenses, inalienability, definitions). The sections amended are not in this text. |
| Sch 2 para 25 | repealed or blank in this text | The text shows the heading "Magistrates’ Courts Act 1980" and then a row of dots where the body should be. |
| Sch 2 para 26 | encoded | spc-sch2: `Sch 2 para 26`, the Transport Act 1982 payment for those in receipt of guarantee state pension credit (fork F-28). |
| Sch 2 paras 27, 29 | inert | Each applies a deduction rule for unpaid community charge to state pension credit as it applies to income support; the deduction rules sit in the amended paragraphs, which are not in this text. |
| Sch 2 para 28 | repealed or blank in this text | The text shows the paragraph number alone and then a row of dots. |
| Sch 2 para 30 | encoded | spc-sch2: `Sch 2 para 30`, freedom from the Children Act 1989 charge (fork F-28). |
| Sch 2 paras 31 to 35 | inert | Add state pension credit to the deductions from benefit for fines and council tax (Criminal Justice Act 1991, Local Government Finance Act 1992). The deductions and their limits are in the amended provisions, not here. |
| Sch 2 paras 36 to 38 | repealed or blank in this text | Rendered in the text as {repealed: ...} (Jobseekers Act 1995 amendments, since repealed): treated as repealed. |
| Sch 2 para 39 | inert | Amends the Pensions Act 1995 so that its pensionable age rules apply for this Act; the rules themselves are not among the inputs, so the days at which pensionable age is attained are facts (fork F-27). |
| Sch 2 paras 40, 41, 43 | inert | Add state pension credit to s 34(3) of the Social Security Act 1998 (priority of claims) and s 94 of the Local Government Act 2000 (disclosure). List insertions. |
| Sch 2 para 42 | repealed or blank in this text | The text shows the heading "Immigration and Asylum Act 1999" and then a row of dots where the body should be. (Section 4(2) of this Act separately amends section 115 of that Act; see fork F-26.) |
| Sch 2 paras 44 to 49 | inert | Amend the Social Security Fraud Act 2001: powers to make regulations on reduced payment of the benefit during a loss-of-benefit period, and list insertions. The regulations are not among the inputs. Sub-paragraph 45(3) is rendered as a row of dots (blank in this text). |
| Sch 3 | inert | A table of repeals in three other Acts (single connecting words and one subsection). A repeal changes the text of another Act and creates no relation between a claimant and anyone. |

**Counts:** 71 rows: encoded 27, inert 37, repealed or blank in this text 6, not applicable 1.

## Fork register

Every place the text allows more than one reading, or defers to something that is not among the inputs: the readings seen, the one taken, and the text that licenses it.

| id | provision | readings seen | reading taken | licensing text |
|---|---|---|---|---|
| F-01 | s 1(6): the qualifying age | (a) a man's qualifying age is his own pensionable age; (b) it is the age that is pensionable age for a woman born the same day | (b). Both days are plain inputs (`day pensionable age is attained`, `day a woman born on the same day attains pensionable age`) because the Pensions Act 1995 rules are not among the inputs. | s 1(6)(a), (b): "in the case of a man, the age which is pensionable age in the case of a woman born on the same day as the man" |
| F-02 | s 1(2)(a) with s 1(5)(b): temporary absence | (a) continued entitlement during a temporary absence is a separate rule after entitlement is found; (b) it is another way of satisfying "he is in Great Britain" | (b): `in Great Britain` OR `temporarily absent ... entitlement continued by regulations`. | s 1(5)(a), (b): regulations as "to circumstances in which a person is to be treated as being or not being in Great Britain" or "continuing a person's entitlement ... during periods of temporary absence" |
| F-03 | s 3ZA(1) and the route to entitlement | (a) a person refused a savings credit under s 3ZA(1) loses only the savings credit amount; (b) she also cannot satisfy s 1(2)(c)(ii) (the conditions in s 3(1) and (2)), so if the savings route was her only way in she is not entitled to state pension credit at all | (b). Case H2 (a mixed-age couple, no guarantee credit) is "not entitled", Asserted. | s 3ZA(1) "is not entitled to a savings credit"; s 1(2)(c)(ii); s 1(3)(b) |
| F-04 | s 17(3): attaining an age | (a) an age is attained on the anniversary of birth; (b) on the day before it; for a birth on 29 February, a non-leap year's anniversary is (c) 28 February or (d) 1 March | (a) and (d): the anniversary, and the lenient `Date` carries a 29 February birthday to 1 March in a year with none. Section 173 of the Contributions and Benefits Act, which s 17(3) applies, is not among the inputs, so this is a stated convention. | s 17(3)(b) "section 173 (meaning of attaining an age etc) ... shall apply"; the section is absent |
| F-05 | s 2(6) and s 3(7)(a) | (a) the substituted amount replaces the standard minimum guarantee wherever the Act uses it; (b) only in s 2(3)(a), the reference the regulation text names | (b): the maximum savings credit still reads the standard minimum guarantee itself. Case G1 Asserted. | s 2(6) "the substitution for the reference in paragraph (a) [of subsection (3)] to the standard minimum guarantee"; s 3(7)(a) "the standard minimum guarantee" |
| F-06 | s 2(8): allowance for both members of a couple | (a) one amount for the circumstance however many members have the allowance; (b) one amount for each member | (a). Cases F2 and F3 Asserted. | s 2(8) "there shall be included ... an amount in respect of that circumstance" (singular) |
| F-07 | s 4(1): the other member's entitlement | (a) computed from the other member's own facts; (b) a plain fact stated by the person | (b): computing it would be circular (each member's entitlement depends on the other's). | s 4(1) "the other member of which is entitled to state pension credit" |
| F-08 | s 4(3): the amount payable | (a) the guarantee credit and the savings credit are compared with the minimum separately; (b) their sum is | (b): "the amount payable by way of state pension credit" is the total of the credits. Cases J1 to J3 Asserted. | s 4(3); s 1(3) "(or to both ...)" |
| F-09 | s 5: qualifying income of the other member | (a) only income is aggregated; (b) qualifying income is aggregated too | (b): qualifying income is income of a description (s 3(6)), so the other member's counts as the claimant's. | s 5 "the income and capital of the other member ... shall ... be treated ... as income and capital of the claimant"; s 3(6) |
| F-10 | s 3(5): when the higher amount applies | (a) whenever a prescribed higher amount exists; (b) only where the s 2(6) substitution is in play | (b). Case G3 (a higher amount, no substitution) Asserted. | s 3(5) "Where, by virtue of regulations under section 2(6), the claimant's appropriate minimum guarantee does not include the standard minimum guarantee" |
| F-11 | s 9(6): the day a period "is brought to an end" | (a) its last day; (b) the first day after it | (a): a period of 5 years beginning on 7 April 2008 expires at the end of 6 April 2013 (inside the window of 6 April 2009 to before 6 April 2014). | s 9(6)(a) "brought to an end, on or after 6 April 2009 but before 6 April 2014, by the expiry of a period of 5 years" |
| F-12 | s 7(6)(a): Northern Ireland counterparts | (a) a Northern Ireland pension counterpart to the Pensions Act 2014 or Contributions and Benefits Act benefit is also excluded; (b) only the Great Britain benefits named are | (b), the literal reading: the exclusion names "Part 1 of the Pensions Act 2014 or the Contributions and Benefits Act". Asserted. | s 7(6)(a) |
| F-13 | s 9(4): the time an event ends a period; events on the start day | (a) the period ends at the event, so the event's day is the first day not in force; (b) the event's day is the last day in force. And: a 65th birthday on or before the day the period begins is (c) an ending event, (d) not one | (a) and (d). A period under s 6 begins on or after the 65th birthday (s 6(3)(c)), so under (c) a claimant who is not in a couple would have every such period ended on its first day. | s 9(4) "end at any time at which ... the claimant attains the age of 65" |
| F-14 | s 18A(1): "not exceeding 12 months" | (a) a scheme starting on a day may last until the day before the same calendar day next year; (b) until that day | (a). Asserted at the edges, including a start on 29 February. | s 18A(1) |
| F-15 | ss 12 and 18A: regulations that may displace the Act | (a) ignore the powers (no regulations are in the inputs); (b) answer as if the Act's rules applied; (c) answer "not covered" whenever the case is within s 12(1) or a pilot scheme applies | (c). Asserted. | s 12(2), (3) "prescribed provisions shall apply instead of prescribed provisions of this Act"; s 18A(5)(a) |
| F-16 | percentages | (a) 60 means 60 per cent; (b) 0.6 means 60 per cent | (a): the person is asked for the figure as the regulations print it. | s 3(4) "a prescribed percentage"; s 3(7) |
| F-17 | Sch 1 para 13: how long is a week | (a) 7 days; (b) a benefit week as the regulations define it | (a): the Act does not say. Asserted at 6 and 7 days. | Sch 1 para 13 "a period of less than a week" |
| F-18 | Sch 2: inserted text | (a) the inserted words are what the paragraph says today; (b) the amended section may have been amended since | (a), stated: each encoded rule states the provision as inserted. The amended Acts are not among the inputs, so nothing is said about their present wording. | Sch 2 paras 2, 4, 17, 26, 30 |
| F-19 | date of Royal Assent | (a) the date from memory; (b) NOTHING | (b): the deposited text carries no assent date (no square-bracketed date under the title). Asserted as NOTHING. | title page, lines 1 to 3; `../../registers/source-bundle/ukpga-2002-16.txt` |
| F-20 | s 22(2), (3): commencement | (a) invent a date; (b) take the appointed day as an input | (b). Sections 19, 20 and 22 are in force on the passing; the rest on the day appointed by order. Asserted on both sides of an invented day. | s 22(2), (3) |
| F-21 | s 3(4): amount A when qualifying income does not exceed the threshold | (a) the excess is negative; (b) the excess is taken as 0 | (b): immaterial, because s 3(2)(a) then fails and there is no savings credit. | s 3(2)(a); s 3(4) "the amount by which the claimant's qualifying income exceeds the savings credit threshold" |
| F-22 | s 17(1): "entitled" and a claim | (a) apply the claim requirement and any s 27 restriction inside ss 2 and 3; (b) apply them once at the top, so the Act's conditions and "entitled" are two answers | (b): `The Act's answer on whether the conditions for entitlement are met` and `... whether the claimant is entitled`. A person who has not claimed meets the conditions and is not entitled. Asserted. | s 17(1) "entitled" (a), (b), (c) |
| F-23 | s 10(2), (3) and Sch 2 para 17: before the commencing date and outside the section | (a) the amount before applies until the commencing date and, outside the section, throughout; (b) the section is silent before the commencing date and outside it, so NOTHING | A mix: outside the section, NOTHING (the section states nothing about what is paid then); before the commencing date, the existing award's amount (an input), because an award in force continues until it is changed. Asserted. This was a defect in the first version of both rules (they returned the old amount whenever the section did not apply), found while writing the seat layer and corrected in layer 1 before its tests were rerun. | s 10(2) "as from the commencing date"; Sch 2 para 17 (s 159B(2)) "as from the commencing date" |
| F-24 | s 2(1)(a): "no income" | (a) a separate test from (b); (b) income of 0, which (b) covers anyway | (b): "no income" is income of 0; condition (b) ("does not exceed") then holds for any non-negative minimum guarantee, so (a) adds nothing, and the credit is the whole minimum guarantee (s 2(2)(a) agrees with s 2(2)(b) at 0). | s 2(1)(a), (b); s 2(2)(a), (b) |
| F-25 | s 6(1) with s 6(2) and s 9(2)(a): which outcome wins | (a) "need not specify" (the Secretary of State's view of s 9(2)) wins over "prevented"; (b) "prevented" wins; and (c) the section's own scope (the cases, and before 6 April 2016) comes first | Scope first, then prevented, then need-not, then must. A person who cannot be given a period is not told he "need not" be given one. | s 6(1) "unless prevented by subsection (2)"; s 9(2)(a) "he need not specify a period under section 6(1)" |
| F-26 | s 4(2): the amendment of the Immigration and Asylum Act 1999 | (a) encode the text of s 115 (not among the inputs); (b) take "excluded under s 115 as amended by s 4(2)" as one fact the person states | (b). | s 4(2) (inserts "or to state pension credit under the State Pension Credit Act 2002" into s 115(1)) |
| F-27 | "pensionable age" (s 17(1), Sch 2 para 39) | (a) compute it from the person's date of birth under the Pensions Act 1995; (b) ask the day it is attained | (b): the rules are not among the inputs; the two days (the person's own, and a woman born on the same day's) are plain inputs. | s 17(1) "pensionable age" ... paragraph 1 of Schedule 4 to the Pensions Act 1995 |
| F-28 | Sch 2 paras 26 and 30: "in receipt of" | (a) "in receipt" is the same as entitled; (b) it means the benefit is being paid | (b): an entitlement that is not payable (for example below the s 4(3) minimum) is not receipt; each member's receipt is a fact. | Sch 2 para 26 (s 70(2)(bb)) and para 30 (s 29(3B)) "in receipt of guarantee state pension credit" |
| F-29 | s 17(1) "couple" limb (b) | (a) a pair who are married but live in different households and live together as a couple fall in limb (b); (b) limb (b) is for pairs who are NOT married or civil partners | (b), the words of limb (b). Such a pair is not a couple. Asserted. | s 17(1) "couple" (a), (b) |

**Where I looked for ambiguity**, so that "none found" is not the claim:

- *The date at which each condition is tested.* The day asked about is a parameter of every date-dependent rule; the age tests (s 1(2)(b), s 3(1)(a), s 6(3)(c), s 9(1)) are at the day the decision takes effect or the day asked about; s 3(1)(a)'s pensionable-age limb and s 3ZA(3) are fixed at 6 April 2016 (forks F-04, F-13; findings 3, 4).
- *Cumulative or alternative.* s 1(2) is (a) AND (b) AND ((c)(i) OR (c)(ii)); s 3(1) is (a) OR (b); s 3(2) is (a) AND (b); s 6(3) is (a) AND (b) AND (c) AND (d), with (c) alternative on the claimant's and the partner's 65th birthday ("if earlier"); s 17(1) "couple" is (a) OR (b). Each limb is asserted true and false at least once, except s 6(3)(a) and (b), which are asserted only together.
- *Overlap.* s 4(1) with s 4(1A) (both exclusions, each alone suffices); s 2(1)(a) with (b) (F-24); s 6(1) with s 6(2) and s 9(2) (F-25); s 10 with Sch 2 para 17 (finding 24); s 1(6) with Sch 2 para 4.
- *Deferral.* Every "prescribed" and every "regulations may" (the figures, qualifying income, the household and severe-disability tests, the exceptions to aggregation and to the ending of a period, further ending times, the minimum payable and its exceptions, the 3ZA and 3(8) descriptions), every other Act (the Administration Act s 1, the Social Security Act 1998 ss 8 to 10 and 27, the Pensions Act 1995, the Immigration and Asylum Act s 115, section 173 of the Contributions and Benefits Act, the Transport Act 1982 s 70, the Children Act 1989 ss 18 and 29), and the Secretary of State's own view (s 9(2)).

## What the text turns out to say

Numbered findings. Each ends "Asserted." where a case in `spc-tests-layer1.l4` or `spc-cases-seat.l4` asserts it, and says what is not asserted otherwise.

1. Income equal to the appropriate minimum guarantee meets the guarantee credit condition ("does not exceed") and the credit is nil; the claimant is, on the Act's conditions, entitled. If a minimum of more than 0 is prescribed, nothing is payable (finding 5). Asserted.
2. The savings credit needs qualifying income that EXCEEDS the threshold, and amount A that EXCEEDS amount B. Equality in either gives no savings credit. With the invented figures, income 260 gives A = B = 30 and no entitlement, while income 259 gives a savings credit of 0.5. Asserted.
3. Section 3(1)(a) reads the claimant's OWN pensionable age (before 6 April 2016) and whether he has attained 65. For a man this differs from his qualifying age (a woman's pensionable age for his birthday), which section 1(2)(b) uses. With the invented days of the tests, a man born on 10 May 1950 reaches the qualifying age on 10 May 2010 and meets s 3(1)(a) only on 10 May 2015; a man whose own pensionable age falls on 6 April 2016 has no savings credit route (6 April 2016 is not before 6 April 2016). Asserted.
4. Section 3ZA(3) tests whether each member had attained pensionable age before 6 April 2016, not whether they have on the day asked about. A couple is mixed-age or not for ever, whatever their ages become. Asserted.
5. Section 4(3): an entitled claimant can be paid nothing. If the amount due is below the prescribed minimum and no prescribed circumstance applies, the amount payable is nil though the person is entitled. Asserted.
6. "Entitled" and "meets the Act's conditions" are different answers. Section 17(1) adds a claim (Administration Act s 1) and the absence of a s 27 restriction. A person who has not claimed meets the conditions, would be entitled to an amount if she claimed, and is not entitled now. Asserted.
7. Section 9(1): a decision taking effect on the claimant's 75th birthday gets an indefinite period; the day before, five years. Asserted.
8. Section 9(4)(c) can never end a period of a claimant who is not a member of a couple on grounds of her own 65th birthday: a period under section 6 starts on or after it (s 6(3)(c)), and a birthday on the start day is not "a time at which" she attains 65 during the period (fork F-13). For a couple, the other member's 65th birthday can end it (s 9(4)(d)). Asserted for a period beginning on the 65th birthday and for the other member's birthday.
9. Section 9(6) never carries on a five-year period begun under s 9(1)(a): a claimant under 75 on the first day is under 80 on the day the five years expire. A claimant born 7 April 1934 with a period starting 7 April 2008 expires on 6 April 2013, inside the s 9(6) window, aged 78 then; the period ends. Only a period longer than five years (which s 9(1) does not give, but s 13(2)(b) transitional provision may) could meet s 9(6). Asserted for the 2008 period; the s 13(2)(b) remark is not asserted (no such regulations are among the inputs).
10. Section 7(4): a prescribed variation of an assessed amount can decrease it only for income from capital. A decrease of -7 takes an income-from-capital element from 100 to 93 and leaves any other element at 100. Asserted.
11. Section 8(1), (2): fresh determinations cannot be made when the new decision leaves the amount unchanged, and a reduction counts only if it is smaller than it would have been apart from them (equal is not smaller). Asserted.
12. Section 10(2): no further decision is needed for the changed amount to be paid, but only when all three of section 10(1)'s conditions hold. Otherwise the Act is silent, and the encoding says so (`Not covered by this encoding`, not `The Act says yes`). Asserted.
13. Section 7(6)(a) excludes the Great Britain benefits named, but on the literal wording not their Northern Ireland counterparts; section 16(1) lists the Northern Ireland counterpart of the state pension inside retirement pension income. Asserted.
14. Section 2(8): a couple both receiving the section 70 allowance (or carer support payment) get one additional amount, not two. Asserted.
15. Section 3(7)(a): the maximum savings credit reads the standard minimum guarantee, not the amount a section 2(6) regulation substitutes. A claimant with a substituted guarantee of 250 and a standard guarantee of 200 has a maximum savings credit of 60% of (200 - 150) = 30. Asserted.
16. Section 3(5): a prescribed higher amount for amount B exists only where the s 2(6) substitution is in play. Where a higher amount is prescribed but there is no substitution, amount B reads the appropriate minimum guarantee. Asserted.
17. "Couple" limb (a) needs marriage or civil partnership AND the same household. Limb (b) is for pairs who are NOT married or civil partners. A married pair in different households who live together fall in neither. Asserted.
18. The deposited text gives no date of Royal Assent (nothing in square brackets under the title). The encoding carries it as NOTHING and the date is not supplied from memory. Asserted.
19. Schedule 2 paragraphs 26 and 30 turn on being IN RECEIPT of guarantee state pension credit, not on being entitled to it, so a person entitled to a nil or unpayable guarantee credit is not covered. Asserted as truth tables on the two inputs; the nil-credit remark is not asserted.
20. Schedule 1 paragraph 12 lists four decisions against which an appeal lies; for any other decision the paragraph says nothing, and the encoding answers `Not covered by this encoding`. Asserted.
21. Schedule 1 paragraph 13 applies to "a period of less than a week"; the Act does not define a week (fork F-17). 6 days is covered, 7 is not. Asserted.
22. Section 12(1) and section 18A(5) take a case outside what the Act decides by itself. The encoding says `Not covered by this encoding` (or no number) for it, never yes or no, on all four answers. Two of the three section 12(1) conditions do not suffice. Asserted.
23. Section 4(1) and (1A) both depend on the other member of the couple, and section 4(1) on that member's ENTITLEMENT, which depends on the same section for the claimant. If each member claims, each could be excluded by the other; the Act does not say how that resolves, and the encoding takes the other member's entitlement as a stated fact (F-07) instead of computing it. Not asserted (argued from the text; the circularity is why the fact is an input).
24. Two overlapping provisions repeat each other: section 10 (retirement provision) and Schedule 2 paragraph 17 (section 159B of the Administration Act); and Schedule 2 paragraph 4 repeats section 1(6). Each repeat is encoded once where the Act states the relation (s 1(6)) or as a separate rule with a different trigger (section 159B has four kinds of alteration), and paragraph 4 delegates to s 1(6). Asserted for paragraph 4 (same day as s 1(6) for a woman and a man) and for paragraph 17.
25. The Act puts no duty of its own on a claimant. What a claimant is exposed to is the SoS's powers: regulations denying a savings credit (s 3ZA(1)), fresh determinations during a period (s 8), the ending of a period (s 9(4), (5)), and the requirement of evidence (Sch 1 para 3(3A)). The seat layer asks the paired "what can be done to me" question for each. Asserted for the four questions.

## Seat questions

Grouped under the `§§` headings of `spc-seat.l4`, which follow the Act's order.
Every question takes plain inputs (one per fact, with a `@desc` worded as the person would be asked) and builds the Act's records in its `WHERE`; it calls one layer-1 rule.

| heading | question | inputs |
|---|---|---|
| 1 Entitlement | Do I meet the conditions for state pension credit (ss 1(2), (4), 2 to 5)? | 62 |
| 1 Entitlement | Am I entitled to state pension credit (s 17(1), "entitled")? | 64 |
| 1 Entitlement | Have I reached the qualifying age for state pension credit (s 1(2)(b), (6))? | 5 |
| 2 Guarantee credit | How much guarantee credit am I entitled to, a week (s 2)? | 62 |
| 3 Savings credit | How much savings credit am I entitled to, a week (s 3)? | 62 |
| 3 Savings credit | Do I meet the age condition for the savings credit (s 3(1))? | 13 |
| 3ZA Power to limit savings credit for certain mixed-age couples | Am I a member of a mixed-age couple (s 3ZA(3))? | 12 |
| 3ZA Power to limit savings credit for certain mixed-age couples | Can the savings credit be refused me as a member of a mixed-age couple (s 3ZA(1))? | 13 |
| 4 Exclusions | Am I excluded from state pension credit because of my partner (s 4(1), (1A))? | 10 |
| 4 Exclusions | How much state pension credit would I be entitled to, a week, if I made a claim (ss 2 to 4)? | 64 |
| 4 Exclusions | How much state pension credit am I entitled to, a week (s 4(3), s 17(1))? | 66 |
| 5 Income and capital of claimant, spouse etc (with sections 15(1) and 17(1) "couple") | Am I a member of a couple under the Act (s 17(1))? | 4 |
| 5 Income and capital of claimant, spouse etc (with sections 15(1) and 17(1) "couple") | How much income counts as mine, a week, with my partner's (ss 5, 15(1))? | 25 |
| 6 Duty to specify assessed income period for pre-6 April 2016 awards | Must the Secretary of State fix an assessed income period for me (s 6)? | 21 |
| 7 Fixing of claimant's retirement provision for assessed income period | Is this kind of income part of my retirement provision (s 7(6))? | 3 |
| 7 Fixing of claimant's retirement provision for assessed income period | What amount of this income is counted for my assessed income period on a given day (s 7(3) to (5))? | 8 |
| 8 Fresh determinations increasing claimant's entitlement | Can fresh determinations of my retirement provision be made during my period (s 8(1), (2))? | 5 |
| 8 Fresh determinations increasing claimant's entitlement | Which determination of my retirement provision governs on a given day (s 8(3))? | 2 |
| 9 Duration of assessed income period | How long does my assessed income period last (s 9(1))? | 2 |
| 9 Duration of assessed income period | Is my assessed income period still in force on a given day (s 9)? | 19 |
| 9 Duration of assessed income period | On what day does my assessed income period stop being in force (s 9)? | 18 |
| 10 Effect of variations under section 7(4) | What state pension credit am I paid on a given day once my income element changes (s 10(2), (3))? | 7 |
| 10 Effect of variations under section 7(4) | Must the Secretary of State make a new decision before my changed amount is paid (s 10(2))? | 3 |
| Schedule 1 (Administration) and Schedule 2 (Minor and consequential amendments) | Can I be asked for evidence about likely future changes in my circumstances (Sch 1 para 3(3A))? | 3 |
| Schedule 1 (Administration) and Schedule 2 (Minor and consequential amendments) | Can I appeal against this decision about my assessed income period (Sch 1 para 12)? | 1 |
| Schedule 1 (Administration) and Schedule 2 (Minor and consequential amendments) | What am I paid for a period of less than a week (Sch 1 para 13)? | 2 |
| Schedule 1 (Administration) and Schedule 2 (Minor and consequential amendments) | Will the Secretary of State pay for my medical exemption from wearing a seat belt (Sch 2 para 26)? | 6 |
| Schedule 1 (Administration) and Schedule 2 (Minor and consequential amendments) | Am I free of a charge for a day-care service for a child in need (Sch 2 para 30)? | 6 |

A field of a record that the rule called never reads is given a fixed placeholder, with a comment saying so.
Three seat questions compose layer-1 rules rather than calling one: `How much guarantee credit...` and `How much savings credit...` call `s 2(2)` and `s 3(3)` behind `s 1(4) -- regulations or a pilot scheme may displace the Act's rules for the case` (answering NOTHING in a displaced case), and `Am I excluded from state pension credit because of my partner...` ORs `s 4(1)` and `s 4(1A)`. No new rule of the Act is stated in them.

## Tests

Expected values are hand-written from the text and were never edited to match output.
`spc-tests-layer1.l4` covers every branch of every rule with boundaries on both sides of each threshold (the savings credit threshold, amount A against amount B, the appropriate minimum guarantee, the minimum payable, 6 April 2016, the 65th, 75th and 80th birthdays, the qualifying-age day, the 12-month limit, the 5-year anniversary, the 6 April 2009 and 2014 window, one day against seven), a case outside the encoding for each of s 12(1) and s 18A(5) and for Sch 1 para 12, and every small rule of ss 1 to 4 and 6 to 9 directly.
`spc-cases-seat.l4` runs a real person's facts through every seat question, including the not-covered outcomes.
No assertion failed or was refused in the final run.
The only expected values changed after a run were the s 10 and Sch 2 para 17 amounts: when I found that those two rules answered an amount where the Act is silent (F-23) I corrected the rules, and rewrote their expectations from the text (NOTHING where the section does not apply) before rerunning; no expected value was ever changed to match what a rule printed.

**Mutation controls** (run on the layer-1 tests when they held 510 assertions): each of these edits to a copy of a layer-1 rule turned assertions red, so the tests can fail.

| edit | assertions red |
|---|---|
| s 2(1)(b): "does not exceed" read as "is less than" | 4 |
| s 3(1)(a): "before 6 April 2016" read as "on or before" | 4 |
| s 3(2)(b): "exceeds" read as "at least" | 2 |
| spc-dates: an age is attained the day AFTER the anniversary (so the 65th, 75th and 80th birthday tests all move) | 13 |
| s 7(4): the income-from-capital exception removed | 1 |
| a man's qualifying age read from his own pensionable age | 8 |

And in the seat tests: changing one expected amount (115 to 116) turned the three cases that assert it red, and reading a man's qualifying age from his own pensionable age turned three red.

## What the stable binary does not accept

The binary governs (1.6.98, built from main; sha256 below). What I met while writing, on this binary:

- **A long left-nested PLUS chain is very slow to type-check.** The ten-term sum of the ten descriptions of income in s 15(1) took 57 seconds in its module and made the entitlement module take 118 seconds; `sum (LIST a, b, ...)` takes 0.4 seconds. Chains of three are fine. The slowness is silent: no diagnostic, just a long wait.
- **AND/OR at one indentation raises a lint warning.** Asyndetic `...` next to `OR` at the same column is reported; the fix is to write the labelled rung on one line (`"label" ... atom`) and join rungs with OR, AND or `..`. A warning counts as red in `check.sh`.
- **A genitive in a function argument needs parentheses:** `filter f (x's y)`, not `filter f x's y`. And `PLUS sum (map ...)` did not parse; a `WHERE` helper did.
- **The names in the head of a definition must follow the order of its `GIVEN` list;** a mismatch is an error, not a reordering.
- **Record construction is by `Type WITH` and named fields,** which the seat layer uses everywhere; there is no record update (`base WITH f IS v`) on this binary per `dialects.md`, so every record in a `WHERE` is built whole.
- **`srcrefs.py` cannot quote a line that is only dots** (the blank rows of Schedule 2); the quote runs are split around them.
- **Constructs the skills describe that this binary does not take:** where the skills describe section-level `GIVEN`, `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, sets, `TYPICALLY` on fields, `WAIT UNTIL`, `@lang`, `@infix*`, `@nonexhaustive`, `RULES EFFECTIVE DATE`, `EVERY`, opaque `DECLARE T` and record update, I wrote what `dialects.md` says to write instead (a `GIVEN` on every rule, an explicit not-covered constructor or NOTHING, `WAITUNTIL`, the `YMD` shim) and did not re-probe each rejection; none is used here.
- **Not-covered values are NOTHING (a MAYBE) or a constructor of `Answer`** (`The Act says yes`, `The Act says no`, `Not covered by this encoding`), never FALSE or 0.

## What check.sh prints

`L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, run last, with the `l4` build named in `encoding.json`:

```
module                                    errors satisfied  failed  refused  expected
spc-cases-seat.l4                              0       229       0        0         0
spc-dates.l4                                   0         0       0        0         0
spc-nouns.l4                                   0         0       0        0         0
spc-part-entitlement.l4                        0         0       0        0         0
spc-part-final.l4                              0         0       0        0         0
spc-part-interpretation.l4                     0         0       0        0         0
spc-part-misc.l4                               0         0       0        0         0
spc-part-retirement.l4                         0         0       0        0         0
spc-sch1.l4                                    0         0       0        0         0
spc-sch2.l4                                    0         0       0        0         0
spc-sch3.l4                                    0         0       0        0         0
spc-seat.l4                                    0         0       0        0         0
spc-tests-layer1.l4                            0       564       0        0         0
TOTAL (13 modules)                             0       793       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/ukpga-2002-16.txt spc-*.l4`:

```
srcrefs check: 461 src: lines, 101 runs, 100 locators, 0 problems
```

Every file runs with no error or warning diagnostic; `expected_failed` in `check.sh` is empty because no file is meant to fail; each case file's assertions written equal its assertions satisfied.

## What would need doing before this encoding is worth relying on

1. A domain expert (a UK social security lawyer) reads every module against the OFFICIAL text, not this rendering, and rules on the forks; most urgently F-03 (the 3ZA route), F-13 (the 65th-birthday event), F-23 (the amount before the commencing date) and F-29 (couples).
2. The current regulations are brought in: the State Pension Credit Regulations 2002 and the annual up-rating order supply the standard minimum guarantee, the additional amounts, the savings credit threshold and percentages, the minimum payable and the prescribed circumstances. Until then every figure is a question the person is asked, and the seat layer says so.
3. The Pensions Act 1995 rules for pensionable age are brought in so that the two pensionable-age days become computed from the date of birth (F-27).
4. The date of Royal Assent and the commencement order(s) are filled in (F-19, F-20).
5. The Administration Act s 1 (claims) and the Social Security Act 1998 ss 8 to 10 and 27 are encoded, so that "a claim has been made" and "a section 27 restriction applies" stop being facts the person states.
6. The outstanding effect in the meta file and the 24 prospective effects are checked against the encoded text.
7. The seat's form is tried on a real claimant, to confirm the `@desc` wording and the order of the inputs (111 inputs in all; several questions ask 60 or more).

## Source and licence

See `SOURCE-LICENSE.md` (it points at `../../SOURCE-LICENSE.md`: Crown copyright, Open Government Licence v3.0).
The text is a converter rendering and is not marked up; this encoding quotes it line by line and claims nothing about the official text.

