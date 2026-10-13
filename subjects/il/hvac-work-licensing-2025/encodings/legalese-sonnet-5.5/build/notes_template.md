# NOTES: the HVAC work-licensing Law 5785-2025 and its Fees Regulations, in L4

**Status: draft.**
No domain expert has read this encoding against the source.
It was written, tested and checked by one Sonnet 5.5 agent working alone from the brief, with no independent test pass, no refuters and no second reader.
Every number below that comes from running something was produced by `check.sh` on @@DATE@@ with the binary named in section 7.
Nothing in this directory has been added to git, committed or pushed.

## 1. What is encoded and what is not

The subject is the Regulation of Engagement in Work on Refrigeration or Air-Conditioning Systems Law 5785-2025 (Sefer HaChukim 3349, p. 182, issue dated 14 January 2025) and the Fees Regulations made under its ss 59-60, in three vintages: the draft shown in the SimpLEX screenshot (Figure 4 of Schwartz, Bar-Siman-Tov and Gelbard 2025), the regulations as made (Kovetz HaTakanot 11951, 9 July 2025) and the regulations as amended (Kovetz HaTakanot 12383, 4 May 2026).
From the Law the pinned scope is encoded: ss 2, 3, 6 with the Second Schedule, 7, 8, 9, 16, 17 and 63.
From the Fees Regulations every regulation is encoded in all three vintages, except where the draft's text is not in the screenshot, in which case a named `REFUSE` says so.
The four rows and the worked example of the SimpLEX test table are transcribed and run against all three vintages.
The Law is encoded in English L4 over the Hebrew gazette text, which is quoted in comments, mechanically, above the rules that encode it.
The three vintages of the Fees Regulations are inputs (`Draft`, `As made`, `As amended`), never merged: where a vintage is silent on a service the answer is `NOTHING`, and where the sources cannot answer the answer is `REFUSE`.

Not encoded, because outside the pinned scope: the First Schedule (which acts need which licence), the Fourth Schedule (the list of flammable refrigerants), the Third Schedule and Chapter 6 (administrative sanctions), ss 4-5, 10-15, 18-62, and the Law's own power to fix fees (ss 59-60) beyond citing it.
What s 3 needs from the First Schedule, and what s 63(a)(1) needs from the Fourth, arrive as facts on the case (see the fields of `Piece of work` and `Refrigerant` in `hvac-nouns.l4`).
Not done: Hebrew `@nlg:he` heralds (they were optional), an independent test pass, and any export or `l4 nlg` run.

## 2. Files

@@FILES@@

Import order: `hvac-nouns` first (nouns only, no rules); then `hvac-fees-regs`; then the Law in the order `hvac-law-s63-commencement`, `hvac-law-s6-second-schedule`, `hvac-law-s8-validity`, `hvac-law-s2-s3-licensing-duty`, `hvac-law-s7-s9-exemption-and-temporary-licence`, `hvac-law-s16-s17-duties-of-licensee`; then the tests.
s 63 comes before the Second Schedule because three Schedule rows are "valid three years from the commencement of this Law under s 63(a)(1)".
The Hebrew quotations in the comments of the modules were inserted by a small script from the input files (`quote.py` and `build.py` in the run directory, outside this deposit), so that they are copies and not retypings; the draft's text and the SimpLEX words, which come from an image, are the exceptions and were typed by eye.
`hvac-simplex-scenarios.l4` holds the table's scenarios as named values so that the green and the red tests refer to the same thing.
`hvac-tests-red.l4` holds the seven expectations that are meant to fail (section 7).

## 3. Coverage table

Every in-scope provision, with its disposition.
Dispositions: `encoded`; `inert` (quoted or cited but not operative: a definition naming an office, a power over a schedule's text, a signature block); `refused` (the sources do not answer, so a named `REFUSE` says so); `out-of-scope`.
No row is `deferred`.

Totals: @@COUNTS@@.

@@TABLE@@

A note on the inert rows.
Law s 3(c) and s 6(b) are powers of the Minister to amend the First and Second Schedules by order.
No order amending either is in the sources, so the encoding takes the Schedules as enacted and says so in a comment.
The 13 inert definitions of s 2 name offices and statutes and are the nouns of `hvac-nouns.l4`.

## 4. Answer table: the fee for each service, under each vintage

As I read the sources.
Amounts are the amounts printed in each text, in new shekels.
`silent` means the vintage prescribes no fee for that service (`NOTHING` in the code).
Every cell is asserted in `hvac-tests-fees.l4`.

| service | draft (screenshot) | as made (11951; in force 16 July 2025) | as amended (12383, 4 May 2026) |
| --- | --- | --- | --- |
| a theory exam | 273, draft reg 2(א) | silent: no theory exam is defined or priced (regs 1, 2) | 158, reg 2(א1), inserted by 12383 s 2(1) |
| a practical exam | 194, draft reg 2(ב) | 194, reg 2(א) | 194, reg 2(א) |
| an objection to a theory exam score, per objection | 40, draft reg 2(ג) (worded "ערעור", appeal) | silent: no theory exam | 40, reg 2(ב) as amended, on top of the 158 |
| an objection to a practical exam score, per objection | 40, draft reg 2(ג) | 40, reg 2(ב) ("על ציון הבחינה") | **silent**: reg 2(ב) as amended reaches "ציון הבחינה העיונית" only |
| an application for a licence or its renewal under s 5 | 284, draft reg 2(ד) ("בעד בקשה") | silent: reg 2(ג) charges for receiving, not applying | silent: same |
| receiving a licence or its renewal under s 5 | silent: draft 2(ד) charges for the application | 284, reg 2(ג) ("בעד קבלת רישיון") | 284, reg 2(ג) |
| a request for a temporary licence for a foreign expert, or its renewal | 398, draft reg 2(ה), citing s 8 of the Law | 398, reg 2(ד), citing s 9 | 398, reg 2(ד) |
| a refresher training under s 17 | silent | silent | silent |

Four things the table does not say, and the encoding therefore does not either.
First, every printed amount is a base amount: reg 3 updates the amounts in reg 2 on each 1 January by the consumer price index, and the sources contain no index value and no notice under reg 3(b).
So the amount payable from 1 January 2026 is not in the sources, and `the fee payable on` refuses for any day from then on.
Second, the unofficial consolidation (Wikisource rev 3011135) annotates 194, 40, 284 and 398 "(מתואם לשנת 2025)" and 158 "(מתואם לשנת 2026)"; those annotations are the consolidator's, not the gazette's.
Third, the draft is silent in the table only because the screenshot shows its reg 2 in full, (א) to (ה), followed at once by the heading of reg 3; for the services the draft's reg 2 does not mention, silent is a finding and not a gap in the screenshot.
Fourth, the amendment's own commencement date is not in the sources (finding N8), so no date selects the amended column after 4 May 2026.

## 5. Fork register

Every ambiguity met, the readings seen, the one taken and why.
A fork resolved by a court or the regulator would say who settled it; none of these has been settled by anyone I could find in the sources.
The code names the fork code (`F-xx`) wherever a reading is taken.

**F-C1. s 63(a)(1): when is the Commencement Day?**
The text: "שלושה חודשים מיום פרסומו או מועד כניסתן לתוקף של תקנות לפי סעיף 59, לפי המאוחר" (three months from its publication or [the] date of entry into force of regulations under s 59, whichever is later).
Reading B (taken): the later of (publication + 3 months) and (the regulations' entry into force): the later of 14 April 2025 and 16 July 2025, which is 16 July 2025.
Reading A: three months after the later of the two events, which is 16 October 2025.
B is taken because s 63(b), in the same section, says "או במועד כניסתן לתוקף" (or on the date of entry into force) and so plainly means "the later of a period's end and a date"; (a)(1) lacks only the "ב".
The unofficial annotation to (a)(1) gives only the date the regulations commenced (16.7.2025) and does not decide it.
Every date that hangs off the Commencement Day moves with this fork: work on other refrigerants (16 January 2027 against 16 April 2027) and the end of the three-year Schedule rows (16 July 2028 against 16 October 2028).

**F-C2. s 63: a listed flammable refrigerant whose use the law does not permit.**
Reading (i) (taken): it is not "as stated in paragraph (1)", which requires use to be permitted, so it falls under (a)(2) ("קרר שאינו כאמור בפסקה (1)"), 18 months after the Commencement Day.
Reading (ii): neither paragraph applies and the Law has no commencement for work on it.
(i) is taken because (a)(2) is worded as the complement of (a)(1).

**F-D1. The draft's regulation 4.**
The screenshot does not show its text.
The SimpLEX panel glosses it only as "תקנה 4: אוסרת רישום ללא תשלום" (regulation 4 prohibits registration without payment) and gives "השעיית שירות" as the outcome of registering for an exam without payment.
Reading (i): refuse everywhere for the draft's reg 4.
Reading (ii) (taken): encode it from the gloss, for the two exams only, and refuse for every other service.
Taken because the brief asks for row 8 to be asserted against the draft in the table's words.
The consequence is that row 8 against the draft tests the panel's gloss and not the regulation.

**F-D2. One scenario, two outcome words.**
Row 8 says that registering for an exam without payment gives "השעיית שירות" (service suspension).
The worked example says that a candidate who registers for a theory exam and does not pay gets "הרשמה נדחית – חובה להשלים תשלום" (registration rejected, payment must be completed).
Those are the same facts; one function cannot return both.
Taken: the function returns row 8's word, so row 8 is green and the example's result is red (expectations F5 to F7 in `hvac-tests-red.l4`).
The example's other content, that reg 4 prohibits registration without payment, is asserted green.

**F-D3. The last day of "three years from the Commencement Day".**
Reading (taken): the third anniversary, the Commencement Day itself not counted: 16 July 2028 on reading B of F-C1.
Alternative: the day before the third anniversary.
The boundary assertions (16 July 2028 in, 17 July 2028 out) test the taken reading only.

**F-D4. Counting a period measured "from" a day (applies to ss 8, 9, 16, 17 and the Schedule's three years).**
Reading (taken): the day the period runs from is not counted, and the period ends on that date N units later.
So s 16's "30 days from the day of the change" ends on the change day plus 30, and a notice on that day is in time.
Alternative: count the day itself as the first, so the last day is one earlier.
The sources do not state the convention.
It affects only boundary days, and every boundary assertion that depends on it says so in a comment.

**F-F1. "ערעור" (draft) and "השגה" (as made): appeal and objection.**
Treated as the same service, an objection to an exam score.
Nothing numeric turns on it; the SimpLEX outcome word is "the appeal is examined".

**F-F2. The draft charges for the application; the regulations as made charge for receiving the licence.**
Draft 2(ד): "בעד בקשה לקבלת רישיון או לחידושו" (for an application to receive a licence or renew it).
As made 2(ג): "בעד קבלת רישיון או חידושו" (for receiving a licence or renewing it).
Taken: two services, because the two wordings name different moments, and neither vintage is allowed to borrow the other's row.
Alternative: one service priced at 284 throughout.
The code and the table keep them apart.

**F-F3. Is the objection fee on top of the exam fee already paid?**
Reg 2(ב): "ישלם מגיש ההשגה, נוסף על התשלום בעד האגרה כאמור בתקנת משנה (א), סכום של 40 שקלים חדשים, בעד כל השגה".
Reading (taken): in addition to the exam fee already paid, the objector pays 40; an objection costs 40.
Alternative: the objector pays the exam fee over again and 40 on top (194 + 40 = 234).
Taken because the payment "בעד האגרה" is the examinee's payment already made, and because row 7 of the panel says "ערעור עם תשלום (40 ש"ח)", an appeal with payment of 40, and expects the appeal to be examined.

**F-F4. Draft 2(ג) adds the 40 "to the payment for the fee as stated in subsection (א)".**
In the draft (א) is the theory exam fee, yet (ג) covers an appeal on "the theory exam or the practical exam".
Reading (i): the cross-reference points only at (א).
Reading (ii): it is a slip for (א) or (ב).
No per-service amount depends on it (40 either way), so no total payable by an appellant is computed anywhere.

**F-F5. As made, 2(ב) "על ציון הבחינה" (on the exam score).**
The only exam reg 1 defines is the practical exam, so "the exam" is read as the practical exam.
Alternative: any exam score, which changes nothing here because no theory exam exists in this vintage.

**F-F6. As amended: an objection on a practical exam score.**
After 12383 s 2(2), reg 2(ב) says "הוגשה השגה על ציון הבחינה העיונית" and adds the fee to 2(א1).
Reading (i) (taken): no fee is prescribed for a practical-exam objection (`NOTHING`).
Reading (ii): the 40 as made survives by implication; rejected, because 2(ב) was amended in terms to reach the theory exam only, and reg 4 conditions only fees "שנקבעה בעדן אגרה" (for which a fee was set).
Reading (iii): a drafting slip that the sources do not let me confirm.
The 40 as made is not carried over.

**F-F7. Is a temporary licence "a licence for which a fee was set" under reg 4?**
Taken: yes; the fee in 2(ד) is for a request to obtain it, and reg 4 bars the Registrar from giving "רישיון שנקבעה בעדו אגרה".
Alternative: reg 4's "רישיון" reaches only licences under s 5.

**F-L1. "בגיר" (adult), s 6(a)(1).**
The sources do not define adulthood, so it is a recorded fact (`an adult`), not an age threshold I supply.

**F-R3. Reg 3: do the updates compound?**
Reading (taken): each update applies to the amount in force just before the update day, rounded to the nearest whole shekel each year, because the base index is only ever one year back.
Alternative: apply the cumulative index ratio to the original amount.
They can differ by a shekel, and a test shows a case (hypothetical index values) where they do.
An exact half does not fall under "to the nearest whole new shekel", so it refuses.

**F-R5. Reg 5: "7 ימים מיום פרסומן" (seven days from publication).**
Reading (taken): the day of publication (9 July 2025) is not counted, so the regulations commenced on 16 July 2025, which the unofficial annotation also states.
Alternative: count it, giving 15 July.

**F-S1. How does the Second Schedule qualify s 6(a)(4)?**
Text: "אחד התנאים שלהלן, והכול בהתאם לתנאים שבתוספת השנייה".
Reading (taken): the Schedule governs every limb, so it is a further conjunct; as written, limb (c) is then satisfied whenever the Schedule is.
Reading (ii): the Schedule qualifies limb (c) only, so (a) or (b) alone suffice.
The code has both; a registered technician applying for Grade 1 (no Part A row covers a technician) passes on (ii) and fails on (i).

**F-S2. "הכשרה של עד N שעות": a ceiling or a minimum?**
Taken: a ceiling on the training the Division may require, carried as information and compared with nothing.
The applicant has met column B when they have completed the training, whatever its length.

**F-S3. Certificates "with no grade stated".**
Part A item 3, Part B items 5 and 6 and Part C items 6 and 7 speak of "תעודת גמר בלימודי קירור ומיזוג אוויר מהאגף" with no grade.
Taken: kept apart from "דרגה 1/2/3" certificates, as the Schedule keeps them apart, so a Grade 1 training does not satisfy a column B that asks for the training with no grade stated.
Alternative: the ungraded wording covers the graded certificates.
Part C items 6 and 7 thereby give a Grade 3 applicant a training that confers a certificate with no grade stated (finding N10).

**F-S4. At what date is a three-year Schedule row tested?**
Taken: the date of the application, which is also the date the experience windows run back from.
Alternative: the date of grant, or of completing the training.

**F-S5. When several rows apply to an applicant.**
Taken: the applicant may rely on any one of them.
The Schedule does not rank them; alternatives are the most specific, or the first.

**F-T1. The SimpLEX rows do not say which exam.**
Rows 5 and 6 name the exam; rows 7 and 8 do not, and none says the fee was paid for rows 5 and 6.
Taken: rows 5 and 6 are registrations with the fee paid in full; rows 7 and 8 are run for both exams.

**F-T2. s 17(a): "בהיקף של שמונה שעות לפחות".**
Taken: an aggregate across the trainings, because the noun is plural ("בהשתלמויות").
Alternative: eight hours in a single training.

**F-T3. What does "registration approved" mean?**
Reg 2 and reg 4 only remove the payment bar; they approve nothing.
The panel's word reads more into them.
Taken: the word is returned when the fee was paid in full and a fee is set; the encoding says so in a comment.

**F-T4. The worked example's "סעיף 9(א): מחייב מעבר בחינה".**
Section 9(a) of the Law as enacted, and of the bill at third reading (11 December 2024), is the foreign expert's temporary licence and has no exam condition (asserted in `hvac-tests-law.l4`).
The nearest provision that makes passing an exam a condition is s 2 "תעודת גמר" (1), through s 6(a)(4)(a): a Division certificate counts only if its holder passed an exam that included a theory and a practical exam (also asserted).
Taken: the example means that, and it is a mis-citation.
Alternative: it cites an earlier numbering that I could not see (finding N3).

**F-T5. s 9(a)(2): "בשש השנים שקדמו להגשת הבקשה".**
Taken: a performance exactly six years before the application counts; one day more does not.
The six years are tested by adding six years to the performance date, never by subtracting from the application date.

**F-V1. s 8: "עד 31 במרץ של השנה החמישית מהשנה שבה ניתן הרישיון".**
Reading A (taken): the grant year is year 0, so a licence given in 2025 runs to 31 March 2030 at the latest.
Reading B: the grant year is year 1, so it runs to 31 March 2029.
A is taken because under B the five-year limb could never be the earlier one (31 March of the fourth year after is always before the fifth anniversary of any day of the grant year), which would leave "לפי המוקדם" with nothing to choose between.
Under A the five-year limb decides exactly for a grant between 1 January and 30 March.
Both are in the code and both are tested.

**F-V2. s 8: the validity period of a renewed licence.**
A licence "ניתן לחדשו לתקופות תוקף נוספות", and a validity period is defined by a formula that runs from "the year in which the licence was given".
A renewed licence was not given again, so the text does not say when the next period starts or which year its fifth year counts from.
Taken: refuse (`the end of a renewed validity period`); the first-period formula is not borrowed.

**F-V3. s 17: "השנה האחרונה לתוקפו של הרישיון".**
Taken: the twelve months ending on the last day of validity; where validity was extended under (c), the original last day is used.
The boundary day (an attendance exactly one year before the last day counts) is part of the taken reading.

## 6. Findings

These are facts the sources show, not choices of mine.

- **N1 (headline).** As amended, no provision prescribes a fee for an objection on a practical exam score: 12383 narrowed reg 2(ב) to the theory exam score.
- **N2.** The theory exam is priced 273 in the draft, absent from the regulations as made, and 158 as amended: it came back lower than the draft priced it.
- **N3.** The draft's reg 2(ה) cites "סעיף 8 לחוק" for the temporary licence; the Law as enacted and the bill at third reading both put it at s 9, and so does reg 2(ד) as made.
- **N4.** The SimpLEX worked example cites "סעיף 9(א): מחייב מעבר בחינה"; s 9(a) as enacted is not that (F-T4).
- **N5.** The panel gives two outcomes for one scenario (F-D2).
- **N6.** The unofficial Wikisource text of the Law differs from the gazette in the Second Schedule: Part C item 4 collapses column A and column B into one cell behind a stray "(", and Part A item 3's column B loses "מקצועית".
The gazette is authoritative and the figures here are the gazette's.
- **N7.** The sources contain no index value and no notice under reg 3(b), so nothing in them gives the fee payable from 1 January 2026.
- **N8.** 12383 has no commencement provision; the sources do not say when the amendment came into force.
- **N9.** s 59 lets the Minister fix a fee for filing an application, for a licence, for exams including objections and for the s 17 trainings; no vintage fixes one for filing an application as made or amended, or for the trainings.
- **N10.** Part C items 6 and 7 require, of an applicant for Grade 3, training that confers a certificate with no grade stated.
- **N11.** The draft words its Chapter A "מטרה והגדרות" where the regulations as made say "הגדרות", and words the practical exam as an assessment "של התלמיד" where they say "של לומד בקורס הכשרה מקצועית".
- **N12.** The screenshot is low-resolution and the SimpLEX panel is a tool's own display: its outcome words, its glosses and the draft text read from it were transcribed by eye, and may contain misreadings.
- **N13.** The screenshot shows only part of the draft.
It shows reg 1, reg 2(א) to (ה) and the heading of reg 3, and the first panel; it does not show the body of reg 3, reg 4, reg 5, the signature block, or any scenario of the second panel "תרחישי בדיקה לעדכוני אגרות ומדד".

## 7. What `check.sh` prints, and which failures are expected

Binary: `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, built 2026-10-13 16:13 from l4-ide `unstable`, as recorded in the task that produced this encoding (`l4` has no version flag).
`JL4_LIBRARY_PATH` was left unset.

```text
@@CHECK@@
```

`hvac-tests-red.l4` is expected to fail seven times, and `check.sh` counts exactly seven (`expected_failed`).
Those seven are findings, not bugs: no expected value in it was edited to match the code.
F1 to F3 run the draft's rows 5, 7 (theory) and 8 (theory) against the regulations as made, which have no theory exam.
F4 runs row 7 (practical) against the regulations as amended, which dropped the practical-exam objection fee.
F5 to F7 run the worked example's result word against all three vintages (F-D2).
Every other assertion is satisfied, and no assertion refused.
The `#TRACE` directives, which `check.sh` does not count, were run and read: s 3(a) breaches on work without a licence; s 6(a), 7(c), 17(e) leave the standing duty; ss 7(a) and 9(a) (permissions) stand unexercised, with no breach, and clear to FULFILLED when exercised; s 16 is inclusive at day 30 and breaches at day 31, with `WITHIN 20` left after ten days.

## 8. Open questions for a domain expert

- Q1. Is the absence of a fee for an objection on a practical exam score, as amended, intended (F-F6)?
- Q2. Which reading of s 63(a)(1) do the Ministry and the Registrar apply: 16 July or 16 October 2025 (F-C1)?
- Q3. How does the Registrar compute the end of a first validity period (F-V1), and the period of a renewed licence (F-V2)?
- Q4. What does the notice under reg 3(b) say for 2026, and what amounts are payable from 1 January 2026 (N7)?
- Q5. When did the 5786 amendment come into force (N8)?
- Q6. Is the Second Schedule meant to qualify every limb of s 6(a)(4) or only (c) (F-S1), and may an applicant rely on any applicable row (F-S5)?
- Q7. What is the intended result of registering for an exam without payment: service suspension or rejection (F-D2)?
- Q8. Are eight hours of refresher training an aggregate (F-T2)?
- Q9. Has any order under s 3(b), any regulation under s 46, or any order amending a Schedule been made?
- Q10. Is a temporary licence under s 9 a licence for reg 4's purposes (F-F7)?

## 9. How it was checked

Every expected value was taken from the text it cites, and the fee table of section 4 was written from the sources before the code was run.
Where a boundary depends on a registered fork the comment says so.
Eight mutations were applied one at a time to a copy of the modules (a grade limit, the 31 March year, the sunset length, the 70 kW boundary, the eight-hour boundary, the amended theory fee, the publication offset, the Schedule's Part test): every one made at least one test fail, so the tests do bite.
Every Hebrew phrase in the modules was checked mechanically against the input files.
The phrases the check did not find in any text input fall into four classes, and only the first is read by eye.
First, words read by eye from the screenshot: the SimpLEX words, the draft's regulation text and its headings (the screenshot is an image, so no text input can contain them).
Second, phrases I composed or merged from two source phrases (for example "שנקבעה בעדו/בעדן אגרה", which joins "שנקבעה בעדו אגרה" and "שנקבעה בעדן אגרה") and citation labels in test comments such as `(ג) 40`.
Third, three phrases that are in `regulations-fees.wiki` inside annotation templates that the checker's cleaner strips ("מתואם לשנת 2025", "מתואם לשנת 2026", and the note "התקנות פורסמו ביום 9.7.2025, ותחילתן ביום 16.7.2025").
Fourth, nothing else: no phrase that claims to be a quotation was left unmatched.
An independent test pass, as `encoding-a-subject` step 8 recommends, was not done: the @@NASSERT@@ assertions share one reader's reading of the sources, which is the main limit on how far they can be trusted.
