# NOTES: Employment Insurance Act, Part I (unemployment benefits), first part: ss 6 to 23.3(5), piece ei1

Written by the piece agent `ei1` (Sonnet 5.5) on 2026-10-24 for lines 133-669 of `S.C.-1996-c.-23.txt`.
Target compiler: the stable `l4` 1.6.98 (`main`, 7689b0d, 2026-10-19); nothing here needs `unstable`.
The text is an unofficial plain-text rendering, made by a converter script, of the Justice Laws consolidation of the Employment Insurance Act, S.C. 1996, c. 23, current to 2026-09-30 (last amended 2026-06-18).
It is not the official text, and nothing here claims to be verified against the official text.
The French version is equally authoritative and was not read.

**What is encoded.**
Every provision of lines 133-669: section 6 (interpretation of Part I), ss 7 and 7.1 (qualifying, violations), s 8 (qualifying period), ss 9-11 (benefit period, week of unemployment), ss 12-13.1 (weeks of benefits, waiting period), ss 14-17 (rate), ss 18-20 (availability, deductions), ss 21-23 (illness, pregnancy, parental benefits), ss 23.1-23.3(5) (compassionate care, critically ill child, critically ill adult).
Section 23.3 continues at line 670 with subsection (6); subsection (6) onward is piece ei2's.
The coverage table has 195 rows over 23 sections and 9 headings: 149 encoded, 21 fork, 11 inert (the 9 headings and ss 16(2) and 16(3)), 14 repealed or blank in this text. Every non-blank line of 133-669 is in exactly one row.

**Which instrument each rule comes from.**
Every rule, type and quotation in the `ei1-*.l4` modules comes from the Act (`src:N` is a line of the Act's raw file).
The Regulations (SOR/96-332) are named only in comments and in the descriptions of inputs, where the Act hands a figure or a condition to them (regs 13, 14, 14.01, 17, 23, 24.1, 26, 29-32, 34, 39, 40, 41, 41.2, 41.6, 76.16, 76.17, 77.992).
Those figures and conditions are plain inputs, never encoded here, because the Regulations' ranges belong to pieces er1 to er6.

**Dates in the range.**
The range holds no date of enactment, assent or commencement, and no commencement rule (s 190, which fixes the Act's commencement, is piece ei6's), so no commencement date is carried and no rule carries a `RULES EFFECTIVE DATE`.
The dates the text states as part of its rules are carried as defined values with an `@ref`: 27 September 2020 to 25 September 2021 (s 12(2.1)) and 26 September 2021 to 7 October 2028 (s 12(2.3)(a)(i)); the years 1997 and 2000 of s 14(1.1) are literals in that rule.

**Files** (all in this folder, flat).

| file | what it holds |
| --- | --- |
| `eia-core*.l4` | the keel's shared core (read-only; not edited) |
| `ei1-interpretation.l4` | s 6 |
| `ei1-qualifying.l4` | ss 7, 7.1, 8 |
| `ei1-payment.l4` | ss 12, 13, 13.1 |
| `ei1-benefit-period.l4` | ss 9, 10, 11 (imports `ei1-payment`) |
| `ei1-rate.l4` | ss 14, 15, 16, 17 |
| `ei1-disentitlement-deductions.l4` | ss 18, 19, 20 |
| `ei1-illness-pregnancy.l4` | ss 21, 22 |
| `ei1-parental.l4` | s 23 (imports `ei1-payment`, `ei1-benefit-period`) |
| `ei1-caring.l4` | ss 23.1, 23.2, 23.3(1)-(5) (imports `ei1-benefit-period`) |
| `ei1-tests-<module>.l4` | one test file per layer-1 module, expected values written by hand from the text |
| `ei1-seat.l4` | layer 2: 119 questions for the person in the seat, in 17 `§§` groups |
| `ei1-cases-seat.l4` | layer 2: 464 worked-case assertions, at least one per question |
| `NOTES.md`, `PROGRESS.md` | this file and the working log |
| `check.sh`, `srcrefs.py` | supplied tools, unchanged |

The names of this piece's own types, constructors and fields begin `ei1 `; its rule names begin `s N` (the Act's section), as the keel's naming conventions ask.

## Seat

The seat is the person to whom Part I is applied: **a person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, who asks whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission.**
It is the seat the brief fixed, and it matches the keel's (`KEEL-NOTES.md`).
Why this seat and no other: Part I is the part of the Act in which a claimant meets the Commission; every right in it (to be paid, to a benefit period, to an extension, to defer a waiting period) is the claimant's, and every duty on the claimant (to prove availability, to declare earnings, to elect 35 or 61 weeks, to prove a reason for an extension) is a condition of one of those rights.
The Commission and the Ministers have no seat; what they must pay, decide or may do appears only as what the claimant is owed or exposed to, and the judgments the Act leaves to the Commission ("in the opinion of the Commission", "in such manner as the Commission may direct") are plain yes/no inputs about what the Commission has found, never worked out.
Layer 1 (nine modules) takes nobody's point of view; layer 2 (`ei1-seat.l4`) calls layer 1's rules by name and never restates one.

How the seat layer is built:
- Every question has `@export` and a `@desc` on each input, worded as the person would be asked; the 119 questions are in the text's order, under 17 `§§` headings. Heading comments say where a group arises only in a situation the person may not be in (illness, pregnancy, a new-born or adopted child, a family member, a critically ill child or adult).
- The lists and records that layer 1 takes (violations, earlier benefit periods, the special benefits paid, the Commission's judgments) are built inside each question from plain inputs. Three simplifications are assumed, not ruled, and recorded in the fork register as F-seat-violation, F-seat-earlier and F-seat-weeks.
- The seat layer is generated from small Python tables kept outside the deposit (in `inputs/work/seat/`), so that the same fact is asked in the same words wherever it occurs.
- Figures that other pieces or the Regulations supply (Schedules I, IV and V, the regional rate, the maximum yearly insurable earnings, the prescribed reductions for provincial benefits, the family supplement) are inputs; a change in any of them changes the answers.

## Jural relations

Notation: "C" is the claimant (the person in the seat), "Com" the Commission. A "claim" is a Hohfeldian right (its correlative is a duty), a "privilege" a liberty (correlative: no-right), a "power" an ability to change a legal relation (correlative: liability), an "immunity" a protection from such a change (correlative: disability). The rule column names the layer-1 rule that encodes the relation once, from the neutral side; the seat question that asks it from C's side is named in the seat file under the same section number.
A relation is stated once in layer 1 and never written again from the other party's side.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | section | L4 rule |
| --- | --- | --- | --- | --- |
| benefits payable to an insured person who qualifies | C (claim) | Com (duty to pay) | s 7(1), 7(2) | `ei1-qualifying` `s 7(1) unemployment benefits are payable ...`, `s 7 and s 7.1 the insured person qualifies to receive benefits` |
| Canada-U.S. agreement bar | Com (privilege not to pay) | C (no-right) | s 7(6) | `s 7(6) the insured person is not qualified ...` |
| increase in required hours after violations | Com (power to issue a notice of violation, s 7.1(4); the increase follows) | C (liability to the higher figure) | s 7.1(1), (3), (4) | `s 7.1(1) the number of hours that an insured person requires`, `s 7.1(3) ...`, `s 7.1(4) an insured person accumulates a violation` |
| class of a violation | Com (power to classify) | C (liability to the class) | s 7.1(5)-(7) | `s 7.1(5) the class of the violation`, `s 7.1(6) the value of the violation` |
| extension of the qualifying period on proof | C (power: by proving the reason, extends the period) | Com (liability to treat the period as extended; duty to accept proof "in such manner as the Commission may direct") | s 8(2), (4), (5), (7) | `s 8(2) the week is one for which ...`, `s 8 the qualifying period` |
| benefit period established on an initial claim | C (claim to a benefit period; power to make the claim) | Com (duty to establish it; liability to the claim) | s 9, 10(1), (3) | `s 9 a benefit period shall be established`, `s 10(1) the first day of the benefit period`, `s 9 and s 10(3) ...` |
| late claim treated as made earlier | C (power, on showing good cause) | Com (liability to treat the claim as earlier; disability to refuse where good cause is shown) | s 10(4), (5), (5.1)-(5.3) | `s 10(4) ...`, `s 10(5) ...`, `s 10(5.1)`, `(5.2)`, `(5.3)` |
| cancellation of a benefit period | Com (power to cancel, s 10(6)(a); power to cancel at C's request, s 10(6)(b)) | C (liability to cancellation; C holds the power to make the request) | s 10(6), (7) | `s 10(6)(a) ...`, `s 10(6)(b) ...`, `s 10(7) ...` |
| ending a benefit period at C's request | C (power to end it by request and a new initial claim) | Com (liability) | s 10(8)(d), (9) | `s 10(8)(d) ...`, `s 10(9) ...`, `s 10(8) the day on which the benefit period ends` |
| extension of the benefit period | C (claim to the extended period) | Com (duty to allow benefits in it) | s 10(10)-(15) | `s 10(10) ...` to `s 10(15) ...`, `s 10(2) and s 10(14) the length of the benefit period in weeks` |
| weeks of benefits for each reason | C (claim to the weeks up to the maximum) | Com (duty to pay for them; no duty beyond them) | s 12(1)-(8) | `s 12(1) ...` to `s 12(8) ...` |
| waiting period | Com (privilege not to pay until one week is served) | C (no-right to benefits in the waiting week) | s 13, 13.1 | `s 13 the claimant has served ...`, `s 13.1(1) ...` |
| rate of weekly benefits | C (claim to the rate) | Com (duty to pay at it; no duty above the maximum) | s 14(1), 17 | `s 14(1) ...`, `s 17 ...`, `s 14(1) and s 17 ...` |
| family supplement | C (power to establish low-income eligibility; claim to the increase) | Com (liability to the increase, up to the cap; duty to pay it) | s 16(1), (4) | `s 16(1) ...`, `s 16(4) ...`, `s 16(1) and s 16(4) ...` |
| proving availability | Com (privilege not to pay for a working day without proof) | C (burden: no entitlement unless C proves (a), (b) or (c)) | s 18(1), (2) | `s 18(1)(a)`, `(b) and s 18(2)`, `(c)`, `s 18(1) ...` |
| deductions for earnings | Com (power to deduct) | C (liability to deduction) | s 19(1), (2), (4); s 20(1), (2) | `s 19(1) ...`, `s 19(2) ...`, `s 19(4) ...`, `s 20(1) ...`, `s 20(2) ...` |
| undeclared earnings | Com (claim that C declare all earnings; power to deduct what was not declared) | C (duty to declare; liability to the deduction) | s 19(3) | `s 19(3)(a) ...`, `s 19(3)(b) ...` |
| minor attachment claimant and illness | Com (privilege not to pay) | C (no-right to sickness benefits) | s 21(1) | `s 21(1) ...` |
| reduction for provincial allowances | Com (power to reduce as prescribed) | C (liability to the reduction) | s 21(2), 22(3), 23(3.5), 23.1(10), 23.2(11) | the five rules `s 21(2) ...`, `s 22(3) ...`, `s 23(3.5) ...`, `s 23.1(10) ...`, `s 23.2(11) ...` |
| deduction of an employer's plan | Com (power to deduct) | C (liability to deduction) | s 21(3), 22(5) | `s 21(3) ...`, `s 22(5) ...` |
| pregnancy benefits | C (claim, despite s 18) | Com (duty to pay for the weeks of the period) | s 22(1), (2), (4), (6), (7) | `s 22(1) ...`, `s 22(2) ...`, `s 22(4) ...`, `s 22(6) and s 22(7) ...` |
| parental benefits | C (claim, despite s 18) | Com (duty to pay for the weeks of the period) | s 23(1), (2), (3), (3.01)-(3.4) | `s 23(1) ...`, `s 23(2) ...`, `s 23(3) ...`, `s 23(3.01) ...`, `s 23(3.2) ...`, `s 23(3.21) ...`, `s 23(3.22) ...`, `s 23(2) to (3.4) ...` |
| election of 35 or 61 weeks | Com (claim that C elect) | C (duty to elect; after payment, disability to revoke: irrevocable) | s 23(1.1), (1.2) | `s 23(1.1) ...`, `s 23(1.2) ...` |
| the first claimant's election binds | the first claimant or individual (power to fix the election for both) | the second claimant (liability to be bound) | s 23(1.3) | `s 23(1.3) the election that binds the claimant` |
| dividing the weeks between two claimants | the two claimants (power to divide the weeks by agreement, within the limits) | Com (liability to pay as divided; if they cannot agree, the prescribed rules apply to them) | s 23(4), (4.1), (4.11); 23.1(8), (9); 23.2(8), (9) | `s 23(4) ...` rules, `s 23(4.11) ...`, `s 23.1(8) ...`, `s 23.1(9) ...`, `s 23.2(8) ...` |
| deferring the waiting period | C (privilege to defer) | Com (no-right to insist that C serve it now) | s 23(5), (6); 23.1(7); 23.2(6); 23.3(5) | `s 23(5) ...`, `s 23(6) ...`, `s 23.1(7) ...`, `s 23.2(6) ...`, `s 23.3(5) ...` |
| compassionate care benefits | C (claim) | Com (duty to pay for the weeks of the period) | s 23.1(2), (4), (4.1), (6) | `s 23.1(2) ...`, `s 23.1(4) ...`, `s 23.1(4.1) ...`, `s 23.1(6) ...` |
| certificate issued by a prescribed practitioner | the practitioner (power to issue the certificate that qualifies C) | C (the certificate changes C's position) | s 23.1(3); 23.2(2); 23.3(2) | `s 23.1(3) ...` |
| no further certificate after 26 weeks | C (immunity from a demand for another certificate, unless s 50(8.1)) | Com (disability to demand one) | s 23.1(4.1) | `s 23.1(4.1) ...` |
| shared maxima for caring | Com (privilege not to pay beyond the shared maximum) | C (no-right beyond it) | s 12(4.1)-(4.5); 23.2(10), (10.1) | `s 12(4.1) ...` to `s 12(4.5) ...`, `s 23.2(10) ...`, `s 23.2(10.1) ...` |
| critically ill child, critically ill adult | C (claim) | Com (duty to pay for the weeks of the period) | s 23.2(1), (3), (5); 23.3(1), (3), (4) | `s 23.2(1) ...`, `s 23.2(3) ...`, `s 23.2(5) ...`, `s 23.3(1) ...`, `s 23.3(3) ...`, `s 23.3(4) ...` |
| suitable employment | C (privilege to refuse work that is not suitable employment, without disqualification under s 27 or loss of availability under s 18) | Com (no-right to disqualify for the refusal) | s 6(4), (5) | `s 6(4) employment is not suitable employment`, `s 6(5) ...` |
| none: definitions and counting rules | - | - | s 6(1) (disentitled, disqualified, initial claim, attachment claimants, qualifying period, waiting period), 6(2) rounding, 6(3) hours, 7(2)(a) and (b) table as such, 8(1), 8(3), 8(6), 11 (week of unemployment), 12(2.2)-(2.5), 13.1(2), 14(1.1), (2)-(4), 15, 16(2), (3), 21(3) reading, 22(2) period dates, 23(2) period dates | the definition and counting rules named in the coverage table |

## Coverage table

One row per provision of lines 133-669.
Counts: 195 rows: 149 encoded, 21 fork, 11 inert (the nine division headings and ss 16(2), 16(3)), 14 repealed or blank in this text; over 23 sections (6, 7, 7.1, 8 to 13, 13.1, 14 to 23, 23.1, 23.2, 23.3) and 9 headings. Where a section's subsections state one rule together, or differ in the rule they state, a row says so; rows for s 6(1), 6(4), 7(2), 7.1(5), 8(1), 10(6), 10(8), 12(2.3), 12(4), 18(1) and 19(3) are split by paragraph. A `where` of the form `X ...` abbreviates a rule name that is given in full in the module.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| heading: PART I Unemployment Benefits | src:133 | inert | - | A Part heading; it carries no text of its own. The Part is named in the core as `Part I`. |
| heading: Interpretation | src:135 | inert | - | A division heading; it carries no text of its own. |
| s 6(1) lead-in "In this Part," | src:136-137 | encoded | rows below | Makes each definition below apply to Part I; the Part's own definitions (disentitled, disqualified, initial claim, major and minor attachment claimant, qualifying period, waiting period) are the rows below. |
| s 6(1) "disentitled" | src:138 | encoded | `ei1-interpretation` `s 6(1) disentitled` | Not entitled under s 13, 18, 21 (this piece) or 31, 32, 33, 36, 37, 49, 50 (piece ei2) or under the regulations: eleven BOOLEAN inputs. |
| s 6(1) "disqualified" | src:139 | encoded | `ei1-interpretation` `s 6(1) disqualified` | Disqualified under s 27 or 30 (piece ei2): two BOOLEAN inputs. |
| s 6(1) "initial claim for benefits" | src:140 | encoded | `ei1-interpretation` `s 6(1) initial claim for benefits` |  |
| s 6(1) "major attachment claimant" | src:141 | encoded | `ei1-interpretation` `s 6(1) major attachment claimant`, `s 6(1) the number of hours of insurable employment that separates a major attachment claimant from a minor one` | 600 hours or more. Schedule II (piece ei6) replaces the definition for one case; not made here. |
| s 6(1) "minor attachment claimant" | src:142 | encoded | `ei1-interpretation` `s 6(1) minor attachment claimant` | Fewer than 600 hours. Schedule II (piece ei6) replaces the definition for one case; not made here. |
| s 6(1) "qualifying period" | src:143 | encoded | `ei1-qualifying` `s 8 the qualifying period` | The definition sends the reader to section 8; the rule is there. |
| s 6(1) "waiting period" | src:144 | encoded | `ei1-payment` `s 13 the claimant has served a waiting period of one week of unemployment` | The definition sends the reader to section 13; the rule is there. |
| s 6(2) | src:145-146 | encoded | core `s 6(2) and s 152.01(5) amount rounded to the nearest dollar` | Encoded once in the shared core; called by `s 13.1`, `s 14(1)`, `s 16(4)`, `s 17`, `s 19(2)`, `s 20` and cited there. |
| s 6(3) | src:147-148 | encoded | `ei1-interpretation` `s 6(3) the hours of insurable employment that a claimant has in the qualifying period` | The hours are established under s 55 (piece ei2) and allocated by regulations made under paragraph 54(z.1); the established figure is an input, named once. |
| s 6(4) lead-in | src:149-150 | encoded | `ei1-interpretation` `s 6(4) employment is not suitable employment` | For paragraphs 18(1)(a) and 27(1)(a) to (c) and subsection 50(8). The combining rule takes the results of (a), (b), (c) and subsection (5). |
| s 6(4)(a) | src:151 | encoded | `ei1-interpretation` `s 6(4)(a) employment arises in consequence of a work stoppage attributable to a labour dispute` |  |
| s 6(4)(b) | src:152 | encoded | `ei1-interpretation` `s 6(4)(b) and s 6(5) at a lower rate of earnings or on conditions less favourable than the benchmark`, `s 6(4)(b) employment in the claimant's usual occupation is at a lower rate or on less favourable conditions` | The benchmark is the agreement between employers and employees, or, with none, what good employers recognize. |
| s 6(4)(c) | src:153 | encoded | `ei1-interpretation` `s 6(4)(c) employment outside the claimant's usual occupation is at a lower rate or on less favourable conditions than the claimant might reasonably expect` | "Might reasonably expect" is a judgment, taken as two BOOLEAN inputs. |
| s 6(5) | src:154-155 | encoded | `ei1-interpretation` `s 6(5) paragraph 6(4)(c) does not apply after a reasonable interval` | "A reasonable interval" is not measured in the Act: a BOOLEAN input (fork F-interval). |
| heading: Qualifying for Benefits | src:157 | inert | - | A division heading; it carries no text of its own. |
| s 7(1) | src:158-159 | encoded | `ei1-qualifying` `s 7(1) unemployment benefits are payable as provided in Part I to the insured person` | The person's claim: benefits are payable to an insured person who qualifies. |
| s 7(2) lead-in | src:160-161 | encoded | `ei1-qualifying` `s 7(2) an insured person qualifies` | An insured person qualifies if (a) and (b). |
| s 7(2)(a) | src:162 | encoded | `ei1-qualifying` `s 7(2)(a) the insured person has had an interruption of earnings from employment` | "Interruption of earnings" is regs 14 and 14.01 (piece er1): an input. |
| s 7(2)(b) and the table | src:163-174 | encoded | `ei1-qualifying` `s 7(2)(b) the number of hours of insurable employment required in relation to the regional rate of unemployment`, `s 7(2)(b) the insured person has had during their qualifying period at least the number of hours required` | The table is read in nine bands through the core's `Rate band` (bands 9 to 12 together are "more than 13%"); the regional rate is an input (reg 17, piece er1). |
| s 7(3) to (5) | src:175 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 209] |
| s 7(6) | src:176-177 | encoded | `ei1-qualifying` `s 7(6) the insured person is not qualified to receive benefits because of the Canada-U.S. agreement` | Whether it is "jointly determined" is a decision of the two states: a BOOLEAN input. |
| s 7.1(1) | src:178-191 | encoded | `ei1-qualifying` `s 7.1(1) the row of the table ...`, `the number of hours set out in the table for the class of the violation`, `the violation was accumulated in the 260 weeks before the initial claim`, `the classes of the violations that raise the hours required`, `the number of hours that an insured person requires`, `s 7 and s 7.1 the insured person qualifies to receive benefits` | All 36 cells of the table are tested. Forks F-several (which column with violations of several classes) and F-window (the 260 weeks). |
| s 7.1(2) | src:192 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 210] |
| s 7.1(2.1) | src:193-194 | encoded | `ei1-qualifying` `s 7.1(2.1) the day on which a violation accumulated under section 152.07 is deemed to be accumulated under section 7.1` | The day is the day the notice of violation was given. Section 152.07 is piece ei5's. |
| s 7.1(3) | src:195-196 | encoded | `ei1-qualifying` `s 7.1(3) the violation may be taken into account in this initial claim` | A violation spent in two earlier qualifying initial claims is not counted again. |
| s 7.1(4) | src:197-201 | encoded | `ei1-qualifying` `s 7.1(4) an insured person accumulates a violation` | Sections 38, 39, 41.1, 65.1, 135, 136 are in other pieces; their results are inputs. |
| s 7.1(5) lead-in | src:202-203 | fork | `ei1-qualifying` `s 7.1(5) the class of the violation` | Except for violations for which a warning was imposed: NOTHING, because the Act gives them no class. Fork F-subsequent: when both (a) and (b) apply, (b) prevails. |
| s 7.1(5)(a) | src:204-207 | encoded | `ei1-qualifying` `s 7.1(5) the class of the violation` | Under $1,000 minor; $1,000 or more but under $5,000 serious; $5,000 or more very serious. |
| s 7.1(5)(b) | src:208 | encoded | `ei1-qualifying` `s 7.1(5)(b) the notice of violation is issued within 260 weeks after the person accumulates another violation`, `s 7.1(5) the class of the violation` | Subsequent violation. |
| s 7.1(6) | src:209-212 | encoded | `ei1-qualifying` `s 7.1(6) the value of the violation` | Overpayment is Part VI's (piece ei4), an input. |
| s 7.1(7) | src:213-214 | encoded | `ei1-qualifying` `s 7.1(7) the amount determined under paragraph 7.1(6)(b)` | Weekly rate times the average number of weeks (reg 13, piece er1), capped at what could have been paid. |
| s 8(1) lead-in | src:215-216 | fork | `ei1-qualifying` `s 8(1) the shorter of the 52-week period and the period since an immediately preceding benefit period began`, `s 8 the qualifying period` | Forks F-no-prior (no immediately preceding benefit period: paragraph (a)) and F-shorter (the "shorter" is judged before the extension). |
| s 8(1)(a) | src:217 | encoded | `ei1-qualifying` `s 8(1)(a) the 52-week period immediately before the beginning of the benefit period` |  |
| s 8(1)(b) | src:218 | encoded | `ei1-qualifying` `s 8(1)(b) the period from the first day of an immediately preceding benefit period to the end of the week before the benefit period` |  |
| s 8(2) | src:219-224 | encoded | `ei1-qualifying` `s 8(2) the week is one for which the person was not employed in insurable employment for a reason that extends the qualifying period` | The proof "in such manner as the Commission may direct" is a BOOLEAN input. Regs 40 and 41 (piece er3) say what is a prescribed illness; section 59 (piece ei2). |
| s 8(3) | src:225 | repealed or blank in this text | - | [Repealed, 2021, c. 23, s. 305] |
| s 8(4) | src:226-227 | encoded | `ei1-qualifying` `s 8(4) the week during an extension further extends the qualifying period` |  |
| s 8(5) | src:228-229 | encoded | `ei1-qualifying` `s 8(5) the week counts for the purposes of subsections 8(2) and 8(4)` | A week in receipt of benefits does not count. |
| s 8(6) | src:230 | repealed or blank in this text | - | [Repealed, 2021, c. 23, s. 305] |
| s 8(7) | src:231-232 | encoded | `ei1-qualifying` `s 8(7) the longest qualifying period after an extension, in weeks` | 104; applied inside `s 8 the qualifying period`. |
| heading: Benefit Period | src:234 | inert | - | A division heading; it carries no text of its own. |
| s 9 | src:235-236 | encoded | `ei1-benefit-period` `s 9 a benefit period shall be established`, `s 9 benefits are payable to the person in accordance with Part I for the week` |  |
| s 10(1) | src:237-240 | encoded | `ei1-benefit-period` `s 10(1) the first day of the benefit period` | The later of the Sundays of the interruption week and the claim week. |
| s 10(2) | src:241-242 | encoded | `ei1-benefit-period` `s 10(2) the length of a benefit period in weeks, before any extension` and `s 10(2) and s 10(14) the length of the benefit period in weeks` | 52 weeks, plus the extensions of (10) to (13.02) capped at 104, plus a section 24 extension (piece ei2) as an input. |
| s 10(3) | src:243-244 | encoded | `ei1-benefit-period` `s 10(3) a benefit period shall not be established for the claimant`, `s 9 and s 10(3) a benefit period is established for the claimant` |  |
| s 10(4) | src:245-246 | encoded | `ei1-benefit-period` `s 10(4) the initial claim for benefits is regarded as having been made on the earlier day` |  |
| s 10(5) | src:247-248 | encoded | `ei1-benefit-period` `s 10(5) the claim for benefits other than an initial claim is regarded as having been made on the earlier day` | The time prescribed for making the claim is reg 26 (piece er2): its last day is an input. |
| s 10(5.1) | src:249-253 | encoded | `ei1-benefit-period` `s 10(5.1) a claim for benefits referred to in section 23.1 is regarded as having been made on an earlier day` | Paragraph (c) "any other circumstances set out in the regulations": no regulation in the deposited text names any, so an input. |
| s 10(5.2) | src:254-258 | encoded | `ei1-benefit-period` `s 10(5.2) a claim for benefits referred to in section 23.2 is regarded as having been made on an earlier day` | Same as (5.1) for a critically ill child. |
| s 10(5.3) | src:259-263 | encoded | `ei1-benefit-period` `s 10(5.3) a claim for benefits referred to in section 23.3 is regarded as having been made on an earlier day` | Same as (5.1) for a critically ill adult. |
| s 10(6) lead-in | src:264-265 | encoded | `ei1-benefit-period` `s 10(6)(a)`, `s 10(6)(b)` | The Commission "may": the rules say whether the power is open to it. |
| s 10(6)(a) | src:266 | encoded | `ei1-benefit-period` `s 10(6)(a) the Commission may cancel the benefit period` |  |
| s 10(6)(b) | src:267-269 | encoded | `ei1-benefit-period` `s 10(6)(b) the Commission may cancel at the request of the claimant the portion of the benefit period immediately before the first week for which benefits were paid or payable` | Section 152.01(1) (piece ei5) is named for the self-employed alternative: a BOOLEAN input. |
| s 10(7) | src:270-271 | encoded | `ei1-benefit-period` `s 10(7) the cancelled benefit period or portion of a benefit period is deemed never to have begun` |  |
| s 10(8) lead-in | src:272-273 | encoded | `ei1-benefit-period` `s 10(8) the day on which the benefit period ends` | The earliest of the days of paragraphs (a), (b) and (d). |
| s 10(8)(a) | src:274 | encoded | `ei1-benefit-period` input of `s 10(8) the day on which the benefit period ends` | The day on which no further benefits are payable, including after the maximum number of weeks of section 12. |
| s 10(8)(b) | src:275 | encoded | `ei1-benefit-period` input of `s 10(8) the day on which the benefit period ends` | The day the benefit period would otherwise end under section 10 (the last day of its length). |
| s 10(8)(c) | src:276 | repealed or blank in this text | - | [Repealed, 2002, c. 9, s. 12] |
| s 10(8)(d) | src:277-280 | encoded | `ei1-benefit-period` `s 10(8)(d) the day on which the claimant requests the end of the benefit period, makes a new initial claim and qualifies` | The request, the new initial claim and the qualifying must all have happened. |
| s 10(9) | src:281-282 | fork | `ei1-benefit-period` `s 10(9) the request under paragraph 10(8)(d) is regarded as having been made on the earlier day` | Fork F-9: the text says "paragraph 8(d)"; read as paragraph 10(8)(d). |
| s 10(10) | src:283-288 | encoded | `ei1-benefit-period` `s 10(10) the week is one for which the claimant was not entitled to benefits for a reason that extends the benefit period`, `s 10(10) and s 10(11) the number of weeks by which the benefit period is extended` |  |
| s 10(11) | src:289-290 | encoded | `ei1-benefit-period` `s 10(11) the week during an extension further extends the benefit period` |  |
| s 10(12) | src:291-292 | encoded | `ei1-benefit-period` `s 10(12) the number of weeks by which the benefit period is extended because the children are in hospital` |  |
| s 10(12.1) | src:293-294 | encoded | `ei1-benefit-period` `s 10(12.1) the number of weeks by which the benefit period is extended because of the Canadian Forces` |  |
| s 10(13) | src:295-300 | fork | `ei1-benefit-period` `s 10(13) the benefit period is extended so that special benefits may be paid up to the maximum total number of weeks`, `s 10(13)(c) the maximum total number ...`, `s 10(13) the number of weeks by which the benefit period is extended` | Fork F-13: the extension is the length of (15) less 52 weeks. Uses `s 12(3)` of `ei1-payment`. |
| s 10(13.01) | src:301-305 | encoded | `ei1-benefit-period` `s 10(13.01) the number of weeks by which the benefit period is extended for the reason mentioned in paragraph 12(3)(b)` | 26 weeks. |
| s 10(13.02) | src:306-307 | fork | `ei1-benefit-period` `s 10(13.02) the number of weeks by which the benefit period is extended for regular and special benefits` | Fork F-13.02: the shortfall to be covered turns on the Schedule IV conversion of s 12(7); it is an input; the extension never exceeds 26 weeks. |
| s 10(13.03) | src:308-309 | encoded | `ei1-benefit-period` `s 10(13.03) benefits of that kind are payable during the extension under subsection (13.02)` |  |
| s 10(13.1) to (13.7) | src:310 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 211] |
| s 10(14) | src:311-312 | encoded | `ei1-benefit-period` `s 10(14) the longest benefit period after extensions under subsections (10) to (13.02), in weeks` | 104; applied inside `s 10(2) and s 10(14) the length of the benefit period in weeks`. |
| s 10(14.1) | src:313 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 211] |
| s 10(15) | src:314-315 | encoded | `ei1-benefit-period` `s 10(15) the maximum number of weeks in a benefit period extended under subsection (13)` | 2 weeks plus the total of the maxima, cut at 104 by (14); s 12(5) takes this figure as an input. |
| s 11(1) | src:316-317 | encoded | `ei1-benefit-period` `s 11(1) the week is a week in which the claimant does not work a full working week` | "Full working week" is the Regulations' (regs 29 to 31, piece er2): an input. |
| s 11(2) | src:318-319 | encoded | `ei1-benefit-period` `s 11(2) the week is not a week of unemployment although the claimant is excused from their normal duties` |  |
| s 11(3) | src:320-324 | encoded | `ei1-benefit-period` `s 11(3) the week or part of a week during a period of leave is not a week of unemployment` |  |
| s 11(4) | src:325-328 | encoded | `ei1-benefit-period` `s 11(4) the insured person is deemed to have worked a full working week`; combined in `s 11 a week of unemployment for a claimant` |  |
| heading: Payment of Benefits | src:330 | inert | - | A division heading; it carries no text of its own. |
| s 12(1) | src:331-332 | encoded | `ei1-payment` `s 12(1) benefits may be paid to the claimant for the week` |  |
| s 12(2) | src:333-334 | encoded | `ei1-payment` `s 12(2) the general maximum number of weeks ...` | The table in Schedule I (piece ei6) is an input. |
| s 12(2.1) | src:335-336 | encoded | `ei1-payment` `s 12(2.1) the period within which a benefit period must begin ...`, `s 12(2.1) the maximum number of weeks is 50 ...`, `s 12(2.1) the maximum number of weeks for a benefit period that begins during that period` | The dates 27 September 2020 and 25 September 2021 are carried as data. |
| s 12(2.2) | src:337-338 | encoded | `ei1-payment` inside `s 12(2.1) the maximum number of weeks is 50 for a benefit period that begins during the period` | A claimant under the Employment Insurance (Fishing) Regulations is excluded. |
| s 12(2.3) lead-in | src:339-340 | encoded | `ei1-payment` `s 12(2.3) the maximum number of weeks is read from the table in Schedule V` | Despite subsection (2), the table in Schedule V (piece ei6) applies if (a) or (b). |
| s 12(2.3)(a) | src:341-345 | fork | `ei1-payment` `s 12(2.3)(a)(i) the period within which a benefit period must be established`, `s 12(2.3) ...` | Forks F-established and F-around. Conditions (i) to (iv) are cumulative. The dates 26 September 2021 and 7 October 2028 are carried as data. |
| s 12(2.3)(b) | src:346 | encoded | `ei1-payment` `s 12(2.3) the maximum number of weeks is read from the table in Schedule V` | Conditions (a)(i) and (ii) and the criteria of reg 77.992 (piece er5), an input. |
| s 12(2.4) | src:347-348 | encoded | `ei1-payment` `s 12(2.4) the earlier benefit period is considered to have been established within the 260 weeks` |  |
| s 12(2.5) | src:349-355 | fork | `ei1-payment` `s 12(2.5) the earlier benefit period began during the period around the week that is n times 52 weeks before`, `s 12(2.5) the earlier benefit period is considered to have begun around the same time of year` | Fork F-around: the period runs from the first day of the week eight weeks before to the last day of the week eight weeks after. |
| s 12(2.6) to (2.8) | src:356 | repealed or blank in this text | - | [Repealed, 2016, c. 7, s. 212] |
| s 12(3) | src:357-366 | encoded | `ei1-payment` `s 12(3) the maximum number of weeks for which benefits may be paid in a benefit period for the reason` | NOTHING for the regular reason, whose maximum is subsection (2)'s. |
| s 12(4) lead-in | src:367-368 | encoded | `ei1-payment` `s 12(4)(a)`, `s 12(4)(b)` |  |
| s 12(4)(a) | src:369 | encoded | `ei1-payment` `s 12(4)(a) the maximum number of weeks for a single pregnancy` | 15. |
| s 12(4)(b) | src:370-372 | encoded | `ei1-payment` `s 12(4)(b) the maximum number of weeks for the care of one or more new-born or adopted children as a result of a single pregnancy or placement` | 35 or 40 (divided), 61 or 69 (divided), by the election. |
| s 12(4.01) | src:373-376 | encoded | `ei1-payment` `s 12(4.01) the maximum number of weeks of benefits payable under the Act in respect of the child or children` | Section 152.05 is piece ei5's. |
| s 12(4.1) | src:377-378 | encoded | `ei1-payment` `s 12(4.1) the maximum number of weeks of benefits payable in respect of the family member`, `s 12(4.1) the weeks of benefits still payable in respect of the family member` |  |
| s 12(4.2) | src:379-380 | encoded | `ei1-payment` `s 12(4.2) the length in weeks of the period of 52 weeks in subsection (4.1), or of the shorter period if one is prescribed` | No regulation in the deposited text prescribes a shorter period (grep of the Regulations for 23.1(5) finds none): an input that is NOTHING when none is. |
| s 12(4.3) | src:381-382 | encoded | `ei1-payment` `s 12(4.3) further benefits are payable under section 23.1 in respect of the family member` |  |
| s 12(4.4) | src:383-384 | encoded | `ei1-payment` `s 12(4.4) the maximum number of weeks of benefits payable in respect of the critically ill child`, `s 12(4.4) the weeks of benefits still payable in respect of the critically ill child` |  |
| s 12(4.5) | src:385-386 | encoded | `ei1-payment` `s 12(4.5) the maximum number of weeks of benefits payable in respect of the critically ill adult`, `s 12(4.5) the weeks of benefits still payable in respect of the critically ill adult` |  |
| s 12(5) | src:387-388 | encoded | `ei1-payment` `s 12(5) the maximum number of combined weeks of benefits because of reasons mentioned in subsection (3)` | The s 10(15) figure is passed in; nothing imports `ei1-benefit-period`. |
| s 12(6) | src:389-390 | encoded | `ei1-payment` `s 12(6) the total number of weeks of benefits that may be combined` |  |
| s 12(7) | src:391-394 | encoded | `ei1-payment` `s 12(7) the number of weeks that count toward the total number of weeks of benefits established under subsection (6)` | The Schedule IV conversion (piece ei6) is an input. |
| s 12(8) | src:395-396 | encoded | `ei1-payment` `s 12(8) the placement is a single placement of a child or children for the purpose of adoption` |  |
| s 13 | src:397-398 | encoded | `ei1-payment` `s 13 the claimant has served a waiting period of one week of unemployment`, `s 13 the claimant is entitled to be paid benefits in the benefit period` | Reg 39.1 (piece er3) waives the waiting period in some cases; it is not part of this range and is not an input here (see "Before this is worth relying on"). |
| s 13.1(1) | src:399-402 | encoded | `ei1-payment` `s 13.1(1) the week of unemployment is deemed to be a week of unemployment for which benefits would otherwise be payable` | The 25% of the rate is rounded under s 6(2). |
| s 13.1(2) | src:403-406 | encoded | `ei1-payment` inside `s 13.1(1) ...` | (a) the s 19(2) deduction is left out of the amount; (b) "earnings" are as determined for s 19(2): the input is named so. |
| heading: Rate of Benefits | src:408 | inert | - | A division heading; it carries no text of its own. |
| s 14(1) | src:409-410 | encoded | `ei1-rate` `s 14(1) the rate of weekly benefits payable to the claimant` | 55%, or 33% for the weeks paid under s 23 at the 61-week maximum; rounded under s 6(2). |
| s 14(1.1) | src:411-414 | encoded | `ei1-rate` `s 14(1.1) the maximum weekly insurable earnings` | $750 for benefit periods beginning in 1997 to 2000, later the maximum yearly insurable earnings (an input) divided by 52; NOTHING before 1997 (the text is silent). |
| s 14(2) | src:415-427 | fork | `ei1-rate` `s 14(2) the number of weeks by which the insurable earnings in the calculation period are divided`, `s 14(2) the claimant's weekly insurable earnings` | The table is read in nine bands. Fork F-cap: the quotient is held to the maximum weekly insurable earnings of (1.1). |
| s 14(3) | src:428-431 | encoded | `ei1-rate` `s 14(3) the insurable earnings in the calculation period` | Amounts established under regs 23 and 24.1 (piece er2) are inputs. |
| s 14(4) | src:432-433 | encoded | `ei1-rate` `s 14(4) the number of weeks in the calculation period`, `s 14(4) the insurable earnings of the weeks in the calculation period` | The highest-earning weeks, whether consecutive or not. |
| s 14(4.1) | src:434 | repealed or blank in this text | - | [Repealed, 2012, c. 19, s. 604] |
| s 15 | src:435 | repealed or blank in this text | - | [Repealed, 2001, c. 5, s. 5] |
| s 16(1) | src:436-437 | encoded | `ei1-rate` `s 16(1) the rate of weekly benefits is increased by the amount of a family supplement`, `s 16(1) and s 16(4) the amount of the increase in the rate of weekly benefits` | The supplement (reg 34(5)), the low-income criteria (reg 34(3)) and "dependent children" are the Regulations' (piece er2): inputs. |
| s 16(2) | src:438-439 | inert | - | A permission for the regulations to take low-income family eligibility criteria that are the same as or similar to those for a Canada child benefit: it governs how the regulation-making power is used and states nothing a claimant could be asked. The criteria that result are reg 34(3) (piece er2), taken as an input of `s 16(1)`. |
| s 16(3) | src:440-441 | inert | - | A definition used only by subsection (2): a Canada child benefit is a deemed overpayment under subdivision a.1 of Division E of Part I of the Income Tax Act. It supports the regulation-making power of (2) and adds no condition of its own; reg 34(2) (piece er2) repeats it. |
| s 16(4) | src:442-443 | encoded | `ei1-rate` `s 16(4) the most that the increase in the rate of weekly benefits may be` | The prescribed percentage is reg 34(6) (piece er2), an input; 25% when none is prescribed; rounded under s 6(2). |
| s 17 | src:444-445 | fork | `ei1-rate` `s 17 the maximum rate of weekly benefits`, `s 14(1) and s 17 the rate of weekly benefits, not above the maximum rate` | Fork F-17: it caps the s 14(1) rate; whether it also caps the rate after the s 16 increase is not said. |
| heading: Disentitlement to Benefits | src:447 | inert | - | A division heading; it carries no text of its own. |
| s 18(1) lead-in | src:448-449 | encoded | `ei1-disentitlement-deductions` `s 18(1) the claimant is entitled to be paid benefits for the day as far as section 18 goes` | A working day (reg 32, piece er2) is the day tested; the claimant must prove (a), (b) or (c). |
| s 18(1)(a) | src:450 | encoded | `ei1-disentitlement-deductions` `s 18(1)(a) the claimant was capable of and available for work and unable to obtain suitable employment` |  |
| s 18(1)(b) | src:451 | encoded | `ei1-disentitlement-deductions` `s 18(1)(b) and s 18(2) the claimant was unable to work because of a prescribed illness, injury or quarantine` | Reg 40 (piece er3). |
| s 18(1)(c) | src:452 | encoded | `ei1-disentitlement-deductions` `s 18(1)(c) the claimant was engaged in jury service` |  |
| s 18(2) | src:453-454 | encoded | `ei1-disentitlement-deductions` `s 18(1)(b) and s 18(2) the claimant was unable to work because of a prescribed illness, injury or quarantine` | A claimant to whom benefits are payable under any of ss 23 to 23.3 need not prove availability under (1)(b). |
| heading: Deductions from Benefits | src:456 | inert | - | A division heading; it carries no text of its own. |
| s 19(1) | src:457-458 | encoded | `ei1-disentitlement-deductions` `s 19(1) the amount deducted from the benefits payable for the first three weeks for which benefits are otherwise payable` | The amount "as prescribed" is reg 39 (piece er3), an input. |
| s 19(2) | src:459-462 | fork | `ei1-disentitlement-deductions` `s 19(2) the amount deducted from the benefits payable in the week`, `s 19(2) the benefits payable in the week after the deduction` | Forks F-round (each percentage amount rounded under s 6(2)) and F-floor (a deduction cannot take the week's benefits below nothing). Pilot projects of Part IV of the Regulations (piece er5) adapt s 19(2); not encoded here. |
| s 19(3) lead-in | src:463-464 | encoded | `ei1-disentitlement-deductions` `s 19(3)(a)`, `s 19(3)(b)` | Undeclared earnings for a period "determined under the regulations". |
| s 19(3)(a) | src:465-470 | encoded | `ei1-disentitlement-deductions` `s 19(3)(a) the amount deducted from the benefits paid to the claimant for the period` | (i) the whole of the undeclared earnings if, in the Commission's opinion, the claimant knowingly failed to declare; (ii) otherwise the undeclared earnings less the difference between (A) and (B). |
| s 19(3)(b) | src:471-473 | encoded | `ei1-disentitlement-deductions` `s 19(3)(b) the amount deducted in each consecutive week` | The deduction each week equals the benefits paid for that week. |
| s 19(4) | src:474-475 | encoded | `ei1-disentitlement-deductions` `s 19(4) the earnings or allowances may be deducted under section 19` | Section 59(c) and (d) (piece ei2) and the regulations are inputs. |
| s 20(1) | src:476-477 | fork | `ei1-disentitlement-deductions` `s 20(1) the amount deducted for the excluded days in the waiting period` | Fork F-day: 1/5 of the rate is rounded under s 6(2) for each day before it is multiplied. |
| s 20(2) | src:478-479 | fork | `ei1-disentitlement-deductions` `s 20(2) the amount deducted for the days of disentitlement in a week that is not in the waiting period` | Fork F-day, as s 20(1). |
| heading: Special Benefits | src:481 | inert | - | A division heading; it carries no text of its own. |
| s 21(1) | src:482-483 | encoded | `ei1-illness-pregnancy` `s 21(1) the minor attachment claimant is not entitled to receive benefits while unable to work for that reason` |  |
| s 21(2) | src:484-485 | encoded | `ei1-illness-pregnancy` `s 21(2) the benefits payable to the claimant after the reduction for allowances payable under a provincial law` | The reduction "as prescribed": no regulation for illness benefits found in the deposited Regulations; an input. |
| s 21(3) | src:486-487 | encoded | `ei1-illness-pregnancy` `s 21(3) the benefits payable for the week after deducting the allowances payable under the employer's plan` | Section 69(1) (piece ei3) is an input. |
| s 22(1) | src:488-489 | encoded | `ei1-illness-pregnancy` `s 22(1) benefits are payable to the claimant despite section 18` |  |
| s 22(2) | src:490-497 | fork | `ei1-illness-pregnancy` `s 22(2) the period during which benefits are payable` | Fork F-22-2: the period runs from the first day of the earlier week to the last day of the week 17 weeks after the later week. |
| s 22(3) | src:498-499 | encoded | `ei1-illness-pregnancy` `s 22(3) the benefits payable to the claimant after the reduction for allowances payable under a provincial law` | Regs 76.16 and 76.17 (piece er4) prescribe the reduction for a provincial plan; an input. |
| s 22(4) | src:500-501 | encoded | `ei1-illness-pregnancy` `s 22(4) section 18 does not apply, for the purposes of section 13, to the week` |  |
| s 22(5) | src:502-503 | encoded | `ei1-illness-pregnancy` `s 22(5) the benefits payable for the week after deducting the allowances payable under the employer's plan` |  |
| s 22(6) | src:504-505 | encoded | `ei1-illness-pregnancy` `s 22(6) and s 22(7) the period during which benefits are payable, extended` |  |
| s 22(7) | src:506-507 | encoded | `ei1-illness-pregnancy` `s 22(6) and s 22(7) the period during which benefits are payable, extended` | The extended period ends no later than the last day of the week 52 weeks after the week of confinement. |
| s 23(1) | src:508-509 | encoded | `ei1-parental` `s 23(1) benefits are payable to the claimant to care for one or more new-born or adopted children` |  |
| s 23(1.1) | src:510-511 | encoded | `ei1-parental` `s 23(1.1) the maximum number of weeks elected` | "Shall elect": no time limit and no consequence are stated, so the election is an input. |
| s 23(1.2) | src:512-513 | encoded | `ei1-parental` `s 23(1.2) the election is irrevocable` |  |
| s 23(1.3) | src:514-515 | encoded | `ei1-parental` `s 23(1.3) the election that binds the claimant` |  |
| s 23(2) | src:516-519 | fork | `ei1-parental` `s 23(2) the period during which benefits are payable` | Fork F-22-2, as for s 22(2). |
| s 23(3) | src:520-521 | encoded | `ei1-parental` `s 23(3) the number of weeks by which the period is extended because the children are in hospital` |  |
| s 23(3.01) | src:522-523 | encoded | `ei1-parental` `s 23(3.01) the number of weeks by which the period is extended because of the Canadian Forces` |  |
| s 23(3.1) | src:524-525 | encoded | `ei1-parental` `s 23(3.1) the longest the period may be after an extension under subsection (3) or (3.01), in weeks`; applied in `s 23(2) to (3.4) the length of the period in weeks` | 104 weeks. |
| s 23(3.2) | src:526-531 | fork | `ei1-parental` `s 23(3.2) the period is extended so that benefits may be paid up to the applicable maximum number of weeks`, `s 23(3.2) the number of weeks by which the period is extended` | Fork F-23-3.2: the text does not say by how many weeks; read as the extension of s 10(13) (to the length of s 10(15)). |
| s 23(3.21) | src:532-536 | encoded | `ei1-parental` `s 23(3.21) the number of weeks by which the period is extended for the reason mentioned in paragraph 12(3)(b)` | 26 weeks. |
| s 23(3.22) | src:537-538 | encoded | `ei1-parental` `s 23(3.22) the number of weeks by which the period is extended for regular and special benefits` | The extension established under s 10(13.02) is passed in. |
| s 23(3.23) | src:539 | repealed or blank in this text | - | [Repealed, 2012, c. 27, s. 17] |
| s 23(3.3) | src:540-541 | fork | `ei1-parental` applied in `s 23(2) to (3.4) the length of the period in weeks` | Fork F-23-3.4: the limits of (3.3) and (3.4) are read as limits on the whole period; the s 10(15) figure is passed in. |
| s 23(3.4) | src:542-543 | fork | `ei1-parental` applied in `s 23(2) to (3.4) the length of the period in weeks` | Fork F-23-3.4. |
| s 23(3.5) | src:544-545 | encoded | `ei1-parental` `s 23(3.5) the benefits payable to the claimant after the reduction for allowances payable under a provincial law` | Regs 76.16 and 76.17 (piece er4); an input. |
| s 23(4) | src:546-547 | encoded | `ei1-parental` `s 23(4) and s 23(4.1) the most weeks of benefits that may be divided between the claimants`, `s 23(4) the division of the weeks of benefits between the claimants is within the limits`, `s 23(4) the weeks of benefits are divided in accordance with the prescribed rules` | The prescribed rules are reg 41.6 (piece er3). Section 152.05 is piece ei5's. |
| s 23(4.1) | src:548-551 | encoded | `ei1-parental` `s 23(4) and s 23(4.1) the most weeks of benefits that may be divided between the claimants` | "For greater certainty": the same limits as (4). |
| s 23(4.11) | src:552-553 | encoded | `ei1-parental` `s 23(4.11) the most weeks of benefits that may be paid to one claimant` | 35 or 61 weeks by the election. |
| s 23(5) | src:554-559 | encoded | `ei1-parental` `s 23(5) the claimant may have their waiting period deferred until they make another claim for benefits in the same benefit period` | The "prescribed requirements" of paragraph (d): no regulation in the deposited text names any; an input. |
| s 23(6) | src:560-563 | fork | `ei1-parental` `s 23(6) the position of the waiting period when a major attachment claimant and an individual claim for the same child` | Fork F-23-6: "that claimant" in paragraph (b) is read as the individual, to whom s 152.05 applies. |
| s 23.1(1) | src:564 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 236] |
| s 23.1(2) | src:565-571 | encoded | `ei1-caring` `s 23.1(2)(a) the certificate states ...`, `s 23.1(2) benefits are payable to the claimant for the care or support of a family member` | "Family member" is reg 1(3) (piece er1): an input. The weeks within which the certificate says death is a significant risk are an input. |
| s 23.1(3) | src:572-573 | encoded | `ei1-caring` `s 23.1(3) the certificate may be issued by a member of a prescribed class of medical practitioners` | Reg 41.2 (piece er3). |
| s 23.1(4) | src:574-583 | fork | `ei1-caring` `s 23.1(4) the period during which benefits are payable`, `ei1 the period that begins with the week of a day and ends with the week in which the first of the events happens` | Fork F-23.1-4: when (a)(i), (ii) and (iii) can each apply, (iii) then (ii) then (i). The 52 weeks end on the Saturday 364 days from the first Sunday. |
| s 23.1(4.1) | src:584-585 | encoded | `ei1-caring` `s 23.1(4.1) an additional certificate is needed for benefits payable after the end of the period of 26 weeks` | Needed only if s 50(8.1) (piece ei2) requires one. |
| s 23.1(5) | src:586-589 | encoded | `ei1-caring` `s 23.1(2)(a) ...` (paragraph (a)) and `s 23.1(4) ...` (paragraph (b)) | A shorter prescribed period is an input that is NOTHING when none is prescribed; no regulation in the deposited text names one. |
| s 23.1(6) | src:590-594 | encoded | `ei1-caring` `s 23.1(6) subparagraph (4)(a)(ii) does not apply to the claim` | Paragraph (c) "other circumstances set out in the regulations": an input. |
| s 23.1(7) | src:595-599 | encoded | `ei1-caring` `s 23.1(7) the claimant may have their waiting period deferred until they make another claim for benefits in the same benefit period` |  |
| s 23.1(8) | src:600-601 | encoded | `ei1-caring` `s 23.1(8) the most weeks of benefits that may be divided between the claimants`, `s 23.1(8) the division of the remaining weeks of benefits between the claimants is within the limit` | Section 152.06 is piece ei5's. |
| s 23.1(8.1) | src:602-603 | encoded | `ei1-caring` `s 23.1(8) the most weeks of benefits that may be divided between the claimants` | "For greater certainty": the same limit, 26 weeks. |
| s 23.1(9) | src:604-605 | encoded | `ei1-caring` `s 23.1(9) the weeks of benefits are divided in accordance with the prescribed rules` | Reg 41.6 (piece er3). |
| s 23.1(10) | src:606-607 | encoded | `ei1-caring` `s 23.1(10) the benefits payable to the claimant after the reduction for allowances payable under a provincial law` |  |
| s 23.2(1) | src:608-611 | encoded | `ei1-caring` `s 23.2(1) benefits are payable to the claimant to care for or support a critically ill child` | "Critically ill child" is reg 1(6) (piece er1): an input. |
| s 23.2(2) | src:612-613 | encoded | `ei1-caring` folded into the certificate input of `s 23.2(1) ...` | A member of a prescribed class may issue the certificate (reg 41.2, piece er3). |
| s 23.2(3) | src:614-622 | fork | `ei1-caring` `s 23.2(3) the period during which benefits are payable` | As s 23.1(4), without the earlier-day case: only (i) and (ii). |
| s 23.2(4) | src:623 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 237] |
| s 23.2(5) | src:624-628 | encoded | `ei1-caring` `s 23.2(5) subparagraph (3)(a)(ii) does not apply to the claim` |  |
| s 23.2(6) | src:629-633 | encoded | `ei1-caring` `s 23.2(6) the claimant may have their waiting period deferred until they make another claim for benefits in the same benefit period` | Section 152.061 is piece ei5's. |
| s 23.2(7) | src:634 | repealed or blank in this text | - | [Repealed, 2017, c. 20, s. 237] |
| s 23.2(8) | src:635-636 | encoded | `ei1-caring` `s 23.2(8) the most weeks of benefits that may be divided between the claimants`, `s 23.2(8) the division of the remaining weeks of benefits between the claimants is within the limit`, `s 23.2(8) the weeks of benefits are divided in accordance with the prescribed rules` |  |
| s 23.2(9) | src:637-638 | encoded | `ei1-caring` `s 23.2(8) the most weeks of benefits that may be divided between the claimants` | "For greater certainty": the same limit, 35 weeks. |
| s 23.2(10) | src:639-640 | encoded | `ei1-caring` `s 23.2(10) benefits under section 23.1 or 152.06 are payable in respect of the child for the week` |  |
| s 23.2(10.1) | src:641-642 | encoded | `ei1-caring` `s 23.2(10.1) benefits under section 23.3 or 152.062 are payable in respect of the person for the week` |  |
| s 23.2(11) | src:643-644 | encoded | `ei1-caring` `s 23.2(11) the benefits payable to the claimant after the reduction for allowances payable under a provincial law` |  |
| s 23.3(1) | src:645-648 | encoded | `ei1-caring` `s 23.3(1) benefits are payable to the claimant to care for or support a critically ill adult` | "Critically ill adult" is reg 1(7) (piece er1): an input. Section 23.3 continues at line 670 (piece ei2): this piece encodes (1) to (5). |
| s 23.3(2) | src:649-650 | encoded | `ei1-caring` folded into the certificate input of `s 23.3(1) ...` | Reg 41.2 (piece er3). |
| s 23.3(3) | src:651-659 | fork | `ei1-caring` `s 23.3(3) the period during which benefits are payable` | As s 23.2(3), for an adult. |
| s 23.3(4) | src:660-664 | encoded | `ei1-caring` `s 23.3(4) subparagraph (3)(a)(ii) does not apply to the claim` |  |
| s 23.3(5) | src:665-669 | encoded | `ei1-caring` `s 23.3(5) the claimant may have their waiting period deferred until they make another claim for benefits in the same benefit period` | Section 152.062 is piece ei5's. Subsection (6) onward is piece ei2's. |

## Fork register

Every entry is assumed, not ruled: a reading was chosen so that work could go on, and each can be reversed in one place.
"Where I looked" for ambiguities: every subsection with a limit, a date, a count of weeks, a cross-reference to a section outside the range, and every place the text says "as prescribed", "in the circumstances set out in the regulations", "in such manner as the Commission may direct", or hands a judgment to the Commission.

| id | provision | what the text leaves open | how it is encoded here | what would settle it |
| --- | --- | --- | --- | --- |
| F-interval | s 6(5) (src:155) | "a lapse of a reasonable interval": the Act does not measure it. | A BOOLEAN input, `a reasonable interval has lapsed ...`; never worked out. | A regulation or a ruling of the Commission. |
| F-several | s 7.1(1) (src:179) | The table is by class of violation; an insured person who has accumulated violations of more than one class in the 260 weeks has no stated column. | The largest figure of the classes in the window. In practice a second violation inside 260 weeks is a subsequent violation (s 7.1(5)(b)), the last and largest column. | A ruling, or the text of a regulation. |
| F-window | s 7.1(1) (src:179) | "In the 260 weeks before making their initial claim": whether the day of the claim is in the window, and whether the first day counts. | 1,820 days, from the day 1,820 days before the claim to the day before it; the day of the claim is out, the first day is in. Asserted at both ends. | The Interpretation Act, which is not among the inputs. |
| F-subsequent | s 7.1(5) (src:203-208) | Paragraph (a) classes by value, paragraph (b) makes a violation "subsequent" if the notice is issued within 260 weeks after another; a violation can satisfy both. | (b) prevails: the class is subsequent whatever the value. A violation for which a warning was imposed has no class (NOTHING). | Nothing in the text says which prevails: (b) is a second sentence joined by "and". The reading follows the table of s 7.1(1), which has a separate column for subsequent violations and none for "a minor violation within 260 weeks of another". The "even if" in (b) is about when the acts happened, not about precedence. |
| F-no-prior | s 8(1) (src:216-218) | With no immediately preceding benefit period paragraph (b) has nothing to measure. | The 52-week period of paragraph (a). | A ruling. |
| F-shorter | s 8(1), (2), (4) (src:216, 220, 227) | Whether the "shorter" of (a) and (b) is judged before or after the extension of subsection (2), which speaks only of "a qualifying period mentioned in paragraph (1)(a)". | The shorter is judged on the unextended periods; the extension applies only to the (a) period; when the two are equal the (a) period is taken. | A ruling. |
| F-9 | s 10(9) (src:282) | "a request under paragraph 8(d)": there is no paragraph 8(d); s 10(8)(d) is the request. | Read as paragraph 10(8)(d). Asserted. | A correction of the text. |
| F-13 | s 10(13), (15) (src:296, 315) | "the benefit period is extended so that those benefits may be paid up to that maximum total number of weeks": the extension is not given in weeks. | The extension is the length of s 10(15) (2 weeks more than the total of the maxima of the benefits paid, at most 104 weeks) less 52 weeks. Asserted (15 + 61 weeks: 78 weeks, extension 26). The opening words of s 10(15), "unless the benefit period is also extended under any of subsections (10) to (12.1)", lift the s 10(15) limit for a claimant who also has one of those extensions; they are not modelled separately, so the same target length is used for them, and only s 10(14)'s 104 weeks limits the total. | A regulation, or the Commission's practice. |
| F-13.02 | s 10(13.02) (src:307) | How many weeks short of "the total number of weeks established under subsection 12(6) as determined under subsection 12(7)" the claimant was is not worked out by the text (it turns on the Schedule IV conversion, piece ei6). | An input, the weeks by which the benefit period must be extended; the extension is never more than 26 weeks. Asserted. | The Schedule IV table (piece ei6). |
| F-established | s 12(2.3)(a)(iii) (src:344) | "at least three benefit periods were established": established when? s 12(2.4) dates an earlier benefit period by the notification received for a week in the 260 weeks. | An earlier benefit period counts if its first day is within the 260 weeks before the current one began, or if it began earlier and the claimant was notified of payment or non-payment for a week in the 260 weeks (s 12(2.4)). Asserted at the boundary day. | The Commission's practice. |
| F-overlap | s 12(2.1) with s 12(2.3) (src:336, 340) | Both begin "Despite subsection (2)"; (2.1) is by the day the benefit period begins, (2.3) by the day it is established, so, if "established" can be later than the day the claim is made (s 9 does not say when a benefit period is established), a benefit period that begins on 19 September 2021 and is established on 27 September 2021 is in both. | (2.3) prevails over (2.1), which prevails over (2). | A ruling; the dates are adjacent, not overlapping, so the case is narrow. |
| F-around | s 12(2.5) (src:350-355) | "the period that begins eight weeks before and ends eight weeks after the week that is 52 weeks before ...": the edges. | From the first day of the week eight weeks before to the last day of the week eight weeks after. Asserted at both edges. | A ruling. |
| F-cap | s 14(1.1), (2) (src:412, 415) | (2) divides the insurable earnings by the weeks; (1.1) names a "maximum weekly insurable earnings" but does not say (2) is held to it. | (2) is held to (1.1). Asserted. NOTHING for a benefit period before 1997 (no maximum is stated). | The structure of s 14 is the only guide. |
| F-17 | s 17 (src:445) | Whether the maximum rate of s 17 also caps the rate after a family supplement is added (s 16(4) limits the increase separately). | s 17 caps the s 14(1) rate only. | A regulation or a ruling. |
| F-round | s 19(2) (src:460-462) | Which amounts are "a percentage or fraction of earnings" rounded under s 6(2). | The 90% line and each of the two deductions are rounded to the nearest dollar, the higher dollar when equidistant. Asserted. | The Commission's practice. |
| F-floor | s 19(2) (src:460) | The deduction is taken "from benefits payable in that week"; whether it can make them negative. | It cannot: the result is not less than nothing. Asserted. | A ruling. |
| F-day | s 20 (src:477, 479) | "an amount equal to 1/5 of their weekly rate of benefits for each such working day": round once or per day. | Per day, then multiplied. Asserted. | The Commission's practice. |
| F-22-2 | s 22(2), 23(2) (src:491-497, 517-519) | "the period that begins the earlier of (i) 12 weeks before the week in which her confinement is expected ... and ends 17 weeks after the later of ..." is by weeks; a period is carried here as dates. | From the first day (Sunday) of the first week to the last day (Saturday) of the last week; the period of s 23(2) ends on the Saturday of the week 52 weeks after the week of the birth or placement. Asserted. | A ruling. |
| F-23-3.2 | s 23(3.2) (src:527-531) | The period "is extended so that benefits may be paid up to the applicable maximum number of weeks": by how much is not said. | Read as the extension of s 10(13) (to the length of s 10(15)). Asserted. | A regulation. |
| F-23-3.4 | s 23(3.1), (3.3), (3.4) (src:525, 541, 543) | Three limits on the length of the period; (3.3) and (3.4) are written for "an extension" and are read here as limits on the whole. | The period is never more than 104 weeks, and an extension under (3.2) never goes past the s 10(15) length. Asserted. | A ruling. |
| F-23-6 | s 23(6)(b) (src:563) | "that claimant may have his or her waiting period deferred in accordance with section 152.05": section 152.05 governs the individual, not the major attachment claimant. | "that claimant" is read as the individual (a self-employed person). Asserted. | A correction of the text. |
| F-23.1-4 | s 23.1(4) (src:575-583) | When (a)(i), (ii) and (iii) can each apply, which begins the period; and what "the period of 52 weeks following the first day of the week" ends on. | (iii), then (ii), then (i); the 52 weeks are the 364 days that begin with the first Sunday, so the period ends on the Saturday before the Sunday 52 weeks on. Asserted. The same shape serves ss 23.2(3) and 23.3(3), which have only (i) and (ii). | A ruling. |
| F-prescribed | ss 10(5.1)-(5.3), 12(4.2), 23(5)(d), 23.1(5), (6)(c), (7)(c), 23.2(5)(c), (6)(c), 23.3(4)(c), (5)(c) | "circumstances set out in the regulations", "prescribed requirements", "a shorter period ... prescribed". A search of the deposited Regulations (grep for each subsection number) finds none that names them. | Each is a plain input (a BOOLEAN, or a MAYBE NUMBER that is NOTHING when none is prescribed). | A regulation. |
| F-seat-violation | the seat, s 7.1 | A person may have several violations. | The seat asks about one violation (the one of the highest class); layer 1 takes a list. | A decision on the form. |
| F-seat-earlier | the seat, s 12(2.3) | A person may have had many earlier benefit periods. | The seat asks about up to five, each by the day it began, and one yes/no (notified of payment or non-payment for a week in the 260 weeks) applied to all five. | A decision on the form. |
| F-seat-weeks | the seat, s 14(2)-(4) | s 14(4) picks the claimant's highest-earning weeks in the qualifying period. | The seat asks for the total insurable earnings of those weeks directly; layer 1's `s 14(4) the insurable earnings of the weeks in the calculation period` takes the week-by-week list and is tested, but is not called by the seat. | A decision on the form. |

## Cross-references out of my ranges

A rule outside the range is taken as an input of the right type, named for the fact, with a comment `-- out of range: ... (piece X)` in the module. "none found" means the deposited Regulations (grep) name nothing for it.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 6(1) "disentitled" | ss 31, 32, 33, 36, 37, 49, 50 | ei2 | eight BOOLEANs `not entitled under section N` |
| s 6(1) "disentitled" | the Regulations | er1 to er6 | BOOLEAN `not entitled under the regulations` |
| s 6(1) "disqualified" | ss 27, 30 | ei2 | two BOOLEANs |
| s 6(3) | s 55; regulations under s 54(z.1) | ei2; er2, er3 | NUMBER `the hours of insurable employment established under section 55 ...` |
| s 7(2)(a); s 10(1) | regs 14, 14.01 (interruption of earnings) | er1 | BOOLEAN `an interruption of earnings has occurred`; DATE `the day on which the interruption of earnings occurs` |
| ss 7(2)(b), 7.1(1), 14(2) | reg 17, Schedule I of the Regulations (the regional rate) | er1, er6 | NUMBER `the regional rate of unemployment that applies to ...` |
| s 7.1(2.1) | s 152.07 | ei5 | DATE `the day on which the notice of violation was given ...` |
| s 7.1(4) | ss 38, 39, 41.1, 65.1; ss 135, 136; the Criminal Code | ei2; ei4; none | four BOOLEANs |
| s 7.1(6) | the meaning of "overpayment of benefits" (Part VI) | ei4 | NUMBER `the amount of the overpayment ...` |
| s 7.1(7) | reg 13 (average number of weeks) | er1 | NUMBER |
| s 8(2) | regs 40(4), 40(5), 41(2) (prescribed illness, injury, quarantine, pregnancy); s 59(c), (d) | er3; ei2 | BOOLEANs |
| s 10(2), (14) | s 24(1)(g) and regulations under it | ei2 (regs er3) | NUMBER `the weeks of extension under regulations made under paragraph 24(1)(g)` |
| s 10(5) | reg 26 (the time prescribed for making a claim) | er2 | DATE `the last day of the time prescribed for making the claim` |
| ss 10(5.1)-(5.3), 23.1(6), 23.2(5), 23.3(4) | "any other circumstances set out in the regulations" | none found | BOOLEAN |
| s 10(6)(b), (8)(d) | s 152.01(1); Part VII.1 | ei5 | BOOLEANs |
| s 11(1) | regs 29 to 31 (a full working week) | er2 | BOOLEAN `the claimant works a full working week` |
| s 12(2) | Schedule I (table of weeks) | ei6 | NUMBER |
| s 12(2.3) | Schedule V; Schedule VI; reg 77.992 | ei6; ei6; er5 | NUMBER; BOOLEAN; BOOLEAN |
| s 12(4.01) | s 152.05 | ei5 | BOOLEAN |
| s 12(4.2) | a shorter period prescribed under s 23.1(5) | none found | MAYBE NUMBER |
| s 12(5) | none (s 10(15) is in this piece) | - | passed in from `ei1-benefit-period` |
| s 12(7) | Schedule IV (conversion of weeks) | ei6 | NUMBER |
| ss 14(1.1), 17 | s 4 (maximum yearly insurable earnings; the published figure) | ei-g0 (the keel) | NUMBER, as the keel's table asks |
| s 14(3) | regs 23, 24.1 (insurable earnings in the calculation period) | er2 | two NUMBERs |
| s 16 | reg 34 (supplement, low-income criteria, dependent children, the percentage) | er2 | NUMBER; BOOLEANs; MAYBE NUMBER |
| s 18 | reg 32 (a working day); reg 40(1), (4) (illness) | er2; er3 | BOOLEANs |
| s 19(1) | reg 39 | er3 | NUMBER |
| s 19(4) | s 59(c), (d); regulations on deduction | ei2; none found | BOOLEANs |
| ss 21(2), 22(3), 23(3.5), 23.1(10), 23.2(11) | regs 76.16, 76.17 (reduction for provincial benefits; they deal only with ss 22 and 23); none found for ss 21(2), 23.1(10), 23.2(11) | er4 | NUMBER `the amount by which the regulations reduce the benefits` |
| ss 21(3), 22(5) | s 69(1) and the premium-reduction regulations | ei3; er4 | BOOLEAN |
| ss 23(1.3), (4), (6); 23.1(7), (8); 23.2(6), (8); 23.3(5) | ss 152.04, 152.05, 152.06, 152.061, 152.062 | ei5 | BOOLEANs |
| ss 23(4), 23.1(9), 23.2(8) | reg 41.6 (prescribed rules for dividing weeks) | er3 | BOOLEAN `... divided in accordance with the prescribed rules` |
| ss 23(5)(d), 23.1(7)(c), 23.2(6)(c), 23.3(5)(c) | "prescribed requirements" | none found | BOOLEAN |
| ss 23.1(2), 23.2(1), 23.3(1) | reg 1(3), (6), (7) (family member, critically ill child, critically ill adult) | er1 | BOOLEANs |
| ss 23.1(3), 23.2(2), 23.3(2) | reg 41.2 (certificate issued outside Canada) | er3 | two BOOLEANs |
| s 23.1(4.1) | s 50(8.1) | ei2 | BOOLEAN |
| s 12(2.2) | the Employment Insurance (Fishing) Regulations | not among the inputs | BOOLEAN |
| ss 10(12.1), 23(3.01) | regulations under the National Defence Act | not among the inputs | BOOLEAN and NUMBER |
| s 7(6) | Article VI of the Canada-U.S. unemployment insurance agreement of 1942 | not among the inputs | BOOLEAN |

Count: 39 rows; the ones that matter most are the regional rate and hours (they drive ss 7, 7.1, 12 and 14), the Schedule I and Schedule V tables (ei6), the Regulations' interruption of earnings (er1) and the maximum yearly insurable earnings (the keel's s 4).

## Needs from the core

The core was enough for everything this piece needed (`Period of days`, `Reason for benefits`, `Election of maximum weeks`, `Violation class`, `Rate band`, the week helpers, the rounding rule, `YMD`).
Nothing of the core was edited or copied. The following are local, defined under distinct specific names; the lead may promote them if pieces ei5 or ei6 need the same:

| local name | what it is | why it might be shared |
| --- | --- | --- |
| `ei1 Special benefits paid for one reason` (in `ei1-benefit-period`) | a reason (`Reason for benefits`) and the weeks paid for it | s 152.1x (piece ei5) and Schedule IV (ei6) read the same facts |
| `ei1 the special benefits actually paid` | keeps the reasons in s 12(3)(a)-(f) for which at least one week was paid | the same |
| `ei1 Violation` (in `ei1-qualifying`) | class, day accumulated, earlier initial claims in which it was counted | s 152.07 (ei5) accumulates violations too |
| `ei1 Earlier benefit period` (in `ei1-payment`) | first day, regular benefits paid or payable, notified of payment | s 12(2.3) only |
| `ei1 the period that begins with the week of a day and ends with the week in which the first of the events happens` (in `ei1-caring`) | the "week to week, at most n weeks" shape of ss 23.1(4), 23.2(3), 23.3(3) | ss 152.06(4) and 152.061(3), 152.062(3) (ei5) have the same shape |
| `ei1 the dates in` (in `ei1-benefit-period`) | a MAYBE DATE as a list of at most one date | a general helper |
| `ei1 Position of the waiting period under subsection 23(6)` (in `ei1-parental`) | a three-way outcome | s 23(6) only |

## What the text turns out to say

Each finding is something the text says that a reader might not expect, or a place where the text and a natural reading part. "Asserted." means a test or a seat case in this folder asserts it, with an expected value worked out by hand from the text. Figures such as 52,000 for the maximum yearly insurable earnings are invented test values (that figure is the keel's s 4, outside the text of this range), not published ones.

1. The hours table of s 7(2) is read in nine bands, and a rate exactly on the line belongs to the lower band: at 6% the person needs 700 hours, at 6.01% 665, at 13% 455, at 13.01% 420. Asserted (`ei1-tests-qualifying`, `ei1-cases-seat`).
2. A violation can double the hours needed: from 700 to 1,400 for a subsequent violation at a regional rate of 6% or less. All 36 cells of the s 7.1(1) table are asserted against the text (`ei1-tests-qualifying`). Asserted.
3. A violation is counted in at most two initial claims in which the person qualified (s 7.1(3)): a violation already used twice no longer raises the hours (490 instead of 980 at 11.5%). Asserted.
4. A violation for which only a warning was imposed has no class (s 7.1(5) leaves it out), so it never raises the hours; the encoding answers NOTHING for its class rather than guessing one. Asserted (an explicit not-covered case).
5. Where a violation fits both (a) and (b) of s 7.1(5) the text does not say which prevails; (b), subsequent, is taken (fork F-subsequent). Asserted.
6. The qualifying period can be shorter than 52 weeks: when an earlier benefit period began within the last 52 weeks, the period starts with that benefit period and the hours before it are never counted again (s 8(1)(b)); only the 52-week period can be extended by s 8(2) and (4), and no extension takes it past 104 weeks. Asserted.
7. A claimant with fewer than 600 hours (a minor attachment claimant) can be paid regular benefits only: s 21(1) bars sickness benefits, and ss 22, 23, 23.1, 23.2 and 23.3 are payable only to a major attachment claimant. Since the s 7(2) table asks for as few as 420 hours, a person can qualify under s 7 and still have no special benefits. Asserted (599 hours against 600 in each question).
8. A benefit period begins on the later of the Sundays of the week of the interruption and the week of the initial claim, so a claim made late in a week is never earlier than that week's Sunday. Asserted.
9. s 10(9) speaks of "a request under paragraph 8(d)": there is no such paragraph; s 10(8)(d) is the request (fork F-9). Asserted.
10. The 104-week limit of s 10(14) applies to extensions under subsections (10) to (13.02); an extension made by regulations under paragraph 24(1)(g) (work-sharing) is outside it and is added afterwards. This is a reading, not a ruling. Asserted (a benefit period of 109 weeks).
11. A claimant who is paid pregnancy benefits (15 weeks) and parental benefits at the 61-week election has a benefit period of 78 weeks (2 weeks more than the total of the maxima, 15 + 61), extended by 26 weeks (fork F-13). Asserted.
12. The maximum weeks by reason (s 12(3)): pregnancy 15, parental 35 or 61 by election, sickness 26, compassionate care 26, critically ill child 35, critically ill adult 15; where the weeks are divided between two claimants, 40 or 69 (s 12(4)(b)). Asserted.
13. Under the 61-week election two claimants can divide at most 69 weeks, so they cannot each take 35 (70); neither can be paid more than 35 or 61 (s 23(4), (4.11)). Asserted.
14. Compassionate care (26 weeks), critically ill child (35) and critically ill adult (15) are limits shared by all claims under the Act for the same person (s 12(4.1), (4.4), (4.5)); what is left is the limit less what any claimant has been paid. Asserted.
15. For a seasonal worker (s 12(2.3)) the dates are inclusive at both ends, the 260 weeks are 1,820 days ending the day before the benefit period begins, and an earlier benefit period that began before those 260 weeks still counts if the claimant was notified of payment or non-payment for a week within them (s 12(2.4)). Asserted at each edge.
16. A week with earnings is deemed to be the waiting-period week if what is left of the weekly benefit after deducting the earnings above $50 (rate under $200) or above 25% of the rate (rate of $200 or more) is more than zero (s 13.1). Asserted at the edges.
17. The rate of weekly benefits is 55% of the weekly insurable earnings, or 33% for the weeks of parental benefits at the 61-week election; both are rounded to the nearest dollar with the higher dollar on a tie (55% of 50 is 27.50, paid as 28), and the maximum rate (s 17) is 55% of the maximum yearly insurable earnings over 52, rounded the same way (65,000 gives 687.50, paid as 688). Asserted.
18. The maximum weekly insurable earnings is $750 for a benefit period beginning in 1997 to 2000, and after 2000 the maximum yearly insurable earnings over 52; the text gives no figure for a benefit period before 1997, and the encoding answers NOTHING. Asserted.
19. Earnings in a week of unemployment cost 50 cents on the dollar up to 90% of the weekly insurable earnings and a dollar on the dollar above it (s 19(2)); at weekly insurable earnings of 500, earnings of 500 cost 275 and earnings of 1,000 cost 775. Asserted.
20. Undeclared earnings are deducted in full if, in the Commission's opinion, the claimant knowingly failed to declare them; otherwise the undeclared earnings less the difference between the s 19(2) amounts counting all earnings and those applied to the declared earnings (s 19(3)(a)); the deduction then takes the whole of each consecutive week's benefits until it is used up (s 19(3)(b)). Asserted.
21. The deduction for a working day on which the claimant is not entitled is one fifth of the weekly rate, rounded per day (s 20): at a weekly rate of 402.50 one day costs 81 (80.50 is a tie and rounds up). Asserted.
22. The pregnancy period runs from the first day of the week 12 weeks before the week confinement is expected (or the week it occurs, if earlier) to the last day of the week 17 weeks after the later of the two, and is extended by the child's weeks in hospital but never past the week 52 weeks after confinement (s 22(2), (6), (7)). Asserted.
23. In s 23(6)(b) "that claimant" is, read literally, the major attachment claimant, but the subsection sends the reader to section 152.05, which governs the self-employed individual; it is read as the individual (fork F-23-6). Asserted.
24. The 52 weeks of ss 23.1(4), 23.2(3) and 23.3(3) are the 364 days beginning with the Sunday of the first week, so the period ends on a Saturday; it ends earlier at the end of the week in which the benefits are exhausted or the person cared for dies. Asserted.
25. Compassionate care benefits are not payable for a child in the child's critically-ill-child period (s 23.2(10)), and adult benefits are not payable in the 52 weeks after benefits were paid for the same person as a critically ill child (s 23.2(10.1)). Asserted.
26. s 12(2.1): for a benefit period beginning from 27 September 2020 to 25 September 2021 the general maximum is 50 weeks, except for a claimant under the Employment Insurance (Fishing) Regulations. Asserted at both ends of the period.
27. No regulation in the deposited Regulations names a shorter period for s 23.1(5), the "other circumstances" of ss 10(5.1)-(5.3), 23.1(6), 23.2(5) and 23.3(4), the "prescribed requirements" of the deferrals, or a reduction under s 21(2), 23.1(10) or 23.2(11) (regs 76.16 and 76.17 deal only with ss 22 and 23). Checked by searching the Regulations on 2026-10-24; not asserted by a case, because it is a statement about a text outside this range.

## What the stable binary does not accept

Binary: `l4 1.6.98 (main, 7689b0d, 2026-10-19)`.
Everything in this folder runs on it with no `DiagnosticSeverity_Error` or `_Warning`; nothing needs `unstable`.

**Measured by this piece** (each hit while writing, and fixed):

- A multi-line chain `append a` / `(append b ...)` with the continuation lines at the column of `append` is a parse error, `unexpected (`. Rewritten as `concat (LIST a, b, ...)` with each member a named helper in `WHERE`, it is accepted (a one-line chain was not tried). Used in the seat's `earlier benefit periods`.
- A lambda `any (GIVEN years YIELD <multi-line body>) list` where the body spans several lines is the same parse error. A named rule with the lambda's variable as a parameter, called by a one-line lambda, is accepted (`s 12(2.5) the earlier benefit period began during the period around the week that is n times 52 weeks before`).
- A list of two records written `LIST R OF a, b, c, R OF d, e, f` is read as one application with six arguments: "expects 3 arguments, but you are applying it to 6". Each record needs its own brackets: `LIST (R OF a, b, c), (R OF d, e, f)`.
- A large seat is slow to run. `ei1-seat.l4` (119 exported questions that call nine modules) and `ei1-cases-seat.l4` (464 assertions over it) together take about 70 seconds to type-check and run on this binary, and the whole `check.sh` takes 167 seconds. Nothing is wrong with either file; split the seat if a faster loop is wanted.

**From the keel's list, relied on here and not re-measured:** `YMD` exists only through `eia-core`; a percent literal as a bare argument needs brackets (`f (6.5%)`, and here `fromMaybe (25%) x`); a record type with spaces in its name is backticked before `OF`; `(f x)'s field` does not parse, so a field is read in a rule that takes the record; every rule needs its own `GIVEN`.

**From `dialects.md`, none used in these files:** `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, a section `GIVEN`, `TYPICALLY`, opaque `DECLARE`, sets, `EVERY`, `RULES EFFECTIVE DATE` and the temporal built-ins, `@lang`, infix `EXPONENT`, `MUST DO`, the spelling `WAIT UNTIL`, an input named in an action. This piece has no regulative rule: nothing in Part I (ss 6 to 23.3) is stated as an obligation with a deadline that a party performs; the Act states entitlements and conditions. Where the text does not answer, a rule returns `NOTHING` (`s 7.1(5) the class of the violation`, `s 12(3) ...` for the regular reason, `s 12(4.01) ...`, `s 14(1.1) ...`, `s 14(2) ...`) and a case asserts it.

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder, after the last edit to any `.l4` file (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so). It took 167 seconds.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ei1-benefit-period.l4                          0         0       0        0         0
ei1-caring.l4                                  0         0       0        0         0
ei1-cases-seat.l4                              0       464       0        0         0
ei1-disentitlement-deductions.l4               0         0       0        0         0
ei1-illness-pregnancy.l4                       0         0       0        0         0
ei1-interpretation.l4                          0         0       0        0         0
ei1-parental.l4                                0         0       0        0         0
ei1-payment.l4                                 0         0       0        0         0
ei1-qualifying.l4                              0         0       0        0         0
ei1-rate.l4                                    0         0       0        0         0
ei1-seat.l4                                    0         0       0        0         0
ei1-tests-benefit-period.l4                    0       156       0        0         0
ei1-tests-caring.l4                            0       113       0        0         0
ei1-tests-disentitlement-deductions.l4         0        58       0        0         0
ei1-tests-illness-pregnancy.l4                 0        44       0        0         0
ei1-tests-interpretation.l4                    0        64       0        0         0
ei1-tests-parental.l4                          0        79       0        0         0
ei1-tests-payment.l4                           0       123       0        0         0
ei1-tests-qualifying.l4                        0       180       0        0         0
ei1-tests-rate.l4                              0        64       0        0         0
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
TOTAL (24 modules)                             0      1345       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
exit 0  seconds 167
```

Zero errors, zero failed, zero refused, no expected failures: 1,345 assertions satisfied (464 in the seat cases and 881 in the nine test files). The layer-1 modules and the seat carry no assertions of their own, so their rows show 0. The keel's four modules (`eia-core*.l4`) are the same as delivered; their tests were not copied here.

`python3 -I srcrefs.py check --refs S.C.-1996-c.-23.txt ei1-*.l4` (the Act's raw file; this piece holds no module of the Regulations) prints:

```
srcrefs check: 432 src: lines, 164 runs, 231 locators, 0 problems
```

`l4 check` on each of the 20 `ei1-*.l4` files, run after the final edit, prints `Check succeeded` and no "follows code on its line", "is at the end of the file", "Unknown annotation" or warning line.

## Before this is worth relying on

What would need doing before this is worth relying on:

1. **A person who knows the law should read layer 1 against the text, section by section.** Nothing here has been reviewed by a domain expert, and the text is a converter's rendering, not the official text.
2. **The Regulations are not encoded.** This piece takes as inputs everything the Act leaves to them: the interruption of earnings (regs 14, 14.01), the regional rate (reg 17 and Schedule I of the Regulations), a full working week (regs 29 to 31), the family supplement (reg 34), the waiting period earnings (reg 39), illness and pregnancy (regs 40, 41), the certificate outside Canada (reg 41.2), the division of weeks (reg 41.6), the reduction for provincial plans (regs 76.16, 76.17), the seasonal criteria (reg 77.992). Two Regulations that change the answers of this piece are in nobody's input here: reg 39.1 (the waiting period is waived for an apprentice attending a required course) and reg 40(6) (the Commission may waive the waiting period where sick leave pay is payable). A user of the seat who is in either situation gets a wrong answer to "Am I entitled to be paid benefits yet" until they are brought in.
3. **The tables of Schedules I, IV and V (piece ei6) and the maximum yearly insurable earnings (the keel's s 4) are inputs;** the seat asks the person for the figure the table gives. A wrong figure gives a wrong answer without a diagnostic.
4. **Schedule II** replaces the definitions of major and minor attachment claimant for one case (piece ei6); not made here.
5. **The forks are assumed, not ruled** (see the fork register). The ones most likely to matter to a person: F-subsequent (which class a violation is), F-13 and F-23-3.2 (how many weeks a benefit period or a parental period is extended), F-cap (weekly insurable earnings held to the maximum), F-17 (whether the maximum rate also caps the rate after a family supplement), F-around and F-established (the seasonal worker test), and the "unless the benefit period is also extended under (10) to (12.1)" words of s 10(15), which are not modelled.
6. **The seat simplifies.** It asks about one violation, up to five earlier benefit periods, and the total insurable earnings of the calculation period (F-seat-violation, F-seat-earlier, F-seat-weeks); it asks the four weeks of benefits of s 19(3)(b) only.
7. **The seat layer is slow** (the seat and its cases take about 70 seconds together). A faster loop means splitting the seat by section.
8. **Section 23.3 continues at line 670** (subsections (6) onward, piece ei2). The two pieces must agree on the names of the defined terms for the division of weeks at the merge: this piece defines `s 23.1(8) ...`, `s 23.2(8) ...` and `s 23(4) ...` rules for the other sections of the family and none for s 23.3(6), which is piece ei2's.
9. **The dates carried as data** (27 September 2020 to 25 September 2021; 26 September 2021 to 7 October 2028; and the years 1997 to 2000 in s 14(1.1)) are the text's own; if the Act is amended again they must be replaced, and a rule that must give the answer of an earlier date will need a rule-version input.

