# NOTES: piece ei5, Employment Insurance Act Part VII.1 (benefits for self-employed persons)

This folder holds the L4 encoding of **Part VII.1 of the Employment Insurance Act (S.C. 1996, c. 23), sections 152.01 to 152.34**, lines 2109 to 2688 of `S.C.-1996-c.-23.txt`, with the seat layer for the person the Part applies to.
It was written by one agent (piece ei5, Sonnet 5.5) for the stable `l4` 1.6.98, and is meant to be merged by the lead with the pieces for the other parts of the Act and the Regulations.

**The sources.**

Both source files are **plain-text renderings made by a converter script from the Justice Laws XML; they are not the official text, and nothing here has been verified against the official text.**
`../../registers/source-bundle/*.meta.json` records the provenance: the Act is a consolidation current to 2026-09-30 (last amended 2026-06-18) and the Regulations are a consolidation current to 2026-09-30 (last amended 2026-04-01).
The converter drops historical notes and footnotes, so the text carries no enactment or amendment dates; it keeps headings, section labels and marginal notes.

Which instrument each rule comes from:

- **Every rule of layer 1 comes from the Act** (`S.C.-1996-c.-23.txt`, Part VII.1).
- **The Regulations (`SOR-96-332.txt`) are consulted for the figures and conditions the Act leaves to regulations**, and are cited in the cross-reference table, not encoded: the Regulations' own sections belong to pieces er1 to er6.
  Where a regulation settles what the Act leaves open, the outcome enters the rule as a plain input named for the fact (for example "the week is a week of unemployment as defined or determined in accordance with the regulations", for regs 30.1 and 30.2).
  Where the Regulations as deposited say nothing, the rule says so with a not-covered value or an input, and the gap is listed under "What the text turns out to say".
- No figure is invented for a rule.
  The invented figures are in the tests and cases only, and each file says so.

**What is in the folder.**

- Layer 1, the law, one module per natural group of the Part: `ei5-interpretation.l4` (s 152.01), `ei5-agreement.l4` (s 152.02), `ei5-sickness-pregnancy.l4` (ss 152.03 and 152.04, with the reductions shared with ss 152.05, 152.06, 152.061 and 152.062), `ei5-parental.l4` (s 152.05), `ei5-caring.l4` (ss 152.06, 152.061 and 152.062), `ei5-qualifying.l4` (ss 152.07 to 152.09), `ei5-benefit-period.l4` (ss 152.1 to 152.12), `ei5-payment.l4` (ss 152.13 to 152.2), `ei5-premium.l4` (ss 152.21 to 152.3), `ei5-other-provisions.l4` (ss 152.31 to 152.34).
  Each rule has `-- src:N | text` quotation lines copied by script from the Act and an `@ref Employment Insurance Act <label> (src:N-M)`.
  `check.sh` does not run the locator check, so it was run separately: `python3 -I srcrefs.py check --refs S.C.-1996-c.-23.txt ei5-*.l4` (its output is under "What check.sh prints").
  Rule names in layer 1 begin with the section they encode (`s 152.07(1)(a) ...`), and types and constructors begin with `ei5 `, so the names stay specific when all the pieces share one folder.
  No layer-1 module imports another ei5 module: a value that one section takes from another is a plain input of the rule, and the seat layer joins them (the tests, the seat and the cases import the modules they test or call).
- Tests of layer 1, one file per module: `ei5-tests-<module>.l4`, with expected values written by hand from the text beside each assertion.
- Layer 2, the seat: `ei5-seat.l4` (146 exported questions) and `ei5-cases-seat.l4` (at least one asserted case for every question, including cases that return the not-covered value).
- `NOTES.md` (this file) and `PROGRESS.md`.

**Conventions the rules follow.**

- **A judgment the Act hands to someone else is a conditional input**, never decided here: "shows good cause", "in the opinion of the Commission, knowingly failed to declare", "the Minister may reduce or remit".
- **A fact the Act leaves open returns `NOTHING` (or a not-covered constructor), never `FALSE` or `0`.**
  Examples: the class of a violation that was only warned; the day a benefit period ends when no end is given; the maximum weeks for parental benefits when no election was made.
- **Dates are DATE values built with the keel's `YMD`**; weeks are Sunday to Saturday as s 2(1) "week" says; a period of days is the keel's `Period of days` and counts both of its end days.
- **Money is in dollars and the rounding of s 152.01(5) is applied once, to the figure that is paid or deducted** (fork F20).

## Seat

**The seat** is the one the brief fixes: a person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many weeks they need or would get, how much they would receive and for how long, and what they must do or tell the Commission.
In Part VII.1 that person is the **self-employed person** (s 152.01(1)), an individual who has entered into an agreement with the Commission, and who may also owe a premium and a return to the Minister of National Revenue.
(A fisher is dealt with by Part VIII, piece ei4: s 152.01(1) takes a person to whom the Part VIII regulations apply out of the definition, and the seat asks about it as one yes/no input.)

**Why this seat.**
Every provision of the Part that matters to a person decides one of five things for the self-employed person: whether the Part applies to them (ss 152.01, 152.02); what they can claim and for how long (ss 152.03 to 152.14); how much (ss 152.15 to 152.2); what they must pay or file (ss 152.21 to 152.3); and what else applies to or can be done to them (ss 152.31, 152.32).
The Commission and the Minister of National Revenue never get a seat: where a provision addresses them (ss 152.02(3), 152.11(7), 152.12, 152.22(2), 152.24, 152.27, 152.3), the question asks what the person is owed or exposed to, and the official's facts (what they have fixed, sent, served or been asked) are plain inputs.
The person administering the self-employed person's affairs (s 152.22(3)) has no seat of their own either: the question asks whether the person's own return must be filed by them.

**The shape.**
`ei5-seat.l4` has 146 exported questions under ten `§§` headings in the text's order, each with `@export`, a `GIVEN` whose every parameter has an `@desc` worded to the person, and a body that calls a layer-1 rule; none of the 146 states a rule again.
Two small non-exported helpers in the seat (`the section 152.14(1) maximum for each benefit paid` and `the section 152.14(1) maximum for`) only build the list of s 152.14(1) maxima by calling the layer-1 rule of that section.

| group | questions |
| --- | --- |
| Am I within this Part? (ss 152.01 and 152.02) | 10 |
| If I cannot work because of an illness, injury or quarantine (s 152.03) | 3 |
| If I am pregnant (s 152.04) | 5 |
| If I am caring for a new-born or adopted child (s 152.05) | 18 |
| If I am caring for a family member, a critically ill child or a critically ill adult (ss 152.06, 152.061 and 152.062) | 13 |
| Do I qualify for benefits? (ss 152.07 to 152.09) | 18 |
| My benefit period (ss 152.1 to 152.12) | 17 |
| How many weeks, and how much (ss 152.13 to 152.2) | 23 |
| The premium I must pay, and the return I must file (ss 152.21 to 152.3) | 32 |
| Other provisions of the Act that apply to me (ss 152.31 and 152.32) | 7 |

**Conventions of the seat** (also in the header of `ei5-seat.l4`).

- A fact that may be absent is asked as a yes/no and, if yes, a date or a number; the date is ignored when the answer is no.
  The question builds the `MAYBE` the module expects from the pair.
- What the Regulations decide is asked as the fact the person can state or is told, and the `@desc` names the regulation (for example reg 41.2, reg 76.43, reg 30.2).
  Where nothing is prescribed in the Regulations as deposited, the `@desc` says so ("none is prescribed in the Regulations as deposited").
- A judgment left to the Commission or the Minister of National Revenue is asked either as a fact the person can state ("Do you show that there was good cause ...?") or as the official's outcome ("Is it the Commission's opinion that you knowingly failed to declare ...?").
- A question that needs the answer to another says so in its `@desc` and asks for that answer as a plain yes/no, number or date; an exported question never calls another exported question, only layer-1 rules (and the two helpers above).

**What the seat leaves without a question, and why.**

- Headings, the definitions that other questions already use (s 152.01(1) "initial claim for benefits", "qualifying period", "waiting period"), and the rounding rule of s 152.01(5) get no question of their own: each is applied inside the questions that need it.
- ss 152.17(2) and (3), 152.26(5), 152.28(2), 152.311 and 152.33 are `inert` machinery: they decide nothing a person could ask.
- s 152.34 (a review the Minister must cause five years after the Part comes into force) gives the individual nothing to claim and nothing to do, so it has a layer-1 rule and no question.
- The earnings question (s 152.01(2)) takes **one business** (its kind, its income under the Income Tax Act, its income without reference to paragraph 81(1)(a), whether the person is an Indian on a reserve, its gross revenue and the rent in it) and the person's total losses; the layer-1 rule takes a list of businesses.
  A person with several businesses must ask the rule once per business or total the figures of the businesses that count.
- The seat takes the maximum yearly insurable earnings of s 4 and the premium rate of ss 66 and 66.32 as plain inputs, because the Act does not state them and no figure is deposited here.

## Jural relations

One row per provision, or run of provisions that state one relation, in the text's order; a provision that creates no relation (a definition, a counting rule, a limit on the content of another provision's claim, a scope rule) is listed as `none` with what it is.
The columns are the brief's: the holder of the right, privilege, power or immunity; the bearer of the correlative duty, no-right, liability or disability; the relation; and the L4 rule that encodes it.
Each relation is stated once, as a relation between the two parties, in the neutral name of the rule; the seat then asks it from the self-employed person's side.

Two notes on how the text names the parties.

- **The text does not name who pays.** Part VII.1 says benefits are "payable" or that the person "is entitled to receive" them (ss 152.03(1), 152.04(1), 152.05(1), 152.1(1), 152.13).
  The only party it names for the benefits side is the Commission, which decides whether the person is qualified (s 152.12), fixes the agreement's form (s 152.02(3)) and may cancel a benefit period (s 152.11(7)).
  The table therefore names the Commission as the bearer of the duty to pay; that is a reading of the text, not a sentence of it.
- **The premium side names the Minister of National Revenue and the Receiver General.**
  The person must "pay to the Receiver General" (ss 152.25 and 152.26); the return is "filed with the Minister of National Revenue" (s 152.22); the Minister examines, assesses and refunds (ss 152.24 and 152.3).
  The table shows the holder of the claim to the premium as the Crown, collecting through the Minister, because s 152.25 names the Receiver General as the payee and the Minister as the collector.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 152.02(1) | none | none | none: a scope rule (who the Part applies to) | `ei5-agreement`: `s 152.02(1) this Part applies in respect of a person` |
| s 152.02(2) | none | none | none: a counting rule (when the agreement is in force) | `ei5-agreement`: `s 152.02(2) the agreement is in force on a day` |
| s 152.02(3) | the Commission | the self-employed person | power / liability: the Commission fixes the form and conditions of the agreement; the person's agreement must meet them | `ei5-agreement`: `s 152.02(3) the agreement is in the form and on the conditions the Commission has fixed` |
| s 152.02(4), (6), (7) | the self-employed person | the Commission | power / liability: the person may end the agreement by notice, and the Commission is subject to the ending (with the withdrawal and the 60-day cases of (7)) | `ei5-agreement`: `s 152.02(4) the agreement is deemed to be terminated`, `s 152.02(4) the individual may terminate the agreement by notice`, `s 152.02(6) December 31 of the year in which the notice is given`, `s 152.02(6) and (7) what becomes of a notice to terminate the agreement` |
| s 152.02(5) | none | none | none: a counting rule (the day a deemed termination takes effect) | `ei5-agreement`: `s 152.02(5) the day on which an agreement deemed to be terminated is terminated` |
| s 152.03(1), (1.1) | the self-employed person | the Commission | claim / duty: benefits for illness, injury or quarantine | `ei5-sickness-pregnancy`: `s 152.03(1) and (1.1) a self-employed person is entitled to benefits while unable to work` |
| s 152.03(4) | the Commission | the self-employed person | privilege / no-right: the person is not entitled where, but for the illness, they would be deemed not to be working | `ei5-sickness-pregnancy`: `s 152.03(4) a self-employed person is not entitled to benefits under subsection (1)`, `s 152.03 entitled to benefits because of illness, injury or quarantine` |
| ss 152.03(2), (3), 152.04(3), (4), 152.05(11), 152.06(9), 152.061(11), 152.062(9) | the Commission | the self-employed person | privilege / no-right: the Commission need pay only the reduced amount | `ei5-sickness-pregnancy`: `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law`, `ss 152.03(3) and 152.04(4) benefits after the deduction of allowances payable under a plan whose employer's premium has been reduced` |
| s 152.04(1) | the self-employed person | the Commission | claim / duty: pregnancy benefits | `ei5-sickness-pregnancy`: `s 152.04(1) benefits are payable because of pregnancy` |
| s 152.04(2), (3.1), (5), (6) | none | none | none: counting rules (the period, the week before it, its extension) | `ei5-sickness-pregnancy`: `s 152.04(2) the period for which benefits are payable because of pregnancy` |
| s 152.05(1) | the self-employed person | the Commission | claim / duty: parental benefits | `ei5-parental`: `s 152.05(1) benefits are payable for the care of a child` |
| s 152.05(1.1) | the self-employed person | the Commission | power / liability: the person elects the 35-week or the 61-week maximum, and the Commission is bound by the election | `ei5-parental`: `s 152.05(1.1) the claim meets the requirement to elect` |
| s 152.05(1.2) | the Commission | the self-employed person | immunity / disability: once benefits are paid the person cannot revoke the election | `ei5-parental`: `s 152.05(1.2) the election is irrevocable` |
| s 152.05(1.3) | the claimant who claimed first | the other claimant for the same child | power / liability: the first claimant's election binds both | `ei5-parental`: `s 152.05(1.3) the election that binds the person` |
| s 152.05(2) to (7) | none | none | none: counting rules (the period and its extensions) | `ei5-parental`: `s 152.05(2) the period for which parental benefits are payable`, `s 152.05(3) and (4) the period extended because the child or children are hospitalized`, `s 152.05(5) the period is extended so that benefits may be paid up to the applicable maximum`, `s 152.05(5) the number of weeks of benefits that may be paid, up to the applicable maximum, after the extension`, `s 152.05(5.1) the number of weeks by which the period is extended`, `s 152.05(6) the length of the period after an extension under subsection (5)`, `s 152.05(7) the length of the period after an extension under subsections 152.11(11) to (14.1)` |
| s 152.05(12), (13), (13.01) | the two claimants together | the Commission | power / liability: they may divide the weeks within the limits; the Commission pays as divided | `ei5-parental`: `ss 152.05(12) and (13) the maximum number of weeks of benefits that may be divided between two claimants`, `s 152.05(12) the weeks of benefits to be paid to a claimant after the division`, `s 152.05(12), (13) and (13.01) a division of the weeks of benefits is within the limits`, `s 152.05(13.01) the maximum number of weeks for which benefits may be paid to a claimant` |
| s 152.05(14) | the self-employed person | the Commission | power / liability: the person may defer the waiting period on the conditions of (a) to (d) | `ei5-parental`: `s 152.05(14) the waiting period may be deferred` |
| s 152.05(15)(a) | the self-employed person | the Commission | immunity / disability: the person is not required to serve a waiting period another claimant has served or elected to serve | `ei5-parental`: `s 152.05(15)(a) the self-employed person is not required to serve a waiting period`, `s 152.05(15)(b) the person making the claim under section 22 or 23 may have their waiting period deferred in accordance with section 23` |
| s 152.05(15)(b) | the person claiming under s 22 or 23 | the Commission | power / liability: that person may defer their waiting period as s 23 provides | `ei5-parental`: `s 152.05(15)(a) the self-employed person is not required to serve a waiting period`, `s 152.05(15)(b) the person making the claim under section 22 or 23 may have their waiting period deferred in accordance with section 23` |
| s 152.06(1), 152.061(1), 152.062(1) | the self-employed person | the Commission | claim / duty: benefits for caring for a gravely ill family member, a critically ill child or a critically ill adult | `ei5-caring`: `s 152.06(1) benefits are payable for the care or support of a gravely ill family member`, `s 152.061(1) benefits are payable for the care or support of a critically ill child`, `s 152.062(1) benefits are payable for the care or support of a critically ill adult` |
| s 152.06(2), 152.061(2), 152.062(2) | none | none | none: a condition of the claim (which practitioners' certificates count) | `ei5-caring`: `ss 152.06(2), 152.061(2) and 152.062(2) the certificate may be issued by the practitioner` |
| s 152.06(3.1) | the self-employed person | the Commission | privilege / no-right (a dispensation): for the weeks after the first 26 the person need not furnish an additional certificate, and the Commission has no claim to one, except where s 50(8.1) (outside this range) requires it | `ei5-caring`: `s 152.06(3.1) an additional certificate is required for benefits payable after the end of the 26 weeks` |
| s 152.06(3), (4), (5), 152.061(3), (5), 152.062(3), (4) | none | none | none: counting rules (the period of the caring benefits and its start) | `ei5-caring`: `ss 152.06(3), 152.061(3) and 152.062(3) the period for which benefits are payable`, `s 152.06(4)(a) the number of weeks within which the certificate must state a significant risk of death`, `s 152.06(4)(b) the number of weeks that ends the period under subparagraph (3)(b)(iii)`, `ss 152.06(5), 152.061(5) and 152.062(4) subparagraph (3)(a)(ii) does not apply to the claim` |
| s 152.06(6), 152.061(6), 152.062(5) | the self-employed person | the Commission | power / liability: the person may defer the waiting period | `ei5-caring`: `ss 152.06(6), 152.061(6) and 152.062(5) the waiting period may be deferred` |
| s 152.06(7), (8), 152.061(8), (9), 152.062(6), (7) | the two claimants together | the Commission | power / liability: they may divide the remaining weeks within 26, 35 or 15; the Commission pays as divided | `ei5-caring`: `ss 152.06(7) and (8), 152.061(8) and (9) and 152.062(6) and (7) a division of the remaining weeks is within the maximum`, `ss 152.06(7), 152.061(8) and 152.062(6) the weeks of benefits to be paid to a claimant after the division`, `s 152.06(7) and (8) the maximum number of weeks that may be divided` |
| s 152.061(10), (10.1), 152.062(8) | the Commission | the self-employed person | privilege / no-right: no compassionate care benefit for a person already covered, and no adult benefit for the 52 weeks of the child's period | `ei5-caring`: `ss 152.061(10) and 152.062(8) benefits under section 23.1 or 152.06 are not payable in respect of the child or adult on a day`, `s 152.061(10.1) benefits under section 23.3 or 152.062 are not payable on a day` |
| s 152.07(1) | the self-employed person | the Commission | claim / duty: the person who qualifies has the claim of ss 152.03 to 152.062 | `ei5-qualifying`: `s 152.07(1) a self-employed person qualifies for benefits` |
| s 152.07(2) | the Commission | the self-employed person | power / liability: a notice of violation, with a penalty or conviction, makes the person's required earnings higher | `ei5-qualifying`: `s 152.07(2) a self-employed person accumulates a violation` |
| s 152.07(3) to (6) | none | none | none: counting rules (value, class and day of a violation) | `ei5-qualifying`: `s 152.07(3)(b) the weekly rate of benefits multiplied by the average number of weeks, held to the maximum of subsection (4)`, `s 152.07(5) the class of a violation`, `s 152.07(6) the day on which a violation accumulated under section 7.1 is deemed to be accumulated under this section` |
| s 152.07(7) | the self-employed person | the Commission | immunity / disability: a violation counts against at most two initial claims | `ei5-qualifying`: `s 152.07(7) the violation may be taken into account under paragraph (1)(d) in this initial claim` |
| s 152.08(1) | none | none | none: a counting rule (the qualifying period) | `ei5-qualifying`: `s 152.08(1) the qualifying period of a self-employed person` |
| s 152.08(2) | the Commission | the self-employed person | privilege / no-right: the same self-employed earnings cannot found a second initial claim | `ei5-qualifying`: `s 152.08(2) the self-employed earnings during a qualifying period may be taken into account` |
| s 152.09(1) | the self-employed person | the Commission | power / liability: the person elects the Part under which benefits are paid | `ei5-qualifying`: `s 152.09(1) the individual must elect the Part under which benefits are to be paid`, `s 152.09(1) the Part under which benefits are to be paid` |
| s 152.09(2) | the Commission | the self-employed person | immunity / disability: the election binds for the reason | `ei5-qualifying`: `s 152.09(2) the election is binding in respect of the reason` |
| s 152.1(1), (2) | the self-employed person | the Commission | claim / duty: the Commission must establish a benefit period for the person who qualifies and claims | `ei5-benefit-period`: `s 152.1(1) a benefit period shall be established`, `s 152.1(1) benefits are payable for the week`, `s 152.1(2) the conditions for establishing a benefit period are met` |
| s 152.11(1) to (3), (8), (10) to (16) | none | none | none: counting rules (the day a benefit period begins and ends, its length and extensions) | `ei5-benefit-period`: `s 152.11(1) the day on which a benefit period begins`, `s 152.11(3) a benefit period may be established despite a prior benefit period`, `s 152.11(8) the benefit period or portion of it is treated as having begun`, `s 152.11(10) the day on which a request that the benefit period end is regarded as having been made`, `s 152.11(11) the number of weeks by which the benefit period is extended` |
| s 152.11(4), (5), (5.1) | the self-employed person | the Commission | power / liability: on showing good cause the person may have a late claim regarded as made on an earlier day | `ei5-benefit-period`: `s 152.11(4) the day on which an initial claim for benefits is regarded as having been made`, `s 152.11(5) the day on which a claim other than an initial claim is regarded as having been made` |
| s 152.11(6), (6.1), (6.2) | the Commission | the self-employed person | immunity / disability: in the caring cases the claim is not regarded as made on an earlier day | `ei5-benefit-period`: `ss 152.11(6), (6.1) and (6.2) the claim is not regarded as made on an earlier day` |
| s 152.11(7) | the Commission | the self-employed person | power / liability: the Commission may cancel a benefit period (or, at the person's request, its early portion) | `ei5-benefit-period`: `s 152.11(7)(a) the Commission may cancel the benefit period`, `s 152.11(7)(b) the Commission may cancel the portion of the benefit period immediately before the first week for which benefits were paid or payable` |
| s 152.11(9) | the self-employed person | the Commission | power / liability: the person may request that the benefit period end | `ei5-benefit-period`: `s 152.11(9) the day on which the benefit period ends`, `s 152.11(9)(c) the day on which the person has requested the end of the benefit period, made a new initial claim and qualified` |
| s 152.12 | the self-employed person | the Commission | claim / duty: a decision on whether the person is qualified, and notice of it | `ei5-benefit-period`: `s 152.12 the person is owed a decision on whether they are qualified and notice of the decision` |
| s 152.13 | the self-employed person | the Commission | claim / duty: benefits for each week of unemployment in the benefit period | `ei5-payment`: `s 152.13 benefits may be paid for the week` |
| s 152.14 | none | none | none: limits on the content of the claim of s 152.13 (maximum weeks) | `ei5-payment`: `s 152.14(1) the maximum number of weeks for which benefits may be paid in a benefit period` |
| s 152.15 | the Commission | the self-employed person | privilege / no-right: nothing is payable until the waiting period is served | `ei5-payment`: `s 152.15 the waiting period of a self-employed person, in weeks`, `s 152.15 the person has served the waiting period and is entitled to be paid benefits` |
| s 152.151, 152.16 | none | none | none: the content of the claim (the waiting-period test and the weekly rate) | `ei5-payment`: `s 152.151(1) the week of unemployment is deemed to be a week for which benefits would otherwise be payable`, `s 152.16(1) the rate of weekly benefits payable to a self-employed person` |
| s 152.17(1) | the self-employed person | the Commission | claim / duty: the family supplement | `ei5-payment`: `s 152.17(1) the family supplement by which the rate is increased`, `s 152.17 the rate of weekly benefits with the family supplement` |
| s 152.17(4), (5) | none | none | none: limits on the content of the claim (the greatest increase and the greatest rate) | `ei5-payment`: `s 152.17(4) the greatest increase in the rate of weekly benefits`, `s 152.17(5) the maximum rate of weekly benefits` |
| s 152.18(1), (2), 152.19 | the Commission | the self-employed person | privilege / no-right: the Commission pays the amount less the deductions | `ei5-payment`: `s 152.18(1) the amount deducted from the benefits payable for the first three weeks`, `s 152.18(2) the deduction for earnings in a week of unemployment`, `ss 152.19(1) and (2) the deduction for working days on which the person is not entitled` |
| s 152.18(3) | the Commission | the self-employed person | power / liability: where in the Commission's opinion earnings were knowingly not declared, the whole amount is deducted | `ei5-payment`: `s 152.18(3)(a) the amount to be deducted for undeclared earnings`, `s 152.18(3)(b) the amounts deducted in consecutive weeks` |
| s 152.2 | the Commission | the self-employed person | privilege / no-right: nothing is payable for a period in prison or outside Canada, except as prescribed | `ei5-payment`: `s 152.2 the person is not entitled to receive benefits for the period` |
| s 152.21(1) | the Crown (Receiver General, through the Minister of National Revenue) | the self-employed person | claim / duty: the self-employment premium | `ei5-premium`: `s 152.21(1) the self-employment premium for the year`, `s 152.21(1) and (3) a premium is required to be paid in respect of the year` |
| s 152.21(2), (3) | none | none | none: counting rules (the amount and the years for which a premium is due) | `ei5-premium`: `s 152.21(2) the amount on which the premium is calculated`, `s 152.21(1) and (3) a premium is required to be paid in respect of the year` |
| s 152.22(1), (2) | the Minister of National Revenue | the self-employed person | claim / duty: the return of self-employed earnings, without notice (1) or on demand (2) | `ei5-premium`: `s 152.22(1) the day on or before which the return of self-employed earnings must be filed without notice or demand`, `s 152.22(1) the person's representative must file the return`, `s 152.22(2) the day on or before which the return demanded must be filed` |
| s 152.22(3) | the Minister of National Revenue | the person administering the self-employed person's affairs | claim / duty: the return the administrator must file | `ei5-premium`: `s 152.22(3) the administrator of the self-employed person's affairs must file the return` |
| s 152.22(4), 152.23 | the Minister of National Revenue | the self-employed person | claim / duty: the province of residence and the estimate of the premium in the return | `ei5-premium`: `s 152.22(4) the return contains the information required`, `s 152.23 the return contains the estimate required` |
| s 152.24 | the self-employed person | the Minister of National Revenue | claim / duty: examination of the return, assessment and a notice of assessment | `ei5-premium`: `s 152.24 the person who filed the return is owed an assessment and a notice of assessment` |
| s 152.25 | the Crown (Receiver General, through the Minister of National Revenue) | the self-employed person | claim / duty: payment of the whole premium, or of the instalments and the remainder | `ei5-premium`: `s 152.25(1) the day on or before which the whole premium must be paid`, `s 152.25(2) the amount payable on or before December 31`, `ss 152.25(2) and (3) the remainder of the premium payable on or before the balance-due day`, `s 152.25(3)(a) each of the four instalments`, `s 152.25(3)(b)(i) each of the instalments of March 15 and June 15`, `s 152.25(3)(b)(ii) each of the instalments of September 15 and December 15`, `s 152.25(3) the days on or before which the instalments of the year are due`, `ss 152.25(2) and (3) the instalment is required` |
| s 152.26(1), (2) | the Crown (Receiver General, through the Minister of National Revenue) | the self-employed person | claim / duty: interest on the unpaid premium and on missed instalments | `ei5-premium`: `s 152.26(1) the difference on which interest is payable`, `s 152.26(1) the period for which interest is payable`, `s 152.26(2) the amount of the instalment on which interest is payable`, `s 152.26(2) the period for which interest on the unpaid instalment is payable` |
| s 152.26(3), (4) | none | none | none: counting rules (the instalment the person is deemed to have owed) | `ei5-premium`: `s 152.26(3) the instalment on which interest is calculated for a farmer`, `s 152.26(4) the least total of the instalments required by the instalment day` |
| s 152.27(1) | the Minister of National Revenue | the self-employed person | power / liability: the 5% penalty for failing to file, which the Minister may reduce or remit | `ei5-premium`: `s 152.27(1) the penalty for failing to file a return`, `s 152.27(1) the Minister of National Revenue may reduce or remit the penalty` |
| s 152.27(2) | the Minister of National Revenue | the person administering the self-employed person's affairs | power / liability: the penalty of $5 a day to $50 | `ei5-premium`: `s 152.27(2) the penalty for failing to file a return required by subsection 152.22(3)` |
| s 152.28(1), 152.29 | none | none | none: the Income Tax Act's collection provisions apply, and a payment is applied to the premium first | `ei5-premium`: `s 152.28(1) the provision of the Income Tax Act applies to the premium as though it were tax`, `s 152.29 the part of the payment applied in payment of the premium`, `s 152.29 the part of the payment left to be applied in payment of tax under the Income Tax Act` |
| s 152.3(1)(a) | the Minister of National Revenue | the self-employed person | power / liability: the Minister may refund an excess payment without an application | `ei5-premium`: `s 152.3(1) the excess of the amount paid over the premium`, `s 152.3(1)(b) the Minister of National Revenue shall make the refund` |
| s 152.3(1)(b) | the self-employed person | the Minister of National Revenue | claim / duty: the refund of an excess payment on written application within three years after the year | `ei5-premium`: `s 152.3(1) the excess of the amount paid over the premium`, `s 152.3(1)(b) the Minister of National Revenue shall make the refund` |
| s 152.3(2) | none | none | none: sends the refund to s 96(11) to (13) (piece ei3) | `ei5-premium`: `s 152.3(2) subsections 96(11) to (13) apply to the refund` |
| s 152.31(1) to (4) | none | none | none: other provisions of the Act (and its proceedings sections 102 and 125) apply to this Part | `ei5-other-provisions`: `s 152.31(1) a provision of the Act applies to this Part`, `s 152.31(2)(a) subsection 86(1) applies to the person as it applies to an employer`, `s 152.31(2)(b) subsection 88(5) applies to the matter as though its reference to this Part were a reference to Part VII.1`, `s 152.31(3) section 102 applies to the matter`, `s 152.31(4) section 125 applies to the matter` |
| s 152.32 | the Crown | the person who contravenes s 152.22 | power / liability: prosecution on summary conviction for a fine of at least $25 a day to $1,000 | `ei5-other-provisions`: `s 152.32 the person is guilty of an offence and liable on summary conviction to a fine`, `s 152.32 the least fine on summary conviction`, `s 152.32 the greatest fine on summary conviction` |
| s 152.34 | none identified in the text | the Minister (s 2(1): the Minister of Employment and Social Development, because Part VII.1 is not one of the Parts IV and VII for which the definition names the Minister of National Revenue) | duty without a stated correlative claim: the Minister must cause a review five years after the Part comes into force; it gives the individual nothing to claim, so the seat has no question for it | `ei5-other-provisions`: `s 152.34 the day five years after the day on which this Part comes into force`, `s 152.34 the party who must cause the review to be conducted` |
| s 152.01(1) to (5) (the definitions, the earnings rules, the week of unemployment, rounding) | none | none | none: definitions and counting rules | `ei5-interpretation`: `s 152.01(2) the amount of the self-employed earnings of a self-employed person for a year`, `s 152.01(3) the income of a business for clause (2)(a)(i)(A)`, `s 152.01(4) week of unemployment for a self-employed person`; `eia-core`: `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` |
| s 152.311, 152.33 | none | none | none for the individual: machinery (delegation; the Commission's regulation-making powers, whose exercise creates relations in the Regulations, not here) | (inert; see the coverage table) |

## Coverage table

The range, lines 2109 to 2688 of `S.C.-1996-c.-23.txt`, holds **14 structural headings** (the Part heading and 13 division headings) and **38 sections** (152.01 to 152.34, including 152.061, 152.062, 152.151 and 152.311).
Every heading has an `inert` row (14 rows: a pure title), and every section has at least one row.
A section whose subsections differ in disposition or in the rule they state has one row per subsection or paragraph (s 152.01(1) has one per definition; s 152.07(1)(d) one per sub-paragraph; s 152.33 one per paragraph), so **212 rows cover 14 headings and 38 sections: 14 heading rows and 198 provision rows**.
The counts by disposition are on the line below.

The text also carries short unpunctuated lines above sections and subsections ("Definitions", "Exception", "Limitation", "Deduction"): marginal notes.
A script found 177 such lines in the range (no digit or parenthesis at the start, under 75 characters, no final punctuation, not starting lower-case), of which 14 are the structural headings above.
The other 163 label the provision beneath them and have no row of their own; each is covered by the row of the provision it labels.
A script confirmed that every non-blank line from 2109 to 2688 lies inside the source lines of at least one row, and that every rule named in the `where` column exists under that name in the module named.

Columns.
`source lines` are `src:` line numbers of `S.C.-1996-c.-23.txt`.
`where` is the module and rule that encode the provision, as the rule is named in the module (a row that lists two rules means the provision is encoded in both: a condition and its consequence, for example).
`inert` rows give a reason from the brief's list (machinery, a pure title) and say what the provision does.
A `fork` row points to the register below by its identifier (F1 to F26) in the note.
`repealed or blank in this text` rows quote what the text shows (`[Repealed, 2012, c. 27, s. 22]`).
No row is `deferred`: the table was filled as each module was written, and its last revision checked every row against the module it names.

Counts: 212 rows: 144 encoded, 37 fork, 26 inert, 5 repealed or blank in this text.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| heading "Part VII.1 heading" | src:2109 | inert | - | A pure title: the heading of Part VII.1 (Benefits for Self-Employed Persons). It names the Part and states no rule; the keel's `Part of the Act` constructor `Part VII.1` carries the name where a rule needs it. |
| heading "Interpretation" | src:2111 | inert | - | A pure title: the division heading above s 152.01. It carries no text of its own. |
| s 152.01(1) lead-in | src:2112-2113 | encoded | rows below | "The following definitions apply in this Part." makes each definition below apply throughout Part VII.1; it adds no rule of its own. |
| s 152.01(1) "balance-due day" | src:2114-2116 | fork | `ei5-interpretation` `s 152.01(1) balance-due day of a self-employed person for a year` | F1: the month boundaries of "after October ... before May". The day is used by s 152.25 and s 152.26. |
| s 152.01(1) "business" | src:2117 | encoded | `ei5-interpretation` `s 152.01(1) business includes` | An open list with one exclusion: JUST TRUE for a listed kind, JUST FALSE for an office or employment, NOTHING for anything else. |
| s 152.01(1) "disentitled" | src:2118 | encoded | `ei5-interpretation` `s 152.01(1) disentitled` | Six inputs: ss 49 and 50 (piece ei2) and the regulations are plain inputs; 152.03, 152.15 and 152.2 are this piece's rules, whose results a caller passes. |
| s 152.01(1) "family member" | src:2119 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 242]. The Regulations, reg 1(3) (piece er1), define "family member" for ss 152.06 to 152.062; those rules take the fact as an input. |
| s 152.01(1) "initial claim for benefits" | src:2120 | encoded | `ei5-interpretation` `s 152.01(1) initial claim for benefits` | A claim made by a self-employed person for the purpose of establishing their benefit period. |
| s 152.01(1) "qualifying period" | src:2121 | encoded | `ei5-qualifying` `s 152.08(1) the qualifying period of a self-employed person` | "means the period described in section 152.08": the definition sends the reader to s 152.08(1), whose rule computes it. |
| s 152.01(1) "self-employed person" | src:2122-2125 | fork | `ei5-interpretation` `s 152.01(1) self-employed person, paragraph (a)`, `s 152.01(1) self-employed person, paragraph (b)` and `s 152.01(1) self-employed person` | F2: "by reason of paragraph 5(2)(b)". The keel rule `s 5(2)(b) employment of a person by a corporation they control` is called for the 40% test. The closing sentence (Part VIII fishers; employment included by s 5(4)(c)) takes individuals out. |
| s 152.01(1) "waiting period" | src:2126 | encoded | `ei5-payment` `s 152.15 the waiting period of a self-employed person, in weeks` | "means the one week of the benefit period described in section 152.15": one week. |
| s 152.01(2) lead-in | src:2127-2128 | encoded | `ei5-interpretation` `s 152.01(2) the amount of the self-employed earnings of a self-employed person for a year` | Selects among paragraphs (a), (b) and (c) by which paragraphs of the definition the individual is in; NOTHING when in neither. |
| s 152.01(2)(a)(i)(A) | src:2129-2131 | encoded | `ei5-interpretation` `s 152.01(2)(a)(i)(A) their income for the year from their businesses, other than a rental business` and `s 152.01(2)(a)(i)(A) a business more than fifty per cent of the gross revenue of which consisted of rent from land or buildings` | Income computed under the Income Tax Act is an input per business; exactly half rent does not take a business out. |
| s 152.01(2)(a)(i)(B) | src:2132-2133 | fork | `ei5-interpretation` `s 152.01(2)(a)(i) the amount equal to their business income less their business losses` | F3: no floor at zero. |
| s 152.01(2)(a)(ii) | src:2134 | encoded | `ei5-interpretation` `s 152.01(2)(a)(ii) their income for the year from employment excluded by a regulation under paragraph 5(6)(c)` | An input (the figure is computed under the Income Tax Act). |
| s 152.01(2)(b) | src:2135 | encoded | `ei5-interpretation` `s 152.01(2)(b) the self-employed earnings of an individual referred to in paragraph (b) of the definition` | An input: the insurable earnings the person would have had (Part IV, piece ei3). |
| s 152.01(2)(c) | src:2136 | encoded | `ei5-interpretation` `s 152.01(2) the amount of the self-employed earnings of a self-employed person for a year` | The aggregate of paragraphs (a) and (b) when the individual is in both. |
| s 152.01(3) | src:2137-2138 | encoded | `ei5-interpretation` `s 152.01(3) the income of a business for clause (2)(a)(i)(A)` | An Indian's income on a reserve is figured without reference to paragraph 81(1)(a) of the Income Tax Act; both figures are inputs. |
| s 152.01(4) | src:2139-2140 | encoded | `ei5-interpretation` `s 152.01(4) week of unemployment for a self-employed person` | One input: regs 30.1 and 30.2 (piece er2) define it. |
| s 152.01(5) | src:2141-2142 | encoded | `eia-core` `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` | The keel's rule; ei5-payment calls it for ss 152.16 and 152.17 and its tests assert it for this subsection. |
| heading "Application" | src:2144 | inert | - | A pure title: the division heading above s 152.02. |
| s 152.02(1) | src:2145-2146 | fork | `ei5-agreement` `s 152.02(1) this Part applies in respect of a person` | F11: the day citizenship or residence is tested is not stated. |
| s 152.02(2) | src:2147-2148 | fork | `ei5-agreement` `s 152.02(2) the agreement is in force on a day` | F6: the agreement is not in force on the day on which it terminates. |
| s 152.02(3) | src:2149-2150 | fork | `ei5-agreement` `s 152.02(3) the agreement is in the form and on the conditions the Commission has fixed` | F4: the text does not say what follows if the form or a condition is not met. |
| s 152.02(4) | src:2151-2152 | encoded | `ei5-agreement` `s 152.02(4) the agreement is deemed to be terminated` and `s 152.02(4) the individual may terminate the agreement by notice` | No regulation setting circumstances of deemed termination, or circumstances that allow termination after benefits were paid, was found in the Regulations as deposited. |
| s 152.02(5) | src:2153-2154 | encoded | `ei5-agreement` `s 152.02(5) the day on which an agreement deemed to be terminated is terminated` | The prescribed date is an input; none was found in the Regulations as deposited. |
| s 152.02(6) | src:2155-2158 | fork | `ei5-agreement` `s 152.02(6) December 31 of the year in which the notice is given` and `s 152.02(6) and (7) what becomes of a notice to terminate the agreement` | F5: overlaps between (6)(a) and (6)(b), and between a deemed termination and a notice. |
| s 152.02(7) | src:2159-2160 | encoded | `ei5-agreement` `s 152.02(6) and (7) what becomes of a notice to terminate the agreement` | Tested before (6) because it begins "Despite subsection (6)"; the 60th day counts. |
| heading "Benefits" | src:2162 | inert | - | A pure title: the division heading above s 152.03. |
| s 152.03(1) | src:2163-2164 | fork | `ei5-sickness-pregnancy` `s 152.03(1) and (1.1) a self-employed person is entitled to benefits while unable to work` | F12: the (1.1) person must still be ill and unable to work. |
| s 152.03(1.1) | src:2165-2166 | fork | `ei5-sickness-pregnancy` `s 152.03(1) and (1.1) a self-employed person is entitled to benefits while unable to work` | F12. |
| s 152.03(2) | src:2167-2168 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | The shared reduction rule; F7 (stops at zero). |
| s 152.03(3) | src:2169-2170 | encoded | `ei5-sickness-pregnancy` `ss 152.03(3) and 152.04(4) benefits after the deduction of allowances payable under a plan whose employer's premium has been reduced` | F7. Subject to s 152.18(3), which is a separate rule in ei5-payment. |
| s 152.03(4) | src:2171-2172 | encoded | `ei5-sickness-pregnancy` `s 152.03(4) a self-employed person is not entitled to benefits under subsection (1)` and `s 152.03 entitled to benefits because of illness, injury or quarantine` | Reg 30.2 (piece er2) says when a person is deemed not working; an input. |
| s 152.04(1) | src:2173-2174 | encoded | `ei5-sickness-pregnancy` `s 152.04(1) benefits are payable because of pregnancy` | Proof is reg 41(1) (piece er3); an input. |
| s 152.04(2) | src:2175-2182 | fork | `ei5-sickness-pregnancy` `s 152.04(2) the period for which benefits are payable because of pregnancy` | F8 (whole weeks) and F9 (confinement not yet occurred). |
| s 152.04(3) | src:2183-2184 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | Shared rule; regs 76.36 to 76.42 (piece er4) prescribe the reduction for ss 152.04 and 152.05. |
| s 152.04(3.1) | src:2185-2186 | encoded | `ei5-sickness-pregnancy` `s 152.04(3.1) the period, for serving the waiting period, with the week that immediately precedes it` | A deeming rule for the waiting period of s 152.15. |
| s 152.04(4) | src:2187-2188 | encoded | `ei5-sickness-pregnancy` `ss 152.03(3) and 152.04(4) benefits after the deduction of allowances payable under a plan whose employer's premium has been reduced` | Shared rule; F7. |
| s 152.04(5) | src:2189-2190 | encoded | `ei5-sickness-pregnancy` `s 152.04(5) and (6) the period extended because the child is hospitalized` | F8 for the end of the week. |
| s 152.04(6) | src:2191-2192 | encoded | `ei5-sickness-pregnancy` `s 152.04(5) and (6) the period extended because the child is hospitalized` | The limit of 52 weeks after the week of confinement. |
| s 152.05(1) | src:2193-2194 | encoded | `ei5-parental` `s 152.05(1) benefits are payable for the care of a child` | Two limbs: new-born children, children placed for adoption. |
| s 152.05(1.1) | src:2195-2196 | encoded | `ei5-parental` `s 152.05(1.1) the claim meets the requirement to elect` | The election is the keel's `Election of maximum weeks`. |
| s 152.05(1.2) | src:2197-2198 | encoded | `ei5-parental` `s 152.05(1.2) the election is irrevocable` |  |
| s 152.05(1.3) | src:2199-2200 | encoded | `ei5-parental` `s 152.05(1.3) the election that binds the person` | The first claimant's election binds both. |
| s 152.05(2) | src:2201-2204 | fork | `ei5-parental` `s 152.05(2) the period for which parental benefits are payable` | F8. |
| s 152.05(3) | src:2205-2206 | encoded | `ei5-parental` `s 152.05(3) and (4) the period extended because the child or children are hospitalized` |  |
| s 152.05(4) | src:2207-2208 | encoded | `ei5-parental` `s 152.05(3) and (4) the period extended because the child or children are hospitalized` | 104 weeks from the first day. |
| s 152.05(5) | src:2209-2210 | encoded | `ei5-parental` `s 152.05(5) the period is extended so that benefits may be paid up to the applicable maximum` and `s 152.05(5) the number of weeks of benefits that may be paid, up to the applicable maximum, after the extension` | The text says benefits may then be paid up to the maximum but not by how many calendar weeks the period is extended: finding 3. |
| s 152.05(5.1) | src:2211-2212 | encoded | `ei5-parental` `s 152.05(5.1) the number of weeks by which the period is extended` | 26 weeks when only the 61-week benefit was paid. |
| s 152.05(6) | src:2213-2214 | encoded | `ei5-parental` `s 152.05(6) the length of the period after an extension under subsection (5)` | The limit is s 152.11(16), an input here (ei5-benefit-period computes it). |
| s 152.05(7) | src:2215-2216 | encoded | `ei5-parental` `s 152.05(7) the length of the period after an extension under subsections 152.11(11) to (14.1)` | 104 weeks. |
| s 152.05(8) to (10) | src:2217 | repealed or blank in this text | - | [Repealed, 2012, c. 27, s. 22] |
| s 152.05(11) | src:2218-2219 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | Shared rule. |
| s 152.05(12) | src:2220-2221 | encoded | `ei5-parental` `ss 152.05(12) and (13) the maximum number of weeks of benefits that may be divided between two claimants` and `s 152.05(12) the weeks of benefits to be paid to a claimant after the division` | 40 or 69 weeks; the prescribed rules are reg 41.6 (piece er3), an input. |
| s 152.05(13) | src:2222-2225 | encoded | `ei5-parental` `ss 152.05(12) and (13) the maximum number of weeks of benefits that may be divided between two claimants` and `s 152.05(12), (13) and (13.01) a division of the weeks of benefits is within the limits` | "For greater certainty": the same 40 or 69. |
| s 152.05(13.01) | src:2226-2227 | encoded | `ei5-parental` `s 152.05(13.01) the maximum number of weeks for which benefits may be paid to a claimant` | 35 or 61 by the election. |
| s 152.05(14) | src:2228-2233 | encoded | `ei5-parental` `s 152.05(14) the waiting period may be deferred` | Four limbs (a) to (d), alternatives; (d) is an input. |
| s 152.05(15) | src:2234-2237 | encoded | `ei5-parental` `s 152.05(15)(a) the self-employed person is not required to serve a waiting period` and `s 152.05(15)(b) the person making the claim under section 22 or 23 may have their waiting period deferred in accordance with section 23` | Two limbs; (b) is a power of the other claimant, stated neutrally. |
| s 152.06(1) | src:2238-2243 | encoded | `ei5-caring` `s 152.06(1) benefits are payable for the care or support of a gravely ill family member` | 26 weeks, or the shorter period under (4)(a). |
| s 152.06(2) | src:2244-2245 | encoded | `ei5-caring` `ss 152.06(2), 152.061(2) and 152.062(2) the certificate may be issued by the practitioner` | Reg 41.2 (piece er3) is the regulation found. |
| s 152.06(3) | src:2246-2254 | fork | `ei5-caring` `ss 152.06(3), 152.061(3) and 152.062(3) the period for which benefits are payable` | F10 and F8: the 52 weeks end on a Saturday. |
| s 152.06(3.1) | src:2255-2256 | encoded | `ei5-caring` `s 152.06(3.1) an additional certificate is required for benefits payable after the end of the 26 weeks` | Always no, unless s 50(8.1) (piece ei2) says otherwise. |
| s 152.06(4) | src:2257-2260 | encoded | `ei5-caring` `s 152.06(4)(a) the number of weeks within which the certificate must state a significant risk of death` and `s 152.06(4)(b) the number of weeks that ends the period under subparagraph (3)(b)(iii)` | No regulation prescribing a shorter period was found. |
| s 152.06(5) | src:2261-2265 | encoded | `ei5-caring` `ss 152.06(5), 152.061(5) and 152.062(4) subparagraph (3)(a)(ii) does not apply to the claim` | Shared rule. |
| s 152.06(6) | src:2266-2270 | encoded | `ei5-caring` `ss 152.06(6), 152.061(6) and 152.062(5) the waiting period may be deferred` | Shared rule. |
| s 152.06(7) | src:2271-2272 | encoded | `ei5-caring` `ss 152.06(7) and (8), 152.061(8) and (9) and 152.062(6) and (7) a division of the remaining weeks is within the maximum` and `ss 152.06(7), 152.061(8) and 152.062(6) the weeks of benefits to be paid to a claimant after the division` | 26 weeks. |
| s 152.06(8) | src:2273-2274 | encoded | `ei5-caring` `s 152.06(7) and (8) the maximum number of weeks that may be divided` | "For greater certainty": the same 26 weeks. |
| s 152.06(9) | src:2275-2276 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | Shared rule. |
| s 152.061(1) | src:2277-2280 | encoded | `ei5-caring` `s 152.061(1) benefits are payable for the care or support of a critically ill child` |  |
| s 152.061(2) | src:2281-2282 | encoded | `ei5-caring` `ss 152.06(2), 152.061(2) and 152.062(2) the certificate may be issued by the practitioner` | Shared rule. |
| s 152.061(3) | src:2283-2291 | fork | `ei5-caring` `ss 152.06(3), 152.061(3) and 152.062(3) the period for which benefits are payable` | F10, F8. Shared rule. |
| s 152.061(4) | src:2292 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 247] |
| s 152.061(5) | src:2293-2297 | encoded | `ei5-caring` `ss 152.06(5), 152.061(5) and 152.062(4) subparagraph (3)(a)(ii) does not apply to the claim` | Shared rule. |
| s 152.061(6) | src:2298-2302 | encoded | `ei5-caring` `ss 152.06(6), 152.061(6) and 152.062(5) the waiting period may be deferred` | Shared rule. |
| s 152.061(7) | src:2303 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 247] |
| s 152.061(8) | src:2304-2305 | encoded | `ei5-caring` `s 152.061(8) and (9) the maximum number of weeks that may be divided` and the shared division rules | 35 weeks. |
| s 152.061(9) | src:2306-2307 | encoded | `ei5-caring` `s 152.061(8) and (9) the maximum number of weeks that may be divided` | "For greater certainty": the same 35 weeks. |
| s 152.061(10) | src:2308-2309 | encoded | `ei5-caring` `ss 152.061(10) and 152.062(8) benefits under section 23.1 or 152.06 are not payable in respect of the child or adult on a day` |  |
| s 152.061(10.1) | src:2310-2311 | encoded | `ei5-caring` `s 152.061(10.1) benefits under section 23.3 or 152.062 are not payable on a day` | 52 weeks from the first day of the week of s 152.061(3)(a). |
| s 152.061(11) | src:2312-2313 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | Shared rule. |
| s 152.062(1) | src:2314-2317 | encoded | `ei5-caring` `s 152.062(1) benefits are payable for the care or support of a critically ill adult` |  |
| s 152.062(2) | src:2318-2319 | encoded | `ei5-caring` `ss 152.06(2), 152.061(2) and 152.062(2) the certificate may be issued by the practitioner` | Shared rule. |
| s 152.062(3) | src:2320-2328 | fork | `ei5-caring` `ss 152.06(3), 152.061(3) and 152.062(3) the period for which benefits are payable` | F10, F8. Shared rule. |
| s 152.062(4) | src:2329-2333 | encoded | `ei5-caring` `ss 152.06(5), 152.061(5) and 152.062(4) subparagraph (3)(a)(ii) does not apply to the claim` | Shared rule. |
| s 152.062(5) | src:2334-2338 | encoded | `ei5-caring` `ss 152.06(6), 152.061(6) and 152.062(5) the waiting period may be deferred` | Shared rule. |
| s 152.062(6) | src:2339-2340 | encoded | `ei5-caring` `s 152.062(6) and (7) the maximum number of weeks that may be divided` and the shared division rules | 15 weeks. |
| s 152.062(7) | src:2341-2342 | encoded | `ei5-caring` `s 152.062(6) and (7) the maximum number of weeks that may be divided` | "For greater certainty": the same 15 weeks. |
| s 152.062(8) | src:2343-2344 | encoded | `ei5-caring` `ss 152.061(10) and 152.062(8) benefits under section 23.1 or 152.06 are not payable in respect of the child or adult on a day` | Shared rule with s 152.061(10). |
| s 152.062(9) | src:2345-2346 | encoded | `ei5-sickness-pregnancy` `ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11) and 152.062(9) benefits after the reduction prescribed for benefits payable under a provincial law` | Shared rule. |
| heading "Qualifying for Benefits" | src:2348 | inert | - | A pure title: the division heading above s 152.07. |
| s 152.07(1) lead-in | src:2349-2350 | encoded | `ei5-qualifying` `s 152.07(1) a self-employed person qualifies for benefits` | All four paragraphs are cumulative ("if (a); (b); (c); and (d)"). F13 for the day tested. |
| s 152.07(1)(a) | src:2351 | fork | `ei5-qualifying` `s 152.07(1)(a) at least 12 months have expired since the day on which the person entered into the agreement` | F13. A prescribed period replaces 12 months; none found in the Regulations; reg 76.43 deems the condition met in one case. |
| s 152.07(1)(b) | src:2352 | encoded | `ei5-qualifying` `s 152.07(1)(b) the agreement has not been terminated or deemed to have been terminated` | The caller passes whether the agreement has been terminated (ei5-agreement). |
| s 152.07(1)(c) | src:2353 | encoded | `ei5-qualifying` `s 152.07(1)(c) the person has had an interruption of earnings from self-employment` | Reg 14.01 (piece er1) is the input. |
| s 152.07(1)(d) lead-in | src:2354 | encoded | `ei5-qualifying` `s 152.07(1)(d) the person has had during their qualifying period an amount of self-employed earnings equal to or greater than the amount required` and `s 152.07(1)(d) the amount of self-employed earnings the person must have had during their qualifying period` | "equal to or greater than". |
| s 152.07(1)(d)(i) lead-in | src:2355 | encoded | `ei5-qualifying` `s 152.07(1)(d) a violation was accumulated in the 260 weeks before making the initial claim` | F14. |
| s 152.07(1)(d)(i)(A) | src:2356 | encoded | `ei5-qualifying` `s 152.07(1)(d)(i)(A) the first day of the period in which a benefit period must begin for the amount of $5,000` and the last-day constant, in `s 152.07(1)(d)(i) the amount of self-employed earnings required of a person who has not accumulated a violation` | $5,000 for a benefit period beginning 3 January to 25 September 2021, both days counted, despite any regulation. |
| s 152.07(1)(d)(i)(B) | src:2357 | encoded | `ei5-qualifying` `s 152.07(1)(d)(i)(B) the first day of the period in which a benefit period must begin for the amount of $5,289` and the last-day constant, in the same rule | $5,289 for a benefit period beginning 26 September 2021 to 24 September 2022, despite any regulation. |
| s 152.07(1)(d)(i)(C) | src:2358 | encoded | `ei5-qualifying` `s 152.07(1)(d)(i) the amount of self-employed earnings required of a person who has not accumulated a violation` | $6,000 or the amount fixed or determined by regulation, if any (reg 11.1, piece er1, an input). |
| s 152.07(1)(d)(ii) | src:2359-2363 | fork | `ei5-qualifying` `s 152.07(1)(d)(ii) the multiplier for the class of the violation` and `s 152.07(1)(d) the amount of self-employed earnings the person must have had during their qualifying period` | F16: which violation counts. The multiplier applies to the amount that would otherwise apply for the date the benefit period begins. 1.25, 1.5, 1.75, 2, or the prescribed multiplier. |
| s 152.07(2) | src:2364-2368 | encoded | `ei5-qualifying` `s 152.07(2) a self-employed person accumulates a violation` | A notice of violation plus any one of three circumstances. |
| s 152.07(3) lead-in and (a) | src:2369-2371 | encoded | `ei5-qualifying` `s 152.07(3) the value of a violation` | Total of (a) and (b). |
| s 152.07(3)(b) | src:2372 | encoded | `ei5-qualifying` `s 152.07(3)(b) the weekly rate of benefits multiplied by the average number of weeks, held to the maximum of subsection (4)` | Weekly rate times the average number of weeks (reg 13(2), piece er1), only if disentitled or the act relates to the qualification requirements. |
| s 152.07(4) | src:2373-2374 | encoded | `ei5-qualifying` `s 152.07(3)(b) the weekly rate of benefits multiplied by the average number of weeks, held to the maximum of subsection (4)` | The maximum is the amount of benefits that could have been paid. |
| s 152.07(5)(a) | src:2375-2380 | encoded | `ei5-qualifying` `s 152.07(5) the class of a violation` | Under $1,000, $1,000 to under $5,000, $5,000 or more; a violation for which a warning was imposed has no class (NOTHING). |
| s 152.07(5)(b) | src:2381 | fork | `ei5-qualifying` `s 152.07(5) the class of a violation` | F14, F15. |
| s 152.07(6) | src:2382-2383 | encoded | `ei5-qualifying` `s 152.07(6) the day on which a violation accumulated under section 7.1 is deemed to be accumulated under this section` |  |
| s 152.07(7) | src:2384-2385 | encoded | `ei5-qualifying` `s 152.07(7) the violation may be taken into account under paragraph (1)(d) in this initial claim` | At most two initial claims. |
| s 152.08(1) | src:2386-2387 | encoded | `ei5-qualifying` `s 152.08(1) the qualifying period of a self-employed person` | The calendar year before the year in which the benefit period begins. |
| s 152.08(2) | src:2388-2389 | encoded | `ei5-qualifying` `s 152.08(2) the self-employed earnings during a qualifying period may be taken into account` | One initial claim only. |
| s 152.09(1) | src:2390-2391 | encoded | `ei5-qualifying` `s 152.09(1) the individual must elect the Part under which benefits are to be paid` and `s 152.09(1) the Part under which benefits are to be paid` | The Part is the keel's `Part of the Act`; NOTHING when the election is missing or invalid. |
| s 152.09(2) | src:2392-2399 | encoded | `ei5-qualifying` `s 152.09(2) the election is binding in respect of the reason` | True for each of the six special reasons. |
| heading "Benefit Period" | src:2401 | inert | - | A pure title: the division heading above s 152.1. |
| s 152.1(1) | src:2402-2403 | encoded | `ei5-benefit-period` `s 152.1(1) a benefit period shall be established` and `s 152.1(1) benefits are payable for the week` | Qualifies under s 152.07 and makes an initial claim; then benefits are payable for each week of unemployment in the period. |
| s 152.1(2) | src:2404-2407 | encoded | `ei5-benefit-period` `s 152.1(2) the conditions for establishing a benefit period are met` | Both paragraphs are required ("unless (a) ... and (b)"); the composite `s 152.1 and s 152.11(3) a benefit period is established` adds (1) and s 152.11(3). |
| s 152.11(1) | src:2408-2412 | encoded | `ei5-benefit-period` `s 152.11(1) the day on which a benefit period begins` | The later of two Sundays. |
| s 152.11(2) | src:2413-2414 | fork | `ei5-benefit-period` `s 152.11(2), (15) and (16) the length of the benefit period, in weeks` | F17: 52 weeks, except as (11) to (19) provide. |
| s 152.11(3) | src:2415-2416 | encoded | `ei5-benefit-period` `s 152.11(3) a benefit period may be established despite a prior benefit period` |  |
| s 152.11(4) | src:2417-2418 | encoded | `ei5-benefit-period` `s 152.11(4) the day on which an initial claim for benefits is regarded as having been made` | "Shows ... good cause" is a BOOLEAN input (the Commission's judgment). F19. |
| s 152.11(5) | src:2419-2420 | encoded | `ei5-benefit-period` `s 152.11(5) the day on which a claim other than an initial claim is regarded as having been made` | The time prescribed is an input (piece er2). F19. |
| s 152.11(5.1) | src:2421-2422 | encoded | `ei5-benefit-period` `s 152.11(5.1) that fact is good cause for a delay in making a claim` |  |
| s 152.11(6) | src:2423-2427 | fork | `ei5-benefit-period` `ss 152.11(6), (6.1) and (6.2) the claim is not regarded as made on an earlier day` | F19. Shared rule for the three subsections. |
| s 152.11(6.1) | src:2428-2432 | fork | `ei5-benefit-period` `ss 152.11(6), (6.1) and (6.2) the claim is not regarded as made on an earlier day` | F19. Shared rule. |
| s 152.11(6.2) | src:2433-2437 | fork | `ei5-benefit-period` `ss 152.11(6), (6.1) and (6.2) the claim is not regarded as made on an earlier day` | F19. Shared rule. |
| s 152.11(7) | src:2438-2443 | encoded | `ei5-benefit-period` `s 152.11(7)(a) the Commission may cancel the benefit period` and `s 152.11(7)(b) the Commission may cancel the portion of the benefit period immediately before the first week for which benefits were paid or payable` | A power of the Commission (the person's liability); (b) is at the request of the person. |
| s 152.11(8) | src:2444-2445 | encoded | `ei5-benefit-period` `s 152.11(8) the benefit period or portion of it is treated as having begun` |  |
| s 152.11(9) | src:2446-2453 | fork | `ei5-benefit-period` `s 152.11(9) the day on which the benefit period ends` and `s 152.11(9)(c) the day on which the person has requested the end of the benefit period, made a new initial claim and qualified` | F18. |
| s 152.11(10) | src:2454-2455 | encoded | `ei5-benefit-period` `s 152.11(10) the day on which a request that the benefit period end is regarded as having been made` |  |
| s 152.11(11) | src:2456-2461 | encoded | `ei5-benefit-period` `s 152.11(11) the number of weeks by which the benefit period is extended` | Four reasons (a) to (d), each a number of weeks the person proves. |
| s 152.11(12) | src:2462-2463 | encoded | `ei5-benefit-period` `s 152.11(12) the number of weeks of the further extension` |  |
| s 152.11(13) | src:2464-2465 | encoded | `ei5-benefit-period` `s 152.11(13) the number of weeks by which the benefit period is extended because the child or children are hospitalized` |  |
| s 152.11(14) | src:2466-2467 | fork | `ei5-benefit-period` `s 152.11(14) the benefit period is extended so that those benefits may be paid up to the maximum total` | F17: the text does not give the number of weeks. |
| s 152.11(14.1) | src:2468-2469 | encoded | `ei5-benefit-period` `s 152.11(14.1) the number of weeks by which the benefit period is extended` | 26 weeks. |
| s 152.11(15) | src:2470-2471 | fork | `ei5-benefit-period` `s 152.11(2), (15) and (16) the length of the benefit period, in weeks` | F17: 104 weeks. |
| s 152.11(16) | src:2472-2473 | fork | `ei5-benefit-period` `s 152.11(16) the longest a benefit period extended under subsection (14) may be, in weeks` and `s 152.11(2), (15) and (16) the length of the benefit period, in weeks` | F17. |
| s 152.11(17) to (19) | src:2474 | repealed or blank in this text | - | [Repealed, 2012, c. 27, s. 24] |
| s 152.12 | src:2475-2476 | encoded | `ei5-benefit-period` `s 152.12 the person is owed a decision on whether they are qualified and notice of the decision` | The decision is the Commission's judgment; what the person is owed is the decision and the notice. |
| heading "Payment of Benefits" | src:2478 | inert | - | A pure title: the division heading above s 152.13. |
| s 152.13 | src:2479-2480 | encoded | `ei5-payment` `s 152.13 benefits may be paid for the week` | Benefits may be paid for each week of unemployment in the benefit period, subject to the maximums of s 152.14. |
| s 152.14(1) | src:2481-2490 | encoded | `ei5-payment` `s 152.14(1) the maximum number of weeks for which benefits may be paid in a benefit period` | MAYBE NUMBER: NOTHING for the regular reason and for parental benefits with no election. |
| s 152.14(2) | src:2491-2496 | encoded | `ei5-payment` `ss 152.14(2) and (4) the maximum number of weeks for a single pregnancy or placement` | 15, or 35/40, or 61/69 by the election and whether the weeks are divided. |
| s 152.14(3) | src:2497-2498 | encoded | `ei5-payment` `s 152.14(3) the placements are regarded as a single placement of a child or children for the purpose of adoption` |  |
| s 152.14(4) | src:2499-2502 | encoded | `ei5-payment` `ss 152.14(2) and (4) the maximum number of weeks for a single pregnancy or placement` | The same figures "under this Act" where a claim under s 23 is also made. |
| s 152.14(5) | src:2503-2504 | encoded | `ei5-payment` `ss 152.14(5), (5.1) and (5.2) the maximum number of weeks of benefits in respect of one family member, critically ill child or critically ill adult` and `ss 152.14(5) and (6) the period during which the maximum applies` | 26 weeks in 52 weeks from the first day of the week of s 152.06(3)(a). |
| s 152.14(5.1) | src:2505-2506 | encoded | `ei5-payment` `ss 152.14(5), (5.1) and (5.2) the maximum number of weeks of benefits in respect of one family member, critically ill child or critically ill adult` | 35 weeks (critically ill child). |
| s 152.14(5.2) | src:2507-2508 | encoded | `ei5-payment` `ss 152.14(5), (5.1) and (5.2) the maximum number of weeks of benefits in respect of one family member, critically ill child or critically ill adult` | 15 weeks (critically ill adult). |
| s 152.14(6) | src:2509-2510 | encoded | `ei5-payment` `ss 152.14(5) and (6) the period during which the maximum applies` | A shorter period prescribed for s 152.06(4) replaces the 52 weeks; none found. |
| s 152.14(7) | src:2511-2512 | encoded | `ei5-payment` `s 152.14(7) no further benefits are payable under section 152.06 in respect of the family member` |  |
| s 152.14(8) | src:2513-2514 | fork | `ei5-payment` `s 152.14(8) the maximum number of combined weeks` and `s 152.14(8) the combined weeks are within the maximum` | 50 combined weeks, or the s 152.11(16) maximum less two weeks when extended under s 152.11(14); see F17. |
| s 152.15 | src:2515-2516 | encoded | `ei5-payment` `s 152.15 the waiting period of a self-employed person, in weeks` and `s 152.15 the person has served the waiting period and is entitled to be paid benefits` | One week. This also carries the definition "waiting period" of s 152.01(1). |
| s 152.151(1) | src:2517-2520 | fork | `ei5-payment` `s 152.151(1) the week of unemployment is deemed to be a week for which benefits would otherwise be payable` | F22: whether the rate includes the family supplement. $50 below a rate of $200, 25% of the rate from $200. |
| s 152.151(2) | src:2521-2524 | encoded | `ei5-payment` `s 152.151(1) the week of unemployment is deemed to be a week for which benefits would otherwise be payable` | (a) the s 152.18(2) deduction is left out of the benefits that would have been payable: the rule starts from the rate; (b) earnings as determined for s 152.18(2): an input. |
| s 152.16(1) | src:2525-2528 | fork | `ei5-payment` `s 152.16(1) the rate of weekly benefits payable to a self-employed person` | F20 (rounding). 55%, or 33% for the weeks paid under s 152.05 under the 61-week election. |
| s 152.16(2) | src:2529-2530 | encoded | `ei5-payment` `ss 152.16(2) and 152.18(2.1) the part of the aggregate taken into account` | Held to the maximum yearly insurable earnings of s 4. |
| s 152.17(1) | src:2531-2532 | encoded | `ei5-payment` `s 152.17(1) the family supplement by which the rate is increased` and `s 152.17 the rate of weekly benefits with the family supplement` | The supplement amount and the criteria are reg 34's (piece er2). |
| s 152.17(2) | src:2533-2534 | inert | - | Regulation-making machinery: it tells the regulations that prescribe the low-income family eligibility criteria of s 152.17(1) (reg 34, piece er2) that they may borrow the Canada child benefit's criteria. It is permissive ("may include"), constrains only the maker of the regulations, and states no fact the person could be asked; the criteria themselves enter the rules for s 152.17(1) as the plain input that the person meets the prescribed criteria. |
| s 152.17(3) | src:2535-2536 | inert | - | Regulation-making machinery: the definition of "Canada child benefit" (a deemed overpayment under subdivision a.1 of Division E of Part I of the Income Tax Act) serves only subsection (2), which is itself guidance to the makers of the regulations. Nothing in it applies to the person except through criteria that the regulations prescribe. |
| s 152.17(4) | src:2537-2538 | encoded | `ei5-payment` `s 152.17(4) the greatest increase in the rate of weekly benefits` | The prescribed percentage or 25% of the person's self-employed earnings for the year divided by 52. |
| s 152.17(5) | src:2539-2540 | encoded | `ei5-payment` `s 152.17(5) the maximum rate of weekly benefits` | 55% of the maximum yearly insurable earnings divided by 52. |
| s 152.18(1) | src:2541-2542 | encoded | `ei5-payment` `s 152.18(1) the amount deducted from the benefits payable for the first three weeks` | The prescribed deduction (reg 39(1), piece er3) is an input; it cannot exceed the earnings. |
| s 152.18(2) | src:2543-2546 | fork | `ei5-payment` `s 152.18(2) the deduction for earnings in a week of unemployment` | F20: rounding of the total. |
| s 152.18(2.1) | src:2547-2548 | encoded | `ei5-payment` `ss 152.16(2) and 152.18(2.1) the part of the aggregate taken into account` |  |
| s 152.18(3) | src:2549-2559 | fork | `ei5-payment` `s 152.18(3)(a) the amount to be deducted for undeclared earnings` and `s 152.18(3)(b) the amounts deducted in consecutive weeks` | F21; the Commission's opinion that the person knowingly failed to declare is a BOOLEAN input. |
| s 152.19(1) | src:2560-2561 | fork | `ei5-payment` `ss 152.19(1) and (2) the deduction for working days on which the person is not entitled` | F20: one fifth of the rate is rounded. |
| s 152.19(2) | src:2562-2563 | fork | `ei5-payment` `ss 152.19(1) and (2) the deduction for working days on which the person is not entitled` | F20. |
| s 152.2 | src:2564-2567 | encoded | `ei5-payment` `s 152.2 the person is not entitled to receive benefits for the period` | An inmate of a prison or similar institution, or not in Canada, unless a regulation provides otherwise (regs 54 and 55.01, piece er3). |
| heading "Premium" | src:2569 | inert | - | A pure title: the division heading above s 152.21. |
| s 152.21(1) | src:2570-2571 | encoded | `ei5-premium` `s 152.21(1) the self-employment premium for the year` and `s 152.21(1) and (3) a premium is required to be paid in respect of the year` | The rate (ss 66 and 66.32, piece ei3) is an input. A premium is not rounded by s 152.01(5): F20. |
| s 152.21(2) | src:2572-2576 | encoded | `ei5-premium` `s 152.21(2) the amount on which the premium is calculated` | The lesser of the self-employed earnings and the maximum less insurable earnings. |
| s 152.21(3) | src:2577-2580 | encoded | `ei5-premium` `s 152.21(1) and (3) a premium is required to be paid in respect of the year` | The year of entry and the year of termination are included, whatever the date. |
| heading "Self-employed Earnings and Collection of Premiums" | src:2582 | inert | - | A pure title: the division heading above s 152.22. |
| s 152.22(1) | src:2583-2584 | encoded | `ei5-premium` `s 152.22(1) the day on or before which the return of self-employed earnings must be filed without notice or demand` and `s 152.22(1) the person's representative must file the return` | The Income Tax Act's due date is an input. |
| s 152.22(2) | src:2585-2587 | encoded | `ei5-premium` `s 152.22(2) the day on or before which the return demanded must be filed` | The days count from the day of service (keel F4). |
| s 152.22(3) | src:2588 | encoded | `ei5-premium` `s 152.22(3) the administrator of the self-employed person's affairs must file the return` | A duty on a person other than the self-employed person. |
| s 152.22(4) | src:2589-2590 | encoded | `ei5-premium` `s 152.22(4) the return contains the information required` |  |
| s 152.23 | src:2591-2592 | encoded | `ei5-premium` `s 152.23 the return contains the estimate required` |  |
| s 152.24 | src:2593-2594 | encoded | `ei5-premium` `s 152.24 the person who filed the return is owed an assessment and a notice of assessment` | A duty of the Minister of National Revenue to the person. |
| s 152.25(1) | src:2595-2596 | encoded | `ei5-premium` `s 152.25(1) the day on or before which the whole premium must be paid` | NOTHING when the person must pay instalments of income tax. |
| s 152.25(2) | src:2597-2601 | fork | `ei5-premium` `s 152.25(2) the amount payable on or before December 31` and `ss 152.25(2) and (3) the remainder of the premium payable on or before the balance-due day` | F24: who chooses between (a) and (b). |
| s 152.25(3) | src:2602-2613 | fork | `ei5-premium` `s 152.25(3)(a) each of the four instalments`, `s 152.25(3)(b)(i) each of the instalments of March 15 and June 15`, `s 152.25(3)(b)(ii) each of the instalments of September 15 and December 15`, `s 152.25(3) the days on or before which the instalments of the year are due` and `ss 152.25(2) and (3) the instalment is required` | F24. No instalment is required that would fall due after the person's death. |
| s 152.26(1) | src:2614-2615 | fork | `ei5-premium` `s 152.26(1) the difference on which interest is payable` and `s 152.26(1) the period for which interest is payable` | F23: the amount of interest is the Income Tax Act's. |
| s 152.26(2) | src:2616-2617 | fork | `ei5-premium` `s 152.26(2) the amount of the instalment on which interest is payable` and `s 152.26(2) the period for which interest on the unpaid instalment is payable` | F23, F26. |
| s 152.26(3) | src:2618-2622 | encoded | `ei5-premium` `s 152.26(3) the instalment on which interest is calculated for a farmer` | The least of two thirds of (a), two thirds of (b), and the notice amount (c). |
| s 152.26(4) | src:2623-2628 | encoded | `ei5-premium` `s 152.26(4) the least total of the instalments required by the instalment day` | The least total by that day among (a), (b), (c) and (d). |
| s 152.26(5) | src:2629-2630 | inert | - | A power of the Minister of National Revenue, with the approval of the Governor in Council, to make regulations prescribing a rate for s 152.26(1) and (2). Regulation-making machinery: no regulation was found in the Regulations as deposited, so the rate is not an input of any rule here (F23). |
| s 152.27(1) | src:2631-2632 | encoded | `ei5-premium` `s 152.27(1) the penalty for failing to file a return` and `s 152.27(1) the Minister of National Revenue may reduce or remit the penalty` | 5% of the unpaid part of the premium at the expiry of the filing time. |
| s 152.27(2) | src:2633-2634 | encoded | `ei5-premium` `s 152.27(2) the penalty for failing to file a return required by subsection 152.22(3)` | $5 a day to a maximum of $50. |
| s 152.28(1) | src:2635-2636 | encoded | `ei5-premium` `s 152.28(1) the provision of the Income Tax Act applies to the premium as though it were tax` |  |
| s 152.28(2) | src:2637-2640 | inert | - | A power of the Minister of National Revenue, with the approval of the Governor in Council, to make regulations exempting a provision of Divisions I and J of Part I of the Income Tax Act from s 152.28(1) or applying it with modifications. Regulation-making machinery; no such regulation was found, and the rule for s 152.28(1) takes "a regulation provides otherwise" as an input. |
| s 152.29 | src:2641-2642 | encoded | `ei5-premium` `s 152.29 the part of the payment applied in payment of the premium` and `s 152.29 the part of the payment left to be applied in payment of tax under the Income Tax Act` | Section 228 of the Income Tax Act and s 37 of the Canada Pension Plan are outside the texts. |
| s 152.3(1) | src:2643-2646 | encoded | `ei5-premium` `s 152.3(1) the excess of the amount paid over the premium` and `s 152.3(1)(b) the Minister of National Revenue shall make the refund` | (a) the Minister may refund without an application; (b) shall refund if applied for in writing within three years after the end of the year. |
| s 152.3(2) | src:2647-2648 | encoded | `ei5-premium` `s 152.3(2) subsections 96(11) to (13) apply to the refund` | The content of s 96(11) to (13) is piece ei3's. |
| heading "Application of other Provisions" | src:2650 | inert | - | A pure title: the division heading above s 152.31. |
| s 152.31(1) | src:2651-2652 | encoded | `ei5-other-provisions` `s 152.31(1) a provision of the Act applies to this Part` | Sections 5 to 37, 48 and 56 to 65.2 are excluded; the section number is read as a decimal. |
| s 152.31(2) | src:2653-2656 | encoded | `ei5-other-provisions` `s 152.31(2)(a) subsection 86(1) applies to the person as it applies to an employer` and `s 152.31(2)(b) subsection 88(5) applies to the matter as though its reference to this Part were a reference to Part VII.1` |  |
| s 152.31(3) | src:2657-2661 | encoded | `ei5-other-provisions` `s 152.31(3) section 102 applies to the matter` |  |
| s 152.31(4) | src:2662-2665 | encoded | `ei5-other-provisions` `s 152.31(4) section 125 applies to the matter` |  |
| heading "Delegation" | src:2667 | inert | - | A pure title: the division heading above s 152.311. |
| s 152.311 | src:2668-2669 | inert | - | Machinery: the Minister of National Revenue may authorize an officer or a class of officers to exercise the Minister's powers or perform the Minister's duties under this Part. It decides nothing for the person, whose rights and duties are the same whoever exercises the Minister's side. |
| heading "Offences" | src:2671 | inert | - | A pure title: the division heading above s 152.32. |
| s 152.32 | src:2672-2673 | fork | `ei5-other-provisions` `s 152.32 the person is guilty of an offence and liable on summary conviction to a fine`, `s 152.32 the least fine on summary conviction`, `s 152.32 the greatest fine on summary conviction` | F25. |
| heading "Regulations" | src:2675 | inert | - | A pure title: the division heading above s 152.33. |
| s 152.33 lead-in | src:2676-2677 | inert | - | Regulation-making machinery: the Commission may, with the approval of the Governor in Council, make the regulations listed in paragraphs (a) to (f). The regulations that exercise it, as far as the Regulations deposited show, are named in the rows below and the cross-reference table; each is an input of the rule it feeds. |
| s 152.33(a) | src:2678 | inert | - | Regulation-making machinery: power to define or determine a week of unemployment for a self-employed person. Exercised by regs 30.1 and 30.2 (piece er2); the result is the input of s 152.01(4). |
| s 152.33(b) | src:2679 | inert | - | Regulation-making machinery: power to set out the circumstances in which agreements are deemed terminated (s 152.02(4)). No such regulation was found in the Regulations as deposited; the circumstance is an input of s 152.02(4). |
| s 152.33(c) | src:2680 | inert | - | Regulation-making machinery: power to fix, for any year, an amount (not less than $6,000) for s 152.07(1)(d)(i), or a manner of determining it. Exercised by reg 11.1 (piece er1); the figure is the input of s 152.07(1)(d)(i). |
| s 152.33(d) | src:2681 | inert | - | Regulation-making machinery: power to determine the average number of weeks of benefits for s 152.07(3)(b). Exercised by reg 13(2) (piece er1); the figure is an input of s 152.07(3)(b). |
| s 152.33(e) | src:2682 | inert | - | Regulation-making machinery: power to specify when self-employed persons are deemed not working for s 152.03(4). Exercised by reg 30.2 (piece er2); the result is an input of s 152.03(4). |
| s 152.33(f) | src:2683 | inert | - | Regulation-making machinery: power to prescribe anything that this Part says is to be prescribed (the prescribed illness, circumstances, requirements, periods, rates, percentages and manners). Each such matter is an input of the rule that uses it; the cross-reference table lists them. |
| heading "Review of this Part" | src:2685 | inert | - | A pure title: the division heading above s 152.34. |
| s 152.34 | src:2686-2687 | encoded | `ei5-other-provisions` `s 152.34 the day five years after the day on which this Part comes into force` and `s 152.34 the party who must cause the review to be conducted` | A duty of the Minister to cause a review; the only fact is the day, derived from the commencement day (an input: the Act's text does not name it). |

## Fork register

Twenty-six places where the text does not settle the reading.
Each row gives what the text leaves open, the readings I saw, the one I took, and the text that licenses it; the rule that carries the reading is named in the coverage table (the row for the provision points here by its identifier).
"No ambiguities found" is not claimed: this register is the result of reading every subsection for five kinds of gap.

- **The day a condition is tested.** F11 (citizenship or residence), F13 (qualification and the 12 months), F14 (the 260 weeks), F6 (the day the agreement ends).
- **Cumulative or alternative.** The conditions of s 152.07(1) are cumulative (the text joins them with "and"), so they are not a fork; those of ss 152.05(14), 152.06(6), 152.31(3) and 152.31(4) are alternatives ("or"), also not a fork.
  Where the text joins limbs ambiguously the fork is recorded (F15, F16).
- **Two rules that overlap.** F5 (a deemed termination with a notice, and the two limbs of s 152.02(6)), F18 (the limbs of s 152.11(9)), F15 (a violation in two classes), F19 (the exceptions of s 152.11(6) to (6.2)).
- **Counting.** F1, F8, F9, F10 (months, weeks and the day a period ends), F20 (rounding), F23 and F26 (interest), F25 (the fine).
- **What the text leaves unsaid or hands elsewhere.** F2, F3, F4, F7, F12, F17, F21, F22, F24.

A reading taken here is a choice that can be reversed in one rule; the seat questions and the cases follow the same reading.

| id | provision | what the text leaves open | the readings seen | the reading taken | the text that licenses it |
| --- | --- | --- | --- | --- | --- |
| F1 | s 152.01(1) "balance-due day" (src:2114-2116) | "died after October in the year and before May in the immediately following year": is the boundary a month or a day? | Month: death in November or December of the year, or January to April of the next (31 October is in October, so not after it); or day: after 31 October, which is the same days. | Read by calendar month; 31 October is "any other case" and 1 November is (a). The two readings coincide, so the boundary is not really open; the tests pin both sides. | (a) and (b) of the definition, lines 2115-2116. |
| F2 | s 152.01(1) "self-employed person" (b) (src:2124) | "is employed but does not have insurable employment by reason of paragraph 5(2)(b)": must the employment be insurable but for 5(2)(b)? | (i) any employment that 5(2)(b) catches; (ii) only employment that would otherwise be insurable employment under s 5(1). | (ii): an extra BOOLEAN input `the employment would be insurable employment but for paragraph 5(2)(b)`, with the keel rule for 5(2)(b) for the 40% test. | "by reason of" (line 2124) makes 5(2)(b) the cause of the lack of insurable employment. |
| F3 | s 152.01(2) (src:2128-2136) | Whether self-employed earnings can be negative when losses exceed business income. | (i) negative as computed; (ii) floored at zero. | No floor: (A) minus (B) as written, so 700 less 3,000 is -2,300; the text states no floor and none is added. | Lines 2131-2133: "minus ... all losses". |
| F4 | s 152.02(3) (src:2150) | What follows if an agreement is not in the form or does not meet a condition the Commission fixed. | The text is silent. | The rule says only whether the agreement is in the form and meets the conditions fixed; no consequence is encoded. | Line 2150: "may fix the form and the conditions". |
| F5 | s 152.02(4) to (6) (src:2152-2158) | Overlaps: a deemed termination (5) together with a notice (6); and (6)(a) together with (6)(b). | Deemed date wins; notice date wins; earlier wins. For (6)(a)/(b): either label, same result (the agreement continues). | The earlier day governs (an agreement ends once); when (6)(a) and (6)(b) both apply the rule reports (6)(a), the first named. | Lines 2152-2158; the text ranks neither. |
| F6 | s 152.02(2), (6) (src:2148, 2156) | Whether the agreement is in force on the day on which it "is terminated". | In force through that day; not in force on that day. | Not in force on that day or after: it is "terminated on" that day. | Line 2156: "the agreement is terminated on December 31". |
| F7 | ss 152.03(2), (3), 152.04(3), (4) and the like (src:2168, 2170, 2184, 2188) | Whether a reduction or a deduction can take the benefit below zero. | (i) negative payment; (ii) stops at zero. | Stops at zero (`max 0`). The alternative reading yields a negative "benefit" (a payment from the claimant to the Commission), which the text has no concept of: it says "reduced or eliminated" and "deducted from those benefits", and an amount that has been eliminated is zero; recovery of money is Part VI's business, not these subsections'. No default is invented: the floor is the end of the reduction the text itself describes. | Lines 2167-2170; the text states no floor, so this is assumed, not ruled. |
| F8 | ss 152.04(2), 152.05(2), 152.06(3), 152.061(3), 152.062(3) (src:2176-2182, 2202-2204, 2247-2254) | Whether a period that "ends n weeks after the week in which" an event happens ends at the start or the end of the week n weeks later, and whether it is made of whole weeks. | Ends on the same weekday n weeks later; ends at the end (Saturday) of the nth week after the event's week; ends at the start (Sunday). | Whole weeks, Sunday to Saturday (s 2(1) "week"): the period begins on the Sunday of its first week and ends on the Saturday of the week n weeks after the event's week, so a period "ending 17 weeks after" a week covers that week and the 17 after it. Benefits are paid by the week (week of unemployment), which is why whole weeks were taken. | s 2(1) "week" (line 50), 152.04(2) "for each week of unemployment in the period". |
| F9 | s 152.04(2) (src:2176-2182) | How to read "the earlier of ... the week in which her confinement occurs" before the confinement has occurred. | Refuse until it occurs; use the expected week for both; use only the 12-week limb. | While confinement has not occurred (NOTHING), the week of confinement is taken to be the week it is expected, so the period shown is the one the expected date gives; once it occurs the actual week is used. | The words "the week in which her confinement occurs" presuppose that it has occurred. |
| F10 | ss 152.06(3)(b)(iii), 152.061(3)(b)(iii), 152.062(3)(b)(iii) (src:2254, 2291, 2328) | "the period of 52 weeks following the first day of the week" - on which day does it end? | The Sunday 52 weeks later; the Saturday before it (364 days after the first Sunday, minus one). | Ends on the Saturday 52*7 - 1 = 363 days after the first Sunday, which is also "the last day of the week in which" that period ends, so the three kinds of end (exhaustion, death, 52 weeks) are all Saturdays. | Line 2251: "ends on the last day of the week in which any of the following occurs". |
| F11 | s 152.02(1) (src:2146) | The day on which "is a Canadian citizen or a permanent resident" is tested: when the agreement is entered into, when the claim is made, or each day. | At the agreement; at the claim; throughout. | Timeless: the rule takes the three facts as they stand on the day the question is asked and ties them to no date. A caller who needs the agreement-day reading asks the question as of that day. | The text says "applies in respect of every self-employed person who is a Canadian citizen or a permanent resident ... who has entered into an agreement" without a date (line 2146). |
| F12 | s 152.03(1.1) (src:2166) | Whether the person to whom benefits are payable under ss 152.05 to 152.062 must still be ill and unable to work. | (i) any such person is entitled, ill or not; (ii) only an ill person who is unable to work. | (ii): (1.1) relaxes only two things, ceasing to work because of the illness and would otherwise be working; subsection (1) still says "while unable to work as a self-employed person for that reason", and (1.1) says the person "is entitled to benefits under subsection (1)". | Lines 2164 and 2166. |
| F13 | s 152.07(1)(a) to (c) (src:2350-2353) | The day on which "qualifies for benefits" is tested, and when "12 months have expired". | At the agreement's anniversary day; the day after it; at the initial claim; at the day the benefit period begins. | Tested on a day the caller names (the day of the initial claim, by s 152.1(1)); twelve months expire on the same day of the month twelve months later (`add months`, clamped), so a person who entered into the agreement on 10 January 2026 qualifies under (a) from 10 January 2027. | Line 2351 "at least 12 months have expired since the day"; s 152.1(1) (line 2403) "who qualifies under section 152.07 makes an initial claim". |
| F14 | s 152.07(1)(d) and (5)(b) (src:2355, 2359, 2381) | How the 260 weeks are counted: "in the 260 weeks before making their initial claim" and "within 260 weeks after the person accumulates another violation". | Includes or excludes the end days; 260 weeks as 1,820 days. | The window before the claim is the 1,820 days ending on the day before it; the window after another violation runs from that day to the 1,820th day after it, both counted (the keel's F4 for "within n days after d"). | Lines 2355, 2359, 2381; the Interpretation Act is not deposited. |
| F15 | s 152.07(5) (src:2376-2381) | A violation that falls under both (a) (by value) and (b) (within 260 weeks of another). | (a) governs; (b) governs; both. | (b) governs: it names a class of its own ("it is a subsequent violation") and says "even if the acts or omissions on which it is based occurred before". | Line 2381. The same ordering is used in s 7.1(5) (piece ei1), which the keel quotes. |
| F16 | s 152.07(1)(d)(ii) (src:2359-2363) | "the violation": which one counts when the person has accumulated more than one in the 260 weeks. | The most serious; the latest; the first. | The text does not say. The rule takes the class as one input, `the class of the violation accumulated in the 260 weeks ...`; the caller supplies the class that applies. | Line 2359: "if the person has accumulated a violation" and "if the violation is a minor violation" (singular). |
| F17 | s 152.11(14), (15), (16) (src:2467, 2471, 2473) | By how many weeks the benefit period is extended under (14), and how the caps of (15) and (16) combine. | (14) fixes the length itself; (14) gives only a right to be paid up to the maximum total; (16) always applies; (16) applies only when (14) is the sole extension. | (14) states the aim ("extended so that those benefits may be paid up to that maximum total number of weeks") but no number, so the length rule takes the extension as an input. (15)'s 104 weeks applies to every extension under (11) to (14.1); (16) applies, with "Subject to subsection (15)", only "unless the benefit period is also extended under any of subsections (11) to (13)", so it is applied when (14) is the only one of (11) to (14) in play, and the lesser of the two limits governs. | Lines 2467, 2471, 2473: "Subject to subsection (15), unless the benefit period is also extended under any of subsections (11) to (13)". |
| F18 | s 152.11(9) (src:2447-2453) | When paragraph (c) ("requests ..., makes a new initial claim for benefits, and qualifies") has occurred, and which of (a), (b), (c) is "first". | (c) occurs at the request; at the new claim; when the last of the three has happened. | (c) occurs on the day the last of the three has happened, because the paragraph lists them as one cumulative event; the benefit period ends on the earliest day among (a), (b) and (c). | Lines 2447 ("any of the following first occurs") and 2450-2453. |
| F19 | s 152.11(6) to (6.2) (src:2424-2437) | Whether the exceptions stop the antedating of a late claim of any kind or only of the claim referred to in the section. | Any late claim; only a claim referred to in s 152.06, 152.061 or 152.062. | The rules for (4) and (5) take one BOOLEAN input, "the claim is not regarded as made on an earlier day under (6), (6.1) or (6.2)", that the caller computes with the shared rule for a caring claim and sets FALSE for any other claim. | Lines 2424, 2429, 2434: "A claim for benefits referred to in section 152.06 ...". |
| F20 | s 152.01(5) applied in ss 152.16, 152.17, 152.18, 152.19 (src:2142, 2526, 2538, 2540, 2544-2546, 2561-2563) | Which amounts "equal to a percentage or fraction of earnings or benefits in a period" are rounded to the nearest dollar, and at what step. | Round every intermediate figure (the weekly average, each threshold); round only the figure that is paid or deducted; round nothing. | Round the result that is paid or deducted, once: the weekly rate (55% or 33% of the held aggregate divided by 52), the greatest increase and the maximum rate of s 152.17, the whole deduction of s 152.18(2), one fifth of the rate under s 152.19. A threshold that is only compared (90% of the weekly figure, the $50 and the 25% of the rate in s 152.151) is not rounded. The keel's rounding rule is the one called, with the higher dollar when equidistant. | s 152.01(5) (line 2142) speaks of "a reference ... to an amount equal to a percentage or fraction of earnings or benefits in a period"; the choice of the end result is assumed, not ruled. |
| F21 | s 152.18(3)(b) (src:2557-2559) | What the last week of the deduction for undeclared earnings takes, and what happens if the weeks of benefits paid run out first. | The last week takes a full week's benefits; only the remainder; the unrecovered balance is carried. | Each week takes the lesser of what is still to be deducted and that week's benefits paid; if the weeks given run out, the amounts end there and the balance is not applied (it is not in this text what becomes of it). | Line 2559: "the amount deducted in each consecutive week equals the person's benefits paid for that week", and line 2551: "the amount of the undeclared earnings" is what "shall be deducted". |
| F22 | s 152.151(1) (src:2518-2520) | Whether "the person's rate of weekly benefits" includes the family supplement of s 152.17. | With the supplement; without it. | The caller passes the rate; the rule does not say which. For the seat layer the rate asked for is the rate of s 152.17 (with the supplement), because s 152.17(1) says "The rate of weekly benefits ... shall be increased by the amount of a family supplement". | Lines 2518-2520 and 2532. |
| F23 | s 152.26(1) and (2) (src:2615, 2617) | How the interest is calculated, and whether the day of payment and the balance-due day are both counted. | Simple interest; compound interest; the Income Tax Act's method; end days in or out. | The rules give the difference on which interest is payable and the period, from the balance-due day to the day of payment, both days named; the interest itself is not computed, because s 152.28(1) applies the Income Tax Act's provisions on interest to the premium and the prescribed rate is made under s 152.26(5) (no such regulation found in the Regulations as deposited). | Lines 2615, 2636, 2630. |
| F24 | s 152.25(2), (3) (src:2597-2613) | Who chooses between "(a) the premium ... as estimated by the person; or (b) the premium ... for the preceding year" (farmers) and between the two schedules (a) and (b) (other persons). | The person chooses; the Minister chooses; the lesser or the greater is required. | The person chooses: a BOOLEAN input says which basis they pay by. The text offers the alternatives and does not say that either is required. | Lines 2598-2600 and 2603-2612 ("or"). |
| F25 | s 152.32 (src:2673) | "a fine of not less than $25 a day for each day the offence continues, to a maximum of $1,000": whether the maximum caps the fine as a whole or only the minimum. | Maximum fine $1,000; the minimum fine is capped at $1,000; both. | The fine is at least $25 for each day but never more than $1,000: two rules, `the least fine` (25 a day, held to 1,000) and `the greatest fine` (1,000). | Line 2673. |
| F26 | s 152.26(2) (src:2617) | The period for the interest on a missed instalment ends at "the beginning of the period in respect of which the person is liable to pay interest ... under subsection (1)": is that day counted in both periods? | Counted in both; counted in one only. | The period of (2) is named to end on that day; the text does not say whether the day is counted twice and the rule does not decide it. | Line 2617. |

## Cross-references out of my ranges

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 152.01(1) "disentitled" | s 49 (src:933), s 50 (src:941) | ei2 | `not entitled under section 49`, `not entitled under section 50` |
| s 152.01(1) "disentitled" | the Regulations, "under the regulations" | er1 to er6 | `not entitled under the regulations` |
| s 152.01(1) "self-employed person" | Part VIII regulations (fishing) | ei4 | `regulations made under Part VIII apply to the individual` |
| s 152.01(1) "self-employed person" | s 5(4)(c), reg 6 (inclusion by regulation) | er1 | `the individual's employment is included in insurable employment by a regulation made under paragraph 5(4)(c)` |
| s 152.01(1) "self-employed person" (b) | s 5(2)(b) | keel (`eia-core-insurable-employment`) | called, not input: `s 5(2)(b) employment of a person by a corporation they control` |
| s 152.01(2)(a)(i) | the Income Tax Act (income and losses) | outside the texts | `ei5 Business of the year` figures; `all losses ... sustained in the year` |
| s 152.01(2)(a)(ii) | s 5(6)(c), regs 7 and 8 | er1 | `their income for the year from employment described in paragraph 5(6)(c) ...` |
| s 152.01(2)(b) | Part IV insurable earnings (s 2(1) "insurable earnings") | ei3 | `the person's insurable earnings for the year had the employment not been excluded from insurable employment` |
| s 152.01(3) | the Indian Act s 2(1); Income Tax Act s 81(1)(a) | outside the texts | `ei5 income of the business ... computed without reference to paragraph 81(1)(a)`, the Indian-on-a-reserve flag |
| s 152.01(4) | regs 30.1 and 30.2 (week of unemployment) | er2 | `the week is a week of unemployment as defined or determined in accordance with the regulations` |
| s 152.02(4) | s 152.33(b); no regulation found setting circumstances | er1 to er6 | `any of the circumstances set out in the regulations exists` |
| s 152.02(4) | reg 9.01 (notice in writing) | er1 | `the individual gives notice to the Commission in the prescribed form and manner` |
| s 152.02(4) | s 152.02(4) "prescribed circumstances"; none found | er1 to er6 | `any of the prescribed circumstances exists` |
| s 152.02(5) | s 152.33(b) prescribed date; none found | er1 to er6 | `the prescribed date` |
| s 152.02(6)(b) | reg 9.02 (withdrawal in writing) | er1 | `the day on which the individual withdrew the notice in the prescribed manner` |
| s 152.03(1) and (1.1) | reg 40(4) (prescribed illness, injury or quarantine) | er3 | `has a prescribed illness, injury or quarantine` |
| s 152.03(4) | reg 30.2 (deemed not working) | er2 | `were it not for the illness, injury or quarantine the person would be deemed in accordance with the regulations to be not working` |
| ss 152.03(1.1), (4) | ss 152.05 to 152.062 (this Part) | ei5 | `benefits are payable to the person under any of sections 152.05 to 152.062`: the caller passes the result of the rules of this piece |
| ss 152.03(2), 152.04(3), 152.05(11), 152.06(9), 152.061(11), 152.062(9) | regs 76.36 to 76.42 (reduction of benefits for provincial benefits) | er4 | `the reduction prescribed` |
| ss 152.03(3), 152.04(4) | s 69(1) and the wage-loss plan regulations (regs 60 to 74) | ei3, er4 | `the allowances, money or other benefits payable to the person for that week under such a plan` |
| s 152.04(1) | reg 41(1) (proof of pregnancy) | er3 | `proves her pregnancy` |
| s 152.05(1.2) | s 23 (parental benefits for insured persons) | ei1 | `benefits have been paid under section 23 in respect of the same child or children` |
| s 152.05(1.3), (12), (13), (15) | ss 22 and 23 (the other claimant) | ei1 | the other person's election and claim as plain inputs |
| s 152.05(6) | s 152.11(16) | ei5 (ei5-benefit-period) | `the maximum benefit period calculated under subsection 152.11(16), in weeks` |
| s 152.05(12) | reg 41.6 (division when claimants cannot agree) | er3 | `the weeks I am to receive under the prescribed rules` |
| s 152.05(14)(d) | s 152.05(14)(d) "prescribed requirements"; none found | er1 to er6 | `the person or another self-employed person meets the prescribed requirements` |
| ss 152.06(1), 152.061(1), 152.062(1) | reg 1(3), (6), (7) (family member, critically ill child, critically ill adult) | er1 | `the person ... is a family member` |
| ss 152.06(2), 152.061(2), 152.062(2) | reg 41.2 (practitioners abroad) | er3 | `is a member of a prescribed class of medical practitioners`, `the circumstances set out in the regulations exist` |
| s 152.06(4) | s 152.06(4) shorter period; none found | er1 to er6 | `the shorter period prescribed, in weeks, if one is prescribed` |
| s 152.06(3.1) | s 50(8.1) | ei2 | `section 50(8.1) requires a further certificate` |
| ss 152.06(5)(c), 152.061(5)(c), 152.062(4)(c) | "other circumstances set out in the regulations"; none found | er1 to er6 | `the claim is made in any other circumstances set out in the regulations` |
| ss 152.06(6)(c), 152.061(6)(c), 152.062(5)(c) | "prescribed requirements"; none found | er1 to er6 | `... meets the prescribed requirements` |
| ss 152.06(7), 152.061(8), 152.062(6) | reg 41.6 | er3 | `the weeks I am to receive under the prescribed rules` |
| ss 152.061(10), (10.1), 152.062(8) | ss 23.1, 23.2, 23.3 (insured persons' benefits) | ei1 | the other benefits and their periods as plain inputs |
| s 152.07(1)(a) | reg 76.43 (condition deemed satisfied in the interprovincial case) | er4 | `the Regulations deem the condition satisfied` |
| s 152.07(1)(a) | "a period has been prescribed for the purpose of this section"; none found | er1 to er6 | `the period prescribed for this section, in months, if one is prescribed` |
| s 152.07(1)(c) | reg 14.01 (interruption of earnings of a self-employed person) | er1 | `the person has had an interruption of earnings from self-employment` |
| s 152.07(1)(d)(i)(C) | reg 11.1 and s 152.33(c) (the $6,000 as adjusted) | er1 | `the amount fixed or determined in accordance with the regulations for that qualifying period, if any` |
| s 152.07(1)(d)(ii) | "the prescribed multiplier"; none found | er1 to er6 | `the prescribed multiplier for that class, if one has been prescribed` |
| s 152.07(2)(a) | ss 38 and 41.1 | ei2 | `one or more penalties are imposed on the person under section 38 ...` |
| s 152.07(2)(b) | ss 135 and 136 | ei4 | `the person is found guilty of one or more offences under section 135 or 136 ...` |
| s 152.07(2)(c) | the Criminal Code | outside the texts | `the person is found guilty of one or more offences under the Criminal Code ...` |
| s 152.07(3)(b) | reg 13(2) (average number of weeks of benefits) | er1 | `the average number of weeks of benefits under this Part, as determined under the regulations` |
| s 152.07(5) | s 41.1 (warning instead of a penalty) | ei2 | `a warning was imposed for the violation` |
| s 152.07(6) | s 7.1 (violations of an insured person) | ei1 | `the violation was accumulated by the individual under section 7.1` |
| s 152.07(7) | s 7.1(1) and the Part VIII regulations | ei1, ei4 | `the number of earlier initial claims in which the violation was taken into account and the individual qualified for benefits` |
| s 152.08(1) | s 152.11(1) (the day the benefit period begins) | ei5 (ei5-benefit-period) | `the day on which the benefit period begins`: the caller passes the result of `s 152.11(1)` |
| s 152.09(1) | Part I qualification (ss 7, 7.1) | ei1 | `the individual qualifies for benefits under Part I as an insured person` |
| s 152.09(1) | reg 25.1 (election in writing) | er2 | `the Part elected in the prescribed manner at the time of making the initial claim, if any` |
| s 152.1(1) | reg 30.1, 30.2 (week of unemployment) | er2 | `the week is a week of unemployment of the self-employed person` |
| s 152.1(2)(a) | s 50 (initial claims; proof of qualification) | ei2 | `the person makes an initial claim for benefits in accordance with section 50 ...` |
| s 152.11(1) | reg 14.01 (day of the interruption of earnings) | er1 | `the day on which the interruption of earnings occurs` |
| s 152.11(5) | the time prescribed for making a claim | er2 | `the claim is made after the time prescribed for making the claim` |
| s 152.11(6)(c), (6.1)(c), (6.2)(c) | "other circumstances set out in the regulations"; none found | er1 to er6 | `the claim is made in any other circumstances set out in the regulations` |
| s 152.11(9)(a) | s 152.14 (maximum weeks paid; no further benefits payable) | ei5 (ei5-payment) | `the day on which no further benefits are payable ...`: the caller passes the day |
| s 152.11(14), (16) | s 152.14(1) maxima (35, 61, 26, 15, 26, 35, 15) | ei5 (ei5-payment) | `the maximum total number of weeks established for those reasons`, `the maximum numbers of weeks ... for each of the benefits paid` |
| s 152.11(13) | s 152.05(2) (the period; hospitalized child) | ei5 (ei5-parental) | `the number of weeks during which the child or children are hospitalized ...` |
| s 152.16(1)(a) | s 152.01(2) (self-employed earnings of the qualifying period) | ei5 (ei5-interpretation) | `the person's self-employed earnings for the qualifying period`: the caller passes the result |
| s 152.16(1)(b) | Part IV insurable earnings (s 2(1) "insurable earnings"); reg 24.3 (prescribed insurable earnings left out) | ei3, er2 | `the person's insurable earnings from employment for the qualifying period, calculated without taking into account prescribed insurable earnings` |
| ss 152.16(2), 152.17(5), 152.18(2.1) | s 4 (maximum yearly insurable earnings) | keel (`eia-core-maximum-earnings`) | `the maximum yearly insurable earnings for the year`: the published figure is outside the text |
| s 152.17(1) | reg 34 (family supplement; low-income family eligibility criteria) | er2 | `the family supplement determined in accordance with the regulations`, `the person establishes ... prescribed low-income family eligibility criteria` |
| s 152.17(4) | "the prescribed percentage"; none found | er1 to er6 | `the prescribed percentage, if one is prescribed` |
| s 152.18(1) | reg 39(1) (deduction of earnings in the waiting period) | er3 | `the amount the regulations prescribe to be deducted` |
| s 152.18(3) | "the Commission's opinion" (knowingly failed to declare) | the Commission's judgment | `in the opinion of the Commission, the person knowingly failed to declare the earnings` |
| s 152.19 | reg 32 (a working day is any day except Saturday and Sunday) | er2 | `the number of working days on which the person is not entitled to receive benefits` |
| s 152.2 | regs 54(2) and 55.01 (inmates on parole; absence from Canada) | er3 | `a regulation otherwise provides for the person's case` |
| s 152.14(7) | "the minimum prescribed number of weeks"; none found | er1 to er6 | `the minimum prescribed number of weeks has elapsed` |
| s 152.14(6) | s 152.06(4) shorter period; none found | er1 to er6 | `the shorter period prescribed for the purposes of subsection 152.06(4), in weeks, if one is prescribed` |
| s 152.21(1) | ss 66 and 66.32 (premium rate) | ei3 | `the premium rate set under section 66 or 66.32` |
| s 152.21(2) | Part IV insurable earnings; s 4 | ei3, keel | `the person's insurable earnings for the year, if any`, `the maximum yearly insurable earnings for the year` |
| s 152.22(1) | the Income Tax Act, return of income under Part I | outside the texts | `the day on which the person's return of income under Part I of the Income Tax Act is required to be filed ...` |
| s 152.25(1) | ss 155 and 156 of the Income Tax Act (instalments) | outside the texts | `the person is required by section 155 or 156 of the Income Tax Act to pay instalments ...` |
| s 152.25(1) | s 152.01(1) "balance-due day" | ei5 (ei5-interpretation) | `the person's balance-due day for the year`: the caller passes the result |
| s 152.26(1), (2), (5) | the rate of interest prescribed under s 152.26(5); none found | er1 to er6 | no rate input: the rules stop at the amount and the period (fork F23) |
| s 152.27(1) | s 162(1), (2) of the Income Tax Act | outside the texts | `the person is liable to a penalty under subsection 162(1) or (2) of the Income Tax Act ...` |
| s 152.28 | the Income Tax Act Divisions I and J of Part I, Part XV, s 248(7), (11); s 152.28(2) regulations; none found | outside the texts | four BOOLEAN inputs |
| s 152.29 | s 228 of the Income Tax Act; s 37 of the Canada Pension Plan | outside the texts | `the part of the payment that would be applied under section 228 of the Income Tax Act in payment of tax` |
| s 152.3(2) | s 96(11) to (13) | ei3 | `the refund is made under subsection 152.3(1)` |
| s 152.31(2)(b) | s 88(5) | ei3 | `the matter is one to which subsection 88(5) applies` |
| s 152.31(3), (4) | ss 102, 106(4), 125, 135(1), 136(2) | ei3, ei4 | the matters as BOOLEAN inputs |
| s 152.34 | the day Part VII.1 comes into force (not in the text; s 190, piece ei6, does not name it) | ei6 | `the day on which this Part comes into force` |
| s 152.15 | regs 77.996 and 77.9992 (the Commission may waive the waiting period in respect of any benefit period that begins from 30 March 2025 to 10 October 2026, and from 11 October 2026 to 9 October 2027) | er5 | none: the regulations speak of "the waiting period" in "any benefit period" and name neither Part VII.1 nor s 152.15, so the waiver is not applied; the rule for s 152.15 takes no waiver as an input (see "What the text turns out to say") |
| s 152.18(2) | regs 77.95(4), 77.97(4) and 77.99(4) (Pilot Projects 18, 19 and 20 each add a subsection (2.1) to s 152.18) | er5 | none: each of the three sections ceases to have effect (1 August 2015, 6 August 2016, 11 August 2018), so s 152.18(2) is applied as the Act states it |
| s 152.02(1), 152.07(1)(a) | 2009, c. 33, ss 18 and 19, in the Related Provisions (src:3641-3648): agreements entered into during a window before section 16 of that Act came into force are deemed entered into on the day it came into force, and a benefit period may begin on or after 1 January 2011 despite 152.07(1)(a) for an agreement entered into between the later of royal assent and 1 January 2010 and 1 April 2010 | ei7 | none: spent transitional rules (they concern agreements of 2010 and benefit periods from 2011); the day section 16 came into force is not in the text; not applied |
| s 152.07(6) | 2009, c. 33, s. 20, in the Related Provisions (src:3649-3651): a violation accumulated under section 7.1 before s 152.07(6) came into force is deemed to be accumulated under s 152.07 on the day the notice of violation was given | ei7 | none: the rule for s 152.07(6) already takes the day of the notice as the day (the same day); the transitional wording is not encoded separately |
| ss 152.03(1.1), 152.05(5.1), 152.09(2), 152.11, 152.14(1), and a new s 152.041 | 2024, c. 15, ss 349 to 355 in the Amendments Not in Force (src:4107-4188): replace 152.03(1.1), add 152.041 (a benefit for responsibilities related to a child's placement or arrival), replace 152.05(5.1), amend 152.09(2), 152.11 and 152.14(1), and continue the present Act for some claimants | ei7 | none: amendments not in force change nothing today; their wording is not merged into any rule of this piece |

## Needs from the core

**Nothing is required of the core for this piece to work.**
Every shared type and function the piece needs, the keel already has, and no keel file was changed.

**Local declarations made under a distinct name**, for the lead to decide whether to promote.
They are specific to Part VII.1 and are not asked for:

- `ei5 Kind of activity the definition of business lists` (nine constructors named `ei5 business - ...`, in `ei5-interpretation`): the kinds of activity s 152.01(1) "business" lists, because the definition is an open list with one exclusion and the rule must return `JUST TRUE` for a listed kind, `JUST FALSE` for an office or employment and `NOTHING` for the rest.
- `ei5 Business of the year` (in `ei5-interpretation`): five figures of one business for s 152.01(2)(a) (income under the Income Tax Act, income without reference to paragraph 81(1)(a), whether the person is an Indian on a reserve, gross revenue, rent).
- `ei5 What becomes of a notice to terminate an agreement` (five constructors, in `ei5-agreement`): the outcomes of s 152.02(6) and (7), one value instead of five yes/no rules.

**Keel names this piece relies on** (a rename in the keel would break these): the types `Reason for benefits`, `Election of maximum weeks`, `Violation class`, `Part of the Act`, `Party`, `Period of days` and their constructors; the functions `YMD` (not in the stable prelude, defined once by the keel), `weeks as days`, `the number of days in`, `s 2(1) the Sunday that begins the week containing`, `s 2(1) the Saturday that ends the week containing`, `s 2(1) the year containing`, `s 6(2) and s 152.01(5) amount rounded to the nearest dollar`, `s 5(2)(b) employment of a person by a corporation they control`, `s 2(1) special benefits`; and, from the standard library's `daydate`, `the earlier of`, `the later of` and `add months` (which clamps to the last day of the month; forks F1 and F13).

**Inputs that other pieces compute** and that the lead can wire at the merge are in the table of cross-references above; the three most used are the week of unemployment (regs 30.1 and 30.2, piece er2), the maximum yearly insurable earnings (s 4, the keel gives the formula and every piece takes the published figure) and the premium rate (ss 66 and 66.32, piece ei3).

## What the text turns out to say

Each entry says what the text shows.
"Asserted." means a test or a seat case asserts the consequence, and the files are named.
An entry without it is a fact about the text that no assertion can state (a gap, a cross-reference, an absence).
Expected values in every assertion were written by hand from the text before the run, and none was changed to match the code: the two seat assertions that first failed were cases I had written the wrong way round (for s 152.11(8)), and I corrected them from the text, not from the output.

1. **The text of Part VII.1 names no day on which it comes into force.**
   Section 152.34 counts "five years after the day on which this Part comes into force".
   The Act's coming-into-force section (s 190, outside this range) does not mention Part VII.1: searching the Act after line 2688 for "Part VII.1" finds it only at src:2723, 2729, 2976, 3647 and 4105, none in s 190.
   The converter drops historical notes, so no enactment, assent or amendment date is in the range.
   The rule for s 152.34 therefore takes the commencement day as an input and adds five years; no value was invented for the day.
   The five-year addition clamps 29 February to 28 February (`add months`).
   Asserted. (`ei5-tests-other-provisions.l4`: a commencement of 31 January 2010 gives 31 January 2015, and one of 29 February 2020 gives 28 February 2025.)

2. **The only dates the range carries are four fixed dates in the required-earnings amounts of s 152.07(1)(d)(i).**
   $5,000 applies to a benefit period beginning from 3 January 2021 to 25 September 2021, $5,289 from 26 September 2021 to 24 September 2022, and otherwise $6,000 or the amount fixed or determined by regulation; each of the four days is a defined value with an `@ref`.
   The first two amounts apply "despite any regulations", so reg 11.1 (piece er1), which adjusts the $6,000 each year from 2012 and not below $6,000, cannot change them.
   Asserted. (`ei5-tests-qualifying.l4`: 2 January 2021 and 25 September 2022 give $6,000, or the regulation amount when one is supplied; 3 January 2021 gives $5,000 and 26 September 2021 gives $5,289 even when a regulation amount of 6,200 is supplied; 25 September 2021 gives $5,000 and 24 September 2022 gives $5,289.)

3. **The Regulations as deposited do not set the following, so each is an input or a not-covered value and nothing is invented:** the circumstances of a deemed termination (s 152.02(4), power in s 152.33(b)); the prescribed date of a deemed termination (s 152.02(5)); the circumstances that allow termination after benefits have been paid (s 152.02(4)); the requirements for deferring a waiting period (ss 152.05(14)(d), 152.06(6)); the shorter period of s 152.06(4); the multiplier for a class of violation (s 152.07(1)(d)(ii)); the percentage of s 152.17(4); the rate of interest (s 152.26(5)); and any regulation under s 152.28(2).
   The check is by citation.
   Searching `SOR-96-332.txt` for the literal subsection numbers 152.02(5), 152.05(14), 152.06(4), 152.06(6), 152.07(1)(d)(ii), 152.17(4), 152.26, 152.28 and 152.33 finds no line.
   A script search for "152." and "Part VII.1" finds citations only in regs 1, 9.01, 9.02, 11.1, 13, 14.01, 24.3, 25.1, 30.1, 30.2, 32, 34, 35, 36, 37, 38, 39, 40, 41, 41.2, 41.6, 54, 55.01, 76.01, 76.06, 76.31 to 76.43, 77.95, 77.97, 77.99 and 91.
   A regulation that prescribes one of the things above without citing the section number would not have been found.
   Asserted for the case where nothing is prescribed. (`ei5-tests-caring.l4`: with `NOTHING` prescribed, the weeks within which a certificate must state a risk of death are 26 and the compassionate-care period is 52 weeks; `ei5-tests-qualifying.l4`: with no multiplier prescribed the Act's 1.25, 1.5, 1.75 and 2 apply, and a prescribed 3 replaces 1.25; `ei5-tests-payment.l4`: with no percentage prescribed the increase is limited to 25% of the weekly earnings, and a prescribed 30% replaces it.)

4. **Regulation 76.43 is narrower than the paragraph it modifies.**
   It deems s 152.07(1)(a) satisfied only "in order to qualify for the benefits payable under sections 152.04 and 152.05", for a person who ceased to reside in a province with a provincial plan, entered into the agreement within 12 months before or within three months after that day, and was covered by the plan during the 12 months before that day.
   The rule for s 152.07(1)(a) takes "the Regulations deem the condition satisfied" as one input; the seat question puts the whole condition in its `@desc` and the rule does not check the reason for the benefit.
   Asserted for the input. (`ei5-tests-qualifying.l4`: for an agreement of 10 January 2026, the paragraph is met on 1 February 2026 when the Regulations deem it, and not otherwise.)

5. **Twelve months are counted to the same day of the month, and 29 February clamps to 28 February.**
   An agreement of 10 January 2026 reaches 12 months on 10 January 2027, not on 9 January; an agreement of 29 February 2024 reaches them on 28 February 2025 and not on 27 February (fork F13).
   Asserted. (`ei5-tests-qualifying.l4`; `ei5-cases-seat.l4`.)

6. **A notice given on the 60th day after the agreement is "within 60 days after", and the 61st day is not.**
   For an agreement of 10 January 2026, a notice on 11 March 2026 (day 60) leaves the agreement deemed never entered into; a notice on 12 March terminates it on 31 December 2026.
   Asserted. (`ei5-tests-agreement.l4`; `ei5-cases-seat.l4`.)

7. **Both ends of the window between the notice and 31 December count.**
   A notice given on 1 June is deemed never given if a benefit period is established on 1 June or on 31 December of that year, and is not if the period is established on 31 May or on 1 January.
   Asserted. (`ei5-tests-agreement.l4`.)

8. **A withdrawal "before December 31" is a withdrawal on 30 December at the latest.**
   Withdrawn on 30 December the notice lapses; withdrawn on 31 December the agreement terminates that day.
   Asserted. (`ei5-tests-agreement.l4`.)

9. **Self-employed earnings can be negative, and a business exactly half rent is not left out.**
   Section 152.01(2)(a)(i)(B) is the business income less all losses with no floor (fork F3): a rental business counted as nothing and losses of 1,000 give earnings of minus 1,000.
   A business "more than fifty per cent" rent is left out of the income of (A): 50,000 of 100,000 is not, 50,001 is.
   Asserted. (`ei5-tests-interpretation.l4`; `ei5-cases-seat.l4`.)

10. **The pregnancy period moves with the confinement.**
    Benefits are payable from the earlier of 12 weeks before the week in which confinement is expected and the week in which it occurs, to 17 weeks after the later of the two weeks.
    With confinement expected on Wednesday 10 June 2026 and not yet occurred, the period is 15 March to 10 October 2026; if the child is born on 1 July it ends on 31 October.
    Before the confinement the period can be stated only for the expected date (fork F9).
    Asserted. (`ei5-tests-sickness-pregnancy.l4`; `ei5-cases-seat.l4`.)

11. **The combined cap of 50 weeks means the maximums of s 152.14(1) cannot all be paid in an ordinary benefit period.**
    Pregnancy (15), parental benefits under the 35-week election (35) and illness (26) add up to 76 weeks, and s 152.14(8) allows 50.
    Section 152.11(14) extends the period "so that those benefits may be paid up to the maximum total" but does not say by how many weeks (fork F17); s 152.11(16) holds the period to two weeks more than the sum of the maximums (78 here), and s 152.14(8) then allows that period less two weeks (76).
    Asserted. (`ei5-tests-payment.l4`, `ei5-tests-benefit-period.l4`; `ei5-cases-seat.l4`: 50 and 51 weeks, 76 and 77 weeks, and a benefit period of 78 weeks.)

12. **Sections 152.05(5) and 152.11(14) say a period is extended but not by how many calendar weeks.**
    The rules return the number of weeks of benefits that may then be paid, up to the maximum, and take the length of an extension under s 152.11(14) as an input; they do not invent a length.
    Asserted for the number of weeks of benefits. (`ei5-tests-parental.l4`; `ei5-cases-seat.l4`: 51 more weeks of parental benefits when 10 of 61 have been paid.)

13. **The 61-week election lowers the weekly rate from 55% to 33%, for the weeks paid under s 152.05 only.**
    A week paid under s 152.05 under the 61-week election is paid at 33%; under the 35-week election, or a week paid for another reason, at 55%.
    Asserted. (`ei5-tests-payment.l4`; `ei5-cases-seat.l4`: 330 and 550 on earnings of 52,000.)

14. **The rate rounds half up, once, on the result.**
    55% of 520 divided by 52 is 5.5 and is paid as 6; of 519 it is 5.49 and is paid as 5.
    Thresholds that are only compared (the 90% of the weekly figure, the $50 and the 25% of s 152.151) are not rounded (fork F20).
    Asserted. (`ei5-tests-payment.l4`.)

15. **The waiting-period test of s 152.151 is continuous at a rate of $200.**
    Below $200 the first $50 of earnings is not deducted; at $200 or more, 25% of the rate is not, and 25% of 200 is 50, so the two limbs allow the same $50 at the boundary.
    Asserted. (`ei5-tests-payment.l4`: rates of 199.99 and 200; `ei5-cases-seat.l4`.)

16. **The deduction for undeclared earnings can outrun the weeks of benefits paid.**
    Section 152.18(3)(b) deducts, in each consecutive week, the benefits paid for that week; if the weeks run out first the rest is not deducted by the text (fork F21), and the last week takes only the remainder.
    Asserted. (`ei5-tests-payment.l4`: 250 against four weeks of 100 gives 100, 100, 50, and 450 against two weeks of 100 gives 100, 100; `ei5-cases-seat.l4`: 700 against four weeks of 400 gives 400, 300.)

17. **The text does not say who chooses between the two bases of the farmer's payment and of the instalments.**
    Sections 152.25(2) and (3)(a) offer the premium "as estimated by the person" or that "for the preceding year" without saying who chooses (fork F24); the rules take the choice as an input made by the person.
    Asserted. (`ei5-tests-premium.l4`; `ei5-cases-seat.l4`: both choices.)

18. **Interest on a missed instalment runs to the earlier of the day of payment and the beginning of the period of s 152.26(1), and the text does not say whether that day is counted in both.**
    The rule ends the period on that day (fork F26); the seat case counts it in the instalment period.
    Asserted. (`ei5-tests-premium.l4`; `ei5-cases-seat.l4`.)

19. **A refund application is out of time after 31 December of the third year following the premium year.**
    Section 152.3(1)(b) says "not later than three years after the end of the year": for the year 2026, 31 December 2029 is in time and 1 January 2030 is not.
    Asserted. (`ei5-tests-premium.l4`; `ei5-cases-seat.l4`.)

20. **The administrator's penalty reaches its maximum on the tenth day; the offence fine reaches its maximum on the fortieth.**
    Section 152.27(2): $5 a day to a maximum of $50 (10 days gives 50, 11 days still 50).
    Section 152.32: at least $25 a day to a maximum of $1,000, so 10 days gives 250 and 40 days or more gives 1,000 (fork F25).
    Asserted. (`ei5-tests-premium.l4`, `ei5-tests-other-provisions.l4`; `ei5-cases-seat.l4`.)

21. **The text does not say who pays the benefits.**
    Part VII.1 says benefits are "payable" and the person "is entitled to receive" them; it names the Commission only as the party that decides, administers and agrees.
    The Hohfeld table names the Commission as the bearer of the duty as a reading, not a sentence.

22. **The definition of "family member" in s 152.01(1) is repealed.**
    The line reads `[Repealed, 2017, c. 20, s. 242]`; ss 152.06(1), 152.061(1) and 152.062(1) use the term as reg 1(3) (piece er1) defines it, so whether a person is a family member is an input in each rule.

23. **Regulations 77.996 and 77.9992 let the Commission "waive the waiting period in respect of any benefit period" that begins from 30 March 2025 to 10 October 2026 and from 11 October 2026 to 9 October 2027.**
    They sit in the Regulations' pilot-project part and name neither Part VII.1 nor s 152.15; the text does not say whether "the waiting period" they mean is the one of s 152.15 (which s 152.01(1) defines as one week).
    The rule for s 152.15 does not take a waiver, and the question is left open.

24. **Three pilot projects once changed s 152.18 and have ceased.**
    Regulations 77.95(4), 77.97(4) and 77.99(4) each add a subsection (2.1) to s 152.18 and cease to have effect on 1 August 2015, 6 August 2016 and 11 August 2018.
    Section 152.18(2) is applied as the Act states it.

25. **Amendments enacted but not in force would add a benefit under a new s 152.041.**
    2024, c. 15, ss 349 to 355 (in the Act's Amendments Not in Force, piece ei7) replace ss 152.03(1.1) and 152.05(5.1), add s 152.041 and amend ss 152.09(2), 152.11 and 152.14(1).
    Their wording is not merged into any rule here.

## What the stable binary does not accept

The binary is the stable `l4` 1.6.98 (the build named in the task).
Each item below was re-run on small probe files when these notes were written, and sorted into the failures that announce themselves and the failure that does not.

**Silent: the code runs, exits 0, and the value is wrong.**

- **`NOT (a) OR b` on one line parses as `NOT ((a) OR b)`.**
  With a = FALSE and b = TRUE it gives FALSE, not TRUE, and nothing is reported.
  Write `(NOT (a)) OR b`, or put `NOT (a)` and `OR b` on separate lines; both were run and give TRUE.
  Every `NOT` in the modules is parenthesised and combined that way.

**Loud: an error appears, and it says little.**

- **`JUST 30%` is a parse error; `JUST (30%)` is accepted.**
  A percentage literal needs its brackets inside `JUST`.
- **A continuation line of an `#ASSERT` is a parse error** (the error points at the first character of the continuation).
  Every `#ASSERT` here is on one line, however long.
- **`YMD` is not in the stable prelude, even after `IMPORT daydate`** (the use is rejected at the name).
  The keel defines the one shim (`YMD y m d MEANS Date d m y`) in `eia-core`, so these modules use `YMD` and must not define it again.
- **A parse error prints an empty `Message:` line.**
  The `Range:` line is the only clue to where.

**Available and used.**
`the earlier of` and `the later of` on DATE come from `daydate`, as does `add months` (which clamps to the last day of the month).
Nothing was found to be missing that a module needed.

**Not reproduced.**
Two layouts that were suspected of failing while the modules were being written (`(f x)'s field` on a call with arguments, and a positional `OF` whose arguments continue on the next lines) were run on probe files and are accepted by this binary in the forms tried (a record built with `OF` and continued on aligned following lines, inside `WHERE`, a `CONSIDER` arm and a function argument; a field taken from a parenthesised call).
No claim is made that these layouts are safe in every context.

## What check.sh prints

Run in this folder as `L4=<the stable l4> L4_TARGET=unstable ./check.sh`.
Exit status 0.
It prints, exactly:

```
module                                    errors satisfied  failed  refused  expected
ei5-agreement.l4                               0         0       0        0         0
ei5-benefit-period.l4                          0         0       0        0         0
ei5-caring.l4                                  0         0       0        0         0
ei5-cases-seat.l4                              0       349       0        0         0
ei5-interpretation.l4                          0         0       0        0         0
ei5-other-provisions.l4                        0         0       0        0         0
ei5-parental.l4                                0         0       0        0         0
ei5-payment.l4                                 0         0       0        0         0
ei5-premium.l4                                 0         0       0        0         0
ei5-qualifying.l4                              0         0       0        0         0
ei5-seat.l4                                    0         0       0        0         0
ei5-sickness-pregnancy.l4                      0         0       0        0         0
ei5-tests-agreement.l4                         0        44       0        0         0
ei5-tests-benefit-period.l4                    0        92       0        0         0
ei5-tests-caring.l4                            0        70       0        0         0
ei5-tests-interpretation.l4                    0        68       0        0         0
ei5-tests-other-provisions.l4                  0        38       0        0         0
ei5-tests-parental.l4                          0        69       0        0         0
ei5-tests-payment.l4                           0       102       0        0         0
ei5-tests-premium.l4                           0        90       0        0         0
ei5-tests-qualifying.l4                        0       100       0        0         0
ei5-tests-sickness-pregnancy.l4                0        39       0        0         0
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
TOTAL (26 modules)                             0      1061       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

and on stderr:

```
check.sh: the target is unstable, so the main check was skipped.
```

The 26 modules are the 10 layer-1 modules, the seat, the 10 test files, the case file and the 4 keel modules; the keel's own test files are not in this folder, so only its modules are run (they carry no assertions).
Every test and case file has assertions written equal to assertions satisfied: 44, 92, 70, 68, 38, 69, 102, 90, 100 and 39 in the test files (712 in all) and 349 in `ei5-cases-seat.l4`.
No assertion is expected to fail, none failed, none was refused, and no module reports an error.

`check.sh` does not run the locator check.
Run separately in this folder: `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/S.C.-1996-c.-23.txt ei5-*.l4` printed `srcrefs check: 476 src: lines, 185 runs, 239 locators, 0 problems`, and `l4 check` on each `ei5-*.l4` file shows no "end of the file" or "follows code" diagnostic (the sign of a misplaced `@ref`).

## Before this is worth relying on

What stands between this encoding and being relied on, most important first.

1. **No independent check of the expected values.**
   This piece had one author for the rules, the tests and the seat cases.
   Every expected value was written by hand from the text before the run, but by the same reader who wrote the rules, so a shared misreading would pass.
   One regulation number was found wrong late (the family supplement is reg 34, not reg 38) and was corrected everywhere; a second reader should write a dozen cases from the text alone, without opening the rules, and run them.
2. **The sources are unofficial plain-text conversions.**
   Nothing here was compared with the official consolidation; the quotation lines match the deposited text (`srcrefs.py` reports 0 problems), not the Justice Laws page.
3. **The 26 forks need the owner's reading.**
   The ones that move the most numbers are F8 and F10 (a period "n weeks after the week" ends on the Saturday of that week), F13 and F14 (the day qualification is tested and how the 260 weeks are counted), F17 (the extension of a benefit period), F20 (what is rounded, and when) and F22 (whether the rate includes the family supplement).
   Each is one rule to reverse.
4. **Values this piece takes from other pieces and from outside the texts have to be wired at the merge.**
   The week of unemployment (regs 30.1 and 30.2), the family supplement and its criteria (reg 34), the deduction for earnings in the waiting period (reg 39(1)), the reductions for provincial plans (regs 76.36 to 76.42), the yearly adjustment of $6,000 (reg 11.1), the maximum yearly insurable earnings (s 4), the premium rate (ss 66 and 66.32) and the Income Tax Act's figures are plain inputs; the cross-reference table lists each.
5. **The commencement day of Part VII.1 is not in the text** (finding 1), so the review day of s 152.34 is an input.
6. **Some questions are left open by the text and are not decided here:** whether the pilot waivers of regs 77.996 and 77.9992 reach the waiting period of s 152.15 (finding 23), who pays the benefits (finding 21), and what the Regulations prescribe where none was found by citation (finding 3).
7. **The Act is amended by enactments not in force.**
   2024, c. 15, ss 349 to 355 add a benefit (s 152.041) and change ss 152.03(1.1), 152.05(5.1), 152.09(2), 152.11 and 152.14(1) when in force (finding 25); the layer-1 rules will need revising then.
8. **The seat is thin by design.**
   Its questions take yes/no and number answers about what the Commission, the Minister or a regulation has decided, and it asks about one business at a time (see "Seat").
   A form built from it asks a great many questions; grouping and defaults belong to the application, not to this layer.
9. **Only the stable binary was used.**
   `check.sh` was run with `L4_TARGET=unstable`, as the brief directs for the stable 1.6.98, so it did not compare against a second binary; nothing was run against a `main` build.
10. **The figures in the tests and the cases are invented** (rates, earnings, premiums, dates of claims); only the figures the Act states are the Act's.
