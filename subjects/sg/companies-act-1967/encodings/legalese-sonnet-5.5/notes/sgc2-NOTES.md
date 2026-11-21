# NOTES (sgc2): Companies Act 1967 (Singapore), Part 6 Division 2 (sections 205 to 209B) and the Thirteenth Schedule

Part agent `sgc2`, model Sonnet 5.5, wave 1 of the Companies Act encoding.
My ranges are lines 19069-20182 and 29013-29310 of `inputs/CoA1967.txt`: Part 6 Division 2 (ss 205, 205AA to 205AF, 205A to 205D, 206, 207, 208, 208A, 209, 209A, 209B) and the Thirteenth Schedule (paragraphs 1 to 14).
Where `inputs/PLAN.md` and the brief (`BRIEF.md`) differ, the brief governs.
`PROGRESS.md` records no point of my ranges where the two differed in a way that changed an answer.

## Edition encoded

This is an encoding of the Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, which carries the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read; the encoding is of that text only.
The text is `inputs/CoA1967.txt`, a rendering: a PDF turned into plain text.
It is not the official text (SSO's terms say so), and nothing in this folder is claimed to be "verified against the official text".
Line numbers everywhere are of that file as it is.
Page furniture (the version line, the running head, the page number) and amendment marks (`[36/2014]`, `[Act 24 of 2025 wef 06/05/2026]`) are not text and are never quoted as a rule.
Nothing here says that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.

## The seat

The seat is an individual who is, or is about to become, a director, a company secretary or a member of a company, or who deals with one, an auditor included.
There is no seat for the Registrar, the Minister or the Court: their powers are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person (for example, "may the Registrar make the appointment on the application of a member").

## Files

- Layer 1 (the law, objectively): `sgc2-common.l4`, `sgc2-s205-appointment.l4` (s 205), `sgc2-s205aa-resignation.l4` (ss 205AA to 205AF), `sgc2-s205a-exemption.l4` (ss 205A to 205D), `sgc2-s206-208a-duties.l4` (ss 206 to 208A), `sgc2-s209-interpretation.l4` (ss 209, 209A; 209B is shown repealed and has no function), `sgc2-sch13-small.l4` (the Thirteenth Schedule).
- Tests, written from the text and not from the code's output: `sgc2-tests-s205.l4`, `sgc2-tests-s205aa.l4`, `sgc2-tests-s205a.l4`, `sgc2-tests-s206-208a.l4`, `sgc2-tests-s209.l4`, `sgc2-tests-sch13.l4`.
- Layer 2: `sgc2-seat.l4` (66 questions in six groups, in the text's order) and `sgc2-cases-seat.l4` (187 assertions).
- `NOTES.md` (this file), `PROGRESS.md`. There is no `NEEDS-CORE.md`: no type or constructor was missing from the core.
- The layer-1 modules were written as templates (`work/src/*.l4t`, outside the deposit) and expanded by `work/expand.py`, which copies the quoted lines mechanically from the text and writes each `@ref` locator.
  The expanded `.l4` files are the deliverable; `python3 -I srcrefs.py check --refs ../../../inputs/CoA1967.txt <my files>`, with and without `--strict`, reports 0 problems (911 `src:` lines, 147 runs, 216 locators).

## Coverage (sgc2)

The table is generated from the text by `work/coverage.py` (with `work/units.py`, which finds each unit's first line from the labels at the start of the lines, and `work/l4map.py`, which reads each `@ref ... (src:a-b)` locator and the fork tags out of the layer-1 files).
A row runs from its first line to the line before the next row's first line, so page furniture and amendment marks fall in the row of the provision they sit in, and a blank line belongs to no row.
The script checks that **every non-blank line of the two ranges falls in exactly one row**: 992 (795 in lines 19069-20182, 197 in lines 29013-29310) non-blank lines, 0 missing, 0 in two rows.

How to read the table:

- **Unit** is the provision as the text labels it (`s 205(5)(a)`, `Sch 13 para 3(a)(ii)(A)`).
  A section whose text opens with `(1)` has no row of its own: its heading is a row (inert, reason 1) and its subsections are rows.
  A section with no subsections (205AE, 205D, 209A, 209B) is one row.
  The text prints the label `(aa)` twice in s 207(2); the two paragraphs are two rows, "first of two" and "second of two".
  A defined term that has a line of its own is a row (`DEF:` rows, the Schedule's para 12(b)(ii)(A) and (B), para 12(c)); four terms defined inside a subsection ("accounting transaction", "small company", "small group", "a serious offence involving fraud or dishonesty") also have a row, shown indented under their subsection, which takes its disposition from the subsection.
  A nested item `(i)`, `(A)` is a row under its paragraph; the Schedule's criteria are those items, so each threshold has its own row.
- **Disposition** is exactly one of `encoded`, `inert (reason 1)`, `fork`, `repealed or blank in this text`.
  `fork` means the answer rests on a fork-register entry of kind "reading" or "site by site" (see `## Fork register (sgc2)`); the **Fork entries** column names it, and the L4 name column names the rule that encodes the reading taken.
  There is no `out-of-scope` row and no `deferred` row; the only `inert` rows are headings (reason 1).
- **L4 name(s)** are the layer-1 functions whose `@ref` locator overlaps the row's lines, read from the files by script, not typed.
  "as s X" means the same functions as the row above it in the text's nesting; the paragraph's rule is the subsection's rule.
- **Seat questions** call these functions by the same names; the seat's questions are listed in `## The seat layer`.

**Counts**

| Disposition | Rows (one per unit) | of which in-line defined-term rows |
| --- | --- | --- |
| encoded | 97 | 3 |
| fork | 177 | 1 |
| inert (reason 1: headings) | 19 | 0 |
| repealed or blank in this text | 5 | 0 |
| **total** | **298** | **4** |

Rows in all: 298 primary rows plus 4 in-line term rows = **302**.
Every `inert` row is a heading (reason 1); there is no `inert` row of reason 2 or 3, no `out-of-scope` row and no `deferred` row.

**Audit** (the instrument is `work/coverage.py`; the figures are what it printed on the last run).

- Units found by the first pass (labels at the start of lines, no nested items, no in-line terms): **261** starts, which become **247** rows once the 14 sections whose first line is also their subsection (1) are not counted twice.
- What the audit added: **51** nested items `(i)`, `(ii)`, `(iii)`, `(A)`, `(B)`, `(C)` (the Schedule's criteria and the items of ss 205B(4)(d) and 207(2)) and **4** in-line defined terms, so the table has **302** rows after the audit (before: 247).
- Rows by kind after the audit: 1 division heading, 17 section heading, 1 schedule heading, 4 section, 86 subsection, 80 paragraph, 51 item, 13 definition, 14 schedule paragraph, 31 schedule sub-paragraph; and 4 in-line term rows.
- Units the script cannot see, checked by eye: the text has no table in these ranges (a search for "table" finds none); the text defines 20 terms, 13 on lines of their own (2 in s 205AA(4), 11 in s 209A), 3 in Schedule para 12 (`(b)(ii)(A)`, `(b)(ii)(B)`, `(c)`) and 4 inside a subsection, and each has a row; the five deleted or repealed provisions are rows of their own.

| Unit | Lines | Kind | Disposition | Fork entries | L4 name(s) |
| --- | --- | --- | --- | --- | --- |
| Heading of Part 6 Division 2 | 19069 | division heading | inert (reason 1) |  | a heading: not operative |
| Heading of s 205 | 19071 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205(1) | 19073-19079 | subsection | fork | F-D1, F-P2, F-T1 | `s 205(1) the last day for the directors to appoint the first auditor`; `s 205(1) the directors are in default of the duty to appoint the first auditor`; `s 205(1) the directors must appoint the first auditor`; `s 205(1) the auditor appointed by the directors holds office` |
| s 205(2) | 19081-19087 | subsection | fork | F-D1, F-T1 | `s 205(2) the company is in default of the duty to appoint an auditor at the annual general meeting`; `s 205(2) the company must appoint an auditor at each annual general meeting`; `s 205(2) the auditor appointed at the annual general meeting holds office` |
| s 205(3) | 19089-19095 | subsection | fork | F-G1 | `s 205(3) the directors may appoint the accounting entity to fill the casual vacancy`; `s 205(3) the surviving or continuing auditor may act` |
| s 205(4) | 19097-19099 | subsection | encoded |  | `s 205(4) the auditor may be removed from office by the resolution` |
| s 205(5) | 19101-19102 | subsection | fork | F-D1 | `s 205(5)(a) the company is in default of the duty to send a copy of the notice`; `s 205(5)(a) the company must send a copy of the notice of the removal resolution` |
| s 205(5)(a) | 19104-19105 | paragraph | fork | F-D1 | as s 205(5) |
| s 205(5)(b) | 19107-19116 | paragraph | fork | F-G1 | `s 205(5)(b) the auditor may make representations and have a copy sent to every member` |
| s 205(6) | 19118-19122 | subsection | fork | F-G1, F-R1 | `s 205(6) the company is in default of the duty to send a copy of the representations`; `s 205(6) the company must send a copy of the representations`; `s 205(6) the auditor may require that the representations be read out at the meeting` |
| s 205(7) | 19124-19125 | subsection | fork | F-G1, F-V1, F-W1 | `s 205(7)(a) the company may immediately appoint another accounting entity as auditor` |
| s 205(7)(a) | 19127-19132 | paragraph | fork | F-G1, F-V1, F-W1 | as s 205(7) |
| s 205(7)(b) | 19134-19142 | paragraph | fork | F-G1, F-W1 | `s 205(7)(b) the company may appoint another accounting entity as auditor at the adjourned meeting` |
| s 205(8) | 19144-19149 | subsection | fork | F-G1 | `s 205(8) the company is in default of the duty to give written notice of the removal to the Registrar`; `s 205(8) the company must give written notice of the removal to the Registrar`; `s 205(8) the Registrar may appoint an auditor of the company` |
| s 205(9) | 19151-19153 | subsection | fork | F-T1 | `s 205(9) the auditor appointed under subsection (7) or (8) holds office` |
| s 205(10) | 19155-19157 | subsection | fork | F-G1 | `s 205(10) the Registrar may make the appointment on the application of a member` |
| s 205(11) | 19159-19170 | subsection | fork | F-G1 | `s 205(11) the accounting entity is capable of being appointed auditor at the annual general meeting` |
| s 205(12) | 19172-19181 | subsection | fork | F-D1, F-P2 | `s 205(12) the last day for the company to send a copy of the notice of nomination`; `s 205(12) the company is in default of the duty to send a copy of the notice of nomination`; `s 205(12) the company must send a copy of the notice of nomination` |
| s 205(12A) | 19183-19188 | subsection | encoded |  | `s 205(12A) the day that stands for the date of the annual general meeting` |
| s 205(12A)(a) | 19190-19191 | paragraph | encoded |  | as s 205(12A) |
| s 205(12A)(b) | 19193-19199 | paragraph | encoded |  | as s 205(12A) |
| s 205(13) | 19201-19212 | subsection | encoded |  | `s 205(13) subsection (11) does not apply in relation to the accounting entity`; `s 205(13) the company is deemed to have complied with subsection (12)` |
| s 205(14) | 19214-19217 | subsection | repealed or blank in this text |  | the text shows [Deleted by Act 36 of 2014] |
| s 205(15) | 19219 | subsection | repealed or blank in this text |  | the text shows [Deleted by Act 36 of 2014] |
| s 205(16) | 19221 | subsection | encoded |  | `s 205(16) the fees and expenses of the auditor are fixed as the subsection requires` |
| s 205(16)(a) | 19223-19227 | paragraph | encoded |  | as s 205(16) |
| s 205(16)(b) | 19229-19236 | paragraph | encoded |  | as s 205(16) |
| s 205(17) | 19238-19241 | subsection | fork | F-E1 | `s 205(17) the person is guilty of the offence`; `s 205(17) the most the person may be fined on conviction` |
| Heading of s 205AA | 19243 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AA(1) | 19245-19251 | subsection | fork | F-G1, F-X1 | `s 205AA(1) the auditor may resign by giving the company a notice of resignation in writing` |
| s 205AA(2) | 19253-19254 | subsection | encoded |  | `s 205AA(2) the day on which the auditor's term of office expires` |
| s 205AA(2)(a) | 19256-19257 | paragraph | encoded |  | as s 205AA(2) |
| s 205AA(2)(b) | 19259-19262 | paragraph | encoded |  | as s 205AA(2) |
| s 205AA(3) | 19264-19273 | subsection | fork | F-D1, F-P2, F-P3 | `s 205AA(3) the last day for the company to lodge the notification`; `s 205AA(3) the company is in default of the duty to lodge the notification`; `s 205AA(3) the company must lodge the notification with the Registrar` |
| s 205AA(4) | 19275 | subsection | encoded |  | `s 205AA(4) "non-public interest company" the company is a non-public interest company` |
| Defined term non‑public interest company | 19277-19278 | definition | encoded |  | `s 205AA(4) "non-public interest company" the company is a non-public interest company` |
| Defined term public interest company | 19280-19285 | definition | encoded |  | `s 205AA(4) "public interest company" the company is a public interest company` |
| Heading of s 205AB | 19287-19288 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AB(1) | 19290-19293 | subsection | fork | F-G1 | `s 205AB(1) the auditor may resign by giving the company a notice of resignation in writing` |
| s 205AB(1)(a) | 19295-19301 | paragraph | fork | F-G1 | as s 205AB(1) |
| s 205AB(1)(b) | 19303-19305 | paragraph | fork | F-G1 | as s 205AB(1) |
| s 205AB(2) | 19307-19311 | subsection | encoded |  | `s 205AB(2) the auditor and the company are to be notified whether the Registrar consents`; `s 205AB(2) the Registrar must notify the auditor and the company whether it consents` |
| s 205AB(3) | 19313-19315 | subsection | encoded |  | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings` |
| s 205AB(3)(a) | 19317-19321 | paragraph | encoded |  | as s 205AB(3) |
| s 205AB(3)(b) | 19323-19330 | paragraph | encoded |  | `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor`; `s 205AB(3) the Registrar's certificate is conclusive evidence that the statement was made in the application or the answer` |
| s 205AB(4) | 19332-19336 | subsection | encoded |  | `s 205AB(4) the statement may be used in the proceedings` |
| s 205AB(5) | 19338-19339 | subsection | encoded |  | `s 205AB(5) the day the resignation takes effect` |
| s 205AB(5)(a) | 19341-19342 | paragraph | encoded |  | as s 205AB(5) |
| s 205AB(5)(b) | 19344-19346 | paragraph | encoded |  | as s 205AB(5) |
| s 205AB(5)(c) | 19348-19352 | paragraph | encoded |  | as s 205AB(5) |
| Heading of s 205AC | 19354-19355 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AC(1) | 19357-19365 | subsection | fork | F-D1, F-P2 | `s 205AC(1) the last day for the company to send a copy of the written statement to every member`; `s 205AC(1) the company is in default of the duty to send a copy of the written statement to every member`; `s 205AC(1) the company must send a copy of the written statement to every member` |
| s 205AC(2) | 19367-19379 | subsection | fork | F-P3 | `s 205AC(2) copies of the written statement need not be sent out` |
| s 205AC(3) | 19381-19382 | subsection | encoded |  | `s 205AC(3) the applicant is in default of the duty to give notice of the application`; `s 205AC(3)(a) the company that applies must give notice of the application to the auditor`; `s 205AC(3)(b) any other person who applies must give notice of the application to the company and the auditor` |
| s 205AC(3)(a) | 19384-19385 | paragraph | encoded |  | as s 205AC(3) |
| s 205AC(3)(b) | 19387-19390 | paragraph | encoded |  | as s 205AC(3) |
| s 205AC(4) | 19392-19397 | subsection | fork | F-E1 | `s 205AC(4) the person is guilty of the offence`; `s 205AC(4) the most the person may be fined on conviction` |
| Heading of s 205AD | 19399 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AD(1) | 19401-19405 | subsection | encoded |  | `s 205AD(1) section 205AD applies` |
| s 205AD(2) | 19407-19409 | subsection | fork | F-G1 | `s 205AD(2)(a) the Court is required to direct that copies of the written statement are not to be sent`; `s 205AD(2)(b) the Court may order the auditor to pay the applicant's costs in whole or in part` |
| s 205AD(2)(a) | 19411-19412 | paragraph | fork | F-G1 | as s 205AD(2) |
| s 205AD(2)(b) | 19414-19418 | paragraph | fork | F-G1 | as s 205AD(2) |
| s 205AD(3) | 19420-19423 | subsection | fork | F-D1, F-P2, F-P3 | `s 205AD(3) the last day for the company to send the notice`; `s 205AD(3) the company is in default of the duty to send a notice setting out the effect of the directions`; `s 205AD(3) the company must send a notice setting out the effect of the directions` |
| s 205AD(3)(a) | 19425-19428 | paragraph | fork | F-D1, F-P2, F-P3 | as s 205AD(3) |
| s 205AD(3)(b) | 19430-19433 | paragraph | fork | F-D1, F-P2, F-P3 | as s 205AD(3) |
| s 205AD(4) | 19435-19438 | subsection | fork | F-D1, F-P2, F-P3 | `s 205AD(4) the last day for the company to give notice and send the copies`; `s 205AD(4) the company is in default of the duty to give notice of the decision and send the copies`; `s 205AD(4) the company must give notice of the decision and send the copies` |
| s 205AD(4)(a) | 19440-19441 | paragraph | fork | F-D1, F-P2, F-P3 | as s 205AD(4) |
| s 205AD(4)(b) | 19443-19446 | paragraph | fork | F-D1, F-P2, F-P3 | as s 205AD(4) |
| s 205AD(5) | 19448-19453 | subsection | fork | F-E1 | `s 205AD(5) the person is guilty of the offence`; `s 205AD(5) the most the person may be fined on conviction` |
| Heading of s 205AE | 19455 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AE | 19457-19467 | section | encoded |  | `s 205AE the person has the privilege against an action for defamation for the publication` |
| Heading of s 205AF | 19469 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205AF(1) | 19471 | subsection | fork | F-D1, F-P2 | `s 205AF(1)(c) the last day for the directors to call the general meeting`; `s 205AF(1)(c) the directors are in default of the duty to call a general meeting`; `s 205AF(1)(c) the directors must call a general meeting to appoint an auditor in place` |
| s 205AF(1)(a) | 19473-19475 | paragraph | fork | F-D1, F-P2 | as s 205AF(1) |
| s 205AF(1)(b) | 19477-19487 | paragraph | fork | F-D1, F-P2 | as s 205AF(1) |
| s 205AF(1)(c) | 19489-19493 | paragraph | fork | F-D1, F-P2 | as s 205AF(1) |
| s 205AF(1)(d) | 19495-19499 | paragraph | fork | F-D1, F-P2, F-P3 | `s 205AF(1)(d) the last day for the directors to lodge the notification`; `s 205AF(1)(d) the directors are in default of the duty to lodge a notification of the appointment`; `s 205AF(1)(d) the directors must lodge a notification of the appointment` |
| s 205AF(2) | 19501-19506 | subsection | fork | F-G1 | `s 205AF(2) the Registrar may make the appointment on the application of a member` |
| s 205AF(3) | 19508-19512 | subsection | encoded |  | `s 205AF(3) subsections (1) and (2) do not apply` |
| s 205AF(4) | 19514-19518 | subsection | encoded |  | `s 205AF(4) the auditor appointed under subsection (1) or (2) holds office` |
| s 205AF(5) | 19520-19525 | subsection | fork | F-E1 | `s 205AF(5) the person is guilty of the offence`; `s 205AF(5) the most the person may be fined on conviction` |
| Heading of s 205A | 19527 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205A(1) | 19529-19534 | subsection | encoded |  | `s 205A(1) the company and its directors are exempt from section 205(1) or (2)` |
| s 205A(2) | 19536-19539 | subsection | fork | F-D1, F-P2, F-P4 | `s 205A(2) the last day for the company to appoint an auditor`; `s 205A(2) the company is in default of the duty to appoint an auditor`; `s 205A(2) the company must appoint an auditor before the next annual general meeting`; `s 205A(2) the auditors appointed hold office` |
| s 205A(3) | 19541-19544 | subsection | fork | F-E1 | `s 205A(3) the person is guilty of the offence`; `s 205A(3) the most the person may be fined on conviction` |
| Heading of s 205B | 19546 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205B(1) | 19548 | subsection | encoded |  | `s 205B(1) the company is exempt from audit requirements` |
| s 205B(1)(a) | 19550 | paragraph | encoded |  | as s 205B(1) |
| s 205B(1)(b) | 19552-19553 | paragraph | encoded |  | as s 205B(1) |
| s 205B(2) | 19555-19557 | subsection | encoded |  | `s 205B(2) the company is dormant during the period`; `s 205B(2) the company ceases to be dormant on the transaction` |
| s 205B(3) | 19559-19560 | subsection | encoded |  | `s 205B(3) helper: the transaction arises from a listed matter`; `s 205B(3) the transaction is to be disregarded` |
| s 205B(3)(a) | 19562-19564 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(b) | 19566-19567 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(c) | 19569 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(d) | 19571-19572 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(e) | 19574-19575 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(f) | 19577-19582 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(fa) | 19584-19585 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(fb) | 19587-19588 | paragraph | encoded |  | as s 205B(3) |
| s 205B(3)(g) | 19590-19592 | paragraph | encoded |  | as s 205B(3) |
| s 205B(4) | 19594-19595 | subsection | fork | F-W1 | `s 205B(4)(a) the copies of the financial statements to be sent under section 203 need not be audited` |
| s 205B(4)(a) | 19597-19599 | paragraph | fork | F-W1 | as s 205B(4) |
| s 205B(4)(b) | 19601-19602 | paragraph | fork | F-W1 | `s 205B(4)(b) section 203 has effect with the omission of any reference to the auditor's report or a copy of it` |
| s 205B(4)(c) | 19604-19605 | paragraph | fork | F-W1 | `s 205B(4)(c) copies of an auditor's report need not be laid before the company in a general meeting` |
| s 205B(4)(d) | 19607-19609 | paragraph | fork | F-D1 | `s 205B(4)(d) the directors are in default of the duty to accompany the annual return with the statement`; `s 205B(4)(d) the directors must accompany the annual return with a statement` |
| s 205B(4)(d)(i) | 19611-19613 | item | fork | F-D1 | as s 205B(4)(d) |
| s 205B(4)(d)(ii) | 19615-19616 | item | fork | F-D1 | as s 205B(4)(d) |
| s 205B(4)(d)(iii) | 19618-19622 | item | fork | F-D1 | as s 205B(4)(d) |
| s 205B(5) | 19624-19627 | subsection | fork | F-W1 | `s 205B(5) the company ceases to be exempt from audit requirements`; `s 205B(5) the company remains exempt in relation to the accounts for the financial year` |
| s 205B(6) | 19629-19640 | subsection | fork | F-G1 | `s 205B(6) the members may require the company to obtain an audit of its accounts for the year` |
| s 205B(7) | 19642-19644 | subsection | fork | F-N1, F-W1 | `s 205B(7) the company is not entitled to the exemption under subsection (1) in respect of the financial year`; `s 205B(1) and (7) the company is exempt from audit requirements under section 205B for the financial year` |
| s 205B(8) | 19646-19648 | subsection | encoded |  | `s 205B(8) "accounting transaction" the transaction is an accounting transaction` |
| &nbsp;&nbsp;in-line term: "accounting transaction" | 19646-19648 | defined term (in-line) | encoded |  | as s 205B(8) |
| Heading of s 205C | 19650 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205C(1) | 19652-19656 | subsection | encoded |  | `s 205C(1) the company is exempt from audit requirements for the financial year` |
| s 205C(2) | 19658-19661 | subsection | fork | F-N1, F-W1 | `s 205C(2) section 205B(4), (6) and (7) apply to the small company`; `s 205C(2) the small company is not entitled to the exemption under subsection (1) in respect of the financial year`; `s 205C(1) and (2) the company is exempt from audit requirements under section 205C for the financial year` |
| s 205C(3) | 19663-19664 | subsection | fork | F-U1 | `s 205C(3) subsection (1) applies to the company as a parent company` |
| s 205C(3)(a) | 19666 | paragraph | fork | F-U1 | as s 205C(3) |
| s 205C(3)(b) | 19668-19670 | paragraph | fork | F-U1 | as s 205C(3) |
| s 205C(4) | 19672-19673 | subsection | fork | F-U1 | `s 205C(4) subsection (1) applies to the company as a subsidiary company` |
| s 205C(4)(a) | 19675 | paragraph | fork | F-U1 | as s 205C(4) |
| s 205C(4)(b) | 19677-19679 | paragraph | fork | F-U1 | as s 205C(4) |
| s 205C(5) | 19681-19684 | subsection | encoded |  | `s 205C(5) "small company" has the meaning given in the Thirteenth Schedule`; `s 205C(5) "small group" has the meaning given in the Thirteenth Schedule` |
| &nbsp;&nbsp;in-line term: "small company" | 19681-19684 | defined term (in-line) | encoded |  | as s 205C(5) |
| &nbsp;&nbsp;in-line term: "small group" | 19681-19684 | defined term (in-line) | encoded |  | as s 205C(5) |
| s 205C(6) | 19686-19696 | subsection | fork | F-D1 | `s 205C(6) this section applies to the company for the financial year`; `s 205C(6) the company and its directors are in default of the duty to prepare and lay the accounts as the earlier Part VI required` |
| s 205C(7) | 19698-19703 | subsection | fork | F-D1 | `s 205C(7) the company is in default of the duty to attach a copy of the accounts to the return`; `s 205C(7) the company must attach a copy of the accounts to the return` |
| Heading of s 205D | 19705-19706 | section heading | inert (reason 1) |  | a heading: not operative |
| s 205D | 19708-19724 | section | fork | F-D1, F-G1, F-P2 | `s 205D the Registrar may require the exempt company to lodge audited financial statements`; `s 205D the company is in default of the requirement in the Registrar's notice`; `s 205D the company must lodge what the Registrar's notice requires` |
| Heading of s 206 | 19726 | section heading | inert (reason 1) |  | a heading: not operative |
| s 206(1) | 19728-19729 | subsection | encoded |  | `s 206(1) the notice engages the duty of the company` |
| s 206(1)(a) | 19731-19732 | paragraph | encoded |  | as s 206(1) |
| s 206(1)(b) | 19734-19745 | paragraph | encoded |  | as s 206(1) |
| s 206(1)(c) | 19747-19751 | paragraph | fork | F-D1 | `s 206(1)(c) the company is in default of the duty to prepare the statement` |
| s 206(1)(d) | 19753-19754 | paragraph | fork | F-D1 | `s 206(1)(d) the company is in default of the duty to forward a copy of the statement` |
| s 206(1)(e) | 19756-19758 | paragraph | fork | F-D1 | `s 206(1)(e) the company is in default of the duty to lay the statement before the company in general meeting`; `s 206(1)(c) the company must prepare the statement of the auditor's other emoluments`; `s 206(1)(d) the company must forward a copy of the statement`; `s 206(1)(e) the company must lay the statement before the company in general meeting` |
| s 206(1A) | 19760-19765 | subsection | fork | F-D1 | `s 206(1A) the duty of the public company to review the auditor's fees applies`; `s 206(1A) the company is in default of the duty to review the auditor's fees and send the outcome`; `s 206(1A) the public company must review the auditor's fees and send the outcome` |
| s 206(2) | 19767-19770 | subsection | fork | F-E1 | `s 206(2) the person is guilty of the offence`; `s 206(2) the most the person may be fined on conviction` |
| Heading of s 207 | 19772-19773 | section heading | inert (reason 1) |  | a heading: not operative |
| s 207(1) | 19775 | subsection | fork | F-D1 | `s 207(1) the auditor is in default of the duty to report to the members`; `s 207(1) the auditor must report to the members` |
| s 207(1)(a) | 19777-19780 | paragraph | fork | F-D1 | as s 207(1) |
| s 207(1)(b) | 19782-19789 | paragraph | fork | F-D1 | as s 207(1) |
| s 207(1A) | 19791-19801 | subsection | fork | F-D1 | `s 207(1A) the auditor is in default of the duty to furnish the report to the directors in sufficient time`; `s 207(1A) the auditor commits no offence under the subsection`; `s 207(1A) the auditor must furnish the report to the directors in sufficient time` |
| s 207(2) | 19803 | subsection | fork | F-D1 | `s 207(2)(a) the auditor is in default of the duty to state the opinions on the financial statements` |
| s 207(2)(a) | 19805-19808 | paragraph | fork | F-D1 | as s 207(2) |
| s 207(2)(a)(i) | 19810-19811 | item | fork | F-D1 | as s 207(2)(a) |
| s 207(2)(a)(ii) | 19813 | item | fork | F-D1 | as s 207(2)(a) |
| s 207(2)(a)(ii)(A) | 19815-19816 | item | fork | F-D1 | as s 207(2)(a)(ii) |
| s 207(2)(a)(ii)(B) | 19818-19820 | item | fork | F-D1 | as s 207(2)(a)(ii) |
| s 207(2)(aa) (first of two) | 19822-19825 | paragraph | fork | F-D1 | `s 207(2)(aa) the auditor is in default of the duty to state whether the non-compliance is necessary for a true and fair view` |
| s 207(2)(aa)(i) | 19827 | item | fork | F-D1 | as s 207(2)(aa) (first of two) |
| s 207(2)(aa)(ii) | 19829-19830 | item | fork | F-D1 | as s 207(2)(aa) (first of two) |
| s 207(2)(aa) (second of two) | 19832-19842 | paragraph | fork | F-D1 | `s 207(2)(aa) the auditor is in default of the duty to state whether the non-compliance is necessary for a true and fair view` |
| s 207(2)(b) | 19844-19849 | paragraph | fork | F-D1 | `s 207(2)(b) the auditor is in default of the duty to state whether the records have been properly kept` |
| s 207(2)(c) | 19851 | paragraph | repealed or blank in this text |  | the text shows [Deleted by Act 5 of 2004] |
| s 207(2)(d) | 19853-19859 | paragraph | fork | F-D1 | `s 207(2)(d) the auditor is in default of the duty to state the defect, irregularity or matter` |
| s 207(2)(e) | 19861-19865 | paragraph | fork | F-D1 | `s 207(2)(e) the auditor is in default of the duty to state the reasons for not being satisfied` |
| s 207(3) | 19867-19868 | subsection | fork | F-D1 | `s 207(3) the auditor is in default of the duty to form an opinion on each of the matters` |
| s 207(3)(a) | 19870-19871 | paragraph | fork | F-D1 | as s 207(3) |
| s 207(3)(b) | 19873-19875 | paragraph | fork | F-D1 | as s 207(3) |
| s 207(3)(c) | 19877-19878 | paragraph | fork | F-D1 | as s 207(3) |
| s 207(3)(d) | 19880 | paragraph | repealed or blank in this text |  | the text shows [Deleted by Act 36 of 2014] |
| s 207(3)(e) | 19882-19897 | paragraph | fork | F-D1 | `s 207(3) the auditor is in default of the duty to form an opinion on each of the matters`; `s 207(3) the auditor is in default of the duty to state particulars of a deficiency, failure or shortcoming` |
| s 207(4) | 19899-19905 | subsection | encoded |  | `s 207(4) the auditor is not required to form an opinion on whether the records of the subsidiary corporation have been kept in accordance with this Act` |
| s 207(5) | 19907-19914 | subsection | fork | F-N1 | `s 207(5) the auditor has a right of access at all times to the item`; `s 207(5) the auditor is entitled to require information and explanations from the person` |
| s 207(6) | 19916-19925 | subsection | encoded |  | `s 207(6) the auditor has a right of access at all times to the item of the subsidiary corporation`; `s 207(6) the auditor is entitled, at the expense of the parent company, to require information and explanations from the person` |
| s 207(7) | 19927-19933 | subsection | fork | F-D1 | `s 207(7) the report is attached or endorsed, read on a member's request and open to inspection as the subsection requires` |
| s 207(8) | 19935-19945 | subsection | fork | F-A1, F-N1 | `s 207(8) the person is entitled to attend any general meeting of the company`; `s 207(8) the person is entitled to receive all notices of, and other communications relating to, any general meeting which a member is entitled to receive`; `s 207(8) the person is entitled to be heard at the general meeting on the part of the business` |
| s 207(9) | 19947-19948 | subsection | fork | F-D1 | `s 207(9) the auditor is in default of the duty to report the matter to the Registrar`; `s 207(9) the auditor must report the matter in writing to the Registrar` |
| s 207(9)(a) | 19950-19951 | paragraph | fork | F-D1 | as s 207(9) |
| s 207(9)(b) | 19953-19964 | paragraph | fork | F-D1 | as s 207(9) |
| s 207(9A) | 19966-19974 | subsection | fork | F-D1 | `s 207(9A) the auditor is in default of the duty to report the matter to the Minister`; `s 207(9A) the auditor must report the matter to the Minister` |
| s 207(9B) | 19976-19979 | subsection | encoded |  | `s 207(9B) no duty to which the auditor is subject is regarded as contravened by the report` |
| s 207(9C) | 19981-19992 | subsection | encoded |  | `s 207(9C) the auditor is not required to make a report to the Minister under subsection (9A)` |
| s 207(9D) | 19994-19995 | subsection | fork | F-J1 | `s 207(9D) the offence is a serious offence involving fraud or dishonesty` |
| &nbsp;&nbsp;in-line term: "a serious offence involving fraud or dishonesty" | 19994-20004 | defined term (in-line) | fork | F-J1 | as s 207(9D) |
| s 207(9D)(a) | 19997-19998 | paragraph | fork | F-J1 | as s 207(9D) |
| s 207(9D)(b) | 20000-20004 | paragraph | fork | F-J1 | as s 207(9D) |
| s 207(10) | 20006-20007 | subsection | fork | F-E1 | `s 207(10) the person is guilty of the offence`; `s 207(10) the most the person may be fined on conviction` |
| s 207(10)(a) | 20009-20013 | paragraph | fork | F-E1 | as s 207(10) |
| s 207(10)(b) | 20015-20020 | paragraph | fork | F-E1 | as s 207(10) |
| s 207(10)(c) | 20022-20025 | paragraph | fork | F-E1 | as s 207(10) |
| s 207(10)(d) | 20027-20032 | paragraph | fork | F-E1 | as s 207(10) |
| s 207(11) | 20034 | subsection | encoded |  | `s 207(11) the item is excluded from the reference to registers in subsections (5), (6) and (10)` |
| s 207(11)(a) | 20036-20039 | paragraph | encoded |  | as s 207(11) |
| s 207(11)(b) | 20041-20042 | paragraph | encoded |  | as s 207(11) |
| s 207(11)(c) | 20044-20050 | paragraph | encoded |  | as s 207(11) |
| Heading of s 208 | 20052-20053 | section heading | inert (reason 1) |  | a heading: not operative |
| s 208(1) | 20055-20059 | subsection | encoded |  | `s 208(1) the auditor is not liable to an action for defamation in respect of the statement` |
| s 208(2) | 20061-20065 | subsection | encoded |  | `s 208(2) the person is not liable to an action for defamation in respect of the publication of the document` |
| s 208(3) | 20067-20069 | subsection | encoded |  | `s 208(3) section 208 limits or affects the right, privilege or immunity` |
| Heading of s 208A | 20071 | section heading | inert (reason 1) |  | a heading: not operative |
| s 208A(1) | 20073-20080 | subsection | encoded |  | `s 208A(1) the provision is void` |
| s 208A(2) | 20082-20087 | subsection | encoded |  | `s 208A(2) the section does not prevent the company from indemnifying the auditor`; `s 208A(1) and (2) the provision is void under the section` |
| s 208A(2)(a) | 20089-20091 | paragraph | encoded |  | as s 208A(2) |
| s 208A(2)(b) | 20093-20097 | paragraph | encoded |  | as s 208A(2) |
| Heading of s 209 | 20099 | section heading | inert (reason 1) |  | a heading: not operative |
| s 209(1) | 20101-20108 | subsection | fork | F-D1, F-P2 | `s 209(1) the last day for the auditor to send a copy to every trustee`; `s 209(1) the auditor is in default of the duty to send a copy to every trustee`; `s 209(1) the auditor must send a copy to every trustee within 7 days` |
| s 209(2) | 20110-20117 | subsection | fork | F-D1, F-P2 | `s 209(2) the last day for the auditor to send the report`; `s 209(2) the auditor is in default of the duty to send the report`; `s 209(2) the auditor must send the report within 7 days` |
| s 209(3) | 20119-20121 | subsection | fork | F-E1 | `s 209(3) the person is guilty of the offence`; `s 209(3) the most the person may be fined on conviction`; `s 209(3) the person is also liable on conviction to a default penalty` |
| Heading of s 209A | 20123 | section heading | inert (reason 1) |  | a heading: not operative |
| s 209A | 20125 | section | encoded |  | `s 209A the definitions of this section apply in this Part` |
| Defined term balance sheet | 20127-20129 | definition | encoded |  | `s 209A "balance sheet" the document is a balance sheet of the company` |
| Defined term consolidated financial statements | 20131-20135 | definition | encoded |  | `s 209A "consolidated financial statements" the statements are consolidated financial statements` |
| Defined term consolidated total assets | 20137-20146 | definition | encoded |  | `s 209A "consolidated total assets" the consolidated total assets of the group, in Singapore dollars` |
| Defined term directors’ statement | 20148-20149 | definition | encoded |  | `s 209A "directors' statement" the statement is the directors' statement` |
| Defined term entity | 20151-20154 | definition | encoded |  | `s 209A "entity" the body is an entity` |
| Defined term financial statements | 20156-20158 | definition | encoded |  | `s 209A "financial statements" the statements are financial statements` |
| Defined term group | 20160 | definition | encoded |  | `s 209A "group" the arrangement is a group` |
| Defined term parent company | 20162-20164 | definition | encoded |  | `s 209A "parent company" the company is a parent company` |
| Defined term subsidiary company | 20166-20167 | definition | encoded |  | `s 209A "subsidiary company" the company is a subsidiary company` |
| Defined term subsidiary corporation | 20169-20170 | definition | encoded |  | `s 209A "subsidiary corporation" the corporation is a subsidiary corporation` |
| Defined term ultimate parent corporation | 20172-20176 | definition | encoded |  | `s 209A "ultimate parent corporation" the corporation is an ultimate parent corporation` |
| s 209B | 20178-20181 | section | repealed or blank in this text |  | the text shows [Repealed by Act 5 of 2004] |
| Heading of the Thirteenth Schedule | 29013-29017 | schedule heading | inert (reason 1) |  | a heading: not operative |
| Sch 13 para 1 | 29019 | schedule paragraph | encoded |  | `sch 13 para 1(a) the company is a small company for the financial year` |
| Sch 13 para 1(a) | 29021-29024 | schedule sub-paragraph | encoded |  | as Sch 13 para 1 |
| Sch 13 para 1(b) | 29026-29029 | schedule sub-paragraph | encoded |  | `sch 13 para 1(b) the group is a small group for the financial year` |
| Sch 13 para 2 | 29031 | schedule paragraph | fork | F-S1 | `sch 13 para 2 the company qualifies as a small company from the financial year`; `sch 13 para 2(b) the company qualifies as a small company from the financial year (other reading: the same 2 criteria in both years)` |
| Sch 13 para 2(a) | 29033 | schedule sub-paragraph | fork | F-S1 | as Sch 13 para 2 |
| Sch 13 para 2(b) | 29035-29036 | schedule sub-paragraph | fork | F-S1 | `sch 13 para 2(b)(i) the revenue for the financial year does not exceed $10 million`; `sch 13 para 2(b)(ii) the total assets at the end of the financial year do not exceed $10 million`; `sch 13 para 2(b)(iii) the company has at the end of the financial year not more than 50 employees`; `sch 13 para 2(b) the number of the criteria the financial year satisfies`; `sch 13 para 2(b) the financial year satisfies any 2 of the criteria`; `sch 13 para 2 the company qualifies as a small company from the financial year`; `sch 13 para 2(b) the company qualifies as a small company from the financial year (other reading: the same 2 criteria in both years)` |
| Sch 13 para 2(b)(i) | 29038-29039 | item | fork | F-S1 | as Sch 13 para 2(b) |
| Sch 13 para 2(b)(ii) | 29041-29042 | item | fork | F-S1 | as Sch 13 para 2(b) |
| Sch 13 para 2(b)(iii) | 29044-29045 | item | fork | F-S1 | as Sch 13 para 2(b) |
| Sch 13 para 3 | 29047-29048 | schedule paragraph | fork | F-S3 | `sch 13 para 3 the company qualifies as a small company from the financial year` |
| Sch 13 para 3(a) | 29050 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 3 |
| Sch 13 para 3(a)(i) | 29052 | item | fork | F-S3 | as Sch 13 para 3(a) |
| Sch 13 para 3(a)(ii) | 29054-29055 | item | fork | F-S3 | as Sch 13 para 3(a) |
| Sch 13 para 3(a)(ii)(A) | 29057-29058 | item | fork | F-S3 | as Sch 13 para 3(a)(ii) |
| Sch 13 para 3(a)(ii)(B) | 29060-29061 | item | fork | F-S3 | as Sch 13 para 3(a)(ii) |
| Sch 13 para 3(a)(ii)(C) | 29063-29069 | item | fork | F-S3 | as Sch 13 para 3(a)(ii) |
| Sch 13 para 3(b) | 29071 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 3 |
| Sch 13 para 3(b)(i) | 29073-29074 | item | fork | F-S3 | as Sch 13 para 3(b) |
| Sch 13 para 3(b)(ii) | 29076-29077 | item | fork | F-S3 | as Sch 13 para 3(b) |
| Sch 13 para 3(b)(ii)(A) | 29079-29080 | item | fork | F-S3 | as Sch 13 para 3(b)(ii) |
| Sch 13 para 3(b)(ii)(B) | 29082-29083 | item | fork | F-S3 | as Sch 13 para 3(b)(ii) |
| Sch 13 para 3(b)(ii)(C) | 29085-29086 | item | fork | F-S3 | as Sch 13 para 3(b)(ii) |
| Sch 13 para 4 | 29088-29089 | schedule paragraph | encoded |  | `sch 13 para 4 the company qualifies as a small company from the financial year` |
| Sch 13 para 4(a) | 29091-29092 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 4 |
| Sch 13 para 4(a)(i) | 29094 | item | fork | F-S3 | as Sch 13 para 4(a) |
| Sch 13 para 4(a)(ii) | 29096-29097 | item | fork | F-S3 | as Sch 13 para 4(a) |
| Sch 13 para 4(a)(ii)(A) | 29099-29100 | item | fork | F-S3 | as Sch 13 para 4(a)(ii) |
| Sch 13 para 4(a)(ii)(B) | 29102-29103 | item | fork | F-S3 | as Sch 13 para 4(a)(ii) |
| Sch 13 para 4(a)(ii)(C) | 29105-29106 | item | fork | F-S3 | as Sch 13 para 4(a)(ii) |
| Sch 13 para 4(b) | 29108-29109 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 4 |
| Sch 13 para 4(b)(i) | 29111-29112 | item | fork | F-S3 | as Sch 13 para 4(b) |
| Sch 13 para 4(b)(ii) | 29114-29115 | item | fork | F-S3 | as Sch 13 para 4(b) |
| Sch 13 para 4(b)(ii)(A) | 29117-29118 | item | fork | F-S3 | as Sch 13 para 4(b)(ii) |
| Sch 13 para 4(b)(ii)(B) | 29120-29126 | item | fork | F-S3 | as Sch 13 para 4(b)(ii) |
| Sch 13 para 4(b)(ii)(C) | 29128-29129 | item | fork | F-S3 | as Sch 13 para 4(b)(ii) |
| Sch 13 para 5 | 29131-29132 | schedule paragraph | fork | F-S2 | `sch 13 para 5 the company ceases to be a small company from the financial year`; `sch 13 para 5(b) the company fails to satisfy any 2 of the criteria in either of the 2 preceding financial years (other reading)` |
| Sch 13 para 5(a) | 29134-29135 | schedule sub-paragraph | fork | F-S2 | as Sch 13 para 5 |
| Sch 13 para 5(b) | 29137-29139 | schedule sub-paragraph | fork | F-S2 | as Sch 13 para 5 |
| Sch 13 para 5(b)(i) | 29141-29142 | item | fork | F-S2 | as Sch 13 para 5(b) |
| Sch 13 para 5(b)(ii) | 29144-29145 | item | fork | F-S2 | as Sch 13 para 5(b) |
| Sch 13 para 5(b)(iii) | 29147-29148 | item | fork | F-S2 | as Sch 13 para 5(b) |
| Sch 13 para 6 | 29150 | schedule paragraph | encoded |  | `sch 13 para 6 paragraph 5 does not apply to the company` |
| Sch 13 para 6(a) | 29152-29153 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 6 |
| Sch 13 para 6(b) | 29155-29156 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 6 |
| Sch 13 para 7 | 29158-29160 | schedule paragraph | fork | F-S1 | `sch 13 para 7 the group qualifies as a small group from the financial year` |
| Sch 13 para 7(a) | 29162-29163 | schedule sub-paragraph | fork | F-S1 | as Sch 13 para 7 |
| Sch 13 para 7(b) | 29165-29166 | schedule sub-paragraph | fork | F-S1 | as Sch 13 para 7 |
| Sch 13 para 7(c) | 29168-29169 | schedule sub-paragraph | fork | F-S1 | as Sch 13 para 7 |
| Sch 13 para 8 | 29171 | schedule paragraph | encoded |  | `sch 13 para 8 the group qualifies as a small group from the financial year` |
| Sch 13 para 8(a) | 29173-29174 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 8 |
| Sch 13 para 8(a)(i) | 29176-29182 | item | fork | F-S3 | as Sch 13 para 8(a) |
| Sch 13 para 8(a)(ii) | 29184-29185 | item | fork | F-S3 | as Sch 13 para 8(a) |
| Sch 13 para 8(a)(iii) | 29187-29188 | item | fork | F-S3 | as Sch 13 para 8(a) |
| Sch 13 para 8(b) | 29190-29191 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 8 |
| Sch 13 para 8(b)(i) | 29193-29194 | item | fork | F-S3 | as Sch 13 para 8(b) |
| Sch 13 para 8(b)(ii) | 29196-29197 | item | fork | F-S3 | as Sch 13 para 8(b) |
| Sch 13 para 8(b)(iii) | 29199-29200 | item | fork | F-S3 | as Sch 13 para 8(b) |
| Sch 13 para 9 | 29202-29203 | schedule paragraph | encoded |  | `sch 13 para 9 the group qualifies as a small group from the financial year` |
| Sch 13 para 9(a) | 29205-29206 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 9 |
| Sch 13 para 9(a)(i) | 29208-29209 | item | fork | F-S3 | as Sch 13 para 9(a) |
| Sch 13 para 9(a)(ii) | 29211-29212 | item | fork | F-S3 | as Sch 13 para 9(a) |
| Sch 13 para 9(a)(iii) | 29214-29215 | item | fork | F-S3 | as Sch 13 para 9(a) |
| Sch 13 para 9(b) | 29217-29219 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 9 |
| Sch 13 para 9(b)(i) | 29221-29222 | item | fork | F-S3 | as Sch 13 para 9(b) |
| Sch 13 para 9(b)(ii) | 29224-29225 | item | fork | F-S3 | as Sch 13 para 9(b) |
| Sch 13 para 9(b)(iii) | 29227-29228 | item | fork | F-S3 | as Sch 13 para 9(b) |
| Sch 13 para 10 | 29230-29237 | schedule paragraph | fork | F-S2 | `sch 13 para 10 the group ceases to be a small group from the financial year`; `sch 13 para 10 the group fails to satisfy any 2 of the criteria in either of the 2 preceding financial years (other reading)` |
| Sch 13 para 10(a) | 29239-29240 | schedule sub-paragraph | fork | F-S2 | as Sch 13 para 10 |
| Sch 13 para 10(b) | 29242-29243 | schedule sub-paragraph | fork | F-S2 | as Sch 13 para 10 |
| Sch 13 para 10(c) | 29245-29246 | schedule sub-paragraph | fork | F-S2 | as Sch 13 para 10 |
| Sch 13 para 11 | 29248 | schedule paragraph | encoded |  | `sch 13 para 11 paragraph 10 does not apply to the group` |
| Sch 13 para 11(a) | 29250-29251 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 11 |
| Sch 13 para 11(b) | 29253-29254 | schedule sub-paragraph | fork | F-S3 | as Sch 13 para 11 |
| Sch 13 para 12 | 29256 | schedule paragraph | encoded |  | `sch 13 para 12(a) the entity is part of the group` |
| Sch 13 para 12(a) | 29258-29259 | schedule sub-paragraph | encoded |  | as Sch 13 para 12 |
| Sch 13 para 12(b) | 29261 | schedule sub-paragraph | encoded |  | `sch 13 para 12(b) the consolidated total assets of the group, in Singapore dollars`; `sch 13 para 12(b) the consolidated revenue of the group, in Singapore dollars` |
| Sch 13 para 12(b)(i) | 29263-29267 | item | encoded |  | as Sch 13 para 12(b) |
| Sch 13 para 12(b)(ii) | 29269-29270 | item | encoded |  | as Sch 13 para 12(b) |
| Sch 13 para 12(b)(ii)(A) | 29272-29273 | item | encoded |  | as Sch 13 para 12(b)(ii) |
| Sch 13 para 12(b)(ii)(B) | 29275-29276 | item | encoded |  | as Sch 13 para 12(b)(ii) |
| Sch 13 para 12(c) | 29278-29280 | schedule sub-paragraph | encoded |  | `sch 13 para 12(c) the entity is a parent for the purposes of the Schedule` |
| Sch 13 para 13 | 29282 | schedule paragraph | encoded |  | `sch 13 para 13(a) the company is a small company for the later financial year` |
| Sch 13 para 13(a) | 29284-29292 | schedule sub-paragraph | encoded |  | as Sch 13 para 13 |
| Sch 13 para 13(b) | 29294-29297 | schedule sub-paragraph | encoded |  | `sch 13 para 13(b) the group is a small group for the later financial year` |
| Sch 13 para 14 | 29299 | schedule paragraph | fork | F-G1 | `sch 13 para 14(a) the company may become a small company again` |
| Sch 13 para 14(a) | 29301-29303 | schedule sub-paragraph | fork | F-G1 | as Sch 13 para 14 |
| Sch 13 para 14(b) | 29305-29309 | schedule sub-paragraph | fork | F-G1 | `sch 13 para 14(b) the group may become a small group again` |

## Fork register (sgc2)

Every entry names its rows (the coverage table's `Unit` column), the readings seen, the one taken, and the text or Guide line that licenses each.
`inputs/ENCODING-GUIDE.md` is cited by section 5's headings and dated rulings, with the Guide's own words quoted.
A row is `fork` in the coverage table when it rests on an entry of kind "reading" or "site by site"; an entry of kind "governed" or "recorded" is listed so that a comment in a layer-1 file that points at it finds it, and a row that rests on such an entry alone stays `encoded`.
Where a layer-1 comment says "fork line F-xx", this is where xx is.
The other reading of a Schedule fork is also coded, as a function labelled `(other reading)` that nothing else calls, so a reviewer can switch to it by changing one call.

### Entries of kind "site by site" (the Guide leaves the case to the encoder and asks for one fork line per site)

- **F-D1** (duty not engaged). Rows: s 205(1), s 205(2), s 205(5), s 205(5)(a), s 205(12), s 205AA(3), s 205AC(1), s 205AD(3), s 205AD(3)(a), s 205AD(3)(b), s 205AD(4), s 205AD(4)(a), s 205AD(4)(b), s 205AF(1), s 205AF(1)(a), s 205AF(1)(b), s 205AF(1)(c), s 205AF(1)(d), s 205A(2), s 205B(4)(d), s 205B(4)(d)(i), s 205B(4)(d)(ii), s 205B(4)(d)(iii), s 205C(6), s 205C(7), s 205D, s 206(1)(c), s 206(1)(d), s 206(1)(e), s 206(1A), s 207(1), s 207(1)(a), s 207(1)(b), s 207(1A), s 207(2), s 207(2)(a), s 207(2)(a)(i), s 207(2)(a)(ii), s 207(2)(a)(ii)(A), s 207(2)(a)(ii)(B), s 207(2)(aa) (first of two), s 207(2)(aa)(i), s 207(2)(aa)(ii), s 207(2)(aa) (second of two), s 207(2)(b), s 207(2)(d), s 207(2)(e), s 207(3), s 207(3)(a), s 207(3)(b), s 207(3)(c), s 207(3)(e), s 207(7), s 207(9), s 207(9)(a), s 207(9)(b), s 207(9A), s 209(1), s 209(2).
  The functions named "... is in default of the duty ...": `JUST TRUE` is "not done by the time asked about" (and, for a duty stated as "immediately", "not done"); `JUST FALSE` is "done in time", "time still running" or "the duty did not arise" (the facts do not engage it).
  Taken: `JUST FALSE` for "the duty did not arise", because the function is the provision's own question ("is this person in default of this duty?") and the text of the duty is the "no".
  Other reading: `NOTHING` when the duty did not arise (the text does not say what a person with no duty has done).
  Licence: Guide section 5, "Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z)", which names two of the six questions: "a bare \"must\" not done; ... a duty whose \"if\" or \"where\" is unmet".
- **F-E1** (an unmet element of an offence). Rows: s 205(17), s 205AC(4), s 205AD(5), s 205AF(5), s 205A(3), s 206(2), s 207(10), s 207(10)(a), s 207(10)(b), s 207(10)(c), s 207(10)(d), s 209(3). This is split site (i); see `## Split sites (sgc2)`.
- **F-W1** ("where" gate). Rows: s 205(7), s 205(7)(a), s 205(7)(b), s 205B(4), s 205B(4)(a), s 205B(4)(b), s 205B(4)(c), s 205B(5), s 205B(7), s 205C(2). This is split site (ii) for the "may" and "need not" functions among them; see `## Split sites (sgc2)`.
  The rows that are not "may" functions (205B(5), 205B(7), 205C(2)) answer the same way for the same reason and are listed here, not counted as sites.
- **F-N1** ("entitled"-named functions). Rows: s 205B(7), s 205C(2), s 207(5), s 207(8).
  s 207(5) and s 207(8) are entitlements ("is entitled to require", "is entitled to attend"): each answers `JUST TRUE` or `NOTHING`, never `JUST FALSE`.
  s 205B(7) and s 205C(2) say the company "is not entitled to the exemption" where a notice was given: the functions are named for the bar and answer `JUST TRUE` where the notice was given, `JUST FALSE` where there was none (a "where" gate, F-W1).
  Other reading: for the entitlements, `JUST FALSE` when the conditions fail; for the bars, `NOTHING` where there was no notice.
  Licence: Guide section 5, the grant ruling of 2026-11-12, limit 3: "an \"entitled\"-named function (an entitlement is a claim, not a power, and this guide does not settle it)".
- **F-G1** (a grant whose "if" gate failed). Rows: s 205(3), s 205(5)(b), s 205(6), s 205(7), s 205(7)(a), s 205(7)(b), s 205(8), s 205(10), s 205(11), s 205AA(1), s 205AB(1), s 205AB(1)(a), s 205AB(1)(b), s 205AD(2), s 205AD(2)(a), s 205AD(2)(b), s 205AF(2), s 205B(6), s 205D, Sch 13 para 14, Sch 13 para 14(a), Sch 13 para 14(b).
  A function named for a grant or a power ("may", "is permitted to", "has power to") answers `NOTHING` where its "if" gate fails, or where the grant is limited by a named complement (a three-fourths majority, "in writing") and the case falls outside it.
  Other reading: `JUST FALSE` ("may not").
  Licence: Guide section 5, the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed".
- **F-U1** ("unless" once met). Rows: s 205C(3), s 205C(3)(a), s 205C(3)(b), s 205C(4), s 205C(4)(a), s 205C(4)(b).
  s 205C(3) and (4): "Subsection (1) does not apply to a parent company unless the parent company (a) is a small company; and (b) is part of a small group" (and the same for a subsidiary company).
  Taken: when both (a) and (b) hold, the function answering "subsection (1) applies to the company as a parent company" is `NOTHING`: the text bars subsection (1) in the other cases and does not say that it applies in this one (subsection (1) itself answers).
  Other reading: `JUST TRUE` (the "unless" restores the application of subsection (1)).
  Licence: Guide section 5, "Questions with no convention", which names "an \"unless\" or \"except\" once it is met".
- **F-X1** (an "(other than X)" carve-out). Rows: s 205AA(1).
  s 205AA(1) gives an auditor of a non-public interest company "(other than a company which is a subsidiary company of a public interest company)" the power to resign by notice.
  Taken: for the excluded company the function answers `NOTHING`, because s 205AB, not s 205AA, governs it.
  Other reading: `JUST FALSE` (s 205AA(1) says no to that company).
  Licence: Guide section 5, "Questions with no convention", which names "\"(other than X)\"".

### Entries of kind "reading" (the words of the text can be read two ways)

- **F-A1** (an agent is heard). Rows: s 207(8).
  s 207(8): the auditor "or an agent authorised by the auditor in writing for the purpose is entitled to attend any general meeting ... and to be heard at any general meeting which the auditor attends on any part of the business of the meeting which concerns the auditor in such capacity as auditor" (lines 19935-19945).
  Taken: the agent may be heard at a meeting the auditor does not attend (read in the agent's favour).
  Other reading: "which the auditor attends" limits the right to be heard to meetings the auditor attends, so an agent is not heard when the auditor is absent.
  Licence: the sentence makes "An auditor ... or an agent" the one subject of "is entitled ... to be heard"; the words "which the auditor attends" are the limit that the other reading relies on.
- **F-J1** ("not less than 2 years"). Rows: s 207(9D), s 207(9D)(a), s 207(9D)(b).
  s 207(9D)(a): "an offence that is punishable by imprisonment for a term that is not less than 2 years" (line 19997).
  Taken: the longest term the offence is punishable with is at least 2 years.
  Other reading: the least term the offence carries is at least 2 years (a minimum sentence).
  Licence: "punishable by imprisonment for a term that is not less than 2 years" is a statement about what the offence can carry, not about a floor; the other reading takes "a term not less than 2 years" as the sentence itself.
- **F-P3** (how "14 days" counts). Rows: s 205AA(3), s 205AC(2), s 205AD(3), s 205AD(3)(a), s 205AD(3)(b), s 205AD(4), s 205AD(4)(a), s 205AD(4)(b), s 205AF(1)(d).
  "Within 14 days beginning on the date on which ..." (s 205AA(3), s 205AC(2), s 205AD(3) and (4)) counts that date as day 1, so the last day is the date plus 13; "within 14 days after ..." counts it out (the keel's rule P1), so the last day is the date plus 14.
  s 205AF(1)(d) says "within 14 days of the appointment", and is read as "after" (date plus 14).
  Other reading: for the "beginning on" sites, the keel's P1 (date plus 14); for "of", the date itself counts (date plus 13).
  Licence: the words "beginning on the date" and "after".
- **F-P4** ("before the next annual general meeting"). Rows: s 205A(2).
  s 205A(2): "appoint a person or persons to be auditor or auditors of the company at any time before the next annual general meeting".
  Taken: the last day is the day before the meeting.
  Other reading: the day of the meeting is in time (an appointment made at the meeting itself).
  Licence: "before".
- **F-R1** ("Unless the Registrar ... otherwise orders"). Rows: s 205(6).
  s 205(6): "Unless the Registrar on the application of the company otherwise orders, the company must send a copy of the representations as so requested and the auditor may, without affecting the auditor's right to be heard orally, require that the representations be read out at the meeting".
  Taken: the "Unless" governs the whole sentence; on such an order both the company's duty and the auditor's right fall away.
  Other reading: it governs only the company's duty to send; the auditor's right to require reading out stands.
  Licence: the "Unless" opens the sentence and both limbs follow one comma-joined clause.
- **F-S1** (the Schedule's "any 2 of the criteria for each of the 2 years", paras 2(b) and 7). Rows: Sch 13 para 2, Sch 13 para 2(a), Sch 13 para 2(b), Sch 13 para 2(b)(i), Sch 13 para 2(b)(ii), Sch 13 para 2(b)(iii), Sch 13 para 7, Sch 13 para 7(a), Sch 13 para 7(b), Sch 13 para 7(c).
  Taken (A): in each of the two years at least 2 of the 3 criteria hold, and the two need not be the same pair in both years.
  Other reading (B): the same two criteria hold in both years; coded as `sch 13 para 2(b) ... (other reading)` and its para 7 counterpart, called by nothing.
  Licence: "satisfies any 2 of the following criteria for each of the 2 financial years" (para 2(b), line 29035) and para 7 (line 29158): "for each of the 2" ties the test to each year.
- **F-S2** (the Schedule's ceasing, paras 5(b) and 10). Rows: Sch 13 para 5, Sch 13 para 5(a), Sch 13 para 5(b), Sch 13 para 5(b)(i), Sch 13 para 5(b)(ii), Sch 13 para 5(b)(iii), Sch 13 para 10, Sch 13 para 10(a), Sch 13 para 10(b), Sch 13 para 10(c).
  Para 5(b): "it does not satisfy any 2 of the following criteria for each of the 2 consecutive financial years immediately preceding the financial year"; para 10: "... for 2 consecutive financial years immediately preceding the financial year" (line 29230; note that para 10 omits "each of").
  Taken (C1): the company or group ceases where it fails the test in both of the 2 preceding years.
  Other reading (C2): it ceases where it fails in either year; coded as `... fails to satisfy any 2 of the criteria in either of the 2 preceding years` and called by nothing.
  Licence: "for each of the 2 consecutive financial years" (a failure in each year); the other reading takes the sentence as "does not satisfy ... for [either] year".
- **F-S3** (the ordinal of a financial year). Rows: Sch 13 para 3, Sch 13 para 3(a), Sch 13 para 3(a)(i), Sch 13 para 3(a)(ii), Sch 13 para 3(a)(ii)(A), Sch 13 para 3(a)(ii)(B), Sch 13 para 3(a)(ii)(C), Sch 13 para 3(b), Sch 13 para 3(b)(i), Sch 13 para 3(b)(ii), Sch 13 para 3(b)(ii)(A), Sch 13 para 3(b)(ii)(B), Sch 13 para 3(b)(ii)(C), Sch 13 para 4(a), Sch 13 para 4(a)(i), Sch 13 para 4(a)(ii), Sch 13 para 4(a)(ii)(A), Sch 13 para 4(a)(ii)(B), Sch 13 para 4(a)(ii)(C), Sch 13 para 4(b), Sch 13 para 4(b)(i), Sch 13 para 4(b)(ii), Sch 13 para 4(b)(ii)(A), Sch 13 para 4(b)(ii)(B), Sch 13 para 4(b)(ii)(C), Sch 13 para 6(a), Sch 13 para 6(b), Sch 13 para 8(a), Sch 13 para 8(a)(i), Sch 13 para 8(a)(ii), Sch 13 para 8(a)(iii), Sch 13 para 8(b), Sch 13 para 8(b)(i), Sch 13 para 8(b)(ii), Sch 13 para 8(b)(iii), Sch 13 para 9(a), Sch 13 para 9(a)(i), Sch 13 para 9(a)(ii), Sch 13 para 9(a)(iii), Sch 13 para 9(b), Sch 13 para 9(b)(i), Sch 13 para 9(b)(ii), Sch 13 para 9(b)(iii), Sch 13 para 11(a), Sch 13 para 11(b).
  Paras 3, 4, 6, 8, 9 and 11 speak of "its first financial year", "its second financial year", "its third financial year", and the Schedule does not say how a first financial year is fixed (a short first year, a year ending on a date set later).
  Taken: the ordinal is asked as a number the person states; no date arithmetic.
  Other reading: derive the ordinal from the incorporation date and the year-end; the text does not choose, so the module does not.
- **F-T1** ("hold office, subject to this section"). Rows: s 205(1), s 205(2), s 205(9).
  s 205(1), (2) and (9): an auditor appointed "hold[s] office, subject to this section, until the conclusion of" the meeting named.
  Taken: an office already ended by removal under s 205(4) or by resignation under ss 205AA or 205AB is not held (`JUST FALSE`), as well as one past the meeting named.
  Other reading: "this section" is s 205 only, so removal ends the tenure but a resignation (outside s 205) is not mentioned by the sentence and the function would answer `NOTHING` for it.
- **F-V1** (the three-fourths majority). Rows: s 205(7), s 205(7)(a).
  s 205(7)(a): "a majority of not less than three-fourths of such members of the company as being entitled to do so vote in person or, where proxies are allowed, by proxy" (lines 19127-19130).
  Taken: three-fourths of the members who vote (the function multiplies the votes for the resolution by 4 and compares with 3 times the votes cast on it).
  Other reading: three-fourths of all members entitled to vote.
  Licence: "such members ... as being entitled to do so vote": the class is the members who vote.

### Entries of kind "governed" or "recorded" (a ruling or the brief decides; listed so that the pointer finds its target)

- **F-M1** (a failed "if" counts as the text's no). Rows resting on it that are not also forks: s 205(13), s 205AD(1), s 205AF(3), s 205B(1), s 205B(1)(a), s 205B(1)(b), s 206(1), s 206(1)(a), s 206(1)(b), Sch 13 para 4, Sch 13 para 8, Sch 13 para 9.
  The status quo of the brief's rule of 2026-10-29, "for a lawyer, not for you to decide": every branch that rests on it is listed under `## Marginal readings for a lawyer (sgc2)` with the other reading.
- **F-P1** (a period the text fixes in its own words). Rows: s 205(5)(b), s 205(7)(b), s 205B(6).
  Guide section 5, the periods ruling of 2026-11-05, item (a): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`".
  Examples: s 205(5)(b) "within 7 days after the receipt", s 205(7)(b) the adjourned meeting "not earlier than 20 days and not later than 30 days after the meeting", s 205B(6) "not later than one month before the end of that year".
- **F-S4** (a scope limit with no "only"). Rows: s 205A(1), s 205C(1).
  Guide section 5, the periods ruling of 2026-11-05, item (c): "a scope limit with no \"only\" ... outside the scope the answer is `NOTHING`".
  s 205A(1) ("a company which is exempt from audit requirements under section 205B or 205C, and its directors, are exempt from section 205(1) or (2)") says nothing of a company that is not so exempt; s 205C(1) says nothing of a company that is not a small company.
- **F-P2** (a duty "within N days after X" is met by any act up to the last day). Rows: every row of a duty with a last day, as the coverage table's fork column shows (s 205(1), s 205(12), s 205AA(3), s 205AC(1), s 205AD(3), s 205AD(3)(a), s 205AD(3)(b), s 205AD(4), s 205AD(4)(a), s 205AD(4)(b), s 205AF(1), s 205AF(1)(a), s 205AF(1)(b), s 205AF(1)(c), s 205AF(1)(d), s 205A(2), s 205D, s 209(1), s 209(2)).
  The keel's `period: the date is within a period after` is a window that opens the day after the event; an act done on the event day, or before it, would fall outside the window and read as late.
  The duty functions here use the last day (`period: the last day of a period after`) and count a default only for an act after it, or no act once it has passed (`s 205 helper: default in an act due by the last day`, `sgc2-common.l4`).
  Other reading: an act done before the window opens is not "within" the days after the event.
  Licence: a duty to act "within N days after X" is a duty not to act later than N days after X; the same reading is in the header comment of `sgc2-common.l4`.
  The pattern is stated in the header comment of `sgc2-common.l4` (fork line F-P2); the layer-1 functions that follow it call the helper, and the coverage table's fork column lists their rows.

## Jural relations (sgc2)

One row per provision of the ranges: 104 rows, of which 36 are `none` (a definition, a counting rule, a tenure rule, a deleted or repealed provision, or a text that decides a status and no relation).
The holder and bearer columns follow Hohfeld's correlatives (a claim and a duty; a privilege and a no-right; a power and a liability; an immunity and a disability); where the text names no one, the cell says so, and no party is invented.
A rule is stated once, as one relation between two parties, and named neutrally; the L4 column lists the functions and rules whose `@ref` locator overlaps the provision (the first six, with the rest in the coverage table).

| Provision | Holder (right, privilege, power, immunity) | Bearer (duty, no-right, liability, disability) | Relation | L4 rule(s) |
| --- | --- | --- | --- | --- |
| s 205(1) | no claimant is named; the Act enforces it through s 205(17) | the directors of the company | duty: appoint an auditor within 3 months after incorporation (the appointed auditor holds office until the first annual general meeting: a tenure rule, no relation) | `s 205(1) the last day for the directors to appoint the first auditor`; `s 205(1) the directors are in default of the duty to appoint the first auditor`; `s 205(1) the directors must appoint the first auditor`; `s 205(1) the auditor appointed by the directors holds office` |
| s 205(2) | no claimant is named; enforced through s 205(17) | the company | duty: appoint an auditor at each annual general meeting | `s 205(2) the company is in default of the duty to appoint an auditor at the annual general meeting`; `s 205(2) the company must appoint an auditor at each annual general meeting`; `s 205(2) the auditor appointed at the annual general meeting holds office` |
| s 205(3) | the directors; the surviving or continuing auditor | the company (bound by the appointment); no one named for the privilege | power / liability: appoint to fill a casual vacancy; privilege / no-right: the surviving or continuing auditor may act while the vacancy continues | `s 205(3) the directors may appoint the accounting entity to fill the casual vacancy`; `s 205(3) the surviving or continuing auditor may act` |
| s 205(4) | the company, by ordinary resolution in general meeting on special notice | the auditor | power / liability: removal from office | `s 205(4) the auditor may be removed from office by the resolution` |
| s 205(5) | the auditor; the Registrar | the company | (a) claim / duty: a copy of the special notice immediately; (b) power / liability: the auditor makes representations and asks that a copy be sent to the members | `s 205(5)(a) the company is in default of the duty to send a copy of the notice`; `s 205(5)(a) the company must send a copy of the notice of the removal resolution`; `s 205(5)(b) the auditor may make representations and have a copy sent to every member` |
| s 205(6) | the auditor; the Registrar | the company | claim / duty: the company sends the representations; power / liability: the auditor requires that they be read out, and the Registrar may order otherwise on the company's application | `s 205(6) the company is in default of the duty to send a copy of the representations`; `s 205(6) the company must send a copy of the representations`; `s 205(6) the auditor may require that the representations be read out at the meeting` |
| s 205(7) | the company in general meeting | the company and the accounting entity nominated (whose position changes on appointment) | power / liability: appoint another accounting entity at once by a three-fourths resolution, or adjourn 20 to 30 days and appoint by ordinary resolution | `s 205(7)(a) the company may immediately appoint another accounting entity as auditor`; `s 205(7)(b) the company may appoint another accounting entity as auditor at the adjourned meeting` |
| s 205(8) | the Registrar | the company | claim / duty: written notice of the removal immediately; power / liability: the Registrar may appoint an auditor if the company has not appointed one under (7) | `s 205(8) the company is in default of the duty to give written notice of the removal to the Registrar`; `s 205(8) the company must give written notice of the removal to the Registrar`; `s 205(8) the Registrar may appoint an auditor of the company` |
| s 205(9) | none | none | none: a tenure rule (the auditor appointed under (7) or (8) holds office until the next annual general meeting) | none; functions: `s 205(9) the auditor appointed under subsection (7) or (8) holds office` |
| s 205(10) | the Registrar (a member applies in writing) | the directors and the company | power / liability: the Registrar may make the appointment on a member's application | `s 205(10) the Registrar may make the appointment on the application of a member` |
| s 205(11) | none named | an accounting entity | disability: not capable of being appointed auditor at an annual general meeting unless it held office or notice of its nomination was given by a member not less than 21 days before | `s 205(11) the accounting entity is capable of being appointed auditor at the annual general meeting` |
| s 205(12) | the accounting entity nominated; each auditor of the company; each person entitled to notice of general meetings | the company | claim / duty: a copy of the notice of nomination, not less than 7 days before the meeting | `s 205(12) the last day for the company to send a copy of the notice of nomination`; `s 205(12) the company is in default of the duty to send a copy of the notice of nomination`; `s 205(12) the company must send a copy of the notice of nomination` |
| s 205(12A) | none | none | none: a counting rule (the day that stands for the date of the annual general meeting where none is held) | none; functions: `s 205(12A) the day that stands for the date of the annual general meeting` |
| s 205(13) | the accounting entity nominated; the company | any person relying on (11) or (12) | immunity / disability: (11) does not bar the nominee where the meeting is called for 21 days or less after the notice, and the company is deemed to have complied with (12) in the case stated | `s 205(13) subsection (11) does not apply in relation to the accounting entity`; `s 205(13) the company is deemed to have complied with subsection (12)` |
| s 205(14) | none | none | none: deleted by Act 36 of 2014 | none (see the coverage table for the functions) |
| s 205(15) | none | none | none: deleted by Act 36 of 2014 | none (see the coverage table for the functions) |
| s 205(16) | the company in general meeting; the directors; the Registrar | the auditor | power / liability: fixing the auditor's fees and expenses as (a) and (b) provide | `s 205(16) the fees and expenses of the auditor are fixed as the subsection requires` |
| s 205(17) | the State (a public claim; no private holder) | the company and every director of the company who is in default | liability: an offence, with a fine up to the figure the text states | `s 205(17) the person is guilty of the offence`; `s 205(17) the most the person may be fined on conviction` |
| s 205AA(1) | the auditor of a non-public interest company (other than a subsidiary of a public interest company) | the company | power / liability: resign by written notice before the end of the term | `s 205AA(1) the auditor may resign by giving the company a notice of resignation in writing` |
| s 205AA(2) | none | none | none: a counting rule (when the auditor's term of office expires) | none; functions: `s 205AA(2) the day on which the auditor's term of office expires` |
| s 205AA(3) | the Registrar | the company | claim / duty: lodge a notification of the notice of resignation within 14 days beginning on the date of receipt | `s 205AA(3) the last day for the company to lodge the notification`; `s 205AA(3) the company is in default of the duty to lodge the notification`; `s 205AA(3) the company must lodge the notification with the Registrar` |
| s 205AA(4) | none | none | none: definitions ("non-public interest company", "public interest company") | none; functions: `s 205AA(4) "non-public interest company" the company is a non-public interest company` |
| s 205AB(1) | the auditor of a public interest company or a subsidiary of one; the Registrar (consent) | the company | power / liability: resign by written notice if the Registrar has consented | `s 205AB(1) the auditor may resign by giving the company a notice of resignation in writing` |
| s 205AB(2) | the auditor; the company | the Registrar | claim / duty: be notified as soon as practicable whether the Registrar consents | `s 205AB(2) the auditor and the company are to be notified whether the Registrar consents`; `s 205AB(2) the Registrar must notify the auditor and the company whether it consents` |
| s 205AB(3) | the auditor | any person who would use the statement against the auditor | immunity / disability: the statement is not admissible and may not be made the ground of a prosecution, an action or a suit (subject to (4)) | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings`; `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor`; `s 205AB(3) the Registrar's certificate is conclusive evidence that the statement was made in the application or the answer` |
| s 205AB(4) | none named (a party to disciplinary proceedings under the Accountants Act 2004, which is outside the sources) | the auditor | privilege / no-right: the statement may be used in such proceedings despite (3) | `s 205AB(4) the statement may be used in the proceedings` |
| s 205AB(5) | none | none | none: a counting rule (the day the resignation takes effect: whichever of the three days last occurs) | none; functions: `s 205AB(5) the day the resignation takes effect` |
| s 205AC(1) | every member of the company | the company | claim / duty: a copy of the written statement within 14 days after receiving the notice and the statement | `s 205AC(1) the last day for the company to send a copy of the written statement to every member`; `s 205AC(1) the company is in default of the duty to send a copy of the written statement to every member`; `s 205AC(1) the company must send a copy of the written statement to every member` |
| s 205AC(2) | the company; any other person who claims to be aggrieved | every member; the auditor | privilege / no-right (the company need not send copies) on an application to the Court within 14 days beginning on the date of receipt; power / liability: the application | `s 205AC(2) copies of the written statement need not be sent out` |
| s 205AC(3) | the auditor (and the company) | the company that applies; any other person who applies | claim / duty: give notice of the application | `s 205AC(3) the applicant is in default of the duty to give notice of the application`; `s 205AC(3)(a) the company that applies must give notice of the application to the auditor`; `s 205AC(3)(b) any other person who applies must give notice of the application to the company and the auditor` |
| s 205AC(4) | the State | the company and every director who is in default | liability: an offence, with a fine up to the figure the text states | `s 205AC(4) the person is guilty of the offence`; `s 205AC(4) the most the person may be fined on conviction` |
| s 205AD(1) | none | none | none: a scope clause (the section applies if an application has been made under s 205AC(2)) | none; functions: `s 205AD(1) section 205AD applies` |
| s 205AD(2) | the applicant (costs); the company and the members (the direction) | the auditor | power / liability: the Court must direct that copies are not to be sent and may order the auditor to pay costs | `s 205AD(2)(a) the Court is required to direct that copies of the written statement are not to be sent`; `s 205AD(2)(b) the Court may order the auditor to pay the applicant's costs in whole or in part` |
| s 205AD(3) | every member; the auditor (unless a party) | the company | claim / duty: a notice of the effect of the directions within 14 days beginning on the date they are given | `s 205AD(3) the last day for the company to send the notice`; `s 205AD(3) the company is in default of the duty to send a notice setting out the effect of the directions`; `s 205AD(3) the company must send a notice setting out the effect of the directions` |
| s 205AD(4) | the auditor; every member | the company | claim / duty: notice of the decision, and a copy of the statement, within 14 days beginning on the date of the decision or discontinuance | `s 205AD(4) the last day for the company to give notice and send the copies`; `s 205AD(4) the company is in default of the duty to give notice of the decision and send the copies`; `s 205AD(4) the company must give notice of the decision and send the copies` |
| s 205AD(5) | the State | the company and every director who is in default | liability: an offence, with a fine up to the figure the text states | `s 205AD(5) the person is guilty of the offence`; `s 205AD(5) the most the person may be fined on conviction` |
| s 205AE | any person who publishes the written statement as 205AC(1) or 205AD(4)(b) requires | a person who would sue for defamation | immunity / disability: no liability in defamation (in the absence of malice for 205AC(1); without that limit for 205AD(4)(b)) | `s 205AE the person has the privilege against an action for defamation for the publication` |
| s 205AF(1) | the members; the Registrar | the directors of the company | claim / duty: call a general meeting to appoint a new auditor as soon as practicable and in any case within 3 months after the resignation; lodge a notification within 14 days of the appointment | `s 205AF(1)(c) the last day for the directors to call the general meeting`; `s 205AF(1)(c) the directors are in default of the duty to call a general meeting`; `s 205AF(1)(c) the directors must call a general meeting to appoint an auditor in place`; `s 205AF(1)(d) the last day for the directors to lodge the notification`; `s 205AF(1)(d) the directors are in default of the duty to lodge a notification of the appointment`; `s 205AF(1)(d) the directors must lodge a notification of the appointment` |
| s 205AF(2) | the Registrar (a member applies in writing) | the directors and the company | power / liability: the Registrar may make the appointment on a member's application | `s 205AF(2) the Registrar may make the appointment on the application of a member` |
| s 205AF(3) | none | none | none: a scope clause (subsections (1) and (2) do not apply where the statements need not be audited or the resigning auditor is not the sole auditor) | none; functions: `s 205AF(3) subsections (1) and (2) do not apply` |
| s 205AF(4) | none | none | none: a tenure rule (the appointed auditor holds office until the next annual general meeting unless removed or resigning) | none; functions: `s 205AF(4) the auditor appointed under subsection (1) or (2) holds office` |
| s 205AF(5) | the State | the company and every director who is in default | liability: an offence, with a fine up to the figure the text states | `s 205AF(5) the person is guilty of the offence`; `s 205AF(5) the most the person may be fined on conviction` |
| s 205A(1) | a company exempt under s 205B or 205C, and its directors | none named | immunity / disability: exempt from s 205(1) and (2) | `s 205A(1) the company and its directors are exempt from section 205(1) or (2)` |
| s 205A(2) | no claimant is named; enforced through s 205A(3) | the company | duty: appoint auditors before the next annual general meeting once the company ceases to be exempt | `s 205A(2) the last day for the company to appoint an auditor`; `s 205A(2) the company is in default of the duty to appoint an auditor`; `s 205A(2) the company must appoint an auditor before the next annual general meeting`; `s 205A(2) the auditors appointed hold office` |
| s 205A(3) | the State | the company and every director who is in default | liability: an offence, with a fine up to the figure the text states | `s 205A(3) the person is guilty of the offence`; `s 205A(3) the most the person may be fined on conviction` |
| s 205B(1) | a dormant company | none named | immunity / disability: exempt from audit requirements | `s 205B(1) the company is exempt from audit requirements` |
| s 205B(2) | none | none | none: a counting rule (when a company is dormant and ceases to be) | none; functions: `s 205B(2) the company is dormant during the period`; `s 205B(2) the company ceases to be dormant on the transaction` |
| s 205B(3) | none | none | none: a counting rule (transactions that are disregarded) | none; functions: `s 205B(3) helper: the transaction arises from a listed matter`; `s 205B(3) the transaction is to be disregarded` |
| s 205B(4) | the company and its directors (relief from (a) to (c)); the Registrar (the statement in (d)) | the directors (for (d)) | privilege / no-right: copies need not be audited or laid and s 203 is read without the auditor's report; claim / duty: the annual return carries a directors' statement | `s 205B(4)(a) the copies of the financial statements to be sent under section 203 need not be audited`; `s 205B(4)(b) section 203 has effect with the omission of any reference to the auditor's report or a copy of it`; `s 205B(4)(c) copies of an auditor's report need not be laid before the company in a general meeting`; `s 205B(4)(d) the directors are in default of the duty to accompany the annual return with the statement`; `s 205B(4)(d) the directors must accompany the annual return with a statement` |
| s 205B(5) | none | none | none: a status rule (a company that ceases to be dormant ceases to be exempt, but remains exempt for the year in which it was dormant throughout) | none; functions: `s 205B(5) the company ceases to be exempt from audit requirements`; `s 205B(5) the company remains exempt in relation to the accounts for the financial year` |
| s 205B(6) | members holding at least 5% of the shares, of a class, or of the members | the company | power / liability: require an audit of the accounts for the year by written notice not later than one month before the year ends | `s 205B(6) the members may require the company to obtain an audit of its accounts for the year` |
| s 205B(7) | the members who gave the notice | the company | disability: the company is not entitled to the exemption for the year to which the notice relates | `s 205B(7) the company is not entitled to the exemption under subsection (1) in respect of the financial year`; `s 205B(1) and (7) the company is exempt from audit requirements under section 205B for the financial year` |
| s 205B(8) | none | none | none: a definition ("accounting transaction") | none; functions: `s 205B(8) "accounting transaction" the transaction is an accounting transaction` |
| s 205C(1) | a small company | none named | immunity / disability: exempt from audit requirements for the financial year (subject to (3), (4) and (6)) | `s 205C(1) the company is exempt from audit requirements for the financial year` |
| s 205C(2) | members as s 205B(6) states | the small company | power / liability and disability: s 205B(4), (6) and (7) apply to a small company | `s 205C(2) section 205B(4), (6) and (7) apply to the small company`; `s 205C(2) the small company is not entitled to the exemption under subsection (1) in respect of the financial year`; `s 205C(1) and (2) the company is exempt from audit requirements under section 205C for the financial year` |
| s 205C(3) | none | none | none: a limit on (1) for a parent company | none; functions: `s 205C(3) subsection (1) applies to the company as a parent company` |
| s 205C(4) | none | none | none: a limit on (1) for a subsidiary company | none; functions: `s 205C(4) subsection (1) applies to the company as a subsidiary company` |
| s 205C(5) | none | none | none: a definition handed to the Thirteenth Schedule | none; functions: `s 205C(5) "small company" has the meaning given in the Thirteenth Schedule`; `s 205C(5) "small group" has the meaning given in the Thirteenth Schedule` |
| s 205C(6) | no claimant is named | the company and its directors | duty: for a financial year commencing before 1 July 2015, prepare the accounts and lay them under Part VI as it then stood | `s 205C(6) this section applies to the company for the financial year`; `s 205C(6) the company and its directors are in default of the duty to prepare and lay the accounts as the earlier Part VI required` |
| s 205C(7) | the Registrar | the company | claim / duty: attach a copy of those accounts to the return lodged under s 197 | `s 205C(7) the company is in default of the duty to attach a copy of the accounts to the return`; `s 205C(7) the company must attach a copy of the accounts to the return` |
| s 205D | the Registrar | a company exempt under s 205B or 205C | power / liability: require audited financial statements and an auditor's report within a time the notice sets; claim / duty: lodge them | `s 205D the Registrar may require the exempt company to lodge audited financial statements`; `s 205D the company is in default of the requirement in the Registrar's notice`; `s 205D the company must lodge what the Registrar's notice requires` |
| s 206(1) | the members who serve the notice (at least 5% of the members, or holders of 5% of the shares); all persons entitled to receive notice of general meetings | the company | power / liability: serving the notice; claim / duty: the company must immediately prepare, forward and lay a statement of the auditor's other emoluments | `s 206(1) the notice engages the duty of the company`; `s 206(1)(c) the company is in default of the duty to prepare the statement`; `s 206(1)(d) the company is in default of the duty to forward a copy of the statement`; `s 206(1)(e) the company is in default of the duty to lay the statement before the company in general meeting`; `s 206(1)(c) the company must prepare the statement of the auditor's other emoluments`; `s 206(1)(d) the company must forward a copy of the statement` (+1 more in the coverage table) |
| s 206(1A) | all persons entitled to receive notice of general meetings | a public company | claim / duty: review the auditor's fees, expenses and emoluments under prescribed circumstances and send the outcome | `s 206(1A) the duty of the public company to review the auditor's fees applies`; `s 206(1A) the company is in default of the duty to review the auditor's fees and send the outcome`; `s 206(1A) the public company must review the auditor's fees and send the outcome` |
| s 206(2) | the State | the company and every director who is in default | liability: an offence, with a fine up to the figure the text states | `s 206(2) the person is guilty of the offence`; `s 206(2) the most the person may be fined on conviction` |
| s 207(1) | the members | the auditor | claim / duty: report on the financial statements | `s 207(1) the auditor is in default of the duty to report to the members`; `s 207(1) the auditor must report to the members` |
| s 207(1A) | the directors | the auditor | claim / duty: furnish the report in sufficient time for s 203(1); no offence if the directors did not submit the statements in time | `s 207(1A) the auditor is in default of the duty to furnish the report to the directors in sufficient time`; `s 207(1A) the auditor commits no offence under the subsection`; `s 207(1A) the auditor must furnish the report to the directors in sufficient time` |
| s 207(2) | the members | the auditor | claim / duty: state the matters (a), (aa), (b), (d) and (e) in the report | `s 207(2)(a) the auditor is in default of the duty to state the opinions on the financial statements`; `s 207(2)(aa) the auditor is in default of the duty to state whether the non-compliance is necessary for a true and fair view`; `s 207(2)(b) the auditor is in default of the duty to state whether the records have been properly kept`; `s 207(2)(d) the auditor is in default of the duty to state the defect, irregularity or matter`; `s 207(2)(e) the auditor is in default of the duty to state the reasons for not being satisfied` |
| s 207(3) | the members | the auditor | claim / duty: form an opinion on the matters (a) to (e) | `s 207(3) the auditor is in default of the duty to form an opinion on each of the matters`; `s 207(3) the auditor is in default of the duty to state particulars of a deficiency, failure or shortcoming` |
| s 207(4) | the auditor | none named | privilege / no-right: not required to form an opinion on a subsidiary's records as stated | `s 207(4) the auditor is not required to form an opinion on whether the records of the subsidiary corporation have been kept in accordance with this Act` |
| s 207(5) | the auditor | an officer of the company; an auditor of a related company | claim / duty: access at all times to the records and registers; information and explanations | `s 207(5) the auditor has a right of access at all times to the item`; `s 207(5) the auditor is entitled to require information and explanations from the person` |
| s 207(6) | the auditor of a parent company | the subsidiary corporation, its officers and auditors | claim / duty: access to records and information, at the expense of the parent | `s 207(6) the auditor has a right of access at all times to the item of the subsidiary corporation`; `s 207(6) the auditor is entitled, at the expense of the parent company, to require information and explanations from the person` |
| s 207(7) | the members | no one is named (the text is passive) | claim / duty: the report is attached, read on a member's demand and open to inspection | `s 207(7) the report is attached or endorsed, read on a member's request and open to inspection as the subsection requires` |
| s 207(8) | the auditor, or an agent authorised in writing | the company | claim / duty: to attend any general meeting, to receive all notices and communications, and to be heard | `s 207(8) the person is entitled to attend any general meeting of the company`; `s 207(8) the person is entitled to receive all notices of, and other communications relating to, any general meeting which a member is entitled to receive`; `s 207(8) the person is entitled to be heard at the general meeting on the part of the business` |
| s 207(9) | the Registrar | the auditor | claim / duty: report in writing a breach or non-observance, or a circumstance, the subsection describes | `s 207(9) the auditor is in default of the duty to report the matter to the Registrar`; `s 207(9) the auditor must report the matter in writing to the Registrar` |
| s 207(9A) | the Minister | the auditor of a public company or its subsidiary | claim / duty: immediately report a serious offence involving fraud or dishonesty | `s 207(9A) the auditor is in default of the duty to report the matter to the Minister`; `s 207(9A) the auditor must report the matter to the Minister` |
| s 207(9B) | the auditor | any person who would say a duty was contravened | immunity / disability: a good-faith report to the Minister contravenes no duty | `s 207(9B) no duty to which the auditor is subject is regarded as contravened by the report` |
| s 207(9C) | the auditor | the Minister | immunity / disability: no report to the Minister is required if one was made to the Monetary Authority of Singapore | `s 207(9C) the auditor is not required to make a report to the Minister under subsection (9A)` |
| s 207(9D) | none | none | none: a definition ("a serious offence involving fraud or dishonesty") | none; functions: `s 207(9D) the offence is a serious offence involving fraud or dishonesty` |
| s 207(10) | the State | the persons (a) to (d) name | liability: an offence, with a fine up to the figure the text states | `s 207(10) the person is guilty of the offence`; `s 207(10) the most the person may be fined on conviction` |
| s 207(11) | none | none | none: a rule about which registers the references in (5), (6) and (10) cover | none; functions: `s 207(11) the item is excluded from the reference to registers in subsections (5), (6) and (10)` |
| s 208(1) | the auditor | a person who would sue for defamation | immunity / disability: no liability in the absence of malice for a statement made in the course of the auditor's duties | `s 208(1) the auditor is not liable to an action for defamation in respect of the statement` |
| s 208(2) | any person who publishes a document required to be lodged with the Registrar | a person who would sue for defamation | immunity / disability: no liability in the absence of malice | `s 208(2) the person is not liable to an action for defamation in respect of the publication of the document` |
| s 208(3) | none | none | none: a saving (other rights, privileges and immunities are not limited) | none; functions: `s 208(3) section 208 limits or affects the right, privilege or immunity` |
| s 208A(1) | the company (its claim against the auditor stands) | the auditor | immunity / disability: a provision exempting or indemnifying the auditor against liability for negligence, default, breach of duty or breach of trust is void | `s 208A(1) the provision is void` |
| s 208A(2) | the company | none named | privilege / no-right: the company may indemnify the auditor against the costs described in (a) and (b) | `s 208A(2) the section does not prevent the company from indemnifying the auditor`; `s 208A(1) and (2) the provision is void under the section` |
| s 209(1) | every trustee for the holders of debentures | the auditor of a borrowing corporation | claim / duty: send a copy of the statements or documents by post within 7 days after furnishing them | `s 209(1) the last day for the auditor to send a copy to every trustee`; `s 209(1) the auditor is in default of the duty to send a copy to every trustee`; `s 209(1) the auditor must send a copy to every trustee within 7 days` |
| s 209(2) | the borrowing corporation; the trustee | the auditor | claim / duty: send a written report of a relevant matter within 7 days after becoming aware of it | `s 209(2) the last day for the auditor to send the report`; `s 209(2) the auditor is in default of the duty to send the report`; `s 209(2) the auditor must send the report within 7 days` |
| s 209(3) | the State | any person who fails to comply with (2) | liability: an offence, with a fine up to the figure the text states and a default penalty | `s 209(3) the person is guilty of the offence`; `s 209(3) the most the person may be fined on conviction`; `s 209(3) the person is also liable on conviction to a default penalty` |
| s 209A | none | none | none: definitions ("balance sheet", "consolidated financial statements", "consolidated total assets", "directors' statement", "entity", "financial statements", "group", "parent company", "subsidiary company", "subsidiary corporation", "ultimate parent corporation") | none; functions: `s 209A the definitions of this section apply in this Part` |
| s 209B | none | none | none: repealed by Act 5 of 2004 | none (see the coverage table for the functions) |
| Sch 13 para 1 | none | none | none: a definition clause (small company and small group for s 205C) | none; functions: `sch 13 para 1(a) the company is a small company for the financial year`; `sch 13 para 1(b) the group is a small group for the financial year` |
| Sch 13 para 2 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 2 the company qualifies as a small company from the financial year`; `sch 13 para 2(b) the company qualifies as a small company from the financial year (other reading: the same 2 criteria in both years)`; `sch 13 para 2(b)(i) the revenue for the financial year does not exceed $10 million` (+4 more) |
| Sch 13 para 3 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 3 the company qualifies as a small company from the financial year` |
| Sch 13 para 4 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 4 the company qualifies as a small company from the financial year` |
| Sch 13 para 5 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 5 the company ceases to be a small company from the financial year`; `sch 13 para 5(b) the company fails to satisfy any 2 of the criteria in either of the 2 preceding financial years (other reading)` |
| Sch 13 para 6 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 6 paragraph 5 does not apply to the company` |
| Sch 13 para 7 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 7 the group qualifies as a small group from the financial year` |
| Sch 13 para 8 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 8 the group qualifies as a small group from the financial year` |
| Sch 13 para 9 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 9 the group qualifies as a small group from the financial year` |
| Sch 13 para 10 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 10 the group ceases to be a small group from the financial year`; `sch 13 para 10 the group fails to satisfy any 2 of the criteria in either of the 2 preceding financial years (other reading)` |
| Sch 13 para 11 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 11 paragraph 10 does not apply to the group` |
| Sch 13 para 12 | none | none | none: counting rules (whether an entity is part of a group; how consolidated figures are found; the meaning of "parent") | none; functions: `sch 13 para 12(a) the entity is part of the group`; `sch 13 para 12(b) the consolidated total assets of the group, in Singapore dollars`; `sch 13 para 12(b) the consolidated revenue of the group, in Singapore dollars` (+1 more) |
| Sch 13 para 13 | none | none | none: a counting rule (what "from a financial year" means) | none; functions: `sch 13 para 13(a) the company is a small company for the later financial year`; `sch 13 para 13(b) the group is a small group for the later financial year` |
| Sch 13 para 14 | none | none | none: a counting rule that decides small-company or small-group status, which s 205C(1) turns into the exemption | none; functions: `sch 13 para 14(a) the company may become a small company again`; `sch 13 para 14(b) the group may become a small group again` |

## Marginal readings for a lawyer (sgc2)

The brief's rule of 2026-10-29 leaves two readings for a lawyer to settle, and tells me to take them as the status quo and list every branch that rests on one:

- **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"); flat negatives count as the text saying no.
  Other reading: a failed "if" leaves the case unanswered, so the branch answers `NOTHING`; a flat negative states a prohibition and the function answers `NOTHING`.
- **(b)** a prohibition or grant limited by its own wording does not count as the text's no: the branch answers `NOTHING`.
  Other reading: the limit is itself the text's no, and the branch answers `JUST FALSE`.

The table below is generated by `work/branches.py` from the `-- FALSE-kind` and `-- NOTHING-kind` tags in the layer-1 files; each row is one branch, located by file and line.
A `JUST FALSE` branch is listed as (a) when its tag names an "if" gate, a "where" gate, a "not met", a flat negative, a bar or an "unless"; a `NOTHING` branch is listed as (b) when its tag says "limited by its own wording".
Branches that rest on something else are not repeated here: a "means" definition (the text says no in so many words), a duty or an offence element (fork entries F-D1 and F-E1), a period the text fixes (F-P1), a delegated definition (Guide section 5, the ruling of 2026-11-05, item (a)), and a `NOTHING` for "silent", "list not closed" or "points outside the text".

**111 branches in all: 50 rest on reading (a) and 61 on reading (b)**, in 76 functions.

| Provision | Function | Where | Reading | Answer taken | Other reading |
| --- | --- | --- | --- | --- | --- |
| s 205(1) | `s 205(1) the auditor appointed by the directors holds office` | s205-appointment:90 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(2) | `s 205(2) the auditor appointed at the annual general meeting holds office` | s205-appointment:137 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(3) | `s 205(3) the directors may appoint the accounting entity to fill the casual vacancy` | s205-appointment:159 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(3) | `s 205(3) the surviving or continuing auditor may act` | s205-appointment:173 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(5)(b) | `s 205(5)(b) the auditor may make representations and have a copy sent to every member` | s205-appointment:249 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(6) | `s 205(6) the auditor may require that the representations be read out at the meeting` | s205-appointment:298 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(6) | `s 205(6) the auditor may require that the representations be read out at the meeting` | s205-appointment:301 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(7)(a) | `s 205(7)(a) the company may immediately appoint another accounting entity as auditor` | s205-appointment:325 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(7)(a) | `s 205(7)(a) the company may immediately appoint another accounting entity as auditor` | s205-appointment:329 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(7)(b) | `s 205(7)(b) the company may appoint another accounting entity as auditor at the adjourned meeting` | s205-appointment:351 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(7)(b) | `s 205(7)(b) the company may appoint another accounting entity as auditor at the adjourned meeting` | s205-appointment:359 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(8) | `s 205(8) the Registrar may appoint an auditor of the company` | s205-appointment:399 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(9) | `s 205(9) the auditor appointed under subsection (7) or (8) holds office` | s205-appointment:412 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(10) | `s 205(10) the Registrar may make the appointment on the application of a member` | s205-appointment:429 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(11) | `s 205(11) the accounting entity is capable of being appointed auditor at the annual general meeting` | s205-appointment:448 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(11) | `s 205(11) the accounting entity is capable of being appointed auditor at the annual general meeting` | s205-appointment:453 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(12A) | `s 205(12A) the day that stands for the date of the annual general meeting` | s205-appointment:547 | (b) | `NOTHING` | `JUST FALSE` |
| s 205(13) | `s 205(13) subsection (11) does not apply in relation to the accounting entity` | s205-appointment:570 | (a) | `JUST FALSE` | `NOTHING` |
| s 205(13) | `s 205(13) the company is deemed to have complied with subsection (12)` | s205-appointment:583 | (a) | `JUST FALSE` | `NOTHING` |
| s 205A(1) | `s 205A(1) the company and its directors are exempt from section 205(1) or (2)` | s205a-exemption:47 | (b) | `NOTHING` | `JUST FALSE` |
| s 205A(2) | `s 205A(2) the auditors appointed hold office` | s205a-exemption:97 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(1) | `s 205B(1) the company is exempt from audit requirements` | s205a-exemption:153 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(4)(a) | `s 205B(4)(a) the copies of the financial statements to be sent under section 203 need not be audited` | s205a-exemption:246 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(4)(b) | `s 205B(4)(b) section 203 has effect with the omission of any reference to the auditor's report or a copy of it` | s205a-exemption:256 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(4)(c) | `s 205B(4)(c) copies of an auditor's report need not be laid before the company in a general meeting` | s205a-exemption:266 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(5) | `s 205B(5) the company ceases to be exempt from audit requirements` | s205a-exemption:317 | (a) | `JUST FALSE` | `NOTHING` |
| s 205B(5) | `s 205B(5) the company remains exempt in relation to the accounts for the financial year` | s205a-exemption:325 | (b) | `NOTHING` | `JUST FALSE` |
| s 205B(6) | `s 205B(6) the members may require the company to obtain an audit of its accounts for the year` | s205a-exemption:361 | (b) | `NOTHING` | `JUST FALSE` |
| s 205B(7) | `s 205B(7) the company is not entitled to the exemption under subsection (1) in respect of the financial year` | s205a-exemption:376 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(1) | `s 205C(1) the company is exempt from audit requirements for the financial year` | s205a-exemption:406 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(1) | `s 205C(1) the company is exempt from audit requirements for the financial year` | s205a-exemption:408 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(1) | `s 205C(1) the company is exempt from audit requirements for the financial year` | s205a-exemption:410 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(1) | `s 205C(1) the company is exempt from audit requirements for the financial year` | s205a-exemption:413 | (b) | `NOTHING` | `JUST FALSE` |
| s 205C(2) | `s 205C(2) section 205B(4), (6) and (7) apply to the small company` | s205a-exemption:425 | (b) | `NOTHING` | `JUST FALSE` |
| s 205C(2) | `s 205C(2) the small company is not entitled to the exemption under subsection (1) in respect of the financial year` | s205a-exemption:433 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(3) | `s 205C(3) subsection (1) applies to the company as a parent company` | s205a-exemption:461 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(3) | `s 205C(3) subsection (1) applies to the company as a parent company` | s205a-exemption:462 | (b) | `NOTHING` | `JUST FALSE` |
| s 205C(4) | `s 205C(4) subsection (1) applies to the company as a subsidiary company` | s205a-exemption:475 | (a) | `JUST FALSE` | `NOTHING` |
| s 205C(4) | `s 205C(4) subsection (1) applies to the company as a subsidiary company` | s205a-exemption:476 | (b) | `NOTHING` | `JUST FALSE` |
| s 205C(6) | `s 205C(6) this section applies to the company for the financial year` | s205a-exemption:505 | (a) | `JUST FALSE` | `NOTHING` |
| s 205D | `s 205D the Registrar may require the exempt company to lodge audited financial statements` | s205a-exemption:571 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AA(1) | `s 205AA(1) the auditor may resign by giving the company a notice of resignation in writing` | s205aa-resignation:78 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AA(1) | `s 205AA(1) the auditor may resign by giving the company a notice of resignation in writing` | s205aa-resignation:81 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(1) | `s 205AB(1) the auditor may resign by giving the company a notice of resignation in writing` | s205aa-resignation:166 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(1) | `s 205AB(1) the auditor may resign by giving the company a notice of resignation in writing` | s205aa-resignation:174 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(a) | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings` | s205aa-resignation:217 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AB(3)(a) | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings` | s205aa-resignation:219 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(a) | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings` | s205aa-resignation:220 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(a) | `s 205AB(3)(a) the statement is admissible in evidence in the proceedings` | s205aa-resignation:221 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(b) | `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor` | s205aa-resignation:232 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AB(3)(b) | `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor` | s205aa-resignation:234 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(b) | `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor` | s205aa-resignation:235 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(3)(b) | `s 205AB(3)(b) the statement may be made the ground of a prosecution, an action or a suit against the auditor` | s205aa-resignation:236 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(4) | `s 205AB(4) the statement may be used in the proceedings` | s205aa-resignation:259 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(4) | `s 205AB(4) the statement may be used in the proceedings` | s205aa-resignation:260 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AB(4) | `s 205AB(4) the statement may be used in the proceedings` | s205aa-resignation:261 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AC(2) | `s 205AC(2) copies of the written statement need not be sent out` | s205aa-resignation:352 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AD(1) | `s 205AD(1) section 205AD applies` | s205aa-resignation:426 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AD(2) | `s 205AD(2)(a) the Court is required to direct that copies of the written statement are not to be sent` | s205aa-resignation:446 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AD(2)(b) | `s 205AD(2)(b) the Court may order the auditor to pay the applicant's costs in whole or in part` | s205aa-resignation:455 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AE | `s 205AE the person has the privilege against an action for defamation for the publication` | s205aa-resignation:591 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AE | `s 205AE the person has the privilege against an action for defamation for the publication` | s205aa-resignation:593 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AF(2) | `s 205AF(2) the Registrar may make the appointment on the application of a member` | s205aa-resignation:699 | (b) | `NOTHING` | `JUST FALSE` |
| s 205AF(3) | `s 205AF(3) subsections (1) and (2) do not apply` | s205aa-resignation:712 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AF(4) | `s 205AF(4) the auditor appointed under subsection (1) or (2) holds office` | s205aa-resignation:723 | (a) | `JUST FALSE` | `NOTHING` |
| s 205AF(4) | `s 205AF(4) the auditor appointed under subsection (1) or (2) holds office` | s205aa-resignation:725 | (a) | `JUST FALSE` | `NOTHING` |
| s 206(1) | `s 206(1) the notice engages the duty of the company` | s206-208a-duties:100 | (a) | `JUST FALSE` | `NOTHING` |
| s 207(4) | `s 207(4) the auditor is not required to form an opinion on whether the records of the subsidiary corporation have been kept in accordance with this Act` | s206-208a-duties:472 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(5) | `s 207(5) the auditor has a right of access at all times to the item` | s206-208a-duties:510 | (a) | `JUST FALSE` | `NOTHING` |
| s 207(5) | `s 207(5) the auditor has a right of access at all times to the item` | s206-208a-duties:512 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(5) | `s 207(5) the auditor is entitled to require information and explanations from the person` | s206-208a-duties:532 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(5) | `s 207(5) the auditor is entitled to require information and explanations from the person` | s206-208a-duties:534 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(6) | `s 207(6) the auditor has a right of access at all times to the item of the subsidiary corporation` | s206-208a-duties:554 | (a) | `JUST FALSE` | `NOTHING` |
| s 207(6) | `s 207(6) the auditor has a right of access at all times to the item of the subsidiary corporation` | s206-208a-duties:556 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(6) | `s 207(6) the auditor is entitled, at the expense of the parent company, to require information and explanations from the person` | s206-208a-duties:569 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(8) | `s 207(8) the person is entitled to attend any general meeting of the company` | s206-208a-duties:610 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(8) | `s 207(8) the person is entitled to receive all notices of, and other communications relating to, any general meeting which a member is entitled to receive` | s206-208a-duties:619 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(8) | `s 207(8) the person is entitled to be heard at the general meeting on the part of the business` | s206-208a-duties:631 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(8) | `s 207(8) the person is entitled to be heard at the general meeting on the part of the business` | s206-208a-duties:632 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(9C) | `s 207(9C) the auditor is not required to make a report to the Minister under subsection (9A)` | s206-208a-duties:709 | (b) | `NOTHING` | `JUST FALSE` |
| s 207(9B) | `s 207(9B) no duty to which the auditor is subject is regarded as contravened by the report` | s206-208a-duties:760 | (b) | `NOTHING` | `JUST FALSE` |
| s 208(1) | `s 208(1) the auditor is not liable to an action for defamation in respect of the statement` | s206-208a-duties:864 | (b) | `NOTHING` | `JUST FALSE` |
| s 208(2) | `s 208(2) the person is not liable to an action for defamation in respect of the publication of the document` | s206-208a-duties:880 | (b) | `NOTHING` | `JUST FALSE` |
| s 208(3) | `s 208(3) section 208 limits or affects the right, privilege or immunity` | s206-208a-duties:891 | (a) | `JUST FALSE` | `NOTHING` |
| s 208A(1) | `s 208A(1) the provision is void` | s206-208a-duties:915 | (b) | `NOTHING` | `JUST FALSE` |
| s 208A(2) | `s 208A(2) the section does not prevent the company from indemnifying the auditor` | s206-208a-duties:938 | (b) | `NOTHING` | `JUST FALSE` |
| s 208A(2) | `s 208A(1) and (2) the provision is void under the section` | s206-208a-duties:947 | (a) | `JUST FALSE` | `NOTHING` |
| s 209A | `s 209A the definitions of this section apply in this Part` | s209-interpretation:156 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 2 | `sch 13 para 2 the company qualifies as a small company from the financial year` | sch13-small:109 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 2 | `sch 13 para 2(b) the company qualifies as a small company from the financial year (other reading: the same 2 criteria in both years)` | sch13-small:124 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 3 | `sch 13 para 3 the company qualifies as a small company from the financial year` | sch13-small:164 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 3 | `sch 13 para 3 the company qualifies as a small company from the financial year` | sch13-small:165 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 4 | `sch 13 para 4 the company qualifies as a small company from the financial year` | sch13-small:208 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 4 | `sch 13 para 4 the company qualifies as a small company from the financial year` | sch13-small:209 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 5 | `sch 13 para 5 the company ceases to be a small company from the financial year` | sch13-small:260 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 5 | `sch 13 para 5 the company ceases to be a small company from the financial year` | sch13-small:262 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 5 | `sch 13 para 5 the company ceases to be a small company from the financial year` | sch13-small:267 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 13(a) | `sch 13 para 13(a) the company is a small company for the later financial year` | sch13-small:326 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 13(a) | `sch 13 para 13(a) the company is a small company for the later financial year` | sch13-small:328 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 14(a) | `sch 13 para 14(a) the company may become a small company again` | sch13-small:341 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 7 | `sch 13 para 7 the group qualifies as a small group from the financial year` | sch13-small:365 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 8 | `sch 13 para 8 the group qualifies as a small group from the financial year` | sch13-small:392 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 8 | `sch 13 para 8 the group qualifies as a small group from the financial year` | sch13-small:393 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 9 | `sch 13 para 9 the group qualifies as a small group from the financial year` | sch13-small:424 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 9 | `sch 13 para 9 the group qualifies as a small group from the financial year` | sch13-small:425 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 10 | `sch 13 para 10 the group ceases to be a small group from the financial year` | sch13-small:466 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 10 | `sch 13 para 10 the group ceases to be a small group from the financial year` | sch13-small:468 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 10 | `sch 13 para 10 the group ceases to be a small group from the financial year` | sch13-small:472 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 13(b) | `sch 13 para 13(b) the group is a small group for the later financial year` | sch13-small:580 | (a) | `JUST FALSE` | `NOTHING` |
| sch 13 para 13(b) | `sch 13 para 13(b) the group is a small group for the later financial year` | sch13-small:582 | (b) | `NOTHING` | `JUST FALSE` |
| sch 13 para 14(b) | `sch 13 para 14(b) the group may become a small group again` | sch13-small:594 | (b) | `NOTHING` | `JUST FALSE` |

### Sites that fit none of the Guide's lines

The brief says that a site that fits none of the Guide's lines is to say so in its fork line and be listed here.
Two kinds of branch of split site (i) are such sites, and both answer `JUST FALSE` (other reading: `NOTHING`):

- s205-appointment:655, `s 205(17) the person is guilty of the offence`: a person outside the class the text names.
- s205aa-resignation:403, `s 205AC(4) the person is guilty of the offence`: a person outside the class the text names.
- s205aa-resignation:556, `s 205AD(5) the person is guilty of the offence`: a person outside the class the text names.
- s205aa-resignation:741, `s 205AF(5) the person is guilty of the offence`: a person outside the class the text names.
- s205a-exemption:113, `s 205A(3) the person is guilty of the offence`: a person outside the class the text names.
- s206-208a-duties:222, `s 206(2) the person is guilty of the offence`: a person outside the class the text names.
- s206-208a-duties:808, `s 207(10) the person is guilty of the offence`: an officer or auditor who does not do what the paragraph describes.
- s206-208a-duties:818, `s 207(10) the person is guilty of the offence`: an officer or auditor who does not do what the paragraph describes.
- s206-208a-duties:827, `s 207(10) the person is guilty of the offence`: an officer or auditor who does not do what the paragraph describes.
- s206-208a-duties:835, `s 207(10) the person is guilty of the offence`: an officer or auditor who does not do what the paragraph describes.

### Reading a result: FALSE and NOTHING (sgc2)

A decision function here answers `JUST TRUE`, `JUST FALSE` or `NOTHING` (a `MAYBE`-wrapped `BOOLEAN`; a `MAYBE NUMBER` or `MAYBE DATE` where the answer is a sum or a day).

- **`JUST FALSE`: the Act says no in its own words.**
  In this Part that means: a "means" definition ("public interest company" is a company listed or issuing instruments on an approved exchange, or one the Minister prescribes, and no other); an "if", "where" or "unless" the text introduces and the facts do not meet (a company that has not been dormant is not exempt under s 205B(1); a company outside the 205C(6) date is outside s 205C); a flat negative ("does not limit or affect", "is not entitled", "may not be made the ground of a prosecution"); a closed meaning (a transaction that is not an accounting transaction, or that s 205B(3) disregards, is not "such a transaction" in s 205B(2)); a period the text fixes (a representation made after the 7 days of s 205(5)(b) is not within them).
  For the functions named "... is in default of the duty ...", `JUST FALSE` has three causes, none of them "the Act says the person is innocent": the act was done in time, the time is still running, or the duty did not arise on these facts (fork entry F-D1, the provision's own question).
  For the offence functions ("... is guilty of the offence"), `JUST FALSE` means an element of the offence is not met on these facts (split site (i), fork entry F-E1), not that the person is cleared.
- **`NOTHING`: the Act does not answer.**
  It is silent; it lists without closing the list; it points outside the sources (the Accounting Standards, Part VI before 1 July 2015, the amounts the Minister or the Registrar prescribes, the default penalty of s 408); or it limits a grant or a scope in its own wording and the case falls outside (s 205(10) says what the Registrar may do on a member's application and does not say that the Registrar may not otherwise; s 205C(1) does not say that a company that is not small is non-exempt, and a dormant company is exempt under s 205B).
  `NOTHING` is not "no".
  A caller must never turn `NOTHING` into `FALSE`.
  The one place this module does turn it into a `BOOLEAN` is the seam to s 7A(2) of the keel (`## Seams (sgc2)`), and the comment above that function says so.
- **A period.** A last day is a date; a duty with a last day is a rule with `WITHIN`, and its "in default" function is the same question asked at a given day.
  Where the text gives no number (the duty is "immediately", or "as soon as practicable", or has no time at all), no deadline is invented: the rule is written, traced, and listed under `## Rules with no breach path (sgc2)`.
- **A seat answer is the layer-1 answer.** The seat's `HOW TO READ AN ANSWER` paragraph says this in the person's words, and each of its 66 questions keeps the direction of the function it calls.

## Seams (sgc2)

Seams are named as `inputs/PLAN.md` section 4 names them.
Where this part takes another part's answer as an input, the input has the name and the type the plan gives.

**Given by this part**

1. To s 7A(2) of `sg-solvency` (PLAN 4.A, "s 7A(2) `sg-solvency` | s 205B, s 205C (sgc2)"): `the company is exempt from audit requirements under section 205B or 205C` (BOOLEAN).
   Given by `s 205B and 205C the company is exempt from audit requirements under section 205B or 205C` in `sgc2-s205a-exemption.l4`, which takes the two answers `s 205B(1) and (7) ...` and `s 205C(1) and (2) ...` (each a `MAYBE BOOLEAN`) and returns `TRUE` when either is `JUST TRUE`.
   **Silent conversion.** Any other answer, `NOTHING` included, becomes `FALSE`, because the keel's input is a plain `BOOLEAN`; `s 205C(1)` answers `NOTHING` for a company that is not small (F-S4), so the seam's `FALSE` means "not shown exempt under s 205B or s 205C", not "the text says the company is not exempt".
   (The comment above the function said that neither answer could be `NOTHING`; that was wrong, and it was corrected, in the template and the expanded file, near the end of this run. The function and its tests were right: `sgc2-tests-s205a.l4` asserts `NOTHING` and `JUST FALSE` give `FALSE`.)
2. To s 4(1) "audit requirements" (PLAN 4.A, "s 201(8), (9) (sgc1); s 207 (sgc2)"): the plan asks this part for "the s 207 requirement fact", the keel's input `the requirement is a requirement of section 207` (BOOLEAN, `sg-definitions.l4` line 231).
   **Not coded, on purpose.** The input says which section a requirement comes from; it is a classification a caller makes of a requirement it already holds, and no fact in the Act computes it.
   The requirements of s 207 are stated by the functions under s 207 in `sgc2-s206-208a-duties.l4`; a caller answers `TRUE` for a requirement that one of those functions states.

**Taken by this part**

3. From the keel's s 6 (PLAN 4.B, "sgc2 line 19911 (the auditor of a company deemed related to the company)"): `s 6 the corporations are deemed to be related to each other`, called in `s 207(5) the auditor is entitled to require information and explanations from the person` for "any auditor of a company that is deemed to be related to the company by virtue of section 6".
   `sgc2-s206-208a-duties.l4` imports `sg-groups` for it.
4. From the keel's s 10 (the plan's row for sgc2: "Takes: the s 10 functions"): **not taken.**
   Who may be an auditor is the keel's (s 10); s 205 asks only that "the person or firm appointed is an accounting entity", and that is a plain `BOOLEAN` input named for the fact (`the person or firm to be appointed is an accounting entity`).
   A caller that wants s 10's answer calls `sg-auditors.l4` and passes the result as that input.
5. From the keel's s 4(1) "borrowing corporation" and "default penalty": **not taken.**
   `sgc2-s209-interpretation.l4` asks `the corporation is a borrowing corporation` as a plain `BOOLEAN`; s 209(3)'s default penalty is s 408's, whose amount is not among the sources: the module answers the fine (`$1,000`) and whether the default penalty applies (`s 209(3) the person is also liable on conviction to a default penalty`), not the penalty's amount.
6. From the Accounting Standards (not a source): the Schedule's `the entity is part of a group within the Accounting Standards`, `the entity is a parent within the Accounting Standards` and `the entity is a subsidiary of any other entity within the Accounting Standards` (plain `BOOLEAN`s) and s 209A's terms defined by reference to the Accounting Standards.
7. Between the Schedule and s 205C (a seam inside this part): s 205C(1) takes `the company is a small company in respect of the financial year` and `the company is part of a small group` as plain `BOOLEAN`s; the seat's question under s 205C asks the two conclusions of the Schedule as plain inputs, and the Schedule's own questions compute them.

**Seams the plan lacks**

8. The Thirteenth Schedule is headed "Sections 8(7) and 205C(5)" (lines 29013-29017): two sections hand their meanings to it.
   The Schedule is encoded here once, for s 205C; s 8(7) is in another part's range, and that part can take `sch 13 para 1(a) the company is a small company for the financial year` and `sch 13 para 1(b) the group is a small group for the financial year` from this one by name once the parts merge.
9. s 205B(3)(fb) (the most that may be prescribed as a nominal sum, a number) and (g) (another prescribed matter, a `BOOLEAN`), s 206(1A) ("under prescribed circumstances"), s 205AA(4) ("such other company as the Minister may prescribe") and s 205C(6) (Part VI as in force before 1 July 2015) hand a figure, a class or a rule to a power or an instrument outside the sources.
   Each is a plain input named for the fact; nothing is guessed.

## Split sites (sgc2)

The brief leaves two questions to each part, to be recorded site by site without harmonising with other parts.
I counted the sites by reading the layer-1 files for the two patterns, and each site's fork line names the line of `inputs/ENCODING-GUIDE.md` section 5, or the dated ruling in it, that the answer relies on.

### (i) An unmet element of an offence or a contravention

**8 sites, answer taken at every one: `JUST FALSE`** (17 branches in all).
The sites are the eight functions named "... the person is guilty of the offence", in ss 205(17), 205A(3), 205AC(4), 205AD(5), 205AF(5), 206(2), 207(10) and 209(3).
The first six share the person type `s 205(17) person charged` (`sgc2-common.l4`).
Each has a companion function for the fine ("the most the person may be fined on conviction"), which answers `NOTHING` where the person is not guilty (the subsection states a penalty only for the persons it makes guilty).

Fork lines, one per site (the provision, the function, the answer taken, the other reading, the Guide line relied on):

- **s 205(17)**, `s 205(17) the person is guilty of the offence` (branches at s205-appointment:655, s205-appointment:656). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 205AC(4)**, `s 205AC(4) the person is guilty of the offence` (branches at s205aa-resignation:403, s205aa-resignation:404). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 205AD(5)**, `s 205AD(5) the person is guilty of the offence` (branches at s205aa-resignation:556, s205aa-resignation:557). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 205AF(5)**, `s 205AF(5) the person is guilty of the offence` (branches at s205aa-resignation:741, s205aa-resignation:742). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 205A(3)**, `s 205A(3) the person is guilty of the offence` (branches at s205a-exemption:113, s205a-exemption:114). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 206(2)**, `s 206(2) the person is guilty of the offence` (branches at s206-208a-duties:222, s206-208a-duties:223). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ..." (for "If default is made ..." / "If any person fails ..."), and "Questions with no convention: decide case by case" ("a duty whose \"if\" or \"where\" is unmet"); for the class of persons, none fits (see the next heading).
- **s 207(10)**, `s 207(10) the person is guilty of the offence` (branches at s206-208a-duties:808, s206-208a-duties:818, s206-208a-duties:827, s206-208a-duties:835). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: none of the Guide's lines fits ("who refuses or fails without lawful excuse ..." is an element the text names, not an "if" and not a flat negative); listed under `## Marginal readings for a lawyer (sgc2)`.
- **s 209(3)**, `s 209(3) the person is guilty of the offence` (branches at s209-interpretation:127). Answer taken: `JUST FALSE`. Other reading: `NOTHING`. Guide: the "In short" line, "a condition the text introduces with \"if\" ...".

The Guide line relied on where the text says "If default is made ..." or "If any person fails ...": Guide section 5, the "In short" line, "a condition the text introduces with \"if\", \"only if\", \"as long as\" or \"unless\"" (the offence is introduced by an "if", and the function answers `JUST FALSE` where the "if" is not met), and "Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z)", which names "a duty whose \"if\" or \"where\" is unmet".
Where the branch is the class of persons ("the company and every director of the company who is in default"; the persons of s 207(10)(a) to (d)), the answer fits none of the Guide's lines (the text names its persons and does not close the class with "only"); that is said in the fork line and the branch is listed under `## Marginal readings for a lawyer (sgc2)`.

### (ii) A "may" (or a relief) gated by "where", "when", "upon", "on application" and the like

**7 sites: 5 answered `JUST FALSE`, 2 answered `NOTHING`.**
Three more functions are gated by "where" and answer `JUST FALSE` for the same reason, but they are not "may" functions (s 205B(5), s 205B(7), s 205C(2)); they are in fork entry F-W1 and are not counted as sites.

- **s 205(7)(a)**, `s 205(7)(a) the company may immediately appoint another accounting entity as auditor`. Answer: `JUST FALSE` where no auditor was removed under s 205(4) at a general meeting ("Where an auditor of a company is removed from office pursuant to subsection (4) at a general meeting of the company"). Other reading: `NOTHING`. Guide: the periods ruling of 2026-11-05, item (b): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`" (the maintainer: "i agree with your lean: no for a and b; nothing for c"), and the grant ruling of 2026-11-12, limit 3, which leaves a "may" whose gate is "where" "for the maintainer or a lawyer". The three-fourths majority and "another accounting entity nominated at the meeting" are named complements of the grant: that limb answers `NOTHING` (F-G1).
- **s 205(7)(b)**, `s 205(7)(b) the company may appoint another accounting entity as auditor at the adjourned meeting`. The same "Where" gate, the same answer and the same Guide lines. The two periods in the paragraph (20 to 30 days after the meeting; 10 days before the resumption) are periods the text fixes, `JUST FALSE` outside them (the periods ruling, item (a); F-P1).
- **s 205B(4)(a)**, `... the copies of the financial statements to be sent under section 203 need not be audited`. Answer: `JUST FALSE` where the company is not, at the end of the financial year, exempt under subsection (1) ("Where a company is, at the end of a financial year, exempt from audit requirements under subsection (1)"). Other reading: `NOTHING`. Guide: the periods ruling, item (b), and grant ruling limit 3, as above.
- **s 205B(4)(b)**, `... section 203 has effect with the omission of any reference to the auditor's report or a copy of it`. Same gate, answer and Guide lines.
- **s 205B(4)(c)**, `... copies of an auditor's report need not be laid before the company in a general meeting`. Same gate, answer and Guide lines.
- **s 205(10)**, `s 205(10) the Registrar may make the appointment on the application of a member`. Answer: `NOTHING` where the directors have appointed, or no member has applied in writing ("If the directors do not appoint an auditor or auditors as required by this section, the Registrar may on the application in writing of any member of the company make the appointment"). Other reading: `JUST FALSE`. Guide: the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed"; the text does not close the gate with "only".
- **s 205AF(2)**, `s 205AF(2) the Registrar may make the appointment on the application of a member`. Answer: `NOTHING` where the directors have appointed or no member has applied ("If the directors of a company fail to appoint an auditor in place of the auditor who desires to resign or has resigned, the Registrar may, on the application in writing of any member of the company, make the appointment"). Other reading: `JUST FALSE`. Guide: the grant ruling, limit 1, as for s 205(10).

Not counted as sites: the other "may" functions of this part (s 205(3), 205(5)(b), 205(6), 205(8), 205AA(1), 205AB(1), 205AD(2)(b), 205B(6), 205D and Sch 13 para 14), whose gate is an "if" or a named complement, not one of the gates the brief names.
They answer `NOTHING` by the grant ruling's limit 1 where the "if" or the complement fails (fork entry F-G1), and `JUST FALSE` for a period the text fixes (F-P1).

## Rules with no breach path (sgc2)

29 regulative rules are written in layer 1; 12 have a number of days (`WITHIN`) and each of those has at least one `#TRACE` that reaches `BREACH`; **17 have no number of days, so no trace can show them breached** (a late act still reads `FULFILLED`).
They are listed here with the provision and the words of the text; no deadline or consequence is invented.
Each is still written as a rule and traced (to `FULFILLED`, and to `RESIDUAL` where the duty can still be open), and has a decision function that answers the same question.

| Provision | Rule | Why no deadline can be missed |
| --- | --- | --- |
| s 205(2) | `s 205(2) the company must appoint an auditor at each annual general meeting` | no time limit: "at each annual general meeting" names an event, not a number of days |
| s 205(5)(a) | `s 205(5)(a) the company must send a copy of the notice of the removal resolution` | "it must immediately send a copy of the notice" |
| s 205(6) | `s 205(6) the company must send a copy of the representations` | no time limit |
| s 205(8) | `s 205(8) the company must give written notice of the removal to the Registrar` | "immediately after the removal of an auditor" |
| s 205AB(2) | `s 205AB(2) the Registrar must notify the auditor and the company whether it consents` | "as soon as practicable after receiving the application" (the Registrar's duty) |
| s 205AC(3) | `s 205AC(3)(a) the company that applies must give notice of the application to the auditor` | no time limit |
| s 205AC(3) | `s 205AC(3)(b) any other person who applies must give notice of the application to the company and the auditor` | no time limit |
| s 205B(4)(d) | `s 205B(4)(d) the directors must accompany the annual return with a statement` | no time limit (the statement accompanies the annual return) |
| s 205C(7) | `s 205C(7) the company must attach a copy of the accounts to the return` | no time limit ("when lodging a return") |
| s 206(1)(c) | `s 206(1)(c) the company must prepare the statement of the auditor's other emoluments` | "the company must immediately" |
| s 206(1)(d) | `s 206(1)(d) the company must forward a copy of the statement` | "the company must immediately" |
| s 206(1)(e) | `s 206(1)(e) the company must lay the statement before the company in general meeting` | "the company must immediately" |
| s 206(1A) | `s 206(1A) the public company must review the auditor's fees and send the outcome` | no time limit ("under prescribed circumstances") |
| s 207(1) | `s 207(1) the auditor must report to the members` | no time limit |
| s 207(1A) | `s 207(1A) the auditor must furnish the report to the directors in sufficient time` | "in sufficient time to enable the company to comply with ... section 203(1)": no number |
| s 207(9) | `s 207(9) the auditor must report the matter in writing to the Registrar` | "the auditor must immediately report the matter in writing to the Registrar" |
| s 207(9A) | `s 207(9A) the auditor must report the matter to the Minister` | "the auditor must immediately report the matter to the Minister" |

## What the text turns out to say

Findings from reading the text closely enough to encode it; each cites the lines it rests on (of `inputs/CoA1967.txt`).

1. **The label `(aa)` is printed twice in s 207(2)** (lines 19822 and 19832).
   The first states a condition: "if the financial statements or consolidated financial statements do not comply with any requirement of the Accounting Standards and the non-compliance is neither (i) approved by the Registrar under section 201(12); nor (ii) allowed under an order by the Minister under section 201(15A)".
   The second states what the report must say: "whether the non-compliance is, in the opinion of the auditor, necessary for the financial statements ... to give a true and fair view ...".
   I read them as one paragraph, a condition and its consequence, and encode one function (`s 207(2)(aa) ...`); the coverage table has two rows for them, "first of two" and "second of two".
   The mark `[Act 24 of 2025 wef 06/05/2026]` follows the second.
2. **The sections of Division 2 are not in numeric order.** The text runs s 205, ss 205AA to 205AF, then s 205A, 205B, 205C, 205D (headings at lines 19243 to 19546): the "AA" sections come before s 205A.
3. **s 205AF(1) uses paragraph labels for two different things** (lines 19471-19499): (a) and (b) are the triggers (a resignation under s 205AA(1), or one under s 205AB(1) that the Registrar "approves ... under section 205AB(2)"), and (c) and (d) are the duties the directors bear.
   The text says "approves" where s 205AB(1)(b) and (2) say "consent": it is one act, and the module takes the two triggers together as one fact, `the resignation is of a kind that subsection (1)(a) or (b) describes`.
4. **s 205AF(1)(c) has two limbs and only one has a number** (lines 19489-19493): "as soon as is practicable, and in any case not more than 3 months after the date of the auditor's resignation".
   The rule checks the 3 months; "as soon as practicable" is not computed.
   s 205AF(1)(d) says "within 14 days of the appointment" (not "after", not "beginning on"): fork entry F-P3.
5. **The appointee has two names.** s 205(1) and (2) say "an accounting entity or accounting entities"; s 205A(2) says "a person or persons" to be auditor (lines 19536-19540).
   The act constructor in `sgc2-s205a-exemption.l4` keeps s 205A(2)'s words (`s 205A(2) appoint a person or persons to be auditor or auditors of the company`); who may be an auditor is the keel's (s 10).
6. **Many duties have no number of days, so no deadline can be missed.**
   "Immediately": s 205(5)(a), s 205(8), s 206(1)(c) to (e), s 207(9), s 207(9A).
   "As soon as practicable": s 205AB(2) (the Registrar's duty); "in sufficient time": s 207(1A).
   No time limit at all: s 205(2), s 205(6), s 205AC(3), s 205B(4)(d), s 205C(7), s 206(1A), s 207(1).
   The functions that ask "in default of the duty" treat "not done immediately" as "not done" and say so in the seat's `HOW TO READ AN ANSWER`; the rules are listed under `## Rules with no breach path (sgc2)`.
7. **s 207(7) is in the passive and names no one** (lines 19927-19933): the report "must be attached to or endorsed on the financial statements ... must, if any member so requires, be read before the company in general meeting and must be open to inspection by any member at any reasonable time".
   There is a decision function ("a demand met") and no regulative rule, because there is no party to put in `PARTY`.
8. **s 207(1A) carries its own defence** (lines 19791-19801): "no offence is committed by an auditor under this subsection if the directors have not submitted the financial statements for audit as required under this Part in sufficient time, having regard to the complexity of the financial statements".
   The module has the function `s 207(1A) the auditor commits no offence under the subsection`.
9. **s 205C(1) is "Subject to subsections (3), (4) and (6)", and (6) is a date** (lines 19652-19696): for a financial year commencing before 1 July 2015 the section does not apply, and the company prepares and lays its accounts "in accordance with Part VI in force immediately before that date".
   Part VI as it then stood is not among the sources; it is a plain input.
10. **s 205B(6) and (7) bind s 205C through s 205C(2)** (lines 19629-19644, 19658-19661): members holding 5% may "by written notice to the company during a financial year but not later than one month before the end of that year, require the company to obtain an audit", and the company "is not entitled to the exemption" for that year.
    The window in (6) is a period the text fixes; the complement ("5%", "written notice") is not.
11. **The Schedule's tests are worded two ways.** Paragraphs 2(b), 5(b) and 7 say "for each of the 2 (consecutive) financial years immediately preceding"; paragraph 10 says "for 2 consecutive financial years immediately preceding" (line 29230), without "each of".
    The two readings of each are fork entries F-S1 and F-S2.
12. **The Schedule is cited by two sections.** Its heading reads "Sections 8(7) and 205C(5)" (lines 29013-29017); only s 205C is in this part's range.
13. **s 205D leaves the time to the Registrar** (lines 19708-19724): the Registrar may require a company exempt under s 205B or 205C to lodge audited statements "within such time as may be specified in that notice".
    The rule `s 205D the company must lodge what the Registrar's notice requires` takes the day the Registrar gave the notice and the last day the notice specifies as inputs; no number is invented.
14. **Five provisions of the range are shown deleted or repealed:** s 205(14) and (15) ("[Deleted by Act 36 of 2014]"), s 207(2)(c) ("[Deleted by Act 5 of 2004]"), s 207(3)(d) ("[Deleted by Act 36 of 2014]") and s 209B ("[Repealed by Act 5 of 2004]", which has no marginal heading in this rendering).
15. **s 207(9D)(a) can be read as a maximum or a minimum** (line 19997): "an offence that is punishable by imprisonment for a term that is not less than 2 years"; fork entry F-J1.
16. **s 205(16)(b) mixes two fixers** (lines 19229-19236): fees of an auditor appointed by the directors or by the Registrar "may be fixed by the directors or by the Registrar, as the case may be and, if not so fixed, must be fixed as provided in paragraph (a) as if the auditor had been appointed by the company".
    The function `s 205(16) the fees and expenses of the auditor are fixed as the subsection requires` takes who appointed the auditor and who fixed the fees as facts, and answers `JUST FALSE` for a combination the subsection does not allow: the Registrar fixing the fees of an auditor the company appointed, the directors fixing those of an auditor the Registrar appointed, or no one having fixed them.

## What the stable binary does not accept

Nothing in my ranges needed a construct that the stable build (1.6.110, and 1.6.109 for the second column) refuses, so there is no workaround to record under this heading.
What I did not use, because the brief says the stable build does not accept it: `REFUSE` and `#ASSERT REFUSED` (a case outside the encoding is `NOTHING`, asserted), `BECAUSE` outside `LEST BREACH ... BECAUSE`, a section-level `GIVEN`, `TYPICALLY`, `EVERY`, and a `YMD` of my own (dates are `Date day month year`).

Three limits of the instruments, which are not limits of the binary but which a reader should know:

- **`check.sh` counts `#ASSERT`s and does not see a regulative rule's outcome.**
  A rule's outcome is a `#TRACE` with `-- EXPECT FULFILLED`, `BREACH` or `RESIDUAL` above it; `check.sh` does not compare it, because it compares four counts and a trace is not one of them (its own footer says it "does not see a different TRACE outcome").
  `work/traces.py` (outside the deposit) runs every `#TRACE` on both builds and compares each outcome with its `-- EXPECT`: 70 traces in five test files; the expectation, build 110 and build 109 agree on every one, 0 problems.
- **Every duty with a last day is encoded twice**, as a rule (traced) and as a decision function named "... is in default of the duty ..." (asserted with `#ASSERT`), so that a duty's behaviour on each side of its last day is asserted as well as traced.
- **A rule with no `WITHIN` cannot be shown breached.** A late act still reads `FULFILLED`; see `## Rules with no breach path (sgc2)`.

The two layout messages that the final gate scans for (`is at the end of the file` and `follows code on its line`) do not occur: `l4 check` run on each of the 15 files whose names begin `sgc2-` printed neither of them, and no line containing `Warning` or `Error`.

## The seat layer

`sgc2-seat.l4` has 66 questions in six groups (`§`), in the text's order; `sgc2-cases-seat.l4` has 187 assertions, and every question is called in it at least once (25 of them have an assertion that answers `NOTHING`, the explicit "not covered" value).

| group | questions |
| --- | --- |
| Section 205: appointing, removing and replacing the auditor | 15 |
| Sections 205AA to 205AF: the auditor resigns | 14 |
| Sections 205A to 205D: the exemptions from the audit | 13 |
| Sections 206 to 208A: the auditor's remuneration, reports, powers and protection | 18 |
| Section 209: the auditor of a borrowing corporation and the trustee for debenture holders | 4 |
| Thirteenth Schedule: the small company and the small group (for section 205C) | 2 |

Every question is named "Under section N, ..." (or "Under schedule 13 paragraph M, ...") and carries `@export` and an `@desc` on every input; each takes plain inputs, one per fact a person in the seat can state, and the same fact has the same name and the same `@desc` in every question.
A question is a thin wrapper: it calls one layer-1 function and builds the records that function expects (the Schedule's yearly figures; the transactions of s 205B(2)) from the plain inputs.
The header comment of the seat file carries a `HOW TO READ AN ANSWER` paragraph (what `JUST TRUE`, `JUST FALSE` and `NOTHING` mean, what "in default" means, and which amounts are outside the sources).

**Direction audit** (the brief: "at the end list every question whose name and body differ in direction or subject and fix each").
I compared each question's name with the layer-1 function it calls, one by one (`work/seatnames.txt` is the list I read: each question next to the function it calls).
Questions whose name and body differ in direction or subject after the audit: **none remain**.
Listed for completeness, one wording variant that I judged not to differ: the question under s 205AC(2) asks whether copies of the written statement are "excused from being sent out", and the function it calls is named `s 205AC(2) copies of the written statement need not be sent out`; the same direction and the same subject, in the person's words.

## What `check.sh` prints

Run from this folder as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` (target `main`: each module is run on both stable builds and the four counts must match); it exited 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgc2-cases-seat.l4                             0       187       0        0         0 |      0       187       0        0  same
sgc2-common.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgc2-s205-appointment.l4                       0         0       0        0         0 |      0         0       0        0  same
sgc2-s205a-exemption.l4                        0         0       0        0         0 |      0         0       0        0  same
sgc2-s205aa-resignation.l4                     0         0       0        0         0 |      0         0       0        0  same
sgc2-s206-208a-duties.l4                       0         0       0        0         0 |      0         0       0        0  same
sgc2-s209-interpretation.l4                    0         0       0        0         0 |      0         0       0        0  same
sgc2-sch13-small.l4                            0         0       0        0         0 |      0         0       0        0  same
sgc2-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc2-tests-s205.l4                             0       114       0        0         0 |      0       114       0        0  same
sgc2-tests-s205a.l4                            0       142       0        0         0 |      0       142       0        0  same
sgc2-tests-s205aa.l4                           0       134       0        0         0 |      0       134       0        0  same
sgc2-tests-s206-208a.l4                        0       181       0        0         0 |      0       181       0        0  same
sgc2-tests-s209.l4                             0        54       0        0         0 |      0        54       0        0  same
sgc2-tests-sch13.l4                            0       116       0        0         0 |      0       116       0        0  same
TOTAL (23 modules)                             0       928       0        0           |      0       928       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**Baseline it replaced:** the keel's own run (`inputs/KEEL-NOTES.md`) was 17 modules, 974 assertions satisfied, 0 errors, 0 failed, 0 refused, the same on both builds, exit 0.
This folder holds the keel's eight modules and my fifteen files: **23 modules, 928 assertions satisfied** (114 + 134 + 142 + 181 + 54 + 116 in the six test files, 187 in the seat case file), 0 errors, 0 failed, 0 refused, identical on both builds.
The keel's eight modules carry no assertions here (their tests are not in this folder), which is why my 928 is not added to the keel's 974.
