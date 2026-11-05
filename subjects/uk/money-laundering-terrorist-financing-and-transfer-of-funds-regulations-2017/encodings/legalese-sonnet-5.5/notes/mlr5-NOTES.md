# NOTES -- mlr5: Schedules 3ZA, 3A, 4, 5, 6, 6A, 6B, 7 and the explanatory note

The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (United Kingdom), S.I. 2017/692, lines 3055-3808 of `uksi-2017-692.txt`.
This is part `mlr5` of a multi-part encoding; the shared core is the keel's `mlr-core.l4` (read-only here).

Status, 2026-11-05: written, then revised the same day under Meng's rulings of 2026-11-05 on periods, "where" and delegated definitions ("What the rulings of 2026-11-05 changed" below); checked on the main build 1.6.109, and read the same on the main build 1.6.108 (the `check.sh` table is below).
How it was verified: `l4 run` of every file with both binaries through `check.sh`; `srcrefs.py check --refs` and `--strict` on every `mlr5-*.l4` file (487 `-- src:` lines, 154 quote runs, 211 locators, 0 problems for each); a positive control on every test file and on the seat cases (`work/ctl.py`, not shipped: in a scratch copy the expected value of each of the 1146 assertions was changed to a different value of its type, namely TRUE and FALSE exchanged, JUST TRUE, JUST FALSE and NOTHING exchanged, a constructor replaced by another of its type, a number, string or date replaced; all 1146 then failed, none still passed); and a comparison of the `#TRACE` outcomes of `mlr5-tests-sch6a.l4` and `mlr5-tests-sch7.l4` on 1.6.108 and 1.6.109 (identical, because `check.sh` cannot see a trace difference).

**The text is a plain-text rendering made by a converter script.
It is not the official text, and nothing here is verified against the official text.**
Where the rendering prints no paragraph number, drops words (the ellipsis in Schedule 3A paragraph 13), or shows a Schedule as lines of dots (Schedule 3ZA, Schedule 7 paragraph 27), the encoding follows the rendering and says so.

## What is in this folder (mlr5)

| file | what it is |
| --- | --- |
| `mlr5-sch3a.l4`, `mlr5-tests-sch3a.l4` | Schedule 3A, excluded trusts (SEAM S-18, answering) |
| `mlr5-sch4.l4`, `mlr5-tests-sch4.l4` | Schedule 4, supervisory information (a table of 21 printed items) |
| `mlr5-sch5.l4`, `mlr5-tests-sch5.l4` | Schedule 5, connected persons (SEAM S-16, answering) |
| `mlr5-sch6.l4`, `mlr5-tests-sch6.l4` | Schedule 6, the meaning of "relevant requirement" (SEAM S-17, answering) |
| `mlr5-sch6a.l4`, `mlr5-tests-sch6a.l4` | Schedule 6A, the United Kingdom's financial intelligence unit |
| `mlr5-sch6b.l4`, `mlr5-tests-sch6b.l4` | Schedule 6B, changes in control of registered cryptoasset businesses (both sets of modifications) |
| `mlr5-sch7.l4`, `mlr5-tests-sch7.l4` | Schedule 7, the three inserted rules that stand alone (paragraphs 3(2), 12, 18) |
| `mlr5-seat.l4`, `mlr5-cases-seat.l4` | the seat layer and its cases |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | these notes, the progress file, and what the core lacks |

Schedule 3ZA and the explanatory note have no module: the first is shown blank in the text, the second is not operative.

Test counts, written by hand from the text before each run:

| file | assertions | `#TRACE` runs |
| --- | --- | --- |
| `mlr5-tests-sch3a.l4` | 224 | 0 |
| `mlr5-tests-sch4.l4` | 131 | 0 |
| `mlr5-tests-sch5.l4` | 46 | 0 |
| `mlr5-tests-sch6.l4` | 207 | 0 |
| `mlr5-tests-sch6a.l4` | 84 | 30 |
| `mlr5-tests-sch6b.l4` | 219 | 0 |
| `mlr5-tests-sch7.l4` | 36 | 3 |
| `mlr5-cases-seat.l4` | 199 | 0 |
| total | 1146 | 33 |

The `#TRACE` runs print `FULFILLED`, `BREACHED` or a residual obligation and never an assertion line, so they are counted apart from the assertions.


## What the rulings of 2026-11-05 changed (mlr5)

Meng's rulings of 2026-11-05 (the two bullets in the fork register) turned a number of NOTHING answers into JUST FALSE.
The first column is the shape; the others say what moved and where.

| shape | what changed | functions |
| --- | --- | --- |
| a "where", "if" or period that the text states, not met | JUST FALSE (the head still holds, so the trust or duty is described and the condition fails) | Schedule 3A: `para 1+1`, `4(1)`, `4(2)`, `6` (the date in 6(b)), `7(1)`, `7+1`, `7+2`, `9`, `9+1`, `12`, `13`, `14`, `15`; Schedule 6A: `para 2`, `5(a)`, `5(b)`, `7`, `8`, `10`, `12(a)`, `12(b)`, `13`, `14`, `15`, `16(a)`, `16(b)`, `16(c)`; Schedule 6B: `para 1`, `para 3`; Schedule 7: `para 18(c)` (the provision is void) |
| a paragraph closed by "only" | JUST FALSE for a case outside it | Schedule 3A `para 4(1)`, `4(2)` |
| a "means" definition inside a paragraph's head | its JUST FALSE passes through the paragraph | Schedule 3A `para 6A(1)`, `10(1)`, `12`, `13` (S3A-F7) |
| a definition handed to a list | JUST FALSE for a person or trust in none of the heads | `sch 5 the person is a connected person of the relevant person` (S5-F2); `sch 3A the trust is a trust listed in Schedule 3A` and `sch 3A the answers of the paragraphs, gathered` (S3A-F8) |
| a scope limit with no "where", "if", period or "only" | stays NOTHING | Schedule 3A paragraphs 1, 2, 3, 4(3), 5, 9B, 10(1)(a) and (b), 11, 16 to 16+6, 23, 23A(1); Schedule 4 "In the case of a self-regulatory organisation" (S4-F2); Schedule 6A paragraphs 3, 4, 9 and the "(subject to paragraph 10 / 11)" arms; Schedule 6B "to which Part 12 of FSMA would not otherwise apply" |

Added: the seat question `Under schedule 3A, is the trust an excluded trust, that is a trust listed in Schedule 3A (any of its paragraphs)` and its six cases; the helper `sch 3A treat an unknown answer as yes`.

## Coverage (mlr5)

How the table was built: a script (`work/coverage.py`, not shipped) reads the raw text and the `-- src:` quote runs in the seven layer-1 modules.
A quote run followed by declarations is an `encoded` row, or a `fork` row when it carries a fork of the register below; a quote run followed by a `§` heading is an `inert` heading row; the stretches no module quotes were classified by hand and added as the rows with an empty module.
Every row has exactly one disposition: `encoded`, `fork` (encoded under a reading taken from the fork register), `inert (reason 1)` (not operative: a title, a heading, the explanatory note), `inert (reason 2)` (machinery: an amendment of another Act or instrument), or `repealed or blank in this text` (reason 3).
A row may cover two or three adjacent units that one declaration encodes together (lines 3357-3358, the two short definitions of "the 2000 Act" and "the 2002 Act", are one row; the three lines of the definition of "external request", 3350-3352, are one).
No unit is in two rows.

Audit counts:

- non-blank lines in 3055-3808, counted by script: **754**;
- rows before the audit: 154, from the quote runs of the modules alone, which left 38 stretches of lines in no row (Schedule 3ZA, thirty-three rows of Schedule 7 amendments, the two Part headings of Schedule 7, paragraph 27 of Schedule 7, the explanatory note);
- rows after the audit: **192** (those 38 rows added); lines in no row: **0**; lines in two rows: **0**;
- by disposition: encoded 90; fork 57; inert, reason 1 (headings, explanatory note) 10; inert, reason 2 (amendments of other Acts and instruments) 33; repealed or blank in this text (reason 3) 2.


| lines | the text | disposition | L4 name |
| --- | --- | --- | --- |
| 3055-3081 | SCHEDULE 3ZA — High-Risk Third Countries | repealed or blank in this text | Schedule 3ZA (High-Risk Third Countries): the heading and 26 lines of dots; blank in the text. No function: the rendering lists no country, so there is nothing to look up (the list is the Treasury's, and regulation 33 points at this Schedule; the keel's `high-risk third country` input stands in for it) |
| 3082 | SCHEDULE 3A — Excluded Trusts | inert (reason 1: heading) |  |
| 3083-3084 | Legislative Trusts | encoded | `sch 3A para 1 the trust is a legislative trust` |
| 3085-3088 | A trust which ceases to be an excluded trust under paragraph 1 of this... | fork S3A-F1 S3A-F4 | `sch 3A para 1+1 the trust is a trust which ceases to be an excluded trust under paragraph 1 within two years of a trustee's death`; `sch 3A less than two years have passed since the death` |
| 3089-3090 | Trusts imposed by court order | encoded | `sch 3A para 2 the trust is a trust imposed by court order` |
| 3091-3092 | Pension scheme trusts | encoded | `sch 3A para 3 the trust is a pension scheme trust` |
| 3093-3096 | Trusts of insurance policies | encoded | `sch 3A para 4(1) the trust is a trust of a life policy paying out only on the listed events or for healthcare` |
| 3097-3099 | (2) A trust of an insurance policy paying out only— | fork S3A-F5 | `sch 3A para 4(2) the trust is a trust of an insurance policy paying out only on temporary disablement or for healthcare` |
| 3100 | (3) A trust of the benefits payable on the death of the person assured... | encoded | `sch 3A para 4(3) the trust is a trust of the death benefits of a retirement policy` |
| 3101-3104 | Charitable trusts | encoded | `sch 3A para 5 the trust is a charitable trust` |
| 3105-3108 | Pilot trusts | fork S3A-F3 | `sch 3A para 6(a) the value limit in pounds`; `sch 3A para 6 the trust is a pilot trust` |
| 3109-3114 | 6A	Bank accounts for minors etc | fork S3A-F7 | `sch 3A para 6A(1) the trust is created as a requirement of opening a relevant account for the sole benefit of a minor or an incapable person` |
| 3115-3117 | (2) In this paragraph— | encoded | `sch 3A para 6A(2) the account is a relevant account`; `sch 3A para 6A(2) the person is an authorised Part 4A person` |
| 3118-3122 | Trusts having effect on death | fork S3A-F4 | `sch 3A para 7(1) the trust is a trust effected by will holding only the estate within two years of the death`; `sch 3A para 7(2) the property is comprised in a person's estate` |
| 3123-3125 | A trust where— | fork S3A-F1 S3A-F4 | `sch 3A para 7+1 the trust holds only death benefits of a policy within paragraph 4 within two years of the death` |
| 3126-3130 | (1) A trust created under a deed or instrument which— | fork S3A-F1 S3A-F4 | `sch 3A para 7+2 the trust is created under a deed or instrument varying dispositions of an estate within two years of the death`; `sch 3A para 7+2(2) the property is comprised in P's estate` |
| 3131-3132 | Co-ownership | encoded | `sch 3A para 9 the trust is a co-ownership trust` |
| 3133-3135 | A trust which ceases to be an excluded trust under paragraph 9 of this... | fork S3A-F1 S3A-F4 | `sch 3A para 9+1 the trust is a trust which ceases to be an excluded trust under paragraph 9 within two years of a trustee's death` |
| 3136-3139 | 9B	Revocation of survivorship destination trusts | encoded | `sch 3A para 9B the trust is a trust created under a deed revoking a survivorship destination` |
| 3140-3146 | Financial markets infrastructure | fork S3A-F7 | `sch 3A para 10(1) the trust is a financial markets infrastructure trust` |
| 3147-3156 | (2) In this paragraph— | encoded | `sch 3A para 10(2) the entity is a segregating entity`; `sch 3A para 10(2) borrowed term`; `sch 3A para 10(2) the term has the meaning given by` |
| 3157-3161 | Professional services | encoded | `sch 3A para 11 the trust is a professional services trust`; `sch 3A para 11(b) borrowed term`; `sch 3A para 11(b) the term has the meaning given by` |
| 3162-3163 | Client money etc. | fork S3A-F7 | `sch 3A para 12 the trust is a client money trust` |
| 3164-3167 | Capital markets etc. | fork S3A-F6 S3A-F7 | `sch 3A para 13 the trust is a capital markets trust` |
| 3168-3172 | Commercial transactions | encoded | `sch 3A para 14 the trust is a commercial transactions trust` |
| 3173-3174 | Registration of assets | fork S3A-F9 | `sch 3A para 15 the trust is a registration of assets trust` |
| 3175-3176 | Trusts meeting legislative requirements | encoded | `sch 3A para 16 the trust holds property to which section 71A or 71D of the Inheritance Tax Act 1984 applies` |
| 3177 | A trust of property in respect of which a direction under paragraph 1 ... | fork S3A-F1 | `sch 3A para 16+1 the trust is of property subject to a direction under paragraph 1 of Schedule 4 to the Inheritance Tax Act 1984` |
| 3178-3180 | A trust of funds derived from a payment— | fork S3A-F1 | `sch 3A para 16+2 the trust is a trust of funds derived from a personal injury payment` |
| 3181 | A trust holding tenants’ contributions for the purposes of section 42 ... | fork S3A-F1 | `sch 3A para 16+3 the trust holds tenants' contributions` |
| 3182 | The plan trust of a share incentive plan which meets the requirements ... | fork S3A-F1 | `sch 3A para 16+4 the trust is the plan trust of a share incentive plan` |
| 3183 | A trust created under a share option scheme that meets the requirement... | fork S3A-F1 | `sch 3A para 16+5 the trust is created under a share option scheme` |
| 3184 | A trust holding property for a beneficiary who is a disabled person wi... | fork S3A-F1 | `sch 3A para 16+6 the trust holds property for a disabled beneficiary` |
| 3185-3191 | Public authorities | encoded | `sch 3A para 23 the trust is a public authorities trust` |
| 3192-3200 | 23A	General exclusion | encoded | `sch 3A para 23A(1)(b) the ceiling on assets of appreciable worth in pounds`; `sch 3A para 23A(1)(c) the ceiling on cumulative value held in pounds`; `sch 3A para 23A(1)(d) the ceiling on income per annum in pounds`; `sch 3A para 23A the trust is within the general exclusion` |
| 3201 | (3) In this paragraph, “assets of appreciable worth” includes works of... | encoded | `sch 3A para 23A(3) the asset is an asset of appreciable worth` |
| 3202-3205 | Interpretation | encoded | `sch 3A para 24 the person is a relevant supervised person`; `sch 3A facts about the trust`; `sch 3A treat an unknown answer as yes`; `sch 3A the answers of the paragraphs, gathered`; `sch 3A the trust is a trust listed in Schedule 3A` |
| 3206 | SCHEDULE 4 — Supervisory Information | inert (reason 1: heading) |  |
| 3207 | The number of persons subject to the supervision of the supervisory au... | fork S4-F2 | `sch 4 item 1`; `sch 4 item 1 the person is a supervised person` |
| 3208 | The number of supervised persons who are individuals. | encoded | `sch 4 item 2` |
| 3209 | In the case of a self-regulatory organisation, the number of its super... | fork S4-F2 | `sch 4 item 3` |
| 3210-3213 | In the case of a self-regulatory organisation, the number of applicati... | fork S4-F2 | `sch 4 item 4` |
| 3214 | The services provided by supervised persons. | encoded | `sch 4 item 5` |
| 3215-3219 | The number of firms subject to the supervision of the supervisory auth... | encoded | `sch 4 item 6`; `sch 4 item 6 the limb that counts firms of that rating`; `sch 4 item 6 risk refers to` |
| 3220-3223 | The number of applications for approval received by the supervisory au... | encoded | `sch 4 item 7` |
| 3224 | The number of approvals under regulation 26 which were not valid, or c... | encoded | `sch 4 item 8` |
| 3225 | In the case of a self-regulatory organisation, the number, amount and ... | fork S4-F2 | `sch 4 item 9` |
| 3226-3228 | The number of times the supervisory authority has— | encoded | `sch 4 item 10` |
| 3229 | The number of times the supervisory authority has exercised any powers... | encoded | `sch 4 item 11` |
| 3230 | The number of contraventions of these Regulations committed by supervi... | encoded | `sch 4 item 12` |
| 3231 | The number of contraventions of these Regulations identified upon exer... | encoded | `sch 4 item 13` |
| 3232 | The number and amount of penalties or charges which have been imposed ... | encoded | `sch 4 item 14` |
| 3233 | The number of times the supervisory authority has exercised the other ... | encoded | `sch 4 item 15` |
| 3234 | The number of times the supervisory authority or any of its supervised... | encoded | `sch 4 item 16`; `sch 4 item 16 suspicious activity disclosure has the meaning given in` |
| 3235 | A copy of any suspicious activity disclosure (within the meaning given... | encoded | `sch 4 item 17` |
| 3236-3238 | The number of supervised persons who have contravened requirements imp... | encoded | `sch 4 item 18` |
| 3239 | Information on the money laundering and terrorist financing practices ... | encoded | `sch 4 item 19` |
| 3240 | Indications that the supervisory authority considers to suggest that a... | encoded | `sch 4 item 20` |
| 3241 | The amount of human resource allocated by the supervisory authority to... | encoded | `sch 4 item 21`; `sch 4 the items`; `sch 4 the items asked of the supervisory authority`; `sch 4 the item is asked of the supervisory authority` |
| 3242 | SCHEDULE 5 — Connected Persons | inert (reason 1: heading) |  |
| 3243-3249 | Corporate Bodies | fork S5-F1 S5-F2 | `sch 5 para 1 the person is a connected person of the body corporate` |
| 3250-3251 | Partnerships | fork S5-F1 S5-F2 | `sch 5 para 2 the person is a connected person of the partnership` |
| 3252-3253 | Unincorporated Associations | fork S5-F1 S5-F2 | `sch 5 para 3 the person is a connected person of the unincorporated association` |
| 3254-3255 | Individuals | fork S5-F1 S5-F2 | `sch 5 para 4 the person is a connected person of the individual`; `sch 5 the person is a connected person of the relevant person` |
| 3256 | SCHEDULE 6 — Meaning of “relevant requirement” | inert (reason 1: heading) |  |
| 3257-3261 | For the purposes of Part 9 of these Regulations, “relevant requirement... | encoded | `sch 6 para 1(a) the requirement is imposed by the funds transfer regulation and specified in paragraph 2, 3 or 4` |
| 3262 | (b) a requirement imposed (otherwise than on supervisory authorities, ... | fork S6-F1 | `sch 6 para 1(b) the requirement is imposed in or under the regulations specified in paragraphs 5 to 13` |
| 3263-3267 | (c) the following requirements imposed on auction platforms— | fork S6-F2 | `sch 6 para 1(c) the requirement is one of those imposed on auction platforms`; `sch 6 the provision is a relevant requirement` |
| 3268-3274 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 2 the listed Articles` |
| 3275-3281 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 3 the listed Articles` |
| 3282-3289 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 4 the listed Articles` |
| 3290-3301 | The requirements specified in this paragraph are those— | encoded | `sch 6 para 5 the listed regulations` |
| 3302 | The requirements specified in this paragraph are those imposed in regu... | encoded | `sch 6 para 6 the listed regulations` |
| 3303-3315 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 7 the listed regulations` |
| 3316-3319 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 8 the listed regulations` |
| 3320-3324 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 9 the listed regulations` |
| 3325 | The requirements specified in this paragraph are those imposed in regu... | encoded | `sch 6 para 10 the listed regulations` |
| 3326-3330 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 11 the listed regulations` |
| 3331 | The requirements specified in this paragraph are those imposed in regu... | encoded | `sch 6 para 12 the listed regulations` |
| 3332-3338 | The requirements specified in this paragraph are those imposed in— | encoded | `sch 6 para 13 the listed regulations` |
| 3339-3347 | The requirements specified in this paragraph are those imposed under— | fork S6-F1 | `sch 6 para 14 the listed regulations` |
| 3348 | The requirement specified in this paragraph is the requirement imposed... | fork S6-F1 | `sch 6 para 15 the listed regulations`; `sch 6 para 1(c)(iv) the listed regulations`; `sch 6 the listed provision covers the requirement`; `sch 6 the listed provision covers only some paragraphs of the one asked about`; `sch 6 the requirement is within the list` |
| 3349 | SCHEDULE 6A — The United Kingdom’s Financial Intelligence Unit | inert (reason 1: heading) |  |
| 3350-3352 | Interpretation | encoded | `sch 6A para 1 the request is an external request` |
| 3353 | “FIU functions” means the functions of a financial intelligence unit a... | encoded | `sch 6A para 1 FIU functions are` |
| 3354 | “foreign competent authority” means an authority in an EEA state other... | encoded | `sch 6A para 1 the authority is a foreign competent authority` |
| 3355 | “foreign FIU” means an authority in an EEA state other than the United... | encoded | `sch 6A para 1 the authority is a foreign FIU` |
| 3356 | “relevant information” means information the NCA possesses in connecti... | encoded | `sch 6A para 1 the information is relevant information` |
| 3357-3358 | “the 2000 Act” means the Terrorism Act 2000 ; | encoded | `sch 6A para 1 the defined Act is` |
| 3359 | “United Kingdom competent authority” means any authority other than th... | fork S6A-F2 | `sch 6A para 1 the body is a United Kingdom competent authority` |
| 3360-3361 | Reports to the National Crime Agency | fork S6A-F5 | `sch 6A para 2 the authority must provide a report to the NCA`; `sch 6A para 2 the report duty` |
| 3362-3363 | Co-operation | encoded | `sch 6A para 3 the NCA must take such steps as it considers appropriate to co-operate with the foreign FIU`; `sch 6A para 3 the co-operation duty` |
| 3364-3365 | Provision of information in response to external requests | fork S6A-F4 | `sch 6A para 4 the NCA must provide promptly any relevant information in its possession`; `sch 6A para 4 the duty to provide information` |
| 3366-3368 | Where an external request is received and the NCA does not possess inf... | fork S6A-F1 S6A-F4 S6A-F5 | `sch 6A para 5(a) the NCA may exercise its powers to seek an order for information from the relevant person`; `sch 6A para 5(a) the power to seek an order`; `sch 6A para 5(b) the NCA must provide to the foreign FIU the relevant information received in consequence of an order`; `sch 6A para 5(b) the duty to pass on the information received` |
| 3369 | The NCA must designate at least one point of contact with responsibili... | fork S6A-F1 | `sch 6A para 6 the NCA must designate at least one point of contact`; `sch 6A para 6 the duty to designate a point of contact` |
| 3370 | Where the NCA has provided relevant information to a foreign FIU, and ... | fork S6A-F1 S6A-F5 | `sch 6A para 7 the NCA must consent to the dissemination of the requested information`; `sch 6A para 7 the duty to consent to dissemination` |
| 3371 | Where the NCA provides relevant information in response to an external... | fork S6A-F1 S6A-F5 | `sch 6A para 8 the NCA shall take such steps as it considers appropriate to ensure the information is transmitted securely`; `sch 6A para 8 the duty to transmit securely` |
| 3372-3373 | Conditions and restrictions on provision or further dissemination of... | encoded | `sch 6A para 9 the NCA may impose restrictions and conditions on the use of the information`; `sch 6A para 9 the power to impose restrictions and conditions` |
| 3374 | Where an obligation arises under this Schedule for the NCA to provide ... | fork S6A-F1 S6A-F5 | `sch 6A para 10 the NCA may decide not to provide some or all of the information`; `sch 6A para 10 the power to decide not to provide information` |
| 3375-3377 | The NCA is not required to comply with the duty to give consent to the... | fork S6A-F1 | `sch 6A para 11 the NCA is required to give the consent under paragraph 7` |
| 3378-3381 | The NCA must have particular regard— | fork S6A-F1 S6A-F5 | `sch 6A para 12(a) the NCA must have particular regard to the need for as unfettered an exchange of relevant information as possible`; `sch 6A para 12(a) the duty to have regard to the exchange of information`; `sch 6A para 12(b) the NCA must have particular regard to the need for as unfettered dissemination of information by the foreign FIU as possible`; `sch 6A para 12(b) the duty to have regard to dissemination` |
| 3382-3383 | Requests for information by the NCA to foreign FIUs | fork S6A-F3 S6A-F5 | `sch 6A para 13 paragraphs 14 and 15 apply` |
| 3384 | The NCA must address a request for the information to the foreign FIU ... | fork S6A-F1 S6A-F3 | `sch 6A para 14 the NCA must address the request to the foreign FIU in the state of the head office`; `sch 6A para 14 the duty to address the request to the foreign FIU` |
| 3385 | Where the NCA makes a request to a foreign FIU for information which t... | fork S6A-F1 S6A-F3 S6A-F5 | `sch 6A para 15 the request must contain the relevant facts, the reasons and the proposed use`; `sch 6A para 15 the duty on the content of the request` |
| 3386-3390 | Conditions and restrictions on use of information received by the N... | fork S6A-F5 | `sch 6A para 16(a) the NCA must use the information only for the purpose for which it was sought or provided`; `sch 6A para 16(a) the duty to use the information only for its purpose`; `sch 6A para 16(b) the NCA must comply with the restrictions or conditions of use imposed by the foreign FIU`; `sch 6A para 16(b) the duty to comply with the foreign FIU's restrictions`; `sch 6A para 16(c) the NCA must obtain the prior consent of the foreign FIU to any further dissemination`; `sch 6A para 16(c) the duty to obtain consent to further dissemination` |
| 3391 | Schedule 6B — Changes in Control of Registered Cryptoasset Businesses | inert (reason 1: heading) |  |
| 3392-3393 | Modifications: Control over registered cryptoasset businesses regist... | fork S6B-F1 S6B-F2 S6B-F4 | `sch 6B para 1 the date before which the business must have been included in the register`; `sch 6B para 1 Part 12 of FSMA applies to the business with the modifications specified in paragraph 2` |
| 3394 | The modifications specified in this paragraph are— | fork S6B-F2 | `sch 6B para 2 the modifications` |
| 3395-3396 | (a) references to a “UK authorised person” are to be read as reference... | encoded | `sch 6B para 2(a) and (b) a reference in Part 12 of FSMA is read as` |
| 3397 | (c) section 178 (obligation to notify the appropriate regulator: acqui... | encoded | `sch 6B para 2(c) section 178` |
| 3398-3407 | (d) section 181 (acquiring control) is to be read as if it said— | encoded | `sch 6B para 2(d) section 181`; `sch 6B para 2(d) section 181(1)(b) the person would hold the control described in limb (b)`; `sch 6B para 2(d) section 181 the person acquires control over the business` |
| 3408-3421 | (e) section 182 (increasing control) is to be read as if it said— | encoded | `sch 6B para 2(e) section 182`; `sch 6B para 2(e) section 182(2) the percentage rises by one of the steps`; `sch 6B para 2(e) section 182(1)(b) the person would increase the holding described in limb (b)`; `sch 6B para 2(e) section 182 the person increases control over the business` |
| 3422-3441 | (f) section 183 (reducing or ceasing to have control) is to be read as... | fork S6B-F5 | `sch 6B para 2(f) section 183`; `sch 6B para 2(f) section 183(2) the percentage falls by one of the steps`; `sch 6B para 2(f) section 183(1)(b) the person would decrease the holding described in limb (b)`; `sch 6B para 2(f) section 183(1) the person reduces control over the business`; `sch 6B para 2(f) section 183(3)(b) the person ceases to be in the position described in limb (b)`; `sch 6B para 2(f) section 183(3) the person ceases to have control over the business` |
| 3442 | (g) section 184 (disregarded holdings) is to be read as if subsections... | encoded | `sch 6B para 2(g) section 184` |
| 3443-3445 | (h) section 185 (assessment: general) is to be read as if— | encoded | `sch 6B para 2(h) section 185` |
| 3446-3448 | (i) section 186 (assessment criteria) is to be read in relation to a s... | encoded | `sch 6B para 2(i) section 186`; `sch 6B para 2(i) section 186 the section 178 notice-giver is a fit and proper person within the meaning of regulation 58A` |
| 3449 | (j) section 187 (approval with conditions) is to be read as if subsect... | encoded | `sch 6B para 2(j) section 187` |
| 3450 | (k) section 187A (assessment: consultation by PRA with FCA) is to be d... | encoded | `sch 6B para 2(k) section 187A` |
| 3451 | (l) section 187B (assessment: consultation by FCA with PRA) is to be d... | encoded | `sch 6B para 2(l) section 187B` |
| 3452 | (m) section 187C (variation etc of conditions) is to be disregarded; | encoded | `sch 6B para 2(m) section 187C` |
| 3453-3455 | (n) section 189 (assessment: procedure) is to be read as if— | encoded | `sch 6B para 2(n) section 189` |
| 3456 | (o) section 190 (requests for further information) is to be read as if... | encoded | `sch 6B para 2(o) section 190` |
| 3457 | (p) section 190A (assessment and resolution) is to be disregarded; | encoded | `sch 6B para 2(p) section 190A` |
| 3458-3460 | (q) section 191A (objection by the appropriate regulator) is to be rea... | encoded | `sch 6B para 2(q) section 191A` |
| 3461-3468 | (r) section 191B (restriction notices) is to be read as if— | encoded | `sch 6B para 2(r) section 191B`; `sch 6B para 2(r) section 191B(3ZA) the FCA may direct that no influence over the management or activities of the business is to be exercisable by the person` |
| 3469-3471 | (s) section 191C (orders for sale of shares) is to be read as if— | encoded | `sch 6B para 2(s) section 191C` |
| 3472 | (t) section 191D (obligation to notify the appropriate regulator: disp... | encoded | `sch 6B para 2(t) section 191D` |
| 3473-3488 | (u) section 191F (offences under this Part) is to be read as if— | fork S6B-F3 | `sch 6B para 2(u) section 191F`; `sch 6B para 2(u)(iii) the penalty for the offence`; `sch 6B para 2(u)(iv) section 191F(10) the person is not guilty because the person took all reasonable steps and exercised all due diligence` |
| 3489-3492 | (v) section 191G (interpretation) is to be read— | fork S6B-F1 | `sch 6B para 2(v) section 191G`; `sch 6B para 2(v)(ii) the business is a registered cryptoasset business within section 191G` |
| 3493-3494 | Modifications: Control over registered cryptoasset businesses regist... | fork S6B-F1 S6B-F2 S6B-F4 | `sch 6B para 3 the date on or after which the business must have been included in the register`; `sch 6B para 3 Part 12 of FSMA applies to the business with the modifications specified in paragraph 4` |
| 3495 | The modifications specified in this paragraph are— | fork S6B-F2 | `sch 6B para 4 the modifications` |
| 3496-3497 | (a) references to a “UK authorised person” are to be read as reference... | encoded | `sch 6B para 4(a) and (b) a reference in Part 12 of FSMA is read as` |
| 3498 | (c) section 178 (obligation to notify the appropriate regulator: acqui... | encoded | `sch 6B para 4(c) section 178` |
| 3499 | (d) section 184 (disregarded holdings) is to be read as if subsections... | encoded | `sch 6B para 4(d) section 184` |
| 3500 | (e) section 185 (assessment: general) is to be read as if in subsectio... | encoded | `sch 6B para 4(e) section 185` |
| 3501 | (f) section 187 (approval with conditions) is to be read as if subsect... | encoded | `sch 6B para 4(f) section 187` |
| 3502 | (g) section 187A (assessment: consultation by PRA with FCA) is to be d... | encoded | `sch 6B para 4(g) section 187A` |
| 3503 | (h) section 187B (assessment: consultation by FCA with PRA) is to be d... | encoded | `sch 6B para 4(h) section 187B` |
| 3504 | (i) section 187C (variation etc of conditions) is to be disregarded; | encoded | `sch 6B para 4(i) section 187C` |
| 3505-3507 | (j) section 189 (assessment: procedure) is to be read as if— | encoded | `sch 6B para 4(j) section 189` |
| 3508 | (k) section 190 (requests for further information) is to be read as if... | encoded | `sch 6B para 4(k) section 190` |
| 3509 | (l) section 190A (assessment and resolution) is to be disregarded; | encoded | `sch 6B para 4(l) section 190A` |
| 3510-3512 | (m) section 191A (objection by the appropriate regulator) is to be rea... | encoded | `sch 6B para 4(m) section 191A` |
| 3513 | (n) section 191B (restriction notices) is to be read as if subsection ... | encoded | `sch 6B para 4(n) section 191B` |
| 3514-3516 | (o) section 191C (orders for sale of shares) is to be read as if— | encoded | `sch 6B para 4(o) section 191C` |
| 3517 | (p) section 191D (obligation to notify the appropriate regulator: disp... | encoded | `sch 6B para 4(p) section 191D` |
| 3518-3533 | (q) section 191F (offences under this Part) is to be read as if— | fork S6B-F3 | `sch 6B para 4(q) section 191F`; `sch 6B para 4(q)(iii) the penalty for the offence`; `sch 6B para 4(q)(iv) section 191F(10) the person is not guilty because the person took all reasonable steps and exercised all due diligence` |
| 3534-3537 | (r) section 191G (interpretation) is to be read as if— | fork S6B-F1 | `sch 6B para 4(r) section 191G`; `sch 6B para 4(r)(ii) the business is a registered cryptoasset business within section 191G` |
| 3538-3539 | Interpretation | encoded | `sch 6B para 5 the business is a cryptoasset business` |
| 3540-3542 | “cryptoasset business” means a cryptoasset exchange provider or a cust... | encoded | `sch 6B para 5 defined term`; `sch 6B para 5 the term has the meaning given by` |
| 3543 | “registered cryptoasset business” means a cryptoasset exchange provide... | fork S6B-F1 | `sch 6B para 5 the business is a registered cryptoasset business`; `sch 6B paras 1 and 3 which set of modifications applies`; `sch 6B a list of modifications treats the section as`; `sch 6B paras 2 and 4 how the applicable set treats a section of Part 12 of FSMA` |
| 3544 | SCHEDULE 7 — Consequential Amendments | inert (reason 1: heading) |  |
| 3545 | PART 1 — Consequential Amendments to Primary Legislation | inert (reason 1: heading) | PART 1 -- Consequential Amendments to Primary Legislation (a heading; Part 1 is paragraphs 1 to 11; nothing turns on the count) |
| 3546-3548 | Solicitors (Scotland) Act 1980 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 1, Solicitors (Scotland) Act 1980: inserts section 34(1D), 'Rules made under this section may make provision as to the way in which solicitors and incorporated practices are to comply with' these Regulations. Inert: an enabling power for the rules of another Act, with no condition to test and no actor named; the host section is not among the sources (the same reason as S7-F2) |
| 3549-3552 | Northern Ireland Act 1998 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 2, Northern Ireland Act 1998: replaces a reference to the 2007 Regulations in paragraph 25 of Schedule 3 and omits paragraph 25A. Inert: a textual amendment; the amended text is not among the sources |
| 3553-3554 | Financial Services and Markets Act 2000 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 3(1), Financial Services and Markets Act 2000: 'FSMA is amended as follows'. Inert: the lead-in to the amendments of paragraph 3 (sub-paragraph (2) is encoded in its own row) |
| 3555-3564 | (2) In section 226 (complaints: the ombudsman scheme etc) after subsec... | fork S7-F2 | `sch 7 para 3(2) s 226(7B) the person is within the subsection`; `sch 7 para 3(2) s 226(7C) the complaint is one to which the subsection applies`; `sch 7 para 3(2) s 226(7A) the rules must provide that the person is eligible in relation to the complaint`; `sch 7 para 3(2) s 226(7D) the term has the meaning given in` |
| 3565-3570 | (3) For the heading of Part 20C (as inserted by the Bank of England an... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 3(3) and (4), Financial Services and Markets Act 2000: renames the heading of Part 20C; amends the heading of section 333U and subsection (3) of it (the Secretary of State becomes the Treasury; 'or under the ombudsman scheme' added). Inert: textual amendments; section 333U is not among the sources |
| 3571-3611 | Terrorism Act 2000 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 4, Terrorism Act 2000: replaces references to the 2007 Regulations and the 2005 directive, and amends Parts 1 and 2 of Schedule 3A to that Act (business in the regulated sector: a figure of 15,000 becomes 10,000, activities are added; supervisory authorities). Inert: textual amendments; the amended text is not among the sources |
| 3612-3620 | Criminal Justice and Police Act 2001 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 5, Criminal Justice and Police Act 2001: replaces references to regulation 39(6) of the 2007 Regulations with regulation 70(7) of these, and omits paragraphs. Inert: textual amendments |
| 3621-3663 | Proceeds of Crime Act 2002 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 6, Proceeds of Crime Act 2002: the same amendments as paragraph 4, to sections 333D and 333E and to Parts 1 and 2 of Schedule 9. Inert: textual amendments; the amended text is not among the sources |
| 3664-3666 | Counter-Terrorism Act 2008 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 7, Counter-Terrorism Act 2008: substitutes paragraph 45(3) of Schedule 7 to that Act ('Unless otherwise defined, expressions used in this Schedule and in Directive 2015/849/EU ... have the same meaning as in that Directive'). Inert: an interpretation clause of another Act; the directive is not among the sources |
| 3667-3670 | Borders, Citizenship and Immigration Act 2009 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 8, Borders, Citizenship and Immigration Act 2009: replaces references to a directive and a regulation in section 1(2)(d) and (e). Inert: textual amendment |
| 3671-3672 | Crime and Courts Act 2013 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 9, Crime and Courts Act 2013: replaces a reference to regulation 45 of the 2007 Regulations in paragraph 27 of Schedule 17. Inert: textual amendment |
| 3673-3674 | Finance Act 2014 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 10, Finance Act 2014: replaces a reference to regulation 45(1) of the 2007 Regulations with regulation 86(1) in paragraph 6(4)(j) of Schedule 34. Inert: textual amendment |
| 3675-3680 | Bank of England and Financial Services Act 2016 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 11, Bank of England and Financial Services Act 2016: adds 'and terrorist financing' to headings above and in section 30, and replaces the Secretary of State with the Treasury in section 30(1). Inert: textual amendments |
| 3681 | PART 2 — Consequential Amendments to Secondary Legislation | inert (reason 1: heading) | PART 2 -- Consequential Amendments to Secondary Legislation (a heading; Part 2 is paragraphs 12 to 35, of which paragraph 27 is blank; nothing turns on the count) |
| 3682-3686 | Estate Agents (Undesirable Practices) (No 2) Order 1991 | fork S7-F1 | `sch 7 para 12 paragraph 2 of Schedule 3 to the Estate Agents (Undesirable Practices) (No 2) Order 1991 applies` |
| 3687-3694 | Public Interest Disclosure (Prescribed Persons) Order (Northern Ire... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 13, Public Interest Disclosure (Prescribed Persons) Order (Northern Ireland) 1999: replaces a reference and inserts an entry in the Schedule's table of matters ('Matters relating to compliance with' the Terrorism Act 2000, the Proceeds of Crime Act 2002 or these Regulations). Inert: a table entry in another Order, with no condition to test; the host Order is not among the sources |
| 3695-3696 | Terrorism Act 2000 (Crown Servants and Regulators) Regulations 2001 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 14, Terrorism Act 2000 (Crown Servants and Regulators) Regulations 2001: replaces 'regulation 3(1)(a) to (h) of the Money Laundering Regulations 2007' with 'regulation 8(2)(a) to (h)' of these. Inert: textual amendment |
| 3697-3698 | Representation of the People (England and Wales) Regulations 2001 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 15, Representation of the People (England and Wales) Regulations 2001: replaces a reference to the 2007 Regulations. Inert: textual amendment |
| 3699-3700 | Representation of the People (Scotland) Regulations 2001 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 16, Representation of the People (Scotland) Regulations 2001: replaces a reference to the 2007 Regulations. Inert: textual amendment |
| 3701-3702 | Financial Services and Markets Act 2000 (Regulated Activities) Orde... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 17, Financial Services and Markets Act 2000 (Regulated Activities) Order 2001: replaces a reference to the 2007 Regulations in article 72E(9). Inert: textual amendment |
| 3703-3711 | Open-Ended Investment Companies Regulations 2001 | fork S7-F3 | `sch 7 para 18(b) the relevant date`; `sch 7 para 18(c) paragraph (3) the application was made before and determined on or after the relevant date`; `sch 7 para 18(c) paragraph (2) the open-ended investment company may issue bearer shares under paragraph (1)`; `sch 7 para 18(c) paragraph (2) the prohibition on issuing bearer shares`; `sch 7 para 18(c) paragraph (2) the provision in the instrument of incorporation is void` |
| 3712-3713 | Proceeds of Crime Act 2002 (Disclosure of information to and by Lor... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 19, Proceeds of Crime Act 2002 (Disclosure of information to and by Lord Advocate and Scottish Ministers) Order 2003: replaces a reference to the 2007 Regulations in article 3(d). Inert: textual amendment |
| 3714-3715 | Proceeds of Crime Act 2002 (Failure to Disclose Money Laundering: S... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 20, Proceeds of Crime Act 2002 (Failure to Disclose Money Laundering: Specified Training) Order 2003: replaces 'regulation 21 of the Money Laundering Regulations 2007' with 'regulation 24' of these. Inert: textual amendment |
| 3716-3719 | Legislative and Regulatory Reform (Regulatory Functions) Order 2007 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 21, Legislative and Regulatory Reform (Regulatory Functions) Order 2007: replaces references to the 2007 Regulations and to Schedule 3 to them. Inert: textual amendments |
| 3720-3722 | Representation of the People (Northern Ireland) Regulations 2008 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 22, Representation of the People (Northern Ireland) Regulations 2008: substitutes paragraph (i) of regulation 112(3)(b) with a reference to these Regulations. Inert: textual amendment |
| 3723-3726 | Transfer of Tribunal Functions and Revenue and Customs Appeals Orde... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 23, Transfer of Tribunal Functions and Revenue and Customs Appeals Order 2009: replaces 'regulations 43 and 44' of the 2007 Regulations with 'regulations 94 to 100' of these and omits paragraph (j). Inert: textual amendment |
| 3727-3743 | Payment Services Regulations 2009 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 24, Payment Services Regulations 2009: replaces references to the 2007 Regulations and the 2005 directive in regulations 2, 6, 13, 25, 29 and 119 and Schedules 2 and 5. Inert: textual amendments |
| 3744-3747 | Companies (Disclosure of Address) Regulations 2009 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 25, Companies (Disclosure of Address) Regulations 2009: replaces references to the 2007 Regulations and the 2005 directive in paragraph 7(b) of Schedule 2. Inert: textual amendments |
| 3748-3751 | Overseas Companies Regulations 2009 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 26, Overseas Companies Regulations 2009: replaces references to the 2007 Regulations and the 2005 directive in paragraph 7(b) of Schedule 2. Inert: textual amendments |
| 3752-3753 | Defence and Security Public Contracts Regulations 2011 | repealed or blank in this text | Schedule 7 paragraph 27, Defence and Security Public Contracts Regulations 2011: the heading and a line of dots; blank in the text. No function |
| 3754-3768 | Electronic Money Regulations 2011 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 28, Electronic Money Regulations 2011: replaces references to the 2007 Regulations and the 2005 directive. Inert: textual amendments |
| 3769-3772 | Terrorism Act 2000 and Proceeds of Crime Act 2002 (Business in the ... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 29, Terrorism Act 2000 and Proceeds of Crime Act 2002 (Business in the Regulated Sector) (No 2) Order 2012: replaces a directive reference in regulation 4(2) and, in regulation 4(4), replaces 'the end of the period of five years beginning with the day on which this Order comes into force' with '26th June 2022'. Inert here: it moves a date in another Order's review clause, and that Order's duty to review is not among the sources |
| 3773-3774 | Payment to Treasury of Penalties (Enforcement Costs) Order 2013 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 30, Payment to Treasury of Penalties (Enforcement Costs) Order 2013: replaces 'regulation 42' of the 2007 Regulations with 'regulation 76' of these. Inert: textual amendment |
| 3775-3782 | Public Interest Disclosure (Prescribed Persons) Order 2014 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 31, Public Interest Disclosure (Prescribed Persons) Order 2014: substitutes the second-column entry for the National Crime Agency (matters relating to bribes, and to compliance with three enactments). Inert: a table entry in another Order, with no condition to test |
| 3783-3786 | Companies (Disclosure of Date of Birth Information) Regulations 201... | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 32, Companies (Disclosure of Date of Birth Information) Regulations 2015: replaces references to the 2007 Regulations and the 2005 directive. Inert: textual amendments |
| 3787-3788 | Payment Accounts Regulations 2015 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 33, Payment Accounts Regulations 2015: replaces a reference to the 2007 Regulations in regulation 25(1)(b). Inert: textual amendment |
| 3789-3792 | Register of People with Significant Control Regulations 2016 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 34, Register of People with Significant Control Regulations 2016: replaces references to the 2007 Regulations and the 2005 directive in paragraph 8(b) of Schedule 4. Inert: textual amendments |
| 3793-3794 | Economic Growth (Regulatory Functions) Order 2017 | inert (reason 2: amendment of another Act or instrument) | Schedule 7 paragraph 35, Economic Growth (Regulatory Functions) Order 2017: replaces a reference to the 2007 Regulations in the entry for Her Majesty's Revenue and Customs. Inert: textual amendment |
| 3795-3808 | (This note is not part of the Regulations) | inert (reason 1: not operative) | Explanatory note: "(This note is not part of the Regulations)" and its summary of the Parts |


### Gaps stated under the coverage rows

- **Schedule 3ZA (lines 3055-3081): blank in the text.** The heading is followed by 26 lines of dots; there is nothing to encode, and no function.
- **Schedule 3A paragraph 6(b) (line 3108).** "The date on which regulation 42(2)(iii) of these Regulations comes into force" is not in the text, so the date is an input DATE the caller states (S3A-F3).
- **Schedule 4 (lines 3206-3241).** The 21 items are free text in the quote runs: no function returns an item's wording, because the Schedule asks for information and states no rule over its words.
  The text is also silent on how often the information is collected or reported (regulation 51(1), line 1715, says only "must collect"; the Treasury's annual review is regulation 51(3), another part's), so there is no function for a frequency (S4-F3).
- **Schedule 6A (lines 3349-3390).** The text is silent on how long "promptly" is (paragraphs 4, 5(b) and 7) and on the most points of contact the NCA may designate (paragraph 6 says "at least one"), so no function returns a time or a number, and the regulative rules carry no WITHIN (S6A-F4).
  The paragraph 6 duty to designate "at least one" point of contact is a rule with no condition; it returns no number.
  **For the merge:** "the duty does not arise" is answered by a companion decision function, as part 4 did, and not through the compliance function: each Schedule 6A duty or permission has a decision function that answers JUST TRUE (it arises), JUST FALSE (a "where", "upon request" or "apply where" of the paragraph is not met) or NOTHING (a scope with no such word, or an exception); the regulative rule calls it and returns the duty only for JUST TRUE, and FULFILLED (no duty) for anything else.
- **Schedule 7 (lines 3544-3794).** Three paragraphs are encoded (3(2), 12, 18).
  Every other row has no function; the reason for each is in the table above: paragraph 1 inserts an enabling power for the rules of another Act, with no condition to test and no actor named; paragraph 27 is blank in the text; the rest (paragraphs 2, 3(1), 3(3) and (4), 4 to 11, 13 to 17, 19 to 26, 28 to 35) change words in other Acts and instruments, or insert table entries in them, and the amended text is not among the sources.
  Paragraph 29(3) replaces a period of five years in another Order's review clause with the date 26th June 2022; the date is noted in its row and nothing here turns on it.
  Part 1 is paragraphs 1 to 11 and Part 2 is paragraphs 12 to 35; the Part headings are inert and nothing turns on a count of them.

## Fork register (mlr5)

### The two rulings of 2026-11-04, word for word

As printed in the brief:

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.

- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.

As recorded in the Commons guide (section 5):

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  Assumed, not ruled: "once" and "in the event of" count as "where" (neither word occurs in lines 3055-3808); a function that returns a number, a date or a record cannot carry JUST FALSE, so it gets a yes/no twin (none was needed here: S6B-F4).
  There is no "until" bar and no "it is a defence ... to prove" in lines 3055-3808: Schedule 6B section 191F(10), "A person is not guilty ... if that person took all reasonable steps and exercised all due diligence", is a flat negative with "if", and already answers JUST FALSE when its conditions are not met.

**Where this part gathered a legal effect by hand (ruling E1, option B as guidance for hand-gathering only).**
Each of these is one plain function in plain L4 that calls the per-paragraph answers and combines them; the per-paragraph answers remain the primary encoding (option C), and no construct gathers by name.

| gather | what it combines | where |
| --- | --- | --- |
| `sch 3A the trust is a trust listed in Schedule 3A` (with `sch 3A the answers of the paragraphs, gathered`) | the answers of the 31 paragraph functions of Schedule 3A that describe a kind of trust (the six definitions the paragraphs call are not among them): JUST TRUE if any says the trust is of its kind; NOTHING if an unknown relevant-supervised-person answer (paragraph 12 or 13) could make one say so; otherwise JUST FALSE (S3A-F8) | `mlr5-sch3a.l4`, SEAM S-18 |
| `sch 5 the person is a connected person of the relevant person` | paragraphs 1 to 4, chosen by the legal form of the subject: JUST TRUE if any says so, otherwise JUST FALSE (regulation 65(3) hands the definition to the list: S5-F2) | `mlr5-sch5.l4`, SEAM S-16 |
| `sch 6 the provision is a relevant requirement` | limbs (a), (b), (c) of the chapeau and the fourteen printed lists | `mlr5-sch6.l4`, SEAM S-17 |
| `sch 6B paras 1 and 3 which set of modifications applies` | paragraphs 1 and 3 (the two vintages, split on the date the business was entered on the register; it returns a constructor, so it has no JUST FALSE and no twin: S6B-F4) | `mlr5-sch6b.l4` |
| `sch 6B paras 2 and 4 how the applicable set treats a section of Part 12 of FSMA` | the tables of paragraphs 2 and 4, for one section | `mlr5-sch6b.l4` |
| `sch 6B at least one of the two answers is yes` | two beneficial-owner answers joined by "or" | `mlr5-sch6b.l4` (a helper, not a provision) |
| `sch 7 para 3(2) s 226(7A) the rules must provide that the person is eligible in relation to the complaint` | the inserted subsections (7B) and (7C) | `mlr5-sch7.l4` |

### The forks

Each row gives the readings seen, the one taken, and the text that licenses it.
"Marginal" means the reading also appears under "Marginal readings for a lawyer" below.

| id | lines | the question | readings seen | reading taken | the text that licenses it |
| --- | --- | --- | --- | --- | --- |
| S3A-F1 | 3085-3088, 3123-3130, 3133-3135, 3177-3184 | The rendering prints a number for paragraphs 1 to 6, 6A, 7, 9, 9B, 10 to 16, 23, 23A and 24 and leaves the other paragraphs of Schedule 3A bare. | (i) label each bare paragraph by position after the last printed number; (ii) fold it into the numbered paragraph above as a limb; (iii) infer the official number | (i): `sch 3A para 1+1`, `7+1`, `7+2`, `9+1`, `16+1` to `16+6`. The labels carry no official number. | Each bare paragraph is a complete description of a kind of trust (for example line 3085 begins "A trust which ceases to be an excluded trust under paragraph 1 of this Schedule where"), so it cannot be a limb of the one above. |
| S3A-F2 | all of 3082-3205 | A trust that fits no paragraph, or fits a paragraph's head but not the "which" clause, the bare list or the amount that completes it: is it not an excluded trust (JUST FALSE) or not covered (NOTHING)? | (i) JUST FALSE, because the Schedule lists the excluded trusts; (ii) NOTHING | (ii) for each paragraph whose whole description is a relative clause, a bare list or an amount (paragraphs 1, 2, 3, 4(3), 5, 6(a), 9B, 10(1)(a) and (b), 11, 16 to 16+6, 23, 23A(1)): marginal (b) in kind, the list is not closed. A paragraph that states a "where", an "if", a period or "only" answers JUST FALSE when it is not met (rulings of 2026-11-05); the combined function answers JUST FALSE for a trust within no paragraph (S3A-F8). Reviewer expected JUST FALSE for the heads that fail only on a "which" clause, a bare list or an amount (scenarios 12, 22, 26, 28, 29, 32, 38, 46, 52, 62, 68, 73, 85, 87, 88, 89, 90; seat S2); open question. | The Schedule lists kinds of trust and nowhere says "only" or "nothing but". Paragraph 23A(2) ("This paragraph does not apply to a trust which is a UK trust ...", line 3198) is the one flat negative and answers JUST FALSE. |
| S3A-F3 | 3108 | Paragraph 6(b) turns on "the date on which regulation 42(2)(iii) of these Regulations comes into force", which the rendering does not give. A trust created on or after it: NOTHING or JUST FALSE? | (i) a constant from memory; (ii) an input the caller states. For a trust created on or after it: (iii) NOTHING; (iv) JUST FALSE | (ii): an input `DATE`, which is how the commencement date stays an input (a reviewer reads "(2)(iii)" as "(2)(b)(iii)"; either way the date is not in the text). A trust created on or after the date answers JUST FALSE whatever its value, the date being read like a period the text fixes in its own words (iv; assumed, not ruled). A trust over the value limit and created before the date answers NOTHING (an amount: S3A-F2). | PLAN.md section 5.5 (line 198) records the same: "a date the rendering does not give; mlr5 takes it as an input DATE". Line 3108: "was created before the date on which regulation 42(2)(iii) of these Regulations comes into force". |
| S3A-F4 | 3088, 3121, 3125, 3129, 3135 | "Less than two years has passed since that person's death": what is the end of the period for a death on 29 February? | (i) 28 February two years on; (ii) 1 March two years on | (ii), because `Date 29 2 2026` is 1 March 2026 in daydate, and the function is tested on both sides of its end. | The text counts in years and names no rule for 29 February. The Interpretation Act module is not staged (see Dependencies). |
| S3A-F5 | 3098 | Paragraph 4(2)(a) ends "where that policy was applied for at the same time as a policy under sub-paragraph (1)". Does the "where" clause qualify limb (b) too? | (i) it qualifies limb (a) alone; (ii) it qualifies both limbs | (i): a policy that pays out only for the cost of healthcare needs no such coincidence. | The clause stands inside limb (a), before the "; or" that opens limb (b) (lines 3098-3099). |
| S3A-F6 | 3165 | Paragraph 13 reads "points 2, 3, 6, 7 or 8 of ... Schedule 2": the rendering replaces the words before "Schedule 2" with an ellipsis and prints no point numbers in Schedule 2. | (i) compute the points from the core's `Listed activity`; (ii) one BOOLEAN fact the caller states | (ii). PLAN.md 5.3 reads the reference as Schedule 2 to these Regulations, whose items the core names without numbering them. | The core lists the thirteen items of Schedule 2 and numbers none (`Listed activity`, core line 235), so the points cannot be derived. |
| S3A-F7 | 3110-3114, 3144-3146, 3163, 3165-3167 | A term the Schedule defines with "means" sits inside a paragraph's head: "relevant account" (6A(1)), "segregating entity" (10(1)(c)), "relevant supervised person" (12 and 13). When the definition says no, does the paragraph answer JUST FALSE? | (i) yes, its no passes through the paragraph; (ii) no, the paragraph is one entry in a list that does not say "only": NOTHING | (i) for 6A(1), 12 and 13, where the defined term is a conjunct of the head, so its no is the paragraph's no. For 10(1)(c) only when the trust is (c)-shaped (a purpose of (c)(i) or (c)(ii) holds) and the entity is not a segregating entity, because limbs (a) and (b) are separate descriptions that the definition does not touch; when neither purpose holds the paragraph stays NOTHING. Assumed, not ruled. | Each definition is written with "means" (lines 3116, 3151, 3203), which is the text's own no for what falls outside it. |
| S3A-F8 | 3082-3205, with regulations 42 (line 1331), 45(10A) (line 1463) and 45ZA(2) (lines 1509-1510) | The combined function, which regulations 42, 45 and 45ZA use when they ask whether a trust "is not a trust listed in Schedule 3A": when does it answer JUST FALSE? | (i) only when every paragraph's function answers JUST FALSE; (ii) when no paragraph says JUST TRUE and no unknown answer could make one say so, reading the Schedule as the list to which the term is handed; (iii) NOTHING for a trust that fits no paragraph | (ii). Under (i) the combined answer would be NOTHING for nearly every trust, because every paragraph function answers NOTHING for a trust outside its head (only 7+1, which has no head, never does), and the paragraphs with no trigger of their own (1, 2, 3, 4(3), 5, 9B, 10(1)(a) and (b), 11, 16 to 16+6, 23, 23A(1) and the amount in 6(a)) answer NOTHING for every trust that does not fit them (S3A-F2); the combined function does not wait on those. The combined function answers JUST TRUE if any paragraph does; NOTHING if a paragraph would say JUST TRUE were an unknown answer (whether the creator, or a participant, is a relevant supervised person) to turn out yes; otherwise JUST FALSE. Flipping to (i) is a one-line change in `sch 3A the answers of the paragraphs, gathered`. Assumed, not ruled, that regulations 42, 45 and 45ZA hand "a trust listed in Schedule 3A" to the Schedule's list (the rulings of 2026-11-05 on a definition handed to a list). | The regulations use the Schedule's title, "Excluded Trusts", and say "listed in Schedule 3A (excluded trusts)"; the Schedule has no "only". |
| S3A-F9 | 3174 | Paragraph 15 reads "A trust created on the transfer or disposal of an asset where the purpose of the trust is to hold the legal title ... until the time when the procedure required by law ... is completed". Is "where" a condition (JUST FALSE when not met) or a description (NOTHING)? And is "until" a bar? | (i) a "where" condition; (ii) a description. And "until" as (a) the end of the stated purpose, (b) a bar on a thing | (i), and "until" is the end of the stated purpose, not a bar on a thing, so the "until" ruling does not apply and no yes/no bar question is added. Assumed, not ruled. | Line 3174: the word is "where", followed by the trust's purpose. |
| S4-F1 | 3207-3241 | Schedule 4 prints its items as bare paragraphs with no number. | (i) label by printed position; (ii) group by subject | (i): `sch 4 item 1` to `sch 4 item 21`, the label carrying no official number. | Counting the non-blank lines 3207-3241 with continuation lines joined to their item gives 21. |
| S4-F2 | 3207, 3209, 3210, 3225 | Items that begin "In the case of a self-regulatory organisation" (and the 3207 variant "or in the case of"): asked of an authority that is not one, are they JUST FALSE or NOTHING? | (i) a scope limit with no "where", "if" or "only": NOTHING; (ii) read as "where it is one": JUST FALSE | (i). "In the case of" is not on the ruling's list of trigger words ("where", "when", "upon", "whenever"; "once" and "in the event of" assumed). Assumed, not ruled. | The items say what is to be counted for a self-regulatory organisation and are silent about another authority. |
| S4-F3 | 3206-3241, with regulation 51(1) (line 1715) | How often is the Schedule 4 information collected or reported? | (i) silent: no function; (ii) a frequency from the regulation | (i). | Schedule 4 lists information to collect and says nothing of how often; regulation 51(1) says "must collect" with no period. |
| S5-F1 | 3243-3255 | Which legal forms of the subject are the "body corporate" of paragraph 1, the "partnership" of paragraph 2, the "unincorporated association" of paragraph 3, the "individual" of paragraph 4? Marginal (a) and (b). | A limited liability partnership: (A) paragraph 1; (B) paragraph 2. | (A). A company, a body corporate of another kind and a limited liability partnership are paragraph 1; a partnership other than a limited liability partnership is paragraph 2; an unincorporated association is paragraph 3; an individual is paragraph 4; a corporation sole, a trust, a foundation, an estate and any other legal arrangement are none of the four and answer JUST FALSE. | Regulation 3(1) (lines 26-32) says "body corporate" includes a body incorporated under the law of the United Kingdom or of another country and excludes a corporation sole and a partnership not regarded as a body corporate; it does not name a limited liability partnership. |
| S5-F2 | 2215, 3243-3255 | Regulation 65(3) says a person is connected "if that person is a person listed in Schedule 5". Is a person within no paragraph not connected (JUST FALSE) or not covered (NOTHING)? | (i) the definition is handed to the Schedule's list, so a person within no paragraph is not listed: JUST FALSE; (ii) a bare list: NOTHING | (i) for `sch 5 the person is a connected person of the relevant person`, which answers JUST TRUE if any paragraph does and otherwise JUST FALSE, whether the subject's form fits no paragraph or fits one and the person has none of its roles. Each of the four paragraph functions keeps NOTHING for a person with none of that paragraph's roles. Assumed, not ruled, that the "if" of regulation 65(3) is a hand-off. | Line 2215: "a person is connected to a relevant person or a payment service provider ("a connected person") if that person is a person listed in Schedule 5". |
| S6-F1 | 3262, 3268-3348 | The chapeau cites "paragraph 2", "paragraph 3", "paragraph 4" and "paragraphs 5 to 13", but the rendering prints 14 lists after it (lines 3268-3348) with no number. Counted by position they are paragraphs 2 to 15. | (i) number by position, so that printed lists 14 (regulations 66, 69(2), 70(7), 74A to 74C, 77 and 78) and 15 (regulation 84(1)) lie beyond "5 to 13"; (ii) take "5 to 13" to reach all of them (a reviewer reads the two printed lists after regulation 64H as paragraphs 12 and 13, so they are within the range) | (i), and a requirement in list 14 or 15 answers NOTHING under limb (b). Reviewer expected JUST TRUE for regulations 66, 74A and 84(1) (lines 3340, 3343, 3348); open question. | Lines 3262 and 3268-3348; whether the official text letters two of the lists cannot be told from the rendering. |
| S6-F2 | 3266 | Limb (c)(iii) reaches "regulations 18 to 21 or 24". Does "18 to 21" reach regulations 18A and 19A, which the rendering lists at lines 3293 and 3295? In particular, does the inserted regulation 19A fall inside "regulations 18 to 21"? | (i) yes; (ii) no; (iii) not said | (iii): regulation 18A or 19A imposed on an auction platform answers NOTHING. Reviewer expected JUST TRUE (it leans to (i): a lettered regulation inserted after 19 lies between 18 and 21); open question. | A range of numbers; lettered regulations are not named in it. |
| S6A-F1 | 3366-3371, 3374-3381, 3384-3385 | The rendering prints paragraph numbers 1, 2, 3, 4, 9, 13 and 16 only. | (i) derive the numbers from the Schedule's own cross-references; (ii) label by position | (i): paragraphs 5 to 8, 10 to 12, 14 and 15. | "subject to paragraph 10" (3365, 3368) is the paragraph beginning "Where an obligation arises" (3374); "subject to paragraph 11" and "under paragraph 7" (3370, 3375) fix the consent duty (3370) as 7 and the exception (3375) as 11; "Paragraphs 14 and 15" (3383) are the two after 13. |
| S6A-F2 | 3359 | "any authority other than the NCA concerned in the prevention ... and any supervisory authority, to which the NCA disseminates information": does "other than the NCA" qualify both kinds of authority? | (i) the first kind only; (ii) both | (i); "to which the NCA disseminates" qualifies both. | The sentence structure of line 3359. |
| S6A-F3 | 3383-3385 | Paragraph 13 says paragraphs 14 and 15 "apply where" the NCA wishes to obtain information about a relevant person with its head office in an EEA state other than the United Kingdom. Does paragraph 15 carry that limit? | (i) yes; (ii) paragraph 15 applies to every request to a foreign FIU | (i). | Paragraph 13 names both paragraphs. |
| S6A-F4 | 3361, 3365-3368, 3369, 3370 | "Promptly" (paragraphs 4, 5(b), 7) and "upon request" (paragraph 2) carry no number of days; paragraph 6 says "at least one point of contact" and gives no maximum. | (i) no WITHIN and no function that returns a time or a number; (ii) a number from memory | (i): the regulative rules have no WITHIN. A question that asks the paragraph 6 duty for a number is not answerable: the duty to designate "at least one" returns none. | The text states no period and no maximum; a deadline or a number is never invented. |
| S6A-F5 | 3361, 3365, 3366-3368, 3370-3371, 3373-3374, 3378-3381, 3383-3385, 3387-3390 | Which Schedule 6A sites are a "where" (or "upon request", "apply where"), so that an unmet condition answers JUST FALSE, and which are a scope limit (NOTHING)? | (i) a "where" / "upon" / "apply where" site is JUST FALSE when unmet; a scope with no such word is NOTHING; (ii) every site NOTHING | (i). JUST FALSE: paragraphs 2 ("Where ... upon request"), 5(a) and 5(b) (the lead-in "Where an external request is received ..."), 7 ("Where the NCA has provided ..."), 8, 10 ("Where an obligation arises ... where and to the extent"), 12(a) and 12(b) ("where making a decision under paragraph 10 / 11", read as a condition of the duty to have regard rather than a scope: assumed), 13 ("apply where"), 14 (through 13), 15, 16(a) to (c). NOTHING: paragraph 3 ("foreign FIUs"), paragraph 4 ("In response to an external request"), paragraph 9 ("provided in response to an external request"), and the exceptions "(subject to paragraph 10)" and "(subject to paragraph 11)" (paragraph 11 has its own function, which answers JUST FALSE when its "if and to the extent" holds). Assumed, not ruled, for each "where" that could be read as a scope. | The words of each paragraph at the lines given. |
| S6B-F1 | 3492, 3537, 3543 | Paragraph 5 defines "registered cryptoasset business" as a cryptoasset exchange provider on the register; the definitions inserted into section 191G (3492, 3537) say an exchange provider or a custodian wallet provider. Which governs paragraphs 1 and 3? | (i) paragraph 5; (ii) the 191G wording | (i): a custodian wallet provider is not within paragraphs 1 and 3, and is within the inserted 191G definition. | Paragraph 5 is the Schedule's own interpretation clause; the inserted definition is words of the host section. |
| S6B-F2 | 3392-3394, 3493-3495 | Which set of modifications applies is fixed by the date the business was included in the register (before 25 October 2027, or on or after it), not by the date of the asking; the text does not say when the Schedule itself comes into force. | (i) encode both sets and split on the registration date; (ii) encode one | (i). | Lines 3393 and 3494. |
| S6B-F3 | 3480, 3485, 3525, 3530 | The penalty for an offence under section 191F(4) in Scotland or Northern Ireland is "the statutory minimum" in paragraph 2 (3485) and "the statutory maximum" in paragraph 4 (3530). The rendering also reads "Scotland or Northern Ireland" (3480, 3530) and "Scotland and Northern Ireland" (3485, 3525). | (i) read each as printed; (ii) treat one as a misprint | (i): as printed, and the difference is a finding. | The rendering is not the official text, so a misprint cannot be told from a difference. |
| S6B-F4 | 3393, 3494, 3392-3394, 3493-3495 | Paragraphs 1 and 3 split at 25 October 2027: for a registered cryptoasset business included in the register on the wrong side of the date, JUST FALSE or NOTHING? And is a business that is not a registered cryptoasset business outside both? | (i) JUST FALSE, the date being read like a period the text fixes in its own words; (ii) NOTHING, a scope limit with no "only". And, for a business that is not a registered cryptoasset business: (a) pass paragraph 5's no through; (b) NOTHING | (i), whether or not Part 12 would otherwise apply (the date decides first); "to which Part 12 of FSMA would not otherwise apply" is a relative clause and stays NOTHING. (b): paragraph 5's no is not passed through, because it would make a custodian wallet provider answer JUST FALSE, a claim about Part 12 that S6B-F1 leaves open. The reviewer leans JUST FALSE for the date. Assumed, not ruled. There is no yes/no twin: `sch 6B paras 1 and 3 which set of modifications applies` returns a constructor, which cannot carry JUST FALSE, but the dates partition, so a registered cryptoasset business always meets one of paragraphs 1 and 3 and a twin could answer JUST FALSE only by passing paragraph 5's no through; the third constructor stays the not-covered answer. | Lines 3393 and 3494: "included in the register before 25th October 2027", "on or after 25th October 2027". |
| S6B-F5 | 3439 | Section 183(3)(b)(i) (line 3439) says 10% of the shares "in B", where section 181(1)(b)(i) (line 3405) says "the shares in B or P" and section 183(3)(b)(ii) (line 3440) says "the voting power in B or P". | (i) read as printed; (ii) treat "in B" as a misprint | (i): as printed, so the percentage of shares in a parent undertaking does not count under 183(3)(b)(i). A difference of the rendering's, not corrected. | Line 3439 against lines 3405 and 3440. |
| S7-F1 | 3686 | "unable to apply the customer due diligence measures required by regulation 28, and where relevant, those required by regulations 33, and 35 to 37": the stray comma after 33 is as printed. Is the agent "unable" if unable on regulation 28 or on the others where relevant, or on both? | (i) unable on regulation 28, or on the others where they are relevant; (ii) unable on both | (i). | The sentence reads "the measures required by regulation 28, and where relevant, those required by ...", a single set of required measures. |
| S7-F2 | 3556 | Section 226(7A): "The rules must provide ..." names no actor. | (i) no regulative rule; (ii) invent the rule-maker | (i): a decision function only. | The host section 226 of FSMA is not among the sources. |
| S7-F3 | 3706-3711 | Regulation 48(2) and (3) of the Open-Ended Investment Companies Regulations 2001 as amended (paragraph 18): what do the bearer-share prohibition and the void-provision limb answer for a company authorised before the relevant date, and for one within paragraph (3)? | (i) the prohibition answers NOTHING outside its scope and the void limb answers JUST FALSE; (ii) both NOTHING; (iii) both JUST FALSE | (i). The prohibition's yes/no is the permission "may issue bearer shares", whose grant is regulation 48(1), not among the sources, so a company authorised before the relevant date answers NOTHING and one within (3) answers NOTHING (paragraph (3) lifts (2) without saying what then follows). The void limb answers "does (2) void it": JUST FALSE for a company authorised before the relevant date (a date the text fixes in its own words, read like a period: assumed) and for one within (3) ("Paragraph (2) does not apply"), and NOTHING when no provision purports to authorise bearer shares. The relevant date is the core's constant `reg 1(2) the date these Regulations came into force`. | Lines 3708-3711: "authorised on or after the relevant date"; "Paragraph (2) does not apply to an open-ended investment company if ...". |
| MLR5-F1 | all of 3055-3808 | The rulings of 2026-11-05 name the shapes (a period, a "where", a definition handed to a list, a defence, an "until" bar), not the sites. Every site in this part that applies one of them to a case the ruling did not name is recorded here. | (i) apply the ruling at each site and record it; (ii) leave NOTHING and ask | (i). The sites: S3A-F3 (the date in 6(b) read like a period); S3A-F7 (a definition's no passes through the paragraph); S3A-F8 (the combined function reads regulations 42, 45 and 45ZA as handing the term to the list); S3A-F9 (the "where" of paragraph 15); S5-F2 (regulation 65(3) as a hand-off); S6A-F5 (each "where" that might be a scope, above all 12(a) and 12(b)); S6B-F4 (the date split of paragraphs 1 and 3); S7-F3 (the void limb of paragraph 18); S4-F2 ("In the case of" kept as a scope). "Once" and "in the event of" are assumed to count as "where", and no site in this range uses either. No yes/no twin was needed: the one function that returns a constructor and could have carried JUST FALSE is in S6B-F4. | The rulings, word for word, above. |

### Choices that were not forks of the text

- The seat layer asks "yes / no / I am not sure" for a fact a person may not know (`mlr5 my answer`), and "I am not sure" becomes NOTHING.
  It never becomes no.
- Beneficial owner (SEAM S-K2, asking) is a `MAYBE BOOLEAN` input of the Schedule 6B rules; the two sources of the answer are regulations 5 and 6 of another part.
- A trace of a regulative rule is run, not asserted (see "What the main binary does not accept").


## Jural relations (mlr5)

The kinds are Hohfeld's: a claim (right) pairs with a duty; a liberty (privilege) pairs with a no-right; a power pairs with a liability; an immunity pairs with a disability.
One row per provision that creates a relation, each relation stated once; a provision that creates none is listed once as `none`.
"Not named" means the text does not name the party; none is invented.
The rule column gives the L4 rule; for a regulative rule the decision function it calls is named in the coverage table.

| provision | lines | holder | correlative bearer | rule |
| --- | --- | --- | --- | --- |
| Schedule 3ZA | 3055-3081 | none (shown blank in the text) | | none |
| Schedule 3A, paragraphs 1 to 24 | 3082-3205 | none: each paragraph (and 23A(2), "does not apply") defines a class of trust; the relations are those of regulations 42, 45 and 45ZA, another part's | | `sch 3A the trust is a trust listed in Schedule 3A` |
| Schedule 4, items 1 to 21 | 3206-3241 | none: a list of the information to collect; the duty to collect and the Treasury's request are regulation 51 (lines 1715-1716), another part's | | `sch 4 the items` |
| Schedule 5, paragraphs 1 to 4 | 3242-3255 | none: a definition of the persons in relation to whom regulation 65(3) and 66 operate | | `sch 5 the person is a connected person of the relevant person` |
| Schedule 6 | 3256-3348 | none: a definition of the class "relevant requirement"; the relations are regulations 76 and 86 (lines 2453-2454, 2643-2644), another part's | | `sch 6 the provision is a relevant requirement` |
| Schedule 6A, paragraph 1 | 3350-3359 | none (definitions) | | the `sch 6A para 1` definitions |
| Schedule 6A, paragraph 2 | 3360-3361 | claim: the NCA | duty: a United Kingdom competent authority, to report on request | `sch 6A para 2 the report duty` |
| Schedule 6A, paragraph 3 | 3362-3363 | claim: foreign FIUs (named as those the NCA co-operates with; the text does not say they can enforce it) | duty: the NCA | `sch 6A para 3 the co-operation duty` |
| Schedule 6A, paragraph 4 | 3364-3365 | claim: the foreign FIU that made the external request | duty: the NCA, to provide relevant information promptly | `sch 6A para 4 the duty to provide information` |
| Schedule 6A, paragraph 5(a) | 3366-3367 | power: the NCA, to seek an order for information | liability: the relevant person suspected of holding it | `sch 6A para 5(a) the power to seek an order` |
| Schedule 6A, paragraph 5(b) | 3368 | claim: the foreign FIU | duty: the NCA, to pass on promptly what an order yields | `sch 6A para 5(b) the duty to pass on the information received` |
| Schedule 6A, paragraph 6 | 3369 | claim: not named | duty: the NCA, to designate a point of contact | `sch 6A para 6 the duty to designate a point of contact` |
| Schedule 6A, paragraph 7 | 3370 | claim: the foreign FIU that asks for consent | duty: the NCA, to consent as far as possible (subject to paragraph 11) | `sch 6A para 7 the duty to consent to dissemination` |
| Schedule 6A, paragraph 8 | 3371 | claim: not named | duty: the NCA, to take steps to ensure secure transmission | `sch 6A para 8 the duty to transmit securely` |
| Schedule 6A, paragraph 9 | 3372-3373 | power: the NCA, to impose restrictions and conditions on use | liability: the foreign FIU that receives the information | `sch 6A para 9 the power to impose restrictions and conditions` |
| Schedule 6A, paragraph 10 | 3374 | liberty: the NCA, not to provide where doing so could be contrary to national law | no-right: the foreign FIU, to the withheld information | `sch 6A para 10 the power to decide not to provide information` |
| Schedule 6A, paragraph 11 | 3375-3377 | liberty: the NCA, from the consent duty of paragraph 7 where it considers consent could prejudice an investigation or be contrary to national law | no-right: the foreign FIU | `sch 6A para 11 the NCA is required to give the consent under paragraph 7` (a decision function only) |
| Schedule 6A, paragraph 12 | 3378-3381 | claim: not named | duty: the NCA, to have particular regard | `sch 6A para 12(a) the duty to have regard to the exchange of information`; `sch 6A para 12(b) the duty to have regard to dissemination` |
| Schedule 6A, paragraph 13 | 3382-3383 | none: it says when paragraphs 14 and 15 apply | | `sch 6A para 13 paragraphs 14 and 15 apply` |
| Schedule 6A, paragraph 14 | 3384 | claim: not named | duty: the NCA, to address the request to the foreign FIU of the state of the head office | `sch 6A para 14 the duty to address the request to the foreign FIU` |
| Schedule 6A, paragraph 15 | 3385 | claim: not named | duty: the NCA, as to what the request must contain | `sch 6A para 15 the duty on the content of the request` |
| Schedule 6A, paragraph 16(a) to (c) | 3386-3390 | claim: the foreign FIU | duty: the NCA, to use for the stated purpose, to comply with its conditions, to obtain its consent to further dissemination | `sch 6A para 16(a) the duty to use the information only for its purpose`; `(b) the duty to comply with the foreign FIU's restrictions`; `(c) the duty to obtain consent to further dissemination` |
| Schedule 6B, paragraphs 1 and 3 | 3392-3394, 3493-3495 | none: a rule of application of Part 12 of FSMA, whose own relations are not among the sources | | `sch 6B paras 1 and 3 which set of modifications applies` |
| Schedule 6B, paragraph 2(a) to (c), (g) to (q), (s), (t); paragraph 4(a) to (p) | 3395-3397, 3442-3460, 3469-3472, 3496-3517 | none: each limb disregards or rewords a section of Part 12; the relation is the section's, not among the sources | | `sch 6B paras 2 and 4 how the applicable set treats a section of Part 12 of FSMA` |
| Schedule 6B, paragraph 2(d) to (f) | 3398-3441 | none: they set out when a person acquires, increases, reduces or ceases to have control | | `sch 6B para 2(d) section 181 ...`, `(e) section 182 ...`, `(f) section 183(1) ...`, `(f) section 183(3) ...` |
| Schedule 6B, paragraph 2(i) | 3446-3448 | none: it states a matter for assessment; the relation is section 185, not among the sources | | `sch 6B para 2(i) section 186 the section 178 notice-giver is a fit and proper person within the meaning of regulation 58A` |
| Schedule 6B, paragraph 2(r) | 3461-3468 | power: the FCA, to direct in a restriction notice that no influence is exercisable | liability: the person | `sch 6B para 2(r) section 191B(3ZA) the FCA may direct that no influence over the management or activities of the business is to be exercisable by the person` |
| Schedule 6B, paragraphs 2(u)(iii) and 4(q)(iii) | 3476-3486, 3521-3531 | power: the court, to impose the penalty | liability: the person guilty of an offence under section 191F | `sch 6B para 2(u)(iii) the penalty for the offence`; `sch 6B para 4(q)(iii) the penalty for the offence` |
| Schedule 6B, paragraphs 2(u)(iv) and 4(q)(iv) | 3487-3488, 3532-3533 | immunity: the person who took all reasonable steps and exercised all due diligence | disability: the court (or prosecutor), to convict | `sch 6B para 2(u)(iv) section 191F(10) ...`; `sch 6B para 4(q)(iv) section 191F(10) ...` |
| Schedule 6B, paragraphs 2(u)(i), (ii), (v), 4(q)(i), (ii), (r), 5 | 3473-3475, 3489-3492, 3518-3520, 3534-3543 | none (omissions and definitions) | | `sch 6B para 5 the business is a registered cryptoasset business` and the definitions |
| Schedule 7, paragraph 3(2) | 3555-3564 | claim: a person identified by a respondent as a politically exposed person, a family member or a known close associate, to be eligible to complain | duty: the maker of the rules (not named in the inserted words; section 226 is not among the sources) | `sch 7 para 3(2) s 226(7A) the rules must provide that the person is eligible in relation to the complaint` |
| Schedule 7, paragraph 12 | 3682-3686 | liberty: the estate agent, from paragraph 2 of Schedule 3 to the 1991 Order when unable to apply customer due diligence | no-right: the person to whom paragraph 2 is owed (not named; the Order is not among the sources) | `sch 7 para 12 paragraph 2 of Schedule 3 to the Estate Agents (Undesirable Practices) (No 2) Order 1991 applies` |
| Schedule 7, paragraph 18(c), regulation 48(2), first limb | 3708 | claim: not named | duty: an open-ended investment company authorised on or after the relevant date, not to issue bearer shares (a prohibition, derived from the no: ruling N2) | `sch 7 para 18(c) paragraph (2) the prohibition on issuing bearer shares` |
| Schedule 7, paragraph 18(c), regulation 48(2), second limb | 3708 | immunity: not named | disability: the company, whose instrument of incorporation cannot authorise bearer shares | `sch 7 para 18(c) paragraph (2) the provision in the instrument of incorporation is void` |
| Schedule 7, paragraph 18(c), regulation 48(3) | 3709-3711 | liberty: a company whose application was made before the relevant date and determined on or after it, from paragraph (2) | no-right: not named | `sch 7 para 18(c) paragraph (3) the application was made before and determined on or after the relevant date` |
| Schedule 7, every other line (the amending words of paragraphs 3, 12 and 18, and the other paragraphs but the blank paragraph 27) | 3546-3554, 3565-3681, 3687-3702, 3712-3794 | none: amendments of other Acts and instruments (inert, reason 2) | | none |
| Explanatory note | 3795-3808 | none (not operative) | | none |


## Marginal readings for a lawyer (mlr5)

The rule of 2026-10-29 is assumed, not ruled by a lawyer.
This part takes the two readings below as the status quo and lists every branch that rests on one.
The other reading is stated for each.

**(a) A failed "if" counts as the text's no, clause by clause, and a flat negative counts as the text saying no.**
The other reading: "if A then B" does not itself say "if not A then not B", so a failed "if" answers NOTHING; and a flat negative ("does not apply", "may not", "is not required") limits the case it names and says nothing of any other.
For flat negatives, ruling N2 (2026-11-04) settles the matter for this corpus: a flat negative is the text's no.
The "if" and "unless" branches remain for a lawyer.
Meng's rulings of 2026-11-05 settle the other shapes that used to sit under this reading: a "where" or "upon request" that is not met, a period the text fixes in its own words, a paragraph closed by "only", and a definition handed to a list.
Their branches are labelled "(ruled 2026-11-05)" in the first table and are no longer marginal.

**(b) A prohibition, grant or description limited by its own wording does not give a no outside the limit.**
The other reading: a grant or description that is limited is, outside the limit, a no (the text gave this much and no more).
This part answers NOTHING outside the limit.

Also marginal, in the register above: S5-F1 (a limited liability partnership is placed with the body corporate of paragraph 1, not with the partnership of paragraph 2; the other reading puts it in paragraph 2).

#### Reading (a), and the rulings of 2026-11-05: branches that answer `JUST FALSE` because an "if" failed, an "unless" did not hold, a flat negative applied, a "where" or a period was not met, or a definition handed to a list had no head that held

| module | line | function | what the no rests on | the words |
| --- | --- | --- | --- | --- |
| mlr5-sch3a | 102 | `sch 3A para 1+1 the trust is a trust which ceases to be an excluded trust under paragraph 1 within two years of a trustee's death` | failed where (ruled 2026-11-05) | "A trust which ceases to be an excluded trust under paragraph 1 of this Schedule where— (a) the trust had been an excluded trust by virtue of section 34 of the Trustee Act 1925; (b) the sole reason for paragraph 1 ceasing to apply |
| mlr5-sch3a | 155 | `sch 3A para 4(1) the trust is a trust of a life policy paying out only on the listed events or for healthcare` | closed by "only" (ruled 2026-11-05) | "A trust of a life policy paying out only— (a) on the death, terminal or critical illness, or permanent or temporary disablement of the person assured; or (b) to meet the cost of healthcare services provided to the person assured" |
| mlr5-sch3a | 179 | `sch 3A para 4(2) the trust is a trust of an insurance policy paying out only on temporary disablement or for healthcare` | closed by "only" (ruled 2026-11-05) | "A trust of an insurance policy paying out only— (a) on the temporary disablement of the person assured, where that policy was applied for at the same time as a policy under sub-paragraph (1); or (b) to meet the cost of healthcare |
| mlr5-sch3a | 236 | `sch 3A para 6 the trust is a pilot trust` | period (ruled 2026-11-05) | "(b) was created before the date on which regulation 42(2)(iii) of these Regulations comes into force" is a date the text fixes in its own words, read like a period (assumed, not ruled: FORK S3A-F3) |
| mlr5-sch3a | 322 | `sch 3A para 7(1) the trust is a trust effected by will holding only the estate within two years of the death` | failed where (ruled 2026-11-05) | "A trust effected by will where— (a) the trust is holding only the property comprised in a person's estate on death, and (b) less than two years has passed since that person's death" |
| mlr5-sch3a | 349 | `sch 3A para 7+1 the trust holds only death benefits of a policy within paragraph 4 within two years of the death` | failed where (ruled 2026-11-05) | "A trust where— (a) the trust is holding only benefits received on the death of the person assured under a policy within paragraph 4, and (b) less than two years has passed since that person's death" |
| mlr5-sch3a | 375 | `sch 3A para 7+2 the trust is created under a deed or instrument varying dispositions of an estate within two years of the death` | failed where (ruled 2026-11-05) | "A trust created under a deed or instrument which ... where less than two years has passed since P's death" |
| mlr5-sch3a | 398 | `sch 3A para 9 the trust is a co-ownership trust` | failed where (ruled 2026-11-05) | "A trust of jointly held property where the trustees and the beneficiaries are the same persons" |
| mlr5-sch3a | 420 | `sch 3A para 9+1 the trust is a trust which ceases to be an excluded trust under paragraph 9 within two years of a trustee's death` | failed where (ruled 2026-11-05) | "A trust which ceases to be an excluded trust under paragraph 9 of this Schedule where— (a) the sole reason for paragraph 9 ceasing to apply is the death of one of the trustees, and (b) less than two years have passed since that p |
| mlr5-sch3a | 586 | `sch 3A para 12 the trust is a client money trust` | failed where (ruled 2026-11-05) | "where that trust is incidental to the carrying on of business by the relevant supervised person" |
| mlr5-sch3a | 611 | `sch 3A para 13 the trust is a capital markets trust` | failed where (ruled 2026-11-05) | "where— (a) one or more of the participants in that activity is a relevant supervised person, and (b) the use of the trust is incidental to the principal purpose of that activity" |
| mlr5-sch3a | 634 | `sch 3A para 14 the trust is a commercial transactions trust` | failed where (ruled 2026-11-05) | "A trust created for the purpose of— (a) enabling or facilitating a transaction effected for genuine commercial reasons; or (b) protecting or enforcing rights relating to such a transaction, where the use of the trust is incidenta |
| mlr5-sch3a | 651 | `sch 3A para 15 the trust is a registration of assets trust` | failed where (ruled 2026-11-05) | "A trust created on the transfer or disposal of an asset where the purpose of the trust is to hold the legal title to the asset on trust for the person to whom the transfer or disposal is being made until the time when the procedu |
| mlr5-sch3a | 803 | `sch 3A para 23A the trust is within the general exclusion` | flat negative | "This paragraph does not apply to a trust which is a UK trust which is an express trust where (a) the settlor has, during his or her lifetime, created one or more other UK trusts which are express trusts, and (b) one of the trusts |
| mlr5-sch3a | 977 | `sch 3A the answers of the paragraphs, gathered` | definition handed to a list (ruled 2026-11-05) | the term "a trust listed in Schedule 3A (excluded trusts)" is read as handed to the Schedule's list of paragraphs (Meng's ruling of 2026-11-05 on a definition handed to a list; assumed to apply here, FORK S3A-F8), and no paragraph |
| mlr5-sch5 | 110 | `sch 5 para 1 the person is a connected person of the body corporate` | failed if | "If the relevant person or payment service provider is a body corporate" fails; Marginal readings, (a) |
| mlr5-sch5 | 130 | `sch 5 para 2 the person is a connected person of the partnership` | failed if | "If the relevant person or payment service provider is a partnership" fails; Marginal readings, (a) |
| mlr5-sch5 | 147 | `sch 5 para 3 the person is a connected person of the unincorporated association` | failed if | "If the relevant person or payment service provider is an unincorporated association of persons which is not a partnership" fails; Marginal readings, (a) |
| mlr5-sch5 | 165 | `sch 5 para 4 the person is a connected person of the individual` | failed if | "If the relevant person or payment service provider is an individual" fails; Marginal readings, (a) |
| mlr5-sch5 | 198 | `sch 5 the person is a connected person of the relevant person` | definition handed to a list (ruled 2026-11-05) | regulation 65(3), "a person is connected ... if that person is a person listed in Schedule 5", hands the definition to the Schedule's list, and the person is within no paragraph; Meng's ruling of 2026-11-05 on a definition handed  |
| mlr5-sch6a | 164 | `sch 6A para 2 the authority must provide a report to the NCA` | failed where (ruled 2026-11-05) | "Where the NCA has, in its performance of FIU functions, disseminated any information to a United Kingdom competent authority, that authority must, upon request, provide a report to the NCA" is not met |
| mlr5-sch6a | 237 | `sch 6A para 5(a) the NCA may exercise its powers to seek an order for information from the relevant person` | failed where (ruled 2026-11-05) | "Where an external request is received and the NCA does not possess information which the NCA considers relevant to the external request, and it suspects a relevant person possesses such information" is not met |
| mlr5-sch6a | 262 | `sch 6A para 5(b) the NCA must provide to the foreign FIU the relevant information received in consequence of an order` | failed where (ruled 2026-11-05) | "Where an external request is received and the NCA does not possess information which the NCA considers relevant to the external request, and it suspects a relevant person possesses such information" is not met |
| mlr5-sch6a | 305 | `sch 6A para 7 the NCA must consent to the dissemination of the requested information` | failed where (ruled 2026-11-05) | "Where the NCA has provided relevant information to a foreign FIU, and that foreign FIU makes a request for consent to disseminate some or all of the relevant information to a foreign competent authority" is not met |
| mlr5-sch6a | 329 | `sch 6A para 8 the NCA shall take such steps as it considers appropriate to ensure the information is transmitted securely` | failed where (ruled 2026-11-05) | "Where the NCA provides relevant information in response to an external request in accordance with this Schedule" is not met |
| mlr5-sch6a | 372 | `sch 6A para 10 the NCA may decide not to provide some or all of the information` | failed where (ruled 2026-11-05) | "Where an obligation arises under this Schedule for the NCA to provide relevant information in response to an external request, the NCA may decide not to provide some or all of the information where and to the extent that the NCA  |
| mlr5-sch6a | 397 | `sch 6A para 11 the NCA is required to give the consent under paragraph 7` | flat negative | "The NCA is not required to comply with the duty to give consent to the dissemination of information to a foreign competent authority under paragraph 7 if and to the extent that the NCA considers that the giving of such consent co |
| mlr5-sch6a | 412 | `sch 6A para 12(a) the NCA must have particular regard to the need for as unfettered an exchange of relevant information as possible` | failed where (ruled 2026-11-05) | "(a) where making a decision under paragraph 10, to the need for as unfettered an exchange of relevant information in response to external requests as possible" is not met |
| mlr5-sch6a | 430 | `sch 6A para 12(b) the NCA must have particular regard to the need for as unfettered dissemination of information by the foreign FIU as possible` | failed where (ruled 2026-11-05) | "(b) where making a decision under paragraph 11, to the need for as unfettered dissemination of information as possible by a foreign FIU to foreign competent authorities" is not met |
| mlr5-sch6a | 452 | `sch 6A para 13 paragraphs 14 and 15 apply` | failed where (ruled 2026-11-05) | "Paragraphs 14 and 15 apply where the NCA wishes to obtain information concerning a relevant person which has its head office in an EEA state other than the United Kingdom" is not met |
| mlr5-sch6a | 464 | `sch 6A para 14 the NCA must address the request to the foreign FIU in the state of the head office` | failed where (ruled 2026-11-05) | "Paragraphs 14 and 15 apply where the NCA wishes to obtain information concerning a relevant person which has its head office in an EEA state other than the United Kingdom (paragraph 13)" is not met |
| mlr5-sch6a | 489 | `sch 6A para 15 the request must contain the relevant facts, the reasons and the proposed use` | failed where (ruled 2026-11-05) | "Where the NCA makes a request to a foreign FIU for information which the NCA considers may be relevant for its performance of FIU functions, and paragraph 13: Paragraphs 14 and 15 apply where the NCA wishes to obtain information  |
| mlr5-sch6a | 516 | `sch 6A para 16(a) the NCA must use the information only for the purpose for which it was sought or provided` | unless | "use the information only for the purpose for which it was sought or provided, unless it has obtained the prior consent of the foreign FIU to any other use of the information" |
| mlr5-sch6a | 519 | `sch 6A para 16(a) the NCA must use the information only for the purpose for which it was sought or provided` | failed where (ruled 2026-11-05) | "Where the NCA receives information from a foreign FIU" is not met |
| mlr5-sch6a | 538 | `sch 6A para 16(b) the NCA must comply with the restrictions or conditions of use imposed by the foreign FIU` | failed where (ruled 2026-11-05) | "Where the NCA receives information from a foreign FIU" is not met |
| mlr5-sch6a | 556 | `sch 6A para 16(c) the NCA must obtain the prior consent of the foreign FIU to any further dissemination` | failed where (ruled 2026-11-05) | "Where the NCA receives information from a foreign FIU" is not met |
| mlr5-sch6b | 112 | `sch 6B at least one of the two answers is yes` | failed where (ruled 2026-11-05) | both operands are the text's own no, each carrying its own quoted words where it is answered |
| mlr5-sch6b | 135 | `sch 6B para 1 Part 12 of FSMA applies to the business with the modifications specified in paragraph 2` | period (ruled 2026-11-05) | "included in the register before 25th October 2027" is a date the text fixes in its own words, read like a period, so a business included on or after that day is outside it (assumed, not ruled: FORK S6B-F4) |
| mlr5-sch6b | 233 | `sch 6B para 2(d) section 181 the person acquires control over the business` | failed if | "a person (“A”) acquires control over a registered cryptoasset business (“B”) if, should the acquisition proceed—" and neither limb (a) nor limb (b) is met (marginal reading (a)) |
| mlr5-sch6b | 296 | `sch 6B para 2(e) section 182 the person increases control over the business` | failed if | "a person (“A”) increases control over a registered cryptoasset business (“B”) if, should the increase in control proceed—" and neither limb (a) nor limb (b) is met (marginal reading (a)) |
| mlr5-sch6b | 365 | `sch 6B para 2(f) section 183(1) the person reduces control over the business` | failed if | "a person (“A”) reduces control over a registered cryptoasset business (“B”) if, should the decrease in control proceed—" and neither limb (a) nor limb (b) is met (marginal reading (a)) |
| mlr5-sch6b | 396 | `sch 6B para 2(f) section 183(3) the person ceases to have control over the business` | failed if | "For the purposes of this Part, A ceases to have control over B if—" and neither limb (a) nor limb (b) is met (marginal reading (a)) |
| mlr5-sch6b | 620 | `sch 6B para 2(u)(iv) section 191F(10) the person is not guilty because the person took all reasonable steps and exercised all due diligence` | flat negative | "A person is not guilty of an offence under this section if that person took all reasonable steps and exercised all due diligence to avoid committing the offence." (marginal reading (a): a failed "if" is the text's no for this def |
| mlr5-sch6b | 666 | `sch 6B para 3 Part 12 of FSMA applies to the business with the modifications specified in paragraph 4` | period (ruled 2026-11-05) | "included in the register on or after 25th October 2027" is a date the text fixes in its own words, read like a period, so a business included before that day is outside it (assumed, not ruled: FORK S6B-F4) |
| mlr5-sch6b | 889 | `sch 6B para 4(q)(iv) section 191F(10) the person is not guilty because the person took all reasonable steps and exercised all due diligence` | flat negative | "A person is not guilty of an offence under this section if that person took all reasonable steps and exercised all due diligence to avoid committing the offence." (marginal reading (a): a failed "if" is the text's no for this def |
| mlr5-sch7 | 64 | `sch 7 para 3(2) s 226(7B) the person is within the subsection` | failed if | "A person is within this subsection if he or she has been identified by a respondent, in carrying on an activity to which the rules apply, as— (a) a politically exposed person; (b) a family member of a politically exposed person;  |
| mlr5-sch7 | 119 | `sch 7 para 12 paragraph 2 of Schedule 3 to the Estate Agents (Undesirable Practices) (No 2) Order 1991 applies` | flat negative | "Paragraph 2 does not apply if the estate agent does not forward accurate details of the offer because the estate agent is unable to apply the customer due diligence measures required by regulation 28, and where relevant, those re |
| mlr5-sch7 | 159 | `sch 7 para 18(c) paragraph (2) the open-ended investment company may issue bearer shares under paragraph (1)` | flat negative | "An open-ended investment company authorised on or after the relevant date may not issue any bearer shares under paragraph (1)" |
| mlr5-sch7 | 189 | `sch 7 para 18(c) paragraph (2) the provision in the instrument of incorporation is void` | period (ruled 2026-11-05) | "authorised on or after the relevant date" is a date the text fixes in its own words, read like a period, so a company authorised before it is outside paragraph (2) and its provision is not voided by it (assumed, not ruled: FORK S |
| mlr5-sch7 | 192 | `sch 7 para 18(c) paragraph (2) the provision in the instrument of incorporation is void` | flat negative | "Paragraph (2) does not apply to an open-ended investment company if— (a) an application for an authorisation order was made ... before the relevant date; and (b) that application was not determined until a date on or after the re |

The other 25 `JUST FALSE` branches rest on a definition that says "means" and are not marginal: mlr5-sch3a:268; mlr5-sch3a:287; mlr5-sch3a:299; mlr5-sch3a:333; mlr5-sch3a:471; mlr5-sch3a:500; mlr5-sch3a:582; mlr5-sch3a:844; mlr5-sch6:349; mlr5-sch6:373; mlr5-sch6:386; mlr5-sch6:390; mlr5-sch6:415; mlr5-sch6:435; mlr5-sch6:450; mlr5-sch6:472; mlr5-sch6a:76; mlr5-sch6a:96; mlr5-sch6a:108; mlr5-sch6a:120; mlr5-sch6a:150; mlr5-sch6b:644; mlr5-sch6b:912; mlr5-sch6b:924; mlr5-sch6b:952.

#### Reading (b): branches that answer `NOTHING` (or a named "not covered") because a grant, prohibition or description is limited by its own wording

| module | line | function | why the case falls outside the limit |
| --- | --- | --- | --- |
| mlr5-sch4 | 82 | `sch 4 item 1 the person is a supervised person` | "supervised persons" labels the persons the item counts; the text does not say that another person is not a supervised person |
| mlr5-sch4 | 421 | `sch 4 the item is asked of the supervisory authority` | an item that begins "In the case of a self-regulatory organisation" says nothing of another authority; and the Schedule has no item at a position outside 1 to 21 |
| mlr5-sch6a | 187 | `sch 6A para 3 the NCA must take such steps as it considers appropriate to co-operate with the foreign FIU` | the paragraph states when the duty arises and does not say that it does not arise in another case |
| mlr5-sch6a | 210 | `sch 6A para 4 the NCA must provide promptly any relevant information in its possession` | the paragraph states when the duty arises and does not say that it does not arise in another case |
| mlr5-sch6a | 263 | `sch 6A para 5(b) the NCA must provide to the foreign FIU the relevant information received in consequence of an order` | the paragraph states when the duty arises and does not say that it does not arise in another case |
| mlr5-sch6a | 306 | `sch 6A para 7 the NCA must consent to the dissemination of the requested information` | the paragraph states when the duty arises and does not say that it does not arise in another case |
| mlr5-sch6a | 350 | `sch 6A para 9 the NCA may impose restrictions and conditions on the use of the information` | the paragraph states when the permission arises and does not say that it does not arise in another case |
| mlr5-sch6a | 398 | `sch 6A para 11 the NCA is required to give the consent under paragraph 7` | the paragraph removes the duty in the two cases it names; whether the duty arises in another case is paragraph 7 |
| mlr5-sch6b | 136 | `sch 6B para 1 Part 12 of FSMA applies to the business with the modifications specified in paragraph 2` | the paragraph applies Part 12 to a registered cryptoasset business included in the register before 25th October 2027 and to which Part 12 would not otherwise apply; "to which Part 12 of FSMA would not otherwise apply" is a relativ |
| mlr5-sch6b | 440 | `sch 6B para 2(i) section 186 the section 178 notice-giver is a fit and proper person within the meaning of regulation 58A` | the limb substitutes section 186 "in relation to a section 178 notice-giver who falls within section 181(a) or 182(1)(a)" and says nothing of any other notice-giver |
| mlr5-sch6b | 543 | `sch 6B para 2(r) section 191B(3ZA) the FCA may direct that no influence over the management or activities of the business is to be exercisable by the person` | the power is "in a restriction notice" and "in respect of a beneficial owner of B or P"; the text does not say the FCA may not give such a direction in another case |
| mlr5-sch6b | 667 | `sch 6B para 3 Part 12 of FSMA applies to the business with the modifications specified in paragraph 4` | the paragraph applies Part 12 to a registered cryptoasset business included in the register on or after 25th October 2027 and to which Part 12 would not otherwise apply; "to which Part 12 of FSMA would not otherwise apply" is a re |
| mlr5-sch6b | 972 | `sch 6B paras 1 and 3 which set of modifications applies` | paragraphs 1 and 3 apply Part 12 to one kind of business and are silent about every other |
| mlr5-sch6b | 996 | `sch 6B paras 2 and 4 how the applicable set treats a section of Part 12 of FSMA` | neither paragraph 1 nor paragraph 3 applies Part 12 to the business, so there is no set of modifications to read |
| mlr5-sch7 | 87 | `sch 7 para 3(2) s 226(7A) the rules must provide that the person is eligible in relation to the complaint` | the subsection names a person within (7B) and a complaint to which (7C) applies; whether anyone else is eligible is for the rest of section 226, which is not among the sources |
| mlr5-sch7 | 193 | `sch 7 para 18(c) paragraph (2) the provision in the instrument of incorporation is void` | the paragraph voids a provision in the instrument "purporting to authorise" the issue of bearer shares, and says nothing where there is no such provision |

The reading-(b) list includes the Schedule 6A scopes that carry no "where": paragraphs 3, 4 and 9, and the exceptions "(subject to paragraph 10)" and "(subject to paragraph 11)" in paragraphs 4, 5(b) and 7.
Each of those decision functions answers JUST TRUE when its condition holds and NOTHING otherwise, because the paragraph states what the NCA must or may do in the case it describes and does not say what is so in any other case.
The other Schedule 6A decision functions answer JUST FALSE when their "where", "upon request" or "apply where" is not met (S6A-F5).


## Reading the answers (mlr5)

### Reading a result: FALSE and NOTHING (mlr5)

Every decision function in this part answers `JUST TRUE`, `JUST FALSE` or `NOTHING`, or a named constructor that says the same.

**A "no" (`JUST FALSE`) in this part is the text saying no in its own words, and nothing wider.**
It appears for a definition that says "means" (for example "relevant supervised person" in Schedule 3A paragraph 24, "external request" in Schedule 6A paragraph 1, "relevant requirement" in Schedule 6); for a condition the text introduces with "if" or "unless" (Schedule 5: "If the relevant person or payment service provider is a body corporate ..."; Schedule 6A paragraph 16(a): "unless it has obtained the prior consent"); and for a flat negative (Schedule 3A paragraph 23A(2), "This paragraph does not apply"; Schedule 6A paragraph 11, "is not required"; Schedule 7 paragraph 12, "does not apply if"; Schedule 7 paragraph 18, "may not issue").
By Meng's rulings of 2026-11-05 it also appears for a "where", "upon request" or "apply where" that is not met (Schedule 6A paragraph 2; Schedule 3A paragraph 9, "where the trustees and the beneficiaries are the same persons"); for a case outside a period the text fixes in its own words (Schedule 3A paragraph 7+1, "less than two years has passed"; Schedule 6B paragraph 1, "before 25th October 2027"); for a case outside a paragraph closed by "only" (Schedule 3A paragraph 4(1), "paying out only"); and for a definition the text hands to a list when no head holds (Schedule 5 through regulation 65(3), S5-F2; the Schedule 3A combined function, S3A-F8).
In this row a "no" never means that the law forbids; it means the text, on these facts, gives a negative answer to the question the function name asks.

**"Not covered" (`NOTHING`) is the answer wherever the text does not say no.**
The commonest case here is a list that is not closed: Schedule 3A lists kinds of excluded trust without saying "only", so a trust that fits none of the paragraphs is not said to be excluded and is not said not to be (the answer is NOTHING).
The next is a duty, a permission or a description limited by its own wording with no "where", "if", period or "only": Schedule 6A paragraph 4 says what the NCA must do "In response to an external request" and says nothing of any other case, so the decision function answers NOTHING there, never "the NCA must not"; the relative-clause paragraphs of Schedule 3A (S3A-F2) are the same.
Others: the text points outside the sources (Part 12 of FSMA itself, regulation 48(1) of the 2001 Regulations, paragraph 2 of Schedule 3 to the 1991 Order); a term is undefined (the roles in Schedule 5); or the text is silent (a requirement in no list of Schedule 6).

**What a caller must never do.**
A caller never turns `NOTHING` into `FALSE`, and the seat layer never turns "I am not sure" into no.
A Schedule 6 answer of NOTHING for regulation 26 as a whole means the Schedule lists only some of its paragraphs, not that regulation 26 imposes no relevant requirement.
A Schedule 3A paragraph's own NOTHING means the trust is outside that paragraph's description, which says nothing of other trusts, and never that the trust is taxable.
The combined Schedule 3A function answers NOTHING only when an answer not yet given (whether the creator of the trust, or a participant in the activity, is a relevant supervised person) could still make paragraph 12 or 13 apply; its JUST FALSE means that no paragraph says the trust is excluded and none could on the answers given, on the assumption of S3A-F8.

**Audit of the tags** (`work/audit.py`, not shipped): every branch that answers a no or a not-covered carries its tag with a reason from the allowed list.

```
sch3a {'NOTHING branches': 33, 'NOTHING: list not closed': 30, 'FALSE branches': 23, 'NOTHING: includes': 1, 'NOTHING: points outside the text': 2}
sch4 {'NOTHING branches': 2, 'NOTHING: limited by its own wording': 2}
sch5 {'FALSE branches': 5, 'NOTHING branches': 4, 'NOTHING: list not closed': 4}
sch6 {'NOTHING branches': 6, 'NOTHING: undefined term': 5, 'FALSE branches': 8, 'NOTHING: silent': 1}
sch6a {'FALSE branches': 21, 'NOTHING branches': 6, 'NOTHING: limited by its own wording': 6}
sch6b {'FALSE branches': 13, 'NOTHING branches': 9, 'NOTHING: undefined term': 1, 'NOTHING: limited by its own wording': 4, 'NOTHING: points outside the text': 4, 'tag on a line that is not a branch': 7}
sch7 {'FALSE branches': 5, 'NOTHING branches': 5, 'NOTHING: list not closed': 1, 'NOTHING: limited by its own wording': 2, 'NOTHING: points outside the text': 2}
TOTAL {'NOTHING branches': 65, 'NOTHING: list not closed': 35, 'FALSE branches': 75, 'NOTHING: includes': 1, 'NOTHING: points outside the text': 8, 'NOTHING: limited by its own wording': 14, 'NOTHING: undefined term': 6, 'NOTHING: silent': 1, 'tag on a line that is not a branch': 7}
problems: 0
```

In the totals, 75 branches are tagged `FALSE-kind`; 72 tags are `NOTHING-kind` (branches that answer NOTHING, and named "not covered" constructors): list not closed 35, limited by its own wording 16, points outside the text 8, undefined term 6, silent 6, includes 1.


## Seams (mlr5)

As PLAN.md section 5 names them.

| seam | direction | what this part did |
| --- | --- | --- |
| S-16 | answering | `sch 5 the person is a connected person of the relevant person`, a `MAYBE BOOLEAN`; the caller supplies the legal form (the core's `Form of customer`) and eight role facts; JUST TRUE if a paragraph says so, otherwise JUST FALSE (S5-F2). |
| S-17 | answering | `sch 6 the provision is a relevant requirement`, a `MAYBE BOOLEAN`; the caller supplies the instrument, the number, the paragraph and on whom the requirement is imposed. |
| S-18 | answering | `sch 3A the trust is a trust listed in Schedule 3A`, a `MAYBE BOOLEAN`, over a record of 94 facts about the trust; JUST TRUE if a paragraph says so, NOTHING if an unknown relevant-supervised-person answer could make paragraph 12 or 13 say so, otherwise JUST FALSE (S3A-F8). |
| S-K2 | asking | "beneficial owner within the meaning of regulation 5 or 6" in Schedule 6B sections 181 to 183 is a `MAYBE BOOLEAN` input of each rule. |
| S-K3 | asking | "supervisory authority" in Schedule 4 and Schedule 6A is a BOOLEAN fact (whether the authority is a self-regulatory organisation; whether a body is a supervisory authority), not a list of authorities. |
| S-K4 | asking | "officer" and "manager" (regulation 3(1) terms with no core type) in Schedule 5 are one BOOLEAN input each, and so are the other roles it names (employee, agent, member, and the parent-undertaking variants): eight in all. Regulation 3(1) defines "officer" "except in Part 8 and Schedule 5" (line 88), so the defined meaning is off inside the Schedule. |
| S-8 | asking | "relevant person" in Schedule 3A paragraph 24(a) is a `MAYBE BOOLEAN` input; in Schedule 5 whether the subject is a relevant person is left to the caller. |

**Seams found that the plan lacks (proposed, not landed; they need an answer from the part that owns each regulation):**

- **Regulation 58A, fit and proper person.** Schedule 6B paragraph 2(i) (line 3448) makes "fit and proper person within the meaning of regulation 58A" the matter specified in section 185(3)(a). This part takes it as a `MAYBE BOOLEAN` input (`sch 6B para 2(i) section 186 ...`).
- **Regulation 54(1A), the FCA register.** Schedule 6B paragraphs 1, 3 and 5 and the inserted section 191G definitions turn on being "included in the register maintained by the FCA under regulation 54(1A)". This part takes membership of the register, and the date of inclusion, as inputs.
- **Regulation 14A, cryptoasset exchange provider and custodian wallet provider.** Schedule 6B paragraph 5 points at regulation 14A(1) and (2) (lines 3541-3542). This part takes each as a BOOLEAN input.

The plan's note (section 5, "Where it will read the core") expected this part to read the core types `Kind of relevant person`, `Professional body` and `Authority`; this part reads `Form of customer`, `Part of the United Kingdom` and `reg 1(2) the date these Regulations came into force` and takes the others as BOOLEAN facts, because each use in this range is a yes-or-no fact about one body, not a choice from a list.

## Seat (mlr5)

The seat is a business that is a relevant person (a bank, an accountancy or legal firm, an estate agent, a money service business, a cryptoasset exchange provider) and its compliance officer.
There is no seat for an official: the NCA, the FCA, the Treasury and the ombudsman appear only as what their rules mean to the business.

`mlr5-seat.l4` has **67 questions**, each with `@export` and a `@desc` on every input, grouped under `§` headings in the text's order: Schedule 3A (38), Schedule 4 (4), Schedule 5 (1), Schedule 6 (1), Schedule 6A (3), Schedule 6B (16), Schedule 7 (4).
`mlr5-cases-seat.l4` has **199 cases**, each hand-written from the text, with at least one case outside the encoding that expects NOTHING.
Every question begins "Under schedule N paragraph M," except four that gather a whole Schedule ("Under schedule 3A,", "Under schedule 4,", "Under schedule 5,", "Under schedule 6,"): the Schedule number keeps the names unique across parts, and a paragraph number would say less than the question asks.
No question restates a rule; each calls a layer-1 function with its inputs bound by name.
The first question of the Schedule 3A group asks every paragraph at once, over the 94 facts of the layer-1 record, and calls the layer-1 gather `sch 3A the trust is a trust listed in Schedule 3A` (S3A-F8); a fact the trust does not turn on can be answered No, 0 or any date.
Every other question of the group asks one paragraph (option C of ruling E1).


## Findings (what the text turns out to say)

1. **Schedule 3ZA is blank.** The heading (line 3055) is followed by 26 lines of dots (3056-3081) and nothing else; the encoding records it as blank in this text (reason 3).
2. **"Officer" is undefined inside Schedule 5.** Regulation 3(1) defines "officer" "except in Part 8 and Schedule 5" (line 88), and Schedule 5 uses "officer", "manager", "agent" and "member" without defining them (lines 3243-3255). Each role is a plain fact the caller states.
3. **Schedule 3A and Schedule 6A print some paragraph numbers and not others** (forks S3A-F1, S6A-F1). Schedule 4 prints none (S4-F1). Schedule 6 prints none after the chapeau (S6-F1).
4. **Schedule 3A paragraph 6 depends on a date the rendering does not give** (S3A-F3), and **paragraph 13 depends on words the rendering replaces with an ellipsis** (S3A-F6).
5. **Schedule 4 asks for counts that other parts encode.** PLAN.md (line 197) records that items at lines 3220, 3224, 3227, 3228, 3234 and 3235 count decisions under regulations 26, 59 and 60 and disclosures under regulation 104; the Schedule names data to collect, and no answer crosses.
6. **Schedule 6 prints 14 lists after a chapeau that cites 5 to 13** (S6-F1): the last two printed lists (regulations 66, 69(2), 70(7), 74A to 74C, 77 and 78; and regulation 84(1)) lie beyond the chapeau's range if numbered by position. Whether regulation 18A or 19A is in "18 to 21" is not said (S6-F2).
7. **Schedule 6B has two vintages**, split on the registration date, 25 October 2027 (lines 3393, 3494). The text does not say when the Schedule itself comes into force (S6B-F2).
8. **Paragraph 5 of Schedule 6B and the inserted section 191G definition disagree** about whether a custodian wallet provider is a "registered cryptoasset business" (lines 3543 against 3492 and 3537; S6B-F1).
9. **Section 183(3)(b)(i) says 10% of the shares "in B" only** (line 3439), where section 181(1)(b)(i) says "in B or P" (line 3405) and section 183(3)(b)(ii) says "in B or P" (line 3440). Read as printed (S6B-F5).
10. **"Statutory minimum" and "statutory maximum"** (S6B-F3): minimum at lines 3480, 3485 and 3525, maximum at line 3530 only.
11. **The defined term "cryptoasset business" (line 3540) is not used on its own in Schedule 6B.** Outside its definition it occurs only inside "registered cryptoasset business(es)" and in the title of regulation 58A quoted at line 3448.
12. **Schedule 7 has 35 paragraphs; paragraph 27 is blank** (lines 3752-3753, the heading and a line of dots). Three paragraphs insert rules that stand alone (3(2), 12, 18); the rest amend other texts and are inert (reason 2).
13. **Schedule 7 paragraph 12 carries a stray comma** ("regulations 33, and 35 to 37", line 3686) and a reading choice that turns on it (S7-F1).
14. **Schedule 7 paragraph 3(2) inserts "The rules must provide ..." with no actor** (S7-F2).
15. **No assertion of this part fails.** There is no expected failure, no refused assertion, and no assertion kept meant to fail.

## What the main binary does not accept

Observed in this part, on 1.6.109 (and read the same on 1.6.108):

- **A `#TRACE` outcome cannot be asserted.** It prints `FULFILLED`, `BREACHED` or a residual obligation as an information line and no assertion line, and `check.sh` counts assertion lines only. So every regulative rule in this part (Schedule 6A: 17 rules, run by 30 traces; Schedule 7 paragraph 18: one rule, run by 3 traces) also exists as a decision function over the same facts, and the decision function is the asserted one. The trace outcomes were compared across 1.6.108 and 1.6.109 by hand: identical.
- **A value of type `DEONTIC` cannot be compared with `EQUALS`,** so a regulative rule cannot be the left side of an `#ASSERT`.
- **`WAIT UNTIL` is spelled `WAITUNTIL`.** The two-word form was rejected.
- **`length` does not exist in the prelude;** the function is `count`.
- **A `GIVETH` type that has spaces or digits needs backticks.** ``GIVETH A sch 6B the set of modifications`` is a parse error ("unexpected 6"); ``GIVETH A `sch 6B the set of modifications` `` is accepted.

From the brief, and avoided here: `REFUSE`, `#ASSERT REFUSED` and `BECAUSE`; an unparenthesised `NOT` (it binds over the whole `AND`); a continuation line in an `#ASSERT`; a bullet list in a `LIST`; `TYPICALLY`; a `YMD` of one's own; sets; a section-level `GIVEN`.

## What check.sh prints

Run as `L4=<main 1.6.109> L4_MAIN=<main 1.6.108> ./check.sh` in this folder (target `main`, the default), after the last edit to any `.l4` file:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
mlr-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
mlr5-cases-seat.l4                             0       199       0        0         0 |      0       199       0        0  same
mlr5-sch3a.l4                                  0         0       0        0         0 |      0         0       0        0  same
mlr5-sch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr5-sch5.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr5-sch6.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr5-sch6a.l4                                  0         0       0        0         0 |      0         0       0        0  same
mlr5-sch6b.l4                                  0         0       0        0         0 |      0         0       0        0  same
mlr5-sch7.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr5-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr5-tests-sch3a.l4                            0       224       0        0         0 |      0       224       0        0  same
mlr5-tests-sch4.l4                             0       131       0        0         0 |      0       131       0        0  same
mlr5-tests-sch5.l4                             0        46       0        0         0 |      0        46       0        0  same
mlr5-tests-sch6.l4                             0       207       0        0         0 |      0       207       0        0  same
mlr5-tests-sch6a.l4                            0        84       0        0         0 |      0        84       0        0  same
mlr5-tests-sch6b.l4                            0       219       0        0         0 |      0       219       0        0  same
mlr5-tests-sch7.l4                             0        36       0        0         0 |      0        36       0        0  same
TOTAL (17 modules)                             0      1146       0        0           |      0      1146       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
EXIT=0
```

Baseline: before this part's files were added, this folder held only the supplied files, and `check.sh` listed one module, `mlr-core.l4`, with 0 errors and 0 assertions on both binaries.
There is no earlier `check.sh` output for the `mlr5-*` files to compare with.
The numbers above are the whole of it: 17 modules, 0 errors, 1146 assertions satisfied, 0 failed, 0 refused, every module `same` on the second main build.

## Dependencies

None.
`inputs/DEPENDENCIES.md` stages no module for this text: the one Commons row for the Interpretation Act 1978 targets unstable (it uses `REFUSE`) and cannot be read by a main build.
This part imports the prelude, `daydate` (for `Date`) and the keel's `mlr-core.l4`.
The one counted period in this range ("less than two years has passed since that person's death", Schedule 3A) is a function with tests on both sides of its end, using `Date`; no rule of the Interpretation Act is applied, and the leap-day consequence is fork S3A-F4.

## Unstable dialect

I looked at time, versions and workarounds and found no shape that earns a second encoding.
The one rule that depends on dates, Schedule 6B, is split on the date the business was included in the register (25 October 2027), which is a fact about the business and not the date of the asking, so main expresses it directly with `Date` and two sets of rows; the relevant-date test in Schedule 7 paragraph 18 is a comparison of three dates the caller states.
No workaround on main was needed beyond those listed under "What the main binary does not accept".

