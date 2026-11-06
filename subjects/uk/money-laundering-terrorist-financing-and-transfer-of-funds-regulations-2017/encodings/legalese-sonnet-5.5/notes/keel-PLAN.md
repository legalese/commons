# PLAN -- the five part agents of the Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (S.I. 2017/692), United Kingdom

STATUS (2026-11-05): written by the keel after `mlr-core.l4`, `mlr-definitions.l4` and `mlr-definitions-tests.l4` compiled and checked.
**The text is not the official text**: it is `uksi-2017-692.txt`, a plain-text rendering made by a converter script.
Line numbers are those of that file.
How each claim below was established: the ranges are copied by script from `inputs/PARTS.md`; the core's contents are read by script from `mlr-core.l4`; the use counts are computed from the text (a count is a pointer to where to look, not a promise); the seams were chosen by reading the line each cross-reference sits on, and every seam row cites that line.
Where a seam needs a term this keel encoded, it is in `mlr-definitions.l4`, which the parts do NOT get.

## 1. The naming rule every part follows

- **Every top-level name a part defines begins with the label of the provision it implements**, in the form `reg 28(3)(a) ...`, `reg 30A(8) ...` or `sch 3 para 2 ...` (the Regulations' own numbering).
  Functions, constants and **constructors of an enumeration** alike.
  A constructor the part needs is therefore, for example, `reg 93(1) a decision of the FCA`, not `a decision of the FCA`.
  Where the core already has the constructor (`high risk` in `Level of risk`, `Scotland` in `Part of the United Kingdom`), use the core's and define nothing.
  Reason: a name defined in two modules that are imported together cannot be used at all.
  The keel's 127 constructors (the core's and `mlr-definitions.l4`'s together) are plain phrases (`the settlor`, `a trustee`, ...): a listing over both files found no duplicate and none beginning with `reg` or `sch`, so no part can collide with them if it follows this rule.
- **The name must not claim more than the section says**: for the form, `reg 28(3) the relevant person must apply customer due diligence measures` and not `is customer due diligence applied` (an example of the form, not an encoding).
- **File names**: every module of part X begins with `X-` (`mlr1-...`); the keel's begin `mlr-`.
- **Types and constructors shared across parts live only in the core.**
  A part never edits the core and never waits for it.
  If a part needs a type or constructor the core lacks, it defines it in its own module under its own prefix and records it in `NEEDS-CORE.md` in its sandbox; the lead hoists it into the core at the merge.
- **A part imports `prelude`, `daydate` and `mlr-core` only.**
  It cannot import another part, and it does not get `mlr-definitions.l4`.
- **Answers**: a decision function answers `JUST FALSE` only where the text says no in its own words, and `NOTHING` everywhere else; each branch carries `-- FALSE-kind (...)` or `-- NOTHING-kind (...)`.
  A caller must never turn `NOTHING` into `FALSE`.
  The two readings flagged "for a lawyer" are listed in each part's `NOTES.md` under `## Marginal readings for a lawyer`; this keel's are in its `NOTES.md`.
- **Dates** are `Date day month year`; never define a `YMD`.
  Parenthesise every `NOT`: bare `NOT a AND b` parses as `NOT (a AND b)` on the main build (measured, `NOTES.md`).
  Keep each `#ASSERT` on one line.
  Infix `elem` is not accepted; write `elem x xs`.

## 2. How a seam input is typed and used

A provision in one part sometimes needs the answer of a provision in another part, or of a term this keel encoded.
A part cannot import either, so it takes that answer as an **input** (a `GIVEN` parameter of its own function, so it collides with nothing), named for the section the answer comes from: `<label of the answering section> <what it answers>`.
The seam ids (S-1, S-K1, ...) below are the contract.
**Both sides write the id in a comment**, `-- SEAM S-5 (asking)` above the asking function and `-- SEAM S-5 (answering)` above the answering one, so the lead can find both with one search at the merge and replace the input with a call.

The type of the input:
- **`MAYBE BOOLEAN`** when the input carries another section's *answer*, because that section's function answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.
  The asking function passes `NOTHING` through; it never reads it as `FALSE`.
  The pattern (the keel's own `reg 4(1) to (3) there is a business relationship` uses it):

```
IF `reg 27 the relevant person is required to apply customer due diligence measures` EQUALS JUST TRUE
THEN <the asking rule's yes>
ELSE IF `reg 27 the relevant person is required to apply customer due diligence measures` EQUALS JUST FALSE
    THEN <the asking rule's no, if its own words say no> -- FALSE-kind (...)
    ELSE NOTHING -- NOTHING-kind (points outside the text): the answering section has not answered
```

- **`BOOLEAN`, `NUMBER`, a core type or a record** when the input is a plain *fact* that a witness of ordinary competence could testify to (that a notice was given, that a person has been convicted).
  Those are never `MAYBE`.

## 3. The core, one line per type


- `Kind of relevant person` (enumeration): `credit institution`, `financial institution`, `auditor`, `insolvency practitioner`, `external accountant`, `tax adviser`, `independent legal professional`, `trust or company service provider`, `estate agent`, `letting agent`, `high value dealer`, `casino`, `art market participant`, `cryptoasset exchange provider`, `custodian wallet provider`, `auction platform`.
- `Professional body` (enumeration): `Association of Accounting Technicians`, `Association of Chartered Certified Accountants`, `Association of International Accountants`, `Association of Taxation Technicians`, `Chartered Institute of Legal Executives`, `Chartered Institute of Management Accountants`, `Chartered Institute of Taxation`, `Council for Licensed Conveyancers`, `Faculty of Advocates`, `Faculty Office of the Archbishop of Canterbury`, `General Council of the Bar`, `General Council of the Bar of Northern Ireland`, `Insolvency Practitioners Association`, `Institute of Certified Bookkeepers`, `Institute of Chartered Accountants in England and Wales`, `Institute of Chartered Accountants in Ireland`, `Institute of Chartered Accountants of Scotland`, `Institute of Financial Accountants`, `Institute of Accountants and Bookkeepers`, `Law Society`, `Law Society of Northern Ireland`, `Law Society of Scotland`.
- `Authority` (enumeration): `the Financial Conduct Authority`, `the Prudential Regulation Authority`, `the Commissioners for Her Majesty's Revenue and Customs`, `the Gambling Commission`, `the National Crime Agency`, `the Treasury`, `the Department for the Economy in Northern Ireland`, `a local weights and measures authority`, `a professional body listed in Schedule 1`.
- `Form of customer` (enumeration): `an individual`, `a company`, `a limited liability partnership`, `a body corporate of another kind`, `a corporation sole`, `a partnership other than a limited liability partnership`, `an unincorporated association`, `a trust`, `a foundation or other legal arrangement similar to a trust`, `the estate of a deceased person in the course of administration`, `another legal entity or legal arrangement`.
- `Part of the United Kingdom` (enumeration): `England and Wales`, `Scotland`, `Northern Ireland`.
- `Customer` (record): `form of the customer`, `securities listed on a regulated market`, `beneficially owned by another person`, `a person purports to act on its behalf`.
- `Transaction` (record): `value in sterling, linked operations taken together`, `paid in cash`, `carried out as part of a business relationship`, `a transfer of funds under the funds transfer regulation`.
- `Kind of cryptoasset transfer` (enumeration): `an inter-cryptoasset business transfer`, `an unhosted wallet transfer`.
- `Cryptoasset transfer` (record): `kind of transfer`, `value in sterling, linked transfers taken together`.
- `Kind of risk` (enumeration): `money laundering`, `terrorist financing`, `proliferation financing`.
- `Level of risk` (enumeration): `high risk`, `low risk`, `neither high nor low risk`.
- `Listed activity` (enumeration): `lending`, `financial leasing`, `payment services`, `issuing and administering other means of payment`, `guarantees and commitments`, `trading for own account or for account of customers`, `participation in securities issues and related services`, `advice to undertakings on capital structure, industrial strategy and mergers`, `money broking`, `portfolio management and advice`, `safekeeping and administration of securities`, `safe custody services`, `issuing electronic money`.
- Constants: `reg 1(2) the date these Regulations came into force` (a `DATE`, 26 June 2017) and `the transfer threshold of 800 pounds sterling` (a `NUMBER`).
  Each part chooses its own comparison against it ("exceeding" in reg 27(1)(b); "equal to or exceeds" in regs 27(7E), 64C(4) and 64G(1)(b)).

Notes on reading the core:
- Amounts in the core are **pounds sterling**, already converted; the conversion (reg 3(2)(a) and (b)) is the seat's step before a rule is asked, and the exchange rate is an input there (`mlr-definitions.l4`, fork F3 in `NOTES.md`).
- `Authority` holds every public body the Regulations name; "a supervisory authority" is a value of it picked out by reg 7 (seam S-K3), not a type of its own.
  A professional body of Schedule 1 is `a professional body listed in Schedule 1` applied to a `Professional body`.
- `Listed activity` names the 13 items of Schedule 2 and numbers none: the rendering prints them unnumbered, and reg 10 cites points 2 to 12, 14 and 15 (fork F4 in `NOTES.md`).
- `Customer` carries four facts a relevant person can state: the form, whether its securities are listed on a regulated market, whether another person beneficially owns it, whether a person purports to act for it.
  `Transaction` carries the sterling value (linked operations taken together), whether it is paid in cash, whether it is carried out as part of a business relationship (so an "occasional transaction" is its negation), and whether it is a transfer of funds under the funds transfer regulation.

Where each part will read the core (lines in the part's range whose words are the core's; a pointer for the part, not a promise):

| core name | mlr1 | mlr2 | mlr3 | mlr4 | mlr5 |
|---|---|---|---|---|---|
| Kind of relevant person | 84 | 11 | 54 | 9 | 22 |
| Professional body | 3 | 2 | 3 | 18 | 7 |
| Authority | 89 | 43 | 119 | 214 | 55 |
| Form of customer | 53 | 147 | 22 | 25 | 78 |
| Customer, Transaction | 138 | 98 | 26 | 5 | 16 |
| Part of the United Kingdom | 13 | 7 | 2 | 37 | 29 |
| Cryptoasset transfer, Kind of cryptoasset transfer | 2 | 3 | 34 | 0 | 3 |
| Kind of risk | 63 | 46 | 43 | 24 | 90 |
| Level of risk | 1 | 9 | 1 | 0 | 2 |
| Listed activity | 5 | 1 | 0 | 2 | 8 |
| the commencement date | 5 | 1 | 2 | 1 | 0 |
| the 800-pound figure | 2 | 0 | 2 | 0 | 0 |

Single-use figures are **not** in the core: £10,000 (regs 13, 14 and 27, all `mlr1`), £2,000 (reg 27, `mlr1`), £1,000 and £100,000 (reg 15, `mlr1`), £150 and £50 (reg 38, `mlr2`), the Schedule 3A figures (`mlr5`).
Each is the owning part's own constant, under its own prefix.
The commencement date is read by lines 639, 886, 890, 893, 894 (`mlr1`), 1142 (`mlr2`), 1858, 2009 (`mlr3`) and 2946 (`mlr4`).

## 4. What the parts do NOT get: the keel's definitions (regs 2 to 7)

`mlr-definitions.l4` encodes reg 3(1), reg 3(2), reg 4, reg 5, reg 6 and reg 7.
A part does not import it.
For each term below, the table gives how often the part's range uses it (lines are not counted; occurrences are) and what the part does instead.

| term | defined in | mlr1 | mlr2 | mlr3 | mlr4 | mlr5 | what a part does |
|---|---|---|---|---|---|---|---|
| relevant person | reg 8 (mlr1) | 148 | 93 | 30 | 25 | 27 | S-8 |
| business relationship | reg 4 (keel) | 21 | 36 | 7 | 0 | 0 | S-K1 |
| beneficial owner | regs 5 and 6 (keel) | 25 | 30 | 8 | 3 | 8 | S-K2 |
| supervisory authority | reg 7 (keel) | 62 | 2 | 57 | 54 | 14 | S-K3 |
| customer due diligence measures | reg 3(1) (keel) and reg 28 (mlr1) | 28 | 29 | 1 | 0 | 12 | pointer; no input |
| enhanced customer due diligence measures | reg 3(1) (keel) and regs 33 to 35 (mlr2) | 1 | 7 | 1 | 0 | 1 | pointer; no input |
| occasional transaction | reg 3(1) (keel) | 6 | 3 | 0 | 0 | 0 | the core field `carried out as part of a business relationship` |
| politically exposed person | reg 35(12) (mlr2) | 0 | 10 | 2 | 0 | 8 | left to mlr2 |
| cryptoasset business | reg 64B (mlr3) | 0 | 7 | 102 | 22 | 24 | left to mlr3 |
| law enforcement authority | reg 44(10) (mlr2) | 3 | 6 | 5 | 0 | 0 | S-15 |
| firm | reg 3(1) (keel) | 44 | 5 | 13 | 0 | 11 | S-K4 |
| officer | reg 3(1) (keel) | 9 | 2 | 10 | 69 | 4 | S-K4 |
| money service business | reg 3(1) (keel) | 6 | 0 | 15 | 0 | 0 | the core kind `financial institution` and the fact in S-K3 |
| regulated market | reg 3(1) (keel) | 3 | 3 | 0 | 0 | 0 | the core field `securities listed on a regulated market` |
| third country | reg 3(1) (keel) | 7 | 28 | 2 | 1 | 0 | a BOOLEAN input; the keel's function is a one-line test |
| document | reg 3(1) (keel) | 9 | 17 | 1 | 42 | 6 | a BOOLEAN input |
| notice | reg 3(1) (keel) | 16 | 0 | 15 | 84 | 7 | a BOOLEAN input |
| senior management | reg 3(1) (keel) | 4 | 4 | 2 | 0 | 0 | a BOOLEAN input |
| cash | reg 3(1) (keel) | 6 | 4 | 0 | 3 | 0 | the core field `paid in cash` |

A reg 3(1) term not in the table is used by few lines; if a part meets one, it takes the term as a `BOOLEAN` fact, or as `MAYBE BOOLEAN` if the keel's function for it can answer `NOTHING`, and writes `-- SEAM S-K4 (asking)` above the function.
Every term of reg 3(1) has a function in `mlr-definitions.l4` whose name begins `reg 3(1)`; `mlr-definitions-tests.l4` shows its inputs.

## 5. Seams

An id with `K` is an answer in the keel's definitions; the others are between two parts.
Each row: asking section (part), answering section (part), the input's name and type, and the line of the text that makes the ask.
"Asking" and "answering" are about the *text*: the asking section's words need the answer.

### 5.1 From the keel's definitions to the parts

| id | asking section (part) | answering section (keel) | input name and type | line |
|---|---|---|---|---|
| S-K1 | every rule that turns on a business relationship; lines per regulation (top eight): mlr1: reg 21 (1), reg 25 (4), reg 27 (1), reg 28 (4), reg 30 (2), reg 30ZA (1), reg 30A (5), reg 31 (2); mlr2: reg 33 (9), reg 35 (8), reg 37 (3), reg 38 (1), reg 40 (2), reg 43 (2), reg 44 (2), reg 45 (2); mlr3: reg 60A (2), reg 64D (2), reg 64E (1), reg 64G (2); mlr4: none; mlr5: none | reg 4 at 147-152 | `reg 4(1) to (3) there is a business relationship`, `MAYBE BOOLEAN` | reg 4 at 147-152 |
| S-K2 | every rule that turns on a beneficial owner; lines per regulation (top eight): mlr1: reg 26 (3), reg 27 (2), reg 28 (9), reg 29 (1), reg 30 (3), reg 30ZA (1), reg 30A (4); mlr2: reg 33 (3), reg 35 (5), reg 39 (2), reg 43 (3), reg 44 (3), reg 45 (5), reg 45ZA (4), reg 45ZB (7); mlr3: reg 48 (2), reg 57 (1), reg 58 (3), reg 58A (2); mlr4: sch 3AZA (2); mlr5: sch 6 (2), sch 6B (7), sch 7 (2) | regs 5 and 6 at 153-198 | `reg 5 and 6 the individual is a beneficial owner of the customer`, `MAYBE BOOLEAN`; the merge picks the keel's function by the customer's `Form of customer`: reg 5(1) for a company, a limited liability partnership or another body corporate; reg 5(3) for a partnership other than a limited liability partnership; reg 6(1) for a trust; reg 6(3) for a foundation or similar arrangement; reg 6(6) for an estate; reg 6(7) and (9) for any other | regs 5 and 6 at 153-198 |
| S-K3 | every rule that names a relevant person's supervisory authority; lines per regulation (top eight): mlr1: reg 16 (3), reg 17 (11), reg 18 (4), reg 18A (2), reg 21 (2), reg 23 (3), reg 25 (11), reg 26 (16); mlr2: reg 35 (1), reg 39 (1); mlr3: reg 46 (8), reg 47 (5), reg 50 (5), reg 51 (4), reg 52 (7), reg 52A (7), reg 57 (3), reg 63 (6); mlr4: reg 66 (7), reg 67 (6), reg 68 (4), reg 69 (3), reg 70 (7), reg 76 (8), reg 78 (4), reg 80 (3); mlr5: sch 4 (11), sch 6 (2), sch 6A (1), sch 7 (7) | reg 7 at 199-232 | `reg 7(1) the supervisory authorities of the relevant person`, `MAYBE (LIST OF Authority)` | reg 7 at 199-232 |
| S-K4 | reg 3(1) terms with no core type: "firm", "officer", "manager", "senior management", "nominated officer", "document", "notice", "third country" | reg 3(1) | one input per term, named for the term, e.g. `reg 3(1) the person is an officer of the entity`, `MAYBE BOOLEAN` where the keel's function can answer `NOTHING` (firm, officer, branch), `BOOLEAN` otherwise | reg 3(1) at 12-139 |

### 5.2 Between parts

| id | asking section (part) | answering section (part) | input name and type | line |
|---|---|---|---|---|
| S-1 | reg 33(3)(b) "relevant transaction"; reg 43(9); reg 44(4); reg 45ZB (`mlr2`) | reg 27 (`mlr1`) | `reg 27 the relevant person is required to apply customer due diligence measures`, `MAYBE BOOLEAN` | 1032, 1384, 1391, 1546 |
| S-3 | reg 30ZA(b) (`mlr1`) | reg 33(1) (`mlr2`) | `reg 33(1) enhanced customer due diligence is required`, `MAYBE BOOLEAN` | 930 |
| S-4 | reg 19 and reg 19A, the agent question (`mlr1`) | reg 58 (`mlr3`) | `reg 58 the agent satisfies the fit and proper test`, `MAYBE BOOLEAN` | 539, 569 |
| S-5 | reg 26(14) (`mlr1`); reg 57(1)(k), reg 58(3), reg 58A(3) (`mlr3`) | Schedule 3 (`mlr4`) | `sch 3 the offence is a relevant offence`, `MAYBE BOOLEAN` | 761, 1913, 1931, 1945 |
| S-6 | reg 30A(8) (`mlr1`) | Schedule 3AZA (`mlr4`) | `sch 3AZA the discrepancy is a material discrepancy`, `MAYBE BOOLEAN` | 976 |
| S-7 | reg 37 and reg 39(3) (`mlr2`) | reg 8 (`mlr1`) | `reg 8 the person is a relevant person`, `MAYBE BOOLEAN` | 1210, 1249, 1258 |
| S-8 | every rule of `mlr2` to `mlr5` that speaks of "a relevant person" (occurrence counts in section 4) | reg 8 (`mlr1`) | the same input as S-7 | wherever "relevant person" appears |
| S-9 | reg 54 (`mlr3`) | reg 23 (`mlr1`) | `reg 23 the person has notified the FCA that it is acting, or intends to act, as a money service business or a trust or company service provider`, `BOOLEAN` (a fact) | 1803 |
| S-10 | reg 55 (`mlr3`) | reg 10(2)(a) (`mlr1`) | `reg 10(2)(a) the person falls within regulation 10(2)(a)`, `MAYBE BOOLEAN` | 1826 |
| S-11 | reg 46(1)(b) (`mlr3`) | reg 26(7) (`mlr1`) | `reg 26(7) the application for approval meets the requirements of regulation 26(7)`, `MAYBE BOOLEAN` | 1608 |
| S-12 | reg 60 (`mlr3`) | reg 66 (`mlr4`) | `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66`, `BOOLEAN` (a fact) | 2006 |
| S-13 | reg 64B "cryptoasset" (`mlr3`) | reg 14A(3)(a) (`mlr1`) | `reg 14A(3)(a) the thing is a cryptoasset`, `MAYBE BOOLEAN` | 2105 |
| S-14 | reg 40 (`mlr2`) | regs 64C, 64D, 64G (`mlr3`) | `reg 64C, 64D or 64G the relevant person holds information or documents received under that regulation`, `BOOLEAN` (a fact) | 1276, 1278, 1279 |
| S-15 | reg 64H (`mlr3`) | reg 44(10) (`mlr2`) | `reg 44(10) the body is a law enforcement authority`, `MAYBE BOOLEAN` | 2199 |
| S-16 | reg 65(3) (`mlr4`) | Schedule 5 (`mlr5`) | `sch 5 the person is a connected person of the relevant person`, `MAYBE BOOLEAN` | 2215 |
| S-17 | reg 75 (`mlr4`) | Schedule 6 (`mlr5`) | `sch 6 the provision is a relevant requirement`, `MAYBE BOOLEAN` | 2451 |
| S-18 | regs 42, 45(10A), 45ZA (`mlr2`) | Schedule 3A (`mlr5`) | `sch 3A the trust is a trust listed in Schedule 3A`, `MAYBE BOOLEAN` | 1331, 1463, 1509 |
| S-19 | regs 93 and 99, the decisions that can be appealed (`mlr4`) | reg 25(2) (`mlr1`); reg 58, reg 59(1), reg 60 (`mlr3`) | four facts, `BOOLEAN` each: `reg 25(2) the decision is a direction`; `reg 58 the decision is that a person is not a fit and proper person, other than one required by regulation 58(3)`; `reg 59(1) the decision refuses to register an applicant`; `reg 60 the decision suspends or cancels a registration` | 2760-2762, 2826-2829 |

### 5.3 Where the ask is already answered by the core, so no input is needed

| asking | answering | how |
|---|---|---|
| reg 27 (`mlr1`) "cryptoasset" and "cryptoasset transfer" (line 804) | reg 64B (`mlr3`) | take the core `Cryptoasset transfer` (a record whose `kind of transfer` is one of the two kinds) as given |
| reg 10(2)(a), (3)(c), (4)(a) (`mlr1`); Schedule 3A (`mlr5`, line 3165: "points 2, 3, 6, 7 or 8 of ... Schedule 2"); Schedule 2 itself (`mlr4`) | the items of Schedule 2 | the core `Listed activity`; the numbering question is fork F4 (`NOTES.md`) |
| reg 55 (`mlr3`, line 1832) and the other rules that name "a professional body listed in Schedule 1" | Schedule 1 (`mlr4`) | the core `Professional body` and `Authority`; the Schedule's own row (`mlr4`) is the list in the core |
| S-2: the relevant person's risk assessment "have regard to" lists: reg 33(1)(a) (line 1013), reg 35 (1109), reg 37(1) (1173), and Part 7A, regs 64D(3), 64E, 64G (2155, 2171, 2187) (`mlr2`, `mlr3`) | reg 18(1) and 18A(1), and the information made available under reg 17(9) and reg 47 (`mlr1`, `mlr3`) | the finding is an input of core types: a `Level of risk` and a `Kind of risk`; whether the information made available identifies the case as high risk is a `BOOLEAN` fact; and "if it determines that the business relationship ... presents a low degree of risk" (reg 37(1)) is a judgement the text hands to the relevant person, so a conditional input, never computed |
| "occasional transaction" wherever it appears (`mlr1`, `mlr2`) | reg 3(1) (keel) | the core field `carried out as part of a business relationship`, negated |

### 5.4 Disapplications (a section that switches off another)

These do not need an input from the switched-off section; the *seat* combines two answers.
- **reg 38(1)** (`mlr2`, line 1221) says that regulations 27, 28, 30 and 33 to 37 do not apply to electronic money when its conditions are met.
  `mlr2` answers `reg 38(1) the relevant person is not required to apply customer due diligence measures in relation to electronic money`, `MAYBE BOOLEAN`; `mlr1` does not read it.
  The merge's seat decides which wins, and the text of reg 38(1) says it does ("do not apply").
- **reg 37** (`mlr2`) permits adjusting measures under regs 28 and 29(11) to (13) (line 1177); `mlr2` answers its own rule and `mlr1` does not read it.

### 5.5 References that are NOT seams

The scan for "regulation N" and "Schedule N" found references that point at another instrument's provision of the same number, and references that only describe content of a notice.
A part that meets one should not look for an answering section here:
- lines 281, 349, 836, 889, 955, 972, 973, 1080, 1102, 1141, 1238, 1315, 1821, 1843, 1857, 1860, 1883, 1957, 1998, 2008, 2014, 2015, 2741, 2983, 3143, 3149, 3180, 3182, 3183, 3264, 3537: the number belongs to another instrument or is a paragraph of a Schedule here (the Regulated Activities Order, the Economic Crime (Transparency and Enforcement) Act 2022, the Open-ended Investment Companies Regulations 2001, the Limited Liability Partnerships (Application of Companies Act 2006) Regulations 2009, the Scottish Partnerships (Register of People with Significant Control) Regulations 2017, the Terrorism Act 2000, the Financial Conglomerates and Other Financial Groups Regulations, the Data Protection Act 2018, the Money Laundering Regulations 2007, the Payment Services Regulations 2017, the UK auctioning regulations, the Magistrates' Courts (Northern Ireland) Order 1981, and others).
- lines 1971, 1972, 1988, 2021, 2022, 2034, 714: a notice must tell the person of a right of review (reg 94) or appeal (regs 93, 99); the content of the notice is the asking section's, and the right is `mlr4`'s.
  No answer crosses.
- line 525 (reg 19, "see regulations 39 to 40"), lines 1610 to 1631 (reg 46), 1640 and 1641 (reg 46A), 1654 and 1655 (reg 47), 1658 to 1667 (reg 48): lists of what a duty covers; the answer of the regulation named is not needed.
- lines 3220, 3224, 3227, 3228, 3234, 3235 (Schedule 4 asks a supervisory authority to count its decisions under regs 26, 59, 60 and its disclosures under reg 104): the Schedule names data to collect; no answer crosses.
- line 3108 (Schedule 3A, "the date on which regulation 42(2)(iii) of these Regulations comes into force"): a date the rendering does not give; `mlr5` takes it as an input `DATE`.
- line 2908 (reg 104A, Schedule 6A) and line 2943 (reg 109, Schedule 7): a pointer to another provision of this text; the owning part encodes the Schedule, and the pointing regulation is a pointer.

## 6. Per part


### mlr1

- **Line range (copied unchanged from `inputs/PARTS.md`):** 233-1008 (16127 words).
- **Seams it asks (asking side):** S-3 (reg 30ZA from reg 33(1)), S-4 (regs 19 and 19A from reg 58), S-5 (reg 26(14) from Schedule 3), S-6 (reg 30A(8) from Schedule 3AZA), and the keel's S-K1 to S-K4.
  It uses "relevant person" most (section 4), but reg 8 is its own: inside `mlr1`, reg 8 is a function, not an input.
- **Seams it answers (answering side):** S-1 (reg 27), S-2 (reg 18(1) and 18A(1): resolved by the core, section 5.3), S-7 and S-8 (reg 8), S-9 (reg 23), S-10 (reg 10(2)(a)), S-11 (reg 26(7)), S-13 (reg 14A(3)(a)), S-19 (reg 25(2)).
- **Definitions left to it:** the reg 3(1) pointers into regs 8 to 16A (section 7).
- **Difficulties:** reg 10(3)(c) and (4)(a) cite Schedule 2 by point number (fork F4); the exclusions in reg 15; reg 27 carries several sterling figures (only £800 is in the core: £10,000 for a high value dealer and for a monthly rent, £2,000 for a casino are this part's own constants); the commencement date is read at lines 639 (reg 23) and 886-894 (reg 29).
- **Where it will read the core** (regulation: lines whose words are the core's; a pointer, not a promise):
  - `Kind of relevant person`: reg 8 (12), reg 10 (5), reg 11 (7), reg 14 (6), reg 27 (10), reg 30ZA (6)
  - `Professional body`: reg 16A (1), reg 30A (2)
  - `Authority`: reg 16 (9), reg 16A (8), reg 17 (13), reg 23 (7), reg 25 (14), reg 26 (16)
  - `Form of customer`: reg 12 (9), reg 21 (8), reg 23 (3), reg 28 (6), reg 29 (4), reg 30A (8)
  - `Customer, Transaction`: reg 27 (30), reg 28 (22), reg 29 (15), reg 30 (7), reg 30ZA (13), reg 30A (10)
  - `Part of the United Kingdom`: reg 11 (1), reg 13 (1), reg 15 (4), reg 26 (3), reg 28 (1), reg 30A (2)
  - `Cryptoasset transfer, Kind of cryptoasset transfer`: reg 27 (2)
  - `Kind of risk`: reg 16 (7), reg 16A (11), reg 17 (6), reg 19 (6), reg 19A (6), reg 24 (5)
  - `Level of risk`: reg 21 (1)
  - `Listed activity`: reg 10 (4), reg 28 (1)
  - `the commencement date`: reg 23 (1), reg 29 (4)
  - `the 800-pound figure`: reg 27 (2)

### mlr2

- **Line range (copied unchanged from `inputs/PARTS.md`):** 1009-1585 (12444 words).
- **Seams it asks:** S-1 (regs 33(3)(b), 43(9), 44(4), 45ZB from reg 27), S-2 (regs 33, 35, 37: resolved by the core, section 5.3), S-7 (regs 37, 39(3)), S-8, S-18 (regs 42, 45(10A), 45ZA from Schedule 3A), and the keel's S-K1 to S-K4 (reg 43(3) at line 1376 names "beneficial owner (within the meaning of regulation 5(1))").
- **Seams it answers:** S-3 (reg 33(1)), S-15 (reg 44(10)), and the disapplication in reg 38(1) (section 5.4).
- **Definitions left to it:** the reg 3(1) pointers into regs 33 to 44 (section 7): correspondent relationship (34(4)), politically exposed person (35(12)), law enforcement authority (44(10)).
- **Difficulties:** reg 33(3) defines "FATF call for action country" by a list published elsewhere (line 1031); "high-risk third country" is only a pointer in reg 39(4) (line 1255) and Schedule 3ZA is all dots; regs 45 to 45ZB turn many times on Schedule 3A (`mlr5`); the commencement date is read at line 1142 (reg 35); reg 38 has its own small figures (£150, £50).
- **Where it will read the core** (regulation: lines whose words are the core's; a pointer, not a promise):
  - `Kind of relevant person`: reg 33 (2), reg 34 (6), reg 35 (1), reg 37 (1), reg 38 (1)
  - `Professional body`: reg 41 (1), reg 42 (1)
  - `Authority`: reg 35 (2), reg 36 (2), reg 44 (3), reg 45 (18), reg 45ZA (5), reg 45ZB (12)
  - `Form of customer`: reg 35 (10), reg 42 (21), reg 44 (15), reg 45 (51), reg 45ZA (25), reg 45ZB (16)
  - `Customer, Transaction`: reg 33 (34), reg 35 (14), reg 37 (11), reg 38 (8), reg 39 (7), reg 40 (8)
  - `Part of the United Kingdom`: reg 42 (2), reg 44 (2), reg 45 (1), reg 45ZB (2)
  - `Cryptoasset transfer, Kind of cryptoasset transfer`: reg 40 (3)
  - `Kind of risk`: reg 33 (12), reg 35 (3), reg 37 (14), reg 39 (6), reg 41 (4), reg 45ZB (3)
  - `Level of risk`: reg 33 (7), reg 37 (2)
  - `Listed activity`: reg 33 (1)
  - `the commencement date`: reg 35 (1)

### mlr3

- **Line range (copied unchanged from `inputs/PARTS.md`):** 1586-2199 (11719 words).
- **Seams it asks:** S-5 (regs 57(1)(k), 58(3), 58A(3) from Schedule 3), S-9 (reg 54), S-10 (reg 55), S-11 (reg 46), S-12 (reg 60), S-13 (reg 64B), S-15 (reg 64H), S-2 (regs 64D, 64E, 64G: resolved by the core, section 5.3), and the keel's S-K1, S-K3, S-K4.
- **Seams it answers:** S-4 (reg 58), S-14 (regs 64C, 64D, 64G), S-19 (regs 58, 59(1), 60).
- **Definitions left to it:** the reg 3(1) pointers into regs 53 to 64B (section 7): Annex 1 financial institution (55(2)), cryptoasset business and the Part 7A terms (64B), the transfer of funds supervisory authority (62), the telecommunication, digital and IT payment service provider (53).
- **Difficulties:** regs 45A to 45H (lines 1587-1604) are headings each followed by a line of dots, so Part 5A is blank in this rendering (record it as `repealed or blank in this text`); reg 56A is headed as a transitional provision for existing cryptoasset businesses; "working day" is defined at line 2119 for Part 7A only (fork F3); Part 7A's £800 figure is read at lines 2125 and 2185 (the core constant); the commencement date is read at lines 1858 (reg 56) and 2009 (reg 60).
- **Where it will read the core** (regulation: lines whose words are the core's; a pointer, not a promise):
  - `Kind of relevant person`: reg 52A (7), reg 54 (7), reg 55 (8), reg 56 (8), reg 56B (4), reg 60 (5)
  - `Professional body`: reg 46 (1), reg 55 (1), reg 63 (1)
  - `Authority`: reg 46 (10), reg 47 (8), reg 52 (9), reg 52A (11), reg 54 (8), reg 60 (10)
  - `Form of customer`: reg 48 (3), reg 54 (2), reg 56 (2), reg 57 (3), reg 58 (2), reg 64C (7)
  - `Customer, Transaction`: reg 48 (2), reg 60A (2), reg 64B (2), reg 64C (6), reg 64D (2), reg 64G (7)
  - `Part of the United Kingdom`: reg 52B (2)
  - `Cryptoasset transfer, Kind of cryptoasset transfer`: reg 64B (6), reg 64C (5), reg 64D (5), reg 64E (4), reg 64F (3), reg 64G (8)
  - `Kind of risk`: reg 46 (3), reg 47 (3), reg 50 (4), reg 52 (3), reg 52A (5), reg 58 (4)
  - `Level of risk`: reg 47 (1)
  - `the commencement date`: reg 56 (1), reg 60 (1)
  - `the 800-pound figure`: reg 64C (1), reg 64G (1)

### mlr4

- **Line range (copied unchanged from `inputs/PARTS.md`):** 2200-3054 (15374 words).
- **Seams it asks:** S-16 (reg 65(3) from Schedule 5), S-17 (reg 75 from Schedule 6), S-19 (regs 93 and 99, the decisions appealed), and the keel's S-K1 to S-K3 (Schedule 3AZA, line 3042, speaks of a beneficial owner "within the meaning of regulation 3").
- **Seams it answers:** S-5 (Schedule 3, the relevant offences), S-6 (Schedule 3AZA), S-12 (reg 66).
- **Definitions left to it:** the reg 3(1) pointers into regs 75 and 76(8) (section 7).
  Schedule 1 is the core enumeration `Professional body` and Schedule 2 the core enumeration `Listed activity`; this part's rows for them are coverage rows pointing at the core, not new definitions.
- **Difficulties:** reg 93 contains the text of a substituted section 133A of FSMA (lines 2772-2777) whose numbered heading is not a regulation of these Regulations; Schedule 3's relevant offences are listed by Act and section, each borrowed (for example line 3010); reg 110 (line 2946) keeps the old regulations in effect for conduct before the commencement date.
- **Where it will read the core** (regulation: lines whose words are the core's; a pointer, not a promise):
  - `Kind of relevant person`: reg 74A (1), reg 74B (1), reg 74C (1), reg 103 (4), sch 1 (1), sch 3 (1)
  - `Professional body`: reg 65 (1), reg 87 (1), reg 102 (1), sch 1 (14), sch 3AZA (1)
  - `Authority`: reg 74C (17), reg 76 (10), reg 81 (9), reg 84 (14), reg 85 (13), reg 98 (11)
  - `Form of customer`: reg 70 (2), reg 78 (4), reg 81 (2), reg 91 (7), reg 92 (4), reg 103 (2)
  - `Customer, Transaction`: sch 2 (2), sch 3 (1), sch 3AZA (2)
  - `Part of the United Kingdom`: reg 70 (6), reg 87 (3), reg 88 (4), reg 89 (3), sch 1 (5), sch 3 (3)
  - `Kind of risk`: reg 67 (2), reg 74C (1), reg 82 (2), reg 93 (3), reg 110 (9), sch 3 (2)
  - `Listed activity`: sch 2 (1), sch 3 (1)
  - `the commencement date`: reg 110 (1)

### mlr5

- **Line range (copied unchanged from `inputs/PARTS.md`):** 3055-3808 (13906 words).
- **Seams it asks:** the keel's S-K2 and S-K3 where Schedules 3A and 4 speak of beneficial owners and supervisory authorities; no deep ones.
  Schedule 6 lists regulations by number (lines 3264 onward); it needs no input, only the numbers.
- **Seams it answers:** S-16 (Schedule 5), S-17 (Schedule 6), S-18 (Schedule 3A).
- **Definitions left to it:** none of reg 3(1)'s pointers point into its range; Schedule 6 is the list that reg 75 (`mlr4`) refers to.
- **Difficulties:** Schedule 3ZA (lines 3055-3081) is entirely lines of dots, a blank; Schedule 3A (line 3108) depends on "the date on which regulation 42(2)(iii) of these Regulations comes into force", which the rendering does not give; Schedule 3A's own figures (£100, £2,000, £10,000, £5,000) are this part's constants; Schedule 3A also cites Schedule 2 by point number (line 3165, fork F4); Schedule 6B (from line 3391) carries dates in October 2027 (lines 3393, 3494), so it may carry an in-force and a prospective version; Schedule 7 (lines 3544 to 3796) amends other legislation (inert, reason 2) except where the amended text is itself operative; the explanatory note (lines 3797-3808) is not operative (inert, reason 1).
- **Where it will read the core** (regulation: lines whose words are the core's; a pointer, not a promise):
  - `Kind of relevant person`: sch 4 (1), sch 6 (5), sch 6B (8), sch 7 (8)
  - `Professional body`: sch 3A (2), sch 7 (5)
  - `Authority`: sch 4 (11), sch 6 (4), sch 6A (20), sch 6B (8), sch 7 (12)
  - `Form of customer`: sch 3A (53), sch 4 (2), sch 5 (6), sch 6 (5), sch 7 (12)
  - `Customer, Transaction`: sch 3A (4), sch 6 (9), sch 7 (3)
  - `Part of the United Kingdom`: sch 3A (6), sch 6B (8), sch 7 (15)
  - `Cryptoasset transfer, Kind of cryptoasset transfer`: sch 6 (3)
  - `Kind of risk`: sch 3A (1), sch 4 (4), sch 6 (2), sch 6A (3), sch 6B (8), sch 7 (72)
  - `Level of risk`: sch 4 (2)
  - `Listed activity`: sch 3A (2), sch 7 (6)


## 7. Definitions left to the parts

The keel encoded every definition and rule of reading in lines 1-232.
A reg 3(1) term that only points at a provision elsewhere is encoded here as a pointer (a `STRING` naming the provision, word for word), and the **definition itself is the row of the part that owns the provision**; the keel's pointer and the part's definition are the two halves.
The pointer functions are in `mlr-definitions.l4`, each named `reg 3(1) <term> is given by`, and the test file asserts each string.
The owner of each, by the line of the provision pointed at:

| term | points at | heading line | owner |
|---|---|---|---|
| relevant person | reg 8 | 235 | mlr1 |
| credit institution | reg 10(1) | 270 | mlr1 |
| financial institution | reg 10(2) | 270 | mlr1 |
| auditor | reg 11(a) | 297 | mlr1 |
| insolvency practitioner | reg 11(b) | 297 | mlr1 |
| external accountant | reg 11(c) | 297 | mlr1 |
| tax adviser | reg 11(d) | 297 | mlr1 |
| independent legal professional | reg 12(1) | 305 | mlr1 |
| trust or company service provider | reg 12(2) | 305 | mlr1 |
| estate agent | reg 13(1) | 327 | mlr1 |
| letting agent | reg 13(3) | 327 | mlr1 |
| high value dealer | reg 14(1)(a) | 345 | mlr1 |
| casino | reg 14(1)(b) | 345 | mlr1 |
| auction platform | reg 14(1)(c) | 345 | mlr1 |
| art market participant | reg 14(1)(d) | 345 | mlr1 |
| cryptoasset exchange provider | reg 14A(1) | 359 | mlr1 |
| custodian wallet provider | reg 14A(2) | 359 | mlr1 |
| proliferation financing | reg 16A(9) | 434 | mlr1 |
| correspondent relationship | reg 34(4) | 1085 | mlr2 |
| politically exposed person | reg 35(12) | 1103 | mlr2 |
| law enforcement authority | reg 44(10) | 1385 | mlr2 |
| telecommunication, digital and IT payment service provider | reg 53 | 1790 | mlr3 |
| Annex 1 financial institution | reg 55(2) | 1823 | mlr3 |
| cryptoasset business | reg 64B | 2101 | mlr3 |
| transfer of funds supervisory authority | reg 62 | 2058 | mlr3 |
| designated supervisory authority | reg 76(8) | 2453 | mlr4 |
| relevant requirement | reg 75 | 2450 | mlr4 |

Beyond the pointers, the keel leaves to the parts the substantive provisions of the same regulations: for example reg 10 to reg 14A (who is a relevant person, `mlr1`), reg 35 (the politically exposed person rules, `mlr2`), reg 64B (the Part 7A terms, `mlr3`).

## 8. Difficulties the parts will meet

- **The rendering is not the official text.**
  Removed text shows as `...` (reg 3(1), six lines) or as lines of dots (Schedule 3ZA, lines 3055-3081, and the Part 5A entries after each of regs 45A to 45H): a blank, to be recorded as `repealed or blank in this text`.
  A part should say what it sees and not guess what the missing text said.
- **Schedule 2 has no point numbers** in the rendering although regs 10(3)(c) and 10(4)(a) cite them (fork F4).
- **"Working day"** is defined only for Part 7A (reg 64B, line 2119); elsewhere it is undefined (fork F3).
- **A listed company** is outside reg 5(1)'s definition; the text is silent on its beneficial owners (fork F1), yet regs 28(5), 30ZA(b), 37(3)(a)(iv) and 43(1) speak of one.
- **Reg 6(7) and reg 6(9) overlap** (fork F2).
- **Borrowed terms are everywhere**: FSMA, the Proceeds of Crime Act 2002, the Payment Services Regulations 2017, the Electronic Money Regulations 2011, the Companies Act 2006.
  Ask each as a fact; never guess its content.
- **`MAYBE BOOLEAN` seams make tests longer**: each seam needs a `JUST TRUE`, a `JUST FALSE` and a `NOTHING` case in the asking function's tests.
- **Prospective versions**: the text may carry an in-force and a prospective version of a provision (Schedule 6B, from line 3391, carries dates in October 2027 at lines 3393 and 3494); a part should say which it encoded.
- **The merge**: `mlr-definitions.l4` is imported with the parts at the merge, so a part's names must not repeat the keel's constructors; the prefix rule (section 1) keeps them apart.

