# FRAGMENT-G5: Articles 13 and 14 of the Charities (Jersey) Law 2014

Group G5 (effects of registration; powers of the court over a registered charity).
Written by ENCODER G5 for the INTEGRATOR, who merges it into `NOTES.md`.
Status: complete for the whole scope (Articles 13 and 14, 58 coverage rows, none `deferred`).
The check script of the group, adapted from the skill's `assets/check.sh` and the fleet's template, is `work/g5/check.sh`; what it printed is in section 10.
Nothing in this fragment is a claim about what a domain expert thinks: no domain expert has read the modules against the Law.

## 0. Files and what is in them

All in `DEPOSIT`, every name starting `g5-`, each importing only `prelude`, `daydate`, `domain` and `g5-` modules (check.sh verifies the imports).

| file | holds |
| --- | --- |
| `g5-interpretation.l4` | the fork points as enumerations, the record `Interpretation of Articles 13 and 14` (one field per fork, `TYPICALLY` the reading taken), `the favoured interpretation of Articles 13 and 14`, and 19 generated variants (one non-favoured reading each, plus two combinations) |
| `g5-nouns.l4` | the nouns domain.l4 does not hold: the acts (`Act under Article 13`, `Act under Article 14`), the facts of each limb of 13(6), the provision about amending purposes, the annual-return records, the relief and payment Orders, the court's orders; `DECLARE` only |
| `g5-art13-effects.l4` | Article 13(1) to (5), (11) and (13), the Commissioner's approvals and permissions the paragraphs imply, and the IP27 decision record |
| `g5-art13-reporting.l4` | Article 13(6) to (10) and (12): the eight reports, the annual return, the year, the Minister's Orders, IP29 |
| `g5-art14-court-powers.l4` | Article 14 whole |
| `g5-tests-fixtures.l4` | named cases shared by the tests (values only) |
| `g5-tests-art13-effects.l4`, `g5-tests-art13-reporting.l4`, `g5-tests-art14.l4` | the tests of the three rule modules, with `#TRACE` expectations in `-- EXPECT:` comments |
| `g5-tests-forks.l4` | the discriminating case of each fork under each reading |
| `g5-tests-properties.l4` | a property test of the year of the annual return (Article 13(7), F5.2 with F5.11): over 104 reference days, under four settings of the forks, the year found contains the day and the next year begins the day after this one ends |
| `g5-tests-red.l4` | assertions MEANT TO FAIL: the answer of the other reading, asked of the reading taken (16, counted) |

Change from the PLAN: PLAN (b) proposed two modules, `g5-art13-effects` and `g5-art14-court-powers`.
Article 13 would have been one module of about 1,200 lines, so it is split along its own paragraphs: `g5-art13-effects` (paragraphs (1) to (5), (11), (13)) and `g5-art13-reporting` (paragraphs (6) to (10), (12)).
The nouns and the fork record are in modules of their own because three rule modules share them.
The export names of PLAN (b) are kept exactly (section 5 lists every export); a module name is not part of a wiring.
No disposition was changed from the PLAN: all 58 rows are `encoded`.

## 1. Coverage

One row per provision of the scope, in the Law's numbering.
"Rule or construct" names what carries the row; where a paragraph is carried by one arm of a larger rule, the arm is named.
Rules that are helpers of a fork are named in section 2.

| id | provision | disposition | module | rule or construct | note |
| --- | --- | --- | --- | --- | --- |
| 13 | Article 13 | encoded | g5-art13-effects; g5-art13-reporting | the Article as a whole: its paragraphs are the rows below, in the Law's order |  |
| 13(1) | Article 13(1) | encoded | g5-art13-effects | `Art 13(1) paragraphs (2) to (4) apply on the day`; `Art 13(1) the registration has not ended on the day` | fork F5.6; trap T15 (retrospective deregistration) tested |
| 13(2) | Article 13(2) | encoded | g5-art13-effects | `Art 13(2) the provision of the constitution is of no effect`; `Art 13(2) the purpose is not charitable`; `Art 13(2) the purpose is a charitable purpose` | fork F5.7; trap T6 (constitutional Law) handled as a Boolean on the provision |
| 13(3) | Article 13(3) | encoded | g5-art13-effects | `Art 13(3) paragraph (3) applies to the provision`; `Art 13(3) the amendment of purposes is subject to evidence and approval` | the result is TRUE when (3) does not apply or both limbs are met |
| 13(3)(a) | Article 13(3)(a) | encoded | g5-art13-effects | conjunct "(a)" of `Art 13(3) the amendment of purposes is subject to evidence and approval` | the Commissioner's satisfaction is an input |
| 13(3)(b) | Article 13(3)(b) | encoded | g5-art13-effects | conjunct "(b)" of the same rule; `Art 13(3)(b) the Commissioner may approve the proposed amendment of purposes` | "prior" is a Boolean fact; the Commissioner's power to approve is implied (33(2)(d)) |
| 13(4) | Article 13(4) | encoded | g5-art13-effects | `Art 13(4) the registered charity must provide public benefit in accordance with its statement`; `Art 13(4)(b) the registered charity that requests approval of an amendment of its statement must provide evidence` |  |
| 13(4)(a) | Article 13(4)(a) | encoded | g5-art13-effects | `Art 13(4) the registered charity must provide public benefit in accordance with its statement` | standing duty, no time in the Law |
| 13(4)(b) | Article 13(4)(b) | encoded | g5-art13-effects | `Art 13(4)(b) the registered charity that requests approval of an amendment of its statement must provide evidence`; `Art 13(4)(b) the Commissioner may approve the proposed amendment of the statement` | the Commissioner's power to approve is implied (33(2)(e)) |
| 13(5) | Article 13(5) | encoded | g5-art13-effects | `Art 13(5) the registered charity in the restricted section must ensure it meets its condition` | standing duty while in the restricted section |
| 13(5)(a) | Article 13(5)(a) | encoded | g5-art13-effects | `Art 13(5) the registered charity in the restricted section meets what paragraph (5) requires`, limb "(a)" | fork F5.8 |
| 13(5)(b) | Article 13(5)(b) | encoded | g5-art13-effects | the same rule, limb "(b)"; `Art 13(5)(b) the Commissioner may give prior permission to remain in the restricted section` | fork F5.8; no provision confers the permission in terms |
| 13(6) | Article 13(6) | encoded | g5-art13-reporting | `Art 13(6) the registered charity must promptly report the matter`; `Art 13(6) the report was made promptly`; `Art 13(6) the duty to report on the reading of promptly` | forks F5.1, F5.10; period P8 |
| 13(6)(a) | Article 13(6)(a) | encoded | g5-art13-reporting | `Art 13(6) the matter falls within the paragraph`, arm "(a)" |  |
| 13(6)(b) | Article 13(6)(b) | encoded | g5-art13-reporting | the same rule, arm "(b)" | consumes IP18; feeds 12(6) |
| 13(6)(c) | Article 13(6)(c) | encoded | g5-art13-reporting | the same rule, arm "(c)" |  |
| 13(6)(d) | Article 13(6)(d) | encoded | g5-art13-reporting | the same rule, arm "(d)" | consumes IP15 and IP16 |
| 13(6)(e) | Article 13(6)(e) | encoded | g5-art13-reporting | the same rule, arm "(e)"; `Art 13(6)(e) a governor of the charity is the one named and has a reportable matter` | consumes IP21 (field `reportable matters` of the `Governor`) |
| 13(6)(f) | Article 13(6)(f) | encoded | g5-art13-reporting | the same rule, arm "(f)" | the likelihood is the charity's judgement: an input |
| 13(6)(g) | Article 13(6)(g) | encoded | g5-art13-reporting | the same rule, arm "(g)" | only for a charity entered in the restricted section |
| 13(6)(h) | Article 13(6)(h) | encoded | g5-art13-reporting | the same rule, arm "(h)"; `Art 13(6)(h) the Minister may by Order prescribe a further matter to be reported` | power typed MAY (the Minister); the Order is an input |
| 13(7) | Article 13(7) | encoded | g5-art13-reporting | `Art 13(7) the registered charity must send an annual return`; `Art 13(7) the year to which the return relates`; `Art 13(7) the annual return contains the information paragraph (7) requires`; `Art 13(7) the Minister may by Order prescribe a further matter for the annual return` | forks F5.2, F5.11, F5.13; period P9; IP33 |
| 13(8) | Article 13(8) | encoded | g5-art13-reporting | `Art 13(8) the annual return is late`; `Art 13(8) the consequence of lateness`; `Art 13(8) the Minister may by Order provide for the format and timing of the annual return`; the two named refusals | fork F5.5; period P10; no Order in the sources: lateness and its consequence are named refusals |
| 13(9) | Article 13(9) | encoded | g5-art13-reporting | `Art 13(9) an Order under Article 13(9) applies to the registered charity` | IP29 (produced here) |
| 13(9)(a) | Article 13(9)(a) | encoded | g5-art13-reporting | `Art 13(9)(a) the Minister may by Order require payment details in the annual return`; `Art 13(9)(a) the payment falls to be included in the annual return`; `Art 13(9)(a) the annual return gives the details of the payments the Order requires` | uses the year of F5.2 |
| 13(9)(b) | Article 13(9)(b) | encoded | g5-art13-reporting | `Art 13(9)(b) the Minister may by Order require a statement of intentions`; `Art 13(9)(b) the registered charity must provide a statement of its current intentions` | feeds 11(2)(e)(ii) through IP29 |
| 13(9)(c) | Article 13(9)(c) | encoded | g5-art13-reporting | `Art 13(9)(c) the Minister may by Order provide for entry on the register` | feeds 8(3)(m) through IP29; the Commissioner's entry duty under the Order is G3's (8(3)(m)) |
| 13(10) | Article 13(10) | encoded | g5-art13-reporting | `Art 13(10) the Minister may by Order relieve small charities`; `Art 13(10) the Minister may by Order provide the relief`; `Art 13(10) the effect of the relief Order on the provision` | fork F5.3; trap T18 |
| 13(10)(a) | Article 13(10)(a) | encoded | g5-art13-reporting | `Art 13(10) the effect of the relief Order on the provision`, arm `relief by disapplication, Article 13(10)(a)` |  |
| 13(10)(b) | Article 13(10)(b) | encoded | g5-art13-reporting | the same rule, arm `relief by modification, Article 13(10)(b)` |  |
| 13(11) | Article 13(11) | encoded | g5-art13-effects | paragraph (a) and (b) below |  |
| 13(11)(a) | Article 13(11)(a) | encoded | g5-art13-effects | `Art 13(11)(a) the registered charity must not make a payment inconsistent with its statement`; `Art 13(11)(a) the payment is inconsistent with the statement`; `Art 13(11)(a) the penalty for a payment inconsistent with the statement` | fork F5.14; no penalty stated (IP13: a contravention is misconduct) |
| 13(11)(b) | Article 13(11)(b) | encoded | g5-art13-effects | `Art 13(11)(b) the registered charity may apply for permission to amend the statement`; `Art 13(11)(b) the Commissioner may give permission to amend the statement` | no decision rule and no appeal right stated (T12) |
| 13(12) | Article 13(12) | encoded | g5-art13-reporting | `Art 13(12) the States may require a charity to avoid or report and remedy a later ground for refusal`; `Art 13(12) the situation is one the Regulations may require the charity or its governors to avoid or to report and remedy` | power typed MAY (the States); the Regulations are an input |
| 13(13) | Article 13(13) | encoded | g5-art13-effects | `Art 13(13) paragraphs (2) and (3) yield to an order under the Loi of 1862` |  |
| 14 | Article 14 | encoded | g5-art14-court-powers | the Article as a whole: its paragraphs are the rows below, in the Law's order |  |
| 14(1) | Article 14(1) | encoded | g5-art14-court-powers | `Art 14(1) the powers of the court are exercisable on the application`; `Art 14(1) the court may exercise the powers on the application`; `Art 14(1) the court's permission once the application is made` | power typed MAY (the court); the applicants' own permission is encoded too |
| 14(1)(a) | Article 14(1)(a) | encoded | g5-art14-court-powers | `Art 14(1)(a) there is or has been misconduct in the administration of the charity` | fork F5.4; consumes IP12 |
| 14(1)(b) | Article 14(1)(b) | encoded | g5-art14-court-powers | `Art 14(1)(b) it is necessary or desirable to exercise the power to protect the property or secure its proper application` | the court's appearance is an input |
| 14(2) | Article 14(2) | encoded | g5-art14-court-powers | `Art 14(2) the court may make any order it sees fit`; `Art 14(2) the order is one the court sees fit` | fork F5.12; the content of the order is an input |
| 14(3) | Article 14(3) | encoded | g5-art14-court-powers | `Art 14(3) the court may make the order`; `Art 14(3) the order is of a kind the paragraph lists`; `Art 14(3) the order is in operation on the day` | IP31; fork F5.9 |
| 14(3)(a) | Article 14(3)(a) | encoded | g5-art14-court-powers | arm "(a)" of `Art 14(3) the order is of a kind the paragraph lists` | directed at the charity or a governor, and saying what it forbids |
| 14(3)(a)(i) | Article 14(3)(a)(i) | encoded | g5-art14-court-powers | constructor `referring to or holding out the entity as a charity or Jersey charity, or as being charitable, having charitable purposes or providing public benefit` of the noun `Action that an order under Article 14(3)(a) forbids` (g5-nouns) |  |
| 14(3)(a)(ii) | Article 14(3)(a)(ii) | encoded | g5-art14-court-powers | constructor `soliciting donations from the public, as specified in the order` of the same noun | "donation" and "solicit" are construed by an Order under 9(3)(b): an input |
| 14(3)(a)(iii) | Article 14(3)(a)(iii) | encoded | g5-art14-court-powers | constructor `taking any other action specified in the order` of the same noun |  |
| 14(3)(b) | Article 14(3)(b) | encoded | g5-art14-court-powers | arm "(b)" of `Art 14(3) the order is of a kind the paragraph lists` | period: fork F5.9 |
| 14(3)(c) | Article 14(3)(c) | encoded | g5-art14-court-powers | arm "(c)" |  |
| 14(3)(d) | Article 14(3)(d) | encoded | g5-art14-court-powers | arm "(d)"; `Art 14(3)(d) the order is directed at a governor or another person concerned in the management or control of the charity` |  |
| 14(3)(e) | Article 14(3)(e) | encoded | g5-art14-court-powers | arm "(e)"; `Art 14(3)(e) the order is directed at a person who holds property on behalf of the charity or of a governor` | "regulated financial services business" is not needed: it only illustrates the person |
| 14(3)(f) | Article 14(3)(f) | encoded | g5-art14-court-powers | arm "(f)" |  |
| 14(3)(g) | Article 14(3)(g) | encoded | g5-art14-court-powers | arm "(g)" | period: fork F5.9 |
| 14(3)(h) | Article 14(3)(h) | encoded | g5-art14-court-powers | arm "(h)"; `Art 14(3)(h) the order is directed at a governor or another person who appears to be responsible for misconduct` | the court's appearance is an input (IP14 is the governor test of 18(4)) |
| 14(3)(i) | Article 14(3)(i) | encoded | g5-art14-court-powers | arm "(i)" |  |
| 14(4) | Article 14(4) | encoded | g5-art14-court-powers | `Art 14(4) the court may amend or revoke an order`; `Art 14(4) the application is by one of the four` |  |
| 14(5) | Article 14(5) | encoded | g5-art14-court-powers | `Art 14(5) the powers apply in addition to other powers and despite the constitution` |  |
| 14(5)(a) | Article 14(5)(a) | encoded | g5-art14-court-powers | `Art 14(5)(a) the court may act under Article 14 or under another power` |  |
| 14(5)(b) | Article 14(5)(b) | encoded | g5-art14-court-powers | `Art 14(5)(b) the powers of the court under Article 14 are exercisable despite the constitution` | the constitutional fact is deliberately not read |
| 14(6) | Article 14(6) | encoded | g5-art14-court-powers | `Art 14(6) the Commissioner's own power is unaffected by the powers of the court` | the court's action is deliberately not read |

Counts: 58 rows; `encoded` 58; `inert` 0; `refused` 0; `out-of-scope` 0; `deferred` 0.
Named refusals inside encoded rows (a row is still `encoded`): four.
The due date and the consequence of lateness (13(8)); the financial year end when the year is the charity's financial year (13(7), F5.2 reading B); a reference day before the charity was registered (13(7), F5.2 reading C).

## 2. Fork register (R4 shape)

The record is `Interpretation of Articles 13 and 14` in `g5-interpretation.l4`; it has 14 fields, one per fork, each `TYPICALLY` the reading taken, and every public decision that depends on a fork takes it as the `GIVEN` named `interp` and delegates by `CONSIDER` to one private implementation per reading (named `F5.n A: ...`, `F5.n B: ...`).
`the favoured interpretation of Articles 13 and 14` is the record at the readings taken.
Readings other than the one taken are values named `the interpretation with ...` in `g5-interpretation.l4` (generated by `work/g5/gen_variants.py` from one table, so the other twelve fields cannot drift), and they are what the tests call.
Fork ids F5.1 to F5.5 continue the survey's; F5.6 to F5.14 are new.
Every period in the scope has a fork on its counting convention: P8 "promptly" (F5.1, F5.10), P9 "the year to which the return relates" (F5.2, F5.11, F5.13), P10 the due date (F5.5), the period of registration in 13(1) (F5.6), the period fixed by the court in 14(3) (F5.9), the statement in force (F5.14).
Orderings stated with "before" and "after" (13(3)(b) "prior approval", 13(5)(b) "before it ceased", 13(6)(b) "after registration") are not periods; they are facts a witness can state (a Boolean), and section 8 says why.

### F5.1 "promptly" (13(6)); period P8, a standard of promptness

- **Provision:** 13(6), lead-in. "(6) A registered charity must promptly report to the Commissioner –" [src:383]
- **Readings.**
  A (taken) `an input judgement that the report was made promptly`: the Law states no number, so the encoding states none; whether a report was prompt is the reader's judgement, recorded as a Boolean.
  B `a number of days from the event or proposal` HAS `number of days`: "promptly" is measured from the day the event happened or the proposal was made.
  C `a number of days from the charity becoming aware of the matter` HAS `number of days`: measured from the day the charity became aware.
- **Why A.** "Promptly" is a standard, not a count; B and C put a number into the law that Parliament did not enact (the number is an input in B and C, never a default).
- **Carried by:** field `how promptness is measured` of type `Measure of promptness under Article 13(6)`; private rules `F5.1 A`, `F5.1 B`, `F5.1 C`; public `Art 13(6) the registered charity must promptly report the matter` (the duty) and `Art 13(6) the report was made promptly` (the test).
- **Discriminating case.** Event 1 March 2026, charity aware 20 March 2026, report 25 March 2026, 14 days: late on B, in time on C.
  And a report on 10 March 2026 that the reader judges not prompt: not prompt on A, prompt on B.
- **Tests.** `g5-tests-forks` "F5.1 and F5.10"; `g5-tests-art13-reporting` "Article 13(6): promptly" and "the duty as a regulative rule" (traces: reading B breach on 16 March, fulfilled on 15 March); `g5-tests-red` assertion (1).

### F5.2 "the year to which the return relates" (13(7), 13(9)(a)); period P9, a reporting period; integration point IP33

- **Provision:** 13(7) "(7) A registered charity must send an annual return to the Commissioner, containing information as to any matter falling within paragraph (6) arising during the year to which the return relates, and as to any other matter prescribed by the Minister by Order for this purpose." [src:392], and 13(9)(a) "(a) require a registered charity to include in its annual return details of a prescribed description of any payment made, during the year to which the return relates, by or on behalf of the registered charity to a governor, or to a person having a prescribed connection with a governor;" [src:395]
- **Readings.**
  A (taken) `the calendar year`: 1 January to 31 December of the year containing a reference day.
  B `the charity's own financial year`: the year ending on the charity's year-end day that contains the reference day.
  C `the twelve months from each anniversary of registration`: from an anniversary of registration (that day included) to the day before the next.
- **Why A.** Nothing in Article 13 qualifies "year".
  Schedule 1 paragraph 4(8) says "in each calendar year" when it means one (trap T24), so the unqualified word is not compelled to be a calendar year; A is taken as the ordinary meaning of an unqualified "year" and because G3 takes it for 8(3)(j) (F3.2), and the two groups must take the same reading.
- **Carried by:** field `the meaning of the year of an annual return`, typed with `domain.l4`'s `Meaning of the year of an annual return` (`the calendar year`, `the charity's own financial year`, `the twelve months from each anniversary of registration`); the integrator sets it, and G3's field, from one value (IP33).
  Public rule `Art 13(7) the year to which the return relates` (takes a reference day inside the year); private rules `F5.2 A`, `F5.2 B`, `F5.2 C`.
- **Discriminating case.** A payment to a governor on 10 February 2026, a charity with a 30 June year-end registered on 1 March 2019.
  For the return that covers 1 December 2026: in the return on A (calendar 2026), not in it on B (1 July 2026 to 30 June 2027) or C (1 March 2026 to 28 February 2027).
  For the return that covers 15 March 2026: in it on A and B (1 July 2025 to 30 June 2026), not on C.
- **Tests.** `g5-tests-forks` "F5.2 and F5.11"; `g5-tests-art13-reporting` "the year to which the return relates" and "Article 13(9)"; `g5-tests-red` assertions (3) and (4).

### F5.3 "any Order under paragraph (7), (8) or (9)" (13(10)); trap T18

- **Provision:** 13(10) "(10) The Minister may by Order, after consulting the Commissioner and any body appearing to the Minister to be representative of interested registered charities, provide that any provision of paragraph (6) or (7), or of any Order under paragraph (7), (8) or (9) –" [src:398] and 13(8) "(8) An Order under paragraph (7) may also make provision as to the format and timing of the annual return, the consequences of lateness, and the content of any entries to be made on the register in respect of the annual return." [src:393]
- **Readings.**
  A (taken) `the Order under paragraph (7) as extended by paragraph (8)`: an "Order under paragraph (8)" is the Order under (7) as it may "also" make provision under (8), so a relief Order that names it reaches the provisions made by virtue of (8).
  B `no Order exists under paragraph (8)`: paragraph (8) confers no Order of its own, so a relief Order that names one reaches nothing.
- **Why A.** It gives the words of 13(10) a meaning (on B the reference to (8) is empty); (8) itself says an Order under (7) "may also make provision" for format, timing and lateness.
  The readings agree on a relief Order that names "an Order under paragraph (7)", which reaches the (8) provisions on both, since they are provisions of an Order under (7).
- **Carried by:** field `the meaning of an Order under paragraph (8)`; rules `F5.3 A`, `F5.3 B`, public `Art 13(10) the relief Order names the provision` and `Art 13(10) the effect of the relief Order on the provision`.
- **Discriminating case.** A valid relief Order naming "a provision of an Order under paragraph (8)", asked about the lateness provisions of an Order under (7) made by virtue of (8): disapplied on A, applies in full on B.
- **Tests.** `g5-tests-forks` "F5.3"; `g5-tests-art13-reporting` "Article 13(10)"; `g5-tests-red` assertion (6).

### F5.4 "misconduct in the administration of the charity" (14(1)(a))

- **Provision:** 14(1)(a) "(a) that there is or has been misconduct in the administration of the charity; or" [src:408]
- **Readings.**
  A (taken) `misconduct within Article 2(10) that bears on the administration of the charity`.
  B `any misconduct within Article 2(10)`.
  C `misconduct in the ordinary sense, not the defined term`: ordinary-sense misconduct that concerns the administration.
- **Why A.** "Misconduct" is a defined term (Articles 1, 2(10), 18(4)); the phrase then adds "in the administration of the charity", and on B those words add nothing; on C the defined term is ignored.
- **Carried by:** field `the meaning of misconduct in the administration`; rules `F5.4 A`, `F5.4 B`, `F5.4 C`, public `Art 14(1)(a) there is or has been misconduct in the administration of the charity`.
  The facts are given as they appear to the court; IP12 is the `GIVEN` `the conduct is misconduct within Article 2(10)`.
- **Discriminating cases.** A governor's conviction for a tax offence committed in relation to the charity (2(10)(b)(iii), so misconduct within 2(10)) that has no bearing on the administration: A no, B yes, C no.
  Mismanagement in the administration that breaks no provision (not 2(10) misconduct): A no, B no, C yes.
- **Tests.** `g5-tests-forks` "F5.4"; `g5-tests-art14` "Article 14(1)"; `g5-tests-red` assertions (7) and (8).

### F5.5 is a return sent on the due date timely? (13(8)); period P10, a deadline

- **Provision:** 13(8) "(8) An Order under paragraph (7) may also make provision as to the format and timing of the annual return, the consequences of lateness, and the content of any entries to be made on the register in respect of the annual return." [src:393]
- **Readings.**
  A (taken) `timely if sent on or before the due date`.
  B `late unless sent before the due date`.
- **Why A.** A date fixed as the time for sending a return is ordinarily met by sending it on that date; the Order that fixes the date is not in the sources and may say otherwise.
- **Carried by:** field `whether a return sent on the due date is timely`; rules `F5.5 A` (`WITHIN 0 OF the due date`, inclusive), `F5.5 B` (`WITHIN 0 OF` the day before), public `Art 13(7) the registered charity must send an annual return` and `Art 13(8) the annual return is late`.
  With no due date in the Order the duty has no time and "late" is a named refusal.
- **Discriminating case.** Due 31 March 2027, sent 31 March 2027: timely on A, late on B.
- **Tests.** `g5-tests-forks` "F5.5"; `g5-tests-art13-reporting` "the duty to send the annual return" (traces on 30 March, 31 March, 1 April); `g5-tests-red` assertion (9).

### F5.6 the day deregistration takes effect (13(1)); the period of registration

- **Provision:** 13(1) "(1) Paragraphs (2) to (4) apply while an entity is registered as a charity, and only cease to apply if the entity is deregistered." [src:372] with 17(3) (a deregistration with retrospective effect "takes effect from the past date specified ... for all purposes"). "(3) The termination takes effect from the past date specified under paragraph (2)(c) for all purposes, including the purposes of any enactment relating to taxation, but subject to paragraph (4)." [src:451]
- **Readings.**
  A (taken) `outside: registered up to the day before deregistration takes effect`.
  B `inside: registered up to and including the day deregistration takes effect`.
- **Why A.** 17(3) says the termination takes effect from that date, so from that date the entity is not registered.
  The first day of registration is the registration date on both readings (8(3)(g) calls it "the date on which the charity was registered").
  A retrospective deregistration therefore ends the regime from the past date, not from the notice (trap T15).
- **Carried by:** field `whether the day deregistration takes effect is inside the registration`; rules `F5.6 A`, `F5.6 B`; public `Art 13(1) paragraphs (2) to (4) apply on the day`.
  The field `date deregistered` of `Registered charity` (set by G6) is the effective date.
- **Discriminating case.** Deregistered with effect from 30 June 2022, the question asked about 30 June 2022: (2) to (4) do not apply on A, apply on B.
- **Tests.** `g5-tests-art13-effects` "Article 13(1)"; `g5-tests-forks` "F5.6"; `g5-tests-red` assertion (10).

### F5.7 "a purpose that is not charitable" (13(2))

- **Provision:** 13(2) "(2) Any provision of the entity’s constitution or constitutional Law is of no effect to the extent that it purports to permit an amendment of the purposes of the entity to include a purpose that is not charitable." [src:373] read with 5(1)(a) (all purposes are charitable purposes "or" purely ancillary or incidental to one) and 6(5).
- **Readings.**
  A (taken) `any purpose that is not a charitable purpose under Article 6, a purely ancillary purpose included`.
  B `a purpose that is neither a charitable purpose nor purely ancillary or incidental to one`.
- **Why A.** It is the literal reading: Article 1 defines "charitable purpose" by Article 6, and Articles 5(1)(a) and 6(5) treat a charitable purpose and an ancillary purpose as two classes.
  B is the purposive reading (what the charity test would reject).
  The consequence of A is that a registered charity's constitution cannot let it add even a purely ancillary purpose; whether that is intended is an open question (section 7).
- **Carried by:** field `the meaning of a purpose that is not charitable`; rules `F5.7 A`, `F5.7 B`, `Art 13(2) the purpose is not charitable`.
  Whether a `Purpose` is "charitable" is read from the record: not political (6(5)) and either under a head of 6(1) or the advancement of a philosophical belief (6(2)(f)).
- **Discriminating case.** A provision that lets an amendment add a purpose "to run a cafe whose profits fund the concerts" (purely ancillary): of no effect on A, has effect on B.
- **Tests.** `g5-tests-art13-effects` "Article 13(2)"; `g5-tests-forks` "F5.7"; `g5-tests-red` assertion (11).

### F5.8 paragraphs (a) and (b) of 13(5), joined by "or"

- **Provision:** 13(5) "(5) A registered charity must, while it is entered in the restricted section of the register, ensure –" [src:380] "(a) that it meets the condition, prescribed under Article 9(2), as to which the Commissioner was satisfied under Article 9(6)(b); or" [src:381] "(b) if, before it ceased to meet that condition, the Commissioner gave prior permission for it to remain entered in the restricted section on the basis of a different condition prescribed under that Article, that it meets that condition as specified in that permission." [src:382]
- **Readings.**
  A (taken) `either the original condition, or after a prior permission and a cessation the different condition`: (a) alone suffices; (b) is open only to a charity that has ceased to meet the original condition and whose permission was given before it ceased.
  B `once permission is given the different condition replaces the original condition`: from a prior permission the charity must meet the different condition, whether or not it has ceased to meet the original.
- **Why A.** The word is "or"; and (b)'s opening, "if, before it ceased to meet that condition, the Commissioner gave prior permission", presupposes that the charity has ceased to.
  B reads "to remain entered ... on the basis of a different condition" as a change of basis.
- **Carried by:** field `how the two paragraphs of Article 13(5) combine`; rules `F5.8 A`, `F5.8 B`, public `Art 13(5) the registered charity in the restricted section meets what paragraph (5) requires`.
- **Discriminating cases.** A prior permission exists, the charity still meets the original condition and fails the different one: complies on A, not on B.
  A charity that never met the original condition, with a prior permission, meeting the different one: not on A (it has not "ceased"), complies on B.
- **Tests.** `g5-tests-art13-effects` "Article 13(5)"; `g5-tests-forks` "F5.8"; `g5-tests-red` assertion (12).

### F5.9 the first day of a period fixed by the court (14(3)(a), (b), (g)); a period fixed by an order

- **Provision:** 14(3)(a) "(whether for a specified or indefinite period)", (b), and (g) "from such time, and for such periods, as the court may specify". "(a) prohibiting (whether for a specified or indefinite period) the charity or a governor from –" [src:412]
- **Readings.**
  A (taken) `the first day named is the first day of the period`.
  B `the period starts on the day after the first day named`.
- **Why A.** (g) says the order operates "from such time" as the court specifies: from the time it names; the Law adds no counting rule.
- **Carried by:** field `whether the first day counts in a period fixed by the court`; rules `Art 14(3) the first day of the period` and `Art 14(3) the order is in operation on the day`.
  The order names a first day and a number of days (`a specified period`), or a first day only (`an indefinite period`).
- **Discriminating case.** A hold for 30 days from 1 June 2026: in operation on 1 June and not on 1 July on A; not on 1 June and on 1 July on B.
- **Tests.** `g5-tests-art14` "Article 14(3)"; `g5-tests-forks` "F5.9"; `g5-tests-red` assertion (13).

### F5.10 counting the days when "promptly" is a number of days (13(6), readings B and C of F5.1)

- **Provision:** 13(6). "(6) A registered charity must promptly report to the Commissioner –" [src:383]
- **Readings.**
  A (taken) `the day of the event is not counted: the last prompt day is the event day plus the number of days`.
  B `the day of the event is the first day: the last prompt day is one day earlier`.
- **Why A.** The usual construction of "within N days after" an event excludes the day of the event.
  The Interpretation (Jersey) Law 1954 is not among the sources, so this is stated as an assumption, not a ruling.
- **Carried by:** field `whether the day of the event counts in a number of days`; rules `F5.10 A`, `F5.10 B`, `Art 13(6) the last prompt day`.
- **Discriminating case.** Event on 1 March 2026, 14 days: the last prompt day is 15 March on A and 14 March on B; a report on 15 March is in time on A and late on B.
- **Tests.** `g5-tests-art13-reporting` "promptly ... counting the days"; `g5-tests-forks` "F5.1 and F5.10"; `g5-tests-red` assertion (2).

### F5.11 the anniversary of a registration made on 29 February (13(7), reading C of F5.2)

- **Provision:** 13(7). "(7) A registered charity must send an annual return to the Commissioner, containing information as to any matter falling within paragraph (6) arising during the year to which the return relates, and as to any other matter prescribed by the Minister by Order for this purpose." [src:392]
- **Readings.**
  A (taken) `the last day of February (the day is clamped, as daydate add years does)`.
  B `the first day of March (the day rolls forward)`.
- **Why A.** `add years` in `daydate` clamps, as a spreadsheet's date-add does; it is the library's own convention for an anniversary.
- **Carried by:** field `the anniversary of a registration made on 29 February`; rules `F5.11 A`, `F5.11 B`, `Art 13(7) the anniversary of the registration`.
- **Discriminating case.** A charity registered on 29 February 2020, reference day 28 February 2025: the year that contains it began on 28 February 2025 on A; it ended on 28 February 2025 (and began on 29 February 2024) on B.
- **Tests.** `g5-tests-forks` "F5.2 and F5.11"; `g5-tests-art13-reporting`; `g5-tests-red` assertion (5).

### F5.12 the three purposes of an order under 14(2)

- **Provision:** 14(2) "(2) The court may make any order that the court sees fit to remedy the misconduct, protect the property and secure its proper application." [src:410] with 14(1)(a) and (b) (alternative grounds).
- **Readings.**
  A (taken) `at least one of the three purposes`.
  B `all three purposes`.
- **Why A.** 14(1)(b) lets the court act with no misconduct at all, and then an order "to remedy the misconduct" is impossible; so the "and" cannot require every purpose.
  B is kept callable because the words, read as a conjunction, would require it.
- **Carried by:** field `the purposes an order under Article 14(2) must serve`; rules `F5.12 A`, `F5.12 B`, `Art 14(2) the order is one the court sees fit`, `Art 14(2) the court may make any order it sees fit`.
- **Discriminating case.** The powers are exercisable on ground (b) alone and the order only protects the property: available on A, not on B.
- **Tests.** `g5-tests-art14` "Article 14(2)"; `g5-tests-forks` "F5.12"; `g5-tests-red` assertion (14).

### F5.13 when a matter "arises" for the annual return (13(7))

- **Provision:** 13(7) "any matter falling within paragraph (6) arising during the year". "(7) A registered charity must send an annual return to the Commissioner, containing information as to any matter falling within paragraph (6) arising during the year to which the return relates, and as to any other matter prescribed by the Minister by Order for this purpose." [src:392]
- **Readings.**
  A (taken) `the date of the event or proposal`.
  B `the date the charity became aware of the matter`.
- **Why A.** "Arising" is about the matter, not the charity's knowledge; 13(6)(b) uses "coming to light" when it means knowledge, so the drafter distinguishes the two.
  Convention for limb (b), where the matter was always there: the date to supply as the date of the event is the day it came to light (assumed, not ruled).
- **Carried by:** field `the date on which a matter arises`; rules `Art 13(7) the date on which the matter arises`, `Art 13(7) the matter arose during the year to which the return relates`.
- **Discriminating case.** An event on 30 December 2026 of which the charity learned on 5 January 2027, the 2026 calendar-year return: arises in 2026 on A, in 2027 on B.
- **Tests.** `g5-tests-art13-reporting` "what the annual return must contain"; `g5-tests-forks` "F5.13"; `g5-tests-red` assertion (15).

### F5.14 which statement a payment is judged by (13(11)(a))

- **Provision:** 13(11)(a) and (b). "(a) must not make any payment that is inconsistent with a statement provided under paragraph (9)(b);" [src:402] "(b) may apply to the Commissioner, with reasons, for permission to amend that statement." [src:403]
- **Readings.**
  A (taken) `the statement in force on the day of the payment`: the latest statement provided on or before the day of the payment (a statement provided on that day counts).
  B `any statement provided on or before the day of the payment`.
- **Why A.** 13(9)(b) speaks of a statement of "current intentions" and 13(11)(b) of permission to amend "that statement", which read as one statement that changes over time; B reads "a statement" literally.
- **Carried by:** field `the statement a payment must be consistent with`; rules `F5.14 A`, `F5.14 B`, `Art 13(11)(a) the payment is inconsistent with the statement`, `Art 13(11)(a) the statements provided on or before the day of the payment`.
- **Discriminating case.** A payment of 10 May 2023 that contradicts the statement of 10 January 2022 but fits the amended statement of 1 February 2023: consistent on A, inconsistent on B.
- **Tests.** `g5-tests-art13-effects` "Article 13(11)"; `g5-tests-forks` "F5.14"; `g5-tests-red` assertion (16).

## 3. Answer table: headline scenarios

Every answer below is asserted in the tests, at the reading taken unless the row says otherwise.

| scenario | answer | Article |
| --- | --- | --- |
| A charity registered 1 March 2019, never deregistered, asked about 1 January 2030 | paragraphs (2) to (4) apply | 13(1) |
| Deregistered with effect from 30 June 2022 (the notice may be later): 29 June / 30 June / 1 August 2022 | apply / do not apply / do not apply | 13(1), 17(3); fork F5.6 |
| A clause that would let the purposes be amended to include a political purpose | of no effect | 13(2), 6(5) |
| A clause that would let only an educational purpose be added | has effect; but read subject to evidence and prior approval | 13(2), 13(3) |
| The same clause, evidence given, no prior approval | not satisfied | 13(3)(a), (b) |
| A clause letting a purely ancillary purpose be added | of no effect (A); has effect (B) | 13(2); fork F5.7 |
| A court-approved fideicommis whose court order under the Loi of 1862 is inconsistent with (2) | paragraphs (2) and (3) yield | 13(13) |
| A restricted-section charity that ceased to meet its condition, no prior permission | does not comply | 13(5) |
| ... with a prior permission and meeting the different condition | complies | 13(5)(b) |
| Event 1 March 2026, aware 20 March, reported 25 March, 14 days | late if counted from the event; in time if from awareness | 13(6); fork F5.1 |
| The same, reported on 15 March / 16 March (event day not counted) | in time / late | 13(6); fork F5.10 |
| A governor's reportable matter, the charity aware | to be reported; if the charity is not aware, or the governor has none, not | 13(6)(e) |
| A proposal to change how the condition is met, charity in the general section | not within (g) | 13(6)(g) |
| Return year containing 1 December 2026: calendar / financial year ending 30 June / from the anniversary of registration | 2026-01-01 to 2026-12-31 / 2026-07-01 to 2027-06-30 / 2026-03-01 to 2027-02-28 | 13(7); fork F5.2 |
| A payment to a governor of 10 February 2026, an Order under 13(9)(a) applying: in the return for that calendar year / for the 2026-27 financial year | in it / not in it | 13(9)(a) |
| An annual return due 31 March 2027, sent 31 March / 1 April | timely / late (A); late / late (B) | 13(7), 13(8); fork F5.5 |
| No Order fixes a due date | "late" is a refusal; the duty has no time | 13(8) |
| A relief Order made without consulting the Commissioner | no effect | 13(10) |
| A payment inconsistent with the statement of intentions | breach of the prohibition; no penalty in the Law | 13(11)(a) |
| An application to the court by the Commissioner or the Attorney General / by the registered charity / by anyone else | opens the powers / does not / does not | 14(1) |
| Only protection of the property is needed | ground (b) suffices | 14(1)(b) |
| A conviction with no bearing on the administration | not a ground (A); a ground (B) | 14(1)(a); fork F5.4 |
| An order suspending the charity itself | not a kind 14(3)(d) lists | 14(3)(d) |
| A hold on property directed at the bank that holds the charity's funds | a kind 14(3)(e) lists | 14(3)(e) |
| An order to remedy, directed at a governor against whom nothing appears | not available | 14(3)(h) |
| A hold for 30 days from 1 June 2026: 30 June / 1 July | in operation / not (A) | 14(3); fork F5.9 |
| An application to amend or revoke: Commissioner, Attorney General, charity, person directed / anyone else | the court may / the court may not | 14(4) |
| The court's Article 14 powers not exercisable, another power exists | the court may act | 14(5)(a) |

## 4. Nouns requests for the INTEGRATOR

1. **Subjects of the Commissioner's decisions (IP27).** `Subject of a decision of the Commissioner` has no subject for the prior permission of 13(5)(b) or the permission to amend the statement of 13(11)(b); `Art 13 the decision of the Commissioner` maps both to `any other matter`.
   Please add `whether to give prior permission to remain entered in the restricted section on a different condition, Article 13(5)(b)` and `whether to permit an amendment of the statement of intentions as to payments, Article 13(11)(b)`, and G8 can then keep them out of Article 33's closed list (trap T12).
2. **A financial year end on the register.** Fork F5.2 reading B needs the charity's financial year end; `Registered charity` has no such field, so `Art 13(7) the year to which the return relates` takes `the financial year end` : `MAYBE` `Day on which a financial year ends` as a separate `GIVEN`.
   G3's 8(3)(j) needs the same.
   Please move `Day on which a financial year ends` and `Year to which an annual return relates` (both in `g5-nouns.l4`) into `domain.l4`, and add the year end to `Registered charity`, so that G3 and G5 share one year.
3. **A per-purpose charitable test.** 13(2) re-derives "charitable purpose" from the `Purpose` record (`Art 13(2) the purpose is a charitable purpose`: not political, and under a head or the advancement of a philosophical belief).
   If G2 exports a per-purpose rule, wire the two and assert they agree.
4. **Types local to G5 that another group may want:** `Application to the court under Article 14` (G6's 17(9) application is by the Attorney General or a governor) and `Person at whom an order is directed`.
5. **`Legal actor` constructors used:** `a registered charity`, `the Commissioner`, `the Minister`, `the States`, `the court`, `the Attorney General`, `any person`; no new constructor is needed.
   (The constructors of `Application to the court under Article 14` are named `an application by ...` so that they do not collide with those of `Legal actor`.)

## 5. Standard inputs consumed, and the functions exported

### 5.1 Standard `GIVEN`s consumed (exact names, as in PLAN section (c))

| name | type | id | read in |
| --- | --- | --- | --- |
| `the registered charity` | `Registered charity` | IP7 (carries the entity of IP5) | everywhere; fields `date registered`, `date deregistered`, `registered public benefit statement`, and the entity's `standing on the register`, `kinds of entity`, `governors` (with their `reportable matters`, IP21) |
| `the entity is a registered charity` | BOOLEAN | IP6 | every duty and permission that binds "a registered charity" |
| `the conduct is misconduct within Article 2(10)` | BOOLEAN | IP12 | `Art 14(1)(a) ...`, the 14(1) gate and the rules that call it |
| `the requirement of Article 11(4)(c) is met`, `the requirement of Article 11(4)(d) is met` | BOOLEAN | IP15, IP16 | 13(6)(d) |
| `the name is undesirable under Article 12(1)` | BOOLEAN | IP18 | 13(6)(b) |
| `someone is acting as the Commissioner` | BOOLEAN | IP28 | every rule whose PARTY is `the Commissioner` |
| `an Order under Article 13(9) applies to the registered charity` | BOOLEAN | IP29 | 13(9)(a), 13(9)(b), 13(11)(a) (produced here by `Art 13(9) an Order under Article 13(9) applies to the registered charity`) |
| `the day` | DATE | IP1 | 13(1) and the rules that call it |

`the entity` (IP5) is not a separate `GIVEN`: the entity travels as the field `entity` of `the registered charity`.
IP3 (the office of the Minister) is not read: every rule of the Minister is typed by the role `the Minister`.

### 5.2 Produced for other groups

| id | what | export |
| --- | --- | --- |
| IP27 | the Commissioner's decisions under Article 13 | `Art 13 the decision of the Commissioner` |
| IP29 | an Order under 13(9) applies to the charity | `Art 13(9) an Order under Article 13(9) applies to the registered charity` (takes `interp`, `order` : `MAYBE` `Order under Article 13(9)`, `reliefs` : `LIST OF` `Order under Article 13(10)`) |
| IP31 | the kinds of order the court may make | `Art 14(3) the court may make the order`; type `Order of the court over a charity` (domain) |
| IP33 | the meaning of "year" | field `the meaning of the year of an annual return` of `Interpretation of Articles 13 and 14` |

### 5.3 Every `@export`

| module | function | takes (in order) | gives |
| --- | --- | --- | --- |
| g5-art13-effects | `Art 13(1) paragraphs (2) to (4) apply on the day` | interp, the registered charity, the day | BOOLEAN |
| g5-art13-effects | `Art 13(2) the provision of the constitution is of no effect` | interp, the registered charity, the day, provision | BOOLEAN |
| g5-art13-effects | `Art 13(3) the amendment of purposes is subject to evidence and approval` | interp, the registered charity, the day, provision, evidence has been provided to the satisfaction of the Commissioner, the Commissioner's approval was obtained before the amendment | BOOLEAN |
| g5-art13-effects | `Art 13(3)(b) the Commissioner may approve the proposed amendment of purposes` | someone is acting as the Commissioner, the entity has proposed an amendment of its purposes and asked for approval | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(4) the registered charity must provide public benefit in accordance with its statement` | interp, the registered charity, the day, public benefit is provided in accordance with the registered public benefit statement | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(4)(b) the registered charity that requests approval of an amendment of its statement must provide evidence` | interp, the registered charity, the day, the entity requests the Commissioner's approval of a proposed amendment of its registered public benefit statement, the evidence is to the satisfaction of the Commissioner | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(4)(b) the Commissioner may approve the proposed amendment of the statement` | someone is acting as the Commissioner, the entity has requested approval of a proposed amendment of its registered public benefit statement | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(5) the registered charity in the restricted section meets what paragraph (5) requires` | interp, facts | BOOLEAN |
| g5-art13-effects | `Art 13(5) the registered charity in the restricted section must ensure it meets its condition` | interp, the entity is a registered charity, the registered charity, facts | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(5)(b) the Commissioner may give prior permission to remain in the restricted section` | someone is acting as the Commissioner, the charity is entered in the restricted section | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(11)(a) the registered charity must not make a payment inconsistent with its statement` | interp, the entity is a registered charity, an Order under Article 13(9) applies to the registered charity | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(11)(b) the registered charity may apply for permission to amend the statement` | the entity is a registered charity, a statement of intentions has been provided under Article 13(9)(b) | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(11)(b) the Commissioner may give permission to amend the statement` | someone is acting as the Commissioner, the charity has applied for permission to amend the statement, with reasons | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-effects | `Art 13(13) paragraphs (2) and (3) yield to an order under the Loi of 1862` | the registered charity, provision | BOOLEAN |
| g5-art13-effects | `Art 13 the decision of the Commissioner` | about, the Commissioner does what was sought | `Decision of the Commissioner` |
| g5-art13-reporting | `Art 13(6) the matter falls within the paragraph` | the registered charity, the requirement of Article 11(4)(c) is met, the requirement of Article 11(4)(d) is met, the name is undesirable under Article 12(1), matter | BOOLEAN |
| g5-art13-reporting | `Art 13(6) the report was made promptly` | interp, timing, report | BOOLEAN |
| g5-art13-reporting | `Art 13(6) the registered charity must promptly report the matter` | interp, the entity is a registered charity, the registered charity, the requirement of Article 11(4)(c) is met, the requirement of Article 11(4)(d) is met, the name is undesirable under Article 12(1), matter, timing, report | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(6)(h) the Minister may by Order prescribe a further matter to be reported` |  | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(7) the year to which the return relates` | interp, the registered charity, the financial year end, a day in the year | `Year to which an annual return relates` |
| g5-art13-reporting | `Art 13(7) the annual return contains the information paragraph (7) requires` | interp, year, matters, the return gives information about every matter prescribed by Order under Article 13(7) | BOOLEAN |
| g5-art13-reporting | `Art 13(7) the registered charity must send an annual return` | interp, the entity is a registered charity, order | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(8) the annual return is late` | interp, order, the day the return was sent | BOOLEAN |
| g5-art13-reporting | `Art 13(8) the consequence of lateness` | order | STRING |
| g5-art13-reporting | `Art 13(7) the Minister may by Order prescribe a further matter for the annual return` |  | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(8) the Minister may by Order provide for the format and timing of the annual return` | subject, the provision is made in an Order under paragraph (7) | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(9)(a) the Minister may by Order require payment details in the annual return` |  | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(9)(b) the Minister may by Order require a statement of intentions` |  | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(9)(c) the Minister may by Order provide for entry on the register` |  | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(9)(a) the payment falls to be included in the annual return` | an Order under Article 13(9) applies to the registered charity, order, year, payment | BOOLEAN |
| g5-art13-reporting | `Art 13(9)(a) the annual return gives the details of the payments the Order requires` | an Order under Article 13(9) applies to the registered charity, order, year, payments | BOOLEAN |
| g5-art13-reporting | `Art 13(9)(b) the registered charity must provide a statement of its current intentions` | the entity is a registered charity, an Order under Article 13(9) applies to the registered charity, order | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(10) the Minister may by Order relieve small charities` | order | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(10) the effect of the relief Order on the provision` | interp, order, target | `Effect of an Order under Article 13(10) on a provision` |
| g5-art13-reporting | `Art 13(9) an Order under Article 13(9) applies to the registered charity` | interp, order, reliefs | BOOLEAN |
| g5-art13-reporting | `Art 13(12) the States may require a charity to avoid or report and remedy a later ground for refusal` | the States make Regulations under Article 11(7) | DEONTIC `Legal actor` `Act under Article 13` |
| g5-art13-reporting | `Art 13(12) the situation is one the Regulations may require the charity or its governors to avoid or to report and remedy` | the situation arose at a time after registration, there would be grounds under the Regulations to refuse an application made at that time | BOOLEAN |
| g5-art14-court-powers | `Art 14(1) the powers of the court are exercisable on the application` | interp, the entity is a registered charity, application, the conduct is misconduct within Article 2(10), appears | BOOLEAN |
| g5-art14-court-powers | `Art 14(1) the court may exercise the powers on the application` | interp, the entity is a registered charity, someone is acting as the Commissioner, application, the conduct is misconduct within Article 2(10), appears | DEONTIC `Legal actor` `Act under Article 14` |
| g5-art14-court-powers | `Art 14(2) the court may make any order it sees fit` | interp, the entity is a registered charity, application, the conduct is misconduct within Article 2(10), appears, sees | DEONTIC `Legal actor` `Act under Article 14` |
| g5-art14-court-powers | `Art 14(3) the order is of a kind the paragraph lists` | order | BOOLEAN |
| g5-art14-court-powers | `Art 14(3) the court may make the order` | interp, the entity is a registered charity, application, the conduct is misconduct within Article 2(10), appears, order | DEONTIC `Legal actor` `Act under Article 14` |
| g5-art14-court-powers | `Art 14(3) the order is in operation on the day` | interp, period, the day | BOOLEAN |
| g5-art14-court-powers | `Art 14(4) the court may amend or revoke an order` | the entity is a registered charity, someone is acting as the Commissioner, application, the order was made under Article 14 | DEONTIC `Legal actor` `Act under Article 14` |
| g5-art14-court-powers | `Art 14(5) the powers apply in addition to other powers and despite the constitution` | the powers of the court under Article 14 are exercisable, the court has the power under another enactment or under customary law, a provision of the constitution of the charity forbids the order | BOOLEAN |
| g5-art14-court-powers | `Art 14(6) the Commissioner's own power is unaffected by the powers of the court` | the Commissioner may take action under this Law in respect of the misconduct, the court has acted under Article 14 | BOOLEAN |

Every `@export` has a one-sentence description and an `@desc` on each `GIVEN`; a function that depends on a fork takes `interp`.

## 6. Contradictions and cross-reference faults in the source (a separate pass, after encoding)

Looked for deliberately, in this order: every cross-reference of Articles 13 and 14 (and every reference to them from elsewhere) against its target; every defined term against its use; the two paragraphs of each "or"; Article 17(3) and 33 against 13.

1. **13(10) names an Order that does not exist.** "Any Order under paragraph (7), (8) or (9)": paragraph (8) says an Order under (7) "may also make provision"; it creates no Order (trap T18).
   Discriminating case and both readings: fork F5.3.
2. **13(5)(b) presupposes a power that no provision confers.** The Commissioner's "prior permission ... to remain entered in the restricted section on the basis of a different condition" is mentioned only here; Article 9 gives no such permission, and Article 33(2) lists no appeal against its refusal (trap T12).
   Encoded as the Commissioner's permission (MAY), marked "presupposed, conferred by no provision"; the case where it matters is the "or" of F5.8.
3. **13(2) against 5(1)(a)(ii) and 6(5).** 13(2) strikes a provision that lets the purposes include one "that is not charitable"; Article 5(1)(a)(ii) treats a purely ancillary purpose as acceptable beside the charitable ones, and 6(5) calls a political purpose "neither a charitable purpose nor a purpose ancillary or incidental".
   So "not charitable" in 13(2) either catches ancillary purposes or does not; fork F5.7.
4. **14(2) "and" against 14(1)(a) or (b).** The order is one the court sees fit "to remedy the misconduct, protect the property and secure its proper application"; but 14(1)(b) lets the court act with no misconduct, where "to remedy the misconduct" is impossible.
   Fork F5.12.
5. **13(11)(a) "a statement" against 13(11)(b) "that statement" and 13(9)(b) "current intentions".** Fork F5.14.
6. **13(1) with 17(3) validates amendments made in the interval of a retrospective deregistration.** If the Commissioner deregisters with effect from a past date "for all purposes" (17(3)), 13(2) is taken never to have applied from that date, so an amendment adding a political purpose made after that date and before the notice is not struck by 13(2).
   The Law does not say that is intended; 17(4) protects only against an offence.
   Tested at F5.6.
7. **Drafting slip in 14(3)(b):** "appointing a person (whether a specified or indefinite period)"; 14(3)(a) has "whether for a specified or indefinite period".
   No effect on the encoding.
8. **14(1) says "the powers set out in paragraph (2)"; (2) is one general power and the listed orders are in (3).**
   17(9) says "the powers set out in Article 14".
   No effect on the encoding.
9. **11(2)(e)(ii) against 13(9)(b) (trap T28; G4's rule).** An applicant must give a draft of the statement "if an Order under Article 13(9)(b) applies to the registered charity"; an applicant is not yet a registered charity, and 13(9)(b) requires a registered charity to provide the statement.
   G5 does not decide it; `Art 13(9) an Order under Article 13(9) applies to the registered charity` is the shared fact.
10. **The word "year" (trap T24).** 13(7) and 13(9)(a) say "the year to which the return relates"; 8(3)(j) says "the most recent year"; Schedule 1 paragraph 4(8) and Schedule 2 paragraph 3(3) say "calendar year".
    Fork F5.2.
11. **13(4)(b) and 33(2)(e) describe a regime the Law does not state.** 13(4)(b) says what the entity does "if it requests the Commissioner's approval of a proposed amendment" of the registered public benefit statement, and 33(2)(e) gives an appeal against a refusal; nothing says the entity may not amend the statement without approval, or what approval does.
    (A gap, not a contradiction; section 8.)
12. **A tension, not a contradiction:** 14(3)(a)(i) lets the court forbid a registered charity to hold itself out as a charity, while an Order under Article 25 may require registered charities to say they are one; the Law does not say which prevails.
13. **No fault found** in the references that Articles 13 and 14 make: 13(5) to 9(2) and 9(6)(b); 13(6)(d) to 11(4)(c) and (d); 13(6)(e) to 19(2); 13(11)(a) to 13(9)(b); 13(12) to 11(7); 13(13) to the Loi of 1862; 14(1)(b) to the defined terms "registered charitable purposes" and "registered public benefit statement".
    Nor in the references to them from elsewhere, each checked against `grep -n 'Article 1[34]'` over the Law's text: Article 1's definition of "annual return" (to 13(7)); 8(3)(m) (to 13(9)(c)); 8(3)(j) (to the annual return, through that defined term, and not by citing Article 13); 11(2)(e)(ii) (to 13(9)(b); but see item 9); 12(6) (to 13(6)(b)); 33(2)(d) (to 13(3)) and 33(2)(e) (to 13(4)(b)); and 17(9) (to Article 14).
    13(6)(b) does not cite Article 12: it speaks of the Commissioner "refusing to accept the name of the charity", and the encoding reads that through IP18 (`the name is undesirable under Article 12(1)`), which is G4's.
    The Table of Renumbered Provisions renumbers only Articles 41 to 44, and affects no cross-reference of these Articles.

## 7. Open questions for a domain expert

1. Does 13(2) strike a provision that would let a registered charity add a purely ancillary purpose (F5.7)?
2. Is a return sent on the day an Order fixes as its due date timely (F5.5), and what is "the year" for a charity with a financial year that is not the calendar year (F5.2)?
3. Which permission does 13(5)(b) refer to, and who may give it?
4. Does "promptly" in 13(6) have an accepted number of days in the Commissioner's guidance (F5.1)?
5. Is an order of the court under 14(3)(a)(i) forbidding a registered charity to call itself a charity compatible with an Order under Article 25?
6. Is "misconduct in the administration" (14(1)(a)) limited to conduct that bears on the administration (F5.4)?
7. If a deregistration is retrospective, is an amendment made in the interval affected by 13(2)?
8. Who is "a person to whom the order was directed" in 14(4) where an order is directed at "the charity or a governor" jointly?

## 8. What the sources do not answer

1. **Every Order and Regulations under Article 13** (13(6)(h), 13(7), 13(8), 13(9), 13(10), 13(12) via 11(7)): none is among the sources.
   Inputs: the matters prescribed, the due date, the consequences of lateness, the register entries, the payments and the statement, the relief.
2. **The due date and the consequence of a late annual return.** "Late" and its consequence are named refusals when no Order is given.
3. **How many days "promptly" is.** The numbers in readings B and C of F5.1 are inputs.
4. **What approval or permission does.** 13(3)(b) and 13(4)(b) require the Commissioner's approval but say nothing of its criteria, its time, or the effect of approval or refusal on an amendment; 13(5)(b) and 13(11)(b) likewise.
   The Commissioner's power to approve or permit is encoded as implied.
5. **Whether an amendment made against 13(2) or 13(3) is void** (the text says the provision is "of no effect" and "to be read as being subject to"), and whether the entity may amend its registered public benefit statement without approval (13(4)(b)).
6. **Same-day ordering.** "Prior approval" (13(3)(b)), "before it ceased" (13(5)(b)), "after registration or after permission for a change of name" (13(6)(b)), "a statement provided under (9)(b)" for a payment (13(11)(a)) turn on which of two events came first; the Law has no time of day.
   The first three are Boolean facts a witness can state, supplied by the caller (no date arithmetic is invented).
   In F5.14 a statement provided on the day of the payment counts.
7. **Whether a report made after the change itself still reports a proposal** (13(6)(c), (d)).
8. **What is a "payment ... inconsistent with" a statement** (13(11)(a)), **"necessary or desirable"** (14(1)(b)), **"sees fit"** (14(2)), **"appears to the court ... to have engaged in any misconduct"** (14(3)(h)), **"to the satisfaction of the Commissioner"** (13(3)(a), 13(4)(b)), **"likely"** (13(6)(f)): the judgement of the person named, an input.
9. **Which person a given order is "directed at"** when an order names several; the encoding takes one capacity per order (a caller with two capacities asks twice).
10. **The text of the Loi of 1862 and of any order made under it** (13(13)): the fact of an inconsistent order is an input.
11. **The text before 1 January 2019, and after 2 October 2026.** Articles 13 and 14 carry no endnote marker in the sources; the only vintage in the sources is that of 2 October 2026.
    Which office "the Minister" names in each vintage is G1's (IP3); the rules here are typed by the role.
12. **The Interpretation (Jersey) Law 1954**, which would settle how "within N days" and "the year" are counted; the conventions are forks.
13. **Who prosecutes**, and any consequence of breaching 13(4), (5), (6), (7) or (11)(a) other than that a contravention of a provision of the Law is misconduct (2(10)(a)(i); IP13).
    Article 13 creates no offence and states no penalty: `Art 13(11)(a) the penalty for a payment inconsistent with the statement` is `Penalty provided` with no imprisonment and no fine.

## 9. Notes for the INTEGRATOR

1. **Wiring is by name.** The `GIVEN` names of section 5.1 are exactly the standard names of PLAN section (c); the names of the exports of section 5.3 are exactly those of PLAN (b) where PLAN names one.
2. **Forks to set together:** F5.2 here and F3.2 in G3 (one `Meaning of the year of an annual return`, IP33).
   Set the 14 fields of `Interpretation of Articles 13 and 14` from `the favoured interpretation of Articles 13 and 14`, or from one of the `the interpretation with ...` values.
3. **Commencement is the integrator's wrapper.** Articles 13 and 14 are in Part 4, in force 1 May 2018 (stage 2); no rule here gates on a date of commencement.
4. **Breach is a fact the integrator maps (IP13).** The prohibition of 13(11)(a) yields BREACH in a `#TRACE`; "misconduct" asks only for a Boolean.
   The same is true of the standing duties of 13(4) and 13(5) (their `PROVIDED` guard is the judgement that the duty is performed).
5. **The clock of a trace.** Rules that carry a date (13(6) readings B and C, 13(7)) use `WITHIN 0 OF` a `DATE`, so their traces must be stamped `AT (DATE_SERIAL (YMD ...))`.
   The other rules have no time and their traces use any numeric clock.
6. **Deontic acts.** `DEONTIC` `Legal actor` `Act under Article 13` and `Act under Article 14` are the two types; the PARTY is always a constructor of `Legal actor`.
   The applicant of Article 14 is the PARTY of an `apply to the court` act, followed by the court's own permission (`HENCE`).
7. **The 13(2)/(3) provision record carries a Boolean `forms part of the entity's constitution or constitutional Law`.** G1's rule `Art 2(5)` answers `NOTHING` for seven of the twelve kinds of entity (trap T6); a caller whose entity has no constitutional Law can supply only provisions of the constitution.
8. **IP27 and IP29.** G5 produces IP29 (and every consumer of it, G3 and G4, reads it by the standard name) and the Article 13 subjects of IP27; G3, G4, G6 and G8 produce the subjects of their own Articles; G8 and G9 consume the record.
9. **Counts to expect from this group:** 58 coverage rows, none `deferred`; 14 fork points; 46 exports (section 5.3 shows the live list).

## 10. What the check printed, and the cleanroom

`work/g5/check.sh` printed:

```
l4 binary: /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4 (sha256 matches the fleet's binary)

module                              errors satisfied  failed  refused  warnings  exp.fail
g5-art13-effects.l4                      0         0       0        0         0         0
g5-art13-reporting.l4                    0         0       0        0         0         0
g5-art14-court-powers.l4                 0         0       0        0         0         0
g5-interpretation.l4                     0         0       0        0         0         0
g5-nouns.l4                              0         0       0        0         0         0
g5-tests-art13-effects.l4                0        92       0        0         0         0
g5-tests-art13-reporting.l4              0       127       0        0         0         0
g5-tests-art14.l4                        0        82       0        0         0         0
g5-tests-fixtures.l4                     0         0       0        0         0         0
g5-tests-forks.l4                        0        41       0        0         0         0
g5-tests-properties.l4                   0         4       0        0         0         0
g5-tests-red.l4                         16         0      16        0         0        16
TOTAL (12 modules)                      16       346      16        0         0        16
(a failed assertion is also an error; any other error, any refusal or warning, and any failed count other than the module's expected_failed, make the run red)

shape: every g5- module has a plain name and imports only prelude, daydate, domain and g5- modules
srcrefs check: 159 src: lines, 76 runs, 147 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g5-tests-art13-effects.l4                         29        29         0     29     0          0
g5-tests-art13-reporting.l4                       43        43         0     43     0          0
g5-tests-art14.l4                                 25        25         0     25     0          0
TOTAL                                             97        97         0     97     0          0
check-traces: all 97 guarded trace(s) behaved as expected
annotations: no @ref at the end of a file or after code on a line

check.sh (G5): GREEN
```

- `srcrefs.py check --refs` over every `g5-` module against `inputs/charities-jersey-law-2014-2026-10-02.txt`: the line above (0 problems).
- The Law's text was compared with the official PDF's text layer for Articles 13 and 14 (`work/g5/crosscheck.py`, page headers removed, whitespace folded): 1,492 words each, no difference.
  Articles 13 and 14 carry no endnote marker.
- Articles 13 and 14 state no number: no period, amount, count or penalty.
  Every number in the tests is a scenario input (a date, the 14 days of readings B and C of F5.1, the 30 days of a court order, which are not the Law's).
- `g5-tests-properties.l4` has a positive control: with the end of the year of reading C moved one day earlier (a scratch copy, not the deposit), the two assertions about the anniversary readings fail and the other two stay satisfied.
- Mutation test of the tests (`work/g5/mutate.py`, `mutations.tsv`, results in `mut/results.txt`): 52 text mutations of the three rule modules, each applied to a scratch copy and run against the four assertion modules and the traces; all 52 are killed.
  One mutation (dropping `ceased to meet` from F5.8 A) first survived and exposed an untested case, a charity that never met the original condition and has a prior permission; the case now has a fixture and assertions.
  The mutations test the assertion and trace modules, not the property test, whose control is the bullet above.
- `peeked`: nothing.
  No file under the forbidden directories was opened.
  The harness's auto-loaded context mentioned this subject in a memory index; none of the files it indexes was opened.
