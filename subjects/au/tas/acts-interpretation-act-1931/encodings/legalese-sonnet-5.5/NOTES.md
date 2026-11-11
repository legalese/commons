# Acts Interpretation Act 1931 (Tasmania): encoding notes

Status: draft.
No domain expert has read this encoding against the text.
Target compiler: `main`.
Written with l4 1.6.98 (main, 7689b0d, 2026-10-19); `check.sh` also ran every module with 1.6.110 (main, e51181d, 2026-11-11), and the counts agree for every module.
The text encoded is the consolidated version of 26 October 2022 of the Acts Interpretation Act 1931 (No. 59 of 1931), as current on the Tasmanian Legislation website on 12 November 2026.
The text file is an unofficial plain-text conversion of the site's consolidated HTML view, made by a converter script.
It is not the authorised version, and nothing here is verified against the authorised version.
Terms of the source text: `SOURCE-LICENSE.md` here points at the subject-level file `../../SOURCE-LICENSE.md`.
This file states the current reading of the encoding.
It is not a log of how the encoding was reached.

## Seat

The seat is a person who has a time limit to meet under a Tasmanian Act or statutory rule (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, and who asks on which day their period ends and which of their days count.
The Act is a set of rules for reading other Acts.
Its parts that touch such a person are the rules for counting time (s 29), for when an Act, a regulation or another instrument takes effect and stops (ss 9, 14, 16(4), 38A, 47), for what ends or survives a repeal (ss 15, 16, 18A), and for being served (ss 29AB, 30, 30A).
Provisions that address only an official (boards and offices, delegation, the making of regulations, judicial notice) are encoded in layer 1 for what they decide and appear in layer 2 only where they mean something to the person.
There is no seat for an official.
Layer 2 is `tas-seat.l4` (22 questions, each with `@export` and `@desc`, grouped under `§` headings in the order of the Act) and `tas-cases-seat.l4` (98 assertions, at least one for every question and an explicit not-covered case for every question that can answer NOTHING).
Every question calls a layer-1 rule and restates none.
The Act gives no statutory holidays, public holidays or sitting days of its own, so the person supplies the dates that do not count as a list.

| Question | Group | Cases |
| --- | --- | --- |
| On which day does an Act come into operation (s 9)? | When an Act or an instrument comes into operation and stops operating (ss 9, 14) | 7 |
| Is an Act, regulation or other instrument already in operation, or still in operation, at the start or the end of a given day (ss 9(5), 14(2))? | When an Act or an instrument comes into operation and stops operating (ss 9, 14) | 5 |
| Are the old provisions still in force on a given day, while the provisions that replace them have not yet come into operation (s 15(1))? | When a right or a liability ends (ss 15, 16, 18A) | 3 |
| May I still start or continue a legal proceeding about a right under an Act that has been repealed or has expired (s 16(1), (2))? | When a right or a liability ends (ss 15, 16, 18A) | 3 |
| Am I free from punishment for something I did after a temporary Act expired and before the Act continuing it was assented to (s 18A)? | When a right or a liability ends (ss 15, 16, 18A) | 7 |
| By which day must I act, if the Act gives me a number of days from a given day (s 29(1), (3), (6))? | Counting my time (s 29) | 8 |
| By which day must I act, if the Act gives me a number of calendar months from a given day (ss 29(1), (3), 46)? | Counting my time (s 29) | 7 |
| By which day must I act, if the Act gives me a number of years from a given day (s 29(1))? | Counting my time (s 29) | 2 |
| On or before which day must I act, if the Act gives me a number of days, counted backwards from a given day (s 29(1), (3)(b), (6))? | Counting my time (s 29) | 7 |
| On which day may I first act, if the Act requires a number of clear days after a given day (s 29(2))? | Counting my time (s 29) | 2 |
| On which day must I act at the latest, if the Act requires a number of clear days before a given day (s 29(2))? | Counting my time (s 29) | 2 |
| Is a given day one that does not count in my period, being a Sunday, a statutory holiday or a public holiday (s 29(3))? | Counting my time (s 29) | 4 |
| On which day may I file or register, if the last day of my period falls on a day when the office is not open (s 29(4))? | Counting my time (s 29) | 3 |
| On which day is my act in due time, if it is directed to be done on a particular day that is an excluded day (s 29(5))? | Counting my time (s 29) | 4 |
| Has a notice or other document been served on me in a way that section 29AB allows (s 29AB(1))? | Being served with a notice or document (ss 29AB, 30, 30A) | 9 |
| On which day am I taken to have been served with a notice or document that was sent to me by post (s 30(1))? | Being served with a notice or document (ss 29AB, 30, 30A) | 3 |
| On which day am I taken to have been served with a notice or document that was sent to me by registered post (s 30(2))? | Being served with a notice or document (ss 29AB, 30, 30A) | 5 |
| Can an infringement notice be served on me electronically (s 30A(a))? | Being served with a notice or document (ss 29AB, 30, 30A) | 3 |
| Am I taken to have been served with an infringement notice that was sent to me electronically (s 30A(b))? | Being served with a notice or document (ss 29AB, 30, 30A) | 3 |
| On which day does a proclamation or order-in-council that does not fix a commencement day take effect (s 38A(2)(d))? | When a proclamation or regulation takes effect, and when regulations are void (ss 38A, 47) | 2 |
| On which day do regulations made under an Act take effect (s 47(3)(d))? | When a proclamation or regulation takes effect, and when regulations are void (ss 38A, 47) | 2 |
| Are the regulations that affect me void because they were not published or notified in the Gazette in time, or take effect too early (s 47(3A))? | When a proclamation or regulation takes effect, and when regulations are void (ss 38A, 47) | 7 |

## What is encoded and what is not

Everything in the text from the title to the end of Schedule 1 has a row in the coverage table below.
Nothing is skipped.
Layer 1 has one module for each run of sections (`tas-ss01-04-application.l4` to `tas-ss48-sch1-rules-of-court-and-transitional.l4`), the nouns they share (`tas-nouns.l4`), the defined terms (`tas-terms.l4`), a provision index (`tas-provisions.l4`) and the cross-references (`tas-xrefs.l4`).
The rules for counting time are in one self-contained module, `tas-interpretation-time.l4`, which imports only `prelude` and `daydate` and has its tests in `tas-tests-time.l4`.
Each rule that is the main encoding of a provision carries an `@ref` with `src:` locators, and its tests give an expected value worked out by hand from the cited section.
About thirty of some 325 function definitions carry none of their own, counted block by block: helpers (the day positions, the earlier or later of two days, the month and counting helpers, the provision-index and cross-reference lookups) and derived functions that call a rule that does.
The dates and periods the text states are computed in `tas-interpretation-time.l4` and asserted in `tas-tests-time.l4`.
The amounts it states (20 and 5 penalty units, s 47(1)(e)) are computed and asserted in `tas-ss47-regulations.l4`, not in the time module.
Not encoded as rules: the short title (s 1) and the repeal of three earlier Acts (s 2), which are machinery; the title, long title, date of enactment and enacting words, which are not operative; and twelve provisions that the text shows only as a row of dots (s 4(4), 9(1), 21(1A), 24(c), 33, 42, 43(3), 45A, 46B, 46BA, 47(9), 49).
Facts the Act does not give are asked as inputs: the statutory holidays and public holidays (s 29(3)), the sitting days of a House (ss 44, 47), the day section 8 of the Acts Interpretation Amendment Act 1981 commenced (s 9), the commencement of the Legislation Publication Act 1996 (s 47(10), (11)), and the value of a penalty unit (ss 37, 47).
The tests use stated fixture values for them.
The Act defines "month" (s 46) and "financial year" (s 45(1)) and no other period word, so a period of years or of weeks answers NOTHING.

## Jural relations

One row for each provision that creates or preserves a relation between two parties, stated once and named neutrally.
Every other provision creates none and is listed in the last row.

| Provision | Holder | Bearer | Relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 6(6) | the Crown | an Act, and anyone relying on it | immunity and disability: no Act binds the Crown or derogates from a prerogative right unless express words are included | `s 6(6): an Act is not binding on the Crown and does not derogate from a prerogative right of the Crown` |
| s 11(1) | the person on whom the later-commencing provision confers a power | the persons subject to its exercise | power and liability: the power may be exercised before the provision commences, as far as necessary or expedient | `s 11(1): the power may be exercised although the provision conferring it has not commenced` |
| s 16(1), (2) | the holder of a right, privilege, claim or remedy acquired, accrued or incurred before a repeal or expiry | the person subject to it | the Act creates none; it preserves the relations, and the proceedings on them, that existed | `s 16(1) and (2) closing words: the investigation, proceeding, remedy or penalty may be instituted, continued, enforced or imposed as if the repealing Act had not been passed or the enactment had not expired` |
| s 18A | a person who did or omitted something between the expiry of a temporary enactment and the assent to its continuation | the authority that would punish (not named) | immunity and disability: no liability to punishment, penalty or forfeiture | `s 18A: the person is not liable to punishment, penalty or forfeiture for the thing done or omitted` |
| s 20(b) | the holder of an office for the time being | those subject to the power | power and liability: the holder exercises a power conferred on the office | `s 20(b): the person is the one by whom the power is to be exercised and the duty performed` |
| s 21(1) | the person with the power to appoint | the person appointed | power and liability: to suspend, remove, reinstate or temporarily replace | `s 21(1): the power to appoint includes the power` |
| s 21(2) | a person appointed | the appointing person | power and liability: to resign, the office being vacated on acceptance | `s 21(2): the office or position is vacated` |
| s 21(3)(b) | a former holder of a fixed-term office | not named | privilege and no-right: to continue until the earlier of two dates | `s 21(3)(b): the person may continue to exercise and perform the powers, authorities, functions and duties of the office on the day` |
| s 23AA(1) | a person with a power to delegate | the delegate | power and liability: to delegate a function or power | `s 23AA(1): the person may delegate the function or power to` |
| s 23AB | the Governor | the body concerned | power and liability: to declare a body duly established, constituted or appointed | `s 23AB: the Governor may declare the body duly established, constituted or appointed` |
| s 29(4) | a person filing or registering a document | the office | privilege and no-right: to file or register on the next ensuing day the office is open | `s 29(4): the last day on which a document may be filed or registered` |
| s 30A(a) | the person serving an infringement notice | the intended recipient | privilege and no-right: to serve it electronically if the recipient consents | `s 30A(a): the infringement notice may be served electronically` |
| s 32 | an offender | the authority that would punish (not named) | immunity and disability: not liable to be punished twice for the same offence | `s 32: the offender is not liable to be punished twice for the same offence` |
| s 47(1) | the Governor or a specified authority | the persons subject to the regulations | power and liability: to prescribe by regulations | `s 47(1): the regulations may prescribe the matter` |
| s 47(3)(a), (b) | the person making regulations (a duty to publish or notify within 21 days) | none named: the Act names no holder of a claim to it | duty without a named correlative | `s 47(3)(a) and (b): the regulations were published or notified in the Gazette within 21 days after the day they were made` |
| s 47(4) | either House of Parliament | the regulation and those it governs | power and liability: to disallow a regulation | `s 47(4): the regulation is void and ceases to have effect` |
| s 47(10), (12) | a regulation | a person who would challenge it | immunity and disability: not to be challenged for non-observance of the filing and recording | `s 47(12): the regulation may not be challenged on the ground of non-observance of subsection (11)` |
| none | every other provision | | Definitions, rules of reading, rules of construction, counting rules, rules of evidence and notice, and the savings and transitional clauses create no relation of their own. A counting rule decides on which day a period ends; the duty or right that the period governs is created by the Act that sets the period. | |

## Coverage table

The table has one row for each section, subsection, paragraph, subparagraph, Schedule, Schedule clause and defined term of the text (621 rows), and four rows for the title, long title, date of enactment and enacting words.
A script builds it from the text file and from the `@ref` lines of the modules, and checks that every non-blank line of the text from the title on falls inside some row.
It found none outside.
Counts by disposition: encoded 384, fork 223, inert 6, repealed or blank in this text 12 (total 625 rows).
Counts by kind of unit: 204 paragraphs, 155 subsections, 120 defined terms, 80 sections, 45 subparagraphs, 16 Schedule clauses, 1 schedule.
A row is `fork` where the text can be read in two or more ways with different outcomes; its "where" column gives the fork-register entry and the module that holds the rule.
Every row marked `fork` is encoded at the reading taken.
A row for a section, a Schedule or a subsection whose own text is only a heading or an opening phrase is marked from its parts ("through its parts").
The two `inert` rows for sections are s 1 (the short title) and s 2 (the repeal of three earlier Acts), both machinery; the other four `inert` rows are the title, long title, date of enactment and enacting words, which are not operative.
A row marked `repealed or blank in this text` is a provision that the text shows only as a row of dots.

| provision | lines | disposition | where |
| --- | --- | --- | --- |
| Title | 9 | inert | not operative |
| Long title | 11 | inert | not operative |
| Date of enactment | 13 | inert | not operative |
| Enacting words | 15 | inert | not operative |
| s 1 | 17-19 | inert | machinery: the short title |
| s 2 | 21-23 | inert | machinery: the repeal of three earlier Acts |
| s 2A | 25-29 | fork | F1; ss01-04-application |
| s 2A term: regulation | 29 | fork | F1; ss01-04-application, terms |
| s 3 | 31-33 | encoded | ss01-04-application |
| s 4 | 35-61 | encoded | through its parts; shown only as a row of dots, ss01-04-application |
| s 4(1) | 37-41 | fork | F2; ss01-04-application |
| s 4(1)(a) | 39 | fork | F2; ss01-04-application |
| s 4(1)(b) | 41 | fork | F2; ss01-04-application |
| s 4(1A) | 43-55 | encoded | through its parts; ss01-04-application |
| s 4(1A)(a) | 45 | encoded | ss01-04-application |
| s 4(1A)(b) | 47 | encoded | ss01-04-application |
| s 4(1A)(c) | 49-55 | encoded | ss01-04-application |
| s 4(1A)(c)(i) | 51 | encoded | ss01-04-application |
| s 4(1A)(c)(ii) | 53 | encoded | ss01-04-application |
| s 4(1A)(c)(iii) | 55 | encoded | ss01-04-application |
| s 4(2) | 57 | fork | F3; ss01-04-application |
| s 4(3) | 59 | encoded | ss01-04-application |
| s 4(4) | 61 | repealed or blank in this text | shown only as a row of dots |
| s 5 | 63-69 | encoded | through its parts; ss05-07a-enactments |
| s 5(1) | 65-67 | encoded | ss05-07a-enactments |
| s 5(1) term: Act | 67 | encoded | ss05-07a-enactments, terms |
| s 5(2) | 69 | encoded | ss05-07a-enactments |
| s 6 | 71-91 | encoded | through its parts; interpretation-time, ss05-07a-enactments |
| s 6(1) | 73 | encoded | ss05-07a-enactments |
| s 6(2) | 75 | encoded | ss05-07a-enactments |
| s 6(3) | 77 | encoded | ss05-07a-enactments |
| s 6(4) | 79-85 | fork | F4, F5; ss05-07a-enactments |
| s 6(4)(a) | 81 | fork | F4, F5; ss05-07a-enactments |
| s 6(4)(b) | 83-85 | fork | F4, F5; ss05-07a-enactments |
| s 6(5) | 87 | encoded | ss05-07a-enactments |
| s 6(6) | 89 | fork | F6; ss05-07a-enactments |
| s 6(7) | 91 | fork | F7; interpretation-time, ss05-07a-enactments |
| s 7 | 93-99 | encoded | through its parts; terms |
| s 7 term: prescribed | 95-99 | encoded | terms |
| s 7 term: prescribed (a) | 97 | encoded | ss05-07a-enactments, terms |
| s 7 term: prescribed (b) | 99 | encoded | ss05-07a-enactments, terms |
| s 7A | 101-109 | encoded | through its parts; ss05-07a-enactments |
| s 7A(1) | 103 | encoded | ss05-07a-enactments |
| s 7A(2) | 105 | encoded | ss05-07a-enactments |
| s 7A(2A) | 107 | encoded | ss05-07a-enactments |
| s 7A(3) | 109 | encoded | ss05-07a-enactments |
| s 8 | 111-117 | encoded | through its parts; ss08-10a-reading-and-commencement |
| s 8(1) | 113 | fork | F8; ss08-10a-reading-and-commencement |
| s 8(2) | 115-117 | encoded | ss08-10a-reading-and-commencement |
| s 8(2) term: the Principal Act | 117 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8A | 119-123 | encoded | through its parts; ss08-10a-reading-and-commencement |
| s 8A(1) | 121 | encoded | ss08-10a-reading-and-commencement |
| s 8A(2) | 123 | encoded | ss08-10a-reading-and-commencement |
| s 8B | 125-163 | encoded | through its parts; ss08-10a-reading-and-commencement, terms |
| s 8B(1) | 127-133 | encoded | ss08-10a-reading-and-commencement |
| s 8B(1)(a) | 129 | encoded | ss08-10a-reading-and-commencement |
| s 8B(1)(b) | 131 | encoded | ss08-10a-reading-and-commencement |
| s 8B(1)(c) | 133 | encoded | ss08-10a-reading-and-commencement |
| s 8B(2) | 135-141 | encoded | ss08-10a-reading-and-commencement |
| s 8B(2)(a) | 137 | encoded | ss08-10a-reading-and-commencement |
| s 8B(2)(b) | 139 | encoded | ss08-10a-reading-and-commencement |
| s 8B(2)(c) | 141 | encoded | ss08-10a-reading-and-commencement |
| s 8B(3) | 143-163 | encoded | through its parts; ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material | 145-161 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (a) | 147 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (b) | 149 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (c) | 151 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (d) | 153 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (e) | 155 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (f) | 157 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (g) | 159 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: extrinsic material (h) | 161 | encoded | ss08-10a-reading-and-commencement, terms |
| s 8B(3) term: ordinary meaning | 163 | encoded | terms |
| s 9 | 165-177 | encoded | through its parts; interpretation-time, shown only as a row of dots, ss08-10a-reading-and-commencement |
| s 9(1) | 167 | repealed or blank in this text | shown only as a row of dots |
| s 9(2) | 169 | encoded | interpretation-time, ss08-10a-reading-and-commencement |
| s 9(3) | 171 | encoded | interpretation-time, ss08-10a-reading-and-commencement |
| s 9(3A) | 173 | encoded | interpretation-time, ss08-10a-reading-and-commencement |
| s 9(4) | 175 | fork | F77; interpretation-time, ss08-10a-reading-and-commencement |
| s 9(5) | 177 | encoded | interpretation-time, ss08-10a-reading-and-commencement |
| s 10 | 179-181 | encoded | ss08-10a-reading-and-commencement |
| s 10A | 183-193 | encoded | through its parts; interpretation-time, ss08-10a-reading-and-commencement |
| s 10A(1) | 185-191 | fork | F9; ss08-10a-reading-and-commencement |
| s 10A(1)(a) | 187 | fork | F9; ss08-10a-reading-and-commencement |
| s 10A(1)(b) | 189 | fork | F9; ss08-10a-reading-and-commencement |
| s 10A(1)(c) | 191 | fork | F9; ss08-10a-reading-and-commencement |
| s 10A(2) | 193 | fork | F9; interpretation-time, ss08-10a-reading-and-commencement |
| s 11 | 195-237 | encoded | through its parts; ss11-13-anticipatory-powers-and-citation |
| s 11(1) | 197-209 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(1)(a) | 199 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(1)(b) | 201 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(1)(c) | 203 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(1)(d) | 205 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(1)(e) | 207-209 | fork | F10, F94; ss11-13-anticipatory-powers-and-citation |
| s 11(2) | 211-227 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(a) | 213 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b) | 215-227 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b)(i) | 217 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b)(ii) | 219 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b)(iii) | 221 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b)(iv) | 223 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(2)(b)(v) | 225-227 | fork | F11; ss11-13-anticipatory-powers-and-citation |
| s 11(3) | 229-235 | fork | F94; ss11-13-anticipatory-powers-and-citation |
| s 11(3)(a) | 231 | fork | F94; ss11-13-anticipatory-powers-and-citation |
| s 11(3)(b) | 233-235 | fork | F94; ss11-13-anticipatory-powers-and-citation |
| s 11(4) | 237 | fork | F12, F94; ss11-13-anticipatory-powers-and-citation |
| s 12 | 239-245 | encoded | through its parts; ss11-13-anticipatory-powers-and-citation |
| s 12(1) | 241 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 12(2) | 243 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 12(3) | 245 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13 | 247-283 | encoded | through its parts; ss11-13-anticipatory-powers-and-citation |
| s 13(1) | 249-267 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(a) | 251-255 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(a)(i) | 253 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(a)(ii) | 255 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(b) | 257 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(c) | 259 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(d) | 261-267 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(d)(i) | 263 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(1)(d)(ii) | 265-267 | fork | F13, F88; ss11-13-anticipatory-powers-and-citation |
| s 13(2) | 269 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(3) | 271-277 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(3)(a) | 273 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(3)(b) | 275 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(3)(c) | 277 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(4) | 279 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(5) | 281 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 13(6) | 283 | encoded | ss11-13-anticipatory-powers-and-citation |
| s 14 | 285-289 | encoded | through its parts; interpretation-time, ss14-18a-repeal-and-expiry |
| s 14(1) | 287 | fork | F14; interpretation-time, ss14-18a-repeal-and-expiry |
| s 14(2) | 289 | encoded | interpretation-time |
| s 15 | 291-297 | encoded | through its parts; ss14-18a-repeal-and-expiry |
| s 15(1) | 293 | fork | F15; ss14-18a-repeal-and-expiry |
| s 15(2) | 295 | fork | F16; ss14-18a-repeal-and-expiry |
| s 15(3) | 297 | encoded | ss14-18a-repeal-and-expiry |
| s 16 | 299-337 | encoded | through its parts; interpretation-time, ss14-18a-repeal-and-expiry |
| s 16(1) | 301-313 | fork | F17; ss14-18a-repeal-and-expiry |
| s 16(1)(a) | 303 | fork | F17; ss14-18a-repeal-and-expiry |
| s 16(1)(b) | 305 | fork | F17; ss14-18a-repeal-and-expiry |
| s 16(1)(c) | 307 | fork | F17; ss14-18a-repeal-and-expiry |
| s 16(1)(d) | 309 | fork | F17, F18; ss14-18a-repeal-and-expiry |
| s 16(1)(e) | 311-313 | fork | F17, F18; ss14-18a-repeal-and-expiry |
| s 16(2) | 315-327 | encoded | ss14-18a-repeal-and-expiry |
| s 16(2)(a) | 317 | encoded | ss14-18a-repeal-and-expiry |
| s 16(2)(b) | 319 | encoded | ss14-18a-repeal-and-expiry |
| s 16(2)(c) | 321 | encoded | ss14-18a-repeal-and-expiry |
| s 16(2)(d) | 323 | fork | F18; ss14-18a-repeal-and-expiry |
| s 16(2)(e) | 325-327 | fork | F18; ss14-18a-repeal-and-expiry |
| s 16(3) | 329-335 | encoded | ss14-18a-repeal-and-expiry |
| s 16(3)(a) | 331 | encoded | ss14-18a-repeal-and-expiry |
| s 16(3)(b) | 333-335 | encoded | ss14-18a-repeal-and-expiry |
| s 16(4) | 337 | encoded | interpretation-time |
| s 17 | 339-341 | encoded | ss14-18a-repeal-and-expiry |
| s 18 | 343-359 | encoded | ss14-18a-repeal-and-expiry |
| s 18(a) | 347-353 | encoded | ss14-18a-repeal-and-expiry |
| s 18(a)(i) | 349 | encoded | ss14-18a-repeal-and-expiry |
| s 18(a)(ii) | 351 | encoded | ss14-18a-repeal-and-expiry |
| s 18(a)(iii) | 353 | encoded | ss14-18a-repeal-and-expiry |
| s 18(b) | 355 | encoded | ss14-18a-repeal-and-expiry |
| s 18(c) | 357-359 | encoded | ss14-18a-repeal-and-expiry |
| s 18A | 361-363 | fork | F19, F20, F89; ss14-18a-repeal-and-expiry |
| s 19 | 365-367 | encoded | ss19-23-powers-and-appointments |
| s 20 | 369-375 | encoded | through its parts; ss19-23-powers-and-appointments |
| s 20(a) | 373 | encoded | ss19-23-powers-and-appointments |
| s 20(b) | 375 | fork | F21; ss19-23-powers-and-appointments |
| s 21 | 377-409 | encoded | through its parts; interpretation-time, shown only as a row of dots, ss19-23-powers-and-appointments |
| s 21(1) | 379-391 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(a) | 381 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(b) | 383 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(c) | 385 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(d) | 387-391 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(d)(i) | 389 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1)(d)(ii) | 391 | fork | F22; ss19-23-powers-and-appointments |
| s 21(1A) | 393 | repealed or blank in this text | shown only as a row of dots |
| s 21(1B) | 395 | fork | F23; ss19-23-powers-and-appointments |
| s 21(2) | 397 | fork | F24; ss19-23-powers-and-appointments |
| s 21(3) | 399-409 | encoded | through its parts; interpretation-time, ss19-23-powers-and-appointments |
| s 21(3)(a) | 401 | fork | F25; ss19-23-powers-and-appointments |
| s 21(3)(b) | 403-409 | fork | F26, F86; interpretation-time, ss19-23-powers-and-appointments |
| s 21(3)(b)(i) | 405 | fork | F26, F86; interpretation-time, ss19-23-powers-and-appointments |
| s 21(3)(b)(ii) | 407-409 | fork | F26, F86; interpretation-time, ss19-23-powers-and-appointments |
| s 21A | 411-447 | encoded | through its parts; ss19-23-powers-and-appointments, terms |
| s 21A(1) | 413-429 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(a) | 415-421 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(a)(i) | 417 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(a)(ii) | 419 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(a)(iii) | 421 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(b) | 423-429 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(b)(i) | 425 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(1)(b)(ii) | 427-429 | fork | F27; ss19-23-powers-and-appointments |
| s 21A(2) | 431-447 | encoded | through its parts; ss19-23-powers-and-appointments, terms |
| s 21A(2) term: appointing authority | 433-437 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: appointing authority (a) | 435 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: appointing authority (b) | 437 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: eligible person | 439 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: enactment | 441-447 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: enactment (a) | 443 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: enactment (b) | 445 | encoded | ss19-23-powers-and-appointments, terms |
| s 21A(2) term: enactment (c) | 447 | encoded | ss19-23-powers-and-appointments, terms |
| s 22 | 449-451 | fork | F28; ss19-23-powers-and-appointments |
| s 22A | 453-455 | fork | F29; ss19-23-powers-and-appointments |
| s 23 | 457-459 | encoded | ss19-23-powers-and-appointments |
| s 23AA | 461-497 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23AA(1) | 463-467 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(1)(a) | 465 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(1)(b) | 467 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(2) | 469-475 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23AA(2)(a) | 471 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(2)(b) | 473 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(2)(c) | 475 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(3) | 477 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(4) | 479 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(5) | 481-485 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23AA(5)(a) | 483 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(5)(b) | 485 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(5A) | 487-491 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23AA(5A)(a) | 489 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(5A)(b) | 491 | fork | F30; ss23aa-23e-delegation-and-bodies |
| s 23AA(6) | 493 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(7) | 495 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AA(8) | 497 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AAB | 499-501 | fork | F31; ss23aa-23e-delegation-and-bodies |
| s 23A | 503-507 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23A(1) | 505 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23A(2) | 507 | encoded | ss23aa-23e-delegation-and-bodies |
| s 23AB | 509-511 | fork | F32, F33; ss23aa-23e-delegation-and-bodies |
| s 23B | 513-523 | encoded | through its parts; ss23aa-23e-delegation-and-bodies |
| s 23B(1) | 515-521 | fork | F34; ss23aa-23e-delegation-and-bodies |
| s 23B(1)(a) | 517 | fork | F34; ss23aa-23e-delegation-and-bodies |
| s 23B(1)(b) | 519-521 | fork | F34; ss23aa-23e-delegation-and-bodies |
| s 23B(2) | 523 | fork | F35, F36, F84; ss23aa-23e-delegation-and-bodies |
| s 23C | 525-527 | fork | F37; ss23aa-23e-delegation-and-bodies |
| s 23D | 529-531 | fork | F38; ss23aa-23e-delegation-and-bodies |
| s 23E | 533-539 | fork | F39; ss23aa-23e-delegation-and-bodies |
| s 23E(a) | 537 | fork | F39; ss23aa-23e-delegation-and-bodies |
| s 23E(b) | 539 | fork | F39; ss23aa-23e-delegation-and-bodies |
| s 24 | 541-561 | fork | F40; ss24-28-construction |
| s 24(a) | 545 | fork | F40; ss24-28-construction |
| s 24(b) | 547 | fork | F40; ss24-28-construction |
| s 24(ba) | 549 | fork | F40; ss24-28-construction |
| s 24(bb) | 551-555 | fork | F40; ss24-28-construction |
| s 24(bb)(i) | 553 | fork | F40; ss24-28-construction |
| s 24(bb)(ii) | 555 | fork | F40; ss24-28-construction |
| s 24(c) | 557 | repealed or blank in this text | shown only as a row of dots |
| s 24(d) | 559-561 | fork | F40; ss24-28-construction |
| s 24A | 563-567 | encoded | through its parts; ss24-28-construction |
| s 24A(1) | 565 | fork | F90; ss24-28-construction |
| s 24A(2) | 567 | encoded | ss24-28-construction |
| s 25 | 569-571 | fork | F41; ss24-28-construction |
| s 26 | 573-575 | encoded | ss24-28-construction |
| s 27 | 577-585 | encoded | through its parts; ss24-28-construction |
| s 27(a) | 581 | encoded | ss24-28-construction |
| s 27(ab) | 583 | encoded | ss24-28-construction |
| s 27(b) | 585 | encoded | ss24-28-construction |
| s 28 | 587-589 | fork | F42; ss24-28-construction |
| s 29 | 591-607 | encoded | through its parts; interpretation-time |
| s 29(1) | 593 | fork | F73, F74, F75; interpretation-time |
| s 29(2) | 595 | encoded | interpretation-time |
| s 29(3) | 597-601 | fork | F73, F76;  |
| s 29(3) term: excluded days | 597 | fork | F73, F76; interpretation-time, terms |
| s 29(3)(a) | 599 | fork | F73, F76; interpretation-time |
| s 29(3)(b) | 601 | fork | F73, F76, F87; interpretation-time |
| s 29(4) | 603 | encoded | interpretation-time |
| s 29(5) | 605 | encoded | interpretation-time |
| s 29(6) | 607 | fork | F73; interpretation-time |
| s 29A | 609-617 | encoded | through its parts; ss29a-31-units-service-and-notices, terms |
| s 29A(1) | 611 | fork | F43; ss29a-31-units-service-and-notices |
| s 29A(2) | 613-617 | encoded | through its parts; ss29a-31-units-service-and-notices, terms |
| s 29A(2) term: Commonwealth Act | 615 | encoded | ss29a-31-units-service-and-notices, terms |
| s 29A(2) term: Commonwealth legal unit of measurement | 617 | encoded | ss29a-31-units-service-and-notices, terms |
| s 29AB | 619-635 | encoded | through its parts; ss29a-31-units-service-and-notices |
| s 29AB(1) | 621-629 | fork | F44; ss29a-31-units-service-and-notices |
| s 29AB(1)(a) | 623-627 | fork | F44; ss29a-31-units-service-and-notices |
| s 29AB(1)(a)(i) | 625 | fork | F44; ss29a-31-units-service-and-notices |
| s 29AB(1)(a)(ii) | 627 | fork | F44; ss29a-31-units-service-and-notices |
| s 29AB(1)(b) | 629 | fork | F44; ss29a-31-units-service-and-notices |
| s 29AB(2) | 631-635 | encoded | ss29a-31-units-service-and-notices |
| s 29AB(2)(a) | 633 | encoded | ss29a-31-units-service-and-notices |
| s 29AB(2)(b) | 635 | encoded | ss29a-31-units-service-and-notices |
| s 30 | 637-649 | encoded | through its parts; interpretation-time, ss29a-31-units-service-and-notices |
| s 30(1) | 639 | encoded | interpretation-time |
| s 30(2) | 641-647 | encoded | interpretation-time |
| s 30(2)(a) | 643 | encoded | interpretation-time |
| s 30(2)(b) | 645-647 | encoded | interpretation-time |
| s 30(3) | 649 | encoded | ss29a-31-units-service-and-notices |
| s 30A | 651-657 | encoded | through its parts; ss29a-31-units-service-and-notices |
| s 30A(a) | 655 | fork | F45; ss29a-31-units-service-and-notices |
| s 30A(b) | 657 | fork | F46, F91; ss29a-31-units-service-and-notices |
| s 31 | 659-669 | encoded | through its parts; ss29a-31-units-service-and-notices, terms |
| s 31(1) | 661 | fork | F92; ss29a-31-units-service-and-notices |
| s 31(2) | 663 | encoded | ss29a-31-units-service-and-notices |
| s 31(3) | 665 | fork | F93; ss29a-31-units-service-and-notices |
| s 31(4) | 667-669 | encoded | through its parts; ss29a-31-units-service-and-notices, terms |
| s 31(4) term: newspaper | 669 | encoded | ss29a-31-units-service-and-notices, terms |
| s 32 | 671-673 | fork | F47; ss32-38-offences |
| s 33 | 675-677 | repealed or blank in this text | shown only as a row of dots |
| s 34 | 679-681 | encoded | ss32-38-offences |
| s 35 | 683-687 | encoded | through its parts; ss32-38-offences |
| s 35(1) | 685 | encoded | ss32-38-offences |
| s 35(2) | 687 | encoded | ss32-38-offences |
| s 36 | 689-693 | encoded | through its parts; ss32-38-offences |
| s 36(1) | 691 | encoded | ss32-38-offences |
| s 36(2) | 693 | fork | F48; ss32-38-offences |
| s 37 | 695-717 | encoded | through its parts; ss32-38-offences |
| s 37(1) | 697 | fork | F50; ss32-38-offences |
| s 37(2) | 699 | encoded | ss32-38-offences |
| s 37(3) | 701-709 | encoded | ss32-38-offences |
| s 37(3)(a) | 703 | encoded | ss32-38-offences |
| s 37(3)(b) | 705 | encoded | ss32-38-offences |
| s 37(3)(c) | 707-709 | encoded | ss32-38-offences |
| s 37(4) | 711 | encoded | ss32-38-offences |
| s 37(5) | 713 | encoded | ss32-38-offences |
| s 37(5A) | 715 | encoded | ss32-38-offences |
| s 37(6) | 717 | fork | F49; ss32-38-offences |
| s 38 | 719-747 | encoded | through its parts; ss32-38-offences |
| s 38(1) | 721-727 | fork | F80, F85; ss32-38-offences |
| s 38(1)(a) | 723 | fork | F80, F85; ss32-38-offences |
| s 38(1)(b) | 725-727 | fork | F80, F85; ss32-38-offences |
| s 38(2) | 729-737 | fork | F80; ss32-38-offences |
| s 38(2)(a) | 731 | fork | F80; ss32-38-offences |
| s 38(2)(b) | 733 | fork | F80; ss32-38-offences |
| s 38(2)(c) | 735-737 | fork | F80; interpretation-time, ss32-38-offences |
| s 38(3) | 739-745 | fork | F80, F85; ss32-38-offences |
| s 38(3)(a) | 741 | fork | F80, F85; ss32-38-offences |
| s 38(3)(b) | 743-745 | fork | F80, F85; ss32-38-offences |
| s 38(4) | 747 | encoded | ss32-38-offences |
| s 38A | 749-791 | encoded | through its parts; interpretation-time, ss38a-40a-instruments-and-notice, terms |
| s 38A(1) | 751-757 | encoded | ss38a-40a-instruments-and-notice |
| s 38A(1)(a) | 753 | encoded | ss38a-40a-instruments-and-notice |
| s 38A(1)(b) | 755 | encoded | ss38a-40a-instruments-and-notice |
| s 38A(1)(c) | 757 | encoded | ss38a-40a-instruments-and-notice |
| s 38A(2) | 759-785 | encoded | through its parts; interpretation-time, ss38a-40a-instruments-and-notice |
| s 38A(2)(a) | 761 | fork | F78; ss38a-40a-instruments-and-notice |
| s 38A(2)(b) | 763 | fork | F78; ss38a-40a-instruments-and-notice |
| s 38A(2)(c) | 765-773 | encoded | interpretation-time |
| s 38A(2)(c)(i) | 767 | encoded | interpretation-time |
| s 38A(2)(c)(ii) | 769 | encoded | interpretation-time |
| s 38A(2)(c)(iii) | 771-773 | encoded | interpretation-time |
| s 38A(2)(d) | 775-785 | fork | F71; interpretation-time |
| s 38A(2)(d)(i) | 777 | fork | F71; interpretation-time |
| s 38A(2)(d)(ii) | 779-781 | fork | F71; interpretation-time |
| s 38A(2)(d)(iii) | 783 | fork | F71; interpretation-time |
| s 38A(2)(d)(iv) | 785 | fork | F71; interpretation-time |
| s 38A(3) | 787 | encoded | ss38a-40a-instruments-and-notice |
| s 38A(4) | 789-791 | encoded | through its parts; ss38a-40a-instruments-and-notice, terms |
| s 38A(4) term: prescribed instrument | 791 | encoded | ss38a-40a-instruments-and-notice, terms |
| s 39 | 793-795 | encoded | ss38a-40a-instruments-and-notice |
| s 39A | 797-805 | encoded | through its parts; ss38a-40a-instruments-and-notice |
| s 39A(1) | 799-803 | encoded | ss38a-40a-instruments-and-notice |
| s 39A(1)(a) | 801 | encoded | ss38a-40a-instruments-and-notice |
| s 39A(1)(b) | 803 | encoded | ss38a-40a-instruments-and-notice |
| s 39A(2) | 805 | encoded | ss38a-40a-instruments-and-notice |
| s 39B | 807-821 | encoded | through its parts; ss38a-40a-instruments-and-notice |
| s 39B(1) | 809-813 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(1)(a) | 811 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(1)(b) | 813 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(2) | 815-821 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(2)(a) | 817 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(2)(b) | 819 | encoded | ss38a-40a-instruments-and-notice |
| s 39B(2)(c) | 821 | encoded | ss38a-40a-instruments-and-notice |
| s 40 | 823-829 | encoded | through its parts; ss38a-40a-instruments-and-notice, terms |
| s 40(1) | 825-827 | encoded | through its parts; ss38a-40a-instruments-and-notice, terms |
| s 40(1) term: statutory authority | 827 | encoded | ss38a-40a-instruments-and-notice, terms |
| s 40(2) | 829 | fork | F51, F52; ss38a-40a-instruments-and-notice |
| s 40A | 831-833 | fork | F53; ss38a-40a-instruments-and-notice |
| s 41 | 835-843 | encoded | through its parts; ss41-45-definitions, terms |
| s 41(1) | 837 | encoded | through its parts; ss41-45-definitions, terms |
| s 41(1) term: person and party | 837 | fork | F54; ss41-45-definitions, terms |
| s 41(2) | 839-841 | encoded | through its parts; ss41-45-definitions, terms |
| s 41(2) term: committed for trial | 841 | encoded | ss41-45-definitions, terms |
| s 41(3) | 843 | encoded | through its parts; ss41-45-definitions, terms |
| s 41(3) term: oath, affidavit and swear | 843 | encoded | ss41-45-definitions, terms |
| s 42 | 845-847 | repealed or blank in this text | shown only as a row of dots |
| s 43 | 849-901 | encoded | through its parts; shown only as a row of dots, ss41-45-definitions, terms |
| s 43(1) | 851-889 | encoded | through its parts; ss41-45-definitions, terms |
| s 43(1) term: Australia | 853 | encoded | ss41-45-definitions, terms |
| s 43(1) term: British possession | 855 | encoded | ss41-45-definitions, terms |
| s 43(1) term: Central Plan Register | 857 | encoded | terms |
| s 43(1) term: coastal waters | 859 | encoded | terms |
| s 43(1) term: external Territory | 861 | encoded | ss41-45-definitions, terms |
| s 43(1) term: foreign country | 863 | encoded | ss41-45-definitions, terms |
| s 43(1) term: Government Printer | 865-869 | encoded | ss41-45-definitions, terms |
| s 43(1) term: Government Printer (a) | 867 | encoded | ss41-45-definitions, terms |
| s 43(1) term: Government Printer (b) | 869 | encoded | ss41-45-definitions, terms |
| s 43(1) term: internal Territory | 871 | encoded | ss41-45-definitions, terms |
| s 43(1) term: Jervis Bay Territory | 873 | encoded | terms |
| s 43(1) term: Northern Division | 875 | fork | F82; ss41-45-definitions, terms |
| s 43(1) term: Northern Territory | 877 | encoded | terms |
| s 43(1) term: Southern Division | 879 | fork | F82; ss41-45-definitions, terms |
| s 43(1) term: State | 881 | encoded | terms |
| s 43(1) term: Territory | 883 | encoded | terms |
| s 43(1) term: the Commonwealth | 885 | encoded | terms |
| s 43(1) term: the Governor | 887 | encoded | ss41-45-definitions, terms |
| s 43(1) term: the United Kingdom | 889 | encoded | terms |
| s 43(1A) | 891 | encoded | ss41-45-definitions |
| s 43(2) | 893-899 | encoded | through its parts; ss41-45-definitions, terms |
| s 43(2) term: northern area or northern region | 895 | encoded | ss41-45-definitions, terms |
| s 43(2) term: north-western area or north-western region | 897 | encoded | ss41-45-definitions, terms |
| s 43(2) term: southern area or southern region | 899 | encoded | ss41-45-definitions, terms |
| s 43(3) | 901 | repealed or blank in this text | shown only as a row of dots |
| s 44 | 903-919 | encoded | through its parts; interpretation-time, ss41-45-definitions, terms |
| s 44 term: Australia Acts | 907-911 | encoded | ss41-45-definitions, terms |
| s 44 term: Australia Acts (a) | 909 | encoded | ss41-45-definitions, terms |
| s 44 term: Australia Acts (b) | 911 | encoded | ss41-45-definitions, terms |
| s 44 term: Commonwealth Parliament | 913 | encoded | terms |
| s 44 term: Imperial Parliament | 915 | fork | F81; interpretation-time, ss41-45-definitions, terms |
| s 44 term: Parliament | 917 | encoded | terms |
| s 44 term: sitting-days | 919 | encoded | terms |
| s 45 | 921-983 | encoded | through its parts; interpretation-time, ss41-45-definitions, terms |
| s 45(1) | 923-955 | encoded | through its parts; interpretation-time, ss41-45-definitions, terms |
| s 45(1) term: Appropriation Act | 925-931 | encoded | ss41-45-definitions, terms |
| s 45(1) term: Appropriation Act (a) | 927 | encoded | ss41-45-definitions, terms |
| s 45(1) term: Appropriation Act (b) | 929 | encoded | ss41-45-definitions, terms |
| s 45(1) term: Appropriation Act (c) | 931 | encoded | ss41-45-definitions, terms |
| s 45(1) term: commencement | 933 | encoded | terms |
| s 45(1) term: the Department | 935 | encoded | terms |
| s 45(1) term: Financial Agreement | 937 | encoded | terms |
| s 45(1) term: financial year | 939 | encoded | interpretation-time, terms |
| s 45(1) term: Gazette | 941 | encoded | terms |
| s 45(1) term: gazetted | 943 | encoded | terms |
| s 45(1) term: the Minister | 945 | encoded | ss41-45-definitions, terms |
| s 45(1) term: order-in-council | 947 | encoded | ss41-45-definitions, terms |
| s 45(1) term: proclaim | 949 | encoded | terms |
| s 45(1) term: proclamation | 951 | encoded | ss41-45-definitions, terms |
| s 45(1) term: the Public Account | 953 | encoded | terms |
| s 45(1) term: the responsible Department | 955 | encoded | terms |
| s 45(2) | 957-969 | encoded | ss41-45-definitions |
| s 45(2)(a) term: the relevant enactment | 959 | encoded | ss41-45-definitions, terms |
| s 45(2)(a) | 959 | encoded | through its parts; ss41-45-definitions, terms |
| s 45(2)(b) | 961-965 | encoded | ss41-45-definitions |
| s 45(2)(b)(i) | 963 | encoded | ss41-45-definitions |
| s 45(2)(b)(ii) | 965 | encoded | ss41-45-definitions |
| s 45(2)(c) | 967-969 | encoded | ss41-45-definitions |
| s 45(3) | 971-983 | encoded | through its parts; ss41-45-definitions, terms |
| s 45(3) term: assigned | 973 | encoded | ss41-45-definitions, terms |
| s 45(3) term: department | 975 | encoded | terms |
| s 45(3) term: enactment | 977-983 | encoded | ss41-45-definitions, terms |
| s 45(3) term: enactment (a) | 979 | encoded | ss41-45-definitions, terms |
| s 45(3) term: enactment (b) | 981 | encoded | ss41-45-definitions, terms |
| s 45(3) term: enactment (c) | 983 | encoded | ss41-45-definitions, terms |
| s 45A | 985-987 | repealed or blank in this text | shown only as a row of dots |
| s 46 | 989-1095 | encoded | through its parts; interpretation-time, ss46-46c-common-phrases, terms |
| s 46 term: Australian lawyer | 993 | encoded | terms |
| s 46 term: Australian legal practitioner | 995 | encoded | terms |
| s 46 term: authorised deposit-taking institution | 997 | encoded | terms |
| s 46 term: Building Regulations | 999 | encoded | terms |
| s 46 term: commissioned police officer | 1001 | encoded | terms |
| s 46 term: Commissioner of Police | 1003 | encoded | terms |
| s 46 term: contravene | 1005 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: council | 1007 | encoded | terms |
| s 46 term: crime | 1009 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: enrolled nurse | 1011 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: estate | 1013 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: fail to comply with | 1015 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: Federal Court | 1017 | encoded | terms |
| s 46 term: fee unit | 1019 | encoded | terms |
| s 46 term: High Court | 1021 | encoded | terms |
| s 46 term: infringement notice | 1023 | encoded | terms |
| s 46 term: instigate | 1025 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: Integrity Commission | 1027 | encoded | terms |
| s 46 term: judge | 1029-1033 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: judge (a) | 1031 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: judge (b) | 1033 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: justice | 1035 | encoded | terms |
| s 46 term: land | 1037 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: local authority | 1039 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: Magistrates Court | 1041 | encoded | terms |
| s 46 term: medical practitioner | 1043 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: mental disorder | 1045 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: month | 1047 | fork | F74, F75; interpretation-time, terms |
| s 46 term: municipal area | 1049 | encoded | terms |
| s 46 term: newspaper | 1051 | encoded | terms |
| s 46 term: offence | 1053 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: paramedic | 1055 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: pharmacist | 1057 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: Plumbing Regulations | 1059 | encoded | terms |
| s 46 term: police officer | 1061 | encoded | terms |
| s 46 term: Police Service | 1063 | encoded | terms |
| s 46 term: psychopathic disorder | 1065 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: public place | 1067 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: registered nurse | 1069 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: State Service | 1071 | encoded | terms |
| s 46 term: State Service Agency | 1073 | encoded | terms |
| s 46 term: State Service employee | 1075 | encoded | terms |
| s 46 term: State Service employment | 1077 | encoded | terms |
| s 46 term: State Service officer | 1079 | encoded | terms |
| s 46 term: statutory declaration or solemn declaration | 1081-1087 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: statutory declaration or solemn declaration (a) | 1083 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: statutory declaration or solemn declaration (b) | 1085 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: statutory declaration or solemn declaration (c) | 1087 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: Supreme Court | 1089 | encoded | interpretation-time, ss46-46c-common-phrases, terms |
| s 46 term: Tasmanian Civil and Administrative Tribunal | 1091 | encoded | terms |
| s 46 term: town | 1093 | encoded | ss46-46c-common-phrases, terms |
| s 46 term: will | 1095 | encoded | ss46-46c-common-phrases, terms |
| s 46AA | 1097-1125 | encoded | through its parts; terms |
| s 46AA term: ASC Law | 1101 | encoded | terms |
| s 46AA term: ASC Regulations | 1103 | encoded | terms |
| s 46AA term: ASIC Law | 1105 | encoded | terms |
| s 46AA term: ASIC Act | 1107 | encoded | terms |
| s 46AA term: ASIC Regulations | 1109-1113 | encoded | terms |
| s 46AA term: ASIC Regulations (a) | 1111 | encoded | terms |
| s 46AA term: ASIC Regulations (b) | 1113 | encoded | terms |
| s 46AA term: Corporations Act | 1115 | encoded | terms |
| s 46AA term: Corporations Law | 1117 | encoded | terms |
| s 46AA term: Corporations legislation | 1119 | encoded | terms |
| s 46AA term: Corporations Regulations | 1121-1125 | encoded | terms |
| s 46AA term: Corporations Regulations (a) | 1123 | encoded | terms |
| s 46AA term: Corporations Regulations (b) | 1125 | encoded | terms |
| s 46A | 1127-1147 | encoded | through its parts; ss46-46c-common-phrases, terms |
| s 46A(1) | 1129-1133 | encoded | ss46-46c-common-phrases |
| s 46A(1)(a) | 1131 | encoded | ss46-46c-common-phrases |
| s 46A(1)(b) | 1133 | encoded | ss46-46c-common-phrases |
| s 46A(2) | 1135 | fork | F55; ss46-46c-common-phrases |
| s 46A(3) | 1137-1147 | encoded | through its parts; ss46-46c-common-phrases, terms |
| s 46A(3) term: Commonwealth Act | 1139 | encoded | terms |
| s 46A(3) term: law of the State | 1141-1147 | encoded | ss46-46c-common-phrases, terms |
| s 46A(3) term: law of the State (a) | 1143 | encoded | ss46-46c-common-phrases, terms |
| s 46A(3) term: law of the State (b) | 1145 | encoded | ss46-46c-common-phrases, terms |
| s 46A(3) term: law of the State (c) | 1147 | encoded | ss46-46c-common-phrases, terms |
| s 46B | 1149-1151 | repealed or blank in this text | shown only as a row of dots |
| s 46BA | 1153-1155 | repealed or blank in this text | shown only as a row of dots |
| s 46C | 1157-1171 | encoded | through its parts; interpretation-time, ss46-46c-common-phrases, terms |
| s 46C(1) | 1159-1163 | encoded | through its parts; ss46-46c-common-phrases, terms |
| s 46C(1) term: written law | 1159-1163 | encoded | ss46-46c-common-phrases, terms |
| s 46C(1) term: written law (a) | 1161 | encoded | ss46-46c-common-phrases, terms |
| s 46C(1) term: written law (b) | 1163 | encoded | ss46-46c-common-phrases, terms |
| s 46C(2) | 1165-1171 | encoded | interpretation-time, ss46-46c-common-phrases |
| s 46C(2)(a) | 1167 | encoded | interpretation-time, ss46-46c-common-phrases |
| s 46C(2)(b) | 1169-1171 | encoded | interpretation-time, ss46-46c-common-phrases |
| s 47 | 1173-1239 | encoded | through its parts; interpretation-time, shown only as a row of dots, ss47-regulations |
| s 47(1) | 1175-1189 | encoded | through its parts; ss47-regulations |
| s 47(1)(a) | 1177-1181 | fork | F56; ss47-regulations |
| s 47(1)(a)(i) | 1179 | fork | F56; ss47-regulations |
| s 47(1)(a)(ii) | 1181 | fork | F56; ss47-regulations |
| s 47(1)(b) | 1183 | fork | F56; ss47-regulations |
| s 47(1)(c) | 1185 | fork | F56; ss47-regulations |
| s 47(1)(d) | 1187 | fork | F56; ss47-regulations |
| s 47(1)(e) | 1189 | encoded | ss47-regulations |
| s 47(2) | 1191 | fork | F57; ss47-regulations |
| s 47(3) | 1193-1211 | encoded | ss47-regulations |
| s 47(3)(a) | 1195 | fork | F79; interpretation-time, ss47-regulations |
| s 47(3)(b) | 1197 | fork | F79; interpretation-time, ss47-regulations |
| s 47(3)(c) | 1199 | encoded | interpretation-time, ss47-regulations |
| s 47(3)(d) | 1201-1211 | fork | F72; ss47-regulations |
| s 47(3)(d)(i) | 1203 | fork | F72; ss47-regulations |
| s 47(3)(d)(ii) | 1205-1207 | fork | F72; ss47-regulations |
| s 47(3)(d)(iii) | 1209 | fork | F72; ss47-regulations |
| s 47(3)(d)(iv) | 1211 | fork | F72; ss47-regulations |
| s 47(3A) | 1213-1221 | fork | F58; ss47-regulations |
| s 47(3A)(a) | 1215 | fork | F58; ss47-regulations |
| s 47(3A)(b) | 1217 | fork | F58; ss47-regulations |
| s 47(3A)(c) | 1219-1221 | fork | F58; ss47-regulations |
| s 47(4) | 1223 | fork | F59, F60; interpretation-time, ss47-regulations |
| s 47(5) | 1225 | encoded | ss47-regulations |
| s 47(6) | 1227 | encoded | ss47-regulations |
| s 47(7) | 1229 | fork | F61, F95; interpretation-time, ss47-regulations |
| s 47(8) | 1231 | fork | F62; ss47-regulations |
| s 47(9) | 1233 | repealed or blank in this text | shown only as a row of dots |
| s 47(10) | 1235 | fork | F63, F64; interpretation-time, ss47-regulations |
| s 47(11) | 1237 | fork | F65; interpretation-time, ss47-regulations |
| s 47(12) | 1239 | fork | F66; ss47-regulations |
| s 48 | 1241-1247 | encoded | through its parts; ss48-sch1-rules-of-court-and-transitional, terms |
| s 48(1) | 1243-1245 | encoded | through its parts; ss48-sch1-rules-of-court-and-transitional, terms |
| s 48(1) term: rules of court | 1245 | encoded | ss48-sch1-rules-of-court-and-transitional, terms |
| s 48(2) | 1247 | encoded | ss48-sch1-rules-of-court-and-transitional |
| s 48A | 1249-1251 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| s 49 | 1253-1255 | repealed or blank in this text | shown only as a row of dots |
| Schedule 1 | 1257-1405 | encoded | through its parts; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 1 | 1259-1265 | fork | F67, F70; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 1(a) | 1263 | fork | F67, F70; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 1(b) | 1265 | fork | F67, F70; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 2 | 1267-1275 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 2(a) | 1271 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 2(b) | 1273-1275 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 3 | 1277-1283 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 3(a) | 1281 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 3(b) | 1283 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 4 | 1285-1291 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 4(a) | 1289 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 4(b) | 1291 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 5 | 1293-1299 | fork | F68, F83; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 5(a) | 1297 | fork | F68, F83; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 5(b) | 1299 | fork | F68, F83; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 6 | 1301-1313 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 6(a) | 1305-1311 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 6(a)(i) | 1307 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 6(a)(ii) | 1309-1311 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 6(b) | 1313 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 7 | 1315-1323 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 7(a) | 1319 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 7(b) | 1321 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 7(c) | 1323 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8 | 1325-1337 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(1) | 1327-1331 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(1)(a) | 1329 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(1)(b) | 1331 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(2) | 1333-1337 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(2)(a) | 1335 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 8(2)(b) | 1337 | fork | F68; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 9 | 1339-1341 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 10 | 1343-1349 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 10(a) | 1347 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 10(b) | 1349 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 11 | 1351-1357 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 11(a) | 1355 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 11(b) | 1357 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12 | 1359-1379 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(1) | 1361-1367 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(1)(a) | 1363 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(1)(b) | 1365-1367 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(2) | 1369-1379 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(2)(a) | 1371 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(2)(b) | 1373-1375 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(2)(c) | 1377 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 12(2)(d) | 1379 | fork | F69; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 13 | 1381-1387 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 13(a) | 1385 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 13(b) | 1387 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 14 | 1389-1395 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 14(a) | 1393 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 14(b) | 1395 | fork | F67; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 15 | 1397-1399 | encoded | ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 16 | 1401-1405 | fork | F70; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 16(1) | 1403 | fork | F70; ss48-sch1-rules-of-court-and-transitional |
| Sch 1 cl 16(2) | 1405 | fork | F70; ss48-sch1-rules-of-court-and-transitional |

## Fork register

Every place where the text can be read two or more ways with different outcomes, or where it does not choose, has one entry: the provision, the rule, the reading taken and the other reading.
The rulings that govern every rule are recorded here word for word, from the guide (section 5, rulings on negatives and legal effects, ruled 2026-11-04) and from the brief:

In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
From the guide, ruled 2026-11-05: "(a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
Also ruled 2026-11-05: "when", "upon" and "whenever" count as "where"; and for "the property does not pass until X" the bar is `JUST TRUE` before X and `JUST FALSE` after X.
Decided at each site, with one fork line each: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)".

Each entry below records a case the rulings leave to the encoder: an "unless" or "except" once met, a bare "must" not done, "listed in Schedule N", a duty whose "if" or "where" is unmet, and "(other than X)", or a place where the text can be read two ways.
A rule that returns a day, a name, a number or a text has no second not-covered value, so it returns `NOTHING` when its text does not apply; the last entry is that convention.

**F1. s 2A.** Rule: `s 2A: an instrument is within the word regulation in this Act`.
Taken: a rule or by-law where the contrary intention appears: JUST FALSE.
Other reading: NOTHING, the "unless" left open.

**F2. s 4(1).** Rule: `s 4(1): the provisions of this Act apply in interpreting the instrument`.
Taken: "Except where otherwise expressly provided" or "except in so far as" (a) or (b) is met: JUST FALSE.
Other reading: NOTHING, the exception treated as outside the text.

**F3. s 4(2).** Rule: `s 4(2): an Act is within a reference in this Act to an Act passed after a specified date`.
Taken: an Act passed on or before the specified date: NOTHING, because the subsection says what the reference includes and not what it leaves out.
Other reading: JUST FALSE, the date read as a period the text fixes.

**F4. s 6(4).** Rule: `s 6(4): the element is not taken to be part of the Act`.
Taken: a heading of a part, division or subdivision, a schedule or appendix, or a heading within one: JUST FALSE, "Except as provided in subsections (2) and (3)" being met.
Other reading: NOTHING.

**F5. s 6(4).** Rule: `s 6(4): the element is not taken to be part of the Act`.
Taken: a footnote appended to a prescribed form: JUST FALSE, the words "(other than ...)" take it out of the subsection in the text's own words, as "other than the Crown" takes the Crown out of s 41(1); the composite `s 6(2) to (4)` still answers NOTHING for it, because the text does not say it is part of the Act.
Other reading: NOTHING.

**F6. s 6(6).** Rule: `s 6(6): an Act is not binding on the Crown and does not derogate from a prerogative right of the Crown`.
Taken: named for the bar, so that express words included give JUST FALSE and none give JUST TRUE; "unless" met.
Other reading: a positive function "an Act is binding on the Crown", which would have to answer NOTHING once express words are included, because the section says what an Act is not and not what it is.

**F7. s 6(7).** Rule: `s 6(7): an Act is a public Act judicially noticed as such`.
Taken: "unless the contrary is expressly provided" met: JUST FALSE.
Other reading: NOTHING.

**F8. s 8(1).** Rule: `s 8(1): an amending Act is read and construed with the amended Act and deemed to be incorporated with it`.
Taken: "unless the contrary is expressly provided therein" met: JUST FALSE; an Act not passed to amend a previous Act: NOTHING, a scope limit with no "only".
Other reading: NOTHING for the "unless".

**F9. s 10A.** Rule: `s 10A: the construction of the word in the provision`.
Taken: the answer is one of three constructions, so where subsection (2) says subsection (1) applies "only" to a provision passed after the commencement, a provision passed earlier gets NOTHING; `s 10A(2): subsection (1) applies in respect of the provision` carries the JUST FALSE as a plain BOOLEAN.
Other reading: a MAYBE BOOLEAN wrapper that would lose the construction.

**F10. s 11(1).** Rule: `s 11(1): the power may be exercised although the provision conferring it has not commenced`.
Taken: "unless the contrary intention appears" met: JUST FALSE; a provision that does commence on the passing of the Act: JUST FALSE, a failed "Where"; a power exercised before the passing, or beyond what is necessary or expedient: NOTHING, because the grant is limited by its own wording.
Other reading: NOTHING for the "unless".

**F11. s 11(2).** Rule: `s 11(2): the power under the other Act may be exercised although the amending provision has not commenced`.
Taken: "unless the contrary intention appears" met: JUST FALSE; either limb of the "Where" failing: JUST FALSE.
Other reading: NOTHING for the "unless".

**F12. s 11(4).** Rule: `s 11(4): the person appointed may act in the office, or the body established may meet and perform its functions`.
Taken: a power that is not one of appointment or establishment, or not exercised under subsection (1) or (2): JUST FALSE, a failed "Where"; an act or meeting for a purpose outside subsections (1) and (2): JUST FALSE, "only".
Other reading: NOTHING.

**F13. s 13(1).** Rule: `s 13(1): an Act of the kind may be cited in the way`.
Taken: an Imperial Act, Commonwealth Act, or Act or Ordinance of another State or Territory with no short title, cited by short title: JUST FALSE, "if any" read as a condition introduced with "if"; an Act of this State with no short title, cited by short title: NOTHING, the paragraph has no "if any".
Other reading: NOTHING for "if any".

**F14. s 14(1).** Rule: `s 14(1): the repealing Act does not have the effect of reviving the former enactment`.
Taken: an Act passed on or before 5 August 1853: JUST FALSE, a failed "Where"; express words included: JUST FALSE, "unless" met.
Other reading: NOTHING for the date.

**F15. s 15(1).** Rule: `s 15(1): the repealed provisions remain in force on the day`.
Taken: the day the substituted provisions come into operation: JUST FALSE, because they operate from the first moment of that day (s 9(5)) and "until" ends the period there.
Other reading: JUST TRUE, the day counted as part of the period.

**F16. s 15(2).** Rule: `s 15(2): the regulation remains in force`.
Taken: a regulation rescinded under the repealing Act: JUST FALSE, "until rescinded" ends the period; a regulation not made under the repealed Act: NOTHING, the subsection speaks of "all regulations made under the repealed Act" and has no "only".
Other reading: NOTHING for a rescinded regulation.

**F17. s 16(1).** Rule: `s 16(1): the repeal does not revive or affect the matter`.
Taken: express words to the contrary: JUST FALSE, "unless" met.
Other reading: NOTHING.

**F18. s 16(1) and (2) closing words.** Rule: `s 16(1) and (2) closing words: the investigation, proceeding, remedy or penalty may be instituted, continued, enforced or imposed as if the repealing Act had not been passed or the enactment had not expired`.
Taken: read as subject to the same "unless the contrary is expressly provided" as the words before the dash; a matter other than paragraphs (d) and (e): NOTHING, the closing words name only those two and are a grant limited by their own wording.
Other reading: the closing words free of the "unless".

**F19. s 18A.** Rule: `s 18A: the temporary enactment is treated as continued in operation on the day`.
Taken: a day before the date of the expiration: JUST FALSE, "on and from" fixes the period.
Other reading: NOTHING, the enactment being in force by its own terms before then.

**F20. s 18A.** Rule: `s 18A: the person is not liable to punishment, penalty or forfeiture for the thing done or omitted`.
Taken: named for the text's "no person is liable", so JUST TRUE is the text's no; a thing done before the date of expiration or after the date of assent: JUST FALSE, "between" fixes the period; a thing not contrary to a provision of the temporary enactment: NOTHING.
Other reading: a positive "is liable" function.

**F21. s 20(b).** Rule: `s 20(b): the person is the one by whom the power is to be exercised and the duty performed`.
Taken: a power or duty not conferred or imposed on the holder of an office as such: JUST FALSE, "if conferred or imposed on the holder" read as a condition; a person who is not the holder for the time being: NOTHING, the paragraph says by whom, not only by whom.
Other reading: NOTHING for the "if".

**F22. s 21(1).** Rule: `s 21(1): the power to appoint includes the power`.
Taken: the power in paragraph (d)(i) or (d)(ii) when its "where" is unmet: JUST FALSE; the powers in (b) and (c) when no one has been suspended or removed: NOTHING, because those paragraphs carry no "where"; some other power: NOTHING, "includes".
Other reading: NOTHING for (d)(i) and (d)(ii), "includes" read as an open list that leaves the "where" open.

**F23. s 21(1B).** Rule: `s 21(1B): the powers conferred by subsection (1) are not exercisable`.
Taken: named for the text's "only", so JUST TRUE is the bar (a recommendation, approval or consent is required and not given) and JUST FALSE is a bar that does not apply; a failed "Where": JUST FALSE.
Other reading: a positive "are exercisable" function, which would have to answer NOTHING when the bar is lifted.

**F24. s 21(2).** Rule: `s 21(2): the office or position is vacated`.
Taken: a resignation not accepted: JUST FALSE, "on acceptance" read as "upon"; a resignation not in writing under his hand and addressed to the appointing person: NOTHING, the grant is limited by its own wording.
Other reading: NOTHING for the acceptance.

**F25. s 21(3)(a).** Rule: `s 21(3)(a): the person may be reappointed at the expiration of the term`.
Taken: a person no longer qualified as prescribed: JUST FALSE, "if he is still qualified" is an "if"; "unless" met: JUST FALSE.
Other reading: NOTHING for both.

**F26. s 21(3)(b).** Rule: `s 21(3)(b): the person may continue to exercise and perform the powers, authorities, functions and duties of the office on the day`.
Taken: a person reappointed: JUST FALSE, "if he is not so reappointed"; a day before the term expired or after the earlier of the two dates: JUST FALSE, the period the text fixes with "until"; a last day the arithmetic cannot give: NOTHING.
Other reading: NOTHING for a person reappointed.

**F27. s 21A(1).** Rule: `s 21A(1): the person may perform or exercise the duty, obligation, right or power in the same manner and to the same extent as if the person were the holder`.
Taken: any part of the "Where" unmet (no duty, an office of none of the three kinds, a holder neither unable nor absent): JUST FALSE; a person who is not an eligible person or not directed in writing: NOTHING, the grant is limited by its own wording.
Other reading: NOTHING for the "Where".

**F28. s 22.** Rule: `s 22: the included power is exercisable in the like manner and subject to the like consent and conditions`.
Taken: no consent or condition attaches to the power to make: JUST FALSE, "if any" read as an "if".
Other reading: NOTHING.

**F29. s 22A.** Rule: `s 22A: the included power is exercisable in a like manner and subject to the same consent and conditions`.
Taken: no consent or condition attaches to the power to grant: JUST FALSE, "if any" read as an "if".
Other reading: NOTHING.

**F30. s 23AA(5A)(b).** Rule: `s 23AA(5A)(b): the authority of the delegate continues`.
Taken: authority terminated by notice in writing: JUST FALSE, "until" ends the period.
Other reading: NOTHING.

**F31. s 23AAB.** Rule: `s 23AAB: the power to delegate includes a power to authorise another person to perform the function or exercise the power on behalf of the person giving the authorisation`.
Taken: no power to delegate conferred on the person: JUST FALSE, a failed "If"; sections 23AA and 23A applied to an authorisation, when no one has been authorised: NOTHING.
Other reading: JUST FALSE for the second.

**F32. s 23AB.** Rule: `s 23AB: the Governor may declare the body duly established, constituted or appointed`.
Taken: any of the Governor's satisfactions unmet, or fewer members than a quorum: JUST FALSE, the "Where" and the "if".
Other reading: NOTHING, because the Governor's power is a grant.

**F33. s 23AB.** Rule: `s 23AB: on the declaration the body is deemed to be duly constituted, established or appointed`.
Taken: no declaration made: JUST FALSE, "on the making of that declaration" read as "upon".
Other reading: NOTHING.

**F34. s 23B(1).** Rule: `s 23B(1): the Governor must obtain the assent of the committee or institution to the appointment`.
Taken: the committee cannot conveniently be consulted, or obtaining assent is not reasonably practicable: JUST FALSE, a duty whose "where" or "if" is unmet is taken not to arise.
Other reading: NOTHING.

**F35. s 23B(2).** Rule: `s 23B(2): the proclamation may not be questioned in a court by`.
Taken: named for the text's "No proclamation ... shall be questioned ... except by an order of review", so JUST TRUE is the bar and an order of review under the Judicial Review Act 2000 gives JUST FALSE, "except" met.
Other reading: a positive "may be questioned" function, which would answer NOTHING for an order of review because the section says how it may not be questioned and not how it may.

**F36. s 23B(2).** Rule: `s 23B(2): the act of the person ousted is deemed to be as valid for all purposes as if the person had been lawfully appointed`.
Taken: an act done on or after the date of judgment: JUST FALSE, "before the date of judgment" fixes the period.
Other reading: NOTHING.

**F37. s 23C.** Rule: `s 23C: the Act is deemed to empower the body to function, and its members to act, notwithstanding vacancies in the membership`.
Taken: fewer members in office than a quorum: JUST FALSE, "so long as" ends the period; a body of fewer than 2 members: JUST FALSE, a failed "Where".
Other reading: NOTHING.

**F38. s 23D.** Rule: `s 23D: the person may be paid the sum`.
Taken: a sum above what the person could have been paid had the Act commenced on the date of appointment: NOTHING, the grant is limited by its own wording and has no "only"; a payment for a day outside the period between the date of appointment and the date of commencement: JUST FALSE, the period the text fixes.
Other reading: JUST FALSE for the sum.

**F39. s 23E.** Rule: `s 23E: the power may also be exercised by`.
Taken: a person authorised otherwise than in writing, or any other person: NOTHING, the paragraphs name who may and the section has no "only"; no such power in an Act: JUST FALSE, a failed "Where".
Other reading: JUST FALSE for a person not named.

**F40. s 24.** Rule: `s 24: the derivative has a meaning corresponding with the definition`.
Taken: a word not defined in an Act: JUST FALSE, a failed "where"; a word that is not a derivative of the defined word: NOTHING, no "only".
Other reading: NOTHING for the "where".

**F41. s 25.** Rule: `s 25: the reference is deemed to include the other Minister`.
Taken: "unless the contrary intention appears" met: JUST FALSE; a Minister not for the time being acting for and on behalf of the referred-to Minister: NOTHING, "deemed to include" has no "only".
Other reading: NOTHING for the "unless".

**F42. s 28.** Rule: `s 28: the distance is measured in a straight line on a horizontal plane`.
Taken: "unless the contrary is expressly provided" met: JUST FALSE; a distance not measured for the purposes of an Act: NOTHING, "In the measurement of any distance for the purposes of any Act" is a scope limit with no "only".
Other reading: NOTHING for the "unless".

**F43. s 29A(1).** Rule: `s 29A(1): a reference in an Act to a unit of measurement is read as a reference to the Commonwealth legal unit of measurement`.
Taken: a day before the date from which the Commonwealth units are the sole legal units: JUST FALSE, "On and after" fixes the period; no Commonwealth legal unit of the same name: JUST FALSE, "if there is"; the date itself not known: NOTHING.
Other reading: NOTHING before the date.

**F44. s 29AB(1).** Rule: `s 29AB(1): the notice or document may be served on the person in the way`.
Taken: no Act authorizing, requiring or permitting service, or an Act that directs a particular manner: JUST FALSE, the "If" clause; a way the paragraphs do not name: NOTHING, because subsection (2) leaves other ways open.
Other reading: NOTHING for the "If".

**F45. s 30A(a).** Rule: `s 30A(a): the infringement notice may be served electronically`.
Taken: no consent from the intended recipient: JUST FALSE, "if the intended recipient consents" read as a condition introduced with "if"; a document that is not an infringement notice: NOTHING.
Other reading: NOTHING, "if" read as less than "only if".

**F46. s 30A(b).** Rule: `s 30A(b): the infringement notice is taken to have been served on the intended recipient`.
Taken: a notice not sent electronically to an address or number provided for that purpose: JUST FALSE, "if it is sent" read as a condition introduced with "if".
Other reading: NOTHING, "if" read as less than "only if".

**F47. s 32.** Rule: `s 32: the offender is not liable to be punished twice for the same offence`.
Taken: named for the text's "shall not be liable to be punished twice", so JUST TRUE is the bar; "Except as otherwise provided by the Criminal Code Act 1924" taken to govern this clause as well as the first, so that a different provision of that Act gives JUST FALSE; an offender not yet punished: NOTHING.
Other reading: a positive "is liable to be punished again" function.

**F48. s 36(2).** Rule: `s 36(2): the provision of the Criminal Code applies in relation to the offence`.
Taken: a provision of the Criminal Code not applicable to the offence: JUST FALSE, "so far as the same are applicable"; a case that is not a case under subsection (1): NOTHING, "In any such case as aforesaid" is a scope limit with no "only".
Other reading: JUST FALSE for the second.

**F49. s 37(6).** Rule: `s 37(6): the Penalty Units and Other Penalties Act 1987 does not affect or prejudice the application of section 37`.
Taken: named for the text's "Nothing in ... affects or prejudices", so JUST TRUE is the bar; a matter that is not the specification of a penalty in an Act: NOTHING.
Other reading: a positive "affects or prejudices" function.

**F50. s 37(1).** Rule: `s 37(1): the contravention or failure to comply is an offence punishable by a penalty not exceeding the one specified`.
Taken: "unless the contrary is expressly provided" met: JUST FALSE; a failed "Where": JUST FALSE.
Other reading: NOTHING for the "unless".

**F51. s 40(2).** Rule: `s 40(2): the citation is sufficient`.
Taken: a person who is not one of those named in the "If" clause (the Governor, a Minister, a statutory authority, a rule-making authority, a specified officer): JUST FALSE, the persons are part of the "If" clause; an instrument that does not cite the authorising Act: NOTHING, the text says what is sufficient and not what is insufficient.
Other reading: NOTHING for a person not named.

**F52. s 40(2).** Rule: `s 40(2): it is not necessary to recite or set forth the facts, circumstances or conditions precedent`.
Taken: named for the text's "it is not necessary", so JUST TRUE is the text's no; a failed "If": JUST FALSE.
Other reading: a positive "it is necessary" function.

**F53. s 40A.** Rule: `s 40A: the reference is to be read as a reference to the changed name of the body`.
Taken: a body that has not changed its name: JUST FALSE, a failed "If"; a reference that is not to the former name: NOTHING.
Other reading: NOTHING for the "If".

**F54. s 41(1).** Rule: `s 41(1): the expressions person and party include the body`.
Taken: the Crown: JUST FALSE, "other than the Crown" excludes it in the text's own words; a body of persons that is not the Crown: JUST TRUE; anything that is not a body of persons: NOTHING, "include".
Other reading: NOTHING for the Crown.

**F55. s 46A(2).** Rule: `s 46A(2): the rule of law applies to, or in relation to, or has effect with respect to, the person`.
Taken: a rule of law that does not apply to an alien: JUST FALSE, a failed "Where"; an Australian citizen: NOTHING, the subsection says the rule applies to a person who is not a citizen and has no "only".
Other reading: NOTHING for the "Where".

**F56. s 47(1).** Rule: `s 47(1): the regulations may prescribe the matter`.
Taken: a matter inconsistent with the Act, or repugnant to an express enactment in force: NOTHING, the paragraph grants power over matters "not inconsistent" and "not repugnant" and has no "only"; the Act not providing that the Governor or a specified authority may make regulations: JUST FALSE, a failed "Where".
Other reading: JUST FALSE for the inconsistent matter.

**F57. s 47(2).** Rule: `s 47(2): the document is a sufficient compliance with the Act`.
Taken: a deviation calculated to mislead or prejudice a person: JUST FALSE, "provided that" read as a condition; forms not prescribed: JUST FALSE, a failed "Where"; a document not in the prescribed form or to the like effect: NOTHING.
Other reading: NOTHING for the proviso.

**F58. s 47(3A).** Rule: `s 47(3A): the regulations are void`.
Taken: none of paragraphs (a), (b) and (c) holds: JUST FALSE, a failed "Where"; a publication day that the caller does not supply is read as not published.
Other reading: NOTHING when none holds.

**F59. s 47(4).** Rule: `s 47(4): the regulation is void and ceases to have effect`.
Taken: no resolution, or notice given outside the first 15 sitting days after the regulation is laid: JUST FALSE, a failed "If" and a period the text fixes; the sitting days supplied too few to find the fifteenth: NOTHING.
Other reading: NOTHING for the "If".

**F60. s 47(4).** Rule: `s 47(4): the thing done under the regulation is unaffected by the resolution`.
Taken: a thing done on or after the day the resolution was passed: JUST FALSE, "except as regards anything done thereunder prior to the passing" fixes the period, and the day of the passing is not prior to it.
Other reading: NOTHING.

**F61. s 47(7).** Rule: `s 47(7): the new regulation may not take effect on the day`.
Taken: named for the text's "no regulation ... shall take effect until", so JUST TRUE is the bar; a regulation made outside the 12 months after the disallowance: JUST FALSE, the period the text fixes (the day of disallowance counted in); a House resolution allowing it sooner: JUST FALSE, "unless" met; a regulation not to the same or substantially the same effect: NOTHING; sitting days supplied that do not reach the 30th sitting day: JUST TRUE (the bar still applies on the days known).
Other reading: a positive "may take effect" function.

**F62. s 47(8).** Rule: `s 47(8): the regulations are to be made by the Governor`.
Taken: an Act that does not provide for regulations, or that specifies the authority: JUST FALSE, a failed "Where".
Other reading: NOTHING.

**F63. s 47(10).** Rule: `s 47(10): the regulation is to be filed and recorded in the office of the Attorney-General`.
Taken: a regulation made before the passing of the Act or on or after the commencement of the Legislation Publication Act 1996: JUST FALSE, the period the text fixes.
Other reading: NOTHING.

**F64. s 47(10).** Rule: `s 47(10): the regulation may not be challenged on the ground of non-observance of the filing and recording`.
Taken: named for the text's "no regulation shall be challenged"; a challenge on some other ground: NOTHING, a scope limit with no "only"; the function takes the ground of the challenge and not the regulation's date, because the words "no regulation" are not limited to the period.
Other reading: a function limited to regulations made in the period.

**F65. s 47(11).** Rule: `s 47(11): the regulation is to be filed and recorded by the Chief Parliamentary Counsel in the responsible Department in relation to the Legislation Publication Act 1996`.
Taken: a regulation made before the commencement of the Legislation Publication Act 1996: JUST FALSE, "on or after the commencement" fixes the period.
Other reading: NOTHING.

**F66. s 47(12).** Rule: `s 47(12): the regulation may not be challenged on the ground of non-observance of subsection (11)`.
Taken: a challenge on another ground: NOTHING.
Other reading: JUST FALSE.

**F67.
Schedule 1 clauses 1, 2, 4, 6(a), 10, 11, 13, 14.** Rule: `Schedule 1 clause 1: section 4 as amended applies in the interpretation and construction of the regulations` and the other clauses built on `Schedule 1: the thing was in operation at the commencement, or came into operation after it`.
Taken: a thing that ceased to be in operation before the commencement: NOTHING, because each clause applies the section to a thing "that" is in operation at the commencement or comes into operation after it, a relative clause with no "only".
Other reading: JUST FALSE.

**F68.
Schedule 1 clauses 3, 5 and 8.** Rule: `Schedule 1 clause 3: section 7 as substituted applies to the reference to the expression prescribed`, `Schedule 1 clause 5: the power conferred by section 11 as substituted is exercisable`, `Schedule 1 clause 8: section 21 as amended applies to the Act which confers a power to appoint a person to an office or position`.
Taken: an Act outside the limbs: JUST FALSE, these clauses are worded "where" (clauses 3 and 8) or "is exercisable where" (clause 5).
Other reading: NOTHING.

**F69.
Schedule 1 clause 12.** Rule: `Schedule 1 clause 12: section 38A as substituted applies to the proclamation, order-in-council or prescribed instrument`.
Taken: an instrument made before the commencement that took effect before it: NOTHING, a relative clause with no "only".
Other reading: JUST FALSE.

**F70.
Schedule 1 clause 16(1).** Rule: `Schedule 1 clause 16(1): section 47 as amended applies to the regulations`.
Taken: regulations made before the commencement: JUST FALSE, the same clause says section 47 as in force before the commencement continues to apply to them "as if section 21 ... had not been enacted".
Other reading: NOTHING, "applies to regulations made after" read as a scope limit with no "only".

**F71. s 38A(2)(d).** Rule: `s 38A(2)(d): an instrument may not be expressed to take effect on a day before publication or notification`.
Taken: named for the text's "shall not be expressed", so JUST TRUE is the bar (a day preceding the date of publication or notification, where rights or privileges would be prejudiced or liabilities imposed) and JUST FALSE is a "where" that fails; a day that does not precede the date: NOTHING.
Other reading: a positive "may be expressed" function, which would answer NOTHING when the "where" fails.

**F72. s 47(3)(d).** Rule: `s 47(3)(d): the regulations may not be expressed to take effect on a day before publication or notification`.
Taken: the same reading as s 38A(2)(d), carried across by the wrapper.
Other reading: the same alternative.

**F73. s 29(3) and s 29(6).** Rule: `s 29: the last day for doing an act within a number of days reckoned forwards from`.
Taken: for a time of 1 to 6 days only s 29(6) is applied, forwards and backwards: the days counted are the days that are not excluded days, and s 29(3)(a) or (b) is not applied a second time to the end of the count; 3 days from Friday 2 January 2026 end on Tuesday 6 January 2026, and 3 days before Monday 12 January 2026 begin on Thursday 8 January 2026.
Other reading: s 29(1) and then s 29(3)(a) or (b): the same times give Monday 5 January 2026 and Friday 9 January 2026, the third day counted by s 29(1) in each case being a day that is not an excluded day.

**F74. s 29(1) and s 46, calendar months.** Rule: `s 29(1) and s 46: the last day of a period of calendar months reckoned forwards from`.
Taken: a period of calendar months from a given day ends on the day of the same number in the month reached, the given day not being counted (s 29(1)); where that month has no such day (a 31st in a month of 30 days, 29 February in a common year) the answer is NOTHING, because the Act says nothing about it.
Other reading: the last day of the later month (the clamping that the library's own month arithmetic applies), or the day before the day of the same number; the Act chooses neither.

**F75. s 29(1), years and weeks.** Rule: `s 29(1): the last day of a period of years reckoned forwards from`, `s 29(1): the last day of a period of weeks reckoned forwards from`.
Taken: the Act defines neither "year" nor "week" (it defines "financial year" only, in s 45(1)), so a period of years or of weeks answers NOTHING for every start day and every count.
Other reading: a year as 12 calendar months and a week as 7 days; neither is in the text.

**F76. s 29(3), the days that do not count.** Rule: `s 29(3): a day is an excluded day`.
Taken: the caller supplies every statutory holiday (Statutory Holidays Act 2000) and every public holiday where the act is to be done, the Act and the other deposited sources giving none; a day that is not a Sunday and is not on the caller's list is not an excluded day.
Other reading: NOTHING for a day not on the list, because the Act points to holidays that it does not list.

**F77. s 9(4).** Rule: `s 9(4): the day an Act reserved for the signification of the Sovereign's pleasure comes into operation`.
Taken: "after the commencement of section 8" is read as on or after the day on which section 8 commenced, because by s 9(5) a section commences at the first moment of its day and an Act reserved later on that day is reserved after the commencement.
Other reading: strictly after that day, so that an Act reserved on the day itself gets NOTHING.

**F78. s 38A(2)(a) and (b).** Rule: `s 38A(2)(a) and (b): the step to be taken in the Gazette`.
Taken: a statutory rule that is exempted from the operation of the Rules Publication Act 1953 is published (paragraph (a)), because paragraph (a) names exempted instruments and paragraph (b) names statutory rules without exception.
Other reading: notified (paragraph (b)), the instrument being a statutory rule.

**F79. s 47(3)(a) and (b).** Rule: `s 47(3)(a) and (b): the step to be taken in the Gazette for the regulations`.
Taken: statutory rules exempted from the operation of the Rules Publication Act 1953 are published (paragraph (a)), for the reason given at s 38A(2)(a) and (b).
Other reading: notified (paragraph (b)).

**F80. s 38(1), (2) and (3).** Rule: `s 38: the proceedings are taken`.
Taken: an offence that s 38(2) makes punishable on indictment and that a provision of the Act also expressly directs to be dealt with summarily gets NOTHING, the Act not saying which subsection prevails.
Other reading: summarily (as the more specific), or by indictment (as the heavier).

**F81. s 44.** Rule: `s 44: a matter is before 12th April 1927`.
Taken: the day 12th April 1927 itself is neither before nor after: NOTHING; "before or since" gives the day no side.
Other reading: the day itself counted as "since" (JUST FALSE).

**F82. s 43(1), Northern and Southern Divisions.** Rule: `s 43(1): the Division of the State in which the place lies`.
Taken: the forty-second parallel is taken as 42 degrees south, the State lying wholly in the southern hemisphere; a place exactly on the parallel is in neither Division, because each definition says "to the north of" or "to the south of", and answers NOTHING.
Other reading: a place on the parallel in the Northern Division, or in the Southern; or the parallel taken as 42 degrees north, which is not the State.

**F83.
Schedule 1 clause 5.** Rule: `Schedule 1 clause 5: the power conferred by section 11 as substituted is exercisable`, `Schedule 1 clause 5 as printed: limbs (a) and (b) both hold`.
Taken: the printed "and" between limbs (a) and (b) is read as "or"; a second function states the "and" as printed.
Other reading: "and" as printed.

**F84. s 23B(2).** Rule: `s 23B(2): the act of the person ousted is deemed to be as valid for all purposes as if the person had been lawfully appointed`.
Taken: the rule applies when a judgment of ouster is given, taken as a plain input, and to acts done before the day of the judgment; the text does not say what "the information" is.
Other reading: no further reading of "the information" is taken.

**F85. s 38(3).** Rule: `s 38: the penalty or forfeiture may be enforced and recovered as provided by`.
Taken: "that Act" at the end of subsection (3) is read as the Justices Act 1959, the Act named earlier in the same subsection.
Other reading: the Act in which the offence provision is contained.

**F86. s 21(3)(b)(ii).** Rule: `s 21(3)(b): the last day on which the holder may continue to exercise the powers after a fixed term`.
Taken: the date "not later than 6 months after the expiration of that term" is read as the latest date allowed, the day of the same number 6 calendar months after the day the term expired (s 46), and the period ends on the earlier of that day and the day another person is appointed, both counted in; the text does not say who picks the date.
Other reading: a date picked by someone, which the rule would take as an input.

**F87. s 29(3)(b).** Rule: `s 29(3)(b): the day on or before which an act is in due time, a time reckoned backwards ending on`.
Taken: the act is in due time if done on the next day before that is not an excluded day, or on any earlier day; the rule returns that day as the latest day for the act.
Other reading: only on that one day, which the words "unless it is done on the next day before" can be read to say.

**F88. s 13(1)(b), (c) and (d).** Rule: `s 13(1): an Act of the kind may be cited in the way`.
Taken: in (b) and (c) the words "together with a reference to the United Kingdom" and "together with a reference to the Commonwealth" attach to the second way of citing (year and chapter, or year and number) only; in (d) "together with a reference to that State or Territory" attaches to both ways.
Other reading: in (b) and (c), attaching to the short title as well.

**F89. s 18A.** Rule: `s 18A: the temporary enactment is treated as continued in operation on the day`.
Taken: the day of the expiration is itself a day of the continuation ("on and from the date of the expiration"), though the expiring enactment is also in operation to the last moment of that day (s 14(2)).
Other reading: the continuation from the day after.

**F90. s 24A(1).** Rule: `s 24A(1): the word or expression is taken to include the gender`.
Taken: a word that indicates at least one gender includes each of the three values the nouns module carries, the text naming no list of genders.
Other reading: another list of genders.

**F91. s 30A(b).** Rule: `s 30A(b): the infringement notice is taken to have been served on the intended recipient`.
Taken: paragraph (b) stands apart from the consent in paragraph (a): a notice sent electronically to an address or number provided for that purpose is taken to be served whether or not the recipient consented.
Other reading: paragraph (b) applying only where paragraph (a) does.

**F92. s 31(1).** Rule: `s 31(1): a notice comprising the essential features of the matter is to be published in`.
Taken: where the context indicates no place, the rule answers NOTHING; the text does not say what then.
Other reading: the Gazette, or a newspaper, as a default.

**F93. s 31(3).** Rule: `s 31(3): the number of publications that is sufficient`.
Taken: where no number is prescribed, one publication in each way prescribed, or one if no way is prescribed; where a number is prescribed the rule answers NOTHING, the subsection speaking only of "no number"; the text does not define a "way".
Other reading: a "way" read as each publication.

**F94. s 11(1), (3) and (4).** Rule: `s 11(1): the power may be exercised although the provision conferring it has not commenced`.
Taken: "subject to subsections (3) and (4)" is read as (3) fixing the day an instrument made under the power takes effect and (4) limiting the person appointed, or the body established, to the purposes of (1) and (2); (3) is not read as a limit on who may exercise the power.
Other reading: both subsections as limits on the exercise of the power.

**F95. s 47(7), the House and the count.** Rule: `s 47(7): the new regulation may not take effect on the day`.
Taken: "such House" is the House that disallowed the regulation; the 30 sitting days are the sitting days of that House after the day the regulation is laid, asked as a list.
Other reading: the sitting days of either House, or counting from the day of the laying.

**F96.
Every rule that returns a day, a name or a value.** Rule: none of them in particular (the convention is applied at each site).
Taken: a rule that returns a day, a name, a number or a text has no "the text says no" value, so it returns NOTHING when its text does not apply, and JUST FALSE is kept for a rule that returns a yes-or-no answer.
Other reading: a day or name of the text's own for the case, which no rule of the Act supplies.

## Worked-cases answer table

Each case below is asserted in `tas-cases-seat.l4` (and, for the underlying counting rules, in `tas-tests-time.l4`).
The expected value of each was worked out by hand from the cited section, with a calendar for the weekdays, before the module was run.

| Case | Answer | Text |
| --- | --- | --- |
| three years from 2025-07-16 | the text does not say: the Act does not define "year" | s 29(1) |
| 36 calendar months from 2025-07-16 (a separate question: the same span counted in months) | 17 July 2028: the 36 calendar months end on 16 July 2028, a Sunday, so the act is in due time on Monday 17 July 2028 | s 29(1), (3)(a), s 46 |
| five years from 2025-01-15 | the text does not say: the Act does not define "year" | s 29(1) |
| 60 calendar months from 2025-01-15 (a separate question) | 15 January 2030, a Tuesday | s 29(1), s 46 |
| five years from 2025-09-01 | the text does not say: the Act does not define "year" | s 29(1) |
| 60 calendar months from 2025-09-01 (a separate question) | 2 September 2030: the 60 calendar months end on 1 September 2030, a Sunday, so Monday 2 September 2030 | s 29(1), (3)(a), s 46 |
| thirty days from 2026-01-01 | 31 January 2026, a Saturday; Saturday is not an excluded day, so the day stands | s 29(1), (3) |
| two months from 2025-12-31 | the text does not say: February 2026 has no 31st day | s 29(1), s 46 |
| one month from 2024-01-31 | the text does not say: February 2024 has no 31st day | s 29(1), s 46 |
| one year from 2024-02-29 | the text does not say: the Act does not define "year" | s 29(1) |

## What the Act turns out to say

1. A period of days "dated or reckoned from a given day, act, or event" does not count that day (s 29(1)): 30 days from 1 January 2026 end on 31 January 2026 (`tas-cases-seat.l4`, `tas-tests-time.l4`).
   Asserted.
2. A period "expressed to be a specified number of clear days or a specified number of days at least" counts neither the given day nor the day on which the purpose is to be fulfilled (s 29(2)): 5 clear days after 1 January 2026 leave 7 January 2026 as the first day the purpose may be fulfilled, and 5 clear days before 20 January 2026 leave 14 January 2026 as the last.
   Asserted.
3. The excluded days are Sundays, the statutory holidays defined in the Statutory Holidays Act 2000, and the public holidays throughout the State or in the part of it where the act is to be done (s 29(3)).
   On the Act's own words a Saturday is not an excluded day.
   Asserted.
4. When the last day of a period reckoned forwards is an excluded day, the act is in due time on the next day that is not an excluded day (s 29(3)(a)): 23 days from 2 January 2026 end on Sunday 25 January, and the act is in due time on Monday 26 January 2026, or on Tuesday 27 January if Monday 26 January is a public holiday.
   Asserted.
5. When the time is reckoned backwards and its first day is an excluded day, the act is not in due time unless done on the next day before that is not an excluded day (s 29(3)(b)): 30 days before 31 January 2026 begin on 1 January 2026, and if 1 January is a public holiday the act is done on or before 31 December 2025.
   Asserted.
6. For a time of 1 to 6 days, excluded days are not reckoned in the computation (s 29(6)): 3 days from Friday 2 January 2026 end on Tuesday 6 January 2026, and 3 days before Monday 12 January 2026 begin on Thursday 8 January 2026.
   The Act does not say whether s 29(3)(a) or (b) applies in addition; the encoding applies s 29(6) alone (fork F73).
   Asserted.
7. Where the last day for filing or registering a document is a day the office is not open, the document may be filed or registered on the next ensuing day on which the office is open (s 29(4)).
   Asserted.
8. An act directed or allowed to be done on a particular day so fixed that s 29(3) does not apply, where that day is an excluded day, is in due time if done on the next day that is not an excluded day (s 29(5)).
   Asserted.
9. "Month" means calendar month (s 46).
   Where the later month has no day of the same number as the start day, the Act gives no answer; the Act does not define "year", "week" or "day", and gives no answer for a period of years or weeks.
   Asserted.
10. An Act assented to before the commencement of section 8 of the Acts Interpretation Amendment Act 1981 is deemed to have come into operation on the day of assent (s 9(2)); one assented to on or after that commencement comes into operation on the fourteenth day after the day of assent (s 9(3)); one reserved for the Sovereign's pleasure after that commencement comes into operation on the day after the proclamation of the Sovereign's assent is published or notified in the Gazette (s 9(4)); each unless a contrary intention appears in the Act.
    Asserted.
11. An Act, regulation or other instrument expressed to commence on a particular day commences immediately on the expiration of the last preceding day, that is at the first moment of that day (s 9(5)); an enactment expressed to expire, cease to operate, or remain in force until a specified day continues until the last moment of that day (s 14(2)), and one expressed to expire or cease to have effect on a particular day does so at the end of that day (s 16(4)).
    Asserted.
12. Where an Act repeals a former Act and substitutes provisions, the repealed provisions remain in force until the substituted provisions come into operation (s 15(1)); the repealed provisions are in force on 30 June 2026 and not on 1 July 2026 when the substituted provisions come into operation on 1 July 2026.
    Asserted.
13. Unless the contrary is expressly provided, a repeal or an expiry does not affect an investigation, legal proceeding or remedy in respect of a right, privilege, obligation, liability, penalty, forfeiture or punishment, and the proceeding may be instituted, continued or enforced as if the repealing Act had not been passed or the enactment had not expired (s 16(1), (2)).
    Asserted.
14. No person is liable to any punishment, penalty or forfeiture for anything done or omitted, contrary to a provision of a temporary enactment, between the date of its expiration and the date of the assent to the Bill continuing it (s 18A); both dates are counted in.
    Asserted.
15. A notice or document to be sent by post is served by properly addressing and posting it as a letter and paying the postage, and, unless the contrary is proved, is taken to be served when the letter would be delivered in the ordinary course of post (s 30(1)); the same holds for registered post, duly registered or sent by the certified mail service unless the Act shows a contrary intention (s 30(2)).
    Asserted.
16. Where an Act authorizes, requires or permits a notice or document to be served without directing a manner, it may be served on a natural person by giving it to the person or by leaving it at, or posting it to, the address last known to the server, and on any other person by leaving it at, or posting it to, the principal or registered office or principal place of business (s 29AB(1)).
    Asserted.
17. An infringement notice may be served electronically if the intended recipient consents, and is taken to have been served if sent electronically to an address or number provided for that purpose (s 30A).
    Asserted.
18. A proclamation, order-in-council or prescribed instrument that does not fix a commencement day takes effect on a day it specifies, or can be worked out from a period reckoned from publication or notification in the Gazette, and otherwise on the day of publication or notification (s 38A(2)(d)); regulations take effect in the same way (s 47(3)(d)).
    Asserted.
19. Regulations are to be published, or their making notified, in the Gazette within 21 days after the day they are made (s 47(3)(a), (b)); if that does not happen, or they are expressed to take effect before publication or notification where rights would be prejudiced or liabilities imposed, they are void (s 47(3A)).
    Regulations made on 1 July 2026 are in time if published on 22 July 2026 and not if published on 23 July 2026.
    Asserted.
20. A regulation is void and ceases to have effect, except as regards things done under it before the resolution, if either House passes a resolution to disallow it of which notice was given within the first 15 sitting days of that House after the regulation was laid before it (s 47(4)); the sitting days are asked as an input (`tas-ss47-regulations.l4`).
    Asserted.
21. The Act gives no statutory holidays, public holidays or sitting days, no commencement date for section 8 of the Acts Interpretation Amendment Act 1981 or for the Legislation Publication Act 1996, and no value for a penalty unit.
    The rules take these as inputs.

## What the stable binary does not accept

Where the skills describe a construct that the stable binary rejects, the binary governs.
These were each run on 1.6.98 and on 1.6.110 with the same result.
- A one-line `CONSIDER ... WHEN ... THEN ... WHEN ... THEN ...` is a parse error; each `WHEN` goes on its own line under the `CONSIDER`.
- A name with a hyphen in it that is not in backticks (`DECLARE tas-kind IS ONE OF aa, bb`) is a parse error; every such name is in backticks.
- An `#ASSERT` continued on a second line is a parse error; each assertion is on one line.
- `NOT (a) AND b` and `NOT (a) OR b` parse as `NOT` of the whole chain, with no error.
  `#ASSERT NOT (TRUE) AND FALSE` is satisfied, and `#ASSERT NOT (FALSE) OR TRUE` fails.
  Each `NOT` is written as `(NOT (a)) AND b`.
  A script (`NOT` followed by `AND` or `OR` on one line) checks the modules.
- `Date 31 2 2026` is not an error; it is 3 March 2026.
  The library's `add months` clamps 31 January 2024 plus one month to 29 February 2024, and `add years` clamps 29 February 2024 plus one year to 28 February 2025.
  The text provides neither, so the time module does not use them.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used.
  A case outside the encoding returns `NOTHING`, or a constructor, and is asserted.
Constructs the brief lists as unavailable, and not met in this encoding: `WAIT UNTIL` (spelled `WAITUNTIL`), and `TYPICALLY` on a record field.

## What check.sh prints

The output of `check.sh` with the writing binary 1.6.98 and the main build 1.6.110, as run at the end:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
tas-cases-seat.l4                              0        98       0        0         0 |      0        98       0        0  same
tas-interpretation-time.l4                     0         0       0        0         0 |      0         0       0        0  same
tas-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
tas-provisions.l4                              0        32       0        0         0 |      0        32       0        0  same
tas-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
tas-ss01-04-application.l4                     0        30       0        0         0 |      0        30       0        0  same
tas-ss05-07a-enactments.l4                     0        50       0        0         0 |      0        50       0        0  same
tas-ss08-10a-reading-and-commencement.l4       0        40       0        0         0 |      0        40       0        0  same
tas-ss11-13-anticipatory-powers-and-citation.l4       0        62       0        0         0 |      0        62       0        0  same
tas-ss14-18a-repeal-and-expiry.l4              0        78       0        0         0 |      0        78       0        0  same
tas-ss19-23-powers-and-appointments.l4         0        78       0        0         0 |      0        78       0        0  same
tas-ss23aa-23e-delegation-and-bodies.l4        0        94       0        0         0 |      0        94       0        0  same
tas-ss24-28-construction.l4                    0        50       0        0         0 |      0        50       0        0  same
tas-ss29a-31-units-service-and-notices.l4       0        52       0        0         0 |      0        52       0        0  same
tas-ss32-38-offences.l4                        0        67       0        0         0 |      0        67       0        0  same
tas-ss38a-40a-instruments-and-notice.l4        0        66       0        0         0 |      0        66       0        0  same
tas-ss41-45-definitions.l4                     0        88       0        0         0 |      0        88       0        0  same
tas-ss46-46c-common-phrases.l4                 0        81       0        0         0 |      0        81       0        0  same
tas-ss47-regulations.l4                        0        76       0        0         0 |      0        76       0        0  same
tas-ss48-sch1-rules-of-court-and-transitional.l4       0        70       0        0         0 |      0        70       0        0  same
tas-terms.l4                                   0       126       0        0         0 |      0       126       0        0  same
tas-tests-time.l4                              0       188       0        0         0 |      0       188       0        0  same
tas-xrefs.l4                                   0       213       0        0         0 |      0       213       0        0  same
TOTAL (23 modules)                             0      1639       0        0           |      0      1639       0        0
```

Every module has `0` errors, `0` failed and `0` refused, and its main-build column reads `same`.
`srcrefs.py check --refs` and `srcrefs.py check --strict` both report 0 problems over every `.l4` file.
`l4 run` on every file shows no `DiagnosticSeverity_Error` and no `_Warning`.
Every case file has assertions written equal to assertions satisfied; no assertion is written to fail.
`check.sh` counts error diagnostics and assertion lines and nothing else.
It does not see a different `#TRACE` outcome between builds; the encoding uses no `#TRACE`.

## Cross-references

`tas-xrefs.l4` has 209 rows: 91 internal and 118 external.
An internal row is a reference from one provision of the text to another provision of the same text.
By kind of target: 40 sections, 43 subsections, 6 paragraphs, 1 subparagraph and 1 Schedule.
Each cited identifier is in the provision index, the row's heading is the index's heading for it, and a test per row asserts both; the rows and the index come from the same script, so those tests check the script against itself.
An external row is a reference to another Act or instrument: 118 rows, naming 41 distinct instruments. 53 carry a provision (a section or similar) and 65 name the instrument only. 15 are written "the lastmentioned section" and are resolved to the section of the amending Act that the same clause named last.
External rows are not resolved here; the borrowed fact is asked as an input where a rule needs it.
A script finds the references by pattern over the text file: it matches "section", "subsection" and "paragraph" with their numbers (and "and" or "or" lists), "Schedule 1", "of the" followed by an Act, Law or Code title, and "lastmentioned section", places each reference in the deepest provision that contains its line, and resolves each internal one against the provision index.
It is not a reading of the text by a person.
A reference written in a form the patterns do not match would not be found.
No internal reference failed to resolve.
The 41 rows that cite a section or Schedule 1 (24 distinct citing and cited pairs) were read by eye against the cited headings, and none was found not to fit.
The 50 rows that cite a subsection, paragraph or subparagraph were not read that way.

## What needs doing before the encoding is worth relying on

- A lawyer qualified in Tasmania should read each rule against the authorised version of the Act and not against the plain-text conversion.
- The fork register should be read, and each reading overruled or confirmed.
- The inputs the Act does not give (the holidays, the sitting days, the commencement of section 8 of the 1981 Amendment Act, the commencement of the Legislation Publication Act 1996, the value of a penalty unit) should be supplied from the instruments that give them, and the fixtures in the tests should then be replaced by those values.
- The cross-reference rows are found by pattern, and the external ones are not resolved; a person should read the list.
- The twelve provisions the text shows only as dots should be checked against the authorised version, in case any carries text.
- Nothing here has been run against a real filing or service; the cases are worked from the text.

## Modules

Layer 1 and layer 2, in reading order: `tas-cases-seat.l4`, `tas-interpretation-time.l4`, `tas-nouns.l4`, `tas-provisions.l4`, `tas-seat.l4`, `tas-ss01-04-application.l4`, `tas-ss05-07a-enactments.l4`, `tas-ss08-10a-reading-and-commencement.l4`, `tas-ss11-13-anticipatory-powers-and-citation.l4`, `tas-ss14-18a-repeal-and-expiry.l4`, `tas-ss19-23-powers-and-appointments.l4`, `tas-ss23aa-23e-delegation-and-bodies.l4`, `tas-ss24-28-construction.l4`, `tas-ss29a-31-units-service-and-notices.l4`, `tas-ss32-38-offences.l4`, `tas-ss38a-40a-instruments-and-notice.l4`, `tas-ss41-45-definitions.l4`, `tas-ss46-46c-common-phrases.l4`, `tas-ss47-regulations.l4`, `tas-ss48-sch1-rules-of-court-and-transitional.l4`, `tas-terms.l4`, `tas-tests-time.l4`, `tas-xrefs.l4`.
