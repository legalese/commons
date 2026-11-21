# Triage, reader group 3 (Companies Act 1967, Singapore: ss205-209B, Thirteenth Schedule, ss210-215K, ss216-216B, ss355-364A, ss365-386)

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset. 706 assertions: 674 satisfied, 32 failed, 0 refused. No type errors, no warnings.
Line numbers are the line of my `#ASSERT` in `enc/tests-independent.l4` (the scenario comment is the line above). Text line numbers are lines of `inputs/CoA1967.txt`.
Format: scenario | assertion line | provision (text line) | expected | encoding answered | verdict | the two readings, or the reason.

## FAILED assertions

### ENCODER (1)

- 80c | 338 | s205B(5) (19624) | JUST FALSE | NOTHING | ENCODER | The text says a company that ceases to be dormant "thereupon ceases to be so exempt; but it remains so exempt in relation to accounts for the financial year in which it was dormant throughout". For a year it was not dormant throughout, the main clause answers "no longer exempt", so "remains exempt" is no; the encoding is silent. (If the encoder keeps the main clause in a different function this could be read as AMBIGUOUS, but the question asked is the one the text answers.)

### SCENARIO (11, my mistakes or my departures from the Guide)

- 11 | 181 | s205(7)(a) (19126) | JUST FALSE | NOTHING | SCENARIO | The function is named for a grant ("the company may ... appoint") and its gate (a three-fourths majority) failed; the Guide's grant ruling, limit 1, answers NOTHING, and the text does not close the gate with "only". I wrote JUST FALSE against the ruling.
- 79 | 332 | s205B(3)(e) (19574) | NOTHING | JUST FALSE | SCENARIO | A transaction from keeping a register under s190 is not among the disregarded transactions, so it is an accounting transaction and the company is not dormant: the "dormant" definition is a "means" definition, so JUST FALSE is right.
- 90 | 362 | s205C(6) (19686) | JUST TRUE | NOTHING | SCENARIO | The subsection is a flat negative for financial years commencing before 1 July 2015; it does not say the section applies to later years, so the later case is silent.
- 149b | 513 | s210(3) (20223) | JUST FALSE | NOTHING | SCENARIO | "may be adjourned ... if the resolution is approved by a majority ... three-fourths in value": a grant whose "if" gate failed, no "only"; the grant ruling, limit 1, answers NOTHING. I wrote JUST FALSE against the ruling.
- 209 | 683 | s215AA(2)(a) (20959) | JUST FALSE | NOTHING | SCENARIO | "satisfied ... by the joint transferees acquiring ... jointly" is not closed with "only"; separate acquisition is not stated to fail, so NOTHING by the open-list convention. (A reader could take the paragraph as the only way; I judge the text does not say so.)
- 213 | 693 | s215AB(1) (21027) | JUST FALSE | NOTHING | SCENARIO | Subsection (3) says that nothing is to be inferred about an offer from the failure of the (1) conditions, so the unmet case is silent.
- 285b | 910 | s361(1)(b) (23376) | NOTHING | JUST FALSE | SCENARIO | "(b) if the entity was registered ... immediately before that date, ceases to be so registered": an "if" condition that is unmet gives JUST FALSE (Guide, example 1). My own comment for the sister case cited the right rule and I did not apply it here.
- 291b | 926 | s362(5) (23447) | NOTHING | JUST FALSE | SCENARIO | "Upon publication ... the order takes effect": "upon" counts as "where" (Guide, delegated-definitions ruling (c)), so before publication the answer is JUST FALSE. My comment on the line states this and the expected value contradicts it.
- 301b | 960 | s364(2) (23556) | NOTHING | JUST FALSE | SCENARIO | "Upon the delivery of the certificates ... prior certificates cease to be operative": same reading as 291b; JUST FALSE before delivery.
- 356d | 1286 | s375(4) (24600) | JUST TRUE | NOTHING | SCENARIO | I added this sibling case. Subsection (4) only delays the s375(3) duty for companies incorporated before 3 January 2016 and says nothing about later companies (their duty is in (3), a different function), so the function is silent for them.
- S-D6b | 1605 | s215(8) (20802) | JUST FALSE | NOTHING | SCENARIO | "a dissenting shareholder includes ...": "includes" is open, so a shareholder who assented and transferred is not stated to be outside it. My layer-1 assertion 198b has the right value (NOTHING, passes); I wrote the seat one from ANSWERS 198, which carried the wrong "FALSE" and the wrong guide label "G-means".

### AMBIGUOUS (20)

Grant or power gated by "where", "upon", "on application" or "on being satisfied" (the Guide's split site: ruling (b) says JUST FALSE, the grant ruling says NOTHING; I wrote NOTHING, the encoding answers JUST FALSE):
- 161 | 541 | s210(10) (20367) | NOTHING | JUST FALSE | AMBIGUOUS | "Where no order has been made ... the Court may ... restrain": a winding-up order has been made. Reading 1 (grant): NOTHING. Reading 2 ("where" fails): JUST FALSE.
- 162 | 543 | s210(10) (20367) | NOTHING | JUST FALSE | AMBIGUOUS | The compromise is only with members, not creditors. Reading 1: a scope limit of the "where", NOTHING. Reading 2: the "where ... compromise ... between the company and its creditors" fails, JUST FALSE.
- 177 | 580 | s212(1) (20499) | NOTHING | JUST FALSE | AMBIGUOUS | "Where an application is made ... and it is shown ... reconstruction or amalgamation, the Court may ...": not shown. Reading 1: grant, NOTHING. Reading 2: "where" fails, JUST FALSE.
- 235 | 766 | s215H(1) (21494) | NOTHING | JUST FALSE | AMBIGUOUS | "it may, on the application ... made at any time before the date on which the amalgamation becomes effective": the application came after. Reading 1: grant gated "on application", NOTHING. Reading 2: a period fixed in the text's own words (ruling (a)) or an "on application" gate, JUST FALSE.
- 273 | 878 | s359(1) (23248) | NOTHING | JUST FALSE | AMBIGUOUS | "upon compliance by the foreign corporate entity with section 358, the Registrar may, if ... thinks fit, register": not complied. Reading 1: grant, NOTHING. Reading 2: "upon" counts as "where", JUST FALSE.
- 299b | 950 | s363(6) (23516) | NOTHING | JUST FALSE | AMBIGUOUS | "The Court, on being satisfied (a) ... (b) ... may order": none of the grounds. Reading 1: grant, NOTHING. Reading 2: "on being satisfied" is a "where"/"upon" gate, JUST FALSE.

A duty or definition whose "if" or "where" is unmet, a deeming rule with a period, or a scope limit (case-by-case questions of the Guide, or ruling (a) against ruling (c)):
- 31 | 221 | s205(13) (19205) | NOTHING | JUST FALSE | AMBIGUOUS | AGM called for a date 8 days after the notice: the deeming of compliance applies only "not more than 7 days after". Reading 1: a scope limit of the deeming rule, NOTHING (ruling (c)). Reading 2: a period fixed in the text's own words, JUST FALSE (ruling (a)).
- 231b | 756 | s215F(2) (21437) | NOTHING | JUST FALSE | AMBIGUOUS | "Where the proposal specifies a date ... the same as or later than the date the Registrar receives the documents ... the notice must be expressed to have effect on that date": the date is earlier. Reading 1: scope limit, NOTHING. Reading 2: a duty whose "where" is unmet, JUST FALSE.
- 109 | 409 | s207(9A) (19966) | NOTHING | JUST FALSE | AMBIGUOUS | "if an auditor of a public company or a subsidiary of a public company ... the auditor must immediately report": a private company that is not such a subsidiary. Reading 1: a scope limit of who the duty binds, NOTHING. Reading 2: a duty whose "if" is unmet, JUST FALSE.
- 148 | 509 | s210(2) (20209) | NOTHING | JUST FALSE | AMBIGUOUS | "The persons referred to in subsection (1) are (a) in the case of a company being wound up, the liquidator; (b) in any other case, (i) the company, (ii) any creditor, member ...": a creditor of a company being wound up. Reading 1: a list not closed with "only", NOTHING. Reading 2: the "in any other case" partition closes (a), so the creditor is outside, JUST FALSE.
- 313 | 1073 | s366(2)(h) (23684) | JUST FALSE | NOTHING | AMBIGUOUS | "not ... regarded as carrying on business ... for the reason only that it (h) conducts an isolated transaction completed within a period of 31 days": completed in 32 days. Reading 1: a period fixed in the text's own words, JUST FALSE (ruling (a)). Reading 2: a scope limit of an exemption, outside it the text is silent, NOTHING (ruling (c)).
- 314 | 1075 | s366(2)(h) (23685) | JUST FALSE | NOTHING | AMBIGUOUS | "but not being one of a number of similar transactions repeated from time to time": repeated. Reading 1: an exception that, when met, takes the case out of the exemption, JUST FALSE. Reading 2: "(other than X)" read as a scope limit, NOTHING.
- 358 | 1293 | s376 (24608) | NOTHING | JUST FALSE | AMBIGUOUS | "sufficiently served (a) if addressed ... left at or sent by post to its registered office; (b) if ...; (c) ... if": the document is sent by email. Reading 1: a list of ways not closed with "only", NOTHING. Reading 2: each way is an "if" condition and none holds, JUST FALSE (Guide, example 1).
- 383b | 1424 | s378(4) (25033) | JUST FALSE | NOTHING | AMBIGUOUS | "No foreign company ... may use in Singapore any name other than (a) the registered name (b) ...": the name used is the registered name. Reading 1: the "other than" carve-out answers "not barred", JUST FALSE. Reading 2: "(other than X)": the subsection grants no right to use X, NOTHING.
- 383c | 1426 | s378(4)(b) (25039) | JUST FALSE | NOTHING | AMBIGUOUS | Same site as 383b, for the registered business name.

"Unless" or "except" once it is met (case-by-case question of the Guide; I wrote JUST FALSE, the encoding answers NOTHING):
- 184 | 601 | s215(1) (20602) | JUST TRUE | JUST FALSE | AMBIGUOUS | 1,000 shares, the transferee already holds 200, 720 of the other 800 approve. The parenthesis "(other than shares already held at the date of the offer by the transferee ...)" follows "or of the shares of that class". Reading 1: it qualifies both limbs (I wrote this), 720 of 800 is 90 percent. Reading 2: it qualifies the class limb only, so the "all the shares" limb counts 720 of 1,000. My class-limb assertions 184c and 184d pass with the same figures, so the encoding does apply the carve-out to the class limb.
- 350a | 1243 | s373(15) (24423) | JUST FALSE | NOTHING | AMBIGUOUS | "must not make an order ... unless the Registrar is of the opinion ...": the opinion is formed. Reading 1: the "unless" is met, the bar is lifted, JUST FALSE. Reading 2: an opinion lifts the bar but gives no answer on the order, NOTHING. (The unmet side, 350b, passes.)
- 355b | 1278 | s375(2) (24579) | JUST FALSE | NOTHING | AMBIGUOUS | "deemed not to have been complied with unless the name is stated in romanised letters not smaller than ...": stated. Reading 1: unless met, JUST FALSE. Reading 2: NOTHING.
- 368a | 1345 | s377A(2) (24763) | JUST FALSE | NOTHING | AMBIGUOUS | "An application is not valid unless received within 6 years after the date ...": received on the last day. Reading 1: unless met, "not valid" is JUST FALSE. Reading 2: NOTHING. (The late side passes.)
- 387b | 1448 | s378(12) (25123) | JUST FALSE | NOTHING | AMBIGUOUS | "must not be registered ... unless the name has been reserved": reserved. Reading 1: unless met, JUST FALSE. Reading 2: NOTHING. (The unreserved side, 387a, passes.)

Period counts that differ: none. Every period I asserted (the event day not counted, the last day in time, "at least N" counted as the Nth anniversary) agreed with the encoding on all 674 passes and no failure above turns on a count.

## GAPS (12; no assertion is written, each is also listed at the end of `enc/tests-independent.l4`)

- 125 | none | s209B (20178) | NOTHING (SILENT) | no function | GAP | The section is repealed; there is nothing to ask.
- 175 | none | ss211A to 211J (20495) | NOTHING (SILENT) | no function | GAP | Repealed.
- 182 | none | s213 (20588) | NOTHING (SILENT) | no function | GAP | Repealed.
- 222b | none | s215C(6) (21246) | maximum fine NOTHING | no function | GAP | The section states no penalty and the encoding has no function for its maximum fine; the offence itself is asserted in 222 (passes).
- 236 | none | s215I(1) (21516) | TRUE at $100 against $100, FALSE at $99 | no function | GAP | The amounts of assets and liabilities are not inputs of any function; only the board's opinion is.
- 255 | none | s216(2)(a) (21726) | NOTHING (open list) | no function | GAP | "Compensation to the applicant personally" has no input; the (a) function takes only the Court's opinion and the aim of the order.
- 304 | none | s364 (23546) | maximum fine NOTHING | no function | GAP | No penalty is stated and the encoding has no function for the maximum fine of a s364(1) default.
- 305 | none | s364A (23590) | TRUE | no function | GAP | The Minister's regulation-making power is not encoded.
- 311b | none | s366(2)(c) (23668) | NOTHING | no function | GAP | A company that also runs a sales office: the function takes one activity at a time, so "for the reason only" cannot be tested.
- 318 | none | s368(1)(e) (23747) | TRUE for a natural person resident in Singapore; FALSE for a company or a person resident abroad | no function | GAP | Whether the person named is a natural person resident in Singapore is not an input; only whether the notice was lodged.
- 397b | none | s380(1)(c) (25237) | NOTHING for a person who ceased to be a member 9 years ago | no function | GAP | The "previous 7 years" has no input; the function takes only whether the register contains the date.
- 406 | none | s385 (25353) | NOTHING (SILENT) | no function | GAP | Repealed.

## Counts

- Scenarios: 406 numbered in `ANSWERS.md` (19 marked SILENT), plus 53 seat items in its "Seat addendum". 397 of the 406 have at least one assertion; the other 9 are GAPS (125, 175, 182, 236, 255, 304, 305, 318, 406). Three further GAPS (222b, 311b, 397b) are halves of scenarios that do have an assertion.
- Assertions: 706 in all. 609 are layer-1 (including sibling cases with a letter suffix) and 97 are seat questions. 674 satisfied, 32 failed, 0 refused.
- Seat layer: 63 distinct seat questions asserted in 97 assertions (sgc2 11 questions in 24 assertions, sgd 13 in 25, sgf 11 in 13, sge 11 in 14, sgg 17 in 21). One seat assertion failed (S-D6b, SCENARIO).
- Triage lines: ENCODER 1, SCENARIO 11, AMBIGUOUS 20, GAP 12.
