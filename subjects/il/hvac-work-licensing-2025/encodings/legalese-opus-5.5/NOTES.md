# NOTES — the HVAC work-licensing Law and its Fees Regulations, in L4

Row `legalese-opus-5.5`.
Status **draft**: no domain expert has read this encoding against the source.
Made on 2026-10-13 by a single Opus 5.5 agent working alone from the brief, with no subagents and no other encoding of this subject in view.
Later the same day, the same agent corrected the row's date logic against s. 10 of the Interpretation Law (§11). For that pass only, it read the Interpretation Law row, a different subject, and vendored its time module.

## 1. What is encoded, and what is not

The subject is חוק הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר, התשפ״ה–2025 (Sefer HaChukim 3349, 14 January 2025, p. 182), together with the Fees Regulations made under its ss. 59-60.

From the Law, the encoding covers exactly the pinned slice: ss. 2, 3, 6 with the Second Schedule, 7, 8, 9, 16, 17 and 63.
Section 2's operative definitions are rules: refrigeration system, work, the three licence grades and completion certificate.
Its definitions of offices, statutes and registers are carried as quoted text.
Section 3(a) is a test and a prohibition.
Section 6 is the grant test and the Registrar's duty to grant.
The Second Schedule is data, all 17 items of its three Parts with column C's three-year limit.
Sections 7, 8 and 9 are the tests and powers they state.
Sections 16 and 17 are duties with their deadlines, and tests over recorded findings.
Section 63 gives the commencement dates, computed from the gazette dates.
Every period counted forward from a day or after an event, in the Law and in the Regulations, is counted by s. 10 of the Interpretation Law 5741-1981.
"Until" is read by its s. 8, and a commencement with no day of its own by Interpretation Ordinance s. 17.
All three come through `il-interpretation-time.l4`, vendored byte-identical from the Interpretation Law row (§11).

From the Fees Regulations, every regulation is encoded in all three vintages.
The DRAFT is what the SimpLEX screenshot shows: reg 1, reg 2(א)-(ה), the heading of reg 3, and a one-line gloss of reg 4 in the test panel.
AS MADE is Kovetz HaTakanot 11951, regs 1-5.
AS AMENDED is that text with the two amendments of Kovetz HaTakanot 12383.
The SimpLEX test table (rows 5-8) and its worked example are transcribed and run against the draft in the table's own words.
They are also run against the other two vintages, asserting what each vintage answers.

Not encoded: the First and Fourth Schedules, which are outside the pinned scope.
Their answer for a given piece of work or system is recorded as a fact on the `Work` and `System` records.
Also not encoded: every other section of the Law (Chapters D-F, s. 10 and the rest), including ss. 59-60, which empower the Regulations.
Nor is anything the screenshot does not show: draft regs 3-5 and beyond, table rows 1-4, and the second table's rows.

## 2. Sources

All in `inputs/` of the run directory, quoted mechanically.
Hebrew from the screenshot is the exception: it is an image, so its Hebrew in this encoding was **transcribed by eye from upscaled crops, not copied**.

| file | what | authority | sha256 (first 16) |
| --- | --- | --- | --- |
| `sefer-hachukim-3349-pp182-209.pdf` / `.txt` | the Law, official gazette, 14 Jan 2025 | authoritative | `8ff58ab802356836` / `56bb076074d0a4a2` |
| `law.wiki` | Wikisource rev 2947808 (2025-07-10) | aid, unofficial | `e8a8ac3bedbc0e7b` |
| `kovetz-hatakanot-11951-p2116.pdf` / `.txt` | Fees Regulations as made, 9 Jul 2025 | authoritative | `fe5d0d1080858f6f` / `fcf7cf8a4b872da8` |
| `takanot-12383.pdf` / `.txt` | the 5786 amendment, 4 May 2026 | authoritative | `b034686dfd8b537d` / `56381444a5437e08` |
| `regulations-fees.wiki` | Wikisource rev 3011135 (2026-05-04), consolidated as amended | aid, unofficial | `4c08bf33dbfa1b4c` |
| `fig4-simplex-screenshot.png`, `fig4-page34-400dpi.png` | the DRAFT: Figure 4 of Schwartz, Bar-Siman-Tov & Gelbard (2025), Hebrew p. 386 | the only witness of the draft | `259ac9e4000020d9`, `eb4472b2e4a1459b` |
| `fig4-en-p28-28.png` | the English page with the caption, p. 379 | aid | `9b3328a07fb55af0` |
| `knesset-bill-25_ls2_5256851.pdf` | the bill for second and third reading, 11 Dec 2024 | aid (numbering check only) | `6ded44c4ed2397be` |
| `revisions.json` | the Wikisource revision ids | aid | `84cb0a971b8829d4` |

Hebrew for the Law is copied from `law.wiki` and was compared with the gazette text section by section, **by eye, not mechanically**.
They agree for every in-scope section except one: in Second Schedule Part C item 4, the wiki prints "(הכשרה של עד 240 שעות …" inside column A, with a stray parenthesis.
The gazette prints it in column B, and the gazette is followed (F28).
Hebrew for the Regulations as made and as amended is copied from `regulations-fees.wiki`; the as-made words of reg 2(ב) were recovered by undoing KT 12383 reg 2(2).
That copy was **measured**, by a script in the run directory (`tools/quotecheck.py`, not part of the deposit), after removing whitespace and bidi controls and unifying dash and quotation-mark glyphs.
Each of the four as-made `the words` strings of reg 2, and the quotations of regs 3 and 4, is a substring of KT 11951's text.
The two as-amended strings, 2(א1) and 2(ב), are substrings of the consolidated wiki text.
KT 12383's own words for 2(א1) are in its text too, but the text extraction scrambles "(א1)" in the instruction for 2(ב), a bidi artefact.
So that instruction was read off the rendered PDF page, which prints "ובמקום ״בתקנת משנה (א)״ יבוא ״בתקנת משנה (א1)״".
The wiki's "(מתואם לשנת 2025)" / "(מתואם לשנת 2026)" notes belong to the wiki, not the text, and are left out.

The figure's English caption calls it "an illustration of an integrated drafting environment (screen capture of the SimpLEX drafting-and-testing tool)".
Footnote 190 says it "was developed as part of the first author's work at the Ministry of Justice".
Whether the draft it shows was ever an official draft is not stated in the sources; see open question Q10.

**The rules for counting time** come from `il-interpretation-time.l4`, copied unchanged from `subjects/il/interpretation-law-1981/encodings/legalese-sonnet-5.5/` at its commit `313de518` (sha256 `d1552de57266d7dc…`).
That row encodes ss. 3, 8, 10 and 21 of the Interpretation Law 5741-1981 and s. 17 of the Interpretation Ordinance [New Version]; its own NOTES.md gives its sources and forks.
This row uses its s. 8, s. 10(a), (b) and (c), and Ordinance s. 17, and does not edit the copy (`cmp` against the source is empty).

## 3. Modules, in reading order

| module | what |
| --- | --- |
| `il-interpretation-time.l4` | VENDORED, unedited, from the Interpretation Law row: Interpretation Law ss. 3, 8, 10, 21 and Ordinance s. 17 as functions; days of rest are an input |
| `domain.l4` | the nouns only: vintages, services, requests, licences, systems, qualifications, Second Schedule columns, parties and acts |
| `fees-regulations.l4` | regs 1-5 in three vintages; the fee lookup takes the vintage as an input |
| `law-commencement.l4` | s. 63 |
| `second-schedule.l4` | the Second Schedule as data, and s. 6(a)(4), which reads it |
| `law-licensing.l4` | ss. 2, 3, 6, 7, 8, 9 |
| `law-duties.l4` | ss. 16, 17 |
| `simplex-scenarios.l4` | the SimpLEX rows and worked example as named cases; how the table's words are read |
| `tests-simplex-draft.l4` | the table against the DRAFT, in its own words: 12 assertions |
| `tests-fees.l4` | every vintage: the fee table cell by cell, regs 1-5, and the SimpLEX scenarios as each vintage answers them: 106 assertions, 1 trace |
| `tests-law.l4` | the Law, with three illustrative rest-day calendars for s. 10(c): 121 assertions, 7 traces |
| `tests-simplex-red.l4` | **expected to fail**: 2 assertions, both expected to fail |

`check.sh` runs them all with `L4=<path to l4> ./check.sh`.

## 4. Coverage table

Every in-scope provision, with its disposition.
**encoded** means it is a rule, a test or data. **encoded (REFUSE)** means a named refusal stands where the source is not shown. **inert** means it is carried as quoted text and decides nothing. **not shown** means the source has nothing visible to encode.
No row is `deferred`.

### The Law

| provision | heading / words | disposition | where |
| --- | --- | --- | --- |
| s. 2 "אגף להכשרה מקצועית" | definition | inert | `law-licensing.l4` §§ Section 2 |
| s. 2 "בעל רישיון" | definition | inert | same |
| s. 2 "חוק ההנדסאים והטכנאים המוסמכים" | definition | inert | same |
| s. 2 "חוק החשמל" | definition | inert | same |
| s. 2 "חוק העונשין" | definition | inert | same |
| s. 2 "המועצה" | definition | inert | same |
| s. 2 "מערכת קירור או מיזוג אוויר", "מערכת" | definition | encoded | `section 2 — a refrigeration or air-conditioning system` |
| s. 2 "מפקח" | definition | inert | same |
| s. 2 "המפקח הבכיר" | definition | inert | same |
| s. 2 "מרשם ההנדסאים והטכנאים המוסמכים" | definition | inert | same |
| s. 2 "המשרד" | definition | inert | same |
| s. 2 "עבודה במערכת קירור או מיזוג אוויר" | definition | encoded (First Schedule answer recorded) | `section 2 — work on a refrigeration or air-conditioning system` |
| s. 2 "קרר" | definition | encoded (as the recorded fact on `System`) | `domain.l4` `System` |
| s. 2 "רישיון" (1)-(3) | definition | encoded (as the type) | `domain.l4` `Licence grade` |
| s. 2 "רישיון דרגה 1" | up to 18 kW | encoded | `section 2 — a licence of … covers …` |
| s. 2 "רישיון דרגה 2" | up to 70 kW | encoded | same |
| s. 2 "רישיון דרגה 3" | any system | encoded | same |
| s. 2 "הרשם" | definition | inert | same |
| s. 2 "תעודת גמר" (1)-(2) | completion certificate | encoded | `section 2 — a completion certificate` |
| s. 2 "השר" | definition | inert | same |
| s. 3(a) | חובת רישוי | encoded | `section 3 prohibits the work`, `section 3(a) — the duty not to do the work unlicensed` |
| s. 3(b) | exemption by order | encoded (an order's effect recorded on `System`) | same |
| s. 3(c) | power to amend the First Schedule | inert | comment at s. 3 |
| s. 6(a) chapeau | "הרשם ייתן רישיון" | encoded (test and MUST) | `section 6(a) — …` |
| s. 6(a)(1) | בגיר | encoded | `section 6(a)(1) to (3) are met by` |
| s. 6(a)(2) | citizen or resident | encoded | same |
| s. 6(a)(3) | offence, "לדעת הרשם" | encoded (recorded determination) | same |
| s. 6(a)(4) chapeau | "והכול בהתאם לתנאים שבתוספת השנייה" | encoded | `section 6(a)(4) is met by` |
| s. 6(a)(4)(a) | completion certificate | encoded, through the Schedule (F12) | same |
| s. 6(a)(4)(b) | registered technician/practical engineer | encoded, through the Schedule (F12) | same |
| s. 6(a)(4)(c) | supplementary studies | encoded, through the Schedule (F12) | same |
| s. 6(b) | power to amend the Second Schedule | inert | comment in `second-schedule.l4` |
| Second Schedule, Part A items 1-3 | grade 1 | encoded (3 rows) | `item A1`-`item A3` |
| Second Schedule, Part B items 1-6 | grade 2 | encoded (6 rows) | `item B1`-`item B6` |
| Second Schedule, Part C items 1-8 | grade 3 | encoded (8 rows) | `item C1`-`item C8` |
| Second Schedule, column C notes | three-year limit (A2, B4, C5) | encoded | `item … is in force on` |
| s. 7(a) | exemption, electricity chapter | encoded (test and MAY) | `section 7(a) — …` |
| s. 7(b) | exemption, work at height | encoded | `section 7(b) — …` |
| s. 7(c) | publish how to apply | encoded (undated MUST) | `section 7(c) — …` |
| s. 8 validity period | "לחמש שנים או עד 31 במרץ …" | encoded | `section 8 — the last day of the validity period …` |
| s. 8 renewal | "בהתקיים התנאים לפי סעיף 6, למעט … (א)(4)" | encoded | `section 8 — the licence may be renewed …` |
| s. 9(a) chapeau | temporary grade 3 licence, at most a year | encoded | `section 9(a) — a foreign expert`, `section 9 — a period … does not exceed a year` |
| s. 9(a)(1) | invited, above 70 kW | encoded | same |
| s. 9(a)(2) | authorised abroad; six years | encoded | same |
| s. 9(a)(3) | recognised by the Registrar | encoded (recorded determination) | same |
| s. 9(b) | two further periods | encoded | `section 9(b) — …` |
| s. 16 | update particulars within 30 days | encoded (test and MUST WITHIN 30) | `section 16 — …` |
| s. 17(a) | eight hours in the last year | encoded (test and MUST WITHIN) | `section 17(a) — …` |
| s. 17(b) | Registrar may require a course | encoded (test over recorded findings) | `section 17(b) — …` |
| s. 17(c) | extension of at most three months | encoded | `section 17(c) — …` |
| s. 17(d) | deemed a licence condition | encoded (deeming constant) | `section 17(d) — …` |
| s. 17(e) | Registrar ensures courses exist | encoded (undated MUST) | `section 17(e) — …` |
| s. 17(f) | Registrar publishes courses | encoded (undated MUST) | `section 17(f) — …` |
| s. 63(a) chapeau | "למעט פרק ו׳" | encoded | `the day this Law, other than Chapter F, comes into force for work on` |
| s. 63(a)(1) | flammable listed refrigerant; יום התחילה | encoded | `the commencement day`, `section 63(a)(1) reaches work on` |
| s. 63(a)(1), last clause | power to amend the Fourth Schedule | inert | comment in `law-commencement.l4` |
| s. 63(a)(2) | 18 months | encoded | `eighteen months from the commencement day` |
| s. 63(b) | Chapter F | encoded (REFUSE where the s. 46 regulations' date is not supplied) | `the day Chapter F comes into force, given` |

### The Fees Regulations

| vintage | provision | disposition | where |
| --- | --- | --- | --- |
| draft | title and preamble (cites s. 59 only) | inert | header comment of `fees-regulations.l4` |
| draft | reg 1, "בחינה עיונית", "בחינה מעשית" | encoded | `regulation 1 defines` |
| draft | reg 2(א) theoretical exam 273 | encoded | `draft regulation 2(א)` |
| draft | reg 2(ב) practical exam 194 | encoded | `draft regulation 2(ב)` |
| draft | reg 2(ג) appeal, 40 per appeal | encoded | `draft regulation 2(ג)` |
| draft | reg 2(ד) licence application 284 | encoded | `draft regulation 2(ד)` |
| draft | reg 2(ה) temporary licence application 398 | encoded | `draft regulation 2(ה)` |
| draft | reg 3 "עדכוני אגרות" (heading only) | encoded (REFUSE) | `the draft's regulation 3 is not shown in the screenshot` |
| draft | reg 4 (text not shown; panel gloss "אוסרת רישום ללא תשלום") | encoded from the gloss, REFUSE beyond it (F2) | `the draft's regulation 4, as glossed — …` |
| draft | commencement (not shown) | encoded (REFUSE) | `the draft's commencement provision is not shown in the screenshot` |
| draft | anything after reg 3's heading | not shown | — |
| as made | preamble (ss. 59 and 60) | inert | header comment |
| as made | reg 1 "בחינה מעשית" | encoded | `regulation 1 defines` |
| as made | reg 2(א) practical exam 194 | encoded | `regulation 2(א) as made` |
| as made | reg 2(ב) objection 40 | encoded | `regulation 2(ב) as made` |
| as made | reg 2(ג) licence 284 | encoded | `regulation 2(ג) as made` |
| as made | reg 2(ד) temporary licence 398 | encoded | `regulation 2(ד) as made` |
| as made | reg 3(a) indexation | encoded | `regulation 3(a) — …`, `the fee payable for … on …` |
| as made | reg 3(b) publication | encoded (undated MUST) | `regulation 3(b) — …` |
| as made | reg 4 payment as a condition | encoded | `regulation 4 as enacted — …`, `regulation 4 — the prohibition on` |
| as made | reg 5 commencement | encoded | `the day the Regulations as made came into force` |
| as amended | KT 12383 preamble | inert | header comment |
| as amended | KT 12383 reg 1: "בחינה עיונית" | encoded | `regulation 1 defines` |
| as amended | KT 12383 reg 2(1): reg 2(א1) theoretical exam 158 | encoded | `regulation 2(א1) as amended` |
| as amended | KT 12383 reg 2(2): reg 2(ב) confined to the theoretical exam | encoded | `regulation 2(ב) as amended` |
| as amended | commencement (KT 12383 has none) | encoded, by Interpretation Ordinance s. 17 (F10) | `the day the amendment came into force` |

### The SimpLEX panel

| item | disposition | where |
| --- | --- | --- |
| heading, "סעיפים רלוונטיים: חוק – סעיף 9 \| תקנות – 2(א)-(ה)" | inert | comment in `simplex-scenarios.l4` |
| row 5 | encoded (tested in all three vintages) | `tests-simplex-draft.l4`, `tests-fees.l4` |
| row 6 | encoded | same |
| row 7 (run on each exam, F1) | encoded | same |
| row 8 (run on each exam, F1) | encoded | same, and `tests-simplex-red.l4` |
| worked example | encoded | same, and `tests-simplex-red.l4`; its s. 9(a) ground in `tests-law.l4` |
| rows 1-4 | not shown | — |
| second table, "תרחישי בדיקה לעדכוני אגרות ומדד" (header only) | not shown | — |

### Tally

| disposition | Law | Regulations | SimpLEX | total |
| --- | --- | --- | --- | --- |
| encoded | 43 | 19 | 5 | 67 |
| encoded (REFUSE, or from a gloss plus REFUSE) | 0 | 3 | 0 | 3 |
| inert | 15 | 3 | 1 | 19 |
| not shown | 0 | 1 | 2 | 3 |
| deferred | 0 | 0 | 0 | 0 |
| rows | 58 | 26 | 8 | 92 |

The Law column counts the Second Schedule as four rows (one per Part, and column C); counted item by item, the Law has 57 encoded rows.
The Regulations' "encoded" count includes KT 12383's missing commencement clause, encoded since 2026-10-13 by Interpretation Ordinance s. 17 (until then, as an assumed date).
s. 63(b) is counted as encoded: it computes when the s. 46 date is supplied, and refuses otherwise.

**Out of scope, crossed by a recorded fact:** the First Schedule (the licence types it sets against a piece of work, recorded on `Work`) and the Fourth Schedule (whether a system's refrigerant is listed, on `System`).
Also s. 10 (cancellation or suspension, recorded on `Licence`), and the instruments s. 7 cites (recorded on `Applicant`).

## 5. The fee for each service under each vintage, as read here

Amounts in new shekels, **as printed**.
On every 1 January from 2026 (from 2027 for 2(א1)), reg 3(a) of the text as made and as amended updates them by the consumer price index.
No index figure is in the sources, so the updated amounts are not stated here; `the fee payable for … on …` computes them from figures a caller supplies.

| service | DRAFT | AS MADE (KT 11951) | AS AMENDED (KT 12383) |
| --- | --- | --- | --- |
| a theoretical exam | **273** — draft reg 2(א) | **silent** — no sub-regulation; reg 1 does not define the exam | **158** — reg 2(א1) |
| a practical exam | **194** — draft reg 2(ב) | **194** — reg 2(א) | **194** — reg 2(א) |
| an objection to (appeal against) a theoretical-exam grade | **40 per appeal** — draft reg 2(ג) | **silent** — reg 2(ב) reaches only the exam in (א) (F3) | **40 per objection** — reg 2(ב) |
| an objection to (appeal against) a practical-exam grade | **40 per appeal** — draft reg 2(ג) | **40 per objection** — reg 2(ב) | **silent** — reg 2(ב) now reaches only "הבחינה העיונית" (F4) |
| a licence, or its renewal, under s. 5 | **284**, charged on the application — draft reg 2(ד) | **284**, on receipt — reg 2(ג) | **284**, on receipt — reg 2(ג) |
| a temporary licence for a foreign expert, or its renewal | **398** — draft reg 2(ה) (which cites "s. 8", F5) | **398** — reg 2(ד) | **398** — reg 2(ד) |
| a continuing-training course under s. 17 | **silent** — the draft's reg 2 is shown whole | **silent** | **silent** |

## 6. The SimpLEX scenarios, as each vintage answers them

What reg 4 does to each request.
A ✓ or ✗ says whether the table's own outcome word holds under the reading in F11 (i).

| row | facts | table's outcome / reference | DRAFT | AS MADE | AS AMENDED |
| --- | --- | --- | --- | --- | --- |
| 5 | theoretical exam, 273 paid | הרשמה מאושרת / 2(א) | not withheld ✓ (2(א)) | not reached: no fee ✓ (no sub-regulation) | not withheld ✓ (2(א1)) |
| 6 | practical exam, 194 paid | הרשמה מאושרת / 2(ב) | not withheld ✓ (2(ב)) | not withheld ✓ (2(א)) | not withheld ✓ (2(א)) |
| 7 | appeal on a theoretical exam, 40 paid | הערעור נבדק / 2(ג) | not withheld ✓ (2(ג)) | not reached: no fee ✓ | not withheld ✓ (2(ב)) |
| 7 | appeal on a practical exam, 40 paid | הערעור נבדק / 2(ג) | not withheld ✓ (2(ג)) | not withheld ✓ (2(ב)) | not reached: no fee ✓ |
| 8 | theoretical exam, nothing paid | השעיית שירות / תקנה 4 | withheld ✓ | **not reached ✗** | withheld ✓ |
| 8 | practical exam, nothing paid | השעיית שירות / תקנה 4 | withheld ✓ | withheld ✓ | withheld ✓ |
| ex. | theoretical exam, nothing paid | הרשמה נדחית – חובה להשלים תשלום | withheld ✓ | **not reached ✗** | withheld ✓ |

The two ✗ are the two assertions of `tests-simplex-red.l4`, expected to fail.
Under the stricter reading F11 (ii), three more would fail: row 5 and row 7 on a theoretical exam as made, and row 7 on a practical exam as amended.
That would make five.
The table's reference column holds for the draft only: the enacted text renumbered the theoretical exam to 2(א1), the practical exam to 2(א) and the objection to 2(ב).

## 7. Fork register

Each entry gives the text, the readings, the one taken, and why.
None of these has been settled by a court or the regulator as far as the sources show.
Since 2026-10-13, F10, F14, F17, F19, F21 and F29 are settled by the Interpretation Law or Ordinance rather than by a reading; F31 to F36 were added in that pass (§11).

**F1 — which exam rows 7 and 8 mean.**
"ערעור עם תשלום (₪ 40)" and "הרשמה לבחינה ללא תשלום" do not name the exam.
Readings: theoretical, practical, either.
Taken: run each row on both exams. The vintages answer them differently, and a single choice would hide that.

**F2 — the draft's regulation 4.**
Its text is not on the screen.
The panel's worked example glosses it, "תקנה 4: אוסרת רישום ללא תשלום", and row 8 cites it.
Readings: (i) unknown, so refuse everything that depends on it; (ii) the gloss, and only the gloss; (iii) the as-made reg 4, which would borrow from another vintage and is forbidden.
Taken: (ii). A request whose draft fee was paid in full is not withheld, because a payment condition is met by full payment whatever its words.
An exam registration with nothing paid is withheld, as the gloss says.
Everything else refuses by name: part-payment, an unpaid objection or licence, or a service draft reg 2 does not price.

**F3 — "the exam" in reg 2(ב) as made, and "(א)" in the draft's 2(ג).**
As made: "הוגשה השגה על ציון הבחינה … נוסף על התשלום בעד האגרה כאמור בתקנת משנה (א)".
Readings: the exam is the one (א) prices, the practical exam; or any exam the Division sets.
Taken: the practical exam. It is the only exam the text as made defines or prices, and the 5786 amendment rewrote the words to "העיונית" and "(א1)", which assumes the old words pointed elsewhere.
Consequence: an objection to a theoretical-exam grade has no fee as made.
The draft's 2(ג) has the mirror problem: it covers "הבחינה עיונית או המעשית" but adds to "(א)", the theoretical fee only. The appeal fee is taken to be 40 on either exam.

**F4 — reg 2(ב) as amended.**
KT 12383 inserts "העיונית" after "הוגשה השגה על ציון הבחינה" and replaces "(א)" with "(א1)".
Taken, on the plain words: as amended, the objection fee attaches only to the theoretical exam, and no sub-regulation sets a fee for an objection to a practical-exam grade.
Reg 4 then does not reach such an objection.
Whether the amendment meant to make practical-exam objections free, to abolish them, or simply overlooked them is not in the sources (Q1).

**F5 — the draft's reg 2(ה) cites "סעיף 8".**
The enacted Law, and the bill for second and third reading (11 Dec 2024), put the temporary licence for a foreign expert at s. 9; s. 8 is the validity period.
Taken: the service is identified by its description; the section number is recorded as a drafting slip in the draft, not as law.

**F6 — what the licence fee is charged on.**
Draft 2(ד): "בעד בקשה לקבלת רישיון או לחידושו" (for the application). As made 2(ג): "בעד קבלת רישיון או חידושו" (for receiving it).
Taken: one service with the same amount, and a separate answer, `what the licence fee is charged on under`, that records the difference.

**F7 — whether reg 4 reaches the temporary licence.**
Reg 4 speaks of "רישיון שנקבעה בעדו אגרה"; reg 2(ד) sets the fee "בעד בקשה לקבלת רישיון זמני".
Taken: reached, since a fee is set in respect of that licence. Read the other way, an unpaid temporary licence would be "not reached".

**F8 — what "paid the fee in full" means for an objection, and the antecedent of "בעדן".**
In "הגשת השגה על בחינות, שנקבעה בעדן אגרה", the feminine plural "בעדן" grammatically follows "בחינות" (the exams).
Readings: (i) reg 4 bars each service for which a fee is set, until that service's fee is paid, so an objection needs its 40; (ii) it bars an objection on an exam for which a fee is set until "the fee" is paid, which might be the exam's fee.
Taken: (i). Reg 2(ב)'s "נוסף על התשלום בעד האגרה כאמור …" presupposes the exam fee is already paid and makes the 40 the objection's own fee.
Under (ii), row 7 could not be answered without knowing whether the exam fee had been paid, a fact the table does not give.

**F9 — rounding under reg 3(a).**
"ויעוגל לשקל החדש השלם הקרוב": the nearest whole shekel. The text does not say which way a half goes.
Taken: half up. L4's `ROUND` rounds half to even and is not used.

**F10 — when KT 12383 came into force. Settled 2026-10-13.**
It has no commencement clause. It was signed on 28 April 2026 and published on 4 May 2026.
Interpretation Ordinance s. 17: regulations of legislative effect come into force on the day of their publication "if there is no other provision on the matter" (`Ordinance s 17 — …` in `il-interpretation-time.l4`).
So KT 12383 came into force on 4 May 2026, now read from a rule, not assumed (F36 for why the Ordinance reaches it).
Before 2026-10-13 this entry recorded the same day as an assumption, because the rule was not among the sources.
Only `the Fees Regulations in force on` and `the fee payable for … on …` depend on it; the vintage-keyed lookup does not.

**F11 — how the table's outcome words are read against reg 4.**
Reg 4 decides only whether a service is withheld for want of payment.
Readings: (i) outcome level, where "הרשמה מאושרת" and "הערעור נבדק" mean not withheld (whether because the fee was paid or because none is set), and "השעיית שירות" and "הרשמה נדחית" mean withheld; (ii) reason level, where "approved" means a fee is set and paid.
Taken: (i), because the table's outcome column states outcomes and its reference column states reasons; the reasons are tested separately.
Note that row 8 and the worked example give two different words, suspension and rejection, to the same facts on a theoretical exam. Both are read as withheld.

**F12 — s. 6(a)(4) and the Second Schedule.**
"(4) מתקיים בו אחד התנאים שלהלן, והכול בהתאם לתנאים שבתוספת השנייה: (א) … (ב) … (ג) …".
Readings: (i) the Schedule governs all three limbs, so (4) is met when some item of the Part for the grade sought describes the applicant in column A and is met in column B; (ii) (א) alone is met by any s. 2 completion certificate, whatever the grade.
Taken: (i). Under (ii), a grade 1 certificate would earn a grade 3 licence, and Parts B and C would do nothing.

**F13 — the "בלא הכשרה או ניסיון קודמים" route, and several items at once.**
Taken: the no-prior-training item is open to everyone, including the experienced, and meeting any one item is enough.
Otherwise a worker with a year's experience who took the full 350-hour course would meet no item at all.

**F14 — when column C's three years end. Corrected 2026-10-13.**
"לתקופה של שלוש שנים מיום תחילתו של חוק זה, כאמור בסעיף 63(א)(1)": the commencement day is 16 July 2025.
Interpretation Law s. 10(b) ends three years from it on 16 July 2028, and that day is inside the period.
So the item stands up to and including 16 July 2028 and is gone on 17 July 2028.
It said 15 and 16 July before. The day that matters is the day s. 6 is applied.
s. 10(c) is not applied to it (F31); 16 July 2028 is a Sunday, so the illustrative calendars would not move it anyway.

**F15 — what identifies a column B course; "עד N שעות".**
Taken: a course is identified as the Schedule identifies it, by its length cap and the certificate it confers, and "up to N hours" describes the course rather than testing the applicant.
This is what keeps items A3, B5, B6, C6 and C7 from being circular: their column A holds the Division's general certificate, and column B is a course conferring that same certificate.
The cost: the 50-hour course is described in identical words in Parts A, B and C, and the text does not tie it to a grade, so completing it once meets column B wherever it appears (Q5).

**F16 — "עד 31 במרץ של השנה החמישית מהשנה שבה ניתן הרישיון" (s. 8).**
Readings: the year of grant plus five, or plus four (counting the year of grant as the first).
Taken: plus five.
Under plus four, 31 March of that year always falls before the fifth anniversary, so "לפי המוקדם" (whichever is earlier) could never choose the five years.
Under plus five, each limb is the earlier one for some grant dates.
A reviewer leaning toward plus four should say what "לפי המוקדם" then does.
Interpretation Law s. 10 does not settle this: "the fifth year" names a calendar year, not a counted period.
The argument still holds with s. 10(b)'s end on the anniversary itself: under plus four, 31 March of year + 4 is always before the anniversary in year + 5.

**F17 — the edges of a validity period, and renewal. Corrected 2026-10-13.**
"לחמש שנים" is a period of years after an event, the grant. Interpretation Law s. 10(b) ends it on the fifth anniversary, which is inside the period; it said the day before the anniversary before.
"עד 31 במרץ" includes 31 March, now by Interpretation Law s. 8 ("until" means until and including) rather than by a reading.
s. 10(c) applies to the five years but not to the fixed day 31 March (F31).
A renewed period is still measured the same way from the day of renewal: the text measures from "השנה שבה ניתן הרישיון" and does not say how a renewed period is measured, and s. 10 does not either.

**F18 — "עד 18 / עד 70 קילו־ואט" (s. 2).**
Taken: "up to" includes the figure.
Against s. 9(a)(1)'s "מעל 70" (above 70), this means that at exactly 70 kW a grade 2 licence covers the system and the foreign-expert route is closed.

**F19 — "בתוך 30 ימים מיום השינוי" (s. 16). Settled 2026-10-13.**
Interpretation Law s. 10(a): the day of the change is not counted, so the 30th day after it is the last day; the 31st is late.
That is the answer the reading gave before; it is now the statute's.
A notice on the day of the change itself is in time, being before the deadline, and a notice dated before the change is not.
So the test is "on or after the day of the change, up to and including the last day". It is not the module's `s 10 — the date … is inside a period …`, whose period begins the day after the change.
s. 10(c) applies (F31): a 30th day that is a day of rest, recess or holiday runs on to the first day that is not.
The duty's `WITHIN` is the number of days from the change to that last day.

**F20 — "במהלך השנה האחרונה לתוקפו של הרישיון" (s. 17(a)).**
Taken: the year that ends on the last day of validity, beginning the day after the same date a year earlier.
The window counts backwards from the end of validity, which Interpretation Law s. 10 does not speak of (F33), so it is unchanged by the 2026-10-13 pass. Its end, the last day of validity, is s. 8's, and is counted by s. 10.
A course must meet every condition in the sentence to count, including "ויעמוד בדרישות אותן השתלמויות".
"שמונה שעות לפחות" is the sum of the hours that count.

**F21 — the s. 63 dates. Counted by s. 10 since 2026-10-13; the dates did not move.**
Publication is 14 January 2025, and three months from it end, by Interpretation Law s. 10(b), on 14 April 2025; the Regulations came into force on 16 July 2025.
The commencement day is the later of the two, 16 July 2025; eighteen months from it end on 16 January 2027.
Wikisource's own note gives 16 July 2025 for the Regulations, consistent with reg 5 counted by s. 10(a).
The Law commences ON the last day of each period (F32), and s. 10(c) is not applied (F31), although 16 January 2027 is a Saturday.

**F22 — a listed flammable refrigerant whose use is not permitted.**
Taken: it is "not as stated in paragraph (1)" and falls under s. 63(a)(2), 18 months.

**F23 — the indexation chain under reg 3.**
Taken: each 1 January update moves the amount as it then stands, rounded.
The first update after commencement, 1 January 2026, uses the June 2025 index as its basic index.
Reg 2(א1), first printed in 2026, is first updated on 1 January 2027, from the November 2025 index.
The amounts KT 12383 did not reprint keep their 2026 update even under the amended text.

**F24 — wording differences with no operative effect.**
The draft's reg 1 says "התלמיד" where the text as made says "לומד בקורס הכשרה מקצועית".
The draft's preamble cites s. 59 only, and consults the Minister of Finance ("לאחר התייעצות עם שר האוצר ובאישורו").
The draft's reg 2 says "תשולם" (shall be paid) where the text as made says "ישלם הנבחן / מבקש הרישיון", naming the payer.
None of these changes an answer here.

**F25 — the worked example's first ground.**
"סעיף 9(א): מחייב מעבר בחינה" (s. 9(a) requires passing an exam).
Section 9(a), as enacted and as in the bill, is the foreign-expert licence and names no exam.
The Law's exam requirement is in s. 2's "תעודת גמר" ("…הכוללת בחינה עיונית ובחינה מעשית").
Both are tested in `tests-law.l4`.

**F26 — the draft calls it "ערעור" (appeal); the enacted text calls it "השגה" (objection).**
Taken: one service, recorded under both names.

**F27 — "רישיון מהסוג המתאים … כמפורט בטור א׳ בתוספת הראשונה" (s. 3(a)).**
Taken: the licence's grade must cover the system's cooling capacity under s. 2's definitions, and the First Schedule must set that grade against the work.
The second part is recorded on `Work`, because the First Schedule is out of scope.

**F28 — Second Schedule Part C item 4.**
The gazette's column B reads "הכשרה של עד 240 שעות …"; the wiki puts it in column A.
The gazette is followed.

**F29 — "לתקופה שלא תעלה על שנה" (s. 9). Corrected 2026-10-13.**
A year after the grant (the first day) ends, by Interpretation Law s. 10(b), on the anniversary, inside the period. So the period may run up to and including the anniversary; it ended the day before the anniversary before.
s. 10(c) applies (F31). The same test serves each renewal under s. 9(b).
The actual period is the Registrar's to set; it is recorded on the `Licence`, and its absence refuses by name.

**F30 — the draft as a vintage.**
The figure is captioned an "illustration" of a drafting environment, made at the Ministry of Justice.
Taken: it is the draft vintage, because the brief makes it so; nothing in the sources says it was ever circulated (Q10).

**F31 — whether s. 10(c) applies, by kind of period. Added 2026-10-13.**
Interpretation Law s. 10(c): "במנין ימי תקופה יבואו גם ימי מנוחה, פגרה או שבתון שעל פי חיקוק, זולת אם הם הימים האחרונים שבתקופה". Its text is unqualified ("ימי תקופה", the days of a period).
The Interpretation row (its F2) applies it to periods of every unit, and its module offers a version with and a version without (c).
Days of rest, recess or holiday are an input, a function from DATE to BOOLEAN, never computed here.
The choice made, kind by kind:
- **(i) A deadline for doing something, applied.** These are s. 16 (30 days to notify the Registrar) and s. 17(c) (an extension of at most three months, "לשם מילוי החובה"). The text and its evident purpose agree: a person must be able to act on the last day.
- **(ii) A period of validity, applied.** These are s. 8's five years and s. 9's year, with each renewal. The text is unqualified, and a licence is a period in which a right is exercised. The consequence: a licence whose anniversary is a day of rest stays in force through it, to the first day that is not one. s. 8's other limb, "עד 31 במרץ", is a fixed day, not a counted period, so (c) does not move it; it can then be the earlier limb.
- **(iii) The day an enactment or provision begins or stops binding, NOT applied.** These are s. 63(a)(1)-(2) and (b), reg 5 of the Fees Regulations, and the Second Schedule's column C. Nothing is done within the period, and no one loses an act by its ending on a day of rest. The one published commencement date in the sources, Wikisource's "16.7.2025" for reg 5, is the plain count. This is a reading against unqualified words, so it is made visible: `eighteen months from the commencement day, if s 10(c) applied to a commencement, …` gives the other answer. With Saturdays as rest days it moves s. 63(a)(2) from Saturday 16 January 2027 to Sunday 17 January 2027 (asserted in `tests-law.l4`).

**F32 — "תחילתו … שלושה חודשים מיום פרסומו", "תחילתן … 7 ימים מיום פרסומן": which day is the commencement. Added 2026-10-13.**
Readings: the commencement is the last day of the counted period, or the day after it ends.
Taken: the last day. Reg 5 so counted gives 16 July 2025, which is the day Wikisource's note gives and the day the rest of this encoding already used. The other reading would make it 17 July 2025, and the s. 63 dates a day later each.
s. 10 says where a period ends; it does not say whether a commencement "N days from" a day falls on that end or after it.

**F33 — windows counted backwards. Added 2026-10-13.**
Interpretation Law s. 10 speaks only of periods "from" a day and "after" an event (the Interpretation row's F8). It does not reach these:
- s. 9(a)(2), "בשש השנים שקדמו להגשת הבקשה";
- the Second Schedule's "שנת ניסיון במצטבר מתוך שלוש שנים … טרם הגשת הבקשה" and its seven-year twin;
- s. 17(a), "השנה האחרונה לתוקפו של הרישיון";
- reg 3, "בחודש שלפני תחילתן" and "בחודש נובמבר שקדם ליום העדכון".
The first two stay recorded facts about the applicant. The last two keep the counting they had: s. 17(a)'s year begins the day after the same date one year before its end (F20), and reg 3 names calendar months.

**F34 — several rest days in a row at the end of a period. Added 2026-10-13; OPEN in the Interpretation row (its F3).**
"הימים האחרונים" is plural, and the text says what is not counted, not what to do.
This row uses the module's reading A: the period runs on to the first day, from the nominal last day on, that is not a rest day.
Under the Friday-and-Saturday calendar, for example, a 30th day falling on a Friday runs on to Sunday (asserted for s. 16).
The Interpretation row's reading B, which adds one day per trailing rest day, would give Monday in that case.
Its reading C, which ends the period before the rest days, would give Thursday.
Neither is computed here.

**F35 — the grant day and the validity period. Added 2026-10-13.**
A licence is in force from the day it is granted. s. 10(b) counts its five years (or s. 9's year) after the grant, so the period ends on the anniversary, and the anniversary is inside it.
Read together, a licence is in force on the grant day and on every day to the anniversary: five years and one day of calendar days, or for s. 9, 366 days in a common year.
That is what the two texts give together; neither says the grant day is outside the licence.

**F36 — Interpretation Ordinance s. 17 reaches the Fees Regulations. Added 2026-10-13.**
They are regulations made under a statutory power (ss. 59-60 of the Law), with the Knesset committee's approval, and published in Reshumot. They are therefore taken to be "תקנות בנות־פעל תחיקתי", regulations of legislative effect, which is the class s. 17 governs.
As made, reg 5 is the "other provision" that fixes the day; KT 12383 has none, so publication decides (F10).

## 8. What `check.sh` prints

Run with `L4=<the pinned binary> ./check.sh`, on the l4 built 2026-10-13 16:13 from l4-ide `unstable`, with `JL4_LIBRARY_PATH` unset:

As of the 2026-10-13 date correction (§11); the as-run numbers are in §10:

```
module                                    errors satisfied  failed  refused  expected
domain.l4                                      0         0       0        0         0
fees-regulations.l4                            0         0       0        0         0
il-interpretation-time.l4                      0         0       0        0         0
law-commencement.l4                            0         0       0        0         0
law-duties.l4                                  0         0       0        0         0
law-licensing.l4                               0         0       0        0         0
second-schedule.l4                             0         0       0        0         0
simplex-scenarios.l4                           0         0       0        0         0
tests-fees.l4                                  0       106       0        0         0
tests-law.l4                                   0       121       0        0         0
tests-simplex-draft.l4                         0        12       0        0         0
tests-simplex-red.l4                           2         0       2        0         2
TOTAL (12 modules)                             2       239       2        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit status 0.
The two errors are the two failed assertions of `tests-simplex-red.l4`, at its lines 27 and 30, and both are expected: they are the table's expectations that do not hold as made.
No module raises any warning.
The 8 `#TRACE` directives were read by hand:
- s. 3: unlicensed work, breached.
- s. 6: grant on day 10, fulfilled.
- s. 16: day 30 fulfilled and day 31 breached with no rest days; day 31 fulfilled for a change on 4.3.2027 with Saturdays as rest days.
- s. 17: day 200 fulfilled; nothing by day 366, breached.
- reg 4: unpaid exam allowed, breached.
The count is of `#ASSERT` directives. `tests-fees.l4` has 106 and `tests-law.l4` has 121, all satisfied. Between them they hold 8 `#ASSERT REFUSED` directives (6 and 2), each satisfied by the refusal it names.

## 9. Open questions for a domain expert

- **Q1.** Did KT 12383 mean to leave an objection to a practical-exam grade with no fee? It might instead have meant to abolish such objections, or simply not considered them (F4).
- **Q2.** On what day did KT 12383 come into force? It has no commencement clause (F10). *Answered 2026-10-13 by Interpretation Ordinance s. 17: the day of publication, 4 May 2026. A reviewer should confirm that the Ordinance reaches these Regulations (F36).*
- **Q3.** Was a notice under reg 3(b) published for 1 January 2026, and with what amounts? The index figures for June 2025 and November 2025 are needed for the 2026 amounts.
- **Q4.** Is the fifth year of s. 8 the year of grant plus five or plus four (F16)? And how is a renewed period measured (F17)? (The day the five years end is now settled by Interpretation Law s. 10(b); these two questions are not.)
- **Q5.** Is the 50-hour course of Part A item 3 the same course as those of Part B items 5-6 and Part C item 7 (F15)?
- **Q6.** May an experienced applicant take the no-prior-training route (F13)?
- **Q7.** Does a course longer than "עד N שעות" still meet column B (F15)?
- **Q8.** Does reg 4 reach the temporary licence, whose fee is charged on the application (F7)?
- **Q9.** Under reg 3, which way does a half shekel round (F9)?
- **Q10.** Was the draft in the SimpLEX figure ever an official draft? The paper calls the figure "an illustration".
- **Q11.** Are draft reg 4's words available? Only the panel's gloss of them is in the sources (F2).
- **Q12.** Does Interpretation Law s. 10(c) apply to a licence's period of validity, and to a statute's commencement, as it does to a deadline (F31)? This row applies it to validity and not to commencement; the words do not distinguish them.
- **Q13.** When several days at the end of a period are rest days, does the period run on to the first working day (taken), add one day per rest day, or end before them (F34)?
- **Q14.** Does a commencement "N days (or months) from" a day fall on the last day of the period or the day after (F32)?

## 10. Provenance of this run (added by the launching session, not by the encoder)

Everything above this heading was written by the encoder.
This section was added afterwards by the Claude Code session that launched and checked the run, on 2026-10-13.

**How the row was made.**
One Claude Opus 5.5 agent (Agent tool, `model: opus`, default effort), working alone in a cleanroom from `BRIEF.md` in this directory, which is THERMOSTAT's brief for this subject with the paths updated.
It is the same brief, the same 13 input files, the same binary and the same effort setting as the sibling row `legalese-sonnet-5.5`, so the model is the only variable between those two.
No ontology agent, no section fleet, no integrator, no independent test author, no refuters.
Its transcript runs 2026-10-13 09:27Z to 10:11Z (17:27 to 18:11 +08), about 44 minutes.
The transcript records 260 requests, all on `claude-opus-5-5`, 17,957 output tokens, 2,487,021 cache-write and 118,230,161 cache-read tokens, with a peak context of 640,815 tokens.
The output-token figure sums the per-request usage the transcript records and may undercount; read it as a lower bound.
Dollar cost is not computed here.

**The binary.**
`/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, built 2026-10-13 16:13 from l4-ide `unstable`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187`.
`JL4_LIBRARY_PATH` was unset.

**What the launching session re-ran, rather than taking from the encoder's report.**
`check.sh` with that binary printed the same table the encoder reported: 11 modules, 202 assertions satisfied (104 in `tests-fees.l4`, 86 in `tests-law.l4`, 12 in `tests-simplex-draft.l4`), 0 refused, and 2 failed in `tests-simplex-red.l4`, both expected.
The `#ASSERT` directive counts in those files are 104, 86, 12 and 2; the 104 and 86 include the 6 and 2 `#ASSERT REFUSED` directives the encoder reports, which are satisfied.
No module emits a warning.
The 7 `#TRACE` directives (1 in `tests-fees.l4`, 6 in `tests-law.l4`) are not counted by `check.sh`; the encoder says it read each against its comment, and the launching session did not re-read them.

**Checked against the sources by the launching session.**
Section 5's as-made and as-amended columns, cell by cell, against Kovetz HaTakanot 11951 and 12383: 194, 40, 284 charged on receipt, 398, 158, a theory exam silent as made, and the practical-exam objection fee silent as amended.
The draft column was checked only for 273, 40 and 398, against our own notes of the screenshot, not against the image.
Section 8's five-year limb is read in `law-licensing.l4` lines 110 to 115 as the day before the fifth anniversary, which differs by one day from the sibling rows' anniversary; the comment at lines 94 to 100 and forks F14, F16 and F17 record the readings.

**Cleanroom, and what it was not.**
The encoder's transcript was audited afterwards: its Read, Glob and Grep calls touch only its own `inputs/` and `crops/` directories and the `encoding-a-subject` and `writing-l4-rules` skills, and no tool call names `commons`, `commonswt`, `canon` or `il`.
It read no `example-brief.md`; its one read of `canon-deposit.md` is the only skill file it opened that names this subject's `legalese` row.
Three leaks were not closed: the launching session's memory index, which names this subject, was in the encoder's context; the encoder reports that the harness reset its working directory repeatedly into directories the brief forbids (not checked here); and `canon-deposit.md` points at our `legalese` row as a worked example.
The encoder reports it followed none of them, and its transcript shows no read through any of them.

**Scratch not filed.**
The encoder also wrote `crops/` (image crops, cleaned gazette text, bill text, `l4` outputs; 4.3 MB) and `probe/` (syntax probes) in its working directory.
Neither holds a deliverable, so they are not filed here; `tools/` (`crop.py`, `quotecheck.py`, `reg2-block.l4`) is, because `quotecheck.py` is how its Hebrew quotations were checked against the sources.
`tools/reg2-block.l4` is a scratch block, not a module of this row, and `check.sh` does not run it.

**Not done.**
No independent test pass: the 202 assertions share the encoder's one reading of the sources.
Heralds: 9 Hebrew `@nlg:he` lines and no English `@nlg` heralds (the brief made heralds optional).
The First and Fourth Schedules are out of the pinned scope; their answers for a case are recorded facts.
No domain expert has read this row; gate HG1 is not sought.

## 11. Date correction, 2026-10-13

The same agent that wrote the row made this pass, at the launching session's request.
Every period this row counts forward from a day, or after an event, now goes through the Interpretation Law's own rules.
Those rules come from `il-interpretation-time.l4`, vendored byte-identical (`cmp` empty) from `subjects/il/interpretation-law-1981/encodings/legalese-sonnet-5.5/` at commit `313de518`.
The rules are: s. 10(a) for days ("from" a day, that day not counted); s. 10(b) for months and years (ending on the day with the event day's number, inside the period); s. 10(c) for days of rest at the end of a period; s. 8 for "until"; and Ordinance s. 17 for regulations that fix no commencement day.
Expected values were decided from those sections, and from the weekday of each day concerned read off a calendar, before the modules were run.
For this pass the cleanroom of the original brief was lifted for the Interpretation row's files and this row's directory only.

### 11.1 What changed, module by module

| module | change |
| --- | --- |
| `il-interpretation-time.l4` | **new**, vendored unchanged; imported by the five modules below |
| `fees-regulations.l4` | reg 5: seven days from 9.7.2025 counted by s. 10(a) (`regulation 5 — the last of the seven days from publication`), and the commencement taken through Ordinance s. 17 with reg 5 as "the other provision"; was `PLUS 7`. KT 12383's commencement now comes from Ordinance s. 17 with no other provision; it was an assumed constant. A comment marks reg 3's "the month before" as outside s. 10 (F33). |
| `law-commencement.l4` | s. 63's three and eighteen months are counted by s. 10(b) (`s 10 — the last day of a period of … months from the day`); they were `add months`. The s. 10(c) reading not taken is added, used only by a test (F31). |
| `second-schedule.l4` | column C's three years are counted by s. 10(b) and read "up to and including" by s. 8. They were `add years` with `LESS THAN`. `the day the three-year items of the Second Schedule lapse` (16.7.2028, exclusive) became `the last day of the three-year items of the Second Schedule` (16.7.2028, inclusive). A comment marks the experience windows as outside s. 10 (F33). |
| `law-licensing.l4` | s. 8's five years are counted by s. 10(b), (c), and "עד 31 במרץ" is read by s. 8; the limb was the day before the anniversary. s. 9's year is counted by s. 10(b), (c); it was `LESS THAN` the anniversary. A rest-day input (`, when days of rest, recess or holiday are` rest) is added to s. 8, `the licence … is in force on`, the three s. 3 functions and the s. 9 period test. A comment marks s. 9(a)(2) as outside s. 10 (F33). |
| `law-duties.l4` | s. 16 is counted by s. 10(a), (c) through the new `section 16 — the last day for notifying the Registrar of`. The test and the duty take the change and a rest-day input, and the duty's `WITHIN` is computed from the last day. The duty was `WITHIN 30`, with no inputs, and its `BECAUSE` string now cites s. 10. s. 17(c)'s cap is counted by s. 10(b), (c), with a rest-day input; it was `add months`. s. 17(a)'s window is unchanged (F33). |
| `tests-law.l4` | three illustrative rest-day calendars (none; Saturdays; Fridays and Saturdays), with four checks on the calendars themselves; every call updated to the new signatures; five expectations flipped; 35 assertions and 1 trace added |
| `tests-fees.l4` | 2 assertions added (reg 5's seventh day; KT 12383's commencement) |
| `NOTES.md`, `encoding.json` | §§ 1-4, 7-9 updated where they had become false; this section; counts and module list |

Not changed: `domain.l4`, `simplex-scenarios.l4`, `tests-simplex-draft.l4`, `tests-simplex-red.l4`, `check.sh`, `SOURCE-LICENSE.md`.
The red file still holds its two expected failures. They are about fees, not dates, and no date change touches them.

### 11.2 Every expectation that moved

| test | old | new | citation |
| --- | --- | --- | --- |
| s. 8: last day of a licence granted 15.2.2025 | 14.2.2030 | **15.2.2030** | Interpretation Law s. 10(b): the five years end on the anniversary, inside the period |
| s. 8: last day of a licence granted 31.3.2025 | 30.3.2030 | **31.3.2030** | s. 10(b); "עד 31 במרץ" by s. 8 gives the same day |
| Second Schedule item A2 met on 16.7.2028 (220-hour worker, grade 1) | not met | **met** | s. 10(b): three years from 16.7.2025 end on 16.7.2028, inside the period |
| items of Part A open on 16.7.2028 (same worker) | `LIST 1` | **`LIST 1, 2`** | s. 10(b) |
| s. 9: a period 1.1.2027 to 1.1.2028 does not exceed a year | false | **true** | s. 10(b): a year after 1.1.2027 ends on 1.1.2028, inside the period |

One test was re-pointed rather than flipped. The case "the no-prior-training route is open to the experienced, after item A2 has lapsed" moved from 16.7.2028 to 17.7.2028, so that A2 is still gone on its day; its expected value, met, is unchanged.

Re-checked against s. 10 and unchanged:
- s. 8 for grants on 16.7.2025 and 1.4.2025 (31.3.2030 both);
- s. 63, 14.4.2025, 16.7.2025 and 16.1.2027;
- reg 5, 16.7.2025;
- s. 16, a change on 1.3.2027: 31.3.2027 in time, 1.4.2027 late;
- s. 17(c), 30.6.2030 within the power, 1.7.2030 not;
- s. 3, a licence granted 1.4.2026: in force 31.3.2031, lapsed 1.4.2031;
- the Fees Regulations in force on 4.5.2026.

Added, each decided from the statute first (in `tests-law.l4` unless marked):

| case | expected | citation |
| --- | --- | --- |
| s. 63(a)(2) under the reading not taken, Saturdays rest | 17.1.2027 (16.1.2027 is a Saturday) | s. 10(b), (c); F31 |
| s. 8, granted 15.2.2025, Saturdays rest | 15.2.2030 (a Friday) | s. 10(b), (c) |
| s. 8, granted 15.2.2025, Fridays and Saturdays rest | 17.2.2030 | s. 10(b), (c); F34 |
| s. 8, granted 30.3.2025, no rest days / Saturdays rest | 30.3.2030 / 31.3.2030 | s. 10(b), (c) |
| s. 8, granted 30.3.2025, 30 and 31 March 2030 listed as holidays | 31.3.2030 (31 March is fixed, not moved) | s. 8, s. 10(c); F31 |
| column C's last day | 16.7.2028; item A2 not met on 17.7.2028; `LIST 1` open on 17.7.2028 | s. 10(b) |
| s. 9: 1.1.2027 to 2.1.2028 | false / true / true (no rest / Saturdays / Fridays and Saturdays); 3.1.2028 false (Saturdays) | s. 10(b), (c) |
| s. 3, licence granted 15.2.2025 | may work 15.2.2030; prohibited 16.2.2030 with no rest days; may work 16.2.2030 and prohibited 18.2.2030 with Fridays and Saturdays | s. 10(b), (c) |
| s. 16, change 4.3.2027 (30th day Saturday 3.4.2027) | last day 3.4.2027 / 4.4.2027 (no rest / Saturdays); notice on 4.4.2027 late / in time / in time; 5.4.2027 late | s. 10(a), (c) |
| s. 16, change 3.3.2027 (30th day Friday 2.4.2027), notice on 4.4.2027 | late with Saturdays only; in time with Fridays and Saturdays | s. 10(a), (c); F34 |
| s. 16 duty, change 4.3.2027, Saturdays rest, act on day 31 | FULFILLED (trace) | s. 10(a), (c) |
| s. 17(c), validity ending 29.3.2030, extension to 30.6.2030 | outside / inside / inside (no rest / Saturdays / Fridays and Saturdays); to 1.7.2030 outside | s. 10(b), (c) |
| `tests-fees.l4`: reg 5's seventh day; KT 12383 in force | 16.7.2025; 4.5.2026 | s. 10(a); Ordinance s. 17 |

### 11.3 Forks added or revised

- **Revised:** F10 (settled by Ordinance s. 17), F14 (corrected), F16 (still a fork; note added), F17 (corrected), F19 (settled), F20 (note), F21 (counted by s. 10; dates unchanged), F29 (corrected).
- **Added:** F31 (s. 10(c) by kind of period), F32 (a commencement falls on the period's last day), F33 (backward windows, outside s. 10), F34 (trailing rest days, reading A; open), F35 (grant day plus a period after it), F36 (Ordinance s. 17 reaches the Fees Regulations).
- **Open questions:** Q2 answered; Q4 narrowed; Q12 to Q14 added.

### 11.4 What `check.sh` prints after the correction

```
module                                    errors satisfied  failed  refused  expected
domain.l4                                      0         0       0        0         0
fees-regulations.l4                            0         0       0        0         0
il-interpretation-time.l4                      0         0       0        0         0
law-commencement.l4                            0         0       0        0         0
law-duties.l4                                  0         0       0        0         0
law-licensing.l4                               0         0       0        0         0
second-schedule.l4                             0         0       0        0         0
simplex-scenarios.l4                           0         0       0        0         0
tests-fees.l4                                  0       106       0        0         0
tests-law.l4                                   0       121       0        0         0
tests-simplex-draft.l4                         0        12       0        0         0
tests-simplex-red.l4                           2         0       2        0         2
TOTAL (12 modules)                             2       239       2        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit status 0. A grep of every module's output for `DiagnosticSeverity_Warning` finds none.
The `#ASSERT` counts are 106, 121, 12 and 2, equal to the satisfied and failed columns.
The 8 traces were read by hand (§8).

### 11.5 Still open

- F31: whether s. 10(c) reaches validity periods and commencements; the words do not distinguish them (Q12).
- F34: the trailing-run reading; it is open in the Interpretation row too (Q13).
- F32: which day a commencement "N days from" a day falls on (Q14).
- F16 and F17: the fifth year, and how a renewed period is measured (Q4).
- F36: that Ordinance s. 17 reaches these Regulations.
- The vendored module's own sources and forks are that row's. This row did not re-check its s. 10 text against the official PDF; the launching session reports that it was.
- Interpretation Law s. 21 (a statute binds from 00:01 on its commencement day) is not used. This row works in whole days, so it does not change any answer here.

### Verification of the date correction (added by the launching session, 2026-10-13)

Everything in section 11 above this heading was written by the encoder; this paragraph was added afterwards.

Re-run with the binary named in section 10: `check.sh` printed the table the encoder reported, 12 modules, 239 assertions satisfied (106 in `tests-fees.l4`, 121 in `tests-law.l4`, 12 in `tests-simplex-draft.l4`), 0 refused, 2 failed in `tests-simplex-red.l4`, both expected.
The `#ASSERT` directive counts in those four files are 106, 121, 12 and 2, and no module emits a warning.
`il-interpretation-time.l4` here is byte-identical to the Interpretation Law subject's copy.
Section 10 is unchanged by the correction.
Every as-run assertion that was removed or edited was paired with its closest replacement and compared for polarity and expected value: exactly the five changes the encoder lists changed (the s.8 last day for grants on 15.2.2025 and 31.3.2025, item A2 on 16.7.2028 and the items open that day, and the s.9 one-year period ending 1.1.2028); the s.16 and s.17(c) expectations and every other one kept theirs.
The encoder applied s.10(c) to periods of validity and to deadlines but not to commencements (its F31); this row's sibling `legalese` applies it to the one window in which an application is made and not to validity (its F7). Both are open readings, and neither is checked by anyone who knows the law.

