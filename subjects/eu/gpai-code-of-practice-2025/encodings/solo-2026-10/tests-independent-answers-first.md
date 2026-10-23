# Independent answers, decided from the source alone (STEP 1)

Written 2026-10-24 by the independent test author, BEFORE opening `encodings/solo-2026-10/`.
Source read: `registers/source-bundle/cop-safety-security-2025.txt` (pdftotext -layout of the 43-page PDF), lines cited as `txt:N`.
Pages are the printed page numbers in the rendering's footers (p.25 = txt:988-1006, p.26 = txt:1008-1053, p.27 = txt:1055-1088).
Date arithmetic below was done with a calculator (Python `date + timedelta`), not with the encoding.

## 0. What the text does and does not contain

- Commitment 9 is at txt:988-1084 (pp.25-27): chapeau, Measures 9.1, 9.2, 9.3, 9.4.
- The Glossary (txt:1136-1374, pp.29-33) defines 'near miss' (txt:1270) and 'resolved' (txt:1307), and 'model' as "a general-purpose AI model with systemic risk" (txt:1230).
- The Glossary does NOT define 'serious incident', 'Signatory' or 'systemic risk'.
  Its chapeau (txt:1137) says a term defined in Article 3 AI Act takes the AI Act definition, so 'serious incident' (Art 3(49)) and 'systemic risk' (Art 3(65)) come from the Act, which is not in this bundle.
- The document never says how a provider becomes a Signatory (no signing procedure, no form, no date). grep for "sign" outside "Signatory" finds only "assigned"/"design".
- Status statements the document does make: Objective A (txt:30-32), "a guiding document for demonstrating compliance with the obligations provided for in Articles 53 and 55 AI Act, while recognising that adherence to the Code does not constitute conclusive evidence of compliance"; Objective B (txt:34-37), providers "who choose to rely on the Code"; recital (b) (txt:62-64), the Chapter "is only relevant for providers of general-purpose AI models with systemic risk and not AI systems"; Commitment 9's header cites "LEGAL TEXT: Article 55(1), and recitals 114 and 115 AI Act" (txt:989) — Article 55(1), not 55(1)(c).
- Recital (j) (txt:153-160): reporting "is not an admission of wrongdoing"; tracking must begin before incidents occur.

## 1. Who is bound

| Facts | Answer |
|---|---|
| Not a Signatory | The Code does not bind me. No Commitment 9 clock, no report, no retention period from this Code. |
| Signatory, provides a GPAI model with systemic risk | Bound by Commitment 9. |
| Signatory, provides no GPAI model with systemic risk | Commitment 9 has nothing to bite on ('model' = GPAISR, txt:1230; recital (b) txt:62-64). Ambiguity A1 below. |

## 2. Initial report: the four clocks (Measure 9.3, txt:1042-1066, pp.26-27)

Trigger: "if the involvement of their model (directly or indirectly) led to" the harm, OR "if the Signatories establish or suspect with reasonable likelihood such a causal relationship between their model and" the harm.
Either route gives the same clock.
Neither route (no involvement, no reasonable-likelihood suspicion) gives no initial-report deadline under 9.3.
Anchor: "after the Signatories become aware of the involvement of their model in the incident" — not the incident date, not the date of learning of the incident itself.
"Days" are calendar days: the chapter says "business days" where it means them (txt:327, 866, 870, 523, 1676, 1691) and 9.3 does not.
Rule: deadline = awareness date + N; submitting on that date is in time, on the next date is late.

| Limb | Harm | N |
|---|---|---|
| 9.3(1) | serious and irreversible disruption of the management or operation of critical infrastructure | 2 |
| 9.3(2) | serious cybersecurity breach, including (self-)exfiltration of model weights and cyberattacks | 5 |
| 9.3(3) | death of a person | 10 |
| 9.3(4) | serious harm to a person's health (mental and/or physical); infringement of obligations under Union law intended to protect fundamental rights; serious harm to property or the environment | 15 |

Scenario deadlines (last in-time day; the day after is late):

| N | Aware | Deadline | First late day | Note |
|---|---|---|---|---|
| 2 | 2026-03-10 | 2026-03-12 | 2026-03-13 | plain |
| 2 | 2026-01-30 | 2026-02-01 | 2026-02-02 | month end; deadline is a Sunday |
| 2 | 2026-12-30 | 2027-01-01 | 2027-01-02 | year end; holiday |
| 2 | 2028-02-27 | 2028-02-29 | 2028-03-01 | leap day is the deadline |
| 2 | 2028-02-28 | 2028-03-01 | 2028-03-02 | leap year |
| 2 | 2027-02-28 | 2027-03-02 | 2027-03-03 | non-leap control |
| 5 | 2026-03-10 | 2026-03-15 | 2026-03-16 | deadline is a Sunday |
| 5 | 2026-01-31 | 2026-02-05 | 2026-02-06 | month end |
| 5 | 2026-12-27 | 2027-01-01 | 2027-01-02 | year end |
| 5 | 2028-02-25 | 2028-03-01 | 2028-03-02 | across leap day |
| 10 | 2026-03-10 | 2026-03-20 | 2026-03-21 | plain |
| 10 | 2026-02-20 | 2026-03-02 | 2026-03-03 | across Feb, non-leap |
| 10 | 2028-02-20 | 2028-03-01 | 2028-03-02 | across Feb, leap |
| 10 | 2026-12-22 | 2027-01-01 | 2027-01-02 | year end |
| 15 | 2026-03-10 | 2026-03-25 | 2026-03-26 | plain |
| 15 | 2026-04-20 | 2026-05-05 | 2026-05-06 | month end |
| 15 | 2026-12-17 | 2027-01-01 | 2027-01-02 | year end |
| 15 | 2028-02-14 | 2028-02-29 | 2028-03-01 | leap day is the deadline |
| 15 | 2027-02-14 | 2027-03-01 | 2027-03-02 | non-leap control |

Same awareness date (2026-03-10) across the four limbs: 2026-03-12, 2026-03-15, 2026-03-20, 2026-03-25.

### "Save in exceptional circumstances" (txt:1045)

It qualifies "at the following points in time".
The text neither defines exceptional circumstances nor states a substitute period.
Answer: where exceptional circumstances are present (taken as an input), the Code states no initial-report date (NOTHING / "not stated"); it does not borrow another period.
The chapeau's "without undue delay" (txt:993) remains, but it is not a date.

### Two or more harm categories at once

The text is silent: it lists four conditional limbs for one initial report and never says which governs when two hold.
Readings: (R1, cumulative) each limb applies by its own terms, so the single initial report must meet every applicable limb, i.e. the earliest deadline; (R2) the "most serious" or "primary" category governs; (R3) one initial report per category, each on its own clock (one could then report the 15-day aspects later).
My answer: the text does not say; under R1 the earliest applicable deadline (e.g. death + serious harm to health, aware 2026-03-10: 2026-03-20; critical infrastructure + property harm: 2026-03-12).
An encoding that silently returns the shortest clock without labelling the fork is a finding; one that returns the R1 date under an explicit R1 label, or "not stated" for a single-governing-clock question, agrees with me.

### No category / near miss

A near miss ("a situation in which a serious incident could have, but ultimately did not, materialise", txt:1270) is not one of the four harms: no initial-report deadline.
It is relevant only as data under 9.2(9) (txt:1032-1034).

## 3. Contents (Measure 9.2, txt:1015-1040; 9.3 first sentence txt:1043)

- Initial report: points (1)-(7) of 9.2, i.e. seven items: start/end dates; harm and victim; chain of events; model involved; material on the model's involvement; Signatory's response; Signatory's recommendations to the AI Office.
- Not in the initial report: (8) root cause analysis; (9) patterns from post-market monitoring incl. near-miss data.
- Intermediate report: updates the initial report's information and adds "further information required by Measure 9.2, as available" (txt:1068-1069), so (8)-(9) as available.
- Final report: "covering all the information required by Measure 9.2" (txt:1073), i.e. all nine items.
- Missing information is recorded as missing in the report (txt:1037-1039), not a ground for delay.
- Addressee: the AI Office and, as applicable, national competent authorities.

## 4. Intermediate reports (txt:1068-1071, p.27)

"For unresolved serious incidents ... at least every four weeks after the initial report."
Four weeks = 28 calendar days, anchored on the initial report (as submitted, not its deadline).
First intermediate report due: initial report date + 28.

| Initial report | First intermediate due | Late on |
|---|---|---|
| 2026-03-10 | 2026-04-07 | 2026-04-08 |
| 2026-12-15 | 2027-01-12 | 2027-01-13 |
| 2028-02-10 | 2028-03-09 | 2028-03-10 |
| 2027-02-10 | 2027-03-10 | 2027-03-11 |

Subsequent ones: ambiguous (A4). Fixed schedule from the initial report (initial + 56, + 84, ...) or rolling (last intermediate + 28).
"at least every four weeks" favours rolling (no gap longer than 28 days); "after the initial report" favours fixed. If the previous report was made exactly on schedule, both agree: initial 2026-03-10, intermediate 2026-04-07, next due 2026-05-05.
Stops: once the incident is resolved, it is no longer "unresolved", so no further intermediate report is due; the final report becomes due instead.
Resolved before the first intermediate falls due (initial 2026-03-10, resolved 2026-04-01): no intermediate report is due.
Resolved on the very day an intermediate is due: ambiguous; not tested.

## 5. Final report (txt:1073-1075, p.27) and 'resolved' (txt:1307-1309, p.32)

'resolved': "a serious incident of a model for which the Signatory adopted corrective measures to rectify the harm, if possible, and to assess and mitigate systemic risks related to it."
So resolved iff (rectifying measures adopted OR rectification not possible) AND (measures to assess and mitigate related systemic risks adopted).
"adopted", not "completed": adoption suffices.
Final report due: resolution date + 60 days; nothing is due while unresolved.

| Resolved | Final report due | Late on |
|---|---|---|
| 2026-11-01 | 2026-12-31 | 2027-01-01 |
| 2028-01-15 | 2028-03-15 | 2028-03-16 |
| 2027-01-15 | 2027-03-16 | 2027-03-17 |
| 2026-04-01 | 2026-05-31 | 2026-06-01 |

## 6. Retention (Measure 9.4, txt:1081-1084, p.27)

"for at least five years from the date of the documentation or the date of the serious incident, whichever is later".
Keep until (later of the two dates) + 5 years, the same calendar date five years on.

| Documentation | Incident | Keep until at least |
|---|---|---|
| 2026-03-10 | 2026-01-05 | 2031-03-10 (documentation later) |
| 2025-12-01 | 2026-02-01 | 2031-02-01 (incident later; documentation can predate the incident, recital (j)) |
| 2026-06-30 | 2026-06-30 | 2031-06-30 (equal) |
| 2028-02-29 | 2028-02-29 | 2033-02-28 under my reading; 2033-03-01 on the roll-over reading (A6) |
| 2027-12-31 | 2027-06-01 | 2032-12-31 (year end) |

## 7. Multiple similar incidents (txt:1077-1079, p.27)

A permission, not a duty: "may include them in the report(s) of the first serious incident, while respecting the timelines for reporting for the first serious incident".
Conditions: the later incident is similar, and it occurs within the reporting timelines (of the first incident).
Bundling never extends the first incident's deadlines.
A later incident that is not similar: no permission (report it separately).
A similar incident occurring after the first incident's reporting has ended (after its final report deadline): no permission.
Within the first incident's initial-report window: permitted.

## 8. Measure 9.1 (txt:998-1013, pp.25-26)

- "consider the exemplary methods in Measure 3.5" — consider, not adopt (Measure 3.5's eleven examples, txt:462-484).
- AND (1) review other sources: police and media reports, social media posts, research papers, incident databases (non-exhaustive: "such as").
- AND (2) facilitate reporting by downstream modifiers, downstream providers, users and other third parties to (a) the Signatory or (b) the AI Office / national competent authorities, by informing them of direct reporting channels, if available; without prejudice to Article 73 AI Act.
- Doing (1) without (2), or (2) without (1), does not meet 9.1.

## 9. Ambiguities I see (readings before looking at the encoding)

- A1. Signatory with no GPAISR model: Commitment 9 inapplicable (my reading) vs. bound but vacuous. Same practical answer: nothing to report.
- A2. Two harm categories at once: R1 earliest (cumulative) / R2 primary category / R3 per-category reports. Text silent.
- A3. Anchor on the suspicion route: the clock runs from awareness of involvement in both routes; on the suspicion route that is the date the reasonable-likelihood suspicion arose. Text uses one anchor phrase for both.
- A4. Intermediate cadence after the first: fixed from the initial report vs. rolling from the last intermediate.
- A5. Weekend/holiday deadlines: the text has no roll-forward; Regulation 1182/71 Art 3(4) would move a period ending on a Saturday, Sunday or holiday to the next working day, but the Code is not a legal act and does not import it. My answer: no roll-forward (2026-03-15, a Sunday, stays).
- A6. Five years from 29 February: 28 February (EU 1182/71 Art 3(2)(c) end-of-month rule; minimum obligation) vs 1 March (roll-over). "at least" makes 1 March safe either way.
- A7. "the date of the serious incident" for an incident with a start and an end date (9.2(1)): start or end. Not tested.
- A8. "save in exceptional circumstances" may relieve only the timing (my reading) or the initial report altogether. Either way, no date.
- A9. Category 9.3(2) (cybersecurity breach) is not in the AI Act's Art 3(49) definition of serious incident; whether 9.3(2) extends reporting to breaches that are not otherwise "serious incidents" is open. I treat it as triggering the 5-day clock.
- A10. "within the reporting timelines" for bundling: the first incident's initial-report window only, or all its timelines through the final report. My reading: all of them; both readings agree inside the initial-report window.
- A11. Bundling a later similar incident with a SHORTER clock than the first (e.g. 2-day inside a 15-day): the text requires respecting the first incident's timelines but says nothing about displacing the later one's own clock.
