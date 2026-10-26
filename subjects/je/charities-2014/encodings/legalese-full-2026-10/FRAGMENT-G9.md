# FRAGMENT-G9: Schedules 1 and 2 (the Jersey Charity Commissioner and the Charity Tribunal)

Status: written by ENCODER G9 of the fleet that encodes the Charities (Jersey) Law 2014; draft; not reviewed by a domain expert against the Law.
Scope: Schedule 1 (paragraphs 1 to 4) and Schedule 2 (paragraphs 1 to 4), src:754 to src:861 of `charities-jersey-law-2014-2026-10-02.txt`.
Every statement below was checked against the modules and the check script's output printed in section 9; nothing here describes a planned state.

## 0. What was written

| file | what it holds |
| --- | --- |
| `g9-interpretation.l4` | the eighteen fork enumerations (F9.13 uses `Unit of a term of imprisonment` from `domain.l4`), the record `Interpretation of Schedules 1 and 2` (one field per fork, each `TYPICALLY` the favoured reading), `the favoured interpretation` and twenty named variants |
| `g9-common.l4` | what the two Schedules share: the counting of every period under each reading (one public decision per period, delegating by `CONSIDER` to one function per reading), the periods of service, and the Dormant Bank Accounts words by vintage. No Schedule's figure is in it |
| `g9-sched1-commissioner.l4` | Schedule 1 paragraphs 1 to 4 |
| `g9-sched2-tribunal.l4` | Schedule 2 paragraphs 1 to 4 |
| `g9-tests-periods.l4` | the counting in `g9-common.l4`, both sides of every threshold, every reading called directly |
| `g9-tests-sched1.l4`, `g9-tests-sched2.l4` | the Schedules, with 65 and 66 `#TRACE`s whose outcomes are written in `-- EXPECT:` comments |
| `g9-tests-t20.l4` | trap T20: the two Schedules' figures side by side, and a proof that both modules import together |
| `g9-tests-red.l4` | 19 assertions that are meant to fail, one per fork |

Changes from the PLAN's section (b): the PLAN named two modules; the nineteen forks share one record and the counting is shared, so two modules were added, `g9-interpretation.l4` and `g9-common.l4`.
The types the PLAN lists as group-local are `Appointment of the Commissioner`, `Appointment of a member of the tribunal`, `Period of service under the Schedules`, `Report of the Commissioner on a calendar year`, `Report on the tribunal for a calendar year`, `Act under Schedule 1` and `Act under Schedule 2` (renamed so that no name can collide across the fleet).
The PLAN listed forks F9.1 to F9.13; six were added, F9.14 to F9.19 (section 2).
Every helper and every act carries a prefix (`Sch 1 and 2: `, `Sch 1: `, `Sch 2: `) or an `F9.n` marker so that its name is unique in the fleet.
The scripts that wrote `g9-interpretation.l4` and the coverage table, and an independent calendar oracle in Python, are encoder scratch in `work/g9/` and are not part of the deposit.

Method notes a reviewer should know.
1. Quotations are copied by `srcrefs.py quote`; the `@@INERT` text of each inert provision is the quoted text of its lines, never retyped.
2. The PDF text layer was compared with the consolidated text over src:754 to src:861 as a token sequence (case, hyphenation at line ends and quote marks normalised): the only differences are the PDF's six page footers.
   Nothing in Schedules 1 and 2 differs between the two, so no fork rests on a difference between them.
3. A deadline written `BEFORE d` is met on `d` itself.
   Measured with a probe on this binary: a notice presented on 1 March 2026 against `BEFORE (15 March 2026 minus 14 days)` is fulfilled; one presented on 2 March is breached.
   That is what makes reading A of F9.1 "14 days" and reading B "15".
4. A day is a calendar date.
   Where a date field ends a period it denotes the first day on which the person is no longer appointed, unless the field says it is a last day (F9.2 reading B).
5. Duties are typed `MUST`/`SHANT`, powers `MAY`, by the role that acts (`Legal actor`) and by what is done (`Act under Schedule 1`, `Act under Schedule 2`); the Minister's opinions and satisfactions, the Commissioner's authorizations and every determination "that all reasonable steps were taken" are inputs.
6. A `MAY` whose precondition fails is written `PROVIDED precondition`: an act without the precondition is not that act, the permission stays open, and the trace is STANDING; a duty whose trigger has not occurred is `IF trigger THEN MUST ... ELSE FULFILLED`.

## 1. Coverage

103 rows, one per provision of the scope in the Law's numbering: **80 encoded, 22 inert, 1 refused, 0 out-of-scope, 0 deferred**.
The PLAN proposed 83 encoded and 20 inert.
Four dispositions changed, and each row says why:
- `Sch 1` and `Sch 2` (the headings): encoded to inert.
  A heading is not operative; the heading of Schedule 2 names the body Article 32 calls the Charity Tribunal (trap T20).
- `Sch1 2(4)` (the chapeau "Despite sub-paragraphs (2) and (3)"): encoded to inert.
  It overrides only 2(2) and 2(3), which are inert and compute nothing; its two limbs, 2(4)(a) and (b), are encoded.
- `Sch2 4(3)(e)`: inert to refused.
  The quorum and voting rules a sitting needs are for Regulations that are not in the sources, so a question for the quorum is a named refusal; the matter is also carried as inert text.

One reason in the PLAN is not carried: the row for `Sch1 2(1)(d)` said the Law creates no offence the Commissioner could commit.
Article 29(1) (src:664 to src:667) reaches "a person who receives information ... under or for the purposes of this Law", which on its words includes the Commissioner.
The row stays inert, for the reason in the table.
A paragraph's own row (`Sch1 1`, `Sch1 2`, `Sch1 3`, `Sch1 4`, `Sch2 1` to `Sch2 4`) is carried by its `§§` heading; its operative rules are those of the sub-paragraphs under it, and the row names the first of them.
Every rule named below was checked mechanically to be defined in the module named (`work/g9/gen/coverage.py` exits 0 with "missing 0").
Inert provisions are definitions of the form `` `Sch 1 para 1(4) the terms of the appointment (inert)` MEANS "..." `` with the quoted words, an `@ref` and, in a comment above, the reason.

| id | provision | disposition | module | rules | note |
| --- | --- | --- | --- | --- | --- |
| Sch 1 | Schedule 1 (heading, Article 3, endnote [5]) | inert | g9-sched1-commissioner | `Sch 1 the heading Jersey Charity Commissioner (inert)` | PLAN: encoded. Changed: the heading is not operative; the L.1/2017 words it points to are encoded where they occur (2(4)(a), 4(7)). |
| Sch1 1 | paragraph 1 Appointment of Commissioner | encoded | g9-sched1-commissioner | `Sch 1 para 1(1) the Minister must appoint a person appearing to the Minister to be suitable` | §§ heading `1 Appointment of Commissioner`; the rules are those of 1(1) to 1(7). |
| Sch1 1(1) | 1(1) | encoded | g9-sched1-commissioner | `Sch 1 para 1(1) the Minister must appoint a person appearing to the Minister to be suitable` | suitability is an input; the Law states no trigger or deadline (see section 8) |
| Sch1 1(2) | 1(2) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 1(2) before appointing a person the Minister must seek the views of the Jersey Appointments Commission` ; `Sch 1 para 1(2) the views of the Jersey Appointments Commission were sought before the appointment` ; `Sch 1 and 2: the latest day for the views of the Jersey Appointments Commission to be sought` | fork F9.14 |
| Sch1 1(3) | 1(3) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 1(3) at least 2 weeks before appointing the Minister must present to the States a notice of intention` ; `Sch 1 para 1(3) the notice of intention was presented to the States in time` ; `Sch 1 para 1(3) the notice of intention must be presented at least this many weeks before appointing` ; `Sch 1 and 2: the latest day for a notice of intention before an appointment` | period P29, fork F9.1 |
| Sch1 1(4) | 1(4) | inert | g9-sched1-commissioner | `Sch 1 para 1(4) the terms of the appointment (inert)` | restates the terms of appointment; no rule of its own |
| Sch1 1(5) | 1(5) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 1(5) when appointing the Minister must determine the period of the appointment, being not more than 6 years` ; `Sch 1 para 1(5) the period of the appointment is within the limit` ; `Sch 1 para 1(5) the period of the appointment is not more than this many years` ; `Sch 1 and 2: the latest end date of a term of an appointment` | period P30, fork F9.2 |
| Sch1 1(6) | 1(6) | encoded | g9-sched1-commissioner | `Sch 1 para 1(6) the Minister may re-appoint a person serving as the Commissioner` | power typed MAY; the extension of 1(2), (3), (5) to re-appointment is tested (a re-appointment is an `Appointment of the Commissioner` with `the person was serving ...` TRUE) |
| Sch1 1(7) | 1(7) | encoded | g9-sched1-commissioner | `Sch 1 para 1(7) the Minister must take all reasonable steps to ensure that at all times the office of the Commissioner is filled` ; `Sch 1 para 1(7) the Minister has complied with the duty to keep the office filled` | all reasonable steps is an input |
| Sch1 1(8) | 1(8) | inert | g9-sched1-commissioner | `Sch 1 para 1(8) part-time terms of appointment (inert)` | clarifies how 1(7) is read; no rule of its own |
| Sch1 2 | paragraph 2 Status of Commissioner | encoded | g9-sched1-commissioner | `Sch 1 para 2(4)(a) the remuneration of the Commissioner must be paid out of the annual income of the States` | §§ heading `2 Status of Commissioner`; the operative rules are 2(4)(a) and (b) |
| Sch1 2(1) | 2(1) | inert | g9-sched1-commissioner | `Sch 1 para 2(1) the Commissioner as a corporation sole (inert)` | capacities of a corporation sole, no precondition or outcome |
| Sch1 2(1)(a) | 2(1)(a) | inert | g9-sched1-commissioner | `Sch 1 para 2(1)(a) enter into an agreement (inert)` | capacity to contract for any purpose of the office |
| Sch1 2(1)(b) | 2(1)(b) | inert | g9-sched1-commissioner | `Sch 1 para 2(1)(b) acquire, hold and dispose of movable property (inert)` | capacity to hold movable property |
| Sch1 2(1)(c) | 2(1)(c) | inert | g9-sched1-commissioner | `Sch 1 para 2(1)(c) sue and be sued in civil proceedings (inert)` | capacity to sue and be sued |
| Sch1 2(1)(d) | 2(1)(d) | inert | g9-sched1-commissioner | `Sch 1 para 2(1)(d) be charged with an offence and defend criminal proceedings (inert)` | capacity to be charged with an offence; the PLAN's reason (the Law creates no offence the Commissioner could commit) is not carried: Article 29(1) reaches any person who receives information under the Law, on its words the Commissioner too |
| Sch1 2(1)(e) | 2(1)(e) | inert | g9-sched1-commissioner | `Sch 1 para 2(1)(e) do anything reasonably necessary or expedient for the Commissioner's functions (inert)` | overlaps Article 4(2), which is G2's |
| Sch1 2(2) | 2(2) | inert | g9-sched1-commissioner | `Sch 1 para 2(2) the Commissioner is independent of the States and the Minister (inert)` | status; its operative echo is the limit in 4(12), which is encoded |
| Sch1 2(3) | 2(3) | inert | g9-sched1-commissioner | `Sch 1 para 2(3) the terms of appointment create no contract of employment or agency (inert)` | employment law is outside the sources |
| Sch1 2(4) | 2(4) | inert | g9-sched1-commissioner | `Sch 1 para 2(4) despite sub-paragraphs (2) and (3) (chapeau, inert)` | PLAN: encoded. Changed: the chapeau overrides only 2(2) and 2(3), which are inert and compute nothing, so it is carried as text and its two limbs are encoded |
| Sch1 2(4)(a) | 2(4)(a) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 2(4)(a) the remuneration of the Commissioner must be paid out of the annual income of the States` ; `Sch 1 and 2: the Dormant Bank Accounts words are in the text of` | vintage-dependent (trap T22), fork F9.9 |
| Sch1 2(4)(b) | 2(4)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 2(4)(b) all fees and other sums received by the Commissioner must be paid to the income of the States` | the payer is not named; the Commissioner, who receives the sums, is read as the party; no deadline; not subject to the Dormant Bank Accounts Law |
| Sch1 3 | paragraph 3 Termination of office as Commissioner | encoded | g9-sched1-commissioner | `Sch 1 para 3(1) the person has ceased to be appointed as the Commissioner by the day` | §§ heading `3 Termination of office as Commissioner` |
| Sch1 3(1) | 3(1) | encoded | g9-sched1-commissioner | `Sch 1 para 3(1) the person has ceased to be appointed as the Commissioner by the day` ; `Sch 1 para 3(1) a person ceases to be appointed as the Commissioner in these three cases (chapeau, inert)` |  |
| Sch1 3(1)(a) | 3(1)(a) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 3(1)(a) the day the office ends by resignation` ; `Sch 1 para 3(1)(a) the Commissioner may resign from office by giving not less than 3 months' notice in writing to the Minister` ; `Sch 1 para 3(1)(a) the person has resigned by the day` ; `Sch 1 para 3(1)(a) the notice of resignation must be for not less than this many months` ; `Sch 1 and 2: the day the office ends by resignation` | period P31, fork F9.3; 3 months (Schedule 2: one month, trap T20) |
| Sch1 3(1)(b) | 3(1)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 3(1)(b) the Minister has terminated the appointment by the day` | ends the office only if the Minister could terminate on the grounds (3(2)) |
| Sch1 3(1)(c) | 3(1)(c) | encoded | g9-sched1-commissioner | `Sch 1 para 3(4) the appointment has expired by the day` | combined in 3(1) |
| Sch1 3(2) | 3(2) | encoded | g9-sched1-commissioner | `Sch 1 para 3(2) the Minister may terminate the appointment of a person as the Commissioner` ; `Sch 1 para 3(2) the Minister has satisfied himself or herself on a ground for terminating` ; `Sch 1 para 3(2) the Minister may terminate the appointment after satisfying himself or herself on one of four grounds (chapeau, inert)` | power typed MAY with the grounds as the guard |
| Sch1 3(2)(a) | 3(2)(a) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 3(2)(a) the person has been absent from duties for a period longer than 4 consecutive weeks` ; `Sch 1 para 3(2)(a) the Minister has satisfied himself or herself that the person has been absent for a period longer than 4 consecutive weeks` ; `Sch 1 para 3(2)(a) the absence must be for a period longer than this many consecutive weeks` ; `Sch 1 and 2: an absence from duties was for a period longer than that many consecutive weeks` | period P32, forks F9.4 and F9.19; 4 weeks (Schedule 2: 8 weeks, trap T20) |
| Sch1 3(2)(b) | 3(2)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 3(2)(b) the Minister has satisfied himself or herself that the person has become bankrupt` | the Minister's satisfaction is an input |
| Sch1 3(2)(c) | 3(2)(c) | encoded | g9-sched1-commissioner | `Sch 1 para 3(2)(c) the Minister has satisfied himself or herself that the person is incapacitated by illness` | the Minister's satisfaction is an input |
| Sch1 3(2)(d) | 3(2)(d) | encoded | g9-sched1-commissioner | `Sch 1 para 3(2)(d) the Minister has satisfied himself or herself that the person is otherwise unable or unfit to discharge the functions of the Commissioner` | the Minister's satisfaction is an input |
| Sch1 3(3) | 3(3) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 3(3) not more than 2 weeks after terminating the appointment the Minister must present to the States a notice that the Minister has terminated it` ; `Sch 1 para 3(3) the notice of the termination was presented to the States in time` ; `Sch 1 para 3(3) the notice of the termination must be presented not more than this many weeks after terminating` ; `Sch 1 and 2: the latest day for a notice of a termination` | period P33, fork F9.5 |
| Sch1 3(4) | 3(4) | encoded | g9-sched1-commissioner | `Sch 1 para 3(4) the day on which the appointment expires` ; `Sch 1 para 3(4) the appointment has expired by the day` ; `Sch 1 para 3(4) a person's appointment as the Commissioner expires in these three cases (chapeau, inert)` | the earliest of (a), (b) and (c) |
| Sch1 3(4)(a) | 3(4)(a) | encoded | g9-sched1-commissioner | `Sch 1 para 3(4)(a) the day the period of the appointment expires without re-appointment` | a term followed by a re-appointment does not expire under (a) |
| Sch1 3(4)(b) | 3(4)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 3(4)(b) the day the person becomes a member of the States` | fork F9.17 |
| Sch1 3(4)(c) | 3(4)(c) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 3(4)(c) the day the person completes 12 years of service as the Commissioner` ; `Sch 1 and 2: the day on which twelve years of service are completed` | period P34, forks F9.6 and F9.11; the mid-term cut-off (trap T21) is tested |
| Sch1 4 | paragraph 4 Staff, resources and reporting | encoded | g9-sched1-commissioner | `Sch 1 para 4(5) someone is treated as the Commissioner` | §§ heading `4 Staff, resources and reporting` |
| Sch1 4(1) | 4(1) | encoded | g9-sched1-commissioner | `Sch 1 para 4(1) the Minister must make available to the Commissioner such number and descriptions of staff as the Minister considers are required` ; `Sch 1 para 4(1) the Minister has made available the number and descriptions of staff that the Minister considers are required` | the Minister's consideration is an input |
| Sch1 4(2) | 4(2) | encoded | g9-sched1-commissioner | `Sch 1 para 4(2) the employee is to be treated as a member of the Commissioner's staff for the function` |  |
| Sch1 4(3) | 4(3) | encoded | g9-sched1-commissioner | `Sch 1 para 4(3) a member of the Commissioner's staff may exercise the function on behalf of the Commissioner` ; `Sch 1 para 4(3) the decision is one that a member of the Commissioner's staff may not make on behalf of the Commissioner` | IP27; forks F9.8 and F9.16; trap T17 |
| Sch1 4(3)(a) | 4(3)(a) | encoded | g9-sched1-commissioner | `Sch 1 para 4(3)(a) the decision is the decision under Article 11 on whether to register a charity` |  |
| Sch1 4(3)(b) | 4(3)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 4(3)(b) the decision is the decision under Article 15(3) on whether to refuse to deregister a charity` | fork F9.8 |
| Sch1 4(3)(c) | 4(3)(c) | encoded | g9-sched1-commissioner | `Sch 1 para 4(3)(c) the decision is the decision under Article 16 on whether to deregister a charity` | includes the mandatory Article 16(2) |
| Sch1 4(4) | 4(4) | encoded | g9-sched1-commissioner | `Sch 1 para 4(4) the Minister may designate a person as the relevant person for the purpose of sub-paragraph (5)` | power typed MAY |
| Sch1 4(5) | 4(5) | encoded | g9-sched1-commissioner | `Sch 1 para 4(5) someone is treated as the Commissioner` ; `Sch 1 para 4(5) the relevant person is treated as the Commissioner` | IP28 (exported); the Law sets no limit on how long the temporary basis lasts |
| Sch1 4(5)(a) | 4(5)(a) | encoded | g9-sched1-commissioner | `Sch 1 para 4(5)(a) the person appointed as the Commissioner is unable to act through incapacity or absence` |  |
| Sch1 4(5)(b) | 4(5)(b) | encoded | g9-sched1-commissioner | `Sch 1 para 4(5)(b) there is a vacancy in the office of Commissioner` |  |
| Sch1 4(6) | 4(6) | encoded | g9-sched1-commissioner | `Sch 1 para 4(6) the Minister must provide such accommodation and equipment as the Minister considers are required` | the Minister's consideration is an input |
| Sch1 4(7) | 4(7) | encoded | g9-sched1-commissioner | `Sch 1 para 4(7) the cost of providing staff, accommodation and equipment must be met out of the annual income of the States` ; `F9.9: the cost must be met out of the annual income of the States` | vintage-dependent (trap T22), fork F9.9 |
| Sch1 4(8) | 4(8) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 4(8) the Commissioner must prepare and publish a report on the activities of the Commissioner in each calendar year` ; `Sch 1 para 4(8) the Commissioner has prepared and published the report` ; `Sch 1 and 2: a report is required of the holder for a calendar year` | period P35: "calendar year" is stated (trap T24); fork F9.12 |
| Sch1 4(9) | 4(9) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 4(9) the Commissioner must provide the Minister with the report as soon as practicable after the end of the year, and in no case later than 4 months after it` ; `Sch 1 para 4(9) the Commissioner provided the Minister with the report in time` ; `Sch 1 para 4(9) the last day for providing the Minister with the report` ; `Sch 1 para 4(9) the report must be provided in no case later than this many months after the end of the year` ; `Sch 1 and 2: the latest day for a report on a calendar year` ; `Sch 1 and 2: a step was taken as soon as practicable` | period P36, forks F9.7 and F9.10 |
| Sch1 4(10) | 4(10) | encoded | g9-common ; g9-sched1-commissioner | `Sch 1 para 4(10) the Minister must lay a copy of the report so provided before the States as soon as practicable after receiving it` ; `Sch 1 para 4(10) the Minister laid a copy of the report before the States as soon as practicable` ; `Sch 1 and 2: the last day for a step that is to be taken as soon as practicable` | period P37, fork F9.10 |
| Sch1 4(11) | 4(11) | encoded | g9-sched1-commissioner | `Sch 1 para 4(11) the Minister may, by giving written notice to the Commissioner and publishing that notice, give directions on the content and form of the report` | power typed MAY |
| Sch1 4(12) | 4(12) | encoded | g9-sched1-commissioner | `Sch 1 para 4(12) directions under sub-paragraph (11) must not require the report to contain justification of any decision of the Commissioner in relation to individual charities, governors or applicants for registration` ; `Sch 1 para 4(12) the directions are within the limit` | prohibition (SHANT) plus the limit as a BOOLEAN; "paragraph (11)" is read as sub-paragraph (11) |
| Sch 2 | Schedule 2 (heading, Article 32) | inert | g9-sched2-tribunal | `Sch 2 the heading Charity Commission tribunal (inert)` | PLAN: encoded. Changed: the heading is not operative; it names the body Article 32 calls the Charity Tribunal (trap T20) |
| Sch2 1 | paragraph 1 Appointment | encoded | g9-sched2-tribunal | `Sch 2 para 1(1) the number of members of the tribunal is within the limits` | §§ heading `1 Appointment` |
| Sch2 1(1) | 1(1) | encoded | g9-sched2-tribunal | `Sch 2 para 1(1) the number of members of the tribunal is within the limits` ; `Sch 2 para 1(1) the Minister must appoint at least 4 persons appearing to be suitable and to have appropriate experience as members of the tribunal` ; `Sch 2 para 1(1) the Minister must not appoint more than 8 members of the tribunal` | at least 4 (MUST) and no more than 8 (SHANT) |
| Sch2 1(2) | 1(2) | encoded | g9-sched2-tribunal | `Sch 2 para 1(2) before appointing a person as a tribunal member the Minister must seek the views of the Jersey Appointments Commission` ; `Sch 2 para 1(2) the views of the Jersey Appointments Commission were sought before the appointment` | fork F9.14 |
| Sch2 1(3) | 1(3) | encoded | g9-sched2-tribunal | `Sch 2 para 1(3) at least 2 weeks before appointing a person as a tribunal member the Minister must present to the States a notice of intention` ; `Sch 2 para 1(3) the notice of intention was presented to the States in time` ; `Sch 2 para 1(3) the notice of intention must be presented at least this many weeks before appointing` | period P38, fork F9.1 |
| Sch2 1(4) | 1(4) | inert | g9-sched2-tribunal | `Sch 2 para 1(4) the terms of the appointment (inert)` | restates the terms of appointment |
| Sch2 1(5) | 1(5) | encoded | g9-sched2-tribunal | `Sch 2 para 1(5) when appointing a person as a tribunal member the Minister must determine the period of the appointment, being not more than 6 years` ; `Sch 2 para 1(5) the period of the appointment is within the limit` ; `Sch 2 para 1(5) the period of the appointment is not more than this many years` | period P39, fork F9.2 |
| Sch2 1(6) | 1(6) | encoded | g9-sched2-tribunal | `Sch 2 para 1(6) the Minister may re-appoint a person serving as a tribunal member` | power typed MAY |
| Sch2 1(7) | 1(7) | encoded | g9-sched2-tribunal | `Sch 2 para 1(7) the Minister must designate one member as the chair and another as the vice-chair` ; `Sch 2 para 1(7) one member is designated as the chair and another as the vice-chair` |  |
| Sch2 1(8) | 1(8) | encoded | g9-sched2-tribunal | `Sch 2 para 1(8) service as a tribunal member is honorary` ; `Sch 2 para 1(8) the Minister may determine that the chair is, or all the members are, to be remunerated by the States` |  |
| Sch2 2 | paragraph 2 Termination of appointment | encoded | g9-sched2-tribunal | `Sch 2 para 2(1) the person has ceased to be a member of the tribunal by the day` | §§ heading `2 Termination of appointment` |
| Sch2 2(1) | 2(1) | encoded | g9-sched2-tribunal | `Sch 2 para 2(1) the person has ceased to be a member of the tribunal by the day` ; `Sch 2 para 2(1) a person ceases to be a member of the tribunal in these three cases (chapeau, inert)` |  |
| Sch2 2(1)(a) | 2(1)(a) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 2(1)(a) the day the position ends by resignation` ; `Sch 2 para 2(1)(a) a member may resign from office by giving not less than one month's notice in writing to the Minister` ; `Sch 2 para 2(1)(a) the person has resigned by the day` ; `Sch 2 para 2(1)(a) the notice of resignation must be for not less than this many months` ; `Sch 1 and 2: the day the office ends by resignation` | period P40, fork F9.3; one month (Schedule 1: 3 months, trap T20) |
| Sch2 2(1)(b) | 2(1)(b) | encoded | g9-sched2-tribunal | `Sch 2 para 2(1)(b) the Minister has terminated the appointment by the day` |  |
| Sch2 2(1)(c) | 2(1)(c) | encoded | g9-sched2-tribunal | `Sch 2 para 2(4) the appointment has expired by the day` | combined in 2(1) |
| Sch2 2(2) | 2(2) | encoded | g9-sched2-tribunal | `Sch 2 para 2(2) the Minister may terminate the appointment of a person as a member of the tribunal` ; `Sch 2 para 2(2) the Minister has satisfied himself or herself on a ground for terminating` ; `Sch 2 para 2(2) the Minister may terminate the appointment after satisfying himself or herself on one of four grounds (chapeau, inert)` | power typed MAY |
| Sch2 2(2)(a) | 2(2)(a) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 2(2)(a) the person has been absent from duties for a period longer than 8 consecutive weeks` ; `Sch 2 para 2(2)(a) the Minister has satisfied himself or herself that the person has been absent for a period longer than 8 consecutive weeks` ; `Sch 2 para 2(2)(a) the absence must be for a period longer than this many consecutive weeks` ; `Sch 1 and 2: an absence from duties was for a period longer than that many consecutive weeks` | period P41, forks F9.4 and F9.19; 8 weeks (Schedule 1: 4 weeks, trap T20) |
| Sch2 2(2)(b) | 2(2)(b) | encoded | g9-sched2-tribunal | `Sch 2 para 2(2)(b) the Minister has satisfied himself or herself that the person has become bankrupt` |  |
| Sch2 2(2)(c) | 2(2)(c) | encoded | g9-sched2-tribunal | `Sch 2 para 2(2)(c) the Minister has satisfied himself or herself that the person is incapacitated by illness` |  |
| Sch2 2(2)(d) | 2(2)(d) | encoded | g9-sched2-tribunal | `Sch 2 para 2(2)(d) the Minister has satisfied himself or herself that the person is otherwise unable or unfit to discharge the functions of a member of the tribunal` |  |
| Sch2 2(3) | 2(3) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 2(3) not more than 2 weeks after terminating the appointment the Minister must present to the States a notice that the Minister has terminated it` ; `Sch 2 para 2(3) the notice of the termination was presented to the States in time` ; `Sch 2 para 2(3) the notice of the termination must be presented not more than this many weeks after terminating` ; `Sch 1 and 2: the latest day for a notice of a termination` | period P42, fork F9.5 |
| Sch2 2(4) | 2(4) | encoded | g9-sched2-tribunal | `Sch 2 para 2(4) the day on which the appointment expires` ; `Sch 2 para 2(4) the appointment has expired by the day` ; `Sch 2 para 2(4) a person's appointment as a member of the tribunal expires in these three cases (chapeau, inert)` |  |
| Sch2 2(4)(a) | 2(4)(a) | encoded | g9-sched2-tribunal | `Sch 2 para 2(4)(a) the day the period of the appointment expires without re-appointment` |  |
| Sch2 2(4)(b) | 2(4)(b) | encoded | g9-sched2-tribunal | `Sch 2 para 2(4)(b) the day the person becomes a member of the States` | fork F9.17 |
| Sch2 2(4)(c) | 2(4)(c) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 2(4)(c) the day the person completes 12 years of service as a member of the tribunal` ; `Sch 1 and 2: the day on which twelve years of service are completed` | period P43, forks F9.6 and F9.11; trap T21 |
| Sch2 3 | paragraph 3 Staff, resources and reporting | encoded | g9-sched2-tribunal | `Sch 2 para 3(2) at least one member of staff is available to the tribunal as the responsible officer` | §§ heading `3 Staff, resources and reporting` |
| Sch2 3(1) | 3(1) | encoded | g9-sched2-tribunal | `Sch 2 para 3(1) the Minister must make available to the tribunal such number and descriptions of staff and resources as the Minister considers are required` ; `Sch 2 para 3(1) the Minister has made available the number and descriptions of staff and the resources that the Minister considers are required` | the Minister's consideration is an input |
| Sch2 3(2) | 3(2) | encoded | g9-sched2-tribunal | `Sch 2 para 3(2) the Minister must secure that at least one member of staff is available to the tribunal as the responsible officer` ; `Sch 2 para 3(2) at least one member of staff is available to the tribunal as the responsible officer` ; `Sch 2 para 3(2) the responsible officer is charged with assisting with the matter` ; `Sch 2 para 3(2) the members of staff who are the responsible officer` | fork F9.18; assisting with administration but not determinations is tested |
| Sch2 3(3) | 3(3) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 3(3) the responsible officer must prepare a report on the activities of the tribunal in each calendar year` ; `Sch 1 and 2: a report is required of the holder for a calendar year` | period P44, fork F9.12 |
| Sch2 3(4) | 3(4) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 3(4) the responsible officer must provide the Minister with the report as soon as practicable after the end of the year, and in no case later than 4 months after it` ; `Sch 2 para 3(4) the responsible officer provided the Minister with the report in time` ; `Sch 2 para 3(4) the last day for providing the Minister with the report` ; `Sch 2 para 3(4) the report must be provided in no case later than this many months after the end of the year` ; `Sch 1 and 2: the latest day for a report on a calendar year` ; `Sch 1 and 2: a step was taken as soon as practicable` | period P44, forks F9.7 and F9.10 |
| Sch2 3(5) | 3(5) | encoded | g9-common ; g9-sched2-tribunal | `Sch 2 para 3(5) the Minister must lay a copy of the report so provided before the States as soon as practicable after receiving it` ; `Sch 2 para 3(5) the Minister laid a copy of the report before the States as soon as practicable` ; `Sch 1 and 2: the last day for a step that is to be taken as soon as practicable` | period P44, fork F9.10 |
| Sch2 4 | paragraph 4 Procedure of tribunal | encoded | g9-sched2-tribunal | `Sch 2 para 4(1) the person presiding over a sitting` | §§ heading `4 Procedure of tribunal` |
| Sch2 4(1) | 4(1) | encoded | g9-sched2-tribunal | `Sch 2 para 4(1) the person presiding over a sitting` ; `Sch 2 para 4(1) the office-holder is absent for the purposes of paragraph 4(1)` | fork F9.15 |
| Sch2 4(1)(a) | 4(1)(a) | encoded | g9-sched2-tribunal | `Sch 2 para 4(1)(a) the chair presides` |  |
| Sch2 4(1)(b) | 4(1)(b) | encoded | g9-sched2-tribunal | `Sch 2 para 4(1)(b) the vice-chair presides, the chair being absent` |  |
| Sch2 4(1)(c) | 4(1)(c) | encoded | g9-sched2-tribunal | `Sch 2 para 4(1)(c) a member appointed by the members present presides, both the chair and the vice-chair being absent` |  |
| Sch2 4(2) | 4(2) | encoded | g9-sched2-tribunal | `Sch 2 para 4(2) subject to sub-paragraph (1) and to any Regulations under sub-paragraph (3) the tribunal may regulate its own procedure` ; `Sch 2 para 4(2) the tribunal may regulate the matter by its own procedure` | power typed MAY (the tribunal); the Regulations are an input |
| Sch2 4(3) | 4(3) | encoded | g9-sched2-tribunal | `Sch 2 para 4(3) the States may by Regulations make further provision as to the procedure of the tribunal` | power typed MAY (the States); the Regulations are not in the sources |
| Sch2 4(3)(a) | 4(3)(a) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(a) the burden of proof on an appeal (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(b) | 4(3)(b) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(b) the summoning of witnesses and the administration of oaths (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(c) | 4(3)(c) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(c) securing the production of documents and evidence (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(d) | 4(3)(d) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(d) the conduct of hearings and the determination of appeals (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(e) | 4(3)(e) | refused | g9-sched2-tribunal | `Sch 2 para 4 the quorum of the tribunal is not stated in the Law` ; `Sch 2 para 4(3)(e) determination of an appeal by the chair or vice-chair, and quorum and voting rules (inert)` | PLAN: inert. Changed: the quorum and voting rules a sitting needs are for Regulations that are not in the sources, so a question for the quorum is a named refusal; the matter is also carried as inert text |
| Sch2 4(3)(f) | 4(3)(f) | encoded | g9-sched2-tribunal | `Sch 2 para 4(3)(f) the penalty is within the cap` ; `Sch 2 para 4(3)(f) the States may by Regulations provide for costs and create offences in relation to the tribunal with a penalty not exceeding imprisonment for 2 years and a fine` ; `Sch 2 para 4(3)(f) the penalty may not exceed imprisonment for this many months` ; `Sch 2 para 4(3)(f) the penalty may not exceed imprisonment for this many days` | period P45, fork F9.13 (IP35) |
| Sch2 4(3)(g) | 4(3)(g) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(g) the publication of reports of the tribunal's decisions (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(h) | 4(3)(h) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(h) duties of the Commissioner in relation to an appeal (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(i) | 4(3)(i) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(i) striking out, withdrawal and amendment of appeals or replies (inert)` | subject matter the Regulations may cover |
| Sch2 4(3)(j) | 4(3)(j) | inert | g9-sched2-tribunal | `Sch 2 para 4(3)(j) such ancillary powers of the tribunal as the States think necessary (inert)` | subject matter the Regulations may cover |

## 2. Fork register

One record carries every fork: `Interpretation of Schedules 1 and 2` (in `g9-interpretation.l4`), nineteen fields, one per fork, each typed by its own enumeration with one constructor per reading and each `TYPICALLY` reading A.
Every public decision that depends on a fork takes the record as an ordinary `GIVEN` (`interp`) and delegates by `CONSIDER` to one function per reading; every such function is named `F9.n reading A: ...`, `F9.n reading B: ...` (and `C` for F9.3) and is called directly, by name, in a test (checked mechanically: of the 45 definitions whose name begins `F9.`, 44 are reading functions called by name in a test module; the 45th, `F9.9: the cost must be met out of the annual income of the States`, is the wrapper shared by 2(4)(a) and 4(7) that every F9.9 test reaches through the public rules).
The favoured interpretation, and a variant that reads exactly one fork as B (or C), are named values in `g9-interpretation.l4` (`` `the favoured interpretation, but F9.n is read as B` ``).
`g9-tests-red.l4` asserts the discriminating case of every fork with the answer of the other reading against the favoured interpretation, so its 19 assertions fail by design (section 9).
In the tests, "B of F9.n" is the variant that differs from the favoured interpretation at F9.n only.

Where the consolidated text and the PDF text layer differ: they do not, anywhere in Schedules 1 and 2 (method note 2), so no fork records such a difference.
The Interpretation (Jersey) Law 1954 is not among the sources; none of the counting readings below can be settled by it (section 8).

### Kinds of period met, and the fork that carries each

| period | words | kind | fork |
| --- | --- | --- | --- |
| P29, P38 | "at least 2 weeks before appointing" (Sch 1 1(3), Sch 2 1(3)) | minimum notice before an event | F9.1 |
| (new) | "Before appointing ... seek the views" (Sch 1 1(2), Sch 2 1(2)) | sequence at day grain | F9.14 |
| P30, P39 | "being not more than 6 years" (Sch 1 1(5), Sch 2 1(5)) | term of office | F9.2 |
| P31, P40 | "not less than 3 months' notice" / "one month's notice" (Sch 1 3(1)(a), Sch 2 2(1)(a)) | minimum notice | F9.3 |
| P32, P41 | "longer than 4 consecutive weeks" / "8 consecutive weeks" (Sch 1 3(2)(a), Sch 2 2(2)(a)) | duration threshold | F9.4 (and F9.19) |
| P33, P42 | "not more than 2 weeks after terminating" (Sch 1 3(3), Sch 2 2(3)) | deadline after an event | F9.5 |
| P34, P43 | "completes 12 years (whether consecutive or in aggregate)" (Sch 1 3(4)(c), Sch 2 2(4)(c)) | cap on service | F9.6, F9.11 |
| P35, P44 | "a report ... in each calendar year" (Sch 1 4(8), Sch 2 3(3)) | reporting period; "calendar year" is stated, not a fork (trap T24) | F9.12 (part-year) |
| P36, P44 | "in no case later than 4 months after the end of that year" (Sch 1 4(9), Sch 2 3(4)) | deadline after the end of a year | F9.7 |
| P37, P44 | "as soon as practicable" (Sch 1 4(9), (10), Sch 2 3(4), (5)) | standard of promptness | F9.10 |
| P45 | "a penalty not exceeding imprisonment for a term of 2 years and a fine" (Sch 2 4(3)(f)) | sentence cap on Regulations | F9.13 |

### The nineteen forks

#### F9.1 "at least 2 weeks before appointing" (Sch 1 1(3), src:760; Sch 2 1(3), src:818; P29, P38)
- Readings and the text that licenses each.
  - A (taken): the appointment day is 14 or more days after the day the notice was presented (the notice day is day 0).
    Licence: "at least 2 weeks before appointing"; a week is 7 days.
  - B: there are 14 clear days between the two days, so the appointment is 15 or more days after the notice.
    Licence: none in the text.
    The Law uses "clear days" nowhere (a search of the whole consolidated text finds none); the reading is the usual caution of a drafter who wants to exclude both end days.
- Taken, and why: A takes the words at their face; B adds a requirement ("clear") that the Law does not state.
- Carried by: field `the 2 weeks before an appointment`; constructors `the appointment is 14 or more days after the notice` (A), `there are 14 clear days between the notice and the appointment` (B).
  Functions `F9.1 reading A: the latest day for a notice that must precede an event by that many weeks`, `F9.1 reading B: ...` (`g9-common.l4`).
- Discriminating case: appointment on 15 March 2026, notice on 1 March 2026.
  A: in time (latest day 1 March).
  B: late (latest day 28 February).
- Tests: `g9-tests-periods.l4` § F9.1 and the reading functions; `g9-tests-sched1.l4` §§ 1(3) (the BOOLEAN and six traces, including the deadline day itself on both readings); `g9-tests-sched2.l4` §§ 1(3); the case is also asserted red in `g9-tests-red.l4`.

#### F9.2 "being not more than 6 years" (Sch 1 1(5), src:762; Sch 2 1(5), src:820; P30, P39)
- Readings.
  - A (taken): the field `the day the term expires` is the end date of the period, the first day on which the person is no longer appointed (3(4)(a), src:790: "the period for which the person was appointed expires"); a period may therefore run to the sixth anniversary of its first day.
    The latest end date is `add years` first day 6.
  - B: the end date is the last day of the term and is itself a day of the term, so the end date must be before the sixth anniversary (the latest is the day before it).
  - An anniversary of 29 February is 28 February (daydate `add years` clamps); the day before it is 27 February.
- Taken, and why: the Law calls the end of a fixed period its expiry; an appointment "for 6 years from 1 March 2026" expires on 1 March 2032.
  B is the same arithmetic on the other meaning of the end date.
- Carried by: field `the 6 years of an appointment`; constructors `the end date is the day the term expires` (A), `the end date is the last day of the term` (B).
  Functions `F9.2 reading A: the latest end date of a term is the anniversary of its start`, `F9.2 reading B: ...`.
- Discriminating case: a term from 1 March 2026 expiring 1 March 2032.
  A: within the limit.
  B: over it (the latest end date is 29 February 2032, 2032 being a leap year).
- Tests: `g9-tests-periods.l4` § F9.2 (including 29 February 2028); `g9-tests-sched1.l4` §§ 1(5) (BOOLEAN, re-appointment for another 6 years, three traces); `g9-tests-sched2.l4` §§ 1(5); red.

#### F9.3 "resigns ... by giving not less than 3 months' notice in writing to the Minister" (Sch 1 3(1)(a), src:780) and "one month's notice" (Sch 2 2(1)(a), src:826; P31, P40)
- Readings.
  - A (taken): the office ends when the notice period runs out; a notice names the day the resignation takes effect, which must be at least the notice day plus the months, the day clamped to the end of the month (30 November plus 3 months is 28 February).
  - B: the office ends on the day the notice is given (the notice must still be for the months, counted as in A).
    Licence: "ceases to be appointed ... if he or she resigns ... by giving ... notice": ceasing is tied to the act of resigning, which is the giving of the notice.
  - C: as A, but the months are added by rolling: 30 February does not exist, so it is 2 March.
- Taken, and why: A is the ordinary notion of notice (the person serves out the notice); a notice that took effect on the day it was given would not be a notice period at all.
  C is the rolling arithmetic of the lenient `Date` constructor and the Law is silent on it.
- Carried by: field `a resignation on notice`; constructors `the office ends when the notice period runs out, the months being clamped` (A), `the office ends when the notice is given` (B), `the office ends when the notice period runs out, the months being rolled` (C).
  Functions: `F9.3 reading A/B/C: the earliest day ...` (the longest allowed notice) and `F9.3 reading A/B/C: the office ends ...` (where the office ends).
- Discriminating case: notice given on 30 November 2026, naming 28 February 2027.
  A: a valid resignation ending the office on 28 February 2027.
  B: ends on 30 November 2026.
  C: not a valid resignation (the earliest day is 2 March 2027).
  Schedule 2, one month, notice on 31 January 2026: A earliest 28 February, C 3 March.
- Tests: `g9-tests-periods.l4` § F9.3 and "F9.3: where the office ends"; `g9-tests-sched1.l4` §§ 3(1)(a) and 3(1); `g9-tests-sched2.l4` §§ 2(1)(a) and 2(1); red.

#### F9.4 "absent ... for a period longer than 4 consecutive weeks" (Sch 1 3(2)(a), src:784) and "8 consecutive weeks" (Sch 2 2(2)(a), src:830; P32, P41)
- Readings.
  - A (taken): the days of absence are counted with the first and the last day both included, and compared with 7 times the weeks.
    Absent from 1 to 29 March 2026 is 29 days.
  - B: the elapsed days, the last day minus the first, are compared with 7 times the weeks.
    The same absence is 28 days.
- Taken, and why: a person absent on each of 29 days was absent for 29 days; the Law says "longer than", which is strict, and A applies it to the number of days of absence.
- Carried by: field `an absence from duties`; constructors `the days of absence are counted, the first and the last included` (A), `the elapsed days from the first to the last day of absence are counted` (B).
  Functions `F9.4 reading A: the days of absence, both ends included, are longer than that many weeks`, `F9.4 reading B: ...`.
- Discriminating case: absent 1 to 29 March 2026 (Schedule 1: 4 weeks = 28 days).
  A: longer.
  B: not longer.
  For Schedule 2 (56 days): 1 March to 26 April 2026 is 57 days counted, 56 elapsed.
- Tests: `g9-tests-periods.l4` § F9.4; `g9-tests-sched1.l4` §§ 3(2) (grounds, gate and traces); `g9-tests-sched2.l4` §§ 2(2); T20 in `g9-tests-t20.l4`; red.

#### F9.5 "not more than 2 weeks after terminating the appointment" (Sch 1 3(3), src:788; Sch 2 2(3), src:834; P33, P42)
- Readings.
  - A (taken): the notice may be presented up to the 14th day after the termination day (the termination day is day 0).
  - B: the termination day is day 1, so the 13th day after it is the last in time.
- Taken, and why: "not more than 2 weeks after" is a bound on the distance between two days; B counts the day of the event as a day of the 2 weeks, which nothing in the text says.
- Carried by: field `the 2 weeks after a termination`; constructors `the 14th day after the termination day is in time` (A), `the termination day is day 1, so the 13th day after it is the last in time` (B).
  Functions `F9.5 reading A/B: the latest day for a notice after an event ...`.
- Discriminating case: terminated 1 March 2026, notice presented 15 March 2026.
  A: in time.
  B: late.
  A notice presented before the termination day is not a notice that the Minister has terminated the appointment, and is not in time on either reading.
- Tests: `g9-tests-periods.l4` § F9.5; `g9-tests-sched1.l4` §§ 3(3) (six traces); `g9-tests-sched2.l4` §§ 2(3); red.
  The deadline day itself is met on A and missed on B (method note 3).

#### F9.6 "completes 12 years (whether consecutive or in aggregate) of service" (Sch 1 3(4)(c), src:792; Sch 2 2(4)(c), src:838; P34, P43)
- Readings.
  - A (taken): twelve calendar years measured in days from the first day of service.
    Operational definition, which a reviewer may disagree with: let C be the periods of earlier service that count (F9.11); let f be the first day of the earliest period in C, or the first day of the current appointment if C is empty; the target T is the number of days from f to the 12th anniversary of f (`add years` f 12; 4,383 days from 1 March 2026, because 2028, 2032 and 2036 each have a 29 February); the days served P are the sum of (day service stopped minus first day of service) over C; the 12 years are complete on the first day of the current appointment plus the greater of 0 and T minus P.
    The points a reviewer may dispute: that the target is measured on the calendar from f (so gaps between spells do not move it); that the day service stopped is the first day not served, so a spell has no more days than the difference of its two dates; and that the leap days inside gaps are not days served.
  - B: twelve years of 365 days, T = 4,380 (the same procedure).
- Taken, and why: A makes a continuous service of twelve years from 1 March 2026 end on 1 March 2038, the 12th anniversary, which is what "completes 12 years" means to a reader of the calendar; the aggregate for broken service is the least departure from that.
  B is the day-count reading.
- Carried by: field `twelve years of service`; constructors `twelve calendar years measured in days from the first day of service` (A), `twelve years of 365 days` (B).
  Functions `F9.6 reading A: the days in twelve calendar years from the first day of service`, `F9.6 reading B: the days in twelve years of 365 days`, and the shared `Sch 1 and 2: the day on which twelve years of service are completed`.
- Discriminating case: 1,461 days served from 1 March 2026 (1 March 2026 to 1 March 2030), then an appointment from 1 January 2031.
  A: 4,383 days in all, the 12 years complete on 1 January 2039.
  B: 4,380 days, complete on 29 December 2038.
- Trap T21 (tested): ten years served as Commissioner (3,653 days), re-appointed from 1 March 2036 for 5 years to 1 March 2041: the appointment expires on 1 March 2038, two years in (B: 26 February 2038), whatever period was fixed.
- Tests: `g9-tests-periods.l4` § F9.6 and F9.11 and "F9.6: the days that make up twelve years"; `g9-tests-sched1.l4` §§ 3(4) (T21 and the earliest-of-three rule); `g9-tests-sched2.l4` §§ 2(4); red.

#### F9.7 "in no case later than 4 months after the end of that year" (Sch 1 4(9), src:808; Sch 2 3(4), src:843; P36, P44)
- Readings.
  - A (taken): the end of the year is 31 December; plus 4 months, the day clamped to the end of the month, is 30 April; a report provided on 30 April is in time.
  - B: the months are added by rolling: 31 April does not exist, so 1 May.
- Taken, and why: 4 months after the end of 31 December is the end of the same day of April; April has no 31st, and the report must be provided "in no case later".
  A is the clamping daydate does for months and years, which the brief tells the fleet to use.
- Carried by: field `the 4 months after the end of the year`; constructors `the months are added and the day is clamped to the end of the month` (A), `the months are added and the day is rolled into the next month` (B).
  Functions `F9.7 reading A/B: the latest day for a report on a calendar year, ...`.
- Discriminating case: the report on 2026 provided on 1 May 2027.
  A: late.
  B: in time.
- Tests: `g9-tests-periods.l4` § F9.7; `g9-tests-sched1.l4` §§ 4(9) (the last day on three readings, the BOOLEAN and six traces); `g9-tests-sched2.l4` §§ 3(4); red.

#### F9.8 "the decision under Article 15(3) on whether to refuse to deregister a charity" (Sch 1 4(3)(b), src:798; trap T17)
- Readings.
  - A (taken): the decision "on whether to refuse" is the single decision of Article 15(3) (src:432 to src:434: the Commissioner must either deregister or refuse); a decision "on whether" has two outcomes, so either outcome is reserved from staff.
  - B: literal: only the refusal is reserved, so a member of staff may deregister an entity on its own application.
- Taken, and why: "whether to refuse" and "whether to register" (4(3)(a)) and "whether to deregister" (4(3)(c)) are all questions with two answers; reserving only one answer of one of them would be an oddity the text does not signal.
- Carried by: field `the decision under Article 15(3)`; constructors `both outcomes of the decision are reserved` (A), `only the refusal is reserved` (B).
  Functions `F9.8 reading A: both outcomes of the decision under Article 15(3) are reserved`, `F9.8 reading B: only the refusal under Article 15(3) is reserved`.
- Discriminating case: a member of staff, authorized, deregisters an entity on its own application.
  A: staff may not.
  B: staff may.
- Tests: `g9-tests-sched1.l4` §§ 4(3) (the 22 subject-and-outcome cases, the case above, and the readings called directly); red.

#### F9.9 "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017" (Sch 1 2(4)(a), src:776, and 4(7), src:806; trap T22)
- The words exist only from the text of 16 December 2019 (L.1/2017 Article 30(3), endnote [5], in force on the day the Table of Legislation History gives; the Act that appointed it is not among the sources).
  `Sch 1 and 2: the Dormant Bank Accounts words are in the text of` answers FALSE for the texts of 1 January 2019 and 31 May 2019, TRUE for the seven later texts, and refuses for the vintage before the first consolidated version (the sources hold no text of Schedule 1 before 1 January 2019).
- Readings (for a text that has the words).
  - A (taken): to the extent that an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs a distribution to the cost, the cost is met from that Fund in place of the annual income of the States (Article 20(2)(a) of that Law allows the Fund to defray the cost of the Commissioner's remuneration, staff, accommodation and equipment).
  - B: the States remain liable; the Fund only reimburses them.
- Taken, and why: "subject to" is a carve-out from "must be paid out of the annual income of the States"; B would leave the words with no effect on who must pay.
- Carried by: field `a cost directed to the Fund`; constructors `the Fund bears the cost in place of the annual income of the States` (A), `the States remain liable and the Fund only reimburses` (B).
  Functions `F9.9 reading A: the Fund bears the cost the Order directs to it`, `F9.9 reading B: ...`.
  The input is the BOOLEAN `an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs the cost to the Fund`: partial direction ("to the extent") is not modelled; the input is TRUE only for a cost the Order directs to the Fund.
- Discriminating case: the text of 16 December 2019 or later, an Order in force that directs the cost to the Fund, and the Fund empty (who must pay).
  A: the annual income of the States need not pay (the cost lies on the Fund, and nothing in the sources says what follows if it cannot).
  B: the States must.
- Tests: `g9-tests-periods.l4` § "F9.9 text" (ten vintages); `g9-tests-sched1.l4` §§ 2(4)(a) and 4(7) (every vintage that matters, both readings, the refusal); red.

#### F9.10 "as soon as practicable" (Sch 1 4(9) and (10), src:808 and src:809; Sch 2 3(4) and (5), src:843 and src:844; P37, P44)
- Readings.
  - A (taken): whether a step was taken as soon as practicable is a judgement of the person who decides, supplied as an input; the Law fixes no day, so the duty to lay a copy (4(10), 3(5)) has no deadline and the hard stop is the 4 months of 4(9) and 3(4).
  - B: it is measured from the day the step falls due (the end of the year in 4(9) and 3(4); the Minister's receipt of the report in 4(10) and 3(5)) against a number of days, the extra input of the reading.
- Taken, and why: "as soon as practicable" is the Law's own evaluative standard, and the brief makes a discretion an input; B turns it into a number the Law does not give.
- Carried by: field `as soon as practicable`; constructors `as soon as practicable is a judgement supplied as an input` (A), `as soon as practicable is a number of days from the day the step falls due` (B, with the field `number of days`).
  Functions `F9.10 reading A: a step is as soon as practicable when the person who decides finds it so`, `F9.10 reading B: a step is as soon as practicable when it is taken within that many days of falling due`, `F9.10 reading A: a judgement fixes no last day`, `F9.10 reading B: the last day is that many days after the day the step falls due`.
- Discriminating case: report received 1 February 2027, copy laid 15 March 2027, 28 days.
  A: in time if the judgement says so.
  B: late (42 days).
- Tests: `g9-tests-periods.l4` § F9.10 (both pairs of readings called directly); `g9-tests-sched1.l4` §§ 4(9) and 4(10); `g9-tests-sched2.l4` §§ 3(4) and 3(5); red.

#### F9.11 service as a designated relevant person (Sch 1 3(4)(c), src:792, with 4(4) and (5), src:800 to src:804)
- Readings.
  - A (taken): service as a designated relevant person does not count toward the 12 years.
    A designated person is "treated as the Commissioner" only "on a temporary basis" (4(5)), and 3(4)(c) counts "service as Commissioner", the person appointed.
  - B: it counts ("treated as the Commissioner for the purposes of this Law").
- Carried by: field `service as a designated relevant person`; constructors `service as a designated relevant person does not count` (A), `service as a designated relevant person counts` (B).
  Functions `F9.11 reading A: service as a designated relevant person is left out`, `F9.11 reading B: ... is counted`.
- Discriminating case: 14 months (426 days) as a designated relevant person from 1 March 2026, then an appointment from 1 June 2027.
  A: the 12 years are complete on 1 June 2039.
  B: on 1 April 2038 (the 426 days count and the 31 days between the two are not served).
- Tests: `g9-tests-periods.l4` §§ F9.6 and F9.11 and F9.11 called directly; `g9-tests-sched1.l4` §§ 3(4); red.
  Schedule 2 has no relevant person; the same record serves its aggregate.

#### F9.12 a report "in each calendar year" for a year in which the office was held only in part (Sch 1 4(8), src:807; Sch 2 3(3), src:842; P35, P44)
- "Calendar year" is stated (contrast Article 13(7)): no fork on its meaning (trap T24).
- Readings.
  - A (taken): a report is required of the holder for every calendar year in which the office was held on at least one day, for the part held.
  - B: only for a calendar year in which the office was held on every day.
- Taken, and why: "in each calendar year" has no exception for a part-year, and the report is the Commissioner's (and the responsible officer's) duty.
- Carried by: field `a year in which the office was held for only part of it`; constructors `a report is required for the part of the year in which the office was held` (A), `a report is required only for a whole calendar year` (B).
  Functions `F9.12 reading A: ...`, `F9.12 reading B: ...`.
- Discriminating case: the office held from 1 November 2026 to 30 June 2027; the report for 2026.
  A: required (due 30 April 2027).
  B: not required.
- Tests: `g9-tests-periods.l4` § F9.12; `g9-tests-sched1.l4` §§ 4(8) (traces); `g9-tests-sched2.l4` §§ 3(3); red.
  (The Commissioner is a corporation sole, Article 3(1); who owes the report for a year in which the holder changes is an open question, section 7.)

#### F9.13 "a penalty not exceeding imprisonment for a term of 2 years and a fine" (Sch 2 4(3)(f), src:857; P45, IP35)
- Readings, typed by the domain's `Unit of a term of imprisonment`.
  - A (taken): calendar months: the cap is 24 months, and a penalty's term is the number of months in it.
  - B: days: the cap is 730 days; a term of n months is counted from a day (an extra input of this reading).
- Taken, and why: as the PLAN's F7.8, so that the integrator can set the four groups' units from one value (IP35).
- Carried by: field `the unit of the cap on imprisonment`; constructors `calendar months` (A), `days` (B).
  Functions `F9.13 reading A: the term is within the cap when its months are at most 24`, `F9.13 reading B: the term is within the cap when its days are at most 730`.
- Discriminating case: Regulations create an offence with a maximum of 24 months, applied from 1 March 2027 (731 days, 2028 being a leap year).
  A: within the cap.
  B: over it.
  From 1 March 2025 24 months are 730 days: within on both.
- The fine: "a fine" states no amount, so any fine, or none, is within the cap; only the imprisonment is tested.
- Tests: `g9-tests-sched2.l4` §§ 4(3)(f) and "F9.13 called directly"; red.

#### F9.14 "Before appointing a person ... the Minister must seek the views" (Sch 1 1(2), src:759; Sch 2 1(2), src:817)
- Readings.
  - A (taken): the views were sought on an earlier day than the day of the appointment (the Law counts days; two things on one day cannot be put in order).
  - B: on or before the day of the appointment.
- Taken, and why: a sequence "before" cannot be shown at day grain on the same day; A is the conservative reading.
- Carried by: field `before appointing`; constructors `the views were sought on an earlier day than the day of the appointment` (A), `the views were sought on or before the day of the appointment` (B).
  Functions `F9.14 reading A: the latest day for the views to be sought is the day before the appointment`, `F9.14 reading B: ...`.
- Discriminating case: views sought on 15 March 2026 for an appointment on 15 March 2026.
  A: not before.
  B: before.
- Tests: `g9-tests-periods.l4` § F9.14; `g9-tests-sched1.l4` §§ 1(2); `g9-tests-sched2.l4` §§ 1(2); red.

#### F9.15 "(b) the vice-chair, if the chair is absent; or (c) if both the chair and vice-chair are absent" (Sch 2 4(1), src:846 to src:849)
- Readings (where an office of chair or vice-chair is vacant: Schedule 2 1(7) requires both to be designated but says nothing of a vacancy).
  - A (taken): a vacant office counts as absent, so the vice-chair, or a member chosen by those present, presides.
  - B: a vacant office is not covered by the paragraph and the Law does not answer (a refusal).
- Carried by: field `a vacant office of chair or vice-chair`; constructors `a vacant office counts as absent` (A), `a vacant office is not covered and the Law does not answer` (B).
  Functions `F9.15 reading A: a vacant office counts as absent`, `F9.15 reading B: ...` (the refusal).
- Discriminating case: the office of chair vacant, the vice-chair at the sitting.
  A: the vice-chair presides.
  B: refusal.
  With the chair at the sitting the chair presides on both readings, whatever the vice-chair's office.
- Tests: `g9-tests-sched2.l4` §§ 4(1) (all nine pairs of statuses on each reading) and "F9.15 called directly"; red.

#### F9.16 the decision on entry in the restricted section (Sch 1 4(3)(a), src:797; Articles 9(6) and (7), src:280 to src:286; 11, src:298)
- Reserved decisions are named by Article: "the decision under Article 11 on whether to register a charity".
  Entry in the restricted section is decided under Article 9(6) and (7), not Article 11 (Article 33(1)(b) lets an applicant appeal a refusal to register it in the restricted section).
- Readings.
  - A (taken): the literal text reserves the Article 11 decision only; the decision on entry in the restricted section is not reserved and staff may make it when authorized.
  - B: it is part of the decision whether to register and is reserved.
- Carried by: field `the decision on entry in the restricted section`; constructors `it is not reserved because it is not a decision under Article 11` (A), `it is reserved as part of the decision whether to register` (B).
  Functions `F9.16 reading A/B: the decision on entry in the restricted section is [not] reserved`.
- Discriminating case: a member of staff, authorized, decides a request for entry in the restricted section.
  A: staff may.
  B: staff may not.
- Tests: `g9-tests-sched1.l4` §§ 4(3); red.

#### F9.17 "the person becomes a member of the States" (Sch 1 3(4)(b), src:791; Sch 2 2(4)(b), src:837)
- Readings.
  - A (taken): only becoming a member on or after the first day of the term ends the appointment; a person who was already a member when appointed is not caught by the event.
  - B: being a member at any time during the appointment ends it, so a person already a member when appointed has the appointment expire on its first day.
- Taken, and why: "becomes" names an event; the Law does not bar a member of the States from appointment.
- Carried by: field `membership of the States when appointed`; constructors `only becoming a member during the appointment ends it` (A), `being a member at any time during the appointment ends it` (B).
  Functions `F9.17 reading A/B: ...`, shared in `g9-common.l4`.
- Discriminating case: a member of the States since 1 January 2025 appointed from 1 March 2026.
  A: no expiry under (b).
  B: expires on 1 March 2026.
- Tests: `g9-tests-periods.l4` § F9.17; `g9-tests-sched1.l4` §§ 3(4); `g9-tests-sched2.l4` §§ 2(4); red.

#### F9.18 "at least one member of staff to serve as the responsible officer" against "the responsible officer" (Sch 2 3(2), src:841, and 3(3) to (5), src:842 to src:844)
- Readings (with several members of staff available, which is "the responsible officer" whose duties 3(3) and (4) state?).
  - A (taken): the one member of staff the Minister has named (an input; the Law does not say how the officer is named).
    With one member available that member; with several available and none named, no answer (a refusal).
  - B: every member of staff available is the responsible officer.
- Carried by: field `the responsible officer where several members of staff are available`; constructors `the one member of staff the Minister has named is the responsible officer` (A), `every member of staff available is the responsible officer` (B).
  Functions `F9.18 reading A/B: ...`.
- Discriminating case: Dee and Eli available, Dee named.
  A: Dee alone.
  B: both.
- Tests: `g9-tests-sched2.l4` §§ 3(2) and "F9.18 called directly"; red.
  The duties themselves are typed by the role `the responsible officer of the tribunal under Schedule 2`, so the fork is about who holds the role.

#### F9.19 "after satisfying himself or herself that the person has been absent ... for a period longer than" (Sch 1 3(2)(a), src:784; Sch 2 2(2)(a), src:830)
- Readings.
  - A (taken): both the Minister's satisfaction and an absence that really is longer than the number of weeks are required.
    The number is the one number in the grounds, and a power that ignored it would make the number pointless.
  - B: the Minister's satisfaction alone is required (the days are evidence).
  - For grounds (b), (c) and (d) there is no number to compute: the Minister's satisfaction is the whole ground.
- Carried by: field `the ground of absence for terminating an appointment`; constructors `the Minister's satisfaction and the absence longer than the number of weeks are both required` (A), `the Minister's satisfaction alone is required` (B).
  Functions `F9.19 reading A: ...`, `F9.19 reading B: ...`.
- Discriminating case: absent 1 to 28 March 2026 (28 days, not longer than 4 weeks), the Minister satisfied.
  A: the ground is not made out.
  B: it is.
- Tests: `g9-tests-periods.l4` § F9.19; `g9-tests-sched1.l4` §§ 3(2); `g9-tests-sched2.l4` §§ 2(2); red.


## 3. Answer table of the headline scenarios

Each answer is on the favoured interpretation (reading A of every fork) unless the cell says otherwise; each is asserted in the tests named in section 2.

| scenario | answer | provision |
| --- | --- | --- |
| a notice of intention presented 1 March 2026 for an appointment on 15 March 2026 | in time (reading B of F9.1: late; it would have to be presented by 28 February) | Sch 1 1(3), src:760; Sch 2 1(3), src:818 |
| the views of the Jersey Appointments Commission sought for an appointment on 15 March 2026 | last day 14 March 2026 (reading B of F9.14: 15 March) | Sch 1 1(2), src:759; Sch 2 1(2), src:817 |
| a term from 1 March 2026 expiring 1 March 2032; or 2 March 2032 | within 6 years (reading B of F9.2: over); over | Sch 1 1(5), src:762; Sch 2 1(5), src:820 |
| fewer than 4 members, exactly 4 to 8 members, a ninth appointment | the duty to appoint stands; within the limits; breach | Sch 2 1(1), src:816 |
| the Commissioner's notice of resignation given 30 November 2026 | the earliest day it can take effect is 28 February 2027 (reading C: 2 March 2027); the office ends on the day it takes effect (reading B: on 30 November 2026) | Sch 1 3(1)(a), src:780 |
| a notice given 30 November 2026 taking effect 30 December 2026 | a valid resignation of a tribunal member (one month); not a resignation of the Commissioner (3 months) | Sch 2 2(1)(a), src:826; Sch 1 3(1)(a); trap T20 |
| absent from duties 1 to 29 March 2026 (29 days), the Minister satisfied | a ground to terminate the Commissioner (longer than 4 weeks); not a ground to terminate a member (longer than 8 weeks); 1 to 28 March: a ground for neither; 1 March to 26 April: a ground for both | Sch 1 3(2)(a), src:784; Sch 2 2(2)(a), src:830 |
| termination on 1 March 2026 | the notice to the States is in time up to 15 March 2026 (reading B of F9.5: 14 March) | Sch 1 3(3), src:788; Sch 2 2(3), src:834 |
| an appointment from 1 March 2026 expiring 1 March 2032, no earlier service | expires 1 March 2032 | Sch 1 3(4), src:789 to src:792 |
| the same appointment followed by a re-appointment | the end of its period is not an expiry; the 12 years are complete on 1 March 2038 (reading B of F9.6: 26 February 2038) | Sch 1 3(4)(a) and (c) |
| trap T21: ten years served, re-appointed from 1 March 2036 for 5 years to 1 March 2041 | expires 1 March 2038, two years into the new period | Sch 1 3(4)(c), src:792; Sch 2 2(4)(c), src:838 |
| a person already a member of the States since 1 January 2025, appointed from 1 March 2026 | no expiry under (b) (reading B of F9.17: expires on 1 March 2026) | Sch 1 3(4)(b), src:791 |
| a spell as a designated relevant person, then an appointment from 1 June 2027 | does not count toward the 12 years (reading B of F9.11: it does; the 12 years are complete 1 April 2038) | Sch 1 3(4)(c), 4(5) |
| the remuneration of the Commissioner, in the text of 31 May 2019 | must be paid out of the annual income of the States whatever any Order says | Sch 1 2(4)(a), src:776 |
| the same, in the text of 16 December 2019 or later, an Order directing the cost to the Fund | not out of the annual income of the States (reading B of F9.9: still out of it); in the text before 1 January 2019: a refusal | Sch 1 2(4)(a), 4(7), src:776, src:806; trap T22 |
| a member of staff, authorized, makes the decision on: registering (Art 11); deregistering on the entity's own application (Art 15(3)); deregistering under Art 16; permitting a name change; entering in the restricted section | may not; may not (reading B of F9.8: may); may not; may; may (reading B of F9.16: may not) | Sch 1 4(3), src:796 to src:799; trap T17 |
| someone is acting as the Commissioner: appointee in office and able to act; vacancy and a relevant person designated; vacancy and none designated; appointee unable and one designated | yes; yes; no; yes | Sch 1 4(5), src:801 to src:804 (IP28) |
| the report on 2026: last day to provide it to the Minister | 30 April 2027 (reading B of F9.7: 1 May 2027; reading B of F9.10 with 28 days: 28 January 2027) | Sch 1 4(9), src:808; Sch 2 3(4), src:843 |
| the Minister's laying of a copy before the States | no day is fixed (reading B of F9.10: the day of receipt plus the days, 1 March 2027 for receipt on 1 February 2027 and 28 days) | Sch 1 4(10), src:809; Sch 2 3(5), src:844 |
| the office held 1 November 2026 to 30 June 2027: is a report required for 2026? | yes (reading B of F9.12: no) | Sch 1 4(8), src:807; Sch 2 3(3), src:842 |
| honorary service of a tribunal member | honorary unless the Minister has determined that the chair, or all the members, are to be remunerated | Sch 2 1(8), src:823 |
| who presides when the chair is absent and the vice-chair is at the sitting; when both are absent; when the chair is at the sitting | the vice-chair; a member appointed by those present; the chair | Sch 2 4(1), src:846 to src:849 |
| the quorum of the tribunal | a refusal: the Law states none | Sch 2 4(3)(e), src:856 |
| Regulations creating an offence in relation to the tribunal, with 24 months and a fine; with 25 months | within the cap; over it (reading B of F9.13: 24 months from 1 March 2027 are 731 days, over the cap of 730) | Sch 2 4(3)(f), src:857 |
| two members of staff available as responsible officer, one named | the named one (reading B of F9.18: both) | Sch 2 3(2), src:841 |

## 4. Nouns requests for the INTEGRATOR

1. `Legal actor` has no constructor for a member of the Charity Tribunal or for the tribunal's responsible officer (Sch 2 2(1)(a), 3(2) to (4)).
   `g9-sched2-tribunal.l4` declares a stand-in, `Role under Schedule 2` with the constructors `a member of the tribunal under Schedule 2` and `the responsible officer of the tribunal under Schedule 2`, and uses it only as the party of the rules of a member and of the responsible officer.
   Request: add `a member of the Charity Tribunal` and `the responsible officer of the Charity Tribunal` to `Legal actor`; the integrator may then replace the stand-in.
2. `Period of service under the Schedules` (first day, day service stopped, as a designated relevant person) is declared in `g9-common.l4`; it is the input of the 12-year aggregate.
   Request: move it to `domain.l4` only if another group needs a person's service.
3. No other noun is requested: the Minister, the Commissioner, the States and the Charity Tribunal are `Legal actor` constructors; `Vintage of the text`, `Decision of the Commissioner`, `Penalty provided` and `Unit of a term of imprisonment` are read from `domain.l4`.

## 5. Inputs consumed and functions exported

Standard inputs, by their exact `GIVEN` names (PLAN section (c)):

| id | exact name and type | where it is read |
| --- | --- | --- |
| IP1 | `the day` : DATE | `Sch 1 para 3(1) the person has ceased to be appointed as the Commissioner by the day`, `Sch 1 para 3(4) the appointment has expired by the day`, `Sch 1 para 3(1)(a) the person has resigned by the day`, `Sch 1 para 3(1)(b) the Minister has terminated the appointment by the day`, and, for Schedule 2, `Sch 2 para 2(1) the person has ceased to be a member of the tribunal by the day`, `Sch 2 para 2(4) the appointment has expired by the day`, `Sch 2 para 2(1)(a) the person has resigned by the day` and `Sch 2 para 2(1)(b) the Minister has terminated the appointment by the day` |
| IP2 | `the vintage of the text` : `Vintage of the text` | `Sch 1 and 2: the Dormant Bank Accounts words are in the text of`, hence `Sch 1 para 2(4)(a) ...` and `Sch 1 para 4(7) ...` |
| IP27 | `the decision of the Commissioner` : `Decision of the Commissioner` | `Sch 1 para 4(3) the decision is one that a member of the Commissioner's staff may not make on behalf of the Commissioner` and `Sch 1 para 4(3) a member of the Commissioner's staff may exercise the function on behalf of the Commissioner` |
| IP35 | field `the unit of the cap on imprisonment` : `Unit of a term of imprisonment` of the record `Interpretation of Schedules 1 and 2` | `Sch 2 para 4(3)(f) the penalty is within the cap` |
| (T22) | `an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs the cost to the Fund` : BOOLEAN | `Sch 1 para 2(4)(a) ...`, `Sch 1 para 4(7) ...` |

Produced for other groups: IP28, `Sch 1 para 4(5) someone is treated as the Commissioner` (BOOLEAN; three inputs: a relevant person has been designated, the appointee is unable to act, there is a vacancy).
A consumer's `GIVEN someone is acting as the Commissioner` is wired to this export.
The `Appointment ...`, `Events ...`, `Grounds ...`, `Report ...` records are inputs of this group's own rules, built by the caller from the facts of a case.
The integrator sets all of the fields of `Interpretation of Schedules 1 and 2` (it is one `GIVEN interp`): `the unit of the cap on imprisonment` must take the same value as the units of F6.16, F7.8 and F8.8 (IP35).

Exports (68; `@export` with a sentence and a `@desc` on every `GIVEN`; the DEONTIC ones return the obligation, permission or prohibition as a value):

| module | export (exact name) | inputs (exact GIVEN names) | gives |
| --- | --- | --- | --- |
| g9-sched1-commissioner | `Sch 1 para 1(1) the Minister must appoint a person appearing to the Minister to be suitable` | `the office of the Commissioner is vacant`, `the person appears to the Minister to be suitable` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 1(2) before appointing a person the Minister must seek the views of the Jersey Appointments Commission` | `interp`, `the day of the appointment` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 1(3) at least 2 weeks before appointing the Minister must present to the States a notice of intention` | `interp`, `the day of the appointment` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 1(3) the notice of intention was presented to the States in time` | `interp`, `appointment` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 1(5) the period of the appointment is within the limit` | `interp`, `appointment` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 1(5) when appointing the Minister must determine the period of the appointment, being not more than 6 years` | `interp`, `appointment` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 1(6) the Minister may re-appoint a person serving as the Commissioner` | `the person is serving as the Commissioner` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 1(7) the Minister must take all reasonable steps to ensure that at all times the office of the Commissioner is filled` | `the office of the Commissioner is filled` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 2(4)(a) the remuneration of the Commissioner must be paid out of the annual income of the States` | `interp`, `the vintage of the text`, `an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs the cost to the Fund` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 3(1)(a) the day the office ends by resignation` | `interp`, `resignation` | A MAYBE DATE |
| g9-sched1-commissioner | `Sch 1 para 3(1)(a) the Commissioner may resign from office by giving not less than 3 months' notice in writing to the Minister` | `interp`, `resignation` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 3(2) the Minister has satisfied himself or herself on a ground for terminating` | `interp`, `grounds` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 3(2) the Minister may terminate the appointment of a person as the Commissioner` | `interp`, `grounds` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 3(3) not more than 2 weeks after terminating the appointment the Minister must present to the States a notice that the Minister has terminated it` | `interp`, `the day of the termination` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 3(3) the notice of the termination was presented to the States in time` | `interp`, `the day of the termination`, `the day on which the notice was presented to the States` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 3(4) the day on which the appointment expires` | `interp`, `appointment` | A DATE |
| g9-sched1-commissioner | `Sch 1 para 3(1) the person has ceased to be appointed as the Commissioner by the day` | `interp`, `appointment`, `events`, `the day` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(1) the Minister must make available to the Commissioner such number and descriptions of staff as the Minister considers are required` | `staff` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(2) the employee is to be treated as a member of the Commissioner's staff for the function` | `the person is a States' employee within the meaning of the Employment of States of Jersey Employees (Jersey) Law 2005`, `the employee was made available to the Commissioner under paragraph 4(1)`, `the employee performs the function under the direction of the Commissioner` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(3) the decision is one that a member of the Commissioner's staff may not make on behalf of the Commissioner` | `interp`, `the decision of the Commissioner` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(3) a member of the Commissioner's staff may exercise the function on behalf of the Commissioner` | `interp`, `the decision of the Commissioner`, `the Commissioner has authorized the member of staff to exercise the function` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(4) the Minister may designate a person as the relevant person for the purpose of sub-paragraph (5)` | none | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(5) someone is treated as the Commissioner` | `a relevant person has been designated under sub-paragraph (4)`, `the person appointed as the Commissioner is unable to act through incapacity or absence`, `there is a vacancy in the office of Commissioner` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(6) the Minister must provide such accommodation and equipment as the Minister considers are required` | `the accommodation and equipment provided are those the Minister considers are required` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(7) the cost of providing staff, accommodation and equipment must be met out of the annual income of the States` | `interp`, `the vintage of the text`, `an Order under Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 directs the cost to the Fund` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(8) the Commissioner must prepare and publish a report on the activities of the Commissioner in each calendar year` | `interp`, `the first day on which the office was held`, `the last day on which the office was held`, `the calendar year` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(9) the Commissioner must provide the Minister with the report as soon as practicable after the end of the year, and in no case later than 4 months after it` | `interp`, `the calendar year` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(9) the Commissioner provided the Minister with the report in time` | `interp`, `report` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(10) the Minister must lay a copy of the report so provided before the States as soon as practicable after receiving it` | `interp`, `the day on which the Minister received the report` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(10) the Minister laid a copy of the report before the States as soon as practicable` | `interp`, `report`, `the day on which the Minister received the report` | A BOOLEAN |
| g9-sched1-commissioner | `Sch 1 para 4(11) the Minister may, by giving written notice to the Commissioner and publishing that notice, give directions on the content and form of the report` | `the notice is in writing and has been published` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(12) directions under sub-paragraph (11) must not require the report to contain justification of any decision of the Commissioner in relation to individual charities, governors or applicants for registration` | `the direction requires the report to contain justification of a decision of the Commissioner in relation to individual charities, governors or applicants for registration` | A DEONTIC Legal actor Act under Schedule 1 |
| g9-sched1-commissioner | `Sch 1 para 4(12) the directions are within the limit` | `the directions respect the independence of the Commissioner`, `the directions require the report to contain justification of a decision of the Commissioner in relation to individual charities, governors or applicants for registration` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 1(1) the number of members of the tribunal is within the limits` | `the number of members of the tribunal` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 1(1) the Minister must appoint at least 4 persons appearing to be suitable and to have appropriate experience as members of the tribunal` | `the number of members of the tribunal`, `appointment` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(1) the Minister must not appoint more than 8 members of the tribunal` | `the number of members of the tribunal` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(2) before appointing a person as a tribunal member the Minister must seek the views of the Jersey Appointments Commission` | `interp`, `the day of the appointment` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(3) at least 2 weeks before appointing a person as a tribunal member the Minister must present to the States a notice of intention` | `interp`, `the day of the appointment` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(3) the notice of intention was presented to the States in time` | `interp`, `appointment` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 1(5) the period of the appointment is within the limit` | `interp`, `appointment` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 1(5) when appointing a person as a tribunal member the Minister must determine the period of the appointment, being not more than 6 years` | `interp`, `appointment` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(6) the Minister may re-appoint a person serving as a tribunal member` | `the person is serving as a member of the tribunal` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(7) one member is designated as the chair and another as the vice-chair` | `members`, `chair`, `vice-chair` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 1(7) the Minister must designate one member as the chair and another as the vice-chair` | `members`, `chair`, `vice-chair` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(8) the Minister may determine that the chair is, or all the members are, to be remunerated by the States` | none | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 1(8) service as a tribunal member is honorary` | `determination`, `the member is the chair` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 2(1)(a) the day the position ends by resignation` | `interp`, `resignation` | A MAYBE DATE |
| g9-sched2-tribunal | `Sch 2 para 2(1)(a) a member may resign from office by giving not less than one month's notice in writing to the Minister` | `interp`, `resignation` | A DEONTIC Role under Schedule 2 Act of a member or the responsible officer under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 2(2) the Minister has satisfied himself or herself on a ground for terminating` | `interp`, `grounds` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 2(2) the Minister may terminate the appointment of a person as a member of the tribunal` | `interp`, `grounds` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 2(3) not more than 2 weeks after terminating the appointment the Minister must present to the States a notice that the Minister has terminated it` | `interp`, `the day of the termination` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 2(3) the notice of the termination was presented to the States in time` | `interp`, `the day of the termination`, `the day on which the notice was presented to the States` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 2(4) the day on which the appointment expires` | `interp`, `appointment` | A DATE |
| g9-sched2-tribunal | `Sch 2 para 2(1) the person has ceased to be a member of the tribunal by the day` | `interp`, `appointment`, `events`, `the day` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 3(1) the Minister must make available to the tribunal such number and descriptions of staff and resources as the Minister considers are required` | `provision` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 3(2) at least one member of staff is available to the tribunal as the responsible officer` | `the number of members of staff available to the tribunal to serve as the responsible officer`, `the responsible officer is charged with assisting with the administration of the tribunal and not with determinations by it` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 3(2) the Minister must secure that at least one member of staff is available to the tribunal as the responsible officer` | `the number of members of staff available to the tribunal to serve as the responsible officer`, `the responsible officer is charged with assisting with the administration of the tribunal and not with determinations by it` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 3(3) the responsible officer must prepare a report on the activities of the tribunal in each calendar year` | `interp`, `the first day on which the post was held`, `the last day on which the post was held`, `the calendar year` | A DEONTIC Role under Schedule 2 Act of a member or the responsible officer under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 3(4) the responsible officer must provide the Minister with the report as soon as practicable after the end of the year, and in no case later than 4 months after it` | `interp`, `the calendar year` | A DEONTIC Role under Schedule 2 Act of a member or the responsible officer under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 3(4) the responsible officer provided the Minister with the report in time` | `interp`, `report` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 3(5) the Minister must lay a copy of the report so provided before the States as soon as practicable after receiving it` | `interp`, `the day on which the Minister received the report` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 3(5) the Minister laid a copy of the report before the States as soon as practicable` | `interp`, `report`, `the day on which the Minister received the report` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 4(1) the person presiding over a sitting` | `interp`, `chair`, `vice-chair` | A Person presiding over a sitting of the tribunal |
| g9-sched2-tribunal | `Sch 2 para 4(2) the tribunal may regulate the matter by its own procedure` | `paragraph 4(1) deals with the matter`, `Regulations under paragraph 4(3) deal with the matter` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 4(2) subject to sub-paragraph (1) and to any Regulations under sub-paragraph (3) the tribunal may regulate its own procedure` | `paragraph 4(1) deals with the matter`, `Regulations under paragraph 4(3) deal with the matter` | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 4(3) the States may by Regulations make further provision as to the procedure of the tribunal` | none | A DEONTIC Legal actor Act under Schedule 2 |
| g9-sched2-tribunal | `Sch 2 para 4(3)(f) the penalty is within the cap` | `interp`, `penalty`, `the day from which the term of imprisonment would run` | A BOOLEAN |
| g9-sched2-tribunal | `Sch 2 para 4(3)(f) the States may by Regulations provide for costs and create offences in relation to the tribunal with a penalty not exceeding imprisonment for 2 years and a fine` | `interp`, `penalty`, `the day from which the term of imprisonment would run` | A DEONTIC Legal actor Act under Schedule 2 |


## 6. Contradictions found in the source, by a separate pass after encoding

The pass re-read src:754 to src:861 against the modules, looking for a definition and its use that disagree, two provisions that answer one question differently, a cross-reference to something that is not there, and a figure that differs between parallel provisions.
Items 1 to 6 are in the Law; item 7 is a statement of the survey that the source corrects; items 8 to 10 are weaker points (a tension, an interplay, a typographical slip) recorded so that a reviewer need not rediscover them.

1. **Schedule 2's heading against Article 32 and Article 1.** src:814 heads Schedule 2 "Charity Commission tribunal"; Article 32(1) (src:686) establishes "a tribunal to be known as the Charity Tribunal" and Article 1 defines the tribunal accordingly.
   The PDF text layer has the same heading (upper case).
   The heading is not operative and names the same body; carried as inert text `Sch 2 the heading Charity Commission tribunal (inert)`.
   No fork: no rule turns on the name.
2. **Schedule 1 4(12), "Directions under paragraph (11)" (src:811).** Every other reference to a sub-paragraph in both Schedules says "sub-paragraph" (src:761 to src:861; "paragraph 1" in 4(5), "this paragraph" in 1(6) and 4(7) refer to whole paragraphs).
   Paragraph (11) is a sub-paragraph of paragraph 4, so the reference is read as sub-paragraph (11).
   This is the only such reference.
   No discriminating case: the only sub-paragraph (11) in Schedule 1 is 4(11), and the Schedules have no paragraph 11.
3. **Schedule 1 4(3)(b), "the decision under Article 15(3) on whether to refuse to deregister a charity" (src:798), against Article 15(3) (src:432 to src:434).** Article 15(3) is one decision with two outcomes, to deregister or to refuse; 4(3)(b) names the decision by one outcome.
   Fork F9.8; discriminating case: staff deregister an entity on its own application.
   Both readings are functions with tests.
4. **Schedule 1 4(3)(a), "the decision under Article 11" (src:797), against Article 9(6) and (7) (src:280 to src:286) and Article 33(1)(b) (src:692).** Entry in the restricted section is decided under Article 9, but Article 33(1)(b) treats a refusal to register in the restricted section as a decision on registration that the applicant may appeal.
   Fork F9.16; discriminating case: staff decide a request for entry in the restricted section.
   Both readings are functions with tests.
5. **Schedule 2 3(2), "at least one member of staff to serve as the responsible officer" (src:841), against 3(3) to (5), "the responsible officer" (src:842 to src:844).** One or more members of staff may be available, but the duties are the duties of "the" responsible officer, in the singular.
   Fork F9.18; discriminating case: two members of staff available and one named.
   Both readings are functions with tests.
6. **Terminology: Schedule 2 1(4) "vacates that position" (src:819) and 2(1)(a) "resigns from office" (src:826); Schedule 1 says "office" throughout.** Not operative; `position` and `office` are read as the same thing.
   Noted so that a reviewer does not look for a difference.
7. **A statement of the survey, not of the Law: the row for Schedule 1 2(1)(d) said the Law creates no offence the Commissioner could commit.** Article 29(1) (src:664 to src:667) makes it an offence for "a person who receives information ... under or for the purposes of this Law" to disclose it without consent; on its words the Commissioner is such a person.
   The row's reason was rewritten; its disposition, inert, stands.
8. **Tension, not a contradiction: independence (Sch 1 2(2), src:773) against the Minister's powers of appointment, termination and direction (1(1), 3(2), 4(11)).** 4(12) states the one limit the Law puts on directions.
   The independence is inert here; its operative echo, 4(12), is encoded.
9. **Interplay, not a contradiction: a period of "not more than 6 years" (1(5)) that cannot be completed because 12 years of service are reached first (3(4)(c)).** Trap T21: the appointment expires at the 12-year mark whatever period was fixed; tested.
10. **Typographical: Schedule 2 1(8) "as Minister sees fit" (src:823) lacks "the".** No effect.

## 7. Open questions for a domain expert

1. Does the Minister's duty to appoint (Sch 1 1(1)) arise only while the office is vacant, and is there a time limit?
   The text states neither (section 8).
2. When an instrument fixes a period of appointment, does its end date mean the day the period expires or the last day of service (F9.2)?
   And is a period of exactly six years and a day one the Law forbids?
3. Does a resignation on notice take effect when the notice runs out, or when it is given (F9.3)?
   How does Jersey practice add months to a date at the end of a month (clamped or rolled)?
4. Under Sch 1 3(2) and Sch 2 2(2): must a ground exist in fact, or is the Minister's satisfaction enough (F9.19)?
   For the absence ground, are the first and the last day of the absence both counted (F9.4)?
5. Is a day on which a notice is presented to the States counted in the "2 weeks before appointing" and "2 weeks after terminating" (F9.1, F9.5)?
   Does the Interpretation (Jersey) Law 1954 (not in the sources) settle "clear days", "month" and "year"?
6. How is "12 years (whether consecutive or in aggregate)" reckoned for broken service (F9.6): by calendar years from the first day of service, or by days?
   Does service as a relevant person designated under 4(4) count (F9.11)?
7. "Subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017": does an Order displace the States' liability or only reimburse (F9.9)?
   To what extent, and who pays if the Fund cannot?
   On what day did L.1/2017 come into force (the Table says 16 December 2019; the Act that appointed it is not among the sources)?
8. May a person already a member of the States be appointed, and if so does the appointment expire at once (F9.17)?
9. Who owes the annual report for a year in which the office changes hands (F9.12)?
   Is the tribunal's report published, as the Commissioner's must be?
10. How is a relevant person designated under Sch 1 4(4): may the designation be made before the incapacity or vacancy, and how long may the "temporary basis" last?
11. Who names the responsible officer where several members of staff are available (F9.18)?
    Is there a quorum for a sitting in practice, and have Regulations under Sch 2 4(3) been made?
12. Does the vacancy of the office of chair or vice-chair count as absence for Sch 2 4(1) (F9.15)?
    What happens to the designation of chair or vice-chair when that member's appointment ends?
13. Is the decision on entry in the restricted section one that staff may make (F9.16)?
    Is the decision to deregister on the entity's own application, Article 15(3)(a), reserved from staff (F9.8)?

## 8. What the sources do not answer

Each is a place where the encoding gives a named refusal, takes an input, or states its assumption; none is a plausible value.
1. **The Interpretation (Jersey) Law 1954.** How a period, a month or a year is counted is not in the sources; every counting is a fork.
2. **The Act appointing 16 December 2019 for L.1/2017, and R&O.136/2019.** The commencement of the Dormant Bank Accounts words is the Table's date, not read from the appointing instrument.
3. **The text of Schedule 1 before 1 January 2019.** No consolidated version precedes it; `Sch 1 and 2: the Dormant Bank Accounts words are in the text of` refuses for that vintage.
4. **The Dormant Bank Accounts (Jersey) Law 2017 beyond Articles 20(1), 20(2)(a), 30(3) and 31(2),** and every Order made under Article 20(1): whether an Order directs the cost to the Fund is an input; how much, and whether the Fund can pay, is not modelled.
5. **Regulations under Sch 2 4(3):** their existence and content; the quorum and voting rules of a sitting (a named refusal); the matters (a) to (e) and (g) to (j) (inert).
6. **Any trigger or deadline for the Minister's duty to appoint (Sch 1 1(1)):** the rule reads the duty as standing while the office is vacant; the Law states neither the trigger nor a time.
   The same for the duty to appoint at least 4 tribunal members (Sch 2 1(1)): it stands while there are fewer than 4.
   And the same for the Commissioner's payment of fees and other sums to the income of the States (Sch 1 2(4)(b)): the Law states no time.
7. **How a notice is presented to the States, how a resignation or termination is given effect, and what the States do with the notices of intention or of termination.** Dates are inputs.
8. **How long the "temporary basis" of Sch 1 4(5) lasts,** and whether a designation may be made in advance of the incapacity or vacancy.
9. **Who names the responsible officer** (F9.18), and what happens to the designation of chair and vice-chair when a member ceases to be one (Sch 2).
10. **Whether the Fund can pay** when an Order directs a cost to it (F9.9).
11. **Everything the Law leaves to the Minister's, the Commissioner's or the court's judgement:** suitability, experience, satisfaction on each ground, "considers are required", "all reasonable steps", "as soon as practicable", the Commissioner's opinion that a report was published; all are inputs.
12. **Anything after 2 October 2026,** the text being "from 2 October 2026 to Current".

## 9. What `check.sh` prints, and what else was checked

`work/g9/check.sh` is the skill's `assets/check.sh` adapted to run only `DEPOSIT/g9-*.l4`, under `nice -n 15`, with a warnings column and the shape, `srcrefs.py` and trace steps added from the fleet's template.
It prints, on the fleet's binary (sha256 `18bd5a72...e89d475`):

```
l4 binary: /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4 (sha256 matches the fleet's binary)

module                              errors satisfied  failed  refused  warnings  expected
g9-common.l4                             0         0       0        0         0         0
g9-interpretation.l4                     0         0       0        0         0         0
g9-sched1-commissioner.l4                0         0       0        0         0         0
g9-sched2-tribunal.l4                    0         0       0        0         0         0
g9-tests-periods.l4                      0       170       0        0         0         0
g9-tests-red.l4                         19         0      19        0         0        19
g9-tests-sched1.l4                       0       230       0        0         0         0
g9-tests-sched2.l4                       0       203       0        0         0         0
g9-tests-t20.l4                          0        18       0        0         0         0
TOTAL (9 modules)                       19       621      19        0         0        19
(a failed assertion is also an error; any other error, any refused assertion, any warning, and any failed count other than expected, make the run red)

shape: ok (ASCII names, no @lang line, every import is prelude, daydate, domain or a g9- module)
srcrefs check: 148 src: lines, 112 runs, 285 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g9-tests-sched1.l4                                65        65         0     65     0          0
g9-tests-sched2.l4                                66        66         0     66     0          0
TOTAL                                            131       131         0    131     0          0
check-traces: all 131 guarded trace(s) behaved as expected

check.sh (G9): GREEN
```

How to read it.
- The 19 failed assertions of `g9-tests-red.l4` are meant to fail, one per fork; check.sh lists that module with `expected` 19 and stays green only if it fails exactly 19 times.
  No assertion refused anywhere and no module has a warning.
  Every `#ASSERT REFUSED` is satisfied (counted among the 621).
- The 131 traces are `#TRACE`s, each with a `-- EXPECT:` comment above it (FULFILLED, BREACH BY ..., or STANDING); check-traces.py runs each and compares.
  A positive control was run: a temporary module with a wrong `#ASSERT` and a wrong `EXPECT` was made red by both (it was removed afterwards).
- `srcrefs.py check --refs` over every module: 148 quote lines, 112 runs, 285 locators, 0 problems.
  Because srcrefs cannot see that a locator names the right provision, a second script (`work/g9/refcheck.py`) ties each of the 285 locators to the paragraph, sub-paragraph and letter its `@ref` text names and to the right Schedule: 0 mismatches.
- Number re-read: every figure in the five test modules is either a figure of the Law (2 weeks, 6 years, 3 months, one month, 4 weeks, 8 weeks, 12 years, 4 months, 4 and 8 members, 2 years; src:760, 762, 780, 826, 784, 830, 792, 838, 808, 843, 816, 857) or an arithmetic consequence.
  The consequences (the dates 28 February 2027, 30 April 2027, 1 March 2038 and so on, and the counts 4,383, 4,380, 3,653, 1,461, 2,922, 426, 1,887, 731, 730, 703) were worked out by hand before the run and then recomputed independently with Python's `datetime` (`work/g9/oracle.py`): 49 checks, 0 disagree.
  A listing of every integer in the `#ASSERT`s shows no number outside those.
- Tests are from the source and the calendar, not from the code.
  One batch of 10 assertions failed on first run: they were the 4(1) presiding matrix of `g9-tests-sched2.l4`, generated by a script of mine whose expectation function was handed a long status name where it tested a short code; the expectations were wrong, not the encoding.
  The generator was corrected and the expectations regenerated from the text of 4(1); no other expected value was changed after a run.

Counts: 5,025 lines in 9 modules; 68 exports (33 in Schedule 1, 35 in Schedule 2); 621 satisfied assertions and 19 meant to fail; 131 traces; 29 `#CHECK`s that the inert definitions exist.

## 10. Notes for the integrator

1. **Wiring.** The only group-to-group wires are IP1, IP2, IP27, IP35 and IP28 (section 5).
   `interp` is one record: pass the same value everywhere in G9.
   `TYPICALLY` is metadata in this release, so the record is not defaulted by the language: use the named value `the favoured interpretation` (in `g9-interpretation.l4`) as the default, and set the field `the unit of the cap on imprisonment` equal to the units of F6.16, F7.8 and F8.8.
   Every `@export` has a sentence and a `@desc` on every `GIVEN` (checked mechanically over all 68).
2. **Commencement is the integrator's wrapper**: G9 does not gate itself.
   Schedules 1 and 2 are in force from 21 November 2014 (the Table of Legislation History, src:876 and src:877), so the wrapper for any G9 export asks for the unit `a Schedule to the Law` with `schedule number` 1 or 2.
3. **The vintage matrix**: the only vintage-dependent rules of G9 are `Sch 1 para 2(4)(a) ...` and `Sch 1 para 4(7) ...`; for each of the ten values of `Vintage of the text` they answer as `g9-tests-sched1.l4` §§ 2(4)(a) and 4(7) and `g9-tests-periods.l4` § "F9.9 text" assert.
4. **Records are inputs.** An `Appointment of the Commissioner` or `Appointment of a member of the tribunal` is built by the caller from the case; the periods of earlier service are given earliest first and not overlapping (the module does not check this).
5. **A refusal is only ever raised by a question the Law does not answer:** the vintage before the first consolidated version (F9.9 text), a vacant office of chair or vice-chair on reading B of F9.15, the responsible officer where several are available and none is named on reading A of F9.18, and the quorum.
   Nothing else refuses.
6. **Peeked: nothing was read that the brief forbids.** I ran `ls` once on `DEPOSIT/` while checking that a control file I had put there was gone, and saw the file names of other groups' modules (and of `FRAGMENT-G6.md`, `FRAGMENT-G8.md`); I opened none of them and read none of their contents.
   I did not open `FLEET_DIR/work` outside `work/g9`, any other encoding of this Law, the original `skills/` of l4-ide, `jl4/examples`, `paper/`, or any directory the brief names as forbidden.
   I read `doc/concepts/legal-modeling/actors-and-actions.md` (permitted) once.
