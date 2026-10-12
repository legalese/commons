# Independent expectations: Accident Compensation Act 2001 (NZ)

Written from `../source/ACC2001.txt` (version as at 10 July 2026) **before** any `.l4` file was opened.
Each item is a concrete scenario and the answer worked from the source text. "REFUSE" means the Act
itself does not supply the answer (it depends on regulations, an outside enactment, or a finding of
fact), so a faithful encoding should refuse rather than guess.

Unless stated, amounts are unindexed statutory figures (s 115/s 116 indexation ignored).

## A. Accident (s 25)

- E01 A specific event involving an external force, such as gravity in a fall: **accident** (s 25(1)(a)(i)).
- E02 A sudden movement of the body to avoid an external force: **accident** (s 25(1)(a)(ii)).
- E03 A twisting movement of the body, as a specific event: **accident** (s 25(1)(a)(iii)).
- E04 A gradual process (repetitive strain over months), not a specific event: **not an accident** under (a) (s 25(1)(a) "other than a gradual process").
- E05 Inhaling a gas on a specific occasion: **accident** (s 25(1)(b)).
- E06 Inhaling a virus (no criminal act): **not an accident** (s 25(1)(b) exception).
- E07 Inhaling a virus as a result of another person's criminal act: **accident** (s 25(1)(b) proviso).
- E08 Inhaling a fungus (no criminal act): **not an accident** (s 25(1)(b) lists fungus in the exception).
- E09 Orally ingesting a fungus (a poisonous mushroom) on a specific occasion: **accident**. Para (ba) excludes only a virus, bacterium or protozoan, not a fungus.
- E10 Orally ingesting a bacterium (food poisoning), with no criminal act: **not an accident** (s 25(1)(ba)).
- E11 A burn on a specific occasion, not caused by the elements: **accident** (s 25(1)(c)).
- E12 Sunburn on one afternoon (exposure to the elements), causing 2 weeks' restriction: **not an accident**. It is excluded from (c), and (e) needs restriction for more than 1 month.
- E13 A chemical absorbed through the skin over 30 days: **accident** (s 25(1)(d), period not exceeding 1 month).
- E14 A chemical absorbed through the skin over 6 weeks: **not an accident** (exceeds 1 month).
- E15 Exposure to extremes of temperature over 3 days, causing restriction for a continuous 6 weeks: **accident** (s 25(1)(e)(i)).
- E16 The same exposure, but the restriction lasts 3 weeks: **not an accident** (needs a continuous period exceeding 1 month).
- E17 Exposure to the elements over 3 days that causes death: **accident** (s 25(1)(e)(ii)).
- E18 Exposure to the elements over 2 months that causes death: **not an accident** (exposure period exceeds 1 month).
- E19 An internal force during labour causing levator avulsion (a Schedule 3A injury) to the person giving birth: **accident** (s 25(1)(f)).
- E20 An internal force during labour causing an injury not listed in Schedule 3A: **not an accident** under (f).
- E21 A Schedule 3A birth injury where the delivery was attended by a registered health professional: **still an accident** (s 25(2A) disapplies the treatment exclusion for (f)).
- E22 An occurrence that is treatment given in NZ by a registered health professional: **not an accident** (s 25(2)(a)(i)).
- E23 An occurrence that is treatment given overseas by an equivalently qualified person: **not an accident** (s 25(2)(a)(ii)).
- E24 Scabies that is not work-related: **not an accident** (s 25(2)(b)).
- E25 Malaria from a mosquito bite, not work-related: **not an accident** (s 25(2)(c)).

## B. Personal injury (s 26)

- E26 Death: **personal injury** (s 26(1)(a)).
- E27 A sprain: **personal injury** (s 26(1)(b)).
- E28 Mental injury caused by the person's own physical injuries: **personal injury** (s 26(1)(c)).
- E29 Mental injury with no physical injury, outside s 21 and s 21B: **not personal injury**.
- E30 Damage (not wear and tear) to dentures: **personal injury** (s 26(1)(e)).
- E31 Damage to spectacles or a hearing aid: **not personal injury** (s 26(5)).
- E32 Wear and tear to a prosthesis: **not personal injury** (s 26(1)(e)).
- E33 Binaural hearing loss of 5.0% caused by a s 20(2) personal injury: **personal injury** (s 26(1A)).
- E34 Binaural hearing loss of 4.9% caused by a s 20(2) personal injury: **not personal injury** (below 5%).
- E35 Binaural hearing loss of 12% caused by ageing: **not personal injury** (s 26(1B)(b)).
- E36 Injury caused wholly or substantially by ageing: **not personal injury** (s 26(4)(a)).
- E37 Damage to teeth from their natural use: **not personal injury** (s 26(4)(b)).
- E38 Injury caused substantially by a gradual process that is not work-related, not a treatment injury and not consequential: **not personal injury** (s 26(2)).
- E39 A heart attack that is neither a treatment injury nor within s 28(3): **not personal injury** (s 26(3)).
- E40 A heart attack caused by physical effort at work that is abnormal or excessive for the person: **personal injury** (s 26(3), s 20(2)(j), s 28(3)).

## C. Cover (ss 20, 22, 23, 16(3))

- E41 An accident in NZ on 1 April 2002 causing a physical injury: **cover** (s 20(1)(a)).
- E42 The same accident on 31 March 2002: **no cover under s 20** (s 8; Parts 10 and 11 deal with earlier injuries).
- E43 A visiting tourist (not ordinarily resident) breaks a leg hiking in NZ: **cover**. Residence is irrelevant under s 20.
- E44 A non-resident is injured on board the cruise ship that brought them to NZ and carries them around it: **no cover** (s 23(1)(a), (2)(c)).
- E45 A non-resident is injured on the gangway while embarking that ship: **no cover** (s 23(1)(b), (3)(a)).
- E46 A non-resident is injured on the wharf after leaving the gangway: **cover** (disembarking has finished, s 23(3)(b)).
- E47 An NZ ordinarily-resident passenger is injured on the same cruise ship in NZ waters: **cover** (s 23 applies only to non-residents).
- E48 A non-resident is injured on a domestic NZ ferry that is not the conveyance they arrived or will leave on: **cover**.
- E49 A non-resident on an NZ-to-NZ sea trip, injured 200 nautical miles out: **remains in NZ**, so cover under s 20 (s 16(3)). At 350 nautical miles they are **not in NZ**, and with no ordinary residence there is no s 22 cover.
- E50 An ordinarily resident person is injured in an accident overseas in 2010: **cover** (s 22(1)).
- E51 A non-resident is injured overseas: **no cover** (s 22(1)(c)).
- E52 An ordinarily resident person suffers a treatment injury overseas on or after 1 July 2005, from treatment by an equivalently qualified person: **cover** (s 22(3), (4)).
- E53 The same overseas treatment injury suffered on 30 June 2005: **no cover** under s 22(3).

## D. Mental injury from criminal acts (s 21) and work-related mental injury (s 21B)

- E54 Mental injury caused by a sexual violation (Crimes Act s 128B, in Schedule 3) committed in NZ, with no one charged: **cover** (s 21(1), (5)(a)).
- E55 A Schedule 3 act committed overseas on a person not ordinarily resident in NZ at the time: **no cover** (s 21(2)(b)(ii)).
- E56 A Schedule 3 act committed overseas on a person ordinarily resident at the time of the act, who is not resident when the mental injury is suffered: **cover** (s 21(2)(b)(ii), (3)).
- E57 Mental injury from a robbery (not in Schedule 3) with no physical injury: **no cover**.
- E58 Mental injury under s 21 whose date of first treatment (s 36(1)) is before 1 April 2002: **no s 21 cover** (s 21(1)(a)).
- E59 The alleged offender is incapable of forming criminal intent: **still cover** (s 21(5)(b)).
- E60 Work-related mental injury from a single sudden event at work that the person witnessed in close proximity, which could reasonably be expected to cause mental injury to people generally, with first treatment on 1 October 2008: **cover** (s 21B; date under s 36(1)).
- E61 The same, with first treatment on 30 September 2008: **no cover**.
- E62 The same event seen on CCTV: **no cover** (s 21B(6)(a)).
- E63 The same event heard about by telephone: **no cover** (s 21B(6)(c)).
- E64 Mental injury from prolonged workplace stress (a gradual process): **no cover** (s 21B(7)(c)).
- E65 A sudden work event that could not reasonably be expected to cause mental injury to people generally: **no cover** (s 21B(2)(b)).
- E66 A work event overseas to a person ordinarily resident at the time: **cover**. To a person not ordinarily resident: **no cover** (s 21B(2)(c)).

## E. Ordinarily resident (s 17)

- E67 An NZ citizen with NZ as their permanent place of residence: **ordinarily resident**.
- E68 An NZ citizen who has been and remains absent for 7 months, with no employment exception: **not ordinarily resident** (s 17(2)).
- E69 An NZ citizen absent 5 months, intending a total absence of 5 months: **ordinarily resident**.
- E70 An NZ citizen absent 1 month who intends to be absent for 8 months: **not ordinarily resident** (s 17(2) "intends").
- E71 An NZ citizen absent 2 years for employment duties whose pay is NZ-taxed, intending to resume NZ residence: **ordinarily resident** (s 17(4)(a)).
- E72 Such a person 4 months after the overseas employment ended: **ordinarily resident** (s 17(4)(a)(ii), up to 6 months). At 7 months after: **not** under (4).
- E73 The accompanying spouse of an E71 person, intending to resume residence: **ordinarily resident** (s 17(4)(b)).
- E74 A work-visa holder (not a residence class visa) living permanently in NZ: **not ordinarily resident** (s 17(1)(b) category not met).
- E75 A person in NZ unlawfully: **not ordinarily resident** (s 17(5)).
- E76 Absent but present in NZ for 184 days in the 12 months before last leaving: **has a permanent place of residence** (s 17(3), exceeding 183 days). At exactly 183 days: **not** under (3).
- E77 Present 200 days in the prior 12 months but absent for 7 months: **not ordinarily resident**. Section 17(2) overrides (3).
- E78 Part days count as whole days for s 17(3): 183 full days plus 1 part day is 184 days, so the person **has a permanent place of residence**.

## F. Work-related, motor vehicle, overlap (ss 28, 29, 35)

- E79 Injured at the place of employment while working: **work-related** (s 28(1)(a)).
- E80 Injured during a meal break at the place of employment: **work-related** (s 28(1)(b)).
- E81 An employee commuting in their own car: **not work-related**.
- E82 An employee commuting at the start of the day in an employer-provided van, driven by the employer and provided for transporting employees: **work-related** (s 28(1)(c)).
- E83 Travelling by the most direct route from work to physio for a work injury: **work-related** (s 28(1)(d)). With an unreasonable shopping detour: **not work-related** (s 28(2)).
- E84 Injured while skylarking at work: **still work-related** (s 28(7)(c)).
- E85 Injured at work by a Schedule 3 offence where the person elects non-work treatment: **not work-related** (s 28(6)).
- E86 Injured in a car crash on a road (movement of a vehicle): **motor vehicle injury** (s 35(1)(a)(i)).
- E87 Injured while loading a truck: **not a motor vehicle injury** (s 35(2)(a)).
- E88 A farm bike used off-road in a paddock: **not a motor vehicle injury** (s 35(2)(c)). Off-road because it went out of control on a road: **motor vehicle injury** (s 35(3)).
- E89 A stationary parked car struck by another car: **motor vehicle injury** (s 35(1)(a)(ii)).
- E90 Work-related mental injury from witnessing a crash: **not a motor vehicle injury** (s 35(1)(b)).
- E91 A courier driver crashes while driving for work (s 28(1)(a)): **motor vehicle injury, not work-related** (s 29(2)), and **entitled to first week compensation** (s 29(3)).
- E92 An employee in an employer-provided commuting van crash (s 28(1)(c)): **work-related, not a motor vehicle injury** (s 29(1)).

## G. Accounts (ss 167, 213, 218, 227, 228)

- E93 A work-related injury to an employee: **Work Account**.
- E94 A motor vehicle injury (to an earner or a non-earner): **Motor Vehicle Account**.
- E95 A non-work injury to an earner: **Earners' Account**.
- E96 A non-work injury to a non-earner: **Non-Earners' Account**.
- E97 A treatment injury from treatment for a non-work injury: **Treatment Injury Account** (s 228(1)(a)).
- E98 A treatment injury from treatment for a work-related injury: **not the Treatment Injury Account** (s 228(3)). It is work-related (s 28(5)), so **Work Account**.
- E99 A work-related injury to an employee of a foreign representative: **Non-Earners' Account** (s 227(3)(b)).
- E100 Clause 43 deemed earner (employment ended), non-work injury: **Earners' Account** (cl 43(6)).

## H. Treatment injury (ss 32, 33)

- E101 Injury caused by treatment from a registered health professional that is not a necessary part or ordinary consequence of it: **treatment injury**.
- E102 An ordinary consequence of the treatment: **not a treatment injury** (s 32(1)(c)).
- E103 Injury wholly or substantially caused by the underlying condition: **not a treatment injury** (s 32(2)(a)).
- E104 Injury solely attributable to a resource allocation decision: **not a treatment injury** (s 32(2)(b)).
- E105 Injury resulting from unreasonably withholding consent: **not a treatment injury** (s 32(2)(c)).
- E106 The only complaint is that the treatment did not achieve the desired result: **not a treatment injury** (s 32(3)).
- E107 A clinical trial where the claimant did not agree in writing to participate: **treatment injury** (s 32(5)). Where the claimant agreed in writing and the trial was principally for the manufacturer: **not** (s 32(6)).
- E108 A treatment-injury infection passed directly to a spouse: **spouse covered** (s 32(7)(a)). Passed from spouse to a child: **covered** (s 32(7)(d)). Passed from an unrelated third party onward to a fourth person: **not covered**.

## I. Dates of injury (ss 36-38) and gradual process (ss 24, 30)

- E109 Gradual process: first treated by a GP on 10 March 2020, first incapacity on 1 February 2020. **Date is 1 February 2020** (s 37(1), earlier of the two).
- E110 Pre-1974 exposure in s 30(2) circumstances, with an actual s 37(1) date in 1990: **deemed 1 July 1992** (s 37(4)). With an actual date of 5 May 2005: **5 May 2005**.
- E111 Mental injury from physical injury: **date of the physical injury** (s 36(2)).
- E112 Mental injury under s 21: **date of first treatment for it as mental injury** (s 36(1)).
- E113 Treatment injury: **date the person first sought or received treatment for the symptoms** (s 38(1)).
- E114 Mesothelioma diagnosed as caused by asbestos, in a worker exposed to asbestos in employment: **work-related gradual process injury without a causation assessment** (s 30(3), (4); Schedule 2 item 2).
- E115 Injury related to non-physical stress: **not a work-related gradual process injury** (s 30(5)(a)).
- E116 Exposure occurred overseas while not ordinarily resident: **not covered** (s 30(4A)).
- E117 The Corporation establishes the risk is not significantly greater for those doing the task: **may decline** (s 30(2A)).
- E118 A property present at work and outside work, where the non-work cause is more likely: **not caused in s 30(2) circumstances** (s 30(2)(c)).

## J. Claims and decisions (ss 53, 56-58, 65, 66, 75)

- E119 A claim for cover lodged 11 months after the injury: **in time** (s 53(3)(a)).
- E120 A claim for cover lodged 13 months after the injury: **late**. It may be declined for lateness **only if the lateness prejudices** the Corporation (s 53(2)).
- E121 Treatment injury suffered January 2020, first considered a treatment injury by a registered health professional in June 2021, claim lodged May 2022: **in time** (s 53(4)(a), 12 months after the later date).
- E122 Simple claim lodged 1 March 2024, no extension, no decision: **deemed cover**, with the deemed decision dated **22 March 2024** (s 56(2), s 58). A decision made on 22 March 2024 is **in time**.
- E123 Simple claim lodged 1 March 2024 with an s 56(2)(b)(ii) extension: the decision is due by **1 July 2024** (4 months, s 56(5)). Missing it gives **deemed cover**.
- E124 Complicated claim (treatment injury) lodged 1 March 2024: initial limit **1 May 2024** (2 months). The extension is at most 2 months (to 1 July 2024). The absolute limit with agreed further extensions is **1 December 2024** (9 months, s 57(4)).
- E125 A claim lodged outside the s 53 period: **complicated claim** (s 57(1)(d)). Mental injury under s 21 or 21B, work-related gradual process and treatment injury claims are also complicated.
- E126 A deemed decision later revised: the Corporation **cannot recover** payments made before the revision unless the claimant was intentionally misleading (s 65(2)).
- E127 Latest action recorded on a claim file 1 January 2015: the file must be kept **until at least 1 January 2025** (s 66, 10 years).
- E128 Cover accepted 1 February 2024: the rehabilitation-plan need is to be determined **by 2 May 2024** (13 weeks, s 75).

## K. First week compensation (ss 97, 98, 306)

- E129 An employee with a work injury earned $1,000 in the 7 days before incapacity and $0 in the first week: **FWC is $800** (s 97(2), (3)).
- E130 The same employee earned $400 during the first week of incapacity: loss is $600, so **FWC is $480**.
- E131 A self-employed person with a work injury: **no FWC** (s 97(1)(b)).
- E132 An employee with a non-work injury: **no FWC** (sick leave may be used, s 306).
- E133 An employee with a motor vehicle injury under s 29(2) (driving for work): **FWC payable** (s 97(1)(a)(ii)).
- E134 The employer is liable to pay FWC (s 98(1)). Failure is an offence (s 98(3)); no fine is specified, so the **general fine of up to $500** applies (s 315).
- E135 First week of incapacity starting 1 March 2024: it **ends at the close of 7 March 2024** (s 6 "first week of incapacity").

## L. Weekly compensation (Schedule 1 Part 2; ss 112, 87)

- E136 An earner incapacitated from 1 March 2024: weekly compensation runs **on and from 8 March 2024** (cl 32(2)(a)).
- E137 A non-earner (not a potential earner) with incapacity: **no cl 32 weekly compensation**.
- E138 Weekly earnings of $1,000: **compensation $800** (cl 32(3)).
- E139 Weekly earnings of $2,000: 80% is $1,600, **capped at $1,341.31** (cl 46).
- E140 Weekly earnings of $1,600: **$1,280** (under the cap).
- E141 Weekly earnings of $1,676.64: 80% is $1,341.312, so **$1,341.31** (cap).
- E142 Permanent employee who earned $4,000 in the 4 weeks before incapacity, all 4 weeks worked: **weekly earnings $1,000 for weeks 2-5** (cl 34(1)).
- E143 The same employee earned $46,800 over 52 weeks: **weekly earnings after the first 5 weeks are $900**, so compensation is **$720** (cl 34(2)).
- E144 A permanent employee who earned $26,000 in 26 of the 52 weeks: **$1,000** (cl 34(2) divides by weeks earned).
- E145 A non-permanent employee with $26,000 in 52 weeks and no cl 36(3) adjustments: **$500** (cl 36(2) divides by 52).
- E146 A non-permanent employee with $26,000 in 52 weeks who was on weekly compensation for 12 of them: divisor 40, so **$650** (cl 36(3)(a), (4)).
- E147 A full-time earner with weekly earnings of $400, minimum weekly earnings supplied as $920, incapacitated more than 1 week: **deemed $920**, so compensation is **$736** (cl 42).
- E148 A part-time (20 hours) employee not on the minimum levy, weekly earnings $400: **no uplift**, so **$320**.
- E149 The cl 42(3) minimum weekly earnings figure itself: **REFUSE** unless supplied. It depends on the minimum wage order and supported living payment rates outside the Act.
- E150 Abatement: weekly earnings $1,000, compensation $800, post-incapacity earnings $300. **Compensation is abated to $700** (cl 51(2)).
- E151 Abatement with post-incapacity earnings of $100: total $900 is within $1,000, so **compensation stays $800**.
- E152 Abatement with post-incapacity earnings of $1,000 or more: **compensation $0**.
- E153 Potential earner injured at 16, now 19, not in full-time study, earning nothing, incapacitated 6 months: **entitled at 80% of minimum weekly earnings** (cl 47(1), (3), (4)).
- E154 The same claimant incapacitated 5 months: **not yet payable** (cl 47(3)).
- E155 A potential earner aged 17: **no cl 47 compensation** (cl 47(1)(c)).
- E156 A potential earner in full-time study: **no** (cl 47(1)(d)).
- E157 A potential earner earning more than the minimum weekly earnings: **no** (cl 47(1)(e)).
- E158 First entitled at 60, with NZ superannuation age 65 (24 months or more before it): **loses entitlement at 65** (cl 52(1), (2)).
- E159 First entitled exactly 24 months before NZS age: cl 52(1)(b) ("24 months or longer") applies, so **loses at NZS age**.
- E160 First entitled at 64, less than 24 months before NZS age: **entitled for 24 months from entitlement**, past NZS age (cl 52(3), (4)).
- E161 First entitled at 66: **24 months** (cl 52(3)(b)).
- E162 Notified of a vocational independence determination on 15 January 2024: **loses weekly compensation on 15 April 2024** (s 112, 3 months).
- E163 Vocational rehabilitation for 3.5 years without the s 87(2B) discretion: **not permitted** (s 87(2), 3 years). With the s 87(2B) criteria met: **may continue**.
- E164 Self-employed purchased weekly compensation (s 209(2)): it must be **at least 80% of minimum weekly earnings and at most the cl 46 maximum**. With minimum earnings of $920, $700 is too low (80% is $736) and $1,400 is too high.

## M. Interest on late weekly compensation (s 114)

- E165 Example 1: $100 due 15 November 2018, paid 15 March 2019, rate 4.275%. **Liability period 120 days; interest $1.41** (1.4055).
- E166 Example 2: $100 due 15 May 2018, paid 15 November 2018. 46 days at 4.175% and 138 days at 4.275%: **184 days; interest $2.14** (2.1425).
- E167 Payment made within 1 month of the Corporation receiving all necessary information: **no interest** (s 114(1)).
- E168 The liability period excludes the day payment should have been made and includes the day it is made (s 114(3)). Due 1 July, paid 2 July: **1 day**.
- E169 The base rate for a given year (the RBNZ 6-month term deposit average): **REFUSE** unless supplied. The premium default is **0.95%**.

## N. Lump sum compensation (Schedule 1 Part 3)

- E170 10% whole-person impairment: **entitled; $2,500** (cl 54(1)(c), cl 56(3)).
- E171 9% whole-person impairment: **no lump sum**.
- E172 80% whole-person impairment: **$100,000**. At 95%: **$100,000** (cl 56(4)).
- E173 50% whole-person impairment, amount: **REFUSE**. It is set by regulations (cl 56(1)).
- E174 Survived 27 days: **no lump sum**. Survived 28 days: **eligible** (cl 54(1)(b)(i)).
- E175 Died before assessment: **no lump sum** (cl 54(1)(b)(ii)). Died after assessment but before payment: **paid to the estate** (cl 62).
- E176 Personal injury suffered before 1 April 2002: **no lump sum** (cl 54(2)).
- E177 Treatment injury from treatment given before 1 April 2002: **no lump sum** (cl 55(3)).
- E178 Mental injury under s 21 from an act that last occurred before 1 April 2002: **no lump sum** (cl 55(1)).
- E179 At 18 months after the injury, a certificate says the condition has not stabilised: the Corporation **must not assess yet** (cl 57(1)(b) needs 2 years). At 2 years with the same certificate: **may assess**.
- E180 Mental injury in a claimant aged 15: **no assessment until 16**, absent compelling reasons (cl 57(2)).
- E181 A second reassessment request under cl 61(4) within 12 months of a previous one: **not entitled** (cl 61(7)).
- E182 Previous lump sum $10,000 (unindexed), new assessed amount $30,000: **pay $20,000** (cl 60(2)).
- E183 Whole-person impairment assessed above 100%: **capped at 100%** (cl 59(6)).

## O. Fatal entitlements (Schedule 1 Part 4)

- E184 Funeral costs of $3,000: **$3,000**. Costs of $8,000: **$4,500** (cl 64).
- E185 Survivor's grant: one spouse **$4,702.79**. Two spouses **$2,351.395 each** (equal division). Each child under 18 **$2,351.40**. A child aged 18: **no grant** under cl 65(1)(b). Other dependant **$2,351.40**.
- E186 Deceased's compensation at 5 weeks was $1,000: **spouse gets $600** (cl 66(2), 60%).
- E187 Child: **$200** (20%). Both parents dead: **$400** (cl 70(6) doubles).
- E188 Spouse plus 3 children: 60% + 3 × 20% = 120% exceeds 100%, so the **total is capped at $1,000** (cl 74).
- E189 Spouse plus 2 children: 100%, **not reduced** ($1,000 total).
- E190 Death in 2020 with the youngest child in the spouse's care aged 10: the spouse's entitlement **ends when the youngest turns 18** (2028), the latest of the cl 66(5) events. With no children: **5 years**.
- E191 The surviving spouse remarries: **compensation continues** (cl 66(4)(a)).
- E192 Child not in study: entitlement **ends at the end of the calendar year in which the child turns 18**. In full-time study: the later of that and the earliest of ceasing study, completing study or turning 21 (cl 70(5)).
- E193 Child care payments: 1 child **$100**; 2 children **$60 each**; 4 children **$35 each** ($140 ÷ 4) (cl 76(2)).
- E194 Child care payments end at the earlier of 5 years or the child turning 14 (cl 77(2)). A child aged 12 at the death stops at 14 (2 years).
- E195 A child born 11 months after the death: **deemed dependent** (cl 63). Born 13 months after: **not deemed**.
- E196 Another dependant's earnings average more than the minimum weekly earnings over 12 months: **weekly compensation ends** (cl 71(5)(a)).
- E197 A person who became a spouse after the injury mainly to qualify for entitlements: **no entitlement** (cl 75(3)).

## P. Disentitlements and payment rules (ss 119-129, 123)

- E198 Wilfully self-inflicted injury: **no Schedule 1 entitlements except treatment and ancillary services** (s 119(1)(a), (2)). For example, weekly compensation is barred and treatment is not.
- E199 Death by suicide: **no Schedule 1 entitlements** (funeral grant, survivors' grants, fatal weekly compensation) (s 119(1)(c)).
- E200 Suicide resulting from mental injury caused by a covered physical injury: **not barred** (s 119(3)(a)).
- E201 Suicide resulting from s 21 or s 21B mental injury: **not barred** (s 119(3)(b)).
- E202 Assisted dying under the End of Life Choice Act 2019: **not barred** (s 119(4)).
- E203 Survivor convicted of murdering the deceased: **no Part 4 Schedule 1 entitlements** for that death (s 120(1)). Merely charged: **suspended** (s 120(2)).
- E204 A prisoner: **no weekly compensation (Part 2) and no fatal entitlements (Part 4)**. Treatment is not barred by s 121. Lump sum (Part 3) is **not required** to be assessed or paid while in prison (s 121(2)).
- E205 Injured while committing an offence with a maximum of 2 years or more, then sentenced to imprisonment: **no Schedule 1 entitlements except treatment and ancillary services**, and surgery only if needed to return to work (s 122).
- E206 The same, but the offence maximum is 1 year: **not barred**.
- E207 The same, but sentenced to community work (not imprisonment or home detention): **not barred**.
- E208 The same, sentenced to home detention: **barred**.
- E209 The surviving spouse of a deceased claimant barred by s 122(1): **spouse barred** (s 122(2)).
- E210 The estate applies 2 years after death for accrued unpaid weekly compensation: **payable** (s 126). Applies 3 years and 1 day after: **not payable**. Lump sum is outside s 126 (cl 62 instead).
- E211 Injured outside NZ, now outside NZ, with earnings in the 6 months before leaving NZ: **weekly compensation may be paid abroad** (subject to assessment, s 127(3)). With no earnings abroad before injury and none within 6 months before leaving: **not payable** (s 127(1)).
- E212 Claimant outside NZ whose condition has not been assessed by a Corporation-approved person: **no weekly or lump sum compensation** (s 127(3)).
- E213 Attendant care during a 40-day trip overseas: **payable for up to 28 days** (s 129(2)).
- E214 An independence allowance assigned to an insurer for 5 years: **allowed** (s 123(2)(b)). For 6 years: **not allowed** (inalienable).

## Q. Reviews and appeals (ss 134-162)

- E215 Notice of decision on 10 January 2024: review application due **by 10 April 2024** (s 135(2)(f), 3 months). Lodged 20 April 2024: **late**, but must be accepted if extenuating circumstances exist (s 135(3)).
- E216 Review of an entitlement claim applied for 10 days after the claim: **not allowed** (s 135(2)(g), not less than 21 days). At 21 days: **allowed**.
- E217 Review hearing notice: **at least 7 days** before the hearing (s 141(3)(b)).
- E218 A hearing is required unless the application is withdrawn or all parties agree (s 141(1)).
- E219 The review decision is due within **28 days after the hearing finishes** (s 144(1)).
- E220 Review application received 1 February 2024, no hearing date set by 1 May 2024, applicant not at fault: **deemed decision in the applicant's favour**, dated **1 May 2024** (s 146). If the applicant contributed to the delay: **no deemed decision**.
- E221 Decision fully or partly for the applicant: **costs must be awarded**. Not for the applicant but they acted reasonably: **may be awarded** (s 148(2)). Costs are payable within 28 days (s 148(5)).
- E222 An employer cannot seek review of entitlement decisions (s 134(3)). It can seek review of a decision that an injury is work-related (s 134(2)).
- E223 A claimant may appeal a review decision to the District Court (s 149(1)). Not a review decision on a Code complaint (s 149(3)).
- E224 Copy of the review decision given 1 March 2024: notice of appeal due **by 29 March 2024** (s 151(3)(a), 28 days). For a deemed decision dated 1 May 2024: **by 29 May 2024**.
- E225 The Corporation must provide names to the Registrar **within 7 days** (s 152(3)).
- E226 District Court decision 1 March 2024: leave to appeal to the High Court must be sought **within 21 days** (by 22 March 2024). If refused, High Court special leave must be sought within 21 days of the refusal (s 162).

## R. Levies and Scheme (Part 6)

- E227 A levy invoice dated 1 March: the due date **must be at least 30 days later** (s 168(3)). Due 15 March is invalid; 31 March is valid.
- E228 No Work Account levy on employee earnings above the specified maximum (s 172(1)).
- E229 Two employers; employer A paid levy on $80,000, employer B on $60,000 (b = $140,000), total excess levy $700: **A's refund is $400** ((80/140) × 700) (s 172(2)(b)).
- E230 Refund claim more than 4 years after the close of the tax year: **not entitled** (s 172(3)).
- E231 Estimated levy overpaid by $15: **no refund required** (s 173(2)(a), more than $20 only). Overpaid by $500: **refund, no interest**. Overpaid by $1,500: **refund plus interest**.
- E232 An employer expects relevant employee earnings to change by 20%: **must notify** (s 174(2)(a)). At 19%: **may notify**.
- E233 Mixed earnings: employee earnings $150,000 with specified maximum $142,283: **no earner levy on self-employed earnings** (s 231(2)). Employee earnings $100,000 and self-employed $80,000: **levy base is $42,283** (lesser of max − employee and self-employed earnings).
- E234 Business ceased 10 March 2024: notify the Corporation **by 15 May 2024** (s 232(2)).
- E235 Levy determination more than 4 years after the close of the tax year of the statement, statement not fraudulent: **not allowed** (s 243(3)). Fraudulent: **allowed**.
- E236 Overpayment of $1,000 from failing to inform: **penalty $100** (s 249(1)(a), 10%). From a knowingly false statement: **penalty up to $3,000** (s 249(1)(b)).
- E237 Unpaid levy at 210 days after the due date: **no 10% penalty yet**. At 211 days: **a 10% penalty**. Another 10% after each further 180 days. Interest plus penalties are **capped at 3 times the unpaid levy** (s 250).
- E238 Levy recovery: an action may be taken **within 10 years** from the close of the date the levy became payable (s 254).
- E239 The default fuel levy rate is **5.08 cents per litre** of motor spirit, exclusive of GST (s 214(4)(b), (5)).
- E240 Accredited employer claim management period: **12 to 60 months**. 6 months or 72 months is **invalid** (s 181).
- E241 Purchase of weekly compensation (s 223): apply while employed or **within 1 month** of ceasing. The period is **at most 2 years**.
- E242 Purchased weekly compensation (s 224): payable **for at most 5 years** after incapacity first commenced.
- E243 Early termination after resuming work (s 226(2)): refund **only if the remaining period exceeds 3 months**.
- E244 A levy refund under $20: the Corporation **may refrain** (s 255(2)).
- E245 A review of a levy decision must be sought within 3 months (s 236(1)). No review of the fuel levy (s 236(2)).
- E246 Activity making up 5% of earnings: **may be ignored** in classification (s 171(2)). At 6%: **must be considered**.

## S. Offences and proceedings (Part 9 and others)

- E247 Misleading the Corporation (s 308): **up to 3 months' imprisonment or a $5,000 fine**.
- E248 Failing to provide requested information (s 309): **$2,000 fine**. **No offence** without the claimant's authorisation (s 309(4)).
- E249 Failing to advise of increased earnings (s 310): **$5,000 fine**.
- E250 Breaching a publication order (s 160(4)): individual **$1,000**, body corporate **$5,000**.
- E251 Misapplying levy deductions (s 316(1)(b)): **5 years or $50,000**. Not making a deduction (s 316(1)(a)): first conviction **$25,000**, later **$50,000** (s 316(4)).
- E252 General offence with no fine provided: **$500** (s 315). This applies to s 98(3) and s 242.
- E253 Regulations may prescribe fines **not exceeding $500** (s 335).
- E254 Offence committed 15 June 2020: the limitation period ends **31 December 2025** (s 313(1), 5 years after the termination of the year, read as the calendar year). An earlier charge is in time.
- E255 A damages claim for a covered personal injury: **barred** (s 317(1)). Exemplary damages: **allowed** (s 319). Property damage: **allowed** (s 317(2)(a)), but no compensation for the personal injury is awarded (s 317(3)).
- E256 Claim under an international carriage-of-passengers convention: **allowed** (s 317(5)).
- E257 Gradual process proceedings commenced before 1 April 1993: **may be completed** (s 318(3)). Commenced in 1995: **barred**.
- E258 An injury with no cover (mental injury with no physical injury, outside s 21 and s 21B): the s 317 bar **does not apply**.
- E259 Employment grievance (unjustifiable dismissal) proceedings: **allowed**, but no personal injury compensation (s 317(2)(c), (3)).

## T. Things the Act does not answer (REFUSE)

- E149 The minimum weekly earnings figure (outside enactments and orders).
- E169 The s 114 base rate for a year (RBNZ data).
- E173 The lump sum for an impairment between 10% and 80% (regulations).
- E260 Levy rates for any Account (regulations, ss 169, 214, 220, 229).
- E261 NZ superannuation qualification age: set by the NZ Superannuation and Retirement Income Act 2001 (65), not this Act. It should be an input.
- E262 Whether a reviewer must award costs of a particular amount (regulations, s 148(4)).
