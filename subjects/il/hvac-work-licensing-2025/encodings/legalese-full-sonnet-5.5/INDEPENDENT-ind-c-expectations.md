# ind-c expectations, decided from the sources before opening any encoding module

Author: independent test author `ind-c` (Opus 5.5), 2026-10-13.
Scope: Law ss. 41-57 (Chapter 6), the Third Schedule, s. 63(b) as it gates Chapter 6, the Fees Regulations in three vintages (SimpLEX draft, as made in KT 11951, as amended by KT 12383), and the SimpLEX test table.
Written BEFORE any `gN-*.l4`, `FRAGMENT-G*.md` or other `phase1/` file was opened.
The assignment names `WORK/c/expectations.md`; I write it at `FLEET_DIR/work/ind-c/expectations.md`, because the constraints allow writing only under `work/ind-c/`.

Sources read: `law.wiki` lines 339-464 and 697-726; gazette Sefer HaChukim 3349 page images pp. 193-198 and 205 (rendered by `pdftoppm` to `work/ind-c/pages/`); `kovetz-hatakanot-11951-p2116.txt`; `takanot-12383.txt`; `regulations-fees.wiki`; `fig4-simplex-screenshot.png` and `fig4-page34-400dpi.png` (cropped and enlarged); `interpretation-NOTES.md` ss. 0.1, 3, 4; the bill p. 5 (bill s. 9) for one cross-reference.

Every number below was read from the gazette page image (Law) or from the official KT text (Regulations), not the wiki.
Gazette and wiki agree on every number in my scope (checked: 40,000 / 80,000 (s.41(b)); 30 (s.43); 1/50 per month (s.45(a)); two years (s.45(b)); 1 January, multiple of 10 (s.47(b)); 30 (s.48); 12 (s.50); 30 (s.53); two years (s.54(b)); 45 (s.56); four / two years (s.57(e)); 18 months (s.63(b)); all fourteen cells of the Third Schedule).
The Law's publication date is 14.1.2025 (gazette footer, every page). KT 11951 is dated 9.7.2025; KT 12383 is dated 4.5.2026.

Dates: weekdays were checked with Python's `datetime`; periods are counted by Interpretation Law s.10 as `interpretation-NOTES.md` gives it (s.10(a): N days from D ends on D+N; s.10(b): N months/years after D ends on the same-numbered day, or the month's last day).
s.10(c) is applied per the brief's ruling 4 (deadlines D and windows W: yes; validity V and commencement C: no); where I test a rest-day case I say which kind it is.
Rest days in my scenarios are illustrations chosen by me, not a statement of Israel's calendar.

## A. Third Schedule (s.41(a)): the amount, per row and per kind of violator

Source: gazette p. 205, column A "the provision", column B amount (NIS), sub-columns individual / corporation. A dash means the Schedule fixes NO amount.

| id | row | facts | individual | corporation |
| --- | --- | --- | --- | --- |
| A1 | (1) s.3(a) | engaged person did work with no licence at all | 20,000 | none (dash): no amount, so no sanction (NOTHING or REFUSE; never 0, never 20,000, never 40,000) |
| A2 | (2) s.3(a) | did work without a licence of the type appropriate to that system | 10,000 | none (dash) |
| A3 | (3) s.4 | advertised as licence holder without a licence, or as holder of a kind without that kind | 5,000 | 10,000 |
| A4 | (4) s.13 | licence holder installed a system without the refrigerant-piping leak test of TI 994 part 4 | 20,000 | none (dash) |
| A5 | (5) s.18(a) | operator employed a person who holds no licence at all | 20,000 | 40,000 |
| A6 | (6) s.18(a) | operator employed a person without the licence of the appropriate type | 10,000 | 20,000 |
| A7 | (7) s.31(2) | did not deliver a DOCUMENT on an inspector's demand under s.31(2) | 3,000 | 6,000 |

That is 14 cells, 14 scenarios.

Routes and exclusions (no row, so no sanction under s.41: the Memuneh has no amount to impose):

- A8. A licence holder breaches s.13 other than by skipping the leak test on installation (for example maintenance not in accordance with TI 994 part 5): not in the Schedule; no sanction.
- A9. A person fails to give INFORMATION (ידיעה) demanded under s.31(2): row (7) names only a document (מסמך); no sanction.
- A10. A person refuses to give name and address under s.31(1): no row; no sanction.
- A11. Breach of s.12 (transferring a licence), s.14 (showing the licence), s.16 (updating details within 30 days), s.17 (training), s.18(b) (operator's duty to ensure the standard): no row; no sanction.
- A12. A person who holds a grade 1 licence (up to 18 kW) works on a 50 kW system: row (2), 10,000 (individual).
- A13. A person with no licence at all: row (1), 20,000. (Whether row (2) also describes him is in the ambiguity file, X1.)
- A14. An operator employs a grade 2 holder on a system above 70 kW: row (6): 10,000 individual / 20,000 corporation. Employs someone with no licence: row (5).

## B. s.41(b): the power to amend the Third Schedule (a power of the Minister)

Preconditions: consent of the Minister of Justice AND approval of the Knesset Labour and Welfare Committee AND every amount in column B at most 40,000 (individual) / 80,000 (corporation).

- B1. order sets an individual amount of 40,000, both approvals: permitted.
- B2. 40,001 individual, both approvals: not permitted.
- B3. corporation 80,000: permitted; B4. corporation 80,001: not permitted.
- B5. corporation 50,000 (above the individual cap but under the corporation cap): permitted.
- B6. no Minister of Justice consent (amount 10,000): not permitted. B7. no committee approval: not permitted.
- B8. The caps limit the ORDER, not the sanction imposed: a repeated and continuing row (1) violation can total more than 40,000 (see C9).

## C. ss.45, 46, 47: the amount actually imposed

s.45(a): continuing violation adds one fiftieth (החלק החמישים) of the fixed sanction for each month the violation continues.
s.45(b): repeat violation adds an amount equal to the fixed sanction; "repeat" = a violation of the same provision within two years of the previous violation of that provision for which a sanction was imposed or the violator was convicted.

- C1. row (1) individual, continues 3 whole months: 20,000 + 3 x 400 = 21,200.
- C2. row (3) individual, 1 month: 5,000 + 100 = 5,100.
- C3. row (7) corporation, 2 months: 6,000 + 2 x 120 = 6,240.
- C4. row (5) corporation, 12 months: 40,000 + 12 x 800 = 49,600 (above the s.41(b) cap; allowed, B8).
- C5. row (6) corporation repeat: 20,000 + 20,000 = 40,000. C6. row (7) individual repeat: 6,000.
- C7. 0 months of continuation and not a repeat: the fixed amount (row (2) individual: 10,000).
- C8. A previous violation of the same provision for which NO sanction was imposed and no conviction (for example only a warning, outside s.54): not a repeat under s.45(b): no addition.
- C9. row (1) individual, repeat AND continuing 3 months: 20,000 + 20,000 + 1,200 = 41,200 (each addition is computed on the fixed sanction "הקבוע לאותה הפרה"; the other reading is X5).

Repeat window, s.45(b) "בתוך שנתיים מההפרה הקודמת": two years after the previous violation, s.10(b) (unit: years), anchored on the date of the previous VIOLATION (not of the sanction).
Not a deadline, window for a request, validity or commencement; I apply no s.10(c) and use no rest days.

- C10. previous violation 2027-03-10 (sanctioned), new violation 2029-03-10: repeat. C11. new violation 2029-03-11: not a repeat.
- C12. previous violation 2028-02-29, new 2030-02-28: repeat (February 2030 lacks the 29th, so the period ends 2030-02-28). C13. new 2030-03-01: not a repeat.
- C14. different provision (previous s.4, new s.18(a)), within the window: not a repeat.
- C15. previous sanction imposed 2028-06-01 for a violation committed 2027-03-01; new violation 2029-04-01: NOT a repeat (more than two years after the previous violation, though less than two after the sanction).

s.46(a)/(b): the Memuneh may not impose less than the fixed amounts, except under circumstances and rates the Minister sets (with the consent of the Minister of Justice and approval of the committee).

- C16. no s.46(b) rules exist: a reduced amount is not permitted. C17. rules exist and their circumstances apply: reduction permitted (the rate is the rules' input).
- C18. s.46(b) rules made without the Minister of Justice's consent, or without the committee: not a valid exercise of the power.

s.47(a): which date's updated amount applies.

- C19. Violator argued (s.43): the amount updated as at the day the payment demand is delivered.
- C20. Violator did not argue (s.44(d)): the amount as at the day the NOTICE OF INTENT was delivered. Discriminating case: notice delivered 2027-12-20, no arguments, deemed demand 2028-01-19: the 2027 amounts apply, not the 2028 (1 January 2028 update) amounts.
- C21. Appeal filed and payment stayed (by the Memuneh or the court): the amount as at the day of the decision in the appeal.

s.47(b): annual update on 1 January by the change in the CPI known on the update day against that known on 1 January of the previous year, rounded to the NEAREST multiple of 10 NIS.

- C22. 3,000 with index 100 -> 101.7: 3,051 -> 3,050.
- C23. 20,000 with 100 -> 102.49: 20,498 -> 20,500.
- C24. 10,000 with 100 -> 102.36: 10,236 -> 10,240.
- C25. 6,000 with 100 -> 101.84: 6,110.4 -> 6,110.
- C26. A falling index (100 -> 99): 20,000 -> 19,800 (the text says "change", not "rise").
- The half-way case (5,000 with 100 -> 102.3 = 5,115) is in the ambiguity file (X6).
- s.47(c): the Memuneh SHALL publish the updated amounts in Reshumot (duty).

## D. Procedure and deadlines: ss. 42, 43, 44, 48, 49, 50, 52, 53, 54, 56

s.42: the Memuneh, with reasonable grounds and an intent to impose, MUST deliver a written notice of intent with at least (1) the act and its date, (2) the amount and the period for payment, (3) the right to argue and the s.44(d) deeming, (4) the power to add for a continuing or repeat violation and the rate.

- D1. a notice that omits any one of (1)-(4) does not meet s.42(b). D2. with all four: meets it.

s.43: arguments in writing within 30 days of the delivery of the notice; s.10(a); a window to make a request (W), so s.10(c) applies by the fleet default.

- D3. notice delivered 2027-03-01: last day 2027-03-31 (Wed). Arguments on 2027-03-31: in time. D4. on 2027-04-01: late (unless extended).
- D5. notice delivered 2027-02-04: nominal last day 2027-03-06 (Saturday). With 2027-03-06 a rest day: last day 2027-03-07 (Sunday), so arguments on 2027-03-07 are in time; without s.10(c) (the alternative) they would be late.
- D6. Extension: the Memuneh MAY extend, only for special reasons that are recorded; special reasons not recorded: no extension.

s.44: the Memuneh decides after considering the arguments; imposing: a written payment demand with the updated amount, the period for payment and reasons; not imposing: a written notice with reasons.

- D7. s.44(d): no arguments within the s.43 period: the notice of intent is deemed a payment demand delivered at the end of that period. Notice 2027-03-01: deemed demand 2027-03-31.

s.48: pay within 30 days of the delivery of the payment demand (deadline D: s.10(a) and s.10(c)).

- D8. demand delivered 2027-05-10: last day 2027-06-09. Paid 2027-06-09: on time. D9. paid 2027-06-10: late (s.49 interest and arrears apply).
- D10. compound with s.44(d): notice 2027-03-01, no arguments: deemed demand 2027-03-31, last day to pay 2027-04-30.
- D11. demand delivered 2027-02-04: nominal last day Saturday 2027-03-06; with that day a rest day: 2027-03-07.

s.49: late payment carries shekel interest and arrears under the Interest and Linkage Law (out of scope: the rate is an input). D12. paid on time: no interest; paid late: interest applies.

s.50: instalments, at the violator's request, considering the amount and special circumstances, at most 12 monthly payments.

- D13. 12 instalments requested: may be granted. D14. 13: may not. D15. no request by the violator: the power does not arise.
- D16. s.50(b): one instalment missed: the instalment decision is void, the balance is due at once, and s.49 applies.

s.52: administrative warning INSTEAD of a sanction, when the Memuneh has reasonable grounds and the circumstances are in procedures the Memuneh set with the approval of the Attorney General (including a deputy the AG authorised for this).

- D17. procedures approved by the AG, circumstances listed: warning permitted. D18. procedures not approved: not permitted. D19. approved by a deputy AG not authorised: not permitted; by an authorised deputy: permitted.

s.53: request to cancel the warning, in writing, within 30 days. The text gives no anchor ("בתוך 30 ימים"); I take the day the warning was delivered (the subsection opens "נמסרה למפר התראה"), and report the missing anchor. Window W: s.10(c) applies.

- D20. warning delivered 2027-03-01: request on 2027-03-31 in time; 2027-04-01 late. D21. grounds: (1) did not commit the violation; (2) the act described is not a violation. Any other ground (for example "the violation was minor"): not a ground under s.53.
- D22. The Memuneh MAY extend for special reasons recorded; decides to cancel or to reject, in writing with reasons.

s.54: after a warning.

- D23. (a) the violator continued the same violation: it is a continuing violation for s.45(a), and the Memuneh MUST deliver a notice of intent.
- D24. (b) repeated within two years of the DELIVERY OF THE WARNING (anchor differs from s.45(b)): warning delivered 2027-04-01, repeated 2029-04-01: a repeat violation (fixed sanction doubled), and the Memuneh MUST deliver a notice of intent. D25. repeated 2029-04-02: not a repeat by s.54(b).
- D26. A warning alone (no sanction, no conviction) plus a repeat within two years of its delivery: doubled via s.54(b), though s.45(b) alone would not double.

s.56: appeal to the Magistrates' Court where the President of the Magistrates' Courts sits, within 45 days of the day notice of the decision was delivered (window W: s.10(c) applies).

- D27. notice delivered 2027-06-01: last day 2027-07-16 (Friday); appeal 2027-07-16 in time; 2027-07-17 late (no rest days).
- D28. notice delivered 2027-06-01, rest days Friday 2027-07-16 and Saturday 2027-07-17: last day Sunday 2027-07-18 (two rest days in a row: the interpretation module's reading A).
- D29. notice delivered 2027-06-02: nominal last day Saturday 2027-07-17; with Saturdays rest: 2027-07-18.
- D30. s.56(b): filing does not stay the decision unless the Memuneh agreed or the court ordered. D31. s.56(c): appeal allowed after payment: refund of the amount refunded or reduced, with shekel interest from the day of payment to the day of return.

## E. s.55: one act, several violations

- E1. One act that constitutes two violations listed in the Third Schedule: at most ONE sanction. E2. One act already sanctioned under another law: no sanction under this Law. Which of the two amounts is imposed is not stated (X4).

## F. s.57: publication

- F1. A sanction imposed: the Memuneh MUST publish (1) the imposition, (2) the nature, date and circumstances of the violation, (3) the amount, (4) if reduced, the circumstances and rates of reduction, (5) relevant details of the violator, (6) the name only if the violator is a corporation.
- F2. individual violator: the name is NOT published under (a)(6). F3. it may be published under (c) only if the Memuneh considers it necessary to warn the public AND gave the violator an opportunity to argue the point; if that opportunity was the s.43 hearing, only if the notice of intent announced the intention to publish the name.
- F4. information a public authority is barred from disclosing under FOI s.9(a): must not be published; under s.9(b): may be withheld.
- F5. appeal filed: publish the filing and its outcome.
- F6. Period of publication (s.57(e)), validity kind V, no s.10(c): corporation four years, individual two years, from the day of publication (anchor not stated; I take publication). Published 2027-05-10: individual through 2029-05-10, corporation through 2031-05-10 (a Saturday; no extension, V kind). On 2029-05-11 the individual's details must be made unviewable.

## G. Commencement of Chapter 6 (s.63(b), with s.63(a)(1))

- G1. "the commencement day" (יום התחילה) = later of three months after publication (14.1.2025 -> 14.4.2025) and the coming into force of the s.59 regulations (16.7.2025): 2025-07-16.
- G2. Chapter 6 commences 18 months after that day (C kind, no s.10(c)): 2027-01-16 (a Saturday), or on the coming into force of regulations under s.46, whichever is later.
- G3. s.46 regulations in force 2026-12-01: Chapter 6 commences 2027-01-16. G4. s.46 regulations in force 2027-03-01: commences 2027-03-01.
- G5. A violation on 2027-01-15 (Chapter 6 not in force): no sanction, no warning. On 2027-01-16 with G3: the chapter applies.
- G6. With s.10(c) applied (the rejected alternative, C kind) and Saturdays rest: 2027-01-17.
- The case where no s.46 regulations are ever made is X7.

## H. Fees Regulations: amounts in three vintages

Vintages: SimpLEX draft (Figure 4, never in force); as made (KT 11951, published 9.7.2025, reg 5: in force 7 days from publication = 2025-07-16, C kind); as amended (KT 12383, published 4.5.2026, no commencement provision, so Interpretation Ordinance s.17: in force on the day of publication, 2026-05-04).

| id | service | draft | as made | as amended |
| --- | --- | --- | --- | --- |
| H1 | theoretical exam | 273 (reg 2(a)) | silent (no fee; never 273, never 158) | 158 (reg 2(a1)) |
| H2 | practical exam | 194 (2(b)) | 194 (2(a)) | 194 (2(a)) |
| H3 | appeal on the practical-exam grade, each | 40 (2(c)) | 40 (2(b)) | silent (2(b) now covers the theoretical grade only) |
| H4 | appeal on the theoretical-exam grade, each | 40 (2(c)) | ambiguous (X8) | 40 (2(b)) |
| H5 | grant or renewal of a licence (any grade) | 284 (2(d)) | 284 (2(c)) | 284 (2(c)) |
| H6 | application for, or renewal of, a temporary foreign-expert licence | 398 (2(e)) | 398 (2(d)) | 398 (2(d)) |
| H7 | s.17 training course (a s.59 head) | silent | silent | silent |
| H8 | separate fee for filing a licence application (s.59 head) | silent | silent | silent |

- H9. Totals (the appeal fee is "in addition to" the exam fee): amended, theoretical exam with two appeals: 158 + 2 x 40 = 238. As made, practical exam with one appeal: 234. Draft, theoretical exam with one appeal: 313.
- H10. Which vintage is in force on a date: 2025-07-15: none; 2025-07-16: as made; 2026-05-03: as made; 2026-05-04: as amended. The draft is never in force.

## I. Fees Regulations: reg 3 (update) and reg 4 (payment as a condition)

Reg 3: amounts updated each 1 January by the change of the "new index" (published in the November before the update day) against the "base index" (published in the November before the previous update day; for the first update day after commencement, the index published in the month before commencement), rounded to the nearest WHOLE SHEKEL.

- I1. 284 with 100 -> 101.7: 288.828 -> 289 (not 290: that would be the s.47(b) rounding).
- I2. 194 with 100 -> 103: 199.82 -> 200. I3. 398 with 100 -> 102.5: 407.95 -> 408. I4. 158 with 100 -> 103.1: 162.898 -> 163.
- I5. First update day after commencement (2025-07-16) is 2026-01-01; base index: the one published in June 2025; new index: the one published in November 2025. Second update day 2027-01-01: base November 2025, new November 2026.
- The half-way case (40 with 100 -> 101.25 = 40.5) is X6.

Reg 4: the Registrar shall not grant or renew a licence for which a fee is set, and the Professional Training Division shall not allow an exam or an appeal for which a fee is set, unless the fee is paid IN FULL.

- I6. licence: paid 283 of 284: refused; 284: not barred by reg 4; 300: not barred.
- I7. practical exam: 193: not allowed; 194: allowed (all three vintages).
- I8. theoretical exam, as made: no fee is set, so reg 4 does not bar it: allowed with nothing paid. As amended: 157 not allowed, 158 allowed. Draft: 272 not, 273 allowed.
- I9. appeal on a practical-exam grade: as made 39 not, 40 allowed; as amended no fee is set, so allowed with nothing paid.

## J. The SimpLEX test table (Figure 4, rows 5-8, and the worked example)

Read from the screenshot: relevant provisions "Law s.9 | Regulations 2(a)-(e)".

| id | row | scenario | draft (expected by SimpLEX) | as made | as amended |
| --- | --- | --- | --- | --- | --- |
| J5 | 5 | registers for the theoretical exam (fee paid) | approved, reg 2(a), fee 273 | approved, no fee due | approved, fee 158 |
| J6 | 6 | registers for the practical exam (fee paid) | approved, reg 2(b), 194 | approved, 194 | approved, 194 |
| J7 | 7 | appeal with payment (40) | appeal examined, reg 2(c) | examined (practical-exam appeal) | examined (theoretical-exam appeal) |
| J8 | 8 | registers for an exam without paying | service refused, reg 4 | practical: refused; theoretical: NOT refused (no fee set) | refused (both exams) |
| J9 | worked example | registers for the theoretical exam, does not pay | registration rejected, must pay | NOT rejected under reg 4 (no fee for the theoretical exam as made) | rejected, must pay |

## Counts

| part | scenarios |
| --- | --- |
| A Third Schedule (14 cells + 7 routes) | 21 |
| B s.41(b) | 8 |
| C ss.45-47 | 26 |
| D ss.42-44, 48-50, 52-54, 56 | 31 |
| E s.55 | 2 |
| F s.57 | 6 |
| G commencement | 6 |
| H fees amounts (8 services x 3 vintages = 24 cells, + totals, + vintage-in-force) | 30 |
| I reg 3 and reg 4 | 9 |
| J SimpLEX (5 rows x 3 vintages) | 15 |
| total | 154 |

## Ambiguities (both readings; these go to `ind-c-tests-ambiguous.l4` if the encoding takes one of them)

- X1. Rows (1)/(2) and (5)/(6): does "without a licence of the appropriate type" also describe someone with no licence at all? Reading A (taken): rows are exclusive, (1)/(5) for no licence, (2)/(6) for a wrong-type licence. Reading B: no licence satisfies both; s.55 then allows one sanction, amount unstated.
- X2. "the same provision" in s.45(b): the section (s.3(a) for rows (1) and (2) alike; s.18(a) for (5) and (6)) or the Schedule row (column A is headed "ההוראה"). Discriminating case: row (2) violation within two years after a sanctioned row (1) violation: repeat under the section reading, not under the row reading.
- X3. s.45(a) "for each month in which the violation continues": a part month counts (each month touched) or only whole months; and calendar months or months counted from the violation. Discriminating: 1.5 months: 2 x 1/50 or 1 x 1/50.
- X4. s.55: which sanction is the one imposed (the highest? the Memuneh's choice?).
- X5. Repeat and continuing together: 1/50 of the fixed sanction (41,200 for C9) or of the doubled sanction (42,400).
- X6. Rounding a half: s.47(b) 5,115 -> 5,110 or 5,120; reg 3 40.5 -> 40 or 41.
- X7. s.63(b) when no s.46 regulations are ever made: Chapter 6 never commences ("whichever is later" of a date that never comes), or it commences at 18 months. The text says nothing; a power the Minister "may" exercise gates the whole chapter.
- X8. As made, reg 2(b) "השגה על ציון הבחינה" (the exam's grade): the only exam the as-made text names is the practical one, so either the practical exam only (theoretical appeal: silent) or any exam (theoretical appeal: 40).
- X9. s.44(d) deemed delivery "at the end of that period": on the period's last day (payment due D+60 from the notice) or the moment after it ends (D+61).
- X10. s.53(a) has no anchor for its 30 days; taken as the delivery of the warning.
- X11. s.57(e) has no anchor for the four or two years; taken as the day of publication.
- X12. Row (1) says "עוסק" (one who engages in the occupation); row (2) does not. Whether row (1) reaches a one-off unlicensed performer who is not engaged in the occupation is not said.
- X13. The SimpLEX draft's cross-references: reg 2(e) cites "section 8" for the temporary foreign-expert licence and the worked example cites "section 9(a): requires passing an exam". In the Law AND in the bill as tabled (bill p. 5) the foreign-expert licence is s.9 and s.9(a) has nothing about exams. Draft reg 2(c) adds the appeal fee "to the fee under subsection (a)" (the theoretical exam) even for a practical-exam appeal. These are defects of the draft, not readings.

---

## Postscript, written AFTER the encoding was opened (nothing above this line was changed)

- The Hebrew fragments above were typed while reading; after writing, a script checked each against `inputs/law.wiki` and `inputs/regulations-fees.wiki`: all eleven are verbatim substrings.
- Probes added after reading the encoding, and therefore NOT counted among the 154 pre-decided scenarios: DIS-2 (an act on the day of delivery is within "N days from" it), DIS-3 (an "extension" to an earlier day), DIS-4 (reg 4 and the grant of a temporary licence), DIS-5 (a notice lacking the s.42(b)(3) statements deemed a payment demand), and the both-readings checks of X3, X6 and X9.
- Two pre-decided expectations could not be asserted as written: A10/A11 (breaches with no Third Schedule row) because `Listed violation` admits only the seven items by construction, and D19/D21 because the encoding folds the AG/deputy distinction into one boolean and the s.53 grounds into a two-constructor type.
