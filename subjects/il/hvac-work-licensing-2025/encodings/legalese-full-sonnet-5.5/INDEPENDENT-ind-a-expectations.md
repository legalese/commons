# ind-a: expectations decided from the sources alone (ss. 1-18, First and Second Schedules, commencement)

Written 2026-10-13 before opening any `gN-*.l4`, any `FRAGMENT-G*.md`, `phase1/PLAN.md` or any other file in `phase1/` other than ASSIGN-IND-A.md, and before reading any other agent's work directory.
Sources read: `inputs/law.wiki` (whole Law), the gazette `sefer-hachukim-3349-pp182-209.pdf` rendered to images (pp. 182-186 for ss. 1-19, pp. 198-205 for s. 63 and the First, Second and Third Schedules; the Second Schedule numbers re-read at 300 dpi), `kovetz-hatakanot-11951-p2116.pdf` (reg 5, publication date), `regulations-fees.wiki`, `interpretation-NOTES.md` ss. 0.1, 3, 4, the bill's reservations list (no explanatory notes in it).
Every number below was read from the gazette image, not from the wiki.

## Conventions used for the expected values

- Periods "from a day" in days: IL s.10(a), start day not counted; "after an event" in months/years: IL s.10(b), same-numbered day (or month's last day), last day inside.
- IL s.10(c) (fleet default, BRIEF ruling 4): applied to a deadline (D) and an application window (W); not to a validity period (V) or commencement (C). Where the alternative changes the answer, both are written.
- Rest days are an input. Where a calendar is needed I use "Saturdays are rest days" as an illustration, and say so.
- Discretions and opinions (the Registrar's opinion of unfitness, "special circumstances", "reasonable time") are inputs stated in the scenario.
- Statutes outside the Law decide "adult" (בגיר), citizenship/residence, electricity licence kinds, height approval: inputs.
- `amb` column: `-` = I think the source answers it; otherwise the alternative answer and why. Ambiguous rows go to `ind-a-tests-ambiguous.l4` only if they fail.

## Gazette dates

| id | fact | value | source |
| --- | --- | --- | --- |
| G-01 | publication of the Law | 2025-01-14 (Tue) | gazette p. 182 header/footer, י״ד בטבת התשפ״ה |
| G-02 | publication of the Fees Regulations | 2025-07-09 (Wed) | Kovetz HaTakanot 11951 p. 2116 footer |
| G-03 | Fees Regs in force "7 days from the day of publication" | 2025-07-16 (Wed) (IL s.10(a): 10th..16th July) | reg 5; the wiki note says the same |

## Commencement (s. 63(a); only as far as my scope needs it)

| id | scenario | expected | provision | amb |
| --- | --- | --- | --- | --- |
| C-01 | the commencement day (יום התחילה): later of 3 months from 2025-01-14 (= 2025-04-14) and 2025-07-16 | 2025-07-16 | s.63(a)(1), IL s.10(b) | - |
| C-02 | counterfactual: s.59 regs in force 2025-03-01 | 2025-04-14 | s.63(a)(1) "לפי המאוחר" | alt 2025-04-15 if commencement is the day AFTER the 3-month period |
| C-03 | work on a system with R-32 (Fourth Schedule item 20), use permitted, on 2025-07-16 | Law applies (commenced) | s.63(a)(1) | - |
| C-04 | same, on 2025-07-15 | not commenced | s.63(a)(1) | - |
| C-05 | work on a system with R-410A (not in the Fourth Schedule) on 2027-01-16 | commenced (18 months after 2025-07-16 = 2027-01-16, a Saturday; no IL s.10(c) for C) | s.63(a)(2) | alt 2027-01-17 (commencement is the day after the period, or IL s.10(c) with Saturday rest) |
| C-06 | same, on 2027-01-15 | not commenced | s.63(a)(2) | - |
| C-07 | a listed flammable refrigerant whose use is NOT permitted by law, on 2026-01-01 | not commenced: falls under (2) ("קרר שאינו כאמור בפסקה (1)") | s.63(a)(1)-(2) | weak alt: (1) |
| C-08 | Second Schedule sunset rows (A2, B4, C5) "in force for three years from the commencement of this Law as in s.63(a)(1)": last day in force | 2028-07-16 (Sun) (IL s.10(b); V, no (c)) | Sch.2 col. C | which date is tested (application date or decision date) is not said |

## s. 1 (purpose): no computable rule; no scenario.

## s. 2 definitions

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S02-01 | grade 1 licence covers a system of cooling capacity 18 kW | TRUE ("עד 18") | IL s.8 speaks of time/quotation only; ordinary "up to" taken inclusive |
| S02-02 | grade 1 covers 18.01 kW | FALSE | - |
| S02-03 | grade 2 covers 70 kW | TRUE | as S02-01 |
| S02-04 | grade 2 covers 70.01 kW | FALSE | - |
| S02-05 | grade 2 covers 5 kW (a higher licence covers a smaller system) | TRUE | - |
| S02-06 | grade 3 covers 5 kW and 5,000 kW | TRUE, TRUE | - |
| S02-07 | grade 1 covers 0.5 kW | TRUE | - |
| S02-08 | completion certificate (1): Division certificate, studies completed, Division exam passed incl. theoretical AND practical | TRUE | - |
| S02-09 | Division certificate where the exam had no practical part | FALSE | - |
| S02-10 | MoE certificate of completing the climate-control track (בקרת אקלים) | TRUE (def. (2)) | - |
| S02-11 | "work on a system" is an action of a kind listed in the First Schedule; measuring energy consumption alone | not "work" (excluded in A1(6), A1(11), B1(8)) | - |
| S02-12 | system: removes heat from a material/space by means of a refrigerant | system iff refrigerant-based heat removal | - |

## s. 3 duty to be licensed

Inputs unless stated: Law commenced for the work (TRUE), no s.3(b) exemption order, licence in force, work in accordance with licence conditions.

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S03-01 | no licence; A1(4) hanging an indoor unit; 5 kW | prohibited | - |
| S03-02 | grade 1; A1(4); 5 kW | permitted | - |
| S03-03 | grade 1; A1(2) connecting piping; 18 kW | permitted | inclusive "עד" |
| S03-04 | grade 1; A1(2); 18.01 kW | prohibited | - |
| S03-05 | grade 2; A2 (= all A1 works) e.g. A1(8) brazing; 70 kW | permitted | inclusive |
| S03-06 | grade 2; A1(8); 70.01 kW | prohibited | - |
| S03-07 | grade 2; A1(8); 10 kW (floor, not band) | permitted | - |
| S03-08 | grade 3; B3(2) treating a refrigerant system; 1,000 kW | permitted | - |
| S03-09 | grade 3; A1(4); 5 kW | permitted | - |
| S03-10 | grade 1; B1(8) chiller check; 15 kW chiller | permitted | - |
| S03-11 | grade 1; B3(3) maintenance: adding oil; 5 kW | prohibited (listed only in row 3, grade 3) | CONTRADICTION: A1(5) lists adding/replacing oil as grade-1 installation work; alt: permitted |
| S03-12 | grade 1; A1(5) adding oil during installation; 5 kW | permitted | - |
| S03-13 | grade 2; B3(2) repairing an electrical component of a refrigerant system; 30 kW | prohibited (only grade 3 row) | OVERLAP with B1(3) (repairing electrical/mechanical components, grade 1): alt permitted |
| S03-14 | no licence; only measuring energy consumption | not prohibited (not "work") | - |
| S03-15 | no licence; Law not yet commenced for this work (R-410A on 2026-06-01) | not prohibited | - |
| S03-16 | grade 1 licence expired | prohibited | - |
| S03-17 | grade 1 licence suspended under s.10 | prohibited | "בידו רישיון": a suspended licence is not one he may act on |
| S03-18 | no licence; system type exempted by a s.3(b) order | not prohibited (subject to the order's conditions) | - |
| S03-19 | grade 3; Registrar's s.10(c) interim order forbids installation works; does installation | prohibited ("בהתאם לתנאי רישיונו ולהוראות לפי חוק זה") | - |
| S03-20 | temporary grade 3 licence (s.9); A1 work on a 100 kW system | permitted | - |
| S03-21 | s.3(b) power: Minister, Council consulted, convinced no risk to public and workers | may make the order | - |
| S03-22 | s.3(b) without consulting the Council | may not | - |
| S03-23 | s.3(b) consulted but not convinced of no risk | may not | - |
| S03-24 | s.3(b) order made: Minister may attach duties/conditions | may | - |
| S03-25 | s.3(c) amend First Schedule by order with approval of the Knesset Labour and Welfare Committee | may | - |
| S03-26 | s.3(c) without committee approval | may not | - |

## s. 4 false advertising

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S04-01 | no licence; holds himself out as a licensee | violation | - |
| S04-02 | grade 1; holds himself out as a licensee (no kind) | no violation | - |
| S04-03 | grade 1; holds himself out as grade 3 | violation | - |
| S04-04 | grade 3; holds himself out as grade 3 | no violation | - |
| S04-05 | grade 3; holds himself out as grade 2 | violation literally (no grade-2 licence) | alt: no violation (grade 3 covers every grade-2 system) |
| S04-06 | grade 2; holds himself out as grade 1 | as S04-05 | as S04-05 |
| S04-07 | licence expired; holds himself out as licensee | violation | - |
| S04-08 | temporary grade 3 (s.9); holds himself out as grade 3 | no violation | - |

## s. 5 application

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S05-01 | Registrar demands a document needed to decide the application | within power | - |
| S05-02 | Registrar demands a document not needed for the decision | outside s.5(b) | - |
| S05-03 | duty of the Registrar to publish on the Ministry website the ways to apply and the documents list | duty exists (MUST) | - |
| S05-04 | application to receive OR renew goes to the Registrar | both are "בקשה לרישיון" | - |

## s. 6 conditions for a licence

Base: adult, Israeli citizen, no conviction or indictment, meets Sch.2 route A1(1).

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S06-01 | base | Registrar must grant (mandatory, "ייתן") | - |
| S06-02 | not adult (17) | not entitled | - |
| S06-03 | turns 18 on the day of the decision | adult (input from another statute) | - |
| S06-04 | resident, not citizen | entitled | - |
| S06-05 | citizen, not resident | entitled | - |
| S06-06 | neither citizen nor resident | not entitled | - |
| S06-07 | convicted; Registrar's opinion: offence makes him unfit | not entitled | - |
| S06-08 | convicted; Registrar's opinion: not unfit | entitled | - |
| S06-09 | indictment pending; Registrar's opinion: unfit | not entitled | - |
| S06-10 | indictment pending; opinion: not unfit | entitled | - |
| S06-11 | no Second Schedule route met | not entitled | - |
| S06-12 | s.6(b) amend Second Schedule with committee approval / without | may / may not | - |

## s. 7 exemptions from training chapters

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S07-01 | holder of a VALID electricity licence of a kind in paras (1)-(7) of reg 7 Electricity (Licences) Regs | Director of the Division may exempt from the electricity chapter | - |
| S07-02 | electricity licence expired | no power | - |
| S07-03 | electricity licence of a kind outside paras (1)-(7) | no power | - |
| S07-04 | valid working-at-height approval (regs 5 and 6 Work at Height Regs) | may exempt from the height chapter | - |
| S07-05 | height approval not valid | no power | - |
| S07-06 | electricity licence holder asks for height exemption | no power under (b) | - |
| S07-07 | duty of the Director to publish instructions for applying | MUST | - |

## s. 8 validity and renewal

Main reading (R5): "the fifth year from the year in which the licence was granted" = grant year + 5. Alt (R4): grant year + 4 (grant year counted as the first). R5 is preferred because under R4 the five-year limb could never be the earlier one, so "לפי המוקדם" would be idle; the bill's rejected reservation 19 ("six years" with "the sixth") pairs the numbers the same way.
Validity is V: no IL s.10(c).

| id | grant | last valid day (R5) | alt (R4) |
| --- | --- | --- | --- |
| S08-01 | 2025-01-15 | 2030-01-15 (five-year limb earlier) | 2029-03-31 |
| S08-02 | 2025-09-01 | 2030-03-31 | 2029-03-31 |
| S08-03 | 2025-03-31 | 2030-03-31 (both limbs equal) | 2029-03-31 |
| S08-04 | 2025-04-01 | 2030-03-31 | 2029-03-31 |
| S08-05 | 2024-02-29 | 2029-02-28 (Feb 2029 lacks the 29th) | 2028-03-31 |
| S08-06 | 2025-07-16 | 2030-03-31: valid on 2030-03-31, not on 2030-04-01 | 2029-03-31 |
| S08-07 | 2025-01-01 | 2030-01-01 | 2029-03-31 |
| S08-08 | 2026-02-01 | 2031-02-01 (Sat); with Saturdays rest NOT valid on 2031-02-02 (no (c) for V) | alt (c) applied: valid 2031-02-02 |
| S08-09 | 2024-06-01 | 2029-03-31 (Sat); not valid 2029-04-01 | alt (c): 2029-04-01 |
| S08-10 | valid on the day of grant | TRUE | F6 of the interpretation notes would start a period the day after; a licence is in force when granted |

| id | renewal scenario | expected | amb |
| --- | --- | --- | --- |
| S08-11 | adult, citizen, no conviction, NO training route proof | s.8 renewal conditions met (s.6(a)(4) excluded) | - |
| S08-12 | no longer citizen or resident | not met | - |
| S08-13 | convicted, Registrar's opinion unfit | not met | - |
| S08-14 | whether renewal is mandatory when met | "ניתן לחדשו" | ambiguous: may vs must (s.6 is "shall grant") |

## s. 9 temporary licence for a foreign expert

Base: applicant from a foreign state; invited to work on a system of 100 kW; authorised abroad; performed similar installation in the 6 years preceding the application (last such work 2 years ago); Registrar recognised reputation.

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S09-01 | base | Registrar may grant a temporary GRADE 3 licence | - |
| S09-02 | system exactly 70 kW | may not ("מעל 70") | - |
| S09-03 | system 70.01 kW | may | - |
| S09-04 | last similar work 7 years before the application, none in the 6 preceding years | may not | backward period, IL s.10 silent; whole-year cases only |
| S09-05 | last similar work 5 years 11 months before | may | as above |
| S09-06 | not authorised abroad | may not | - |
| S09-07 | not recognised by the Registrar | may not | - |
| S09-08 | not adult / not Israeli resident (s.6 displaced) | still may | - |
| S09-09 | period 12 months / 1 year | within power | - |
| S09-10 | period 13 months | exceeds | - |
| S09-11 | granted 2028-02-29: latest end | 2029-02-28 | - |
| S09-12 | first and second renewals, each ≤ 1 year | may | - |
| S09-13 | third renewal | may not | - |
| S09-14 | renewal for 18 months | may not | - |
| S09-15 | temporary licence is not subject to s.8's five-year rule | - | - |

## s. 10 refusal to renew, cancellation, restriction, suspension

Base: ground (1) holds; Council consulted; written hearing given.

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S10-01 | base: cancel / refuse renewal / condition renewal on s.17 training / restrict / suspend | may (each) | - |
| S10-02 | base without Council consultation | may not | - |
| S10-03 | base without written hearing | may not | - |
| S10-04 | no ground (1)-(6) | may not | - |
| S10-05..10 | each of grounds (2) condition of s.6 or s.9 ceased, (3) breach of licence condition, (4) breach of duty under the Law or another enactment re his activity, (5) false/misleading info to Registrar/Ministry employee/inspector, (6) unprofessionalism/negligence risking life or property | may (each) | - |
| S10-11 | suspension 36 months | within | - |
| S10-12 | suspension 37 months / 3 years and 1 day | exceeds | whether the 3-year cap also binds a restriction ("להגבילו או להתלותו לתקופה"): ambiguous |
| S10-13 | (b) indictment for a 6(a)(3)-type offence; seriousness/public interest requires; Council consulted; hearing | may suspend until final judgment | - |
| S10-14 | (b) without "seriousness/public interest requires" | may not | - |
| S10-15 | (b) no indictment filed | may not | - |
| S10-16 | (b) suspension 5 years pending judgment | not capped by 3 years | - |
| S10-17 | (c) defect curable; Council consulted | may order no works pending cure (no hearing needed) | - |
| S10-18 | (c) Council not consulted | may not | - |
| S10-19 | (c) period lapsed, defect not cured, hearing given | may take (a) measures | whether Council must be consulted again: (a)'s measures carry it, (c) does not say |
| S10-20 | (c) defect cured | may not take (a) measures under (c) | - |
| S10-21 | (d) licence cancelled under (a): Registrar MUST set a waiting period, after consulting the Council; MAY add conditions | duty + power | - |

## s. 11 register

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S11-01 | register must hold: holder details, licence type, validity period; cancellation or suspension | required | - |
| S11-02 | restriction or refusal to renew | not required by (a) | - |
| S11-03 | public query must state identifying details of the person | required | - |

## ss. 12-16 duties of the licensee

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S12-01 | licensee transfers licence / lets another use it | violation / violation | - |
| S12-02 | neither | no violation | - |
| S13-01 | licensee does First Schedule work not per IS 994 parts 4 and 5 | violation | - |
| S13-02 | per the standard | no violation | - |
| S14-01 | work orderer demands; licensee does not show licence | violation | - |
| S14-02 | no demand | no duty | - |
| S14-03 | demand by someone who did not order the work | no s.14 duty | - |
| S15-01 | Registrar demands a report; licensee delivers / does not | compliant / violation | - |
| S16-01 | change 2026-03-10; notified 2026-04-09 | timely (30 days, IL s.10(a)) | - |
| S16-02 | change 2026-03-10; notified 2026-04-10 | late | - |
| S16-03 | change 2026-01-01; no rest days; notified 2026-01-31 | timely | - |
| S16-04 | change 2026-01-01; no rest days; notified 2026-02-01 | late | - |
| S16-05 | change 2026-01-01; Saturdays rest (01-31 is Sat); notified 2026-02-01 | timely (D: IL s.10(c)) | alt (no (c)): late |
| S16-06 | same; notified 2026-02-02 | late | - |
| S16-07 | notified on the day of change | timely | - |

## s. 17 in-service training

Licence expiring 2030-03-31.

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S17-01 | 8 hours of qualifying training, 2029-10-01 | complies | - |
| S17-02 | 7.5 hours | does not | - |
| S17-03 | two trainings of 4 hours each in the last year | complies (plural "השתלמויות", "בהיקף של") | alt: one training of 8 h |
| S17-04 | 8 hours on 2028-12-01 (outside the last year) | does not | backward year, IL s.10 silent; edge days not tested |
| S17-05 | 8 hours neither run by the Registrar nor recognised by the Division | does not | - |
| S17-06 | 8 hours outside his field | does not | - |
| S17-07 | (c) extension to 2030-06-30 (3 months after 2030-03-31; June lacks the 31st) | within | - |
| S17-08 | (c) extension to 2030-07-01 | exceeds | - |
| S17-09 | (c) without Council consultation, or no special case | may not | - |
| S17-10 | (c) licensee who did fulfil the duty | not within (c) | - |
| S17-11 | (b) circumstances justify, needed for training and the Law's objects | may require a specific training | - |
| S17-12 | (b) notice must be given a reasonable time before | duty | - |
| S17-13 | (d) non-participation = breach of a licence condition → s.10(a)(3) ground | TRUE | - |
| S17-14 | (e), (f) Registrar must ensure availability; publish a reasonable time before | MUST | - |

## s. 18 operator

| id | scenario | expected | amb |
| --- | --- | --- | --- |
| S18-01 | regular employer employs an unlicensed person on R/AC work | violation | - |
| S18-02 | operator employs grade 1 on a 50 kW system | violation | - |
| S18-03 | operator employs grade 2 on 50 kW | no violation | - |
| S18-04 | operator employs grade 3 on 50 kW | no violation | - |
| S18-05 | one-off employer (not "דרך קבע") employs unlicensed | not an operator; no s.18 violation | - |
| S18-06 | owner/manager of a business offering R/AC works to the public | operator | - |
| S18-07 | unlicensed operator employs a correctly licensed worker | no violation | - |
| S18-08 | (b) operator must ensure work per IS 994 via guidelines, briefings, procedures, sample checks | MUST | - |

## First Schedule: one scenario per row (s.3 "appropriate licence" for the work)

| id | row | scenario | expected |
| --- | --- | --- | --- |
| SCH1-A1 | Part A row 1 | grade 1, A1(1) refrigerant quantity check, 10 kW | permitted |
| SCH1-A1b | Part A row 1 | grade 1, A1(12) electrical work on integral electrical system, 10 kW | permitted |
| SCH1-A2 | Part A row 2 | grade 2, A1(7) commissioning, 50 kW | permitted |
| SCH1-A3 | Part A row 3 | grade 3, A1(10) flushing, 200 kW | permitted |
| SCH1-B1 | Part B row 1 | grade 1, B1(4) leak repair, 12 kW | permitted |
| SCH1-B1b | Part B row 1 | grade 1, B1(14) electrical work, 12 kW | permitted |
| SCH1-B2 | Part B row 2 | grade 2, B1(9) cold-room refrigeration, 60 kW | permitted |
| SCH1-B2x | Part B row 2 | grade 2, B3(3) oil, 60 kW | prohibited (literal) |
| SCH1-B3 | Part B row 3 | grade 3, B3(3) oil, 5 kW | permitted |
| SCH1-B3b | Part B row 3 | grade 3, B1(13) chiller protections, 500 kW | permitted |

## Second Schedule: one scenario per row (and the gaps)

Every row needs the applicant ALSO to meet s.6(a)(1)-(3). "הכשרה של עד N שעות המקנה תעודת …" is read as: the requirement is completing the Division training that grants the named certificate; N caps the length of that training (it is not a minimum the applicant must exceed). "כל אחד מאלה" = any one of.
Required training hours per row (gazette p. 201-205): A1 350, A2 220, A3 50, B1 480, B2 none, B3 100, B4 330, B5 50, B6 50, C1 720, C2 none, C3 290, C4 240, C5 455, C6 200, C7 50, C8 230.

| id | grade | prior | completed | expected | amb |
| --- | --- | --- | --- | --- | --- |
| SCH2-A1a | 1 | none | Division training (≤350 h) → grade-1 completion cert | meets (4) | - |
| SCH2-A1b | 1 | MoE climate control 3 units | nothing more | meets | - |
| SCH2-A1c | 1 | none | a 300-hour Division grade-1 course with the certificate | meets ("up to") | alt: hours are a minimum → not |
| SCH2-A2a | 1 | 12 months in the last 3 years, applying 2026-01-01 | ≤220 h → grade-1 cert | meets | - |
| SCH2-A2b | 1 | 11 months in last 3, 3 years in last 7 | 220 h | meets via (2) | - |
| SCH2-A2c | 1 | 11 months in last 3, 2.5 years in last 7 | 220 h | not via row 2 | - |
| SCH2-A2d | 1 | 12 months in last 3; applying 2028-07-16 | 220 h | meets (sunset last day) | date tested |
| SCH2-A2e | 1 | same, applying 2028-07-17 | 220 h | row 2 not available | - |
| SCH2-A3a | 1 | Division R&AC completion cert (ungraded) | ≤50 h → Division cert | meets | - |
| SCH2-A3b | 1 | Division R&AC cert (ungraded) | nothing | not met | s.6(a)(4)(a) alone ("holds a completion certificate") would say met; the Schedule governs |
| SCH2-A-gap | 1 | MoE climate control 5 units | nothing | not listed in Part A | alt: met (higher level); ambiguous |
| SCH2-B1a | 2 | none | ≤480 h → grade-2 cert | meets | - |
| SCH2-B1b | 2 | MoE 5 units | nothing | meets (row 1(2)) | CONTRADICTION with B5(3): 50 h |
| SCH2-B2a | 2 | certified AC technician + programme incl. completion course | nothing | meets | - |
| SCH2-B2b | 2 | certified AC technician without the completion course | nothing | not met (row 6: 50 h) | - |
| SCH2-B3a | 2 | grade 1 licence | ≤100 h → grade-2 cert | meets | - |
| SCH2-B3b | 2 | Division grade-1 cert | 100 h | meets | overlap with B5(1)? only if a graded cert is "a Division R&AC cert" |
| SCH2-B3c | 2 | MoE 3 units | 100 h | meets | - |
| SCH2-B3d | 2 | grade 1 licence | nothing | not met | - |
| SCH2-B4a | 2 | experience 1 of 3 | ≤330 h | meets (before sunset) | - |
| SCH2-B4b | 2 | experience, after 2028-07-16 | 330 h | row unavailable | - |
| SCH2-B5a | 2 | Division R&AC cert (ungraded) | ≤50 h | meets | - |
| SCH2-B5b | 2 | Division youth vocational school R&AC cert | 50 h | meets | - |
| SCH2-B5c | 2 | MoE 5 units | 50 h | meets | (and see B1b) |
| SCH2-B6a | 2 | certified AC technician (no completion course) | ≤50 h | meets | - |
| SCH2-B-gap | 2 | AC practical engineer (הנדסאי) | nothing | no Part B row | alt: s.6(a)(4)(b) "registered" read alone; ambiguous |
| SCH2-C1 | 3 | none | ≤720 h → grade-3 cert | meets | - |
| SCH2-C2a | 3 | AC practical engineer + programme incl. completion course | nothing | meets | - |
| SCH2-C2b | 3 | AC practical engineer, no completion course | nothing | not met | - |
| SCH2-C3a | 3 | grade 1 licence / grade-1 cert / MoE 3 units | ≤290 h → grade-3 cert | meets | - |
| SCH2-C4a | 3 | grade 2 licence / grade-2 cert / MoE 5 units | ≤240 h → grade-3 cert | meets | wiki puts 240 h in column A (defect), gazette p.204 column B |
| SCH2-C4b | 3 | grade 2 licence | nothing | not met | - |
| SCH2-C5a | 3 | experience 1 of 3 | ≤455 h | meets (before sunset) | - |
| SCH2-C5b | 3 | experience, after sunset | - | unavailable | - |
| SCH2-C6 | 3 | Division R&AC cert (ungraded) | ≤200 h | meets | - |
| SCH2-C7a | 3 | AC practical engineer | ≤50 h | meets | - |
| SCH2-C8a | 3 | engineer, mechanical branch | ≤230 h → grade-3 cert | meets | - |
| SCH2-C8b | 3 | engineer, electrical branch | 230 h | not via row 8 | - |

## Counts of scenarios decided before opening the encoding

| part | scenarios |
| --- | --- |
| gazette dates + commencement (s.63 as used) | 3 + 8 |
| s.2 | 12 |
| s.3 | 26 |
| s.4 | 8 |
| s.5 | 4 |
| s.6 | 12 |
| s.7 | 7 |
| s.8 | 14 |
| s.9 | 15 |
| s.10 | 26 (S10-05..10 counted as 6) |
| s.11 | 3 |
| s.12 | 2 |
| s.13 | 2 |
| s.14 | 3 |
| s.15 | 1 |
| s.16 | 7 |
| s.17 | 14 |
| s.18 | 8 |
| First Schedule (Part A rows 1-3: 4; Part B rows 1-3: 6) | 10 |
| Second Schedule (Part A rows 1-3: 10 incl. gap; Part B rows 1-6: 15 incl. gap; Part C rows 1-8: 13) | 38 |

## Source notes found while reading (for report item 6)

- Wiki line 669 (Part C row 4) puts "(הכשרה של עד 240 שעות …" inside column A with a stray "(", leaving column B empty; the gazette p. 204 has it in column B. Gazette governs.
- Wiki Part A row 3 column B ends "מהאגף להכשרה"; the gazette p. 201 has "מהאגף להכשרה מקצועית".
- A1(12)/B1(14) spell "אינטרגרלית" in the gazette too (not a wiki error), and use word order that does not match the defined term "מערכת החשמל האינטגרלית של מערכת הקירור או מיזוג האוויר".
- Contradictions: Part B row 1(2) vs row 5(3) (MoE 5 units: nothing vs 50 h); Part A1(5) vs B3(3) (oil: grade 1 vs grade 3); B1(3) vs B3(2) (component repair: grade 1 vs grade 3); s.6(a)(4)(a)/(b) read alone vs the Schedule rows A3, B6, C7 (holding a completion certificate or being registered is not enough under the Schedule).

## Correction appended after step 3 (the rows above are unchanged)

The count table above miscounts two lines; the scenario rows themselves are as written before the encoding was opened.
s.10 has 21 scenario ids, not 26 (S10-05..10 is six ids; S10-01 asks five measures under one id).
The Second Schedule split is Part A 11 (incl. the gap row), Part B 15 (incl. the gap row), Part C 12: 38 in all, as stated.
Corrected total: 218 scenario ids (3 gazette facts, 8 commencement, 207 for ss.2-18 and the two Schedules).
