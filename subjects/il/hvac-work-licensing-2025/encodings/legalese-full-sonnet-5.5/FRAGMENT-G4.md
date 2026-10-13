# FRAGMENT-G4: the Registrar and the Council (sections 19 to 29)

Written by ENCODER G4 on 2026-10-13 for the row `legalese-full-sonnet-5.5`.
Status: draft.
No domain expert has read any of it against the Law.
Everything below is the encoder's reading; where the Law does not settle a point the section says so and the alternative is a callable function with a test.

Modules, in `DEPOSIT`: `g4-registrar.l4` (s.19), `g4-council-membership.l4` (ss.20 to 23), `g4-council-work.l4` (ss.24 to 28), `g4-conflict.l4` (s.29), and `g4-composition.l4` on top of the four (the wiring between them; section 5).
Tests: `g4-tests-registrar.l4`, `g4-tests-membership.l4`, `g4-tests-council-work.l4`, `g4-tests-conflict.l4`, `g4-tests-composition.l4`, and `g4-tests-red.l4` (17 expectations that are meant to fail).
Source: `inputs/law.wiki` lines 159 to 242 (Wikisource revision 2947808), checked against the gazette (Sefer HaChukim 3349, pp. 186 to 189).
Binary: `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187` (verified at the start of the work).
The time module `il-interpretation-time.l4` was used unedited; its sha256 `d1552de57266d7dc7a5d2fca43b73e100b8814dc78f33fb755daeb2294cf671f` was verified by the check script.

## 0. What changed from the PLAN and the slice, and how the files were made

- **Module boundary.** s.24 (the saving of the Council's acts) is in `g4-council-work.l4`, not `g4-council-membership.l4` as the PLAN had it, because s.24 and s.25(a) count the same base ("רוב חבריה") and the IP7 function needs both without a cross-module import.
- **Dispositions.** Rows 20(1) to 20(11) stay `inert`, as the slice proposed and the assignment says to accept: they are composition (which office fills which seat is the 11 constructors of `Council seat`, the count and the chair test are in the lead-in rules). Under ruling 2 the computable preconditions of an appointment are nevertheless encoded, one rule per item (`s 20(n) — …`: the position held, the proposal of the competent Minister or Commissioner, the Minister's opinion, the exclusion of engineers), so those rows list a rule although they are `inert`. The one disposition changed is row 25(e), proposed `inert` and `encoded`, because "תקבע" is a duty with a precondition (the Law has not fixed the matter). Row 29(a) (the lead-in) stays `inert`.
- **Counts after encoding:** 51 encoded, 12 inert, 0 refused, 7 out-of-scope, 0 deferred (the slice proposed 50, 13, 0, 7; the difference is row 25(e)). Named refusals live inside encoded rows (section 8).
- **Imports.** The lead ruled that brief ruling 1 forbids only imports across groups: a group's own modules may import one another, the graph kept acyclic, and no module of another group is imported. The four modules were written first and stay independent of one another (every fact one decides and another takes is a `GIVEN` under a standard name or a record field, section 5); `g4-composition.l4` sits on top of them and calls the deciding module in place of each of those inputs. The graph, generated from the files' `IMPORT` lines (`prelude`, `daydate`, `il-interpretation-time` and `domain` are the shared libraries):

```
g4-registrar             -> prelude, domain
g4-council-membership    -> prelude, daydate, il-interpretation-time, domain
g4-council-work          -> prelude, domain
g4-conflict              -> prelude, domain
g4-composition           -> prelude, daydate, domain, g4-registrar, g4-council-membership, g4-council-work, g4-conflict
g4-tests-registrar       -> prelude, domain, g4-registrar
g4-tests-membership      -> prelude, daydate, il-interpretation-time, domain, g4-council-membership
g4-tests-council-work    -> prelude, domain, g4-council-membership, g4-council-work
g4-tests-conflict        -> prelude, domain, g4-conflict
g4-tests-composition     -> prelude, daydate, domain, g4-registrar, g4-council-membership, g4-council-work, g4-conflict, g4-composition
g4-tests-red             -> prelude, daydate, il-interpretation-time, domain, g4-registrar, g4-council-membership, g4-council-work, g4-conflict
```

- **How the files were made.** The modules are generated from `work/g4/src/*.l4.in` by `work/g4/build.py`, which replaces each `@@QUOTE N [M]` line with the `-- src:N | …` quotation lines that `srcrefs.py quote` prints from `inputs/law.wiki`. No Hebrew in a quotation line was typed. Hebrew inside other comments was typed from the text and is checked by `work/g4/check-hebrew.py` (every double-quoted Hebrew span a verbatim slice of the Law; every Hebrew word present in it): 0 problems. This file's own Hebrew is checked the same way.
- **Gazette.** `work/g4/check-gazette.py` compares ss.19 to 29 as bags of words and numbers with the gazette text layer (pp. 186 to 189): every word and number of the Wikisource text occurs in the gazette, and the gazette words the Wikisource lines do not account for are headings, page numbers, the reversed running header and footnote citations. The page images were also read by eye (`work/g4/pages/gz-06.png` to `gz-09.png`). No difference was found, so no fork between the two sources was needed in this scope. One oddity is in both: "לרבות קרוב כאמור שהוא שלוב (חורג)" in s.29(a) (section 7).
- **Regulative rules, and what the language checks.** Every duty, power and prohibition is a `PARTY … MUST/MAY/SHANT` rule over an action type whose first actor-typed field is `actor IS A Party`. The language refuses a wrong performer on a trace event and on a constant act, but not on an enum constructor inside a rule (measured), so every rule is traced with its own `PARTY` as performer.
- **A DEONTIC has no equality, so a `#TRACE` cannot be asserted.** Each `#TRACE` therefore carries its expected outcome in a `-- EXPECT FULFILLED | BREACH <reason> | STANDING <text>` comment, and `work/g4/trace-expect.py` compares it with what `l4 run --json` reports for that directive. The INTEGRATOR's `check.sh` does not run this; the 92 traces are checked only by that script.

## 1. Coverage

One row per provision of the scope, in the Law's numbering (the 70 rows of the slice).
A row's note says where the disposition differs from the slice.
Rule names are found by prefix in the built modules, so every name quoted is exact; rules whose name contains "alternative reading" are the callable alternatives of section 2 and are not repeated here.

| row | provision | disposition | module | rule or declaration (exact names) | note |
| --- | --- | --- | --- | --- | --- |
| 19 | s.19 | encoded | g4-registrar | (none) | container: the rules are under 19(a), (b), (c) |
| 19(a) | s.19(a) | encoded | g4-registrar | `s 19(a) — the person was appointed to hold the Registrar's powers`<br>`s 19(a) — the Minister must appoint, from among the Ministry's employees, a person to hold the Registrar's powers` | publication of notice names no actor: fork F-19a-actor; publication is not a condition of the appointment: fork F-19a |
| 19(b) | s.19(b) | encoded | g4-registrar | `s 19(b) — the study programme needs the Registrar's consent`<br>`s 19(b) — the study programme has the Registrar's consent`<br>`s 19(b) — the study programme satisfies the requirement of the Registrar's consent`<br>`s 19(b) — the Registrar may give consent to the study programme` | passive requirement of consent: a boolean, plus the Registrar's MAY |
| 19(c) | s.19(c) | encoded | g4-registrar | `s 19(c) — the foreign qualification was recognised under section 19(c)` | container; the consequence for IP5 is `s 19(c) — the foreign qualification was recognised under section 19(c)` |
| 19(c)(1) | s.19(c)(1) | encoded | g4-registrar | `s 19(c)(1) — a foreign qualification may be recognised`<br>`s 19(c)(1) — the Registrar may recognise the foreign qualification` | fork F-19c-advice |
| 19(c)(2) | s.19(c)(2) | encoded | g4-registrar | `s 19(c)(2) — in a decision to recognise, the Registrar must consider the level, programme, scope and duration of the studies`<br>`s 19(c)(2) — the Registrar considered the level, programme, scope and duration of the studies`<br>`s 19(c)(2) — the Registrar may make the recognition conditional on a test, training or both` | the duty to consider is four acts in parallel (RAND); the power to attach a condition is a MAY |
| 20 | s.20 | encoded | g4-council-membership | `the eleven seats of the Council`<br>`s 20 — the number of seats on the Council`<br>`s 20 — the candidate satisfies the conditions of the seat`<br>`s 20 — the Minister must appoint a member to the seat`<br>`s 20 — the Minister must appoint a member to each of the seats`<br>`s 20, s 21, s 29(b) — the candidate may be appointed to the seat` | the lead-in: eleven seats, the Minister's duty to appoint, the chair |
| 20(1) | s.20(1) | inert | g4-council-membership | `s 20(1) — the candidate represents the senior occupations-regulation division of the Ministry`<br>`s 20(1) — the seat is the chair's` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2; also the chair test (T43) |
| 20(2) | s.20(2) | inert | g4-council-membership | `s 20(2) — the candidate is the Registrar` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(3) | s.20(3) | inert | g4-council-membership | `s 20(3) — the candidate is the Commissioner for Standards at the Ministry of Economy and Industry or an employee on the Commissioner's behalf` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(4) | s.20(4) | inert | g4-council-membership | `s 20(4) — the candidate is an employee of the Ministry of Energy and Infrastructure, appointed on the proposal of its Minister` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(5) | s.20(5) | inert | g4-council-membership | `s 20(5) — the candidate is an employee of the Ministry of Environmental Protection, appointed on the proposal of its Minister` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(6) | s.20(6) | inert | g4-council-membership | `s 20(6) — the candidate is an employee of the National Fire and Rescue Authority, appointed on the proposal of the Fire and Rescue Commissioner` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(7) | s.20(7) | inert | g4-council-membership | `s 20(7) — the candidate represents the workers' organisation with the most holders of grade 1, 2 or 3 licences and is neither a practical engineer nor an engineer` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(8) | s.20(8) | inert | g4-council-membership | `s 20(8) — the candidate represents an employers' organisation that in the Minister's opinion is representative in the field` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(9) | s.20(9) | inert | g4-council-membership | `s 20(9) — the candidate represents the organisation that in the Minister's opinion represents the most engineers working in the field` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(10) | s.20(10) | inert | g4-council-membership | `s 20(10) — the candidate represents the representative organisation as defined in the Engineers and Technicians Law` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 20(11) | s.20(11) | inert | g4-council-membership | `s 20(11) — the candidate is a public representative whose main occupation is, in the Minister's opinion, work on cooling systems` | composition, `inert` as the slice and the assignment have it (which office fills the seat is the constructor of `Council seat`); the item's appointment precondition is nevertheless carried as this rule, under ruling 2 |
| 21 | s.21 | encoded | g4-council-membership | `s 21 — the proceeding bars the person from appointment`<br>`s 21 — the person is barred from appointment to the Council`<br>`s 21 — the Minister must not appoint to the Council a person barred by section 21` | T29 on the s.21 side; the passive prohibition is put on the Minister: fork F-21-actor |
| 22 | s.22 | encoded | g4-council-membership | `s 22 — the seat has a term of four years`<br>`s 22 — the last day of the term of office when`<br>`s 22 — the last day of the term of office of the member in the seat`<br>`s 22 — the Minister may extend the term of the member in the seat` | P19, kind V: forks F-22-V, F-22-length |
| 23 | s.23 | encoded | g4-council-membership | `s 22, s 23 — the member is serving on the day` | container; whether a member is serving on a day: fork F-day |
| 23(a) | s.23(a) | encoded | g4-council-membership | `s 23(a) — the earlier of the possible days`<br>`s 23(a) — the day the member ceased to serve under section 23(a)` | ceasing to serve of one's own accord |
| 23(a)(1) | s.23(a)(1) | encoded | g4-council-membership | `s 23(a)(1) — the day the member's service ended by resignation` |  |
| 23(a)(2) | s.23(a)(2) | encoded | g4-council-membership | `s 23(a)(2) — the day the member's service ended by ceasing to be employee or member, or by becoming a State employee` | seat 11 reads the State-employee limb; seats 1 to 10 the ceasing limb |
| 23(b) | s.23(b) | encoded | g4-council-membership | `s 23(b) — a ground for removal exists`<br>`s 23(b) — the Minister's duty to remove the member arises`<br>`s 23(b) — the Minister must remove the member by written notice` | contradiction C-23a-b3 (the duty arises while the member still serves) |
| 23(b)(1) | s.23(b)(1) | encoded | g4-council-membership | `s 23(b)(1) — the proceeding is a ground for removal` | trap T29, fork F-23b1 |
| 23(b)(2) | s.23(b)(2) | encoded | g4-council-membership | `s 23(b)(2) — the member is permanently unable to perform the function` | a judgement, an input |
| 23(b)(3) | s.23(b)(3) | encoded | g4-council-membership | `s 23(b)(3) — the member ceased to meet a condition required for the appointment` | fork F-23b3 |
| 23(c) | s.23(c) | encoded | g4-council-membership | `s 23(c) — the member was absent from the meeting without justification`<br>`s 23(c) — the meetings of the Council itself among`<br>`s 23(c) — three consecutive meetings were missed without justification, counting a run of`<br>`s 23(c) — the member was absent without justification from three consecutive meetings of the Council`<br>`s 23(c) — the meeting was held during the year ending on`<br>`s 23(c) — the member was absent without justification from more than half of the meetings of the Council held during the year ending on`<br>`s 23(c) — a ground for removal by absence exists on`<br>`s 23(c) — the Minister may remove the member for absence` | P20, kind B: forks F-23c-year, F-23c-sub |
| 23(d) | s.23(d) | encoded | g4-council-membership | `s 23(d) — the Minister must not end a member's term under section 23(b) or (c) before the member had the opportunity to put arguments in writing` | a SHANT on the Minister; also a precondition of every removal act |
| 23(e) | s.23(e) | encoded | g4-council-membership | `s 23(e) — the Minister must appoint another member to the seat of one who ceased to serve` | "as soon as possible" is kind N, a judgement on the act |
| 24 | s.24 | encoded | g4-council-work | `s 24 — the saving of the Council's acts applies` | module changed from g4-council-membership to g4-council-work (see section 0); the saving is named for what it saves, not for validity |
| 25 | s.25 | encoded | g4-council-work | (none) | container |
| 25(a) | s.25(a) | encoded | g4-council-work | `s 25(a) — the serving members present at`<br>`s 25(a) — the meeting has a quorum`<br>`s 25(a), (b) — the Council's decision is carried at the meeting` | fork F-base |
| 25(b) | s.25(b) | encoded | g4-council-work | `s 25(b) — the number of serving members present who voted for, at`<br>`s 25(b) — the number of serving members present who voted against, at`<br>`s 25(b) — the chair voted for, at`<br>`s 25(b) — the chair voted against, at`<br>`s 25(b) — the votes carry the proposal at` | the tie with no chair vote is a named refusal: fork F-25b-tie |
| 25(c) | s.25(c) | encoded | g4-council-work | `s 25(c) — the Council may deliberate in an incomplete composition` | trap T28, fork F-T28 |
| 25(d) | s.25(d) | encoded | g4-council-work | `s 25(d) — the Council may use advisers and experts who can help form its position` |  |
| 25(e) | s.25(e) | encoded | g4-council-work | `s 25(e) — the Council must fix its working methods and procedures where the Law has not`<br>`s 25(e) — the subcommittee's procedure was as the Council fixed it, if it fixed one` | disposition changed from inert to encoded: "תקבע" is a duty with a precondition (the Law has not fixed the matter); slice proposed `inert` |
| 26 | s.26 | encoded | g4-council-work | (none) | container |
| 26(a) | s.26(a) | encoded | g4-council-work | `s 24 to 26 — the advice of`<br>`s 24 to 26 — the Council's advice was validly given`<br>`s 26 — the Council was consulted` | container; the IP7 interface |
| 26(a)(1) | s.26(a)(1) | encoded | g4-council-work | `s 26(a)(1) — the Council must advise the Minister on exempting classes of work on cooling systems from the licence` | fork F-26a |
| 26(a)(2) | s.26(a)(2) | encoded | g4-council-work | `s 26(a)(2) — the Council must advise the Registrar on the Ministry's policy` | fork F-26a |
| 26(a)(3) | s.26(a)(3) | encoded | g4-council-work | `s 26(a)(3) — the Council must advise the Registrar on an individual application or decision` | fork F-26a; the list after "לרבות" is an illustration |
| 26(a)(4) | s.26(a)(4) | encoded | g4-council-work | `s 26(a)(4) — the Council must perform any other function the Law gives it` | fork F-26a |
| 26(b) | s.26(b) | encoded | g4-council-work | `s 26(b) — the Council may appoint a subcommittee, from its members or from outside, to advise it`<br>`s 26(b) — the Council may delegate its powers in the function to a subcommittee`<br>`s 26(b) — the Council's power to delegate its powers in the function to the subcommittee` | forks F-26b, F-26-sub |
| 27 | s.27 | encoded | g4-council-work | (none) | container |
| 27(a) | s.27(a) | encoded | g4-council-work | `s 27(a) — the member is not a State, budgeted-body or supported-body employee`<br>`s 27(a) — the member is entitled to payment from the Ministry for taking part in meetings` | gap G-27 and contradiction C-27 |
| 27(b) | s.27(b) | encoded | g4-council-work | `s 27(b) — the member is a State employee, a budgeted-body employee or an employee of the body the member represents`<br>`s 27 — the member is entitled to a refund of reasonable travel expenses` | contradiction C-27 |
| 28 | s.28 | encoded | g4-council-work | `s 28 — the provision of`<br>`s 28 — the member with the employment` | fork F-28-scope |
| 28(1) | s.28(1) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Public Service (Gifts) Law 1979` of the list of enactments |
| 28(2) | s.28(2) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Penal Law, the provisions concerning public servants`; reached only for the provisions it names (an input flag) |
| 28(3) | s.28(3) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Public Service (Restrictions after Retirement) Law 1969` |
| 28(4) | s.28(4) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Civil Service (Restriction of Party Activity and Fund-raising) Law 1959, the provisions on all State employees`; reached only for the provisions it names |
| 28(5) | s.28(5) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Evidence Ordinance, the provisions on a public servant's certificate`; reached only for the provisions it names |
| 28(6) | s.28(6) | out-of-scope | g4-council-work | `DECLARE Enactment named in section 28` | constructor `the Knesset Elections Law` |
| 29 | s.29 | encoded | g4-conflict | (none) | container |
| 29(a) | s.29(a) | inert | g4-conflict | (none) | lead-in "בסעיף זה –": no content; each definition has its own row |
| 29(a)/def1 | s.29(a) def.1 | encoded | g4-conflict | `s 29(a) def.1 — the relation is that of a family member` | step-relations are included in each kind: no separate constructor |
| 29(a)/def2 | s.29(a) def.2 | out-of-scope | g4-conflict | `DECLARE Party in relation to a member of the Council` | the Securities Law 1968 defines "בעל עניין": each fact that someone is an interested party is a BOOLEAN field of `Party in relation to a member of the Council` |
| 29(a)/def3 | s.29(a) def.3 | encoded | g4-conflict | `s 29(a) def.3 — the way of dealing with the matter is handling` | "לרבות": an open list; the residue is an input |
| 29(a)/def4 | s.29(a) def.4 | encoded | g4-conflict | `s 29(a) def.4, (e) — the member, who sits in one of the seats 7 to 11:` | the conflict test, with the s.29(e) exception applied |
| 29(a)/def5 | s.29(a) def.5 | encoded | g4-conflict | `s 29(a) def.5 — the party is a relative of the member` | four categories |
| 29(a)/def5(1) | s.29(a) def.5(1) | encoded | g4-conflict | `s 29(a) def.5(1) — the party is a family member of the member` |  |
| 29(a)/def5(2) | s.29(a) def.5(2) | encoded | g4-conflict | `s 29(a) def.5(2) — the member has an interest in the financial position of the party` | a judgement about the member, an input |
| 29(a)/def5(3) | s.29(a) def.5(3) | encoded | g4-conflict | `s 29(a) def.5(3) — the party is a corporation in which the member, a family member or a person of category (2) is an interested party` |  |
| 29(a)/def5(4) | s.29(a) def.5(4) | encoded | g4-conflict | `s 29(a) def.5(4) — the party is a body that the member, a family member or a person of category (2) manages or is responsibly employed in` |  |
| 29(b) | s.29(b) | encoded | g4-conflict | `s 29(b) — the person is barred from the Council by regular conflicts of interest`<br>`s 29(b) — the Minister must not appoint to the Council a person who would regularly be in a conflict of interest preventing the main part of the function`<br>`s 29(b) — a member who would regularly be in a conflict of interest preventing the main part of the function must not serve` | a boolean and two prohibitions (the Minister must not appoint, the member must not serve): fork F-29b-actor |
| 29(c) | s.29(c) | encoded | g4-conflict | `s 29(c) — a member must not handle a matter whose handling puts the member in a conflict of interest` |  |
| 29(d) | s.29(d) | encoded | g4-conflict | `s 29(d) — a member who learned of a possible conflict must tell the chair as soon as possible`<br>`s 29(d) — a chair who learned of a possible conflict must tell the Minister as soon as possible` | two duties: the member tells the chair, the chair tells the Minister; "בהקדם האפשרי" is kind N |
| 29(e) | s.29(e) | encoded | g4-conflict | `s 29(e) — a member who sits in one of the seats 7 to 11:`<br>`s 29(a) def.4, (e) — the member, who sits in one of the seats 7 to 11:` | the MAY, and the exception inside the conflict test |

## 2. Forks

Each fork gives the readings, the one taken, the text that licenses each, the callable alternative (exact name) and the test.
"Red n" is the assertion in `g4-tests-red.l4` that states the rejected reading's answer against the reading taken; it must fail.
The Interpretation Law is written "IL" throughout; the Law's own s.10(c) is not met in this scope.

### 2.0 One fork for every kind of period met (brief, ruling 4)

Periods in ss.19 to 29 (PLAN section (d), P19 to P21): **V** one (s.22: four years), **B** one (s.23(c): one year, counted backwards), **N** several (s.23(b), s.23(e), s.29(d)).
I met no deadline for doing something (D), no window for an application or request (W) and no commencement counted from another date (C) in ss.19 to 29.
I looked at every sentence of the scope that carries a number or a word of time: "11 חברים", "ארבע שנים", "משלוש ישיבות רצופות", "ממחצית הישיבות", "שנה אחת", "בסמוך למועד", "בהקדם האפשרי".
So IL s.10(c) is applied to no period here, and the default for D and W (apply it) is not exercised by this group.
The kind-V fork is F-22-V; the kind-B fork is F-23c-year; the kind-N fork is below.

- **F-22-V (kind V: IL s.10(c) and a term).** Reading taken (the fleet default for V): IL s.10(c) is not applied; the term's last day is `s 10(b) — the last day of a period of 4 years after an event on` the day of appointment, and that day is inside the term. Alternative: IL s.10(c) applied, so an end on a day of rest moves to the first day that is not one. Text: s.22 "תקופת כהונתו … תהיה ארבע שנים"; IL s.10(b) and (c) (`il-interpretation-time.l4`). A term is a duration, not a time within which someone must act, and moving its end would lengthen it by a rest day. Callable: `s 22, alternative reading — the last day of the first term when IL s.10(c) moves an end that falls on a day of rest, appointed on` … `with days of rest` … (takes a `Calendar of rest days`). Tests: `g4-tests-membership.l4` (appointed 2025-06-30, end Saturday 2029-06-30: unmoved; alternative with Saturday and Sunday rest days 2029-07-02, with Saturday only 2029-07-01, with none 2029-06-30; a Monday end unmoved by the same calendar). Red 3.
- **F-22-length.** The text does not say how long a further term is. Reading taken: each further term is four years counted on from the last day of the term before it ("תקופת כהונתו … ארבע שנים, ורשאי השר להאריך … לתקופות כהונה נוספות": each further one is a term of office, "תקופות כהונה נוספות"). Alternative: the Minister fixes the length of each further term (a list of years). Callable: `s 22, alternative reading — the last day of a term when the Minister fixes each further term, appointed on` … Tests: 2033-07-16 and 2037-07-16 against 2031-07-16 (a further term of two years), 2030-07-16 (one year), 2032-07-16 (two then one). Red 4. There is no limit on the number of further terms in the text, and none is encoded.
- **F-23c-year (kind B).** "מיותר ממחצית הישיבות שקיימה במהלך שנה אחת": which year. IL s.10 does not cover a period counted backwards and "one year" here is not a period "from" a day, so IL s.10 is not claimed to govern it. Reading taken: the year ending on the day of removal; a meeting belongs to it if it is not after that day and the day of removal falls before the first anniversary of the meeting (this uses the time module forwards from the meeting, so no date is ever subtracted). Alternatives: any one year at all (`s 23(c), alternative reading — … held during some one year, among`), a calendar year (`… held in the calendar year` n `, among`). Tests: the year ending 2026-06-30 begins 2025-07-01 (two absences on 2025-06-30 are outside, two on 2025-07-01 inside, two on 2026-06-30 inside, two on 2026-07-01 outside); the year ending 2025-02-28 begins 2024-03-01 (two absences on 2024-02-29 outside, two on 2024-03-01 inside); the discriminating list (two absences early in 2024, attendance in mid 2025): reading taken no, any-year yes, calendar 2024 yes. Red 10.
- **F-23c-sub.** "ישיבות רצופות של המועצה": meetings of a subcommittee. Reading taken: they are not meetings of the Council and are filtered out. Alternative: pass them in the list as meetings of the Council (field `held by a subcommittee of the Council` FALSE); no separate function is needed. Test: three unjustified absences at subcommittee meetings are no ground; the same dates as Council meetings are. Red 11.
- **Kind N (vague time).** "בסמוך למועד התקיימות הנסיבה" (s.23(b)), "בהקדם האפשרי" (s.23(e), s.29(d)). No number is invented and no `WITHIN` is written (a `WITHIN` would write a deadline nobody enacted). The judgement is a field of the act (`close to the time the circumstance arose`, `as soon as possible after the previous member ceased`, `as soon as possible`): performance of the duty is the act itself, and a `HENCE (IF … THEN FULFILLED ELSE BREACH …)` records a late act as a breach of the timing without un-doing the act. The alternative (a number of days) is not offered because the text gives none. Tests: each rule traced with the field TRUE (fulfilled), FALSE (breach naming the timing) and with no act at all, however long the clock runs (the duty stands).
- **F-19a (s.19(a): is publication a condition of the appointment).** Reading taken: no; the appointment counts when the Minister appointed a Ministry employee. Alternative: only once notice was published in Reshumot. Text: "הודעה על מינוי הרשם תפורסם ברשומות" is a separate duty; s.2 defines the Registrar as "מי שמונה לפי סעיף 19". Callable: `s 19(a), alternative reading — the appointment counts only once notice of it was published`. Test: `g4-tests-registrar.l4`. Red 1.
- **F-19a-actor.** The sentence about notice names no actor. Reading taken: the Minister, who appoints (the publication duty is the `HENCE` of the appointment). Alternative: the Ministry. Callable: `s 19(a), alternative reading — the Ministry must publish notice of the appointment of the Registrar in Reshumot`. Test: a trace.
- **F-19c-advice.** "לאחר התייעצות עם המועצה": reading taken, the Council was consulted and its advice was validly given (ss.24 to 26), since a body that could not lawfully give advice was not consulted as the Council; the Registrar is not bound by what the advice says. Alternative: consulted is enough. Callable: `s 19(c)(1), alternative reading — a foreign qualification may be recognised once the Council was consulted`. Test: consulted but advice not validly given: reading taken no, alternative yes. Red 2.
- **F-base (the base of "רוב חבריה" in s.24 and s.25(a)).** Reading taken: the eleven seats of s.20, so a majority is six and the quorum is six with the chair among them. Alternative: the members serving on the day. For: s.24 says "מכהנים בה רוב חבריה": a majority of its members serve in it, which is a tautology if "its members" are the serving ones. Against: s.25(c) says "כל חבריה זומנו כדין", and a vacant seat has no member to summon, so there "its members" must be the serving ones (contradiction C-25, section 6). Callable: `s 25(a), alternative reading — the meeting has a quorum, a majority of the members serving being enough` (s.24 has no alternative: under it the proviso is empty). Tests: eight serving, five present with the chair: reading taken no quorum, alternative quorum; four present: neither; five present without the chair: neither. Red 12.
- **F-T28 (trap T28).** Whether the Council may decide, not only deliberate, at a meeting held in an incomplete composition (s.25(c) against s.25(a)). Reading taken: (c) permits discussion only; a decision needs the quorum of (a) and the majority of (b), because (c) says "לדון" (deliberate), (b) says "החלטות" (decisions), and (a) fixes "המניין החוקי" for meetings. Alternative: (c) relaxes (a). Callable: `s 25(c), alternative reading — the Council's decision is carried at a meeting held in an incomplete composition`. Test: three present with the chair, every member summoned, 2 to 1: reading taken no decision, alternative carried. Red 13.
- **F-25b-tie.** A tie in which the chair cast no vote: "תכריע דעתו של יושב ראש המועצה" gives the casting vote to the chair's opinion and says nothing when there is none. Reading taken: a named refusal, not FALSE. Alternative: a tie with no chair vote fails the proposal. Callable: `s 25(b), alternative reading — a tie in which the chair cast no vote fails the proposal, at`. Tests: refusal asserted with its message; the alternative answers FALSE. Red 14 (asserting that the alternative refuses fails because it answers).
- **F-26a (functions as duties or powers).** "תפקידי המועצה הם: לייעץ …". Reading taken: duties (MUST, no time), since s.20 says the Council "שתמלא את התפקידים". Alternative: powers (MAY). Callable: `s 26(a), alternative reading — the Council may perform the function`. Tests: traces for both.
- **F-26-sub (and F-26b).** Whether a subcommittee's advice is "the Council's" for a consultation. Reading taken: only for the function of s.26(a)(3), the only one for which s.26(b) lets the Council delegate its powers, and only if the Council delegated and the subcommittee proceeded as the procedure the Council fixed under s.25(e) requires; if the Council fixed no procedure the text does not answer (named refusal, and only where the answer is not already FALSE). Alternative: delegated advice suffices for every function. Callable: `s 24 to 26, alternative reading — the Council's advice was validly given, a subcommittee's delegated advice sufficing for every function`. Tests: a subcommittee on function (2) or (1): reading taken no, alternative yes. Red 15. Delegation for the other functions is read as not granted (expressio unius: the text names (a)(3) alone).
- **F-21-actor and F-29b-actor.** "לא ימונה" and "ולא יכהן" are passive and name no actor. Reading taken: the prohibition falls on the appointer of s.20, the Minister, and, for service, on the member (s.29(b)). Alternative: an actor-free constitutive bar. Callables: `s 21 — the person is barred from appointment to the Council`, `s 29(b) — the person is barred from the Council by regular conflicts of interest` (both tested on every branch).
- **F-day.** The day a member's service ends (resignation, ceasing, removal). Reading taken: the member does not serve from the day of the event; the last day of the term is a day of service (IL s.10(b)). Alternative: the day of the event is a day of service. Callable: `s 22, s 23, alternative reading — the member is serving on the day` … Tests: resignation on 2026-03-01, removal on 2027-01-10, both sides. Red 5.
- **F-20-2 (the Registrar's membership and the office).** s.22 excludes the Registrar from the four-year term; s.20(2) makes "הרשם" a member. Reading taken: nothing ends the Registrar's membership with the office; ceasing to be the Registrar is the loss of a condition of seat 2, a ground for removal under s.23(b)(3), so the Registrar serves until the Minister removes him. Alternative: the seat is the office's, so membership ends the day the person ceases to be the Registrar. Callable: `s 20(2), s 22, alternative reading — the Registrar's membership continues on the day` … Tests: office ended 2026-03-01, serving on 2026-03-15: reading taken yes, alternative no. Red 6. The Registrar's seat has no end by term: `s 22 — the last day of the term of office of the member in the seat` answers NOTHING, the source's own absent case.
- **F-23b1 (trap T29).** See contradiction C-T29 (section 6). Reading taken: s.23(b)(1) is read as written, so a proceeding on an offence that makes the person unfit is a ground whatever became of it. Alternative: it mirrors s.21. Callable: `s 23(b), alternative reading — a ground for removal exists`. Red 7.
- **F-23b3.** "תנאי מהתנאים הדרושים למינויו": which conditions. Reading taken: all the conditions the Law puts on appointment: the item of s.20, the bar of s.21 and the bar of s.29(b). Alternative: only the item of s.20. Callable: `s 23(b)(3), alternative reading — the member ceased to satisfy the conditions of the seat`. Test: a member barred by s.29(b) only. Red 8.
- **C-23a-b3.** See section 6. Reading taken: the duty to remove arises only while the member still serves. Alternative: whenever a ground exists. Callable: `s 23(b), alternative reading — the Minister's duty to remove the member arises whether or not the member has ceased under section 23(a)`. Red 9.
- **C-27 and G-27.** See section 6. Reading taken: s.27(b) prevails over (a). Alternative: (a) prevails. Callable: `s 27, alternative reading — the member is entitled to a refund of reasonable travel expenses, section 27(a) prevailing`. Red 16.
- **F-28-scope.** "לעניין חיקוקים אלה ולעניין פעולותיהם במועצה". Reading taken: both, the listed enactment and an act in the Council. Alternative: the listed enactment whatever the act. Callable: `s 28, alternative reading — the member with the employment` … `whatever the act, a provision the item names being` … Red 17.

## 3. Answer table: headline scenarios

Each row is asserted or traced in the test module of its section; the expected value was decided from the Hebrew before the module ran.

| scenario | section | answer |
| --- | --- | --- |
| the Minister appoints a Ministry employee, notice not yet published | s.19(a) | appointed (reading taken); the duty to publish stands |
| a study programme from which a s.6(a)(4) final certificate can be obtained, without the Registrar's consent | s.19(b) | the requirement of consent is not satisfied |
| a foreign degree, Council consulted, advice not validly given, the Registrar's opinion that scope and content match | s.19(c)(1) | may not be recognised (reading taken); may under F-19c-advice |
| the number of seats; the chair | s.20, s.20(1) | 11; seat 1, not the Registrar's |
| seat 4 candidate who is an employee of the Ministry of Energy and Infrastructure but was not proposed by its Minister | s.20(4) | conditions not satisfied |
| seat 7 candidate who is an engineer | s.20(7) | not satisfied |
| convicted of an offence that makes the person unfit; charged for it, no final judgment yet; charged and acquitted | s.21 | barred; barred; not barred |
| appointed 2025-07-16: last day of the first term; after one further term; the Registrar's seat | s.22 | 2029-07-16; 2033-07-16; no end by term (NOTHING) |
| appointed 2096-02-29 | s.22 with IL s.10(b) | 2100-02-28 (2100 is not a leap year) |
| appointed 2025-06-30: end falls on Saturday 2029-06-30 | s.22 (kind V) | 2029-06-30, unmoved; 2029-07-02 under IL s.10(c) with Saturday and Sunday as rest days |
| a seat 4 member resigns by a letter delivered on 2026-03-01 | s.23(a)(1) | serving on 2026-02-28, not on 2026-03-01 |
| a public representative is appointed a State employee; a seat 4 member is | s.23(a)(2) | service ends; no effect |
| a member charged for an offence that makes the person unfit and later acquitted | s.21, s.23(b)(1) | no bar on appointment; a ground for removal (reading taken) |
| a member permanently unable; the removal is by written notice after the chance to answer in writing, close to the time | s.23(b)(2), (d) | the Minister must remove him; the duty is fulfilled |
| the same removal before the chance to answer | s.23(d) | breach |
| three consecutive meetings missed without justification; two; three with one justified | s.23(c) | ground; no ground; no ground |
| 6 of 10 meetings missed; 5 of 10 | s.23(c) | more than half; exactly half is not |
| six of the eleven serving, the chair among them; five; six without the chair | s.24 | the saving applies; does not; does not |
| six present with the chair; five; six without the chair; a stranger counted as the sixth | s.25(a) | quorum; none; none; none |
| 3 for, 2 against; 3 for, 3 against with the chair for; with the chair against | s.25(b) | carried; carried; not carried |
| 2 for, 2 against, the chair abstaining | s.25(b) | refusal (the text does not answer) |
| three present with the chair, every member summoned, 2 for 1 against | s.25(c), s.25(a) | may deliberate; no quorum, so no decision (reading taken) |
| advice carried at a quorate meeting; a subcommittee's delegated advice on an individual application, procedure followed; on policy | s.24 to s.26 | valid; valid; not valid |
| a member who is nobody's employee; a State employee; an employee of a private body he represents; a supported-body employee of another body | s.27 | refund yes, payment no; no refund; no refund (reading taken); refusal |
| a member who is not a State employee, an act in the Council, the Gifts Law; the same act outside the Council | s.28 | treated as a State employee; not (reading taken) |
| the parent of a spouse; a relation the definition does not list | s.29(a) def.1 | family member; not |
| a corporation in which a family member is an interested party; one in which nobody connected is | s.29(a) def.5(3) | relative; not |
| the public's interest related to the Council's functions, a member of seats 7 to 11; a member outside them | s.29(e), s.29(a) def.4 | no conflict; a conflict |
| a regular conflict that prevents the main part of the function; either alone | s.29(b) | barred; not barred |
| a member handles a matter whose handling puts him in a conflict | s.29(c) | breach |
| a member who learned of a possible conflict tells the chair late | s.29(d) | the notice stands and is a breach of "as soon as possible" |

## 4. Nouns requests for the INTEGRATOR

- **`Record of offences` (domain).** Its two "pending" fields already contain "no final judgment yet", so it cannot say that an indictment or complaint WAS filed once a final judgment has been given, and trap T29 (s.21 against s.23(b)(1)) turns on exactly that. g4-council-membership defines a local stand-in, `Proceeding against a Council candidate or member for an offence` (a list of them per person, each with the outcome `proceeding ended in a conviction`, `proceeding with no final judgment yet` or `proceeding ended in a final judgment other than a conviction`, and the judgement that the offence makes the person unfit). Move it to domain, or add an outcome to `Record of offences`, if another group (s.30(b)(1), s.6(a)(3)) needs the same history.
- No other `domain.l4` noun was missing. `Party`, `Calendar of rest days` and `Person` were used as they are; `Certificate`, `Licence`, `Applicant` were not needed by ss.19 to 29.
- Local nouns that no other group is expected to share: `Council seat`, `Candidate for a seat on the Council`, `Meeting of the Council`, `Serving member of the Council`, `Consultation of the Council`, `Source of the Council's advice`, `Function of the Council under section 26(a)`, `Employment of a member of the Council`, `Enactment named in section 28`, `Party in relation to a member of the Council`, `Study programme under section 19(b)`, `Foreign qualification under section 19(c)`, and the action types `An act under section 19`, `An act under sections 20 to 23`, `An act under sections 24 to 28`, `An act under section 29`.
- Names and the fleet-wide uniqueness rule (ruling 5): every exported rule starts with the Law's section number (`s 19(c)(1) — …`); constructors and helper rules were made specific (`a spouse of the member`, `proceeding ended in a conviction`, `s 25(a) — the serving members present at`). The Party constructor `a subcommittee of the Council` of domain.l4 is deliberately not reused for the local `a subcommittee that advises the Council`.

## 5. Standard inputs consumed, and the functions exported (wiring)

The four modules take every cross-module fact as a `GIVEN` under its standard name, so any consumer can wire them by hand, as the table below shows.
`g4-composition.l4` does that wiring for the facts that stay inside G4: `s 19(c) with ss 24 to 26 — …` (g4-registrar with the IP7 functions of g4-council-work, from a `Consultation of the Council`), `ss 20, 21 and 29(b) — the candidate may be appointed to the seat` and `s 23(b) with s 29(b) — a ground for removal exists …` (g4-council-membership with g4-conflict), `s 20, s 29(e) — the seat is one of the seats 7 to 11` and `s 29 with s 20 — the member in the seat …` (g4-conflict with the seat), and `s 22, s 23, s 20(1) — the serving members of the Council on the day …` with `s 24 with ss 22 and 23 — the saving of the Council's acts applies on the day …` (the service records of g4-council-membership with g4-council-work). It adds no reading: every fork stays in the module that decides it. The facts other groups take (IP5, IP7) are still delivered as functions of the modules above, or of these compositions, for the INTEGRATOR to wire to the other groups' inputs.

Inputs this group takes under the PLAN's standard names (the exact `GIVEN` name is the left column):

| input (exact GIVEN name) | IP | taken by | decided by |
| --- | --- | --- | --- |
| `the Council was consulted` | IP7 | g4-registrar: `s 19(c)(1) — a foreign qualification may be recognised`, `s 19(c)(1) — the Registrar may recognise the foreign qualification`, `s 19(c)(2) — the Registrar may make the recognition conditional on a test, training or both`, `s 19(c) — the foreign qualification was recognised under section 19(c)` | g4-council-work: `s 26 — the Council was consulted` |
| `the Council's advice was validly given` | IP7 | the same four rules | g4-council-work: `s 24 to 26 — the Council's advice was validly given` |
| fields named `in the Registrar's opinion …` | IP17 | g4-registrar, field of `Foreign qualification under section 19(c)` | the Registrar (an input) |
| `the candidate is barred from the Council by section 29(b)`; field `the member is barred from the Council by section 29(b)` | none (a G4-internal wire) | g4-council-membership | g4-conflict: `s 29(b) — the person is barred from the Council by regular conflicts of interest` |
| `seats7to11` | none (a G4-internal wire) | g4-conflict: `s 29(a) def.4, (e) — …`, `s 29(e) — …` | the caller, from `Council seat` (seats 7 to 11 are the constructors `seat 7: …` to `seat 11: …`) |
| `Calendar of rest days` | IP15 | only the callable alternative `s 22, alternative reading — the last day of the first term when IL s.10(c) …` | an input |

No commencement input is taken (IP2, IP16): s.63(a) fixes a commencement only "לעניין ביצוע עבודה במערכת קירור או מיזוג אוויר" and for Chapter 6, and says nothing about the Registrar or the Council (T20, F26); no day is chosen here.

What this group decides for others:

| consumer | their input (exact name) | wire it to |
| --- | --- | --- |
| G2 (s.6(a)(4), IP5) | `the programme was approved by the Registrar` | `s 19(b) — the study programme has the Registrar's consent` (and `… satisfies the requirement of the Registrar's consent` for a programme that needs none) |
| G2 (IP5) | `the foreign qualification was recognised` | `s 19(c) — the foreign qualification was recognised under section 19(c)` |
| G1 (s.3(b), s.10(a) to (d)), G3 (s.17(b), (c)) (IP7) | `the Council was consulted` | `s 26 — the Council was consulted` |
| the same | `the Council's advice was validly given` | `s 24 to 26 — the Council's advice was validly given` |

The exported (`@export`) rules, with their inputs in order:

| module | exported rule (first segment of the name) | inputs (GIVEN names, in order) | result |
| --- | --- | --- | --- |
| g4-registrar | s 19(b) — the study programme has the Registrar's consent | programme | A BOOLEAN |
| g4-registrar | s 19(b) — the study programme satisfies the requirement of the Registrar's consent | programme | A BOOLEAN |
| g4-registrar | s 19(c)(1) — a foreign qualification may be recognised | qualification, `the Council was consulted`, `the Council's advice was validly given` | A BOOLEAN |
| g4-registrar | s 19(c) — the foreign qualification was recognised under section 19(c) | qualification, matters, `the Council was consulted`, `the Council's advice was validly given` | A BOOLEAN |
| g4-council-membership | s 21 — the person is barred from appointment to the Council | proceedings | A BOOLEAN |
| g4-council-membership | s 20, s 21, s 29(b) — the candidate may be appointed to the seat | seat, candidate, proceedings, `the candidate is barred from the Council by section 29(b)` | A BOOLEAN |
| g4-council-membership | s 22 — the last day of the term of office of the member in the seat | seat, d, furtherTerms | A MAYBE DATE |
| g4-council-membership | s 23(a) — the day the member ceased to serve under section 23(a) | seat, events | A MAYBE DATE |
| g4-council-membership | s 23(b) — a ground for removal exists | facts | A BOOLEAN |
| g4-council-membership | s 23(c) — a ground for removal by absence exists on | removal, meetings | A BOOLEAN |
| g4-council-work | s 24 — the saving of the Council's acts applies | serving | A BOOLEAN |
| g4-council-work | s 25(a) — the meeting has a quorum | meeting | A BOOLEAN |
| g4-council-work | s 25(a), (b) — the Council's decision is carried at the meeting | meeting | A BOOLEAN |
| g4-council-work | s 26 — the Council was consulted | consultation | A BOOLEAN |
| g4-council-work | s 24 to 26 — the Council's advice was validly given | consultation | A BOOLEAN |
| g4-council-work | s 27 — the member is entitled to a refund of reasonable travel expenses | employment | A BOOLEAN |
| g4-council-work | s 27(a) — the member is entitled to payment from the Ministry for taking part in meetings | employment | A BOOLEAN |
| g4-council-work | s 28 — the member with the employment | employment, enactment, actInCouncil, provisionNamed | A BOOLEAN |
| g4-conflict | s 29(a) def.1 — the relation is that of a family member | kinship | A BOOLEAN |
| g4-conflict | s 29(a) def.5 — the party is a relative of the member | party | A BOOLEAN |
| g4-conflict | s 29(a) def.4, (e) — the member, who sits in one of the seats 7 to 11: | seats7to11, interests | A BOOLEAN |
| g4-conflict | s 29(b) — the person is barred from the Council by regular conflicts of interest | regularly, preventsMainPart | A BOOLEAN |
| g4-composition | s 19(c) with ss 24 to 26 — a foreign qualification may be recognised: | qualification, consultation | A BOOLEAN |
| g4-composition | s 19(c) with ss 24 to 26 — the foreign qualification was recognised: | qualification, matters, consultation | A BOOLEAN |
| g4-composition | ss 20, 21 and 29(b) — the candidate may be appointed to the seat | seat, candidate, proceedings, regularly, preventsMainPart | A BOOLEAN |
| g4-composition | s 29 with s 20 — the member in the seat | seat, interests | A BOOLEAN |
| g4-composition | s 24 with ss 22 and 23 — the saving of the Council's acts applies on the day | x, records | A BOOLEAN |

The full mixfix heads, exactly as written:

```
g4-registrar: `s 19(b) — the study programme has the Registrar's consent` programme
g4-registrar: `s 19(b) — the study programme satisfies the requirement of the Registrar's consent` programme
g4-registrar: `s 19(c)(1) — a foreign qualification may be recognised` qualification `the Council was consulted` `the Council's advice was validly given`
g4-registrar: `s 19(c) — the foreign qualification was recognised under section 19(c)` qualification matters `the Council was consulted` `the Council's advice was validly given`
g4-council-membership: `s 21 — the person is barred from appointment to the Council` proceedings
g4-council-membership: `s 20, s 21, s 29(b) — the candidate may be appointed to the seat` seat candidate proceedings `the candidate is barred from the Council by section 29(b)`
g4-council-membership: `s 22 — the last day of the term of office of the member in the seat` seat `appointed on the day` d `, after` furtherTerms `further terms granted`
g4-council-membership: `s 23(a) — the day the member ceased to serve under section 23(a)` seat events
g4-council-membership: `s 23(b) — a ground for removal exists` facts
g4-council-membership: `s 23(c) — a ground for removal by absence exists on` removal `, according to` meetings
g4-council-work: `s 24 — the saving of the Council's acts applies` serving
g4-council-work: `s 25(a) — the meeting has a quorum` meeting
g4-council-work: `s 25(a), (b) — the Council's decision is carried at the meeting` meeting
g4-council-work: `s 26 — the Council was consulted` consultation
g4-council-work: `s 24 to 26 — the Council's advice was validly given` consultation
g4-council-work: `s 27 — the member is entitled to a refund of reasonable travel expenses` employment
g4-council-work: `s 27(a) — the member is entitled to payment from the Ministry for taking part in meetings` employment
g4-council-work: `s 28 — the member with the employment` employment `is treated as a State employee under` enactment `for an act in the Council being` actInCouncil `and a provision the item names being` provisionNamed
g4-conflict: `s 29(a) def.1 — the relation is that of a family member` kinship
g4-conflict: `s 29(a) def.5 — the party is a relative of the member` party
g4-conflict: `s 29(a) def.4, (e) — the member, who sits in one of the seats 7 to 11:` seats7to11 `, is in a conflict of interest among the interests` interests
g4-conflict: `s 29(b) — the person is barred from the Council by regular conflicts of interest` regularly `with the main part of the function prevented being` preventsMainPart
g4-composition: `s 19(c) with ss 24 to 26 — a foreign qualification may be recognised:` qualification `after the consultation` consultation
g4-composition: `s 19(c) with ss 24 to 26 — the foreign qualification was recognised:` qualification `having considered` matters `after the consultation` consultation
g4-composition: `ss 20, 21 and 29(b) — the candidate may be appointed to the seat` seat candidate proceedings `, regularly in a conflict being` regularly `and the main part of the function prevented being` preventsMainPart
g4-composition: `s 29 with s 20 — the member in the seat` seat `is in a conflict of interest among the interests` interests
g4-composition: `s 24 with ss 22 and 23 — the saving of the Council's acts applies on the day` x `according to` records
```

The Council functions of the plan (`the Council has a quorum`, `the Council's decision is carried`, `the member may be appointed`, `the term has ended`, `the Minister must remove the member`, `the person is a relative of the member`, `the member is in a conflict of interest`, `a foreign qualification may be recognised`) are, respectively: `s 25(a) — the meeting has a quorum`, `s 25(a), (b) — the Council's decision is carried at the meeting`, `s 20, s 21, s 29(b) — the candidate may be appointed to the seat`, `s 22, s 23 — the member is serving on the day` (negated; and `s 22 — the last day of the term of office of the member in the seat`), `s 23(b) — a ground for removal exists` with `s 23(b) — the Minister's duty to remove the member arises`, `s 29(a) def.5 — the party is a relative of the member`, `s 29(a) def.4, (e) — the member, who sits in one of the seats 7 to 11:` … `, is in a conflict of interest among the interests` …, and `s 19(c)(1) — a foreign qualification may be recognised`.

## 6. Contradictions in the source (found in a deliberate separate pass after encoding)

Each gives the provisions, the discriminating case, and both readings as callable functions with tests (the reading taken is the first; the alternative is named in section 2).

- **C-T29: s.21 against s.23(b)(1).** s.21 bars one against whom an indictment or complaint was filed "וטרם ניתן פסק דין סופי"; s.23(b)(1) removes one against whom it "הוגשו" with no such qualifier. The case: a member charged for an offence that makes him unfit and acquitted by a final judgment. s.21: not barred (`s 21 — the person is barred from appointment to the Council` answers no); s.23(b)(1) as written: a ground for removal (`s 23(b) — a ground for removal exists` answers yes). Alternative: `s 23(b), alternative reading — a ground for removal exists`.
- **C-27: s.27(a) against s.27(b).** (a) entitles a member who is not a State, budgeted-body or supported-body employee to a refund of reasonable travel expenses; (b) denies it to a State employee, a budgeted-body employee and "עובד באותו גוף שהוא מייצג במועצה". The case: an employee of a private body that he represents on the Council, outside the three classes: (a) entitles, (b) denies. Reading taken: (b) prevails, since it refers to the refund "כאמור בסעיף קטן (א)" and so carves out of it. Alternative: `s 27, alternative reading — … section 27(a) prevailing`.
- **G-27: a gap between the same two.** A supported-body employee who is not an employee of the body he represents: (a) excludes him from its entitlement, (b) does not list him. Neither provision answers; the encoding returns a named refusal under both readings (`s 27 says nothing about the entitlement of a supported-body employee who is not an employee of the body represented on the Council`). Likewise (a) is silent about payment for the employee classes (`s 27(a) says nothing about payment to a member who is a State, budgeted-body or supported-body employee`).
- **C-25: "its members" in s.25(a) and s.25(c) (and s.24).** (a) and s.24 read naturally as a majority of the eleven (s.24's "מכהנים בה רוב חבריה" is empty otherwise); (c) says "כל חבריה זומנו כדין", which for an "הרכב חסר" can only mean the serving ones. The case: eight serving, three seats vacant, every serving member summoned, the chair and four others present: (c) the Council may deliberate; (a) on the eleven: no quorum; (a) on the members serving: quorum. Both readings are callable (`s 25(a) — …`, `s 25(a), alternative reading — …`) and tested.
- **T28: s.25(a) against s.25(c).** Whether deliberation under (c) can end in a decision (F-T28).
- **C-23a-b3: s.23(a)(2) against s.23(b)(3).** A seat 4 member who ceases to be an employee of his ministry ceases to serve at once under (a)(2); the same event is a condition required for his appointment that ceased to be fulfilled, which makes the Minister remove him under (b)(3), though there is nothing left to remove him from. Reading taken: the duty of (b) arises only while he still serves. Alternative callable: `s 23(b), alternative reading — the Minister's duty to remove the member arises whether or not the member has ceased under section 23(a)`.
- **Not contradictions, but redundancies noted:** under the base of eleven the proviso of s.24 is implied by the quorum of s.25(a) for a decision at a meeting and adds something only for the Council's other acts; s.23(b)(1) and s.23(b)(3) overlap for the s.21 bar (a conviction is both).

## 7. Open questions for a domain expert

1. Is "its members" in s.24 and s.25(a) the eleven seats or the members serving (F-base, C-25)? Which is the Ministry's practice?
2. May the Council decide at a meeting held under s.25(c) (T28)?
3. What follows from a tie in which the chair casts no vote (F-25b-tie)?
4. Should a member charged and later acquitted be removed under s.23(b)(1) (T29)?
5. Is the Registrar's membership of the Council ex officio, ending when the office does (F-20-2)? Is there any provision for ending the Registrar's own appointment? ss.19 to 29 have none (no other section was read for it).
6. s.27: does a private-body employee who represents his employer get the travel refund (C-27)? What is a supported-body employee's position (G-27)?
7. Does the advice of a subcommittee to which the Council delegated its powers satisfy a "consultation with the Council" for functions other than s.26(a)(3) (F-26-sub)? What procedure has the Council fixed under s.25(e), and for subcommittees?
8. In s.23(c): which "year", and do meetings of a subcommittee count? Does a justified absence in the middle break a run of "three consecutive meetings"? The encoding says it does (each of the three must be an unjustified absence).
9. Is each further term under s.22 four years, and is the number of further terms unlimited?
10. Is IL s.10(c) meant to move the end of a term (F-22-V)?
11. Must valid advice of the Council, and not merely consultation, precede a recognition under s.19(c)(1) (F-19c-advice)?
12. Does the Registrar's consent under s.19(b) reach study programmes of the Ministry of Education (the second kind of final certificate in s.2)?
13. Who publishes notice of the Registrar's appointment, and is publication a condition (F-19a, F-19a-actor)?
14. s.29(a), "לרבות קרוב כאמור שהוא שלוב (חורג)": "שלוב" is an unusual word beside "(חורג)" (step-); the encoding reads it as a step-relation and includes step-relations in each listed kind. Is that the meaning?
15. How is seat 7 filled ("המייצג את המספר הגדול ביותר של בעלי רישיון") before any licence has been granted?
16. Does Chapter 4 have a commencement of its own? s.63(a) speaks only of work on a system, and Chapter 6 (T20, F26).
17. "סיבה מוצדקת" (a justified reason for an absence, s.23(c)) and "ראוי" (fitness, s.21): whose judgement, and is it reviewable? The encoding takes both as inputs.

## 8. What the sources do not answer

Each is an input, a named refusal or an absent case in the encoding; none has a default.

- The Council's own rules of procedure (s.25(e)) and any quorum or voting rule for a subcommittee: a named refusal where it matters.
- What happens when a tie has no chair vote (s.25(b)): a named refusal.
- The Budget Principles Law's definitions of "State employee", "budgeted body" and "supported body" (s.27): booleans on the member. s.28 uses "State employee" with no definition at all, and s.27's definition is expressly "בסעיף זה".
- The Securities Law's "interested party" (s.29(a)): booleans on the party record.
- The Accountant General's instructions on travel expenses (s.27(a)): the amount is not computed; only the entitlement is.
- Who currently holds any seat, the identity of the Registrar, the Minister's and the Registrar's opinions, the calendar of rest days.
- Any time limit on the Council's reply to a consultation, on the Registrar's appointment, on filling a vacant seat (s.23(e) says "as soon as possible"), or on notice of the appointment.
- Whether a member who never met a condition of appointment (a defective appointment, s.24) can be removed under s.23(b)(3), which speaks of a condition that "חדל להתקיים".
- A duty to fill a seat vacated by the expiry of a term (s.23(e) covers a member who ceased under that section; the standing duty of s.20 is encoded).
- The effect of a failure of the proviso of s.24: the section saves acts only if a majority serve, and does not say the acts are void otherwise; the encoding names the saving, not validity.
- The commencement of Chapter 4 (T20, F26): no day is chosen.
- The Fourth Schedule, the Second Schedule and the other groups' facts are not touched by this scope.

## 9. What was run

The check script (a copy of the skill's `check.sh` for G4's modules, with a warnings column and the extra checks named in it) printed, on the final run:

```
module                              errors  warnings satisfied  failed  refused  expected
g4-composition.l4                        0         0         0       0        0         0
g4-conflict.l4                           0         0         0       0        0         0
g4-council-membership.l4                 0         0         0       0        0         0
g4-council-work.l4                       0         0         0       0        0         0
g4-registrar.l4                          0         0         0       0        0         0
g4-tests-composition.l4                  0         0        49       0        0         0
g4-tests-conflict.l4                     0         0        59       0        0         0
g4-tests-council-work.l4                 0         0       115       0        0         0
g4-tests-membership.l4                   0         0       157       0        0         0
g4-tests-red.l4                         17         0         0      17        0        17
g4-tests-registrar.l4                    0         0        39       0        0         0
TOTAL (11 modules)                      17         0       419      17        0
(a failed assertion is also an error; any other error, any warning or any refused assertion makes the run red)

extra checks
  all g4 modules start with '@lang en' and have ASCII file names
  time module sha256 matches
  l4 check: no stray @ref warnings, no warnings
  srcrefs: srcrefs check: 205 src: lines, 81 runs, 142 locators, 0 problems 
  check-hebrew: ok 
  gazette: wiki words of ss.19-29 missing from the gazette: none
  g4-tests-composition.l4: trace-expect: 0 traces, 0 as expected, 0 not
  g4-tests-conflict.l4: trace-expect: 21 traces, 21 as expected, 0 not
  g4-tests-council-work.l4: trace-expect: 22 traces, 22 as expected, 0 not
  g4-tests-membership.l4: trace-expect: 32 traces, 32 as expected, 0 not
  g4-tests-registrar.l4: trace-expect: 17 traces, 17 as expected, 0 not
```

- The 17 failed assertions are all in `g4-tests-red.l4`, each a rejected reading's answer asserted against the reading taken (section 2, "Red n"); `check.sh` lists the count (`expected_failed` 17).
- No assertion refused and none could not be evaluated. No module emits a warning.
- **Mutation check.** `work/g4/mutate.py` applies one textual mutation at a time to a copy of the modules and runs the tests: 27 mutations (the majority threshold, the chair's presence, the casting vote, the four-year term, the half-and-more-than-half edge, the window edge, three consecutive absences, the s.21 pending limb, the engineer exclusion, advice validity, s.27(b), relative category (4), s.29(e), s.29(b)'s conjunction, four in the composition, and six on the traces) were each caught by at least one assertion or trace; a no-op control was not caught.
- **Re-read of every number against the Hebrew.** Done, after encoding and before the final run, against `law.wiki` lines 159 to 242 and the gazette page images: 11 members and eleven items (s.20); the proposals in items (4) to (6); seats (7) to (11) as the ones s.29(e) names; four years (s.22); three consecutive meetings, more than half of the meetings, one year (s.23(c)); a majority including the chair (ss.24 and 25(a)); the four matters of s.19(c)(2); the six enactments of s.28; the thirteen relations of `Kinship to a member of the Council` (twelve listed, one for the rest) against the definition in s.29(a). The numbers that are mine, not the Law's (10 meetings with 6 absences, 8 serving members, and so on), are scenario sizes chosen on both sides of the Law's thresholds; the dates were computed with Python's calendar (`expectations.md`, written before any module).
- **Hebrew.** Only the `-- src:N |` lines are generated. The Hebrew in other comments and in this file was typed while reading the Law and then verified by `check-hebrew.py` as verbatim slices (five spans were wrong when first typed, an ellipsis and a mis-ordered phrase among them, and were fixed); it was not typed from memory, but it is not script-generated either.
- **Expectation slips found while running.** Two of my own expectations in `g4-tests-membership.l4` were wrong when first written and were corrected by deriving the answer from the Hebrew again, not from the module's output: a list of two absences in two meetings is a majority (2 of 2), so it is not a "no ground" case; and under "some one year" a window starting later than the first meeting can hold a majority (the window from 2025-11-01 holds seven meetings of which four were missed), so the alternative answers yes where the reading taken answers no. Neither was a defect in a module.
- **Peeked:** nothing. No file outside `inputs/`, `phase1/`, `deposit/` (the files named in the assignment), `work/g4/`, the two skills and the `doc/` tree was opened.
