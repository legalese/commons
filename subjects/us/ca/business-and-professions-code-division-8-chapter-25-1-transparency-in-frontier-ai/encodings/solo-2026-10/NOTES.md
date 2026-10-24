# California Transparency in Frontier Artificial Intelligence Act (SB 53): critical safety incident reporting

**Not for use as advice.**
This is a first draft.
No domain expert and no lawyer qualified in California law has read it against the source.
Gates HG1 and HG2 have not been sought.

## Method and edition

- **Method.** Solo workflow of the `encoding-a-subject` skill: one session, a pinned brief, a coverage table, nouns first, tests written by hand from the source and a calendar, `check.sh` against a main build, `srcrefs.py check --strict` over every quotation.
  An independent test pass has been run (see "Independent test pass" below): 122 assertions, 121 satisfied, 1 failed as an expected red (F14), 0 refused.
- **Sources**, all from the California Legislature's Office of Legislative Counsel, read from its official bulk export `pubinfo_2025.zip` on 2026-10-24 (details in `../../SOURCE-LICENSE.md` and each `.meta.json`):
  - `ca-bpc-div8-ch25-1-tfaia-2026-10.txt`: Bus. & Prof. Code §§ 22757.10 to 22757.16, every row of the code table whose chapter is 25.1. Role: authoritative (the Legislative Counsel's own codified text; the plain-text conversion is ours and unofficial).
  - `ca-sb53-stats-2025-ch-138-chaptered.txt`: SB 53 as chaptered, Stats. 2025, ch. 138, for the act's uncodified SEC. 5 and as a cross-check. Role: authoritative, as above.
  - `ca-time-computation-2026-10.txt`: Code Civ. Proc. §§ 12 and 12a, Civ. Code § 10 and Gov. Code § 6800, for counting days. Role: authoritative, as above.
  - `ca-time-computation-holidays-2026-10.txt`: Code Civ. Proc. §§ 12b and 135 and Gov. Code § 6700, which § 12a and § 135 refer to for the meaning of "holiday"; deposited after the independent test pass (read 2026-10-24, 02:24Z to 02:27Z). Role: authoritative, as above. Gov. Code § 6700 is the version effective March 26, 2026 (Stats. 2026, ch. 7); the earlier text was not read. The encoding does not compute these holidays (deferred). For a last day before 2026-03-26 the encoding applies that later text (it computes Sundays whatever the date), so such answers rest on a text not yet in force on that day.
- **Checked against the chaptered text.** All 108 paragraphs of the seven codified sections were found verbatim among the paragraphs of the chaptered bill (SEC. 2), by a script, on 2026-10-24.
  The official printed statutes were not consulted.
- **Edition and vintage.** One.
  Each section's history note reads "Added by Stats. 2025, Ch. 138, Sec. 2. (SB 53) Effective January 1, 2026."
  The code table (last updated 2026-10-03) has no other row for Chapter 25.1, so it records no amendment, repeal or second version (verified in this session).
  Stats. 2026, ch. 861 (SB 1000) amended § 22757.1, which is in Chapter 25, not 25.1 (verified in the same table); it does not touch this chapter.
  Whether any statute chaptered after 2026-10-03 amends Chapter 25.1 was not checked.
- **Target compiler: `main`.** Written and run with `1.6.99 (main, 6cc2c91, 2026-10-21)`; `check.sh` compared it with the newest main build its `fetch-main-l4.sh` found, the same build 99.
- **Licence of the sources: public domain** (Gov. Code § 10248.5, read 2026-10-24 in the same export). See `SOURCE-LICENSE.md`.

## Source gate (2026-10-24, about 09:32 to 09:42 SGT)

- `https://leginfo.legislature.ca.gov/robots.txt` and the SB 53 bill page: HTTP 403, a Cloudflare challenge page, once each. Not used, not worked around.
- `https://www.leginfo.ca.gov/robots.txt`: HTTP 403. Not used.
- `https://www.caloes.ca.gov/wp-content/uploads/Preparedness/Documents/01-2450.pdf` (robots.txt allows it): fetched, and it is **not about SB 53**. It is a one-page Barclays reproduction of 19 CCR § 2450, after-action reports under the Standardized Emergency Management System, "current through 1/30/09". Not deposited, not used.
- `https://downloads.leginfo.legislature.ca.gov/`: no robots.txt (HTTP 404); the owner approved this bulk route for California on 2026-10-20 (`subjects/us/ca/README.md`). Only the zip's central directory and the named members were read, by HTTP Range requests; no refusal of any kind.
- Unofficial reproductions (california.public.law, FindLaw, LegiScan) were not needed and not fetched.
- 2026-10-24, 10:24 to 10:27 SGT: the same route again, for Code Civ. Proc. §§ 12b and 135 and Gov. Code § 6700 (the code table and three members); no refusal.

## Seat

**A frontier developer**, a company: "Am I a frontier developer? a large one?", "Is this a critical safety incident?", "Must I report it, to whom, and by when?", "Must I disclose it within 24 hours?", "What can happen to me if I don't?".
Every input is a fact that developer can state: its model's features and training compute, its revenue with its affiliates, what happened, when it discovered it, whether it has declared the federal route of § 22757.13(i).
The Office of Emergency Services and the Attorney General get no seat; where § 22757.13 addresses them, the encoding says what it means for the developer (the four items the Office's mechanism takes; the report's exemption from the Public Records Act; who may sue for the penalty), or records the subdivision as inert.
Design defaults (CLAUDE.md, 2026-10-18) followed: the chapter's own definitions are worked out from facts ("frontier model", "frontier developer", "large frontier developer", "foundation model", "catastrophic risk", "critical safety incident"); judgments the text leaves to the developer ("materially contributed", "materially increased catastrophic risk", "imminent risk") are asked as facts; borrowed terms ("artificial intelligence model" as a description, "holiday" under Code Civ. Proc. § 135) are asked as facts.
One departure, stated: the input "the most operations I have used or intend to use to train any foundation model" reaches beyond the one model in the case, because a developer can be a frontier developer through another model (F3).

## What is encoded, and what is not

Encoded: § 22757.11 so far as it decides who is bound and what is reportable ((b), (c), (d), (f), (h), (i), (j), with (a), (e), (g), (k), (l) as glosses or inert); § 22757.13(a), (c)(1) to (c)(4), (f), (h) to (j); § 22757.15 as it bears on reporting; § 22757.16; SB 53 SEC. 5(d) and (e) as inputs; Code Civ. Proc. §§ 12 and 12a for counting the 15 days.
Not encoded: § 22757.12 (frontier AI frameworks, transparency reports, quarterly internal-use summaries, false statements, redactions), § 22757.14, and the act's CalCompute (SEC. 3) and whistleblower (SEC. 4) sections; each has a row below.

Modules, in reading order:

| module | what it holds |
| --- | --- |
| `tfaia-domain.l4` | nouns only: the developer and its model, the incident, the four kinds, the reporting position, the report's items, the failures |
| `tfaia-definitions.l4` | § 22757.11 and § 22757.16: foundation model, frontier model, frontier developer, large frontier developer, catastrophic risk, critical safety incident |
| `tfaia-reporting.l4` | § 22757.13 with SB 53 SEC. 5(d), (e) and Code Civ. Proc. §§ 12, 12a |
| `tfaia-penalty.l4` | § 22757.15 for a failure to report |
| `tfaia-seat.l4` | the baseline: eleven `@export` questions from the developer's seat, every input with an `@desc` |
| `tfaia-tests.l4` | 94 assertions by the encoder, expected values by hand |
| `tests-independent.l4` | 122 assertions by an independent author, who decided its answers before opening the encoding; one is an expected red |

Beside them, `tests-independent-answers-first.md` is that author's record of its answers, written from the sources first.

The eleven exported questions: Am I a frontier developer? Am I a large frontier developer? Is this a critical safety incident? Must I report this incident to the Office of Emergency Services, and by when? Must I disclose this incident within 24 hours? Did I report to the Office in time? Did I disclose within 24 hours? May I file an amended report? What must my report give? Is my report exempt from public records requests? What is the most I can be made to pay for failing to report?

## Where the text differs from the brief

Each was checked against the deposited text in this session; the text wins.

1. **The civil penalty reaches only a LARGE frontier developer.** § 22757.15(a): "A large frontier developer that ... fails to report an incident as required by Section 22757.13 ... shall be subject to a civil penalty".
   The reporting duty of § 22757.13(c)(1) is on every "frontier developer".
   The chapter states no penalty for a frontier developer that is not large (F1). The brief did not say this.
2. **The federal route is federal only.** § 22757.13(h) and (i) let the Office designate "one or more federal laws, regulations, or guidance documents", and a developer that declares its intent to comply through one is "deemed in compliance with this section to the extent" it meets it.
   No other jurisdiction's regime (the EU AI Act, for example) can be designated.
   Failing the designated federal standard "shall constitute a violation of this chapter" (§ 22757.13(i)(2)(B)).
3. **The act switches itself off in two further cases** (SB 53, SEC. 5, not codified): "to the extent that it strictly conflicts with the terms of a contract between a federal government entity and a frontier developer" (d), and "to the extent that it is preempted by federal law" (e). The brief did not mention them; both are inputs.
4. **Confirmed as the brief states:** Chapter 25.1, §§ 22757.10 to 22757.16 (the slug's "chapter-25-1" is right); Stats. 2025, ch. 138; effective January 1, 2026; 15 days to the Office (§ 22757.13(c)(1)); 24 hours to "an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law" (c)(2); Public Records Act exemption (f); the Office's anonymized, aggregated annual report "Beginning January 1, 2027" (g)(1); four kinds of critical safety incident in § 22757.11(d); "greater than 10^26 integer or floating-point operations" (§ 22757.11(i)(1)); "annual gross revenues in excess of five hundred million dollars ($500,000,000) in the preceding calendar year", with affiliates (§ 22757.11(j)); a civil penalty "dependent upon the severity of the violation that does not exceed one million dollars ($1,000,000) per violation", "recovered in a civil action brought only by the Attorney General" (§ 22757.15).
5. **The whistleblower provisions are in the Labor Code**, Chapter 5.1 (§§ 1107 to 1107.2) of Part 3 of Division 2, added by SB 53 SEC. 4; CalCompute is Gov. Code § 11546.8, added by SEC. 3 (both read in the chaptered text; neither encoded).

## Answer table: the reporting clocks and consequences

| duty or consequence | on whom | to whom | when | how counted | provision |
| --- | --- | --- | --- | --- | --- |
| report a critical safety incident "pertaining to one or more of its frontier models" | every frontier developer (F1) | the Office of Emergency Services | "within 15 days of discovering" it | calendar days; the day of discovery not counted, the last day counted (Code Civ. Proc. § 12); a last day that is a Saturday, a Sunday (§ 135 with Gov. Code § 6700(a)(1)) or another § 135 / § 12b holiday moves to the next day that is not a holiday (§ 12a); Saturdays and Sundays are computed, other holidays must be listed (F9) | § 22757.13(c)(1) |
| disclose an incident that "poses an imminent risk of death or serious physical injury" | a frontier developer that discovers that; not limited to its own models (F12) | "an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate ... and as required by law"; none named | "within 24 hours" | hours from discovering the imminent risk; exactly 24 is in time (F10, F16) | § 22757.13(c)(2) |
| both of the above | | | both are owed; "Subject to paragraph (2)" is not read as displacing the 15-day report (F4) | | § 22757.13(c)(1), (2) |
| amended report | may, after discovering new information | the Office | **no period stated** | | § 22757.13(c)(3) |
| incidents with foundation models that are not frontier models | "encouraged, but not required" | | **no period stated** | | § 22757.13(c)(4) (F8) |
| federal route | after a declaration of intent to the Office | | deemed in compliance "to the extent" the federal standard is met; **no period stated** for the declaration | | § 22757.13(h) to (j) |
| what the report gives | | | the date; why it qualifies; a short plain statement; whether internal use of a frontier model was involved | | § 22757.13(a)(1) to (4) |
| public access | | | exempt from the California Public Records Act | | § 22757.13(f) |
| civil penalty for failing to report | a **large** frontier developer only (F1) | recovered only by the Attorney General in a civil action | up to $1,000,000 per violation, "dependent upon the severity"; **no minimum stated**; how violations are counted **not stated** (F13) | | § 22757.15 |
| civil penalty for a failed 24-hour disclosure | a large frontier developer, **on one reading** (F14) | as above | as above | | § 22757.15 |
| a frontier developer that is not large and fails to report | | | **no penalty stated in the chapter** | | § 22757.15 (absence) |
| incidents discovered before 1 January 2026 | | | **not covered**: the chapter has no transitional provision (F15) | | history notes |

Not encoded, for contrast: a large frontier developer's summaries of internal-use catastrophic-risk assessments go to the Office "every three months or pursuant to another reasonable schedule" it specifies (§ 22757.12(d)); a modified frontier AI framework is published "within 30 days" (§ 22757.12(b)(2)).

## Fork register

| id | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | § 22757.13(c)(1); § 22757.15(a) | Is a frontier developer that is not large bound to report, and what follows if it does not? | The duty's subject is "a frontier developer"; the penalty's is "A large frontier developer". | Both as written: every frontier developer must report; only a large one is subject to the § 22757.15 penalty. SB 53 SEC. 5(c) keeps duties under other law, which is not encoded. |
| F2 | § 22757.11(i)(1), (j), (c)(1) | Are the thresholds inclusive? | "greater than 10^26", "in excess of five hundred million dollars", "more than 50 people", "more than one billion dollars". | Strict in every case: exactly 10^26 operations, $500,000,000, 50 people or $1,000,000,000 is not enough. Tested on both sides. |
| F3 | § 22757.11(h), (i) | When is a model a frontier model, and a person a frontier developer? | (i) "was trained using" more than 10^26 operations; (h) a person who "has trained, or initiated the training of, a frontier model, with respect to which the person has used, or intends to use" at least that much. | A frontier model has already used more than 10^26 operations (counting fine-tuning and other modifications, (i)(2)). A frontier developer has trained or begun training a foundation model for which it has used or intends to use more than 10^26; the developer states the largest figure over all its foundation models. So a developer can be a frontier developer while the model in an incident is not yet a frontier model, and then that event is not a critical safety incident. |
| F4 | § 22757.13(c)(1), (2) | What does "Subject to paragraph (2)" do? | R-A: where (2) applies, its 24-hour disclosure displaces the 15-day report; R-B: both are owed. | R-B. The two can both be performed, (2) names a different recipient, and nothing in (2) says it replaces (1). Open question 3. |
| F5 | § 22757.11(c), (d)(2) | When has a catastrophic risk "materialized"? | R-A: the event the risk describes has happened: a frontier model, doing one of (A) to (C), materially contributed to death or serious injury of more than 50 people or more than $1,000,000,000 of property damage, from a single incident, and no exclusion applies; R-B: any harm from conduct of kinds (A) to (C), whatever its size. | R-A, because the risk is defined by its size and R-B drops it. Exclusion (c)(2)(C) is met by the "materially contribute" requirement. Equity value is left out (§ 22757.16). |
| F6 | § 22757.11(d) | How is an event that fits two kinds handled? | The kinds overlap (a weights theft that kills fits (1); a loss of control that kills fits (3)). | Every kind that fits is listed; one report covers the incident. Nothing in the chapter makes the kind change the clock. |
| F7 | § 22757.11(e); § 22757.13(c)(1), (a)(4) | Is an incident with a model not yet deployed reportable? | "Deploy" is defined, but the duty is for any incident "pertaining to one or more of its frontier models", and a report states "Whether the incident was associated with internal use of a frontier model". | Reportable: deployment is not an element. "pertaining to ... its frontier models" is read as a frontier model the developer trained or began to train. |
| F8 | § 22757.13(c)(4); § 22757.11(d) | (c)(4) speaks of "critical safety incidents pertaining to foundation models that are not frontier models", but every kind in (d) names "a frontier model". | R-A: (c)(4) means events that would be critical safety incidents if the model were a frontier model; R-B: (c)(4) has no field of application. | R-A, as an encouragement only: the answer is "not required but encouraged". Open question 4. |
| F9 | § 22757.13(c)(1); Code Civ. Proc. §§ 12, 12a | How are the 15 days counted? | The chapter states no rule. Code Civ. Proc. § 12 (and Civ. Code § 10, Gov. Code § 6800): exclude the first day, include the last. § 12a(a): a last day that is a holiday moves to the next day that is not; "holiday" includes every Saturday; § 12a(b): it applies to "all other provisions of law ... whether expressed in this or any other code". | Both applied: last day = day of discovery + 15, moved past Saturdays (§ 12a(a)), past Sundays (§ 135, which makes a holiday of every day Gov. Code § 6700 designates, and § 6700(a)(1) "Every Sunday"), and past any other § 135 / § 12b holiday the developer lists. Only Saturdays and Sundays are computed. The fixed-date and nth-weekday holidays of § 6700 and § 135 (1 January, Thanksgiving and the day after, and the rest) are NOT computed, so a last day that falls on one of them is wrong unless the developer lists it; with an empty list the answer is the EARLIEST possible last day, assuming no holiday but Saturdays and Sundays. Vintage: the deposited § 6700 took effect 2026-03-26 (Stats. 2026, ch. 7); for a last day before that date the Sunday rule rests on that later text, because the earlier text was not read. The answer gives both the 15th day and the extended last day. Whether § 12a reaches a duty to report to an agency, as distinct from a court filing, is open question 5. |
| F10 | § 22757.13(c)(1), (2) | What is "discovering", and whose? When do the 24 hours start? | Undefined: the developer as an organization, an employee, an automated monitor? (2) begins "If a frontier developer discovers that a critical safety incident poses an imminent risk". | The developer states the date it discovered the incident (15 days) and the hours since it discovered the imminent risk (24 hours). The encoding does not decide whose knowledge counts. Open question 2. |
| F11 | SB 53 SEC. 5(d), (e) | Is the chapter preempted, enjoined, or displaced by a federal contract? | A legal conclusion, and a moving one (see "Federal preemption" below). | Two inputs, "in force and not preempted as applied to me" (the `@desc` says answer yes unless displaced) and "a federal-government contract strictly conflicts". `main` has no defaults, so the presumed value is in the `@desc`. |
| F12 | § 22757.13(c)(2) | Is the 24-hour duty limited to incidents with the developer's own frontier models? | (1) says "pertaining to one or more of its frontier models"; (2) says only "a critical safety incident". | Literal: not limited. A frontier developer that discovers an imminent-risk critical safety incident with another developer's frontier model must disclose it. Contestable; open question 6. |
| F13 | § 22757.15(a) | What counts as one violation? | Per incident, per day late, per report? | Not stated. The developer gives a count; the answer is the count times $1,000,000 as the most, and $1,000,000 per violation. |
| F14 | § 22757.15(a); § 22757.13(c)(2), (i)(2)(B) | Does "fails to report an incident as required by Section 22757.13" reach a failed 24-hour "disclose"? Does it reach a failure to meet the designated federal standard, which (i)(2)(B) calls "a violation of this chapter"? | Yes (it is a failure to tell an authority about an incident as § 22757.13 requires); or no ("report" in (c)(1) and (c)(3) is to the Office, (c)(2) says "disclose"). | For the 24-hour disclosure the answer says the penalty applies only if § 22757.15 reaches it. The federal-standard failure is not encoded as a penalty case. Open question 7. |
| F15 | history notes; no transitional provision | An incident discovered before 1 January 2026? | The chapter took effect that day and says nothing about earlier discoveries. | "not covered", never a guessed date. Tested on 31 December 2025 and 1 January 2026. |
| F16 | § 22757.13(c)(2) | Is a disclosure at exactly 24 hours "within 24 hours"? | Yes; or only before the 24th hour ends. | Yes. Tested at 23.5, 24, 24.5 and 25 hours. |
| F17 | § 22757.11(i)(2) (src:41) | Does a developer that fine-tunes another's foundation model count the base model's original training run toward the 10^26 threshold? | R-A: yes, (i)(2) includes "the original training run" with later modifications, so the fine-tuned model is a frontier model and the fine-tuner, which "has trained" it, may be a frontier developer; R-B: no, "the developer applies" limits the count to one developer's own runs. | Not decided by the encoding: the compute inputs are single numbers and their `@desc` asks for the original run plus later modifications, leaving the fine-tuner to choose. Raised by the independent author. Open question 10. |
| F18 | § 22757.11(j) (src:42) | "in the preceding calendar year": preceding what? | R-A: the year before the act or omission (the discovery, or the last day to report); R-B: the year before the question is asked. | Not decided: revenue is one number the developer gives, and the `@desc` says only "the preceding calendar year". The readings differ only for a question asked in a later year than the discovery. Raised by the independent author. |
| F19 | § 22757.13(c)(2) (src:93) | What does "and as required by law" add to the 24-hour disclosure? | R-A: it qualifies the choice of authority (the one other law makes appropriate); R-B: it limits the duty to disclosures other law already requires; R-C: it imports other law's form and content requirements. | The encoding names no recipient and computes nothing from the phrase; the answer is "an appropriate authority". Raised by the independent author. |
| F20 | § 22757.13(g)(1), (3) (src:100) (src:102) | Does the Office publish its annual report? When is the first one due? | (g)(1) "Beginning January 1, 2027" the Office "shall produce" a report; (g)(3) it "shall transmit" it "to the Legislature, pursuant to Section 9795, and to the Governor". The text says transmit, not publish, and does not say whether the first report is due on or after 1 January 2027. | Inert for the seat: no answer turns on it. The coverage table's "annual report" row is read as a transmission to the Legislature and the Governor, not a publication. Raised by the independent author. |

### Open disagreement on F14

The independent author's answer (its F13) is that a missed 24-hour disclosure is a failure "to report an incident as required by Section 22757.13" (§ 22757.15(a)), so the penalty applies as for a missed 15-day report.
This encoding answers that the penalty applies only if § 22757.15 reaches that failure.
`tests-independent.l4` line 564 (line 536 before the author's revision of 23d3485ea) asserts the author's reading and fails; it is kept failing on purpose, as the record of the disagreement, and declared as an expected red in `check.sh` (`expected_failed`) and `encoding.json` (`expected_red`). Its expected value was not edited.
The three lines both readers rest on, quoted mechanically (`srcrefs.py quote`):

```
-- src:92 | (c) (1) Subject to paragraph (2), a frontier developer shall report any critical safety incident pertaining to one or more of its frontier models to the Office of Emergency Services within 15 days of discovering the critical safety incident.
-- src:93 | (2) If a frontier developer discovers that a critical safety incident poses an imminent risk of death or serious physical injury, the frontier developer shall disclose that incident within 24 hours to an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law.
-- src:94 | (3) A frontier developer that discovers information about a critical safety incident after filing the initial report required by this subdivision may file an amended report.
```

(c)(1) "report[s]" to the Office; (c)(2) "disclose[s]" to "an authority"; (c)(3) calls the Office filing "the initial report required by this subdivision".
The author judged the text open and, if anything, leaning toward this encoding's hedged answer.
Neither reading is adopted as the law; open question 7.

The lines F17 to F20 rest on, quoted the same way:

```
-- src:41 | (2) The quantity of computing power described in paragraph (1) shall include computing for the original training run and for any subsequent fine-tuning, reinforcement learning, or other material modifications the developer applies to a preceding foundation model.
-- src:42 | (j) “Large frontier developer” means a frontier developer that together with its affiliates collectively had annual gross revenues in excess of five hundred million dollars ($500,000,000) in the preceding calendar year.
-- src:93 | (2) If a frontier developer discovers that a critical safety incident poses an imminent risk of death or serious physical injury, the frontier developer shall disclose that incident within 24 hours to an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law.
-- src:100 | (g) (1) Beginning January 1, 2027, and annually thereafter, the Office of Emergency Services shall produce a report with anonymized and aggregated information about critical safety incidents that have been reviewed by the Office of Emergency Services since the preceding report.
-- src:102 | (3) The Office of Emergency Services shall transmit a report pursuant to this subdivision to the Legislature, pursuant to Section 9795, and to the Governor.
```

## Federal preemption and the status of the chapter on 2026-10-24

What could be established, with the source and date of each statement:

- The Legislative Counsel's code table, updated 2026-10-03, lists all seven sections of Chapter 25.1 as active, with no amendment (primary; read 2026-10-24).
- A federal executive order of 11 December 2025 directed the Justice Department to set up an AI Litigation Task Force against state AI laws (secondary: web search results of 2026-10-24 summarizing law-firm and research notes; not checked against the order).
- A Cloud Security Alliance research note dated 2026-04-04 said no complaint had yet been filed by that task force and no federal court had invalidated a state AI law (secondary; not checked).
- Nothing was found, in a single web search on 2026-10-24, reporting that SB 53 has been enjoined, held preempted or suspended; that is an absence of a search result, not evidence that no such order exists.

**Could not establish** whether the chapter is enjoined, preempted or suspended as of 2026-10-24.
The encoding takes "the chapter is in force and not preempted as applied to me" as an input, presumed yes in its `@desc`, and every answer turns on it (tested both ways).

## What the chapter does not contain

Each searched for in the deposited text of §§ 22757.10 to 22757.16 (by reading, and by `grep` for the words in quotes):

- **No definition of "discover" or "discovering"** ("discover" appears only in § 22757.13(c)(1) to (3)).
- **No rule for counting days or hours**: no "calendar day" ("calendar" appears only in "preceding calendar year", (j)), no "business day"; "hour" appears only in (c)(2). Hence Code Civ. Proc. §§ 12, 12a (F9).
- **No form or format for a report** beyond the four items the Office's mechanism takes (§ 22757.13(a)); no deadline for the Office to set up that mechanism.
- **No period for an amended report** ((c)(3)), for a (c)(4) report, or for the (i)(1) declaration.
- **No named recipient of the 24-hour disclosure**, and no definition of "imminent", "serious physical injury" or "bodily injury".
- **No penalty for a frontier developer that is not large**, no minimum penalty, no rule for counting violations, and no private right of action: the penalty is "recovered in a civil action brought only by the Attorney General".
- **No transitional provision** for incidents discovered before 1 January 2026, and no repeal or sunset date ("repeal" and "operative" do not occur in the chapter).
- **No duty to tell users or the public** about an incident ("notify" and "notice" do not occur).
- **No deployment condition** on the reporting duty (F7).
- **No deemed compliance through a non-federal regime** (Finding 2).

## Coverage table

| provision | disposition |
| --- | --- |
| § 22757.10, short title | inert (quoted) |
| § 22757.11 opening words | inert (quoted) |
| § 22757.11(a) "Affiliate" | encoded as a gloss: revenue is stated with affiliates |
| § 22757.11(b) "Artificial intelligence model" | encoded: asked as a fact |
| § 22757.11(c)(1), (2) "Catastrophic risk" | encoded (F5) |
| § 22757.11(d)(1) to (4) "Critical safety incident" | encoded (F6) |
| § 22757.11(e) "Deploy" | inert: the reporting duty does not turn on it (F7) |
| § 22757.11(f) "Foundation model" | encoded |
| § 22757.11(g) "Frontier AI framework" | inert: used only by § 22757.12 |
| § 22757.11(h) "Frontier developer" | encoded (F3) |
| § 22757.11(i)(1), (2) "Frontier model" | encoded (F2, F3) |
| § 22757.11(j) "Large frontier developer" | encoded (F2) |
| § 22757.11(k) "Model weight" | inert: a gloss on kind (1) |
| § 22757.11(l) "Property" | inert: a gloss on the dollar input |
| § 22757.12(a) frontier AI framework, including (a)(8) "Identifying and responding to critical safety incidents" | out-of-scope: a publication duty of large frontier developers, not a reporting clock |
| § 22757.12(b) annual review; publication of a modified framework within 30 days | out-of-scope: as above |
| § 22757.12(c) transparency report at deployment | out-of-scope: a publication duty at deployment, not incident reporting |
| § 22757.12(d) internal-use risk summaries to the Office every three months | out-of-scope: a periodic reporting duty about assessments, not incidents; its failure is a § 22757.15 "fails to ... transmit" case |
| § 22757.12(e) false or misleading statements | out-of-scope: not incident reporting |
| § 22757.12(f) redactions | out-of-scope: applies to documents published under § 22757.12, not to incident reports |
| § 22757.13(a) the Office's mechanism and its four items | encoded (what a report gives) |
| § 22757.13(b)(1) internal-use summary mechanism | out-of-scope: belongs to § 22757.12(d) |
| § 22757.13(b)(2) the Office limits access to internal-use reports | inert: an official's duty |
| § 22757.13(c)(1) 15-day report | encoded (F1, F4, F7, F9, F10, F15) |
| § 22757.13(c)(2) 24-hour disclosure | encoded (F4, F10, F12, F16) |
| § 22757.13(c)(3) amended report | encoded |
| § 22757.13(c)(4) encouraged reports | encoded (F8) |
| § 22757.13(d) the Office reviews reports | inert: an official's act |
| § 22757.13(e) the Attorney General or the Office may pass reports on | inert: an official's discretion; recorded in the reporting module |
| § 22757.13(f) Public Records Act exemption | encoded |
| § 22757.13(g) the Office's annual report from 1 January 2027 | inert: an official's duty |
| § 22757.13(h) designation of federal standards by regulation | encoded as part of an input (whether a designation and declaration are in effect) |
| § 22757.13(i)(1), (2) declaration and deemed compliance | encoded |
| § 22757.13(j) revocation of a designation | encoded as part of the same input |
| § 22757.14 Department of Technology's review of the definitions; Attorney General's whistleblower report | out-of-scope: officials' duties; no effect on a reporting duty until the Legislature acts |
| § 22757.15(a) civil penalty, as to failing to report | encoded (F1, F13, F14) |
| § 22757.15(a) civil penalty, other failures | out-of-scope: not incident reporting |
| § 22757.15(b) Attorney General only | encoded |
| § 22757.16 equity value | encoded (in the dollar input's `@desc` and the catastrophic-risk rule) |
| SB 53 SECTION 1, findings | inert: not quoted in the modules |
| SB 53 SEC. 2 | the chapter itself (above) |
| SB 53 SEC. 3, Gov. Code § 11546.8 (CalCompute) | out-of-scope: a public computing consortium; no duty on developers |
| SB 53 SEC. 4, Labor Code §§ 1107 to 1107.2 (whistleblowers) | out-of-scope: duties toward covered employees, not incident reporting; another subject |
| SB 53 SEC. 5(a) severability, (b) liberal construction, (c) cumulative duties | inert (quoted); (c) noted in F1 |
| SB 53 SEC. 5(d) federal-contract conflict, (e) federal preemption | encoded as inputs (F11) |
| SB 53 SEC. 5(f) local preemption | inert: protects the developer from local rules adopted on or after 1 January 2025; no reporting effect |
| SB 53 SEC. 6, public-access findings | inert |
| Code Civ. Proc. § 12; Civ. Code § 10; Gov. Code § 6800 | encoded (F9) |
| Code Civ. Proc. § 12a | encoded (F9): Saturdays computed; other holidays as below |
| Code Civ. Proc. § 12b (an office closed for the whole of a day) | deposited; deferred: taken from the developer's list of holiday dates, not computed |
| Code Civ. Proc. § 135 (judicial holidays: the days Gov. Code § 6700 designates, with five exceptions, plus every Saturday and the day after Thanksgiving) | encoded for Sundays (with § 6700(a)(1)); deferred for every other day: taken from the developer's list |
| Gov. Code § 6700(a)(1) "Every Sunday" | encoded: Sundays computed (the text in force from 2026-03-26; the earlier text was not read) |
| Gov. Code § 6700, the other holidays (fixed dates such as 1 January, nth weekdays, Thanksgiving and the day after under § 135, lunar and Hindu-calendar dates) | deposited; deferred and NOT computed: a last day on one of them is wrong unless the developer lists it, so the answer is the earliest possible last day. Computing the holiday calendar (fixed dates, nth weekdays, lunar and Hindu-calendar dates, § 135's exceptions, Good Friday's three hours) is deferred |

Three rows are `deferred`, all for the holiday calendar: the encoding computes Saturdays and Sundays and takes every other holiday as a list of dates the developer gives.

## How the expected dates were worked out

By counting on a calendar, before running anything. 1 January 2026 is a Thursday.

- Discovered Monday 2 March 2026: 15 days on is Tuesday 17 March. Reported 17 March: in time; 18 March: late.
- Discovered Thursday 1 January 2026: Friday 16 January.
- Discovered Friday 6 March 2026: the 15th day is Saturday 21 March, a holiday under § 12a(a); Sunday 22 March is a holiday too (Gov. Code § 6700(a)(1) "Every Sunday", made a judicial holiday by Code Civ. Proc. § 135); so **Monday 23 March**, with no holiday listed. Listing Sunday 22 March as well changes nothing. A report on 23 March is in time; on 24 March, late. If Monday 23 March were another holiday, the developer would have to list it. (Sunday 22 March 2026 is before 26 March 2026, when the deposited Gov. Code § 6700 took effect; that it was a holiday rests on the later text, because the earlier text was not read.)
  History: the first version computed only Saturdays and gave Sunday 22 March for an empty list; the independent author found that every Friday discovery got a Sunday last day. Sundays are now computed, and `tfaia-tests.l4`'s expectations for these cases were changed with the rule.
- Discovered Friday 9 October 2026: Saturday 24 October, so Monday 26 October (in time on 26 October, late on 27); a listed Sunday 25 October changes nothing.
- Discovered Friday 18 December 2026: Saturday 2 January 2027, so Monday 4 January 2027.
- Discovered Friday 22 May 2026: Saturday 6 June, Sunday 7 June, so Monday 8 June; with Monday 8 June listed, Tuesday 9 June.
- Discovered Saturday 7 March 2026: the 15th day is Sunday 22 March, so Monday 23 March. (The same vintage caveat: Sunday 22 March 2026 is before 2026-03-26.)
- Discovered Sunday 23 August 2026: 8 days to 31 August, 7 more to Monday 7 September; with 7 September listed, Tuesday 8 September; a listed 4 September changes nothing.
- Discovered Sunday 20 December 2026: 11 days to 31 December, 4 more to Monday 4 January 2027.
- The 24-hour clock: 23.5 and 24 hours in time, 24.5 and 25 late.
- Penalty: one violation, at most $1,000,000; three, $3,000,000; two, $2,000,000.

## Corrections made while testing

Two assertions ("not a frontier developer" when the model is not a foundation model) were first written with 2 × 10^26 as "the most operations on any foundation model", which by that input's own `@desc` says another foundation model is over the line, so the developer IS one (F3).
The inputs were changed to 0; the expectation was not changed.

## Independent test pass

**Method.**
A separate model session, which had not seen this encoding being built, read the deposited sources whole (the chapter, the chaptered bill, the time-computation sections, their `.meta.json` and `SOURCE-LICENSE.md`) and wrote its answers to the seat's questions in `tests-independent-answers-first.md` before opening the encoding.
One exception, which that file records: while finding `check.sh`'s settings it saw `encoding.json`'s fork list before it read this NOTES.md.
It then read the modules for names and types, wrote `tests-independent.l4` (122 assertions), ran it, and only then read NOTES.md and `tfaia-tests.l4`; it says nothing in its answers was changed after the encoding was opened.
This encoding did not edit `tests-independent.l4`.
The author is a model agent, not a person qualified in California law, so agreement between the two shows consistency between two readings of the same text, not faithfulness to the law.

**Result.**
Against the encoding as first committed (`f565d699b`): 122 assertions, **121 satisfied, 1 failed, 0 refused**, the same on both main column groups.
The one failure (then line 536, now line 564) is the F14 disagreement above, kept as an expected red.

**Revision after Sundays were computed (`23d3485ea`).**
When this encoding began to compute Sundays as holidays (`4def2fa92`), nine of the author's assertions failed (then lines 432, 439, 451, 458, 466, 467, 471, 493 and 508): each had asserted the Saturday-only rule's answer for an empty holiday list, a Friday or Saturday discovery whose last day was a Sunday and is now the Monday after.
The author, not this encoding, re-derived those nine by hand from the newly deposited Code Civ. Proc. § 135 and Gov. Code § 6700 and kept each original as a comment (commit `23d3485ea`, recorded in its header and in `tests-independent-answers-first.md`).
Its "no listed holidays" assertions whose last day is 1 January, Thanksgiving or the day after now test the encoding's input contract (those days must be listed), not the law.
After the revision: 122 assertions, **121 satisfied, 1 failed (line 564, the expected red), 0 refused**; `check.sh` exits 0.

**Negative control (the author's).**
In a scratch copy of the encoding, changing `the days to report` from 15 to 14 and the frontier-model test from "greater than 10^26" to "at least" made 40 of its assertions fail.

**Agreements, each tested on both sides by the author:** every threshold strict; intended compute counts for frontier-developer status but a model is a frontier model only once over the line (F3); kinds (1) and (3) need death or bodily injury and kind (4) needs none; the materialization reading (F5); 15 days with the first day excluded and a Saturday last day extended (F9); every frontier developer reports and only a large one is penalised (F1); up to $1,000,000 per violation, Attorney General only; (c)(4) encouraged only (F8); the two duties cumulative (F4); exactly 24 hours in time (F16); discoveries before 2026-01-01 not covered (F15); deemed compliance and SEC. 5(d), (e); the four report items; the Public Records Act exemption; the amended report as a permission.

**Readings only this encoding asserts:** F12 (the 24-hour duty reaches another developer's frontier model); the author took no position and did not test it.

**What it added:** forks F17 to F20; the Sunday finding (above, and under "How the expected dates were worked out"), which led to depositing Code Civ. Proc. §§ 12b and 135 and Gov. Code § 6700 and to computing Sundays; and the list below.

## Not exposed by the baseline

The independent author found these points the exported questions cannot show, because the baseline takes them as one number, one list, a constant, or not at all:

- the revenue period and affiliate aggregation: revenue is one number, so "preceding calendar year" (F18) and who counts as an affiliate are the developer's to apply;
- a fine-tuner's compute: one number, so F17 is the developer's to apply;
- which days other than Saturdays and Sundays § 135 (with § 12b and Gov. Code § 6700) makes holidays: a list the developer gives;
- who receives the 24-hour disclosure: the answer says "an appropriate authority" and names none (F19);
- that there is no minimum penalty and no private right of action: stated only in the answer's wording;
- the § 22757.13(i)(2)(B) violation (failing a designated federal standard) as a penalty case: not encoded (F14);
- the date from which the penalty can apply: no date input on the penalty question;
- the Office's duties under § 22757.13(e) (passing reports on) and (g) (the annual report): inert (F20).

## What `check.sh` prints

Run on 2026-10-24 with `L4=/Users/mengwong/.cache/l4-main/99/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
tests-independent.l4                           1       121       1        0         1 |      1       121       1        0  same
tfaia-definitions.l4                           0         0       0        0         0 |      0         0       0        0  same
tfaia-domain.l4                                0         0       0        0         0 |      0         0       0        0  same
tfaia-penalty.l4                               0         0       0        0         0 |      0         0       0        0  same
tfaia-reporting.l4                             0         0       0        0         0 |      0         0       0        0  same
tfaia-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
tfaia-tests.l4                                 0        94       0        0         0 |      0        94       0        0  same
TOTAL (7 modules)                              1       215       1        0           |      1       215       1        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Exit status 0.
`tfaia-tests.l4` has 94 `#ASSERT` lines and 94 are satisfied.
`tests-independent.l4` has 122 and 121 are satisfied; the one failure, at line 564, is expected (F14, "Open disagreement") and is declared in `check.sh`'s `expected_failed` table and in `encoding.json`'s `expected_red`, so the run is green with it and red if the count changes.
All modules: 215 satisfied, 1 failed (the expected red), 0 refused.
The error counted against `tests-independent.l4` is that failure.
Both column groups are the same main build (99); the comparison says nothing about `unstable`, which is not the target.
No module prints a warning, and none prints "is at the end of the file" or "follows code on its line" (checked with `l4 check` on each module).
The encoding has no `#TRACE`.

Also run:

- `python3 -I srcrefs.py check --strict ../../registers/source-bundle/ca-bpc-div8-ch25-1-tfaia-2026-10.txt tfaia-*.l4`: `srcrefs check: 92 src: lines, 22 runs, 49 locators, 0 problems`.
- A negative control, in a scratch copy: one expected date changed (7 September to 8 September 2026) gave exactly one failed assertion (logged twice, as every outcome is), so the harness can fail.

## Links to other encodings (not code)

- `eu/ai-act-2024` (Article 73) and `eu/gpai-code-of-practice-2025` (Commitment 9) encode comparable serious-incident clocks for the EU. The California chapter's federal route (§ 22757.13(h), (i)) can designate only federal instruments, so neither EU regime can stand in for a California report (Finding 2).
- The whistleblower provisions SB 53 added to the Labor Code (§§ 1107 to 1107.2) would be a separate California subject.

## Open questions for a domain expert

1. Does any law outside Chapter 25.1 impose a penalty on a frontier developer that is not large and fails to report (F1, SB 53 SEC. 5(c))?
2. Whose knowledge is "discovering", and when does an organization discover an incident (F10)?
3. Does "Subject to paragraph (2)" ever displace the 15-day report (F4)?
4. What does § 22757.13(c)(4) reach, given that every kind of critical safety incident names a frontier model (F8)?
5. Does Code Civ. Proc. § 12a extend a reporting deadline owed to an agency, and which days are holidays under §§ 135 and 12b (F9)?
6. Is the 24-hour duty limited to the developer's own frontier models (F12)?
7. Does § 22757.15 reach a failed 24-hour disclosure, or a failure to meet a designated federal standard (F14)? How are violations counted (F13)?
8. Has the Office of Emergency Services designated any federal standard under § 22757.13(h), and what has it prescribed for its reporting mechanism? (Not checked: the Office's site was not read beyond one unrelated PDF.)
9. What is the status of federal preemption litigation against the chapter as of the date of use (F11)?
10. Does a fine-tuner count the base model's training run (F17)? From what date is "the preceding calendar year" measured (F18)?

## Before relying on it

A second reader for the readings only this encoding asserts (F12, F14); a reader qualified in California law to read each rule against the text (HG1); answers to the open questions, each of which would change outputs; and a check of the chapter's status (amendment after 2026-10-03, preemption, injunction) on the date of use.
