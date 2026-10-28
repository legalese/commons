# The two Interpretation Laws and the forks of this row

Status: draft, written 2026-10-28, not reviewed by anyone who knows Jersey law.
How the figures below were verified: the check.sh figures are from a run on 2026-10-28 whose output was read (section 8); the counts of forks per bin are from `bins.json` in the writer's scratch directory, which is not deposited, and every row below was re-read against the fork text and the Laws' text on the day it was written.
Every reading in this document is "assumed, not ruled": nobody with authority has ruled on it.

## 1. What this document is

The Charities (Jersey) Law 2014 uses words that the Interpretation (Jersey) Law 1954 and the Legislation (Jersey) Law 2021 define or give rules for.
This row was made without those two Laws among its sources, so it recorded 137 places where the Charities Law can be read two ways (the forks, listed in NOTES.md section 5).
Both Laws are now encoded in full, each as a subject of its own in the commons: `subjects/je/interpretation-1954` (all seven consolidated texts from 1 January 2019) and `subjects/je/legislation-2021` (both texts), in the row `legalese-2026-10` of each.
This document sorts every fork of this row into one of four bins according to what those two Laws say about it, and says what was changed in this row as a result.

| Bin | Meaning | Forks |
| --- | --- | --- |
| Settled | A provision of the two Laws answers the question the fork asks, so one reading has licence and the other has none | 2 |
| Narrowed | A provision removes some readings or part of the question, and something remains | 7 |
| Open | The Laws touch the fork's subject and give no rule: a rule was looked for and is not there | 49 |
| Not reached | Nothing in either Law touches the fork's subject | 79 |

Only the settled forks were changed in this row (section 3).
The narrowed and the open forks stay forks, and become questions for the Legislative Drafting Office (section 7).

## 2. The sources, and the one hack

The texts are the consolidated versions on jerseylaw.je, deposited with their provenance in the two subjects (`source/` of each).
The 1954 Law is deposited in seven versions (1 Jan 2019 to 27 Sep 2021; then six more, the last from 19 Jun 2026), and its text before 1 January 2019 is not deposited.
Of the days from 28 March 2003 to 31 December 2018, the 1954 row answers four items only (Article 1(5), Article 1(6), and the Schedule's "month" and "midnight"), by inference from the endnotes of the 2019 consolidation, and says so in every answer.
Everything else it refuses for those days, as this row does for the Charities Law itself.
Neither Law defines "day", "week" or "year", and neither gives a rule for counting a period.
That was checked three ways: by the 1954 encoder's keyword search of all seven texts (NOTES.md section 7 of that row), by the 2021 encoder's search of both, and by the writer's own search on 2026-10-28 of the provisions of all nine texts (everything before the endnotes) for day, week, year, month, hour, period and sitting.
The provisions of the 1954 Law contain "day" only in Article 1(5), 1(6), 1(7) and the Schedule's definition of "midnight", and "month" only in the Schedule's definition of "month"; they contain no "week" or "year".
The provisions of the 2021 Law contain "day" in Article 3 and in the definition of "relevant period" (Article 8(2)), "months" in Article 15(9) and "sittings" in Article 11.

L4 cannot import across folders yet (relative imports have not reached main), and `check.sh` lets a group module import only `prelude`, `daydate`, `domain` and modules of its own group.
So the definitions that the tests need were COPIED by hand into `g7-interpretation-laws.l4`: 22 blocks, each textually identical to its source in the two other rows, each preceded by a comment naming the subject, the module and the Article.
The copies are a hack, assumed and not ruled; when relative imports reach main, that module is to be deleted and the tests to import the two rows.
`tools/sync-copies/sync-check.sh` compares each copied block with its source and says whether any has drifted; it must be re-run whenever either of the other two rows changes.
The two rows are, at the time of writing, committed on a local branch of the commons worktree (branch `je-interp-1954`) and not pushed.

## 3. Settled: 2 forks

### F7.11: how the day named as the day of commencement is counted

The reading taken is that the named day is the first day in force.
The other reading (the day after the named day) has no licence in either Law.

- **1954 Article 1(5)**, in the text in force from 1 January 2019 to 27 September 2021 (`interpretation-1954/source/l_17_1954_20210927.txt`, line 9): "Where an enactment is expressed or construed as being expressed to come into operation on a particular day, it shall be construed as coming into operation immediately on the expiration of the previous day."
- The endnotes of that text date Articles 1(5) and 1(6) to L.16/2003, in force 28 March 2003, so the same rule governed an enactment made from that day. That is an inference from the 2019 consolidation, not a reading of the text of 2003, which is not deposited.
- **2021 Article 3(2)** (`legislation-2021/source/l_8_2021.current.txt`, line 48): "If any Jersey legislation is expressed to come into force on a particular day, it is treated as coming into force at the beginning of that day, unless provision is made to the contrary."
- **2021 Article 3(6)** (line 54): "Nothing in this Article affects the commencement of any Jersey legislation that had commenced before the commencement of this Part." The Law came into force on 28 September 2021. So the 1954 rule governs an enactment that commenced before that day, and Article 3 governs one that commenced on or after it.
- The 1954 Law deleted Articles 1(5) and 1(6) from 28 September 2021 (endnotes of the current text); the 2021 Law took over.

Which Law governs which row of the Table of Legislation History of the Charities Law:

| Row | Day named | Commenced | Governs |
| --- | --- | --- | --- |
| Stage 1 of L.41/2014 | 21 November 2014 | before 28 Sep 2021 | 1954 Art 1(5), inferred text |
| Stage 2 (R&O.17/2018) | 1 May 2018 | before 28 Sep 2021 | 1954 Art 1(5), inferred text |
| Stage 3 (R&O.17/2018, made 6 March 2018) | 1 January 2019 | before 28 Sep 2021 | 1954 Art 1(5), inferred text |
| R&O.40/2019, L.1/2017, L.13/2019 (R&O.136/2019), R&O.29/2021 | 31 May 2019; 16 Dec 2019; 1 Jan 2020; 2 Mar 2021 | before 28 Sep 2021 | 1954 Art 1(5), deposited text |
| R&O.28/2023, R&O.56/2025, R&O.102/2026 | none: "7 days after it is made" | after 28 Sep 2021 | 2021 Art 3 applies, but they name no day: this is fork F7.2, which is not settled (section 5) |

Stages 1 to 3, and the four rows that name a day, all give the named day as the first day in force on both Laws; the Charities row's reading A gives the same day in every case, and its reading B (the day after) gives a day that neither Law gives.
Tests: `g7-tests-interpretation-laws.l4`, lines 82 to 171 (groups 1 and 2a, 43 assertions, hand-written expected values).

Caveats.

- Stage 1 was brought into force by Article 44(2) of the Law as enacted, which is not among the sources. The tests assume that the instrument names the day, as the Table says ("in force 21 November 2014"). If it does not, stage 1 is not settled by this.
- The 1954 text in force when the enactments of stages 1 and 2 were made is not deposited: the answer for them carries the basis "inferred from the endnotes of the 2019 consolidation, not verified against L.16/2003". The day is the same on either basis.
- R&O.10/2024 (9.30 a.m. on 27 February 2024) states a time of day. It is not settled by this and is in the narrowed bin (F7.1).

What changed in this row: no default and no rule. Added: the copies, the 43 assertions, and the status line in the register (NOTES.md section 5 and `FRAGMENT-G7.md`).

### F7.14: whether an Order under Article 2(2) can make consequential amendments of other provisions of the Law

The reading taken is that only Regulations can.
The other reading (the power to add sub-paragraphs carries the consequential amendments) has no licence in the 2021 Law.

- **2021 Article 9(5)** (line 97): "Unless provision is made to the contrary, a power to make Jersey subordinate legislation also authorises the making of provision incidental to, supplemental to, or consequential upon that legislation."
- **2021 Article 9(6)(b)** (line 100): "However, the power in paragraph (5) is limited ... (b) in the case of any legislation not made by the States, to amending any other legislation not made by the States."
- An Order of the Minister is signed, not adopted by the States Assembly (Article 2(3)(b)); the Charities Law is a Law, made by the States. So the incidental power of an Order cannot amend the Charities Law.
- That holds on both readings of "made by the States" (the 2021 row's fork L5): an Order is not made by the States on either, and a Law is on either. It holds on both readings of the 2021 row's fork L6.
- Article 39(1) of the Charities Law says the same in terms ("other than an amendment of this Law"); the 2021 Law is a second, independent ground. The one route to reading B would be "provision made to the contrary" within Article 9(5), and Article 39(1) says the opposite.
- R&O.56/2025, the one Order made under Article 2(2) in the sources, was made on 9 October 2025, after the 2021 Law came into force; it inserted paragraph (ba) in Article 2(1) and changed nothing else.

Tests: `g7-tests-interpretation-laws.l4`, lines 203 to 293 (group 3, 28 assertions).

Caveats.

- Article 9(5) has no date limit, whereas Article 9(2) is confined to legislation "made after 28th March 2003" and Article 9(1) says "(whenever made)". That Article 9(5) reaches a power conferred by a Law of 2014 is an inference from that contrast and from the date of the Order, not from a sentence of the text.
- The same Article does not bar Regulations from amending the Charities Law on the first reading of L5; on the second (a Law only) Regulations are not made by the States and are barred too. Whether Article 39(2) of the Charities Law is itself a provision to the contrary for Regulations under 9(6)(a) is not tested.

What changed in this row: no default and no rule. Added: the copies, the 28 assertions, the status line in the register.

## 4. Narrowed: 7 forks

### F1.6: does "in relation to Jersey" in 2(1)(e) qualify (iii) only, or each of (i) to (iii)?

The reading taken: only the Royal Charter in sub-paragraph (iii).
The text: 1954 Article 1(1): "enactment" means "any provision of any Law passed by the States and confirmed by Order in Council and any provision of any regulations, Order, rules, bye-laws, scheme or other instrument passed or made in Jersey under the authority of any Order in Council or under any such Law" (current text, line 5; the text to 27 September 2021 says "confirmed by Her Majesty in Council"), "unless a contrary intention appears".
What it removes: The case on which readings A and B of F1.6 differ for sub-paragraph (e)(i), a body established by an "enactment" that is not "in relation to Jersey", cannot arise if the Charities Law uses "enactment" in the 1954 sense, because every enactment is of Jersey.
What remains: The 1954 sense is subject to a contrary intention, and the words "in relation to Jersey" are themselves what a reader might take as one. Not changed.

### F1.8: does sub-paragraph (g) overlap (c), (d) and (f)?

The reading taken: as written, so a foundation or an incorporated 1862 association is also within (g).
The text: 1954 Article 2(b): "words in the singular shall include the plural and words in the plural shall include the singular" (line 15 of every text), unless the contrary intention appears.
What it removes: The only stated licence for reading B (the kinds of entity in sub-paragraphs (c), (d), (f) and (g) are mutually exclusive) was that Article 8(3)(a)(i) says "the sub-paragraph" in the singular. Article 2(b) removes that licence: the singular does not suggest exclusivity.
What remains: Whether the kinds are exclusive on other grounds remains. Not changed.

### F5.3: any Order under paragraph (7), (8) or (9) (13(10)); trap T18

The reading taken: the Order under paragraph (7) as extended by paragraph (8).
The text: 1954 Article 4(1): "The definitions in Part 1 of the Schedule shall, unless the contrary intention appears, apply to every enactment, whenever passed or made" (current text, line 21), and the Schedule, Part 1: "“under”, in relation to an enactment, shall include “by”, “in accordance with”, “pursuant to” and “by virtue of”" (line 116).
What it removes: Reading B says that paragraph (8) confers no Order of its own, so a relief Order that names "an Order under paragraph (8)" reaches nothing, and that the words are empty. Under the definition an Order made "by virtue of" paragraph (8) is an Order "under" it, and paragraph (8) says that an Order under paragraph (7) "may also make provision" as to the format and timing of the annual return, the consequences of lateness and the content of entries. So B's ground, that no such Order can exist, is removed.
What remains: The definition gives way to a contrary intention, and neither Law says whether the Order that the relief Order names is the whole Order under paragraph (7) or only the provisions of it made by virtue of paragraph (8). That is the discriminating case of the fork. Not changed.

### F7.1: how a day on which a text takes effect at a stated time is treated

The reading taken: a question about that day alone is refused.
The text: 2021 Article 3(2) (`legislation-2021/source/l_8_2021.current.txt`, line 48): "If any Jersey legislation is expressed to come into force on a particular day, it is treated as coming into force at the beginning of that day, unless provision is made to the contrary." R&O.10/2024 was made after 28 September 2021, so Article 3 governs it (Article 3(6)).
What it removes: The Law supplies a default for legislation that names only a day, the beginning of that day, so the fork is reduced to one question: whether the time the Order states, "9.30 a.m. on 27th February 2024", is "provision ... to the contrary".
What remains: Neither Law says whether a stated time of day is such provision (fork L2 of the 2021 row). If it is, the new text takes effect at 9.30 (reading A); if it is not, the whole of 27 February 2024 is in the new text (reading B). Both readings survive, one on each answer to L2. Not changed.

### F7.4: how the strict and the knowing offences combine for one act

The reading taken: both offences are made out.
The text: 1954 Article 12 (current text, line 66; the sentence is the same in all seven deposited texts, checked by search on 2026-10-28): "Where an act or omission constitutes an offence under 2 or more enactments ... the offender shall, unless the contrary intention appears, be liable to be prosecuted and punished under either or any of those enactments or under the customary law, but shall not be liable to be punished twice for the same offence." With Article 1(1) (line 5): an "enactment" is "any provision of any Law" and of the instruments made under one, so Articles 21 and 23 of the Charities Law are two enactments.
What it removes: Reading B (the knowing offence displaces the strict one) is a departure from Article 12, which makes the offender liable to be prosecuted under either or any of the offences unless a contrary intention appears. The only licence given for B, "one act, one wrong", is not a sentence of either Law, and nothing in Articles 21 or 23 says that one offence excludes the other.
What remains: Reading A as written also goes too far on penalties: Article 12 forbids punishing twice "for the same offence", and neither Law says whether the strict offence of Article 21 and the knowing offence of Article 23 are "the same offence". If they are, only one penalty can be imposed. Not changed.

### F7.7: on which date a notice is served

The reading taken: the date of receipt.
The text: 1954 Article 7: "Where an enactment ... authorizes or requires any document to be served by post ... the service shall be deemed to be effected by properly addressing, prepaying and posting a letter containing the document, and, unless the contrary is proved, to have been effected at the time at which the letter would be delivered in the ordinary course of post" (current text, line 27), unless the contrary intention appears.
What it removes: Where the Article applies, the date of service is neither the date of sending (reading B) nor the date of receipt (reading A) as such: it is the date the letter would be delivered in the ordinary course of post, unless the contrary is proved.
What remains: Article 7 applies only if an enactment authorizes or requires service by post. The Charities Law says nothing about post; Article 38 only lets the Minister make provision as to service by Order. So Article 7 applies if and only if an Order (or another enactment) authorizes post. For other modes of service, and for how long post takes, nothing is settled. Not changed.

### F8.8: in what unit is a term of imprisonment measured in Articles 26(7), 26(10) and 29(1)?

The reading taken: calendar months.
The text: 1954 Schedule, Part 1: "month" shall mean a calendar month (current text, line 105).
What it removes: For "a term of 3 months" (Article 26(7)), reading B (days, with a month counted as 30 days) has no licence: a calendar month is not 30 days.
What remains: "2 years" (Articles 26(10) and 29(1)) is not settled, because "year" is not defined. Not changed.

## 5. Open: 49 forks

For each of these a rule was looked for in the two Laws, in every version, and is not there.
Four general reasons account for 41 of them, and the same few questions to the drafters would close most of those (section 7).
The other 8 each have a nearest provision, named in the second table.

| Reason | Forks | Count |
| --- | --- | --- |
| no rule for counting a period of days | F2.6 F2.7 F3.4 F4.9 F5.5 F5.9 F5.10 F6.17 F6.20 F6.21 F6.22 F7.2 F8.7 F8.12 F9.1 F9.2 F9.4 F9.5 F9.14 | 19 |
| "year" is not defined | F3.2 F3.5 F4.6 F5.2 F5.11 F6.14 F6.16 F6.18 F7.8 F8.9 F8.10 F9.6 F9.13 | 13 |
| no rule for counting a calendar month | F4.1 F9.3 F9.7 | 3 |
| no meaning for "promptly" / "as soon as practicable" | F2.4 F4.10 F5.1 F6.12 F8.2 F9.10 | 6 |

What was looked for, by reason.

- **Counting days.** Whether the day of the event is counted, whether the last day is included, what "clear days" are. Neither Law has a rule, and neither defines "day". Article 1(5) and 3(2) say when an enactment comes into force; they do not count a period.
- **"Year".** "Month" is defined as a calendar month; "year" is not defined in either Law, in any version.
- **Calendar months.** The Schedule says only "a calendar month". It does not say how one is counted from a day, or what a month back from the 31st is. The readings of F4.1, F9.3 and F9.7 differ on exactly that.
- **Promptness.** "Promptly", "reasonable time", "as soon as practicable": neither Law gives a number of days. (The 2021 Law uses "as soon as practicable" in Article 11(1) without defining it.)

The forks with a nearest provision of their own:

| Fork | Nearest provision | What it does not say |
| --- | --- | --- |
| F1.1 | 1954 Article 9(2) and (3) | Article 9(2) reads a reference to a paragraph by letter alone as a reference to the paragraph of that letter in the Article, and Article 9(3) reads a reference to an enactment as a reference to it as amended. Neither says whether a range of letters, "(a) to (h)", written before an insertion takes in a paragraph inserted later between two of them. |
| F1.3 | 1954 Article 4(1) and the Schedule, "under" | Under the definition "under" includes "by", so "incorporated by (but not under)" (Article 2(5)(e)) names nothing unless "(but not under)" is a contrary intention, which Article 4(1) allows, or a slip. Neither Law says which, or what the constitutional Law of a body incorporated under but not by an enactment is. |
| F2.13 | 1954 Article 11(2) | A duty laid on the holder of an office as such is performed by the holder for the time being or, in absence or incapacity, by the person performing the duty of the office. Neither Law says whether a member of staff who exercises the Commissioner's function on the Commissioner's behalf (Schedule 1 paragraph 4(3) of the Charities Law) is bound as the Commissioner is. |
| F3.13 | 1954 Article 9(2) and (3) | The rules on references to provisions and to enactments as amended. Neither Law says whether a list of lettered sub-paragraphs written before an insertion takes in the sub-paragraph inserted later, (ba). |
| F7.3 | 2021 Article 14(1)(d)(iii) and (2), and Schedule 1(o) | The Drafter may correct errors in numbering when consolidating, the Board may renumber a provision in a revision, and a change of that kind cannot change meaning (Article 14(2)). These concern the editor's changes to the text. Neither Law says whether the numbers in a commencement table among the endnotes are the original numbers or the present ones. |
| F7.9 | 2021 Article 3(1) and (4) | Commencement is provision by provision, and a power to commence may name different days for different provisions. Neither Law says when a Part that has been brought into force in stages is itself "in force". |
| F9.15 | 1954 Articles 11(2) and 11A(2) (Article 11A from 28 September 2021) | Article 11A(2), about appointing to an office, lists "the office is vacant" and "the person holding the office is absent" as separate circumstances; Article 11(2) provides for the absence or incapacity of the holder. Neither says whether a vacant office is "absent" for Schedule 2 paragraph 4(1) of the Charities Law. |
| F9.18 | 1954 Article 2(b) | Words in the singular include the plural, so "the responsible officer" may denote several members of staff. Neither Law says whether it denotes the one the Minister names or every member available. |

Every open fork:

| Fork | Group | The question | Reason |
| --- | --- | --- | --- |
| F1.1 | G1 | does "(a) to (h)" reach the inserted sub-paragraph (ba)? | nearest provision, above |
| F1.3 | G1 | what is the constitutional Law of a body incorporated "under, but not by," an enactment? | nearest provision, above |
| F2.4 | G2 | within a reasonable time and "as soon as practicable" (periods P1 and P2) | no meaning for "promptly" / "as soon as practicable" |
| F2.6 | G2 | how the days of a period measured from an event are counted (periods P1 and P2 under F2.4's second reading) | no rule for counting a period of days |
| F2.7 | G2 | Before issuing or amending guidance (period P3) | no rule for counting a period of days |
| F2.13 | G2 | is a member of the Commissioner's staff, exercising the Commissioner's function, bound as the Commissioner is? | nearest provision, above |
| F3.2 | G3 | Article 8(3)(j): which year is "the most recent year"? | "year" is not defined |
| F3.4 | G3 | Every period of years: is the day of the event counted? | no rule for counting a period of days |
| F3.5 | G3 | Adding a year to a date that does not exist in the target year | "year" is not defined |
| F3.13 | G3 | Article 8(3)(a): does it reach sub-paragraph (ba) of Article 2(1)? | nearest provision, above |
| F4.1 | G4 | the 12 months preceding the application | no rule for counting a calendar month |
| F4.6 | G4 | a year before 29 February | "year" is not defined |
| F4.9 | G4 | counting the period for the Commissioner's decision | no rule for counting a period of days |
| F4.10 | G4 | reasonable time and as soon as practicable, for the guidance | no meaning for "promptly" / "as soon as practicable" |
| F5.1 | G5 | promptly (13(6)); period P8, a standard of promptness | no meaning for "promptly" / "as soon as practicable" |
| F5.2 | G5 | the year to which the return relates (13(7), 13(9)(a)); period P9, a reporting period; integration point IP33 | "year" is not defined |
| F5.5 | G5 | is a return sent on the due date timely? (13(8)); period P10, a deadline | no rule for counting a period of days |
| F5.9 | G5 | the first day of a period fixed by the court (14(3)(a), (b), (g)); a period fixed by an order | no rule for counting a period of days |
| F5.10 | G5 | counting the days when "promptly" is a number of days (13(6), readings B and C of F5.1) | no rule for counting a period of days |
| F5.11 | G5 | the anniversary of a registration made on 29 February (13(7), reading C of F5.2) | "year" is not defined |
| F6.12 | G6 | how a report is judged prompt under Article 19(2) | no meaning for "promptly" / "as soon as practicable" |
| F6.14 | G6 | how the fifteen years of Article 20(5) are counted | "year" is not defined |
| F6.16 | G6 | how a term of imprisonment of one year or two years is measured | "year" is not defined |
| F6.17 | G6 | when the Commissioner may deregister after giving the preliminary notice | no rule for counting a period of days |
| F6.18 | G6 | how the ten years of Article 17(1)(a) are counted | "year" is not defined |
| F6.20 | G6 | whether a declaration given on the day of the application is in time | no rule for counting a period of days |
| F6.21 | G6 | from when a governor who has been notified is in breach of Article 19(4) | no rule for counting a period of days |
| F6.22 | G6 | whether the last day named in a time limit is inside the permission | no rule for counting a period of days |
| F7.2 | G7 | how “7 days after it is made” is counted | no rule for counting a period of days |
| F7.3 | G7 | which numbering the commencement table speaks in | nearest provision, above |
| F7.8 | G7 | in what unit a term of imprisonment is counted | "year" is not defined |
| F7.9 | G7 | how a Part brought into force in two stages is treated | nearest provision, above |
| F8.2 | G8 | what is "as soon as practicable" in Article 26(6)? | no meaning for "promptly" / "as soon as practicable" |
| F8.7 | G8 | how is a period fixed by a notice counted (Articles 26(1)(a), (b) and 27(2))? | no rule for counting a period of days |
| F8.9 | G8 | does the one year end on the anniversary of the day it starts, or on the day before? | "year" is not defined |
| F8.10 | G8 | what is a year from 29 February in Article 26(5)(a)? | "year" is not defined |
| F8.12 | G8 | is the first day counted in an appeal time limit under Article 36(2)? | no rule for counting a period of days |
| F9.1 | G9 | at least 2 weeks before appointing (Sch 1 1(3), src:760; Sch 2 1(3), src:818; P29, P38) | no rule for counting a period of days |
| F9.2 | G9 | being not more than 6 years (Sch 1 1(5), src:762; Sch 2 1(5), src:820; P30, P39) | no rule for counting a period of days |
| F9.3 | G9 | resigns ... by giving not less than 3 months' notice in writing to the Minister (Sch 1 3(1)(a), src:780) and "one month's notice" (Sch 2 2(1)(a), src:826; P31, P40) | no rule for counting a calendar month |
| F9.4 | G9 | absent ... for a period longer than 4 consecutive weeks (Sch 1 3(2)(a), src:784) and "8 consecutive weeks" (Sch 2 2(2)(a), src:830; P32, P41) | no rule for counting a period of days |
| F9.5 | G9 | not more than 2 weeks after terminating the appointment (Sch 1 3(3), src:788; Sch 2 2(3), src:834; P33, P42) | no rule for counting a period of days |
| F9.6 | G9 | completes 12 years (whether consecutive or in aggregate) of service (Sch 1 3(4)(c), src:792; Sch 2 2(4)(c), src:838; P34, P43) | "year" is not defined |
| F9.7 | G9 | in no case later than 4 months after the end of that year (Sch 1 4(9), src:808; Sch 2 3(4), src:843; P36, P44) | no rule for counting a calendar month |
| F9.10 | G9 | as soon as practicable (Sch 1 4(9) and (10), src:808 and src:809; Sch 2 3(4) and (5), src:843 and src:844; P37, P44) | no meaning for "promptly" / "as soon as practicable" |
| F9.13 | G9 | a penalty not exceeding imprisonment for a term of 2 years and a fine (Sch 2 4(3)(f), src:857; P45, IP35) | "year" is not defined |
| F9.14 | G9 | Before appointing a person ... the Minister must seek the views (Sch 1 1(2), src:759; Sch 2 1(2), src:817) | no rule for counting a period of days |
| F9.15 | G9 | (b) the vice-chair, if the chair is absent; or (c) if both the chair and vice-chair are absent (Sch 2 4(1), src:846 to src:849) | nearest provision, above |
| F9.18 | G9 | at least one member of staff to serve as the responsible officer against "the responsible officer" (Sch 2 3(2), src:841, and 3(3) to (5), src:842 to src:844) | nearest provision, above |

## 6. Not reached: 79 forks

Nothing in either Law touches the subject of these forks.
They were checked, not assumed: the writer read each fork against the digest of both Laws, and a second reader, who had not seen this sort, did the same (section 9).
Three were looked at with particular care because a provision comes near them, and were kept here: F2.3 ("a Minister" against "the Minister"; 1954 Article 5 is about the formal and the common name of one office, not about the indefinite and the definite article), F4.3 (an application that does not comply; see question 6 of section 7) and F7.6 (which bodies are within Article 37(1)). None is answered by a provision of either Law.
Fourteen forks (F3.1, F3.6, F3.7, F4.2, F5.6, F5.13, F6.4, F6.5, F6.10, F6.13, F6.19, F8.1, F8.6, F9.12) are about the event from which a period runs, the day an entry takes effect, which year is meant, or whether a stated time must be reasonable.
Their periods are counted in days or years, which is why the first sort put them among the open forks; but the Laws' day rules are for the commencement of legislation only (1954 Article 1(5) and (6), 2021 Article 3), so they are silent on the event or the year the fork asks about, and the forks are here.

| Fork | Group | The question |
| --- | --- | --- |
| F1.2 | G1 | do the words "in relation to ..." in 2(10)(b) govern every limb (i) to (vi)? |
| F1.4 | G1 | which cases of the lists in 2(4) to 2(7) apply to a body in more than one kind? |
| F1.5 | G1 | is information "published" on the publisher's opinion or on the manner's likelihood? |
| F1.7 | G1 | is the standing of a "registered charity" read when the conduct occurred or when the question is asked? |
| F2.1 | G2 | all of its purposes with no purposes, and with ancillary purposes alone |
| F2.2 | G2 | acting in that capacity |
| F2.3 | G2 | a Minister or "the Minister" |
| F2.5 | G2 | a philosophical-belief purpose: (p) or (c)? |
| F2.8 | G2 | do the examples in 4(3) add to 4(2)? |
| F2.9 | G2 | so far appears to him or her to be reasonably practicable |
| F2.10 | G2 | what follows from a determination of public benefit made in breach of the duties on its maker |
| F2.11 | G2 | the promotion of equality and diversity |
| F2.12 | G2 | which guidance do Articles 5(6) to 5(8) apply to? |
| F2.14 | G2 | does Article 6(2)(e) add an operand to head (n)? |
| F3.1 | G3 | Article 8(6): from when do the ten years of retention run? |
| F3.3 | G3 | Article 10(4): does "a particular registered charity" include a deregistered entity? |
| F3.6 | G3 | The day on which an entry in a section takes effect |
| F3.7 | G3 | Article 8(3)(j): which year is the most recent, on the day asked? |
| F3.8 | G3 | Article 8(3)(k): is a notice noted once it has been complied with? |
| F3.9 | G3 | Article 8(4)(a): which entities are within "a company, foundation, or other entity required by its constitutional Law to have a registered office or business address in… |
| F3.10 | G3 | Article 8(4)(b), (c): main premises that are a private dwelling house |
| F3.11 | G3 | Article 8(5)(b): "if the entity was registered in the general section" |
| F3.12 | G3 | Article 9(2): who must meet the condition? |
| F4.2 | G4 | the date of "the application" |
| F4.3 | G4 | an application that does not comply |
| F4.4 | G4 | the duty to register against the bars on granting |
| F4.5 | G4 | is a formerly registered charity "another registered charity" |
| F4.7 | G4 | which names of another charity Article 12(1)(a) compares |
| F4.8 | G4 | a previous registered name of the charity itself |
| F4.11 | G4 | the payee who is a governor |
| F4.12 | G4 | applies or should be applied in Article 11(4)(f) |
| F5.4 | G5 | misconduct in the administration of the charity (14(1)(a)) |
| F5.6 | G5 | the day deregistration takes effect (13(1)); the period of registration |
| F5.7 | G5 | a purpose that is not charitable (13(2)) |
| F5.8 | G5 | paragraphs (a) and (b) of 13(5), joined by "or" |
| F5.12 | G5 | the three purposes of an order under 14(2) |
| F5.13 | G5 | when a matter "arises" for the annual return (13(7)) |
| F5.14 | G5 | which statement a payment is judged by (13(11)(a)) |
| F6.1 | G6 | what follows where the entity has not complied with Article 15(2) |
| F6.2 | G6 | how Article 16(2) relates to the procedure of Article 16(1) |
| F6.3 | G6 | which notice Articles 17(2)(c) and 17(4) mean |
| F6.4 | G6 | the date before which property must have been acquired to be remaining property |
| F6.5 | G6 | when the ten years of Article 17(1)(a) start |
| F6.6 | G6 | how long the bar on assigning the registered number lasts |
| F6.7 | G6 | which governors Article 18(2) binds |
| F6.8 | G6 | what the reasonable time of Article 18(4)(d)(ii) qualifies |
| F6.9 | G6 | whether a disqualification that has ended is a reportable matter |
| F6.10 | G6 | when the ban of Article 19(10) starts |
| F6.11 | G6 | whether acting in breach of Article 19(2) or (4) is an offence |
| F6.13 | G6 | whether the time for objections must be reasonable |
| F6.15 | G6 | how the duty in Article 19(9)(e)(i) stands against Article 28(3) |
| F6.19 | G6 | when the entity has failed to comply with a required steps notice |
| F6.23 | G6 | whose view of expediency lets a person apply under Article 20(3) |
| F6.24 | G6 | whether assisting another governor is misconduct only if that governor engages in misconduct |
| F7.5 | G7 | whether the wording of the advantage limb of the knowing offences is kept as printed or harmonised |
| F7.6 | G7 | which bodies are within Article 37(1) |
| F7.10 | G7 | how capacity is paired with the kind of body in Article 37(1) |
| F7.12 | G7 | whether Article 22 defines an excepted foreign charity outside Article 21 |
| F7.13 | G7 | whether adapting Articles 21 to 23 under Article 24(3)(a) can carry their imprisonment |
| F8.1 | G8 | when does the one year of Article 26(5)(a) start? |
| F8.3 | G8 | does Article 28(1)(a) "by virtue of Article 6(1)(c)" reach a philosophical-belief purpose? |
| F8.4 | G8 | is the list of appealable decisions in Article 33 closed? |
| F8.5 | G8 | on what ground is a decision of the tribunal appealed to the court? |
| F8.6 | G8 | from when does an appeal time limit under Article 36(2) run? |
| F8.11 | G8 | which consents does Article 29(1) require? |
| F8.13 | G8 | who is excluded from appealing under Article 33(5)? |
| F8.14 | G8 | does Article 27(1) "if the Commissioner believes that" make the belief alone the ground? |
| F8.15 | G8 | may a notice on any ground of Article 27(1) require a governor to be suspended, removed or replaced? |
| F8.16 | G8 | does Article 33(2)(a) "a decision to deregister the charity" reach a deregistration granted on the charity's own application? |
| F8.17 | G8 | when must a person have been a governor to fall within Article 26(2)(b)? |
| F8.18 | G8 | how do the two grounds of Article 33(5) combine with the two times? |
| F8.19 | G8 | which charity does Article 26(4)(a) speak of? |
| F9.8 | G9 | the decision under Article 15(3) on whether to refuse to deregister a charity (Sch 1 4(3)(b), src:798; trap T17) |
| F9.9 | G9 | subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 (Sch 1 2(4)(a), src:776, and 4(7), src:806; trap T22) |
| F9.11 | G9 | service as a designated relevant person (Sch 1 3(4)(c), src:792, with 4(4) and (5), src:800 to src:804) |
| F9.12 | G9 | a report "in each calendar year" for a year in which the office was held only in part (Sch 1 4(8), src:807; Sch 2 3(3), src:842; P35, P44) |
| F9.16 | G9 | the decision on entry in the restricted section (Sch 1 4(3)(a), src:797; Articles 9(6) and (7), src:280 to src:286; 11, src:298) |
| F9.17 | G9 | the person becomes a member of the States (Sch 1 3(4)(b), src:791; Sch 2 2(4)(b), src:837) |
| F9.19 | G9 | after satisfying himself or herself that the person has been absent ... for a period longer than (Sch 1 3(2)(a), src:784; Sch 2 2(2)(a), src:830) |

## 7. Questions for the Legislative Drafting Office

These are the questions whose answers would change this encoding.
They are written for the people who draft and read Jersey Laws, and they are not legal advice.
No question has been sent to anyone.

1. **Counting days.** Does Jersey drafting practice or case law count a period of days in a known way (the day of the event excluded or included; the last day included; "clear days" excluded at both ends), given that neither the Interpretation (Jersey) Law 1954 nor the Legislation (Jersey) Law 2021 says? This one answer would close 19 forks: F2.6 F2.7 F3.4 F4.9 F5.5 F5.9 F5.10 F6.17 F6.20 F6.21 F6.22 F7.2 F8.7 F8.12 F9.1 F9.2 F9.4 F9.5 F9.14.
2. **"Year".** Is a year in a Jersey Law a calendar year or twelve calendar months? ("Month" is defined as a calendar month; "year" is not defined.) It would close 13 forks: F3.2 F3.5 F4.6 F5.2 F5.11 F6.14 F6.16 F6.18 F7.8 F8.9 F8.10 F9.6 F9.13, and the "2 years" of F8.8.
3. **Calendar months.** When a period is a number of calendar months from a day, does it end on the corresponding day, and what is the last day when the corresponding day does not exist (30 November plus 3 months)? Does "the 12 months preceding" an application mean the 12 months to the day before, or whole calendar months? It would close 3 forks: F4.1 F9.3 F9.7.
4. **Promptness.** Is there a customary number of days for "promptly", "as soon as practicable" or "reasonable time" in a statute, or is it always a question of fact? 6 forks: F2.4 F4.10 F5.1 F6.12 F8.2 F9.10.
5. **A stated time of day.** Where an Order or an Act says it comes into force "at 9.30 a.m. on 27th February 2024", is that a "provision to the contrary" within Article 3(2) of the Legislation (Jersey) Law 2021, so that the earlier text governs until 9.30? F7.1 turns on it, and so does the 2021 row's fork L2.
6. **Deviation in forms (new).** Article 11(2) of the Charities Law requires the applicant to provide information to the Commissioner "in such form as the Commissioner may publish". Article 14 of the Interpretation (Jersey) Law 1954 says that, "Where a form is prescribed or specified by an enactment, deviations from that form not materially affecting the substance nor likely to mislead shall not invalidate the form used." Is a form published by the Commissioner under Article 11(2) a form "prescribed or specified by an enactment" (is the publication an "enactment" within Article 1(1)), so that an application that deviates from it in a way that is neither material nor likely to mislead still complies? If so, fewer applications "do not comply" for fork F4.3, which asks what an application that does not comply leads to. This does not settle F4.3 (not reached); it changes who is in it.
7. **Service by post.** Is service by post authorized by any enactment for the notices of the Charities Law (an Order under Article 38, or another enactment)? If so, Article 7 of the 1954 Law makes the date of service the date the letter would be delivered in the ordinary course of post; how long is that? (F7.7.)
8. **Stage 1.** What does Article 44(2) of the Charities Law as enacted say? It brought stage 1 into force and is not among the sources. If it names a day, F7.11 is settled for stage 1 as for the others.
9. **Article 9(5) of the Legislation (Jersey) Law 2021.** Does the incidental power of Article 9(5) and (6) reach a power conferred by a Law made before the 2021 Law (here, Article 2(2) of a Law of 2014)? The text has no date limit; Article 9(2) has one and Article 9(1) says "(whenever made)". (F7.14.)
10. **"Enactment".** Does the Charities Law use "enactment" in the sense of Article 1(1) of the 1954 Law, or is "in relation to Jersey" in Article 2(1)(e) a contrary intention? (F1.6.) Question 4 of section 7 of `FRAGMENT-G1.md` (what "enactment" means in 2(1)(e)(i) and 2(1)(g), and whether "partnership" includes the limited and separate limited partnerships) is answered by Article 1(1) for "enactment"; its half about "partnership" is not.
11. **Two offences for one act (F7.4).** Article 12 of the 1954 Law makes an offender liable to be prosecuted and punished under either or any of the enactments that create the offences, "but shall not be liable to be punished twice for the same offence", and Article 1(1) makes an "enactment" any provision of a Law. Are the strict offence of Article 21 and the knowing offence of Article 23 of the Charities Law "the same offence" for that purpose, so that only one penalty can be imposed when one statement is both?
12. **"Order under paragraph (8)" (F5.3).** Paragraph (8) of Article 13 lets an Order under paragraph (7) "also make provision" as to the format and timing of the annual return. Is such an Order an "Order under paragraph (8)" within Article 13(10), given that the 1954 Law says "under" includes "by virtue of", and does a relief Order that names it reach the whole Order or only the provisions made by virtue of paragraph (8)?

## 8. What changed in this row, and the checks

- Added `g7-interpretation-laws.l4` (the copies, 22 blocks), `g7-tests-interpretation-laws.l4` (83 assertions: 19 for the three stages, 36 for the Table rows after 1 January 2019 of which 12 are not F7.11, 28 for F7.14), `tools/sync-copies/` (the drift check) and this file.
- Annotated the two settled forks in NOTES.md (section 5, and section 16) and in `FRAGMENT-G7.md`; updated the module and assertion counts in NOTES.md (line 56) and `encoding.json`.
- Not changed: `domain.l4` (its sha is pinned by `check.sh`), every rule module, every default. No fork flipped.
- `check.sh` on 2026-10-28, with the prerelease `unstable-20261026-6325439`: 166 modules, 8224 assertions satisfied, 157 failed on purpose (157 expected), 10 refused on purpose (10 expected), 10 warnings (one per expected refusal), srcrefs 1730 src: lines, 891 runs, 1679 locators, 0 problems, GREEN. The baseline before this work, on the same binary: 164 modules, 8,141 satisfied, 157 failed (157 expected), 10 refused (10 expected), srcrefs 1730 / 891 / 1679 / 0. The difference is exactly the two new modules and their 83 assertions; every other line of the output is identical.
- The tests are not vacuous: six mutations on scratch copies (the 1954 rule giving the day after; the 2021 Article 3(6) cut-off moved to 2014; Article 9(6)(b) always met; Article 3(2) giving the next day; the taken reading of F7.11 changed; the taken reading of F7.14 changed) each made the stated number of assertions fail.

## 9. How the sort was checked, and its limits

- The first sort was the writer's, made before the two Laws were encoded, from the texts. On re-reading, three forks were moved from narrowed to open (F4.1, F9.3, F9.7) because "calendar month" does not choose between their readings; F7.1 was moved to open and, after the second sort, back to narrowed (below).
- A second reader, who had not seen the first sort or this document, sorted all 137 forks against the texts of the two Laws and checked every quotation in its table against the line it cites. It counted settled 4, narrowed 5, open 49, not reached 79. The two sorts differed on 27 forks. Each was settled by re-reading the fork and the provisions; none was settled by taking one sorter's word.
  - **Fourteen** that the first sort had as open (F3.1, F3.6, F3.7, F4.2, F5.6, F5.13, F6.4, F6.5, F6.10, F6.13, F6.19, F8.1, F8.6, F9.12) the second had as not reached; the second was right, for the reason in section 6.
  - **Seven** that the first sort had as not reached (F1.1, F1.3, F2.13, F3.13, F7.9, F9.15, F9.18) the second had as open, naming a nearest provision; the second was right (section 5).
  - **F7.4**: the first sort missed Article 12 of the 1954 Law; the second narrowed it, and so does this document.
  - **Five** differences remain, each a judgement. F5.3 and F7.1: the second sort called them settled; this document calls them narrowed, because the definition of "under" yields to a contrary intention and leaves the scope of the Order open (F5.3), and because the stated time of day may or may not be a "provision to the contrary" (F7.1). F7.3: the second sort called it narrowed; this document calls it open, because the nearest provisions are about the editor's powers and not about the numbers in an endnote table. F1.8: the first sort called it narrowed and the second not reached; it is kept as narrowed, weakly, since 1954 Article 2(b) removes only the licence given for reading B. F2.3: the second sort called it open through 1954 Article 5; it is kept as not reached, since Article 5 does not touch "a Minister" against "the Minister".
  - The boundary between open and not reached is a judgement, and nothing turns on it for the forks themselves: both stay forks. The boundaries between settled, narrowed and open are the ones that matter, and they are the ones section 3 and section 4 quote the text for.
- The two Laws' encodings have each had an independent test pass; the 2021 pass found one encoding error and the 1954 pass fourteen, all now corrected (NOTES.md section 10.3 of each row). The readings in those rows are assumed, not ruled, and no domain expert has read either encoding against its Law.
- The sort depends on those encodings only where they say what a Law does not say; the quotations in sections 3 and 4 were read from the deposited texts, with line numbers, on the day of writing.
- Nothing here has been sent to the Legislative Drafting Office or to anyone outside the session.
