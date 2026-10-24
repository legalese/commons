# California SB 53 (TFAIA), critical safety incidents: answers decided from the source alone

Independent test author, 2026-10-24.
Written BEFORE opening anything else under `encodings/solo-2026-10/` and before the subject's NOTES.md.
Sources read, whole: `registers/source-bundle/ca-bpc-div8-ch25-1-tfaia-2026-10.txt` (139 lines, §§ 22757.10-22757.16), `ca-sb53-stats-2025-ch-138-chaptered.txt` (244 lines, SECTION 1 to SEC. 6), `ca-time-computation-2026-10.txt` (26 lines, CCP §§ 12, 12a, Civ. Code § 10, Gov. Code § 6800), their three `.meta.json`, and `SOURCE-LICENSE.md`.
All three are authoritative (Legislative Counsel bulk export; unofficial plain-text conversion).
Locators below are `bpc:N` (line N of the chapter file), `bill:N` (chaptered bill) and `time:N` (time-computation file).
Federal law, any OES regulation and any preemption litigation are not in the sources: every answer is "on the deposited text", with those inputs left open.
Weekdays were computed with the system calendar (`date -j`), not from memory.

Seat: a frontier developer (a company), asking about its own duties.

## (1) Am I a "frontier developer"? A "large frontier developer"?

**Frontier model** (§ 22757.11(i)(1), bpc:40): a *foundation model* trained using computing power **greater than 10^26** integer or floating-point operations.
Strict: exactly 10^26 operations is not a frontier model; 10^26 + 1 is.
The quantity is a count of operations (not a rate), and (i)(2) (bpc:41) makes it cumulative: the original training run plus "any subsequent fine-tuning, reinforcement learning, or other material modifications the developer applies to a preceding foundation model".
**Foundation model** (f) (bpc:34-37): an AI model ((b), bpc:18) that is ALL of: trained on a broad data set; designed for generality of output; adaptable to a wide range of distinctive tasks. Fail any one limb and nothing is a frontier model, however much compute.
**Frontier developer** (h) (bpc:39): a person who has trained, or initiated the training of, a frontier model, having used **or intending to use** at least the (i) quantity. So a developer who has started a run it intends to take past 10^26 is a frontier developer before the run finishes.
**Large frontier developer** (j) (bpc:42): a frontier developer that **together with its affiliates** collectively had annual **gross** revenues **in excess of $500,000,000** in the **preceding calendar year**.
Strict: exactly $500,000,000 is not large; $500,000,001 is.
Gross, not net or profit; all revenue, not AI revenue; no geographic limit stated.
Affiliates ((a), bpc:17): controlling, controlled by, or under common control, directly or indirectly, through intermediaries; so parent, subsidiaries and sisters all count.
A person that is not a frontier developer cannot be a large one, whatever its revenue.

Forks:
- F1 (fine-tuner). A company fine-tunes another's >10^26 base model with 10^24 of its own compute. Reading A: (i)(2) aggregates the base run, so the result is a frontier model and the fine-tuner, which "has trained" it, is a frontier developer. Reading B: (h) asks what "the person has used", and (i)(2)'s "the developer applies" means one developer's own runs, so the fine-tuner is not one. The text does not settle it.
- F2 ("preceding calendar year" relative to what). Reading A: the year before the date of the act or omission (discovery / the deadline). Reading B: the year before the date the question is asked. For a discovery on 2026-03-06 both give 2025.
- F3 (initiated, not yet over the line). (h) counts intended use, so an initiated run counts; but the (i) definition is in the past tense ("was trained"). I read (h) as governing.

## (2) Is this event a "critical safety incident"? (§ 22757.11(d), bpc:27-31)

Four categories; any one suffices.
- (d)(1) unauthorized access to, modification of, or exfiltration of the model weights of a frontier model **that results in death or bodily injury**. Weight theft with no injury is NOT (d)(1). Property loss does not count here.
- (d)(2) **harm** resulting from the **materialization of a catastrophic risk**. Catastrophic risk ((c), bpc:19-26): a foreseeable and material risk that the developer's development, storage, use or deployment of a frontier model will materially contribute to death of or serious injury to **more than 50 people** or **more than $1,000,000,000** property damage/loss, arising from a **single incident** of a frontier model (A) giving expert-level CBRN-weapon assistance, (B) engaging, with no meaningful human oversight, in a cyberattack or conduct that would be murder, assault, extortion or theft if done by a human, or (C) evading the control of its developer or user. Excluded ((c)(2)): output otherwise publicly accessible in substantially similar form from a non-foundation-model source; lawful federal-government activity; harm in combination with other software where the frontier model did not materially contribute. § 22757.16 (bpc:137): loss of equity value is not property damage.
- (d)(3) **loss of control** of a frontier model **causing death or bodily injury**. Loss of control with no injury is NOT (d)(3).
- (d)(4) a frontier model that **uses deceptive techniques against the frontier developer** to subvert its controls or monitoring, **outside** an evaluation designed to elicit that behaviour, **and** in a manner that demonstrates **materially increased catastrophic risk**. No harm needed.

Not included: weight exfiltration or loss of control without death or bodily injury; deception inside an eliciting evaluation; deception that does not demonstrate materially increased catastrophic risk; deception aimed at a user rather than the developer (on the words "against the frontier developer"); any incident with a foundation model that is not a frontier model (reporting is "encouraged, but not required", § 22757.13(c)(4), bpc:95); equity-value loss.
"Bodily injury" in (d)(1),(3) is unqualified; contrast "serious injury" in (c)(1) and "serious physical injury" in § 22757.13(c)(2).
Near miss: only (d)(4) catches an event with no harm. A near miss of kinds (1)-(3) is not a critical safety incident.
Confirmed difference: Labor Code § 1107(c) (bill:203-207, the whistleblower chapter) defines "critical safety incident" more widely ((1) adds "damage to, or loss of, property" and all four limbs say "foundation model"). That definition is "for purposes of this chapter" (the Labor Code chapter) and does not govern § 22757.13.

Forks:
- F4 ((d)(2) threshold). Reading A: harm counts only if the catastrophic outcome occurs (>50 dead/seriously injured or >$1B, single incident). Reading B: any harm resulting from the materialized risk (e.g. 3 injured in a CBRN-assisted event) counts, because "materialization" refers to the risk-type, not its full magnitude. I lean A but the text is open.
- F5 ((d)(4) "against the frontier developer"): deception against a third-party deployer that subverts the developer's controls only indirectly.

## (3) Must I report it, to whom, by when? (§ 22757.13(c)(1), bpc:92)

A **frontier developer** (not only a large one) shall report **any critical safety incident pertaining to one or more of its frontier models** to the **Office of Emergency Services** **within 15 days of discovering** it.
The clock starts on **discovery**, not occurrence. The unit is calendar days.
Counting (CCP § 12, time:11; same words in Civ. Code § 10 and Gov. Code § 6800, time:20, time:24): exclude the first day (the discovery day), include the last; if the last day is a holiday it is excluded too.
CCP § 12a(a) (time:15): if the last day is a holiday, the period runs to and including **the next day that is not a holiday**. § 12a(b) (time:16) applies this to every provision of law in any code, so it reaches § 22757.13.
**Holidays the deposited text lists:** "all day on Saturdays", and nothing else by name. It **incorporates** "all holidays specified in Section 135" and days required by § 12b to be considered holidays; **neither § 135 nor § 12b is deposited** (the time-computation meta.json says so).
So every date answer has two branches: (i) deposited text only: Saturday is the only holiday shown; (ii) with § 135 (recalled, not checked: § 135 is understood to take in Gov. Code § 6700's list, which includes every Sunday, 1 January and Thanksgiving Day).
Simple rule: last day = discovery date + 15 calendar days.

| Discovered | +15 (naive last day) | (i) deposited text only | (ii) with § 135 (recalled, not checked) |
| --- | --- | --- | --- |
| Fri 2026-03-06 | Sat 2026-03-21 | Sun 2026-03-22 | Mon 2026-03-23 |
| Thu 2026-03-05 | Fri 2026-03-20 | Fri 2026-03-20 (the day before a Saturday; no extension) | Fri 2026-03-20 |
| Thu 2026-10-08 | Fri 2026-10-23 | Fri 2026-10-23 | Fri 2026-10-23 |
| Fri 2026-10-09 | Sat 2026-10-24 | Sun 2026-10-25 | Mon 2026-10-26 |
| Wed 2026-11-11 | Thu 2026-11-26 (Thanksgiving) | Thu 2026-11-26 | Fri 2026-11-27 at earliest; Mon 2026-11-30 if the day after Thanksgiving is also a § 135 holiday (not checked) |
| Thu 2026-11-12 | Fri 2026-11-27 | Fri 2026-11-27 | Fri 2026-11-27, or Mon 2026-11-30 (same open point) |
| Wed 2026-12-16 | Thu 2026-12-31 | Thu 2026-12-31 | Thu 2026-12-31 |
| Thu 2026-12-17 | Fri 2027-01-01 (New Year's Day) | Fri 2027-01-01 | Mon 2027-01-04 |
| Fri 2026-12-18 | Sat 2027-01-02 | Sun 2027-01-03 | Mon 2027-01-04 |
| Wed 2027-11-10 | Thu 2027-11-25 (Thanksgiving) | Thu 2027-11-25 | Fri 2027-11-26 or Mon 2027-11-29 |
| Thu 2027-12-16 | Fri 2027-12-31 | Fri 2027-12-31 | Fri 2027-12-31 (unless an observed-holiday rule moves 2028-01-01 to Friday; not checked) |
| Fri 2027-12-17 | Sat 2028-01-01 | Sun 2028-01-02 | Mon 2028-01-03 |

A Friday discovery always gives a Saturday day 15, so every Friday discovery is extended, on both branches.
Off-by-one guards: counting the discovery day as day 1 would give Thu 2026-03-19 for Thu 2026-03-05; that is wrong under CCP § 12.
Where the report goes: OES, through the mechanism § 22757.13(a) (bpc:85-89) has OES establish. An amended report is permitted, not required ((c)(3), bpc:94: "may file").

Forks:
- F6 (Sunday on the deposited text). On branch (i) a Saturday last day rolls to Sunday, which is almost certainly not the law; it is what the deposited text alone yields. The fix is to deposit CCP § 135 and § 12b.
- F7 (commencement). The chapter is effective 2026-01-01 (Legislative Counsel's history note, bpc:13 etc.; the chaptered bill states no operative date of its own). A discovery on or after 2026-01-01 is in scope. A discovery on Wed 2025-12-17 (day 15 = Thu 2026-01-01) is not addressed: Reading A, no duty (discovered before the chapter took effect); Reading B, a duty from 2026-01-01. I take A.
- F8 ("discovering"): undefined; actual knowledge vs. constructive.

## (4) The 24-hour disclosure (§ 22757.13(c)(2), bpc:93)

If a frontier developer **discovers that a critical safety incident poses an imminent risk of death or serious physical injury**, it shall disclose that incident **within 24 hours** to **an authority**, "including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law".
The clock starts on discovering the imminent risk, which may be later than discovering the incident.
The recipient is an appropriate authority, not necessarily OES.
Binds every frontier developer.

Forks:
- F9 (interaction). (c)(1) opens "Subject to paragraph (2)". Reading A (mine): cumulative; the 24-hour disclosure to an authority AND the 15-day report to OES are both owed. Reading B: where (2) applies it displaces (1), so the imminent-risk incident goes to an authority within 24 hours instead of to OES within 15 days. Reading C: a 24-hour disclosure made to OES discharges both.
- F10 (24 hours and CCP § 12/§ 12a). These count days; 24 hours is not a period of days and has no "last day". Reading A (mine): clock hours, no Saturday extension. Reading B: § 12a reaches it.
- F11 ("as required by law"): Reading A: describes which authority is appropriate. Reading B: the disclosure is owed only where some other law requires it.

## (5) Who each duty binds

| Duty | Binds |
| --- | --- |
| § 22757.13(c)(1) 15-day OES report | every frontier developer |
| § 22757.13(c)(2) 24-hour disclosure | every frontier developer |
| § 22757.13(c)(3) amended report | permissive, any frontier developer |
| § 22757.13(i)(1) declaration of intent | any frontier developer that wants deemed compliance |
| § 22757.12(c)(1) transparency report; (e)(1)(A) no false statements about catastrophic risk; (f) redaction rules | every frontier developer |
| § 22757.12(a),(b) framework; (c)(2) risk summaries; (d) internal-use summaries to OES; (e)(1)(B) | large frontier developer only |
| § 22757.15 civil penalty | **large frontier developer only** |

The finding to make loud: a frontier developer that is NOT large owes the 15-day report and the 24-hour disclosure, but the chapter attaches no penalty to its failure; § 22757.15(a) (bpc:132) opens "A large frontier developer that ...".
§ 22757.13(i)(2)(B) (bpc:110) makes a declarant's failure to meet the federal standard "a violation of this chapter" for any frontier developer, but § 22757.15 still reaches only a large one.
Remedies under other law (SEC. 5(c), bill:238, cumulative) are outside the sources.

## (6) The penalty (§ 22757.15, bpc:132-133)

Who: a large frontier developer. For: failing to publish or transmit a compliant document required by the chapter; a statement violating § 22757.12(e); **failing to report an incident as required by § 22757.13**; failing to comply with its own frontier AI framework.
Amount: a civil penalty "dependent upon the severity of the violation" that **does not exceed $1,000,000 per violation**. $1,000,000 is within the cap; $1,000,001 is not. **No minimum** is stated.
Enforcement: recovered in a civil action **brought only by the Attorney General**. No private right of action under this chapter.
Forks: F12 (unit of "per violation"): per unreported incident, per day late, per duty (15-day vs 24-hour). Not stated. F13: whether a missed 24-hour *disclosure* is "fail[ing] to report an incident as required by Section 22757.13"; I read yes (it is a duty in § 22757.13 about an incident). F14: whether a declarant's (i)(2)(B) violation falls in the § 22757.15(a) list; it is not named there, and it is penalised only if it is also a failure "to report an incident as required by Section 22757.13".

## (7) Deemed compliance and the uncodified switch-offs

§ 22757.13(h)-(j) (bpc:103-111): OES **may** adopt regulations designating federal laws, regulations or guidance that (1)(A) impose CSI-reporting standards substantially equivalent to or stricter than § 22757.13, (B) need not require reporting to California, and (2) are intended to assess, detect or mitigate catastrophic risk.
A frontier developer that intends to comply that way **shall declare its intent to OES** ((i)(1)).
After declaring: (A) it is **deemed in compliance with this section** (§ 22757.13 only, not the whole chapter) **to the extent** it meets the federal standard, until it declares revocation or OES revokes the designating regulation under (j); (B) failing the federal standard is a violation of this chapter.
So deemed compliance needs all of: a designation exists, a declaration was made, neither revoked, and the developer meets the federal standard. Any one missing: the § 22757.13 duties apply as written.
Whether OES has adopted any designation is not in the sources: an open input.
SEC. 5 (bill:236-241): (a) severability; (b) liberal construction; (c) duties cumulative with other law; **(d) the act does not apply "to the extent that it strictly conflicts with the terms of a contract between a federal government entity and a frontier developer"**; **(e) the act does not apply "to the extent that it is preempted by federal law"**; (f) preempts local rules adopted on or after 2025-01-01 specifically regulating frontier developers' management of catastrophic risk.
(d) and (e) are partial ("to the extent"), not wholesale; each is an open input. If either is set, the duty does not apply (to that extent); otherwise it does.

## (8) Confidentiality and what OES must publish

§ 22757.13(f) (bpc:99): a CSI report to OES is **exempt from the California Public Records Act** (so are internal-use assessment reports and covered-employee reports).
(b)(2): OES limits access to reports related to internal use to need-to-know personnel.
(e) (bpc:97-98): the AG or OES **may** transmit CSI reports to the Legislature, the Governor, the federal government or appropriate state agencies, strongly considering trade-secret, safety, cybersecurity and national-security risks.
(g) (bpc:100-102): **beginning 1 January 2027, and annually thereafter**, OES shall **produce** a report of **anonymized and aggregated** information about CSIs it has reviewed since the preceding report, omitting trade secrets, cybersecurity, public safety and national security information and anything another law forbids, and shall **transmit** it to the Legislature (Gov. Code § 9795) and the Governor.
Nothing requires OES to publish it to the public; and no individual report is published.
Fork F15: whether the first (g) report is due ON 2027-01-01 or merely during 2027.
SEC. 6 (bill:242-244) records the constitutional findings for this limit on public access.

## (9) What the chapter does NOT contain

- No counting rule of its own (borrowed: CCP § 12/§ 12a).
- No definition of "discover", "imminent", "bodily injury" or "serious physical injury".
- No form or content duty for the developer's report beyond what OES's mechanism "includes" ((a)(1)-(4): date, reasons it qualifies, a short and plain statement, whether associated with internal use); no content stated for the 24-hour disclosure.
- No period for an amended report ((c)(3) "may file"); no duty to amend.
- No period for OES to establish the mechanism, or to review reports; no acknowledgment duty.
- No duty to report incidents with non-frontier foundation models (encouraged only).
- No penalty for a non-large frontier developer; no minimum penalty; no criminal penalty; no private right of action; no limitation period.
- No territorial nexus (nothing about doing business in California).
- No operative date in the bill text (2026-01-01 comes from the codified history note).
- No rule for an incident discovered before 2026-01-01.
- No duty on deployers or users; the duty-holder is the frontier developer.

## After reading the encoding (step E, written after everything above)

Order of reading: everything above was written first; then `tfaia-seat.l4` and the other modules (except `tfaia-tests.l4`) for names and types; while finding check.sh's settings I also saw `encoding.json`'s fork list; then `tests-independent.l4` was written and run; then `NOTES.md` and `tfaia-tests.l4`.
Nothing above was changed after the encoding was opened.

`tests-independent.l4`, main build 99 (`1.6.99 (main, 6cc2c91, 2026-10-21)`), via check.sh: 122 `#ASSERT` lines, **121 satisfied, 1 failed, 0 refused**, 1 error (the failure); same on main.
Negative control, in a scratch copy of the encoding (not committed): changing `the days to report` to 14 and the frontier-model test to `AT LEAST` gave 40 failed assertions here.

**Disagreement (the one failure, `tests-independent.l4` line 536 as first committed; line 564 after the revision below).** My F13 said a missed 24-hour disclosure is a § 22757.15 "fail[ure] to report an incident as required by Section 22757.13" (bpc:132). The encoding answers that the penalty applies only if § 22757.15 reaches it (its F14).
From the source: (c)(1) is "shall report ... to the Office of Emergency Services" (bpc:92); (c)(2) is "shall disclose that incident within 24 hours to an authority" (bpc:93); (c)(3) speaks of "the initial report required by this subdivision" (bpc:94).
The verbs differ and (c)(3) ties "report" to the Office filing, so the text is open, if anything leaning against me. The encoding's hedged answer is the more faithful one; no change needed. The assertion stays failing as the record of the disagreement.

**Agreements, each tested both sides:** every threshold strict (10^26, $500,000,000, 50 people, $1,000,000,000); intended compute counts for frontier-developer status but a model is a frontier model only once over the line; (d)(1) and (d)(3) need death or bodily injury; (d)(4) needs no harm; my F4 reading A = its F5; 15 days from discovery, first day excluded, a Saturday last day extended, other holidays only if listed (my branch (i) is its empty list); every frontier developer must report, only a large one is penalised; up to $1,000,000 per violation, AG only; (c)(4) encouraged only; 15-day and 24-hour duties cumulative (my F9 reading A = its F4); 24 clock hours, exactly 24 in time; discoveries before 2026-01-01 not covered (my F7 reading A = its F15); deemed compliance and SEC. 5(d), (e) switch the duties off; the four report items; the Public Records Act exemption; amended report permissive.

**Encoder readings I did not test, because answers-first took no position:** its F12 (the 24-hour duty reaches another developer's frontier model). Literal on bpc:93 ("a critical safety incident", not "its frontier models"); defensible.

**Forks I raised that its register lacks (recommend adding):** my F1 (does a fine-tuner count the base model's run? (i)(2) "the developer applies", bpc:41; the baseline's compute `@desc` leaves it to the user); my F2 ("preceding calendar year" measured from when, bpc:42); my F11 ("as required by law" in (c)(2), bpc:93); my F15 (is the first OES report due on 2027-01-01, bpc:100; and (g) is "transmit" to the Legislature and Governor, not publication).

**Finding for both of us:** with an empty holiday list (the deposited text alone, § 12a naming only Saturday, time:15), every Friday discovery gets a Sunday last day. Depositing Code Civ. Proc. § 135 and § 12b would close this.

**Not testable through the baseline:** revenue period and affiliate aggregation (one number in); fine-tuner compute (one number in); which days are § 135 holidays (user list); who receives the 24-hour disclosure; no minimum penalty and no private right of action (only in constructor text); the § 22757.13(i)(2)(B) federal-standard violation as a penalty case; designation vs declaration (one boolean); the penalty's commencement (no date input); OES's (e) and (g) duties (inert).

## Revision after the Sunday change (2026-10-24, about 11:10 SGT)

What changed upstream: the encoder deposited Code Civ. Proc. §§ 12b, 135 and Gov. Code § 6700 (`registers/source-bundle/ca-time-computation-holidays-2026-10.txt`, "holidays:N" below) and the encoding now computes Sundays as holidays (commit 4def2fa92).
Nine of my assertions assumed the Saturday-only rule and failed.
I read the newly deposited text (not the encoder's NOTES) and re-derived each by hand; weekdays from the system calendar.

What the deposited text now says, for § 12a's "holiday" (time:15):
- § 135 (holidays:16): every full day that § 6700 designates a holiday is a judicial holiday, "including that Thursday of November declared by the President to be Thanksgiving Day", except Lunar New Year, Diwali, 24 April, 9 September, Columbus Day and other days appointed by the President alone; and "Every Saturday and the day after Thanksgiving Day are judicial holidays".
- § 6700(a) (holidays:20-41) includes "(1) Every Sunday" and "(2) January 1"; Good Friday is only 12 noon to 3 p.m., so not a "full day".
- § 12b (holidays:12): a day the relevant public office is closed for the whole day is a holiday; a fact, not in the sources.
- § 135 also says "If a judicial holiday falls on a Saturday or a Sunday, the Judicial Council may designate an alternative day for observance"; no designation is in the sources.

Re-derived, each a Friday discovery whose day 15 is a Saturday and whose Sunday is now a holiday:

| line (after revision) | discovered | day 15 | was | now | why the next day is not a holiday |
| --- | --- | --- | --- | --- | --- |
| 442 | Fri 2026-03-06 | Sat 03-21 | Sun 03-22 | Mon 2026-03-23 | not in § 6700; see caveat |
| 451 | Fri 2026-10-09 | Sat 10-24 | Sun 10-25 | Mon 2026-10-26 | Columbus Day was 10-12, and § 135 excepts it |
| 465 | Fri 2026-12-18 | Sat 2027-01-02 | Sun 01-03 | Mon 2027-01-04 | MLK Day is 2027-01-18 |
| 476 | Fri 2027-12-17 | Sat 2028-01-01 | Sun 01-02 | Mon 2028-01-03 | not in § 6700, unless the Judicial Council designates it for 1 January (not in sources) |
| 486, 488, 494, 518 | Fri 2026-03-06 | Sat 03-21 | Sun 03-22 | Mon 2026-03-23 | as the first row |
| 536 | Fri 2026-03-06, reported Mon 03-23 | | late | in time | the last day is now 03-23; a report on 03-24 stays late (line 538, asserted with Sunday listed) |

In every case the encoding's new output matched my re-derivation, so no assertion is left failing for this change.
The original expectations are kept as comments ("before §135/§6700 were deposited: ...") above each revised line.
Only line 564 fails: the F13 disagreement above, unchanged (it moved from line 536 because of the added comment lines, so references to "line 536" in the encoder's NOTES.md and encoding.json now point at the wrong line).

Caveat on the March 2026 dates: the deposited § 6700 is the text "Amended by Stats. 2026, Ch. 7 ... Effective March 26, 2026" (holidays:3, 43), and the bundle says the earlier text was not read. For Sun 2026-03-22 the earlier text governs. I take Sunday as a holiday then too, because § 6700(a)(1) "Every Sunday" is not likely to be what AB 2156 added; that part is recalled, not checked.

Not revised, but their meaning has shifted: the assertions with `indep: no listed holidays` whose last day is Thanksgiving (Thu 2026-11-26, Thu 2027-11-25), the day after (Fri 2026-11-27), or 1 January (Fri 2027-01-01) still pass, because the encoding computes only Saturdays and Sundays and leaves every other holiday to the user's list.
On the deposited text those days ARE holidays (holidays:16, 22), so the legal last days are Mon 2026-11-30, Mon 2026-11-30, Mon 2027-11-29 and Mon 2027-01-04; the assertions with the listed days already say so.
So the "no listed holidays" assertions now test the encoding's input contract (a user who lists nothing), not the law.
The same holds for line 542, which asserts that a report on Mon 2027-01-04 is late when nothing is listed: on the text it is in time.
Recommendation to the encoder: compute the fixed-date and rule-based § 6700 days that § 135 keeps (1 January, the third Mondays of January and February, 12 February, 31 March, the last Monday in May, 19 June, 4 July, the first Monday in September, the fourth Friday in September, 11 November, Thanksgiving and the day after, 25 December), and leave only presidential or gubernatorial days, Judicial Council alternatives and § 12b closures to the user's list.
