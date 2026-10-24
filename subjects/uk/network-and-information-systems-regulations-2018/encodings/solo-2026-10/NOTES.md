# UK Network and Information Systems Regulations 2018: incident notification, from an AI model provider's seat

**Not for use as advice.**
This is a first draft.
No domain expert and no lawyer qualified in the law of any part of the United Kingdom has read it against the source.
Gates HG1 and HG2 have not been sought.

**The source is an aid, and the encoding was NOT checked against the official text.**
legislation.gov.uk answered every request from this session with an AWS WAF challenge (HTTP 202, `x-amzn-waf-action: challenge`, no content), which the brief treats as a no; it was not worked around.
The text encoded is the revised text as re-served by Lex, an experimental API of the UK government's Incubator for AI, which says its data is sourced from legislation.gov.uk (role `aid`; see "Method and edition").
Every "verified" below means compared with that aid text in this session, and nothing more.

## Why this subject

The UK has no AI-specific serious-incident reporting duty on AI providers that the coordinator could find, and this session found none either (see "What the UK statute book does not contain").
A secondary paper (Arcadia Impact / The Future Society, arXiv 2608.19278, 18 Aug 2026; secondary source, not checked) reports that the UK has no binding AI-incident-reporting duty: a non-binding AISI evaluation template reaches providers, and the UK's binding provisions are borrowed from sectoral regimes.
The nearest **binding** notification clocks an AI provider could be subject to are cyber and data regimes.
This encoding takes the Network and Information Systems Regulations 2018 (S.I. 2018/506) as the UK's in-force borrowed channel and asks the seat's real question: "I run an AI model service: am I in scope, and if so what must I notify, to whom, by when, and what happens if I don't?"

**These Regulations are not an AI incident law, and nothing here says an AI provider is an RDSP.**
Whether a hosted AI model, API or chat service is a "cloud computing service", an "online search engine" or an "online marketplace" under regulation 1 is a fork the text leaves open (F1).
The encoding asks it as an explicit input with no default, allows "I cannot say", and tabulates both answers.

## Method and edition

- **Method.** Solo workflow of the `encoding-a-subject` skill: one session, a pinned brief (with its scope cut), a coverage table, nouns first, tests written by hand from the source and a calendar, `check.sh` against a main build, `srcrefs.py check --strict` over every quotation.
  An independent test pass has been run (see "Independent test pass" below): 71 assertions, all satisfied.
- **Source.** `../../registers/source-bundle/uksi-2018-506.txt`: the `full_text` field of the JSON returned by `POST https://lex.lab.i.ai.gov.uk/legislation/text` for `uksi/2018/506` with schedules, written out unchanged; the JSON is deposited beside it (`uksi-2018-506.lex.json`, sha256 `79804ad2…304e08`).
  Retrieved 2026-10-24T01:35:04Z.
  Role: **aid**.
  A second aid, `../../registers/source-bundle/eur-2018-151.txt`, is the UK text of Commission Implementing Regulation (EU) 2018/151 from the same API (retrieved 2026-10-24T01:55:59Z; Lex `valid_date` 2022-01-12), because regulation 12(7)(a) points to its Article 3; it contains Articles 3, 4 (shown omitted) and 5 only.
  Its form differs from the register: the provisions inserted after 2018 (14A, A20, 19A, 8A, 19B) come first, each provision is labelled "Section N)", Schedule 1's table is flattened onto one line, omitted words show as "..." or a row of dots, and no Schedule 3 appears.
- **Edition.** One: the revised text Lex labels `valid_date` 2026-09-30, `modified_date` 2026-10-02 (publisher "Statute Law Database", status "revised"), record created 2026-10-03.
  **Not checked:** whether any effect took place between 2026-09-30 and 2026-10-24, and whether any effect is outstanding (unapplied) in this text; the register's "changes to legislation" panel was unreachable.
  Lex's amendment index (an aid) lists 385 effects from these instruments: S.I. 2018/629, 2019/653, 2019/1444, 2020/1245 (246 effects), 2021/1461, 2023/424, 2024/706, 2026/230, 2026/386, and ukpga 2022/31 (the Health and Care Act 2022, title from a Lex lookup).
  None of those instruments was read.
- **Target compiler: `main`.** Written and run with `1.6.99 (main, 6cc2c91, 2026-10-21)`.
- **Licence of the source:** Open Government Licence v3.0, read on Lex's page and on The National Archives' OGL page on 2026-10-24 (`SOURCE-LICENSE.md`).

### Source gate (2026-10-24, about 09:32 to 09:41 SGT)

| request | answer |
| --- | --- |
| `https://www.legislation.gov.uk/robots.txt` (twice) | 202, `x-amzn-waf-action: challenge`, 0 bytes |
| `https://www.legislation.gov.uk/uksi/2018/506/data.xml` | 202 challenge, 0 bytes |
| `https://www.legislation.gov.uk/uksi/2018/506` | 202 challenge, 0 bytes |
| `https://www.legislation.gov.uk/help` | 202 challenge, 0 bytes |
| `https://www.bailii.org/robots.txt` | 200; disallows `/uk` for every user agent, so not pursued |
| `https://webarchive.nationalarchives.gov.uk/robots.txt` | 405, an AWS WAF "Human Verification" page |
| `https://lex.lab.i.ai.gov.uk/robots.txt` | 404 (no robots file); `/openapi.json`, `/legislation/lookup` (three times), `/legislation/text` (twice), `/amendment/search` (twice), the landing page and four searches: 200; 14 requests in all |
| `https://bills.parliament.uk/robots.txt` | 403, a Cloudflare "Just a moment..." challenge |
| `https://bills-api.parliament.uk/api/v1/Bills?SearchTerm=Cyber%20Security%20and%20Resilience` | 200 (`robots.txt` 404) |

Earlier deposits in `subjects/uk/` record fetching legislation.gov.uk through a relay in London after the same challenge; that route is a workaround and was not used.

## Seat

**The provider** of an AI model service: a company asking whether the NIS Regulations bind it and, if so, what it must notify, to whom, by when, and what can be done to it if it does not.
Every input is a fact that company can state: what kind of service it provides (with "I cannot say" allowed), where its head office is, whether it has a UK representative, whether it is a micro or small enterprise, whether it has been designated an OES, what the incident did, when it became aware, when it notified, what enforcement notice it was served and what it did about it.
The Information Commission, the competent authorities, GCHQ and the CSIRT get no seat; where the Regulations address them, the encoding says only what the provider must give them and what they may do to it.
Design defaults (CLAUDE.md, 2026-10-18) followed: judgments the text leaves to the provider ("substantial", "significant" impact) or to the authority (the regulation 18(6)(c)/(d) determination) are asked as facts and answered conditionally; borrowed terms (information society service, micro or small enterprise, OES designation) are asked as facts; the Regulations' own definitions ("digital service", "RDSP", "incident", "material contravention") are worked out from facts.
No default was departed from.

## What is encoded, and what is not

Encoded: regulation 1's definitions that decide scope and "incident" (1(2) "cloud computing service", "digital service", "digital service provider", "incident", "OES", "online marketplace", "online search engine", "representative"; 1(3)(d), (e) and (f)); regulation 3(1)-(2) (whom to notify); regulation 8 as a fact; regulation 11(1)-(3) (the OES's duty and clock); regulation 12(1), (3), (4), (6)(a), (7) and (9) (the RDSP's duty and clock, and the OES's notice of an RDSP incident); regulation 14A(1)-(2) (who must nominate a UK representative); regulation 17(1)(a)-(d) and 17(2)(a)-(d) (the failures that count); regulation 18(1), (2), (5), (6) and (7)(a) (the penalty ceilings and the material-contravention test); EU Regulation 2018/151 Articles 3 and 4 as quoted, inert (the parameters for "substantial", and no threshold).
Regulation 14A and EU Regulation 2018/151 were deferred items, taken up after the must-haves were tested and `check.sh` was clean.
Still deferred for time on 2026-10-24: Schedule 2's sector thresholds, and regulation 14A(3)'s three-month clock (F13).
Everything else is a coverage-table row.

| module | what it holds |
| --- | --- |
| `nis-domain.l4` | nouns only: the provider's self-description (with the three-valued classification answer), the event, a moment on one clock, the three notification duties, what happened to a notification, the enforcement-notice position, the authority's view, the two readings of F3 |
| `nis-regulations.l4` | the rules, one place per provision, every rule with an `@ref` and source locators |
| `nis-seat.l4` | the baseline: seven `@export` questions from the provider's seat, every input with an `@desc` |
| `nis-tests.l4` | 90 assertions by the encoder, expected values by hand |
| `tests-independent.l4` | 71 assertions by an independent author, who wrote `tests-independent-answers-first.md` from the source before opening the encoding |

The seven exported questions: Do the NIS Regulations apply to me? Must I nominate a UK representative? Must I notify this incident? Whom must I notify about this incident? By when must I notify? Was my notification within 72 hours? What is the most I can be penalised for failing to notify?

**Units and counting, for any reader of the exported questions.** The clocks are in **hours**, not days or business days: the last moment is exactly 72 hours (4,320 minutes) after the moment of awareness, on one clock, to the minute.
A notice at 72h00m is in time ("no later than 72 hours after"); at 72h01m it is late.
Times are given as a date plus an hour (0-23) and a minute (0-59); the Regulations name no time zone, so every time must be on the same clock (for example UTC).
The RDSP's clock starts when it is "first aware that an incident has occurred" (12(6)(a)); the OES's when it "is aware that a NIS incident has occurred" (11(3)(b)(i)); see F2.
Hour and minute inputs out of range are not rejected; they are counted as given.

## Where the text differs from the brief

Each checked against the deposited aid text; the text wins.

1. **No Schedule 3.** The brief puts the penalties in "regs 15-19, Schedule 3".
   The aid text has Schedules 1 and 2 only; the tiers are in regulation 18(6) and the "material contravention" test in 18(7)(a).
   Regulation 19 shows only a row of dots (omitted); appeals are now regulations 19A and 19B.
2. **Regulation 14 is registration, not the representative.** Regulation 14 is "Registration with the Information Commission"; the UK representative is regulation 14A (deferred) and a limb of the RDSP definition, 1(3)(e)(i).
3. **"Information Commission", not "Information Commissioner".** The aid text says "Information Commission" throughout (0 occurrences of "Information Commissioner").
   Lex's amendment index (an aid) attributes 36 effects to S.I. 2026/386, among them word substitutions by its Sch. 3, para. 24 in regulations 1(3)(f), 12, 17 and 18; that instrument was not read.
4. **The OES's clock runs from awareness of "a NIS incident"**, that is one with a significant impact on continuity (11(1)), not of "an incident": "no later than 72 hours after the operator is aware that a NIS incident has occurred" (11(3)(b)(i), src:299).
   The RDSP's runs from when it "is first aware that an incident has occurred" (12(6)(a), src:342). See F2.
5. **Confirmed as the brief states:** the 72-hour periods with "without undue delay"; the content lists (11(3)(a), 12(5)); the impact factors (11(2), 12(7)); the Information Commission as competent authority for RDSPs (3(2)); the ceilings £1,000,000, £8,500,000 and £17,000,000 (18(6)(a), (c), (d)); and that the highest tier needs a material contravention the authority determines "has or could have created a significant risk to, or significant impact on, or in relation to, the service provision" (18(6)(d)).
   18(6)(b) is omitted (a row of dots).
6. **No threshold for "substantial".** Regulation 12(7)(a) points to Article 3 of EU Regulation 2018/151; in the deposited aid text, Article 3 lists what the RDSP must be able to estimate or identify, and Article 4 ("Substantial impact of an incident") is a row of dots, omitted (eur-2018-151.txt lines 12-13).
   So the deposited aid text sets no numeric threshold (whether the official text does was not checked), and none is borrowed from the EU text.
7. **The Bill is not law** (see below).

## Answer table: notification

For one incident, from the provider's seat.
"Aware" is the moment the clock starts, as F2 describes; "72 hours" is 4,320 minutes on one clock (F4).

| route | who must notify | which incidents | to whom | outer limit | provision |
| --- | --- | --- | --- | --- | --- |
| RDSP | an RDSP (1(3)(e)): provides a digital service in the UK; head office in the UK or a nominated UK representative; not a micro or small enterprise | an incident with a substantial impact on the provision of its online marketplace, online search engine or cloud computing service, if it has information to assess that | the Information Commission | 72 hours after it is first aware that an incident has occurred | 12(3), (4), (6)(a); 3(2) |
| OES | a designated or deemed-designated OES | a NIS incident: significant impact on the continuity of its essential service | its designated competent authority (Schedule 1) | 72 hours after it is aware that a NIS incident has occurred | 11(1), (3)(b)(i); 3(1) |
| OES relying on an RDSP | an OES | a significant impact on continuity caused by an incident affecting an RDSP it relies on | its designated competent authority | **none stated**: "without undue delay" only | 12(9) |

**F1 tabulated, for a typical AI model provider** (an information society service provided in the UK, head office in the UK, not a micro or small enterprise, not an OES, an incident with a substantial impact and the information to assess it):

| its answer to "is my service a cloud computing service?" (and the other two kinds "no") | Do the Regulations apply? | Must I notify? | Whom? |
| --- | --- | --- | --- |
| yes | yes, as an RDSP only | I must notify (72 hours) | the Information Commission |
| no | no: neither an OES nor an RDSP | I need not notify under these Regulations | no one under these Regulations |
| I cannot say | only as an RDSP, and only if the service is of a kind regulation 1 names | I must notify only if it is | the Information Commission, if it is |

## Answer table: the most I can be penalised for failing to notify

Ceilings only: whether to impose a penalty, and its amount up to the ceiling, are the authority's (18(1), (2), (5)(a), regulation 23).

| the failure | enforcement notice | regulation 18(7)(a) | the authority's determination | ceiling |
| --- | --- | --- | --- | --- |
| a failure 17(1)(a)-(d) or 17(2)(a)-(d) lists | none served, or one that required no steps | material (ii) | significant risk or impact, 18(6)(d) | £17,000,000 |
| the same | the same | material (ii) | does not meet 18(6)(d) | £8,500,000 |
| the same | the same | material (ii) | not yet determined | £8,500,000, or £17,000,000 if so determined |
| the same | required steps, not taken in time | material (i) | as above | as above |
| the same | required steps, taken in time | not material (F9) | any | £1,000,000 |
| an RDSP's late notice, reading A (F3) | as above | as above | as above | as above |
| an RDSP's late notice, reading B (F3) | — | not a listed failure | — | no penalty under regulation 18 |
| an RDSP's notice short of the cross-border information 12(6)(b) requires, reading A or B (F14) | as for a late notice | as for a late notice | as for a late notice | as for a late notice |
| no failure | — | — | — | no penalty |

Which failures are listed: an OES's failure to notify a NIS incident (17(1)(b)) or to meet 11(3), which holds both the content and the 72-hour clock (17(1)(c)); an OES's failure to notify under 12(9) (17(1)(d)); an RDSP's failure to notify under 12(3) (17(2)(b)) or to give the 12(5) content (17(2)(c)).
For 12(9) only a failure to notify at all is answered; lateness and content under 12(9) answer "not answered here", because 12(9) has no 72-hour clock and no content list.
A 12(6)(b) shortfall is answered only for an RDSP; for an OES it answers "not answered here: regulation 12(6)(b) binds only an RDSP".

## Fork register

| id | where | the question | readings | taken, and why |
| --- | --- | --- | --- | --- |
| F1 | reg 1(2), src:89, 94, 106-107 | Is a hosted AI model, API or chat service a "cloud computing service" ("enables access to a scalable and elastic pool of shareable computing resources"), an "online search engine" or an "online marketplace"? | The text says nothing about AI. An API giving access to a model hosted on shared compute might be read as access to shareable computing resources, or as a software service that merely runs on them; a chat service that returns links might or might not "perform searches of, in principle, all websites". | Not chosen. Each kind is an input with three answers (yes / no / I cannot say) and no default; "I cannot say" gives a conditional answer. Both answers are tabulated above and asserted. |
| F2 | reg 11(3)(b)(i), src:299; reg 12(6)(a), src:342; reg 12(4), src:333 | When does each clock start, who must be aware, and how is awareness attributed to a company? | The OES's clock starts on awareness "that a NIS incident has occurred" (so only once it knows the impact is significant); the RDSP's on being "first aware that an incident has occurred" (any incident, before it can know the impact is substantial), even though 12(4) makes the duty depend on having information to assess substantiality. Neither says whose awareness counts. | Each trigger as written; the provider states the moment, and each `@desc` says which awareness it is. Not harmonised. Open question 2. |
| F3 | reg 17(2), src:471-475; reg 12(6), src:341-343 | Is an RDSP's notice made after 72 hours an enforceable failure? | 17(2) lists failures to "notify an incident under regulation 12(3)" (b) and to meet "the notification requirements stipulated in regulation 12(5)" (c), but not 12(6), which holds the clock; 17(1)(c) does list 11(3), which holds the OES's clock. Reading A: a late notice is a failure to notify under 12(3). Reading B: lateness alone is not a failure 17(2) lists, so neither an enforcement notice under 17(2) nor a penalty under 18(2) rests on it. | Both computed; the provider picks a reading in the penalty question. **Not** stated as "no penalty for lateness". Open question 3. This rests on the aid text; the official text was not read. The independent tester labels the two readings the other way round (its reading A is the literal one) and rates the literal reading, that lateness alone is not enforceable, as the stronger, because 17(1)(c) names all of 11(3), its timing limb included (src:465, src:299), while 17(2)(c) names only 12(5) (src:474) and 12(6) is named nowhere in 17(2); the computed outputs are unchanged. |
| F4 | regs 11(3)(b)(i), 12(6)(a) | How are the 72 hours counted, and on what clock? | Hours from the moment of awareness; no time zone is named; across a UK clock change, 72 hours and "the same clock time three days later" differ by an hour on local time. | Exactly 4,320 minutes on one clock the provider uses for every time (e.g. UTC); at 72h00m in time, at 72h01m late; to the minute. |
| F5 | regs 11(3)(b)(i), 12(6)(a), 12(9) | Does "without undue delay" require notice before the 72 hours? | It may; the text gives 72 hours only as the outer limit ("and in any event"). | The encoding gives the outer limit only and says so in the `@desc`. For 12(9), which has no outer limit, the answer is NOTHING. |
| F6 | regs 11(2), 12(7); EU Reg 2018/151 Arts 3-4 | When is an impact "significant" (OES) or "substantial" (RDSP)? | The OES and the RDSP each determine it, having regard to listed factors; 12(7)(a) points to Article 3 of EU Regulation 2018/151, which in the deposited aid text explains the parameters and shows Article 4 (thresholds) omitted; 12(7)(b) points to the Information Commission's guidance (not read). | Asked as a fact, with the factors in the `@desc`; no numeric threshold. |
| F7 | reg 1(3)(e)(i), src:117-118; reg 14A (deferred); reg 17(2)(da) | Is a provider with its head office outside the UK and no UK representative an RDSP? | Literally no: the definition requires a UK head office or a nominated UK representative. Yet 14A requires such a provider to nominate one, and 17(2)(da) lets the Information Commission serve an enforcement notice "upon a RDSP" for failing 14A, which on the literal reading it is not. | Literal: not an RDSP, asserted. Open question 4. |
| F8 | reg 1(2), "digital service", src:94 | Is the service an information society service within point (b) of Article 1(1) of Directive 2015/1535? | A borrowed term; the Directive is not deposited. | Asked as a fact. |
| F9 | reg 18(7)(a), src:532-539 | Is a listed failure a "material contravention" when an enforcement notice required steps and they were taken in time? | (i) needs a failure to take the steps; (ii) applies only where no notice was served or it required no steps. So, literally, it is neither, and the ceiling is £1,000,000 (18(6)(a)). | Literal, asserted. 18(6) leaves the determination to "the NIS enforcement authority"; the encoding computes what 18(7)(a) says. |
| F10 | reg 18(2), src:502 | What is "the duty set out in regulation (3A)"? | A slip for regulation 17(3A) (the duty to comply with an enforcement notice), which 18(1) names. | Read as 17(3A); nothing computed depends on it. Recorded, not repaired. |
| F11 | reg 18(6), src:527-531 | What does "the most I can be penalised" answer when the authority has not yet made its 18(6)(c)/(d) determination? | £8,500,000 or £17,000,000. | Both, in one answer; `the ceiling in pounds` gives the higher, £17,000,000. |
| F14 | reg 12(6)(b), src:343; reg 17(2)(c), src:474 | Is a notice short of "sufficient information to enable the Information Commission to determine the significance of any cross-border impact" an enforceable failure? | Not a 12(5) item, and 12(6) is not named in 17(2): the same two readings as F3. Found by the independent test pass: as first committed, the "what happened" input could not tell such a shortfall from a missing 12(5) item, so it was answered as a listed failure, which the literal reading does not support. | Fixed after the pass: a separate option for a 12(6)(b) shortfall, answered on F3's two readings for an RDSP and "not answered here" for an OES; five assertions added to `nis-tests.l4`. |
| F12 | reg 1(3)(e)(ii) | An OES that is a micro or small enterprise? | The small-enterprise exclusion is in the RDSP definition only. | Still an OES; asserted. |
| F13 | reg 14A(3), src:9-11 | By when must a non-UK provider nominate its UK representative? | (a) for a provider offering in the UK "on the coming into force date of these regulations": three months from that date, where "these regulations" (lower case) may be these Regulations (10 May 2018) or the instrument that inserted 14A (S.I. 2019/1444 by Lex's index; not read); (b) otherwise three months from first offering in the UK. How "within three months" is counted is not stated. | Not computed: the export says whether 14A applies and that the time limit is not computed here. |

Also observed, not encoded: regulation 14A(5) says "A nomination under paragraph (1)", where the nomination is made under paragraph (2); regulation 21(6)(b) points to "regulation 18(7)(b)" for the meaning of "enforcement authority", and 18(7)(b) is omitted in the aid text (a row of dots); regulation 1(2) shows one omitted definition ("...").
No ambiguity was looked for outside regulations 1, 3, 8, 11, 12, 14A, 17 and 18 and Article 3 of EU Regulation 2018/151.

## What the UK statute book does not contain (as far as this session could search)

**The search.** On 2026-10-24 (01:36Z and 01:49Z) through Lex, whose search is a semantic and keyword hybrid over its copy of legislation.gov.uk, **not** an exhaustive full-text search, and returns the top results only.
legislation.gov.uk's own search was unreachable (WAF challenge).

| query (all from 2018 on) | endpoint | what came back | an AI-specific incident duty on providers? |
| --- | --- | --- | --- |
| "artificial intelligence" | `/legislation/search`, 30 results | among them the National Security and Investment Act 2021 (Notifiable Acquisition) Regulations 2021 (S.I. 2021/1264), the Data (Use and Access) Act 2025, the Crime and Policing Act 2026, the Online Safety Act 2023, the Data Protection Act 2018, the Automated Vehicles Act 2024 | none identified; none of these was read beyond its search result |
| "artificial intelligence serious incident report notify" | `/legislation/search`, 30 results | the NIS Regulations 2018 among sectoral incident regimes (air accidents, spaceflight, higher-risk buildings, energy) | none identified |
| "artificial intelligence model provider must notify incident" | `/legislation/section/search`, 10 results | NIS regs 11 and 12; Space Industry Regulations 2021 reg 186; Energy Act 2023 s 274; S.I. 2021/1264 Sch 3 ("Artificial intelligence", a definition for notifiable acquisitions); assimilated EU security-incident articles | none: the only result whose text contains "artificial intelligence" is the acquisitions schedule |
| "artificial intelligence" | `/legislation/section/search`, 30 results | sections whose text contains "artificial intelligence": S.I. 2021/1264 Schs 2, 3 and 6 (acquisition definitions); Data (Use and Access) Act 2025 s 136 (a report by the Secretary of State on copyright works in AI development); S.I. 2025/557 art 6 (transfer of functions); Online Safety Act 2023 s 231 ("proactive technology"); an EU statistics annex | none |

**Not found:** any enacted UK instrument that imposes an incident-reporting duty on AI providers as such.
This is weaker than the Japanese sibling's absence finding: it rests on a non-exhaustive search of an aid copy, and the statutes listed were not read.
The AISI evaluation template is non-binding (secondary source, not checked).

**The Cyber Security and Resilience (Network and Information Systems) Bill is not law.**
The UK Parliament Bills API, 2026-10-24T01:33:34Z, for bill 4035: `"isAct":false`, `"currentHouse":"Lords"`, `"currentStage"`: `"Report stage"` in the Lords, with a sitting dated 2026-10-26; `"lastUpdate":"2026-10-22T18:54:12.6658447"`.
Nothing is encoded from it, and its clocks (24 and 72 hours in secondary reports) are not law.

## Coverage table

Regulation numbers as the aid text gives them.

| provision | disposition |
| --- | --- |
| reg 1(1) citation, commencement (10 May 2018) | inert |
| reg 1(2) "cloud computing service", "digital service", "digital service provider", "online marketplace", "online search engine" | encoded (F1, F8) |
| reg 1(2) "incident" | encoded |
| reg 1(2) "OES" | encoded (as a fact, through regulation 8) |
| reg 1(2) "representative" | encoded through 1(3)(e)(i) (F7) |
| reg 1(2) "essential service", "network and information system", "risk", "GCHQ", "First-tier Tribunal", the Directives, "EU Regulation 2018/151", the other definitions | inert: used only through the facts asked |
| reg 1(3)(a)-(c), (g) | inert |
| reg 1(3)(d) "designated competent authority for an OES" | encoded (the answer "my designated competent authority") |
| reg 1(3)(e) "RDSP" | encoded |
| reg 1(3)(f) "NIS enforcement authorities" | encoded (named in the penalty answers as "the authority") |
| reg 1(4)-(5) | inert |
| reg 1(6) application (UK, territorial sea, designated areas) | out-of-scope: territorial reach is taken as met by "I provide the service in the United Kingdom" |
| reg 2 NIS national strategy | out-of-scope: a Minister's duty; nothing for the provider |
| reg 3(1)-(2) competent authorities | encoded (whom to notify) |
| reg 3(3)-(6) | out-of-scope: duties of the authorities |
| reg 4 SPOC (GCHQ), reg 5 CSIRT (GCHQ) | out-of-scope: officials' duties; the provider notifies the competent authority, not GCHQ |
| reg 6, reg 7 information sharing | out-of-scope: officials' powers |
| reg 8(1)-(3) identification of OESs | encoded as a fact (Schedule 2 deferred) |
| reg 8(1A), (2), (2A), (4)-(11) | out-of-scope: OES identification machinery and the OES's own notice of its status; the seat asks the result |
| reg 8A OES's UK nominee | out-of-scope: an OES-only duty with no notification clock |
| reg 9 revocation | out-of-scope: officials' power |
| reg 10 OES security duties | out-of-scope: not a notification duty |
| reg 11(1)-(2) | encoded |
| reg 11(3)(a), (4) content | inert: the penalty question asks whether the required information was given |
| reg 11(3)(b) the 72-hour clock, form and manner | encoded (F2, F4, F5); form and manner inert |
| reg 11(5)-(11) | out-of-scope: what the authority and CSIRT do after notice |
| reg 11(12) guidance | inert |
| reg 12(1)-(2) RDSP security duties | encoded only as the list of services in (1); the security duties are out-of-scope |
| reg 12(3)-(4) | encoded |
| reg 12(5) content | inert: as 11(3)(a) |
| reg 12(6)(a) the 72-hour clock | encoded (F2, F3, F4) |
| reg 12(6)(b) cross-border information | encoded in the penalty question (F14) |
| reg 12(7) | encoded as a fact (F6) |
| reg 12(8), (10)-(17) | out-of-scope: what the Information Commission and CSIRT do; (10) and (17) omitted |
| reg 12(9) | encoded (no outer limit) |
| reg 13 co-operation with the EU | out-of-scope: an official's power |
| reg 14 registration with the Information Commission | out-of-scope: a registration duty with its own date, not incident notification |
| reg 14A(1)-(2) UK representative of a non-UK DSP | encoded (F7 records the interaction with 1(3)(e)) |
| reg 14A(3) the three-month time limit | **deferred** for time on 2026-10-24 (F13: which "coming into force date", and how three months is counted) |
| reg 14A(4)-(5) | inert |
| reg 15 information notices | out-of-scope: an enforcement power not needed for the penalty ceiling; failure to comply is 17(2)(e), outside 18(7)(a) |
| reg 16 inspection | out-of-scope, as reg 15 |
| reg 17(1)(a)-(d), 17(2)(a)-(d) | encoded |
| reg 17(1)(za)-(zb), (e)-(f); 17(2)(da)-(f) | out-of-scope: failures other than notification |
| reg 17(2A)-(6) procedure | out-of-scope: procedure; the seat asks the enforcement-notice position as a fact |
| reg 18(1), (2) | encoded (F10) |
| reg 18(3)-(4) procedure | out-of-scope |
| reg 18(5)-(6) | encoded (ceilings) |
| reg 18(7)(a) material contravention | encoded (F9) |
| reg 18(7)(b) | omitted in the aid text |
| reg 19 | omitted in the aid text (row of dots) |
| reg 19A-19B appeals | out-of-scope: appeal machinery |
| reg 20, A20 enforcement of penalties, civil proceedings | out-of-scope: recovery machinery |
| reg 21 fees | out-of-scope: not a sanction |
| reg 22 proceeds | out-of-scope |
| reg 23 general considerations | inert: the authority's matters before acting; whether a penalty is imposed is not encoded |
| reg 24 service, reg 25 review | out-of-scope: machinery |
| Schedule 1 competent authorities | inert: the answer names "my designated competent authority" without looking up the table (flattened in the aid text) |
| Schedule 2 essential services and thresholds | **deferred** for time on 2026-10-24 |
| EU Regulation 2018/151, Article 3 (parameters, as 12(7)(a) points to it) | inert: quoted; the RDSP's judgment is asked as a fact (F6) |
| EU Regulation 2018/151, Article 4 (substantial impact) | omitted in the deposited aid text (a row of dots); no threshold encoded |
| EU Regulation 2018/151, Article 5; Articles 1-2 | Article 5 inert (entry into force); Articles 1-2 are not in the Lex text and were not read (Article 2 concerns 12(2)(c), out of scope) |
| UK GDPR / Data Protection Act 2018 personal-data breach notification (72 hours to the ICO; secondary, not checked) | out-of-scope: a separate regime, not AI-specific; named so the crosswalk can add it |
| AISI evaluation template | out-of-scope: non-binding (secondary source, not checked) |
| Online Safety Act 2023 reporting duties | out-of-scope: a separate regime, not read |
| FCA / PRA incident reporting | out-of-scope: sectoral financial-services regimes, not read |
| Cyber Security and Resilience (Network and Information Systems) Bill | out-of-scope (not law): in the Lords at report stage on 2026-10-24 |

## How the expected times were worked out

Each by counting on a calendar, before running anything.

- 72 hours is 3 × 24 hours, so on one clock the last moment is the same time of day three calendar days later.
- Aware 2 March 2026 09:15: 3, 4, 5 March, so 5 March 09:15; 09:14 is 71h59m, 09:16 is 72h01m.
- Aware 2 March 2026 23:30: 5 March 23:30 is 72h00m; 6 March 00:00 is 72h30m.
- Aware 27 February 2026 22:30 (February 2026 has 28 days): 28 February, 1, 2 March, so 2 March 22:30; 22:31 late.
- Aware 27 February 2028 10:00 (leap year): 28, 29 February, 1 March, so 1 March 10:00.
- Aware 30 December 2026 18:00: 31 December, 1, 2 January 2027, so 2 January 2027 18:00.
- Aware 2 March 09:15, notified 5 March 08:00: 70h45m, in time.

## What `check.sh` prints

Run on 2026-10-24 with `L4=/Users/mengwong/.cache/l4-main/99/l4 ./check.sh`, `JL4_LIBRARY_PATH` unset:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
nis-domain.l4                                  0         0       0        0         0 |      0         0       0        0  same
nis-regulations.l4                             0         0       0        0         0 |      0         0       0        0  same
nis-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
nis-tests.l4                                   0        90       0        0         0 |      0        90       0        0  same
tests-independent.l4                           0        71       0        0         0 |      0        71       0        0  same
TOTAL (5 modules)                              0       161       0        0           |      0       161       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Exit status 0.
`nis-tests.l4` has 90 `#ASSERT` lines and 90 are satisfied; `tests-independent.l4` has 71 and 71 are satisfied; no assertion is expected to fail.
Both column groups are the same main build (99), the binary the brief names and the newest main build `fetch-main-l4.sh` found.
No module prints a warning. The encoding has no `#TRACE`.

Also run:

- `python3 -I srcrefs.py check --strict ../../registers/source-bundle/uksi-2018-506.txt *.l4`: `119 src: lines, 17 runs, 49 locators, 0 problems` (the `src:eur-2018-151:N` lines are checked against `eur-2018-151.txt` beside the main source).
- A negative control, in a scratch copy of `nis-tests.l4` when it had 85 assertions: two expectations edited on purpose (the 72h00m RDSP notice to `JUST FALSE`, and a UK-headquartered provider's regulation 14A answer) gave exactly two failed assertions, so the harness can fail.

Tests written by the same model that wrote the encoding show consistency, not faithfulness.

## Independent test pass

**Method.**
A separate model agent, given the brief and the deposited sources, wrote its answers to the seat's questions in `tests-independent-answers-first.md` before, by its own account, opening anything in this folder or reading these notes.
It then read the encoding only to learn its names and wrote `tests-independent.l4` (71 assertions), added in its own commit (`262690868`).
This encoding did not edit either file.

**Result.**
71 assertions: 0 errors, 71 satisfied, 0 failed, 0 refused, with the main columns the same.
With it, all five modules gave 156 satisfied against commit `262690868` (as the coordinator reported), and 161 after the fixes below, which added five assertions to `nis-tests.l4` (the block above).
None of its expectations disagreed with the encoding's outputs.
**Negative control** (reported by the tester): two of its 71 expectations, edited on purpose, failed, so that file can fail.

**What it found, and what changed.**
- F3: it labels the two readings the other way round and rates the literal reading (lateness alone not enforceable) the stronger; recorded in F3, outputs unchanged.
- F14: the "what happened" input could not tell a missing 12(5) item from a 12(6)(b) cross-border shortfall; fixed (see F14).
- The OES `@desc` now says that none of Schedule 2's services (src:621-973) is an AI model service, and every statement that there is no numeric threshold for "substantial" is now scoped to the deposited aid text.
- It also raised a reading this encoding does not compute: whether 17(2)(da), inserted after (d), is inside "(a) to (d)" for 18(7)(a) (it reads it as outside, so a 14A failure would be capped at £1,000,000); 14A's enforcement is not encoded here.

**Caveats.**
The author is a model agent, not a person qualified in UK law, so agreement shows consistency between two readings of the same text, not faithfulness to the law.
Both readings are of the same aid text; neither was checked against the official text.

## Links to other encodings (not code)

The stable `l4` cannot import across subjects, so these links are prose only, and none of these encodings was read for this one.

- `eu/ai-act-2024` (serious-incident reporting from the provider's seat, per its row in `subjects/README.md`): the EU's AI-specific duty; this session found no UK counterpart.
  Directive 2016/1148, which these Regulations implemented (their description, as Lex gives it), is not encoded here.
- `eu/gpai-code-of-practice-2025` (Commitment 9): a voluntary code with 2-, 5-, 10- and 15-day clocks for Signatories (per that encoding's NOTES.md).
- `jp/ai-promotion-act-2025`: Japan's AI Act, which that encoding finds contains no reporting duty or penalty.
- California's SB 53 and Korea's AI law are being encoded in parallel in this batch; neither is linked or read here.
- A crosswalk would place the NIS 72-hour clock (hours, from awareness, cyber incidents only, binding only on RDSPs and OESs) beside the EU AI Act's serious-incident clocks, and would add UK GDPR's 72-hour personal-data breach clock (not encoded).

## Open questions for a domain expert

1. Is a hosted AI model API, or an AI chat service, a "cloud computing service" or an "online search engine" within regulation 1(2) (F1)? Has the Information Commission said?
2. Whose awareness starts the clocks for a company, and does the RDSP's clock really start before it can assess substantiality (F2)?
3. Is an RDSP's late notice enforceable under regulation 17(2) (F3)? Does the official text of 17(2)(c) name 12(5) only, as the aid text does?
4. Is a non-UK digital service provider with no UK representative outside the RDSP definition, and if so how does regulation 14A bite (F7)?
5. Does the deposited aid text match the official revised text on 24 October 2026, including any effect after 30 September 2026 and any outstanding effect?
6. Which UK binding regimes other than NIS and UK GDPR could reach an AI provider's incident (Online Safety Act 2023, FCA/PRA rules)?
7. In regulation 14A(3)(a), which "coming into force date" is meant, and how is "within three months" counted (F13)?

## Before relying on it

The official text of S.I. 2018/506 read against the deposited aid text, provision by provision (the first thing to do, and the reason this encoding is an aid-based draft); an independent test pass; a reader qualified in UK law to read each rule against the text (HG1); answers to the open questions, each of which would change outputs; and the deferred rows (Schedule 2, regulation 14A(3)) encoded.
