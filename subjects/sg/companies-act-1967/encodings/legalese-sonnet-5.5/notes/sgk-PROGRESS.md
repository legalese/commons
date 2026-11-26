# PROGRESS (sgk)

Part agent sgk: Companies Act 1967 (Singapore), lines 11039-11492 (Part 4 Division 8, ss 131-141) and 21886-22626 (Parts 8, 8A, 9: ss 217-227X repealed, ss 228-246).
State: finished on 2026-11-18.
Everything below was checked at the last edit of this file; the numbers are those `check.sh` printed (see NOTES.md, "What `check.sh` prints").

## Files

- Layer 1 (seven modules, 199 functions): `sgk-div8-application.l4` (ss 139 to 141), `sgk-div8-registration.l4` (ss 131 to 133), `sgk-div8-register.l4` (ss 134 to 138), `sgk-part9-declared.l4` (ss 228 to 231), `sgk-part9-inspectors.l4` (ss 232 to 236; s 234 repealed), `sgk-part9-consequences.l4` (ss 237 to 242), `sgk-part9-ownership.l4` (ss 243 to 246).
- Tests: `sgk-tests-<module>.l4` for each, 626 assertions and 83 traces.
- Layer 2: `sgk-seat.l4` (93 questions) and `sgk-cases-seat.l4` (280 assertions).
- `NOTES.md` (every section the brief names), `NEEDS-CORE.md`, this file.
- Not shipped: `../../../work/` (templates in `work/src/*.l4` with %%Q/%%R/%%INC directives, `expand.py`, `qrun.sh`, `tracecheck.py`, `quotecheck.py`, and the generators for the coverage, jural, marginal and seat tables).

## Results

- `check.sh`: 24 modules, 0 errors, 906 satisfied, 0 failed, 0 refused; the main build 1.6.109 gives the same four counts on every module; exit 0.
- `srcrefs.py check --refs` and `--strict`: 853 src lines, 106 runs, 196 locators, 0 problems.
- `tracecheck.py`: 83 traces, every `-- EXPECT` matched on both stable builds.
- `quotecheck.py` over every `sgk-*.l4`: 0 quoted spans not found in the text.

## Decisions taken (with the text that licenses each)

All 34 forks are in NOTES.md, "Fork register (sgk)", each with the text that licenses it and the other reading.
The ones that shaped the most code:

- "within 30 days after" (s 131(1), (5), (6), s 133(1)) is a deadline: a lodging not later than the 30th day after the event, including one on the day of the event itself, is in time; F-K4.
- s 139 "extended by 7 days or such further periods": 7 days plus any further days the Registrar has allowed; F-K1.
- s 131(1) and (6) name no bearer ("there must be lodged"); the company is taken because s 132(1) puts the default on the company and its officers; F-K6.
- A duty or prohibition whose "if", "where" or "upon" gate is unmet answers JUST FALSE; F-K5.
- A "may" gated by "where", "when" or "upon" answers JUST FALSE (11 sites), and the four "on application" and "with the consent" gates answer NOTHING; F-K7, F-K13, F-K15, F-K21, F-K24.
- An unmet element of an offence answers JUST FALSE (9 sites); F-K10.
- A "may" or "power" function with an "if" gate answers NOTHING when the gate fails (8 sites); F-K18.
- The ten regulative rules derived from an offence or an entitlement carry a trailing `-- fork F-K34` on their MEANS line.

## Names unified before filing

One fact has one input name across the modules and the seat: the officer in default (`the person is an officer of the company who is in default, as section 408(3) uses the phrase`), the officer or agent of a corporation under investigation, the foreign company, and the s 6 relatedness of the other corporation (the same name in s 235 and s 236(1)).
The seat checks that no input name carries two `@desc`.

## Left for the lead

- `NEEDS-CORE.md`: an `Inspector` constructor and an officer-or-agent constructor in the core `Party`; `s 231 party` and `s 231 act` can then be re-pointed.
- The marginal-readings tables in NOTES.md are for a lawyer; 97 "no" branches and 83 "not covered" branches rest on the brief's two status-quo readings.
