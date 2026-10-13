# FRAGMENT-G6: financial sanctions (Chapter 6, ss.41-57) and the Third Schedule

Status: written by ENCODER G6 on 2026-10-13.
No domain expert has read this against the Law.
The values in sections 2 and 3 are values asserted in the test modules, which pass; the run is in section 0, and the Hebrew quoted below was cut from `inputs/law.wiki` by a script (`work/g6/mkfragment.py`), not typed.
The gazette (Sefer HaChukim 3349, pp. 193-197 and p. 205) was read as page images for every number in ss.41-57 and for the Third Schedule table; it agrees with the Wikisource text in every number of this scope.

## 0. Files, assumptions, and what the check printed

Files written (all in `deposit/`, all with the prefix `g6-`, plus this file):
`g6-nouns.l4`, `g6-schedule-three.l4`, `g6-notice-and-hearing.l4`, `g6-amount.l4`, `g6-payment.l4`, `g6-warning.l4`, `g6-appeal-and-publication.l4`,
and the test modules `g6-tests-schedule-three.l4`, `g6-tests-notice-and-hearing.l4`, `g6-tests-amount.l4`, `g6-tests-payment.l4`, `g6-tests-warning.l4`, `g6-tests-appeal-and-publication.l4`, `g6-tests-scenarios.l4` (three whole proceedings run through the modules) and `g6-tests-red.l4`.

One module is added to the survey's list: `g6-nouns.l4`, the nouns of Chapter 6 that no other group needs (the notice, the demand, the warning, the extension, the previous violation, the Third Schedule row).
It holds `DECLARE` and nothing else.

Imports: brief ruling 1 forbids imports across groups only, as the lead confirmed after I finished.
My own modules import each other (the graph is acyclic) and my tests import my modules; no G6 module imports another group's module.
Every `g6-` module imports `prelude`, `daydate` and `domain`; `il-interpretation-time` is imported by `g6-notice-and-hearing`, `g6-amount`, `g6-payment`, `g6-warning`, `g6-appeal-and-publication` and the test modules that use dates (not by `g6-nouns` or `g6-schedule-three`).
The graph among the `g6-` modules, each line "module imports ...":

- `g6-nouns`: nothing from G6.
- `g6-schedule-three`: `g6-nouns`.
- `g6-notice-and-hearing`: `g6-nouns`.
- `g6-amount`: `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`.
- `g6-payment`: `g6-nouns`, `g6-notice-and-hearing`.
- `g6-warning`: `g6-nouns`, `g6-schedule-three`, `g6-notice-and-hearing`, `g6-amount`.
- `g6-appeal-and-publication`: `g6-nouns`, `g6-notice-and-hearing`.
- each `g6-tests-*` module: `g6-nouns` and the modules it tests, directly (`-scenarios` and `-red` import all seven rule modules).

What `work/g6/check-g6.sh` printed (the skill's `check.sh`, run over `deposit/g6-*.l4` only, with a column for warnings, the srcrefs gate over `inputs/law.wiki`, and the hash of the vendored time module); exit status 0:

```text
module                                    errors satisfied  failed  refused  expected warnings
g6-amount.l4                                   0         0       0        0         0        0
g6-appeal-and-publication.l4                   0         0       0        0         0        0
g6-notice-and-hearing.l4                       0         0       0        0         0        0
g6-nouns.l4                                    0         0       0        0         0        0
g6-payment.l4                                  0         0       0        0         0        0
g6-schedule-three.l4                           0         0       0        0         0        0
g6-tests-amount.l4                             0       137       0        0         0        0
g6-tests-appeal-and-publication.l4             0        80       0        0         0        0
g6-tests-notice-and-hearing.l4                 0        99       0        0         0        0
g6-tests-payment.l4                            0        53       0        0         0        0
g6-tests-red.l4                               40         0      40        0        40        0
g6-tests-scenarios.l4                          0        28       0        0         0        0
g6-tests-schedule-three.l4                     0        80       0        0         0        0
g6-tests-warning.l4                            0        72       0        0         0        0
g6-warning.l4                                  0         0       0        0         0        0
TOTAL (15 modules)                            40       549      40        0                  0
(a failed assertion is also an error; any other error, any refused assertion, any warning makes the run red)

extra checks
  all g6 modules start with '@lang en' and have ASCII filenames
  l4 check: no stray @ref or @nlg warnings
  srcrefs: srcrefs check: 95 src: lines, 42 runs, 173 locators, 0 problems
  il-interpretation-time.l4 sha256 matches
```

The 40 failing assertions in `g6-tests-red.l4` are expected and are all the failures there are (section 2 says which fork each belongs to).
Read the diagnostics, not the exit code: the script counts the line after every `Message:`.
No module emits a warning, and no assertion refuses.

The srcrefs gate was run at `--refs` over every `g6-*.l4`, and it reports no problem (the line is in the output above).
At `--strict` it reports problems of two kinds only (a first `@ref` whose locators do not reach exactly the lines of the run it follows, and a later rule that cites lines quoted in an earlier block); the skill says to use `--refs` for a row that cites broadly, and G6's rules do.

Numbers: every number of ss.41-57 and of the Third Schedule table was checked in two ways.
The page images (pp. 193-197 and 205) were read for each amount, period and count.
And a script compared the digits of the Wikisource lines with the gazette's text layer: every literal figure of ss.41-57 (30 three times, 45, 12, 10, 1, 40,000, 80,000) and every money figure of the Third Schedule (20,000 four times, 10,000 three times, 5,000, 40,000, 3,000, 6,000) occurs in the gazette; the only Wikisource digits the gazette lacks are HTML table attributes.

One slip, disclosed: in `g6-tests-amount.l4` the assertion for "the reading taken for the same facts (item (5), individual, repeat, one month)" was first typed with the expected value 40,800 while the comment above it, written first, derives 20,000 + 400 + 20,000 = 40,400.
The module computed 40,400 and the assertion failed; the expected value was corrected to the derivation in its own comment (a transcription slip, not a finding about the Law).
No other expected value was changed after a run.

Repairs after the independent review.
An independent test author (ind-c) decided its expected values from the source before opening these modules and found three defects, which are repaired; no exported name or signature changed, and each old reading is kept as a callable alternative (section 2 has the forks):
(1) F-ACTDAY: an act on the day of delivery was counted late at s.43, s.53(a) and s.56(a), so representations made the day the notice arrived led s.44(d) to deem the notice a payment demand; the same defect was in s.48 (a payment on the day the demand arrives), which the review did not list and which is repaired with the rest.
(2) F-SHORTEN: an "extension" that ended before the 30 days were out shortened them; the end is now the later of the Commissioner's day and the standard end, at s.43 and s.53(b).
(3) F-NOTICE: a notice that omits what s.42(b) requires gave the violator no s.43 right, yet s.44 deemed it a payment demand; the day the demand is treated as delivered is now NOTHING for such a notice.
The assertions that encoded the old readings (an act on the day of delivery is not within the period, in four test modules) were moved to `g6-tests-red.l4` as 32 to 36; four more were added there (37 to 40), so the red count is 40 (it was 31) and the satisfied assertions are 549 (they were 485).
The review's eight assertions for these three groups (its DIS-2, DIS-3 and DIS-5, copied without edit into a scratch module that imports only G6 modules) fail against the modules as they were before the repair (8 of 8) and pass against these (8 of 8).
A date that is the day of delivery or later is timely; a day before delivery is not.
The date predicates `s 43 — the day ... is within ...`, `s 53(a) — the day ...`, `s 56(a) — the day ...` and `s 48 — the day ...` changed meaning; the deontic rules did not need to, since their WITHIN already counted from the day of delivery (AT 0).
Consequence for the wiring: `s 56(a) — the day notice of the decision counts as delivered to a violator who made no representations` still returns a date for any notice (its signature returns a DATE); ask `s 44 — the day the payment demand is delivered or treated as delivered` first, which is NOTHING for a notice the Law does not treat as a demand.

Deliberate mutations, to show that the tests can fail (`work/g6/mutate.py`, run on a scratch copy; `deposit/` was not touched): 38 of 38 mutations were caught, each by at least one failing or refusing assertion (the count is the assertions that failed or refused in the test modules, the red file excluded).

```text
[0] s.45(a) one fiftieth -> one fortieth: CAUGHT (16 failing)
[1] s.45(b) repeat window: last day inside -> outside: CAUGHT (3 failing)
[2] s.45(b) repeat addition doubled: CAUGHT (11 failing)
[3] s.47(b) rounding half up -> down: CAUGHT (8 failing)
[4] s.47(b) ratio inverted: CAUGHT (21 failing)
[5] s.45(a) months: completed -> same-day counts one more: CAUGHT (12 failing)
[6] s.43 thirty days -> thirty-one: CAUGHT (28 failing)
[7] s.44(d) deemed day -> the day after: CAUGHT (15 failing)
[8] s.42(b) contents: drop limb (b)(4): CAUGHT (1 failing)
[9] Third Schedule item (4) corporation dash -> 0: CAUGHT (5 failing)
[10] Third Schedule item (3) individual 5,000 -> 6,000: CAUGHT (5 failing)
[11] s.41(b) cap: corporation 80,000 -> 60,000: CAUGHT (5 failing)
[12] s.41(b) cap: AT MOST -> LESS THAN: CAUGHT (4 failing)
[13] s.41(a) limb order: dash reached before Chapter 6: CAUGHT (1 failing)
[14] s.48 thirty days -> thirty-one: CAUGHT (8 failing)
[15] s.50(a) twelve -> thirteen instalments: CAUGHT (1 failing)
[16] s.49 late: on the last day counts as late: CAUGHT (2 failing)
[17] s.53 thirty days -> twenty-nine: CAUGHT (18 failing)
[18] s.54(b) window inside -> outside: CAUGHT (1 failing)
[19] s.56 forty-five days -> forty: CAUGHT (10 failing)
[20] s.57(e) corporation four years -> two: CAUGHT (4 failing)
[21] s.57(a) item (6) required for individuals too: CAUGHT (2 failing)
[22] s.55 allows a second sanction (act reference ignored): CAUGHT (1 failing)
[23] s.56(c) refund: whole amount always: CAUGHT (3 failing)
[24] s.43/s.44(d): no representations counts as made: CAUGHT (2 failing)
[25] s.47(a): a silent violator updated at the demand day, not the notice day: CAUGHT (3 failing)
[26] s.45(b) same provision -> same item: CAUGHT (3 failing)
[27] Third Schedule item (7) corporation 6,000 -> 3,000: CAUGHT (3 failing)
[28] s.46(a) floor: additions not counted: CAUGHT (2 failing)
[29] s.57(e) individual two years -> four: CAUGHT (4 failing)
[30] s.43 an early extension shortens the period (later-of takes the official's day): CAUGHT (12 failing)
[31] s.43 an act on the day of delivery is untimely: CAUGHT (3 failing)
[32] s.53 a request on the day of delivery is untimely: CAUGHT (1 failing)
[33] s.56 an appeal on the day of delivery is untimely: CAUGHT (1 failing)
[34] s.48 a payment on the day of delivery is untimely: CAUGHT (1 failing)
[35] s.44 a notice that omits what s.42(b) requires is deemed a demand: CAUGHT (5 failing)
[36] s.53(b) an early extension shortens the period: CAUGHT (4 failing)
[37] s.44(d) treated as a demand: the validity of the notice is not asked: CAUGHT (1 failing)
```

## 1. Coverage

One row per provision of the scope, in the Law's numbering; the Hebrew is the first words of the provision, copied from `phase1/coverage.tsv`.
Dispositions: 68 encoded, 1 inert, 2 out-of-scope, 2 refused.
Nothing is `deferred`: 0 rows.
One disposition differs from the survey: s.57(f) (inert in the survey, encoded here, by ruling 2 of the brief: a power of the Minister is a regulative `MAY`).
Every rule name in the table was checked to exist in the module it is credited to.

| id | provision | Hebrew (by script) | disposition | module | rule | note |
| --- | --- | --- | --- | --- | --- | --- |
| 41 | s.41 | עיצום כספי | encoded | `g6-schedule-three` | — | (container: carried by the lettered rows below) |
| 41(a) | s.41(a) | הפר אדם הוראה מההוראות לפי חוק זה, כמפורט … | encoded | `g6-schedule-three` | `s 41(a) — a financial sanction may be imposed for`<br>`s 41(a) — the Commissioner may impose the financial sanction for`<br>`s 41(a) — the amount the Third Schedule fixes for` |  |
| 41(b) | s.41(b) | השר, בהסכמת שר המשפטים, ובאישור ועדת העבודה והרווחה … | encoded | `g6-schedule-three` | `s 41(b) — the Minister may change the Third Schedule by order`<br>`s 41(b) — the Minister may change the Third Schedule by an order that sets`<br>`s 41(b) — every row is within the cap`<br>`s 41(b) — the cap on a column B amount for` | A power (ruling 2): a MAY with its two preconditions and the cap as a computable condition; the order's content is an input. |
| 42 | s.42 | הודעה על כוונת חיוב | encoded | `g6-notice-and-hearing` | — | (container: carried by the lettered rows below) |
| 42(a) | s.42(a) | היה לממונה יסוד סביר להניח כי אדם הפר … | encoded | `g6-notice-and-hearing` | `s 42(a) — the Commissioner must give notice of intention` | A MUST with no deadline (none is stated); grounds and intention are inputs. |
| 42(b) | s.42(b) | בהודעה על כוונת חיוב יציין הממונה, בין השאר, … | encoded | `g6-notice-and-hearing` | `s 42(b) — the notice of intention states what the Law requires` | The guard on the act of giving the notice. |
| 42(b)(1) | s.42(b)(1) | המעשה או המחדל (בפרק זה – המעשה), המהווה … | encoded | `g6-notice-and-hearing` | `s 42(b) — the notice of intention states what the Law requires` | Limb (b)(1) of the predicate. |
| 42(b)(2) | s.42(b)(2) | סכום העיצום הכספי והתקופה לתשלומו; | encoded | `g6-notice-and-hearing` | `s 42(b) — the notice of intention states what the Law requires` | Limbs (b)(2): the amount and the period for payment. |
| 42(b)(3) | s.42(b)(3) | זכותו של המפר לטעון את טענותיו לפני הממונה … | encoded | `g6-notice-and-hearing` | `s 42(b) — the notice of intention states what the Law requires` | Limbs (b)(3): the right to make representations, and the notice treated as a demand. |
| 42(b)(4) | s.42(b)(4) | הסמכות להוסיף על סכום העיצום הכספי בשל הפרה … | encoded | `g6-notice-and-hearing` | `s 42(b) — the notice of intention states what the Law requires` | Limb (b)(4); see also fork F-ADD. |
| 43 | s.43 | זכות טיעון — מפר שנמסרה לו הודעה על כוונת … | encoded | `g6-notice-and-hearing` | `s 43 — the last day for representations`<br>`s 43 — the violator may make written representations`<br>`s 43 — the Commissioner may extend the period for representations`<br>`s 43 — the day`<br>`s 43 — counting the day after delivery as the first day, the day`<br>`s 43 — the last day for representations, an extension that ends before the 30 days being taken as it is` | Kind W, IL s.10(a) and (c); forks F-ACTDAY (an act on the day of delivery is timely), F-SHORTEN (an extension cannot shorten), F-NOTICE. |
| 44 | s.44 | החלטת הממונה ודרישת תשלום | encoded | `g6-notice-and-hearing` | — | (container: carried by the lettered rows below) |
| 44(a) | s.44(a) | הממונה יחליט, לאחר ששקל את הטענות שנטענו לפי … | encoded | `g6-notice-and-hearing` | `s 44(a) — the Commissioner decides after representations` | The decision is an input (an enum). |
| 44(b) | s.44(b) | החליט הממונה לפי הוראות סעיף קטן (א) – | encoded | `g6-notice-and-hearing` | `s 44(b) — what the Commissioner must give the violator after deciding` |  |
| 44(b)(1) | s.44(b)(1) | להטיל על המפר עיצום כספי – ימסור לו … | encoded | `g6-notice-and-hearing` | `s 44(b)(1) and (c) — the payment demand states what the Law requires` |  |
| 44(b)(2) | s.44(b)(2) | שלא להטיל על המפר עיצום כספי – ימסור … | encoded | `g6-notice-and-hearing` | `s 44(b)(2) and (c) — the notice of no sanction states what the Law requires` |  |
| 44(c) | s.44(c) | בדרישת התשלום או בהודעה לפי סעיף קטן (ב) … | encoded | `g6-notice-and-hearing` | `s 44(b)(1) and (c) — the payment demand states what the Law requires`<br>`s 44(b)(2) and (c) — the notice of no sanction states what the Law requires` | The reasons limb of the two predicates. |
| 44(d) | s.44(d) | לא טען המפר את טענותיו לפי הוראות סעיף … | encoded | `g6-notice-and-hearing` | `s 44(d) — the day the notice of intention is treated as a payment demand delivered`<br>`s 44(d) — the notice of intention is treated as a payment demand`<br>`s 44 — the day the payment demand is delivered or treated as delivered`<br>`s 44 — the day the payment demand is delivered or treated as delivered, whatever the notice states`<br>`s 44(d) — the notice` | Kind C; forks F-DEEMED, F-C, F-NOTICE (a notice that omits what s.42(b) requires is not deemed a demand). |
| 45 | s.45 | הפרה נמשכת והפרה חוזרת | encoded | `g6-amount` | — | (container: carried by the lettered rows below) |
| 45(a) | s.45(a) | בהפרה נמשכת ייווסף על העיצום הכספי הקבוע לאותה … | encoded | `g6-amount` | `s 45(a) — the whole months a violation continued from`<br>`s 45(a) — the addition of one fiftieth of` | Forks F-MONTHS, F-START, F-BASE, F-ADD. |
| 45(b) | s.45(b) | בהפרה חוזרת ייווסף על העיצום הכספי הקבוע לאותה … | encoded | `g6-amount` | `s 45(b) — the violation`<br>`s 45(b) — the previous violation makes the violation a repeat violation`<br>`s 45(b) — the addition for a repeat violation of` | Kind B; forks F-SAME, F-WINDOW. |
| 46 | s.46 | סכומים מופחתים | encoded | `g6-amount` | — | (container: carried by the lettered rows below) |
| 46(a) | s.46(a) | הממונה אינו רשאי להטיל עיצום כספי בסכום הנמוך … | encoded | `g6-amount` | `s 46(a) — a sanction of`<br>`s 46(a) — the Commissioner shall not impose a sanction below the floor of` | A SHANT with a guard; fork F-FLOOR. |
| 46(b) | s.46(b) | השר, בהסכמת שר המשפטים ובאישור ועדת העבודה והרווחה … | refused | `g6-amount` | `s 46 — the lowest sanction the Commissioner may impose`<br>`s 46(b) — the Minister may set the circumstances and rates for lower amounts`<br>`s 46(b) — no regulations fixing the circumstances and the rates for lower amounts are in the sources, so no lower floor can be computed` | Disposition kept from the survey: the power is encoded (ruling 2); a floor that relies on its regulations is a named REFUSE unless the caller supplies the rate of reduction. |
| 47 | s.47 | סכום מעודכן של העיצום הכספי | encoded | `g6-amount` | — | (container: carried by the lettered rows below) |
| 47(a) | s.47(a) | העיצום הכספי יהיה לפי סכומו המעודכן ביום מסירת … | encoded | `g6-amount` | `s 47(a) — the day on which the amount of the sanction is updated` | Fork F-DAY. |
| 47(b) | s.47(b) | סכומי העיצום הכספי הקבועים לפי סימן זה יתעדכנו … | encoded | `g6-amount` | `s 47(b) — the amount of`<br>`s 47(b) — the index known on`<br>`s 47(b) — the nearest multiple of NIS 10 to` | Kind R; forks F-ROUND, F-CHAIN, F-FIRST, F-R. |
| 47(c) | s.47(c) | הממונה יפרסם ברשומות הודעה על סכומי העיצום הכספי … | encoded | `g6-amount` | `s 47(c) — the Commissioner must publish the updated amounts in Reshumot` | A MUST with no deadline. |
| 48 | s.48 | המועד לתשלום העיצום הכספי — על המפר לשלם את העיצום הכספי … | encoded | `g6-payment` | `s 48 — the last day of the 30 days from the delivery of the payment demand`<br>`s 48 — the violator must pay the financial sanction of`<br>`s 48 — the day`<br>`s 48 — counting the day after delivery as the first day, the day` | Kind D; forks F-D, F-PERIOD, F-ACTDAY. |
| 49 | s.49 | ריבית שקלית ודמי פיגורים — לא שילם המפר עיצום כספי במועד, … | refused | `g6-payment` | `s 49 — the amount owed on a sanction of`<br>`s 49 — the payment of`<br>`s 49 — the days of delay, from the day after`<br>`s 49 — the shekel interest and the arrears fees are fixed by the Interest and Linkage Law, whose rates are not in the sources, and none was supplied` | Disposition kept from the survey: the liability is encoded, the amount is a named REFUSE unless the caller supplies the accrued shekel interest and arrears fees; fork F-INTEREST. |
| 49/def1 | s.49 def.1 | ”דמי פיגורים“ ו”ריבית שקלית“ – כהגדרתם בחוק פסיקת … | out-of-scope | `g6-payment` | `s 49 — the amount owed on a sanction of` | Defers to the Interest and Linkage Law: carried as the two inputs `the shekel interest accrued over the delay` and `the arrears fees accrued over the delay`. |
| 49/def2 | s.49 def.2 | ”חוק פסיקת ריבית והצמדה“ – חוק פסיקת ריבית … | out-of-scope | `g6-payment` | `s 49 — the shekel interest and the arrears fees are fixed by the Interest and Linkage Law, whose rates are not in the sources, and none was supplied` | Names the external statute: carried as the source of those two inputs and as the text of the named refusal. |
| 50 | s.50 | פריסת תשלום העיצום הכספי | encoded | `g6-payment` | — | (container: carried by the lettered rows below) |
| 50(a) | s.50(a) | הממונה רשאי, לבקשת המפר, להחליט על פריסת התשלום … | encoded | `g6-payment` | `s 50(a) — an instalment plan is within what the Law allows`<br>`s 50(a) — the Commissioner may allow payment by instalments` | Kind Q (a count of payments). |
| 50(b) | s.50(b) | לא שילם המפר תשלום במועדו, יראו את החלטת … | encoded | `g6-payment` | `s 50(b) — the decision on instalments is treated as void and the balance falls due at once`<br>`s 50(b) — the balance of the debt that falls due at once on a sanction of` | s.49 then applies to the balance: see s.49 rules. |
| 51 | s.51 | גבייה — עיצום כספי ייגבה לאוצר המדינה, ועל … | inert | `g6-payment` | `s 51 — the payee of a financial sanction` | Disposition kept from the survey: the destination of the money is carried as the constant; the Collection Centre Law is outside the scope. |
| 52 | s.52 | התראה מינהלית | encoded | `g6-warning` | — | (container: carried by the lettered rows below) |
| 52(a) | s.52(a) | היה לממונה יסוד סביר להניח כי אדם הפר … | encoded | `g6-warning` | `s 52(a) — the Commissioner may give an administrative warning instead of a financial sanction`<br>`s 52(a) — the Commissioner may give the violator an administrative warning` |  |
| 52(b) | s.52(b) | בהתראה מינהלית יציין הממונה מהו המעשה המהווה את … | encoded | `g6-warning` | `s 52(b) — the administrative warning states what the Law requires` |  |
| 53 | s.53 | בקשה לביטול התראה מינהלית | encoded | `g6-warning` | — | (container: carried by the lettered rows below) |
| 53(a) | s.53(a) | נמסרה למפר התראה מינהלית כאמור בסעיף 52, רשאי … | encoded | `g6-warning` | `s 53(a) — the violator may ask for the warning to be cancelled`<br>`s 53(a), (b) — the last day to ask to cancel`<br>`s 53(a) — the day`<br>`s 53(a) — counting the day after delivery as the first day, the day` | Kind W; forks F-W, F-ANCHOR, F-ACTDAY. |
| 53(a)(1) | s.53(a)(1) | המפר לא ביצע את ההפרה; | encoded | `g6-warning` | `s 53(a) — the violator may ask for the warning to be cancelled` | The constructor `the violator did not commit the breach` of `Ground for cancelling a warning` (g6-nouns). |
| 53(a)(2) | s.53(a)(2) | המעשה שביצע המפר, המפורט בהתראה, אינו מהווה הפרה. | encoded | `g6-warning` | `s 53(a) — the violator may ask for the warning to be cancelled` | The constructor `the act the violator committed, as detailed in the warning, is not a breach` (g6-nouns). |
| 53(b) | s.53(b) | הממונה רשאי להאריך את התקופה האמורה בסעיף קטן … | encoded | `g6-warning` | `s 53(b) — the Commissioner may extend the period to ask for cancellation`<br>`s 53(b) — taking an extension that ends before the 30 days as it is, the last day to ask to cancel` | Kind X; forks F-EXT, F-SHORTEN. |
| 53(c) | s.53(c) | קיבל הממונה בקשה לביטול התראה מינהלית, לפי הוראות … | encoded | `g6-warning` | `s 53(c) — the Commissioner decides a request to cancel the warning`<br>`s 53(c) — the decision is in writing and gives reasons` |  |
| 54 | s.54 | הפרה נמשכת והפרה חוזרת לאחר התראה | encoded | `g6-warning` | — | (container: carried by the lettered rows below) |
| 54(a) | s.54(a) | נמסרה למפר התראה מינהלית לפי הוראות סימן זה … | encoded | `g6-warning` | `s 54(a) — a breach continued after`<br>`s 54 — the Commissioner must give notice of intention after a warning` | Forks F-CANCEL, F-START, F-MUST54. |
| 54(b) | s.54(b) | נמסרה למפר התראה מינהלית לפי הוראות סימן זה … | encoded | `g6-warning` | `s 54(b) — the further violation after`<br>`s 54(b) — the last day of the two years from the delivery of` | Kind B; fork F-WINDOW-54. |
| 55 | s.55 | עיצום כספי בשל הפרה לפי חוק זה ולפי חוק אחר — על מעשה אחד המהווה כמה הפרות … | encoded | `g6-appeal-and-publication` | `s 55 — a financial sanction may still be imposed for`<br>`s 55 — no act has more than one financial sanction among`<br>`s 55 — the Commissioner shall not impose a further sanction for the same act` |  |
| 56 | s.56 | ערעור | encoded | `g6-appeal-and-publication` | — | (container: carried by the lettered rows below) |
| 56(a) | s.56(a) | על החלטה סופית של הממונה לפי פרק זה … | encoded | `g6-appeal-and-publication` | `s 56(a) — the last day of the 45 days from`<br>`s 56(a) — the violator may appeal to the Magistrates' Court`<br>`s 56(a) — the day notice of the decision counts as delivered to a violator who made no representations`<br>`s 56(a) — the day`<br>`s 56(a) — counting the day after delivery as the first day, the day` | Kind W; forks F-W, F-APPEAL-DEEMED, F-ACTDAY. |
| 56(b) | s.56(b) | אין בהגשת ערעור כאמור בסעיף קטן (א) כדי … | encoded | `g6-appeal-and-publication` | `s 56(b) — the filing of the appeal stays the execution of the decision, given` |  |
| 56(c) | s.56(c) | החליט בית המשפט, לאחר ששולם העיצום הכספי, לקבל … | encoded | `g6-appeal-and-publication` | `s 56(c) — the amount to be returned of`<br>`s 56(c) — the amount returned with shekel interest` | Trap T40: shekel interest only, no arrears fees. |
| 57 | s.57 | פרסום | encoded | `g6-appeal-and-publication` | — | (container: carried by the lettered rows below) |
| 57(a) | s.57(a) | הטיל הממונה עיצום כספי לפי פרק זה, יפרסם … | encoded | `g6-appeal-and-publication` | `s 57(a) — the Commissioner must publish the particulars of the financial sanction`<br>`s 57(a) — the numbers of the items the Law requires where`<br>`s 57(a) — the publication deals with each item as the Law requires, given the items` |  |
| 57(a)(1) | s.57(a)(1) | דבר הטלת העיצום הכספי; | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 1: always required. |
| 57(a)(2) | s.57(a)(2) | מהות ההפרה שבשלה הוטל העיצום הכספי, מועד ביצוע … | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 2: always required. |
| 57(a)(3) | s.57(a)(3) | סכום העיצום הכספי שהוטל; | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 3: always required. |
| 57(a)(4) | s.57(a)(4) | אם הופחת סכום העיצום הכספי – הנסיבות שבשלהן … | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 4: required only if the amount was reduced. |
| 57(a)(5) | s.57(a)(5) | פרטים על אודות המפר, הנוגעים לעניין; | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 5: always required; "relevant" is the Commissioner's judgement and arrives as the item's `published` fact. |
| 57(a)(6) | s.57(a)(6) | שמו של המפר – אם המפר הוא תאגיד. | encoded | `g6-appeal-and-publication` | `s 57(a) — the numbers of the items the Law requires where` | Item 6: required only for a corporation. |
| 57(b) | s.57(b) | הוגש ערעור לפי סעיף 56 על החלטת הממונה … | encoded | `g6-appeal-and-publication` | `s 57(b) — the Commissioner must publish the appeal and its result` |  |
| 57(c) | s.57(c) | על אף הוראות סעיף קטן (א)(6), הממונה רשאי … | encoded | `g6-appeal-and-publication` | `s 57(c) — the Commissioner may publish the name of the violator`<br>`s 57(c) — the Commissioner's power to publish an individual's name` |  |
| 57(d) | s.57(d) | על אף האמור בסעיף זה, לא יפרסם הממונה … | encoded | `g6-appeal-and-publication` | `s 57(a), (d) — the item is dealt with as the Law requires`<br>`s 57(d) — the Commissioner shall not publish a particular that section 9(a) bars` | The Freedom of Information Law's s.9 is outside the scope: whether a particular is barred is an input. |
| 57(e) | s.57(e) | פרסום לפי סעיף זה בעניין עיצום כספי שהוטל … | encoded | `g6-appeal-and-publication` | `s 57(e) — the last day of the publication period that began on`<br>`s 57(e) — the Ministry must apply technological measures when the publication that began on` | Kind V; fork F-VALID. |
| 57(f) | s.57(f) | השר רשאי לקבוע דרכים נוספות לפרסום הפרטים האמורים … | encoded (survey: inert) | `g6-appeal-and-publication` | `s 57(f) — the Minister may set further ways of publishing the particulars` | CHANGED from `inert` (survey) to `encoded` by the brief's ruling 2: a power of the Minister is a MAY rule, even where no exercise of it is in the sources. |
| S3.1 | S3.1 | עוסק שביצע עבודה במערכת קירור או מיזוג אוויר … | encoded | `g6-schedule-three` | `Third Schedule item (1)` |  |
| S3.2 | S3.2 | ביצע עבודה במערכת קירור או מיזוג אוויר בלי … | encoded | `g6-schedule-three` | `Third Schedule item (2)` |  |
| S3.3 | S3.3 | פרסם עצמו כבעל רישיון בלי שיש בידו רישיון … | encoded | `g6-schedule-three` | `Third Schedule item (3)` |  |
| S3.4 | S3.4 | בעל רישיון שביצע התקנה של מערכת קירור או … | encoded | `g6-schedule-three` | `Third Schedule item (4)` |  |
| S3.5 | S3.5 | מפעיל שהפעיל אדם אחר בביצוע עבודה במערכת קירור … | encoded | `g6-schedule-three` | `Third Schedule item (5)` |  |
| S3.6 | S3.6 | מפעיל שהפעיל אדם אחר בביצוע עבודה במערכת קירור … | encoded | `g6-schedule-three` | `Third Schedule item (6)` |  |
| S3.7 | S3.7 | לא מסר מסמך לפי דרישת מפקח שניתנה לפי … | encoded | `g6-schedule-three` | `Third Schedule item (7)` |  |

What is not a row because the Law gives no provision for it, and so is not encoded (traps T12 and T13):
a licensee who breaches a licence condition (s.3(a), s.17(d)) and a person who breaches ss.12, 14, 15, 16, 17 or 18(b) have no Third Schedule row, so there is no amount and no `Listed violation` for them; the encoding does not invent one.

## 2. Forks

Each fork gives: where, the readings, the one taken, the text that licenses each, the callable alternative, and the test.
"Red" is the number of the assertion in `g6-tests-red.l4` that asserts the answer of the rejected reading and fails; the tests named are passing assertions of the alternative's own answer.
Where a fork is a reading of a deontic rule, the alternative is traced in its module's test file and has no red assertion (a `DEONTIC` cannot be compared).

### The kinds of period (ruling 4 of the brief)

For every kind of period met in this scope, here is whether IL s.10(c) was applied and why.
IL s.10(c) is the Interpretation Law's own (the Hebrew is in the vendored `il-interpretation-time.l4` at its `src:85` line; my translation, not a quotation): days of rest, recess or holiday fixed by an enactment do count in the days of a period, unless they are the last days of the period; so a period whose last day falls on one ends on the first day after it that is not one.
This Law's s.10(c) is something else.

- **F-D, kind D, a deadline for doing something (P31, s.48: 30 days from delivery of the payment demand).**
  Taken: IL s.10(a), the day of delivery not counted, and IL s.10(c) applied, so a last day that is a day of rest, recess or holiday moves to the next day that is not one (ruling 4).
  Why: a deadline for paying is a time within which a person must act, which is what (c) is for.
  Alternative: `s 48 — the last day of the 30 days from the delivery of the payment demand, without s 10(c)`.
  Test: `g6-tests-payment.l4`, "s 48: 30 days from the delivery of the demand" (Friday 2 July 2027 against Sunday 4 July 2027).
  Red: 7.
- **F-W, kind W, a window in which a request or an act may be made (P26 s.43, P33 s.53(a), P35 s.56(a)).**
  Taken: IL s.10(a) and IL s.10(c) applied, as for F-D; the day of delivery is itself timely (F-ACTDAY) and an extension cannot shorten the 30 days (F-SHORTEN), both below.
  Alternatives: `s 43 — the last day of the 30 days from the delivery of the notice, without s 10(c)`, `s 53(a) — without s 10(c), the last day of the 30 days from`, `s 56(a) — without s 10(c), the last day of the 45 days from`.
  Tests: "s 43: 30 days from delivery" in `g6-tests-notice-and-hearing.l4`, "s 53(a)" in `g6-tests-warning.l4`, "s 56(a)" in `g6-tests-appeal-and-publication.l4`.
  Red: 4, 5, 6.
- **F-VALID, kind V, a period of validity (P37 s.57(e): publication for four years or two).**
  Taken: IL s.10(b), years after an event, the last day inside the period; IL s.10(c) NOT applied (ruling 4).
  Why: the publication period is not a time for doing something, and applying (c) would lengthen a publication by a rest day.
  Alternative: `s 57(e) — with s 10(c) applied, the last day of the publication period that began on`.
  Test: "s 57(e)" in `g6-tests-appeal-and-publication.l4` (Monday 3 September 2029 a holiday: 3 September against 4 September).
  Red: 8.
  The other V rows are not periods with a last day to move: P28 (a count of months, F-MONTHS), P36 (the days from payment to refund) and P45 (the days of the delay) are counts of days, computed by `Day` differences; IL s.10(c) does not apply to a count.
- **F-C, kind C, a date counted from another date (P27 s.44(d): "at the end of that period").**
  Taken: the date is the last day of the s.43 period, whose end already has the kind-W reading; IL s.10(c) is NOT applied a second time by s.44(d) itself.
  Alternative: `s 43 — the last day for representations, with s 10(c) applied to an extension as well` (as the deemed demand's day).
  The two coincide wherever s.43's own end is not an official's chosen day; they differ for an extension that ends on a day of rest.
  Test: "Forks F-X, F-C and F-DEEMED" in `g6-tests-notice-and-hearing.l4` (an extension to Saturday 10 April 2027: 10 April against 11 April).
  Red: 10.
- **F-X, kind X, a length fixed by an official (s.43 and s.53(b): "the Commissioner may extend the said period").**
  Taken: the extension is the day the Commissioner chose, an input, used as it is; it is outside IL s.10.
  Alternative and test: as F-C; red 10.
- **F-WINDOW, kind B, "within two years of the previous violation" (P29 s.45(b)).**
  Here the survey (kind W, IL s.10(b)) and the lead's note to G6 (kind B, outside IL s.10, plain comparison, test both sides) differ.
  Taken, following the lead's note: the window classifies a violation; it is not a time for doing something.
  IL s.10 says nothing of "within" (the vendored NOTES, F8), but it is the only source for what "two years after a day" means (same-numbered day, the month's last day), so the encoding uses IL s.10(b)'s end rule for the arithmetic and does NOT apply IL s.10(c).
  The last day is inside the window; the day of the previous violation is not.
  Alternative: the PLAN's kind W, with IL s.10(c): `s 45(b) — the previous violation, with s 10(c) applied to the window, makes the violation a repeat violation`.
  Test: "s 45(b)" in `g6-tests-amount.l4` (16 March 2029 inside, 17 March outside; with 16 and 17 March days of rest, 18 March inside).
  Red: 17.
- **F-WINDOW-54, kind B, "within two years of the day the warning was delivered" (P34 s.54(b)).**
  Taken and alternative as F-WINDOW.
  Alternative: `s 54(b) — with s 10(c) applied to the window, the further violation after`.
  Test: "s 54(b)" in `g6-tests-warning.l4` (3 March 2029 inside, 4 March outside; with Saturday 3 March 2029 a day of rest, 4 March inside).
  Red: 18.
- **F-R, kind R, "each 1 January" (P30 s.47(b)).**
  Taken: the update day is 1 January even when it is a day of rest, and the amount is updated from it; a recurring calendar date is not a period, so IL s.10 does not reach it.
  Alternative: `s 47(b) — the update day of ... if s 10(c) moved it past days of rest` (moves 1 January 2027, a Friday, with Saturday 2 January a day of rest, to Sunday 3 January).
  Test: "Fork F-R" in `g6-tests-amount.l4`.
  Red: 24.
- **Kind Q, "not more than 12 monthly payments" (P32 s.50(a)).**
  A count of payments, not a period; IL s.10 does not apply and there is nothing to register.
  Tested at both sides of the threshold (12 allowed, 13 not, 0 not).

### The other forks

- **F-DASH (trap T14): the dashes in the corporation column for items (1), (2) and (4).**
  Readings: (a) no amount is fixed, so the Law does not say what a corporation owes: a named `REFUSE` (taken); (b) a dash means no sanction may be imposed on that kind of person for that item; (c) zero; (d) the individual's amount.
  Text: s.41(a) says the amount is «בסכום הקבוע בטור ב׳ לצידה» ("in the amount fixed in column B beside it"); the Law prints a dash and does not say what it means.
  Taken: (a), at the decision level (`s 41(a) — the amount the Third Schedule fixes for ...`, and the power predicate `s 41(a) — a financial sanction may be imposed for`, which refuses only when the Law's earlier answers hold: Chapter 6 in force and the officer authorised).
  The table itself (`s 41(a) — column B sets, for ... and ...`) is a `MAYBE NUMBER` with `NOTHING` at a dash, so it says exactly what the Law prints.
  Alternative (b), callable: `s 41(a) — reading a dash as no sanction, a financial sanction may be imposed for`.
  (c) and (d) have no callable function: they are the answers the trap names as wrong.
  Test: "The alternative reading of a dash" in `g6-tests-schedule-three.l4`.
  Red: 1 (d), 2 (c).
- **F-CAP (trap T15): the cap of s.41(b) against s.45 and s.47(b).**
  Readings: the cap of 40,000 / 80,000 bounds the amount an order sets in column B (taken); the cap also bounds what is payable after the s.45 additions and the s.47(b) updates.
  Text: «ובלבד שסכום העיצום הכספי שייקבע בטור ב׳ שבה, לא יעלה על 40,000 שקלים חדשים» ("provided that the amount of the financial sanction that shall be fixed in its column B shall not exceed 40,000 new shekels") speaks of what an order sets; s.45 adds to "the fixed sanction" and s.47(b) updates the fixed amounts, and neither mentions the cap.
  Callable alternative: `s 45 to 47 — the financial sanction for the violation, held to the cap of s 41(b)`.
  Test: "Fork F-CAP" in `g6-tests-amount.l4`, and, for the reading taken, "ss 45 to 47 together" (item (5) for a corporation, repeat: 80,000, the cap exactly; with six months, 84,800).
  Red: 3.
- **F-NOTICE: a notice that omits what s.42(b) lists.**
  Readings: it is not "a notice under s.42", so s.43 gives no right of representation and s.44(d) deems nothing: the day the demand is treated as delivered is NOTHING (taken, as the guard on the act); it is a notice that starts the 30 days whatever it states, gives the right, and is deemed a demand when no representations are made.
  History: until the independent review the code gave the violator no right (s.43) and still deemed the same notice a payment demand (s.44); the two now agree.
  Text: s.43 gives the right to a violator «מפר שנמסרה לו הודעה על כוונת חיוב לפי הוראות סעיף 42» ("a violator to whom a notice of intention was delivered under the provisions of s.42"); s.42(b) says the notice states "among other things" the listed items.
  Callable alternatives: (a deontic) `s 43 — the violator may make written representations, whatever the notice states`, and `s 44 — the day the payment demand is delivered or treated as delivered, whatever the notice states`; used together they are the other reading.
  Tests: traced in `g6-tests-notice-and-hearing.l4`, "Forks F-X, F-C and F-DEEMED"; asserted there, "Fork F-NOTICE read through to s.44(d)".
  Red: 39 (the day the demand is treated as delivered for a notice silent on the right to argue: 2 April 2027 against NOTHING); no red assertion for the deontic.
- **F-EXT: an extension without recorded reasons.**
  Readings: it is ignored (taken); it counts.
  Text: s.43 and s.53(b) allow the Commissioner to extend «מטעמים מיוחדים שיירשמו» ("for special reasons that shall be recorded").
  Callable alternative: `s 43 — the last day for representations, without s 10(c) and counting an extension whether or not reasons were recorded`.
  Test: "s 43" in `g6-tests-notice-and-hearing.l4`; s.53(b): `g6-tests-warning.l4`.
  Red: 9.
- **F-ACTDAY (the independent review, DIS-2): an act on the day of delivery (s.43, s.48, s.53(a), s.56(a)).**
  Readings: an act on the day the notice, demand, warning or decision is delivered is within the period: it is timely when the day is the day of delivery or later and the last day or earlier (taken); the period starts the day AFTER delivery, so an act on the day of delivery is late.
  Text: s.43 «בתוך 30 ימים ממועד מסירת ההודעה» ("within 30 days from the time of delivery of the notice"), s.48 «בתוך 30 ימים מיום מסירת» ("within 30 days from the day of delivery of"), s.53(a) «בתוך 30 ימים» ("within 30 days") and s.56(a) «בתוך 45 ימים מיום שנמסרה» ("within 45 days from the day on which notice was delivered"); IL s.10(a) leaves the day of delivery out of the COUNT that fixes the last day and says nothing that makes an act on that day late.
  Why: counting representations made the day the notice arrives as late would have deemed the notice a payment demand under s.44(d) although the violator argued.
  Only the date predicates changed: the deontic rules already allowed an act AT 0 (the WITHIN counts from the day of delivery).
  Callable alternatives (the strict reading): `s 43 — counting the day after delivery as the first day, the day ... is within the period for representations of`, `s 43, s 44(d) — counting the day after delivery as the first day, the violator made his representations within the period`, `s 48 — counting the day after delivery as the first day, the day ...`, `s 53(a) — counting the day after delivery as the first day, the day ...`, `s 56(a) — counting the day after delivery as the first day, the day ...`.
  Tests: the "Both edges" blocks in `g6-tests-notice-and-hearing.l4`, `g6-tests-warning.l4`, `g6-tests-appeal-and-publication.l4` and `g6-tests-payment.l4`, each with the strict reading asserted and the day before delivery not timely.
  Red: 32 (s.43), 33 (s.43 and s.44(d)), 34 (s.53(a)), 35 (s.56(a)), 36 (s.48), 40 (its consequence under s.44(d): a violator who argued on the day of delivery is not deemed silent).
  History: the strict reading was the encoding's own until the independent test author showed it wrong; the assertions that encoded it were moved to the red file (32-36), and s.48 was repaired with the other three (same defect, not in the review's list).
  Not changed: `s 57(e) — the day ... is within the publication period` (a period of validity of the publication, kind V, not a window for an act); whether the day of publication itself is inside it is open (section 7).
- **F-SHORTEN (the independent review, DIS-3): an "extension" that ends before the 30 days are out (s.43, s.53(b)).**
  Readings: to "extend" a period is to lengthen it, so the 30 days stand and an extension takes effect only when it ends later: the last day is the later of the Commissioner's day and the standard end (taken); the Commissioner's day is the end whatever day it is.
  Text: s.43 «להאריך את התקופה האמורה» ("the Commissioner may extend the said period"); s.53(b) says the same of the period to ask to cancel.
  The standard end it is compared with has IL s.10(c) applied (as the 30 days do); the Commissioner's day, when later, is used as it is (F-X).
  The F-EXT alternative also takes the later of the two.
  Callable alternatives: `s 43 — the last day for representations, an extension that ends before the 30 days being taken as it is`, `s 53(b) — taking an extension that ends before the 30 days as it is, the last day to ask to cancel`.
  Tests: "Fork F-SHORTEN" in `g6-tests-notice-and-hearing.l4` and `g6-tests-warning.l4` (an extension to 20 March 2027 for a delivery on 3 March: the last day stays 2 April; an extension to Saturday 3 April when 2 and 3 April are days of rest: 4 April).
  Red: 37 (s.43), 38 (s.53(b)).
- **F-DEEMED (trap T16): which day is "the said date" in s.44(d).**
  Readings: (a) the last day of the s.43 period, so the notice is a demand delivered at the end of the period (taken); (b) the day after that last day; (c) the day the notice of intention was in fact delivered.
  Text: «בתום אותה תקופה, כדרישת תשלום שנמסרה למפר במועד האמור» ("at the end of that period, as a payment demand delivered to the violator on the said date"); no date is "said" in s.44(d) itself except the end of the period; s.47(a) gives a silent violator the day the notice was delivered for the update, which would be redundant under (c).
  Why (a): under (c) the s.48 thirty days would end the same day the s.43 thirty days end (the violator's time to pay would end the day his time to argue ends), and s.47(a)'s special rule for a silent violator would say nothing new.
  Callable alternatives: (b) `s 44(d) — the day the notice of intention is treated as a payment demand delivered, counting from the day after the period ends`; (c) `s 44(d) — ..., the said date being the day the notice was delivered`.
  Test: "s 44(d)" and "Forks F-X, F-C and F-DEEMED" in `g6-tests-notice-and-hearing.l4`; the 60-day consequence in `g6-tests-payment.l4` (the comment "Trap T16" under "s 48").
  Red: 11 (b), 12 (c).
- **F-PERIOD (trap T16): the period for payment the notice and the demand state, against s.48's 30 days.**
  Readings: s.48's 30 days govern, whatever the demand states (taken); a period stated in the demand governs when there is one.
  Text: s.42(b)(2) and s.44(b)(1) say the notice and the demand "state" the period for payment; s.48 says the violator "shall pay within 30 days of the delivery of the payment demand".
  Callable alternative: `s 48 — the last day for payment, when a period stated in the demand governs`.
  Test: the comment "The period the demand states (F-PERIOD)" under "s 48" in `g6-tests-payment.l4`.
  Red: 26.
- **F-MONTHS (trap T18): "for each month in which the violation continues".**
  Readings: the months COMPLETED after the day the violation started, each month ending on the same-numbered day (IL s.10(b)), counting only if the violation was still continuing on that day (taken: the narrower reading, since a sanction is read strictly against the person it burdens); the calendar months touched, first and part months included; the calendar months touched after the first.
  Text: «לכל חודש שבו נמשכת ההפרה»; IL s.3 makes a month a Gregorian month and IL s.10(b) says what a month after an event is; nothing says whether a part month counts.
  Callable alternatives: `s 45(a) — the calendar months touched by a violation from`, `s 45(a) — the calendar months touched after the first, by a violation from`.
  Test: "s 45(a)" in `g6-tests-amount.l4` (15 March to 14 June 2027: 2, 4 and 3), and "ss 45 to 47 together" (20,800, 21,600, 21,200).
  Red: 13, 14.
- **F-START (trap T18): where the months of a violation after a warning are counted from.**
  Readings: from the day the breach began (taken); from the delivery of the warning.
  Text: s.54(a) says only that the continued breach is treated as a continuing violation for s.45(a).
  Callable alternatives: `s 54(a) — the months of a continuing violation counted from the day the breach began`, `s 54(a) — the months of a continuing violation counted from the delivery of`.
  Test: "s 54(a)" in `g6-tests-warning.l4` (10 February against 3 March 2027, to 2 June: 3 months against 2).
  Red: 15.
- **F-BASE (trap T18): whether the fiftieth is of the fixed amount as enacted or as updated.**
  Readings: of the amount as updated on the s.47(a) day, the additions being computed on it (taken); of the amount as enacted, the total then updated and rounded once.
  Text: s.45 adds a fiftieth of "the fixed sanction" and s.47(b) updates "the fixed sanction amounts"; the Law does not say which is "the fixed sanction" in s.45.
  Callable alternative: `s 45 to 47 — the financial sanction for the violation, with the additions computed on the amount as enacted`.
  Test: "ss 45 to 47 together" in `g6-tests-amount.l4` (item (3), individual, two months, updated on 1 June 2026: 5,293.6 against 5,290).
  Red: 20.
- **F-SAME (trap T17): "the same provision" in s.45(b).**
  Readings: the same provision of the Law that column A names at the end of the item (taken), so items (1) and (2) are both s.3(a) and items (5) and (6) both s.18(a); the same Third Schedule item.
  Text: «בתוך שנתיים מההפרה הקודמת של אותה הוראה» ("within two years of the previous violation of the same provision"); column A's heading is "the provision" and each item ends "contrary to the provisions of s.3(a)" (or 4, 13, 18(a), 31(2)).
  Callable alternative: `s 45(b) — the previous violation, read by Third Schedule item, makes the violation a repeat violation`.
  Test: "s 45(b)" in `g6-tests-amount.l4` (an item (1) violation followed by an item (2) violation: a repeat by provision, not by item).
  Red: 16.
- **F-FLOOR: what "the amounts fixed under this subchapter" are in s.46(a).**
  Readings: the fixed sanction plus the s.45 additions, because s.45 is in the same subchapter (ss.41-51) (taken); the column B amount alone, as updated.
  Callable alternatives: `s 46(a) — the amounts fixed under the subchapter for the violation, additions included`, `... column B only, as updated`.
  Test: "Fork F-FLOOR" in `g6-tests-amount.l4` (a sanction of 30,000 for a repeat item (5): below the floor taken, above the alternative).
  Red: 29.
- **F-ADD: the additions as a power or as a charge (s.42(b)(4) against s.45).**
  Readings: s.45 says the additions "shall be added" («ייווסף»), so they are automatic (taken); s.42(b)(4) tells the Commissioner to state in the notice «הסמכות להוסיף על סכום העיצום הכספי» ("the authority to add to the amount of the sanction"), which reads like a power.
  Callable alternative: `s 45 to 47 — the financial sanction for the violation, the additions being at the Commissioner's discretion`.
  Test: "Fork F-ADD" in `g6-tests-amount.l4`.
  Red: 31.
- **F-DAY: the order of the three limbs of s.47(a).**
  Readings: a stayed appeal displaces the other two (taken); the demand's day, or the notice's for a silent violator, displaces a stayed appeal.
  Text: «הוגש ערעור לבית המשפט לפי סעיף 56 ועוכב תשלומו של העיצום הכספי בידי הממונה או בידי בית המשפט, יהיה העיצום הכספי לפי סכומו המעודכן ביום ההחלטה בערעור» (the stayed appeal is the last limb and says the sanction "shall be at its updated amount on the day of the decision on the appeal").
  Callable alternative: `s 47(a) — the day on which the amount of the sanction is updated, the demand's day before the appeal's`.
  Test: "s 47(a)" in `g6-tests-amount.l4`.
  Red: 25.
- **F-ROUND: a half-way amount.**
  Readings: half up (taken); half to the even multiple.
  Text: «הסכום האמור יעוגל לסכום הקרוב שהוא מכפלה של 10 שקלים חדשים» ("to the nearest multiple of NIS 10"); at 5,085 both 5,080 and 5,090 are nearest.
  Callable alternative: `s 47(b) — the nearest multiple of NIS 10, a half going to the even multiple, to`.
  Test: "s 47(b)" in `g6-tests-amount.l4` (5,085 → 5,090 against 5,080).
  Red: 22.
- **F-CHAIN: each year's rounded amount as the next year's base.**
  Readings: each update is applied to the previous year's rounded amount (taken); the update is applied to the unrounded amount and rounded once at the end.
  Callable alternative: `s 47(b) — the amount of ... updated on ..., rounded once at the end, ...`.
  Test: "s 47(b)" in `g6-tests-amount.l4` (5,000 on 1 June 2027: 5,180 against 5,170).
  Red: 21.
- **F-FIRST: the first update day.**
  The Law says the amounts are updated "each 1 January" and does not say from which one.
  Taken as an INPUT (`the year of the first update day`); the tests use 2026, the first 1 January after the Law was published on 14 January 2025 (the date line of Sefer HaChukim 3349, p. 182).
  The alternative reading (the first 1 January after Chapter 6 commences) is the same function with the year the caller supplies.
  Test: "s 47(b)" in `g6-tests-amount.l4`.
  Red: 23 (the first update in 2028 against 2026).
- **F-ANCHOR: what the 30 days of s.53(a) run from.**
  Readings: the delivery of the warning, the event the sentence has just named (taken); the day of the breach the warning states.
  Text: «בתוך 30 ימים» ("within 30 days") has no anchor; s.43 and s.56(a) name delivery.
  Callable alternative: `s 53(a) — the last day to ask to cancel, counting from the day of the breach`.
  Test: "s 53(a)" in `g6-tests-warning.l4` (3 March against 10 February 2027: 2 April against 12 March).
  Red: 27.
- **F-CANCEL: a warning that was cancelled under s.53 and s.54.**
  Readings: a cancelled warning triggers nothing under s.54 (taken); s.54 applies to a warning delivered, cancelled or not.
  Text: s.54 speaks of a violator to whom a warning "was delivered"; s.53(c) lets the Commissioner cancel it.
  Callable alternative: `s 54(a) — ignoring any cancellation, a breach continued after`.
  Test: "s 54(a)" in `g6-tests-warning.l4`.
  Red: 19.
- **F-MUST54: whether s.54 keeps s.42(a)'s condition that the Commissioner intends to impose a sanction.**
  Readings: s.54(a) and (b) say «והממונה ימסור למפר הודעה» ("and the Commissioner shall deliver to the violator a notice of intention"), a duty whenever the section applies (taken); s.42(a) conditions the duty on «ובכוונתו להטיל» ("and he intends to impose").
  Callable alternative (a deontic): `s 54 — the Commissioner must give notice of intention after a warning, if he intends to impose a sanction`.
  Test: traced in `g6-tests-warning.l4`, "s 54(b)".
  No red assertion (a deontic).
- **F-APPEAL-DEEMED: the day "notice of the decision" counts as delivered, for a violator who made no representations (s.56(a)).**
  Readings: there is no decision on his case, only the notice treated as a demand; the day is the day it is treated as delivered (taken); the day the notice of intention was in fact delivered.
  Text: «על החלטה סופית» ("a final decision of the Commissioner") and «בתוך 45 ימים מיום שנמסרה הודעה על ההחלטה» ("within 45 days of the day notice of the decision was delivered").
  Callable alternative: `s 56(a) — the day notice of the decision counts as delivered to a violator who made no representations, taking the day the notice of intention was delivered`.
  Test: "s 56(a)" in `g6-tests-appeal-and-publication.l4`.
  Red: 28.
- **F-INTEREST: the unit of the s.49 input.**
  Readings: the caller supplies the shekel interest and the arrears fees accrued over the delay, as the Interest and Linkage Law computes them (taken: the encoding invents no mechanics); the caller supplies rates for the whole delay and the encoding adds simple interest on the sanction.
  Callable alternative: `s 49 — the amount owed, at simple rates, on a sanction of`.
  Test: "s 49" in `g6-tests-payment.l4`.
  Red: 30.
- **Not forks, readings taken without a callable alternative (stated so a reviewer can disagree):**
  (i) the two additions of s.45 are cumulative when a violation is both continuing and repeat (open question 2);
  (ii) the additions of s.45 are not themselves rounded to NIS 10 (open question 3);
  (iii) the refund of s.56(c) is a computed amount with no deontic, because the sentence names no payer (nouns request 3);
  (iv) `s 50(a)`'s plan needs at least one payment (the Law states only the maximum);
  (v) the previous violation's anchor in s.45(b) is its own date, not the day the sanction was imposed or the conviction obtained (open question 8).

## 3. Answer table: the headline scenarios

Money in new shekels.
The calendars of rest days and the index series in the tests are illustrative inputs; the sources give neither (section 8).

| scenario | answer | section | test |
| --- | --- | --- | --- |
| individual, item (1), as enacted | 20,000 | s.41(a), Third Schedule (1) | `g6-tests-schedule-three.l4` |
| individual, items (2) to (7) | 10,000; 5,000; 20,000; 20,000; 10,000; 3,000 | Third Schedule (2)-(7) | same |
| corporation, items (3), (5), (6), (7) | 10,000; 40,000; 20,000; 6,000 | Third Schedule | same |
| corporation, items (1), (2), (4) | named REFUSE (the dash), never 0 and never the individual amount | s.41(a), T14 | same |
| individual, item (5), repeat violation | 20,000 + 20,000 = 40,000 | s.45(b) | `g6-tests-amount.l4` |
| corporation, item (5), repeat violation | 40,000 + 40,000 = 80,000, the cap of s.41(b) exactly (T15) | s.45(b), s.41(b) | same |
| the same with six months of continuation | 84,800, above the cap | s.45(a), s.45(b), T15 | same |
| item (1), individual, 15 March to 14 June 2027 | 20,800 (2 months completed); 21,600 (4 calendar months touched); 21,200 (3 after the first) | s.45(a), F-MONTHS | same |
| index series 100.0, 101.7, 103.4 (invented): 20,000 | 20,340 after 1 January 2026; 20,680 after 1 January 2027 | s.47(b) | same |
| the same series: 5,000 | 5,090, then 5,180 (each year rounded); 5,170 if rounded once | s.47(b), F-ROUND, F-CHAIN | same |
| notice of intention delivered Wed 3 March 2027 | last day for representations Fri 2 April 2027; Sun 4 April if 2 and 3 April are days of rest | s.43 | `g6-tests-notice-and-hearing.l4` |
| the same notice, representations made on Wed 3 March 2027 itself | timely; no deemed demand (NOTHING); on the strict reading late, and deemed a demand on 2 April 2027 | s.43, s.44(d), F-ACTDAY | same |
| the same notice, an extension to 20 March 2027 for recorded reasons | the last day stays 2 April 2027 (4 April if 2 and 3 April are days of rest); taken as it is, 20 March | s.43, F-SHORTEN | same |
| a notice that omits the right to make representations and the s.44(d) consequence, the violator silent | no s.43 right; no deemed demand (NOTHING); on the other reading, deemed a demand on 2 April 2027 | s.42(b), s.43, s.44(d), F-NOTICE | same |
| payment demand delivered Wed 2 June 2027 | last day to pay Fri 2 July 2027; Sun 4 July if 2 and 3 July are days of rest | s.48 | `g6-tests-payment.l4` |
| violator who made no representations, notice 3 March 2027 | treated as a demand on 2 April 2027, last day to pay Sun 2 May 2027: 60 days after the notice (62 with 2 and 3 April days of rest) | s.44(d), s.48, T16 | same |
| the same violator: the update day of the amount | the day the notice was delivered, not the deemed demand's day (20 December 2026 gives the 2026 amount even though the demand is treated as delivered on 19 January 2027) | s.47(a) | `g6-tests-amount.l4` |
| previous sanctioned violation 16 March 2027, a further one | a repeat on 16 March 2029 (last day inside), not on 17 March | s.45(b) | same |
| a violation of 20 February 2029 after a sanction of 10 January 2027 and a warning of 3 March 2027 | not a repeat under s.45(b) (window ended 10 January 2029), a repeat under s.54(b) (window to 3 March 2029): T17 | s.45(b), s.54(b) | `g6-tests-warning.l4` |
| warning delivered 3 March 2027 | last day to ask for cancellation 2 April 2027 (4 April with 2 and 3 April days of rest); a further breach is a repeat until 3 March 2029, not on 4 March | s.53(a), s.54(b) | same |
| notice of the decision delivered Wed 2 June 2027 | last day to appeal Sat 17 July 2027; Sun 18 July if 16 and 17 July are days of rest | s.56(a) | `g6-tests-appeal-and-publication.l4` |
| late payment | owes the sanction plus shekel interest and arrears fees: REFUSE unless the caller supplies them (20,000 + 150 + 50 = 20,200) | s.49 | `g6-tests-payment.l4` |
| instalments | at most 12 monthly payments; 13 or 0 is outside the section | s.50(a) | same |
| refund after a successful appeal | 20,000 paid, sanction reduced to 15,000: 5,000 returned, plus shekel interest the caller supplies; never the arrears fees | s.56(c), T40 | `g6-tests-appeal-and-publication.l4` |
| publication | items (1), (2), (3), (5) always; (4) after a reduction; (6) for a corporation; a barred particular is not published | s.57(a), (d) | same |
| publication period | a corporation four years, an individual two: from 1 September 2027 to 1 September 2031 / 2029; from 29 February 2028 to 29 February 2032 / 28 February 2030 | s.57(e) | same |

## 4. Nouns requests for the INTEGRATOR

1. **`g6-nouns` records into `domain.l4`, if another group wants them.**
   `Third Schedule row`, `Provision contravened`, `Previous violation`, `Extension granted by the Commissioner`, `Notice of intention`, `Payment demand`, `Notice of a decision not to impose a sanction`, `Administrative warning`, `Ground for cancelling a warning`, `Decision on a request to cancel a warning`, `Decision on a financial sanction`.
   No other group needs them in this encoding; G7's commencement function does not.
2. **A derived function, not a field, for the provision a violation contravenes.**
   `Violation` carries `Listed violation`; the provision comes from `Third Schedule — the provision contravened by` (g6-schedule-three), which s.45(b) and s.54 need.
   If another group needs the provision, it should call that function rather than add a field that can disagree with the item.
3. **A `Party` for the State (`the State Treasury`).**
   s.51 and s.56(c) speak of the money going to and coming from the State; the Law names no actor for the refund ("shall be returned"), so no deontic is written for it.
   If the lead wants a deontic for the refund, `Party` needs `the State Treasury` (or the Ministry is taken as the payer, which is a modelling choice).
4. **A `Party` for the Attorney General is not needed**: s.52(a)'s approval is an input boolean.

## 5. Inputs consumed and functions exported

Standard inputs (PLAN section (c)), by their exact `GIVEN` names:

- IP9: domain's `Violation` and `Listed violation`.
  G6 consumes them in `s 41(a) — a financial sanction may be imposed for`, `s 41(a) — the amount the Third Schedule fixes for the violation`, `s 45 to 47 — the financial sanction for the violation`, `s 45(b) — the violation ... is a repeat violation, given`, `s 55 — a financial sanction may still be imposed for`.
- IP16: `Chapter 6 was in force on the day of the act` (BOOLEAN), a parameter of `s 41(a) — a financial sanction may be imposed for`, `s 41(a) — the Commissioner may impose the financial sanction for`, `s 42(a) — the Commissioner must give notice of intention` and `s 52(a) — the Commissioner may give an administrative warning instead of a financial sanction`.
  Later rules presuppose that the earlier acts of the chain happened lawfully.
- IP15: domain's `Calendar of rest days`, passed as the parameter `calendar` to every rule that counts a period.
- IP12: domain's `Price index reading`, in the list `the index readings` (the parameter `readings` in the s.47(b) helpers).
- IP14: the assumption that no order or regulation changes the Third Schedule or the cap and that no regulation under s.46(b) exists is carried as follows: the Schedule as enacted is the only vintage modelled; the content of an order under s.41(b) is an input of the Minister's rule; a floor that would rely on s.46(b) regulations is a named `REFUSE` unless the caller supplies the rate.
- IP1, IP3, IP4, IP10 are not consumed directly: a `Violation` exists only if G1, G3 or G5 decided that the violation occurred (that is where the licence, its kind, the job kind and the lawful demand are tested), so they are already inside the record G6 takes.

Inputs invented by G6 (named in the rules that read them): the Commissioner's grounds, intention, authorisation and findings (`the Commissioner has reasonable grounds to think the person breached a listed provision`, `the Commissioner intends to impose a financial sanction`, `the Commissioner holds the Minister's authorisation for Chapter 6`, `the Commissioner finds special reasons for an extension`), the notice, demand, warning and extension records of `g6-nouns`, `the number of months for which the violation continued`, `the violation is a repeat violation`, `the day on which the amount is updated`, `the year of the first update day`, `the shekel interest accrued over the delay`, `the arrears fees accrued over the delay`, and the publication facts.

Functions exported (`@export`, with `@desc` on every parameter), exact names:

- `s 41(a) — the amount the Third Schedule fixes for the violation`
- `s 45 to 47 — the financial sanction for the violation`
- `s 47(b) — the amount of` ... `updated on` ... `, the first update being in` ... (the form with the first update year; the rounded-once variant is not exported)
- `s 45(a) — the whole months a violation continued from` ... `to` ...
- `s 45(b) — the violation` ... `is a repeat violation, given` ...
- `s 43 — the last day for representations`
- `s 48 — the last day of the 30 days from the delivery of the payment demand`
- `s 53(a), (b) — the last day to ask to cancel` ...
- `s 56(a) — the last day of the 45 days from` ...
- `s 57(e) — the last day of the publication period that began on` ...

Toolchain note on the exports, for whoever deploys them: `l4 batch` with `-e` on the exported function works for `g6-schedule-three.l4` (which imports no time module: item (1), an individual, gives 20000; a corporation at item (1) gives the named refusal; item (5) gives 40000), but fails for every module that imports `il-interpretation-time` (`g6-notice-and-hearing.l4`, `g6-amount.l4` and the others): the generated `<module>.batch1.l4` reports "multiple definitions" of the time module's mixfix names, each listed twice as predefined, and no row is evaluated.
`l4 run`, `l4 check` and every test here are unaffected, and the failure is not specific to G6: a probe module that does nothing but import the time module and export one function calling `s 10(a) — the last day of a period of` fails the same way (`work/g6/probe/pb.l4`).
It was not investigated further; the effect is that a deployment of the date functions through `l4 batch` or a service built the same way may need the time module flattened into the importing file or the tool fixed.

Other functions the INTEGRATOR will wire (not exported):
`s 41(a) — a financial sanction may be imposed for`, `s 44 — the day the payment demand is delivered or treated as delivered`, `s 47(a) — the day on which the amount of the sanction is updated`, `s 55 — a financial sanction may still be imposed for`, `s 57(a) — the numbers of the items the Law requires where`, and the regulative rules (each returns a `DEONTIC Party` over its module's `Act under ...` type; the clock convention of each is in its module header).

A wiring recipe: G1, G3 and G5 give a `Violation`; G7 gives `Chapter 6 was in force on the day of the act`; `s 41(a) — a financial sanction may be imposed for` answers whether the Commissioner may impose; `s 42(a)` starts the notice; `s 43` and `s 44` date the window and the demand; `s 47(a)` gives the update day; `s 45 to 47 — the financial sanction for the violation` gives the amount; `s 48` and `s 56(a)` date the payment and the appeal.

## 6. Contradictions in the source

Found by a separate pass over my own modules after encoding, reading ss.41-57 against each other and against ss.3, 63 and the Third Schedule.
Each gives the provisions, the case that discriminates, and the two readings (both callable unless said).
Items 1, 3 (first two readings), 4, 5 (first case), 7 and 8 confirm the survey's traps (T15 to T19 and the note on P33) against the encoding; items 2, 6, 9 and 10, the third reading in item 3 and the second case in item 5 are not in the survey's list and were found in this pass.

1. **s.41(b) against s.45 and s.47(b) (trap T15).**
   A fixed cap of 40,000 / 80,000 on what an order sets in column B, while s.45(b) can double an item and s.45(a) add a fiftieth a month, and s.47(b) indexes every fixed amount each year and the cap is not indexed.
   Case: a corporation, item (5), repeat, one month: 40,000 + 800 + 40,000 = 80,800, above the cap of 80,000; and an item whose indexed amount passes the cap could not be re-stated by an order.
   Readings: F-CAP.
2. **s.42(b)(4) against s.45: "authority to add" against "shall be added".**
   Case: a continuing violation where the Commissioner decides not to add.
   Readings: F-ADD.
3. **s.44(d) against s.47(a): "the said date".**
   Case: a violator who stays silent; the notice is delivered 3 March 2027.
   Readings: F-DEEMED (three; the third makes s.47(a)'s special rule for a silent violator redundant and makes the two 30-day periods end together).
4. **s.42(b)(2) and s.44(b)(1) against s.48: who fixes the period for payment.**
   Case: a demand that states 45 days.
   Readings: F-PERIOD.
5. **s.45(b) against s.54(b): two definitions of "repeat violation" with different anchors (trap T17).**
   Case: a violation on 20 February 2029, after a sanctioned violation on 10 January 2027 and a warning on 3 March 2027, both for s.3(a): a repeat under s.54(b) only.
   Readings: both functions are callable side by side (`s 45(b) — the violation ... is a repeat violation, given` and `s 54(b) — the further violation after ...`); the test is "Trap T17" in `g6-tests-warning.l4`.
   A second case: a previous violation that ended in a warning only is not "a violation for which a sanction was imposed or a conviction obtained", so it never makes a repeat under s.45(b), but s.54(b) deems one.
6. **s.54(a) against s.42(a): "shall give" against "intends".**
   Readings: F-MUST54.
7. **s.46(b) against s.63(b) (trap T19, G7's).**
   s.63(b) starts Chapter 6 at the later of 18 months from the commencement day and the entry into force of regulations under s.46, while s.46(b) says the Minister "may" make them.
   If none is made the later date does not exist and Chapter 6 may never commence; the same text says in s.46(a) that the Commissioner may go below the fixed amounts only "under (b)", which reads as if the regulations were optional.
   Case: a violation on 1 February 2027, with no regulations under s.46; 16 January 2027 is 18 months after 16 July 2025, the day the note beside s.63 gives for the commencement of the s.59 regulations, which on my reading is the commencement day of s.63(a)(1) (G7's reading to confirm).
   G6 does not decide it: it takes `Chapter 6 was in force on the day of the act`; the tests give both values (`g6-tests-schedule-three.l4`, "s 41(a)").
8. **s.53(a) against s.43 and s.56(a): the one period with no anchor.**
   Readings: F-ANCHOR.
9. **s.56(a) against s.44(d): an appeal lies from "a final decision", and a silent violator has none.**
   Readings: F-APPEAL-DEEMED.
10. **s.47(a) against s.47(b) and s.46(a): "the fixed amounts" are both the amounts that are updated and the amounts below which no sanction may be imposed.**
    Readings: F-FLOOR, F-BASE.
11. **Wikisource against the gazette.**
    None in this scope: every number of ss.41-57 and of the Third Schedule table was read on the gazette page images (pp. 193-197, 205) and agrees with `inputs/law.wiki`.

## 7. Open questions for a domain expert

1. What does a dash in the corporation column mean at items (1), (2) and (4): no sanction, or a figure left out (F-DASH)?
2. Are the s.45 additions cumulative when a violation is both continuing and repeat, and automatic (F-ADD)?
3. Is an addition of s.45 itself rounded to NIS 10 (the Law rounds "the said amount" of s.47(b))?
4. From which 1 January are the amounts updated (F-FIRST), and is a half-way amount rounded up (F-ROUND)?
5. How are "the months in which the violation continues" counted (F-MONTHS, F-START)?
6. What is "the said date" of s.44(d) (F-DEEMED)?
7. Does IL s.10(c) apply to the s.45(b) and s.54(b) windows and to the s.57(e) publication period (F-WINDOW, F-VALID)?
8. Is the two years of s.45(b) counted from the previous violation's own day (taken) or from the day the sanction was imposed or the conviction obtained?
9. Does a notice that omits what s.42(b) lists start the 30 days, give the right, and count as a payment demand when the violator is silent (F-NOTICE)?
10. Does the update of the amounts under s.47(b) wait for the Commissioner's notice in Reshumot under s.47(c), or are they independent (taken: independent)?
11. Who refunds under s.56(c), and is there a time within which the refund must be made?
12. For one act that is several breaches, which breach carries the single sanction (s.55)?
13. May the Commissioner extend the s.43 or s.53 period after it has run?
14. Which court hears an appeal of a decision that is not a final decision of the Commissioner under Chapter 6 (trap T39, s.62)?
15. Is an act on the day a notice, demand, warning or decision is delivered within the period "within 30 (or 45) days" of it (F-ACTDAY), and is a publication on the day of publication inside the s.57(e) period?
16. May the Commissioner's "extension" end the period earlier than the 30 days (F-SHORTEN)?

## 8. What the sources do not answer

Each is an input or a named `REFUSE` in the encoding; none gets a default.

- The Interest and Linkage Law's rates and mechanics (s.49, s.56(c)): the amount of shekel interest and arrears fees is an input, a named `REFUSE` when not supplied.
- Any regulation under s.46(b), any order under s.41(b) or s.57(f): none is in the sources; the Schedule as enacted is the only vintage.
- The consumer price index readings and the first update day (s.47(b)): the readings in the tests are invented and say so.
- The calendar of days of rest, recess or holiday for any year: an input; the calendars in the tests name only the days that matter.
- The identity of the Commissioner and the Minister's authorisation of him (`the Commissioner holds the Minister's authorisation for Chapter 6`), the Commissioner's reasonable grounds, intention, special reasons and decisions: inputs.
- The Freedom of Information Law s.9 (s.57(d)): whether a particular is barred or may be omitted is an input.
- The Fines, Fees and Expenses Collection Centre Law (s.51): out of scope.
- How a document is delivered (ss.42, 44, 52, 56): the day of delivery is an input.
- The commencement of Chapter 6 (s.63(b)): the flag `Chapter 6 was in force on the day of the act` is G7's.
- The text of any procedure the Commissioner directs under s.52(a): its circumstances are an input.
