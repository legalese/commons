# Proceeds of Crime Act 2002, Part 7 (Money Laundering) and Schedule 9 -- encoding `legalese-sonnet-5.5`

Status: draft, written 2026-11-05 by a single Sonnet 5.5 agent working alone from the brief; no domain expert has read it against the text.
Target compiler: **main**, checked with build 1.6.109 (main, 4c887e0, 2026-11-04) and compared with build 1.6.108 (main, 2ae7c9b, 2026-11-02) by `check.sh`.
Every layer-1 module and the seat layer are complete; the numbers below are those of the final run (see "What check.sh prints").

## Method

One session, one agent, no subagents, working from the brief (`BRIEF.md`) and the two deposited plain-text renderings.
The two texts are plain-text renderings made by a converter script (`convert_uk.py`, see `inputs/SOURCES.md` and `SOURCE-LICENSE.md`); they are **not the official text**, and nothing here claims to have been verified against the official text.
Edition: the point-in-time of the latest revised version, 2026-06-30, retrieved 2026-11-05; the converter does not distinguish prospective provisions or extent versions (`text_caveat` in the meta files).
Quotations are never typed: a macro expander (`mkrefs.py`) copies the raw lines into `-- src:N | ...` comments and `@ref` locators, and `srcrefs.py` checks them (0 problems over all 21 modules).
The ruling of 2026-11-05 on periods, "where" conditions and scope limits is applied rule-wide (fork F12).
Every comment `-- FALSE-kind (...)` quotes the text, and `tags.py` checks that each quoted piece is in the source and that every `JUST FALSE` and every `NOTHING` result carries its tag.

## Layout

Layer 1, the law, in the text's order: `poca-nouns.l4` (shared nouns), `poca-sch9.l4` (Schedule 9), `poca-interp.l4` (s 340), `poca-threshold.l4` (s 339A), `poca-dealing.l4` (ss 327 to 329, 334), `poca-failure.l4` (ss 330 to 332), `poca-tipping.l4` (ss 333 to 333E), `poca-consent.l4` (ss 335 to 336D), `poca-disclose.l4` (ss 337 to 339ZG), `poca-orders.l4` (ss 339ZH to 339ZL).
Each has a `poca-tests-<name>.l4` beside it.
Layer 2, the seat: `poca-seat.l4` (47 questions) and `poca-cases-seat.l4` (281 cases).
Tools kept in the folder: `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`, `mkrefs.py`, `coverage.py`, `covgen.py`, `tags.py`, `marginal.py`, `runtest.sh`, `traces.sh`; `coverage-manual.tsv` is hand-written and `coverage-map.tsv` is generated from it and from the rule names.

## Seat

The seat is **a person in or outside the regulated sector who knows or suspects that property is criminal property, or who is asked to deal with it, asking on facts they can state whether they commit an offence under Part 7 or have a defence, and what they must disclose to whom and when**.
It is the individual to whom Part 7 is applied: the bank clerk who is asked to move a payment, the accountant who has come to suspect a client, the nominated officer who receives the report, the person who has made a disclosure and wants to proceed.
There is no seat for an official: a constable, an officer of Revenue and Customs, an NCA officer, a court or the Secretary of State.
Where a provision addresses only an official (the duty of s 339ZA, the court's power in s 339ZH(1), the court's powers in ss 336A and 336B), its rule is in layer 1 and the person meets it only through the questions that ask what they may be made to do or are protected from: the moratorium question takes the days of extension granted under s 336A or s 336C, and the information-order questions ask what a court can order of the person.
Section 339ZJ(2) lets any party appeal, so the person has three seat questions on it (s 339ZJ(1) to (3)); the appeal court's own powers on appeal (s 339ZJ(4)) stay in layer 1.
The seat layer has 47 questions in eleven `§` groups, in the order of the provisions they ask about (the file's helper rules come first): the three offences of dealing (ss 327 to 329); failure to disclose (ss 330 to 332); tipping off and the permitted disclosures (ss 333A to 333E); the ceilings of sentence (ss 333A(4), 334); consent (ss 335, 336); protection when disclosing (ss 337 to 339); the threshold amounts (s 339A); sharing a suspicion with another regulated business and the notifications and joint reports that count as the required disclosure (ss 339ZB to 339ZF); information orders and appeals (ss 339ZH to 339ZK, including s 339ZJ); criminal conduct and criminal property (s 340); and Schedule 9.
The questions on ss 339ZB to 339ZF are the person's own: whether they may share a suspicion with another regulated business, who must make the required notification, whether their notification or joint report counts as the disclosure s 330 or s 331 requires, and whether the relevant disclosure is protected.
Every question has `@export`, and every input has `@desc` worded as the person would be asked; plain yes/no, number, date, list of dates or choice inputs only.
A fact the person may not know is asked as `Yes / No / I am not sure`; "I am not sure" becomes `NOTHING` and a rule that cannot answer without it answers `NOTHING`.
The orders and regulations that Part 7 points to (the training the Secretary of State specifies in s 330(7), conduct prescribed in an order under ss 327(2A) and 330(7C), excluded business under s 327(2E), the prescribed form of a disclosure, regulation 28 of the 2017 Regulations, Directives 2002/87/EC and 2015/849/EU) are not among the sources, so the person says whether each applies.
Hand-gathering (E1, option B as guidance) appears in four functions, listed in fork F11; every section still has its own answer (option C).

### Reading a result: FALSE and NOTHING

Every decision function in this row answers `JUST TRUE`, `JUST FALSE` or `NOTHING`; the rule is that of 2026-10-29 and the two readings "for a lawyer" are listed under "Marginal readings for a lawyer".
- **`JUST TRUE`** means the text gives the answer yes on the facts stated: the offence is committed, the exception applies, the disclosure is protected, the consent is deemed.
- **A "no" (`JUST FALSE`)** is only an answer the text itself gives in its own words: "does not commit an offence if", "is not to be taken to breach", "may not be used in evidence", a "means" definition the facts do not meet, or (reading (a)) a failed condition of an offence, or a condition the text states for a rule or a protection ("if", "where", a period the text fixes in its own words) that the facts do not meet (ruling of 2026-11-05 (a) and (b)).
  On an offence question it means the text says the person does not commit the offence on those facts.
  It does not mean that the act is wise, or that no other offence or regulation applies.
- **"Not covered" (`NOTHING`)** means the text does not answer on the facts stated: the property's status is not known (`I am not sure` to s 340(3)), the Schedule 9 answer cannot be given (the person is not sure which head or exclusion applies, or a term Schedule 9 borrows from another instrument is not in the sources), an exception removes a bar without saying what follows (s 339ZI(2)), a protection or power given to a class of person or disclosure in a sentence that states no condition and no "only" (s 338(4) for a disclosure that is not "an authorised disclosure", s 339(1) for anyone but the Secretary of State: ruling of 2026-11-05 (c)), or a number or definition lives in an instrument that is not among the sources.
  `NOTHING` on "do I commit an offence" does not mean "you are safe"; it means that, on these facts, the text does not say.
- A caller must never turn `NOTHING` into `FALSE`.
- Hohfeld kinds are in the table below and are not typed into any answer (ruling N2).

## Jural relations

One row per provision or group of provisions that creates a relation; a provision that creates none (a definition, a counting or reading rule, a condition of an offence) is listed once as `none`.
"Crown" means the State that prosecutes and the court that convicts.
A prohibition is encoded twice, as an offence (a decision function) and as its derived `SHANT`; the relation is stated once here.

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 327(1), 328(1), 329(1) | the Crown | any person dealing with criminal property | claim / duty (`SHANT`, derived from the offence) | `s 327(1) the person must not ...`, `s 328(1) the person must not ...`, `s 329(1) the person must not ...`; offences `s 327(1) the person commits an offence` and its two siblings |
| s 327(2), (2A), (2C), (2D), (2F); 328(2), (3), (5), (6), (8); 329(2), (2A), (2C), (2D), (2F) | the person who does the act | the Crown | immunity / disability (the Crown cannot convict) | the matching `s 327(2) the exception ...` rules |
| s 327(2B), (2E), (2G), (3); 328(1) act, (4), (7), (9); 329(2B), (2E), (2G), (3) | none | none | definitions, counting and reading rules | `s 327(2B)`, `s 327(2G)`, `s 327(3)`, `s 329(3)(a) and (b)`, `s 329(3)(c)` and the like |
| s 330(1), 331(1), 332(1) | the Crown | a person in the regulated sector (330), a nominated officer (331, 332) | claim / duty (`MUST` make the required disclosure as soon as practicable; derived from the offence) | `s 330(1) the person must make the required disclosure`, `s 330(4) the person must make ...`, and the 331 and 332 siblings |
| s 330(2), (3), (3A), (4), (5), (5A); 331(2) to (5A); 332(2) to (5B) | none | none | the conditions of the offence and the required disclosure | `s 330(2) the first condition ...` and siblings |
| s 330(6), (7), (7B), (7C), (7D), (7E); 331(6), (6A), (6B), (6C); 332(6), (7) | the person | the Crown | immunity / disability | the matching exception rules and `s 330(6) to (7E) one of the exceptions applies` |
| s 330(8), 331(7) | the person | the court (it must consider guidance) | claim / duty | `s 330(8)`, `s 331(7)` |
| s 330(9), (9A), (10), (11), (12), (13), (14); 331(8), (9) | none | none | definitions | `s 330(9A)`, `s 330(10)`, `s 330(14)` and the like |
| s 333 | none | none | blank in this text | coverage row |
| s 333A(1), (3) | the Crown | a person in the regulated sector | claim / duty (`SHANT`, derived) | `s 333A(1) the person must not disclose ...`, `s 333A(3) ...` |
| s 333A(2), (5) | none | none | the matters within the offence; subject-to clause | `s 333A(2) ...`, `s 333A(5) ...` |
| s 333A(4); 334(1), (2), (3); 336(6) | the court (power to impose up to the ceiling) | the guilty person (liability) | power / liability | `s 333A(4)`, `s 334(1)`, `s 334(2)`, `s 334(3)`, `s 336(6)` |
| s 333B(1), (2), (4); 333C(2); 333D(1), (1A), (2), (3), (4) | the person who makes the permitted disclosure | the Crown | immunity / disability | the matching rules in `poca-tipping.l4` |
| s 333B(3), 333C(1), 333E(1) to (5) | none | none | definitions | `s 333B(3)`, `s 333C(1)`, `s 333E(...)` |
| s 335(2) | the person who made the authorised disclosure | the Crown (and the nominated officer) | immunity / disability (treated as having the appropriate consent) | `s 335(2) the person must be treated as having the appropriate consent` |
| s 335(1), (3) to (9) | none | none | what consent is; counting the notice period and the moratorium period | `s 335(1)`, `s 335(5)`, `s 335(6)`, `s 335(7)` ... |
| s 336(1) | the Crown | the nominated officer | claim / duty (`SHANT` give the appropriate consent unless a condition holds) | `s 336(1) the nominated officer must not give the appropriate consent unless a condition is satisfied` |
| s 336(5) | the Crown | the nominated officer | claim / duty (offence) | `s 336(5) the nominated officer commits an offence` |
| s 336(2) to (4), (7) to (11) | none | none | conditions, counting rules, definitions | `s 336(2)` ... |
| s 336A(1), (5) to (8) | the court (power to extend) | persons interested in the property (liability) | power / liability | `s 336A(1)`, `s 336A(5)` to `(8)` |
| s 336A(2), (9) | a senior officer, a constable, an immigration officer (power to apply) | persons interested in the property (liability) | power / liability | `s 336A(2)`, `s 336A(9)` |
| s 336A(3), (4), (10) | none | none | time limits and definitions | `s 336A(3)`, `s 336A(4)`, `s 336A(10)` |
| s 336B(2) | the parties | the court (duty to determine as soon as reasonably practicable) | claim / duty | `s 336B(2) the court has determined the proceedings as it must` |
| s 336B(3), (5), (6) | the court (power to exclude, to withhold) | an interested person (liability) | power / liability | `s 336B(3)`, `s 336B(5)`, `s 336B(6)` |
| s 336B(4) | the applicant (power to apply for an order withholding information) | an interested person | power / liability | `s 336B(4)` |
| s 336B(8) to (11) | a party (right of appeal) | the other party | power / liability | `s 336B(8)` to `(11)` |
| s 336C(1) to (9), 336D(2) to (9) | none | none | counting rules and definitions (the extension operates on the period of s 335(6) or s 336(8)) | `s 336C(...)`, `s 336D(...)` |
| s 337(1), (4A); 338(4), (4A); 339(4); 339ZF(1), (3), (4) | the discloser | whoever is owed a duty of confidence (and the Crown for civil liability) | immunity / disability (no breach, no civil liability) | the matching rules in `poca-disclose.l4` |
| s 337(2) to (5); 338(1), (2), (2A), (3), (5), (6); 339(3), (7) | none | none | the conditions of protection; definitions | `s 337(2)` ... `s 338(1)` ... |
| s 339(1) | the Secretary of State (power to prescribe the form and manner by order) | a person who makes a disclosure under ss 330, 331, 332 or 338 (liability) | power / liability | `s 339(1) the person may by order prescribe the form and manner of the disclosure` |
| s 339(1A) (with 339(1B)) | the Crown | any person who discloses under ss 330, 331, 332 or 338 | claim / duty (`SHANT`, derived) and offence | `s 339(1A) the person commits an offence`, `s 339(1A) the person must not make a disclosure ...` |
| s 339A(3), (4) | an officer of Revenue and Customs or a constable (power to specify a threshold amount) | the deposit-taking body, e-money or payment institution | power / liability | `s 339A(3)`, `s 339A(4)` |
| s 339A(2), (5), (6), (6A), (8) | none | none | amounts and definitions | `s 339A(2)` ... |
| s 339ZA | the Director General of the NCA | a constable or an officer of Revenue and Customs | claim / duty (`MUST` disclose in full to an authorised person as soon as practicable) | `s 339ZA the constable or officer of Revenue and Customs must disclose the disclosure in full to an authorised person` |
| s 339ZB(1), (6) | A (the discloser) | whoever owes a duty of confidence | privilege / no-right | `s 339ZB(1)`, `s 339ZB(6)` |
| s 339ZB(2) to (5); 339ZC(1), (2), (4), (5) | none | none | conditions; content of a request or notification | `s 339ZB(2)` ... `s 339ZC(1)` ... |
| s 339ZC(3); 339ZE(9) | the NCA | the person who must make the required notification / notify that no report is made | claim / duty (`MUST`) | `s 339ZC(3)`, `s 339ZE(9)` |
| s 339ZD(2), (3); 339ZE(2), (3), (5) to (8), (10) | the person whose notification or report is treated as the required disclosure | the Crown | immunity / disability | `s 339ZD(2)`, `s 339ZD(3)`, `s 339ZE(...)` |
| s 339ZD(4) to (8); 339ZG(2) to (9) | none | none | definitions and conditions | `s 339ZD(...)`, `s 339ZG(...)` |
| s 339ZF(2) | a UK law enforcement agency | a person making a relevant disclosure | claim / duty (`SHANT` include its information unless it consents) | `s 339ZF(2) a relevant disclosure must not include ...` |
| s 339ZF(5) | none | none | definitions | `s 339ZF(5) ...` |
| s 339ZH(1) | the court (power to make an information order) | the respondent (liability) | power / liability | `s 339ZH(1) the court may make an information order` |
| s 339ZH(2) to (7), (9), (11), (12) | none | none | content, conditions and definitions | `s 339ZH(2)` ... |
| s 339ZH(8) | a magistrates' court (power to order payment up to 5,000 pounds) | the person who fails to comply | power / liability | `s 339ZH(8)` |
| s 339ZI(1) | the person who made the statement | the prosecution (disability to use it) | immunity / disability | `s 339ZI(1)` |
| s 339ZI(2), (3), (4) | none | none | the exceptions and the meaning of perjury | `s 339ZI(2)` ... |
| s 339ZJ(1), (2), (4) | a party (right of appeal; the appeal court's power) | the other party | power / liability | `s 339ZJ(1)`, `s 339ZJ(2)`, `s 339ZJ(4)` |
| s 339ZJ(3) | none | none | which court hears the appeal | `s 339ZJ(3)` |
| s 339ZK(1), (3) | the respondent | the court and the NCA (disability to require privileged information; no breach) | immunity / disability | `s 339ZK(1)`, `s 339ZK(3)` |
| s 339ZK(2), (4) | none; the court (power to sit in private) | none; the parties | definition; power / liability | `s 339ZK(2)`, `s 339ZK(4)` |
| s 339ZL(7) | the person | the prosecution (a failure to follow the code does not of itself make liable) | immunity / disability | `s 339ZL(7)` |
| s 339ZL(8) | none | none | admissibility of the code | `s 339ZL(8)` |
| s 340(2) to (17) | none | none | definitions | the rules of `poca-interp.l4` |
| sch 9 paras 1 to 4 | none | none | what is in the regulated sector, what is excluded, who is a supervisory authority | `poca-sch9.l4` |
| the inert rows (powers to make orders, regulations, codes and rules of court: ss 336B(7), 339A(7), 339ZH(10), 339ZK(5), 339ZL(1) to (6), (9), 340(14B), sch 9 para 5) | the Secretary of State, the Treasury or the court (power) | whoever is subject to what they make (liability) | power / liability | none: the rows are inert, reason 2 |

## What is encoded and what is not

Everything in the two deposited texts has a row in the coverage table below; no row is out of scope or deferred.
All 994 non-blank text lines (820 of Part 7, 174 of Schedule 9) fall in exactly one finest row; the audit found no line without a row.
- **Encoded** (951 rows): every operative provision of Part 7 (ss 327 to 340 with the lettered sections) and every limb of Schedule 9, as a tested decision function, and for each duty or prohibition also a regulative rule (`#TRACE`) with a decision-function twin.
- **Inert** (42 rows): headings and titles, lead-ins that create no rule (reason 1); powers to make regulations, orders, codes and rules of court and the duties that surround them (reason 2).
  None is inert because "it addresses an official": ss 339ZA, 339ZH(1), 336A, 336B(2) to (6), 339ZJ are encoded for what they mean to the person.
- **Fork** (2 rows): `sch 9 para 2` (F4) and `s 330(6)(b)` (F5).
- **Repealed or blank in this text** (11 rows): s 333, ss 338(1)(b), 339(5), 339(6), and the dotted lines of Schedule 9.
- **Not encoded because they are not among the sources**: the Money Laundering Regulations 2017, the orders of the Secretary of State that Parts 7 points to, the Immigration Act 2014 checks, the Directives, the Crime and Courts Act 2013 s 1(5).
  Each is an input (a yes/no or a number the person states), never a value from memory.
  The seat layer asks it with an `@desc`.

## Coverage table

<!-- COVERAGE:BEGIN -->
Counts by disposition: encoded 951, fork 2, inert 42, repealed or blank in this text 11; rows 1006; unresolved 0.

| row | src lines | disposition | where it is encoded / why | test or fork |
|---|---|---|---|---|
| part 7 heading | p7:1 | inert: 1 not operative | the Part's title | - |
| part 7 heading "Offences" | p7:2 | inert: 1 not operative | a cross-heading | - |
| s 327 | p7:3-43 | encoded | see the child rows | poca-tests-dealing.l4 |
| s 327(1) | p7:4-9 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(1)(a) | p7:5 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(1)(b) | p7:6 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(1)(c) | p7:7 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(1)(d) | p7:8 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(1)(e) | p7:9 | encoded | `s 327(1) the act is one of those listed` ; `s 327(1) the person commits an offence` ; `s 327(1) the person must not conceal, disguise, convert, transfer or remove criminal property` | poca-tests-dealing.l4 |
| s 327(2) | p7:10-13 | encoded | `s 327(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 327(2)(a) | p7:11 | encoded | `s 327(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 327(2)(b) | p7:12 | encoded | `s 327(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 327(2)(c) | p7:13 | encoded | `s 327(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 327(2A) | p7:14-18 | encoded | `s 327(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 327(2A)(a) | p7:15 | encoded | `s 327(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 327(2A)(b) | p7:16-18 | encoded | `s 327(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 327(2B) | p7:19 | encoded | `s 327(2B) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 327(2B) “the relevant criminal conduct” | p7:19 | encoded | `s 327(2B) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 327(2C) | p7:20-22 | encoded | `s 327(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 327(2C)(a) | p7:21 | encoded | `s 327(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 327(2C)(b) | p7:22 | encoded | `s 327(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 327(2D) | p7:23-29 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2D) “P” | p7:23 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2D)(a) | p7:24 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2D)(b) | p7:25-27 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2D)(c) | p7:28 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2D)(d) | p7:29 | encoded | `s 327(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 327(2E) | p7:30-33 | encoded | folded into the input fields of `s 327(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 327(2E)(a) | p7:31 | encoded | folded into the input fields of `s 327(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 327(2E)(b) | p7:32 | encoded | folded into the input fields of `s 327(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 327(2E)(c) | p7:33 | encoded | folded into the input fields of `s 327(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 327(2E)(c) “customer due diligence duties” | p7:33 | encoded | folded into the input fields of `s 327(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 327(2F) | p7:34-39 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F) “P” | p7:34 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(a) | p7:35 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(b) | p7:36 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(c) | p7:37 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(c) “the relevant criminal property” | p7:37 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(d) | p7:38 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2F)(e) | p7:39 | encoded | `s 327(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 327(2G) | p7:40-42 | encoded | `s 327(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 327(2G)(a) | p7:41 | encoded | `s 327(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 327(2G)(b) | p7:42 | encoded | `s 327(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 327(3) | p7:43 | encoded | `s 327(3) concealing or disguising criminal property includes concealing or disguising it in this way` | poca-tests-dealing.l4 |
| s 328 | p7:44-78 | encoded | see the child rows | poca-tests-dealing.l4 |
| s 328(1) | p7:45 | encoded | `s 328(1) the person's act is the act of subsection (1)` ; `s 328(1) the person commits an offence` ; `s 328(1) the person must not enter into or become concerned in an arrangement which facilitates the use of criminal property` | poca-tests-dealing.l4 |
| s 328(2) | p7:46-49 | encoded | `s 328(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 328(2)(a) | p7:47 | encoded | `s 328(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 328(2)(b) | p7:48 | encoded | `s 328(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 328(2)(c) | p7:49 | encoded | `s 328(2) the exception for a disclosure, an excuse or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 328(3) | p7:50-54 | encoded | `s 328(3) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 328(3)(a) | p7:51 | encoded | `s 328(3) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 328(3)(b) | p7:52-54 | encoded | `s 328(3) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 328(4) | p7:55 | encoded | `s 328(4) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 328(4) “the relevant criminal conduct” | p7:55 | encoded | `s 328(4) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 328(5) | p7:56-58 | encoded | `s 328(5) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 328(5)(a) | p7:57 | encoded | `s 328(5) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 328(5)(b) | p7:58 | encoded | `s 328(5) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 328(6) | p7:59-65 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(6) “P” | p7:59 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(6)(a) | p7:60 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(6)(b) | p7:61-63 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(6)(c) | p7:64 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(6)(d) | p7:65 | encoded | `s 328(6) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 328(7) | p7:66-69 | encoded | folded into the input fields of `s 328(6) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 328(7)(a) | p7:67 | encoded | folded into the input fields of `s 328(6) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 328(7)(b) | p7:68 | encoded | folded into the input fields of `s 328(6) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 328(7)(c) | p7:69 | encoded | folded into the input fields of `s 328(6) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 328(7)(c) “customer due diligence duties” | p7:69 | encoded | folded into the input fields of `s 328(6) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 328(8) | p7:70-75 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8) “P” | p7:70 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(a) | p7:71 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(b) | p7:72 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(c) | p7:73 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(c) “the relevant criminal property” | p7:73 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(d) | p7:74 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(8)(e) | p7:75 | encoded | `s 328(8) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 328(9) | p7:76-78 | encoded | `s 328(9) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 328(9)(a) | p7:77 | encoded | `s 328(9) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 328(9)(b) | p7:78 | encoded | `s 328(9) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 329 | p7:79-121 | encoded | see the child rows | poca-tests-dealing.l4 |
| s 329(1) | p7:80-83 | encoded | `s 329(1) the act is one of those listed` ; `s 329(1) the person commits an offence` ; `s 329(1) the person must not acquire, use or have possession of criminal property` | poca-tests-dealing.l4 |
| s 329(1)(a) | p7:81 | encoded | `s 329(1) the act is one of those listed` ; `s 329(1) the person commits an offence` ; `s 329(1) the person must not acquire, use or have possession of criminal property` | poca-tests-dealing.l4 |
| s 329(1)(b) | p7:82 | encoded | `s 329(1) the act is one of those listed` ; `s 329(1) the person commits an offence` ; `s 329(1) the person must not acquire, use or have possession of criminal property` | poca-tests-dealing.l4 |
| s 329(1)(c) | p7:83 | encoded | `s 329(1) the act is one of those listed` ; `s 329(1) the person commits an offence` ; `s 329(1) the person must not acquire, use or have possession of criminal property` | poca-tests-dealing.l4 |
| s 329(2) | p7:84-88 | encoded | `s 329(2) the exception for a disclosure, an excuse, adequate consideration or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 329(2)(a) | p7:85 | encoded | `s 329(2) the exception for a disclosure, an excuse, adequate consideration or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 329(2)(b) | p7:86 | encoded | `s 329(2) the exception for a disclosure, an excuse, adequate consideration or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 329(2)(c) | p7:87 | encoded | `s 329(2) the exception for a disclosure, an excuse, adequate consideration or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 329(2)(d) | p7:88 | encoded | `s 329(2) the exception for a disclosure, an excuse, adequate consideration or the enforcement of the law applies` | poca-tests-dealing.l4 |
| s 329(2A) | p7:89-93 | encoded | `s 329(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 329(2A)(a) | p7:90 | encoded | `s 329(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 329(2A)(b) | p7:91-93 | encoded | `s 329(2A) the exception for conduct lawful abroad applies` | poca-tests-dealing.l4 |
| s 329(2B) | p7:94 | encoded | `s 329(2B) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 329(2B) “the relevant criminal conduct” | p7:94 | encoded | `s 329(2B) the conduct is the relevant criminal conduct` | poca-tests-dealing.l4 |
| s 329(2C) | p7:95-97 | encoded | `s 329(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 329(2C)(a) | p7:96 | encoded | `s 329(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 329(2C)(b) | p7:97 | encoded | `s 329(2C) the exception for acts in operating an account applies` | poca-tests-dealing.l4 |
| s 329(2D) | p7:98-104 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2D) “P” | p7:98 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2D)(a) | p7:99 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2D)(b) | p7:100-102 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2D)(c) | p7:103 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2D)(d) | p7:104 | encoded | `s 329(2D) the exception for acts that end a business relationship applies` | poca-tests-dealing.l4 |
| s 329(2E) | p7:105-108 | encoded | folded into the input fields of `s 329(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 329(2E)(a) | p7:106 | encoded | folded into the input fields of `s 329(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 329(2E)(b) | p7:107 | encoded | folded into the input fields of `s 329(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 329(2E)(c) | p7:108 | encoded | folded into the input fields of `s 329(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 329(2E)(c) “customer due diligence duties” | p7:108 | encoded | folded into the input fields of `s 329(2D) the exception for acts that end a business relationship applies`: 'excluded business' is a description in regulations (an input), a transfer 'to the customer or client' includes one at the customer's direction (carried in the field's wording), and the customer due diligence duties are those of regulation 28 of the 2017 Regulations (an input) | poca-tests-dealing.l4 |
| s 329(2F) | p7:109-114 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F) “P” | p7:109 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(a) | p7:110 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(b) | p7:111 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(c) | p7:112 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(c) “the relevant criminal property” | p7:112 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(d) | p7:113 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2F)(e) | p7:114 | encoded | `s 329(2F) the exception for mixed funds applies` | poca-tests-dealing.l4 |
| s 329(2G) | p7:115-117 | encoded | `s 329(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 329(2G)(a) | p7:116 | encoded | `s 329(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 329(2G)(b) | p7:117 | encoded | `s 329(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-tests-dealing.l4 |
| s 329(3) | p7:118-121 | encoded | `s 329(3)(a) and (b) the consideration is inadequate` and `s 329(3)(c) the provision of goods or services is consideration` | poca-tests-dealing.l4 |
| s 329(3)(a) | p7:119 | encoded | `s 329(3)(a) and (b) the consideration is inadequate` | poca-tests-dealing.l4 |
| s 329(3)(b) | p7:120 | encoded | `s 329(3)(a) and (b) the consideration is inadequate` | poca-tests-dealing.l4 |
| s 329(3)(c) | p7:121 | encoded | `s 329(3)(c) the provision of goods or services is consideration` | poca-tests-dealing.l4 |
| s 330 | p7:122-190 | encoded | see the child rows | poca-tests-failure.l4 |
| s 330(1) | p7:123 | encoded | `s 330(1) the person commits an offence` ; `s 330(1) the person must make the required disclosure` | poca-tests-failure.l4 |
| s 330(2) | p7:124-127 | encoded | `s 330(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 330(2)(a) | p7:125 | encoded | `s 330(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 330(2)(b) | p7:126-127 | encoded | `s 330(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 330(3) | p7:128-131 | encoded | `s 330(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 330(3)(a) | p7:129 | encoded | `s 330(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 330(3)(b) | p7:130-131 | encoded | `s 330(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 330(3A) | p7:132-134 | encoded | `s 330(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 330(3A)(a) | p7:133 | encoded | `s 330(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 330(3A)(b) | p7:134 | encoded | `s 330(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 330(4) | p7:135-138 | encoded | `s 330(4) the fourth condition is satisfied` ; `s 330(4) the person must make the required disclosure to a nominated officer or an authorised person as soon as practicable` ; GAP (stated, not invented): the text fixes no number for "as soon as is practicable", so no function works out a deadline or says a disclosure was late; the condition takes the person's own statement, and the MUST has no WITHIN (fork F7, and the ruling of 2026-11-05 (a)) | poca-tests-failure.l4 |
| s 330(4)(a) | p7:136 | encoded | `s 330(4) the fourth condition is satisfied` ; `s 330(4) the person must make the required disclosure to a nominated officer or an authorised person as soon as practicable` ; GAP (stated, not invented): the text fixes no number for "as soon as is practicable", so no function works out a deadline or says a disclosure was late; the condition takes the person's own statement, and the MUST has no WITHIN (fork F7, and the ruling of 2026-11-05 (a)) | poca-tests-failure.l4 |
| s 330(4)(b) | p7:137-138 | encoded | `s 330(4) the fourth condition is satisfied` ; `s 330(4) the person must make the required disclosure to a nominated officer or an authorised person as soon as practicable` ; GAP (stated, not invented): the text fixes no number for "as soon as is practicable", so no function works out a deadline or says a disclosure was late; the condition takes the person's own statement, and the MUST has no WITHIN (fork F7, and the ruling of 2026-11-05 (a)) | poca-tests-failure.l4 |
| s 330(5) | p7:139-142 | encoded | `s 330(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 330(5) “the required disclosure” | p7:139 | encoded | `s 330(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 330(5)(a) | p7:140 | encoded | `s 330(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 330(5)(b) | p7:141 | encoded | `s 330(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 330(5)(c) | p7:142 | encoded | `s 330(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 330(5A) | p7:143 | encoded | `s 330(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 330(5A) “the laundered property” | p7:143 | encoded | `s 330(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 330(6) | p7:144-149 | encoded | `s 330(6) to (7E) one of the exceptions applies` | poca-tests-failure.l4 |
| s 330(6)(a) | p7:145 | encoded | `s 330(6)(a) the exception for a reasonable excuse applies` | poca-tests-failure.l4 |
| s 330(6)(b) | p7:146-148 | fork | F5: paragraph (i) opens "if he knows either of the things mentioned in subsection (5)(a) and (b), he knows the thing because of ..."; read literally as a material conditional, an adviser who knows neither thing satisfies (i) vacuously; the other reading is that (i) requires privileged knowledge always; encoded by `s 330(6)(b) the exception for a professional adviser applies` | poca-tests-failure.l4 |
| s 330(6)(c) | p7:149 | encoded | `s 330(6)(c) subsection (7) or (7B) applies to him` | poca-tests-failure.l4 |
| s 330(7) | p7:150-152 | encoded | `s 330(7) the exception for an untrained person who does not know or suspect applies` | poca-tests-failure.l4 |
| s 330(7)(a) | p7:151 | encoded | `s 330(7) the exception for an untrained person who does not know or suspect applies` | poca-tests-failure.l4 |
| s 330(7)(b) | p7:152 | encoded | `s 330(7) the exception for an untrained person who does not know or suspect applies` | poca-tests-failure.l4 |
| s 330(7B) | p7:153-156 | encoded | `s 330(7B) the exception for a person assisting an adviser applies` | poca-tests-failure.l4 |
| s 330(7B)(a) | p7:154 | encoded | `s 330(7B) the exception for a person assisting an adviser applies` | poca-tests-failure.l4 |
| s 330(7B)(b) | p7:155 | encoded | `s 330(7B) the exception for a person assisting an adviser applies` | poca-tests-failure.l4 |
| s 330(7B)(c) | p7:156 | encoded | `s 330(7B) the exception for a person assisting an adviser applies` | poca-tests-failure.l4 |
| s 330(7C) | p7:157-161 | encoded | `s 330(7C) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 330(7C)(a) | p7:158 | encoded | `s 330(7C) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 330(7C)(b) | p7:159-161 | encoded | `s 330(7C) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 330(7D) | p7:162-164 | encoded | `s 330(7D) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 330(7D)(a) | p7:163 | encoded | `s 330(7D) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 330(7D)(b) | p7:164 | encoded | `s 330(7D) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 330(7E) | p7:165-167 | encoded | `s 330(7E) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 330(7E)(a) | p7:166 | encoded | `s 330(7E) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 330(7E)(b) | p7:167 | encoded | `s 330(7E) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 330(8) | p7:168-171 | encoded | `s 330(8) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 330(8)(a) | p7:169 | encoded | `s 330(8) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 330(8)(b) | p7:170 | encoded | `s 330(8) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 330(8)(c) | p7:171 | encoded | `s 330(8) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 330(9) | p7:172-174 | encoded | `s 330(9) the disclosure satisfies paragraphs (a) and (b) of the definition of a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9) “a disclosure to a nominated officer” | p7:172 | encoded | `s 330(9) the disclosure satisfies paragraphs (a) and (b) of the definition of a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9)(a) | p7:173 | encoded | `s 330(9) the disclosure satisfies paragraphs (a) and (b) of the definition of a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9)(b) | p7:174 | encoded | `s 330(9) the disclosure satisfies paragraphs (a) and (b) of the definition of a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9A) | p7:175-178 | encoded | `s 330(9A) the disclosure is a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9A)(a) | p7:176 | encoded | `s 330(9A) the disclosure is a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9A)(b) | p7:177 | encoded | `s 330(9A) the disclosure is a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(9A)(c) | p7:178 | encoded | `s 330(9A) the disclosure is a disclosure to a nominated officer` | poca-tests-failure.l4 |
| s 330(10) | p7:179-182 | encoded | `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-tests-failure.l4 |
| s 330(10) “information that comes to an adviser in privileged circumstances” | p7:179 | encoded | `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-tests-failure.l4 |
| s 330(10)(a) | p7:180 | encoded | `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-tests-failure.l4 |
| s 330(10)(b) | p7:181 | encoded | `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-tests-failure.l4 |
| s 330(10)(c) | p7:182 | encoded | `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-tests-failure.l4 |
| s 330(11) | p7:183 | encoded | folded into `s 330(10) the information or other matter came to the adviser in privileged circumstances`: its criminal-purpose input makes the answer JUST FALSE | poca-tests-failure.l4 |
| s 330(12) | p7:184-186 | encoded | see the child rows | poca-tests-failure.l4 |
| s 330(12)(a) | p7:185 | encoded | `s 330(12)(a) the business is a business in the regulated sector` | poca-tests-failure.l4 |
| s 330(12)(b) | p7:186 | encoded | `s 330(12)(b) the body is a supervisory authority` | poca-tests-failure.l4 |
| s 330(13) | p7:187 | encoded | `s 330(13) the body is an appropriate body` | poca-tests-failure.l4 |
| s 330(13) “an appropriate body” | p7:187 | encoded | `s 330(13) the body is an appropriate body` | poca-tests-failure.l4 |
| s 330(14) | p7:188-190 | encoded | `s 330(14) the person is a relevant professional adviser` | poca-tests-failure.l4 |
| s 330(14) “a relevant professional adviser” | p7:188 | encoded | `s 330(14) the person is a relevant professional adviser` | poca-tests-failure.l4 |
| s 330(14)(a) | p7:189 | encoded | `s 330(14) the person is a relevant professional adviser` | poca-tests-failure.l4 |
| s 330(14)(b) | p7:190 | encoded | `s 330(14) the person is a relevant professional adviser` | poca-tests-failure.l4 |
| s 331 | p7:191-228 | encoded | see the child rows | poca-tests-failure.l4 |
| s 331(1) | p7:192 | encoded | `s 331(1) the person commits an offence` ; `s 331(1) the nominated officer must make the required disclosure` | poca-tests-failure.l4 |
| s 331(2) | p7:193-196 | encoded | `s 331(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 331(2)(a) | p7:194 | encoded | `s 331(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 331(2)(b) | p7:195-196 | encoded | `s 331(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 331(3) | p7:197-200 | encoded | `s 331(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 331(3)(a) | p7:198 | encoded | `s 331(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 331(3)(b) | p7:199-200 | encoded | `s 331(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 331(3A) | p7:201-204 | encoded | `s 331(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 331(3A)(a) | p7:202 | encoded | `s 331(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 331(3A)(b) | p7:203 | encoded | `s 331(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 331(3A)(c) | p7:204 | encoded | `s 331(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 331(4) | p7:205 | encoded | `s 331(4) the fourth condition is satisfied` ; `s 331(4) the nominated officer must make the required disclosure to an authorised person as soon as practicable` ; GAP (stated, not invented): the text fixes no number for "as soon as is practicable", so no function works out a deadline or says a disclosure was late; the condition takes the person's own statement, and the MUST has no WITHIN (fork F7, and the ruling of 2026-11-05 (a)) | poca-tests-failure.l4 |
| s 331(5) | p7:206-209 | encoded | `s 331(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 331(5) “the required disclosure” | p7:206 | encoded | `s 331(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 331(5)(a) | p7:207 | encoded | `s 331(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 331(5)(b) | p7:208 | encoded | `s 331(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 331(5)(c) | p7:209 | encoded | `s 331(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 331(5A) | p7:210 | encoded | `s 331(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 331(5A) “the laundered property” | p7:210 | encoded | `s 331(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 331(6) | p7:211 | encoded | `s 331(6) the exception for a reasonable excuse applies` | poca-tests-failure.l4 |
| s 331(6A) | p7:212-216 | encoded | `s 331(6A) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 331(6A)(a) | p7:213 | encoded | `s 331(6A) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 331(6A)(b) | p7:214-216 | encoded | `s 331(6A) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 331(6B) | p7:217-219 | encoded | `s 331(6B) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 331(6B)(a) | p7:218 | encoded | `s 331(6B) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 331(6B)(b) | p7:219 | encoded | `s 331(6B) the exception for information from an immigration check applies` | poca-tests-failure.l4 |
| s 331(6C) | p7:220-222 | encoded | `s 331(6C) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 331(6C)(a) | p7:221 | encoded | `s 331(6C) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 331(6C)(b) | p7:222 | encoded | `s 331(6C) the exception for information from an eligibility verification notice applies` | poca-tests-failure.l4 |
| s 331(7) | p7:223-226 | encoded | `s 331(7) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 331(7)(a) | p7:224 | encoded | `s 331(7) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 331(7)(b) | p7:225 | encoded | `s 331(7) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 331(7)(c) | p7:226 | encoded | `s 331(7) the court must consider whether he followed the guidance` | poca-tests-failure.l4 |
| s 331(8) | p7:227 | encoded | `s 331(8) the body is a supervisory authority` | poca-tests-failure.l4 |
| s 331(9) | p7:228 | encoded | `s 331(9) the body is an appropriate body` | poca-tests-failure.l4 |
| s 331(9) “an appropriate body” | p7:228 | encoded | `s 331(9) the body is an appropriate body` | poca-tests-failure.l4 |
| s 332 | p7:229-249 | encoded | see the child rows | poca-tests-failure.l4 |
| s 332(1) | p7:230 | encoded | `s 332(1) the person commits an offence` ; `s 332(1) the nominated officer must make the required disclosure` | poca-tests-failure.l4 |
| s 332(2) | p7:231 | encoded | `s 332(2) the first condition is satisfied` | poca-tests-failure.l4 |
| s 332(3) | p7:232 | encoded | `s 332(3) the second condition is satisfied` | poca-tests-failure.l4 |
| s 332(3A) | p7:233-236 | encoded | `s 332(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 332(3A)(a) | p7:234 | encoded | `s 332(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 332(3A)(b) | p7:235 | encoded | `s 332(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 332(3A)(c) | p7:236 | encoded | `s 332(3A) the third condition is satisfied` | poca-tests-failure.l4 |
| s 332(4) | p7:237 | encoded | `s 332(4) the fourth condition is satisfied` ; `s 332(4) the nominated officer must make the required disclosure to an authorised person as soon as practicable` ; GAP (stated, not invented): the text fixes no number for "as soon as is practicable", so no function works out a deadline or says a disclosure was late; the condition takes the person's own statement, and the MUST has no WITHIN (fork F7, and the ruling of 2026-11-05 (a)) | poca-tests-failure.l4 |
| s 332(5) | p7:238-241 | encoded | `s 332(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 332(5) “the required disclosure” | p7:238 | encoded | `s 332(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 332(5)(a) | p7:239 | encoded | `s 332(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 332(5)(b) | p7:240 | encoded | `s 332(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 332(5)(c) | p7:241 | encoded | `s 332(5) the disclosure is the required disclosure` | poca-tests-failure.l4 |
| s 332(5A) | p7:242 | encoded | `s 332(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 332(5A) “the laundered property” | p7:242 | encoded | `s 332(5A) the property is the laundered property` | poca-tests-failure.l4 |
| s 332(5B) | p7:243 | encoded | `s 332(5B) the section is the applicable section` | poca-tests-failure.l4 |
| s 332(5B) “the applicable section” | p7:243 | encoded | `s 332(5B) the section is the applicable section` | poca-tests-failure.l4 |
| s 332(6) | p7:244 | encoded | `s 332(6) the exception for a reasonable excuse applies` | poca-tests-failure.l4 |
| s 332(7) | p7:245-249 | encoded | `s 332(7) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 332(7)(a) | p7:246 | encoded | `s 332(7) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 332(7)(b) | p7:247-249 | encoded | `s 332(7) the exception for money laundering lawful abroad applies` | poca-tests-failure.l4 |
| s 333 | p7:250-251 | repealed or blank in this text | shown as a row of dots only (line 251) | - |
| s 333A | p7:252-273 | encoded | see the child rows | poca-tests-tipping.l4 |
| s 333A(1) | p7:253-256 | encoded | `s 333A(1) the person commits an offence by disclosing a matter within subsection (2)` ; `s 333A(1) the person must not disclose a matter within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(1)(a) | p7:254 | encoded | `s 333A(1) the person commits an offence by disclosing a matter within subsection (2)` ; `s 333A(1) the person must not disclose a matter within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(1)(b) | p7:255 | encoded | `s 333A(1) the person commits an offence by disclosing a matter within subsection (2)` ; `s 333A(1) the person must not disclose a matter within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(1)(c) | p7:256 | encoded | `s 333A(1) the person commits an offence by disclosing a matter within subsection (2)` ; `s 333A(1) the person must not disclose a matter within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(2) | p7:257-262 | encoded | `s 333A(2) the matter is within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(2)(a) | p7:258 | encoded | `s 333A(2) the matter is within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(2)(b) | p7:259 | encoded | `s 333A(2) the matter is within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(2)(c) | p7:260 | encoded | `s 333A(2) the matter is within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(2)(d) | p7:261-262 | encoded | `s 333A(2) the matter is within subsection (2)` | poca-tests-tipping.l4 |
| s 333A(3) | p7:263-266 | encoded | `s 333A(3) the person commits an offence by disclosing an investigation` ; `s 333A(3) the person must not disclose that an investigation is contemplated or is being carried out` | poca-tests-tipping.l4 |
| s 333A(3)(a) | p7:264 | encoded | `s 333A(3) the person commits an offence by disclosing an investigation` ; `s 333A(3) the person must not disclose that an investigation is contemplated or is being carried out` | poca-tests-tipping.l4 |
| s 333A(3)(b) | p7:265 | encoded | `s 333A(3) the person commits an offence by disclosing an investigation` ; `s 333A(3) the person must not disclose that an investigation is contemplated or is being carried out` | poca-tests-tipping.l4 |
| s 333A(3)(c) | p7:266 | encoded | `s 333A(3) the person commits an offence by disclosing an investigation` ; `s 333A(3) the person must not disclose that an investigation is contemplated or is being carried out` | poca-tests-tipping.l4 |
| s 333A(4) | p7:267-269 | encoded | `s 333A(4) the most that can be imposed on a person guilty of an offence under section 333A` | poca-tests-tipping.l4 |
| s 333A(4)(a) | p7:268 | encoded | `s 333A(4) the most that can be imposed on a person guilty of an offence under section 333A` | poca-tests-tipping.l4 |
| s 333A(4)(b) | p7:269 | encoded | `s 333A(4) the most that can be imposed on a person guilty of an offence under section 333A` | poca-tests-tipping.l4 |
| s 333A(5) | p7:270-273 | encoded | `s 333A(5) one of the permitted disclosures of sections 333B to 333D applies` | poca-tests-tipping.l4 |
| s 333A(5)(a) | p7:271 | encoded | `s 333A(5) one of the permitted disclosures of sections 333B to 333D applies` | poca-tests-tipping.l4 |
| s 333A(5)(b) | p7:272 | encoded | `s 333A(5) one of the permitted disclosures of sections 333B to 333D applies` | poca-tests-tipping.l4 |
| s 333A(5)(c) | p7:273 | encoded | `s 333A(5) one of the permitted disclosures of sections 333B to 333D applies` | poca-tests-tipping.l4 |
| s 333B | p7:274-284 | encoded | see the child rows | poca-tests-tipping.l4 |
| s 333B(1) | p7:275 | encoded | `s 333B(1) the disclosure within an undertaking is permitted` | poca-tests-tipping.l4 |
| s 333B(2) | p7:276-279 | encoded | `s 333B(2) the disclosure within a group of institutions is permitted` | poca-tests-tipping.l4 |
| s 333B(2)(a) | p7:277 | encoded | `s 333B(2) the disclosure within a group of institutions is permitted` | poca-tests-tipping.l4 |
| s 333B(2)(b) | p7:278 | encoded | `s 333B(2) the disclosure within a group of institutions is permitted` | poca-tests-tipping.l4 |
| s 333B(2)(c) | p7:279 | encoded | `s 333B(2) the disclosure within a group of institutions is permitted` | poca-tests-tipping.l4 |
| s 333B(3) | p7:280 | encoded | `s 333B(3) the institutions belong to the same group` | poca-tests-tipping.l4 |
| s 333B(3) “group” | p7:280 | encoded | `s 333B(3) the institutions belong to the same group` | poca-tests-tipping.l4 |
| s 333B(4) | p7:281-284 | encoded | `s 333B(4) the disclosure between advisers in undertakings under common control is permitted` | poca-tests-tipping.l4 |
| s 333B(4)(a) | p7:282 | encoded | `s 333B(4) the disclosure between advisers in undertakings under common control is permitted` | poca-tests-tipping.l4 |
| s 333B(4)(b) | p7:283 | encoded | `s 333B(4) the disclosure between advisers in undertakings under common control is permitted` | poca-tests-tipping.l4 |
| s 333B(4)(c) | p7:284 | encoded | `s 333B(4) the disclosure between advisers in undertakings under common control is permitted` | poca-tests-tipping.l4 |
| s 333C | p7:285-298 | encoded | see the child rows | poca-tests-tipping.l4 |
| s 333C(1) | p7:286-290 | encoded | `s 333C(1) this section applies to the disclosure` | poca-tests-tipping.l4 |
| s 333C(1)(a) | p7:287 | encoded | `s 333C(1) this section applies to the disclosure` | poca-tests-tipping.l4 |
| s 333C(1)(b) | p7:288 | encoded | `s 333C(1) this section applies to the disclosure` | poca-tests-tipping.l4 |
| s 333C(1)(c) | p7:289 | encoded | `s 333C(1) this section applies to the disclosure` | poca-tests-tipping.l4 |
| s 333C(1)(d) | p7:290 | encoded | `s 333C(1) this section applies to the disclosure` | poca-tests-tipping.l4 |
| s 333C(2) | p7:291-298 | encoded | `s 333C(2) the disclosure between institutions or advisers is permitted` | poca-tests-tipping.l4 |
| s 333C(2)(a) | p7:292-295 | encoded | `s 333C(2) the disclosure between institutions or advisers is permitted` | poca-tests-tipping.l4 |
| s 333C(2)(b) | p7:296 | encoded | `s 333C(2) the disclosure between institutions or advisers is permitted` | poca-tests-tipping.l4 |
| s 333C(2)(c) | p7:297 | encoded | `s 333C(2) the disclosure between institutions or advisers is permitted` | poca-tests-tipping.l4 |
| s 333C(2)(d) | p7:298 | encoded | `s 333C(2) the disclosure between institutions or advisers is permitted` | poca-tests-tipping.l4 |
| s 333D | p7:299-317 | encoded | see the child rows | poca-tests-tipping.l4 |
| s 333D(1) | p7:300-307 | encoded | `s 333D(1) the disclosure for one of the listed purposes is permitted` | poca-tests-tipping.l4 |
| s 333D(1)(a) | p7:301 | encoded | `s 333D(1) the disclosure for one of the listed purposes is permitted` | poca-tests-tipping.l4 |
| s 333D(1)(aa) | p7:302 | encoded | `s 333D(1) the disclosure for one of the listed purposes is permitted` | poca-tests-tipping.l4 |
| s 333D(1)(ab) | p7:303 | encoded | `s 333D(1) the disclosure for one of the listed purposes is permitted` | poca-tests-tipping.l4 |
| s 333D(1)(b) | p7:304-307 | encoded | `s 333D(1) the disclosure for one of the listed purposes is permitted` | poca-tests-tipping.l4 |
| s 333D(1A) | p7:308-312 | encoded | `s 333D(1A) the disclosure to a customer or client about the application is permitted` | poca-tests-tipping.l4 |
| s 333D(1A)(a) | p7:309 | encoded | `s 333D(1A) the disclosure to a customer or client about the application is permitted` | poca-tests-tipping.l4 |
| s 333D(1A)(b) | p7:310 | encoded | `s 333D(1A) the disclosure to a customer or client about the application is permitted` | poca-tests-tipping.l4 |
| s 333D(1A)(c) | p7:311-312 | encoded | `s 333D(1A) the disclosure to a customer or client about the application is permitted` | poca-tests-tipping.l4 |
| s 333D(2) | p7:313-315 | encoded | `s 333D(2) the disclosure by an adviser to dissuade the client is permitted` | poca-tests-tipping.l4 |
| s 333D(2)(a) | p7:314 | encoded | `s 333D(2) the disclosure by an adviser to dissuade the client is permitted` | poca-tests-tipping.l4 |
| s 333D(2)(b) | p7:315 | encoded | `s 333D(2) the disclosure by an adviser to dissuade the client is permitted` | poca-tests-tipping.l4 |
| s 333D(3) | p7:316 | encoded | `s 333D(3) the exception of section 333D(3) applies` | poca-tests-tipping.l4 |
| s 333D(4) | p7:317 | encoded | `s 333D(4) the exception of section 333D(4) applies` | poca-tests-tipping.l4 |
| s 333E | p7:318-329 | encoded | see the child rows | poca-tests-tipping.l4 |
| s 333E(1) | p7:319-321 | encoded | `s 333E(1) the business is a business in the regulated sector` ; `s 333E(1) the body is a supervisory authority` | poca-tests-tipping.l4 |
| s 333E(1)(a) | p7:320 | encoded | `s 333E(1) the business is a business in the regulated sector` ; `s 333E(1) the body is a supervisory authority` | poca-tests-tipping.l4 |
| s 333E(1)(b) | p7:321 | encoded | `s 333E(1) the business is a business in the regulated sector` ; `s 333E(1) the body is a supervisory authority` | poca-tests-tipping.l4 |
| s 333E(2) | p7:322-324 | encoded | `s 333E(2) the institution is a credit institution` ; `s 333E(2) the undertaking is a financial institution` | poca-tests-tipping.l4 |
| s 333E(2) “credit institution” | p7:323 | encoded | `s 333E(2) the institution is a credit institution` ; `s 333E(2) the undertaking is a financial institution` | poca-tests-tipping.l4 |
| s 333E(2) “financial institution” | p7:324 | encoded | `s 333E(2) the institution is a credit institution` ; `s 333E(2) the undertaking is a financial institution` | poca-tests-tipping.l4 |
| s 333E(3) | p7:325 | encoded | `s 333E(3) the disclosure counts as a disclosure by or to the institution` | poca-tests-tipping.l4 |
| s 333E(4) | p7:326 | encoded | `s 333E(4) the country or territory imposes equivalent money laundering requirements` | poca-tests-tipping.l4 |
| s 333E(5) | p7:327-329 | encoded | `s 333E(5) the person is a relevant professional adviser` | poca-tests-tipping.l4 |
| s 333E(5) “relevant professional adviser” | p7:327 | encoded | `s 333E(5) the person is a relevant professional adviser` | poca-tests-tipping.l4 |
| s 333E(5)(a) | p7:328 | encoded | `s 333E(5) the person is a relevant professional adviser` | poca-tests-tipping.l4 |
| s 333E(5)(b) | p7:329 | encoded | `s 333E(5) the person is a relevant professional adviser` | poca-tests-tipping.l4 |
| s 334 | p7:330-337 | encoded | see the child rows | poca-tests-dealing.l4 |
| s 334(1) | p7:331-333 | encoded | `s 334(1) the most that can be imposed on a person guilty of an offence under section 327, 328 or 329` | poca-tests-dealing.l4 |
| s 334(1)(a) | p7:332 | encoded | `s 334(1) the most that can be imposed on a person guilty of an offence under section 327, 328 or 329` | poca-tests-dealing.l4 |
| s 334(1)(b) | p7:333 | encoded | `s 334(1) the most that can be imposed on a person guilty of an offence under section 327, 328 or 329` | poca-tests-dealing.l4 |
| s 334(2) | p7:334-336 | encoded | `s 334(2) the most that can be imposed on a person guilty of an offence under section 330, 331 or 332` | poca-tests-dealing.l4 |
| s 334(2)(a) | p7:335 | encoded | `s 334(2) the most that can be imposed on a person guilty of an offence under section 330, 331 or 332` | poca-tests-dealing.l4 |
| s 334(2)(b) | p7:336 | encoded | `s 334(2) the most that can be imposed on a person guilty of an offence under section 330, 331 or 332` | poca-tests-dealing.l4 |
| s 334(3) | p7:337 | encoded | `s 334(3) the most that can be imposed on a person guilty of an offence under section 339(1A)` | poca-tests-dealing.l4 |
| part 7 heading "Consent" | p7:338 | inert: 1 not operative | a cross-heading | - |
| s 335 | p7:339-362 | encoded | see the child rows | poca-tests-consent.l4 |
| s 335(1) | p7:340-343 | encoded | `s 335(1) the consent is the appropriate consent` | poca-tests-consent.l4 |
| s 335(1) “the appropriate consent” | p7:340 | encoded | `s 335(1) the consent is the appropriate consent` | poca-tests-consent.l4 |
| s 335(1)(a) | p7:341 | encoded | `s 335(1) the consent is the appropriate consent` | poca-tests-consent.l4 |
| s 335(1)(b) | p7:342 | encoded | `s 335(1) the consent is the appropriate consent` | poca-tests-consent.l4 |
| s 335(1)(c) | p7:343 | encoded | `s 335(1) the consent is the appropriate consent` | poca-tests-consent.l4 |
| s 335(2) | p7:344-346 | encoded | `s 335(2) the person must be treated as having the appropriate consent` | poca-tests-consent.l4 |
| s 335(2)(a) | p7:345 | encoded | `s 335(2)(a) he makes an authorised disclosure to a constable or a customs officer` | poca-tests-consent.l4 |
| s 335(2)(b) | p7:346 | encoded | `s 335(2) the person must be treated as having the appropriate consent` | poca-tests-consent.l4 |
| s 335(3) | p7:347 | encoded | `s 335(3) the condition is satisfied` | poca-tests-consent.l4 |
| s 335(4) | p7:348-350 | encoded | `s 335(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 335(4)(a) | p7:349 | encoded | `s 335(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 335(4)(b) | p7:350 | encoded | `s 335(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 335(5) | p7:351 | encoded | `s 335(5) the first day of the notice period` ; `s 335(5) the last day of the notice period` | poca-tests-consent.l4 |
| s 335(5) “the notice period” | p7:351 | encoded | `s 335(5) the first day of the notice period` ; `s 335(5) the last day of the notice period` | poca-tests-consent.l4 |
| s 335(6) | p7:352 | encoded | `s 335(6) the last day of the moratorium period` | poca-tests-consent.l4 |
| s 335(6) “the moratorium period” | p7:352 | encoded | `s 335(6) the last day of the moratorium period` | poca-tests-consent.l4 |
| s 335(6A) | p7:353-355 | encoded | the extension of the moratorium period: input `the days by which the period has been extended under section 336A or 336C` of `s 335(6) the last day of the moratorium period`; the extension is worked out by the rules of ss 336A and 336C | poca-tests-consent.l4 |
| s 335(6A)(a) | p7:354 | encoded | the extension of the moratorium period: input `the days by which the period has been extended under section 336A or 336C` of `s 335(6) the last day of the moratorium period`; the extension is worked out by the rules of ss 336A and 336C | poca-tests-consent.l4 |
| s 335(6A)(b) | p7:355 | encoded | the extension of the moratorium period: input `the days by which the period has been extended under section 336A or 336C` of `s 335(6) the last day of the moratorium period`; the extension is worked out by the rules of ss 336A and 336C | poca-tests-consent.l4 |
| s 335(7) | p7:356 | encoded | `s 335(7) the day is a working day` | poca-tests-consent.l4 |
| s 335(7) “a working day” | p7:356 | encoded | `s 335(7) the day is a working day` | poca-tests-consent.l4 |
| s 335(8) | p7:357 | encoded | `s 335(8) the act is a prohibited act` | poca-tests-consent.l4 |
| s 335(8A) | p7:358-360 | encoded | as s 335(6A): the same cross-reference, for subsection (8) | poca-tests-consent.l4 |
| s 335(8A)(a) | p7:359 | encoded | as s 335(6A): the same cross-reference, for subsection (8) | poca-tests-consent.l4 |
| s 335(8A)(b) | p7:360 | encoded | as s 335(6A): the same cross-reference, for subsection (8) | poca-tests-consent.l4 |
| s 335(9) | p7:361 | encoded | `s 335(9) the person is a nominated officer` | poca-tests-consent.l4 |
| s 335(9) “a nominated officer” | p7:361 | encoded | `s 335(9) the person is a nominated officer` | poca-tests-consent.l4 |
| s 335(10) | p7:362 | inert: 1 not operative | says where subsections (1) to (4) are used ("for the purposes of this Part") (a lead-in or signpost that creates no rule) | - |
| s 336 | p7:363-385 | encoded | see the child rows | poca-tests-consent.l4 |
| s 336(1) | p7:364 | encoded | `s 336(1) the nominated officer is prohibited from giving the appropriate consent` ; `s 336(1) the nominated officer must not give the appropriate consent unless a condition is satisfied` | poca-tests-consent.l4 |
| s 336(2) | p7:365-367 | encoded | `s 336(2) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(2)(a) | p7:366 | encoded | `s 336(2) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(2)(b) | p7:367 | encoded | `s 336(2) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(3) | p7:368-370 | encoded | `s 336(3) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(3)(a) | p7:369 | encoded | `s 336(3) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(3)(b) | p7:370 | encoded | `s 336(3) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(4) | p7:371-374 | encoded | `s 336(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(4)(a) | p7:372 | encoded | `s 336(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(4)(b) | p7:373 | encoded | `s 336(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(4)(c) | p7:374 | encoded | `s 336(4) the condition is satisfied` | poca-tests-consent.l4 |
| s 336(5) | p7:375-377 | encoded | `s 336(5) the nominated officer commits an offence` | poca-tests-consent.l4 |
| s 336(5)(a) | p7:376 | encoded | `s 336(5) the nominated officer commits an offence` | poca-tests-consent.l4 |
| s 336(5)(b) | p7:377 | encoded | `s 336(5) the nominated officer commits an offence` | poca-tests-consent.l4 |
| s 336(6) | p7:378-380 | encoded | `s 336(6) the most that can be imposed on a person guilty of the offence` | poca-tests-consent.l4 |
| s 336(6)(a) | p7:379 | encoded | `s 336(6) the most that can be imposed on a person guilty of the offence` | poca-tests-consent.l4 |
| s 336(6)(b) | p7:380 | encoded | `s 336(6) the most that can be imposed on a person guilty of the offence` | poca-tests-consent.l4 |
| s 336(7) | p7:381 | encoded | `s 336(7) the last day of the notice period` | poca-tests-consent.l4 |
| s 336(7) “the notice period” | p7:381 | encoded | `s 336(7) the last day of the notice period` | poca-tests-consent.l4 |
| s 336(8) | p7:382 | encoded | `s 336(8) the last day of the moratorium period` | poca-tests-consent.l4 |
| s 336(8) “the moratorium period” | p7:382 | encoded | `s 336(8) the last day of the moratorium period` | poca-tests-consent.l4 |
| s 336(9) | p7:383 | encoded | `s 336(9) the day is a working day` | poca-tests-consent.l4 |
| s 336(9) “a working day” | p7:383 | encoded | `s 336(9) the day is a working day` | poca-tests-consent.l4 |
| s 336(10) | p7:384 | encoded | `s 336(10) the act is a prohibited act` | poca-tests-consent.l4 |
| s 336(11) | p7:385 | encoded | `s 336(11) the person is a nominated officer` | poca-tests-consent.l4 |
| s 336(11) “a nominated officer” | p7:385 | encoded | `s 336(11) the person is a nominated officer` | poca-tests-consent.l4 |
| s 336A | p7:386-410 | encoded | see the child rows | poca-tests-consent.l4 |
| s 336A(1) | p7:387-391 | encoded | `s 336A(1) the court may grant an extension of a moratorium period` | poca-tests-consent.l4 |
| s 336A(1)(a) | p7:388 | encoded | `s 336A(1) the court may grant an extension of a moratorium period` | poca-tests-consent.l4 |
| s 336A(1)(b) | p7:389 | encoded | `s 336A(1) the court may grant an extension of a moratorium period` | poca-tests-consent.l4 |
| s 336A(1)(c) | p7:390 | encoded | `s 336A(1) the court may grant an extension of a moratorium period` | poca-tests-consent.l4 |
| s 336A(1)(d) | p7:391 | encoded | `s 336A(1) the court may grant an extension of a moratorium period` | poca-tests-consent.l4 |
| s 336A(2) | p7:392 | encoded | `s 336A(2) the person may make an application under this section` | poca-tests-consent.l4 |
| s 336A(3) | p7:393 | encoded | `s 336A(3) the application is made in time` | poca-tests-consent.l4 |
| s 336A(4) | p7:394 | encoded | `s 336A(4) the latest day on which an extension may end` ; `s 336A(4) the extension ends in time` | poca-tests-consent.l4 |
| s 336A(5) | p7:395 | encoded | `s 336A(5) the court may further extend the moratorium period` | poca-tests-consent.l4 |
| s 336A(6) | p7:396 | encoded | `s 336A(6) the court may further extend a period extended under section 336C` | poca-tests-consent.l4 |
| s 336A(7) | p7:397 | encoded | `s 336A(7) the court may grant a further extension` ; `s 336A(7) the latest day to which the moratorium period may be extended in total` ; `s 336A(7) the court may grant a further extension to that day` | poca-tests-consent.l4 |
| s 336A(8) | p7:398 | encoded | `s 336A(8) subsections (1) to (4) apply to the extension` | poca-tests-consent.l4 |
| s 336A(9) | p7:399-401 | encoded | `s 336A(9) an immigration officer may make an application` | poca-tests-consent.l4 |
| s 336A(9)(a) | p7:400 | encoded | `s 336A(9) an immigration officer may make an application` | poca-tests-consent.l4 |
| s 336A(9)(b) | p7:401 | encoded | `s 336A(9) an immigration officer may make an application` | poca-tests-consent.l4 |
| s 336A(10) | p7:402-410 | encoded | `s 336A(10) the enactment is a relevant nationality enactment` | poca-tests-consent.l4 |
| s 336A(10) “prohibited act” | p7:403 | encoded | `s 336A(10) the enactment is a relevant nationality enactment` | poca-tests-consent.l4 |
| s 336A(10) “relevant nationality enactment” | p7:404 | encoded | `s 336A(10) the enactment is a relevant nationality enactment` | poca-tests-consent.l4 |
| s 336B | p7:411-435 | encoded | see the child rows | poca-tests-consent.l4 |
| s 336B(1) | p7:412 | inert: 1 not operative | a lead-in: says the section applies to proceedings on an application under s 336A, and creates no rule | - |
| s 336B(2) | p7:413 | encoded | `s 336B(2) the court has determined the proceedings as it must` | poca-tests-consent.l4 |
| s 336B(3) | p7:414-416 | encoded | `s 336B(3) the court may exclude the person from any part of the hearing` | poca-tests-consent.l4 |
| s 336B(3)(a) | p7:415 | encoded | `s 336B(3) the court may exclude the person from any part of the hearing` | poca-tests-consent.l4 |
| s 336B(3)(b) | p7:416 | encoded | `s 336B(3) the court may exclude the person from any part of the hearing` | poca-tests-consent.l4 |
| s 336B(4) | p7:417-419 | encoded | `s 336B(4) the person may apply for an order that the information be withheld from an interested person` | poca-tests-consent.l4 |
| s 336B(4)(a) | p7:418 | encoded | `s 336B(4) the person may apply for an order that the information be withheld from an interested person` | poca-tests-consent.l4 |
| s 336B(4)(b) | p7:419 | encoded | `s 336B(4) the person may apply for an order that the information be withheld from an interested person` | poca-tests-consent.l4 |
| s 336B(5) | p7:420-425 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(5)(a) | p7:421 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(5)(b) | p7:422 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(5)(c) | p7:423 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(5)(d) | p7:424 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(5)(e) | p7:425 | encoded | `s 336B(5) the court may make an order that the information be withheld` | poca-tests-consent.l4 |
| s 336B(6) | p7:426-428 | encoded | `s 336B(6) the court must direct that the person be excluded from the hearing` | poca-tests-consent.l4 |
| s 336B(6)(a) | p7:427 | encoded | `s 336B(6) the court must direct that the person be excluded from the hearing` | poca-tests-consent.l4 |
| s 336B(6)(b) | p7:428 | encoded | `s 336B(6) the court must direct that the person be excluded from the hearing` | poca-tests-consent.l4 |
| s 336B(7) | p7:429 | inert: 2 machinery | rules of court may make provision as to practice and procedure | - |
| s 336B(8) | p7:430 | encoded | `s 336B(8) an appeal lies to the appropriate appeal court` | poca-tests-consent.l4 |
| s 336B(9) | p7:431 | encoded | `s 336B(9) the appropriate appeal court may make the order` | poca-tests-consent.l4 |
| s 336B(10) | p7:432-434 | encoded | `s 336B(10) the appropriate appeal court` | poca-tests-consent.l4 |
| s 336B(10)(a) | p7:433 | encoded | `s 336B(10) the appropriate appeal court` | poca-tests-consent.l4 |
| s 336B(10)(b) | p7:434 | encoded | `s 336B(10) the appropriate appeal court` | poca-tests-consent.l4 |
| s 336B(11) | p7:435 | encoded | `s 336B(11) there is a right of appeal from the decision` | poca-tests-consent.l4 |
| s 336C | p7:436-454 | encoded | see the child rows | poca-tests-consent.l4 |
| s 336C(1) | p7:437-439 | encoded | the conditions of (1) are the inputs of `s 336C(2) the last day of the moratorium period extended pending the application` | poca-tests-consent.l4 |
| s 336C(1)(a) | p7:438 | encoded | the conditions of (1) are the inputs of `s 336C(2) the last day of the moratorium period extended pending the application` | poca-tests-consent.l4 |
| s 336C(1)(b) | p7:439 | encoded | the conditions of (1) are the inputs of `s 336C(2) the last day of the moratorium period extended pending the application` | poca-tests-consent.l4 |
| s 336C(2) | p7:440 | encoded | `s 336C(2) the last day of the moratorium period extended pending the application` | poca-tests-consent.l4 |
| s 336C(3) | p7:441-443 | encoded | the conditions of (3) are the inputs of `s 336C(4) the last day of the moratorium period extended pending the appeal` | poca-tests-consent.l4 |
| s 336C(3)(a) | p7:442 | encoded | the conditions of (3) are the inputs of `s 336C(4) the last day of the moratorium period extended pending the appeal` | poca-tests-consent.l4 |
| s 336C(3)(b) | p7:443 | encoded | the conditions of (3) are the inputs of `s 336C(4) the last day of the moratorium period extended pending the appeal` | poca-tests-consent.l4 |
| s 336C(4) | p7:444 | encoded | `s 336C(4) the last day of the moratorium period extended pending the appeal` | poca-tests-consent.l4 |
| s 336C(5) | p7:445 | encoded | `s 336C(5) the earlier of the day the proceedings end and the cap` | poca-tests-consent.l4 |
| s 336C(6) | p7:446-449 | encoded | `s 336C(6) the moratorium period is extended in accordance with subsection (7)` | poca-tests-consent.l4 |
| s 336C(6)(a) | p7:447 | encoded | `s 336C(6) the moratorium period is extended in accordance with subsection (7)` | poca-tests-consent.l4 |
| s 336C(6)(b) | p7:448 | encoded | `s 336C(6) the moratorium period is extended in accordance with subsection (7)` | poca-tests-consent.l4 |
| s 336C(6)(c) | p7:449 | encoded | `s 336C(6) the moratorium period is extended in accordance with subsection (7)` | poca-tests-consent.l4 |
| s 336C(7) | p7:450-452 | encoded | `s 336C(7) the day until which the moratorium period is extended` | poca-tests-consent.l4 |
| s 336C(7)(a) | p7:451 | encoded | `s 336C(7) the day until which the moratorium period is extended` | poca-tests-consent.l4 |
| s 336C(7)(b) | p7:452 | encoded | `s 336C(7) the day until which the moratorium period is extended` | poca-tests-consent.l4 |
| s 336C(8) | p7:453 | encoded | `s 336C(8) the last day of the 5 day period` | poca-tests-consent.l4 |
| s 336C(8) “5 day period” | p7:453 | encoded | `s 336C(8) the last day of the 5 day period` | poca-tests-consent.l4 |
| s 336C(9) | p7:454 | encoded | `s 336C(9) the extension is within the restriction in section 336A(7)` | poca-tests-consent.l4 |
| s 336D | p7:455-483 | encoded | see the child rows | poca-tests-consent.l4 |
| s 336D(1) | p7:456 | inert: 1 not operative | a lead-in: says what the section provides (the meaning of terms), and creates no rule | - |
| s 336D(2) | p7:457-459 | encoded | `s 336D(2) the court` | poca-tests-consent.l4 |
| s 336D(2) “The court” | p7:457 | encoded | `s 336D(2) the court` | poca-tests-consent.l4 |
| s 336D(2) “the court” | p7:457 | encoded | `s 336D(2) the court` | poca-tests-consent.l4 |
| s 336D(2)(a) | p7:458 | encoded | `s 336D(2) the court` | poca-tests-consent.l4 |
| s 336D(2)(b) | p7:459 | encoded | `s 336D(2) the court` | poca-tests-consent.l4 |
| s 336D(3) | p7:460-462 | encoded | `s 336D(3) the person is an interested person` | poca-tests-consent.l4 |
| s 336D(3) “Interested person” | p7:460 | encoded | `s 336D(3) the person is an interested person` | poca-tests-consent.l4 |
| s 336D(3) “interested person” | p7:460 | encoded | `s 336D(3) the person is an interested person` | poca-tests-consent.l4 |
| s 336D(3)(a) | p7:461 | encoded | `s 336D(3) the person is an interested person` | poca-tests-consent.l4 |
| s 336D(3)(b) | p7:462 | encoded | `s 336D(3) the person is an interested person` | poca-tests-consent.l4 |
| s 336D(4) | p7:463 | encoded | `s 336D(4) the period is a moratorium period` | poca-tests-consent.l4 |
| s 336D(4) “Moratorium period” | p7:463 | encoded | `s 336D(4) the period is a moratorium period` | poca-tests-consent.l4 |
| s 336D(4) “moratorium period” | p7:463 | encoded | `s 336D(4) the period is a moratorium period` | poca-tests-consent.l4 |
| s 336D(5) | p7:464-466 | encoded | `s 336D(5) the relevant disclosure` | poca-tests-consent.l4 |
| s 336D(5) “Relevant disclosure” | p7:464 | encoded | `s 336D(5) the relevant disclosure` | poca-tests-consent.l4 |
| s 336D(5) “relevant disclosure” | p7:464 | encoded | `s 336D(5) the relevant disclosure` | poca-tests-consent.l4 |
| s 336D(5)(a) | p7:465 | encoded | `s 336D(5) the relevant disclosure` | poca-tests-consent.l4 |
| s 336D(5)(b) | p7:466 | encoded | `s 336D(5) the relevant disclosure` | poca-tests-consent.l4 |
| s 336D(6) | p7:467 | encoded | `s 336D(6) the property is relevant property` | poca-tests-consent.l4 |
| s 336D(6) “Relevant property” | p7:467 | encoded | `s 336D(6) the property is relevant property` | poca-tests-consent.l4 |
| s 336D(6) “relevant property” | p7:467 | encoded | `s 336D(6) the property is relevant property` | poca-tests-consent.l4 |
| s 336D(7) | p7:468-476 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7) “senior officer” | p7:468 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7) “senior officer (Crown Court)” | p7:468 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(a) | p7:469 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(b) | p7:470 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(c) | p7:471 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(d) | p7:472 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(e) | p7:473 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(f) | p7:474 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(g) | p7:475 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(7)(h) | p7:476 | encoded | `s 336D(7) the officer is a senior officer for an application to the Crown Court` | poca-tests-consent.l4 |
| s 336D(8) | p7:477 | encoded | `s 336D(8) the officer is a senior officer for an application to the sheriff` | poca-tests-consent.l4 |
| s 336D(8) “senior officer” | p7:477 | encoded | `s 336D(8) the officer is a senior officer for an application to the sheriff` | poca-tests-consent.l4 |
| s 336D(8) “senior officer (sheriff)” | p7:477 | encoded | `s 336D(8) the officer is a senior officer for an application to the sheriff` | poca-tests-consent.l4 |
| s 336D(9) | p7:478-483 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9) “Working day” | p7:478 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9) “working day” | p7:478 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9)(a) | p7:479 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9)(b) | p7:480 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9)(c) | p7:481 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9)(d) | p7:482 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| s 336D(9)(e) | p7:483 | encoded | `s 336D(9) the day is a working day` | poca-tests-consent.l4 |
| part 7 heading "Disclosures" | p7:484 | inert: 1 not operative | a cross-heading | - |
| s 337 | p7:485-499 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 337(1) | p7:486 | encoded | `s 337(1) the disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 337(2) | p7:487 | encoded | `s 337(2) the first condition is satisfied` | poca-tests-disclose.l4 |
| s 337(3) | p7:488-491 | encoded | `s 337(3) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 337(3)(a) | p7:489 | encoded | `s 337(3) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 337(3)(b) | p7:490-491 | encoded | `s 337(3) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 337(4) | p7:492 | encoded | `s 337(4) the third condition is satisfied` | poca-tests-disclose.l4 |
| s 337(4A) | p7:493-496 | encoded | `s 337(4A) the further disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 337(4A)(a) | p7:494 | encoded | `s 337(4A) the further disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 337(4A)(b) | p7:495-496 | encoded | `s 337(4A) the further disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 337(5) | p7:497-499 | encoded | `s 337(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 337(5) “a disclosure to a nominated officer” | p7:497 | encoded | `s 337(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 337(5)(a) | p7:498 | encoded | `s 337(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 337(5)(b) | p7:499 | encoded | `s 337(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 338 | p7:500-519 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 338(1) | p7:501-504 | encoded | `s 338(1) the disclosure is authorised` | poca-tests-disclose.l4 |
| s 338(1)(a) | p7:502 | encoded | `s 338(1) the disclosure is authorised` | poca-tests-disclose.l4 |
| s 338(1)(b) | p7:503 | repealed or blank in this text | shown as dots (line 503) | - |
| s 338(1)(c) | p7:504 | encoded | `s 338(1) the disclosure is authorised` | poca-tests-disclose.l4 |
| s 338(2) | p7:505 | encoded | `s 338(2) the first condition is satisfied` | poca-tests-disclose.l4 |
| s 338(2A) | p7:506-509 | encoded | `s 338(2A) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 338(2A)(a) | p7:507 | encoded | `s 338(2A) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 338(2A)(b) | p7:508 | encoded | `s 338(2A) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 338(2A)(c) | p7:509 | encoded | `s 338(2A) the second condition is satisfied` | poca-tests-disclose.l4 |
| s 338(3) | p7:510-513 | encoded | `s 338(3) the third condition is satisfied` | poca-tests-disclose.l4 |
| s 338(3)(a) | p7:511 | encoded | `s 338(3) the third condition is satisfied` | poca-tests-disclose.l4 |
| s 338(3)(b) | p7:512 | encoded | `s 338(3) the third condition is satisfied` | poca-tests-disclose.l4 |
| s 338(3)(c) | p7:513 | encoded | `s 338(3) the third condition is satisfied` | poca-tests-disclose.l4 |
| s 338(4) | p7:514 | encoded | `s 338(4) the authorised disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 338(4A) | p7:515 | encoded | `s 338(4A) no civil liability arises in respect of the disclosure` | poca-tests-disclose.l4 |
| s 338(5) | p7:516-518 | encoded | `s 338(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 338(5) “a disclosure to a nominated officer” | p7:516 | encoded | `s 338(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 338(5)(a) | p7:517 | encoded | `s 338(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 338(5)(b) | p7:518 | encoded | `s 338(5) the disclosure is a disclosure to a nominated officer` | poca-tests-disclose.l4 |
| s 338(6) | p7:519 | encoded | `s 338(6) the act is the prohibited act` | poca-tests-disclose.l4 |
| s 339 | p7:520-531 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339(1) | p7:521 | encoded | `s 339(1) the person may by order prescribe the form and manner of the disclosure` | poca-tests-disclose.l4 |
| s 339(1A) | p7:522 | encoded | `s 339(1A) the person commits an offence` ; `s 339(1A) the person must not make a disclosure otherwise than in the prescribed form or manner unless he has a reasonable excuse` | poca-tests-disclose.l4 |
| s 339(1B) | p7:523 | encoded | a branch of `s 339(1A) the person commits an offence` (the reasonable-excuse exception) and of its regulative twin | poca-tests-disclose.l4 |
| s 339(2) | p7:524 | inert: 2 machinery | says what the power to prescribe the form includes (a request for information); the effect on the individual is in subsections (3) and (4) | - |
| s 339(3) | p7:525-527 | encoded | `s 339(3) the form complies with the requirements for a form that includes a request` | poca-tests-disclose.l4 |
| s 339(3)(a) | p7:526 | encoded | `s 339(3) the form complies with the requirements for a form that includes a request` | poca-tests-disclose.l4 |
| s 339(3)(b) | p7:527 | encoded | `s 339(3) the form complies with the requirements for a form that includes a request` | poca-tests-disclose.l4 |
| s 339(4) | p7:528 | encoded | `s 339(4) the disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-tests-disclose.l4 |
| s 339(5) | p7:529 | repealed or blank in this text | shown as dots only (line 529) | - |
| s 339(6) | p7:530 | repealed or blank in this text | shown as dots only (line 530) | - |
| s 339(7) | p7:531 | encoded | `s 339(7) subsection (2) does not apply to the disclosure` | poca-tests-disclose.l4 |
| s 339ZA | p7:532-533 | encoded | `s 339ZA the constable or officer of Revenue and Customs must disclose it in full to an authorised person` ; `s 339ZA the constable or officer of Revenue and Customs must disclose the disclosure in full to an authorised person` | poca-tests-disclose.l4 |
| s 339ZB | p7:534-545 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZB(1) | p7:535 | encoded | `s 339ZB(1) A may disclose information to one or more other persons` | poca-tests-disclose.l4 |
| s 339ZB(2) | p7:536-539 | encoded | `s 339ZB(2) condition 1 is met` | poca-tests-disclose.l4 |
| s 339ZB(2)(a) | p7:537 | encoded | `s 339ZB(2) condition 1 is met` | poca-tests-disclose.l4 |
| s 339ZB(2)(b) | p7:538 | encoded | `s 339ZB(2) condition 1 is met` | poca-tests-disclose.l4 |
| s 339ZB(2)(c) | p7:539 | encoded | `s 339ZB(2) condition 1 is met` | poca-tests-disclose.l4 |
| s 339ZB(3) | p7:540-542 | encoded | `s 339ZB(3) condition 2 is met` | poca-tests-disclose.l4 |
| s 339ZB(3)(a) | p7:541 | encoded | `s 339ZB(3) condition 2 is met` | poca-tests-disclose.l4 |
| s 339ZB(3)(b) | p7:542 | encoded | `s 339ZB(3) condition 2 is met` | poca-tests-disclose.l4 |
| s 339ZB(4) | p7:543 | encoded | `s 339ZB(4) condition 3 is met` | poca-tests-disclose.l4 |
| s 339ZB(5) | p7:544 | encoded | `s 339ZB(5) condition 4 is met` | poca-tests-disclose.l4 |
| s 339ZB(6) | p7:545 | encoded | `s 339ZB(6) the person may disclose information to A for the purposes of making a disclosure request` | poca-tests-disclose.l4 |
| s 339ZC | p7:546-563 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZC(1) | p7:547-551 | encoded | `s 339ZC(1) the disclosure request has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(1)(a) | p7:548 | encoded | `s 339ZC(1) the disclosure request has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(1)(b) | p7:549 | encoded | `s 339ZC(1) the disclosure request has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(1)(c) | p7:550 | encoded | `s 339ZC(1) the disclosure request has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(1)(d) | p7:551 | encoded | `s 339ZC(1) the disclosure request has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(2) | p7:552-554 | encoded | `s 339ZC(2) the disclosure request has the further content it must have` | poca-tests-disclose.l4 |
| s 339ZC(2)(a) | p7:553 | encoded | `s 339ZC(2) the disclosure request has the further content it must have` | poca-tests-disclose.l4 |
| s 339ZC(2)(b) | p7:554 | encoded | `s 339ZC(2) the disclosure request has the further content it must have` | poca-tests-disclose.l4 |
| s 339ZC(3) | p7:555-557 | encoded | `s 339ZC(3) who must make the required notification` | poca-tests-disclose.l4 |
| s 339ZC(3)(a) | p7:556 | encoded | `s 339ZC(3) who must make the required notification` | poca-tests-disclose.l4 |
| s 339ZC(3)(b) | p7:557 | encoded | `s 339ZC(3) who must make the required notification` | poca-tests-disclose.l4 |
| s 339ZC(4) | p7:558 | encoded | `s 339ZC(4) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(5) | p7:559-563 | encoded | `s 339ZC(5) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(5)(a) | p7:560 | encoded | `s 339ZC(5) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(5)(b) | p7:561 | encoded | `s 339ZC(5) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(5)(c) | p7:562 | encoded | `s 339ZC(5) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZC(5)(d) | p7:563 | encoded | `s 339ZC(5) the required notification has the content it must have` | poca-tests-disclose.l4 |
| s 339ZD | p7:564-592 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZD(1) | p7:565-568 | encoded | the scope of the section: the input `a question arises in proceedings ...` of `s 339ZD(2)` and `s 339ZD(3)` | poca-tests-disclose.l4 |
| s 339ZD(1)(a) | p7:566 | encoded | the scope of the section: the input `a question arises in proceedings ...` of `s 339ZD(2)` and `s 339ZD(3)` | poca-tests-disclose.l4 |
| s 339ZD(1)(b) | p7:567 | encoded | the scope of the section: the input `a question arises in proceedings ...` of `s 339ZD(2)` and `s 339ZD(3)` | poca-tests-disclose.l4 |
| s 339ZD(1)(c) | p7:568 | encoded | the scope of the section: the input `a question arises in proceedings ...` of `s 339ZD(2)` and `s 339ZD(3)` | poca-tests-disclose.l4 |
| s 339ZD(2) | p7:569-570 | encoded | `s 339ZD(2) the required notification is treated as satisfying the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZD(3) | p7:571-572 | encoded | `s 339ZD(3) the joint disclosure report is treated as satisfying the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZD(4) | p7:573-577 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(4) “a joint disclosure report” | p7:573 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(4)(a) | p7:574 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(4)(b) | p7:575 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(4)(c) | p7:576 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(4)(d) | p7:577 | encoded | `s 339ZD(4) the report is a joint disclosure report` | poca-tests-disclose.l4 |
| s 339ZD(5) | p7:578-582 | encoded | `s 339ZD(5) the report satisfies the requirements as to content` | poca-tests-disclose.l4 |
| s 339ZD(5)(a) | p7:579 | encoded | `s 339ZD(5) the report satisfies the requirements as to content` | poca-tests-disclose.l4 |
| s 339ZD(5)(b) | p7:580 | encoded | `s 339ZD(5) the report satisfies the requirements as to content` | poca-tests-disclose.l4 |
| s 339ZD(5)(c) | p7:581 | encoded | `s 339ZD(5) the report satisfies the requirements as to content` | poca-tests-disclose.l4 |
| s 339ZD(5)(d) | p7:582 | encoded | `s 339ZD(5) the report satisfies the requirements as to content` | poca-tests-disclose.l4 |
| s 339ZD(6) | p7:583-585 | encoded | `s 339ZD(6) the last day of the applicable period` | poca-tests-disclose.l4 |
| s 339ZD(6) “the applicable period” | p7:583 | encoded | `s 339ZD(6) the last day of the applicable period` | poca-tests-disclose.l4 |
| s 339ZD(6)(a) | p7:584 | encoded | `s 339ZD(6) the last day of the applicable period` | poca-tests-disclose.l4 |
| s 339ZD(6)(b) | p7:585 | encoded | `s 339ZD(6) the last day of the applicable period` | poca-tests-disclose.l4 |
| s 339ZD(7) | p7:586-589 | encoded | `s 339ZD(7) the joint disclosure report is approved and signed as required` | poca-tests-disclose.l4 |
| s 339ZD(7)(a) | p7:587 | encoded | `s 339ZD(7) the joint disclosure report is approved and signed as required` | poca-tests-disclose.l4 |
| s 339ZD(7)(b) | p7:588-589 | encoded | `s 339ZD(7) the joint disclosure report is approved and signed as required` | poca-tests-disclose.l4 |
| s 339ZD(8) | p7:590-592 | encoded | `s 339ZD(8) the person is within the references to A, B or C` | poca-tests-disclose.l4 |
| s 339ZD(8)(a) | p7:591 | encoded | `s 339ZD(8) the person is within the references to A, B or C` | poca-tests-disclose.l4 |
| s 339ZD(8)(b) | p7:592 | encoded | `s 339ZD(8) the person is within the references to A, B or C` | poca-tests-disclose.l4 |
| s 339ZE | p7:593-614 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZE(1) | p7:594 | encoded | the case in which A makes the required notification: the input `the required notification is made by A` of `s 339ZE(2)` and `s 339ZE(3)` | poca-tests-disclose.l4 |
| s 339ZE(2) | p7:595-597 | encoded | `s 339ZE(2) section 339ZD(2) has effect on the requirement in the case of A, B or C` | poca-tests-disclose.l4 |
| s 339ZE(2)(a) | p7:596 | encoded | `s 339ZE(2) section 339ZD(2) has effect on the requirement in the case of A, B or C` | poca-tests-disclose.l4 |
| s 339ZE(2)(b) | p7:597 | encoded | `s 339ZE(2) section 339ZD(2) has effect on the requirement in the case of A, B or C` | poca-tests-disclose.l4 |
| s 339ZE(3) | p7:598 | encoded | `s 339ZE(3) section 339ZD(2) removes the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(4) | p7:599 | encoded | the case in which B makes the required notification: the input `the required notification is made by B` of `s 339ZE(5)` to `s 339ZE(7)` | poca-tests-disclose.l4 |
| s 339ZE(5) | p7:600-602 | encoded | `s 339ZE(5) section 339ZD(2) has effect on the requirement in the case of A or C` | poca-tests-disclose.l4 |
| s 339ZE(5)(a) | p7:601 | encoded | `s 339ZE(5) section 339ZD(2) has effect on the requirement in the case of A or C` | poca-tests-disclose.l4 |
| s 339ZE(5)(b) | p7:602 | encoded | `s 339ZE(5) section 339ZD(2) has effect on the requirement in the case of A or C` | poca-tests-disclose.l4 |
| s 339ZE(6) | p7:603 | encoded | `s 339ZE(6) section 339ZD(2) removes the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(7) | p7:604-606 | encoded | `s 339ZE(7) section 339ZD(2) has effect on the requirement in the case of B` | poca-tests-disclose.l4 |
| s 339ZE(7)(a) | p7:605 | encoded | `s 339ZE(7) section 339ZD(2) has effect on the requirement in the case of B` | poca-tests-disclose.l4 |
| s 339ZE(7)(b) | p7:606 | encoded | `s 339ZE(7) section 339ZD(2) has effect on the requirement in the case of B` | poca-tests-disclose.l4 |
| s 339ZE(8) | p7:607-609 | encoded | `s 339ZE(8) section 339ZD(2) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(8)(a) | p7:608 | encoded | `s 339ZE(8) section 339ZD(2) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(8)(b) | p7:609 | encoded | `s 339ZE(8) section 339ZD(2) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(9) | p7:610 | encoded | `s 339ZE(9) the person who made the required notification must notify an NCA authorised officer that a report is not being made` ; `s 339ZE(9) the person who made the required notification must notify an NCA authorised officer that a report is not being made` | poca-tests-disclose.l4 |
| s 339ZE(10) | p7:611-613 | encoded | `s 339ZE(10) section 339ZD(3) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(10)(a) | p7:612 | encoded | `s 339ZE(10) section 339ZD(3) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(10)(b) | p7:613 | encoded | `s 339ZE(10) section 339ZD(3) has effect on the requirement to make the required disclosure` | poca-tests-disclose.l4 |
| s 339ZE(11) | p7:614 | inert: 1 not operative | says that terms in the section have the meanings they have in s 339ZD (a lead-in or signpost that creates no rule) | - |
| s 339ZF | p7:615-630 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZF(1) | p7:616-619 | encoded | `s 339ZF(1) the relevant disclosure does not breach an obligation of confidence or another restriction on disclosure` | poca-tests-disclose.l4 |
| s 339ZF(1)(a) | p7:617 | encoded | `s 339ZF(1) the relevant disclosure does not breach an obligation of confidence or another restriction on disclosure` | poca-tests-disclose.l4 |
| s 339ZF(1)(b) | p7:618-619 | encoded | `s 339ZF(1) the relevant disclosure does not breach an obligation of confidence or another restriction on disclosure` | poca-tests-disclose.l4 |
| s 339ZF(2) | p7:620 | encoded | `s 339ZF(2) the relevant disclosure may not include the information` ; `s 339ZF(2) a relevant disclosure must not include information obtained from a UK law enforcement agency unless it consents` | poca-tests-disclose.l4 |
| s 339ZF(3) | p7:621-623 | encoded | `s 339ZF(3)(a)` and `s 339ZF(3)(b)` | poca-tests-disclose.l4 |
| s 339ZF(3) “the undertaking” | p7:621 | encoded | `s 339ZF(3)(a)` and `s 339ZF(3)(b)` | poca-tests-disclose.l4 |
| s 339ZF(3)(a) | p7:622 | encoded | `s 339ZF(3)(a) the relevant disclosure by the undertaking is made as required` | poca-tests-disclose.l4 |
| s 339ZF(3)(b) | p7:623 | encoded | `s 339ZF(3)(b) the relevant disclosure to the undertaking is made as required` | poca-tests-disclose.l4 |
| s 339ZF(4) | p7:624 | encoded | `s 339ZF(4) subsection (1) applies whether or not the conditions in section 339ZB were met` | poca-tests-disclose.l4 |
| s 339ZF(5) | p7:625-630 | encoded | `s 339ZF(5) the disclosure is a relevant disclosure` ; `s 339ZF(5) the body is a UK law enforcement agency` | poca-tests-disclose.l4 |
| s 339ZF(5) “relevant disclosure” | p7:626 | encoded | `s 339ZF(5) the disclosure is a relevant disclosure` ; `s 339ZF(5) the body is a UK law enforcement agency` | poca-tests-disclose.l4 |
| s 339ZF(5) “UK law enforcement agency” | p7:627 | encoded | `s 339ZF(5) the disclosure is a relevant disclosure` ; `s 339ZF(5) the body is a UK law enforcement agency` | poca-tests-disclose.l4 |
| s 339ZG | p7:631-648 | encoded | see the child rows | poca-tests-disclose.l4 |
| s 339ZG(1) | p7:632 | inert: 1 not operative | says where the section's definitions are used (a lead-in or signpost that creates no rule) | - |
| s 339ZG(2) | p7:633 | encoded | `s 339ZG(2) the request is a disclosure request` | poca-tests-disclose.l4 |
| s 339ZG(2) “Disclosure request” | p7:633 | encoded | `s 339ZG(2) the request is a disclosure request` | poca-tests-disclose.l4 |
| s 339ZG(2) “disclosure request” | p7:633 | encoded | `s 339ZG(2) the request is a disclosure request` | poca-tests-disclose.l4 |
| s 339ZG(3) | p7:634 | encoded | `s 339ZG(3) the person is an NCA authorised officer` | poca-tests-disclose.l4 |
| s 339ZG(3) “NCA authorised officer” | p7:634 | encoded | `s 339ZG(3) the person is an NCA authorised officer` | poca-tests-disclose.l4 |
| s 339ZG(4) | p7:635 | encoded | `s 339ZG(4) the person is a nominated officer` | poca-tests-disclose.l4 |
| s 339ZG(4) “Nominated officer” | p7:635 | encoded | `s 339ZG(4) the person is a nominated officer` | poca-tests-disclose.l4 |
| s 339ZG(4) “nominated officer” | p7:635 | encoded | `s 339ZG(4) the person is a nominated officer` | poca-tests-disclose.l4 |
| s 339ZG(5) | p7:636-641 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5) “Relevant undertaking” | p7:636 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5) “relevant undertaking” | p7:636 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5)(a) | p7:637 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5)(b) | p7:638 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5)(c) | p7:639 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5)(d) | p7:640 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(5)(e) | p7:641 | encoded | `s 339ZG(5) the undertaking is a relevant undertaking` | poca-tests-disclose.l4 |
| s 339ZG(6) | p7:642 | encoded | `s 339ZG(6) the disclosure is the required disclosure` | poca-tests-disclose.l4 |
| s 339ZG(6) “Required disclosure” | p7:642 | encoded | `s 339ZG(6) the disclosure is the required disclosure` | poca-tests-disclose.l4 |
| s 339ZG(6) “required disclosure” | p7:642 | encoded | `s 339ZG(6) the disclosure is the required disclosure` | poca-tests-disclose.l4 |
| s 339ZG(7) | p7:643 | encoded | `s 339ZG(7) the notification is a required notification` | poca-tests-disclose.l4 |
| s 339ZG(7) “Required notification” | p7:643 | encoded | `s 339ZG(7) the notification is a required notification` | poca-tests-disclose.l4 |
| s 339ZG(7) “required notification” | p7:643 | encoded | `s 339ZG(7) the notification is a required notification` | poca-tests-disclose.l4 |
| s 339ZG(8) | p7:644-647 | encoded | `s 339ZG(8)(a)`, `s 339ZG(8)(b)`, `s 339ZG(8)(c)` | poca-tests-disclose.l4 |
| s 339ZG(8)(a) | p7:645 | encoded | `s 339ZG(8)(a) the undertaking is a credit institution` | poca-tests-disclose.l4 |
| s 339ZG(8)(a) “credit institution” | p7:645 | encoded | `s 339ZG(8)(a) the undertaking is a credit institution` | poca-tests-disclose.l4 |
| s 339ZG(8)(b) | p7:646 | encoded | `s 339ZG(8)(b) the undertaking is a financial institution` | poca-tests-disclose.l4 |
| s 339ZG(8)(b) “financial institution” | p7:646 | encoded | `s 339ZG(8)(b) the undertaking is a financial institution` | poca-tests-disclose.l4 |
| s 339ZG(8)(c) | p7:647 | encoded | `s 339ZG(8)(c) the person is a relevant professional adviser` | poca-tests-disclose.l4 |
| s 339ZG(8)(c) “relevant professional adviser” | p7:647 | encoded | `s 339ZG(8)(c) the person is a relevant professional adviser` | poca-tests-disclose.l4 |
| s 339ZG(9) | p7:648 | encoded | `s 339ZG(9) the business is a business in the regulated sector` | poca-tests-disclose.l4 |
| part 7 heading "Information orders" | p7:649 | inert: 1 not operative | a cross-heading | - |
| s 339ZH | p7:650-711 | encoded | see the child rows | poca-tests-orders.l4 |
| s 339ZH(1) | p7:651 | encoded | `s 339ZH(1) the court may make an information order` | poca-tests-orders.l4 |
| s 339ZH(2) | p7:652-654 | encoded | `s 339ZH(2) the application has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(2)(a) | p7:653 | encoded | `s 339ZH(2) the application has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(2)(b) | p7:654 | encoded | `s 339ZH(2) the application has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(2)(b) “the respondent” | p7:654 | encoded | `s 339ZH(2) the application has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(3) | p7:655-658 | encoded | `s 339ZH(3) the information order requires the respondent to provide the information` | poca-tests-orders.l4 |
| s 339ZH(3)(a) | p7:656 | encoded | `s 339ZH(3) the information order requires the respondent to provide the information` | poca-tests-orders.l4 |
| s 339ZH(3)(b) | p7:657-658 | encoded | `s 339ZH(3) the information order requires the respondent to provide the information` | poca-tests-orders.l4 |
| s 339ZH(4) | p7:659-663 | encoded | `s 339ZH(4) condition 1 is met` | poca-tests-orders.l4 |
| s 339ZH(4)(a) | p7:660 | encoded | `s 339ZH(4) condition 1 is met` | poca-tests-orders.l4 |
| s 339ZH(4)(b) | p7:661 | encoded | `s 339ZH(4) condition 1 is met` | poca-tests-orders.l4 |
| s 339ZH(4)(c) | p7:662 | encoded | `s 339ZH(4) condition 1 is met` | poca-tests-orders.l4 |
| s 339ZH(4)(d) | p7:663 | encoded | `s 339ZH(4) condition 1 is met` | poca-tests-orders.l4 |
| s 339ZH(5) | p7:664-669 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(5)(a) | p7:665 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(5)(b) | p7:666 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(5)(c) | p7:667 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(5)(d) | p7:668 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(5)(e) | p7:669 | encoded | `s 339ZH(5) condition 2 is met` | poca-tests-orders.l4 |
| s 339ZH(6) | p7:670 | encoded | `s 339ZH(6) the request is an external request` | poca-tests-orders.l4 |
| s 339ZH(6) “external request” | p7:670 | encoded | `s 339ZH(6) the request is an external request` | poca-tests-orders.l4 |
| s 339ZH(6A) | p7:671-681 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6A)(a) | p7:672-675 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6A)(b) | p7:676 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6A)(c) | p7:677 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6A)(d) | p7:678-680 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6A)(e) | p7:681 | encoded | `s 339ZH(6A) condition 3 is met` | poca-tests-orders.l4 |
| s 339ZH(6B) | p7:682-694 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(a) | p7:683 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(b) | p7:684-687 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(c) | p7:688 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(d) | p7:689 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(e) | p7:690 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(f) | p7:691-693 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(6B)(g) | p7:694 | encoded | `s 339ZH(6B) condition 4 is met` | poca-tests-orders.l4 |
| s 339ZH(7) | p7:695-697 | encoded | `s 339ZH(7) the information order has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(7)(a) | p7:696 | encoded | `s 339ZH(7) the information order has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(7)(b) | p7:697 | encoded | `s 339ZH(7) the information order has the content it must have` | poca-tests-orders.l4 |
| s 339ZH(8) | p7:698 | encoded | `s 339ZH(8) the magistrates' court may order the person to pay the amount` | poca-tests-orders.l4 |
| s 339ZH(9) | p7:699 | encoded | `s 339ZH(9) the sum is treated as adjudged to be paid by a conviction of the court` | poca-tests-orders.l4 |
| s 339ZH(10) | p7:700 | inert: 2 machinery | a power of the Secretary of State to substitute another sum for the £5,000 of subsection (8) by regulations; the encoded figure is that of the edition date | - |
| s 339ZH(11) | p7:701 | encoded | `s 339ZH(11) the business is a business in the regulated sector` | poca-tests-orders.l4 |
| s 339ZH(12) | p7:702-711 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “authorised NCA officer” | p7:703 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “corresponding disclosure requirement” | p7:704 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “corresponding money laundering offence” | p7:705 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “the criminal intelligence function” | p7:706 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “foreign country” | p7:707 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “foreign FIU” | p7:708 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZH(12) “relevant person” | p7:709 | encoded | `s 339ZH(12) the person is an authorised NCA officer` ; `s 339ZH(12) the requirement is a corresponding disclosure requirement` ; `s 339ZH(12) the offence is a corresponding money laundering offence` ; `s 339ZH(12) the function is the criminal intelligence function` ; `s 339ZH(12) the place is a foreign country` ; `s 339ZH(12) the body is a foreign FIU` ; `s 339ZH(12) the applicant is a relevant person` | poca-tests-orders.l4 |
| s 339ZL | p7:712-727 | encoded | see the child rows | poca-tests-orders.l4 |
| s 339ZL(1) | p7:713-715 | inert: 2 machinery | a duty on the Secretary of State to make a code of practice about the NCA's applications for information orders on condition 3 or 4: the making of a code | - |
| s 339ZL(1)(a) | p7:714 | inert: 2 machinery | a duty on the Secretary of State to make a code of practice about the NCA's applications for information orders on condition 3 or 4: the making of a code | - |
| s 339ZL(1)(b) | p7:715 | inert: 2 machinery | a duty on the Secretary of State to make a code of practice about the NCA's applications for information orders on condition 3 or 4: the making of a code | - |
| s 339ZL(2) | p7:716-719 | inert: 2 machinery | the procedure for issuing the code (publish a draft, consider representations, modify) | - |
| s 339ZL(2)(a) | p7:717 | inert: 2 machinery | the procedure for issuing the code (publish a draft, consider representations, modify) | - |
| s 339ZL(2)(b) | p7:718 | inert: 2 machinery | the procedure for issuing the code (publish a draft, consider representations, modify) | - |
| s 339ZL(2)(c) | p7:719 | inert: 2 machinery | the procedure for issuing the code (publish a draft, consider representations, modify) | - |
| s 339ZL(3) | p7:720 | inert: 2 machinery | lets the consultation steps be taken before the section came into force | - |
| s 339ZL(4) | p7:721 | inert: 2 machinery | a duty to lay a draft of the code before Parliament | - |
| s 339ZL(5) | p7:722 | inert: 2 machinery | a power to bring the code into operation by regulations | - |
| s 339ZL(6) | p7:723 | inert: 2 machinery | a power to revise the code, with the same procedure | - |
| s 339ZL(7) | p7:724 | encoded | `s 339ZL(7) the failure of itself makes the person liable to criminal or civil proceedings` | poca-tests-orders.l4 |
| s 339ZL(8) | p7:725 | encoded | `s 339ZL(8) the code is admissible in evidence and is to be taken into account` | poca-tests-orders.l4 |
| s 339ZL(9) | p7:726 | inert: 2 machinery | lets the code be combined with the code under section 22F of the Terrorism Act 2000 | - |
| s 339ZL(10) | p7:727 | inert: 1 not operative | points to the definition of "authorised NCA officer" in s 339ZH(12), which is encoded there (a lead-in or signpost that creates no rule) | - |
| s 339ZL(10) “authorised NCA officer” | p7:727 | inert: 1 not operative | points to the definition of "authorised NCA officer" in s 339ZH(12), which is encoded there (a lead-in or signpost that creates no rule) | - |
| s 339ZI | p7:728-740 | encoded | see the child rows | poca-tests-orders.l4 |
| s 339ZI(1) | p7:729 | encoded | `s 339ZI(1) the statement may be used in evidence against the person in criminal proceedings` | poca-tests-orders.l4 |
| s 339ZI(2) | p7:730-733 | encoded | `s 339ZI(2) subsection (1) does not apply` | poca-tests-orders.l4 |
| s 339ZI(2)(a) | p7:731 | encoded | `s 339ZI(2) subsection (1) does not apply` | poca-tests-orders.l4 |
| s 339ZI(2)(b) | p7:732 | encoded | `s 339ZI(2) subsection (1) does not apply` | poca-tests-orders.l4 |
| s 339ZI(2)(c) | p7:733 | encoded | `s 339ZI(2) subsection (1) does not apply` | poca-tests-orders.l4 |
| s 339ZI(3) | p7:734-737 | encoded | `s 339ZI(3) use of the statement by virtue of subsection (2)(c) is barred` | poca-tests-orders.l4 |
| s 339ZI(3)(a) | p7:735 | encoded | `s 339ZI(3) use of the statement by virtue of subsection (2)(c) is barred` | poca-tests-orders.l4 |
| s 339ZI(3)(b) | p7:736-737 | encoded | `s 339ZI(3) use of the statement by virtue of subsection (2)(c) is barred` | poca-tests-orders.l4 |
| s 339ZI(4) | p7:738-740 | encoded | `s 339ZI(4) the prosecution is a prosecution for perjury` | poca-tests-orders.l4 |
| s 339ZI(4)(a) | p7:739 | encoded | `s 339ZI(4) the prosecution is a prosecution for perjury` | poca-tests-orders.l4 |
| s 339ZI(4)(b) | p7:740 | encoded | `s 339ZI(4) the prosecution is a prosecution for perjury` | poca-tests-orders.l4 |
| s 339ZJ | p7:741-750 | encoded | see the child rows | poca-tests-orders.l4 |
| s 339ZJ(1) | p7:742 | encoded | `s 339ZJ(1) an appeal lies to the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(2) | p7:743 | encoded | `s 339ZJ(2) the appeal lies at the instance of the person` | poca-tests-orders.l4 |
| s 339ZJ(3) | p7:744-747 | encoded | `s 339ZJ(3) the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(3) “relevant appeal court” | p7:744 | encoded | `s 339ZJ(3) the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(3)(a) | p7:745 | encoded | `s 339ZJ(3) the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(3)(b) | p7:746 | encoded | `s 339ZJ(3) the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(3)(c) | p7:747 | encoded | `s 339ZJ(3) the relevant appeal court` | poca-tests-orders.l4 |
| s 339ZJ(4) | p7:748-750 | encoded | `s 339ZJ(4) the relevant appeal court may do the thing on an appeal under this section` | poca-tests-orders.l4 |
| s 339ZJ(4)(a) | p7:749 | encoded | `s 339ZJ(4) the relevant appeal court may do the thing on an appeal under this section` | poca-tests-orders.l4 |
| s 339ZJ(4)(b) | p7:750 | encoded | `s 339ZJ(4) the relevant appeal court may do the thing on an appeal under this section` | poca-tests-orders.l4 |
| s 339ZK | p7:751-756 | encoded | see the child rows | poca-tests-orders.l4 |
| s 339ZK(1) | p7:752 | encoded | `s 339ZK(1) the information order confers the right to require the person to provide the information` | poca-tests-orders.l4 |
| s 339ZK(2) | p7:753 | encoded | `s 339ZK(2) the information is privileged information` | poca-tests-orders.l4 |
| s 339ZK(2) “Privileged information” | p7:753 | encoded | `s 339ZK(2) the information is privileged information` | poca-tests-orders.l4 |
| s 339ZK(2) “privileged information” | p7:753 | encoded | `s 339ZK(2) the information is privileged information` | poca-tests-orders.l4 |
| s 339ZK(3) | p7:754 | encoded | `s 339ZK(3) the provision is not to be taken to breach a restriction on the disclosure of information` | poca-tests-orders.l4 |
| s 339ZK(4) | p7:755 | encoded | `s 339ZK(4) the application may be heard and determined in private` | poca-tests-orders.l4 |
| s 339ZK(5) | p7:756 | inert: 2 machinery | rules of court may make provision as to practice and procedure | - |
| part 7 heading "Threshold amounts" | p7:757 | inert: 1 not operative | a cross-heading | - |
| s 339A | p7:758-771 | encoded | see the child rows | poca-tests-threshold.l4 |
| s 339A(1) | p7:759-761 | inert: 1 not operative | a cross-reference table: says which subsections serve which exceptions in ss 327, 328 and 329 (a lead-in or signpost that creates no rule) | - |
| s 339A(1)(a) | p7:760 | inert: 1 not operative | a cross-reference table: says which subsections serve which exceptions in ss 327, 328 and 329 (a lead-in or signpost that creates no rule) | - |
| s 339A(1)(b) | p7:761 | inert: 1 not operative | a cross-reference table: says which subsections serve which exceptions in ss 327, 328 and 329 (a lead-in or signpost that creates no rule) | - |
| s 339A(2) | p7:762 | encoded | `s 339A(2) the threshold amount for acts done in operating an account, in pounds` | poca-tests-threshold.l4 |
| s 339A(3) | p7:763-765 | encoded | `s 339A(3) the person may specify the threshold amount for acts done in operating an account` | poca-tests-threshold.l4 |
| s 339A(3)(a) | p7:764 | encoded | `s 339A(3) the person may specify the threshold amount for acts done in operating an account` | poca-tests-threshold.l4 |
| s 339A(3)(b) | p7:765 | encoded | `s 339A(3) the person may specify the threshold amount for acts done in operating an account` | poca-tests-threshold.l4 |
| s 339A(4) | p7:766 | encoded | `s 339A(4) the person may vary the threshold amount for acts done in operating an account` | poca-tests-threshold.l4 |
| s 339A(5) | p7:767 | encoded | `s 339A(5) different threshold amounts may be specified for different acts on the same account` | poca-tests-threshold.l4 |
| s 339A(6) | p7:768 | encoded | `s 339A(6) the specified amount is one that may be specified as the threshold amount` | poca-tests-threshold.l4 |
| s 339A(6A) | p7:769 | encoded | `s 339A(6A) the threshold amount for acts done to terminate a business relationship, in pounds` | poca-tests-threshold.l4 |
| s 339A(7) | p7:770 | inert: 2 machinery | a power of the Secretary of State to vary the figures in (2) and (6A) by order; the encoded figures are those of the edition date | - |
| s 339A(8) | p7:771 | encoded | `s 339A(8) the account is related to the other` | poca-tests-threshold.l4 |
| part 7 heading "Interpretation" | p7:772 | inert: 1 not operative | a cross-heading | - |
| s 340 | p7:773-820 | encoded | see the child rows | poca-tests-interp.l4 |
| s 340(1) | p7:774 | inert: 1 not operative | says where the section's definitions are used ("for the purposes of this Part") (a lead-in or signpost that creates no rule) | - |
| s 340(2) | p7:775-777 | encoded | `s 340(2) the conduct is criminal conduct` | poca-tests-interp.l4 |
| s 340(2) “criminal conduct” | p7:775 | encoded | `s 340(2) the conduct is criminal conduct` | poca-tests-interp.l4 |
| s 340(2)(a) | p7:776 | encoded | `s 340(2) the conduct is criminal conduct` | poca-tests-interp.l4 |
| s 340(2)(b) | p7:777 | encoded | `s 340(2) the conduct is criminal conduct` | poca-tests-interp.l4 |
| s 340(3) | p7:778-780 | encoded | `s 340(3) the property is criminal property` | poca-tests-interp.l4 |
| s 340(3) “criminal property” | p7:778 | encoded | `s 340(3) the property is criminal property` | poca-tests-interp.l4 |
| s 340(3)(a) | p7:779 | encoded | `s 340(3) the property is criminal property` | poca-tests-interp.l4 |
| s 340(3)(b) | p7:780 | encoded | `s 340(3) the property is criminal property` | poca-tests-interp.l4 |
| s 340(4) | p7:781-784 | encoded | `s 340(4) the matter is immaterial` | poca-tests-interp.l4 |
| s 340(4)(a) | p7:782 | encoded | `s 340(4) the matter is immaterial` | poca-tests-interp.l4 |
| s 340(4)(b) | p7:783 | encoded | `s 340(4) the matter is immaterial` | poca-tests-interp.l4 |
| s 340(4)(c) | p7:784 | encoded | `s 340(4) the matter is immaterial` | poca-tests-interp.l4 |
| s 340(5) | p7:785 | encoded | `s 340(5) the person benefits from the conduct` | poca-tests-interp.l4 |
| s 340(5) “benefits from conduct” | p7:785 | encoded | `s 340(5) the person benefits from the conduct` | poca-tests-interp.l4 |
| s 340(6) | p7:786 | encoded | `s 340(6) the sum of money he is taken to obtain, in pounds` | poca-tests-interp.l4 |
| s 340(7) | p7:787 | encoded | `s 340(7) the property or advantage was obtained in connection with the conduct` | poca-tests-interp.l4 |
| s 340(8) | p7:788 | encoded | `s 340(8) the property is his benefit` | poca-tests-interp.l4 |
| s 340(9) | p7:789-792 | encoded | `s 340(9) the thing is property` | poca-tests-interp.l4 |
| s 340(9) “property” | p7:789 | encoded | `s 340(9) the thing is property` | poca-tests-interp.l4 |
| s 340(9)(a) | p7:790 | encoded | `s 340(9) the thing is property` | poca-tests-interp.l4 |
| s 340(9)(b) | p7:791 | encoded | `s 340(9) the thing is property` | poca-tests-interp.l4 |
| s 340(9)(c) | p7:792 | encoded | `s 340(9) the thing is property` | poca-tests-interp.l4 |
| s 340(10) | p7:793-797 | encoded | the lead-in of paragraphs (a) to (d), which have their own rules | poca-tests-interp.l4 |
| s 340(10)(a) | p7:794 | encoded | `s 340(10)(a) the property is obtained by the person` | poca-tests-interp.l4 |
| s 340(10)(b) | p7:795 | encoded | `s 340(10)(b) the thing is an interest in land in England and Wales or Northern Ireland` | poca-tests-interp.l4 |
| s 340(10)(c) | p7:796 | encoded | `s 340(10)(c) the thing is an interest in land in Scotland` | poca-tests-interp.l4 |
| s 340(10)(d) | p7:797 | encoded | `s 340(10)(d) the thing is an interest in property other than land` | poca-tests-interp.l4 |
| s 340(11) | p7:798-802 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(11) “money laundering” | p7:798 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(11)(a) | p7:799 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(11)(b) | p7:800 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(11)(c) | p7:801 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(11)(d) | p7:802 | encoded | `s 340(11) the act is money laundering` | poca-tests-interp.l4 |
| s 340(12) | p7:803-805 | encoded | `s 340(12) the body is the person's employer for a disclosure to a nominated officer` | poca-tests-interp.l4 |
| s 340(12)(a) | p7:804 | encoded | `s 340(12) the body is the person's employer for a disclosure to a nominated officer` | poca-tests-interp.l4 |
| s 340(12)(b) | p7:805 | encoded | `s 340(12)(b) the person is in employment for a disclosure to a nominated officer` | poca-tests-interp.l4 |
| s 340(13) | p7:806 | encoded | `s 340(13) the person is a constable for the purposes of this Part` | poca-tests-interp.l4 |
| s 340(14) | p7:807-810 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14) “Deposit-taking body” | p7:807 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14) “deposit-taking body” | p7:807 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14)(a) | p7:808 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14)(b) | p7:809 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14)(c) | p7:810 | encoded | `s 340(14) the person is a deposit-taking body` | poca-tests-interp.l4 |
| s 340(14A) | p7:811-813 | encoded | inputs of `s 340(14) the person is a deposit-taking body` (the regulated-activity limit of (14A)(a) and the excluded persons of (14A)(b)) | poca-tests-interp.l4 |
| s 340(14A)(a) | p7:812 | encoded | inputs of `s 340(14) the person is a deposit-taking body` (the regulated-activity limit of (14A)(a) and the excluded persons of (14A)(b)) | poca-tests-interp.l4 |
| s 340(14A)(b) | p7:813 | encoded | inputs of `s 340(14) the person is a deposit-taking body` (the regulated-activity limit of (14A)(a) and the excluded persons of (14A)(b)) | poca-tests-interp.l4 |
| s 340(14B) | p7:814 | inert: 2 machinery | a duty on the Treasury or the Secretary of State to consult before making regulations | - |
| s 340(14C) | p7:815 | encoded | `s 340(14C) the person is an electronic money institution` | poca-tests-interp.l4 |
| s 340(14C) “Electronic money institution” | p7:815 | encoded | `s 340(14C) the person is an electronic money institution` | poca-tests-interp.l4 |
| s 340(14C) “electronic money institution” | p7:815 | encoded | `s 340(14C) the person is an electronic money institution` | poca-tests-interp.l4 |
| s 340(15) | p7:816 | encoded | `s 340(15) the order is an information order` | poca-tests-interp.l4 |
| s 340(15) “Information order” | p7:816 | encoded | `s 340(15) the order is an information order` | poca-tests-interp.l4 |
| s 340(15) “information order” | p7:816 | encoded | `s 340(15) the order is an information order` | poca-tests-interp.l4 |
| s 340(16) | p7:817 | encoded | `s 340(16) the person is a payment institution` | poca-tests-interp.l4 |
| s 340(16) “Payment institution” | p7:817 | encoded | `s 340(16) the person is a payment institution` | poca-tests-interp.l4 |
| s 340(16) “payment institution” | p7:817 | encoded | `s 340(16) the person is a payment institution` | poca-tests-interp.l4 |
| s 340(17) | p7:818-820 | encoded | `s 340(17) the relationship is a business relationship` | poca-tests-interp.l4 |
| s 340(17) “Business relationship” | p7:818 | encoded | `s 340(17) the relationship is a business relationship` | poca-tests-interp.l4 |
| s 340(17) “business relationship” | p7:818 | encoded | `s 340(17) the relationship is a business relationship` | poca-tests-interp.l4 |
| s 340(17)(a) | p7:819 | encoded | `s 340(17) the relationship is a business relationship` | poca-tests-interp.l4 |
| s 340(17)(b) | p7:820 | encoded | `s 340(17) the relationship is a business relationship` | poca-tests-interp.l4 |
| sch 9 heading "SCHEDULE 9 — Regulated sector and supervisory authorities" | s9:1 | inert: 1 not operative | a title | - |
| sch 9 heading "PART 1 — REGULATED SECTOR" | s9:2 | inert: 1 not operative | a heading | - |
| sch 9 para 1 | s9:3-98 | encoded | see the child rows | F1 (numbering) |
| sch 9 para 1(1) | s9:4-41 | encoded | `sch 9 para 1(1) the business is in the regulated sector to the extent that it consists of a listed activity` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(a) | s9:5 | encoded | `sch 9 para 1(1)(a) the business consists of accepting deposits or granting credits as a credit institution` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(b) | s9:6-12 | encoded | `sch 9 para 1(1)(b) the business consists of listed activities carried on by an undertaking not excluded by (i), (ia) or (ii)` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(c) | s9:13 | encoded | `sch 9 para 1(1)(c) the business consists of long-term insurance other than reinsurance` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(d) | s9:14 | encoded | `sch 9 para 1(1)(d) the business consists of investment services or activities by a person not excluded` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(e) | s9:15 | encoded | `sch 9 para 1(1)(e) the business consists of the marketing or offering of units or shares by a collective investment undertaking` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(f) | s9:16 | encoded | `sch 9 para 1(1)(f) the business consists of the activities of an insurance intermediary in respect of long-term insurance` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(g) | s9:17 | encoded | `sch 9 para 1(1)(g) the business consists of activities in (b) to (f) carried on by a branch in the United Kingdom` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(h) | s9:18 | encoded | `sch 9 para 1(1)(h) the business consists of the activities of the National Savings Bank` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(i) | s9:19 | encoded | `sch 9 para 1(1)(i) the business consists of an activity for raising money under the National Loans Act 1968` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(j) | s9:20 | encoded | `sch 9 para 1(1)(j) the business consists of statutory audit work by a statutory auditor` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(ja) | s9:21 | encoded | `sch 9 para 1(1)(ja) the business consists of local audit work by a local auditor` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(k) | s9:22 | encoded | `sch 9 para 1(1)(k) the business consists of the activities of an insolvency practitioner` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(l) | s9:23 | encoded | `sch 9 para 1(1)(l) the business consists of the provision of accountancy services` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(m) | s9:24 | encoded | `sch 9 para 1(1)(m) the business consists of material aid, assistance or advice in connection with tax affairs` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(n) | s9:25-31 | encoded | `sch 9 para 1(1)(n) the business consists of participation in a financial or real property transaction by a legal or notarial services provider` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(o) | s9:32 | encoded | `sch 9 para 1(1)(o) the business consists of a service mentioned in sub-paragraph (4)` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(p) | s9:33 | encoded | `sch 9 para 1(1)(p) the business consists of estate agency work or letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(q) | s9:34 | encoded | `sch 9 para 1(1)(q) the business consists of trading in goods where a transaction involves cash payments of at least 10,000 pounds in total` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(r) | s9:35 | encoded | `sch 9 para 1(1)(r) the business consists of operating a casino under a casino operating licence` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(s) | s9:36 | encoded | `sch 9 para 1(1)(s) the business consists of the auctioning by an auction platform of two-day spot or five-day futures` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(t) | s9:37 | encoded | `sch 9 para 1(1)(t) the business consists of bidding directly on behalf of clients in auctions of emissions allowances` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(u) | s9:38-40 | encoded | `sch 9 para 1(1)(u) the business consists of activities in works of art of 10,000 pounds or more, or storing works of art in a freeport` | poca-tests-sch9.l4 |
| sch 9 para 1(1)(v) | s9:41 | encoded | `sch 9 para 1(1)(v) the business consists of activities as a cryptoasset exchange provider or custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(2) | s9:42-44 | encoded | `sch 9 para 1(2) the person is a credit institution` | poca-tests-sch9.l4 |
| sch 9 para 1(2) “credit institution” | s9:42 | encoded | `sch 9 para 1(2) the person is a credit institution` | poca-tests-sch9.l4 |
| sch 9 para 1(2)(a) | s9:43 | encoded | `sch 9 para 1(2) the person is a credit institution` | poca-tests-sch9.l4 |
| sch 9 para 1(2)(b) | s9:44 | encoded | `sch 9 para 1(2) the person is a credit institution` | poca-tests-sch9.l4 |
| sch 9 para 1(2A) | s9:45 | encoded | `sch 9 para 1(2A) the contract is a contract of long-term insurance` | poca-tests-sch9.l4 |
| sch 9 para 1(2A) “contract of long-term insurance” | s9:45 | encoded | `sch 9 para 1(2A) the contract is a contract of long-term insurance` | poca-tests-sch9.l4 |
| sch 9 para 1(3) | s9:46 | encoded | `sch 9 para 1(3) the person participates in the transaction` | poca-tests-sch9.l4 |
| sch 9 para 1(4) | s9:47-57 | encoded | `sch 9 para 1(4) the service is one referred to in sub-paragraph (1)(o)` | poca-tests-sch9.l4 |
| sch 9 para 1(4)(a) | s9:48-49 | encoded | `sch 9 para 1(4) the service is one referred to in sub-paragraph (1)(o)` | poca-tests-sch9.l4 |
| sch 9 para 1(4)(b) | s9:50-53 | encoded | `sch 9 para 1(4) the service is one referred to in sub-paragraph (1)(o)` | poca-tests-sch9.l4 |
| sch 9 para 1(4)(c) | s9:54 | encoded | `sch 9 para 1(4) the service is one referred to in sub-paragraph (1)(o)` | poca-tests-sch9.l4 |
| sch 9 para 1(4)(d) | s9:55-57 | encoded | `sch 9 para 1(4) the service is one referred to in sub-paragraph (1)(o)` | poca-tests-sch9.l4 |
| sch 9 para 1(4A) | s9:58-60 | encoded | `sch 9 para 1(4A) the firm is an off-the-shelf firm` | poca-tests-sch9.l4 |
| sch 9 para 1(4A) “off-the-shelf firm” | s9:58 | encoded | `sch 9 para 1(4A) the firm is an off-the-shelf firm` | poca-tests-sch9.l4 |
| sch 9 para 1(4A)(a) | s9:59 | encoded | `sch 9 para 1(4A) the firm is an off-the-shelf firm` | poca-tests-sch9.l4 |
| sch 9 para 1(4A)(b) | s9:60 | encoded | `sch 9 para 1(4A) the firm is an off-the-shelf firm` | poca-tests-sch9.l4 |
| sch 9 para 1(5) | s9:61 | encoded | `sch 9 para 1(5) the market is a regulated market` | poca-tests-sch9.l4 |
| sch 9 para 1(5) “regulated market” | s9:61 | encoded | `sch 9 para 1(5) the market is a regulated market` | poca-tests-sch9.l4 |
| sch 9 para 1(6) | s9:62 | repealed or blank in this text | shown as dots only (line 62) | - |
| sch 9 para 1(6A) | s9:63 | encoded | `sch 9 para 1(6A) the work is estate agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6A) “estate agency work” | s9:63 | encoded | `sch 9 para 1(6A) the work is estate agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6B) | s9:64-70 | encoded | `sch 9 para 1(6B) the work is letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6B) “letting agency work” | s9:64 | encoded | `sch 9 para 1(6B) the work is letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6B)(a) | s9:65-67 | encoded | `sch 9 para 1(6B) the work is letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6B)(b) | s9:68-70 | encoded | `sch 9 para 1(6B) the work is letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6C) | s9:71 | encoded | `sch 9 para 1(6C) the thing done is letting agency work` | poca-tests-sch9.l4 |
| sch 9 para 1(6D) | s9:72-76 | encoded | `sch 9 para 1(6D) the thing is one of those listed` | poca-tests-sch9.l4 |
| sch 9 para 1(6D)(a) | s9:73 | encoded | `sch 9 para 1(6D) the thing is one of those listed` | poca-tests-sch9.l4 |
| sch 9 para 1(6D)(b) | s9:74 | encoded | `sch 9 para 1(6D) the thing is one of those listed` | poca-tests-sch9.l4 |
| sch 9 para 1(6D)(c) | s9:75 | encoded | `sch 9 para 1(6D) the thing is one of those listed` | poca-tests-sch9.l4 |
| sch 9 para 1(6D)(d) | s9:76 | encoded | `sch 9 para 1(6D) the thing is one of those listed` | poca-tests-sch9.l4 |
| sch 9 para 1(6E) | s9:77 | encoded | `sch 9 para 1(6E) the thing is land` | poca-tests-sch9.l4 |
| sch 9 para 1(6E) “land” | s9:77 | encoded | `sch 9 para 1(6E) the thing is land` | poca-tests-sch9.l4 |
| sch 9 para 1(7) | s9:78 | encoded | `sch 9 para 1(7) the person is a firm` | poca-tests-sch9.l4 |
| sch 9 para 1(7) “firm” | s9:78 | encoded | `sch 9 para 1(7) the person is a firm` | poca-tests-sch9.l4 |
| sch 9 para 1(8) | s9:79 | encoded | `sch 9 para 1(8) the thing is cash` | poca-tests-sch9.l4 |
| sch 9 para 1(8) “cash” | s9:79 | encoded | `sch 9 para 1(8) the thing is cash` | poca-tests-sch9.l4 |
| sch 9 para 1(9) | s9:80 | encoded | `sch 9 para 1(9) the platform is an auction platform` | poca-tests-sch9.l4 |
| sch 9 para 1(9) “auction platform” | s9:80 | encoded | `sch 9 para 1(9) the platform is an auction platform` | poca-tests-sch9.l4 |
| sch 9 para 1(10) | s9:81 | encoded | `sch 9 para 1(10) the thing is a work of art` | poca-tests-sch9.l4 |
| sch 9 para 1(10) “work of art” | s9:81 | encoded | `sch 9 para 1(10) the thing is a work of art` | poca-tests-sch9.l4 |
| sch 9 para 1(11) | s9:82 | encoded | `sch 9 para 1(11) the place is a freeport` | poca-tests-sch9.l4 |
| sch 9 para 1(11) “freeport” | s9:82 | encoded | `sch 9 para 1(11) the place is a freeport` | poca-tests-sch9.l4 |
| sch 9 para 1(12) | s9:83-90 | encoded | `sch 9 para 1(12) the person is a cryptoasset exchange provider or a custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(12)(a) | s9:84-87 | encoded | `sch 9 para 1(12) the person is a cryptoasset exchange provider or a custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(12)(a) “cryptoasset exchange provider” | s9:84 | encoded | `sch 9 para 1(12) the person is a cryptoasset exchange provider or a custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(12)(b) | s9:88-90 | encoded | `sch 9 para 1(12) the person is a cryptoasset exchange provider or a custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(12)(b) “custodian wallet provider” | s9:88 | encoded | `sch 9 para 1(12) the person is a cryptoasset exchange provider or a custodian wallet provider` | poca-tests-sch9.l4 |
| sch 9 para 1(13) | s9:91-98 | inert: 1 not operative | the lead-in "For the purposes of sub-paragraph (12)"; paragraphs (a) to (c) have their own rules (a lead-in or signpost that creates no rule) | - |
| sch 9 para 1(13)(a) | s9:92 | encoded | `sch 9 para 1(13)(a) and (c) the thing is a cryptoasset` | poca-tests-sch9.l4 |
| sch 9 para 1(13)(a) “cryptoasset” | s9:92 | encoded | `sch 9 para 1(13)(a) and (c) the thing is a cryptoasset` | poca-tests-sch9.l4 |
| sch 9 para 1(13)(b) | s9:93-97 | encoded | `sch 9 para 1(13)(b) the thing is money` | poca-tests-sch9.l4 |
| sch 9 para 1(13)(b) “money” | s9:93 | encoded | `sch 9 para 1(13)(b) the thing is money` | poca-tests-sch9.l4 |
| sch 9 para 1(13)(c) | s9:98 | encoded | `sch 9 para 1(13)(a) and (c) the thing is a cryptoasset` (the same rule: (c) widens (a) to a right to, or interest in, the cryptoasset) | poca-tests-sch9.l4 |
| sch 9 para 1(13)(c) “cryptoasset” | s9:98 | encoded | `sch 9 para 1(13)(a) and (c) the thing is a cryptoasset` (the same rule: (c) widens (a) to a right to, or interest in, the cryptoasset) | poca-tests-sch9.l4 |
| sch 9 para 2 | s9:99-125 | fork | F4: the Schedule states no priority between paragraph 1(1) (what is in the regulated sector) and paragraph 2 (what is not); read as paragraph 2 winning, from its own words "A business is not in the regulated sector to the extent that"; the other reading is that both can hold and the text then gives no single answer; encoded by `sch 9 paras 1 and 2 the business is in the regulated sector`; F1 (numbering) | poca-tests-sch9.l4 |
| sch 9 para 2(1) | s9:100-108 | encoded | `sch 9 para 2(1) the business is in the regulated sector to the extent that it consists of an excluded activity` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(a) | s9:101 | encoded | `sch 9 para 2(1)(a) the business consists of a registered society's issuing of withdrawable share capital or acceptance of deposits within the limits` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(b) | s9:102 | encoded | `sch 9 para 2(1)(b) the business consists of a registered Northern Ireland society's issuing of withdrawable share capital or acceptance of deposits within the limits` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(c) | s9:103 | encoded | `sch 9 para 2(1)(c) the business consists of an activity for which a person specified in the Exemption Order is exempt` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(d) | s9:104 | encoded | `sch 9 para 2(1)(d) the business consists of the exercise of functions under section 45 of the Financial Services Act 1986 by a formerly exempted person` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(e) | s9:105 | encoded | `sch 9 para 2(1)(e) the business consists of financial activity meeting the conditions in sub-paragraph (3) by a high value dealer` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(f) | s9:106 | repealed or blank in this text | shown as dots only (line 106) | - |
| sch 9 para 2(1)(g) | s9:107 | encoded | `sch 9 para 2(1)(g) the business consists of an activity of a local authority that would be regulated but for article 72G` | poca-tests-sch9.l4 |
| sch 9 para 2(1)(h) | s9:108 | encoded | `sch 9 para 2(1)(h) the business consists of the preparation of a home report` | poca-tests-sch9.l4 |
| sch 9 para 2(2) | s9:109 | encoded | `sch 9 para 2(2) the person is a high value dealer` | poca-tests-sch9.l4 |
| sch 9 para 2(2) “high value dealer” | s9:109 | encoded | `sch 9 para 2(2) the person is a high value dealer` | poca-tests-sch9.l4 |
| sch 9 para 2(3) | s9:110-117 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(a) | s9:111 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(b) | s9:112 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(c) | s9:113 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(d) | s9:114 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(e) | s9:115 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(f) | s9:116 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(3)(g) | s9:117 | encoded | `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-tests-sch9.l4 |
| sch 9 para 2(4) | s9:118-125 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(a) | s9:119 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(b) | s9:120 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(c) | s9:121 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(d) | s9:122 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(e) | s9:123 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(f) | s9:124 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 2(4)(g) | s9:125 | encoded | `sch 9 para 2(4) the business is in the regulated sector` | poca-tests-sch9.l4 |
| sch 9 para 3 | s9:126-138 | encoded | see the child rows | F1 (numbering) |
| sch 9 para 3(1) | s9:127-136 | encoded | `sch 9 para 3(1) what the defined instrument means` | poca-tests-sch9.l4 |
| sch 9 para 3(1) “the Capital Requirements Regulation” | s9:130 | encoded | `sch 9 para 3(1) what the defined instrument means` | poca-tests-sch9.l4 |
| sch 9 para 3(1) “the Emission Allowance Auctioning Regulation” | s9:131 | encoded | `sch 9 para 3(1) what the defined instrument means` | poca-tests-sch9.l4 |
| sch 9 para 3(1) “the Markets in Financial Instruments Directive” | s9:135 | encoded | `sch 9 para 3(1) what the defined instrument means` | poca-tests-sch9.l4 |
| sch 9 para 3(1) “the Solvency 2 Directive” | s9:136 | encoded | `sch 9 para 3(1) what the defined instrument means` | poca-tests-sch9.l4 |
| sch 9 para 3(2) | s9:137 | encoded | `sch 9 para 3(2) the amount is within a reference to an amount in euros` | poca-tests-sch9.l4 |
| sch 9 para 3(3) | s9:138 | encoded | `sch 9 para 3(3) the term has the same meaning in this Part as in that Regulation or Directive` | poca-tests-sch9.l4 |
| sch 9 heading "PART 2 — SUPERVISORY AUTHORITIES" | s9:139 | inert: 1 not operative | a heading | - |
| sch 9 para 4 | s9:140-172 | encoded | see the child rows | F1 (numbering) |
| sch 9 para 4(1) | s9:140-148 | encoded | `sch 9 para 4(1) the body is a supervisory authority` | poca-tests-sch9.l4 |
| sch 9 para 4(1)(a) | s9:141 | encoded | `sch 9 para 4(1) the body is a supervisory authority` | poca-tests-sch9.l4 |
| sch 9 para 4(1)(b) | s9:142 | repealed or blank in this text | shown as dots only (line 142) | - |
| sch 9 para 4(1)(c) | s9:143 | encoded | `sch 9 para 4(1) the body is a supervisory authority` | poca-tests-sch9.l4 |
| sch 9 para 4(1)(d) | s9:144 | encoded | `sch 9 para 4(1) the body is a supervisory authority` | poca-tests-sch9.l4 |
| sch 9 para 4(1)(e) | s9:145 | repealed or blank in this text | shown as dots only (line 145) | - |
| sch 9 para 4(1)(ea) | s9:146 | repealed or blank in this text | shown as dots only (line 146) | - |
| sch 9 para 4(1)(f) | s9:147 | repealed or blank in this text | shown as "..." (line 147) | - |
| sch 9 para 4(1)(g) | s9:148 | encoded | `sch 9 para 4(1) the body is a supervisory authority` | poca-tests-sch9.l4 |
| sch 9 para 4(2) | s9:149-172 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(a) | s9:150 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(b) | s9:151 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(c) | s9:152 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(d) | s9:153 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(da) | s9:154 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(e) | s9:155 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(f) | s9:156 | repealed or blank in this text | shown as dots only (line 156) | - |
| sch 9 para 4(2)(g) | s9:157 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(h) | s9:158 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(i) | s9:159 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(j) | s9:160 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(k) | s9:161 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(l) | s9:162 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(m) | s9:163 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(n) | s9:164 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(o) | s9:165 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(p) | s9:166 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(q) | s9:167 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(r) | s9:168 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(s) | s9:169 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(t) | s9:170 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(u) | s9:171 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 para 4(2)(v) | s9:172 | encoded | `sch 9 para 4(2) the body is a professional body referred to in sub-paragraph (1)(g)` | poca-tests-sch9.l4 |
| sch 9 heading "Part 3 — Power to amend" | s9:173 | inert: 1 not operative | a heading | - |
| sch 9 para 5 | s9:174 | inert: 2 machinery | a power for the Treasury to amend Parts 1 and 2 of the Schedule by order; an amended Schedule is a different text (see poca-sch9.l4, last comment) | F1 (numbering) |
<!-- COVERAGE:END -->

## Fork register

The two rulings of 2026-11-04 on negatives and legal effects, word for word as the brief prints them:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

Forks of this row (each: the readings seen, the one taken, the text that licenses each).
The first three are readings; F5 and F6 are readings of a drafting point; the others are modelling choices where the text is silent.

- **F1: Schedule 9 paragraph numbers.**
  The deposited Schedule 9 text has no paragraph numbers, only headings and lettered limbs.
  Taken: paragraph 1 is the list of regulated activities, 2 the exclusions, 3 the meaning of "the Instrument", 4 the supervisory authorities, 5 the power to amend; this follows the order of the headings and the cross-reference in para 2(3)(f) to "paragraph 1(1)(a) to (p) or (r) to (t)".
  Other reading: a different numbering from the official text; labels would then differ, rules would not.
  Not asserted; check against the official text (open question 1).
- **F2: s 340(2) and (3).**
  The brief says they are not among the sources and must be asked as inputs; the text has both (lines 775 to 780).
  Taken: encode both in full (`s 340(2) the conduct is criminal conduct`, `s 340(3) the property is criminal property`); the brief's statement is wrong about this text.
  Asserted.
- **F3: "is" and "means" definitions read as closed.**
  A definition in the form "X is Y if (a), (b)" (for example s 335(1) "The appropriate consent is", s 340(8) "his benefit is") is read as the text's no when the facts fail it.
  Other reading: an "is ... if" is not a "means" and would leave a failed case `NOTHING`.
  This is lawyer reading (a); each such branch is in the table under "Marginal readings for a lawyer".
- **F4: Schedule 9 paragraph 2 over paragraph 1.**
  The Schedule states no priority between para 1(1) ("A business is in the regulated sector to the extent that it consists of") and para 2 ("A business is not in the regulated sector to the extent that").
  Taken: para 2 wins; `sch 9 paras 1 and 2 the business is in the regulated sector` gathers the routes by hand (E1 option B as guidance), and says `JUST FALSE` when any para 2 exclusion holds, otherwise the answer of para 1(1).
  Other reading: both can hold and the text then gives no single answer (`NOTHING`).
  Asserted (`poca-tests-sch9.l4`).
- **F5: s 330(6)(b)(i), the vacuous conditional.**
  Para (i) reads "if he knows either of the things mentioned in subsection (5)(a) and (b), he knows the thing because of information that came to him in privileged circumstances".
  Taken, literally: a material conditional, so an adviser who knows neither thing satisfies (i) without privilege.
  Other reading: (i) always requires that the knowledge be privileged.
  Asserted (`poca-tests-failure.l4`, the case marked "the literal reading of (i)").
- **F6: derived duties.**
  The text states no duty to make the required disclosure, to give no consent, or to include no UK law enforcement information; it makes the failure an offence or says it may not be done.
  Taken (N2): the prohibition is derived from the offence (`SHANT`) and the duty to disclose is derived (`MUST`), each as a decision twin and a regulative rule; where an exception to the offence applies the derived duty is `JUST FALSE`.
  Other reading: the duty exists and is only unpunished; the twin would then be `JUST TRUE` where an exception applies.
  Listed under reading (b).
- **F7: "as soon as is practicable" has no number.**
  Taken: the duties of ss 330(4), 331(4), 332(4), 339ZA, 339ZE(9) are `MUST` with no `WITHIN`, and the prohibitions are `SHANT` with no `WITHIN`; on main a `MUST` with no `WITHIN` never breaches by the passing of time, and only the event discharges it (traced).
  Other reading: a period the text does not state; none invented.
- **F8: penalties as ceilings.**
  "A fine" with no ceiling (on indictment) is `a fine with no ceiling stated`; "to both" is a flag that imprisonment and a fine may both be imposed; "14 years" is 168 months, "five years" 60, "two years" 24.
  Never a tariff.
  Asserted.
- **F9: counting days.**
  Taken: the notice period is the seven working days starting with the first working day after the day the disclosure is made (a Saturday or Sunday is not a working day); the moratorium period is 31 days starting with the day notice of refusal is received, so its last day is thirty days later, plus any days of extension; both edges are inclusive.
  The same reading governs "sent to the NCA authorised officer before the end of the applicable period" (s 339ZD(4)(d)): a report sent on the last day is in time, one sent the day after is not.
  Good Friday and the bank holidays of the part of the United Kingdom where the person is are an input (a list of dates); Christmas Day is computed.
  Asserted (`poca-tests-consent.l4`).
- **F10: the seat takes the person's conclusion on Schedule 9 paragraph 1(1).**
  The 23 limbs of para 1(1) are encoded and tested one by one in layer 1, but the seat question "Is my business in the regulated sector?" asks one yes/no for "my business consists of a listed activity" and one for each exclusion; it does not ask 23 questions.
  A person who answers No gets `JUST FALSE`: the Act hands the question to the list (F15), so a business in no head is not in the regulated sector.  "I am not sure" gets `NOTHING`.
- **F11: legal effects gathered by hand (E1, option B as guidance only).**
  `sch 9 paras 1 and 2 the business is in the regulated sector` (para 1(1) and the three exclusions of para 2), `s 330(6) to (7E) one of the exceptions applies` (the six routes by which s 330 gives no offence), `s 330(6)(c) subsection (7) or (7B) applies to him`, and `s 333A(5) one of the permitted disclosures of sections 333B to 333D applies` (the three sections that permit a disclosure).
  Each gathers routes the text states in separate subsections, by name, in plain L4; no construct gathers them for the reader, and each subsection keeps its own answer (option C).
- **F12: the ruling of 2026-11-05 applied site by site.**
  Taken (a), outside the period JUST FALSE: s 339ZE(8) and (9) ("before the end of the applicable period": when a joint report was made in time, neither subsection applies), s 336B(2) ("as soon as reasonably practicable" read as a period for this purpose, judged by the person's stated fact), s 336A(7) (a day beyond the cap; the calendar date of the cap is now a rule).
  Already JUST FALSE outside the period before the ruling: ss 335(2) to (4), 336(3) and (4), 336A(3) and (4), 337(4), 338(2), 338(2A), 338(3), 339ZD(4)(d), and the fourth condition of ss 330, 331 and 332.
  Taken (b), a "where" not met is JUST FALSE: ss 327(2G), 328(9), 329(2G), 336A(5), 337(4A), 338(4A), 339(3), 339A(4), 339ZA, 339ZC(2), 339ZE(2), (5) and (7), 339ZF(3)(a) and (b); and s 336C(1) and (3), which are new companion questions ("is the period extended?") because the date rules s 336C(2) and (4) return a date and can only say NOTHING.
  An "if" not met is the text's no by the rule of 2026-10-29, and the places that still said NOTHING now say JUST FALSE: ss 339ZF(4) and 339ZH(8).
  s 337(1) ("A disclosure which satisfies the following three conditions") is read like "if": a late disclosure, a recipient s 337(4) does not name, or information that did not come in the course of trade, profession, business or employment is JUST FALSE.
  Taken (c), NOTHING outside the scope: a power or protection given to a class in a sentence with no condition and no "only": ss 338(4), 339(1) (anyone but the Secretary of State), 339(4), 339(7), 336A(6) and (8), 336B(3), (4), (6) and (8), 339A(6A), 339A(3) for a person it does not name, 339ZD(2) and (3) (the notification or report "in good faith"), 339ZE(3) and (6), 339ZF(1) and (2), 339ZH(1) and (9), 339ZI, 339ZJ, 339ZK, 339ZL.
  Where I could not tell which of (a), (b) and (c) a clause was: "In a case within subsection (3)(a)" (s 339ZC(4) and (5)) is read as "where", (b); "In a case where" (s 339ZF(3)) is (b); s 336A(5) has a "Where" and an "on the making of another application", and both limbs are (b); "as soon as reasonably practicable" in s 336B(2) is (a); the lead-in s 339ZD(1) ("This section applies if in any proceedings a question arises") is taken as (c), because its condition is an input of s 339ZD(2) and (3) and not a sentence of its own.
  Other reading for each: the opposite letter.
  Asserted (the test files of the modules named).
- **F13: s 340(13) ("References to a constable include references to a person authorised for the purposes of this Part by the Director General of the National Crime Agency").**
  Applied to: s 335(1) (the person who gives the consent and the person the disclosure was made to, both sides), s 335(2)(a) (a new rule that works out "to a constable or a customs officer" from the recipient), s 339ZA (the recipient is now an input), s 339A(3) and (4) (the person who acts).
  Already applied: ss 337(4) and 338(1)(a).
  Not needed: s 333A(2), which lists the NCA officer separately in its own words at (d); ss 335(3), (4) and 336(3), (4), where the notice is a day the person states, so an NCA-authorised giver counts; the seat's s 335(2) question says so in its `@desc`.
  Asserted.
- **F14: left as they are (reviewer expected JUST FALSE; open question).**
  The lines for Schedule 9 para 1(1), para 4(1) and para 1(4) and for s 339A(3) are gone: the ruling of 2026-11-05 (06:04) settles them (F15).
  - s 330(8)(b) (and its sibling s 331(7)): the court must consider the guidance described; the text does not say it may not consider other guidance, so NOTHING; reviewer expected JUST FALSE; open question.
  - s 336A(7): beyond 186 days in total JUST FALSE, within it NOTHING, because the permission comes from subsections (1) and (8); reviewer expected JUST FALSE; open question.
  - s 339ZI(2)(a): "Subsection (1) does not apply" lifts the bar and does not permit use in evidence, so NOTHING; reviewer expected JUST FALSE; open question.
  - s 340(14)(c) is left as it is.
- **F15: the ruling "Delegated definitions, defences and 'until' bars" applied.**
  (a) A definition the text hands to a list.
  The Act hands "what is a business in the regulated sector" to Schedule 9 in s 330(12)(a), s 333E(1)(a), s 339ZG(9) and s 339ZH(11), and "what is a supervisory authority" in s 330(12)(b), s 331(8) and s 333E(1)(b).
  So `sch 9 para 1(1) ...` is JUST FALSE when none of the 23 heads (a) to (v) holds, `sch 9 paras 1 and 2 ...` follows (it never answers NOTHING now unless a caller passes NOTHING in), and `sch 9 para 4(1) the body is a supervisory authority` is JUST FALSE for a body in none of its heads, which includes a professional body not listed in para 4(2) and a body once named in paras (b), (e), (ea) or (f), now blank.
  The seat question "Is my business in the regulated sector" maps "No" to JUST FALSE; "I am not sure" stays NOTHING.
  The sites that consume the answer: ss 330(12), 331 and 332 and ss 333A to 333E take it as a MAYBE BOOLEAN input; ss 339ZG(9) and 339ZH(11) take it as a yes/no input ("carrying on a business in the regulated sector"), which the caller fills from `sch 9 paras 1 and 2`.
  A bare list with no hand-off answers NOTHING: `sch 9 para 4(2)` (the professional bodies; its own answer for a body not listed, while `sch 9 para 4(1)` answers FALSE), para 1(4) (the services of (1)(o)), para 1(6D), 1(3), 3(1).
  `sch 9 para 1(4)(d)(ii)` answers JUST FALSE for a nominee shareholder for a company whose securities are listed, in the text's own words (the function was added in the round before); the list of services as a whole stays open.
  The exclusions (para 2(1), (3), (4), para 1(6C)) answer JUST FALSE when they apply and NOTHING when their own condition is unmet, because those functions ask the positive question ("is the business in the regulated sector", "is the thing letting agency work") and a carve-out whose condition is unmet says nothing about it; `sch 9 paras 1 and 2` gathers them with para 1(1).
  Other reading: the exclusions' unmet condition is FALSE for the exclusion's own question; that question is not asked by any function.
  (b) "It is a defence ... to prove that X".
  No provision of Part 7 or Schedule 9 uses that wording (searched for "defence", "prove", "proves", "burden"): the exceptions are phrased "does not commit an offence if", which are the text's own no (JUST FALSE) already.
  No site changed.
  (c) "When", "upon" and "whenever".
  Changed: s 339A(3), where "when he gives consent, or gives notice refusing consent" and "on a request" are the occasions of the power, so an occasion not named is JUST FALSE (a person not named stays NOTHING, (c) of the first ruling).
  Read and left: Schedule 9 para 1(1)(q), (u) and (v) ("whenever", "when it", "when acting"), which are conditions of a head and already make the head FALSE; para 2(2) ("when carrying on", a closed "means"); para 1(6C) ("when done by", an exclusion, see (a)); s 336B(4) ("specified information upon which he or she intends to rely", a relative clause that describes the information, not a condition); s 336C(2), (4), (7) ("from the time when it would otherwise end", a point in time); s 338(2A)(b) ("at a time when", a point in time); s 339A(6) ("when specified", a point in time); s 340(17)(b) ("at the time when contact is established"); ss 335(7), 336(9) ("where the person is when he makes the disclosure", a place); s 339ZL(5) ("When the Secretary of State has laid a draft", inert, reason 2).
  (d) "Until" bars.
  None in range.
  The three "until" clauses (s 336C(2), (4), (7)) say how long an extension lasts, not that something may not be done until an event; each is a date rule, with a yes/no companion ("is the period extended?") for s 336C(2) and (4) in `s 336C(1)` and `s 336C(3)`, and `s 336C(6)` for (7).
  Asserted (the test files of the modules named).

## Marginal readings for a lawyer

<!-- MARGINAL:BEGIN -->
Generated by `python3 -I marginal.py write NOTES.md` from the comments in the layer-1 modules: 154 rules, 171 branches resting on reading (a) and 58 on reading (b).

- **Reading (a)**, taken: a failed "if", a definition ("means" or "is") read as closed, a list the text closes, and a flat negative all count as the text's no, so the branch answers `JUST FALSE`.
  The other reading: "if A then B" does not itself say "if not A then not B", so the branch would answer `NOTHING` (not covered).
- **Reading (b)**, taken: a prohibition or grant limited by its own wording does not say no outside its limit, so the branch answers `NOTHING`.
  The other reading: outside its limit the grant is refused (or the prohibition does not bite), so the branch would answer `JUST FALSE`.
  The same label covers the duties the text never states but its offence implies (the `MUST` and `SHANT` twins): they are derived from the offence, not stated.

| rule | file:line | branches on (a) | branches on (b) |
| --- | --- | ---: | ---: |
| `s 335(1) the consent is the appropriate consent` | poca-consent.l4:61 | 1 | 0 |
| `s 335(7) the day is a working day` | poca-consent.l4:100 | 1 | 0 |
| `s 335(2) the person must be treated as having the appropriate consent` | poca-consent.l4:144 | 2 | 0 |
| `s 335(2)(a) he makes an authorised disclosure to a constable or a customs officer` | poca-consent.l4:160 | 1 | 0 |
| `s 335(8) the act is a prohibited act` | poca-consent.l4:172 | 1 | 0 |
| `s 335(9) the person is a nominated officer` | poca-consent.l4:183 | 1 | 0 |
| `s 336(9) the day is a working day` | poca-consent.l4:223 | 1 | 0 |
| `s 336(1) the nominated officer is prohibited from giving the appropriate consent` | poca-consent.l4:271 | 1 | 0 |
| `s 336(5) the nominated officer commits an offence` | poca-consent.l4:299 | 4 | 0 |
| `s 336(10) the act is a prohibited act` | poca-consent.l4:325 | 1 | 0 |
| `s 336(11) the person is a nominated officer` | poca-consent.l4:334 | 1 | 0 |
| `s 336A(1) the court may grant an extension of a moratorium period` | poca-consent.l4:353 | 1 | 0 |
| `s 336A(3) the application is made in time` | poca-consent.l4:377 | 1 | 0 |
| `s 336A(4) the extension ends in time` | poca-consent.l4:393 | 1 | 0 |
| `s 336A(5) the court may further extend the moratorium period` | poca-consent.l4:403 | 1 | 0 |
| `s 336A(6) the court may further extend a period extended under section 336C` | poca-consent.l4:413 | 0 | 1 |
| `s 336A(7) the court may grant a further extension` | poca-consent.l4:422 | 1 | 1 |
| `s 336A(7) the court may grant a further extension to that day` | poca-consent.l4:440 | 1 | 1 |
| `s 336A(8) subsections (1) to (4) apply to the extension` | poca-consent.l4:450 | 0 | 1 |
| `s 336B(2) the court has determined the proceedings as it must` | poca-consent.l4:502 | 1 | 0 |
| `s 336B(3) the court may exclude the person from any part of the hearing` | poca-consent.l4:514 | 0 | 1 |
| `s 336B(4) the person may apply for an order that the information be withheld from an interested person` | poca-consent.l4:526 | 0 | 1 |
| `s 336B(6) the court must direct that the person be excluded from the hearing` | poca-consent.l4:563 | 0 | 1 |
| `s 336B(8) an appeal lies to the appropriate appeal court` | poca-consent.l4:581 | 0 | 1 |
| `s 336B(9) the appropriate appeal court may make the order` | poca-consent.l4:590 | 1 | 0 |
| `s 336C(2) the last day of the moratorium period extended pending the application` | poca-consent.l4:638 | 0 | 1 |
| `s 336C(1) the moratorium period is extended in accordance with subsection (2)` | poca-consent.l4:648 | 1 | 0 |
| `s 336C(4) the last day of the moratorium period extended pending the appeal` | poca-consent.l4:663 | 0 | 1 |
| `s 336C(3) the moratorium period is extended in accordance with subsection (4)` | poca-consent.l4:673 | 1 | 0 |
| `s 336C(9) the extension is within the restriction in section 336A(7)` | poca-consent.l4:724 | 1 | 1 |
| `s 327(2B) the conduct is the relevant criminal conduct` | poca-dealing.l4:122 | 1 | 0 |
| `s 327(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-dealing.l4:190 | 1 | 0 |
| `s 327(1) the person commits an offence` | poca-dealing.l4:229 | 7 | 1 |
| `s 328(4) the conduct is the relevant criminal conduct` | poca-dealing.l4:295 | 1 | 0 |
| `s 328(9) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-dealing.l4:355 | 1 | 0 |
| `s 328(1) the person commits an offence` | poca-dealing.l4:371 | 7 | 1 |
| `s 329(2B) the conduct is the relevant criminal conduct` | poca-dealing.l4:436 | 1 | 0 |
| `s 329(2G) the funds or property immediately after the act are assumed to include the relevant criminal property` | poca-dealing.l4:496 | 1 | 0 |
| `s 329(3)(a) and (b) the consideration is inadequate` | poca-dealing.l4:518 | 2 | 0 |
| `s 329(3)(c) the provision of goods or services is consideration` | poca-dealing.l4:526 | 1 | 1 |
| `s 329(1) the person commits an offence` | poca-dealing.l4:544 | 7 | 1 |
| `s 334(3) the most that can be imposed on a person guilty of an offence under section 339(1A)` | poca-dealing.l4:595 | 0 | 1 |
| `s 337(1) the disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-disclose.l4:61 | 1 | 0 |
| `s 337(4A) the further disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-disclose.l4:75 | 1 | 0 |
| `s 337(5) the disclosure is a disclosure to a nominated officer` | poca-disclose.l4:87 | 1 | 0 |
| `s 338(1) the disclosure is authorised` | poca-disclose.l4:146 | 1 | 0 |
| `s 338(4) the authorised disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-disclose.l4:162 | 0 | 1 |
| `s 338(4A) no civil liability arises in respect of the disclosure` | poca-disclose.l4:172 | 1 | 0 |
| `s 338(5) the disclosure is a disclosure to a nominated officer` | poca-disclose.l4:184 | 1 | 0 |
| `s 338(6) the act is the prohibited act` | poca-disclose.l4:195 | 1 | 0 |
| `s 339(1) the person may by order prescribe the form and manner of the disclosure` | poca-disclose.l4:214 | 0 | 1 |
| `s 339(1A) the person commits an offence` | poca-disclose.l4:227 | 3 | 0 |
| `s 339(3) the form complies with the requirements for a form that includes a request` | poca-disclose.l4:254 | 2 | 0 |
| `s 339(4) the disclosure is not to be taken to breach a restriction on the disclosure of information` | poca-disclose.l4:264 | 0 | 1 |
| `s 339(7) subsection (2) does not apply to the disclosure` | poca-disclose.l4:275 | 0 | 1 |
| `s 339ZA the constable or officer of Revenue and Customs must disclose it in full to an authorised person` | poca-disclose.l4:290 | 1 | 0 |
| `s 339ZB(1) A may disclose information to one or more other persons` | poca-disclose.l4:350 | 1 | 0 |
| `s 339ZB(6) the person may disclose information to A for the purposes of making a disclosure request` | poca-disclose.l4:360 | 1 | 0 |
| `s 339ZC(1) the disclosure request has the content it must have` | poca-disclose.l4:378 | 1 | 0 |
| `s 339ZC(2) the disclosure request has the further content it must have` | poca-disclose.l4:391 | 2 | 0 |
| `s 339ZC(4) the required notification has the content it must have` | poca-disclose.l4:423 | 2 | 0 |
| `s 339ZC(5) the required notification has the content it must have` | poca-disclose.l4:441 | 2 | 0 |
| `s 339ZD(5) the report satisfies the requirements as to content` | poca-disclose.l4:467 | 1 | 0 |
| `s 339ZD(4) the report is a joint disclosure report` | poca-disclose.l4:501 | 1 | 0 |
| `s 339ZD(2) the required notification is treated as satisfying the requirement to make the required disclosure` | poca-disclose.l4:516 | 0 | 1 |
| `s 339ZD(3) the joint disclosure report is treated as satisfying the requirement to make the required disclosure` | poca-disclose.l4:528 | 0 | 1 |
| `s 339ZD(7) the joint disclosure report is approved and signed as required` | poca-disclose.l4:543 | 1 | 0 |
| `s 339ZE(2) section 339ZD(2) has effect on the requirement in the case of A, B or C` | poca-disclose.l4:572 | 1 | 0 |
| `s 339ZE(3) section 339ZD(2) removes the requirement to make the required disclosure` | poca-disclose.l4:583 | 0 | 1 |
| `s 339ZE(5) section 339ZD(2) has effect on the requirement in the case of A or C` | poca-disclose.l4:596 | 1 | 0 |
| `s 339ZE(6) section 339ZD(2) removes the requirement to make the required disclosure` | poca-disclose.l4:607 | 0 | 1 |
| `s 339ZE(7) section 339ZD(2) has effect on the requirement in the case of B` | poca-disclose.l4:620 | 1 | 0 |
| `s 339ZE(8) section 339ZD(2) has effect on the requirement to make the required disclosure` | poca-disclose.l4:633 | 1 | 0 |
| `s 339ZE(9) the person who made the required notification must notify an NCA authorised officer that a report is not being made` | poca-disclose.l4:646 | 1 | 0 |
| `s 339ZF(1) the relevant disclosure does not breach an obligation of confidence or another restriction on disclosure` | poca-disclose.l4:684 | 0 | 1 |
| `s 339ZF(2) the relevant disclosure may not include the information` | poca-disclose.l4:694 | 1 | 1 |
| `s 339ZF(3)(a) the relevant disclosure by the undertaking is made as required` | poca-disclose.l4:717 | 2 | 0 |
| `s 339ZF(3)(b) the relevant disclosure to the undertaking is made as required` | poca-disclose.l4:729 | 2 | 0 |
| `s 339ZF(4) subsection (1) applies whether or not the conditions in section 339ZB were met` | poca-disclose.l4:739 | 1 | 0 |
| `s 339ZG(6) the disclosure is the required disclosure` | poca-disclose.l4:829 | 1 | 0 |
| `s 339ZG(8)(a) the undertaking is a credit institution` | poca-disclose.l4:850 | 1 | 0 |
| `s 339ZG(8)(c) the person is a relevant professional adviser` | poca-disclose.l4:866 | 1 | 0 |
| `s 330(3) the second condition is satisfied` | poca-failure.l4:41 | 1 | 0 |
| `s 330(5) the disclosure is the required disclosure` | poca-failure.l4:79 | 1 | 0 |
| `s 330(5A) the property is the laundered property` | poca-failure.l4:91 | 1 | 0 |
| `s 330(1) the person commits an offence` | poca-failure.l4:215 | 2 | 0 |
| `s 330(1) the person must make the required disclosure` | poca-failure.l4:227 | 2 | 1 |
| `s 330(4) the person must make the required disclosure to a nominated officer or an authorised person as soon as practicable` | poca-failure.l4:236 | 0 | 1 |
| `s 330(8) the court must consider whether he followed the guidance` | poca-failure.l4:254 | 0 | 1 |
| `s 330(9A) the disclosure is a disclosure to a nominated officer` | poca-failure.l4:281 | 2 | 0 |
| `s 330(10) the information or other matter came to the adviser in privileged circumstances` | poca-failure.l4:298 | 2 | 0 |
| `s 330(13) the body is an appropriate body` | poca-failure.l4:323 | 1 | 0 |
| `s 330(14) the person is a relevant professional adviser` | poca-failure.l4:334 | 1 | 0 |
| `s 331(5) the disclosure is the required disclosure` | poca-failure.l4:395 | 1 | 0 |
| `s 331(5A) the property is the laundered property` | poca-failure.l4:407 | 1 | 0 |
| `s 331(1) the person commits an offence` | poca-failure.l4:468 | 2 | 0 |
| `s 331(1) the nominated officer must make the required disclosure` | poca-failure.l4:481 | 2 | 1 |
| `s 331(4) the nominated officer must make the required disclosure to an authorised person as soon as practicable` | poca-failure.l4:490 | 0 | 1 |
| `s 331(7) the court must consider whether he followed the guidance` | poca-failure.l4:508 | 0 | 1 |
| `s 331(9) the body is an appropriate body` | poca-failure.l4:524 | 1 | 0 |
| `s 332(5B) the section is the applicable section` | poca-failure.l4:540 | 1 | 0 |
| `s 332(5) the disclosure is the required disclosure` | poca-failure.l4:593 | 1 | 0 |
| `s 332(5A) the property is the laundered property` | poca-failure.l4:605 | 1 | 0 |
| `s 332(1) the person commits an offence` | poca-failure.l4:642 | 2 | 0 |
| `s 332(1) the nominated officer must make the required disclosure` | poca-failure.l4:655 | 2 | 1 |
| `s 332(4) the nominated officer must make the required disclosure to an authorised person as soon as practicable` | poca-failure.l4:664 | 0 | 1 |
| `s 340(2) the conduct is criminal conduct` | poca-interp.l4:29 | 1 | 0 |
| `s 340(3) the property is criminal property` | poca-interp.l4:44 | 1 | 0 |
| `s 340(5) the person benefits from the conduct` | poca-interp.l4:76 | 1 | 0 |
| `s 340(6) the sum of money he is taken to obtain, in pounds` | poca-interp.l4:87 | 0 | 1 |
| `s 340(8) the property is his benefit` | poca-interp.l4:106 | 1 | 0 |
| `s 340(10)(a) the property is obtained by the person` | poca-interp.l4:140 | 1 | 0 |
| `s 340(10)(b) the thing is an interest in land in England and Wales or Northern Ireland` | poca-interp.l4:151 | 1 | 0 |
| `s 340(10)(c) the thing is an interest in land in Scotland` | poca-interp.l4:161 | 1 | 0 |
| `s 340(11) the act is money laundering` | poca-interp.l4:189 | 1 | 0 |
| `s 339ZH(1) the court may make an information order` | poca-orders.l4:150 | 1 | 1 |
| `s 339ZH(2) the application has the content it must have` | poca-orders.l4:163 | 1 | 0 |
| `s 339ZH(3) the information order requires the respondent to provide the information` | poca-orders.l4:177 | 1 | 1 |
| `s 339ZH(7) the information order has the content it must have` | poca-orders.l4:190 | 1 | 0 |
| `s 339ZH(8) the magistrates' court may order the person to pay the amount` | poca-orders.l4:200 | 2 | 0 |
| `s 339ZH(9) the sum is treated as adjudged to be paid by a conviction of the court` | poca-orders.l4:210 | 0 | 1 |
| `s 339ZH(12) the applicant is a relevant person` | poca-orders.l4:288 | 1 | 0 |
| `s 339ZL(7) the failure of itself makes the person liable to criminal or civil proceedings` | poca-orders.l4:304 | 1 | 1 |
| `s 339ZL(8) the code is admissible in evidence and is to be taken into account` | poca-orders.l4:314 | 0 | 1 |
| `s 339ZI(1) the statement may be used in evidence against the person in criminal proceedings` | poca-orders.l4:333 | 1 | 2 |
| `s 339ZI(4) the prosecution is a prosecution for perjury` | poca-orders.l4:345 | 1 | 0 |
| `s 339ZI(3) use of the statement by virtue of subsection (2)(c) is barred` | poca-orders.l4:360 | 1 | 0 |
| `s 339ZI(2) subsection (1) does not apply` | poca-orders.l4:375 | 0 | 1 |
| `s 339ZJ(1) an appeal lies to the relevant appeal court` | poca-orders.l4:388 | 0 | 1 |
| `s 339ZJ(2) the appeal lies at the instance of the person` | poca-orders.l4:397 | 0 | 1 |
| `s 339ZK(2) the information is privileged information` | poca-orders.l4:451 | 1 | 0 |
| `s 339ZK(1) the information order confers the right to require the person to provide the information` | poca-orders.l4:460 | 1 | 1 |
| `s 339ZK(3) the provision is not to be taken to breach a restriction on the disclosure of information` | poca-orders.l4:469 | 0 | 1 |
| `s 339ZK(4) the application may be heard and determined in private` | poca-orders.l4:478 | 0 | 1 |
| `sch 9 para 1(1) the business is in the regulated sector to the extent that it consists of a listed activity` | poca-sch9.l4:300 | 1 | 0 |
| `sch 9 para 1(4)(d)(ii) the service is acting as a nominee shareholder for a person other than a listed company` | poca-sch9.l4:381 | 1 | 0 |
| `sch 9 para 1(6C) the thing done is letting agency work` | poca-sch9.l4:446 | 1 | 1 |
| `sch 9 para 2(1) the business is in the regulated sector to the extent that it consists of an excluded activity` | poca-sch9.l4:667 | 1 | 1 |
| `sch 9 para 2(3) the business is in the regulated sector to the extent that it consists of financial activity` | poca-sch9.l4:702 | 1 | 1 |
| `sch 9 para 2(4) the business is in the regulated sector` | poca-sch9.l4:726 | 1 | 1 |
| `sch 9 paras 1 and 2 the business is in the regulated sector` | poca-sch9.l4:751 | 3 | 0 |
| `sch 9 para 3(3) the term has the same meaning in this Part as in that Regulation or Directive` | poca-sch9.l4:798 | 0 | 1 |
| `sch 9 para 4(1) the body is a supervisory authority` | poca-sch9.l4:818 | 1 | 0 |
| `s 339A(3) the person may specify the threshold amount for acts done in operating an account` | poca-threshold.l4:51 | 1 | 1 |
| `s 339A(4) the person may vary the threshold amount for acts done in operating an account` | poca-threshold.l4:62 | 1 | 1 |
| `s 339A(5) different threshold amounts may be specified for different acts on the same account` | poca-threshold.l4:72 | 0 | 1 |
| `s 339A(6) the specified amount is one that may be specified as the threshold amount` | poca-threshold.l4:83 | 1 | 0 |
| `s 339A(6A) the threshold amount for acts done to terminate a business relationship, in pounds` | poca-threshold.l4:94 | 0 | 1 |
| `s 339A(8) the account is related to the other` | poca-threshold.l4:106 | 1 | 0 |
| `s 333A(2) the matter is within subsection (2)` | poca-tipping.l4:38 | 3 | 0 |
| `s 333A(1) the person commits an offence by disclosing a matter within subsection (2)` | poca-tipping.l4:57 | 5 | 1 |
| `s 333A(3) the person commits an offence by disclosing an investigation` | poca-tipping.l4:79 | 4 | 0 |
| `s 333C(1) this section applies to the disclosure` | poca-tipping.l4:200 | 1 | 0 |
| `s 333E(5) the person is a relevant professional adviser` | poca-tipping.l4:357 | 1 | 0 |
<!-- MARGINAL:END -->

## Findings: what the text turns out to say

1. Section 340(2) and (3) are in the deposited text (lines 775 to 780), contrary to the brief; the two definitions are encoded and asserted (`poca-tests-interp.l4`). Asserted.
2. Schedule 9 comes without paragraph numbers; the labels `sch 9 para N` are this encoding's (fork F1). Not asserted.
3. Section 333 is shown as a row of dots; it is blank in this text. Not asserted (coverage row).
4. A person does not commit a section 327, 328 or 329 offence unless the property is criminal property, and property is criminal property under s 340(3) only if the person knows or suspects that it constitutes or represents a benefit from crime; so a person who does not know or suspect commits none of the three. Asserted (`poca-tests-dealing.l4`, `poca-tests-interp.l4`).
5. The exceptions of s 327(2C), (2D) and (2F) and their twins in ss 328 and 329 turn on a value being "less than" the threshold (2C, 2D) or "not less than" the criminal part (2F): a value equal to the threshold is not excepted, and a value equal to the criminal part is. Asserted.
6. The default threshold amount is 3,000 pounds; a "higher amount" specified under s 339A(3) or (4) replaces it, and an amount that is not higher leaves the default. Asserted (`poca-tests-threshold.l4`, seat cases).
7. Adequate consideration is a defence to s 329 only; it is no defence to ss 327 or 328. Asserted.
8. Section 330 and s 331 have an objective limb ("reasonable grounds for knowing or suspecting"); s 332 has only "knows or suspects". Asserted.
9. Section 330(7): a person who does not know or suspect, and whose employer has not given the training the Secretary of State specifies, is excepted; once trained, the exception is gone. Asserted. (My first hand expectation for the seat case was the reverse; the encoding was right and the expectation was the error, corrected from s 330(7)(a) and (b), not from the output.)
10. Section 330(6)(b)(i) is satisfied vacuously by an adviser who knows neither of the things in subsection (5)(a) and (b) (fork F5). Asserted.
11. The lists of recipients differ from section to section: s 337(4) names a constable, a customs officer, a nominated officer and a person authorised by the Director General, and not an officer of Revenue and Customs, while ss 333A(2) and 339ZA name an officer of Revenue and Customs and not a customs officer. Asserted for s 337(4) and s 333A(2).
12. Section 333D(3) excuses only an offence under s 333A(1), and s 333D(4) only one under s 333A(3). Asserted.
13. Section 333A(2) is a closed list of four recipients of the earlier disclosure; a disclosure to anyone else is not a matter within subsection (2). Asserted.
14. The offence of s 339(1A) is punished by a fine on summary conviction only (s 334(3)); the text says nothing of conviction on indictment, so that case is `NOTHING`. Asserted.
15. Under s 335(2) the person is treated as having the appropriate consent only when the notice period has run without refusal, or the refusal was followed by the whole moratorium period; the deemed consent is not available on the last day of either period. Asserted.
16. A statement made in response to an information order may not be used against the person (s 339ZI(1)); where an exception of s 339ZI(2) applies the bar goes and the text says nothing about admissibility, so the answer is `NOTHING`, not `JUST TRUE`. Asserted.
17. An information order does not confer the right to require privileged information (s 339ZK(1)); where the information is not privileged the section is silent, so `NOTHING`. Asserted.
18. A magistrates' court may order a payment of up to 5,000 pounds for failing to comply with an information order (s 339ZH(8)); 5,001 is outside; "another court" cannot make the order (s 339ZH(1)). Asserted.
19. The extension of a moratorium period under s 336A may end no later than 31 days beginning with the day after the day it would otherwise end, and further extensions may not take the total beyond 186 days (s 336A(4), (7)). Asserted.
20. Section 339ZD(3) treats a joint disclosure report as the required disclosure only if it is a joint disclosure report, which s 339ZD(4) makes depend on its being sent within the applicable period; a report sent the day after the last day is therefore not covered and the answer is `NOTHING`, not no. (My first hand expectation for that seat case was `JUST TRUE`, a slip; the encoding was right and the expectation was corrected from s 339ZD(4).) Asserted.
21. Words the text leaves to others stay inputs: "reasonable excuse", "likely to prejudice", "significantly less", "as soon as is practicable", "reasonable grounds" and the equivalence of a foreign country's requirements are asked as yes/no, never decided. Not asserted.

22. Under the ruling of 2026-11-05, a protection that the text states with its conditions is JUST FALSE when one fails: information that came to the person in private life (s 337(2)), a disclosure to anyone s 337(4) does not name (a journalist, an officer of Revenue and Customs), and a disclosure that was not made as soon as practicable are each JUST FALSE under s 337(1). Asserted (`poca-tests-disclose.l4`, `poca-cases-seat.l4`).
23. A person authorised by the Director General of the National Crime Agency is a constable (s 340(13)): the appropriate consent of s 335(1) can be given by such a person to a disclosure made to such a person, and s 339ZA and s 339A(3) and (4) apply to such a person (fork F13). Asserted.
24. The latest day to which a moratorium period may be extended in total is the last day of the 31 day period plus 186 days (s 336A(7), counted as s 336A(4) counts); a day beyond it is JUST FALSE, a day within it is NOTHING because the permission is in subsections (1) and (8). Asserted.
25. Section 339(1) names one holder of the power to prescribe the form and manner of a disclosure, the Secretary of State; what an order prescribes is not in the sources, and the offence of s 339(1A) takes the person's statement that a form and manner are prescribed. Asserted.
26. Schedule 9 para 1(4)(d)(ii) takes a nominee shareholder for a company whose securities are listed on a regulated market out of that limb in the text's own words (JUST FALSE for the limb); the list of services in para 1(4) as a whole is open and stays NOTHING. Asserted.
27. Sections 330(4), 331(4) and 332(4) say "as soon as is practicable" and give no number: there is no function that computes a deadline or says a disclosure was late. The conditions take the person's statement and the `MUST` has no `WITHIN`. This is a stated gap, recorded under those three coverage rows. Not asserted.

28. A business that is in none of the heads (a) to (v) of Schedule 9 para 1(1) is not in the regulated sector (JUST FALSE), because the Act hands the question to the Schedule (s 330(12)(a) and its siblings), and a body in none of the heads of para 4(1) is not a supervisory authority (JUST FALSE; ss 330(12)(b), 331(8), 333E(1)(b)). Asserted (`poca-tests-sch9.l4`, `poca-cases-seat.l4`).
29. Under s 339A(3) an officer of Revenue and Customs, a constable or an NCA-authorised person may specify the threshold only on the occasions the subsection names (when giving consent, when giving notice refusing consent, on a request); on any other occasion the answer is JUST FALSE. Asserted.

## What the main binary does not accept

- Record update (`base WITH a IS ...` on an existing value) is not available; tests build whole records or pass BOOLEAN arguments positionally.
- `EMPTY LIST OF DATE` is a parse error; the empty list is `EMPTY`.
- `WAIT UNTIL` is spelled `WAITUNTIL n` in `#TRACE`.
- A `DEONTIC` value cannot be compared with `EQUALS`, so a regulative rule is run with `#TRACE` and read, and each duty has a decision-function twin that is asserted (as the brief asks).
- A `MUST` with no `WITHIN` never breaches by the passing of time (traced), and a conditional `SHANT` with no `WITHIN` works; the "as soon as practicable" duties therefore have no deadline (fork F7).
- Every `NOT` is parenthesised, every `#ASSERT` is one line, a record literal is positional (`Type OF a, b`), and `Date day month year` is used; nothing from `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` (other than `LEST BREACH ... BECAUSE`) is used.
- A name defined in two imported modules cannot be used, so every function name carries its section number and the seat layer defines only wiring names; a record literal's field names may repeat inside one module (`P is carrying on business in the regulated sector`) without harm.
- The seat layer imports all ten layer-1 modules at once; this works on both builds.
- Nothing else I wrote was rejected by build 1.6.109 or by build 1.6.108, and both read every module the same way (`check.sh`).

## Unstable dialect

I looked at time (the notice period of s 335(5), the moratorium of s 335(6) and its extensions in ss 336A and 336C, deadlines counted from events), at rule versions (the edition is one point in time, 2026-06-30, so no rule is in force on different dates in the text deposited) and at workarounds (the working-day arithmetic is a recursive function over `Date` with an input list of holidays; the duties of "as soon as is practicable" have no number to put in a `WITHIN`), and found no shape that earns a second encoding; I did not write one and did not run the unstable build.

## Dependencies

Each Act or instrument that a provision of this range borrows a meaning or a fact from, and that is not among the sources, is taken as a named input; none is filled from memory.
Each is **a named input, to fill later**: when a row for the instrument exists on main, the input becomes a call.
Line numbers are those of the deposited texts: `p7:N` for `ukpga-2002-29-part-7.txt` and `sch9:N` for `ukpga-2002-29-schedule-9.txt`.
A provision that borrows nothing is not listed.

1. **Interpretation Act 1978**
   - ss 327(1), 328(1), 329(1), 330(1), 331(1), 332(1), 333A(1), 336(5), 339(1A): "person", wherever the Part says "a person" (p7 passim).
   - ss 333A(4)(a), 334(1)(a), 334(2)(a), 336(6)(a): "month" (p7:268, 332, 335, 379).
   - ss 335(5), 335(6), 336(7), 336(8), 336A(4), 336A(7), 336C(5), 336C(8), 339ZD(6)(b): counting of days, working days and periods (p7:351, 352, 381, 382, 394, 397, 445, 453, 585).
   - Borrowed: the meaning of "person" (it includes a body corporate) and of "month" (a calendar month), and the rule for counting a period.
   - Taken now: months are the numbers the text prints (3 and 6); periods are counted by this row's own rule (fork F9); the person is the seat's "I".  The Act's own row in Commons targets unstable and cannot be copied into a main row.  The section is the Act's section 5 with Schedule 1, cited from memory and not among the sources: check it when the row is filled..
2. **Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017**
   - ss 327(2E)(c), 328(7)(c), 329(2E)(c): "customer due diligence duties" are the duties imposed by regulation 28(2), (3), (3A), (4), (8) or (10) (p7:33, 69, 108).
   - s 333D(1)(a): "the supervisory authority for that person by virtue of" the Regulations (p7:301).
   - sch 9 para 1(1)(b), (ia), (ii): the activities listed in Schedule 2 to the Regulations (points 2 to 12, 14 and 15; point 7) (sch9:6, 12).
   - sch 9 para 1(5): "regulated market" has the meaning given by regulation 3(1) (sch9:61).
   - Borrowed: which duties are customer due diligence duties; who is a person's supervisory authority; which activities Schedule 2 lists; what a regulated market is.
   - Taken now: a yes/no input at each use (the person says whether the duty, authority, listed activity or regulated market is one); the Schedule 9 rules answer NOTHING (points outside the text) where only the Regulations could decide.
3. **Orders and regulations of the Secretary of State and the Treasury that Part 7 and Schedule 9 point to (not themselves among the sources)**
   - ss 327(2A)(b)(ii), 328(3)(b)(ii), 329(2A)(b)(ii): conduct "of a description prescribed by an order made by the Secretary of State" (p7:18, 54, 93).
   - ss 327(2E)(a), 328(7)(a), 329(2E)(a): business "excluded" if of a description specified in regulations (p7:31, 67, 106).
   - s 330(7)(b): the training "specified by the Secretary of State by order" (p7:152).
   - ss 330(7C)(b)(ii), 331(6A)(b)(ii), 332(7)(b)(ii): conduct "prescribed in an order made by the Secretary of State" (p7:161, 216, 249).
   - s 336D(7)(h): an accredited financial investigator within a description specified in an order (p7:476).
   - s 339(1): the form and manner of a disclosure (p7:521).
   - s 340(14)(c), (14A)(b): persons specified in regulations (p7:810, 813).
   - Borrowed: the content of each order or regulation.
   - Taken now: a yes/no input at each use ("is the conduct of a description prescribed?", "has the employer given the specified training?"); s 339(1) names the holder of the power and nothing more.
4. **Directive 2002/87/EC (financial conglomerates)**
   - s 333B(3): "group" (p7:280).
   - Borrowed: the meaning of "group".
   - Taken now: NOTHING (points outside the text) where the answer turns on it.
5. **Directive 2015/849/EU as amended by Directive 2018/843, and the Data Protection Act 2018 (Parts 5 to 7; section 3(2) and (14))**
   - s 333C(2)(d): "equivalent duties of professional confidentiality and the protection of personal data" (p7:298).
   - s 333E(4): a country imposes "equivalent money laundering requirements" (p7:326).
   - Borrowed: what is equivalent to the Directive's requirements, and the Act's meaning of protection of personal data.
   - Taken now: a yes/no input at each use; NOTHING (points outside the text) where a failure cannot be shown from the text.
6. **Immigration Act 2014 (sections 40 and 40A) and Social Security Administration Act 1992 (Schedule 3B, paragraph 1(1))**
   - ss 330(7D), 331(6B): information obtained only in consequence of a status check or an immigration check (p7:162-163, 217-218).
   - ss 330(7E), 331(6C): information obtained only in consequence of an eligibility verification notice (p7:165-166, 220-221).
   - Borrowed: whether a check or notice was one of those Acts' checks or notices.
   - Taken now: a yes/no input at each use.
7. **Banking and Financial Dealings Act 1971**
   - ss 335(7), 336(9), 336D(9)(e): a working day is not a day that is a bank holiday under the Act in the part of the United Kingdom where the person (or the application) is (p7:356, 383, 483).
   - Borrowed: which days are bank holidays.
   - Taken now: a list of dates the person gives (Good Friday and the bank holidays); Christmas Day, Saturdays and Sundays are computed.
8. **Senior Courts Act 1981 (section 28)**
   - s 336B(11): rights of appeal from the Crown Court in England and Wales (p7:435).
   - Borrowed: the right of appeal.
   - Taken now: NOTHING (points outside the text).
9. **Magistrates' Courts Act 1980 and Magistrates' Courts (Northern Ireland) Order 1981**
   - s 339ZH(9): the sum is treated as adjudged to be paid by a conviction "for the purposes of" those enactments (p7:699).
   - Borrowed: what follows from being treated as a conviction for the purposes of those enactments.
   - Taken now: the rule says the treatment is given (JUST TRUE) and nothing of what follows.
10. **Crime and Courts Act 2013 (section 1(5))**
   - s 339ZH(12): "the criminal intelligence function" (p7:706).
   - Borrowed: the meaning of the term.
   - Taken now: NOTHING (points outside the text).
11. **Perjury Act 1911 (section 5) and Perjury (Northern Ireland) Order 1979 (Article 10)**
   - s 339ZI(4): a prosecution for perjury (p7:739-740).
   - Borrowed: which offence is perjury in each part.
   - Taken now: the rule names the part of the United Kingdom and takes "a prosecution for perjury" as the fact.
12. **Electronic Money Regulations 2011 (regulation 2), Payment Services Regulations 2017 (regulation 2) and Financial Services and Markets Act 2000 (section 22)**
   - s 340(14C): "electronic money institution" (p7:815).
   - s 340(16): "payment institution" (p7:817).
   - s 340(14A)(a): accepting deposits as a regulated activity "by virtue of an order under section 22" (p7:812).
   - Borrowed: the meanings of the three terms.
   - Taken now: NOTHING (points outside the text) where the answer turns on one of them.
13. **Financial Services and Markets Act 2000, its (Regulated Activities) Order 2001 (S.I. 2001/544) and its (Exemption) Order 2001**
   - sch 9 para 1(1)(c): an authorised person under section 31, with permission under Part 4A (sch9:13).
   - sch 9 para 1(1)(d): "investment firm" in article 3(1) of the Order (sch9:14).
   - sch 9 para 1(1)(f), 1(2A): article 33B(4), article 3(1) and Part II of Schedule 1 (long-term insurance) (sch9:16, 45).
   - sch 9 para 2(1)(c), 2(1)(g): persons exempt under the Exemption Order; local authority under article 3(1) (sch9:103, 107).
   - Borrowed: who is an authorised person, an investment firm, an insurance intermediary, an exempt person or a local authority.
   - Taken now: a yes/no input at each use.
14. **Capital Requirements Regulation (Regulation (EU) No. 575/2013), Markets in Financial Instruments Directive (2014/65/EU), Solvency 2 Directive (2009/138/EC) and Emission Allowance Auctioning Regulation (Commission Regulation (EU) No. 1031/2010)**
   - sch 9 para 1(2): "credit institution" (Article 4(1)(1) and (17) of the Capital Requirements Regulation) (sch9:43-44).
   - sch 9 para 1(1)(d): the Markets in Financial Instruments Directive (sch9:14).
   - sch 9 para 1(1)(s), (t), 1(9): the Emission Allowance Auctioning Regulation (sch9:36, 37, 80).
   - sch 9 para 3(1), (3): the four definitions, and terms used in this Part and in those instruments (sch9:130-138).
   - Borrowed: the meanings of the terms.
   - Taken now: a yes/no input at each use; NOTHING (points outside the text) where only the instrument could decide.
15. **Consumer Credit Act 1974 (sections 10(1)(b) and 12(a)), National Loans Act 1968, Companies Act 2006 (section 1210; Part 42), Local Audit and Accountability Act 2014 (Schedule 5), Insolvency Act 1986 (section 388), Insolvency (Northern Ireland) Order 1989 (article 3), Gambling Act 2005 (section 65(2))**
   - sch 9 para 1(1)(b)(ia): a creditor within the Consumer Credit Act (sch9:9-10).
   - sch 9 para 1(1)(i): money raised under the National Loans Act (sch9:19).
   - sch 9 para 1(1)(j), (ja), (k): statutory audit, local audit, insolvency practice (sch9:20-22).
   - sch 9 para 1(1)(r): a casino operating licence (sch9:35).
   - Borrowed: the meanings of the terms.
   - Taken now: a yes/no input at each use.
16. **Estate Agents Act 1979 (section 1), Value Added Tax Act 1994 (section 21(5)(a), (6) to (6B)), Customs and Excise Management Act 1979 (section 100A(1))**
   - sch 9 para 1(6A): estate agency work (sch9:63).
   - sch 9 para 1(10): a work of art (sch9:81).
   - sch 9 para 1(11): a freeport (sch9:82).
   - Borrowed: the meanings of the terms.
   - Taken now: NOTHING (points outside the text) where only the Act could decide.
17. **Co-operative and Community Benefit Societies Act 2014 (section 24), Industrial and Provident Societies Act (Northern Ireland) 1969 (section 6), Financial Services Act 1986 (section 45), Housing (Scotland) Act 2006 (sections 98, 99(1), 101(2))**
   - sch 9 para 2(1)(a), (b), (d), (h): the excluded activities (sch9:101, 102, 104, 108).
   - Borrowed: the limits of the excluded activities.
   - Taken now: a yes/no input at each use.

## What check.sh prints

<!-- CHECK:BEGIN -->
Run as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` on 2026-11-05 (your l4: 1.6.109 (main, 4c887e0, 2026-11-04), sha256 eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb; the main build it compared with is named on the second line below, sha256 4159128db3bb804afff82aa3319caf320267ea0acf459cedc5483ee173c06e64):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
poca-cases-seat.l4                             0       281       0        0         0 |      0       281       0        0  same
poca-consent.l4                                0         0       0        0         0 |      0         0       0        0  same
poca-dealing.l4                                0         0       0        0         0 |      0         0       0        0  same
poca-disclose.l4                               0         0       0        0         0 |      0         0       0        0  same
poca-failure.l4                                0         0       0        0         0 |      0         0       0        0  same
poca-interp.l4                                 0         0       0        0         0 |      0         0       0        0  same
poca-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
poca-orders.l4                                 0         0       0        0         0 |      0         0       0        0  same
poca-sch9.l4                                   0         0       0        0         0 |      0         0       0        0  same
poca-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
poca-tests-consent.l4                          0       227       0        0         0 |      0       227       0        0  same
poca-tests-dealing.l4                          0       208       0        0         0 |      0       208       0        0  same
poca-tests-disclose.l4                         0       219       0        0         0 |      0       219       0        0  same
poca-tests-failure.l4                          0       217       0        0         0 |      0       217       0        0  same
poca-tests-interp.l4                           0        70       0        0         0 |      0        70       0        0  same
poca-tests-orders.l4                           0       122       0        0         0 |      0       122       0        0  same
poca-tests-sch9.l4                             0       196       0        0         0 |      0       196       0        0  same
poca-tests-threshold.l4                        0        28       0        0         0 |      0        28       0        0  same
poca-tests-tipping.l4                          0       105       0        0         0 |      0       105       0        0  same
poca-threshold.l4                              0         0       0        0         0 |      0         0       0        0  same
poca-tipping.l4                                0         0       0        0         0 |      0         0       0        0  same
TOTAL (21 modules)                             0      1673       0        0           |      0      1673       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```
<!-- CHECK:END -->

No baseline numbers were replaced: this encoding was written from nothing, so there is no earlier run.
No assertion fails on purpose, so `check.sh`'s `expected_failed` lists none and `encoding.json` has no `expected_red`.
The `#TRACE` outcomes are not counted by `check.sh`; I compared the 37 traces of the five test files that have them (consent 3, disclose 11, dealing 8, failure 10, tipping 5) between build 1.6.109 and build 1.6.108 and they are identical.

## Open questions and what would need doing before this encoding is worth relying on

1. A lawyer should read the two readings in "Marginal readings for a lawyer" against the text, forks F3 to F6, and the clauses in F12 where I could not tell which of (a), (b) and (c) applied, and F14.
2. The Schedule 9 paragraph numbers (F1) should be checked against the official text, and the whole of both texts against the official text; the deposited renderings are converter output, may carry more than one extent version of a provision, and do not mark prospective provisions.
3. The instruments Part 7 points to are not among the sources (the Money Laundering Regulations 2017, the Secretary of State's orders and regulations, the Directives, the Crime and Courts Act 2013); a second pass could bring in the ones that set numbers or dates.
4. The seat's Schedule 9 question takes the person's conclusion on para 1(1) (F10); a question per limb could be generated from layer 1.
5. `encoding.json` names `legalese` as maintainer and Apache-2.0 as the licence, as `references/canon-deposit.md` says canon encodings carry; the maintainer line is for the owner to confirm.
6. No domain expert has read this encoding.
