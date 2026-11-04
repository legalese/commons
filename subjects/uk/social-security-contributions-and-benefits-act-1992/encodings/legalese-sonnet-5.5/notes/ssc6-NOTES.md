# NOTES -- ssc6: Parts XI, XII, 12ZA and 12ZB of the Social Security Contributions and Benefits Act 1992 (UK), 1992 c. 4, ss 151-171ZT

**Status of the claims below, and how each was checked.**
The encodings were run on the stable binary (l4 1.6.98) and on a main build (1.6.108); `check.sh` printed identical counts on both (section "What `check.sh` prints").
Every `src:` citation was checked mechanically by `srcrefs.py check --refs` and `--strict` (0 problems; section "What `check.sh` prints").
Every expected value in the tests was written by hand from the text, not copied from output.
Nothing was checked against the official text: the source is `ukpga-1992-4.txt`, a plain-text rendering made by a converter script, and `src:N` is a line of that rendering.
No lawyer has read any reading below; the choices are assumed, not ruled, and the ones that matter are in the fork register and the marginal readings.

## What this is

This part encodes lines 3095-3717 of the rendering: Part XI, Statutory Sick Pay (ss 151-163), Part XII, Statutory Maternity Pay (ss 164-171), Part 12ZA, Statutory Paternity Pay (ss 171ZA-171ZK) and Part 12ZB, Statutory Adoption Pay (ss 171ZL-171ZT).
It stands on the keel's shared core (`ssc-core.l4`, read-only) and has two layers.

- **Layer 1, the isomorphic rules.**
  `ssc6-ssp.l4` (Part XI), `ssc6-smp.l4` (Part XII), `ssc6-spp.l4` (Part 12ZA) and `ssc6-sap.l4` (Part 12ZB) hold the decision functions, each preceded by the quoted words (`-- src:N | ...`) and an `@ref` citing the section.
  `ssc6-duties.l4` holds the four payment duties as regulative rules (`PARTY ... MUST ...`), with traces.
  `ssc6-tests-ssp.l4`, `-smp`, `-spp` and `-sap` test the four modules (hand-written expected values; a test on each side of each period, week-count and limit boundary the text states).
  `ssc6-ssp.l4` imports `ssc6-smp.l4` because section 153(12) points at sections 165(1) and 171(1); the other three modules import only the prelude, `daydate` and the core.
- **Layer 2, the seat.**
  `ssc6-seat.l4` has 42 `@export`ed questions for a person who works, is self-employed, or claims a benefit, statutory pay or Child Benefit in Great Britain, here asking about statutory sick, maternity, paternity or adoption pay.
  Every question is named "Under section N, ...", takes plain inputs (yes or no, a number, a date) with an `@desc` worded as that person would be asked, and is grouped under a `§` heading in text order.
  It restates no rule: each question builds the module records from the plain answers and calls one rule.
  `ssc6-cases-seat.l4` has 115 hand-written cases for it.

The quoted words are never retyped: `work/build.py` (not shipped) copies each quotation from the raw file with `srcrefs.py quote`, so a quotation cannot drift from its line.

## Where `PLAN.md` and the brief differ

The brief governs.
The differences that matter in this range are the `MAYBE` types of seams S29, S30 and S32, and the extra inputs those answers take (section "Seams (ssc6)").

## Coverage (ssc6)

Every unit of lines 3095-3717 of the rendering has exactly one disposition: `encoded` (with the L4 name), `inert` (with a reason), `fork` (with the fork id and the rule that carries the reading taken) or `repealed or blank in this text`.
There is no out-of-scope or deferred row.
A unit is a heading, a section, a subsection, a paragraph, a sub-paragraph, a defined term, a line of dots, or an omission marker; `work/units.py` (not shipped) splits the range into units and asserts that each of the 623 lines belongs to exactly one.
A unit is `encoded` when every line of it is quoted (`-- src:N | ...`) in the block of a rule, and the rule is named in the last column.
The seven units that `ssc6-duties.l4` also quotes (ss 151(1), 164(1), 164(3), 171ZA(1), 171ZD(1), 171ZL(1), 171ZM(1)) keep that one disposition; the duty rule is named in the Jural relations section.

| disposition | units |
| --- | --- |
| encoded | 288 |
| fork | 20 |
| inert, reason 1 (not operative: a heading, or the lead-in words of a list of definitions) | 63 |
| inert, reason 2 (machinery: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input) | 191 |
| repealed or blank in this text | 23 |
| **total** | **585** |

No unit is `inert` with reason 3: repealed or blank text has its own disposition, `repealed or blank in this text`.

**Audit.**
Text units counted: 585 (623 lines audited, each in exactly one unit).
Rows in the table before the dispositions were assigned by hand: 387 resolved by rule (headings, lines of dots, units whose every line a rule quotes) and 198 without a disposition; after: 585 rows, none without a disposition.
The join (`work/coverage.py`) prints every unit without a disposition and exits 1; the last run printed none.

| unit | lines | disposition | L4 name, or reason, or fork |
| --- | --- | --- | --- |
| heading: Part XI | 3095 | inert | reason 1: a heading; creates no rule |
| heading: Employer’s liability | 3096 | inert | reason 1: a heading; creates no rule |
| s 151 | 3097 | inert | reason 1: a heading; creates no rule |
| s 151(1) | 3098 | encoded | ssp: s 151(1) the employer is liable to make a payment of statutory sick pay in respect of the day |
| s 151(2) | 3099 | encoded | ssp: s 151(2) the agreement is void to the extent that it purports |
| s 151(2)(a) | 3100 | encoded | ssp: s 151(2) the agreement is void to the extent that it purports |
| s 151(2)(b) | 3101 | encoded | ssp: s 151(2) the agreement is void to the extent that it purports |
| s 151(3) | 3102 | encoded | ssp: s 151(3) the agreement is protected from being void by virtue of subsection (2)(a) |
| s 151(3)(a) | 3103 | encoded | ssp: s 151(3) the agreement is protected from being void by virtue of subsection (2)(a) |
| s 151(3)(b) | 3104 | encoded | ssp: s 151(3) the agreement is protected from being void by virtue of subsection (2)(a) |
| s 151(4) | 3105 | encoded | ssp: s 151(4) the day is a day of incapacity for work in relation to the contract of service |
| s 151(5) | 3106 | encoded | ssp: s 151(5) the employer is treated as a different employer in relation to each contract of service |
| s 151(6) | 3107 | encoded | ssp: s 151(6) who is liable to make payments of statutory sick pay |
| s 151(7) | 3108 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| heading: The qualifying conditions | 3109 | inert | reason 1: a heading; creates no rule |
| s 152 | 3110 | inert | reason 1: a heading; creates no rule |
| s 152(1) | 3111 | repealed or blank in this text | the converter shows only dots |
| s 152(2) | 3112 | encoded | ssp: s 152(2) the days form a period of incapacity for work |
| s 152(3) | 3113 | fork | F-gap; rule: ssp: s 152(3) the two periods of incapacity for work are treated as a single period |
| s 152(4) | 3114 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 152(5) | 3115 | encoded | ssp: s 152(5) the number of days in the period counting every day of the week |
| s 152(6) | 3116 | encoded | ssp: s 152(6) the day may be a day of incapacity for work notwithstanding |
| s 152(6)(a) | 3117 | encoded | ssp: s 152(6) the day may be a day of incapacity for work notwithstanding |
| s 152(6)(b) | 3118 | encoded | ssp: s 152(6) the day may be a day of incapacity for work notwithstanding |
| s 153 | 3119 | inert | reason 1: a heading; creates no rule |
| s 153(1) | 3120 | encoded | ssp: s 153(1) the first condition is satisfied |
| s 153(2) | 3121 | encoded | ssp: s 153(2) the period of entitlement ends on |
| s 153(2)(a) | 3122 | encoded | ssp: s 153(2) the period of entitlement ends on |
| s 153(2)(b) | 3123 | encoded | ssp: s 153(2) the period of entitlement ends on |
| s 153(2)(c) | 3124 | encoded | ssp: s 153(2) the period of entitlement ends on |
| s 153(2)(d) | 3125 | encoded | ssp: s 153(2)(d) the period of entitlement ends on the day before the disqualifying period; ssp: s 153(2) the period of entitlement ends on |
| s 153(3) | 3126 | encoded | ssp: s 153(1) the first condition is satisfied |
| s 153(4) | 3127 | encoded | ssp: s 153(4) the period is also a period of entitlement as between the employee and another employer |
| s 153(5) | 3128 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 153(5)(a) | 3129 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 153(5)(b) | 3130 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 153(6) | 3131 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 153(7) | 3132 | encoded | ssp: s 153(7) the period of entitlement begins on |
| s 153(8) | 3133 | encoded | ssp: s 153(7) the period of entitlement begins on |
| s 153(9) | 3134 | encoded | ssp: s 153(7) the period of entitlement begins on |
| s 153(10) | 3135 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 153(11) | 3136 | encoded | ssp: s 153(2)(d) the period of entitlement ends on the day before the disqualifying period |
| s 153(12) | 3137 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 153(12) “confinement” | 3138 | fork | F-24; rule: ssp: s 153(12) she has been confined |
| s 153(12) “disqualifying period” | 3139-3141 | fork | F-both; rule: ssp: s 153(12) the relevant date falls within the disqualifying period |
| s 153(12) “maternity allowance period” | 3142 | encoded | ssp: s 153(12) the maternity allowance period |
| s 153(12) “maternity pay period” | 3143 | encoded | ssp: s 153(12) the maternity pay period |
| s 154 | 3144 | inert | reason 1: a heading; creates no rule |
| s 154(1) | 3145 | encoded | ssp: s 154(1) the second condition is satisfied |
| s 154(2) | 3146 | encoded | ssp: s 154(2) the day is a qualifying day |
| s 154(3) | 3147 | encoded | ssp: s 154(3) the agreement provides at least one qualifying day in the week |
| s 154(4) | 3148 | encoded | ssp: s 154(4) the day is also a qualifying day as between the employee and another employer |
| heading: Limitations on entitlement, etc. | 3149 | inert | reason 1: a heading; creates no rule |
| s 155 | 3150 | inert | reason 1: a heading; creates no rule |
| s 155(1) | 3151 | repealed or blank in this text | the converter shows only dots |
| s 155(2) | 3152 | encoded | ssp: s 155(2) the employee is entitled as against the employer to the aggregate amount |
| s 155(3) | 3153 | encoded | ssp: s 155(3) the day on which the maximum entitlement is reached |
| s 155(4) | 3154 | encoded | ssp: s 155(4) the number of times the weekly rate that makes up the entitlement limit |
| s 155(5) | 3155 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 156 | 3156 | inert | reason 1: a heading; creates no rule |
| s 156(1) | 3157 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 156(2) | 3158 | encoded | ssp: s 156(2) the employer is entitled to withhold payment for the day |
| s 156(2)(a) | 3159 | encoded | ssp: s 156(2) the employer is entitled to withhold payment for the day |
| s 156(2)(b) | 3160 | repealed or blank in this text | the converter shows only dots |
| s 156(3) | 3161 | encoded | ssp: s 156(3)(a) the period of entitlement is affected by the withholding; ssp: s 156(3)(b) the amount counted towards the maximum entitlement in pounds |
| s 156(3)(a) | 3162 | encoded | ssp: s 156(3)(a) the period of entitlement is affected by the withholding; ssp: s 156(3)(b) the amount counted towards the maximum entitlement in pounds |
| s 156(3)(b) | 3163 | encoded | ssp: s 156(3)(b) the amount counted towards the maximum entitlement in pounds |
| heading: Rates of payment, etc. | 3164 | inert | reason 1: a heading; creates no rule |
| s 157 | 3165 | inert | reason 1: a heading; creates no rule |
| s 157(1) | 3166 | fork | F-specified; rule: ssp: s 157(1) the weekly rate of statutory sick pay specified in section 157(1) in pounds |
| s 157(1)(a) | 3167 | encoded | ssp: s 157(1)(a) the weekly rate cap in pounds |
| s 157(1)(b) | 3168 | encoded | ssp: s 157(1)(a) the weekly rate cap in pounds |
| s 157(2) | 3169 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 157(2)(a) | 3170 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 157(2)(b) | 3171 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 157(3) | 3172 | encoded | ssp: s 157(3) the amount of statutory sick pay payable in respect of the day in pounds |
| s 158 | 3173 | inert | reason 1: a heading; creates no rule |
| s 158 dots line at 3174 | 3174 | repealed or blank in this text | the converter shows only dots |
| s 159 | 3175 | inert | reason 1: a heading; creates no rule |
| s 159 dots line at 3176 | 3176 | repealed or blank in this text | the converter shows only dots |
| s 159A | 3177 | inert | reason 1: a heading; creates no rule |
| s 159A(1) | 3178 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(2) | 3179 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(2)(a) | 3180 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(2)(b) | 3181 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(2)(c) | 3182 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(2)(d) | 3183-3184 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159A(3) | 3185 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 159A(3) “contributions payments” | 3186 | encoded | ssp: s 159A(3) the payment is a contributions payment |
| s 159A(3) “specified” | 3187 | encoded | ssp: s 159A(3) the figure is specified |
| s 159A(4) | 3188 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 159B | 3189 | inert | reason 1: a heading; creates no rule |
| s 159B dots line at 3190 | 3190 | repealed or blank in this text | the converter shows only dots |
| heading: Miscellaneous | 3191 | inert | reason 1: a heading; creates no rule |
| s 160 | 3192-3193 | inert | reason 1: a heading; creates no rule |
| s 161 | 3194 | inert | reason 1: a heading; creates no rule |
| s 161(1) | 3195 | encoded | ssp: s 161 Part XI applies to the person employed by or under the Crown |
| s 161(2) | 3196 | encoded | ssp: s 161 Part XI applies to the person employed by or under the Crown |
| s 161(3) | 3197 | encoded | ssp: s 161(3) the establishment or organisation is part of Her Majesty's forces |
| s 162 | 3198 | inert | reason 1: a heading; creates no rule |
| s 162(1) | 3199 | encoded | ssp: s 162(1) regulations may modify Part XI in its application to the person |
| s 162(1)(a) | 3200 | encoded | ssp: s 162(1) regulations may modify Part XI in its application to the person |
| s 162(1)(b) | 3201 | encoded | ssp: s 162(1) regulations may modify Part XI in its application to the person |
| s 162(1)(c) | 3202 | encoded | ssp: s 162(1) regulations may modify Part XI in its application to the person |
| s 162(2) | 3203 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 162(2)(a) | 3204 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 162(2)(b) | 3205 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 162(2)(c) | 3206 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 162(2)(d) | 3207 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163 | 3208 | inert | reason 1: a heading; creates no rule |
| s 163(1) | 3209 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 163(1) “contract of service” | 3210 | encoded | ssp: s 163(1) the arrangement counts as a contract of service |
| s 163(1) “employee” | 3211-3212 | encoded | ssp: s 163(1) the person is an employee |
| s 163(1) dots line at 3213 | 3213 | repealed or blank in this text | the converter shows only dots |
| s 163(1) “employee” closing words | 3214 | encoded | ssp: s 163(1) the person is an employee |
| s 163(1) “employer” | 3215-3219 | encoded | ssp: s 163(1) the person is the employer in relation to the employee and the contract of service |
| s 163(1) “period of entitlement” | 3220 | encoded | ssp: s 163(1) the section that gives the meaning of the term |
| s 163(1) “period of incapacity for work” | 3221 | encoded | ssp: s 163(1) the section that gives the meaning of the term |
| s 163(1) dots line at 3222 | 3222 | repealed or blank in this text | the converter shows only dots |
| s 163(1) “prescribed” | 3223 | encoded | ssp: s 163(1) the thing is prescribed |
| s 163(1) “qualifying day” | 3224 | encoded | ssp: s 163(1) the section that gives the meaning of the term |
| s 163(1) “week” | 3225 | encoded | ssp: s 163(1) the week convention of Part XI |
| s 163(2) | 3226 | encoded | ssp: s 163(2) the employee's normal weekly earnings in pounds |
| s 163(3) | 3227 | encoded | ssp: s 163(2) the employee's normal weekly earnings in pounds |
| s 163(4) | 3228 | encoded | ssp: s 163(2) the employee's normal weekly earnings in pounds |
| s 163(5) | 3229 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(5)(a) | 3230 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(5)(b) | 3231 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6) | 3232 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(a) | 3233 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(b) | 3234 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(c) | 3235 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(d) | 3236 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(e) | 3237 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(6)(f) | 3238-3239 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 163(7) | 3240 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| heading: Part XII | 3241 | inert | reason 1: a heading; creates no rule |
| s 164 | 3242 | inert | reason 1: a heading; creates no rule |
| s 164(1) | 3243 | encoded | smp: s 164(1) the woman is entitled to payments of statutory maternity pay |
| s 164(2) | 3244 | encoded | smp: s 164(2)(a) she has been in employed earner's employment with an employer for a continuous period of at least 26 weeks and has ceased to work for him; smp: s 164(2) the conditions mentioned in subsection (1) are satisfied |
| s 164(2)(a) | 3245 | encoded | smp: s 164(2)(a) the number of weeks of continuous employment required; smp: s 164(2)(a) she has been in employed earner's employment with an employer for a continuous period of at least 26 weeks and has ceased to work for him; smp: s 164 the relevant week |
| s 164(2)(b) | 3246 | encoded | smp: s 164(2)(b) her normal weekly earnings are not less than the lower earnings limit; smp: s 164 the relevant week |
| s 164(2)(c) | 3247 | encoded | smp: s 164(2)(c) she has become pregnant and has reached, or been confined before reaching, the commencement of the 11th week |
| s 164(3) | 3248 | encoded | smp: s 164(3) the liability to make payments of statutory maternity pay is the person's |
| s 164(4) | 3249 | encoded | smp: s 164(4)(b) the number of days of notice required |
| s 164(4)(a) | 3250 | encoded | smp: s 164(4)(b) the number of days of notice required |
| s 164(4)(b) | 3251 | encoded | smp: s 164(4)(b) the number of days of notice required |
| s 164(5) | 3252 | encoded | smp: s 164(5) the notice shall be in writing |
| s 164(6) | 3253 | encoded | smp: s 164(6) the agreement is void to the extent that it purports |
| s 164(6)(a) | 3254 | encoded | smp: s 164(6) the agreement is void to the extent that it purports |
| s 164(6)(b) | 3255 | encoded | smp: s 164(6) the agreement is void to the extent that it purports |
| s 164(7) | 3256 | encoded | smp: s 164(7) the agreement is protected from being void by virtue of subsection (6)(a) |
| s 164(7)(a) | 3257 | encoded | smp: s 164(7) the agreement is protected from being void by virtue of subsection (6)(a) |
| s 164(7)(b) | 3258 | encoded | smp: s 164(7) the agreement is protected from being void by virtue of subsection (6)(a) |
| s 164(8) | 3259 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9) | 3260 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(a) | 3261 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(b) | 3262 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(c) | 3263 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(d) | 3264 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(d)(i) | 3265 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(d)(ii) | 3266 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(e) | 3267 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(ea) | 3268 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(f) | 3269 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(g) | 3270 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(g)(i) | 3271 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(9)(g)(ii) | 3272-3273 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(10) | 3274 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(10)(a) | 3275 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(10)(b) | 3276 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 164(11) | 3277 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165 | 3278 | inert | reason 1: a heading; creates no rule |
| s 165(1) | 3279 | encoded | smp: s 165(1) the longest maternity pay period in weeks; smp: s 165(1) the maternity pay period |
| s 165(2) | 3280 | encoded | smp: s 165(2) the day on which the maternity pay period begins |
| s 165(3) | 3281 | encoded | smp: s 165(3) the prescribed first day is permitted |
| s 165(3A) | 3282 | encoded | smp: s 165(3A) the maternity pay period as reduced; smp: s 165(3A) the woman would be entitled to statutory maternity pay for the week but for the reduction in the maternity pay period |
| s 165(3B) | 3283 | encoded | smp: s 165(3B) the reduced period ends at a time the regulations may allow |
| s 165(3B)(a) | 3284 | encoded | smp: s 165(3B) the reduced period ends at a time the regulations may allow |
| s 165(3B)(b) | 3285 | encoded | smp: s 165(3B) the reduced period ends at a time the regulations may allow |
| s 165(3C) | 3286 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(3C)(a) | 3287 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(3C)(b) | 3288 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(3C)(c) | 3289 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(3C)(d) | 3290 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(3D) | 3291 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(4) | 3292 | encoded | smp: s 165(4) statutory maternity pay is payable by the person for the week |
| s 165(5) | 3293 | encoded | smp: s 165(5) the work counts for subsection (4) whichever contract it is under |
| s 165(6) | 3294 | encoded | smp: s 165(6) statutory maternity pay is payable for the week after confinement |
| s 165(7) | 3295 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(7)(a) | 3296 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(7)(b) | 3297 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(7)(b)(i) | 3298 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(7)(b)(ii) | 3299 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 165(8) | 3300 | encoded | smp: s 165(8) the week convention of subsections (1), (4) and (6); smp: s 165(8) the first day of the week of the maternity pay period containing the day |
| s 166 | 3301 | inert | reason 1: a heading; creates no rule |
| s 166(1) | 3302 | encoded | smp: s 166(1) the weekly rate of statutory maternity pay for the week in pounds |
| s 166(1)(a) | 3303 | encoded | smp: s 166(1)(a) the number of weeks payable at the earnings-related rate; smp: s 166(1) the weekly rate of statutory maternity pay for the week in pounds |
| s 166(1)(b) | 3304 | encoded | smp: s 166(1) the weekly rate of statutory maternity pay for the week in pounds |
| s 166(1A) | 3305 | encoded | smp: s 166(1A) the week convention of section 166(1) |
| s 166(2) | 3306 | encoded | smp: s 166(2) the percentage of normal weekly earnings |
| s 166(3) | 3307 | fork | F-specified; rule: smp: s 166(3) the weekly rate prescribed is not less than the weekly rate of statutory sick pay |
| s 166(4) | 3308 | encoded | smp: s 166(4) the daily rate of statutory maternity pay in pounds |
| s 167 | 3309 | inert | reason 1: a heading; creates no rule |
| s 167(1) | 3310 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(2) | 3311 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(2)(a) | 3312 | encoded | smp: s 167(2)(a) the amount the regulations must provide for the payer to be entitled to recover in pounds |
| s 167(2)(a)(i) | 3313 | encoded | smp: s 167(2)(a) the amount the regulations must provide for the payer to be entitled to recover in pounds |
| s 167(2)(a)(ii) | 3314 | encoded | smp: s 167(2)(a)(ii) the percentage recoverable of payments that do not qualify for small employers' relief; smp: s 167(2)(a) the amount the regulations must provide for the payer to be entitled to recover in pounds |
| s 167(2)(b) | 3315 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(2)(b)(i) | 3316 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(2)(b)(ii) | 3317 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(2)(b)(iii) | 3318 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(3) | 3319 | encoded | smp: s 167(3) the payment qualifies for small employers' relief |
| s 167(4) | 3320 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(4)(a) | 3321 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(4)(b) | 3322 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(4)(b)(i) | 3323 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(4)(b)(ii) | 3324 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(5) | 3325 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(5)(a) | 3326 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(5)(b) | 3327 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(5)(c) | 3328 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(6) | 3329 | encoded | smp: s 167(6) the amount deducted is treated as paid towards discharging the employer's liability |
| s 167(6)(a) | 3330 | encoded | smp: s 167(6) the amount deducted is treated as paid towards discharging the employer's liability |
| s 167(6)(b) | 3331-3332 | encoded | smp: s 167(6) the amount deducted is treated as paid towards discharging the employer's liability |
| s 167(7) | 3333 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 167(8) | 3334 | encoded | smp: s 167(8) the payment is a contributions payment |
| s 168 | 3335-3336 | inert | reason 1: a heading; creates no rule |
| s 169 | 3337-3338 | inert | reason 1: a heading; creates no rule |
| s 170 | 3339 | inert | reason 1: a heading; creates no rule |
| s 170(1) | 3340 | encoded | smp: s 170(1) regulations may modify Part XII in its application to her |
| s 170(1)(a) | 3341 | encoded | smp: s 170(1) regulations may modify Part XII in its application to her |
| s 170(1)(b) | 3342 | encoded | smp: s 170(1) regulations may modify Part XII in its application to her |
| s 170(1)(c) | 3343 | encoded | smp: s 170(1) regulations may modify Part XII in its application to her |
| s 170(2) | 3344 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 170(2)(a) | 3345 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 170(2)(b) | 3346 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 170(2)(c) | 3347 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 170(2)(d) | 3348 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171 | 3349 | inert | reason 1: a heading; creates no rule |
| s 171(1) | 3350 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 171(1) “confinement” | 3351-3354 | fork | F-24; rule: smp: s 171(1) she is confined |
| s 171(1) “dismissed” | 3355 | encoded | smp: s 171(1) she was dismissed |
| s 171(1) “employee” | 3356-3357 | encoded | smp: s 171(1) she is an employee |
| s 171(1) dots line at 3358 | 3358 | repealed or blank in this text | the converter shows only dots |
| s 171(1) “employee” closing words | 3359 | encoded | smp: s 171(1) she is an employee |
| s 171(1) “employer” | 3360-3364 | encoded | smp: s 171(1) the person is the employer in relation to her |
| s 171(1) “maternity pay period” | 3365 | encoded | smp: s 171(1) the maternity pay period |
| s 171(1) “modifications” | 3366 | encoded | smp: s 171(1) the change is a modification |
| s 171(1) “prescribed” | 3367 | encoded | smp: s 171(1) the thing is prescribed |
| s 171(1) dots line at 3368 | 3368 | repealed or blank in this text | the converter shows only dots |
| s 171(1A) | 3369 | encoded | smp: s 171(1A) the week convention of Part XII; smp: s 171(1A) the first day of the week containing the day |
| s 171(2) | 3370 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(2)(a) | 3371 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(2)(b) | 3372 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3) | 3373 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(a) | 3374 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(b) | 3375 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(c) | 3376 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(d) | 3377 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(e) | 3378 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(3)(f) | 3379-3380 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171(4) | 3381 | encoded | smp: s 171(4) her normal weekly earnings in pounds |
| s 171(5) | 3382 | encoded | smp: s 171(4) her normal weekly earnings in pounds |
| s 171(6) | 3383 | encoded | smp: s 171(4) her normal weekly earnings in pounds |
| s 171(7) | 3384 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| heading: Part 12ZA | 3385 | inert | reason 1: a heading; creates no rule |
| omission line at 3386 | 3386 | repealed or blank in this text | the converter shows only dots |
| s 171ZA | 3387 | inert | reason 1: a heading; creates no rule |
| s 171ZA(1) | 3388 | encoded | spp: s 171ZA(1) he is entitled to statutory paternity pay on a birth |
| s 171ZA(2) | 3389 | encoded | spp: s 171ZA(2) the conditions are satisfied |
| s 171ZA(2)(a) | 3390 | encoded | spp: s 171ZA(2)(a) he satisfies prescribed conditions as to relationship with a newborn child and with the child's mother |
| s 171ZA(2)(a)(i) | 3391 | encoded | spp: s 171ZA(2)(a) he satisfies prescribed conditions as to relationship with a newborn child and with the child's mother |
| s 171ZA(2)(a)(ii) | 3392 | encoded | spp: s 171ZA(2)(a) he satisfies prescribed conditions as to relationship with a newborn child and with the child's mother |
| s 171ZA(2)(b) | 3393 | encoded | spp: s 171ZA(2)(b) the number of weeks of continuous employment required; spp: s 171ZA(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 weeks ending with the relevant week |
| s 171ZA(2)(c) | 3394 | encoded | spp: s 171ZA(2)(c) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week |
| s 171ZA(2)(d) | 3395 | encoded | spp: s 171ZA(2)(d) he has been in employed earner's employment with that employer from the end of the relevant week to the day the child is born |
| s 171ZA(3) | 3396 | encoded | spp: s 171ZA(2) the relevant week |
| s 171ZA(4) | 3397 | encoded | spp: s 171ZA(4) the entitlement is affected by the birth, or expected birth, of more than one child |
| s 171ZA(5) | 3398 | fork | F-24; rule: spp: s 171ZA(5) a child stillborn counts as a newborn child |
| s 171ZB | 3399 | inert | reason 1: a heading; creates no rule |
| s 171ZB(1) | 3400 | encoded | spp: s 171ZB(1) he is entitled to statutory paternity pay on an adoption |
| s 171ZB(2) | 3401 | encoded | spp: s 171ZB(2) the conditions are satisfied |
| s 171ZB(2)(a) | 3402 | encoded | spp: s 171ZB(2)(a) he satisfies prescribed conditions as to relationship with the child and with the person with whom the child is placed |
| s 171ZB(2)(a)(i) | 3403 | encoded | spp: s 171ZB(2)(a) he satisfies prescribed conditions as to relationship with the child and with the person with whom the child is placed |
| s 171ZB(2)(a)(ii) | 3404 | encoded | spp: s 171ZB(2)(a) he satisfies prescribed conditions as to relationship with the child and with the person with whom the child is placed |
| s 171ZB(2)(b) | 3405 | encoded | spp: s 171ZB(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 weeks ending with the relevant week |
| s 171ZB(2)(c) | 3406 | encoded | spp: s 171ZB(2)(c) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week |
| s 171ZB(2)(d) | 3407 | encoded | spp: s 171ZB(2)(d) he has been in employed earner's employment with that employer from the end of the relevant week to the day the child is placed |
| s 171ZB(2)(e) | 3408 | fork | F-e; rule: spp: s 171ZB(2)(e) where he is a person with whom the child is placed, he has elected to receive statutory paternity pay |
| s 171ZB(3) | 3409 | fork | F-adopter; rule: spp: s 171ZB(2) the relevant week |
| s 171ZB(4) | 3410 | encoded | spp: s 171ZB(4) he may elect to receive statutory paternity pay |
| s 171ZB(5) | 3411 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZB(6) | 3412 | encoded | spp: s 171ZB(6) the entitlement is affected by the placement for adoption of more than one child |
| s 171ZB(7) | 3413 | fork | F-adopter; rule: spp: s 171ZB(7) the person is the adopter |
| s 171ZB(8) | 3414 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(8)(a) | 3415 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(8)(b) | 3416 | encoded | spp: s 171ZB(2) the relevant week |
| s 171ZB(8)(c) | 3417 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(8)(d) | 3418 | encoded | spp: s 171ZB(7) the person is the adopter |
| s 171ZB(9) | 3419 | encoded | spp: s 171ZB(9) he may become entitled in connection with the placement of the child for adoption |
| s 171ZB(10) | 3420 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(10)(a) | 3421 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(10)(b) | 3422 | encoded | spp: s 171ZB(2) the relevant week |
| s 171ZB(10)(c) | 3423 | encoded | spp: s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZB(10)(d) | 3424 | encoded | spp: s 171ZB(7) the person is the adopter |
| s 171ZB(11) | 3425 | encoded | spp: s 171ZB(11) he may become entitled in connection with the placement of the child for adoption |
| s 171ZC | 3426 | inert | reason 1: a heading; creates no rule |
| s 171ZC(1) | 3427 | encoded | spp: s 171ZC(1) the notice condition for payments of statutory paternity pay is met |
| s 171ZC(1A) | 3428 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(2) | 3429 | encoded | spp: s 171ZC(2) the notice shall be in writing |
| s 171ZC(3) | 3430 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(a) | 3431 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(b) | 3432 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(c) | 3433 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(d) | 3434 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(e) | 3435 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(e)(i) | 3436 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(e)(ii) | 3437 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(f) | 3438 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(g) | 3439 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(g)(i) | 3440 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZC(3)(g)(ii) | 3441-3442 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZD | 3443 | inert | reason 1: a heading; creates no rule |
| s 171ZD(1) | 3444 | encoded | spp: s 171ZD(1) the liability to make payments of statutory paternity pay is the person's |
| s 171ZD(2) | 3445 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZD(3) | 3446 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZE | 3447 | inert | reason 1: a heading; creates no rule |
| s 171ZE(1) | 3448 | encoded | spp: s 171ZE(1) the weekly rate of statutory paternity pay in pounds |
| s 171ZE(2) | 3449 | encoded | spp: s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable |
| s 171ZE(2)(a) | 3450 | encoded | spp: s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable |
| s 171ZE(2)(b) | 3451 | encoded | spp: s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable |
| s 171ZE(2)(b)(i) | 3452 | encoded | spp: s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable |
| s 171ZE(2)(b)(ii) | 3453-3454 | encoded | spp: s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable |
| s 171ZE(3) | 3455 | encoded | spp: s 171ZE(3) the day on which the qualifying period begins; spp: s 171ZE(3) the least length of the qualifying period in days |
| s 171ZE(3)(a) | 3456 | encoded | spp: s 171ZE(3) the day on which the qualifying period begins |
| s 171ZE(3)(b) | 3457 | encoded | spp: s 171ZE(3) the day on which the qualifying period begins |
| s 171ZE(3A) | 3458 | encoded | spp: s 171ZE(3A) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(3A)(a) | 3459 | encoded | spp: s 171ZE(3A) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(3A)(b) | 3460 | encoded | spp: s 171ZE(3A) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(4) | 3461 | fork | F-purpose; rule: spp: s 171ZE(4) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(4)(a) | 3462 | fork | F-purpose; rule: spp: s 171ZE(4) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(4)(b) | 3463 | fork | F-purpose; rule: spp: s 171ZE(4) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(5) | 3464 | encoded | spp: s 171ZE(5) the person is liable to pay statutory paternity pay to the other in respect of the statutory pay week |
| s 171ZE(6) | 3465 | encoded | spp: s 171ZE(5) the person is liable to pay statutory paternity pay to the other in respect of the statutory pay week |
| s 171ZE(7) | 3466 | encoded | spp: s 171ZE(7) statutory paternity pay is payable to him in respect of the statutory pay week |
| s 171ZE(8) | 3467 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZE(9) | 3468 | encoded | spp: s 171ZE(3) the day on which the qualifying period begins |
| s 171ZE(10) | 3469 | encoded | spp: s 171ZE(3) the day on which the qualifying period begins |
| s 171ZE(10A) | 3470 | encoded | spp: s 171ZE(10A) the daily rate of statutory paternity pay in pounds |
| s 171ZE(11) | 3471 | encoded | spp: s 171ZE(11) the week is a statutory pay week |
| s 171ZE(11) “statutory pay week” | 3472 | encoded | spp: s 171ZE(11) the week is a statutory pay week |
| s 171ZE(11) “week” | 3473 | encoded | spp: s 171ZE(11) the week convention of section 171ZE |
| s 171ZE(12) | 3474 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| s 171ZE(12)(a) | 3475 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| s 171ZE(12)(b) | 3476 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| s 171ZE(13) | 3477 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| s 171ZE(13)(a) | 3478 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| s 171ZE(13)(b) | 3479 | encoded | spp: s 171ZE(12) the placement that the references to placement for adoption are read as |
| omission line at 3480 | 3480 | repealed or blank in this text | the converter shows only dots |
| s 171ZEA | 3481 | inert | reason 1: a heading; creates no rule |
| s 171ZEA dots line at 3482 | 3482 | repealed or blank in this text | the converter shows only dots |
| s 171ZEB | 3483 | inert | reason 1: a heading; creates no rule |
| s 171ZEB dots line at 3484 | 3484 | repealed or blank in this text | the converter shows only dots |
| s 171ZEC | 3485 | inert | reason 1: a heading; creates no rule |
| s 171ZEC dots line at 3486 | 3486 | repealed or blank in this text | the converter shows only dots |
| s 171ZED | 3487 | inert | reason 1: a heading; creates no rule |
| s 171ZED dots line at 3488 | 3488 | repealed or blank in this text | the converter shows only dots |
| s 171ZEE | 3489 | inert | reason 1: a heading; creates no rule |
| s 171ZEE dots line at 3490 | 3490 | repealed or blank in this text | the converter shows only dots |
| omission line at 3491 | 3491 | repealed or blank in this text | the converter shows only dots |
| s 171ZF | 3492 | inert | reason 1: a heading; creates no rule |
| s 171ZF(1) | 3493 | encoded | spp: s 171ZF(1) the agreement is void to the extent that it purports |
| s 171ZF(1)(a) | 3494 | encoded | spp: s 171ZF(1) the agreement is void to the extent that it purports |
| s 171ZF(1)(b) | 3495 | encoded | spp: s 171ZF(1) the agreement is void to the extent that it purports |
| s 171ZF(2) | 3496 | encoded | spp: s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZF(2)(a) | 3497 | encoded | spp: s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZF(2)(b) | 3498 | encoded | spp: s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZG | 3499 | inert | reason 1: a heading; creates no rule |
| s 171ZG(1) | 3500 | encoded | spp: s 171ZG(1) the entitlement to statutory paternity pay affects his right to contractual remuneration |
| s 171ZG(2) | 3501 | fork | F-credit; rule: spp: s 171ZG(2)(a) the statutory paternity pay still owed for the period in pounds; spp: s 171ZG(2)(b) the contractual remuneration still owed for the period in pounds |
| s 171ZG(2)(a) | 3502 | fork | F-credit; rule: spp: s 171ZG(2)(a) the statutory paternity pay still owed for the period in pounds |
| s 171ZG(2)(b) | 3503 | fork | F-credit; rule: spp: s 171ZG(2)(b) the contractual remuneration still owed for the period in pounds |
| s 171ZG(3) | 3504 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZG(4) | 3505 | repealed or blank in this text | the converter shows only dots |
| s 171ZH | 3506-3507 | inert | reason 1: a heading; creates no rule |
| s 171ZI | 3508 | inert | reason 1: a heading; creates no rule |
| s 171ZI(1) | 3509 | encoded | spp: s 171ZI(1) regulations may modify Part 12ZA in its application to the person |
| s 171ZI(1)(a) | 3510 | encoded | spp: s 171ZI(1) regulations may modify Part 12ZA in its application to the person |
| s 171ZI(1)(b) | 3511 | encoded | spp: s 171ZI(1) regulations may modify Part 12ZA in its application to the person |
| s 171ZI(1)(c) | 3512 | encoded | spp: s 171ZI(1) regulations may modify Part 12ZA in its application to the person |
| s 171ZI(2) | 3513 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZI(2)(a) | 3514 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZI(2)(b) | 3515 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZI(2)(c) | 3516 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZI(2)(d) | 3517 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ | 3518 | inert | reason 1: a heading; creates no rule |
| s 171ZJ(1) | 3519 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 171ZJ(1) “the Board” | 3520 | encoded | spp: s 171ZJ(1) the Board |
| s 171ZJ(1) “employer” | 3521-3525 | encoded | spp: s 171ZJ(1) the person is the employer in relation to the employee |
| s 171ZJ(1) “local authority” | 3526 | encoded | spp: s 171ZJ(1) the body is a local authority |
| s 171ZJ(1) “local authority foster parent” | 3527 | encoded | spp: s 171ZJ(1) the body is a local authority |
| s 171ZJ(1) “modifications” | 3528 | encoded | spp: s 171ZJ(1) the change is a modification |
| s 171ZJ(1) “prescribed” | 3529 | encoded | spp: s 171ZJ(1) the thing is prescribed |
| s 171ZJ(2) | 3530 | encoded | spp: s 171ZJ(2) the person is an employee |
| s 171ZJ(2)(a) | 3531 | encoded | spp: s 171ZJ(2) the person is an employee |
| s 171ZJ(2)(b) | 3532 | repealed or blank in this text | the converter shows only dots |
| s 171ZJ(3) | 3533 | encoded | spp: s 171ZJ(2) the person is an employee |
| s 171ZJ(3)(a) | 3534 | encoded | spp: s 171ZJ(2) the person is an employee |
| s 171ZJ(3)(b) | 3535 | encoded | spp: s 171ZJ(2) the person is an employee |
| s 171ZJ(4) | 3536 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(4)(a) | 3537 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(4)(b) | 3538 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(5) | 3539 | encoded | spp: s 171ZJ(5) the first day of the week containing the day; spp: s 171ZJ(5) the week convention of Part 12ZA |
| s 171ZJ(6) | 3540 | encoded | spp: s 171ZJ(6) his normal weekly earnings in pounds |
| s 171ZJ(7) | 3541 | encoded | spp: s 171ZJ(6) his normal weekly earnings in pounds |
| s 171ZJ(8) | 3542 | encoded | spp: s 171ZJ(6) his normal weekly earnings in pounds |
| s 171ZJ(9) | 3543 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(9)(a) | 3544 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(9)(b) | 3545-3546 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10) | 3547 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(a) | 3548 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(b) | 3549 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(c) | 3550 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(d) | 3551 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(e) | 3552 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(10)(f) | 3553 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(11) | 3554 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZJ(12) | 3555 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZK | 3556 | inert | reason 1: a heading; creates no rule |
| s 171ZK(1) | 3557 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZK(2) | 3558 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| heading: Part 12ZB | 3559 | inert | reason 1: a heading; creates no rule |
| s 171ZL | 3560 | inert | reason 1: a heading; creates no rule |
| s 171ZL(1) | 3561 | encoded | sap: s 171ZL(1) he is entitled to statutory adoption pay |
| s 171ZL(2) | 3562 | encoded | sap: s 171ZL(2) the conditions are satisfied |
| s 171ZL(2)(a) | 3563 | encoded | sap: s 171ZL(2)(a) he is a person with whom a child is, or is expected to be, placed for adoption |
| s 171ZL(2)(b) | 3564 | encoded | sap: s 171ZL(2)(b) the number of weeks of continuous employment required; sap: s 171ZL(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 weeks ending with the relevant week |
| s 171ZL(2)(c) | 3565 | encoded | sap: s 171ZL(2)(c) he has ceased to work for the employer |
| s 171ZL(2)(d) | 3566 | encoded | sap: s 171ZL(2)(d) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week |
| s 171ZL(2)(e) | 3567 | encoded | sap: s 171ZL(2)(e) he has elected to receive statutory adoption pay |
| s 171ZL(3) | 3568 | encoded | sap: s 171ZL(2) the relevant week |
| s 171ZL(4) | 3569 | encoded | sap: s 171ZL(4) he may elect to receive statutory adoption pay |
| s 171ZL(4)(a) | 3570 | encoded | sap: s 171ZL(4) he may elect to receive statutory adoption pay |
| s 171ZL(4)(b) | 3571 | encoded | sap: s 171ZL(4) he may elect to receive statutory adoption pay |
| s 171ZL(4A) | 3572 | encoded | sap: s 171ZL(4A) he falls within the subsection |
| s 171ZL(4A)(a) | 3573 | encoded | sap: s 171ZL(4A) he falls within the subsection |
| s 171ZL(4A)(b) | 3574 | encoded | sap: s 171ZL(4A) he falls within the subsection |
| s 171ZL(4A)(c) | 3575 | encoded | sap: s 171ZL(4A) he falls within the subsection |
| s 171ZL(4B) | 3576 | encoded | sap: s 171ZL(4B) he is a member of a couple |
| s 171ZL(4B)(a) | 3577 | encoded | sap: s 171ZL(4B) he is a member of a couple |
| s 171ZL(4B)(b) | 3578 | repealed or blank in this text | the converter shows only dots |
| s 171ZL(4B)(c) | 3579 | encoded | sap: s 171ZL(4B) he is a member of a couple |
| s 171ZL(5) | 3580 | encoded | sap: s 171ZL(5) the entitlement is affected by the placement, or expected placement, of more than one child |
| s 171ZL(6) | 3581 | encoded | sap: s 171ZL(6) the notice condition for payments of statutory adoption pay is met |
| s 171ZL(6)(a) | 3582 | encoded | sap: s 171ZL(6)(a) he gives the notice of the date the liability is to begin |
| s 171ZL(6)(b) | 3583 | encoded | sap: s 171ZL(6)(b) the least number of days of notice before the liability begins; sap: s 171ZL(6)(b) the notice is given at least 28 days before that date or, if that is not reasonably practicable, as soon as is reasonably practicable |
| s 171ZL(7) | 3584 | encoded | sap: s 171ZL(7) the notice shall be in writing |
| s 171ZL(8) | 3585 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(a) | 3586 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(b) | 3587 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(c) | 3588 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(d) | 3589 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(e) | 3590 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(e)(i) | 3591 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(e)(ii) | 3592 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(f) | 3593 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(g) | 3594 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(g)(i) | 3595 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(g)(ii) | 3596-3597 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(8)(h) | 3598 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZL(9) | 3599 | encoded | sap: s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZL(9)(a) | 3600 | encoded | sap: s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZL(9)(b) | 3601 | encoded | sap: s 171ZL(2) the relevant week |
| s 171ZL(9)(c) | 3602 | encoded | sap: s 171ZL(4B) he is a member of a couple |
| s 171ZL(9)(d) | 3603 | encoded | sap: s 171ZL(5) the entitlement is affected by the placement, or expected placement, of more than one child |
| s 171ZL(10) | 3604 | encoded | sap: s 171ZL(10) he may become entitled as a result of the child being placed for adoption |
| s 171ZL(11) | 3605 | encoded | sap: s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZL(11)(a) | 3606 | encoded | sap: s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied |
| s 171ZL(11)(b) | 3607 | encoded | sap: s 171ZL(2) the relevant week |
| s 171ZL(11)(c) | 3608 | encoded | sap: s 171ZL(4B) he is a member of a couple |
| s 171ZL(11)(d) | 3609 | encoded | sap: s 171ZL(5) the entitlement is affected by the placement, or expected placement, of more than one child |
| s 171ZL(12) | 3610 | encoded | sap: s 171ZL(12) he may become entitled as a result of the child being placed for adoption |
| s 171ZM | 3611 | inert | reason 1: a heading; creates no rule |
| s 171ZM(1) | 3612 | encoded | sap: s 171ZM(1) the liability to make payments of statutory adoption pay is the person's |
| s 171ZM(2) | 3613 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZM(3) | 3614 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN | 3615 | inert | reason 1: a heading; creates no rule |
| s 171ZN(1) | 3616 | repealed or blank in this text | the converter shows only dots |
| s 171ZN(2) | 3617 | encoded | sap: s 171ZN(2) the longest adoption pay period in weeks; sap: s 171ZN(2) the adoption pay period |
| s 171ZN(2A) | 3618 | encoded | sap: s 171ZN(2A) the adoption pay period as reduced |
| s 171ZN(2B) | 3619 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2B)(a) | 3620 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2B)(b) | 3621 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2C) | 3622 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2C)(a) | 3623 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2C)(b) | 3624 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2C)(c) | 3625 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2C)(d) | 3626 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2D) | 3627 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(2E) | 3628 | encoded | sap: s 171ZN(2E) the weekly rate of statutory adoption pay for the week in pounds |
| s 171ZN(2E)(a) | 3629 | encoded | sap: s 171ZN(2E)(a) the number of weeks payable at the earnings-related rate; sap: s 171ZN(2E) the weekly rate of statutory adoption pay for the week in pounds |
| s 171ZN(2E)(b) | 3630 | encoded | sap: s 171ZN(2E) the weekly rate of statutory adoption pay for the week in pounds |
| s 171ZN(2F) | 3631 | encoded | sap: s 171ZN(2F) the percentage of normal weekly earnings; sap: s 171ZN(2F) the earnings-related rate in pounds |
| s 171ZN(2G) | 3632 | fork | F-specified; rule: sap: s 171ZN(2G) the weekly rate prescribed is not less than the weekly rate of statutory sick pay |
| s 171ZN(3) | 3633 | encoded | sap: s 171ZN(3) the person is liable to pay statutory adoption pay to the other in respect of the week |
| s 171ZN(4) | 3634 | encoded | sap: s 171ZN(3) the person is liable to pay statutory adoption pay to the other in respect of the week |
| s 171ZN(5) | 3635 | encoded | sap: s 171ZN(5) statutory adoption pay is payable to him in respect of the week |
| s 171ZN(6) | 3636 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZN(6A) | 3637 | encoded | sap: s 171ZN(6A) the daily rate of statutory adoption pay in pounds |
| s 171ZN(7) | 3638 | encoded | sap: s 171ZN(7) the week convention of subsections (2) and (2E) |
| s 171ZN(8) | 3639 | encoded | sap: s 171ZN(8) the week convention of subsections (3), (5) and (6); sap: s 171ZN(8) the first day of the week of the adoption pay period containing the day |
| s 171ZN(9) | 3640 | encoded | sap: s 171ZN(9) the placement that the notification in subsection (2F) is read as |
| s 171ZN(10) | 3641 | encoded | sap: s 171ZN(9) the placement that the notification in subsection (2F) is read as |
| s 171ZO | 3642 | inert | reason 1: a heading; creates no rule |
| s 171ZO(1) | 3643 | encoded | sap: s 171ZO(1) the agreement is void to the extent that it purports |
| s 171ZO(1)(a) | 3644 | encoded | sap: s 171ZO(1) the agreement is void to the extent that it purports |
| s 171ZO(1)(b) | 3645 | encoded | sap: s 171ZO(1) the agreement is void to the extent that it purports |
| s 171ZO(2) | 3646 | encoded | sap: s 171ZO(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZO(2)(a) | 3647 | encoded | sap: s 171ZO(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZO(2)(b) | 3648 | encoded | sap: s 171ZO(2) the agreement is protected from being void by virtue of subsection (1)(a) |
| s 171ZP | 3649 | inert | reason 1: a heading; creates no rule |
| s 171ZP(1) | 3650 | encoded | sap: s 171ZP(1) the day is treated as a day of incapacity for work |
| s 171ZP(2) | 3651 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZP(3) | 3652 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZP(4) | 3653 | encoded | sap: s 171ZP(4) the entitlement to statutory adoption pay affects his right to contractual remuneration |
| s 171ZP(5) | 3654 | fork | F-credit; rule: sap: s 171ZP(5)(a) the statutory adoption pay still owed for the week in pounds; sap: s 171ZP(5)(b) the contractual remuneration still owed for the week in pounds |
| s 171ZP(5)(a) | 3655 | fork | F-credit; rule: sap: s 171ZP(5)(a) the statutory adoption pay still owed for the week in pounds |
| s 171ZP(5)(b) | 3656 | fork | F-credit; rule: sap: s 171ZP(5)(b) the contractual remuneration still owed for the week in pounds |
| s 171ZP(6) | 3657 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZP(7) | 3658 | encoded | sap: s 171ZP(7) the week convention of subsection (5); sap: s 171ZN(8) the first day of the week of the adoption pay period containing the day |
| s 171ZQ | 3659-3660 | inert | reason 1: a heading; creates no rule |
| s 171ZR | 3661 | inert | reason 1: a heading; creates no rule |
| s 171ZR(1) | 3662 | encoded | sap: s 171ZR(1) regulations may modify Part 12ZB in its application to the person |
| s 171ZR(1)(a) | 3663 | encoded | sap: s 171ZR(1) regulations may modify Part 12ZB in its application to the person |
| s 171ZR(1)(b) | 3664 | encoded | sap: s 171ZR(1) regulations may modify Part 12ZB in its application to the person |
| s 171ZR(1)(c) | 3665 | encoded | sap: s 171ZR(1) regulations may modify Part 12ZB in its application to the person |
| s 171ZR(2) | 3666 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZR(2)(a) | 3667 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZR(2)(b) | 3668 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZR(2)(c) | 3669 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZR(2)(d) | 3670 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS | 3671 | inert | reason 1: a heading; creates no rule |
| s 171ZS(1) | 3672 | inert | reason 1: lead-in words of a list of definitions; each definition has its own row |
| s 171ZS(1) “adoption pay period” | 3673 | encoded | sap: s 171ZS(1) the adoption pay period |
| s 171ZS(1) “the Board” | 3674 | encoded | sap: s 171ZS(1) the Board |
| s 171ZS(1) “employer” | 3675-3679 | encoded | sap: s 171ZS(1) the person is the employer in relation to the employee |
| s 171ZS(1) “local authority” | 3680 | encoded | sap: s 171ZS(1) the body is a local authority |
| s 171ZS(1) “local authority foster parent” | 3681 | encoded | sap: s 171ZS(1) the person is a local authority foster parent |
| s 171ZS(1) “modifications” | 3682 | encoded | sap: s 171ZS(1) the change is a modification |
| s 171ZS(1) “prescribed” | 3683 | encoded | sap: s 171ZS(1) the thing is prescribed |
| s 171ZS(2) | 3684 | encoded | sap: s 171ZS(2) the person is an employee |
| s 171ZS(2)(a) | 3685 | encoded | sap: s 171ZS(2) the person is an employee |
| s 171ZS(2)(b) | 3686 | repealed or blank in this text | the converter shows only dots |
| s 171ZS(3) | 3687 | encoded | sap: s 171ZS(2) the person is an employee |
| s 171ZS(3)(a) | 3688 | encoded | sap: s 171ZS(2) the person is an employee |
| s 171ZS(3)(b) | 3689 | encoded | sap: s 171ZS(2) the person is an employee |
| s 171ZS(4) | 3690 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(4)(a) | 3691 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(4)(b) | 3692 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(5) | 3693 | encoded | sap: s 171ZS(5) the week convention of Part 12ZB; sap: s 171ZS(5) the first day of the week containing the day |
| s 171ZS(6) | 3694 | encoded | sap: s 171ZS(6) his normal weekly earnings in pounds |
| s 171ZS(7) | 3695 | encoded | sap: s 171ZS(6) his normal weekly earnings in pounds |
| s 171ZS(8) | 3696 | encoded | sap: s 171ZS(6) his normal weekly earnings in pounds |
| s 171ZS(9) | 3697 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(9)(a) | 3698 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(9)(b) | 3699-3700 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10) | 3701 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(a) | 3702 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(b) | 3703 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(c) | 3704 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(d) | 3705 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(e) | 3706 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(10)(f) | 3707 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(11) | 3708 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZS(12) | 3709 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT | 3710 | inert | reason 1: a heading; creates no rule |
| s 171ZT(1) | 3711 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(2) | 3712 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(2)(a) | 3713 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(2)(b) | 3714 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(3) | 3715 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(3)(a) | 3716 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |
| s 171ZT(3)(b) | 3717 | inert | reason 2: a power to make regulations or an order, or a duty to make them; its exercise reaches the rules as a prescribed input |

## Fork register (ssc6)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry names the units that rest on it (they have the disposition `fork` in the coverage table), every reading seen, the reading taken, the text that licenses each, and the rule that carries the reading.
Every choice below is assumed, not ruled; the reading not taken is one edit away.
`src:N` is a line of the converter rendering, which is not the official text.

| id | units | the text |
| --- | --- | --- |
| F-gap | s 152(3) | src:3113 "Any two periods of incapacity for work which are separated by a period of not more than 8 weeks shall be treated as a single period of incapacity for work." |
| F-specified | s 157(1), s 166(3), s 171ZN(2G) | src:3166-3168 "The weekly rate of statutory sick pay that an employer must pay to an employee is the lower of— (a) £123.25, and (b) 80% of the employee's normal weekly earnings."; src:3307 "must not be less than the weekly rate of statutory sick pay for the time being specified in section 157(1) above or, if two or more such rates are for the time being so specified, the higher or highest of those rates" |
| F-both | s 153(12) "disqualifying period" | src:3139-3141 "“disqualifying period” means— in relation to a woman entitled to statutory maternity pay, the maternity pay period; and in relation to a woman entitled to maternity allowance, the maternity allowance period;" |
| F-24 | s 153(12) "confinement", s 171(1) "confinement", s 171ZA(5) | src:3352-3353 "labour resulting in the issue of a living child, or labour after 24 weeks of pregnancy resulting in the issue of a child whether alive or dead"; src:3398 "“newborn child” includes a child stillborn after twenty-four weeks of pregnancy" |
| F-e | s 171ZB(2)(e) | src:3408 "(e) where he is a person with whom the child is placed for adoption, that he has elected to receive statutory paternity pay." |
| F-adopter | s 171ZB(3), s 171ZB(7) | src:3409 "the week in which the adopter is notified of being matched with the child"; src:3413 "“adopter”, in relation to a person who satisfies the condition under subsection (2)(a)(ii) above, means the person by reference to whom he satisfies that condition." |
| F-purpose | s 171ZE(4) with (a), (b) | src:3461-3463 "Statutory paternity pay shall not be payable to a person in respect of a statutory pay week if it is not his purpose at the beginning of the week— (a) to care for the child ... or (b) to support the person ..." |
| F-credit | s 171ZG(2) with (a), (b); s 171ZP(5) with (a), (b) | src:3502-3503, src:3655-3656 "any contractual remuneration paid ... shall go towards discharging any liability ... to pay statutory ... pay"; "any statutory ... pay paid ... shall go towards discharging any liability ... to pay contractual remuneration" |

### F-gap: how many days lie "between" two periods of incapacity

- Reading A, taken: the days strictly between the last day of the earlier period and the first day of the later one are counted, so a gap of 56 such days is "not more than 8 weeks" and 57 is more.
  Licensed by "separated by a period of not more than 8 weeks": the period that separates them is the stretch with no incapacity in it.
- Reading B: the count runs from the last day of the earlier period to the first day of the later one, both ends included or one of them, which moves the boundary by one or two days.
  The text does not say how a "period" between two periods is counted.
- Rule: `s 152(3) the two periods of incapacity for work are treated as a single period` (ssc6-ssp); both sides of the boundary are tested (27 and 28 February 2026 after a period ending 1 January 2026).
  A week is any 7 days (s 163(1), src:3225); the number of weeks is the input `the number of weeks specified in subsection (3)`, which an order under s 152(4) may raise.

### F-specified: which rate is "the weekly rate of statutory sick pay for the time being specified in section 157(1)"

- Reading A, taken: the figure £123.25, the only amount s 157(1) names.
  The second limb, 80 per cent of earnings, is a proportion and not a rate "specified"; the phrase "if two or more such rates are for the time being so specified" fits an order under s 157(2) naming more than one amount.
- Reading B: the rate is whichever limb is lower for this employee, so the floor on the prescribed rate in ss 166(3) and 171ZN(2G) would differ person by person.
- Rule: `s 157(1) the weekly rate of statutory sick pay specified in section 157(1) in pounds` (ssc6-ssp) is the constant £123.25; ss 166(3) and 171ZN(2G) take it as a `GIVEN` named for s 157(1), so a different figure from an order under s 157(2) is one input.
  The floor tests are on both sides of 123.25 (123.24 fails, 123.25 and 150 pass).

### F-both: a woman entitled to both statutory maternity pay and maternity allowance

- Reading A, taken: the definition does not choose, so the answer is `NOTHING`; for a woman entitled to neither it is also `NOTHING`, because "disqualifying period" is defined only "in relation to" those two cases.
- Reading B: the later of the two periods, or the earlier, or the union.
- Rule: `s 153(12) the relevant date falls within the disqualifying period` (ssc6-ssp); this is the answer ssc9's Schedule 11 asks for (seam S32), and its `NOTHING` is not a "no".

### F-24: "after 24 weeks of pregnancy"

- Reading A, taken: more than 24 weeks, so 24 weeks exactly is not after 24 weeks; for a confinement the pregnancy is measured when labour began (the core's `Labour` field), and for a stillbirth when the child was stillborn.
  Licensed by "after" in both places.
- Reading B: 24 completed weeks or more, which would include 24.
  Reading C for a confinement: the pregnancy is measured when the child was issued.
- Rules: `s 171(1) she is confined` (ssc6-smp), which `s 153(12) she has been confined` repeats, and `s 171ZA(5) a child stillborn counts as a newborn child` (ssc6-spp).
  The core constant is `the weeks of pregnancy named in the stillbirth rule` = 24; both rules use `GREATER THAN` it.
  The core `Labour` has no field for "the labour resulted in the issue of a child, alive or dead": it is a plain input of the rule, and `NEEDS-CORE.md` asks for the field.
- For s 171ZA(5) the text says "includes", so a child stillborn at 24 weeks or fewer is `NOTHING` (list not closed), not a "no".

### F-e: paragraph (e) for a person with whom the child is NOT placed

- Reading A, taken: the condition is expressed only for "a person with whom the child is placed for adoption", so for the other person (the partner) it has nothing to bite on and is met.
- Reading B: it is a condition no partner can meet (so the partner never qualifies), or it is `NOTHING` for the partner.
- Rule: `s 171ZB(2)(e) where he is a person with whom the child is placed, he has elected to receive statutory paternity pay` (ssc6-spp), over the type `s 171ZB Adoption relationship`.
  The election bar in s 171ZB(4) is a separate rule.

### F-adopter: whose notification starts the relevant week in s 171ZB(3)

- Reading A, taken: the week in which the person with whom the child is placed is told of the match, whoever that is.
  Where the claimant is himself that person, "the adopter" is the claimant.
- Reading B: always the other person, the one by reference to whom the claimant satisfies s 171ZB(2)(a)(ii), as src:3413 literally says; then a claimant with whom the child is placed has no relevant week.
- Rule: `s 171ZB(2) the relevant week` (ssc6-spp) takes the day that person was notified as a field of the core's `Placement`.
  By contrast s 171ZL(3) (src:3568) names "the person" himself, and `s 171ZL(2) the relevant week` (ssc6-sap) takes his own notification day.

### F-purpose: the "purpose" bar in s 171ZE(4)

- Reading A, taken: pay is barred when the person has neither purpose at the beginning of the week (not to care for the child, and not to support the other person); "or" between the two limbs is read as "either of them suffices".
- Reading B: pay is barred when either purpose is missing (he must have both).
- Rule: `s 171ZE(4) statutory paternity pay is payable to him in respect of the statutory pay week` (ssc6-spp); a bar is a `JUST FALSE`, and the case where the bar does not apply is `NOTHING` (the text bars payment in one case and does not itself say it is payable otherwise).
  Tested: one purpose present, both present, neither present.

### F-credit: contractual pay and statutory pay each "go towards discharging" the other

- Reading A, taken: each amount paid reduces the other liability pound for pound and never below nothing; the two rules are computed separately, so the same payment can reduce both.
- Reading B: a payment discharges one liability or the other, not both.
- Rules: `s 171ZG(2)(a)` and `(b)` (ssc6-spp), and `s 171ZP(5)(a)` and `(b)` (ssc6-sap); the amount still owed is the liability less the amount paid, with a floor of 0 (tested).
  The text says "go towards discharging", not "discharge", so a part payment is a part discharge.

### Where the text does not choose and the rule answers `NOTHING`

These are not forks of reading; they are the explicit "not covered" cases (see "What the text does not answer", in the findings below).

## Jural relations (ssc6)

One row per provision that creates a relation.
The holder has the right (claim), privilege, power or immunity; the other party bears the correlative duty, no-right, liability or disability.
"Employer" means the person liable under the Part (the employer of the employee, or the Commissioners of Inland Revenue where regulations say so).
A relation that rests only on regulations (a power the Secretary of State may exercise) is listed once with the holder named as the Secretary of State; the Act does not encode its exercise, and its effect reaches the rules as a "prescribed" input.
The last row of each Part lists the provisions that create no relation.
The four payment duties (ss 151(1), 164(3), 171ZD(1), 171ZM(1)) are also run as regulative rules in `ssc6-duties.l4`: `s 151(1) the employer's duty to pay statutory sick pay for the day`, `s 164(3) the duty to pay statutory maternity pay for the week`, `s 171ZD(1) the duty to pay statutory paternity pay for the week` and `s 171ZM(1) the duty to pay statutory adoption pay for the week`.
The relation is stated once, in the row of its provision, and not again from the other side.

### Part XI -- Statutory Sick Pay

| provision | holder | correlative bearer | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 151(1) | employee | employer | claim / duty to pay for a day of incapacity for work | `s 151(1) the employer is liable to make a payment of statutory sick pay in respect of the day` |
| s 151(2) | employee or former employee | employer | immunity / disability (a term cannot exclude, limit or modify the Part, or make the employee contribute to the employer's costs) | `s 151(2) the agreement is void to the extent that it purports` |
| s 151(3) | employer | employee | privilege / no-right (deductions the employer could also make from contractual pay) | `s 151(3) the agreement is protected from being void by virtue of subsection (2)(a)` |
| s 151(5) | employer | employee | none (treats the employer as a different employer for each contract) | `s 151(5) the employer is treated as a different employer in relation to each contract of service` |
| s 151(6) | employee | Commissioners of Inland Revenue, in prescribed circumstances | claim / duty to pay in place of the employer | `s 151(6) who is liable to make payments of statutory sick pay` |
| s 153(1) to (11) | employee | employer | none on their own: they fix the first condition of the claim in s 151(1) (the period of entitlement) | `s 153(1)`, `s 153(2)`, `s 153(7)` |
| s 154 | employee | employer | none on their own: they fix the second condition of the claim in s 151(1) (qualifying days) | `s 154(1)`, `s 154(2)` |
| s 155(2) | employer | employee | immunity / disability (no entitlement above the limit of 28 times the weekly rate) | `s 155(2) the employee is entitled as against the employer to the aggregate amount` |
| s 156(2) | employer | employee | privilege / no-right (withhold payment for a qualifying day if not duly notified) | `s 156(2) the employer is entitled to withhold payment for the day` |
| s 156(3) | employee | employer | immunity / disability (withholding does not shorten the period of entitlement or count towards the limit) | `s 156(3)(a)`, `s 156(3)(b)` |
| s 157(1), (3) | employee | employer | claim / duty to pay at the lower of £123.25 and 80 per cent of normal weekly earnings, divided over the qualifying days | `s 157(1) the weekly rate of statutory sick pay in pounds`, `s 157(3) the amount of statutory sick pay payable in respect of the day in pounds` |
| s 160 | employee | employer or the payer of the benefit | none here: Schedule 12 (another part's range) says; the answer is an input | `s 160 Schedule 12 has effect with respect to the relationship between statutory sick pay and the benefit or payment` |
| s 161 | employee employed by or under the Crown | the Crown as employer | claim / duty on the same terms as other employees (members of Her Majesty's forces, as such, are outside) | `s 161 Part XI applies to the person employed by or under the Crown`, `s 161(3)` |
| s 162(1) | Secretary of State (with the Treasury) | persons on ships, vessels, hovercraft, aircraft, outside Great Britain, or on the continental shelf | power / liability (to have Part XI modified) | `s 162(1) regulations may modify Part XI in its application to the person` |
| none | -- | -- | none: ss 151(4), 152(2), (3), (5), (6), 153(12), 154(3), (4), 155(3), (4), 157(1)(a)-(b), 159A(3), 163(1) to (4) are definitions, counting rules or constants; ss 151(7), 152(4), 153(5), (6), (10), 155(5), 156(1), 157(2), 159A(1), (2), (4), 162(2), 163(5), (6), (7) are powers of the Secretary of State whose exercise is a "prescribed" input | the rules named in the coverage table |

### Part XII -- Statutory Maternity Pay

| provision | holder | correlative bearer | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 164(1), (3) | woman who is or has been an employee | the person liable (her employer) | claim / duty to pay when she meets the conditions and gives notice | `s 164(1) the woman is entitled to payments of statutory maternity pay`, `s 164(3) the liability to make payments of statutory maternity pay is the person's` |
| s 164(4), (5) | woman | person liable | power / liability (her notice brings the liability to pay into being; in writing if asked) | `s 164(4) the notice condition for payments of statutory maternity pay is met`, `s 164(5) the notice shall be in writing` |
| s 164(6) | woman or former employee | employer | immunity / disability (same as s 151(2)) | `s 164(6) the agreement is void to the extent that it purports` |
| s 164(7) | employer | woman | privilege / no-right (same as s 151(3)) | `s 164(7) the agreement is protected from being void by virtue of subsection (6)(a)` |
| s 165(1), (2), (3), (3A), (3B) | woman | employer | claim / duty to pay for each week of the maternity pay period (the period fixes when the duty runs) | `s 165(1) the maternity pay period`, `s 165(2)`, `s 165(3)`, `s 165(3A)`, `s 165(3B)` |
| s 165(4), (5), (6) | employer | woman | privilege / no-right (no payment for a week of work for the employer, or after confinement for another employer who is not liable) | `s 165(4)`, `s 165(5)`, `s 165(6)` |
| s 166 | woman | employer | claim / duty at the earnings-related rate (90 per cent) for 6 weeks, then the lower of that and the prescribed rate (not below the SSP rate) | `s 166(1)`, `s 166(2)`, `s 166(3)`, `s 166(4)` |
| s 167 | employer (payer) | Commissioners of Inland Revenue | claim / duty (recover the payments and a percentage, out of contributions payments) | `s 167(2)(a)`, `s 167(3)`, `s 167(6)`, `s 167(8)` |
| s 168 | woman | employer or the payer of the benefit | none here: Schedule 13 (another part's range) says; the answer is an input | `s 168 Schedule 13 has effect with respect to the relationship between statutory maternity pay and the benefit or payment` |
| s 169 | woman employed by or under the Crown | the Crown as employer | claim / duty on the same terms as other employees | `s 169 Part XII applies to the woman as it applies to women employed otherwise than by or under the Crown` |
| s 170(1) | Secretary of State (with the Treasury) | women in the classes named | power / liability (to have Part XII modified) | `s 170(1) regulations may modify Part XII in its application to her` |
| none | -- | -- | none: s 171(1), (4), (5), (6) (definitions, week and earnings rules; (1A) is the week rule inside (1)) and the powers ss 164(8)-(11), 165(3C), (3D), (7), 167(1), (2)(b), (4), (5), (7), 170(2), 171(2), (3), (7) | the rules named in the coverage table |

### Part 12ZA -- Statutory Paternity Pay

| provision | holder | correlative bearer | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 171ZA(1) to (5) | father (or the child's mother's partner) on a birth | employer | claim / duty (entitlement conditions, relevant week, more than one child, stillbirth) | `s 171ZA(1)`, `s 171ZA(2)`, `s 171ZA(2) the relevant week`, `s 171ZA(4)`, `s 171ZA(5)` |
| s 171ZB(1) to (11) | adopter's partner, or the person with whom the child is placed | employer | claim / duty (as above, on an adoption or a s 22C or s 81 placement); also a disability: no election if he has elected under s 171ZL, no second entitlement | `s 171ZB(1)`, `s 171ZB(2)`, `s 171ZB(4)`, `s 171ZB(8)`, `s 171ZB(9)`, `s 171ZB(11)` |
| s 171ZC(1), (2) | person claiming | person liable to pay | power / liability (his notice brings the liability into being; in writing if asked) | `s 171ZC(1) the notice condition for payments of statutory paternity pay is met`, `s 171ZC(2) the notice shall be in writing` |
| s 171ZD(1) | person entitled | any person of whom he has been an employee as in s 171ZA(2)(b) and (d) | claim / duty | `s 171ZD(1) the liability to make payments of statutory paternity pay is the person's` |
| s 171ZE(1), (2), (3), (10A) | person entitled | employer | claim / duty to pay the prescribed weekly rate for the weeks he chooses within the qualifying period; a day is a seventh of a week | `s 171ZE(1)`, `s 171ZE(2)`, `s 171ZE(3)`, `s 171ZE(10A)` |
| s 171ZE(3A), (4), (5), (7) | employer | person entitled | privilege / no-right (no payment, or no liability, in the weeks the text excludes: shared parental pay or leave, no caring or supporting purpose, work for the paying employer, work for an employer not liable) | `s 171ZE(3A)`, `s 171ZE(4)`, `s 171ZE(5)`, `s 171ZE(7)` |
| s 171ZF(1) | employee or former employee | employer | immunity / disability (a term cannot exclude or modify the Part, or make the employee contribute) | `s 171ZF(1) the agreement is void to the extent that it purports` |
| s 171ZF(2) | employer | employee | privilege / no-right (deductions the employer could also make from contractual pay) | `s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a)` |
| s 171ZG(1), (2) | employee | employer | immunity / disability (statutory pay does not affect contractual rights); each payment is credited towards the other liability | `s 171ZG(1)`, `s 171ZG(2)(a)`, `s 171ZG(2)(b)` |
| s 171ZH | employee employed by or under the Crown | the Crown as employer | claim / duty on the same terms | `s 171ZH Part 12ZA applies to the person as it applies to persons employed otherwise than by or under the Crown` |
| s 171ZI(1) | Secretary of State (with the Treasury) | persons in the classes named | power / liability | `s 171ZI(1) regulations may modify Part 12ZA in its application to the person` |
| none | -- | -- | none: s 171ZJ(1) to (3), (5) to (8) (definitions, week and earnings rules); the powers ss 171ZB(5), 171ZC(1A), (3), 171ZD(2), (3), 171ZE(8), 171ZG(3), 171ZI(2), 171ZJ(4), (9)-(12), 171ZK | the rules named in the coverage table |

### Part 12ZB -- Statutory Adoption Pay

| provision | holder | correlative bearer | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 171ZL(1), (2), (3) | person with whom a child is or is expected to be placed | employer | claim / duty (conditions (a)-(e), relevant week) | `s 171ZL(1)`, `s 171ZL(2)`, `s 171ZL(2) the relevant week` |
| s 171ZL(4), (4A), (4B) | person who would elect | -- | disability (he may not elect if he has elected to receive statutory paternity pay, or if he and the other member of a couple fall within (4A)) | `s 171ZL(4)`, `s 171ZL(4A)`, `s 171ZL(4B)` |
| s 171ZL(5) | person entitled | employer | immunity (not affected by more than one child) | `s 171ZL(5)` |
| s 171ZL(6), (7) | person claiming | person liable to pay | power / liability (notice at least 28 days before, or as soon as reasonably practicable; in writing if asked) | `s 171ZL(6)(a)`, `s 171ZL(6)(b)`, `s 171ZL(6)`, `s 171ZL(7)` |
| s 171ZL(9) to (12) | person with a s 22C or s 81 placement | employer | claim / duty on the modified terms; no second entitlement | `s 171ZL(9)`, `s 171ZL(10)`, `s 171ZL(12)` |
| s 171ZM(1) | person entitled | any person of whom he has been an employee as in s 171ZL(2)(b) | claim / duty | `s 171ZM(1)` |
| s 171ZN(2), (2A), (2E), (2F), (2G), (6A) | person entitled | employer | claim / duty to pay for the weeks of the adoption pay period at the earnings-related rate (90 per cent) for 6 weeks, then the lower of that and the prescribed rate (not below the SSP rate) | `s 171ZN(2)`, `s 171ZN(2A)`, `s 171ZN(2E)`, `s 171ZN(2F)`, `s 171ZN(2G)`, `s 171ZN(6A)` |
| s 171ZN(3), (4), (5), (9), (10) | employer | person entitled | privilege / no-right (no liability or payment for a week of work for the paying employer or another employer not liable) | `s 171ZN(3)`, `s 171ZN(5)`, `s 171ZN(9)` |
| s 171ZO(1), (2) | employee or former employee; employer | employer; employee | immunity / disability; privilege / no-right (as in s 151(2) and (3)) | `s 171ZO(1)`, `s 171ZO(2)` |
| s 171ZP(1) | person entitled | -- | immunity (a day in the adoption pay period is not a day of incapacity for work, except as prescribed) | `s 171ZP(1)` |
| s 171ZP(4), (5) | employee | employer | immunity / disability (statutory pay does not affect contractual rights); each payment is credited towards the other liability | `s 171ZP(4)`, `s 171ZP(5)(a)`, `s 171ZP(5)(b)` |
| s 171ZQ | employee employed by or under the Crown | the Crown as employer | claim / duty on the same terms | `s 171ZQ` |
| s 171ZR(1) | Secretary of State (with the Treasury) | persons in the classes named | power / liability | `s 171ZR(1)` |
| none | -- | -- | none: s 171ZS(1) to (3), (5) to (8) (definitions, week and earnings rules) and the powers ss 171ZL(8), 171ZM(2), (3), 171ZN(2B)-(2D), (6), 171ZP(2), (3), (6), 171ZR(2), 171ZS(4), (9)-(12), 171ZT | the rules named in the coverage table |

A duty that this Part puts on the Secretary of State (to make regulations on a former employer's liability: ss 153(10), 164(8), 171ZD(2), 171ZM(2)) is machinery; the correlative of an employee's claim against a former employer who dismissed to avoid liability is whatever those regulations say, and is not in the text.

## Marginal readings for a lawyer (ssc6)

The rule of 2026-10-29 leaves two readings for a lawyer to decide.
I took both as the status quo; neither is ruled.

- **(a)** A failed "if", "where" or "The conditions are" clause counts as the text's no, clause by clause, within the provision that holds the clause; and a flat negative ("shall not", "may not", "must not", "does not") or a stated minimum the text requires ("shall secure that it is ... at least") counts as the text saying no to its own case.
  The inference is that "if A then B" does not itself say "if not A then not B".
  **The other reading:** a failed "if", a flat negative or a stated minimum is not the text's own "no", so each branch below would answer `NOTHING` (not covered) instead of `JUST FALSE`.
- **(b)** A prohibition or grant limited by its own wording does not count as a no for a case outside the limit; the answer there is `NOTHING`.
  **The other reading:** outside the limit the text does say no, so each branch in table (b) would answer `JUST FALSE`.

To take the other reading, change `JUST FALSE` to `NOTHING` (for (a)), or `NOTHING` to `JUST FALSE` (for (b)), in the branch named, and change the assertions that test it; nothing else in a rule depends on the choice.
Branches that rest on the text's own words are not listed: 30 definitions that say "means" (the case is outside the definition) and 5 clauses that say "only if".

### (a) A failed "if", "where" or "The conditions are" clause answers `JUST FALSE`

| module | rule | the words |
| --- | --- | --- |
| ssp | `s 151(1) the employer is liable to make a payment of statutory sick pay in respect of the day` | "that employer shall, if the conditions set out in sections 153 and 154 below are satisfied, be liable" (marginal reading (a): a failed "if" counts as the text's no) |
| ssp | `s 151(3) the agreement is protected from being void by virtue of subsection (2)(a)` | "shall not be void by virtue of subsection (2)(a) above if the employer" (marginal reading (a): a failed "if" counts as the text's no) |
| ssp | `s 153(2)(d) the period of entitlement ends on the day before the disqualifying period` | "Subsection (2)(d) above does not apply in relation to an employee who has been pregnant if her pregnancy terminated, before the beginning of the disqualifying period,... |
| ssp | `s 153(1) the first condition is satisfied` | "The first condition is that the day in question falls within a period which is, as between the employee and his employer, a period of entitlement." |
| ssp | `s 156(2) the employer is entitled to withhold payment for the day` | "shall be entitled to withhold payment of that amount if" (marginal reading (a): a failed "if" counts as the text's no) |
| ssp | `s 163(1) the person is an employee` | "cases where any such person is not to be treated as an employee for the purposes of this Part of this Act" |
| smp | `s 164(2)(a) she has been in employed earner's employment with an employer for a continuous period of at least 26 week...` | "The conditions mentioned in subsection (1) above are—" |
| smp | `s 164(2)(b) her normal weekly earnings are not less than the lower earnings limit` | "The conditions mentioned in subsection (1) above are—" |
| smp | `s 164(2)(c) she has become pregnant and has reached, or been confined before reaching, the commencement of the 11th week` | "The conditions mentioned in subsection (1) above are—" |
| smp | `s 164(2) the conditions mentioned in subsection (1) are satisfied` | "The conditions mentioned in subsection (1) above are—" |
| smp | `s 164(1) the woman is entitled to payments of statutory maternity pay` | "Where a woman who is or has been an employee satisfies the conditions set out in this section" (marginal reading (a): a failed "where"/"if" counts as the text's no) |
| smp | `s 164(5) the notice shall be in writing` | "The notice shall be in writing if the person who is liable to pay the woman statutory maternity pay so requests." (marginal reading (a): a failed "if" counts as the t... |
| smp | `s 164(7) the agreement is protected from being void by virtue of subsection (6)(a)` | "shall not be void by virtue of subsection (6)(a) above if the employer" (marginal reading (a): a failed "if" counts as the text's no) |
| smp | `s 167(3) the payment qualifies for small employers' relief` | "qualifies for small employers' relief if" (marginal reading (a): a failed "if" counts as the text's no) |
| smp | `s 171(1) she is an employee` | "cases where any such woman is not to be treated as an employee for the purposes of this Part of this Act" |
| spp | `s 171ZA(2)(a) he satisfies prescribed conditions as to relationship with a newborn child and with the child's mother` | "The conditions are— (a) that he satisfies prescribed conditions" |
| spp | `s 171ZA(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 wee...` | "The conditions are—" |
| spp | `s 171ZA(2)(c) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week` | "The conditions are—" |
| spp | `s 171ZA(2)(d) he has been in employed earner's employment with that employer from the end of the relevant week to the...` | "The conditions are—" |
| spp | `s 171ZA(2) the conditions are satisfied` | "The conditions are—" |
| spp | `s 171ZB(2)(a) he satisfies prescribed conditions as to relationship with the child and with the person with whom the ...` | "The conditions are—" |
| spp | `s 171ZB(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 wee...` | "The conditions are—" |
| spp | `s 171ZB(2)(c) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week` | "The conditions are—" |
| spp | `s 171ZB(2)(d) he has been in employed earner's employment with that employer from the end of the relevant week to the...` | "The conditions are—" |
| spp | `s 171ZB(2)(e) where he is a person with whom the child is placed, he has elected to receive statutory paternity pay` | "The conditions are— ... (e) where he is a person with whom the child is placed for adoption, that he has elected to receive statutory paternity pay" |
| spp | `s 171ZB(2) the conditions are satisfied` | "The conditions are—" |
| spp | `s 171ZB(4) he may elect to receive statutory paternity pay` | "A person may not elect to receive ... statutory paternity pay if he has elected in accordance with section 171ZL below to receive statutory adoption pay." |
| spp | `s 171ZC(2) the notice shall be in writing` | "The notice shall be in writing if the person who is liable to pay the ... statutory paternity pay so requests." (marginal reading (a): a failed "if" counts as the tex... |
| spp | `s 171ZE(3A) statutory paternity pay is payable to him in respect of the statutory pay week` | "Statutory paternity pay is not payable to a person in respect of a statutory pay week if" |
| spp | `s 171ZE(4) statutory paternity pay is payable to him in respect of the statutory pay week` | "Statutory paternity pay shall not be payable to a person in respect of a statutory pay week if it is not his purpose at the beginning of the week— (a) to care for the... |
| spp | `s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a)` | "shall not be void by virtue of subsection (1)(a) above if the employer" (marginal reading (a): a failed "if" counts as the text's no) |
| spp | `s 171ZJ(2) the person is an employee` | "for cases where a person who falls within the definition in subsection (2) above is not to be treated as an employee for the purposes of this Part of this Act" |
| sap | `s 171ZL(2)(a) he is a person with whom a child is, or is expected to be, placed for adoption` | "The conditions are— (a) that he is a person with whom a child is, or is expected to be, placed for adoption under the law of any part of the United Kingdom" |
| sap | `s 171ZL(2)(b) he has been in employed earner's employment with an employer for a continuous period of at least 26 wee...` | "The conditions are—" |
| sap | `s 171ZL(2)(c) he has ceased to work for the employer` | "The conditions are—" |
| sap | `s 171ZL(2)(d) his normal weekly earnings are not less than the lower earnings limit at the end of the relevant week` | "The conditions are—" |
| sap | `s 171ZL(2)(e) he has elected to receive statutory adoption pay` | "The conditions are—" |
| sap | `s 171ZL(2) the conditions are satisfied` | "The conditions are—" |
| sap | `s 171ZL(1) he is entitled to statutory adoption pay` | "Where a person who is, or has been, an employee satisfies the conditions in subsection (2) below, he shall be entitled" (marginal reading (a): a failed "where" counts... |
| sap | `s 171ZL(4A) he falls within the subsection` | "A person falls within this subsection if—" (marginal reading (a): a failed "if" counts as the text's no) |
| sap | `s 171ZL(4) he may elect to receive statutory adoption pay` | "A person may not elect to receive statutory adoption pay if— (a) he has elected in accordance with section 171ZB above to receive statutory paternity pay" |
| sap | `s 171ZL(4) he may elect to receive statutory adoption pay` | "A person may not elect to receive statutory adoption pay if— ... (b) he falls within subsection (4A)" |
| sap | `s 171ZL(7) the notice shall be in writing` | "The notice shall be in writing if the person who is liable to pay the statutory adoption pay so requests." (marginal reading (a): a failed "if" counts as the text's no) |
| sap | `s 171ZO(2) the agreement is protected from being void by virtue of subsection (1)(a)` | "shall not be void by virtue of subsection (1)(a) above if the employer" (marginal reading (a): a failed "if" counts as the text's no) |
| sap | `s 171ZS(2) the person is an employee` | "for cases where a person who falls within the definition in subsection (2) above is not to be treated as an employee for the purposes of this Part of this Act" |

### (a) A flat negative, or a stated minimum the text requires, answers `JUST FALSE` for its own case

| module | rule | the words |
| --- | --- | --- |
| ssp | `s 153(1) the first condition is satisfied` | "Schedule 11 to this Act has effect for the purpose of specifying circumstances in which a period of entitlement does not arise" |
| ssp | `s 155(2) the employee is entitled as against the employer to the aggregate amount` | "An employee shall not be entitled, as against any one employer, to an aggregate amount of statutory sick pay in respect of any one period of entitlement which exceeds... |
| ssp | `s 156(3)(a) the period of entitlement is affected by the withholding` | "the period of entitlement in question shall not be affected" |
| ssp | `s 161 Part XI applies to the person employed by or under the Crown` | "the provisions of this Part of this Act do not apply in relation to persons serving as members of Her Majesty's forces, in their capacity as such" |
| smp | `s 165(3) the prescribed first day is permitted` | "but not later than the day immediately following the day on which she is confined" |
| smp | `s 165(4) statutory maternity pay is payable by the person for the week` | "statutory maternity pay shall not be payable to a woman by a person in respect of any week during any part of which she works under a contract of service with him" |
| smp | `s 165(6) statutory maternity pay is payable for the week after confinement` | "statutory maternity pay shall not be payable to a woman in respect of any week after she has been confined and during any part of which she works for any employer who... |
| smp | `s 166(3) the weekly rate prescribed is not less than the weekly rate of statutory sick pay` | "must not be less than the weekly rate of statutory sick pay" |
| spp | `s 171ZA(4) the entitlement is affected by the birth, or expected birth, of more than one child` | "shall not be affected by the birth, or expected birth, of more than one child as a result of the same pregnancy" |
| spp | `s 171ZB(6) the entitlement is affected by the placement for adoption of more than one child` | "shall not be affected by the placement for adoption of more than one child as part of the same arrangement" |
| spp | `s 171ZB(9) he may become entitled in connection with the placement of the child for adoption` | "the person may not become entitled to payments of statutory paternity pay in connection with the placement of the child for adoption" |
| spp | `s 171ZB(11) he may become entitled in connection with the placement of the child for adoption` | "the person may not become entitled to payments of statutory paternity pay in connection with the placement of the child for adoption" |
| spp | `s 171ZE(3) the qualifying period determined by regulations is long enough` | "shall secure that it is a period of at least 56 days" (marginal reading (a): a stated minimum the text requires counts as the text's no, as in s 154(3) and s 166(3)) |
| spp | `s 171ZE(5) the person is liable to pay statutory paternity pay to the other in respect of the statutory pay week` | "A person shall not be liable to pay ... statutory paternity pay to another in respect of a statutory pay week during any part of which the other works under a contrac... |
| spp | `s 171ZE(7) statutory paternity pay is payable to him in respect of the statutory pay week` | "statutory paternity pay shall not be payable to a person in respect of a statutory pay week during any part of which he works for any employer who is not liable to pa... |
| spp | `s 171ZG(1) the entitlement to statutory paternity pay affects his right to contractual remuneration` | "any entitlement to statutory paternity pay shall not affect any right of a person in relation to remuneration under any contract of service" (subject to subsections (... |
| sap | `s 171ZL(5) the entitlement is affected by the placement, or expected placement, of more than one child` | "A person's entitlement to statutory adoption pay shall not be affected by the placement, or expected placement, for adoption of more than one child as part of the sam... |
| sap | `s 171ZL(10) he may become entitled as a result of the child being placed for adoption` | "the person may not become entitled to payments of statutory adoption pay as a result of the child being, or being expected to be, placed for adoption" |
| sap | `s 171ZL(12) he may become entitled as a result of the child being placed for adoption` | "the person may not become entitled to payments of statutory adoption pay as a result of the child being, or being expected to be, placed for adoption" |
| sap | `s 171ZN(2G) the weekly rate prescribed is not less than the weekly rate of statutory sick pay` | "must not be less than the weekly rate of statutory sick pay" |
| sap | `s 171ZN(3) the person is liable to pay statutory adoption pay to the other in respect of the week` | "a person shall not be liable to pay statutory adoption pay to another in respect of any week during any part of which the other works under a contract of service with... |
| sap | `s 171ZN(5) statutory adoption pay is payable to him in respect of the week` | "statutory adoption pay shall not be payable to a person in respect of any week during any part of which he works for any employer who is not liable to pay him statuto... |
| sap | `s 171ZP(1) the day is treated as a day of incapacity for work` | "a day which falls within the adoption pay period shall not be treated as a day of incapacity for work" |
| sap | `s 171ZP(4) the entitlement to statutory adoption pay affects his right to contractual remuneration` | "any entitlement to statutory adoption pay shall not affect any right of a person in relation to remuneration under any contract of service" (subject to subsections (5... |

### (a) A class fixed by "shall be", "shall be taken to consist of" or "being" (not worded "means") answers `JUST FALSE` for a case outside it

| module | rule | the words |
| --- | --- | --- |
| ssp | `s 154(2) the day is a qualifying day` | "shall be such day or days as may, subject to regulations, be agreed between the employee and his employer" |
| ssp | `s 154(3) the agreement provides at least one qualifying day in the week` | "there shall, in each week (beginning with Sunday), be at least one qualifying day" (marginal reading: a "shall" requirement is taken as the text's no) |
| ssp | `s 161(3) the establishment or organisation is part of Her Majesty's forces` | "shall be taken to consist of such establishments and organisations as may be prescribed" |
| ssp | `s 161(3) the establishment or organisation is part of Her Majesty's forces` | "being establishments and organisations in which persons serve under the control of the Defence Council" |

### (b) A grant or prohibition limited by its own wording answers `NOTHING` outside the limit

| module | rule | the limit |
| --- | --- | --- |
| ssp | `s 151(2) the agreement is void to the extent that it purports` | "to the extent that it purports" |
| ssp | `s 151(3) the agreement is protected from being void by virtue of subsection (2)(a)` | the subsection speaks only of "any agreement ... authorising any deductions" |
| ssp | `s 152(3) the two periods of incapacity for work are treated as a single period` | "separated by a period of not more than 8 weeks" |
| ssp | `s 152(6) the day may be a day of incapacity for work notwithstanding` | "may be a day of incapacity ... notwithstanding that" names two cases only to say they do not prevent it |
| ssp | `s 153(2)(d) the period of entitlement ends on the day before the disqualifying period` | "in the case of an employee who is, or has been, pregnant" |
| ssp | `s 153(4) the period is also a period of entitlement as between the employee and another employer` | "may also be" names a possibility for another employer of his |
| ssp | `s 153(12) the relevant date falls within the disqualifying period` | "disqualifying period" is defined only "in relation to a woman entitled to statutory maternity pay" or "to maternity allowance" |
| ssp | `s 154(4) the day is also a qualifying day as between the employee and another employer` | "may also be" names a possibility for another employer of his |
| ssp | `s 156(2) the employer is entitled to withhold payment for the day` | "An employer who would, apart from this section, be liable to pay" |
| ssp | `s 162(1) regulations may modify Part XI in its application to the person` | the power reaches persons "employed on board any ship, vessel, hovercraft or aircraft", "outside Great Britain" or in "prescribed employment in connection with contine... |
| smp | `s 164(6) the agreement is void to the extent that it purports` | "to the extent that it purports" |
| smp | `s 164(7) the agreement is protected from being void by virtue of subsection (6)(a)` | the subsection speaks only of "any agreement ... authorising any deductions" |
| smp | `s 165(3) the prescribed first day is permitted` | "a prescribed day after the beginning of the 11th week" |
| smp | `s 165(1) the maternity pay period` | "of a duration not exceeding 52 weeks" |
| smp | `s 165(3A) the maternity pay period as reduced` | "to be reduced" |
| smp | `s 165(3A) the woman would be entitled to statutory maternity pay for the week but for the reduction in the maternity ...` | "in respect of each week during a prescribed period"; a week inside the reduced period, or outside the unreduced one, is not a week lost to the reduction |
| smp | `s 165(8) the first day of the week of the maternity pay period containing the day` | the weeks are counted from the day the maternity pay period begins |
| smp | `s 166(1) the weekly rate of statutory maternity pay for the week in pounds` | the rate is for weeks of "the maternity pay period", which does not exceed 52 weeks |
| smp | `s 167(6) the amount deducted is treated as paid towards discharging the employer's liability` | the treatment is of "the amount so deducted" |
| smp | `s 170(1) regulations may modify Part XII in its application to her` | the power reaches persons "employed on board any ship, vessel, hovercraft or aircraft", "outside Great Britain" or in "prescribed employment in connection with contine... |
| spp | `s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied` | subsection (8) applies "in a case involving a child placed under section 22C ... with a local authority foster parent who has been approved as a prospective adopter" |
| spp | `s 171ZB(8) the placement is one to which the conditions of subsection (2) are applied` | subsection (10) applies "in a case involving a child placed under section 81 ... with a local authority foster parent who has been approved as a prospective adopter" |
| spp | `s 171ZE(2) the person may choose the weeks in respect of which statutory paternity pay is payable` | "a period of two consecutive weeks within the qualifying period" |
| spp | `s 171ZF(1) the agreement is void to the extent that it purports` | "to the extent that it purports" |
| spp | `s 171ZF(2) the agreement is protected from being void by virtue of subsection (1)(a)` | the subsection speaks only of "any agreement ... authorising any deductions" |
| spp | `s 171ZI(1) regulations may modify Part 12ZA in its application to the person` | the power reaches persons "employed on board any ship, vessel, hovercraft or aircraft", "outside Great Britain" or in "prescribed employment in connection with contine... |
| sap | `s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied` | subsection (9) applies "in a case involving a child who is, or is expected to be, placed under section 22C ... with a local authority foster parent who has been approv... |
| sap | `s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied` | subsection (11) applies "in a case involving a child who is, or is expected to be, placed under section 81 ... with a local authority foster parent who has been approv... |
| sap | `s 171ZN(2) the adoption pay period` | "of a duration not exceeding 52 weeks" |
| sap | `s 171ZN(2A) the adoption pay period as reduced` | "to be reduced" |
| sap | `s 171ZN(2E) the weekly rate of statutory adoption pay for the week in pounds` | the rate is for weeks of "the adoption pay period", which does not exceed 52 weeks |
| sap | `s 171ZN(8) the first day of the week of the adoption pay period containing the day` | the weeks are counted from the day the adoption pay period begins |
| sap | `s 171ZO(1) the agreement is void to the extent that it purports` | "to the extent that it purports" |
| sap | `s 171ZO(2) the agreement is protected from being void by virtue of subsection (1)(a)` | the subsection speaks only of "any agreement ... authorising any deductions" |
| sap | `s 171ZR(1) regulations may modify Part 12ZB in its application to the person` | the power reaches persons "employed on board any ship, vessel, hovercraft or aircraft", "outside Great Britain" or in "prescribed employment in connection with contine... |

Counts of `FALSE-kind` comments by the kind of text that licenses them: flat negative 24, if / where / conditions are 45, means 30, only if 5, other 4; total 108 (one comment per branch; a rule with several branches has several).
Branches that answer `NOTHING` because the text limits its own wording: 35.

### Reading a result: FALSE and NOTHING (ssc6)

Every rule in these four Parts answers a question about one person's claim to statutory sick, maternity, paternity or adoption pay, or about a rule that limits or measures it.
The answer is a `MAYBE BOOLEAN`, a `MAYBE NUMBER`, a `MAYBE Period` or a `MAYBE DATE`.

- **`JUST TRUE`** means the text says yes to the case in its own words (a definition that says "means", a condition that is met, a grant).
- **`JUST FALSE`** is a "no" and means only that the text itself says no to this case.
  In these Parts that is one of: a condition the text introduces with "if", "where", "only if" or "The conditions are" and that is not met (the person is not entitled; the notice was not given; the employer may not withhold); a flat negative ("shall not be payable", "may not elect", "shall not be void", "must not be less than") whose case is present; or a definition that says "means" and the case is outside it.
  Every `JUST FALSE` carries a comment that quotes the words.
- **`NOTHING`** is "not covered", and is never a "no".
  In these Parts the reasons are:
  1. the text names a prescribed matter and regulations decide it ("points outside the text": a prescribed week, rate, period, or class of case; the lower earnings limit; the weekly rate of pay; the number of weeks of a reduced pay period; Schedules 11 to 13; sections 6, 35(2), 120(2), 172(a) and 173(a), which other parts of the Act answer);
  2. the text bars or grants in one case and is silent on the others ("silent": a bar on payment for a week of work does not itself say the other weeks are payable, so the answer for the other weeks is `NOTHING`, not "payable");
  3. the text limits its own grant or prohibition and the case is outside the limit ("limited by its own wording": a modification that applies only to a child placed by a local authority with an approved foster parent; "to the extent that it purports"; a rate that applies only to a stated week);
  4. the text says "includes" ("includes": "modifications" includes additions, omissions and amendments; "newborn child" includes a child stillborn after 24 weeks);
  5. the term is defined by regulations ("undefined term": "earnings" and "relevant period" in the normal-weekly-earnings rule; the expected week of confinement).
- **A caller must never turn `NOTHING` into `FALSE`.**
  A `NOTHING` from `s 164(1) the woman is entitled to payments of statutory maternity pay` means the encoding could not decide on the facts and inputs given, not that she is not entitled.
  The three-valued `AND` that joins the conditions (the helper `... all of these answers hold` in each module) gives `JUST FALSE` if any condition is `JUST FALSE` even when another is `NOTHING`, because one failed condition is enough; it gives `NOTHING` when no condition is `JUST FALSE` and at least one is `NOTHING`.
- **In the seat** (`ssc6-seat.l4`, 42 questions) each question returns the answer of one module rule (the seat's only `IF`s turn the person's answers into the rule's inputs, for example a date given only if the event has happened, and add no condition of the Act), so `JUST FALSE` is the text's own no and `NOTHING` means the Act alone does not decide this person's case.
  Where the Act says "except as may be prescribed" or leaves a figure to regulations, the seat asks the person, for example "Do regulations prescribe another period, in place of a week beginning with Sunday, for your case?"; the answer the Act alone gives is "no", and "yes" returns `NOTHING`.
  A fact that another part of the Act or another Act decides (section 6, section 172(a), section 173(a), Schedules 11 to 13, the Children Act 1989) is asked as a plain yes or no and passed on as `JUST` that answer, so such an input never produces `NOTHING` by itself.

## Seams (ssc6)

A seam input is a `GIVEN` parameter named for the answering section, as `PLAN.md` section 4 says; at the merge the lead replaces it by a call to the answering function.
Where `PLAN.md` and the brief differ, the brief governs, and the difference is stated in the row.
"Asked by" lists the function that takes the input; "answered by" lists the function in this range that another part asks for.

### Seams `PLAN.md` names for ssc6

| id | direction | name as taken or given | type | function | note |
| --- | --- | --- | --- | --- | --- |
| S24 | asks | `s 35(2) the maternity allowance period` | `Period` | asked by `s 153(12) the maternity allowance period` and `s 153(12) the relevant date falls within the disqualifying period` (ssc6-ssp) | answered by ssc2 |
| S25 | asks | `s 120(2) the employment is in connection with continental shelf operations` | `BOOLEAN` | asked by `s 162(1)`, `s 170(1)`, `s 171ZI(1)` and `s 171ZR(1)` (the four "regulations may modify" rules) | `PLAN.md` names s 162 only; the other three sections carry the same power and take the same input |
| S26 | asks | `s 5(1)(a) the lower earnings limit in force at the time in pounds` | `NUMBER` | asked by `s 164(2)(b)`, `s 171ZA(2)(c)`, `s 171ZB(2)(c)` and `s 171ZL(2)(d)` | `PLAN.md` names ss 164 and 171ZA only; ss 171ZB and 171ZL also test the limit. I took the plain number and not the core's `Earnings limits`, which is per tax year, because the moment is named in each section and need not fall in the tax year of the claim (see finding 4) |
| S6 | answers | `s 165(1) the maternity pay period if she were entitled to statutory maternity pay`; `s 165(3A) the woman would be entitled to statutory maternity pay for the week but for the reduction in the maternity pay period` | `MAYBE Period`; `MAYBE BOOLEAN` | ssc6-smp | `PLAN.md` gives `Period` for the first; the brief's three-valued rule governs (the prescribed duration may be unknown) |
| S7 | answers | `s 166(1)(b) the weekly rate prescribed in pounds` | `NUMBER` | the same name is a `GIVEN` of `s 166(1) the weekly rate of statutory maternity pay for the week in pounds` and `s 166(3) the weekly rate prescribed is not less than the weekly rate of statutory sick pay` (ssc6-smp) | regulations prescribe it, so it is an input in every case, as `PLAN.md` says |
| S27 | answers | `s 165(3A) the number of weeks to which the maternity pay period is reduced` | `NUMBER` | `GIVEN` of `s 165(3A) the maternity pay period as reduced`; the week convention is `s 165(8) the first day of the week of the maternity pay period containing the day` (ssc6-smp) | the input and ssc7's input are one fact under one name |
| S28 | answers | `s 171ZN(2A) the number of weeks to which the adoption pay period has been reduced` | `NUMBER` | `GIVEN` of `s 171ZN(2A) the adoption pay period as reduced`; `s 171ZN(8) the first day of the week of the adoption pay period containing the day` (ssc6-sap) | the second answers `MAYBE DATE` |
| S29 | answers | `s 171ZN(2) the adoption pay period`; `s 165(1) the maternity pay period` | `MAYBE Period` each (`PLAN.md` says `Period`) | ssc6-sap, ssc6-smp | each takes the first day of the period and the duration in weeks as inputs: a duration above the statutory 52 weeks, or a period that regulations prescribe differently, answers `NOTHING` |
| S30 | answers | `s 164 the relevant week`; `s 171ZA(2) the relevant week`; `s 171ZB(2) the relevant week`; `s 171ZL(2) the relevant week` | `MAYBE Period` each (`PLAN.md` says `Period`) | ssc6-smp, ssc6-spp (two), ssc6-sap | `s 164 the relevant week` is not a defined term of s 164 (src:3245 describes the week in words); it is added because S30 asks for it by that name. The three others take the placement or the day in the expected week, and the input `regulations prescribe another period in place of a week beginning with Sunday for the case` |
| S32 | answers | `s 153(12) the relevant date falls within the disqualifying period`; `s 171(1) the pregnancy terminated otherwise than by confinement` | `MAYBE BOOLEAN` each (`PLAN.md` says `BOOLEAN`) | ssc6-ssp, ssc6-smp | the first also answers `NOTHING` for a woman entitled to both, or to neither, of statutory maternity pay and maternity allowance (fork F-both) |
| K1 | asks | `s 172(a) a reference to Great Britain includes the place` | `MAYBE BOOLEAN` | asked by the four employee definitions: `s 163(1)`, `s 171(1)`, `s 171ZJ(2)`, `s 171ZS(2)` | the keel's section 3 |
| K2 | asks | `s 173(a) the person is under 16` | `MAYBE BOOLEAN` | asked by the four employer definitions | the keel's section 3 |

### Seams I found that `PLAN.md` lacks

Each follows the same pattern: the name carries the label of the answering section.

| asking function | input | type | answered by |
| --- | --- | --- | --- |
| the four employer definitions: `s 163(1)`, `s 171(1)`, `s 171ZJ(1)`, `s 171ZS(1)` (the person is the employer in relation to the employee) | `s 6 the person is liable to pay secondary Class 1 contributions in relation to any earnings of the employee ...` (the wording follows each Part: "of the employee", "of her earnings", "of the earnings of the person") | `MAYBE BOOLEAN` | ssc1 s 6 |
| `s 153(1) the first condition is satisfied` | `sch 11 a circumstance specified in Schedule 11 prevents a period of entitlement arising in relation to the person` | `MAYBE BOOLEAN` | Schedule 11 (ssc9) |
| `s 160 Schedule 12 has effect with respect to the relationship between statutory sick pay and the benefit or payment` | `sch 12 the relationship between statutory sick pay and the benefit or payment is as Schedule 12 provides` | `MAYBE BOOLEAN` | Schedule 12 (ssc9) |
| `s 168 Schedule 13 has effect with respect to the relationship between statutory maternity pay and the benefit or payment` | `sch 13 the relationship between statutory maternity pay and the benefit or payment is as Schedule 13 provides` | `MAYBE BOOLEAN` | Schedule 13 (ssc9) |
| `s 166(3)` and `s 171ZN(2G)` (the floor on the prescribed rate) | `s 157(1) the weekly rate of statutory sick pay specified in section 157(1) in pounds` | `NUMBER` | `s 157(1) the weekly rate of statutory sick pay specified in section 157(1) in pounds` (ssc6-ssp, the constant 123.25; fork F-specified); a `GIVEN`, not an `IMPORT`, so that SMP and SAP need not import SSP, which imports SMP |
| `s 164(1) the woman is entitled to payments of statutory maternity pay` | `s 171(1) she is an employee` | `MAYBE BOOLEAN` | `s 171(1) she is an employee` (ssc6-smp), passed in by the caller |
| `s 171ZL(1) he is entitled to statutory adoption pay` | `s 171ZS(2) the person is, or has been, an employee` | `MAYBE BOOLEAN` | `s 171ZS(2) the person is an employee` (ssc6-sap), passed in by the caller |
| `s 153(12) the relevant date falls within the disqualifying period` | `s 165(1) the maternity pay period` | `Period` | `s 165(1) the maternity pay period` (ssc6-smp), passed in by the caller |

Facts that another Act decides are asked as plain `MAYBE BOOLEAN` inputs, with names that cite the Act and the section: section 105(1) of the Children Act 1989 (ssc6-spp and ssc6-sap, once for a local authority and once for a local authority foster parent), section 144(4) of the Adoption and Children Act 2002 and section 29(3) of the Adoption and Children (Scotland) Act 2007 (ssc6-sap, `s 171ZL(4B)`), and Part X of the Employment Rights Act 1996 (ssc6-smp, whether she was dismissed within its meaning).
`PLAN.md` section 5 says references to other Acts need no seam input; the rules here still need the fact the other Act decides, so each takes it as an input named for the Act and section.

### Where `PLAN.md` and the brief differ

- Types: S29, S30 and S32 are `MAYBE` in this range (the brief's rule that `NOTHING` flows through and is never turned into `FALSE`); `PLAN.md` gives plain `Period` and `BOOLEAN`.
  The lead can wrap a plain value in `JUST` at the merge.
- Extra inputs: the functions that answer S29, S30 and S32 take further plain inputs (the first day of a period, its duration, whether regulations prescribe another period, which of the two benefits she is entitled to), because the Act leaves them to regulations or to the person; `PLAN.md` names only the output.
- S26 is also taken in ss 171ZB(2)(c) and 171ZL(2)(d), which `PLAN.md` omits.
- S25 is also taken in ss 170(1), 171ZI(1) and 171ZR(1), which `PLAN.md` omits.

## What the text turns out to say (ssc6)

Numbered findings, each checked against the lines cited.
`src:N` is a line of `ukpga-1992-4.txt`, a plain-text rendering made by a converter script; it is not the official text, and nothing here is verified against the official text.

1. **Dots stand for words this text does not contain.**
   A line of nothing but dots, and a run of dots inside a sentence (for example `but has ceased to work for him ... ;` at src:3245, and `payments of ... statutory paternity pay` at src:3444), mark words the converter shows as omitted or repealed.
   I cannot tell from this text which, so the 23 units that are only dots are `repealed or blank in this text` in the coverage table, and nothing is encoded for words inside a dotted run.
   Where a dotted run sits inside a sentence that is encoded, the encoding reads the sentence as it stands.

2. **A reference in section 171ZL(11)(b) breaks its own pattern.**
   Src:3607 reads "placed with him under section 8", while src:3605, 3606, 3608, 3609 and 3610 of the same subsection read "section 81", and src:3601 (subsection (9)(b)) reads "section 22C".
   The rule `s 171ZL(9) the placement is one to which the conditions of subsection (2) are applied` keys on the kind of placement and not on the number, so the slip changes nothing in the answers.
   I have not corrected the text; this is a note for whoever checks the official text.

3. **The four Parts do not open the same way.**
   Section 164(1) (src:3243) and section 171ZL(1) (src:3561) give the entitlement to a woman or person "who is or has been an employee".
   Sections 171ZA(1) (src:3388) and 171ZB(1) (src:3400) say only "Where a person satisfies the conditions in subsection (2) below"; employment enters those two through the conditions in subsection (2) (src:3393, 3395, 3405, 3407).
   So the entitlement rules for paternity pay take no separate "is an employee" input, while those for maternity and adoption pay do (`s 171(1) she is an employee`, `s 171ZS(2) the person is, or has been, an employee`).

4. **The lower earnings limit is read at a different moment in each Part.**
   Section 164(2)(b) (src:3246) reads it "immediately before the commencement of the 14th week before the expected week of confinement".
   Sections 171ZA(2)(c) (src:3394), 171ZB(2)(c) (src:3406) and 171ZL(2)(d) (src:3566) read it "at the end of the relevant week".
   The seam input `s 5(1)(a) the lower earnings limit in force at the time in pounds` is therefore the figure at the moment each section names, and the caller must supply the right one; a single tax-year figure may be wrong when the two moments straddle a tax year.

5. **"The adopter" in section 171ZB is not always the claimant.**
   Section 171ZB(3) (src:3409) starts the relevant week from the week "in which the adopter is notified of being matched with the child", and subsection (7) (src:3413) defines "adopter" as the person "by reference to whom he satisfies" the condition in subsection (2)(a)(ii), who is the other person and not the claimant.
   Section 171ZL(3) (src:3568) names the claimant himself: "the week in which the person is notified that he has been matched".
   The two Parts therefore start the week differently for a claimant with whom the child is placed (fork F-adopter).

6. **"Week" has three meanings across these Parts, and each rule uses one.**
   Any period of 7 days: src:3225 (section 163), src:3473 (section 171ZE), src:3638 (section 171ZN(7)).
   Seven days beginning with the day the pay period begins: src:3300 (section 165(8)), src:3639 (section 171ZN(8)), src:3658 (section 171ZP(7)).
   Seven days beginning with Sunday, or another prescribed period: src:3369 (section 171(1A)), src:3539 (section 171ZJ(5)), src:3693 (section 171ZS(5)).
   Each rule names its convention in a constant, for example `s 165(8) the week convention of subsections (1), (4) and (6)`, and the core's `Week convention` gives the type.

7. **The Act states some figures in its own words, and the modules hold them as constants.**
   Statutory sick pay: the weekly rate is the lower of £123.25 and 80 per cent of normal weekly earnings (src:3166-3168), and the entitlement limit is 28 times the weekly rate (src:3154).
   Two periods of incapacity are linked if separated by not more than 8 weeks (src:3113).
   Employment for a continuous period of at least 26 weeks (src:3245, 3393, 3405, 3564), notice at least 28 days before the date (src:3251, 3583), and pay periods of a duration not exceeding 52 weeks (src:3279, 3617).
   The earnings-related rate for the first 6 weeks (src:3303, 3629) is 90 per cent of normal weekly earnings for the 8 weeks named (src:3306, 3631), and the recovery of 92 per cent of payments that do not qualify for small employers' relief (src:3314).
   An order or regulations that substituted another figure would change these answers; the figures that regulations set (the lower earnings limit, the prescribed weekly rate, the length of a pay period) are inputs.

8. **The text says who is liable to pay, and does not say by when.**
   Section 151(1) (src:3098) puts the liability on "that employer"; section 164(3) (src:3248), section 171ZD(1) (src:3444) and section 171ZM(1) (src:3612) say the liability "is a liability of any person of whom" the claimant has been an employee.
   A search of lines 3095-3717 for "within", "falls due", "not later than" and "as soon as" finds no sentence that gives a date or a period for paying any of the four; the matches are about notices, elections, the first day of a pay period, and "falls within" in the sense of lying inside a period.
   A search of the same lines for "offence", "penalt", "breach", "default" and "enforce" finds nothing, and "recover" finds only recovery of payments by employers and the Commissioners (src:3178-3181, 3312-3328), so no sentence gives a consequence of failing to pay.
   So the four regulative rules in `ssc6-duties.l4` are `PARTY ... MUST ...` with no `WITHIN` and no `LEST`; a trace in which no payment is made stays unbreached, which is what the text says (it states no deadline), not an omission.

9. **Some duties name no party, so none was invented.**
   "Regulations shall prescribe the manner in which, and the time within which, notice ... is to be given" (src:3157) and "Regulations shall make provision for the payment by employers of statutory maternity pay to be funded by the Commissioners of Inland Revenue" (src:3310) impose a duty on no named person.
   They are machinery (inert, reason 2): their exercise reaches the rules as a prescribed input, and the regulative layer holds no duty for them.

10. **"Includes", "undefined term" and "points outside the text" are not three names for one thing.**
    Of the 157 `NOTHING-kind` comments in the four modules: 57 are "points outside the text" (a prescribed rate, week, period or class of case, the lower earnings limit, Schedules 11 to 13, section 6, section 120(2), sections 172(a) and 173(a), another Act's definition), 55 "silent", 35 "limited by its own wording", 5 "includes", 5 "undefined term", and none "list not closed".
    The five "includes" are "newborn child" (src:3398), "modifications" in three Parts, and "contract of service" in section 163(1).
    The five "undefined term" are "relevant period" in the normal-weekly-earnings rule of each of the four modules, and the expected week of confinement.

### What the text does not answer

These are the explicit "not covered" cases; none is a "no".

- **When any of the four payments falls due**, or by what date it must be made (finding 8).
- **A woman entitled to both statutory maternity pay and maternity allowance, or to neither,** in section 153(12): "disqualifying period" is defined only "in relation to" each of the two cases (fork F-both).
- **A child stillborn at 24 weeks or fewer** in section 171ZA(5): the text says "includes", so the list is not closed (fork F-24).
- **Which test of "member of a couple" applies to adoption under any other law** in section 171ZL(4B): the subsection names England and Wales or Northern Ireland, and Scotland, and its middle paragraph is blank in this text (src:3578), so the rule answers `NOTHING` for another place.
- **What a reduction of the maternity pay period to no weeks means** in section 165(3A) (src:3282): the subsection does not say, and `s 165(3A) the maternity pay period as reduced` answers `NOTHING` (silent) for a reduction to 0 weeks or fewer.
- **Whether a payment of statutory pay and a payment of contractual pay discharge each other once or twice** in sections 171ZG(2) and 171ZP(5): the text says "go towards discharging" each way (fork F-credit).
- **Any case that regulations decide:** a prescribed week, rate, period, class of case, or exception, and the figures in finding 7 that regulations set; the rule answers `NOTHING` (points outside the text), and the seat asks the person whether regulations prescribe otherwise in their case.

## What the stable binary does not accept (ssc6)

The stable binary is l4 1.6.98 (main, 7689b0d, 2026-10-19).
Where a skill describes something it rejects, the binary governs.
Each item says whether I tested it in this run or took it from the brief or a skill reference.

**Loud: the binary says so and the run is red.**

- `WAIT UNTIL` with a space in a trace is an error on both the stable binary and main 1.6.108; the spelling that works is `WAITUNTIL`.
  Tested here: a copy of `ssc6-duties.l4` with `(WAIT UNTIL 400)` gave a `DiagnosticSeverity_Error` on both.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (except `LEST BREACH ... BECAUSE`) do not exist on the stable binary.
  Taken from the brief, not re-tested; I wrote none, and a case outside the encoding returns `NOTHING` or a named "... not covered" constructor, asserted.
- A section-level `GIVEN` (one that stands under a `§` heading and is meant for every rule below it) is rejected: it belongs to the next rule only.
  Taken from `dialects.md` of the writing skill, not re-tested; each rule here carries its own `GIVEN`.

**Silent: the binary accepts it and gives a result that can mislead.**

- **The amount named in a `MUST` action is not compared with the payload of the event.**
  Tested here on both binaries: the duty `s 151(1) the employer's duty to pay statutory sick pay for the day` for 24.65, met by a payment event of 1 pound, gives `FULFILLED`.
  The four rules in `ssc6-duties.l4` therefore say what the section says (the amount is in the action) but cannot show an underpayment as a breach.
  The amount is computed and asserted in the decision functions (`s 157(3) the amount of statutory sick pay payable in respect of the day in pounds`, `s 166(1) the weekly rate of statutory maternity pay for the week in pounds`, `s 171ZE(1) the weekly rate of statutory paternity pay in pounds`, `s 171ZN(2E) the weekly rate of statutory adoption pay for the week in pounds`) and their tests.
- **A trace is not an assertion.**
  The stable binary prints a `#TRACE` result as an Information diagnostic (seen in this run with `l4 run ssc6-duties.l4`), and `check.sh` counts assertions only, so a trace that changed its outcome would turn nothing red.
  The regulative reference of the writing skill shows no `#ASSERT` over a trace.
  So the duties are covered twice: the four rules in `ssc6-duties.l4` are run, with the expected result written beside each of eight traces (a payment fulfils the duty; no payment leaves it standing and unbreached, because the text states no deadline); and the same entitlement-and-liability is a decision function that is asserted: `s 151(1) the employer is liable to make a payment of statutory sick pay in respect of the day`, `s 164(1) the woman is entitled to payments of statutory maternity pay`, `s 171ZA(1) he is entitled to statutory paternity pay on a birth` and `s 171ZB(1) he is entitled to statutory paternity pay on an adoption`, and `s 171ZL(1) he is entitled to statutory adoption pay`.
  I read the eight trace outcomes by hand on both binaries (stable and main) in this run; `check.sh` does not see a different `TRACE` outcome, as its last line says.
- **A `MUST` with no `WITHIN` is accepted** and stays unbreached for as long as the payment is outstanding, which matches a text that states no deadline.

**Followed from the brief, not re-tested.**
Parenthesise every `NOT`; one line per `#ASSERT`; bracket arithmetic that crosses a line break; write dates as `Date day month year` and define no `YMD`; write a list of strings as a vertical `LIST` block or inline `LIST a, b`; `IMPORT` finds only modules beside the importing file.

## What `check.sh` prints (ssc6)

Run from this folder as `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh`, with `JL4_LIBRARY_PATH` unset, binaries by absolute path.
The default target is `main`: each module runs on the stable binary and on the main build, and the main columns must match.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-cases-seat.l4                             0       115       0        0         0 |      0       115       0        0  same
ssc6-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc6-sap.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc6-smp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-spp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-ssp.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc6-tests-sap.l4                              0       219       0        0         0 |      0       219       0        0  same
ssc6-tests-smp.l4                              0       205       0        0         0 |      0       205       0        0  same
ssc6-tests-spp.l4                              0       207       0        0         0 |      0       207       0        0  same
ssc6-tests-ssp.l4                              0       194       0        0         0 |      0       194       0        0  same
TOTAL (12 modules)                             0       940       0        0           |      0       940       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced is the keel's: 165 assertions over `ssc-core.l4`, its definitions and its definitions tests; those files are not in this folder.
This folder is 12 modules (the core, the four rule modules, the duties module, the seat, its cases, and four test files): 940 assertions satisfied, 0 errors, 0 failed, 0 refused, on both builds.
The 940 are 205 (smp tests) + 194 (ssp) + 207 (spp) + 219 (sap) + 115 (seat cases); the core, the four rule modules, the duties module and the seat hold no assertions of their own.
`ssc6-duties.l4` has no assertions: its eight traces print Information messages that `check.sh` does not count (see "What the stable binary does not accept").

Quote gate, over every `ssc6-*.l4`:

```
$ python3 -I srcrefs.py check --refs ukpga-1992-4.txt ssc6-*.l4
srcrefs check: 377 src: lines, 213 runs, 248 locators, 0 problems
$ python3 -I srcrefs.py check --refs ukpga-1992-4.txt --strict ssc6-*.l4
srcrefs check: 377 src: lines, 213 runs, 248 locators, 0 problems
```

Two further checks, by hand:

- Flipping two expected values in a scratch copy of `ssc6-cases-seat.l4` gave 113 satisfied and 2 failed, so the seat cases can fail.
- No `.l4` file contains an absolute path (a search for the home-directory prefix finds none in any of the eleven `ssc6-*.l4` files), and `l4 check` raises no "is at the end of the file" or "follows code on its line" warning for any file.

## Files (ssc6)

All under `deposit/encodings/legalese-sonnet-5.5/`.

| file | what it is |
| --- | --- |
| ssc6-ssp.l4 | Part XI, statutory sick pay (ss 151-163); imports ssc6-smp |
| ssc6-smp.l4 | Part XII, statutory maternity pay (ss 164-171) |
| ssc6-spp.l4 | Part 12ZA, statutory paternity pay (ss 171ZA-171ZK) |
| ssc6-sap.l4 | Part 12ZB, statutory adoption pay (ss 171ZL-171ZT) |
| ssc6-duties.l4 | the four payment duties as regulative rules, with eight traces |
| ssc6-tests-ssp.l4, ssc6-tests-smp.l4, ssc6-tests-spp.l4, ssc6-tests-sap.l4 | tests for the four modules |
| ssc6-seat.l4 | layer 2, the seat: 42 exported questions |
| ssc6-cases-seat.l4 | layer 2, 115 cases for the seat |
| NOTES.md | this file |
| PROGRESS.md | working log |
| NEEDS-CORE.md | one core change asked for: a `Labour` field for "a child, alive or dead" |
| ssc-core.l4, check.sh, srcrefs.py, fetch-main-l4.sh | supplied; unchanged |
