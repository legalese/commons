# NOTES: Employment Insurance Regulations, piece er4 (Parts II, III, III.1 and III.2; lines 993-1393 of SOR-96-332.txt)

Written by the piece agent `er4` (Sonnet 5.5) on 2026-10-24.
Both texts are unofficial plain-text conversions made by a converter script from the Justice Laws Website consolidations; nothing here is "verified against the official text".
The Regulations are `SOR/96-332`, consolidation current to 2026-09-30, last amended 2026-04-01 (`../../registers/source-bundle/*.meta.json`).
Every rule in this piece's modules comes from the Regulations; `src:N` in a comment or an `@ref` is a line of `SOR-96-332.txt`.
Where a rule reads a figure or a condition of the Act (sections 12, 22, 23, 66, 66.4, 68, 69, 82, 152.04, 152.05, 152.14 and others) it takes it as an input and says so in a comment; the Act is the other pieces' (see Cross-references).

**What the piece is.**
The range is lines 993 to 1393.
The brief's one-line description of the piece names Parts II, III and III.1; its line range and its section labels (58 to 76.45) also take in Part III.2 (regs 76.31 to 76.45, premium reduction for self-employed persons covered by a provincial plan), so Part III.2 is encoded here and is not a gap.
Line 1393 is blank; Part IV opens at line 1394 (piece er5).
The range holds 66 sections (regs 58 to 76.45, which the section index lists for er4) and 48 heading lines (Part, Division and sub-headings); the coverage table has 183 rows: 66 sections (some as several subsection rows) and 48 headings.
Dispositions: 97 `encoded`, 29 `fork`, 54 `inert` (the 48 headings and six regulations: 76.07, 76.08, 76.26(2), 76.27(1), 76.27(2), 76.35), 3 `repealed or blank in this text` (76.041, 76.1, 76.12).
No row is `deferred`.

**Dates.**
No enactment, making or commencement date of the Regulations is in lines 993 to 1393, so no rule here carries one.
Reg 76 holds one date as data, `December 4, 1994` (`reg 76 December 4, 1994`, with an `@ref`).
Reg 76.23 speaks of "the day on which this Part comes into force"; the text in this range does not give it, so it is a DATE input of the rules `reg 76.23(a)` and `reg 76.23` and of the seat question (see Cross-references).
Reg 76.08 names the signing date of an agreement (March 1, 2005); it is in an `inert` row, because the signing of the Entente is not an enactment or commencement date of this text.
Time limits (30 days in regs 68(2), 70, 74; one year in reg 75; 12 months and three months in reg 76.43; 60 months in reg 76.11) follow the keel's reading F4 of the core: the last day counts, and months and years go through `add months` and `add years`.

**Method.**
Each module was written from the text of its lines; the quotations in the `-- src:N | ...` comments were copied from the raw file by a script (`srcrefs.py quote`), never retyped.
Duties with a deadline are encoded as the last day plus a BOOLEAN that says whether the act was done in time (constitutive rules, which can be asserted), not as regulative `PARTY ... MUST ...` rules, because a trace prints no assertion line and `check.sh` would count none.
Expected values in the tests were decided from the text before the run; no expected value was edited to match a result.
No `REFUSE`, `BECAUSE` or section `GIVEN` is used.

## Seat

**The seat.**
A person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission.
This is the seat the brief fixes for the whole text; this piece asks it of regs 58 to 76.45.
Officials (the Commission, the Minister of National Revenue, the Canada Revenue Agency, an officer) have no seat; they appear only as what the person is owed or exposed to.
No employer seat is written in this piece (the Commons rule allows one beside this, `er4-seat-employer.l4`, over the same modules); the employer's duties in Part III are encoded in layer 1 and reach the person only as the five-twelfths share (reg 61) and the category (reg 69(1)).

**Where the person's questions live.**
Part II gives the person a claim on the national employment service (regs 58(b), 58(c), 59).
Part III is about the employer's premium and the employer's wage-loss plan; the person asks whether the reduction is made in respect of them, whether the plan meets its standards, what share insured persons must benefit from, which category they are in, and from what date the reduction applies.
Parts III.1 and III.2 carry most of the person's questions: whether provincial benefits (QPIP is the instance the Regulations name in reg 76.08) bar or reduce federal benefits, how provincial weeks count, how weeks are shared by two parents in different provinces, and what premium is taken from them.
Where Parts III.1 and III.2 say the same thing (they are the same relation, Hohfeld's correlatives over again), one question serves the employed person and the self-employed person and asks "Are you self-employed?"; the self-employed rule calls the Part III.1 rule where the arithmetic is the same.

**Provisions with no question, and why.**
- reg 58(a), 58(d): a duty of the Commission as to what it collects and what it does for employers; the person is owed nothing by them (the person's claim is (b) and (c)).
- regs 62(3), (4): the Commission's computation of the two cost ratios; it decides nothing the person could state facts about.
- regs 63 to 66 are asked in one question (11); regs 67(1), (3), (5) are asked inside question 14, reg 67(2) in 15 and 67(4) inside 15.
- regs 68(1), 68(2), 69(2), 69(3), 69(4), 70, 72, 73, 74, 75, 76: duties and powers of the employer and the Commission between themselves; reg 69(1) is asked (the person's category), the rest are not the person's duties or claims.
- regs 76.02 (a reading rule), 76.03 and 76.32 (standards a province's plan must meet), 76.06 (the Commission's rate formula, on actuarial estimates), 76.07 and 76.35 (publication), 76.08, 76.27 and 76.26(2) (accounting between governments): no question; each is in layer 1 or in an `inert` row with its reason.
Every one of these is encoded in layer 1 or marked `inert`; the seat never decides what is left out.

**The 45 questions** (`@export`, each with `@desc` on every input, grouped under `§` headings in the order of the text; the Part III group only arises for a person whose employer has a wage-loss plan, and the Parts III.1 and III.2 groups only for a person who lives where a province pays its own benefits for pregnancy or the care of a new-born or adopted child, or whose partner does).

**§ Part II -- the national employment service**

1. Can I use the national employment service at no cost (reg 59)?
2. Is the national employment service to make labour market information available to me (reg 58(b))?
3. Is the national employment service to give me information on job openings and on careers in demand (reg 58(c)(i))?
4. Is the national employment service to refer me to other sources of labour market information (reg 58(c)(ii))?
5. May the national employment service obtain from me the information it needs to refer me to jobs (reg 58(c)(iii))?
6. Is the national employment service to interview and counsel me and help me make an action plan (reg 58(c)(iv))?
7. Is the national employment service to tell me about special assistance (reg 58(c)(v))?

**§ Part III -- my employer's sick-leave or wage-loss plan**

8. Is my employer's premium rate reduced because of me (regs 62(1), 62(2))?
9. By how much must the insured persons benefit from my employer's premium reduction, in dollars (reg 61)?
10. Does the Part on employers' wage-loss plans apply to me and my co-workers (reg 61)?
11. Does my employer's wage-loss plan meet the standards for its kind (regs 63, 64, 65, 66)?
12. Which category of insured persons am I placed in on my employer's application (reg 69(1))?
13. From what date does my employer's premium reduction take effect (reg 71)?
14. Is my employer's plan a qualifying plan (reg 67(3))?
15. For how many months of the year does my employer's premium reduction apply (reg 67(2), reg 67(4), reg 71)?

**§ Parts III.1 and III.2 -- am I barred from federal benefits because I can receive provincial benefits?**

16. Are the benefits I am paid provincial benefits within the meaning of these Regulations (regs 76.01, 76.31)?
17. Is my province's plan a plan to which these Regulations apply (regs 76.01, 76.31)?
18. Am I disentitled to maternity or parental benefits because I can receive provincial benefits (regs 76.09(1), 76.09(2), 76.36(1), 76.36(2))?
19. Am I still caught by the provincial benefit rules if I have moved to another province (regs 76.09(4), 76.36(4))?
20. Am I disentitled to a week of other benefits, or of fishing benefits, because I received provincial benefits for that week (reg 76.09(3))?
21. As a self-employed person, am I disentitled to a week of other benefits because I received provincial benefits for that week (reg 76.36(3))?
22. Am I disentitled because the other person caring for our child is entitled to provincial benefits (regs 76.09(5), 76.36(5))?

**§ Parts III.1 and III.2 -- how provincial benefits affect my claim and my weeks**

23. Am I an insured participant for employment benefits assistance (reg 76.11)?
24. Does a week I was paid provincial benefits count as a week in receipt of benefits when my qualifying period is extended (reg 76.13)?
25. Do my benefits count as paid for pregnancy or the care of a new-born when my benefit period is extended (reg 76.14(a))?
26. Up to how many weeks is my benefit period extended so that my other special benefits can be paid (reg 76.14(b))?
27. By how many weeks is my benefit period extended because my child was in hospital (reg 76.15)?
28. How much will my benefits for a week be after the provincial benefits are deducted, in dollars (regs 76.16, 76.17, 76.37, 76.38)?
29. May a week of my EI benefits be counted for a purpose when a week of my provincial benefits has already been counted for it (regs 76.18, 76.39)?
30. How many weeks of benefits are left within my maximum once my provincial weeks are counted (regs 76.19(1), 76.4(1))?
31. How many weeks of benefits do my provincial weeks, paid at an accelerated rate, represent (regs 76.19(2), 76.19(3), 76.4(3), 76.4(4))?
32. How many of my provincial weeks are taken into account when the provincial plan allows more weeks than the Act (regs 76.2, 76.41)?
33. When is my benefit period deemed to have begun when I had a benefit period under a provincial law (regs 76.19(1.1), 76.4(2))?
34. How many weeks of parental benefits can I be paid when the other parent claims provincial benefits (regs 76.21, 76.42)?
35. Is my waiting period waived because provincial benefits were paid to me (regs 76.22, 76.421)?
36. Does the Act as it stood before the provincial plan rules still apply to my claim (reg 76.23)?
37. Am I deemed to meet the 12-month condition after moving out of a province with a plan (reg 76.43)?

**§ Parts III.1 and III.2 -- the premium I pay**

38. Will my employer take the provincial premium reduction into account when deducting my premium (regs 76.04, 76.24, 76.25)?
39. As a self-employed person, is my self-employment premium reduced because of provincial benefits (reg 76.33)?
40. By how much is my premium reduced, in dollars (regs 76.05, 76.34)?
41. How much premium adjustment is paid to my province on my behalf, in dollars (reg 76.26(1))?
42. What premiums are counted in deciding whether I overpaid, once my province's premium adjustment is added (reg 76.28(1))?
43. Is a premium adjustment paid to my province counted in deciding whether I overpaid (reg 76.28(2))?
44. May the Canada Revenue Agency and the Minister of National Revenue disclose my information to my province (regs 76.3, 76.45)?
45. Will my social insurance number be used to exchange information with my province (regs 76.29, 76.44)?

**Assumed, not ruled** (design choices of this piece, each reversible in one place):
- Question 38 returns a result enum declared in the seat file, `er4 What the employer does about the provincial premium reduction at source`, with a third value `er4 the Regulations do not say`; its third BRANCH arm (a person covered by a plan and working in the plan's province gets the reduction by reg 76.04) is this piece's composition of regs 76.04, 76.24 and 76.25, not a rule the text states.
- Question 11 builds the lists the layer-1 rules read (the events that end payment, the conditions that preclude payment) from yes/no answers; whether a plan's own condition fits one of the 17 of reg 63(g), within its limits, is therefore the person's answer to one question (`my plan refuses payment in a case reg 63(g) does not allow`), whose `@desc` lists the 17.
- A judgment the text hands to the service or the Commission ("where appropriate", "when necessary", "substantially equivalent", "substantially the same persons") is asked as a yes/no fact about that judgment and never decided.
- The Act's figures that the formulas of regs 76.14 and 76.21 read (the 35 and 61 weeks of s 12(3)(b), the 40 of s 12(4)(b)(i), the maxima of s 12(3) and s 152.14) are asked as numbers; a change in the Act changes those inputs, not a rule. They are the Act's, out of range (Cross-references).
- A fisher claims under the Employment Insurance (Fishing) Regulations, an instrument that is in neither input; this piece meets it once, in reg 76.09(3)(b), and takes it as a constructor of the choice in question 20.
- The `@desc` of question 11's condition input quotes the 17 conditions of reg 63(g) in the person's words; it is a paraphrase for the form, not the text.

## Jural relations

One row per provision that creates a relation, at the grain of the regulation (a subsection that stands apart from its section has its own row).
Hohfeld's correlatives: claim and duty; privilege (liberty) and no-right; power and liability; immunity and disability.
Each relation is stated once, in the rule named in the last column, which is named for the relation and not for one party.
The last row, `none`, lists the provisions that create no relation (definitions, counting rules, conditions that other rules use).

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| reg 58(b) | a member of the general public (also a public authority, an employers' or a workers' organization) | the Commission | claim / duty | `reg 58(b) the national employment service is to make labour market information available systematically and promptly to` |
| reg 58(c)(i) | a worker | the Commission | claim / duty | `reg 58(c)(i) the national employment service is to make available information on employment opportunities and on careers and occupations in demand to` |
| reg 58(c)(ii), (iv) | a worker | the Commission, which holds the judgments "where appropriate", "when necessary" and "in accordance with local strategies" | claim / duty, conditional on the service's judgment | `reg 58(c)(ii) ...`, `reg 58(c)(iv) ...` |
| reg 58(c)(iii) | the Commission (it obtains the information it needs to refer a worker seeking employment) | the worker (the text states no duty to give it; the worker is exposed to the request) | privilege / no-right | `reg 58(c)(iii) ...` |
| reg 58(c)(v) | a worker having particular difficulty obtaining or keeping employment | the Commission | claim / duty | `reg 58(c)(v) ...` |
| reg 58(d) | an employer | the Commission | claim / duty | `reg 58(d) the help the national employment service is to give an employer to find suitable workers` |
| reg 59 | a worker (insured or not, claiming or not), an employer, a workers' organization, an organization providing employment assistance services | the Commission | claim / duty (the service is free of charge) | `reg 59 the national employment service is to be made available at no cost to` |
| reg 61 | the insured persons covered by the plan | the employer | claim / duty (at least five-twelfths of the reduction) | `reg 61 this Part applies`, `reg 61 five-twelfths of the reduction of the employer's premium` |
| reg 62(1) | the employer | the Commission | claim / duty (the employer's premium rate is reduced) | `reg 62(1) the employer's premium rate is to be reduced in respect of the insured person` |
| reg 62(2) | the Commission | the employer | privilege / no-right (no reduction for the three cases) | `reg 62(2) the employer's premium rate is not to be reduced in respect of the insured person` |
| reg 62(3), (4) | the employer and the insured persons | the Commission | claim / duty (to compute the two ratios) | `reg 62(3) the experience cost ratio`, `reg 62(4) the first payer cost ratio` |
| reg 67(2) | the employer | the Commission | claim / duty (the reduction applies to the qualifying months) | `reg 67(2) the number of months in the year to which the reduction applies` |
| reg 68(1) | the employer (power to apply) | the Commission (liability to a proper application, to be decided by 72(1)) | power / liability | `reg 68(1) the application is in the form the subsection requires` |
| reg 68(2) | the Commission (claim to the information within 30 days; power to decide on what exists) | the employer (duty; liability to the decision) | claim / duty; power / liability | `reg 68(2) ...` (three rules) |
| reg 69(1) | the Commission and the Canada Revenue Agency (the employer's grouping) | the employer (duty); the insured person is placed in the category | claim / duty | `reg 69(1) the category the insured person is placed in` |
| reg 69(2), (3), (4) | the Commission and the Canada Revenue Agency | the employer | claim / duty | `reg 69(2) ...`, `reg 69(3) ...`, `reg 69(4) ...` |
| reg 70, reg 74 | the Commission | the employer | claim / duty (30 days) | `reg 70 the employer has done what the section requires`, `reg 74 ...` |
| reg 72(1) | the employer | the Commission (an officer) | claim / duty (to decide and notify) | `reg 72(1) ...` |
| reg 72(2) | the employer | the Commission (an officer) | claim / duty (to be heard first) | `reg 72(2) ...` |
| reg 72(3) | the Commission (an officer: power to terminate) | the employer | power / liability | `reg 72(3) ...` |
| reg 73 | the Commission | the employer | claim / duty (evidence on a late application) | `reg 73 ...` |
| reg 75 | the employer (power to appeal within one year after notice is sent) | the Commission | power / liability | `reg 75 the employer may appeal to the Commission` |
| reg 76 | the Commission (power to reconsider a 1995 application) | the employer | power / liability | `reg 76 the Commission may reconsider the application for the year 1995` |
| reg 76.04, 76.05 | the employee and the employer (premiums reduced) | the Commission and the Minister of National Revenue | claim / duty | `reg 76.04 ...`, `reg 76.05 ...` |
| reg 76.09(1), (3), (5) | the Commission (it need not pay) | the claimant | privilege / no-right (disentitlement) | `reg 76.09(1) ...`, `reg 76.09(3) ...`, `reg 76.09(5)(a) ...`, `(b)` |
| reg 76.09(2) | the claimant (power to ask for a determination) | the Commission (liability to determine; a finding lifts the bar) | power / liability | `reg 76.09(2) subsection (1) does not apply` |
| reg 76.11 | an insured person who qualifies | the Commission | claim / duty (treated as an insured participant for assistance under employment benefits) | `reg 76.11 ...` |
| regs 76.13, 76.14, 76.15 | the claimant | the Commission | claim / duty (weeks counted, benefit period extended) | `reg 76.13 ...`, `reg 76.14(a) ...`, `reg 76.14(b) ...`, `reg 76.15 ...` |
| regs 76.16, 76.17 | the Commission (power to deduct the provincial amount) | the claimant | power / liability | `reg 76.16 ...`, `reg 76.17 ...` |
| reg 76.18, reg 76.39 | the claimant (not counted twice) | the Commission | immunity / disability | `reg 76.18 ...`, `reg 76.39 ...` |
| regs 76.19, 76.2 | the claimant | the Commission | claim / duty (provincial weeks count, up to the Act's maximum) | `reg 76.19(1) ...`, `reg 76.19(2) and (3) ...`, `reg 76.2 ...` |
| reg 76.21 | the claimant (share of the weeks) | the Commission | claim / duty (the provincial applicant's side is provincial law, out of range) | `reg 76.21 the number of weeks of benefits payable to the claimant` |
| reg 76.22 | the claimant | the Commission | claim / duty (waiting period waived) | `reg 76.22 ...` |
| reg 76.23 | the claimant | the Commission | immunity / disability (the Act as before continues) | `reg 76.23 the Act applies to the claim as it did before this Part` |
| reg 76.24 | the Minister of National Revenue (full premium) | the employer (duty not to apply the reduction); the insured person (liable to the unreduced deduction) | claim / duty; power / liability | `reg 76.24 ...` |
| reg 76.25 | the insured person | the employer | claim / duty (the reduction is applied at source) | `reg 76.25 ...` |
| reg 76.26(1) | the province | the Minister of National Revenue | claim / duty (the premium adjustment) | `reg 76.26(1) the premium adjustment that the Minister of National Revenue is to pay to the province` |
| reg 76.28(1) | the employee | the Minister of National Revenue | claim / duty (the adjustment is counted for the overpayment) | `reg 76.28(1) ...` |
| reg 76.29, 76.44 | the Government of Canada and the province | the claimant, the self-employed person | privilege / no-right (the number is used for the exchange) | `reg 76.29 ...`, `reg 76.44 ...` |
| reg 76.3, 76.45 | the Canada Revenue Agency and the Minister of National Revenue | the person whose information it is | privilege / no-right (disclosure to the province) | `reg 76.3 ...`, `reg 76.45 ...` |
| regs 76.33, 76.34 | the self-employed person | the Commission and the Minister of National Revenue | claim / duty (the self-employment premium is reduced) | `reg 76.33 ...`, `reg 76.34 ...` |
| reg 76.36 | the Commission (it need not pay) | the self-employed person | privilege / no-right; power / liability for (2) | `reg 76.36(1) ...`, `(2)`, `(3)`, `(4)`, `(5)(a)`, `(b)` |
| regs 76.37, 76.38 | the Commission (power to deduct) | the self-employed person | power / liability | `reg 76.37 ...`, `reg 76.38 ...` |
| regs 76.4, 76.41, 76.42, 76.421 | the self-employed person | the Commission | claim / duty (as regs 76.19, 76.2, 76.21, 76.22) | `reg 76.4(1)(a) ...`, `reg 76.41 ...`, `reg 76.42 ...`, `reg 76.421 ...` |
| reg 76.43 | the self-employed person (deemed to satisfy paragraph 152.07(1)(a)) | the Commission | claim / duty | `reg 76.43 ...` |
| none | reg 60 (definition), regs 63 to 66 (the standards that condition reg 62(1)), reg 67(1), (3), (4), (5), reg 71, reg 76.01, 76.02, 76.03, 76.06, 76.31, 76.32 (definitions, reading rule, standards and a formula that other rules use), reg 76.4(2) to (4) (counting rules); regs 76.07, 76.08, 76.26(2), 76.27, 76.35 are `inert` (machinery) | | no relation of its own | |

## Coverage table

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| heading "PART II National Employment Service" | src:993 | inert | - | A Part heading; it carries no text of its own. |
| reg 58 (lead-in) | src:994 | encoded | er4-part2-national-employment-service.l4: comment; fork F2 | States the purpose (integration of persons who need assistance in competing in the labour market) and the manner (in cooperation with public authorities, employers, unions and organizations); a purpose is not a condition, since reg 59 opens the service to all workers. Quoted with (a) and cited in the `@ref` of the (a) declaration. |
| reg 58(a) | src:995 | encoded | er4-part2-national-employment-service.l4: `reg 58(a) the information the national employment service is to collect and analyse`, `reg 58(a) the levels at which the national employment service is to collect and analyse it` | A duty on the Commission as to what it collects: the six matters and four levels as data. No seat question: it gives the person nothing to claim. |
| reg 58(b) | src:996 | encoded | er4-part2-national-employment-service.l4: `reg 58(b) the national employment service is to make labour market information available systematically and promptly to` | A member of the general public is a recipient (the person's claim); anyone not named gets NOTHING. |
| reg 58(c) (lead-in) | src:997 | encoded | er4-part2-national-employment-service.l4: comment; each limb takes `the person is a worker` | Helps 'workers'; not defined, so a BOOLEAN input. |
| reg 58(c)(i) | src:998 | encoded | er4-part2-national-employment-service.l4: `reg 58(c)(i) the national employment service is to make available information on employment opportunities and on careers and occupations in demand to` | A worker's claim, no further condition. |
| reg 58(c)(ii) | src:999 | encoded | er4-part2-national-employment-service.l4: `reg 58(c)(ii) the national employment service is to refer a worker to other sources of labour market information` | 'Where appropriate' is a judgment left to the service: a BOOLEAN input (fork F1). |
| reg 58(c)(iii) | src:1000 | encoded | er4-part2-national-employment-service.l4: `reg 58(c)(iii) the national employment service is to obtain from a worker the information necessary to effect proper referrals` | Applies to a worker seeking employment. The service obtains the information; the text puts no duty to give it on the worker. |
| reg 58(c)(iv) | src:1001 | encoded | er4-part2-national-employment-service.l4: `reg 58(c)(iv) the national employment service is to interview and counsel a worker and help them develop action plans` | Two judgments of the service: local strategies call for it, and it is necessary (fork F1). |
| reg 58(c)(v) | src:1002 | encoded | er4-part2-national-employment-service.l4: `reg 58(c)(v) the national employment service is to provide a worker with information on the availability of special assistance` | Where the worker is experiencing particular difficulty obtaining or keeping employment. |
| reg 58(d) | src:1003-1006 | encoded | er4-part2-national-employment-service.l4: `reg 58(d) the help the national employment service is to give an employer to find suitable workers` | Help to employers, three limbs, as data. No seat question: it is for employers, not for the individual. |
| reg 59 | src:1007 | encoded | er4-part2-national-employment-service.l4: `reg 59 the national employment service is to be made available at no cost to` | Free to all workers whether insured or not and whether claiming or not (neither is an input), and to employers, workers' organizations and organizations providing employment assistance services. Anyone else: NOTHING. |
| heading "PART III Reduction of Premium for Employers with Wage-Loss Plans" | src:1009 | inert | - | A Part heading; it carries no text of its own. |
| heading "Interpretation" (line 1011) | src:1011 | inert | - | A heading; it carries no text of its own (reg 60 follows). |
| reg 60 | src:1012-1013 | encoded | er4-nouns.l4: `er4 Kind of wage-loss plan`; er4-part3-reduction.l4: `reg 60 plan` | The definition of 'plan': a wage-loss plan covering insured persons employed by an employer, which includes the four named kinds (fork F3). |
| heading "Application" | src:1015 | inert | - | A heading; it carries no text of its own (reg 61 follows). |
| reg 61 | src:1016 | encoded | er4-part3-reduction.l4: `reg 61 this Part applies`, `reg 61 five-twelfths of the reduction of the employer's premium` | The insured persons must benefit from at least 5/12 of the reduction (also Act s 69(1)(b), out of range, piece ei3). The person's claim against the employer, paired with the employer's undertaking in reg 68(1)(c). |
| heading "Reduction of Employer's Premium Rate" | src:1018 | inert | - | A heading; it carries no text of its own (reg 62 follows). |
| reg 62(1) | src:1019-1022 | fork | er4-part3-reduction.l4: `reg 62(1) the percentage by which the experience cost ratio is less than the first payer cost ratio`, `reg 62(1) the employer's premium rate reduced by the percentage`, `reg 62(1) the employer's premium rate is to be reduced in respect of the insured person` | F4: 'the percentage by which (a) is less than (b)' read as the relative shortfall (b minus a) over b. Subject to (2); covered, plan meets the requirements and is a qualifying plan (reg 67(3)). |
| reg 62(2) | src:1023-1026 | encoded | er4-part3-reduction.l4: `reg 62(2) the employer's premium rate is not to be reduced in respect of the insured person` | Not reduced for a person not covered, covered by a plan that does not meet the requirements, or whose eligibility to use paid sick leave is deferred under a plan of reg 65 or 66. |
| reg 62(3) | src:1027-1031 | encoded | er4-part3-reduction.l4: `reg 62(3) the three years over which both averages are taken`, `reg 62(3) the experience cost ratio` | Yearly figures are inputs (out of range: Act ss 12 and 18(1)(b), piece ei1). The Commission's computation; no seat question. |
| reg 62(4) | src:1032-1036 | encoded | er4-part3-reduction.l4: `reg 62(4) the first payer cost ratio` | Same arithmetic on the Commission's estimates, which are inputs (a judgment of the Commission). |
| heading "Standards" (line 1038) | src:1038 | inert | - | A heading; it carries no text of its own (regs 63 to 67 follow). |
| reg 63 (lead-in) | src:1039 | encoded | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63 the plan meets the requirements of a Weekly Indemnity Plan` | The seven paragraphs joined by AND; the plan 'shall meet' all. The facts of one plan are in `er4 Case under a Weekly Indemnity Plan`. |
| reg 63(a) | src:1040-1042 | fork | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(a) the person becomes eligible to claim benefits under the plan in time` and its helpers | F5 (maximum wait), F6 (hour-bank limb replaces month limb): eligible on or before the first day of the month following the last day of a period of at most three months from commencement, or (hour-bank) the day of 400 hours. |
| reg 63(b) | src:1043 | encoded | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(b) any elimination period does not exceed seven consecutive days beginning with the first day of the period of incapacity` | No elimination period: nothing to test. |
| reg 63(c) | src:1044-1046 | encoded | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(c) benefits are paid in full regardless of the benefits payable under the Act and from other sources` | Both limbs (i) and (ii) required. |
| reg 63(d) | src:1047 | encoded | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(d) the benefits payable under the plan are at least 55% of the normal weekly insurable earnings` | Equal to 55% meets it (boundary asserted). |
| reg 63(e) | src:1048-1050 | fork | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(e)(i) full benefits are reinstated in time on the recurrence of an illness or injury`, `reg 63(e)(ii) full benefits are reinstated in time for a new illness or injury`, `reg 63(e) full benefits are reinstated as the paragraph requires` | F5, F6: three months or 400 hours on a recurrence; one month or 150 hours for a new illness. Subject to the elimination period of (b), which these tests do not touch. |
| reg 63(f) | src:1051-1055 | fork | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(f) an event at which payment under the plan may end`, `reg 63(f) benefits are payable until the earliest of the four events` | F7: the plan pays for at least 15 weeks and may stop only at an event the paragraph names. |
| reg 63(g) | src:1056-1073 | encoded | er4-part3-reg63-weekly-indemnity-plan.l4: `reg 63(g) a condition that may preclude payment of benefits under the plan`, `reg 63(g) the only conditions precluding payment are conditions the paragraph lists` | A closed list of 17 conditions as an enum (five carry the paragraph's own limit as a field) plus a constructor for a condition on no line; the plan's own list is checked with all. |
| reg 64 (lead-in) | src:1074 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 64 the plan meets the requirements of a Special Weekly Indemnity Plan` | The four paragraphs joined by AND. |
| reg 64(a) | src:1075 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 64(a) the plan is provided or financed, in whole or in part, by an employer the paragraph names` | Five kinds of employer named; any other employer fails. |
| reg 64(b) | src:1076 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 64(b) the plan satisfies all the requirements of section 63 except paragraphs 63(e) and (f)` | Calls 63(a), (b), (c), (d) and (g); a test asserts that a case failing 63(e) and (f) still passes. |
| reg 64(c) | src:1077 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 64(c) full benefits are reinstated after one month of active employment` | F5: at most one month. |
| reg 64(d) | src:1078-1082 | fork | er4-part3-regs64-66-other-plans.l4: `reg 64(d) an event at which payment under the plan may end`, `reg 64(d) benefits are payable until the earliest of the four events` | F7: at least 52 weeks; the same four events as 63(f). |
| reg 65 (lead-in) | src:1083 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 65 the plan meets the requirements of a Cumulative Paid Sick Leave Plan` | (a), (b), (d), (e) and (f) joined by AND; (c) permits and adds no test (fork F8). |
| reg 65(a) | src:1084 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 65(a) the plan satisfies all the requirements of section 63 except paragraphs 63(e) and (f)` | Calls 63(a), (b), (c), (d) and (g). |
| reg 65(b) | src:1085 | fork | er4-part3-regs64-66-other-plans.l4: `reg 65(b) the plan credits at least one day of paid sick leave each full month, at least one of them reserved` | F9: the sentence says one or more days credited and at least one day a month available only for illness, injury, pregnancy, child care or care or support; read as two floors. |
| reg 65(c) | src:1086-1089 | fork | er4-part3-regs64-66-other-plans.l4: `reg 65(c)(i) the paid sick leave credit for a month, prorated in relation to the active employment in the month`, `reg 65(c)(ii) the plan may preclude the accumulation of paid sick leave for the month`, `reg 65(c)(iii) the plan may allow the insured person to use paid sick leave while remaining at home for` | F10 (proration formula). What the plan MAY do 'notwithstanding paragraph (b)': three permissions, each a small rule, none a test (F8). |
| reg 65(d) | src:1090 | fork | er4-part3-regs64-66-other-plans.l4: `reg 65(d) any deferral of eligibility to use paid sick leave is for no more than 12 months` | F22: the 12-month cap is tested on any deferral the plan has (no deferral is 0 months); the text states it for a temporary or probationary person. A person whose eligibility is deferred gets no reduction (reg 62(2)(c)). |
| reg 65(e) | src:1091 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 65(e) unused days accumulate at the prescribed rate up to at least 75 working days` | The 'rate prescribed in paragraphs (b) and (c)' is the credit of (b) as (c) allows it to be prorated or withheld. |
| reg 65(f) | src:1092-1097 | fork | er4-part3-regs64-66-other-plans.l4: `reg 65(f) an event at which payment under the plan may end`, `reg 65(f) benefits are payable until the earliest of the five events` | F7: at least 75 working days; five events, which add the exhaustion of all accumulated paid sick leave. |
| reg 66 (lead-in) | src:1098 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 66 the plan meets the requirements of an Enhanced Cumulative Paid Sick Leave plan` | (a), (b), (d) and (e) joined by AND; the text says 'Enhanced Cumulative Paid Sick Leave' without 'Plan' in the lead-in (reproduced in the name only as 'plan'). |
| reg 66(a) | src:1099 | fork | er4-part3-regs64-66-other-plans.l4: `reg 66(a) the plan satisfies all the requirements of section 65 except paragraph 65(b), subparagraph 65(c)(i) and paragraphs 65(e) and (f)` | F8: leaves 65(a) and 65(d) as tests; 65(c)(ii) and (iii) are permissions with nothing to satisfy. |
| reg 66(b) | src:1100 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 66(b) the plan credits at least one and two thirds days of paid sick leave each full month, that many reserved` | 5/3 of a day, exact (boundary asserted at 5/3 and at 1.66). |
| reg 66(c) | src:1101 | fork | er4-part3-regs64-66-other-plans.l4: `reg 66(c) the paid sick leave credit for a month, prorated in relation to the active employment in the month` | F10: the permission to prorate, as in 65(c)(i). |
| reg 66(d) | src:1102 | encoded | er4-part3-regs64-66-other-plans.l4: `reg 66(d) unused days accumulate at the prescribed rate up to at least 125 working days` | As 65(e) with 125 working days. |
| reg 66(e) | src:1103-1108 | fork | er4-part3-regs64-66-other-plans.l4: `reg 66(e) an event at which payment under the plan may end`, `reg 66(e) benefits are payable until the earliest of the five events` | F7: at least 125 working days; the same five events as 65(f). |
| reg 67(1) | src:1109-1116 | fork | er4-part3-qualifying-plan.l4: `reg 67(1) the form is a formal written commitment`, `reg 67(1) the plan is evidenced by a formal written commitment` | F11: 'including' leaves the list open, so another formal written commitment counts; a board of directors' resolution only if implemented. |
| reg 67(2) | src:1117 | fork | er4-part3-qualifying-plan.l4: `reg 67(2) the number of months in the year to which the reduction applies` | F13: 'subject to section 71' read as: no month before the effective date of the reduction counts. |
| reg 67(3) | src:1118 | encoded | er4-part3-qualifying-plan.l4: `reg 67(3) the plan is a qualifying plan` | Evidenced, and meets 63 or 64, or (subject to (5)) 65 or 66 and credited as (5) says. |
| reg 67(4) | src:1119-1121 | encoded | er4-part3-qualifying-plan.l4: `reg 67(4) the day on which a plan is considered to become or cease to be a qualifying plan` | On or before the 15th: the first of that month; after the 15th: the first of the next month (15 and 16 March asserted). |
| reg 67(5) | src:1122-1124 | fork | er4-part3-qualifying-plan.l4: `reg 67(5) each insured person covered by the plan is credited with the days the subsection requires`, `reg 67(5)(a) the days of paid sick leave a person must be credited with under a plan of section 65`, `reg 67(5)(b) the days of paid sick leave a person must be credited with under a plan of section 66`, `reg 67(5) the day as of which the plan is considered to be a qualifying plan` | F12: 'equal to' read strictly, so a credit above the figure is not met. The maximum accumulable days are an input. |
| heading "Application for Reduction of Employer's Premium Rate" | src:1126 | inert | - | A heading; it carries no text of its own (regs 68 to 73 follow). |
| reg 68(1) | src:1127-1130 | encoded | er4-part3-application.l4: `reg 68(1) the application is in the form the subsection requires` | The employer's application must carry the documents of the formal commitment, the information and the 5/12 undertaking. An employer's duty; no seat question. |
| reg 68(2) | src:1131 | encoded | er4-part3-application.l4: `reg 68(2) the last day for the employer to provide the information or documentation`, `reg 68(2) the employer provided the information or documentation within 30 days after the request`, `reg 68(2) an officer of the Commission is to make a decision on the existing information or documentation` | 30 days from the Commission's request (the keel's counting, F4); if not provided, the officer decides on what exists. |
| reg 69(1) | src:1132-1137 | encoded | er4-part3-application.l4: `er4 Category of insured persons`, `reg 69(1) the category the insured person is placed in` | Five categories; a person whose eligibility to use paid sick leave is deferred (65(d)) falls in the residual category. The person's own category decides whose account number their premiums go to; seat question. |
| reg 69(2) | src:1138-1140 | fork | er4-part3-application.l4: `reg 69(2) the employer has done what the subsection requires` | F14: 'immediately' has no number of days; a BOOLEAN input for whether it was done immediately. The duty arises on the Commission's notification. |
| reg 69(3) | src:1141-1143 | fork | er4-part3-application.l4: `reg 69(3) the employer has done what the subsection requires` | F14, as 69(2); arises on a change in the categories plus the Commission's notification. |
| reg 69(4) | src:1144-1146 | encoded | er4-part3-application.l4: `reg 69(4) the employer has done what the subsection requires for the year` | Remitting by category account from the first remittance, and an information return for each account number. |
| reg 70 | src:1147-1149 | encoded | er4-part3-application.l4: `reg 70(a) the last day for the employer to notify the Commission`, `reg 70(a) the employer notified the Commission within 30 days after the modification or replacement`, `reg 70 the employer has done what the section requires` | Notify within 30 days after the modification or replacement; apply for a continuation under reg 68. |
| reg 71 | src:1150-1154 | encoded | er4-part3-application.l4: `reg 71 the effective date of the reduction of the employer's premium rate` | Initial application: first day of the next month if made on or before the 15th, of the second next month if after (not reg 67(4)); continuation: the effective date of the modification or replacement. |
| reg 72(1) | src:1155 | encoded | er4-part3-application.l4: `reg 72(1) an officer of the Commission is to decide whether the employer meets or continues to meet the requirements and notify the employer` | On receiving an application in accordance with reg 68 the officer must decide and notify: what the employer is owed. |
| reg 72(2) | src:1156 | encoded | er4-part3-application.l4: `reg 72(2) an officer of the Commission is to give the employer an opportunity to be heard, then decide and notify the employer` | Non-compliance with reg 70: the employer must first be given an opportunity to be heard. |
| reg 72(3) | src:1157 | encoded | er4-part3-application.l4: `reg 72(3) an officer of the Commission is to terminate entitlement to the reduction and notify the employer` | Only when the plan has ceased to meet 63(d) (it met it before, not now); 72(3) names 63(d) alone. |
| reg 73 | src:1158 | encoded | er4-part3-application.l4: `reg 73 the employer has produced the evidence the regulation requires` | An employer on a late application (Act s 69(4), out of range, piece ei3) must produce evidence of a qualifying plan in effect during the period. |
| heading "Termination of Plan" | src:1160 | inert | - | A heading; it carries no text of its own (reg 74 follows). |
| reg 74 | src:1161 | encoded | er4-part3-application.l4: `reg 74 the last day for the employer to notify the Commission of the termination`, `reg 74 the employer notified the Commission of the termination within 30 days` | 30 days after the plan is terminated. |
| heading "Appeals" | src:1163 | inert | - | A heading; it carries no text of its own (reg 75 follows). |
| reg 75 | src:1164 | encoded | er4-part3-application.l4: `er4 Decision the employer may appeal to the Commission`, `reg 75 the last day for the employer to appeal`, `reg 75 the employer may appeal to the Commission` | The employer's power to appeal three kinds of decision within one year after notice is sent (Commission's liability); any other decision: NOTHING. |
| heading "Transitional Provisions" | src:1166 | inert | - | A heading; it carries no text of its own (reg 76 follows). |
| reg 76 | src:1167-1170 | encoded | er4-part3-application.l4: `reg 76 December 4, 1994`, `reg 76 the Commission may reconsider the application for the year 1995` | A power of the Commission to reconsider a 1995 application made before 4 December 1994; probably spent in practice, but still law in this text, so encoded. The date is data with an @ref. |
| heading "PART III.1 Reduction of Premiums for Employees Covered by a Provincial Plan and for their Employers" | src:1172 | inert | - | A Part heading; it carries no text of its own. |
| heading "DIVISION 1 General" | src:1174 | inert | - | A Division heading; it carries no text of its own. |
| heading "Interpretation" (line 1176) | src:1176 | inert | - | A heading; it carries no text of its own (reg 76.01 follows). |
| reg 76.01 | src:1177-1180 | encoded | er4-part3-1-premium-reduction.l4: `reg 76.01 provincial benefits`, `reg 76.01 provincial plan`, `er4 Operating cost of the Act`, `reg 76.01 variable administrative costs` | Three definitions: provincial benefits (paid under a provincial plan because of pregnancy or the care of new-born or adopted children), provincial plan (with the agreement with the Government of Canada), variable administrative costs (direct costs that fluctuate with the claims processed; fixed costs excluded). |
| heading "Adaptation of the Act and these Regulations" | src:1182 | inert | - | A heading; it carries no text of its own (reg 76.02 follows). |
| reg 76.02 | src:1183 | encoded | er4-part3-1-premium-reduction.l4: `er4 Provision of the Act or the Regulations adapted for Part III.1`, `reg 76.02 the Act and these Regulations are adapted for Part III.1 in respect of` | A reading rule: the Act and Regulations are adapted 'as provided in this Part'. Encoded as the list of provisions the Part adapts (Act ss 58, 8(5), 10(12), 10(13), 12; reg 40(6)(b)), each cited where the adaptation is encoded; any other provision: NOTHING. |
| heading "DIVISION 2 Premium Reduction System" | src:1185 | inert | - | A Division heading; it carries no text of its own. |
| heading "Standards" (line 1187) | src:1187 | inert | - | A heading; it carries no text of its own (reg 76.03 follows). |
| reg 76.03 | src:1188-1194 | fork | er4-part3-1-premium-reduction.l4: `reg 76.03 the provincial plan meets the requirements from the day it takes effect` | F15: 'substantially the same persons' and 'substantially equivalent to or greater than' are judgments left to others: BOOLEAN inputs. The requirements bind the province's plan from the day it takes effect (a date test). |
| heading "Premium Reduction" (line 1196) | src:1196 | inert | - | A heading; it carries no text of its own (regs 76.04 to 76.08 follow). |
| reg 76.04 | src:1197 | encoded | er4-part3-1-premium-reduction.l4: `reg 76.04 the employee's and employer's premiums payable under sections 67 and 68 of the Act are to be reduced` | Premiums are reduced if provincial benefits would reduce or eliminate benefits under ss 22 and 23 (the effect is a BOOLEAN fact, Act s 69(2), out of range, piece ei3). The person's premium is affected. |
| reg 76.041 | src:1198 | repealed or blank in this text | - | [Repealed, SOR/2010-301, s. 2] |
| reg 76.05 | src:1199 | fork | er4-part3-1-premium-reduction.l4: `reg 76.05 the premium reduction obtained by applying the premium reduction rate` | F16: the reduction is rate times the amount the premium rate is applied to; how that applies to the employer's premium (1.4 times the employees', Act s 68, out of range) is not worked out by the text, so the base is an input. |
| reg 76.06(1) | src:1200-1206 | fork | er4-part3-1-premium-reduction.l4: `er4 Estimates for one group of persons`, `reg 76.06(1) the sum of the estimated insurable earnings multiplied by 2.4 and the estimated self-employed earnings`, `reg 76.06(1)(a)(i) and (b)(i) the result obtained by dividing the estimated benefits by the divisor`, `reg 76.06(1)(a)(ii) and (b)(ii) the result obtained by dividing the estimated variable administrative costs by the divisor`, `reg 76.06(1)(a) and (b) the rate determined by adding the two results`, `reg 76.06(1) the rate rounded to the nearest one hundredth of one per cent, as section 66.4 of the Act directs`, `reg 76.06(1) the premium reduction rate for a year` | F17: 2.4 multiplies the insurable earnings alone. (a) the rate for persons NOT covered minus (b) the rate for those covered, rounded as Act s 66.4 (out of range, piece ei3) directs; the rounding is restated here under a local name. A divisor not above zero: NOTHING. |
| reg 76.06(2) | src:1207 | encoded | er4-part3-1-premium-reduction.l4: `reg 76.06(2) actuarial estimates are used to determine the estimated amounts` | A condition on the estimates: they must be actuarial (BOOLEAN input); `reg 76.06 the premium reduction rate determined as the regulation requires` returns NOTHING without it. |
| reg 76.06(3) | src:1208 | encoded | er4-part3-1-premium-reduction.l4: `reg 76.06(3) the results are determined having regard to the same factors as those set out in section 66 of the Act` | A condition on the results (Act s 66, out of range, piece ei3): BOOLEAN input; `reg 76.06 the premium reduction rate determined as the regulation requires` returns NOTHING without it. |
| reg 76.07 | src:1209 | inert | - | A duty of the Commission to publish the premium reduction rate in Part 1 of the Canada Gazette as soon as feasible after it is determined: machinery of publication. The rate itself is reg 76.06; publication gives or takes nothing from the person and sets no figure. |
| reg 76.08 | src:1210 | inert | - | The reimbursement amount that the Province of Quebec pays under section 4.5 of the Entente finale Canada-Quebec sur le regime quebecois d'assurance parentale (signed on March 1, 2005) is to be paid to the Receiver General and into the Consolidated Revenue Fund as if it were an amount under Act s 72: government-to-government accounting (machinery). It states no right, duty or fact of a person who lost work. The signing date of the Entente is not an enactment or commencement date of this text. |
| heading "DIVISION 3 Entitlement" | src:1212 | inert | - | A Division heading; it carries no text of its own. |
| heading "Disentitlement" (line 1214) | src:1214 | inert | - | A heading; it carries no text of its own (reg 76.09 follows). |
| reg 76.09(1) | src:1215 | fork | er4-part3-1-entitlement.l4: `reg 76.09(1) the claimant is disentitled to be paid benefits under section 22 or 23 of the Act` | F18: whole claim, not week by week: (1) does not speak of a week, unlike (3). The claimant's bar on maternity and parental benefits if entitled to provincial benefits, unless (2). Seat question. |
| reg 76.09(2) | src:1216 | encoded | er4-part3-1-entitlement.l4: `reg 76.09(2) subsection (1) does not apply` | The claimant's power to ask the Commission to determine that the provincial amount is not substantially equivalent or greater; the Commission's determination is a BOOLEAN input (a judgment the text hands to the Commission). Both the request and the finding are needed. |
| reg 76.09(3) | src:1217-1219 | encoded | er4-part3-1-entitlement.l4: `er4 Benefits claimed by a claimant with provincial benefits`, `reg 76.09(3) the claimant is disentitled to be paid those benefits in respect of the same week` | Week by week for other Part I benefits and the Fishing Regulations; ss 22 and 23 are outside (3) and governed by (1); a benefit of another kind: NOTHING. |
| reg 76.09(4) | src:1220 | encoded | er4-part3-1-entitlement.l4: `reg 76.09(4) subsections (1) to (3) apply to the claimant whether or not they have ceased to reside in the province where the plan was established` | For greater certainty: moving province after applying makes no difference, so residence is not an input. |
| reg 76.09(5) | src:1221-1223 | fork | er4-part3-1-entitlement.l4: `reg 76.09(5)(a) subsections (1) to (3) apply in respect of the other person`, `reg 76.09(5)(b) subsections 76.36(1) to (3) apply in respect of the other person` | F19: 'apply in respect of the other person' read as bringing the other caregiver under the same bars as the claimant under (4). (b) reaches a self-employed person through reg 76.36 (Part III.2, this piece). |
| reg 76.1 | src:1224 | repealed or blank in this text | - | [Repealed, SOR/2016-206, s. 3] |
| heading "Insured Participant — Part II of the Act" | src:1226 | inert | - | A heading; it carries no text of its own (regs 76.11 and 76.12 follow). |
| reg 76.11 | src:1227 | encoded | er4-part3-1-entitlement.l4: `reg 76.11 the person is an insured participant, as the definition in section 58 of the Act is adapted` | Adds to Act s 58 'insured participant' (out of range, piece ei2) an insured person who requests employment benefits assistance while unemployed with a provincial benefit period current or ended within the previous 60 months and who would have had special benefits. Seat question. |
| reg 76.12 | src:1228 | repealed or blank in this text | - | [Repealed, SOR/2016-206, s. 5] |
| heading "Week Not Counted to Extend Qualifying Period" | src:1230 | inert | - | A heading; it carries no text of its own (reg 76.13 follows). |
| reg 76.13 | src:1231 | encoded | er4-part3-1-entitlement.l4: `reg 76.13 the week is a week during which the person was in receipt of benefits, for subsection 8(5) of the Act` | A week of provincial benefits (this Part or Part III.2) counts as a week in receipt of benefits for Act s 8(5) (out of range, piece ei1). |
| heading "Extension of the Benefit Period" | src:1233 | inert | - | A heading; it carries no text of its own (regs 76.14 and 76.15 follow). |
| reg 76.14 | src:1234-1236 | encoded | er4-part3-1-entitlement.l4: `reg 76.14(a) the benefits count as benefits paid for one of the reasons mentioned in paragraphs 12(3)(a) and (b) of the Act`, `reg 76.14(b) the number of weeks up to which the benefit period is extended so that those benefits may be paid` | (a) provincial benefits for the same reasons count; (b) the extension runs up to the applicable maximum for the reason in paragraphs 12(3)(c) to (f). Both maxima are inputs (Act ss 10(13) and 12(3), out of range, piece ei1). |
| reg 76.15 | src:1237 | encoded | er4-part3-1-entitlement.l4: `reg 76.15 the number of weeks by which the benefit period is considered to be extended under subsection 10(12) of the Act` | The weeks the child or children are hospitalized extend the benefit period, for a claimant who has received or is entitled to provincial benefits; otherwise NOTHING. |
| heading "Reduction of Benefits" (line 1239) | src:1239 | inert | - | A heading; it carries no text of its own (regs 76.16 and 76.17 follow). |
| reg 76.16 | src:1240 | encoded | er4-part3-1-entitlement.l4: `reg 76.16 the benefits payable under section 22 or 23 of the Act for the week are to be reduced` | A week in which the claimant has received or is entitled to provincial benefits is reduced as 76.17 says. |
| reg 76.17 | src:1241 | encoded | er4-part3-1-entitlement.l4: `reg 76.17 the benefits payable under section 22 or 23 of the Act for the week after the provincial benefits are deducted` | The provincial amount for the same week is deducted, in addition to the deductions of Act ss 19, 22(5), 23(3.5) (out of range, piece ei1). A deduction larger than what is left: NOTHING (the text does not answer). |
| heading "No Double Counting of Weeks" (line 1243) | src:1243 | inert | - | A heading; it carries no text of its own (reg 76.18 follows). |
| reg 76.18 | src:1244 | fork | er4-part3-1-entitlement.l4: `reg 76.18 a week of benefits paid under section 22 or 23 of the Act may be taken into account for that same purpose` | F23: 'that same purpose': a BOOLEAN the person states (a week of provincial benefits has already been taken into account for the purpose of any of 76.11 to 76.14 or 76.19). |
| heading "Payment of Benefits" (line 1246) | src:1246 | inert | - | A heading; it carries no text of its own (regs 76.19 and 76.2 follow). |
| reg 76.19(1) | src:1247-1249 | encoded | er4-part3-1-weeks.l4: `reg 76.19(1) the provincial benefits paid for the week are considered to be benefits paid in respect of a week under the Act`, `reg 76.19(1)(a) the weeks counted toward the overall maximum number of weeks under paragraphs 12(3)(a) and (b) of the Act taken together`, `reg 76.19(1)(a) the weeks left within the overall maximum`, `reg 76.19(1)(b) the weeks counted toward the maximum number of weeks under subsection 12(4) of the Act`, `reg 76.19(1)(b) the weeks left within the maximum under subsection 12(4)` | Weeks of provincial benefits count as weeks under the Act and use up the maxima of Act s 12 (inputs, piece ei1). More weeks counted than the maximum: NOTHING. |
| reg 76.19(1.1) | src:1250 | encoded | er4-part3-1-weeks.l4: `reg 76.19(1.1) a benefit period is deemed to be established`, `reg 76.19(1.1) the week in which the benefit period is deemed to have begun` | F21: a provincial benefit period is deemed established; deemed to have begun the same week only if the claimant would have been entitled to the corresponding benefits. |
| reg 76.19(2) | src:1251 | encoded | er4-part3-1-weeks.l4: `reg 76.19(2) the number of weeks of benefits that the weeks of provincial benefits represent under the Act, before rounding`, `reg 76.19(2) and (3) the weeks of provincial benefits as weeks under the Act` | Accelerated rate: weeks paid times (maximum weeks at the non-accelerated rate over maximum weeks at the accelerated rate); an accelerated maximum not above zero: NOTHING. |
| reg 76.19(3) | src:1252 | encoded | er4-part3-1-weeks.l4: `reg 76.19(3) the number of weeks rounded to the nearest multiple of one week, the higher multiple when equidistant` | Rounds half up (7.5 to 8 asserted); a local rule named for this regulation, not the keel's dollar rounding. |
| reg 76.2 | src:1253 | encoded | er4-part3-1-weeks.l4: `reg 76.2 the weeks of provincial benefits that are taken into account in determining the maximum number of weeks` | Weeks of provincial benefits beyond the Act's maximum for the reason are not taken into account. |
| heading "Persons Making Claims Under Different Regimes" (line 1255) | src:1255 | inert | - | A heading; it carries no text of its own (reg 76.21 follows). |
| reg 76.21(1) | src:1256 | encoded | er4-part3-1-weeks.l4: `reg 76.21(1) subsection (2) applies in respect of the two persons` | Two persons caring for the same child who do not live in the same province when the first applies. |
| reg 76.21(2) | src:1257-1261 | encoded | er4-part3-1-weeks.l4: `reg 76.21(2) the number of weeks of benefits payable to the claimant, subject to subsection (3)` | Half of an even number; for an odd number, 1 + half the rest if the claimant applied first, half the rest if the provincial applicant did; an agreement or court order: NOTHING (the number is theirs). Seat question. |
| reg 76.21(3) | src:1262-1270 | encoded | er4-part3-1-weeks.l4: `reg 76.21(3)(a) the most weeks payable to a claimant who elected the 35-week maximum`, `reg 76.21(3)(b) the most weeks payable to a claimant who elected the 61-week maximum`, `reg 76.21(3) the most weeks that may be paid to the claimant` | A and B: A - B; formula (A - B) x C/D rounded down. Inputs A, B, C, D from Act s 12 (piece ei1). |
| reg 76.21(4) | src:1271 | fork | er4-part3-1-weeks.l4: `reg 76.21(4) the maximum number of weeks for which benefits may be paid to the claimant in accordance with the election`, `reg 76.21 the number of weeks of benefits payable to the claimant` | F20: (4) read as a ceiling: the weeks payable are the least of the share under (2), the cap of (3) and the elected maximum of (4). |
| heading "Waiving of the Waiting Period" (line 1273) | src:1273 | inert | - | A heading; it carries no text of its own (reg 76.22 follows). |
| reg 76.22 | src:1274 | encoded | er4-part3-1-entitlement.l4: `reg 76.22 the condition of paragraph 40(6)(b), as adapted, is met` | The words added to paragraph 40(6)(b) (out of range, piece er3): sick leave pay was payable or provincial benefits were paid. Only the adapted condition is encoded here. |
| heading "Coming Into Force of Provincial Plan — Transition" | src:1276 | inert | - | A heading; it carries no text of its own (reg 76.23 follows). |
| reg 76.23 | src:1277-1279 | encoded | er4-part3-1-entitlement.l4: `reg 76.23(a) the Act applies in respect of a claim for benefits made in respect of the birth or placement`, `reg 76.23(b) the Act continues to apply in respect of any claim relating to the birth or placement`, `reg 76.23 the Act applies to the claim as it did before this Part` | Transition for births or placements before, or benefits paid before, the day this Part comes into force; that day is not in the text in this range, so it is an input. |
| heading "DIVISION 4 Premium And Adjustment Payments — Provincial Plans" | src:1281 | inert | - | A Division heading; it carries no text of its own. |
| heading "Premium for Insured Person Covered in a Province by a Provincial Plan but Working in Another Province or Working Outside Canada" | src:1283 | inert | - | A heading; it carries no text of its own (reg 76.24 follows). |
| reg 76.24 | src:1284-1286 | encoded | er4-part3-1-premiums-and-administration.l4: `er4 Where the insured person is employed`, `reg 76.24 the employer is not to take any premium reduction into account in deducting the employee's premium or remitting the employer's premium` | A person covered by a provincial plan but employed in a province with none, or outside Canada, has no reduction taken into account at source (full premium deducted and remitted; Act s 82(1), out of range, piece ei3). The person's liability; the employer's duty. Seat question. |
| heading "Premium for Insured Person Working in a Province that Has a Provincial Plan but Not Covered by that Plan" | src:1288 | inert | - | A heading; it carries no text of its own (reg 76.25 follows). |
| reg 76.25 | src:1289-1293 | encoded | er4-part3-1-premiums-and-administration.l4: `reg 76.25 the employer is to take any premium reduction into account in deducting the employee's premium and remitting the employer's premium` | A person employed in a province with a provincial plan but not covered by it has the reduction taken into account at source. Seat question. |
| reg 76.26(1) | src:1294-1300 | encoded | er4-part3-1-premiums-and-administration.l4: `er4 Insured person referred to in section 76.24`, `reg 76.26(1)(a) the lesser of the total of the premium reduction deducted and the overpayment, and what the person owes under the provincial plan`, `reg 76.26(1)(a) the amount obtained by adding together the amounts for the insured persons who reside in the province on December 31`, `reg 76.26(1)(b) the total of the premium reduction remitted by employers as employer's premiums for the insured persons who reside in the province on December 31`, `reg 76.26(1) the premium adjustment that the Minister of National Revenue is to pay to the province` | The Minister of National Revenue pays the province a premium adjustment: (a) per person the lesser of the premium reduction deducted from them plus their overpayment, and what they owe under the provincial plan, for persons resident in the province on 31 December; plus (b) the employer-premium reduction remitted for those persons. Seat question for the person's own share. |
| reg 76.26(2) | src:1301 | inert | - | The payment may be made by the Commissioner of Revenue: says which official may make a payment between governments (machinery). It states nothing the person is owed or must do. |
| heading "Premium Adjustment — Credits and Debits" | src:1303 | inert | - | A heading; it carries no text of its own (reg 76.27 follows). |
| reg 76.27(1) | src:1304-1306 | inert | - | Government accounting: an amount a province pays the Receiver General on account of a premium adjustment is treated as a premium under Act s 72(a), paid into the Consolidated Revenue Fund and credited to the Employment Insurance Operating Account (Act s 73(a)). Machinery of the accounts; no right, duty or fact of a person who lost work. |
| reg 76.27(2) | src:1307 | inert | - | Government accounting: an amount paid to a province under reg 76.26 is paid out of the Consolidated Revenue Fund and charged to the Employment Insurance Operating Account as if required by Act s 77(1). Machinery of the accounts; no right, duty or fact of a person who lost work. |
| heading "Overpayment and Refund of Employee’s Premiums" | src:1309 | inert | - | A heading; it carries no text of its own (reg 76.28 follows). |
| reg 76.28(1) | src:1310 | encoded | er4-part3-1-premiums-and-administration.l4: `reg 76.28(1) the employee's premiums taken into account in determining whether there has been an overpayment` | The province's premium adjustment for premiums deducted under its plan is counted as if paid on account of the employee's premiums under the Act when deciding whether the employee overpaid (Act Part IV, out of range, piece ei3); the rule gives the amount counted, not the overpayment itself. Seat question. |
| reg 76.28(2) | src:1311 | encoded | er4-part3-1-premiums-and-administration.l4: `reg 76.28(2) the amount is taken into account for the purposes of Part IV of the Act` | A premium adjustment paid or to be paid to a province under 76.26(1) is not taken into account for Part IV of the Act. |
| heading "DIVISION 5 Administrative Matters" | src:1313 | inert | - | A Division heading; it carries no text of its own. |
| heading "Social Insurance Number" | src:1315 | inert | - | A heading; it carries no text of its own (reg 76.29 follows). |
| reg 76.29 | src:1316 | encoded | er4-part3-1-premiums-and-administration.l4: `reg 76.29 the claimant's social insurance number is to be used` | The claimant's SIN is used to exchange information between Canada and a province: what may be done with the claimant's number (their liability; no right to withhold it for that purpose). |
| heading "Disclosure of Information" | src:1318 | inert | - | A heading; it carries no text of its own (reg 76.3 follows). |
| reg 76.3 | src:1319 | encoded | er4-part3-1-premiums-and-administration.l4: `reg 76.3 the Canada Revenue Agency and the Minister of National Revenue are authorized to disclose the information to the province` | The Agency and the Minister may disclose to a province with a plan the information necessary to administer this Part, obtained under the Act or Regulations, and information prepared from it: what may be done with the person's information. |
| heading "PART III.2 Reduction of Premium for Self-Employed Persons Covered by a Plan Established Under a Provincial Law" | src:1321 | inert | - | A Part heading; it carries no text of its own. |
| heading "Interpretation" (line 1323) | src:1323 | inert | - | A heading; it carries no text of its own (reg 76.31 follows). |
| reg 76.31 | src:1324-1326 | encoded | er4-part3-2-self-employed.l4: `reg 76.31 plan established under a provincial law`, `reg 76.31 provincial benefits of a self-employed person` | Two definitions, close to but not the same as reg 76.01's (premium under Act s 152.21; benefits under ss 152.04 and 152.05). |
| heading "Standards" (line 1328) | src:1328 | inert | - | A heading; it carries no text of its own (reg 76.32 follows). |
| reg 76.32 | src:1329-1334 | fork | er4-part3-2-self-employed.l4: `reg 76.32 the plan established under a provincial law meets the requirements` | F15: 'substantially the same persons' and 'substantially equivalent to or greater than' are BOOLEAN judgment inputs. Five requirements; no 'from the day it takes effect' as in reg 76.03. |
| heading "Premium Reduction" (line 1336) | src:1336 | inert | - | A heading; it carries no text of its own (regs 76.33 to 76.35 follow). |
| reg 76.33 | src:1337 | encoded | er4-part3-2-self-employed.l4: `reg 76.33 the self-employment premium payable under section 152.21 of the Act is to be reduced` | The self-employment premium is reduced if provincial benefits would reduce or eliminate benefits under ss 152.04 and 152.05. |
| reg 76.34 | src:1338 | fork | er4-part3-2-self-employed.l4: `reg 76.34 the premium reduction to be applied to the self-employment premium` | F16: the rate of reg 76.06 times the amount the premium rate is applied to (input). |
| reg 76.35 | src:1339 | inert | - | A duty of the Commission to publish the premium reduction rate of the self-employment premium in Part 1 of the Canada Gazette as soon as feasible after it is determined: machinery of publication, as reg 76.07. The rate is reg 76.06's. |
| heading "Disentitlement" (line 1341) | src:1341 | inert | - | A heading; it carries no text of its own (reg 76.36 follows). |
| reg 76.36(1) | src:1342 | fork | er4-part3-2-self-employed.l4: `reg 76.36(1) the self-employed person is disentitled to be paid benefits under section 152.04 or 152.05 of the Act` | F18: whole claim, as reg 76.09(1). The self-employed person's bar if entitled to provincial benefits, unless (2). Seat question. |
| reg 76.36(2) | src:1343 | encoded | er4-part3-2-self-employed.l4: `reg 76.36(2) subsection (1) does not apply` | As reg 76.09(2): the self-employed person's request and the Commission's finding (BOOLEAN inputs). |
| reg 76.36(3) | src:1344 | encoded | er4-part3-2-self-employed.l4: `er4 Benefits claimed by a self-employed person with provincial benefits`, `reg 76.36(3) the self-employed person is disentitled to be paid those benefits in respect of the same week` | Week by week for other benefits under Part VII.1; ss 152.04 and 152.05 are governed by (1); benefits of another kind: NOTHING. |
| reg 76.36(4) | src:1345 | encoded | er4-part3-2-self-employed.l4: `reg 76.36(4) subsections (1) to (3) apply to the self-employed person whether or not they have ceased to reside in the province providing those benefits` | As reg 76.09(4): moving province after applying makes no difference. |
| reg 76.36(5) | src:1346-1348 | fork | er4-part3-2-self-employed.l4: `reg 76.36(5)(a) subsections (1) to (3) apply in respect of the other person`, `reg 76.36(5)(b) subsections 76.09(1) to (3) apply in respect of the other person` | F19: as reg 76.09(5); (b) reaches an insured person through reg 76.09. |
| heading "Reduction of Benefits" (line 1350) | src:1350 | inert | - | A heading; it carries no text of its own (regs 76.37 and 76.38 follow). |
| reg 76.37 | src:1351 | encoded | er4-part3-2-self-employed.l4: `reg 76.37 the benefits payable under section 152.04 or 152.05 of the Act for the week are to be reduced` | As reg 76.16. The text says 'the claimant' here although the section is about the self-employed person (reproduced as written). |
| reg 76.38 | src:1352 | encoded | er4-part3-2-self-employed.l4: `reg 76.38 the benefits payable under section 152.04 or 152.05 of the Act for the week after the provincial benefits are deducted` | As reg 76.17, in addition to the deductions of Act ss 152.04(4), 152.05(11), 152.18 (out of range, piece ei5). A deduction larger than what is left: NOTHING. |
| heading "No Double Counting of Weeks" (line 1354) | src:1354 | inert | - | A heading; it carries no text of its own (reg 76.39 follows). |
| reg 76.39 | src:1355 | encoded | er4-part3-2-self-employed.l4: `reg 76.39 benefits paid under section 152.04 or 152.05 of the Act in respect of a week may be taken into account for that same purpose` | A week of provincial benefits already taken into account for reg 76.4 excludes a week under ss 152.04 or 152.05 for that purpose (only reg 76.4 is named, not a list as in reg 76.18). |
| heading "Payment of Benefits" (line 1357) | src:1357 | inert | - | A heading; it carries no text of its own (regs 76.4 and 76.41 follow). |
| reg 76.4(1) | src:1358-1360 | encoded | er4-part3-2-self-employed.l4: `reg 76.4(1) the provincial benefits paid for the week are considered to be benefits paid in respect of a week under the Act`, `reg 76.4(1)(a) the weeks counted toward the overall maximum number of weeks under paragraphs 152.14(1)(a) and (b) of the Act taken together`, `reg 76.4(1)(b) the weeks counted toward the maximum number of weeks under subsection 152.14(2) of the Act`, `reg 76.4(1)(a) the weeks left within the overall maximum`, `reg 76.4(1)(b) the weeks left within the maximum under subsection 152.14(2)` | As reg 76.19(1), with the maxima of Act s 152.14 (inputs, piece ei5); the two `weeks left` rules are the maximum less the weeks counted, and are what seat question 30 calls. |
| reg 76.4(2) | src:1361 | encoded | er4-part3-2-self-employed.l4: `reg 76.4(2) a benefit period is deemed to be established`, `reg 76.4(2) the week in which the benefit period is deemed to have begun` | As reg 76.19(1.1) (F21). |
| reg 76.4(3) | src:1362 | encoded | er4-part3-2-self-employed.l4: `reg 76.4(3) the number of weeks of benefits that the weeks of provincial benefits represent under the Act, before rounding`, `reg 76.4(3) and (4) the weeks of provincial benefits as weeks under the Act` | As reg 76.19(2): calls that rule. |
| reg 76.4(4) | src:1363 | encoded | er4-part3-2-self-employed.l4: `reg 76.4(4) the number of weeks rounded to the nearest multiple of one week, the higher multiple when equidistant` | As reg 76.19(3): calls that rule. |
| reg 76.41 | src:1364 | encoded | er4-part3-2-self-employed.l4: `reg 76.41 the weeks of provincial benefits that are taken into account in determining the maximum number of weeks` | As reg 76.2, with the maxima of Act s 152.14(1)(a) or (b) and (2)(a) or (b): calls that rule. |
| heading "Persons Making Claims Under Different Regimes" (line 1366) | src:1366 | inert | - | A heading; it carries no text of its own (reg 76.42 follows). |
| reg 76.42(1) | src:1367 | encoded | er4-part3-2-self-employed.l4: `reg 76.42(1) subsection (2) applies in respect of the two persons` | As reg 76.21(1), with applications under ss 152.04 or 152.05. |
| reg 76.42(2) | src:1368-1372 | encoded | er4-part3-2-self-employed.l4: `reg 76.42(2) the number of weeks of benefits payable to the self-employed person, subject to subsection (3)` | As reg 76.21(2): calls that rule. Seat question. |
| reg 76.42(3) | src:1373-1381 | encoded | er4-part3-2-self-employed.l4: `reg 76.42(3) the most weeks that may be paid to the self-employed person` | As reg 76.21(3), with A, C, D from Act s 152.14 (inputs, piece ei5): calls that rule. |
| reg 76.42(4) | src:1382 | fork | er4-part3-2-self-employed.l4: `reg 76.42(4) the maximum number of weeks for which benefits may be paid in accordance with the election`, `reg 76.42 the number of weeks of benefits payable to the self-employed person` | F20: as reg 76.21(4). The text says 'a claimant' in (4) of a section about the self-employed person (reproduced as written). |
| heading "Waiving of the Waiting Period" (line 1384) | src:1384 | inert | - | A heading; it carries no text of its own (reg 76.421 follows). |
| reg 76.421 | src:1385 | encoded | er4-part3-2-self-employed.l4: `reg 76.421 the condition of paragraph 40(6)(b), as adapted, is met` | As reg 76.22 (the two regulations carry identical text). |
| heading "Interprovincial Mobility" | src:1387 | inert | - | A heading; it carries no text of its own (reg 76.43 follows). |
| reg 76.43 | src:1388 | encoded | er4-part3-2-self-employed.l4: `reg 76.43 the agreement was entered into within 12 months before the day the self-employed person ceased to reside in the province, or within three months after that day`, `reg 76.43 the self-employed person is deemed to have satisfied the condition set out in paragraph 152.07(1)(a) of the Act` | A self-employed person who left a province with a plan, and made the agreement within 12 months before or three months after, is deemed to have met 152.07(1)(a) (out of range, piece ei5) if covered by the plan during the 12 months before leaving. Seat question. |
| heading "Administration" | src:1390 | inert | - | A heading; it carries no text of its own (regs 76.44 and 76.45 follow). |
| reg 76.44 | src:1391 | encoded | er4-part3-2-self-employed.l4: `reg 76.44 the self-employed person's social insurance number is to be used` | As reg 76.29. |
| reg 76.45 | src:1392 | encoded | er4-part3-2-self-employed.l4: `reg 76.45 the Canada Revenue Agency and the Minister of National Revenue are authorized to disclose the information to the province` | As reg 76.3. |

## Fork register

Every entry is assumed, not ruled: the reading was chosen so that work could go on, and each can be reversed in the one place named.
"No ambiguities found" is not claimed anywhere: where nothing was found the entry says where it was looked for (the last paragraph).

| id | provision | what the text leaves open | how it is encoded | what would settle it |
| --- | --- | --- | --- | --- |
| F1 | reg 58(c)(ii), (iv) (src:999, 1001) | "where appropriate", "when necessary" and "in accordance with local community-based service and client targeting strategies" do not say whose judgment; "worker" is not defined | each is a BOOLEAN input named for the judgment of the service, never guessed; "worker" is `the person is a worker` | a definition of "worker", or a ruling that the judgment is the Commission's |
| F2 | reg 58 lead-in (src:994) | whether the purpose ("persons who need assistance in competing in the labour market") limits the help in (c) | it does not: a purpose is not a condition, and reg 59 opens the service to all workers | the French text or a ruling |
| F3 | reg 60 (src:1013) | whether "includes" makes the four named kinds plans whatever else is true | they are plans; any other plan must be a wage-loss plan covering insured persons employed by an employer | the Act s 69(1) and the practice of the Commission |
| F4 | reg 62(1) (src:1019-1022) | "the percentage by which (a) is less than (b)": relative shortfall or difference in percentage points | the relative shortfall, (b - a) / b, so 0.8% against 1.0% is a reduction of 20% of the rate; (a) not below (b) gives 0 | the Commission's published method; the text alone does not say |
| F5 | regs 63(a), 63(e), 64(c) (src:1040-1042, 1048-1050, 1077) | "not more than three months", "after three months", "after one month": the longest wait the plan may impose, or the exact wait | the longest wait: a plan with a shorter wait also meets it | a ruling |
| F6 | regs 63(a), 63(e) (src:1040-1042, 1048-1050) | whether the hour-bank limb is an alternative to the month limb or replaces it for a plan "based on an hour-bank principle" | it replaces it; one NUMBER for months-or-hours follows the hour-bank flag | a ruling; the other reading is `OR` and would change `reg 63(a) the person becomes eligible ...` and the two (e) rules only |
| F7 | regs 63(f), 64(d), 65(f), 66(e) (src:1051-1055, 1078-1082, 1092-1097, 1103-1108) | "payable until the earliest of": whether the plan may stop only at those events or may also pay longer | the plan pays for at least the stated period and may stop only at the named events; any other stopping event fails | a ruling |
| F8 | regs 65(c), 66(a), 66(c) (src:1086-1089, 1099, 1101) | "requirements" includes a paragraph that only says what a plan "may" do; "except 65(b), 65(c)(i), (e), (f)" then leaves 65(c)(ii), (iii) | 65(c) and 66(c) are permissions and add no test; 66(a) leaves 65(a) and 65(d) as the tests | a ruling |
| F9 | regs 65(b), 66(b) (src:1085, 1100) | "one or more days ... of which at least one day per month is available only for": two floors or one | two floors (1 and 1; 5/3 and 5/3), the credit and the reserved days | a ruling |
| F10 | regs 65(c)(i), 66(c) (src:1087, 1101) | "prorated in relation to the total period of active employment in a month": the formula | credit for a full month times (active employment in the month / active employment in a full month); a full month of nothing gives NOTHING | the plan's rules; the text gives no formula |
| F11 | reg 67(1) (src:1109-1116) | "including one or a combination of any of the following": open or closed list | open: another formal written commitment counts; a board of directors' resolution only "that has been implemented" | a ruling |
| F12 | reg 67(5) (src:1122-1124) | "a number of days ... equal to": exact or at least | exact: a credit above 72 (or 120) minus the maximum days accumulable does not meet it | a ruling |
| F13 | reg 67(2) (src:1117) | "subject to section 71": how the effective date and the months a plan qualifies combine | no month before the effective date of the reduction counts, and none before the plan is considered to have become a qualifying plan | a ruling |
| F14 | regs 69(2), 69(3) (src:1138-1143) | "immediately" has no number of days | a BOOLEAN input for whether it was done immediately | the Commission's practice |
| F15 | regs 76.03(b), (c), 76.32(b), (c) (src:1190-1191, 1331-1332) | "substantially the same persons", "substantially equivalent to or greater than" are judgments left to others | BOOLEAN inputs named for the judgment | the Commission's or the Minister's finding |
| F16 | regs 76.05, 76.34 (src:1199, 1338) | how "applying the premium reduction rate" works on the employer's premium, which Act s 68 makes 1.4 times the employees' | reduction = rate x the amount the premium rate is applied to; that amount is an input | the Act s 66 to 68 and the Commission's published rates |
| F17 | reg 76.06(1) (src:1200-1206) | whether "multiplied by 2.4" applies to the insurable earnings alone or to the sum with the self-employed earnings | to the insurable earnings alone | the Commission's published method |
| F18 | regs 76.09(1), 76.36(1) (src:1215, 1342) | (1) says "disentitled to be paid benefits" if "entitled to receive provincial benefits", with no week; (3) is week by week | (1) bars the whole claim for ss 22 and 23 (152.04 and 152.05), (3) the same week of other benefits; the two do not overlap because (3) excludes ss 22 and 23 | a ruling |
| F19 | regs 76.09(5), 76.36(5) (src:1221-1223, 1346-1348) | "subsections (1) to (3) apply in respect of the other person": whose entitlement to provincial benefits is tested | the other person is treated as entitled, the first person's entitlement being attributed; "a claimant referred to in subsection (4)" is read as someone who has applied for and is entitled to provincial benefits | a ruling |
| F20 | regs 76.21(4), 76.42(4) (src:1271, 1382) | "the maximum number of weeks ... under subsection (3) is the maximum ... established under 12(3)(b)(i) or (ii)": what (4) adds | a ceiling: weeks payable = the least of the (2) share, the (3) cap and the elected maximum; an agreement or court order gives NOTHING | a ruling |
| F21 | regs 76.19(1.1), 76.4(2) (src:1250, 1361) | whether "if the claimant would have been entitled to the corresponding types of benefits" qualifies the first limb ("deemed to be established") or only the second ("deemed to have begun the same week") | only the second | a ruling |
| F22 | regs 65(d), 62(2)(c) (src:1090, 1026) | whether deferral of eligibility may be longer for a person who is not temporary or probationary | the cap of 12 months is tested on any deferral the plan has; no deferral is 0 months | a ruling |
| F23 | reg 76.18 (src:1244) | whether one counted week of provincial benefits bars one week of benefits under s 22 or 23 for "that same purpose", or every such week | the rule answers for the week asked about: it takes a BOOLEAN, whether a week of provincial benefits has been taken into account for that purpose, and says the week of EI benefits may not then be counted | a ruling |
| F24 | the seat, questions 22 and 38 | not a reading of the text: how the seat composes rules (see Seat, "Assumed, not ruled") | as in Seat | the owner's choice |

Where I looked and found nothing further: regs 59, 61, 70, 73, 74, 75, 76 (single clear conditions and counted limits); reg 69(1) (the five categories read as written; (c) and (d) except "the insured persons referred to in paragraph 65(d)" by cross-reference); reg 71 (the two cases and the continuation; its "15th day" is the same cut as reg 67(4)'s but dates a different thing); regs 76.13 to 76.17 and 76.22 to 76.30 (adaptations and definitions); the Part III.2 mirrors 76.39 to 76.45 (which differ from Part III.1 only in the Act sections they name, and in two places where the text says "claimant" in a Part about the self-employed person: 76.37 and 76.42(4); reg 76.421 also says "claimant", but it quotes the words of paragraph 40(6)(b)).

## Cross-references out of my ranges

Each row is a provision of this piece that depends on a provision outside lines 993 to 1393.
The input named is the plain-typed `GIVEN` the rule takes in its place (a comment `-- out of range: ...` stands at each).
"The Act" is S.C. 1996, c. 23; the pieces are read from the brief's table (Act: ei1 133-669, ei2 670-1126, ei3 1127-1803, ei5 2109-2688; Regulations: er3 540-992), checked against `SECTION-INDEX.txt`.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| reg 61, reg 68(1)(c) | Act s 69(1)(b): the five-twelfths share | ei3 | none: the 5/12 is the Regulations' own figure; `the reduction of the employer's premium` NUMBER |
| reg 62(1) | Act s 68: the employer's premium rate | ei3 | `the employer's premium rate fixed under section 68 of the Act` NUMBER (a fraction) |
| reg 62(3), (4) | Act s 12 and s 18(1)(b): the cost of benefits for illness, injury or quarantine | ei1 | `the yearly cost of benefits paid in each of the three years` and the Commission's estimates, LISTs of NUMBER |
| regs 63(c)(ii), 63(g)(ii) | reg 35: what counts as earnings | er3 | `er4 plan pays in full whatever benefits are payable from another source that are not earnings under section 35` BOOLEAN; the field of the constructor for 63(g)(ii) |
| reg 63(g)(xiv) | reg 35(2)(d): a motor vehicle accident covered by a provincial plan | er3 | a constructor with no further input |
| reg 63(g)(vii) | Act ss 22, 23, 23.1, 23.2, 23.3 | ei1 | a constructor |
| regs 65(b), (c), (e), 66(b), (d) | Act ss 23(1), 23.1(2): the child and family member concerned | ei1 | the enum `er4 Purpose for which paid sick leave may be used while at home`; the days are NUMBERs |
| reg 67(2) | reg 71 (same piece, same range) | er4 | `the effective date of the reduction under section 71` DATE (the caller passes reg 71's result) |
| regs 68, 72, 73, 75 | Act s 69(4) (late applications) and s 69(5) (reconsideration) | ei3 | a BOOLEAN `the application is one referred to in subsection 69(4) of the Act`; constructors of `er4 Decision the employer may appeal to the Commission` |
| reg 69(2), (3), (4) | the Canada Revenue Agency (an external body) and Act s 82(1) | ei3 | BOOLEANs for what the employer did |
| reg 76.01 "provincial benefits" and "provincial plan" | Act ss 22, 23, 69(2) | ei1, ei3 | BOOLEANs `...agreement ... would have the effect ...` |
| reg 76.01 "variable administrative costs" | Act ss 22, 23, 152.04, 152.05 | ei1, ei5 | the BOOLEAN field `direct cost of providing benefits under section 22, 23, 152.04 or 152.05 of the Act` |
| reg 76.04 | Act ss 67, 68 and 69(2) | ei3 | BOOLEAN `...would have the effect ... of reducing or eliminating them` |
| reg 76.05 | Act s 67 (insurable earnings) and s 68 (1.4 times) | ei3 | `the amount to which the premium rate is applied` NUMBER (fork F16) |
| reg 76.06(1) | Act s 4 (maximum yearly insurable earnings), s 66 (factors), s 66.4 (rounding), s 152.02 (agreements) | keel, ei3, ei5 | the estimates as NUMBERs; the rounding restated locally (Needs from the core); `the results have been determined having regard to the same factors as those set out in section 66 of the Act` BOOLEAN |
| reg 76.09 | Act ss 22, 23, Part I; the Employment Insurance (Fishing) Regulations | ei1; external (in neither input) | constructors of `er4 Benefits claimed by a claimant with provincial benefits` |
| reg 76.11 | Act s 58 (insured participant) | ei2 | `the person is an insured participant under section 58 of the Act` BOOLEAN |
| reg 76.13 | Act s 8(5) (weeks that do not extend the qualifying period) | ei1 | `the person was in receipt of benefits in the week` BOOLEAN |
| reg 76.14 | Act ss 10(13) and 12(3)(a) to (f) | ei1 | `the applicable maximum number of weeks established for that reason` and `that maximum total number of weeks`, NUMBERs; the keel's `Reason for benefits` |
| reg 76.15 | Act ss 10(12) and 23(2) | ei1 | `the number of weeks during which the child or children are hospitalized during the period referred to in subsection 23(2) of the Act` NUMBER |
| reg 76.17 | Act s 19 and ss 22(5), 23(3.5): other deductions | ei1 | `the benefits payable for the week after the deductions referred to in section 19 and subsections 22(5) and 23(3.5) of the Act` NUMBER |
| regs 76.19, 76.2 | Act s 12(3)(a), (b), 12(4) | ei1 | the maxima, NUMBERs |
| reg 76.21 | Act ss 12(3)(b)(i), (ii), 12(4)(b)(i), 23(1.1) | ei1 | A, B, C, D as NUMBERs; the keel's `Election of maximum weeks` |
| regs 76.22, 76.421 | reg 40(6)(b): waiting period | er3 | the two BOOLEANs of the adapted condition |
| reg 76.23 | "the day on which this Part comes into force": not in the text of this range | none | `the day on which this Part comes into force` DATE |
| regs 76.24, 76.25 | Act s 82(1)(a), (b): the deduction and the remittance | ei3 | none: the rule says whether the reduction is taken into account |
| reg 76.26, 76.28 | Act Part IV (overpayment of employee's premiums), s 72(a), 73(a), 77(1) | ei3 | NUMBERs for amounts; ss 72, 73, 77 only in `inert` rows |
| regs 76.31 to 76.45 | Act ss 152.02, 152.04, 152.05, 152.07(1)(a), 152.14, 152.18, 152.21 | ei5 | NUMBERs, BOOLEANs and the keel's `Election of maximum weeks`, as for the Part III.1 rows |
| reg 76.26(2) ("the Commissioner of Revenue") | an office outside both texts | none | none (76.26(2) is `inert`) |

Count: 29 rows. The ones that matter most to a person's answer are the maxima of Act s 12 and s 152.14 (regs 76.14, 76.19, 76.2, 76.21, 76.4, 76.41, 76.42), which the person is asked for as numbers.

## Needs from the core

Nothing in the core is missing for this piece to run; these are the places where a shared rule would replace a local one, for the lead to promote or not.
- **A rounding to the nearest multiple of one unit, higher when equidistant, for a number of weeks.** The keel's `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` is for dollars and cites the Act; reg 76.19(3) (and 76.4(4), which calls it) needs the same arithmetic for weeks. Defined locally as `reg 76.19(3) the number of weeks rounded to the nearest multiple of one week, the higher multiple when equidistant`.
- **The rounding of a premium rate to the nearest one hundredth of one per cent (Act s 66.4).** Reg 76.06(1) says "rounding off the difference in accordance with section 66.4 of the Act". Piece ei3 will encode s 66.4; this piece cannot import it, so it restates the arithmetic as `reg 76.06(1) the rate rounded to the nearest one hundredth of one per cent, as section 66.4 of the Act directs`. After the merge that rule should call ei3's.
- **"The first day of the month following a date"** is `add months (YMD (DATE_YEAR d) (DATE_MONTH d) 1) 1`, written in three places here: the helper `reg 63(a) the first day of the month following`, and inline in `reg 67(4)` and `reg 71`. A core helper for the first day of the month containing a date would shorten all three; none is needed for them to run.
- **The Employment Insurance (Fishing) Regulations** are outside both inputs; reg 76.09(3)(b) names them. The constructor `er4 benefits under the Employment Insurance (Fishing) Regulations` stands for them.
- **`er4 Who made the earlier application`** (nouns) is used by regs 76.21(2) and 76.42(2) only; it needs no promotion.
- **The keel's `Party`, `Period of days`, `Rate band` are not used**: nothing in this range needed them.

## What the text turns out to say

Numbered findings. "Asserted." means a test or a seat case in this folder asserts it (the file is named); a finding without it is a reading of the text no case pins down.

1. **The national employment service is free to every worker, insured or not, claiming or not (reg 59).** Neither whether the worker is insured nor whether they claim benefits is an input of the rule, so the answer cannot depend on either. A user the regulation does not name (not a worker, an employer, a workers' organization or an organization providing employment assistance) gets NOTHING, not FALSE. Asserted (`er4-tests-part2.l4`, `er4-cases-seat.l4`).
2. **The help in reg 58(c) is a claim of "workers" without a test of need, except where the paragraph says "where appropriate" ((ii)), "when necessary" ((iv)), "seeking employment" ((iii)) or "particular difficulty" ((v)).** (c)(i) has no condition at all beyond being a worker. Asserted (`er4-tests-part2.l4`).
3. **Reg 62(1) reduces the employer's premium rate by "the percentage by which" the experience cost ratio is less than the first payer cost ratio.** Read as the relative shortfall, 0.8% against 1.0% is a reduction of 20% of the rate (2.282% becomes 1.8256%); if the first payer cost ratio is not above zero the percentage is not defined. Asserted (`er4-tests-part3-reduction.l4`).
4. **Reg 62(2)(c) takes the reduction away from a person whose eligibility to use paid sick leave is deferred under a plan of reg 65 or 66, even though the plan meets its standards.** Reg 65(d) lets a plan defer that eligibility for a temporary or probationary person for up to 12 months. Asserted (`er4-tests-part3-reduction.l4`, `er4-tests-part3-regs64-66.l4`, `er4-cases-seat.l4`).
5. **The elimination period of reg 63(b) is a standard for the other three plans too:** 64(b) and 65(a) call 63(a), (b), (c), (d) and (g), and 66(a) reaches them through 65(a). A plan can fail 63(e) and 63(f) and still meet 64(b) and 65(a). Asserted (`er4-tests-part3-regs64-66.l4`).
6. **Reg 66(a) is a double indirection:** 66(a) takes section 65 "except 65(b), 65(c)(i), 65(e) and (f)", and 65(a) itself takes section 63 "except 63(e) and (f)". What is left to test is 65(a) and 65(d); 65(c)(ii) and (iii) only say what a plan may do. A cumulative plan that fails 65(b), (e) and (f) passes 66(a). Asserted (`er4-tests-part3-regs64-66.l4`).
7. **Reg 66(b) means exactly 5/3 of a day:** "one and two thirds or more" is met by 5/3 and by 2, not by 1.66. Asserted (`er4-tests-part3-regs64-66.l4`).
8. **Reg 63(g) is a closed list of 17 conditions; several carry a limit of their own** (for instance (ii) amounts that are earnings under s 35, (x) reinstatement of the right to benefits, (xiii) no continuing treatment, (xvi) surgery needed because of illness, (xvii) a reinstatement period of six months at most). A plan with no precluding condition at all meets it. Asserted (`er4-tests-part3-reg63.l4`).
9. **Reg 63(d) is met at exactly 55%:** 550 of 1,000 meets it, 549.99 does not. Asserted (`er4-tests-part3-reg63.l4`).
10. **Reg 67(4) and reg 71 both cut at the 15th day of a month but date different things.** 67(4) dates the day a plan is considered to become or cease to be a qualifying plan (15 March is considered 1 March, 16 March is considered 1 April); 71 dates the effective date of the reduction for an initial application (made 15 March, 1 April; made 16 March, 1 May). Asserted (`er4-tests-part3-reg67.l4`, `er4-tests-part3-application.l4`, `er4-cases-seat.l4`).
11. **Reg 67(5) says "equal to", not "at least":** a plan that credits more than 72 (or 120) minus the days that could have been accumulated does not meet the subsection. Asserted (`er4-tests-part3-reg67.l4`).
12. **Reg 72(3) names paragraph 63(d) alone,** although regs 64, 65 and 66 take 63(d) over; the officer terminates only when the plan has ceased to meet 63(d). Asserted (`er4-tests-part3-application.l4`).
13. **Reg 75's "within one year after the day on which notice ... is sent" is the same date a year later** (29 February 2024 gives 28 February 2025). Asserted (`er4-tests-part3-application.l4`).
14. **Reg 76 (1995 reconsideration) is spent in practice but is still law in this text,** so it is encoded: an application made on 4 December 1994 itself is not "before" it. Asserted (`er4-tests-part3-application.l4`).
15. **A person entitled to provincial benefits is disentitled to maternity and parental benefits for the whole claim (reg 76.09(1)); the week-by-week bar of 76.09(3) covers other Part I benefits and fishing benefits and excludes ss 22 and 23.** Asking the Commission is not enough: the Commission must also find the provincial amount not substantially equivalent (76.09(2)). Moving province after applying changes nothing (76.09(4)), so residence is not an input. Asserted (`er4-tests-part3-1-entitlement.l4`, `er4-cases-seat.l4`).
16. **Reg 76.09(5) and 76.36(5) cross-refer: the other caregiver of a person under 76.09(4) is bound by 76.09(1) to (3) if insured, by 76.36(1) to (3) if self-employed, and the same the other way round.** The seat question has four routes, by who is self-employed. Asserted (`er4-cases-seat.l4`, mirror cases).
17. **Reg 76.17 deducts the provincial amount for the same week, in addition to the deductions of Act s 19 and ss 22(5), 23(3.5);** the text does not say what happens if the deduction is larger than what is left to pay, so the rule answers NOTHING, not zero. Asserted (`er4-tests-part3-1-entitlement.l4`, `er4-cases-seat.l4`).
18. **Reg 76.19(3) rounds a fractional number of weeks half up** (7.5 weeks is 8, 7.49 is 7). Asserted (`er4-tests-part3-1-weeks.l4`, `er4-cases-seat.l4`).
19. **Reg 76.21(2) gives the claimant half of an even number of weeks; of an odd number, one week plus half the rest if the claimant applied first, half of the number less one week if the provincial applicant did.** With an agreement or a court order the subsection gives no number. Reg 76.21(3)(b) uses A, the 12(4)(b)(i) maximum of weeks "when divided", for the 61-week election as well as for the 35-week one; with the stand-in figures A = 40, C = 61, D = 35 and B = 0 the formula gives 69, above the 61-week ceiling of subsection (4), which is why (4) matters (the figures are the tests', not asserted as the Act's). Asserted (`er4-tests-part3-1-weeks.l4`, `er4-cases-seat.l4`).
20. **Reg 76.06(1) is the rate for persons NOT covered by a provincial plan minus the rate for those covered; the 2.4 multiplies the insurable earnings alone; the result is rounded to one hundredth of one per cent.** (0.06 - 0.035 = 0.025; 0.02345 rounds to 0.0235.) Asserted (`er4-tests-part3-1-premium-reduction.l4`).
21. **Regs 76.24, 76.25 and 76.04 together leave one person unanswered:** someone who is neither covered by a provincial plan nor employed in a province that has one. Asserted (`er4-cases-seat.l4`).
22. **Reg 76.26(1)(a) counts a covered person's overpayment of employee's premiums toward what they owe their province** (the lesser of the premium reduction deducted plus the overpayment, and what they owe), for persons resident in the province on 31 December. Asserted (`er4-tests-part3-1-premiums-and-administration.l4`, `er4-cases-seat.l4`).
23. **Reg 76.39 names only reg 76.4,** where its Part III.1 counterpart reg 76.18 names "any of sections 76.11 to 76.14 or 76.19". No case distinguishes them: the seat question takes the same BOOLEAN for both (`er4-cases-seat.l4`).
24. **Reg 76.43's two windows include both ends:** an agreement exactly 12 months before the day the person ceased to reside, or exactly three months after it, is within. Asserted (`er4-tests-part3-2-self-employed.l4`, `er4-cases-seat.l4`).
25. **The text says "claimant" in two places of a Part about the self-employed person:** reg 76.37 ("the claimant has received ...") and reg 76.42(4) ("paid to a claimant"). Reproduced as written; the rules are for the self-employed person.
26. **The lead-in of reg 66 reads "An Enhanced Cumulative Paid Sick Leave shall meet": the word "Plan" is missing;** the rule is named for the plan.
27. **Reg 76.23 depends on a date the text does not give:** "the day on which this Part comes into force". It is an input of the rule and of the seat question; no case asserts a real date. Not asserted as law (the tests use an invented day).

## What the stable binary does not accept

Binary: `l4 1.6.98 (main)` at the path named in the task (sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`). It is the `main` build itself, so `check.sh` ran with `L4_TARGET=unstable` and made no second-binary comparison.

**Measured while writing this piece** (each was met, reproduced and fixed in the file):
- `WHEN `a constructor` WITH x THEN ...` is a parse error: `unexpected WITH`, `expecting (, EXACTLY, FOLLOWED, Float Literal, Numeric Literal, OF, String Literal, THEN, identifier, or space token`. Write the field as a pattern argument: ``WHEN `a constructor` x THEN ...``.
- `max d1 d2` on two DATEs fails with `There are multiple definitions for the identifier max` (the prelude has `max` for NUMBER and for MAYBE NUMBER only). Write `IF d1 AT LEAST d2 THEN d1 ELSE d2`.
- A mixfix head that names a parameter which is not in the `GIVEN` fails with `The names in a type signature must match those in the definition`. Define a rule by its name alone and let the `GIVEN` order give the arguments.
- In a positional `OF`, a bare `LIST x` or a bare `Record OF a, b` swallows the commas after it: `All elements in a LIST literal must have the same type`, or `expects 2 arguments, but you are applying it to 3 arguments`. Parenthesise each: `(LIST x)`, `(Record OF a, b)`.
- The `, item` lines of a `name MEANS LIST a` list must sit to the right of the column where the first item starts: renaming a head longer made the old indentation fail with `incorrect indentation (got 27, should be greater than 31)`, which is a parse error and so turns the whole file red. The fix is to indent the continuation lines under the first item, not to shorten the name.
- `NOT a AND NOT b` reads as `NOT (a AND NOT b)` (the Guide's rule; met once in a draft of the seat's `BRANCH` and fixed with `(NOT a) AND (NOT b)`).

**Not used, so not measured here:** `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, a section `GIVEN`, `TYPICALLY`, sets, the ledger, `EVERY`, `RULES EFFECTIVE DATE`, the temporal built-ins, `@lang`, regulative `MUST` rules.

**Not a rejection, but worth knowing:** `er4-seat.l4` takes about 9 s to type-check and `er4-cases-seat.l4` about 36 s to run (the seat imports twelve modules and the plan-standards question has 26 inputs); a full `check.sh` run takes about two minutes.

## What check.sh prints

Run on 2026-10-24 after the last edit to any `.l4` file, in this folder, as `L4=<stable l4 1.6.98> L4_TARGET=unstable ./check.sh`.
The "main" check was skipped by the script itself, because the only binary is the `main` build.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
er4-cases-seat.l4                              0       156       0        0         0
er4-nouns.l4                                   0         0       0        0         0
er4-part2-national-employment-service.l4       0         0       0        0         0
er4-part3-1-entitlement.l4                     0         0       0        0         0
er4-part3-1-premium-reduction.l4               0         0       0        0         0
er4-part3-1-premiums-and-administration.l4       0         0       0        0         0
er4-part3-1-weeks.l4                           0         0       0        0         0
er4-part3-2-self-employed.l4                   0         0       0        0         0
er4-part3-application.l4                       0         0       0        0         0
er4-part3-qualifying-plan.l4                   0         0       0        0         0
er4-part3-reduction.l4                         0         0       0        0         0
er4-part3-reg63-weekly-indemnity-plan.l4       0         0       0        0         0
er4-part3-regs64-66-other-plans.l4             0         0       0        0         0
er4-seat.l4                                    0         0       0        0         0
er4-tests-part2.l4                             0        31       0        0         0
er4-tests-part3-1-entitlement.l4               0        63       0        0         0
er4-tests-part3-1-premium-reduction.l4         0        50       0        0         0
er4-tests-part3-1-premiums-and-administration.l4       0        25       0        0         0
er4-tests-part3-1-weeks.l4                     0        59       0        0         0
er4-tests-part3-2-self-employed.l4             0        95       0        0         0
er4-tests-part3-application.l4                 0        74       0        0         0
er4-tests-part3-reduction.l4                   0        34       0        0         0
er4-tests-part3-reg63.l4                       0        59       0        0         0
er4-tests-part3-reg67.l4                       0        38       0        0         0
er4-tests-part3-regs64-66.l4                   0        74       0        0         0
TOTAL (29 modules)                             0       758       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
check.sh exit: 0
```

The 758 satisfied assertions are the `#ASSERT` lines written: 602 in the eleven `er4-tests-*.l4` files and 156 in `er4-cases-seat.l4`; none was edited to match a result.
No module has an error, a failed or a refused assertion, and no `l4 check` of any `er4-*.l4` file printed a warning (`follows code on its line`, `end of the file`, unknown annotation).
`python3 -I srcrefs.py check --refs SOR-96-332.txt er4-*.l4` prints `304 src: lines, 138 runs, 213 locators, 0 problems`.

## Before this is worth relying on

- **A person who knows the law reads it against the official text.** Nothing here is checked against the official text, the French text or the Justice Laws Website; the source is a converter's rendering. No domain expert has read any module section by section.
- **The 23 readings F1 to F23 in the Fork register are mine, not rulings (F24 records how the seat composes rules).** The ones that change an answer most are F4 (the percentage of reg 62(1)), F18 and F19 (disentitlement of the whole claim and of the other caregiver), F20 (the ceiling of reg 76.21(4)) and F17 (the 2.4 of reg 76.06(1)).
- **The Act's figures are inputs, not law in this piece.** The maxima of Act ss 12 and 152.14 and the 35, 61, 40 of the weeks formulas are asked of the person; once the other pieces are merged the seat should read them from the Act's rules. The tests use stand-in values.
- **The Employment Insurance (Fishing) Regulations are not among the inputs.** A fisher's claim under them is outside this piece; reg 76.09(3)(b) only names them.
- **Reg 76.23's coming-into-force day is not in the text of this range.** It is an input until it is read from the instrument that brought Part III.1 into force.
- **The judgments the text hands to the Commission or the service** (substantially equivalent, where appropriate, when necessary, immediately) are inputs; a use of the encoding must say who decides them.
- **The rounding of reg 76.06(1) restates Act s 66.4 locally** until ei3's rule can be called; the two must agree.
- **No employer seat exists.** The employer's duties are in layer 1 and are tested, but the form the website builds for this piece asks only the individual's questions.
- **Deployment.** The seat has not been run through Legalese Cloud or the Interact form; question 11 has 26 inputs and several `@desc` texts that paraphrase the text for a lay reader. `check.sh` was run with the stable binary only, so the `main` versus `unstable` comparison was not made (the binary is `main`).
- **`srcrefs.py check --strict`** (not required by the brief) reports 22 informational messages, of two kinds: a run of `src:` quote lines whose `@ref` locators reach fewer lines than the run quotes ("not exact"), and a `@ref` range wider than the quote lines directly above it ("not covered by the quote lines it follows", where one `@ref` spans several quoted paragraphs). `--refs` reports 0 problems.
