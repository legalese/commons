# EU GPAI Code of Practice, Safety and Security Chapter: Commitment 9 (serious incident reporting)

**Not for use as advice.**
This is a first draft.
No domain expert and no lawyer qualified in EU law has read it against the source.
Gates HG1 and HG2 have not been sought.

## Method and edition

- **Method.** Solo workflow of the `encoding-a-subject` skill: one session, a pinned brief, tests written by hand from the source and a calendar, `check.sh` against a main build, `srcrefs.py check --strict` over every quotation.
  An independent test pass has been run (see "The independent test pass" below): 134 assertions, all satisfied.
- **Source.** `../../registers/source-bundle/cop-safety-security-2025.txt`, a `pdftotext -layout` rendering (Poppler 25.12.0) of the 43-page PDF served at https://ec.europa.eu/newsroom/dae/redirection/document/118119 (sha256 `d879f9b5…8da2f4a`, checked before use).
  Re-extracted in this session and compared byte for byte with the coordinator's extraction: identical.
  Role: authoritative, as the Code's own text (it is a voluntary code, not legislation).
  Page numbers below are the printed ones, which equal the PDF's (checked on ten pages).
- **Edition and vintages.** One.
  **The PDF's text states no date, no version and no version history** (its 43 pages were searched; the front matter is a title page of names).
  The brief's "July 2025" is not in the text.
  The PDF's metadata, which is not part of the text, carries an XMP creation date of 2025-08-01 and a Commission sensitivity label set on 2025-07-09.
- **Target compiler: `main`.** Written and run with `1.6.99 (main, 6cc2c91, 2026-10-21)`; `check.sh` compared it with the newest main build its `fetch-main-l4.sh` found, which is the same build 99, so both column groups are main.
- **Licence of the source: UNDETERMINED** as to ownership (CC BY 4.0 if EU-owned). See `SOURCE-LICENSE.md`.

## Seat

**The provider** of a general-purpose AI model: a company deciding whether the Code binds it and, if it does, what it must report, to whom, by when, and how long it must keep the records.
Every input is a fact that provider can state (whether it is a Signatory, how its model is linked to each harm, when it became aware, what corrective measures it adopted and when).
The AI Office and the national competent authorities get no seat; where the Code addresses them, the encoding says only what the provider must give them and by when.
Design defaults (CLAUDE.md, 2026-10-18) followed: judgments the Code leaves open ("serious", "exceptional circumstances", "similar", "if possible") are asked as facts and answered conditionally; the Code's own term 'resolved' is worked out from facts; borrowed AI Act terms ('general-purpose AI model with systemic risk', 'serious incident') are asked as facts.
No default was departed from.

## What is encoded, and what is not

Encoded: Commitment 9 in full (the chapeau as inert text; Measures 9.1, 9.2, 9.3 with all four paragraphs, and 9.4), the Glossary terms Commitment 9 relies on ('model', 'including', 'resolved'), and the Code's status as far as the Chapter states it (Objectives A and B, Recital (b)).
Not encoded: Commitments 1 to 8 and 10, the Appendices, and the Code's other chapters, which are not in this PDF.
The places where other Commitments use Commitment 9's information are listed in the coverage table and are out of scope.

Modules, in reading order:

| module | what it holds |
| --- | --- |
| `cop-domain.l4` | nouns only: the provider's standing, the incident's seven harm links, the four points of Measure 9.3, corrective measures, the nine items of Measure 9.2, Measure 9.1's facts |
| `cop-commitment-9.l4` | the rules, one place per provision, every rule with an `@ref` and source locators |
| `cop-seat.l4` | the baseline: seven `@export` questions from the provider's seat, every input with an `@desc` |
| `cop-tests.l4` | 85 assertions by the encoder, expected values by hand |
| `tests-independent.l4` | 134 assertions by an independent author, who decided every answer before opening the encoding |

Beside them, `tests-independent-answers-first.md` is that author's record of the answers, written before the encoding was opened.

The seven exported questions: Does this Code bind me? By when must I make my initial report? When is my next intermediate report due? When is my final report due? Does my report give the required information? May I include a later similar incident in the first one's reports? How long must I keep the records?

## Where the text differs from the brief

Each was checked against the deposited text; the text wins.

1. **'serious incident', 'Signatory' and 'systemic risk' are not defined in the Chapter's Glossary** (pp. 29-33).
   The Glossary defines 'near miss' (p. 31), 'resolved' (p. 32) and 'model' (p. 30), among others.
   Its preamble says "Wherever this Chapter refers to a term defined in Article 3 AI Act, the AI Act definition applies" (p. 29, src:1137).
   'systemic risk' is quoted from Article 3(65) AI Act in Appendix 1's "LEGAL TEXT" box (p. 34, src:1388-1391), and Recital (i) refers to "the definition of 'systemic risk' in Article 3(65) AI Act" without quoting it (p. 5, src:149); the Chapter gives it no meaning of its own.
   'serious incident' is not defined or quoted anywhere in the PDF, and neither is the AI Act paragraph that defines it.
   'Signatory' is used throughout and defined nowhere.
2. **The Chapter does not say how a provider becomes a Signatory.** Nothing in its 43 pages describes signing, adhering or withdrawing. The encoding asks "Are you a Signatory?" as a fact.
3. **The Chapter never cites Article 55(1)(c).** Commitment 9's header reads "LEGAL TEXT: Article 55(1), and recitals 114 and 115 AI Act" (p. 25, src:989), and Objective A speaks of "the obligations provided for in Articles 53 and 55 AI Act" (p. 2, src:30-31).
   On the relationship to Article 55, the text says only Objective A: the Code is "a guiding document for demonstrating compliance", and "adherence to the Code does not constitute conclusive evidence of compliance". The encoding asserts that, and nothing about the consequences of not signing.
4. **No date or version in the text** (above).
5. **Confirmed as the brief states:** two, five, 10 and 15 days after the Signatories "become aware of the involvement of their model in the incident"; "save in exceptional circumstances"; both routes ("led to" and "establish or suspect with reasonable likelihood"); intermediate reports "at least every four weeks after the initial report" for unresolved incidents; the final report "not later than 60 days after the serious incident has been resolved"; the multiple-similar-incidents permission; retention "for at least five years from the date of the documentation or the date of the serious incident, whichever is later" (pp. 26-27).

## Answer table: the reporting clocks

All counted in calendar days (F6) from the day the provider became aware of its model's involvement (F7), for a Signatory whose model is a general-purpose AI model with systemic risk.

| report | when it is owed | last day | Measure, page |
| --- | --- | --- | --- |
| initial, point (1) | a serious and irreversible disruption of the management or operation of critical infrastructure | awareness + 2 days | 9.3, first paragraph, point (1), p. 26 |
| initial, point (2) | a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks | awareness + 5 days | 9.3, point (2), p. 27 |
| initial, point (3) | a death of a person | awareness + 10 days | 9.3, point (3), p. 27 |
| initial, point (4) | serious harm to a person's health, an infringement of Union-law obligations protecting fundamental rights, or serious harm to property or the environment | awareness + 15 days | 9.3, point (4), p. 27 |
| initial, any point | exceptional circumstances apply | **none stated** | 9.3, first paragraph, p. 26 |
| initial, two or more points | the Code does not say which clock governs | every applicable date, the earliest and the latest (F9) | 9.3, first paragraph, pp. 26-27 |
| intermediate | the incident is unresolved | "at least every four weeks after the initial report": latest report + 28 days (F11) | 9.3, second paragraph, p. 27 |
| final | the incident is resolved | resolution + 60 days | 9.3, third paragraph, p. 27 |
| retention | all documentation gathered under Commitment 9 | at least five years from the later of the documentation's date and the incident's date (F14, F15) | 9.4, p. 27 |

The initial report gives items (1) to (7) of Measure 9.2; the final report "all the information required by Measure 9.2", items (1) to (9); an item not yet held is recorded as such (p. 26).
Contrast: other Measures count in **business days** (Measure 1.4, "within five business days", p. 10, src:327; Measure 3.5, 30 business days, p. 15; Measure 7.7, five and 15 business days, pp. 22-23).
Measure 9.3 says "days" and "weeks", and is encoded in calendar days; nothing from the business-day provisions is borrowed.
Commitment 10's retention period ("at least 10 years after the model has been placed on the market", Measure 10.1, p. 28) is a different duty and is not encoded.

## Fork register

| id | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | throughout | Who is a Signatory, and how does one become one? | The Chapter never says. | Asked as a fact. |
| F2 | Recital (h), p. 4 (src:129-135) | Are SMEs and SMCs exempt from Commitment 9? | "may be exempted from some reporting commitments (Article 56(5) AI Act)", not saying which. | Inert. No exemption is encoded; the recital says an exempted Signatory "may nonetheless voluntarily adhere". Open question 1. |
| F3 | Glossary preamble, p. 29 (src:1136-1142) | What is a 'serious incident'? | Defined in Article 3 AI Act, which is not deposited here. | The encoding asks the harms Measure 9.3 names, which are what start the clocks, and does not restate the AI Act's definition. An event within a point of 9.3 that is nonetheless not a serious incident under the AI Act would still be given a clock here. Open question 2. |
| F4 | Commitment 9 chapeau, p. 25 (src:991-996) | Does "without undue delay" require reporting earlier than Measure 9.3's last day? | (a) 9.3 gives outer limits and "without undue delay" can require earlier; (b) 9.3 is what "without undue delay" means. | The encoding gives 9.3's last day and says nothing about earlier. Inert. |
| F5 | Measure 9.1(2), p. 26 (src:1008-1013) | If no direct reporting channel is available, is point (2) met? | (a) yes: the only means named is informing third parties of channels "if available"; (b) no: some other facilitation is still owed. | (a). |
| F6 | Measure 9.3, pp. 26-27 | How are "days" counted? | Calendar days with the day of awareness excluded and the last day included; or hours (48 for "two days"); or a roll-forward when the last day is a weekend or holiday (Regulation (EEC, Euratom) No 1182/71 on periods, dates and time limits is the usual EU source for such a rule; it is not deposited, and neither its terms nor its reach to a voluntary code were checked). The time zone is not stated. | Calendar days, awareness day excluded, last day included, no roll-forward: aware 2 March, point (1), last day 4 March. |
| F7 | Measure 9.3, points (1)-(4) | When does the clock start on the suspicion route? | The text: when the Signatory "become[s] aware of the involvement of their model". Where it only suspects a causal link, the text does not say when it becomes aware of the involvement. | The provider gives the date; the `@desc` says the clock runs from awareness of the model's involvement, not from the incident. |
| F8 | Measure 9.3(2), Glossary 'including', p. 29 (src:1180-1181) | Is every (self-)exfiltration of model weights, and every cyberattack, a "serious cybersecurity breach"? | (a) yes: 'including' makes the listed items "the minimum required by the term"; (b) only an exfiltration or cyberattack that is itself a serious breach. The text does not clearly say that every cyberattack qualifies: a cyberattack that breaches nothing is hard to call a breach, and 'including' qualifies "a serious cybersecurity breach". | (a), and it is **contestable**. Nothing is computed from it: there is no separate input for an exfiltration or a cyberattack, and the reading appears only in the seat's `@desc` for the cybersecurity question, which tells the provider these are included. On reading (b), a provider who followed that `@desc` and answered yes for a minor or failed cyberattack would be given a five-day clock where (b) gives none; the clock for a breach that is serious is the same on both readings. Open question 8. |
| F9 | Measure 9.3, first paragraph | Which clock governs when an incident falls within two or more points? | R-A: each point binds on its own, so one report by the earliest last day meets all; R-B: one clock governs, which the Code does not name. | Not chosen. The answer gives every applicable clock, the earliest (R-A) and the latest (the bound on R-B). The shortest is never given silently. Two harms within point (4) are one point and one clock. |
| F10 | Measure 9.3, first paragraph (src:1045) | What are "exceptional circumstances", and what time applies then? | Undefined; no other time is stated. | An input. If it is true and a point applies, the answer is "the Code sets no deadline". It qualifies the initial report only; the intermediate and final paragraphs do not carry it. |
| F11 | Measure 9.3, second paragraph (src:1068-1071) | How does "at least every four weeks after the initial report" run, and when does it stop? | R-A: no more than 28 days between one report and the next, so the next is due 28 days after the latest report made; R-B: on a fixed schedule, the initial report + 28, + 56, and so on. | R-A, because R-B lets more than four weeks pass after an early report. The duty is for "unresolved" incidents, so an incident resolved on or before the day the next report would fall due needs none; resolved on that very day is read as resolved. |
| F12 | Glossary 'resolved', p. 32 (src:1307-1309) | On what date is an incident resolved? | The day the Signatory adopted corrective measures to assess and mitigate the related systemic risks and, "if possible", to rectify the harm. | The later of those two dates; if rectifying is not possible, the systemic-risk date alone. Whether rectifying is possible is asked as a fact. |
| F13 | Measure 9.3, fourth paragraph (src:1077-1079) | What is "within the reporting timelines"? | R-A: on or before the last day for the first incident's initial report; R-B: while the first incident's reporting runs, that is on or before the last day for its final report, or at any time while it is unresolved. | Both computed. The paragraph does not say whether the later incident's own clocks are displaced; the encoding does not change them. |
| F14 | Measure 9.4 (src:1083) | Which is "the date of the serious incident" when Measure 9.2(1) gives it a start and an end? | The start date; the end date. | Both computed. |
| F15 | Measure 9.4 | Five years from 29 February? | 28 February or 1 March. | 28 February, which is what the library's `add years` gives. This is the encoding's choice, not the Code's. |

## The independent test pass

- **Method.** A separate session, given the brief and the deposited source, wrote its answers first, before opening this folder (`tests-independent-answers-first.md`, dates worked with a calculator), then opened the modules only to learn their exported names and wrote `tests-independent.l4`.
- **Caveat.** While that author looked up how the tests import the modules and spell the `YMD` shim, a grep printed some of `cop-tests.l4`'s assertions. No expectation was changed after that.
- **Result.** 134 assertions: 134 satisfied, 0 failed, 0 refused, 0 errors, on both main column groups. None of its expectations disagreed with the encoding.
- **Negative control.** Three expectations edited on purpose failed exactly three lines, so that file can fail.
- **Its statements about the AI Act** (for example the paragraph that defines 'serious incident', and what that definition contains, in its ambiguities A9 and section 0) are the independent author's and were not checked against any deposited text.

Readings the independent author left open, and did not test.
Each is asserted only in `cop-tests.l4`, by the encoder, so each rests on one reader:

| reading | fork | what `cop-tests.l4` asserts |
| --- | --- | --- |
| an incident resolved on the very day an intermediate report falls due | F11 | no intermediate report is due |
| "the date of the serious incident" for an incident with a start and an end date | F14 | both computed; no choice made |
| Measure 9.1(2) when no direct reporting channel exists | F5 | point (2) is met |
| later intermediate reports: rolling from the latest report, or a fixed schedule from the initial report | F11 | rolling; the independent file asserts only the on-schedule case, where the two readings agree |
| every exfiltration and cyberattack within point (2) | F8 | nothing: the reading is in an `@desc` only |

## Corrections after review (2026-10-24)

1. **A wrong reason, with the right outcome.** For a Signatory whose model is not a general-purpose AI model with systemic risk, "Does this Code bind me?" answered "not relevant here, because the model is not a general-purpose AI model with systemic risk", while the initial-report, intermediate-report, final-report and retention questions answered "because the Chapter does not bind me". The coordinator found it.
   `cop-tests.l4` had asserted the same wrong label for the initial report, so it could not catch it.
   Fixed: each of the four answer types has its own "because the model is not a general-purpose AI model with systemic risk" constructor, and each rule now takes its reason from `whether the Chapter binds me`, so the two cannot drift apart again.
   The mistaken expectation was corrected, with a comment saying so, and seven assertions were added: three more that the new reason is given (intermediate, final, retention), and four that the non-Signatory's reason is not given, which also run against the rules as first committed and fail there (four lines, checked).
2. **'systemic risk'.** The first version of these notes said 'systemic risk' appears "only" in Appendix 1; Recital (i) refers to the Article 3(65) definition too. Corrected above.

## Coverage table

| provision | page | disposition |
| --- | --- | --- |
| Objectives, overarching objective | 2 | inert (quoted with A and B) |
| Objectives, point A | 2 | encoded: adherence is not conclusive evidence of compliance with Articles 53 and 55 |
| Objectives, point B | 2 | inert: "providers ... who choose to rely on the Code" supports reading the Code as binding only those who adopt it |
| Recitals (a), (c) to (g) | 3-4 | out-of-scope: principles for systemic risk assessment and mitigation; no Commitment 9 rule turns on them |
| Recital (b) | 3 | encoded: the Chapter is only relevant to providers of general-purpose AI models with systemic risk |
| Recital (h) | 4 | inert (F2) |
| Recital (i), Glossary sentence | 5 | inert: applied by using the Glossary's meanings |
| Recital (i), rest | 5 | out-of-scope: interpretive guidance for Appendix 1 |
| Recital (j) | 5 | inert: reporting "is not an admission of wrongdoing" |
| Measure 1.2, points (1)(c) and (2) | 7-8 | out-of-scope: uses Commitment 9 information in risk assessment and mitigation; no reporting duty |
| Measure 1.3, ground (2) | 9 | out-of-scope: serious incidents as a ground for a Framework assessment |
| Measure 2.1, point (1)(a)(ii) | 11 | out-of-scope: information about serious incidents and near misses in risk identification |
| Measure 3.4 | 13 | out-of-scope: Commitment 9 information in risk estimation |
| Measure 3.5 | 13-15 | out-of-scope: its methods are referred to by Measure 9.1 and 9.2(9); 9.1 asks whether the provider considers them, as a fact |
| Measure 7.6, ground (4) | 22 | out-of-scope: serious incidents as a ground for updating a Model Report |
| Measure 8.1, point (2) | 23 | out-of-scope: responsibility for the response to serious incidents |
| Commitments 1 to 8 and 10, otherwise | 5-28 | out-of-scope: not pinned by the brief; none sets a serious-incident reporting duty |
| Commitment 9, chapeau | 25 | inert (F4): "without undue delay", resourcing "appropriate for the severity" |
| Commitment 9, "as applicable, to national competent authorities" (chapeau, 9.2, 9.3) | 25-27 | inert: the Code does not say when they apply; the answers give dates, not recipients |
| Measure 9.1 | 25-26 | encoded (F5) |
| Measure 9.2, first paragraph, items (1) to (9) | 26 | encoded as the list of items |
| Measure 9.2, "to the best of their knowledge, redacted ..." | 26 | inert |
| Measure 9.2, second paragraph, recording what is not yet held | 26 | encoded |
| Measure 9.2, second paragraph, investigation and level of detail | 26 | inert: a duty of effort with no computable test |
| Measure 9.3, first paragraph, chapeau | 26 | encoded: items (1) to (7); "save in exceptional circumstances" (F10); the two routes |
| Measure 9.3, points (1) to (4) | 26-27 | encoded |
| Measure 9.3, second paragraph | 27 | encoded (F11) |
| Measure 9.3, third paragraph | 27 | encoded |
| Measure 9.3, fourth paragraph | 27 | encoded (F13) |
| Measure 9.4 | 27 | encoded (F14, F15) |
| Glossary preamble | 29 | inert, applied (F3) |
| Glossary 'including' | 29 | encoded (F8) |
| Glossary 'model' | 30 | encoded: the model must be a general-purpose AI model with systemic risk |
| Glossary 'near miss' | 31 | inert: used only in 9.2(9) as an example |
| Glossary 'resolved' | 32 | encoded (F12) |
| Glossary '(self-)exfiltration of model weights' | 32 | inert: quoted beside point (2), named in the seat's `@desc` |
| Glossary 'appropriate', 'process', 'post-market monitoring', 'systemic risk assessment', 'systemic risk mitigations' | 29-32 | inert: used by Commitment 9 in duties of effort that are not computed |
| 'serious incident', 'Signatory', 'systemic risk' | — | not defined in the Glossary (see above); 'systemic risk' is quoted from Article 3(65) AI Act in Appendix 1, p. 34, and referred to in Recital (i), p. 5; inert |
| Appendices 1 to 4 | 34-43 | out-of-scope: risk taxonomy, similarly safe models, evaluations, security; no serious-incident rule |
| The Code's other chapters | — | out-of-scope: not in this PDF |

No row is `deferred`.

## How the expected dates were worked out

Each by counting on a calendar, before running anything:

- Awareness 2 March 2026. Point (1): 3, 4 March, so 4 March; 5 March is late. Point (2): 3 to 7 March, so 7 March; 8 March late. Point (3): 3 to 12 March, so 12 March; 13 March late. Point (4): 3 to 17 March, so 17 March; 18 March late.
- Awareness 31 January 2026, point (1): 1, 2 February.
- Awareness 27 February 2028 (a leap year), point (1): 28, 29 February; point (2): 28, 29 February, 1, 2, 3 March.
- Awareness 20 December 2026, point (4): 11 days to 31 December, 4 more to 4 January 2027.
- Initial report 4 March 2026, next intermediate: 27 days to 31 March, 1 more to 1 April; 2 April late. After an intermediate report on 20 March: 11 days to 31 March, 17 more to 17 April.
- Resolved 25 March 2026, final report: 6 days to 31 March, 30 in April (36), 24 in May (60), so 24 May; 25 May late. Resolved 20 March: 11 + 30 + 19, so 19 May.
- Retention: five calendar years on from the later date, so 10 March 2026 gives 10 March 2031; 15 April 2026 gives 15 April 2031; 1 February 2026 gives 1 February 2031; 29 February 2028 gives 28 February 2033 (F15).

## What `check.sh` prints

Run on 2026-10-24 with `L4=/Users/mengwong/.cache/l4-main/99/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
cop-commitment-9.l4                            0         0       0        0         0 |      0         0       0        0  same
cop-domain.l4                                  0         0       0        0         0 |      0         0       0        0  same
cop-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
cop-tests.l4                                   0        85       0        0         0 |      0        85       0        0  same
tests-independent.l4                           0       134       0        0         0 |      0       134       0        0  same
TOTAL (5 modules)                              0       219       0        0           |      0       219       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Exit status 0.
`cop-tests.l4` has 85 `#ASSERT` lines and 85 are satisfied; `tests-independent.l4` has 134 and 134 are satisfied; no assertion is expected to fail.
Both column groups are the same main build (99), because that is both the binary the brief names and the newest main build `fetch-main-l4.sh` found; the comparison therefore says nothing about `unstable`, which is not the target.
No module prints a warning, and none prints "is at the end of the file" or "follows code on its line".
The encoding has no `#TRACE`, so the blind spot `check.sh` names does not arise.

Also run:

- `python3 -I srcrefs.py check --strict ../../registers/source-bundle/cop-safety-security-2025.txt *.l4`: `126 src: lines, 21 runs, 31 locators, 0 problems`.
- A negative control, in a scratch copy: one expected date changed from 4 March to 5 March gave exactly one failed assertion, so the harness can fail.
- The independent author's negative control: three edited expectations in `tests-independent.l4` failed exactly three lines.
- The four new reason assertions (see "Corrections after review"), run against the rules as first committed, failed exactly four lines.

## Links to other encodings (not code)

- `eu/ai-act-2024`, being encoded in parallel: Article 3, whose definitions the Glossary preamble adopts, including the one for 'serious incident' (F3) and Article 3(65) 'systemic risk', which Appendix 1 quotes and Recital (i) refers to; Article 55(1), which Commitment 9's header cites; Article 56(5), which Recital (h) cites (F2); Article 73, to whose reporting obligations of third parties Measure 9.1(2) is "without prejudice"; and whatever provision makes a model a general-purpose AI model with systemic risk, which this encoding asks as a fact.
  None of these AI Act provisions was read for this encoding.
  The stable `l4` cannot import across subjects, so these links are prose only.
- `comparative/ai-content-labelling` encodes Measure 1.1 of a different code (Transparency of AI-Generated Content); nothing is shared.

## Open questions for a domain expert

1. Are SMEs or SMCs exempted from Commitment 9 under Article 56(5) AI Act, and how would a provider know (F2)?
2. Does Measure 9.3 apply only to events that are serious incidents under Article 3 AI Act, or to every event within its four points (F3)?
3. Which clock governs an incident within two points (F9)? Has the AI Office said?
4. How are the days counted, and in which time zone (F6)? Does Regulation No 1182/71 reach this Code?
5. When does a Signatory that only suspects a causal link "become aware of the involvement of their model" (F7)?
6. Is "within the reporting timelines" the initial-report clock or the whole reporting cycle (F13)?
7. Who owns the copyright in the text (SOURCE-LICENSE.md)?
8. Is every (self-)exfiltration of model weights and every cyberattack a "serious cybersecurity breach" under point (2), or only a serious one (F8)?

## Before relying on it

A second reader for the readings only one reader has asserted (listed under "The independent test pass"); a reader qualified in EU law to read each rule against the text (HG1); an answer to the open questions, each of which would change outputs; and the licence question settled.
