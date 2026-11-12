# Crimes Act 1914 (Cth), sections 4AA to 4N: penalty units and the general rules on penalties and liability

Status: draft, not reviewed.
Verified by: `check.sh` on build 1.6.98 and on build 1.6.110 (the counts agree on every module), `srcrefs.py --refs` and `--strict`, and a search of every module's `l4 run` output for warnings and errors on both builds.
What was run is under "What `check.sh` prints" below.
No domain expert has read this encoding against the text.

Edition: compilation C2026C00368 (Compilation No. 167, compilation date 27 August 2026), as converted in `C1914A00012.txt`.
Scope: section 4A, sections 4AA to 4N (text lines 4332-4456), and the section 3 lines the in-scope text uses (lines 41, 144, 146, 151, 163 and 189-196).
The formulas the text file lost are read from its sidecar `C1914A00012.formulas.md` (entries for s 4AA(3), s 4AA(4) and s 4B(2)).
The text is a converted rendering and is not the authorised text; see `SOURCE-LICENSE.md`.

Layer 1 holds the rules, one module for each group of sections.
Layer 2 is `crm-seat.l4` and `crm-cases-seat.l4`.
Every rule in layer 1 carries `@ref` with `src:` quotations that `srcrefs.py` checks against the text.

## Seat

The seat is a person or officer working out the most that can be imposed for a Commonwealth offence.
Such a person asks what a penalty of so many penalty units comes to in dollars, how a penalty stated in dollars converts to penalty units, what a natural person or a body corporate may be fined, whether an offence is indictable or summary, whether a court of summary jurisdiction may deal with it, and whether a child of a given age can be liable.
The seat is that person's, not the court's, the prosecutor's or the Minister's.
Provisions addressed to a court (ss 4B, 4J, 4JA, 4K(4)), to the Minister (s 4AA(1A)) or to the prosecution (s 4N(2)) are encoded in layer 1 for what they decide, and appear in the seat only as what they mean to the person: how much, whether, and for whom.
`crm-seat.l4` has 32 questions, each with `@export` and `@desc`; a judgment the text leaves to a court ("the court thinks it appropriate", "the court thinks fit", "a contrary intention appears") is a yes/no input.

## What is encoded and what is not

Encoded, with tests:

- Section 4A (committed for trial; indictment) and the section 3 terms State, Territory, property, quarter and fine.
- Sections 4AA and 4AB: the amount of a penalty unit, its indexation on 1 July 2026 and every third 1 July after it, the choice of amount for an offence, and the conversion of a penalty in dollars to penalty units.
- Sections 4B, 4D, 4E and 4F: pecuniary penalties for natural persons and bodies corporate, penalties at the foot of a provision, recovery in a court of summary jurisdiction, and alterations in penalties.
- Sections 4C, 4G, 4H, 4J and 4JA: offences under two or more laws, indictable and summary offences, and summary hearing of indictable offences.
- Sections 4K, 4L, 4M and 4N: continuing and multiple offences, other defences, and children.

Not encoded, because the text file does not hold it and the encoding asks for it as an input:

- The index numbers of s 4AA(4) and the Minister's notifiable instrument of s 4AA(1A).
- The provisions prescribed for s 4AB(3).
- The content of the Divisions of the Criminal Code named in s 4J(7), of section 76 of the Competition and Consumer Act 2010, and of the other Acts the section 3 terms and s 4AB(2) name.
- Counting rules of the Acts Interpretation Act: not used; the module of Australian counting rules offered in the inputs was not copied.

The seat takes up to three offences for s 4K(4) (the third is 0 when there is none); layer 1 takes any number.

## How dates, periods and amounts are counted

`crm-time.l4` imports only `prelude` and `daydate`; every other module calls it for each number, term, date and age.
`Date day month year` rolls an impossible date forward (`Date 31 6 2026` is 1 July 2026), so no date the module builds is a 31st of a 30-day month or a 29 February in a year without one; `add years` clamps 29 February to 28 February, which the module does not use.
The first indexation day is `Date 1 7 2026`; the others are every third 1 July, and a day is tested by its day, month and year.
The reference quarter of an indexation day is the March quarter ending on 31 March of that year; the base quarter ends on 31 March three years earlier.
The factor is rounded half up at the fourth decimal place; the amount is rounded half up to the dollar; both use `FLOOR (x PLUS 0.5)` because the built-in `ROUND` rounds half to even.
A term of imprisonment is an `ImprisonmentTerm` (months, years, life, none); a year is 12 months (fork F1); the bands 12 months, 5 years and 10 years are cut by comparing months.
Days of a continuing failure are counted inclusively at both ends.
An age is the number of completed years from a date of birth to a given day; for a person born on 29 February the day 28 February of a year without a 29 February is not decided (fork F12).
Every stated period, amount and age has a test on each side of its limit in `crm-tests-time.l4`.

## Jural relations

One row for each provision that creates a relation between two parties.
Layer 1 states each relation once; the table gives both sides.

| provision | holder | holds | other party | correlative |
| --- | --- | --- | --- | --- |
| 4B(2), 4B(2A) | court | power to impose a pecuniary penalty on a natural person | natural person convicted | liability |
| 4B(3) | court | power to impose a pecuniary penalty on a body corporate | body corporate convicted | liability |
| 4B(4) | body corporate that is the person aggrieved | claim to the forfeiture, penalty or reparation | the payer under the law | duty |
| 4C(1) | prosecuting authority | power to prosecute and punish under either or any law | offender | liability |
| 4C(1) | offender | immunity from being punished twice for the same act | court | disability |
| 4C(2) | offender punished under a State or Territory law | immunity from punishment under the law of the Commonwealth | prosecuting authority | disability |
| 4D(1) | prosecuting authority | claim that an offence is punishable up to the penalty printed at the foot of the provision | person who contravenes | duty |
| 4E | claimant of a pecuniary penalty | power to recover it in a court of summary jurisdiction | person liable to pay | liability |
| 4F(1) | offender | immunity from a penalty increased after the offence | court | disability |
| 4J(1) | court of summary jurisdiction | power to hear and determine an indictable offence, with consent | prosecutor and defendant | liability |
| 4J(1) | prosecutor and defendant, each | power to consent, which the other party's consent completes | the other of them | liability |
| 4J(4) | prosecutor | power to request summary hearing | defendant | liability |
| 4J(3), (5), (6) | defendant | immunity from a sentence or fine above the limits | court of summary jurisdiction | disability |
| 4JA(1), (2) | court of summary jurisdiction | power to hear a fine-only indictable offence and impose up to the stated penalty | defendant | liability |
| 4K(1), (2) | Commonwealth | claim that the act be done, and an offence for each day | person bound | duty |
| 4K(3) | prosecution | power to join charges in one information, complaint or summons | defendant | liability |
| 4K(4) | court | power to impose one penalty for several offences | defendant | liability |
| 4K(4) | defendant | immunity from one penalty above the sum of the separate maxima | court | disability |
| 4L | defendant | privilege to use any defence otherwise available | prosecution | no-right |
| 4M | child under 10 | immunity from liability for an offence against a law of the Commonwealth | prosecution | disability |
| 4N(1) | child of 10 or more but under 14 | immunity from liability unless the child "knows that his or her conduct is wrong" | prosecution | disability |
| 4N(2) | defendant child | claim that the prosecution prove that the child knows | prosecution | duty |
| 4AA(1A) | the text names no holder | claim to publication of the indexed amount | Minister | duty |

## Coverage table

Every non-blank line of the text file, lines 1 to 17237, is in exactly one row; `work/coverage.py` builds the table and fails if a line is in none or in two.
Rows: 100 (10 out of scope, 19 inert, 45 encoded, 26 fork).
Text lines by disposition: 17097 out of scope, 19 inert, 66 encoded, 55 fork, counting non-blank lines.
The last three rows are formulas the text file lost; the sidecar carries them.
Out-of-scope rows stand for a whole Part or range and name it.
A row whose disposition is `fork` points at the fork register below and at the rule that encodes the reading taken; `convention F9` marks a rule that carries a contrary-intention input.

| row | text lines | provision | what it is | disposition | encoded in | tests | fork |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | 1-39 | Front matter, compilation notes, Part I heading, section 1 | Title, compilation notes, Part I heading and the short title | out of scope | - | - | - |
| C002 | 40 | 3 Interpretation (heading) | Heading of section 3 | inert | reason 1: not operative (a heading) | - | - |
| C003 | 41 | 3(1) opening words | "In this Act, unless the contrary intention appears:" | encoded | crm-defs: `s 3(1) the definitions in this subsection apply` | crm-tests-defs | convention F9 |
| C004 | 42-51 | 3(1) definitions, terms not used by ss 4A-4N | Definitions from "abuse" to "Australian law enforcement officer" that the in-scope text does not use | out of scope | - | - | - |
| C005 | 52 | 3(1) child | "child: without limiting who is a child of a person for the purposes of this Act, someone is the child of a person if ... within the meaning of the Family Law Act 1975" | fork | crm-defs: `s 3(1) someone is the child of a person`; ss 4M and 4N take the child's age as an input | crm-tests-defs | F26 |
| C006 | 53-143 | 3(1) definitions, terms not used by ss 4A-4N | Definitions from "child abuse material" to "person assisting the NACC Inspector" that the in-scope text does not use | out of scope | - | - | - |
| C007 | 144 | 3(1) property | "property includes money and every thing ... capable of being the subject of ownership" | encoded | crm-defs: `s 3(1) a thing is property` | crm-tests-defs | F17 |
| C008 | 145 | 3(1) public authority under the Commonwealth | A definition the in-scope text does not use | out of scope | - | - | - |
| C009 | 146 | 3(1) quarter | "quarter means a period of 3 months ending on 31 March, 30 June, 30 September or 31 December" | encoded | crm-defs: `s 3(1) a period is a quarter`; crm-time: `the first day of the quarter ending on` | crm-tests-defs, crm-tests-time | - |
| C010 | 147-150 | 3(1) definitions, terms not used by ss 4A-4N | Definitions from "relative" to "staff member of the NACC" | out of scope | - | - | - |
| C011 | 151 | 3(1) State | "State includes the Northern Territory" | encoded | crm-defs: `s 3(1) a place is a State` | crm-tests-defs, crm-cases-seat | F17 |
| C012 | 152-162 | 3(1) definitions, terms not used by ss 4A-4N | Definitions from "State offence" to the note on "target entity" | out of scope | - | - | - |
| C013 | 163 | 3(1) Territory | "Territory does not include the Northern Territory" | encoded | crm-defs: `s 3(1) a place is a Territory` | crm-tests-defs, crm-cases-seat | F17 |
| C014 | 164-188 | 3(1) definitions, terms not used by ss 4A-4N | Definitions from "terrorism offence" to "wholly-owned Commonwealth company" | out of scope | - | - | - |
| C015 | 189 | 3(2) opening words | "In this Act, a reference to a fine includes a reference:" | encoded | crm-defs: `s 3(2) a reference to a fine includes a reference to` | crm-tests-defs | - |
| C016 | 190-195 | 3(2)(a) | A pecuniary penalty other than five kinds listed in (i) to (iv) | encoded | crm-defs: `s 3(2) a reference to a fine includes a reference to` (the kinds are the choices of the type FineKind) | crm-tests-defs | - |
| C017 | 196 | 3(2)(b) | Costs or other amounts ordered to be paid by offenders | encoded | crm-defs: `s 3(2) a reference to a fine includes a reference to` | crm-tests-defs | - |
| C018 | 197-262 | 3(3) and 3AA | Relatives of a person, and State offences that have a federal aspect | out of scope | - | - | - |
| C019 | 263-4331 | Sections 3A to 4AAB (Parts I to IA, before section 4A) | Operation of the Act, search, information gathering and arrest powers, and the other provisions before section 4A | out of scope | - | - | - |
| C020 | 4332 | 4A heading | Meaning of certain words | inert | reason 1: not operative (a heading) | - | - |
| C021 | 4333 | 4A opening words | "In a law of the Commonwealth, unless the contrary intention appears:" | encoded | crm-defs: both s 4A rules take two yes/no inputs, that the term is used in a law of the Commonwealth and that a contrary intention appears | crm-tests-defs | convention F9 |
| C022 | 4334 | 4A committed for trial | "committed for trial ... means committed to prison ... or admitted to bail ..." | encoded | crm-defs: `s 4A a person is committed for trial` | crm-tests-defs | - |
| C023 | 4335 | 4A indictment | "indictment includes an information and a presentment" | encoded | crm-defs: `s 4A a document is an indictment` | crm-tests-defs | - |
| C024 | 4336 | 4AA heading | Penalty units | inert | reason 1: not operative (a heading) | - | - |
| C025 | 4337-4338 | 4AA(1) | The penalty unit is $330, subject to indexation | encoded | crm-penalty-units: `s 4AA(1) a penalty unit means the amount mentioned in that subsection`, `s 4AA(1) the number of dollars in a penalty of a number of penalty units`; crm-time: `the amount of a penalty unit before any indexation, in dollars` | crm-tests-penalty-units, crm-tests-time | convention F9 |
| C026 | 4339 | 4AA(1A) | The Minister publishes the amount; failure to publish does not invalidate the indexation | fork | crm-penalty-units: `s 4AA(1A) the Minister must, by notifiable instrument, publish the amount of a penalty unit`, `s 4AA(1A) a failure by the Minister to publish the amount invalidates the indexation` | crm-tests-penalty-units | F21 |
| C027 | 4340-4344 | 4AA(2) | Territory Ordinance | fork | crm-penalty-units: `s 4AA(2) a Territory Ordinance` | crm-tests-penalty-units | F22 |
| C028 | 4345 | 4AA sub-heading | Indexation of penalty unit | inert | reason 1: not operative (a heading) | - | - |
| C029 | 4346 | 4AA(3) | On 1 July 2026 and each third 1 July the dollar amount is replaced (formula in the sidecar) | encoded | crm-time: `the first indexation day`, `the indexation day numbered`, `a day is an indexation day`, `the number of indexation days on or before`, `the dollar amount after an indexation, to the nearest whole dollar`; crm-penalty-units: `s 4AA(3) the dollar amount mentioned in subsection (1) after the indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C030 | 4347-4348 | 4AA(4) and "where:" | The indexation factor (formula in the sidecar); the opening words of its list of terms | encoded | crm-time: `the indexation factor for an indexation day`; crm-penalty-units: `s 4AA(4) the indexation factor for an indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C031 | 4349 | 4AA(4) base quarter | The March quarter 3 years before the reference quarter | encoded | crm-time: `the day on which the base quarter ends`; crm-penalty-units: `s 4AA(4) a quarter is the base quarter for the indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C032 | 4350 | 4AA(4) index number | The All Groups Consumer Price Index number published for the quarter | encoded | crm-penalty-units: `s 4AA(4) a number is the index number for a quarter` (the number is an input) | crm-tests-penalty-units | - |
| C033 | 4351 | 4AA(4) March quarter | A quarter ending on 31 March | encoded | crm-time: `a March quarter ends on`; crm-penalty-units: `s 4AA(4) a period is a March quarter` | crm-tests-time, crm-tests-penalty-units | - |
| C034 | 4352 | 4AA(4) reference quarter | The March quarter immediately before the indexation day | encoded | crm-time: `the day on which the reference quarter ends`; crm-penalty-units: `s 4AA(4) a quarter is the reference quarter for the indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C035 | 4353 | 4AA(5) | The factor is calculated to 3 decimal places, rounding up at 5 | encoded | crm-time: `an indexation factor calculated to 3 decimal places`; crm-penalty-units: `s 4AA(5) an indexation factor calculated to 3 decimal places` | crm-tests-time, crm-tests-penalty-units | - |
| C036 | 4354 | 4AA(6) | Amounts are rounded to the nearest dollar, 50 cents upwards | encoded | crm-time: `the dollar amount after an indexation, to the nearest whole dollar`; crm-penalty-units: `s 4AA(6) the amount worked out under subsection (3), rounded to the nearest whole dollar` | crm-tests-time, crm-tests-penalty-units | - |
| C037 | 4355-4357 | 4AA(7) | Which index numbers the calculations use | encoded | crm-penalty-units: `s 4AA(7) an index number is used in a calculation under subsection (4)` | crm-tests-penalty-units | - |
| C038 | 4358 | 4AA sub-heading | Application of indexed penalty unit | inert | reason 1: not operative (a heading) | - | - |
| C039 | 4359 | 4AA(8) | The increased amount applies only to offences on or after the indexation day | fork | crm-time: `an offence was committed on or after the indexation day`; crm-penalty-units: `s 4AA(8) the increased amount applies to an offence`, `s 4AA(3), (8) the amount of a penalty unit for an offence` | crm-tests-time, crm-tests-penalty-units, crm-cases-seat | F11 |
| C040 | 4360 | 4AB heading | Conversion of pecuniary penalties expressed in dollar amounts to penalty units | inert | reason 1: not operative (a heading) | - | - |
| C041 | 4361-4363 | 4AB(1) | A penalty of D dollars is taken to be P penalty units, D / 100 rounded up | encoded | crm-time: `the number of penalty units that a penalty of D dollars is taken to be`; crm-penalty-units: `s 4AB(1) a reference to a pecuniary penalty of D dollars is taken to be a reference to a pecuniary penalty of P penalty units`, `s 4AB(1) P is` | crm-tests-time, crm-tests-penalty-units, crm-cases-seat | - |
| C042 | 4364 | 4AB(2) | Subsection (1) does not apply to the maximum amount of a penalty not imposed by a court or service tribunal | fork | crm-penalty-units: `s 4AB(2) subsection (1) applies` | crm-tests-penalty-units, crm-cases-seat | F10 |
| C043 | 4365-4367 | 4AB(3) | Subsection (1) does not apply to section 76 of the Competition and Consumer Act 2010 or a prescribed provision | encoded | crm-penalty-units: `s 4AB(3) subsection (1) applies`, `s 4AB the conversion of a penalty of D dollars to penalty units applies` | crm-tests-penalty-units, crm-cases-seat | - |
| C044 | 4368-4369 | 4AB(4) penalty | "penalty includes a fine" | encoded | crm-penalty-units: `s 4AB(4) a penalty includes` | crm-tests-penalty-units | - |
| C045 | 4370 | 4AB(4) Territory Ordinance | Same meaning as in section 4AA | encoded | crm-penalty-units: `s 4AB(4) Territory Ordinance has the same meaning as in section 4AA` | crm-tests-penalty-units | - |
| C046 | 4371 | 4B heading | Pecuniary penalties - natural persons and bodies corporate | inert | reason 1: not operative (a heading) | - | - |
| C047 | 4372 | 4B(1) | A provision is deemed to refer to bodies corporate as well as natural persons | encoded | crm-penalties: `s 4B(1) a provision is deemed to refer to bodies corporate as well as to natural persons` | crm-tests-penalties | convention F9 |
| C048 | 4373-4375 | 4B(2) | Natural person, imprisonment only: pecuniary penalty up to Term of Imprisonment x 5 penalty units (formula in the sidecar) | fork | crm-penalties: `s 4B(2) the court may impose a pecuniary penalty instead of, or in addition to, imprisonment`, `s 4B(2) the number of penalty units the pecuniary penalty may not exceed`; crm-time: `the term of imprisonment expressed in months`, `the number of penalty units calculated using the formula` | crm-tests-penalties, crm-tests-time, crm-cases-seat | F1, F2, F24 |
| C049 | 4376 | 4B(2A) | Natural person, imprisonment for life: pecuniary penalty up to 2,000 penalty units | fork | crm-penalties: `s 4B(2A) the court may impose a pecuniary penalty instead of, or in addition to, imprisonment for life`, `s 4B(2A) the number of penalty units the pecuniary penalty may not exceed` | crm-tests-penalties, crm-cases-seat | F24 |
| C050 | 4377 | 4B(3) | Body corporate: pecuniary penalty up to 5 times the natural person's maximum | fork | crm-penalties: `s 4B(3) the court may impose a pecuniary penalty on a body corporate`, `s 4B(3) the number of penalty units the pecuniary penalty on a body corporate may not exceed`; crm-time: `the amount equal to 5 times the natural person's maximum` | crm-tests-penalties, crm-tests-time, crm-cases-seat | F18 |
| C051 | 4378-4379 | 4B(3A) and (3A)(a) | An Act that specifies the maximum penalty for an instrument: the specified penalty is taken to be the maximum for natural persons | encoded | crm-penalties: `s 4B(3A)(a) the specified penalty is taken to be the maximum penalty that the instrument can prescribe for such offences by natural persons` | crm-tests-penalties | convention F9 |
| C052 | 4380 | 4B(3A)(b) | Specifying the penalty is not an indication of a contrary intention for subsection (3) | encoded | crm-penalties: `s 4B(3A)(b) the specifying of the penalty is treated as an indication of a contrary intention for the purposes of applying subsection (3)` | crm-tests-penalties | - |
| C053 | 4381 | 4B(4) | A penalty paid to a person aggrieved is payable to a body corporate that is the person aggrieved | encoded | crm-penalties: `s 4B(4) the forfeiture, penalty or reparation is payable to the body corporate` | crm-tests-penalties | - |
| C054 | 4382 | 4C heading | Offences under 2 or more laws | inert | reason 1: not operative (a heading) | - | - |
| C055 | 4383-4386 | 4C(1) | Offender liable to be prosecuted and punished under either or any law, not twice | fork | crm-offences: `s 4C(1) the offender is liable to be prosecuted and punished under either or any of those laws`, `s 4C(1) the offender is liable to be punished twice for the same act or omission` | crm-tests-offences, crm-cases-seat | F9, F23, F25 |
| C056 | 4387-4390 | 4C(2) | Punished under the State or Territory law: not liable under the law of the Commonwealth | fork | crm-offences: `s 4C(2) the offender is liable to be punished for the offence under the law of the Commonwealth` | crm-tests-offences, crm-cases-seat | F25 |
| C057 | 4391 | 4C(3) | Validity of a Territory law is not affected merely because the act is also a Commonwealth offence | fork | crm-offences: `s 4C(3) the validity of that law is affected` | crm-tests-offences | F25 |
| C058 | 4392 | 4D heading | Penalties | inert | reason 1: not operative (a heading) | - | - |
| C059 | 4393-4395 | 4D(1) | A penalty at the foot of a provision: the offence is punishable by it, or contravention is an offence punishable by it | fork | crm-penalties: `s 4D(1)(a) ...`, `s 4D(1)(b) ...`, `s 4D(1) a penalty is not exceeding the penalty so set out` | crm-tests-penalties, crm-cases-seat | F16 |
| C060 | 4396-4400 | 4D(1A) | The four places a penalty may be set out | fork | crm-penalties: `s 4D(1A) subsection (1) applies to a penalty set out` | crm-tests-penalties, crm-cases-seat | F15 |
| C061 | 4401 | 4D(1B) | Subsection (1) does not affect 4B(2), (2A) or (3) | encoded | crm-penalties: `s 4D(1B) subsection (1) affects the operation of` | crm-tests-penalties, crm-cases-seat | - |
| C062 | 4402 | 4D(2) | Subsection (1) applies to instruments made under an Act, not a law of a Territory | encoded | crm-penalties: `s 4D(2) subsection (1) applies to the instrument`, `s 4D(2) the rule, regulation or by-law is treated as a section of an Act` | crm-tests-penalties, crm-cases-seat | - |
| C063 | 4403 | 4E heading | Pecuniary penalties | inert | reason 1: not operative (a heading) | - | - |
| C064 | 4404 | 4E | A pecuniary penalty may be recovered in a court of summary jurisdiction | encoded | crm-penalties: `s 4E the pecuniary penalty may be recovered in the court` | crm-tests-penalties, crm-cases-seat | convention F9 |
| C065 | 4405 | 4F heading | Effect of alterations in penalties | inert | reason 1: not operative (a heading) | - | - |
| C066 | 4406 | 4F(1) | An increased penalty applies only to offences committed after the commencement | fork | crm-penalties: `s 4F(1) the penalty or maximum penalty as increased applies to the offence`; crm-time: `an offence was committed after the commencement` | crm-tests-penalties, crm-tests-time, crm-cases-seat | F3 |
| C067 | 4407 | 4F(2) | A reduced penalty extends to earlier offences but does not affect a penalty already imposed | fork | crm-penalties: `s 4F(2) the penalty or maximum penalty as reduced extends to an offence committed before the commencement`, `s 4F(2) the reduction affects a penalty imposed before the commencement`; crm-time: `an offence was committed before the commencement`, `a penalty was imposed before the commencement` | crm-tests-penalties, crm-tests-time, crm-cases-seat | F3, F4, F25 |
| C068 | 4408 | 4G heading | Indictable offences | inert | reason 1: not operative (a heading) | - | - |
| C069 | 4409 | 4G | Offences punishable by imprisonment for a period exceeding 12 months are indictable | fork | crm-offences: `s 4G the offence is an indictable offence`; crm-time: `the band of a term of imprisonment` | crm-tests-offences, crm-tests-time, crm-cases-seat | F2, F8 |
| C070 | 4410 | 4H heading | Summary offences | inert | reason 1: not operative (a heading) | - | - |
| C071 | 4411-4414 | 4H | Offences punishable by imprisonment for not more than 12 months, or not at all, are summary | fork | crm-offences: `s 4H the offence is a summary offence` | crm-tests-offences, crm-cases-seat | F2, F8 |
| C072 | 4415 | 4J heading | Certain indictable offences may be dealt with summarily | inert | reason 1: not operative (a heading) | - | - |
| C073 | 4416 | 4J(1) | An indictable offence punishable by not more than 10 years may be heard by a court of summary jurisdiction with consent | fork | crm-offences: `s 4J(1) a court of summary jurisdiction may hear and determine the indictable offence`, `s 4J(1) the consent of the prosecutor and the defendant is given` | crm-tests-offences, crm-cases-seat | F2, F6, F7 |
| C074 | 4417 | 4J(2) | Subsection (1) does not apply where another law lets a court of summary jurisdiction hear the offence | encoded | crm-offences: `s 4J(1) a court of summary jurisdiction may hear and determine the indictable offence` (an input) | crm-tests-offences, crm-cases-seat | - |
| C075 | 4418-4420 | 4J(3) | Limits of 12 months or 60 penalty units, and 2 years or 120 penalty units | fork | crm-offences: `s 4J(3) the most months of imprisonment the court may impose`, `s 4J(3) the most penalty units of fine the court may impose`; crm-time: `s 4J(3)(a) ...`, `s 4J(3)(b) ...` | crm-tests-offences, crm-tests-time, crm-cases-seat | F1, F2, F6 |
| C076 | 4421 | 4J(4) | A court of summary jurisdiction may hear an indictable offence about property of $5,000 or less on the prosecutor's request | encoded | crm-offences: `s 4J(4) a court of summary jurisdiction may hear and determine the proceeding`, `s 4J(4) the offence relates to property whose value does not exceed $5,000` | crm-tests-offences, crm-cases-seat | - |
| C077 | 4422 | 4J(5) | Limits of 12 months or 60 penalty units for an offence dealt with under subsection (4) | encoded | crm-offences: `s 4J(5) the most months of imprisonment the court may impose`, `s 4J(5) the most penalty units of fine the court may impose` | crm-tests-offences, crm-cases-seat | - |
| C078 | 4423-4426 | 4J(6) | No more than could have been imposed on indictment; not both where the offence is punishable by imprisonment or a fine but not both | fork | crm-offences: `s 4J(6)(a) ...`, `s 4J(6)(b) ...`, `s 4J(6)(c) ...` | crm-tests-offences, crm-cases-seat | F19 |
| C079 | 4427-4431 | 4J(7) | Section 4J does not apply to offences against Divisions 80, 82, 91 and 92 of the Criminal Code | encoded | crm-offences: `s 4J(7) section 4J does not apply to the offence` | crm-tests-offences, crm-cases-seat | - |
| C080 | 4432 | 4JA heading | Some indictable offences punishable by fine only may be dealt with summarily | inert | reason 1: not operative (a heading) | - | - |
| C081 | 4433-4436 | 4JA(1) | A court of summary jurisdiction may hear an indictable fine-only offence of up to 600 or 3,000 penalty units with consent | encoded | crm-offences: `s 4JA(1) a court of summary jurisdiction may hear and determine the indictable offence`, `s 4JA(1)(b) the pecuniary penalty for the offence is not more than the limit` | crm-tests-offences, crm-cases-seat | - |
| C082 | 4437-4440 | 4JA(2) | The most pecuniary penalty: 60 or 300, or 120 or 600, penalty units; not more than on indictment | fork | crm-offences: `s 4JA(2)(a) ...`, `s 4JA(2)(b) ...`, `s 4JA(2) the limit after the closing sentence`, and the two readings of the paragraphs together | crm-tests-offences, crm-cases-seat | F5 |
| C083 | 4441 | 4JA(3) | This section has effect subject to any contrary intention indicated by the law creating the offence | encoded | crm-offences: `s 4JA(3) this section has effect`, called by `s 4JA(1) a court of summary jurisdiction may hear and determine the indictable offence` | crm-tests-offences, crm-cases-seat | convention F9 |
| C084 | 4442-4444 | 4JA(4) | This section does not apply to an offence created by a law that provides for summary hearing, or one described in subsection 4J(4) | encoded | crm-offences: `s 4JA(4)(a) this section does not apply to the offence`, `s 4JA(4)(b) the offence is described in subsection 4J(4)`, both called by `s 4JA(1) ...` | crm-tests-offences, crm-cases-seat | - |
| C085 | 4445 | 4K heading | Continuing and multiple offences | inert | reason 1: not operative (a heading) | - | - |
| C086 | 4446 | 4K(1) | The obligation to do an act continues after the period has expired, until it is done | encoded | crm-liability: `s 4K(1) the obligation to do that act or thing continues` | crm-tests-liability, crm-cases-seat | convention F9 |
| C087 | 4447 | 4K(2) | An offence is committed in respect of each day of refusal or failure, including the day of conviction or any later day | fork | crm-liability: `s 4K(2) the person commits an offence in respect of the day`; crm-time: `the number of days in respect of each of which an offence is committed` | crm-tests-liability, crm-tests-time, crm-cases-seat | F13 |
| C088 | 4448 | 4K(3) | Charges against the same person for offences against the same provision may be joined | fork | crm-liability: `s 4K(3) the charges may be joined in the same information, complaint or summons` | crm-tests-liability, crm-cases-seat | F14 |
| C089 | 4449 | 4K(4) | One penalty for 2 or more offences, not more than the sum of the separate maxima | encoded | crm-liability: `s 4K(4) the court may impose one penalty in respect of both or all of those offences`, `s 4K(4) the most the one penalty may be`; crm-time: `the sum of the maximum penalties of 2 or more offences` | crm-tests-liability, crm-tests-time, crm-cases-seat | - |
| C090 | 4450 | 4L heading | Specified defences not to preclude other defences | inert | reason 1: not operative (a heading) | - | - |
| C091 | 4451 | 4L | A provision providing a defence does not prevent the use of any other available defence | fork | crm-liability: `s 4L the provision does not prevent the use of any defence that is otherwise available` | crm-tests-liability, crm-cases-seat | F9, F25 |
| C092 | 4452 | 4M heading | Children under 10 | inert | reason 1: not operative (a heading) | - | - |
| C093 | 4453 | 4M | A child under 10 years old cannot be liable | fork | crm-liability: `s 4M a child can be liable for an offence against a law of the Commonwealth`; crm-time: `the age in completed years` | crm-tests-liability, crm-tests-time, crm-cases-seat | F12 |
| C094 | 4454 | 4N heading | Children over 10 but under 14 | inert | reason 1: not operative (a heading) | - | - |
| C095 | 4455 | 4N(1) | A child of 10 or more but under 14 can only be liable if the child "knows that his or her conduct is wrong" | fork | crm-liability: `s 4N(1) a child can be liable for an offence against a law of the Commonwealth`, `ss 4M and 4N(1) a child can be liable for an offence against a law of the Commonwealth` | crm-tests-liability, crm-cases-seat | F12, F20 |
| C096 | 4456 | 4N(2) | Whether the child knows is a question of fact; the burden of proof is on the prosecution | encoded | crm-liability: `s 4N(2) the question whether a child knows that his or her conduct is wrong is one of fact`, `s 4N(2) the party on whom the burden of proving that the child knows rests` | crm-tests-liability | - |
| C097 | 4457-17238 | Section 6 to the end | The remaining sections, the Schedule and the endnotes | out of scope | - | - | - |
| C098 | sidecar | 4AA(3) formula | Indexation factor for the indexation day x Dollar amount immediately before the indexation day | encoded | crm-time: `the dollar amount after an indexation, to the nearest whole dollar`; crm-penalty-units: `s 4AA(3) the dollar amount mentioned in subsection (1) after the indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C099 | sidecar | 4AA(4) formula | Index number for the reference quarter / Index number for the base quarter | encoded | crm-time: `the indexation factor for an indexation day` | crm-tests-time, crm-tests-penalty-units | - |
| C100 | sidecar | 4B(2) formula | Term of Imprisonment x 5 | encoded | crm-time: `the number of penalty units calculated using the formula` | crm-tests-time, crm-tests-penalties | - |

## Fork register

Every ambiguity, the readings seen, the one taken, and the text that licenses each.
A function answers `JUST FALSE` where the text says no in its own words ("means", "if", "only if", "unless", "cannot", "does not apply", a failed "where" condition) and `NOTHING` where it lists without closing the list, says "includes", limits a grant without "only", or does not say.
Each row below is a site where that rule needed a decision.

| id | provision | rule | readings | taken | text |
| --- | --- | --- | --- | --- | --- |
| F1 | 4B(2), 4J(1), 4J(3) | `the term of imprisonment expressed in months` | A: a year is 12 months. B: the text defines neither year nor month, so a term stated in years has no number of months | A | "expressed in months" (4375); terms in years (4416, 4419) |
| F2 | 4B(2), 4G, 4H, 4J(1), 4J(3) | `the band of a term of imprisonment` | A: imprisonment for life is "a period exceeding 12 months". B: life is not a period, so the text does not say | B: `NOTHING` | "for a period exceeding 12 months" (4409) |
| F3 | 4F(1), 4F(2) | `an offence was committed after the commencement`, `... before the commencement` | A: an offence on the day of commencement is after it. B: that day is neither before nor after | B: `NOTHING` | "after the commencement", "before the commencement" (4406, 4407) |
| F4 | 4F(2) | `a penalty was imposed before the commencement` | A: a penalty imposed on the day of commencement is before it. B: the text does not say | B: `NOTHING` | "imposed before that commencement" (4407) |
| F5 | 4JA(2) | the two functions `s 4JA(2) the most penalty units the court may impose, on the reading that ...` | A: "or" between (a) and (b), so the court may impose the figure of any paragraph whose condition is met, and an offence within (a)'s condition is also within (b)'s. B: (a) covers the lower band and (b) only what is above it | both encoded; the seat asks both | (a) "not more than 300", (b) "not more than 600" (4438, 4439) |
| F6 | 4J(1), 4J(3) | `s 4J(1) a court of summary jurisdiction may hear and determine the indictable offence` | A: an offence not punishable by imprisonment, punishable for life, or over 10 years, is `JUST FALSE`. B: the grant is limited without "only", so the text does not say | B: `NOTHING` | "being an offence punishable by imprisonment for a period not exceeding 10 years" (4416) |
| F7 | 4J(1) | `s 4J(1) the consent of the prosecutor and the defendant is given` | A: no consent is `JUST FALSE`. B: `NOTHING` | A | "with the consent of the prosecutor and the defendant" (4416) |
| F8 | 4G, 4H | `s 4G ...`, `s 4H ...` | A: an offence of 12 months or less is not indictable, and one of more than 12 months is not summary. B: the text does not say, because neither section says "only" | B: `NOTHING` | "are indictable offences", "are summary offences" (4409, 4414) |
| F9 | 3(1), 4A, 4B(1), 4B(3A)(a), 4D(1), 4E, 4G, 4H, 4J(1), 4JA(3), 4K(1), 4L | every rule with the input `a contrary intention appears` | A: where a contrary intention appears, the proposition the text states is `JUST FALSE`. B: `NOTHING` | A, except the definition of Territory, which states what the term does not include and answers `NOTHING` | "unless the contrary intention appears" |
| F10 | 4AB(2) | `s 4AB(2) subsection (1) applies` | A: "not imposed by a court, or by a service tribunal" means imposed by neither. B: not imposed by a court, or not imposed by a service tribunal | A | (4364) |
| F11 | 4AA(8) | `s 4AA(8) the increased amount applies to an offence` | A: for an amount that was not increased the text says nothing about an offence before the indexation day. B: the earlier amount applies to it | A: `NOTHING` | "the increased amount only applies" (4359) |
| F12 | 4M, 4N | `the age in completed years` | A: completed years from the date of birth to the day of the offence; for a birth on 29 February, 28 February of a year without one is not decided. B: another way of counting years | A; `NOTHING` on that day | "A child under 10 years old" (4453) |
| F13 | 4K(2) | `the number of days in respect of each of which an offence is committed` | A: the person states the first and last day of the failure and both are counted. B: the first day is the day after the period expires | A | "each day during which the person refuses or fails to comply" (4447) |
| F14 | 4K(3) | `s 4K(3) the charges may be joined in the same information, complaint or summons` | A: the facts or series condition is an "if" condition, so failing it is `JUST FALSE`; other charges are outside the grant. B: `NOTHING` | A | "if those charges are founded on the same facts" (4448) |
| F15 | 4D(1A) | `s 4D(1A) subsection (1) applies to a penalty set out` | A: the four places are the only ones. B: the list is not closed, so a place the list does not name is not decided. (A penalty at the foot of a subsection that is also at the foot of the section containing it is at the foot of a section, so it is within paragraph (a).) | B: `NOTHING` for another place | no "only" (4396-4400) |
| F16 | 4D(1) | `s 4D(1)(a) ...`, `s 4D(1)(b) ...` | A: (a) is `JUST FALSE` where the provision does not expressly create an offence, and (b) where it does. B: `NOTHING` | A | "if the provision expressly creates an offence", "in any other case" (4394, 4395) |
| F17 | 3(1) | `s 3(1) a place is a State`, `... a Territory`, `... a thing is property` | A: a thing or place the definition does not name is outside it. B: the definition says "includes", so the text does not say | B: `NOTHING` | "includes" (144, 151); "does not include" (163) |
| F18 | 4B(3) | `s 4B(3) the number of penalty units the pecuniary penalty on a body corporate may not exceed` | A: the natural person's maximum is a number the person states (for an offence punishable by imprisonment only, the figure of s 4B(2)). B: the rule works it out | A | "the maximum pecuniary penalty that could be imposed by the court on a natural person convicted of the same offence" (4377) |
| F19 | 4J(6)(b), (c) | `s 4J(6)(b) ...`, `s 4J(6)(c) ...` | A: the maximum fine on indictment, and whether the offence is punishable by imprisonment or a fine but not both, are stated by the person. B: the rule works them out from s 4B(2), which allows a pecuniary penalty instead of, or in addition to, imprisonment | A | (4425, 4426) |
| F20 | 4N(1) | `s 4N(1) a child can be liable for an offence against a law of the Commonwealth` | A: "can only be liable ... if the child knows" is a necessary condition, so a child who knows is `NOTHING`. B: such a child is liable | A | "can only be liable" (4455) |
| F21 | 4AA(1A) | `s 4AA(1A) a failure by the Minister to publish the amount invalidates the indexation` | A: where the Minister has not published, `JUST FALSE`. B: `NOTHING` | A | "does not invalidate the indexation" (4339) |
| F22 | 4AA(2) | `s 4AA(2) a Territory Ordinance` | A: "means an ordinance that (a) and (b)", so an ordinance failing either, and a thing that is neither an ordinance nor a regulation made under one, is `JUST FALSE`; a regulation made under such an ordinance is included. B: `NOTHING` | A | "means an ordinance that" (4341), "and includes a regulation" (4344) |
| F23 | 4C(1) | `s 4C(1) the offender is liable to be punished twice for the same act or omission` | A: "unless the contrary intention appears" qualifies only the first limb, and "shall not be liable to be punished twice" is a flat negative. B: it qualifies both | A | the sentence structure (4386) |
| F24 | 4B(2), 4B(2A) | the seat question on s 4B(2), (2A) | A: an offence punishable by imprisonment for life is dealt with under 4B(2A) alone. B: it is also "punishable by imprisonment only", so both subsections apply | A | (4373, 4376) |
| F25 | 4C(1), 4C(2), 4C(3), 4F(2), 4L | the rules named, where the opening "Where" condition fails | A: a failed "Where" condition is `JUST FALSE`, as in ss 4B, 4F(1), 4J(4), 4JA, 4K. B: where the proposition asked is a negative consequence ("shall not be liable", "is not affected", "does not affect", "does not prevent") or is about several laws, the text says nothing about it outside the situation the "Where" describes | B: `NOTHING` at these sites | "Where" (4383, 4387, 4391, 4407, 4451) |
| F26 | 3(1), 4M, 4N | `s 3(1) someone is the child of a person` | A: ss 4M and 4N use "child" by age and take it as an input, so the section 3 entry, which says when someone is the child of a person, is not applied to them. B: the entry applies to them | A | "child: without limiting who is a child of a person" (52); "A child under 10 years old" (4453) |

## What the Act turns out to say

Each statement is the text's answer on the facts given; "Asserted." marks a statement a case in `crm-cases-seat.l4` or a layer-1 test asserts.

1. A penalty unit is $330 before the first indexation day, 1 July 2026. Asserted.
2. On 1 July 2026 and each third 1 July after it the amount is replaced by the indexation factor times the amount just before, rounded to the nearest dollar with 50 cents rounded up; on index numbers 130 and 125 the factor is 1.04 and $330 becomes $343. Asserted.
3. The increased amount applies only to offences committed on or after the indexation day: an offence on 30 June 2026 is at $330, one on 1 July 2026 at $343. Asserted.
4. A penalty of D dollars in a law of the Commonwealth is taken to be D divided by 100 penalty units, rounded up to a whole number: $250 is 3 penalty units, $200 is 2. Asserted.
5. That conversion does not apply to the maximum amount of a penalty that is not imposed by a court or service tribunal, to section 76 of the Competition and Consumer Act 2010, or to a provision prescribed for the purpose. Asserted.
6. Where a natural person is convicted of an offence punishable by imprisonment only, the court may, if it thinks it appropriate and no contrary intention appears, impose a pecuniary penalty of up to 5 penalty units for each month of the longest term: 12 months gives 60, 24 months gives 120. Asserted.
7. Where imprisonment for life may be imposed the pecuniary penalty is up to 2,000 penalty units. Asserted.
8. A body corporate may be fined up to 5 times the natural person's maximum: 60 gives 300, 2,000 gives 10,000. Asserted.
9. A penalty at the foot of a section makes the offence punishable by that penalty where the provision expressly creates an offence, and otherwise makes contravention an offence punishable by it, unless a contrary intention appears. Asserted.
10. A penalty at the foot of a subsection that is also at the foot of the section containing it is at the foot of a section, so s 4D(1A)(a) applies and the offence is punishable by that penalty unless a contrary intention appears. Asserted.
11. An increased penalty applies only to offences committed after the commencement: an offence on 31 December 2026 against a commencement on 1 January 2027 is outside it, one on 2 January 2027 inside it, and the text does not say about one on 1 January 2027. Asserted.
12. A reduced penalty extends to offences committed before the commencement but does not affect a penalty imposed before it. Asserted.
13. An offence punishable by imprisonment for more than 12 months is indictable; the text does not say that an offence of exactly 12 months is. Asserted.
14. An offence punishable by imprisonment for 12 months or less, or not at all, is summary. Asserted.
15. An indictable offence punishable by imprisonment for up to 10 years may be heard by a court of summary jurisdiction with the consent of the prosecutor and the defendant; the text does not say about one over 10 years. Asserted.
16. A court of summary jurisdiction may impose up to 12 months or 60 penalty units on an offence punishable by up to 5 years, and up to 24 months or 120 penalty units on one punishable by more than 5 years and up to 10. Asserted.
17. Those limits do not exceed what could have been imposed on indictment: for an offence with a longest term of 6 months the most is 6 months. Asserted.
18. A court of summary jurisdiction may, on the prosecutor's request, hear an indictable offence about property of $5,000 or less, and not one about property of $5,001. Asserted.
19. Section 4J does not apply to offences against Division 80 (other than Subdivision CA), 82, 91 or 92 of the Criminal Code. Asserted.
20. A court of summary jurisdiction may hear an indictable offence that is not punishable by imprisonment where the pecuniary penalty is not more than 600 penalty units for an individual or 3,000 for a body corporate and the defendant and prosecution consent. Asserted.
21. For such an offence punishable on indictment by 300 penalty units against an individual, the most the court may impose is 120 if paragraphs (a) and (b) of s 4JA(2) are alternatives and 60 if (a) covers only the lower band. Asserted.
22. An offender punished under a State or Territory law is not liable to be punished for the same act under the law of the Commonwealth; the Northern Territory is a State and not a Territory. Asserted.
23. A person who fails to do an act on each day from 1 March 2026 to 3 March 2026 commits an offence in respect of each of 3 days. Asserted.
24. One penalty for 2 or more joined offences may not exceed the sum of the separate maxima: 10 and 20 give 30. Asserted.
25. A provision giving a defence does not, unless a contrary intention appears, prevent the use of any other available defence. Asserted.
26. A child under 10 cannot be liable; a child of 10 or more but under 14 can be liable only if the child "knows that his or her conduct is wrong"; the question is one of fact and the burden of proving it is on the prosecution. Asserted.
27. For a child born on 29 February 2016 the text does not say on 28 February 2026 whether the tenth birthday has come; on 1 March 2026 the child is 10. Asserted.

## What the text does not answer

- The amount of a penalty unit after the first indexation day: the text states the formula and not the index numbers or the Minister's notice, so the question asks for them.
- Whether imprisonment for life is a period of more than 12 months, and so whether such an offence is indictable (fork F2).
- Which side of the day of commencement an offence or penalty on that day falls (forks F3, F4).
- Whether s 4JA(2)(a) applies to an offence that also meets the condition of (b) (fork F5).
- Whether a child who "knows that his or her conduct is wrong" is thereby liable, and the standard on which the prosecution must prove it.
- How years of age are counted for a person born on 29 February (fork F12).
- The provisions prescribed for s 4AB(3), and the content of the Divisions of the Criminal Code that s 4J(7) names.

## Cross-references

The text has 43 references from one provision of the in-scope text to another provision or to an instrument: 30 to a subsection of the same Act, 1 to a section of the same Act, 6 to a provision of another instrument (a section, Division or Part of another Act) and 6 to another instrument by name only.
None cites a provision of this Act outside the in-scope text, so no row is marked out of scope, and none is unresolved: every same-Act row has its section in the index, its subsection printed in that section, and the heading the text prints.
`work/gen_index.py` reads the text file, finds each reference with patterns for "section" and "subsection" (any case), a Division or Part followed by an Act title or the Criminal Code, and an Act title followed by a year, and writes `crm-provisions.l4` (the index: Part I, Part IA, section 3 and sections 4A to 4N, each with its identifier, heading, text lines and printed subsections), `crm-xrefs.l4` (one row for each reference, quoting the line that holds it) and `crm-tests-xrefs.l4` (three assertions for each same-Act row, two for each row about another instrument, and one for the count).
A reference to another instrument is a row of its own kind and is not resolved here.
A reference such as "this section" or "this subsection" is not a row, because it cites no other provision.
In `crm-xrefs.l4` the words are as printed, except that a non-breaking space is a plain space.

## What the stable binary does not accept

The writing binary is the stable build 1.6.98, so anything it rejects is not available; `check.sh` also runs every module on build 1.6.110 and the counts agree.
What this encoding met on 1.6.98:

- `LENGTH`, `length`, `MIN` and `MAX` are not defined; `crm-time.l4` counts a list with its own recursive function and compares with `IF`.
- Two `GIVEN` parameters on one line are rejected; each is on its own line.
- A `NOT` followed by `AND` or `OR` takes in everything to its right (`NOT a AND b` is `NOT (a AND b)`), so the encoding writes `(NOT a) AND ...` and `(NOT (a)) OR (NOT (b))`; a test of s 4AA(8) failed until that was done.
- An `ELSE IF` chain whose `ELSE` is at the same column as the line before it is rejected with "incorrect indentation"; a chain of three or more outcomes is written with `BRANCH ... OTHERWISE`.
- An empty list is written `(LIST)`; a record is built with `OF` and its fields in declaration order, each record in a list in brackets.
- `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, `YMD`, section `GIVEN`, `TYPICALLY` and sets are not used; a case outside the encoding is `NOTHING` or an explicit constructor, and is asserted.
- `JL4_LIBRARY_PATH` was left unset throughout.

## What `check.sh` prints

Run from the encoding folder as `L4=<build 1.6.98> L4_MAIN=<build 1.6.110> ./check.sh`; the output of the last run was:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
crm-cases-seat.l4                              0       210       0        0         0 |      0       210       0        0  same
crm-defs.l4                                    0         0       0        0         0 |      0         0       0        0  same
crm-liability.l4                               0         0       0        0         0 |      0         0       0        0  same
crm-offences.l4                                0         0       0        0         0 |      0         0       0        0  same
crm-penalties.l4                               0         0       0        0         0 |      0         0       0        0  same
crm-penalty-units.l4                           0         0       0        0         0 |      0         0       0        0  same
crm-provisions.l4                              0         0       0        0         0 |      0         0       0        0  same
crm-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
crm-tests-defs.l4                              0        48       0        0         0 |      0        48       0        0  same
crm-tests-liability.l4                         0        58       0        0         0 |      0        58       0        0  same
crm-tests-offences.l4                          0       184       0        0         0 |      0       184       0        0  same
crm-tests-penalties.l4                         0        90       0        0         0 |      0        90       0        0  same
crm-tests-penalty-units.l4                     0       101       0        0         0 |      0       101       0        0  same
crm-tests-time.l4                              0       205       0        0         0 |      0       205       0        0  same
crm-tests-xrefs.l4                             0       156       0        0         0 |      0       156       0        0  same
crm-time.l4                                    0         0       0        0         0 |      0         0       0        0  same
crm-xrefs.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (17 modules)                             0      1052       0        0           |      0      1052       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `srcrefs.py check --strict` over every `crm-*.l4`: `--refs` printed "srcrefs check: 277 src: lines, 190 runs, 190 locators, 0 problems" and `--strict` printed "srcrefs check: 277 src: lines, 190 runs, 190 locators, 0 problems".
A search of every module's `l4 run` output for `_Warning` and `_Error` on both builds found 0 lines on build 1.6.98 and 0 on build 1.6.110.

## What would need doing before relying on it

- A reader with the authorised text should check the encoding against it; the text used is a converted rendering, and the three formulas come from a sidecar.
- Each fork above should be ruled; F2, F3, F5, F6, F8 and F20 change answers a person would act on.
- The index numbers of s 4AA(4) and the Minister's notice of s 4AA(1A) should be fetched, so that the amount after 1 July 2026 is known and not an input.
- The provisions prescribed for s 4AB(3), the Divisions of the Criminal Code named in s 4J(7), and section 76 of the Competition and Consumer Act 2010 should be read and, where a rule turns on them, encoded.
- The currency of compilation C2026C00368 should be confirmed against the Federal Register of Legislation.
- The seat's three-offence limit for s 4K(4) should be lifted if the form can take a list.
