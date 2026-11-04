# NOTES (snap5): Food and Nutrition Act of 2008, 7 U.S.C. ch. 51, sections 2025, 2026a and 2028

Part agent `snap5`, run `iaw-snap5`.
Lines 1911-2391, 2656-2697 and 2731-2804 of `usc07-ch51.txt`: section 2025 (administrative cost-sharing and quality control), section 2026a (healthy fluid milk incentives projects) and section 2028 (consolidated block grants for Puerto Rico and American Samoa).

**Status, 2026-11-04.**
Written with the stable build `l4` 1.6.98 (main, 7689b0d, 2026-10-19).
How each claim below was checked is named where the claim is made: `check.sh` (below), `srcrefs.py check --refs` and `--strict` (0 problems on every layer-1 module and test), a quote verifier (every quoted piece found in the text), a kind-comment lint (0 unflagged `JUST FALSE` or `NOTHING` branches), and the coverage audit (460 units, 0 unmapped, 0 lines in no row).
The documents in this folder are generated, where they are tables, from the modules by scripts kept outside the deposit; the tables cannot be older than the modules they were generated from, but they were generated once, at the end, and a later edit of a module is not carried into them.

**The source is a converter's rendering.**
`usc07-ch51.txt` is a plain-text rendering made by a one-off converter script from the Office of the Law Revision Counsel's USLM XML (release point Public Law 119-121, as at 2026-10-09; see `usc07-ch51.meta.json`).
It is not the official text, and nothing in this encoding is verified against the official text.
Every quotation in the modules is checked against that rendering, line by line, and against nothing else.

## What is in this folder

| file | what it is |
| --- | --- |
| `snap5-s2025-ab.l4`, `snap5-tests-s2025-ab.l4` | section 2025(a) administrative costs and retention, (b) work supplementation or support programs |
| `snap5-s2025-c1.l4`, `snap5-tests-s2025-c1.l4` | section 2025(c)(1) quality control system, liability amount, at-risk amount, corrective action |
| `snap5-s2025-c2.l4`, `snap5-tests-s2025-c2.l4` | section 2025(c)(2) to (c)(9) error rates, exclusions, national performance measure, review, the 2025(c)(8) timetable, good cause |
| `snap5-s2025-dfij.l4`, `snap5-tests-s2025-dfij.l4` | section 2025(d) performance bonus payments, (e) social security numbers, (f) legal fees, (i) error-prone profiles, (j) training materials |
| `snap5-s2025-gh.l4`, `snap5-tests-s2025-gh.l4` | section 2025(g) computerization, (h)(1)(A) to (E) and (h)(2) to (5) employment and training funding and oversight |
| `snap5-s2025-hf.l4`, `snap5-tests-s2025-hf.l4` | section 2025(h)(1)(F) pilot projects |
| `snap5-s2025-k.l4`, `snap5-tests-s2025-k.l4` | section 2025(k) reductions in payments for administrative costs |
| `snap5-s2025-duties.l4`, `snap5-tests-s2025-duties.l4` | the twelve regulative rules (PARTY / MUST / MAY / WITHIN / HENCE / LEST) of sections 2025(c)(8), 2025(k) and 2028(b), with 27 `#TRACE` runs |
| `snap5-s2026a.l4`, `snap5-tests-s2026a.l4` | section 2026a |
| `snap5-s2028.l4`, `snap5-tests-s2028.l4` | section 2028 |
| `snap5-seat.l4`, `snap5-cases-seat.l4` | layer 2: the seat, 17 questions, 82 cases |
| `NOTES.md`, `PROGRESS.md`, `SEAMS.md`, `NEEDS-CORE.md` | documents |
| `snap-core.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` | supplied; not edited |

Assertions satisfied on the last run, per file: `snap5-tests-s2025-ab.l4` 84; `snap5-tests-s2025-c1.l4` 75; `snap5-tests-s2025-c2.l4` 110; `snap5-tests-s2025-dfij.l4` 85; `snap5-tests-s2025-duties.l4` 47; `snap5-tests-s2025-gh.l4` 187; `snap5-tests-s2025-hf.l4` 180; `snap5-tests-s2025-k.l4` 88; `snap5-tests-s2026a.l4` 54; `snap5-tests-s2028.l4` 149; `snap5-cases-seat.l4` 82; total 1141.
Every layer-1 function names its section (`s 2025(c)(8)(D) ...`), cites its source lines with a `@ref` and a `-- src:` quotation expanded mechanically from the text, and has a test that exercises each branch and each side of every threshold.
Money is a `NUMBER` of dollars; a share is a fraction (20 percent is 0.20); dates are `Date day month year`.

## Where PLAN.md and the brief differ (the brief governs)

1. **How a borrowed term is asked.**
   PLAN.md section 4 asks a term the keel's definitions module answers as a `MAYBE BOOLEAN` input named exactly like the keel's function (`s 2012(n) the area is a reservation`).
   The brief asks a borrowed term or fact as a plain input.
   I took plain `BOOLEAN`, `NUMBER` and `DATE` facts for everything borrowed (for example `the State agency administers the program on all or part of an Indian reservation under section 2020(d)`, and the one place the plan expects `s 2012(l)`, the list of target groups at line 2134, which includes homeless individuals).
   The seams the plan names keep the plan's `s 20NN <what you ask>` name and type: `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between the two dates` (`NUMBER`, used by `s 2025(c)(1)(A)(ii)(II)` and `s 2028(a)(2)(A)`), `s 2015(o)(2)`, `(3)`, `(4)` and `(6)` (`MAYBE BOOLEAN`, used by `s 2025(h)(1)(E)`), and `s 2027(a) appropriations are available` (`MAYBE BOOLEAN`, used by `s 2028(a)(2)(A)`).
   Where the text hands a decision to the Secretary ("the Secretary determines that ..."), the input is a `MAYBE BOOLEAN`, so that an undecided determination stays `NOTHING` and is never turned into `FALSE`.
2. **The core.**
   The brief says layer 1 imports `snap-core.l4`.
   Only `snap5-s2025-ab.l4` does, for the core's `Claim` (the amount a State may keep of a claim it recovers, `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars`).
   Nothing else in these three sections fits a core type: `Area` and `Kind of place` have no value for Puerto Rico or American Samoa; `Party` has no constructor for the chief executive officer of a State, an administrative law judge, the Departmental Appeals Board, the Commonwealth or American Samoa, and a `DEONTIC` rule takes one actor type; `Individual`, `Household`, `Benefit` and `Kind of decision` describe a household's case, and these sections are about what a State agency owes the Secretary, what the Secretary owes a State agency, and what a Commonwealth must report.
   What was missing is in `NEEDS-CORE.md`.
3. **The seat layer, the FALSE and NOTHING rule and the Hohfeld table** are in the brief and not in the keel's plan; the brief's text is followed.
4. **Regulative rules.**
   The brief asks for regulative rules where a provision imposes a duty on a named party with a time limit; the stable binary cannot assert a `#TRACE`, so each regulative rule has a decision-function twin that carries the assertions (see "What the stable binary does not accept").
5. **One small function per cited unit.**
   The plan advises that a section others cite (it names section 2025 as asked by four or more parts) give each cited subsection its own small function named `s 2025(x) ...`.
   The modules have one function per paragraph, subparagraph or sentence of the text they encode (268 in all, the list is `SEAMS.md`, ANSWERS), so that any cited unit has a function to wire to; which units other parts cite is the lead's to check, because the other parts' bodies are not visible from here.

## Coverage (snap5)

**Audit** (`work/tools/coverage.py`, run at the end). Text units counted by listing every labelled line of the three ranges (`units.py`): 460. Rows in the table: 460. Units with no disposition: 0. In the final run the audit found no unit without a row and no line in no row, so the rows before the audit and after it are both 460 (the table is generated from the unit listing, so the two agree by construction; the audit has two real checks, the count of units without a mapping, which must be 0, and the count of non-blank lines that fall in no row, which must also be 0). Non-blank lines in the ranges: 594; lines that fall in no row: 0.

**Counts per disposition** (rows): encoded 371; fork 15; inert, reason 1 (not operative) 64; inert, reason 2 (machinery) 10; inert, reason 3 (repealed or blank in this text) 0; total 460.

Each row is one labelled unit of the text (a section, subsection, paragraph, subparagraph, clause, subclause, item, or source credit), in the order of the text.
The disposition is exactly one of `encoded`, `fork F-n` (the text can be read two or more ways with different outcomes; the row points at the register entry below and at the rule that encodes the reading taken), or `inert (n ...)` for the brief's reasons 1 (not operative), 2 (machinery) and 3 (text shown repealed or blank; none in these ranges).
A child unit that the function of its parent encodes says "in the functions of" its parent; a lead-in whose subunits carry the rule says so and points at them.
There is no `out-of-scope` and no `deferred` row.

| lines | unit | disposition | where it is encoded |
| --- | --- | --- | --- |
| 1911-1911 | s 2025 | inert (1 not operative) | the section heading |
| 1912-1913 | s 2025(a) | fork F-3 | retention proviso; `s 2025(a) the share of administrative costs the Secretary is authorized to pay`; `s 2025(a) the amount the Secretary is authorized to pay before any reduction under subsection (k)`; `s 2025(a) the cost is an administrative cost the Secretary is authorized to pay a share of`; `s 2025(a) the additional amount the Secretary may pay a State agency for a reservation or a Native village`; `s 2025(a) the share of recovered or collected funds the Secretary may permit the State to retain`; `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars`; `s 2025(a) the official may receive or benefit from the revenues retained by the State` (snap5-s2025-ab) |
| 1914-1914 | s 2025(b) | inert (1 not operative) | a heading; its text is in the subunits |
| 1915-1916 | s 2025(b)(1) | encoded | `s 2025(b)(1) the program is a work supplementation or support program` (snap5-s2025-ab) |
| 1917-1918 | s 2025(b)(2) | encoded | `s 2025(b)(2) the State agency may elect to use an amount equal to the allotment to subsidize or support the job` (snap5-s2025-ab) |
| 1919-1920 | s 2025(b)(3) | encoded | `s 2025(b)(3) the procedure applies` (snap5-s2025-ab) |
| 1921-1921 | s 2025(b)(3)(A) | encoded | `s 2025(b)(3)(A) the amount the Secretary shall pay the State agency` (snap5-s2025-ab) |
| 1922-1922 | s 2025(b)(3)(B) | encoded | `s 2025(b)(3)(B) the State agency has expended the amount as required` (snap5-s2025-ab) |
| 1923-1923 | s 2025(b)(3)(C) | encoded | in the functions of s 2025(b)(3) (snap5-s2025-ab) |
| 1924-1924 | s 2025(b)(3)(C)(i) | encoded | `s 2025(b)(3)(C)(i) the amount received is excluded from household income and resources for sections 2014 and 2017(a)` (snap5-s2025-ab) |
| 1925-1925 | s 2025(b)(3)(C)(ii) | encoded | `s 2025(b)(3)(C)(ii) the amount received is considered the value of an allotment provided to the household for section 2017(b)` (snap5-s2025-ab) |
| 1926-1926 | s 2025(b)(3)(D) | encoded | `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` (snap5-s2025-ab) |
| 1927-1928 | s 2025(b)(4) | encoded | `s 2025(b)(4) the individual is excused from a work requirement under section 2015(d) by reason of the fact that the State has a work supplementation or support program` (snap5-s2025-ab) |
| 1929-1930 | s 2025(b)(5) | encoded | `s 2025(b)(5) the State agency has provided the description required` (snap5-s2025-ab) |
| 1931-1932 | s 2025(b)(6) | encoded | `s 2025(b)(6) the work supplementation or support program is permitted` (snap5-s2025-ab) |
| 1933-1933 | s 2025(c) | inert (1 not operative) | a heading; its text is in the subunits |
| 1934-1934 | s 2025(c)(1) | inert (1 not operative) | a heading; its text is in the subunits |
| 1935-1935 | s 2025(c)(1)(A) | inert (1 not operative) | a heading; its text is in the subunits |
| 1936-1937 | s 2025(c)(1)(A)(i) | encoded | `s 2025(c)(1)(A)(i) the Secretary's quality control system is the system required` (snap5-s2025-c1) |
| 1938-1939 | s 2025(c)(1)(A)(ii) | encoded | the lead-in of its subunits, encoded in them (s 2025(c)(1)(A)(ii)(I), s 2025(c)(1)(A)(ii)(II)) (snap5-s2025-c1) |
| 1940-1940 | s 2025(c)(1)(A)(ii)(I) | encoded | `s 2025(c)(1)(A)(ii)(I) the tolerance level set is within the limit` (snap5-s2025-c1) |
| 1941-1941 | s 2025(c)(1)(A)(ii)(II) | encoded | `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year` (snap5-s2025-c1) |
| 1942-1942 | s 2025(c)(1)(B) | inert (1 not operative) | a heading; its text is in the subunits |
| 1943-1944 | s 2025(c)(1)(B)(i) | encoded | `s 2025(c)(1)(B)(i) the last day for the interim final regulations`; `s 2025(c)(1)(B)(i) the interim final regulations are issued in time`; `s 2025(c)(1)(B)(i) the interim final regulations have the content required` (snap5-s2025-c1) |
| 1945-1945 | s 2025(c)(1)(B)(i)(I) | encoded | in the functions of s 2025(c)(1)(B)(i) (snap5-s2025-c1) |
| 1946-1946 | s 2025(c)(1)(B)(i)(II) | encoded | in the functions of s 2025(c)(1)(B)(i) (snap5-s2025-c1) |
| 1947-1947 | s 2025(c)(1)(B)(i)(III) | encoded | in the functions of s 2025(c)(1)(B)(i) (snap5-s2025-c1) |
| 1948-1948 | s 2025(c)(1)(B)(i)(IV) | encoded | in the functions of s 2025(c)(1)(B)(i) (snap5-s2025-c1) |
| 1949-1950 | s 2025(c)(1)(B)(ii) | encoded | `s 2025(c)(1)(B)(ii) the Secretary shall debar the person` (snap5-s2025-c1) |
| 1951-1952 | s 2025(c)(1)(C) | encoded | `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency`; `s 2025(c)(1)(C) the liability amount` (snap5-s2025-c1) |
| 1953-1953 | s 2025(c)(1)(C)(i) | encoded | in the functions of s 2025(c)(1)(C) (snap5-s2025-c1) |
| 1954-1954 | s 2025(c)(1)(C)(ii) | fork F-4 | difference between; `s 2025(c)(1)(C) the liability amount` (snap5-s2025-c1) |
| 1955-1955 | s 2025(c)(1)(C)(ii)(I) | encoded | in the functions of s 2025(c)(1)(C)(ii) (reading F-4) (snap5-s2025-c1) |
| 1956-1956 | s 2025(c)(1)(C)(ii)(II) | encoded | in the functions of s 2025(c)(1)(C)(ii) (reading F-4) (snap5-s2025-c1) |
| 1957-1957 | s 2025(c)(1)(C)(iii) | encoded | in the functions of s 2025(c)(1)(C) (snap5-s2025-c1) |
| 1958-1959 | s 2025(c)(1)(D) | encoded | the lead-in of its subunits, encoded in them (s 2025(c)(1)(D)(i)(I), s 2025(c)(1)(D)(i)(II), s 2025(c)(1)(D)(i)(III)) ... (snap5-s2025-c1) |
| 1960-1960 | s 2025(c)(1)(D)(i) | inert (1 not operative) | a heading; its text is in the subunits |
| 1961-1961 | s 2025(c)(1)(D)(i)(I) | encoded | `s 2025(c)(1)(D)(i)(I) the portion required for new investment is within the limit`; `s 2025(c)(1)(D)(i)(I) the new investment amount may be matched by Federal funds` (snap5-s2025-c1) |
| 1962-1962 | s 2025(c)(1)(D)(i)(II) | encoded | `s 2025(c)(1)(D)(i)(II) the portion designated as the at-risk amount is within the limit` (snap5-s2025-c1) |
| 1963-1963 | s 2025(c)(1)(D)(i)(III) | encoded | `s 2025(c)(1)(D)(i)(III) the combination of actions is allowed` (snap5-s2025-c1) |
| 1964-1964 | s 2025(c)(1)(D)(ii) | fork F-14 | before the end of the fiscal year; `s 2025(c)(1)(D)(ii) the settlement with the State agency is permitted` (snap5-s2025-c1) |
| 1965-1965 | s 2025(c)(1)(E) | inert (1 not operative) | a heading; its text is in the subunits |
| 1966-1967 | s 2025(c)(1)(E)(i) | encoded | `s 2025(c)(1)(E)(i) the State agency shall pay the at-risk amount to the Secretary`; `s 2025(c)(1)(E)(i) the at-risk amount payable to the Secretary` (snap5-s2025-c1) |
| 1968-1968 | s 2025(c)(1)(E)(ii) | inert (1 not operative) | a heading; its text is in the subunits |
| 1969-1970 | s 2025(c)(1)(E)(ii)(I) | encoded | `s 2025(c)(1)(E)(ii)(I) the chief executive officer of the State shall now remit the at-risk amount to the Secretary` (snap5-s2025-c1) |
| 1971-1971 | s 2025(c)(1)(E)(ii)(II) | inert (1 not operative) | a heading; its text is in the subunits |
| 1972-1973 | s 2025(c)(1)(E)(ii)(II)(aa) | encoded | `s 2025(c)(1)(E)(ii)(II)(aa) the largest reduction the Secretary may make in amounts due to the State agency` (snap5-s2025-c1) |
| 1974-1975 | s 2025(c)(1)(E)(ii)(II)(bb) | encoded | `s 2025(c)(1)(E)(ii)(II)(bb) interest accrues on the payment under section 2022(a)(2)` (snap5-s2025-c1) |
| 1976-1976 | s 2025(c)(1)(F) | inert (1 not operative) | a heading; its text is in the subunits |
| 1977-1978 | s 2025(c)(1)(F)(i) | encoded | `s 2025(c)(1)(F)(i) the largest reduction the Secretary may make in amounts due to the State agency` (snap5-s2025-c1) |
| 1979-1980 | s 2025(c)(1)(F)(ii) | encoded | `s 2025(c)(1)(F)(ii) the amount the Secretary shall pay the State agency` (snap5-s2025-c1) |
| 1981-1982 | s 2025(c)(1)(F)(iii) | encoded | `s 2025(c)(1)(F)(iii) the Secretary shall require new investment or payment of the new investment amount`; `s 2025(c)(1)(F)(iii) the new investment amount is divided as required` (snap5-s2025-c1) |
| 1983-1983 | s 2025(c)(1)(F)(iii)(I) | encoded | in the functions of s 2025(c)(1)(F)(iii) (snap5-s2025-c1) |
| 1984-1984 | s 2025(c)(1)(F)(iii)(II) | encoded | in the functions of s 2025(c)(1)(F)(iii) (snap5-s2025-c1) |
| 1985-1986 | s 2025(c)(1)(F)(iv) | inert (2 machinery) | a duty to make regulations |
| 1987-1988 | s 2025(c)(1)(G) | encoded | `s 2025(c)(1)(G) the State agency is required to develop and implement a corrective action plan` (snap5-s2025-c1) |
| 1989-1990 | s 2025(c)(2) | encoded | the lead-in of its subunits, encoded in them (s 2025(c)(2)(A), s 2025(c)(2)(B), s 2025(c)(2)(C)) (snap5-s2025-c2) |
| 1991-1991 | s 2025(c)(2)(A) | encoded | `s 2025(c)(2)(A) the payment error rate` (snap5-s2025-c2) |
| 1992-1992 | s 2025(c)(2)(B) | encoded | `s 2025(c)(2)(B) the overpayment error rate` (snap5-s2025-c2) |
| 1993-1993 | s 2025(c)(2)(B)(i) | encoded | in the functions of s 2025(c)(2)(B) (snap5-s2025-c2) |
| 1994-1994 | s 2025(c)(2)(B)(ii) | encoded | in the functions of s 2025(c)(2)(B) (snap5-s2025-c2) |
| 1995-1995 | s 2025(c)(2)(C) | encoded | `s 2025(c)(2)(C) the underpayment error rate` (snap5-s2025-c2) |
| 1996-1997 | s 2025(c)(3) | encoded | the lead-in of its subunits, encoded in them (s 2025(c)(3)(A), s 2025(c)(3)(B)) (snap5-s2025-c2) |
| 1998-1998 | s 2025(c)(3)(A) | fork F-5 | first 120 days; `s 2025(c)(3)(A) the error is excluded from the payment error rate` (snap5-s2025-c2) |
| 1999-1999 | s 2025(c)(3)(B) | encoded | `s 2025(c)(3)(B) the error is excluded from the payment error rate` (snap5-s2025-c2) |
| 2000-2001 | s 2025(c)(4) | encoded | `s 2025(c)(4) the Secretary may require the State agency to report the factor`; `s 2025(c)(4) the Secretary shall base the determination on all pertinent information available` (snap5-s2025-c2) |
| 2002-2003 | s 2025(c)(5) | encoded | `s 2025(c)(5) the State agency has submitted the data as required`; `s 2025(c)(5) the collection efforts are initiated in time` (snap5-s2025-c2) |
| 2004-2004 | s 2025(c)(6) | inert (1 not operative) | a heading; its text is in the subunits |
| 2005-2006 | s 2025(c)(6)(A) | encoded | `s 2025(c)(6)(A) the national performance measure` (snap5-s2025-c2) |
| 2007-2008 | s 2025(c)(6)(B) | encoded | `s 2025(c)(6)(B) the Secretary may use another measure of the State's error` (snap5-s2025-c2) |
| 2009-2010 | s 2025(c)(6)(C) | encoded | `s 2025(c)(6)(C) the announced national performance measure shall be used` (snap5-s2025-c2) |
| 2011-2012 | s 2025(c)(6)(D) | encoded | `s 2025(c)(6)(D) the national performance measure is subject to administrative or judicial review` (snap5-s2025-c2) |
| 2013-2013 | s 2025(c)(7) | inert (1 not operative) | a heading; its text is in the subunits |
| 2014-2015 | s 2025(c)(7)(A) | encoded | `s 2025(c)(7)(A) the State may seek administrative and judicial review of the action under section 2023` (snap5-s2025-c2) |
| 2016-2017 | s 2025(c)(7)(B) | encoded | `s 2025(c)(7)(B) the determination is subject to administrative or judicial review` (snap5-s2025-c2) |
| 2018-2019 | s 2025(c)(7)(C) | encoded | `s 2025(c)(7)(C) the action is subject to administrative or judicial review` (snap5-s2025-c2) |
| 2020-2020 | s 2025(c)(8) | inert (1 not operative) | a heading; its text is in the subunits |
| 2021-2021 | s 2025(c)(8)(A) | encoded | `s 2025(c)(8)(A) this paragraph applies to the determination` (snap5-s2025-c2) |
| 2022-2022 | s 2025(c)(8)(B) | encoded | `s 2025(c)(8)(B) the first May 31 after the end of the fiscal year`; `s 2025(c)(8)(B) the case review and arbitrations are completed in time` (snap5-s2025-c2) |
| 2023-2023 | s 2025(c)(8)(C) | encoded | `s 2025(c)(8)(C) the first June 30 after the end of the fiscal year` (snap5-s2025-c2) |
| 2024-2024 | s 2025(c)(8)(C)(i) | encoded | `s 2025(c)(8)(C)(i) the final error rates are determined in time` (snap5-s2025-c2) |
| 2025-2025 | s 2025(c)(8)(C)(ii) | encoded | `s 2025(c)(8)(C)(ii) the State agencies are notified in time` (snap5-s2025-c2) |
| 2026-2026 | s 2025(c)(8)(C)(iii) | encoded | `s 2025(c)(8)(C)(iii) the copy is provided in time to the chief executive officer and the legislature` (snap5-s2025-c2) |
| 2027-2027 | s 2025(c)(8)(D) | encoded | `s 2025(c)(8)(D)(i) the notice of appeal is submitted in time`; `s 2025(c)(8)(D)(ii) the evidence in support of the appeal is submitted in time`; `s 2025(c)(8)(D) to (G) a State agency appeals a payment claim` (snap5-s2025-c2 and snap5-s2025-duties) |
| 2028-2028 | s 2025(c)(8)(D)(i) | encoded | in the functions of s 2025(c)(8)(D) (snap5-s2025-c2 and snap5-s2025-duties) |
| 2029-2029 | s 2025(c)(8)(D)(ii) | encoded | in the functions of s 2025(c)(8)(D) (snap5-s2025-c2 and snap5-s2025-duties) |
| 2030-2030 | s 2025(c)(8)(E) | encoded | `s 2025(c)(8)(E) the responsive evidence is submitted in time`; `s 2025(c)(8)(D) to (G) a State agency appeals a payment claim` (snap5-s2025-c2 and snap5-s2025-duties) |
| 2031-2031 | s 2025(c)(8)(F) | encoded | `s 2025(c)(8)(F) the rebuttal evidence is submitted in time`; `s 2025(c)(8)(D) to (G) a State agency appeals a payment claim` (snap5-s2025-c2 and snap5-s2025-duties) |
| 2032-2032 | s 2025(c)(8)(G) | encoded | `s 2025(c)(8)(G) the last day for the administrative law judge's decision`; `s 2025(c)(8)(G) the appeal is decided in time`; `s 2025(c)(8)(D) to (G) a State agency appeals a payment claim`; `s 2025(c)(8)(G)(ii) the administrative law judge decides when no rebuttal evidence is submitted` (snap5-s2025-c2 and snap5-s2025-duties) |
| 2033-2033 | s 2025(c)(8)(G)(i) | encoded | in the functions of s 2025(c)(8)(G) (snap5-s2025-c2 and snap5-s2025-duties) |
| 2034-2034 | s 2025(c)(8)(G)(ii) | encoded | in the functions of s 2025(c)(8)(G) (snap5-s2025-c2 and snap5-s2025-duties) |
| 2035-2035 | s 2025(c)(8)(H) | encoded | `s 2025(c)(8)(H) the administrative law judge has considered what the text requires` (snap5-s2025-c2) |
| 2036-2036 | s 2025(c)(8)(I) | encoded | `s 2025(c)(8)(I) the deadline as extended for cause shown`; `s 2025(c)(8)(I) the administrative law judge shall extend the deadline` (snap5-s2025-c2) |
| 2037-2038 | s 2025(c)(9) | encoded | `s 2025(c)(9) the circumstance is good cause`; `s 2025(c)(9)(C) the growth in the caseload is a significant growth` (snap5-s2025-c2) |
| 2039-2039 | s 2025(c)(9)(A) | encoded | in the functions of s 2025(c)(9) (snap5-s2025-c2) |
| 2040-2040 | s 2025(c)(9)(B) | encoded | in the functions of s 2025(c)(9) (snap5-s2025-c2) |
| 2041-2041 | s 2025(c)(9)(C) | encoded | in the functions of s 2025(c)(9) (snap5-s2025-c2) |
| 2042-2042 | s 2025(c)(9)(D) | encoded | in the functions of s 2025(c)(9) (snap5-s2025-c2) |
| 2043-2043 | s 2025(c)(9)(E) | encoded | in the functions of s 2025(c)(9) (snap5-s2025-c2) |
| 2044-2044 | s 2025(d) | inert (1 not operative) | a heading; its text is in the subunits |
| 2045-2045 | s 2025(d)(1) | inert (1 not operative) | a heading; its text is in the subunits |
| 2046-2047 | s 2025(d)(1)(A) | encoded | `s 2025(d)(1)(A) the guidance is issued in time`; `s 2025(d)(1)(A) the guidance has the content required` (snap5-s2025-dfij) |
| 2048-2048 | s 2025(d)(1)(A)(i) | encoded | in the functions of s 2025(d)(1)(A) (snap5-s2025-dfij) |
| 2049-2049 | s 2025(d)(1)(A)(i)(I) | encoded | in the functions of s 2025(d)(1)(A) (snap5-s2025-dfij) |
| 2050-2050 | s 2025(d)(1)(A)(i)(II) | encoded | in the functions of s 2025(d)(1)(A) (snap5-s2025-dfij) |
| 2051-2051 | s 2025(d)(1)(A)(ii) | encoded | in the functions of s 2025(d)(1)(A) (snap5-s2025-dfij) |
| 2052-2053 | s 2025(d)(1)(B) | encoded | the lead-in of its subunits, encoded in them (s 2025(d)(1)(B)(i), s 2025(d)(1)(B)(ii)) (snap5-s2025-dfij) |
| 2054-2054 | s 2025(d)(1)(B)(i) | encoded | `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` (snap5-s2025-dfij) |
| 2055-2055 | s 2025(d)(1)(B)(ii) | encoded | `s 2025(d)(1)(B)(ii) the total amount of performance bonus payments for the fiscal year`; `s 2025(d)(1)(B)(ii) the State agency shall be awarded a performance bonus payment` (snap5-s2025-dfij) |
| 2056-2056 | s 2025(d)(2) | inert (1 not operative) | a heading; its text is in the subunits |
| 2057-2058 | s 2025(d)(2)(A) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2059-2059 | s 2025(d)(2)(A)(i) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2060-2060 | s 2025(d)(2)(A)(i)(I) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2061-2061 | s 2025(d)(2)(A)(i)(II) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2062-2062 | s 2025(d)(2)(A)(ii) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2063-2063 | s 2025(d)(2)(A)(iii) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2064-2065 | s 2025(d)(2)(B) | encoded | the lead-in of its subunits, encoded in them (s 2025(d)(2)(B)(i), s 2025(d)(2)(B)(ii)) (snap5-s2025-dfij) |
| 2066-2066 | s 2025(d)(2)(B)(i) | encoded | `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` (snap5-s2025-dfij) |
| 2067-2067 | s 2025(d)(2)(B)(ii) | encoded | `s 2025(d)(2)(B)(ii) the total amount of performance bonus payments for the fiscal year`; `s 2025(d)(2)(B)(ii) the State agency shall be awarded a performance bonus payment` (snap5-s2025-dfij) |
| 2068-2069 | s 2025(d)(3) | encoded | `s 2025(d)(3) the State agency is eligible for a performance bonus payment for the fiscal year` (snap5-s2025-dfij) |
| 2070-2071 | s 2025(d)(4) | encoded | `s 2025(d)(4) the determination is subject to administrative or judicial review` (snap5-s2025-dfij) |
| 2072-2073 | s 2025(d)(5) | encoded | `s 2025(d)(5) the State agency may use the performance bonus payment for the use` (snap5-s2025-dfij) |
| 2074-2074 | s 2025(d)(5)(A) | encoded | in the functions of s 2025(d)(5) (snap5-s2025-dfij) |
| 2075-2075 | s 2025(d)(5)(B) | encoded | in the functions of s 2025(d)(5) (snap5-s2025-dfij) |
| 2076-2076 | s 2025(d)(5)(C) | encoded | in the functions of s 2025(d)(5) (snap5-s2025-dfij) |
| 2077-2077 | s 2025(d)(6) | inert (1 not operative) | a heading; its text is in the subunits |
| 2078-2078 | s 2025(d)(6)(A) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2079-2079 | s 2025(d)(6)(A)(i) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2080-2080 | s 2025(d)(6)(A)(ii) | inert (2 machinery) | regulation-making: "establish, by regulation" |
| 2081-2081 | s 2025(d)(6)(B) | encoded | `s 2025(d)(6)(B) the Secretary may award performance bonus payments` (snap5-s2025-dfij) |
| 2082-2083 | s 2025(e) | encoded | `s 2025(e)(1) the household member has met the condition of eligibility of furnishing a social security account number`; `s 2025(e)(2) the account numbers are used in the administration of the program`; `s 2025(e) the Secretary and State agencies shall have access to the information` (snap5-s2025-dfij) |
| 2084-2085 | s 2025(f) | encoded | `s 2025(f) the expense may be paid` (snap5-s2025-dfij) |
| 2086-2086 | s 2025(g) | inert (1 not operative) | a heading; its text is in the subunits |
| 2087-2088 | s 2025(g)(1) | fork F-7 | the amount provided under subsection (a)(6); `s 2025(g)(1) the amount the Secretary is authorized to pay for the costs` (snap5-s2025-gh) |
| 2089-2089 | s 2025(g)(1)(A) | encoded | `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` (snap5-s2025-gh) |
| 2090-2090 | s 2025(g)(1)(A)(i) | encoded | in the functions of s 2025(g)(1)(A) (snap5-s2025-gh) |
| 2091-2091 | s 2025(g)(1)(A)(ii) | encoded | in the functions of s 2025(g)(1)(A) (snap5-s2025-gh) |
| 2092-2092 | s 2025(g)(1)(A)(iii) | encoded | in the functions of s 2025(g)(1)(A) (snap5-s2025-gh) |
| 2093-2093 | s 2025(g)(1)(A)(iv) | encoded | in the functions of s 2025(g)(1)(A) (snap5-s2025-gh) |
| 2094-2094 | s 2025(g)(1)(A)(v) | encoded | `s 2025(g)(1)(A)(v) the system would be tested adequately before and after implementation` (snap5-s2025-gh) |
| 2095-2095 | s 2025(g)(1)(A)(v)(I) | encoded | in the functions of s 2025(g)(1)(A)(v) (snap5-s2025-gh) |
| 2096-2096 | s 2025(g)(1)(A)(v)(II) | encoded | in the functions of s 2025(g)(1)(A)(v) (snap5-s2025-gh) |
| 2097-2097 | s 2025(g)(1)(A)(v)(III) | encoded | in the functions of s 2025(g)(1)(A)(v) (snap5-s2025-gh) |
| 2098-2098 | s 2025(g)(1)(A)(vi) | encoded | `s 2025(g)(1)(A)(vi) the system would be operated in accordance with an adequate plan` (snap5-s2025-gh) |
| 2099-2099 | s 2025(g)(1)(A)(vi)(I) | encoded | in the functions of s 2025(g)(1)(A)(vi) (snap5-s2025-gh) |
| 2100-2100 | s 2025(g)(1)(A)(vi)(II) | encoded | in the functions of s 2025(g)(1)(A)(vi) (snap5-s2025-gh) |
| 2101-2101 | s 2025(g)(1)(A)(vii) | encoded | in the functions of s 2025(g)(1)(A) (snap5-s2025-gh) |
| 2102-2102 | s 2025(g)(1)(B) | encoded | `s 2025(g)(1)(B) the operation of the system qualifies for payment` (snap5-s2025-gh) |
| 2103-2104 | s 2025(g)(2) | fork F-8 | overlap of the two kinds of cost; `s 2025(g)(2) the costs on which the Secretary may make payments after the limitation` (snap5-s2025-gh) |
| 2105-2105 | s 2025(g)(2)(A) | encoded | in the functions of s 2025(g)(2) (reading F-8) (snap5-s2025-gh) |
| 2106-2106 | s 2025(g)(2)(B) | encoded | in the functions of s 2025(g)(2) (reading F-8) (snap5-s2025-gh) |
| 2107-2107 | s 2025(h) | inert (1 not operative) | a heading; its text is in the subunits |
| 2108-2108 | s 2025(h)(1) | inert (1 not operative) | a heading; its text is in the subunits |
| 2109-2110 | s 2025(h)(1)(A) | fork F-13 | 24 months; `s 2025(h)(1)(A) the amount the Secretary shall reserve for each fiscal year, in dollars`; `s 2025(h)(1)(A) the last day the funds remain available` (snap5-s2025-gh) |
| 2111-2112 | s 2025(h)(1)(B) | encoded | `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` (snap5-s2025-gh) |
| 2113-2113 | s 2025(h)(1)(B)(i) | encoded | in the functions of s 2025(h)(1)(B) (snap5-s2025-gh) |
| 2114-2114 | s 2025(h)(1)(B)(ii) | encoded | in the functions of s 2025(h)(1)(B) (snap5-s2025-gh) |
| 2115-2115 | s 2025(h)(1)(C) | inert (1 not operative) | a heading; its text is in the subunits |
| 2116-2117 | s 2025(h)(1)(C)(i) | encoded | `s 2025(h)(1)(C)(i) the unexpended funds the Secretary shall reallocate to other States` (snap5-s2025-gh) |
| 2118-2119 | s 2025(h)(1)(C)(ii) | encoded | `s 2025(h)(1)(C)(ii) the reallocation allows the State agency the time required` (snap5-s2025-gh) |
| 2120-2121 | s 2025(h)(1)(C)(iii) | encoded | `s 2025(h)(1)(C)(iii) every State agency has had an opportunity to obtain reallocated funds` (snap5-s2025-gh) |
| 2122-2123 | s 2025(h)(1)(C)(iv) | encoded | the lead-in of its subunits, encoded in them (s 2025(h)(1)(C)(iv)(I)(aa), s 2025(h)(1)(C)(iv)(I)(bb), s 2025(h)(1)(C)(iv)(I)(cc)) ... (snap5-s2025-gh) |
| 2124-2124 | s 2025(h)(1)(C)(iv)(I) | inert (1 not operative) | a heading; its text is in the subunits |
| 2125-2125 | s 2025(h)(1)(C)(iv)(I)(aa) | encoded | `s 2025(h)(1)(C)(iv)(I) the amount reallocated under subclause (I) meets the minimum` (snap5-s2025-gh) |
| 2126-2126 | s 2025(h)(1)(C)(iv)(I)(bb) | encoded | `s 2025(h)(1)(C)(iv)(I)(bb) the determination is based on what the text requires` (snap5-s2025-gh) |
| 2127-2127 | s 2025(h)(1)(C)(iv)(I)(bb)(AA) | encoded | in the functions of s 2025(h)(1)(C)(iv)(I)(bb) (snap5-s2025-gh) |
| 2128-2128 | s 2025(h)(1)(C)(iv)(I)(bb)(BB) | encoded | in the functions of s 2025(h)(1)(C)(iv)(I)(bb) (snap5-s2025-gh) |
| 2129-2129 | s 2025(h)(1)(C)(iv)(I)(cc) | encoded | `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to the evaluation of subparagraph (F)(vii)`; `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to monitoring under paragraph (5)` (snap5-s2025-gh) |
| 2130-2130 | s 2025(h)(1)(C)(iv)(II) | encoded | `s 2025(h)(1)(C)(iv)(II) the amount reallocated under subclause (II) meets the minimum`; `s 2025(h)(1)(C)(iv)(II) the group is one the programs and activities are targeted to` (snap5-s2025-gh) |
| 2131-2131 | s 2025(h)(1)(C)(iv)(II)(aa) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2132-2132 | s 2025(h)(1)(C)(iv)(II)(bb) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2133-2133 | s 2025(h)(1)(C)(iv)(II)(cc) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2134-2134 | s 2025(h)(1)(C)(iv)(II)(dd) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2135-2135 | s 2025(h)(1)(C)(iv)(II)(ee) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2136-2136 | s 2025(h)(1)(C)(iv)(II)(ff) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2137-2137 | s 2025(h)(1)(C)(iv)(II)(gg) | encoded | in the functions of s 2025(h)(1)(C)(iv)(II) (snap5-s2025-gh) |
| 2138-2138 | s 2025(h)(1)(C)(iv)(III) | encoded | `s 2025(h)(1)(C)(iv)(III) the remaining funds to be reallocated` (snap5-s2025-gh) |
| 2139-2140 | s 2025(h)(1)(C)(v) | encoded | `s 2025(h)(1)(C)(v) the State agency may also be considered for funding under clause (iv)(II)` (snap5-s2025-gh) |
| 2141-2142 | s 2025(h)(1)(D) | encoded | `s 2025(h)(1)(D) the allocation meets the minimum` (snap5-s2025-gh) |
| 2143-2143 | s 2025(h)(1)(E) | inert (1 not operative) | a heading; its text is in the subunits |
| 2144-2145 | s 2025(h)(1)(E)(i) | encoded | `s 2025(h)(1)(E)(i) the additional allocation is within the limit`; `s 2025(h)(1)(E)(i) the costs of serving the member may be reimbursed from the additional allocation` (snap5-s2025-gh) |
| 2146-2146 | s 2025(h)(1)(E)(i)(I) | encoded | in the functions of s 2025(h)(1)(E)(i) (snap5-s2025-gh) |
| 2147-2147 | s 2025(h)(1)(E)(i)(II) | encoded | in the functions of s 2025(h)(1)(E)(i) (snap5-s2025-gh) |
| 2148-2149 | s 2025(h)(1)(E)(ii) | encoded | `s 2025(h)(1)(E)(ii) the State agency is eligible for an additional allocation`; `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant or recipient` (snap5-s2025-gh) |
| 2150-2150 | s 2025(h)(1)(E)(ii)(I) | encoded | in the functions of s 2025(h)(1)(E)(ii) (snap5-s2025-gh) |
| 2151-2151 | s 2025(h)(1)(E)(ii)(II) | encoded | in the functions of s 2025(h)(1)(E)(ii) (snap5-s2025-gh) |
| 2152-2152 | s 2025(h)(1)(E)(ii)(III) | encoded | in the functions of s 2025(h)(1)(E)(ii) (snap5-s2025-gh) |
| 2153-2153 | s 2025(h)(1)(E)(ii)(IV) | encoded | in the functions of s 2025(h)(1)(E)(ii) (snap5-s2025-gh) |
| 2154-2154 | s 2025(h)(1)(F) | inert (1 not operative) | a heading; its text is in the subunits |
| 2155-2155 | s 2025(h)(1)(F)(i) | inert (1 not operative) | a heading; its text is in the subunits |
| 2156-2157 | s 2025(h)(1)(F)(i)(I) | encoded | `s 2025(h)(1)(F)(i)(I) the Secretary has carried out the pilot projects as required` (snap5-s2025-hf) |
| 2158-2159 | s 2025(h)(1)(F)(i)(II) | encoded | `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` (snap5-s2025-hf) |
| 2160-2160 | s 2025(h)(1)(F)(i)(II)(aa) | encoded | in the functions of s 2025(h)(1)(F)(i)(II) (snap5-s2025-hf) |
| 2161-2161 | s 2025(h)(1)(F)(i)(II)(bb) | encoded | in the functions of s 2025(h)(1)(F)(i)(II) (snap5-s2025-hf) |
| 2162-2162 | s 2025(h)(1)(F)(ii) | inert (1 not operative) | a heading; its text is in the subunits |
| 2163-2164 | s 2025(h)(1)(F)(ii)(I) | encoded | `s 2025(h)(1)(F)(ii)(I) the Secretary has selected the pilot project as required` (snap5-s2025-hf) |
| 2165-2166 | s 2025(h)(1)(F)(ii)(II) | encoded | `s 2025(h)(1)(F)(ii)(II) the State agency meets the qualifying criteria`; `s 2025(h)(1)(F)(ii)(II)(cc) the commitment is at least the amount expended for fiscal year 2013` (snap5-s2025-hf) |
| 2167-2167 | s 2025(h)(1)(F)(ii)(II)(aa) | encoded | in the functions of s 2025(h)(1)(F)(ii)(II) (snap5-s2025-hf) |
| 2168-2168 | s 2025(h)(1)(F)(ii)(II)(bb) | encoded | in the functions of s 2025(h)(1)(F)(ii)(II) (snap5-s2025-hf) |
| 2169-2169 | s 2025(h)(1)(F)(ii)(II)(cc) | encoded | in the functions of s 2025(h)(1)(F)(ii)(II) (snap5-s2025-hf) |
| 2170-2171 | s 2025(h)(1)(F)(ii)(III) | encoded | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selecting the pilot project`; `s 2025(h)(1)(F)(ii)(III)(ee) the Secretary has ensured that the group of pilot projects tests the strategies` (snap5-s2025-hf) |
| 2172-2172 | s 2025(h)(1)(F)(ii)(III)(aa) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2173-2173 | s 2025(h)(1)(F)(ii)(III)(bb) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2174-2174 | s 2025(h)(1)(F)(ii)(III)(cc) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2175-2175 | s 2025(h)(1)(F)(ii)(III)(dd) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2176-2176 | s 2025(h)(1)(F)(ii)(III)(ee) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2177-2177 | s 2025(h)(1)(F)(ii)(III)(ee)(AA) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2178-2178 | s 2025(h)(1)(F)(ii)(III)(ee)(BB) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2179-2179 | s 2025(h)(1)(F)(ii)(III)(ee)(CC) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2180-2180 | s 2025(h)(1)(F)(ii)(III)(ee)(DD) | encoded | in the functions of s 2025(h)(1)(F)(ii)(III) (snap5-s2025-hf) |
| 2181-2181 | s 2025(h)(1)(F)(iii) | inert (1 not operative) | a heading; its text is in the subunits |
| 2182-2183 | s 2025(h)(1)(F)(iii)(I) | encoded | `s 2025(h)(1)(F)(iii)(I) the Secretary has established and implemented the termination process` (snap5-s2025-hf) |
| 2184-2185 | s 2025(h)(1)(F)(iii)(II) | encoded | `s 2025(h)(1)(F)(iii)(II) the time period allowed to correct the noncompliance is as required` (snap5-s2025-hf) |
| 2186-2187 | s 2025(h)(1)(F)(iv) | encoded | `s 2025(h)(1)(F)(iv) the program or service is allowable` (snap5-s2025-hf) |
| 2188-2188 | s 2025(h)(1)(F)(iv)(I) | encoded | `s 2025(h)(1)(F)(iv)(I) the activity is employment in the public or private sector that is not subsidized` (snap5-s2025-hf) |
| 2189-2189 | s 2025(h)(1)(F)(iv)(II) | encoded | `s 2025(h)(1)(F)(iv)(II) the activity is subsidized employment in the private sector` (snap5-s2025-hf) |
| 2190-2190 | s 2025(h)(1)(F)(iv)(III) | encoded | `s 2025(h)(1)(F)(iv)(III) the activity is subsidized employment in the public sector` (snap5-s2025-hf) |
| 2191-2191 | s 2025(h)(1)(F)(iv)(IV) | encoded | `s 2025(h)(1)(F)(iv)(IV) the activity is a work activity of the kind described` (snap5-s2025-hf) |
| 2192-2192 | s 2025(h)(1)(F)(iv)(IV)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IV) (snap5-s2025-hf) |
| 2193-2193 | s 2025(h)(1)(F)(iv)(IV)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IV) (snap5-s2025-hf) |
| 2194-2194 | s 2025(h)(1)(F)(iv)(IV)(cc) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IV) (snap5-s2025-hf) |
| 2195-2195 | s 2025(h)(1)(F)(iv)(IV)(dd) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IV) (snap5-s2025-hf) |
| 2196-2196 | s 2025(h)(1)(F)(iv)(V) | encoded | `s 2025(h)(1)(F)(iv)(V) the activity is training of the kind described` (snap5-s2025-hf) |
| 2197-2197 | s 2025(h)(1)(F)(iv)(V)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(V) (snap5-s2025-hf) |
| 2198-2198 | s 2025(h)(1)(F)(iv)(V)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(V) (snap5-s2025-hf) |
| 2199-2199 | s 2025(h)(1)(F)(iv)(VI) | encoded | `s 2025(h)(1)(F)(iv)(VI) the activity is job search, obtaining employment, or preparation of the kind described` (snap5-s2025-hf) |
| 2200-2200 | s 2025(h)(1)(F)(iv)(VI)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VI) (snap5-s2025-hf) |
| 2201-2201 | s 2025(h)(1)(F)(iv)(VI)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VI) (snap5-s2025-hf) |
| 2202-2202 | s 2025(h)(1)(F)(iv)(VI)(cc) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VI) (snap5-s2025-hf) |
| 2203-2203 | s 2025(h)(1)(F)(iv)(VII) | encoded | `s 2025(h)(1)(F)(iv)(VII) the activity is a structured program or embedded activity of the kind described` (snap5-s2025-hf) |
| 2204-2204 | s 2025(h)(1)(F)(iv)(VII)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VII) (snap5-s2025-hf) |
| 2205-2205 | s 2025(h)(1)(F)(iv)(VII)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VII) (snap5-s2025-hf) |
| 2206-2206 | s 2025(h)(1)(F)(iv)(VII)(cc) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VII) (snap5-s2025-hf) |
| 2207-2207 | s 2025(h)(1)(F)(iv)(VII)(dd) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VII) (snap5-s2025-hf) |
| 2208-2208 | s 2025(h)(1)(F)(iv)(VII)(ee) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VII) (snap5-s2025-hf) |
| 2209-2209 | s 2025(h)(1)(F)(iv)(VIII) | encoded | `s 2025(h)(1)(F)(iv)(VIII) the activity is a career and technical training program of the kind described` (snap5-s2025-hf) |
| 2210-2210 | s 2025(h)(1)(F)(iv)(VIII)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VIII) (snap5-s2025-hf) |
| 2211-2211 | s 2025(h)(1)(F)(iv)(VIII)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(VIII) (snap5-s2025-hf) |
| 2212-2212 | s 2025(h)(1)(F)(iv)(IX) | encoded | `s 2025(h)(1)(F)(iv)(IX) the activity is training or education for job skills of the kind described` (snap5-s2025-hf) |
| 2213-2213 | s 2025(h)(1)(F)(iv)(IX)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IX) (snap5-s2025-hf) |
| 2214-2214 | s 2025(h)(1)(F)(iv)(IX)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(IX) (snap5-s2025-hf) |
| 2215-2215 | s 2025(h)(1)(F)(iv)(X) | encoded | `s 2025(h)(1)(F)(iv)(X) the activity is education of the kind described` (snap5-s2025-hf) |
| 2216-2216 | s 2025(h)(1)(F)(iv)(X)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(X) (snap5-s2025-hf) |
| 2217-2217 | s 2025(h)(1)(F)(iv)(X)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(X) (snap5-s2025-hf) |
| 2218-2218 | s 2025(h)(1)(F)(iv)(XI) | encoded | `s 2025(h)(1)(F)(iv)(XI) the activity is regular attendance of the kind described` (snap5-s2025-hf) |
| 2219-2219 | s 2025(h)(1)(F)(iv)(XI)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(XI) (snap5-s2025-hf) |
| 2220-2220 | s 2025(h)(1)(F)(iv)(XI)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(XI) (snap5-s2025-hf) |
| 2221-2221 | s 2025(h)(1)(F)(iv)(XII) | encoded | `s 2025(h)(1)(F)(iv)(XII) the activity is providing child care of the kind described` (snap5-s2025-hf) |
| 2222-2222 | s 2025(h)(1)(F)(iv)(XII)(aa) | encoded | in the functions of s 2025(h)(1)(F)(iv)(XII) (snap5-s2025-hf) |
| 2223-2223 | s 2025(h)(1)(F)(iv)(XII)(bb) | encoded | in the functions of s 2025(h)(1)(F)(iv)(XII) (snap5-s2025-hf) |
| 2224-2224 | s 2025(h)(1)(F)(iv)(XII)(cc) | encoded | in the functions of s 2025(h)(1)(F)(iv)(XII) (snap5-s2025-hf) |
| 2225-2226 | s 2025(h)(1)(F)(v) | encoded | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` (snap5-s2025-hf) |
| 2227-2227 | s 2025(h)(1)(F)(vi) | inert (1 not operative) | a heading; its text is in the subunits |
| 2228-2229 | s 2025(h)(1)(F)(vi)(I) | encoded | `s 2025(h)(1)(F)(vi)(I) the activities are considered to be carried out under section 2015(d)` (snap5-s2025-hf) |
| 2230-2231 | s 2025(h)(1)(F)(vi)(II) | encoded | `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility`; `s 2025(h)(1)(F)(vi)(II) the Secretary has established the standards` (snap5-s2025-hf) |
| 2232-2233 | s 2025(h)(1)(F)(vi)(III) | encoded | `s 2025(h)(1)(F)(vi)(III) the State agency complied before assigning the work registrant to mandatory activities` (snap5-s2025-hf) |
| 2234-2234 | s 2025(h)(1)(F)(vi)(III)(aa) | encoded | in the functions of s 2025(h)(1)(F)(vi)(III) (snap5-s2025-hf) |
| 2235-2235 | s 2025(h)(1)(F)(vi)(III)(bb) | encoded | in the functions of s 2025(h)(1)(F)(vi)(III) (snap5-s2025-hf) |
| 2236-2236 | s 2025(h)(1)(F)(vii) | inert (1 not operative) | a heading; its text is in the subunits |
| 2237-2237 | s 2025(h)(1)(F)(vii)(I) | inert (1 not operative) | a heading; its text is in the subunits |
| 2238-2239 | s 2025(h)(1)(F)(vii)(I)(aa) | encoded | `s 2025(h)(1)(F)(vii)(I) the Secretary has conducted the independent evaluation as required`; `s 2025(h)(1)(F)(vii)(I)(aa) the reporting of results is frequent enough` (snap5-s2025-hf) |
| 2240-2241 | s 2025(h)(1)(F)(vii)(I)(bb) | inert (1 not operative) | a statement of the evaluation's purpose that creates no rule |
| 2242-2243 | s 2025(h)(1)(F)(vii)(I)(cc) | encoded | `s 2025(h)(1)(F)(vii)(I)(cc) the evaluation uses the methodology required` (snap5-s2025-hf) |
| 2244-2244 | s 2025(h)(1)(F)(vii)(I)(cc)(AA) | encoded | in the functions of s 2025(h)(1)(F)(vii)(I)(cc) (snap5-s2025-hf) |
| 2245-2245 | s 2025(h)(1)(F)(vii)(I)(cc)(BB) | encoded | in the functions of s 2025(h)(1)(F)(vii)(I)(cc) (snap5-s2025-hf) |
| 2246-2247 | s 2025(h)(1)(F)(vii)(II) | fork F-10 | until the completion; `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year`; `s 2025(h)(1)(F)(vii)(II) the report is submitted in time`; `s 2025(h)(1)(F)(vii)(II) the report is submitted and shared as required`; `s 2025(h)(1)(F)(vii)(II) the report describes what is required` (snap5-s2025-hf) |
| 2248-2248 | s 2025(h)(1)(F)(vii)(II)(aa) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2249-2249 | s 2025(h)(1)(F)(vii)(II)(bb) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2250-2250 | s 2025(h)(1)(F)(vii)(II)(cc) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2251-2251 | s 2025(h)(1)(F)(vii)(II)(dd) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2252-2252 | s 2025(h)(1)(F)(vii)(II)(dd)(AA) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2253-2253 | s 2025(h)(1)(F)(vii)(II)(dd)(BB) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2254-2254 | s 2025(h)(1)(F)(vii)(II)(ee) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2255-2255 | s 2025(h)(1)(F)(vii)(II)(ff) | encoded | in the functions of s 2025(h)(1)(F)(vii)(II) (reading F-10) (snap5-s2025-hf) |
| 2256-2256 | s 2025(h)(1)(F)(viii) | inert (1 not operative) | a heading; its text is in the subunits |
| 2257-2258 | s 2025(h)(1)(F)(viii)(I) | encoded | `s 2025(h)(1)(F)(viii)(I) the amount the Secretary shall use to carry out the subparagraph for the fiscal year` (snap5-s2025-hf) |
| 2259-2259 | s 2025(h)(1)(F)(viii)(I)(aa) | encoded | in the functions of s 2025(h)(1)(F)(viii)(I) (snap5-s2025-hf) |
| 2260-2260 | s 2025(h)(1)(F)(viii)(I)(bb) | encoded | in the functions of s 2025(h)(1)(F)(viii)(I) (snap5-s2025-hf) |
| 2261-2261 | s 2025(h)(1)(F)(viii)(II) | inert (1 not operative) | a heading; its text is in the subunits |
| 2262-2263 | s 2025(h)(1)(F)(viii)(II)(aa) | encoded | `s 2025(h)(1)(F)(viii)(II)(aa) the number of funded pilot projects is within the limit` (snap5-s2025-hf) |
| 2264-2265 | s 2025(h)(1)(F)(viii)(II)(bb) | fork F-11 | not more than 3 years; `s 2025(h)(1)(F)(viii)(II)(bb) the pilot project is in effect for no more than the limit` (snap5-s2025-hf) |
| 2266-2267 | s 2025(h)(1)(F)(viii)(III) | fork F-12 | through September 30, 2018; `s 2025(h)(1)(F)(viii)(III) the funds remain available on the date` (snap5-s2025-hf) |
| 2268-2268 | s 2025(h)(1)(F)(ix) | inert (1 not operative) | a heading; its text is in the subunits |
| 2269-2270 | s 2025(h)(1)(F)(ix)(I) | encoded | `s 2025(h)(1)(F)(ix)(I) the funds may be used for the use` (snap5-s2025-hf) |
| 2271-2271 | s 2025(h)(1)(F)(ix)(I)(aa) | encoded | in the functions of s 2025(h)(1)(F)(ix)(I) (snap5-s2025-hf) |
| 2272-2272 | s 2025(h)(1)(F)(ix)(I)(bb) | encoded | in the functions of s 2025(h)(1)(F)(ix)(I) (snap5-s2025-hf) |
| 2273-2273 | s 2025(h)(1)(F)(ix)(I)(cc) | encoded | in the functions of s 2025(h)(1)(F)(ix)(I) (snap5-s2025-hf) |
| 2274-2274 | s 2025(h)(1)(F)(ix)(I)(dd) | encoded | in the functions of s 2025(h)(1)(F)(ix)(I) (snap5-s2025-hf) |
| 2275-2276 | s 2025(h)(1)(F)(ix)(II) | encoded | `s 2025(h)(1)(F)(ix)(II) the funds are used as the text allows` (snap5-s2025-hf) |
| 2277-2278 | s 2025(h)(1)(F)(ix)(III) | encoded | `s 2025(h)(1)(F)(ix)(III) the State may contribute the additional funds` (snap5-s2025-hf) |
| 2279-2279 | s 2025(h)(2) | fork F-9 | first limitation in paragraph (3); `s 2025(h)(2) the amount the Secretary shall pay for the additional costs` (snap5-s2025-gh) |
| 2280-2280 | s 2025(h)(3) | encoded | `s 2025(h)(3) the most the reimbursement for dependent care expenses may be`; `s 2025(h)(3) the amount the Secretary shall reimburse the State agency`; `s 2025(h)(3) the reimbursement may be made out of funds allocated under paragraph (1)` (snap5-s2025-gh) |
| 2281-2281 | s 2025(h)(4) | encoded | `s 2025(h)(4) the funds may be used for the use` (snap5-s2025-gh) |
| 2282-2282 | s 2025(h)(5) | inert (1 not operative) | a heading; its text is in the subunits |
| 2283-2284 | s 2025(h)(5)(A) | encoded | `s 2025(h)(5)(A) the Secretary has monitored and assessed as required` (snap5-s2025-gh) |
| 2285-2285 | s 2025(h)(5)(A)(i) | encoded | in the functions of s 2025(h)(5)(A) (snap5-s2025-gh) |
| 2286-2286 | s 2025(h)(5)(A)(ii) | encoded | in the functions of s 2025(h)(5)(A) (snap5-s2025-gh) |
| 2287-2287 | s 2025(h)(5)(B) | inert (1 not operative) | a heading; its text is in the subunits |
| 2288-2289 | s 2025(h)(5)(B)(i) | encoded | `s 2025(h)(5)(B) the State reporting measures are as required` (snap5-s2025-gh) |
| 2290-2291 | s 2025(h)(5)(B)(ii) | encoded | `s 2025(h)(5)(B) the State reporting measures are as required` (snap5-s2025-gh) |
| 2292-2292 | s 2025(h)(5)(B)(ii)(I) | encoded | in the functions of s 2025(h)(5)(B)(ii) (snap5-s2025-gh) |
| 2293-2293 | s 2025(h)(5)(B)(ii)(II) | encoded | in the functions of s 2025(h)(5)(B)(ii) (snap5-s2025-gh) |
| 2294-2295 | s 2025(h)(5)(B)(iii) | encoded | `s 2025(h)(5)(B)(iii) the threshold the Secretary determines is allowed`; `s 2025(h)(5)(B)(iii) the State employment and training plan must identify reporting measures for the component` (snap5-s2025-gh) |
| 2296-2297 | s 2025(h)(5)(B)(iv) | encoded | `s 2025(h)(5)(B)(iv) the reporting measure may be included` (snap5-s2025-gh) |
| 2298-2298 | s 2025(h)(5)(B)(iv)(I) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2299-2299 | s 2025(h)(5)(B)(iv)(II) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2300-2300 | s 2025(h)(5)(B)(iv)(III) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2301-2301 | s 2025(h)(5)(B)(iv)(IV) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2302-2302 | s 2025(h)(5)(B)(iv)(IV)(aa) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2303-2303 | s 2025(h)(5)(B)(iv)(IV)(bb) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2304-2304 | s 2025(h)(5)(B)(iv)(IV)(cc) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2305-2305 | s 2025(h)(5)(B)(iv)(V) | encoded | in the functions of s 2025(h)(5)(B)(iv) (snap5-s2025-gh) |
| 2306-2307 | s 2025(h)(5)(B)(v) | encoded | `s 2025(h)(5)(B)(v) the State agency may report the data to demonstrate the number of participants served` (snap5-s2025-gh) |
| 2308-2309 | s 2025(h)(5)(C) | encoded | `s 2025(h)(5)(C) the Secretary has assessed the State programs as required` (snap5-s2025-gh) |
| 2310-2310 | s 2025(h)(5)(C)(i) | encoded | in the functions of s 2025(h)(5)(C) (snap5-s2025-gh) |
| 2311-2311 | s 2025(h)(5)(C)(ii) | encoded | in the functions of s 2025(h)(5)(C) (snap5-s2025-gh) |
| 2312-2312 | s 2025(h)(5)(C)(iii) | encoded | in the functions of s 2025(h)(5)(C) (snap5-s2025-gh) |
| 2313-2313 | s 2025(h)(5)(C)(iv) | encoded | `s 2025(h)(5)(C)(iv) the Secretary may require the information` (snap5-s2025-gh) |
| 2314-2314 | s 2025(h)(5)(C)(iv)(I) | encoded | in the functions of s 2025(h)(5)(C)(iv) (snap5-s2025-gh) |
| 2315-2315 | s 2025(h)(5)(C)(iv)(II) | encoded | in the functions of s 2025(h)(5)(C)(iv) (snap5-s2025-gh) |
| 2316-2316 | s 2025(h)(5)(C)(iv)(III) | encoded | in the functions of s 2025(h)(5)(C)(iv) (snap5-s2025-gh) |
| 2317-2318 | s 2025(h)(5)(D) | encoded | `s 2025(h)(5)(D) the State agency has reported as required` (snap5-s2025-gh) |
| 2319-2320 | s 2025(h)(5)(E) | encoded | `s 2025(h)(5)(E) the Secretary may require the State agency to modify the plan` (snap5-s2025-gh) |
| 2321-2322 | s 2025(h)(5)(F) | encoded | `s 2025(h)(5)(F) the study is conducted in time`; `s 2025(h)(5)(F) the study covers what the text requires` (snap5-s2025-gh) |
| 2323-2323 | s 2025(h)(5)(F)(i) | encoded | in the functions of s 2025(h)(5)(F) (snap5-s2025-gh) |
| 2324-2324 | s 2025(h)(5)(F)(ii) | encoded | in the functions of s 2025(h)(5)(F) (snap5-s2025-gh) |
| 2325-2325 | s 2025(i) | inert (1 not operative) | a heading; its text is in the subunits |
| 2326-2326 | s 2025(i)(1) | encoded | `s 2025(i)(1) the Department of Agriculture may use the information to determine which project areas have payment error rates that impair the integrity of the program` (snap5-s2025-dfij) |
| 2327-2327 | s 2025(i)(2) | encoded | `s 2025(i)(2) the Secretary may require the State agency to carry out new or modified certification procedures` (snap5-s2025-dfij) |
| 2328-2329 | s 2025(j) | fork F-6 | annually thereafter; `s 2025(j) the date by which the instructional materials are due`; `s 2025(j) the instructional materials are published as required` (snap5-s2025-dfij) |
| 2330-2330 | s 2025(k) | inert (1 not operative) | a heading; its text is in the subunits |
| 2331-2332 | s 2025(k)(1) | encoded | the lead-in of its subunits, encoded in them (s 2025(k)(1)(A), s 2025(k)(1)(B), s 2025(k)(1)(C)) (snap5-s2025-k) |
| 2333-2334 | s 2025(k)(1)(A) | encoded | `s 2025(k)(1)(A) the program is the AFDC program` (snap5-s2025-k) |
| 2335-2336 | s 2025(k)(1)(B) | encoded | `s 2025(k)(1)(B) the period is the base period` (snap5-s2025-k) |
| 2337-2338 | s 2025(k)(1)(C) | encoded | `s 2025(k)(1)(C) the program is the medicaid program` (snap5-s2025-k) |
| 2339-2340 | s 2025(k)(2) | encoded | `s 2025(k)(2) the date by which the Secretary of Health and Human Services must make the determinations`; `s 2025(k)(2) the determinations are made as required`; `s 2025(k)(2) the Secretary of Health and Human Services makes the determinations` (snap5-s2025-k and snap5-s2025-duties) |
| 2341-2341 | s 2025(k)(2)(A) | encoded | in the functions of s 2025(k)(2) (snap5-s2025-k and snap5-s2025-duties) |
| 2342-2342 | s 2025(k)(2)(B) | encoded | `s 2025(k)(2)(B) the amount of common costs allocated to each program when allocated equally` (snap5-s2025-k) |
| 2343-2343 | s 2025(k)(3) | inert (1 not operative) | a heading; its text is in the subunits |
| 2344-2345 | s 2025(k)(3)(A) | encoded | `s 2025(k)(3)(A) the amount paid to the State after the reduction`; `s 2025(k)(3)(A) the reductions are made on a quarterly basis as required` (snap5-s2025-k) |
| 2346-2347 | s 2025(k)(3)(B) | encoded | `s 2025(k)(3)(B) the determinations were not made by September 30, 1999` (snap5-s2025-k) |
| 2348-2348 | s 2025(k)(3)(B)(i) | encoded | `s 2025(k)(3)(B)(i) the amount of the reduction in the fiscal year in which the determinations are made` (snap5-s2025-k) |
| 2349-2349 | s 2025(k)(3)(B)(ii) | encoded | `s 2025(k)(3)(B)(ii) subparagraph (A) applies in the fiscal year` (snap5-s2025-k) |
| 2350-2350 | s 2025(k)(4) | inert (1 not operative) | a heading; its text is in the subunits |
| 2351-2352 | s 2025(k)(4)(A) | encoded | `s 2025(k)(4)(A) the last day for the Secretary to notify the chief executive officer of the State`; `s 2025(k)(4)(A) the Secretary notifies the chief executive officer in time`; `s 2025(k)(4)(A) the Secretary notifies the chief executive officer of the State` (snap5-s2025-k and snap5-s2025-duties) |
| 2353-2353 | s 2025(k)(4)(B) | inert (1 not operative) | a heading; its text is in the subunits |
| 2354-2355 | s 2025(k)(4)(B)(i) | encoded | `s 2025(k)(4)(B)(i) the last day for the State to appeal to an administrative law judge`; `s 2025(k)(4)(B)(i) the State may appeal the determination`; `s 2025(k)(4)(B)(i) the State appeals to an administrative law judge` (snap5-s2025-k and snap5-s2025-duties) |
| 2356-2357 | s 2025(k)(4)(B)(ii) | encoded | `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` (snap5-s2025-k) |
| 2358-2359 | s 2025(k)(4)(B)(iii) | encoded | `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` (snap5-s2025-k) |
| 2360-2361 | s 2025(k)(4)(B)(iv) | encoded | `s 2025(k)(4)(B)(iv) the last day for the administrative law judge to decide and notify`; `s 2025(k)(4)(B)(iv) the administrative law judge decides and notifies in time`; `s 2025(k)(4)(B)(iv) the administrative law judge decides and notifies` (snap5-s2025-k and snap5-s2025-duties) |
| 2362-2362 | s 2025(k)(4)(B)(iv)(I) | encoded | in the functions of s 2025(k)(4)(B)(iv) (snap5-s2025-k and snap5-s2025-duties) |
| 2363-2363 | s 2025(k)(4)(B)(iv)(II) | encoded | in the functions of s 2025(k)(4)(B)(iv) (snap5-s2025-k and snap5-s2025-duties) |
| 2364-2364 | s 2025(k)(4)(C) | inert (1 not operative) | a heading; its text is in the subunits |
| 2365-2366 | s 2025(k)(4)(C)(i) | encoded | `s 2025(k)(4)(C)(i) the last day for the State to appeal to the Departmental Appeals Board`; `s 2025(k)(4)(C)(i) the State may appeal the decision`; `s 2025(k)(4)(C)(i) the State appeals to the Departmental Appeals Board` (snap5-s2025-k and snap5-s2025-duties) |
| 2367-2368 | s 2025(k)(4)(C)(ii) | encoded | `s 2025(k)(4)(C)(ii) the Board has reviewed the decision as required` (snap5-s2025-k) |
| 2369-2370 | s 2025(k)(4)(C)(iii) | encoded | `s 2025(k)(4)(C)(iii) the last day for the Board to decide and notify`; `s 2025(k)(4)(C)(iii) the Board decides and notifies in time`; `s 2025(k)(4)(C)(iii) the Board decides and notifies` (snap5-s2025-k and snap5-s2025-duties) |
| 2371-2371 | s 2025(k)(4)(C)(iii)(I) | encoded | in the functions of s 2025(k)(4)(C)(iii) (snap5-s2025-k and snap5-s2025-duties) |
| 2372-2372 | s 2025(k)(4)(C)(iii)(II) | encoded | in the functions of s 2025(k)(4)(C)(iii) (snap5-s2025-k and snap5-s2025-duties) |
| 2373-2374 | s 2025(k)(4)(D) | encoded | `s 2025(k)(4)(D) the determination or decision is subject to judicial review` (snap5-s2025-k) |
| 2375-2376 | s 2025(k)(4)(E) | encoded | `s 2025(k)(4)(E) the pendency of the appeal affects the requirement that the Secretary reduce payments` (snap5-s2025-k) |
| 2377-2377 | s 2025(k)(5) | encoded | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` (snap5-s2025-k) |
| 2378-2379 | s 2025(k)(5)(A) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2380-2380 | s 2025(k)(5)(A)(i) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2381-2381 | s 2025(k)(5)(A)(ii) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2382-2383 | s 2025(k)(5)(B) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2384-2384 | s 2025(k)(5)(B)(i) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2385-2385 | s 2025(k)(5)(B)(ii) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2386-2386 | s 2025(k)(5)(B)(iii) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2387-2387 | s 2025(k)(5)(B)(iv) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2388-2388 | s 2025(k)(5)(B)(iv)(I) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2389-2389 | s 2025(k)(5)(B)(iv)(II) | encoded | in the functions of s 2025(k)(5) (snap5-s2025-k) |
| 2390-2391 | source credit of s 2025 | inert (1 not operative) | a source credit lists amending Acts and creates no rule |
| 2656-2656 | s 2026a | inert (1 not operative) | the section heading |
| 2657-2658 | s 2026a(a) | fork F-2 | vitamins A and D: FDA, State and local standards; `s 2026a(a) the product is fluid milk` (snap5-s2026a) |
| 2659-2659 | s 2026a(a)(1) | encoded | in the functions of s 2026a(a) (reading F-2) (snap5-s2026a) |
| 2660-2660 | s 2026a(a)(2) | encoded | in the functions of s 2026a(a) (reading F-2) (snap5-s2026a) |
| 2661-2661 | s 2026a(a)(3) | encoded | in the functions of s 2026a(a) (reading F-2) (snap5-s2026a) |
| 2662-2662 | s 2026a(a)(4) | encoded | in the functions of s 2026a(a) (reading F-2) (snap5-s2026a) |
| 2663-2664 | s 2026a(b) | encoded | `s 2026a(b) the project is a healthy fluid milk incentive project the Secretary is to carry out` (snap5-s2026a) |
| 2665-2665 | s 2026a(c) | inert (1 not operative) | a heading; its text is in the subunits |
| 2666-2667 | s 2026a(c)(1) | encoded | `s 2026a(c)(1) the Secretary shall enter into the agreement with, or provide the grant to, the entity` (snap5-s2026a) |
| 2668-2669 | s 2026a(c)(2) | encoded | `s 2026a(c)(2) the entity has met the application requirement` (snap5-s2026a) |
| 2670-2671 | s 2026a(c)(3) | encoded | `s 2026a(c)(3) the projects are evaluated against the required criteria` (snap5-s2026a) |
| 2672-2673 | s 2026a(c)(4) | encoded | `s 2026a(c)(4) the funds made available under this section may be used for the project` (snap5-s2026a) |
| 2674-2674 | s 2026a(d) | inert (1 not operative) | a heading; its text is in the subunits |
| 2675-2675 | s 2026a(d)(1) | inert (1 not operative) | a heading; its text is in the subunits |
| 2676-2676 | s 2026a(d)(1)(A) | inert (1 not operative) | a heading; its text is in the subunits |
| 2677-2678 | s 2026a(d)(1)(A)(i) | encoded | `s 2026a(d)(1)(A)(i) the evaluation is the independent evaluation required` (snap5-s2026a) |
| 2679-2680 | s 2026a(d)(1)(A)(ii) | encoded | `s 2026a(d)(1)(A)(ii) the evaluation meets the requirement of rigorous methodologies` (snap5-s2026a) |
| 2681-2682 | s 2026a(d)(1)(B) | encoded | `s 2026a(d)(1)(B) the amount used for evaluation is within the limit` (snap5-s2026a) |
| 2683-2684 | s 2026a(d)(2) | encoded | `s 2026a(d)(2) the date by which the report is due in the year`; `s 2026a(d)(2) the report is submitted in time`; `s 2026a(d)(2) the report describes the matters required` (snap5-s2026a) |
| 2685-2685 | s 2026a(d)(2)(A) | encoded | in the functions of s 2026a(d)(2) (snap5-s2026a) |
| 2686-2686 | s 2026a(d)(2)(B) | encoded | in the functions of s 2026a(d)(2) (snap5-s2026a) |
| 2687-2687 | s 2026a(d)(2)(B)(i) | encoded | in the functions of s 2026a(d)(2) (snap5-s2026a) |
| 2688-2688 | s 2026a(d)(2)(B)(ii) | encoded | in the functions of s 2026a(d)(2) (snap5-s2026a) |
| 2689-2690 | s 2026a(d)(3) | encoded | `s 2026a(d)(3) the evaluation results are shared as required` (snap5-s2026a) |
| 2691-2691 | s 2026a(e) | inert (1 not operative) | a heading; its text is in the subunits |
| 2692-2693 | s 2026a(e)(1) | encoded | `s 2026a(e)(1) the amount authorized to be appropriated, in dollars` (snap5-s2026a) |
| 2694-2695 | s 2026a(e)(2) | encoded | `s 2026a(e)(2) the funds are available to carry out this section` (snap5-s2026a) |
| 2696-2697 | source credit of s 2026a | inert (1 not operative) | a source credit lists amending Acts and creates no rule |
| 2731-2731 | s 2028 | inert (1 not operative) | the section heading |
| 2732-2732 | s 2028(a) | inert (1 not operative) | a heading; its text is in the subunits |
| 2733-2734 | s 2028(a)(1) | encoded | `s 2028(a)(1) the place is a governmental entity` (snap5-s2028) |
| 2735-2735 | s 2028(a)(1)(A) | encoded | in the functions of s 2028(a)(1) (snap5-s2028) |
| 2736-2736 | s 2028(a)(1)(B) | encoded | in the functions of s 2028(a)(1) (snap5-s2028) |
| 2737-2737 | s 2028(a)(2) | inert (1 not operative) | a heading; its text is in the subunits |
| 2738-2739 | s 2028(a)(2)(A) | encoded | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` (snap5-s2028) |
| 2740-2740 | s 2028(a)(2)(A)(i) | encoded | in the functions of s 2028(a)(2)(A) (snap5-s2028) |
| 2741-2741 | s 2028(a)(2)(A)(ii) | fork F-15 | as adjusted by the percentage; `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` (snap5-s2028) |
| 2742-2742 | s 2028(a)(2)(B) | inert (1 not operative) | a heading; its text is in the subunits |
| 2743-2744 | s 2028(a)(2)(B)(i) | encoded | `s 2028(a)(2)(B)(i) the Commonwealth's share of the funds`; `s 2028(a)(2)(B)(i) the payment toward the Commonwealth's expenditures and administrative expenses` (snap5-s2028) |
| 2745-2745 | s 2028(a)(2)(B)(i)(I) | encoded | in the functions of s 2028(a)(2)(B)(i) (snap5-s2028) |
| 2746-2746 | s 2028(a)(2)(B)(i)(II) | encoded | in the functions of s 2028(a)(2)(B)(i) (snap5-s2028) |
| 2747-2748 | s 2028(a)(2)(B)(ii) | encoded | `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` (snap5-s2028) |
| 2749-2749 | s 2028(a)(2)(B)(ii)(I) | encoded | in the functions of s 2028(a)(2)(B)(ii) (snap5-s2028) |
| 2750-2750 | s 2028(a)(2)(B)(ii)(II) | encoded | in the functions of s 2028(a)(2)(B)(ii) (snap5-s2028) |
| 2751-2751 | s 2028(a)(2)(B)(ii)(III) | encoded | in the functions of s 2028(a)(2)(B)(ii) (snap5-s2028) |
| 2752-2753 | s 2028(a)(2)(C) | encoded | `s 2028(a)(2)(C) American Samoa's share of the funds`; `s 2028(a)(2)(C) the payment toward American Samoa's expenditures` (snap5-s2028) |
| 2754-2755 | s 2028(a)(2)(D) | encoded | `s 2028(a)(2)(D) the carryover is within the limit` (snap5-s2028) |
| 2756-2757 | s 2028(a)(3) | encoded | `s 2028(a)(3) the payment to the Commonwealth for the fiscal year` (snap5-s2028) |
| 2758-2758 | s 2028(b) | inert (1 not operative) | a heading; its text is in the subunits |
| 2759-2759 | s 2028(b)(1) | inert (1 not operative) | a heading; its text is in the subunits |
| 2760-2760 | s 2028(b)(1)(A) | encoded | `s 2028(b)(1) the Commonwealth may receive payments`; `s 2028(b)(1)(A) the plan is submitted in time`; `s 2028(b)(1)(A) the plan has the required contents`; `s 2028(b)(1)(A) the Commonwealth submits a plan` (snap5-s2028 and snap5-s2025-duties) |
| 2761-2761 | s 2028(b)(1)(A)(i) | encoded | in the functions of s 2028(b)(1)(A) (snap5-s2028 and snap5-s2025-duties) |
| 2762-2762 | s 2028(b)(1)(A)(ii) | encoded | in the functions of s 2028(b)(1)(A) (snap5-s2028 and snap5-s2025-duties) |
| 2763-2763 | s 2028(b)(1)(A)(iii) | encoded | in the functions of s 2028(b)(1)(A) (snap5-s2028 and snap5-s2025-duties) |
| 2764-2764 | s 2028(b)(1)(A)(iv) | encoded | in the functions of s 2028(b)(1)(A) (snap5-s2028 and snap5-s2025-duties) |
| 2765-2765 | s 2028(b)(1)(A)(v) | encoded | in the functions of s 2028(b)(1)(A) (snap5-s2028 and snap5-s2025-duties) |
| 2766-2766 | s 2028(b)(1)(B) | inert (1 not operative) | a heading; its text is in the subunits |
| 2767-2767 | s 2028(b)(1)(B)(i) | encoded | `s 2028(b)(1)(B)(i) the Secretary's decision on the plan is in time`; `s 2028(b)(1)(B)(i) the Secretary shall approve the plan`; `s 2028(b)(1)(B)(i) payments may be made for the fiscal year of the plan`; `s 2028(b)(1)(B)(i) the Secretary approves or disapproves the plan` (snap5-s2028 and snap5-s2025-duties) |
| 2768-2768 | s 2028(b)(1)(B)(ii) | encoded | `s 2028(b)(1)(B)(ii) the withheld payments are to be paid` (snap5-s2028) |
| 2769-2769 | s 2028(b)(2) | inert (1 not operative) | a heading; its text is in the subunits |
| 2770-2770 | s 2028(b)(2)(A) | fork F-1 | biennial; `s 2028(b)(2)(A) the last day for the report of the audit findings`; `s 2028(b)(2)(A) the report of the audit findings is in time`; `s 2028(b)(2)(A) the audit is biennial`; `s 2028(b)(2)(A) the Commonwealth reports the findings of the audit` (snap5-s2028 and snap5-s2025-duties) |
| 2771-2771 | s 2028(b)(2)(B) | encoded | `s 2028(b)(2)(B) the statement is provided in time`; `s 2028(b)(2)(B) the statement has the required contents`; `s 2028(b)(2)(B) the Commonwealth provides the Secretary with a statement` (snap5-s2028 and snap5-s2025-duties) |
| 2772-2772 | s 2028(b)(2)(C) | inert (1 not operative) | a heading; its text is in the subunits |
| 2773-2773 | s 2028(b)(2)(C)(i) | encoded | `s 2028(b)(2)(C)(i) further payments may be made` (snap5-s2028) |
| 2774-2774 | s 2028(b)(2)(C)(ii) | encoded | `s 2028(b)(2)(C)(ii) the withheld payments are to be paid` (snap5-s2028) |
| 2775-2775 | s 2028(b)(2)(C)(iii) | encoded | `s 2028(b)(2)(C)(iii) the Secretary may refer the matter to the Attorney General`; `s 2028(b)(2)(C)(iii) appropriate injunctive relief shall issue` (snap5-s2028) |
| 2776-2776 | s 2028(c) | inert (1 not operative) | a heading; its text is in the subunits |
| 2777-2777 | s 2028(c)(1) | encoded | `s 2028(c)(1) the Secretary shall provide for the review of the program` (snap5-s2028) |
| 2778-2778 | s 2028(c)(2) | encoded | `s 2028(c)(2) the Secretary may provide technical assistance` (snap5-s2028) |
| 2779-2780 | s 2028(d) | encoded | `s 2028(d) the conduct is within the offence`; `s 2028(d) the most the person may be fined, in dollars`; `s 2028(d) the longest term of imprisonment, in years` (snap5-s2028) |
| 2781-2781 | s 2028(e) | inert (1 not operative) | a heading; its text is in the subunits |
| 2782-2783 | s 2028(e)(1) | encoded | `s 2028(e)(1) the review includes the required examinations` (snap5-s2028) |
| 2784-2784 | s 2028(e)(1)(A) | encoded | in the functions of s 2028(e)(1) (snap5-s2028) |
| 2785-2785 | s 2028(e)(1)(B) | encoded | in the functions of s 2028(e)(1) (snap5-s2028) |
| 2786-2786 | s 2028(e)(1)(C) | encoded | in the functions of s 2028(e)(1) (snap5-s2028) |
| 2787-2787 | s 2028(e)(1)(D) | encoded | in the functions of s 2028(e)(1) (snap5-s2028) |
| 2788-2788 | s 2028(e)(1)(E) | encoded | in the functions of s 2028(e)(1) (snap5-s2028) |
| 2789-2790 | s 2028(e)(2) | encoded | `s 2028(e)(2) the last day for the report`; `s 2028(e)(2) the report is in time` (snap5-s2028) |
| 2791-2791 | s 2028(e)(3) | inert (1 not operative) | a heading; its text is in the subunits |
| 2792-2793 | s 2028(e)(3)(A) | encoded | `s 2028(e)(3)(A) the largest share of a participant's benefit a plan may distribute in cash`; `s 2028(e)(3)(A) the Secretary shall disapprove the plan` (snap5-s2028) |
| 2794-2794 | s 2028(e)(3)(A)(i) | encoded | in the functions of s 2028(e)(3)(A) (snap5-s2028) |
| 2795-2795 | s 2028(e)(3)(A)(ii) | encoded | in the functions of s 2028(e)(3)(A) (snap5-s2028) |
| 2796-2796 | s 2028(e)(3)(A)(iii) | encoded | in the functions of s 2028(e)(3)(A) (snap5-s2028) |
| 2797-2797 | s 2028(e)(3)(A)(iv) | encoded | in the functions of s 2028(e)(3)(A) (snap5-s2028) |
| 2798-2798 | s 2028(e)(3)(A)(v) | encoded | in the functions of s 2028(e)(3)(A) (snap5-s2028) |
| 2799-2800 | s 2028(e)(3)(B) | encoded | `s 2028(e)(3)(B) the Secretary may approve a plan that exempts participants or categories of participants` (snap5-s2028) |
| 2801-2802 | s 2028(e)(4) | encoded | `s 2028(e)(4) the amount to make available for the review and report` (snap5-s2028) |
| 2803-2804 | source credit of s 2028 | inert (1 not operative) | a source credit lists amending Acts and creates no rule |

## Fork register (snap5)

Fifteen places where the text can be read two or more ways with different outcomes.
Each entry gives the words, the readings seen, the reading taken, what the choice changes, and the rule that carries it.
The reading taken is a reading, not a ruling; the other reading is one line of code to change, named in each entry.

**F-1. Section 2028(b)(2)(A), "a biennial audit" (line 2770).**
The words: "The Commonwealth shall provide for a biennial audit of expenditures ..., and within 120 days of the end of each fiscal year in which the audit is made, shall report to the Secretary the findings of such audit."
Readings: (1) an audit in each period of two fiscal years, so the gap between consecutive audited fiscal years is at most 2; (2) an audit exactly two years apart, so a gap of 1 is not biennial; (3) "twice a year" (the common slip for "biannual").
Taken: (1).
Licence: "each fiscal year in which the audit is made" shows that audits are not made every year, which rules out (3); the text does not say whether an audit sooner than two years is allowed, and (1) is the reading that does not add a prohibition.
Changes: whether a gap of one fiscal year is a no (`JUST FALSE`) or fine.
Encoded in: `s 2028(b)(2)(A) the audit is biennial`; the report date in `s 2028(b)(2)(A) the report of the audit findings is in time`.
To change reading (2): `EQUALS 2` for `AT MOST 2`.

**F-2. Section 2026a(a)(4), vitamins A and D (line 2662).**
The words: "contains vitamins A and D at levels consistent with the Food and Drug Administration, State, and local standards for fluid milk".
Readings: (1) consistent with all three standards; (2) consistent with each of the standards that exists where the milk is sold (a place with no local standard needs none); (3) consistent with any one of the three.
Taken: (1): three plain yes/no inputs, all required.
Licence: the standards are joined by commas and "and" in a single list after "consistent with", which is the way the other three limbs are joined by "and" (a conjunction).
Changes: a milk that meets the FDA standard in a county with a stricter local standard it does not meet.
What the text does not say: what a missing local standard means; the caller states the fact, and the encoding does not decide it.
Encoded in: `s 2026a(a) the product is fluid milk`.

**F-3. Section 2025(a), the retention proviso (line 1913).**
Three small readings in one sentence.
(i) "recovered or collected pursuant to sections 2015(b) and 2022(c)": (1) either section (taken); (2) both sections at once.
(ii) "20 percent of the value of any other funds or allotments recovered or collected, except the value of funds or allotments recovered or collected that arise from an error of a State agency": (1) the exception qualifies only the 20 percent limb, the nearest antecedent (taken); (2) the exception qualifies both limbs, so a section 2015(b) recovery that arises from the State agency's error is not retained at all.
(iii) "the Secretary is authorized at the Secretary's discretion to pay ... as well as to permit each State to retain": (1) the discretion reaches the permission to retain, so the share is the most the Secretary may permit (taken); (2) the shares are entitlements.
Licence: (i) a recovery under one section would not also be "pursuant to" the other; (ii) the exception follows "any other funds" immediately; (iii) the infinitive "to permit" is governed by "is authorized".
Changes: (i) on reading (2) a recovery under only one of the two sections would be retained at 20 percent, not 35; (ii) a section 2015(b) recovery from the State agency's own error is 35 percent, not 0; (iii) the answer is a ceiling.
Encoded in: `s 2025(a) the share of recovered or collected funds the Secretary may permit the State to retain` and `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars` (the core's `Claim`).
Tested: a section 2015(b) recovery arising from the State's error is still 35 percent (350 of 1000); an ordinary recovery from the State's error is 0.

**F-4. Section 2025(c)(1)(C)(ii), "the difference between ... the payment error rate ... and 6 percent" (lines 1954-1956).**
Readings: (1) the rate minus 0.06, which is negative below 6 percent (taken); (2) the absolute difference; (3) the excess over 6 percent, zero below it.
Taken: (1), and a rate under 6 percent is `NOTHING`.
Licence: "the difference between (I) the payment error rate and (II) 6 percent" lists the rate first; the text says nothing of a rate below 6 percent, and the liability provision begins from a rate that "exceeds 105 percent of the national performance measure".
Changes: a State agency below 6 percent (but above 105 percent of the national measure): `NOTHING` here, a positive amount on (2), zero on (3).
Encoded in: `s 2025(c)(1)(C) the liability amount` (allotments times the rate minus 0.06 times 0.10).

**F-5. Section 2025(c)(3)(A), "during the first 120 days from the required implementation date" (line 1998).**
Readings: (1) the implementation date through that date plus 120, both ends included (taken); (2) the 120 days after that date (days 1 to 120); (3) the date and the 119 after it (120 days counting the date as the first).
Licence: "from" the date, and the clause does not say the date itself is excluded.
Changes: an error on day 0, day 120 or day 121 (the days at the two edges).
Encoded in: `s 2025(c)(3)(A) the error is excluded from the payment error rate`.

**F-6. Section 2025(j), "Not later than 180 days after September 19, 1988, and annually thereafter" (line 2329).**
Readings: (1) the first deadline is 18 March 1989 and the next ones are its anniversaries (taken); (2) once in each calendar year after 1989, on any date; (3) within a year of the last publication, whenever that was.
Licence: "annually thereafter" repeats the deadline, which is a date, so the anniversary of the date is the nearest reading; (2) and (3) turn a deadline into a frequency.
Changes: the date by which publication in year n is late.
Encoded in: `s 2025(j) the date by which the instructional materials are due` (takes the number of years after the first deadline) and `s 2025(j) the instructional materials are published as required`.

**F-7. Section 2025(g)(1), "the amount provided under subsection (a)(6)" (line 2088).**
Readings: (1) the share that subsection (a) states for administrative costs (50 percent through fiscal year 2026, 25 percent after), times the qualifying costs (taken); (2) the whole of the costs; (3) a rate in another provision.
Licence: paragraph (a)(6) lists the computerization costs among the costs subsection (a) pays a share of, and states no amount of its own; "provided under subsection (a)(6)" reads as "the amount subsection (a) provides for the costs of (a)(6)".
Changes: the amount paid for a qualifying system by a factor of two to four.
Encoded in: `s 2025(g)(1) the amount the Secretary is authorized to pay for the costs`.

**F-8. Section 2025(g)(2), "to the extent that the State agency (A) is reimbursed for the costs under any other Federal program; or (B) uses the systems for purposes not connected with the program" (lines 2103-2106).**
Readings: (1) the two kinds of cost are separate and both come off the costs incurred (taken); (2) a cost that is both reimbursed elsewhere and used for another purpose comes off once.
Licence: the caller states each figure; the text does not say how an overlap is counted.
Changes: the payable cost whenever the two figures overlap.
Also taken: a total below zero is no payment, so the result is clamped at 0.
Encoded in: `s 2025(g)(2) the costs on which the Secretary may make payments after the limitation`.

**F-9. Section 2025(h)(2), "subject to the first limitation in paragraph (3)" (line 2279).**
Readings: (1) the cap on the reimbursement for dependent care expenses, the first "except that" limit of paragraph (3) (taken); (2) the 50 per centum rate of paragraph (3) itself.
Licence: paragraph (3) has two limits, in this order: dependent care "shall not exceed an amount equal to the payment made under section 2015(d)(4)(I)(i)(II) ... but not more than the applicable local market rate", and "such reimbursement shall not be made out of funds allocated under paragraph (1)".
Changes: whether the dependent care part of the additional costs in paragraph (2) is paid at 50 per centum up to the dependent care cap (reading 1, as the code does) or at 50 per centum with no cap.
Encoded in: `s 2025(h)(2) the amount the Secretary shall pay for the additional costs`.

**F-10. Section 2025(h)(1)(F)(vii)(II), "each December 31 thereafter until the completion of the last evaluation" (line 2247).**
Readings: (1) a December 31 on or after the date of completion has no report due; the last report is the one due on the last 31 December before completion (taken); (2) the 31 December of the year of completion is the last report.
Licence: "until" ends the series, and a report of an evaluation not yet completed is the only one the clause describes.
Changes: whether a final report is due in the year of completion.
Encoded in: `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year`, `... the report is submitted in time`.

**F-11. Section 2025(h)(1)(F)(viii)(II)(bb), "Each pilot project shall be in effect for not more than 3 years" (line 2265).**
Readings: (1) the last day is no later than the third anniversary of the first day (taken); (2) the last day is no later than the day before the third anniversary (a period of 3 years that starts on day one ends the day before).
Changes: one day.
Encoded in: `s 2025(h)(1)(F)(viii)(II)(bb) the pilot project is in effect for no more than the limit`.

**F-12. Section 2025(h)(1)(F)(viii)(III), "Funds ... shall remain available through September 30, 2018" (line 2267).**
Readings: (1) on a date after 30 September 2018 the text says nothing about the funds: `NOTHING` (taken, marginal reading (b)); (2) after that date the funds are no longer available, so the answer is a no.
Licence: "remain available through" states a period of availability and does not state that they cease to be available.
Encoded in: `s 2025(h)(1)(F)(viii)(III) the funds remain available on the date`.

**F-13. Section 2025(h)(1)(A), "to remain available for 24 months" (line 2110).**
Readings: (1) the same day of the month 24 months after the date the funds are reserved (taken); (2) the day before that date; (3) 24 months from the start of the fiscal year.
Licence: the text does not say when the 24 months start; the encoding asks the date the funds are reserved as an input.
Changes: the last day by one day, or by up to a year.
Encoded in: `s 2025(h)(1)(A) the last day the funds remain available`.

**F-14. Section 2025(c)(1)(D)(ii), a settlement "before the end of the fiscal year in which the liability amount is determined" (line 1964).**
Readings: (1) a settlement on or before the last day of the fiscal year is in time (taken); (2) a settlement on the last day is too late.
Licence: the end of a fiscal year is the end of its last day.
Encoded in: `s 2025(c)(1)(D)(ii) the settlement with the State agency is permitted`.

**F-15. Section 2028(a)(2)(A)(ii), "the amount specified in clause (i), as adjusted by the percentage by which the thrifty food plan has been adjusted ... between June 30, 2002, and June 30 of the immediately preceding fiscal year" (line 2741).**
Readings: (1) the amount in clause (i) times one plus the cumulative percentage change between the two dates (taken); (2) the amount adjusted year by year, compounded.
Licence: "the amount specified in clause (i)" is named as the base for every later year, so the adjustment is applied to that one amount; the caller supplies the cumulative change, so (2) gives the same result when the caller states the compounded figure.
Encoded in: `s 2028(a)(2)(A) the amount of the block grants for the fiscal year`.
Also: the percentage is an input (`s 2012(u)(3) ...`, a fraction: 0.05 is 5 percent), and the clause is "subject to the availability of appropriations under section 2027(a)", which is the input `s 2027(a) appropriations are available`.

## Jural relations (snap5)

One row per provision (or per sentence of a provision) that creates, or is read as creating, a relation between two parties; a provision that creates none is listed as `none`.
The vocabulary is Hohfeld's: **claim** (right) with **duty**; **privilege** (liberty) with **no-right**; **power** with **liability**; **immunity** with **disability**.
How the words of the Act are read: "shall" addressed to an official or a State agency is a duty of that party, with the party for whose benefit it is made holding the claim (`not named in the text` where the text names nobody); "is authorized to" and "may" are a privilege (or a power where the act changes someone's legal position, such as establishing a liability amount or approving a plan); "shall not be subject to administrative or judicial review" is an immunity of the decision-maker and a disability of whoever might review.
The holder is the party holding the right, privilege, power or immunity; "against" is the party bearing the correlative.
Each rule is stated once, as a relation between two parties, and named neutrally; the twelve regulative rules and their decision twins are the same relations in the form of a timetable, and appear here once under the unit they implement.
The last column is the L4 rule of the unit; the others of the unit are in its coverage row.

| unit | holder | holds | against | correlative | what it is | L4 rule |
| --- | --- | --- | --- | --- | --- | --- |
| s 2025(a) | the Secretary | privilege | the State agency | no-right (the payment is authorised, not owed) | to pay 50 percent (through fiscal year 2026) or 25 percent (from 2027) of a State agency's administrative costs | `s 2025(a) the share of administrative costs the Secretary is authorized to pay` |
| s 2025(a) proviso, first limb | the Secretary | privilege | a State agency on a reservation or in a Native village | no-right | to pay such further administrative amounts as the Secretary determines necessary, at the Secretary's discretion | `s 2025(a) the additional amount the Secretary may pay a State agency for a reservation or a Native village` |
| s 2025(a) proviso, second limb | the Secretary | power | the State agency | liability (the share it may keep is fixed by the Secretary) | to permit the State to retain 35 percent or 20 percent of what it recovers or collects | `s 2025(a) the share of recovered or collected funds the Secretary may permit the State to retain` |
| s 2025(a) proviso, second limb (the amount of a claim) | the Secretary | power | the State agency | liability (the core's Claim: its amount times the share) | the dollar amount of a recovered claim the State may keep | `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars` |
| s 2025(a), last sentence | not named in the text | claim | the officials responsible for determinations of ineligibility | duty not to receive or benefit from the retained revenues | a bar on personal benefit | `s 2025(a) the official may receive or benefit from the revenues retained by the State` |
| s 2025(b)(1) | none | - | none | - | a definition of the program | `s 2025(b)(1) the program is a work supplementation or support program` |
| s 2025(b)(2) | the State agency | power | the household whose allotment is used | liability | to elect to use an amount equal to the allotment to subsidise or support a job | `s 2025(b)(2) the State agency may elect to use an amount equal to the allotment to subsidize or support the job` |
| s 2025(b)(3) (lead-in) | none | - | none | - | the condition on which the procedure applies | `s 2025(b)(3) the procedure applies` |
| s 2025(b)(3)(A) | the State agency | claim | the Secretary | duty | to be paid an amount equal to the allotment | `s 2025(b)(3)(A) the amount the Secretary shall pay the State agency` |
| s 2025(b)(3)(B) | the Secretary | claim | the State agency | duty | that the State agency expends the amount as the clause requires | `s 2025(b)(3)(B) the State agency has expended the amount as required` |
| s 2025(b)(3)(C)(i) | the household | immunity | the State agency and the Secretary | disability | the payment is not counted as income or resources under sections 2014 and 2017(a) | `s 2025(b)(3)(C)(i) the amount received is excluded from household income and resources for sections 2014 and 2017(a)` |
| s 2025(b)(3)(C)(ii) | none | - | none | - | a counting rule: the payment is treated as the value of an allotment for section 2017(b) | `s 2025(b)(3)(C)(ii) the amount received is considered the value of an allotment provided to the household for section 2017(b)` |
| s 2025(b)(3)(D) | the State agency | privilege | the household | no-right | to give no allotment for the period during which the member takes part in the program | `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` |
| s 2025(b)(4) | the State agency | claim | the individual | duty (the work requirement of section 2015(d) still binds) | that no one is excused from a work requirement because of the program | `s 2025(b)(4) the individual is excused from a work requirement under section 2015(d) by reason of the fact that the State has a work supplementation or support program` |
| s 2025(b)(5) | the Secretary | claim | the State agency | duty | to receive a description of how recipients will move into unsubsidised employment | `s 2025(b)(5) the State agency has provided the description required` |
| s 2025(b)(6) | workers who are not supplemented or supported | claim | the State agency | duty | not to have their employment displaced by the program | `s 2025(b)(6) the work supplementation or support program is permitted` |
| s 2025(c)(1)(A)(i) | not named in the text | claim | the Secretary | duty | to carry out a quality control system that enhances payment accuracy | `s 2025(c)(1)(A)(i) the Secretary's quality control system is the system required` |
| s 2025(c)(1)(A)(ii)(I) | the Secretary | power | the State agencies | liability | to set the tolerance level within the statutory limit | `s 2025(c)(1)(A)(ii)(I) the tolerance level set is within the limit` |
| s 2025(c)(1)(A)(ii)(II) | the Secretary | power | the State agencies | liability | to set the tolerance level for each fiscal year | `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year` |
| s 2025(c)(1)(B)(i) | not named in the text | claim | the Secretary | duty | to issue interim final regulations not later than 180 days after 20 December 2018 | `s 2025(c)(1)(B)(i) the last day for the interim final regulations` (+2 more in the coverage row) |
| s 2025(c)(1)(B)(ii) | the Secretary | power | any person who knowingly submits false information | liability (to debarment) | to debar them (a duty of the Secretary, a liability of the person) | `s 2025(c)(1)(B)(ii) the Secretary shall debar the person` |
| s 2025(c)(1)(C) | the Secretary | power | the State agency | liability (the liability amount) | to establish the amount for which the State agency may be liable | `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency` |
| s 2025(c)(1)(C)(ii) | none | - | none | - | the arithmetic of the liability amount (fork F-4) | `s 2025(c)(1)(C) the liability amount` |
| s 2025(c)(1)(D)(i)(I) | the Secretary | power | the State agency | liability | to require up to 50 percent of the liability amount to be used for new investment | `s 2025(c)(1)(D)(i)(I) the portion required for new investment is within the limit` (+1 more in the coverage row) |
| s 2025(c)(1)(D)(i)(II) | the Secretary | power | the State agency | liability | to designate up to 50 percent as the at-risk amount | `s 2025(c)(1)(D)(i)(II) the portion designated as the at-risk amount is within the limit` |
| s 2025(c)(1)(D)(i)(III) | the Secretary | power | the State agency | liability | to take any combination of the two | `s 2025(c)(1)(D)(i)(III) the combination of actions is allowed` |
| s 2025(c)(1)(D)(ii) | the Secretary | power | the State agency | liability | to settle with the State agency before the end of the fiscal year (fork F-14) | `s 2025(c)(1)(D)(ii) the settlement with the State agency is permitted` |
| s 2025(c)(1)(E)(i) | the Secretary | claim | the State agency | duty | to be paid the at-risk amount where a liability amount is established the next year | `s 2025(c)(1)(E)(i) the State agency shall pay the at-risk amount to the Secretary` |
| s 2025(c)(1)(E)(ii)(I) | the Secretary | claim | the chief executive officer of the State | duty | to have the at-risk amount remitted | `s 2025(c)(1)(E)(ii)(I) the chief executive officer of the State shall now remit the at-risk amount to the Secretary` |
| s 2025(c)(1)(E)(ii)(II)(aa) | the Secretary | power | the State agency | liability | to reduce amounts due the State agency, up to a stated cap | `s 2025(c)(1)(E)(ii)(II)(aa) the largest reduction the Secretary may make in amounts due to the State agency` |
| s 2025(c)(1)(E)(ii)(II)(bb) | the State agency | immunity | the Secretary | disability | no interest accrues for the period the Secretary determines | `s 2025(c)(1)(E)(ii)(II)(bb) interest accrues on the payment under section 2022(a)(2)` |
| s 2025(c)(1)(F)(i) | the Secretary | power | the State agency | liability | to reduce amounts due, up to a stated cap | `s 2025(c)(1)(F)(i) the largest reduction the Secretary may make in amounts due to the State agency` |
| s 2025(c)(1)(F)(ii) | the State agency | claim | the Secretary | duty | to be paid the amount that follows from the settlement | `s 2025(c)(1)(F)(ii) the amount the Secretary shall pay the State agency` |
| s 2025(c)(1)(F)(iii) | the Secretary | power | the State agency | liability | to require new investment, and to divide the new investment amount | `s 2025(c)(1)(F)(iii) the Secretary shall require new investment or payment of the new investment amount` (+1 more in the coverage row) |
| s 2025(c)(1)(F)(iv) | none | - | none | - | regulation-making (inert, reason 2) | none (inert) |
| s 2025(c)(1)(G) | the Secretary | claim | the State agency (other than one under 6 percent) | duty | to develop and implement a corrective action plan | `s 2025(c)(1)(G) the State agency is required to develop and implement a corrective action plan` |
| s 2025(c)(2)(A) | none | - | none | - | definition of the payment error rate | `s 2025(c)(2)(A) the payment error rate` |
| s 2025(c)(2)(B) | none | - | none | - | definition of the overpayment error rate | `s 2025(c)(2)(B) the overpayment error rate` |
| s 2025(c)(2)(C) | none | - | none | - | definition of the underpayment error rate | `s 2025(c)(2)(C) the underpayment error rate` |
| s 2025(c)(3)(A) | the State agency | immunity | the Secretary | disability | errors from new regulations in the first 120 days are not counted (fork F-5) | `s 2025(c)(3)(A) the error is excluded from the payment error rate` |
| s 2025(c)(3)(B) | the State agency | immunity | the Secretary | disability | errors from correctly processed Federal information or approved policy are not counted | `s 2025(c)(3)(B) the error is excluded from the payment error rate` |
| s 2025(c)(4) | the Secretary | power | the State agency | liability | to require a report of a factor, and the duty to base a determination on all pertinent information | `s 2025(c)(4) the Secretary may require the State agency to report the factor` (+1 more in the coverage row) |
| s 2025(c)(5) | the Secretary | claim | the State agency | duty | to receive data on operations, and collection efforts started in time | `s 2025(c)(5) the State agency has submitted the data as required` (+1 more in the coverage row) |
| s 2025(c)(6)(A) | not named in the text | claim | the Secretary | duty | to announce the national performance measure | `s 2025(c)(6)(A) the national performance measure` |
| s 2025(c)(6)(B) | the Secretary | power | the State agency | liability | to use another measure of the State's error | `s 2025(c)(6)(B) the Secretary may use another measure of the State's error` |
| s 2025(c)(6)(C) | the State agency | claim | the Secretary | duty | that the announced measure is used | `s 2025(c)(6)(C) the announced national performance measure shall be used` |
| s 2025(c)(6)(D) | the Secretary | immunity | the State agency and the courts | disability | the measure is not subject to administrative or judicial review | `s 2025(c)(6)(D) the national performance measure is subject to administrative or judicial review` |
| s 2025(c)(7)(A) | the State | power | the Secretary | liability | to seek administrative and judicial review under section 2023 of a liability action | `s 2025(c)(7)(A) the State may seek administrative and judicial review of the action under section 2023` |
| s 2025(c)(7)(B) | the State | power | the Secretary | liability | the determination is reviewable only if a liability amount is established | `s 2025(c)(7)(B) the determination is subject to administrative or judicial review` |
| s 2025(c)(7)(C) | the Secretary | immunity | the State agency | disability | the action is not subject to review | `s 2025(c)(7)(C) the action is subject to administrative or judicial review` |
| s 2025(c)(8)(A) | none | - | none | - | scope: which determinations the paragraph applies to | `s 2025(c)(8)(A) this paragraph applies to the determination` |
| s 2025(c)(8)(B) | the State agency | claim | the Secretary | duty | case review and arbitrations completed by the first 31 May | `s 2025(c)(8)(B) the first May 31 after the end of the fiscal year` (+1 more in the coverage row) |
| s 2025(c)(8)(C) | none | - | none | - | the date: the first 30 June after the end of the fiscal year | `s 2025(c)(8)(C) the first June 30 after the end of the fiscal year` |
| s 2025(c)(8)(C)(iii) | the chief executive officer and the legislature of the State | claim | the Secretary | duty | to be given a copy of the notice | `s 2025(c)(8)(C)(iii) the copy is provided in time to the chief executive officer and the legislature` |
| s 2025(c)(8)(C)(i) | the State agency | claim | the Secretary | duty | final error rates determined by the first 30 June | `s 2025(c)(8)(C)(i) the final error rates are determined in time` |
| s 2025(c)(8)(C)(ii) | the State agency | claim | the Secretary | duty | to be notified by the first 30 June | `s 2025(c)(8)(C)(ii) the State agencies are notified in time` |
| s 2025(c)(8)(D) | the State agency | power | the Secretary | liability (to hear the appeal) | to appeal a claim or liability amount: notice within 10 days, evidence within 60 days | `s 2025(c)(8)(D)(i) the notice of appeal is submitted in time` |
| s 2025(c)(8)(E) | the State agency | claim | the Secretary | duty | to receive the Secretary's responsive evidence within 60 days | `s 2025(c)(8)(E) the responsive evidence is submitted in time` (+1 more in the coverage row) |
| s 2025(c)(8)(F) | the Secretary | claim | the State agency | duty | to receive the State agency's rebuttal evidence within 30 days | `s 2025(c)(8)(F) the rebuttal evidence is submitted in time` (+1 more in the coverage row) |
| s 2025(c)(8)(G) | the State agency | claim | the administrative law judge | duty | to have the appeal decided within 60 or 90 days | `s 2025(c)(8)(G) the last day for the administrative law judge's decision` |
| s 2025(c)(8)(H) | the State agency and the Secretary | claim | the administrative law judge | duty | to have all grounds for denying the claim or liability considered | `s 2025(c)(8)(H) the administrative law judge has considered what the text requires` |
| s 2025(c)(8)(I) | the administrative law judge | power | the parties | liability | to extend a deadline for cause shown | `s 2025(c)(8)(I) the deadline as extended for cause shown` (+1 more in the coverage row) |
| s 2025(c)(9) | none | - | none | - | definitions of good cause and of a significant growth in the caseload (for subsection (c) only) | `s 2025(c)(9) the circumstance is good cause` (+1 more in the coverage row) |
| s 2025(d)(1)(A) | the State agencies | claim | the Secretary | duty | to be given guidance on the performance measures by 1 October 2002 | `s 2025(d)(1)(A) the guidance is issued in time` (+1 more in the coverage row) |
| s 2025(d)(1)(B)(i) | the State agencies | claim | the Secretary | duty | to have their performance measured | `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` |
| s 2025(d)(1)(B)(ii) | a qualifying State agency | claim | the Secretary | duty | to be awarded a performance bonus payment in the following fiscal year, from the fixed total | `s 2025(d)(1)(B)(ii) the State agency shall be awarded a performance bonus payment` |
| s 2025(d)(2)(A) | none | - | none | - | regulation-making (inert, reason 2) | none (inert) |
| s 2025(d)(2)(B)(i) | the State agencies | claim | the Secretary | duty | to have their performance measured | `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` |
| s 2025(d)(2)(B)(ii) | a qualifying State agency | claim | the Secretary | duty | to be awarded a performance bonus payment | `s 2025(d)(2)(B)(ii) the State agency shall be awarded a performance bonus payment` |
| s 2025(d)(3) | the Secretary | privilege | the State agency | no-right | to pay no performance bonus for a year in which a liability amount is established | `s 2025(d)(3) the State agency is eligible for a performance bonus payment for the fiscal year` |
| s 2025(d)(4) | the Secretary | immunity | the State agency | disability | the determinations are not subject to review | `s 2025(d)(4) the determination is subject to administrative or judicial review` |
| s 2025(d)(5) | the State agency | privilege (limited) | the Secretary | no-right within the use, claim outside it | to use a bonus payment only to carry out the program | `s 2025(d)(5) the State agency may use the performance bonus payment for the use` |
| s 2025(d)(6)(A) | none | - | none | - | regulation-making (inert, reason 2) | none (inert) |
| s 2025(d)(6)(B) | the State agencies | no-right | the Secretary | privilege (to pay no bonus in 2019 for 2018) | no bonus is awarded in fiscal year 2019 for fiscal year 2018 | `s 2025(d)(6)(B) the Secretary may award performance bonus payments` |
| s 2025(e), first sentence | the Secretary and the State agency | claim | each household member | duty (to furnish a social security account number as a condition of eligibility) | to require and use the number | `s 2025(e)(1) the household member has met the condition of eligibility of furnishing a social security account number` |
| s 2025(e), second sentence | the Secretary and the State agencies | claim | the Commissioner of Social Security | duty (to give access, to the extent determined necessary) | to have access to the Social Security record of an applicant or participant, to the extent determined necessary | `s 2025(e) the Secretary and State agencies shall have access to the information` |
| s 2025(f) | the Secretary | privilege | the officers and employees of the Department | none (benefits them but gives them no claim) | to employ counsel and pay fees, costs and bail for the defence of Department officers and employees | `s 2025(f) the expense may be paid` |
| s 2025(g)(1) | the State agency | claim | the Secretary | duty (where the Secretary determines the system qualifies) | to be paid the (a)(6) share of the cost of a qualifying computer system (fork F-7) | `s 2025(g)(1) the amount the Secretary is authorized to pay for the costs` |
| s 2025(g)(1)(A) | the Secretary | power | the State agency | liability (the system is judged against the seven clauses) | to determine that a system qualifies for planning, design, development or installation payment | `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` |
| s 2025(g)(1)(A)(v) | none | - | none | - | a test the Secretary applies: the system would be tested adequately | `s 2025(g)(1)(A)(v) the system would be tested adequately before and after implementation` |
| s 2025(g)(1)(A)(vi) | none | - | none | - | a test the Secretary applies: the system would be run by an adequate plan | `s 2025(g)(1)(A)(vi) the system would be operated in accordance with an adequate plan` |
| s 2025(g)(1)(B) | the Secretary | power | the State agency | liability | to determine that a system may continue to be operated | `s 2025(g)(1)(B) the operation of the system qualifies for payment` |
| s 2025(g)(2) | the Secretary | immunity | the State agency | disability (it cannot claim payment for costs reimbursed under another Federal program or used for other purposes) | a limit on the payment (fork F-8) | `s 2025(g)(2) the costs on which the Secretary may make payments after the limitation` |
| s 2025(h)(1)(A) | the State agencies | claim | the Secretary | duty | the Secretary reserves $103,900,000 a year for allocation, available for 24 months (fork F-13) | `s 2025(h)(1)(A) the amount the Secretary shall reserve for each fiscal year, in dollars` (+1 more in the coverage row) |
| s 2025(h)(1)(B) | the State agencies | claim | the Secretary | duty | allocation by a formula of the kind required | `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` |
| s 2025(h)(1)(C)(i) | the State agencies that ask for funds | claim | the Secretary | duty | unexpended funds are reallocated | `s 2025(h)(1)(C)(i) the unexpended funds the Secretary shall reallocate to other States` |
| s 2025(h)(1)(C)(ii) | the State agency receiving reallocated funds | claim | the Secretary | duty | at least 270 days to expend them | `s 2025(h)(1)(C)(ii) the reallocation allows the State agency the time required` |
| s 2025(h)(1)(C)(iii) | every State agency | claim | the Secretary | duty | an opportunity to obtain reallocated funds | `s 2025(h)(1)(C)(iii) every State agency has had an opportunity to obtain reallocated funds` |
| s 2025(h)(1)(C)(iv)(I)(aa) | the State agencies requesting funds | claim | the Secretary | duty | at least 50 percent of the reallocated funds | `s 2025(h)(1)(C)(iv)(I) the amount reallocated under subclause (I) meets the minimum` |
| s 2025(h)(1)(C)(iv)(I)(bb) | the Secretary | power | the State agencies | liability | to determine the reallocation on the stated bases | `s 2025(h)(1)(C)(iv)(I)(bb) the determination is based on what the text requires` |
| s 2025(h)(1)(C)(iv)(I)(cc) | the State agency | immunity | the Secretary | disability | the activities are not subject to the evaluation of subparagraph (F)(vii) | `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to the evaluation of subparagraph (F)(vii)` (+1 more in the coverage row) |
| s 2025(h)(1)(C)(iv)(II) | the State agencies with qualifying programs | claim | the Secretary | duty | at least 30 percent of the reallocated funds | `s 2025(h)(1)(C)(iv)(II) the amount reallocated under subclause (II) meets the minimum` (+1 more in the coverage row) |
| s 2025(h)(1)(C)(iv)(III) | the State agencies requesting funds | claim | the Secretary | duty | the remainder of the reallocated funds | `s 2025(h)(1)(C)(iv)(III) the remaining funds to be reallocated` |
| s 2025(h)(1)(C)(v) | the State agency | privilege | the Secretary | no-right | to be considered for funding under both clauses | `s 2025(h)(1)(C)(v) the State agency may also be considered for funding under clause (iv)(II)` |
| s 2025(h)(1)(D) | each State agency | claim | the Secretary | duty | to receive not less than $100,000 for each fiscal year | `s 2025(h)(1)(D) the allocation meets the minimum` |
| s 2025(h)(1)(E)(i) | the State agency | claim | the Secretary | duty | an additional allocation of up to $20,000,000 a year, with which it may reimburse the cost of serving a participant | `s 2025(h)(1)(E)(i) the additional allocation is within the limit` (+1 more in the coverage row) |
| s 2025(h)(1)(E)(ii) | the State agency | claim | the Secretary | duty (on condition that the State commits to offer a position) | to the additional allocation if it commits | `s 2025(h)(1)(E)(ii) the State agency is eligible for an additional allocation` (+1 more in the coverage row) |
| s 2025(h)(1)(F)(i)(I) | not named in the text | claim | the Secretary | duty | to carry out pilot projects with State agencies | `s 2025(h)(1)(F)(i)(I) the Secretary has carried out the pilot projects as required` |
| s 2025(h)(1)(F)(i)(II) | none | - | none | - | what a pilot project must be | `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` |
| s 2025(h)(1)(F)(ii)(I) | the State agency | claim | the Secretary | duty | the Secretary selects pilot projects by the criteria | `s 2025(h)(1)(F)(ii)(I) the Secretary has selected the pilot project as required` |
| s 2025(h)(1)(F)(ii)(II) | the Secretary | power | the State agency | liability (to qualifying criteria) | a State agency must meet the criteria to take part | `s 2025(h)(1)(F)(ii)(II) the State agency meets the qualifying criteria` (+1 more in the coverage row) |
| s 2025(h)(1)(F)(ii)(III) | the State agencies | claim | the Secretary | duty | the Secretary considers the stated factors and ensures a range of strategies | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selecting the pilot project` (+1 more in the coverage row) |
| s 2025(h)(1)(F)(iii)(I) | the State agency | claim | the Secretary | duty | to have a process for terminating a pilot project | `s 2025(h)(1)(F)(iii)(I) the Secretary has established and implemented the termination process` |
| s 2025(h)(1)(F)(iii)(II) | the State agency | claim | the Secretary | duty | a time of up to 180 days to correct noncompliance | `s 2025(h)(1)(F)(iii)(II) the time period allowed to correct the noncompliance is as required` |
| s 2025(h)(1)(F)(iv) | none | - | none | - | a definition: the twelve kinds of allowable program or service | `s 2025(h)(1)(F)(iv) the program or service is allowable` |
| s 2025(h)(1)(F)(iv)(I) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(I) the activity is employment in the public or private sector that is not subsidized` |
| s 2025(h)(1)(F)(iv)(II) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(II) the activity is subsidized employment in the private sector` |
| s 2025(h)(1)(F)(iv)(III) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(III) the activity is subsidized employment in the public sector` |
| s 2025(h)(1)(F)(iv)(IV) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(IV) the activity is a work activity of the kind described` |
| s 2025(h)(1)(F)(iv)(V) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(V) the activity is training of the kind described` |
| s 2025(h)(1)(F)(iv)(VI) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(VI) the activity is job search, obtaining employment, or preparation of the kind described` |
| s 2025(h)(1)(F)(iv)(VII) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(VII) the activity is a structured program or embedded activity of the kind described` |
| s 2025(h)(1)(F)(iv)(VIII) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(VIII) the activity is a career and technical training program of the kind described` |
| s 2025(h)(1)(F)(iv)(IX) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(IX) the activity is training or education for job skills of the kind described` |
| s 2025(h)(1)(F)(iv)(X) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(X) the activity is education of the kind described` |
| s 2025(h)(1)(F)(iv)(XI) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(XI) the activity is regular attendance of the kind described` |
| s 2025(h)(1)(F)(iv)(XII) | none | - | none | - | a definition: one kind of allowable activity | `s 2025(h)(1)(F)(iv)(XII) the activity is providing child care of the kind described` |
| s 2025(h)(1)(F)(v) | the work registrant | immunity (from ineligibility, for good cause) | the State agency | disability | a registrant who fails to work for good cause does not become ineligible | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` |
| s 2025(h)(1)(F)(vi)(I) | none | - | none | - | activities count as carried out under section 2015(d) | `s 2025(h)(1)(F)(vi)(I) the activities are considered to be carried out under section 2015(d)` |
| s 2025(h)(1)(F)(vi)(II) | the work registrant | immunity | the State agency | disability | failure to work for reasons beyond one's control does not result in ineligibility | `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` (+1 more in the coverage row) |
| s 2025(h)(1)(F)(vi)(III) | the work registrant | claim | the State agency | duty (to give the notice and counting the hours before assigning mandatory activities) | conditions before assignment | `s 2025(h)(1)(F)(vi)(III) the State agency complied before assigning the work registrant to mandatory activities` |
| s 2025(h)(1)(F)(vii)(I)(aa) | not named in the text | claim | the Secretary | duty | to conduct an independent evaluation, reported in 12-month increments | `s 2025(h)(1)(F)(vii)(I) the Secretary has conducted the independent evaluation as required` (+1 more in the coverage row) |
| s 2025(h)(1)(F)(vii)(I)(bb) | none | - | none | - | a statement of the purpose of the evaluation (inert, reason 1) | none (inert) |
| s 2025(h)(1)(F)(vii)(I)(cc) | not named in the text | claim | the Secretary | duty | the evaluation uses valid statistical methods | `s 2025(h)(1)(F)(vii)(I)(cc) the evaluation uses the methodology required` |
| s 2025(h)(1)(F)(vii)(II) | the Committees on Agriculture of the House and of the Senate | claim | the Secretary | duty | a report every 31 December from 2015 until the last evaluation is complete (fork F-10) | `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year` (+3 more in the coverage row) |
| s 2025(h)(1)(F)(viii)(I) | none | - | none | - | the amount to be used (a sum) | `s 2025(h)(1)(F)(viii)(I) the amount the Secretary shall use to carry out the subparagraph for the fiscal year` |
| s 2025(h)(1)(F)(viii)(II)(aa) | the State agencies | immunity (outside the ten) | the Secretary | disability (to fund more than 10 projects) | a limit of ten pilot projects | `s 2025(h)(1)(F)(viii)(II)(aa) the number of funded pilot projects is within the limit` |
| s 2025(h)(1)(F)(viii)(II)(bb) | none | - | none | - | a limit of 3 years in effect (fork F-11) | `s 2025(h)(1)(F)(viii)(II)(bb) the pilot project is in effect for no more than the limit` |
| s 2025(h)(1)(F)(viii)(III) | none | - | none | - | the funds remain available through 30 September 2018 (fork F-12) | `s 2025(h)(1)(F)(viii)(III) the funds remain available on the date` |
| s 2025(h)(1)(F)(ix)(I) | the Secretary | claim | the State agency | duty (use the funds only for the stated purposes) | use of pilot project funds | `s 2025(h)(1)(F)(ix)(I) the funds may be used for the use` |
| s 2025(h)(1)(F)(ix)(II) | the Secretary | claim | the State agency | duty (supplement, not supplant) | the funds supplement non-Federal funds | `s 2025(h)(1)(F)(ix)(II) the funds are used as the text allows` |
| s 2025(h)(1)(F)(ix)(III) | the State | privilege | the Secretary | no-right | to contribute additional funds if permissible under Federal law | `s 2025(h)(1)(F)(ix)(III) the State may contribute the additional funds` |
| s 2025(h)(2) | the State agency | claim | the Secretary | duty | to be paid 50 percent of the additional costs, subject to the first limitation of paragraph (3) (fork F-9) | `s 2025(h)(2) the amount the Secretary shall pay for the additional costs` |
| s 2025(h)(3) | the State agency | claim | the Secretary | duty (up to a cap) | to be reimbursed for dependent care expenses | `s 2025(h)(3) the amount the Secretary shall reimburse the State agency` |
| s 2025(h)(4) | the Secretary | claim | the State agency | duty | funds are used only for the stated programs | `s 2025(h)(4) the funds may be used for the use` |
| s 2025(h)(5)(A) | not named in the text | claim | the Secretary | duty | to monitor and assess State programs | `s 2025(h)(5)(A) the Secretary has monitored and assessed as required` |
| s 2025(h)(5)(B)(i) | not named in the text | claim | the Secretary | duty | to develop State reporting measures with the Secretary of Labor | `s 2025(h)(5)(B) the State reporting measures are as required` |
| s 2025(h)(5)(B)(ii) | none | - | none | - | what the measures must be based on | `s 2025(h)(5)(B) the State reporting measures are as required` |
| s 2025(h)(5)(B)(iii) | the Secretary | power | the State agency | liability | to require plans to identify reporting measures for each component serving at least 100 people a year | `s 2025(h)(5)(B)(iii) the threshold the Secretary determines is allowed` (+1 more in the coverage row) |
| s 2025(h)(5)(B)(iv) | none | - | none | - | a list of measures a plan may include | `s 2025(h)(5)(B)(iv) the reporting measure may be included` |
| s 2025(h)(5)(B)(v) | the State agency | privilege | the Secretary | no-right | to report workforce-partnership data | `s 2025(h)(5)(B)(v) the State agency may report the data to demonstrate the number of participants served` |
| s 2025(h)(5)(C) | not named in the text | claim | the Secretary | duty | to assess State programs periodically | `s 2025(h)(5)(C) the Secretary has assessed the State programs as required` |
| s 2025(h)(5)(C)(iv) | the Secretary | power | the State agency (with an additional allocation) | liability | to require the information to evaluate compliance | `s 2025(h)(5)(C)(iv) the Secretary may require the information` |
| s 2025(h)(5)(D) | the Secretary | claim | the State agency | duty | an annual report | `s 2025(h)(5)(D) the State agency has reported as required` |
| s 2025(h)(5)(E) | the Secretary | power | the State agency | liability | to require modifications to the plan where outcomes are inadequate | `s 2025(h)(5)(E) the Secretary may require the State agency to modify the plan` |
| s 2025(h)(5)(F) | not named in the text | claim | the Secretary | duty | a study by 1 October 2016 and every 5 years | `s 2025(h)(5)(F) the study is conducted in time` (+1 more in the coverage row) |
| s 2025(i)(1) | the Department of Agriculture | privilege | the State agencies | no-right | to use quality control information to find project areas with impairing error rates | `s 2025(i)(1) the Department of Agriculture may use the information to determine which project areas have payment error rates that impair the integrity of the program` |
| s 2025(i)(2) | the Secretary | power | the State agency | liability | to require new or modified certification procedures in those areas | `s 2025(i)(2) the Secretary may require the State agency to carry out new or modified certification procedures` |
| s 2025(j) | not named in the text | claim | the Secretary | duty | to publish training materials by 180 days after 19 September 1988 and annually thereafter (fork F-6) | `s 2025(j) the date by which the instructional materials are due` (+1 more in the coverage row) |
| s 2025(k)(1)(A) | none | - | none | - | definition of the AFDC program | `s 2025(k)(1)(A) the program is the AFDC program` |
| s 2025(k)(1)(B) | none | - | none | - | definition of the base period | `s 2025(k)(1)(B) the period is the base period` |
| s 2025(k)(1)(C) | none | - | none | - | definition of the medicaid program | `s 2025(k)(1)(C) the program is the medicaid program` |
| s 2025(k)(2) | the Secretary of Agriculture | claim | the Secretary of Health and Human Services | duty | to determine, within 180 days after 23 June 1998, the amounts attributable to benefiting programs | `s 2025(k)(2) the date by which the Secretary of Health and Human Services must make the determinations` |
| s 2025(k)(2)(B) | none | - | none | - | the arithmetic of the common-cost allocation | `s 2025(k)(2)(B) the amount of common costs allocated to each program when allocated equally` |
| s 2025(k)(3)(A) | the Secretary | power | the State | liability (reduction of the payment) | to reduce the payment under subsection (a) by the (2)(B) amount, quarterly where practicable | `s 2025(k)(3)(A) the amount paid to the State after the reduction` |
| s 2025(k)(3)(B) | the Secretary | power | the State | liability | the reduction if the determinations are late | `s 2025(k)(3)(B) the determinations were not made by September 30, 1999` |
| s 2025(k)(3)(B)(i) | the Secretary | power | the State | liability | the size of the reduction in the year the determinations are made | `s 2025(k)(3)(B)(i) the amount of the reduction in the fiscal year in which the determinations are made` |
| s 2025(k)(3)(B)(ii) | the Secretary | power | the State | liability | when subparagraph (A) applies after a late determination | `s 2025(k)(3)(B)(ii) subparagraph (A) applies in the fiscal year` |
| s 2025(k)(4)(A) | the State | claim | the Secretary of Health and Human Services | duty | to be notified within 5 days of a determination | `s 2025(k)(4)(A) the last day for the Secretary to notify the chief executive officer of the State` (+2 more in the coverage row) |
| s 2025(k)(4)(B)(i) | the State | power | the Secretary of Health and Human Services | liability (to the appeal) | to appeal to an administrative law judge within 60 days | `s 2025(k)(4)(B)(i) the last day for the State to appeal to an administrative law judge` (+2 more in the coverage row) |
| s 2025(k)(4)(B)(ii) | the State | claim | the administrative law judge | duty | the appeal is reviewed as the clause requires | `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` |
| s 2025(k)(4)(B)(iii) | the State | claim | the administrative law judge | duty | the appeal is reviewed as the clause requires | `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` |
| s 2025(k)(4)(B)(iv) | the State | claim | the administrative law judge | duty | a decision and notice within 60 days after the record closes | `s 2025(k)(4)(B)(iv) the last day for the administrative law judge to decide and notify` (+2 more in the coverage row) |
| s 2025(k)(4)(C)(i) | the State | power | the Departmental Appeals Board | liability | to appeal to the Board within 30 days | `s 2025(k)(4)(C)(i) the last day for the State to appeal to the Departmental Appeals Board` (+2 more in the coverage row) |
| s 2025(k)(4)(C)(ii) | the State | claim | the Board | duty | the decision is reviewed on the record | `s 2025(k)(4)(C)(ii) the Board has reviewed the decision as required` |
| s 2025(k)(4)(C)(iii) | the State | claim | the Board | duty | a final decision and notice within 60 days | `s 2025(k)(4)(C)(iii) the last day for the Board to decide and notify` (+2 more in the coverage row) |
| s 2025(k)(4)(D) | the Secretary of Health and Human Services | immunity | the State | disability | the determination or decision is not subject to judicial review | `s 2025(k)(4)(D) the determination or decision is subject to judicial review` |
| s 2025(k)(4)(E) | the Secretary | immunity | the State | disability | an appeal does not suspend the duty to reduce payments | `s 2025(k)(4)(E) the pendency of the appeal affects the requirement that the Secretary reduce payments` |
| s 2025(k)(5) | the Secretary | claim | the State | duty | the listed funds and expenditures are not used to pay the costs | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` |
| s 2026a(a) | none | - | none | - | a definition of fluid milk (fork F-2) | `s 2026a(a) the product is fluid milk` |
| s 2026a(b) | not named in the text | claim | the Secretary | duty | to carry out healthy fluid milk incentive projects | `s 2026a(b) the project is a healthy fluid milk incentive project the Secretary is to carry out` |
| s 2026a(c)(1) | governmental entities and nonprofit organisations | claim (a competitive one) | the Secretary | duty | to enter into a cooperative agreement or grant for a project that meets the criteria | `s 2026a(c)(1) the Secretary shall enter into the agreement with, or provide the grant to, the entity` |
| s 2026a(c)(2) | the Secretary | power | the applicant | liability (must apply to be eligible) | to require an application with the information the Secretary requires | `s 2026a(c)(2) the entity has met the application requirement` |
| s 2026a(c)(3) | the applicants | claim | the Secretary | duty | evaluation against publicly disseminated criteria | `s 2026a(c)(3) the projects are evaluated against the required criteria` |
| s 2026a(c)(4) | households receiving benefits | immunity | the Secretary and the grantee | disability | the funds are not used for a project that limits the use of benefits | `s 2026a(c)(4) the funds made available under this section may be used for the project` |
| s 2026a(d)(1)(A)(i) | not named in the text | claim | the Secretary | duty | an independent evaluation of selected projects | `s 2026a(d)(1)(A)(i) the evaluation is the independent evaluation required` |
| s 2026a(d)(1)(A)(ii) | not named in the text | claim | the Secretary | duty | the evaluation uses rigorous methodologies | `s 2026a(d)(1)(A)(ii) the evaluation meets the requirement of rigorous methodologies` |
| s 2026a(d)(1)(B) | the Secretary | privilege | none | no-right | to use up to 7 percent of the funding for evaluation | `s 2026a(d)(1)(B) the amount used for evaluation is within the limit` |
| s 2026a(d)(2) | the Committees on Agriculture | claim | the Secretary | duty | a report by 31 December 2020 and every two years after | `s 2026a(d)(2) the date by which the report is due in the year` (+2 more in the coverage row) |
| s 2026a(d)(3) | the public | claim | the Secretary | duty | evaluation results are shared publicly | `s 2026a(d)(3) the evaluation results are shared as required` |
| s 2026a(e)(1) | none | - | none | - | an authorisation of $20,000,000, available until expended | `s 2026a(e)(1) the amount authorized to be appropriated, in dollars` |
| s 2026a(e)(2) | the Secretary | immunity | the grantee | disability | only funds appropriated in advance for this section are available for it | `s 2026a(e)(2) the funds are available to carry out this section` |
| s 2028(a)(1) | none | - | none | - | a definition of governmental entity | `s 2028(a)(1) the place is a governmental entity` |
| s 2028(a)(2)(A) | the governmental entities | claim | the Secretary | duty (subject to the section) | $1,401,000,000 for fiscal year 2003 | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` |
| s 2028(a)(2)(A)(ii) | the governmental entities | claim | the Secretary | duty (subject to appropriations; fork F-15) | the amount adjusted by the percentage the thrifty food plan has changed | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` |
| s 2028(a)(2)(B)(i) | the Commonwealth of Puerto Rico | claim | the Secretary | duty | 99.6 percent of the funds: 100 percent of the expenditures under its approved plan and 50 percent of the related administrative expenses | `s 2028(a)(2)(B)(i) the Commonwealth's share of the funds` (+1 more in the coverage row) |
| s 2028(a)(2)(B)(ii) | the Commonwealth | privilege | the Secretary | no-right | to spend up to $6,000,000 in fiscal year 2002 or 2003 on the systems named | `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` |
| s 2028(a)(2)(C) | American Samoa | claim | the Secretary | duty | 0.4 percent of the funds, to pay 100 percent of its expenditures | `s 2028(a)(2)(C) American Samoa's share of the funds` (+1 more in the coverage row) |
| s 2028(a)(2)(D) | each governmental entity | privilege | the Secretary | no-right | to carry over up to 2 percent to the next fiscal year | `s 2028(a)(2)(D) the carryover is within the limit` |
| s 2028(a)(3) | the Commonwealth | claim | the Secretary | duty | to be paid the estimated amount, adjusted for prior overpayment or underpayment | `s 2028(a)(3) the payment to the Commonwealth for the fiscal year` |
| s 2028(b)(1)(A) | the Secretary | claim | the Commonwealth | duty (a plan by 1 July, to receive payments) | to receive a plan with the stated contents | `s 2028(b)(1) the Commonwealth may receive payments` |
| s 2028(b)(1)(B)(i) | the Commonwealth | claim | the Secretary | duty | to have the plan approved or disapproved by 1 August, and approved if it complies | `s 2028(b)(1)(B)(i) the Secretary's decision on the plan is in time` (+3 more in the coverage row) |
| s 2028(b)(1)(B)(ii) | the Secretary | power | the Commonwealth | liability | to withhold payments instead of denying them, until satisfied | `s 2028(b)(1)(B)(ii) the withheld payments are to be paid` |
| s 2028(b)(2)(A) | the Secretary | claim | the Commonwealth | duty | a biennial audit, reported within 120 days (fork F-1) | `s 2028(b)(2)(A) the last day for the report of the audit findings` (+3 more in the coverage row) |
| s 2028(b)(2)(B) | the Secretary | claim | the Commonwealth | duty | a statement within 120 days of the end of the fiscal year | `s 2028(b)(2)(B) the statement is provided in time` (+2 more in the coverage row) |
| s 2028(b)(2)(C)(i) | the Secretary | power | the Commonwealth | liability | on a finding of substantial failure, to terminate payments | `s 2028(b)(2)(C)(i) further payments may be made` |
| s 2028(b)(2)(C)(ii) | the Secretary | power | the Commonwealth | liability | to suspend termination and withhold payments instead | `s 2028(b)(2)(C)(ii) the withheld payments are to be paid` |
| s 2028(b)(2)(C)(iii) | the Secretary | power | the Commonwealth | liability | to refer the matter to the Attorney General for injunctive relief | `s 2028(b)(2)(C)(iii) the Secretary may refer the matter to the Attorney General` (+1 more in the coverage row) |
| s 2028(c)(1) | not named in the text | claim | the Secretary | duty | to review the programs | `s 2028(c)(1) the Secretary shall provide for the review of the program` |
| s 2028(c)(2) | the Commonwealth and American Samoa | no-right | the Secretary | privilege | technical assistance is at the Secretary's discretion | `s 2028(c)(2) the Secretary may provide technical assistance` |
| s 2028(d) | the United States | power | any person who knowingly and willfully embezzles, misapplies, steals or obtains the funds by fraud | liability (fine up to $10,000 or imprisonment up to five years; lower penalty if the value is $200 or less) | to punish | `s 2028(d) the conduct is within the offence` (+2 more in the coverage row) |
| s 2028(e)(1) | not named in the text | claim | the Secretary | duty | to carry out a review with the Secretary of Health and Human Services | `s 2028(e)(1) the review includes the required examinations` |
| s 2028(e)(2) | the Committees on Agriculture | claim | the Secretary | duty | a report not later than 18 months after 7 February 2014 | `s 2028(e)(2) the last day for the report` (+1 more in the coverage row) |
| s 2028(e)(3)(A) | the Secretary | power | the Commonwealth | liability (a plan above the cash share is disapproved) | to disapprove a plan that distributes more than 20, 15, 10, 5 or 0 percent in cash in fiscal years 2017 to 2021 | `s 2028(e)(3)(A) the largest share of a participant's benefit a plan may distribute in cash` (+1 more in the coverage row) |
| s 2028(e)(3)(B) | the Secretary | power | the Commonwealth | liability | to approve a plan that exempts participants, if discontinuation of cash would have significant adverse effects | `s 2028(e)(3)(B) the Secretary may approve a plan that exempts participants or categories of participants` |
| s 2028(e)(4) | none | - | none | - | the Secretary makes $1,000,000 available out of section 2027 funds for the review and report | `s 2028(e)(4) the amount to make available for the review and report` |

## Marginal readings for a lawyer (snap5)

The rule of 2026-10-29 (assumed, not ruled by a lawyer) has two readings the brief flags for a lawyer, not for the encoder to decide: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not count as a no.
I took both as the status quo.
This section lists every branch that rests on either, with the other reading.
The class names are mine, assigned by the words each branch rests on (a lawyer may well sort them differently), and the generator that built the tables is kept with the work files.

Counts in the modules and the seat as filed: 156 FALSE-kind branches (6 are closed definitions that say "means", listed below as not marginal), 166 NOTHING-kind branches (110 of them "limited by its own wording").

### Reading (a): a branch answered FALSE because a condition, limit or duty in the text was not met, or because of a flat negative

Each row is a `-- FALSE-kind` comment in the named file. The class says which kind of (a) it rests on; the other reading of each class is stated under the table.

| # | class | function | file:line | the words the branch rests on |
| --- | --- | --- | --- | --- |
| 1 | A-neg | `s 2025(a) the official may receive or benefit from the revenues retained by the State` | snap5-s2025-ab.l4:121 | "shall not receive or benefit from revenues retained by the State under the provisions of this subsection" |
| 2 | A-neg | `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` | snap5-s2025-ab.l4:224 | "the household shall not receive an allotment from the State agency for the period during which the member continues to participate" |
| 3 | A-neg | `s 2025(b)(4) the individual is excused from a work requirement under section 2015(d) by reason of the fact that the S...` | snap5-s2025-ab.l4:242 | "No individual shall be excused, by reason of the fact that a State has a work supplementation or support program, from any work requirement under section 2015(d)" |
| 4 | A-neg | `s 2025(b)(6) the work supplementation or support program is permitted` | snap5-s2025-ab.l4:262 | "A work supplementation or support program shall not displace the employment of individuals who are not supplemented or supported" |
| 5 | A-neg | `s 2025(c)(1)(D)(i)(I) the new investment amount may be matched by Federal funds` | snap5-s2025-c1.l4:151 | "which new investment amount shall not be matched by Federal funds" |
| 6 | A-neg | `s 2025(c)(1)(E)(ii)(II)(bb) interest accrues on the payment under section 2022(a)(2)` | snap5-s2025-c1.l4:243 | "During any period of time determined by the Secretary under item (aa), interest on the payment under subclause (I) shall not accrue" |
| 7 | A-neg | `s 2025(c)(6)(D) the national performance measure is subject to administrative or judicial review` | snap5-s2025-c2.l4:182 | "shall not be subject to administrative or judicial review" |
| 8 | A-neg | `s 2025(c)(7)(C) the action is subject to administrative or judicial review` | snap5-s2025-c2.l4:218 | "shall not be subject to administrative or judicial review" |
| 9 | A-neg | `s 2025(d)(3) the State agency is eligible for a performance bonus payment for the fiscal year` | snap5-s2025-dfij.l4:140 | "A State agency shall not be eligible for a performance bonus payment with respect to any fiscal year for which the State agency has a liability amount established und... |
| 10 | A-neg | `s 2025(d)(4) the determination is subject to administrative or judicial review` | snap5-s2025-dfij.l4:151 | "shall not be subject to administrative or judicial review" |
| 11 | A-neg | `s 2025(d)(6)(B) the Secretary may award performance bonus payments` | snap5-s2025-dfij.l4:176 | "The Secretary shall not award performance bonus payments to State agencies in fiscal year 2019 for fiscal year 2018 performance" |
| 12 | A-neg | `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to the evaluation of subparagraph (F)(vii)` | snap5-s2025-gh.l4:258 | "Employment and training activities funded under this subclause are not subject to subparagraph (F)(vii)" |
| 13 | A-neg | `s 2025(h)(3) the reimbursement may be made out of funds allocated under paragraph (1)` | snap5-s2025-gh.l4:427 | "such reimbursement shall not be made out of funds allocated under paragraph (1)" |
| 14 | A-neg | `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` | snap5-s2025-hf.l4:361 | "failure to work for reasons beyond the control of an individual, such as involuntary reduction in hours of employment, shall not result in ineligibility" |
| 15 | A-neg | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` | snap5-s2025-hf.l4:386 | "shall not result in ineligibility" |
| 16 | A-neg | `s 2025(k)(4)(D) the determination or decision is subject to judicial review` | snap5-s2025-k.l4:277 | "shall not be subject to judicial review" |
| 17 | A-neg | `s 2025(k)(4)(E) the pendency of the appeal affects the requirement that the Secretary reduce payments` | snap5-s2025-k.l4:288 | "The pendency of an appeal under this paragraph shall not affect the requirement that the Secretary reduce payments in accordance with paragraph (3)" |
| 18 | A-neg | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` | snap5-s2025-k.l4:319 | "No funds or expenditures described in subparagraph (B) may be used to pay for costs" |
| 19 | A-neg | `s 2026a(c)(4) the funds made available under this section may be used for the project` | snap5-s2026a.l4:109 | "shall not be used for any project that limits the use of benefits" |
| 20 | A-if | `s 2025(a) the share of recovered or collected funds the Secretary may permit the State to retain` | snap5-s2025-ab.l4:98 | "20 percent of the value of any other funds or allotments recovered or collected, except the value of funds or allotments recovered or collected that arise from an err... |
| 21 | A-if | `s 2025(a) the amount of the claim the State may be permitted to retain, in dollars` | snap5-s2025-ab.l4:112 | "except the value of funds or allotments recovered or collected that arise from an error of a State agency" |
| 22 | A-if | `s 2025(b)(1) the program is a work supplementation or support program` | snap5-s2025-ab.l4:142 | "as determined by the Secretary" |
| 23 | A-if | `s 2025(b)(3) the procedure applies` | snap5-s2025-ab.l4:165 | "If a State agency makes an election under paragraph (2) and identifies each household" |
| 24 | A-if | `s 2025(c)(1)(D)(ii) the settlement with the State agency is permitted` | snap5-s2025-c1.l4:191 | "enter into a settlement with the State agency, only with respect to any new investment amount, before the end of the fiscal year" |
| 25 | A-if | `s 2025(c)(1)(E)(i) the State agency shall pay the at-risk amount to the Secretary` | snap5-s2025-c1.l4:203 | "if, with respect to the immediately following fiscal year, a liability amount has been established for the State agency under subparagraph (C)" |
| 26 | A-if | `s 2025(c)(7)(B) the determination is subject to administrative or judicial review` | snap5-s2025-c2.l4:209 | "shall be subject to administrative or judicial review only if the Secretary establishes a liability amount with respect to the fiscal year" |
| 27 | A-if | `s 2025(d)(5) the State agency may use the performance bonus payment for the use` | snap5-s2025-dfij.l4:165 | "may use a performance bonus payment received under this subsection only to carry out the program established under this chapter" |
| 28 | A-if | `s 2025(e) the Secretary and State agencies shall have access to the information` | snap5-s2025-dfij.l4:216 | "but only to the extent that the Secretary and the Commissioner of Social Security determine necessary for purposes of determining or auditing a household's eligibility" |
| 29 | A-if | `s 2025(i)(2) the Secretary may require the State agency to carry out new or modified certification procedures` | snap5-s2025-dfij.l4:268 | "if the Secretary determines such procedures would improve the integrity of the supplemental nutrition assistance program and be cost effective" |
| 30 | A-if | `s 2025(h)(1)(C)(iv)(I)(bb) the determination is based on what the text requires` | snap5-s2025-gh.l4:249 | "if the project results from the independent evaluations conducted under subparagraph (F)(vii)(I) are not yet available, the reports under subparagraph (F)(vii)(II) or... |
| 31 | A-if | `s 2025(h)(1)(E)(ii) the State agency is eligible for an additional allocation` | snap5-s2025-gh.l4:367 | "To be eligible for an additional allocation under clause (i), a State agency shall make and comply with a commitment to offer a position" |
| 32 | A-if | `s 2025(h)(4) the funds may be used for the use` | snap5-s2025-gh.l4:440 | "may be used only for operating an employment and training program under section 2015(d)(4) of this title or a pilot project under paragraph (1)(F), and may not be use... |
| 33 | A-if | `s 2025(h)(5)(E) the Secretary may require the State agency to modify the plan` | snap5-s2025-gh.l4:578 | "if the Secretary determines that the performance of a State agency with respect to employment and training outcomes is inadequate" |
| 34 | A-if | `s 2025(h)(1)(F)(ii)(II) the State agency meets the qualifying criteria` | snap5-s2025-hf.l4:69 | "To be eligible to participate in a pilot project, a State agency shall" |
| 35 | A-if | `s 2025(h)(1)(F)(vi)(III) the State agency complied before assigning the work registrant to mandatory activities` | snap5-s2025-hf.l4:420 | "if determined to be acceptable, count hours engaged in the activities toward any minimum participation requirement" |
| 36 | A-if | `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year` | snap5-s2025-hf.l4:477 | "each December 31 thereafter until the completion of the last evaluation under subclause (I)" |
| 37 | A-if | `s 2025(h)(1)(F)(ix)(I) the funds may be used for the use` | snap5-s2025-hf.l4:597 | "Funds made available under this subparagraph for pilot projects shall be used only for" |
| 38 | A-if | `s 2025(h)(1)(F)(ix)(II) the funds are used as the text allows` | snap5-s2025-hf.l4:608 | "shall be used only to supplement, not to supplant, non-Federal funds" |
| 39 | A-if | `s 2025(h)(1)(F)(ix)(III) the State may contribute the additional funds` | snap5-s2025-hf.l4:618 | "on the condition that the use of the contributions is permissible under Federal law" |
| 40 | A-if | `s 2025(k)(3)(B) the determinations were not made by September 30, 1999` | snap5-s2025-k.l4:122 | "If the Secretary of Health and Human Services does not make the determinations required by paragraph (2) by September 30, 1999" |
| 41 | A-if | `s 2026a(c)(2) the entity has met the application requirement` | snap5-s2026a.l4:89 | "To be eligible to enter into a cooperative agreement or receive a grant under this subsection, a government entity or nonprofit organization shall submit to the Secre... |
| 42 | A-if | `s 2028(b)(1)(B)(i) payments may be made for the fiscal year of the plan` | snap5-s2028.l4:242 | "payments will not be made to it under subsection (a) for the fiscal year to which the plan applies until the Secretary is satisfied" |
| 43 | A-if | `s 2028(b)(1)(B)(ii) the withheld payments are to be paid` | snap5-s2028.l4:255 | "withhold payments provided for under subsection (a), in whole or in part, for the fiscal year to which the plan applies, until the Secretary is satisfied" |
| 44 | A-if | `s 2028(b)(2)(C)(i) further payments may be made` | snap5-s2028.l4:326 | "further payments will not be made to it under subsection (a) until the Secretary is satisfied that there will no longer be any such failure to comply" |
| 45 | A-if | `s 2028(b)(2)(C)(ii) the withheld payments are to be paid` | snap5-s2028.l4:339 | "withhold payments provided for under subsection (a), in whole or in part, until the Secretary is satisfied" |
| 46 | A-if | `s 2028(e)(3)(B) the Secretary may approve a plan that exempts participants or categories of participants` | snap5-s2028.l4:504 | "if the Secretary determines that discontinuation of benefits in the form of cash is likely to have significant adverse effects" |
| 47 | A-if | `Under section 2025(a), what share of the money recovered or collected from my household may the State keep` | snap5-seat.l4:53 | "except the value of funds or allotments recovered or collected that arise from an error of a State agency" |
| 48 | A-limit | `s 2025(b)(5) the State agency has provided the description required` | snap5-s2025-ab.l4:253 | "A State agency shall provide a description of how the public assistance recipients in the program shall, within a specific period of time, be moved" |
| 49 | A-limit | `s 2025(c)(1)(A)(ii)(I) the tolerance level set is within the limit` | snap5-s2025-c1.l4:31 | "for fiscal year 2014, at an amount not greater than $37" |
| 50 | A-limit | `s 2025(c)(1)(B)(i) the interim final regulations are issued in time` | snap5-s2025-c1.l4:62 | "Not later than 180 days after December 20, 2018, the Secretary shall issue interim final regulations" |
| 51 | A-limit | `s 2025(c)(1)(D)(i)(I) the portion required for new investment is within the limit` | snap5-s2025-c1.l4:143 | "a portion, not to exceed 50 percent, of the liability amount established for the fiscal year be used by the State agency for new investment" |
| 52 | A-limit | `s 2025(c)(1)(D)(i)(II) the portion designated as the at-risk amount is within the limit` | snap5-s2025-c1.l4:164 | "designate a portion, not to exceed 50 percent, of the amount established for the fiscal year for payment to the Secretary" |
| 53 | A-limit | `s 2025(c)(1)(D)(i)(III) the combination of actions is allowed` | snap5-s2025-c1.l4:178 | "take any combination of the actions described in subclauses (I) and (II)", each portion "not to exceed 50 percent" |
| 54 | A-limit | `s 2025(c)(5) the collection efforts are initiated in time` | snap5-s2025-c2.l4:137 | "before the end of the fiscal year following such fiscal year" |
| 55 | A-limit | `s 2025(c)(8)(B) the case review and arbitrations are completed in time` | snap5-s2025-c2.l4:251 | "Not later than the first May 31 after the end of the fiscal year" |
| 56 | A-limit | `s 2025(c)(8)(C)(i) the final error rates are determined in time` | snap5-s2025-c2.l4:271 | "Not later than the first June 30 after the end of the fiscal year referred to in subparagraph (A), the Secretary shall— (i) determine final error rates" |
| 57 | A-limit | `s 2025(c)(8)(C)(ii) the State agencies are notified in time` | snap5-s2025-c2.l4:282 | "Not later than the first June 30 after the end of the fiscal year referred to in subparagraph (A), the Secretary shall— (i) determine final error rates, the national ... |
| 58 | A-limit | `s 2025(c)(8)(D)(i) the notice of appeal is submitted in time` | snap5-s2025-c2.l4:333 | "a notice of appeal, not later than 10 days after receiving a notice of the claim or liability amount" |
| 59 | A-limit | `s 2025(c)(8)(D)(ii) the evidence in support of the appeal is submitted in time` | snap5-s2025-c2.l4:345 | "evidence in support of the appeal of the State agency, not later than 60 days after receiving a notice of the claim or liability amount" |
| 60 | A-limit | `s 2025(c)(8)(E) the responsive evidence is submitted in time` | snap5-s2025-c2.l4:360 | "Not later than 60 days after a State agency submits evidence in support of the appeal, the Secretary shall submit responsive evidence" |
| 61 | A-limit | `s 2025(c)(8)(F) the rebuttal evidence is submitted in time` | snap5-s2025-c2.l4:375 | "Not later than 30 days after the Secretary submits responsive evidence, the State agency shall submit rebuttal evidence" |
| 62 | A-limit | `s 2025(c)(8)(G) the appeal is decided in time` | snap5-s2025-c2.l4:402 | "shall decide the appeal— (i) not later than 60 days after receipt of rebuttal evidence submitted by the State agency; or (ii) if the State agency does not submit rebu... |
| 63 | A-limit | `s 2025(d)(1)(A) the guidance is issued in time` | snap5-s2025-dfij.l4:26 | "in guidance issued to State agencies not later than October 1, 2002" |
| 64 | A-limit | `s 2025(j) the instructional materials are published as required` | snap5-s2025-dfij.l4:299 | "Not later than 180 days after September 19, 1988, and annually thereafter, the Secretary shall publish instructional materials" |
| 65 | A-limit | `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` | snap5-s2025-gh.l4:73 | "(v) would be tested adequately before and after implementation" |
| 66 | A-limit | `s 2025(g)(1)(A)(v) the system would be tested adequately before and after implementation` | snap5-s2025-gh.l4:102 | "would be tested adequately before and after implementation, including a requirement that" |
| 67 | A-limit | `s 2025(h)(1)(C)(ii) the reallocation allows the State agency the time required` | snap5-s2025-gh.l4:208 | "within a timeframe that allows each State agency to which funds are reallocated at least 270 days to expend the reallocated funds" |
| 68 | A-limit | `s 2025(h)(1)(C)(iv)(I) the amount reallocated under subclause (I) meets the minimum` | snap5-s2025-gh.l4:229 | "not less than 50 percent shall be reallocated to State agencies requesting such funds" |
| 69 | A-limit | `s 2025(h)(1)(C)(iv)(II) the amount reallocated under subclause (II) meets the minimum` | snap5-s2025-gh.l4:280 | "Not less than 30 percent shall be reallocated to State agencies requesting such funds" |
| 70 | A-limit | `s 2025(h)(1)(D) the allocation meets the minimum` | snap5-s2025-gh.l4:328 | "shall receive not less than $100,000 for each fiscal year" |
| 71 | A-limit | `s 2025(h)(1)(E)(i) the additional allocation is within the limit` | snap5-s2025-gh.l4:338 | "the Secretary shall allocate not more than $20,000,000 for each fiscal year" |
| 72 | A-limit | `s 2025(h)(5)(B)(iii) the threshold the Secretary determines is allowed` | snap5-s2025-gh.l4:484 | "a threshold number of participants determined by the Secretary of at least 100 people a year" |
| 73 | A-limit | `s 2025(h)(5)(F) the study is conducted in time` | snap5-s2025-gh.l4:595 | "not later than October 1, 2016, and not less frequently than once every 5 years thereafter" |
| 74 | A-limit | `s 2025(h)(5)(F) the study is conducted in time` | snap5-s2025-gh.l4:600 | "not later than October 1, 2016" |
| 75 | A-limit | `s 2025(h)(1)(F)(ii)(II)(cc) the commitment is at least the amount expended for fiscal year 2013` | snap5-s2025-hf.l4:80 | "commit to maintain at least the amount of State funding" |
| 76 | A-limit | `s 2025(h)(1)(F)(iii)(II) the time period allowed to correct the noncompliance is as required` | snap5-s2025-hf.l4:148 | "The process shall include a reasonable time period, not to exceed 180 days" |
| 77 | A-limit | `s 2025(h)(1)(F)(vi)(III) the State agency complied before assigning the work registrant to mandatory activities` | snap5-s2025-hf.l4:418 | "Before assigning a work registrant to mandatory employment and training activities, a State agency shall— (aa) assess" |
| 78 | A-limit | `s 2025(h)(1)(F)(vii)(I)(aa) the reporting of results is frequent enough` | snap5-s2025-hf.l4:445 | "with results reported not less frequently than in consecutive 12-month increments" |
| 79 | A-limit | `s 2025(h)(1)(F)(vii)(II) the report is submitted in time` | snap5-s2025-hf.l4:488 | "Not later than December 31, 2015, and each December 31 thereafter" |
| 80 | A-limit | `s 2025(h)(1)(F)(viii)(II)(aa) the number of funded pilot projects is within the limit` | snap5-s2025-hf.l4:555 | "The Secretary shall not fund more than 10 pilot projects under this subparagraph" |
| 81 | A-limit | `s 2025(h)(1)(F)(viii)(II)(bb) the pilot project is in effect for no more than the limit` | snap5-s2025-hf.l4:567 | "Each pilot project shall be in effect for not more than 3 years" |
| 82 | A-limit | `s 2025(k)(2) the determinations are made as required` | snap5-s2025-k.l4:76 | "Not later than 180 days after June 23, 1998, the Secretary of Health and Human Services, in consultation with the Secretary of Agriculture and the States, shall" |
| 83 | A-limit | `s 2025(k)(4)(A) the Secretary notifies the chief executive officer in time` | snap5-s2025-k.l4:164 | "Not later than 5 days after the date on which the Secretary of Health and Human Services makes any determination required by paragraph (2) with respect to a State, th... |
| 84 | A-limit | `s 2025(k)(4)(B)(i) the State may appeal the determination` | snap5-s2025-k.l4:181 | "Not later than 60 days after the date on which a State receives notice under subparagraph (A) of a determination, the State may appeal the determination" |
| 85 | A-limit | `s 2025(k)(4)(B)(iv) the administrative law judge decides and notifies in time` | snap5-s2025-k.l4:217 | "Not later than 60 days after the date on which the record is closed, the administrative law judge shall— (I) make a final decision with respect to an appeal filed und... |
| 86 | A-limit | `s 2025(k)(4)(C)(i) the State may appeal the decision` | snap5-s2025-k.l4:234 | "Not later than 30 days after the date on which a State receives notice under subparagraph (B) of a final decision, the State may appeal the decision" |
| 87 | A-limit | `s 2025(k)(4)(C)(iii) the Board decides and notifies in time` | snap5-s2025-k.l4:266 | "Not later than 60 days after the date on which the appeal is filed, the Board shall— (I) make a final decision with respect to an appeal filed under clause (i); and (... |
| 88 | A-limit | `s 2026a(d)(1)(B) the amount used for evaluation is within the limit` | snap5-s2026a.l4:145 | "not to exceed 7 percent of the funding provided to carry out this section" |
| 89 | A-limit | `s 2026a(d)(2) the report is submitted in time` | snap5-s2026a.l4:168 | "Not later than December 31 of 2020, and biennially thereafter" |
| 90 | A-limit | `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` | snap5-s2028.l4:109 | "not more than $6,000,000" |
| 91 | A-limit | `s 2028(a)(2)(D) the carryover is within the limit` | snap5-s2028.l4:146 | "not more than 2 percent of the funds" |
| 92 | A-limit | `s 2028(b)(1)(A) the plan is submitted in time` | snap5-s2028.l4:186 | "By July 1 of each year" |
| 93 | A-limit | `s 2028(b)(1)(B)(i) the Secretary's decision on the plan is in time` | snap5-s2028.l4:221 | "no later than August 1 of the year in which it is submitted" |
| 94 | A-limit | `s 2028(b)(2)(A) the report of the audit findings is in time` | snap5-s2028.l4:276 | "within 120 days of the end of each fiscal year in which the audit is made" |
| 95 | A-limit | `s 2028(b)(2)(B) the statement is provided in time` | snap5-s2028.l4:298 | "Within 120 days of the end of the fiscal year, the Commonwealth shall provide the Secretary with a statement" |
| 96 | A-limit | `s 2028(b)(2)(B) the statement has the required contents` | snap5-s2028.l4:313 | "a statement as to whether the payments received under subsection (a) for that fiscal year exceeded the expenditures" |
| 97 | A-limit | `s 2028(e)(2) the report is in time` | snap5-s2028.l4:461 | "Not later than 18 months after February 7, 2014" |
| 98 | A-duty | `s 2025(a) the cost is an administrative cost the Secretary is authorized to pay a share of` | snap5-s2025-ab.l4:62 | "but not including recruitment activities designed to persuade an individual to apply for program benefits or that promote the program through television, radio, or bi... |
| 99 | A-duty | `s 2025(b)(3)(B) the State agency has expended the amount as required` | snap5-s2025-ab.l4:190 | "the State agency shall expend the amount received under subparagraph (A) in accordance with the work supplementation or support program" |
| 100 | A-duty | `s 2025(c)(1)(A)(i) the Secretary's quality control system is the system required` | snap5-s2025-c1.l4:20 | "the Secretary shall carry out a system that enhances payment accuracy and improves administration by establishing fiscal incentives" |
| 101 | A-duty | `s 2025(c)(1)(B)(i) the interim final regulations have the content required` | snap5-s2025-c1.l4:82 | "the Secretary shall issue interim final regulations that" |
| 102 | A-duty | `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency` | snap5-s2025-c1.l4:111 | "any fiscal year thereafter for which the Secretary determines that, for the second or subsequent consecutive fiscal year, a 95 percent statistical probability exists" |
| 103 | A-duty | `s 2025(c)(1)(F)(iii) the new investment amount is divided as required` | snap5-s2025-c1.l4:297 | "require all or any portion of the new investment amount to be used by the State agency for new investment" and "require payment of any remaining portion of the new in... |
| 104 | A-duty | `s 2025(c)(1)(G) the State agency is required to develop and implement a corrective action plan` | snap5-s2025-c1.l4:309 | "other than State agencies with payment error rates of less than 6 percent" |
| 105 | A-duty | `s 2025(c)(5) the State agency has submitted the data as required` | snap5-s2025-c2.l4:124 | "each State agency shall expeditiously submit to the Secretary data concerning the operations of the State agency in each fiscal year" |
| 106 | A-duty | `s 2025(c)(8)(C)(iii) the copy is provided in time to the chief executive officer and the legislature` | snap5-s2025-c2.l4:298 | "provide a copy of the document providing notification under clause (ii) to the chief executive officer and the legislature of the State" |
| 107 | A-duty | `s 2025(c)(8)(H) the administrative law judge has considered what the text requires` | snap5-s2025-c2.l4:416 | "the administrative law judge shall consider all grounds for denying the claim or liability amount, in whole or in part, including the contention of a State agency tha... |
| 108 | A-duty | `s 2025(d)(1)(A) the guidance has the content required` | snap5-s2025-dfij.l4:44 | "the Secretary shall establish, in guidance issued to State agencies" |
| 109 | A-duty | `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:59 | "the Secretary shall— (i) measure the performance of each State agency" |
| 110 | A-duty | `s 2025(d)(1)(B)(ii) the State agency shall be awarded a performance bonus payment` | snap5-s2025-dfij.l4:84 | "award performance bonus payments in the following fiscal year" |
| 111 | A-duty | `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:102 | "the Secretary shall— (i) measure the performance of each State agency" |
| 112 | A-duty | `s 2025(d)(2)(B)(ii) the State agency shall be awarded a performance bonus payment` | snap5-s2025-dfij.l4:127 | "award performance bonus payments in the following fiscal year" |
| 113 | A-duty | `s 2025(e)(1) the household member has met the condition of eligibility of furnishing a social security account number` | snap5-s2025-dfij.l4:193 | "require, as a condition of eligibility for participation in the supplemental nutrition assistance program, that each household member furnish to the State agency thei... |
| 114 | A-duty | `s 2025(e)(2) the account numbers are used in the administration of the program` | snap5-s2025-dfij.l4:203 | "The Secretary and State agencies shall ... (2) use such account numbers in the administration of the supplemental nutrition assistance program" |
| 115 | A-duty | `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` | snap5-s2025-gh.l4:66 | "automatic data processing and information retrieval systems that the Secretary determines— (i) would assist in meeting the requirements of this chapter" |
| 116 | A-duty | `s 2025(g)(1)(A) the planning, design, development or installation of the system qualifies for payment` | snap5-s2025-gh.l4:80 | "systems that the Secretary determines" |
| 117 | A-duty | `s 2025(g)(1)(A)(vi) the system would be operated in accordance with an adequate plan` | snap5-s2025-gh.l4:116 | "would be operated in accordance with an adequate plan for" |
| 118 | A-duty | `s 2025(g)(1)(B) the operation of the system qualifies for payment` | snap5-s2025-gh.l4:126 | "systems that the Secretary determines may continue to be operated in accordance with clauses (i) through (vii)" |
| 119 | A-duty | `s 2025(h)(1)(B) the allocation is made under a formula of the kind required` | snap5-s2025-gh.l4:187 | "shall be made available to and reallocated among State agencies under a reasonable formula that" |
| 120 | A-duty | `s 2025(h)(1)(C)(iii) every State agency has had an opportunity to obtain reallocated funds` | snap5-s2025-gh.l4:218 | "The Secretary shall ensure that all State agencies have an opportunity to obtain reallocated funds" |
| 121 | A-duty | `s 2025(h)(1)(C)(iv)(I)(bb) the determination is based on what the text requires` | snap5-s2025-gh.l4:244 | "The Secretary shall base the determination under item (aa) on— (AA) project results from the independent evaluations" |
| 122 | A-duty | `s 2025(h)(5)(A) the Secretary has monitored and assessed as required` | snap5-s2025-gh.l4:453 | "The Secretary shall monitor the employment and training programs carried out by State agencies under section 2015(d)(4) of this title and assess the effectiveness of ... |
| 123 | A-duty | `s 2025(h)(5)(B) the State reporting measures are as required` | snap5-s2025-gh.l4:474 | "The Secretary, in consultation with the Secretary of Labor, shall develop State reporting measures" |
| 124 | A-duty | `s 2025(h)(5)(C) the Secretary has assessed the State programs as required` | snap5-s2025-gh.l4:542 | "The Secretary shall assess State employment and training programs on a periodic basis to ensure" |
| 125 | A-duty | `s 2025(h)(5)(D) the State agency has reported as required` | snap5-s2025-gh.l4:568 | "Each State agency shall annually prepare and submit to the Secretary a report on the State employment and training program" |
| 126 | A-duty | `s 2025(h)(5)(F) the study covers what the text requires` | snap5-s2025-gh.l4:617 | "the Secretary shall conduct a study to review existing practice and research to identify employment and training program components and practices that" |
| 127 | A-duty | `s 2025(h)(1)(F)(i)(I) the Secretary has carried out the pilot projects as required` | snap5-s2025-hf.l4:20 | "The Secretary shall carry out pilot projects under which State agencies shall enter into cooperative agreements with the Secretary" |
| 128 | A-duty | `s 2025(h)(1)(F)(i)(II) the pilot project meets the requirements` | snap5-s2025-hf.l4:34 | "Pilot projects shall— (aa) meet such terms and conditions as the Secretary considers to be appropriate" |
| 129 | A-duty | `s 2025(h)(1)(F)(ii)(I) the Secretary has selected the pilot project as required` | snap5-s2025-hf.l4:47 | "The Secretary shall select pilot projects under this subparagraph in accordance with the criteria established under this clause and additional criteria established by... |
| 130 | A-duty | `s 2025(h)(1)(F)(ii)(III) the Secretary has considered the factors in selecting the pilot project` | snap5-s2025-hf.l4:101 | "In selecting pilot projects, the Secretary shall— (aa) consider the degree to which the pilot project would enhance existing employment and training programs in the S... |
| 131 | A-duty | `s 2025(h)(1)(F)(ii)(III)(ee) the Secretary has ensured that the group of pilot projects tests the strategies` | snap5-s2025-hf.l4:124 | "ensure the pilot projects, when considered as a group, test a range of strategies, including strategies that" |
| 132 | A-duty | `s 2025(h)(1)(F)(iii)(I) the Secretary has established and implemented the termination process` | snap5-s2025-hf.l4:137 | "The Secretary shall establish and implement a process to terminate a pilot project" |
| 133 | A-duty | `s 2025(h)(1)(F)(vi)(II) the Secretary has established the standards` | snap5-s2025-hf.l4:373 | "The Secretary shall establish standards for employment activities described in subclauses (I), (II), and (III) of clause (iv) that ensure" |
| 134 | A-duty | `s 2025(h)(1)(F)(vii)(I) the Secretary has conducted the independent evaluation as required` | snap5-s2025-hf.l4:434 | "The Secretary shall, under such terms and conditions as the Secretary determines to be appropriate, conduct for each State agency that enters into a cooperative agree... |
| 135 | A-duty | `s 2025(h)(1)(F)(vii)(I)(cc) the evaluation uses the methodology required` | snap5-s2025-hf.l4:459 | "The independent evaluation shall use valid statistical methods" |
| 136 | A-duty | `s 2025(h)(1)(F)(vii)(II) the report is submitted and shared as required` | snap5-s2025-hf.l4:499 | "the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate and... |
| 137 | A-duty | `s 2025(h)(1)(F)(vii)(II) the report describes what is required` | snap5-s2025-hf.l4:530 | "a report that includes a description of— (aa) the status of each pilot project" |
| 138 | A-duty | `s 2025(k)(3)(A) the reductions are made on a quarterly basis as required` | snap5-s2025-k.l4:110 | "The Secretary shall, to the extent practicable, make the reductions required by this paragraph on a quarterly basis" |
| 139 | A-duty | `s 2025(k)(4)(B) the administrative law judge has reviewed the appeal as required` | snap5-s2025-k.l4:195 | "The administrative law judge shall consider an appeal filed by a State under clause (i) on the basis of such documentation" |
| 140 | A-duty | `s 2025(k)(4)(C)(ii) the Board has reviewed the decision as required` | snap5-s2025-k.l4:244 | "The Board shall review the decision on the record" |
| 141 | A-duty | `s 2026a(c)(3) the projects are evaluated against the required criteria` | snap5-s2026a.l4:100 | "Projects proposed in applications shall be evaluated against publicly disseminated criteria that shall incorporate a scientifically based strategy" |
| 142 | A-duty | `s 2026a(d)(1)(A)(i) the evaluation is the independent evaluation required` | snap5-s2026a.l4:124 | "The Secretary shall provide for an independent evaluation of projects selected under this section that measures, to the maximum extent practicable, the impact on heal... |
| 143 | A-duty | `s 2026a(d)(1)(A)(ii) the evaluation meets the requirement of rigorous methodologies` | snap5-s2026a.l4:134 | "shall use rigorous methodologies" |
| 144 | A-duty | `s 2026a(d)(2) the report describes the matters required` | snap5-s2026a.l4:188 | "shall submit ... a report that includes a description of" |
| 145 | A-duty | `s 2026a(d)(3) the evaluation results are shared as required` | snap5-s2026a.l4:198 | "evaluation results shall be shared publicly" |
| 146 | A-duty | `s 2026a(e)(2) the funds are available to carry out this section` | snap5-s2026a.l4:216 | "Only funds appropriated under paragraph (1) in advance specifically to carry out this section shall be available" |
| 147 | A-duty | `s 2028(b)(1) the Commonwealth may receive payments` | snap5-s2028.l4:172 | "In order to receive payments under this chapter for any fiscal year, the Commonwealth shall have a plan for that fiscal year approved by the Secretary" |
| 148 | A-duty | `s 2028(b)(1)(A) the plan has the required contents` | snap5-s2028.l4:210 | "it shall submit a plan for the provision of the assistance described in subsection (a)(2)(B) for the following fiscal year which" |
| 149 | A-duty | `s 2028(b)(2)(A) the audit is biennial` | snap5-s2028.l4:287 | "The Commonwealth shall provide for a biennial audit of expenditures" |
| 150 | A-duty | `s 2028(e)(1) the review includes the required examinations` | snap5-s2028.l4:446 | "shall carry out a review of the provision of nutrition assistance in Puerto Rico in the form of cash benefits under this section that shall include" |

The other reading, by class:

- **A-neg** (19 branches): a flat negative ("shall not", "may not", "does not", "no ... shall") is read as the text saying no to the case it describes; the other reading is that a prohibition addressed to an actor does not itself say what the legal position is, so the answer is NOTHING.
- **A-if** (28 branches): a failed condition ("if", "only if", "unless", "to be eligible") is read as the text saying no; the other reading is that "if A then B" does not say "if not A then not B", so the answer is NOTHING.
- **A-limit** (50 branches): a time or amount limit that is not met is read as the text saying no to the act; the other reading is that the limit stops the grant or duty applying and says nothing about what follows, so the answer is NOTHING.
- **A-duty** (53 branches): a duty that is not met is read as the text saying no to the question "has the duty been performed"; the other reading is that the text states the duty and not the consequence of its breach, so the answer is NOTHING.

### Reading (b): a branch answered NOTHING because the case falls outside a limit the text sets in its own words

Each row is a `-- NOTHING-kind (limited by its own wording)` comment. The other reading, the same for every row: the case falls outside a limit the text sets in its own words, so the answer is NOTHING (reading (b)); the other reading is that the limit is the text saying no, so the answer would be FALSE.

| # | function | file:line | the limit the case falls outside |
| --- | --- | --- | --- |
| 1 | `s 2025(a) the cost is an administrative cost the Secretary is authorized to pay a share of` | snap5-s2025-ab.l4:67 | "subject to the conditions set forth in subsection (g)" |
| 2 | `s 2025(a) the additional amount the Secretary may pay a State agency for a reservation or a Native village` | snap5-s2025-ab.l4:84 | the discretion is "to pay any State agency administering the supplemental nutrition assistance program on all or part of an Indian reservation ... or in a Native village" |
| 3 | `s 2025(a) the official may receive or benefit from the revenues retained by the State` | snap5-s2025-ab.l4:123 | the bar is on "the officials responsible for making determinations of ineligibility under this chapter" |
| 4 | `s 2025(b)(2) the State agency may elect to use an amount equal to the allotment to subsidize or support the job` | snap5-s2025-ab.l4:154 | "for the purpose of subsidizing or supporting a job under a work supplementation or support program established by the State" |
| 5 | `s 2025(b)(3)(A) the amount the Secretary shall pay the State agency` | snap5-s2025-ab.l4:176 | the duty arises only "If a State agency makes an election under paragraph (2) and identifies each household" |
| 6 | `s 2025(b)(3)(B) the State agency has expended the amount as required` | snap5-s2025-ab.l4:192 | the duty arises only where the election is made and the households identified |
| 7 | `s 2025(b)(3)(C)(i) the amount received is excluded from household income and resources for sections 2014 and 2017(a)` | snap5-s2025-ab.l4:202 | the exclusion is for the amount "received under this subsection", which exists only where the procedure applies |
| 8 | `s 2025(b)(3)(C)(ii) the amount received is considered the value of an allotment provided to the household for section...` | snap5-s2025-ab.l4:212 | the deeming is for the amount "received under this subsection", which exists only where the procedure applies |
| 9 | `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` | snap5-s2025-ab.l4:226 | the bar lasts only "for the period during which the member continues to participate" |
| 10 | `s 2025(b)(3)(D) the household may receive an allotment from the State agency for the period` | snap5-s2025-ab.l4:228 | the bar is part of the procedure that applies only where the State agency elects and identifies the household |
| 11 | `s 2025(b)(4) the individual is excused from a work requirement under section 2015(d) by reason of the fact that the S...` | snap5-s2025-ab.l4:238 | the bar is "by reason of the fact that a State has a work supplementation or support program" |
| 12 | `s 2025(b)(6) the work supplementation or support program is permitted` | snap5-s2025-ab.l4:264 | the text bars displacement and does not itself permit a program that does not displace |
| 13 | `s 2025(c)(1)(A)(ii)(I) the tolerance level set is within the limit` | snap5-s2025-c1.l4:33 | subclause (I) speaks of fiscal year 2014 only |
| 14 | `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year` | snap5-s2025-c1.l4:44 | "the amount specified in subclause (I)" is "an amount not greater than $37" |
| 15 | `s 2025(c)(1)(A)(ii)(II) the tolerance level for the fiscal year` | snap5-s2025-c1.l4:47 | subclause (II) is for each fiscal year after fiscal year 2014 |
| 16 | `s 2025(c)(1)(B)(ii) the Secretary shall debar the person` | snap5-s2025-c1.l4:93 | "any person that, in carrying out the quality control system established under this subsection, knowingly submits, or causes to be submitted, false information" |
| 17 | `s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency` | snap5-s2025-c1.l4:106 | the text speaks of "fiscal year 2004 and any fiscal year thereafter" |
| 18 | `s 2025(c)(1)(D)(i)(I) the new investment amount may be matched by Federal funds` | snap5-s2025-c1.l4:153 | the bar is on "the new investment amount" |
| 19 | `s 2025(c)(1)(E)(i) the at-risk amount payable to the Secretary` | snap5-s2025-c1.l4:213 | the amount is payable "if ... a liability amount has been established" for the following fiscal year |
| 20 | `s 2025(c)(1)(E)(ii)(I) the chief executive officer of the State shall now remit the at-risk amount to the Secretary` | snap5-s2025-c1.l4:223 | "as soon as practicable after completion of all administrative and judicial reviews with respect to that requirement to pay" |
| 21 | `s 2025(c)(1)(E)(ii)(II)(aa) the largest reduction the Secretary may make in amounts due to the State agency` | snap5-s2025-c1.l4:234 | "If the chief executive officer of the State fails to make the payment under subclause (I) within a reasonable period of time determined by the Secretary" |
| 22 | `s 2025(c)(1)(F)(i) the largest reduction the Secretary may make in amounts due to the State agency` | snap5-s2025-c1.l4:259 | "In the case of a State agency that fails to comply with a requirement for new investment" |
| 23 | `s 2025(c)(1)(F)(ii) the amount the Secretary shall pay the State agency` | snap5-s2025-c1.l4:272 | the payment is for a State agency that begins the new investment, appeals, and has the liability amount "reduced to $0 on administrative or judicial review" |
| 24 | `s 2025(c)(1)(F)(iii) the Secretary shall require new investment or payment of the new investment amount` | snap5-s2025-c1.l4:286 | "If a State agency does not begin required new investment under subparagraph (D)(i)(I), the State agency appeals the liability amount of the State agency, and the dete... |
| 25 | `s 2025(c)(4) the Secretary may require the State agency to report the factor` | snap5-s2025-c2.l4:103 | the power is "to determine a State agency's payment error rate, liability amount or new investment amount under paragraph (1), or performance under the performance mea... |
| 26 | `s 2025(c)(4) the Secretary shall base the determination on all pertinent information available` | snap5-s2025-c2.l4:114 | "If a State agency fails to meet the reporting requirements established by the Secretary" |
| 27 | `s 2025(c)(5) the collection efforts are initiated in time` | snap5-s2025-c2.l4:134 | "subject to the conclusion of any formal or informal appeal procedure and administrative or judicial review" |
| 28 | `s 2025(c)(6)(B) the Secretary may use another measure of the State's error` | snap5-s2025-c2.l4:162 | "Where a State fails to meet reporting requirements pursuant to paragraph (4)" |
| 29 | `s 2025(c)(6)(C) the announced national performance measure shall be used` | snap5-s2025-c2.l4:173 | "in determining the liability amount of a State under paragraph (1)(C) for the fiscal year whose error rates are being announced" |
| 30 | `s 2025(c)(6)(D) the national performance measure is subject to administrative or judicial review` | snap5-s2025-c2.l4:184 | the bar is on "the national performance measure announced under this paragraph" |
| 31 | `s 2025(c)(7)(A) the State may seek administrative and judicial review of the action under section 2023` | snap5-s2025-c2.l4:196 | "if the Secretary asserts a financial claim against or establishes a liability amount with respect to a State agency under paragraph (1)"; subparagraphs (B) and (C) ar... |
| 32 | `s 2025(c)(7)(B) the determination is subject to administrative or judicial review` | snap5-s2025-c2.l4:206 | "a determination of the payment error rate of a State agency or a determination whether the payment error rate exceeds 105 percent of the national performance measure" |
| 33 | `s 2025(c)(7)(C) the action is subject to administrative or judicial review` | snap5-s2025-c2.l4:220 | the bar is on "an action by the Secretary under subparagraph (D) or (F)(iii) of paragraph (1)" |
| 34 | `s 2025(c)(8)(A) this paragraph applies to the determination` | snap5-s2025-c2.l4:232 | "This paragraph applies to the determination of whether a payment is due by a State agency for a fiscal year under paragraph (1)" |
| 35 | `s 2025(c)(8)(I) the administrative law judge shall extend the deadline` | snap5-s2025-c2.l4:321 | "for cause shown" |
| 36 | `s 2025(c)(8)(E) the responsive evidence is submitted in time` | snap5-s2025-c2.l4:357 | "to the extent such evidence exists" |
| 37 | `s 2025(c)(8)(F) the rebuttal evidence is submitted in time` | snap5-s2025-c2.l4:372 | "to the extent such evidence exists" |
| 38 | `s 2025(c)(8)(G) the appeal is decided in time` | snap5-s2025-c2.l4:399 | "after an evidentiary hearing, shall decide the appeal" |
| 39 | `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:55 | "With respect to each of fiscal years 2003 and 2004" |
| 40 | `s 2025(d)(1)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:61 | paragraph (1) is for "Fiscal years 2003 and 2004" |
| 41 | `s 2025(d)(1)(B)(ii) the total amount of performance bonus payments for the fiscal year` | snap5-s2025-dfij.l4:71 | "With respect to each of fiscal years 2003 and 2004" |
| 42 | `s 2025(d)(1)(B)(ii) the State agency shall be awarded a performance bonus payment` | snap5-s2025-dfij.l4:82 | "With respect to each of fiscal years 2003 and 2004" |
| 43 | `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:98 | "With respect to fiscal year 2005 through fiscal year 2017" |
| 44 | `s 2025(d)(2)(B)(i) the performance of each State agency has been measured` | snap5-s2025-dfij.l4:104 | paragraph (2) is for "Fiscal years 2005 through 2017" |
| 45 | `s 2025(d)(2)(B)(ii) the total amount of performance bonus payments for the fiscal year` | snap5-s2025-dfij.l4:114 | "With respect to fiscal year 2005 through fiscal year 2017" |
| 46 | `s 2025(d)(2)(B)(ii) the State agency shall be awarded a performance bonus payment` | snap5-s2025-dfij.l4:125 | "With respect to fiscal year 2005 through fiscal year 2017" |
| 47 | `s 2025(d)(3) the State agency is eligible for a performance bonus payment for the fiscal year` | snap5-s2025-dfij.l4:142 | the bar is for a fiscal year "for which the State agency has a liability amount established" |
| 48 | `s 2025(d)(4) the determination is subject to administrative or judicial review` | snap5-s2025-dfij.l4:153 | the bar is on "A determination by the Secretary whether, and in what amount, to award a performance bonus payment" |
| 49 | `s 2025(d)(6)(B) the Secretary may award performance bonus payments` | snap5-s2025-dfij.l4:178 | the bar is on awards "in fiscal year 2019 for fiscal year 2018 performance" |
| 50 | `s 2025(e) the Secretary and State agencies shall have access to the information` | snap5-s2025-dfij.l4:214 | the access is to the information "regarding individual supplemental nutrition assistance program applicants and participants who receive benefits under title XVI of th... |
| 51 | `s 2025(f) the expense may be paid` | snap5-s2025-dfij.l4:239 | the payment is of expenses "incidental to the defense of officers and employees of the Department of Agriculture ... in judicial or administrative proceedings to which... |
| 52 | `s 2025(i)(1) the Department of Agriculture may use the information to determine which project areas have payment erro...` | snap5-s2025-dfij.l4:252 | "may use quality control information made available under this section" |
| 53 | `s 2025(i)(2) the Secretary may require the State agency to carry out new or modified certification procedures` | snap5-s2025-dfij.l4:263 | "in areas identified under paragraph (1)" |
| 54 | `s 2025(g)(1) the amount the Secretary is authorized to pay for the costs` | snap5-s2025-gh.l4:158 | the payment is for costs in the systems "that the Secretary determines" qualify under subparagraph (A) or (B) |
| 55 | `s 2025(h)(1)(C)(i) the unexpended funds the Secretary shall reallocate to other States` | snap5-s2025-gh.l4:198 | "If a State agency will not expend all of the funds allocated to the State agency for a fiscal year" |
| 56 | `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to the evaluation of subparagraph (F)(vii)` | snap5-s2025-gh.l4:260 | the exemption is for activities "funded under this subclause" |
| 57 | `s 2025(h)(1)(C)(iv)(I)(cc) the activities are subject to monitoring under paragraph (5)` | snap5-s2025-gh.l4:269 | the monitoring is of activities "funded under this subclause" |
| 58 | `s 2025(h)(1)(C)(v) the State agency may also be considered for funding under clause (iv)(II)` | snap5-s2025-gh.l4:315 | "a State agency that receives reallocated funds under clause (iv)(I) may also be considered" |
| 59 | `s 2025(h)(1)(D) the allocation meets the minimum` | snap5-s2025-gh.l4:325 | "each State agency operating an employment and training program" |
| 60 | `s 2025(h)(1)(E)(i) the costs of serving the member may be reimbursed from the additional allocation` | snap5-s2025-gh.l4:356 | "for the costs incurred in serving members of households receiving supplemental nutrition assistance program benefits who" are "not eligible for an exception" and are ... |
| 61 | `s 2025(h)(1)(E)(ii) the commitment to offer a position covers the applicant or recipient` | snap5-s2025-gh.l4:387 | the commitment is "to each applicant or recipient who" "is in the last month of the 3-month period", "is not eligible for an exception", "is not eligible for a waiver"... |
| 62 | `s 2025(h)(2) the amount the Secretary shall pay for the additional costs` | snap5-s2025-gh.l4:403 | "If, in carrying out such program during such fiscal year, a State agency incurs costs that exceed the amount allocated to the State agency under paragraph (1)" |
| 63 | `s 2025(h)(3) the reimbursement may be made out of funds allocated under paragraph (1)` | snap5-s2025-gh.l4:429 | the bar is on "such reimbursement" |
| 64 | `s 2025(h)(5)(B)(iii) the State employment and training plan must identify reporting measures for the component` | snap5-s2025-gh.l4:494 | "each proposed component that serves a threshold number of participants" |
| 65 | `s 2025(h)(5)(B)(v) the State agency may report the data to demonstrate the number of participants served` | snap5-s2025-gh.l4:522 | "relevant data from a workforce partnership carried out under section 2015(d)(4)(N)" |
| 66 | `s 2025(h)(5)(C)(iv) the Secretary may require the information` | snap5-s2025-gh.l4:555 | "for States receiving additional allocations under paragraph (1)(E)" |
| 67 | `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` | snap5-s2025-hf.l4:363 | the standards are for "employment activities described in subclauses (I), (II), and (III) of clause (iv)" and for failures "beyond the control of an individual" |
| 68 | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` | snap5-s2025-hf.l4:391 | "no work registrant shall be eligible ... if the individual refuses without good cause"; a refusal with good cause is not answered |
| 69 | `s 2025(h)(1)(F)(v) the work registrant is ineligible to participate in the supplemental nutrition assistance program` | snap5-s2025-hf.l4:395 | "if the individual refuses without good cause to participate in an employment and training program under this subparagraph, to the extent required by the State agency" |
| 70 | `s 2025(h)(1)(F)(vi)(I) the activities are considered to be carried out under section 2015(d)` | snap5-s2025-hf.l4:405 | "Employment and training activities under this subparagraph shall be considered to be carried out under section 2015(d)" |
| 71 | `s 2025(h)(1)(F)(vii)(I) the Secretary has conducted the independent evaluation as required` | snap5-s2025-hf.l4:436 | the evaluation is "for each State agency that enters into a cooperative agreement" |
| 72 | `s 2025(h)(1)(F)(vii)(II) a report is due on 31 December of the year` | snap5-s2025-hf.l4:470 | "Not later than December 31, 2015, and each December 31 thereafter" names no report for an earlier year |
| 73 | `s 2025(h)(1)(F)(viii)(I) the amount the Secretary shall use to carry out the subparagraph for the fiscal year` | snap5-s2025-hf.l4:545 | the clause names "for fiscal year 2014" and "for fiscal year 2015" only |
| 74 | `s 2025(h)(1)(F)(viii)(III) the funds remain available on the date` | snap5-s2025-hf.l4:578 | "shall remain available through September 30, 2018" says how long they remain available and not what becomes of them afterwards |
| 75 | `s 2025(h)(1)(F)(ix)(III) the State may contribute the additional funds` | snap5-s2025-hf.l4:621 | "States may contribute additional funds obtained from other sources" |
| 76 | `s 2025(k)(3)(A) the reductions are made on a quarterly basis as required` | snap5-s2025-k.l4:112 | the duty holds only "to the extent practicable" |
| 77 | `s 2025(k)(3)(B)(i) the amount of the reduction in the fiscal year in which the determinations are made` | snap5-s2025-k.l4:133 | clause (i) applies if the determinations are not made "by September 30, 1999" |
| 78 | `s 2025(k)(3)(B)(ii) subparagraph (A) applies in the fiscal year` | snap5-s2025-k.l4:145 | clause (ii) is "for each subsequent fiscal year" when the determinations are not made by September 30, 1999 |
| 79 | `s 2025(k)(4)(D) the determination or decision is subject to judicial review` | snap5-s2025-k.l4:279 | the bar is on the determinations and final decisions it names |
| 80 | `s 2025(k)(4)(E) the pendency of the appeal affects the requirement that the Secretary reduce payments` | snap5-s2025-k.l4:290 | the sentence speaks of "The pendency of an appeal under this paragraph" |
| 81 | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` | snap5-s2025-k.l4:313 | "any other Federal funds (except funds provided under subsection (a))" |
| 82 | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` | snap5-s2025-k.l4:315 | "Subparagraph (A) applies to—" the four kinds it lists |
| 83 | `s 2025(k)(5) the funds or expenditures may be used to pay for the costs` | snap5-s2025-k.l4:321 | the bar is on costs that meet both clause (i) and clause (ii) |
| 84 | `s 2026a(b) the project is a healthy fluid milk incentive project the Secretary is to carry out` | snap5-s2026a.l4:60 | the text describes the projects the Secretary shall carry out; it does not say that a project of another description may not be carried out |
| 85 | `s 2026a(c)(1) the Secretary shall enter into the agreement with, or provide the grant to, the entity` | snap5-s2026a.l4:79 | "on a competitive basis" and "for projects that meet the purpose and selection criteria" |
| 86 | `s 2026a(c)(4) the funds made available under this section may be used for the project` | snap5-s2026a.l4:111 | the text bars a use of the funds and does not itself authorize a project that does not limit benefits |
| 87 | `s 2026a(d)(2) the date by which the report is due in the year` | snap5-s2026a.l4:156 | the text names December 31 of 2020 and every second year after it, and no other date |
| 88 | `s 2026a(d)(2) the report is submitted in time` | snap5-s2026a.l4:170 | no report is due in that year |
| 89 | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` | snap5-s2028.l4:67 | "subject to the availability of appropriations under section 2027(a)" |
| 90 | `s 2028(a)(2)(A) the amount of the block grants for the fiscal year` | snap5-s2028.l4:69 | the text gives an amount for fiscal year 2003 and each fiscal year thereafter |
| 91 | `s 2028(a)(2)(B)(i) the Commonwealth's share of the funds` | snap5-s2028.l4:82 | the text speaks of fiscal year 2003 and each fiscal year thereafter |
| 92 | `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` | snap5-s2028.l4:103 | "may spend in fiscal year 2002 or 2003" |
| 93 | `s 2028(a)(2)(B)(ii) the Commonwealth may spend the amount on the cost` | snap5-s2028.l4:112 | the exception is for "fiscal year 2002 or 2003" |
| 94 | `s 2028(a)(2)(C) American Samoa's share of the funds` | snap5-s2028.l4:123 | the text speaks of fiscal year 2003 and each fiscal year thereafter |
| 95 | `s 2028(a)(2)(D) the carryover is within the limit` | snap5-s2028.l4:144 | the text speaks of fiscal year 2002 and each fiscal year thereafter |
| 96 | `s 2028(a)(3) the payment to the Commonwealth for the fiscal year` | snap5-s2028.l4:160 | "subject to the provisions of subsection (b)" |
| 97 | `s 2028(b)(1)(A) the plan is submitted in time` | snap5-s2028.l4:183 | "if the Commonwealth wishes to receive payments" |
| 98 | `s 2028(b)(1)(B)(i) payments may be made for the fiscal year of the plan` | snap5-s2028.l4:240 | "except as provided in subparagraph (B)(ii)" |
| 99 | `s 2028(b)(1)(B)(ii) the withheld payments are to be paid` | snap5-s2028.l4:257 | clause (ii) applies only where the Secretary has suspended the denial of payments |
| 100 | `s 2028(b)(2)(C)(i) further payments may be made` | snap5-s2028.l4:324 | "except as provided in subparagraph (C)(ii)" |
| 101 | `s 2028(b)(2)(C)(ii) the withheld payments are to be paid` | snap5-s2028.l4:341 | clause (ii) applies only where the Secretary has suspended the termination of payments |
| 102 | `s 2028(b)(2)(C)(iii) the Secretary may refer the matter to the Attorney General` | snap5-s2028.l4:351 | "Upon a finding under subparagraph (C)(i) of a substantial failure" |
| 103 | `s 2028(b)(2)(C)(iii) appropriate injunctive relief shall issue` | snap5-s2028.l4:361 | "upon suit by the Attorney General in an appropriate district court of the United States and a showing that noncompliance has occurred" |
| 104 | `s 2028(c)(1) the Secretary shall provide for the review of the program` | snap5-s2028.l4:373 | "for which payments are made under this chapter" |
| 105 | `s 2028(c)(2) the Secretary may provide technical assistance` | snap5-s2028.l4:383 | "as the Secretary deems practicable" |
| 106 | `s 2028(d) the conduct is within the offence` | snap5-s2028.l4:396 | "Whoever knowingly and willfully" |
| 107 | `s 2028(d) the conduct is within the offence` | snap5-s2028.l4:398 | "any funds, assets, or property provided or financed under this section" |
| 108 | `s 2028(e)(3)(A) the largest share of a participant's benefit a plan may distribute in cash` | snap5-s2028.l4:481 | the text states a limit for each of fiscal years 2017 to 2021 and none for any other year |
| 109 | `s 2028(e)(3)(A) the Secretary shall disapprove the plan` | snap5-s2028.l4:493 | "that provides for the distribution of more than" the stated share; a plan at or under the share is not mentioned |
| 110 | `s 2028(e)(4) the amount to make available for the review and report` | snap5-s2028.l4:516 | the text names only fiscal year 2014 |

### Closed definitions answered FALSE (not marginal)

These 6 branches rest on a definition that says "means"; the brief counts that as the text saying no in its own words, so they are not listed above.

| function | file:line | the words |
| --- | --- | --- |
| `s 2025(b)(1) the program is a work supplementation or support program` | snap5-s2025-ab.l4:137 | "means a program under which" |
| `s 2025(k)(1)(A) the program is the AFDC program` | snap5-s2025-k.l4:31 | "The term “AFDC program” means the program of aid to families with dependent children established under part A of tit... |
| `s 2025(k)(1)(B) the period is the base period` | snap5-s2025-k.l4:42 | "The term “base period” means the period used to determine the amount of the State family assistance grant for a Stat... |
| `s 2025(k)(1)(C) the program is the medicaid program` | snap5-s2025-k.l4:54 | "The term “medicaid program” means the program of medical assistance under a State plan or under a waiver of the plan... |
| `s 2026a(a) the product is fluid milk` | snap5-s2026a.l4:43 | "the term fluid milk means all varieties of pasteurized cow's milk that" |
| `s 2028(a)(1) the place is a governmental entity` | snap5-s2028.l4:48 | "the term governmental entity means" |

Everything else that answers `NOTHING` is not marginal in this sense: 20 `silent`, 18 `includes`, 13 `points outside the text`, 4 `list not closed`, 1 `undefined term`, each marked on its branch.

### Reading a result: FALSE and NOTHING (snap5)

Almost everything in sections 2025, 2026a and 2028 is a rule about money and duties between the Secretary, a State agency, the Commonwealth of Puerto Rico and American Samoa.
A household member meets it as a condition (a Social Security number), a protection (the work supplementation money is not income), a limit on a sanction (a failure to work for reasons beyond your control does not end your eligibility), or the definition of a thing they buy (fluid milk).

- **A no (`JUST FALSE`, or an answer of `0`) means the text itself says no to the case.**
  Here that is: a closed definition ("the term fluid milk means ...", "the term governmental entity means ..."); a flat negative ("shall not be subject to administrative or judicial review", "shall not receive or benefit from revenues", "No funds ... may be used"); a condition the text introduces with "if", "only if", "until", "unless", "except" or "To be eligible ... shall" that is not met; and a time or amount limit the case misses or exceeds ("Not later than 60 days", "not more than 10 pilot projects").
  The answer to "is the report in time?" is a no when it was late; the answer to "has the Secretary done what the clause requires?" is a no when the clause's condition was not met.
  It is not a statement that a person is not entitled to something unless the question asked was about entitlement.
- **"Not covered" (`NOTHING`) means the text does not say.**
  Here that is: a fiscal year outside the period the text states (a block grant for a fiscal year before 2003, a cash share for any year but 2017 to 2021, a report due in a year the text does not name); a term the text leaves undefined where it is used (`good cause` outside subsection (c), `governmental entity` in section 2026a); an open list that "includes" (`good cause`); an official's determination that was not supplied ("the Secretary determines ..."); a power, rate or authority outside these sections; and a case the text does not mention (a State agency whose payment error rate is under 6 percent, which the liability formula does not address).
- **A caller must never turn `NOTHING` into `FALSE`.**
  A State agency under 6 percent has no liability amount of `0` under the text; it has no stated liability amount, and the answer is `NOTHING`.
  A report that is not yet due is not a late report.
- **In the seat layer** the same marks are returned unchanged: a question about a person's own case returns `JUST TRUE` or `JUST FALSE` only where the text says so, and `NOTHING` where it does not or where the person could not state a fact the question needs.

## Seams (snap5)

`SEAMS.md` has the two lists (ASKS and ANSWERS), generated from the modules.
The seams the plan names, as I took them:

| input | type | asked by | answered by |
| --- | --- | --- | --- |
| `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between the two dates` | `NUMBER` (a fraction) | `s 2025(c)(1)(A)(ii)(II)`, `s 2028(a)(2)(A)` | section 2012(u)(3), another part (the plan: "a published figure and a conditional input") |
| `s 2015(o)(2) the individual is in the last month of the 3-month period` | `MAYBE BOOLEAN` | `s 2025(h)(1)(E)(ii)` | section 2015(o)(2), another part |
| `s 2015(o)(3) the individual is eligible for an exception` | `MAYBE BOOLEAN` | `s 2025(h)(1)(E)(i)`, `s 2025(h)(1)(E)(ii)` | section 2015(o)(3), another part |
| `s 2015(o)(4) the individual is eligible for a waiver` | `MAYBE BOOLEAN` | `s 2025(h)(1)(E)(ii)` | section 2015(o)(4), another part |
| `s 2015(o)(6) the individual is exempt` | `MAYBE BOOLEAN` | `s 2025(h)(1)(E)(ii)` | section 2015(o)(6), another part |
| `s 2027(a) appropriations are available` | `MAYBE BOOLEAN` | `s 2028(a)(2)(A)` | section 2027(a), another part |

Two inputs are named like the functions of this part that answer them (so the answering function can be wired to the asking one by name): `s 2025(h)(1)(F)(vi)(II) the failure to work results in ineligibility` (asked by the sanction in `s 2025(h)(1)(F)(v)`) and `s 2028(b)(1) the Commonwealth may receive payments` (asked by `s 2028(a)(3)`).

Seams the plan lacks (found in these ranges): the generated ASKS list in `SEAMS.md` counts plan-named seam: 8; another section or Act: 27; the Secretary's decision or another official's: 38 (73 inputs).
The plan's Group C counts the literal mentions "section 20NN" in the asking section (section 2025 names section 2015 21 times, section 2020 four times, section 2027 three times, section 2023 twice, and sections 2017, 2022, 2026 and 2029 once each) and advises naming each such input for the answering section.
The brief governs: these are asked as plain facts, named for the fact and not for another part's function.
`SEAMS.md` ASKS lists every one with the section that answers it, in three groups: the plan-named seams above, facts about another section or Act, and determinations of the Secretary or another official.

## What the text turns out to say

Numbered findings.
Each was checked against the text when written; the lines are of `usc07-ch51.txt`.

1. **"Good cause" is defined for subsection (c) only, and with "includes".**
   Line 2038: "As used in this subsection, the term "good cause" includes--", then five items.
   The term is used at line 2226 (section 2025(h)(1)(F)(v): "refuses without good cause"), outside subsection (c), where it is undefined.
   The encoding therefore takes it as an input where it is used in (h)(1)(F)(v) and answers `NOTHING` when it is not supplied; inside subsection (c) the list is open (`includes`), so a circumstance not on the list is `NOTHING`, not a no.
   The same happens to "governmental entity": section 2028(a)(1) defines it "In this subsection", and section 2026a(c)(1) uses it (and 2026a(c)(2) spells it "government entity").
2. **The heading of section 2025(c)(1)(C) says fiscal year 2003; the body says 2004.**
   Line 1951 (heading): "Establishment of liability amount for fiscal year 2003 and thereafter"; line 1952: "With respect to fiscal year 2004 and any fiscal year thereafter".
   The body is followed (`s 2025(c)(1)(C) the Secretary shall establish a liability amount for the State agency` answers `NOTHING` for a year before 2004).
3. **Section 2025(i)(1) cites the wrong subsection for the payment error rate.**
   Line 2326 refers to "payment error rates (as defined in subsection (d)(1))"; subsection (d)(1) is the guidance on performance indicators for fiscal years 2003 and 2004, and the payment error rate is defined in section 2025(c)(2)(A) ("As used in this section", line 1990).
   The encoding uses the (c)(2)(A) definition.
4. **The liability formula is silent below 6 percent.**
   Section 2025(c)(1)(C)(ii) multiplies by "the difference between the payment error rate and 6 percent".
   For a State agency under 6 percent that difference is negative, and the text does not say what a negative liability amount is (fork F-4).
5. **"At the Secretary's discretion" reaches the retention shares.**
   The proviso of section 2025(a) says the Secretary "is authorized at the Secretary's discretion to pay ... such amounts for administrative costs ... as well as to permit each State to retain 35 percent ... and 20 percent": the discretion governs the permission to retain, so the share is a ceiling the Secretary may permit, not an entitlement (fork F-3).
6. **Section 2025(k)(2)(A) feeds no rule.**
   Paragraph (2)(A) asks the Secretary of Health and Human Services to determine the amount a State received under the AFDC program for common costs; paragraph (3)(A) reduces the payment by "the amount determined ... under paragraph (2)(B)" only.
   The encoding computes (2)(B) from the facts and keeps (2)(A) as a determination to be made (`s 2025(k)(2) the determinations are made ...`).
7. **Section 2025(h)(1)(F)(vii)(I)(bb) is a pure purpose clause.**
   "The purpose of the independent evaluation shall be to measure the impact ..."; it states what the evaluation is for and gives no one a right or a duty beyond subclause (aa) and (cc).
   It is `inert (1 not operative)` in the coverage table.
8. **"To be eligible ... a State agency shall" is read as the text's own eligibility condition.**
   It occurs three times in these ranges (section 2025(h)(1)(E)(ii), section 2025(h)(1)(F)(ii)(II) and section 2026a(c)(2)).
   A State agency that does not do what the clause says is, on that reading, not eligible: a no in the text's own words.
   It is listed as a marginal reading (a) in the table above.
9. **Section 2028(b) and (e)(3) speak only of the Commonwealth.**
   American Samoa receives its share of the block grant under (a)(2)(C) with no plan, audit or statement requirement in (b), and (e) is about "Puerto Rico".
   The penalty in (d) reaches funds "provided or financed under this section", so both.
10. **Section 2028(e)(3)(A) names fiscal years 2017 to 2021 only.**
    The cash share is 20, 15, 10, 5 and 0 percent for those years; the text says nothing for any other year, and the encoding answers `NOTHING` (limited by its own wording).
11. **The block grant formula is silent before fiscal year 2003.**
    Section 2028(a)(2)(A)(i) fixes $1,401,000,000 for fiscal year 2003; paragraph (D) speaks of "fiscal year 2002 and each fiscal year thereafter" for the carryover, and (B)(ii) of 2002 and 2003 for the systems exception.
    The encoding takes each period as the text states it.
12. **Dates computed from the text.**
    Section 2025(k)(2): "Not later than 180 days after June 23, 1998" is 20 December 1998 (`Date 23 6 1998 PLUS 180`, tested).
    Section 2025(j): 180 days after 19 September 1988 is 18 March 1989; "annually thereafter" is fork F-6.
    Section 2028(e)(2): "Not later than 18 months after February 7, 2014" is 7 August 2015.
13. **Fiscal years are not defined in these sections.**
    The encoding names a fiscal year by its number, and passes a date where the text speaks of "the end of the fiscal year" (the date is an input, not a computed 30 September).
14. **Several provisions are time-limited in their own wording and are now spent** (fiscal year 2014 for section 2028(e)(4), 2002 and 2003 for section 2028(a)(2)(B)(ii), "through September 30, 2018" for section 2025(h)(1)(F)(viii)(III)).
    They are encoded as the text states them, and a case outside the period is `NOTHING` (marginal reading (b)).

## What the stable binary does not accept

Probed on `l4` 1.6.98 (main, 7689b0d), with the probe files kept in the work folder.
Where the skills describe a construct the stable binary rejects, the binary governs.

**Loud (an error says so):**

- `EVERY p IN ps MUST pay WITHIN 5`: parse error at `IN`.
  A rule for "each of several parties" is written as one rule per party, or as a decision function over a list.
- `AFTER 3 WITHIN 5`: parse error at `AFTER`.
  A window that opens late is written with `(WAITUNTIL n)` or by starting the trace at the opening day.
- `WAIT UNTIL n` (two words): "I could not find a definition for the identifier WAIT" and "... UNTIL".
  The one-word spelling `WAITUNTIL` works.
- `LEST BREACH BY LIST a, b BECAUSE "..."`: type error, "The HENCE clause of a regulative rule is expected to be of type DEONTIC OF P, X" (a list of parties is not a party).
- A `GIVEN` inside a function body (a section `GIVEN`): parse error at the body's first expression.
- `TYPICALLY` on a record field: parse error "unexpected 5" at the value, on a multi-line `DECLARE R HAS` with one field per line (the same declaration without `TYPICALLY` checks clean); the Commons guide says so as well.
- `#ASSERT REFUSED f`: "I could not find a definition for the identifier REFUSED" (`REFUSE` does not exist on the stable binary; "not covered" is `NOTHING` or a constructor, asserted).

**Silent (the binary returns an answer and the answer is not the one the words suggest, or the check cannot see it):**

- `NOT x AND y` parses as `NOT (x AND y)`, not `(NOT x) AND y`.
  Probe: with `g MEANS NOT a AND b`, `g FALSE FALSE` is `TRUE` (a failed assertion `EQUALS FALSE`, a satisfied one `EQUALS TRUE`).
  Every `NOT` in these modules is parenthesised; two tests caught the mistake while the `snap5-s2025-k.l4` module was written.
- A `#TRACE` result cannot be asserted: `#ASSERT r EQUALS FULFILLED` compares the rule itself with `FULFILLED` and fails, so a regulative rule's outcome is only printed.
  Every regulative rule in `snap5-s2025-duties.l4` therefore has a decision-function twin, and `snap5-tests-s2025-duties.l4` writes the expected trace outcome in a comment before the trace (from the text, before the file was run) and asserts the twin on the same facts on the next lines.
  `check.sh` counts assertion lines and does not compare `#TRACE` outcomes, so I compared the 27 traces by hand: the `Message:` lines of the run on the stable build and on the main build 1.6.108 are identical, and so are the other lines but the diagnostic codes.

**A tooling note (`srcrefs.py`, not the binary):** a comment between an `@ref` and the declaration it cites risks breaking the binding of the locator to the declaration; the modules put any such comment above the `--QUOTE` line.

## Seat

**Seat:** a member of a household that applies for, or receives, benefits under the Supplemental Nutrition Assistance Program.
Layer 2 (`snap5-seat.l4`, `snap5-cases-seat.l4`) asks 17 questions from that position, each beginning "Under section N,", each with `@export` and `@desc`, grouped under `§§` headings, taking plain inputs (yes/no answers, numbers and the modules' own choices), and calling layer-1 rules without restating them.
The 82 cases are the facts a real person in the seat would state, between 3 and 9 for each question, and they include the cases in which the answer is `NOTHING`.

Questions: section 2025(a) (what share of money recovered from my household the State may keep); 2025(b)(3)(C)(i) (is the money my State pays my employer left out of my household's income and resources); 2025(b)(3)(C)(ii) (is it treated as the value of an allotment my household has received); 2025(b)(3)(D) (may my household receive an allotment while I stay in the program); 2025(b)(4) (am I excused from a work requirement); 2025(e)(1) (have I met the condition of furnishing a Social Security number); 2025(e) (may the Secretary and my State agency see my Social Security records); 2025(h)(1)(E)(ii) (does my State agency's commitment to offer a position cover me); 2025(h)(1)(F)(vi)(II) (does my failure to work cost me my eligibility); 2025(h)(1)(F)(v) (am I ineligible because I refused to take part in a pilot project); 2025(h)(1)(F)(vi)(III) (did my State agency do what it must before assigning me to mandatory activities); 2026a(a) (is the milk I buy fluid milk for the incentive projects); 2028(a)(1) (is the place where I live one the block grants go to); 2028(e)(3)(A) (the largest share of my benefit Puerto Rico's plan may pay me in cash); 2028(d) (is what I did within the offence of taking the block grant's money; the most I can be fined; the longest I can be imprisoned).

**Units.** A share in an answer is a fraction, not the percent printed in the Act (35 percent is 0.35, 5 percent is 0.05); money is in dollars; the seat file says so in its header.

Provisions that address only an official (the quality control system, performance bonus payments, the cost-sharing percentages, computerization, State plans, funding formulas, the Secretary's reports) are encoded in layer 1 for what they decide and are not asked in layer 2, because there is no seat for an official; they ask nothing a household member can state.
A judgment the Act leaves to an official (the Secretary's determination that access to Social Security records is necessary) is asked as a yes/no fact: if the answer is not yet known, the question cannot be answered from the seat and returns `NOTHING`.

## Independent review (2026-11-04): the items in this range

An independent reviewer wrote its own tests from the text against the merged encoding; 20 of its assertions in sections 2025, 2026a and 2028 did not match.
Each was triaged against the text.
No item was a defect of this encoding.
Of the 20: 3 are forks the register already holds (498d is F-3, 537a is F-13, 550e is F-12); 1 is a FALSE-kind branch (S3.41); 6 are NOTHING-kind branches (515b, 543b, 546b, 555b, 603a, 631c) under the two readings left for a lawyer; and 10 are the unit, a fraction and not the printed percent (496a-c, S3.39, S3.40, S4.23, S4.24, and 506, 513a, 631a, where a percent was passed into a function that takes a fraction).
The only edits made were comments that state the unit; no code, expectation or signature changed.

| id | verdict | evidence | action |
| --- | --- | --- | --- |
| 498d | FORK (F-3, second limb) | Text 1913: "any other funds or allotments recovered or collected, except the value of funds ... that arise from an error of a State agency". The test sets 2015(b) and error both true. The 35 percent test comes first (`snap5-s2025-ab.l4:97`) and the "except" is read as qualifying only the 20 percent limb, its nearest antecedent (`:99-100`). The reviewer's own note on 498d2 calls 498d "the contested reading"; 498d2 (error, neither section) passes with 0. | none; the other reading is to test the error first |
| 537a | FORK (F-13) | Text 2110: "to remain available for 24 months, from funds made available for each fiscal year". The text gives no start date. `snap5-s2025-gh.l4:172-174` adds 24 months to the reservation date and returns the corresponding date (1 October 2028 for 1 October 2026); the reviewer's 30 September 2028 is the day before. The name says "last day", the value is the corresponding date: a one-day fork. | none; both readings in NOTES F-13 |
| S3.41 | FALSE-KIND, reading (a) | Text 1913 "except the value of funds ... that arise from an error of a State agency"; "except" is one of the brief's plain "unless" variants. Seat `snap5-seat.l4:53-54` returns JUST 0, from the layer-1 constructor `may not be permitted to retain under this proviso` (`snap5-s2025-ab.l4:99`). The reviewer's own 498d2 expects 0 for the same facts and passes. | none |
| 515b | NOTHING-KIND (list not closed), also reading (b) | Text 1997-1998: "The following errors ... shall not be included in the payment error rate: (A) ... during the first 120 days". An error on day 151 is not mentioned (`snap5-s2025-c2.l4:75`). | none |
| 543b | NOTHING-KIND (limited by its own wording), reading (b) | Text 2149, 2152: "commitment to offer a position ... to each applicant or recipient who— ... is not eligible for a waiver". It says whom the commitment must cover, not that a waiver-eligible person is outside it (`snap5-s2025-gh.l4:387`). | none |
| 546b | NOTHING-KIND (limited by its own wording), reading (b); "good cause" is also undefined here (finding 1) | Text 2226: "no work registrant shall be eligible ... if the individual refuses without good cause to participate". With good cause the prohibition does not apply and the text says nothing more (`snap5-s2025-hf.l4:391-392`). Reading (a) would give FALSE; this is one of the listed marginal readings. | none |
| 550e | NOTHING-KIND (limited by its own wording), FORK F-12, reading (b) | Text 2267: "Funds ... shall remain available through September 30, 2018." It says how long, not what follows (`snap5-s2025-hf.l4:574-578`). | none |
| 555b | NOTHING-KIND (limited by its own wording), reading (b) | Text 2295: "each proposed component that serves a threshold number of participants determined by the Secretary of at least 100 people a year". A component below the threshold is outside the requirement, and the text does not forbid measures for it (`snap5-s2025-gh.l4:494`). | none |
| 603a | NOTHING-KIND (list not closed), also reading (b) (a named complement) | Text 2667: "shall enter into cooperative agreements with, or provide grants to, governmental entities or nonprofit organizations". No "only" (`snap5-s2026a.l4:73-75`). | none |
| 496a, 496b, 496c | UNIT | A share is a fraction (50 percent is 0.50). Documented in the module header `snap5-s2025-ab.l4:7`, now also at the function (`:31`), in NOTES.md and PROGRESS.md. The reviewer's 496d (1000 gives 500) passes. | comment added at `:31` |
| S3.39, S3.40 | UNIT | The seat returns the share as a fraction (0.35, 0.20). The seat file did not say so; it now does (`snap5-seat.l4:31`), and NOTES.md "Seat" says so. | comment added |
| S4.23, S4.24 | UNIT | The cash share is a fraction (0.20, 0.05): `snap5-s2028.l4:6` (header), now also at the function (`:464`). S4.25 (JUST 0) passes, since 0 has no unit. | comment added |
| 506 | UNIT-INPUT | `s 2025(c)(1)(C) the liability amount` takes the rate as a fraction (`snap5-s2025-c1.l4:6` header, now also `:117`). With 9: 1,000,000,000 x (9 - 0.06) x 0.10 = 894,000,000. The reviewer's twin 506b (0.09) passes with 3,000,000. | comment added |
| 513a | UNIT-INPUT | 5.99 is not less than 0.06, so JUST TRUE (`snap5-s2025-c1.l4:310`). The twin 513c (0.0599, JUST FALSE) passes, and so does 513b. | comment added at `:302` |
| 631a | UNIT-INPUT | 10 is more than 0.10 (`snap5-s2028.l4:492`). Its fraction twin 631c does NOT pass, for the reason in the next row; 631d (0.11) passes, and 631b (11) is TRUE on either unit. | comment added at `:464` |
| 631c | NOTHING-KIND (limited by its own wording), reading (b) | Text 2796: "disapprove any plan ... for fiscal year 2019 that provides for the distribution of more than 10 percent". Exactly 10 percent is not "more than"; a plan at or under the cap is not mentioned (`snap5-s2028.l4:492-493`). | none |

**The FALSE and NOTHING items read again against the brief's own list of grounds.**
The brief's FALSE grounds are a "means" definition; a condition introduced with "if", "only if", "as long as", "unless" (and "so long as", "while", "until", "except", "save", "provided that"); a list closed with "only"; and a flat negative ("does not", "shall not", "may not", "is not entitled").
Its NOTHING grounds are silent, list not closed, includes, undefined term, points outside the text, and limited by its own wording ("without", "against the will of", "when", a stated period, a named complement).
No branch changed and no expectation changed.

| id | words that fit the FALSE list | NOTHING ground relied on | why it beats the FALSE ground | sibling check |
| --- | --- | --- | --- | --- |
| 546b | "no work registrant shall be eligible ... if the individual refuses without good cause": a flat negative and an "if" | limited by its own wording, for the case where the caller says the registrant HAS good cause (`snap5-s2025-hf.l4:391-392`): the brief's own NOTHING list names "without", and "without good cause" names its complement | the "if" is the trigger of a prohibition, not a condition of a grant: the flat negative is spent when the trigger is met (the function is phrased "is ineligible" and answers TRUE there, `:390`), and the text does not say that a registrant who refuses with good cause is eligible; ("undefined term" is the ground of the other branch, `:393-394`, where good cause is not supplied, and is not relied on here) | the shared shape is a definite answer inside the trigger and NOTHING outside it: s 2025(b)(3)(D) (`snap5-s2025-ab.l4:220-229`), s 2025(b)(4) (`snap5-s2025-ab.l4:236-243`: NOTHING on the "except" side, "points outside the text"), s 2025(d)(3) (`snap5-s2025-dfij.l4:138-143`), s 2025(d)(6)(B) (`snap5-s2025-dfij.l4:174-179`), s 2026a(c)(4) (`snap5-s2026a.l4:107-112`); the five siblings are phrased positively ("may", "is excused", "is eligible") and answer FALSE inside; 546b is phrased "is ineligible" and answers TRUE inside |
| 515b | "shall not be included in the payment error rate": a flat negative | list not closed (no "only"), and a stated period ("during the first 120 days") | the flat negative covers the errors the list names; an error on day 151 is not named, and nothing closes the list | `snap5-s2025-c2.l4:75` and the other open lists answer NOTHING; the lists closed with "only" answer FALSE (`snap5-s2025-dfij.l4:165`, `snap5-s2025-c1.l4:191`, `snap5-s2025-c2.l4:209`) |
| 543b | none: a relative clause, "each applicant or recipient who ... is not eligible for a waiver" | limited by its own wording (a named complement) | no FALSE word is in the sentence | other relative-clause scopes answer NOTHING (`snap5-s2025-gh.l4:158`, `:315`, `:403`) |
| 550e | none: "through September 30, 2018" is a date, not "until" an event | limited by its own wording (a stated period); fork F-12 | "through" with a date is not on the FALSE list | "through fiscal year 2017" answers NOTHING (`snap5-s2025-dfij.l4:98-125`); the "until" branches that answer FALSE all name an event (`snap5-s2025-hf.l4:477`, `snap5-s2028.l4:242`, `:255`, `:326`, `:339`) |
| 555b | none: "each proposed component that serves a threshold number of participants ... of at least 100 people a year" | limited by its own wording (a relative clause and a threshold) | no FALSE word is in the sentence | same as 543b |
| 603a | none: no "only" | list not closed | a list closed with "only" would be FALSE, and this one is not | open lists answer NOTHING, closed lists FALSE (see 515b) |
| 631c | none: "more than 10 percent" is a threshold on a duty, with no "except" or "unless" | limited by its own wording (the threshold) | no FALSE word is in the sentence | `snap5-s2025-c1.l4:303-310` answers FALSE because the text says "other than State agencies with payment error rates of less than 6 percent", an exception in its own words; `snap5-s2028.l4:492-493` has none |
| S3.41 | "except the value of funds ... that arise from an error of a State agency" | not applicable | the branch already answers FALSE (the seat returns 0) | consistent with the brief |

**What would change under reading (a), for 546b.**
This is a choice, not a finding: the branch rests on reading (b), and it is one of the rows in "Marginal readings for a lawyer" (rows 68 and 69).
Under reading (a), a failed "if" counts as the text's no, and the good-cause case (`snap5-s2025-hf.l4:391-392`) would answer JUST FALSE.
The own assertions that pin NOTHING there are `snap5-tests-s2025-hf.l4:146` and `snap5-cases-seat.l4:71`.
A strict reading (a) would also flip the case where the individual does not refuse (`snap5-s2025-hf.l4:395-396`; `snap5-tests-s2025-hf.l4:149`, `snap5-cases-seat.l4:74`).
The cases where the individual is not a work registrant or the State agency does not require the participation (`snap5-tests-s2025-hf.l4:148` and `:150`, `snap5-cases-seat.l4:73` and `:75`) turn on the scope of the sentence ("no work registrant", "to the extent required by the State agency") and stay NOTHING on either reading.
Nothing was changed.

**Units, restated.**
Every function in this range takes a share or a rate as a fraction (50 percent is 0.50, 6 percent is 0.06) and the seat returns fractions.
That is stated in the header of `snap5-s2025-c1.l4` (lines 6 and 7), at the functions (`snap5-s2025-c1.l4:117` and `:302`, `snap5-s2025-ab.l4:31`, `snap5-s2028.l4:464`, `snap5-seat.l4:31`), in this file under "Seat", and in `PROGRESS.md`.
Given 9 as a rate, the liability amount (506) is 1,000,000,000 x (9 - 0.06) x 0.10 = 894,000,000, not 8; the reviewer's twins 506b, 513c and 631d, which use fractions, pass.

## Tests that fail on purpose

None.
Every assertion in every file is written to be satisfied and is, on the stable build and on the main build; `expected_failed` in `check.sh` is unchanged (0 for every module).

## What the text does not answer

- Whether an audit sooner than two years after the last is "biennial" (F-1); what a missing local standard for fluid milk means (F-2); whether the State agency's own error excuses a retention under section 2015(b) (F-3).
- The liability amount of a State agency whose payment error rate is under 6 percent (F-4).
- How overlapping costs in section 2025(g)(2) are counted (F-8).
- What follows when the Secretary does not approve a plan that does not comply, or does not decide by 1 August: the text says what the Secretary shall do with a plan that complies and with one that does not, and says nothing of a missed date.
- What follows a missed deadline in sections 2025(c)(8), 2025(k)(4) and 2028(b)(2) beyond the `LEST BREACH BY` the encoding records (the text gives no remedy; the breach is recorded, no consequence is invented).
- What a "significant growth" in caseload is beyond the example "such as a 15 percent growth" (section 2025(c)(9)(C)), and whether "good cause" outside subsection (c) is the same list (finding 1).
- The cash share of a Puerto Rico plan for any fiscal year but 2017 to 2021 (finding 10).
- The amount of the block grant before fiscal year 2003 (finding 11).

## What `check.sh` prints

Run in this folder, 2026-11-04, with `L4` the stable build (1.6.98, main, 7689b0d, 2026-10-19) and `L4_MAIN` the main build 1.6.108 (main, 2ae7c9b, 2026-11-02); target main, the default; the script's exit status was 0 (the line `exit=` is not part of its output and is not in the block below, which is its output as printed).
Baseline: `expected_failed` is 0 for every module (no entry added), so the baseline number of expected failures is 0 and the numbers below replace none.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
snap-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap5-cases-seat.l4                            0        82       0        0         0 |      0        82       0        0  same
snap5-s2025-ab.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-c1.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-c2.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-dfij.l4                            0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-gh.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-hf.l4                              0         0       0        0         0 |      0         0       0        0  same
snap5-s2025-k.l4                               0         0       0        0         0 |      0         0       0        0  same
snap5-s2026a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap5-s2028.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap5-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap5-tests-s2025-ab.l4                        0        84       0        0         0 |      0        84       0        0  same
snap5-tests-s2025-c1.l4                        0        75       0        0         0 |      0        75       0        0  same
snap5-tests-s2025-c2.l4                        0       110       0        0         0 |      0       110       0        0  same
snap5-tests-s2025-dfij.l4                      0        85       0        0         0 |      0        85       0        0  same
snap5-tests-s2025-duties.l4                    0        47       0        0         0 |      0        47       0        0  same
snap5-tests-s2025-gh.l4                        0       187       0        0         0 |      0       187       0        0  same
snap5-tests-s2025-hf.l4                        0       180       0        0         0 |      0       180       0        0  same
snap5-tests-s2025-k.l4                         0        88       0        0         0 |      0        88       0        0  same
snap5-tests-s2026a.l4                          0        54       0        0         0 |      0        54       0        0  same
snap5-tests-s2028.l4                           0       149       0        0         0 |      0       149       0        0  same
TOTAL (23 modules)                             0      1141       0        0           |      0      1141       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Nothing here changes the module counts reported above: 1141 assertions satisfied on both builds, 0 failed, 0 refused, 0 errors, 23 modules (22 of them mine, plus the keel's `snap-core.l4`).

## Peeked

Until the lead's triage message (2026-11-04), nothing.
That was checked by listing every file this session read or searched, from its own transcript: only `BRIEF.md`, `snap-core.l4`, and files under `inputs/` (`COMMONS-CLAUDE.md`, `ENCODING-GUIDE.md`, `EXAMPLE-sg-employment-act-seat/ea-seat.l4`, `KEEL-NOTES.md`, `PLAN.md`, `usc07-ch51.txt`).
No skill reference, no other run's folder, nothing under `~/.claude/`, and no existing encoding was opened.

After that message, and as the lead instructed, the session read the list of failing assertions the lead pointed to (a file under `~/.claude/state/`), and, read-only, the independent reviewer's `tests-independent.l4` and `ANSWERS.md`.
Nothing in those files changed a branch, an expectation or a signature.

After the session's context was compacted, the harness also attached to it the text of three files that the lead had read or written in the lead's own session: `sections/pc42.md` (the independent-test-pass write-up of another encoding, which discusses the same FALSE and NOTHING convention), `ship_market.py` and a memory note about compaction.
The session did not open them and cites nothing from them.
The view that 546b should stay NOTHING, resting on the "without" ground and on the prohibition in s 2025(d)(3), was already in the session's own notes before they arrived; the other prohibitions it compares with were found afterwards, by reading this encoding's own modules.
