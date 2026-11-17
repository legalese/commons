# NOTES -- part ccc28 of the Criminal Code (Canada), R.S.C., 1985, c. C-46: PART XXIV, PART XXV and PART XXVI (lines 16296-16683)

Agent `ccc28`, run `dst-ccc28`, encoder Claude Sonnet 5.5, stable L4 (1.6.110 main e51181d, cross-checked on 1.6.109 main 4c887e0).

The text is a plain-text rendering, made by a converter script, of the English text of the Justice Laws Website consolidation current to 2026-09-30 (`inputs/SOURCES.md`); it is not the official text, and nothing here is claimed to have been verified against the official text.

The French version is equally authoritative and is not among the sources.

Where `inputs/PLAN.md` and the brief differ the brief governs.

One difference matters here: the brief says layer 1 imports `ccc-core` and `ccc-definitions`, and PLAN.md section 1 says a part imports the core only and takes every section 2 answer as an input named for its section.

This part imports `ccc-core` only and takes the one section 2 answer it needs as an input named `s 2 <term>: <the thing asked>`, because nothing in the range needs a call into `ccc-definitions` (each section 2 fact needed here is a fact the person states).

Files: layer 1 is `ccc28-part24-s752.l4` (s 752), `ccc28-part24a-dangerous-offender.l4` (ss 752.01 to 753.02), `ccc28-part24b-long-term.l4` (ss 753.1 to 755), `ccc28-part24c-hearing-appeal.l4` (ss 757 to 761), `ccc28-part25-forfeiture.l4` (ss 762 to 773), `ccc28-part26-extraordinary-remedies.l4` (ss 774 to 784), each with a `ccc28-tests-*.l4`; layer 2 is `ccc28-seat.l4` and `ccc28-cases-seat.l4`.

## Coverage (ccc28)

Built by a script (`work/coverage.py`) from the text and from the `@ref ... (src:N-M)` spans of the modules.

Every one of the 383 non-blank lines of 16296-16683 falls in exactly one row (the script fails otherwise), so the table has 383 rows, one per line: a section, subsection, paragraph, subparagraph, defined term, table row, or heading.

Each row has one disposition: encoded 212, fork 50, repealed or blank in this text 7, inert 114.

Every `encoded` row has a test: 178 of the 207 layer-1 functions are named in a `ccc28-tests-*.l4` file, and the other 29 are helpers and listed-provision tables (the offence lists of s 752 and s 753.1(2)(a), the count and comparison helpers, the document-kind helpers) that are called by a rule that is tested, with each table row asserted through that rule.

Every `inert` row is reason 1 of the three (not operative: a heading, or the lead-in that introduces the definitions that follow): 112 headings and 2 lead-ins (lines 16300 and 16543), and none is reason 2 or reason 3.

The seven `repealed or blank in this text` rows are s 752 "designated offence" (b)(x) to (xii) (line 16317), s 753(6) (16428), s 753.1(4) and (5) (16462), s 756 (16500), s 759(1.1) (16515), s 759(3.1) and (3.2) (16524) and s 759(4.1) to (5) (16527); each shows `[Repealed, ...]` in the text.

The Schedule to Part XXV (lines 17389-17405) is in another part's range; s 762(1) takes the Schedule's columns as inputs (see Seams).

A `fork` row names the fork-register entry that licenses it (F1 to F15 and F3.1 to F3.8); the rows of groups F16 and F17 of the name-test sweep stay `encoded` here, because the sweep lists them in the fork register only.


| Line | Unit | Disposition | L4 name(s), or the reason | Fork |
|---|---|---|---|---|
| 16296 | heading: PART XXIV Dangerous Offenders and Long-term Offenders | inert | reason 1 (not operative: a heading) |  |
| 16298 | heading: Interpretation | inert | reason 1 (not operative: a heading) |  |
| 16299 | heading: Definitions | inert | reason 1 (not operative: a heading) |  |
| 16300 | s 752 lead-in | inert | reason 1 (not operative: introduces the definitions that follow) |  |
| 16301 | s 752 "court" | encoded | `s 752 court` |  |
| 16302 | s 752 "designated offence" | encoded | `s 752 the offence is a designated offence` |  |
| 16303 | s 752 "designated offence" (a) | encoded | `s 752 the offence is a designated offence` |  |
| 16304 | s 752 "designated offence" (b) | encoded | `s 752 designated offence (b) the listed provisions`; `s 752 designated offence (b), (c) and (c.1) the offence is one of those` |  |
| 16305 | s 752 "designated offence" (b)(i) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16306 | s 752 "designated offence" (b)(ii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16307 | s 752 "designated offence" (b)(iii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16308 | s 752 "designated offence" (b)(iv) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16309 | s 752 "designated offence" (b)(iv.1) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16310 | s 752 "designated offence" (b)(iv.2) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16311 | s 752 "designated offence" (b)(v) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16312 | s 752 "designated offence" (b)(vi) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16313 | s 752 "designated offence" (b)(vii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16314 | s 752 "designated offence" (b)(viii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16315 | s 752 "designated offence" (b)(ix) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16316 | s 752 "designated offence" (b)(ix.1) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16317 | s 752 "designated offence" (b)(x) | repealed or blank in this text | (x) to (xii) [Repealed, 2014, c. 25, s. 29] |  |
| 16318 | s 752 "designated offence" (b)(xiii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16319 | s 752 "designated offence" (b)(xiv) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16320 | s 752 "designated offence" (b)(xv) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16321 | s 752 "designated offence" (b)(xvi) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16322 | s 752 "designated offence" (b)(xvii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16323 | s 752 "designated offence" (b)(xviii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16324 | s 752 "designated offence" (b)(xix) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16325 | s 752 "designated offence" (b)(xx) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16326 | s 752 "designated offence" (b)(xx.1) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16327 | s 752 "designated offence" (b)(xx.2) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16328 | s 752 "designated offence" (b)(xx.3) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16329 | s 752 "designated offence" (b)(xxi) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16330 | s 752 "designated offence" (b)(xxii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16331 | s 752 "designated offence" (b)(xxiii) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16332 | s 752 "designated offence" (b)(xxiii.1) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16333 | s 752 "designated offence" (b)(xxiii.2) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16334 | s 752 "designated offence" (b)(xxiii.3) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16335 | s 752 "designated offence" (b)(xxiii.4) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16336 | s 752 "designated offence" (b)(xxiii.5) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16337 | s 752 "designated offence" (b)(xxiii.6) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16338 | s 752 "designated offence" (b)(xxiii.7) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16339 | s 752 "designated offence" (b)(xxiii.8) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16340 | s 752 "designated offence" (b)(xxiv) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16341 | s 752 "designated offence" (b)(xxv) | encoded | `s 752 designated offence (b) the listed provisions` |  |
| 16342 | s 752 "designated offence" (c) | encoded | `s 752 designated offence (c) the listed provisions` |  |
| 16343 | s 752 "designated offence" (c)(i) | encoded | `s 752 designated offence (c) the listed provisions` |  |
| 16344 | s 752 "designated offence" (c)(ii) | encoded | `s 752 designated offence (c) the listed provisions` |  |
| 16345 | s 752 "designated offence" (c)(iii) | encoded | `s 752 designated offence (c) the listed provisions` |  |
| 16346 | s 752 "designated offence" (c)(iv) | encoded | `s 752 designated offence (c) the listed provisions` |  |
| 16347 | s 752 "designated offence" (c.1) | encoded | `s 752 designated offence (c.1) the listed provisions` |  |
| 16348 | s 752 "designated offence" (c.1)(i) | encoded | `s 752 designated offence (c.1) the listed provisions` |  |
| 16349 | s 752 "designated offence" (c.1)(ii) | encoded | `s 752 designated offence (c.1) the listed provisions` |  |
| 16350 | s 752 "designated offence" (c.1)(iii) | encoded | `s 752 designated offence (c.1) the listed provisions` |  |
| 16351 | s 752 "designated offence" (c.1)(iv) | encoded | `s 752 designated offence (c.1) the listed provisions` |  |
| 16352 | s 752 "designated offence" (d) | encoded | `s 752 designated offence (d) the offence is an attempt or conspiracy to commit one of thos`... |  |
| 16353 | s 752 "long-term supervision" | encoded | `type s 752 the order under which the supervision was ordered`; `s 752 long-term supervision` |  |
| 16354 | s 752 "primary designated offence" | encoded | `s 752 the offence is a primary designated offence` |  |
| 16355 | s 752 "primary designated offence" (a) | encoded | `s 752 primary designated offence (a) the listed provisions`; `s 752 primary designated offence (a) to (d) the offence is one of those` |  |
| 16356 | s 752 "primary designated offence" (a)(i) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16357 | s 752 "primary designated offence" (a)(ii) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16358 | s 752 "primary designated offence" (a)(iii) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16359 | s 752 "primary designated offence" (a)(iv) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16360 | s 752 "primary designated offence" (a)(v) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16361 | s 752 "primary designated offence" (a)(vi) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16362 | s 752 "primary designated offence" (a)(vii) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16363 | s 752 "primary designated offence" (a)(viii) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16364 | s 752 "primary designated offence" (a)(ix) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16365 | s 752 "primary designated offence" (a)(x) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16366 | s 752 "primary designated offence" (a)(xi) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16367 | s 752 "primary designated offence" (a)(xii) | encoded | `s 752 primary designated offence (a) the listed provisions` |  |
| 16368 | s 752 "primary designated offence" (b) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16369 | s 752 "primary designated offence" (b)(i) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16370 | s 752 "primary designated offence" (b)(ii) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16371 | s 752 "primary designated offence" (b)(iii) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16372 | s 752 "primary designated offence" (b)(iv) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16373 | s 752 "primary designated offence" (b)(v) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16374 | s 752 "primary designated offence" (b)(vi) | encoded | `s 752 primary designated offence (b) the listed provisions` |  |
| 16375 | s 752 "primary designated offence" (c) | encoded | `s 752 primary designated offence (c) the listed provisions` |  |
| 16376 | s 752 "primary designated offence" (c)(i) | encoded | `s 752 primary designated offence (c) the listed provisions` |  |
| 16377 | s 752 "primary designated offence" (c)(ii) | encoded | `s 752 primary designated offence (c) the listed provisions` |  |
| 16378 | s 752 "primary designated offence" (c)(iii) | encoded | `s 752 primary designated offence (c) the listed provisions` |  |
| 16379 | s 752 "primary designated offence" (d) | encoded | `s 752 primary designated offence (d) the listed provisions` |  |
| 16380 | s 752 "primary designated offence" (d)(i) | encoded | `s 752 primary designated offence (d) the listed provisions` |  |
| 16381 | s 752 "primary designated offence" (d)(ii) | encoded | `s 752 primary designated offence (d) the listed provisions` |  |
| 16382 | s 752 "primary designated offence" (e) | encoded | `s 752 primary designated offence (e) the offence is an attempt or conspiracy to commit one`... |  |
| 16383 | s 752 "serious personal injury offence" | encoded | `s 752 the offence is a serious personal injury offence` |  |
| 16384 | s 752 "serious personal injury offence" (a) | encoded | `s 752 serious personal injury offence (a)` |  |
| 16385 | s 752 "serious personal injury offence" (a)(i) | encoded | `s 752 serious personal injury offence (a)` |  |
| 16386 | s 752 "serious personal injury offence" (a)(ii) | encoded | `s 752 serious personal injury offence (a)` |  |
| 16387 | s 752 "serious personal injury offence" (b) | encoded | `s 752 serious personal injury offence (b) the listed provisions`; `s 752 serious personal injury offence (b)` |  |
| 16389 | heading: Dangerous Offenders and Long-Term Offenders | inert | reason 1 (not operative: a heading) |  |
| 16390 | heading: Prosecutor’s duty to advise court | inert | reason 1 (not operative: a heading) |  |
| 16391 | s 752.01 | fork | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an a`...; `s 752.01 the prosecutor's duty to advise the court`; `s 752.01 the prosecutor advised the court before sentence was imposed` | F1 |
| 16392 | s 752.01(a) | fork | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an a`...; `s 752.01 the prosecutor's duty to advise the court`; `s 752.01 the prosecutor advised the court before sentence was imposed` | F2 |
| 16393 | s 752.01(b) | fork | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an a`...; `s 752.01 the prosecutor's duty to advise the court`; `s 752.01 the prosecutor advised the court before sentence was imposed` | F2 |
| 16394 | heading: Application for remand for assessment | inert | reason 1 (not operative: a heading) |  |
| 16395 | s 752.1(1) | encoded | `s 752.1(1) the court shall remand the offender for an assessment`; `s 752.1(1) the remand is for a period not exceeding 60 days`; `s 752.1(1) the court's duty to remand the offender` |  |
| 16396 | heading: Report | inert | reason 1 (not operative: a heading) |  |
| 16397 | s 752.1(2) | encoded | `s 752.1(2) the duty of the person to whom the offender is remanded`; `s 752.1(2) the report is filed not later than 30 days after the end of the assessment peri`...; `s 752.1(2) the last day on which the report is filed in time` |  |
| 16398 | heading: Extension of time | inert | reason 1 (not operative: a heading) |  |
| 16399 | s 752.1(3) | fork | `s 752.1(3) the court may extend the period within which the report must be filed`; `s 752.1(3) the extension is by a maximum of 30 days` | F3.1 |
| 16400 | heading: Application for finding that an offender is a dangerous offe | inert | reason 1 (not operative: a heading) |  |
| 16401 | s 753(1) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16402 | s 753(1)(a) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16403 | s 753(1)(a)(i) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16404 | s 753(1)(a)(ii) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16405 | s 753(1)(a)(iii) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16406 | s 753(1)(b) | encoded | `s 753(1) the court shall find the offender to be a dangerous offender` |  |
| 16407 | heading: Presumption | inert | reason 1 (not operative: a heading) |  |
| 16408 | s 753(1.1) | fork | `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` | F2 |
| 16409 | heading: Time for making application | inert | reason 1 (not operative: a heading) |  |
| 16410 | s 753(2) | fork | `s 753(2) the application is made not later than six months after the imposition of sentenc`...; `s 753(2)(a) the notice was given and the application is not later than six months after th`...; `s 753(2)(b) relevant evidence became available in the interim and the application is not l`... (+2 more) | F4 |
| 16411 | s 753(2)(a) | fork | `s 753(2) the application is made not later than six months after the imposition of sentenc`...; `s 753(2)(a) the notice was given and the application is not later than six months after th`...; `s 753(2)(b) relevant evidence became available in the interim and the application is not l`... (+2 more) | F4 |
| 16412 | s 753(2)(b) | fork | `s 753(2) the application is made not later than six months after the imposition of sentenc`...; `s 753(2)(a) the notice was given and the application is not later than six months after th`...; `s 753(2)(b) relevant evidence became available in the interim and the application is not l`... (+2 more) | F4 |
| 16413 | heading: Application for remand for assessment after imposition of se | inert | reason 1 (not operative: a heading) |  |
| 16414 | s 753(3) | encoded | `s 753(3) an application under subsection 752.1(1) may be made after the imposition of sent`... |  |
| 16415 | heading: Sentence for dangerous offender | inert | reason 1 (not operative: a heading) |  |
| 16416 | s 753(4) | encoded | `s 753(4) the disposition is within paragraph (a), (b) or (c)` |  |
| 16417 | s 753(4)(a) | encoded | `s 753(4) the disposition is within paragraph (a), (b) or (c)` |  |
| 16418 | s 753(4)(b) | encoded | `s 753(4) the disposition is within paragraph (a), (b) or (c)` |  |
| 16419 | s 753(4)(c) | encoded | `s 753(4) the disposition is within paragraph (a), (b) or (c)` |  |
| 16420 | heading: Sentence of indeterminate detention | inert | reason 1 (not operative: a heading) |  |
| 16421 | s 753(4.1) | encoded | `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeter`... |  |
| 16422 | heading: If application made after sentencing | inert | reason 1 (not operative: a heading) |  |
| 16423 | s 753(4.2) | encoded | `s 753(4.2) the sentence imposed replaces the sentence that was imposed for the offence` |  |
| 16424 | heading: If offender not found to be dangerous offender | inert | reason 1 (not operative: a heading) |  |
| 16425 | s 753(5) | fork | `s 753(5) the court may take this course` | F3.2 |
| 16426 | s 753(5)(a) | fork | `s 753(5) the court may take this course` | F3.2 |
| 16427 | s 753(5)(b) | fork | `s 753(5) the court may take this course` | F3.2 |
| 16428 | s 753(6) | repealed or blank in this text | (6) [Repealed, 2008, c. 6, s. 42] |  |
| 16429 | heading: Application for remand for assessment — later conviction | inert | reason 1 (not operative: a heading) |  |
| 16430 | s 753.01(1) | encoded | `s 753.01(1) the court shall remand the offender for an assessment`; `s 753.01(1) the remand is for a period not exceeding 60 days` |  |
| 16431 | heading: Report | inert | reason 1 (not operative: a heading) |  |
| 16432 | s 753.01(2) | encoded | `s 753.01(2) the duty of the person to whom the offender is remanded`; `s 753.01(2) the report is filed not later than 30 days after the end of the assessment per`... |  |
| 16433 | heading: Extension of time | inert | reason 1 (not operative: a heading) |  |
| 16434 | s 753.01(3) | fork | `s 753.01(3) the court may extend the period within which the report must be filed`; `s 753.01(3) the extension is by a maximum of 30 days` | F3.3 |
| 16435 | heading: Application for new sentence or order | inert | reason 1 (not operative: a heading) |  |
| 16436 | s 753.01(4) | encoded | `s 753.01(4) the prosecutor may apply for this sentence or order` |  |
| 16437 | heading: Sentence of indeterminate detention | inert | reason 1 (not operative: a heading) |  |
| 16438 | s 753.01(5) | encoded | `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indete`... |  |
| 16439 | heading: New long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16440 | s 753.01(6) | encoded | `s 753.01(6) the court shall order that the offender be subject to a new period of long-ter`... |  |
| 16441 | heading: Victim evidence | inert | reason 1 (not operative: a heading) |  |
| 16442 | s 753.02 | encoded | `s 753.02 the evidence is deemed also to have been given during the hearing` |  |
| 16443 | heading: Application for finding that an offender is a long-term offe | inert | reason 1 (not operative: a heading) |  |
| 16444 | s 753.1(1) | fork | `s 753.1(1) the court may find the offender to be a long-term offender` | F3.4 |
| 16445 | s 753.1(1)(a) | fork | `s 753.1(1) the court may find the offender to be a long-term offender` | F3.4 |
| 16446 | s 753.1(1)(b) | fork | `s 753.1(1) the court may find the offender to be a long-term offender` | F3.4 |
| 16447 | s 753.1(1)(c) | fork | `s 753.1(1) the court may find the offender to be a long-term offender` | F3.4 |
| 16448 | heading: Substantial risk | inert | reason 1 (not operative: a heading) |  |
| 16449 | s 753.1(2) | encoded | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender`... |  |
| 16450 | s 753.1(2)(a) | encoded | `s 753.1(2)(a) the listed provisions`; `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender`... |  |
| 16451 | s 753.1(2)(b) | encoded | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender`... |  |
| 16452 | s 753.1(2)(b)(i) | encoded | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender`... |  |
| 16453 | s 753.1(2)(b)(ii) | encoded | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender`... |  |
| 16454 | heading: Sentence for long-term offender | inert | reason 1 (not operative: a heading) |  |
| 16455 | s 753.1(3) | encoded | `s 753.1(3) the sentence and order are within paragraphs (a) and (b)` |  |
| 16456 | s 753.1(3)(a) | encoded | `s 753.1(3) the sentence and order are within paragraphs (a) and (b)` |  |
| 16457 | s 753.1(3)(b) | encoded | `s 753.1(3) the sentence and order are within paragraphs (a) and (b)` |  |
| 16458 | heading: Exception — if application made after sentencing | inert | reason 1 (not operative: a heading) |  |
| 16459 | s 753.1(3.1) | encoded | `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)` |  |
| 16460 | s 753.1(3.1)(a) | encoded | `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)` |  |
| 16461 | s 753.1(3.1)(b) | encoded | `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)` |  |
| 16462 | s 753.1(4) | repealed or blank in this text | (4) and (5) [Repealed, 2008, c. 6, s. 44] |  |
| 16463 | heading: If offender not found to be long-term offender | inert | reason 1 (not operative: a heading) |  |
| 16464 | s 753.1(6) | encoded | `s 753.1(6) the court shall impose sentence for the offence` |  |
| 16465 | heading: Long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16466 | s 753.2(1) | encoded | `s 753.2(1) the offender shall be supervised in the community` |  |
| 16467 | s 753.2(1)(a) | encoded | `s 753.2(1) the offender shall be supervised in the community` |  |
| 16468 | s 753.2(1)(b) | encoded | `s 753.2(1) the offender shall be supervised in the community` |  |
| 16469 | heading: Sentence served concurrently with supervision | inert | reason 1 (not operative: a heading) |  |
| 16470 | s 753.2(2) | fork | `s 753.2(2) the sentence is to be served concurrently with the long-term supervision` | F5 |
| 16471 | heading: Application for reduction in period of long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16472 | s 753.2(3) | encoded | `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long`...; `s 753.2(3) the onus of proving the ground is on the applicant` |  |
| 16473 | heading: Notice to Attorney General | inert | reason 1 (not operative: a heading) |  |
| 16474 | s 753.2(4) | encoded | `s 753.2(4) the duty of the applicant to give notice to the Attorney General`; `s 753.2(4) the notice is given at the time the application is made` |  |
| 16475 | heading: Breach of long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16476 | s 753.3(1) | fork | `s 753.3(1) the offender is guilty of an offence` | F6 |
| 16477 | s 753.3(1)(a) | fork | `s 753.3(1) the offender is guilty of an offence` | F6 |
| 16478 | s 753.3(1)(b) | fork | `s 753.3(1) the offender is guilty of an offence` | F6 |
| 16479 | heading: Where accused may be tried and punished | inert | reason 1 (not operative: a heading) |  |
| 16480 | s 753.3(2) | encoded | `s 753.3(2) the accused may be tried and punished in this place` |  |
| 16481 | heading: New offence | inert | reason 1 (not operative: a heading) |  |
| 16482 | s 753.4(1) | fork | `s 753.4(1) the long-term supervision is interrupted` | F7 |
| 16483 | heading: Reduction in term of long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16484 | s 753.4(2) | encoded | `s 753.4(2) the court may order a reduction in the length of the period of long-term superv`... |  |
| 16485 | heading: Hearing of application | inert | reason 1 (not operative: a heading) |  |
| 16486 | s 754(1) | fork | `s 754(1) the court may not hear the application` | F8 |
| 16487 | s 754(1)(a) | fork | `s 754(1) the court may not hear the application` | F8 |
| 16488 | s 754(1)(b) | fork | `s 754(1) the court may not hear the application` | F8 |
| 16489 | s 754(1)(c) | fork | `s 754(1) the court may not hear the application` | F8 |
| 16490 | heading: By court alone | inert | reason 1 (not operative: a heading) |  |
| 16491 | s 754(2) | encoded | `s 754(2) the application is heard and determined by the court without a jury` |  |
| 16492 | heading: When proof unnecessary | inert | reason 1 (not operative: a heading) |  |
| 16493 | s 754(3) | encoded | `s 754(3) no proof of the allegations is required` |  |
| 16494 | heading: Proof of consent | inert | reason 1 (not operative: a heading) |  |
| 16495 | s 754(4) | encoded | `s 754(4) the document is proof of the nomination or consent` |  |
| 16496 | heading: Exception to long-term supervision — life sentence | inert | reason 1 (not operative: a heading) |  |
| 16497 | s 755(1) | encoded | `s 755(1) the court shall not order that the offender be subject to long-term supervision` |  |
| 16498 | heading: Maximum length of long-term supervision | inert | reason 1 (not operative: a heading) |  |
| 16499 | s 755(2) | fork | `s 755(2) the total number of whole months of the periods`; `s 755(2) the periods of long-term supervision do not total more than 10 years` | F9 |
| 16500 | s 756 | repealed or blank in this text | 756 [Repealed, 1997, c. 17, s. 5] |  |
| 16501 | heading: Evidence of character | inert | reason 1 (not operative: a heading) |  |
| 16502 | s 757 | fork | `s 757 evidence of character and repute may be admitted` | F3.5 |
| 16503 | s 757(a) | fork | `s 757 evidence of character and repute may be admitted` | F3.5 |
| 16504 | s 757(b) | fork | `s 757 evidence of character and repute may be admitted` | F3.5 |
| 16505 | heading: Presence of accused at hearing of application | inert | reason 1 (not operative: a heading) |  |
| 16506 | s 758(1) | encoded | `s 758(1) the offender shall be present at the hearing of the application` |  |
| 16507 | s 758(1)(a) | fork | `s 758(1)(a) the court may order the person having the custody of the accused to bring the `...; `s 758(1)(a) the court's power to order the person having the custody to bring the offender` | F3.6 |
| 16508 | s 758(1)(b) | encoded | `s 758(1)(b) the court shall issue a summons or a warrant to compel the accused to attend b`... |  |
| 16509 | heading: Exception | inert | reason 1 (not operative: a heading) |  |
| 16510 | s 758(2) | encoded | `s 758(2)(a) the court may cause the offender to be removed and kept out of court` |  |
| 16511 | s 758(2)(a) | encoded | `s 758(2)(a) the court may cause the offender to be removed and kept out of court` |  |
| 16512 | s 758(2)(b) | encoded | `s 758(2)(b) the court may permit the offender to be out of court` |  |
| 16513 | heading: Appeal — offender | inert | reason 1 (not operative: a heading) |  |
| 16514 | s 759(1) | encoded | `s 759(1) the offender may appeal to the court of appeal` |  |
| 16515 | s 759(1.1) | repealed or blank in this text | (1.1) [Repealed, 2008, c. 6, s. 51] |  |
| 16516 | heading: Appeal — Attorney General | inert | reason 1 (not operative: a heading) |  |
| 16517 | s 759(2) | encoded | `s 759(2) the Attorney General may appeal to the court of appeal` |  |
| 16518 | heading: Disposition of appeal | inert | reason 1 (not operative: a heading) |  |
| 16519 | s 759(3) | encoded | `s 759(3) the court of appeal may make this disposition` |  |
| 16520 | s 759(3)(a) | encoded | `s 759(3) the court of appeal may make this disposition` |  |
| 16521 | s 759(3)(a)(i) | encoded | `s 759(3) the court of appeal may make this disposition` |  |
| 16522 | s 759(3)(a)(ii) | encoded | `s 759(3) the court of appeal may make this disposition` |  |
| 16523 | s 759(3)(b) | encoded | `s 759(3) the court of appeal may make this disposition` |  |
| 16524 | s 759(3.1) | repealed or blank in this text | (3.1) and (3.2) [Repealed, 2008, c. 6, s. 51] |  |
| 16525 | heading: Effect of decision | inert | reason 1 (not operative: a heading) |  |
| 16526 | s 759(4) | encoded | `s 759(4) the decision has the same force and effect as a decision of the trial court` |  |
| 16527 | s 759(4.1) | repealed or blank in this text | (4.1) to (5) [Repealed, 2008, c. 6, s. 51] |  |
| 16528 | heading: Commencement of sentence | inert | reason 1 (not operative: a heading) |  |
| 16529 | s 759(6) | encoded | `s 759(6) the day the sentence is deemed to have commenced` |  |
| 16530 | heading: Part XXI applies re appeals | inert | reason 1 (not operative: a heading) |  |
| 16531 | s 759(7) | encoded | `s 759(7) the provisions of Part XXI with respect to procedure on appeals apply to the appe`... |  |
| 16532 | heading: Disclosure to Correctional Service of Canada | inert | reason 1 (not operative: a heading) |  |
| 16533 | s 760 | encoded | `s 760 the court shall order that the reports, testimony, observations and transcript be fo`...; `s 760 the court's duty to order disclosure to the Correctional Service of Canada` |  |
| 16534 | heading: Review for parole | inert | reason 1 (not operative: a heading) |  |
| 16535 | s 761(1) | fork | `s 761(1) the day on which seven years from the day the person was taken into custody have `...; `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances `...; `s 761(1) the first review is after the expiration of seven years` (+2 more) | F1,F4 |
| 16536 | heading: Idem | inert | reason 1 (not operative: a heading) |  |
| 16537 | s 761(2) | fork | `s 761(2) the Parole Board of Canada shall review the condition, history and circumstances `...; `s 761(2) the review is within a year of the previous review`; `s 761(2) the duty of the Parole Board of Canada to review the person at least once in ever`... | F4 |
| 16539 | heading: PART XXV Effect and Enforcement of Undertakings, Release Ord | inert | reason 1 (not operative: a heading) |  |
| 16540 | heading: Applications for forfeiture | inert | reason 1 (not operative: a heading) |  |
| 16541 | s 762(1) | encoded | `s 762(1) the application for forfeiture is made to the court the schedule designates` |  |
| 16542 | heading: Definitions | inert | reason 1 (not operative: a heading) |  |
| 16543 | s 762(2) lead-in | inert | reason 1 (not operative: introduces the definitions that follow) |  |
| 16544 | s 762(2) "clerk of the court" | encoded | `s 762(2) the person is the clerk of the court` |  |
| 16545 | s 762(2) "schedule" | encoded | `s 762(2) the document is the schedule` |  |
| 16546 | heading: Undertaking or release order binding on person | inert | reason 1 (not operative: a heading) |  |
| 16547 | s 763(1) | encoded | `s 763(1) the person and their sureties continue to be bound` |  |
| 16548 | heading: Summary of certain provisions | inert | reason 1 (not operative: a heading) |  |
| 16549 | s 763(2) | fork | `s 763(2) the document sets out a summary of section 763 as it must` | F10 |
| 16550 | heading: Undertaking or release order binding on accused | inert | reason 1 (not operative: a heading) |  |
| 16551 | s 764(1) | encoded | `s 764(1) the undertaking or release order continues to bind the accused and their sureties`... |  |
| 16552 | heading: Committal or new sureties | inert | reason 1 (not operative: a heading) |  |
| 16553 | s 764(2) | encoded | `s 764(2) the court, provincial court judge or justice may take this step` |  |
| 16554 | heading: Effect of committal | inert | reason 1 (not operative: a heading) |  |
| 16555 | s 764(3) | encoded | `s 764(3) the sureties of the accused are discharged` |  |
| 16556 | heading: Summary of certain provisions | inert | reason 1 (not operative: a heading) |  |
| 16557 | s 764(4) | fork | `s 764(4) the document sets out a summary of subsections (1) to (3) as it must` | F10 |
| 16558 | heading: Effect of subsequent arrest | inert | reason 1 (not operative: a heading) |  |
| 16559 | s 765 | encoded | `s 765 the undertaking or release order continues to bind the accused and their sureties de`... |  |
| 16560 | heading: Render of accused by sureties | inert | reason 1 (not operative: a heading) |  |
| 16561 | s 766(1) | encoded | `s 766(1) the surety may apply to be relieved of their obligation`; `s 766(1) the court, provincial court judge or justice shall make an order in writing for c`...; `s 766(1) the court's duty to commit the person on the surety's application` |  |
| 16562 | heading: Arrest | inert | reason 1 (not operative: a heading) |  |
| 16563 | s 766(2) | fork | `s 766(2) the order is given to the surety as it must be`; `s 766(2) the keeper's duty to receive and imprison the person` | F11 |
| 16564 | heading: Certificate and entry of render | inert | reason 1 (not operative: a heading) |  |
| 16565 | s 766(3) | encoded | `s 766(3) the court, provincial court judge or justice shall order an entry of the committa`...; `s 766(3) the court's duty to order an entry of the committal to be endorsed` |  |
| 16566 | heading: Discharge of sureties | inert | reason 1 (not operative: a heading) |  |
| 16567 | s 766(4) | encoded | `s 766(4) the release order or recognizance is cancelled and the sureties are discharged` |  |
| 16568 | heading: Render of accused in court by sureties | inert | reason 1 (not operative: a heading) |  |
| 16569 | s 767 | encoded | `s 767 the surety may bring the person before the court`; `s 767 the surety discharges their obligation under the release order or recognizance`; `s 767 the court shall commit the person to prison` (+1 more) |  |
| 16570 | heading: Substitution of surety | inert | reason 1 (not operative: a heading) |  |
| 16571 | s 767.1(1) | fork | `s 767.1(1) the court, justice or provincial court judge may substitute another person for `... | F3.7 |
| 16572 | heading: Signing of release order or recognizance by new sureties | inert | reason 1 (not operative: a heading) |  |
| 16573 | s 767.1(2) | encoded | `s 767.1(2) the original surety is discharged` |  |
| 16574 | heading: Rights of surety preserved | inert | reason 1 (not operative: a heading) |  |
| 16575 | s 768 | encoded | `s 768 this Part limits the surety's right of taking and giving the person into custody` |  |
| 16576 | heading: Application of judicial interim release provisions | inert | reason 1 (not operative: a heading) |  |
| 16577 | s 769 | encoded | `s 769 the interim release provisions of Parts XVI, XXI and XXVII apply in respect of the p`... |  |
| 16578 | heading: Default to be endorsed | inert | reason 1 (not operative: a heading) |  |
| 16579 | s 770(1) | encoded | `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorse`...; `s 770(1) the duty of the court, provincial court judge or justice to endorse the certifica`... |  |
| 16580 | s 770(1)(a) | encoded | `s 770(1) the certificate is as the subsection requires` |  |
| 16581 | s 770(1)(b) | encoded | `s 770(1) the certificate is as the subsection requires` |  |
| 16582 | s 770(1)(c) | encoded | `s 770(1) the certificate is as the subsection requires` |  |
| 16583 | s 770(1)(d) | encoded | `s 770(1) the certificate is as the subsection requires` |  |
| 16584 | heading: Transmission to clerk of court | inert | reason 1 (not operative: a heading) |  |
| 16585 | s 770(2) | fork | `s 770(2) the document is sent to the clerk of the court as it must be` | F11 |
| 16586 | heading: Certificate is evidence | inert | reason 1 (not operative: a heading) |  |
| 16587 | s 770(3) | encoded | `s 770(3) the certificate is evidence of the default to which it relates` |  |
| 16588 | heading: Transmission of deposit | inert | reason 1 (not operative: a heading) |  |
| 16589 | s 770(4) | encoded | `s 770(4) the money is sent to the clerk of the court with the defaulted document as it mus`... |  |
| 16590 | heading: Proceedings in case of default | inert | reason 1 (not operative: a heading) |  |
| 16591 | s 771(1) | encoded | `s 771(1)(a) a judge of the court shall fix a time and place for the hearing of an applicat`... |  |
| 16592 | s 771(1)(a) | encoded | `s 771(1)(a) a judge of the court shall fix a time and place for the hearing of an applicat`... |  |
| 16593 | s 771(1)(b) | encoded | `s 771(1)(b) the clerk of the court sends the notice as the paragraph requires`; `s 771(1)(b) the clerk of the court's duty to send the notice` |  |
| 16594 | heading: Order of judge | inert | reason 1 (not operative: a heading) |  |
| 16595 | s 771(2) | fork | `s 771(2) the judge may take this course` | F3.8 |
| 16596 | heading: Judgment debtors of the Crown | inert | reason 1 (not operative: a heading) |  |
| 16597 | s 771(3) | encoded | `s 771(3) the principal and their sureties become judgment debtors of the Crown` |  |
| 16598 | heading: Order may be filed | inert | reason 1 (not operative: a heading) |  |
| 16599 | s 771(3.1) | encoded | `s 771(3.1) the order may be filed with the clerk of the superior court`; `s 771(3.1) the clerk shall issue a writ of fieri facias and deliver it to the sheriff of t`...; `s 771(3.1) the clerk's duty to issue and deliver the writ` |  |
| 16600 | heading: Transfer of deposit | inert | reason 1 (not operative: a heading) |  |
| 16601 | s 771(4) | encoded | `s 771(4) no writ of fieri facias may be issued` |  |
| 16602 | heading: Levy under writ | inert | reason 1 (not operative: a heading) |  |
| 16603 | s 772(1) | encoded | `s 772(1) the sheriff executes the writ and deals with the proceeds as the subsection requi`...; `s 772(1) the sheriff's duty to execute the writ` |  |
| 16604 | heading: Costs | inert | reason 1 (not operative: a heading) |  |
| 16605 | s 772(2) | fork | `s 772(2) the Crown is entitled to the costs of execution and of proceedings incidental the`...; `s 772(2) the tariff that fixes the costs` | F12 |
| 16606 | heading: Committal when writ not satisfied | inert | reason 1 (not operative: a heading) |  |
| 16607 | s 773(1) | encoded | `s 773(1) a judge of the court may fix a time and place for the sureties to show cause` |  |
| 16608 | heading: Notice | inert | reason 1 (not operative: a heading) |  |
| 16609 | s 773(2) | fork | `s 773(2) the number of clear days of notice`; `s 773(2) the notice given to the sureties is seven clear days notice` | F11 |
| 16610 | heading: Hearing | inert | reason 1 (not operative: a heading) |  |
| 16611 | s 773(3) | encoded | `s 773(3) the judge inquires into the circumstances of the case as the judge shall`; `s 773(3) the judge may make this order in their discretion` |  |
| 16612 | s 773(3)(a) | encoded | `s 773(3) the judge may make this order in their discretion` |  |
| 16613 | s 773(3)(b) | encoded | `s 773(3) the judge may make this order in their discretion` |  |
| 16614 | heading: Warrant to committal | inert | reason 1 (not operative: a heading) |  |
| 16615 | s 773(4) | encoded | `s 773(4) the warrant authorizes the sheriff to confine the person in this prison` |  |
| 16616 | heading: Definition of Attorney General | inert | reason 1 (not operative: a heading) |  |
| 16617 | s 773(5) | encoded | `s 773(5) the person is the Attorney General for the purposes of section 771 and this secti`... |  |
| 16619 | heading: PART XXVI Extraordinary Remedies | inert | reason 1 (not operative: a heading) |  |
| 16620 | heading: Application of Part | inert | reason 1 (not operative: a heading) |  |
| 16621 | s 774 | encoded | `s 774 this Part applies to the proceedings` |  |
| 16622 | heading: Appearance in person — habeas corpus | inert | reason 1 (not operative: a heading) |  |
| 16623 | s 774.1 | encoded | `s 774.1 the person who is the subject of a writ of habeas corpus appears in court in perso`...; `s 774.1 the duty of the person who is the subject of a writ of habeas corpus to appear in `... |  |
| 16624 | heading: Detention on inquiry to determine legality of imprisonment | inert | reason 1 (not operative: a heading) |  |
| 16625 | s 775 | encoded | `s 775 the judge or court may take this course without determining the question` |  |
| 16626 | heading: Where conviction or order not reviewable | inert | reason 1 (not operative: a heading) |  |
| 16627 | s 776 | encoded | `s 776 the conviction or order shall not be removed by certiorari` |  |
| 16628 | s 776(a) | encoded | `s 776 the conviction or order shall not be removed by certiorari` |  |
| 16629 | s 776(b) | encoded | `s 776 the conviction or order shall not be removed by certiorari` |  |
| 16630 | heading: Conviction or order remediable, when | inert | reason 1 (not operative: a heading) |  |
| 16631 | s 777(1) | encoded | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the`... |  |
| 16632 | s 777(1)(a) | encoded | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the`... |  |
| 16633 | s 777(1)(b) | encoded | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the`... |  |
| 16634 | s 777(1)(c) | encoded | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the`... |  |
| 16635 | s 777(1) closing clause | encoded | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the`...; `s 777(1) the court or judge has the same powers to deal with the proceedings as a court to`... |  |
| 16636 | heading: Correcting punishment | inert | reason 1 (not operative: a heading) |  |
| 16637 | s 777(2) | encoded | `s 777(2) the court or judge shall correct the sentence or remit the matter` |  |
| 16638 | s 777(2)(a) | fork | `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | F15 |
| 16639 | s 777(2)(a)(i) | fork | `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | F15 |
| 16640 | s 777(2)(a)(ii) | fork | `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | F15 |
| 16641 | s 777(2)(a)(iii) | fork | `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | F15 |
| 16642 | s 777(2)(b) | encoded | `s 777(2)(b) the punishment imposed on remittal is not greater than the punishment that may`... |  |
| 16643 | heading: Amendment | inert | reason 1 (not operative: a heading) |  |
| 16644 | s 777(3) | encoded | `s 777(3) the document shall be amended to conform to the adjudication as varied` |  |
| 16645 | heading: Sufficiency of statement | inert | reason 1 (not operative: a heading) |  |
| 16646 | s 777(4) | encoded | `s 777(4) the statement is sufficient for the purposes of the document` |  |
| 16647 | heading: Irregularities within section 777 | inert | reason 1 (not operative: a heading) |  |
| 16648 | s 778 | fork | `s 778 section 777 is deemed by this section to apply` | F13 |
| 16649 | s 778(a) | fork | `s 778 section 777 is deemed by this section to apply` | F13 |
| 16650 | s 778(b) | fork | `s 778 section 777 is deemed by this section to apply` | F13 |
| 16651 | s 778(c) | fork | `s 778 section 777 is deemed by this section to apply` | F13 |
| 16652 | heading: General order for security by recognizance | inert | reason 1 (not operative: a heading) |  |
| 16653 | s 779(1) | encoded | `s 779(1) the court may prescribe by general order that no motion to quash shall be heard u`... |  |
| 16654 | heading: Provisions of Part XXV | inert | reason 1 (not operative: a heading) |  |
| 16655 | s 779(2) | encoded | `s 779(2) the provisions of Part XXV relating to forfeiture of an amount set out in a recog`... |  |
| 16656 | heading: Effect of order dismissing application to quash | inert | reason 1 (not operative: a heading) |  |
| 16657 | s 780 | encoded | `s 780 the order refusing the application is sufficient authority for the clerk of the cour`... |  |
| 16658 | heading: Want of proof of order in council | inert | reason 1 (not operative: a heading) |  |
| 16659 | s 781(1) | encoded | `s 781(1) the order, conviction or other proceeding shall not be quashed or set aside, nor `... |  |
| 16660 | s 781(1)(a) | encoded | `s 781(1) the order, conviction or other proceeding shall not be quashed or set aside, nor `... |  |
| 16661 | s 781(1)(b) | encoded | `s 781(1) the order, conviction or other proceeding shall not be quashed or set aside, nor `... |  |
| 16662 | s 781(1)(c) | encoded | `s 781(1) the order, conviction or other proceeding shall not be quashed or set aside, nor `... |  |
| 16663 | heading: Judicial notice | inert | reason 1 (not operative: a heading) |  |
| 16664 | s 781(2) | encoded | `s 781(2) the matter shall be judicially noticed` |  |
| 16665 | heading: Defect in form | inert | reason 1 (not operative: a heading) |  |
| 16666 | s 782 | encoded | `s 782 the warrant of committal shall not be held to be void by reason of the defect` |  |
| 16667 | s 782(a) | encoded | `s 782 the warrant of committal shall not be held to be void by reason of the defect` |  |
| 16668 | s 782(b) | encoded | `s 782 the warrant of committal shall not be held to be void by reason of the defect` |  |
| 16669 | heading: No action against official when conviction, etc., quashed | inert | reason 1 (not operative: a heading) |  |
| 16670 | s 783 | encoded | `s 783 the court or judge may order that no civil proceedings shall be taken against the ju`... |  |
| 16671 | heading: Appeal in mandamus, etc. | inert | reason 1 (not operative: a heading) |  |
| 16672 | s 784(1) | encoded | `s 784(1) an appeal lies to the court of appeal from the decision` |  |
| 16673 | heading: Application of Part XXI | inert | reason 1 (not operative: a heading) |  |
| 16674 | s 784(2) | encoded | `s 784(2) Part XXI applies to the appeal` |  |
| 16675 | heading: Refusal of application, and appeal | inert | reason 1 (not operative: a heading) |  |
| 16676 | s 784(3) | fork | `s 784(3) no application may again be made on the same grounds`; `s 784(3) an appeal lies to the court of appeal from the refusal`; `s 784(3) a further appeal lies to the Supreme Court of Canada` | F14 |
| 16677 | heading: Where writ granted | inert | reason 1 (not operative: a heading) |  |
| 16678 | s 784(4) | encoded | `s 784(4) an appeal lies from the granting of the writ` |  |
| 16679 | heading: Appeal from judgment on return of writ | inert | reason 1 (not operative: a heading) |  |
| 16680 | s 784(5) | encoded | `s 784(5) the appeal lies at the instance of this appellant` |  |
| 16681 | heading: Hearing of appeal | inert | reason 1 (not operative: a heading) |  |
| 16682 | s 784(6) | fork | `s 784(6) the appeal is heard at an early date as it shall be`; `s 784(6) the court's duty to hear the appeal in a habeas corpus matter at an early date` | F1 |

## Fork register (ccc28)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each.

The six site-by-site decisions that no convention covers (the maintainer, 2026-11-05) are marked as forks here, one line each, for the human reviewer to overrule.


| Id | Provision | Function | Reading taken | Other reading | Text |
|---|---|---|---|---|---|
| F1 | ss 752.01, 761(1), 784(6) | `s 752.01 the prosecutor's duty to advise the court`; `s 761(1) the duty of the Parole Board of Canada to review the person again`; `s 784(6) the appeal is heard at an early date as it shall be` | "As soon as feasible", "as soon as possible" and "at an early date" are open-textured and are not computed. The limits the text does fix are computed: 752.01's outer limit "in any event before sentence is imposed" (the regulative deadline), 761(1)'s day seven years after custody and day two years after the previous review. Whether an appeal was heard "at an early date" is an input. | A fixed number of days read into the phrase (no such number is in the text). | 752.01: "as soon as feasible after the finding of guilt and in any event before sentence is imposed"; 761(1): "as soon as possible after the expiration of seven years ... and not later than every two years after the previous review"; 784(6): "at an early date". |
| F2 | ss 752.01(a) and (b), 753(1.1) | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an application under subsection 752.1(1)`; `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` | "Convicted previously at least twice of a designated offence and was sentenced to at least two years of imprisonment for each of those previous convictions" is read as: at least two previous convictions each of which is of the kind named and each of which carried at least two years (convictions that do not qualify are not counted, and do not defeat the rule). 752.01(b) counts previous convictions of an offence against the same class of person that was a designated or serious personal injury offence. | "Each of those previous convictions" ranges over every previous conviction of a designated offence, so that a third, shorter sentence defeats the rule. | 752.01(a): "convicted previously at least twice ... for each of those previous convictions"; 753(1.1): "convicted previously at least twice of a primary designated offence ... for each of those convictions". |
| F3.1 | s 752.1(3) | `s 752.1(3) the court may extend the period within which the report must be filed` | Written `NOTHING` from the first pass when the court is not satisfied that there are reasonable grounds (name-test sweep of 2026-11-12, test 1). No earlier `JUST FALSE` existed, so no assertion was restated. When the separate "On application" gate (F16.1) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). | `JUST FALSE`: a failed "if" read as the text's own no, so that the answer reads "the court may not extend". | "the court may extend the period ... by a maximum of 30 days if the court is satisfied that there are reasonable grounds to do so". |
| F3.2 | s 753(5) | `s 753(5) the court may take this course` | `NOTHING` when the court did find the offender to be a dangerous offender (the "if" gate fails). Written so from the first pass. | `JUST FALSE`. | "If the court does not find an offender to be a dangerous offender, (a) the court may treat the application ... (b) the court may impose sentence". |
| F3.3 | s 753.01(3) | `s 753.01(3) the court may extend the period within which the report must be filed` | `NOTHING` when the court is not satisfied that there are reasonable grounds. Written so from the first pass. When the separate "On application" gate (F16.3) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). | `JUST FALSE`. | "if the court is satisfied that there are reasonable grounds to do so". |
| F3.4 | s 753.1(1) | `s 753.1(1) the court may find the offender to be a long-term offender` | `NOTHING` when the court is not satisfied of all three of (a), (b) and (c). Written so from the first pass. When the separate "on application" gate (F16.5) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). | `JUST FALSE`. | "find an offender to be a long-term offender if it is satisfied that (a) ...; (b) ...; and (c) ...". |
| F3.5 | s 757 | `s 757 evidence of character and repute may be admitted` | `NOTHING` when the court does not think fit. Written so from the first pass. | `JUST FALSE`. | "if the court thinks fit, evidence of character and repute may be admitted". |
| F3.6 | s 758(1)(a) | `s 758(1)(a) the court may order the person having the custody of the accused to bring the offender before the court` | `NOTHING` when the offender is not confined in a prison at the time the application is to be heard. Written so from the first pass. | `JUST FALSE`. | "if at the time the application is to be heard (a) he is confined in a prison, the court may order, in writing, the person having the custody of the accused to bring him before the court". |
| F3.7 | s 767.1(1) | `s 767.1(1) the court, justice or provincial court judge may substitute another person for the surety` | `NOTHING` when the surety has neither given the person into custody under s 767 nor applied to be relieved, and when the other person is not suitable. Written so from the first pass. | `JUST FALSE`. | "If a surety ... has given the person into the custody of a court under section 767, or a surety applies to be relieved of their obligation ... may ... substitute any other suitable person". |
| F3.8 | s 771(2) | `s 771(2) the judge may take this course` | `NOTHING` when subsection (1) has not been complied with. Written so from the first pass. The separate "after giving the parties an opportunity to be heard" gate answers `JUST FALSE` and is listed as F16.11; when both gates fail the answer is `JUST FALSE`, because the "after" gate is tested first (asserted), although the text puts the "if" first. | `JUST FALSE`. | "If subsection (1) has been complied with, the judge may, after giving the parties an opportunity to be heard ... grant or refuse the application". |
| F4 | ss 753(2), 761(1), 761(2) | `s 753(2)(a) ...`, `s 753(2)(b) ...`; `s 761(1) the day on which seven years from the day the person was taken into custody have expired` | "Six months after", "seven years from" and "two years after" are counted on the calendar with `add months` and `add years` of daydate: the day of the month is kept, and clamped to the last day of a shorter month. | A count in days (180 days, 365 days a year), or the day before the anniversary. | "not later than six months after the imposition of sentence"; "after the expiration of seven years from the day on which that person was taken into custody". |
| F5 | s 753.2(2) | `s 753.2(2) the sentence is to be served concurrently with the long-term supervision` | "Other than a sentence that requires imprisonment" limits the rule by its own wording; for a sentence that requires imprisonment the answer is `NOTHING` (silent), not `JUST FALSE`. | `JUST FALSE`: the exception read as the text saying that such a sentence is not served concurrently. | "A sentence imposed on an offender referred to in subsection (1), other than a sentence that requires imprisonment, is to be served concurrently with the long-term supervision." |
| F6 | s 753.3(1) | `s 753.3(1) the offender is guilty of an offence` | A case outside the elements (not subject to long-term supervision, no failure to comply, or a reasonable excuse) is `NOTHING`: the offence is limited by its own wording ("without reasonable excuse") and by the named class. | `JUST FALSE`: the offence is closed by its elements, so the offender is not guilty. | "An offender who, without reasonable excuse, fails or refuses to comply with long-term supervision is guilty of ...". |
| F7 | s 753.4(1) | `s 753.4(1) the long-term supervision is interrupted` | Once the court orders termination, and once all the sentences are served, the supervision is not interrupted: `JUST FALSE` (an "unless" and an "until" the text itself states). | `NOTHING`: after termination or completion the subsection is silent about what the supervision then is. | "the long-term supervision is interrupted until the offender has finished serving all the sentences, unless the court orders its termination". |
| F8 | s 754(1) | `s 754(1) the court may not hear the application` | The bar is `JUST FALSE` for an application for remand for assessment ("With the exception of") and when (a), (b) and (c) are all met ("unless"); `JUST TRUE` when one is unmet. | `NOTHING` for the exception: the subsection says nothing about such an application. | "With the exception of an application for remand for assessment, the court may not hear an application made under this Part unless (a) ...; (b) ...; and (c) ...". |
| F9 | s 755(2) | `s 755(2) the periods of long-term supervision do not total more than 10 years` | A month is read as 28 to 31 days: `JUST TRUE` when 28 times the whole months plus the days is at most 3,360, `JUST FALSE` when 31 times the whole months plus the days is more than 3,720, otherwise `NOTHING` (the calendar decides, and the subsection does not fix it). | A month of 30 days (3,600 days in all) giving a single answer in every case. | "must not total more than 10 years". |
| F10 | ss 763(2), 764(4) | `s 763(2) the document sets out a summary of section 763 as it must`; `s 764(4) the document sets out a summary of subsections (1) to (3) as it must` | A bare "must" with no actor: a document that lacks the summary does not comply, `JUST FALSE`. | `NOTHING`: a bare "must" unmet is silent about what follows. | "A summary of section 763 must be set out in any undertaking, release order or recognizance." |
| F11 | ss 766(2), 770(2), 773(2) | `s 766(2) the order is given to the surety as it must be`; `s 770(2) the document is sent to the clerk of the court as it must be`; `s 773(2) the number of clear days of notice` | The text names no actor for these passive duties ("must be given to the surety", "must be sent to the clerk", "shall be given to the sureties"), so no regulative rule is written; the functions ask only whether it was done, and for 773(2) how many clear days of notice there were (the day difference less one). | An actor supplied from context (the court that issued the order; the court that endorsed the document; the Attorney General). | 766(2): "must be given to the surety"; 770(2): "must be sent to the clerk of the court"; 773(2): "Seven clear days notice ... shall be given to the sureties". |
| F12 | s 772(2) | `s 772(2) the tariff that fixes the costs` | "In the Province of Quebec ... and in any other province": a territory is not named, so the tariff for a territory is `NOTHING`. | A territory read as a province for this purpose. | "fixed, in the Province of Quebec, by any tariff applicable in the Superior Court ..., and in any other province, by any tariff applicable in the superior court of the province". |
| F13 | s 778 | `s 778 section 777 is deemed by this section to apply` | The section deems section 777 to apply where (a), (b) or (c) holds, `JUST TRUE`; where none holds the answer is `JUST FALSE` for this section only ("this section does not deem"), and section 777 may still apply of its own force. | `NOTHING`: the section is silent about other cases. | "Without restricting the generality of section 777, that section shall be deemed to apply where (a) ...; (b) ...; or (c) ...". |
| F14 | s 784(3) | `s 784(3) no application may again be made on the same grounds` | On the bar, an "unless" once met: the bar then does not apply, `JUST FALSE` for the bar. An application on other grounds is `NOTHING`. | `NOTHING` for the met "unless": the subsection is then silent. | "no application may again be made on the same grounds ... unless fresh evidence is adduced". |
| F15 | s 777(2)(a) | `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | Where the person has served a term at least equal to the lawful maximum, subparagraph (ii) states no correction and the answer is `NOTHING`; subparagraph (iii) sends a fine and imprisonment to (i) or (ii). | `JUST FALSE` for any corrected term when the maximum has been served. | "(ii) where the punishment is imprisonment, and the person has not served a term ... equal to or greater than the term ... that might lawfully have been imposed, by imposing a term of imprisonment that does not exceed the maximum". |

### Case-by-case sites of 2026-11-05 (rows F18)

The maintainer's ruling of 2026-11-05 (quoted below) leaves six kinds of site to be decided where they occur, each with one fork line for the reviewer: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger.

Bare "must" is F10; "listed in Schedule N" and a missing event in the state ledger do not occur in this range (s 762(1) takes the Schedule's columns as inputs, and the part has no ledger).

The rows below are the other sites, generated from the `FALSE-kind` comments of the modules, one row for each function and kind: the answer taken is `JUST FALSE` (the gate unmet, or the exception or the "unless" met), and the other reading is `NOTHING`.

They are listed for the reviewer to overrule; their coverage rows stay `encoded` (assumed, not ruled).


| Id | Provision | Function | Kind of site | Words in the text | Answer taken | Other reading |
|---|---|---|---|---|---|---|
| F18.1 | s 752 | `s 752 serious personal injury offence (a)` | "(other than X)" | "other than high treason, treason, first degree or second degree murder" | `JUST FALSE`: the exclusion sits inside a definition that "means" and so closes the list, so a case within the exclusion is outside the definition; contrast s 753.2(2) (F5), whose "other than" limits a rule and not a closed definition, and so answers `NOTHING` | `NOTHING` |
| F18.2 | s 752.01 | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an application under subsection 752.1(1)` | a duty whose "if" or "where" is unmet | "if the prosecutor is of the opinion that an offence for which an offender is found guilty is a serious personal injury o..." | `JUST FALSE` | `NOTHING` |
| F18.3 | s 752.1(1) | `s 752.1(1) the court shall remand the offender for an assessment` | a duty whose "if" or "where" is unmet | "On application by the prosecutor" | `JUST FALSE` | `NOTHING` |
| F18.4 | s 753(1) | `s 753(1) the court shall find the offender to be a dangerous offender` | a duty whose "if" or "where" is unmet | "On application made under this Part after an assessment report is filed under subsection 752.1(2)" | `JUST FALSE` | `NOTHING` |
| F18.5 | s 753(1.1) | `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` | an "unless" or "except" once it is met | "unless the contrary is proved on a balance of probabilities" | `JUST FALSE` | `NOTHING` |
| F18.6 | s 753(2) | `s 753(2) the application under subsection (1) is made in time` | an "unless" or "except" once it is met | "must be made before sentence is imposed on the offender unless" | `JUST FALSE` | `NOTHING` |
| F18.7 | s 753(4.1) | `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | an "unless" or "except" once it is met | "unless it is satisfied by the evidence adduced during the hearing of the application" | `JUST FALSE` | `NOTHING` |
| F18.8 | s 753.01(1) | `s 753.01(1) the court shall remand the offender for an assessment` | a duty whose "if" or "where" is unmet | "If an offender who is found to be a dangerous offender is later convicted of" | `JUST FALSE` | `NOTHING` |
| F18.9 | s 753.01(5) | `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | a duty whose "if" or "where" is unmet | "If the application is for a sentence of detention in a penitentiary for an indeterminate period" | `JUST FALSE` | `NOTHING` |
| F18.10 | s 753.01(5) | `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | an "unless" or "except" once it is met | "unless it is satisfied by the evidence adduced during the hearing of the application" | `JUST FALSE` | `NOTHING` |
| F18.11 | s 753.01(6) | `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision` | a duty whose "if" or "where" is unmet | "If the application is for a new period of long-term supervision" | `JUST FALSE` | `NOTHING` |
| F18.12 | s 753.01(6) | `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision` | an "unless" or "except" once it is met | "unless it is satisfied by the evidence adduced during the hearing of the application" | `JUST FALSE` | `NOTHING` |
| F18.13 | s 753.1(6) | `s 753.1(6) the court shall impose sentence for the offence` | a duty whose "if" or "where" is unmet | "If the court does not find an offender to be a long-term offender" | `JUST FALSE` | `NOTHING` |
| F18.14 | s 753.2(1) | `s 753.2(1) the offender shall be supervised in the community` | a duty whose "if" or "where" is unmet | "when the offender has finished serving" | `JUST FALSE` | `NOTHING` |
| F18.15 | s 753.4(1) | `s 753.4(1) the long-term supervision is interrupted` | an "unless" or "except" once it is met | "unless the court orders its termination" | `JUST FALSE` | `NOTHING` |
| F18.16 | s 754(1) | `s 754(1) the court may not hear the application` | "(other than X)" | "With the exception of an application for remand for assessment" | `JUST FALSE` for an application for remand for assessment (F8) | `NOTHING` |
| F18.17 | s 754(1) | `s 754(1) the court may not hear the application` | an "unless" or "except" once it is met | "the court may not hear an application made under this Part unless" | `JUST FALSE` | `NOTHING` |
| F18.18 | s 758(1)(b) | `s 758(1)(b) the court shall issue a summons or a warrant to compel the accused to attend before the court` | a duty whose "if" or "where" is unmet | "if at the time the application is to be heard ... (b) he is not confined in a prison" | `JUST FALSE` | `NOTHING` |
| F18.19 | s 760 | `s 760 the court shall order that the reports, testimony, observations and transcript be forwarded to the Correctional Service of Canada` | a duty whose "if" or "where" is unmet | "Where a court finds an offender to be a dangerous offender or a long-term offender" | `JUST FALSE` | `NOTHING` |
| F18.20 | s 761(1) | `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances of the person` | a duty whose "if" or "where" is unmet | "where a person is in custody under a sentence of detention in a penitentiary for an indeterminate period" | `JUST FALSE` | `NOTHING` |
| F18.21 | s 761(2) | `s 761(2) the Parole Board of Canada shall review the condition, history and circumstances of the person at least once in every year` | a duty whose "if" or "where" is unmet | "Where a person is in custody under a sentence of detention in a penitentiary for an indeterminate period" | `JUST FALSE` | `NOTHING` |
| F18.22 | s 766(2) | `s 766(2) the keeper shall receive and imprison the person` | a duty whose "if" or "where" is unmet | "until the person is discharged according to law" | `JUST FALSE` | `NOTHING` |
| F18.23 | s 766(3) | `s 766(3) the court, provincial court judge or justice shall order an entry of the committal to be endorsed on the document` | a duty whose "if" or "where" is unmet | "If a court, provincial court judge or justice issues an order under subsection (1) and receives from the sheriff a certi..." | `JUST FALSE` | `NOTHING` |
| F18.24 | s 767 | `s 767 the court shall commit the person to prison` | a duty whose "if" or "where" is unmet | "until the person is discharged according to law" | `JUST FALSE` | `NOTHING` |
| F18.25 | s 769 | `s 769 the person shall forthwith be taken before a justice or judge` | a duty whose "if" or "where" is unmet | "Where a surety for a person has rendered him into custody and that person has been committed to prison" | `JUST FALSE` | `NOTHING` |
| F18.26 | s 770(1) | `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorsed a certificate` | a duty whose "if" or "where" is unmet | "If, in proceedings to which this Act applies, a person who is subject to an undertaking, release order or recognizance d..." | `JUST FALSE` | `NOTHING` |
| F18.27 | s 770(4) | `s 770(4) the money is sent to the clerk of the court with the defaulted document as it must be` | a duty whose "if" or "where" is unmet | "If, in proceedings to which this section applies, the principal or surety has deposited money as security for the perfor..." | `JUST FALSE` | `NOTHING` |
| F18.28 | s 771(1)(a) | `s 771(1)(a) a judge of the court shall fix a time and place for the hearing of an application for forfeiture` | a duty whose "if" or "where" is unmet | "If an undertaking, release order or recognizance has been endorsed with a certificate and has been received by the clerk..." | `JUST FALSE` | `NOTHING` |
| F18.29 | s 771(3.1) | `s 771(3.1) the clerk shall issue a writ of fieri facias and deliver it to the sheriff of this territorial division` | a duty whose "if" or "where" is unmet | "if one is filed, the clerk shall issue a writ of fieri facias" | `JUST FALSE` | `NOTHING` |
| F18.30 | s 771(4) | `s 771(4) the deposit is transferred to the person entitled by law to receive it as it must be` | a duty whose "if" or "where" is unmet | "If a deposit has been made by a person against whom an order for forfeiture has been made" | `JUST FALSE` | `NOTHING` |
| F18.31 | s 777(2) | `s 777(2) the court or judge shall correct the sentence or remit the matter` | a duty whose "if" or "where" is unmet | "Where, in proceedings to which subsection (1) applies, the court or judge is satisfied that a person was properly convic..." | `JUST FALSE` | `NOTHING` |
| F18.32 | s 777(3) | `s 777(3) the document shall be amended to conform to the adjudication as varied` | a duty whose "if" or "where" is unmet | "Where an adjudication is varied pursuant to subsection (1) or (2)" | `JUST FALSE` | `NOTHING` |
| F18.33 | s 779(1) | `s 779(1) the motion to quash may not be heard under the general order` | an "unless" or "except" once it is met | "shall be heard unless the defendant has entered into a recognizance" | `JUST FALSE` | `NOTHING` |
| F18.34 | s 784(2) | `s 784(2) Part XXI applies to the appeal` | an "unless" or "except" once it is met | "Except as provided in this section" | `JUST FALSE` | `NOTHING` |
| F18.35 | s 784(3) | `s 784(3) no application may again be made on the same grounds` | an "unless" or "except" once it is met | "unless fresh evidence is adduced" | `JUST FALSE` | `NOTHING` |

### Rulings carried word for word (from the brief)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

### Name-test sweep rows: listed, not decided (groups F16 and F17)

ASSUMED, NOT RULED: that the equivalents marked "assumed" below ("on ...", "after ...", "until", "in the case of", "at the hearing", "during ... and before") go with the "where", "when" and "upon" group.

For each row the answer the part gives is `JUST FALSE` when the gate fails; the other reading is `NOTHING`.

Ruling (b) of the "Periods, where and scope limits" paragraph of the brief, and ruling (c) of the 2026-11-05 delegated ruling, say `JUST FALSE`; the Guide's line on grants ("limits a grant or prohibition in its own wording and the case falls outside the limit") points the other way.

That is a question for the maintainer or a lawyer, not one to settle by a sweep, so these rows are listed and the answer is left as the part already gives it.


| Id | Provision | Function | Gate words | Kind of gate | Answer the part gives | Other reading |
|---|---|---|---|---|---|---|
| F16.1 | s 752.1(3) | `s 752.1(3) the court may extend the period within which the report must be filed` | "On application by the prosecutor" | equivalent ("on ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.2 | s 753(3) | `s 753(3) an application under subsection 752.1(1) may be made after the imposition of sentence or after the offender begins to serve the sentence` | "in a case to which paragraphs (2)(a) and (b) apply" | equivalent ("in the case of"), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.3 | s 753.01(3) | `s 753.01(3) the court may extend the period within which the report must be filed` | "On application by the prosecutor" | equivalent ("on ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.4 | s 753.01(4) | `s 753.01(4) the prosecutor may apply for this sentence or order` | "After the report is filed" | equivalent ("after ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.5 | s 753.1(1) | `s 753.1(1) the court may find the offender to be a long-term offender` | "on application made under this Part following the filing of an assessment report" | equivalent ("on ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.6 | s 753.2(3) | `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision` | "on approval of that Board, the offender's parole supervisor" | equivalent ("on ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.7 | s 758(2)(a) | `s 758(2)(a) the court may cause the offender to be removed and kept out of court` | "where he misconducts himself by interrupting the proceedings so that to continue the proceedings in his presence would not be feasible" | "where" | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.8 | s 764(2) | `s 764(2) the court, provincial court judge or justice may take this step` | "until the accused is discharged or sentenced, as the case may be" | equivalent ("until"), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.9 | s 766(2) | `s 766(2) this person may arrest the person named in the order and deliver them to the keeper of the prison` | "on receipt of it" | equivalent ("on ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.10 | s 767 | `s 767 the surety may bring the person before the court` | "at any time during the sittings of that court and before the person's trial" | equivalent ("when", "during", "before"), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.11 | s 771(2) | `s 771(2) the judge may take this course` | "after giving the parties an opportunity to be heard" | equivalent ("after ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.12 | s 773(1) | `s 773(1) a judge of the court may fix a time and place for the sureties to show cause` | "Where a writ of fieri facias has been issued ... and it appears ..." and "upon the application of the Attorney General" | "where" and "upon" | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.13 | s 773(3) | `s 773(3) the judge may make this order in their discretion` | "at the hearing held pursuant to subsection (1)" | equivalent ("when"), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.14 | s 775 | `s 775 the judge or court may take this course without determining the question` | "Where proceedings to which this Part applies have been instituted ..." | "where" | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.15 | s 783 | `s 783 the court or judge may order that no civil proceedings shall be taken against the justice, provincial court judge or officer` | "Where an application is made to quash ..." and "in quashing the conviction, order or other proceeding" | "where" and equivalent ("in ..."), assumed | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.16 | s 773(4) | `s 773(4) the warrant authorizes the sheriff to confine the person in this prison` | "until satisfaction is made or until the period of imprisonment fixed by the judge has expired" | equivalent ("until"), assumed; the name says "authorizes", counted with the word "authorised" of the list because it names a grant | `JUST FALSE` when the gate fails | `NOTHING` |
| F16.17 | s 780 | `s 780 the order refusing the application is sufficient authority for the clerk of the court to return the conviction, order or proceeding` | "Where a motion to quash a conviction, order or other proceeding is refused" | "where"; the name says "authority", counted with the word "authorised" of the list because it names a grant | `JUST FALSE` when the gate fails | `NOTHING` |

| Id | Provision | Function | Gate | Answer the part gives | Other reading |
|---|---|---|---|---|---|
| F17.1 | s 772(2) | `s 772(2) the Crown is entitled to the costs of execution and of proceedings incidental thereto` | "Where this section applies": the answer is `JUST FALSE` when no writ of fieri facias is issued pursuant to section 771. | `JUST FALSE` | `NOTHING`: an entitlement is a claim, not a power, and the Guide does not settle it |

### Reading a result: FALSE and NOTHING (ccc28)

In this part a `JUST TRUE` answer is yes on the facts given, and the facts are the ones a person in the seat can state.

A `JUST FALSE` answer is the text saying no in its own words: a definition that "means" (the offence is not within the closed list of `s 752`), an "if", "unless", "until", "where" or "on" condition the facts do not meet, a flat negative ("may not", "shall not", "no ... may be issued"), or a period the text fixes.

A `NOTHING` answer is "not covered": the text is silent, or its grant or prohibition is limited by its own wording and the case falls outside the limit (a named class of person, a named court, a named ground, a "without reasonable excuse"), or a list is not closed with "only", or the answer depends on another part's answer that is itself not covered.

A question that asks whether a provision bars something (`s 754(1)`, `s 755(1)`, `s 776`, `s 784(3)`) is titled as the bar: `JUST TRUE` means the bar applies, and `JUST FALSE` or `NOTHING` is not a grant.

A function named for a grant or a power ("may") answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (the sweep of 2026-11-12; F3.1 to F3.8); where the gate is "where", "when", "upon" or an equivalent, the part keeps `JUST FALSE` and lists it (F16.1 to F16.17).

Lint of the layer-1 modules (`work/lint.py`): every branch that answers `JUST FALSE` carries a `FALSE-kind` comment whose quoted words are found in the text, and every branch that answers `NOTHING` carries a `NOTHING-kind` comment giving one of the six reasons: 158 `JUST FALSE` branches, 126 `NOTHING` branches, 0 problems.

## Jural relations (ccc28)

One row per provision that creates a relation, with the party holding the right (claim), privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, and the L4 rule that encodes it.

A provision that creates no such relation (a definition, a counting rule, a rule of evidence, a deeming rule) is listed once as `none`.

Where the text names no actor for a passive duty ("must be given", "must be sent", "shall be given") the bearer is shown as unnamed (fork F11).


| Provision | Holder (right, privilege, power, immunity) | Bearer (duty, no-right, liability, disability) | Kind | L4 rule |
|---|---|---|---|---|
| s 752 (definitions: court, designated offence, long-term supervision, primary designated offence, serious personal injury offence) | none | none | definitions | `s 752 court`, `s 752 the offence is a designated offence`, `s 752 the offence is a primary designated offence`, `s 752 long-term supervision`, `s 752 the offence is a serious personal injury offence` |
| s 752.01 | the court (claim to be advised) | the prosecutor (duty) | claim - duty | `s 752.01 the prosecutor's duty to advise the court` |
| s 752.1(1) | the prosecutor (power to apply; claim that the court remand) | the court (duty to remand); the offender (liability to be remanded) | power - liability; claim - duty | `s 752.1(1) the court shall remand the offender for an assessment`, `s 752.1(1) the court's duty to remand the offender` |
| s 752.1(2) | the court, the prosecutor and counsel for the offender (claim to the report and copies) | the person to whom the offender is remanded (duty, 30 days) | claim - duty | `s 752.1(2) the duty of the person to whom the offender is remanded` |
| s 752.1(3) | the court (power to extend by up to 30 days) | the person to whom the offender is remanded (liability) | power - liability | `s 752.1(3) the court may extend the period within which the report must be filed` |
| s 753(1) | the prosecutor (claim that the court find) | the court (duty); the offender (liability to the finding) | claim - duty; power - liability | `s 753(1) the court shall find the offender to be a dangerous offender` |
| s 753(1.1) | none (a rebuttable presumption that allocates the burden of proof) | none | none | `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` |
| s 753(2) | the offender (immunity from a late application) | the prosecutor (disability to apply late unless (a) and (b)) | immunity - disability | `s 753(2) the application under subsection (1) is made in time` |
| s 753(3) | the prosecutor (power to apply for remand after sentence) | the offender (liability) | power - liability | `s 753(3) an application under subsection 752.1(1) may be made after the imposition of sentence ...` |
| s 753(4) | the prosecutor (claim that the court choose one disposition) | the court (duty); the offender (liability) | claim - duty | `s 753(4) the disposition is within paragraph (a), (b) or (c)` |
| s 753(4.1) | the prosecutor (claim to an indeterminate sentence) | the court (duty); the offender (liability) | claim - duty | `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` |
| s 753(4.2) | none (the new sentence replaces the earlier one: a rule of effect) | none | none | `s 753(4.2) the sentence imposed replaces the sentence that was imposed ...` |
| s 753(5) | the court (power) | the offender (liability) | power - liability | `s 753(5) the court may take this course` |
| s 753(6) | repealed | repealed | none | none (repealed) |
| s 753.01(1) | the prosecutor (claim that the court remand a dangerous offender later convicted) | the court (duty); the offender (liability) | claim - duty | `s 753.01(1) the court shall remand the offender for an assessment` |
| s 753.01(2) | the court, the prosecutor and counsel for the offender (claim to the report) | the person to whom the offender is remanded (duty) | claim - duty | `s 753.01(2) the duty of the person to whom the offender is remanded` |
| s 753.01(3) | the court (power to extend) | the person to whom the offender is remanded (liability) | power - liability | `s 753.01(3) the court may extend the period within which the report must be filed` |
| s 753.01(4) | the prosecutor (power to apply) | the offender (liability) | power - liability | `s 753.01(4) the prosecutor may apply for this sentence or order` |
| s 753.01(5) | the prosecutor (claim to an indeterminate sentence) | the court (duty); the offender (liability) | claim - duty | `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` |
| s 753.01(6) | the prosecutor (claim to a new period of long-term supervision) | the court (duty); the offender (liability) | claim - duty | `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision` |
| s 753.02 | none (evidence given is deemed given at the later hearing) | none | none | `s 753.02 the evidence is deemed also to have been given during the hearing` |
| s 753.1(1) | the prosecutor (power to apply); the court (power to find) | the offender (liability) | power - liability | `s 753.1(1) the court may find the offender to be a long-term offender` |
| s 753.1(2) | the prosecutor (claim that the court be satisfied on these facts) | the court (duty) | claim - duty | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender will reoffend` |
| s 753.1(3) | the prosecutor (claim to the sentence and order) | the court (duty); the offender (liability) | claim - duty | `s 753.1(3) the sentence and order are within paragraphs (a) and (b)` |
| s 753.1(3.1) | the offender (immunity from a sentence under (3)(a) in the case described) | the court (disability) | immunity - disability | `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)` |
| s 753.1(4) and (5) | repealed | repealed | none | none (repealed) |
| s 753.1(6) | the prosecutor (claim to a sentence for the offence) | the court (duty) | claim - duty | `s 753.1(6) the court shall impose sentence for the offence` |
| s 753.2(1) | the public (claim to supervision in the community); the offender (liability to supervision) | no actor is named (passive "shall be supervised") | claim - duty (actor unnamed); liability | `s 753.2(1) the offender shall be supervised in the community` |
| s 753.2(2) | none (a rule on concurrency of sentences) | none | none | `s 753.2(2) the sentence is to be served concurrently with the long-term supervision` |
| s 753.2(3) | the offender, a member of the Parole Board of Canada, or with the Board's approval the offender's parole supervisor (power to apply) | the superior court of criminal jurisdiction (liability to be applied to) | power - liability | `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision` |
| s 753.2(4) | the Attorney General (claim to notice) | the applicant (duty to give notice at the time of the application) | claim - duty | `s 753.2(4) the duty of the applicant to give notice to the Attorney General` |
| s 753.3(1) | the Crown (claim that the offender comply) | the offender (duty; liability to conviction) | claim - duty | `s 753.3(1) the offender is guilty of an offence` |
| s 753.3(2) | the Crown (power to try and punish in these places) | the accused (liability); the Attorney General's consent is a condition outside the province | power - liability | `s 753.3(2) the accused may be tried and punished in this place` |
| s 753.4(1) | none (a rule of effect: the supervision is interrupted) | none | none | `s 753.4(1) the long-term supervision is interrupted` |
| s 753.4(2) | the court (power to reduce the supervision) | the offender (liability) | power - liability | `s 753.4(2) the court may order a reduction in the length of the period of long-term supervision` |
| s 754(1) | the offender (immunity from an application not made on consent and notice) | the court and the prosecutor (disability) | immunity - disability | `s 754(1) the court may not hear the application` |
| s 754(2) | none (mode of hearing: without a jury) | none | none | `s 754(2) the application is heard and determined by the court without a jury` |
| s 754(3) | none (a rule of proof) | none | none | `s 754(3) no proof of the allegations is required` |
| s 754(4) | none (a rule of proof) | none | none | `s 754(4) the document is proof of the nomination or consent` |
| s 755(1) | the offender sentenced to life imprisonment (immunity from long-term supervision) | the court (disability) | immunity - disability | `s 755(1) the court shall not order that the offender be subject to long-term supervision` |
| s 755(2) | the offender (immunity from supervision totalling more than 10 years) | the court (disability) | immunity - disability | `s 755(2) the periods of long-term supervision do not total more than 10 years` |
| s 756 | repealed | repealed | none | none (repealed) |
| s 757 | the court (power to admit evidence of character and repute); the offender's own right to tender evidence is saved (privilege) | the parties (liability) | power - liability; privilege - no-right | `s 757 evidence of character and repute may be admitted` |
| s 758(1) | the court (claim to the offender's presence; power to order the person having custody to bring the offender) | the offender (duty); the person having the custody of the accused (liability) | claim - duty; power - liability | `s 758(1) the offender shall be present at the hearing of the application`, `s 758(1)(a) the court's power to order the person having the custody to bring the offender` |
| s 758(2) | the court (power to remove the offender, or permit the offender to be out of court) | the offender (liability) | power - liability | `s 758(2)(a) the court may cause the offender to be removed and kept out of court`, `s 758(2)(b) the court may permit the offender to be out of court` |
| s 759(1) | the offender (power to appeal) | the Attorney General and the court of appeal (liability) | power - liability | `s 759(1) the offender may appeal to the court of appeal` |
| s 759(1.1) | repealed | repealed | none | none (repealed) |
| s 759(2) | the Attorney General (power to appeal) | the offender (liability) | power - liability | `s 759(2) the Attorney General may appeal to the court of appeal` |
| s 759(3) | the court of appeal (power) | the parties (liability) | power - liability | `s 759(3) the court of appeal may make this disposition` |
| s 759(3.1) and (3.2) | repealed | repealed | none | none (repealed) |
| s 759(4) | none (a rule of effect: same force as a trial-court decision) | none | none | `s 759(4) the decision has the same force and effect as a decision of the trial court` |
| s 759(4.1) to (5) | repealed | repealed | none | none (repealed) |
| s 759(6) | none (a deeming rule for the day a sentence commenced) | none | none | `s 759(6) the day the sentence is deemed to have commenced` |
| s 759(7) | none (Part XXI procedure applies) | none | none | `s 759(7) the provisions of Part XXI with respect to procedure on appeals apply to the appeal` |
| s 760 | the Correctional Service of Canada (claim to the reports, for information) | the court (duty to order them forwarded) | claim - duty | `s 760 the court shall order that the reports, testimony, observations ...` |
| s 761(1) | the person in custody (claim to a review) | the Parole Board of Canada (duty) | claim - duty | `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances of the person`, `s 761(1) the duty of the Parole Board of Canada to review the person again` |
| s 761(2) | the person in custody under a sentence imposed before 15 October 1977 (claim to an annual review) | the Parole Board of Canada (duty) | claim - duty | `s 761(2) the Parole Board of Canada shall review ... at least once in every year` |
| s 762(1) | the Crown (power to apply for forfeiture to the designated court) | the principal and sureties (liability) | power - liability | `s 762(1) the application for forfeiture is made to the court the schedule designates` |
| s 762(2) | none (definitions: clerk of the court, schedule) | none | definitions | `s 762(2) the person is the clerk of the court`, `s 762(2) the document is the schedule` |
| s 763(1) | the court, provincial court judge or justice (claim that the person appear) | the person and their sureties (duty continues) | claim - duty | `s 763(1) the person and their sureties continue to be bound` |
| s 763(2) | none stated (a bare "must": F10) | no actor named | none | `s 763(2) the document sets out a summary of section 763 as it must` |
| s 764(1) | the Crown (claim to appearance) | the accused and their sureties (continuing duty) | claim - duty | `s 764(1) the undertaking or release order continues to bind the accused and their sureties for their appearance` |
| s 764(2) | the court, provincial court judge or justice (power to commit or require new sureties) | the accused (liability) | power - liability | `s 764(2) the court, provincial court judge or justice may take this step` |
| s 764(3) | the sureties (immunity: discharged on committal) | the Crown (disability) | immunity - disability | `s 764(3) the sureties of the accused are discharged` |
| s 764(4) | none stated (a bare "must": F10) | no actor named | none | `s 764(4) the document sets out a summary of subsections (1) to (3) as it must` |
| s 765 | the Crown (claim to appearance despite another arrest) | the accused and their sureties (continuing duty) | claim - duty | `s 765 the undertaking or release order continues to bind the accused and their sureties despite the arrest on another charge` |
| s 766(1) | the surety (power to apply to be relieved) | the court, provincial court judge or justice (liability to the application) | power - liability | `s 766(1) the surety may apply to be relieved of their obligation` |
| s 766(2) | the surety or a peace officer (power to arrest and deliver); the person named in the order (liability) | the keeper of the prison (duty to receive and imprison); no actor named for giving the order (F11) | power - liability; claim - duty | `s 766(2) this person may arrest the person named in the order and deliver them to the keeper of the prison`, `s 766(2) the order is given to the surety as it must be` |
| s 766(3) | the surety (claim to the endorsement) | the court, provincial court judge or justice (duty to order the entry of the committal endorsed) | claim - duty | `s 766(3) the court's duty to order an entry of the committal to be endorsed` |
| s 766(4) | the surety (immunity: the release order or recognizance is cancelled and the sureties discharged) | the Crown (disability) | immunity - disability | `s 766(4) the release order or recognizance is cancelled and the sureties are discharged` |
| s 767 | the surety (power to bring the person before the court and be discharged by giving them into custody) | the person (liability); the court (duty to commit) | power - liability; claim - duty | `s 767 the surety may bring the person before the court` |
| s 767.1(1) | the court, justice or provincial court judge (power to substitute another suitable person) | the surety (liability) | power - liability | `s 767.1(1) the court, justice or provincial court judge may substitute another person for the surety` |
| s 767.1(2) | the original surety (immunity: discharged when the substitute signs) | the Crown (disability) | immunity - disability | `s 767.1(2) the original surety is discharged` |
| s 768 | the surety (privilege: the right of taking and giving into custody is saved) | the person for whom the surety stands (no-right) | privilege - no-right | `s 768 this Part limits the surety's right of taking and giving the person into custody` |
| s 769 | the person committed (claim to be taken forthwith before a justice or judge) | no actor named (passive "shall forthwith be taken") | claim - duty (actor unnamed) | `s 769 the interim release provisions of Parts XVI, XXI and XXVII apply in respect of the person`, `s 769 the person shall forthwith be taken before a justice or judge` |
| s 770(1) | the Crown (claim to a certificate of default) | the court, provincial court judge or justice (duty to endorse) | claim - duty | `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorsed a certificate` |
| s 770(2) | the clerk of the court (claim to receive the document) | no actor named (passive "must be sent": F11) | claim - duty (actor unnamed) | `s 770(2) the document is sent to the clerk of the court as it must be` |
| s 770(3) | none (a rule of evidence) | none | none | `s 770(3) the certificate is evidence of the default to which it relates` |
| s 770(4) | the clerk of the court (claim to the deposited money) | no actor named (passive "must be sent") | claim - duty (actor unnamed) | `s 770(4) the money is sent to the clerk of the court with the defaulted document as it must be` |
| s 771(1) | the Attorney General (claim to a fixed hearing); each principal and surety (claim to notice) | a judge of the court (duty to fix time and place); the clerk of the court (duty to send notice, 10 days before) | claim - duty | `s 771(1)(a) a judge of the court shall fix a time and place for the hearing of an application for forfeiture`, `s 771(1)(b) the clerk of the court's duty to send the notice` |
| s 771(2) | the judge (power to grant or refuse and order on forfeiture) | the principal and sureties (liability) | power - liability | `s 771(2) the judge may take this course` |
| s 771(3) | the Crown (claim to payment of the amount ordered) | the principal and their sureties (liability as judgment debtors) | claim - duty | `s 771(3) the principal and their sureties become judgment debtors of the Crown` |
| s 771(3.1) | the Crown (power to file the order with the clerk of the superior court) | the principal and sureties (liability to enforcement as a judgment) | power - liability | `s 771(3.1) the order may be filed with the clerk of the superior court`, `s 771(3.1) the clerk's duty to issue and deliver the writ` |
| s 771(4) | the person who made a deposit (immunity from a writ of fieri facias); the person entitled by law (claim to the deposit) | the Crown (disability); the person who has custody of the deposit (duty to transfer) | immunity - disability; claim - duty | `s 771(4) no writ of fieri facias may be issued`, `s 771(4) the deposit is transferred to the person entitled by law to receive it as it must be` |
| s 772(1) | the Crown (claim to execution of the writ) | the sheriff (duty to execute and deal with the proceeds) | claim - duty | `s 772(1) the sheriff executes the writ and deals with the proceeds as the subsection requires`, `s 772(1) the sheriff's duty to execute the writ` |
| s 772(2) | the Crown (claim to the costs, as the judge may direct) | the principal and sureties (liability) | claim - duty | `s 772(2) the Crown is entitled to the costs of execution and of proceedings incidental thereto` |
| s 773(1) | the Attorney General or counsel (power to apply); a judge of the court (power to fix a time and place) | the sureties (liability) | power - liability | `s 773(1) a judge of the court may fix a time and place for the sureties to show cause` |
| s 773(2) | the sureties (claim to seven clear days' notice) | no actor named (passive "shall be given": F11) | claim - duty (actor unnamed) | `s 773(2) the number of clear days of notice` |
| s 773(3) | the judge (duty to inquire; power to order discharge or imprisonment) | the surety (liability) | power - liability | `s 773(3) the judge may make this order in their discretion`, `s 773(3) the judge inquires into the circumstances of the case as the judge shall` |
| s 773(4) | the sheriff (power under the warrant of committal) | the surety (liability to confinement) | power - liability | `s 773(4) the warrant authorizes the sheriff to confine the person in this prison` |
| s 773(5) | none (a definition of Attorney General) | none | definitions | `s 773(5) the person is the Attorney General for the purposes of section 771 and this section` |
| s 774 | none (scope: the Part applies to these proceedings) | none | none | `s 774 this Part applies to the proceedings` |
| s 774.1 | the court (claim to the person's presence) | the person who is the subject of a writ of habeas corpus (duty to appear in person) | claim - duty | `s 774.1 the person who is the subject of a writ of habeas corpus appears in court in person as they must` |
| s 775 | the judge or court (power to order further detention or direct what will best further the ends of justice, without determining the question) | the person in custody (liability) | power - liability | `s 775 the judge or court may take this course without determining the question` |
| s 776 | the person convicted or ordered (immunity from removal by certiorari in (a) and (b)) | any court (disability) | immunity - disability | `s 776 the conviction or order shall not be removed by certiorari` |
| s 777(1) | the Crown (immunity: the conviction, order or warrant is not held invalid for the irregularity) | the defendant (disability to rely on it); the court or judge (same powers as an appeal court) | immunity - disability | `s 777(1) the conviction, order or warrant shall not be held to be invalid ...`, `s 777(1) the court or judge has the same powers ...` |
| s 777(2) | the person convicted (claim to a lawful punishment) | the court or judge (duty to correct or remit) | claim - duty | `s 777(2) the court or judge shall correct the sentence or remit the matter`, `s 777(2)(a) the corrected sentence is in accordance with this paragraph`, `s 777(2)(b) ...` |
| s 777(3) | none (the conviction and warrant follow the varied adjudication) | none | none | `s 777(3) the document shall be amended to conform to the adjudication as varied` |
| s 777(4) | none (a rule of sufficiency of a statement) | none | none | `s 777(4) the statement is sufficient for the purposes of the document` |
| s 778 | none (a deeming rule extending section 777) | none | none | `s 778 section 777 is deemed by this section to apply` |
| s 779(1) | the court that may quash (power to prescribe a general order requiring security) | the defendant (liability to give security before a motion is heard) | power - liability | `s 779(1) the court may prescribe by general order that no motion to quash shall be heard unless the defendant gives security`, `s 779(1) the motion to quash may not be heard under the general order` |
| s 779(2) | none (Part XXV applies to such a recognizance) | none | none | `s 779(2) the provisions of Part XXV relating to forfeiture ... apply` |
| s 780 | the clerk of the court (authority to return the conviction, order or proceeding) | none named (passive "proceedings to be taken") | none | `s 780 the order refusing the application is sufficient authority ...` |
| s 781(1) | the Crown (immunity: no quashing or discharge by reason only of the matters listed) | the defendant (disability) | immunity - disability | `s 781(1) the order, conviction or other proceeding shall not be quashed ...` |
| s 781(2) | none (judicial notice) | none | none | `s 781(2) the matter shall be judicially noticed` |
| s 782 | the Crown (immunity: the warrant of committal is not held void by reason only of a defect) | the defendant (disability) | immunity - disability | `s 782 the warrant of committal shall not be held to be void by reason of the defect` |
| s 783 | the court or judge (power to order that no civil proceedings be taken); the justice, provincial court judge or officer (immunity from civil proceedings so ordered) | the person who would sue (disability) | power - liability; immunity - disability | `s 783 the court or judge may order that no civil proceedings shall be taken against the justice, provincial court judge or officer` |
| s 784(1) | the party refused or granted the relief (power to appeal to the court of appeal) | the other party (liability) | power - liability | `s 784(1) an appeal lies to the court of appeal from the decision` |
| s 784(2) | none (Part XXI applies to the appeal) | none | none | `s 784(2) Part XXI applies to the appeal` |
| s 784(3) | the court or judge that refused (immunity from a repeated application on the same grounds); the applicant (power to appeal, and to a further appeal with leave) | the applicant (disability to apply again without fresh evidence) | immunity - disability; power - liability | `s 784(3) no application may again be made on the same grounds`, `s 784(3) an appeal lies to the court of appeal from the refusal`, `s 784(3) a further appeal lies to the Supreme Court of Canada` |
| s 784(4) | the applicant (immunity from an appeal against the granting of the writ) | any party including the Attorney General of the province and of Canada (disability) | immunity - disability | `s 784(4) an appeal lies from the granting of the writ` |
| s 784(5) | the applicant or the Attorney General of the province concerned or of Canada (power to appeal) | any other party (disability); the other side (liability) | power - liability; immunity - disability | `s 784(5) the appeal lies at the instance of this appellant` |
| s 784(6) | the appellant in habeas corpus matters (claim to an early hearing) | the court to which the appeal is directed (duty) | claim - duty | `s 784(6) the appeal is heard at an early date as it shall be` |

## Marginal readings for a lawyer (ccc28)

Reading (a): a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"); flat negatives count as the text saying no.

Reading (b): a prohibition or grant limited by its own wording does not.

Both are taken as the status quo and are not decided here.

Below, every function with a branch that rests on reading (a) or on reading (b), with the number of such branches and the other reading; the branch's own quoted words are on its line in the module (`-- FALSE-kind` and `-- NOTHING-kind` comments).

Counted: 152 branches rest on reading (a) (every `JUST FALSE` branch that is not a closed "means" definition: a failed condition, a flat negative, or a period), in 112 functions; 88 branches rest on reading (b) (every `NOTHING` branch that is "limited by its own wording"); 5 `JUST FALSE` branches rest on a closed "means" definition (the closed definitions of s 752) and are not marginal.


| Function | Branches resting on (a): `JUST FALSE` for a failed condition, a flat negative or a period | Branches resting on (b): `NOTHING` for a limit by the text's own wording | Sample words |
|---|---|---|---|
| `s 752 court` | 1 | 0 | court means the court by which an offender in relation to whom an application under this Part is made was conv... |
| `s 752 serious personal injury offence (a)` | 4 | 0 | other than high treason, treason, first degree or second degree murder |
| `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an application under subsection 752.1(1)` | 1 | 0 | if the prosecutor is of the opinion that an offence for which an offender is found guilty is a serious persona... |
| `s 752.01 the prosecutor advised the court before sentence was imposed` | 1 | 0 | in any event before sentence is imposed |
| `s 752.1(1) the court shall remand the offender for an assessment` | 3 | 0 | On application by the prosecutor |
| `s 752.1(1) the remand is for a period not exceeding 60 days` | 1 | 0 | for a period not exceeding 60 days |
| `s 752.1(2) the report is filed not later than 30 days after the end of the assessment period` | 1 | 0 | not later than 30 days after the end of the assessment period |
| `s 752.1(3) the court may extend the period within which the report must be filed` | 1 | 1 | On application by the prosecutor |
| `s 752.1(3) the extension is by a maximum of 30 days` | 1 | 0 | by a maximum of 30 days |
| `s 753(1) the court shall find the offender to be a dangerous offender` | 2 | 0 | On application made under this Part after an assessment report is filed under subsection 752.1(2) |
| `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` | 2 | 0 | unless the contrary is proved on a balance of probabilities |
| `s 753(2)(a) the notice was given and the application is not later than six months after the imposition of sentence` | 2 | 0 | before the imposition of sentence, the prosecutor gives notice to the offender of a possible intention to make... |
| `s 753(2)(b) relevant evidence became available in the interim and the application is not later than six months after the imposition of sentence` | 2 | 0 | at the time of the application under subsection (1) that is not later than six months after the imposition of ... |
| `s 753(2) the application under subsection (1) is made in time` | 1 | 0 | must be made before sentence is imposed on the offender unless |
| `s 753(3) an application under subsection 752.1(1) may be made after the imposition of sentence or after the offender begins to serve the sentence` | 1 | 0 | in a case to which paragraphs (2)(a) and (b) apply |
| `s 753(4) the disposition is within paragraph (a), (b) or (c)` | 3 | 0 | If the court finds an offender to be a dangerous offender |
| `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | 1 | 0 | unless it is satisfied by the evidence adduced during the hearing of the application |
| `s 753(4.2) the sentence imposed replaces the sentence that was imposed for the offence` | 2 | 0 | If the application is made after the offender begins to serve the sentence |
| `s 753.01(1) the court shall remand the offender for an assessment` | 3 | 0 | If an offender who is found to be a dangerous offender is later convicted of |
| `s 753.01(1) the remand is for a period not exceeding 60 days` | 1 | 0 | for a period not exceeding 60 days |
| `s 753.01(2) the report is filed not later than 30 days after the end of the assessment period` | 1 | 0 | not later than 30 days after the end of the assessment period |
| `s 753.01(3) the court may extend the period within which the report must be filed` | 1 | 1 | On application by the prosecutor |
| `s 753.01(3) the extension is by a maximum of 30 days` | 1 | 0 | by a maximum of 30 days |
| `s 753.01(4) the prosecutor may apply for this sentence or order` | 1 | 0 | After the report is filed |
| `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | 2 | 0 | If the application is for a sentence of detention in a penitentiary for an indeterminate period |
| `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision` | 2 | 0 | If the application is for a new period of long-term supervision |
| `s 753.1(1) the court may find the offender to be a long-term offender` | 1 | 1 | on application made under this Part following the filing of an assessment report under subsection 752.1(2) |
| `s 753.1(2)(a) the offence is one the paragraph names` | 1 | 0 | has been convicted of an offence under section 151 (sexual interference),152 (invitation to sexual touching or... |
| `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender will reoffend` | 1 | 0 | The court shall be satisfied that there is a substantial risk that the offender will reoffend if |
| `s 753.1(3) the sentence and order are within paragraphs (a) and (b)` | 3 | 0 | If the court finds an offender to be a long-term offender |
| `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)` | 3 | 0 | if the application was one that (a) was made after the offender begins to serve the sentence |
| `s 753.1(6) the court shall impose sentence for the offence` | 1 | 0 | If the court does not find an offender to be a long-term offender |
| `s 753.2(1) the offender shall be supervised in the community` | 1 | 1 | when the offender has finished serving |
| `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision` | 1 | 3 | on approval of that Board, the offender's parole supervisor |
| `s 753.2(4) the notice is given at the time the application is made` | 1 | 0 | at the time the application is made |
| `s 753.3(2) the accused may be tried and punished in this place` | 1 | 2 | no proceedings in respect of that offence shall be instituted in that place without the consent of the Attorne... |
| `s 753.4(1) the long-term supervision is interrupted` | 3 | 0 | If an offender who is subject to long-term supervision commits one or more offences under this or any other Ac... |
| `s 754(1) the court may not hear the application` | 2 | 0 | With the exception of an application for remand for assessment |
| `s 754(2) the application is heard and determined by the court without a jury` | 1 | 0 | shall be heard and determined by the court without a jury |
| `s 754(3) no proof of the allegations is required` | 1 | 0 | where an offender admits any allegations contained in the notice referred to in paragraph (1)(b) |
| `s 754(4) the document is proof of the nomination or consent` | 1 | 1 | in the absence of any evidence to the contrary |
| `s 755(1) the court shall not order that the offender be subject to long-term supervision` | 1 | 0 | if they have been sentenced to life imprisonment |
| `s 755(2) the periods of long-term supervision do not total more than 10 years` | 1 | 0 | must not total more than 10 years |
| `s 758(1) the offender shall be present at the hearing of the application` | 1 | 1 | Notwithstanding subsection (1), the court may |
| `s 758(1)(b) the court shall issue a summons or a warrant to compel the accused to attend before the court` | 1 | 0 | if at the time the application is to be heard ... (b) he is not confined in a prison |
| `s 758(2)(a) the court may cause the offender to be removed and kept out of court` | 1 | 0 | where he misconducts himself by interrupting the proceedings so that to continue the proceedings in his presen... |
| `s 760 the court shall order that the reports, testimony, observations and transcript be forwarded to the Correctional Service of Canada` | 1 | 0 | Where a court finds an offender to be a dangerous offender or a long-term offender |
| `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances of the person` | 2 | 0 | where a person is in custody under a sentence of detention in a penitentiary for an indeterminate period |
| `s 761(1) the review is not later than two years after the previous review` | 1 | 0 | not later than every two years after the previous review |
| `s 761(2) the Parole Board of Canada shall review the condition, history and circumstances of the person at least once in every year` | 2 | 0 | Where a person is in custody under a sentence of detention in a penitentiary for an indeterminate period |
| `s 761(2) the review is within a year of the previous review` | 1 | 0 | at least once in every year |
| `s 762(1) the application for forfeiture is made to the court the schedule designates` | 1 | 1 | must be made to the courts designated in column II of the schedule of the respective provinces designated in c... |
| `s 762(2) the person is the clerk of the court` | 1 | 0 | clerk of the court means the officer designated in column III of the schedule in respect of the court designat... |
| `s 762(2) the document is the schedule` | 1 | 0 | schedule means the schedule to this Part |
| `s 763(1) the person and their sureties continue to be bound` | 1 | 1 | If a person is bound by an undertaking, release order or recognizance to appear before a court, provincial cou... |
| `s 763(2) the document sets out a summary of section 763 as it must` | 1 | 1 | A summary of section 763 must be set out in any undertaking, release order or recognizance |
| `s 764(1) the undertaking or release order continues to bind the accused and their sureties for their appearance` | 2 | 1 | If an accused is bound by an undertaking or release order to appear for trial |
| `s 764(2) the court, provincial court judge or justice may take this step` | 1 | 1 | until the accused is discharged or sentenced, as the case may be |
| `s 764(3) the sureties of the accused are discharged` | 1 | 1 | are discharged if the accused is committed to prison under subsection (2) |
| `s 764(4) the document sets out a summary of subsections (1) to (3) as it must` | 1 | 1 | A summary of subsections (1) to (3) must be set out in any undertaking or release order |
| `s 765 the undertaking or release order continues to bind the accused and their sureties despite the arrest on another charge` | 2 | 1 | If an accused is bound by an undertaking or a release order to appear for trial |
| `s 766(1) the court, provincial court judge or justice shall make an order in writing for committal of the person` | 1 | 1 | shall then make an order in writing for committal of that person |
| `s 766(2) the order is given to the surety as it must be` | 1 | 1 | must be given to the surety |
| `s 766(2) this person may arrest the person named in the order and deliver them to the keeper of the prison` | 1 | 1 | on receipt of it |
| `s 766(2) the keeper shall receive and imprison the person` | 1 | 1 | until the person is discharged according to law |
| `s 766(3) the court, provincial court judge or justice shall order an entry of the committal to be endorsed on the document` | 1 | 1 | If a court, provincial court judge or justice issues an order under subsection (1) and receives from the sheri... |
| `s 767 the surety may bring the person before the court` | 1 | 2 | at any time during the sittings of that court and before the person's trial |
| `s 767 the court shall commit the person to prison` | 2 | 0 | The court shall then commit that person to prison |
| `s 767.1(2) the original surety is discharged` | 1 | 0 | If a person substituted for a surety under a release order or recognizance under subsection (1) signs the rele... |
| `s 768 this Part limits the surety's right of taking and giving the person into custody` | 1 | 1 | Nothing in this Part limits any right that a surety has of taking and giving into custody any person |
| `s 769 the interim release provisions of Parts XVI, XXI and XXVII apply in respect of the person` | 1 | 0 | Where a surety for a person has rendered him into custody and that person has been committed to prison |
| `s 769 the person shall forthwith be taken before a justice or judge` | 1 | 0 | Where a surety for a person has rendered him into custody and that person has been committed to prison |
| `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorsed a certificate` | 1 | 1 | If, in proceedings to which this Act applies, a person who is subject to an undertaking, release order or reco... |
| `s 770(1) the certificate is as the subsection requires` | 1 | 0 | a certificate in Form 33 setting out (a) the nature of the default; (b) the reason for the default, if it is k... |
| `s 770(2) the document is sent to the clerk of the court as it must be` | 2 | 0 | Once endorsed, the undertaking, release order or recognizance must be sent to the clerk of the court |
| `s 770(2) the clerk keeps the document with the records of the court as they shall` | 2 | 0 | Once endorsed, the undertaking, release order or recognizance must be sent to the clerk of the court and shall... |
| `s 770(4) the money is sent to the clerk of the court with the defaulted document as it must be` | 2 | 0 | If, in proceedings to which this section applies, the principal or surety has deposited money as security for ... |
| `s 771(1)(a) a judge of the court shall fix a time and place for the hearing of an application for forfeiture` | 1 | 1 | If an undertaking, release order or recognizance has been endorsed with a certificate and has been received by... |
| `s 771(1)(b) the clerk of the court sends the notice as the paragraph requires` | 1 | 0 | not less than 10 days before the time fixed under paragraph (a) for the hearing, send by registered mail, or h... |
| `s 771(2) the judge may take this course` | 1 | 1 | after giving the parties an opportunity to be heard |
| `s 771(3) the principal and their sureties become judgment debtors of the Crown` | 1 | 0 | If a judge orders forfeiture of the amount set out in the undertaking, release order or recognizance, the prin... |
| `s 771(3.1) the clerk shall issue a writ of fieri facias and deliver it to the sheriff of this territorial division` | 1 | 1 | if one is filed, the clerk shall issue a writ of fieri facias |
| `s 771(4) no writ of fieri facias may be issued` | 1 | 0 | If a deposit has been made by a person against whom an order for forfeiture has been made, no writ of fieri fa... |
| `s 771(4) the deposit is transferred to the person entitled by law to receive it as it must be` | 2 | 0 | If a deposit has been made by a person against whom an order for forfeiture has been made |
| `s 772(1) the sheriff executes the writ and deals with the proceeds as the subsection requires` | 2 | 0 | Where a writ of fieri facias is issued pursuant to section 771, the sheriff to whom it is delivered shall exec... |
| `s 772(2) the Crown is entitled to the costs of execution and of proceedings incidental thereto` | 1 | 0 | Where this section applies, the Crown is entitled to the costs of execution |
| `s 773(1) a judge of the court may fix a time and place for the sureties to show cause` | 2 | 0 | Where a writ of fieri facias has been issued under this Part and it appears from a certificate in a return mad... |
| `s 773(2) the notice given to the sureties is seven clear days notice` | 1 | 0 | Seven clear days notice of the time and place fixed for the hearing pursuant to subsection (1) shall be given ... |
| `s 773(3) the judge inquires into the circumstances of the case as the judge shall` | 2 | 0 | The judge shall, at the hearing held pursuant to subsection (1), inquire into the circumstances of the case |
| `s 773(3) the judge may make this order in their discretion` | 1 | 0 | at the hearing held pursuant to subsection (1) |
| `s 773(4) the warrant authorizes the sheriff to confine the person in this prison` | 1 | 2 | until satisfaction is made or until the period of imprisonment fixed by the judge has expired |
| `s 773(5) the person is the Attorney General for the purposes of section 771 and this section` | 1 | 0 | Attorney General means, where subsection 734.4(2) applies, the Attorney General of Canada |
| `s 774.1 the person who is the subject of a writ of habeas corpus appears in court in person as they must` | 1 | 1 | must appear in court in person |
| `s 775 the judge or court may take this course without determining the question` | 1 | 1 | Where proceedings to which this Part applies have been instituted before a judge or court having jurisdiction,... |
| `s 776 the conviction or order shall not be removed by certiorari` | 1 | 0 | No conviction or order shall be removed by certiorari |
| `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the irregularity, informality or insufficiency` | 1 | 2 | where the court before which or the judge before whom the question is raised, on perusal of the evidence, is s... |
| `s 777(2) the court or judge shall correct the sentence or remit the matter` | 1 | 0 | Where, in proceedings to which subsection (1) applies, the court or judge is satisfied that a person was prope... |
| `s 777(2)(a) the corrected sentence is in accordance with this paragraph` | 3 | 0 | by imposing a punishment in accordance with subparagraph (i) or (ii), as the case requires |
| `s 777(2)(b) the punishment imposed on remittal is not greater than the punishment that may be lawfully imposed` | 1 | 0 | to impose a punishment that is not greater than the punishment that may be lawfully imposed |
| `s 777(3) the document shall be amended to conform to the adjudication as varied` | 1 | 1 | Where an adjudication is varied pursuant to subsection (1) or (2) |
| `s 778 section 777 is deemed by this section to apply` | 1 | 0 | that section shall be deemed to apply where |
| `s 779(1) the motion to quash may not be heard under the general order` | 1 | 1 | shall be heard unless the defendant has entered into a recognizance |
| `s 780 the order refusing the application is sufficient authority for the clerk of the court to return the conviction, order or proceeding` | 1 | 0 | Where a motion to quash a conviction, order or other proceeding is refused, the order of the court refusing th... |
| `s 782 the warrant of committal shall not be held to be void by reason of the defect` | 1 | 1 | where (a) it is alleged in the warrant that the defendant was convicted; and (b) there is a valid conviction t... |
| `s 783 the court or judge may order that no civil proceedings shall be taken against the justice, provincial court judge or officer` | 2 | 0 | Where an application is made to quash a conviction, order or other proceeding made or held by a provincial cou... |
| `s 784(2) Part XXI applies to the appeal` | 1 | 1 | Except as provided in this section |
| `s 784(3) no application may again be made on the same grounds` | 2 | 1 | Where an application for a writ of habeas corpus ad subjiciendum is refused by a judge of a court having juris... |
| `s 784(3) an appeal lies to the court of appeal from the refusal` | 1 | 0 | Where an application for a writ of habeas corpus ad subjiciendum is refused by a judge of a court having juris... |
| `s 784(3) a further appeal lies to the Supreme Court of Canada` | 1 | 1 | where on the appeal the application is refused a further appeal shall lie to the Supreme Court of Canada |
| `s 784(4) an appeal lies from the granting of the writ` | 1 | 1 | no appeal therefrom shall lie at the instance of any party including the Attorney General of the province conc... |
| `s 784(5) the appeal lies at the instance of this appellant` | 2 | 1 | Where a judgment is issued on the return of a writ of habeas corpus ad subjiciendum, an appeal therefrom lies |
| `s 784(6) the appeal is heard at an early date as it shall be` | 1 | 1 | shall be heard by the court to which the appeal is directed at an early date |
| `s 753(5) the court may take this course` | 0 | 1 | "If the court does not find an offender to be a dangerous offender": a grant limited by an "if" gate; the text... |
| `s 753.02 the evidence is deemed also to have been given during the hearing` | 0 | 2 | "Any evidence given during the hearing of an application made under subsection 753(1) by a victim": the deemin... |
| `s 753.2(2) the sentence is to be served concurrently with the long-term supervision` | 0 | 2 | "A sentence imposed on an offender referred to in subsection (1)" |
| `s 753.2(3) the onus of proving the ground is on the applicant` | 0 | 1 | "The onus of proving that ground is on the applicant": the sentence speaks of an application under subsection ... |
| `s 753.3(1) the offender is guilty of an offence` | 0 | 2 | "An offender who ... fails or refuses to comply with long-term supervision is guilty of": the provision names ... |
| `s 753.4(2) the court may order a reduction in the length of the period of long-term supervision` | 0 | 1 | "A court that imposes a sentence of imprisonment under subsection (1)": the power is given to a named class of... |
| `s 757 evidence of character and repute may be admitted` | 0 | 1 | "if the court thinks fit": a grant limited by an "if" gate; the section does not say that evidence of characte... |
| `s 758(1)(a) the court may order the person having the custody of the accused to bring the offender before the court` | 0 | 1 | "if at the time the application is to be heard (a) he is confined in a prison, the court may order": a grant l... |
| `s 758(2)(b) the court may permit the offender to be out of court` | 0 | 1 | "during the whole or any part of the hearing": the power is limited to the hearing |
| `s 759(1) the offender may appeal to the court of appeal` | 0 | 1 | "An offender who is found to be a dangerous offender or a long-term offender ... from a decision made under th... |
| `s 759(2) the Attorney General may appeal to the court of appeal` | 0 | 4 | "from a decision made under this Part" |
| `s 759(4) the decision has the same force and effect as a decision of the trial court` | 0 | 1 | "A decision of the court of appeal": the subsection speaks of that court's decision, and is silent about any o... |
| `s 759(6) the day the sentence is deemed to have commenced` | 0 | 1 | "a sentence imposed on an offender by the court of appeal pursuant to this section": the subsection is silent ... |
| `s 759(7) the provisions of Part XXI with respect to procedure on appeals apply to the appeal` | 0 | 1 | "to appeals under this section" |
| `s 766(1) the surety may apply to be relieved of their obligation` | 0 | 2 | "a person who is subject to a release order or recognizance": an undertaking is not named in this subsection |
| `s 766(4) the release order or recognizance is cancelled and the sureties are discharged` | 0 | 1 | "An endorsement under subsection (3) cancels": the subsection speaks of that endorsement, and is silent about ... |
| `s 767 the surety discharges their obligation under the release order or recognizance` | 0 | 1 | "by giving that person into the custody of the court": the section names this way of discharging the obligatio... |
| `s 767.1(1) the court, justice or provincial court judge may substitute another person for the surety` | 0 | 2 | "If a surety ... has given the person into the custody of a court under section 767, or a surety applies to be... |
| `s 770(3) the certificate is evidence of the default to which it relates` | 0 | 1 | "A certificate that has been endorsed on the undertaking, release order or recognizance": the subsection speak... |
| `s 771(3.1) the order may be filed with the clerk of the superior court` | 0 | 1 | "An order made under subsection (2) may be filed": the subsection names that order, and is silent about any ot... |
| `s 772(2) the tariff that fixes the costs` | 0 | 3 | "in the Province of Quebec ... and in any other province": a territory is not a province, and the subsection n... |
| `s 774 this Part applies to the proceedings` | 0 | 1 | "proceedings in criminal matters": the section speaks of criminal matters, and is silent about any other |
| `s 777(1) the court or judge has the same powers to deal with the proceedings as a court to which an appeal might have been taken` | 0 | 1 | "the court or judge has the same powers": the clause is given for proceedings under subsection (1), and is sil... |
| `s 777(4) the statement is sufficient for the purposes of the document` | 0 | 1 | "Any statement that appears in a conviction and is sufficient for the purpose of the conviction": the subsecti... |
| `s 779(1) the court may prescribe by general order that no motion to quash shall be heard unless the defendant gives security` | 0 | 1 | "A court that has authority to quash a conviction, order or other proceeding on certiorari may prescribe": the... |
| `s 779(2) the provisions of Part XXV relating to forfeiture of an amount set out in a recognizance apply` | 0 | 1 | "a recognizance entered into under this section": the subsection speaks of that recognizance, and is silent ab... |
| `s 781(1) the order, conviction or other proceeding shall not be quashed or set aside, nor the defendant discharged, by reason of this want of evidence` | 0 | 1 | "by reason only that evidence has not been given": where there is another ground, the subsection is silent |
| `s 781(2) the matter shall be judicially noticed` | 0 | 1 | "mentioned in subsection (1)": the subsection names those matters, and is silent about any other |
| `s 784(1) an appeal lies to the court of appeal from the decision` | 0 | 4 | "proceedings by way of mandamus, certiorari or prohibition": habeas corpus is not named in this subsection; su... |

The other reading for a column (a) branch is `NOTHING` (the text says what holds when the condition is met, or what is barred, and is silent otherwise); the other reading for a column (b) branch is `JUST FALSE` (a case outside the limit is a case the text does not grant, so the text says no).

In addition, one line for each function flipped under the name-test sweep (the other reading in each is `JUST FALSE`, a failed "if" read as the text's own no):


- F3.1, s 752.1(3): Written `NOTHING` from the first pass when the court is not satisfied that there are reasonable grounds (name-test sweep of 2026-11-12, test 1). No earlier `JUST FALSE` existed, so no assertion was restated. When the separate "On application" gate (F16.1) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). Other reading: `JUST FALSE`: a failed "if" read as the text's own no, so that the answer reads "the court may not extend".
- F3.2, s 753(5): `NOTHING` when the court did find the offender to be a dangerous offender (the "if" gate fails). Written so from the first pass. Other reading: `JUST FALSE`.
- F3.3, s 753.01(3): `NOTHING` when the court is not satisfied that there are reasonable grounds. Written so from the first pass. When the separate "On application" gate (F16.3) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). Other reading: `JUST FALSE`.
- F3.4, s 753.1(1): `NOTHING` when the court is not satisfied of all three of (a), (b) and (c). Written so from the first pass. When the separate "on application" gate (F16.5) also fails the answer is `JUST FALSE`, because that gate is tested first (asserted). Other reading: `JUST FALSE`.
- F3.5, s 757: `NOTHING` when the court does not think fit. Written so from the first pass. Other reading: `JUST FALSE`.
- F3.6, s 758(1)(a): `NOTHING` when the offender is not confined in a prison at the time the application is to be heard. Written so from the first pass. Other reading: `JUST FALSE`.
- F3.7, s 767.1(1): `NOTHING` when the surety has neither given the person into custody under s 767 nor applied to be relieved, and when the other person is not suitable. Written so from the first pass. Other reading: `JUST FALSE`.
- F3.8, s 771(2): `NOTHING` when subsection (1) has not been complied with. Written so from the first pass. The separate "after giving the parties an opportunity to be heard" gate answers `JUST FALSE` and is listed as F16.11; when both gates fail the answer is `JUST FALSE`, because the "after" gate is tested first (asserted), although the text puts the "if" first. Other reading: `JUST FALSE`.

## Seams (ccc28)

**Taken from other parts or from section 2 (inputs).**


- One section 2 term is taken as an input, in two functions: `s 2 superior court of criminal jurisdiction`, as a `MAYBE BOOLEAN` named `s 2 superior court of criminal jurisdiction: the court is a superior court of criminal jurisdiction` in `s 752 court` and `s 2 superior court of criminal jurisdiction: the court applied to is a superior court of criminal jurisdiction` in `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision` (PLAN.md section 4 names the form `s 2 <term>: <the thing asked>`; the answer can be `NOTHING` and is carried through, never turned into `FALSE`).
- Every other section 2 term the range uses (offender, release order, recognizance, undertaking, Attorney General, justice, provincial court judge, prosecutor, prison, clerk of the court) is either a `Party` or `Process document` constructor of the core or a fact the person states, and is not asked of `ccc-definitions`.
- The Schedule to Part XXV (lines 17389-17405, another part's range): s 762(1) takes the Schedule's column I (the province), column II (the designating court) and column III (the clerk) as inputs; the names of the courts and officers are not copied.
- Section 734.4(2) (another part): s 773(5) takes as an input whether subsection 734.4(2) applies, and says which Attorney General it then means (the Attorney General of Canada).
- Part XXI (procedure on appeals), Part XVI, Part XXI and Part XXVII (interim release) are named by ss 759(7), 769 and 784(2) as applying; they are not encoded here, and the functions record only that they apply.

**Given to other parts.**


- `s 752 the offence is a serious personal injury offence` is the answer ccc22 asks at s 606(4.1) (PLAN.md section 6, ccc28 row: "`s 752 the offence is a serious personal injury offence`: MAYBE BOOLEAN").
  The name is the same and the result is a `MAYBE BOOLEAN`.
  The function takes four arguments (the offence as a `s 752 offence`, whether it is first or second degree murder, the penalty limb as a `Punishment`, and the conduct as a `s 752 conduct in the offence`) where ccc22 may have expected a bare input; ccc22 can call it with those facts, or take the answer as an input named the same.
  Which of the two the merge uses is for the lead to decide; nothing here changes the function's name or its result type.
- `s 752 the offence is a designated offence`, `s 752 the offence is a primary designated offence` and `s 752 long-term supervision` are the other definitions of the range and are called inside the Part.

**A seam the plan lacks.**


- Section 753.1(2)(a) names offences, and s 752.1(1) asks whether the offender is convicted of one: `s 753.1(2)(a) the offence is one the paragraph names` is computed in `ccc28-part24b-long-term.l4` and s 752.1(1) takes its answer as an input named `... by s 753.1(2)(a)`; the seat passes one into the other.

## Seat layer (ccc28)

The seat is a person who is, or may be, accused of an offence under the Criminal Code, asking on facts they can state; here, what the Code says about a person who faces an application to be found a dangerous offender or a long-term offender (Part XXIV), about the undertaking, release order or recognizance they or their sureties are bound by (Part XXV), and about the extraordinary remedies (Part XXVI).

`ccc28-seat.l4` holds 38 questions, each named "Under section N, ...", each with `@export` and an `@desc` on every input, returning a `MAYBE BOOLEAN`; `ccc28-cases-seat.l4` holds 137 assertions written equal to the assertions satisfied.

Records the modules expect are built in each question's WHERE from the plain inputs, and the same module rule is then called; a record field the rule never reads is given a placeholder with a comment saying so.

Limits: the offence is stated by the Code, section, subsection or paragraph and the way the person was convicted (a coarser statement than the list names is not matched); at most two previous convictions are asked, each taken as an offence under the Code as it now reads; the court's own judgments are asked as facts; no time limit is asked for the court's orders in these Parts because the text states none for most of them.


**§ Part XXIV: dangerous offenders and long-term offenders**

- Under section 752, is the offence I was convicted of a serious personal injury offence  (calls `s 752 the offence is a serious personal injury offence`)
- Under section 752, is the offence I was convicted of a designated offence  (calls `s 752 the offence is a designated offence`)
- Under section 752, is the offence I was convicted of a primary designated offence  (calls `s 752 the offence is a primary designated offence`)
- Under section 752.01, must the prosecutor advise the court whether they intend to apply for me to be assessed  (calls `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an application under subsection 752.1(1)`)
- Under section 752.1(1), shall the court remand me for an assessment  (calls `s 752.1(1) the court shall remand the offender for an assessment`)
- Under section 753(1), shall the court find me to be a dangerous offender  (calls `s 753(1) the court shall find the offender to be a dangerous offender`)
- Under section 753(1.1), are the conditions for a dangerous offender finding presumed to have been met  (calls `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met`)
- Under section 753(2), is the application for a dangerous offender finding made in time  (calls `s 753(2) the application under subsection (1) is made in time`)
- Under section 753(4.1), shall the court impose a sentence of detention in a penitentiary for an indeterminate period  (calls `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeterminate period`)
- Under section 753(5), may the court take this course  (calls `s 753(5) the court may take this course`)
- Under section 753.01(5), shall the court impose a sentence of detention in a penitentiary for an indeterminate period  (calls `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period`)
- Under section 753.01(6), shall the court order that I be subject to a new period of long-term supervision  (calls `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision`)
- Under section 753.1(1), may the court find me to be a long-term offender  (calls `s 753.1(1) the court may find the offender to be a long-term offender`)
- Under section 753.1(2), shall the court be satisfied that there is a substantial risk that I will reoffend  (calls `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender will reoffend`)
- Under section 753.1(3), are the sentence and the order I received within the limits in paragraphs (a) and (b)  (calls `s 753.1(3) the sentence and order are within paragraphs (a) and (b)`)
- Under section 753.2(1), shall I be supervised in the community  (calls `s 753.2(1) the offender shall be supervised in the community`)
- Under section 753.2(3), may this applicant apply for an order reducing or terminating the period of long-term supervision  (calls `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision`)
- Under section 753.3(1), am I guilty of an offence for failing to comply with long-term supervision  (calls `s 753.3(1) the offender is guilty of an offence`)
- Under section 753.4(1), is my long-term supervision interrupted  (calls `s 753.4(1) the long-term supervision is interrupted`)
- Under section 754(1), does the section bar the court from hearing the application  (calls `s 754(1) the court may not hear the application`)
- Under section 755(1), does the section bar the court from ordering that I be subject to long-term supervision  (calls `s 755(1) the court shall not order that the offender be subject to long-term supervision`)
- Under section 755(2), do my periods of long-term supervision total no more than 10 years  (calls `s 755(2) the periods of long-term supervision do not total more than 10 years`)
- Under section 758(1), must I be present at the hearing of the application  (calls `s 758(1) the offender shall be present at the hearing of the application`)
- Under section 759(1), may I appeal to the court of appeal  (calls `s 759(1) the offender may appeal to the court of appeal`)
- Under section 761(1), shall the Parole Board of Canada review my condition, history and circumstances  (calls `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances of the person`)
- Under section 761(2), shall the Parole Board of Canada review my condition, history and circumstances at least once in every year  (calls `s 761(2) the Parole Board of Canada shall review the condition, history and circumstances of the person at least once in every year`)
**§ Part XXV: effect and enforcement of undertakings, release orders and recognizances**

- Under section 764(1), does my undertaking or release order continue to bind me and my sureties after my arraignment or conviction  (calls `s 764(1) the undertaking or release order continues to bind the accused and their sureties for their appearance`)
- Under section 765, does my undertaking or release order continue to bind me and my sureties despite my arrest on another charge  (calls `s 765 the undertaking or release order continues to bind the accused and their sureties despite the arrest on another charge`)
- Under section 766(1), may my surety apply to be relieved of their obligation  (calls `s 766(1) the surety may apply to be relieved of their obligation`)
- Under section 770(1), shall a court endorse a certificate of default on my undertaking, release order or recognizance  (calls `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorsed a certificate`)
- Under section 771(2), may the judge take this course on an application to forfeit the amount set out in my document  (calls `s 771(2) the judge may take this course`)
- Under section 771(3), do I and my sureties become judgment debtors of the Crown  (calls `s 771(3) the principal and their sureties become judgment debtors of the Crown`)
- Under section 773(1), may a judge fix a time and place for my sureties to show cause why a warrant of committal should not be issued  (calls `s 773(1) a judge of the court may fix a time and place for the sureties to show cause`)
**§ Part XXVI: extraordinary remedies**

- Under section 774.1, does the subject of a writ of habeas corpus appear in court in person as the section requires  (calls `s 774.1 the person who is the subject of a writ of habeas corpus appears in court in person as they must`)
- Under section 776, does the section bar the removal of my conviction or order by certiorari  (calls `s 776 the conviction or order shall not be removed by certiorari`)
- Under section 777(1), shall my conviction, order or warrant not be held to be invalid by reason of an irregularity, informality or insufficiency  (calls `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the irregularity, informality or insufficiency`)
- Under section 784(3), does the section bar a further application for habeas corpus on the same grounds  (calls `s 784(3) no application may again be made on the same grounds`)
- Under section 784(5), does an appeal lie at the instance of this appellant from the judgment on the return of a writ of habeas corpus  (calls `s 784(5) the appeal lies at the instance of this appellant`)

### Seat-question audit, second pass (2026-11-12)

Every seat question's name and `@export` text was read once more against the BODY of the layer-1 function it calls, using the four mismatch criteria of `seat-audit-second-pass.md`, and a question was retitled only when at least one of them held.

Questions read: 38.
Retitled: 4.
Read and left: 34.

The seat file was written in this same session, so the first-pass names (the "was" names below) existed only as the first draft; the retitles are recorded as the pass asks, with each assertion restated in place in `ccc28-cases-seat.l4` as `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>` (15 assertions on the four questions), and no answer changed.


**Retitled (the new name is written exactly as in `ccc28-seat.l4`).**

| New name | First-pass name | Direction or subject of the mismatch |
|---|---|---|
| Under section 753(5), may the court take this course | Under section 753(5), may the court take this course when it does not find me to be a dangerous offender | the old title stated as a given the status that the function tests as an input and does not carry in its own name |
| Under section 753.1(3), are the sentence and the order I received within the limits in paragraphs (a) and (b) | Under section 753.1(3), are the sentence and order I received those the section requires for a long-term offender | the old title said 'requires' where the function checks a minimum and a maximum, and stated as a given the status 'long-term offender' that the function tests as an input |
| Under section 753.2(3), may this applicant apply for an order reducing or terminating the period of long-term supervision | Under section 753.2(3), may I apply for an order reducing or terminating the period of long-term supervision | the old title asked about the offender only ('I'), the function answers for each applicant the subsection names |
| Under section 774.1, does the subject of a writ of habeas corpus appear in court in person as the section requires | Under section 774.1, must I appear in court in person on a writ of habeas corpus | the old title asked whether the duty applies ('must I'), the function answers whether the person does appear as the duty requires: JUST FALSE is a person who does not appear, not a person who need not |

**Read, left (one line of reason each).**

| Question | Function it calls | Reason |
|---|---|---|
| Under section 752, is the offence I was convicted of a serious personal injury offence | `s 752 the offence is a serious personal injury offence` | restates the function's own name; the limbs of paragraphs (a) and (b) are inputs |
| Under section 752, is the offence I was convicted of a designated offence | `s 752 the offence is a designated offence` | restates the function's own name |
| Under section 752, is the offence I was convicted of a primary designated offence | `s 752 the offence is a primary designated offence` | restates the function's own name |
| Under section 752.01, must the prosecutor advise the court whether they intend to apply for me to be assessed | `s 752.01 the prosecutor shall advise the court whether the prosecutor intends to make an application under subsection 752.1(1)` | "must" for "shall" is the same modal; "apply for me to be assessed" is plain wording for the application under 752.1(1); the prosecutor's opinion is an input the title does not assume |
| Under section 752.1(1), shall the court remand me for an assessment | `s 752.1(1) the court shall remand the offender for an assessment` | restates the function's name; "me" for "the offender" is wording |
| Under section 753(1), shall the court find me to be a dangerous offender | `s 753(1) the court shall find the offender to be a dangerous offender` | restates the function's name; the matters the court is satisfied of are inputs |
| Under section 753(1.1), are the conditions for a dangerous offender finding presumed to have been met | `s 753(1.1) the conditions in paragraph (1)(a) or (b) are presumed to have been met` | restates the function's name |
| Under section 753(2), is the application for a dangerous offender finding made in time | `s 753(2) the application under subsection (1) is made in time` | restates the function's name; the dates are inputs |
| Under section 753(4.1), shall the court impose a sentence of detention in a penitentiary for an indeterminate period | `s 753(4.1) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | restates the function's name; the status "found a dangerous offender" is an input and the title does not carry it |
| Under section 753.01(5), shall the court impose a sentence of detention in a penitentiary for an indeterminate period | `s 753.01(5) the court shall impose a sentence of detention in a penitentiary for an indeterminate period` | restates the function's name; the status is an input and the title does not carry it |
| Under section 753.01(6), shall the court order that I be subject to a new period of long-term supervision | `s 753.01(6) the court shall order that the offender be subject to a new period of long-term supervision` | restates the function's name |
| Under section 753.1(1), may the court find me to be a long-term offender | `s 753.1(1) the court may find the offender to be a long-term offender` | restates the function's name; "may" matches the power |
| Under section 753.1(2), shall the court be satisfied that there is a substantial risk that I will reoffend | `s 753.1(2) the court shall be satisfied that there is a substantial risk that the offender will reoffend` | restates the function's name |
| Under section 753.2(1), shall I be supervised in the community | `s 753.2(1) the offender shall be supervised in the community` | restates the function's name; the status "subject to long-term supervision" is an input and the title does not carry it |
| Under section 753.3(1), am I guilty of an offence for failing to comply with long-term supervision | `s 753.3(1) the offender is guilty of an offence` | the body answers the whole offence of 753.3(1) (conduct and excuse); the title names that offence, so it asks neither a narrower nor a wider limb |
| Under section 753.4(1), is my long-term supervision interrupted | `s 753.4(1) the long-term supervision is interrupted` | restates the function's name |
| Under section 754(1), does the section bar the court from hearing the application | `s 754(1) the court may not hear the application` | the function is the bar and the title is the bar (JUST TRUE: the court may not hear it) |
| Under section 755(1), does the section bar the court from ordering that I be subject to long-term supervision | `s 755(1) the court shall not order that the offender be subject to long-term supervision` | the function is the bar and the title is the bar |
| Under section 755(2), do my periods of long-term supervision total no more than 10 years | `s 755(2) the periods of long-term supervision do not total more than 10 years` | restates the function's name |
| Under section 758(1), must I be present at the hearing of the application | `s 758(1) the offender shall be present at the hearing of the application` | "must" for "shall" is the same modal; the function is the duty |
| Under section 759(1), may I appeal to the court of appeal | `s 759(1) the offender may appeal to the court of appeal` | restates the function's name |
| Under section 761(1), shall the Parole Board of Canada review my condition, history and circumstances | `s 761(1) the Parole Board of Canada shall review the condition, history and circumstances of the person` | restates the function's name; the function answers whether the duty arises, as the title asks |
| Under section 761(2), shall the Parole Board of Canada review my condition, history and circumstances at least once in every year | `s 761(2) the Parole Board of Canada shall review the condition, history and circumstances of the person at least once in every year` | restates the function's name |
| Under section 764(1), does my undertaking or release order continue to bind me and my sureties after my arraignment or conviction | `s 764(1) the undertaking or release order continues to bind the accused and their sureties for their appearance` | "after my arraignment or conviction" is the subsection's own "notwithstanding" clause and the answer does not depend on it |
| Under section 765, does my undertaking or release order continue to bind me and my sureties despite my arrest on another charge | `s 765 the undertaking or release order continues to bind the accused and their sureties despite the arrest on another charge` | restates the function's name |
| Under section 766(1), may my surety apply to be relieved of their obligation | `s 766(1) the surety may apply to be relieved of their obligation` | restates the function's name |
| Under section 770(1), shall a court endorse a certificate of default on my undertaking, release order or recognizance | `s 770(1) the court, provincial court judge or justice shall endorse or cause to be endorsed a certificate` | restates the function's name ("shall endorse ... a certificate") |
| Under section 771(2), may the judge take this course on an application to forfeit the amount set out in my document | `s 771(2) the judge may take this course` | "on an application to forfeit" is the context 771(1) gives the subsection, not a premise the text omits |
| Under section 771(3), do I and my sureties become judgment debtors of the Crown | `s 771(3) the principal and their sureties become judgment debtors of the Crown` | restates the function's name |
| Under section 773(1), may a judge fix a time and place for my sureties to show cause why a warrant of committal should not be issued | `s 773(1) a judge of the court may fix a time and place for the sureties to show cause` | restates the function's name; the purpose clause is the subsection's own words |
| Under section 776, does the section bar the removal of my conviction or order by certiorari | `s 776 the conviction or order shall not be removed by certiorari` | the function is the bar and the title is the bar |
| Under section 777(1), shall my conviction, order or warrant not be held to be invalid by reason of an irregularity, informality or insufficiency | `s 777(1) the conviction, order or warrant shall not be held to be invalid by reason of the irregularity, informality or insufficiency` | restates the function's name; JUST TRUE means it shall not be held invalid |
| Under section 784(3), does the section bar a further application for habeas corpus on the same grounds | `s 784(3) no application may again be made on the same grounds` | the function is the bar and the title is the bar |
| Under section 784(5), does an appeal lie at the instance of this appellant from the judgment on the return of a writ of habeas corpus | `s 784(5) the appeal lies at the instance of this appellant` | restates the function's name |

### Name-test sweep of 2026-11-12

Checked against its three tests: every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorised" (40 functions: 38 contain "may", "power" or "entitled"; `s 773(4)` ("authorizes") and `s 780` ("authority") are counted with "authorised/authorized" because each names a grant; none contains "permitted").

Changing nothing else: no `.l4` file was changed by this sweep, because the eight functions of the first column were written `NOTHING` from the first pass (so no assertion was restated), and every other function already answers as the three tests require.


The sweep changed no answer: the eight functions in the first column were written `NOTHING` under test 1 from the first pass, so they count as "flipped" by the test and not by any edit of an earlier answer.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 8 | 8 | 17 | 1 |

Four functions are in both the first and the third column, because they have an "if" gate (flipped) and a separate "on" or "after" gate (listed): s 752.1(3), s 753.01(3), s 753.1(1) and s 771(2).

The 40 functions are 8 + 17 + 1 + 8 + 10 minus those 4 counted twice, where the last 10 are functions that never answer `JUST FALSE` (so there was nothing to flip or keep).


**Flipped to `NOTHING`** (a function named for a grant or a power; a failed "if" answers `NOTHING`; one fork line each in the fork register and in the marginal readings above):

- `s 752.1(3) the court may extend the period within which the report must be filed` (F3.1)
- `s 753(5) the court may take this course` (F3.2)
- `s 753.01(3) the court may extend the period within which the report must be filed` (F3.3)
- `s 753.1(1) the court may find the offender to be a long-term offender` (F3.4)
- `s 757 evidence of character and repute may be admitted` (F3.5)
- `s 758(1)(a) the court may order the person having the custody of the accused to bring the offender before the court` (F3.6)
- `s 767.1(1) the court, justice or provincial court judge may substitute another person for the surety` (F3.7)
- `s 771(2) the judge may take this course` (F3.8)

**Kept `JUST FALSE`** (the text closes the gate itself, or the function is a bar, a duty or the provision's own question):

- `s 753.1(3.1) the court may not impose a sentence under paragraph (3)(a)`: bar ("may not")
- `s 753.3(2) the accused may be tried and punished in this place`: flat negative: "no proceedings ... shall be instituted ... without the consent of the Attorney General" (the `JUST FALSE` branch is that bar, not a failed "if")
- `s 754(1) the court may not hear the application`: bar ("may not ... unless")
- `s 771(4) no writ of fieri facias may be issued`: bar ("no writ ... may be issued")
- `s 771(4) the deposit is transferred to the person entitled by law to receive it as it must be`: duty; "entitled" describes the recipient and the function does not answer an entitlement (judgement call, stated here)
- `s 777(2)(b) the punishment imposed on remittal is not greater than the punishment that may be lawfully imposed`: the provision's own question; "may be lawfully imposed" describes the limit, not a grant
- `s 779(1) the motion to quash may not be heard under the general order`: bar ("shall be heard unless")
- `s 784(3) no application may again be made on the same grounds`: bar ("no application may again be made ... unless")

**Listed, "may" with a where/when/upon-kind gate** (fork rows F16.1 to F16.17; the answer stays as the part gave it):

- F16.1 `s 752.1(3) the court may extend the period within which the report must be filed`
- F16.2 `s 753(3) an application under subsection 752.1(1) may be made after the imposition of sentence or after the offender begins to serve the sentence`
- F16.3 `s 753.01(3) the court may extend the period within which the report must be filed`
- F16.4 `s 753.01(4) the prosecutor may apply for this sentence or order`
- F16.5 `s 753.1(1) the court may find the offender to be a long-term offender`
- F16.6 `s 753.2(3) the applicant may apply for an order reducing or terminating the period of long-term supervision`
- F16.7 `s 758(2)(a) the court may cause the offender to be removed and kept out of court`
- F16.8 `s 764(2) the court, provincial court judge or justice may take this step`
- F16.9 `s 766(2) this person may arrest the person named in the order and deliver them to the keeper of the prison`
- F16.10 `s 767 the surety may bring the person before the court`
- F16.11 `s 771(2) the judge may take this course`
- F16.12 `s 773(1) a judge of the court may fix a time and place for the sureties to show cause`
- F16.13 `s 773(3) the judge may make this order in their discretion`
- F16.14 `s 775 the judge or court may take this course without determining the question`
- F16.15 `s 783 the court or judge may order that no civil proceedings shall be taken against the justice, provincial court judge or officer`
- F16.16 `s 773(4) the warrant authorizes the sheriff to confine the person in this prison`
- F16.17 `s 780 the order refusing the application is sufficient authority for the clerk of the court to return the conviction, order or proceeding`

**Listed, "entitled"** (fork row F17.1):

- F17.1 `s 772(2) the Crown is entitled to the costs of execution and of proceedings incidental thereto`

**Names that contain one of the words but never answer `JUST FALSE`** (nothing to flip or keep; ten):

- `s 753.4(2) the court may order a reduction in the length of the period of long-term supervision`
- `s 758(1)(a) the court's power to order the person having the custody to bring the offender` (a regulative rule: PARTY `the court` MAY ...)
- `s 758(2)(b) the court may permit the offender to be out of court`
- `s 759(1) the offender may appeal to the court of appeal`
- `s 759(2) the Attorney General may appeal to the court of appeal`
- `s 759(3) the court of appeal may make this disposition`
- `s 766(1) the surety may apply to be relieved of their obligation`
- `s 771(3.1) the order may be filed with the clerk of the superior court`
- `s 777(1) the court or judge has the same powers to deal with the proceedings as a court to which an appeal might have been taken`
- `s 779(1) the court may prescribe by general order that no motion to quash shall be heard unless the defendant gives security`

**Outside the sweep: named "it is lawful".**

Scoped ("s N makes it lawful ..."): 0.

Unscoped and retitled to the scoped form: 0.

No function of this part is named "it is lawful" (`grep -i "it is lawful\|makes it lawful" ccc28-*.l4` finds nothing); `s 777(2)(b)` contains "lawfully imposed" in a description of the limit and is the provision's own question.


## What the text turns out to say (ccc28)

1. The definition of "long-term supervision" in s 752 (line 16353) lists "subsection 753(4), 753.01(5) or (6) or 753.1(3) or subparagraph 759(3)(a)(i)"; subsection 753.01(5) (line 16438) has the court impose an indeterminate sentence "unless it is satisfied ... that a sentence for the offence ... with or without a new period of long-term supervision ... will adequately protect the public", and it is subsection (6) (line 16440) that orders "a new period of long-term supervision". `s 752 long-term supervision` follows the definition as written and lists 753.01(5); whether (5) itself orders supervision is not decided here.
2. Section 766(2) (line 16563) has the surety or a peace officer deliver the person to "the keeper of the prison", and section 766(3) (line 16565) speaks of a certificate received "from the sheriff" that the person has been committed to prison under subsection (2); the sheriff is not named in (2).
3. Section 772(2) (line 16605) fixes the costs by the tariff in "the Province of Quebec" and "any other province"; a territory is not named, so `s 772(2) the tariff that fixes the costs` answers `NOTHING` for a territory (fork F12).
4. Three passive duties name no actor: s 766(2) ("must be given to the surety"), s 770(2) ("must be sent to the clerk of the court") and s 773(2) ("shall be given to the sureties"); no regulative rule is written for them (fork F11).
5. "Serious personal injury offence" paragraph (b) (line 16387) names "an offence or attempt to commit an offence" under the listed sections and does not name a conspiracy, while "designated offence" paragraph (d) (line 16352) and "primary designated offence" paragraph (e) (line 16382) take in "an attempt or conspiracy"; `s 752 serious personal injury offence (b)` therefore answers `JUST FALSE` for a conspiracy to commit a listed offence.
6. Section 784(5) (line 16680) lets an appeal go from the court of appeal to the Supreme Court of Canada "with the leave of that Court", and s 784(3) (line 16676) does the same for a refusal of habeas corpus; where leave has not been given the text is silent, so the answer is `NOTHING` (limited by its own wording).
7. Section 755(2) (line 16499) caps the supervision at 10 years in total "at any particular time" but does not say how long a month is; the in-between band of days is `NOTHING` (fork F9).
8. Section 753.2(2) (line 16470) is silent for a sentence that requires imprisonment ("other than a sentence that requires imprisonment") (fork F5).

## What the stable binary does not accept (ccc28)

No construct the brief lists as available was refused in this range, and no construct was found that the brief does not list.

Things that cost attempts, so that the next encoder need not repeat them:


- An identifier with parentheses must be written in backticks everywhere, including as the head of a local definition: `paragraph (a) holds`, not `paragraph (a) MEANS`.
- `NOT x OR y` parses as `NOT (x OR y)`: parenthesise every `NOT`, which the brief already says.
- A regulative action constructor with a `HAS` payload and a `PROVIDED` guard was not accepted; the 60-day limit of s 752.1(1) is a separate decision function.
- `NOT a EQUALS b` is not accepted: write `NOT (a EQUALS b)`.
- `(`fn` arg)'s `field`` needs the parentheses; `fn arg's field` reads the projection as part of the argument.
- The core has `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years` and `fourteen years` as `Length of time` constants and no `one year`; a length of one year is `Length of time OF 1, 0, 0, FALSE`.
- `add months` and `add years` of daydate clamp to the end of a shorter month (`Date 31 8 2020` plus six months is 28 February 2021).

## What check.sh prints (ccc28)

Baseline before any edit of mine (2026-11-16): 3 modules (the keel's `ccc-core`, `ccc-definitions` and `ccc-interpretation`), 0 errors, 0 satisfied, 0 failed, 0 refused, the same on 1.6.109.

Last run, with the seat layer, after the audit and the sweep:


```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc28-cases-seat.l4                            0       137       0        0         0 |      0       137       0        0  same
ccc28-part24-s752.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc28-part24a-dangerous-offender.l4            0         0       0        0         0 |      0         0       0        0  same
ccc28-part24b-long-term.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc28-part24c-hearing-appeal.l4                0         0       0        0         0 |      0         0       0        0  same
ccc28-part25-forfeiture.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc28-part26-extraordinary-remedies.l4         0         0       0        0         0 |      0         0       0        0  same
ccc28-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc28-tests-part24-s752.l4                     0       227       0        0         0 |      0       227       0        0  same
ccc28-tests-part24a.l4                         0       127       0        0         0 |      0       127       0        0  same
ccc28-tests-part24b.l4                         0       137       0        0         0 |      0       137       0        0  same
ccc28-tests-part24c.l4                         0        58       0        0         0 |      0        58       0        0  same
ccc28-tests-part25.l4                          0       189       0        0         0 |      0       189       0        0  same
ccc28-tests-part26.l4                          0       124       0        0         0 |      0       124       0        0  same
TOTAL (17 modules)                             0       999       0        0           |      0       999       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `--strict` over every `ccc28-*.l4`: 307 src: lines, 153 runs, 180 locators, 0 problems in each mode.

#TRACE: with `JL4_LIBRARY_PATH` unset, the full output of `l4 run` on each of the five test files that hold regulative rules (`ccc28-tests-part24a`, `24b`, `24c`, `25`, `26`) is byte-identical on 1.6.110 and 1.6.109 (a diff of 0 lines each), and the number of `#TRACE` lines in each file (10, 3, 7, 9, 3) equals the number of evaluation results printed by each build.


