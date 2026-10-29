# NOTES: Magna Carta (1215), the English translation in McKechnie (1905), encoded in L4

Status: draft.
Verified by: `check.sh` (910 assertions satisfied, 0 failed, 0 refused, identical on the main build), `check-traces.py` (not shipped; every `#TRACE` against a hand-written `-- expect:` line, on both binaries), `srcrefs.py check` and `--strict` (0 problems), `tools/branchcheck.py` (every branch that answers no quotes the text's own words, found in its own source lines, and every branch that answers not covered names its reason, with the words that can make the text say no accounted for), and `tools/coverage.py` (not shipped; every unit has a disposition, every rule it cites exists).
Not verified by: any person.
No domain expert has read this encoding against the source.
Encoding name: `legalese-sonnet-5.5` (one Sonnet 5.5 agent, working alone from the brief, with no subagents).
Binary: `l4` 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`; `JL4_LIBRARY_PATH` unset.

This file was generated in part, by scripts that are not shipped; "Generators and checkers used and not shipped" says which.
The files in this folder are the source of truth, and this file is edited directly.

## What this encoding does not claim

It makes no claim that any provision of the Charter is, or was, in force or applied, in whole or in part, at any time.
The Charter is encoded as the text reads: it grants, confirms, forbids and orders.
The source is an English translation printed in a 1905 commentary, rendered to plain text by a script.
It is a translation or extract, not the official text.
No domain expert has read this encoding against the source.
It imports no later law, no history and no other version of the Charter; where the translation can be read two ways, the fork register records both and says which was taken.
The glosses in the section on undefined terms are marked "gloss (not the text's)" and are reader's aids, not definitions the encoding relies on.

## What this is

The text is a preamble and 63 chapters; the division is a modern convenience.
Layer 1 is the law, as thirteen chapter modules and a nouns module, each rule citing the text it encodes with `@ref` and `-- src:` quotation lines, each module tested.
Layer 2 is the seat: `mc15-seat.l4` (126 questions) and `mc15-cases-seat.l4` (328 worked cases).

| File | What it holds |
| --- | --- |
| `mc15-nouns.l4` | the parties, the acts, the answer types (`Bar`, `Entitlement`, `Obligation`, `Forum`, `Remedy`, ...) and the small kinds the chapters sort things into |
| `mc15-ch01.l4` to `mc15-ch60-63.l4` | the chapter modules, in the text's order |
| `mc15-tests-ch*.l4` | one test file per module: `#ASSERT` on the decision functions, `#TRACE` with a `-- expect:` line on every regulative rule |
| `mc15-seat.l4`, `mc15-cases-seat.l4` | layer 2 |
| `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` | supplied; unchanged |
| `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`, `PROGRESS.md` | deposit metadata, the licence pointer, a copy of the brief, and the work log |

The chapter modules, the seat and its cases were generated from templates and from one table of seat questions; neither is shipped.
The quotation lines in the modules were read from the raw text by the generator and never retyped.

## Seat

The seat is a person living under King John's rule who is not the King: a free man, a widow, an heir, a merchant, a tenant who holds land by military service, someone who owes money.
That person asks, on facts they can state, what the Crown and its officers may and may not do to them under the Charter, and what the Charter gives them.
Commons requires every body of law to be asked about from the position of the individual to whom it is applied, because the Legalese website turns such a layer into a question form.
Each of the 126 questions has `@export` and, on every input, `@desc` worded as the person would be asked.
The questions are grouped under `§§` headings in the text's own order, from chapter 1 to chapter 63.
Every question takes plain inputs, one per fact the person can state, and calls the chapter module's rule; no rule is restated in the seat.
Provisions that address only the King's own acts are encoded in layer 1 for what they decide, and appear in the seat only as what they mean to the person ("May the King imprison me ...?").
There is no seat for an official.
The answer types read the same way throughout: `Barred` (the text's own words bar it on those facts), `Not barred` (the text itself says no in its own words, such as "if", "unless" or "so long as"; it says nothing about any other law), and `Bar not covered` (the text is silent on those facts, or its list is not closed, or a term is undefined, or it points outside itself), and likewise for `Entitlement` and `Obligation`.
A question that can answer no is named for its chapter ("Under chapter 9, may ...?"), because the answer is about that chapter and no other.
See "Where the text says no, and where it does not".

## Where the text says no, and where it does not

The rule (the team lead's refinement of the rule for a source that does not answer): an answer is `No` only where the text itself says no in its own words.
That is a definition that says "means"; a condition introduced by "if", "only if", "as long as" or "unless"; or a list the text closes with "only".
Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the answer is "not covered", the encoding's NOTHING.
In the chapter modules the answer types carry that rule: `Not barred`, `Not entitled` and `Not obliged` are the "no" values, and `Bar not covered`, `Entitlement not covered` and `Obligation not covered` are the "not covered" values (and `Standard not covered`, `Forum not covered` and the like for the choice types).
Every branch that returns a "no" has a `-- FALSE-kind` comment above it that quotes the words; every branch that returns a "not covered" (or NOTHING) has a `-- NOTHING-kind (<why>)` comment above it, where <why> is one of "silent", "list not closed", "includes", "undefined term" and "outside the text", or, where the function's source holds one of the words that can make the text say no, the form given under "The sweep of the not-covered branches" below.
`tools/branchcheck.py` fails when a branch has no comment, when a "no" comment quotes none of the accepted words or quotes a passage that is not in the function's source lines, or when a "not covered" comment names none of the allowed reasons.
Its output is under "What branchcheck.py prints".

Five entries in the fork register say what the rule is taken to mean:

- **F64a** takes the plain variants of the named words: "so long as", "while" and "until" for "as long as"; "except", "save", "saving" and "other than" for "unless"; "provided (always) that" for "if"; and "need not", which says in terms that nothing is owed.
- **F64b** takes six limits the text states without the word "only" as closed: "nothing but" (4.1), "not ... more than" (12.2), "greater service ... than is due" (16.1), "elsewhere than" (18.1), "beyond one year and one day" (32.1) and "no other ... than" (43.1).
- **F64c** does not take the rest: where the text states what is required in other words ("on payment of", "without disparagement", "against the will of", "shall remain at", "shall be held in", "as soon as", "thereafter", "as far as", "as many as", "for this purpose only"), the case that meets the requirement, or lies outside the stated time, is not a "no".
  It is `Bar not covered`, `Entitlement not covered` or `Obligation not covered`.
- **F64d** does not take "when" as "if": "when he is willing to perform it in his own person" (29.1) and "the wardship of them, when vacant" (46.1) say when the rule applies, and where "when" is not met the answer is `Bar not covered` or `Entitlement not covered`.
  The other reading is that "when" works as "if", and "Marginal readings for a lawyer" below states it.
- **F64e** takes the failing of a fact the clause makes a condition (the debtor died, the heir was under age, the debt fell into the King's hands, information was received) as the text's no, and does not take the failing of the class of person or thing the clause speaks of (the Jews' debtor, a holder in chief, an officer other than a sheriff or bailiff) as one.
  A person outside the class is outside the sentence, and the text does not say.

A function that can answer no is named for the scope its no claims.
Every chapter-module rule begins `ch N --`, and every seat question that can answer no begins "Under chapter N," ("Under chapter 9, may the King or his bailiffs seize my land or rent for my debt?"), not "May the King ...?".
The seat questions that return a number, a date or a choice are not renamed, because they answer no to nothing.
The yes/no functions that remain (`... as the Charter requires`, `... within the forty days`, a count compared with a count, a majority of those present) compare facts the person states with a number the text gives, and are named for what they compare; they do not say that anything is allowed or barred.

What changed when the rule was applied, so a reader of an earlier copy of this encoding can see it.

**The first pass.**
24 functions that answered `Not barred`, `Not entitled` or `Not obliged` on facts where the text only states a rule or a time now answer "not covered" (chapters 2, 6, 17, 19, 22, 25, 26, 28, 29, 30, 31, 32, 35, 38, 41, 43, 46, 51, 52, 53, 55, 57, 60 and 61), and the forty days in 7.3 answer `Entitlement not covered` for day 41 and for a day before the death where they answered FALSE.
How the expected values were changed, which differs between the two kinds of file:
the template change was made first, then the module tests were run, and 37 assertions then needed a new expected value (30 failed, 5 would not type-check because 7.3 changed type, and 2 sat behind those type errors).
Each of the 37 was re-derived from the rule and the text, and moved to the matching "not covered" value (or, for 7.3, to `Entitled` or `Entitlement not covered`); none was changed to any other value, and no assertion outside that set failed.
One more (ch 28, money tendered at once) was re-derived by the same reading before its run, after a review of the rule found it inconsistent with F64c.
The 22 expected values in the seat cases were rewritten before the cases were run, and all 328 then passed.
The tests keep the same number of assertions (579 and 328).

**The second pass (2026-10-30), and why it happened.**
An independent test author, writing from the text alone, reported six branches in which the governing sentence opens with "if" (or turns on an "if ... and ...") and the function answered "not covered" when the "if" failed.
This encoding's own rule counts "if" as the text's no.
The first pass had applied that rule to the functions it looked at and had read an "if" that fails as silence in these six, so the six answers broke the rule.
The team lead's fix list named the six and asked for a sweep of every other "not covered" branch whose sentence holds one of the words that can make the text say no.
The six, now `Not obliged` or `Not entitled`, each with a `-- FALSE-kind` comment quoting the "if":
chapter 19 (all the assizes can be taken), chapter 26.1 (the letters patent not exhibited, `Not entitled`; the limits "to the value of that debt" and "at the sight of lawful men" stay "not covered"), chapter 41.4 (our men not safe, `Not entitled`), chapter 52 (dispossession with a legal judgment), chapter 56 (disseisin of a Welshman with a judgment) and chapter 61.4 (notified to fewer than four barons; "four" is read as at least four, F61i).
The sweep is the next subsection.
How the expected values were changed in this pass: the templates were changed first and the tests were run; for the sweep, the failing list was compared with the set the changes predicted before any expected value was touched, and the two were equal.
Every expected value that had said "not covered" for a failing "if" (29 module assertions and 12 seat cases) was re-derived from the text and the rule and moved to the matching "no" value, with a `-- RECONCILED 2026-10-30` comment that quotes the original; none was deleted.
Three seat cases were added where the "no" had no case yet, so the seat cases are 331 and the module tests are still 579.
The branch counts are in the table below.

| | `no` branches | `not covered` branches |
| --- | --- | --- |
| after the first pass (the last `branch-output.txt` before the second pass) | 43 | 138 |
| after the second pass | 66 | 128 |

The `no` count rose by 23, the 23 branches in the table below.
The `not covered` count fell by 10 and not by 23, because several of the changes restructured a function (the class limb outside, the fact limbs inside), and the class limb is a new `not covered` branch; I have not counted the new branches function by function.

### The sweep of the not-covered branches

`tools/sweepscan.py` lists every branch that answers "not covered" in a function whose source text holds one of these words: if, unless, while, until, as long as, so long as, except, excepting, save, saving, provided, other than, only.
For each, the sweep either changed it to the no-valued answer with a `-- FALSE-kind` comment, or kept it with `-- NOTHING-kind (word not the condition here: <the word> because <one sentence>)`.
The numbers: the first complete scan, run before any sweep edit, flagged 75 branches (the scan's output was scratch and was not kept, so this one number is from my notes of that run and cannot be re-run), and one more was found afterwards that the scanner could not see (ch 29, the number of days of guard: its comment sits above the `DECIDE` line, which the scan did not read), so 76 were flagged at the start.
17 were changed (in 15 functions), and 70 are kept.
So 11 of the 70 were not among the 76 (76 - 17 = 59).
One is chapter 53, which became flagged when it quoted 52.3 ("until the usual term of crusaders") into its own source lines.
The other ten are the remainder of that subtraction; 21 of the 70 sit in the 21 functions this pass changed, so they are probably class-limb branches that the restructuring created, but I did not list them one by one.
The end-state numbers are the ones `branchcheck.py` checks: 70 kept, every one carrying the comment, and 23 changed to the no; the 75 and 76 are history.
The full lists, generated from the modules by `tools/sweeptable.py`, follow; the table of changes also lists the six branches of the fix list, so its total is 23 = 6 + 17, and it is checked by that script against the modules, so it cannot drift from the code.

**Changed to the text's no: 23 branches in 21 functions.**

| pass | function | line of the text | branches changed | word |
| --- | --- | --- | --- | --- |
| fix list | `ch 19 -- the knight or freeholder who was present remains` (mc15-ch17-19.l4) | src:45 | 1 | if |
| fix list | `ch 26 -- the officer may attach and catalogue chattels of the deceased` (mc15-ch23-32.l4) | src:59 | 1 | if |
| fix list | `ch 41 -- the enemy merchant is safe in our land` (mc15-ch41-42.l4) | src:89 | 1 | if |
| fix list | `ch 52 -- the lands, castles, franchises or right are to be restored` (mc15-ch49-59.l4) | src:111 | 1 | if |
| fix list | `ch 56 -- the lands, liberties or other things are to be restored to the Welshman` (mc15-ch49-59.l4) | src:119 | 1 | if |
| fix list | `ch 61 -- the four barons are to repair to the King and petition for the transgression to be corrected` (mc15-ch60-63.l4) | src:129 | 1 | if |
| sweep | `ch 2 -- the heir has his inheritance on payment of the ancient relief` (mc15-ch02-08.l4) | src:11 | 1 | if |
| sweep | `ch 3 -- relief or a fine may be demanded of the heir on coming of age` (mc15-ch02-08.l4) | src:13 | 1 | if |
| sweep | `ch 9 -- the sureties answer for the debt` (mc15-ch09-11.l4) | src:25 | 1 | if |
| sweep | `ch 10 -- the debt may bear interest` (mc15-ch09-11.l4) | src:27 | 1 | if |
| sweep | `ch 10 -- the King may take this sum of the debt` (mc15-ch09-11.l4) | src:27 | 1 | if |
| sweep | `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased` (mc15-ch09-11.l4) | src:29 | 1 | if |
| sweep | `ch 20 -- the amercement may be imposed` (mc15-ch20-22.l4) | src:47 | 1 | if |
| sweep | `ch 25 -- the rent or payment demanded of this unit may be demanded` (mc15-ch23-32.l4) | src:57 | 1 | except |
| sweep | `ch 26 -- the wife and children have their reasonable shares` (mc15-ch23-32.l4) | src:59 | 1 | if, saving |
| sweep | `ch 27 -- the debt which the deceased owed to a person is saved to him` (mc15-ch23-32.l4) | src:61 | 1 | if |
| sweep | `ch 29 -- the knight is relieved from guard in proportion to his time on service` (mc15-ch23-32.l4) | src:65 | 1 | if |
| sweep | `ch 37 -- the King may have wardship of this by reason of the tenure` (mc15-ch33-38.l4) | src:81 | 2 | if |
| sweep | `ch 41 -- the enemy merchant is to be detained` (mc15-ch41-42.l4) | src:89 | 1 | if |
| sweep | `ch 41 -- the body or goods of the detained merchant may be injured` (mc15-ch41-42.l4) | src:89 | 2 | until, if |
| sweep | `ch 61 -- another baron is to be chosen in his place` (mc15-ch60-63.l4) | src:129 | 1 | if |
| | total | | 23 | |

**Kept as `not covered` with a reason: 70 branches in 54 functions.**
The reason is the comment on the branch in the module, in the form `-- NOTHING-kind (word not the condition here: <the word> because <one sentence>)`.

| module | function | line of the text | words |
| --- | --- | --- | --- |
| mc15-ch02-08.l4:47 | `ch 2 -- the heir has his inheritance on payment of the ancient relief` | src:11 | if |
| mc15-ch02-08.l4:51 | `ch 2 -- the heir has his inheritance on payment of the ancient relief` | src:11 | if |
| mc15-ch02-08.l4:121 | `ch 3 -- relief or a fine may be demanded of the heir on coming of age` | src:13 | if |
| mc15-ch02-08.l4:125 | `ch 3 -- relief or a fine may be demanded of the heir on coming of age` | src:13 | if |
| mc15-ch02-08.l4:326 | `ch 8 -- the widow may be compelled to marry` | src:23 | if, so long as, provided |
| mc15-ch09-11.l4:33 | `ch 9 -- land or rent may be seized for the debt` | src:25 | so long as |
| mc15-ch09-11.l4:105 | `ch 9 -- the surety may have the lands and rents of the debtor` | src:25 | if, unless, until |
| mc15-ch09-11.l4:142 | `ch 10 -- the debt may bear interest` | src:27 | if, while |
| mc15-ch09-11.l4:163 | `ch 10 -- the King may take this sum of the debt` | src:27 | if, except |
| mc15-ch09-11.l4:199 | `ch 11 -- the wife has her dower and pays nothing of the debt` | src:29 | if |
| mc15-ch09-11.l4:216 | `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased` | src:29 | if, provided |
| mc15-ch12-16.l4:223 | `ch 15 -- the aid levied by a lord on one of the three occasions may be this aid` | src:37 | only |
| mc15-ch17-19.l4:110 | `ch 19 -- the knight or freeholder who was present remains` | src:45 | if |
| mc15-ch17-19.l4:112 | `ch 19 -- the knight or freeholder who was present remains` | src:45 | if |
| mc15-ch20-22.l4:73 | `ch 21 -- the earl or baron may be amerced in this way` | src:49 | except, only |
| mc15-ch20-22.l4:97 | `ch 22 -- the clerk may be amerced in this way` | src:51 | except |
| mc15-ch20-22.l4:99 | `ch 22 -- the clerk may be amerced in this way` | src:51 | except |
| mc15-ch23-32.l4:76 | `ch 25 -- the rent or payment demanded of this unit may be demanded` | src:57 | except |
| mc15-ch23-32.l4:81 | `ch 25 -- the rent or payment demanded of this unit may be demanded` | src:57 | except |
| mc15-ch23-32.l4:105 | `ch 26 -- the officer may attach and catalogue chattels of the deceased` | src:59 | if |
| mc15-ch23-32.l4:109 | `ch 26 -- the officer may attach and catalogue chattels of the deceased` | src:59 | if |
| mc15-ch23-32.l4:141 | `ch 26 -- the attached chattels may be removed from the lay fief` | src:59 | until, provided |
| mc15-ch23-32.l4:168 | `ch 26 -- the wife and children have their reasonable shares` | src:59 | if, saving |
| mc15-ch23-32.l4:180 | `ch 27 -- how the chattels are distributed` | src:61 | if, saving |
| mc15-ch23-32.l4:206 | `ch 27 -- the debt which the deceased owed to a person is saved to him` | src:61 | if, saving |
| mc15-ch23-32.l4:225 | `ch 28 -- the officer may take corn or other provisions in this way` | src:63 | unless |
| mc15-ch23-32.l4:228 | `ch 28 -- the officer may take corn or other provisions in this way` | src:63 | unless |
| mc15-ch23-32.l4:262 | `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard` | src:65 | if |
| mc15-ch23-32.l4:264 | `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard` | src:65 | if |
| mc15-ch23-32.l4:297 | `ch 29 -- the days of guard of which the knight is relieved` | src:65 | if |
| mc15-ch33-38.l4:33 | `ch 33 -- the kydell is to be removed` | src:73 | except |
| mc15-ch33-38.l4:151 | `ch 37 -- the King may have wardship of this by reason of the tenure` | src:81 | if, unless |
| mc15-ch33-38.l4:154 | `ch 37 -- the King may have wardship of this by reason of the tenure` | src:81 | if, unless |
| mc15-ch39-40.l4:35 | `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` | src:85 | unless |
| mc15-ch39-40.l4:69 | `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` | src:85 | unless |
| mc15-ch41-42.l4:33 | `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water` | src:89 | except |
| mc15-ch41-42.l4:52 | `ch 41 -- the merchant may buy and sell` | src:89 | except |
| mc15-ch41-42.l4:54 | `ch 41 -- the merchant may buy and sell` | src:89 | except |
| mc15-ch41-42.l4:75 | `ch 41 -- a toll may be taken from the merchant` | src:89 | except |
| mc15-ch41-42.l4:77 | `ch 41 -- a toll may be taken from the merchant` | src:89 | except |
| mc15-ch41-42.l4:101 | `ch 41 -- the enemy merchant is to be detained` | src:89 | if, until |
| mc15-ch41-42.l4:123 | `ch 41 -- the body or goods of the detained merchant may be injured` | src:89 | if, until |
| mc15-ch41-42.l4:145 | `ch 41 -- the enemy merchant is safe in our land` | src:89 | if |
| mc15-ch41-42.l4:168 | `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water` | src:91 | except, excepting, provided |
| mc15-ch43-48.l4:37 | `ch 43 -- the King may take this relief and service from the heir` | src:93 | if |
| mc15-ch43-48.l4:39 | `ch 43 -- the King may take this relief and service from the heir` | src:93 | if |
| mc15-ch43-48.l4:94 | `ch 44 -- the man must come before the justiciars of the forest upon a general summons` | src:95 | except |
| mc15-ch43-48.l4:98 | `ch 44 -- the man must come before the justiciars of the forest upon a general summons` | src:95 | except |
| mc15-ch43-48.l4:111 | `ch 45 -- the King may appoint this person to the office` | src:97 | only |
| mc15-ch43-48.l4:196 | `ch 48 -- the evil custom is to be inquired into` | src:103 | if, provided |
| mc15-ch43-48.l4:233 | `ch 48 -- the evil custom is to be utterly abolished` | src:103 | if, provided |
| mc15-ch49-59.l4:161 | `ch 52 -- who decides a dispute over the restoration` | src:111 | if |
| mc15-ch49-59.l4:182 | `ch 52 -- the King has respite for the possession` | src:111 | until, excepting |
| mc15-ch49-59.l4:198 | `ch 52 -- full justice is to be granted for the possession` | src:111 | if |
| mc15-ch49-59.l4:200 | `ch 52 -- full justice is to be granted for the possession` | src:111 | if |
| mc15-ch49-59.l4:231 | `ch 53 -- the King has the same respite concerning the matter` | src:111, src:113 | until |
| mc15-ch49-59.l4:247 | `ch 53 -- full justice is to be granted to the person who complains` | src:113 | if |
| mc15-ch49-59.l4:251 | `ch 53 -- full justice is to be granted to the person who complains` | src:113 | if |
| mc15-ch49-59.l4:282 | `ch 54 -- a person may be arrested or imprisoned upon the appeal` | src:115 | other than |
| mc15-ch49-59.l4:316 | `ch 55 -- who decides what is done with the fine or amercement` | src:117 | if |
| mc15-ch49-59.l4:338 | `ch 55 -- the substitute may sit in the place of a baron in a similar suit` | src:117 | if, provided, only |
| mc15-ch49-59.l4:356 | `ch 56 -- the lands, liberties or other things are to be restored to the Welshman` | src:119 | if |
| mc15-ch49-59.l4:380 | `ch 56 -- who decides a dispute over the restoration to the Welshman` | src:119 | if |
| mc15-ch49-59.l4:443 | `ch 57 -- the King has respite for the possession taken from a Welshman` | src:121 | until, excepting |
| mc15-ch49-59.l4:459 | `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh` | src:121 | if |
| mc15-ch49-59.l4:461 | `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh` | src:121 | if |
| mc15-ch49-59.l4:517 | `ch 59 -- how the King deals with Alexander, King of Scots` | src:125 | unless |
| mc15-ch60-63.l4:158 | `ch 61 -- the five-and-twenty barons are to distrain and distress the King` | src:129 | until |
| mc15-ch60-63.l4:181 | `ch 61 -- the person may be harmed in the distraint` | src:129 | saving |
| mc15-ch60-63.l4:334 | `ch 61 -- the thing procured` | src:129 | if |

`tools/branchcheck.py` now fails on a "not covered" branch in such a function that has neither the comment above nor the no-valued answer, on a comment that names a word the source does not hold or leaves out one it does, and on a `-- FALSE-kind` comment that quotes a passage not present in the function's `-- src:` lines (88 quotations are checked).
That last check found two mistakes of my own and both were corrected: a comment on chapter 54 quoted the word "except", which is not in 54.1 (it now reads "other than" as the text's word), and chapter 53's comment quoted chapter 52's "until" while its source lines held only chapter 53 (it now quotes 52.3 into the source lines and cites it with a second `@ref`).

Calls made in the sweep that a lawyer may take the other way, and that the lead may veto:

1. The lead's cases were single "if" sentences; the sweep extended the same reading to every operative fact limb that fails in the same sentence (for example, the three conditions of 2.1, that the holder has died, that the heir is of full age and that relief is owed, which the fix list did not name).
2. Functions that return a `Bar` and whose operative sentence is conditioned by an "if" now answer `Not barred` when the condition fails (ch 3, the ward; ch 20, mercy; ch 10, ch 37).
3. "Until information" is applied to the bar on injury to the detained merchant as well as to the duty to detain him (ch 41.3), because the one sentence governs both.
4. A failing class, identity or scope limb stays "not covered" (F64e), including "indebted to the Jews" in ch 11, which is read as a class limb.
5. Choice-typed functions (a `Distribution`, a `Forum`, a `Standard`) are kept: they have no no-value.


## Marginal readings for a lawyer

These are the places where one word of the text carries a choice a lawyer should confirm.
Each row quotes the words, names the fork-register entry that states both readings, and says whether the entry was already in the register or was added or amended in the second pass.

| words | entry | the reading taken | the other reading | status |
| --- | --- | --- | --- | --- |
| "when he is willing to perform it in his own person, or ... by another responsible man" (29.1), "when vacant" (46.1) | F64d | "when" says when the rule applies and is not a condition: where it is not met the answer is "not covered" | "when" works as "if": a knight who is not willing and has no substitute may be compelled, and a baron has no wardship of an abbey that is not vacant | added |
| "need not ... except those who are impleaded, or who have become sureties" (44.1) | F44 | the exception withdraws the exemption and does not itself say those men must come (`Obligation not covered`) | it does say they must come (`Obliged`) | amended (full words, other reading) |
| "unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter" (12.1) | F12 and F12b | the exception lifts the common-counsel requirement for the three purposes, for an aid (F12) | the exception does not lift it: common counsel stays required, and the three purposes only name the occasions for an aid | F12 existing, F12b added |
| "after the expiry of at least forty days" (14.2) | F14 | forty elapsed days is enough | more than forty elapsed days are needed | existing |
| "unless by the lawful judgment of his peers and by the law of the land" (39.1, 39.2) | F39a (F39b, F39c) | "and" means both are needed | either suffices (F39b); or the exception does not reach the first limb (F39c) | existing |
| "any debt" (9.1) | F9b | any debt, whoever is owed | a debt owed to the Crown | added |
| "in like manner let it be done touching debts due to others than Jews" (11.4) | F11 | each of 11.1, 11.2 and 11.3 applies to debts to others | only the payment from the residue applies | existing |
| "100s. at most" (2.4), the two sums of £100 | F2b | £100 flat unless less is owed; 100s a ceiling | all three sums are ceilings | existing |
| "in proportion to the time" (29.2) | F29 | no proportion is stated: the days relieved are not covered | a day of guard for each day of service | existing |
| "one width of cloth ... to wit, two ells within the selvedges" (35.4) | F35b | the width is two ells | one width is required and two ells is an instance | added |
| "provided always that we previously have intimation thereof" (48) | F48a | the proviso governs the inquiry and the abolition | it governs the abolition only | existing |
| "the barons choose five-and-twenty barons of the kingdom, whomsoever they will" (61.2) | F61j | the twenty-five must be barons of the kingdom | a non-baron may be chosen | added (no answer depends on it) |
| "notified to four barons of the foresaid five-and-twenty" (61.4) | F61i | at least four | exactly four | added |
| "as far as pertains to us" (62.2) | F62b | the remission is the King's side only | the remission is complete as to everyone | added (no answer depends on it) |
| "if our men are safe there, the others shall be safe in our land" (41.4) | F41b | the "if" is the text's no: `Not entitled` | the text says nothing of the other case | amended |

Of the F12 row: the reading this encoding takes already lifts the common-counsel requirement for the three purposes (the module `ch 12 -- the levy needs the common counsel of the kingdom` is false for an aid for one of them).
F12b states that reading and its alternative side by side so that a lawyer can see which is which.

## Summary of the coverage table

The audit: the raw text has 134 lines, 132 of them non-blank; the units cover 132 of those 132 lines, so 0 non-blank lines are uncovered.
The text is split into 231 units (64 headings, the 4 header lines, and 163 clauses of the preamble and the chapters).
The table has one row per unit by construction: 231 rows, 0 units without a disposition; the audit added no row (rows before the audit: 231, after: 231).

| Disposition | Rows |
| --- | --- |
| encoded | 62 |
| fork | 92 |
| inert, reason 1 (not operative) | 77 |
| inert, reason 2 (machinery) | 0 |
| inert, reason 3 (repealed or blank) | 0 |
| repealed or blank in this text | 0 |
| total | 231 |

## What is encoded and what is not

Every unit of the text has a row below, with exactly one disposition.
`encoded` means a rule or decision function cites the unit with `@ref` and is tested.
`fork` means the text can be read two or more ways with different outcomes; the row points at the fork-register entry and at the rule that encodes the chosen reading.
`inert` is used only for reason 1 (not operative): the title and edition note, the headings, the King's style and the addressees, the reasons for the grant, the enacting words, the names of those who only advised or witnessed, one recital (1.3), the letters patent recorded as evidence (62.3), and the place and date of the grant (63.3).
There is no inert row for reason 2 (machinery) or reason 3 (repealed or blank), and no `out-of-scope` or `deferred` row.
Chapters that do something once (49 to 59, the security in 61, the remission in 62, the observance clause in 63) are encoded as rules, with a fork entry where the text does not say who may enforce or by when.
Rows moved out of `inert`: none; no row was ever placed in `inert` except for reason 1, and the one-off chapters were never inert.

## Coverage table

| Unit | Raw line | Text | Disposition | Rules, or reason | Fork |
| --- | --- | --- | --- | --- | --- |
| H.1 | 1 | Magna Carta (1215) | inert (reason 1) | reason 1: the title and the edition note of the printed text; not operative |  |
| H.2 | 2 | English translation printed in William Sharp McKechnie, Magna Carta: A Commentary ... | inert (reason 1) | reason 1: the title and the edition note of the printed text; not operative |  |
| H.3 | 3 | The division into a preamble and sixty-three chapters is modern, for convenience of ... | inert (reason 1) | reason 1: the title and the edition note of the printed text; not operative |  |
| H.4 | 4 | Footnote markers (numbers in square brackets) are removed, and the underscores that ... | inert (reason 1) | reason 1: the title and the edition note of the printed text; not operative |  |
| P.h | 6 | Preamble | inert (reason 1) | reason 1: a heading |  |
| P.1 | 7 | John, by the grace of God, king of England, lord of Ireland, duke of Normandy and ... | inert (reason 1) | reason 1: the King's style and the addressees; not operative |  |
| P.2 | 7 | Know that, looking to God and for the salvation of our soul, and those of all our ... | inert (reason 1) | reason 1: the reasons for the grant; a purposes clause that creates no rule |  |
| P.3 | 7 | [we have granted as underwritten] | inert (reason 1) | reason 1: the enacting words (the book's bracketed insertion); the rules are in the chapters |  |
| P.4 | 7 | by advice of our venerable fathers, Stephen, archbishop of Canterbury, primate of ... | inert (reason 1) | reason 1: names of those who gave advice; they only advise |  |
| P.5 | 7 | of master Pandulf, subdeacon and member of the household of our lord the Pope, of ... | inert (reason 1) | reason 1: names of those who gave advice; they only advise |  |
| 1.h | 8 | Chapter 1 | inert (reason 1) | reason 1: a heading |  |
| 1.1 | 9 | In the first place we have granted to God, and by this our present charter ... | encoded | `ch 1 -- the English church shall be free, with her rights entire and her liberties inviolate` | F1 |
| 1.2 | 9 | and we will that it be thus observed; | encoded | `ch 1 -- the English church shall be free, with her rights entire and her liberties inviolate` |  |
| 1.3 | 9 | which is apparent from this that the freedom of elections, which is reckoned most ... | inert (reason 1) | reason 1: a recital of past acts that explains 1.1 to 1.2; the rule is in 1.4 |  |
| 1.4 | 9 | and this we will observe, and our will is that it be observed in good faith by our ... | encoded | `ch 1 -- the freedom of elections of the English church shall be observed` | F1 |
| 1.5 | 9 | We have also granted to all freemen of our kingdom, for us and our heirs forever, ... | encoded | `ch 1 -- the person holds the liberties granted in this Charter` | F1 |
| 2.h | 10 | Chapter 2 | inert (reason 1) | reason 1: a heading |  |
| 2.1 | 11 | If any of our earls or barons, or others holding of us in chief by military service ... | fork | `ch 2 -- the holder is one of those this chapter speaks of`; `ch 2 -- the heir has his inheritance on payment of the ancient relief` | F2, F64c, F64e |
| 2.2 | 11 | the heir or heirs of an earl, £100 for a whole earl’s barony; | fork | `ch 2 -- the sum the Charter names for a whole holding of this kind`; `ch 2 -- the relief the heir is to give` | F2b |
| 2.3 | 11 | the heir or heirs of a baron, £100 for a whole barony; | fork | `ch 2 -- the sum the Charter names for a whole holding of this kind`; `ch 2 -- the relief the heir is to give` | F2b |
| 2.4 | 11 | the heir or heirs of a knight, 100s. at most for a whole knight’s fee; | fork | `ch 2 -- the sum the Charter names for a whole holding of this kind`; `ch 2 -- the knight's relief, which is 100s at most`; `ch 2 -- the relief the heir is to give` | F2b |
| 2.5 | 11 | and whoever owes less let him give less, according to the ancient custom of fiefs. | fork | `ch 2 -- the named sum, or less if less is owed`; `ch 2 -- the knight's relief, which is 100s at most`; `ch 2 -- the relief the heir is to give` | F2b |
| 3.h | 12 | Chapter 3 | inert (reason 1) | reason 1: a heading |  |
| 3.1 | 13 | If, however, the heir of any one of the aforesaid has been under age and in ... | fork | `ch 3 -- relief or a fine may be demanded of the heir on coming of age`; `ch 3 -- the heir shall have his inheritance without relief and without fine` | F3, F64e |
| 4.h | 14 | Chapter 4 | inert (reason 1) | reason 1: a heading |  |
| 4.1 | 15 | The guardian of the land of an heir who is thus under age, shall take from the land ... | fork | `ch 4 -- the guardian may take this from the heir's land`; `ch 4 -- the guardian shall take from the land nothing but reasonable produce, customs and services`; `ch 4 -- the guardian shall not make destruction or waste of men or goods` | F64b |
| 4.2 | 15 | and if we have committed the wardship of the lands of any such minor to the ... | encoded | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` | F4 |
| 4.3 | 15 | and the land shall be committed to two lawful and discreet men of that fee, who ... | encoded | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` | F4 |
| 4.4 | 15 | and if we have given or sold the wardship of any such land to someone and he has ... | encoded | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` | F4 |
| 5.h | 16 | Chapter 5 | inert (reason 1) | reason 1: a heading |  |
| 5.1 | 17 | The guardian, moreover, so long as he has the wardship of the land, shall keep up ... | encoded | `ch 5 -- the guardian shall keep up the houses, parks, fishponds, mills and other things out of the issues of the land` |  |
| 5.2 | 17 | and he shall restore to the heir, when he has come to full age, all his land, ... | encoded | `ch 5 -- the guardian shall restore the land to the heir who has come to full age`; `ch 5 -- the restoration is what the Charter requires` |  |
| 6.h | 18 | Chapter 6 | inert (reason 1) | reason 1: a heading |  |
| 6.1 | 19 | Heirs shall be married without disparagement, yet so that before the marriage takes ... | fork | `ch 6 -- the heir may be married in this way` | F6, F64c |
| 7.h | 20 | Chapter 7 | inert (reason 1) | reason 1: a heading |  |
| 7.1 | 21 | A widow, after the death of her husband, shall forthwith and without difficulty ... | encoded | `ch 7 -- the widow may be kept waiting or put to difficulty over her marriage portion and inheritance` | F7 |
| 7.2 | 21 | nor shall she give anything for her dower, or for her marriage portion, or for the ... | encoded | `ch 7 -- the widow may be made to give this` | F7 |
| 7.3 | 21 | and she may remain in the house of her husband for forty days after his death, | fork | `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- the widow may remain in her husband's house` | F7b, F64c |
| 7.4 | 21 | within which time her dower shall be assigned to her. | fork | `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- her dower is assigned within the forty days` | F7, F7b |
| 8.h | 22 | Chapter 8 | inert (reason 1) | reason 1: a heading |  |
| 8.1 | 23 | Let no widow be compelled to marry, so long as she prefers to live without a ... | fork | `ch 8 -- the widow may be compelled to marry` | F8, F64a |
| 8.2 | 23 | provided always that she gives security not to marry without our consent, if she ... | fork | `ch 8 -- the widow may be compelled to marry`; `ch 8 -- the consent her security is against` | F8, F64a |
| 9.h | 24 | Chapter 9 | inert (reason 1) | reason 1: a heading |  |
| 9.1 | 25 | Neither we nor our bailiffs shall seize any land or rent for any debt, so long as ... | fork | `ch 9 -- land or rent may be seized for the debt`; `ch 9 -- neither the King nor his bailiffs shall seize land or rent for a debt while the chattels suffice` | F9b, F64a |
| 9.2 | 25 | nor shall the sureties of the debtor be distrained so long as the principal debtor ... | fork | `ch 9 -- the sureties of the debtor may be distrained`; `ch 9 -- the sureties answer for the debt` | F9, F64a, F64e |
| 9.3 | 25 | and if the principal debtor shall fail to pay the debt, having nothing wherewith to ... | fork | `ch 9 -- the sureties answer for the debt`; `ch 9 -- the sureties shall answer for the debt if the principal debtor fails and has nothing wherewith to pay` | F64a, F64e |
| 9.4 | 25 | and let them have the lands and rents of the debtor, if they desire them, until ... | encoded | `ch 9 -- the surety may have the lands and rents of the debtor`; `ch 9 -- the sureties may have the lands and rents of the debtor until they are indemnified` | F64a |
| 9.5 | 25 | unless the principal debtor can show proof that he is discharged thereof as against ... | encoded | `ch 9 -- the surety may have the lands and rents of the debtor`; `ch 9 -- the sureties may have the lands and rents of the debtor until they are indemnified` | F64a |
| 10.h | 26 | Chapter 10 | inert (reason 1) | reason 1: a heading |  |
| 10.1 | 27 | If one who has borrowed from the Jews any sum, great or small, die before that loan ... | fork | `ch 10 -- the debt may bear interest` | F10, F64a, F64e |
| 10.2 | 27 | and if the debt fall into our hands, we will not take anything except the principal ... | fork | `ch 10 -- the King may take this sum of the debt`; `ch 10 -- the King will take nothing but the principal sum of a debt fallen into his hands` | F10, F64a, F64e |
| 11.h | 28 | Chapter 11 | inert (reason 1) | reason 1: a heading |  |
| 11.1 | 29 | And if anyone die indebted to the Jews, his wife shall have her dower and pay ... | fork | `ch 11 -- the wife has her dower and pays nothing of the debt` | F11 |
| 11.2 | 29 | and if any children of the deceased are left under age, necessaries shall be ... | fork | `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased` | F11, F64e |
| 11.3 | 29 | and out of the residue the debt shall be paid, reserving, however, service due to ... | fork | `ch 11 -- the amount of the debt paid out of the residue`; `ch 11 -- the payment of the debt may be made at the expense of service due to feudal lords` | F11 |
| 11.4 | 29 | in like manner let it be done touching debts due to others than Jews. | fork | `ch 11 -- the wife has her dower and pays nothing of the debt`; `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased`; `ch 11 -- the amount of the debt paid out of the residue` | F11, F64e |
| 12.h | 30 | Chapter 12 | inert (reason 1) | reason 1: a heading |  |
| 12.1 | 31 | No scutage nor aid shall be imposed in our kingdom, unless by common counsel of our ... | fork | `ch 12 -- the levy is an aid for one of the three purposes`; `ch 12 -- the levy needs the common counsel of the kingdom`; `ch 12 -- a scutage or aid may be imposed` | F12, F12b, F64a |
| 12.2 | 31 | and for these there shall not be levied more than a reasonable aid. | fork | `ch 12 -- a scutage or aid may be imposed` | F64a, F64b |
| 12.3 | 31 | In like manner it shall be done concerning aids from the citizens of London. | encoded | `ch 12 -- an aid from the citizens of London may be imposed` |  |
| 13.h | 32 | Chapter 13 | inert (reason 1) | reason 1: a heading |  |
| 13.1 | 33 | And the citizens of London shall have all their ancient liberties and free customs, ... | encoded | `ch 13 -- the citizens of London have all their ancient liberties and free customs, by land and by water` | F13 |
| 13.2 | 33 | furthermore, we decree and grant that all other cities, boroughs, towns, and ports ... | encoded | `ch 13 -- all other cities, boroughs, towns and ports have all their liberties and free customs` | F13 |
| 14.h | 34 | Chapter 14 | inert (reason 1) | reason 1: a heading |  |
| 14.1 | 35 | And for obtaining the common counsel of the kingdom anent the assessing of an aid ... | fork | `ch 14 -- the King will cause the archbishops, bishops, abbots, earls and greater barons to be summoned by letters under seal`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` | F12, F12b |
| 14.2 | 35 | and we will moreover cause to be summoned generally, through our sheriffs and ... | fork | `ch 14 -- the King will cause all others who hold of him in chief to be summoned generally`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` | F14 |
| 14.3 | 35 | and in all letters of such summons we will specify the reason of the summons. | encoded | `ch 14 -- the King will specify the reason of the summons in all letters of summons`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` |  |
| 14.4 | 35 | And when the summons has thus been made, the business shall proceed on the day ... | encoded | `ch 14 -- the business proceeds on the day appointed according to the counsel of those present` |  |
| 15.h | 36 | Chapter 15 | inert (reason 1) | reason 1: a heading |  |
| 15.1 | 37 | We will not for the future grant to any one licence to take an aid from his own ... | encoded | `ch 15 -- the King may grant a licence to take an aid from a lord's own free tenants`; `ch 15 -- the King will not grant a licence to take an aid from a lord's own free tenants, except for the three purposes` | F15, F64a |
| 15.2 | 37 | and on each of these occasions there shall be levied only a reasonable aid. | encoded | `ch 15 -- the aid levied by a lord on one of the three occasions may be this aid` | F15 |
| 16.h | 38 | Chapter 16 | inert (reason 1) | reason 1: a heading |  |
| 16.1 | 39 | No one shall be compelled to perform greater service for a knight’s fee, or for any ... | fork | `ch 16 -- greater service than is due may be demanded` | F16, F64b |
| 17.h | 40 | Chapter 17 | inert (reason 1) | reason 1: a heading |  |
| 17.1 | 41 | Common pleas shall not follow our court, but shall be held in some fixed place. | fork | `ch 17 -- the common plea may be held where the King's court happens to be` | F17, F64c |
| 18.h | 42 | Chapter 18 | inert (reason 1) | reason 1: a heading |  |
| 18.1 | 43 | Inquests of novel disseisin, of mort d’ancestor, and of darrein presentment, shall ... | fork | `ch 18 -- the inquest may be held here` | F64b |
| 18.2 | 43 | We, or, if we should be out of the realm, our chief justiciar, will send two ... | fork | `ch 18 -- two justiciars will be sent through every county four times a year`; `ch 18 -- the justiciars were sent through the county often enough`; `ch 18 -- the assizes are held as the Charter requires` | F18 |
| 19.h | 44 | Chapter 19 | inert (reason 1) | reason 1: a heading |  |
| 19.1 | 45 | And if any of the said assizes cannot be taken on the day of the county court, let ... | fork | `ch 19 -- enough of the knights and freeholders present remain`; `ch 19 -- the knight or freeholder who was present remains` | F19, F64c |
| 20.h | 46 | Chapter 20 | inert (reason 1) | reason 1: a heading |  |
| 20.1 | 47 | A freeman shall not be amerced for a small offence, except in accordance with the ... | fork | `ch 20 -- the amercement may be imposed` | F20, F64a, F64e |
| 20.2 | 47 | and for a grave offence he shall be amerced in accordance with the gravity of his ... | fork | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` | F20b, F64a, F64e |
| 20.3 | 47 | and a merchant in the same way, saving his wares; | fork | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` | F20b, F64a, F64e |
| 20.4 | 47 | and a villein shall be amerced in the same way, saving his wainage—if they have ... | fork | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` | F20b, F64a, F64e |
| 20.5 | 47 | and none of the aforesaid amercements shall be imposed except by the oath of honest ... | fork | `ch 20 -- the amercement may be imposed` | F20, F64a, F64e |
| 21.h | 48 | Chapter 21 | inert (reason 1) | reason 1: a heading |  |
| 21.1 | 49 | Earls and barons shall not be amerced except through their peers, and only in ... | encoded | `ch 21 -- the earl or baron may be amerced in this way` | F20, F64a |
| 22.h | 50 | Chapter 22 | inert (reason 1) | reason 1: a heading |  |
| 22.1 | 51 | A clerk shall not be amerced in respect of his lay holding except after the manner ... | fork | `ch 22 -- the clerk may be amerced in this way` | F22, F64a, F64c |
| 22.2 | 51 | further, he shall not be amerced in accordance with the extent of his church ... | fork | `ch 22 -- the clerk may be amerced in this way` | F64a, F64c |
| 23.h | 52 | Chapter 23 | inert (reason 1) | reason 1: a heading |  |
| 23.1 | 53 | No community or individual shall be compelled to make bridges at river banks, ... | encoded | `ch 23 -- a community or individual may be compelled to make a bridge at a river bank` | F64a |
| 24.h | 54 | Chapter 24 | inert (reason 1) | reason 1: a heading |  |
| 24.1 | 55 | No sheriff, constable, coroners, or others of our bailiffs, shall hold pleas of our ... | encoded | `ch 24 -- the officer may hold pleas of the Crown`; `ch 24 -- no sheriff, constable, coroner or other bailiff shall hold pleas of the Crown` |  |
| 25.h | 56 | Chapter 25 | inert (reason 1) | reason 1: a heading |  |
| 25.1 | 57 | All counties, hundreds, wapentakes, and trithings (except our demesne manors) shall ... | fork | `ch 25 -- the rent or payment demanded of this unit may be demanded` | F25, F64c, F64e |
| 26.h | 58 | Chapter 26 | inert (reason 1) | reason 1: a heading |  |
| 26.1 | 59 | If any one holding of us a lay fief shall die, and our sheriff or bailiff shall ... | fork | `ch 26 -- the officer may attach and catalogue chattels of the deceased`; `ch 26 -- the sheriff or bailiff may attach and catalogue chattels to the value of the debt` | F64c |
| 26.2 | 59 | provided always that nothing whatever be thence removed until the debt which is ... | encoded | `ch 26 -- the attached chattels may be removed from the lay fief` | F26, F64a |
| 26.3 | 59 | and the residue shall be left to the executors to fulfil the will of the deceased; | encoded | `ch 26 -- the value of the residue left to the executors` | F26 |
| 26.4 | 59 | and if there be nothing due from him to us, all the chattels shall go to the ... | fork | `ch 26 -- the wife and children have their reasonable shares` | F26, F64e |
| 27.h | 60 | Chapter 27 | inert (reason 1) | reason 1: a heading |  |
| 27.1 | 61 | If any freeman shall die intestate, his chattels shall be distributed by the hands ... | fork | `ch 27 -- how the chattels are distributed`; `ch 27 -- the nearest kinsfolk and friends shall distribute the chattels of a freeman who died intestate`; `ch 27 -- the debt which the deceased owed to a person is saved to him` | F64e |
| 28.h | 62 | Chapter 28 | inert (reason 1) | reason 1: a heading |  |
| 28.1 | 63 | No constable or other bailiff of ours shall take corn or other provisions from any ... | fork | `ch 28 -- the officer may take corn or other provisions in this way`; `ch 28 -- no constable or other bailiff shall take corn or other provisions without immediately tendering money` | F64c |
| 29.h | 64 | Chapter 29 | inert (reason 1) | reason 1: a heading |  |
| 29.1 | 65 | No constable shall compel any knight to give money in lieu of castle-guard, when he ... | fork | `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard`; `ch 29 -- no constable shall compel a knight to give money in lieu of castle-guard` | F64c, F64d |
| 29.2 | 65 | Further, if we have led or sent him upon military service, he shall be relieved ... | fork | `ch 29 -- the knight is relieved from guard in proportion to his time on service`; `ch 29 -- the days of guard of which the knight is relieved` | F29, F64e |
| 30.h | 66 | Chapter 30 | inert (reason 1) | reason 1: a heading |  |
| 30.1 | 67 | No sheriff or bailiff of ours, or any other person, shall take the horses or carts ... | fork | `ch 30 -- horses or carts may be taken for transport duty`; `ch 30 -- no sheriff or bailiff or other person shall take the horses or carts of a freeman for transport duty against his will` | F64c |
| 31.h | 68 | Chapter 31 | inert (reason 1) | reason 1: a heading |  |
| 31.1 | 69 | Neither we nor our bailiffs shall take, for our castles or for any other work of ... | fork | `ch 31 -- wood may be taken for the King's castles or other work`; `ch 31 -- neither the King nor his bailiffs shall take wood which is not the King's against the will of the owner` | F64c |
| 32.h | 70 | Chapter 32 | inert (reason 1) | reason 1: a heading |  |
| 32.1 | 71 | We will not retain beyond one year and one day, the lands of those who have been ... | fork | `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs` | F32, F32b, F32c, F64b, F64c |
| 33.h | 72 | Chapter 33 | inert (reason 1) | reason 1: a heading |  |
| 33.1 | 73 | All kydells for the future shall be removed altogether from Thames and Medway, and ... | encoded | `ch 33 -- the kydell is to be removed` | F33, F64a |
| 34.h | 74 | Chapter 34 | inert (reason 1) | reason 1: a heading |  |
| 34.1 | 75 | The writ which is called praecipe shall not for the future be issued to anyone, ... | encoded | `ch 34 -- the writ praecipe may be issued` | F34 |
| 35.h | 76 | Chapter 35 | inert (reason 1) | reason 1: a heading |  |
| 35.1 | 77 | Let there be one measure of wine throughout our whole realm; | fork | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` | F35, F64c |
| 35.2 | 77 | and one measure of ale; | fork | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` | F64c |
| 35.3 | 77 | and one measure of corn, to wit, “the London quarter”; | fork | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` | F64c |
| 35.4 | 77 | and one width of cloth (whether dyed, or russet, or halberget), to wit, two ells ... | fork | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` | F35b, F64c |
| 35.5 | 77 | of weights also let it be as of measures. | fork | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` | F35, F64c |
| 36.h | 78 | Chapter 36 | inert (reason 1) | reason 1: a heading |  |
| 36.1 | 79 | Nothing in future shall be given or taken for a writ of inquisition of life or ... | encoded | `ch 36 -- something may be given or taken for the writ`; `ch 36 -- the writ may be denied` | F36 |
| 37.h | 80 | Chapter 37 | inert (reason 1) | reason 1: a heading |  |
| 37.1 | 81 | If anyone holds of us by fee-farm, by socage, or by burgage, and holds also land of ... | fork | `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure` | F37, F64e |
| 37.2 | 81 | nor shall we have wardship of that fee-farm, socage, or burgage, unless such ... | fork | `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure` | F37, F64e |
| 37.3 | 81 | We will not by reason of any petty serjeanty which anyone may hold of us by the ... | fork | `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure` | F37, F64e |
| 38.h | 82 | Chapter 38 | inert (reason 1) | reason 1: a heading |  |
| 38.1 | 83 | No bailiff for the future shall put any man to his “law” upon his own mere word of ... | fork | `ch 38 -- the officer may put a man to his law upon his own mere word of mouth`; `ch 38 -- no bailiff shall put any man to his law upon his own mere word of mouth, without credible witnesses` | F64c |
| 39.h | 84 | Chapter 39 | inert (reason 1) | reason 1: a heading |  |
| 39.1 | 85 | No freeman shall be arrested, or detained in prison, or deprived of his freehold, ... | fork | `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading C, no exception to the passive limb: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` | F39a, F39b, F39c, F39d, F39e |
| 39.2 | 85 | and we will not set forth against him, nor send against him, unless by the lawful ... | fork | `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` | F39a, F39b, F39e, F39f |
| 40.h | 86 | Chapter 40 | inert (reason 1) | reason 1: a heading |  |
| 40.1 | 87 | To no one will we sell, to no one will we refuse or delay, right or justice. | fork | `ch 40 -- right or justice may be sold, refused or delayed`; `ch 40 -- to no one will we sell, refuse or delay right or justice` | F40a, F40b, F40c |
| 41.h | 88 | Chapter 41 | inert (reason 1) | reason 1: a heading |  |
| 41.1 | 89 | All merchants shall have safe and secure exit from England, and entry to England, ... | fork | `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant` | F41a, F64a, F64c |
| 41.2 | 89 | except (in time of war) such merchants as are of the land at war with us. | fork | `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant` | F41c, F64a, F64c |
| 41.3 | 89 | And if such are found in our land at the beginning of the war, they shall be ... | fork | `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured` | F41a, F41c, F64a, F64e |
| 41.4 | 89 | and if our men are safe there, the others shall be safe in our land. | fork | `ch 41 -- the enemy merchant is safe in our land` | F41a, F41b |
| 42.h | 90 | Chapter 42 | inert (reason 1) | reason 1: a heading |  |
| 42.1 | 91 | It shall be lawful in future for any one (excepting always those imprisoned or ... | encoded | `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water` | F64a |
| 42.2 | 91 | except for a short period in time of war, on grounds of public policy— | fork | `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water` | F42a, F64a |
| 42.3 | 91 | reserving always the allegiance due to us. | fork | `ch 42 -- the allegiance due to the King remains owed` | F42b |
| 43.h | 92 | Chapter 43 | inert (reason 1) | reason 1: a heading |  |
| 43.1 | 93 | If one who holds of some escheat (such as the honour of Wallingford, of Nottingham, ... | fork | `ch 43 -- the King may take this relief and service from the heir`; `ch 43 -- his heir shall give no other relief and perform no other service to us than he would have done to the baron` | F43, F64b, F64c |
| 43.2 | 93 | and we shall hold it in the same manner in which the baron held it. | fork | `ch 43 -- the King holds the escheat in the manner in which the baron held it`; `ch 43 -- we shall hold it in the same manner in which the baron held it` | F43 |
| 44.h | 94 | Chapter 44 | inert (reason 1) | reason 1: a heading |  |
| 44.1 | 95 | Men who dwell without the forest need not henceforth come before our justiciars of ... | fork | `ch 44 -- the man must come before the justiciars of the forest upon a general summons` | F44, F64a |
| 45.h | 96 | Chapter 45 | inert (reason 1) | reason 1: a heading |  |
| 45.1 | 97 | We will appoint as justices, constables, sheriffs, or bailiffs only such as know ... | encoded | `ch 45 -- the King may appoint this person to the office`; `ch 45 -- we will appoint as justices, constables, sheriffs or bailiffs only such as know the law of the realm and mean to observe it well` | F45 |
| 46.h | 98 | Chapter 46 | inert (reason 1) | reason 1: a heading |  |
| 46.1 | 99 | All barons who have founded abbeys, concerning which they hold charters from the ... | fork | `ch 46 -- the baron shall have the wardship of the abbey` | F46, F64c, F64d |
| 47.h | 100 | Chapter 47 | inert (reason 1) | reason 1: a heading |  |
| 47.1 | 101 | All forests that have been made such in our time shall forthwith be disafforested; | encoded | `ch 47 -- the forest is to be disafforested` | F47 |
| 47.2 | 101 | and a similar course shall be followed with regard to river-banks that have been ... | encoded | `ch 47 -- the river-bank is to be released from defence` | F47 |
| 48.h | 102 | Chapter 48 | inert (reason 1) | reason 1: a heading |  |
| 48.1 | 103 | All evil customs connected with forests and warrens, foresters and warreners, ... | fork | `ch 48 -- the evil custom is to be inquired into`; `ch 48 -- the inquest is constituted as the text requires` | F48a, F64a |
| 48.2 | 103 | and shall, within forty days of the said inquest, be utterly abolished, so as never ... | fork | `ch 48 -- the last day for abolishing the evil custom`; `ch 48 -- the evil custom is to be utterly abolished`; `ch 48 -- abolition on this day is within the forty days`; `ch 48 -- the abolished custom may be restored` | F48a, F48b, F64a |
| 48.3 | 103 | provided always that we previously have intimation thereof, or our justiciar, if we ... | fork | `ch 48 -- the evil custom is to be inquired into`; `ch 48 -- the evil custom is to be utterly abolished` | F48a, F64a |
| 49.h | 104 | Chapter 49 | inert (reason 1) | reason 1: a heading |  |
| 49.1 | 105 | We will immediately restore all hostages and charters delivered to us by ... | encoded | `ch 49 -- the hostages and charters are to be restored`; `ch 49 -- we will immediately restore all hostages and charters delivered to us by Englishmen` | F49 |
| 50.h | 106 | Chapter 50 | inert (reason 1) | reason 1: a heading |  |
| 50.1 | 107 | We will entirely remove from their bailiwicks, the relations of Gerard de Athyes ... | encoded | `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- the person may have a bailiwick in England in future`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes` |  |
| 50.2 | 107 | namely Engelard de Cygony, Peter, Gyon, and Andrew of the Chancery, Gyon de Cygony, ... | fork | `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes` | F50a, F50b |
| 51.h | 108 | Chapter 51 | inert (reason 1) | reason 1: a heading |  |
| 51.1 | 109 | As soon as peace is restored, we will banish from the kingdom all foreign-born ... | fork | `ch 51 -- the person is to be banished from the kingdom`; `ch 51 -- we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants and mercenary soldiers who have come with horses and arms to the kingdom's hurt` | F51, F64c |
| 52.h | 110 | Chapter 52 | inert (reason 1) | reason 1: a heading |  |
| 52.1 | 111 | If any one has been dispossessed or removed by us, without the legal judgment of ... | encoded | `ch 52 -- the lands, castles, franchises or right are to be restored`; `ch 52 -- we will immediately restore them to him` |  |
| 52.2 | 111 | and if a dispute arise over this, then let it be decided by the five-and-twenty ... | fork | `ch 52 -- who decides a dispute over the restoration` | F52 |
| 52.3 | 111 | Moreover, for all those possessions, from which any one has, without the lawful ... | encoded | `ch 52 -- the King has respite for the possession`; `ch 53 -- the King has the same respite concerning the matter` | F52b, F64a |
| 52.4 | 111 | excepting those things about which a plea has been raised, or an inquest made by ... | encoded | `ch 52 -- the King has respite for the possession` | F52b, F64a |
| 52.5 | 111 | but as soon as we return from our expedition (or if perchance we desist from the ... | fork | `ch 52 -- full justice is to be granted for the possession`; `ch 52 -- as soon as we return from our expedition we will immediately grant full justice therein` | F52b, F64c |
| 53.h | 112 | Chapter 53 | inert (reason 1) | reason 1: a heading |  |
| 53.1 | 113 | We shall have, moreover, the same respite and in the same manner in rendering ... | encoded | `ch 53 -- the King has the same respite concerning the matter` | F53, F64a |
| 53.2 | 113 | and concerning the wardship of lands which are of the fief of another (namely, such ... | encoded | `ch 53 -- the King has the same respite concerning the matter` | F53, F64a |
| 53.3 | 113 | and concerning abbeys founded on other fiefs than our own, in which the lord of the ... | encoded | `ch 53 -- the King has the same respite concerning the matter` | F53, F64a |
| 53.4 | 113 | and when we have returned, or if we desist from our expedition, we will immediately ... | fork | `ch 53 -- full justice is to be granted to the person who complains`; `ch 53 -- when we have returned we will immediately grant full justice to all who complain of such things` | F53, F64c |
| 54.h | 114 | Chapter 54 | inert (reason 1) | reason 1: a heading |  |
| 54.1 | 115 | No one shall be arrested or imprisoned upon the appeal of a woman, for the death of ... | encoded | `ch 54 -- a person may be arrested or imprisoned upon the appeal` | F54, F64a |
| 55.h | 116 | Chapter 55 | inert (reason 1) | reason 1: a heading |  |
| 55.1 | 117 | All fines made with us unjustly and against the law of the land, and all ... | fork | `ch 55 -- what is to be done with the fine or amercement` | F55a |
| 55.2 | 117 | or else it shall be done concerning them according to the decision of the ... | fork | `ch 55 -- what is to be done with the fine or amercement`; `ch 55 -- who decides what is done with the fine or amercement` | F55a |
| 55.3 | 117 | along with the aforesaid Stephen, archbishop of Canterbury, if he can be present, ... | fork | `ch 55 -- who decides what is done with the fine or amercement` | F55b |
| 55.4 | 117 | and if he cannot be present the business shall nevertheless proceed without him, | encoded | `ch 55 -- who decides what is done with the fine or amercement` |  |
| 55.5 | 117 | provided always that if any one or more of the aforesaid five-and-twenty barons are ... | fork | `ch 55 -- the baron may sit in this particular judgment`; `ch 55 -- the substitute may sit in the place of a baron in a similar suit` | F55b, F64c |
| 56.h | 118 | Chapter 56 | inert (reason 1) | reason 1: a heading |  |
| 56.1 | 119 | If we have disseised or removed Welshmen from lands or liberties, or other things, ... | encoded | `ch 56 -- the lands, liberties or other things are to be restored to the Welshman`; `ch 56 -- they shall be immediately restored to them` |  |
| 56.2 | 119 | and if a dispute arise over this, then let it be decided in the marches by the ... | encoded | `ch 56 -- who decides a dispute over the restoration to the Welshman` |  |
| 56.3 | 119 | for tenements in England according to the law of England, for tenements in Wales ... | encoded | `ch 56 -- the law by which the dispute over a tenement is decided` |  |
| 56.4 | 119 | Welshmen shall do the same to us and ours. | fork | `ch 56 -- the Welshman is to restore to the King and his men`; `ch 56 -- Welshmen shall do the same to us and ours` | F56 |
| 57.h | 120 | Chapter 57 | inert (reason 1) | reason 1: a heading |  |
| 57.1 | 121 | Further, for all those possessions from which any Welshman has, without the lawful ... | encoded | `ch 57 -- the King has respite for the possession taken from a Welshman` | F57, F64a |
| 57.2 | 121 | excepting those things about which a plea has been raised or an inquest made by our ... | encoded | `ch 57 -- the King has respite for the possession taken from a Welshman` | F57, F64a |
| 57.3 | 121 | but as soon as we return, (or if perchance we desist from our expedition), we will ... | fork | `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh`; `ch 57 -- as soon as we return we will immediately grant full justice in accordance with the laws of the Welsh` | F57, F64c |
| 58.h | 122 | Chapter 58 | inert (reason 1) | reason 1: a heading |  |
| 58.1 | 123 | We will immediately give up the son of Llywelyn and all the hostages of Wales, and ... | encoded | `ch 58 -- the person or thing is to be given up`; `ch 58 -- we will immediately give up the son of Llywelyn and all the hostages of Wales` | F58 |
| 59.h | 124 | Chapter 59 | inert (reason 1) | reason 1: a heading |  |
| 59.1 | 125 | We will do toward Alexander, King of Scots, concerning the return of his sisters ... | fork | `ch 59 -- how the King deals with Alexander, King of Scots`; `ch 59 -- we will do toward Alexander, King of Scots, in the same manner as we shall do towards our other barons of England` | F59 |
| 59.2 | 125 | and this shall be according to the judgment of his peers in our court. | encoded | `ch 59 -- who judges the matter between the King and Alexander, King of Scots` |  |
| 60.h | 126 | Chapter 60 | inert (reason 1) | reason 1: a heading |  |
| 60.1 | 127 | Moreover, all the aforesaid customs and liberties, the observance of which we have ... | fork | `ch 60 -- the person must observe the customs and liberties towards his men`; `ch 60 -- the customs and liberties shall be observed by all of our kingdom towards their men` | F60, F64c |
| 61.h | 128 | Chapter 61 | inert (reason 1) | reason 1: a heading |  |
| 61.1 | 129 | Since, moreover, for God and the amendment of our kingdom, and for the better ... | inert (reason 1) | reason 1: the reasons for the security; a purposes clause that creates no rule |  |
| 61.2 | 129 | we give and grant to them the underwritten security, namely, that the barons choose ... | encoded | `ch 61 -- the barons choose five-and-twenty barons of the kingdom, whomsoever they will` | F61f, F61j |
| 61.3 | 129 | who shall be bound with all their might, to observe and hold, and cause to be ... | encoded | `ch 61 -- the five-and-twenty barons shall be bound to observe and hold, and cause to be observed, the peace and liberties` | F61f, F61j |
| 61.4 | 129 | so that if we, or our justiciar, or our bailiffs or any one of our officers, shall ... | fork | `ch 61 -- the four barons are to repair to the King and petition for the transgression to be corrected`; `ch 61 -- to whom the four barons repair`; `ch 61 -- the said four barons shall repair to us and petition to have that transgression corrected without delay` | F61a, F61i |
| 61.5 | 129 | And if we shall not have corrected the transgression (or, in the event of our being ... | fork | `ch 61 -- the last day for correcting the transgression`; `ch 61 -- the four barons are to refer the matter to the rest of the five-and-twenty`; `ch 61 -- the four barons aforesaid shall refer that matter to the rest of the five-and-twenty barons` | F61b |
| 61.6 | 129 | the four barons aforesaid shall refer that matter to the rest of the ... | encoded | `ch 61 -- the four barons are to refer the matter to the rest of the five-and-twenty`; `ch 61 -- the four barons aforesaid shall refer that matter to the rest of the five-and-twenty barons` |  |
| 61.7 | 129 | and those five-and-twenty barons shall, together with the community of the whole ... | fork | `ch 61 -- the five-and-twenty barons are to distrain and distress the King`; `ch 61 -- those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways` | F61c, F64a |
| 61.8 | 129 | saving harmless our own person, and the persons of our queen and children; | encoded | `ch 61 -- the person may be harmed in the distraint`; `ch 61 -- saving harmless our own person, and the persons of our queen and children` | F61g |
| 61.9 | 129 | and when redress has been obtained, they shall resume their old relations towards ... | fork | `ch 61 -- the five-and-twenty barons are to resume their old relations towards the King`; `ch 61 -- when redress has been obtained, they shall resume their old relations towards us` | F61g, F64c |
| 61.10 | 129 | And let whoever in the country desires it, swear to obey the orders of the said ... | encoded | `ch 61 -- let whoever in the country desires it swear to obey the orders of the said five-and-twenty barons` | F61d |
| 61.11 | 129 | and we publicly and freely grant leave to every one who wishes to swear, and we ... | encoded | `ch 61 -- the person has the King's leave to swear`; `ch 61 -- we shall never forbid anyone to swear` | F61d |
| 61.12 | 129 | All those, moreover, in the land who of themselves and of their own accord are ... | encoded | `ch 61 -- the person is to be compelled by the King's command to swear`; `ch 61 -- we shall by our command compel the same to swear to the effect foresaid` | F61d |
| 61.13 | 129 | And if any one of the five-and-twenty barons shall have died or departed from the ... | fork | `ch 61 -- another baron is to be chosen in his place`; `ch 61 -- those of the said twenty-five barons who are left shall choose another in his place according to their own judgment` | F64e |
| 61.14 | 129 | Further, in all matters the execution of which is entrusted to these twenty-five ... | fork | `ch 61 -- what those present ordain or command is held as fixed and established` | F61e |
| 61.15 | 129 | and the said twenty-five shall swear that they will faithfully observe all that is ... | encoded | `ch 61 -- the said twenty-five shall swear that they will faithfully observe all that is aforesaid` | F61h |
| 61.16 | 129 | And we shall procure nothing from anyone, directly or indirectly, whereby any part ... | encoded | `ch 61 -- we shall procure nothing from anyone, directly or indirectly, whereby any part of these concessions and liberties might be revoked or diminished` | F61h |
| 61.17 | 129 | and if any such thing has been procured, let it be void and null, and we shall ... | encoded | `ch 61 -- the thing procured`; `ch 61 -- we shall never use it personally or by another` | F61h |
| 62.h | 130 | Chapter 62 | inert (reason 1) | reason 1: a heading |  |
| 62.1 | 131 | And all the ill-will, hatreds, and bitterness that have arisen between us and our ... | encoded | `ch 62 -- the ill-will, hatreds and bitterness are remitted and pardoned` | F62, F62b |
| 62.2 | 131 | Moreover, all trespasses occasioned by the said quarrel, from Easter in the ... | encoded | `ch 62 -- the trespass is fully remitted and completely forgiven, as far as pertains to the King` | F62, F62b |
| 62.3 | 131 | And, on this head, we have caused to be made out to them letters patent of Stephen, ... | inert (reason 1) | reason 1: records that letters patent were made out as evidence, naming those who issued them; creates no rule |  |
| 63.h | 132 | Chapter 63 | inert (reason 1) | reason 1: a heading |  |
| 63.1 | 133 | Wherefore it is our will, and we firmly enjoin, that the English Church be free, ... | encoded | `ch 63 -- the person has and holds all the aforesaid liberties, rights and concessions for himself and his heirs` | F1 |
| 63.2 | 133 | An oath, moreover, has been taken, as well on our part as on the part of the ... | fork | `ch 63 -- all these conditions shall be kept in good faith and without evil intent` | F63 |
| 63.3 | 133 | Given under our hand—the above-named and many others being witnesses—in the meadow ... | inert (reason 1) | reason 1: the place and date of the grant and its witnesses; not operative |  |

## Fork register

Each entry gives the units, what the text leaves open, the readings seen, the one taken, the licensing text verbatim from the source, and the rules that encode the chosen reading.
Entries of the kind "who is bound, by when, or what a plain input means" leave the unit's disposition `encoded`; entries of the kind "a reading that would change an answer" make it a `fork` row.
Where no one is named the encoding returns an explicit "not covered" value or a decision function; it does not invent an actor, a deadline or a remedy.

#### F1: units 1.1, 1.4, 1.5, 63.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "We", "us" and "our" are the King; "our heirs" are bound or benefited too.

Readings seen:
1. "Our heirs" are a second party, bound separately from the King.
2. "We" is the King for the time being, and the heirs are bound through that one party.

Taken: One party, `the King`; the heirs are not a separate party.

Licensing text (verbatim):
> 1.1: In the first place we have granted to God, and by this our present charter confirmed for us and our heirs for ever that the English church shall be free, and shall have her rights entire, and her liberties inviolate;
>
> 1.4: and this we will observe, and our will is that it be observed in good faith by our heirs for ever.
>
> 1.5: We have also granted to all freemen of our kingdom, for us and our heirs forever, all the underwritten liberties, to be had and held by them and their heirs, of us and our heirs forever.
>
> 63.1: Wherefore it is our will, and we firmly enjoin, that the English Church be free, and that the men in our kingdom have and hold all the aforesaid liberties, rights, and concessions, well and peaceably, freely and quietly, fully and wholly, for themselves and their heirs, of us and our heirs, in all respects and in all places for ever, as is aforesaid.

Rules that encode the chosen reading: `ch 1 -- the English church shall be free, with her rights entire and her liberties inviolate`; `ch 1 -- the freedom of elections of the English church shall be observed`; `ch 1 -- the person holds the liberties granted in this Charter`; `ch 63 -- the person has and holds all the aforesaid liberties, rights and concessions for himself and his heirs`

#### F2: units 2.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "in chief by military service" qualifies earls and barons as well as "others".

Readings seen:
1. Three classes: earls, barons, and others holding in chief by military service.
2. One class: everyone named holds in chief by military service.

Taken: The broader reading: an earl or baron, or any other holder in chief by military service.

Licensing text (verbatim):
> 2.1: If any of our earls or barons, or others holding of us in chief by military service shall have died, and at the time of his death his heir shall be of full age and owe “relief,” he shall have his inheritance on payment of the ancient relief, namely

Rules that encode the chosen reading: `ch 2 -- the holder is one of those this chapter speaks of`; `ch 2 -- the heir has his inheritance on payment of the ancient relief`

#### F2b: units 2.2, 2.3, 2.4, 2.5

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the two sums of £100 are flat sums or ceilings, and what a knight's fee pays when nothing is owed by custom.

Readings seen:
1. £100 is a flat sum unless less is owed by custom; 100s is a ceiling.
2. All three sums are ceilings.

Taken: £100 flat unless less is owed by custom, "whoever owes less let him give less"; 100s at most for a knight's fee, and the text states no sum if nothing less is owed (the answer is NOTHING).

Licensing text (verbatim):
> 2.2: the heir or heirs of an earl, £100 for a whole earl’s barony;
>
> 2.3: the heir or heirs of a baron, £100 for a whole barony;
>
> 2.4: the heir or heirs of a knight, 100s. at most for a whole knight’s fee;
>
> 2.5: and whoever owes less let him give less, according to the ancient custom of fiefs.

Rules that encode the chosen reading: `ch 2 -- the sum the Charter names for a whole holding of this kind`; `ch 2 -- the relief the heir is to give`; `ch 2 -- the knight's relief, which is 100s at most`; `ch 2 -- the named sum, or less if less is owed`

#### F3: units 3.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who must let the heir have his inheritance without relief and without fine; the text names no one.

Readings seen:
1. The King, since the holders concerned hold "of us in chief".
2. Any lord to whom relief would be due.
3. No one is named.

Taken: The King (`PARTY the King SHANT demand ...`), gated by a Bar decision; the Bar decision is what the person is told.

Licensing text (verbatim):
> 3.1: If, however, the heir of any one of the aforesaid has been under age and in wardship, let him have his inheritance without relief and without fine when he comes of age.

Rules that encode the chosen reading: `ch 3 -- relief or a fine may be demanded of the heir on coming of age`; `ch 3 -- the heir shall have his inheritance without relief and without fine`

#### F4: units 4.2, 4.3, 4.4

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive about who takes amends, who commits the land and who transfers the wardship.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: A decision function that returns the consequence the text states (a `WasteConsequence`), with no party.

Licensing text (verbatim):
> 4.2: and if we have committed the wardship of the lands of any such minor to the sheriff, or to any other who is responsible to us for its issues, and he has made destruction or waste of what he holds in wardship, we will take of him amends,
>
> 4.3: and the land shall be committed to two lawful and discreet men of that fee, who shall be responsible to us for the issues, or to him to whom we shall assign them;
>
> 4.4: and if we have given or sold the wardship of any such land to someone and he has therein made destruction or waste, he shall lose that wardship, and it shall be transferred to two lawful and discreet men of that fief, who shall be responsible to us in like manner as aforesaid.

Rules that encode the chosen reading: `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste`

#### F6: units 6.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who marries heirs is not named, and "disparagement" is not defined.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.
4. "Disparagement" is a judgment of rank.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party. Disparagement is a plain input.  A marriage that is not a disparagement and was notified is `Bar not covered`: the chapter states what bars a marriage and carries no if, unless or only (F64c).

Licensing text (verbatim):
> 6.1: Heirs shall be married without disparagement, yet so that before the marriage takes place the nearest in blood to that heir shall have notice.

Rules that encode the chosen reading: `ch 6 -- the heir may be married in this way`

#### F7: units 7.1, 7.2, 7.4

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who must give the widow her portion and inheritance, who must not ask her to give, and who must assign dower are not named.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 7.1: A widow, after the death of her husband, shall forthwith and without difficulty have her marriage portion and inheritance;
>
> 7.2: nor shall she give anything for her dower, or for her marriage portion, or for the inheritance which her husband and she held on the day of the death of that husband;
>
> 7.4: within which time her dower shall be assigned to her.

Rules that encode the chosen reading: `ch 7 -- the widow may be kept waiting or put to difficulty over her marriage portion and inheritance`; `ch 7 -- the widow may be made to give this`; `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- her dower is assigned within the forty days`

#### F7b: units 7.3, 7.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: How the forty days are counted from the death.

Readings seen:
1. The day of death is day 0 and day 40 is the last day (at most 40).
2. The forty days begin the day after the death and day 40 is the last day (the same last day).
3. The forty days end on day 39 (fewer than 40).

Taken: Days since the death are counted from 0, and 40 is allowed (AT MOST 40); the text is silent about day 41 and about a day before the death, so those are `Entitlement not covered` (F64c).

Licensing text (verbatim):
> 7.3: and she may remain in the house of her husband for forty days after his death,
>
> 7.4: within which time her dower shall be assigned to her.

Rules that encode the chosen reading: `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- the widow may remain in her husband's house`; `ch 7 -- her dower is assigned within the forty days`

#### F8: units 8.1, 8.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the security is a condition of the bar on compelling a widow, or a further duty beside it; and who compels.

Readings seen:
1. "Provided always": the bar applies only to a widow who gives the security.
2. The bar applies to every widow who prefers to live without a husband, and the security is a separate duty.

Taken: The first reading: Barred needs a widow who prefers to live without a husband AND gives the security; a widow who gives none is `Not barred`.

Licensing text (verbatim):
> 8.1: Let no widow be compelled to marry, so long as she prefers to live without a husband;
>
> 8.2: provided always that she gives security not to marry without our consent, if she holds of us, or without the consent of the lord of whom she holds, if she holds of another.

Rules that encode the chosen reading: `ch 8 -- the widow may be compelled to marry`; `ch 8 -- the consent her security is against`

#### F9: units 9.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive about who may distrain the sureties.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 9.2: nor shall the sureties of the debtor be distrained so long as the principal debtor is able to satisfy the debt;

Rules that encode the chosen reading: `ch 9 -- the sureties of the debtor may be distrained`; `ch 9 -- the sureties answer for the debt`

#### F9b: units 9.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "any debt" in "Neither we nor our bailiffs shall seize any land or rent for any debt" is a debt owed to anyone, or only a debt owed to the Crown.

Readings seen:
1. Any debt, whoever is owed: the Bar applies to a seizure by the King or a bailiff for any debt.
2. A debt owed to the Crown: the King and his bailiffs are speaking of their own debtors.

Taken: Any debt, whoever is owed.  The function takes no input for the creditor, so a seizure for a debt owed to a private creditor is answered as for any other; on the other reading it would be `Bar not covered`.

Licensing text (verbatim):
> 9.1: Neither we nor our bailiffs shall seize any land or rent for any debt, so long as the chattels of the debtor are sufficient to repay the debt;

Rules that encode the chosen reading: `ch 9 -- land or rent may be seized for the debt`; `ch 9 -- neither the King nor his bailiffs shall seize land or rent for a debt while the chattels suffice`

#### F10: units 10.1, 10.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "the debt" in 10.2 is the debt of 10.1 (a loan from the Jews whose borrower has died), or any debt that falls into the King's hands.

Readings seen:
1. The same debt: borrowed from the Jews, borrower dead, fallen into the King's hands.
2. Any debt to the Jews that falls into the King's hands.

Taken: The same debt: the Bar applies when the loan was from the Jews, the borrower died and the debt fell into the King's hands.

Licensing text (verbatim):
> 10.1: If one who has borrowed from the Jews any sum, great or small, die before that loan be repaid, the debt shall not bear interest while the heir is under age, of whomsoever he may hold;
>
> 10.2: and if the debt fall into our hands, we will not take anything except the principal sum contained in the bond.

Rules that encode the chosen reading: `ch 10 -- the debt may bear interest`; `ch 10 -- the King may take this sum of the debt`; `ch 10 -- the King will take nothing but the principal sum of a debt fallen into his hands`

#### F11: units 11.1, 11.2, 11.3, 11.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: How far "in like manner let it be done touching debts due to others than Jews" reaches.

Readings seen:
1. Each of 11.1, 11.2 and 11.3 applies to debts to others.
2. Only the payment from the residue (11.3) applies to debts to others.

Taken: Each applies to debts to others: the three rules take a debt to the Jews or to others.

Licensing text (verbatim):
> 11.1: And if anyone die indebted to the Jews, his wife shall have her dower and pay nothing of that debt;
>
> 11.2: and if any children of the deceased are left under age, necessaries shall be provided for them in keeping with the holding of the deceased;
>
> 11.3: and out of the residue the debt shall be paid, reserving, however, service due to feudal lords;
>
> 11.4: in like manner let it be done touching debts due to others than Jews.

Rules that encode the chosen reading: `ch 11 -- the wife has her dower and pays nothing of the debt`; `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased`; `ch 11 -- the amount of the debt paid out of the residue`; `ch 11 -- the payment of the debt may be made at the expense of service due to feudal lords`

#### F12: units 12.1, 14.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the three cases excused from common counsel excuse a scutage as well as an aid; and whether the reasonableness limit applies to every aid.

Readings seen:
1. The exception reaches aids and scutages alike.
2. The exception reaches aids only: 14.1 puts "(except in the three cases aforesaid)" after "aid" and before "or of a scutage", so a scutage always needs common counsel.

Taken: The second reading: a scutage always needs common counsel; an aid for one of the three purposes needs only to be reasonable.

Licensing text (verbatim):
> 12.1: No scutage nor aid shall be imposed in our kingdom, unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter;
>
> 14.1: And for obtaining the common counsel of the kingdom anent the assessing of an aid (except in the three cases aforesaid) or of a scutage, we will cause to be summoned the archbishops, bishops, abbots, earls, and greater barons, by our letters under seal;

Rules that encode the chosen reading: `ch 12 -- the levy is an aid for one of the three purposes`; `ch 12 -- the levy needs the common counsel of the kingdom`; `ch 12 -- a scutage or aid may be imposed`; `ch 14 -- the King will cause the archbishops, bishops, abbots, earls and greater barons to be summoned by letters under seal`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires`

#### F12b: units 12.1, 14.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What the exception does in "No scutage nor aid shall be imposed in our kingdom, unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter": whether it lifts the common-counsel requirement for the three purposes.

Readings seen:
1. It lifts the requirement: for the three purposes an aid needs no common counsel, and 12.2 limits it to "a reasonable aid".
2. It does not lift the requirement: it names the three purposes as the occasions on which an aid, once common counsel has been had, is allowed at all, and 12.2 limits the amount.

Taken: The first, which is the reading F12 already builds on: `ch 12 -- the levy needs the common counsel of the kingdom` is false for an aid for one of the three purposes, and `ch 12 -- a scutage or aid may be imposed` then asks only whether the aid is reasonable.  The other reading is the second; a lawyer who takes it makes common counsel necessary for every scutage and aid.

Licensing text (verbatim):
> 12.1: No scutage nor aid shall be imposed in our kingdom, unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter;
>
> 14.1: And for obtaining the common counsel of the kingdom anent the assessing of an aid (except in the three cases aforesaid) or of a scutage, we will cause to be summoned the archbishops, bishops, abbots, earls, and greater barons, by our letters under seal;

Rules that encode the chosen reading: `ch 12 -- the levy is an aid for one of the three purposes`; `ch 12 -- the levy needs the common counsel of the kingdom`; `ch 12 -- a scutage or aid may be imposed`; `ch 14 -- the King will cause the archbishops, bishops, abbots, earls and greater barons to be summoned by letters under seal`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires`

#### F13: units 13.1, 13.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 13.1: And the citizens of London shall have all their ancient liberties and free customs, as well by land as by water;
>
> 13.2: furthermore, we decree and grant that all other cities, boroughs, towns, and ports shall have all their liberties and free customs.

Rules that encode the chosen reading: `ch 13 -- the citizens of London have all their ancient liberties and free customs, by land and by water`; `ch 13 -- all other cities, boroughs, towns and ports have all their liberties and free customs`

#### F14: units 14.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "after the expiry of at least forty days" counts as enough.

Readings seen:
1. Forty elapsed days is enough.
2. More than forty elapsed days are needed.

Taken: Forty elapsed days is enough (days AT LEAST 40).  No deadline window is used here: the forty days are tested by a decision function over the number of days.

Licensing text (verbatim):
> 14.2: and we will moreover cause to be summoned generally, through our sheriffs and bailiffs, all others who hold of us in chief, for a fixed date, namely, after the expiry of at least forty days, and at a fixed place;

Rules that encode the chosen reading: `ch 14 -- the King will cause all others who hold of him in chief to be summoned generally`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires`

#### F15: units 15.1, 15.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The licence is granted by "us"; the aid is levied by "any one", whom the text does not name.

Readings seen:
1. The King is bound as to the licence and the lord as to the aid.
2. Neither is named for the aid.

Taken: The King is the party for the licence (gated by a Bar decision); the levying lord is not named, so the aid is a Bar decision with no party.

Licensing text (verbatim):
> 15.1: We will not for the future grant to any one licence to take an aid from his own free tenants, except to ransom his body, to make his eldest son a knight, and once to marry his eldest daughter;
>
> 15.2: and on each of these occasions there shall be levied only a reasonable aid.

Rules that encode the chosen reading: `ch 15 -- the King may grant a licence to take an aid from a lord's own free tenants`; `ch 15 -- the King will not grant a licence to take an aid from a lord's own free tenants, except for the three purposes`; `ch 15 -- the aid levied by a lord on one of the three occasions may be this aid`

#### F16: units 16.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "No one shall be compelled" does not say by whom.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 16.1: No one shall be compelled to perform greater service for a knight’s fee, or for any other free tenement, than is due therefrom.

Rules that encode the chosen reading: `ch 16 -- greater service than is due may be demanded`

#### F17: units 17.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "Some fixed place" is not defined.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 17.1: Common pleas shall not follow our court, but shall be held in some fixed place.

Rules that encode the chosen reading: `ch 17 -- the common plea may be held where the King's court happens to be`

#### F18: units 18.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "four times a year" requires.

Readings seen:
1. At least four times.
2. Exactly four times.

Taken: At least four times (a count of 4 or more is enough).  The text gives no day on which any visit falls.

Licensing text (verbatim):
> 18.2: We, or, if we should be out of the realm, our chief justiciar, will send two justiciars through every county four times a year, who shall, along with four knights of the county chosen by the county, hold the said assizes in the county court, on the day and in the place of meeting of that court.

Rules that encode the chosen reading: `ch 18 -- two justiciars will be sent through every county four times a year`; `ch 18 -- the justiciars were sent through the county often enough`; `ch 18 -- the assizes are held as the Charter requires`

#### F19: units 19.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "As many as may be required" is not defined, and who requires them is not named.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 19.1: And if any of the said assizes cannot be taken on the day of the county court, let there remain of the knights and freeholders who were present at the county court on that day, as many as may be required for the efficient making of judgments, according as the business be more or less.

Rules that encode the chosen reading: `ch 19 -- enough of the knights and freeholders present remain`; `ch 19 -- the knight or freeholder who was present remains`

#### F20: units 20.1, 20.5, 21.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who amerces is not named (the text speaks of falling "into our mercy").

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 20.1: A freeman shall not be amerced for a small offence, except in accordance with the degree of the offence;
>
> 20.5: and none of the aforesaid amercements shall be imposed except by the oath of honest men of the neighbourhood.
>
> 21.1: Earls and barons shall not be amerced except through their peers, and only in accordance with the degree of the offence.

Rules that encode the chosen reading: `ch 20 -- the amercement may be imposed`; `ch 21 -- the earl or baron may be amerced in this way`

#### F20b: units 20.2, 20.3, 20.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the saving (contenement, wares, wainage) holds for a small offence as well as a grave one.

Readings seen:
1. The saving holds for any amercement of that person.
2. The saving holds only for a grave offence.

Taken: The saving is read as holding for any amercement of that person.

Licensing text (verbatim):
> 20.2: and for a grave offence he shall be amerced in accordance with the gravity of his offence, yet saving always his “contenement”;
>
> 20.3: and a merchant in the same way, saving his wares;
>
> 20.4: and a villein shall be amerced in the same way, saving his wainage—if they have fallen into our mercy:

Rules that encode the chosen reading: `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed`

#### F22: units 22.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "after the manner of the others aforesaid" refers to.

Readings seen:
1. The manner of chapters 20 and 21 together.
2. The manner of chapter 21 alone.

Taken: Chapters 20 and 21; whether the manner was followed is a plain input.

Licensing text (verbatim):
> 22.1: A clerk shall not be amerced in respect of his lay holding except after the manner of the others aforesaid;

Rules that encode the chosen reading: `ch 22 -- the clerk may be amerced in this way`

#### F25: units 25.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "shall remain at the old rents" bars a rent lowered below the old rent.

Readings seen:
1. Only a higher rent, or an additional payment, is a departure.
2. Any change is a departure, lower included.

Taken: Only an increase or an additional payment is barred.  The old rent itself and a rent below it are `Bar not covered`: "shall remain at the old rents" carries no if, unless or only (F64c).

Licensing text (verbatim):
> 25.1: All counties, hundreds, wapentakes, and trithings (except our demesne manors) shall remain at the old rents, and without any additional payment.

Rules that encode the chosen reading: `ch 25 -- the rent or payment demanded of this unit may be demanded`

#### F26: units 26.2, 26.3, 26.4

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "Nothing whatever be thence removed" does not say by whom.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 26.2: provided always that nothing whatever be thence removed until the debt which is evident shall be fully paid to us;
>
> 26.3: and the residue shall be left to the executors to fulfil the will of the deceased;
>
> 26.4: and if there be nothing due from him to us, all the chattels shall go to the deceased, saving to his wife and children their reasonable shares.

Rules that encode the chosen reading: `ch 26 -- the attached chattels may be removed from the lay fief`; `ch 26 -- the value of the residue left to the executors`; `ch 26 -- the wife and children have their reasonable shares`

#### F29: units 29.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: "In proportion to the time" states no proportion.

Readings seen:
1. A day of guard for each day of service.
2. The text states no proportion.

Taken: The text states no proportion, so the days of guard relieved are not covered (the value is NOTHING).

Licensing text (verbatim):
> 29.2: Further, if we have led or sent him upon military service, he shall be relieved from guard in proportion to the time during which he has been on service because of us.

Rules that encode the chosen reading: `ch 29 -- the knight is relieved from guard in proportion to his time on service`; `ch 29 -- the days of guard of which the knight is relieved`

#### F32: units 32.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: From what day "one year and one day" is counted.

Readings seen:
1. From the conviction.
2. From the taking of the lands.
3. From some other day.

Taken: The text does not say, so the starting day is an input.

Licensing text (verbatim):
> 32.1: We will not retain beyond one year and one day, the lands of those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.

Rules that encode the chosen reading: `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs`

#### F32b: units 32.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What a year on from 29 February is.

Readings seen:
1. 28 February (the standard library's `add years` clamps).
2. 1 March (rolling forward, as `Date 29 2 y` does).

Taken: The library's clamp: a year on from 29 February 2000 is 28 February 2001, and one day more is 1 March 2001.

Licensing text (verbatim):
> 32.1: We will not retain beyond one year and one day, the lands of those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.

Rules that encode the chosen reading: `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs`

#### F32c: units 32.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "The lands shall thereafter be handed over to the lords of the fiefs" does not say by whom.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 32.1: We will not retain beyond one year and one day, the lands of those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.

Rules that encode the chosen reading: `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs`

#### F33: units 33.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "Kydell" is not defined.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 33.1: All kydells for the future shall be removed altogether from Thames and Medway, and throughout all England, except upon the sea coast.

Rules that encode the chosen reading: `ch 33 -- the kydell is to be removed`

#### F34: units 34.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 34.1: The writ which is called praecipe shall not for the future be issued to anyone, concerning any tenement whereby a freeman may lose his court.

Rules that encode the chosen reading: `ch 34 -- the writ praecipe may be issued`

#### F35: units 35.1, 35.5

Kind: a reading that would change an answer; its units are `fork` rows.

Open: The text says "one measure" of wine and ale without fixing its size, and says weights are "as of measures".

Readings seen:
1. The size is left to the standard in force.
2. "As of measures" means one standard weight throughout the realm.

Taken: One measure (size not stated) for wine and ale; the London quarter for corn; two ells within the selvedges for cloth; one weight (size not stated) for weights.

Licensing text (verbatim):
> 35.1: Let there be one measure of wine throughout our whole realm;
>
> 35.5: of weights also let it be as of measures.

Rules that encode the chosen reading: `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used`

#### F35b: units 35.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "one width of cloth (whether dyed, or russet, or halberget), to wit, two ells within the selvedges" fixes the width at two ells, or requires one width and gives two ells as an instance.

Readings seen:
1. The width is two ells within the selvedges: "to wit" states it.
2. The text requires a single width throughout the realm and gives two ells as an instance; another single width would satisfy it.

Taken: The first: the Standard returned for cloth is `two ells within the selvedges`.

Licensing text (verbatim):
> 35.4: and one width of cloth (whether dyed, or russet, or halberget), to wit, two ells within the selvedges;

Rules that encode the chosen reading: `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used`

#### F36: units 36.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 36.1: Nothing in future shall be given or taken for a writ of inquisition of life or limbs, but freely it shall be granted, and never denied.

Rules that encode the chosen reading: `ch 36 -- something may be given or taken for the writ`; `ch 36 -- the writ may be denied`

#### F37: units 37.1, 37.2, 37.3

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether 37.2 ("that fee-farm") needs the second holding of 37.1, and whether 37.3 needs one.

Readings seen:
1. 37.2 needs the same second holding as 37.1; 37.3 needs none.
2. 37.2 applies to any fee-farm; 37.3 needs the second holding.

Taken: 37.2 needs the second holding ("that fee-farm"); 37.3 names none and applies as written.

Licensing text (verbatim):
> 37.1: If anyone holds of us by fee-farm, by socage, or by burgage, and holds also land of another lord by knight’s service, we will not (by reason of that fee-farm, socage, or burgage,) have the wardship of the heir, or of such land of his as is of the fief of that other;
>
> 37.2: nor shall we have wardship of that fee-farm, socage, or burgage, unless such fee-farm owes knight’s service.
>
> 37.3: We will not by reason of any petty serjeanty which anyone may hold of us by the service of rendering to us knives, arrows, or the like, have wardship of his heir or of the land which he holds of another lord by knight’s service.

Rules that encode the chosen reading: `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure`

#### F39a: units 39.1, 39.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the closing words ("unless by the lawful judgment of his peers and by the law of the land") are an exception to the whole sentence or only to the second limb, and whether "and" means both are needed.

Readings seen:
1. The exception covers 39.1 and 39.2; both the judgment of peers and the law of the land are needed.
2. See F39b (either suffices) and F39c (exception only to 39.2).

Taken: The exception covers both limbs, and both conditions are needed (the translation says "and").

Licensing text (verbatim):
> 39.1: No freeman shall be arrested, or detained in prison, or deprived of his freehold, or outlawed, or banished, or in any way molested;
>
> 39.2: and we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land.

Rules that encode the chosen reading: `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land`

#### F39b: units 39.1, 39.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Reading B: "and" read as "or", so either the judgment of peers or the law of the land suffices.

Readings seen:
1. Both needed.
2. Either suffices.

Taken: Not taken.  Encoded as `ch 39 -- reading B, either suffices: ...` so that a case can show the two rows where it differs; no seat question uses it.

Licensing text (verbatim):
> 39.1: No freeman shall be arrested, or detained in prison, or deprived of his freehold, or outlawed, or banished, or in any way molested;
>
> 39.2: and we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land.

Rules that encode the chosen reading: `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`

#### F39c: units 39.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Reading C: the exception belongs to 39.2 alone, because 39.1 ends in a semicolon.

Readings seen:
1. The passive limb has the same exception.
2. The passive limb has no exception.

Taken: Not taken.  Encoded as `ch 39 -- reading C, no exception to the passive limb: ...` for comparison; no seat question uses it.

Licensing text (verbatim):
> 39.1: No freeman shall be arrested, or detained in prison, or deprived of his freehold, or outlawed, or banished, or in any way molested;

Rules that encode the chosen reading: `ch 39 -- reading C, no exception to the passive limb: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`

#### F39d: units 39.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The first limb is passive: "shall be arrested ... or in any way molested" names no one who does it.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.  Only 39.2 ("we") carries a party, the King.

Licensing text (verbatim):
> 39.1: No freeman shall be arrested, or detained in prison, or deprived of his freehold, or outlawed, or banished, or in any way molested;

Rules that encode the chosen reading: `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading C, no exception to the passive limb: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`

#### F39e: units 39.1, 39.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "Freeman", "his peers", "lawful judgment", "the law of the land" and "in any way molested" are not defined.

Readings seen:
1. Each is a plain fact the person states.
2. Each is defined from outside the text.

Taken: Plain inputs: whether the person is a freeman, whether it is done by the lawful judgment of his peers, whether by the law of the land.  No outside definition is imported.

Licensing text (verbatim):
> 39.1: No freeman shall be arrested, or detained in prison, or deprived of his freehold, or outlawed, or banished, or in any way molested;
>
> 39.2: and we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land.

Rules that encode the chosen reading: `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading C, no exception to the passive limb: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land`

#### F39f: units 39.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: What "set forth against him, nor send against him" covers.

Readings seen:
1. Only force or armed expeditions.
2. Any proceeding against him.

Taken: The words are kept as the text's own, in the Act `set forth against a freeman, or send against him, ...`; the encoding does not decide the scope.

Licensing text (verbatim):
> 39.2: and we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land.

Rules that encode the chosen reading: `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`

#### F40a: units 40.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "to no one" is limited to freemen as chapter 39 is.

Readings seen:
1. Everyone.
2. Freemen only.

Taken: Everyone: the rule takes no input about the person.

Licensing text (verbatim):
> 40.1: To no one will we sell, to no one will we refuse or delay, right or justice.

Rules that encode the chosen reading: `ch 40 -- right or justice may be sold, refused or delayed`; `ch 40 -- to no one will we sell, refuse or delay right or justice`

#### F40b: units 40.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: What "right or justice" is.

Readings seen:
1. A fact the person states.
2. Defined from outside the text.

Taken: A plain input: `it is right or justice`.

Licensing text (verbatim):
> 40.1: To no one will we sell, to no one will we refuse or delay, right or justice.

Rules that encode the chosen reading: `ch 40 -- right or justice may be sold, refused or delayed`; `ch 40 -- to no one will we sell, refuse or delay right or justice`

#### F40c: units 40.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Whether "sell", "refuse" and "delay" are three separate bars, and whether "delay" has a period.

Readings seen:
1. Three separate bars; no period.
2. One bar; delay beyond some period.

Taken: Three separate acts of the King, each a SHANT; no period is stated, so none is encoded.

Licensing text (verbatim):
> 40.1: To no one will we sell, to no one will we refuse or delay, right or justice.

Rules that encode the chosen reading: `ch 40 -- right or justice may be sold, refused or delayed`; `ch 40 -- to no one will we sell, refuse or delay right or justice`

#### F41a: units 41.1, 41.3, 41.4

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 41.1: All merchants shall have safe and secure exit from England, and entry to England, with the right to tarry there and to move about as well by land as by water, for buying and selling by the ancient and right customs, quit from all evil tolls,
>
> 41.3: And if such are found in our land at the beginning of the war, they shall be detained, without injury to their bodies or goods, until information be received by us, or by our chief justiciar, how the merchants of our land found in the land at war with us are treated;
>
> 41.4: and if our men are safe there, the others shall be safe in our land.

Rules that encode the chosen reading: `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant`; `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured`; `ch 41 -- the enemy merchant is safe in our land`

#### F41b: units 41.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What follows if "our men" are not safe in the land at war with us: whether the "if" in "if our men are safe there, the others shall be safe in our land" makes the others' safety conditional on ours, or states only what follows when ours are safe.

Readings seen:
1. The "if" is a condition, and the text's own no: where our men are not safe, the others are not entitled to be safe.
2. The text states what follows when ours are safe and says nothing of the other case.

Taken: The first.  The "if" is the text's own word (F64a), so the answer is `Not entitled`.  The first version of this encoding answered `Entitlement not covered`; the second pass of 2026-10-30 (the team lead's fix list) changed it, and the module test and the seat case carry a `-- RECONCILED 2026-10-30` comment quoting the original.

Licensing text (verbatim):
> 41.4: and if our men are safe there, the others shall be safe in our land.

Rules that encode the chosen reading: `ch 41 -- the enemy merchant is safe in our land`

#### F41c: units 41.2, 41.3

Kind: a reading that would change an answer; its units are `fork` rows.

Open: "Of the land at war with us" may mean nationality, residence or origin.

Readings seen:
1. Nationality.
2. Residence.
3. Origin.

Taken: A plain input: `the merchant is of the land at war with the King`.

Licensing text (verbatim):
> 41.2: except (in time of war) such merchants as are of the land at war with us.
>
> 41.3: And if such are found in our land at the beginning of the war, they shall be detained, without injury to their bodies or goods, until information be received by us, or by our chief justiciar, how the merchants of our land found in the land at war with us are treated;

Rules that encode the chosen reading: `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant`; `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured`

#### F42a: units 42.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "except for a short period in time of war, on grounds of public policy" needs both limbs.

Readings seen:
1. Both a short period in war and public policy.
2. Either.

Taken: Both are needed.

Licensing text (verbatim):
> 42.2: except for a short period in time of war, on grounds of public policy—

Rules that encode the chosen reading: `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water`

#### F42b: units 42.3

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "reserving always the allegiance due to us" does.

Readings seen:
1. It leaves the person's allegiance owed.
2. It is a limit on the entitlement to leave.

Taken: It leaves the allegiance owed (an Obligation), and does not reduce the entitlement.

Licensing text (verbatim):
> 42.3: reserving always the allegiance due to us.

Rules that encode the chosen reading: `ch 42 -- the allegiance due to the King remains owed`

#### F43: units 43.1, 43.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "no other relief" bars a smaller relief than the baron would have had, and what "in the same manner" is.

Readings seen:
1. Any different relief is barred, smaller included.
2. Only a greater relief is barred.

Taken: A greater relief, or a service the baron would not have had, is barred.  The baron's own relief is `Not barred` ("no other relief ... than" closes the list, F64b).  A smaller relief is `Bar not covered`: read literally it is "other", read by purpose it is not, and the text does not say (F64c).  "In the same manner" is the text's own phrase, in the Act `hold the escheat in the same manner in which the baron held it`.

Licensing text (verbatim):
> 43.1: If one who holds of some escheat (such as the honour of Wallingford, of Nottingham, of Boulogne, of Lancaster, or of other escheats which are in our hands and are baronies) shall die, his heir shall give no other relief, and perform no other service to us than he would have done to the baron, if that barony had been in the baron’s hand;
>
> 43.2: and we shall hold it in the same manner in which the baron held it.

Rules that encode the chosen reading: `ch 43 -- the King may take this relief and service from the heir`; `ch 43 -- his heir shall give no other relief and perform no other service to us than he would have done to the baron`; `ch 43 -- the King holds the escheat in the manner in which the baron held it`; `ch 43 -- we shall hold it in the same manner in which the baron held it`

#### F44: units 44.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the exception in "Men who dwell without the forest need not henceforth come before our justiciars of the forest upon a general summons, except those who are impleaded, or who have become sureties for any person or persons attached for forest offences" makes those men attend, or only withdraws the exemption.

Readings seen:
1. It makes them attend: the men who are impleaded, or who have become sureties, MUST come.
2. It only withdraws the exemption: the text says that the others need not come and does not itself say that these men must.

Taken: The second: the answer for the impleaded man and the surety is `Obligation not covered` (asserted); the encoding does not say those men MUST come.  The other reading is that it does, and a lawyer who takes it changes that one answer to `Obliged`.

Licensing text (verbatim):
> 44.1: Men who dwell without the forest need not henceforth come before our justiciars of the forest upon a general summons, except those who are impleaded, or who have become sureties for any person or persons attached for forest offences.

Rules that encode the chosen reading: `ch 44 -- the man must come before the justiciars of the forest upon a general summons`

#### F45: units 45.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "Know the law of the realm and mean to observe it well" is not defined, and the office list is closed.

Readings seen:
1. Plain facts the person states.
2. Defined from outside the text.

Taken: Plain inputs; an office not listed gets `Bar not covered`.

Licensing text (verbatim):
> 45.1: We will appoint as justices, constables, sheriffs, or bailiffs only such as know the law of the realm and mean to observe it well.

Rules that encode the chosen reading: `ch 45 -- the King may appoint this person to the office`; `ch 45 -- we will appoint as justices, constables, sheriffs or bailiffs only such as know the law of the realm and mean to observe it well`

#### F46: units 46.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "As they ought to have" is not defined.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 46.1: All barons who have founded abbeys, concerning which they hold charters from the kings of England, or of which they have long-continued possession, shall have the wardship of them, when vacant, as they ought to have.

Rules that encode the chosen reading: `ch 46 -- the baron shall have the wardship of the abbey`

#### F47: units 47.1, 47.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act. "Forthwith" states no period.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 47.1: All forests that have been made such in our time shall forthwith be disafforested;
>
> 47.2: and a similar course shall be followed with regard to river-banks that have been placed “in defence” by us in our time.

Rules that encode the chosen reading: `ch 47 -- the forest is to be disafforested`; `ch 47 -- the river-bank is to be released from defence`

#### F48a: units 48.1, 48.2, 48.3

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the proviso ("provided always that we previously have intimation thereof") governs the inquiry, the abolition, or both.

Readings seen:
1. Both.
2. The abolition only.

Taken: Both: without intimation the answer is `Not obliged`.

Licensing text (verbatim):
> 48.1: All evil customs connected with forests and warrens, foresters and warreners, sheriffs and their officers, river-banks and their wardens, shall immediately be inquired into in each county by twelve sworn knights of the same county chosen by the honest men of the same county,
>
> 48.2: and shall, within forty days of the said inquest, be utterly abolished, so as never to be restored,
>
> 48.3: provided always that we previously have intimation thereof, or our justiciar, if we should not be in England.

Rules that encode the chosen reading: `ch 48 -- the evil custom is to be inquired into`; `ch 48 -- the inquest is constituted as the text requires`; `ch 48 -- the last day for abolishing the evil custom`; `ch 48 -- the evil custom is to be utterly abolished`; `ch 48 -- abolition on this day is within the forty days`; `ch 48 -- the abolished custom may be restored`

#### F48b: units 48.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: How "within forty days of the said inquest" is counted.

Readings seen:
1. The day of the inquest is not counted; the fortieth day after it is the last.
2. The day of the inquest is day 1.

Taken: The first reading: the last day is the day of the inquest plus 40.

Licensing text (verbatim):
> 48.2: and shall, within forty days of the said inquest, be utterly abolished, so as never to be restored,

Rules that encode the chosen reading: `ch 48 -- the last day for abolishing the evil custom`; `ch 48 -- the evil custom is to be utterly abolished`; `ch 48 -- abolition on this day is within the forty days`; `ch 48 -- the abolished custom may be restored`

#### F49: units 49.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "Immediately" states no period, and the text does not say who may enforce.

Readings seen:
1. A fixed period from the Charter.
2. No period.

Taken: No period; the King is the party, gated by an Obligation decision.

Licensing text (verbatim):
> 49.1: We will immediately restore all hostages and charters delivered to us by Englishmen, as sureties of the peace or of faithful service.

Rules that encode the chosen reading: `ch 49 -- the hostages and charters are to be restored`; `ch 49 -- we will immediately restore all hostages and charters delivered to us by Englishmen`

#### F50a: units 50.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: The grouping of the names ("Peter, Gyon, and Andrew of the Chancery").

Readings seen:
1. Three persons: Peter, Gyon and Andrew of the Chancery.
2. Peter and Gyon, and Andrew of the Chancery, are one group or one family.

Taken: Three persons, as the list reads.

Licensing text (verbatim):
> 50.2: namely Engelard de Cygony, Peter, Gyon, and Andrew of the Chancery, Gyon de Cygony, Geoffrey de Martyn with his brothers, Philip Mark with his brothers and his nephew Geoffrey, and the whole brood of the same.

Rules that encode the chosen reading: `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes`

#### F50b: units 50.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "with his brothers", "his nephew" and "the whole brood of the same" reach persons not named.

Readings seen:
1. They reach brothers, the nephew and others of the brood.
2. Only the persons named.

Taken: They reach brothers of Geoffrey de Martyn and of Philip Mark, Geoffrey the nephew, and any other of the brood.

Licensing text (verbatim):
> 50.2: namely Engelard de Cygony, Peter, Gyon, and Andrew of the Chancery, Gyon de Cygony, Geoffrey de Martyn with his brothers, Philip Mark with his brothers and his nephew Geoffrey, and the whole brood of the same.

Rules that encode the chosen reading: `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes`

#### F51: units 51.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "As soon as peace is restored" states no period; "foreign-born" is not defined.

Readings seen:
1. A fixed period after peace.
2. No period.

Taken: No period; peace restored is a plain input, as is being foreign-born.  Before peace is restored the text is silent: `Obligation not covered` (F64c).

Licensing text (verbatim):
> 51.1: As soon as peace is restored, we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants, and mercenary soldiers, who have come with horses and arms to the kingdom’s hurt.

Rules that encode the chosen reading: `ch 51 -- the person is to be banished from the kingdom`; `ch 51 -- we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants and mercenary soldiers who have come with horses and arms to the kingdom's hurt`

#### F52: units 52.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: 52.2 names the five-and-twenty barons "of whom mention is made below in the clause for securing the peace".

Readings seen:
1. The twenty-five barons of chapter 61.
2. A different body.

Taken: The five-and-twenty barons of chapter 61.

Licensing text (verbatim):
> 52.2: and if a dispute arise over this, then let it be decided by the five-and-twenty barons of whom mention is made below in the clause for securing the peace.

Rules that encode the chosen reading: `ch 52 -- who decides a dispute over the restoration`

#### F52b: units 52.3, 52.4, 52.5

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: What "the usual term of crusaders" is, and when the respite ends.

Readings seen:
1. A fixed date.
2. A plain fact: whether the usual term has ended.

Taken: A plain input: `the usual term of crusaders has ended`.

Licensing text (verbatim):
> 52.3: Moreover, for all those possessions, from which any one has, without the lawful judgment of his peers, been disseised or removed, by our father, King Henry, or by our brother, King Richard, and which we retain in our hand (or which are possessed by others, to whom we are bound to warrant them) we shall have respite until the usual term of crusaders;
>
> 52.4: excepting those things about which a plea has been raised, or an inquest made by our order, before our taking of the cross;
>
> 52.5: but as soon as we return from our expedition (or if perchance we desist from the expedition) we will immediately grant full justice therein.

Rules that encode the chosen reading: `ch 52 -- the King has respite for the possession`; `ch 53 -- the King has the same respite concerning the matter`; `ch 52 -- full justice is to be granted for the possession`; `ch 52 -- as soon as we return from our expedition we will immediately grant full justice therein`

#### F53: units 53.1, 53.2, 53.3, 53.4

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "The same respite and in the same manner" refers back to chapter 52.

Readings seen:
1. Exactly chapter 52's respite and justice.
2. A different respite.

Taken: The same: respite until the usual term, then full justice on the King's return or desisting.

Licensing text (verbatim):
> 53.1: We shall have, moreover, the same respite and in the same manner in rendering justice concerning the disafforestation or retention of those forests which Henry our father and Richard our brother afforested,
>
> 53.2: and concerning the wardship of lands which are of the fief of another (namely, such wardships as we have hitherto had by reason of a fief which anyone held of us by knight’s service),
>
> 53.3: and concerning abbeys founded on other fiefs than our own, in which the lord of the fee claims to have right;
>
> 53.4: and when we have returned, or if we desist from our expedition, we will immediately grant full justice to all who complain of such things.

Rules that encode the chosen reading: `ch 53 -- the King has the same respite concerning the matter`; `ch 53 -- full justice is to be granted to the person who complains`; `ch 53 -- when we have returned we will immediately grant full justice to all who complain of such things`

#### F54: units 54.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The text is passive and names no one who must act.

Readings seen:
1. The King is the party bound.
2. An officer of the Crown is the party bound.
3. No one is named, so the rule is a decision function with no party.

Taken: No one is named, so the rule is a decision function that returns the answer for the person (Bar, Entitlement or Obligation) and names no party.

Licensing text (verbatim):
> 54.1: No one shall be arrested or imprisoned upon the appeal of a woman, for the death of any other than her husband.

Rules that encode the chosen reading: `ch 54 -- a person may be arrested or imprisoned upon the appeal`

#### F55a: units 55.1, 55.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: "Shall be entirely remitted, or else it shall be done concerning them according to the decision of the five-and-twenty barons": who chooses between the two.

Readings seen:
1. The King chooses.
2. The twenty-five choose.
3. The text does not say.

Taken: The text does not say: the answer is the Remedy `Remitted entirely, or else dealt with by the five-and-twenty barons`.

Licensing text (verbatim):
> 55.1: All fines made with us unjustly and against the law of the land, and all amercements imposed unjustly and against the law of the land, shall be entirely remitted,
>
> 55.2: or else it shall be done concerning them according to the decision of the five-and-twenty barons of whom mention is made below in the clause for securing the peace, or according to the judgment of the majority of the same,

Rules that encode the chosen reading: `ch 55 -- what is to be done with the fine or amercement`; `ch 55 -- who decides what is done with the fine or amercement`

#### F55b: units 55.3, 55.5

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the archbishop and "such others as he may wish to bring" take part in the decision, and what "the majority of the same" is a majority of.

Readings seen:
1. They decide with the barons.
2. They advise only.

Taken: The Forum names them with the barons; the majority is of the twenty-five (chapter 61.14 has the rule for those present).

Licensing text (verbatim):
> 55.3: along with the aforesaid Stephen, archbishop of Canterbury, if he can be present, and such others as he may wish to bring with him for this purpose,
>
> 55.5: provided always that if any one or more of the aforesaid five-and-twenty barons are in a similar suit, they shall be removed as far as concerns this particular judgment, others being substituted in their places after having been selected by the rest of the same five-and-twenty for this purpose only, and after having been sworn.

Rules that encode the chosen reading: `ch 55 -- who decides what is done with the fine or amercement`; `ch 55 -- the baron may sit in this particular judgment`; `ch 55 -- the substitute may sit in the place of a baron in a similar suit`

#### F56: units 56.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: "Welshmen shall do the same to us and ours": what "the same" is.

Readings seen:
1. Welshmen shall restore to the King and his men what they took without the legal judgment of peers.
2. Welshmen shall give the King's men the same procedure.

Taken: Restoration by Welshmen to the King and his men, a duty of `a Welshman`.

Licensing text (verbatim):
> 56.4: Welshmen shall do the same to us and ours.

Rules that encode the chosen reading: `ch 56 -- the Welshman is to restore to the King and his men`; `ch 56 -- Welshmen shall do the same to us and ours`

#### F57: units 57.1, 57.2, 57.3

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: "The foresaid regions" and "the laws of the Welsh" are not defined.

Readings seen:
1. Wales and the marches.
2. Wales only.

Taken: The laws of the Welsh are the text's own words in the Act; the regions are not asked.

Licensing text (verbatim):
> 57.1: Further, for all those possessions from which any Welshman has, without the lawful judgment of his peers, been disseised or removed by King Henry our father, or King Richard our brother, and which we retain in our hand (or which are possessed by others, to whom we are bound to warrant them) we shall have respite until the usual term of crusaders;
>
> 57.2: excepting those things about which a plea has been raised or an inquest made by our order before we took the cross;
>
> 57.3: but as soon as we return, (or if perchance we desist from our expedition), we will immediately grant full justice in accordance with the laws of the Welsh and in relation to the foresaid regions.

Rules that encode the chosen reading: `ch 57 -- the King has respite for the possession taken from a Welshman`; `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh`; `ch 57 -- as soon as we return we will immediately grant full justice in accordance with the laws of the Welsh`

#### F58: units 58.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who the son of Llywelyn is, and what "immediately" means.

Readings seen:
1. A named person.
2. A class.

Taken: A choice among the three things the text names, or something else.

Licensing text (verbatim):
> 58.1: We will immediately give up the son of Llywelyn and all the hostages of Wales, and the charters delivered to us as security for the peace.

Rules that encode the chosen reading: `ch 58 -- the person or thing is to be given up`; `ch 58 -- we will immediately give up the son of Llywelyn and all the hostages of Wales`

#### F59: units 59.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "in the same manner as we shall do towards our other barons of England" is, and what follows if the charters from William provide otherwise.

Readings seen:
1. The manner is defined elsewhere in the text.
2. It is not stated.

Taken: The text does not state the manner or what the charters provide; the Treatment returned is the text's own phrase, and the charters' content is not covered.

Licensing text (verbatim):
> 59.1: We will do toward Alexander, King of Scots, concerning the return of his sisters and his hostages, and concerning his franchises, and his right, in the same manner as we shall do towards our other barons of England, unless it ought to be otherwise according to the charters which we hold from William his father, formerly King of Scots;

Rules that encode the chosen reading: `ch 59 -- how the King deals with Alexander, King of Scots`; `ch 59 -- we will do toward Alexander, King of Scots, in the same manner as we shall do towards our other barons of England`

#### F60: units 60.1

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who enforces the observance by "all of our kingdom, as well clergy as laymen" towards "their men".

Readings seen:
1. Their lords.
2. The King.
3. No one is named.

Taken: No one is named; the Act is the text's own words and the Party is `a member of the kingdom, clergy or lay`.

Licensing text (verbatim):
> 60.1: Moreover, all the aforesaid customs and liberties, the observance of which we have granted in our kingdom as far as pertains to us towards our men, shall be observed by all of our kingdom, as well clergy as laymen, as far as pertains to them towards their men.

Rules that encode the chosen reading: `ch 60 -- the person must observe the customs and liberties towards his men`; `ch 60 -- the customs and liberties shall be observed by all of our kingdom towards their men`

#### F61a: units 61.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: "Our justiciar" in 61.4 is read as the chief justiciar named in chapters 18 and 41.

Readings seen:
1. The chief justiciar.
2. Another justiciar.

Taken: The King's chief justiciar.

Licensing text (verbatim):
> 61.4: so that if we, or our justiciar, or our bailiffs or any one of our officers, shall in anything be at fault toward anyone, or shall have broken any one of the articles of the peace or of this security, and the offence be notified to four barons of the foresaid five-and-twenty, the said four barons shall repair to us (or our justiciar, if we are out of the realm) and, laying the transgression before us, petition to have that transgression corrected without delay.

Rules that encode the chosen reading: `ch 61 -- the four barons are to repair to the King and petition for the transgression to be corrected`; `ch 61 -- to whom the four barons repair`; `ch 61 -- the said four barons shall repair to us and petition to have that transgression corrected without delay`

#### F61b: units 61.5

Kind: a reading that would change an answer; its units are `fork` rows.

Open: How "within forty days, reckoning from the time it has been intimated" is counted.

Readings seen:
1. The day of intimation is not counted; the fortieth day after it is the last.
2. The day of intimation is day 1.

Taken: The last day is the day of intimation plus 40.

Licensing text (verbatim):
> 61.5: And if we shall not have corrected the transgression (or, in the event of our being out of the realm, if our justiciar shall not have corrected it) within forty days, reckoning from the time it has been intimated to us (or to our justiciar, if we should be out of the realm),

Rules that encode the chosen reading: `ch 61 -- the last day for correcting the transgression`; `ch 61 -- the four barons are to refer the matter to the rest of the five-and-twenty`; `ch 61 -- the four barons aforesaid shall refer that matter to the rest of the five-and-twenty barons`

#### F61c: units 61.7

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "shall ... distrain and distress us" is a duty or only a power of the twenty-five.

Readings seen:
1. A duty (the text's own word, "shall").
2. A power.

Taken: A duty of `the five-and-twenty barons`, ending when redress is obtained as they deem fit.

Licensing text (verbatim):
> 61.7: and those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways, namely, by seizing our castles, lands, possessions, and in any other way they can, until redress has been obtained as they deem fit,

Rules that encode the chosen reading: `ch 61 -- the five-and-twenty barons are to distrain and distress the King`; `ch 61 -- those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways`

#### F61d: units 61.10, 61.11, 61.12

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: How 61.12 (the King compels those who are unwilling of themselves and of their own accord) stands beside 61.11 (the King never forbids anyone to swear).

Readings seen:
1. Both stand: leave to swear, and compulsion of the unwilling.
2. 61.12 is limited to those not forbidden.

Taken: Both stand as written; the person who is unwilling of his own accord is `Obliged` to be compelled.

Licensing text (verbatim):
> 61.10: And let whoever in the country desires it, swear to obey the orders of the said five-and twenty barons for the execution of all the aforesaid matters, and along with them, to molest us to the utmost of his power;
>
> 61.11: and we publicly and freely grant leave to every one who wishes to swear, and we shall never forbid anyone to swear.
>
> 61.12: All those, moreover, in the land who of themselves and of their own accord are unwilling to swear to the twenty-five to help them in constraining and molesting us, we shall by our command compel the same to swear to the effect foresaid.

Rules that encode the chosen reading: `ch 61 -- let whoever in the country desires it swear to obey the orders of the said five-and-twenty barons`; `ch 61 -- the person has the King's leave to swear`; `ch 61 -- we shall never forbid anyone to swear`; `ch 61 -- the person is to be compelled by the King's command to swear`; `ch 61 -- we shall by our command compel the same to swear to the effect foresaid`

#### F61e: units 61.14

Kind: a reading that would change an answer; its units are `fork` rows.

Open: What "the majority of those present" requires, and whether a quorum is needed.

Readings seen:
1. More than half of those present; no quorum.
2. More than half of the twenty-five.

Taken: More than half of those present, with no quorum: one baron present can be a majority, and a tie is not a majority (asserted).

Licensing text (verbatim):
> 61.14: Further, in all matters the execution of which is entrusted to these twenty-five barons, if perchance these twenty-five are present and disagree about anything, or if some of them, after being summoned, are unwilling or unable to be present, that which the majority of those present ordain or command shall be held as fixed and established, exactly as if the whole twenty-five had concurred in this;

Rules that encode the chosen reading: `ch 61 -- what those present ordain or command is held as fixed and established`

#### F61f: units 61.2, 61.3

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Who "the barons" are, and whether the twenty-five are chosen by all barons.

Readings seen:
1. All barons.
2. Some barons.

Taken: The Party `the barons`, and the choice is a MAY.

Licensing text (verbatim):
> 61.2: we give and grant to them the underwritten security, namely, that the barons choose five-and-twenty barons of the kingdom, whomsoever they will,
>
> 61.3: who shall be bound with all their might, to observe and hold, and cause to be observed, the peace and liberties we have granted and confirmed to them by this our present Charter,

Rules that encode the chosen reading: `ch 61 -- the barons choose five-and-twenty barons of the kingdom, whomsoever they will`; `ch 61 -- the five-and-twenty barons shall be bound to observe and hold, and cause to be observed, the peace and liberties`

#### F61g: units 61.8, 61.9

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Whether "saving harmless our own person ..." limits only the seizure of castles and lands or all distress.

Readings seen:
1. All distress.
2. Only the seizure of castles and lands.

Taken: All distress: the Bar and the SHANT speak of harm to those persons in distraining and distressing the King.

Licensing text (verbatim):
> 61.8: saving harmless our own person, and the persons of our queen and children;
>
> 61.9: and when redress has been obtained, they shall resume their old relations towards us.

Rules that encode the chosen reading: `ch 61 -- the person may be harmed in the distraint`; `ch 61 -- saving harmless our own person, and the persons of our queen and children`; `ch 61 -- the five-and-twenty barons are to resume their old relations towards the King`; `ch 61 -- when redress has been obtained, they shall resume their old relations towards us`

#### F61h: units 61.15, 61.16, 61.17

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Whether "let it be void and null" is a rule of the Charter or a statement.

Readings seen:
1. A rule.
2. A statement of a result.

Taken: A Validity decision `Void and null`; the King's SHANT on using it is separate.

Licensing text (verbatim):
> 61.15: and the said twenty-five shall swear that they will faithfully observe all that is aforesaid, and cause it to be observed with all their might.
>
> 61.16: And we shall procure nothing from anyone, directly or indirectly, whereby any part of these concessions and liberties might be revoked or diminished;
>
> 61.17: and if any such thing has been procured, let it be void and null, and we shall never use it personally or by another.

Rules that encode the chosen reading: `ch 61 -- the said twenty-five shall swear that they will faithfully observe all that is aforesaid`; `ch 61 -- we shall procure nothing from anyone, directly or indirectly, whereby any part of these concessions and liberties might be revoked or diminished`; `ch 61 -- the thing procured`; `ch 61 -- we shall never use it personally or by another`

#### F61i: units 61.4

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "notified to four barons of the foresaid five-and-twenty" needs exactly four barons or at least four, and whether notice to fewer than four starts the duty.

Readings seen:
1. At least four: notice that has reached four or more starts the duty.
2. Exactly four: notice to more than four does not start it.

Taken: At least four.  The input is the plain fact `the offence has been notified to four barons of the five-and-twenty`, true when notice has reached four barons or more.  Notice to fewer than four is the text's own no (its "if" is not met), `Not obliged`, and the second pass of 2026-10-30 changed it from `Obligation not covered`.

Licensing text (verbatim):
> 61.4: so that if we, or our justiciar, or our bailiffs or any one of our officers, shall in anything be at fault toward anyone, or shall have broken any one of the articles of the peace or of this security, and the offence be notified to four barons of the foresaid five-and-twenty, the said four barons shall repair to us (or our justiciar, if we are out of the realm) and, laying the transgression before us, petition to have that transgression corrected without delay.

Rules that encode the chosen reading: `ch 61 -- the four barons are to repair to the King and petition for the transgression to be corrected`; `ch 61 -- to whom the four barons repair`; `ch 61 -- the said four barons shall repair to us and petition to have that transgression corrected without delay`

#### F61j: units 61.2, 61.3

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Whether the twenty-five must themselves be barons: "the barons choose five-and-twenty barons of the kingdom, whomsoever they will" names barons, and "whomsoever they will" could let the barons choose a person who is not a baron.

Readings seen:
1. The twenty-five must be barons of the kingdom; "whomsoever they will" says which barons.
2. A non-baron may be chosen: "whomsoever they will" is a free choice and "barons" describes the office.

Taken: The act is the text's own words (`choose five-and-twenty barons of the kingdom, whomsoever they will`) and no function decides whether a given person is eligible, so either reading gives the same answers here.

Licensing text (verbatim):
> 61.2: we give and grant to them the underwritten security, namely, that the barons choose five-and-twenty barons of the kingdom, whomsoever they will,
>
> 61.3: who shall be bound with all their might, to observe and hold, and cause to be observed, the peace and liberties we have granted and confirmed to them by this our present Charter,

Rules that encode the chosen reading: `ch 61 -- the barons choose five-and-twenty barons of the kingdom, whomsoever they will`; `ch 61 -- the five-and-twenty barons shall be bound to observe and hold, and cause to be observed, the peace and liberties`

#### F62: units 62.1, 62.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: The remission is in the past tense ("we have completely remitted and pardoned").

Readings seen:
1. A grant that takes effect now.
2. A report of something already done.

Taken: The entitlement the remission leaves for the person.

Licensing text (verbatim):
> 62.1: And all the ill-will, hatreds, and bitterness that have arisen between us and our men, clergy and lay, from the date of the quarrel, we have completely remitted and pardoned to everyone.
>
> 62.2: Moreover, all trespasses occasioned by the said quarrel, from Easter in the sixteenth year of our reign till the restoration of peace, we have fully remitted to all, both clergy and laymen, and completely forgiven, as far as pertains to us.

Rules that encode the chosen reading: `ch 62 -- the ill-will, hatreds and bitterness are remitted and pardoned`; `ch 62 -- the trespass is fully remitted and completely forgiven, as far as pertains to the King`

#### F62b: units 62.1, 62.2

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Whether "as far as pertains to us" in 62.2 limits the remission to what is the King's to remit, or leaves the remission of all trespasses of the quarrel complete.

Readings seen:
1. It limits the remission to the King's side: a private claim of one person against another is untouched.
2. It is a flourish: the remission is complete as to everyone.

Taken: The King's side: the function is named `... as far as pertains to the King` and returns the person's entitlement against the King.  The encoding has no input for a private claim, so none is addressed, and either reading gives the same answers here.

Licensing text (verbatim):
> 62.1: And all the ill-will, hatreds, and bitterness that have arisen between us and our men, clergy and lay, from the date of the quarrel, we have completely remitted and pardoned to everyone.
>
> 62.2: Moreover, all trespasses occasioned by the said quarrel, from Easter in the sixteenth year of our reign till the restoration of peace, we have fully remitted to all, both clergy and laymen, and completely forgiven, as far as pertains to us.

Rules that encode the chosen reading: `ch 62 -- the ill-will, hatreds and bitterness are remitted and pardoned`; `ch 62 -- the trespass is fully remitted and completely forgiven, as far as pertains to the King`

#### F63: units 63.2

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether the oath in 63.2 ("an oath has been taken") creates a duty or only reports an act, and what "the aforesaid" covers.

Readings seen:
1. A duty on both sides to keep the conditions in good faith.
2. A report of an act that creates no duty.

Taken: A duty on `the King` and `the barons` (the two sides who swore).

Licensing text (verbatim):
> 63.2: An oath, moreover, has been taken, as well on our part as on the part of the barons, that all these conditions aforesaid shall be kept in good faith and without evil intent.

Rules that encode the chosen reading: `ch 63 -- all these conditions shall be kept in good faith and without evil intent`

#### F64a: units 8.1, 8.2, 9.1, 9.2, 9.3, 9.4, 9.5, 10.1, 10.2, 12.1, 12.2, 15.1, 20.1, 20.2, 20.3, 20.4, 20.5, 21.1, 22.1, 22.2, 23.1, 26.2, 33.1, 41.1, 41.2, 41.3, 42.1, 42.2, 44.1, 48.1, 48.2, 48.3, 52.3, 52.4, 53.1, 53.2, 53.3, 54.1, 57.1, 57.2, 61.7

Kind: who is bound, by when, or what a plain input means; no answer changes with the reading, so its units keep the disposition `encoded`.

Open: Which words of the text count as the text saying no.  The rule names "if", "only if", "as long as", "unless", a list closed with "only", and a definition that says "means".

Readings seen:
1. Exactly those words.
2. Those words and their plain variants: "so long as", "while" and "until" for "as long as"; "except", "save", "saving" and "other than" for "unless"; "provided (always) that" for "if"; "need not", which says in terms that nothing is owed.

Taken: The plain variants.  A branch that answers `Not barred`, `Not entitled` or `Not obliged` quotes the word in a `-- FALSE-kind` comment, and `tools/branchcheck.py` fails when the quote holds no accepted word.

Licensing text (verbatim):
> 8.1: Let no widow be compelled to marry, so long as she prefers to live without a husband;
>
> 8.2: provided always that she gives security not to marry without our consent, if she holds of us, or without the consent of the lord of whom she holds, if she holds of another.
>
> 9.1: Neither we nor our bailiffs shall seize any land or rent for any debt, so long as the chattels of the debtor are sufficient to repay the debt;
>
> 9.2: nor shall the sureties of the debtor be distrained so long as the principal debtor is able to satisfy the debt;
>
> 9.3: and if the principal debtor shall fail to pay the debt, having nothing wherewith to pay it, then the sureties shall answer for the debt;
>
> 9.4: and let them have the lands and rents of the debtor, if they desire them, until they are indemnified for the debt which they have paid for him,
>
> 9.5: unless the principal debtor can show proof that he is discharged thereof as against the said sureties.
>
> 10.1: If one who has borrowed from the Jews any sum, great or small, die before that loan be repaid, the debt shall not bear interest while the heir is under age, of whomsoever he may hold;
>
> 10.2: and if the debt fall into our hands, we will not take anything except the principal sum contained in the bond.
>
> 12.1: No scutage nor aid shall be imposed in our kingdom, unless by common counsel of our kingdom, except for ransoming our person, for making our eldest son a knight, and for once marrying our eldest daughter;
>
> 12.2: and for these there shall not be levied more than a reasonable aid.
>
> 15.1: We will not for the future grant to any one licence to take an aid from his own free tenants, except to ransom his body, to make his eldest son a knight, and once to marry his eldest daughter;
>
> 20.1: A freeman shall not be amerced for a small offence, except in accordance with the degree of the offence;
>
> 20.2: and for a grave offence he shall be amerced in accordance with the gravity of his offence, yet saving always his “contenement”;
>
> 20.3: and a merchant in the same way, saving his wares;
>
> 20.4: and a villein shall be amerced in the same way, saving his wainage—if they have fallen into our mercy:
>
> 20.5: and none of the aforesaid amercements shall be imposed except by the oath of honest men of the neighbourhood.
>
> 21.1: Earls and barons shall not be amerced except through their peers, and only in accordance with the degree of the offence.
>
> 22.1: A clerk shall not be amerced in respect of his lay holding except after the manner of the others aforesaid;
>
> 22.2: further, he shall not be amerced in accordance with the extent of his church benefice.
>
> 23.1: No community or individual shall be compelled to make bridges at river banks, except those who from of old were legally bound to do so.
>
> 26.2: provided always that nothing whatever be thence removed until the debt which is evident shall be fully paid to us;
>
> 33.1: All kydells for the future shall be removed altogether from Thames and Medway, and throughout all England, except upon the sea coast.
>
> 41.1: All merchants shall have safe and secure exit from England, and entry to England, with the right to tarry there and to move about as well by land as by water, for buying and selling by the ancient and right customs, quit from all evil tolls,
>
> 41.2: except (in time of war) such merchants as are of the land at war with us.
>
> 41.3: And if such are found in our land at the beginning of the war, they shall be detained, without injury to their bodies or goods, until information be received by us, or by our chief justiciar, how the merchants of our land found in the land at war with us are treated;
>
> 42.1: It shall be lawful in future for any one (excepting always those imprisoned or outlawed in accordance with the law of the kingdom, and natives of any country at war with us, and merchants, who shall be treated as is above provided) to leave our kingdom and to return, safe and secure by land and water,
>
> 42.2: except for a short period in time of war, on grounds of public policy—
>
> 44.1: Men who dwell without the forest need not henceforth come before our justiciars of the forest upon a general summons, except those who are impleaded, or who have become sureties for any person or persons attached for forest offences.
>
> 48.1: All evil customs connected with forests and warrens, foresters and warreners, sheriffs and their officers, river-banks and their wardens, shall immediately be inquired into in each county by twelve sworn knights of the same county chosen by the honest men of the same county,
>
> 48.2: and shall, within forty days of the said inquest, be utterly abolished, so as never to be restored,
>
> 48.3: provided always that we previously have intimation thereof, or our justiciar, if we should not be in England.
>
> 52.3: Moreover, for all those possessions, from which any one has, without the lawful judgment of his peers, been disseised or removed, by our father, King Henry, or by our brother, King Richard, and which we retain in our hand (or which are possessed by others, to whom we are bound to warrant them) we shall have respite until the usual term of crusaders;
>
> 52.4: excepting those things about which a plea has been raised, or an inquest made by our order, before our taking of the cross;
>
> 53.1: We shall have, moreover, the same respite and in the same manner in rendering justice concerning the disafforestation or retention of those forests which Henry our father and Richard our brother afforested,
>
> 53.2: and concerning the wardship of lands which are of the fief of another (namely, such wardships as we have hitherto had by reason of a fief which anyone held of us by knight’s service),
>
> 53.3: and concerning abbeys founded on other fiefs than our own, in which the lord of the fee claims to have right;
>
> 54.1: No one shall be arrested or imprisoned upon the appeal of a woman, for the death of any other than her husband.
>
> 57.1: Further, for all those possessions from which any Welshman has, without the lawful judgment of his peers, been disseised or removed by King Henry our father, or King Richard our brother, and which we retain in our hand (or which are possessed by others, to whom we are bound to warrant them) we shall have respite until the usual term of crusaders;
>
> 57.2: excepting those things about which a plea has been raised or an inquest made by our order before we took the cross;
>
> 61.7: and those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways, namely, by seizing our castles, lands, possessions, and in any other way they can, until redress has been obtained as they deem fit,

Rules that encode the chosen reading: `ch 8 -- the widow may be compelled to marry`; `ch 8 -- the consent her security is against`; `ch 9 -- land or rent may be seized for the debt`; `ch 9 -- neither the King nor his bailiffs shall seize land or rent for a debt while the chattels suffice`; `ch 9 -- the sureties of the debtor may be distrained`; `ch 9 -- the sureties answer for the debt`; `ch 9 -- the sureties shall answer for the debt if the principal debtor fails and has nothing wherewith to pay`; `ch 9 -- the surety may have the lands and rents of the debtor`; `ch 9 -- the sureties may have the lands and rents of the debtor until they are indemnified`; `ch 10 -- the debt may bear interest`; `ch 10 -- the King may take this sum of the debt`; `ch 10 -- the King will take nothing but the principal sum of a debt fallen into his hands`; `ch 12 -- the levy is an aid for one of the three purposes`; `ch 12 -- the levy needs the common counsel of the kingdom`; `ch 12 -- a scutage or aid may be imposed`; `ch 15 -- the King may grant a licence to take an aid from a lord's own free tenants`; `ch 15 -- the King will not grant a licence to take an aid from a lord's own free tenants, except for the three purposes`; `ch 20 -- the amercement may be imposed`; `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 21 -- the earl or baron may be amerced in this way`; `ch 22 -- the clerk may be amerced in this way`; `ch 23 -- a community or individual may be compelled to make a bridge at a river bank`; `ch 26 -- the attached chattels may be removed from the lay fief`; `ch 33 -- the kydell is to be removed`; `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant`; `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured`; `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water`; `ch 44 -- the man must come before the justiciars of the forest upon a general summons`; `ch 48 -- the evil custom is to be inquired into`; `ch 48 -- the inquest is constituted as the text requires`; `ch 48 -- the last day for abolishing the evil custom`; `ch 48 -- the evil custom is to be utterly abolished`; `ch 48 -- abolition on this day is within the forty days`; `ch 48 -- the abolished custom may be restored`; `ch 52 -- the King has respite for the possession`; `ch 53 -- the King has the same respite concerning the matter`; `ch 54 -- a person may be arrested or imprisoned upon the appeal`; `ch 57 -- the King has respite for the possession taken from a Welshman`; `ch 61 -- the five-and-twenty barons are to distrain and distress the King`; `ch 61 -- those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways`

#### F64b: units 4.1, 12.2, 16.1, 18.1, 32.1, 43.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether a limit the text states without the word "only" closes the matter, so that what is inside the limit is not barred: "nothing but" (4.1), "not ... more than" (12.2), "greater service ... than is due" (16.1), "elsewhere than" (18.1), "beyond one year and one day" (32.1), "no other ... than" (43.1).

Readings seen:
1. Each is a closed list or a ceiling, and what is inside it is `Not barred`.
2. Only the word "only" closes a list; inside the limit the answer is `Bar not covered`.

Taken: Each is a closed limit.  The limit is the text's own statement of how far the bar reaches, and inside it the answer is `Not barred`.

Licensing text (verbatim):
> 4.1: The guardian of the land of an heir who is thus under age, shall take from the land of the heir nothing but reasonable produce, reasonable customs, and reasonable services, and that without destruction or waste of men or goods;
>
> 12.2: and for these there shall not be levied more than a reasonable aid.
>
> 16.1: No one shall be compelled to perform greater service for a knight’s fee, or for any other free tenement, than is due therefrom.
>
> 18.1: Inquests of novel disseisin, of mort d’ancestor, and of darrein presentment, shall not be held elsewhere than in their own county-courts, and that in manner following,—
>
> 32.1: We will not retain beyond one year and one day, the lands of those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.
>
> 43.1: If one who holds of some escheat (such as the honour of Wallingford, of Nottingham, of Boulogne, of Lancaster, or of other escheats which are in our hands and are baronies) shall die, his heir shall give no other relief, and perform no other service to us than he would have done to the baron, if that barony had been in the baron’s hand;

Rules that encode the chosen reading: `ch 4 -- the guardian may take this from the heir's land`; `ch 4 -- the guardian shall take from the land nothing but reasonable produce, customs and services`; `ch 4 -- the guardian shall not make destruction or waste of men or goods`; `ch 12 -- a scutage or aid may be imposed`; `ch 16 -- greater service than is due may be demanded`; `ch 18 -- the inquest may be held here`; `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs`; `ch 43 -- the King may take this relief and service from the heir`; `ch 43 -- his heir shall give no other relief and perform no other service to us than he would have done to the baron`

#### F64c: units 2.1, 6.1, 7.3, 17.1, 19.1, 22.1, 22.2, 25.1, 26.1, 28.1, 29.1, 30.1, 31.1, 32.1, 35.1, 35.2, 35.3, 35.4, 35.5, 38.1, 41.1, 41.2, 43.1, 46.1, 51.1, 52.5, 53.4, 55.5, 57.3, 60.1, 61.9

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Where the text states what is required, permitted or owed in other words ("on payment of", "without disparagement", "against the will of", "shall remain at", "shall be held in", "when", "as soon as", "thereafter", "as far as", "as many as", "for this purpose only"), whether the case that meets the requirement, or falls outside the stated time, is a "no".

Readings seen:
1. Yes: the stated requirement is a condition, and failing or exceeding it is a no.
2. No: the text states what bars, permits or requires; it does not say in the words of the rule that the opposite case is not barred, entitled or obliged.

Taken: No.  Those cases answer `Bar not covered`, `Entitlement not covered` or `Obligation not covered`, each branch carrying a `-- NOTHING-kind (silent)` comment.  A first version of this encoding answered `Not barred`, `Not entitled` or `Not obliged` on these facts in 24 functions, and answered FALSE in one more (7.3, the forty days); all 25 were changed when the rule for a source that does not answer was refined.  The module tests were re-derived from the rule and the text after a first run showed which 37 assertions expected a "no" there (each moved to the matching "not covered" value and to nothing else); the seat cases were rewritten before they were run.

Licensing text (verbatim):
> 2.1: If any of our earls or barons, or others holding of us in chief by military service shall have died, and at the time of his death his heir shall be of full age and owe “relief,” he shall have his inheritance on payment of the ancient relief, namely
>
> 6.1: Heirs shall be married without disparagement, yet so that before the marriage takes place the nearest in blood to that heir shall have notice.
>
> 7.3: and she may remain in the house of her husband for forty days after his death,
>
> 17.1: Common pleas shall not follow our court, but shall be held in some fixed place.
>
> 19.1: And if any of the said assizes cannot be taken on the day of the county court, let there remain of the knights and freeholders who were present at the county court on that day, as many as may be required for the efficient making of judgments, according as the business be more or less.
>
> 22.1: A clerk shall not be amerced in respect of his lay holding except after the manner of the others aforesaid;
>
> 22.2: further, he shall not be amerced in accordance with the extent of his church benefice.
>
> 25.1: All counties, hundreds, wapentakes, and trithings (except our demesne manors) shall remain at the old rents, and without any additional payment.
>
> 26.1: If any one holding of us a lay fief shall die, and our sheriff or bailiff shall exhibit our letters patent of summons for a debt which the deceased owed to us, it shall be lawful for our sheriff or bailiff to attach and catalogue chattels of the deceased, found upon the lay fief, to the value of that debt, at the sight of lawful men,
>
> 28.1: No constable or other bailiff of ours shall take corn or other provisions from any one without immediately tendering money therefor, unless he can have postponement thereof by permission of the seller.
>
> 29.1: No constable shall compel any knight to give money in lieu of castle-guard, when he is willing to perform it in his own person, or (if he himself cannot do it from any reasonable cause) then by another responsible man.
>
> 30.1: No sheriff or bailiff of ours, or any other person, shall take the horses or carts of any freeman for transport duty, against the will of the said freeman.
>
> 31.1: Neither we nor our bailiffs shall take, for our castles or for any other work of ours, wood which is not ours, against the will of the owner of that wood.
>
> 32.1: We will not retain beyond one year and one day, the lands of those who have been convicted of felony, and the lands shall thereafter be handed over to the lords of the fiefs.
>
> 35.1: Let there be one measure of wine throughout our whole realm;
>
> 35.2: and one measure of ale;
>
> 35.3: and one measure of corn, to wit, “the London quarter”;
>
> 35.4: and one width of cloth (whether dyed, or russet, or halberget), to wit, two ells within the selvedges;
>
> 35.5: of weights also let it be as of measures.
>
> 38.1: No bailiff for the future shall put any man to his “law” upon his own mere word of mouth, without credible witnesses brought for this purpose.
>
> 41.1: All merchants shall have safe and secure exit from England, and entry to England, with the right to tarry there and to move about as well by land as by water, for buying and selling by the ancient and right customs, quit from all evil tolls,
>
> 41.2: except (in time of war) such merchants as are of the land at war with us.
>
> 43.1: If one who holds of some escheat (such as the honour of Wallingford, of Nottingham, of Boulogne, of Lancaster, or of other escheats which are in our hands and are baronies) shall die, his heir shall give no other relief, and perform no other service to us than he would have done to the baron, if that barony had been in the baron’s hand;
>
> 46.1: All barons who have founded abbeys, concerning which they hold charters from the kings of England, or of which they have long-continued possession, shall have the wardship of them, when vacant, as they ought to have.
>
> 51.1: As soon as peace is restored, we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants, and mercenary soldiers, who have come with horses and arms to the kingdom’s hurt.
>
> 52.5: but as soon as we return from our expedition (or if perchance we desist from the expedition) we will immediately grant full justice therein.
>
> 53.4: and when we have returned, or if we desist from our expedition, we will immediately grant full justice to all who complain of such things.
>
> 55.5: provided always that if any one or more of the aforesaid five-and-twenty barons are in a similar suit, they shall be removed as far as concerns this particular judgment, others being substituted in their places after having been selected by the rest of the same five-and-twenty for this purpose only, and after having been sworn.
>
> 57.3: but as soon as we return, (or if perchance we desist from our expedition), we will immediately grant full justice in accordance with the laws of the Welsh and in relation to the foresaid regions.
>
> 60.1: Moreover, all the aforesaid customs and liberties, the observance of which we have granted in our kingdom as far as pertains to us towards our men, shall be observed by all of our kingdom, as well clergy as laymen, as far as pertains to them towards their men.
>
> 61.9: and when redress has been obtained, they shall resume their old relations towards us.

Rules that encode the chosen reading: `ch 2 -- the holder is one of those this chapter speaks of`; `ch 2 -- the heir has his inheritance on payment of the ancient relief`; `ch 6 -- the heir may be married in this way`; `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- the widow may remain in her husband's house`; `ch 17 -- the common plea may be held where the King's court happens to be`; `ch 19 -- enough of the knights and freeholders present remain`; `ch 19 -- the knight or freeholder who was present remains`; `ch 22 -- the clerk may be amerced in this way`; `ch 25 -- the rent or payment demanded of this unit may be demanded`; `ch 26 -- the officer may attach and catalogue chattels of the deceased`; `ch 26 -- the sheriff or bailiff may attach and catalogue chattels to the value of the debt`; `ch 28 -- the officer may take corn or other provisions in this way`; `ch 28 -- no constable or other bailiff shall take corn or other provisions without immediately tendering money`; `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard`; `ch 29 -- no constable shall compel a knight to give money in lieu of castle-guard`; `ch 30 -- horses or carts may be taken for transport duty`; `ch 30 -- no sheriff or bailiff or other person shall take the horses or carts of a freeman for transport duty against his will`; `ch 31 -- wood may be taken for the King's castles or other work`; `ch 31 -- neither the King nor his bailiffs shall take wood which is not the King's against the will of the owner`; `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs`; `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used`; `ch 38 -- the officer may put a man to his law upon his own mere word of mouth`; `ch 38 -- no bailiff shall put any man to his law upon his own mere word of mouth, without credible witnesses`; `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant`; `ch 43 -- the King may take this relief and service from the heir`; `ch 43 -- his heir shall give no other relief and perform no other service to us than he would have done to the baron`; `ch 46 -- the baron shall have the wardship of the abbey`; `ch 51 -- the person is to be banished from the kingdom`; `ch 51 -- we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants and mercenary soldiers who have come with horses and arms to the kingdom's hurt`; `ch 52 -- full justice is to be granted for the possession`; `ch 52 -- as soon as we return from our expedition we will immediately grant full justice therein`; `ch 53 -- full justice is to be granted to the person who complains`; `ch 53 -- when we have returned we will immediately grant full justice to all who complain of such things`; `ch 55 -- the baron may sit in this particular judgment`; `ch 55 -- the substitute may sit in the place of a baron in a similar suit`; `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh`; `ch 57 -- as soon as we return we will immediately grant full justice in accordance with the laws of the Welsh`; `ch 60 -- the person must observe the customs and liberties towards his men`; `ch 60 -- the customs and liberties shall be observed by all of our kingdom towards their men`; `ch 61 -- the five-and-twenty barons are to resume their old relations towards the King`; `ch 61 -- when redress has been obtained, they shall resume their old relations towards us`

#### F64d: units 29.1, 46.1

Kind: a reading that would change an answer; its units are `fork` rows.

Open: Whether "when" works as "if": "when he is willing to perform it in his own person, or (if he himself cannot do it from any reasonable cause) then by another responsible man" (29.1) and "shall have the wardship of them, when vacant, as they ought to have" (46.1).

Readings seen:
1. "When" says at what time or in what case the rule applies, and is not one of the words that make the text say no: where it is not met the text is silent.
2. "When" works as "if": where it is not met the text's no follows (a constable may compel a knight who is not willing and has no substitute; a baron has no wardship of an abbey that is not vacant).

Taken: The first, as F64c: those cases answer `Bar not covered` and `Entitlement not covered`.  The other reading is the second; a lawyer who takes it turns those two branches into `Not barred` and `Not entitled`.

Licensing text (verbatim):
> 29.1: No constable shall compel any knight to give money in lieu of castle-guard, when he is willing to perform it in his own person, or (if he himself cannot do it from any reasonable cause) then by another responsible man.
>
> 46.1: All barons who have founded abbeys, concerning which they hold charters from the kings of England, or of which they have long-continued possession, shall have the wardship of them, when vacant, as they ought to have.

Rules that encode the chosen reading: `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard`; `ch 29 -- no constable shall compel a knight to give money in lieu of castle-guard`; `ch 46 -- the baron shall have the wardship of the abbey`

#### F64e: units 2.1, 3.1, 9.2, 9.3, 10.1, 10.2, 11.2, 11.4, 20.1, 20.2, 20.3, 20.4, 20.5, 25.1, 26.4, 27.1, 29.2, 37.1, 37.2, 37.3, 41.3, 61.13

Kind: a reading that would change an answer; its units are `fork` rows.

Open: When a sentence is conditioned by "if", "while", "until", "unless" or "except", which failing limb is the text's no: a fact the clause makes the condition (the debtor died, the heir was under age, the debt fell into the King's hands, information was received), or also the class of person or thing the clause speaks of (the Jews' debtor, a holder in chief by military service, an officer other than a sheriff or bailiff).

Readings seen:
1. Every failing limb: a person or thing outside the class the clause speaks of also gets the no.
2. Only the fact limbs; a person or thing outside the class is outside the sentence, and the text does not say.

Taken: Only the fact limbs, in 15 functions that the sweep of 2026-10-30 changed; the units above are theirs.  A failing class, identity or scope limb gives `... not covered`, and that branch carries `-- NOTHING-kind (word not the condition here: <the word> because <one sentence>)`, which `tools/branchcheck.py` requires wherever the function's source holds one of the words.  A lawyer who takes the first reading turns those class branches into `Not barred`, `Not entitled` and `Not obliged`.

Licensing text (verbatim):
> 2.1: If any of our earls or barons, or others holding of us in chief by military service shall have died, and at the time of his death his heir shall be of full age and owe “relief,” he shall have his inheritance on payment of the ancient relief, namely
>
> 3.1: If, however, the heir of any one of the aforesaid has been under age and in wardship, let him have his inheritance without relief and without fine when he comes of age.
>
> 9.2: nor shall the sureties of the debtor be distrained so long as the principal debtor is able to satisfy the debt;
>
> 9.3: and if the principal debtor shall fail to pay the debt, having nothing wherewith to pay it, then the sureties shall answer for the debt;
>
> 10.1: If one who has borrowed from the Jews any sum, great or small, die before that loan be repaid, the debt shall not bear interest while the heir is under age, of whomsoever he may hold;
>
> 10.2: and if the debt fall into our hands, we will not take anything except the principal sum contained in the bond.
>
> 11.2: and if any children of the deceased are left under age, necessaries shall be provided for them in keeping with the holding of the deceased;
>
> 11.4: in like manner let it be done touching debts due to others than Jews.
>
> 20.1: A freeman shall not be amerced for a small offence, except in accordance with the degree of the offence;
>
> 20.2: and for a grave offence he shall be amerced in accordance with the gravity of his offence, yet saving always his “contenement”;
>
> 20.3: and a merchant in the same way, saving his wares;
>
> 20.4: and a villein shall be amerced in the same way, saving his wainage—if they have fallen into our mercy:
>
> 20.5: and none of the aforesaid amercements shall be imposed except by the oath of honest men of the neighbourhood.
>
> 25.1: All counties, hundreds, wapentakes, and trithings (except our demesne manors) shall remain at the old rents, and without any additional payment.
>
> 26.4: and if there be nothing due from him to us, all the chattels shall go to the deceased, saving to his wife and children their reasonable shares.
>
> 27.1: If any freeman shall die intestate, his chattels shall be distributed by the hands of his nearest kinsfolk and friends, under the supervision of the church, saving to every one the debts which the deceased owed to him.
>
> 29.2: Further, if we have led or sent him upon military service, he shall be relieved from guard in proportion to the time during which he has been on service because of us.
>
> 37.1: If anyone holds of us by fee-farm, by socage, or by burgage, and holds also land of another lord by knight’s service, we will not (by reason of that fee-farm, socage, or burgage,) have the wardship of the heir, or of such land of his as is of the fief of that other;
>
> 37.2: nor shall we have wardship of that fee-farm, socage, or burgage, unless such fee-farm owes knight’s service.
>
> 37.3: We will not by reason of any petty serjeanty which anyone may hold of us by the service of rendering to us knives, arrows, or the like, have wardship of his heir or of the land which he holds of another lord by knight’s service.
>
> 41.3: And if such are found in our land at the beginning of the war, they shall be detained, without injury to their bodies or goods, until information be received by us, or by our chief justiciar, how the merchants of our land found in the land at war with us are treated;
>
> 61.13: And if any one of the five-and-twenty barons shall have died or departed from the land, or be incapacitated in any other manner which would prevent the foresaid provisions being carried out, those of the said twenty-five barons who are left shall choose another in his place according to their own judgment, and he shall be sworn in the same way as the others.

Rules that encode the chosen reading: `ch 2 -- the holder is one of those this chapter speaks of`; `ch 2 -- the heir has his inheritance on payment of the ancient relief`; `ch 3 -- relief or a fine may be demanded of the heir on coming of age`; `ch 3 -- the heir shall have his inheritance without relief and without fine`; `ch 9 -- the sureties of the debtor may be distrained`; `ch 9 -- the sureties answer for the debt`; `ch 9 -- the sureties shall answer for the debt if the principal debtor fails and has nothing wherewith to pay`; `ch 10 -- the debt may bear interest`; `ch 10 -- the King may take this sum of the debt`; `ch 10 -- the King will take nothing but the principal sum of a debt fallen into his hands`; `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased`; `ch 11 -- the wife has her dower and pays nothing of the debt`; `ch 11 -- the amount of the debt paid out of the residue`; `ch 20 -- the amercement may be imposed`; `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 25 -- the rent or payment demanded of this unit may be demanded`; `ch 26 -- the wife and children have their reasonable shares`; `ch 27 -- how the chattels are distributed`; `ch 27 -- the nearest kinsfolk and friends shall distribute the chattels of a freeman who died intestate`; `ch 27 -- the debt which the deceased owed to a person is saved to him`; `ch 29 -- the knight is relieved from guard in proportion to his time on service`; `ch 29 -- the days of guard of which the knight is relieved`; `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure`; `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured`; `ch 61 -- another baron is to be chosen in his place`; `ch 61 -- those of the said twenty-five barons who are left shall choose another in his place according to their own judgment`


## Jural relations

One or more rows for each operative provision, in Hohfeld's terms.
Each relation is stated once, neutrally, between two parties; where the text names no one the cell says so and cites the fork.
`none` is for definitions, limits on another provision's relation, and restatements.

| Provision | Holder | Correlative party | Relation | L4 rule |
| --- | --- | --- | --- | --- |
| 1.1 | the English church | the King | claim-right / duty | `ch 1 -- the English church shall be free, with her rights entire and her liberties inviolate` |
| 1.2 | none (restates 1.1) | none | none | none |
| 1.4 | the English church (elections) | the King | claim-right / duty | `ch 1 -- the freedom of elections of the English church shall be observed` |
| 1.5 | freemen of the kingdom and their heirs | the King | claim-right / duty | `ch 1 -- the person holds the liberties granted in this Charter` |
| 2.1 | the heir of a holder in chief | not named by the text (fork F1: the King) | claim-right / duty | `ch 2 -- the holder is one of those this chapter speaks of`; `ch 2 -- the heir has his inheritance on payment of the ancient relief` |
| 2.2 | none (defines the relief in 2.1) | none | none | none |
| 2.3 | none (defines the relief in 2.1) | none | none | none |
| 2.4 | none (defines the relief in 2.1) | none | none | none |
| 2.5 | none (defines the relief in 2.1) | none | none | none |
| 3.1 | the heir who was a ward | the King (fork F3) | claim-right / duty | `ch 3 -- relief or a fine may be demanded of the heir on coming of age`; `ch 3 -- the heir shall have his inheritance without relief and without fine` |
| 4.1 | the heir under age | the guardian | claim-right / duty | `ch 4 -- the guardian may take this from the heir's land`; `ch 4 -- the guardian shall take from the land nothing but reasonable produce, customs and services`; `ch 4 -- the guardian shall not make destruction or waste of men or goods` |
| 4.2 | the King | the guardian committed by the King to the sheriff or another accountable to him | power / liability | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` |
| 4.3 | the King | the two lawful and discreet men of that fee | claim-right / duty | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` |
| 4.4 | not named by the text (fork F4) | the guardian to whom the King gave or sold the wardship | power / liability | `ch 4 -- the consequence for a guardian of this kind who has made waste`; `ch 4 -- what follows if the guardian lays waste` |
| 5.1 | the heir under age | the guardian | claim-right / duty | `ch 5 -- the guardian shall keep up the houses, parks, fishponds, mills and other things out of the issues of the land` |
| 5.2 | the heir who has come to full age | the guardian | claim-right / duty | `ch 5 -- the guardian shall restore the land to the heir who has come to full age`; `ch 5 -- the restoration is what the Charter requires` |
| 6.1 | the heir | not named by the text (fork F6) | claim-right / duty | `ch 6 -- the heir may be married in this way` |
| 6.1 | the nearest in blood to the heir | not named by the text (fork F6) | claim-right / duty | `ch 6 -- the heir may be married in this way` |
| 7.1 | the widow | not named by the text (fork F7) | claim-right / duty | `ch 7 -- the widow may be kept waiting or put to difficulty over her marriage portion and inheritance` |
| 7.2 | the widow | not named by the text (fork F7) | immunity / disability | `ch 7 -- the widow may be made to give this` |
| 7.3 | the widow | not named by the text (fork F7) | liberty / no-claim | `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- the widow may remain in her husband's house` |
| 7.4 | the widow | not named by the text (fork F7) | claim-right / duty | `ch 7 -- the number of days the widow may remain in her husband's house, within which her dower is assigned`; `ch 7 -- her dower is assigned within the forty days` |
| 8.1 | the widow | not named by the text (fork F8) | immunity / disability | `ch 8 -- the widow may be compelled to marry` |
| 8.2 | the King, or the lord of whom she holds | the widow | claim-right / duty | `ch 8 -- the widow may be compelled to marry`; `ch 8 -- the consent her security is against` |
| 9.1 | the debtor | the King and his bailiffs | claim-right / duty | `ch 9 -- land or rent may be seized for the debt`; `ch 9 -- neither the King nor his bailiffs shall seize land or rent for a debt while the chattels suffice` |
| 9.2 | the sureties of the debtor | not named by the text (fork F9) | claim-right / duty | `ch 9 -- the sureties of the debtor may be distrained`; `ch 9 -- the sureties answer for the debt` |
| 9.3 | not named by the text (the creditor) | the sureties | claim-right / duty | `ch 9 -- the sureties answer for the debt`; `ch 9 -- the sureties shall answer for the debt if the principal debtor fails and has nothing wherewith to pay` |
| 9.4 | the sureties who paid | the principal debtor | liberty / no-claim | `ch 9 -- the surety may have the lands and rents of the debtor`; `ch 9 -- the sureties may have the lands and rents of the debtor until they are indemnified` |
| 9.5 | none (limits 9.4) | none | none | none |
| 10.1 | the heir under age of the borrower | the lender (the Jews) | claim-right / duty | `ch 10 -- the debt may bear interest` |
| 10.2 | the debtor | the King | claim-right / duty | `ch 10 -- the King may take this sum of the debt`; `ch 10 -- the King will take nothing but the principal sum of a debt fallen into his hands` |
| 11.1 | the wife | not named by the text (fork F11) | claim-right / duty | `ch 11 -- the wife has her dower and pays nothing of the debt` |
| 11.2 | the children under age | not named by the text (fork F11) | claim-right / duty | `ch 11 -- necessaries shall be provided for the children under age, in keeping with the holding of the deceased` |
| 11.3 | not named by the text (the creditor) | not named by the text (fork F11) | claim-right / duty | `ch 11 -- the amount of the debt paid out of the residue`; `ch 11 -- the payment of the debt may be made at the expense of service due to feudal lords` |
| 11.4 | none (extends 11.1 to 11.3 to other creditors; stated once above) | none | none | none |
| 12.1 | the subject of the kingdom | the King | immunity / disability | `ch 12 -- the levy is an aid for one of the three purposes`; `ch 12 -- the levy needs the common counsel of the kingdom`; `ch 12 -- a scutage or aid may be imposed` |
| 12.2 | the person asked for an aid | the King | claim-right / duty | `ch 12 -- a scutage or aid may be imposed` |
| 12.3 | the citizens of London | the King | claim-right / duty | `ch 12 -- an aid from the citizens of London may be imposed` |
| 13.1 | the citizens of London | not named by the text (fork F13) | claim-right / duty | `ch 13 -- the citizens of London have all their ancient liberties and free customs, by land and by water` |
| 13.2 | other cities, boroughs, towns and ports | not named by the text (fork F13) | claim-right / duty | `ch 13 -- all other cities, boroughs, towns and ports have all their liberties and free customs` |
| 14.1 | the archbishops, bishops, abbots, earls and greater barons | the King | claim-right / duty | `ch 14 -- the King will cause the archbishops, bishops, abbots, earls and greater barons to be summoned by letters under seal`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` |
| 14.2 | all others who hold of the King in chief | the King | claim-right / duty | `ch 14 -- the King will cause all others who hold of him in chief to be summoned generally`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` |
| 14.3 | those summoned | the King | claim-right / duty | `ch 14 -- the King will specify the reason of the summons in all letters of summons`; `ch 14 -- the least number of days between the summons and the date fixed`; `ch 14 -- the summons for the common counsel is as the Charter requires` |
| 14.4 | those of the summoned who are present | those summoned who did not come | power / liability | `ch 14 -- the business proceeds on the day appointed according to the counsel of those present` |
| 15.1 | a lord's free tenants | the King | claim-right / duty | `ch 15 -- the King may grant a licence to take an aid from a lord's own free tenants`; `ch 15 -- the King will not grant a licence to take an aid from a lord's own free tenants, except for the three purposes` |
| 15.2 | a lord's free tenants | the lord who takes the aid (fork F15) | claim-right / duty | `ch 15 -- the aid levied by a lord on one of the three occasions may be this aid` |
| 16.1 | the holder of a knight's fee or other free tenement | not named by the text (fork F16) | claim-right / duty | `ch 16 -- greater service than is due may be demanded` |
| 17.1 | the parties to a common plea | not named by the text (fork F17) | claim-right / duty | `ch 17 -- the common plea may be held where the King's court happens to be` |
| 18.1 | the parties to the inquests | not named by the text (fork F18) | claim-right / duty | `ch 18 -- the inquest may be held here` |
| 18.2 | the county | the King, or the chief justiciar while the King is out of the realm | claim-right / duty | `ch 18 -- two justiciars will be sent through every county four times a year`; `ch 18 -- the justiciars were sent through the county often enough`; `ch 18 -- the assizes are held as the Charter requires` |
| 19.1 | not named by the text (fork F19) | the knights and freeholders present at the county court | claim-right / duty | `ch 19 -- enough of the knights and freeholders present remain`; `ch 19 -- the knight or freeholder who was present remains` |
| 20.1 | a freeman | not named by the text (fork F20) | claim-right / duty | `ch 20 -- the amercement may be imposed` |
| 20.2 | a freeman | not named by the text (fork F20) | claim-right / duty | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` |
| 20.3 | a merchant | not named by the text (fork F20) | claim-right / duty | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` |
| 20.4 | a villein | not named by the text (fork F20) | claim-right / duty | `ch 20 -- what is saved to a person of this class when he is amerced`; `ch 20 -- the amercement may be imposed` |
| 20.5 | the person amerced | not named by the text (fork F20) | claim-right / duty | `ch 20 -- the amercement may be imposed` |
| 21.1 | earls and barons | not named by the text (fork F20) | claim-right / duty | `ch 21 -- the earl or baron may be amerced in this way` |
| 22.1 | a clerk | not named by the text (fork F22) | claim-right / duty | `ch 22 -- the clerk may be amerced in this way` |
| 22.2 | a clerk | not named by the text (fork F22) | claim-right / duty | `ch 22 -- the clerk may be amerced in this way` |
| 23.1 | a community or individual | not named by the text | immunity / disability | `ch 23 -- a community or individual may be compelled to make a bridge at a river bank` |
| 24.1 | the King (pleas of the Crown) | a sheriff, constable, coroner or other bailiff | immunity / disability | `ch 24 -- the officer may hold pleas of the Crown`; `ch 24 -- no sheriff, constable, coroner or other bailiff shall hold pleas of the Crown` |
| 25.1 | counties, hundreds, wapentakes and trithings | not named by the text (fork F25) | claim-right / duty | `ch 25 -- the rent or payment demanded of this unit may be demanded` |
| 26.1 | the King's sheriff or bailiff | the holder of the deceased's chattels (executors, heirs) | power / liability | `ch 26 -- the officer may attach and catalogue chattels of the deceased`; `ch 26 -- the sheriff or bailiff may attach and catalogue chattels to the value of the debt` |
| 26.2 | the deceased's estate | not named by the text (fork F26) | claim-right / duty | `ch 26 -- the attached chattels may be removed from the lay fief` |
| 26.3 | the executors | not named by the text (fork F26) | claim-right / duty | `ch 26 -- the value of the residue left to the executors` |
| 26.4 | the wife and children | not named by the text (fork F26) | claim-right / duty | `ch 26 -- the wife and children have their reasonable shares` |
| 27.1 | a person to whom the deceased owed a debt | the nearest kinsfolk and friends who distribute | claim-right / duty | `ch 27 -- how the chattels are distributed`; `ch 27 -- the nearest kinsfolk and friends shall distribute the chattels of a freeman who died intestate`; `ch 27 -- the debt which the deceased owed to a person is saved to him` |
| 28.1 | the seller | a constable or other bailiff of the King | claim-right / duty | `ch 28 -- the officer may take corn or other provisions in this way`; `ch 28 -- no constable or other bailiff shall take corn or other provisions without immediately tendering money` |
| 29.1 | the knight | a constable | claim-right / duty | `ch 29 -- the constable may compel the knight to give money in lieu of castle-guard`; `ch 29 -- no constable shall compel a knight to give money in lieu of castle-guard` |
| 29.2 | the knight | not named by the text (fork F29) | claim-right / duty | `ch 29 -- the knight is relieved from guard in proportion to his time on service`; `ch 29 -- the days of guard of which the knight is relieved` |
| 30.1 | a freeman | a sheriff or bailiff of the King, or any other person | claim-right / duty | `ch 30 -- horses or carts may be taken for transport duty`; `ch 30 -- no sheriff or bailiff or other person shall take the horses or carts of a freeman for transport duty against his will` |
| 31.1 | the owner of the wood | the King and his bailiffs | claim-right / duty | `ch 31 -- wood may be taken for the King's castles or other work`; `ch 31 -- neither the King nor his bailiffs shall take wood which is not the King's against the will of the owner` |
| 32.1 | the lords of the fiefs | the King | claim-right / duty | `ch 32 -- the last day the King may retain the lands`; `ch 32 -- the King may retain the lands on this day`; `ch 32 -- the King will not retain the lands beyond one year and one day`; `ch 32 -- the lands are handed over to the lords of the fiefs` |
| 33.1 | not named by the text (fork F33) | not named by the text (fork F33) | claim-right / duty | `ch 33 -- the kydell is to be removed` |
| 34.1 | a freeman who may lose his court | not named by the text (fork F34) | claim-right / duty | `ch 34 -- the writ praecipe may be issued` |
| 35.1 | not named by the text (buyers) | not named by the text (fork F35) | claim-right / duty | `ch 35 -- the standard throughout the realm`; `ch 35 -- a measure other than the standard may be used` |
| 35.2 | none (extends 35.1 to ale, corn, cloth and weights; the London quarter and the two ells are definitions) | none | none | none |
| 35.3 | none (extends 35.1 to ale, corn, cloth and weights; the London quarter and the two ells are definitions) | none | none | none |
| 35.4 | none (extends 35.1 to ale, corn, cloth and weights; the London quarter and the two ells are definitions) | none | none | none |
| 35.5 | none (extends 35.1 to ale, corn, cloth and weights; the London quarter and the two ells are definitions) | none | none | none |
| 36.1 | the person seeking the writ | not named by the text (fork F36) | claim-right / duty | `ch 36 -- something may be given or taken for the writ`; `ch 36 -- the writ may be denied` |
| 37.1 | the holder of a fee-farm, socage or burgage who holds also by knight's service | the King | immunity / disability | `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure` |
| 37.2 | none (limits 37.1: the fee-farm itself) | none | none | none |
| 37.3 | the holder of a petty serjeanty | the King | immunity / disability | `ch 37 -- the King may have wardship of this by reason of the tenure`; `ch 37 -- we will not have wardship by reason of that tenure` |
| 38.1 | a man | a bailiff | claim-right / duty | `ch 38 -- the officer may put a man to his law upon his own mere word of mouth`; `ch 38 -- no bailiff shall put any man to his law upon his own mere word of mouth, without credible witnesses` |
| 39.1 | a freeman | not named by the text (fork F39d) | claim-right / duty | `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- reading C, no exception to the passive limb: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` |
| 39.2 | a freeman | the King | claim-right / duty | `ch 39 -- a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested`; `ch 39 -- we will not set forth against him, nor send against him, unless by the lawful judgment of his peers and by the law of the land`; `ch 39 -- reading B, either suffices: a freeman may be arrested, detained in prison, deprived of his freehold, outlawed, banished or in any way molested` |
| 40.1 | everyone | the King | claim-right / duty | `ch 40 -- right or justice may be sold, refused or delayed`; `ch 40 -- to no one will we sell, refuse or delay right or justice` |
| 41.1 | merchants | not named by the text (fork F41a) | claim-right / duty | `ch 41 -- the merchant has safe and secure exit, entry, stay and movement by land and by water`; `ch 41 -- the merchant may buy and sell`; `ch 41 -- a toll may be taken from the merchant` |
| 41.2 | none (limits 41.1) | none | none | none |
| 41.3 | the enemy merchants found in the land at the beginning of the war | not named by the text (fork F41a) | claim-right / duty | `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured` |
| 41.3 | the King, or his chief justiciar | the enemy merchants found in the land at the beginning of the war | power / liability | `ch 41 -- the enemy merchant is to be detained`; `ch 41 -- the body or goods of the detained merchant may be injured` |
| 41.4 | the enemy merchants | not named by the text (fork F41a) | claim-right / duty | `ch 41 -- the enemy merchant is safe in our land` |
| 42.1 | any one who leaves the kingdom and returns | not named by the text | liberty / no-claim | `ch 42 -- the person may leave the kingdom and return, safe and secure by land and water` |
| 42.2 | none (limits 42.1) | none | none | none |
| 42.3 | the King | the person who leaves | claim-right / duty | `ch 42 -- the allegiance due to the King remains owed` |
| 43.1 | the heir of one who held of an escheat | the King | claim-right / duty | `ch 43 -- the King may take this relief and service from the heir`; `ch 43 -- his heir shall give no other relief and perform no other service to us than he would have done to the baron` |
| 43.2 | the heir of one who held of an escheat | the King | claim-right / duty | `ch 43 -- the King holds the escheat in the manner in which the baron held it`; `ch 43 -- we shall hold it in the same manner in which the baron held it` |
| 44.1 | men who dwell without the forest | the justiciars of the forest | immunity / disability | `ch 44 -- the man must come before the justiciars of the forest upon a general summons` |
| 45.1 | the subjects of the realm | the King | claim-right / duty | `ch 45 -- the King may appoint this person to the office`; `ch 45 -- we will appoint as justices, constables, sheriffs or bailiffs only such as know the law of the realm and mean to observe it well` |
| 46.1 | barons who founded abbeys | not named by the text (fork F46) | claim-right / duty | `ch 46 -- the baron shall have the wardship of the abbey` |
| 47.1 | not named by the text (fork F47) | not named by the text (fork F47) | claim-right / duty | `ch 47 -- the forest is to be disafforested` |
| 47.2 | not named by the text (fork F47) | not named by the text (fork F47) | claim-right / duty | `ch 47 -- the river-bank is to be released from defence` |
| 48.1 | not named by the text (fork F48a) | not named by the text (fork F48a) | claim-right / duty | `ch 48 -- the evil custom is to be inquired into`; `ch 48 -- the inquest is constituted as the text requires` |
| 48.2 | not named by the text (fork F48a) | not named by the text (fork F48a) | claim-right / duty | `ch 48 -- the last day for abolishing the evil custom`; `ch 48 -- the evil custom is to be utterly abolished`; `ch 48 -- abolition on this day is within the forty days`; `ch 48 -- the abolished custom may be restored` |
| 48.3 | none (condition of 48.1 and 48.2) | none | none | none |
| 49.1 | Englishmen who delivered hostages and charters | the King | claim-right / duty | `ch 49 -- the hostages and charters are to be restored`; `ch 49 -- we will immediately restore all hostages and charters delivered to us by Englishmen` |
| 50.1 | not named by the text | the King | claim-right / duty | `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- the person may have a bailiwick in England in future`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes` |
| 50.1 | not named by the text (the kingdom) | the relations of Gerard de Athyes | immunity / disability | `ch 50 -- the person is to be removed from his bailiwick`; `ch 50 -- the person may have a bailiwick in England in future`; `ch 50 -- we will entirely remove from their bailiwicks the relations of Gerard de Athyes` |
| 50.2 | none (lists the persons of 50.1) | none | none | none |
| 51.1 | not named by the text | the King | claim-right / duty | `ch 51 -- the person is to be banished from the kingdom`; `ch 51 -- we will banish from the kingdom all foreign-born knights, cross-bowmen, serjeants and mercenary soldiers who have come with horses and arms to the kingdom's hurt` |
| 52.1 | the person dispossessed without judgment | the King | claim-right / duty | `ch 52 -- the lands, castles, franchises or right are to be restored`; `ch 52 -- we will immediately restore them to him` |
| 52.2 | the five-and-twenty barons | the parties to the dispute | power / liability | `ch 52 -- who decides a dispute over the restoration` |
| 52.3 | the King | those from whom the King's father or brother took possessions | liberty / no-claim | `ch 52 -- the King has respite for the possession`; `ch 53 -- the King has the same respite concerning the matter` |
| 52.4 | none (limits 52.3) | none | none | none |
| 52.5 | the dispossessed | the King | claim-right / duty | `ch 52 -- full justice is to be granted for the possession`; `ch 52 -- as soon as we return from our expedition we will immediately grant full justice therein` |
| 53.1 | the King | those who claim in the matters of 53.1 | liberty / no-claim | `ch 53 -- the King has the same respite concerning the matter` |
| 53.2 | none (extends 52.3's respite to the wardships of 53.2) | none | none | none |
| 53.3 | none (extends 52.3's respite to the abbeys of 53.3) | none | none | none |
| 53.4 | those who complain of such things | the King | claim-right / duty | `ch 53 -- full justice is to be granted to the person who complains`; `ch 53 -- when we have returned we will immediately grant full justice to all who complain of such things` |
| 54.1 | a person against whom a woman appeals | not named by the text (fork F54) | immunity / disability | `ch 54 -- a person may be arrested or imprisoned upon the appeal` |
| 55.1 | the person who paid or was amerced unjustly | not named by the text (fork F55a) | claim-right / duty | `ch 55 -- what is to be done with the fine or amercement` |
| 55.2 | the five-and-twenty barons | the person who paid or was amerced unjustly | power / liability | `ch 55 -- what is to be done with the fine or amercement`; `ch 55 -- who decides what is done with the fine or amercement` |
| 55.3 | none (the archbishop sits with the twenty-five; stated once at 55.2) | none | none | none |
| 55.4 | none (the business proceeds without the archbishop; limit on 55.3) | none | none | none |
| 55.5 | the five-and-twenty barons | a baron who is in a similar suit | power / liability | `ch 55 -- the baron may sit in this particular judgment`; `ch 55 -- the substitute may sit in the place of a baron in a similar suit` |
| 56.1 | Welshmen | the King | claim-right / duty | `ch 56 -- the lands, liberties or other things are to be restored to the Welshman`; `ch 56 -- they shall be immediately restored to them` |
| 56.2 | Welshmen | not named by the text (fork F56) | claim-right / duty | `ch 56 -- who decides a dispute over the restoration to the Welshman` |
| 56.3 | none (defines the law by the place of the tenement) | none | none | none |
| 56.4 | the King and his men | Welshmen | claim-right / duty | `ch 56 -- the Welshman is to restore to the King and his men`; `ch 56 -- Welshmen shall do the same to us and ours` |
| 57.1 | the King | Welshmen from whom possessions were taken by the King's father or brother | liberty / no-claim | `ch 57 -- the King has respite for the possession taken from a Welshman` |
| 57.2 | none (limits 57.1) | none | none | none |
| 57.3 | Welshmen | the King | claim-right / duty | `ch 57 -- full justice is to be granted in accordance with the laws of the Welsh`; `ch 57 -- as soon as we return we will immediately grant full justice in accordance with the laws of the Welsh` |
| 58.1 | not named by the text (fork F58) | the King | claim-right / duty | `ch 58 -- the person or thing is to be given up`; `ch 58 -- we will immediately give up the son of Llywelyn and all the hostages of Wales` |
| 59.1 | Alexander, King of Scots | the King | claim-right / duty | `ch 59 -- how the King deals with Alexander, King of Scots`; `ch 59 -- we will do toward Alexander, King of Scots, in the same manner as we shall do towards our other barons of England` |
| 59.2 | Alexander, King of Scots | the King | claim-right / duty | `ch 59 -- who judges the matter between the King and Alexander, King of Scots` |
| 60.1 | the men of each person in the kingdom | all of the kingdom, clergy and laymen | claim-right / duty | `ch 60 -- the person must observe the customs and liberties towards his men`; `ch 60 -- the customs and liberties shall be observed by all of our kingdom towards their men` |
| 61.2 | the barons | none | liberty / no-claim | `ch 61 -- the barons choose five-and-twenty barons of the kingdom, whomsoever they will` |
| 61.3 | not named by the text (fork F61f) | the five-and-twenty barons | claim-right / duty | `ch 61 -- the five-and-twenty barons shall be bound to observe and hold, and cause to be observed, the peace and liberties` |
| 61.4 | not named by the text (those wronged) | four of the five-and-twenty barons | claim-right / duty | `ch 61 -- the four barons are to repair to the King and petition for the transgression to be corrected`; `ch 61 -- to whom the four barons repair`; `ch 61 -- the said four barons shall repair to us and petition to have that transgression corrected without delay` |
| 61.5 | none (the time for 61.4 and 61.6) | none | none | none |
| 61.6 | not named by the text (the rest of the twenty-five) | four of the five-and-twenty barons | claim-right / duty | `ch 61 -- the four barons are to refer the matter to the rest of the five-and-twenty`; `ch 61 -- the four barons aforesaid shall refer that matter to the rest of the five-and-twenty barons` |
| 61.7 | not named by the text (fork F61c) | the five-and-twenty barons | claim-right / duty | `ch 61 -- the five-and-twenty barons are to distrain and distress the King`; `ch 61 -- those five-and-twenty barons shall, together with the community of the whole land, distrain and distress us in all possible ways` |
| 61.8 | the King, the queen and their children | the five-and-twenty barons | claim-right / duty | `ch 61 -- the person may be harmed in the distraint`; `ch 61 -- saving harmless our own person, and the persons of our queen and children` |
| 61.9 | the King | the five-and-twenty barons | claim-right / duty | `ch 61 -- the five-and-twenty barons are to resume their old relations towards the King`; `ch 61 -- when redress has been obtained, they shall resume their old relations towards us` |
| 61.10 | whoever in the country desires it | none | liberty / no-claim | `ch 61 -- let whoever in the country desires it swear to obey the orders of the said five-and-twenty barons` |
| 61.11 | whoever wishes to swear | the King | claim-right / duty | `ch 61 -- the person has the King's leave to swear`; `ch 61 -- we shall never forbid anyone to swear` |
| 61.12 | not named by the text (fork F61d) | the King | claim-right / duty | `ch 61 -- the person is to be compelled by the King's command to swear`; `ch 61 -- we shall by our command compel the same to swear to the effect foresaid` |
| 61.13 | not named by the text (the twenty-five) | the barons who are left of the five-and-twenty | claim-right / duty | `ch 61 -- another baron is to be chosen in his place`; `ch 61 -- those of the said twenty-five barons who are left shall choose another in his place according to their own judgment` |
| 61.13 | not named by the text (the twenty-five) | the baron chosen in the place of one of the five-and-twenty | claim-right / duty | `ch 61 -- another baron is to be chosen in his place`; `ch 61 -- those of the said twenty-five barons who are left shall choose another in his place according to their own judgment` |
| 61.14 | the five-and-twenty barons present | those who disagree or are absent | power / liability | `ch 61 -- what those present ordain or command is held as fixed and established` |
| 61.15 | not named by the text (the kingdom) | the five-and-twenty barons | claim-right / duty | `ch 61 -- the said twenty-five shall swear that they will faithfully observe all that is aforesaid` |
| 61.16 | the subjects | the King | claim-right / duty | `ch 61 -- we shall procure nothing from anyone, directly or indirectly, whereby any part of these concessions and liberties might be revoked or diminished` |
| 61.17 | the subjects | the King | immunity / disability | `ch 61 -- the thing procured`; `ch 61 -- we shall never use it personally or by another` |
| 62.1 | everyone, clergy and lay | the King | immunity / disability | `ch 62 -- the ill-will, hatreds and bitterness are remitted and pardoned` |
| 62.2 | everyone, clergy and lay | the King | immunity / disability | `ch 62 -- the trespass is fully remitted and completely forgiven, as far as pertains to the King` |
| 63.1 | the men in the kingdom and their heirs | the King and his heirs (fork F1) | claim-right / duty | `ch 63 -- the person has and holds all the aforesaid liberties, rights and concessions for himself and his heirs` |
| 63.1 | none (the English church, stated once at 1.1) | none | none | none |
| 63.2 | the other side of the oath | the King and the barons | claim-right / duty | `ch 63 -- all these conditions shall be kept in good faith and without evil intent` |

## What the text turns out to say

Each finding says where it is asserted.
The last sentence of a finding is "Asserted." when a test or a seat case in the named file asserts it; a finding that ends "Not asserted: ..." says why it is not.

1. Chapter 39 says "unless by the lawful judgment of his peers and by the law of the land", and the translation's "and" is read as "and": the judgment of peers alone, or the law of the land alone, leaves a freeman's arrest, imprisonment, disseisin, outlawry, banishment or molestation barred.
   The reading "either suffices" (F39b) and the reading that the passive limb has no exception at all (F39c) are encoded beside it, each in its own function, so that the rows where they differ are visible.
   The assertions are in `mc15-tests-ch39-40.l4` and in the seat cases for "May the King imprison me or take my land without a judgment of my peers?".
   Asserted.
2. The first limb of chapter 39 (arrested, imprisoned, deprived of freehold, outlawed, banished, molested) is passive and names no one who does it; only the second limb ("we will not set forth against him, nor send against him") has a party, the King.
   The King's `SHANT` is therefore gated by the Bar decision and applies to the second limb only.
   The assertions are in `mc15-tests-ch39-40.l4` (traces).
   Asserted.
3. Chapter 40 says "To no one", not "to no freeman": the Bar decision takes no input about who the person is.
   It also gives no period for "delay", so none is encoded.
   The assertions are in `mc15-tests-ch39-40.l4` (three traces, one per act) and in the seat cases.
   Asserted.
4. Chapter 12 puts the three purposes (ransoming the King, knighting his eldest son, once marrying his eldest daughter) outside the need for common counsel, but chapter 14 puts "(except in the three cases aforesaid)" after "aid" and before "or of a scutage".
   So a scutage always needs common counsel, and an aid for the three purposes needs only to be reasonable.
   A second aid for the eldest daughter's marriage is barred ("once").
   The assertions are in `mc15-tests-ch12-16.l4` and in the seat cases for "May the King impose this scutage or aid on me?".
   Asserted.
5. Chapter 44 says men who dwell outside the forest "need not" come before the forest justiciars on a general summons "except those who are impleaded, or who have become sureties".
   The exception withdraws the exemption; it does not itself say those men must come, so for them the answer is `Obligation not covered`.
   The assertions are in `mc15-tests-ch43-48.l4` and in the seat cases.
   Asserted.
6. Chapter 41.4 says that if the King's merchants are safe in the land at war with him, the others shall be safe in the King's land.
   The "if" is the text's own word, so if they are not safe the others are not entitled to be safe: `Not entitled` (F41b).
   The first version answered `Entitlement not covered`; the second pass changed it, and the assertion and the seat case carry a `-- RECONCILED 2026-10-30` comment.
   The assertions are in `mc15-tests-ch41-42.l4` and in the seat cases.
   Asserted.
7. Chapter 41.3 forbids injury to the detained merchants' bodies or goods "until information be received"; "until" is the text's own word, so after information has been received the answer is `Not barred`, and the same holds for the duty to detain (`Not obliged`).
   A merchant who was not found in the land at the beginning of the war is outside 41.3's "if such are found", which is the text's no: `Not barred` and `Not obliged`; a person who is not one of the merchants 41.2 excepts is outside the sentence, and the answer is "not covered" (F64e).
   The assertions are in `mc15-tests-ch41-42.l4` and in the seat cases.
   Asserted.
8. Chapter 41.2's exception is "in time of war" and for "such merchants as are of the land at war with us": a merchant of that land in peace, or a merchant in war who is not of that land, keeps the entitlement.
   Chapter 42 sends merchants back to chapter 41, and excepts those imprisoned or outlawed and natives of a country at war; a merchant who is also imprisoned is excepted twice and gets `Not entitled` under chapter 42's own entitlement.
   The assertions are in `mc15-tests-ch41-42.l4`.
   Asserted.
9. Chapter 29.2 says the knight "shall be relieved from guard in proportion to the time during which he has been on service" and states no proportion: the number of days relieved is `NOTHING`.
   The sentence opens "if we have led or sent him upon military service", which is the text's own if, so a knight the King has not led or sent is not entitled to be relieved: `Not entitled`.
   The assertions are in `mc15-tests-ch23-32.l4` and in the seat cases.
   Asserted.
10. Chapter 61.14 makes "that which the majority of those present ordain or command" established and sets no quorum.
    One baron present with one in favour is a majority of those present, and a tie (ten of twenty) is not.
    The assertions are in `mc15-tests-ch60-63.l4` and in the seat cases.
    Asserted.
11. Chapter 7.3 lets the widow remain forty days after the death and 7.4 assigns her dower within that time; counted from day 0, day 40 is allowed, and the text is silent about day 41 and about a day before the death, which are `Entitlement not covered` (F7b, F64c).
    The assertions are in `mc15-tests-ch02-08.l4` and in the seat cases.
    Asserted.
12. Chapter 32 says "one year and one day" without saying from what day: the starting day is an input.
    A year on from 29 February 2000 is 28 February 2001 by the standard library's `add years`, so the last day is 1 March 2001; a start of 15 January 2001 gives 16 January 2002.
    The assertions are in `mc15-tests-ch23-32.l4` and in the seat cases.
    Asserted.
13. Chapters 48 and 61.5 count "within forty days" from the inquest or the intimation without counting that day: a start of 15 January 2001 gives 24 February 2001 as the last day, 25 December 2001 gives 3 February 2002, and 1 February 2000 gives 12 March 2000 (a leap year).
    The assertions are in `mc15-tests-ch43-48.l4`, `mc15-tests-ch60-63.l4` and in the seat cases.
    Asserted.
14. Chapter 25 keeps counties, hundreds, wapentakes and trithings "at the old rents, and without any additional payment": a rent above the old rent, or an additional payment, is barred; the old rent itself and a rent below it are `Bar not covered`, because "shall remain at the old rents" carries no if, unless or only (F25, F64c); the demesne manors are excepted by the text's own "except" and are `Not barred`.
    The assertions are in `mc15-tests-ch23-32.l4`.
    Asserted.
15. Chapter 2.4 names only a ceiling ("100s. at most") for a knight's fee, so with nothing owed by custom the text states no sum: the relief is `NOTHING`.
    The two sums of £100 are flat unless less is owed by custom.
    The assertions are in `mc15-tests-ch02-08.l4` and in the seat cases.
    Asserted.
16. Chapter 8.2 says "provided always that she gives security": a widow who prefers to live without a husband but gives no security is `Not barred` from being compelled to marry (F8).
    The assertions are in `mc15-tests-ch02-08.l4` and in the seat cases.
    Asserted.
17. Chapters 52, 53 and 57 give the King "respite until the usual term of crusaders" and no date; whether the term has ended is a plain input.
    The duty to grant full justice begins "as soon as we return from our expedition (or if perchance we desist)"; before that the text is silent and the answer is `Obligation not covered`, and for a thing about which a plea was raised or an inquest made before the King took the cross it is `Obligation not covered`.
    The assertions are in `mc15-tests-ch49-59.l4` and in the seat cases.
    Asserted.
18. Chapter 55 gives two things to be done with an unjust fine, "entirely remitted, or else ... according to the decision of the five-and-twenty barons", and does not say who chooses; the `Remedy` value names both.
    The archbishop is with the barons if he can be present, and the business proceeds without him if he cannot.
    The assertions are in `mc15-tests-ch49-59.l4` and in the seat cases.
    Asserted.
19. Chapter 61.11 gives everyone leave to swear and forbids the King ever to forbid it; 61.12 makes the King compel those "who of themselves and of their own accord are unwilling".
    The two stand as written (F61d): an unwilling person in the land is `Obliged` to be compelled, a willing one is `Obligation not covered`.
    The assertions are in `mc15-tests-ch60-63.l4` and in the seat cases.
    Asserted.
20. Chapter 61.7 says the twenty-five "shall ... distrain and distress us", ending "until redress has been obtained as they deem fit": a duty, ending when redress is obtained; before the matter is referred the answer is `Obligation not covered`.
    The assertions are in `mc15-tests-ch60-63.l4` and in the seat cases.
    Asserted.
21. Chapter 10.2's limit on the King (nothing but the principal sum) applies to the debt of 10.1, borrowed from the Jews by a borrower who has died, once it falls into the King's hands (F10).
    The assertions are in `mc15-tests-ch09-11.l4` and in the seat cases.
    Asserted.
22. Chapter 26.1 lets the officer attach chattels "to the value of that debt": the text says nothing about an attachment of more than the debt, an attachment not at the sight of lawful men, or one of chattels not found upon the lay fief, and those are `Entitlement not covered` (F64c).
    The sentence is "If any one holding of us a lay fief shall die, and our sheriff or bailiff shall exhibit our letters patent", which is the text's own if: where the holder has not died, or the letters patent are not exhibited, the officer is `Not entitled` to attach (second pass, 2026-10-30).
    The assertions are in `mc15-tests-ch23-32.l4` and in the seat cases.
    Asserted.
23. Chapter 37.2 allows wardship of the fee-farm itself "unless such fee-farm owes knight's service" only in the situation of 37.1 (F37); a petty serjeanty (37.3) bars wardship of the heir and of the land held by knight's service without any second-holding condition.
    A holder of fee-farm, socage or burgage who holds no land by knight's service is outside 37.1's "if" and gets `Not barred` (sweep, 2026-10-30).
    The assertions are in `mc15-tests-ch33-38.l4` and in the seat cases.
    Asserted.
24. Chapter 14.4 makes the business proceed on the appointed day "although not all who were summoned have come", so the duty is the same whether all came or some stayed away; if the summons was not made as the Charter requires, the text does not say.
    The assertions are in `mc15-tests-ch12-16.l4` and in the seat cases.
    Asserted.
25. Chapter 36 has two Bars, one on giving or taking anything for the writ of inquisition of life or limbs and one on denying it; it names no one who does either.
    The assertions are in `mc15-tests-ch33-38.l4` and in the seat cases.
    Asserted.
26. Chapter 9.2 bars distraining the sureties only "so long as the principal debtor is able to satisfy the debt"; when he cannot, 9.3 makes them answer, and 9.4 gives them his lands and rents until indemnified unless he can show proof that he is discharged.
    The sureties are obliged only if he has failed ("and if the principal debtor shall fail to pay"), so a debtor who is neither able nor has failed leaves them `Not obliged` (sweep, 2026-10-30).
    The assertions are in `mc15-tests-ch09-11.l4` and in the seat cases.
    Asserted.
27. Chapter 59 does not state "the same manner as we shall do towards our other barons", and does not say what the charters from William provide; the `Treatment` value returns the text's own phrase.
    The assertions are in `mc15-tests-ch49-59.l4` and in the seat cases.
    Asserted.
28. Chapter 63.1 begins by restating chapter 1 ("that the English Church be free"), so that relation is stated once, at 1.1, and 63.1 carries the second limb (the men in the kingdom and their heirs).
    Not asserted: this is a statement about how the Hohfeld table is built, not about an answer.
29. Chapters 6, 17, 25, 28, 30, 31, 35 and 38 state a rule and no exception for the case that meets it: a person who meets the rule (a marriage without disparagement and with notice, a common plea held in a fixed place, the old rent, money tendered at once, a taking with the owner's will, the standard measure, a man put to his law with credible witnesses) is told `Bar not covered`, not `Not barred`.
    The words that describe the barred act ("without", "against the will of", "shall remain at", "shall be held in") are not an if, an unless or an only, so the text does not say in its own words that the opposite case is allowed (F64c).
    The assertions are in `mc15-tests-ch02-08.l4`, `mc15-tests-ch17-19.l4`, `mc15-tests-ch23-32.l4`, `mc15-tests-ch33-38.l4` and in the seat cases.
    Asserted.
30. Where a sentence is conditioned by "if", "while", "until", "unless" or "except" and the condition is a fact that fails, the text's own word makes the no: the heir who is not of full age is not entitled to his inheritance "on payment of the ancient relief" under 2.1 (`Not entitled`; chapter 3 treats the heir under age), a Jewish loan whose borrower is alive is not barred from bearing interest under chapter 10 (`Not barred`) while a loan from someone else is outside the sentence (`Bar not covered`), a debt that has not fallen into the King's hands is not barred under 10.2, where no child of the deceased is left under age there is no entitlement to necessaries under 11.2 (`Not entitled`), and so on for the 23 branches in "The sweep of the not-covered branches".
    Where what fails is the class of person the clause speaks of, the answer stays "not covered" (F64e), and 70 branches say so, each with its reason.
    The assertions are in the test files for those chapters and in the seat cases, each restated one carrying a `-- RECONCILED 2026-10-30` comment.
    Asserted.

## Terms the text does not define

The encoding does not define these.
Each is taken as a plain input (a yes/no, a number or a choice that the person states), or as a typed value, or kept as the text's own phrase inside an `Act` or `Forum` name.
Each gloss is marked "gloss (not the text's)" and is a reader's aid only; none is relied on by a rule.
Money stays in the text's units (pounds, shillings); where a rule compares two amounts it takes them in whatever unit the person states and converts nothing.

| Term | Chapters | How it is taken | gloss (not the text's) |
| --- | --- | --- | --- |
| freeman | 1, 20, 27, 30, 39 | plain input: whether the person is one | a person of free status; the text does not say who is |
| relief | 2, 3, 43 | plain inputs: whether it is owed, whether paid; the sums are the text's | a sum an heir pays on taking up an inheritance |
| earl, baron, knight's fee, in chief, military service | 2, 3, 43, 46 | plain inputs | ranks and tenures of land-holding; not defined in the text |
| wardship, guardian, full age, under age | 3 to 5, 37, 46 | plain inputs | the keeping of an heir and his land during minority; "full age" is not stated |
| disparagement, nearest in blood | 6 | plain inputs | a marriage thought beneath the heir's rank; the heir's closest relation |
| dower, marriage portion, security | 7, 8 | the person states what is asked | the widow's share of her husband's land; what she brought; a guarantee |
| surety, distrain, indemnified, discharged | 9 | plain inputs | a guarantor; to seize goods to compel payment; made whole; released |
| the Jews, interest | 10, 11 | plain input: whether the lender was one of "the Jews" | the text's name for a class of lenders |
| scutage, aid, common counsel, reasonable | 12 to 15 | a choice of kind, a choice of purpose, plain inputs | payments in lieu of service, and a payment for a lord's needs; the kingdom's consultation; a judgment |
| tenement, free tenement, service | 16, 34, 37 | plain inputs | land held; the amount of service is a number |
| common plea, county court, assize, justiciar, knights and freeholders | 17 to 19 | plain inputs and counts | kinds of court and of officer |
| novel disseisin, mort d'ancestor, darrein presentment | 18 | a choice of kind | three kinds of inquest named by the text |
| amerce, contenement, wainage, villein, honest men, peers, clerk, lay holding, church benefice | 20 to 22 | plain inputs and a choice of class | a penal fine; a freeman's livelihood; a villein's cart and tools; a bondman |
| bridges, pleas of the Crown, demesne manor, hundred, wapentake, trithing | 23 to 25 | a choice of unit or plain inputs | not glossed; the text uses them without explanation |
| lay fief, letters patent, lawful men, executors, reasonable shares | 26 | plain inputs | not glossed |
| intestate, kinsfolk, castle-guard, military service, responsible man | 27, 29 | plain inputs | not glossed |
| kydell, praecipe, writ of inquisition of life or limbs, fee-farm, socage, burgage, petty serjeanty | 33 to 37 | plain inputs and choices | not glossed |
| "law" (to put a man to his law), credible witnesses | 38 | plain input: whether credible witnesses are brought | not glossed |
| lawful judgment of his peers, the law of the land, arrested, outlawed, molested | 39 | plain inputs | not glossed; see forks F39a to F39f |
| right, justice, sell, refuse, delay | 40 | plain input: whether it is right or justice | not glossed |
| merchant, evil tolls, ancient and right customs, time of war, public policy, allegiance | 41, 42 | plain inputs | not glossed |
| escheat, honour, barony, forest, impleaded, disafforested, river-banks "in defence", warrens | 43, 44, 47, 48 | plain inputs | not glossed |
| hostages, charters, bailiwick, franchises, foreign-born, mercenary soldiers | 49 to 51 | plain inputs, choices, and the names the text lists | not glossed |
| the usual term of crusaders, taking of the cross, plea, inquest, full justice | 52, 53, 57 | plain inputs | the text gives no date for the term |
| appeal of a woman, unjustly, similar suit, marches | 54 to 56 | plain inputs | not glossed |
| queen, quarrel, trespass, Easter, oath, good faith, evil intent | 61 to 63 | plain inputs | not glossed |
| the barons, the five-and-twenty barons, the community of the whole land, offence, redress "as they deem fit" | 61 | typed parties and plain inputs | the text names the twenty-five as chosen by the barons |

## What the stable binary does not accept

Measured on the two binaries named in `check.sh` (1.6.98 and 1.6.102) in this session, with small probe files that were deleted afterwards.
Loud failures (an error in the diagnostics, which `check.sh` counts) are listed apart from silent ones (a wrong answer with exit code 0).

Loud:
- `REFUSE` does not exist on either build ("I could not find a definition for the identifier REFUSE"), so no rule here refuses; "not covered" is a constructor or `NOTHING`.
- A multi-line `#ASSERT` (the `EQUALS` on a line of its own) is a parse error on both builds, so every assertion is one line.
- `BREACH BY` a `LIST` is rejected (the `HENCE` clause is then typed `DEONTIC OF LIST OF ...`), so each rule names a single party.
- `PLUS` on a `DATE` is a type error unless `daydate` is imported; with `IMPORT daydate` it works (`15 January 2001 PLUS 40` gives 24 February 2001), and the modules here use `Date (Day d PLUS n)` with the import.
- A `DEONTIC` value cannot be compared or asserted: on 1.6.98 the assertion is reported as "assertion failed", which reads like a wrong answer, and on 1.6.102 as "Trying to check equality on types that do not support it".
  Every regulative rule here is therefore gated by a decision function that carries the assertions, and the rule itself is tested by `#TRACE`.

Silent:
- `NOT a AND b` parses as `NOT (a AND b)`, not `(NOT a) AND b`: with `a` true and `b` false the first is true and the second false.
  Every `NOT` in these files is parenthesised.
- A `#TRACE` prints `FULFILLED`, a breach or a residual duty and no assertion line, so `check.sh`'s counts do not move when a trace comes out differently.
  `check-traces.py` closes the gap: it fails on a trace with no `-- expect:` line, on a result that cannot be found, and on a result that differs from the expectation.
  Its negative control (one `#ASSERT` and one `-- expect:` flipped in a copy) was seen to fail on each.
- `check.sh` says, and it is true, that the main-build columns cannot see a different `#TRACE` outcome; `check-traces.py` was therefore run on both binaries (below).
- Chapter 14's forty days are not a deadline window in this encoding; they are tested by a decision function over the number of days (F14).

## What check.sh prints

Run as `L4=<the 1.6.98 binary> L4_MAIN=<the 1.6.102 binary> ./check.sh`.
The run below replaces the 907-assertion run of the first pass (579 module assertions and 328 seat cases); the folder held only the supplied tools when the work began.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.102 (main, e4f2553, 2026-10-26)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
mc15-cases-seat.l4                             0       331       0        0         0 |      0       331       0        0  same
mc15-ch01.l4                                   0         0       0        0         0 |      0         0       0        0  same
mc15-ch02-08.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch09-11.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch12-16.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch17-19.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch20-22.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch23-32.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch33-38.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch39-40.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch41-42.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch43-48.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch49-59.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-ch60-63.l4                                0         0       0        0         0 |      0         0       0        0  same
mc15-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
mc15-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
mc15-tests-ch01.l4                             0         4       0        0         0 |      0         4       0        0  same
mc15-tests-ch02-08.l4                          0        69       0        0         0 |      0        69       0        0  same
mc15-tests-ch09-11.l4                          0        39       0        0         0 |      0        39       0        0  same
mc15-tests-ch12-16.l4                          0        52       0        0         0 |      0        52       0        0  same
mc15-tests-ch17-19.l4                          0        30       0        0         0 |      0        30       0        0  same
mc15-tests-ch20-22.l4                          0        18       0        0         0 |      0        18       0        0  same
mc15-tests-ch23-32.l4                          0        72       0        0         0 |      0        72       0        0  same
mc15-tests-ch33-38.l4                          0        38       0        0         0 |      0        38       0        0  same
mc15-tests-ch39-40.l4                          0        15       0        0         0 |      0        15       0        0  same
mc15-tests-ch41-42.l4                          0        35       0        0         0 |      0        35       0        0  same
mc15-tests-ch43-48.l4                          0        50       0        0         0 |      0        50       0        0  same
mc15-tests-ch49-59.l4                          0       109       0        0         0 |      0       109       0        0  same
mc15-tests-ch60-63.l4                          0        48       0        0         0 |      0        48       0        0  same
TOTAL (29 modules)                             0       910       0        0           |      0       910       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## What check-traces.py prints

Run as `L4=<binary> python3 -I check-traces.py` once for each binary.

```
--- with l4 1.6.98 (L4_BIN):
mc15-tests-ch01.l4                       traces   4  as expected   4  not as expected   0
mc15-tests-ch02-08.l4                    traces  12  as expected  12  not as expected   0
mc15-tests-ch09-11.l4                    traces  13  as expected  13  not as expected   0
mc15-tests-ch12-16.l4                    traces  12  as expected  12  not as expected   0
mc15-tests-ch17-19.l4                    traces   4  as expected   4  not as expected   0
mc15-tests-ch23-32.l4                    traces  26  as expected  26  not as expected   0
mc15-tests-ch33-38.l4                    traces   6  as expected   6  not as expected   0
mc15-tests-ch39-40.l4                    traces   9  as expected   9  not as expected   0
mc15-tests-ch43-48.l4                    traces   9  as expected   9  not as expected   0
mc15-tests-ch49-59.l4                    traces  29  as expected  29  not as expected   0
mc15-tests-ch60-63.l4                    traces  44  as expected  44  not as expected   0
TOTAL traces 168  as expected 168  not as expected 0
exit 0
--- with l4 1.6.102 (L4_MAIN):
mc15-tests-ch01.l4                       traces   4  as expected   4  not as expected   0
mc15-tests-ch02-08.l4                    traces  12  as expected  12  not as expected   0
mc15-tests-ch09-11.l4                    traces  13  as expected  13  not as expected   0
mc15-tests-ch12-16.l4                    traces  12  as expected  12  not as expected   0
mc15-tests-ch17-19.l4                    traces   4  as expected   4  not as expected   0
mc15-tests-ch23-32.l4                    traces  26  as expected  26  not as expected   0
mc15-tests-ch33-38.l4                    traces   6  as expected   6  not as expected   0
mc15-tests-ch39-40.l4                    traces   9  as expected   9  not as expected   0
mc15-tests-ch43-48.l4                    traces   9  as expected   9  not as expected   0
mc15-tests-ch49-59.l4                    traces  29  as expected  29  not as expected   0
mc15-tests-ch60-63.l4                    traces  44  as expected  44  not as expected   0
TOTAL traces 168  as expected 168  not as expected 0
exit 0
```

## What srcrefs.py prints

```
$ python3 -I srcrefs.py check --refs <raw text> <every mc15-*.l4>
srcrefs check: 264 src: lines, 201 runs, 202 locators, 0 problems
exit 0
$ python3 -I srcrefs.py check --strict --refs <raw text> <every mc15-*.l4>
srcrefs check: 264 src: lines, 201 runs, 202 locators, 0 problems
exit 0
```

## What branchcheck.py prints

Run as `python3 -I tools/branchcheck.py`.
It is the instrument for the rule in "Where the text says no, and where it does not".

```
module                         `no` branches   `not covered` branches   of which kept with `word not the condition here`
mc15-ch01.l4                          0                1                          0
mc15-ch02-08.l4                       4               11                          5
mc15-ch09-11.l4                      10                6                          6
mc15-ch12-16.l4                       4                5                          1
mc15-ch17-19.l4                       2                5                          2
mc15-ch20-22.l4                       4                3                          3
mc15-ch23-32.l4                       9               21                         13
mc15-ch33-38.l4                       4               12                          3
mc15-ch39-40.l4                       2                4                          2
mc15-ch41-42.l4                      10               10                          9
mc15-ch43-48.l4                       5               13                          7
mc15-ch49-59.l4                       7               26                         16
mc15-ch60-63.l4                       5               11                          3
TOTAL                                66              128                         70
FALSE-kind quotations checked against the source lines: 88
branchcheck.py: ok; every `no` branch quotes an accepted word that is in its source, and every `not covered` branch names its reason, with the swept words accounted for
```

## Method and independence

One agent worked alone from the brief: no ontology agent, no fleet, no subagents.
No independent test author was involved in writing the encoding; one wrote tests from the text alone afterwards, and the second pass answers a fix list the team lead drew from that author's report.
Nothing under `commons`, `commonswt`, `canon`, any other run directory or `~/.claude/` was opened by me; the `peeked` paragraph below says what the harness attached unasked.
`peeked`: two things, reported for completeness.
The second, in the second pass: after a context summary, a harness message attached to my context the text of four files from outside this deposit (a shipping script and a section of another row's notes from the lead's session, another row's test report, and a pull-request body); I did not ask for them and did not open them with a tool, I have not used their content, and nothing in this encoding was taken from or changed because of them.
The first: a `find` listing, made late in the work to look for the supplied `check.sh` and `srcrefs.py` to compare against, printed the file names (not the contents) of other run directories under the scratchpad; none of their files was read, and the comparison was made against the skill's own `assets/` copies instead, which are identical to the ones used here.
The only example read was `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4`, for its shape.
Expected values in every test were written from the text before the file was run, except the 38 assertions re-derived after the first rule change and the 29 module assertions and 12 seat cases restated in the second pass, which were re-derived from the text and the rule after the failing list had been compared with the predicted one ("Where the text says no, and where it does not").
Every failing assertion would have been recorded as a finding and left as written: there was none, so there is no `expected_failed` entry in `check.sh`.
Every case file ends with assertions written equal to assertions satisfied (331 of 331 in `mc15-cases-seat.l4`).

## What would need doing before this encoding is worth relying on

1. A person with knowledge of the Charter should read each module against the printed text and the fork register, and say which readings they would take.
2. The 91 fork entries should be read, in particular F39a to F39f, F40a to F40c, F12 and F12b, F44, F61c, F61e, F61i and F64a to F64e, because they decide what a person is told.
3. Every plain input should be checked for whether a person can answer it without already knowing the answer to the legal question (for example "the toll is an evil toll", "the amercement is in accordance with the degree of the offence").
4. The choice of decision functions where the text names no one (the "actor" entries in the register) should be reviewed, and parties added where a reader holds that the text names them.
5. The Hohfeld table's correlative parties for the passive provisions are marked "not named by the text"; a reader may name them, and the rules would then change from decision functions to regulative rules.
6. The seat's 126 questions should be tried on a few people in the seat, to see which ones they cannot answer from what they know.
7. The cases use arbitrary years where dates matter, because the text names no calendar; a user of the date questions should supply real dates.
8. Nothing here has been run on any build later than 1.6.102; the main-build column of `check.sh` is the only forward check.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `tools/` (the generator, the register data, the coverage script and the templates the chapter modules were generated from), `check-traces.py` and `coverage-map.tsv`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The `-- expect:` line above each `#TRACE` stays in the module, so the traces can be read back by hand.
The lead keeps the scripts outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the translation alone before it opened any `.l4` file: 540 numbered scenarios, of which 485 are on the text (the preamble and chapters 1 to 63, with at least one scenario where each rule applies and one where it does not or is silent) and 55 are put in a person's own words; 99 are answered "not covered".
It then wrote `tests-independent.l4`: 488 assertions covering 476 of the 540 scenarios, one assertion for each of the 126 seat questions and some for variants of a scenario, and ran it with the stable binary.
`ANSWERS.md` is not kept in this folder; the `S<n>` numbers in the comments of `tests-independent.l4` refer to it, and the seat questions are numbered `Q<n>`.
The author's convention is stated in the file: `Not barred`, `Not entitled` and `Not obliged` are its "no"; the `... not covered` constructors are its "not covered".

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run, against a copy of the modules made while the encoder was still revising them | 487 | 464 | 23 | 0 |
| first run against the final modules of that round | 488 | 454 | 34 | 0 |
| after the encoder's repairs and sweep, before the reconciliation below | 488 | 478 | 10 | 0 |
| after the reconciliation below | 488 | 488 | 0 | 0 |

The author was first given a copy of the modules taken before the encoder's last round of changes (which changed which branches answer "no" and which "not covered", renamed 105 seat questions to "Under chapter N, ...?" and retyped chapter 7.3 from `BOOLEAN` to `Entitlement`); the lead replaced it with the final modules of that round, and the author re-mapped 115 assertions by name and 4 by type (117 distinct, 2 lines being in both counts) without changing an expected value.
The author's file was rewritten after the first run, so which 23 assertions failed then is not known; the table's second row is from a run on the final modules of the round, which the lead repeated and which gave the same 34 failures.
The 64 scenarios the encoding has no function for are the `-- GAP` lines at the end of the test file, each in the author's words from `ANSWERS.md`, grouped by why: the preamble (11); recitals, the date and place, and the oath, which are inert (9); rules held as a `DEONTIC` with no decision function that answers the question (17); and cases the calls cannot state with the inputs they take (27), most of which have "not covered" as the author's expected answer.

**What the 34 first-run failures turned out to be.**
The author sorted the 34 into five kinds; the sweep added a sixth.

- **Six were encoder defects, repaired; the author's assertions stand unchanged (S162, S195, S299, S372, S407, S438).**
  In each the governing sentence of the translation opens with, or says, "if" ("if any of the said assizes cannot be taken", "If any one holding of us a lay fief shall die, and our sheriff or bailiff shall exhibit our letters patent", "if our men are safe there", "If any one has been dispossessed ... without the legal judgment of his peers", the same for the Welshmen, "if we ... shall in anything be at fault ..., and the offence be notified to four barons"), the condition fails, and the first version answered "not covered" where the rule counts the text as saying no.
  S372 and S407 are arguable, because the failing limb is a qualifier inside the antecedent.
  The lead's fix list named the six and asked for a sweep of every other "not covered" branch whose governing sentence holds one of the words that can make the text say no ("if", "unless", "while", "until", "as long as", "so long as", "except", "save", "provided", "other than", "only").
  The encoder made the six `Not obliged` or `Not entitled`, each with a `-- FALSE-kind` comment quoting the "if" (and read "notified to four barons" as at least four, F61i).
  Its sweep flagged 75 branches on the first complete scan, plus one the scanner could not see; 17 branches in 15 functions were changed to the text's no, and 70 are kept, each with a comment `word not the condition here` giving a one-sentence reason (the 70 include 11 that came into being after the first scan, when changes split branches; the 75 comes from the encoder's notes of a run whose output it deleted, so that figure cannot be re-run).
  Its checker (`branchcheck.py`, not shipped) now fails a "not covered" branch in a function whose source holds one of those words and has neither the no-answer nor the reason comment, and fails a `-- FALSE-kind` quotation that is not in the function's `-- src:` lines; that second check caught two mistakes of the encoder's own, a quoted "except" that is not in chapter 54 and chapter 53 quoting chapter 52's "until", both fixed.
  The branches are now 66 "no" and 128 "not covered", from 43 and 138 after the first pass.
  New or amended entries in the fork register: F64d ("when" is not taken as "if"), F64e (the failing of a fact the clause makes a condition is the text's no; the failing of the class of person or thing it speaks of is not), F61i, F9b, and amended F12b and F44.
- **Ten more failed only after the encoder's sweep, and were reconciled to its new answer, the text's no (S27, S34, S90, S94, S192, S200, S218, S270, S373, S414).**
  The author had expected "not covered" for a case outside what the provision speaks of, for example the heir under age at the death in chapter 2, a borrower who has not died in chapter 10, no child under age in chapter 11, a demesne manor in chapter 25, and a dispossession by a baron and not by the King in chapters 52 and 56; the sweep reads the failing of such a condition of an "if" or "except" sentence as the text's own no.
  This is the line fork F64e draws between a failed fact and a failed class, and **where it falls is for a lawyer**: it rests on counting a failed "if" as the text's no, which is an inference ("if A then B" does not itself say "if not A then not B"), and if a failed "if" is not the text's no, the 66 "no" branches of this encoding that rest on one move to "not covered".
- **Twenty were reconciled to the encoding's answer, "not covered" (and, for S85, to `Not barred`): the author's scenarios.**
  The author's `ANSWERS.md` counted a prohibition or grant "expressly limited by its own wording" as the text's no for the case outside the limit, which is wider than the family's rule, whose words are "means", "if", "only if", "as long as", "unless" and a list closed with "only" (and, in this encoding, the plain variants F64a lists).
  The words it closed on are: "without disparagement, yet so that ... notice" (S54); "for forty days", day 41 (S63, Q11); "but shall be held in some fixed place" (S143); "to the value of that debt" (S196); "without immediately tendering money" (S208); "when he is willing ... or ... by another responsible man" (S216) and "when vacant" (S334), where "when" can work as "if" and the author called S216 the most arguable of its scenarios; "against the will of" (S221, S227); "whereby a freeman may lose his court" (S242); "without credible witnesses" (S272); "As soon as peace is restored" (S365); the respite for possessions taken "by King Henry our father, or King Richard our brother", which does not say what follows for King John's own dispossession (S380, S384, S418); "after having been selected ... and after having been sworn" (S404, S405); and "from Easter in the sixteenth year ... till the restoration of peace" (S474, S475).
  The author's own verdict on each was that by the rule's list the encoder is right and that whether those words close a case is for a lawyer to rule.
  **These are the first thing for a lawyer to look at:** if the words do close a case, the encoding is wrong on the nineteen assertions above (S85 aside), all in the direction of saying "the Charter does not say" where a reader would say "no".
  S85 goes the other way: "shall not bear interest while the heir is under age" is a "while", the temporal twin of "as long as" (fork F64a), so for an heir of full age the encoding's `Not barred` is the text's own no, and the author's `Bar not covered` was the weaker answer.
- **Four were genuine forks, reconciled to the encoding's answer (S108, S321, S322, S516).**
  S108: whether "except for ransoming our person, ..." lifts the "unless by common counsel" requirement for a scutage as well as for the aids (fork F12; the encoding says it does not, on chapter 14's second mention of "a scutage").
  S321, S322 and the seat question S516 (chapter 44): "Men who dwell without the forest need not ... come before our justiciars of the forest upon a general summons, except those who are impleaded, or who have become sureties" lifts the exemption, but the text never itself says those men must come; the author leans to `Obliged`.
- **Three were the author's own inconsistencies (S160, S338/S339, S397).**
  In each the author's own class-limit rule gives "not covered" ("who were present at the county court on that day", "made such in our time", "unjustly and against the law of the land"), and S397 shows that the lack of a no-valued constructor in `Remedy` is consistent with the rule and not a gap in the type.
- **One did not fit the question (S22/S495).**
  The text gives a ceiling ("100s. at most for a whole knight's fee"), the seat question asks what I must give, and no function asks for the most that can be charged; the assertion is restated to `NOTHING` and the maximum chargeable is a gap in effect.

Thirty-eight assertions of the author's are restated in all (28 after its first run, 10 after the sweep); each is rewritten in place with a `-- RECONCILED 2026-10-30` comment that quotes the author's original and gives the reason, and none is deleted.
The encoder's own tests and seat cases were restated for the second pass in the same way (29 module assertions and 12 seat cases, with three seat cases added, so 579 module assertions and 331 seat cases), as its NOTES.md records.

**What the author could not decide from the text** (its best reading is in `ANSWERS.md`; compare the fork register).
Which words close a case, as above; chapter 39 reads "and by the law of the land" where the 1297 text reads "or" (the author took "and": both required); chapter 14's "after the expiry of at least forty days" (whether day 40 itself counts); chapter 7, day 41 (no, or not covered, since the text does not say she must leave); chapter 9, "any debt" (all debts, not only debts owed to the Crown); chapter 11, "in like manner" (whether it carries chapter 10's interest suspension to debts owed to others than Jews); chapter 2, the 100 pounds (the fixed ancient relief and also the ceiling, "at most" being said of the knight only); chapter 29, "relieved from guard in proportion to the time" (no ratio given); chapter 35, whether "one width of cloth" extends to cloths not in the parenthesis; chapter 48, whether the "provided always" proviso conditions the abolition and not the inquiry; chapter 61, whether "notified to four barons" means exactly or at least four, and whether a non-baron may be among the 25; chapter 62, "as far as pertains to us" (private claims between subjects fall outside); chapter 44 and chapter 12, as above.

**Independence caveat.**
`ANSWERS.md` was first written at 16:23:10 UTC on 2026-10-29, eleven seconds before the author first opened a module (16:23:21); it listed the file names of `enc/` only.
At 16:31:45 it appended a "Seat addendum" fixing its answer for each of the 126 seat questions, which it says in its own heading it wrote after listing the questions' names and inputs in `mc15-seat.l4` and before running anything; the numbered scenarios 486 to 540 are the 55 seat scenarios in a person's words that it wrote earlier.
Its tool calls contain no read under the commons or canon trees, `~/.claude/` or another run's folder; it read the translation, `ANSWERS.md`, the modules for names and types, the L4 documentation for syntax, and `daydate.l4` and `prelude.l4`.
**After its tests were written and run, the harness attached to its session the contents of four files of the lead's, at 16:48:16 UTC: the lead's staging script for these two encodings, the section of NOTES.md written for the 1297 encoding, the 1297 test author's report, and the body of the pull request for the interpretation-act rows.**
None concerns this encoding; the author's last write to `tests-independent.l4` was at 16:43:28, before they arrived, and it changed no expected value afterwards.
It classified S372 and S407 after the delivery, on the rule's "if" alone, and marked them arguable.
The encoder was not shown the assertions; it answered fix lists the lead wrote from the author's report.
It too was sent the four files, at 17:12:23 UTC, in the middle of its second fix list and after a summary of its context; it records that it did not open them with a tool and that nothing in the encoding was taken from them, and its next recorded step says it would not open them.
One of the four, the 1297 section of NOTES.md, discusses repairing a branch that answered "not covered" for a failed "if", which is what the lead's fix list also asked of it.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 30 modules, 1,398 satisfied (910 and 488), 0 failed, 0 refused, and every module `same` on the 1.6.102 build, run on 2026-10-30.
