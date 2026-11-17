# NOTES.md -- ccc19: the Criminal Code (Canada), R.S.C., 1985, c. C-46, PART XV.1 Unreasonable Delay, ss 492.21 to 492.31 (text lines 10957-11031)

Status (2026-11-13, part agent `ccc19`, model Sonnet 5.5): every number below was produced by a command run in this session (the commands are in `PROGRESS.md` and under `work/`, which is not shipped).
The target is the stable `l4` 1.6.110 (main, e51181d, 2026-11-11), checked against the second stable build 1.6.109 (main, 4c887e0, 2026-11-04) by `check.sh`.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30; last amended 2026-07-18; `inputs/SOURCES.md`).
It is not the official text, and nothing here is claimed verified against the official text.
The French version is equally authoritative and is not among the sources; the French equivalents in parentheses after a defined term are quoted inside the quotation lines, not encoded.
No independent test pass was run (no subagent was available): the tests were written by the same agent that wrote the rules, expected values first, from the text.
Where PLAN.md and the brief differ the brief governs: see "## Seams (ccc19)", the last paragraph.

## What is encoded and what is not

The whole of PART XV.1 Unreasonable Delay: eleven sections, 492.21 to 492.31, 75 lines of the text (67 non-blank).
Every unit has a row in the coverage table below with one disposition (60 rows: 23 encoded, 20 fork, 17 inert; no `repealed`, no `out-of-scope`, no `deferred`).
Layer 1 is five modules, one per group of headings, each with a tests module:

| module | sections | tests module | assertions | #TRACE |
| --- | --- | --- | --- | --- |
| `ccc19-s492-21-to-24.l4` | 492.21 definitions, 492.22 jurisdiction not lost, 492.23 stay only in accordance with this Part, 492.24 common law | `ccc19-tests-s492-21-to-24.l4` | 30 | 3 |
| `ccc19-s492-25.l4` | 492.25 notice to victims | `ccc19-tests-s492-25.l4` | 14 | 10 |
| `ccc19-s492-26.l4` | 492.26 case complexity | `ccc19-tests-s492-26.l4` | 13 | 7 |
| `ccc19-s492-27-to-3.l4` | 492.27, 492.28, 492.29 days to be excluded; 492.3 actions not made in good faith | `ccc19-tests-s492-27-to-3.l4` | 92 | 8 |
| `ccc19-s492-31.l4` | 492.31 alternative remedies to a stay | `ccc19-tests-s492-31.l4` | 12 | 7 |

Layer 2 is `ccc19-seat.l4` (21 questions) and `ccc19-cases-seat.l4` (78 assertions).
Layer 1 imports `prelude`, `daydate` (module D only) and `ccc-core`; the seat also imports `ccc-definitions`, to call the keel's `s 2 victim` and `s 2 clerk of the court`.
Every decision function answers a `MAYBE BOOLEAN`; every duty and prohibition is encoded twice, as a decision function and as a regulative rule (`DEONTIC Party <act>`), which is exercised with `#TRACE`.
Every top-level name begins with the label of its provision (`s 492.25(1) ...`), including every `DECLARE`d type and constructor.
Every quotation is a `-- src:N | text` line made by `srcrefs.py quote` (by `work/gen.py`, which reads the raw text), and `srcrefs.py check --refs` and `--strict` report 0 problems on every file.
Nothing was copied from another encoding; nothing was imported from another subject.

## Seat

The seat is the brief's: a person who is, or may be, accused of an offence under the Criminal Code (the accused), asking, on facts they can state, whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction.
(Assumed, not ruled: Singapore's Penal Code is the model, as the maintainer instructed on 2026-11-09, but this is a plain seat layer; no charge-generator contract.)
This range answers the part of that seat about delay: what the court must count and must not count against the Crown when it decides whether the accused has waited too long to be tried, who must tell the victims, what stops a court staying the case, and what the court must weigh before it does.
Part XV.1 addresses only courts and prosecutors, so the questions are asked for what the provisions mean to the accused (what the court may not count against them, what the court must weigh, what a prosecutor's failure does not stop).
There is no seat for an official.
The questions apply only where delay is being raised in the accused's case; each `§` heading's comment says so, so that a form can ask "Has an application for a finding of unreasonable delay been, or is it about to be, filed in your case?" first.

## Coverage (ccc19)

One row per unit of lines 10957-11031 of `R.S.C.-1985-c.-C-46.txt`, built by `work/coverage.py`, which checks that every non-blank line of the range is in exactly one row and that every L4 name a row cites occurs in a layer-1 module.
Dispositions: `encoded` (a rule, definition or table in layer-1 L4 with a test and an `@ref`), `fork` (the text can be read two or more ways: the row points at the fork-register entry, and the rule it names encodes the reading taken), `inert` (reason 1: not operative, a heading or marginal note; reasons 2 and 3 are not used: nothing in the range is machinery or shown repealed).
No row is `out-of-scope`, `deferred` or `repealed or blank in this text`.

**Audit.** An independent scan of the text by line type counted, in the 75 lines (67 non-blank): 1 Part heading; 23 heading and marginal-note lines (16 groups: 9 marginal notes standing alone and 7 pairs of a heading and a marginal note); 11 sections; 5 subsection lines besides the three subsections (1) that share a line with their section (s 492.25(2) to (4), s 492.26(2), s 492.31(2)); 19 paragraphs (s 492.26(2)(a)-(h), 492.27(a)-(c), 492.28(a)-(c), 492.31(2)(a)-(e)); 6 subparagraphs ((i) and (ii) of each of 492.27(a), (b), (c)); and 2 defined terms ("court", "unreasonable delay"): 43 content lines, which is 43 content rows, plus 17 inert rows covering the Part heading and the 23 heading lines.
Rows before the line-coverage audit: 60. Rows after it: 60. The audit found 0 non-blank lines in no row and 0 in more than one.
The totals: 60 rows = 23 `encoded` + 20 `fork` + 17 `inert`.


| text lines | unit | disposition | L4 name (module) | note |
| --- | --- | --- | --- | --- |
| 10957 | PART XV.1 Unreasonable Delay (Part heading) | inert | (none) | reason 1: heading |
| 10959-10960 | Headings "Definitions" (heading and marginal note) | inert | (none) | reason 1: headings |
| 10961 | s 492.21 lead-in: "The following definitions apply in this Part." | encoded | `s 492.21 the definitions apply to the provision` (ccc19-s492-21-to-24) | the Part is ss 492.21 to 492.31; a provision outside it is NOTHING |
| 10962 | s 492.21 "court" (defined term) | encoded | `s 492.21 court` (ccc19-s492-21-to-24) | a "means" definition |
| 10963 | s 492.21 "unreasonable delay" (defined term) | encoded | `s 492.21 unreasonable delay` (ccc19-s492-21-to-24) | Charter paragraph 11(b) is the input (a MAYBE BOOLEAN); NOTHING passes through |
| 10965-10966 | Headings "Jurisdiction", "Jurisdiction not lost" | inert | (none) | reason 1: headings |
| 10967 | s 492.22 a finding of unreasonable delay does not deprive the court of jurisdiction | fork | `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction` (ccc19-s492-21-to-24)<br>`s 492.22 matter of jurisdiction` (ccc19-s492-21-to-24) | fork F1 |
| 10969-10970 | Headings "Application", "Stay of proceedings" | inert | (none) | reason 1: headings |
| 10971 | s 492.23 a court shall not order a stay except in accordance with this Part | fork | `s 492.23 the court is barred from ordering a stay of proceedings` (ccc19-s492-21-to-24)<br>`s 492.23 the court shall not order a stay of proceedings` (ccc19-s492-21-to-24) | fork F2 |
| 10972 | Marginal note "Common law rules and principles" | inert | (none) | reason 1: marginal note |
| 10973 | s 492.24 common law rules and principles continue to apply | fork | `s 492.24 the rule or principle of the common law continues to apply` (ccc19-s492-21-to-24) | fork F3 |
| 10975-10976 | Headings "Notice to Victims", "Reasonable steps to inform" | inert | (none) | reason 1: headings |
| 10977 | s 492.25(1) the prosecutor shall take reasonable steps to inform any victim of the filing | fork | `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing` (ccc19-s492-25)<br>`s 492.25(1) the duty of the prosecutor to inform the victims of the filing` (ccc19-s492-25) | fork F4; gate: case-by-case site F13 |
| 10978 | Marginal note "Court to inquire if notice given" | inert | (none) | reason 1: marginal note |
| 10979 | s 492.25(2) the court shall inquire of the prosecutor | encoded | `s 492.25(2) the court must inquire of the prosecutor whether reasonable steps were taken to inform the victims` (ccc19-s492-25)<br>`s 492.25(2) the duty of the court to inquire of the prosecutor` (ccc19-s492-25) | gate "at the time the application is heard": F13 |
| 10980 | Marginal note "Notice of court’s decision" | inert | (none) | reason 1: marginal note |
| 10981 | s 492.25(3) the prosecutor shall inform the victims of the decision | fork | `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision` (ccc19-s492-25)<br>`s 492.25(3) the duty of the prosecutor to inform the victims of the decision` (ccc19-s492-25) | fork F4; gates: F13 |
| 10982 | Marginal note "Decision not precluded" | inert | (none) | reason 1: marginal note |
| 10983 | s 492.25(4) the failure of the prosecutor does not preclude the court from making a decision | encoded | `s 492.25(4) the failure of the prosecutor precludes the court from making a decision on the application` (ccc19-s492-25) | a flat negative: JUST FALSE where the failure occurred; NOTHING where it did not |
| 10985-10986 | Headings "Case Complexity", "Case complexity — factors" | inert | (none) | reason 1: headings |
| 10987 | s 492.26(1) the court shall consider whether any relevant factors made the case complex | encoded | `s 492.26(1) the court must consider whether any relevant factors contributed or will contribute to making the case complex` (ccc19-s492-26)<br>`s 492.26(1) the duty of the court to consider case complexity` (ccc19-s492-26) | gate "In determining": F13 |
| 10988 | Marginal note "Applications and motions — factors" | inert | (none) | reason 1: marginal note |
| 10989 | s 492.26(2) lead-in: if the case involved or will involve applications or motions, the court shall also consider the following factors | encoded | `s 492.26(2) the court must also consider the factor in assessing whether the case is complex` (ccc19-s492-26)<br>`s 492.26(2) the duty of the court to consider the factor` (ccc19-s492-26)<br>`s 492.26(2) factor` (ccc19-s492-26) | gate "If": F13 |
| 10990 | s 492.26(2)(a) the number of applications or motions | encoded | `s 492.26(2)(a) the number of applications or motions` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10991 | s 492.26(2)(b) whether any of the applications or motions required or will require scheduling court dates separately and in advance of trial dates | encoded | `s 492.26(2)(b) whether any of the applications or motions required or will require scheduling court dates separately and in advance of trial dates` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10992 | s 492.26(2)(c) whether any adjournments were or will be required | encoded | `s 492.26(2)(c) whether any adjournments were or will be required in order to complete the steps required by any of the applications or motions` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10993 | s 492.26(2)(d) whether more than one judicial decision was or will be needed (the line ends without a semicolon in the text) | encoded | `s 492.26(2)(d) whether more than one judicial decision was or will be needed to complete the steps required by any of the applications or motions` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10994 | s 492.26(2)(e) the amount of cumulative court time | encoded | `s 492.26(2)(e) the amount of cumulative court time that was or will be required to adjudicate the applications or motions` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10995 | s 492.26(2)(f) the need for trial continuation dates (applications that required more time than anticipated) | encoded | `s 492.26(2)(f) the need for trial continuation dates arising from the applications or motions that required more time than anticipated` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10996 | s 492.26(2)(g) the need for trial continuation dates (applications not scheduled in advance of the trial) | encoded | `s 492.26(2)(g) the need for trial continuation dates arising from the applications or motions that were not scheduled in advance of the trial` (ccc19-s492-26) | a constructor of `s 492.26(2) factor`; the court's duty is the same for (a) to (g) |
| 10997 | s 492.26(2)(h) any factor that the court finds relevant in assessing the complexity of the applications or motions | fork | `s 492.26(2)(h) another factor, not named in paragraphs (a) to (g)` (ccc19-s492-26) | fork F5; the court's finding of relevance is an input |
| 10999-11000 | Headings "Days to Be Excluded", "Exclusions — sexual offence proceedings" | inert | (none) | reason 1: headings |
| 11001 | s 492.27 lead-in (the chapeau): subject to section 492.3, in determining ..., the court shall not take into account any day within any of the following periods | fork | `s 492.27 the court shall not take the day into account, subject to section 492.3` (ccc19-s492-27-to-3)<br>`s 492.27 the prohibition on the court taking the day into account` (ccc19-s492-27-to-3) | fork F9; gate "in determining": F13 |
| 11002 | s 492.27(a) application under section 276.01, if a copy was not filed with the clerk of the court at least 60 days before the hearing | fork | `s 492.27(a) the day is within a period of paragraph (a)` (ccc19-s492-27-to-3)<br>`s 492.27(a) a copy of the application was filed with the clerk of the court at least 60 days before the hearing` (ccc19-s492-27-to-3)<br>`s 492.27(a) the court shall not take the day into account` (ccc19-s492-27-to-3) | fork F7; the clerk is the s 2 seam |
| 11003 | s 492.27(a)(i) the period that consists of the cumulative number of days it took to hear the application | encoded | `s 492.27(i) a day it took to hear the application` (ccc19-s492-27-to-3) | a constructor of `s 492.27 kind of day`; the same constructor serves (b)(i) and (c)(i) |
| 11004 | s 492.27(a)(ii) any other period, as determined by the court, attributable to the late filing, including delay caused by adjournment | fork | `s 492.27(ii) a day in another period that the court has determined is attributable to the fact that a copy of the application was not filed or served at least 60 days before the hearing` (ccc19-s492-27-to-3) | fork F6 |
| 11005 | s 492.27(b) application under section 278.12 or 278.21, if a copy was not served at least 60 days before the hearing to the persons referred to | fork | `s 492.27(b) the day is within a period of paragraph (b)` (ccc19-s492-27-to-3)<br>`s 492.27(b) a copy of the application was served at least 60 days before the hearing` (ccc19-s492-27-to-3)<br>`s 492.27(b) the court shall not take the day into account` (ccc19-s492-27-to-3) | forks F7 and F8 |
| 11006 | s 492.27(b)(i) the cumulative number of days it took to hear the application | encoded | `s 492.27(i) a day it took to hear the application` (ccc19-s492-27-to-3) | the same constructor as (a)(i) |
| 11007 | s 492.27(b)(ii) any other period, as determined by the court, attributable to the late filing | fork | `s 492.27(ii) a day in another period that the court has determined is attributable to the fact that a copy of the application was not filed or served at least 60 days before the hearing` (ccc19-s492-27-to-3) | fork F6 |
| 11008 | s 492.27(c) application under section 278.3, if a copy was not filed with the clerk of the court at least 60 days before the hearing | fork | `s 492.27(c) the day is within a period of paragraph (c)` (ccc19-s492-27-to-3)<br>`s 492.27(c) a copy of the application was filed with the clerk of the court at least 60 days before the hearing` (ccc19-s492-27-to-3)<br>`s 492.27(c) the court shall not take the day into account` (ccc19-s492-27-to-3) | fork F7; the clerk is the s 2 seam |
| 11009 | s 492.27(c)(i) the cumulative number of days it took to hear the application | encoded | `s 492.27(i) a day it took to hear the application` (ccc19-s492-27-to-3) | the same constructor as (a)(i) |
| 11010 | s 492.27(c)(ii) any other period, as determined by the court, attributable to the late filing | fork | `s 492.27(ii) a day in another period that the court has determined is attributable to the fact that a copy of the application was not filed or served at least 60 days before the hearing` (ccc19-s492-27-to-3) | fork F6 |
| 11011 | Marginal note "Exclusions — Canada Evidence Act" | inert | (none) | reason 1: marginal note |
| 11012 | s 492.28 lead-in (the chapeau, in the same words as s 492.27) | fork | `s 492.27 the court shall not take the day into account, subject to section 492.3` (ccc19-s492-27-to-3)<br>`s 492.28 the day falls within the period that begins on one day and ends on another` (ccc19-s492-27-to-3) | forks F9 and F10; encoded once, for ss 492.27 to 492.29 |
| 11013 | s 492.28(a) objection under subsection 37(1) of the Canada Evidence Act before a superior court: from the day made to the day finally determined | fork | `s 492.28(a) the court shall not take the day into account` (ccc19-s492-27-to-3) | forks F10 and F11 |
| 11014 | s 492.28(b) objection before a court, person or body other than a superior court and an application under subsection 37(3): from the day the objection was made to the day the application was finally determined | fork | `s 492.28(b) the court shall not take the day into account` (ccc19-s492-27-to-3) | forks F10 and F11 |
| 11015 | s 492.28(c) application under subsection 38.04(1) or (2) in respect of a notice given under subsections 38.01(1) to (4): from the day made to the day finally determined | fork | `s 492.28(c) the court shall not take the day into account` (ccc19-s492-27-to-3) | forks F10 and F11 |
| 11016 | Marginal note "Exclusion — Canadian Security Intelligence Service Act" | inert | (none) | reason 1: marginal note |
| 11017 | s 492.29 subject to section 492.3, the court shall not take into account any day within the period of an application under subsection 18.1(4) of the Canadian Security Intelligence Service Act | fork | `s 492.29 the court shall not take the day into account` (ccc19-s492-27-to-3) | forks F9 and F10 |
| 11018 | Marginal note "Actions not made in good faith" | inert | (none) | reason 1: marginal note |
| 11019 | s 492.3 for greater certainty, the court shall take into account any frivolous or dilatory action, or action not made in good faith, taken by the prosecutor, counsel for the Attorney General of Canada or a person acting for either | fork | `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith` (ccc19-s492-27-to-3)<br>`s 492.3 the duty of the court to take the action into account` (ccc19-s492-27-to-3)<br>`s 492.3 who took the action` (ccc19-s492-27-to-3) | fork F9 |
| 11021-11022 | Headings "Alternative Remedies to Stay of Proceedings", "Alternative remedies to be considered" | inert | (none) | reason 1: headings |
| 11023 | s 492.31(1) a court shall not order a stay of proceedings unless satisfied that no other remedy would be appropriate and just | fork | `s 492.31(1) the court is barred from ordering a stay of proceedings` (ccc19-s492-31)<br>`s 492.31(1) the court shall not order a stay of proceedings` (ccc19-s492-31) | fork F12 |
| 11024 | Marginal note "Factors to be considered" | inert | (none) | reason 1: marginal note |
| 11025 | s 492.31(2) lead-in: in determining whether a remedy other than a stay is appropriate and just, the court shall take into account the following factors | encoded | `s 492.31(2) the court must take the factor into account` (ccc19-s492-31)<br>`s 492.31(2) the duty of the court to take the factor into account` (ccc19-s492-31)<br>`s 492.31(2) factor` (ccc19-s492-31) | gate "In determining": F13; the list is not closed, so another factor is NOTHING |
| 11026 | s 492.31(2)(a) the stage of the proceedings | encoded | `s 492.31(2)(a) the stage of the proceedings during which the finding of unreasonable delay is made or during which the delay became unreasonable` (ccc19-s492-31) | a constructor of `s 492.31(2) factor` |
| 11027 | s 492.31(2)(b) the impact that a stay is likely to have on any victim | encoded | `s 492.31(2)(b) the impact that a stay of proceedings is likely to have on any victim of the offence` (ccc19-s492-31) | a constructor of `s 492.31(2) factor` |
| 11028 | s 492.31(2)(c) the prejudice that has been or would be suffered by the accused or offender | encoded | `s 492.31(2)(c) the prejudice that has been or would be suffered by the accused or offender as a result of unreasonable delay` (ccc19-s492-31) | a constructor of `s 492.31(2) factor` |
| 11029 | s 492.31(2)(d) the public’s confidence in the administration of justice | encoded | `s 492.31(2)(d) the public’s confidence in the administration of justice` (ccc19-s492-31) | a constructor of `s 492.31(2) factor` |
| 11030 | s 492.31(2)(e) the interest that society has in having a final decision on the merits | encoded | `s 492.31(2)(e) the interest that society has in having a final decision on the merits` (ccc19-s492-31) | a constructor of `s 492.31(2) factor` |


## Fork register (ccc19)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry: the provision and function, the readings and the text that licenses each, the reading taken.
The reading taken is the status quo for a human reviewer to overrule.
The rulings are copied at the end of this section, by script, from the brief.

- **F1. s 492.22** (`s 492.22 a finding of unreasonable delay deprives the court of jurisdiction`; line 10967). "A finding of unreasonable delay by a court in respect of any proceedings does not deprive a court seized with those proceedings of jurisdiction in respect of the offence, the accused or the offender."
  Reading A (taken): a flat negative (ruling N2: it counts as the text's no) about the three things named; a finding not made, a court not seized with the proceedings, or a thing other than the offence, the accused and the offender (a witness, a surety) is outside it: NOTHING. Licence: "a court" twice, "the offence, the accused or the offender" with no "only".
  Reading B: the three are examples, and "anything else" is also JUST FALSE. Reading C: the court that made the finding and the court seized with the proceedings are the same court, so only one input is needed; the encoding asks two, because the text says "a court" and "a court seized".
- **F2. s 492.23** (`s 492.23 the court is barred from ordering a stay of proceedings`; line 10971). "A court shall not order a stay of proceedings as a result of a finding of unreasonable delay except in accordance with this Part."
  Reading A (taken): once the "except" is met (the stay is in accordance with this Part) the section does not bar it: JUST FALSE, which is "this section does not bar it", not a grant ("an except once it is met" is one of the six case-by-case questions). Reading B: NOTHING.
  Second fork in the same sentence: what "in accordance with this Part" requires. Reading A (taken): a BOOLEAN input, so that each section answers for itself (ruling E1, option C). Reading B: derive it from s 492.31(1) and (2), the Part's only conditions on a stay, which gathers several sections into one answer (E1, option B, "by hand only").
  Note that Part XV.1 gives no court the power to order a stay or any other remedy (finding 1): the sentence presupposes a power that lives outside this text.
- **F3. s 492.24** (`s 492.24 the rule or principle of the common law continues to apply`; line 10973). "Rules and principles of the common law in respect of a determination of unreasonable delay continue to apply except insofar as they are altered by or are inconsistent with this Part."
  Reading A (taken): asked of one rule and of the part of it in issue ("insofar as"): JUST TRUE if that part is neither altered nor inconsistent; JUST FALSE if it is either (the text's "except"); NOTHING if it is not a common-law rule or principle in respect of a determination of unreasonable delay. Reading B: all-or-nothing for the whole rule (a rule partly altered would not continue at all): contradicted by "insofar as".
  The two limbs "altered by" and "inconsistent with" are separate inputs; the text does not say which prevails when both are true (the answer is the same).
- **F4. s 492.25(1) and (3), the victims** (lines 10977, 10981). (1) "inform any victim of the offence referred to in the application"; (3) "inform the victims, if any, of the decision".
  Taken: with no victim, (1) is NOTHING ("any victim" is a scope limit with no "only": ruling of 2026-11-05 (c)) and (3) is JUST FALSE (the text's own ", if any": a failed "if"). Other reading: both JUST FALSE, or both NOTHING; the text uses two different words for the same situation.
  Whether there is a victim is the section 2 term "victim" (seam `s 2 victim: ...`, a `MAYBE BOOLEAN`); its extension "for the purposes of sections 672.5, 722 and 745.63" leaves a person harmed only by an offence against someone else NOT COVERED for section 492.25, and that NOTHING passes through.
  Subsection (2) is not gated on a victim: ", if any" qualifies the victims the court inquires about, not its duty.
- **F5. s 492.26(2), the list and paragraph (h)** (lines 10989-10997). "the court shall also consider the following factors ... (h) any factor that the court finds relevant in assessing the complexity of the applications or motions".
  Taken: paragraphs (a) to (g) are seven factors the court must consider whether or not the court finds them relevant; paragraph (h) is a factor the court has found relevant (a plain input: the judgment is the court's); a factor the court has not found relevant is NOTHING (the list is not closed by "only").
  Other reading: because (h) says "any factor that the court finds relevant", the court is bound to consider any relevant factor at all (so a factor the court has not found relevant but which is relevant is JUST TRUE). Not taken: it would put the encoding in the court's place.
  The text of (d) has no closing semicolon (a transcription quirk: finding 6); it is quoted as the text has it.
- **F6. s 492.27(a)(ii), (b)(ii), (c)(ii)** (lines 11004, 11007, 11010). "any other period, as determined by the court, that is attributable to the fact that a copy of the application was not filed [served] ... at least 60 days before the hearing, including any delay caused by the adjournment of any proceeding that is attributable to the late filing of the application".
  Taken: "as determined by the court" hands the judgment to the court, so the caller says whether the court has so determined (the constructor `s 492.27(ii) ...`); "including any delay caused by the adjournment" is inside that determination and is not separately encoded; one shared constructor serves (a), (b) and (c) because the three subparagraphs say the same thing in the same words (with "filed" in (a) and (c), "served" in (b)). A day in neither period: NOTHING (list not closed).
  Other reading: a day in a period the court has not yet determined is JUST FALSE (the periods are those the court determines); or the days attributable to late filing are excluded whether or not the court says so.
- **F7. s 492.27, "at least 60 days before the hearing"** (lines 11002, 11005, 11008). Taken: a copy in place exactly 60 days before the hearing is "at least 60 days" before it (tested at 60 and 59 days: 2 April and 3 April 2026 against a hearing on 1 June 2026), computed with `Day` as a difference of day counts. Other reading: "clear days", excluding the day of the hearing or of the filing, which would move the boundary by a day. A copy never filed is "not filed at least 60 days before".
- **F8. s 492.27(b), "served ... to the persons referred to"** (line 11005). "if a copy of the application was not served at least 60 days before the hearing ... to the persons referred to in subsection 278.12(5) or 278.21(5)".
  Taken: the caller gives the date a copy had been served on every one of those persons (the date of the last service); a copy not yet served on one of them is not "served ... to the persons", so the limb applies. Other reading: the limb applies only if no copy was served in time on any of them. The persons are named in another part of the Code and are not looked up here.
- **F9. "Subject to section 492.3" and section 492.3's effect** (lines 11001, 11012, 11017, 11019). Sections 492.27, 492.28 and 492.29 each begin "Subject to section 492.3"; section 492.3 says only that "the court shall take into account any frivolous or dilatory action, or any action not made in good faith, taken by the prosecutor, by counsel representing the Attorney General of Canada or by any person acting on behalf of" either, "in determining the days that are not to be taken into account".
  Reading A (taken): section 492.3 is a duty to take the action into account and does not say what days then remain, so when it applies (JUST TRUE) the exclusion's answer is NOTHING (limited by its own wording: "Subject to section 492.3"); when it does not apply, the exclusion stands as written.
  Reading B: the days attributable to the prosecution's frivolous, dilatory or bad-faith action are not excluded (so the bar is JUST FALSE for them). The text does not say so; the section is "for greater certainty".
  Section 492.3 names three kinds of actor (the prosecutor; counsel for the Attorney General of Canada; a person acting for either) and no action by the accused's side: an action by anyone else is NOTHING. The chapeau of the three sections is encoded once (`s 492.27 the court shall not take the day into account, subject to section 492.3`), citing all three.
- **F10. Periods "that begin on the day ... and end on the day ..."** (lines 11013-11015, 11017). Taken: both end days are in the period (the period "begins on the day" and "ends on the day"), so the day of the objection and the day it was finally determined are both excluded; outside the period: JUST FALSE (ruling of 2026-11-05 (a)). Other reading: the last day is outside the period (a period that ends "on" a day ends at its start). A period that has begun and has not ended (no final determination yet): a day before it began is JUST FALSE; a day on or after it began is NOTHING (the end is a day not yet fixed).
  In the paragraphs (b), the period ends on the day the APPLICATION under subsection 37(3) was finally determined, not the objection.
- **F11. "in the case of" against "in the case where"** (lines 11013-11015). Taken, following the ruling's words: paragraphs (a) and (c) of section 492.28 and section 492.29 say "in the case of" or "any application": a scope limit with no "only", so outside it NOTHING (ruling of 2026-11-05 (c)); paragraph (b) says "in the case where": a "where" condition, so when it fails JUST FALSE (ruling of 2026-11-05 (b)). Other reading: all four alike, either way. The difference is the drafter's word, not a difference of meaning the text states.
- **F12. s 492.31(1), "unless it is satisfied"** (`s 492.31(1) the court is barred from ordering a stay of proceedings`; line 11023). "A court shall not order a stay of proceedings as a result of a finding of unreasonable delay unless it is satisfied that no other remedy would be appropriate and just in the circumstances."
  Taken: once the "unless" is met (the court is satisfied), the subsection does not bar the stay: JUST FALSE, which is "this subsection does not bar it", not a grant; whether the court is satisfied is a plain input (the judgment is the court's). Other reading: NOTHING. A stay not "as a result of a finding of unreasonable delay" is NOTHING.
- **F13. Duties and bars whose gate is unmet: the case-by-case sites** (ruling of 2026-11-05, "a duty whose if or where is unmet"). Each site is named in the generated list under "Reading (a)" in "## Marginal readings for a lawyer (ccc19)" below (11 sites of an "if", "where", "when", "in determining", "at the time" or "after", with the function, the quoted words and the other reading). Taken at every site: the duty or bar does not arise on these facts, JUST FALSE. Other reading at every site: NOTHING. The sites are: s 492.25(1) "If ... filed", (2) "at the time the application is heard", (3) "after a decision has been made" and "the victims, if any"; s 492.26(1) "In determining", (2) "If the case involved"; the chapeau of ss 492.27-492.29 "in determining"; s 492.27(b) "if a copy ... was not served"; s 492.28(b) "in the case where"; s 492.3 "in determining ... in relation to"; s 492.31(2) "In determining".
- **F14. Regulative rules carry no WITHIN, and a bare duty not done is not a breach by lateness** ("a bare must not done": a case-by-case question). "as soon as feasible" (s 492.25(1), (3)) is the text's own measure and gives no number of days; (2), s 492.26, s 492.3 and s 492.31(2) give no time at all (s 492.25(2): "at the time the application is heard"). The rules end in `LEST BREACH BY <party> BECAUSE "..."` but, with no deadline, a trace shows the standing obligation and never a breach for lateness (14 of the 35 traces end that way). The prohibitions (`SHANT`: ss 492.23, 492.27-492.29, 492.31(1)) breach when the act is done. Other reading: infer a reasonable-time deadline; not done, because it would invent one.
- **F15. s 492.21 "unreasonable delay"** (line 10963). The standard is "the reasonable time ... in accordance with paragraph 11(b) of the Canadian Charter of Rights and Freedoms", which is outside the sources: the Charter's answer is an input (`MAYBE BOOLEAN`), and a NOTHING from it is carried through (NOTHING-kind: points outside the text). In the seat it is the person's yes/no. No number of months appears anywhere in the Part (finding 2).
- **F16. s 492.25(4), no failure** (line 10983). The subsection says a failure "does not preclude" the court from deciding. Taken: where the prosecutor failed to take reasonable steps to inform the victims of the application, JUST FALSE (the text's no); where there was no such failure the subsection does not speak: NOTHING. A failure to inform the victims of the decision (subsection (3)) is not "the application" failure.
- **F17. Seat stand-ins** (not a fork of the text). (i) For ss 492.27-492.29 the seat calls `s 492.3` with the relation flag "the days being determined are days in relation to an application or objection referred to in ss 492.27 to 492.29" fixed TRUE, because the question is about such an application; the two other facts (a frivolous, dilatory or bad-faith action; who took it) are asked. (ii) The seat calls `s 2 victim` with its fourth input, "the purpose is section 672.5, 722 or 745.63", fixed FALSE, because the purpose is section 492.25. (iii) A date asked of a person who may not have done the thing (filed a copy; had an objection decided) is paired with a yes/no and the date is ignored when the answer is no. (iv) A fixed placeholder is used nowhere else.
- **F18. The defined term "court" in the operative sections** (lines 10962, 10967-11030). Section 492.21 defines "court" for the Part as "a court seized of an application for a determination of unreasonable delay", and every "the court" and "a court" in ss 492.22 to 492.31 is in the Part. Reading A (taken): `s 492.21 court` is a function of its own (the seat asks it as a question), and the operative functions are written for the court that is doing the thing (the gates "the court is determining ...", "an application ... is filed with the court" say so) without re-testing the definition in each. Reading B: every operative function should take `s 492.21 court` = JUST TRUE as a further input. The two differ only for a court that orders a stay as a result of a finding of unreasonable delay without being seized of an application, a case the text does not discuss.


Rulings carried, word for word (copied by script from lines 113-117 of the brief):

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (ccc19)

Hohfeld's correlatives: right and duty; privilege and no-right; power and liability; immunity and disability.
A row marked "(inferred)" names a holder or bearer that the text does not name; the text names only the court, the prosecutor and, as an object of a duty, the victims.
The rule column cites the L4 rule that encodes the relation, stated once as a relation between two parties.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | section | L4 rule |
| --- | --- | --- | --- | --- |
| the Part heading and every heading and marginal note | none | none | -- | -- |
| where the two definitions apply | none (a scope: "in this Part") | none | s 492.21 | `s 492.21 the definitions apply to the provision` |
| "court" and "unreasonable delay" | none (definitions) | none | s 492.21 | `s 492.21 court`, `s 492.21 unreasonable delay` |
| a finding does not take away jurisdiction | power: the court seized with the proceedings (its jurisdiction over the offence, the accused and the offender is kept) | liability: the accused and the offender (they stay subject to it) | s 492.22 | `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction` |
| no stay except in accordance with the Part | immunity: the prosecutor (the proceeding is not stayed as a result of a finding of unreasonable delay except in accordance with the Part) (inferred) | disability: the court (it cannot order such a stay otherwise); and for the accused, no-right to a stay otherwise than in accordance with the Part (inferred) | s 492.23 | `s 492.23 the court is barred from ordering a stay of proceedings`; regulative `s 492.23 the court shall not order a stay of proceedings` |
| the common law continues | none (the text names no party: a saving of rules of law) | none | s 492.24 | `s 492.24 the rule or principle of the common law continues to apply` |
| the prosecutor informs the victims of the filing | claim: the victim (inferred from the heading "Notice to Victims": the text names the victim as the object of the steps) | duty: the prosecutor | s 492.25(1) | `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing`; regulative `s 492.25(1) the duty of the prosecutor to inform the victims of the filing` |
| the court inquires whether notice was given | claim: the victim (inferred); the text names no claimant | duty: the court | s 492.25(2) | `s 492.25(2) the court must inquire of the prosecutor ...`; regulative `s 492.25(2) the duty of the court to inquire of the prosecutor` |
| the prosecutor informs the victims of the decision | claim: the victim (inferred) | duty: the prosecutor | s 492.25(3) | `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision`; regulative `s 492.25(3) the duty of the prosecutor to inform the victims of the decision` |
| a failure to inform does not stop the decision | power: the court (to decide the application despite the prosecutor's failure) | liability: the applicant (the accused) and the prosecutor (they are subject to the decision) | s 492.25(4) | `s 492.25(4) the failure of the prosecutor precludes the court from making a decision on the application` |
| the court considers whether factors made the case complex | claim: the parties to the application, that is the accused who raises delay and the prosecutor (inferred) | duty: the court | s 492.26(1) | `s 492.26(1) the court must consider ...`; regulative `s 492.26(1) the duty of the court to consider case complexity` |
| the court also considers the applications-and-motions factors | claim: the same parties (inferred) | duty: the court | s 492.26(2)(a)-(h) | `s 492.26(2) the court must also consider the factor ...`; regulative `s 492.26(2) the duty of the court to consider the factor` |
| days the court shall not take into account | claim: the prosecutor, that the excluded days are not counted against it (inferred); the accused has no-right that those days count | duty: the court (it shall not take the day into account), subject to s 492.3 | ss 492.27(a)-(c), 492.28(a)-(c), 492.29 | `s 492.27 the court shall not take the day into account, subject to section 492.3`; the limb functions `s 492.27(a)`, `(b)`, `(c)`, `s 492.28(a)`, `(b)`, `(c)`, `s 492.29 the court shall not take the day into account`; regulative `s 492.27 the prohibition on the court taking the day into account` |
| the court takes the prosecution's bad-faith actions into account | claim: the accused (inferred: the person to whom the lost days matter) | duty: the court | s 492.3 | `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith`; regulative `s 492.3 the duty of the court to take the action into account` |
| no stay unless no other remedy would be appropriate and just | immunity: the prosecutor (the proceeding is not stayed unless the court is satisfied) (inferred); the accused has no-right to a stay as of right | disability: the court | s 492.31(1) | `s 492.31(1) the court is barred from ordering a stay of proceedings`; regulative `s 492.31(1) the court shall not order a stay of proceedings` |
| the factors the court takes into account before choosing a remedy | claim: the accused (the prejudice, paragraph (c)), the victim (paragraph (b)), the public and society (paragraphs (d) and (e)) (inferred: the text names factors, not claimants) | duty: the court | s 492.31(2)(a)-(e) | `s 492.31(2) the court must take the factor into account`; regulative `s 492.31(2) the duty of the court to take the factor into account` |

## Marginal readings for a lawyer (ccc19)

The two readings left open for a lawyer, taken as the status quo (the rule of 2026-10-29; assumed, not ruled): (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
The lists below are generated from the `FALSE-kind` and `NOTHING-kind` comments of the layer-1 modules, so that they cover every branch.

The ruling of 2026-11-12 on functions named for a grant or a power, as the brief states it:

> **A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).


### Name-test sweep of 2026-11-12

The class: a layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised/authorized" (whole words, any case), and a function named "it is lawful ...".
The sweep covers every function definition of this part: 41 in the five layer-1 modules, 21 seat questions and 18 local definitions inside the seat questions (80 in all).
Measured 2026-11-16 by `grep -c -i -w` over the 62 top-level names (the lines of the five layer-1 modules and `ccc19-seat.l4` that begin with a backquoted name and contain MEANS, taken with `grep -h '^`[^`]*` MEANS'`), over the 18 indented local names of `ccc19-seat.l4`, and over lines 10957-11031 of the raw text: each of may, permitted, power, powers, entitled, authorised, authorized and lawful has 0 hits in the names and 0 in the raw text.
Positive controls on the same files, so that a zero is not a dead grep: "must" 14, "barred" 11 and "shall" 10 in the top-level names; "shall" 12 and "court" 26 in the raw text range.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |

- Flipped to `NOTHING`: none.
- Kept `JUST FALSE` because the text closes the gate ("only if", "only where", "may not ... unless"): none in the class. The bars and duties of this Part ("is barred", "shall not take the day into account", "must ...") are not named for a grant or a power, so under limit (2) of the ruling they keep their answers; they are not counted.
- Listed with a where/when/upon-kind gate: none. The fork register therefore has no row for this ruling.
- Listed as "entitled": none.
- Outside the sweep, named "it is lawful": 0 (scoped, kept: 0; unscoped and retitled to the scoped form: 0). No assertion was restated for this sweep.

The other reading the ruling would name ("a failed `if` of a grant read as the text's own no") is therefore never needed in this range.


### Generated lists (work/marginal.py reads every `FALSE-kind` and `NOTHING-kind` comment of the layer-1 modules, so the lists cannot omit a branch)

Sites in all: 27 FALSE-kind and 29 NOTHING-kind comments.

#### Reading (a): a failed "if", "where", "when", "in determining", "at the time" or "after" counts as the text's no (JUST FALSE). Other reading: NOTHING, because "if A then B" does not itself say "if not A then not B".
Each of these is also a site of the maintainer's case-by-case question "a duty whose if or where is unmet" (fork F13).

- `ccc19-s492-25.l4:26` in `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing`: "If an application for a finding of unreasonable delay is filed with the court" (gate of a duty or bar)
- `ccc19-s492-25.l4:66` in `s 492.25(2) the court must inquire of the prosecutor whether reasonable steps were taken to inform the victims`: "at the time the application is heard" (gate of a duty or bar)
- `ccc19-s492-25.l4:97` in `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision`: "after a decision has been made on the application" (gate of a duty or bar)
- `ccc19-s492-25.l4:103` in `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision`: "the victims, if any" (gate of a duty or bar)
- `ccc19-s492-26.l4:21` in `s 492.26(1) the court must consider whether any relevant factors contributed or will contribute to making the case complex`: "In determining whether there has been or will be unreasonable delay" (gate of a duty or bar)
- `ccc19-s492-26.l4:73` in `s 492.26(2) the court must also consider the factor in assessing whether the case is complex`: "If the case involved or will involve applications or motions, either before, during or after the trial" (gate of a duty or bar)
- `ccc19-s492-27-to-3.l4:29` in `s 492.27 the court shall not take the day into account, subject to section 492.3`: "in determining whether there has been or will be unreasonable delay" (gate of a duty or bar)
- `ccc19-s492-27-to-3.l4:152` in `s 492.27(b) the day is within a period of paragraph (b)`: "if a copy of the application was not served at least 60 days before the hearing" (gate of a duty or bar)
- `ccc19-s492-27-to-3.l4:290` in `s 492.28(b) the court shall not take the day into account`: "in the case where an objection was made under subsection 37(1) of that Act before a court, person or body other than a superior court and an application was made under subsection 37(3) of that Act in respect of the objection" (gate of a duty or bar)
- `ccc19-s492-27-to-3.l4:351` in `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith`: "in determining the days that are not to be taken into account in relation to applications or objections referred to in sections 492.27 to 492.29" (gate of a duty or bar)
- `ccc19-s492-31.l4:65` in `s 492.31(2) the court must take the factor into account`: "In determining whether a remedy other than a stay of proceedings is appropriate and just" (gate of a duty or bar)

#### Reading (a) again: outside a period or day the text fixes in its own words (ruling of 2026-11-05 (a): JUST FALSE). Other reading: NOTHING.

- `ccc19-s492-27-to-3.l4:34` in `s 492.27 the court shall not take the day into account, subject to section 492.3`: "any day within any of the following periods" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:88` in `s 492.27(a) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "was not filed with the clerk of the court at least 60 days before the hearing" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:95` in `s 492.27(a) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "was not filed with the clerk of the court at least 60 days before the hearing" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:106` in `s 492.27(a) the day is within a period of paragraph (a)`: "if a copy of the application was not filed with the clerk of the court at least 60 days before the hearing referred to in section 276.02" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:187` in `s 492.27(c) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "was not filed with the clerk of the court at least 60 days before the hearing" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:194` in `s 492.27(c) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "was not filed with the clerk of the court at least 60 days before the hearing" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:205` in `s 492.27(c) the day is within a period of paragraph (c)`: "if a copy of the application was not filed with the clerk of the court at least 60 days before the hearing referred to in section 278.31" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:249` in `s 492.28 the day falls within the period that begins on one day and ends on another`: "the period that begins on the day" (period or day-count the text fixes)
- `ccc19-s492-27-to-3.l4:253` in `s 492.28 the day falls within the period that begins on one day and ends on another`: "the period that begins on the day" (period or day-count the text fixes)

#### Flat negatives (ruling N2: they count as the text's no). Other reading: NOTHING.

- `ccc19-s492-21-to-24.l4:79` in `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction`: "does not deprive a court seized with those proceedings of jurisdiction in respect of the offence, the accused or the offender" (flat negative)
- `ccc19-s492-25.l4:135` in `s 492.25(4) the failure of the prosecutor precludes the court from making a decision on the application`: "does not preclude the court from making a decision in respect of the application" (flat negative)

#### "except" and "unless" once met (case by case, forks F2 and F12). Other reading: NOTHING.

- `ccc19-s492-21-to-24.l4:95` in `s 492.23 the court is barred from ordering a stay of proceedings`: "except in accordance with this Part" (exception or unless met)
- `ccc19-s492-21-to-24.l4:126` in `s 492.24 the rule or principle of the common law continues to apply`: "except insofar as they are altered by or are inconsistent with this Part" (exception or unless met)
- `ccc19-s492-31.l4:24` in `s 492.31(1) the court is barred from ordering a stay of proceedings`: "unless it is satisfied that no other remedy would be appropriate and just in the circumstances" (exception or unless met)

#### "means" definitions (no marginal reading: the text closes them in its own word).

- `ccc19-s492-21-to-24.l4:39` in `s 492.21 court`: "means a court seized of an application for a determination of unreasonable delay" (definition)
- `ccc19-s492-21-to-24.l4:54` in `s 492.21 unreasonable delay`: "means a delay that exceeds the reasonable time for a person charged with an offence to be tried" (definition)

#### Reading (b): a prohibition or duty limited by its own wording, the case falling outside the limit (NOTHING). Other reading: JUST FALSE.

- `ccc19-s492-21-to-24.l4:27` in `s 492.21 the definitions apply to the provision`: "apply in this Part" (limited by its own wording)
- `ccc19-s492-21-to-24.l4:76` in `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction`: "A finding of unreasonable delay by a court in respect of any proceedings" (limited by its own wording)
- `ccc19-s492-21-to-24.l4:77` in `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction`: "a court seized with those proceedings" (limited by its own wording)
- `ccc19-s492-21-to-24.l4:78` in `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction`: "in respect of the offence, the accused or the offender" (limited by its own wording)
- `ccc19-s492-21-to-24.l4:94` in `s 492.23 the court is barred from ordering a stay of proceedings`: "as a result of a finding of unreasonable delay" (limited by its own wording)
- `ccc19-s492-21-to-24.l4:125` in `s 492.24 the rule or principle of the common law continues to apply`: "Rules and principles of the common law in respect of a determination of unreasonable delay" (limited by its own wording)
- `ccc19-s492-25.l4:32` in `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing`: "any victim of the offence referred to in the application" (limited by its own wording)
- `ccc19-s492-25.l4:136` in `s 492.25(4) the failure of the prosecutor precludes the court from making a decision on the application`: "The failure of the prosecutor to take reasonable steps to inform the victims, if any, of the application" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:31` in `s 492.27 the court shall not take the day into account, subject to section 492.3`: "any day within any of the following periods" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:38` in `s 492.27 the court shall not take the day into account, subject to section 492.3`: "Subject to section 492.3" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:248` in `s 492.28 the day falls within the period that begins on one day and ends on another`: "ends on the day the objection was finally determined" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:271` in `s 492.28(a) the court shall not take the day into account`: "in the case of an objection made under subsection 37(1) of the Canada Evidence Act before a superior court" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:308` in `s 492.28(c) the court shall not take the day into account`: "in the case of an application made under subsection 38.04(1) or (2) of that Act" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:328` in `s 492.29 the court shall not take the day into account`: "any application under subsection 18.1(4) of the Canadian Security Intelligence Service Act" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:352` in `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith`: "any frivolous or dilatory action, or any action not made in good faith" (limited by its own wording)
- `ccc19-s492-27-to-3.l4:353` in `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith`: "taken by the prosecutor, by counsel representing the Attorney General of Canada or by any person acting on behalf of the prosecutor or the Attorney General of Canada" (limited by its own wording)
- `ccc19-s492-31.l4:23` in `s 492.31(1) the court is barred from ordering a stay of proceedings`: "as a result of a finding of unreasonable delay" (limited by its own wording)

#### NOTHING for other reasons (no other reading needed, or stated in the fork register)

- `ccc19-s492-26.l4:77` in `s 492.26(2) the court must also consider the factor in assessing whether the case is complex`: "the following factors" (list not closed)
- `ccc19-s492-27-to-3.l4:110` in `s 492.27(a) the day is within a period of paragraph (a)`: "any of the following periods" (list not closed)
- `ccc19-s492-27-to-3.l4:156` in `s 492.27(b) the day is within a period of paragraph (b)`: "any of the following periods" (list not closed)
- `ccc19-s492-27-to-3.l4:209` in `s 492.27(c) the day is within a period of paragraph (c)`: "any of the following periods" (list not closed)
- `ccc19-s492-31.l4:66` in `s 492.31(2) the court must take the factor into account`: "the following factors" (list not closed)
- `ccc19-s492-27-to-3.l4:91` in `s 492.27(a) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "clerk of the court" (includes)
- `ccc19-s492-27-to-3.l4:103` in `s 492.27(a) the day is within a period of paragraph (a)`: "clerk of the court" (includes)
- `ccc19-s492-27-to-3.l4:190` in `s 492.27(c) a copy of the application was filed with the clerk of the court at least 60 days before the hearing`: "clerk of the court" (includes)
- `ccc19-s492-27-to-3.l4:202` in `s 492.27(c) the day is within a period of paragraph (c)`: "clerk of the court" (includes)
- `ccc19-s492-21-to-24.l4:50` in `s 492.21 unreasonable delay`: "in accordance with paragraph 11(b) of the Canadian Charter of Rights and Freedoms" (points outside the text)
- `ccc19-s492-25.l4:28` in `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing`: "any victim of the offence referred to in the application" (points outside the text)
- `ccc19-s492-25.l4:99` in `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision`: "the victims, if any" (points outside the text)


### Reading a result: FALSE and NOTHING (ccc19)

Every function answers a `MAYBE BOOLEAN` (the regulative rules answer a `DEONTIC`, and their gate is the decision function's answer).
- `JUST TRUE` is yes, on the text's own words. For a duty ("must") it means the duty arises on these facts. For a bar ("is barred", "shall not take the day into account") it means the bar holds.
- `JUST FALSE` is the text's no, in its own words. In this Part that means: a "means" definition and the case outside it ("court", "unreasonable delay"); a flat negative ("does not deprive", "does not preclude"); an exception met ("except in accordance with this Part", "unless it is satisfied"); a day outside a period the text fixes ("the period that begins on the day ..."); and a duty or bar whose "if", "where", "when", "in determining", "at the time" or "after" is not met (the rule of 2026-10-29, reading (a), listed below). A `JUST FALSE` from a function named for a bar means only that this section does not bar it: it is not a grant, and the Part grants nothing.
- `NOTHING` is "not covered": the text does not say. In this Part that means: a stay on another ground than a finding of unreasonable delay; a day that is in none of the listed periods or that is excluded only "subject to section 492.3"; a factor outside a list that the text does not close; an actor outside the three kinds section 492.3 names; a thing other than the offence, the accused and the offender (section 492.22); and a borrowed term the sources do not settle (the Charter's reasonable time; a section 2 term whose definition says "includes"), which is carried through and never turned into FALSE.
- A caller must never read `NOTHING` as no.
- `REFUSE` is not used on the stable binary: "not covered" is `NOTHING`, asserted with `EQUALS NOTHING`.
- The ruling of 2026-11-12 on functions named for a grant or a power bites on nothing in this Part: see "Name-test sweep of 2026-11-12" under Marginal readings.

## Seams (ccc19)

Taken as INPUTS (the answer of another section, named `s <label>: <what is asked>` and typed as the answering section answers):
- `s 2 clerk of the court: the person with whom the copy was filed is the clerk of the court`, `MAYBE BOOLEAN`, in `s 492.27(a)` and `s 492.27(c)` ("filed with the clerk of the court": lines 11002 and 11008). PLAN.md lists "clerk of the court (4)". The keel's `s 2 clerk of the court` can answer NOTHING (the definition says "includes"), and the NOTHING passes through. The seat calls the keel's function with the person's choice among its three kinds.
- `s 2 victim: there is a victim of the offence referred to in the application` and `s 2 victim: there are victims of the offence`, `MAYBE BOOLEAN`, in `s 492.25(1)` and `s 492.25(3)` (lines 10977 and 10981). PLAN.md's row for this part does not list "victim"; it occurs in ss 492.25 and 492.31(2)(b), and the rule of s 492.25 turns on whether there is one, so it is a seam the plan lacks. The seat calls the keel's `s 2 victim` (with its purpose input fixed FALSE: fork F17).
- `s 492.3: the court must take into account ...`, `MAYBE BOOLEAN`, the chapeau of ss 492.27 to 492.29 ("Subject to section 492.3"): an internal seam inside module D, taken as an input of the chapeau so that the "subject to" is visible; the seat computes it by calling `s 492.3`.
- Facts (R1/R2: the sources do not need to answer them): which application it is (276.01 and 276.02; 278.12, 278.13(1), 278.21, 278.22(1) and persons in 278.12(5) and 278.21(5); 278.3 and 278.31) is stated as a fact (the date of the hearing; the date a copy was filed or served), not looked up. The Canada Evidence Act (ss 37(1), 37(3), 38.01(1) to (4), 38.04(1) and (2)) and the Canadian Security Intelligence Service Act (s 18.1(4)) are outside the sources: that an objection or application was made under them, and when, are facts the caller states.
- The Charter: `the delay exceeds the reasonable time ... under paragraph 11(b) of the Charter, by the Charter`, `MAYBE BOOLEAN` (fork F15).

Offered by PLAN.md and not taken: `s 2 day` (PLAN.md lists "day (21)"). The keel's `s 2 day` means the period between six o'clock in the forenoon and nine o'clock in the afternoon of the same day (a time-of-day function); every "day" in this Part (ss 492.27 to 492.29: "any day within", "the day the objection was made", "60 days") is a calendar day, so no rule turns on it. The 21 occurrences of "day" are ordinary uses.

Seams this part offers and the plan lacks: none is needed by another part's range as far as this agent can see (every section of Part XV.1 is read only by the court that decides a delay application); `s 492.21 court` and `s 492.21 unreasonable delay` are the only terms other parts might ask, and the lead can import them by name.

The brief and PLAN.md differ on one point and the brief governs: PLAN.md section 1 says a part receives `ccc-core.l4` only and takes every section 2 answer as an input, while the brief says the part IMPORTs `ccc-core.l4` and `ccc-definitions.l4`, which sit in the folder. Layer 1 imports `ccc-core` only (so the seams above remain inputs, and the swap at the merge is mechanical); the seat layer imports `ccc-definitions` and calls the keel's two functions.

## Seat questions: audit passes (first pass under the brief; second pass of 2026-11-12)

**Counts.** First pass (name against body, in direction and subject): 21 read, 0 differed in direction or subject.
Second pass of 2026-11-12 (name and `@export` text against the BODY of the function each question calls, and against the tightened definition of a mismatch): 21 read, 10 retitled, 11 read and left.
No layer-1 file changed, no answer changed, and the assertion count stays 78 (the 39 assertions under the ten retitled questions were restated in place with `-- RECONCILED 2026-11-12: was #ASSERT ...`).

**First pass.** Brief: "A seat question's name asks the question its body answers, in the same direction ... Before you finish, list every seat question of yours whose name and body differ in direction or in subject ("must I" against "have I") and fix each."
All 21 questions were read, name against body, by the function each calls and what its `JUST TRUE` says.
None differed in direction or in subject: questions named for a bar say "is the court barred ..."; the questions named for a duty say "must ..."; the negatives say "does ... deprive / preclude" and answer JUST FALSE for no.
The seat never asks "may I" and never negates a layer-1 answer.
That pass read each title against itself, and a title always agrees with itself.

**Second pass.** Each question's name was read against every branch of the body it calls: for each branch that answers `JUST FALSE`, the name was read with that "no" put to it.
A name was retitled only where the tightened test says so: the name asks a different limb or scope than the body answers, or carries a premise, qualifier or consequence the function does not compute or the text does not say, or the polarity or modal is wrong, or the type differs.
The ten that were retitled share one shape: the old name stated as a given a condition that the function tests and answers `JUST FALSE` when it fails ("except in accordance with this Part", "unless it is satisfied", "where my application ... was not filed ... at least 60 days before the hearing", "where the day is within the period", "at the time my application is heard"), so that the "no" read as "not barred even where ...", which the text does not say.
The function's own name does not carry those words, so the exclusion for a status the function's own name also carries does not reach them.
In each case the condition was already an input with its own `@desc`; the new name asks about "this stay" or "this day" under "the rule for" the paragraph's case, and the condition is left to the input.
Where the name states a condition but the answer off that condition is `NOTHING` ("not covered"), where the function's own name carries the same words, or where only "my" against "the" differs (wording), the question was left.
**Assumed, not ruled (one exception kept).** Three groups were left although the name carries a phrase whose failure the function answers `JUST FALSE`: the seven names of ss 492.27-492.29 keep "in deciding unreasonable delay" (the case "the court is not now deciding" answers JUST FALSE), s 492.31(2) keeps "in deciding whether a remedy other than a stay of proceedings is appropriate and just" ("the court is not now deciding that" answers JUST FALSE), and s 492.3 keeps "in determining the days that are not to be taken into account" ("the days are not in relation to ..." answers JUST FALSE). The reason is mine, not the instruction file's: each phrase is the object of the act the section forbids or requires (the regulative act of each is named with the words), so the name cannot ask the question without it. When in doubt the question was left. The other reading, retitle these too, is a call for the lead or a lawyer; all ten retitles come from one table, `RETITLE` in `work/gen-seat.py`, which is the single point to revert or extend.

| question's section | layer-1 function called | JUST TRUE says | second pass |
| --- | --- | --- | --- |
| s 492.21 | `s 492.21 unreasonable delay` | the delay is an unreasonable delay | read, left: the name restates the function's own name; "for the purposes of Part XV.1" is the lead-in "in this Part", and the function answers for the delay itself |
| s 492.21 | `s 492.21 court` | the body is a court for the Part | read, left: the name restates the function's own name; the condition (seized of an application) is the second input, and a "means" definition says no (JUST FALSE) where it fails |
| s 492.22 | `s 492.22 a finding of unreasonable delay deprives the court of jurisdiction` | the finding deprives the court (the text says no: the answer is JUST FALSE) | read, left: the name restates the function's own name; where the finding, the seizing or the matter is not as the text says, the answer is NOTHING, so no JUST FALSE can be misread |
| s 492.23 | `s 492.23 the court is barred from ordering a stay of proceedings` | the court is barred | retitled (listed below) |
| s 492.24 | `s 492.24 the rule or principle of the common law continues to apply` | the rule continues to apply | read, left: the name restates the function's own name; outside the scope the answer is NOTHING, and JUST FALSE is only "altered by or inconsistent with this Part", which the name does not assume |
| s 492.25(1) | `s 492.25(1) the prosecutor must take reasonable steps to inform the victims of the filing` | the prosecutor must | read, left: "of the filing of an application" is carried by the function's own name ("... of the filing") |
| s 492.25(2) | `s 492.25(2) the court must inquire of the prosecutor whether reasonable steps were taken to inform the victims` | the court must | retitled (listed below) |
| s 492.25(3) | `s 492.25(3) the prosecutor must take reasonable steps to inform the victims of the decision` | the prosecutor must | read, left: the function's own name carries "of the decision"; "my application" against "the application" is wording |
| s 492.25(4) | `s 492.25(4) the failure of the prosecutor precludes the court from making a decision on the application` | the failure precludes the court (the text says no: JUST FALSE) | read, left: the function's own name carries "the failure of the prosecutor"; "my" against "the" is wording |
| s 492.26(1) | `s 492.26(1) the court must consider whether any relevant factors contributed or will contribute to making the case complex` | the court must | read, left: the name restates the function's own name; its "in determining" gate is not in the title |
| s 492.26(2) | `s 492.26(2) the court must also consider the factor in assessing whether the case is complex` | the court must | read, left: the name restates the function's own name; its "if the case involved applications or motions" gate is not in the title |
| s 492.27(a) | `s 492.27(a) the court shall not take the day into account` | the court is barred (shall not) | retitled (listed below) |
| s 492.27(b) | `s 492.27(b) the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.27(c) | `s 492.27(c) the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.28(a) | `s 492.28(a) the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.28(b) | `s 492.28(b) the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.28(c) | `s 492.28(c) the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.29 | `s 492.29 the court shall not take the day into account` | the court is barred | retitled (listed below) |
| s 492.3 | `s 492.3: the court must take into account a frivolous or dilatory action or an action not made in good faith` | the court must | read, left (assumed, not ruled): "in determining the days that are not to be taken into account" is the object of the duty (the regulative act is named with it), but the days not being in relation to an application or objection of ss 492.27 to 492.29 answers JUST FALSE, so the off-gate answer is JUST FALSE here; left under "when in doubt, leave" |
| s 492.31(1) | `s 492.31(1) the court is barred from ordering a stay of proceedings` | the court is barred | retitled (listed below) |
| s 492.31(2) | `s 492.31(2) the court must take the factor into account` | the court must | read, left (assumed, not ruled): "in deciding whether a remedy other than a stay of proceedings is appropriate and just" is the object of the duty (the act of its regulative rule carries the same words), but the court not now deciding that answers JUST FALSE, so the off-gate answer is JUST FALSE here; left under "when in doubt, leave" |

**Retitled in the second pass (10), each new name written out exactly; the `@export` text is the same plus a question mark.** The conditions each old name stated stay as inputs with their `@desc`; no layer-1 function and no answer changed.

- s 492.23: the old name stated "except in accordance with Part XV.1", the exception whose being met answers JUST FALSE.
  - was: `Under section 492.23, is the court barred from ordering a stay of proceedings as a result of a finding of unreasonable delay except in accordance with Part XV.1`
  - now: `Under section 492.23, is the court barred from ordering this stay of proceedings as a result of a finding of unreasonable delay`
- s 492.25(2): the old name stated "at the time my application is heard", the gate whose failure answers JUST FALSE (and "my" for "the" is wording).
  - was: `Under section 492.25(2), must the court inquire of the prosecutor whether reasonable steps were taken to inform the victims, at the time my application is heard`
  - now: `Under section 492.25(2), must the court inquire of the prosecutor whether reasonable steps were taken to inform the victims of the filing of the application`
- s 492.27(a): the old name stated "where my application ... was not filed ... at least 60 days before the hearing", the "if" whose failure answers JUST FALSE.
  - was: `Under section 492.27(a), is the court barred from taking a day into account in deciding unreasonable delay, where my application under section 276.01 was not filed with the clerk of the court at least 60 days before the hearing`
  - now: `Under section 492.27(a), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an application made under section 276.01`
- s 492.27(b): the old name stated "where my application ... was not served at least 60 days before the hearing", the "if" whose failure answers JUST FALSE.
  - was: `Under section 492.27(b), is the court barred from taking a day into account in deciding unreasonable delay, where my application under section 278.12 or 278.21 was not served at least 60 days before the hearing`
  - now: `Under section 492.27(b), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an application made under section 278.12 or 278.21`
- s 492.27(c): the old name stated "where my application ... was not filed ... at least 60 days before the hearing", the "if" whose failure answers JUST FALSE.
  - was: `Under section 492.27(c), is the court barred from taking a day into account in deciding unreasonable delay, where my application under section 278.3 was not filed with the clerk of the court at least 60 days before the hearing`
  - now: `Under section 492.27(c), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an application made under section 278.3`
- s 492.28(a): the old name stated "where the day is within the period", which the function tests and answers JUST FALSE for a day outside it.
  - was: `Under section 492.28(a), is the court barred from taking a day into account in deciding unreasonable delay, where the day is within the period of an objection under subsection 37(1) of the Canada Evidence Act before a superior court`
  - now: `Under section 492.28(a), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an objection made under subsection 37(1) of the Canada Evidence Act before a superior court`
- s 492.28(b): the old name stated "where the day is within the period", which the function tests and answers JUST FALSE for a day outside it (and JUST FALSE where the objection or application is not as stated).
  - was: `Under section 492.28(b), is the court barred from taking a day into account in deciding unreasonable delay, where the day is within the period of an objection made before a court, person or body other than a superior court and an application under subsection 37(3) of the Canada Evidence Act`
  - now: `Under section 492.28(b), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an objection made under subsection 37(1) of the Canada Evidence Act before a court, person or body other than a superior court, with an application under subsection 37(3) in respect of it`
- s 492.28(c): the old name stated "where the day is within the period", which the function tests and answers JUST FALSE for a day outside it.
  - was: `Under section 492.28(c), is the court barred from taking a day into account in deciding unreasonable delay, where the day is within the period of an application under subsection 38.04(1) or (2) of the Canada Evidence Act`
  - now: `Under section 492.28(c), is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an application made under subsection 38.04(1) or (2) of the Canada Evidence Act`
- s 492.29: the old name stated "where the day is within the period", which the function tests and answers JUST FALSE for a day outside it.
  - was: `Under section 492.29, is the court barred from taking a day into account in deciding unreasonable delay, where the day is within the period of an application under subsection 18.1(4) of the Canadian Security Intelligence Service Act`
  - now: `Under section 492.29, is the court barred from taking this day into account in deciding unreasonable delay, under the rule for an application made under subsection 18.1(4) of the Canadian Security Intelligence Service Act`
- s 492.31(1): the old name stated "unless it is satisfied that no other remedy would be appropriate and just", the "unless" whose being met answers JUST FALSE.
  - was: `Under section 492.31(1), is the court barred from ordering a stay of proceedings as a result of a finding of unreasonable delay unless it is satisfied that no other remedy would be appropriate and just`
  - now: `Under section 492.31(1), is the court barred from ordering this stay of proceedings as a result of a finding of unreasonable delay`

## Findings

### What the text turns out to say (numbered)

1. Part XV.1 limits and conditions; it grants nothing. No provision says who may apply for a finding of unreasonable delay, and no provision gives a court the power to order a stay or any other remedy: ss 492.23 and 492.31(1) only bar a stay "except in accordance with this Part" and "unless it is satisfied that no other remedy would be appropriate and just". The power sits outside this text (s 492.24, "Rules and principles of the common law ... continue to apply", points to it). "may" and "entitled" occur 0 times in lines 10957-11031, which is why no function here is named for a grant.
2. No number of months or days of delay appears in the Part: "unreasonable delay" is "a delay that exceeds the reasonable time ... in accordance with paragraph 11(b)" of the Charter, so every ceiling is outside the text (0 hits for "month" in the 75 lines). The only number in the Part is "60 days" (ss 492.27(a), (b), (c)).
3. The 60 days run backward from the hearing and apply to three applications by their own verbs: a copy "filed with the clerk of the court" (276.01 and 278.3) or "served ... to the persons referred to" (278.12 and 278.21). The late-filing exclusions therefore bite on the accused: the applications they cover are made "by or on behalf of the accused" (s 276.01(1), line 5173; s 278.3(1), line 5541) or by "An accused who seeks production" (s 278.12(1), line 5316; s 278.21(1), line 5426). Part XV.1 itself does not say who files; the seat's questions are written so that the accused can ask them.
4. "Subject to section 492.3" (ss 492.27 to 492.29) points at a section that says only that the court "shall take into account" the prosecution's frivolous, dilatory or bad-faith action; it does not say the exclusion then falls away (fork F9). Section 492.3 names no action by the accused's side.
5. "(ii) any other period, as determined by the court" (ss 492.27(a)(ii), (b)(ii), (c)(ii)) leaves the periods to the court; only (i), the cumulative days it took to hear the application, is fixed by the text.
6. Paragraph (d) of s 492.26(2) is printed without a closing semicolon (the text has "...required by any of the applications or motions" at the end of line 10993 and the next line begins "(e)"); quoted as it is.
7. Sections 492.28(a) and (c) and 492.29 say "in the case of"/"any application" and 492.28(b) says "in the case where" (fork F11).
8. Subsection 492.25(4) is about the failure to inform the victims "of the application" only; failing to inform them of the decision (subsection (3)) is not covered by it (fork F16).
9. The defined term "court" (s 492.21: "a court seized of an application for a determination of unreasonable delay") governs every "court" in the Part, but the operative sections do not all repeat the seizure (fork F18).
10. Part XV.1 has 11 sections (492.21 to 492.31) and no repealed or blank provision; the section numbers sort in the Code's order as decimals (492.3 between 492.29 and 492.31), which is what `s 492.21 the definitions apply to the provision` tests (492.2, 493 and 515 are outside the Part).

### What the stable binary does not accept

Measured on 2026-11-13 on 1.6.110 (main, e51181d) and 1.6.109 (main, 4c887e0). This part met no construct that either build rejected: what the brief names (`REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH`, a section `GIVEN`, `TYPICALLY`, `YMD`) was not used, and nothing was probed against the brief's list.
- Regulative values: a `DEONTIC` result cannot be compared in an `#ASSERT` (the skill's page 5.2 says so; this part did not probe it). So every duty and prohibition is exercised with `#TRACE` (35 traces: 18 FULFILLED, 14 the obligation standing, 3 BREACHED; the results are identical on both builds, compared by `work/trace-table.py`) and each duty is also a decision function with assertions, as the brief requires.
- `check.sh` counts assertions and errors and does not see a `#TRACE` outcome; the two builds' trace results were therefore compared by hand (they agree).
- `WAIT UNTIL` is spelled `WAITUNTIL` and was used in the form `(WAITUNTIL n)`; it works on both builds.
- `PARTY the court SHANT <act> accordance PROVIDED NOT (accordance)` (a wildcard bound to the act's field and a guard) works on both builds: an act whose guard is false does not match, and the prohibition stays standing (the residual prints as `MUST NOT`); `MUST <act> considered PROVIDED considered EQUALS factor` works the same way for a duty on a particular factor.
- `@export` with an enumerated type and a `DATE` input was checked with `l4 check` and `l4 run` only; the seat's inputs are values (yes/no, a date, a choice from a list; no `MAYBE` input), but the layer was not deployed to `jl4-service` or Legalese Cloud, so its JSON spelling at the boundary is not tested.
- Not probed and therefore not claimed: `NOT a AND b` without brackets (every `NOT` here is bracketed), `#EVALTRACE`.

### Regulative rules exercised (35 `#TRACE` directives; results identical on 1.6.110 and 1.6.109)

Each result below matched the expectation written in the comment above the trace before the run (a standing obligation where no event is due, FULFILLED where the duty was performed or nothing was owed, BREACHED where a prohibited act was done).

The complete `l4 run` output of each of the five tests modules was compared byte for byte between 1.6.110 and 1.6.109 (`cmp`): identical for all five (13,464; 9,899; 8,578; 37,111 and 10,138 bytes), so every trace result, not only its outcome class, reads the same on both builds.

- `ccc19-tests-s492-21-to-24.l4`: 3 traces: 1 BREACHED, 2 standing
- `ccc19-tests-s492-25.l4`: 10 traces: 7 FULFILLED, 3 standing
- `ccc19-tests-s492-26.l4`: 7 traces: 4 FULFILLED, 3 standing
- `ccc19-tests-s492-27-to-3.l4`: 8 traces: 1 BREACHED, 5 FULFILLED, 2 standing
- `ccc19-tests-s492-31.l4`: 7 traces: 1 BREACHED, 2 FULFILLED, 4 standing

### Limits of this work

- Expected values were written by hand from the text before each run, by the same agent that wrote the functions; the independent test pass was not run.
- The tests exercise each branch and each boundary of each function (60 and 59 days; the first and last day of a period and the days either side), and every seat question has cases on each answer the section can give. They do not test how another part composes these functions.
- The `@ref` locators and quotations are checked by `srcrefs.py check --refs` and `--strict`; the FALSE-kind and NOTHING-kind quotations by `work/verify-kinds.py` (every quoted fragment occurs in lines 10957-11031 of the text). Neither checks that an encoding means what the text says.
- The seat layer was not deployed.

## Open questions for a domain expert

- Is a stay not "as a result of a finding of unreasonable delay" (abuse of process, say) outside Part XV.1 altogether, as encoded (NOTHING), or does s 492.23 reach it?
- Does "Subject to section 492.3" put the prosecution's bad-faith days back into the count (reading B of fork F9), or only oblige the court to weigh them?
- Are the periods of s 492.28 inclusive of the day the objection was finally determined (fork F10)?
- Is "at least 60 days before the hearing" a count of clear days (fork F7)?

## What `check.sh` prints

Run as `L4=<1.6.110> L4_MAIN=<1.6.109> ./check.sh` (target main: every module is also run with the second stable build and the four counts are compared); the last line, `exit=0`, is the exit status of that run. The same run before the second seat audit pass printed the same TOTAL (15 modules, 239 satisfied, 0 failed, 0 errors, 0 refused, every module `same`).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc19-cases-seat.l4                            0        78       0        0         0 |      0        78       0        0  same
ccc19-s492-21-to-24.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-25.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-26.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-27-to-3.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc19-s492-31.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc19-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc19-tests-s492-21-to-24.l4                   0        30       0        0         0 |      0        30       0        0  same
ccc19-tests-s492-25.l4                         0        14       0        0         0 |      0        14       0        0  same
ccc19-tests-s492-26.l4                         0        13       0        0         0 |      0        13       0        0  same
ccc19-tests-s492-27-to-3.l4                    0        92       0        0         0 |      0        92       0        0  same
ccc19-tests-s492-31.l4                         0        12       0        0         0 |      0        12       0        0  same
TOTAL (15 modules)                             0       239       0        0           |      0       239       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit=0
```

`srcrefs.py` over every `ccc19-*.l4` file:

```
$ python3 -I srcrefs.py check --refs R.S.C.-1985-c.-C-46.txt ccc19-*.l4
srcrefs check: 43 src: lines, 21 runs, 56 locators, 0 problems
exit=0
$ python3 -I srcrefs.py check --strict R.S.C.-1985-c.-C-46.txt ccc19-*.l4
srcrefs check: 43 src: lines, 21 runs, 56 locators, 0 problems
exit=0
```

## Files

All under `encodings/legalese-sonnet-5.5/`: `ccc19-s492-21-to-24.l4`, `ccc19-s492-25.l4`, `ccc19-s492-26.l4`, `ccc19-s492-27-to-3.l4`, `ccc19-s492-31.l4`; `ccc19-tests-s492-21-to-24.l4`, `ccc19-tests-s492-25.l4`, `ccc19-tests-s492-26.l4`, `ccc19-tests-s492-27-to-3.l4`, `ccc19-tests-s492-31.l4`; `ccc19-seat.l4`, `ccc19-cases-seat.l4`; `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`. The keel's files and `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` are as supplied. The generators (`work/gen.py`, `gen-seat.py`, `gen-cases.py`, `coverage.py`, `marginal.py`, `verify-kinds.py`, `trace-table.py`, `traces.py`, `notes.py`) and the templates are under `DEPOSIT/../work/` and are not shipped.
