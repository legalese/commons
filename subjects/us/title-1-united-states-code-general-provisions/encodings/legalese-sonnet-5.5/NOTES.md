# NOTES: Title 1 of the United States Code (General Provisions), row legalese-sonnet-5.5

STATUS: draft. No domain expert has read this encoding against the statute.
The row is the work of one Sonnet 5.5 agent working alone from the brief in `BRIEF.md`.
Written 2026-10-21 against release point Public Law 119-121.

**Target compiler: `unstable`.**
The brief requires `REFUSE`, `#ASSERT REFUSED`, `YMD` and `@lang en`, which `main` rejects; so `check.sh` was run with `L4_TARGET=unstable`, and the main step was skipped (the script says so).
The `l4` binary has no `--version` flag; it is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`.
`JL4_LIBRARY_PATH` was left unset throughout.

**The source text is a plain-text rendering, not the official text.**
`../../registers/source-bundle/usc01.txt` was made from the Office of the Law Revision Counsel's USLM XML (release point Public Law 119-121) by a converter script and is not marked up; sha256 `e7ba0ac7ff7aef5b7b5bf866205950f32762a37f0fc904b550473bedb9f6f085`, as `../../registers/source-bundle/usc01.meta.json` records.
Nothing here is verified against the official text.
Every `-- src:N | ...` line in the modules is a verbatim slice of line N of that file, and `srcrefs.py check --strict` checks it (result in section 5).

## 1. What is encoded and what is not

### The finding that shapes the row

Title 1 has no rule on any of the following, and the six must-encode time items are therefore named refusals rather than computations:

- how a period of days, weeks, months or years is counted from a day or after an event;
- what happens when the last day of a period is a day of rest, recess or holiday;
- when an Act or an instrument comes into force or begins to bind, or from what moment of that day;
- when a document is treated as served or a notice as given;
- what "day", "week", "month", "year", "calendar year", "session" or "forthwith" mean.

How this was established: the text was searched for `holiday`, `Sunday`, `Saturday`, `recess`, `hour` (no line at all), and for `deemed`, `commence`, `effective`, `in force`, `takes effect`, `serve`, `notice`, `forthwith`, `calendar year`, `session`, `repeal`, `revive`, `reenact` (every hit was read).
`deemed` is s 5 (successors and assigns), not service; `notice` is s 106b (official notice of an amendment), not a notice to a party; `commence` is s 110 ("may be commenced") and s 204 (the commencement of a session); `in force` is ss 109, 111 and 204 and none of them says when anything comes into force; `reenact` is s 203 (bills to codify and reenact the District of Columbia laws), not a rule on repeal and re-enactment; `serve` is "preserve", "serve concurrently" and "who serves at the Department of State".
Title 1 does state a few periods in its own operative sections: s 106 (the last six days of a session), s 204 (the day preceding the commencement of a session), s 112b and s 202(c) ("N days after", "N years after").
Those are read in the ordinary sense, in Part B of `us-interpretation-time.l4`, and every one of them is a labelled fork (F-after).

### The modules

| file | what it holds |
| --- | --- |
| `us-nouns.l4` | DECLARE only: the facts a witness could testify to (a kind of body, a subdivision, a contrivance, a place, a marriage, a birth, a section of an Act, a publication, a matter to be proved, a forum, a printed copy, an instrument under s 112b, a non-binding instrument). |
| `us-interpretation-time.l4` | The reusable time module; imports only `prelude` and `daydate`. Part A: the six items, each a named function with a `@ref` and a named `REFUSE` (plus deemed service and the time words). Part B: the text's own periods read in the ordinary sense (ss 106, 204, 112b, 202(c)). |
| `us-ch1-construction.l4` | ss 1 to 8. |
| `us-ch2-forms-of-acts.l4` | ss 101 to 107, 106a, 106b, 114. |
| `us-ch2-repeals.l4` | ss 108 to 111, and two named refusals for what the text does not say about repeal. |
| `us-evidence-of-law.l4` | ss 112, 112a(a), 113, 204 and 209: what Title 1 makes evidence of what. |
| `us-ch2-international-agreements.l4` | ss 112a(b) and 112b. |
| `us-ch3-codes.l4` | ss 201 to 203, 205 to 208, 210 to 213 (ss 204 and 209 are in the evidence module). |
| `tests-time.l4`, `tests-ch1.l4`, `tests-ch2.l4`, `tests-112b.l4`, `tests-ch3.l4` | the assertions; counts in section 5. |

Every module starts with `@lang en`.
The language server prints a Hint on that line in a module that declares nothing ("A module that declares nothing is English; this line can go"); the brief requires the line, so the hint is left.

### How "includes", "means" and "shall" are encoded

- A definition that says "includes" is not a closed list. Each such function is named for what the section EXPRESSLY includes: TRUE reads "the section says so", FALSE reads "the section does not say so", never "it is not so". Applies to ss 1, 2, 3, 4, 112b(k)(4) and (k)(7), and to the evidence sections (a matter, a publication or a forum that a section does not name is FALSE under that section and may be evidence under another rule).
- A definition that says "means" is exhaustive: s 7(b) "State", s 8(b) "born alive", s 112b(k)(5) "qualifying non-binding instrument".
- "Unless the context indicates otherwise" (s 1) is an input, `the context indicates otherwise`, that switches the limb off.
- A duty or power is encoded as what the section provides on the facts given, never as a prediction that the duty will be met.
- Where the text is silent the answer is a `REFUSE` named for what is missing; the message equals the function's own name, and each refusal is tested with `#ASSERT REFUSED ... BECAUSE "<the exact message>"`.

## 2. Coverage table

Title 1 has 39 sections in three chapters, no schedules and no tables, and none of its sections is repealed, transferred or blank in this text.
Counts by disposition: **encoded 35, inert 4 (ss 107, 203, 205, 206), repealed or blank in this text 0, not applicable 0.**
"Encoded" means at least one limb of the section is a tested function; the limbs left inert inside an encoded section are in the second table.
A named refusal counts as encoded (ss 106a, 106b): the function exists, is cited to the section, and is tested.

| section | heading (as the text prints it) | line in usc01.txt | disposition | what is in it |
| --- | --- | --- | --- | --- |
| s 1 | Words denoting number, gender, and so forth | src:17 | encoded | us-ch1-construction.l4: person and whoever, officer, signature and subscription, oath and sworn, writing, each as a scoped function with the context as an input. INERT limbs (see limb table): the canons of number, gender and tense, and "insane". |
| s 2 | “County” as including “parish”, and so forth | src:31 | encoded | us-ch1-construction.l4: county, scoped. |
| s 3 | “Vessel” as including all means of water transportation | src:35 | encoded | us-ch1-construction.l4: vessel, scoped; fork F-3-4. |
| s 4 | “Vehicle” as including all means of land transportation | src:39 | encoded | us-ch1-construction.l4: vehicle, scoped; fork F-3-4. |
| s 5 | “Company” or “association” as including successors and assigns | src:43 | encoded | us-ch1-construction.l4: successors and assigns deemed embraced, when used in reference to a corporation. |
| s 6 | Limitation of term “products of American fisheries” | src:47 | encoded | us-ch1-construction.l4: the exclusion from "products of American fisheries"; fork F-6. |
| s 7 | Marriage | src:51 | encoded | us-ch1-construction.l4: (a) considered married, (b) "State", (c) only the law at the time of the marriage (folded into one input); fork F-7a. |
| s 8 | “Person”, “human being”, “child”, and “individual” as including born-alive infant | src:57 | encoded | us-ch1-construction.l4: (b) born alive, (a) inclusion; (c) is a rule of non-construction, folded into (a): for a member not born alive (a) affirms and denies nothing. |
| s 101 | Enacting clause | src:65 | encoded | us-ch2-forms-of-acts.l4: the enacting clause as a string check; fork F-101. |
| s 102 | Resolving clause | src:69 | encoded | us-ch2-forms-of-acts.l4: the resolving clause as a string check; fork F-101. |
| s 103 | Enacting or resolving words after first section | src:73 | encoded | us-ch2-forms-of-acts.l4: no enacting or resolving words after the first section, over a list of sections. |
| s 104 | Numbering of sections; single proposition | src:77 | encoded | us-ch2-forms-of-acts.l4: each section numbered. "a single proposition of enactment, as nearly as may be" is a standard of judgment and is INERT. |
| s 105 | Title of appropriation Acts | src:81 | encoded | us-ch2-forms-of-acts.l4: the style and title of an appropriation Act; fork F-101 (the stop) and F-105. |
| s 106 | Printing bills and joint resolutions | src:85 | encoded | us-ch2-forms-of-acts.l4: the last sentence (the last six days of a session, by concurrent resolution), through the time module, B.1. The procedure of engrossing and enrolling is INERT. |
| s 106a | Promulgation of laws | src:89 | encoded | us-ch2-forms-of-acts.l4: a named refusal: "forthwith" is never defined, so the day the Archivist must receive a law cannot be computed. |
| s 106b | Amendments to Constitution | src:93 | encoded | us-ch2-forms-of-acts.l4: a named refusal for the same reason ("forthwith"). |
| s 107 | Parchment or paper for printing enrolled bills or resolutions | src:97 | inert | Parchment or paper "of suitable quality as shall be determined by the Joint Committee on Printing": the quality is left to a body not asked in this text, and no fact a downstream encoding asks about turns on it. |
| s 108 | Repeal of repealing act | src:101 | encoded | us-ch2-repeals.l4: no revival unless expressly so provided; fork F-108. |
| s 109 | Repeal of statutes as affecting existing liabilities | src:105 | encoded | us-ch2-repeals.l4: repeal and expiration of a temporary statute: liability not released, statute treated as still in force to enforce it, unless the repealing Act (or the temporary statute) expressly provides. |
| s 110 | Saving clause of Revised Statutes | src:109 | encoded | us-ch2-repeals.l4: both limbs of the saving clause; fork F-110. |
| s 111 | Repeals as evidence of prior effectiveness | src:113 | encoded | us-ch2-repeals.l4: no inference of prior effectiveness, and the proviso that rights and liabilities are unaffected. |
| s 112 | Statutes at Large; contents; admissibility in evidence | src:117 | encoded | us-evidence-of-law.l4: the third sentence (legal evidence). The first and second sentences (the Archivist compiles and publishes; extra sessions consolidated) are INERT duties of compilation. |
| s 112a | United States Treaties and Other International Agreements; contents; admissibility in evidence | src:121 | encoded | (a) second sentence in us-evidence-of-law.l4; (b) in us-ch2-international-agreements.l4. (a) first sentence (the Secretary of State compiles) is INERT. |
| s 112b | United States international agreements and non-binding instruments; transparency provisions | src:126 | encoded | us-ch2-international-agreements.l4: exemptions (b)(3), deadlines (b)(1), (b)(2), (c), (d)(1)-(3), (f), (g), audits (h)(1), definitions (k)(4), (k)(5), (k)(7), savings (l). "Month" in (a)(1) is a named refusal. Limb table lists the inert limbs. |
| s 113 | “Little and Brown’s” edition of laws and treaties; slip laws; Treaties and Other International Acts Series; admissibility in evidence | src:200 | encoded | us-evidence-of-law.l4: competent evidence without further proof or authentication; forks F-113-case and F-forum. |
| s 114 | Sealing of instruments | src:204 | encoded | us-ch2-forms-of-acts.l4: a seal made by impression on the paper is as valid as one on wax. |
| s 201 | Publication and distribution of Code of Laws of United States and Supplements and District of Columbia Code and Supplements | src:210 | encoded | us-ch3-codes.l4: (a) dispensing with slip publication, (b) the number once the exception is applied (fork F-201b), (c) at least one supplement per Congress. The lead-in "in order to avoid duplication and waste" is INERT. |
| s 202 | Preparation and publication of Codes and Supplements | src:220 | encoded | us-ch3-codes.l4: (c) no new edition oftener than once in each five years (fork F-202c) and the supplement-contents limit. (a) and (b) (supplements for each session) and the distribution sentence are INERT. |
| s 203 | District of Columbia Code; preparation and publication; cumulative supplements | src:230 | inert | A bare authorisation: the Committee on the Judiciary "is authorized to print bills to codify, revise, and reenact" the District of Columbia laws. No condition, no period, nothing a program tests. |
| s 204 | Codes and Supplements as evidence of the laws of United States and District of Columbia; citation of Codes and Supplements | src:234 | encoded | us-evidence-of-law.l4: (a) and (b) prima facie evidence as at the day before the following session; the proviso (positive-law titles); (c), (d), (e) citation forms. Forks F-204a, F-204day, F-roman, F-204e. |
| s 205 | Codes and Supplement; where printed; form and style; ancillaries | src:248 | inert | Printing at the Government Publishing Office "in such form and style and with such ancillaries as may be prescribed by the Committee": the content is left to a committee that this text does not ask. |
| s 206 | Bills and resolutions of Committee on the Judiciary of House of Representatives; form and style; ancillaries; curtailment of copies | src:252 | inert | Bills on revision are printed "in such form and style, and with such ancillaries, as such committee may prescribe", and the committee "may also curtail" copies: left to the committee, same reason as s 205. |
| s 207 | Copies of acts and resolutions in slip form; additional number printed for Committee on the Judiciary of House of Representatives | src:256 | encoded | us-ch3-codes.l4: twenty slip copies of each public Act and joint resolution, as MAYBE NUMBER (NOTHING for a private Act); fork F-207. |
| s 208 | Delegation of function of Committee on the Judiciary to other agencies; printing, and so forth, under direction of Joint Committee on Printing | src:260 | encoded | us-ch3-codes.l4: which functions may be vested in another agency by concurrent resolution (201, 202, 204 to 207), and the proviso on the Joint Committee on Printing; fork F-208. |
| s 209 | Copies of Supplements to Code of Laws of United States and of District of Columbia Code and Supplements; conclusive evidence of original | src:264 | encoded | us-evidence-of-law.l4: a printed copy bearing the imprint is conclusive evidence of the original. |
| s 210 | Distribution of Supplements to Code of Laws of United States and of District of Columbia Code and Supplements; slip and pamphlet copies | src:268 | encoded | us-ch3-codes.l4: the proviso (slip and pamphlet copies need not be printed). The first limb (distribution by the Superintendent of Documents in the manner of the Statutes at Large) is INERT. |
| s 211 | Copies to Members of Congress | src:272 | encoded | us-ch3-codes.l4: the number of copies of each publication (ten per Member, ten times the Judiciary Committee members, one per committee). |
| s 212 | Additional distribution at each new Congress | src:276 | encoded | us-ch3-codes.l4: entitlement of a Senator or Representative to one copy, on written application and certification; fork F-212. |
| s 213 | Appropriation for preparing and editing supplements | src:280 | encoded | us-ch3-codes.l4: $6,500 annually authorised for the purposes of ss 202 and 203; for any other purpose, a named refusal. |

### The brief's six must-encode items: what the text has

| must-encode item | what the text has | where it is encoded |
| --- | --- | --- |
| commencement: when an enactment comes into force or begins to bind, the day and the moment | the Act is silent on this | time module, items 5 and 6 below |
| period counting, from or after a day or an event | the Act is silent on this | time module, items 1 and 2 below |
| a last day that is a day of rest, a holiday or a day an office is closed | the Act is silent on this (no line mentions a holiday, a Sunday, a Saturday or a recess) | time module, item 3 below |
| deemed service or notice | the Act is silent on this | `the day a document is treated as served` |
| what a repeal does | ss 108 to 111 only: no revival unless expressly provided; liabilities not released and the statute treated as still in force to enforce them; acts of limitation of the Revised Statutes saved; no inference of prior effectiveness from the 1933 Act. Nothing on repeal and re-enactment. | `us-ch2-repeals.l4`, and two named refusals (repeal and re-enactment; what a repeal does beyond ss 109 to 111) |
| the meanings of time words | the Act is silent on this | `the meaning Title 1 gives to a time word` (seven refusals) |

### The six functions of the time module (`us-interpretation-time.l4`, Part A) and their tests

| item | function | tests-time.l4 lines |
| --- | --- | --- |
| 1 the last day of a period of N days or N weeks counted from a day | `the last day of a period of days or weeks counted from a day` (refuses) | 32 to 40 |
| 2 the last day of a period of N months or N years counted after an event, with a start on the 31st or on 29 February | `the last day of a period of months or years counted after an event` (refuses) | 45 to 57 |
| 3 a period whose last day or days are days of rest, recess or holiday | `the last day of a period once days of rest, recess or holiday are allowed for`, which takes the rest days as an input list (refuses) | 61 to 68 |
| 4 whether a date falls inside a period | `a date falls inside a period counted from a day or after an event` (refuses); `a date lies on or between the first day given and the last day given` (arithmetic on two days the caller holds; no section cited) | 73 to 76; 79 to 85 |
| 5 the day, and the moment within the day, from which an enactment binds | `the day from which an Act binds` (the day the Act itself fixes, else a refusal); `the moment within its commencement day from which an Act binds` (always a refusal) | 90 to 96 |
| 6 the day subordinate legislation comes into force | `the day from which subordinate legislation comes into force` (the day it fixes, else a refusal) | 101 to 103 |
| deemed service | `the day a document is treated as served` (refuses) | 107 |
| time words | `the meaning Title 1 gives to a time word` (seven refusals: day, week, month, year, calendar year, session, forthwith) | 108 to 114 |
| Part B, the text's own periods | last six days (s 106), the day before a session (s 204), N days after, N years after (ss 112b, 202(c)), the preceding N days (s 112b(b)(2)), a period of N years beginning on a day (s 112b(h)) | 116 to 185 |

### Limbs of encoded sections that are inert

| limb | why it is inert |
| --- | --- |
| s 1: the singular includes the plural and the plural the singular; the masculine includes the feminine; the present tense includes the future | Canons about the form of words, applied by a reader to a sentence. A program that holds a fact about a person has no word to put in the singular or the plural; the brief excuses these. |
| s 1: "insane" and "insane person" include "every idiot, insane person, and person non compos mentis" | A list of archaic words for one another, with no test a program applies to a fact about a person. |
| s 8(c) | A rule of non-construction ("Nothing in this section shall be construed to affirm, deny, expand, or contract any legal status ... prior to being born alive"). It is folded into s 8(a): for a member not born alive, (a) affirms and denies nothing. |
| s 104 "a single proposition of enactment, as nearly as may be" | A standard of judgment ("as nearly as may be"), not a test. The numbering is encoded. |
| s 106 the procedure | Engrossing, signing, sending, enrolling and presenting: a sequence of acts of the two Houses and the President. No fact a downstream encoding asks about turns on it. The last sentence is encoded. |
| s 112 first and second sentences; s 112a(a) first sentence | The Archivist or the Secretary of State "shall cause to be compiled, edited, indexed, and published" a volume with stated contents; a duty of compilation owed by an office. |
| s 112b(a)(1)(A), (B)(i), (B)(iii) | The lists, texts and descriptions the Secretary provides to named leaders and committees; every period in them runs on "the prior month" (refused). |
| s 112b(d)(4), (e), (h)(2) to (4), (i), (j) | "On an ongoing basis" and "as needed" (standards of conduct); the designation and title of the Chief International Agreements Officer; what the Comptroller General does after a failure and where he publishes; a duty to make rules; a sense of Congress that imposes nothing. |
| s 112b(k)(1), (2), (3), (6) | Definitions that name an office or a body ("appropriate congressional committees", "appropriate department or agency", "intelligence community", "Secretary"); a program asks nothing of them. |
| s 201 lead-in | "In order to avoid duplication and waste": a statement of purpose that no limb reads. |
| s 202(a), (b); the distribution sentence of (c) | A supplement for each session; copies distributed "in the same manner as" supplements, a manner s 202 does not state. |
| s 210 first limb | Distribution by the Superintendent of Documents "in the same manner as bound volumes of the Statutes at Large"; that manner is not stated in Title 1. |

## 3. Fork register

Each entry: the question, the readings seen, the one taken, and the text that licenses each.
"Searched" means the whole of `usc01.txt`, not a section.

### The forks the brief names

**F-from** — Does a period "from" a day count that day; does a period "after" an event; is the last day inside the period?
- Readings: (i) the day itself is not counted and the last day is inside, so "N days after D" ends on D plus N; (ii) D is day 1; (iii) the last day is outside.
- Taken: in Part A, none; every item refuses, because no section counts a period (searched). In Part B, reading (i), for the word "after" only.
- Text: none counts. The words are used without a counting rule in s 112b(b)(1) ("120 days after the date on which"), (b)(2), (c) ("30 days after"), (d)(1) to (3) ("15 days after"), (h)(1) ("3 years after"), s 202(c) ("once in each five years").

**F-after** — Should the Part B helpers exist at all?
- Readings: (i) read "N days after D" and "N years after D" in their ordinary sense (D plus N) and say so; (ii) refuse these too, because Title 1 has no counting rule.
- Taken: (i), labelled in the module and here as ordinary meaning and not a rule of Title 1. Reading (ii) is what a reader gets by deleting Part B and refusing in the deadline functions of ss 112b and 202(c).
- Text: as F-from.

**F-rest-days** — Does a rule that moves a last day off a rest day or holiday apply to periods in months and years or only to days; and what does it do when several last days in a row are days of rest?
- Taken: the question does not arise. Title 1 has no such rule (no line has `holiday`, `Sunday`, `Saturday` or `recess`). The function exists, takes the rest days as an input list, and refuses; it is tested with one rest day, with two in a row and with three in a row, and with a last day not on the list.

**F-month-year** — What do "month" and "year" mean (calendar or fixed length), and what follows for a start on the 31st or on 29 February?
- Taken: Title 1 never says. "Month" occurs only in s 112b(a)(1) ("once each month", "the prior month"), where it is a named refusal. `daydate` clamps: measured on this binary, `add months` 2025-01-31 by 1 gives 2025-02-28, and `add years` 2024-02-29 by 1 gives 2025-02-28. Title 1 licenses neither answer, so Part A does not use them; Part B uses `add years` only when the month and the day of the result are the same as the start, and otherwise refuses ("the same calendar date does not exist that many years after the date, and Title 1 does not say what then").

**F-moment** — From what moment of its commencement day does an enactment bind?
- Taken: the text does not say (no line); the function returns a TIME and always refuses.

**F-lang** — Which language version has authority?
- Taken: Title 1 has no provision on language (`language` and `English` do not occur in the text). The subject's `STUB-SOURCE-LICENSE.md` says English is the only authoritative language because Congress enacts in English; that note is not part of the statute text and is not used.

### Reading forks inside sections

**F-1-context** — "unless the context indicates otherwise" opens s 1 and governs every limb after the dash. It is an input to each limb. The alternative (it governs only the first limb) reads the sentence against its structure.

**F-3-4** — In "every description of watercraft or other artificial contrivance used, or capable of being used, as a means of transportation on water" (s 3, and s 4 likewise), does "used, or capable of being used" qualify both nouns or only the contrivance?
- Readings: (i) both; (ii) only "other artificial contrivance", so every watercraft is a vessel.
- Taken: (i). The qualifier follows both nouns in one noun phrase. Tested both ways round (a watercraft that cannot be used is not included).

**F-6** — In "fresh or frozen fish fillets, fresh or frozen fish steaks, or fresh or frozen slices of fish substantially free of bone (including any of the foregoing divided into sections)", does "substantially free of bone" qualify all three or only the slices?
- Readings: (i) slices only (the words follow "of fish"); (ii) all three.
- Taken: (i). The record keeps the three kinds and the bone fact apart, so a caller who holds reading (ii) changes one line. Tested with a steak with bone (excluded), a slice with bone (not excluded) and a boneless slice (excluded).

**F-7a** — "an individual shall be considered married if ..." is a sufficient condition, and s 7(a) does not say when an individual is not considered married.
- Taken: the function is TRUE when the conditions hold and FALSE otherwise, and FALSE reads "section 7(a) does not require it to be considered", not "unmarried".

**F-7c** — s 7(c) lets only "the law of the jurisdiction applicable at the time the marriage was entered into" be considered; the record has one field, `it is valid under the law applicable when it was entered into`, which carries both the validity in the State or place and the time rule of (c).

**F-8** — "at any stage of development" has no gestational field to read, and the two "regardless" clauses of (b) (cord cut; natural or induced labor, cesarean section, induced abortion) are in the record and read by nothing, which is the point of them.

**F-101** — The enacting clause (s 101), the resolving clause (s 102) and the appropriation title (s 105) are printed between quotation marks with the closing full stop INSIDE them. Is the stop part of the prescribed words? Taken: the check accepts the form with or without the stop. Another form of words is not accepted. In s 105 the blanks are filled with the object and "the calendar year" as the text prints them, with a space and no comma before the year.

**F-103** — "No enacting or resolving words shall be used in any section ... except in the first": the first section of a list may use them and need not; every later one must not. The encoding takes a list of sections.

**F-106** — The exception for the last six days needs "the order of Congress by concurrent resolution", an input; the six days are the last day of the session and the five before it, by Part B.1.

**F-108** — "unless it shall be expressly so provided" does not say in which instrument. The input is the fact that revival is expressly provided, and the function does not ask where.

**F-110** — The second limb of s 110 ("all suits, proceedings, or prosecutions ... for causes arising, or acts done or committed prior to said repeal, may be commenced and prosecuted within the same time as if said repeal had not been made") is read on its own words, and applies whenever the cause arose or the act was done before the repeal; it is not tied to the Revised Statutes beyond the first limb. The time itself is the time the repealed act of limitation allowed, which Title 1 does not state, so the function says only whether the rule applies.

### Evidence and publication

**F-112-laws** — s 112 lists "laws" among what the Statutes at Large are legal evidence of. Taken: "laws" is the two kinds of Act of Congress that s 113 names, a public Act and a private Act. A general and permanent law of the United States is not listed in s 112 and is FALSE under it (it is covered by s 204). Reading (ii), that "laws" covers every law, makes that one assertion TRUE.

**F-113-case** — "as the case may be" in s 113: taken as "each publication is competent evidence of the matters it contains", an input `the matter is contained in the publication`, so any of the three publications with any of the five matters named. A reader who pairs slip laws only with Acts and the Series only with treaties changes the function.

**F-forum** — The fora named differ by section. s 112 and s 112a(a): courts of the United States, of the several States, and of the Territories and insular possessions. s 113: courts and "tribunals and public offices" of the United States and of the several States. s 204: courts, tribunals and public offices of the United States, of the District of Columbia, and of each State, Territory or insular possession. A court of the District of Columbia is not "a court of the United States" under s 112 on its words, and is FALSE there.

**F-abroad** — s 204 says "of the United States, at home or abroad"; s 113 says "of the United States". The forum type has no fact for where a tribunal sits, so the two read alike.

**F-204a** — Does the proviso of s 204(a) (the text of a title enacted into positive law "shall be legal evidence") displace the prima facie rule for that title, or add to it? Taken: displaces, since a proviso limits the clause before it; the function for prima facie evidence is FALSE when the title is positive law, and the proviso function is TRUE.

**F-204day** — "the day preceding the commencement of the session following the last session the legislation of which is included": the commencement day of a session is an input (Title 1 does not say when a session commences); the day asked about must equal that day minus one.

**F-roman** — s 204(d) says "Roman figures denoting the number of the supplement". The subtractive convention is taken (IV, IX, XL, XC, CD, CM), the largest figure is MMMCMXCIX (3999), and a number that is not a whole number from 1 to 3999 is a named refusal. The text gives no numeral rules.

**F-204e** — The blank in "U.S.C., ed." is filled with "figures denoting the last year the legislation of which is included". The quotation prints no space after "ed."; the function writes a space and the year.

### Section 112a(b) and section 112b

**F-112a-b** — s 112a(b) takes out "the agreements described in section 112b(b)(3)(A)". Category (A) describes both international agreements and qualifying non-binding instruments. Taken: the exclusion removes the whole category, instruments included. The narrower reading (agreements only) would make a classified non-binding instrument available on request.

**F-b3E** — s 112b(b)(3)(A) to (D) exempt the instrument and the information on its legal authority and implementation; (E) (separately published) exempts the instrument but "the Secretary shall make the information ... available". Two functions, and the second is FALSE for category (E).

**F-k7** — "contemporaneously and in conjunction with" is "construed liberally" and "may not be interpreted to require any action to have occurred simultaneously or on the same day". No date is an input; the input is the judgment, made liberally, that the document was entered into in conjunction with the instrument.

**F-nine** — s 112b(h)(1): a period of nine years "beginning on" a day includes that day and ends the day before the ninth anniversary. With an audit on the sixth anniversary the next falls due on the ninth, which is the first day after the period, so no further audit is required; a reader who counts three audits (the third on the ninth anniversary) reaches the opposite answer for that one boundary. The date "of the enactment of this section" is an input (O-h).

**F-month-112b** — "once each month" and "the prior month" in s 112b(a)(1) are a named refusal (F-month-year).

### Chapter 3

**F-201b** — s 201(b): the number the Committee directs may be curtailed, "except that the Director ... shall print such numbers as are necessary for depository library distribution and for sale". Taken: a floor, so the number printed is the greater of the two. The alternative adds them.

**F-202c** — "not ... oftener than once in each five years": taken as a gap of at least five years from the previous new edition (rolling), counted through the Part B helper, so the earliest day is the same calendar date five years later; a previous edition on 29 February is a refusal. The alternative is fixed blocks of five years, which would need a start date Title 1 does not give.

**F-207** — "twenty copies in slip form of each public Act and joint resolution": taken as "public" qualifying "Act" only, so a joint resolution of any kind is covered; a private Act is NOTHING.

**F-208** — "sections 201, 202, 204-207": taken as 201, 202 and 204 to 207; 203 and 208 itself are not in the list.

**F-212** — "no Senator or Representative during his term of service shall receive under this section more than one copy each of the volumes enumerated herein": taken per volume, the input being the number of copies of that volume already received.

## 4. Answer table, worked cases

Every Part A answer is a refusal: Title 1 is silent.
The right-hand column is what the ordinary meaning of "after" gives (the Part B helper, not a rule of Title 1), so a reader who accepts F-after can see it and a reader who does not can ignore it.
Lines are in `tests-time.l4`.

| period | counted from | what Title 1 says | Part B, ordinary sense of "after" |
| --- | --- | --- | --- |
| three years | 2025-07-16 | silent: refusal "Title 1 has no rule for counting a period of years after an event" (line 45) | 2028-07-16 (line 180) |
| five years | 2025-01-15 | silent (line 46) | 2030-01-15 (line 181) |
| five years | 2025-09-01 | silent (line 47) | 2030-09-01 (line 182) |
| thirty days | 2026-01-01 | silent: refusal "Title 1 has no rule for counting a period of days from a day" (line 32) | 2026-01-31 (line 183) |
| two years | 2024-02-28 | silent (line 48) | 2026-02-28 (line 184) |
| one year | 2024-02-29 | silent (line 49) | refusal: the same calendar date does not exist, and Title 1 does not say what then (line 185) |
| one month | 2025-01-31 | silent: refusal "Title 1 has no rule for counting a period of months after an event" (line 50) | no helper: Title 1 does not say what a month is, and a start on the 31st is the case the missing rule would decide |

| case | question | answer |
| --- | --- | --- |
| an Act is passed or published on 2026-03-10 and says nothing about when it comes into force | from what day, and what moment of that day, does it bind, on the text? | the text is silent on both: refusals "Title 1 does not say from what day an Act binds when the Act does not say" (line 90) and "Title 1 does not say from what moment of its commencement day an Act binds" (line 91) |
| an Act says it comes into force on a day to be fixed later; the day is fixed as 2026-06-01 | from what day and moment does it bind? | the day is 2026-06-01, because that is the Act's own word and Title 1 says nothing against it (line 93); the moment is a refusal (line 94) |
| subordinate legislation is made on 2026-03-10 and says nothing about when it comes into force | from what day does it bind, on the text? | the text is silent: refusal "Title 1 does not say when subordinate legislation comes into force when it does not say" (line 101) |

Other computed answers in the tests, each with its section: the last six days of a session (s 106; tests-time.l4 B.1), the day as at which a Code speaks (s 204; B.2), the 120, 30 and 15 day deadlines of s 112b (tests-112b.l4), the five-year gap of s 202(c) and the three-year audit schedule of s 112b(h) (tests-ch3.l4, tests-112b.l4).

## 5. What check.sh prints

Command: `L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 L4_TARGET=unstable ./check.sh`, run 2026-10-21, exit status 0.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
tests-112b.l4                                  0        73       0        0         0
tests-ch1.l4                                   0        85       0        0         0
tests-ch2.l4                                   0       158       0        0         0
tests-ch3.l4                                   0        53       0        0         0
tests-time.l4                                  0        93       0        0         0
us-ch1-construction.l4                         0         0       0        0         0
us-ch2-forms-of-acts.l4                        0         0       0        0         0
us-ch2-international-agreements.l4             0         0       0        0         0
us-ch2-repeals.l4                              0         0       0        0         0
us-ch3-codes.l4                                0         0       0        0         0
us-evidence-of-law.l4                          0         0       0        0         0
us-interpretation-time.l4                      0         0       0        0         0
us-nouns.l4                                    0         0       0        0         0
TOTAL (13 modules)                             0       462       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`check.sh` counts per module the error diagnostics, the satisfied assertions, the failed ones and the refused ones.
A failed assertion is also an error, and a refused plain `#ASSERT` is red.
`l4 run` prints every assertion result twice, so a grep over the raw output gives double these numbers.
There are no expectations meant to fail: the `expected` column is 0 everywhere, and no file holds a deliberately red assertion.

Source-locator gate: `python3 -I srcrefs.py check --strict <inputs>/usc01.txt us-*.l4` printed `srcrefs check: 102 src: lines, 77 runs, 127 locators, 0 problems`.

Positive control: on a throwaway copy of `tests-ch2.l4`, six expectations were flipped from `#ASSERT` to `#ASSERT NOT`, one expected string was changed (`MCMXCIV` to `MCMXCV`) and one refusal message was changed, and `l4 run` reported 8 failed assertions (and 150 satisfied of 158).
So the harness does detect a failing equality, a failing truth value and a wrong refusal message. The copy was deleted.

## 6. Open questions for a domain expert

- **O-rules-elsewhere.** If a rule that counts periods, moves a last day off a day of rest, fixes the moment of commencement or deems service exists outside Title 1, it is not in this row; every one of those answers here is a refusal because the text deposited has none.
- **O-h.** s 112b(h) counts from "the date of the enactment of this section". The source credit prints a date for the section's addition and later dates for its amendments, and the text does not say which the words mean. The date is an input.
- **O-inhofe.** s 112b(l)(2) names "the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023" and gives no date; the caller supplies the fact whether the material "was required to be provided" before it.
- **O-session.** Title 1 uses "session" (ss 106, 112, 202, 204, 212) and never says when one commences or ends; the dates are inputs.
- **O-forthwith.** ss 106a and 106b say "forthwith" and give no period.
- **O-F-readings.** The reading forks above that most need an expert: F-3-4, F-6, F-7a, F-112-laws, F-113-case, F-204a, F-201b, F-202c and F-nine.
- **O-positive-law.** The subject's licence note says Title 1 is enacted into positive law, so under s 204(a) its text is legal evidence of the law. That is stated in the source metadata and not in the text, and the encoding does not use it.
- **O-roman.** Whether the supplement numbers of s 204(d) are ever above a few dozen, so that the 3999 limit is moot.
