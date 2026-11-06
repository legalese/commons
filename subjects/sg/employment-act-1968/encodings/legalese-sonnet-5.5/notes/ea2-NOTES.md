# NOTES: part ea2 of the Employment Act 1968 (Singapore) encoding

Part ea2 covers lines 2597 to 4611 of `EmA1968.txt` (Parts 6A, 7, 8, 9, 10, 11 (repealed), 12, 13 and 14; sections 66A to 114) and the whole of the Employment (Retrenchment Reporting) Notification 2019 (S 200/2019), made under section 96A.
Target: the `main` build of `l4` (written against 1.6.109, read the same on 1.6.108).

## What this is, and what it is not

- The text is a plain-text rendering made by a converter script from Singapore Statutes Online (`EmA1968.txt` and `EmA1968-S200-2019.txt`).
  It is not the official text, and nothing here is verified against the official text.
- Layer 1 is the law objectively: tested modules named `ea2-*.l4`, each rule with an `@ref` and `src:` lines that `srcrefs.py` checks against the raw text.
  They import the keel's `ea-core.l4` and `ea-definitions.l4` and the Interpretation Act module (see Dependencies).
- Layer 2 is one thin seat layer: `ea2-seat.l4` (219 questions) and `ea2-cases-seat.l4`.
  The seat is an employee in Singapore, or a person about to start work there, asking whether the Act covers them, what they are owed, when, and what they can do if it is not given.
  It calls layer-1 rules and restates none of them.
  There is no seat for an official: where a provision addresses only an official (Part 13 above all), the question is what may be done to the person, what they must be given, and by when.
- **Where PLAN.md and the brief differ, the brief governs.**
  PLAN section 1 says the lead must confirm whether the Notification (S 200/2019) belongs to ea2; the brief's Scope puts it in ea2's range, so ea2 encodes it.
- **PLAN has sections 1 to 6 only.**
  The brief cites PLAN sections 5, 6, 7, 8, 11 and 12 for seams and other matters; sections 7, 8, 11 and 12 do not exist.
  The seams are PLAN section 4 and this part followed that (Seams, below).

## Coverage (ea2)

```
Audit of lines 2597-4611 of EmA1968.txt: 1415 non-blank lines, 1415 covered, 0 not covered []
  covered by: amendment note 99, furniture 48, heading 66, row 1202
Audit of EmA1968-S200-2019.txt (131 lines): 130 non-blank lines, 130 covered, 0 not covered []
Rows: 327 in EmA1968 (units counted by the script: 327), 34 in S 200/2019
  encoded                            EmA1968 265   S 200/2019  30   total 295
  inert                              EmA1968  25   S 200/2019   0   total  25
  fork                               EmA1968  30   S 200/2019   3   total  33
  repealed or blank in this text     EmA1968   7   S 200/2019   1   total   8
  inert by reason: reason 1: 8, reason 2: 17
```

How the lines that are not rows are handled (a script counts them and asserts that none is left over):

- **Section headings** (66 lines, including a few two-line headings) are `inert`, reason 1 (headings), and are not given a row of their own.
- **Amendment notes** such as `[S 781/2021 wef 01/11/2021]` (99 lines) and **page furniture** of the rendering (48 lines: the version line and the running page headers) are `inert`, reason 1, and likewise carry no row.
- **Closing words** after a list of paragraphs (14 places, for example the "is not entitled to any pay ..." that closes s 76(2A)) are counted in the row of the enclosing subsection.
- **Part headings** (Parts 6A, 7, 8, 9, 10, 12, 13 and 14) have one row each, `inert`, reason 1.
  PART 11 has a row, `repealed or blank in this text`: it has no title and its four sections each show "[Repealed by Act 32 of 2008]".
- A paragraph's row names the rule of the subsection it sits in ("within ...") unless the paragraph has a rule of its own.
  Where one rule encodes several paragraphs together (the paragraphs of s 113A(6) "officer", say) they share it.
- For the Notification, lines 1 to 23 (the title block, arrangement of paragraphs and enacting words), the headings, the amendment notes, the page furniture and the signature and date of making (lines 125 to 131) are `inert`, reason 1; the Schedule's items are one row each, encoded as the constructors of `S 200/2019 Schedule item`.

The table follows.
An `encoded` or `fork` row names the L4 rule that encodes it (at most three, with a count of the rest).
A `fork` row also names the fork-register entries (F1 to F24).
F18 and F19 are rules that apply to many rows and are named in only a few; every other entry names the rows it governs.
Every named rule was checked by the script to exist in the deposit.

| text lines | unit | disposition | reason / fork | encoded as |
| --- | --- | --- | --- | --- |
| | **Employment Act 1968** | | | |
| 2597-2599 | Part 6A Part-time employees | inert | reason 1: Part heading | - |
| 2603-2605 | s 66A(1) | fork | F8 | `s 66A(1) the person is a part-time employee`; `s 66A(1) gathered with (2): the employee is a part-time employee for the purposes of this Part` |
| 2607-2609 | s 66A(2) | fork | F8 | `s 66A(2) the employee is regarded as a part-time employee for the purposes of this Part` |
| 2614-2616 | s 66B | inert | reason 2: machinery: a regulation-making power of the Minister to exclude or modify the Act for part-time employees; nothing in the Act changes until regulations are made, so there is no function | - |
| 2618-2620 | Part 7 Domestic workers | inert | reason 1: Part heading | - |
| 2624-2629 | s 67 | fork | F21 | `s 67 the provision of the Act applies to the domestic worker` |
| 2631-2632 | Part 8 Employment of children and young persons | inert | reason 1: Part heading | - |
| 2634 | s 67A | encoded |  | `s 67A "child" the person is a child`; `s 67A "young person" the person is a young person` |
| 2636-2637 | s 67A "child" | fork | F13 | `s 67A "child" the person is a child` |
| 2642-2644 | s 67A "young person" | fork | F13 | `s 67A "young person" the person is a young person` |
| 2648-2650 | s 68(1) | encoded |  | `s 68(1) the prohibition on employing a child`; `s 68(1) the person may employ the child` |
| 2652-2653 | s 68(2) | encoded |  | `s 68(2) a child may be employed in the undertaking` |
| 2655-2657 | s 68(3) | encoded |  | `s 68(3) a child may be employed in the undertaking` |
| 2659-2661 | s 68(4) | encoded |  | `s 68(4) the work is suited to the capacity of the child` |
| 2665-2668 | s 69 | encoded |  | `s 69 the young person may be employed in the undertaking` |
| 2672-2674 | s 70 | inert | reason 2: regulation-making power of the Minister to prescribe conditions of employment of children and young persons | - |
| 2678-2689 | s 71(1) | inert | reason 2: the Minister's power to prescribe minimum salaries after inquiry; what the order says arrives as an input to s 71(2) | - |
| 2691-2696 | s 71(2) | encoded |  | `s 71(2) the person is guilty of an offence`; `s 71(2) the penalty on conviction` |
| 2700 | s 72(1) | encoded |  | `s 72(1) sections 68 and 69 apply to the employment` |
| 2702-2709 | s 72(1)(a) | encoded |  | within `s 72(1) sections 68 and 69 apply to the employment` |
| 2711-2713 | s 72(1)(b) | encoded |  | within `s 72(1) sections 68 and 69 apply to the employment` |
| 2715-2718 | s 72(2) | encoded |  | `s 72(2) the body is the Institute of Technical Education, Singapore` |
| 2722-2726 | s 73 | fork | F14 (the second limb is encoded; the regulation-making first limb is inert, reason 2) | `s 73 the child or young person may be employed as a workman` |
| 2730-2744 | s 74 | fork | F22 | `s 74 the person is guilty of an offence`; `s 74 the penalty on conviction` |
| 2749-2754 | s 75 | encoded |  | `s 75 the child or young person may be brought before a Youth Court`; `s 75 the Youth Court may exercise the powers conferred by section 54 of the Children and Young Persons Act 1993` |
| 2758-2761 | Part 9 Maternity protection and benefits and childcare leave for parent | inert | reason 1: Part heading | - |
| 2765-2766 | s 76(1) | encoded |  | `s 76(1) the person is a female employee`; `s 76(1) the female employee is entitled to absent herself from work`; `s 76(1)(a)(i) the 4 weeks immediately before the confinement` (+11 more) |
| 2768-2774 | s 76(1)(a) | fork | F1 | `s 76(1)(a)(i) the 4 weeks immediately before the confinement`; `s 76(1)(a)(ii) the 8 weeks immediately after the confinement` |
| 2776-2785 | s 76(1)(b) | encoded |  | `s 76(1)(b) the agreed 12 weeks`; `s 76(1)(b) the agreed 12 weeks begin inside the window` |
| 2787-2803 | s 76(1)(c) | encoded |  | `s 76(1)(c)(i) the agreed 8 weeks`; `s 76(1)(c)(i) the agreed 8 weeks begin inside the window`; `s 76(1)(c)(ii) the least total of the further periods, in days` (+5 more) |
| 2807-2810 | s 76(1A) | fork | F8, F1 | `s 76(1A) the benefit period`; `s 76(1A) the female employee is entitled to payment at her gross rate of pay for the benefit period`; `s 76(1A) the sum payable for the days of the benefit period` (+2 more) |
| 2812-2814 | s 76(1A)(a) | encoded |  | within `s 76(1A) the benefit period`; `s 76(1A) the female employee is entitled to payment at her gross rate of pay for the benefit period`; `s 76(1A) the sum payable for the days of the benefit period` (+2 more) |
| 2816-2817 | s 76(1A)(b) | encoded |  | within `s 76(1A) the benefit period`; `s 76(1A) the female employee is entitled to payment at her gross rate of pay for the benefit period`; `s 76(1A) the sum payable for the days of the benefit period` (+2 more) |
| 2819-2820 | s 76(1A)(c) | encoded |  | within `s 76(1A) the benefit period`; `s 76(1A) the female employee is entitled to payment at her gross rate of pay for the benefit period`; `s 76(1A) the sum payable for the days of the benefit period` (+2 more) |
| 2824-2833 | s 76(2) | encoded |  | `s 76(2) the female employee is entitled to pay during the benefit period` |
| 2837 | s 76(2A) | encoded |  | `s 76(2A) the female employee is entitled to pay during the benefit period`; `s 76(2A) helper: not entitled if served less than 3 months` |
| 2839 | s 76(2A)(a) | encoded |  | within `s 76(2A) the female employee is entitled to pay during the benefit period`; `s 76(2A) helper: not entitled if served less than 3 months` |
| 2841-2847 | s 76(2A)(b) | encoded |  | within `s 76(2A) the female employee is entitled to pay during the benefit period`; `s 76(2A) helper: not entitled if served less than 3 months` |
| 2851 | s 76(2B) | encoded |  | `s 76(2B) the female employee is entitled to pay during the benefit period`; `s 76(2B) helper: not entitled if not served at least 3 months` |
| 2853 | s 76(2B)(a) | encoded |  | within `s 76(2B) the female employee is entitled to pay during the benefit period`; `s 76(2B) helper: not entitled if not served at least 3 months` |
| 2855-2861 | s 76(2B)(b) | encoded |  | within `s 76(2B) the female employee is entitled to pay during the benefit period`; `s 76(2B) helper: not entitled if not served at least 3 months` |
| 2865-2870 | s 76(3) | fork | F2 | `s 76(3) the amount equivalent to a day's pay for the days worked`; `s 76(3) the days she may absent herself instead at the end of the benefit period` |
| 2872-2875 | s 76(4) | encoded |  | `s 76(4) the female employee is entitled to payment under subsection (1A) for the confinement` |
| 2877 | s 76(4)(a) | encoded |  | within `s 76(4) the female employee is entitled to payment under subsection (1A) for the confinement` |
| 2879-2880 | s 76(4)(b) | encoded |  | within `s 76(4) the female employee is entitled to payment under subsection (1A) for the confinement` |
| 2885-2887 | s 76(5) | encoded |  | `s 76(5) subsection (4) applies to the female employee` |
| 2889-2893 | s 76(5A) | encoded |  | `s 76(5A)(a) the female employee keeps the entitlement to absent herself from work`; `s 76(5A)(a) the female employee forfeits the entitlement to absent herself from work`; `s 76(5A)(b) the female employee keeps the entitlement to payment at her gross rate of pay for the forfeited period` (+1 more) |
| 2895-2896 | s 76(5A)(a) | encoded |  | `s 76(5A)(a) the female employee keeps the entitlement to absent herself from work`; `s 76(5A)(a) the female employee forfeits the entitlement to absent herself from work` |
| 2898-2901 | s 76(5A)(b) | encoded |  | `s 76(5A)(b) the female employee keeps the entitlement to payment at her gross rate of pay for the forfeited period`; `s 76(5A)(b) the female employee forfeits the entitlement to payment at her gross rate of pay for the forfeited period` |
| 2905-2914 | s 76(6) | encoded |  | `s 76(6) the female employee keeps the entitlement under subsection (1)(c)(ii)`; `s 76(6) the female employee forfeits the entitlement under subsection (1)(c)(ii)` |
| 2916-2919 | s 77(1) | encoded |  | `s 77(1) the payment referred to in section 76 must be paid for the day` |
| 2923-2925 | s 77(2) | encoded |  | `s 77(2) section 77 requires the employer to pay an extra day's salary for the holiday` |
| 2929-2938 | s 78(1) | encoded |  | `s 78(1) the duty to pay the payment in 2 instalments`; `s 78(1) the days allowed for the second instalment`; `s 78(1) the days allowed for the first instalment` (+6 more) |
| 2940-2942 | s 78(2) | encoded |  | `s 78(2) the date by which the payment must be paid` |
| 2947-2957 | s 79(1) | fork | F3, F4 | `s 79(1) the person to whom the employer must pay`; `s 79(1) the employer must pay a sum of money after her death`; `s 79(1) the days for which the sum is payable` (+2 more) |
| 2959-2966 | s 79(2) | encoded |  | `s 79(2) the employer must pay a sum of money after her death`; `s 79(2) the days of the benefit period up to the day before her death` |
| 2970-2973 | s 80(1) | fork | F5 | `s 80(1) the duty to give notice`; `s 80(1) the days from today until the last day for giving the notice`; `s 80(1) the female employee must give her employer notice of the date she intends to begin absenting herself` (+1 more) |
| 2978-2980 | s 80(2) | encoded |  | `s 80(2) the female employee who has been confined must inform her employer of the date of the confinement` |
| 2982-2986 | s 80(3) | fork | F8 | `s 80(3) the female employee is entitled to only half the amount of the payment`; `s 80(3) the amount of the payment` |
| 2988-2992 | s 80(4) | encoded |  | `s 80(4) the payment is deemed to be payment to the female employee` |
| 2996-3000 | s 81 | encoded |  | `s 81 the prohibition on giving her notice of dismissal`; `s 81 it is lawful for her employer to give her the notice of dismissal`; `s 81 it is not lawful for her employer to give her the notice of dismissal` |
| 3004-3006 | s 82 | fork | F1 | `s 82 the employer is guilty of an offence` |
| 3010-3013 | s 83 | encoded |  | `s 83 the female employee keeps her claim to payment under this Part`; `s 83 the female employee forfeits her claim to payment under this Part`; `s 83 the female employee is liable to dismissal` (+1 more) |
| 3021-3023 | s 84(1) | encoded |  | `s 84(1) the notice of dismissal has the effect of depriving her of a payment under this Part`; `s 84(1) helper: the day is within the months preceding the date`; `s 84(1) helper: the notice was given within the months preceding the estimated delivery date or the confinement` |
| 3025-3032 | s 84(1)(a) | fork | F6, F7 | within `s 84(1) the notice of dismissal has the effect of depriving her of a payment under this Part`; `s 84(1) helper: the day is within the months preceding the date`; `s 84(1) helper: the notice was given within the months preceding the estimated delivery date or the confinement` |
| 3034-3038 | s 84(1)(b) | encoded |  | within `s 84(1) the notice of dismissal has the effect of depriving her of a payment under this Part`; `s 84(1) helper: the day is within the months preceding the date`; `s 84(1) helper: the notice was given within the months preceding the estimated delivery date or the confinement` |
| 3040-3053 | s 84(1)(c) | fork | F6, F7 | within `s 84(1) the notice of dismissal has the effect of depriving her of a payment under this Part`; `s 84(1) helper: the day is within the months preceding the date`; `s 84(1) helper: the notice was given within the months preceding the estimated delivery date or the confinement` |
| 3057-3060 | s 84(1A) | encoded |  | `s 84(1A) the estimated delivery date that is relevant`; `s 84(1A) helper: the latest day of certification before the notice`; `s 84(1A) helper: the estimated delivery dates certified on the day` (+2 more) |
| 3062-3063 | s 84(1A)(a) | encoded |  | `s 84(1A) the estimated delivery date that is relevant` |
| 3068-3069 | s 84(1A)(b) | encoded |  | `s 84(1A) the estimated delivery date that is relevant` |
| 3071-3076 | s 84(2) | encoded |  | `s 84(2) the female employee may lodge a claim for the relief` |
| 3078 | s 84(2)(a) | encoded |  | within `s 84(2) the female employee may lodge a claim for the relief` |
| 3080 | s 84(2)(b) | encoded |  | within `s 84(2) the female employee may lodge a claim for the relief` |
| 3084-3086 | s 84(3) | encoded |  | `s 84(3)(a) the Tribunal may direct the employer to reinstate her and to pay her the wages she would have earned`; `s 84(3)(b) the Tribunal may direct the employer to pay her compensation in wages` |
| 3088-3096 | s 84(3)(a) | encoded |  | `s 84(3)(a) the Tribunal may direct the employer to reinstate her and to pay her the wages she would have earned` |
| 3098-3101 | s 84(3)(b) | encoded |  | `s 84(3)(b) the Tribunal may direct the employer to pay her compensation in wages` |
| 3109-3112 | s 84A(1) | encoded |  | `s 84A(1) the notice of dismissal has the effect of depriving her of a payment under this Part` |
| 3117-3124 | s 84A(1)(a) | fork | F6, F7 | within `s 84A(1) the notice of dismissal has the effect of depriving her of a payment under this Part` |
| 3126-3130 | s 84A(1)(b) | encoded |  | within `s 84A(1) the notice of dismissal has the effect of depriving her of a payment under this Part` |
| 3132-3145 | s 84A(1)(c) | fork | F6, F7 | within `s 84A(1) the notice of dismissal has the effect of depriving her of a payment under this Part` |
| 3149-3152 | s 84A(2) | encoded |  | `s 84A(2) the estimated delivery date that is relevant` |
| 3154-3155 | s 84A(2)(a) | encoded |  | `s 84A(2) the estimated delivery date that is relevant` |
| 3157-3158 | s 84A(2)(b) | encoded |  | `s 84A(2) the estimated delivery date that is relevant` |
| 3160-3167 | s 84A(3) | encoded |  | `s 84A(3) the payment is in addition to a retrenchment benefit or other payment` |
| 3169 | s 85 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 3173-3177 | s 86 | encoded |  | `s 86 the term of the contract of service is void` |
| 3181 | s 87(1) | encoded |  | `s 87(1) the employer is guilty of an offence`; `s 87(1) the penalty on conviction` |
| 3183-3185 | s 87(1)(a) | encoded |  | within `s 87(1) the employer is guilty of an offence`; `s 87(1) the penalty on conviction` |
| 3187-3189 | s 87(1)(b) | encoded |  | within `s 87(1) the employer is guilty of an offence`; `s 87(1) the penalty on conviction` |
| 3191-3195 | s 87(1)(c) | encoded |  | within `s 87(1) the employer is guilty of an offence`; `s 87(1) the penalty on conviction` |
| 3199-3201 | s 87(2) | encoded |  | `s 87(2) the penalty on conviction for an offence under section 82` |
| 3205-3209 | s 87(3) | encoded |  | `s 87(3) the penalty on conviction of a repeat offender` |
| 3216-3220 | s 87(4) | encoded |  | `s 87(4) the person is a repeat offender`; `s 87(4) helper: the earlier convictions that count` |
| 3222-3223 | s 87(4)(a) | encoded |  | `s 87(4) the person is a repeat offender` |
| 3225-3231 | s 87(4)(b) | encoded |  | `s 87(4) the person is a repeat offender` |
| 3237 | s 87A(1) | fork | F19 | `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period`; `s 87A(1) the entitlement to childcare leave for the relevant period arises`; `s 87A(1)(b) helper: the child is below 7 years of age at some time during the period` (+1 more) |
| 3239-3240 | s 87A(1)(a) | fork | F9a | within `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period`; `s 87A(1) the entitlement to childcare leave for the relevant period arises`; `s 87A(1)(b) helper: the child is below 7 years of age at some time during the period` (+1 more) |
| 3242-3246 | s 87A(1)(b) | encoded |  | `s 87A(1)(b) helper: the child is below 7 years of age at some time during the period`; `s 87A(1)(b) helper: some child is below 7 years of age at some time during the period` |
| 3248 | s 87A(2) | encoded |  | `s 87A(2)(a) the employee is entitled to the days now claimed in respect of the child`; `s 87A(2)(a) the days that remain within the 14-day limit for the child`; `s 87A(2)(b)(i) the first entitlement is taken in time` (+1 more) |
| 3250-3251 | s 87A(2)(a) | fork | F9 | `s 87A(2)(a) the employee is entitled to the days now claimed in respect of the child`; `s 87A(2)(a) the days that remain within the 14-day limit for the child` |
| 3253-3267 | s 87A(2)(b) | fork | F9b | `s 87A(2)(b)(i) the first entitlement is taken in time`; `s 87A(2)(b)(ii) the number of the relevant period in which the entitlement must be taken` |
| 3269-3271 | s 87A(3) | encoded |  | `s 87A(3) the total days off the employee is entitled to` |
| 3275-3278 | s 87A(4) | fork | F9c | `s 87A(4) the duty to grant and to take the childcare leave`; `s 87A(4) the days from today until the last day of the relevant period`; `s 87A(4) the days of the entitlement that are lost` (+2 more) |
| 3280 | s 87A(4)(a) | encoded |  | `s 87A(4)(a) the employee is still entitled to the days not taken by the last day` |
| 3282 | s 87A(4)(b) | encoded |  | `s 87A(4)(b) the employee is entitled to payment in lieu of the days not taken` |
| 3284-3286 | s 87A(5) | encoded |  | `s 87A(5) the amount the employer must pay for the childcare leave taken` |
| 3288-3289 | s 87A(5A) | encoded |  | `s 87A(5A) the employee is entitled to take paid childcare leave on the day` |
| 3293-3297 | s 87A(6) | encoded |  | `s 87A(6)(a) the employee is still entitled to the leave not yet taken`; `s 87A(6)(a) the employee ceases to be entitled to the leave not yet taken`; `s 87A(6)(b) the employee is entitled to payment in lieu of the leave not yet taken` (+1 more) |
| 3299-3300 | s 87A(6)(a) | encoded |  | `s 87A(6)(a) the employee is still entitled to the leave not yet taken`; `s 87A(6)(a) the employee ceases to be entitled to the leave not yet taken` |
| 3302 | s 87A(6)(b) | encoded |  | `s 87A(6)(b) the employee is entitled to payment in lieu of the leave not yet taken`; `s 87A(6)(b) the employee is not entitled to payment in lieu of the leave not yet taken` |
| 3304-3307 | s 87A(7) | encoded |  | `s 87A(7) the employer is guilty of an offence`; `s 87A(7) the penalty on conviction` |
| 3311-3319 | s 87A(7A) | encoded |  | `s 87A(7A) the employer is guilty of an offence`; `s 87A(7A) the penalty on conviction` |
| 3323-3327 | s 87A(7B) | encoded |  | `s 87A(7B) the penalty on conviction of a person convicted under subsection (7) or (7A)`; `s 87A(7B) the penalty for a repeat offender applies` |
| 3331-3335 | s 87A(7C) | encoded |  | `s 87A(7C) the person is a repeat offender`; `s 87A(7C) helper: the earlier convictions that count` |
| 3337 | s 87A(7C)(a) | encoded |  | `s 87A(7C) the person is a repeat offender` |
| 3339-3341 | s 87A(7C)(b) | encoded |  | `s 87A(7C) the person is a repeat offender` |
| 3343-3348 | s 87A(7C)(c) | encoded |  | `s 87A(7C) the person is a repeat offender` |
| 3352 | s 87A(8) | encoded |  | `s 87A(8) "child" the person is a child of the employee`; `s 87A(8) "relevant period" the period` |
| 3354 | s 87A(8) "child" | encoded |  | `s 87A(8) "child" the person is a child of the employee` |
| 3356 | s 87A(8) "child"(a) | encoded |  | `s 87A(8) "child" the person is a child of the employee` |
| 3358-3363 | s 87A(8) "child"(b) | encoded |  | `s 87A(8) "child" the person is a child of the employee` |
| 3368 | s 87A(8) "relevant period" | encoded |  | `s 87A(8) "relevant period" the period` |
| 3370-3371 | s 87A(8) "relevant period"(a) | encoded |  | `s 87A(8) "relevant period" the period` |
| 3373 | s 87A(8) "relevant period"(b) | encoded |  | `s 87A(8) "relevant period" the period` |
| 3377-3380 | Part 10 Holiday, annual leave and sick leave entitlements | inert | reason 1: Part heading | - |
| 3386-3388 | s 88(1) | encoded |  | `s 88(1) the employee is entitled to a paid holiday at the gross rate of pay on the public holiday`; `s 88(1)(a) the day may be substituted for the public holiday`; `s 88(1)(b) the day that is a paid holiday` (+2 more) |
| 3390-3392 | s 88(1)(a) | encoded |  | `s 88(1)(a) the day may be substituted for the public holiday` |
| 3394-3395 | s 88(1)(b) | encoded |  | `s 88(1)(b) the day that is a paid holiday`; `s 88(1)(b) the rule of paragraph (b) applies` |
| 3397-3401 | s 88(1)(c) | encoded |  | `s 88(1)(c) the employer may do this` |
| 3405-3408 | s 88(2) | encoded |  | `s 88(2) the employee is entitled to holiday pay for the public holiday` |
| 3412-3420 | s 88(3) | fork | F10 | `s 88(3) the employee is entitled to holiday pay for that holiday` |
| 3424-3430 | s 88(4) | fork | F17, F19 | `s 88(4) the employee is entitled to an extra day's salary at the basic rate of pay`; `s 88(4) the total the employee must be paid for the day` |
| 3434-3441 | s 88(4A) | encoded |  | `s 88(4A) the time off the employee may be given in lieu`; `s 88(4A) this rule applies to the employee`; `s 88(4A) the pay the employee must be paid for the day` |
| 3443-3445 | s 88(4A)(a) | encoded |  | `s 88(4A) the time off the employee may be given in lieu` |
| 3447-3454 | s 88(4A)(b) | encoded |  | `s 88(4A) the time off the employee may be given in lieu` |
| 3458-3459 | s 88(5) | encoded |  | `s 88(5) the employee is entitled by reason of subsection (4) to receive double the allowance` |
| 3461-3464 | s 88(6) | encoded |  | `s 88(6) subsection (4) applies to the employee`; `s 88(6)(a) the employee may be required to work on the public holiday`; `s 88(6)(b) the employee must be given a day or part of a day off in substitution` |
| 3469-3472 | s 88(6)(a) | encoded |  | `s 88(6)(a) the employee may be required to work on the public holiday` |
| 3474-3476 | s 88(6)(b) | encoded |  | `s 88(6)(b) the employee must be given a day or part of a day off in substitution` |
| 3480-3482 | s 88(7) | encoded |  | `s 88(7) the rate of pay payable for the public holiday`; `s 88(7) the rule of subsection (7) applies` |
| 3488-3491 | s 88A(1) | encoded |  | `s 88A(1)(a) the days of paid annual leave for the first 12 months`; `s 88A(1)(b) the additional days for the year of continuous service`; `s 88A(1)(c) the most days of paid annual leave` (+1 more) |
| 3493-3494 | s 88A(1)(a) | encoded |  | `s 88A(1)(a) the days of paid annual leave for the first 12 months` |
| 3496-3498 | s 88A(1)(b) | encoded |  | `s 88A(1)(b) the additional days for the year of continuous service` |
| 3500 | s 88A(1)(c) | encoded |  | `s 88A(1)(c) the most days of paid annual leave` |
| 3504-3507 | s 88A(2) | fork | F11 | `s 88A(2) with (3) the days of paid annual leave in proportion to the completed months` |
| 3511-3512 | s 88A(3) | encoded |  | `s 88A(3) the whole days of proportionate annual leave` |
| 3514-3515 | s 88A(3)(a) | encoded |  | within `s 88A(3) the whole days of proportionate annual leave` |
| 3520-3521 | s 88A(3)(b) | encoded |  | within `s 88A(3) the whole days of proportionate annual leave` |
| 3525-3528 | s 88A(4) | encoded |  | `s 88A(4) the days counted as continuous service` |
| 3532-3536 | s 88A(5) | encoded |  | `s 88A(5) the employee keeps the entitlement to annual leave`; `s 88A(5) the employee forfeits the entitlement to annual leave` |
| 3540-3541 | s 88A(6) | encoded |  | `s 88A(6)(a) the duty to grant and to take the paid annual leave`; `s 88A(6)(a) the days from today until the last day for taking the paid annual leave`; `s 88A(6)(a) the last day for taking the paid annual leave` (+3 more) |
| 3543-3545 | s 88A(6)(a) | encoded |  | `s 88A(6)(a) the duty to grant and to take the paid annual leave`; `s 88A(6)(a) the days from today until the last day for taking the paid annual leave`; `s 88A(6)(a) the last day for taking the paid annual leave` (+1 more) |
| 3547-3548 | s 88A(6)(b) | encoded |  | `s 88A(6)(b) the employee is still entitled to the paid annual leave not taken`; `s 88A(6)(b) the employee ceases to be entitled to the paid annual leave not taken` |
| 3552-3553 | s 88A(7) | encoded |  | `s 88A(7) the amount the employer must pay for the paid annual leave` |
| 3557-3561 | s 88A(8) | encoded |  | `s 88A(8) the amount the employer must pay for the paid annual leave not taken` |
| 3565-3566 | s 88A(9) | inert | reason 2: the Minister's power, by notification in the Gazette, to do the things in (a) and (b) | - |
| 3568-3570 | s 88A(9)(a) | inert | reason 2: part of the Minister's power in s 88A(9) | - |
| 3575-3577 | s 88A(9)(b) | inert | reason 2: part of the Minister's power in s 88A(9) | - |
| 3583-3586 | s 89(1) | encoded |  | `s 89(1) the most days of paid sick leave in the year` |
| 3588 | s 89(1)(a) | encoded |  | within `s 89(1) the most days of paid sick leave in the year` |
| 3590-3595 | s 89(1)(b) | encoded |  | within `s 89(1) the most days of paid sick leave in the year` |
| 3599-3602 | s 89(2) | encoded |  | `s 89(2)(a) the most days of paid sick leave in the year`; `s 89(2)(b) the most days of paid sick leave in the year`; `s 89(2)(c) the most days of paid sick leave in the year` (+4 more) |
| 3604-3616 | s 89(2)(a) | encoded |  | `s 89(2)(a) the most days of paid sick leave in the year`; `s 89(2)(a) this paragraph applies to the employee` |
| 3618-3633 | s 89(2)(b) | encoded |  | `s 89(2)(b) the most days of paid sick leave in the year`; `s 89(2)(b) this paragraph applies to the employee` |
| 3635-3647 | s 89(2)(c) | encoded |  | `s 89(2)(c) the most days of paid sick leave in the year`; `s 89(2)(c) this paragraph applies to the employee` |
| 3651 | s 89(3) | encoded |  | `s 89(3)(a) the employee is hospitalised`; `s 89(3)(b) the employee is to be treated as hospitalised for the period`; `s 89(3) the employee is hospitalised or treated as hospitalised` |
| 3653-3656 | s 89(3)(a) | encoded |  | `s 89(3)(a) the employee is hospitalised` |
| 3658-3670 | s 89(3)(b) | encoded |  | `s 89(3)(b) the employee is to be treated as hospitalised for the period` |
| 3677 | s 89(4) | encoded |  | `s 89(4) the employee is deemed to have absented himself or herself without the employer's permission and without reasonable excuse` |
| 3679 | s 89(4)(a) | encoded |  | within `s 89(4) the employee is deemed to have absented himself or herself without the employer's permission and without reasonable excuse` |
| 3681-3688 | s 89(4)(b) | fork | F23 | within `s 89(4) the employee is deemed to have absented himself or herself without the employer's permission and without reasonable excuse` |
| 3692-3693 | s 89(5) | encoded |  | `s 89(5) the amount the employer must pay for the days of sick leave` |
| 3695-3697 | s 89(5)(a) | encoded |  | within `s 89(5) the amount the employer must pay for the days of sick leave` |
| 3699 | s 89(5)(b) | encoded |  | within `s 89(5) the amount the employer must pay for the days of sick leave` |
| 3701-3706 | s 89(6) | fork | F12 | `s 89(6) the employee is entitled to paid sick leave on the day` |
| 3708-3713 | s 89(7) | encoded |  | `s 89(7) the employee is entitled to paid sick leave for the period` |
| 3717-3720 | s 89(7A) | encoded |  | `s 89(7A) the employer is liable to bear or reimburse the fees of the examination` |
| 3722-3723 | s 89(7A)(a) | encoded |  | within `s 89(7A) the employer is liable to bear or reimburse the fees of the examination` |
| 3728-3729 | s 89(7A)(b) | encoded |  | within `s 89(7A) the employer is liable to bear or reimburse the fees of the examination` |
| 3733-3734 | s 89(8) | encoded |  | `s 89(8) the employer is deemed to fulfil its obligation under subsection (7A)` |
| 3736-3742 | s 89(8)(a) | encoded |  | within `s 89(8) the employer is deemed to fulfil its obligation under subsection (7A)` |
| 3744-3745 | s 89(8)(b) | encoded |  | within `s 89(8) the employer is deemed to fulfil its obligation under subsection (7A)` |
| 3749 | s 89(9) | inert | reason 2: the terms and revocation of the Commissioner's order under s 89(8)(a) | - |
| 3751-3753 | s 89(9)(a) | inert | reason 2: a term of the Commissioner's order under s 89(8)(a) | - |
| 3755 | s 89(9)(b) | inert | reason 2: a term of the Commissioner's order under s 89(8)(a) | - |
| 3757-3758 | s 89(9)(c) | inert | reason 2: revocation of the Commissioner's order under s 89(8)(a) | - |
| 3760-3763 | s 89(10) | encoded |  | `s 89(10) section 89 applies to the employee` |
| 3769-3779 | s 90(1) | encoded |  | `s 90(1) the employer is guilty of an offence`; `s 90(1) the penalty on conviction` |
| 3783 | s 90(2) | encoded |  | `s 90(2)(a) the employer and the employees or their trade union may negotiate for and agree to the terms`; `s 90(2)(b) it is an offence for the employer to grant the terms` |
| 3785-3789 | s 90(2)(a) | encoded |  | `s 90(2)(a) the employer and the employees or their trade union may negotiate for and agree to the terms` |
| 3791-3793 | s 90(2)(b) | encoded |  | `s 90(2)(b) it is an offence for the employer to grant the terms` |
| 3797 | Part 11 (heading) | repealed or blank in this text | PART 11 has no title; its four sections each show "[Repealed by Act 32 of 2008]" | - |
| 3798 | s 91 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 3799 | s 92 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 3800 | s 93 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 3801 | s 94 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 3803-3806 | Part 12 Registers, returns and other documentary requirements | inert | reason 1: Part heading | - |
| 3810-3812 | s 95(1) | encoded |  | `s 95(1) the employer must make and keep an employee record for the person`; `s 95(1) the employer failed to comply` |
| 3814 | s 95(1)(a) | encoded |  | within `s 95(1) the employer must make and keep an employee record for the person`; `s 95(1) the employer failed to comply` |
| 3816 | s 95(1)(b) | encoded |  | within `s 95(1) the employer must make and keep an employee record for the person`; `s 95(1) the employer failed to comply` |
| 3820-3827 | s 95(2) | encoded |  | `s 95(2) the employer failed to ensure that the employee record is readily accessible` |
| 3831-3834 | s 95(3) | encoded |  | `s 95(3) the employer is taken to have failed to comply with subsection (1)` |
| 3838-3840 | s 95(4) | inert | reason 2: power to prescribe different record retention periods; the period arrives as an input to s 95(1) | - |
| 3844-3847 | s 95(5) | encoded |  | `s 95(5) "employee record" the record is one` |
| 3853-3854 | s 95A(1) | encoded |  | `s 95A(1) section 95A applies to the employee` |
| 3856-3857 | s 95A(1)(a) | encoded |  | within `s 95A(1) section 95A applies to the employee` |
| 3859-3860 | s 95A(1)(b) | encoded |  | within `s 95A(1) section 95A applies to the employee` |
| 3864-3868 | s 95A(2) | fork | F15 | `s 95A(2) the duty to give the written record`; `s 95A(2) the days allowed for giving the written record`; `s 95A(2) the last day for giving the written record of the key employment terms` (+1 more) |
| 3872-3873 | s 95A(3) | encoded |  | `s 95A(3) the requirement to give a written record is satisfied` |
| 3875-3882 | s 95A(3)(a) | encoded |  | within `s 95A(3) the requirement to give a written record is satisfied` |
| 3884-3891 | s 95A(3)(b) | encoded |  | within `s 95A(3) the requirement to give a written record is satisfied` |
| 3895-3897 | s 95A(4) | encoded |  | `s 95A(4) subsection (3) limits the manner of giving the record` |
| 3901-3904 | s 95A(5) | encoded |  | `s 95A(5) the employer is taken to have failed to comply with subsection (2)` |
| 3908-3910 | s 95A(6) | encoded |  | `s 95A(2) the employer failed to comply` |
| 3912-3913 | s 95A(6)(a) | encoded |  | `s 95A(2) the employer failed to comply` |
| 3915-3916 | s 95A(6)(b) | encoded |  | `s 95A(2) the employer failed to comply` |
| 3920-3923 | s 95A(7) | encoded |  | `s 95A(7) "key employment term" the term is one` |
| 3932 | s 96(1) | encoded |  | `s 96(1)(a) the employer failed to give the employee a pay slip`; `s 96(1)(b) the employer failed to give the employee a pay slip for the sum paid`; `s 96(1) the employer failed to comply` |
| 3934-3937 | s 96(1)(a) | encoded |  | `s 96(1)(a) the employer failed to give the employee a pay slip` |
| 3939-3940 | s 96(1)(b) | encoded |  | `s 96(1)(b) the employer failed to give the employee a pay slip for the sum paid` |
| 3944-3946 | s 96(2) | encoded |  | `s 96(2) the pay slip given meets the requirements of form and information` |
| 3950-3954 | s 96(3) | encoded |  | `s 96(3) the requirement to give a pay slip is satisfied` |
| 3958-3961 | s 96(4) | encoded |  | `s 96(4) the employer is taken to have failed to comply with subsection (1)` |
| 3965-3967 | s 96(5) | encoded |  | `s 96(1) the employer failed to comply` |
| 3969-3970 | s 96(5)(a) | encoded |  | `s 96(1) the employer failed to comply` |
| 3972-3973 | s 96(5)(b) | encoded |  | `s 96(1) the employer failed to comply` |
| 3983-3987 | s 96A(1) | encoded |  | `s 96A the employer failed to comply with a requirement in the notification`; `S 200/2019 para 3(1) the Notification applies to the employer` |
| 3991-3994 | s 96A(2) | encoded |  | `s 96A the employer failed to comply with a requirement in the notification` |
| 4000-4006 | s 97(1) | encoded |  | `s 97(1) the employer must furnish the particulars and information prescribed in the return` |
| 4008-4011 | s 97(2) | encoded |  | `s 97(2) the person is bound to furnish the particulars or information` |
| 4015-4020 | s 98(1) | encoded |  | `s 98(1) the employer is required to furnish the fuller or further returns` |
| 4025 | s 98(2) | inert | reason 2: what a requisition may specify: power to set the content of a notice | - |
| 4027-4028 | s 98(2)(a) | inert | reason 2: part of the power to set the content of a requisition | - |
| 4030 | s 98(2)(b) | inert | reason 2: part of the power to set the content of a requisition | - |
| 4032-4035 | s 98(2)(c) | inert | reason 2: part of the power to set the content of a requisition | - |
| 4037-4045 | s 99 | encoded |  | `s 99 the person must complete and deliver the return, or attend and produce the books, documents, accounts and returns, as the notice requires` |
| 4047 | s 100 | repealed or blank in this text | the text shows "[Repealed ...]" | - |
| 4051 | s 101(1) | fork | F16, F19 | `s 101(1)(a) the employer is guilty of an offence`; `s 101(1)(b) the employer is guilty of an offence`; `s 101(1)(c) the employer is guilty of an offence` (+5 more) |
| 4053-4060 | s 101(1)(a) | encoded |  | `s 101(1)(a) the employer is guilty of an offence` |
| 4062-4065 | s 101(1)(b) | encoded |  | `s 101(1)(b) the employer is guilty of an offence` |
| 4070-4080 | s 101(1)(c) | encoded |  | `s 101(1)(c) the employer is guilty of an offence` |
| 4082-4084 | s 101(2) | encoded |  | `s 101(2) the certificate is sufficient prima facie evidence of the facts it states` |
| 4086-4088 | s 101(3) | encoded |  | `s 101(3) subsections (1) and (2) apply to the information` |
| 4094-4103 | s 102(1) | encoded |  | `s 102(1) the return or answer may be published`; `s 102(1) the return or answer must not be published`; `s 102(1) the person may be permitted to see the individual return` (+1 more) |
| 4105-4117 | s 102(2) | encoded |  | `s 102(2) the person must make the declaration in the prescribed form`; `s 102(2) the person is guilty of an offence`; `s 102(2) the penalty on conviction` |
| 4119-4124 | s 102(3) | encoded |  | `s 102(3) the publication may disclose or arrange the particulars in that way` |
| 4126-4131 | s 102(4) | encoded |  | `s 102(4) the person is guilty of an offence`; `s 102(4) the penalty on conviction` |
| 4133-4135 | s 102(5) | encoded |  | `s 102(5) subsections (1) to (4) apply to the information` |
| 4139-4141 | Part 13 Inspection and enquiry | inert | reason 1: Part heading | - |
| 4145-4146 | s 103(1) | encoded |  | `s 103(1) the official has the powers in this subsection`; `s 103(1)(a) the official may enter and search the premises`; `s 103(1)(aa) the official may enter the place of employment without previous notice` (+8 more) |
| 4148-4151 | s 103(1)(a) | encoded |  | `s 103(1)(a) the official may enter and search the premises` |
| 4153-4156 | s 103(1)(aa) | encoded |  | `s 103(1)(aa) the official may enter the place of employment without previous notice` |
| 4158-4166 | s 103(1)(b) | encoded |  | `s 103(1)(b) the official may examine the person orally and reduce the answer or statement into writing` |
| 4168-4174 | s 103(1)(c) | encoded |  | `s 103(1)(c) the official may require the person to produce the document and to answer questions about it` |
| 4176-4179 | s 103(1)(d) | encoded |  | `s 103(1)(d) the official may examine the notice or document` |
| 4181-4182 | s 103(1)(e) | encoded |  | `s 103(1)(e) the official may make copies of or retain the notice or document` |
| 4184-4188 | s 103(1)(f) | encoded |  | `s 103(1)(f) the official may retain the samples for analysis` |
| 4190-4194 | s 103(1)(g) | encoded |  | `s 103(1)(g) the official may take the photograph or audio or video recording` |
| 4196-4198 | s 103(1)(h) | encoded |  | `s 103(1)(h) the official may require the person to produce the article and, if necessary, take it into custody` |
| 4202-4204 | s 103(2) | encoded |  | `s 103(2) the person examined is bound to state truly the facts and circumstances with which the person is acquainted` |
| 4209-4211 | s 103(3) | encoded |  | `s 103(3) the statement must be read over to the person and, after correction, signed by the person` |
| 4213-4214 | s 103(4) | encoded |  | `s 103(4) the Commissioner or the inspecting officer must show his or her credentials` |
| 4219-4223 | s 104 | encoded |  | `s 104 the official must notify the employer or the employer's representative of his or her presence` |
| 4227-4228 | s 105(1) | encoded |  | `s 105(1) the inspecting officer may arrest the person without warrant` |
| 4230-4231 | s 105(1)(a) | encoded |  | within `s 105(1) the inspecting officer may arrest the person without warrant` |
| 4233-4234 | s 105(1)(b) | encoded |  | within `s 105(1) the inspecting officer may arrest the person without warrant` |
| 4238-4243 | s 105(2) | encoded |  | `s 105(2) the inspecting officer may arrest the person without warrant` |
| 4247-4249 | s 105(3) | encoded |  | `s 105(3) the inspecting officer must produce the person arrested before a Magistrate's Court` |
| 4253-4261 | s 105(4) | encoded |  | `s 105(4) the prohibition on detaining the person in custody`; `s 105(4) the inspecting officer may detain the person in custody for that long`; `s 105(4) the inspecting officer must not detain the person in custody for that long` |
| 4265-4267 | s 105(5) | encoded |  | `s 105(5) an inspecting officer may release the person on bail or on his or her own bond` |
| 4273-4275 | s 105A(1) | encoded |  | `s 105A(1) the inspecting officer must touch or confine the body of the person to be arrested` |
| 4279-4280 | s 105A(2) | encoded |  | `s 105A(2) the inspecting officer may use all means necessary to effect the arrest` |
| 4286-4287 | s 105B(1) | encoded |  | `s 105B(1) the person arrested may be subjected to the restraint` |
| 4291-4292 | s 105B(2) | encoded |  | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| 4294 | s 105B(2)(a) | encoded |  | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| 4296 | s 105B(2)(b) | encoded |  | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| 4298 | s 105B(2)(c) | encoded |  | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| 4300 | s 105B(2)(d) | encoded |  | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| 4304-4305 | s 105B(3) | encoded |  | `s 105B(3) the handcuffs or similar means of restraint may be used` |
| 4311-4319 | s 105C(1) | encoded |  | `s 105C(1) the inspecting officer may take possession of the article found upon the person` |
| 4323-4325 | s 105C(2) | encoded |  | `s 105C(2) the inspecting officer may make the search`; `s 105C(2) the search must be made by an inspecting officer of the same sex as the person` |
| 4331-4333 | s 105D | inert | reason 2: equipping inspecting officers: administration of the office, no effect on any person | - |
| 4339-4341 | s 105E | encoded |  | `s 105E the inspecting officer may take the offensive weapon from the person arrested` |
| 4347-4351 | s 105F | encoded |  | `s 105F the inspecting officer may immediately pursue and arrest the person in any place within Singapore` |
| 4357-4362 | s 106 | encoded |  | `s 106 the prohibition on revealing a manufacturing or commercial secret`; `s 106 the person may reveal the manufacturing or commercial secret` |
| 4364-4365 | s 106A(1) | encoded |  | `s 106A(1) what must be done with the document, article or thing` |
| 4370-4372 | s 106A(1)(a) | encoded |  | `s 106A(1) what must be done with the document, article or thing` |
| 4374-4375 | s 106A(1)(b) | encoded |  | `s 106A(1) what must be done with the document, article or thing` |
| 4379-4381 | s 106A(2) | encoded |  | `s 106A(2) the Magistrate may order the document, article or thing to be forfeited or to be disposed of` |
| 4383 | s 106A(2)(a) | encoded |  | `s 106A(2) the Magistrate may order the document, article or thing to be forfeited or to be disposed of` |
| 4385-4386 | s 106A(2)(b) | encoded |  | `s 106A(2) the Magistrate may order the document, article or thing to be forfeited or to be disposed of` |
| 4390-4391 | s 106A(3) | encoded |  | `s 106A(3) section 106A prejudices the right to retain or dispose of the property` |
| 4397 | s 107 | encoded |  | `s 107(a) the person is guilty of an offence`; `s 107(b) the person is guilty of an offence`; `s 107(c) the person is guilty of an offence` (+2 more) |
| 4399-4400 | s 107(a) | encoded |  | `s 107(a) the person is guilty of an offence` |
| 4402-4405 | s 107(b) | encoded |  | `s 107(b) the person is guilty of an offence` |
| 4407-4413 | s 107(c) | encoded |  | `s 107(c) the person is guilty of an offence` |
| 4418-4420 | Part 14 General | inert | reason 1: Part heading | - |
| 4425-4427 | s 107A(1) | encoded |  | `s 107A(1) the gross rate of pay per day` |
| 4429-4431 | s 107A(2) | encoded |  | `s 107A(2) the basic rate of pay per day` |
| 4435-4442 | s 108 | encoded |  | `s 108 the employer is guilty of an offence`; `s 108 the penalty on conviction`; `s 108 the court may adjudge the whole or any portion of the fine to be paid to the employee` |
| 4447-4449 | s 109 | encoded |  | `s 109 the employee is bound to answer for the debt, default or miscarriage of another person` |
| 4453-4457 | s 110 | encoded |  | `s 110 the employer or other person is guilty of an offence`; `s 110 the penalty on conviction` |
| 4464-4466 | s 111 | encoded |  | `s 111 the person is guilty of an offence` |
| 4470-4475 | s 112 | encoded |  | `s 112 first conviction`; `s 112 subsequent conviction`; `s 112 the penalty on conviction` |
| 4479-4481 | s 112A | encoded |  | `s 112A the person is guilty of the offence abetted`; `s 112A the punishment of the person who abets` |
| 4487-4494 | s 113 | encoded |  | `s 113 the person is guilty of an offence`; `s 113 the penalty on conviction` |
| 4496-4497 | s 113A(1) | encoded |  | `s 113A(1) the officer of the body corporate is guilty of the offence as well` |
| 4499-4500 | s 113A(1)(a) | encoded |  | `s 113A(1) the officer of the body corporate is guilty of the offence as well` |
| 4502-4505 | s 113A(1)(b) | encoded |  | `s 113A(1) the officer of the body corporate is guilty of the offence as well` |
| 4512-4515 | s 113A(2) | encoded |  | `s 113A(2) subsection (1) applies to the member as if he or she were a director` |
| 4519-4520 | s 113A(3) | encoded |  | `s 113A(3) the partner is guilty of the offence as well` |
| 4522-4523 | s 113A(3)(a) | encoded |  | `s 113A(3) the partner is guilty of the offence as well` |
| 4525-4528 | s 113A(3)(b) | encoded |  | `s 113A(3) the partner is guilty of the offence as well` |
| 4532-4533 | s 113A(4) | encoded |  | `s 113A(4) the officer or member is guilty of the offence as well` |
| 4535-4537 | s 113A(4)(a) | encoded |  | `s 113A(4) the officer or member is guilty of the offence as well` |
| 4539-4544 | s 113A(4)(b) | encoded |  | `s 113A(4) the officer or member is guilty of the offence as well` |
| 4548-4554 | s 113A(5) | encoded |  | `s 113A(5) the offence is presumed to be attributable to the neglect of the person` |
| 4556-4557 | s 113A(5)(a) | encoded |  | `s 113A(5) the offence is presumed to be attributable to the neglect of the person` |
| 4562-4563 | s 113A(5)(b) | encoded |  | `s 113A(5) the offence is presumed to be attributable to the neglect of the person` |
| 4567 | s 113A(6) | encoded |  | `s 113A(6) "body corporate" the entity is one`; `s 113A(6) "officer" of a body corporate the person is one`; `s 113A(6) "officer" of an unincorporated association the person is one` (+1 more) |
| 4569-4570 | s 113A(6) "body corporate" | encoded |  | `s 113A(6) "body corporate" the entity is one` |
| 4572 | s 113A(6) "officer" | encoded |  | `s 113A(6) "officer" of a body corporate the person is one`; `s 113A(6) "officer" of an unincorporated association the person is one` |
| 4574-4578 | s 113A(6) "officer"(a) | encoded |  | `s 113A(6) "officer" of a body corporate the person is one` |
| 4580-4586 | s 113A(6) "officer"(b) | encoded |  | `s 113A(6) "officer" of an unincorporated association the person is one` |
| 4588 | s 113A(6) "partner" | encoded |  | `s 113A(6) "partner" the person is one` |
| 4592-4596 | s 113A(7) | inert | reason 2: regulation-making power of the Minister | - |
| 4602-4605 | s 114 | encoded |  | `s 114 the Commissioner may compound the offence by accepting the sum` |
| | **Employment (Retrenchment Reporting) Notification 2019** | | | |
| Notification 24-25 | S 200/2019 para 1 | encoded |  | `S 200/2019 para 1 the Notification is in operation on the day` |
| Notification 27-29 | S 200/2019 para 2(1) "employer" | repealed or blank in this text | the definition is followed by "[Deleted by S 781/2021 wef 01/11/2021 ]" | - |
| Notification 30-33 | S 200/2019 para 2(1) "retrench" | encoded |  | `S 200/2019 para 2(1) "retrench" the termination is a retrenchment` |
| Notification 36-39 | S 200/2019 para 2(1) "retrenchment report" | encoded |  | `S 200/2019 para 2(1) "retrenchment report" the report is one` |
| Notification 40-41 | S 200/2019 para 2(1) "working day" | encoded |  | `S 200/2019 para 2(1) "working day" the day is one` |
| Notification 42-44 | S 200/2019 para 2(2) | encoded |  | `S 200/2019 para 2(2) the employee is one to whom the Notification refers` |
| Notification 45 | S 200/2019 para 2(2)(a) | encoded |  | `S 200/2019 para 2(2) the employee is one to whom the Notification refers` |
| Notification 46 | S 200/2019 para 2(2)(b) | encoded |  | `S 200/2019 para 2(2) the employee is one to whom the Notification refers` |
| Notification 47-50 | S 200/2019 para 2(3) | fork | F20 (orphan after the deletion of "employer" (NOTES.md, finding 2)) | `S 200/2019 para 2(3) the employer has 10 or more employees` |
| Notification 52-56 | S 200/2019 para 3(1) | fork | F20 (the Act-as-written reading and the 10-employee reading, two rules) | `S 200/2019 para 3(1) the Notification applies to the employer`; `S 200/2019 para 3(1) the Notification applies to the employer, if the 10-employee definition still operates` |
| Notification 57-59 | S 200/2019 para 3(2) | fork | F24 (a report that states every listed item is not shown complete: the lists are not closed) | `S 200/2019 para 3(2) the report contains all the information specified in the Schedule` |
| Notification 62-64 | S 200/2019 para 4 | encoded |  | `S 200/2019 para 4 the duty to give the retrenchment report`; `S 200/2019 para 4 the days allowed for giving the retrenchment report`; `S 200/2019 para 4 helper: the nth working day after` (+2 more) |
| Notification 69-71 | S 200/2019 para 5 | encoded |  | `S 200/2019 para 5 the requirement as to the form of the report is met` |
| Notification 75-77 | S 200/2019 sch 1 (intro) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 78 | S 200/2019 sch 1(a) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 79-80 | S 200/2019 sch 1(a)(i) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 81 | S 200/2019 sch 1(a)(ii) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 82-83 | S 200/2019 sch 1(a)(ii)(A) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 84-87 | S 200/2019 sch 1(a)(ii)(B) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 88 | S 200/2019 sch 1(b) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 89-90 | S 200/2019 sch 1(c) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 91-95 | S 200/2019 sch 1(d) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 96 | S 200/2019 sch 1(e) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 97-98 | S 200/2019 sch 1(f) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 99-105 | S 200/2019 sch 1(g) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 107 | S 200/2019 sch 2 (intro) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 108-111 | S 200/2019 sch 2(a) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 112-113 | S 200/2019 sch 2(b) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 114-115 | S 200/2019 sch 2(c) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 116 | S 200/2019 sch 2(d) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 118 | S 200/2019 sch 2(e) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 119-120 | S 200/2019 sch 2(f) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 121-122 | S 200/2019 sch 2(g) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |
| Notification 123-124 | S 200/2019 sch 2(h) | encoded | a constructor of `S 200/2019 Schedule item` named for the item | `S 200/2019 Schedule the items the report must state` |

## Fork register (ea2)

The two rulings of 2026-11-04 that govern how this part treats negation are copied word for word from the brief; the two rulings of 2026-11-05 on periods, "where" and delegated definitions follow them, in this part's own words:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

How this part applied them.
E1: every section answers on its own (option C).
Option B appears only as hand-gathering, flagged here as fork F8: `s 66A(1) gathered with (2)`, `s 76(1A) gathered with ss 76(2) to (5A) and 83`, and `s 76(1A) gathered with s 80(3): the amount of the payment`.
No rule is gathered by bare name.
N2: a flat negative ("must not", "is not entitled", "does not apply") is `JUST FALSE`; where the text names the bearer the prohibition is derived with `SHANT` from that answer (`ea2-duties.l4`: ss 68(1), 81, 105(4) and 106).
Where the text does not name the bearer (ss 69, 73, 102(1), 102(3), 105B(1) and (3), which are in the passive) no `SHANT` is written, and the Jural relations table says so.
The Hohfeld kind of each provision is in the Jural relations table, not in the L4 answers.
The two rulings of 2026-11-05 above are applied in F18 (which words say no, and the yes/no twins that follow) and F19 (the sites that rest on an assumption the rulings do not state); F20 to F24 record the readings of the Notification's headcount and the points where an independent reviewer expected a different answer.

Every other ambiguity the encoding had to settle is below: the readings seen, the one taken, and the text that licenses each.
Line numbers are lines of `EmA1968.txt`.

- **F1. Where the day of the confinement falls (s 76(1)(a), s 76(1A)(a), s 82; lines 2768-2774, 2807-2814, 3004-3006).**
  Readings: (i) the day of the confinement is the first day of the 8 weeks "immediately after", and the 4 weeks "immediately before" end the day before; (ii) it belongs to the 4 weeks before; (iii) it belongs to neither, leaving a one-day gap.
  Taken: (i), so the 4 weeks before and the first 4 weeks after meet and the benefit period (a) is one stretch of 56 days (13 May to 7 July for a confinement on 10 June 2026), and the 4 weeks of s 82 run 28 days from the day of the confinement.
  Licence: "immediately before" and "immediately after" in s 76(1)(a)(i) and (ii) and "immediately following her confinement" in s 82; the Act counts a "week" as 7 consecutive days (s 2(1)).
  The outcomes differ by a day at each end of the period.
  Section 82 follows (i): the 4 weeks run from the day of the confinement to 27 days after it (28 days in all).
  For the last day of the 4 weeks of s 82, an independent reviewer expected a different answer; open question.
- **F2. Who chooses between the day's pay and the day off (s 76(3); lines 2865-2870).**
  Readings: the employee chooses; the employer chooses; they agree.
  Taken: the section does not say, so two rules give the two things (`s 76(3) the amount equivalent to a day's pay for the days worked` and `s 76(3) the days she may absent herself instead at the end of the benefit period`) and neither chooses.
  Licence: s 76(3) says she "is entitled to receive in addition to her gross rate of pay for that day an amount that is equivalent to a day's pay at the gross rate of pay or to absent herself from work on another day at the end of the benefit period"; it names both and no chooser.
- **F3. "the rate prescribed under section 76" (s 79(1); lines 2947-2957).**
  Readings: the gross rate of pay that s 76(1A) fixes; a rate set in regulations.
  Taken: the gross rate (the Third Schedule's answer, seam S6).
  Licence: section 76 prescribes one rate, in s 76(1A).
  Reviewer expected a different answer for s 79(1); open question.
- **F4. Which "period" the 30-day cap limits (s 79(1)).**
  Readings: the days between the last day she worked and her death; the days for which the sum is payable.
  Taken: the period for which the sum is payable; outside the circumstances of the subsection, more than 30 days is `JUST FALSE`; within them the subsection gives no answer (`NOTHING`).
  Licence: "except in the circumstances mentioned in this subsection no employer is liable to pay any sum in respect of a period exceeding 30 days".
  Reviewer expected a different answer for s 79(1); open question.
- **F5. "at least one week before" (s 80(1); lines 2970-2973).**
  Readings: 7 or more days between the day the notice is given and the first day of absence; 8 or more (a clear week); more than 6.
  Taken: 7 or more days between the two dates (a plain date comparison, which carries no legal "no").
  Licence: a "week" is 7 consecutive days (s 2(1)); the Act does not say whether the two days are counted.
- **F6. Counting back N months from a date (ss 84(1)(a) and (c), 84A(1)(a) and (c); lines 3025-3032, 3040-3053, 3117-3124, 3132-3145).**
  Readings: clamp the day to the end of a short month (31 August less 6 months is 28 February); push the overflow into the next month; count 30-day months.
  Taken: daydate's `add months`, which clamps.
  Licence: none; the staged Interpretation Act module says the Act has no rule for counting months from a day.
- **F7. "within a period of N months preceding D" (the same paragraphs).**
  Readings: the days from D less N months up to the day before D; the same including D; the same excluding the first day.
  Taken: from D less N months up to the day before D.
  Licence: "preceding" the estimated delivery date or the date of the confinement.
- **F8. Hand-gathering a legal effect (E1 option B): s 66A(1) with (2); s 76(1A) with ss 76(2) to (5A) and 83; s 76(1A) with s 80(3).**
  Readings: leave each section's answer separate (option C, the default); gather by hand into one answer.
  Taken: both, the separate answers first and, additionally, three hand-gathered rules, each flagged by name and in its header.
  The gathered rules apply the order the text gives: a declaration under s 66A(2) wins over the definition in (1); the entitlement is "subject to this section and section 77", so the exclusions in (2) to (5A) and s 83 come before the amount; s 80(3) halves the amount.
  Licence: s 76(1A) "Subject to this section and section 77"; s 66A(2).
  For s 80(3) the seat asks "how much" and the answer is the gathered amount, which is an awkward question for a person to put; reviewer expected a different answer; open question.
- **F9. The 14-day cap per child (s 87A(2)(a); lines 3250-3251).**
  Readings: a cap on all the days ever granted for the child; a cap per relevant period.
  Taken: all the days ever granted for the child; days claimed beyond what remains are `JUST FALSE`; days within the cap are not answered (`NOTHING`), since the paragraph caps and does not grant.
  Licence: "is not entitled to more than 14 days of childcare leave in respect of any child".
- **F9a. As of what day the 3 months of service are counted (s 87A(1)(a); lines 3239-3240).**
  Readings: the day asked about; the first day of the relevant period.
  Taken: completed months as of the day asked.
  Licence: "has served an employer for a period of not less than 3 months" names no day.
- **F9b. Which period each later entitlement is taken in (s 87A(2)(b); lines 3253-3267).**
  Readings: the next period after the one in which the first was taken; the next after the one for which it arose.
  Taken: the period after the one in which the first was taken, and so on for each later entitlement.
  Licence: s 87A(2)(b)(ii) says the employee must "then take his or her next and each subsequent entitlement of childcare leave of 2 days for a relevant period in the next succeeding relevant" period "and in each subsequent succeeding relevant period, respectively" (a page break falls inside the sentence in the rendering).
- **F9c. Which days are lost (s 87A(4); lines 3275-3278).**
  Readings: the days of the 2 that remain untaken at the end of the period; all 2 if any are untaken.
  Taken: the days that remain untaken.
  Licence: s 87A(4) says "any employee who fails to take that leave by that day" "(a) thereupon ceases to be entitled to that leave; and (b) is not entitled to any payment in lieu thereof" ("that leave" is the entitlement of 2 days).
- **F10. "without the prior consent of his or her employer or without reasonable excuse" (s 88(3); lines 3412-3420).**
  Readings: lacking either the consent or the excuse is enough; lacking both is needed.
  Taken: lacking either is enough, as it stands.
  Licence: the "or" between the two.
  Reviewer expected a different answer for s 88(3); open question.
- **F11. The proportion in s 88A(2); lines 3504-3507.**
  Readings: a proportion of the full-year entitlement for the year she is in; a proportion of the first year's 7 days.
  Taken: the full-year entitlement for the year she is in, rounded by subsection (3).
  Licence: "in proportion to the number of completed months of service in that year".
- **F12. A day substituted for a public holiday (s 89(6); lines 3701-3706).**
  Readings: it is a holiday "under section 88" and so excluded from paid sick leave; it is not named and so not excluded.
  Taken: not named; the case answers `NOTHING`.
  Licence: the list in s 89(6) names rest days, holidays under ss 36 or 88, days of paid annual leave, days not required to work, and days of leave without pay, and no substituted day.
- **F13. "has not completed his or her 15th year of age" (s 67A "child"; lines 2636-2637).**
  Readings: (i) the 15th year of age is the year that ends on the 15th birthday, so a person who "has not completed" it is under 15 and one who has completed it but not the 16th year is 15; (ii) the 15th year of age is the year that begins on the 15th birthday, so a child is under 16 and a young person is 16.
  Taken: (i), a child is under 15 and a young person is 15, in completed years of age.
  Licence: s 67A: "child" means a person "who has not completed his or her 15th year of age"; "young person" means a person "who has completed his or her 15th year of age but who has not completed his or her 16th year of age"; the Act does not say which year is meant, and s 68(3) speaks of a child "who is 13 years of age or above", which counts age in completed years.
- **F14. The second limb of s 73 (lines 2722-2726).**
  Readings: the circumstances and conditions are those the Minister has actually prohibited by regulations (reading 1); the sentence only states the Minister's power.
  Taken: reading 1, so a child or young person must not be employed as a workman where the Minister has prohibited the circumstances or conditions, and the first limb (regulation-making) is a power with no function here.
  Licence: "must not be employed as a workman under any circumstances or under any conditions which may be prohibited by the Minister by regulations".
- **F15. Counting "14 days after the day" (s 95A(2); lines 3864-3868).**
  Readings: count as the Interpretation Act counts "from" an event and apply its s 50(b) to the last day; count "after" as a different rule.
  Taken: the first; the Interpretation Act module counts only "from" (it answers `NOTHING` for "after"), so ea2 uses the "from" function.
  Licence: s 50 of the Interpretation Act; the Act's "after the day that the employee starts employment".
- **F16. How long a false-particulars offence continues (s 101(1); line 4051).**
  Readings: from the day the false particulars were furnished up to and not including the day the true ones were furnished; the same including that day.
  Taken: not including the day the true ones were furnished; until they are, up to and not including the day asked about.
  Licence: "the offence is deemed to continue until true particulars, information or answers have been furnished or given".
- **F17. The sum under s 88(4) (lines 3424-3430).**
  Readings: three amounts added (the extra day at the basic rate, the gross rate for the day, and the travelling allowance for the day); the travelling allowance is part of the gross rate and not added.
  Taken: three amounts added, the allowance being 0 if none is payable.
  Licence: "an extra day's salary at the basic rate of pay for one day's work in addition to the gross rate of pay for that day and to a travelling allowance, if payable ... for one day".
- **F18. Which words say no and which only limit; the yes/no twins (rulings of 2026-11-05, applied to every rule in the range).**
  Readings: a condition or period that is not met is the text's no (`JUST FALSE`); the Act is silent there (`NOTHING`).
  Taken, by the text's own words: `JUST FALSE` when the rule opens with "if", "where", "when", "whenever", "upon", "unless", "while" or "until" and the opening is not met, and for a case outside a period the text fixes in its own words ("within 7 days from", "not earlier than 28 days immediately preceding", "not later than", "all of which must be taken within the period of 12 months"); `NOTHING` when the limit is a relative clause ("who", "which"), a named complement ("a claim for reinstatement"), "Subject to", "In the case of X" or a plain scope limit with no "only" (ruling (c)).
  Where a "where" sentence itself names an exclusion (s 88(4A): "other than an employee to whom Part 4 applies by virtue of section 35(b)"), the exclusion is part of the "where".
  A type that cannot say no (a number, a date, a period, a penalty record) cannot carry the text's no, so such a rule keeps its answers and has a yes/no twin that asks "this rule applies"; the rule's own `NOTHING` is tagged to point at the twin.
  Twins of that kind: `s 76(1)(b)` and `s 76(1)(c)(i)` (the agreed weeks begin inside the window), `s 78(1)` (each instalment is paid in time), `s 87A(1)` (the entitlement arises), `s 87A(7B)` (the penalty for a repeat offender applies), `s 88(1)(b)`, `s 88(4A)` and `s 88(7)` (the rule applies), `s 88A(6)(a)` (the leave is taken in time) and `s 89(2)(a)` to `(c)` (this paragraph applies).
  The period rule `s 76(1)(c)(ii)` answers a `MAYBE BOOLEAN` itself: every period must fall inside the 12 months.
  Twins that use the text's own verb, where the older function asked the opposite question: `s 76(5A)(a)` and `(b)`, `s 76(6)`, `s 83` ("forfeits"; and "is liable to dismissal"), `s 87A(6)(a)` and `(b)` ("ceases to be entitled"; "is not entitled to payment in lieu"), `s 88A(5)` ("forfeits"), `s 88A(6)(b)` ("ceases to be entitled"), `s 81` ("it is not lawful"), `s 102(1)` ("must not be published"; "must not be permitted to see") and `s 105(4)` ("must not detain").
  `s 105C(2)` has the same shape: the older function asks whether the officer may make the search, and the twin says the search must be made by an officer of the same sex.
  The seat asks the twins, in the text's verb.
  The older functions keep their names because `ea2-duties.l4` takes `the answer of s 81` and `the answer of s 105(4)` as inputs in the older functions' polarity (`JUST FALSE` there means the prohibition holds); the twins answer the opposite way (`JUST TRUE` means the prohibition holds), so a twin's answer must not be fed to those inputs.
  Licence: Meng's rulings of 2026-11-05 above; every `JUST FALSE` quotes the words that say it.
- **F19. Sites that rest on an assumption the rulings do not state (assumed, not ruled).**
  1. "in such event" (s 88(4); lines 3424-3430) is read as "where": an employee who is not required to work on the public holiday has no entitlement to the extra day's salary, `JUST FALSE`.
  2. A "where" on an amount: `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period` (lines 3237-3246) answers `JUST 0` when the "where" fails, because a number cannot be `FALSE` (as `s 88A(8)` does, Marginal readings 3), and the twin `s 87A(1) the entitlement to childcare leave for the relevant period arises` says `JUST FALSE` for the same facts.
  3. "until" in s 101(1) (lines 4070-4080), "the offence is deemed to continue until true particulars, information or answers have been furnished or given", is read as a bar: `JUST TRUE` on the days before the true particulars are furnished, `JUST FALSE` from the day they are furnished (F16), and `NOTHING` for a day before the false particulars (the deeming runs from them, and the text says nothing of an earlier day).
  4. "the proof of which is to lie on the employer" (s 101(1)(a) lines 4053-4060, s 108 lines 4435-4442) is read as part of the offence (a relative clause, a scope limit, `NOTHING` when the excuse is proved), not as "it is a defence ... to prove".
  No provision in this range uses "it is a defence" or hands a definition to a list ("has effect for determining"), so those two rulings have no site here.
  5. "until the contrary is proved" in s 113A(5) (lines 4548-4563): `JUST FALSE` once the contrary has been proved, and `JUST FALSE` where no offence was committed by a body corporate, an unincorporated association or a partnership (the "where").
  6. "when", "whenever" and "upon" are on the ruled list and are applied, not assumed: s 76(5A), s 76(6), s 83 and s 87A(6) ("upon" the termination of employment), s 81 and s 105C(1) ("when"), s 103(1)(a) ("when he or she has reasonable cause to believe") and s 105C(2) ("whenever").
- **F20. The employer's headcount in the Notification (para 2(1) "employer", para 2(3), para 3(1); lines 28-29, 47-50 and 52-56 of `EmA1968-S200-2019.txt`).**
  Readings: (i) the definition of "employer" as "an employer with 10 or more employees" is followed by "[Deleted by S 781/2021 wef 01/11/2021 ]", so from 1 November 2021 "Every employer" in paragraph 3(1) has no threshold and the headcount of paragraph 2(3) does no work; (ii) the definition still operates, so paragraph 3(1) reaches only an employer with 10 or more employees, counted as paragraph 2(3) says.
  Taken: both.
  `S 200/2019 para 3(1) the Notification applies to the employer` takes (i); `S 200/2019 para 3(1) the Notification applies to the employer, if the 10-employee definition still operates` takes (ii) and says `JUST FALSE` for an employer of fewer than 10 at the time the notice is given.
  The seat asks the first under "does the Notification apply to my employer" and the second under a question that adds the headcount.
  Licence: para 2(3) is still in the text: "Whether or not an employer has 10 or more employees is to be worked out as at the time when a notice of retrenchment is given".
- **F21. Whether the Act applies to domestic workers before the Minister applies it (s 67; lines 2624-2629).**
  Readings: the Act applies to domestic workers only if the Minister has applied a provision, so otherwise `JUST FALSE`; the section only gives a power and is silent.
  Taken: silent, `NOTHING`.
  Licence: "The Minister may ... apply all or any of the provisions of this Act ... to all domestic workers or to any group, class or number of domestic workers": no "only", no flat negative.
  Reviewer expected a different answer; open question.
- **F22. Who commits the offence of s 74 (lines 2730-2744).**
  Readings: the offence is exactly the two acts described, so any other act is `JUST FALSE`; the relative clause ("Any person who employs ... and any parent or guardian who ...") only describes who is guilty and the Act does not say that no one else is.
  Taken: the second, `NOTHING` outside the two acts (ruling (c): a scope limit with no "only").
  Licence: "Any person who employs a child or young person in contravention of the provisions of this Part ... shall be guilty of an offence".
  Reviewer expected a different answer; open question.
- **F23. The deeming of s 89(4)(b) (lines 3677-3688).**
  Readings: sick leave certified by a medical practitioner not appointed by the employer, and of which the employee informed or tried to inform the employer within 48 hours, is not deemed absence without permission (`JUST FALSE`); the deeming is a relative clause and says nothing of that case.
  Taken: the second, `NOTHING` (ruling (c)); the 48 hours is the period in which the employee is to inform, which the deeming does not fix as a limit on a duty.
  Licence: "(b) which is certified by a medical practitioner not appointed by the employer, but of which the employee did not inform or attempt to inform the employer within 48 hours after its commencement, is deemed to have absented himself or herself from work".
  Reviewer expected a different answer; open question.
- **F24. Whether a report with every listed item is complete (Notification para 3(2) and the Schedule; lines 57-59 and 72-124 of `EmA1968-S200-2019.txt`).**
  Readings: a report that states every item the Schedule lists contains "all the information specified" (`JUST TRUE`); each list in the Schedule opens "including the following", so other information may be specified and a report that states every listed item is not shown to be complete.
  Taken: the second; a report that leaves out a listed item is `JUST FALSE`, and one that states them all is `NOTHING`.
  Licence: "including the following" in each of the Schedule's lists (list not closed).
  Reviewer expected a different answer; open question.
- **A1. The public holidays (an assumption of the seat, not a fork of the Act).**
  The Interpretation Act module and the Notification's "working day" take a list of public holidays.
  The seat cannot ask a person for a list, so it asks whether the day that would be the last day is a public holiday and builds a list of that one day (and, for the Notification's report, of at most one holiday in the period).
  Two holidays in one period are not handled by the seat; layer 1 handles any list.

## Regulative rules and what they show (ea2-duties.l4)

Positive duties with a time limit are written as regulative rules, each with a decision function beside it that gives its days; negative duties whose text names the bearer are derived from the decision function's answer.
The unit of `WITHIN` is the day, and the clock is 0 on the day the duty arises.
A plain `WITHIN` under `HENCE` counts from the previous act, so independent deadlines (the two instalments of s 78(1), the employer and the employee of s 87A(4) and s 88A(6)) are written as parallel `RAND` branches.
`#TRACE` outcomes were read by eye on l4-main-109 and l4-main-108, and the 31 evaluation outcomes of `ea2-duties.l4` are identical on the two builds.

| rule | trace | outcome |
| --- | --- | --- |
| `s 68(1) the prohibition on employing a child`, answer `JUST FALSE` | person employs a child at 3 | BREACH BY the person |
| the same, answer `JUST TRUE` or `NOTHING` | the same | FULFILLED (the prohibition does not arise on these facts) |
| `s 81 the prohibition on giving her notice of dismissal` | employer gives notice at 12 | BREACH BY her employer; FULFILLED if the answer is `NOTHING` |
| `s 105(4) the prohibition on detaining the person in custody` | detains at 49 | BREACH BY the inspecting officer; FULFILLED if `NOTHING` |
| `s 106 the prohibition on revealing a manufacturing or commercial secret` | reveals at 5 | BREACH BY the person; FULFILLED if `NOTHING` |
| `s 78(1) the duty to pay the payment in 2 instalments` 7 34 | first at 7, second at 34 | FULFILLED |
| the same | first at 8 | BREACH BY the employer (first instalment late) |
| the same | second at 35 | BREACH BY the employer (second instalment late) |
| `s 80(1) the duty to give notice` 13 | notice at 13 / at 14 | FULFILLED / BREACH BY the female employee |
| `s 87A(4) the duty to grant and to take the childcare leave` 100 | employer at 10, employee at 100 / at 101 | FULFILLED / BREACH BY the employee |
| `s 88A(6)(a) the duty to grant and to take the paid annual leave` (JUST TRUE) (JUST FALSE) 30 | employer at 5, employee at 30 / at 31 | FULFILLED / BREACH BY the employee |
| `s 95A(2) the duty to give the written record` 14 | at 14 / at 15 | FULFILLED / BREACH BY the employer |
| `S 200/2019 para 4 the duty to give the retrenchment report` 7 | at 7 / at 8 | FULFILLED / BREACH BY the employer |

`FULFILLED` from a derived prohibition means "the prohibition does not arise on these facts"; it does not mean the Act says anyone complied.
The days given to each rule are asserted in `ea2-tests-duties.l4` (18 assertions) and in `ea2-duties.l4` (9).
Positive duties with no stated time limit or number (s 80(2) "as soon as practicable", the records of s 95, the pay slip of s 96, ss 103(2) to (4) and 104) are decision functions only.

## Jural relations (ea2)

One row per provision that creates a relation.
Correlatives: a claim is the other party's duty; a privilege is the other party's no-right; a power is the other party's liability; an immunity is the other party's disability.
Provisions that create no relation are listed once, at the foot, as `none`.
Where a flat negative names its bearer, the row says that a `SHANT` is derived; where it does not (the passive voice), the row says there is no bearer named, so no `SHANT`.
Rows marked "inert" are the powers and administration of Reason 2; the relation is real but has no function in the individual's questions.

| section | holder (right, privilege, power, immunity) | relation | bearer (duty, no-right, liability, disability) | L4 rule |
| --- | --- | --- | --- | --- |
| s 66B | the Minister | power (regulations excluding or modifying the Act) | part-time employees and their employers (liability); inert, reason 2 | none (inert) |
| s 67 | the Minister | power (to apply the Act to domestic workers) | domestic workers and their employers (liability) | `s 67 the provision of the Act applies to the domestic worker` |
| s 68(1) | the child | claim (not to be employed) | any person (duty not to employ); SHANT derived: `s 68(1) the prohibition on employing a child` | `s 68(1) the prohibition on employing a child` (+1 more) |
| s 68(2) | the employer of a family-only industrial undertaking | privilege (to employ a child) | the State (no-right) | `s 68(2) a child may be employed in the undertaking` |
| s 68(3) | the employer | privilege (to employ a child of 13 or over in light work in a non-industrial undertaking) | the State (no-right) | `s 68(3) a child may be employed in the undertaking` |
| s 69 | the young person | claim (not to be employed in a declared industrial undertaking) | employers (duty); no bearer named, so no SHANT | `s 69 the young person may be employed in the undertaking` |
| s 70 | the Minister | power (regulations on conditions of employment) | employers (liability); inert, reason 2 | none (inert) |
| s 71(1) | the Minister | power (to prescribe minimum salaries) | employers (liability); inert, reason 2 | none (inert) |
| s 71(2) | the State | claim (to compliance with the Minister's order) | the employer (duty); offence | `s 71(2) the person is guilty of an offence` (+1 more) |
| s 72(1) | the employer or training body | immunity (from ss 68 and 69 for approved training work) | the State (disability) | `s 72(1) sections 68 and 69 apply to the employment` |
| s 73 | the child or young person | claim (not to be employed as a workman in prohibited circumstances) | employers (duty); no bearer named, so no SHANT; first limb is the Minister's power (inert, reason 2) | `s 73 the child or young person may be employed as a workman` |
| s 74 | the State | claim (no employment in breach of Part 8) | the employer, parent or guardian (duty); offence | `s 74 the person is guilty of an offence` (+1 more) |
| s 75 | the State | power (to bring the child or young person before a Youth Court) | the child or young person (liability) | `s 75 the child or young person may be brought before a Youth Court` (+1 more) |
| s 76(1) | the female employee | privilege (to absent herself from work) | her employer (no-right) | `s 76(1) the person is a female employee` (+13 more) |
| s 76(1A) | the female employee | claim (payment at her gross rate for the benefit period) | her employer (duty) | `s 76(1A) the benefit period` (+4 more) |
| s 76(2) | the employer | privilege (no pay if served less than 90 days; confinement before 1 May 2013) | the female employee (no-right) | `s 76(2) the female employee is entitled to pay during the benefit period` |
| s 76(2A) | the employer | privilege (no pay if served less than 3 months; the 2013-2015 tier) | the female employee (no-right) | `s 76(2A) the female employee is entitled to pay during the benefit period` (+1 more) |
| s 76(2B) | the employer | privilege (no pay if served less than 3 months; from 22 August 2015) | the female employee (no-right) | `s 76(2B) the female employee is entitled to pay during the benefit period` (+1 more) |
| s 76(3) | the female employee | claim (a day's pay, or a day off, for each day worked in the benefit period) | her employer (duty) | `s 76(3) the amount equivalent to a day's pay for the days worked` (+1 more) |
| s 76(4) | the employer | privilege (no payment for the third or later qualifying confinement) | the female employee (no-right) | `s 76(4) the female employee is entitled to payment under subsection (1A) for the confinement` |
| s 76(5) | the female employee in a specified class | immunity (from subsection (4)) | her employer (disability) | `s 76(5) subsection (4) applies to the female employee` |
| s 76(5A) | the employer | privilege (no duty to the unused entitlement after resignation) | the female employee (no-right) | `s 76(5A)(a) the female employee keeps the entitlement to absent herself from work` (+3 more) |
| s 76(6) | the employer | privilege (no duty to the unused further periods after the employment ends) | the female employee (no-right) | `s 76(6) the female employee keeps the entitlement under subsection (1)(c)(ii)` (+1 more) |
| s 77(1) | the female employee | claim (payment for each day of the benefit period except no-pay leave) | her employer (duty) | `s 77(1) the payment referred to in section 76 must be paid for the day` |
| s 77(2) | the employer | privilege (no extra day's salary for a holiday in the benefit period) | the female employee (no-right) | `s 77(2) section 77 requires the employer to pay an extra day's salary for the holiday` |
| s 78(1) | the daily-rated female employee | claim (payment in 2 instalments within 7 days) | her employer (duty); regulative rule `s 78(1) the duty to pay the payment in 2 instalments` | `s 78(1) the duty to pay the payment in 2 instalments` (+8 more) |
| s 78(2) | the female employee not daily-rated | claim (payment when her salary is due) | her employer (duty) | `s 78(2) the date by which the payment must be paid` |
| s 79(1) | the nominee or personal representative | claim (the sum after the employee's death) | the employer (duty) | `s 79(1) the person to whom the employer must pay` (+4 more) |
| s 79(2) | the nominee or personal representative | claim (the unpaid sum after her death) | the employer (duty) | `s 79(2) the employer must pay a sum of money after her death` (+1 more) |
| s 80(1) | the employer | claim (notice at least one week before absence) | the female employee (duty); regulative rule `s 80(1) the duty to give notice` | `s 80(1) the duty to give notice` (+3 more) |
| s 80(2) | the employer | claim (to be told the date of the confinement) | the female employee (duty) | `s 80(2) the female employee who has been confined must inform her employer of the date of the confinement` |
| s 80(3) | the employer | privilege (to pay only half where the notice was omitted) | the female employee (no-right) | `s 80(3) the female employee is entitled to only half the amount of the payment` (+1 more) |
| s 80(4) | the employer | immunity (payment to the nominee is payment to her) | the female employee (disability) | `s 80(4) the payment is deemed to be payment to the female employee` |
| s 81 | the female employee | immunity (from notice of dismissal during her absence) | her employer (disability); SHANT derived: `s 81 the prohibition on giving her notice of dismissal` | `s 81 the prohibition on giving her notice of dismissal` (+2 more) |
| s 82 | the State | claim (no knowing employment within 4 weeks after confinement) | the employer (duty); offence | `s 82 the employer is guilty of an offence` |
| s 83 | the employer | power (to dismiss) and privilege (no payment) | the female employee who works for another employer (liability and no-right) | `s 83 the female employee keeps her claim to payment under this Part` (+3 more) |
| s 84(1) | the female employee | immunity (a notice of dismissal without sufficient cause does not deprive her of payment) | her employer (disability) | `s 84(1) the notice of dismissal has the effect of depriving her of a payment under this Part` (+2 more) |
| s 84(2) | the female employee | power (to lodge a claim for reinstatement or compensation) | her employer (liability) | `s 84(2) the female employee may lodge a claim for the relief` |
| s 84(3) | the Tribunal | power (to direct reinstatement or compensation) | the employer (liability) | `s 84(3)(a) the Tribunal may direct the employer to reinstate her and to pay her the wages she would have earned` (+1 more) |
| s 84A(1) | the female employee | immunity (a notice on the ground of redundancy or reorganisation does not deprive her of payment) | her employer (disability) | `s 84A(1) the notice of dismissal has the effect of depriving her of a payment under this Part` |
| s 84A(3) | the female employee | claim (the payment is in addition to a retrenchment benefit) | her employer (duty) | `s 84A(3) the payment is in addition to a retrenchment benefit or other payment` |
| s 86 | the female employee | immunity (a contract term giving up maternity benefit is void) | her employer (disability) | `s 86 the term of the contract of service is void` |
| s 87(1) | the State | claim (no failure to grant leave or pay, no breach of s 81) | the employer (duty); offence | `s 87(1) the employer is guilty of an offence` (+1 more) |
| s 87(2) | the State | power (to punish by fine or imprisonment) | the convicted employer (liability) | `s 87(2) the penalty on conviction for an offence under section 82` |
| s 87(3) | the State | power (to punish a repeat offender more heavily) | the convicted employer (liability) | `s 87(3) the penalty on conviction of a repeat offender` |
| s 87A(1) | the employee | claim (2 days of childcare leave for each relevant period) | the employer (duty) | `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period` (+3 more) |
| s 87A(2) | the employer | privilege (no more than 14 days per child) and claim (the employee takes the first entitlement in time) | the employee (no-right and duty) | `s 87A(2)(a) the employee is entitled to the days now claimed in respect of the child` (+3 more) |
| s 87A(4) | the employee | claim (the leave is granted by the last day of the relevant period) | the employer (duty); and the employer holds the matching claim that the employee takes it (regulative rule `s 87A(4) the duty to grant and to take the childcare leave`) | `s 87A(4) the duty to grant and to take the childcare leave` (+4 more) |
| s 87A(5) | the employee | claim (pay at the gross rate for each day taken) | the employer (duty) | `s 87A(5) the amount the employer must pay for the childcare leave taken` |
| s 87A(5A) | the employer | privilege (no paid childcare leave on a day of no-pay leave) | the employee (no-right) | `s 87A(5A) the employee is entitled to take paid childcare leave on the day` |
| s 87A(6) | the employer | privilege (no duty for leave not yet taken when the employment ends) | the employee (no-right) | `s 87A(6)(a) the employee is still entitled to the leave not yet taken` (+3 more) |
| s 87A(7) | the State | claim (pay for childcare leave taken) | the employer (duty); offence | `s 87A(7) the employer is guilty of an offence` (+1 more) |
| s 87A(7A) | the State | claim (grant childcare leave to an entitled employee who asks) | the employer (duty); offence | `s 87A(7A) the employer is guilty of an offence` (+1 more) |
| s 87A(7B) | the State | power (to punish by fine or imprisonment) | the convicted employer (liability) | `s 87A(7B) the penalty on conviction of a person convicted under subsection (7) or (7A)` (+1 more) |
| s 88(1) | the employee | claim (a paid holiday on each public holiday) | the employer (duty) | `s 88(1) the employee is entitled to a paid holiday at the gross rate of pay on the public holiday` (+4 more) |
| s 88(2) | the employer | privilege (no holiday pay during no-pay leave) | the employee (no-right) | `s 88(2) the employee is entitled to holiday pay for the public holiday` |
| s 88(3) | the employer | privilege (no holiday pay after unexcused absence next to the holiday) | the employee (no-right) | `s 88(3) the employee is entitled to holiday pay for that holiday` |
| s 88(4) | the employer | power (to require work on a public holiday) | the employee (liability); the employee holds the claim to the extra day's salary | `s 88(4) the employee is entitled to an extra day's salary at the basic rate of pay` (+1 more) |
| s 88(4A) | the employee | claim (pay for the day and time off in lieu) | the employer (duty) | `s 88(4A) the time off the employee may be given in lieu` (+2 more) |
| s 88(5) | the employer | privilege (no double allowance) | the employee (no-right) | `s 88(5) the employee is entitled by reason of subsection (4) to receive double the allowance` |
| s 88(6) | the Government or statutory-authority employer | immunity (from the extra day's salary rule) | the employee (disability) | `s 88(6) subsection (4) applies to the employee` (+2 more) |
| s 88(7) | the employee | claim (pay at the full day's rate for a half working day) | the employer (duty) | `s 88(7) the rate of pay payable for the public holiday` (+1 more) |
| s 88A(1) | the employee | claim (days of paid annual leave) | the employer (duty) | `s 88A(1)(a) the days of paid annual leave for the first 12 months` (+3 more) |
| s 88A(2) | the employee | claim (proportionate annual leave) | the employer (duty) | `s 88A(2) with (3) the days of paid annual leave in proportion to the completed months` |
| s 88A(5) | the employer | privilege (no annual leave where absences exceed 20 per cent) | the employee (no-right) | `s 88A(5) the employee keeps the entitlement to annual leave` (+1 more) |
| s 88A(6) | the employee | claim (the leave is granted within 12 months), with the employer's matching claim that she takes it | the employer (duty) and the employee (duty); the unused leave is lost | `s 88A(6)(a) the duty to grant and to take the paid annual leave` (+5 more) |
| s 88A(7) | the employee | claim (pay for annual leave) | the employer (duty) | `s 88A(7) the amount the employer must pay for the paid annual leave` |
| s 88A(8) | the employee | claim (pay for annual leave not taken when the employment ends) | the employer (duty) | `s 88A(8) the amount the employer must pay for the paid annual leave not taken` |
| s 88A(9) | the Minister | power (by notification) | employers and employees (liability); inert, reason 2 | none (inert) |
| s 89(1) | the employee | claim (paid outpatient sick leave) | the employer (duty) | `s 89(1) the most days of paid sick leave in the year` |
| s 89(2) | the employee | claim (paid sick leave in the first 6 months) | the employer (duty) | `s 89(2)(a) the most days of paid sick leave in the year` (+6 more) |
| s 89(4) | the employer | privilege (to treat the absence as without permission) | the employee (no-right) | `s 89(4) the employee is deemed to have absented himself or herself without the employer's permission and without reasonable excuse` |
| s 89(5) | the employee | claim (pay for sick leave) | the employer (duty) | `s 89(5) the amount the employer must pay for the days of sick leave` |
| s 89(6) | the employer | privilege (no paid sick leave on the days listed) | the employee (no-right) | `s 89(6) the employee is entitled to paid sick leave on the day` |
| s 89(7) | the employer | privilege (no paid sick leave while work injury compensation is payable) | the employee (no-right) | `s 89(7) the employee is entitled to paid sick leave for the period` |
| s 89(7A) | the employee | claim (the employer bears or reimburses the examination fees) | the employer (duty) | `s 89(7A) the employer is liable to bear or reimburse the fees of the examination` |
| s 89(8) | the employer | immunity (deemed to fulfil the obligation) | the employee (disability) | `s 89(8) the employer is deemed to fulfil its obligation under subsection (7A)` |
| s 89(9) | the Commissioner | power (the terms and revocation of the order) | employers (liability); inert, reason 2 | none (inert) |
| s 89(10) | the employer | privilege (cosmetic treatment does not engage s 89) | the employee (no-right) | `s 89(10) section 89 applies to the employee` |
| s 90(1) | the State | claim (no employment contrary to Part 10, and payment of salary) | the employer (duty); offence and penalty | `s 90(1) the employer is guilty of an offence` (+1 more) |
| s 90(2) | the employer and employees or their trade union | privilege (to negotiate and grant more favourable terms) | the State (no-right) | `s 90(2)(a) the employer and the employees or their trade union may negotiate for and agree to the terms` (+1 more) |
| s 95(1) | the employee or former employee | claim (the employer makes and keeps an employee record) | the employer (duty) | `s 95(1) the employer must make and keep an employee record for the person` (+1 more) |
| s 95(2) | the employee or former employee | claim (the record is readily accessible) | the employer (duty) | `s 95(2) the employer failed to ensure that the employee record is readily accessible` |
| s 95(4) | the Minister | power (to prescribe retention periods) | employers (liability); inert, reason 2 | none (inert) |
| s 95A(2) | the employee | claim (a written record of the key employment terms within 14 days) | the employer (duty); regulative rule `s 95A(2) the duty to give the written record` | `s 95A(2) the duty to give the written record` (+3 more) |
| s 95A(3) | the employer | privilege (to satisfy the duty by electronic record or website) | the employee (no-right) | `s 95A(3) the requirement to give a written record is satisfied` |
| s 95A(6) | the Minister | power (to exempt by order); encoded as an input | employers (liability) | `s 95A(2) the employer failed to comply` |
| s 96(1) | the employee | claim (a pay slip) | the employer (duty) | `s 96(1)(a) the employer failed to give the employee a pay slip` (+2 more) |
| s 96(3) | the employer | privilege (to satisfy the duty by electronic record) | the employee (no-right) | `s 96(3) the requirement to give a pay slip is satisfied` |
| s 96(5) | the Minister | power (to exempt by order); encoded as an input | employers (liability) | `s 96(1) the employer failed to comply` |
| s 96A(1) | the Commissioner | power (to require retrenchment information by notification) | employers (liability); the exercise is the input `the notification applies to the employer` | `s 96A the employer failed to comply with a requirement in the notification` (+1 more) |
| s 96A(2) | the Commissioner | claim (compliance with the notification) | the employer (duty) | `s 96A the employer failed to comply with a requirement in the notification` |
| s 97(1) | the Commissioner | claim (the return) | the employer (duty) | `s 97(1) the employer must furnish the particulars and information prescribed in the return` |
| s 97(2) | the Commissioner | claim (the particulars) | the person who has access to them (duty) | `s 97(2) the person is bound to furnish the particulars or information` |
| s 98(1) | the Commissioner | power (to require fuller or further returns) | the employer (liability) | `s 98(1) the employer is required to furnish the fuller or further returns` |
| s 98(2) | the Commissioner | power (the content of a requisition) | employers (liability); inert, reason 2 | none (inert) |
| s 99 | the Commissioner | power (to require a return, attendance and books) | any person (liability) | `s 99 the person must complete and deliver the return, or attend and produce the books, documents, accounts and returns, as the notice requires` |
| s 101(1) | the State | claim (no refusal, neglect or false particulars) | the employer (duty); offence and penalty | `s 101(1)(a) the employer is guilty of an offence` (+7 more) |
| s 101(2) | the State | power (to rely on the Commissioner's certificate as prima facie evidence) | the employer (liability) | `s 101(2) the certificate is sufficient prima facie evidence of the facts it states` |
| s 101(3) | the employer | immunity (from s 101(1) and (2) for s 96A information) | the State (disability) | `s 101(3) subsections (1) and (2) apply to the information` |
| s 102(1) | the person who gave the return | immunity (a return is not published, or seen, without consent) | the State and publishers (disability); no bearer named, so no SHANT | `s 102(1) the return or answer may be published` (+3 more) |
| s 102(2) | the State | claim (the declaration by those who collect statistics, and no breach of it) | the person engaged in statistics (duty); offence and penalty | `s 102(2) the person must make the declaration in the prescribed form` (+2 more) |
| s 102(3) | the business or person in a return | immunity (from identifying publication) | the publisher (disability); no bearer named, so no SHANT | `s 102(3) the publication may disclose or arrange the particulars in that way` |
| s 102(4) | the State | claim (no publication of information disclosed in breach) | the person with the information (duty); offence and penalty | `s 102(4) the person is guilty of an offence` (+1 more) |
| s 103(1) | the Commissioner and inspecting officers | power (to enter, search, examine, require, copy, sample, photograph and take custody) | occupiers, employers and persons (liability) | `s 103(1) the official has the powers in this subsection` (+10 more) |
| s 103(2) | the inspecting officer | claim (a true statement) | the person examined (duty) | `s 103(2) the person examined is bound to state truly the facts and circumstances with which the person is acquainted` |
| s 103(3) | the person examined | claim (the statement is read over and signed after correction) | the inspecting officer (duty) | `s 103(3) the statement must be read over to the person and, after correction, signed by the person` |
| s 103(4) | the person | claim (to see credentials) | the Commissioner or inspecting officer (duty) | `s 103(4) the Commissioner or the inspecting officer must show his or her credentials` |
| s 104 | the employer | claim (to be notified of the official's presence) | the official (duty); no bearer named for a prohibition, so no SHANT | `s 104 the official must notify the employer or the employer's representative of his or her presence` |
| s 105(1) | the inspecting officer | power (to arrest without warrant) | a person suspected of an offence (liability) | `s 105(1) the inspecting officer may arrest the person without warrant` |
| s 105(2) | the inspecting officer | power (to arrest an officer or partner without warrant) | that person (liability) | `s 105(2) the inspecting officer may arrest the person without warrant` |
| s 105(3) | the person arrested | claim (to be produced before a Magistrate's Court) | the inspecting officer (duty) | `s 105(3) the inspecting officer must produce the person arrested before a Magistrate's Court` |
| s 105(4) | the person arrested | claim (not to be detained for longer than reasonable, or over 48 hours) | the inspecting officer (duty); SHANT derived: `s 105(4) the prohibition on detaining the person in custody` | `s 105(4) the prohibition on detaining the person in custody` (+2 more) |
| s 105(5) | the inspecting officer | power (to release on bail or bond) | the person arrested (liability) | `s 105(5) an inspecting officer may release the person on bail or on his or her own bond` |
| s 105A(1) | the inspecting officer | privilege (to touch or confine the body of the person) | the person to be arrested (no-right) | `s 105A(1) the inspecting officer must touch or confine the body of the person to be arrested` |
| s 105A(2) | the inspecting officer | privilege (to use all means necessary) | the person who resists (no-right) | `s 105A(2) the inspecting officer may use all means necessary to effect the arrest` |
| s 105B(1) | the person arrested | claim (not to be restrained more than necessary) | the inspecting officer (duty); no bearer named, so no SHANT | `s 105B(1) the person arrested may be subjected to the restraint` |
| s 105B(2) | the inspecting officer | privilege (to use handcuffs) | the person arrested (no-right) | `s 105B(2) the inspecting officer may use handcuffs or a similar means of restraint` |
| s 105B(3) | the person arrested | claim (no handcuffs as punishment) | the inspecting officer (duty); no bearer named, so no SHANT | `s 105B(3) the handcuffs or similar means of restraint may be used` |
| s 105C(1) | the inspecting officer | power (to take possession of articles) | the person arrested (liability) | `s 105C(1) the inspecting officer may take possession of the article found upon the person` |
| s 105C(2) | the person arrested | claim (to be searched by an officer of the same sex) | the inspecting officer (duty) | `s 105C(2) the inspecting officer may make the search` (+1 more) |
| s 105E | the inspecting officer | power (to take an offensive weapon) | the person arrested (liability) | `s 105E the inspecting officer may take the offensive weapon from the person arrested` |
| s 105F | the inspecting officer | power (to pursue and arrest a person who escapes) | the escaped person (liability) | `s 105F the inspecting officer may immediately pursue and arrest the person in any place within Singapore` |
| s 106 | the employer | claim (secrecy of manufacturing and commercial secrets) | the person who was an inspecting officer (duty); SHANT derived: `s 106 the prohibition on revealing a manufacturing or commercial secret` | `s 106 the prohibition on revealing a manufacturing or commercial secret` (+1 more) |
| s 106A(1) | the owner of the thing taken | claim (the thing is dealt with as the subsection requires) | the Commissioner or inspecting officer (duty) | `s 106A(1) what must be done with the document, article or thing` |
| s 106A(2) | the Magistrate | power (to order forfeiture or disposal) | the owner (liability) | `s 106A(2) the Magistrate may order the document, article or thing to be forfeited or to be disposed of` |
| s 107 | the State | claim (no refusal to produce, no false statement, no obstruction) | the person (duty); offence and penalty | `s 107(a) the person is guilty of an offence` (+4 more) |
| s 108 | the employee | claim (to be allowed to leave the service); the court's power to award the fine to the employee | the employer (duty); offence and penalty | `s 108 the employer is guilty of an offence` (+2 more) |
| s 109 | the employee | immunity (not bound for another's debt, default or miscarriage) | the employer or other claimant (disability) | `s 109 the employee is bound to answer for the debt, default or miscarriage of another person` |
| s 110 | the employee | claim (to appear before the Commissioner unobstructed) | the employer or other person (duty); offence and penalty | `s 110 the employer or other person is guilty of an offence` (+1 more) |
| s 111 | the State | claim (no wilful obstruction of an entry, inspection or inquiry) | the person (duty); offence and penalty | `s 111 the person is guilty of an offence` |
| s 112 | the State | power (the general penalty) | the convicted person (liability) | `s 112 first conviction` (+2 more) |
| s 112A | the State | claim (no abetment) | the abettor (duty); offence | `s 112A the person is guilty of the offence abetted` (+1 more) |
| s 113 | the person induced | claim (not to be induced to work beyond Singapore by force or fraud) | the inducer (duty); offence and penalty | `s 113 the person is guilty of an offence` (+1 more) |
| s 113A(1) | the State | power (to convict the officer as well as the body corporate) | the officer (liability) | `s 113A(1) the officer of the body corporate is guilty of the offence as well` |
| s 113A(2) | the State | power (to treat a managing member as a director) | the member (liability) | `s 113A(2) subsection (1) applies to the member as if he or she were a director` |
| s 113A(3) | the State | power (to convict the partner as well) | the partner (liability) | `s 113A(3) the partner is guilty of the offence as well` |
| s 113A(4) | the State | power (to convict the officer or member of an association as well) | the officer or member (liability) | `s 113A(4) the officer or member is guilty of the offence as well` |
| s 113A(5) | the State | privilege (a presumption of neglect) | the person primarily responsible (no-right) | `s 113A(5) the offence is presumed to be attributable to the neglect of the person` |
| s 113A(7) | the Minister | power (regulations) | bodies formed under foreign law (liability); inert, reason 2 | none (inert) |
| s 114 | the Commissioner | power (to compound an offence for a sum up to $5,000) | the person suspected (liability) | `s 114 the Commissioner may compound the offence by accepting the sum` |
| S 200/2019 para 3(1) | the Commissioner | claim (a retrenchment report) | the employer (duty) | `S 200/2019 para 3(1) the Notification applies to the employer` (+1 more) |
| S 200/2019 para 3(2) | the Commissioner | claim (all the information in the Schedule) | the employer (duty) | `S 200/2019 para 3(2) the report contains all the information specified in the Schedule` |
| S 200/2019 para 4 | the Commissioner | claim (the report within 5 working days) | the employer (duty); regulative rule `S 200/2019 para 4 the duty to give the retrenchment report` | `S 200/2019 para 4 the duty to give the retrenchment report` (+4 more) |
| S 200/2019 para 5 | the Commissioner | claim (the report in the form provided) | the employer (duty) | `S 200/2019 para 5 the requirement as to the form of the report is met` |
| S 200/2019 sch | the Commissioner | claim (the information about the employer and each retrenched employee) | the employer (duty) | `S 200/2019 Schedule the items the report must state` |

Provisions that create no relation (listed once, as `none`): s 66A(1); s 66A(2); s 67A; s 67A "child"; s 67A "young person"; s 68(4); s 72(2); s 84(1A); s 84A(2); s 85; s 87(4); s 87A(3); s 87A(7C); s 87A(8); s 88A(3); s 88A(4); s 89(3); s 91; s 92; s 93; s 94; s 95(3); s 95(5); s 95A(1); s 95A(4); s 95A(5); s 95A(7); s 96(2); s 96(4); s 100; s 102(5); s 105D; s 106A(3); s 107A(1); s 107A(2); s 113A(6); S 200/2019 para 1; S 200/2019 para 2(1); S 200/2019 para 2(2); S 200/2019 para 2(3).

## Marginal readings for a lawyer (ea2)

Points where a careful reader might disagree with how a clause was put into L4, each with the effect on the answer.

1. **No `FALSE` for compliance.**
   The Act and the Notification say what an employer must do and when an employer has failed.
   They never say that an employer who did everything has complied, so `s 95(1)`, `s 95A(2)`, `s 96(1)`, `s 96A` and `S 200/2019 the employer met every requirement concerning the report` answer `JUST TRUE` ("failed") or `JUST FALSE` ("did not meet") only where the text says so, and `NOTHING` otherwise.
   A caller who needs "complied" must not read `NOTHING` as that.
2. **`JUST 0` stands in for "no" on an amount.**
   An amount cannot be `FALSE`, so there are four places where the text says no to an amount and the rule answers `JUST 0`, each with a `FALSE-kind` comment: `s 76(1A) gathered with s 80(3): the amount of the payment` (the text says she "is not entitled to any pay during the benefit period" in the cases of s 76(2) to (5A) and s 83); `s 88A(8) the amount the employer must pay for the paid annual leave not taken` (see reading 3); and the imprisonment cell for a first offence in `s 90(1) the penalty on conviction` (the text states a fine only); and `s 87A(1) the days of childcare leave the employee is entitled to for the relevant period` where its "where" fails (F19, item 2; the twin says `JUST FALSE`).
   `NOTHING` in an amount means the Act does not give the amount.
   (NEEDS-CORE.md, item 2, proposes a third state.)
3. **Section 88A(8) is an "if" provision, and the rule of 2026-10-29 turns that into a "no".**
   The subsection says that "If an employee is dismissed on any ground other than misconduct before the employee has taken all of the employee's paid annual leave, the employer must pay the employee the employee's gross rate of pay in respect of every day of that leave not taken by the employee".
   Under the brief's rule (a condition the text introduces with "if" is the text's no for the case outside it) an employee who resigns, or is dismissed for misconduct, is answered `JUST 0`, and so is a dismissed employee with no untaken days.
   A lawyer may read the subsection as silent about resignation and misconduct, in which case those answers are `NOTHING`; the effect is that the seat tells a resigning employee "nothing" where the Act perhaps says nothing at all.
   The same applies to every `ELSE JUST FALSE` that follows a `FALSE-kind` quote beginning "If".
   The visible instances are two offence rules and a power: `s 102(4) the person is guilty of an offence` ("If any person, having possession of any information ...") answers `ELSE JUST FALSE`, while `s 101(1)` ("Any employer who ...") answers `ELSE NOTHING`, because the brief's rule treats "if" as the text's no and a relative clause as a limit on the offence; and `s 105A(2) the inspecting officer may use all means necessary to effect the arrest` ("If the person forcibly resists or tries to evade arrest") answers `ELSE JUST FALSE`.
   A reader should not take the difference between neighbouring offence rows as an accident, and a lawyer may prefer `NOTHING` throughout.
   One pair that looks inconsistent is not: `s 76(1) the person is a female employee` answers `JUST FALSE` for a person who is not an employee (it classifies, and the keel's definition of "employee" has already said no), while `s 76(1) the female employee is entitled to absent herself from work` answers `NOTHING` for the same person (the grant is limited to female employees and the section says nothing about anyone else).
4. **Dated tiers are ordinary date comparisons.**
   Sections 76(2), 76(2A), 76(2B), 84(1) and 84A(1) have tiers by date (before 1 May 2013; 1 May 2013 to 21 August 2015; from 22 August 2015; before 1 August 2013).
   They are encoded as comparisons of the dates the caller states; the seat asks only the current tier (76(2B)) for a person confined now.
5. **"Completed months".**
   Months of service are completed months (3 months is 3 completed months), and the sick-leave tiers (ss 89(1) and (2)) are read on that count: 3, 4 and 5 completed months give 5, 8 and 11 days; 6 or more give 14.
6. **The 48 hours in s 105(4).**
   The hours exclude "the time necessary for the journey from the place of arrest to the Magistrate's Court"; the input is the hours net of the journey.
   The text says "must not detain", so the seat asks the twin `s 105(4) the inspecting officer must not detain the person in custody for that long`: over 48 hours, or longer than reasonable, is `JUST TRUE` (the prohibition holds), and 48 hours or less that is reasonable is `JUST FALSE` (the text's "if" fails; F18).
   The older `s 105(4) the inspecting officer may detain ...` asks the opposite question: `JUST FALSE` over the limit and `NOTHING` at 48 hours exactly, where the subsection does not say yes.
7. **"Industrial undertaking" in s 68(2) and (3).**
   The keel reads "industrial undertaking" literally (its fork F3, `KEEL-NOTES.md` line 116: any undertaking is industrial, the four kinds being examples), which would leave the non-industrial limb of s 68(3) with nothing to apply to.
   ea2 takes the fact as an input and the seat asks it directly (its question begins "Is the place where you work an industrial undertaking").
8. **Offence rows say that an offence exists, not that anyone is charged.**
   "Guilty of an offence" is answered on the facts alleged; penalties are separate rules returning the `Penalty on conviction` record.
9. **The Notification's own "working day".**
   Paragraph 2(1) defines "working day" as a day other than a Saturday, Sunday or public holiday, and paragraph 4 counts 5 of them after the day the notice is given.
   That text governs paragraph 4, not the Interpretation Act's s 50(d).
10. **Paragraph 3(1) of the Notification gates on 1 November 2021.**
   The paragraph 1 date (1 April 2019) is encoded as written; paragraph 3(1) applies to a notice of retrenchment given on or after 1 November 2021.
11. **Public holidays in the seat.** See A1 in the fork register.

### Reading a result: FALSE and NOTHING (ea2)

Every layer-1 rule that can say "no" answers a `MAYBE BOOLEAN`: `JUST TRUE`, `JUST FALSE` or `NOTHING`.

- `JUST TRUE` and `JUST FALSE` are answers the Act itself gives, in its own words: a "means" definition, "if / only if / unless / while / until / where / when / whenever / upon / except / provided that", a period the text fixes in its own words, a closed list, or a flat negative ("must not", "is not entitled", "does not apply").
  Each `JUST FALSE` carries a comment `-- FALSE-kind (the text says no in its own words): "<quote>"`, and a script checks that each quote occurs in the raw text.
- `NOTHING` means the Act does not answer on these facts: it is silent, the list is not closed, it uses "includes", the term is undefined, it points outside the text, or its own wording limits the answer.
  Each `NOTHING` carries `-- NOTHING-kind (<why>)`.
  **Never read `NOTHING` as no.**
- A plain `BOOLEAN` or `NUMBER` answer is a date or count comparison ("at least one week before", "5 working days after") and carries no legal conclusion.

How a mistake shows up:

**Loud** (the tool says so; fix it):
a type error or unknown identifier (for example `WAIT UNTIL`, `length`, `APPEND` as an infix, `min` over dates); `eval/unsupported-equality` when an `#ASSERT` compares a regulative value; a failed assertion (a finding, never an edit to the expected value); a refused assertion.

**Silent** (exit 0, a wrong answer; these are the ones to watch):

- reading `NOTHING` as "no", or as "complied" in the compliance rules;
- `JUST 0` read as a number the Act states, when it stands for a "no" on an amount or a missing imprisonment term;
- a plain `BOOLEAN` or `NUMBER` read as a legal conclusion;
- `FULFILLED` from a derived `SHANT` read as "the Act says they complied", when it means the prohibition does not arise on these facts;
- an unparenthesised `NOT` in `IF NOT x AND y`, which parses as `NOT (x AND y)` and not as `(NOT x) AND y` (measured on l4-main-109: `IF NOT x AND y THEN 1 ELSE 2` gives 1 for `x` FALSE and `y` FALSE; the brief's rule: parenthesise every `NOT`); it was met once while drafting;
- an `l4` binary older than the prelude or corpus it reads, which fails to load the prelude and drowns the real error in `could not find a definition` messages;
- a pair of functions that ask opposite questions (`s 81 it is lawful ...` and `s 81 it is not lawful ...`, "keeps" and "forfeits", `may detain` and `must not detain`) answers opposite booleans for the same facts: read each with its own name, and prefer the one in the text's verb (F18);
- feeding a twin's answer (`s 81 it is not lawful ...`, `s 105(4) ... must not detain ...`) into the inputs `the answer of s 81` and `the answer of s 105(4)` of `ea2-duties.l4`, which expect the older functions' polarity: the prohibition is then derived for the wrong facts, with exit 0;
- the seat's "I am not sure" becoming `NOTHING`, which is right, but is easy to read as "no";
- the seat's one-holiday list (A1), which is right for one holiday and silently wrong for two in the same period.

## Seams (ea2)

The seams are PLAN section 4 (the brief cites PLAN sections 5 to 8, 11 and 12, which do not exist; PLAN has sections 1 to 6).
Taken as inputs, with exactly the types the PLAN gives:

| seam | input | type | used in |
| --- | --- | --- | --- |
| S1, S2, S3 | `the answer of s 35(a)`, `the answer of s 35(b)` | MAYBE BOOLEAN | s 88(4A), s 88A(6), `ea2-duties.l4` |
| S5 | `the answer of s 41A(2)` | MAYBE BOOLEAN | s 88(4) |
| S6 | `the answer of sch 3 gross rate of pay per day`, `the answer of sch 3 basic rate of pay per day` | MAYBE NUMBER | ss 76(1A), 76(3), 79(1), 87A(5), 88(4), 88(4A), 88A(7), 88A(8), 89(5), 107A |
| S8 | `the answer of sch 5 days` | MAYBE NUMBER | s 76(1)(c)(ii) |

Answered here (SEAMS-ANSWERED.md): S4 `s 88A the days of paid annual leave`; S9 `s 95(1) the employer failed to comply`; S10 `s 95A(2) the employer failed to comply`; S11 `s 96(1) the employer failed to comply`; S12 `s 96A the employer failed to comply with a requirement in the notification`; S15 `s 112 first conviction` and `s 112 subsequent conviction`.
Not taken: S14, because s 105(1)(a) turns on what the officer reasonably suspects (SEAMS-FOUND.md).
Found and not in the PLAN: SEAMS-FOUND.md, rows F-S1 to F-S4.

The Third Schedule (lines 5542 to 5758 of `EmA1968.txt`) and the Fifth Schedule (from line 5759) are outside this part's lines, so their answers stay inputs (S6 and S8).

The keel's definitional answers are taken as `the answer of s 2(1) "<term>"` inputs (MAYBE BOOLEAN) for "employee", "confinement", "no-pay leave", "Tribunal" and "medical officer".

## Findings: what the text turns out to say

1. **No sentence says an employer complied.**
   Sections 95, 95A, 96 and 96A and the Notification say what the employer must do and give consequences for failing; none says that an employer who did it has complied.
   The seam answers (S9 to S12) are therefore `JUST TRUE` or `NOTHING`, never `JUST FALSE` for a compliant employer.
   The deeming rules are different: `s 95(3)`, `s 95A(5)` and `s 96(4)` say that an employer "is taken to have failed to comply ... if" something is so, and answer `JUST FALSE` when that "if" fails (F18).
   That says the deeming does not arise; it does not say the employer complied.
2. **Paragraph 2(3) of the Notification is an orphan.**
   The definition of "employer" ("an employer with 10 or more employees") is followed by "[Deleted by S 781/2021 wef 01/11/2021 ]".
   Paragraph 3(1) now says "Every employer", with no threshold.
   Paragraph 2(3) still says how to work out "Whether or not an employer has 10 or more employees", at the time the notice of retrenchment is given.
   It is encoded as it reads (`S 200/2019 para 2(3) the employer has 10 or more employees`), and only the second reading of paragraph 3(1), `S 200/2019 para 3(1) the Notification applies to the employer, if the 10-employee definition still operates`, uses it (F20).
3. **The keel's reading of "industrial undertaking" leaves the non-industrial limb of s 68(3) with nothing to apply to** (see Marginal readings, 7).
4. **The imprisonment cell of `Penalty on conviction` cannot say "none".**
   Section 90(1) states a fine for a first offence and no imprisonment; the core's `longest imprisonment in months` is a MAYBE NUMBER in which `NOTHING` means no maximum is stated.
   ea2 wrote `JUST 0` (NEEDS-CORE.md, item 2).
5. **Sections 101(3) and 102(5) take the retrenchment information out of the offences and out of the secrecy rules.**
   Section 101(3): "Subsections (1) and (2) do not apply to any information furnished or required to be furnished under section 96A by an employer on the retrenchment of any employee by the employer".
   Subsection (1) is the employer's offences (refusing or neglecting to furnish particulars, furnishing false particulars, refusing to answer or giving a false answer) and (2) is the Commissioner's certificate as prima facie evidence.
   Section 102(5): "Subsections (1) to (4) do not apply to any information furnished under section 96A by an employer on the retrenchment of any employee by the employer".
   Those four subsections are the ban on publishing returns and on letting anyone not engaged on the statistics see them (1), the declaration of secrecy and its offence (2), the ban on disclosing particulars in a report (3), and the offence of publishing information disclosed in contravention (4).
   A retrenchment report under the Notification is therefore outside both the offence provisions of s 101(1) and the secrecy provisions of s 102; the duty to furnish it is s 96A.
6. **Section 105C(2) grants nothing.**
   "the search must be made by an inspecting officer of the same sex as the person" is a requirement; where it is not met the answer to "may the officer make the search" is `JUST FALSE`, and where it is met the subsection does not say whether the search is authorised, so the answer is `NOTHING`.
   The twin `s 105C(2) the search must be made by an inspecting officer of the same sex as the person` asks the text's own question: `JUST TRUE` whenever a search is necessary, and `JUST FALSE` when none is ("Whenever" is not met; F18).
7. **The Part 9 offence of dismissing during the absence is in two places.**
   Section 81 makes the notice "not lawful"; section 87(1)(c) makes the employer's act an offence.
   They are encoded separately (a prohibition and an offence) and the seat asks both.
8. **Independent deadlines need parallel branches.**
   In regulative rules on the main build, a `WITHIN` under `HENCE` counts from the previous act; the two instalments of s 78(1) and the employer and employee duties of s 87A(4) and s 88A(6) are `RAND` branches.
9. **Paragraph 1 of the Notification and paragraph 3(1) disagree on the start.**
   Paragraph 1 says the Notification comes into operation on 1 April 2019; the consolidated paragraph 3(1) applies to a retrenchment notice given on or after 1 November 2021.
   Both are encoded; paragraph 3(1) decides the duty.
10. **The Notification states no penalty.**
    Paragraphs 3 to 5 say what the employer must give, when and in what form; none says what follows from not giving it.
    This part encodes no penalty rule for the Notification.
11. **Reviewer's points left as they are.**
    The points in F1 (the last day of the 4 weeks of s 82), F3, F4, F8 (s 80(3), the seat's "how much"), F10 and F21 to F24 are recorded with the line "reviewer expected a different answer; open question".

## What the main binary does not accept

Measured on l4-main-109; the first two were also run on l4-main-108 with the same result.

- **An `#ASSERT` on a regulative value.**
  `#ASSERT `the duty` EQUALS FULFILLED` gives `eval/unsupported-equality`: "Trying to check equality on types that do not support it" (loud).
  Every regulative rule is therefore run with `#TRACE` and its outcome read by eye (the table above), and the same duty is encoded as a decision function over the facts, which is asserted.
- **`(`WAIT UNTIL` n)` in a `#TRACE`.**
  `check/unknown-identifier`: "I could not find a definition for the identifier `WAIT UNTIL`" (loud).
  A missed deadline is shown by a late act instead.
- `min` and `max` over `DATE` (multiple definitions); an infix `APPEND`; `length` (use `count`); partial application; a lambda that reads a field; `IF NOT x AND y` (silent, see above); a section-level `GIVEN` shared across rules; `REFUSE`; `BECAUSE` outside `LEST BREACH`.
  All loud except the `NOT` precedence.
- The traces of `ea2-duties.l4` were compared by eye between the two builds (every outcome listed on each, side by side): no difference.
  `check.sh` does not compare traces, so this comparison is by hand.

## Dependencies

- `ea-core.l4` and `ea-definitions.l4` (the keel's, copied read-only).
- `sgia-interpretation-time.l4`: the Interpretation Act module, copied unchanged; the copy carries a 3-line header.
  Commons path `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4`, blob fe60ab2c1f2326a5b061e163761bd63e4f47e12a, Commons main d468311a6.
  Used by s 78(1), s 95A(2) and the duties.
- `prelude` and `daydate` (the l4 libraries): `daydate` for `Date day month year`, `Weekday of`, `add months`, and `date PLUS n` / `date MINUS date`.

## Unstable dialect

No second encoding: the dated tiers (ss 76(2) to (2B), 84(1), 84A(1)) are ordinary `Date` comparisons on main, and no shape in this range needs the unstable dialect.

## What `check.sh` prints

Run on 2026-11-05 with `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` in the deposit folder; the shell reported `exit 0`.  The script printed exactly this:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ea-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
ea-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
ea2-cases-seat.l4                              0       606       0        0         0 |      0       606       0        0  same
ea2-duties.l4                                  0         9       0        0         0 |      0         9       0        0  same
ea2-notification.l4                            0         0       0        0         0 |      0         0       0        0  same
ea2-part-10-holiday-annual.l4                  0         0       0        0         0 |      0         0       0        0  same
ea2-part-10-sick.l4                            0         0       0        0         0 |      0         0       0        0  same
ea2-part-12-records.l4                         0         0       0        0         0 |      0         0       0        0  same
ea2-part-12-returns.l4                         0         0       0        0         0 |      0         0       0        0  same
ea2-part-13.l4                                 0         0       0        0         0 |      0         0       0        0  same
ea2-part-14.l4                                 0         0       0        0         0 |      0         0       0        0  same
ea2-part-6a-8.l4                               0         0       0        0         0 |      0         0       0        0  same
ea2-part-9a.l4                                 0         0       0        0         0 |      0         0       0        0  same
ea2-part-9b.l4                                 0         0       0        0         0 |      0         0       0        0  same
ea2-part-9c.l4                                 0         0       0        0         0 |      0         0       0        0  same
ea2-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
ea2-tests-duties.l4                            0        18       0        0         0 |      0        18       0        0  same
ea2-tests-notification.l4                      0        70       0        0         0 |      0        70       0        0  same
ea2-tests-part-10-holiday-annual.l4            0       131       0        0         0 |      0       131       0        0  same
ea2-tests-part-10-sick.l4                      0       105       0        0         0 |      0       105       0        0  same
ea2-tests-part-12-records.l4                   0        66       0        0         0 |      0        66       0        0  same
ea2-tests-part-12-returns.l4                   0        62       0        0         0 |      0        62       0        0  same
ea2-tests-part-13.l4                           0       109       0        0         0 |      0       109       0        0  same
ea2-tests-part-14.l4                           0        69       0        0         0 |      0        69       0        0  same
ea2-tests-part-6a-8.l4                         0        81       0        0         0 |      0        81       0        0  same
ea2-tests-part-9a.l4                           0       166       0        0         0 |      0       166       0        0  same
ea2-tests-part-9b.l4                           0       131       0        0         0 |      0       131       0        0  same
ea2-tests-part-9c.l4                           0        94       0        0         0 |      0        94       0        0  same
sgia-interpretation-time.l4                    0         0       0        0         0 |      0         0       0        0  same
TOTAL (29 modules)                             0      1717       0        0           |      0      1717       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Baseline replaced: the keel's `check.sh` run, recorded in `KEEL-NOTES.md` (line 12), printed 0 errors, 155 assertions satisfied, 0 failed, 0 refused, on 3 modules.
Those 3 modules were `ea-core.l4`, `ea-definitions.l4` and the keel's `ea-definitions-tests.l4` (`KEEL-NOTES.md` line 25, 155 assertions).
The keel's tests module is not distributed (`PLAN.md` line 119), so in this deposit `ea-core` and `ea-definitions` show 0 assertions; the 155 are not re-run here.
