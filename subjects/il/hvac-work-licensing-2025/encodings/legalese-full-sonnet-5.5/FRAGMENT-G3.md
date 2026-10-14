# FRAGMENT-G3: sections 12 to 18 (the duties of licensees and operators)

Written by ENCODER G3 for the fleet row `legalese-full-sonnet-5.5`.
Scope: Chapter 3, sections 12 to 18 of the Regulation of Engagement in Work on Refrigeration or Air-Conditioning Systems Law 5785-2025, 16 coverage rows, 404 words of Hebrew.
Status: draft; no domain expert has read it against the Law.
Everything below that says "checked" was run, and the numbers are in section 9.

Sources read: `inputs/law.wiki` lines 127-155 (Chapter 3), lines 59-61 (the grades), 100 (s.8), 109-119 (s.10), 207-213 (s.26), 715-721 (Third Schedule items (4) to (6)), and the gazette page images pp. 185, 186 and 205 of Sefer HaChukim 3349.
The gazette agrees with the wiki on every number and on the wording of items (4) to (6): 30 days from the day of the change (s.16), eight hours at least (s.17(a)), three months (s.17(c)).
Interpretation: `il-interpretation-time.l4` (sha256 `d1552de5...671f`, checked on the deposited copy) and `interpretation-NOTES.md` sections 3 and 4.
Independence: nothing under `commons/`, `commonswt/`, `canon/`, `il/` or `jl4/examples`, and nothing under `~/.claude` other than the two skills, was opened.

## 0. Files

| file | what it holds |
| --- | --- |
| `g3-licensee-duties.l4` | ss.12-16: the ban on transferring a licence; the duty to meet Israeli Standard 994; showing the licence; the Registrar's demand for reports; notice of a change in 30 days |
| `g3-training-duty.l4` | s.17: eight hours in the last year of validity; a particular course; extension by up to three months; the deemed licence condition; the Registrar's duties to ensure and publish |
| `g3-operator.l4` | s.18: the operator's ban on engaging the unlicensed; making sure that licensees work to the Standard; who is an operator |
| `g3-tests-licensee-duties.l4`, `g3-tests-training-duty.l4`, `g3-tests-operator.l4` | the passing tests (expected values decided from the Hebrew before the modules were run) |
| `g3-tests-red.l4` | 19 assertions that are MEANT to fail: the answer of a rejected reading put to the reading taken (section 2) |

Each module opened with `@lang en` as delivered (that line was removed on 2026-10-14; English is the default), imports only `prelude`, `daydate`, `il-interpretation-time` (not `g3-operator.l4`, which counts no period) and `domain`, and carries `@ref` with `src:` locators on every rule.
The Hebrew in comments is copied by `srcrefs.py quote`, never typed; this fragment quotes Hebrew only in section 10, by the same script.
Every rule of a duty or power is a regulative rule typed by the party and the act; every discretion (the Registrar's opinions, "regularly", "sufficient measures", "a reasonable time") is an input.

Import graph (acyclic; no module of another group is imported):
- `g3-licensee-duties` imports `prelude`, `daydate`, `il-interpretation-time`, `domain`.
- `g3-training-duty` imports `prelude`, `daydate`, `il-interpretation-time`, `domain`.
- `g3-operator` imports `prelude`, `daydate`, `domain`.
- `g3-tests-licensee-duties` imports those four and `g3-licensee-duties`; `g3-tests-training-duty` the same four and `g3-training-duty`; `g3-tests-operator` imports `prelude`, `daydate`, `domain`, `g3-operator`.
- `g3-tests-red` imports `prelude`, `daydate`, `il-interpretation-time`, `domain` and the three modules.
- The three modules import each other nowhere, because each declares its own acts and records under names that carry the section.

A `#TRACE` result cannot be compared with `EQUALS`, so each `#TRACE` in the test modules has a line `-- TRACE-EXPECT: FULFILLED`, `BREACHED | text` or `STANDING | text` above it, and `check-traces.py` (in WORK) checks the printed result against it.
The INTEGRATOR's `check.sh` should list `g3-tests-red.l4` in `expected_failed` with 19 and run the trace check, or accept that the traces are checked by hand.

The scripts are in `work/g3/` (WORK), and the module sources are templates there (`src/*.l4.tmpl`, rendered into the deposit by `render.py`, which fills every quotation marker from `inputs/law.wiki`):
- `check.sh` (the skill's script, adapted to `g3-*.l4`, with `expected_failed` 19 for `g3-tests-red.l4`);
- `python3 -I srcrefs.py check --refs inputs/law.wiki g3-licensee-duties.l4 g3-training-duty.l4 g3-operator.l4`;
- `check-traces.py l4nice FILE...` over the three passing test modules;
- `numbers-check.py` (the numbers the tests rest on, searched in the Hebrew lines of `law.wiki`);
- `mutate.py` (38 single-edit mutations run on scratch copies).

## 1. Coverage

16 rows: 16 `encoded`, 0 `inert`, 0 `refused`, 0 `out-of-scope`, **0 `deferred`**.
No disposition was changed from `slice-G3.md`.

| Law | provision | disposition | module | rule or decision |
| --- | --- | --- | --- | --- |
| 12 | A licence is personal; no transfer, no permission for another to use it | encoded | `g3-licensee-duties` | the rule `s.12 — the licensee shall not transfer the licence or permit another person to use it` (two SHANT, joined by RAND); the decisions `s.12 — a transfer of the licence to the person breaches section 12` and `s.12 — permitting the person to use the licence breaches section 12` |
| 13 | Work to parts 4 and 5 of Israeli Standard 994, as their wording is from time to time | encoded | `g3-licensee-duties` | the rule `s.13 — the licensee shall do the work in accordance with parts 4 and 5 of Israeli Standard 994` (SHANT of the converse; the text's own MUST form is the alternative `s.13 — the licensee must perform the work ..., in the text's own form`); the decisions `s.13 — the licensee breached section 13` and `s.13 — the listed violation committed under section 13`; the record `s.13 — the violation committed under section 13` |
| 14 | Show the licence to the orderer of the work, on demand | encoded | `g3-licensee-duties` | the rule `s.14 — the orderer of the work may demand to see the licence, and the licensee must then show it` (MAY, HENCE MUST); the decisions `s.14 — the licensee must show the licence` and `s.14 — the licensee breached section 14` |
| 15 | The Registrar may demand a report, information or documents; the licensee must supply them | encoded | `g3-licensee-duties` | the rule `s.15 — the Registrar may demand a report, information or documents, and the licensee must supply them` (MAY, HENCE MUST WITHIN the days to the day directed); the decisions `s.15 — the Registrar has the power to make the demand`, `s.15 — the licensee must comply with the demand`, `s.15 — the condition for renewing or extending the licence is satisfied` |
| 16 | Notify the Registrar of a change in the application particulars within 30 days from the day of the change | encoded | `g3-licensee-duties` | the rule `s.16 — the licensee must notify the Registrar of a change in the application particulars` (MUST WITHIN the days to the last day counted under IL s.10(a), (c)); the decisions `s.16 — the licensee gave notice of the change in time` and `s.16 — the licensee breached section 16 as at` |
| 17 | Continuing training (container) | encoded | `g3-training-duty` | see 17(a) to (f) |
| 17(a) | At least eight hours in the last year of validity, and meet the requirements | encoded | `g3-training-duty` | the rule `s.17(a) — the licensee must attend eight hours of qualifying training in the last year of validity`; the decisions `s.17(a) — the training duty of section 17(a) was met`, `s.17(a) — the day is in the last year of validity`, `s.17(a) — the session counts towards the eight hours` |
| 17(b) | The Registrar may require a particular course, after consulting the Council; reasonable notice | encoded | `g3-training-duty` | the rule `s.17(b) — the Registrar may require attendance at a particular course` (MAY, HENCE MUST WITHIN the days from the notice to the course); the decisions `s.17(b) — the Registrar has the power to require attendance at the course`, `s.17(b) — the licensee must attend the course`, `s.17(b) — the licensee breached the duty to attend the course as at` |
| 17(c) | The Registrar may extend validity by up to three months, after consulting the Council | encoded | `g3-training-duty` | the rule `s.17(c) — the Registrar may extend the validity of the licence by up to three months` (MAY); the decisions `s.17(c) — the Registrar may extend the validity of the licence` and `s.17(c) — the latest last day of validity after an extension of up to three months from` |
| 17(d) | The duty to attend and meet the requirements is deemed a licence condition | encoded | `g3-training-duty` | the decisions `s.17(d) — the licence condition of section 17(a) was breached as at`, `... of section 17(b) ...`, and `s.17(d) — the licensee breached a licence condition through the training duty as at`; a deeming is a decision, not a duty, so it has no regulative rule |
| 17(e) | The Registrar must ensure that trainings exist and are available | encoded | `g3-training-duty` | the rule `s.17(e) — the Registrar must ensure that the trainings exist and are available` (MUST, no deadline); the decision `s.17(e) — the Registrar has ensured that the trainings exist and are available` |
| 17(f) | The Registrar must publish the trainings a reasonable time before them | encoded | `g3-training-duty` | the rule `s.17(f) — the Registrar must publish the trainings on the Ministry website` (MUST, no deadline); the decision `s.17(f) — the Registrar published the training in good time` |
| 18 | Duties of an operator (container) | encoded | `g3-operator` | see 18(a) to (c) |
| 18(a) | An operator shall not engage a person who lacks a licence of the appropriate kind | encoded | `g3-operator` | the rule `s.18(a) — the operator shall not engage a person in work on a cooling system without a licence of the appropriate kind` (SHANT); the decisions `s.18(a) — the operator may engage the person`, `s.18(a) — the operator breached section 18(a)`, `s.18(a) — the listed violation committed under section 18(a)`, and the record `s.18(a) — the violation committed under section 18(a)` |
| 18(b) | The operator shall make sure that the licensees he engages work to the Standard of s.13 | encoded | `g3-operator` | the rule `s.18(b) — the operator must make sure that the licensee works to the Standard` (MUST, no deadline); the decisions `s.18(b) — the operator took the section 18(b) steps` and `s.18(b) — the operator breached section 18(b)` |
| 18(c) | Definition of "operator" | encoded | `g3-operator` | `s.18(c) — the person is an operator` |

Named refusals carried inside encoded rows (each is returned in the position of the answer, so it is forced): `s.13 — no wording of Israeli Standard 994 in force on the day the work is judged against was supplied`, `s.15 — the day the Registrar directed for compliance precedes the day of the demand`, `s.17(b) — notice of the requirement was given after the day of the course`, and, for the alternative reading S18-D only, `s.18(c) — the word operator in Third Schedule items (5) and (6) is defined only for section 18, so the items cannot be applied`.

## 2. Forks

Each fork gives the readings, the one taken, the text that licenses each (the Hebrew is quoted in section 10), and the callable alternative with its test.
A "red row" is an assertion in `g3-tests-red.l4` that puts the alternative's answer to the reading taken and fails exactly where they part.
Assumed, not ruled: every reading taken below is this encoder's choice, and each is meant to be reverted alone.

### 2.0 One fork for every kind of period met (brief ruling 4)

G3 meets kinds D, V, B, N, X and Q.
It meets no kind C (a commencement counted from another date) and no kind W (a window for an application or request).

**S16, kind D (a deadline for doing something): s.16, 30 days from the day of the change.**
Readings: (1) IL s.10(a) and IL s.10(c) (the brief's default for a deadline: the period does not end on a day of rest, recess or holiday, and then ends on the first later day that is not one); (2) IL s.10(a) alone.
Taken: (1).
Why: the Law's own words make s.16 a time within which a person must act (text 10.5); IL s.10(a) leaves the day of the change out, so the days are D+1 to D+30, and IL s.10(c) is unqualified.
The calendar of rest days is IP15, an input; no holiday is computed; with several rest days in a row the time module's reading (its fork F3, the period runs to the first later day that is not a rest day) is used.
Alternative, callable: `s.16 — the last day for notifying the Registrar, counting only IL s.10(a), of a change made on`.
Tests: change of 1 March 2026 gives 31 March 2026 under (2), and under (1) 31 March with no rest days, 1 April with 31 March a rest day, 2 April with 31 March and 1 April both rest days, 31 March when only 15 March or only 1 April is a rest day; red rows R1 and R2.
The WITHIN of the rule is the number of days to the last day (30, 31, 32), so a trace counts under the reading taken.

**S15, kind X (a time an official fixes): s.15, "as he directed".**
Readings: the Registrar directs a day by which the report or supply is to be made (taken); or he directs a number of days.
Taken: an input date, `the day the Registrar directed that the report or supply be made by` (a `MAYBE DATE`), never counted, so there is no IL s.10 question; NOTHING is no time limit, because the text states none.
The number of days to it, from the day of the demand (not counted), is the WITHIN of the licensee's duty; a directed day before the day of the demand is a named refusal.
A directed number of days would be a kind D period counted by IL s.10(a), (c); it is not modelled because the text gives no unit.
Tests: 1 to 15 March 2026 is 14 days; the same day is 0; NOTHING is NOTHING; a day before is refused; traces at day 14 (FULFILLED) and 15 (BREACHED).

**S17-B, kind B (counted backwards): s.17(a), "the last year of the validity".**
IL s.10 counts forwards only, so it does not cover this and no function of the time module is used.
Reading taken: the days after the same day one year earlier than the last day of validity, up to and including the last day; found by plain comparison of dates (`s.17(a) — the same day one year earlier than`, clamped to the month's last day when the month lacks the day, IL s.10(b)'s clamp used by analogy).
For 31 March 2030 the window is 1 April 2029 to 31 March 2030, both ends inside.
The clamp matters only for an anchor of 29 February, where the window starts on 1 March of the year before (a rolled date, 2 March, would shorten it by a day: rejected as the time module's F25 rejects rolling).
No callable alternative for the clamp: no source text bears on it, and it changes one day for 29 February anchors only.
Tests: the anniversary day (31 March 2029) is out, 1 April 2029 in, 31 March 2030 in, 1 April 2030 out; 29 February 2028 starts 1 March 2027.

**S17-V, kind V (a period of validity): s.17(c), "not exceeding three months".**
Readings: (1) three calendar months counted forwards from the last day of validity by IL s.10(b), without IL s.10(c) (the brief's default: a period of validity is not a time to act); (2) the same with IL s.10(c), so a cap that falls on a day of rest moves.
Taken: (1).
Why: applying IL s.10(c) would lengthen a licence by a rest day; "not exceeding" is a cap, and the length actually granted is an input.
Alternative, callable: `s.17(c) — the latest last day of validity, with IL s.10(c) applied, after an extension of up to three months from`.
Tests: 31 March 2030 gives 30 June 2030; 31 January 2030 gives 30 April 2030 (clamp); 30 November 2030 gives 28 February 2031; with 30 June a rest day the alternative gives 1 July, with 30 June and 1 July 2 July; red row R9.

**S17-N, kind N (vague time): s.17(b) and s.17(f), "a reasonable time before".**
Not a period; no number is invented.
Taken: an input judgement on the record (`notice was given a reasonable time before the date of the course`; `the publication was a reasonable time before the training`), together with the one thing the text fixes: the publication precedes the training and the notice precedes the course.
No callable alternative (a numeric reading would be an invention).

**S17-Q, kind Q (a quantity): s.17(a), "eight hours at least".**
A constant, 8; "at least" is inclusive.
Tests: 8 hours met, 7.99 and 7.5 not met, 9 met, 4 and 4 met, 4 and 3 not.

### 2.1 Forks of substance

**COM (commencement; trap T20): ss.12, 15, 16 and 17.**
s.63(a) fixes the commencement of the Law (but for Chapter 6) only "for the performance of work on a system".
Ss.13, 14 and 18 are about such work and take the standard input `the Law has commenced for the work on the system` (IP2) as it is named.
Ss.12, 15, 16 and 17 are about a licensee, not one piece of work; the sources do not say when they commence (interpretation NOTES F26 found no default day).
Taken: the same input is read there as "the Law has commenced for the licensee's work" and gates the duty.
Alternative, callable by passing TRUE: no commencement gate.
The Registrar's duties of 17(e) and 17(f) take no gate, because they concern the training and not any work.
Tests: every duty function is asserted both ways (commenced TRUE and FALSE).

**S13a (the Standard "as its wording is from time to time"): s.13.**
Readings: (1) the work is judged against the wording in force on the day it was done; (2) against the wording in force on the day it is inspected.
Taken: (1).
Why: the work's lawfulness cannot depend on a later amendment; the wording "from time to time" is read at the time of the act.
The Standard is not in the sources: each wording is an input carrying the day it took effect and the findings on the work (`Wording of Israeli Standard 994`); the latest wording that took effect on or before the day is chosen; none in force is a named refusal.
The wordings used in the tests are illustrations.
Alternative, callable: `s.13 — the licensee breached section 13, judged against the wording in force on the day of the inspection`.
Tests: a work of 31 December 2025 is judged by the 2020 wording (no breach) and one of 1 January 2026, the day the 2026 wording took effect, by the 2026 wording (breach); the alternative with an inspection on 1 June 2026 finds a breach for the first; the order in which the wordings are supplied changes nothing; red row R3.

**S13b (the form of s.13): "shall perform in accordance with".**
Readings: (1) a prohibition of work not in accordance (SHANT, no deadline); (2) the text's own MUST, with no deadline.
Taken: (1), because a MUST with no deadline cannot be breached in a trace, and the sentence is a constraint on how work is done and not a duty to do work.
Alternative, callable: `s.13 — the licensee must perform the work in accordance with parts 4 and 5 of Israeli Standard 994, in the text's own form`.
Tests: two traces show that the conforming work discharges it and the non-conforming work leaves it standing, never breached.

**S13c (s.13 against Third Schedule item (4)): trap T13.**
Item (4) prices one failure: a licensee who installed a cooling system without a tightness test of the refrigerant piping under the testing chapter of part 4 of the Standard.
Every other breach of s.13 is a breach with no row; the sources give no amount and none is invented.
So `s.13 — the licensee breached section 13` and `s.13 — the listed violation committed under section 13` are two decisions; NOTHING from the second means "no Third Schedule row", never "no breach".
Tests: installation without the test gives item (4); maintenance without it, an installation with another defect in part 4, and an installation failing part 5 only are breaches with NOTHING.
Second point: item (4) names the Standard's title as enacted ("Air conditioners: installation"), while s.13 follows the Standard from time to time.
Taken: the tightness test is judged against the wording in force on the day of the work.
Alternative, callable: `s.13 — the listed violation committed under section 13, the testing chapter being that of the wording in force on a fixed day` (the day the Law was published, an input).
Tests: an installation of 10 March 2026 gives NOTHING under the reading taken (the 2026 wording is in force and the test was performed under it) and item (4) with the fixed day 14 January 2025 (the 2020 wording); a fixed day before every wording is refused; red row R16.

**S14 (s.14, when failure to show begins).**
The duty arises with the orderer's demand (the words "on his demand", text 10.3) and no time is stated.
Taken: the licensee's duty stands from the demand until he shows the licence, with no WITHIN (the orderer's demand is a MAY: an orderer who never demands has used a liberty, not failed in a duty); the input `the licensee failed to show the licence on the demand` carries the judgement that failure has begun.
No callable alternative: another reading would invent a time.
Tests: demanded and refused is a breach; demanded and shown is not; no demand is no duty; a stranger's demand is no duty; traces.

**S15b (s.15, whether the duty to comply reaches a report).**
The last clause of s.15 says "the licensee shall supply to him the information or documents as stated"; it does not name the report.
Readings: (1) the duty reaches a demand for a report too; (2) only what the clause names.
Taken: (1), since a power to demand a report that bound nobody would be empty.
Alternative, callable: `s.15 — the licensee must comply with the demand, the express duty reaching only information or documents`.
Tests: a report demand binds under (1) and not under (2); a documents demand binds under both; red row R18.

**S16b (s.16, what counts as giving notice).**
The notice must be "in the manner the Registrar directs", and the sources do not say whether the day is that of dispatch or of receipt.
Taken: the input is the day the notice was given to the Registrar; a notice not in the manner directed does not count (it does not match the act), so the duty runs on.
No callable alternative.
Tests: directed and followed counts, directed and not followed does not, not directed means the flag is irrelevant; traces.

**S17-A (s.17(a), the window and an extension under (c)).**
Readings: (1) the last year is counted back from the last day of validity before any extension and closes on the last day as extended, so training attended during the extension counts; (2) the whole window moves with the extension.
Taken: (1), since the extension is given "so as to fulfil the duty".
Alternative, callable: `s.17(a) — the training duty was met, the last year counted back from the last day as extended`.
Tests: with L = 31 March 2030 extended to 30 June 2030, 1 April 2030 and 30 June 2030 count and 1 July 2030 does not; a session of 10 April 2029 counts under (1) and not under (2); red row R4.

**S17-C (s.17(b), "in addition to the trainings under (a)").**
Readings: (1) a course required under (b) does not count towards the eight hours of (a); (2) it counts.
Taken: (1).
Alternative, callable: `s.17(a) — the training duty was met, counting a course required under section 17(b) as well`.
Tests: eight hours that are a (b) course are not enough under (1) and enough under (2); red row R5.

**S17-D (s.17(a), "and shall meet the requirements of those trainings").**
Readings: (1) the requirements limb reaches every session that qualifies; (2) a session counts only if its requirements were met, and the limb adds nothing.
Taken: (1).
Alternative, callable: `s.17(a) — the training duty was met, a session counting only if its requirements were met`.
Tests: eight met hours plus two qualifying hours not met is not enough under (1) and enough under (2); a non-qualifying session with requirements unmet does not trouble (1); red row R6.

**S17-E (s.17(a) with (e), no training available).**
Ss.17(a) and (e) each stand alone: the sources give the licensee no excuse when the Registrar failed to ensure the trainings.
Taken: no excuse (the Registrar's remedy for the licensee is the extension of (c)).
Alternative, callable: `s.17(a) — the training duty was met, or no qualifying training was available`.
Tests: with no sessions, not met under the reading taken and met under the alternative when no training was available; red row R7.

**S17-F (s.17(b), reasonable notice).**
Readings: (1) reasonable notice is a condition of the licensee's duty to attend; (2) it is a duty of the Registrar and its lack does not undo the requirement.
Taken: (1), because a licensee cannot be bound to attend a course he was not told of in time.
Alternative, callable: `s.17(b) — the licensee must attend the course, whether or not notice was given a reasonable time before`.
Tests: notice the day before, judged not reasonable: the power stays, the duty does not under (1) and does under (2); red row R8.

**S17-T (s.17(c), when the decision may be taken).**
Readings: (1) on or before the last day of validity as it stands (the power is over the validity of a licence that still has validity, and "licensee" means a holder of a licence); (2) at any time, even after the validity ran out.
Taken: (1).
Alternative, callable: `s.17(c) — the Registrar may extend the validity of the licence, whenever the decision is taken`.
Tests: a decision on 31 March 2030 is in time, on 1 April 2030 it is not under (1) and is under (2); red row R11.

**S17-V2 (s.17(c), several extensions).**
Readings: (1) each extension is for "a period not exceeding three months" counted from the last day of validity as it stands, and the text limits no number of extensions; (2) the three months are cumulative from the last day before any extension.
Taken: (1).
Alternative, callable: `s.17(c) — the Registrar may extend the validity of the licence, the three months being cumulative`.
Tests: after a first extension to 30 June 2030, a second to 30 September 2030 is allowed under (1) and refused under (2); red row R10.

**S17-M (s.17(c) against s.8: trap T25).**
Readings: (1) the extension may pass 31 March of the fifth year, the limit of s.8, because (c) extends the "validity period" that s.8 defines and only an extension can lengthen it; (2) it may not pass the limit of s.8 (an input date).
Taken: (1).
Alternative, callable: `s.17(c) — the Registrar may extend the validity of the licence, no later than the limit of section 8`.
Tests: a licence ending 31 March 2030 extended to 30 June 2030 is allowed under (1) and refused under (2) with the limit 31 March; a licence ending 15 March 2030 extended to 1 April 2030 is refused under (2) with that limit; extended to 31 March, or with a limit of 30 June, it is allowed; red row R12.

**S17-d (s.17(d), when the deemed condition is breached; trap T12).**
Readings: (1) the duty of (a) is breached only when its window has closed without the eight hours and the requirements, and the duty of (b) when the day of the course has passed; (2) the condition binds from the first day of the last year, so the licensee is in breach of it on every day of the last year until the eight hours are met.
Taken: (1), because under (2) s.3(a) ("in accordance with the conditions of his licence") would bar every licensee from work for the whole of his last year.
The output is the value of IP8, the input `the licensee breached a licence condition` of G1 (s.3(a), s.10(a)(3)) and G2.
Alternative, callable: `s.17(d) — the condition of section 17(a), read as binding from the first day of the last year, was breached as at`.
Tests: as at 1 October 2029, with no sessions, a breach under (2) and none under (1); not before 1 April 2029; not once the eight hours are met; red row R19.

**S17-W (s.17(a), a licence whose term is shorter than a year).**
Section 9 lets a temporary licence run for up to a year; "the last year of its validity" is then shorter than the twelve months counted back.
Taken: a session counts only if the licence was in force on the day attended (a field of the session), so training before the licence began is not credited.
Alternative: set that field TRUE for the session.
Tests: a six-month licence from 1 April 2030: training of 20 March 2030 does not count; 4 hours before plus 4 after are not eight; with the field TRUE they are.

**S18-B (s.18(b), conduct or result).**
Readings: (1) a duty of conduct: the operator must take measures sufficient to make sure that the licensee works to the Standard, and sufficiency is a judgement; (2) a duty of result: breached whenever an engaged licensee did not work to the Standard.
Taken: (1), because the text's means include sample checks (text 10.7), which cannot guarantee a result, and the means are listed "inter alia" as ways of making sure.
Alternative, callable: `s.18(b) — the operator breached section 18(b), the duty being one of result`.
Tests: sufficient measures with a licensee whose work failed: no breach under (1), a breach under (2); insufficient measures with a licensee who conformed: a breach under (1), none under (2); red row R15.

**S18-C (s.18(c), "including an owner or manager of a business").**
Readings: (1) the business limb is a limb of its own: an owner or manager of a business offering the work to the public is an operator by that status, and a person who regularly engages another is one too; (2) "including" only illustrates the first limb.
Taken: (1), because each limb of the text then has a place in the encoding and (2) would leave the second limb with no effect.
Alternative, callable: `s.18(c) — the person is an operator, the business limb being only an illustration`.
Discriminating case: an owner of a business offering the work to the public who engages an unlicensed person once, not regularly: an operator under (1), so a breach of s.18(a) (item (5)); not under (2).
The operator's own licence is irrelevant ("whether he holds a licence or not"), so it is no input.
Tests: the four combinations of the two facts under both readings; the discriminating case; red row R14.

**S18-D (s.18(c) against the Third Schedule).**
s.18(c) defines "operator" "in this section", and Third Schedule items (5) and (6) use the word.
Readings: (1) the word of the items is the operator of s.18(c) (the items are "contrary to s.18(a)"); (2) the definition does not reach the items, which then use an undefined word and cannot be applied.
Taken: (1).
Alternative, callable: `s.18(a) — the listed violation committed under section 18(a), the word operator of the Third Schedule being undefined`, a named refusal.
Tests: asserted refused with its message; red row R17.

**S18-H (s.18(a) against Third Schedule items (5) and (6)).**
The two items partition the duty: (5) a person who has no licence at all, (6) one with a licence not of the appropriate kind.
Readings: (1) a person has a licence when it is in force, so no kind in force is item (5), and a kind in force that does not fit is item (6); (2) a licence held but not in force (expired, revoked, suspended) is still a licence "in his hand", so item (5) needs that the person holds no licence of any kind.
Taken: (1), since the Law speaks of persons who "hold" a licence for the purpose of doing work (s.2: a licensee is a holder of a licence to perform work).
Alternative, callable: `s.18(a) — the listed violation committed under section 18(a), a licence held but not in force being a licence held`.
Tests: a lapsed grade 1 licence on a 25 kW system is item (5) under (1) and item (6) under (2); no licence at all is item (5) under both; a licence in force that does not fit is item (6) under both; red row R13.

## 3. Answer table

All values were asserted by the passing tests; the wordings of Standard 994 and the calendars of rest days are illustrations.

| scenario | answer | section |
| --- | --- | --- |
| A licensee transfers his licence to another person, or lets another person use it | breach of s.12; transfer to himself (same reference) is not | s.12 |
| Before the Law has commenced for his work, the same transfer | no breach | s.12, s.63(a), fork COM |
| Work of 31 December 2025, wordings of 2020 (all conformed) and 2026 (part 5 not met, in force from 1 January 2026) | no breach of s.13: the 2020 wording governs | s.13, fork S13a |
| The same work on 1 January 2026 | breach of s.13: the 2026 wording governs | s.13 |
| Installation without the tightness test of the testing chapter of part 4 | breach of s.13 and listed violation `installation without the tightness test of the piping` | s.13, Third Schedule (4) |
| Maintenance without that test | breach of s.13; no listed violation | s.13, Third Schedule (4) |
| Orderer demands to see the licence and the licensee refuses | breach of s.14 | s.14 |
| Nobody demands, or a stranger demands | no duty | s.14 |
| Demand of the Registrar dated 1 March 2026, directed for 15 March 2026 | 14 days; supply on day 14 in time, day 15 breach | s.15 |
| Demand with no day directed | no time limit; the duty stands | s.15 |
| Demand for a report whose particulars do not concern the engagement | no power | s.15 |
| Change on 1 March 2026, no rest days | last day 31 March 2026; notice on 31 March in time, on 1 April late | s.16, IL s.10(a) |
| The same, 31 March a rest day | last day 1 April 2026 (31 days) | s.16, IL s.10(c) |
| The same, 31 March and 1 April rest days | last day 2 April 2026 (32 days) | s.16, IL s.10(c) |
| Change on 31 January 2026 | last day 2 March 2026 | s.16, IL s.10(a) |
| Licence ending 31 March 2030: one session of 8 hours on 1 April 2029 | duty met | s.17(a) |
| The same session on 31 March 2029 | not met: the anniversary day is outside the last year | s.17(a) |
| 7.5 hours; 7.99 hours | not met | s.17(a) |
| 8 qualifying hours, requirements met, plus 2 qualifying hours not met | not met (taken); met (alternative S17-D) | s.17(a), fork S17-D |
| 8 hours that are a course required under (b) | not met (taken); met (alternative S17-C) | s.17(a), s.17(b), fork S17-C |
| Course on 10 June 2027, notice 1 May 2027 | 40 days; attend on day 40 in time, day 41 breach | s.17(b) |
| Notice not a reasonable time before the course | power stays; the duty to attend does not (taken) | s.17(b), fork S17-F |
| Extension from 31 March 2030 | at most to 30 June 2030; 1 July refused | s.17(c), IL s.10(b) |
| Extension to 30 June 2030 of a validity ending 31 March | allowed (taken); refused under the limit of s.8 (alternative S17-M) | s.17(c), s.8, fork S17-M |
| Decision to extend on 1 April 2030 of a validity ended 31 March 2030 | refused (taken) | s.17(c), fork S17-T |
| Window closed 1 April 2030, no 8 hours | a licence condition is breached | s.17(d), s.3(a), s.10(a)(3) |
| Operator engages a grade 1 licensee for a 25 kW system | breach of s.18(a); listed violation item (6) | s.18(a), Third Schedule (6) |
| Operator engages a person with no licence in force | listed violation item (5) | s.18(a), Third Schedule (5) |
| Operator engages a grade 2 licensee for a 25 kW system | permitted | s.18(a) |
| Measures judged insufficient to make sure of the Standard | breach of s.18(b) (conduct, taken) | s.18(b), fork S18-B |
| Owner of a public business, no regular engagement | an operator (taken) | s.18(c), fork S18-C |

## 4. Nouns requests for the INTEGRATOR

`domain.l4` is read-only, so each noun below is declared locally in the module that uses it, with the name and fields shown.
The INTEGRATOR may move them to `domain.l4`; none clashes with a name in it.

| noun | module | fields (names) | used by |
| --- | --- | --- | --- |
| `Wording of Israeli Standard 994` | `g3-licensee-duties` | the day it took effect; conformed to part 4; tightness test performed; conformed to part 5 | G6 (item (4)) |
| `Demand of the Registrar under section 15`, `Kind of demand under section 15` | `g3-licensee-duties` | kind; particulars concern the engagement; the Registrar's opinion that they are needed; made as a condition of renewal or extension; the day of the demand; the day directed | G1, G2 (the renewal condition) |
| `Demand to see the licence` | `g3-licensee-duties` | the person ordered the work; demanded; the licensee failed to show | none |
| `Change in the application particulars` | `g3-licensee-duties` | the particular was one given in the application; the day of the change; a manner directed; the notice followed it; the day the notice was given | none |
| `Training session attended`, `Particular course required under section 17(b)`, `Extension of validity under section 17(c)`, `Training offered` | `g3-training-duty` | see the module | G1, G2 (the breach of the licence condition; the extension) |
| `Facts about a person who engages others in work on cooling systems`, `Measures the operator took under section 18(b)` | `g3-operator` | regular engagement; owns or manages a business offering the work to the public; sufficiency of measures | G6 |
| `Act under sections 12 to 16 of the Law`, `Act under section 17 of the Law`, `Act under section 18 of the Law` | the three modules | the acts of the regulative rules | none |

Two requests that touch `domain.l4`:
1. The `Licence` record carries `validity ends on, as recorded` but not the first day of the current term; s.17(a) takes the days the licence was in force as a field of each session, which is a workaround.
2. A `Party` for "the engaged person" is not needed; the persons engaged appear as lists of licence kinds in force.

## 5. Inputs consumed and functions exported

### Standard inputs (names as in PLAN section (c), exact `GIVEN` names)

| IP | `GIVEN` name | type | used in |
| --- | --- | --- | --- |
| IP1 | `licence kinds in force on the day` | LIST OF `Licence kind` | ss.12-16 (the licensee on the day of the act), s.18 (the person engaged, on the day of the engagement) |
| IP2 | `the Law has commenced for the work on the system` | BOOLEAN | every duty and power; see fork COM |
| IP3 | `licence kinds that cover the system` (G1's `licence kinds that cover a cooling system`) | LIST OF `Licence kind` | s.18(a) |
| IP4 | `the act is work on a cooling system`; the job kind is `Work item`'s `the kind of job` | BOOLEAN; `Job kind` | ss.13, 14, 18 |
| IP7 | the Council's consultation: fields `the Council was consulted about requiring the course`, `the Council's advice about requiring the course was validly given`, `the Council was consulted about the extension`, `the Council's advice about the extension was validly given` | BOOLEAN | s.17(b), (c) |
| IP15 | `Calendar of rest days` (through `days of rest, recess or holiday listed in`) | domain record | s.16 |
| IP17 | the Registrar's opinions, fields `in the Registrar's opinion ...` | BOOLEAN | ss.15, 17(b), 17(c) |
| IP19 | `the last day of validity` (the G2 date; here `anchor` and `closing` of s.17(a), and the fields of the extension) | DATE | s.17 |

Everything else is a fact on a record (sessions, courses, the demand, the change, the facts about a person who engages others) or the wordings of Israeli Standard 994.

### Functions exported to the INTEGRATOR (the `@export`ed ones are marked; every other function is a plain rule or decision)

| function | what it answers | for |
| --- | --- | --- |
| `s.16 — the licensee gave notice of the change in time` (export) | BOOLEAN | the PLAN's `the licensee gave notice of the change in time` |
| `s.16 — the licensee breached section 16 as at` (export) | BOOLEAN | |
| `s.13 — the licensee breached section 13` (export) | BOOLEAN | |
| `s.13 — the listed violation committed under section 13` (export) | MAYBE `Listed violation` | IP9, G6 |
| `s.13 — the violation committed under section 13` (export) | MAYBE `Violation` | IP9, G6 |
| `s.12 — a transfer of the licence to the person breaches section 12` (export) | BOOLEAN | |
| `s.17(a) — the training duty of section 17(a) was met` (export) | BOOLEAN | the PLAN's `the training duty was met` |
| `s.17(c) — the Registrar may extend the validity of the licence` (export) | BOOLEAN | the PLAN's `the validity may be extended`; IP19: G2 takes the extended last day |
| `s.17(d) — the licensee breached a licence condition through the training duty as at` (export) | BOOLEAN | IP8: the value of G1's and G2's input `the licensee breached a licence condition` |
| `s.18(a) — the operator may engage the person` (export) | BOOLEAN | the PLAN's `the operator may engage the person` |
| `s.18(a) — the listed violation committed under section 18(a)` (export) | MAYBE `Listed violation` | IP9, G6 |
| `s.18(a) — the violation committed under section 18(a)` (export) | MAYBE `Violation` | IP9, G6 |
| `s.18(b) — the operator took the section 18(b) steps` (export) | BOOLEAN | the PLAN's `the operator took the s.18(b) steps` |
| `s.18(c) — the person is an operator` (export) | BOOLEAN | |

The PLAN suggested one function `the violation committed` for ss.13 and 18(a); the names above carry the section so that no name clashes with G1 and G5.
Every duty has its regulative rule as well (section 1); the rules are not exported, because a `DEONTIC` is exercised with `#TRACE`.

## 6. Contradictions in the source

Found by a separate pass after the encoding, reading ss.12 to 18 again with the schedules and the neighbouring sections (ss.2, 3, 5, 8, 9, 10, 26, the Third Schedule).
A **contradiction** is two provisions (or two limbs) answering one question differently; a **gap** is a place where the text is silent; both are listed, and only the first has two callable readings.

| id | provisions | discriminating case | readings | callable |
| --- | --- | --- | --- | --- |
| C1 | s.8 ("until 31 March of the fifth year") against s.17(c) (extend the validity by up to three months) | a licence ending on 31 March 2030 extended to 30 June 2030 | s.17(c) prevails (taken) / s.8's limit caps the extension | S17-M, tested; red row R12 (trap T25) |
| C2 | s.18(c) (operator defined "in this section") against Third Schedule items (5), (6) (use the word) | any operator violation priced by item (5) or (6) | the definition reaches the items (taken) / it does not, and the items cannot be applied | S18-D, tested (refusal); red row R17 |
| C3 | s.18(c) internally: "regularly" against "including an owner or manager of a business offering the work to the public" | the owner of such a business who engages an unlicensed person once | the business limb stands alone (taken) / it only illustrates regular engagement | S18-C, tested; red row R14 |
| C4 | s.17(c) ("a licensee who has not fulfilled his duty") against the time the duty falls due ((a): the end of the last year) | a decision on the day after the last day of validity | the decision must be taken while the licence is valid (taken) / any time | S17-T, tested; red row R11 |
| C5 | s.17(b) ("in addition to the trainings under (a)") against s.17(c) and (d) ("(a) or (b)") | eight hours that are a (b) course | they do not count towards (a) (taken) / they do | S17-C, tested; red row R5 |
| C6 | s.13 ("as their wording is from time to time") against Third Schedule item (4) (names the chapter and the title of part 4 as enacted) | an installation under a wording that moved the tightness test | the wording of the day of the work (taken) / the wording fixed at a day | S13c, tested; red row R16 |
| C7 | the heading of s.15 ("duty to report") against its body (the express duty is to supply "the information or documents") | a demand for a report that the licensee ignores | the duty reaches reports (taken) / only information or documents | S15b, tested; red row R18 |
| C8 | s.17(a) ("the last year of its validity") against s.9 (a temporary licence runs for up to a year) | training before a six-month licence began | the licence must be in force on the day attended (taken) / the twelve months back count | S17-W, tested |
| C9 | s.3(a) (work not in accordance with the conditions of the licence is forbidden) with s.17(d) (the training duty is a condition) against the Third Schedule (prices only no licence or the wrong kind) | a licensee who missed a course required under (b) and keeps working | forbidden by s.3(a) but with no row: a gap in the sanctions (trap T12) | S17-d (when the condition is breached), tested; red row R19; the missing sanction row is a gap: an amount would be invented |
| C10 | s.26(b) (a subcommittee may take the Council's powers "under (a)(3)", which lists the extension of validity) against s.17(b) (the Council's advice on requiring a course, not listed in (a)(3)) | advice on a required course given by a subcommittee | on the text the delegation reaches s.17(c) and not s.17(b); G4 decides IP7 | none here; passed to the INTEGRATOR with IP7 |
| C11 | s.17(c) extends the END of validity; a (b) duty can fall due on any day | a course missed in the second year of a five-year licence | the extension at the end cannot cure it unless the course is offered again in the extension | none: a gap |
| C12 | s.15 (a report on particulars "as he directed") against s.16 (30 days to notify a change) | a change notified on day 20 after the Registrar directed a report within 10 days | s.16's period is a floor for a duty with no demand; a demand may set a shorter time | none: an overlap, not a conflict |
| C13 | drafting: in s.13 the participle "listed in the First Schedule" is feminine singular and can agree with "work" or with "system" (text 10.2) | work listed in the First Schedule | the First Schedule lists actions, not systems, so it is read of the work | none: the input `the act is work on a cooling system` carries it |

One more point found in the same pass, not a contradiction: s.15 speaks of "renewal or extension of a licence", and the only extension of a licence the Law gives is s.17(c)'s (s.8 and s.9(b) speak of renewal; s.26(a)(2) and (3) list "extension of its validity" among the Council's matters, and nowhere else).
The word "extension" in s.15 is therefore read as the extension of s.17(c); `s.15 — the condition for renewing or extending the licence is satisfied` carries both and the INTEGRATOR passes it to G2 (s.8, s.9(b)) for renewal and to the s.17(c) rule for extension.

## 7. Open questions for a domain expert

1. May an extension under s.17(c) pass 31 March of the fifth year, and may the Registrar extend more than once (S17-M, S17-V2)?
2. Is s.18(b) a duty of conduct or of result (S18-B)?
3. Is the owner of a business offering the work to the public an operator even if he does not regularly engage anyone (S18-C), and does the s.18(c) definition govern Third Schedule items (5) and (6) (S18-D)?
4. Is a licence that is held but not in force "in the hand" of the person for items (5) and (6) (S18-H)?
5. Which wording of Standard 994 governs, and what does item (4) mean when the Standard is amended (S13a, S13c)?
6. Does an extension move the window of the last year, and do hours attended during an extension count (S17-A)?
7. Does a course required under (b) count towards the eight hours (S17-C)?
8. Does the duty to meet "the requirements" reach every session or only those counted (S17-D)?
9. Is a licensee excused when no qualifying training was available (S17-E)?
10. Is reasonable notice of a (b) course a condition of the duty (S17-F)?
11. Does s.17 apply to a temporary licence of a foreign expert, and how is the last year counted for a term shorter than a year (S17-W)?
12. When do ss.12, 15, 16 and 17 commence for a person who is a licensee (COM)?
13. Does the licensee's duty in s.15 reach a demand for a report (S15b)?
14. Is the day of notice under s.16 the day of dispatch or of receipt (S16b)?
15. Under s.26(b), may a subcommittee give the Council's advice under s.17(b) (C10)?
16. A licensee who breached the training condition under (b) and keeps working: what follows under s.3(a), given that the Third Schedule has no row (C9)? And is the deemed condition of (a) breached only when its window has closed (S17-d)?
17. Does s.5(b) (information from an applicant for renewal) or s.15 (from a licensee, "including as a condition for renewal or extension") govern a licensee who has applied for renewal, given their different thresholds?

## 8. What the sources do not answer

Each is an input or a named refusal in the encoding; none has a default.
- The text of Israeli Standard 994 parts 4 and 5, the title of part 5, and the testing chapter of part 4 (ss.13, Third Schedule (4)): conformity is a finding on the work, per wording.
- When a given wording of the Standard took effect; this is a field of each wording.
- The Registrar's directions: the dates of the trainings (s.17(a)), the manner of the notice of a change (s.16), the day for a report (s.15).
- What "regularly" (s.18(c)), "sufficient measures" (s.18(b)), "a reasonable time" (s.17(b), (f)), "special cases and justified circumstances" (s.17(c)), "circumstances that justify" and "required for the training" (s.17(b)) mean: judgements and opinions, inputs.
- Whether a session is "in the licensee's field of work under his licence": a fact on the session.
- What "the requirements of the training" are.
- The Council's advice being validly given (IP7), and whether a subcommittee may give it for s.17(b).
- The first day of the current term of a licence, and the effect of an extension under s.17(c) on the register.
- Whether the day of notice under s.16 is the day of dispatch or of receipt; whether a demand under s.15 must be in writing.
- When a failure to show the licence under s.14 begins.
- When ss.12, 15, 16 and 17 commence (trap T20).
- The calendar of days of rest, recess and holiday for any year (IP15).
- The amount of any sanction for a breach of ss.12, 14, 15, 16, 17, 18(b) (trap T13): the Third Schedule has no row, and none is invented.

## 9. Evidence

The numbers below are what the scripts printed on the final files; the commands are the ones in section 0.

`check.sh` (the skill's script, adapted to `g3-*.l4`, run on `l4` with `nice -n 15`, exit status 0):

```
module                                    errors satisfied  failed  refused  expected
g3-licensee-duties.l4                          0         0       0        0         0
g3-operator.l4                                 0         0       0        0         0
g3-tests-licensee-duties.l4                    0       102       0        0         0
g3-tests-operator.l4                           0        55       0        0         0
g3-tests-red.l4                               19         0      19        0        19
g3-tests-training-duty.l4                      0       136       0        0         0
g3-training-duty.l4                            0         0       0        0         0
TOTAL (7 modules)                             19       293      19        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

The `#TRACE` check (`check-traces.py`): `checked 50  ok 50  wrong 0` (all printed results equal the expectation written above each #TRACE)
The source-reference gate (`python3 -I srcrefs.py check --refs inputs/law.wiki g3-licensee-duties.l4 g3-training-duty.l4 g3-operator.l4`): `srcrefs check: 26 src: lines, 20 runs, 117 locators, 0 problems`.
`--strict` also lists 33 places where a rule cites a quotation placed above another rule (one quotation is cited by several rules) or its first `@ref` is narrower than its quotation; those are not defects, and `--refs` is the gate the convention gives for such a file.
No module emits a warning: `l4 run` on each of the seven files prints no `DiagnosticSeverity_Warning`.
The numbers the tests rest on were re-read against the Hebrew by script (`numbers-check.py`): `numbers re-read: 12 checks, 0 failed`
Positive controls: 38 single-edit mutations of the three modules (a limit changed, a comparison turned, a condition dropped, a branch inverted) were each run against the test modules, and all 38 of 38 were caught: each turned at least one assertion red or refused (`mutate.py`, run on scratch copies of the final files; nothing in the deposit was changed).
The gazette pages 185, 186 and 205 were viewed as images and agree with the wiki on s.12 to 18 and Third Schedule items (4) to (6).

## 10. Texts quoted (copied from `inputs/law.wiki` by script)

10.1 s.12:

> src:130 | {{ח:ת}} רישיון הוא אישי; בעל רישיון לא יעביר את הרישיון שבידו לאדם אחר ולא יתיר לאדם אחר לעשות שימוש ברישיונו.

10.2 s.13:

> src:133 | {{ח:ת}} בעל רישיון יבצע עבודה במערכת קירור או מיזוג אוויר המנויה {{ח:פנימי|תוספת 1|בתוספת הראשונה}} בהתאם לחלקים 4 ו־5 לתקן ישראלי ת״י 994, כפי נוסחם מזמן לזמן.

10.3 s.14:

> src:136 | {{ח:ת}} בעל רישיון יציג את רישיונו למזמין עבודה במערכת קירור או מיזוג אוויר, לפי דרישתו.

10.4 s.15:

> src:139 | {{ח:ת}} הרשם רשאי לדרוש מבעל רישיון לדווח לו על פרטים בקשר לעיסוקו כבעל רישיון, כפי שהורה, ולמסור לו כל מידע או מסמכים הדרושים לו לשם מימוש מטרות חוק זה, לרבות כתנאי לחידוש או להארכה של רישיון, ובעל הרישיון ימסור לו את המידע או המסמכים כאמור.

10.5 s.16:

> src:142 | {{ח:ת}} בעל רישיון יודיע לרשם על כל שינוי בפרטים שמסר בבקשה לרישיון, באופן שעליו יורה הרשם, בתוך 30 ימים מיום השינוי.

10.6 s.17, subsections (a) to (f):

> src:145 | {{ח:תת|(א)}} בעל רישיון ישתתף במהלך השנה האחרונה לתוקפו של הרישיון, בהשתלמויות בפיקוח המשרד, שערך הרשם או שהאגף להכשרה מקצועית הכיר בהן, בהיקף של שמונה שעות לפחות, בתחום עיסוקו לפי רישיונו, במועדים שעליהם הורה הרשם, ויעמוד בדרישות אותן השתלמויות.
> src:146 | {{ח:תת|(ב)}} נוסף על ההשתלמויות לפי סעיף קטן (א), הרשם רשאי לדרוש מבעל רישיון להשתתף בהשתלמות מסוימת שערך הרשם או שהאגף להכשרה מקצועית הכיר בה לאחר התייעצות עם המועצה, אם מצא כי מתקיימות נסיבות המצדיקות זאת וכי ההשתתפות נדרשת לשם הכשרת בעל הרישיון ולשם מימוש מטרות חוק זה; הודעה לפי סעיף קטן זה תינתן לבעל הרישיון זמן סביר לפני מועד ההשתלמות.
> src:147 | {{ח:תת|(ג)}} הרשם רשאי, לאחר התייעצות עם המועצה, להאריך את תקופת תוקף רישיונו של בעל רישיון שלא מילא את חובתו להשתתף בהשתלמות לפי סעיף קטן (א) או (ב), במקרים מיוחדים ובנסיבות מוצדקות, בתקופה שלא תעלה על שלושה חודשים, לשם מילוי החובה.
> src:148 | {{ח:תת|(ד)}} יראו חובת השתתפות בהשתלמות ועמידה בדרישותיה לפי סעיף זה כתנאי ברישיון של בעל הרישיון.
> src:149 | {{ח:תת|(ה)}} הרשם יוודא את קיומן, לרבות באמצעות אחר, של השתלמויות, ואת זמינותן.
> src:150 | {{ח:תת|(ו)}} הרשם יפרסם השתלמויות שהוא עורך והשתלמויות שהאגף להכשרה מקצועית הכיר בהן לפי סעיף זה, באתר האינטרנט של המשרד, זמן סביר לפני מועד ההשתלמות.

10.7 s.18, subsections (a) to (c):

> src:153 | {{ח:תת|(א)}} מפעיל לא יפעיל אדם בביצוע עבודה במערכת קירור או מיזוג אוויר, אלא אם כן יש בידי אותו אדם רישיון מהסוג המתאים לביצוע עבודה באותה מערכת.
> src:154 | {{ח:תת|(ב)}} מפעיל יוודא כי בעל רישיון שהוא מפעיל יבצע עבודה במערכת קירור או מיזוג אוויר כמפורט {{ח:פנימי|תוספת 1|בתוספת הראשונה}} בהתאם לתקן כאמור {{ח:פנימי|סעיף 13|בסעיף 13}}, בין השאר באמצעות הנחיות, תדריכים או נהלים וביצוע בדיקות מדגמיות.
> src:155 | {{ח:תת|(ג)}} בסעיף זה, ”מפעיל“ – מי שמפעיל, דרך קבע, אדם אחר בביצוע עבודות במערכות קירור או מיזוג אוויר, בין שהמפעיל הוא בעל רישיון ובין שאינו בעל רישיון, ובכלל זה מי שהוא בעלים או מנהל של עסק המציע לציבור ביצוע עבודות במערכות קירור או מיזוג אוויר.

10.8 s.8 and s.26(a)(3), (a)(4) and (b), for forks S17-M and C10:

> src:100 | {{ח:ת}} תוקפו של רישיון יהיה לחמש שנים או עד 31 במרץ של השנה החמישית מהשנה שבה ניתן הרישיון, לפי המוקדם (להלן – תקופת תוקף), וניתן לחדשו לתקופות תוקף נוספות בהתקיים התנאים לפי {{ח:פנימי|סעיף 6|סעיף 6}}, למעט התנאי לפי {{ח:פנימי|סעיף 6|סעיף קטן (א)(4) של אותו סעיף}}.
> src:211 | {{ח:תתת|(3)}} לייעץ לרשם בבקשות פרטניות, לרבות הכרה בתעודה, בתואר או בהכשרה ממוסד לימודים במדינת חוץ, סירוב לחדש רישיון, התניית חידוש רישיון בהשתתפות בהשתלמות, ביטול רישיון, הגבלתו, התלייתו או הארכת תקופת תוקפו;
> src:212 | {{ח:תתת|(4)}} למלא כל תפקיד אחר שהוטל עליה בחוק.
> src:213 | {{ח:תת|(ב)}} המועצה רשאית למנות, מקרב חבריה או מי שאינו נמנה עם חבריה, ועדות משנה שייעצו לה בעניין תפקידיה, ולעניין תפקידה לפי סעיף קטן (א)(3) – רשאית המועצה לאצול לוועדת משנה את סמכויותיה.

10.9 Third Schedule items (4), (5) and (6):

> src:715 | {{ח:תת|(4)}} בעל רישיון שביצע התקנה של מערכת קירור או מיזוג אוויר בלי לבצע בדיקת אטימות לצנרת חומר הקירור בהתאם להוראות הקבועות בפרק הבדיקות בתקן ישראלי ת״י 994 חלק 4 – מזגני אוויר: התקנה, בניגוד להוראת {{ח:פנימי|סעיף 13|סעיף 13}};
> src:718 | {{ח:תת|(5)}} מפעיל שהפעיל אדם אחר בביצוע עבודה במערכת קירור או מיזוג אוויר בלי שיש בידי אותו אדם רישיון כלל, בניגוד להוראות {{ח:פנימי|סעיף 18|סעיף 18(א)}};
> src:721 | {{ח:תת|(6)}} מפעיל שהפעיל אדם אחר בביצוע עבודה במערכת קירור או מיזוג אוויר בלי שיש בידי אותו אדם רישיון מהסוג המתאים לביצוע עבודה באותה מערכת, בניגוד להוראות {{ח:פנימי|סעיף 18|סעיף 18(א)}};
