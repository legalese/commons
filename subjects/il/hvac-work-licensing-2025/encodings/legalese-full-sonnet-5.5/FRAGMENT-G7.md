# FRAGMENT-G7: ENCODER G7, sections 58 to 63 and the Fourth Schedule

Status: written on 2026-10-13 by ENCODER G7 of the fleet encoding Israel's HVAC work-licensing Law 5785-2025.
Verified by running `work/g7/check-g7.sh` (its output is in section 0); not read by a domain expert; nothing here is ruled by the owner.
The INTEGRATOR merges this fragment into `NOTES.md`.
Every Hebrew quotation in this file and in the modules was produced by a script that reads `inputs/law.wiki` (`srcrefs.py quote`, `gen-fragment.py`), never typed; the English glosses are mine.
The page images of the gazette (Sefer HaChukim 3349, printed pages 197, 198, 206, 207 and 208) were viewed for ss.58 to 63 and the Fourth Schedule.

## 0. What was written, and what the check printed

Files in `deposit/` (all start with `@lang en` and have ASCII names):

| file | what it holds |
| --- | --- |
| `g7-fourth-schedule.l4` | the Fourth Schedule as data (95 items), the test that a designation or a refrigerant is listed, and a tolerant alternative |
| `g7-electrical.l4` | ss.58 and 61: the licensee as a service electrician, and the electrical work the added subsection (e) allows; the two compared (T32) |
| `g7-administrative-courts.l4` | s.62: the Administrative Courts Law, and the meeting of s.62 with s.56 (T39) |
| `g7-regulations.l4` | ss.59 and 60: the Minister's powers to set fees and make regulations, as MAY rules with their approvals |
| `g7-commencement.l4` | s.63: the commencement day, the two regimes by refrigerant, Chapter 6, the readings, and the power to amend the Fourth Schedule |
| `g7-tests-fourth-schedule.l4`, `g7-tests-electrical.l4`, `g7-tests-administrative-courts.l4`, `g7-tests-regulations.l4`, `g7-tests-commencement.l4` | tests, expected values decided from the source before any run |
| `g7-tests-red.l4` | assertions that are MEANT to fail: each states the answer of a reading the fork register rejects |
| `FRAGMENT-G7.md` | this file |

How the modules were made.
The five modules and the six test modules are generated from templates in `work/g7/tpl/` by `work/g7/build.py`, in which every Hebrew quotation is a marker that `srcrefs.py quote` expands from `inputs/law.wiki`; the build refuses a template with Hebrew or a direction mark typed into it.
The Fourth Schedule's 95 items are generated from the wiki by `work/g7/parse4.py`, with item (66) taken from the gazette, and then compared with two other readings (below).

Import graph.
The fleet lead clarified brief ruling 1: it forbids imports ACROSS groups only; the modules of one group (prefix `g7-`) may import each other if the graph is acyclic, and tests import the modules they test.
No module imports another group's module.
Every module also imports `prelude` (listed once below), and the ones that count a period or build a date also import `daydate` and the vendored `il-interpretation-time`.

```text
g7-fourth-schedule        <- prelude, domain
g7-electrical             <- prelude, domain
g7-administrative-courts  <- prelude, domain
g7-regulations            <- prelude, daydate, il-interpretation-time, domain
g7-commencement           <- prelude, daydate, il-interpretation-time, domain, g7-fourth-schedule
g7-tests-fourth-schedule        <- g7-fourth-schedule
g7-tests-electrical             <- g7-electrical
g7-tests-administrative-courts  <- g7-administrative-courts
g7-tests-regulations            <- g7-regulations (and daydate)
g7-tests-commencement           <- g7-commencement, g7-fourth-schedule (and daydate, il-interpretation-time)
g7-tests-red                    <- all five modules above (and daydate, il-interpretation-time)
```

The graph is acyclic: the only edge between two non-test modules is `g7-commencement` to `g7-fourth-schedule`, because the regime test of s.63(a)(1) needs the Fourth Schedule's list.
`check-g7.sh` fails a module that imports anything other than `prelude`, `daydate`, `il-interpretation-time`, `domain` or a `g7-` module.

What `check-g7.sh` printed on the final run (the script is the skill's `assets/check.sh` adapted to `g7-*.l4`, with two checks of its own: no warning of any kind, and `srcrefs.py check --refs` over every module):

```text
module                               errors satisfied  failed  refused  expected warnings
g7-administrative-courts.l4               0         0       0        0         0        0
g7-commencement.l4                        0         0       0        0         0        0
g7-electrical.l4                          0         0       0        0         0        0
g7-fourth-schedule.l4                     0         0       0        0         0        0
g7-regulations.l4                         0         0       0        0         0        0
g7-tests-administrative-courts.l4         0        13       0        0         0        0
g7-tests-commencement.l4                  0       107       0        0         0        0
g7-tests-electrical.l4                    0        19       0        0         0        0
g7-tests-fourth-schedule.l4               0        85       0        0         0        0
g7-tests-red.l4                          19         0      19        0        19        0
g7-tests-regulations.l4                   0        55       0        0         0        0
TOTAL (11 modules)                       19       279      19        0                  0
(a failed assertion is also an error; any other error, any warning, or any refused assertion makes the run red)

extra checks
  all modules start with '@lang en', have ASCII filenames and import only the allowed modules
  il-interpretation-time.l4 in DEPOSIT matches the brief's sha256
  l4 check: no stray @ref warnings
  srcrefs: srcrefs check: 220 src: lines, 12 runs, 127 locators, 0 problems
```

How to read it.
A failed assertion is also an error, so `g7-tests-red.l4` shows 19 errors and 19 failed, and its 19 are expected (section 2 says which fork each belongs to).
No assertion is refused, none could not be evaluated, and no module emits a warning.
`srcrefs.py check --refs` finds no problem in any quotation or locator.
`work/g7/audit-refs.py` finds no rule, type or constant without an `@ref` in the five non-test modules.
`work/g7/mutate.py` breaks one thing at a time in a scratch copy and runs the five test modules; its result is in section 0.1 (31 mutations, none survived).
`work/g7/check-gazette-text.py` reads the Fourth Schedule a third way, from the gazette's own text layer, and finds it agrees with the module's data and with my hand transcription from the page images on all 95 items (including E170 at item (66)).

### 0.1 Mutations

```text
caught  fourth schedule: item (66) back to the wiki reading 170E               fourth-schedule: 7 failed 0 refused 0 other errors
caught  fourth schedule: item (95) dropped                                     fourth-schedule: 7 failed 0 refused 0 other errors
caught  fourth schedule: item (92) misspelt                                    fourth-schedule: 4 failed 0 refused 0 other errors
caught  fourth schedule: exact test made case-blind                            fourth-schedule: 3 failed 0 refused 0 other errors
caught  commencement: later-of becomes earlier-of                              commencement: 40 failed 4 refused 0 other errors
caught  commencement: 18 months become 17 (paragraph 2)                        commencement: 17 failed 0 refused 0 other errors
caught  commencement: three months become two                                  commencement: 7 failed 0 refused 0 other errors
caught  commencement: paragraph (2) edge made exclusive                        commencement: 6 failed 3 refused 0 other errors
caught  commencement: paragraph (1) edge made exclusive                        commencement: 12 failed 0 refused 0 other errors
caught  commencement: Chapter 6 edge made exclusive                            commencement: 1 failed 0 refused 0 other errors
caught  commencement: Chapter 6 ignores the section 46 limb                    commencement: 1 failed 0 refused 0 other errors
caught  commencement: any-reading of a mixed system becomes every              commencement: 3 failed 1 refused 0 other errors
caught  commencement: unlawful listed refrigerant counted as paragraph (1)     commencement: 5 failed 0 refused 0 other errors
caught  commencement: s.10(b) replaced by 90 days                              commencement: 18 failed 1 refused 0 other errors
caught  commencement: day-after reading switched on by default                 commencement: 19 failed 3 refused 0 other errors
caught  electrical: s.58 ignores the licence                                   electrical: 2 failed 0 refused 0 other errors
caught  electrical: s.58 ignores the cooling system                            electrical: 1 failed 0 refused 0 other errors
caught  electrical: s.61 drops the First Schedule condition                    electrical: 2 failed 0 refused 0 other errors
caught  regulations: 60(2)(a) made to need approval                            regulations: 3 failed 0 refused 0 other errors
caught  regulations: 60(1)(c) consultation dropped                             regulations: 3 failed 0 refused 0 other errors
caught  regulations: approval requirement ignored                              regulations: 5 failed 0 refused 0 other errors
caught  regulations: one head of fee dropped                                   regulations: 2 failed 0 refused 0 other errors
caught  courts: additional reading loses the Administrative Court              administrative-courts: 2 failed 0 refused 0 other errors
caught  courts: s.62 ignores the input about jurisdiction                      administrative-courts: 1 failed 0 refused 0 other errors
caught  commencement: moment-level binds from midnight instead of 00:01        commencement: 1 failed 0 refused 0 other errors
caught  regulations: 60(2)(a) default stops applying IL s.10(c)                regulations: 1 failed 0 refused 0 other errors
caught  regulations: 60(2)(a) refusal replaced by a default day                regulations: 1 failed 0 refused 0 other errors
caught  regulations: paragraph (1) reading of the matters of (2) is the default regulations: 3 failed 0 refused 0 other errors
caught  fourth schedule: tolerant reading strips only U+200E                   fourth-schedule: 9 failed 0 refused 0 other errors
caught  fourth schedule: tolerant reading strips only U+200F                   fourth-schedule: 9 failed 0 refused 0 other errors
caught  fourth schedule: tolerant reading carries the unsubstituted placeholder fourth-schedule: 9 failed 0 refused 0 other errors

31 mutations, each broken alone in a scratch copy and run against the five test modules; every one was caught (survivors: none).
(One mutation of the first run, the moment-level one, broke type-checking and is replaced by the "binds from midnight" mutation of the second run; one mutation of the second run repeats the first run's "60(2)(a) made to need approval".  The last three were added with the repair of section 11.)
```

## 1. Coverage

One row per provision of my scope, in the Law's own numbering (the Hebrew letters come from the survey's `coverage.tsv`, by script).
`slice` is the disposition proposed in `slice-G7.md`; `disposition` is mine.
Nothing is `deferred`.

| provision | Law's numbering (by script) | first Hebrew words (by script) | slice | disposition | module | rules | change, and why |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s.58 | 58 | ביצוע עבודות חשמל — יראו בעל רישיון לבצע עבודה במערכת … | encoded | **encoded** | `g7-electrical` | `the licensee is treated as a service electrician under section 58`; the saving limb as inert text `s 58 — the saving of other law` | unchanged |
| s.59 | 59 | אגרות — השר, באישור ועדת העבודה והרווחה של … | encoded | **encoded** | `g7-regulations` | `Head of fee under section 59` (six heads), `s 59 — the heads of fee for which the Minister may set a fee`, `s 59 — the heads of fee for which a different rate may be set for a foreign expert's temporary licence`, `s 59 — the Law lets the Minister set a fee for`, `s 59 — the approval the Minister needs to set fees has been given`, `s 59 — the Minister's power to set a fee by regulations for … , given the procedure …` (MAY) | unchanged |
| s.60 | 60 | ביצוע ותקנות — השר ממונה על ביצוע חוק זה … | inert | **inert** | `g7-regulations` | `s 60 — the Minister is in charge of implementing the Law` (inert text); the power half of the lead-in is carried by the rows below | unchanged: a statement of responsibility with no consequence of its own |
| s.60(1) | 60(1) | באישור ועדת העבודה והרווחה של הכנסת, להתקין תקנות … | inert | **encoded** | `g7-regulations` | constructor `any matter connected with the implementation of the Law`; `s 60 — the approval of the Knesset Labour and Welfare Committee is required for regulations on`; `s 60 — the procedure required for regulations on … has been followed, given the procedure …`; `s 60 — the Minister's power to make regulations on … , given the procedure …` (MAY) | changed from inert by the fleet lead's ruling 2 (powers are encoded) |
| s.60(1)(a) | 60(1)(א) | דרישות הכשרה לשם קבלת רישיון, ובכלל זה השתתפות … | inert | **encoded** | `g7-regulations` | constructor `the requirements of training for a licence`, through the same four rules; the content of such regulations is an input and is not modelled | changed from inert by ruling 2 |
| s.60(1)(b) | 60(1)(ב) | כללים בדבר בחינות הנדרשות לקבלת תעודת גמר, ובכלל … | inert | **encoded** | `g7-regulations` | constructor `the rules on the examinations required for a final certificate, including objections`, through the same four rules | changed from inert by ruling 2 |
| s.60(1)(c) | 60(1)(ג) | תנאים לשמש בודקים או מומחים לשם הסתייעות בהם … | inert | **encoded** | `g7-regulations` | constructor `the conditions for serving as testers or experts`, through the same four rules, and `s 60(1)(c) — consultation with the Minister concerned is required for regulations on` (the consultation limb) | changed from inert by ruling 2 |
| s.60(2) | 60(2) | להתקין תקנות בעניינים אלה: | inert | **encoded** | `g7-regulations` | the same rules with approval NOT required for the two matters of paragraph (2); fork F-R-2 gives the alternative reading | changed from inert by ruling 2 |
| s.60(2)(a) | 60(2)(א) | אופן הגשת בקשה לרישיון או חידושו, הפרטים שתכלול … | inert | **encoded** | `g7-regulations` | constructor `the manner of applying for a licence or its renewal, and the time for applying to renew`; `s 60(2)(a) — the last day for an application to renew a licence` and its alternative, with the named REFUSE `s 60(2)(a) fixes the time for an application to renew by regulations, and no regulation under section 60(2)(a) is in the sources` | changed from inert by ruling 2; the missing time is a named REFUSE |
| s.60(2)(b) | 60(2)(ב) | אופן הגשת בקשה לרישיון זמני למומחה זר או … | inert | **encoded** | `g7-regulations` | constructor `the manner of applying for a temporary licence for a foreign expert, or for its renewal`, through the same rules | changed from inert by ruling 2 |
| s.61 | 61 | — הנוסח שולב בחוק החשמל, התשי״ד–1954. | out-of-scope | **out-of-scope** | `g7-electrical` | the amended statute (the Electricity Law) is not modelled; the effect of the added subsection is carried by `s 61 — the licensee may do electrical work under subsection (e) added to section 6 of the Electricity Law`, which reads three input facts and nothing of that statute's own text | unchanged |
| s.62 | 62 | — הנוסח שולב בחוק בתי משפט לעניינים … | out-of-scope | **out-of-scope** | `g7-administrative-courts` | the amended statute (the Administrative Courts Law) is not modelled; carried by `the Law is listed in item 21 of the First Schedule to the Administrative Courts Law, as section 62 adds it`, `s 62 — the decision can be taken to an Administrative Court` and the two fora functions; module moved out of g7-electrical because section 62 has nothing to do with electricity | unchanged disposition; module changed |
| s.63 | 63 | תחילה ותחולה | encoded | **encoded** | `g7-commencement` | the container; carried by the rows below | unchanged |
| s.63(a) | 63(א) | תחילתו של חוק זה, למעט פרק ו׳ – | encoded | **encoded** | `g7-commencement` | `s 63(a) — under the readings, the Law has commenced for work on the system`, the moment-level `s 63(a) and IL s.21 — …`, the work-item wrapper, and the named REFUSE for provisions that are not about work on a system, `the Law has commenced, for a provision that is not about work on a system, on the day` (trap T20) | unchanged |
| s.63(a)(1) | 63(א)(1) | לעניין ביצוע עבודה במערכת קירור או מיזוג אוויר … | encoded | **encoded** | `g7-commencement` | `s 63(a)(1) — the commencement day, under the readings` and `the commencement day under section 63(a)(1)`; `s 63(a)(1) — the refrigerant is a listed flammable refrigerant whose use is permitted by law`; `s 63(a) — the regime of the refrigerant, under the readings`; the Minister's power to amend the Fourth Schedule by order (`s 63(a)(1) — the Minister's power to amend the Fourth Schedule by order`) | unchanged |
| s.63(a)(2) | 63(א)(2) | לעניין ביצוע עבודה במערכת קירור או מיזוג אוויר … | encoded | **encoded** | `g7-commencement` | `s 63(a)(2) — the day the Law commences for a system with any other refrigerant, under the readings` and `the day the Law commences for a system with any other refrigerant under section 63(a)(2)`; `s 63(a) — the regime of the system, under the readings` | unchanged |
| s.63(b) | 63(ב) | תחילתו של פרק ו׳ 18 חודשים מיום התחילה … | refused | **refused** | `g7-commencement` | `s 63(b) — the day Chapter 6 commences, under the readings` (named REFUSE when no section 46 regulation is known), `Chapter 6 was in force on the day of the act`, and the closed-world alternative | unchanged |
| S4 | Fourth Schedule | 440A 1132a 142b 152a 403A 406A … | encoded | **encoded** | `g7-fourth-schedule` | `the Fourth Schedule` (95 items as data), `the designation is printed in the Fourth Schedule`, `a refrigerant is a listed flammable refrigerant`, and the tolerant alternative | unchanged |

18 rows: 14 encoded, 1 inert, 2 out-of-scope, 1 refused; deferred 0.

Rules that belong to no single row (helpers and readings), all in `g7-commencement.l4`: `s 63 — the day the Law commences, N months from the day … , under the readings` (the one place a period of months is counted), `s 63 — the later of … and …`, the record types `Facts that fix the commencement of the Law under section 63` and `Readings of the dates of section 63` and `Readings of the regime of section 63(a)`, and the constants that build each alternative reading.

## 2. Forks

Format: the readings, the one taken, the text that licenses each, the callable alternative and its test.
"Taken" means the default of every exported function.
Every alternative is a call of the same function with a different value of a `Readings of …` record (or a second named function), and each is tested green in the test module named; the assertion that the reading TAKEN does not give the alternative's answer is in `g7-tests-red.l4` and fails by design.
Forks that are refusals are tested green with the alternative function and with `#ASSERT REFUSED … BECAUSE "…"`.

### Kinds of period met in my scope (the brief's ruling 4)

The brief names four kinds: a deadline (D), a period of validity (V), a commencement counted from another date (C), and a window for an application (W).
Kinds met in ss.58 to 63 and the Fourth Schedule: C (the three months and the 18 months of s.63) and X (the time for a renewal application, s.60(2)(a), a length fixed by an official).
Kinds NOT met: D, V, W (the Law fixes no time for the Minister to act; the powers of ss.59 and 60 carry no `WITHIN`), and no period is counted backwards.
For C the fleet default is not to apply IL s.10(c) (fork F-C-1); for X the default is to apply it to the nominal last day the regulation gives, as for a deadline or a window (fork F-R-6).
"IL s.10(c)" is the Interpretation Law's provision; the Law has its own s.10(c).

### F-C-1 (kind C): is IL s.10(c) applied to a commencement counted from another date?

- Periods: P38 (three months from publication), P40 (18 months from the commencement day), P41 (the first limb of Chapter 6).
- Readings: (a) the commencement is the period's last day, with no shift for a day of rest; (b) IL s.10(c) moves the end when it falls on a day of rest, recess or holiday.
- Taken: (a), the fleet lead's ruling 4 (assumed, not ruled by the owner).
- Text: IL s.10(c) is unqualified ("in counting the days of a period, days of rest are counted too, unless they are the last days of the period", copied by script in `il-interpretation-time.l4`); its reach is the open question of the Interpretation row, and nothing in s.63 says it applies or does not.
- Alternative (callable): `the readings of the dates with IL s.10(c) applied, for the calendar` given to `s 63(a)(2) — …, under the readings`, `s 63(a)(1) — the commencement day, under the readings`, `s 63(b) — the day Chapter 6 commences, under the readings` and `s 63(a) — under the readings, the Law has commenced for work on the system`.
- Discriminating case: 18 months after 16.7.2025 end on Saturday 16.1.2027; with that Saturday a day of rest, (b) gives Sunday 17.1.2027.
- Tests: `g7-tests-commencement.l4`, "Fork F-C-1" (6 assertions: Saturday case, no-rest case, first limb with 14 and 15 April 2025 as rest days giving 16.4.2025, Chapter 6, work on a system on both sides of the moved day); red: the default does not give 17.1.2027 nor 16.4.2025.
- The calendar is an input (domain `Calendar of rest days`), never computed; the calendars in the tests are illustrations.

### F-C-2: what "its publication" is

- Readings: (a) the day the Law was published in Reshumot, Sefer HaChukim 3349, 14.1.2025; (b) the day the Knesset passed it, 8.1.2025 (the signature block).
- Taken: (a). The wording is "from the day of its publication"; the gazette's date line is 14.1.2025 on every page viewed (printed pages 197, 198, 206, 207 and 208).
- Text for (b): the signature block records the adoption day:

```text
-- src:1017 | {{ח:חתימות|התקבל בכנסת ביום ח׳ בטבת התשפ״ה (8 בינואר 2025).}}
```

- Alternative: the same functions with the adoption day supplied as `the day the Law was published in Reshumot` (it is an input field).
- Discriminating case: with the section 59 regulations in force early (hypothetical 1.3.2025), the first limb is 14.4.2025 under (a) and 8.4.2025 under (b).
- It does not matter on the real facts: the regulations came into force on 16.7.2025, later than either, so the commencement day is 16.7.2025 under both (tested).
- Tests: "Fork F-C-2" (2 assertions); red: the default does not give 8.4.2025.

### F-C-3: "three months from [its publication or the entry into force of the regulations], whichever is later"

- The text of s.63(a)(1):

```text
-- src:461 | {{ח:תתת|(1)}} לעניין ביצוע עבודה במערכת קירור או מיזוג אוויר הפועלת באמצעות קרר דליק המנוי {{ח:פנימי|תוספת 4|בתוספת הרביעית}}, ובלבד שהשימוש בו הותר על פי כל דין – שלושה חודשים מיום פרסומו או מועד כניסתן לתוקף של תקנות לפי {{ח:פנימי|סעיף 59|סעיף 59}}, לפי המאוחר (להלן – יום התחילה); השר, לאחר התייעצות עם השר להגנת הסביבה, רשאי לשנות, בצו, את {{ח:פנימי|תוספת 4|התוספת הרביעית}};
```

- Readings: (a) the later of two dates: the end of three months from publication (14.4.2025) and the day the section 59 regulations entered into force (16.7.2025); (b) three months counted from the later of those two days (16.7.2025 plus three months, so 16.10.2025).
- Taken: (a), which is also the survey's chain and the lead's assignment, and which treats "the entry into force of the regulations" as the date it is.
- Why (b) is open: the Hebrew has no preposition before "the date of their entry into force" in (a)(1), whereas s.63(b) introduces the same kind of limb with the preposition "on" ("on the date of their entry into force", line 464 below); so "three months from" can govern both nouns.

```text
-- src:464 | {{ח:תת|(ב)}} תחילתו של {{ח:פנימי|פרק ו|פרק ו׳}} 18 חודשים מיום התחילה או במועד כניסתן לתוקף של תקנות לפי {{ח:פנימי|סעיף 46|סעיף 46}}, לפי המאוחר.
```

- The wiki's editorial note under (a)(1) (line 462) says, in my translation, "the commencement of the regulations under section 59 is on 16.7.2025"; it names the date of the regulations, not of the Law, so it settles neither reading.

```text
-- src:462 | {{ח:תתת}} {{ח:הערה|(תחילתן של התקנות לפי {{ח:פנימי|סעיף 59|סעיף 59}}, היא ביום 16.7.2025).}}
```

- Alternative (callable): `the readings of the dates with the three months counted from the later of the two days`.
- Discriminating case: the commencement day is 16.7.2025 under (a) and 16.10.2025 under (b); paragraph (2) is 16.1.2027 under (a) and 16.4.2027 under (b); the Second Schedule's three years are 16.7.2028 and 16.10.2028.
- Tests: "Fork F-C-3" (5 assertions, including work on a propane system on 16.7.2025 and 16.10.2025); red: the default does not give 16.10.2025.
- Open question for a domain expert: section 7, question 1.

### F-C-4: does the Law commence on the last day of the period, or the day after?

- Readings: (a) the Law commences on the last day of the period of months, the same-numbered day (IL s.10(b): the period "ends" on that day); (b) the Law commences on the day after the period ends.
- Taken: (a). IL s.10(b) says a period of months after an event ends on the day whose number is the event's, and "N months from" a day is the date that period reaches; the Interpretation NOTES (answer table) give the same date for "three years from 2025-07-16", namely 2028-07-16.
- The text of s.63 does not say whether the Law commences on the day the period ends or the next day; that is why (b) is callable.
- Support for (a), by analogy and in days, not months: regulation 5 of the Fees Regulations says its commencement is 7 days from its publication, and its note says published 9.7.2025 with commencement 16.7.2025, the last day of the 7 days (IL s.10(a)) and not the day after:

```text
regulations-fees.wiki:40 | {{ח:סעיף|5|תחילה}}
regulations-fees.wiki:41 | {{ח:ת}} תחילתן של תקנות אלה 7 ימים מיום פרסומן {{ח:הערה|(התקנות פורסמו ביום 9.7.2025, ותחילתן ביום 16.7.2025)}}.
```

- Alternative: `the readings of the dates with commencement on the day after a period ends` (the day after is computed by the module's `s 10(a) — the last day of a period of 1 days from`, not by adding to a date).
- Discriminating case: 16.1.2027 (a) against 17.1.2027 (b); with the regulations early, 14.4.2025 against 15.4.2025.
- Tests: "Fork F-C-4" (5 assertions); red: the default does not give 17.1.2027.

### F-C-5: is the commencement day bound for the whole day, or from 00.01?

- Readings: (a) at the level of a DAY, the Law has commenced on the whole of the commencement day; (b) by IL s.21, a statute binds from 00:01 on its commencement day, so the first minute of that day does not bind.
- Taken: (a), because the questions the other groups ask are about the day an act was done (a `DATE`).
- Alternative (callable): `s 63(a) and IL s.21 — under the readings, the Law binds work on the system at the moment`, which uses the module's `s 21 — the moment … is one at which a statute commencing on … binds`.
- Discriminating case: 00:00:30 on 16.7.2025 is not bound; 00:01:00 is; 23:59:59 on 15.7.2025 is not.
- Tests: "Fork F-C-5" (7 assertions); red: the default does not say the commencement day is not a commenced day.

### F-C-6a: a system with refrigerants of both kinds

- Text (lines 461 and 463; my translation): (1) a system that operates by means of a flammable refrigerant listed in the Fourth Schedule, provided its use was permitted by any law; (2) a system that operates by means of a refrigerant that is not as stated in paragraph (1).
- Both limbs' words are met by a system with a lawful listed refrigerant and another refrigerant; the text gives two dates and says nothing about how to combine them.
- Readings: (a) paragraph (1) governs if ANY refrigerant is as stated in it (the earlier date applies); (b) paragraph (1) governs only if EVERY refrigerant is as stated in it (the later date applies); (c) the text does not say, a named REFUSE.
- Taken: (a), on my reasoning and not the text's: each paragraph states the date from which the Law reaches work on systems of its description, and a later date given to another description does not take away the earlier one.
- Alternatives: `the readings of the regime with a mixed system governed by the later paragraph` and `the readings of the regime with a mixed system refused`, given to `s 63(a) — under the readings, the Law has commenced for work on the system`.
- Discriminating case: a system with lawful propane (290) and R134a (134a) on 16.7.2025: TRUE under (a), FALSE under (b), REFUSED under (c).
- Tests: "Fork F-C-6a" (11 assertions, including that a system whose refrigerants are all of one paragraph is unaffected); red: the default does not say FALSE.

### F-C-6b: a listed refrigerant whose use is not permitted by law

- Readings: (a) paragraph (1) requires lawful use, paragraph (2) is "not as stated in paragraph (1)", so such a refrigerant falls to (2) by the words; (b) the text does not say, a named REFUSE.
- Taken: (a), the complement reading, because (2) is defined as the residual of (1).
- Alternative: `the readings of the regime with a listed refrigerant of unlawful use refused`.
- Discriminating case: a system with unlawful propane on 16.7.2025: FALSE under (a), REFUSED under (b); on 16.1.2027 both TRUE.
- Tests: "Fork F-C-6b" (4 assertions) and the default cases in "63(a). Whether the Law has commenced for work on a system on a day"; red: the default does not say TRUE on 16.7.2025.
- The proviso is said of the refrigerant, so it is the field `use of the refrigerant is permitted by law` of the domain's `Refrigerant`; whether "permitted" is judged at the day of the work or at the commencement is not said (section 7, question 6).

### F-C-6c: a system with no refrigerant recorded

- The text classifies a system by its refrigerant and says nothing of a system with none recorded (the domain says an empty list means none is recorded; s.2 makes every cooling system operate by a refrigerant).
- Taken: a named REFUSE, only where the answer depends on the regime.
- Before the commencement day nothing has commenced and from the day paragraph (2) takes effect both regimes have, so the rules answer FALSE and TRUE there without classifying.
- Tests: "A system with no refrigerant recorded" (4 assertions).

### F-C-7 (trap T20): the provisions that are not about work on a system

- s.63(a) fixes a commencement only "for the performance of work on a system" and says nothing of the Registrar, the Council, inspection, applications, or the Minister's powers.
- The Interpretation NOTES (F26) found no default commencement day for a statute that fixes none; the encoding does not choose one.
- Taken: a named REFUSE, `the Law has commenced, for a provision that is not about work on a system, on the day`.
- The powers of ss.59 and 60 are not gated on any commencement (fork F-R-3).
- No alternative: the sources give none.
- Tests: "63(a). The provisions that are not about work on a system" (2 assertions).

### F-C-8 (trap T19): Chapter 6 and the regulations under section 46

- s.63(b): Chapter 6 commences 18 months from the commencement day, or on the entry into force of regulations under s.46, whichever is later; s.46(b) is a power ("may") to make them.
- Readings: (a) no section 46 regulation known means the later date is not known, so the answer that depends on it is a named REFUSE; (b) no regulation means "none in force", so Chapter 6 has not commenced.
- Taken: (a): the sources cannot show that no regulation exists after their own dates (the Law's wiki revision is 2025-07-10), so "not yet" would be a guess.
- Alternative (callable): `s 63(b) — reading no regulation under section 46 as none in force, Chapter 6 has commenced on the day`.
- Discriminating case: 16.1.2027 with no section 46 regulation known: REFUSED under (a), FALSE under (b).
- Before the first limb (before 16.1.2027) the answer is FALSE under both, whatever section 46 says; with a regulation known the readings agree.
- Tests: "63(b). Chapter 6" (13 assertions) and "Fork F-C-8" (5 assertions).
- The red file carries the reading that ignores the section 46 limb altogether: the default does not give 16.1.2027 when the regulations come on 1.3.2027.

### F-C-9: the vintage of the Fourth Schedule, and "was permitted"

- The Minister, after consulting the Minister of Environmental Protection, may amend the Fourth Schedule by order, so a system's regime can change between two dates; no order is in the sources.
- Taken: the Schedule as enacted is the only vintage modelled (the fleet lead's ruling 2).
- The power is encoded as a MAY rule with the consultation as a computable condition, and the content of an order is an input that no rule reads.
- A refrigerant's lawful use is one field, not a function of the day; a refrigerant whose use became lawful after the commencement day, or ceased to be, is not modelled (section 7, question 6).

### F-C-10: where the date 16.7.2025 comes from

- The date the section 59 regulations entered into force is an input (IP13), decided by G8: regulation 5 of the Fees Regulations gives 7 days from the publication of 9.7.2025 (IL s.10(a)), which is 16.7.2025.
- The wiki's note under s.63(a)(1) also says 16.7.2025; it is an editorial note and not the Law's text, and the encoding does not read it.
- The tests use 16.7.2025 as the sources' own value and other dates as hypothetical values that put a date on each side of an edge.

### F-S4-1: the Fourth Schedule: item (66), direction marks, and how a designation is matched

- Item (66): the wiki reads `170E`, the gazette (printed page 207, page image viewed; line 1222 of its text layer) reads `E170`.
- Taken: the gazette governs (the brief): `E170`.
- Items (69) and (71): the wiki and the gazette text layer carry an invisible left-to-right mark (U+200E) inside `1130(E)` and `1132(E)`; the data does not carry the marks.
- Matching.
  Readings: (a) exact: a designation is listed when it equals one of the 95 as plain text, same letters, same case, no leading R; (b) tolerant: ignoring case, a leading R or R-, and direction marks.
  Taken: (a): the Schedule prints bare designations, the domain says to compare the designation as plain text, and the case the gazette prints is part of what it prints (`1132a`, `600a` against `440A`).
  Alternative: `a refrigerant, read tolerantly, is a listed flammable refrigerant`, `the designation, read tolerantly, is printed in the Fourth Schedule`.
- Twelve designations are purely numeric (32, 50, 170, 290, 600, 601, 702, 1150, 1270, 40, 611, 717); a designation is a STRING, never a NUMBER, so `290` is listed and `29` and `2900` are not.
- Tests: `g7-tests-fourth-schedule.l4`: an independent transcription of all 95 from the three page images, compared with the generated data; the count; the items the brief names (66), (69), (71), (92) to (95); near misses; the tolerant reading on its own terms (37 assertions, 26 of them about direction marks: see section 11); red: the wiki's `170E`, `600A`, `R290`, `1234YF` against the exact reading.

### F-E-1 (trap T32): s.58 against s.61

- s.58: a licensee is treated as a service electrician for cooling systems, under s.6 of the Electricity Law, with no limit drawn from the First Schedule.
- s.61: adds subsection (e) to s.6 of the Electricity Law: a person may engage in electrical work "in accordance with the First Schedule", within work on a cooling system, if he holds a licence under this Law; the First Schedule's limits (items A12 and B14: the integral electrical system only) bite only through s.61.
- Readings: (a) s.58 is a wide gateway: the licensee may do the electrical work a service electrician may on a cooling system; (b) s.61 is the only gateway: only Schedule electrical work.
- The Law does not say which governs electrical work on a cooling system that the First Schedule does not list.
- Both rules are encoded, neither is the Law's answer: `the licensee is treated as a service electrician under section 58` and `s 61 — the licensee may do electrical work under subsection (e) added to section 6 of the Electricity Law`, and the two readings `electrical work is open to the licensee, reading section 58 as a wide gateway` and `…, reading section 61 as the only gateway`.
- Discriminating case: a licensee doing electrical work on a cooling system that the First Schedule does not list: TRUE under (a), FALSE under (b).
- Tests: `g7-tests-electrical.l4`, "58 against 61" (6 assertions); red: the two readings are not equal.

### F-E-2: s.58 and s.61 are not gated on commencement

- A licence cannot be in force before the licensing provisions operate, so the licence list (IP1) already carries the commencement; s.63(a) gives no commencement to these provisions (trap T20).
- Taken: no gate.

### F-E-3: s.58's status is for an act, not for the person

- The deeming holds "for cooling systems", so the rule takes the input `the act is work on a cooling system` (IP4) as well as the licence list; with a licence and an act that is not work on a cooling system the answer is FALSE.
- No alternative: the words say "for cooling systems".

### F-A-1 (trap T39): s.62 against s.56

- s.56(a): a final decision of the Commissioner under Chapter 6 can be appealed to the Magistrates' Court (the one where the President of the Magistrates' Court sits) within 45 days of notice.
- s.62 adds this Law to item 21 of the First Schedule to the Administrative Courts Law; on its face every decision under the Law is then listed, including the Commissioner's.
- The Law does not say which court governs the Commissioner's final decision, or whether both are open.
- Readings: (a) s.62 is additional to s.56 (both fora are open for the Commissioner's final decision, if the Administrative Courts Law gives jurisdiction); (b) s.56 is the only route for the Commissioner's final decision.
- Taken: (a) is the function `the fora for review of a decision, reading section 62 as additional to section 56`; (b) is `the fora for review of a decision, reading section 56 as the only route for a final decision of the Commissioner`; both are callable and neither is the Law's answer (no default is exported).
- Whether the Administrative Courts Law gives an Administrative Court jurisdiction over a decision of a kind its schedule lists is out of scope: it is the input `the Administrative Courts Law gives an Administrative Court jurisdiction over the decision`.
- Tests: `g7-tests-administrative-courts.l4` (13 assertions); red: the two are not equal.

### F-R-1: how many heads of fee

- s.59 has four "for" phrases in its first sentence (application; grant or renewal; examinations including objections; the s.17 training) and two in its second (a different rate for a foreign expert's temporary licence: application or renewal; and grant).
- Readings: (a) six heads, one per phrase; (b) five, the survey's count, with the temporary licence as one head.
- Taken: (a). Alternative: none callable beyond the count; the red file asserts the count of five against the six.
- G8 consults the list for silence (T38): a version of the Fees Regulations that sets no fee for a head is silent on it.

### F-R-2: s.60(1)'s general power against s.60(2)

- s.60(1) lets the Minister, with the committee's approval, make regulations on "any matter connected with implementation", including (a) to (c); s.60(2) lets him make regulations on two matters, how to apply for a licence or renewal and how a foreign expert applies for a temporary licence, with no approval.
- Those two matters are also matters connected with implementation, so the general power seems to reach them with approval required.
- Readings: (a) the specific paragraph governs: no approval for the (2) matters; (b) the general power covers every matter, so approval is required for all.
- Taken: (a). Alternative (callable): `s 60 — reading paragraph (1) as covering the matters of paragraph (2), the procedure required for regulations on … has been followed, given the procedure …`.
- Discriminating case: regulations on the manner of applying for a licence made without the committee's approval: valid under (a), not under (b).
- Tests: `g7-tests-regulations.l4`, "Fork F-R-2" (8 assertions); red: the default does not say the procedure is unfollowed.

### F-R-3: the powers are not gated on commencement

- s.63(a)(1) makes the commencement day depend on the entry into force of the regulations under s.59; so the s.59 power has to be usable before the commencement day, or the definition is circular.
- The Interpretation Ordinance s.19 (the Interpretation NOTES, fork F16) lets a power be used before commencement to the extent needed to operate the enactment.
- Taken: ss.59 and 60 carry no commencement gate and no `WITHIN`.

### F-R-4: what a MAY rule says when its condition fails

- A power with an unmet precondition (the committee's approval, the consultation) is encoded `IF conditions THEN PARTY the Minister MAY act ELSE FULFILLED`: with the conditions met the permission stands, and is fulfilled when the Minister acts or does not (a MAY is not breached by non-use); without them there is no permission, which a deontic can only show as FULFILLED.
- A DEONTIC cannot be asserted, so the assertable answer is the BOOLEAN gate (`s 59 — the approval the Minister needs to set fees has been given`, `s 60 — the procedure required for regulations on … has been followed …`, `s 63(a)(1) — the consultation needed for an order amending the Fourth Schedule has taken place`), and the deontic rules are exercised with `#TRACE` (printed, not counted).

### F-R-5: the second sentence of s.59 and the approval

- "In regulations as aforesaid" the Minister may set different rates for the temporary licence, so the approval of the committee governs those rates too.
- Taken: one approval gate for all six heads.

### F-R-6 (kind X): the time for an application to renew (s.60(2)(a))

- The text (line 450, quoted below; my translation of its end: "and, for an application to renew a licence, also the time for submitting it"):

```text
-- src:450 | {{ח:תתת|(א)}} אופן הגשת בקשה לרישיון או חידושו, הפרטים שתכלול והמסמכים שיש לצרף אליה, ולעניין בקשה לחידוש רישיון – גם המועד להגשתה;
```

- No such regulation is in the sources, so the time is not known; it is a length fixed by an official (kind X), an input and never a default.
- Taken: `s 60(2)(a) — the last day for an application to renew a licence` takes the NOMINAL last day the regulation gives, as a MAYBE DATE, and a calendar; NOTHING is the named REFUSE `s 60(2)(a) fixes the time for an application to renew by regulations, and no regulation under section 60(2)(a) is in the sources`; IL s.10(c) is applied to the nominal day as for a deadline or a window (ruling 4).
- Alternative (callable): `s 60(2)(a) — the last day for an application to renew a licence, IL s.10(c) not applied`.
- Discriminating case: a nominal last day on a day of rest (Saturday 21.3.2026 with that day in the calendar): moved to Sunday 22.3.2026 under the default, kept under the alternative.
- Whether a deadline fixed by a regulation in so many days "before" the end of validity would be counted backwards (kind B, outside IL s.10) is not decidable until the regulation exists.
- Tests: `g7-tests-regulations.l4`, "Section 60(2)(a)" (6 assertions); red: the default does not give the nominal day when it falls on a day of rest.

## 3. Answer table: the headline scenarios

Dates are `d.m.yyyy`.
"Facts as the sources give them": published 14.1.2025; regulations under s.59 in force 16.7.2025; no regulation under s.46 known.

| scenario | answer | section | test |
| --- | --- | --- | --- |
| the commencement day | 16.7.2025 | s.63(a)(1) | tests-commencement |
| three months after publication (the first limb alone) | 14.4.2025 (Monday) | s.63(a)(1) with IL s.10(b) | tests-commencement |
| the day paragraph (2) takes effect: 18 months from the commencement day | 16.1.2027 (Saturday) | s.63(a)(2) | tests-commencement |
| the three years of the Second Schedule's notes, from the commencement day | 16.7.2028 (Sunday); not 16.1.2030 (T7) | s.63(a)(1), Second Schedule notes | tests-commencement |
| the day Chapter 6 commences, no s.46 regulation known | REFUSED | s.63(b), s.46(b) | tests-commencement |
| the same, s.46 regulations in force 1.6.2026 | 16.1.2027 | s.63(b) | tests-commencement |
| the same, s.46 regulations in force 1.3.2027 | 1.3.2027 | s.63(b) | tests-commencement |
| work on a system with lawful propane (290), 15.7.2025 | FALSE | s.63(a)(1) | tests-commencement |
| the same, 16.7.2025 | TRUE | s.63(a)(1) | tests-commencement |
| work on a system with R134a (134a) only, 15.1.2027 / 16.1.2027 | FALSE / TRUE | s.63(a)(2) | tests-commencement |
| a system with unlawful propane, 16.7.2025 / 16.1.2027 | FALSE / TRUE (REFUSED / TRUE on reading b of F-C-6b) | s.63(a)(1), (2) | tests-commencement |
| a system with lawful propane and R134a, 16.7.2025 | TRUE (FALSE on F-C-6a(b), REFUSED on (c)) | s.63(a)(1), (2) | tests-commencement |
| a system with no refrigerant recorded: 15.7.2025 / 16.7.2025 / 16.1.2027 | FALSE / REFUSED / TRUE | s.63(a) | tests-commencement |
| a provision that is not about work on a system, any day | REFUSED | s.63(a) | tests-commencement |
| Chapter 6 in force on 15.1.2027 / 16.1.2027 / 1.1.2030, no s.46 regulation | FALSE / REFUSED / REFUSED | s.63(b) | tests-commencement |
| the Law binds a propane system at 00:00:30 / 00:01:00 on 16.7.2025 | no / yes | s.63(a)(1), IL s.21 | tests-commencement |
| the Fourth Schedule has | 95 items; item (66) is E170 | Fourth Schedule | tests-fourth-schedule |
| is 170E listed? is E170? | no / yes | Fourth Schedule item (66) | tests-fourth-schedule |
| are 488A, 489A, 490A, 491A listed? | yes (items (92) to (95)) | Fourth Schedule | tests-fourth-schedule |
| are 290 and 600a listed? 29, 600A, R290? | yes and no (exact reading); R290 and 600A listed on the tolerant reading | Fourth Schedule | tests-fourth-schedule |
| a licensee doing work on a cooling system is treated as a service electrician | TRUE with a licence in force, FALSE with none | s.58 | tests-electrical |
| electrical work outside the First Schedule on a cooling system | open on the wide reading of s.58; not open on the narrow reading of s.61 | ss.58, 61 | tests-electrical |
| heads of fee the Minister may set | 6, two of them at a different rate for a foreign expert's temporary licence | s.59 | tests-regulations |
| regulations on testers and experts need | approval and consultation | s.60(1)(c) | tests-regulations |
| regulations on the manner of applying for a licence need | no approval (reading taken) | s.60(2)(a) | tests-regulations |
| the last day to apply to renew, no regulation | REFUSED | s.60(2)(a) | tests-regulations |
| a final decision of the Commissioner that an Administrative Court could also hear | both courts (s.62 additional) or the Magistrates' Court only (s.56 exclusive) | ss.56, 62 | tests-administrative-courts |

## 4. Nouns requests for the INTEGRATOR

All my types are declared locally with names that carry the section number; none edits `domain.l4`.
Requests:

1. `Head of fee under section 59` (six constructors, `g7-regulations.l4`) should move to `domain.l4` if G8 is to key its services to the heads without a cross-group import: G8 consults `s 59 — the heads of fee for which the Minister may set a fee` for "a vintage silent on a head answers silence" (T38).
2. `Matter of regulations under section 60` and `Procedure of the Minister's regulations` should move to `domain.l4` if G5 (s.36(a), under head (c)) wants to say whether regulations on the conditions for testers and experts exist; at present G5 can hold that as its own input and nothing here depends on it.
3. `Forum for review of a decision under the Law` (two constructors, `g7-administrative-courts.l4`) should move to `domain.l4` if G6 wants the route of an appeal under s.56 in the same type as the Administrative Court route of s.62.
4. The record `Facts that fix the commencement of the Law under section 63` could move to `domain.l4`; no other group needs it, because the groups consume the two booleans below.
5. No new constructor of `Party` is needed: the Minister of Environmental Protection and the Knesset Labour and Welfare Committee enter as BOOLEAN inputs (a consultation took place, an approval was given), not as parties.
6. The domain's description of `Refrigerant`.`designation` should say what the Fourth Schedule fixes: bare, no direction mark, letters in the case the gazette prints, compared as exact text (the tolerant function exists for callers that cannot promise this).
7. Wiring: the booleans PLAN names are `the Law has commenced for the work on the system` (IP2) and `Chapter 6 was in force on the day of the act` (IP16); G7's functions that compute them are in section 5.

## 5. Standard inputs consumed, and functions exported

### 5.1 Inputs, by exact `GIVEN` or field name

| input | type | PLAN id | where used |
| --- | --- | --- | --- |
| `licence kinds in force on the day` | LIST OF `Licence kind` | IP1 | `g7-electrical`: ss.58, 61 |
| `the act is work on a cooling system` | BOOLEAN | IP4 | `g7-electrical`: ss.58, 61 |
| `the electrical work is in accordance with the First Schedule` | BOOLEAN | new: G1's items A12 and B14 | `g7-electrical`: s.61 |
| `the day the Law was published in Reshumot` (field of `Facts that fix the commencement of the Law under section 63`) | DATE | (new) 14.1.2025 by the gazette | `g7-commencement` |
| `the s.59 regulations came into force on` (field of the same record) | DATE | IP13, decided by G8: 16.7.2025 | `g7-commencement` |
| `the day regulations under section 46 came into force, if any` (field of the same record) | MAYBE DATE | (new) none in the sources | `g7-commencement`: s.63(b) |
| the calendar `Calendar of rest days` (field `the calendar of rest days` of `Readings of the dates of section 63`) | domain record | IP15 | alternatives of s.63 only |
| `Cooling system`, `Refrigerant`, `Work item` | domain records | IP2, domain | `g7-commencement` |
| `the Knesset Labour and Welfare Committee approved the regulations`, `the Minister consulted the Minister concerned with the fields of the testers or experts` (fields of `Procedure of the Minister's regulations`) | BOOLEAN | input approvals | `g7-regulations` |
| `the Minister consulted the Minister of Environmental Protection` | BOOLEAN | input consultation | `g7-commencement` |
| `the nominal last day for an application to renew fixed by regulations under section 60(2)(a), if any` | MAYBE DATE | (new) none in the sources | `g7-regulations` |
| `the decision was made under the Law`, `the Administrative Courts Law gives an Administrative Court jurisdiction over the decision`, `the decision is a final decision of the Commissioner under Chapter 6` | BOOLEAN | (new) | `g7-administrative-courts` |

### 5.2 Functions exported (exact names; `@export` where the language allows)

| function | module | answers |
| --- | --- | --- |
| `the commencement day under section 63(a)(1)` | `g7-commencement` | DATE: the commencement day (facts) |
| `the day the Law commences for a system with any other refrigerant under section 63(a)(2)` | `g7-commencement` | DATE: 18 months from the commencement day |
| `the Law has commenced for work on the system … on the day … given the facts …` | `g7-commencement` | BOOLEAN, PLAN IP2 (system, day, facts) |
| `the Law has commenced for the work item … given the facts …` | `g7-commencement` | BOOLEAN, IP2 for a `Work item` |
| `the day Chapter 6 commences under section 63(b)` | `g7-commencement` | DATE; REFUSED without a section 46 date |
| `Chapter 6 was in force on the day of the act … given the facts …` | `g7-commencement` | BOOLEAN, PLAN IP16 |
| `the regime of a system under section 63(a)` | `g7-commencement` | `Commencement regime of section 63(a)`; REFUSED for a system with no refrigerant |
| `a refrigerant is a listed flammable refrigerant` | `g7-fourth-schedule` | BOOLEAN (the slice's name) |
| `the licensee is treated as a service electrician under section 58` | `g7-electrical` | BOOLEAN, PLAN IP21 (the slice's name was `the licensee is treated as a service electrician`; renamed to carry the section) |
| `s 61 — the licensee may do electrical work under subsection (e) added to section 6 of the Electricity Law` | `g7-electrical` | BOOLEAN, IP21 and IP4 |
| `s 59 — the heads of fee for which the Minister may set a fee`, `… a different rate may be set for a foreign expert's temporary licence` | `g7-regulations` | LIST OF `Head of fee under section 59`, for G8 |
| `s 59 — …`, `s 60 — …` powers | `g7-regulations` | gates (BOOLEAN) and `DEONTIC Party` rules, ruling 2 |
| `s 60(2)(a) — the last day for an application to renew a licence` | `g7-regulations` | DATE; REFUSED without a regulation |

### 5.3 Call shapes

The names are mixfix; the arguments go where the backticks leave a gap, in this order:

```text
`the commencement day under section 63(a)(1)` facts
`the day the Law commences for a system with any other refrigerant under section 63(a)(2)` facts
`the Law has commenced for work on the system` system `on the day` day `given the facts` facts
`the Law has commenced for the work item` item `given the facts` facts
`the day Chapter 6 commences under section 63(b)` facts
`Chapter 6 was in force on the day of the act` day `given the facts` facts
`the regime of a system under section 63(a)` system
`a refrigerant is a listed flammable refrigerant` refrigerant
`the licensee is treated as a service electrician under section 58` `licence kinds in force on the day` `the act is work on a cooling system`
```

where `facts` is a `Facts that fix the commencement of the Law under section 63`, `system` a domain `Cooling system`, `item` a domain `Work item`, `day` a `DATE`.
The wiring the INTEGRATOR needs: G8's date of the section 59 regulations goes into `the s.59 regulations came into force on`; the publication day (14.1.2025) is a constant of the Law; the section 46 field is `NOTHING` until a regulation is known.

The `@export` marks are on: the commencement day, the paragraph (2) day, the work boolean, the Chapter 6 day and boolean, the listed-refrigerant test, and the s.58 test.
Not exported: the rules that take a `Readings of …` record (a record of readings is an input a caller can build, but the default wrappers fix it) and the DEONTIC rules.

## 6. Contradictions in the source (a separate pass, after encoding)

I re-read every provision of my scope against the others, and the Fourth Schedule against the gazette, looking for two provisions that give different answers to the same facts.
Each entry: provisions, the case that discriminates, and the callable readings.

1. s.63(a)(1) against s.63(a)(2) for a system with two kinds of refrigerant.
   Both limbs' words are met; the dates differ by 18 months.
   Case: lawful propane and R134a on 16.7.2025.
   Readings: F-C-6a, `the readings of the regime with a mixed system governed by the later paragraph` and `… refused`.
2. s.58 against s.61: electrical work on a cooling system outside the First Schedule (F-E-1, T32).
3. s.56 against s.62: the Commissioner's final decision (F-A-1, T39).
4. s.60(1) against s.60(2): the manner of applying for a licence, a matter of implementation under (1) and a matter without approval under (2) (F-R-2).
5. s.63(a)(1): two grammatical readings of "three months from its publication or the entry into force of the regulations": 16.7.2025 against 16.10.2025 (F-C-3).
6. s.63(b) against s.46(b): Chapter 6 commences at the later of 18 months and the entry into force of regulations that the Law only permits ("may"); with no regulation the later date does not exist and Chapter 6 may never commence on this text (F-C-8, T19).
7. s.63(a) against the rest of the Law: a commencement is fixed only "for the performance of work", so the provisions that would have to operate before any licence can be required (applications, the Registrar, the Council, the s.59 regulations that define the commencement day) have none (F-C-7, T20).
8. s.63(a)(1) against s.59: the commencement day is defined by the entry into force of regulations under s.59, which s.59 lets the Minister make; the power must be usable before the commencement day (F-R-3); this is circular only if the power is gated on commencement, which this encoding does not do.
9. The Fourth Schedule: the wiki and the gazette differ at item (66) (`170E` against `E170`); the gazette governs (F-S4-1).
10. The Second Schedule's three years "from the commencement as stated in s.63(a)(1)" (G2, T7) reach a system of paragraph (2) only for about eighteen months after its duty begins: the case is an application for work on an ordinary-refrigerant system made between 17.7.2028 and 16.1.2030.
    G7 contributes the anchor: the three years run from `the commencement day under section 63(a)(1)` (16.7.2028), and the test shows 16.1.2030 if they ran from paragraph (2)'s date.

Looked at and found consistent: the six heads of s.59 against the Fees Regulations (T38: a power not exercised is silence, not conflict); the Fourth Schedule's 95 items against each other (no duplicates, ignoring case: an independent transcription and the survey's script agree); s.60(1)(c)'s consultation against s.36(a)'s reference to it (G5's).

## 7. Open questions for a domain expert

1. s.63(a)(1): is "three months from [its publication or the entry into force of the regulations], whichever is later" counted from the later of the two days (16.10.2025) or is it the later of two dates (16.7.2025)? (F-C-3.)
2. Does the Law commence on the last day of a period of months or on the day after? Does IL s.10(c) move a commencement that falls on a Saturday? (F-C-4, F-C-1.)
3. Which paragraph of s.63(a) governs a system with refrigerants of both kinds, and which a listed refrigerant whose use is not permitted? (F-C-6a, F-C-6b.)
4. What commences the provisions of the Law that are not about work on a system, for example the Registrar's powers and the s.59 power itself? (F-C-7.)
5. If no regulation under s.46 is made, does Chapter 6 never commence, or is s.46(b)'s "may" read as "shall"? (F-C-8.)
6. "Provided its use was permitted by any law": at what day is lawfulness judged, the day of the work or the commencement, and who certifies it? Has the Minister made any order amending the Fourth Schedule since January 2025?
7. Is item (66) `E170`, as the gazette prints it? Is a designation matched by its printed letters and case, or ignoring case and a leading R? (F-S4-1.)
8. s.58 and s.61: does s.58's status let a licensee do electrical work on a cooling system beyond the First Schedule? (F-E-1.)
9. s.56 and s.62: which court hears the Commissioner's final decision, and which court hears a decision of the Registrar or the Minister? (F-A-1.)
10. s.60(2): do the matters of paragraph (2) need the committee's approval because they are also matters of paragraph (1)? (F-R-2.)
11. How many heads of fee does s.59 give, and does it give a fee for the grant of a temporary licence at a different rate? (F-R-1.)

## 8. What the sources do not answer

Each item is an input or a named REFUSE in the encoding; none gets a default.

- Any order amending the Fourth Schedule under s.63(a)(1); any regulation under s.46, s.60(1) or s.60(2) other than the Fees Regulations.
- The day regulations under s.46 came into force (if they exist).
- The calendar of days of rest, recess and holiday for any year (IL s.10(c)).
- The text of the Electricity Law's s.6(a) and of the service-electrician licence's scope (what it lets the holder do): outside the sources; s.58 and s.61 only deem and add.
- The Administrative Courts Law's own sections and item 21 of its First Schedule, so which decisions an Administrative Court hears.
- The time for submitting an application to renew a licence (s.60(2)(a)).
- Which refrigerants are lawful under other enactments, and from when; whether a designation on a unit written as R600A is the Schedule's `600a`.
- The commencement of any provision of the Law other than as regards work on a system.
- The text of ss.61 and 62 beyond the gazette's page images: the wiki says only that the amendments were incorporated, and the gazette's text layer is scrambled, so their content is my translation of the page images and is not quoted.
- The Law as amended after the Wikisource revision of 2025-07-10.

## 9. peeked

Nothing.
I read only what the assignment and the brief allow: `inputs/`, `phase1/`, the two skills and their references, one page of the `doc/` tree (`doc/reference/builtins/README.md`, for the string built-ins), and from the deposit only `domain.l4` and `il-interpretation-time.l4`.
I did not open another encoder's files, any other encoding of this subject, or anything outside the fleet directory and the skills.

## 10. Incident

At about 21:50 I ran a `pkill -f` pattern that matched the shared `l4` binary's path, to stop two stray mutation-test runs of my own, and it will also have sent SIGTERM to any `l4 run` another agent had in flight.
I told the fleet lead and enc-g1 and enc-g4 at once.
No file was touched; a killed run only needs rerunning.

## 11. Defect found after the first deposit, and repaired

What it was.
In `g7-fourth-schedule.l4` the tolerant normaliser `the designation with direction marks and a leading R removed, in upper case` removes direction marks with two REPLACEs, one for U+200E and one for U+200F.
The second REPLACE carried the literal text `{{MARK2}}` (the build's placeholder) where the right-to-left mark U+200F belonged, so a designation with U+200F in it was not recognised by the tolerant reading, and the literal text `{{MARK2}}` would have been removed instead.
Found by the independent test author and verified by the fleet lead.

How it hid.
`build.py` expanded `{{MARK}}` but its patch to expand `{{MARK2}}` silently did not apply (a string replacement on text that was not found raises nothing), and I did not read the generated file for it.
My own test `"{{MARK2}}E170"` in `g7-tests-fourth-schedule.l4` carried the same literal, so the function removed it and the assertion passed: a test and a module agreeing on the same mistake.
No test measured the length of a marked string, and none of my 28 mutations touched mark stripping.

Repair.
- `build.py` now writes the marks with `chr(0x200E)` and `chr(0x200F)` (no mark and no placeholder in its source), and after expanding a template it scans the output for any unsubstituted placeholder token (`{{MARK`, `{{Q `, `{{DATA4}}`, `{{H `, `{{HF `, `{{COVERAGE}}`, `{{CHECK}}`, `{{MUTATIONS}}`) and aborts if it finds one.
- Both files were regenerated; line 372 of `g7-fourth-schedule.l4` now holds a real U+200E and a real U+200F (checked by code point).
- Scan of every generated `g7-*.l4` for `{{` in a non-comment line: none (the quote lines of the wiki carry the wiki's own double-brace templates, inside `--` comments, by design).
- No exported name or signature changed: the module template is untouched, so only the string on that one line differs; the test file gained assertions.

Tests added (all in `g7-tests-fourth-schedule.l4`, section "The tolerant reading"; the one wrong assertion was replaced by 26 lines; the section went from 12 to 37 assertions, the module from 60 to 85, all g7 tests from 254 to 279):
- `STRINGLENGTH` of `290` (3), U+200E then `290` (4), U+200F then `290` (4), U+200F then `E170` (5), both marks then `290` (5) and `29`, U+200F, `0` (4): each mark is one character, so a placeholder cannot pass again.
- Tolerant reading, listed: `290` with neither mark; U+200F then `E170`; U+200F then `290`; U+200E then `290`; U+200E then `E170`; both marks together in either order then `290`; a mark inside `29`+`0`; both marks then `R-1234ze(E)`.
- Tolerant reading, not listed: U+200F then the wiki's `170E`; both marks then `29`.
- The normaliser's output: U+200F `E170` gives `E170`; U+200E `290` gives `290`; both marks `290` gives `290`; both marks `R-600a` gives `600A`; `290` gives `290`.
- Exact reading, not listed (it does not strip): U+200F then `E170`; U+200E then `290`; both marks then `290`; and `290` itself exact-listed.
- Mutations added: the tolerant reading strips only U+200E; only U+200F; carries the unsubstituted placeholder: all three are caught (9 failed assertions each).
