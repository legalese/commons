# NOTES (wra3): Welfare Reform Act 2012 (United Kingdom), 2012 c. 5, part wra3

Status: written 2026-11-04 by the part agent `wra3` of run `iaw-wra3`.
Every count below was read off a run of the files in this folder on that date: the coverage counts from the audit script, and the assertion counts in the Files table from the `check.sh` run printed at the end (the builder parses that log, so the two cannot differ).
The text was not checked against the official text, and no domain expert has read this against the source.
Where a claim is a reading rather than a measurement, it says so.

## About the source

- The only source is `inputs/ukpga-2012-5.txt`, a plain-text rendering made by a converter script from legislation.gov.uk (point-in-time version 2026-07-01, as `inputs/KEEL-NOTES.md` line 9 says).
- It is not the official text, and nothing in this encoding is verified against the official text.
- It is a point-in-time version, so it carries amendments made after 2012: section 95 defines four Scottish disability payments by regulations of 2021, 2022, 2024 and 2025 (raw lines 1511-1519).
- My four ranges are raw lines 1344-1519 (Part 4, ss 77-95), 2475-2629 (Parts 6 and 7, ss 135-151), 3001-3049 (Schedule 4) and 3237-3959 (Schedules 9 to 14).
- The brief and the plan give the last range as ending at line 3960; that line does not exist (the file has 3959 lines, `wc -l` and `grep -c .` both give 3959), so the last row of the coverage table is 3957-3959.
- `inputs/PLAN.md` section 1 says a part does not import `wra-definitions`; the brief says to import both keel modules, and where the two differ the brief governs.
  Every layer-1 module of this part imports it, and it defines nothing.
- Peeked: nothing.

### Files

| file | what it holds | assertions satisfied (`check.sh`, your l4 column) |
| --- | --- | --- |
| wra3-pt4-s77-84.l4 and wra3-tests-pt4-s77-84.l4 | ss 77-84: the allowance, the two components, the ability questions, the required period condition, terminal illness, the age bar, the EU competence bar; the three-valued helpers `s 78(6) the conjunction of the results` and `s 78(6) the disjunction of the results` | 184 |
| wra3-pt4-s85-90.l4 and wra3-tests-pt4-s85-90.l4 | ss 85-90: care home, hospital, prison, claims and awards, information, the report to Parliament (with a regulative rule traced), the abolition of disability living allowance | 73 |
| wra3-pt4-s92.l4 and wra3-tests-pt4-s92.l4 | s 92(3): primary and secondary legislation | 8 |
| wra3-pt4-s95.l4 and wra3-tests-pt4-s95.l4 | s 95: the interpretation of Part 4 | 20 |
| wra3-pt6-misc.l4 and wra3-tests-pt6-misc.l4 | ss 135-146: Tell Us Once, child support, indicative calculations, fees, voluntary arrangements, standards of decision-making, jobcentres, child poverty (with a regulative rule, s 141, traced) | 79 |
| wra3-pt7-final.l4, wra3-sch10.l4 and wra3-tests-pt7-sch10.l4 | s 148 financial provision, s 150(3) the appointed day (seam 10), Schedule 10 paragraph 1(2) | 15 |
| wra3-sch4.l4 and wra3-tests-sch4.l4 | Schedule 4: the housing credit element of state pension credit | 36 |
| wra3-sch9.l4 and wra3-tests-sch9.l4 | Schedule 9: the six units that state a rule or a limb in their own words | 23 |
| wra3-sch11.l4 and wra3-tests-sch11.l4 | Schedule 11: the shared reading of consideration of revision before appeal (seam 8), and the purported appeal | 49 |
| wra3-sch12.l4 and wra3-tests-sch12.l4 | Schedule 12: the former appellate bodies and the decisions listed as open to supersession | 26 |
| wra3-sch13.l4 and wra3-tests-sch13.l4 | Schedule 13: the Commission and the Northern Ireland appointed day | 16 |
| wra3-seat.l4 and wra3-cases-seat.l4 | the seat layer: 69 questions, with 283 assertions in the case file | 283 |
| total | | 812 |

## Coverage (wra3)

One row per unit of my four ranges, each with exactly one disposition and the L4 name that encodes it.
A unit is what the text itself starts afresh: a heading, a section, a numbered or bracketed subsection, a quoted defined term, or a paragraph of an amendment schedule.
A lettered paragraph is part of its lead-in unless it was given its own row because its disposition differs (12 such splits, listed below).
Every one of the 1103 lines of the four ranges is non-blank (the whole file is), so 1103 lines are covered, each in exactly one row.

| disposition | rows | lines |
| --- | --- | --- |
| encoded | 125 | 225 |
| fork | 12 | 23 |
| inert | 440 | 852 |
| repealed or blank in this text | 3 | 3 |
| total | 580 | 1103 |

| inert, by reason | rows | lines |
| --- | --- | --- |
| 1 not operative (headings, signposts) | 127 | 131 |
| 2 machinery (amendments of other Acts, repeals, regulation-making powers, commencement, short title, procedure) | 313 | 721 |
| 3 text shown repealed or blank | 0 | 0 |

No row is `inert` for reason 3: the three rows where the text shows a blank have the disposition `repealed or blank in this text`, which the brief lists beside `inert`.
Those three rows are raw line 3038 (a line of dots where a paragraph of Schedule 4 is omitted from this rendering) and raw lines 3355 and 3356 (Schedule 9 paragraphs 49 and 50, where the lead-in is printed and the inserted table row and abbreviation are missing).

**Audit counts.**

The segmenter counted 568 units in the 1103 lines before any disposition was assigned.
The audit then forced 12 splits, so the table has 580 rows after the audit; the splits are at raw lines 1404, 1405, 1417, 1418, 1419, 3338, 3347, 3349, 3404, 3428, 3437, 3471.
The audit script checks six things, and found 0 problems on the final run: every non-blank line is in exactly one row; every disposition key is the first line of a unit and is mapped once; no row is without a disposition; every `encoded` or `fork` row names at least one function or type; every name prefix resolves to a definition in a `wra3-*.l4` module of this folder (the names in the last column were resolved by that script, so a renamed function breaks the audit instead of drifting); and a row that is not `encoded` or `fork` names nothing.
The script is kept in the run's work directory, not in the deposit.

### Why a unit is `inert` (every inert row, grouped by the reason the row gives)

| reason | rows | the reason as the rows state it |
| --- | --- | --- |
| 1 | 76 | 1: heading |
| 1 | 39 | 1: section heading (the section is covered by its own rows) |
| 1 | 5 | 1: heading of an inserted section |
| 1 | 2 | 1: a signpost ("See sections 80 and 81"); it creates no rule of its own, and ss 80 and 81 are encoded |
| 1 | 2 | 1: introductory words ("In this section—") of the definitions |
| 1 | 1 | 1: introductory words ("In this Part—") of the definitions; each definition has its own row |
| 1 | 1 | 1: introductory words ("In this paragraph—") of the definitions |
| 1 | 1 | 1: lead-in words ("In subsection (1)—"); paragraphs (a) to (c) have their own rows |
| 2 | 73 | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |
| 2 | 59 | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 2 | 54 | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 2 | 43 | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |
| 2 | 7 | 2: regulation-making power |
| 2 | 7 | 2: regulation-making power and its procedure |
| 2 | 7 | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |
| 2 | 4 | 2: extent |
| 2 | 1 | 2: a duty to make regulations (their content, the required period condition, is s 81 and is encoded there) |
| 2 | 1 | 2: amendment lead-in |
| 2 | 1 | 2: amendment lead-in (Child Maintenance and Other Payments Act 2008 Schedule 5) |
| 2 | 1 | 2: amendment lead-in (Child Maintenance and Other Payments Act 2008 section 6) |
| 2 | 1 | 2: amendment lead-in (Child Poverty Act 2010 section 9) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991 Schedule 4C) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991 section 17) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991 section 43) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991 section 9) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991) |
| 2 | 1 | 2: amendment lead-in (Child Support Act 1991, new section 9A) |
| 2 | 1 | 2: amendment lead-in (Child Support, Pensions and Social Security Act 2000 Schedule 7 paragraph 4) |
| 2 | 1 | 2: amendment lead-in (Employment and Training Act 1973, new section 2A) |
| 2 | 1 | 2: amendment lead-in (Housing Act 1996 section 122) |
| 2 | 1 | 2: amendment lead-in (Insolvency Act 1986 section 382) |
| 2 | 1 | 2: amendment lead-in (Registration Service Act 1953) |
| 2 | 1 | 2: amendment lead-in (Social Security Act 1998 section 10) |
| 2 | 1 | 2: amendment lead-in (Social Security Administration Act 1992 section 122F) |
| 2 | 1 | 2: amendment lead-in (Social Security Administration Act 1992) |
| 2 | 1 | 2: amendment lead-in (State Pension Credit Act 2002 section 17) |
| 2 | 1 | 2: amendment lead-in (State Pension Credit Act 2002 section 7) |
| 2 | 1 | 2: amendment lead-in (State Pension Credit Act 2002) |
| 2 | 1 | 2: amendment lead-in (new section 3A) |
| 2 | 1 | 2: amendment lead-in (new sub-paragraph (3)) |
| 2 | 1 | 2: amendment lead-in (new sub-paragraph (7)) |
| 2 | 1 | 2: amendment lead-in (new subsection (5)) |
| 2 | 1 | 2: amendment lead-in (new subsection (6)) |
| 2 | 1 | 2: amendment lead-in (new subsection (7)) |
| 2 | 1 | 2: amendment lead-in and a substitution of words in CSA 7(3) |
| 2 | 1 | 2: amendment lead-in and repeal of words in CSA 4(2) |
| 2 | 1 | 2: amendment of State Pension Credit Act 2002 section 12(2)(b) (words inserted) |
| 2 | 1 | 2: amendment of a section heading |
| 2 | 1 | 2: amendment of section 122(1) (words inserted) |
| 2 | 1 | 2: amendment of section 122F(3)(a) (words inserted) |
| 2 | 1 | 2: amendment of section 122F(4) (words inserted) |
| 2 | 1 | 2: amendment of section 5(6) of the Social Security Administration Act 1992 (words inserted) |
| 2 | 1 | 2: amendment of section 69(1)(a) of the Child Support, Pensions and Social Security Act 2000 (words inserted) |
| 2 | 1 | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(i) |
| 2 | 1 | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(ii) |
| 2 | 1 | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(b) |
| 2 | 1 | 2: amendment of wording in the Child Poverty Act 2010 section 9(8) |
| 2 | 1 | 2: amends a section heading in the Insolvency Act 1986 |
| 2 | 1 | 2: amends the regulation-making power in section 6(2) of the Child Maintenance and Other Payments Act 2008 (fees); paragraph (h) is itself a power to make regulations |
| 2 | 1 | 2: gives effect to Schedule 10 (transitional); Schedule 10 has its own rows |
| 2 | 1 | 2: introduces amendments of other Acts (Schedule 9); the amendments have their own rows |
| 2 | 1 | 2: procedure for an order (annulment by resolution) |
| 2 | 1 | 2: regulation-making power (power to specify by description); the description is an input of s 85(5) |
| 2 | 1 | 2: regulation-making power (regulations under section 93 may in particular make provision ...) |
| 2 | 1 | 2: regulation-making power (transitional) |
| 2 | 1 | 2: regulation-making power (what is a good reason) |
| 2 | 1 | 2: regulation-making power (what is to be taken into account) |
| 2 | 1 | 2: repeal in the State Pension Credit Act 2002 Schedule 2 |
| 2 | 1 | 2: repeal of section 81 of the Social Security Act 1998 |
| 2 | 1 | 2: short title |
| 2 | 1 | 2: signpost to Schedule 13 (establishing a body); Schedule 13 has its own rows |
| 2 | 1 | 2: signpost to Schedule 14 (repeals); Schedule 14 has its own rows |
| 2 | 1 | 2: the Act's own commencement (on the day it is passed) |
| 2 | 1 | 2: the Act's own commencement (two months after the day it is passed) |
| 2 | 1 | 2: the Act's own commencement (what an order under (3) may do) |

Each inert row is in the table below with its raw lines and its reason number; the same list, compact, by raw line:

- reason 1, Part 4 (ss 77-95) (28 rows): 1344, 1345, 1346, 1354, 1365-1367, 1369, 1382-1384, 1387, 1409, 1416, 1423, 1424, 1436, 1442, 1447, 1459, 1465, 1467, 1468, 1473, 1477, 1478, 1480, 1482, 1490, 1493, 1509, 1510
- reason 1, Parts 6 and 7 (ss 135-151) (27 rows): 2475, 2476, 2477, 2479, 2491, 2492, 2499, 2514, 2516, 2523, 2529, 2535, 2543, 2547, 2548, 2550, 2551, 2553, 2560, 2561, 2563, 2579, 2580, 2582, 2587, 2599, 2628
- reason 1, Schedule 4 (8 rows): 3001, 3002, 3003, 3014, 3034, 3035, 3044, 3048
- reason 1, Schedules 9 to 14 (64 rows): 3237, 3238, 3241, 3243, 3255, 3310, 3312, 3318, 3340, 3344, 3353, 3357, 3358, 3361, 3367, 3377, 3388, 3393, 3394, 3418, 3443, 3457, 3473, 3493, 3494, 3501, 3509, 3514, 3517, 3525, 3528, 3529, 3532, 3533, 3545, 3548, 3562, 3565, 3566, 3574, 3587, 3594, 3596, 3598, 3602, 3604, 3611, 3613, 3641, 3657, 3658, 3869, 3884, 3885, 3893, 3894, 3905, 3910, 3917, 3924, 3925, 3931, 3938, 3956
- reason 2, Part 4 (ss 77-95) (18 rows): 1393, 1394-1397, 1398-1401, 1404, 1405, 1457, 1481, 1483, 1484-1486, 1491, 1492, 1494, 1495-1497, 1498-1500, 1501, 1502, 1503-1507, 1508
- reason 2, Parts 6 and 7 (ss 135-151) (30 rows): 2478, 2493, 2497, 2500, 2501-2503, 2507-2509, 2515, 2524, 2530-2534, 2536, 2544, 2546, 2549, 2552, 2559, 2562, 2564, 2565-2567, 2568-2571, 2572-2576, 2577-2578, 2581, 2588, 2589-2596, 2597, 2598, 2600-2606, 2607-2618, 2620-2627, 2629
- reason 2, Schedule 4 (19 rows): 3004, 3013, 3022-3026, 3027, 3028, 3029, 3030, 3031, 3033, 3036, 3037, 3039, 3040, 3041, 3042, 3045, 3046, 3047, 3049
- reason 2, Schedules 9 to 14 (246 rows): 3239-3240, 3242, 3244, 3245-3246, 3247, 3248, 3249, 3253-3254, 3256, 3257, 3258-3261, 3262-3263, 3264-3265, 3266-3267, 3268, 3270-3271, 3272, 3273, 3274-3275, 3276, 3277-3280, 3281-3282, 3283-3284, 3285, 3286, 3287, 3288-3289, 3290-3292, 3293, 3294-3295, 3296-3298, 3299, 3300, 3301-3302, 3303, 3304, 3305, 3308, 3309, 3311, 3313, 3314, 3315-3317, 3319, 3320-3322, 3323-3326, 3327, 3328-3331, 3332-3334, 3335-3337, 3341-3343, 3345, 3346, 3354, 3359, 3362-3365, 3366, 3368-3375, 3376, 3378-3380, 3381-3387, 3389-3392, 3395, 3396, 3397, 3403, 3405, 3406, 3407, 3408-3410, 3411, 3412-3417, 3419, 3420, 3421, 3427, 3429, 3430, 3436, 3438, 3439-3441, 3442, 3444, 3445, 3446, 3452, 3453, 3454, 3455, 3456, 3458, 3459, 3460-3461, 3462, 3468-3470, 3472, 3474, 3475, 3476, 3477, 3483, 3484, 3485, 3486-3491, 3492, 3495, 3496, 3500, 3504, 3507, 3510, 3513, 3518, 3524, 3530, 3531, 3535, 3536, 3537-3539, 3540, 3541-3544, 3546, 3547, 3549, 3550-3554, 3555-3558, 3559, 3560, 3561, 3563, 3564, 3567-3572, 3573, 3575, 3576, 3577, 3578-3582, 3583-3585, 3586, 3588-3592, 3593, 3595, 3597, 3599-3601, 3603, 3605-3607, 3608-3610, 3612, 3614, 3615, 3616-3618, 3619-3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630, 3632, 3634, 3636, 3637, 3638, 3639, 3640, 3642-3644, 3645-3647, 3648-3650, 3651-3653, 3654-3656, 3659-3661, 3662-3664, 3665-3667, 3668-3671, 3672-3674, 3675-3677, 3678-3681, 3682-3687, 3688-3692, 3693-3696, 3697-3699, 3700-3702, 3703-3708, 3709-3714, 3715-3717, 3718-3722, 3723-3725, 3726-3730, 3731-3733, 3734-3736, 3737-3739, 3740-3742, 3743-3753, 3754-3757, 3758-3761, 3762-3764, 3765-3768, 3769-3771, 3772-3774, 3775-3781, 3782-3784, 3785-3787, 3788-3792, 3793-3797, 3798-3801, 3802-3805, 3806-3808, 3809-3811, 3812-3814, 3815-3817, 3818-3820, 3821-3823, 3824-3826, 3827-3829, 3830-3838, 3839-3841, 3842-3844, 3845, 3846-3850, 3851-3853, 3854-3856, 3857-3862, 3863-3868, 3870-3875, 3876-3879, 3880-3883, 3886-3889, 3890-3892, 3895-3897, 3898-3901, 3902-3904, 3906-3909, 3911-3913, 3914-3916, 3918-3920, 3921-3923, 3926-3930, 3932-3934, 3935-3937, 3939-3941, 3942-3945, 3946-3955, 3957-3959

A row that carries a note in the coverage table below (for example the Schedule 9 amendments, or Schedule 14) gives its reason there in full.
A judgement, assumed and not ruled: Schedule 9 adds "personal independence payment" to many lists and cross-references in other Acts.
Where the inserted words are a free-standing paragraph of a list that another part's Schedule also adds a paragraph to, or state a rule in their own words, the unit is encoded (SSCBA 64(1A), SSAA 73(6) and 187(1)(ad), SSA1998 Sch 3 para 3(h) and (i), SSFA 6A(1)(ca) twice, SSFA 10(3)(be)).
The rest (SSAA 5(2), 71(11), 121DA, 122B, 122C, 124, 125, 150, 159 to 165, 170, 179, 180, 182B, 184, 191 and Schedule 7, IAA 115, ITEPA 2003) splice words into a sentence or a list whose lead-in is not printed, and are inert under reason 2 (amendments of other Acts).
If a lawyer wants any of them encoded, each is a list-limb function of the same shape as `sch 9 para 31 SSAA 187(1)(ad) the benefit is within the limb`.

### The table

| Lines | Provision | Text begins | Disposition | Reason / fork / note | L4 name (module) |
| --- | --- | --- | --- | --- | --- |
| 1344 | heading | Part 4 — Personal independence payment | inert | 1: heading |  |
| 1345 | heading | Personal independence payment | inert | 1: heading |  |
| 1346 | s 77 heading | 77 Personal independence payment | inert | 1: section heading (the section is covered by its own rows) |  |
| 1347 | s 77(1) | (1) An allowance known as personal independence payment is p | encoded |  | `s 77(1) the allowance known as personal independence payment` (wra3-pt4-s77-84.l4) |
| 1348-1351 | s 77(2) | (2) A person's entitlement to personal independence payment  | encoded |  | `s 77(2) the components the person's entitlement is an entitlement to` (wra3-pt4-s77-84.l4) |
| 1352 | s 77(3) | (3) A person is not entitled to personal independence paymen | encoded |  | `s 77(3) the person is not barred for want of the prescribed residence and presence conditions` (wra3-pt4-s77-84.l4) |
| 1353 | s 77(4) | (4) A person is not entitled to personal independence paymen | encoded |  | `s 77(4) the person is not barred by being entitled to a Scottish disability payment` (wra3-pt4-s77-84.l4); `s 95 Scottish disability assistance` (wra3-pt4-s95.l4) |
| 1354 | s 78 heading | 78 Daily living component | inert | 1: section heading (the section is covered by its own rows) |  |
| 1355-1357 | s 78(1) | (1) A person is entitled to the daily living component at th | encoded |  | `s 78(1) the person is entitled to the daily living component at the standard rate` (wra3-pt4-s77-84.l4) |
| 1358-1360 | s 78(2) | (2) A person is entitled to the daily living component at th | encoded |  | `s 78(2) the person is entitled to the daily living component at the enhanced rate` (wra3-pt4-s77-84.l4) |
| 1361-1363 | s 78(3) | (3) In this section, in relation to the daily living compone | encoded |  | `s 78(3) the weekly rate of the daily living component at the rate` (wra3-pt4-s77-84.l4); `s 78(3)(a) the weekly rate of the daily living component at the standard rate` (wra3-pt4-s77-84.l4); `s 78(3)(b) the weekly rate of the daily living component at the enhanced rate` (wra3-pt4-s77-84.l4) |
| 1364 | s 78(4) | (4) In this Part “daily living activities“ means such activi | encoded |  | `s 78(4) the activity is a daily living activity` (wra3-pt4-s77-84.l4) |
| 1365-1367 | s 78(5) | (5) See sections 80 and 81 for provision about determining— | inert | 1: a signpost ("See sections 80 and 81"); it creates no rule of its own, and ss 80 and 81 are encoded |  |
| 1368 | s 78(6) | (6) This section is subject to the provisions of this Part,  | encoded |  | `s 78(6) the conjunction of the results` (wra3-pt4-s77-84.l4); `s 78(6) the disjunction of the results` (wra3-pt4-s77-84.l4); `s 78(6) the person is entitled to the daily living component, subject to the other provisions of Part 4 relating to entitlement` (wra3-pt4-s77-84.l4) |
| 1369 | s 79 heading | 79 Mobility component | inert | 1: section heading (the section is covered by its own rows) |  |
| 1370-1373 | s 79(1) | (1) A person is entitled to the mobility component at the st | encoded |  | `s 79(1) the person is entitled to the mobility component at the standard rate` (wra3-pt4-s77-84.l4); `s 79(1)(a) the person is of or over the age prescribed` (wra3-pt4-s77-84.l4) |
| 1374-1377 | s 79(2) | (2) A person is entitled to the mobility component at the en | encoded |  | `s 79(2) the person is entitled to the mobility component at the enhanced rate` (wra3-pt4-s77-84.l4); `s 79(2)(a) the person is of or over the age prescribed` (wra3-pt4-s77-84.l4) |
| 1378-1380 | s 79(3) | (3) In this section, in relation to the mobility component— | encoded |  | `s 79(3) the weekly rate of the mobility component at the rate` (wra3-pt4-s77-84.l4); `s 79(3)(a) the weekly rate of the mobility component at the standard rate` (wra3-pt4-s77-84.l4); `s 79(3)(b) the weekly rate of the mobility component at the enhanced rate` (wra3-pt4-s77-84.l4) |
| 1381 | s 79(4) | (4) In this Part “mobility activities” means such activities | encoded |  | `s 79(4) the activity is a mobility activity` (wra3-pt4-s77-84.l4) |
| 1382-1384 | s 79(5) | (5) See sections 80 and 81 for provision about determining— | inert | 1: a signpost ("See sections 80 and 81"); it creates no rule of its own, and ss 80 and 81 are encoded |  |
| 1385 | s 79(6) | (6) This section is subject to the provisions of this Part,  | encoded |  | `s 79(6) the person is entitled to the mobility component, subject to the other provisions of Part 4 relating to entitlement` (wra3-pt4-s77-84.l4) |
| 1386 | s 79(7) | (7) Regulations may provide that a person is not entitled to | encoded |  | `s 79(7) the person is not barred by regulations about unlikelihood of benefiting from enhanced mobility` (wra3-pt4-s77-84.l4) |
| 1387 | s 80 heading | 80 Ability to carry out daily living activities or mobility  | inert | 1: section heading (the section is covered by its own rows) |  |
| 1388-1392 | s 80(1) | (1) For the purposes of this Part, the following questions a | encoded |  | `s 80(1) determinations made in accordance with regulations` (wra3-pt4-s77-84.l4); `s 80(1) question about the person's ability` (wra3-pt4-s77-84.l4); `s 80(1) the question as determined in accordance with regulations` (wra3-pt4-s77-84.l4) |
| 1393 | s 80(2) | (2) Regulations must make provision for determining, for the | inert | 2: a duty to make regulations (their content, the required period condition, is s 81 and is encoded there) |  |
| 1394-1397 | s 80(3) | (3) Regulations under this section— | inert | 2: regulation-making power |  |
| 1398-1401 | s 80(4) | (4) The regulations may, in particular, make provision— | inert | 2: regulation-making power |  |
| 1402-1403 | s 80(5) | (5) The regulations may include provision— | encoded | lead-in and paragraph (a) | `s 80(5)(a) a negative determination is treated as made against the person` (wra3-pt4-s77-84.l4) |
| 1404 | s 80(5)(b) | (b) about what does or does not constitute a good reason for | inert | 2: regulation-making power (what is a good reason) |  |
| 1405 | s 80(5)(c) | (c) about matters which are, or are not, to be taken into ac | inert | 2: regulation-making power (what is to be taken into account) |  |
| 1406-1408 | s 80(6) | (6) In subsection (5)(a) a “negative determination” means a  | encoded |  | `s 80(6) determination about the requirements for a component` (wra3-pt4-s77-84.l4); `s 80(6) the determination is a negative determination` (wra3-pt4-s77-84.l4) |
| 1409 | s 81 heading | 81 Required period condition: further provision | inert | 1: section heading (the section is covered by its own rows) |  |
| 1410-1412 | s 81(1) | (1) Regulations under section 80(2) must provide for the que | fork | F-81-1 | `s 81(1) the person meets the required period condition on the usual test` (wra3-pt4-s77-84.l4); `s 81(1)(a) the time is within the previous 3 months` (wra3-pt4-s77-84.l4); `s 81(1)(b) the time is within the next 9 months` (wra3-pt4-s77-84.l4) |
| 1413-1415 | s 81(2) | (2) In subsection (1) “the relevant ability” means— | encoded |  | `s 81(2) the relevant ability` (wra3-pt4-s77-84.l4) |
| 1416 | s 81(3) | (3) In subsection (1)— | inert | 1: lead-in words ("In subsection (1)—"); paragraphs (a) to (c) have their own rows |  |
| 1417 | s 81(3)(a) | (a) “assessed” means assessed in accordance with regulations | encoded |  | `s 81(3)(a) the assessment is an assessment for the purposes of section 81(1)` (wra3-pt4-s77-84.l4) |
| 1418 | s 81(3)(b) | (b) “the previous 3 months” means the 3 months ending with t | fork | F-81-2 | `s 81(3) the last day of the months beginning with the day` (wra3-pt4-s77-84.l4); `s 81(3)(b) the previous 3 months ending with the prescribed date` (wra3-pt4-s77-84.l4) |
| 1419 | s 81(3)(c) | (c) “the next 9 months” means the 9 months beginning with th | fork | F-81-2 | `s 81(3) the last day of the months beginning with the day` (wra3-pt4-s77-84.l4); `s 81(3)(c) the next 9 months beginning with the day after the prescribed date` (wra3-pt4-s77-84.l4) |
| 1420-1422 | s 81(4) | (4) Regulations under section 80(2) may provide that in pres | encoded |  | `s 81(4) the person meets the required period condition` (wra3-pt4-s77-84.l4) |
| 1423 | heading | Entitlement and payability: further provision | inert | 1: heading |  |
| 1424 | s 82 heading | 82 Terminal illness | inert | 1: section heading (the section is covered by its own rows) |  |
| 1425-1427 | s 82(1) | (1) This section applies to a person who— | encoded |  | `s 82(1) this section applies to the person` (wra3-pt4-s77-84.l4) |
| 1428 | s 82(2) | (2) A person to whom this section applies is entitled to the | encoded |  | `s 82(2) section 78(1) and (2) apply to the person` (wra3-pt4-s77-84.l4); `s 82(2) the person is entitled to the daily living component at the enhanced rate, section 82 displacing section 78(2)` (wra3-pt4-s77-84.l4); `s 82(2) the person is entitled to the daily living component at the enhanced rate` (wra3-pt4-s77-84.l4); `s 82(2) the result under section 78(1), section 82 displacing section 78(1)` (wra3-pt4-s77-84.l4) |
| 1429 | s 82(3) | (3) Section 79(1)(c) and (2)(c) (required period condition f | encoded |  | `s 82(3) the required period condition limb of section 79(1)(c) and (2)(c), as it stands for the person` (wra3-pt4-s77-84.l4); `s 82(3) the required period condition of section 79(1)(c) and (2)(c) applies to the person` (wra3-pt4-s77-84.l4) |
| 1430 | s 82(4) | (4) For the purposes of this section a person is “terminally | fork | F-82 | `s 82(4) the last day of the 12 months beginning with the time` (wra3-pt4-s77-84.l4); `s 82(4) the person is terminally ill at the time` (wra3-pt4-s77-84.l4) |
| 1431-1434 | s 82(5) | (5) For the purposes of this section, where— | encoded |  | `s 82(5) the person on whose behalf the claim purports to be made is regarded as making the claim` (wra3-pt4-s77-84.l4) |
| 1435 | s 82(6) | (6) In subsection (2) “the enhanced rate” has the meaning gi | encoded |  | `s 82(6) the enhanced rate for the purposes of section 82(2)` (wra3-pt4-s77-84.l4) |
| 1436 | s 83 heading | 83 Persons of pensionable age | inert | 1: section heading (the section is covered by its own rows) |  |
| 1437 | s 83(1) | (1) A person is not entitled to the daily living component o | encoded |  | `s 83(1) the person is not barred by having reached the relevant age` (wra3-pt4-s77-84.l4) |
| 1438-1440 | s 83(2) | (2) In subsection (1) “the relevant age” means— | fork | F-83 | `s 83(2) the person has reached the relevant age` (wra3-pt4-s77-84.l4) |
| 1441 | s 83(3) | (3) Subsection (1) is subject to such exceptions as may be p | encoded | the exceptions regulations may provide are the input "regulations provide an exception ..." of s 83(1); the power itself is not coded | `s 83(1) the person is not barred by having reached the relevant age` (wra3-pt4-s77-84.l4) |
| 1442 | s 84 heading | 84 No entitlement to daily living component where UK is not  | inert | 1: section heading (the section is covered by its own rows) |  |
| 1443 | s 84(1) | (1) A person to whom a relevant EU Regulation applies is not | encoded |  | `s 84(1) the person is not barred from the daily living component by the United Kingdom not being the competent state` (wra3-pt4-s77-84.l4) |
| 1444-1446 | s 84(2) | (2) Each of the following is a “relevant EU Regulation” for  | encoded |  | `s 84(2) instrument` (wra3-pt4-s77-84.l4); `s 84(2) the instrument is a relevant EU Regulation` (wra3-pt4-s77-84.l4) |
| 1447 | s 85 heading | 85 Care home residents | inert | 1: section heading (the section is covered by its own rows) |  |
| 1448 | s 85(1) | (1) Regulations may provide that no amount in respect of per | encoded |  | `s 85(1) the amount attributable to the daily living component is not barred as payable` (wra3-pt4-s85-90.l4) |
| 1449 | s 85(2) | (2) The condition is that the person is a resident of a care | encoded |  | `s 85(2) the person meets the condition` (wra3-pt4-s85-90.l4) |
| 1450 | s 85(3) | (3) In this section “care home” means an establishment that  | encoded |  | `s 85(3) the establishment is a care home` (wra3-pt4-s85-90.l4) |
| 1451-1455 | s 85(4) | (4) The following are “qualifying services“ for the purposes | encoded |  | `s 85(4) service` (wra3-pt4-s85-90.l4); `s 85(4) the service is a qualifying service` (wra3-pt4-s85-90.l4) |
| 1456 | s 85(5) | (5) The reference in subsection (2) to a “specified enactmen | encoded |  | `s 85(5) the enactment is a specified enactment` (wra3-pt4-s85-90.l4) |
| 1457 | s 85(6) | (6) The power to specify an enactment for the purposes of su | inert | 2: regulation-making power (power to specify by description); the description is an input of s 85(5) |  |
| 1458 | s 85(7) | (7) In this section “enactment” includes an enactment compri | encoded |  | `s 85(7) provision` (wra3-pt4-s85-90.l4); `s 85(7) the provision is an enactment` (wra3-pt4-s85-90.l4) |
| 1459 | s 86 heading | 86 Hospital in-patients | inert | 1: section heading (the section is covered by its own rows) |  |
| 1460-1462 | s 86(1) | (1) Regulations may provide as mentioned in either or both o | encoded |  | `s 86(1) the amount attributable to the component is not barred as payable` (wra3-pt4-s85-90.l4) |
| 1463 | s 86(2) | (2) The condition is that the person is undergoing medical o | encoded |  | `s 86(2) the person meets the condition` (wra3-pt4-s85-90.l4) |
| 1464 | s 86(3) | (3) For the purposes of subsection (2) the question of wheth | encoded |  | `s 86(3) whether any of the costs are borne out of public funds, as determined in accordance with the regulations` (wra3-pt4-s85-90.l4) |
| 1465 | s 87 heading | 87 Prisoners and detainees | inert | 1: section heading (the section is covered by its own rows) |  |
| 1466 | s 87 | Except to the extent that regulations provide otherwise, no  | encoded |  | `s 87 the amount is not barred as payable by imprisonment or detention` (wra3-pt4-s85-90.l4) |
| 1467 | heading | Supplementary | inert | 1: heading |  |
| 1468 | s 88 heading | 88 Claims, awards and information | inert | 1: section heading (the section is covered by its own rows) |  |
| 1469 | s 88(1) | (1) A person is not entitled to personal independence paymen | encoded |  | `s 88(1) the person is not barred for a period by its beginning before the claim` (wra3-pt4-s85-90.l4) |
| 1470 | s 88(2) | (2) An award of personal independence payment is to be for a | encoded |  | `s 88(2) the award is required to be for a fixed term` (wra3-pt4-s85-90.l4) |
| 1471 | s 88(3) | (3) In deciding whether a fixed term award would be inapprop | encoded |  | `s 88(3) the duty to have regard to the Secretary of State's guidance is discharged` (wra3-pt4-s85-90.l4) |
| 1472 | s 88(4) | (4) Information supplied under this Part is to be taken for  | encoded |  | `s 88(4) the information is information relating to social security` (wra3-pt4-s85-90.l4) |
| 1473 | s 89 heading | 89 Report to Parliament | inert | 1: section heading (the section is covered by its own rows) |  |
| 1474-1476 | s 89 | The Secretary of State must lay before Parliament an indepen | encoded |  | `s 89 act` (wra3-pt4-s85-90.l4); `s 89 the duty to lay the report within the period` (wra3-pt4-s85-90.l4); `s 89(a) the last day of the 2 years beginning with the date the first regulations come into force` (wra3-pt4-s85-90.l4); `s 89(a) the report was laid within the 2 years` (wra3-pt4-s85-90.l4); `s 89(b) the last day of the 4 years beginning with the date the first regulations come into force` (wra3-pt4-s85-90.l4); `s 89(b) the report was laid within the 4 years` (wra3-pt4-s85-90.l4) |
| 1477 | heading | General | inert | 1: heading |  |
| 1478 | s 90 heading | 90 Abolition of disability living allowance | inert | 1: section heading (the section is covered by its own rows) |  |
| 1479 | s 90 | Sections 71 to 76 of the Social Security Contributions and B | encoded |  | `s 90 the benefit is abolished by the repeal of sections 71 to 76 of the Contributions and Benefits Act` (wra3-pt4-s85-90.l4) |
| 1480 | s 91 heading | 91 Amendments | inert | 1: section heading (the section is covered by its own rows) |  |
| 1481 | s 91 | Schedule 9 contains amendments relating to this Part. | inert | 2: introduces amendments of other Acts (Schedule 9); the amendments have their own rows |  |
| 1482 | s 92 heading | 92 Power to make supplementary and consequential provision | inert | 1: section heading (the section is covered by its own rows) |  |
| 1483 | s 92(1) | (1) Regulations may make such consequential, supplementary o | inert | 2: regulation-making power |  |
| 1484-1486 | s 92(2) | (2) Regulations under this section may— | inert | 2: regulation-making power |  |
| 1487-1489 | s 92(3) | (3) In this section— | encoded | the definitions that the power in (1) and (2) uses | `s 92(3) legislation` (wra3-pt4-s92.l4); `s 92(3)(a) the legislation is primary legislation` (wra3-pt4-s92.l4); `s 92(3)(b) the legislation is secondary legislation` (wra3-pt4-s92.l4) |
| 1490 | s 93 heading | 93 Transitional | inert | 1: section heading (the section is covered by its own rows) |  |
| 1491 | s 93(1) | (1) Regulations may make such provision as the Secretary of  | inert | 2: regulation-making power (transitional) |  |
| 1492 | s 93(2) | (2) Schedule 10 (transitional provision for introduction of  | inert | 2: gives effect to Schedule 10 (transitional); Schedule 10 has its own rows |  |
| 1493 | s 94 heading | 94 Regulations | inert | 1: section heading (the section is covered by its own rows) |  |
| 1494 | s 94(1) | (1) Regulations under this Part are to be made by the Secret | inert | 2: regulation-making power and its procedure |  |
| 1495-1497 | s 94(2) | (2) A power to make regulations under this Part may be exerc | inert | 2: regulation-making power and its procedure |  |
| 1498-1500 | s 94(3) | (3) Such a power includes— | inert | 2: regulation-making power and its procedure |  |
| 1501 | s 94(4) | (4) The power under subsection (2)(a) includes, in particula | inert | 2: regulation-making power and its procedure |  |
| 1502 | s 94(5) | (5) Regulations under this Part are to be made by statutory  | inert | 2: regulation-making power and its procedure |  |
| 1503-1507 | s 94(6) | (6) A statutory instrument containing (whether alone or with | inert | 2: regulation-making power and its procedure |  |
| 1508 | s 94(7) | (7) Any other statutory instrument containing regulations un | inert | 2: regulation-making power and its procedure |  |
| 1509 | s 95 heading | 95 Interpretation of Part 4 | inert | 1: section heading (the section is covered by its own rows) |  |
| 1510 | s 95 | In this Part— | inert | 1: introductory words ("In this Part—") of the definitions; each definition has its own row |  |
| 1511 | s 95 "adult disability payment" | “adult disability payment” means disability assistance given | encoded |  | `s 95 disability assistance given in accordance with` (wra3-pt4-s95.l4); `s 95 the disability assistance is the payment named` (wra3-pt4-s95.l4) |
| 1512 | s 95 "child disability payment" | “child disability payment” means disability assistance given | encoded |  | `s 95 disability assistance given in accordance with` (wra3-pt4-s95.l4); `s 95 the disability assistance is the payment named` (wra3-pt4-s95.l4) |
| 1513 | s 95 "daily living activities" | “daily living activities” has the meaning given by section 7 | encoded |  | `s 95 daily living activities has the meaning given by` (wra3-pt4-s95.l4) |
| 1514 | s 95 "daily living component" | “daily living component” means the daily living component of | encoded |  | `s 95 daily living component means the daily living component of personal independence payment` (wra3-pt4-s95.l4) |
| 1515 | s 95 "mobility activities" | “mobility activities” has the meaning given by section 79(4) | encoded |  | `s 95 mobility activities has the meaning given by` (wra3-pt4-s95.l4) |
| 1516 | s 95 "mobility component" | “mobility component” means the mobility component of persona | encoded |  | `s 95 mobility component means the mobility component of personal independence payment` (wra3-pt4-s95.l4) |
| 1517 | s 95 "pension age disability payment" | “pension age disability payment” means disability assistance | encoded |  | `s 95 disability assistance given in accordance with` (wra3-pt4-s95.l4); `s 95 the disability assistance is the payment named` (wra3-pt4-s95.l4) |
| 1518 | s 95 "prescribed" | “prescribed” means prescribed by regulations; | encoded |  | `s 95 the matter is prescribed` (wra3-pt4-s95.l4) |
| 1519 | s 95 "Scottish adult disability living allowance" | “Scottish adult disability living allowance” means disabilit | encoded |  | `s 95 disability assistance given in accordance with` (wra3-pt4-s95.l4); `s 95 the disability assistance is the payment named` (wra3-pt4-s95.l4) |
| 2475 | heading | Part 6 — Miscellaneous | inert | 1: heading |  |
| 2476 | heading | Tell Us Once | inert | 1: heading |  |
| 2477 | s 135 heading | 135 Functions of registration service | inert | 1: section heading (the section is covered by its own rows) |  |
| 2478 | s 135 | In the Registration Service Act 1953, after section 19 there | inert | 2: amendment lead-in (Registration Service Act 1953) |  |
| 2479 | RSA 19A heading (inserted) | 19A Functions relating to transmission of information to Sec | inert | 1: section heading (the section is covered by its own rows) |  |
| 2480-2483 | s 135 RSA 19A(1) | (1) The functions of a registrar of births and deaths, a sup | encoded |  | `s 135 RSA 19A(1) the functions of a registrar include the power to transmit and verify the information for the Secretary of State` (wra3-pt6-misc.l4) |
| 2484-2486 | s 135 RSA 19A(2) | (2) That service is a service operated by the Secretary of S | encoded |  | `s 135 RSA 19A(2) the arrangement is the service in subsection (2)` (wra3-pt6-misc.l4) |
| 2487 | s 135 RSA 19A(3) | (3) References in subsections (1) and (2) to the Secretary o | encoded |  | `s 135 RSA 19A(3) the person is within the references to the Secretary of State in subsections (1) and (2)` (wra3-pt6-misc.l4) |
| 2488-2490 | s 135 RSA 19A(4) | (4) This section does not authorise any disclosure which is  | encoded |  | `s 135 RSA 19A(4) the section authorises the disclosure` (wra3-pt6-misc.l4) |
| 2491 | heading | Child support maintenance | inert | 1: heading |  |
| 2492 | s 136 heading | 136 Supporting maintenance agreements | inert | 1: section heading (the section is covered by its own rows) |  |
| 2493 | s 136(1) | (1) In section 9 of the Child Support Act 1991 (maintenance  | inert | 2: amendment lead-in (Child Support Act 1991 section 9) |  |
| 2494-2496 | s 136(2A) | (2A) The Secretary of State may, with a view to reducing the | encoded |  | `s 136(1) CSA 9(2A)(a) the Secretary of State may take the step` (wra3-pt6-misc.l4); `s 136(1) CSA 9(2A)(b) the Secretary of State may invite the applicant to consider whether it is possible to make a maintenance agreement` (wra3-pt6-misc.l4) |
| 2497 | s 136(2) | (2) In Schedule 5 to the Child Maintenance and Other Payment | inert | 2: amendment lead-in (Child Maintenance and Other Payments Act 2008 Schedule 5) |  |
| 2498 | s 136(3) | (3) The Secretary of State may before accepting an applicati | encoded |  | `s 136(2) CMOPA Sch 5 para 3(3) the Secretary of State may invite the applicant to consider whether it is possible to make a maintenance agreement` (wra3-pt6-misc.l4) |
| 2499 | s 137 heading | 137 Collection of child support maintenance | inert | 1: section heading (the section is covered by its own rows) |  |
| 2500 | s 137(1) | (1) The Child Support Act 1991 is amended as follows. | inert | 2: amendment lead-in (Child Support Act 1991) |  |
| 2501-2503 | s 137(2) | (2) In section 4 (child support maintenance)— | inert | 2: amendment lead-in and repeal of words in CSA 4(2) |  |
| 2504-2506 | s 137(2A) | (2A) The Secretary of State may only make arrangements under | encoded |  | `s 137(2) CSA 4(2A) the Secretary of State may make arrangements under section 4(2)(a)` (wra3-pt6-misc.l4); `s 137(2) CSA 4(2A) the condition for arrangements under section 4(2)(a) is met` (wra3-pt6-misc.l4) |
| 2507-2509 | s 137(3) | (3) In section 7 (right of child in Scotland to apply for ca | inert | 2: amendment lead-in and a substitution of words in CSA 7(3) |  |
| 2510-2512 | s 137(3A) | (3A) The Secretary of State may only make arrangements under | encoded |  | `s 137(3) CSA 7(3A) the Secretary of State may make arrangements under section 7(3)(a)` (wra3-pt6-misc.l4); `s 137(3) CSA 7(3A) the condition for arrangements under section 7(3)(a) is met` (wra3-pt6-misc.l4) |
| 2513 | s 137(4) | (4) In section 29 (collection of child support maintenance), | encoded |  | `s 137(4) CSA 29(1) the Secretary of State may make the arrangement for collection, subject to sections 4(2A) and 7(3A)` (wra3-pt6-misc.l4); `s 137(4) arrangement for collection` (wra3-pt6-misc.l4) |
| 2514 | s 138 heading | 138 Indicative maintenance calculations | inert | 1: section heading (the section is covered by its own rows) |  |
| 2515 | s 138 | After section 9 of the Child Support Act 1991 there is inser | inert | 2: amendment lead-in (Child Support Act 1991, new section 9A) |  |
| 2516 | CSA 9A heading (inserted) | 9A Maintenance agreements: indicative calculations | inert | 1: section heading (the section is covered by its own rows) |  |
| 2517 | s 138 CSA 9A(1) | (1) A person with care or non-resident parent in relation to | encoded |  | `s 138 CSA 9A(1) the person may apply for an indicative calculation` (wra3-pt6-misc.l4); `s 138 role in relation to a qualifying child` (wra3-pt6-misc.l4) |
| 2518 | s 138 CSA 9A(2) | (2) A qualifying child who has attained the age of 12 years  | encoded |  | `s 138 CSA 9A(2) the child may apply for an indicative calculation with respect to themselves` (wra3-pt6-misc.l4) |
| 2519 | s 138 CSA 9A(3) | (3) An indicative calculation is a calculation of the amount | encoded |  | `s 138 CSA 9A(3) the calculation is an indicative calculation` (wra3-pt6-misc.l4) |
| 2520 | s 138 CSA 9A(4) | (4) An indicative calculation does not create any liability  | encoded |  | `s 138 CSA 9A(4) the calculation creates a liability to pay child support maintenance` (wra3-pt6-misc.l4) |
| 2521 | s 138 CSA 9A(5) | (5) The Secretary of State may limit the number of applicati | encoded |  | `s 138 CSA 9A(5) the application is not barred by a limit on the number of applications` (wra3-pt6-misc.l4) |
| 2522 | s 138 CSA 9A(6) | (6) Where a person who is alleged to be the parent of a chil | encoded |  | `s 138 CSA 9A(6) the Secretary of State is not barred from making the calculation on the assumption that the person is a parent` (wra3-pt6-misc.l4) |
| 2523 | s 139 heading | 139 Recovery of child support maintenance by deduction from  | inert | 1: section heading (the section is covered by its own rows) |  |
| 2524 | s 139 | In section 43 of the Child Support Act 1991 (as substituted  | inert | 2: amendment lead-in (Child Support Act 1991 section 43) |  |
| 2525 | s 139(1) | (1) The power of the Secretary of State to make regulations  | encoded |  | `s 139 CSA 43 the regulations power under section 5(1)(p) of the Social Security Administration Act 1992 may be exercised to secure the payment` (wra3-pt6-misc.l4); `s 139 payment` (wra3-pt6-misc.l4) |
| 2526-2528 | s 139(2) | (2) The reference in subsection (1) to the making of payment | encoded |  | `s 139 CSA 43 the regulations power under section 5(1)(p) of the Social Security Administration Act 1992 may be exercised to secure the payment` (wra3-pt6-misc.l4); `s 139 payment` (wra3-pt6-misc.l4) |
| 2529 | s 140 heading | 140 Fees | inert | 1: section heading (the section is covered by its own rows) |  |
| 2530-2534 | s 140 | In section 6 of the Child Maintenance and Other Payments Act | inert | 2: amends the regulation-making power in section 6(2) of the Child Maintenance and Other Payments Act 2008 (fees); paragraph (h) is itself a power to make regulations |  |
| 2535 | s 141 heading | 141 Review of fees regulations | inert | 1: section heading (the section is covered by its own rows) |  |
| 2536 | s 141 | In section 6 of the Child Maintenance and Other Payments Act | inert | 2: amendment lead-in (Child Maintenance and Other Payments Act 2008 section 6) |  |
| 2537 | s 141(3A) | (3A) The Secretary of State must review the effect of the fi | encoded |  | `s 141 act` (wra3-pt6-misc.l4); `s 141 the duty to review the effect of the first fees regulations` (wra3-pt6-misc.l4) |
| 2538 | s 141(3B) | (3B) The review must take place before the end of the period | encoded |  | `s 141 CMOPA 6(3B) the last day of the 30 months beginning with the day the first fees regulations come into force` (wra3-pt6-misc.l4); `s 141 CMOPA 6(3B) the review took place within the 30 months` (wra3-pt6-misc.l4); `s 141 the duty to review the effect of the first fees regulations` (wra3-pt6-misc.l4) |
| 2539-2541 | s 141(3C) | (3C) After the review, the Secretary of State must make and  | encoded |  | `s 141 CMOPA 6(3C)-(3D) the Secretary of State has done what the report provisions require` (wra3-pt6-misc.l4) |
| 2542 | s 141(3D) | (3D) The report must be laid before Parliament by the Secret | encoded |  | `s 141 CMOPA 6(3C)-(3D) the Secretary of State has done what the report provisions require` (wra3-pt6-misc.l4) |
| 2543 | s 142 heading | 142 Exclusion from individual voluntary arrangements | inert | 1: section heading (the section is covered by its own rows) |  |
| 2544 | s 142(1) | (1) In the Insolvency Act 1986, in section 382 (meaning of “ | inert | 2: amendment lead-in (Insolvency Act 1986 section 382) |  |
| 2545 | s 142(5) | (5) Liability under the Child Support Act 1991 to pay child  | encoded |  | `s 142(1) IA 382(5) the liability is a debt or liability for the purposes of Part 8 of the Insolvency Act 1986` (wra3-pt6-misc.l4) |
| 2546 | s 142(2) | (2) In the heading to that section, after “bankruptcy debt”  | inert | 2: amends a section heading in the Insolvency Act 1986 |  |
| 2547 | heading | Reports on decision-making | inert | 1: heading |  |
| 2548 | s 143 heading | 143 Standards of decision-making | inert | 1: section heading (the section is covered by its own rows) |  |
| 2549 | s 143 | Section 81 of the Social Security Act 1998 (reports by Secre | inert | 2: repeal of section 81 of the Social Security Act 1998 |  |
| 2550 | heading | Employment and training | inert | 1: heading |  |
| 2551 | s 144 heading | 144 Use of jobcentres by sex industry | inert | 1: section heading (the section is covered by its own rows) |  |
| 2552 | s 144 | In the Employment and Training Act 1973, after section 2 (du | inert | 2: amendment lead-in (Employment and Training Act 1973, new section 2A) |  |
| 2553 | ETA 2A heading (inserted) | 2A Restriction on section 2 arrangements: sex industry | inert | 1: section heading (the section is covered by its own rows) |  |
| 2554 | s 144 ETA 2A(1) | (1) Arrangements made by the Secretary of State under sectio | encoded |  | `s 144 ETA 2A(1) the arrangements under section 2 are not barred from including arrangements in respect of the employment` (wra3-pt6-misc.l4) |
| 2555-2557 | s 144 ETA 2A(2) | (2) For the purposes of this section employment is for sexua | encoded |  | `s 144 ETA 2A(2) the employment is employment for sexual purposes` (wra3-pt6-misc.l4) |
| 2558 | s 144 ETA 2A(3) | (3) The Secretary of State may by order specify exceptions t | encoded | the Secretary of State's power to specify exceptions is the input "an order under subsection (3) specifies an exception ..." of s 144 ETA 2A(1); the power itself is not coded | `s 144 ETA 2A(1) the arrangements under section 2 are not barred from including arrangements in respect of the employment` (wra3-pt6-misc.l4) |
| 2559 | s 144 ETA 2A(4) | (4) A statutory instrument containing an order under subsect | inert | 2: procedure for an order (annulment by resolution) |  |
| 2560 | heading | Child poverty | inert | 1: heading |  |
| 2561 | s 145 heading | 145 Social Mobility and Child Poverty Commission | inert | 1: section heading (the section is covered by its own rows) |  |
| 2562 | s 145 | Schedule 13 amends the Child Poverty Act 2010 for the purpos | inert | 2: signpost to Schedule 13 (establishing a body); Schedule 13 has its own rows |  |
| 2563 | s 146 heading | 146 UK child poverty strategies | inert | 1: section heading (the section is covered by its own rows) |  |
| 2564 | s 146(1) | (1) Section 9 of the Child Poverty Act 2010 (UK strategies)  | inert | 2: amendment lead-in (Child Poverty Act 2010 section 9) |  |
| 2565-2567 | s 146(2) | (2) In subsection (7)(a)(i)— | inert | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(i) |  |
| 2568-2571 | s 146(3) | (3) In subsection (7)(a)(ii)— | inert | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(ii) |  |
| 2572-2576 | s 146(4) | (4) In subsection (7)(b)— | inert | 2: amendment of wording in the Child Poverty Act 2010 section 9(7)(b) |  |
| 2577-2578 | s 146(5) | (5) In subsection (8), for paragraphs (b) and (c) there is s | inert | 2: amendment of wording in the Child Poverty Act 2010 section 9(8) |  |
| 2579 | heading | Part 7 — Final | inert | 1: heading |  |
| 2580 | s 147 heading | 147 Repeals | inert | 1: section heading (the section is covered by its own rows) |  |
| 2581 | s 147 | Schedule 14 contains consequential repeals. | inert | 2: signpost to Schedule 14 (repeals); Schedule 14 has its own rows |  |
| 2582 | s 148 heading | 148 Financial provision | inert | 1: section heading (the section is covered by its own rows) |  |
| 2583-2586 | s 148 | There shall be paid out of money provided by Parliament— | encoded |  | `s 148 sum` (wra3-pt7-final.l4); `s 148 the sum is to be paid out of money provided by Parliament` (wra3-pt7-final.l4) |
| 2587 | s 149 heading | 149 Extent | inert | 1: section heading (the section is covered by its own rows) |  |
| 2588 | s 149(1) | (1) This Act extends to England and Wales and Scotland only, | inert | 2: extent |  |
| 2589-2596 | s 149(2) | (2) The following provisions extend to England and Wales, Sc | inert | 2: extent |  |
| 2597 | s 149(3) | (3) Sections 128 and 129 extend to England and Wales only. | inert | 2: extent |  |
| 2598 | s 149(4) | (4) Any amendment or repeal made by this Act has the same ex | inert | 2: extent |  |
| 2599 | s 150 heading | 150 Commencement | inert | 1: section heading (the section is covered by its own rows) |  |
| 2600-2606 | s 150(1) | (1) The following provisions of this Act come into force on  | inert | 2: the Act's own commencement (on the day it is passed) |  |
| 2607-2618 | s 150(2) | (2) The following provisions of this Act come into force at  | inert | 2: the Act's own commencement (two months after the day it is passed) |  |
| 2619 | s 150(3) | (3) The remaining provisions of this Act come into force on  | encoded | the appointed day mechanism: used by Schedule 10 paragraph 1(2) | `s 150(3) the day appointed for the coming into force of the provision` (wra3-pt7-final.l4); `s 150(3) the provision is in force on the date` (wra3-pt7-final.l4) |
| 2620-2627 | s 150(4) | (4) An order under subsection (3) may— | inert | 2: the Act's own commencement (what an order under (3) may do) |  |
| 2628 | s 151 heading | 151 Short title | inert | 1: section heading (the section is covered by its own rows) |  |
| 2629 | s 151 | This Act may be cited as the Welfare Reform Act 2012. | inert | 2: short title |  |
| 3001 | Sch 4 heading | SCHEDULE 4 — Housing credit element of state pension credit | inert | 1: heading |  |
| 3002 | Sch 4 heading | Part 1 — Amendments to State Pension Credit Act 2002 | inert | 1: heading |  |
| 3003 | Sch 4 heading | State Pension Credit Act 2002 (c. 16) | inert | 1: heading |  |
| 3004 | Sch 4 State Pension Credit Act 2002 | The State Pension Credit Act 2002 is amended as follows. | inert | 2: amendment lead-in (State Pension Credit Act 2002) |  |
| 3005-3007 | Sch 4 State Pension Credit Act 2002 | In section 1 (entitlement), in subsection (2)(c), at the end | encoded |  | `sch 4 para 2 SPCA 1(2)(c)(iii) the claimant satisfies the conditions in section 3A(1) and (2)` (wra3-sch4.l4) |
| 3008-3012 | Sch 4 State Pension Credit Act 2002 | In that section, in subsection (3)— | encoded |  | `sch 4 para 3 SPCA 1(3)(b) the credits the claimant is entitled to` (wra3-sch4.l4); `sch 4 para 3 SPCA 1(3)(c) the claimant is entitled to a housing credit` (wra3-sch4.l4); `sch 4 para 3 credit` (wra3-sch4.l4) |
| 3013 | Sch 4 State Pension Credit Act 2002 | After section 3 there is inserted— | inert | 2: amendment lead-in (new section 3A) |  |
| 3014 | Sch 4 State Pension Credit Act 2002 | 3A Housing credit | inert | 1: heading of an inserted section |  |
| 3015 | Sch 4 State Pension Credit Act 2002 (1) | (1) The first of the conditions mentioned in section 1(2)(c) | encoded |  | `sch 4 para 4 SPCA 3A(1) the first condition for housing credit is met` (wra3-sch4.l4) |
| 3016 | Sch 4 State Pension Credit Act 2002 (2) | (2) The second of the conditions mentioned in section 1(2)(c | encoded |  | `sch 4 para 4 SPCA 3A(2) the second condition for housing credit is met` (wra3-sch4.l4) |
| 3017 | Sch 4 State Pension Credit Act 2002 (3) | (3) Where the claimant is entitled to a housing credit, the  | encoded |  | `sch 4 para 4 SPCA 3A(3) the amount of the housing credit` (wra3-sch4.l4) |
| 3018-3021 | Sch 4 State Pension Credit Act 2002 (4) | (4) For the purposes of subsection (1)— | encoded |  | `sch 4 para 4 SPCA 3A(4) the accommodation is accommodation for the purposes of subsection (1)` (wra3-sch4.l4) |
| 3022-3026 | Sch 4 State Pension Credit Act 2002 (5) | (5) Regulations may make provision as to— | inert | 2: regulation-making power |  |
| 3027 | Sch 4 State Pension Credit Act 2002 (6) | (6) Regulations under this section may make different provis | inert | 2: regulation-making power |  |
| 3028 | Sch 4 State Pension Credit Act 2002 | In section 7 (fixing of retirement provision for assessed in | inert | 2: amendment lead-in (State Pension Credit Act 2002 section 7) |  |
| 3029 | Sch 4 State Pension Credit Act 2002 (10) | (10) Regulations may prescribe circumstances in which subsec | inert | 2: regulation-making power |  |
| 3030 | Sch 4 State Pension Credit Act 2002 | In section 12 (polygamous marriages), in subsection (2)(b),  | inert | 2: amendment of State Pension Credit Act 2002 section 12(2)(b) (words inserted) |  |
| 3031 | Sch 4 State Pension Credit Act 2002 | In section 17 (interpretation), in subsection (1), after the | inert | 2: amendment lead-in (State Pension Credit Act 2002 section 17) |  |
| 3032 | Sch 4 State Pension Credit Act 2002 | “housing credit” shall be construed in accordance with secti | encoded |  | `sch 4 para 7 SPCA 17(1) housing credit is construed in accordance with` (wra3-sch4.l4) |
| 3033 | Sch 4 State Pension Credit Act 2002 (8) | (8) In Schedule 2 (consequential amendments etc), paragraph  | inert | 2: repeal in the State Pension Credit Act 2002 Schedule 2 |  |
| 3034 | Sch 4 heading | Part 2 — Amendments to other Acts | inert | 1: heading |  |
| 3035 | Sch 4 heading | Social Security Administration Act 1992 (c. 5) | inert | 1: heading |  |
| 3036 | Sch 4 Social Security Administration Act 1992 | The Social Security Administration Act 1992 is amended as fo | inert | 2: amendment lead-in (Social Security Administration Act 1992) |  |
| 3037 | Sch 4 Social Security Administration Act 1992 | In section 5 (regulations about claims and payments) in subs | inert | 2: amendment of section 5(6) of the Social Security Administration Act 1992 (words inserted) |  |
| 3038 | Sch 4 Social Security Administration Act 1992 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | repealed or blank in this text | a line of dots: the text shows a blank paragraph (a provision omitted from this rendering) |  |
| 3039 | Sch 4 Social Security Administration Act 1992 (1) | (1) Section 122F (supply by rent officers of information) is | inert | 2: amendment lead-in (Social Security Administration Act 1992 section 122F) |  |
| 3040 | Sch 4 Social Security Administration Act 1992 (2) | (2) In subsection (3)(a) at the end of the words in brackets | inert | 2: amendment of section 122F(3)(a) (words inserted) |  |
| 3041 | Sch 4 Social Security Administration Act 1992 (3) | (3) In subsection (4) at the end there is inserted “or housi | inert | 2: amendment of section 122F(4) (words inserted) |  |
| 3042 | Sch 4 Social Security Administration Act 1992 (4) | (4) After that subsection there is inserted— | inert | 2: amendment lead-in (new subsection (5)) |  |
| 3043 | Sch 4 Social Security Administration Act 1992 (5) | (5) In this section “housing credit“ has the same meaning as | encoded |  | `sch 4 para 12 SSAA 122F(5) housing credit has the same meaning as in` (wra3-sch4.l4) |
| 3044 | Sch 4 heading | Housing Act 1996 (c. 52) | inert | 1: heading |  |
| 3045 | Sch 4 Housing Act 1996 (1) | (1) Section 122 of the Housing Act 1996 (rent officers) is a | inert | 2: amendment lead-in (Housing Act 1996 section 122) |  |
| 3046 | Sch 4 Housing Act 1996 (2) | (2) In the heading, at the end there is inserted “and housin | inert | 2: amendment of a section heading |  |
| 3047 | Sch 4 Housing Act 1996 (3) | (3) In subsection (1), at the end there is inserted “or hous | inert | 2: amendment of section 122(1) (words inserted) |  |
| 3048 | Sch 4 heading | Child Support, Pensions and Social Security Act 2000 (c. 19) | inert | 1: heading |  |
| 3049 | Sch 4 Child Support, Pensions and Social Security Act 2000 | In section 69 of the Child Support, Pensions and Social Secu | inert | 2: amendment of section 69(1)(a) of the Child Support, Pensions and Social Security Act 2000 (words inserted) |  |
| 3237 | Sch 9 heading | SCHEDULE 9 — Personal independence payment: amendments | inert | 1: heading |  |
| 3238 | Sch 9 heading | Transport Act 1982 (c. 49) | inert | 1: heading |  |
| 3239-3240 | Sch 9 Transport Act 1982 | In section 70 of the Transport Act 1982 (payments in respect | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3241 | Sch 9 heading | Child Support Act 1991 (c. 48) | inert | 1: heading |  |
| 3242 | Sch 9 Child Support Act 1991 | In section 8 of the Child Support Act 1991 (role of courts w | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3243 | Sch 9 heading | Social Security Contributions and Benefits Act 1992 (c. 4) | inert | 1: heading |  |
| 3244 | Sch 9 Social Security Contributions and Benefits Act 1992 | The Social Security Contributions and Benefits Act 1992 is a | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3245-3246 | Sch 9 Social Security Contributions and Benefits Act 1992 | In section 30B (incapacity benefit: rate), in subsection (4) | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3247 | Sch 9 Social Security Contributions and Benefits Act 1992 (1) | (1) Section 64 (entitlement to attendance allowance) is amen | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3248 | Sch 9 Social Security Contributions and Benefits Act 1992 (2) | (2) In subsection (1), for “the care component of a disabili | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3249 | Sch 9 Social Security Contributions and Benefits Act 1992 (3) | (3) After subsection (1) there is inserted— | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3250-3252 | Sch 9 Social Security Contributions and Benefits Act 1992 (1A) | (1A) The following allowances are within this subsection— | encoded |  | `sch 9 para 5 SSCBA 64(1A) the allowance is within subsection (1A)` (wra3-sch9.l4); `sch 9 para 5 allowance` (wra3-sch9.l4) |
| 3253-3254 | Sch 9 Social Security Contributions and Benefits Act 1992 | In section 150 (Christmas bonus for pensioners: interpretati | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3255 | Sch 9 heading | Social Security Administration Act 1992 (c. 5) | inert | 1: heading |  |
| 3256 | Sch 9 Social Security Administration Act 1992 | The Social Security Administration Act 1992 is amended as fo | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3257 | Sch 9 Social Security Administration Act 1992 (1) | (1) Section 1 (entitlement to benefit dependent on claim) is | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3258-3261 | Sch 9 Social Security Administration Act 1992 (2) | (2) In subsection (3)— | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3262-3263 | Sch 9 Social Security Administration Act 1992 (3) | (3) In subsection (4), after paragraph (ac) there is inserte | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3264-3265 | Sch 9 Social Security Administration Act 1992 | In section 5(2) (regulations about claims for and payments o | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3266-3267 | Sch 9 Social Security Administration Act 1992 | In section 71(11) (overpayments), after paragraph (ac) there | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3268 | Sch 9 Social Security Administration Act 1992 | In section 73 (overlapping benefits - general), after subsec | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3269 | Sch 9 Social Security Administration Act 1992 (6) | (6) Personal independence payment is to be treated for the p | encoded |  | `sch 9 para 11 SSAA 73(6) the benefit is treated for the purposes of section 73 as if it were benefit as defined in section 122 of the Contributions and Benefits Act` (wra3-sch9.l4) |
| 3270-3271 | Sch 9 Social Security Administration Act 1992 | In section 121DA (interpretation of Part 6), in subsection ( | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3272 | Sch 9 Social Security Administration Act 1992 | In section 122B (supply of other government information for  | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3273 | Sch 9 Social Security Administration Act 1992 | In section 122C (supply of information to authorities admini | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3274-3275 | Sch 9 Social Security Administration Act 1992 | In section 124 (age, death and marriage), in subsection (1), | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3276 | Sch 9 Social Security Administration Act 1992 | In section 125 (regulations as to notification of deaths), i | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3277-3280 | Sch 9 Social Security Administration Act 1992 | In section 150 (uprating)— | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3281-3282 | Sch 9 Social Security Administration Act 1992 | In section 159 (effect of alteration in the component rates  | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3283-3284 | Sch 9 Social Security Administration Act 1992 | In section 159A (effect of alteration of rates of a jobseeke | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3285 | Sch 9 Social Security Administration Act 1992 | In section 159B (effect of alterations affecting state pensi | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3286 | Sch 9 Social Security Administration Act 1992 | In section 159C (effect of alteration of rates of an employm | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3287 | Sch 9 Social Security Administration Act 1992 | In section 160 (implementation of increases in income suppor | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3288-3289 | Sch 9 Social Security Administration Act 1992 | In section 160A (implementation of increases in income-based | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3290-3292 | Sch 9 Social Security Administration Act 1992 | In section 160B (implementation of increases in employment a | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3293 | Sch 9 Social Security Administration Act 1992 | In section 165 (adjustments between National Insurance Fund  | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3294-3295 | Sch 9 Social Security Administration Act 1992 | In section 170 (Social Security Advisory Committee), in subs | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3296-3298 | Sch 9 Social Security Administration Act 1992 | Part 4 of that Act; | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3299 | Sch 9 Social Security Administration Act 1992 (1) | (1) Section 179 (reciprocal agreements) is amended as follow | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3300 | Sch 9 Social Security Administration Act 1992 (2) | (2) In subsection (3)(a), after “Welfare Reform Act 2012” (i | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3301-3302 | Sch 9 Social Security Administration Act 1992 (3) | (3) In subsection (4), after paragraph (ag) (inserted by Sch | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3303 | Sch 9 Social Security Administration Act 1992 | In section 180 (payment of travelling expenses), in paragrap | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3304 | Sch 9 Social Security Administration Act 1992 | In section 182B (information about postal redirection), in s | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3305 | Sch 9 Social Security Administration Act 1992 | In section 184 (control of pneumoconiosis), in paragraph (c) | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3306-3307 | Sch 9 Social Security Administration Act 1992 | In section 187 (inalienability), in subsection (1), after pa | encoded |  | `sch 9 para 31 SSAA 187(1)(ad) the benefit is within the limb` (wra3-sch9.l4) |
| 3308 | Sch 9 Social Security Administration Act 1992 | In section 191 (interpretation), in the definition of “benef | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3309 | Sch 9 Social Security Administration Act 1992 | In Schedule 7 (regulations not requiring prior submission to | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3310 | Sch 9 heading | Personal independence payment | inert | 1: heading |  |
| 3311 | Sch 9 Social Security Administration Act 1992 | Regulations under section 78(3) or 79(3) of the Welfare Refo | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3312 | Sch 9 heading | Social Security (Recovery of Benefits) Act 1997 (c. 27) | inert | 1: heading |  |
| 3313 | Sch 9 Social Security (Recovery of Benefits) Act 1997 | The Social Security (Recovery of Benefits) Act 1997 is amend | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3314 | Sch 9 Social Security (Recovery of Benefits) Act 1997 | In section 29 (general interpretation), in the definition of | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3315-3317 | Sch 9 Social Security (Recovery of Benefits) Act 1997 | In Schedule 2 (calculation of compensation payment), in the  | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3318 | Sch 9 heading | Social Security Act 1998 (c. 14) | inert | 1: heading |  |
| 3319 | Sch 9 Social Security Act 1998 | The Social Security Act 1998 is amended as follows. | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3320-3322 | Sch 9 Social Security Act 1998 | In section 2(2) (use of computers), after paragraph (k) (ins | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3323-3326 | Sch 9 Social Security Act 1998 | In section 8 (decisions by Secretary of State)— | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3327 | Sch 9 Social Security Act 1998 | In section 11(3) (regulations with respect to decisions), in | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3328-3331 | Sch 9 Social Security Act 1998 | In section 27(7) (restriction on entitlement in cases of err | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3332-3334 | Sch 9 Social Security Act 1998 | In section 28(3) (correction of errors in decisions etc), af | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3335-3337 | Sch 9 Social Security Act 1998 | In Schedule 3 (decisions against which an appeal lies), in p | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3338-3339 | Sch 9 Social Security Act 1998 | (h) regulations made under section 85(1) or 86(1) of the Wel | fork | F-sch9-1 | `sch 9 para 43 SSA1998 Sch 3 para 3(h) and (i) an appeal lies against the decision` (wra3-sch9.l4); `sch 9 para 43 decision` (wra3-sch9.l4) |
| 3340 | Sch 9 heading | Immigration and Asylum Act 1999 (c. 33) | inert | 1: heading |  |
| 3341-3343 | Sch 9 Immigration and Asylum Act 1999 | In section 115 of the Immigration and Asylum Act 1999 (exclu | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3344 | Sch 9 heading | Social Security Fraud Act 2001 (c. 11) | inert | 1: heading |  |
| 3345 | Sch 9 Social Security Fraud Act 2001 | The Social Security Fraud Act 2001 is amended as follows. | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3346 | Sch 9 Social Security Fraud Act 2001 | In section 6A(1) (definitions)— | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3347-3348 | Sch 9 Social Security Fraud Act 2001 | (a) in the definition of “disqualifying benefit”, after para | encoded |  | `sch 9 para 46 SSFA 6A(1) disqualifying benefit (ca) the benefit is within the limb` (wra3-sch9.l4) |
| 3349-3350 | Sch 9 Social Security Fraud Act 2001 | (b) in the definition of “sanctionable benefit”, after parag | encoded |  | `sch 9 para 46 SSFA 6A(1) sanctionable benefit (ca) the benefit is within the limb` (wra3-sch9.l4) |
| 3351-3352 | Sch 9 Social Security Fraud Act 2001 | In section 10 (power to supplement and mitigate loss of bene | encoded |  | `sch 9 para 47 SSFA 10(3)(be) the benefit is within the limb` (wra3-sch9.l4) |
| 3353 | Sch 9 heading | Income Tax (Earnings and Pensions) Act 2003 (c. 1) | inert | 1: heading |  |
| 3354 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | The Income Tax (Earnings and Pensions) Act 2003 is amended a | inert | 2: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |  |
| 3355 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | In section 677 (UK social security benefits wholly exempt fr | repealed or blank in this text | the text shows a blank where the inserted entry would be (the inserted table row is missing from this rendering) |  |
| 3356 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | In Part 1 of Schedule 1 (abbreviations of Acts), at the end  | repealed or blank in this text | the text shows a blank where the inserted entry would be (the inserted abbreviation is missing from this rendering) |  |
| 3357 | Sch 10 heading | SCHEDULE 10 — Personal independence payment: transitional | inert | 1: heading |  |
| 3358 | Sch 10 heading | General | inert | 1: heading |  |
| 3359 | Sch 10 (1) | (1) Regulations under section 93 may in particular make prov | inert | 2: regulation-making power (regulations under section 93 may in particular make provision ...) |  |
| 3360 | Sch 10 (2) | (2) In this Schedule “the appointed day” means the day appoi | encoded |  | `sch 10 para 1(2) the appointed day` (wra3-sch10.l4); `sch 10 para 1(2) the date is on or after the appointed day` (wra3-sch10.l4) |
| 3361 | Sch 10 heading | Claims before the appointed day | inert | 1: heading |  |
| 3362-3365 | Sch 10 (1) | (1) The provision referred to in paragraph 1(1) includes— | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3366 | Sch 10 (2) | (2) The provision referred to in paragraph 1(1) includes pro | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3367 | Sch 10 heading | Claims after the appointed day | inert | 1: heading |  |
| 3368-3375 | Sch 10 (1) | (1) The provision referred to in paragraph 1(1) includes— | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3376 | Sch 10 (2) | (2) The provision referred to in paragraph 1(1) includes pro | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3377 | Sch 10 heading | Awards | inert | 1: heading |  |
| 3378-3380 | Sch 10 (1) | (1) The provision referred to in paragraph 1(1) includes— | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3381-3387 | Sch 10 (2) | (2) The provision referred to in sub-paragraph (1)(b) includ | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3388 | Sch 10 heading | Supplementary | inert | 1: heading |  |
| 3389-3392 | Sch 10 | Regulations under section 93— | inert | 2: regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources |  |
| 3393 | Sch 11 heading | SCHEDULE 11 — Power to require consideration of revision bef | inert | 1: heading |  |
| 3394 | Sch 11 heading | Vaccine Damage Payments Act 1979 (c. 17) | inert | 1: heading |  |
| 3395 | Sch 11 Vaccine Damage Payments Act 1979 | The Vaccine Damage Payments Act 1979 is amended as follows. | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3396 | Sch 11 Vaccine Damage Payments Act 1979 (1) | (1) Section 4 (appeals to appeal tribunals) is amended as fo | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3397 | Sch 11 Vaccine Damage Payments Act 1979 (2) | (2) After subsection (1A) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3398 | Sch 11 Vaccine Damage Payments Act 1979 (1B) | (1B) If the claimant's address is not in Northern Ireland, r | encoded |  | `sch 11 para 2(2) VDPA 4(1B) there is a right of appeal against the decision` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3399-3402 | Sch 11 Vaccine Damage Payments Act 1979 (1C) | (1C) The regulations may in particular provide that that con | encoded | the three conditions of (1C) are one plain input, "the consideration satisfied the further conditions the regulations specify" | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3403 | Sch 11 Vaccine Damage Payments Act 1979 (3) | (3) At the end of subsection (2) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3404 | Sch 11 Vaccine Damage Payments Act 1979 | (c) provision that, where in accordance with regulations und | encoded |  | `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4); `sch 11 para 2(3) VDPA 4(2)(c) a purported appeal may be treated as an application to reverse the decision under section 3A` (wra3-sch11.l4) |
| 3405 | Sch 11 Vaccine Damage Payments Act 1979 (1) | (1) Section 8 (regulations) is amended as follows. | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3406 | Sch 11 Vaccine Damage Payments Act 1979 (2) | (2) In subsection (2)(a) the words from “which shall be” to  | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3407 | Sch 11 Vaccine Damage Payments Act 1979 (3) | (3) After that subsection there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3408-3410 | Sch 11 Vaccine Damage Payments Act 1979 (2A) | (2A) A statutory instrument containing regulations made by t | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3411 | Sch 11 Vaccine Damage Payments Act 1979 (4) | (4) At the end there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3412-3417 | Sch 11 Vaccine Damage Payments Act 1979 (5) | (5) The power to make regulations under section 4(1B) may be | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3418 | Sch 11 heading | Child Support Act 1991 (c. 48) | inert | 1: heading |  |
| 3419 | Sch 11 Child Support Act 1991 | The Child Support Act 1991 is amended as follows. | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3420 | Sch 11 Child Support Act 1991 (1) | (1) Section 20 (appeals to First-tier Tribunal), as substitu | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3421 | Sch 11 Child Support Act 1991 (2) | (2) After subsection (2) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3422 | Sch 11 Child Support Act 1991 (2A) | (2A) Regulations may provide that, in such cases or circumst | encoded |  | `sch 11 para 5(2) CSA 20(2A) there is a right of appeal against the decision` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3423-3426 | Sch 11 Child Support Act 1991 (2B) | (2B) The regulations may in particular provide that that con | encoded | the three conditions of (2B) are one plain input | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3427 | Sch 11 Child Support Act 1991 (3) | (3) At the end of subsection (4) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3428 | Sch 11 Child Support Act 1991 | (c) provision that, where in accordance with regulations und | encoded |  | `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4); `sch 11 para 5(3) CSA 20(4)(c) a purported appeal may be treated as an application for revision under section 16` (wra3-sch11.l4) |
| 3429 | Sch 11 Child Support Act 1991 (1) | (1) Section 20 (appeals to First-tier Tribunal), as it has e | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3430 | Sch 11 Child Support Act 1991 (2) | (2) After subsection (3) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3431 | Sch 11 Child Support Act 1991 (3A) | (3A) Regulations may provide that, in such cases or circumst | encoded |  | `sch 11 para 6(2) CSA 20(3A) there is a right of appeal against the decision` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3432-3435 | Sch 11 Child Support Act 1991 (3B) | (3B) The regulations may in particular provide that that con | encoded | the three conditions of (3B) are one plain input | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3436 | Sch 11 Child Support Act 1991 (3) | (3) At the end of subsection (5) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3437 | Sch 11 Child Support Act 1991 | (c) provision that, where in accordance with regulations und | encoded |  | `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4); `sch 11 para 6(3) CSA 20(5)(c) a purported appeal may be treated as an application for revision under section 16` (wra3-sch11.l4) |
| 3438 | Sch 11 Child Support Act 1991 | In section 51A (pilot schemes) at the end there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3439-3441 | Sch 11 Child Support Act 1991 (6) | (6) This section does not apply to regulations under— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3442 | Sch 11 Child Support Act 1991 | In section 52 (regulations and orders), in subsection (2)(a) | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3443 | Sch 11 heading | Social Security (Recovery of Benefits) Act 1997 (c. 27) | inert | 1: heading |  |
| 3444 | Sch 11 Social Security (Recovery of Benefits) Act 1997 | The Social Security (Recovery of Benefits) Act 1997 is amend | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3445 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (1) | (1) Section 11 (appeals against certificates) is amended as  | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3446 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2) | (2) After subsection (2) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3447 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2A) | (2A) Regulations may provide that, in such cases or circumst | encoded |  | `sch 11 para 10(2) SSRBA 11(2A) an appeal may be made against the certificate` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3448-3451 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2B) | (2B) The regulations may in particular provide that that con | encoded | the three conditions of (2B) are one plain input | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3452 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (3) | (3) In subsection (5)(c) after “any such appeal“ there is in | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3453 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (1) | (1) Section 30 of that Act (regulations and orders) is amend | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3454 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2) | (2) In subsection (2) after “regulations under section” ther | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3455 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (3) | (3) After that subsection there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3456 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2A) | (2A) A statutory instrument containing regulations under sec | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3457 | Sch 11 heading | Child Support, Pensions and Social Security Act 2000 (c. 19) | inert | 1: heading |  |
| 3458 | Sch 11 Child Support, Pensions and Social Security Act 2000 | Schedule 7 to the Child Support, Pensions and Social Securit | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3459 | Sch 11 Child Support, Pensions and Social Security Act 2000 (1) | (1) Paragraph 6 (housing benefit and council tax benefit: ap | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3460-3461 | Sch 11 Child Support, Pensions and Social Security Act 2000 (2) | (2) In sub-paragraph (4), after paragraph (b) there is inser | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3462 | Sch 11 Child Support, Pensions and Social Security Act 2000 (3) | (3) After sub-paragraph (5) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3463 | Sch 11 Child Support, Pensions and Social Security Act 2000 (5A) | (5A) Regulations may provide that, in such cases or circumst | encoded |  | `sch 11 para 13(3) CSPSSA Sch 7 para 6(5A) there is a right of appeal against the decision` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3464-3467 | Sch 11 Child Support, Pensions and Social Security Act 2000 (5B) | (5B) The regulations may in particular provide that that con | encoded | the three conditions of (5B) are one plain input | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3468-3470 | Sch 11 Child Support, Pensions and Social Security Act 2000 (4) | (4) In sub-paragraph (8)— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3471 | Sch 11 Child Support, Pensions and Social Security Act 2000 | (b) provide that, where in accordance with regulations under | encoded |  | `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4); `sch 11 para 13(4) CSPSSA Sch 7 para 6(8)(b) a purported appeal may be treated as an application for revision under paragraph 3` (wra3-sch11.l4) |
| 3472 | Sch 11 Child Support, Pensions and Social Security Act 2000 | In paragraph 20(4) (regulations subject to affirmative proce | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3473 | Sch 11 heading | Child Maintenance and Other Payments Act 2008 (c. 6) | inert | 1: heading |  |
| 3474 | Sch 11 Child Maintenance and Other Payments Act 2008 | The Child Maintenance and Other Payments Act 2008 is amended | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3475 | Sch 11 Child Maintenance and Other Payments Act 2008 | In section 49(2) (regulations regarding reconsideration) aft | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3476 | Sch 11 Child Maintenance and Other Payments Act 2008 (1) | (1) Section 50 (appeals to First-tier Tribunal) is amended a | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3477 | Sch 11 Child Maintenance and Other Payments Act 2008 (2) | (2) After subsection (1) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3478 | Sch 11 Child Maintenance and Other Payments Act 2008 (1A) | (1A) Regulations may provide that, in such cases or circumst | encoded |  | `sch 11 para 17(2) CMOPA 50(1A) there is a right of appeal against the determination` (wra3-sch11.l4); `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3479-3482 | Sch 11 Child Maintenance and Other Payments Act 2008 (1B) | (1B) The regulations may in particular provide that that con | encoded | the three conditions of (1B) are one plain input | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) |
| 3483 | Sch 11 Child Maintenance and Other Payments Act 2008 (3) | (3) In subsection (4)(c) after “an appeal under subsection ( | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3484 | Sch 11 Child Maintenance and Other Payments Act 2008 (1) | (1) Section 53 (regulations under Part 4) is amended as foll | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3485 | Sch 11 Child Maintenance and Other Payments Act 2008 (2) | (2) After subsection (2) there is inserted— | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3486-3491 | Sch 11 Child Maintenance and Other Payments Act 2008 (2A) | (2A) The power to make regulations under section 50(1A) may  | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3492 | Sch 11 Child Maintenance and Other Payments Act 2008 (3) | (3) In subsection (3) after “section 46” there is inserted “ | inert | 2: amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed) |  |
| 3493 | Sch 12 heading | SCHEDULE 12 — Supersession of decisions of former appellate  | inert | 1: heading |  |
| 3494 | Sch 12 heading | Child Support Act 1991 (c. 48) | inert | 1: heading |  |
| 3495 | Sch 12 Child Support Act 1991 | The Child Support Act 1991 is amended as follows. | inert | 2: amendment lead-in |  |
| 3496 | Sch 12 Child Support Act 1991 (1) | (1) Section 17 (decisions superseding earlier decisions) is  | inert | 2: amendment lead-in (Child Support Act 1991 section 17) |  |
| 3497-3499 | Sch 12 Child Support Act 1991 (2) | (2) In subsection (1)— | fork | F-sch12-1 | `sch 12 para 2(2) CSA 17(1) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4) |
| 3500 | Sch 12 Child Support Act 1991 (3) | (3) After subsection (5) there is inserted— | inert | 2: amendment lead-in (new subsection (6)) |  |
| 3501 | Sch 12 Child Support Act 1991 (6) | (6) In this section— | inert | 1: introductory words ("In this section—") of the definitions |  |
| 3502 | Sch 12 Child Support Act 1991 | “appeal tribunal” means an appeal tribunal constituted under | encoded |  | `sch 12 body` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body is an appeal tribunal` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4) |
| 3503 | Sch 12 Child Support Act 1991 | “Child Support Commissioner” means a person appointed as suc | encoded |  | `sch 12 para 2(3) CSA 17(6) the body is a Child Support Commissioner` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4) |
| 3504 | Sch 12 Child Support Act 1991 (1) | (1) In Schedule 4C (departure directions), paragraph 2 is am | inert | 2: amendment lead-in (Child Support Act 1991 Schedule 4C) |  |
| 3505 | Sch 12 Child Support Act 1991 (2) | (2) In sub-paragraph (1)(c), after “any decision of” there i | fork | F-sch12-1 | `sch 12 para 3 CSA Sch 4C para 2 the decision is within the decisions listed` (wra3-sch12.l4) |
| 3506 | Sch 12 Child Support Act 1991 (3) | (3) In sub-paragraph (2), after “any decision of“ (in each p | fork | F-sch12-1 | `sch 12 para 3 CSA Sch 4C para 2 the decision is within the decisions listed` (wra3-sch12.l4) |
| 3507 | Sch 12 Child Support Act 1991 (4) | (4) After sub-paragraph (2) there is inserted— | inert | 2: amendment lead-in (new sub-paragraph (3)) |  |
| 3508 | Sch 12 Child Support Act 1991 (3) | (3) In this paragraph “appeal tribunal“ means an appeal trib | encoded |  | `sch 12 para 2(3) CSA 17(6) the body is an appeal tribunal` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4) |
| 3509 | Sch 12 heading | Social Security Act 1998 (c. 14) | inert | 1: heading |  |
| 3510 | Sch 12 Social Security Act 1998 (1) | (1) Section 10 of the Social Security Act 1998 (decisions su | inert | 2: amendment lead-in (Social Security Act 1998 section 10) |  |
| 3511-3512 | Sch 12 Social Security Act 1998 (2) | (2) In subsection (1), the “and” at the end of paragraph (a) | fork | F-sch12-1 | `sch 12 para 4(2) SSA1998 10(1)(aa) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4) |
| 3513 | Sch 12 Social Security Act 1998 (3) | (3) After subsection (6) there is inserted— | inert | 2: amendment lead-in (new subsection (7)) |  |
| 3514 | Sch 12 Social Security Act 1998 (7) | (7) In this section— | inert | 1: introductory words ("In this section—") of the definitions |  |
| 3515 | Sch 12 Social Security Act 1998 | “appeal tribunal” means an appeal tribunal constituted under | encoded |  | `sch 12 para 2(3) CSA 17(6) the body is an appeal tribunal` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4) |
| 3516 | Sch 12 Social Security Act 1998 | “Commissioner” means a person appointed as a Social Security | encoded |  | `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4); `sch 12 para 4(3) SSA1998 10(7) the body is a Commissioner` (wra3-sch12.l4) |
| 3517 | Sch 12 heading | Child Support, Pensions and Social Security Act 2000 (c. 19) | inert | 1: heading |  |
| 3518 | Sch 12 Child Support, Pensions and Social Security Act 2000 (1) | (1) In Schedule 7 to the Child Support, Pensions and Social  | inert | 2: amendment lead-in (Child Support, Pensions and Social Security Act 2000 Schedule 7 paragraph 4) |  |
| 3519-3520 | Sch 12 Child Support, Pensions and Social Security Act 2000 (2) | (2) In sub-paragraph (1), the “and” at the end of paragraph  | fork | F-sch12-1 | `sch 12 para 5 CSPSSA Sch 7 para 4(1)(aa) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4) |
| 3521-3523 | Sch 12 Child Support, Pensions and Social Security Act 2000 (3) | (3) In sub-paragraph (2)— | fork | F-sch12-1 | `sch 12 para 5 CSPSSA Sch 7 para 4(1)(aa) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4) |
| 3524 | Sch 12 Child Support, Pensions and Social Security Act 2000 (4) | (4) After sub-paragraph (6) there is inserted— | inert | 2: amendment lead-in (new sub-paragraph (7)) |  |
| 3525 | Sch 12 Child Support, Pensions and Social Security Act 2000 (7) | (7) In this paragraph— | inert | 1: introductory words ("In this paragraph—") of the definitions |  |
| 3526 | Sch 12 Child Support, Pensions and Social Security Act 2000 | “appeal tribunal” means an appeal tribunal constituted under | encoded |  | `sch 12 para 2(3) CSA 17(6) the body is an appeal tribunal` (wra3-sch12.l4); `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4) |
| 3527 | Sch 12 Child Support, Pensions and Social Security Act 2000 | “Commissioner” means a person appointed as a Social Security | encoded |  | `sch 12 para 2(3) CSA 17(6) the body whose functions have been transferred is now` (wra3-sch12.l4); `sch 12 para 4(3) SSA1998 10(7) the body is a Commissioner` (wra3-sch12.l4) |
| 3528 | Sch 13 heading | SCHEDULE 13 — Social Mobility and Child Poverty Commission | inert | 1: heading |  |
| 3529 | Sch 13 heading | Part 1 — Establishment of Social Mobility and Child Poverty  | inert | 1: heading |  |
| 3530 | Sch 13 | The Child Poverty Act 2010 is amended as follows. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3531 | Sch 13 | For section 8 (and the preceding italic heading) there is su | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3532 | Sch 13 heading | Social Mobility and Child Poverty Commission | inert | 1: heading |  |
| 3533 | Sch 13 | 8 Social Mobility and Child Poverty Commission | inert | 1: heading of an inserted section |  |
| 3534 | Sch 13 (1) | (1) There is to be a body called the Social Mobility and Chi | encoded |  | `sch 13 CPA 8(1) the body is the Commission` (wra3-sch13.l4); `sch 13 body` (wra3-sch13.l4) |
| 3535 | Sch 13 (2) | (2) The Commission's functions are those conferred on it by  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3536 | Sch 13 (3) | (3) Schedule 1 contains further provision about the Commissi | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3537-3539 | Sch 13 (4) | (4) A Minister of the Crown may by order provide for the Com | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3540 | Sch 13 (5) | (5) An order under subsection (4) may contain such transitio | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3541-3544 | Sch 13 (6) | (6) That provision may include provision amending, repealing | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3545 | Sch 13 | 8A Advice | inert | 1: heading of an inserted section |  |
| 3546 | Sch 13 (1) | (1) The Commission must on request give advice to a Minister | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3547 | Sch 13 (2) | (2) Advice given under this section must be published. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3548 | Sch 13 | 8B Annual reports | inert | 1: heading of an inserted section |  |
| 3549 | Sch 13 (1) | (1) Before each anniversary of the coming into force of this | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3550-3554 | Sch 13 (2) | (2) Those goals are— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3555-3558 | Sch 13 (3) | (3) A report under subsection (1) must also describe— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3559 | Sch 13 (4) | (4) A report under subsection (1) may by published as one or | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3560 | Sch 13 (5) | (5) If the Commission so requests, a Minister of the Crown m | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3561 | Sch 13 (6) | (6) A Minister of the Crown must lay a report under this sec | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3562 | Sch 13 | 8C Other functions | inert | 1: heading of an inserted section |  |
| 3563 | Sch 13 | A Minister of the Crown may direct the Commission to carry o | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3564 | Sch 13 | For Schedule 1 (Child Poverty Commission) there is substitut | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3565 | Sch 13 heading | SCHEDULE 1 — Social Mobility and Child Poverty Commission | inert | 1: heading |  |
| 3566 | Sch 13 heading | Membership, chair and deputy chair | inert | 1: heading |  |
| 3567-3572 | Sch 13 (1) | (1) The members of the Commission are to be— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3573 | Sch 13 (2) | (2) A Minister of the Crown may appoint one of the members a | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3574 | Sch 13 heading | Term of office | inert | 1: heading |  |
| 3575 | Sch 13 | Members are to hold and vacate office in accordance with the | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3576 | Sch 13 | Members must be appointed for a term of not more than five y | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3577 | Sch 13 | A member may resign by giving notice in writing to a Ministe | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3578-3582 | Sch 13 | A Minister of the Crown may remove a member if— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3583-3585 | Sch 13 | A person ceases to be the chair or the deputy chair if the p | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3586 | Sch 13 | A person who holds or has held office as the chair, or as th | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3587 | Sch 13 heading | Provision of staff and facilities etc | inert | 1: heading |  |
| 3588-3592 | Sch 13 (1) | (1) A Minister of the Crown may provide the Commission with— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3593 | Sch 13 (2) | (2) A Minister of the Crown may, if the Commission so reques | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3594 | Sch 13 heading | Payments | inert | 1: heading |  |
| 3595 | Sch 13 | A Minister of the Crown may pay to or in respect of the memb | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3596 | Sch 13 heading | Supplementary powers | inert | 1: heading |  |
| 3597 | Sch 13 | The Commission may do anything that appears to it necessary  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3598 | Sch 13 heading | Status | inert | 1: heading |  |
| 3599-3601 | Sch 13 | The Commission is not to be regarded— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3602 | Sch 13 heading | Sub-committees | inert | 1: heading |  |
| 3603 | Sch 13 | The Commission may establish sub-committees. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3604 | Sch 13 heading | Validity of proceedings | inert | 1: heading |  |
| 3605-3607 | Sch 13 | The Commission may regulate— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3608-3610 | Sch 13 | The validity of anything done by the Commission or any sub-c | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3611 | Sch 13 heading | Discharge of functions | inert | 1: heading |  |
| 3612 | Sch 13 | The Commission may authorise a sub-committee or member to ex | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3613 | Sch 13 heading | Part 2 — Supplementary amendments to Child Poverty Act 2010 | inert | 1: heading |  |
| 3614 | Sch 13 | The Child Poverty Act 2010 is amended as follows. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3615 | Sch 13 | In section 6 (persistent poverty target), subsection (6)(b)  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3616-3618 | Sch 13 | In section 10 (provision of advice and consultation)— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3619-3621 | Sch 13 | In section 13 (advice and consultation: Scotland and Norther | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3622 | Sch 13 (1) | (1) In the italic heading preceding section 14, for “Reports | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3623 | Sch 13 (2) | (2) Section 14 is repealed. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3624 | Sch 13 (1) | (1) Section 15 (statement in relation to target year) is ame | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3625 | Sch 13 (2) | (2) In subsection (1), for “The report under section 14(3) m | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3626 | Sch 13 (3) | (3) In subsection (4), for “the report under section 14(3)”  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3627 | Sch 13 (4) | (4) At the end there is inserted— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3628 | Sch 13 (5) | (5) The Secretary of State must consult the Scottish Ministe | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3629 | Sch 13 | In section 16 (economic and fiscal circumstances), in subsec | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3630 | Sch 13 (1) | (1) Section 18 (interpretation) is amended as follows. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3631 | Sch 13 (2) | (2) In the definition of “the Commission” in subsection (1), | encoded |  | `sch 13 CPA 18(1) the name that now stands in the definition of the Commission` (wra3-sch13.l4) |
| 3632 | Sch 13 (3) | (3) After the definition of “financial year” in that subsect | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3633 | Sch 13 | “Minister of the Crown” has the same meaning as in the Minis | encoded |  | `sch 13 CPA 18(1) the person is a Minister of the Crown` (wra3-sch13.l4) |
| 3634 | Sch 13 (4) | (4) After subsection (2) there is inserted— | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3635 | Sch 13 (3) | (3) In this Part “appointed day for Northern Ireland” means  | encoded |  | `sch 13 CPA 18(3) the day is the appointed day for Northern Ireland for the provision` (wra3-sch13.l4) |
| 3636 | Sch 13 | In section 28 (regulations and orders), in subsection (5)(b) | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3637 | Sch 13 (1) | (1) Schedule 2 (continuing effect of targets) is amended as  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3638 | Sch 13 (2) | (2) In paragraph 1, in paragraph (a) of the definition of “t | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3639 | Sch 13 (3) | (3) In paragraph 3(d), for “the Secretary of State”, in the  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3640 | Sch 13 (4) | (4) Paragraphs 6(c) and (d) and 7(1)(b) are repealed. | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3641 | Sch 13 heading | Part 3 — Supplementary amendments to other Acts | inert | 1: heading |  |
| 3642-3644 | Sch 13 | In Schedule 1 to the Public Records Act 1958 (definition of  | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3645-3647 | Sch 13 | In Schedule 2 to the Parliamentary Commissioner Act 1967 (de | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3648-3650 | Sch 13 (1) | (1) In Part 2 of Schedule 1 to the House of Commons Disquali | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3651-3653 | Sch 13 (2) | (2) In Part 2 of Schedule 1 to the Northern Ireland Assembly | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3654-3656 | Sch 13 | In Part 6 of Schedule 1 to the Freedom of Information Act 20 | inert | 2: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |  |
| 3657 | Sch 14 heading | SCHEDULE 14 — Repeals | inert | 1: heading |  |
| 3658 | Sch 14 heading | Part 1 — Abolition of benefits superseded by universal credi | inert | 1: heading |  |
| 3659-3661 | Sch 14 | In section 53(3)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3662-3664 | Sch 14 | In section 17— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3665-3667 | Sch 14 | In section 105(1), the definitions of— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3668-3671 | Sch 14 | In section 54(1), the definitions of— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3672-3674 | Sch 14 | In section 22— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3675-3677 | Sch 14 | In section 5— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3678-3681 | Sch 14 | In section 7— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3682-3687 | Sch 14 | In section 15A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3688-3692 | Sch 14 | In section 74— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3693-3696 | Sch 14 | In section 105— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3697-3699 | Sch 14 | In section 109A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3700-3702 | Sch 14 | In section 111— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3703-3708 | Sch 14 | In section 115A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3709-3714 | Sch 14 | In section 115B— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3715-3717 | Sch 14 | In section 115C (as inserted by section 116 of this Act)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3718-3722 | Sch 14 | In section 116— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3723-3725 | Sch 14 | In section 126(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3726-3730 | Sch 14 | In section 150— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3731-3733 | Sch 14 | In section 159B— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3734-3736 | Sch 14 | In section 159D (as inserted by Schedule 2 to this Act)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3737-3739 | Sch 14 | In section 166— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3740-3742 | Sch 14 | In section 189— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3743-3753 | Sch 14 | In section 191, the definitions of— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3754-3757 | Sch 14 | In Schedule 4— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3758-3761 | Sch 14 | In section 2— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3762-3764 | Sch 14 | In section 4— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3765-3768 | Sch 14 | In section 5— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3769-3771 | Sch 14 | In section 35(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3772-3774 | Sch 14 | In section 38— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3775-3781 | Sch 14 | In Schedule 1— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3782-3784 | Sch 14 | In section 122— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3785-3787 | Sch 14 | In section 457(4)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3788-3792 | Sch 14 | In section 512ZB(4)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3793-3797 | Sch 14 | In Schedule 2— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3798-3801 | Sch 14 | In Schedule 2A, in paragraph 3— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3802-3805 | Sch 14 | In section 115(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3806-3808 | Sch 14 | In Schedule A1, in paragraph 17(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3809-3811 | Sch 14 | In section 6B— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3812-3814 | Sch 14 | In section 7— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3815-3817 | Sch 14 | In section 9— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3818-3820 | Sch 14 | In section 11(3)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3821-3823 | Sch 14 | In section 13, the definitions of— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3824-3826 | Sch 14 | In section 110— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3827-3829 | Sch 14 | In section 13A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3830-3838 | Sch 14 | In section 1— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3839-3841 | Sch 14 | In section 1A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3842-3844 | Sch 14 | In Schedule 1— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3845 | Sch 14 | Part 2. | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3846-3850 | Sch 14 | In Schedule 2— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3851-3853 | Sch 14 | In section 1059— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3854-3856 | Sch 14 | In section 1108— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3857-3862 | Sch 14 | In Part 3 of Schedule 7, the entries relating to — | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3863-3868 | Sch 14 | In section 131— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3869 | Sch 14 heading | Part 2 — Entitlement to jobseeker's allowance without seekin | inert | 1: heading |  |
| 3870-3875 | Sch 14 | In section 32(2), in the inserted section 20E of the Jobseek | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3876-3879 | Sch 14 | In section 32— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3880-3883 | Sch 14 | In Part 3 of Schedule 7, the entries relating to— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3884 | Sch 14 heading | Part 3 — Jobseeker's allowance: responsibilities for interim | inert | 1: heading |  |
| 3885 | Sch 14 heading | Part 4 — Jobseeker's allowance: responsibilities after intro | inert | 1: heading |  |
| 3886-3889 | Sch 14 | In section 35(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3890-3892 | Sch 14 | In section 37(1)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3893 | Sch 14 heading | Part 5 — Employment and support allowance: responsibilities  | inert | 1: heading |  |
| 3894 | Sch 14 heading | Part 6 — Claimants dependent on drugs etc | inert | 1: heading |  |
| 3895-3897 | Sch 14 | In section 16— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3898-3901 | Sch 14 | In Schedule 2— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3902-3904 | Sch 14 | In section 32, in the section 20E to be inserted into the Jo | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3905 | Sch 14 heading | Part 7 — Industrial injuries arising before 5 July 1948 | inert | 1: heading |  |
| 3906-3909 | Sch 14 | In section 2— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3910 | Sch 14 heading | Part 8 — Social fund: ending of discretionary payments | inert | 1: heading |  |
| 3911-3913 | Sch 14 | In section 138— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3914-3916 | Sch 14 | In Schedule 4, in Part 1— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3917 | Sch 14 heading | Part 9 — Disability living allowance | inert | 1: heading |  |
| 3918-3920 | Sch 14 | In section 150— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3921-3923 | Sch 14 | In Schedule 2, in the second column of the table— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3924 | Sch 14 heading | Part 10 — Powers to require information relating to claims a | inert | 1: heading |  |
| 3925 | Sch 14 heading | Part 11 — Recovery of benefit payments | inert | 1: heading |  |
| 3926-3930 | Sch 14 | In section 71— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3931 | Sch 14 heading | Part 12 — Loss of benefit: cautions | inert | 1: heading |  |
| 3932-3934 | Sch 14 | In section 6B— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3935-3937 | Sch 14 | In section 36A (as inserted by section 120 of this Act)— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3938 | Sch 14 heading | Part 13 — Information-sharing between Secretary of State and | inert | 1: heading |  |
| 3939-3941 | Sch 14 | In section 121E— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3942-3945 | Sch 14 | In section 121F— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3946-3955 | Sch 14 | In Schedule 5— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |
| 3956 | Sch 14 heading | Part 14 — Standards of decision-making | inert | 1: heading |  |
| 3957-3959 | Sch 14 | In section 171A— | inert | 2: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |  |

## Fork register (wra3)

Six forks, each a place where the text can be read two or more ways with a different outcome.
The reading I took is the one the function encodes; the other readings are not encoded.
Where the text does not choose, the function answers `NOTHING` or the reading is stated as a lawyer's reading in the next section.

| fork | the text (raw lines) | readings | taken | what licenses each | encoded in |
| --- | --- | --- | --- | --- | --- |
| F-81-1 | s 81(1) (1410-1412): "Regulations under section 80(2) must provide for the question of whether a person meets “the required period condition” ... to be determined by reference to— (a) whether, as respects every time in the previous 3 months, it is likely that ... and (b) whether, as respects every time in the next 9 months, it is likely that ..." | (1) the two limbs are the test: the condition is met when both hold and not met when either fails; (2) "by reference to" only tells the regulations what to take into account, the Act states no test of its own, so the answer is `NOTHING` until the regulations are among the sources | (1) | (1) the two limbs are joined by "and" and each is a "whether" question; s 81(4) lets regulations depart from "the provision made by virtue of subsections (1) to (3)" only "in prescribed cases", which reads as if (1) to (3) were the rule; (2) the subsection's subject is what the regulations "must provide", not what a person must show | `s 81(1) the person meets the required period condition on the usual test` (wra3-pt4-s77-84.l4); `s 81(4) the person meets the required period condition` (wra3-pt4-s77-84.l4) |
| F-81-2 | s 81(3)(b), (c) (1418-1419): "“the previous 3 months” means the 3 months ending with the prescribed date; “the next 9 months” means the 9 months beginning with the day after that date" | (1) calendar months: a period of n months beginning on a day ends on the day before the corresponding date n months on, or on the last day of a shorter month; (2) 30-day months (90 days and 270 days); (3) the previous 3 months start on the corresponding date, so 15 March to 15 June for a prescribed date of 15 June | (1) | (1) "month" is not defined in the sources and "the 3 months ending with ... the next 9 months beginning with the day after" splits a year at a date, which calendar months do without a gap or an overlap; (2) and (3) would also fit the words, and nothing in the sources chooses between them | `s 81(3) the last day of the months beginning with the day` (wra3-pt4-s77-84.l4); `s 81(3)(b) the previous 3 months ending with the prescribed date` (wra3-pt4-s77-84.l4); `s 81(3)(c) the next 9 months beginning with the day after the prescribed date` (wra3-pt4-s77-84.l4) |
| F-82 | s 82(4) (1430): "death ... can reasonably be expected within 12 months"; also s 89(a), (b) (1475-1476): "within 2 years beginning with the date", "within 4 years beginning with that date" | (1) the 12 months beginning with a time end on the day before the corresponding date a year on (15 January 2026 gives 14 January 2027); (2) they end on the corresponding date (15 January 2027); (3) 365 days | (1), by the same helper as F-81-2 (s 89 uses it with 24 and 48 months) | (1) "beginning with the time" counts the time itself as the first day, so a year later is the day before; (2) and (3) are the ordinary spoken reading; the sources define no counting rule | `s 82(4) the last day of the 12 months beginning with the time` (wra3-pt4-s77-84.l4); `s 89(a) the last day of the 2 years beginning with the date the first regulations come into force` (wra3-pt4-s85-90.l4); `s 89(b) the last day of the 4 years beginning with the date the first regulations come into force` (wra3-pt4-s85-90.l4) |
| F-83 | s 83(1), (2) (1437-1440): "not entitled ... for any period after the person reaches the relevant age"; the relevant age is pensionable age "or, if higher, 65" | (1) a person who has reached the relevant age is within the bar on the day they reach it (age in years 65 or more, and pensionable age reached); (2) the bar starts the day after, because "any period after" excludes the day of reaching | (1) | (1) a person is of an age in years from the day of the birthday, the ordinary count; (2) "any period after the person reaches" can be read to begin only after the day of reaching; the sources do not say how a day of reaching is counted | `s 83(2) the person has reached the relevant age` (wra3-pt4-s77-84.l4); `s 83(1) the person is not barred by having reached the relevant age` (wra3-pt4-s77-84.l4) |
| F-sch9-1 | Sch 9 para 43 (3335-3339): "In Schedule 3 (decisions against which an appeal lies), in paragraph 3— ... (h) regulations made under section 85(1) or 86(1) of the Welfare Reform Act 2012; (i) section 87 of that Act." The lead-in of paragraph 3 of that Schedule is not printed | (1) the Schedule's printed title makes (h) and (i) decisions against which an appeal lies, so a decision as to either is `JUST TRUE`; (2) the lead-in is not among the sources, so the paragraphs prove nothing and the answer is `NOTHING` | (1) | (1) "Schedule 3 (decisions against which an appeal lies)" is the text's own title and (h), (i) are inserted into its list; (2) the paragraph's own lead-in, which would say what the list is a list of, is missing | `sch 9 para 43 SSA1998 Sch 3 para 3(h) and (i) an appeal lies against the decision` (wra3-sch9.l4) |
| F-sch12-1 | Sch 12 paras 2-5 (3497-3527): each inserts "an appeal tribunal or a Commissioner" into a host list of decisions, and the host provisions' lead-ins are not printed; s 103(1) (1661, wra4's range) says the Schedule contains "amendments reinstating powers to make decisions superseding decisions made by appellate bodies" | (1) the decisions of the named bodies are within the lists of decisions open to supersession, so each is `JUST TRUE`; (2) the host lists are not among the sources, so the answer is `NOTHING` | (1) for the named bodies, `NOTHING` for any other body | (1) s 103(1) states the purpose of the whole Schedule; (2) each inserted limb is one limb of a longer list whose other limbs are not printed | `sch 12 para 2(2) CSA 17(1) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4); `sch 12 para 3 CSA Sch 4C para 2 the decision is within the decisions listed` (wra3-sch12.l4); `sch 12 para 4(2) SSA1998 10(1)(aa) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4); `sch 12 para 5 CSPSSA Sch 7 para 4(1)(aa) the decision is within the decisions listed as open to supersession` (wra3-sch12.l4) |

Each coverage row with the disposition `fork` names its fork in the "Reason / fork / note" column.

## Jural relations (wra3)

One row per provision that creates a relation, over the whole of my ranges (headings excepted).
A provision that creates no relation of its own (a definition, a counting rule, a lead-in, an amendment that only adds words to another Act) is listed once as `none`, with its reason in the note.
The party names are the text's: the claimant is a person who claims or is entitled to personal independence payment, or is a party to a child support case; the Secretary of State is the payer or decision-maker.
Most rows have the Secretary of State on one side, and many are powers in the Secretary of State to make regulations, whose correlative is a liability in the persons the regulations will bind.
The L4 rule that encodes each row is in the coverage table above, in the row with the same raw lines.

| Lines | Provision | Relation | Holder | Counter-party | Note |
| --- | --- | --- | --- | --- | --- |
| 1347 | s 77(1) | claim-right / duty | the claimant (a person entitled) | the Secretary of State (the payer) | qualified: payable "in accordance with this Part" |
| 1348-1351 | s 77(2) | none |  |  | classifies an entitlement as to one component or both; the claim-rights are in ss 78 and 79 |
| 1352 | s 77(3) | disability / no-right | the claimant without the prescribed residence and presence | the Secretary of State | no claim-right "unless" the person meets conditions that regulations prescribe |
| 1353 | s 77(4) | disability / no-right | the claimant entitled to a Scottish disability payment | the Secretary of State | no claim-right "while" so entitled; the four payments are named in s 95 |
| 1355-1357 | s 78(1) | claim-right / duty | the claimant | the Secretary of State | the daily living component at the standard rate "if" (a) and (b) |
| 1358-1360 | s 78(2) | claim-right / duty | the claimant | the Secretary of State | the daily living component at the enhanced rate "if" (a) and (b) |
| 1361-1363 | s 78(3) | power / liability | the Secretary of State (by regulations) | the claimant | fixes the weekly rate, which is the content of the claim-right in (1) and (2) |
| 1364 | s 78(4) | power / liability | the Secretary of State (by regulations) | the claimant | prescribes the activities the ability questions are about |
| 1368 | s 78(6) | condition on a claim-right | the claimant | the Secretary of State | subjects the claim-rights in s 78 to the rest of Part 4 (ss 82, 83 in particular) |
| 1370-1373 | s 79(1) | claim-right / duty | the claimant | the Secretary of State | the mobility component at the standard rate "if" (a) to (c); (a) is an age that regulations prescribe |
| 1374-1377 | s 79(2) | claim-right / duty | the claimant | the Secretary of State | the mobility component at the enhanced rate "if" (a) to (c) |
| 1378-1380 | s 79(3) | power / liability | the Secretary of State (by regulations) | the claimant | fixes the weekly rate of the mobility component |
| 1381 | s 79(4) | power / liability | the Secretary of State (by regulations) | the claimant | prescribes the mobility activities |
| 1385 | s 79(6) | condition on a claim-right | the claimant | the Secretary of State | subjects the claim-rights in s 79 to the rest of Part 4 |
| 1386 | s 79(7) | power / liability | the Secretary of State (by regulations) | the claimant | a power to remove the mobility component in prescribed circumstances: a disability on the claimant if used |
| 1388-1392 | s 80(1) | power / liability | the decision-maker, by regulations | the claimant | the four ability questions are decided in accordance with regulations; the claimant is liable to the answer |
| 1393-1401 | s 80 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | a duty to make regulations (their content, the required period condition, is s 81 and is encoded there); the content is in regulations that are not among the sources |
| 1402-1403 | s 80(5) | power / liability | the Secretary of State (by regulations) | the claimant | (a): a negative determination may be treated as made against a claimant who fails without good reason to comply |
| 1404-1405 | s 80 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power (what is a good reason); the content is in regulations that are not among the sources; regulation-making power (what is to be taken into account) |
| 1406-1408 | s 80(6) | none |  |  | defines "negative determination" for (5)(a) |
| 1410-1412 | s 81(1) | power / liability | the Secretary of State (by regulations) | the claimant | the required period condition must be decided by reference to the previous 3 and next 9 months (fork F-81-1) |
| 1413-1415 | s 81(2) | none |  |  | defines "the relevant ability" for the required period condition |
| 1417 | s 81(3)(a) | none |  |  | defines "assessed" |
| 1418 | s 81(3)(b) | none |  |  | defines "the previous 3 months" (fork F-81-2) |
| 1419 | s 81(3)(c) | none |  |  | defines "the next 9 months" (fork F-81-2) |
| 1420-1422 | s 81(4) | power / liability | the Secretary of State (by regulations) | the claimant | a power to decide the required period condition otherwise in prescribed cases |
| 1425-1427 | s 82(1) | none |  |  | says to whom s 82 applies: a person who is terminally ill and has claimed expressly on that ground |
| 1428 | s 82(2) | claim-right / duty | the claimant to whom s 82 applies | the Secretary of State | the daily living component at the enhanced rate; s 78(1) and (2) do not apply to such a person |
| 1429 | s 82(3) | immunity / disability | the claimant to whom s 82 applies | the Secretary of State | the required period condition of s 79(1)(c) and (2)(c) is not a condition the person can fail |
| 1430 | s 82(4) | none |  |  | defines "terminally ill" (fork F-82) |
| 1431-1434 | s 82(5) | power / liability | a person acting for another | the person for whom the claim is made | a claim made on behalf of another, expressly on the ground of terminal illness, is regarded as that person's own claim, despite lack of knowledge or authority |
| 1435 | s 82(6) | none |  |  | points "the enhanced rate" in s 82(2) at s 78(3) |
| 1437 | s 83(1) | disability / no-right | the claimant who has reached the relevant age | the Secretary of State | no claim-right to either component "for any period after" the person reaches the relevant age |
| 1438-1440 | s 83(2) | none |  |  | defines "the relevant age" (fork F-83) |
| 1441 | s 83(3) | power / liability | the Secretary of State (by regulations) | the claimant | exceptions to s 83(1) may be provided by regulations |
| 1443 | s 84(1) | disability / no-right | the claimant to whom a relevant EU Regulation applies | the Secretary of State | no claim-right to the daily living component "unless" the United Kingdom is competent for sickness benefits in cash |
| 1444-1446 | s 84(2) | none |  |  | names the two relevant EU Regulations |
| 1448 | s 85(1) | power / liability | the Secretary of State (by regulations) | the claimant who meets the s 85(2) condition | regulations may provide that no amount attributable to the daily living component is payable: a disability on the claimant if used |
| 1449 | s 85(2) | none |  |  | defines the condition (a care home resident whose services are publicly funded under a specified enactment) |
| 1450 | s 85(3) | none |  |  | defines "care home" |
| 1451-1455 | s 85(4) | none |  |  | defines "qualifying services" |
| 1456 | s 85(5) | none |  |  | defines "specified enactment" |
| 1457 | s 85 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power (power to specify by description); the description is an input of s 85(5); the content is in regulations that are not among the sources |
| 1458 | s 85(7) | none |  |  | defines "enactment" to include Scottish enactments |
| 1460-1462 | s 86(1) | power / liability | the Secretary of State (by regulations) | the claimant who meets the s 86(2) condition | regulations may bar either component for a hospital in-patient |
| 1463 | s 86(2) | none |  |  | defines the hospital in-patient condition |
| 1464 | s 86(3) | none |  |  | says the public-funds question is decided in accordance with the regulations |
| 1466 | s 87 | disability / no-right | the claimant in imprisonment or detention | the Secretary of State | no amount is payable for the period "except to the extent that regulations provide otherwise" |
| 1469 | s 88(1) | disability / no-right | the claimant | the Secretary of State | no claim-right for any period before the claim is made or treated as made |
| 1470 | s 88(2) | duty / claim-right | the person making the award (duty) | the claimant | an award must be for a fixed term unless that person considers it inappropriate; the claimant has no claim-right to any other term |
| 1471 | s 88(3) | duty / no-right | the person making the award (duty) | none for the claimant | a duty to have regard to guidance; the text gives no consequence for failing it |
| 1472 | s 88(4) | none |  |  | information supplied under Part 4 is information relating to social security |
| 1474-1476 | s 89 | duty / no-right | the Secretary of State (duty to lay a report) | none for the claimant | the claimant has no claim-right; a duty to Parliament |
| 1479 | s 90 | power exercised by Parliament | Parliament (exercised) | DLA claimants | repeals ss 71 to 76 of the Contributions and Benefits Act; the date of abolition is s 150(3) |
| 1481 | s 91 | none |  |  | amendment or machinery: introduces amendments of other Acts (Schedule 9); the amendments have their own rows |
| 1483-1486 | s 92 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power; the content is in regulations that are not among the sources |
| 1487-1489 | s 92(3) | none |  |  | defines "primary legislation" and "secondary legislation" for the power in (1) and (2) |
| 1491 | s 93 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power (transitional); the content is in regulations that are not among the sources |
| 1492 | s 93 | none |  |  | amendment or machinery: gives effect to Schedule 10 (transitional); Schedule 10 has its own rows |
| 1494-1508 | s 94 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power and its procedure; the content is in regulations that are not among the sources |
| 1511 | s 95 "adult disability payment" | none |  |  | a definition for Part 4 |
| 1512 | s 95 "child disability payment" | none |  |  | a definition for Part 4 |
| 1513 | s 95 "daily living activities" | none |  |  | a definition for Part 4 |
| 1514 | s 95 "daily living component" | none |  |  | a definition for Part 4 |
| 1515 | s 95 "mobility activities" | none |  |  | a definition for Part 4 |
| 1516 | s 95 "mobility component" | none |  |  | a definition for Part 4 |
| 1517 | s 95 "pension age disability payment" | none |  |  | a definition for Part 4 |
| 1518 | s 95 "prescribed" | none |  |  | a definition for Part 4 |
| 1519 | s 95 "Scottish adult disability living allowance" | none |  |  | a definition for Part 4 |
| 2478 | s 135 | none |  |  | amendment or machinery: amendment lead-in (Registration Service Act 1953) |
| 2480-2483 | s 135 RSA 19A(1) | power / liability | registrars and the Registrar General (functions) | persons whose births are registered | the power to transmit and verify birth information for the Tell Us Once service |
| 2484-2486 | s 135 RSA 19A(2) | none |  |  | describes the service in (1) |
| 2487 | s 135 RSA 19A(3) | none |  |  | extends references to the Secretary of State to the service's providers |
| 2488-2490 | s 135 RSA 19A(4) | immunity | persons whose information is held | the registrars and the Secretary of State | the section does not authorise a disclosure that is unlawful by an enactment or by the law of confidentiality or privacy |
| 2493 | s 136 | none |  |  | amendment or machinery: amendment lead-in (Child Support Act 1991 section 9) |
| 2494-2496 | s 136(2A) | privilege / no-right | the Secretary of State | applicants | steps to encourage maintenance agreements and, before accepting an application, an invitation to consider one; no corresponding duty on the applicant |
| 2497 | s 136 | none |  |  | amendment or machinery: amendment lead-in (Child Maintenance and Other Payments Act 2008 Schedule 5) |
| 2498 | s 136(3) | privilege / no-right | the Secretary of State | applicants in transferred cases | the same invitation power for transferred cases |
| 2500-2503 | s 137 | none |  |  | amendment or machinery: amendment lead-in (Child Support Act 1991); amendment lead-in and repeal of words in CSA 4(2) |
| 2504-2506 | s 137(2A) | disability / immunity | the Secretary of State (disabled) | the non-resident parent (immune) | the Secretary of State "may only" make collection arrangements under s 4(2)(a) if the parent agrees or payment is unlikely without them |
| 2507-2509 | s 137 | none |  |  | amendment or machinery: amendment lead-in and a substitution of words in CSA 7(3) |
| 2510-2512 | s 137(3A) | disability / immunity | the Secretary of State (disabled) | the non-resident parent (immune) | the same for s 7(3)(a) |
| 2513 | s 137(4) | condition on a power | the Secretary of State | the paying parent | makes the collection power in s 29(1) subject to ss 4(2A) and 7(3A) |
| 2515 | s 138 | none |  |  | amendment or machinery: amendment lead-in (Child Support Act 1991, new section 9A) |
| 2517 | s 138 CSA 9A(1) | privilege / power | a person with care or a non-resident parent | the Secretary of State | may apply for an indicative calculation |
| 2518 | s 138 CSA 9A(2) | privilege / power | a qualifying child aged 12 or over, habitually resident in Scotland | the Secretary of State | may apply for an indicative calculation about themselves |
| 2519 | s 138 CSA 9A(3) | none |  |  | defines "indicative calculation" |
| 2520 | s 138 CSA 9A(4) | immunity | every person | the claimant of maintenance | an indicative calculation creates no liability to pay child support maintenance |
| 2521 | s 138 CSA 9A(5) | power / liability | the Secretary of State | applicants | a power to limit the number of applications accepted in a case |
| 2522 | s 138 CSA 9A(6) | disability / immunity | the Secretary of State (disabled) | the person alleged to be the parent (immune) | no calculation on the assumption of parentage if the person denies it, unless Case A3(b) applies |
| 2524 | s 139 | none |  |  | amendment or machinery: amendment lead-in (Child Support Act 1991 section 43) |
| 2525 | s 139(1) | power / liability | the Secretary of State (by regulations) | non-resident parents | the SSAA 5(1)(p) power may be used to secure child support maintenance payments by deduction from benefit |
| 2526-2528 | s 139(2) | none |  |  | extends (1) to arrears and to fees under CMOPA s 6 |
| 2530-2534 | s 140 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amends the regulation-making power in section 6(2) of the Child Maintenance and Other Payments Act 2008 (fees); paragraph (h) is itself a power to make regulations; the content is in regulations that are not among the sources |
| 2536 | s 141 | none |  |  | amendment or machinery: amendment lead-in (Child Maintenance and Other Payments Act 2008 section 6) |
| 2537 | s 141(3A) | duty / no-right | the Secretary of State | none for the individual | a duty to review the effect of the first fees regulations |
| 2538 | s 141(3B) | duty / no-right | the Secretary of State | none for the individual | the review must take place within 30 months of the regulations coming into force |
| 2539-2541 | s 141(3C) | duty / no-right | the Secretary of State | none for the individual | a duty to make and publish a report |
| 2542 | s 141(3D) | duty / no-right | the Secretary of State | none for the individual | a duty to lay the report before Parliament |
| 2544 | s 142 | none |  |  | amendment or machinery: amendment lead-in (Insolvency Act 1986 section 382) |
| 2545 | s 142(5) | immunity | a person liable to pay child support maintenance | creditors under Part 8 of the Insolvency Act 1986 | the liability is not a debt or liability for Part 8 (it is outside an individual voluntary arrangement) |
| 2546 | s 142 | none |  |  | amendment or machinery: amends a section heading in the Insolvency Act 1986 |
| 2549 | s 143 | none |  |  | amendment or machinery: repeal of section 81 of the Social Security Act 1998 |
| 2552 | s 144 | none |  |  | amendment or machinery: amendment lead-in (Employment and Training Act 1973, new section 2A) |
| 2554 | s 144 ETA 2A(1) | disability / immunity | the Secretary of State (disabled) | employers and jobseekers | section 2 arrangements may not include employment for sexual purposes |
| 2555-2557 | s 144 ETA 2A(2) | none |  |  | defines "employment for sexual purposes" |
| 2558 | s 144 ETA 2A(3) | power / liability | the Secretary of State (by order) | employers and jobseekers | a power to specify exceptions to (1) |
| 2559 | s 144 | none |  |  | amendment or machinery: procedure for an order (annulment by resolution) |
| 2562 | s 145 | none |  |  | amendment or machinery: signpost to Schedule 13 (establishing a body); Schedule 13 has its own rows |
| 2564-2578 | s 146 | none |  |  | amendment or machinery: amendment lead-in (Child Poverty Act 2010 section 9); amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(i); amendment of wording in the Child Poverty Act 2010 section 9(7)(a)(ii) |
| 2581 | s 147 | none |  |  | amendment or machinery: signpost to Schedule 14 (repeals); Schedule 14 has its own rows |
| 2583-2586 | s 148 | duty / no-right | Parliament (money provided) | none for the individual | sums paid by way of universal credit or personal independence payment, and the expenditure the Act causes, are paid out of money provided by Parliament |
| 2588-2598 | s 149 | none |  |  | amendment or machinery: extent |
| 2600-2618 | s 150 | none |  |  | amendment or machinery: the Act's own commencement (on the day it is passed); the Act's own commencement (two months after the day it is passed) |
| 2619 | s 150(3) | power / liability | the Secretary of State (by order) | every person the remaining provisions affect | the day on which the remaining provisions come into force |
| 2620-2627 | s 150 | none |  |  | amendment or machinery: the Act's own commencement (what an order under (3) may do) |
| 2629 | s 151 | none |  |  | amendment or machinery: short title |
| 3004 | Sch 4 State Pension Credit Act 2002 | none |  |  | amendment or machinery: amendment lead-in (State Pension Credit Act 2002) |
| 3005-3007 | Sch 4 State Pension Credit Act 2002 | condition on a claim-right | a state pension credit claimant | the Secretary of State | adds the housing credit conditions to s 1(2)(c) of the 2002 Act |
| 3008-3012 | Sch 4 State Pension Credit Act 2002 | claim-right / duty | a state pension credit claimant | the Secretary of State | a housing credit "if he satisfies the conditions in subsections (1) and (2)"; more than one credit if the relevant conditions are satisfied |
| 3013 | Sch 4 State Pension Credit Act 2002 | none |  |  | amendment or machinery: amendment lead-in (new section 3A) |
| 3015 | Sch 4 State Pension Credit Act 2002 (1) | condition on a claim-right | a state pension credit claimant | the Secretary of State | liable to make payments in respect of the accommodation occupied as the home |
| 3016 | Sch 4 State Pension Credit Act 2002 (2) | condition on a claim-right | a state pension credit claimant | the Secretary of State | the housing credit payable would not be less than a prescribed amount |
| 3017 | Sch 4 State Pension Credit Act 2002 (3) | power / liability | the Secretary of State (by regulations) | the claimant | the amount is calculated in or determined under regulations (which may be zero) |
| 3018-3021 | Sch 4 State Pension Credit Act 2002 (4) | none |  |  | what counts as accommodation for (1): in Great Britain, residential, whole or part of a building immaterial |
| 3022-3027 | Sch 4 State Pension Credit Act 2002 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power; the content is in regulations that are not among the sources |
| 3028 | Sch 4 State Pension Credit Act 2002 | none |  |  | amendment or machinery: amendment lead-in (State Pension Credit Act 2002 section 7) |
| 3029 | Sch 4 State Pension Credit Act 2002 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power; the content is in regulations that are not among the sources |
| 3030-3031 | Sch 4 State Pension Credit Act 2002 | none |  |  | amendment or machinery: amendment of State Pension Credit Act 2002 section 12(2)(b) (words inserted); amendment lead-in (State Pension Credit Act 2002 section 17) |
| 3032 | Sch 4 State Pension Credit Act 2002 | none |  |  | a cross-reference definition ("housing credit") |
| 3033 | Sch 4 State Pension Credit Act 2002 | none |  |  | amendment or machinery: repeal in the State Pension Credit Act 2002 Schedule 2 |
| 3036-3037 | Sch 4 Social Security Administration Act 1992 | none |  |  | amendment or machinery: amendment lead-in (Social Security Administration Act 1992); amendment of section 5(6) of the Social Security Administration Act 1992 (words inserted) |
| 3038 | Sch 4 Social Security Administration Act 1992 | none |  |  | a line of dots: the text shows a blank paragraph (a provision omitted from this rendering) |
| 3039-3042 | Sch 4 Social Security Administration Act 1992 | none |  |  | amendment or machinery: amendment lead-in (Social Security Administration Act 1992 section 122F); amendment of section 122F(3)(a) (words inserted); amendment of section 122F(4) (words inserted) |
| 3043 | Sch 4 Social Security Administration Act 1992 (5) | none |  |  | a cross-reference definition ("housing credit") |
| 3045-3047 | Sch 4 Housing Act 1996 | none |  |  | amendment or machinery: amendment lead-in (Housing Act 1996 section 122); amendment of a section heading; amendment of section 122(1) (words inserted) |
| 3049 | Sch 4 Child Support, Pensions and Social Security Act 2000 | none |  |  | amendment or machinery: amendment of section 69(1)(a) of the Child Support, Pensions and Social Security Act 2000 (words inserted) |
| 3239-3240 | Sch 9 Transport Act 1982 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3242 | Sch 9 Child Support Act 1991 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3244-3249 | Sch 9 Social Security Contributions and Benefits Act 1992 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3250-3252 | Sch 9 Social Security Contributions and Benefits Act 1992 (1A) | none |  |  | lists the allowances within the attendance allowance provision (PIP and the care component of DLA) |
| 3253-3254 | Sch 9 Social Security Contributions and Benefits Act 1992 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3256-3268 | Sch 9 Social Security Administration Act 1992 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3269 | Sch 9 Social Security Administration Act 1992 (6) | condition on a claim-right | a benefit claimant | the Secretary of State | personal independence payment is treated as benefit for the overlapping-benefits rule in SSAA s 73 |
| 3270-3305 | Sch 9 Social Security Administration Act 1992 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3306-3307 | Sch 9 Social Security Administration Act 1992 | none |  |  | a limb of the list in section 187(1) of the Social Security Administration Act 1992, which the text titles "inalienability"; the lead-in is not printed |
| 3308-3311 | Sch 9 Social Security Administration Act 1992 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3313-3317 | Sch 9 Social Security (Recovery of Benefits) Act 1997 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3319-3337 | Sch 9 Social Security Act 1998 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3338-3339 | Sch 9 Social Security Act 1998 | power / liability | a claimant | the decision-maker | an appeal lies against decisions as to regulations under ss 85(1) and 86(1) and as to s 87 (fork F-sch9-1) |
| 3341-3343 | Sch 9 Immigration and Asylum Act 1999 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3345-3346 | Sch 9 Social Security Fraud Act 2001 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3347-3348 | Sch 9 Social Security Fraud Act 2001 | none |  |  | a limb of "disqualifying benefit" |
| 3349-3350 | Sch 9 Social Security Fraud Act 2001 | none |  |  | a limb of "sanctionable benefit" |
| 3351-3352 | Sch 9 Social Security Fraud Act 2001 | none |  |  | a limb of the benefits to which the power in SSFA s 10 applies |
| 3354 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | none |  |  | amendment or machinery: amendment of another Act: adds personal independence payment (or Part 4) to a list or cross-reference whose host text is not among the sources |
| 3355 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | none |  |  | the text shows a blank where the inserted entry would be (the inserted table row is missing from this rendering) |
| 3356 | Sch 9 Income Tax (Earnings and Pensions) Act 2003 | none |  |  | the text shows a blank where the inserted entry would be (the inserted abbreviation is missing from this rendering) |
| 3359 | Sch 10 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power (regulations under section 93 may in particular make provision ...); the content is in regulations that are not among the sources |
| 3360 | Sch 10 (2) | none |  |  | defines "the appointed day" for Schedule 10 |
| 3362-3392 | Sch 10 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | regulation-making power: says what regulations under section 93 may in particular provide; the claims, awards and transitions are made by regulations that are not among the sources; the content is in regulations that are not among the sources |
| 3395-3397 | Sch 11 Vaccine Damage Payments Act 1979 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3398 | Sch 11 Vaccine Damage Payments Act 1979 (1B) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | VDPA 4(1B): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3399-3402 | Sch 11 Vaccine Damage Payments Act 1979 (1C) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3403 | Sch 11 Vaccine Damage Payments Act 1979 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3404 | Sch 11 Vaccine Damage Payments Act 1979 | privilege / power | the Secretary of State (by regulations) | a person whose appeal is barred | regulations may let a purported appeal be treated as an application for revision or reversal |
| 3405-3417 | Sch 11 Vaccine Damage Payments Act 1979 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3419-3421 | Sch 11 Child Support Act 1991 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3422 | Sch 11 Child Support Act 1991 (2A) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | CSA 20(2A): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3423-3426 | Sch 11 Child Support Act 1991 (2B) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3427 | Sch 11 Child Support Act 1991 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3428 | Sch 11 Child Support Act 1991 | privilege / power | the Secretary of State (by regulations) | a person whose appeal is barred | regulations may let a purported appeal be treated as an application for revision or reversal |
| 3429-3430 | Sch 11 Child Support Act 1991 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3431 | Sch 11 Child Support Act 1991 (3A) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | CSA 20(3A): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3432-3435 | Sch 11 Child Support Act 1991 (3B) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3436 | Sch 11 Child Support Act 1991 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3437 | Sch 11 Child Support Act 1991 | privilege / power | the Secretary of State (by regulations) | a person whose appeal is barred | regulations may let a purported appeal be treated as an application for revision or reversal |
| 3438-3442 | Sch 11 Child Support Act 1991 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3444-3446 | Sch 11 Social Security (Recovery of Benefits) Act 1997 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3447 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2A) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | SSRBA 11(2A): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3448-3451 | Sch 11 Social Security (Recovery of Benefits) Act 1997 (2B) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3452-3456 | Sch 11 Social Security (Recovery of Benefits) Act 1997 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3458-3462 | Sch 11 Child Support, Pensions and Social Security Act 2000 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3463 | Sch 11 Child Support, Pensions and Social Security Act 2000 (5A) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | CSPSSA Sch 7 para 6(5A): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3464-3467 | Sch 11 Child Support, Pensions and Social Security Act 2000 (5B) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3468-3470 | Sch 11 Child Support, Pensions and Social Security Act 2000 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3471 | Sch 11 Child Support, Pensions and Social Security Act 2000 | privilege / power | the Secretary of State (by regulations) | a person whose appeal is barred | regulations may let a purported appeal be treated as an application for revision or reversal |
| 3472 | Sch 11 Child Support, Pensions and Social Security Act 2000 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3474-3477 | Sch 11 Child Maintenance and Other Payments Act 2008 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3478 | Sch 11 Child Maintenance and Other Payments Act 2008 (1A) | power / liability | the Secretary of State (by regulations) | the claimant or person affected | CMOPA 50(1A): regulations may make a right of appeal depend on the earlier step (a disability on the claimant if used) |
| 3479-3482 | Sch 11 Child Maintenance and Other Payments Act 2008 (1B) | none |  |  | what the regulations may count as the earlier step having been taken |
| 3483-3492 | Sch 11 Child Maintenance and Other Payments Act 2008 | power / liability | the Secretary of State (by regulations) | persons the regulations will bind | amendment of another Act or procedure for regulations (lead-in, annulment or approval of instruments, power to make regulations, or words inserted into a host provision whose text is not printed); the content is in regulations that are not among the sources |
| 3495-3496 | Sch 12 Child Support Act 1991 | none |  |  | amendment or machinery: amendment lead-in; amendment lead-in (Child Support Act 1991 section 17) |
| 3497-3499 | Sch 12 Child Support Act 1991 (2) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3500 | Sch 12 Child Support Act 1991 | none |  |  | amendment or machinery: amendment lead-in (new subsection (6)) |
| 3502 | Sch 12 Child Support Act 1991 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3503 | Sch 12 Child Support Act 1991 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3504 | Sch 12 Child Support Act 1991 | none |  |  | amendment or machinery: amendment lead-in (Child Support Act 1991 Schedule 4C) |
| 3505 | Sch 12 Child Support Act 1991 (2) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3506 | Sch 12 Child Support Act 1991 (3) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3507 | Sch 12 Child Support Act 1991 | none |  |  | amendment or machinery: amendment lead-in (new sub-paragraph (3)) |
| 3508 | Sch 12 Child Support Act 1991 (3) | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3510 | Sch 12 Social Security Act 1998 | none |  |  | amendment or machinery: amendment lead-in (Social Security Act 1998 section 10) |
| 3511-3512 | Sch 12 Social Security Act 1998 (2) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3513 | Sch 12 Social Security Act 1998 | none |  |  | amendment or machinery: amendment lead-in (new subsection (7)) |
| 3515 | Sch 12 Social Security Act 1998 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3516 | Sch 12 Social Security Act 1998 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3518 | Sch 12 Child Support, Pensions and Social Security Act 2000 | none |  |  | amendment or machinery: amendment lead-in (Child Support, Pensions and Social Security Act 2000 Schedule 7 paragraph 4) |
| 3519-3520 | Sch 12 Child Support, Pensions and Social Security Act 2000 (2) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3521-3523 | Sch 12 Child Support, Pensions and Social Security Act 2000 (3) | power / liability | the decision-maker | a person whose appeal tribunal or Commissioner decision is in issue | adds the decisions of the former appellate bodies to the decisions that may be superseded (fork F-sch12-1) |
| 3524 | Sch 12 Child Support, Pensions and Social Security Act 2000 | none |  |  | amendment or machinery: amendment lead-in (new sub-paragraph (7)) |
| 3526 | Sch 12 Child Support, Pensions and Social Security Act 2000 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3527 | Sch 12 Child Support, Pensions and Social Security Act 2000 | none |  |  | defines "appeal tribunal" or "Commissioner" (and says where their functions went) |
| 3530-3531 | Sch 13 | none |  |  | amendment or machinery: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 3534 | Sch 13 (1) | none |  |  | names the body and the short form "the Commission" |
| 3535-3630 | Sch 13 | none |  |  | amendment or machinery: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 3631 | Sch 13 (2) | none |  |  | changes the name in the definition of "the Commission" |
| 3632 | Sch 13 | none |  |  | amendment or machinery: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 3633 | Sch 13 | none |  |  | borrows the meaning of "Minister of the Crown" |
| 3634 | Sch 13 | none |  |  | amendment or machinery: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 3635 | Sch 13 (3) | power / liability | a Minister of the Crown (by order, with the Northern Ireland Assembly's consent) | the Commission and the Northern Ireland departments | appoints the "appointed day for Northern Ireland" |
| 3636-3656 | Sch 13 | none |  |  | amendment or machinery: establishes, staffs and funds a body, gives it functions, or amends another Act to list it (boards and offices and their staffing; amendments of other Acts) |
| 3659-3959 | Sch 14 | none |  |  | amendment or machinery: repeal of enactments of other Acts, consequential on this Act (the Act column of the table is lost in this text) |

## Marginal readings for a lawyer (wra3)

The rule of 2026-10-29 is assumed here, not ruled by a lawyer.
Two readings are the status quo of this encoding and are for a lawyer to confirm: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Every branch that rests on one is listed here, with the other reading.

### Reading (a): a failed "if" is taken as the text's no (the branch answers `JUST FALSE`)

| provision | functions | the reading taken | the other reading |
| --- | --- | --- | --- |
| s 78(1), s 78(2) | `s 78(1) the person is entitled to the daily living component at the standard rate` (wra3-pt4-s77-84.l4); `s 78(2) the person is entitled to the daily living component at the enhanced rate` (wra3-pt4-s77-84.l4) | a person who fails limb (a) or (b) is not entitled: "is entitled ... if" is read as the whole test | `NOTHING`: the Act says when a person is entitled and does not say in terms that a person who fails is not |
| s 79(1), s 79(2), including the age limb (a) | `s 79(1) the person is entitled to the mobility component at the standard rate` (wra3-pt4-s77-84.l4); `s 79(2) the person is entitled to the mobility component at the enhanced rate` (wra3-pt4-s77-84.l4); `s 79(1)(a) the person is of or over the age prescribed` (wra3-pt4-s77-84.l4); `s 79(2)(a) the person is of or over the age prescribed` (wra3-pt4-s77-84.l4) | a person who fails a limb, or is under the age regulations prescribe, is not entitled | `NOTHING`, as for s 78 |
| s 81(1) (fork F-81-1) | `s 81(1) the person meets the required period condition on the usual test` (wra3-pt4-s77-84.l4) | either limb failing means the condition is not met | `NOTHING`: the subsection directs the regulations and states no test of its own |
| s 82(4) | `s 82(4) the person is terminally ill at the time` (wra3-pt4-s77-84.l4) | "is terminally ill at any time if" the conditions hold: a person who does not meet them is not terminally ill | `NOTHING`: a definition by "if" without "means" or "only if" |
| s 85(2), s 86(2) | `s 85(2) the person meets the condition` (wra3-pt4-s85-90.l4); `s 86(2) the person meets the condition` (wra3-pt4-s85-90.l4) | "The condition is that ..." is closed: a person who fails a limb does not meet it | `NOTHING`: "is that" is not "means" or "only if" |
| s 137(2), s 137(3) | `s 137(2) CSA 4(2A) the Secretary of State may make arrangements under section 4(2)(a)` (wra3-pt6-misc.l4); `s 137(3) CSA 7(3A) the Secretary of State may make arrangements under section 7(3)(a)` (wra3-pt6-misc.l4) | "may only ... if" with neither limb: the Secretary of State may not (the "only" already says no; listed because the plan lists the same shape under seam 8) | `NOTHING`, if "may only ... if" is read as a condition on a power whose source is outside the sources |
| s 144 ETA 2A(2) | `s 144 ETA 2A(2) the employment is employment for sexual purposes` (wra3-pt6-misc.l4) | "employment is for sexual purposes if (a) ... and (b) ...": a failed limb means it is not | `NOTHING`: "if" without "means" or "only if" |
| s 150(3), seam 10 | `s 150(3) the provision is in force on the date` (wra3-pt7-final.l4) | a date before the appointed day is not a date on which the provision is in force | `NOTHING`: the text says only that the provisions "come into force on such day" |
| Sch 4: SPCA 3A(1), 3A(2), 3A(4)(a) and (b), SPCA 1(2)(c)(iii), SPCA 1(3)(c) | `sch 4 para 4 SPCA 3A(1) the first condition for housing credit is met` (wra3-sch4.l4); `sch 4 para 4 SPCA 3A(2) the second condition for housing credit is met` (wra3-sch4.l4); `sch 4 para 4 SPCA 3A(4) the accommodation is accommodation for the purposes of subsection (1)` (wra3-sch4.l4); `sch 4 para 2 SPCA 1(2)(c)(iii) the claimant satisfies the conditions in section 3A(1) and (2)` (wra3-sch4.l4); `sch 4 para 3 SPCA 1(3)(c) the claimant is entitled to a housing credit` (wra3-sch4.l4) | a condition that fails, or accommodation that "must be" in Great Britain and residential but is not, means the condition is not met and housing credit is not due | `NOTHING`: "is that" and "must be" without "only if" or "unless" |
| Sch 11, every host Act (the shared reading of seam 8) | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4) | regulations require consideration first, it has not been done (or the further conditions are unmet): there is no right of appeal ("only if") | `NOTHING`: "only if" states a necessary condition, so a failed "only if" says no to this route only (listed because the plan lists it) |

One consequence of reading (a) to say outright: a `JUST TRUE` answer from a function named "... is not barred ..." means only that this one bar does not apply.
It never means that the person is entitled or that the amount is payable.

### Reading (b): a grant or prohibition limited by its own wording is not extended (the branch answers `NOTHING`)

The other reading of each row is `JUST FALSE` for a case outside the limit.

| provision | function | the limit in the text |
| --- | --- | --- |
| s 80(5)(a) | `s 80(5)(a) a negative determination is treated as made against the person` (wra3-pt4-s77-84.l4) | the provision reaches only a person who "fails without a good reason to comply"; the text is silent on anyone else |
| s 82(1) | `s 82(1) this section applies to the person` (wra3-pt4-s77-84.l4) | the section "applies to a person who ... has made a claim ... expressly on the ground of terminal illness"; the text is silent on anyone else |
| s 82(1) | `s 82(1) this section applies to the person` (wra3-pt4-s77-84.l4) | the section "applies to a person who is terminally ill"; the text is silent on anyone else |
| s 82(2) | `s 82(2) the person is entitled to the daily living component at the enhanced rate` (wra3-pt4-s77-84.l4) | the grant is to "a person to whom this section applies" |
| s 82(2) | `s 82(2) section 78(1) and (2) apply to the person` (wra3-pt4-s77-84.l4) | the sentence is about "such a person", a person to whom the section applies |
| s 82(2) | `s 82(2) the person is entitled to the daily living component at the enhanced rate, section 82 displacing section 78(2)` (wra3-pt4-s77-84.l4) | section 82(2) says nothing where the section does not apply, so the result under section 78(2) stands |
| s 82(2) | `s 82(2) the result under section 78(1), section 82 displacing section 78(1)` (wra3-pt4-s77-84.l4) | the sentence is about "such a person", a person to whom the section applies; for anyone else the result under section 78(1) stands |
| s 82(3) | `s 82(3) the required period condition of section 79(1)(c) and (2)(c) applies to the person` (wra3-pt4-s77-84.l4) | the sentence is about "a person to whom this section applies" |
| s 82(3) | `s 82(3) the required period condition limb of section 79(1)(c) and (2)(c), as it stands for the person` (wra3-pt4-s77-84.l4) | section 82(3) is about "a person to whom this section applies"; for anyone else the limb stands as the caller's result |
| s 82(5) | `s 82(5) the person on whose behalf the claim purports to be made is regarded as making the claim` (wra3-pt4-s77-84.l4) | the deeming is for a claim made on behalf of another "expressly on the ground" of terminal illness |
| s 88(4) | `s 88(4) the information is information relating to social security` (wra3-pt4-s85-90.l4) | the deeming is for "Information supplied under this Part"; the text is silent on other information |
| s 136(1) CSA 9(2A)(a) | `s 136(1) CSA 9(2A)(a) the Secretary of State may take the step` (wra3-pt6-misc.l4) | the power is to take "such steps as the Secretary of State considers appropriate"; the text is silent on a step the Secretary of State does not consider appropriate |
| s 136(1) CSA 9(2A)(b) | `s 136(1) CSA 9(2A)(b) the Secretary of State may invite the applicant to consider whether it is possible to make a maintenance agreement` (wra3-pt6-misc.l4) | the invitation is "before accepting an application"; the text is silent on one made after acceptance |
| s 136(2) CMOPA | `s 136(2) CMOPA Sch 5 para 3(3) the Secretary of State may invite the applicant to consider whether it is possible to make a maintenance agreement` (wra3-pt6-misc.l4) | the invitation is "before accepting an application required by provision under sub-paragraph (2)(b)"; the text is silent on any other |
| s 137(4) CSA 29(1) | `s 137(4) CSA 29(1) the Secretary of State may make the arrangement for collection, subject to sections 4(2A) and 7(3A)` (wra3-pt6-misc.l4) | the amendment makes the power "subject to section 4(2A) and 7(3A)" only; it says nothing about any other arrangement |
| s 138 CSA 9A(1) | `s 138 CSA 9A(1) the person may apply for an indicative calculation` (wra3-pt6-misc.l4) | the grant is to a person with care "in relation to any qualifying child" |
| s 138 CSA 9A(1) | `s 138 CSA 9A(1) the person may apply for an indicative calculation` (wra3-pt6-misc.l4) | the grant is to a non-resident parent "in relation to any qualifying child" |
| s 138 CSA 9A(2) | `s 138 CSA 9A(2) the child may apply for an indicative calculation with respect to themselves` (wra3-pt6-misc.l4) | the grant is to "A qualifying child who has attained the age of 12 years and is habitually resident in Scotland"; the text is silent on any other child |
| s 138 CSA 9A(5) | `s 138 CSA 9A(5) the application is not barred by a limit on the number of applications` (wra3-pt6-misc.l4) | the limit is set "in such manner as the Secretary of State thinks fit", so what happens at the limit is not stated (a lawyer's reading (b); the other reading is JUST FALSE) |
| sch 11 | `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4) | the provision is for a case "where ... there is no right of appeal against a decision" |
| sch 11 para 2(2) VDPA 4(1B) | `sch 11 para 2(2) VDPA 4(1B) there is a right of appeal against the decision` (wra3-sch11.l4) | the power is given "If the claimant's address is not in Northern Ireland"; the text is silent on a claimant whose address is |
| sch 9 para 11 SSAA 73(6) | `sch 9 para 11 SSAA 73(6) the benefit is treated for the purposes of section 73 as if it were benefit as defined in section 122 of the Contributions and Benefits Act` (wra3-sch9.l4) | the deeming is for "Personal independence payment"; the subsection is silent on any other benefit |

That is 22 branches in 20 functions.

### Reading a result: FALSE and NOTHING (wra3)

The rule of 2026-10-29 is assumed here, not ruled by a lawyer.
In this part a function answers `JUST FALSE` only where the Act says no in its own words: a definition that says "means" (s 92(3), s 95), a bar introduced by "not entitled", "no amount ... is payable" or "shall not" (ss 77(3) and (4), 83(1), 84(1), 87, 88(1)), a deeming sentence that says "do not apply" (s 82(2) and (3)), or an "if" the section sets as the test (the lawyer's reading (a) above).
A function answers `NOTHING` ("not covered") where the text is silent, lists without closing the list, says "includes", leaves a term or a figure to regulations or to another Act that is not among the sources, or limits a grant or a prohibition in its own wording and the case lies outside the limit (reading (b) above).
Take three cases in the Act's own terms.
For a person in custody, the s 87 function ("the amount is not barred as payable") gives `JUST FALSE` when no regulations provide otherwise, because the section says "no amount ... is payable" for the period of custody; it gives `NOTHING` when whether regulations provide otherwise is not known, because the section yields "to the extent that regulations provide otherwise".
A claimant who is not terminally ill gets `NOTHING` from s 82(2), not `JUST FALSE`: the section grants the enhanced daily living component to "a person to whom this section applies" and says nothing about anyone else, so the claimant's entitlement is whatever ss 78 and 79 say.
For a care home resident, the s 85(1) function ("the amount is not barred as payable") gives `JUST TRUE` when the regulations do not provide for the bar, because the bar exists only if regulations so provide; and `NOTHING` when whether they provide is not known, because that is outside the text.
A caller must never turn `NOTHING` into `FALSE`: it means the text does not decide the case, not that the answer is no.
Every branch that answers `JUST FALSE` carries a `FALSE-kind` comment, and every branch that answers `NOTHING` carries a `NOTHING-kind` comment on its own line or the line above, with one exception that is not a gap: three `WHEN NOTHING THEN NOTHING` lines (s 82(2) twice and s 82(3)) pass an unknown input through, and share the comment of the `WHEN JUST FALSE THEN NOTHING` line above them.
Checked on 2026-11-04 by an awk pass over the layer-1 modules: 97 lines that answer `NOTHING`, 94 with the comment on the line itself or the line above, and the 3 passthroughs.
The seat layer returns the layer-1 result unchanged, so its answers are the same three values, and each question's `@desc` says which scope its answer claims.

## Seams (wra3)

A seam is a provision in one part whose answer another part needs; the lead wires it at the merge (`inputs/PLAN.md` section 8).

| seam | what I took or gave | the name |
| --- | --- | --- |
| 7 (SSFA 6A, the lists of disqualifying and sanctionable benefit) | I encode only my own limbs, Sch 9 para 46, the two limbs (ca) (raw lines 3346-3350), and answer `NOTHING` for a benefit another part's limb names; the plan's row 7 names wra1 and wra4 as the other limbs and does not name mine, so the lead's composite takes these two functions as well | `sch 9 para 46 SSFA 6A(1) disqualifying benefit (ca) the benefit is within the limb` (wra3-sch9.l4); `sch 9 para 46 SSFA 6A(1) sanctionable benefit (ca) the benefit is within the limb` (wra3-sch9.l4) |
| found, not in the plan: SSFA 10(3) | Sch 9 para 47 adds (be) (raw lines 3351-3353) to the list that Schedule 2 (wra1, raw line 2909) adds (bc) to; same treatment as seam 7 | `sch 9 para 47 SSFA 10(3)(be) the benefit is within the limb` (wra3-sch9.l4) |
| found, not in the plan: SSAA 187(1) | Sch 9 para 31 adds (ad) personal independence payment (raw lines 3306-3307) to the list that Schedule 2 (raw line 2794) adds (za) universal credit to; same treatment | `sch 9 para 31 SSAA 187(1)(ad) the benefit is within the limb` (wra3-sch9.l4) |
| 8 (the shared reading of consideration of revision before appeal) | Sch 11 uses the shared reading as the plan states it: the regulations' requirement is a `MAYBE BOOLEAN` input, consideration done is a `BOOLEAN`; `NOTHING` or `JUST FALSE` for the requirement gives `NOTHING`; a requirement with no consideration gives `JUST FALSE`; consideration done gives `NOTHING`. Two things the plan does not state: a third input, "the consideration satisfied the further conditions the regulations specify" (the Act lets regulations say the condition is met "only where" the consideration was on an application, the issues were of a specified description, or another specified condition is satisfied), which the lead can set to `TRUE` if wra4's section has no such limb; and a gate for the Vaccine Damage Payments Act, whose power is given only "If the claimant's address is not in Northern Ireland" | `sch 11 there is a right of appeal, on the shared reading of the requirement of consideration first` (wra3-sch11.l4); `sch 11 a purported appeal may be treated as an application for revision, on the shared reading` (wra3-sch11.l4); `sch 11 para 2(2) VDPA 4(1B) there is a right of appeal against the decision` (wra3-sch11.l4) |
| 10 (the appointed day) | The plan names the function "... of section 1"; mine is `s 150(3) the day appointed for the coming into force of the provision`, which takes the day appointed for the provision concerned in the area concerned as a `MAYBE DATE` and returns it, so wra1 and wra2 call it with their own provision's day. Schedule 10 takes the day for section 77 as an input | `s 150(3) the day appointed for the coming into force of the provision` (wra3-pt7-final.l4); `sch 10 para 1(2) the appointed day` (wra3-sch10.l4) |
| found, not in the plan: s 103(2) | Schedule 12 is in my range and s 103 is in wra4's (raw lines 1660-1664): s 103(2) says the amendments of Schedule 12 "have effect as if they had come into force on 3 November 2008", so no function of mine says when they took effect, and a caller who needs that date reads it from s 103(2). I did not encode the retrospective date because it is wra4's provision | |

Two things the plan lists as not seams and I did not connect: the pensionable-age question in s 83(2) is asked as its own `BOOLEAN`, and wra4's "couple" in s 96(10) is not used.

## What the text turns out to say (numbered findings)

1. The source is a converter rendering of the version of 2026-07-01 and carries later amendments; it is not the official text.
2. The file ends at line 3959; line 3960, where the brief and the plan put the end of my last range, does not exist.
3. Schedule 14 (raw lines 3657-3959) is a run of repeals whose "Act" column is lost: entries read "In section 53(3)—" with no Act named, and the headings of its Parts are the only structure left (the last is "Part 14 — Standards of decision-making", line 3956).
   Every Schedule 14 row is therefore `inert` under reason 2, and nothing says which Act a repeal belongs to.
4. Three lines show a blank: raw line 3038 (a line of dots in Schedule 4) and raw lines 3355 and 3356 (the inserted entries in Schedule 9's amendment of the Income Tax (Earnings and Pensions) Act 2003 are missing).
5. The paragraph numbers of Schedules 4, 9, 10, 11 and 12 are not printed.
   They are counted from the "is amended as follows" lines and the cross-headings (a lead-in line counts as a paragraph), and are DERIVED and uncorroborated, except Schedule 4 paragraphs 1 to 8, where line 3033 prints "(8)" for the eighth.
   Schedule 13 is unnumbered, so its names cite the Child Poverty Act section (CPA 8(1), 18(1), 18(3)).
6. Section 82 gives a terminally ill claimant the daily living component at the enhanced rate (s 82(2)) and disapplies only 79(1)(c) and (2)(c), the required period condition, for the mobility component (s 82(3)).
   It does not touch the age limb (a) or the ability limb (b) of s 79(1) and (2), so a terminally ill claimant is still asked both for the mobility component.
7. The "relevant age" in s 83(2) is pensionable age "or, if higher, 65", so a person has reached it only when both are reached; the bar in s 83(1) is "for any period after" and is "subject to such exceptions as may be provided by regulations" (s 83(3)).
8. The care-home and hospital bars (ss 85 and 86) exist only where regulations provide for them: each section begins "Regulations may provide that no amount ... is payable".
   Section 87 is the only bar that operates on the Act's own terms, and it too yields "to the extent that regulations provide otherwise".
9. Section 81 is a direction to the regulations: they "must provide" for the required period condition to be "determined by reference to" two predictions, that it is likely the person's ability would have been limited at every time in the previous 3 months and would be at every time in the next 9, around a date the regulations prescribe.
   The two predictions are inputs, and the prescribed date is an input; s 81(4) lets the regulations depart from the rule in prescribed cases (fork F-81-1).
10. Section 82(4) defines "terminally ill" by a prediction too ("can reasonably be expected within 12 months"); the encoding takes the date by which death can reasonably be expected as the input.
11. Section 88(3) says the person deciding on a fixed-term award "must have regard to guidance issued by the Secretary of State" and says nothing about what follows if they do not, so the function answers `JUST TRUE` for regard had and `NOTHING` otherwise.
   Section 88(4) deems information supplied under Part 4 to be information relating to social security; for any other information it is silent.
12. Section 95 prints an S.S.I. number for one of the four Scottish payments only (child disability payment, "S.S.I. 2021/174"); the other three are named by title and year, so each is identified by the regulations named.
13. Section 137(2) and (3) say the Secretary of State "may only" make the arrangements "if" the non-resident parent agrees or the Secretary of State is satisfied that without them maintenance is unlikely to be paid: a necessary condition, never a sufficient one, so a case that meets it is `NOTHING` (the power is in the Child Support Act 1991, not among the sources) and a case that meets neither is `JUST FALSE`.
14. Section 138(5) lets the Secretary of State "limit the number of applications ... in such manner as the Secretary of State thinks fit" and does not say what happens at the limit; the function answers `JUST TRUE` when no limit is set or the number of applications already accepted is below it, and `NOTHING` otherwise (reading (b)).
15. Schedule 10 paragraph 1(2) defines "the appointed day" as the day appointed for section 77; paragraphs 1(1) and 2 to 5 say only what regulations under section 93 "may in particular" provide to replace disability living allowance with personal independence payment, so they are regulation-making powers (inert, reason 2) and the individual's transitional rights are in regulations that are not among the sources.
16. The six Schedule 11 amendments name the earlier step in different words: the Secretary of State "has considered whether to reverse the decision under section 3A" (Vaccine Damage Payments Act), "has considered whether to revise the decision under section 16" (Child Support Act, twice), "has reviewed the certificate under section 10" (Social Security (Recovery of Benefits) Act), the relevant authority "has considered whether to revise the decision under paragraph 3" (Child Support, Pensions and Social Security Act 2000), and the Secretary of State "has decided whether to reconsider the determination under section 49" (Child Maintenance and Other Payments Act); only the first carries a Northern Ireland exclusion (raw line 3398).
   The shared reading treats the five as one step, which is the plan's reading of seam 8.
17. Schedule 12 reinstates powers to supersede the decisions of the former appellate bodies, and the Act deems the amendments in force from 3 November 2008 (s 103(2), wra4's range, raw lines 1662-1664); the named bodies are an appeal tribunal constituted under Chapter 1 of Part 1 of the Social Security Act 1998 and the Commissioners, whose functions the text says were transferred to the First-tier Tribunal and the Upper Tribunal.
18. Section 150(3) leaves the commencement of the rest of the Act to an order and s 150(4)(b)(iii) lets the order appoint different days for different areas for any provision of Part 4, so the day for a person depends on the area they are in; the caller supplies it.
19. Section 144 inserts a flat negative (ETA 2A(1): arrangements under section 2 "may not include arrangements in respect of employment for sexual purposes") and a power to specify exceptions by order (2A(3)).
   The function for 2A(1) is a "not barred" function: `JUST TRUE` when the employment is not for sexual purposes (this bar does not apply), `JUST FALSE` when it is and no order specifies an exception, and `NOTHING` when either question is not settled.

### What the stable binary does not accept

The brief lists the constructs the stable binary (1.6.98) does not accept and says the binary governs.
Not used in this part, for that reason, and not re-measured: `REFUSE`, `BECAUSE` outside `LEST BREACH BY ... BECAUSE`, `#ASSERT REFUSED`, the date literal `YMD` (dates are `Date d m y`), an unparenthesised `NOT`, more than one `#ASSERT` per line, and an `IMPORT` of a module from another folder.
Two limits were found by running the binary, while writing the seat layer and the allocation helpers:
- A `WHERE` binding whose body starts on the same line as `MEANS concat (LIST (` fails to parse; the body goes on the next line.
- `APPEND` accepts strings only; a list is built with `concat` or `FOLLOWED BY`.
- A deontic value cannot be asserted: the regulative rules (s 89 and s 141) are checked with `#TRACE`, and the date and boolean twins of the same rules are asserted (`s 89(a) the report was laid within the 2 years`, `s 141 CMOPA 6(3B) the review took place within the 30 months`).

## The seat layer (wra3)

`wra3-seat.l4` has 69 questions and `wra3-cases-seat.l4` has 283 assertions on them, all satisfied on the stable binary.
Each question is named "Under section N," or "Under schedule N paragraph M,", has `@desc` and `@export`, takes plain yes/no, number, date and choice inputs worded as the person would be asked, and returns the layer-1 result unchanged.
Each fact that layer 1 takes as `MAYBE` (what regulations provide, what a decision-maker decided, a figure left to regulations) is two plain inputs, "do you know whether ...?" and "...?", joined in the `WHERE` by three helpers (`wra3 seat a yes or no the person may be unable to give` and its number and date twins), so that a person who cannot say gets `NOTHING` and never `FALSE`.
`Person` is built in the `WHERE`, with a comment on each placeholder field that no rule reads.
There is no seat for an official; the questions that are not asked, and why, are listed in the header of `wra3-seat.l4`.
A mutation check made while the seat was written, when it had 259 assertions, flipped 37 expected values and exactly 37 assertions failed (`PROGRESS.md`); it was not repeated on the final 283.
The Schedule 4 questions are marked "assumed, not ruled": state pension credit housing credit is adjacent to the seat's core questions and is included so that the schedule is not silently left out.

## What check.sh prints

`L4=<stable 1.6.98> L4_MAIN=<main build 1.6.108> ./check.sh` in this folder, run on 2026-11-04 after the last change to any `.l4` file; it exited 0:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wra-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
wra3-cases-seat.l4                             0       283       0        0         0 |      0       283       0        0  same
wra3-pt4-s77-84.l4                             0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s85-90.l4                             0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s92.l4                                0         0       0        0         0 |      0         0       0        0  same
wra3-pt4-s95.l4                                0         0       0        0         0 |      0         0       0        0  same
wra3-pt6-misc.l4                               0         0       0        0         0 |      0         0       0        0  same
wra3-pt7-final.l4                              0         0       0        0         0 |      0         0       0        0  same
wra3-sch10.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch11.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch12.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch13.l4                                  0         0       0        0         0 |      0         0       0        0  same
wra3-sch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra3-sch9.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra3-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
wra3-tests-pt4-s77-84.l4                       0       184       0        0         0 |      0       184       0        0  same
wra3-tests-pt4-s85-90.l4                       0        73       0        0         0 |      0        73       0        0  same
wra3-tests-pt4-s92.l4                          0         8       0        0         0 |      0         8       0        0  same
wra3-tests-pt4-s95.l4                          0        20       0        0         0 |      0        20       0        0  same
wra3-tests-pt6-misc.l4                         0        79       0        0         0 |      0        79       0        0  same
wra3-tests-pt7-sch10.l4                        0        15       0        0         0 |      0        15       0        0  same
wra3-tests-sch11.l4                            0        49       0        0         0 |      0        49       0        0  same
wra3-tests-sch12.l4                            0        26       0        0         0 |      0        26       0        0  same
wra3-tests-sch13.l4                            0        16       0        0         0 |      0        16       0        0  same
wra3-tests-sch4.l4                             0        36       0        0         0 |      0        36       0        0  same
wra3-tests-sch9.l4                             0        23       0        0         0 |      0        23       0        0  same
TOTAL (27 modules)                             0       812       0        0           |      0       812       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: the keel's own run, `TOTAL (3 modules) 0 38 0 0` on both columns (`inputs/KEEL-NOTES.md` lines 124-129).
That is not a like-for-like delta: the 38 assertions are in the keel's `wra-core-tests.l4`, which is not in this folder, so the two keel modules that are here (`wra-core.l4`, `wra-definitions.l4`) show 0, and the 812 is this part's alone (27 modules: the 2 keel modules and 25 of mine).
What `check.sh` does not see, and what I did about it.
It does not see a different `#TRACE` outcome, because a trace prints no assertion line, and it does not see any difference that no assertion exercises.
This part has four traces (two in `wra3-tests-pt4-s85-90.l4`, for the report to Parliament in s 89, and two in `wra3-tests-pt6-misc.l4`, for the review of fees regulations in s 141).
I ran both files with the stable and the main binary and compared the whole output: the outcomes are the same (the on-time trace is FULFILLED and the late one is BREACH, in both files, on both binaries), and the only difference in the output is the `Code:` field of each diagnostic, which the main binary names (`eval/result`, `eval/assertion-passed`) and the stable binary leaves as `<none>`.
The date and boolean twins of the two rules are also asserted, so the same days are checked by assertion on both binaries.
