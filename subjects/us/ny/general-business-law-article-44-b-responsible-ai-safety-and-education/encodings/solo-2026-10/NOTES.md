# New York RAISE Act (General Business Law Article 44-B, as amended in 2026): critical safety incident reporting

**Not for use as advice.**
This is a first draft.
No domain expert and no lawyer qualified in New York law has read it against the source.
Gates HG1 and HG2 have not been sought.
The text encoded is the legislature's bill print (S.8828, signed as Laws of 2026, chapter 96), converted to plain text by us; no official consolidated text of the General Business Law and no published session law was obtained or compared.

## Method and edition

- **Method.** Solo workflow of the `encoding-a-subject` skill: one session, a pinned brief, a coverage table, nouns first, tests written by hand from the source and a calendar, `check.sh` against a main build, `srcrefs.py check --strict` over every quotation.
  An independent test pass has been run (see "Independent test pass" below): 104 assertions, 102 satisfied, 2 failed as an expected red (F18), 0 refused.
- **Sources**, both from the New York State Assembly's bill-search pages, read 2026-10-24 between 02:43Z and 02:50Z (details in `../../SOURCE-LICENSE.md` and each `.meta.json`):
  - `ny-s8828-2026-ch-96.txt`: S.8828, the chapter amendment, signed 2026-03-27 as chapter 96 of 2026. Its section 2 repeals Article 44-B as added in 2025 and adds a new Article 44-B (§§ 1420-1429); section 3 moves the 2025 act's effective date; section 5 says when it all takes effect. **This is the text encoded.** Role: authoritative (the legislature's own print; our plain-text conversion is unofficial).
  - `ny-s6953b-2025-ch-699.txt`: S.6953-B, the RAISE Act as first enacted, signed 2025-12-19 as chapter 699 of 2025 (§§ 1420-1425). Used only to say what the amendment changed. Role: authoritative, as above.
- **Why the Senate prints.** The Actions on each page record the Assembly bill being substituted by the Senate bill (A6453-B by S6953-B on 2025-06-12; A9449 by S8828 on 2026-02-25) and the Senate bill being signed. S8828's page shows `AMEND=` blank: there is no amended print, so the introduced print is the one passed. (Read on the fetched pages' Actions sections in this session; the Actions are not part of the deposited text, and the pages themselves are not deposited: their sha256 is in each `.meta.json`.)
- **Edition and vintage.** Article 44-B as re-added by chapter 96, effective 1 January 2027 (chapter 96, sections 3 and 5, verified in the deposited text). The 2025 article is a second vintage, deposited and compared (see "What chapter 96 changed") but not encoded. Whether anything enacted after 2026-03-27 amends Article 44-B was not checked.
- **Target compiler: `main`.** Written and run with `1.6.99 (main, 6cc2c91, 2026-10-21)` at `/Users/mengwong/.cache/l4-main/99/l4`; `check.sh` compared it with the same main build.
- **Licence of the sources: UNDETERMINED** for the host pages (no terms found on nyassembly.gov); see `../../SOURCE-LICENSE.md`.

## Source gate (2026-10-24, about 10:43 to 10:50 SGT)

- `https://www.nysenate.gov/robots.txt`: HTTP 403, a Cloudflare challenge page ("Just a moment..."). Not used, not worked around.
- `https://legislation.nysenate.gov/robots.txt`: connection timed out after 20 s. Not used. The Senate open-legislation API needs a key; none was registered or used.
- `https://nyassembly.gov/robots.txt`: HTTP 200, `User-agent: GPTBot` / `Disallow: /` only. The bill pages for A06453, S06953, A09449 and S08828 (term 2025) each answered HTTP 200. Fewer than 15 requests in all.
- The chapter-amendment bill number (S8828 / A9449) came from a web search result (Wikipedia, secondary); the deposited S08828 page then confirmed it ("SIGNED CHAP.96", 03/27/2026).
- `http://public.leginfo.state.ny.us/robots.txt` (the Legislative Bill Drafting Commission's laws search, which the Assembly page links as "Laws"): connection timed out after 20 s, once, at about 03:09Z. Not used.
- **Outcome: passed**, with the legislature's own bill prints. No General Construction Law text was obtained: nysenate.gov is behind the challenge and public.leginfo.state.ny.us did not answer.

## Seat

The frontier developer: a company that has trained, or begun to train, a foundation model with more than 10^26 operations, or one asking whether it is one.
Questions are asked in its voice ("Am I a frontier developer?", "Must I report this incident to the office, and by when?", "Did I report within 72 hours?", "What is the most the Attorney General can recover?").
Provisions that address only the office within the Department of Financial Services or the Attorney General are encoded for what they mean to the developer, or recorded as inert.
Where the text distinguishes a **large** frontier developer (revenue with affiliates over $500,000,000), the encoding asks for revenue and answers accordingly: the reporting duty binds every frontier developer, but the § 1427 civil penalty reaches only a large one (F1).

## What is encoded, and what is not

Modules (all import within this folder only):

- `raise-domain.l4`: nouns only (the developer and model, the incident, a moment with its UTC offset, the reporting position, report items, failures).
- `raise-definitions.l4`: § 1420(2), (3), (4), (6), (8), (9), (10) and § 1423.
- `raise-reporting.l4`: §§ 1425, 1426 (scope and exceptions); § 1422(1) (report items), (3)(a) (72 hours), (3)(b) (24 hours), (3)(c) (amended report), (6) (FOIL exemption), (8)-(10) (the federal route); chapter 96 §§ 3, 5 (effective date).
- `raise-penalty.l4`: § 1427(1), (2) (Attorney General, $1,000,000 / $3,000,000, large frontier developers only, no private action); § 1428(5) (office's $1,000 a day for a missing disclosure statement).
- `raise-seat.l4`: the baseline, 14 `@export` questions.
- `raise-tests.l4`: 70 assertions, expected values by hand.

Not encoded (rows in the coverage table): § 1421 (frontier AI framework, transparency reports, false statements, redactions), § 1422(2), (4), (5), (7) (internal-use summaries, the office's review, transmission and annual report), § 1424, § 1427(3), § 1428(1)-(4), (6), § 1429, chapter 96 §§ 1, 4.

## Where the text differs from the brief

- **Penalty reaches only large frontier developers.** The brief's "the Attorney General may sue, with civil penalties ... up to $1 million for a first violation and $3 million for subsequent ones" is right as to amounts (verified, § 1427(1)), but § 1427(1) applies "where a large frontier developer ... fails to report"; a frontier developer that is not large has the duty (§ 1422(3)(a)) and no § 1427 penalty.
- **"Subsequent" is per violation.** The text says "not to exceed three million dollars per subsequent violation", "determined based on the severity of the violation" (verified).
- **No California deemed-compliance.** The brief asked whether complying with California or a federal regime counts. Article 44-B has a federal route only (§ 1422(8)-(10)): the office designates a federal law, regulation or guidance document by regulation, and a developer that declares its intent is "deemed in compliance with subdivision three" to the extent it meets it, must copy its federal reports to the office, and commits "a violation of this article" if it fails the federal standard. Nothing in Article 44-B mentions California or any other state (verified by reading the whole deposited text; `grep -i california` finds nothing in either deposit).
- **No preemption or federal-contract clause.** Unlike SB 53's SEC. 5(d), (e), Article 44-B has no clause switching itself off for federal preemption or a conflicting federal contract. § 1424 only says its duties are cumulative.
- **The 72-hour clock has two starting events**, "a determination that a critical safety incident has occurred" or "learning facts sufficient to establish a reasonable belief that a critical safety incident has occurred" (verified, § 1422(3)(a)). The brief had both; the encoding takes whichever came first (F8).
- **The 24-hour disclosure** goes "to an authority, including any law enforcement agency or public safety agency with jurisdiction, that is appropriate based on the nature of that incident and as required by law" (verified, § 1422(3)(b)). The brief's "does not replace the 72-hour report" is consistent with "Subject to paragraph (b)" read as F4, but the text does not say so in terms.
- **Effective date 1 January 2027** (verified: chapter 96 § 3 amends chapter 699 § 3 to read "January 1, 2027"; § 5 makes chapter 96's §§ 1, 2, 4 take effect on the same date as chapter 699).
- **Signing dates** 2025-12-19 (chapter 699) and 2026-03-27 (chapter 96) were read on the fetched pages' Actions sections, which are not part of the deposited text (page sha256 in each `.meta.json`); the bill texts themselves carry no signing date.
- **Effective date as a constant, not an input.** The brief asked for the effective date as an explicit input. It is a constant here (`the day the article takes effect`, 2027-01-01), because the text fixes it (chapter 96 §§ 3, 5); the input the developer gives is the moment its clock started, and a start before that date is answered "not covered by this encoding" (F14).

## What chapter 96 changed (2025 text against 2026 text)

| Point | Chapter 699 of 2025 (as first enacted) | Chapter 96 of 2026 (encoded) |
| --- | --- | --- |
| Who must report | a "large developer" (trained a frontier model and spent over $100,000,000 in compute costs on frontier models), § 1421(4) | every "frontier developer", § 1422(3)(a) |
| What is reported | each "safety incident" (known critical harm, or one of four kinds of incident giving demonstrable evidence of increased risk of critical harm), § 1420(13) | each "critical safety incident" (four kinds), § 1420(4) |
| Frontier model | > 10^26 operations AND compute cost > $100,000,000, or a distilled model with compute cost > $5,000,000, § 1420(6) | foundation model trained with > 10^26 operations, § 1420(9) |
| Harm threshold | "one hundred or more people" or "at least one billion dollars", § 1420(7) | "more than fifty people" or "more than one billion dollars", § 1420(3) |
| Recipient | the Attorney General and the Division of Homeland Security and Emergency Services | the office within the Department of Financial Services |
| Clock | 72 hours from "learning of the safety incident" or from facts sufficient for a reasonable belief | 72 hours from "a determination" or from facts sufficient for a reasonable belief |
| 24-hour disclosure | none | § 1422(3)(b) |
| Amended report, FOIL exemption, federal route | none | § 1422(3)(c), (6), (8)-(10) |
| Penalty | up to $10,000,000 first, $30,000,000 subsequent, for violating § 1421; injunctive or declaratory relief | up to $1,000,000 first, $3,000,000 per subsequent, large frontier developers only; no injunction clause |
| Disclosure statement and fees | none | § 1428 |
| Takes effect | "on the ninetieth day after it shall have become a law" | January 1, 2027 |

All rows were read in the two deposited texts in this session.

## Answer table: the reporting clocks and consequences

| Duty | Who | Starts | Period, unit, counting | To whom | Pin |
| --- | --- | --- | --- | --- | --- |
| Report a critical safety incident | every frontier developer, for its own frontier models | the earlier of: determining that a critical safety incident occurred; learning facts sufficient to establish a reasonable belief that one occurred (F8) | 72 hours, as 4,320 minutes on the UTC scale; exactly 72:00 is in time, 72:01 is late (F10); no weekend or holiday rule (F9) | the office within the Department of Financial Services | § 1422(3)(a) |
| Disclose an imminent-risk incident | every frontier developer (not limited to its own models, F16) | discovering that a critical safety incident poses an imminent risk of death or serious physical injury | 24 hours, as 1,440 minutes on the UTC scale, inclusive | an appropriate authority, including a law enforcement or public safety agency with jurisdiction (none named, F17) | § 1422(3)(b) |
| Amended report | a frontier developer that filed an initial report | discovering more information | no period stated ("may") | the office | § 1422(3)(c) |
| Copy federal reports | a developer on the federal route | sending a federal critical safety incident report | "concurrently" | the office | § 1422(9)(b)(iii) |
| Civil penalty | large frontier developers only (F1) | a failure to report under § 1422 (24-hour disclosure: not plain, F18) | up to $1,000,000 first violation, up to $3,000,000 per subsequent violation, by severity; counting not stated (F19) | recovered by the Attorney General in a civil action; no private right of action | § 1427(1), (2) |
| Office penalty | a person developing, deploying or operating "a large frontier model" in part in New York without a current disclosure statement, with false information, or not paying an assessment (F20) | each day of failure | $1,000 a day, plus an amount equal to the assessments owed, after notice and hearing | levied by the office | § 1428(5) |

Every figure in this table was read in `ny-s8828-2026-ch-96.txt` in this session; none rests on a secondary source.

## Fork register

| # | Ambiguity | Readings | Taken | Text |
| --- | --- | --- | --- | --- |
| F1 | Does the penalty reach a frontier developer that is not large? | (a) yes, through "fails to report"; (b) no | (b) | § 1427(1): "where a large frontier developer ... fails to report an incident as required by section fourteen hundred twenty-two" |
| F2 | Are the thresholds strict? | strict / inclusive | strict: > 10^26 operations, > $500,000,000, > 50 people, > $1,000,000,000 | "greater than", "in excess of", "more than" |
| F3 | Frontier model vs frontier developer compute | model: already used; developer: used or intends to use | as stated; the developer gives the largest figure over its foundation models | § 1420(8), (9) |
| F4 | "Subject to paragraph (b)" | (a) both duties owed; (b) the 24-hour disclosure displaces the 72-hour report | (a) | § 1422(3)(a), (b) |
| F5 | When has a catastrophic risk "materialized"? | the described event at its stated size has happened and no exclusion applies | as stated | § 1420(3), (4)(b) |
| F6 | Overlapping kinds | list every kind that fits | as stated | § 1420(4) |
| F7 | Is deployment an element of the reporting duty? | no | no | § 1422(3)(a) "pertaining to one or more of its frontier models" |
| F8 | Two starting events for 72 hours | (a) earlier of the two; (b) later; (c) either, at the developer's choice | (a): each "within seventy-two hours" sentence is a deadline, so the earlier one binds | § 1422(3)(a) |
| F9 | Time zone, daylight saving, holidays | the text names no zone and no counting rule | moments carry their UTC offset and are counted on the UTC scale; no weekend or holiday extension. New York's General Construction Law was NOT deposited (nysenate.gov blocked); that it has day-counting and holiday rules (§§ 20, 25-a) is **recalled, not checked**, as is the expectation that they speak of days, not hours | § 1422(3) |
| F10 | Is exactly 72 (24) hours "within"? | inclusive / exclusive | inclusive | "within seventy-two hours", "within twenty-four hours" |
| F11 | § 1422(1) describes the office's mechanism, not the developer's report | (a) the four items are what a report gives; (b) only what the mechanism takes | (a) | § 1422(1) |
| F12 | The deposited page prints "10§26" | read as 10^26 | 10^26 | § 1420(9)(a); the § is the page's byte A7 (see meta.json); not compared with an official print |
| F13 | Federal route | one input: a designated federal standard exists, the developer has declared, and neither has been revoked | as stated; no designation is known to this session | § 1422(8)-(10) |
| F14 | Effective date and pre-2027 events | (a) a clock that started before 2027-01-01 is not covered; (b) the duty attaches on 2027-01-01 to earlier events | (a), answered "not covered by this encoding"; the date compared is the local date of the start moment. Separately: chapter 699's original § 3 ("ninetieth day after it shall have become a law") would by a plain count (2025-12-19 + 90 days = 2026-03-19, a calendar count, not a General Construction Law computation) have fallen before chapter 96 was signed (2026-03-27). Whether the 2025 article was briefly in force is not decided here; nothing in this encoding depends on it | chapter 96 §§ 3, 5 |
| F15 | "the preceding calendar year" | preceding the incident / the question / the act | not decided; revenue is one input | § 1420(10) |
| F16 | Is the 24-hour duty limited to the developer's own models? | (a) no, read literally; (b) yes, by analogy with (a) | (a) | § 1422(3)(b) "a critical safety incident" |
| F17 | 24-hour recipient | the text names a class, not an agency | none named; "as required by law" computes nothing | § 1422(3)(b) |
| F18 | Does § 1427 reach a missed 24-hour disclosure? | "fails to report an incident as required by section 1422"; (3)(b) says "disclose" | not decided; the answer says "only if" | § 1427(1), § 1422(3)(b) |
| F19 | Counting violations; "first" vs "subsequent" | not stated | the developer says whether this is its first violation | § 1427(1) |
| F20 | "large frontier model" in § 1428(5) | § 1420 defines "frontier model" and "large frontier developer", not "large frontier model" | the encoding computes only the amount and does not decide who § 1428(5) reaches | § 1428(5) |
| F21 | § 1422(6) exempts "a report of assessments of catastrophic risk from internal use pursuant to section fourteen hundred twenty-one", but those summaries are required by § 1422(2) | cross-reference error or deliberate | recorded only; not encoded (internal-use summaries are out of scope) | § 1422(2), (6) |
| F22 | Does a fine-tuner of another developer's base model count the base model's training run? | (a) yes, (9)(b) aggregates the original run; (b) no, (8) asks what "the person has used" and (9)(b) counts what "the developer applies" | not decided; the compute inputs leave it to the developer (raised by the independent tester) | § 1420(8), (9)(b) |
| F23 | Whose "determination" starts the 72-hour clock? | (a) the developer's own; (b) anyone's (the office, a court, a third party) | (a), the developer states the moment; open (raised by the independent tester) | § 1422(3)(a) "from a determination", no actor |
| F24 | What does "to the extent" limit in § 1426(1)? | (a) the university is outside only for its academic research; (b) the whole university is outside | (a): the input asks whether the question is about that academic research (raised by the independent tester) | § 1426(1) |
| F25 | Can a governmental body be a frontier developer? | "Person" is an individual or a listed business form, "or any other nongovernmental organization" | no, but not encoded: no input asks whether the developer is governmental (raised by the independent tester) | § 1420(14) |
| F26 | Is the office's annual report published? | the text says it is produced and transmitted to named officials | inert; the text does not say it is published (raised by the independent tester) | § 1422(7)(a), (c) |

Source lines for F22 to F26, quoted mechanically from `ny-s8828-2026-ch-96.txt` with `srcrefs.py quote`:

F22:

```
-- src:151 | 49 (b) The quantity of computing power described in paragraph (a) of this
-- src:152 | 50 subdivision shall include computing for the original training run and
-- src:153 | 51 for any subsequent fine-tuning, reinforcement learning, or other materi-
-- src:154 | 52 al modifications the developer applies to a preceding foundation model.
```

F23:

```
-- src:280 | 8 3. (a) Subject to paragraph (b) of this subdivision, a frontier devel-
-- src:281 | 9 oper shall report any critical safety incident pertaining to one or more
-- src:282 | 10 of its frontier models to the office within seventy-two hours from a
-- src:283 | 11 determination that a critical safety incident has occurred or within
```

F24:

```
-- src:385 | 56 § 1426. Exceptions. Nothing in this article shall apply to:
-- src:386 | S. 8828 8
-- src:387 | 1 1. accredited colleges and universities in New York state, to the
-- src:388 | 2 extent such colleges and universities are engaging in academic research
-- src:389 | 3 regarding artificial intelligence models; or
```

F25:

```
-- src:164 | 6 14. "Person" means an individual, proprietorship, firm, partnership,
-- src:165 | 7 joint venture, syndicate, business trust, company, corporation, limited
-- src:166 | 8 liability company, association, committee, or any other nongovernmental
-- src:167 | 9 organization or group of persons acting in concert.
```

F26:

```
-- src:318 | 46 7. (a) Beginning January first, two thousand twenty-eight, and annual-
-- src:319 | 47 ly thereafter, the office shall produce a report, that includes the
-- src:320 | 48 following:
-- src:333 | 4 (c) The office shall transmit a report pursuant to this subdivision to
-- src:334 | 5 the governor, the temporary president and minority leader of the senate,
-- src:335 | 6 the speaker and minority leader of the assembly, the chair and ranking
-- src:336 | 7 member of the senate committee on internet and technology, and the chair
-- src:337 | 8 and ranking member of the assembly committee on science and technology.
```

### Open disagreement on F18

The independent tester read § 1427(1)'s "fails to report an incident as required by section fourteen hundred twenty-two" as reaching a missed 24-hour disclosure under § 1422(3)(b), and wrote two assertions (`tests-independent.l4` lines 314-315) expecting the plain civil-penalty answer ($1,000,000 first, $3,000,000 subsequent).
The encoding answers "a civil penalty only if section 1427 reaches a failure to disclose within 24 hours" with the same amounts, so both assertions fail.
The tester, on its own reading of the source after the run, judged the text open and leaning toward the encoding: (3)(a) says "shall report ... to the office", (3)(b) says "shall disclose ... to an authority", and (3)(c) ties "the initial report required by this subdivision" to the office filing.
Neither side's expected values were changed; `check.sh` declares the two failures (`expected_failed`: `tests-independent.l4) echo 2 ;;`) and is red if the count changes.
The lines, quoted mechanically:

```
-- src:398 | 12 or transmit a compliant document required to be published or transmitted
-- src:399 | 13 under this article, makes a statement in violation of subdivision four
-- src:400 | 14 of section fourteen hundred twenty-one of this article, fails to report
-- src:401 | 15 an incident as required by section fourteen hundred twenty-two of this
-- src:402 | 16 article, or fails to comply with its own frontier AI framework.
-- src:280 | 8 3. (a) Subject to paragraph (b) of this subdivision, a frontier devel-
-- src:281 | 9 oper shall report any critical safety incident pertaining to one or more
-- src:282 | 10 of its frontier models to the office within seventy-two hours from a
-- src:283 | 11 determination that a critical safety incident has occurred or within
-- src:289 | 17 developer shall disclose that incident within twenty-four hours to an
-- src:290 | 18 authority, including any law enforcement agency or public safety agency
-- src:293 | 21 (c) A frontier developer that discovers information about a critical
-- src:294 | 22 safety incident after filing the initial report required by this subdi-
-- src:295 | 23 vision may file an amended report.
```

## What the Act does not contain

Read in the whole of `ny-s8828-2026-ch-96.txt` in this session:

- no provision treating compliance with California's SB 53, or any other state's law, as compliance;
- no federal-preemption or federal-contract carve-out;
- no whistleblower or employee-protection provision (SB 53 has one; `grep -iE 'whistle|employee'` finds nothing in chapter 96);
- no definition of "determination", "discovers" or "reasonable belief", and no time zone or rule for counting hours;
- no form or content of the 72-hour report beyond the office's mechanism (§ 1422(1)), and no form for the 24-hour disclosure;
- no injunctive or declaratory relief (chapter 699 had it; chapter 96's § 1427 does not);
- no private right of action (§ 1427(2) says so expressly).

## Coverage table

| Provision | Disposition |
| --- | --- |
| ch. 96 § 1 (findings) | inert: findings and intent |
| § 1420(1) affiliate | encoded (revenue "together with its affiliates" is one input) |
| § 1420(2) AI model | encoded (a fact) |
| § 1420(3) catastrophic risk | encoded |
| § 1420(4) critical safety incident | encoded, all four kinds |
| § 1420(5) deploy | inert (F7) |
| § 1420(6) foundation model | encoded |
| § 1420(7) frontier AI framework | out of scope: § 1421 |
| § 1420(8) frontier developer | encoded |
| § 1420(9) frontier model | encoded |
| § 1420(10) large frontier developer | encoded |
| § 1420(11), (13) model weight, property | inert: glosses |
| § 1420(12), (14)-(16) department, person, superintendent, office | inert: names |
| § 1421 (frameworks, transparency reports, false statements, redactions) | out of scope: publication duties, not reporting; deferred to a later pass |
| § 1422(1) mechanism contents | encoded (F11) |
| § 1422(2) quarterly internal-use summaries (large frontier developers) | deferred: a reporting duty, but not incident reporting; no time to encode its "every three months or ... another reasonable schedule" clock |
| § 1422(3)(a) 72-hour report | encoded |
| § 1422(3)(b) 24-hour disclosure | encoded |
| § 1422(3)(c) amended report | encoded |
| § 1422(4) office reviews reports | inert: addresses the office |
| § 1422(5) office may transmit; FOIL exemption on transmission | inert for the developer; noted in `raise-reporting.l4` |
| § 1422(6) FOIL exemption | encoded |
| § 1422(7) annual report from 2028-01-01 | inert: addresses the office |
| § 1422(8)-(10) federal route | encoded as one input (F13) |
| § 1423 loss of equity | encoded (left out of the dollar figure) |
| § 1424 cumulative duties | inert: no other law is encoded |
| § 1425 scope | encoded (input) |
| § 1426 exceptions | encoded (inputs) |
| § 1427(1), (2) penalty, no private action | encoded |
| § 1427(3) other causes | inert |
| § 1428(1)-(4), (6) disclosure statement, fees, publication | deferred: a registration duty, not incident reporting |
| § 1428(5) office penalty | encoded (amount only, F20) |
| § 1429 rulemaking | inert |
| ch. 96 § 3 effective date of ch. 699 | encoded (2027-01-01) |
| ch. 96 § 4 severability | inert |
| ch. 96 § 5 effect | encoded (2027-01-01) |
| ch. 699 (2025 text) | deposited, compared, not encoded (repealed and replaced) |
| General Construction Law | not deposited: host blocked (F9) |

## How the expected moments were worked out

UTC offsets: New York is UTC-5 (EST) and UTC-4 (EDT).
In 2027 daylight time starts on Sunday 14 March and ends on Sunday 7 November (1 March 2027 is a Monday, so the second Sunday is the 14th; 1 November 2027 is a Monday, so the first Sunday is the 7th; checked against Python's `zoneinfo` America/New_York in this session).

- 2027-03-01 10:00 EST + 72 h = 2027-03-04 10:00 EST. 09:59 and 10:00 are in time; 10:01 is not.
- 2027-02-10 23:30 EST + 72 h = 2027-02-13 23:30 EST (across three midnights). 23:31 and 2027-02-14 00:00 are late.
- 2027-03-13 12:00 EST = 17:00 UTC; + 72 h = 2027-03-16 17:00 UTC = 13:00 EDT. 12:59 EDT and 13:00 EDT are in time; 13:01 EDT is late. The duty answer writes the last moment in the start's offset: 2027-03-16 12:00 EST.
- 2027-11-05 12:00 EDT = 16:00 UTC; + 72 h = 2027-11-08 16:00 UTC = 11:00 EST. 11:00 EST is in time; 11:01 EST and 12:00 EST are late.
- Two triggers: belief 2027-05-08 15:00 EDT, determination 2027-05-10 09:00 EDT; the earlier governs, so the last moment is 2027-05-11 15:00 EDT; 15:01 is late.
- 24 hours: 2027-06-01 08:00 EDT to 2027-06-02 08:00 EDT inclusive; 08:01 late. Across spring forward: 2027-03-13 22:00 EST = 2027-03-14 03:00 UTC; + 24 h = 2027-03-15 03:00 UTC = 2027-03-14 23:00 EDT; 23:01 EDT late.
- Effective date: a start at 2026-12-31 23:59 EST is not covered; a start at 2027-01-01 00:00 EST gives 2027-01-04 00:00 EST.

## Independent test pass

- **Who and how.** A separate model agent wrote `tests-independent-answers-first.md` from the deposited source text before opening the encoding; it then read the modules only for the exported questions, parameters and result types (in the order its file records), wrote and ran `tests-independent.l4`, and only then read this file and `raise-tests.l4`. It states that nothing in its answers-first file was changed after the encoding was opened.
- **Result.** 104 assertions: 102 satisfied, 2 failed as a declared expected red (lines 314-315, F18; see "Open disagreement on F18"), 0 refused; the main columns are the same. Everything else agrees, including the daylight-saving crossings and the 2027-01-01 cutoff.
- **Negative controls** (the tester's, in a scratch copy of the encoding, counting the 2 standing failures): ignoring the UTC offset (a wall-clock reading) gave 20 failed; making the 72-hour test exclusive gave 20 failed; making the 10^26 test `AT LEAST` gave 16 failed.
- **Forks it raised** are F22 to F26 in the fork register.
- **What it does not show.** The tester is a separate model agent, not a lawyer; its agreement with the encoding shows consistency, not faithfulness to New York law.
- The unused input on `what must my report give` is kept: the independent tests call that question with `TRUE` and `FALSE` (lines 287 and 289), and their file is not edited here.

## Not exposed by the baseline

These are decided, or deliberately left open, inside the encoding, but no exported question lets a user see or vary them:

- the revenue period ("the preceding calendar year", F15) and how affiliates' revenues are added up: one number goes in;
- who receives the 24-hour disclosure (F17): the answer names a class, not an agency;
- that there is no minimum penalty and no private right of action (§ 1427(1), (2)): stated in `@desc` and here, not computed;
- designation of a federal standard, the developer's declaration, and revocation by either side (F13): one boolean;
- the office's annual report (§ 1422(7), F26) and its published list of large frontier developers (§ 1428(6)): inert;
- a clock starting within an hour of midnight on 2027-01-01: the effective-date test compares the local date of the start moment, in the offset the developer gives, so a start at 2026-12-31 23:30 EST and one at 2027-01-01 00:30 EST fall on opposite sides; no test pins a start given in a non-New-York offset.

## What `check.sh` prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
raise-definitions.l4                           0         0       0        0         0 |      0         0       0        0  same
raise-domain.l4                                0         0       0        0         0 |      0         0       0        0  same
raise-penalty.l4                               0         0       0        0         0 |      0         0       0        0  same
raise-reporting.l4                             0         0       0        0         0 |      0         0       0        0  same
raise-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
raise-tests.l4                                 0        70       0        0         0 |      0        70       0        0  same
tests-independent.l4                           2       102       2        0         2 |      2       102       2        0  same
TOTAL (7 modules)                              2       172       2        0           |      2       172       2        0
```

`python3 -I srcrefs.py check --strict ../../registers/source-bundle/ny-s8828-2026-ch-96.txt raise-*.l4`: 196 `src:` lines, 18 runs, 47 locators, 0 problems.

Exit status 0: the two failures in `tests-independent.l4` are the declared expected red.

Encoder's negative control: changing one expected report moment from 10:00 to 10:01 (turning the 72:00 case into a 72:01 case) gave exactly one failed assertion (`check.sh`: 69 satisfied, 1 failed), on both columns.
`raise-tests.l4` and the encoding were written by the same model session: agreement shows consistency, not faithfulness.

## Links to other encodings (not code)

- `us/ca/business-and-professions-code-division-8-chapter-25-1-transparency-in-frontier-ai` (California SB 53): the same definitions nearly word for word; 15 days instead of 72 hours; Office of Emergency Services instead of the DFS office; $1,000,000 per violation instead of $1,000,000 / $3,000,000; a preemption and federal-contract carve-out New York lacks.
- `eu/ai-act-2024` (Article 73) and `eu/gpai-code-of-practice-2025` (Commitment 9): comparable duties, not imported.

## Open questions for a domain expert

1. F8: does the earlier of the two starting events govern, as encoded?
2. F18: does § 1427 reach a missed 24-hour disclosure?
3. F14: was the 2025 article in force between its original 90th day and chapter 96's signing, and does the 72-hour duty attach on 2027-01-01 to incidents determined earlier?
4. F9: does any New York computation-of-time rule reach an hours clock?
5. F20 and F21: are "large frontier model" (§ 1428(5)) and the § 1421 cross-reference in § 1422(6) drafting slips?

## Before relying on it

Do not.
Check the text against the official Laws of New York and have a New York lawyer read the forks, F18 first.
