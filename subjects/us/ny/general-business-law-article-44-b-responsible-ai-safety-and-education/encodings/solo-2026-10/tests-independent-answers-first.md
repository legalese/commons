# New York RAISE Act (GBL Article 44-B, as re-added by L. 2026 ch. 96), critical safety incidents: answers decided from the source alone

Not for use as advice.
Independent test author, 2026-10-24.
Written BEFORE opening anything else under `encodings/solo-2026-10/` and before the subject's NOTES.md.
Sources read, whole: `registers/source-bundle/ny-s8828-2026-ch-96.txt` (488 lines, the chapter amendment: legislative findings, Article 44-B §§ 1420-1429 as re-added, and sections 3-5 on effect), `ny-s6953b-2025-ch-699.txt` (248 lines, the act as first enacted), their two `.meta.json`, and `SOURCE-LICENSE.md`.
Both are the bill prints from nyassembly.gov in an unofficial plain-text conversion; the Laws of New York as published, a consolidated General Business Law and the General Construction Law were NOT obtained, so every answer is "on the deposited text".
Locators: `ch96:N` and `ch699:N` are line N of the respective `.txt` file (not the bill's own page/line numbers).
Weekdays and daylight-saving instants were computed with the system calendar (`date -j`, `TZ=America/New_York`), not from memory: 2027-03-14 is a Sunday and the zone is EST before 02:00 and EDT after; 2027-11-07 is a Sunday and the zone is EST after 02:00.

Seat: a frontier developer (a company), asking about its own duties.

## (1) Am I a "frontier developer"? A "large frontier developer"?

**Frontier model** (§ 1420(9)(a), ch96:148-150): a *foundation model* "trained using a quantity of computing power greater than 10§26 integer or floating-point operations".
"10§26" is the conversion artefact the meta.json describes (the page prints the exponent as byte A7); I read it as 10^26, and the 2025 text has the same artefact (ch699:74).
Strict: exactly 10^26 operations is not a frontier model; 10^26 + 1 is.
Cumulative ((9)(b), ch96:151-154): the original run plus "any subsequent fine-tuning, reinforcement learning, or other material modifications the developer applies to a preceding foundation model".
**Foundation model** (§ 1420(6), ch96:136-140): an AI model that is ALL of: trained on a broad data set; designed for generality of output; adaptable to a wide range of distinctive tasks. Fail any limb and it is not a frontier model, whatever the compute.
**Frontier developer** (§ 1420(8), ch96:141-145): a person who "has trained, or initiated the training of, a frontier model", having "used, or intends to use, at least as much computing power ... as would meet the technical specifications found in subdivision nine". Exactly 10^26 does not "meet" a "greater than 10^26" specification, so it is not enough.
An initiated run intended to exceed 10^26 makes the person a frontier developer before the run completes.
**Person** (§ 1420(14), ch96:163-167): an individual or listed business form, "or any other **nongovernmental** organization". A governmental body is not a person, so it cannot be a frontier developer.
**Large frontier developer** (§ 1420(10), ch96:155-157): a frontier developer that "together with its affiliates collectively had annual gross revenues in excess of five hundred million dollars in the preceding calendar year".
Strict: exactly $500,000,000 is not large; $500,000,001 is. Gross revenue, all sources, no geographic limit. Affiliates (§ 1420(1), ch96:89-91): controlling, controlled by, or under common control, directly or indirectly. Affiliates count for revenue only, not for compute.
A person that is not a frontier developer is not large, whatever its revenue.
**Scope and exceptions** (§ 1425, ch96:382-384): the article applies only to frontier models "developed, deployed, or operating in whole or in part in New York state". § 1426 (ch96:385-392): nothing applies to accredited NY colleges and universities "to the extent" engaged in academic AI research, or to the Empire AI consortium or institute (Econ. Dev. Law § 361, not deposited).

Forks:
- F1 (fine-tuner). Someone fine-tunes another's >10^26 base model with 10^24 of its own compute. A: (9)(b) aggregates, so the fine-tuner "has trained" a frontier model. B: (8) asks what "the person has used", and (9)(b) speaks of "the developer" applying modifications, so only its own compute counts. Open.
- F2 ("preceding calendar year" relative to what): the year before the act/omission, or before the question is asked. Same answer for any 2027 incident date if asked in 2027.
- F3 (§ 1426(1) "to the extent"): a university is outside only for its academic research; its commercial models are inside.

## (2) Is this event a "critical safety incident"? (§ 1420(4), ch96:116-129)

Any one of four:
- (a) unauthorized access to, modification of, or exfiltration of the model weights of a frontier model **that results in death or bodily injury** (ch96:117-119). Weight theft with no injury is not (a); property loss does not count here.
- (b) **harm resulting from the materialization of a catastrophic risk** (ch96:120). Catastrophic risk (§ 1420(3)(a), ch96:96-109): a foreseeable and material risk that the developer's development, storage, use or deployment of a frontier model will materially contribute to the death of, or serious injury to, **more than fifty people** or **more than one billion dollars** in damage to or loss of property, arising from **a single incident** of a frontier model (i) giving expert-level CBRN-weapon assistance, (ii) engaging with no meaningful human oversight in a cyberattack or conduct that would be murder, assault, extortion or theft (including by false pretense) if done by a human, or (iii) evading the control of its developer or user. Excluded ((3)(b), ch96:110-115): output publicly accessible in substantially similar form from a source other than a foundation model; lawful federal-government activity; harm with other software where the frontier model did not materially contribute. § 1423 (ch96:375-376): loss of equity value is not property damage.
- (c) **loss of control** of a frontier model **causing death or bodily injury** (ch96:121-122). Loss of control with no injury is not (c).
- (d) a frontier model that **uses deceptive techniques against the frontier developer** to subvert its controls or monitoring, **outside** an evaluation designed to elicit that behaviour, **and** in a manner that demonstrates **materially increased catastrophic risk** (ch96:123-127). No harm needed.

Not included: weight compromise or loss of control without death or bodily injury; deception inside an eliciting evaluation; deception not demonstrating materially increased catastrophic risk; any event with a model that is not a frontier model (there is no "encouraged" reporting for other models in this text); equity loss; any harm at or under the thresholds (exactly 50 people, exactly $1,000,000,000) for (b) on reading F4-A.
Three injury terms: "bodily injury" ((a), (c)), "serious injury" (catastrophic risk), "serious physical injury" (24-hour duty, ch96:288).

Forks:
- F4 ((b) magnitude). A: (b) needs the catastrophic outcome (>50 people or >$1bn, single incident). B: any harm from a materialized risk of the listed kind. I lean A; open.
- F5 ((d) "against the frontier developer"): deception against a deployer or user that only indirectly subverts the developer's controls. Open.

## (3) Must I report it, to whom, by when? (§ 1422(3)(a), ch96:280-286)

"Subject to paragraph (b) of this subdivision, a **frontier developer** shall report any critical safety incident pertaining to one or more of its frontier models **to the office** within seventy-two hours **from a determination** that a critical safety incident has occurred **or** within seventy-two hours **of the frontier developer learning facts sufficient to establish a reasonable belief** that a critical safety incident has occurred."
Who: every frontier developer, large or not. To whom: "the office" (§ 1420(16), ch96:169-171: an office within the Department of Financial Services), through the mechanism § 1422(1) (ch96:257-265) has it establish, whose report includes the incident date, why it qualifies, a short plain statement, and whether it was associated with internal use.
Unit: hours, elapsed. Deadline = trigger instant + 72 hours. An amended report is permitted, not required ((3)(c), ch96:290-295: "may file").
Which trigger: on reading F6-A (taken) the clock runs from **whichever comes first**; reasonable belief ordinarily precedes a determination, so the reasonable-belief instant usually governs.

Concrete moments, reading F6-A, elapsed hours, New York time used only to state the instants:

| Trigger (NY time) | Deadline (elapsed 72h) | Wall-clock reading (F8-B) |
| --- | --- | --- |
| Fri 2027-01-08 18:00 EST (Friday evening) | Mon 2027-01-11 18:00 EST | same |
| Thu 2027-01-07 23:30 EST (across midnight) | Sun 2027-01-10 23:30 EST | same |
| Fri 2027-03-12 20:00 EST (spring-forward 2027-03-14) | **Mon 2027-03-15 21:00 EDT** | Mon 2027-03-15 20:00 EDT (only 71 elapsed hours) |
| Fri 2027-11-05 20:00 EDT (fall-back 2027-11-07) | **Mon 2027-11-08 19:00 EST** | Mon 2027-11-08 20:00 EST (73 elapsed hours) |
| Wed 2027-01-13 18:00 EST | Sat 2027-01-16 18:00 EST (no weekend extension on the deposited text) | same |

Boundary, trigger T: a report at T + 71h59m is on time; at T + 72h00m is on time ("within seventy-two hours" read inclusively; fork F7); at T + 72h01m is late.
Both triggers: belief Mon 2027-02-01 09:00, determination Wed 2027-02-03 09:00. F6-A: deadline Thu 2027-02-04 09:00. F6-B: Sat 2027-02-06 09:00.
Time zone: the text states none (grep for "time zone", "eastern", "business day", "holiday", "Saturday", "Sunday", "weekend" over ch96: zero hits). On an elapsed-hours reading the zone does not matter, since both instants are absolute; it matters only on a wall-clock reading. "Hours" favours elapsed.
Computation-of-time and holiday rules: none in the deposited text. New York's General Construction Law was not deposited; whether its weekend/holiday rule (recalled as § 25-a, not checked) could extend an hours deadline is not answered here. On the deposited text: no extension.

Forks:
- F6 (two triggers joined by "or"). A: the earlier trigger starts the clock (purpose: "timely reporting", ch96:60-65; otherwise the belief limb would add nothing whenever a determination later follows). B: a report within either window complies, so the later deadline governs.
- F6' ("a determination" has no actor): the developer's own determination, or anyone's (the office, a court, a third party). Open; I treat it as the developer's.
- F7 (72h00m): inclusive (taken) or exclusive. Open; the text has no rule.
- F8 (hours): A elapsed (taken); B wall-clock in an unstated zone.

## (4) The 24-hour disclosure (§ 1422(3)(b), ch96:287-292)

"If a frontier developer **discovers that a critical safety incident poses an imminent risk of death or serious physical injury**, the frontier developer shall disclose that incident **within twenty-four hours** to **an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate** based on the nature of that incident and as required by law."
Who: every frontier developer. Trigger: discovery of the imminent risk (not of the incident). To whom: an appropriate authority; the office is not named. Content and form: none stated.
Example: imminent risk discovered Fri 2027-03-12 20:00 EST: disclosure by Sat 2027-03-13 20:00 EST; 72-hour report to the office (if belief formed at the same instant) by Mon 2027-03-15 21:00 EDT.
Relationship: on reading F9-A (taken), both duties are owed; the 24-hour disclosure does not replace the 72-hour report to the office.
- F9 ("Subject to paragraph (b)", ch96:280). A: both owed; the two can be performed together, so there is no conflict for "subject to" to resolve. B: for an imminent-risk incident (b) displaces (a). C: a disclosure to the office within 24 hours, if the office is "an appropriate authority", discharges both. Open.

## (5) Which developers each duty binds; penalties (§ 1427, ch96:393-409; § 1428, ch96:410-460)

Duties: § 1422(3) (72-hour report, 24-hour disclosure): every frontier developer. § 1422(2) (internal-use summaries every three months): large only. § 1421(1)-(2) (framework): large only; § 1421(3)(a) transparency report: every frontier developer; (3)(b): large. § 1421(4)(a)(i) false statements on catastrophic risk: every frontier developer; (4)(a)(ii): large. § 1428 disclosure statement and assessment: large only.
§ 1427(1): **the attorney general** may bring a civil action for a civil penalty **not to exceed $1,000,000 for a first violation** and **not to exceed $3,000,000 per subsequent violation**, by severity, "where **a large frontier developer** fails to publish or transmit a compliant document ..., makes a statement in violation of [§ 1421(4)], **fails to report an incident as required by section [1422]**, or fails to comply with its own frontier AI framework".
So the § 1427 penalty reaches only large frontier developers. A frontier developer that is not large and fails to report has no § 1427 penalty on this text (its duty stands; no consequence is stated).
No minimum (ceilings only). No private right of action (§ 1427(2), ch96:403-405). No injunctive relief is mentioned (ch699 § 1422(1)(b), ch699:223-224, had it). § 1424 (ch96:377-381): duties cumulative with other law.
§ 1428(5) (ch96:446-456): if "any person develops, deploys, or operates a **large frontier model** in part in New York state" without a current disclosure, submits false information, or fails to pay an assessment, **the office**, after notice and hearing, may levy $1,000 per day of failure to file or to correct, plus the assessments owed. "Large frontier model" is not defined in § 1420 (which defines "frontier model" and "large frontier developer"): confirmed. Read with § 1428(1) it most likely means a large frontier developer's frontier model; open (F10).
- F11: does "fails to report an incident as required by section 1422" include the 24-hour disclosure? It is in § 1422(3)(b), so I read yes.
- F12: "first violation" is per developer, not per kind of violation; the text does not say.

## (6) Alternative compliance routes; California

§ 1422(8) (ch96:338-349): the office **may** by regulation designate federal laws, regulations or guidance documents that impose incident-reporting standards substantially equivalent to or stricter than subdivision three (need not require reporting to New York) and are intended to assess, detect or mitigate catastrophic risk.
§ 1422(9) (ch96:350-371): a frontier developer that intends to comply with subdivision three through a designated federal instrument **shall declare its intent to the office**; then it is **deemed in compliance with subdivision three** (all of it: 72-hour report, 24-hour disclosure, amended reports) **to the extent** it meets the federal standard, until it revokes the declaration or the office revokes the regulation; failing the federal standard is itself a violation of the article; and it must send copies of the federal incident reports to the office **concurrently** with sending them to federal authorities.
§ 1422(10) (ch96:372-374): the office shall revoke a designation whose conditions no longer hold.
So deemed compliance needs all three: a designation in force, a declared and unrevoked intent, and meeting the federal standard. Without a designation, no alternative route exists.
California: no deemed-compliance clause for California's SB 53 or any other state's law, and no preemption clause. Grep of ch96 for "california", "preempt", "another state", "other state": zero hits. The legislative findings (ch96:23-69) do not mention California either.

## (7) Effective date and transition

Ch. 96 § 5 (ch96:483-488): the act takes effect immediately, but §§ 1, 2 and 4 take effect on the same date and in the same manner as ch. 699. Ch. 96 § 3 (ch96:470-475) amends ch. 699's effective-date section to read "January 1, 2027". So Article 44-B as re-added takes effect **2027-01-01**. A trigger before 2027-01-01 is outside the re-added article (F13 for its incidents).
Ch. 699 § 3 as enacted (ch699:247-248): "on the ninetieth day after it shall have become a law". Signed 2025-12-19 (meta.json), the ninetieth day is 2026-03-19 (counting the day after signing as day 1; GCL not deposited); ch. 96 was signed 2026-03-27 (meta.json). Whether the original article was briefly in force is open (F14); the text supports only the 2027-01-01 date for the re-added article.
What ch. 96 changed for incident reporting: who (ch699 "large developer" → every "frontier developer"); what ("safety incident", ch699:144-153, → "critical safety incident"); to whom (attorney general and the division of homeland security and emergency services, ch699:202-204, → the office in DFS); trigger ("learning of the safety incident", ch699:205-206, → "a determination"; the reasonable-belief limb kept); added the 24-hour imminent-risk disclosure, amended reports, and the federal route; penalties ($10M/$30M for any § 1421 violation plus injunctive relief, ch699:216-224, → $1M/$3M, large frontier developers only, listed failures); thresholds (10^26 AND >$100M compute cost, or distillation >$5M, ch699:73-80; large = >$100M aggregate compute cost, ch699:107-117 → 10^26 foundation model, cumulative; large = >$500M revenue with affiliates).
- F13 (incident before 2027-01-01, determined after): the trigger is the determination/belief, so A: reportable if the trigger is on or after 2027-01-01. B: only incidents occurring after. I take A for triggers.

## (8) Confidentiality; what the office must publish

§ 1422(6) (ch96:313-317): a critical safety incident report submitted to the office, and "a report of assessments of catastrophic risk from internal use pursuant to section fourteen hundred twenty-one", are exempt from disclosure under Public Officers Law article 6 (FOIL). The internal-use summaries are required by § 1422(2)(a) (ch96:266-271), not § 1421 (§ 1421(1)(j), ch96:199-201, only requires the framework to describe internal-use assessment): confirmed misreference (F15: read as § 1422(2)).
§ 1422(5)(a) (ch96:299-309): the office may transmit reports to other governmental entities (should consider the attorney general); transmitted reports are FOIL-exempt. § 1422(2)(b): access to internal-use reports limited to authorised personnel.
Publication: the office's annual report, "beginning January first, two thousand twenty-eight, and annually thereafter" (§ 1422(7), ch96:318-337), with anonymized aggregated incident information, is "produce[d]" and "transmit[ted]" to the governor and named legislators; the word "publish" is not used for it. The only thing the office must "publish" is the list of large frontier developers that have filed disclosure statements, without contact details (§ 1428(6), ch96:457-460). No date is stated for that list.
The 24-hour disclosure to another authority is not a report "submitted to the office", so § 1422(6) does not cover it.

## (9) What the Act does NOT contain (on the deposited text)

A time zone; a computation-of-time or weekend/holiday rule; a definition of "determination", "discovers", "learning facts" or "reasonable belief"; an actor for "a determination"; content or form for the 24-hour disclosure; a deadline for an amended report; a penalty under § 1427 for a frontier developer that is not large; a minimum penalty; injunctive relief; a private right of action (expressly excluded); any reference to California or any other state, deemed compliance with another state's law, or a preemption clause; a definition of "large frontier model" (used once, § 1428(5)); a duty or encouragement to report incidents with non-frontier models; whistleblower or employee protections; audits; a short-title section in ch. 96 (the article heading names the RAISE Act, ch96:75-76; ch. 699 § 1 had one); criminal penalties; a fee amount (pro rata assessment only, § 1428(4)).

## Fork summary

F1 fine-tuner; F2 preceding year; F3 university extent; F4 (b) magnitude; F5 deception target; F6 which trigger (earlier, taken); F6' who determines; F7 72h00m inclusive (taken); F8 elapsed vs wall-clock (elapsed, taken); F9 24h vs 72h (both owed, taken); F10 "large frontier model"; F11 24h within § 1427 (yes); F12 "first violation" scope; F13 pre-2027 incidents (trigger date governs, taken); F14 ch. 699 briefly in force; F15 § 1422(6) cross-reference.

## After reading the encoding (step E, written after everything above)

Order of reading: everything above was written first; then `raise-seat.l4` (exported questions and parameters), `raise-domain.l4` (types), the result types in `raise-reporting.l4` and `raise-penalty.l4`, and the rules in `raise-definitions.l4`; then `tests-independent.l4` was written and run; then `NOTES.md` and `raise-tests.l4`.
Nothing above this section was changed after the encoding was opened.

`tests-independent.l4`, main build 99 (`1.6.99 (main, 6cc2c91, 2026-10-21)`), via check.sh: 104 `#ASSERT` lines, **102 satisfied, 2 failed, 0 refused**, 2 errors (the two failures); same on main.
Negative controls, in a scratch copy of the encoding (deleted, not committed), counting the 2 standing failures: ignoring the UTC offset (a wall-clock reading) gave 20 failed; making the 72-hour test exclusive gave 20 failed; making the 10^26 test `AT LEAST` gave 16 failed.

**Disagreement (the two failures, the F11 assertions in section (5) of `tests-independent.l4`).** My F11 read a missed 24-hour disclosure as a § 1427(1) failure "to report an incident as required by section fourteen hundred twenty-two" (ch96:400-401), so a large frontier developer would face up to $1,000,000 / $3,000,000. The encoding answers "a civil penalty only if section 1427 reaches a failure to disclose within 24 hours" with the same amounts (its F18).
From the source: § 1422(3)(a) is "shall report ... to the office" (ch96:281-282); (3)(b) is "shall disclose that incident within twenty-four hours to an authority" (ch96:289-290); (3)(c) speaks of "the initial report required by this subdivision" (ch96:294-295).
The verbs differ and (3)(c) ties "report" to the office filing, so the text is open, if anything leaning against me. The encoding's hedged answer is the more faithful one; no change needed. The assertions stay failing as the record of the disagreement.

**Agreements, each tested on both sides:** every threshold strict (10^26 operations, $500,000,000, 50 people, $1,000,000,000); intended compute counts for frontier-developer status (an initiated run at 10^25 intended to reach 2 x 10^26); (a) and (c) need death or bodily injury; (d) needs no harm and fails inside an eliciting evaluation; the (3)(b) exclusions; every frontier developer must report, to the office, for its own frontier models; the earlier trigger starts the 72-hour clock (my F6-A = its F8); 72 and 24 elapsed hours on the UTC scale, inclusive at 72h00m / 24h00m (my F7, F8-A = its F9, F10), across midnight, the 2027 spring-forward and fall-back, a leap day, a year end and a report stated in UTC; no weekend extension; a clock started before 2027-01-01 not covered (my F13 = its F14); §§ 1425, 1426 and the federal route as switches; the 24-hour disclosure does not replace the 72-hour report (my F9-A = its F4); deemed compliance reaches the 24-hour disclosure; no California or other-state route; the four report items; amended report permissive; the FOIL exemption; § 1427 large only, AG only, $1,000,000 / $3,000,000; § 1428(5) $1,000 a day plus assessments.

**Encoder readings I did not test, because answers-first took no position:** its F16 (the 24-hour duty is not limited to the developer's own models). Literal on ch96:287-288 ("a critical safety incident", where (3)(a) says "pertaining to one or more of its frontier models"); defensible.

**Points in my answers-first that the encoding's register lacks (recommend adding):** my F1 (does a fine-tuner count the base model's run? § 1420(9)(b) "the developer applies", ch96:151-154; the baseline's compute `@desc` leaves it to the user); my F6' (whose "determination" starts the clock: § 1422(3)(a) names no actor, ch96:282-283); my F3 (§ 1426(1) "to the extent", ch96:387-389: the baseline's `college research` input carries it, but the register should say a university's non-research models are covered); § 1420(14) "Person" is limited to nongovernmental organisations (ch96:166-167), so a government body cannot be a frontier developer (the coverage table files § 1420(14) as "inert: names"); and § 1422(7) (ch96:318-337) says the annual report is produced and "transmit[ted]" to the governor and named legislators, not published (the only publication duty is § 1428(6)'s list, ch96:457-460). Its F21 matches my F15 (the § 1422(6) cross-reference to § 1421; confirmed against ch96:313-317 and ch96:266-271), its F20 my F10 ("large frontier model", ch96:446, confirmed undefined: § 1420 defines only "frontier model" and "large frontier developer"), and its F12 my reading of "10§26" (ch96:149, ch699:74).

**Not testable through the baseline:** the revenue period and affiliate aggregation (one number in); fine-tuner compute (one number in); whose determination counts; the 24-hour recipient and content (no output names one); no minimum penalty and no private right of action (only in `@desc` and constructor text); the federal-standard failure as a § 1427 case (§ 1422(9)(b)(ii)); designation vs declaration vs revocation (one boolean); the start of the office's annual report (2028-01-01) and the § 1428(6) list (inert); FOIL for onward transmission (§ 1422(5)(a), inert); the governmental-person exclusion (not an input); a start moment within an hour of midnight on 1 January 2027 (the encoding compares the start's local date, its F14; the text names no zone, and I did not assert either side).
