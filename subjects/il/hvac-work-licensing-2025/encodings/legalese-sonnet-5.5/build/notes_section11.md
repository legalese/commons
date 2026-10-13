## 11. Date correction, 2026-10-13

Written by the encoder (the same Sonnet 5.5 agent, resumed), after the launching session asked for the date logic to be corrected against Interpretation Law 5741-1981 s 10, using the module the Interpretation row now provides.
Section 10 above is the launching session's and is unchanged; its numbers are the as-run numbers.
Everything here is the state after the correction.

### 11.1 What was asked, and what I did

- The experiment was over, so the cleanroom rule of the original brief was lifted for this pass, for the paths the task named.
- I vendored `il-interpretation-time.l4`, the Interpretation row's module, into this directory, byte-identical (checked with `cmp`; sha256 `@@VSHA@@`); I did not edit it.
It is imported as ``IMPORT `il-interpretation-time` `` by the modules that count a period.
No name in it clashes with a name in this row (37 heads compared with 236; `l4 check` is clean).
- Before changing anything I made the build scripts read `INPUTS` and `DEPOSIT` from the environment (`build/build.py`, `build/verify_hebrew.py`, `build/make_notes.py`) and confirmed that the 13 templates regenerate the 13 committed `.l4` files byte-for-byte, and that `check.sh` reproduced the as-run table (281 satisfied, 7 expected failures).
- The Interpretation Law is taken to govern every period here (its s 1 gate, "if there is no other provision on the matter and nothing in the matter or its context is inconsistent", is the caller's question in the module and is taken as met: nothing in the Law or the regulations says how a period is counted); this premise is on the page in F-N1.
- I decided every expected value from the statute first, using a separate Python reading of s 10(a), (b) and (c) (reading A of (c), the extension reading the module takes; filed as `build/date-oracle.py`) and the weekdays of the dates, and only then changed the modules and ran the tests.
The oracle is a second reading in another language: it catches slips in the L4, not an error of reading, and it shares reading A with the module.

Section 10's remark that the build scripts "do not run from here without recreating that layout" is superseded, and section 10 is left as written: `build/build.py`, `build/verify_hebrew.py` and `build/make_notes.py` now read `INPUTS` (the directory of source files, which is not filed with the row) and `DEPOSIT` (default: this directory) from the environment, and `build/make_notes.py` splices section 10 back in verbatim from `build/section10.md`.
To regenerate: `INPUTS=<inputs directory> python3 -I build/build.py`, then `python3 -I build/make_notes.py`.

### 11.2 What changed, module by module

- `hvac-fees-regs.l4`: reg 5's seven days are `s 10(a) — the last day of a period of 7 days from` the publication (16 July 2025, unchanged); the amendment's commencement is no longer a refusal but the day of publication under Interpretation Ordinance s 17 (4 May 2026; F-N1); `the vintage in force on` selects the amended vintage from that day; a function applies s 10(c) to reg 5 for a reader who wants it (F-X3).
- `hvac-law-s63-commencement.l4`: the three-month period (reading B), reading A's three months, the 18 months of (a)(2) and of (b) go through `s 10 — … months from the day`; "if s 10(c) applied" versions of the Commencement Day and of the commencement per class take a calendar (F-X3, F-C3).
- `hvac-law-s6-second-schedule.l4`: the three-year sunset is `s 10 — … 3 years from the day` the Commencement Day, tested with `s 8 — the date … is up to and including`; an "if s 10(c) applied" version (F-X2).
- `hvac-law-s8-validity.l4`: the five-year limb is `s 10(b)`; validity is tested with s 8's "up to and including"; the "31 March" limb is a named date and is not a counted period; an "if s 10(c) applied" version of the five-year limb and of the first period (F-X2, F-V4).
- `hvac-law-s7-s9-exemption-and-temporary-licence.l4`: s 9's one-year ceiling is `s 10`, tested with s 8; the three-period ceiling is three one-year periods chained (F-V5); the six-year look-back is left as it was and says so (F-B1).
- `hvac-law-s16-s17-duties-of-licensee.l4`: s 16's thirty days and s 17(c)'s three months take a calendar of rest days (s 10(a), (c) and s 10(b), (c)); the old names without a calendar remain and mean "no rest-day input"; the s 16 deontic's `WITHIN` is computed from the last day (F-X1, F-X4); s 17(a)'s last-year window is left as it was and says so (F-B1).
- Tests: `hvac-tests-calendars.l4` is new (Saturdays; Fridays and Saturdays; Sundays, as an illustration only; 15 positive controls on their weekdays); `hvac-tests-fees.l4`, `hvac-tests-law.l4` and `hvac-tests-red.l4` were extended; `check.sh` now expects 13 failures in the red file.
- `encoding.json`, `SOURCE-LICENSE.md` and sections 1 to 9 of this file were updated; section 10 was spliced back in verbatim (its text is `build/section10.md`, compared with `git show HEAD` before the first run).

### 11.3 Expectations that moved

Two, both caused by the one change that goes beyond s 10 (Interpretation Ordinance s 17, fork F-N1).

| assertion | as run | now | statute |
| --- | --- | --- | --- |
| `the day the 5786 amendment commenced` | refused: "12383 states no commencement date, so the sources do not say when the 5786 amendment came into force" | 4 May 2026 | Interpretation Ordinance s 17: regulations of legislative effect bind from the day of publication if there is no other provision; 12383 was published on 4 May 2026 |
| `the vintage in force on` 4 May 2026 | refused | `As amended` | the same |

No other expectation moved.
Of the 281 assertions satisfied in the as-run state, 279 pass unchanged (70 in the fees tests, 187 in the law tests, 22 in the SimpLEX tests), the 7 expected failures still fail for the same reasons, and the two above changed.
That is what I expected: the first encoding had already taken the readings s 10 states.
These values are unchanged because I checked them against the statute and they agree: reg 5 (16 July 2025), the Commencement Day (16 July 2025), 18 months on (16 January 2027), the three-year sunset (16 July 2028), s 8's first validity period (5 years from 2025-01-15 ends 2030-01-15; a grant after 31 March ends 31 March of the fifth year), s 9's year and its three-period ceiling, s 16's last day (30 days from 1 March 2026 end on 31 March) and s 17(c)'s ceiling (31 March 2030 plus three months is 30 June 2030).

### 11.4 Assertions added

- `hvac-tests-calendars.l4`: 15 (controls on the weekdays the tests lean on).
- `hvac-tests-fees.l4`: 4 added to the 72 (reg 5 under two calendars; 31 December 2026 is `As amended`; the fee payable on 10 May 2026 refuses because of reg 3), and the 2 above rewritten.
- `hvac-tests-law.l4`: 47 added to the 187, in the last section: the statutory counting with no rest-day input, s 16 and s 17(c) under three calendars (including a Friday nominal last day that only the Friday-and-Saturday calendar moves, and a Saturday one that both move), the "told in time" and "in breach" consequences, three new `#TRACE`s on s 16, and for each kind that (c) is not applied to: s 8, s 9, the sunset and s 63, the unchanged answer and the alternative's answer.
- `hvac-tests-red.l4`: 6 added (F8 to F13, section 7).

### 11.5 Forks added or revised

- Settled by the statute, no longer forks: F-D3 (the last day of three years), F-D4 (counting "from" a day), and the counting half of F-R5.
- Added: F-B1 (backward windows are not covered by s 10), F-C3 (a commencement "N from" an event falls on the last day of the period), F-N1 (Ordinance s 17 for the amendment), F-V4 (a licence is valid from the day it is given), F-V5 (s 9(b)'s renewal periods run back to back), F-X1 (s 10(c) applied to deadlines: s 16, s 17(c)), F-X2 (not applied to periods of validity: s 8, s 9, the sunset), F-X3 (not applied to commencement days: s 63, reg 5), F-X4 (several days of rest in a row: the module's reading A, left OPEN by the Interpretation row).
- Revised by a sentence: F-C1 (the three months are s 10(b)), F-T5 and F-V3 (backward windows).
- The text of (c) is unqualified ("ימי תקופה"), so F-X1 to F-X3 are readings by purpose, and each has its alternative in the code and in a test: a reader who applies (c) to every period uses the "if s 10(c) applied" functions.

### 11.6 What `check.sh` prints now

```text
@@CHECK@@
```

The same run, read for diagnostics and not for the exit code: no module prints a warning, and the only errors are the 13 failed assertions of `hvac-tests-red.l4`, which `check.sh` expects.
The @@NTRACE@@ `#TRACE` directives (3 new) were run and read.
Counts of `#ASSERT` directives: @@N_CAL@@ in `hvac-tests-calendars.l4`, @@N_FEES@@ in `hvac-tests-fees.l4`, @@N_LAW@@ in `hvac-tests-law.l4`, @@N_SIMPLEX@@ in `hvac-tests-simplex.l4`, @@N_RED@@ in `hvac-tests-red.l4`.

### 11.7 How the correction was checked

Ten mutations were applied one at a time to a scratch copy of the modules (outside this directory), and the four test files were run.
Failures are counted once each.

| mutation | caught by |
| --- | --- |
| s 16 ignores the calendar of rest days | 5 law assertions |
| s 17(c) ignores the calendar | 4 law assertions |
| s 8's "if s 10(c) applied" version ignores the calendar | 3 law assertions |
| s 63's 18 months become 17 | 3 law assertions |
| the Second Schedule sunset ends one day early | 3 law assertions; and F8 of the red file then passes (12 failures instead of 13) |
| the Ordinance s 17 default is replaced by another date | 2 fees assertions |
| reg 5 counts eight days | 19 law and 4 fees assertions |
| s 9's ceiling chains two periods, not three | 3 law assertions |
| the sunset's "if s 10(c) applied" version ignores the calendar | 1 law assertion |
| the s 16 deontic's `WITHIN` is fixed at 30 | no assertion: that rule is exercised only by `#TRACE`, which `check.sh` does not count; the trace of day 31 under Saturday-as-rest flipped from FULFILLED to BREACH, so the traces do discriminate, and they are read, not counted |

That last row is a limit worth stating: a deontic cannot be compared in an `#ASSERT`, so the s 16 `WITHIN` that carries s 10(c) is checked by reading three traces and not by a count.
The Hebrew-phrase check (`build/verify_hebrew.py`) was rerun after the change: it now also matches this row's quotations of Interpretation Law s 10 and Ordinance s 17 against the comments of the vendored module (section 9), and its unmatched phrases are the same classes as before (56 against 55: the new one is the Wikisource note on reg 5, now split over two comment lines).

### 11.8 Still open

- Whether Interpretation Ordinance s 17 is as the unofficial text has it, and that no other provision fixes when regulations under the Law commence (Q5).
Only s 10 of the Law has been compared with the enacted gazette; if the Ordinance's text differs, `the day the 5786 amendment commenced` goes back to a refusal in one function.
- Whether the fee regulations are regulations of legislative effect, which Ordinance s 17 speaks of (premise of F-N1).
- Whether (c) reaches validity periods, ceilings and commencement days (Q11; a validity period is a period in which a right is exercised, which is the task's own wording, so if one counts F-X2 flips), and what it does when several days of rest end a period (Q12, F-X4: the Interpretation row's F3 is open there too).
- Whether a commencement "N days from" publication is the last day of the period or the day after it (Q13, F-C3).
- Everything section 8 already listed that this correction did not touch, and the same limit as before: the assertions share one reader's reading of the sources, and no independent test pass was run.
- The calendars the tests supply are illustrations; which days are days of rest "על פי חיקוק" for a given period is not in the sources.

### 11.9 What I opened that the original brief forbade

Allowed for this pass, reported anyway.
In the Interpretation row (`.../subjects/il/interpretation-law-1981/encodings/legalese-sonnet-5.5/`): `il-interpretation-time.l4` (all of it), `NOTES.md` sections 0, 3 to 7, and the first 80 lines of `tests-worked-cases.l4` (to see how it defines its calendars).
I did not open its other files.
No other row of this subject was opened.
While I worked the harness printed a change notice for another row's `encoding.json` (`legalese-michael`), with some of its content, into my session; I did not open that file, and nothing in this correction depends on it.
