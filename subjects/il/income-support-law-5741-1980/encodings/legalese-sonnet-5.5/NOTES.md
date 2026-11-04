# NOTES -- Income Support Law 5741-1980 (Israel), whole, encoding `legalese-sonnet-5.5`

Method: a single Sonnet 5.5 agent working alone from the brief (BRIEF.md in this folder).
Target compiler: `main` (stable). Binary: l4 1.6.98 (main, 7689b0d, 2026-10-19), sha256 82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e; second stable build for the `check.sh` comparison: L4_MAIN (see "What check.sh prints").
Status: draft. No domain expert has read this against the text.

**The source is not the official text.** It is a consolidated working text from Hebrew Wikisource (page revision 3073779, last edited 2026-08-14T06:30:18Z), as raw MediaWiki source, deposited 2026-10-08. Israel publishes no free official consolidated text; the official version is the Reshumot publication plus each amending Act. `inputs/SOURCES.md` and the `.meta.json` record the hashes. Nothing here is "verified against the official text".
**The English is a gloss, not a translation of the Law.** Identifiers, `@desc` strings and this file are in English; the Hebrew term of art sits in a comment beside the first use; the `-- src:` lines quote the Hebrew exactly as the file prints it, including the wiki markup, so that `srcrefs.py` can check them.

## Seat

**The seat.** A person or family living in Israel whose means fall short of the minimum the Income Support Law sets, asking: am I entitled to an income-support allowance, how much and from when, what must I do to keep it, what can reduce or stop it, and what can I be made to repay.

**Why this seat.** The Law is written to the National Insurance Institute (the Institute): most sections say what the Institute pays, withholds, may demand or may do.
The person on the other side is the one with a question that needs an answer, and the Law gives that person a claim, duties and exposures that can each be asked as a plain question with plain facts.
The seat never speaks for an official: there is no question for the Institute's clerk (who decides, how a claim is examined, who appoints whom), and those sections are `inert` in the coverage table (reason 2, machinery).
**Five questions, under four sections, are asked from the position of someone other than the claimant or the claimant's family.** They are not officials, so the rule against an official's seat is not broken, but they are not the seat either: s 17(a) and s 17(c) are asked by a person who owes maintenance to someone the Institute paid (s 17(a), src:306, addresses a person liable by law or agreement for the maintenance of someone the Institute paid; s 17(c), src:308, names the court that hears the Institute's claim against that person), s 21(c) (src:340) by a person who holds information about a claimant's income or property, and s 22 (src:350) by a member of the management, a manager or an official of a body that committed an offence.
They are kept so that layer 2 touches those sections; a stricter seat would drop them, which would take the questions from 99 to 94 and the cases from 404 to 388 (the five questions carry 16 cases).

**Layer 2 in numbers.** `isl-seat.l4` has 99 questions under 14 `§§` groups, every one with `@export` and, on every input, `@desc`; `isl-cases-seat.l4` has 404 cases, every question has at least one, and each expected value was written by hand from the text before the run (the only generated parts of the cases file are the function names and the Hebrew Part C warning, copied from the layer-1 test, which quotes the source line).
Each question takes plain inputs and builds the records the rules need (`Household`, `Figures`) in its own `WHERE`; the seat restates no rule, and no layer-1 module was changed to suit it. Three layer-1 changes made in review fix defects the questions exposed (F19, the join of s 2(a)(2A) and s 2(d)(2); F17, the Third Schedule answering NOTHING where two rows fit; F4, `Household` carrying a widow and an independent parent as two fields), and with F4 the questions for s 5(a) and s 30A(b) ask "I am a widow" and "I am an independent parent" as two inputs.
Where a figure is held by the Institute or the Minister (the basic amount, the average wage, the vehicle limits, the determining amount) it is an input, asked with a description of where to find it.

| group | questions |
|---|---|
| Am I entitled to the allowance? (ss 2 to 4) | 15 |
| Am I barred or excluded? (ss 3, 3A, 3C, 4) | 7 |
| How much would I be paid? (ss 5 to 8) | 11 |
| How much of my income counts? (ss 9 to 12B) | 14 |
| From when am I paid? (s 14) | 3 |
| If I leave Israel (s 14A) | 6 |
| Other payments | 5 |
| If I was paid more in the past (s 30A, s 30) | 4 |
| What must I do to get and keep the allowance? (ss 13, 17(b), 19 to 21, Fifth Schedule) | 12 |
| Can an official come in, and who sees my information? (ss 21, 21A) | 4 |
| What can reduce, delay or stop my allowance, or cost me a fine? (ss 18, 19(b), 20B, 23(b)) | 9 |
| What can I be made to repay? (ss 17, 20A, 23(a)) | 3 |
| Which court hears my case? (ss 17(c), 26) | 3 |
| Who pays, and when the body is at fault (ss 14(c)(2), 22, 25) | 3 |

**Where the seat leans on a judgment the person cannot make unaided.** A few inputs are themselves legal conclusions, because the Law's own test is a conclusion and the person is the only one in the seat to ask it of: `one of the grounds in s 2(a) applies to me` (in the `s 2(a) and (b)` question; answer it with the earlier questions), `I would be entitled if I were 25` (item 3 and s 2(e); the pregnancy question still asks it, but it never changes that answer, because s 2(a)(2A) needs no such test for item 7), `a ground of entitlement in s 2 applies to me`, `s 3 bars me`, `s 3A bars me this month`, `s 3C bars me` (in the overall `ss 2 to 4` question; answer them with the questions above it), and `an exception in s 9A(c) holds` (answer it with the next question but one).
Each of these is a plain yes or no that the earlier question answers, and each is passed on as "yes means JUST TRUE, no means not covered" (`helper true or not covered`): a person who answers no is not told "you are not entitled", only that the Law does not answer.

**Polarity.** Every question's name says which way a `JUST TRUE` reads.
Where the Law's own function is a bar or a withholding ("the benefit is not paid for the month"), the question is phrased the same way ("Is my allowance withheld for ..."), so `JUST TRUE` is never read as "you will be paid".

**The question the seat cannot answer: what can I be made to repay.**
The Law has no section of its own on repaying an overpaid benefit.
Section 20A makes s 327 of the Insurance Law apply to one who claims or receives a benefit, and s 23(a) lists nineteen Insurance Law sections that apply (`s 327` is not among them).
Neither section's text is in the sources, so the seat's repayment group says only what the Law says: s 327 applies (`JUST TRUE`), and the Insurance Law sections on the s 23(a) list apply.
Whether, how much and by when an overpayment is recovered is `NOTHING`: that answer is asserted (`Does this section of the National Insurance Law apply :: "327"` is `NOTHING`).

## Jural relations

Hohfeld's correlatives: a claim-right of one party is a duty of the other; a privilege (liberty) is the other's no-right; a power is the other's liability; an immunity is the other's disability.
"Institute" is the National Insurance Institute (המוסד לביטוח לאומי); "claimant" is a person who has claimed, "recipient" one who is paid; "the Minister" is the Minister of Labour and Welfare (s 1), "the Ministers" the Minister with the Ministers of Justice and Finance (s 2(e)).
Each relation is stated once, as a relation between two parties, not again from the other side; the assignment of right/duty/power/liability is my reading of the text and is part of what a lawyer should check.
A provision that creates no relation is listed as `none`.

| provision | holder (claim-right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | L4 rule(s) |
|---|---|---|---|
| s 1 (definitions: "widow", "spouses", "retirement age", "benefit", "independent parent", "basic amount", "single person", "child", "new immigrant", "resident of Israel", the short names) | none | none | `s 1 ...` rules (13); `s 1 "basic amount" (1)` and `(2)` say how the Institute updates the figure |
| s 2(a)(1) to (9), (2A), (d), (e) and First Schedule items 1 to 26 | claimant: claim-right to the allowance when a ground holds | Institute: duty to pay | `s 2(a)(1) ...` to `s 2(a) and (b) ...`, `s 2(d)(1) ...`, `s 2(d)(2) ...`, `s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule`, `s 2(e) ...`, `s 2 the person is entitled by some route`, `sch 1 item N ...` |
| s 2(a)(5)(a), (b), (c) | spouses of a child under two: power to choose which parent holds the entitlement and to change the choice (not more than every six months where the other is entitled as unemployed) | Institute: liability to pay the parent chosen; the other spouse: liability to the change | `s 2(a)(5)(a) ...`, `s 2(a)(5)(b) ...`, `s 2(a)(5)(c) ...` |
| s 2(c), s 2(e) (the Ministers' rules and tests), s 4(b), s 5(e)(3) share | the Minister, the Ministers: power to set entitlement rules, tests, the share of 50% to 80% | claimants and the Institute: liability | `s 2(c) the person is entitled under the Minister's rules`; the share is an input (`s 5(e)(3) ...`) |
| s 3(1) to (3), s 3A, s 3C(a), (b) | Institute: privilege not to pay | claimant: no-right to the allowance | `s 3(1) ...`, `s 3(2) ...`, `s 3(3) ...`, `s 3A ...`, `s 3C(a) ...`, `s 3C(b) ...`, `s 3 the person is not entitled` |
| s 3(4) (students) and its exceptions; s 3C(b) end of sentence | claimant (retirement age, independent parent with 16 of 20 months, within 36 months): immunity from the student bar | Institute: disability to withhold | `s 3(4) the student is not entitled`, `s 3(4)(b)(2) ...` |
| s 3B | none (repealed in this text) | none | none |
| s 4 | Institute: privilege to withhold unless the spouse also meets s 2 | claimant: no-right | `s 4 the spouse also meets the conditions of s 2`, `s 2 to 4 the claimant is entitled to the benefit` |
| s 5(a) with Second Schedule | claimant: claim-right to the rate for their family and age | Institute: duty to pay that rate | `s 5(a) the benefit for an entitled person with no income`, `sch 2 ...`, `s 5(a)(1) to (2) the column ...` |
| s 5(b) | claimant: claim-right to the rate less income | Institute: duty | `s 5(b) the benefit for an entitled person who has income` |
| s 5(c) | none (repealed) | none | none |
| s 5(d) | parent whose spouse is excepted: privilege to be treated as an independent parent | Institute: no-right to apply the spouse rate | `s 5(d) the parent is treated as an independent parent` |
| s 5(e) | claimants under item 1, 5, 25, s 2(c), s 4(b), s 2(e): claim-right to the rate the Minister or the Ministers set | Institute: duty | `s 5(e)(1) ...`, `s 5(e)(2) ...`, `s 5(e)(3) ...` |
| s 5(f) | claimant: immunity from a reduction of the rate merely because maintenance was awarded | Institute: disability | `s 5(f) the rate is reduced merely because maintenance was awarded` |
| s 5(g) | woman of 62 to retirement age: claim-right to the supplement of 7.95% | Institute: duty | `s 5(g) ...` (3 rules) |
| s 6(a), (b), (c) | spouses: claim-right to one benefit, the higher of the two; power to choose which spouse is paid | Institute: duty; liability to pay the spouse chosen | `s 6(a) ...`, `s 6(b) ...`, `s 6(c) ...` |
| s 6(d), (e) | entitled spouse of one kept at public expense: claim-right to the couple's rate less 7.5% of the basic amount | Institute: duty | `s 6(d) ...`, `s 6(e)(1) ...`, `s 6(e)(2) ...` |
| s 7 | Minister: power to set the determining amount; Institute: privilege to pay only the headroom under it | claimant: liability; no-right to more | `s 7(b) ...`, `s 7(c) ...` |
| s 8 | Institute: privilege not to pay under six shekels (unless a pension is paid) | claimant: no-right | `s 8 the benefit is not paid` |
| s 9(a), (b1), (c); s 9A(a); s 10; s 11; s 12(c); Third Schedule; s 12, 12A, 12B deductions | none (what counts as income and property, what is left out, what is deducted) | none | `s 9(a) ...`, `s 9(b1)(1) ...` to `(2)(b) ...`, `s 9(c) ...`, `s 10 ...`, `s 11 ...`, `s 12(a)(1) ...` to `s 12B ...`, `sch 3 ...` |
| s 9A(b), (b1), (c) | Institute: privilege to withhold from one who owns vehicles beyond the limits, and to deduct for one vehicle; claimant: immunity under an exception in (c) | claimant: no-right; Institute: disability | `s 9A(b) ...`, `s 9A(b1) ...`, `s 9A(c)(2) ...` to `s 9A(c)(5)(b) ...`, `s 9A(c) one of the exceptions holds` |
| s 9(b), s 13(b), s 16, s 24(a), (b), s 27, s 31 | Minister: power to make regulations (and, in s 13(b), a duty to make them) | everyone affected: liability | none: inert, reason 2 |
| s 13(a) | claimant: power to submit a claim | Institute: liability to decide it (who decides is machinery) | `s 13(a) where a claim for a benefit is submitted` |
| s 14(a), (c)(1) | claimant: claim-right to payment from the first of the claim's month, and, at retirement age, for up to 12 earlier months | Institute: duty to pay | `s 14(a) ...`, `s 14(c)(1) ...` |
| s 14(c)(2) | Institute and public bodies: privilege not to extend the earlier-period privileges | claimant: no-right | `s 14(c)(2) "public body" ...`, `s 14(c)(2) the person paid under paragraph (1) ...` |
| s 14A(a), (b), (c), (c1) | Institute: privilege to withhold the allowance for months abroad | claimant: no-right | `s 14A(a) ...`, `s 14A(b) ...`, `s 14A(c) ...`, `s 14A(c1) ...` |
| s 14A(d) | claimant who was entitled and needs treatment abroad, or accompanies a sick relative: immunity from those bars | Institute: disability | `s 14A(d) ...`, `s 14A(d)(3) ...` |
| s 14A(e), (f) | spouse in Israel: claim-right to the individual rate; Institute: power to treat the person as outside Israel after 183 days | Institute: duty; person abroad: liability | `s 14A(e) ...`, `s 14A(f)(1) ...`, `s 14A(f)(2) ...` |
| s 14B | claimant (entitled for Oct, Nov or Dec and at retirement age): claim-right to the heating grant of 6.4% | Institute: duty | `s 14B the heating grant` |
| s 15 | surviving spouse, or one child: claim-right to the grant on death | Institute: duty; (b) no claim to both grants | `s 15(a) ...` (3 rules), `s 15(b) ...` |
| s 17(a), (c) | Institute: claim-right against the person liable for the recipient's maintenance, and power to sue in the District Court (a religious court may also hear) | the liable person: duty; liability to suit | `s 17(a) ...`, `s 17(c) ...` (2 rules) |
| s 17(b) | Institute: right that the recipient helps it, and does not harm its right | recipient: duty to help; duty not to harm | regulative `s 17(b) the recipient must help the Institute`, `s 17(b) the recipient shall not harm the Institute's right`; twin `s 17(b) the recipient is in breach of the duty` |
| s 18 | Institute: power to reduce, suspend or revoke | recipient: liability | `s 18 the Institute may reduce, suspend or revoke the benefit` |
| s 19(a) | Institute: right to information, an examination, an appearance | claimant or recipient: duty to comply | regulative `s 19(a) the claimant or recipient must comply with the Institute's demand`; twin `s 19(a) ... has met ...` |
| s 19(b) | Institute: power to delay the claim, stop payment or refuse | claimant: liability | `s 19(b) ...` |
| s 19(c) | none (repealed) | none | none |
| s 20 | Institute: right to be told in writing within 60 days of a change | recipient: duty (`WITHIN 60`) | regulative `s 20 the recipient must report a change`; twin `s 20 the recipient notified the change in time` |
| s 20A | Institute: the Insurance Law's s 327 powers (outside the sources) | claimant or recipient: liability | `s 20A the provisions of s 327 of the Insurance Law apply to the person` (applies; content `NOTHING`) |
| s 20B(a) | the State: power to prosecute and fine under s 61(a)(2) of the Penal Law (outside the sources) | claimant: liability to a fine for a false declaration or concealment | `s 20B(a) the claimant is liable to a fine` |
| s 20B(b)(1) to (5) | Institute: power to send a registered notice and rely on deemed service; State: power to fine | recipient: liability to a fine; (b)(5) recipient found disabled or in need of supervision: immunity | `s 20B(b)(1) ...` to `(5) ...` |
| s 21(a) | an employee the Institute's administration authorised: power to enter at a reasonable time; no power to force a residence without a magistrate's order | occupant: liability; occupant of a residence: immunity from forced entry | `s 21(a) the employee may enter the place`, `s 21(a) the employee may enter by force` |
| s 21(b) | Institute: right to a full and true answer | person questioned: duty | regulative `s 21(b) the person questioned must answer`; twin `s 21(b) the person met the duty to answer` |
| s 21(c) | Institute: right to the details within 30 days of the demand | person with the information: duty (`WITHIN 30`) | regulative `s 21(c) the person with the information must give it`; twin `s 21(c) the person gave the details in time` |
| s 21A | Institute: privilege to use information given under s 326(f) of the Insurance Law for ss 3C, 5(d), 6(e) | person: no-right | `s 21A(1) ...`, `s 21A(2) ...` |
| s 22 | the State: presumption that a manager is responsible for the body's offence | manager: liability; immunity on proving no knowledge, or every suitable measure | `s 22 the manager is treated as responsible for the body's offence` |
| s 23(a) | Institute: the Insurance Law's listed sections apply to this Law | those affected: liability (content outside the sources) | `s 23(a) the sections of the Insurance Law that apply`, `s 23(a) the section of the Insurance Law applies to this Law` |
| s 23(b) | recipient: immunity from transfer, pledge or attachment of the benefit (even for maintenance owed) | creditors and others: disability | `s 23(b) the benefit may be transferred, pledged or attached` |
| s 25(a), (b) | Institute: claim-right to the money for the payments and its administrative expenses, month by month | State Treasury: duty to pay the benefits and to transfer the money | `s 25(a) who pays the benefit`, `s 25(b) the State Treasury transfers the money for the month` |
| s 24(c) | none (applies sub-chapter C, ss 19 to 21A, with the necessary changes to participation in expenses under s 24) | none | `s 24(c) the provisions of sub-chapter C apply to the matter` |
| s 26 | none (a rule on which court has jurisdiction; parties to an action under this Law are subject to it) | none | `s 26 the Regional Labour Court has exclusive jurisdiction` |
| s 27, s 28, s 29, s 30(a), (c), s 31, s 32 | none (regulation powers, amendments of other Acts, savings, commencement) | none | none: inert, reason 2 |
| s 30(b) | claimant paid support just before becoming entitled: claim-right to not less than the last support | Institute: duty | `s 30(b) the benefit paid, not less than the last support` |
| s 30A with Fourth Schedule | former entitled person: claim-right at the Fourth Schedule rate (until six months out) | Institute: duty | `s 30A(a) ...`, `s 30A(b) ...`, `s 30A(c) ...`, `sch 4 ...` |
| First Schedule | see s 2(a), (d): grounds of entitlement for the young and special cases | Institute: duty | `sch 1 item 1(a) ...` to `sch 1 item 26 ...` |
| Second, Third, Fourth Schedules | none (rate tables) | none | `sch 2 ...`, `sch 3 ...`, `sch 4 ...` |
| Fifth Schedule, Part A and B | Institute: right to be told these ten details | recipient: duty to report | `sch 5 part A ...`, `sch 5 part B the detail is required` |
| Fifth Schedule, Part C | recipient: claim that the notice carries the warning | Institute: duty to carry it | `sch 5 part C the warning the notice must carry`, `s 20B(b)(2) ...` |

## What is encoded and what is not

**Encoded (layer 1), 225 functions and values (decision functions, three three-valued helpers, the list of items in s 2(a)(2A) and the string constants) and 6 regulative rules in nine modules, 1,130 hand-checked assertions in eight test files (plus 404 seat cases):**

| module | text | contents |
|---|---|---|
| `isl-nouns` | none (shared) | `Household`, `Figures`, the three enumerations, and three small three-valued helpers (`helper both`, `helper either`, `helper true or not covered`) |
| `isl-s01-definitions` | s 1 | the defined terms; the figure the text states for the basic amount (6,964) and how it is updated; the table of short names |
| `isl-p2-eligibility` | ss 2, 3, 3A, 3C, 4 | the grounds of entitlement, the bars, the spouse condition, and the combined `s 2 to 4` function |
| `isl-sch1-young` | First Schedule | items 1 to 26 (the young, pregnant women, those released, the ill, and the rest) |
| `isl-p3-rates` | ss 5 to 8, 30A, Second and Fourth Schedules | the column and row of the rate table, every cell, the supplement, the spouse rules, the determining amount, the six-shekel floor, the former entitled |
| `isl-p4-income` | ss 9 to 12B, Third Schedule | what counts as income and property, the vehicle limits and exceptions, the couple's income, the three deduction regimes, the Third Schedule |
| `isl-p5-claims-payment` | ss 13 to 15, 17 (a), (c), 18 | where to claim, the first day, the earlier months, leaving Israel, the heating grant, the grant on death, compensation claims, reduction of the benefit |
| `isl-p5-duties` | ss 17(b), 19 to 21A, 20B, Fifth Schedule | the regulative rules (s 17(b) two limbs, s 19(a), s 20 `WITHIN 60`, s 21(b), s 21(c) `WITHIN 30`) and their decision-function twins; entry, information, fines, deemed service; the ten details to report |
| `isl-p5-misc` | ss 22 to 26, 30(b) | managers' liability, the Insurance Law sections that apply, non-attachment, who pays, jurisdiction, the floor for the previously supported |

Every rule has an `@ref` and its Hebrew source lines in `-- src:` comments; `python3 -I srcrefs.py check --refs <the raw text> isl-*.l4` and the same with `--strict` each report 0 problems.
Every branch that answers a "no" carries `-- FALSE-kind (...)`, and every branch that answers "not covered" carries `-- NOTHING-kind (...)`: 80 and 218 branches respectively (`grep -c` over the nine modules).

**Regulative rules and their twins.** Each of the six regulative rules is run with `#TRACE` in `isl-tests-p5-duties.l4` (ten runs, the expected result written in a comment above each); a trace prints its result but cannot be asserted on the stable binary (see "What the stable binary does not accept"), so the same duty is also a decision function over the facts, and those are asserted.
The ten trace outputs read the same on the stable build (1.6.98) and on the main build (1.6.108) compared with it (checked by diffing the two outputs of `isl-tests-p5-duties.l4`: the only difference is the diagnostic's `Code:` label on the assertion lines).

**Inputs, not encoded numbers.** The basic amount now in force, the average wage, the basic amount for a child, the value of a pension point (`Figures`), the updated vehicle thresholds (60,000 and 10,309 are the figures the text states; the updated figures are inputs), the s 7 determining amount, the Minister's deduction for one vehicle, the Ministers' share under s 5(e)(3), the regulations' conditions under s 2(a)(3), (7), 14A(d), and every date the person states.
The `{{ח:הערה}}` notes (for example "2026: 10,382") are the Wikisource editor's, not the Law's, and are not used.

**Not encoded (the coverage table gives each row its disposition and reason).**
- Reason 2, machinery: the Minister's powers to make regulations (`s 9(b)`, `s 13(b)`, `s 16`, `s 24(a)`, `s 24(b)`, `s 27`, `s 31`, `s 30(c)`), amendments of other Acts shown incorporated (`s 28`, `s 29`), a saving (`s 30(a)`), commencement (`s 32`). Twenty rows.
- Reason 1, not operative: the title and amendment history, the table of contents, chapter and section headings, the lead-in words ("in this Law ..."), and the signatures. Sixty-nine rows.
- Reason 3, repealed or blank in this text: s 1 definitions 1, 19, 20, 23, 24, 25; s 2(a)(6); s 3B; s 5(c); s 9A(c)(1), (6), (7); s 14(b); s 19(c). Fourteen rows.
- Moved out of inert: none. This is a fresh encoding and the coverage table was built once, so no row changed disposition and there is no baseline to compare against. Four rows that look inert at first reading were encoded from the start, because the text still reaches a person: `s 7(a)` is mapped to the `s 7(b)` function that carries it, `s 13(a)` and `s 25(a)` are encoded as the strings they name, and `s 30(b)` (the floor for those supported before the Law) is encoded though it may now reach few.
- The Insurance Law, the Penal Law, the Supervision Law, the Arrests Law, the Minimum Wage Law, the Single-Parent Families Assistance Law, the Disengagement Plan Implementation Law and the Law of Return are not in the sources: every rule that points at one asks the borrowed fact as an input (for example `an independent parent as s 1 of the Single-Parent Families Assistance Law means it`) and returns `NOTHING` where the answer lies in the borrowed text.

**What the text does not answer** (each is `NOTHING` or an input in the encoding):
1. How much an overpaid benefit is repaid, by when, and how it is recovered: the Law has no repayment section; s 20A and s 23(a) borrow the Insurance Law.
2. What follows a breach of s 17(b), s 21(b) or s 21(c): the Law attaches no consequence to them in the sections encoded (a search of the text for references to those sections finds none that does; s 19(b) attaches one to s 19(a), and s 20B(b)(1) attaches a fine to s 20 after a registered notice). The regulative rules end at `BREACH` with a stated reason and nothing more.
3. The determining amount of s 7, the Ministers' share of s 5(e)(3), the vehicle deduction, and every rule the Minister sets by regulation.
4. What the Institute does when income exceeds the allowance (s 5(b) is silent: not "zero", `NOTHING`).
5. A pregnant woman who lives with parents who do not receive the benefit (First Schedule items 5 and 6 leave her out).
6. A man in a shelter for battered women (s 2(a)(9) says "she").
7. Who certifies that the conditions of s 2 are met: s 13(b) leaves it to the Minister's regulations.

## Coverage table

<!-- COVERAGE:BEGIN -->
Units (rows): 456. Non-blank lines of the text: 509, every one in exactly one row (0 uncovered, 0 in two rows). Dispositions: encoded 307, fork 46, inert (1: not operative) 69, inert (2: machinery) 20, repealed or blank in this text 14.

| row | lines | text (Hebrew, markup stripped) | disposition | encoded as / reason |
|---|---|---|---|---|
| front.title | 1-4 |  | inert (1: not operative) | title, amendment history and table of contents: not operative |
| front.history | 5-7 | , ; ; ; , , ; ; , ; ; , ; ; , , ; ; , , ; ; , , ; ... | inert (1: not operative) | title, amendment history and table of contents: not operative |
| front.toc | 9-29 |  | inert (1: not operative) | title, amendment history and table of contents: not operative |
| ch1.head | 31-31 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s1.head | 33-33 |  | inert (1: not operative) | a heading or section title: not operative |
| s1 | 34-34 | בחוק זה – | inert (1: not operative) | lead-in words ('in this Law'): they create no rule of their own |
| s1.def1 | 35-35 | ”אישור השתתפות“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def2 | 36-36 | ”אלמנה“ – לרבות מי שמשתלמת לה קיצבת שאירים או תלוי... | encoded | s 1 "widow" the person is a widow |
| s1.def3 | 37-37 | ”בני זוג“ – לרבות איש ואשה הידועים בציבור כבני זוג... | encoded | s 1 "spouses" the two are spouses |
| s1.def4 | 38-38 | ”גיל פרישה“ – כהגדרתו בחוק הביטוח; | encoded | s 1 "retirement age" the person has reached it |
| s1.def5 | 39-39 | ”גימלה“ – גימלה חדשית להבטחת הכנסה המשולמת לפי חוק... | encoded | s 1 "benefit" the payment is a benefit |
| s1.def6 | 40-40 | ”הורה עצמאי“ – כמשמעותו בסעיף 1 לחוק סיוע למשפחות ... | encoded | s 1 "independent parent" the person is an independent parent |
| s1.def7 | 41-41 | ”הסכום הבסיסי“ – 6,964 שקלים חדשים , כשהוא מעודכן ... | encoded | s 1 "basic amount" the figure the text states |
| s1.def7(1) | 42-42 | ביום א׳ בטבת התשס״ו (1 בינואר 2006) – לפי שיעור על... | fork | s 1 "basic amount" (1) the amount updated on 1 January 2006 -- F1 basic-amount-rates-added |
| s1.def7(1)(a) | 43-43 | לענין גמלה המשתלמת למקבלי גמלה לפי הוראות סימן ח׳ ... | fork | s 1 "basic amount" (1) the amount updated on 1 January 2006 -- F1 basic-amount-rates-added |
| s1.def7(1)(b) | 44-44 | לעניין גמלה המשתלמת לפי חוק זה למי שאינו מנוי בפסק... | fork | s 1 "basic amount" (1) the amount updated on 1 January 2006 -- F1 basic-amount-rates-added |
| s1.def7(2) | 45-45 | משנת 2007 ואילך – ב־1 בינואר של כל שנה לפי שיעור ע... | encoded | s 1 "basic amount" (2) the amount updated on a 1 January from 2007 |
| s1.def8 | 46-46 | ”הפקודה“ – פקודת מס הכנסה; | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def9 | 47-47 | ”השכר הממוצע“ – כמשמעותו בסעיפים 1 ו־2 לחוק הביטוח... | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def10 | 48-48 | ”השר“ – שר העבודה והרווחה; | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def11 | 49-49 | ”חוק הביטוח“ – חוק הביטוח הלאומי [נוסח משולב], התש... | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def12 | 50-50 | ”חוק יישום תכנית ההתנתקות“ – חוק יישום תכנית ההתנת... | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def13 | 51-51 | ”חוק המעצרים“ – חוק סדר הדין הפלילי (סמכויות אכיפה... | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def14 | 52-52 | ”חוק הפיקוח“ – חוק הפיקוח על מוסדות לטיפול במשתמשי... | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def15 | 53-53 | ”חוק העונשין“ – חוק העונשין, התשל״ז–1977; | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def16 | 54-54 | ”חוק שכר מינימום“ – חוק שכר מינימום, התשמ״ז–1987; | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def17 | 55-55 | ”יחיד“ – מי שאין לו בן זוג; | encoded | s 1 "single person" the claimant is a single person |
| s1.def18 | 56-56 | ”ילד“ – כל אחד מאלה: | encoded | s 1 "child" the person is a child |
| s1.def18(a) | 57-57 | ילד כמשמעותו בהגדרה ”ילד“ בסעיף 238 לחוק הביטוח; | encoded | s 1 "child" the person is a child |
| s1.def18(b) | 58-58 | מי שאינו ילדו של התובע ובלבד שהתקיימו בו כל אלה: | encoded | s 1 "child" the person is a child |
| s1.def18(b)(1) | 59-59 | הוא אחד המנויים בפסקאות (1) עד (5) להגדרה ”ילד“ בס... | encoded | s 1 "child" the person is a child |
| s1.def18(b)(2) | 60-60 | הוא מתגורר דרך קבע עם תובע הגימלה; | encoded | s 1 "child" the person is a child |
| s1.def18(b)(3) | 61-61 | תובע הגימלה מונה כאפוטרופוס עליו, לרבות תובע גימלה... | encoded | s 1 "child" the person is a child |
| s1.def19 | 62-62 | ”מסגרת שיקומית“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def20 | 63-63 | ”מתכנן יעדים תעסוקתי“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def21 | 64-64 | ”נקודת קיצבה“ – כמשמעותה בסעיף 68(א) לחוק הביטוח; | encoded | s 1 what a defined short name stands for -- a pointer definition: the table of short names |
| s1.def22 | 65-65 | ”עולה חדש“ – מי שטרם מלאו 5 שנים מיום שהתקיים בו א... | fork | s 1 "new immigrant" the person is a new immigrant -- F2 new-immigrant-any-of-four-days |
| s1.def22(1) | 66-66 | נכנס לראשונה לישראל באשרת עולה לפי חוק השבות, התש״... | fork | s 1 "new immigrant" the person is a new immigrant -- F2 new-immigrant-any-of-four-days |
| s1.def22(2) | 67-67 | ניתנה לו תעודת עולה לפי חוק השבות; | fork | s 1 "new immigrant" the person is a new immigrant -- F2 new-immigrant-any-of-four-days |
| s1.def22(3) | 68-68 | ניתנה לו תעודה של אזרח עולה מהמשרד לקליטת העליה; | fork | s 1 "new immigrant" the person is a new immigrant -- F2 new-immigrant-any-of-four-days |
| s1.def22(4) | 69-69 | הוא זכאי לסל קליטה מהמשרד לקליטת העליה ונכנס לישרא... | fork | s 1 "new immigrant" the person is a new immigrant -- F2 new-immigrant-any-of-four-days |
| s1.def23 | 70-70 | ”פרק שילוב מקבלי גמלאות בעבודה“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def24 | 71-71 | ”תושב אזור שילוב“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def25 | 72-72 | ”תושב אזור שילוב פטור“ – | repealed or blank in this text | the text shows it repealed or blank |
| s1.def26 | 73-73 | ”תושב ישראל“ – לרבות תושב ישראל באזור כהגדרתו בסעי... | encoded | s 1 "resident of Israel" the person is a resident of Israel |
| ch2.head | 75-75 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s2.head | 77-77 |  | inert (1: not operative) | a heading or section title: not operative |
| s2(a) | 78-78 | תושב ישראל שמלאו לו 25 שנים זכאי לגימלה, בכפוף להו... | encoded | s 2(a) the resident aged 25 or over is entitled under subsection (a);  s 2 the person is entitled by some route |
| s2(a)(1) | 79-79 | אין לו הכושר לעבוד ולהתפרנס כדי מחייתו, או שאינו נ... | encoded | s 2(a)(1) the person has no capacity to work or cannot be placed in any work |
| s2(a)(1)(a) | 80-80 | לגבי מי שמטופל במוסד או נמצא בתהליך גמילה מסם לפי ... | fork | s 2(a)(1) the finding of non-placement was made by the body the text names for the situation -- F3 institution-of-treatment |
| s2(a)(1).def1 | 81-81 | ”מוסד“, ”סם“ – כהגדרתם בסעיף 1 בחוק הפיקוח; | encoded | s 2(a)(1) the finding of non-placement was made by the body the text names for the situation -- the defined terms select the situation the finding is about |
| s2(a)(1).def2 | 82-82 | ”צו מבחן“ – כמשמעותו בסימן ז׳ של פרק ו׳ בחוק העונש... | encoded | s 2(a)(1) the finding of non-placement was made by the body the text names for the situation -- the defined terms select the situation the finding is about |
| s2(a)(1)(b) | 83-83 | לגבי מי שמצוי בפיקוחו של קצין מבחן לפי חוק המעצרים... | encoded | s 2(a)(1) the finding of non-placement was made by the body the text names for the situation |
| s2(a)(1)(c) | 84-84 | לגבי מי ששוהה במרכז לטיפול באלכוהוליסטים המצוי בפי... | encoded | s 2(a)(1) the finding of non-placement was made by the body the text names for the situation |
| s2(a)(2) | 85-85 | הוא רשום בלשכת שירות התעסוקה כמחוסר עבודה בהתאם לכ... | encoded | s 2(a)(2) the work or training is suitable work;  s 2(a)(2) the person is registered as unemployed and was offered no suitable work |
| s2(a)(2A) | 86-86 | מתקיים בו האמור בפסקאות (7) עד (10), (14), (16), (... | fork | s 2(a)(2A) the person meets one of the listed items of the First Schedule;  s 2(a)(2A) the listed items of the First Schedule;  s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule -- F19 2a2a-and-d2-either-route |
| s2(a)(3) | 87-87 | הוא עובד בעבודה או נמצא בהכשרה, לרבות במסגרת שיקומ... | encoded | s 2(a)(3) the person works or is in training with a low income |
| s2(a)(4) | 88-88 | הוא הגיע לגיל הפרישה; | encoded | s 2(a)(4) the person has reached retirement age |
| s2(a)(5)(a) | 89-89 | הוא הורה לילד שבהחזקתו ונמצא עמו וטרם מלאו לו שנתי... | encoded | s 2(a)(5)(a) the parent of a child under two is entitled |
| s2(a)(5)(b) | 90-90 | בחרו בני הזוג כאמור בפסקת משנה (א), הם רשאים לחזור... | encoded | s 2(a)(5)(b) the spouses may change their choice |
| s2(a)(5)(c) | 91-91 | תוקפה של זכאות לאחר מסירת הודעה על בחירה כאמור בפס... | encoded | s 2(a)(5)(c) the day the choice takes effect |
| s2(a)(6) | 92-92 |  | repealed or blank in this text | the text shows it repealed or blank |
| s2(a)(7) | 93-93 | עיקר זמנו מוקדש לטיפול בבן זוגו החולה או בילדו החו... | encoded | s 2(a)(7) the person's main time goes to caring for a sick spouse or child |
| s2(a)(8) | 94-94 | הוא עובד שירות בעבודה ציבורית לפי סימן ב׳1 לפרק ו׳... | encoded | s 2(a)(8) the person performs community service |
| s2(a)(9) | 95-95 | היא שוהה במקלט לנשים מוכות באישור המחלקה לשירותים ... | encoded | s 2(a)(9) the woman stays in a shelter for battered women |
| s2(b) | 96-96 | תנאי נוסף לזכאות לגימלה הוא שהתובע היה תושב ישראל ... | encoded | s 2(b) the additional condition of 24 months of residence is met;  s 2(a) and (b) the resident aged 25 or over is entitled |
| s2(c) | 97-97 | השר רשאי לקבוע בתקנות כללים ומבחנים לזכאות לגימלה ... | encoded | s 2(c) the person is entitled under the Minister's rules |
| s2(d)(1) | 98-98 | ילד תושב ישראל שמתקיים בו האמור בפסקה (1) של התוספ... | encoded | s 2(d)(1) the child who is a resident is entitled under item 1 of the First Schedule |
| s2(d)(2) | 99-99 | תושב ישראל שמתקיים בו האמור בפסקאות (2) ואילך של ה... | fork | s 2(d)(2) the resident is entitled under an item of the First Schedule from item 2 onward;  s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule -- F19 2a2a-and-d2-either-route |
| s2(e) | 100-100 | השר, שר המשפטים ושר האוצר כאחד (בסעיף קטן זה – השר... | encoded | s 2(e) the resident aged 20 to under 25 meets the two conditions |
| s2(e)(1) | 101-101 | אילו מלאו לו 25 שנים היה זכאי לגמלה; | encoded | s 2(e) the resident aged 20 to under 25 meets the two conditions |
| s2(e)(2) | 102-102 | הוא הוכיח באופן ובתנאים שקבעו השרים, להנחת דעתו של... | encoded | s 2(e) the resident aged 20 to under 25 meets the two conditions |
| s3.head | 104-104 |  | inert (1: not operative) | a heading or section title: not operative |
| s3 | 105-105 | לא יהיו זכאים לגימלה לפי חוק זה – | encoded | s 3 the person is not entitled -- the chapeau: the four classes |
| s3(1) | 106-106 | אדם הנמצא במוסד וכל החזקתו היא על חשבון אוצר המדינ... | encoded | s 3(1) the person kept in an institution at public expense is not entitled |
| s3(2) | 107-107 | אדם המשרת שירות סדיר בצבא־הגנה לישראל ואשתו; | encoded | s 3(2) the soldier in regular service and his wife are not entitled |
| s3(3) | 108-108 | חבר בתאגיד האחראי לכלכלת חבריו; | encoded | s 3(3) the member of a body corporate responsible for its members' livelihood is not entitled |
| s3(4) | 109-109 | תלמיד הלומד במוסד שקבע השר בתקנות ובתנאים שקבע, למ... | encoded | s 3(4) the student is not entitled |
| s3(4)(a) | 110-110 | מי שמשתלמת לו גמלה לפי פסקה (4) של סעיף 2(א); | encoded | s 3(4) the student is not entitled |
| s3(4)(b)(1) | 111-111 | הורה עצמאי, שהשתלמה לו גמלה בעד 16 חודשים לפחות מת... | encoded | s 3(4) the student is not entitled |
| s3(4)(b)(2) | 112-112 | אין בהוראות פסקת משנה (1) כדי לגרוע מהאמור בסעיף 2... | encoded | s 3(4)(b)(2) subparagraph (1) does not take away an entitlement under s 2(a)(2) or (3) |
| s3A.head | 114-114 |  | inert (1: not operative) | a heading or section title: not operative |
| s3A | 115-115 | מי שזכאותו לגמלה מותנית בקיום האמור בסעיף 2(א)(2),... | encoded | s 3A the person who refused suitable work is not entitled for the month |
| s3B.head | 117-117 |  | inert (1: not operative) | a heading or section title: not operative |
| s3B | 118-118 |  | repealed or blank in this text | the text shows it repealed or blank |
| s3C.head | 120-120 |  | inert (1: not operative) | a heading or section title: not operative |
| s3C(a) | 121-121 | מי שנדון למאסר בשל עבירת רצח או ניסיון לרצח בנסיבו... | encoded | s 3C(a) the person is not entitled;  s 3C(a) the person is not counted as a spouse for the benefit;  s 3C(a) the spouse is not treated as an independent parent |
| s3C(b) | 122-122 | על מי ששוחרר ממאסר במסגרת שחרור שבויים ישראליים או... | encoded | s 3C(b) subsection (a) applies to the person released in an exchange |
| s3C(c) | 123-123 | בסעיף זה, ”עבירת ביטחון“ ו”עבירת רצח או ניסיון לרצ... | encoded | s 3C(c) what the two terms mean |
| s4.head | 125-125 |  | inert (1: not operative) | a heading or section title: not operative |
| s4(a) | 126-126 | הזכאות לגימלה של כל אחד מבני זוג מותנית בכך שמתקיי... | encoded | s 4 the spouse also meets the conditions of s 2;  s 2 to 4 the claimant is entitled to the benefit |
| s4(b) | 127-127 | האמור בסעיף קטן (א) לא יחול על מי שהשר קבע בתקנות,... | encoded | s 4 the spouse also meets the conditions of s 2 |
| ch3.head | 129-129 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s5.head | 131-131 |  | inert (1: not operative) | a heading or section title: not operative |
| s5(a) | 132-132 | הגימלה לזכאי שאין לו הכנסה תהיה בסכומים המחושבים ל... | encoded | s 5(a) the benefit for an entitled person with no income |
| s5(a)(1) | 133-133 | למי שהגיע לגיל פרישה, למי שמשתלמת לו קצבת אזרח ותי... | encoded | s 5(a)(1) to (2) the column of the Second Schedule that applies |
| s5(a)(2) | 134-134 | למי שלא משתלמת לו קצבה כאמור בפסקה (1) – | encoded | s 5(a)(1) to (2) the column of the Second Schedule that applies |
| s5(a)(2)(a) | 135-135 | אם טרם מלאו לו 55 שנים – בשיעורים הנקובים בטור ב׳ ... | encoded | s 5(a)(1) to (2) the column of the Second Schedule that applies |
| s5(a)(2)(b) | 136-136 | אם מלאו לו 55 שנים – בשיעורים הנקובים בטור ג׳ בתוס... | encoded | s 5(a)(1) to (2) the column of the Second Schedule that applies |
| s5(a)(3) | 137-137 | להורה עצמאי – לפי , לפי הענין. | fork | sch 2 which row of the table applies to the household -- F4 second-schedule-widow-overlap-is-nothing |
| s5(b) | 138-138 | הגימלה לזכאי שיש לו הכנסה תהיה בסכום השווה להפרש ש... | encoded | s 5(b) the benefit for an entitled person who has income |
| s5(c) | 139-139 |  | repealed or blank in this text | the text shows it repealed or blank |
| s5(d) | 140-140 | לענין סעיף זה יראו כהורה עצמאי גם הורה, שיש עמו יל... | encoded | s 5(d) the parent is treated as an independent parent |
| s5(e) | 141-141 | על אף הוראות סעיף קטן (א) – | encoded | s 5(e)(1) the rate for one entitled under item 1, 5 or 25 of the First Schedule;  s 5(e)(2) the rate for one entitled under s 2(c) or s 4(b);  s 5(e)(3) the benefit for one entitled under s 2(e) |
| s5(e)(1) | 142-142 | שיעור הגמלה שתשולם למי שזכאי לגמלה כאמור בפסקאות (... | encoded | s 5(e)(1) the rate for one entitled under item 1, 5 or 25 of the First Schedule |
| s5(e)(2) | 143-143 | השר רשאי לקבוע את שיעור הגמלה שתשולם למי שזכאי לגמ... | encoded | s 5(e)(2) the rate for one entitled under s 2(c) or s 4(b) |
| s5(e)(3) | 144-144 | השר, שר המשפטים ושר האוצר כאחד יקבעו את שיעור הגמל... | encoded | s 5(e)(3) the benefit for one entitled under s 2(e) |
| s5(f) | 145-145 | מי שנפסקו לזכותו מזונות והוא אינו זכאי לתשלום חודש... | encoded | s 5(f) the rate is reduced merely because maintenance was awarded |
| s5(g) | 146-146 | אישה הזכאית לגמלה לפי סעיף קטן (א)(2)(ב), ומלאו לה... | fork | s 5(g) the woman is entitled to the supplement for the month;  s 5(g) the amount of the supplement -- F5 supplement-period-from-62 |
| s5(g)(1) | 147-147 | ינואר 1960 עד דצמבר 1960 – 4 חודשים; | fork | s 5(g) the number of months of the supplement -- F5 supplement-period-from-62 |
| s5(g)(2) | 148-148 | ינואר 1961 עד דצמבר 1961 – 8 חודשים; | fork | s 5(g) the number of months of the supplement -- F5 supplement-period-from-62 |
| s5(g)(3) | 149-149 | ינואר 1962 עד דצמבר 1962 – 12 חודשים; | fork | s 5(g) the number of months of the supplement -- F5 supplement-period-from-62 |
| s5(g)(4) | 150-150 | ינואר 1963 עד דצמבר 1963 – 15 חודשים; | fork | s 5(g) the number of months of the supplement -- F5 supplement-period-from-62 |
| s5(g)(5) | 151-151 | ינואר 1964 עד דצמבר 1964 – 18 חודשים. | fork | s 5(g) the number of months of the supplement -- F5 supplement-period-from-62 |
| s6.head | 153-153 |  | inert (1: not operative) | a heading or section title: not operative |
| s6(a) | 154-154 | לבני זוג הזכאים לגימלה תשולם גימלה אחת בלבד, בשיעו... | encoded | s 6(a) the single benefit paid to two spouses |
| s6(b) | 155-155 | היה שיעור הגמלה המחושב לבני הזוג לפי נתוניו האישיי... | encoded | s 6(b) the benefit paid to the couple is the higher |
| s6(c) | 156-156 | הגימלה לפי סעיף זה תשולם לאחד מבני הזוג לפי בחירתם... | encoded | s 6(c) the benefit is paid to one of the spouses as they choose |
| s6(d) | 157-157 | אדם שאינו זכאי לגימלה לפי חוק זה רק בשל האמור בסעי... | encoded | s 6(d) the benefit paid to the entitled spouse of one excluded by s 3(1) |
| s6(e)(1) | 158-158 | על אף האמור בהוראות לפי סעיף קטן (ג), מי שהורשע בע... | encoded | s 6(e)(1) the benefit is not paid to the person under this section |
| s6(e)(2) | 159-159 | הוראות סעיף קטן (ד) יחולו גם לגבי מי שאינו זכאי לג... | encoded | s 6(e)(2) subsection (d) applies to the entitled spouse |
| s7.head | 161-161 |  | inert (1: not operative) | a heading or section title: not operative |
| s7(a) | 162-162 | השר רשאי לקבוע בתקנות, לגבי סוגי זכאים, לרבות סוגי... | encoded | s 7(b) the benefit payable where a determining amount applies -- the Minister's determining amounts are an input of s 7(b) |
| s7(b) | 163-163 | זכאי שהכנסתו, המחושבת לפי סעיפים 9 עד 11, אינה נמו... | encoded | s 7(b) the benefit payable where a determining amount applies |
| s7(c) | 164-164 | סעיף זה לא יחול על זכאי שמשתלמת לו גמלה לפי פסקה (... | encoded | s 7(c) section 7 does not apply to the person |
| s8.head | 166-166 |  | inert (1: not operative) | a heading or section title: not operative |
| s8 | 167-167 | גימלה שהיא פחותה מששה שקלים חדשים לא תשולם אלא אם ... | encoded | s 8 the benefit is not paid |
| ch4.head | 169-169 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s9.head | 171-171 |  | inert (1: not operative) | a heading or section title: not operative |
| s9(a) | 172-172 | בחוק זה, | encoded | s 9(a) "income" the receipt is income |
| s9.def1 | 173-173 | ”הכנסה“ – הכנסה מהמקורות המפורטים בסעיף 2 לפקודה, ... | encoded | s 9(a) "income" the receipt is income |
| s9.def1(1) | 174-174 | כל גימלה כמשמעותה בחוק הביטוח; | encoded | s 9(a) "income" the receipt is income |
| s9.def1(2) | 175-175 | תשלומים למי שמצוי בהכשרה מקצועית; | encoded | s 9(a) "income" the receipt is income |
| s9.def1(3) | 176-176 | דמי מזונות שמקבל אדם לפי כל דין בעדו ובעד ילדיו, ל... | encoded | s 9(a) "income" the receipt is income |
| s9.def1(4) | 177-177 | סכומים שיראו אותם כהכנסה מנכס, אף אם הנכס הוא של י... | encoded | s 9(a) "income" the receipt is income |
| s9.def1(5) | 178-178 |  | encoded | s 9(a) "income" the receipt is income |
| s9(b) | 179-179 | השר רשאי לקבוע בתקנות – | inert (2: machinery) | the Minister's power to make regulations on income from property and the calculation of income |
| s9(b)(1) | 180-180 | כללים בדבר חישוב הסכומים שיראו אותם כהכנסה מנכס, כ... | inert (2: machinery) | the Minister's power to make regulations |
| s9(b)(2) | 181-181 | נסיבות שבהן ייראה נכס שהועבר לאחר כשייך למעביר הנכ... | inert (2: machinery) | the Minister's power to make regulations |
| s9(b)(3) | 182-182 | הוראות מיוחדות ומשלימות בדבר חישוב ההכנסה לענין חו... | inert (2: machinery) | the Minister's power to make regulations |
| s9(b1) | 183-183 | לגבי סכום המשתלם לפי סעיף 3(א1)(1) לתוספת השלישית ... | encoded | s 9(b1)(1) the one-off payment is treated as property;  s 9(b1)(2)(a) the instalment payment is counted as income;  s 9(b1)(2)(b) the property the claimant is treated as having;  s 9(b1)(2)(b) the income counted from the deemed property |
| s9(b1)(1) | 184-184 | אם הוא משתלם לתובע כתשלום חד־פעמי, יראו בתשלום החד... | encoded | s 9(b1)(1) the one-off payment is treated as property |
| s9(b1)(2) | 185-185 | אם הוא משתלם לתובע לשיעורין – | encoded | s 9(b1)(2)(a) the instalment payment is counted as income;  s 9(b1)(2)(b) the property the claimant is treated as having |
| s9(b1)(2)(a) | 186-186 | לא יראו בתשלום המשתלם לתובע לשיעורין כהכנסה; | encoded | s 9(b1)(2)(a) the instalment payment is counted as income |
| s9(b1)(2)(b) | 187-187 | יראו כאילו לתובע יש נכס בסכום השווה לתשלום החד־פעמ... | fork | s 9(b1)(2)(b) the property the claimant is treated as having;  s 9(b1)(2)(b) the income counted from the deemed property -- F6 instalment-per-period |
| s9(c) | 188-188 | לענין סעיף זה, | inert (1: not operative) | lead-in words ('for this section'): they create no rule of their own; the definitions that follow are encoded |
| s9.def2 | 189-189 | ”נכס“ – כל רכוש, בין מקרקעין ובין מיטלטלין, וכן כל... | encoded | s 9(c) "property" the thing is property |
| s9.def3 | 190-190 | ”סכום שאינו מובא בחשבון“ – סכום כמפורט להלן: | encoded | s 9(c) "amount not counted" (1) the sum of money is not counted;  s 9(c) "amount not counted" (2) the sale proceeds are not counted on the day |
| s9.def3(1) | 191-191 | סכום כסף שאינו עולה על סכום השווה לסכום הבסיסי כפו... | fork | s 9(c) "amount not counted" (1) the sum of money is not counted -- F7 money-is-the-total |
| s9.def3(2) | 192-192 | סכום שהתקבל בעד מכירת דירת מגורים, לרבות פיצויים ל... | fork | s 9(c) "amount not counted" (2) the sale proceeds are not counted on the day -- F8 period-ends-on-anniversary |
| s9A.head | 194-194 |  | inert (1: not operative) | a heading or section title: not operative |
| s9A(a) | 195-195 | בסעיף זה – | inert (1: not operative) | lead-in words ('in this section'): they create no rule of their own; the definitions that follow are encoded |
| s9A.def1 | 196-196 | ”בעל רכב“ – לרבות מי שנוהג ברכב מנהג בעלים, אף אם ... | encoded | s 9A(a) "owner of a vehicle" the person is one |
| s9A.def2 | 197-197 | ”רכב“ – רכב מנועי כהגדרתו בפקודת התעבורה; | encoded | s 9A(a) "vehicle" the thing is a vehicle |
| s9A.def3 | 198-198 | ”תובע“ – לרבות ילדו הנמצא עמו. | encoded | s 9A(a) "claimant" the person is one for this section |
| s9A(b) | 199-199 | תובע שהוא בעל שני כלי רכב או יותר או שהוא בעל רכב ... | encoded | s 9A(b) the claimant is not entitled because of their vehicles;  s 9A(b) the figure the text states for a claimant to whom s 5(a)(1) applies |
| s9A(b1) | 200-200 | השר רשאי לקבוע כי מגמלתו של תובע שבבעלותו רכב אחד ... | encoded | s 9A(b1) the deduction from the benefit for the vehicle;  s 9A(b1) the figure the text states for a non-working claimant to whom s 5(a)(1) applies |
| s9A(c) | 201-201 | הוראות סעיפים קטנים (ב) ו־(ב1) לא יחולו אם מתקיים ... | encoded | s 9A(c) one of the exceptions holds |
| s9A(c)(1) | 202-202 |  | repealed or blank in this text | the text shows it repealed or blank |
| s9A(c)(2) | 203-203 | התובע, או בן משפחתו של התובע, זקוקים לרכב לצורך טי... | encoded | s 9A(c)(2) the vehicle is needed for medical treatment;  s 9A(c)(2) "family member" the person is one |
| s9A(c)(3) | 204-204 | התובע, בן זוגו או ילדו הוא נכה ברגליו ומשתלם לו מא... | encoded | s 9A(c)(3) the person disabled in the legs |
| s9A(c)(3A) | 205-205 | תובע שהוא מורשה נהיגה של נכה לפי הסכם בדבר גמלת ני... | encoded | s 9A(c)(3A) the driving licensee of a disabled person |
| s9A(c)(4) | 206-206 | לילדו של התובע משתלמת קצבה לפי הוראות סימן ו׳ לפרק... | encoded | s 9A(c)(4) a pension is paid for the claimant's child |
| s9A(c)(5) | 207-207 | רישיון הרכב הופקד אצל הרשות המוסמכת להוציא אותו רי... | encoded | s 9A(c)(5)(a) the claimant is ill and the licence is deposited;  s 9A(c)(5)(b) the tractor of an inactive farm |
| s9A(c)(5)(a) | 208-208 | התובע אינו מסוגל לעבוד בעבודה כלשהי בגלל מחלה, ובל... | fork | s 9A(c)(5)(a) the claimant is ill and the licence is deposited -- F8 period-ends-on-anniversary |
| s9A(c)(5)(b) | 209-209 | הרכב הוא טרקטור כאמור בתקנות התעבורה, התשכ״א–1961,... | encoded | s 9A(c)(5)(b) the tractor of an inactive farm |
| s9A(c)(6) | 210-210 |  | repealed or blank in this text | the text shows it repealed or blank |
| s9A(c)(7) | 211-211 |  | repealed or blank in this text | the text shows it repealed or blank |
| s10.head | 213-213 |  | inert (1: not operative) | a heading or section title: not operative |
| s10 | 214-214 | על אף האמור בסעיף 9, לא תיחשב כהכנסה – | encoded | s 10 the receipt is not counted as income |
| s10(1) | 215-215 | קיצבת ילדים לפי פרק ד׳ לחוק הביטוח; | encoded | s 10 the receipt is not counted as income |
| s10(2) | 216-216 | הענקות לחיילים ולבני משפחותיהם לפי חוק החיילים המש... | encoded | s 10 the receipt is not counted as income |
| s10(3) | 217-217 | כל הכנסה אחרת שקבע השר בתקנות. | encoded | s 10 the receipt is not counted as income |
| s11.head | 219-219 |  | inert (1: not operative) | a heading or section title: not operative |
| s11 | 220-220 | מי שיש לו בן זוג, תהיה הכנסתו לענין חוק זה צירוף ה... | encoded | s 11 the income of a person with a spouse |
| s12.head | 222-222 |  | inert (1: not operative) | a heading or section title: not operative |
| s12(a) | 223-223 | בחישוב הכנסתו לענין סעיף 5 של מי שמשתלמת לו גמלה ל... | fork | s 12(a) the section applies to the claimant -- F9 proviso-second-class-only |
| s12(a)(1) | 224-224 | סכום השווה ל־13% מהשכר הממוצע – מתגמול וכן מהכנסתו... | fork | s 12(a)(1) the deduction from earnings -- F10 per-earner-capped-at-income |
| s12(a)(2) | 225-225 | סכום השווה ל־40% מתגמול וכן מהכנסה מהמקורות המפורט... | encoded | s 12(a)(2) the deduction from earnings after paragraph (1) |
| s12(a)(2)(a) | 226-226 | לעניין חלק ההכנסה מתגמול וכן מהמקורות המפורטים בסע... | fork | s 12(a)(2)(a)-(b) the deduction for an independent parent -- F11 independent-parent-slices |
| s12(a)(2)(b) | 227-227 | לעניין חלק ההכנסה מתגמול ומעבודה העולה על 33.81% מ... | fork | s 12(a)(2)(a)-(b) the deduction for an independent parent -- F11 independent-parent-slices |
| s12(a)(3) | 228-228 | סכום השווה ל־13% מהשכר הממוצע – מהכנסה שמקורה בקיצ... | encoded | s 12(a)(3) the deduction from pension income |
| s12(b) | 229-229 | הסכומים שינוכו לפי סעיף קטן (א)(1) ו־(3) לא יעלו ע... | fork | s 12(b) the deductions under (a)(1) and (3) together;  s 12 the income after the deductions -- F12 paragraph-2-uses-uncapped-paragraph-1 |
| s12(c) | 230-230 | לענין סעיף זה וסעיפים 12א ו־12ב, | inert (1: not operative) | lead-in words ('for this section and ss 12A and 12B'): they create no rule of their own; the definitions that follow are encoded and used by ss 12, 12A and 12B |
| s12.def1 | 231-231 | ”תגמול“ – כל אחד מאלה: | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(1) | 232-232 | דמי לידה וגמלה לשמירת הריון כמשמעותם לפי פרק ג׳ לח... | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(2) | 233-233 | דמי פגיעה כמשמעותם לפי פרק ה׳ לחוק הביטוח; | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(3) | 234-234 |  | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(4) | 235-235 | גמלה המשולמת לעובד לפי הוראות פרק ח׳ לחוק הביטוח; | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(5) | 236-236 | תגמול כמשמעותו לפי פרק י״ב לחוק הביטוח; | encoded | s 12(c) "tagmul" the payment is one |
| s12.def1(6) | 237-237 | דמי אבטלה כהגדרתם בסעיף 158 לחוק הביטוח; | encoded | s 12(c) "tagmul" the payment is one |
| s12.def2 | 238-238 | ”מועסק בעל יכולת עבודה מופחתת“ – כל אחד מאלה: | encoded | s 12(c) "employed with reduced capacity for work" the person is one |
| s12.def2(1) | 239-239 | מי שזכאי לשכר מינימום מותאם לפי סעיף 17(ב) לחוק שכ... | encoded | s 12(c) "employed with reduced capacity for work" the person is one |
| s12.def2(2) | 240-240 | מי שמתקיים בו האמור בפסקה (17) לתוספת הראשונה; | encoded | s 12(c) "employed with reduced capacity for work" the person is one |
| s12.def2(3) | 241-241 | משתקם כהגדרתו בחוק זכויות לאנשים עם מוגבלות המועסק... | encoded | s 12(c) "employed with reduced capacity for work" the person is one |
| s12A.head | 243-243 |  | inert (1: not operative) | a heading or section title: not operative |
| s12A(a) | 244-244 | בחישוב הכנסתו לענין סעיף 5 של מי שמשתלמת לו גמלה ל... | encoded | s 12A(a) the section applies to the claimant |
| s12A(a)(1) | 245-245 | סכום השווה ל־5% מהשכר הממוצע, מתגמול וכן מהכנסתו ש... | fork | s 12A(a)(1) the deduction from earnings -- F10 per-earner-capped-at-income |
| s12A(a)(2) | 246-246 | סכום השווה לשיעור המחושב לפי התוספת השלישית, בהתאם... | fork | s 12A(a)(2) the deduction from earnings after paragraph (1) -- F11 independent-parent-slices |
| s12A(a)(3) | 247-247 | סכום השווה ל־5% מהשכר הממוצע, מהכנסה שמקורה בקצבה ... | encoded | s 12A(a)(3) the deduction from pension income |
| s12A(b) | 248-248 | הסכומים שינוכו לפי סעיף קטן (א)(1) ו־(3) לא יעלו ע... | encoded | s 12A(b) the deductions under (a)(1) and (3) together;  s 12A the income after the deductions |
| s12B.head | 250-250 |  | inert (1: not operative) | a heading or section title: not operative |
| s12B(a) | 251-251 | בחישוב הכנסתו לעניין סעיף 5 של מי שמשתלמת לו גמלה ... | encoded | s 12B(a) the section applies to the claimant |
| s12B(a)(1) | 252-252 | סכום השווה ל־23.5% מהשכר הממוצע – מתגמול וכן מהכנס... | fork | s 12B(a)(1) the deduction from earnings -- F10 per-earner-capped-at-income |
| s12B(a)(2) | 253-253 | סכום השווה ל־40% מתגמול וכן מהכנסה ממקורות המפורטי... | fork | s 12B(a)(2) the deduction from earnings after paragraph (1) -- F11 independent-parent-slices |
| s12B(a)(3) | 254-254 | סכום השווה ל־13% מהשכר הממוצע מהכנסה שמקורה בקצבה ... | encoded | s 12B(a)(3) the deduction from pension income |
| s12B(b) | 255-255 | הסכומים שינוכו לפי סעיף קטן (א)(1) ו־(3) לא יעלו ע... | encoded | s 12B(b) the deductions under (a)(1) and (3) together;  s 12B the income after the deductions |
| ch5.head | 257-257 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| ch5.sub1.head | 258-258 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s13.head | 260-260 |  | inert (1: not operative) | a heading or section title: not operative |
| s13(a) | 261-261 | תביעה לגימלה תוגש למוסד לביטוח לאומי; עובד המוסד ל... | encoded | s 13(a) where a claim for a benefit is submitted |
| s13(b) | 262-262 | השר יקבע בתקנות את המוסמכים לאשר אם מתקיימים באדם ... | inert (2: machinery) | the Minister's duty to make regulations on who certifies the conditions of s 2 |
| ch5.sub2.head | 264-264 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s14.head | 266-266 |  | inert (1: not operative) | a heading or section title: not operative |
| s14(a) | 267-267 | גימלה תשולם רק בעד התקופה שתחילתה ב־1 לחודש שבו הו... | encoded | s 14(a) the first day for which the benefit is paid;  s 14(a) the day is within the period for which the benefit is paid |
| s14(b) | 268-268 |  | repealed or blank in this text | the text shows it repealed or blank |
| s14(c)(1) | 269-269 | על אף האמור בסעיף קטן (א), מי שהגיע לגיל פרישה ומב... | encoded | s 14(c)(1) the benefit is paid for a month before the month of the claim |
| s14(c)(2) | 270-270 | אין בהוראות פסקה (1) כדי לזכות את מי שמשתלמת לו גמ... | encoded | s 14(c)(2) the person paid under paragraph (1) is entitled to the privilege;  s 14(c)(2) "public body" the body is one |
| s14A.head | 272-272 |  | inert (1: not operative) | a heading or section title: not operative |
| s14A(a) | 273-273 | לא תשולם לזכאי שיצא את ישראל גמלה בעד חודש קלנדרי ... | encoded | s 14A(a) the benefit is not paid for the month |
| s14A(b) | 274-274 | לא תשולם לזכאי שיצא את ישראל גמלה בעד החודש הקלנדר... | encoded | s 14A(b) the benefit is not paid for the month of exit and the month of return |
| s14A(b)(1) | 275-275 | לפני שיצא את ישראל כאמור, הוא יצא את ישראל פעם נוס... | encoded | s 14A(b) the benefit is not paid for the month of exit and the month of return |
| s14A(b)(2) | 276-276 | הוא לא היה זכאי לגמלה בעד החודש הקלנדרי שקדם לחודש... | encoded | s 14A(b) the benefit is not paid for the month of exit and the month of return |
| s14A(c) | 277-277 | על אף הוראות סעיף קטן (ב), לא תשולם גמלה לזכאי שחל... | fork | s 14A(c) the benefit is not paid for the month of exit and the month of return -- F13 c-exception-needs-both |
| s14A(c1) | 278-278 | לא תשולם גמלה לזכאי שהוא או בן זוגו הגיעו לגיל פרי... | encoded | s 14A(c1) the benefit is not paid for the month |
| s14A(c1)(1) | 279-279 | הזכאי ובן זוגו יצאו את ישראל, במצטבר, ארבע פעמים ב... | encoded | s 14A(c1) the benefit is not paid for the month |
| s14A(c1)(1A) | 280-280 | הזכאי ובן זוגו יצאו את ישראל, במצטבר, יותר מארבע פ... | encoded | s 14A(c1) the benefit is not paid for the month |
| s14A(c1)(2) | 281-281 | הזכאי ובן זוגו יצאו את ישראל, במצטבר, פחות מארבע פ... | encoded | s 14A(c1) the benefit is not paid for the month |
| s14A(c1)(2)(a) | 282-282 | בעד כל אחד מהחודשים, כולם או חלקם, מהיום ה־73 ועד ... | fork | s 14A(c1) the benefit is not paid for the month -- F14 c1-month-holds-day-73-to-100 |
| s14A(c1)(2)(b) | 283-283 | בעד כל אחד מהחודשים באותה שנה קלנדרית שבהם שהו, בכ... | encoded | s 14A(c1) the benefit is not paid for the month |
| s14A(d)(1) | 284-284 | הוראות סעיפים קטנים (א), (ב) ו־(ג1) לא יחולו על מי... | encoded | s 14A(d) subsections (a), (b) and (c1) do not apply to the person |
| s14A(d)(1)(1) | 285-285 | הוא היה זכאי לגמלה בעד החודש הקלנדרי שקדם לחודש הי... | encoded | s 14A(d) subsections (a), (b) and (c1) do not apply to the person |
| s14A(d)(1)(2) | 286-286 | הוא נזקק לטיפול רפואי מחוץ לישראל, או שהוא זכאי לג... | encoded | s 14A(d) subsections (a), (b) and (c1) do not apply to the person |
| s14A(d)(2) | 287-287 | גמלה לפי סעיף קטן זה תשולם לפי כללים, תנאים ולתקופ... | encoded | s 14A(d) subsections (a), (b) and (c1) do not apply to the person |
| s14A(d)(3) | 288-288 | בסעיף קטן זה, ”טיפול רפואי מחוץ לישראל“ – שירות בר... | encoded | s 14A(d)(3) "medical treatment outside Israel" the service is one |
| s14A(e) | 289-289 | היה לאדם הנמצא מחוץ לישראל ואשר אינו זכאי לגמלה בש... | encoded | s 14A(e) the benefit paid to the spouse in Israel |
| s14A(f)(1) | 290-290 | שהה זכאי לגמלה מחוץ לישראל 183 ימים לפחות במהלך 12... | encoded | s 14A(f)(1) the entitled person is treated as outside Israel;  s 14A(f)(1) the spouse is treated as an individual |
| s14A(f)(2) | 291-291 | הוראות פסקה (1) לא יחולו על אלה: | encoded | s 14A(f)(2) paragraph (1) does not apply to the person |
| s14A(f)(2)(a) | 292-292 | מי שהודיע למוסד לביטוח לאומי במועד, בתנאים ובאופן ... | encoded | s 14A(f)(2) paragraph (1) does not apply to the person |
| s14A(f)(2)(b) | 293-293 | מי ששהה מחוץ לישראל לצורך קבלת טיפול רפואי הניתן ל... | encoded | s 14A(f)(2) paragraph (1) does not apply to the person |
| s14B.head | 295-295 |  | inert (1: not operative) | a heading or section title: not operative |
| s14B | 296-296 | הזכאי לגמלה בעד אחד מהחודשים אוקטובר, נובמבר או דצ... | fork | s 14B the heating grant -- F15 heating-grant-once-a-year |
| s15.head | 298-298 |  | inert (1: not operative) | a heading or section title: not operative |
| s15(a) | 299-299 | נפטר זכאי שהיתה משתלמת לו גימלה, ישלם המוסד לביטוח... | encoded | s 15(a) who is paid the death grant;  s 15(a) the 1 April before the day of death;  s 15(a) the amount of the death grant |
| s15(b) | 300-300 | הזכאי למענק פטירה לפי סעיף זה וכן למענק פטירה לפי ... | encoded | s 15(b) how many of the two grants the person may receive |
| s16.head | 302-302 |  | inert (1: not operative) | a heading or section title: not operative |
| s16 | 303-303 | לענין מי שמצוי בהכשרה מקצועית רשאי השר לקבוע בתקנו... | inert (2: machinery) | the Minister's power to make regulations on payment through another body |
| s17.head | 305-305 |  | inert (1: not operative) | a heading or section title: not operative |
| s17(a) | 306-306 | אדם החייב על פי כל דין או הסכם במזונותיו של מי ששו... | encoded | s 17(a) the Institute may claim compensation from the person |
| s17(b) | 307-307 | הזכאי לגימלה חייב להושיט כל עזרה ולנקוט כל פעולה ס... | encoded | s 17(b) the recipient must help the Institute;  s 17(b) the recipient shall not harm the Institute's right;  s 17(b) the recipient is in breach of the duty |
| s17(c) | 308-308 | בית המשפט המוסמך לדון בתביעת המוסד לביטוח לאומי לפ... | encoded | s 17(c) the District Court may hear the claim;  s 17(c) the religious court may also hear the claim |
| s18.head | 310-310 |  | inert (1: not operative) | a heading or section title: not operative |
| s18 | 311-311 | המוסד לביטוח לאומי רשאי להפחית, להשהות או לשלול גי... | encoded | s 18 the Institute may reduce, suspend or revoke the benefit |
| ch5.sub3.head | 313-313 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s19.head | 315-315 |  | inert (1: not operative) | a heading or section title: not operative |
| s19(a) | 316-316 | לצורך קביעת הזכאות לגימלה או המשך תשלומה, חייב התו... | encoded | s 19(a) the claimant or recipient must comply with the Institute's demand;  s 19(a) the claimant or recipient has met the Institute's demand |
| s19(a)(1) | 317-317 | למסור למוסד לביטוח לאומי כל ידיעה או מסמכים שברשות... | encoded | s 19(a) the claimant or recipient must comply with the Institute's demand;  s 19(a) the claimant or recipient has met the Institute's demand |
| s19(a)(2) | 318-318 | לעמוד לבדיקה רפואית או לבדיקה של פסיכולוג, של מומח... | encoded | s 19(a) the claimant or recipient must comply with the Institute's demand;  s 19(a) the claimant or recipient has met the Institute's demand |
| s19(a)(3) | 319-319 | להופיע לפני מי שהמוסד לביטוח לאומי קבע לכך ולמסור ... | encoded | s 19(a) the claimant or recipient must comply with the Institute's demand;  s 19(a) the claimant or recipient has met the Institute's demand |
| s19(b) | 320-320 | כל עוד לא קויימה דרישה לפי סעיף קטן (א), רשאי המוס... | encoded | s 19(b) the Institute may delay the claim, stop payment or refuse the benefit |
| s19(c) | 321-321 |  | repealed or blank in this text | the text shows it repealed or blank |
| s20.head | 323-323 |  | inert (1: not operative) | a heading or section title: not operative |
| s20 | 324-324 | מקבל גמלה יודיע בכתב למוסד לביטוח לאומי בכתב על כל... | encoded | s 20 the recipient must report a change;  s 20 the recipient notified the change in time |
| s20A.head | 326-326 |  | inert (1: not operative) | a heading or section title: not operative |
| s20A | 327-327 | הוראות סעיף 327 לחוק הביטוח יחולו גם לגבי מי שתובע... | encoded | s 20A the provisions of s 327 of the Insurance Law apply to the person |
| s20B.head | 329-329 |  | inert (1: not operative) | a heading or section title: not operative |
| s20B(a) | 330-330 | תובע שמסר הצהרה כוזבת לגבי מידע הדרוש למוסד לביטוח... | encoded | s 20B(a) the claimant is liable to a fine |
| s20B(b)(1) | 331-331 | קיבל מקבל גמלה הודעה מהמוסד לביטוח לאומי בדואר רשו... | fork | s 20B(b)(1) the recipient is liable to a fine -- F8 period-ends-on-anniversary |
| s20B(b)(2) | 332-332 | ההודעה כאמור בפסקה (1) תכלול אזהרה בנוסח האמור בחל... | encoded | s 20B(b)(2) the notice meets the content requirements |
| s20B(b)(3) | 333-333 | נשלחה למקבל גמלה הודעה לפי סעיף קטן זה בדואר רשום ... | fork | s 20B(b)(3) the notice is deemed served -- F16 service-on-day-15 |
| s20B(b)(4) | 334-334 | הוכיח מקבל גמלה כי לא קיבל את ההודעה בדואר רשום מס... | encoded | s 20B(b)(4) paragraph (1) applies to the recipient all the same |
| s20B(b)(5) | 335-335 | הוראות סעיף קטן זה לא יחולו על מי שנקבעה לגביו נכו... | encoded | s 20B(b)(5) subsection (b) does not apply to the recipient |
| s21.head | 337-337 |  | inert (1: not operative) | a heading or section title: not operative |
| s21(a) | 338-338 | עובד המוסד לביטוח לאומי שמינהלת המוסד הסמיכה אותו ... | encoded | s 21(a) the employee may enter the place;  s 21(a) the employee may enter by force |
| s21(b) | 339-339 | מי שנחקר או שבחצריו נערכת בדיקה לפי סעיף קטן (א), ... | encoded | s 21(b) the person questioned must answer;  s 21(b) the person met the duty to answer |
| s21(c) | 340-340 | אדם שברשותו או בידיעתו ידיעות בדבר הכנסתו או רכושו... | encoded | s 21(c) the person with the information must give it;  s 21(c) the person gave the details in time |
| s21A.head | 342-342 |  | inert (1: not operative) | a heading or section title: not operative |
| s21A | 343-343 | לעניין הוראות סעיפים 3ג, 5(ד) ו־6(ה) יחולו הוראות ... | encoded | s 21A(1) the Institute may use the information;  s 21A(2) the provisions of s 326(g) of the Insurance Law apply -- the lead-in scopes both paragraphs |
| s21A(1) | 344-344 | המוסד רשאי לעשות שימוש במידע שנמסר לו לפי הוראות ס... | encoded | s 21A(1) the Institute may use the information |
| s21A(2) | 345-345 | אם העבירה כאמור באותם סעיפים היא עבירת טרור ביטחונ... | encoded | s 21A(2) the provisions of s 326(g) of the Insurance Law apply |
| ch5.sub4.head | 347-347 |  | inert (1: not operative) | a chapter or sub-chapter heading: not operative |
| s22.head | 349-349 |  | inert (1: not operative) | a heading or section title: not operative |
| s22 | 350-350 | חברה, אגודה שיתופית או כל חבר בני אדם אחר שעברו עב... | encoded | s 22 the manager is treated as responsible for the body's offence |
| s23.head | 352-352 |  | inert (1: not operative) | a heading or section title: not operative |
| s23(a) | 353-353 | סעיפים 2א, 297א, 297ב, 301, 302(א)(1) ו־(ב), 303, ... | encoded | s 23(a) the section of the Insurance Law applies to this Law;  s 23(a) the sections of the Insurance Law that apply |
| s23(b) | 354-354 | על אף האמור בסעיף 303(א) לחוק הביטוח, גימלה אינה נ... | encoded | s 23(b) the benefit may be transferred, pledged or attached |
| s24.head | 356-356 |  | inert (1: not operative) | a heading or section title: not operative |
| s24(a) | 357-357 | השר רשאי לקבוע בתקנות כללים, מבחנים ותנאים בדבר הש... | inert (2: machinery) | the Minister's power to make regulations on the Treasury's share in special needs |
| s24(b) | 358-358 | בתקנות לפי סעיף זה יכול שייקבע סכום שהמוסד לביטוח ... | inert (2: machinery) | the Minister's power to make regulations on a deduction |
| s24(c) | 359-359 | הוראות סימן ג׳ לפרק זה, וכן הוראות אחרות של פרק זה... | encoded | s 24(c) the provisions of sub-chapter C apply to the matter |
| s25.head | 361-361 |  | inert (1: not operative) | a heading or section title: not operative |
| s25(a) | 362-362 | גימלאות לפי חוק זה ישולמו מאוצר המדינה באמצעות המו... | encoded | s 25(a) who pays the benefit |
| s25(b) | 363-363 | אוצר המדינה יעביר למוסד לביטוח לאומי מדי חודש בחדש... | encoded | s 25(b) the State Treasury transfers the money for the month |
| s26.head | 365-365 |  | inert (1: not operative) | a heading or section title: not operative |
| s26 | 366-366 | לבית דין אזורי כמשמעותו בחוק בית הדין לעבודה, התשכ... | encoded | s 26 the Regional Labour Court has exclusive jurisdiction |
| s27.head | 368-368 |  | inert (1: not operative) | a heading or section title: not operative |
| s27 | 369-369 | השר רשאי לקבוע בתקנות, בין לגבי כלל הזכאים ובין לג... | inert (2: machinery) | the Minister's power to make regulations on filing claims and paying benefits |
| s27(1) | 370-370 | הגשת תביעה לגימלה והמסמכים שיש לצרף לתביעה; | inert (2: machinery) | the Minister's power to make regulations |
| s27(2) | 371-371 | אופן התשלום של גימלאות ומועדי תשלומן; | inert (2: machinery) | the Minister's power to make regulations |
| s27(3) | 372-372 |  | inert (2: machinery) | the Minister's power to make regulations |
| s28.head | 374-374 |  | inert (1: not operative) | a heading or section title: not operative |
| s28 | 375-375 |  | inert (2: machinery) | an amendment of another Act, shown as incorporated |
| s29.head | 377-377 |  | inert (1: not operative) | a heading or section title: not operative |
| s29 | 378-378 |  | inert (2: machinery) | an amendment of another Act, shown as incorporated |
| s30.head | 380-380 |  | inert (1: not operative) | a heading or section title: not operative |
| s30(a) | 381-381 | סעיף 143ב לחוק הביטוח, כנוסחו לפני תחילת חוק זה, י... | inert (2: machinery) | a saving for support paid before the Law began: s 143B of the Insurance Law as it then read |
| s30(b) | 382-382 | אדם שבתכוף לפני שנעשה זכאי לגימלה קיבל תמיכה חדשית... | encoded | s 30(b) the benefit paid, not less than the last support |
| s30(c) | 383-383 | השר רשאי לקבוע בתקנות הוראות מיוחדות בדבר קביעת זכ... | inert (2: machinery) | the Minister's power to make regulations on those who received support before the Law began |
| s30A.head | 385-385 |  | inert (1: not operative) | a heading or section title: not operative |
| s30A(a) | 386-386 | בסעיף זה, ”זכאי קודם“ – מי שלא מתקיים בו האמור בסע... | encoded | s 30A(a) the person is a former entitled person |
| s30A(a)(1) | 387-387 | הוראות סעיף 5(א)(2), (2א) או (ד) בחוק זה, כנוסחם ע... | encoded | s 30A(a) the person is a former entitled person |
| s30A(a)(2) | 388-388 | הוראת סעיף 5(ג) בחוק זה, כנוסחו ערב תחילתו של פרק ... | encoded | s 30A(a) the person is a former entitled person |
| s30A(b) | 389-389 | על אף הוראות סעיף 5(א), הגמלה לזכאי שהוא זכאי קודם... | encoded | s 30A(b) the benefit of a former entitled person |
| s30A(c) | 390-390 | הוראות סעיף קטן (ב) לא יחולו על זכאי קודם שאחרי יו... | encoded | s 30A(c) subsection (b) does not apply and s 5(a) applies |
| s31.head | 392-392 |  | inert (1: not operative) | a heading or section title: not operative |
| s31(a) | 393-393 | השר ממונה על ביצוע חוק זה, והוא רשאי להתקין תקנות ... | inert (2: machinery) | the Minister is in charge of carrying out the Law and may make regulations |
| s31(b) | 394-394 | תקנות לפי סעיפים 2(ג), 3(4), 4(ב), 5(ה), 7(א), 9(ב... | inert (2: machinery) | which regulations need the Finance Minister's consent |
| s31(c) | 395-395 | תקנות לפי סעיפים 2(ג), 2(ה), 3(4), 4(ב), 5(ה)(2) ו... | inert (2: machinery) | which regulations need the Knesset committee's approval |
| s32.head | 397-397 |  | inert (1: not operative) | a heading or section title: not operative |
| s32 | 398-398 | תחילתו של חוק זה ביום ו׳ בטבת התשמ״ב (1 בינואר 198... | inert (2: machinery) | commencement |
| sch1.head | 400-402 |  | inert (1: not operative) | a schedule or part heading: not operative |
| sch1.item1 | 404-404 |  | encoded | sch 1 item 1(a) the child meets the conditions |
| sch1.item1(a) | 405-405 | ילד יתום או ילד הזכאי לגמלה מיוחדת, שמתקיימים בו כ... | encoded | sch 1 item 1(a) the child meets the conditions |
| sch1.item1(a)(1) | 406-406 | אם מלאו לו 18 שנים וטרם מלאו לו 20 שנים – עיקר זמנ... | encoded | sch 1 item 1(a) the child meets the conditions |
| sch1.item1(a)(2) | 407-407 | הוא אינו ילד מאומץ הנמצא במשמורתו של ההורה המאמץ; | encoded | sch 1 item 1(a) the child meets the conditions |
| sch1.item1(a)(3) | 408-408 | אוצר המדינה או רשות מקומית אינם נושאים בהחזקתו; | encoded | sch 1 item 1(a) the child meets the conditions |
| sch1.item1(b) | 409-409 | הגמלה לילד יתום או לילד הזכאי לגמלה מיוחדת כאמור ב... | encoded | sch 1 item 1(b) the benefit for the children |
| sch1.item1(b)(1) | 410-410 | לילד אחד – 25% מהסכום הבסיסי פחות נקודת קצבה; | encoded | sch 1 item 1(b) the benefit for the children |
| sch1.item1(b)(2) | 411-411 | לשני ילדים – 37.5% מהסכום הבסיסי פחות שתי נקודות ק... | encoded | sch 1 item 1(b) the benefit for the children |
| sch1.item1(b)(3) | 412-412 | לכל ילד נוסף – 10% מהסכום הבסיסי; | encoded | sch 1 item 1(b) the benefit for the children |
| sch1.item1(b1) | 413-413 | הגמלה לילד יתום או נטוש כאמור בפסקת משנה (א) הנמצא... | encoded | sch 1 item 1(b1) the benefit for a child in a relative's custody is paid for the month;  sch 1 item 1(b1) the person is a relative |
| sch1.item1(c) | 414-414 | בפסקה זו – | encoded | sch 1 item 1(c) the parent is absent |
| sch1.item1.def1 | 415-415 | ”ילד יתום“ – ילד יתום משני הוריו, או ילד יתום מהור... | encoded | sch 1 item 1(c) the child is an orphan child |
| sch1.item1.def2 | 416-416 | ”ילד הזכאי לגמלה מיוחדת“ – ילד שהוריו נטשו אותו בי... | encoded | sch 1 item 1(c) the child is a child entitled to a special benefit |
| sch1.item1.def3 | 417-417 | ”נעדר“ – אחד מאלה: | encoded | sch 1 item 1(c) the parent is absent |
| sch1.item1.def3(1) | 418-418 | גר דרך קבע מחוץ לישראל; | encoded | sch 1 item 1(c) the parent is absent |
| sch1.item1.def3(2) | 419-419 | עקבותיו נעלמו; | encoded | sch 1 item 1(c) the parent is absent |
| sch1.item1.def3(3) | 420-420 | לא ידוע; | encoded | sch 1 item 1(c) the parent is absent |
| sch1.item2 | 422-422 |  | encoded | sch 1 item 2 the person aged 18 or over was paid under item 1 before reaching 18 |
| sch1.item2.text | 423-423 | מי שמלאו לו 18 שנים ושולמה לו גמלה לפני הגיעו לגיל... | encoded | sch 1 item 2 the person aged 18 or over was paid under item 1 before reaching 18 |
| sch1.item3 | 425-425 |  | encoded | sch 1 item 3 the person is a parent of a child in their custody |
| sch1.item3.text | 426-426 | הורה לילד שבהחזקתו; | encoded | sch 1 item 3 the person is a parent of a child in their custody |
| sch1.item4 | 428-428 |  | encoded | sch 1 item 4 the person's spouse is entitled |
| sch1.item4.text | 429-429 | בן זוגו זכאי לגמלה, ובלבד שאינו זכאי לגמלה לפי סעי... | encoded | sch 1 item 4 the person's spouse is entitled |
| sch1.item5 | 431-431 |  | encoded | sch 1 item 5 the woman lives with her parents who receive the benefit;  sch 1 item 5 the benefit before income |
| sch1.item5.text | 432-432 | אישה הרה הגרה עם הוריה המקבלים גמלה, או עם אחד מהם... | encoded | sch 1 item 5 the woman lives with her parents who receive the benefit;  sch 1 item 5 the benefit before income |
| sch1.item6 | 434-434 |  | encoded | sch 1 item 6 the woman does not live with her parents |
| sch1.item6.text | 435-435 | אישה הרה שאינה גרה עם הוריה, או עם אחד מהם; | encoded | sch 1 item 6 the woman does not live with her parents |
| sch1.item7 | 437-437 |  | encoded | sch 1 item 7 a pregnant woman aged 18 or over in or after week 13 |
| sch1.item7.text | 438-438 | אישה הרה שמלאו לה 18 שנים, החל בשבוע ה־13 להריונה; | encoded | sch 1 item 7 a pregnant woman aged 18 or over in or after week 13 |
| sch1.item8 | 440-440 |  | encoded | sch 1 item 8 severe distress |
| sch1.item8.text | 441-441 | מי שמלאו לו 18 שנים והוא נקלע למצב מצוקה חמור עקב ... | encoded | sch 1 item 8 severe distress |
| sch1.item9 | 443-443 |  | encoded | sch 1 item 9 release from arrest or imprisonment |
| sch1.item9.text | 444-444 | מי שמלאו לו 18 שנים וריצה, במשך תקופה של שישה חודש... | encoded | sch 1 item 9 release from arrest or imprisonment |
| sch1.item10 | 446-446 |  | encoded | sch 1 item 10 illness lasting more than 30 days;  sch 1 item 10 the earliest day of entitlement |
| sch1.item10.text | 447-447 | מי שמלאו לו 18 שנים והוא אינו מסוגל לעבוד בעבודה כ... | encoded | sch 1 item 10 illness lasting more than 30 days;  sch 1 item 10 the earliest day of entitlement |
| sch1.item11 | 449-449 |  | encoded | sch 1 item 11 treatment under a probation order or supervision |
| sch1.item11.text | 450-450 | מי שמלאו לו 18 שנים והוא מטופל במוסד או נמצא בתהלי... | encoded | sch 1 item 11 treatment under a probation order or supervision |
| sch1.item12 | 452-452 |  | encoded | sch 1 item 12 found not placeable by a diagnosis centre |
| sch1.item12.text | 453-453 | מי שמלאו לו 18 שנים ומרכז לאבחון מתמכרים לסמים שאי... | encoded | sch 1 item 12 found not placeable by a diagnosis centre |
| sch1.item13 | 455-455 |  | encoded | sch 1 item 13 an alcoholics treatment centre |
| sch1.item13.text | 456-456 | מי שמלאו לו 18 שנים ומרכז לטיפול באלכוהוליסטים, המ... | encoded | sch 1 item 13 an alcoholics treatment centre |
| sch1.item14 | 458-458 |  | encoded | sch 1 item 14 incapacity to earn of 75% or more |
| sch1.item14.text | 459-459 | מי שמלאו לו 18 שנים ונקבעה לגביו דרגת אי כושר להשת... | encoded | sch 1 item 14 incapacity to earn of 75% or more |
| sch1.item15 | 461-461 |  | encoded | sch 1 item 15 injury allowance |
| sch1.item15.text | 462-462 | מי שמלאו לו 18 שנים והוא מקבל דמי פגיעה לפי סימן ד... | encoded | sch 1 item 15 injury allowance |
| sch1.item16 | 464-464 |  | encoded | sch 1 item 16 imprisonment by community service |
| sch1.item16.text | 465-465 | מי שמלאו לו 18 שנים והוא נושא מאסר בעבודות שירות ל... | encoded | sch 1 item 16 imprisonment by community service |
| sch1.item17 | 467-467 |  | encoded | sch 1 item 17 sheltered workshop |
| sch1.item17.text | 468-468 | מי שמלאו לו 18 שנים והוא עובד מטעמי בריאות במפעל מ... | encoded | sch 1 item 17 sheltered workshop |
| sch1.item18 | 470-470 |  | encoded | sch 1 item 18 bail and electronic monitoring |
| sch1.item18.text | 471-471 | מי שמלאו לו 18 שנים ומתקיים בו אחד מאלה: | encoded | sch 1 item 18 bail and electronic monitoring |
| sch1.item18(a) | 472-472 | הוא שוחרר בערובה בתנאים כאמור בסעיף 48 לחוק סדר הד... | encoded | sch 1 item 18 bail and electronic monitoring |
| sch1.item18(b) | 473-473 | ילדו או בן זוגו שוחררו בערובה בתנאים כאמור בסעיף 4... | encoded | sch 1 item 18 bail and electronic monitoring |
| sch1.item19 | 475-475 |  | encoded | sch 1 item 19 sleeping rough |
| sch1.item19.text | 476-476 | מי שמלאו לו 18 שנים והוא מטופל על ידי הלשכה לשירות... | encoded | sch 1 item 19 sleeping rough |
| sch1.item20 | 478-478 |  | encoded | sch 1 item 20 rehabilitation framework |
| sch1.item20.text | 479-479 | מי שמלאו לו 18 שנים והוא נמצא במסגרת שיקומית בפיקו... | encoded | sch 1 item 20 rehabilitation framework |
| sch1.item21 | 481-481 |  | encoded | sch 1 item 21 the conditions of s 2(a)(7) are met |
| sch1.item21.text | 482-482 | מי שמלאו לו 18 שנים והתקיימו בו התנאים שנקבעו לפי ... | encoded | sch 1 item 21 the conditions of s 2(a)(7) are met |
| sch1.item22 | 484-484 |  | encoded | sch 1 item 22 dependants' or survivors' allowance |
| sch1.item22.text | 485-485 | מי שמשתלמת לו קצבת תלויים לפי סימן ח׳ בפרק ה׳ בחוק... | encoded | sch 1 item 22 dependants' or survivors' allowance |
| sch1.item23 | 487-487 |  | encoded | sch 1 item 23 a new immigrant studying at an ulpan |
| sch1.item23.text | 488-488 | עולה חדש שמלאו לו 18 שנים והוא לומד באולפן לפי הפנ... | encoded | sch 1 item 23 a new immigrant studying at an ulpan |
| sch1.item24 | 490-490 |  | encoded | sch 1 item 24 disability allowance as a housewife |
| sch1.item24.text | 491-491 | מי שמשתלמת לה קצבת נכות כעקרת בית לפי סימן ב׳ בפרק... | encoded | sch 1 item 24 disability allowance as a housewife |
| sch1.item25 | 493-493 |  | encoded | sch 1 item 25(a) the child of a detained or imprisoned parent |
| sch1.item25(a) | 494-494 | ילד תושב ישראל, שאחד מהוריו הוא תושב ישראל הנמצא ב... | encoded | sch 1 item 25(a) the child of a detained or imprisoned parent |
| sch1.item25(b) | 495-495 | הגמלה לילד כאמור בפסקת משנה (א) תהיה בשיעור הקבוע ... | encoded | sch 1 item 25(b) the benefit for the children of a detained or imprisoned parent |
| sch1.item25(c) | 496-496 | לעניין גמלה המשולמת לפי הוראות פסקת משנה (א), יכול... | encoded | sch 1 item 25(c) the parent's income may be counted |
| sch1.item26 | 498-498 |  | encoded | sch 1 item 26 a shelter for battered women |
| sch1.item26.text | 499-499 | אישה השוהה במקלט לנשים מוכות באישור המחלקה לשירותי... | encoded | sch 1 item 26 a shelter for battered women |
| sch2.head | 501-503 |  | inert (1: not operative) | a schedule or part heading: not operative |
| sch2.block1 | 505-509 |  | encoded | sch 2 the rate in the table cell |
| sch2.row1 | 510-510 | (1) יחיד 42.14% 42.55% 42.96% 20% 25% | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row2 | 511-511 | (2) שני בני זוג 66.58% 67.24% 67.89% 27.5% 37.5% | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row3 | 512-512 | (3) שני בני זוג שעמם ילד 77.39% 78.04% 78.70% 30% ... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row4 | 513-513 | (4) שני בני זוג שעמם שני ילדים לפחות 88.19% 88.87%... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row5 | 514-514 | (5) יחיד שעמו ילד 71.92% פחות הסכום הבסיסי לילד 72... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row6 | 515-515 | (6) יחיד שעמו שני ילדים לפחות 82.72% פחות הסכום הב... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row7 | 516-516 | (7) אלמנה או הורה עצמאי שעמם ילד 71.92% פחות הסכום... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.row8 | 517-518 | (8) אלמנה או הורה עצמאי שעמם שני ילדים לפחות 82.72... | encoded | sch 2 the rate in the table cell;  sch 2 the table cell subtracts the basic amount for a child;  sch 2 which row of the table applies to the household |
| sch2.block2 | 520-520 |  | encoded | sch 2 note what the basic amount for a child is |
| sch2.block2.text | 521-521 | בתוספת זו, ”הסכום הבסיסי לילד“ – הסכום הבסיסי לעני... | encoded | sch 2 note what the basic amount for a child is |
| sch3.head | 523-525 |  | inert (1: not operative) | a schedule or part heading: not operative |
| sch3.block1 | 527-527 |  | encoded | sch 3 the rate in the table row |
| sch3.block1.text | 528-529 |  | encoded | sch 3 the rate in the table row |
| sch3.row1 | 530-530 | (1) אלמנה או הורה עצמאי שעמם ילד אחד לפחות 40% | fork | sch 3 which row of the table applies to the household;  sch 3 the rate in the table row;  sch 3 the rate of deduction for the household -- F17 schedule-3-overlap-is-nothing |
| sch3.row2 | 531-531 | (2) שני בני זוג שעמם שני ילדים לפחות 37.5% | fork | sch 3 which row of the table applies to the household;  sch 3 the rate in the table row;  sch 3 the rate of deduction for the household -- F17 schedule-3-overlap-is-nothing |
| sch3.row3 | 532-532 | (3) יחיד הזכאי לגמלה לפי סעיף 30א, שני בני זוג הזכ... | fork | sch 3 which row of the table applies to the household;  sch 3 the rate in the table row;  sch 3 the rate of deduction for the household -- F17 schedule-3-overlap-is-nothing |
| sch3.row4 | 533-534 | (4) כל הרכב משפחתי אחר 30% | fork | sch 3 which row of the table applies to the household;  sch 3 the rate in the table row;  sch 3 the rate of deduction for the household -- F17 schedule-3-overlap-is-nothing |
| sch4.head | 536-538 |  | inert (1: not operative) | a schedule or part heading: not operative |
| sch4.block1 | 540-542 |  | encoded | sch 4 the rate in the table row |
| sch4.row1 | 543-543 | (1) יחיד 22.5% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row2 | 544-544 | (2) שני בני זוג 30% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row3 | 545-545 | (3) שני בני זוג שעמם ילד 33.5% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row4 | 546-546 | (4) שני בני זוג שעמם שני ילדים לפחות 39% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row5 | 547-547 | (5) יחיד שעמו ילד 33.5% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row6 | 548-548 | (6) יחיד שעמו שני ילדים לפחות 37.5% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row7 | 549-549 | (7) אלמנה או הורה עצמאי שעמם ילד 33.5% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch4.row8 | 550-551 | (8) אלמנה או הורה עצמאי שעמם שני ילדים לפחות 39% | encoded | sch 4 the rate in the table row;  s 30A(b) the benefit of a former entitled person |
| sch5.head | 553-554 |  | inert (1: not operative) | a schedule or part heading: not operative |
| sch5.partA.head | 555-555 |  | inert (1: not operative) | a part heading: not operative |
| sch5.partA.body | 557-557 |  | encoded | sch 5 part A note what the basic amount is |
| sch5.partA.text | 558-558 | בלוח זה, ”הסכום הבסיסי“ – הסכום כאמור בפסקה (3) לה... | encoded | sch 5 part A note what the basic amount is |
| sch5.partA.item1 | 560-560 |  | fork | sch 5 part A item 1 the account balance must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item1.text | 561-561 | קיומה או אי־קיומה של יתרת חשבון של מקבל הגמלה במוס... | fork | sch 5 part A item 1 the account balance must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item2 | 563-563 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item2.text | 564-564 | קיומה או אי־קיומה של זכות בנכס מקרקעין, של מקבל הג... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item3 | 566-566 |  | fork | sch 5 part A item 3 the income from work must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item3.text | 567-567 | גובה ההכנסה מעבודה שמקבל הגמלה עובד בה, או שינוי ש... | fork | sch 5 part A item 3 the income from work must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item4 | 569-569 |  | fork | sch 5 part A item 4 the income from other sources must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item4.text | 570-570 | הכנסה ממקורות אחרים של מקבל הגמלה או שינוי שחל בה,... | fork | sch 5 part A item 4 the income from other sources must be reported;  sch 5 part A the number of the detail;  sch 5 part B the detail is required -- F18 sch5-threshold-on-the-change |
| sch5.partA.item5 | 572-572 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item5.text | 573-573 | כתובת המגורים של מקבל הגמלה בישראל או שינוי בכתובת... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item6 | 575-575 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item6.text | 576-576 | היות מקבל הגמלה בעל אזרחות זרה או שינוי לעניין אזר... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item7 | 578-578 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item7.text | 579-579 | מועדי כניסה לישראל ויציאה ממנה של מקבל הגמלה, ותקו... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item8 | 581-581 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item8.text | 582-582 | מגורים תחת קורת גג אחת, תחילתם או הפסקתם של מגורים... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item8(1) | 583-583 | מי שנישא למקבל הגמלה, לרבות מי שנישא על פי הדין במ... | encoded | sch 5 part A item 8 living with the person must be reported;  sch 5 part A the number of the detail |
| sch5.partA.item8(2) | 584-584 | מי שהוא הורה של אחד מילדי מקבל הגמלה; | encoded | sch 5 part A item 8 living with the person must be reported;  sch 5 part A the number of the detail |
| sch5.partA.item8(3) | 585-585 | מי שיש למקבל הגמלה חשבון בנק משותף עמו או שיש למקב... | encoded | sch 5 part A item 8 living with the person must be reported;  sch 5 part A the number of the detail |
| sch5.partA.item8(4) | 586-586 | מי שיש למקבל הגמלה הסכם ממון או הסכם אחר בדבר שיתו... | encoded | sch 5 part A item 8 living with the person must be reported;  sch 5 part A the number of the detail |
| sch5.partA.item9 | 588-588 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item9.text | 589-589 | קבלת כספים על ידי מקבל הגמלה ישירות מהחייב או ממי ... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item10 | 591-591 |  | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partA.item10.text | 592-592 | קיומו או אי־קיומו של פסק דין מזונות לטובת מקבל הגמ... | encoded | sch 5 part A the number of the detail;  sch 5 part B the detail is required |
| sch5.partB.head | 594-594 |  | inert (1: not operative) | a part heading: not operative |
| sch5.partB.body | 596-596 |  | encoded | sch 5 part B the detail is required |
| sch5.partB.text | 597-601 |  | encoded | sch 5 part B the detail is required |
| sch5.partC.head | 603-603 |  | inert (1: not operative) | a part heading: not operative |
| sch5.partC.body | 605-605 |  | encoded | sch 5 part C the warning the notice must carry |
| sch5.partC.text | 606-606 | הרינו להביא לידיעתך כי אם לא תעדכן את המוסד לביטוח... | encoded | sch 5 part C the warning the notice must carry |
| back.signatures | 608-616 |  | inert (1: not operative) | the record of enactment and signatures: not operative |
<!-- COVERAGE:END -->

## Fork register

**Bench rulings of 2026-11-04** (full text in `docs/ENCODING-GUIDE.md` section 5; they apply to every entry below).
These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23


Every ambiguity I saw, the readings, the one taken, and the text that licenses each.
Each entry is named by the backticked token used in the `.l4` comments (`grep` it in `isl-*.l4` to see the rule), and the coverage table points each `fork` row at its entry by F-number.
The readings taken are mine and unreviewed; none is a ruling.

| F | token | where | the text | readings seen | taken |
|---|---|---|---|---|---|
| F1 | `basic-amount-rates-added` | s 1 "basic amount" (1), `s 1 "basic amount" (1) the amount updated on 1 January 2006` | src:42-44: the index rise "בתוספת" (plus) an addition for pension recipients (a) or for everyone else (b) | (i) the addition is added to the rise as a rate, 1 + r1 + r2; (ii) the two compound, (1 + r1)(1 + r2) | (i). Asserted: 6,964 x (1 + 2% + 25%) = 8,844.28 and 6,964 x (1 + 2% + 3%) = 7,312.2 in `isl-tests-s01.l4` |
| F2 | `new-immigrant-any-of-four-days` | s 1 "new immigrant", `s 1 "new immigrant" the person is a new immigrant` | src:65-69: "מי שטרם מלאו 5 שנים מיום שהתקיים בו אחד מאלה" | (i) five years have not run from at least one of the days on which a limb was met (in effect the latest); (ii) from the first day any limb was met; (iii) limb by limb | (i); the dates are inputs |
| F3 | `institution-of-treatment` | s 2(a)(1)(a), `s 2(a)(1) the finding of non-placement was made by the body the text names for the situation` | src:80-81: "מרכז לאבחון מתמכרים לסמים שאישר השר או המוסד האמור; לענין זה ”מוסד“ ... כהגדרתם בחוק הפיקוח" | (i) "המוסד האמור" is the institution (as the Supervision Law defines it) in which the person is treated; (ii) any such institution; (iii) the diagnosis centre only | (i) |
| F4 | `second-schedule-widow-overlap-is-nothing` | s 5(a)(3) and Second Schedule rows 5 to 8, `sch 2 which row of the table applies to the household` (also the Fourth Schedule, which takes its row) | src:137: an independent parent is paid "לפי הפרטים (7) או (8)"; src:516-517 label rows 7 and 8 "אלמנה או הורה עצמאי שעמם ילד"; src:55 "יחיד" is one with no spouse, so a widow with a child fits row 5 (6) as well as row 7 (8) | (i) rows 7 and 8 govern over 5 and 6 for a widow and for an independent parent (the earlier encoding); (ii) rows 7 and 8 for an independent parent only, a widow who is not one uses 5 and 6; (iii) the more favourable row; (iv) rows 7 and 8 for an independent parent, NOTHING for a widow who is not one | (iv): an independent parent is sent to rows 7 and 8 by the text itself (s 5(a)(3), src:137), a widow who is not an independent parent fits two rows that nothing orders and gets NOTHING; a widow who is also an independent parent is an independent parent. `Household` carries the two as separate fields. Asserted: `isl-tests-p3-rates.l4` (which row, s 5(a), s 30A(b)) and the seat cases for s 5(a) and s 30A(b) |
| F5 | `supplement-period-from-62` | s 5(g), `s 5(g) the woman is entitled to the supplement for the month` | src:146-151: "במשך תקופה בהתאם לחודש לידתה" (4, 8, 12, 15, 18 months by birth year) | the length is given, the start is not: (i) from the month she reaches 62; (ii) from the month she claims; (iii) from the first month of entitlement under (a)(2)(b) | (i). Asserted: months 0 to 3 in, 4 out for a 1960 birth |
| F6 | `instalment-per-period` | s 9(b1)(2)(b), `s 9(b1)(2)(b) the income counted from the deemed property` | src:187: income from the deemed property "לא יעלה על הסכום המשתלם לתובע לשיעורין" | (i) at most the instalment for the period the income is worked out for; (ii) at most the sum of all instalments | (i). Asserted: 800 against 500 gives 500 |
| F7 | `money-is-the-total` | s 9 "amount not counted" (1), `s 9(c) "amount not counted" (1) the sum of money is not counted` | src:191: "סכום כסף שאינו עולה על ... הסכום הבסיסי כפול ארבע" (six with a child or spouse) | (i) the total money the claimant holds; (ii) each sum separately | (i). Asserted: 4,000 in, 4,001 not covered (basic amount 1,000) |
| F8 | `period-ends-on-anniversary` | s 9 "amount not counted" (2); s 9A(c)(5)(a); s 20B(b)(1) | src:192 "בתום 12 חודשים מאותו מועד"; the six-month limit in s 9A(c)(5)(a); src:331 "תוך ארבע שנים" | (i) the same calendar date later, clamped at the end of a short month, inclusive; (ii) exclusive of that date; (iii) a day count (365, 6 x 30, 4 x 365) | (i). Asserted: a leap-day receipt ends on 28 February 2029; 31 August ends on 28 February 2027; four years from 1 March 2026 is 1 March 2030 |
| F9 | `proviso-second-class-only` | s 12(a), `s 12(a) the section applies to the claimant` | src:223: the section covers one paid under s 5(a)(2)(b) "וכן" an employed person with reduced capacity "שלא משתלמת לו קצבת שאירים ... או תלויים" | (i) the proviso (no survivors' or dependants' pension) attaches to the second class only, as the sentence reads; (ii) it attaches to both classes | (i). Asserted: aged 55 or over with a survivors' pension is still within s 12(a) |
| F10 | `per-earner-capped-at-income` | s 12(a)(1), s 12A(a)(1), s 12B(a)(1) | src:224: 13% (17%) of the average wage from the income "של כל עובד או עובד עצמאי" | (i) per earner, each deduction never more than that earner's income; (ii) per earner, uncapped; (iii) one deduction for the household | (i). Asserted: earnings of 1,000 give 1,000; two earners of 5,000 give 3,400 |
| F11 | `independent-parent-slices` | s 12(a)(2)(a)-(b); s 12A(a)(2), s 12B(a)(2) | src:225-227: up to 33.81% of the average wage, 75% of the income after the paragraph (1) amount; the part above, 40% of the income | (i) slice by slice: the first slice carries the paragraph (1) amount, the second is 40% of what lies above; (ii) the whole income at one rate depending on which side of 33.81% it falls; (iii) the cut applied after paragraph (1); (iv) which paragraph (1) the first slice subtracts when the term is used in s 12A(a)(2) or s 12B(a)(2): the one in the section doing the deducting (s 12A(a)(1) or s 12B(a)(1)), or always the one in s 12(a)(1), where the term is defined "in this chapter" and sub-paragraph (a) says "the amount stated in paragraph (1)" (src:225-226, 246, 253) | (i) and, for (iv), the paragraph (1) of the section doing the deducting; for the same earnings the two readings of (iv) give different money (earnings 5,000, average wage 10,000, spouse or child: s 12A paragraph (1) amount 700 gives 2,658.35, the s 12(a)(1) amount 1,700 gives 1,908.35; the tests assert both numbers, but no case sets the two readings against each other for one family). Asserted for (i): 3,381 gives 1,260.75 and 3,382 gives 1,261.15 |
| F12 | `paragraph-2-uses-uncapped-paragraph-1` | s 12, 12A, 12B (a)(2) with (b) | src:224-229: (a)(2) is "after the amount in paragraph (1)"; (b) caps (1) and (3) together | (i) paragraph (2) is worked from the paragraph (1) amount before the (b) limit; (ii) after it | (i). No case separates the two readings: the 5,000 earner with a 3,000 pension and 200 other income (5,420) comes out the same under both |
| F13 | `c-exception-needs-both` | s 14A(c), `s 14A(c) the benefit is not paid for the month of exit and the month of return` | src:277: payment resumes if the s 2(a)(2) or (3) condition holds all month "נוסף על הוראות סעיף קטן (ב)" | (i) the exception needs both that (b) does not bar and that the condition holds all month; (ii) the condition alone suffices | (i). Asserted: the (c) test table |
| F14 | `c1-month-holds-day-73-to-100` | s 14A(c1)(2)(a), `s 14A(c1) the benefit is not paid for the month` | src:282: each month "מהיום ה־73 עד ה־100" abroad | (i) a month that contains at least one of days 73 to 100; (ii) the month of the 73rd day only; (iii) months wholly inside the range | (i). Asserted: 60 days before and 13 in the month is withheld; 12 is not |
| F15 | `heating-grant-once-a-year` | s 14B, `s 14B the heating grant` | src:296: "הזכאי לגמלה בעד אחד מהחודשים אוקטובר, נובמבר או דצמבר ... יהיה זכאי למענק חימום" | (i) one grant a calendar year; (ii) one for each of the three months | (i). Asserted: entitled for all three months gives 64 once |
| F16 | `service-on-day-15` | s 20B(b)(3), `s 20B(b)(3) the notice is deemed served` | src:333: served "בתום 15 ימים מיום שנשלחה" | (i) from the day that is 15 days after the day sent (sent 1 March, served 16 March); (ii) counting the day sent as day 1 (served 15 March) | (i). Asserted: 15 March is not covered, 16 March is served |
| F17 | `schedule-3-overlap-is-nothing` | Third Schedule, `sch 3 which row of the table applies to the household`, `sch 3 the rate of deduction for the household` | src:530-533: the rows overlap (a widow or independent parent with a child who is an individual under s 30A fits rows 1 and 3, since "יחיד" is one with no spouse, src:55; a couple with two or more children who are both under s 30A fits rows 2 and 3) and the table says nothing about which governs | (i) a household that fits two rows gets NOTHING; (ii) the first row that fits, in the order printed (the earlier encoding); (iii) the most favourable; (iv) the most specific. Also read: row 3's "ילד" is exactly one child (otherwise every couple with two or more children would fit rows 2 and 3 and row 2 could never apply) | (i), and exactly one child for row 3. Asserted: the which-row table, the rate table and two seat cases (couple with two children: row 2 gives 2,687.5, both under s 30A gives NOTHING; widow with a child: row 1 gives 2,580, an individual under s 30A gives NOTHING) |
| F18 | `sch5-threshold-on-the-change` | Fifth Schedule Part A items 1, 3, 4 | src:561, 567, 570: "קיומה או אי־קיומה ... או שינוי שחל בה, אם השינוי כאמור עולה על 9% (13%) מהסכום הבסיסי" | (i) the existence is a detail with no threshold and the threshold qualifies the change only; (ii) the threshold qualifies both | (i). Asserted: reporting the existence needs no change; a change must exceed 90 (130) of a basic amount of 1,000 |
| F19 | `2a2a-and-d2-either-route` | s 2(a)(2A) and s 2(d)(2), `s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule` | src:86: a resident to whom items (7) to (10), (14), (16), (18), (19), (23), (24) or (26) of the First Schedule apply is entitled "אף אם טרם מלאו לו 25 שנים"; src:99: a resident to whom items from (2) on apply "ושאילו מלאו לו 25 שנים היה זכאי" is entitled though under 25 | (i) either route is enough: (2A) for the listed items with no 25 test, (d)(2) with it; (ii) (d)(2) governs every item from 2 on, so the 25 test applies to the listed items too (the earlier encoding); (iii) (2A) governs the listed items and (d)(2) the rest | (i). Asserted: item 7, resident, aged 22, week 14, would not be entitled at 25 gives JUST TRUE; a listed item and each unlisted neighbour (6, 11, 15, 25) on both sides of the 25 test (`isl-tests-p2-eligibility.l4`; seat) |

Smaller choices not worth a fork: a percentage is a fraction (42.14% is 0.4214); an age is in completed years; a "month" in `s 14(c)(1)` and `s 14A` is a calendar month; "within N days" is inclusive of day N (the same trace result as `WITHIN N`); where the text says "by the Minister's regulations" the result is an input or `NOTHING`.

## Marginal readings for a lawyer

The brief asks for two readings to be taken as the status quo and listed branch by branch with the other reading stated.
Neither is a decision of mine, and no lawyer has read this.

**Reading (a): a failed "if" counts as the text's no, clause by clause.**
Where a section grants something "if", "only if", "as long as", "unless", "except", "until", "provided that" ("ובלבד ש", "אלא אם", "למעט", "כל עוד", "עד") and the case fails the condition, the function answers `JUST FALSE`, and not `NOTHING`.
The other reading: "if A then B" says nothing about "not A", so a failed condition leaves the case `NOTHING` (not covered). Flat negatives ("shall not be entitled", "is not transferable") and definitions that say "means" are the text's no under both readings and are not on this list.
Branches resting on (a) (a `FALSE-kind` branch whose quoted words introduce a condition or an exception; the tagged ones carry `lawyer reading (a)` in the comment):

*Tagged `lawyer reading (a)` in the code* (14 branches in 13 functions):

- **isl-p2-eligibility**: `s 2(a)(1) the person has no capacity to work or cannot be placed in any work`; `s 2(a)(2) the person is registered as unemployed and was offered no suitable work`; `s 2(a)(3) the person works or is in training with a low income` (2); `s 2(a)(4) the person has reached retirement age`; `s 2(a)(5)(a) the parent of a child under two is entitled`; `s 2(a)(7) the person's main time goes to caring for a sick spouse or child`; `s 2(a)(8) the person performs community service`; `s 2(a)(9) the woman stays in a shelter for battered women`; `s 2(a) the resident aged 25 or over is entitled under subsection (a)`; `s 2(b) the additional condition of 24 months of residence is met`; `s 2(e) the resident aged 20 to under 25 meets the two conditions`; `s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule` (both routes say no)
- **isl-p5-duties**: `s 20B(b)(1) the recipient is liable to a fine`

*Other `FALSE-kind` branches whose quoted words begin with a condition, proviso, exception or time limit* (32 branches in 29 functions; my classification by the Hebrew introducer, for a lawyer to confirm or move):

- **isl-p2-eligibility**: `s 2(a)(1) the finding of non-placement was made by the body the text names for the situation`; `s 2(a)(1) the person has no capacity to work or cannot be placed in any work`; `s 2(a)(5)(a) the parent of a child under two is entitled`; `s 3(4) the student is not entitled` (2); `s 3C(a) the person is not counted as a spouse for the benefit`; `s 3C(b) subsection (a) applies to the person released in an exchange`; `s 4 the spouse also meets the conditions of s 2`; `s 2 to 4 the claimant is entitled to the benefit`
- **isl-sch1-young**: `sch 1 item 1(c) the child is a child entitled to a special benefit`; `sch 1 item 1(a) the child meets the conditions`; `sch 1 item 1(b1) the benefit for a child in a relative's custody is paid for the month`; `sch 1 item 4 the person's spouse is entitled`; `sch 1 item 9 release from arrest or imprisonment`; `sch 1 item 10 illness lasting more than 30 days`
- **isl-p3-rates**: `s 5(d) the parent is treated as an independent parent`; `s 8 the benefit is not paid`
- **isl-p4-income**: `s 9(c) "property" the thing is property` (3); `s 9A(b) the claimant is not entitled because of their vehicles`; `s 9A(b1) the deduction from the benefit for the vehicle`; `s 9A(c)(2) "family member" the person is one`; `s 12A(a) the section applies to the claimant`
- **isl-p5-claims-payment**: `s 14(a) the day is within the period for which the benefit is paid`
- **isl-p5-duties**: `s 19(a) the claimant or recipient has met the Institute's demand`; `s 20 the recipient notified the change in time`; `s 21(c) the person gave the details in time`; `s 20B(b)(3) the notice is deemed served`; `s 21(a) the employee may enter by force`
- **isl-p5-misc**: `s 22 the manager is treated as responsible for the body's offence`; `s 26 the Regional Labour Court has exclusive jurisdiction`

The remaining 34 `FALSE-kind` branches are definitions that say "means", closed lists and flat negatives, which are the text's no under both readings.

**Reading (b): a prohibition or grant limited by its own wording does not say no outside the limit.**
Where a grant or a bar is limited ("without", "against", "when", a stated period, a named complement, a threshold) and the case lies outside the limit, the function answers `NOTHING`, and not `JUST FALSE`.
The other reading: outside the limit the text is read as refusing, so the case is `JUST FALSE`. The branches are every `NOTHING-kind (limited by its own wording)` comment: 159 branches in 121 functions, by function (count of branches in parentheses; `grep -n 'limited by its own wording' isl-*.l4` lists each with its line):

- **isl-p2-eligibility**: `s 2(a)(2A) the person meets one of the listed items of the First Schedule`; `s 2(a)(5)(a) the parent of a child under two is entitled` (2); `s 2(a)(5)(b) the spouses may change their choice`; `s 2(a)(9) the woman stays in a shelter for battered women` (2); `s 2(a) the resident aged 25 or over is entitled under subsection (a)` (2); `s 2(d)(1) the child who is a resident is entitled under item 1 of the First Schedule`; `s 2(d)(2) the resident is entitled under an item of the First Schedule from item 2 onward`; `s 2(a)(2A) or (d)(2) the resident is entitled under an item of the First Schedule` (2); `s 2(e) the resident aged 20 to under 25 meets the two conditions` (2); `s 3(1) the person kept in an institution at public expense is not entitled`; `s 3(2) the soldier in regular service and his wife are not entitled`; `s 3(3) the member of a body corporate responsible for its members' livelihood is not entitled`; `s 3(4) the student is not entitled` (2); `s 3(4)(b)(2) subparagraph (1) does not take away an entitlement under s 2(a)(2) or (3)`; `s 3 the person is not entitled`; `s 3A the person who refused suitable work is not entitled for the month` (2); `s 3C(a) the person is not entitled`; `s 3C(a) the person is not counted as a spouse for the benefit`; `s 3C(a) the spouse is not treated as an independent parent`; `s 3C(b) subsection (a) applies to the person released in an exchange`; `s 4 the spouse also meets the conditions of s 2`
- **isl-sch1-young**: `sch 1 item 1(a) the child meets the conditions`; `sch 1 item 1(b1) the benefit for a child in a relative's custody is paid for the month`; `sch 1 item 2 the person aged 18 or over was paid under item 1 before reaching 18`; `sch 1 item 3 the person is a parent of a child in their custody`; `sch 1 item 4 the person's spouse is entitled`; `sch 1 item 5 the woman lives with her parents who receive the benefit`; `sch 1 item 6 the woman does not live with her parents`; `sch 1 item 7 a pregnant woman aged 18 or over in or after week 13`; `sch 1 item 8 severe distress`; `sch 1 item 9 release from arrest or imprisonment` (3); `sch 1 item 10 illness lasting more than 30 days` (4); `sch 1 item 11 treatment under a probation order or supervision`; `sch 1 item 12 found not placeable by a diagnosis centre`; `sch 1 item 13 an alcoholics treatment centre`; `sch 1 item 14 incapacity to earn of 75% or more` (2); `sch 1 item 15 injury allowance`; `sch 1 item 16 imprisonment by community service`; `sch 1 item 17 sheltered workshop`; `sch 1 item 18 bail and electronic monitoring` (2); `sch 1 item 19 sleeping rough`; `sch 1 item 20 rehabilitation framework`; `sch 1 item 21 the conditions of s 2(a)(7) are met`; `sch 1 item 22 dependants' or survivors' allowance`; `sch 1 item 23 a new immigrant studying at an ulpan`; `sch 1 item 24 disability allowance as a housewife`; `sch 1 item 25(a) the child of a detained or imprisoned parent`; `sch 1 item 26 a shelter for battered women`
- **isl-p3-rates**: `s 5(e)(3) the benefit for one entitled under s 2(e)`; `s 5(f) the rate is reduced merely because maintenance was awarded`; `s 5(g) the woman is entitled to the supplement for the month` (3); `s 6(e)(1) the benefit is not paid to the person under this section`; `s 6(e)(2) subsection (d) applies to the entitled spouse`; `s 7(c) section 7 does not apply to the person`; `s 8 the benefit is not paid`; `s 30A(c) subsection (b) does not apply and s 5(a) applies`
- **isl-p4-income**: `s 9(b1)(1) the one-off payment is treated as property`; `s 9(b1)(2)(a) the instalment payment is counted as income`; `s 9(b1)(2)(b) the property the claimant is treated as having`; `s 9(c) "amount not counted" (1) the sum of money is not counted`; `s 9(c) "amount not counted" (2) the sale proceeds are not counted on the day` (4); `s 9A(b) the claimant is not entitled because of their vehicles`; `s 9A(b1) the deduction from the benefit for the vehicle`; `s 9A(c)(2) "family member" the person is one`; `s 9A(c)(2) the vehicle is needed for medical treatment` (2); `s 9A(c)(3) the person disabled in the legs`; `s 9A(c)(3A) the driving licensee of a disabled person`; `s 9A(c)(4) a pension is paid for the claimant's child`; `s 9A(c)(5)(a) the claimant is ill and the licence is deposited` (3); `s 9A(c)(5)(b) the tractor of an inactive farm`; `s 10 the receipt is not counted as income`; `s 11 the income of a person with a spouse`; `s 12(a) the section applies to the claimant`; `s 12 the income after the deductions`; `s 12A(a) the section applies to the claimant`; `s 12A the income after the deductions`; `s 12B(a) the section applies to the claimant`; `s 12B the income after the deductions`
- **isl-p5-claims-payment**: `s 14(c)(1) the benefit is paid for a month before the month of the claim` (2); `s 14(c)(2) the person paid under paragraph (1) is entitled to the privilege`; `s 14A(a) the benefit is not paid for the month` (2); `s 14A(b) the benefit is not paid for the month of exit and the month of return` (3); `s 14A(c) the benefit is not paid for the month of exit and the month of return` (4); `s 14A(c1) the benefit is not paid for the month` (2); `s 14A(d) subsections (a), (b) and (c1) do not apply to the person` (2); `s 14A(e) the benefit paid to the spouse in Israel`; `s 14A(f)(2) paragraph (1) does not apply to the person`; `s 14A(f)(1) the entitled person is treated as outside Israel`; `s 14A(f)(1) the spouse is treated as an individual`; `s 14B the heating grant`; `s 15(a) who is paid the death grant`; `s 15(b) how many of the two grants the person may receive`; `s 17(a) the Institute may claim compensation from the person`; `s 17(c) the District Court may hear the claim`; `s 17(c) the religious court may also hear the claim`; `s 18 the Institute may reduce, suspend or revoke the benefit`
- **isl-p5-duties**: `s 17(b) the recipient is in breach of the duty`; `s 19(a) the claimant or recipient has met the Institute's demand`; `s 19(b) the Institute may delay the claim, stop payment or refuse the benefit`; `s 20 the recipient notified the change in time` (2); `s 21(c) the person gave the details in time` (2); `s 20A the provisions of s 327 of the Insurance Law apply to the person`; `s 20B(a) the claimant is liable to a fine`; `s 20B(b)(3) the notice is deemed served` (2); `s 20B(b)(4) paragraph (1) applies to the recipient all the same`; `s 20B(b)(5) subsection (b) does not apply to the recipient`; `s 20B(b)(1) the recipient is liable to a fine` (4); `s 21(a) the employee may enter the place`; `s 21(a) the employee may enter by force` (2); `s 21A(1) the Institute may use the information`; `s 21A(2) the provisions of s 326(g) of the Insurance Law apply`; `sch 5 part A item 1 the account balance must be reported`; `sch 5 part A item 3 the income from work must be reported`; `sch 5 part A item 4 the income from other sources must be reported`
- **isl-p5-misc**: `s 22 the manager is treated as responsible for the body's offence`; `s 23(a) the section of the Insurance Law applies to this Law`; `s 23(b) the benefit may be transferred, pledged or attached`; `s 24(c) the provisions of sub-chapter C apply to the matter`; `s 25(b) the State Treasury transfers the money for the month`; `s 26 the Regional Labour Court has exclusive jurisdiction`; `s 30(b) the benefit paid, not less than the last support`

**One inference worth a lawyer's eye on its own.** In s 2(a)(5)(a), "the entitlement under this paragraph is the mother's" unless the spouses chose the other parent; the encoding reads the choice of the other parent as taking the entitlement away from the mother (`JUST FALSE`), an inference from the allocation (tagged `marginal reading` in `isl-p2-eligibility.l4`). The other reading: both parents could hold it, and the text is silent.

### Reading a result: FALSE and NOTHING

In this subject a **no** (`JUST FALSE`) is the Law's own no: a definition that says "means" (a "child" is one of two limbs and nothing else), a closed list ("each of these"), a flat negative ("shall not be entitled", "a benefit is not transferable or attachable"), or a condition the Law introduces that the case fails ("as long as", "except", "until", "provided that"; see the marginal readings).
Example: a woman who is not staying in an approved shelter for battered women at all is `JUST FALSE` for s 2(a)(9); one who has stayed 30 days or fewer is `NOTHING`, because "more than 30 days" is a stated period she has not yet passed.

**Not covered** (`NOTHING`) means the Law, as the sources give it, does not answer. It is never a no, and no caller may turn it into one.
The reasons, as written on each branch: *silent* (the Law has no rule for the case), *list not closed*, *includes* (the definition says "including"), *undefined term*, *points outside the text* (the answer lies in a regulation, the Minister's order, or the Insurance Law, none of which is in the sources), and *limited by its own wording* (a grant or bar with a limit, and the case lies outside it).
Examples: a woman aged 24 who meets no ground in s 2(a) is `NOTHING` for s 2(a) (s 2(e) may reach her); the amount for a person whose income is above the allowance is `NOTHING` (s 5(b) is silent); whether an overpaid benefit is repaid is `NOTHING` (the Law points at s 327 of the Insurance Law).
A `JUST TRUE` is a yes only for the question's own wording: "Is my allowance withheld ..." answers `JUST TRUE` when the Law withholds it.

### Same words, different kind

Three places where the same wording is answered differently, each decided by the rule of 2026-10-29 (the brief's "What FALSE and NOTHING mean"): a condition introduced by "if", "as long as" or "provided that", or a definition that says "means", is the text's no under reading (a); a grant or bar limited by a stated period, a stated number or a named complement, with the case outside the limit, is not a no under reading (b).
Both readings are marginal readings for a lawyer; none of this is a ruling.

1. **s 2(a)(9) and First Schedule item 26** ("a woman staying in a shelter for battered women, with the approval of the social services department or the Ministry, for a period exceeding 30 days"; src:95 and src:499).
   A stay of 30 days or fewer is `NOTHING` in both: "a period exceeding 30 days" is a stated period she has not yet passed, so the rule makes it reading (b).
   The earlier encoding answered `JUST FALSE` for s 2(a)(9) there; that was a change forced by the rule, and the assertions are changed (`isl-tests-p2-eligibility.l4`, seat case).
   No approved stay in a shelter at all stays `JUST FALSE` for s 2(a)(9) and `NOTHING` for item 26.
   The text-based reason: s 2(a)(9) is a limb of the list that s 2(a)'s lead-in introduces with "as long as one of these conditions holds" ("כל עוד מתקיים בו אחד מתנאים אלה"), so a limb that fails is the text's no under reading (a); item 26 is a class description in a Schedule that s 2(a)(2A) and s 2(d)(2) refer to ("the conditions fixed for him in the Schedule"), and every item of the First Schedule answers `NOTHING` outside its class unless a proviso says no.
   The alternative (making item 26 answer `JUST FALSE` here, or s 2(a)(9) `NOTHING` here) is open to a lawyer; the first would break the Schedule's pattern in one item.
   How `s 2(a)` resolves it: `s 2(a)` says "no" only when every limb says no, so a woman at day 20 of a stay whose other limbs all fail now gets `NOTHING` from `s 2(a)`, not a no.
   That is the right answer under reading (b): she may pass day 30, and nothing in the text says she is not entitled.
   A person who is not a woman, or who stays in no approved shelter, still reaches the `s 2(a)` no through the other limbs only if the caller supplies `JUST FALSE` for (9); the seat question for (9) does.
2. **First Schedule item 10** ("30 days or fewer of illness" is `NOTHING`; "a payment at least equal to the benefit" is `JUST FALSE`; src:447).
   The two are different words: the payment limb is a proviso ("ובלבד שאם הוא זכאי לתשלום ממקור כלשהו ... יהיה זכאי לגמלה אם התשלום נמוך"), which the rule lists among the words that say no; the age of 18, the illness lasting more than 30 days, the 6 months and the inability to work because of an illness are a stated age, a stated period and a named complement, which the rule lists among the words that do not.
   No change; the reason is written in the code comment.
3. **s 9A(c)(2)** (the closed "family member" definition is `JUST FALSE` for a non-member; the thresholds "more than 90 consecutive days" and "at least 6 times a month" are `NOTHING`; src:203).
   The definition is a "means" definition with a closed list and a proviso ("ובלבד"), which the rule lists among the words that say no; the two thresholds are a stated period and a stated number limiting the exception in its own wording.
   No change; the reason is written in the code comment.

## Findings: what the text turns out to say

Each finding ends "Asserted." where a case asserts it; the file is named.

1. **The Law has no repayment provision.** Section 20A makes s 327 of the Insurance Law apply to one who claims or receives a benefit; s 23(a) lists nineteen Insurance Law sections that apply, and s 327 is not among them. The question "what can I be made to repay" has `NOTHING` as its answer beyond "s 327 applies". Asserted (`isl-cases-seat.l4`, the repayment group; `isl-tests-p5-duties.l4`, s 20A).
2. **The s 23(a) list has nineteen entries.** "302" and "302(a)(2)" are not on it though "302(a)(1)" and "302(b)" are; "305" is not on it though "304" and "307" are. Asserted (`isl-tests-p5-misc.l4`).
3. **First Schedule items 5 and 6 leave a gap.** A pregnant woman who lives with her parents when they do not receive the benefit is in neither item 5 (parents receive it) nor item 6 (does not live with her parents). Asserted (`isl-tests-sch1-young.l4`).
4. **Third Schedule row 1 names independent parents, but s 12A(a)(2) sends an independent parent to the separate deduction of s 12(a)(2)(a)-(b).** So in practice row 1's 40% reaches only a widow who is not an independent parent. The rate is ignored for an independent parent even when supplied. Asserted (`isl-tests-p4-income.l4`, `s 12A(a)(2)`).
5. **The rows of the Second Schedule overlap for a widow with a child (rows 5 and 7, or 6 and 8).** An independent parent is sent to rows 7 and 8 by s 5(a)(3) in its own words (src:137), so that pick has text behind it. A widow who is not an independent parent fits row 5 ("יחיד שעמו ילד", and "יחיד" is one with no spouse, src:55) and row 7, nothing orders them, and she now gets `NOTHING` for the row and for the benefit (F4; the earlier encoding gave her row 7 quietly). `Household` has two fields, `the claimant is a widow` and `the claimant is an independent parent`, so the two can be told apart; a widow who is also an independent parent is an independent parent. The Fourth Schedule takes the Second Schedule's row and so carries the same answer. Asserted (`isl-tests-p3-rates.l4`; seat cases for s 5(a) and s 30A(b)). Noticed and left, for a ruling: a household with a spouse takes rows 2 to 4 first, even where s 5(d) treats a parent who still has a spouse as an independent parent and s 5(a)(3) would send them to rows 7 and 8; no assertion covers that household. Swept and found without this problem: the age bands of s 5(a)(1) (under 70, 70 to under 80, 80 and over) and the columns of s 5(a)(2) (under 55, 55 and over), which partition; the Fifth Schedule items, which are separate details and not rows to choose between.
6. **The independent parent's deduction is sliced at 33.81% of the average wage.** The first slice carries the paragraph (1) amount; the boundary case is 3,381 giving 1,260.75 and 3,382 giving 1,261.15. Asserted (`isl-tests-p4-income.l4`).
7. **Income above the allowance is not covered.** Section 5(b) says the allowance is the difference; for income above the allowance it says nothing, so the result is `NOTHING`, not zero. Asserted (`isl-tests-p3-rates.l4`; seat case).
8. **A man in a shelter for battered women is not covered.** Section 2(a)(9) says "she". Asserted (`isl-tests-p2-eligibility.l4`).
9. **The s 5(g) supplement lists birth years 1960 to 1964 only.** 1959 and 1965 are `NOTHING`; the lengths are 4, 8, 12, 15 and 18 months. Asserted (`isl-tests-p3-rates.l4`).
10. **Six shekels is not "under six".** A benefit of 5.99 is withheld (`JUST TRUE`), 6 is not covered, and a pensioner is never withheld. Asserted (`isl-tests-p3-rates.l4`; seat).
11. **Payment starts on the first of the claim's month.** An earlier day is covered only by a regulation of the Minister, which is not in the sources: `NOTHING`. Asserted (`isl-tests-p5-claims-payment.l4`; seat).
12. **Section 14A stacks three bars and two exceptions.** Month wholly abroad (a); month of exit and return (b); day-counts for a retirement-age couple (c1: exactly four exits uses neither day-count paragraph, day 72 is not caught, day 73 is, more than 100 days catches every month); the s 2(a)(2) and (3) trainee exception (c); medical need abroad (d). The day-count boundaries are tested on both sides. Asserted (`isl-tests-p5-claims-payment.l4`).
13. **A fine for not reporting needs more than s 20's duty.** Section 20 requires a written notice within 60 days; the fine of s 20B(b)(1) needs a registered notice from the Institute and a change within four years of it. A change one day outside the four years is not covered. Asserted (`isl-tests-p5-duties.l4`).
14. **A registered notice is deemed served 15 days after the day sent, unless the addressee proves non-receipt.** Day 15 is not covered, day 16 is `JUST TRUE`, and a proved non-receipt is `JUST FALSE` (F16). Asserted (`isl-tests-p5-duties.l4`).
15. **Section 23(b) overrides s 303(a) of the Insurance Law:** a benefit cannot be transferred, pledged or attached, not even for maintenance owed. Asserted (`isl-tests-p5-misc.l4`).
16. **The s 30(b) floor works only when the Law's income rules are the only reason the amount is lower.** An allowance equal to the last support is not covered (there is nothing to lift). Asserted (`isl-tests-p5-misc.l4`).
17. **The vehicle exceptions of s 9A(c) are a closed list;** none holding means s 9A(b) applies, which the composite function answers with a plain `FALSE` (a BOOLEAN, for a caller that asks "does an exception hold"). Asserted (`isl-tests-p4-income.l4`; seat).
18. **A sum received for the sale of a home on a leap day (29 February 2028) is still left out of property on 28 February 2029, which is the last day it is left out; from 1 March 2029 the exclusion no longer applies.** The twelve-month period is read as the same date later, clamped at the end of a short month (F8). Asserted (`isl-tests-p4-income.l4`): the function answers JUST TRUE on 28 February 2029 and NOTHING on 1 March 2029.
19. **The Law states a basic amount of 6,964 new shekels and how it is updated each 1 January from 2007;** the current figure, and the Wikisource editor's note of 10,382 for 2026, are not the Law's and the encoding takes the current figure as an input. Asserted for the 6,964 and the update formula (`isl-tests-s01.l4`).
20. **The student bar of s 3(4) has exits and a clock.** A student paid as a person of retirement age is outside it; an independent parent is outside it if paid for 16 of the 20 months before the studies began (15 is not enough) and not studying for a second or third degree; the exit lasts while at most 36 months have been paid (35 paid still leaves it open, 36 closes it unless the Minister set a longer period). Asserted (`isl-tests-p2-eligibility.l4`).
21. **Item 7 (a pregnant woman) is reached by two routes, and the first needs no "would be entitled at 25" test.** Section 2(a)(2A) lists items 7 to 10, 14, 16, 18, 19, 23, 24 and 26 of the First Schedule as entitling a resident "אף אם טרם מלאו לו 25 שנים"; s 2(d)(2) reaches the same items but adds "had they been 25 they would have been entitled". The earlier seat question took only the (d)(2) route, so a resident aged 22 in week 14 who would not be entitled at 25 got `NOTHING`; she is now `JUST TRUE`. F19. Asserted (`isl-tests-p2-eligibility.l4`, `s 2(a)(2A) or (d)(2) ...`; `isl-cases-seat.l4`, the pregnancy group).
22. **A household can fit two rows of the Third Schedule and the table does not choose.** A widow or independent parent with a child who is an individual under s 30A fits rows 1 (40%) and 3 (32.5%); a couple with two or more children who are both under s 30A fits rows 2 (37.5%) and 3. The earlier encoding silently took the first row printed (and so gave 37.5% to the couple); the row function now answers `NOTHING` and so does the rate. F17. Asserted (`isl-tests-p4-income.l4`; two seat cases).

## What the stable binary does not accept

The binary is `l4` 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
Each of these was met while building this encoding, and the binary governs over the skills where they differ.
**Loud failures** (a parse or type error; the file will not run):
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` outside `LEST BREACH ... BECAUSE` do not exist; "not covered" is `NOTHING`, asserted. None is used.
- `` `WAIT UNTIL` `` is not defined: the trace waits with `(WAITUNTIL n)`.
- `length` does not exist; `count` does.
- `ELSE IF` after `THEN NOTHING` is an indentation error; the encoding uses `BRANCH`.
- A positional record needs commas: `Figures OF a, b, c, d`, not `Figures OF a b c d`.
- A `GIVEN` with a `LIST OF` parameter followed by a comma and another parameter gives "unexpected IS": one parameter per line.
- A list of calls needs commas between its elements: `LIST (f x) (g y)` fails with "unexpected (", `LIST f x, g y` does not. The seat's s 9A(c) and the s 12 question use names in a `WHERE` to avoid the issue.
- A `§` heading followed by a parenthetical gloss is a parse error; the gloss is a comment.
- `(IF c THEN f x y ELSE NOTHING)` written as a parenthesised argument of `helper either` on the next line gives "unexpected (" (met in `s 2(a)(2A) or (d)(2) ...`); the two arguments are named in a `WHERE`.

**Silent failures** (the file runs and gives a wrong or odd answer; the ones that cost the most):
- **`IF NOT x AND y` parses as `NOT (x AND y)`.** Found by a test of `isl-p3-rates` before it was fixed; every `NOT` in the nine modules is now parenthesised (`(NOT x) AND y`).
- **`JUST 42.14%` parses as `(JUST 42.14)%`.** Every percentage inside a `JUST` is written `JUST (42.14%)`, including in the generated Second, Third and Fourth Schedule tables.
- **A trace prints but cannot be asserted.** `#TRACE` prints `FULFILLED`, `DEONTIC BREACHED` or the residual obligation, and produces no assertion line, so `check.sh` counts nothing for it and a changed trace outcome moves no count. The ten `#TRACE` runs of `isl-tests-p5-duties.l4` have the expected result in a comment above each, were read on the stable and the main build and were equal; the asserted copies are the decision-function twins.
- **A `SHANT` with no `WITHIN` prints a breach with a deadline message that reads oddly** ("surpassed the deadline ... which was at 5"): the act is simply forbidden and the text gives no deadline. The `s 17(b)` "shall not harm" limb is written without one, and its trace is read for the word `BREACHED` only.
- **`Date d m y` rolls forward** (`Date 31 2 2026` is 3 March 2026; checked), so an anniversary is computed with `add months` / `add years`, which clamp; every period in the Law that ends "on the same date later" uses them (F8).
- **A deadline day is inclusive** in `WITHIN n`: an act at day `n` is in time. The decision-function twins say `AT MOST` for the same reason.

## What check.sh prints

Target `main`. Command: `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` (`JL4_LIBRARY_PATH` unset), run in this folder on 2026-11-04. A fresh encoding: no earlier run to replace.
Your l4: 1.6.98 (main, 7689b0d, 2026-10-19). The main build it compared with: 1.6.108 (main, 2ae7c9b, 2026-11-02).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
isl-cases-seat.l4                              0       404       0        0         0 |      0       404       0        0  same
isl-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
isl-p2-eligibility.l4                          0         0       0        0         0 |      0         0       0        0  same
isl-p3-rates.l4                                0         0       0        0         0 |      0         0       0        0  same
isl-p4-income.l4                               0         0       0        0         0 |      0         0       0        0  same
isl-p5-claims-payment.l4                       0         0       0        0         0 |      0         0       0        0  same
isl-p5-duties.l4                               0         0       0        0         0 |      0         0       0        0  same
isl-p5-misc.l4                                 0         0       0        0         0 |      0         0       0        0  same
isl-s01-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
isl-sch1-young.l4                              0         0       0        0         0 |      0         0       0        0  same
isl-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
isl-tests-p2-eligibility.l4                    0       188       0        0         0 |      0       188       0        0  same
isl-tests-p3-rates.l4                          0       217       0        0         0 |      0       217       0        0  same
isl-tests-p4-income.l4                         0       238       0        0         0 |      0       238       0        0  same
isl-tests-p5-claims-payment.l4                 0       116       0        0         0 |      0       116       0        0  same
isl-tests-p5-duties.l4                         0       115       0        0         0 |      0       115       0        0  same
isl-tests-p5-misc.l4                           0        48       0        0         0 |      0        48       0        0  same
isl-tests-s01.l4                               0        63       0        0         0 |      0        63       0        0  same
isl-tests-sch1-young.l4                        0       145       0        0         0 |      0       145       0        0  same
TOTAL (19 modules)                             0      1534       0        0           |      0      1534       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Read: no error on any of the nineteen modules, 1,534 assertions satisfied, none failed, none refused, and every module has the same four counts on the main build.
Seat cases: 404 satisfied of 404 written (`grep -c '^#ASSERT' isl-cases-seat.l4` is 404).
The tests are written equal to satisfied for every file: 63 + 188 + 217 + 238 + 116 + 115 + 48 + 145 = 1,130 in the eight layer-1 test files, 404 in the seat cases. `expected_failed` in `check.sh` is zero for every file: no assertion is meant to fail.
A positive control: a copy of three seat cases with two expected values altered fails two and satisfies one (so an assertion that does not match does fail on this binary); the copy was deleted. In the second pass a copy of three new assertions with wrong expected values (the pregnancy case at 22, the couple under s 30A, the 30-day stay) failed all three and satisfied none; the copy was deleted. In the third pass a copy of three Second Schedule expectations written the old way (a widow alone in row 7, an independent parent not covered, the widow's benefit 4,050) failed all three and satisfied none; the copy was deleted.
`check.sh` does not see a `#TRACE` outcome; the ten traces were compared by hand (the two builds' outputs for `isl-tests-p5-duties.l4` are equal except for the diagnostic `Code:` label).

Other checks:
- `python3 -I srcrefs.py check --refs <raw text> isl-*.l4`: srcrefs check: 365 src: lines, 212 runs, 226 locators, 0 problems
- `python3 -I srcrefs.py check --strict <raw text> isl-*.l4`: srcrefs check: 365 src: lines, 212 runs, 226 locators, 0 problems
- `python3 -I isl-coverage.py <raw text> check`: units (rows): 456 / non-blank lines: 509; covered: 509; in more than one row: 0 / dispositions: encoded=307, fork=46, inert1=69, inert2=20, repealed=14 / 0 problems

## What would need doing before the encoding is worth relying on

1. **A domain expert** (an Israeli social-security lawyer, or an adviser at the Institute) has to read this against the Hebrew; nobody has. The English is a gloss and may mistranslate a term of art.
2. **The official text.** The source is an unofficial consolidation (Hebrew Wikisource, revision 3073779). The official version is the Reshumot publication plus each amending Act; a point-in-time question needs the commencement and amendment history. Compare section by section before any reliance.
3. **The regulations and the Insurance Law are not in the sources.** Every rule that points to them returns `NOTHING` or takes an input: the Minister's regulations, the determining amount, the vehicle deduction, the Ministers' tests for ages 20 to 25, the Supervision, Arrests, Penal, Minimum Wage and Single-Parent Families Assistance Laws, and the Insurance Law (including s 327, ss 303(a) and 326). The repayment question cannot be answered until s 327 is encoded.
4. **A lawyer's decision on the marginal readings** (a) and (b) and the nineteen forks (F1 to F19), above all F4, F9 to F12, F13, F17 and F19, which change money amounts, whether a month is paid or whether a person is entitled.
5. **Current figures.** The basic amount, the average wage, the child basic amount, the pension point and the updated vehicle limits change each year; they are inputs, and the seat asks for them with a pointer to where the Institute publishes them. No figure in this encoding is from memory.
6. **A test with real users** of the seat's wording: the inputs a person cannot answer unaided (`I would be entitled if I were 25`, `one of the grounds in s 2(a) applies to me`) should be replaced by questions the person can answer, which needs the earlier grounds to be asked in the same flow.
7. **The Hebrew quotes** are checked against the file by `srcrefs.py` (`--refs` and `--strict`, 0 problems each), not against the Knesset's database; a wiki edit after revision 3073779 would not show.
8. **A comparison of the traces and the cases on a future main build.** `check.sh` does not see a different `#TRACE` outcome.

## Source not official

Nothing here is "verified against the official text". The quoted Hebrew is the Wikisource consolidation as the file prints it, including its wiki markup; `SOURCE-LICENSE.md` records the terms (no copyright in Israeli statutes; the working text is not an official version).

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `isl-coverage-map.tsv`, `isl-coverage.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated or checked a module, the module in this folder is the file to edit.
The commands in this file that run one of them (`python3 -I coverage.py ...` and the like) cannot be run from this folder; `check.sh` and `srcrefs.py` can.
The lead keeps the scripts outside this repository.

## Independent test pass

A separate agent that had not seen this encoding's `NOTES.md`, `PROGRESS.md`, brief or tests wrote `ANSWERS.md` from the Hebrew text alone before it opened any `.l4` file: 365 numbered scenarios and 99 seat questions.
It then wrote `tests-independent.l4`: 610 assertions, covering 319 of the 365 numbered scenarios and 96 of the 99 seat questions, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the numbers in square brackets in the comments of `tests-independent.l4` refer to it.
The author's rule for "no" and "not covered" is at the head of its `ANSWERS.md`: it counts an "if", "only if", "as long as" or "provided that" condition, a "means" definition, a closed list and an express prohibition as the text's no, and in practice it also wrote `JUST FALSE` for a case outside a stated "more than", "at least", period or age (the groups A and B below), which is wider than the family's rule (see "Reading a result: FALSE and NOTHING" above).

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against the modules as first deposited | 610 | 517 | 93 | 0 |
| after the encoder's repairs below, with the author's calls adapted to the repaired signatures, before the reconciliation | 610 | 518 | 92 | 0 |
| after the reconciliation below | 610 | 610 | 0 | 0 |

**What the 93 first-run failures turned out to be.**

- **Two were encoder defects, repaired; the author's assertions stand unchanged (the seat question about pregnancy, S15b, and Third Schedule rows 2 and 3, 154b).**
  Item 7 of the First Schedule is listed in s 2(a)(2A), which gives entitlement "even if not yet 25" with no "would be entitled at 25" test, but the seat reached it only through s 2(d)(2), which has that test; a pregnant woman aged 22 got `NOTHING` where the text gives her the allowance.
  The encoder added a function that takes either route (fork F19) and swept the other seat questions and functions for the same shape: nothing else changed.
  A couple with two or more children, both former recipients under s 30A, fits rows 2 and 3 of the Third Schedule, and the text gives no priority; the row function took row 2 without saying so.
  It now answers `NOTHING` where more than one row fits (fork F17).
  The sweep found the same overlap for rows 1 and 3 (a widow or independent parent with a child who is an individual under s 30A), and a third in the Second and Fourth Schedules: a widow with a child fits rows 5 and 7, and nothing orders them.
  The `Household` record had one field for "widow or independent parent", so it now has two, a widow alone with a child gets `NOTHING`, and an independent parent keeps the rows 7 and 8 that s 5(a)(3) names (fork F4).
- **The encoder was also asked to look at three places where identical wording got a different answer (the author's finding).**
  s 2(a)(9) ("תקופה העולה על 30 ימים") answered `JUST FALSE` for a stay of 30 days or fewer, while the identical clause in First Schedule item 26 answered `NOTHING`; the encoder moved s 2(a)(9) to `NOTHING`, because a stay of a stated period she has not yet passed is a limit in the text's own wording.
  That change made the author's assertion 67b fail, and it is reconciled with the others below.
  A difference remains and is marked for a lawyer: with no approved stay at all, s 2(a)(9) answers `JUST FALSE` (it is a limb of the list that s 2(a) introduces with "כל עוד מתקיים בו אחד מתנאים אלה"), and item 26 answers `NOTHING` (a class description in a Schedule).
  The other two pairs (inside First Schedule item 10, and inside s 9A(c)(2)) were left as they were, with the reason written in the code and in NOTES: a proviso and a "means" definition say no, a stated age, period or number does not.
- **Six of the encoder's own expected values changed with these repairs.**
  The seat case for a pregnant woman with a "would be entitled at 25" answer of false went from `NOTHING` to `JUST TRUE`.
  The s 5(a) seat case for a widow aged 60 with one child went from `JUST 4050` to `NOTHING` (the cases for an independent parent keep `JUST 4050`).
  The Third Schedule row for a widow or independent parent with an individual child under s 30A went from row 1 to `NOTHING`, and for a couple with two children, both under s 30A, from row 2 to `NOTHING`.
  s 2(a)(9) at 30 days went from `JUST FALSE` to `NOTHING`, in `isl-tests-p2-eligibility.l4` and in `isl-cases-seat.l4`.
  The ten `sch 2 which row` and twelve `sch 3 which row` assertions only changed `EQUALS n` to `EQUALS JUST n`, because the functions now return a `MAYBE NUMBER`.
- **Five were genuine forks, reconciled to the encoding's answer (24, 180c, 95, 81 and S12).**
  24 and 180c: months counted from a day a short month lacks (a start on 29 February); the encoding's fork `period-ends-on-anniversary` picks an anniversary day, and the author, who could not decide it from the text, expected "not covered".
  95: whether the student exclusion bites again after the 36-month cap, given the Minister's power to extend, which is outside the text.
  81 and S12: the author read s 2(e) as only telling the Ministers to make rules; the encoding reads it as giving entitlement to one who meets its two conditions, because s 5(e)(3) speaks of "one entitled under s 2(e)".
  **Which reading is right is for a lawyer.**
- **Seven were the author's own scenarios, reconciled with the reason in the file (2, 80, 126b, 189b, 199b, 283b and 301).**
  The author conceded six of them: an ordinary widow without a pension is a widow (2); "this route is closed" does not mean "not entitled" (80); s 5(b) is silent on income above the benefit (126b); s 11 is silent about a single person (199b); "אלא על פי צו" makes a magistrate's order necessary, not sufficient (283b); s 30(b) is silent outside the floor case (301).
  189b (a sister, "אחיו") it held weakly: masculine drafting covers a woman in ordinary Hebrew drafting, and the encoding answers `JUST TRUE`.
- **Eighty were one convention disagreement, reconciled to the encoding's `NOTHING` (the author's groups A and B, 44 and 33 assertions, with 58, S07b and 67b).**
  Where a rule is limited by a stated period, number, age, class or trigger in its own wording and the case lies outside the limit (a child of exactly 2, a stay of exactly 30 days, a change of exactly 9%, a change of choice after 3 months, a reserve soldier where the text says regular service), the author wrote `JUST FALSE`; the encoding tags the branch "NOTHING-kind (limited by its own wording)" and answers not covered.
  The author's own view of the 33 in its group B (an exclusion, bar, power or class whose trigger is unmet) was that `NOTHING` is defensible under the family's convention; of the 44 in group A, that the provision's own sentence states an "if", "more than", "at least" or closed-list condition and it is unmet.
  Each reconciled assertion carries a `-- RECONCILED` comment quoting what the author wrote.
  **These are the first thing for a lawyer to look at, together with the five forks above:** if a stated-limit wording does close a case, the encoding says "the Law does not say" in 80 places where a reader would say "no".
  This is the second of the two readings that the 2026-10-29 rule leaves for a lawyer (a prohibition or grant limited by its own wording is not counted as the text's no); no ruling has been made.

**The lead adapted the author's file to the repaired signatures; no expected value was touched.**
The author's first file calls three things the repairs changed: the `Household` record (two fields in place of one), the `which row` functions (a `MAYBE NUMBER` in place of a `NUMBER`), and two seat questions (one more input each).
The lead changed 45 lines so that the file type-checks: nine `Household` fixtures (the author's "widow" fixtures are its independent-parent cases and became "independent parent" with "widow" false), five `which row` assertions (`EQUALS n` to `EQUALS JUST n`), two assertions on the rate (they now call `sch 3 the rate of deduction for the household`), and two seat calls (S23 and S63, one more `FALSE`).
Before this change the file produced 27 type errors and evaluated nothing.

**The gaps.**
46 of the 365 numbered scenarios have no assertion, and so have 3 of the 99 seat questions; each is kept as a `-- GAP` line at the end of the file with the author's reason, and one more (186, the figure of 9,691) is kept as a partial gap.
By the author's grouping: the encoding takes counts of months or days and not dates, so it has no anniversary-day, last-day or rest-day function (74, 265, 266, 267, 287, 335); no input for "A is not entitled for another reason" (144); a duty that is a `DEONTIC`, so there is no boolean to assert on (263); content in other statutes or index data, taken as input by design (17, 18, 31, 34, 35); repealed provisions, regulation powers, commencement and savings, which the encoding marks inert (100, 198, 222, 293, 298, 299, 302 to 310); silences with no section to call (311 to 314); and string-valued answers where no literal can be asserted without copying the encoding's own (8, 9, 221, 364, 365 and the seat questions about where to submit a claim, the warning a notice about the Fifth Schedule must carry, and who pays).
Seven scenarios are covered by another assertion (97, 130, 137, 162, 179, 360, 361), 88 has the same inputs as 87, and 16 was dropped by the author as contradictory.

**What the author could not decide from the text** (for comparison with the fork register above):
months counted from a day a short month lacks;
whether s 2(a)(2A) (items 7 to 10, 14, 16, 18, 19, 23, 24 and 26, with no age-25 test) or s 2(d)(2) (item 2 onward, with the test) governs where they overlap;
Third Schedule rows 2 and 3 for a couple with two or more children, both under s 30A;
whether s 2(e) grants entitlement or only tells the Ministers to make rules;
a negative difference in s 5(b);
whether the student exclusion bites again after the 36-month cap given the Minister's power to extend;
whether "אלא על פי צו" in s 21(a) is sufficient as well as necessary;
whether "אחיו" covers a sister;
and whether s 3(2), "אדם … ואשתו", reaches the husband of a female soldier.

**Left open by the encoder, for a lawyer.**
A household with a spouse takes the Second Schedule rows 2 to 4 first, even where s 5(d) treats a parent who still has a spouse as an independent parent and s 5(a)(3) would send them to rows 7 and 8.
This was noticed and not asserted (finding 5 above).

**Independence, as far as it went.**
The author did not open `NOTES.md` or `PROGRESS.md`, any other encoding, anything under `~/.claude/`, or any other run's directory.
It read the modules' signatures and bodies, and ran probes and `#EVAL` sweeps, only after `ANSWERS.md` was written; it edited `ANSWERS.md` once afterwards, in the wording of scenario 231, and the expected value in the assertion is the one in `ANSWERS.md` today.
The encoder was given the author's findings 154b and S15b and the three pairs of identical wording (and not the convention disagreement or the other failures), repaired or answered them, and reran everything.
