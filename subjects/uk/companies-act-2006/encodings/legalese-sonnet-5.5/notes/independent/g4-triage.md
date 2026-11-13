# Triage — Companies Act 2006 (UK), ranges coa18-coa22 (lines 10757-14665), review run dst-rev-coa4

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset; diagnostics read, not the exit code.
Result: 356 assertions written, 343 satisfied, 13 failed, 0 refused; 13 GAPs (scenarios with no function to ask); no other diagnostic (no type or name errors).
Scenarios in `ANSWERS.md`: 281, written before any `.l4` file was opened.
Assertion lines: 268 are the scenarios of ANSWERS.md that a function could answer (281 minus 13 gaps), S-numbered lines are seat questions (68), X-numbered lines are 20 extra edge cases (dates across month ends, leap days, Good Friday and Easter Monday) written in step 4 after the modules were opened; their expected values are still from the text.
Seat questions asked per Part: 22: 5, 23: 5, 24: 5, 25: 7, 26: 5, 26A: 5, 27: 7, 28: 7, 29: 2, 30: 7, 31: 8, 32: 3, 33: 2.
Parts 29, 32 and 33 have fewer than five seat questions in the seat modules (2, 3 and 2); every one of them is asked.
One of my own mistakes, fixed before the final run and so not a finding: X1's first version wrote its working-day lambda as `NOT (a) AND NOT (b)`, which parsed as a different function and made the encoding's 2026-04-23 look wrong; with explicit brackets the encoding's 2026-04-27 (the 15th working day after 2026-04-02) agrees with the text.

Format: scenario | assertion line in `enc/tests-independent.l4` | provision (text line) | my expected | the encoding answered | verdict | note.

## Failed assertions

52 | line 135 | s.853G(6)(a) (L11528) 4.99% holder: must name and address be delivered | JUST FALSE | NOTHING | SCENARIO | "The information is— (a) ... each person who ... held at least 5%" is a list not closed with "only"; the family convention gives NOTHING, not FALSE, for a holder below the limit. I misapplied the convention.
65 | line 147 | s.859H(1) (L11703) a charge on acquired property (s.859C), is s.859H engaged | NOTHING | JUST FALSE | SCENARIO | "This section applies if (a) a company creates a charge to which section 859A or 859B applies" is an "if" condition: the family convention gives FALSE. I expected NOTHING, wrongly.
83 | line 165 | s.860(7)(a) (L11856) a charge for rent issuing out of land | JUST FALSE | NOTHING | SCENARIO | "This section applies to the following charges— (a)...(i)" is a list not closed with "only"; the carve-out in (a) does not stop the rent charge falling in another limb. The convention gives NOTHING.
89 | line 171 | s.876(1) (L11990) an unlimited company: must it keep a register of charges | NOTHING | JUST FALSE | ENCODER | "Every limited company shall keep available for inspection a register of charges" is a duty limited by its own wording; the convention says that is not the text's no for a case outside the limit (an unlimited company), so NOTHING. The encoding labels the branch "the text says no in its own words" (`coa19-ch1-registrar.l4:396`); the same family treats s.793(1) and s.939(4) as NOTHING for this shape.
95 | line 177 | s.887(2) (L12120) a fixed (not floating) charge: is the statement accompanied as the subsection requires | JUST TRUE | JUST FALSE | AMBIGUOUS | Reading 1: the subsection requires accompaniment only for a floating charge, so a fixed-charge statement meets it with nothing attached (TRUE). Reading 2 (the encoding's): "accompanied as required" is false because nothing accompanies it and the encoder codes "If the charge is a floating charge" as FALSE for a fixed charge. The function's polarity is unclear for the fixed case.
215 | line 294 | s.992(6) (L13924) directors' report for a year beginning 2006-05-19 | JUST FALSE | NOTHING | SCENARIO | "apply in relation to directors' reports for financial years beginning on or after 20th May 2006" is a grant limited by its own wording; the convention gives NOTHING for a year outside the limit.
226 | line 306 | s.994(1)(a) (L13938) affairs prejudicial only to other members, not the petitioner | JUST FALSE | NOTHING | SCENARIO | The ground carries "(including at least himself)" as its own limit; the convention gives NOTHING outside it.
229 | line 309 | s.995(1) (L13949) a company with no s.437 report, no s.447/448 power and no Part 11 FSMA step | JUST FALSE | NOTHING | SCENARIO | "This section applies to a company in respect of which (a)...(d)" has no "only"; NOTHING under the convention.
232 | line 312 | s.996(2) (L13962) may the order contain a provision not in the list (removing a director) | NOTHING | JUST TRUE | SCENARIO | I overlooked s.996(1) (L13961): "may make such order as it thinks fit for giving relief", so the court may; the encoding's TRUE rests on s.996(1).
248 | line 329 | s.1006(5) (L14112) is unawareness of the application a defence | NOTHING | JUST FALSE | SCENARIO | The function only has the input "took all reasonable steps"; with that input false it correctly answers that s.1006(5) gives no defence on those facts. My question (unawareness) cannot be put to this function; s.1007(5)(a) (L14136) is the unawareness defence and scenario 247 (satisfied) asks it.
274 | line 357 | s.1040(1)(b)(i) (L14628) a company formed under the Companies Act 1985 | JUST FALSE | NOTHING | SCENARIO | "This section applies to (a) ... (b)..." is not closed with "only", and (b)(iii) ("otherwise duly constituted according to law") may still catch such a company; NOTHING is the convention's answer.
281 | line 364 | s.1043(1) (L14652) a body incorporated in the UK with its principal place of business in France | JUST FALSE | NOTHING | SCENARIO | "This section applies to bodies corporate incorporated in and having a principal place of business in the United Kingdom, other than—" is a scope sentence without "only"; NOTHING.
S26A-5 | line 422 | s.901I(1) (L12455) seat: employer in a non-money-purchase scheme, notice required to go to a creditor, not yet sent to the Regulator: must it also be sent | JUST TRUE | JUST FALSE | AMBIGUOUS | The question's name says "must a notice to creditors also be sent to the Pensions Regulator" (reading 1: yes, it must: TRUE) but its export text says "must ..., and has it been?" and the body answers "has it been sent as required" (reading 2: not yet, so FALSE). A person reading only the title would take FALSE as "no duty".

## Gaps (no function to ask the scenario)

54 | - | s.853L(2)(a) (L11571) the daily default fine in pounds | JUST 500 | no layer-1 function (the pounds need the level-4 value, which the Act does not state) | GAP | Asked through the seat question: S24-4, satisfied.
56 | - | s.854 (L11579) duty to deliver annual returns | NOTHING | no function; the module comments that ss 854-859 show only dots and are on its coverage table | GAP | Nothing to model; recorded only because I wrote a not-covered scenario for it.
96 | - | s.893(9) (L12197) negative resolution procedure | JUST TRUE | no function | GAP | The encoder marks such procedure provisions as "machinery (inert)".
97 | - | s.894(2) (L12202) affirmative resolution procedure | JUST TRUE | no function | GAP | Same.
114 | - | s.901B(3) (L12357) affirmative resolution procedure | JUST TRUE | no function (`coa20-part26a.l4:137`, "machinery (inert, reason 2). No L4.") | GAP | Same.
123 | - | s.901I(6),(7) (L12468-12469) approval after being made | JUST TRUE | no function | GAP | Same.
143 | - | s.915(4) (L12696) does s.915 disapply s.910 | NOTHING | no function asks it; `s 910(6)` lists only ss.915A and 918A | GAP | On reflection the text supports the encoding: s.910(6) (L12635) lists only ss.915A and 918A as exceptions, so my NOTHING was too weak (this would be SCENARIO if there were a function).
167 | - | s.943(4),(5) (L13157-13158) which body discharges the rule-making function | JUST FALSE | no function | GAP | Constitutional machinery; not modelled.
178 | - | s.965 (L13416) Order in Council extension to Gibraltar | NOTHING | no function | GAP | Not modelled.
194 | - | s.979(2) (L13614) 90% in value but 89% of voting rights | JUST FALSE | the layer-1 test takes a list of block records | GAP | Asked through seat question S28-4, satisfied.
195 | - | s.979(2) (L13614) 90% in value and 90% of voting rights | JUST TRUE | same | GAP | Asked through seat question S28-5, satisfied.
206 | - | s.983(2) (L13722) 90% in value, 88% of voting rights | JUST FALSE | the layer-1 test takes a record of ten or more fields | GAP | Asked through seat question S28-7, satisfied.
225 | - | s.993 (L13926) civil liability to contribute | NOTHING | no function | GAP | The Part is silent; nothing to model.

## Counts by verdict word

ENCODER: 1
SCENARIO: 10
AMBIGUOUS: 2
GAP: 13
