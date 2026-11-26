# Dead `LEST` clauses: dropped, or given the deadline the text states (Companies Act 1967 (Singapore, 2020 Revised Edition))

Status: decided by Claude on 2026-11-26 (assumed, not ruled); every row below is a proposal for a maintainer to confirm or reverse, and each can be restored from the commit before it.

Later the same day the 205 sites were sorted by kind of duty (section "Sorted by kind of duty"), and the 105 that are duties to do a thing once were given a time that is an input: 86 the time that Interpretation Act 1965 s 52 supplies, and 19 the time that their own section's standard ("immediately", "as soon as practicable", ...) supplies (section "What was done to the achievement sites").
On 2026-11-27, after an independent review, six sites changed class (decided by Claude, assumed, not ruled; section "What the review of 2026-11-27 changed"): s 29A(2)(a) and (b) and s 205(6) went from ACHIEVEMENT back to OTHER and are comments again, s 207(1) went from s 52 to its own standard, s 210(8)(a) went from its own standard to s 52, and s 386AF(7)(b) went from MAINTENANCE to OTHER.
The sections that follow them keep the account of the first drop as it was written, so "dropped" in them means dropped at that time; the 105 are no longer dropped.

## What was found and what was done

Running `l4 run` (unstable, a50cbd0) over every module in this folder reported `lint/lest-without-deadline` at 205 places in 67 modules: a `MUST` (or `MAY`) with neither `WITHIN` nor `BEFORE` whose `LEST` can therefore never be reached (the lint's own wording: "time alone never takes it to this LEST").
Each such `LEST` was read against the statute lines its rule cites and against the rest of its section.
A `WITHIN n` was to be added where the text states a period of whole days or weeks for that very duty; otherwise the `LEST` goes.
The result: all 205 `LEST` clauses dropped; no duty carries a period of days or weeks in the text (one, s 377(2), names 14 days that cannot run for it: see the last section).
A dropped `LEST` line is replaced by a one-line comment of the same line number, so every `file:line` that cites a later line still held at that commit, and a closing parenthesis that followed the `BECAUSE` string moves to the line above.
That held for the classification commit, the own-standard commit and the comments commit too, which change no `.l4` line count; the code commit changed the line count of 41 rule modules, the tests commit of 32 modules, and the commit of 2026-11-27 of 5, and the cites were re-pointed at the tests commit and again at that one (section "What the tests show now").
Dropping an unreachable `LEST` changes no result: the obligation still waits for its action however long it takes, as before.
The one visible difference is that a `#TRACE` which ends with the obligation still open prints it without the `LEST` it used to carry.

An independent reader read 181 of these 205 sites (all 168 whose section holds any time phrase, and 13 of the others) against the statute text itself, and a scan of the whole section of the other 24 found no number of days or weeks.
It challenged one site, s 377(2); that was not accepted, and the last section says why.

## Each dropped clause is kept in its comment

Each of the 205 comments began `-- no LEST:`, so `grep -rn -e '-- no LEST:' .` in this folder found every site without the git history.
After the s 52 pass the 100 sites that are not achievements still begin that way, and end with their class, so the same grep finds them; the 105 achievements are code again, and `grep -rn -e 'WITHIN `the period of all convenient speed, as found`' .` finds the 86 sites under s 52, and `grep -rn -e 'WITHIN `the period the standard of time allows, as found`' .` the 19 under their own section's standard.
The comment says that no deadline is modelled for the duty (`-- no LEST: no deadline is modelled for this duty; dropped clause: LEST BREACH BY … BECAUSE "…"`).
Until the review of 2026-11-27 it said instead that the section states no time and that a breach needs a standard of time from outside the section, and it named Interpretation Act 1965 s 52; for 30 of the 97 sites it then covered, the table itself says the text does give a time (another act's, "before" a later act, the party's, a meeting's, another person's window, or regulations'), so the sentence was wrong there and is gone.
It carries the dropped `LEST` clause word for word (`dropped clause: LEST BREACH BY … BECAUSE "…"`), copied from the commit before the drop and checked against it byte for byte; for the 7 clauses whose closing parenthesis moved to the line above, the 3 that stay comments carry the clause without it.
Not every site wants a deadline: a duty that must hold throughout ("keep a register", "act honestly at all times") is broken at any moment it stops holding, not when a period runs out, and L4 has no form for such a duty yet.
Sorting the 205 into duties to do a thing once, which can take a `WITHIN` whose length is found (under s 52, or under the section's own standard where it gives one), and duties that must hold throughout, which stay as they are, is done in the section "Sorted by kind of duty" (decided by Claude on 2026-11-26, assumed, not ruled).

## Sorted by kind of duty: achievement, maintenance, other

Status: decided by Claude on 2026-11-26, assumed, not ruled; every row below is a proposal for a maintainer to confirm or reverse.
The sorting was done by reading the operative verb of each rule and the statute words in its row of the section "Dropped", one site at a time; a script only applied the sorting from a table written by hand, and it chose no class.
The line column is the line in the tree at the commit that carries this table: for the 100 sites left as comments it is the line of the `-- no LEST:` comment, and for the 105 restored sites it is the line of the restored `LEST`.
The rows of the section "Dropped" keep the lines at commit 1142117325, where this work began; restoring a site adds a line or two above every later site in its module.
Each class is also written on the comment itself, so `grep -rn -e '\[class: ' .` in this folder finds the 100 sites that are not achievements, and says which class each is.

### The three classes

- **ACHIEVEMENT**: the duty is to do a thing once (lodge, send, declare, convene, furnish, issue, notify, pay, appoint, sign, publish).
  It can be late, so a deadline suits it; where the section states none, the standard of time comes from the Interpretation Act 1965 s 52, "all convenient speed" (the sub-class "ACHIEVEMENT, s 52"); where the section gives its own standard ("immediately"), s 52 does not apply and the sub-class is "ACHIEVEMENT, text's own standard".
- **MAINTENANCE**: the duty is to hold throughout (keep a register, maintain a system, "at all times act honestly", ensure the register contains the particulars).
  It is broken at any moment it stops holding, not when a period runs out, so a deadline is the wrong model; and an untimed `MUST` is wrong too, because one compliant act would discharge it for ever.
  L4 has no form for such a duty yet: a design is proposed, not landed, and a search of `jl4-core/src/L4/Lexer.hs` on the unstable tip on 2026-11-26 found none of `ALWAYS`, `THROUGHOUT`, `MAINTAIN`, `INVARIANT` or `WHILE`; these sites stay as they are.
- **OTHER**: neither of the above, or the sorting could not tell.
  Where a site could be either an achievement or something else, the tie goes to OTHER with the reason written on the row.

### Counts

| class | sites |
| ----- | ----- |
| ACHIEVEMENT, s 52 | 86 |
| ACHIEVEMENT, text's own standard | 19 |
| ACHIEVEMENT, both | 105 |
| MAINTENANCE | 35 |
| OTHER | 65 |
| all | 205 |

ACHIEVEMENT, s 52: 49 a thing done once, 37 a thing done once on a trigger the text names (a request, an application, a receipt).
ACHIEVEMENT, text's own standard: 19 a thing done once for which the section gives its own non-numeric standard of time.
MAINTENANCE: 18 a state that must hold, 14 a register, index or record to be kept, 3 others (a holding in trust, a duty attached to every copy issued, a standing rule of treatment).
OTHER: 15 timed by another act or filing, 9 weighed in the course of another act, 8 a requirement on a document's content, 8 a step in an application, 4 bound only by "before" a later act, 4 tied to a meeting, 3 tied to another person's window, 3 a bar on a power, 4 a time left to regulations, 2 a liability, 2 a time left to the party, 2 an effort standard, 1 a direction on recouping a sum.

### Calls the sorting rests on (each decided by Claude on 2026-11-26, assumed, not ruled)

1. **The Registrar, the Minister and the Official Receiver are treated like any other bearer of a duty.**
   Where their duty is an act (issue, publish, send, appoint, register, strike off, report), it is an ACHIEVEMENT, since s 52 speaks of "anything" to be done.
2. **The 19 sites whose section gives its own standard of time ("immediately", "as soon as practicable", "without delay", "within a reasonable time", "thereupon", "in sufficient time") are ACHIEVEMENT, text's own standard, and s 52 is not their source.**
   s 52 does not reach them: it applies only "where no time is prescribed or allowed within which anything is to be done" (`subjects/sg/interpretation-act/registers/source-bundle/IA1965.txt:2188-2190`), and each of these sections prescribes a standard of time in its own words, so the first limb of s 52 is not met.
   The number of days is as missing as for the others, so they take an input too, named for what it is, `the period the standard of time allows, as found`; the comment beside the `WITHIN` gives the section's own standard (its word and its section number) and says the period is an input, as found, and it does not mention s 52.
   I chose a second name for those 19 and left the other 86 on the s 52 name, which is the least churn: no call site changes, because the input is positional.
   Reclassing them is a one-pass change.
   They are (lines at commit 1142117325): `sgb1-s149b-appointment.l4:367`, `sgb1-s156-interests.l4:471`, `sgc2-s205-appointment.l4:221`, `sgc2-s205-appointment.l4:390`, `sgc2-s205aa-resignation.l4:195`, `sgc2-s206-208a-duties.l4:149`, `sgc2-s206-208a-duties.l4:158`, `sgc2-s206-208a-duties.l4:167`, `sgc2-s206-208a-duties.l4:264`, `sgc2-s206-208a-duties.l4:303`, `sgc2-s206-208a-duties.l4:672`, `sgc2-s206-208a-duties.l4:746`, `sgd-acquisition.l4:1341`, `sgd-amalgamation.l4:1371`, `sgl-circulation.l4:415`, `sgl-minutes.l4:401`, `sgl-minutes.l4:414`, `sgl-written.l4:613`, `sgm-part5-div4.l4:1248`.
   `s 207(1)` is among them because `s 207(1A)` says of "a report by an auditor of a company under subsection (1)" that it "must be furnished by the auditor to the directors of the company in sufficient time" (`subjects/sg/companies-act-1967/registers/source-bundle/CoA1967.txt:19791-19794`).
   The rule for (1) has the one input, as the rule for (1A) has; neither has two, and the two rules are separate duties (to report to the members, to furnish the report to the directors) that use the same input name.
   `s 210(8)(a)` is not among them: "as soon as possible" governs the accountants' or solicitors' forwarding of their report ("forward their report or reports to the directors as soon as possible"), and I read it as not governing the directors' instruction (assumed, not ruled), so the instruction is under s 52; on the other reading it joins the 19 in one pass.
   **Why "thereupon" (s 215(4)) is among the 19 and "Upon ..." is not.**
   "The transferor company must thereupon register the transferee" puts the word on the act itself, saying how soon the register follows the transferee's step, so it is a standard of time in the section's own words.
   "Upon the application of the company ... the Registrar must issue" opens the clause with the event that arms the duty and says nothing of how soon the act follows it; the event is what the `WITHIN` counts from, and s 52 supplies the speed.
   14 of the ACHIEVEMENT sites under s 52 have a row below that quotes "upon" (counted by searching the rows of the section "Dropped" for the word).
   13 of them use it as that opening trigger: s 201B(7), s 215F(1), s 215F(4), s 359(3), s 359(4), s 17(9), s 19(3), s 19(7), s 12B(1), s 134(3), s 344A(3), s 344B(2)(a) and s 344C(3)(a); the 14th, s 233(1), says "upon which the inspector's opinion is based", a relative clause.
   This is a reading (assumed, not ruled): if "upon" is read as a word of promptness too, those 13 move to ACHIEVEMENT, text's own standard, in one pass, and s 52 stops being their source.
3. **A duty that is a bar on a power, not an act that falls due, is OTHER.**
   "The Registrar must refuse to register" (`sge-p10a-360.l4` s 360(1) and (2), `sgh-incorporation.l4` s 20(2)) is breached by registering, and no day arrives on which it is late.
4. **A duty whose time the Act hands to regulations is OTHER.**
   `sgn-register.l4:414`, `sgn-register.l4:502`, `sgn-register.l4:515` and `sgn-register.l4:797` say "within the prescribed time" or "within the prescribed period", so s 52 is not the standard (for :414, the update of the register, it is s 386AF(8) that says "must enter the particulars in its register and update the register within the prescribed time"); the existing input `the prescribed period, in days` (as `sgn-register.l4`'s s 386AFA(4) rule uses) is the candidate, and it is not added here.
   s 386AF(7)(b) is therefore not aligned with s 196A(5): the section of s 196A(5) gives no time anywhere, and (7)(b)'s section does.
5. **A step a person takes to obtain what they apply for is OTHER**: submitting the constitution, paying the fee, making the declaration, reserving a name, and a charitable company's altering its constitution and filing the form to omit "Limited" or "Berhad" from its name (s 29A(2)(a) and (b), the same shape as s 19(1), s 22(2) and s 357(1)).
   Nothing arms a clock, and failing to take the step forfeits the application and is not a default.
6. **A duty tied to another act's own time is OTHER**: lodged "with the return", attached "when lodging a return", signed "by the chairperson of the next succeeding meeting", noticed "at the same time as notice of the meeting" (s 183(3C)).
   Giving it an independent period would contradict the anchor the text states.
7. **A requirement on what a document contains or looks like is OTHER**: it is met when the document is made.
8. **Where a rule holds a `MUST` inside the `HENCE` of another, each is its own site and has its own class.**
   `sgl-calling.l4` s 176(4) pays the requisitionists (ACHIEVEMENT) and then retains the sum out of what is due to the directors in default (OTHER, a direction on recouping a sum); only the first takes a period.
9. **When the sorting was torn between ACHIEVEMENT and OTHER, it chose OTHER.**
   Examples: s 201(9)(b), s 215(1B), s 135(1), s 37(4), s 183(1)(a) and (b), s 188(1)(b), s 184F(1), s 156(11), s 215F(1)(b), s 205(6) ("as so requested" imports the auditor's request, in (5)(b), that the copy be sent "prior to the meeting", as the module's own comment quotes).

### The table

| module | line | section | class | the operative verb, and why it is in this class |
| ------ | ---- | ------- | ----- | ------------------------------------------------ |
| `sg-solvency.l4` | 234 | s 7A(3) | OTHER | "take into account all liabilities of the company (including contingent liabilities)": to be weighed in the course of another act (the director's opinion for the solvency statement), with no time of its own |
| `sg-solvency.l4` | 258 | s 7A(4)(a) | OTHER | "have regard to all other circumstances that the directors know or ought to know affect the v...": to be weighed in the course of another act (the director's opinion for the solvency statement), with no time of its own |
| `sg-solvency.l4` | 259 | s 7A(4)(a) | OTHER | "have regard to the most recent financial statements of the company that comply with section...": to be weighed in the course of another act (the director's opinion for the solvency statement), with no time of its own |
| `sga1-issue.l4` | 595 | s 63B(1) | OTHER | "lodge with the return of allotment the contract, or a copy of it certified as prescribed": its time is that of another act or filing: "with the return of allotment"; the return's own deadline governs |
| `sga1-issue.l4` | 655 | s 63B(3) | OTHER | "lodge with the return of allotment the document specified in subsection (4)": its time is that of another act or filing: "at the same time and together with the return of allotment", s 63B(5) |
| `sga1-rights.l4` | 409 | s 66(4) | ACHIEVEMENT, s 52 | "cancel a share warrant issued before 29 December 1967 that is unaccounted for by the expiry...": a thing done once, on its trigger (the expiry of the 2-year period) |
| `sga3-76f-76g.l4` | 287 | s 76G(1) | ACHIEVEMENT, s 52 | "reduce the amount of its share capital or its profits, or both, by the total amount of the p...": a thing done once |
| `sgb1-s149b-appointment.l4` | 369 | s 152(2) | ACHIEVEMENT, text's own standard | "send a copy of the notice of the intended resolution to the director concerned": a thing done once; the text's own standard is "immediately" |
| `sgb1-s156-interests.l4` | 473 | s 156(1) | ACHIEVEMENT, text's own standard | "declare the nature of the interest at a meeting of the directors, or send a written notice t...": a thing done once; the text's own standard is "as soon as is practicable" |
| `sgb1-s156-interests.l4` | 506 | s 156(11) | OTHER | "record the declaration in the minutes": its time is that of another act or filing: the minutes of the meeting, which s 188(1)(a) times ("within one month") |
| `sgb1-s156-interests.l4` | 520 | s 156(12) | OTHER | "permit the chief executive officer to attend the meeting of the board of directors": tied to a meeting (attendance at a board meeting "where such attendance is necessary"), whose own time governs |
| `sgb1-s157-duties.l4` | 437 | s 157(1) | MAINTENANCE | "act honestly and use reasonable diligence in the discharge of the duties of the office of di...": a state that must hold throughout ("at all times act honestly") |
| `sgc1-s199.l4` | 56 | s 199(1) | MAINTENANCE | "cause accounting and other records to be kept": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgc1-s199.l4` | 138 | s 199(2A) | MAINTENANCE | "devise and maintain a system of internal accounting controls": a state that must hold throughout ("devise and maintain" a system) |
| `sgc1-s199.l4` | 171 | s 199(3) | MAINTENANCE | "keep the records open to inspection by the directors": a state that must hold throughout ("at all times be open to inspection") |
| `sgc1-s201-statement.l4` | 213 | s 201(23) | OTHER | "attach a copy of the report prepared under section 201(5) as in force before 1 July 2015 to...": its time is that of another act or filing: "when lodging a return with the Registrar under section 197" |
| `sgc1-s201.l4` | 281 | s 201(9)(b) | OTHER | "cause the auditor's report to be attached to the financial statements": a requirement on the content or form of a document (the auditor's report attached to the financial statements), met when the document is made |
| `sgc1-s201.l4` | 343 | s 201(11) | OTHER | "state the name of the ultimate parent corporation in the financial statements": a requirement on the content or form of a document (a statement in the financial statements laid at the annual general meeting), met when the document is made |
| `sgc1-s201a.l4` | 214 | s 201A(7) | OTHER | "attach a copy of the accounts or consolidated accounts to the return": its time is that of another act or filing: "when lodging a return with the Registrar under section 197" |
| `sgc1-s201b.l4` | 52 | s 201B(1) | MAINTENANCE | "have an audit committee": a state that must hold throughout ("must have an audit committee") |
| `sgc1-s201b.l4` | 203 | s 201B(6) | OTHER | "appear before the audit committee when required to do so": tied to a window another person holds (the committee's requirement fixes when the auditor appears) |
| `sgc1-s201b.l4` | 227 | s 201B(7) | ACHIEVEMENT, s 52 | "convene a meeting of the audit committee on the auditor's request": a thing done once, on its trigger (the auditor's request) |
| `sgc1-s201b.l4` | 279 | s 201B(9) | OTHER | "describe in the directors' statement the nature and extent of the functions performed by the...": a requirement on the content or form of a document (a description in the directors' statement), met when the document is made |
| `sgc1-s203.l4` | 149 | s 203(3) | ACHIEVEMENT, s 52 | "furnish the member or debenture holder without charge with a copy of the last financial stat...": a thing done once, on its trigger (a request) |
| `sgc1-s203a.l4` | 90 | s 203A(4) | ACHIEVEMENT, s 52 | "send copies of the documents referred to in section 203(1) to the member who wishes to recei...": a thing done once, on its trigger (the member wishing to receive them) |
| `sgc1-s203a.l4` | 153 | s 203A(6A) | OTHER | "ensure that the summary financial statements comply with the requirements referred to in sub...": a requirement on the content or form of a document (the summary financial statements must comply), met when the document is made |
| `sgc2-s205-appointment.l4` | 124 | s 205(2) | OTHER | "appoint an accounting entity or accounting entities as the auditor or auditors at the annual...": tied to a meeting (appointment "at each annual general meeting"), whose own time governs |
| `sgc2-s205-appointment.l4` | 223 | s 205(5)(a) | ACHIEVEMENT, text's own standard | "send a copy of the notice of the resolution to remove the auditor to the auditor concerned a...": a thing done once; the text's own standard is "immediately" |
| `sgc2-s205-appointment.l4` | 287 | s 205(6) | OTHER | "send a copy of the representations to every member to whom notice of the meeting is sent": tied to a meeting ("as so requested" imports the auditor's request, in s 205(5)(b), that the copy be sent "prior to the meeting"), whose own time governs |
| `sgc2-s205-appointment.l4` | 394 | s 205(8) | ACHIEVEMENT, text's own standard | "give written notice of the removal of the auditor to the Registrar": a thing done once; the text's own standard is "immediately after the removal" |
| `sgc2-s205a-exemption.l4` | 303 | s 205B(4)(d) | OTHER | "accompany the annual return with a statement by the directors": its time is that of another act or filing: the annual return to be lodged |
| `sgc2-s205a-exemption.l4` | 545 | s 205C(7) | OTHER | "attach a copy of the accounts or consolidated accounts to the return lodged under section 197": its time is that of another act or filing: "when lodging a return with the Registrar under section 197" |
| `sgc2-s205aa-resignation.l4` | 197 | s 205AB(2) | ACHIEVEMENT, text's own standard | "notify the auditor and the company whether the Registrar consents to the resignation": a thing done once; the text's own standard is "as soon as practicable" |
| `sgc2-s205aa-resignation.l4` | 383 | s 205AC(3)(a) | ACHIEVEMENT, s 52 | "give notice of the application to the auditor of the company": a thing done once |
| `sgc2-s205aa-resignation.l4` | 394 | s 205AC(3)(b) | ACHIEVEMENT, s 52 | "give notice of the application to the company and the auditor of the company": a thing done once |
| `sgc2-s206-208a-duties.l4` | 151 | s 206(1)(c) | ACHIEVEMENT, text's own standard | "prepare a statement showing particulars of all emoluments paid to the auditor or other perso...": a thing done once; the text's own standard is "immediately" |
| `sgc2-s206-208a-duties.l4` | 162 | s 206(1)(d) | ACHIEVEMENT, text's own standard | "forward a copy of the statement to all persons entitled to receive notice of general meeting...": a thing done once; the text's own standard is "immediately" |
| `sgc2-s206-208a-duties.l4` | 173 | s 206(1)(e) | ACHIEVEMENT, text's own standard | "lay the statement before the company in general meeting": a thing done once; the text's own standard is "immediately" |
| `sgc2-s206-208a-duties.l4` | 215 | s 206(1A) | ACHIEVEMENT, s 52 | "send the outcome of the review to all persons entitled to receive notice of general meetings...": a thing done once |
| `sgc2-s206-208a-duties.l4` | 216 | s 206(1A) | ACHIEVEMENT, s 52 | "undertake a review of the fees, expenses and emoluments of the auditor to determine whether...": a thing done once |
| `sgc2-s206-208a-duties.l4` | 275 | s 207(1) | ACHIEVEMENT, text's own standard | "report to the members": a thing done once; the text's own standard is "in sufficient time", which s 207(1A) gives for "a report by an auditor of a company under subsection (1)" |
| `sgc2-s206-208a-duties.l4` | 316 | s 207(1A) | ACHIEVEMENT, text's own standard | "furnish the report to the directors in sufficient time": a thing done once; the text's own standard is "in sufficient time" |
| `sgc2-s206-208a-duties.l4` | 687 | s 207(9) | ACHIEVEMENT, text's own standard | "report the matter in writing to the Registrar": a thing done once; the text's own standard is "immediately" |
| `sgc2-s206-208a-duties.l4` | 763 | s 207(9A) | ACHIEVEMENT, text's own standard | "report the matter to the Minister": a thing done once; the text's own standard is "immediately" |
| `sgd-acquisition.l4` | 1263 | s 215(1B) | OTHER | "state which of the alternative terms is to apply where the dissenting shareholder fails to e...": a requirement on the content or form of a document (a statement in the notice of which terms apply), met when the document is made |
| `sgd-acquisition.l4` | 1282 | s 215(2) | ACHIEVEMENT, s 52 | "supply the dissenting shareholder with a written statement of the names and addresses of all...": a thing done once, on its trigger (the shareholder's written demand) |
| `sgd-acquisition.l4` | 1329 | s 215(4)(a) | ACHIEVEMENT, s 52 | "transmit a copy of the notice to the transferor company with an instrument of transfer": a thing done once |
| `sgd-acquisition.l4` | 1335 | s 215(4)(b) | ACHIEVEMENT, s 52 | "pay, allot or transfer to the transferor company the amount or other consideration": a thing done once |
| `sgd-acquisition.l4` | 1348 | s 215(4) | ACHIEVEMENT, text's own standard | "register the transferee as the holder of the shares": a thing done once; the text's own standard is "thereupon" |
| `sgd-acquisition.l4` | 1365 | s 215(5) | ACHIEVEMENT, s 52 | "pay the sums received into a separate bank account": a thing done once |
| `sgd-acquisition.l4` | 1374 | s 215(5) | MAINTENANCE | "hold the sums and other consideration in trust for the persons entitled": a holding that continues ("must be held ... in trust") |
| `sgd-acquisition.l4` | 1414 | s 215(7)(a) | ACHIEVEMENT, s 52 | "deal with the moneys received under subsection (6) as if they were paid under section 197 of...": a thing done once |
| `sgd-acquisition.l4` | 1424 | s 215(7)(b) | ACHIEVEMENT, s 52 | "sell or dispose of the other consideration and deal with the proceeds as if they were moneys...": a thing done once |
| `sgd-acquisition.l4` | 1438 | s 215AA(6) | OTHER | "make the notice by all of the joint transferees, signed for each company by a director of th...": a requirement on the content or form of a document (the notice must be made by all the joint transferees and signed by a director), met when the document is made |
| `sgd-amalgamation-solvency.l4` | 383 | s 215I(3) | OTHER | "take into account all liabilities of the amalgamating company (including contingent liabilit...": to be weighed in the course of another act (the directors' opinion for the solvency statement), with no time of its own |
| `sgd-amalgamation-solvency.l4` | 407 | s 215I(4)(a) | OTHER | "have regard to the most recent financial statements and all other circumstances": to be weighed in the course of another act (the directors' opinion for the solvency statement), with no time of its own |
| `sgd-amalgamation-solvency.l4` | 419 | s 215J(2) | OTHER | "take into account all liabilities of the amalgamated company (including contingent liabilities)": to be weighed in the course of another act (the directors' opinion for the solvency statement), with no time of its own |
| `sgd-amalgamation-solvency.l4` | 444 | s 215J(3)(a) | OTHER | "have regard to the most recent financial statements and all other circumstances": to be weighed in the course of another act (the directors' opinion for the solvency statement), with no time of its own |
| `sgd-amalgamation.l4` | 1202 | s 215C(3) | ACHIEVEMENT, s 52 | "sign a declaration stating that, in the director's opinion, the conditions are satisfied, an...": a thing done once |
| `sgd-amalgamation.l4` | 1338 | s 215D(6) | ACHIEVEMENT, s 52 | "sign a declaration stating that, in the director's opinion, the conditions specified in sect...": a thing done once |
| `sgd-amalgamation.l4` | 1360 | s 215F(1) | OTHER | "issue a notice of amalgamation together with the notice of incorporation under section 19(4)": its time is that of another act or filing: "together with the notice of incorporation under section 19(4)" |
| `sgd-amalgamation.l4` | 1365 | s 215F(1) | ACHIEVEMENT, s 52 | "issue a notice of amalgamation": a thing done once, on its trigger (receipt of the documents and fees) |
| `sgd-amalgamation.l4` | 1379 | s 215F(3) | ACHIEVEMENT, text's own standard | "remove the amalgamating companies, other than the amalgamated company, from the register": a thing done once; the text's own standard is "as soon as practicable" |
| `sgd-amalgamation.l4` | 1393 | s 215F(4) | ACHIEVEMENT, s 52 | "issue to the amalgamated company a certificate of confirmation of amalgamation": a thing done once, on its trigger (the application and the fee) |
| `sgd-amalgamation.l4` | 1436 | s 215K(2)(a) | ACHIEVEMENT, s 52 | "deal with the moneys received under subsection (1) as if they were paid under section 197 of...": a thing done once |
| `sgd-amalgamation.l4` | 1452 | s 215K(2)(b) | ACHIEVEMENT, s 52 | "sell or dispose of the other consideration and deal with the proceeds as if they were moneys...": a thing done once |
| `sgd-compromise.l4` | 1017 | s 210(6) | MAINTENANCE | "annex a copy of the order to a copy of the constitution": a duty attached to every item of a continuing flow ("every copy of the constitution ... issued after the order"), so no single act discharges it |
| `sgd-compromise.l4` | 1034 | s 210(8)(a) | ACHIEVEMENT, s 52 | "instruct the accountants or solicitors named in the resolution to report on the proposals": a thing done once; "as soon as possible" governs the accountants' forwarding of their report, and is read as not governing the directors' instruction (assumed, not ruled) |
| `sgd-compromise.l4` | 1093 | s 210(10B)(a) | ACHIEVEMENT, s 52 | "deal with the moneys received under subsection (10A) as if they were paid under section 197...": a thing done once |
| `sgd-compromise.l4` | 1103 | s 210(10B)(b) | ACHIEVEMENT, s 52 | "sell or dispose of the other consideration and deal with the proceeds as if they were moneys...": a thing done once |
| `sgd-compromise.l4` | 1121 | s 211(3) | ACHIEVEMENT, s 52 | "furnish the person with a copy of the statement free of charge": a thing done once, on its trigger (an application) |
| `sge-p10a-357-358.l4` | 51 | s 357(1) | OTHER | "apply to reserve the name of the intended company": a step taken to obtain what is applied for (a foreign corporate entity that "intends to be registered" applies to reserve the name); no event arms a clock |
| `sge-p10a-359.l4` | 79 | s 359(3) | ACHIEVEMENT, s 52 | "issue a notice of transfer of registration": a thing done once, on its trigger (registration) |
| `sge-p10a-359.l4` | 166 | s 359(4) | ACHIEVEMENT, s 52 | "issue a certificate of confirmation of registration": a thing done once, on its trigger (the application) |
| `sge-p10a-360.l4` | 49 | s 360(1) | OTHER | "refuse to register the foreign corporate entity": a bar on a power (the Registrar "must refuse to register" if not satisfied), breached by registering, not an act that falls due |
| `sge-p10a-360.l4` | 114 | s 360(2) | OTHER | "refuse to register the foreign corporate entity": a bar on a power (the Registrar "must refuse to register" if satisfied of a ground), breached by registering, not an act that falls due |
| `sge-p10a-362.l4` | 118 | s 362(2) | OTHER | "consider the company's written representations": tied to a window another person holds (the company's window for representations under the notice) |
| `sge-p10a-362.l4` | 119 | s 362(2) | OTHER | "and (b) give the company written notice of the Registrar's intention to revoke the registrat...": the text's only time is "before" a later act: "before making an order of revocation" |
| `sge-p10a-362.l4` | 221 | s 362(4) | ACHIEVEMENT, s 52 | "serve a copy of the notice of the order of revocation on the company": a thing done once |
| `sge-p10a-362.l4` | 222 | s 362(4) | ACHIEVEMENT, s 52 | "cause a notice of the order of revocation to be published in the Gazette": a thing done once |
| `sgg-cessation.l4` | 176 | s 377(2) | ACHIEVEMENT, s 52 | "lodge with the Registrar notice of the appointment of a liquidator": a thing done once, on its trigger (the liquidator being appointed) |
| `sgg-identity.l4` | 47 | s 375(1)(b) | MAINTENANCE | "cause its name and the place where it is formed or incorporated to be stated in legible roma...": a state that must hold throughout (the name and place stated "in legible romanised letters" wherever the section requires) |
| `sgg-identity.l4` | 97 | s 375(1)(c) | MAINTENANCE | "cause notice that the liability of its members is limited to be given": a state that must hold throughout (notice of limited liability to be given wherever the section requires) |
| `sgg-identity.l4` | 141 | s 375(3) | MAINTENANCE | "cause its unique entity number to appear in a legible form": a state that must hold throughout (the unique entity number "on all business letters, statements of account, invoices") |
| `sgg-lodging.l4` | 516 | s 370(1) | MAINTENANCE | "keep a registered office in Singapore open and accessible to the public": a state that must hold throughout ("must be open and accessible to the public" each business day) |
| `sgg-lodging.l4` | 594 | s 370(4) | ACHIEVEMENT, s 52 | "lodge the notice and the consent statement for the new authorised representative": a thing done once, on its trigger (the appointment of a new authorised representative) |
| `sgg-lodging.l4` | 660 | s 370(6)(a) | ACHIEVEMENT, s 52 | "appoint another authorised representative": a thing done once, on its trigger (the sole authorised representative ceasing) |
| `sgg-registers.l4` | 235 | s 380(2)(a) | MAINTENANCE | "keep an index in convenient form of the names of the members": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgg-registers.l4` | 262 | s 380(2)(c) | MAINTENANCE | "keep the index at the same place as the register of members": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgg-returns.l4` | 783 | s 374 | OTHER | "lodge a return containing the prescribed information about the keeping of the registers": its time is that of another act or filing: "at the time when making a lodgment" of the financial statements |
| `sgh-address.l4` | 311 | s 12E(1) | ACHIEVEMENT, s 52 | "cause the residential address to be excluded from public access": a thing done once, on its trigger (the individual's application) |
| `sgh-address.l4` | 330 | s 12E(3) | ACHIEVEMENT, s 52 | "cause the exclusion from public access to resume": a thing done once, on its trigger (the change of contact address or Court direction) |
| `sgh-address.l4` | 350 | s 12E(4) | ACHIEVEMENT, s 52 | "cause the residential address to be excluded from public access in respect of the document": a thing done once, on its trigger (the form lodged) |
| `sgh-address.l4` | 367 | s 12F(2) | OTHER | "give the individual, and each company the paragraphs name, the notice under subsection (3)": the text's only time is "before" a later act: "before causing the individual's residential address to cease to be excluded" |
| `sgh-address.l4` | 378 | s 12F(4) | OTHER | "consider the representations given in response to the notice": tied to a window another person holds (the individual's window for representations) |
| `sgh-address.l4` | 391 | s 12F(5) | OTHER | "give notice of the decision to the individual and to each company": the text's only time is "before" a later act: "before doing so" |
| `sgh-address.l4` | 423 | s 12F(9) | ACHIEVEMENT, s 52 | "replace the individual's contact address in each register kept under section 12(1)": a thing done once |
| `sgh-constitution.l4` | 377 | s 22(2) | OTHER | "make a declaration to the Registrar as to the number of shares the subscriber agrees to take": a step taken to obtain what is applied for (a subscriber's declaration made in the course of incorporating the company); no event arms a clock |
| `sgh-formation.l4` | 377 | s 17(9) | ACHIEVEMENT, s 52 | "issue to the company a certificate of confirmation of incorporation": a thing done once, on its trigger (the application and the fee) |
| `sgh-incorporation.l4` | 357 | s 19(1)(a) | OTHER | "submit to the Registrar the constitution of the proposed company and such other documents as...": a step taken to obtain what is applied for (a person "desiring to incorporate a company" does this to obtain incorporation); no event arms a clock |
| `sgh-incorporation.l4` | 369 | s 19(1)(b) | OTHER | "furnish the Registrar with the last day of the proposed company's first financial year and s...": a step taken to obtain what is applied for (a person "desiring to incorporate a company" does this to obtain incorporation); no event arms a clock |
| `sgh-incorporation.l4` | 379 | s 19(1)(c) | OTHER | "pay the Registrar the prescribed fee": a step taken to obtain what is applied for (a person "desiring to incorporate a company" does this to obtain incorporation); no event arms a clock |
| `sgh-incorporation.l4` | 401 | s 19(2) | OTHER | "make the declaration to the Registrar": a step taken to obtain what is applied for (a person "desiring to incorporate a company" does this to obtain incorporation); no event arms a clock |
| `sgh-incorporation.l4` | 415 | s 19(3) | ACHIEVEMENT, s 52 | "register the company by registering its constitution": a thing done once, on its trigger (receipt of the documents, information and payment) |
| `sgh-incorporation.l4` | 433 | s 19(4) | ACHIEVEMENT, s 52 | "issue a notice of incorporation": a thing done once, on its trigger (registration of the constitution) |
| `sgh-incorporation.l4` | 446 | s 19(7) | ACHIEVEMENT, s 52 | "issue to the company a certificate of confirmation of incorporation": a thing done once, on its trigger (the application and the fee) |
| `sgh-incorporation.l4` | 476 | s 20(2) | OTHER | "refuse to register the constitution": a bar on a power (the Registrar "must refuse to register" if satisfied of a ground), breached by registering, not an act that falls due |
| `sgh-part2-inspection.l4` | 446 | s 8B(4)(d) | MAINTENANCE | "permit a person entitled to inspect the books to inspect them at all reasonable times": a state that must hold throughout ("at all reasonable times" during the period) |
| `sgh-part2-savings.l4` | 84 | s 8E | ACHIEVEMENT, s 52 | "give the name and address of the person to whom or by or on behalf of whom the communication...": a thing done once, on its trigger (refusal to produce the document) |
| `sgh-rectification.l4` | 328 | s 12B(1) | ACHIEVEMENT, s 52 | "rectify the register on receipt of the Court's order": a thing done once, on its trigger (receipt of the Court's order) |
| `sgh-rectification.l4` | 343 | s 12B(2) | ACHIEVEMENT, s 52 | "file the fresh document with a copy of the Court order and a copy of the Court application": a thing done once |
| `sgh-rectification.l4` | 367 | s 12D(2) | OTHER | "give written notice of the intention to rectify or update the register": the text's only time is "before" a later act: "before the Registrar rectifies or updates the register" |
| `sgh-registers.l4` | 401 | s 12A(3) | MAINTENANCE | "keep a record of the alteration of the electronic transaction system or the registers under...": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgh-returns.l4` | 382 | s 14(5) | ACHIEVEMENT, s 52 | "register the order of the Court lodged with the Registrar": a thing done once |
| `sgi-constitution.l4` | 186 | s 37(4) | OTHER | "submit a copy of the constitution to the Registrar in accordance with section 19(1)": its time is that of another act or filing: "in accordance with section 19(1)", whose own submission is a step in an application and has no clock |
| `sgi-constitution.l4` | 325 | s 40(1) | ACHIEVEMENT, s 52 | "send to the member a copy of the constitution": a thing done once, on its trigger (being so required by a member) |
| `sgi-contracts-seal.l4` | 291 | s 41(7) | OTHER | "certify in writing under his or her hand, on the instrument to which the official seal is af...": its time is that of another act or filing: the affixing of the official seal to the instrument |
| `sgi-director-transactions.l4` | 243 | s 25C(4)(a) | OTHER | "account to the company for any gain made directly or indirectly by the transaction": a liability that arises with the transaction (a gain made by the transaction), not an act that falls due |
| `sgi-director-transactions.l4` | 260 | s 25C(4)(b) | OTHER | "indemnify the company for any loss or damage resulting from the transaction": a liability that arises with the transaction (loss or damage resulting from the transaction), not an act that falls due |
| `sgi-name-changes.l4` | 585 | s 29(3) | ACHIEVEMENT, s 52 | "insert the conditions in the constitution of the company": a thing done once, on its trigger (the Registrar so directing) |
| `sgi-name-changes.l4` | 910 | s 29A(2)(a) | OTHER | "alter the constitution to reflect the change of name": a step taken to obtain what is applied for (a charitable company that "proposes to change its name" takes this step to obtain the change, the same shape as s 19(1)); no event arms a clock |
| `sgi-name-changes.l4` | 925 | s 29A(2)(b) | OTHER | "file the prescribed form with the Registrar, together with a copy of the special resolution...": a step taken to obtain what is applied for (a charitable company that "proposes to change its name" takes this step to obtain the change, the same shape as s 19(1)); no event arms a clock |
| `sgj-div4-substantial-shareholdings.l4` | 1026 | s 91(5) | OTHER | "satisfy itself that the order would not unfairly prejudice any person": to be weighed in the course of another act (the Court's own order, "before making an order"), with no time of its own |
| `sgj-div5-debentures.l4` | 51 | s 93(1) | MAINTENANCE | "keep a register of holders of the debentures at the registered office or at some other place...": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgj-div5-debentures.l4` | 137 | s 93(3) | MAINTENANCE | "keep the register open to inspection": a state that must hold throughout ("must ... be open to the inspection") |
| `sgj-div7-private-transfers.l4` | 74 | s 126(2) | ACHIEVEMENT, s 52 | "lodge with the Registrar notice of the transfer of shares in the prescribed form": a thing done once, on its trigger (a transfer of shares) |
| `sgj-div7-private-transfers.l4` | 165 | s 128(1)(a) | ACHIEVEMENT, s 52 | "lodge with the Registrar a notice of transfer of shares in the prescribed form": a thing done once, on its trigger (the transferor's written request) |
| `sgj-div7-private-transfers.l4` | 176 | s 128(1)(b) | ACHIEVEMENT, s 52 | "enter the name of the transferee in the register the company considers appropriate": a thing done once, on its trigger (the transferor's request) |
| `sgj-div7-private-transfers.l4` | 231 | s 128(3) | ACHIEVEMENT, s 52 | "require by written notice the person having possession, custody or control to deliver or pro...": a thing done once, on its trigger (the company calling in the documents) |
| `sgj-div7-private-transfers.l4` | 287 | s 128(6) | OTHER | "exhibit and advertise the list of share certificates or debentures called in and not deliver...": the text leaves the time to the party: "at such times as the company thinks fit" |
| `sgj-div7-public-transfers.l4` | 117 | s 130AA(1) | ACHIEVEMENT, s 52 | "enter in the appropriate register the name of the transferee": a thing done once, on its trigger (the transferor's request) |
| `sgj-div7-public-transfers.l4` | 155 | s 130AA(2) | ACHIEVEMENT, s 52 | "require by written notice the person having possession, custody or control to deliver or pro...": a thing done once, on its trigger (the company calling in the documents) |
| `sgj-div7-public-transfers.l4` | 210 | s 130AA(5) | OTHER | "exhibit and advertise the list of share certificates or debentures called in and not brought in": the text leaves the time to the party: "at such times as the company thinks fit" |
| `sgj-div7-public-transfers.l4` | 359 | s 130AC(2) | MAINTENANCE | "accept the document as sufficient evidence of the grant": a standing rule of treatment (a grant document "must be accepted"), not an act |
| `sgj-div7-title.l4` | 142 | s 123(2) | OTHER | "issue the share certificate under the seal and stating what the subsection requires": a requirement on the content or form of a document (a share certificate "must be under the common seal"), met when the document is made |
| `sgj-div7-title.l4` | 308 | s 125(1) | ACHIEVEMENT, s 52 | "issue a duplicate certificate or document in lieu of the one lost or destroyed": a thing done once, on its trigger (the owner's application) |
| `sgj-part5-office-name.l4` | 68 | s 142(1) | MAINTENANCE | "keep the registered office open and accessible to the public for not less than 3 hours durin...": a state that must hold throughout ("open and accessible to the public" each business day) |
| `sgk-div8-register.l4` | 92 | s 134(1) | ACHIEVEMENT, s 52 | "enter the particulars of the charge in the register": a thing done once |
| `sgk-div8-register.l4` | 115 | s 134(2) | ACHIEVEMENT, s 52 | "issue to the company a notice of the registration of the charge": a thing done once |
| `sgk-div8-register.l4` | 147 | s 134(3) | ACHIEVEMENT, s 52 | "issue to the company a certificate confirming the registration of the charge": a thing done once, on its trigger (the application and the fee) |
| `sgk-div8-register.l4` | 185 | s 135(1) | OTHER | "endorse on the debenture or certificate of debenture stock a copy of the notice of registrat...": a requirement on the content or form of a document (a copy of the notice endorsed "on every debenture ... which is issued"), met when the document is made |
| `sgk-div8-register.l4` | 255 | s 136(1) | ACHIEVEMENT, s 52 | "enter the particulars of the statement of satisfaction or release in the register": a thing done once |
| `sgk-div8-register.l4` | 364 | s 138(1) | MAINTENANCE | "keep the instrument creating the charge, or a copy, at the registered office": a state that must hold throughout ("for as long as the charge ... remains in force") |
| `sgk-div8-register.l4` | 460 | s 138(2) | MAINTENANCE | "keep a register of charges at the registered office": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgk-part9-consequences.l4` | 54 | s 237(1) | ACHIEVEMENT, s 52 | "pay the expenses of and incidental to the investigation": a thing done once |
| `sgk-part9-consequences.l4` | 92 | s 237(2)(a) | ACHIEVEMENT, s 52 | "make good the deficiency up to the amount of the security": a thing done once |
| `sgk-part9-declared.l4` | 211 | s 231(1) | ACHIEVEMENT, s 52 | "appoint one or more inspectors to investigate the affairs of the declared company": a thing done once |
| `sgk-part9-inspectors.l4` | 240 | s 233(1) | ACHIEVEMENT, s 52 | "report to the Minister the inspector's opinion on the affairs investigated, with the facts o...": a thing done once, on its trigger (the conclusion of the investigation) |
| `sgk-part9-inspectors.l4` | 250 | s 233(1) | ACHIEVEMENT, s 52 | "forward a copy of the report to the registered office of the company": a thing done once |
| `sgk-part9-inspectors.l4` | 264 | s 233(1A) | ACHIEVEMENT, s 52 | "give a copy of the report to a person whose affairs it relates to in a material extent": a thing done once |
| `sgk-part9-inspectors.l4` | 344 | s 233(3) | ACHIEVEMENT, s 52 | "institute a prosecution": a thing done once |
| `sgk-part9-inspectors.l4` | 353 | s 233(3) | OTHER | "give the Minister all assistance in connection with the prosecution that the person is reaso...": an effort standard (assistance "in connection with the prosecution", at the Minister's requirement), neither one act nor a state |
| `sgk-part9-inspectors.l4` | 427 | s 236(1) | ACHIEVEMENT, s 52 | "report on the affairs of the related corporation": a thing done once |
| `sgk-part9-inspectors.l4` | 467 | s 236(2) | ACHIEVEMENT, s 52 | "produce to the inspector all books and documents in the person's custody or power and give a...": a thing done once, on its trigger (the inspector's requirement) |
| `sgk-part9-inspectors.l4` | 531 | s 236(4)(c) | MAINTENANCE | "permit the corporation to have access to the books and documents taken possession of": a state that must hold throughout ("at all reasonable times ... so long as they are in his or her possession") |
| `sgk-part9-ownership.l4` | 78 | s 243(3) | ACHIEVEMENT, s 52 | "appoint an inspector to conduct the investigation": a thing done once |
| `sgk-part9-ownership.l4` | 249 | s 244(3) | ACHIEVEMENT, s 52 | "give the Minister information required under section 244": a thing done once, on its trigger (the Minister's requirement) |
| `sgk-part9-ownership.l4` | 472 | s 245(3)(c) | ACHIEVEMENT, s 52 | "notify the holders entitled to vote of the restrictions": a thing done once |
| `sgl-calling.l4` | 391 | s 176(4) | OTHER | "retain the sum out of sums due to the directors in default": a direction on recouping a sum (retained "out of any sums due or to become due" to the directors in default), not an act with a time |
| `sgl-calling.l4` | 392 | s 176(4) | ACHIEVEMENT, s 52 | "pay the requisitionists their reasonable expenses": a thing done once |
| `sgl-circulation.l4` | 387 | s 183(1)(a) | OTHER | "give members notice of the resolution": its time is that of another act or filing: the notice of the meeting: "at the same time as notice of the meeting" or "as soon as practicable thereafter", s 183(3C) |
| `sgl-circulation.l4` | 401 | s 183(1)(b) | OTHER | "circulate the statement to members": its time is that of another act or filing: the notice of the meeting: "at the same time as notice of the meeting" or "as soon as practicable thereafter", s 183(3C) |
| `sgl-circulation.l4` | 417 | s 183(4B) | ACHIEVEMENT, text's own standard | "notify the specified person of the date of receipt": a thing done once; the text's own standard is "without delay" |
| `sgl-minutes.l4` | 368 | s 188(1)(b) | OTHER | "have the minutes signed by the chairperson": its time is that of another act or filing: signature "by the chairperson of the next succeeding meeting" bounds it, not a period |
| `sgl-minutes.l4` | 403 | s 188(3B) | ACHIEVEMENT, text's own standard | "ensure the minutes are signed by a director": a thing done once; the text's own standard is "within a reasonable time" |
| `sgl-minutes.l4` | 418 | s 188(3C) | ACHIEVEMENT, text's own standard | "sign the minutes": a thing done once; the text's own standard is "within a reasonable time" |
| `sgl-minutes.l4` | 432 | s 189(1) | MAINTENANCE | "keep the books at the registered office or the principal place of business in Singapore": a state that must hold throughout ("must be kept ... at the registered office") |
| `sgl-statutory.l4` | 436 | s 174(6) | OTHER | "cause the list of members to be produced at the commencement of the meeting and to remain op...": tied to a meeting (the list "to be produced at the commencement of the meeting and to remain open" during it), whose own time governs |
| `sgl-written.l4` | 615 | s 184C(1) | ACHIEVEMENT, text's own standard | "send each member a copy of the text of the resolution": a thing done once; the text's own standard is "without delay" |
| `sgl-written.l4` | 633 | s 184D(2)(b) | ACHIEVEMENT, s 52 | "proceed to convene a general meeting for the resolution": a thing done once |
| `sgl-written.l4` | 666 | s 184F(1) | OTHER | "enter the record of the resolution in a book": its time is that of another act or filing: "in the same way as minutes", which s 188(1)(a) times ("within one month") |
| `sgm-part10.l4` | 205 | s 344(4) | ACHIEVEMENT, s 52 | "publish in the Gazette notice of the striking off of the name of the company": a thing done once |
| `sgm-part10.l4` | 393 | s 344(7)(a) | ACHIEVEMENT, s 52 | "send the particulars to the Inland Revenue Authority of Singapore and the Central Provident...": a thing done once |
| `sgm-part10.l4` | 419 | s 344(7)(b) | ACHIEVEMENT, s 52 | "publish the substance of the notices on the Authority's website": a thing done once |
| `sgm-part10.l4` | 487 | s 344A(3) | ACHIEVEMENT, s 52 | "send the company and its directors, secretaries and members a letter informing them of the a...": a thing done once |
| `sgm-part10.l4` | 566 | s 344A(5) | ACHIEVEMENT, s 52 | "strike off the name of the company from the register and publish a notice in the Gazette": a thing done once |
| `sgm-part10.l4` | 638 | s 344A(8)(a) | ACHIEVEMENT, s 52 | "send the particulars of the company and of the application to the Inland Revenue Authority o...": a thing done once |
| `sgm-part10.l4` | 664 | s 344A(8)(b) | ACHIEVEMENT, s 52 | "publish the substance of the notices on the Authority's website": a thing done once |
| `sgm-part10.l4` | 735 | s 344B(2)(a) | ACHIEVEMENT, s 52 | "send the company by ordinary post a notice that the application has been withdrawn": a thing done once |
| `sgm-part10.l4` | 750 | s 344B(2)(b) | ACHIEVEMENT, s 52 | "publish a notice on the Authority's website that the application has been withdrawn": a thing done once |
| `sgm-part10.l4` | 832 | s 344C(3)(a) | ACHIEVEMENT, s 52 | "give the applicant or applicants notice of the objection": a thing done once |
| `sgm-part10.l4` | 845 | s 344C(3)(b) | OTHER | "take into account the considerations prescribed in deciding whether to allow the objection": to be weighed in the course of another act (the Registrar's own decision whether to allow the objection), with no time of its own |
| `sgm-part10.l4` | 926 | s 344E(1) | ACHIEVEMENT, s 52 | "give the applicant notice of the decision": a thing done once |
| `sgm-part10.l4` | 984 | s 344E(2)(b)(i) | ACHIEVEMENT, s 52 | "enter in the register a note of the date on which the restoration takes effect": a thing done once |
| `sgm-part10.l4` | 999 | s 344E(2)(b)(ii) | ACHIEVEMENT, s 52 | "cause notice of the restoration to be published in the Gazette and on the Authority's website": a thing done once |
| `sgm-part5-div4.l4` | 394 | s 190(1) | MAINTENANCE | "keep a register of its members and enter in it what the subsection requires": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgm-part5-div4.l4` | 408 | s 190(5) | MAINTENANCE | "keep an index in convenient form of the names of the members": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgm-part5-div4.l4` | 628 | s 192(2) | MAINTENANCE | "open the register and index to inspection": a state that must hold throughout ("must be open to the inspection" of members) |
| `sgm-part5-div4.l4` | 1250 | s 196(4) | ACHIEVEMENT, text's own standard | "transmit to the office at which the principal register is kept a copy of every entry in the...": a thing done once; the text's own standard is "as soon as possible" |
| `sgm-part5-div4.l4` | 1261 | s 196(4) | MAINTENANCE | "cause to be kept at that office a duplicate of the branch register, duly entered up": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgm-part5-div4a.l4` | 49 | s 196A(1) | MAINTENANCE | "keep and maintain an electronic register of members of the private company": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgm-part5-div4a.l4` | 256 | s 196A(5) | ACHIEVEMENT, s 52 | "update the electronic register of members in accordance with the change": a thing done once, on its trigger (a change lodged with the Registrar) |
| `sgn-nominees.l4` | 65 | s 386AKA(1) | MAINTENANCE | "keep a register of its directors who are nominees in the prescribed form and at the prescrib...": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgn-nominees.l4` | 684 | s 386ALA(1) | MAINTENANCE | "keep a register of its shareholders who are nominees in the prescribed form and at the presc...": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgn-notices.l4` | 56 | s 386AG(1) | OTHER | "take reasonable steps to find out and identify the registrable controllers": an effort standard ("take reasonable steps to find out and identify"), neither one act nor a state |
| `sgn-register.l4` | 382 | s 386AF(7)(a) | MAINTENANCE | "ensure that the register contains the prescribed particulars of its registrable individual c...": a state that must hold throughout ("ensure that the register contains" the particulars) |
| `sgn-register.l4` | 397 | s 386AF(7)(aa) | MAINTENANCE | "ensure that the register contains the note and prescribed particulars required under section...": a state that must hold throughout ("ensure that the register contains" the note and particulars) |
| `sgn-register.l4` | 414 | s 386AF(7)(b) | OTHER | "ensure that the register is updated if any change to the prescribed particulars occurs": the Act itself defers the time to regulations ("within the prescribed time", s 386AF(8), which covers this update), so s 52 is not the standard |
| `sgn-register.l4` | 432 | s 386AF(7)(c) | MAINTENANCE | "ensure that the register is kept in the prescribed form and at the prescribed place": a state that must hold throughout ("ensure that the register is kept in the prescribed form and at the prescribed place") |
| `sgn-register.l4` | 502 | s 386AF(9)(a) | OTHER | "enter or update the particulars of a controller after the controller has confirmed them": the Act itself defers the time to regulations ("within the prescribed time", s 386AF(8)), so s 52 is not the standard |
| `sgn-register.l4` | 515 | s 386AF(9)(b) | OTHER | "enter or update the particulars of a controller with a note that they have not been confirme...": the Act itself defers the time to regulations ("within the prescribed time", s 386AF(8)), so s 52 is not the standard |
| `sgn-register.l4` | 797 | s 386AFA(3) | OTHER | "enter in the register of controllers the note and the prescribed particulars of each directo...": the Act itself defers the time to regulations ("within the prescribed period", s 386AFA(4)), so s 52 is not the standard |
| `sgn-registrar.l4` | 237 | s 386AN(2)(a) | MAINTENANCE | "keep a central register of controllers consisting of the particulars contained in the regist...": a register, index or record to be kept: it must hold throughout, not be done once |
| `sgn-registrar.l4` | 258 | s 386AN(2)(b) | ACHIEVEMENT, s 52 | "require a company or foreign company to which this Part applies to lodge the particulars con...": a thing done once, on its trigger (the Registrar requiring it) |
| `sgn-registrar.l4` | 410 | s 386ANA(1) | MAINTENANCE | "keep a central register of nominee directors and a central register of nominee shareholders": a register, index or record to be kept: it must hold throughout, not be done once |

## What was done to the achievement sites

Status: decided by Claude on 2026-11-26, assumed, not ruled; each point can be reversed alone.

- **The `LEST` is back, word for word.**
  At each of the 105 ACHIEVEMENT sites the clause the comment carried is the `LEST` again, and every one of the 105 was compared with the line of the same number in the commit before the drop (`8b082ad0c^`) and is byte-for-byte equal to it.
  4 of them, the sites whose closing parenthesis had moved to the line above, have it back at the end of the `LEST` line.
- **The `WITHIN` is an input.**
  Each such rule gains a rule-level `GIVEN`, written last in the rule's `GIVEN` list: `` `the period of all convenient speed, as found` IS A NUMBER ``, in days, which is the unit of every other `WITHIN` in this folder and of the `AT` of every `#TRACE`.
  It means how many days count as all convenient speed for that duty, as found by whoever applies the rule on the facts in front of them.
  That is the input of the 83 rules (86 sites) whose section states no time: the rule's `WITHIN` names it, and a comment on the same line cites Interpretation Act 1965 s 52 ("with all convenient speed") and says that this is assumed, not ruled.
  The wording of s 52 was read on 2026-11-26 in the lawplain copy of the Interpretation Act 1965 (`IA1965`, current, https://sso.agc.gov.sg/Act/IA1965), headed "Provision when no time prescribed": "Where no time is prescribed or allowed within which anything is to be done, that thing is to be done with all convenient speed and as often as the prescribed occasion arises."
  That is the wording the project's brief quotes.
  The Act is in this repository at `subjects/sg/interpretation-act/registers/source-bundle/IA1965.txt:2188-2190`, where the same wording stands under the heading "Provision when no time prescribed" (read on 2026-11-27).
  The 19 rules whose section gives its own standard of time take a different input, written the same way and last in the rule's `GIVEN` list: `` `the period the standard of time allows, as found` IS A NUMBER ``, in days.
  Its `WITHIN` carries a comment that gives the section's own word as the standard ("immediately", "as soon as is practicable", "without delay", "within a reasonable time", ...) with its section number, and does not mention Interpretation Act 1965 s 52, which does not reach these sites because they prescribe their own standard (decided by Claude on 2026-11-26, assumed, not ruled).
  No rule has both inputs.
- **No default number is anywhere.**
  There is no `TYPICALLY` on the input, and no number in any rule; the only numbers are the ones each `#TRACE` supplies (see the tests commit).
  The project's guidance on the length of the standard is that a week or two is good, a month is concerning, and more than six weeks could be considered spiteful.
  That is guidance for whoever supplies the input, not a default, and no number taken from it appears in a rule.
- **Why a rule-level input and not a section-level one.**
  Measured on 2026-11-26 with the unstable build: a section `GIVEN` that nothing supplies, used as a `WITHIN`, stops the evaluation with `eval/internal-error` and not the assumed-term message.
- **What the period counts from.**
  As for any `WITHIN`: from the moment the obligation is owed, which in a trace is its `AT`, and in a chain of two duties (`s 206(1A)`, `s 362(4)`, the two operands of `s 215(4)`) from the moment the earlier one is done.
  One input serves each duty of such a rule.
  For `s 215(4)`, where the text says "after the expiration of one month", the caller starts the trace on the first day the transferee may act (the rule `s 215(4) the first day on which the transferee must act` finds it).
- **Callers.**
  The only callers of these rules are the `#TRACE` directives of the test modules: 210 call sites in 41 modules at the commit before this work began (the next section says what the tests added); no other rule and no `@export` calls them.
  A `#TRACE` that leaves the input out is an error under both `l4 check` and `l4 run`, and the code depends on the rule: `check/wrong-argument-count` ("expects 2 inputs, but here it is given 1 input") for the rules here, which take the name of the actor and the input, and `check/type-mismatch` for a rule with the input alone and no argument given (both measured on probes on 2026-11-27, under `l4 check` and `l4 run` alike, on a `dev` build of the unstable tip).
  Each call passes the input after the rule's other arguments.
- **Maintenance and other sites are untouched** apart from the class written at the end of their comment and, since the review of 2026-11-27, the opener of that comment (section "What the review of 2026-11-27 changed").
  The sections of the per-agent notes called "Rules with no breach path" were written before this pass; for a rule that is now an ACHIEVEMENT they are out of date, and this file is the later record: each of the 20 sections carries a dated pointer (2026-11-27) that lists the rules in it that now take a `WITHIN`.

## What the tests show now

Status: decided by Claude on 2026-11-26, assumed, not ruled; each point can be reversed alone.

- **Each `#TRACE` of an achievement rule passes the input as 7 or as 45, chosen per trace.**
  Neither is a default or a finding; they are two values that make the outcomes differ.
  A trace whose last event falls in days 8 to 45 gets 45 (so it keeps its outcome); a trace with no event, or only events by day 7, alternates; a trace with an event or a wait later than day 45 alternates too, and is past the period at either value.
- **59 `EXPECT` lines changed, all to `BREACH`: 20 from `FULFILLED` and 39 from `RESIDUAL`.**
  The `FULFILLED` ones are a late act (on day 400 or later): before, no `WITHIN` meant a late act still read `FULFILLED`; now the act is past the input.
  The `RESIDUAL` ones are a wait with no act (to day 60 or later, and in one trace the first duty of a pair done on day 1 and the second never) which ended with the obligation open because nothing could lapse; now it lapses.
  Every one is a trace of the achievement rule itself, and its old comment said in terms that the rule could not be breached ("a late act still reads FULFILLED", "the obligation stays open, never BREACH"), so the old line was about exactly this obligation and is wrong now.
  No `#ASSERT` was changed, and no trace of any other rule: the 344 traces of rules that are not achievements, in the same 41 modules, end as they did before.
- **One trace kept its outcome on purpose.**
  `s 176(4)` pays the requisitionists (an achievement) and then retains the sum out of what is due to the directors in default (OTHER, no time of its own): with 45 days, the payment on day 30 is in time and the retaining on day 400 is not timed, so the chain still ends `FULFILLED`.
  A third trace, with 7 days, shows the payment on day 30 breached.
- **72 traces were added**: 17 in-time acts (45 days, act on day 5, `FULFILLED`) for the rules that had no trace reaching `FULFILLED` once the late ones changed, and 55 late acts (7 days, the act on day 400, or on day 30 for `s 176(4)`, `BREACH`) for the rules that had none reaching `BREACH`.
  The achievement rules now have 282 traces (210 before); every one of the 41 test modules has at least one that reaches `BREACH`.
- **Five rule names lost "(no time limit)"** (`s 183(4B)`, `s 188(3B)`, `s 188(3C)`, `s 184C(1)`, `s 184D(2)(b)`), because they now have one; the name and every call changed together.
  The rows of the section "Dropped" below quote the old names.
- **The text that went stale was found by searching every line of the 108 changed `.l4` files** (67 rule modules, 41 test modules), not only the lines near a rule, for "no time", "no breach", "no deadline" and the like.
  Besides the 205 `-- no LEST:` comments, the line diff against commit 1142117325 rewrites 54 comment lines and 3 section headings in the rule modules, and 46 comment lines and 7 section headings in the test modules; they now say that the input sets the time (the s 52 input, or the section's own standard for the 19).
  The same words above a maintenance or other rule were left, because they are still true there.
- **The per-agent notes were kept in step.**
  Every `module:NNN` or `module.l4:NNN` cite in the markdown of this folder (1,596 cites) was mapped from commit 1142117325 to the tree through a line diff of the cited module: 114 of them moved because lines were added or removed above them (35 in `sga1`, `sgb1`, `sgh`, `sgl` and `sgm` NOTES.md, re-pointed at the tests commit, and 79 in `sgc2-NOTES.md`, which that pass missed and the review of 2026-11-27 found), and now cite the line they cited before; 22 more cite a line that itself changed (a `#TRACE` that gained its input, a comment), and cite the changed line.
  A second scan after the edit finds no cite whose line differs from the diff's mapping.
  The five renamed rules are renamed in `sgl-NOTES.md` too (12 places).
  Their sections called "Rules with no breach path" remain what they were, an account of the encoding before this pass, with a dated pointer under each heading.
- **How it was checked.**
  `check.sh` counts assertions and never reads a `#TRACE`, so a trace outcome was read from `l4 run` itself: every one of the 626 traces in the 41 modules ends as its `EXPECT` line says, on the unstable build and on the main build (112), with 0 errors on both; the same read of the 554 traces before the change found 0 differences between `EXPECT` and the outcome, so the instrument was not blind.

## What the review of 2026-11-27 changed

Status: decided by Claude on 2026-11-27, assumed, not ruled; each point can be reversed alone.
An independent review of the branch as it stood on 2026-11-26 found no wrong encoding result, but prose that contradicted what the branch did and six disputed classes.
This section is here so that a later editor does not silently undo a repair.

- **s 29A(2)(a) and (b) are OTHER again.**
  They are steps to change the name, the same shape as s 19(1), s 22(2) and s 357(1) (call 5), so each rule lost the s 52 input, the `WITHIN` and the `LEST`, which is a comment again.
  The two day-400 `BREACH` traces of `sgi-tests-name-changes.l4` went with them, and the traces of the two rules are back in the form they had at commit 1142117325.
- **s 205(6) is OTHER again** (call 9): "as so requested" imports "prior to the meeting" from (5)(b), which the module's own comment quotes, so the meeting's time governs.
  The same loss, and its trace in `sgc2-tests-s205.l4` is back in its form at commit 1142117325.
- **s 207(1) moved from s 52 to the text's own standard** (call 2): (1A) says "in sufficient time" of a report under (1).
  The rule keeps its one input, now named `the period the standard of time allows, as found`; no trace changed, because the input is positional.
- **s 210(8)(a) moved from the text's own standard to s 52** (call 2): "as soon as possible" governs the accountants' forwarding, not the directors' instruction (assumed, not ruled).
- **s 386AF(7)(b) moved from MAINTENANCE to OTHER** (call 4): s 386AF(8) gives the time of the update, "within the prescribed time", so it is neither a state that holds throughout nor under s 52, and it is not aligned with s 196A(5), whose section gives no time anywhere.
- **The opener of the 100 comments** no longer says that the section states no time and needs s 52: 30 of the 97 sites it then covered have a row that says the text does give a time, so it was wrong there.
  It says `no deadline is modelled for this duty`; the dropped clause and the class tag are unchanged.
- **The "Rules with no breach path" sections of the per-agent notes** each carry a dated pointer under the heading.
  15 of the 20 sections name at least one rule that now takes a `WITHIN` (102 rule mentions in all, in 94 rows of those sections), and the pointer lists them and says that "no time limit" and "no breach path" read as the position before this pass, wherever the notes say so of them; the other 5 sections say that none of their rules is affected (checked by rule name and by section label).
  Other places in the notes say the same of a rule that now has a breach path (the review counted 22 in `sgh`, `sgc2`, `sgg` and `sga1` alone); they are not rewritten one by one, and the pointer covers them.
- **`NOTES.md`**: the section "Dead LESTs dropped" is rewritten for the sort and renamed "The 205 untimed duties, sorted"; nothing linked to the old heading.
- **The code comments on s 377(2)** (`sgg-cessation.l4`, `sgg-tests-cessation.l4`) say the notice of the appointment is read as not governed by (a) or (b) (assumed, not ruled).
- **s 52 is cited by file and line**: `subjects/sg/interpretation-act/registers/source-bundle/IA1965.txt:2188-2190`.
- **79 cites in `sgc2-NOTES.md`** pointed at lines that moved when the achievement sites were restored; they are re-pointed (section "What the tests show now").
- **Numbers that moved**: ACHIEVEMENT 108 to 105 (s 52 89 to 86, the text's own standard 19 to 19), MAINTENANCE 36 to 35, OTHER 61 to 65; restored `LEST` lines 108 to 105; traces 629 to 626; added traces 75 to 72; achievement call sites 290 to 282; changed `EXPECT` outcomes stay at 59.
- **Claims withdrawn**: that no line moved (see "What was found and what was done"), and the figure of 1,458 cites, which did not reproduce; the cite count is now 1,596, counted over the whole folder.

## Dropped

Each row gives the module and the line the `LEST` was on, the rule, the section, and the statute words the decision rests on (copied from the text, with `/` for a line break in the quotation); "other time phrase" is a period the section states elsewhere, with the reason it is not this duty's.
A row is the reason given at the first drop.
Where a site's class has changed since (s 29A(2)(a) and (b), s 205(6), s 207(1), s 210(8)(a), s 386AF(7)(b)), the table in "Sorted by kind of duty" and the section "What the review of 2026-11-27 changed" give the present reading; the s 207(1) row below, which says that "in sufficient time" is in a different subsection, is the reading the review reversed.

### `sg-solvency.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 234 | s 7A(3) a director must take into account all liabilities | s 7A(3) | the directors of the company must take into account all liabilities of the company (including contingent liabilities) // other time phrase in section: that the company will be able to pay its debts as they fall due during the period of 12 months immediately after the date of the statement (No period for this duty; the 12 months in (1)(b) is part of the content of the opinion (and is months), not a deadline for taking liabilities into account.) |
| 258 | s 7A(4)(a) a director must have regard to the financial statements | s 7A(4)(a) | must have regard to — (i) the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be; and (ii) all other circumstances that the directors know or ought to know affect, or may affect, the value of the company’s assets and the value of its liabilities (including contingent liabilities) // other time phrase in section: that the ... (The 12 months in (1)(b) belong to the opinion the directors form, and are in months; no period is stated for the duty in (a)(ii).) |
| 259 | s 7A(4)(a) a director must have regard to the financial statements | s 7A(4)(a) | must have regard to — (i) the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be; and (ii) all other circumstances that the directors know or ought to know affect, or may affect, the value of the company’s assets and the value of its liabilities (including contingent liabilities) // other time phrase in section: that the ... (No period for the (a)(i) duty; this is the OUTER LEST (last line of the rule). The 12 months in (1)(b) is a different subsection's opinion content, and is months.) |

### `sga1-issue.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 595 | s 63B(1) a company must lodge the contract with the return of allotment | s 63B(1) | the company must lodge with the return of allotment the contract evidencing the entitlement of the allottee or a copy of any such contract certified as prescribed // other time phrase: the company must lodge with the Registrar a notice in the prescribed form with respect to the total amount of such payments and the increase in the total amount paid up on the relevant class of s ... (Timing is only 'with the return of allotment' (an anchor, no number; the return's own deadline is not in this section). The 14 days is in s 63C, a different section and duty.) |
| 655 | s 63B(3) a company must lodge the document specified in subsection (4) with the return of allotment | s 63B(3) | the company must lodge with the Registrar the document specified in subsection (4) within the time specified in subsection (5) // (5) The company must lodge the document specified in subsection (4) at the same time and together with the return of allotment. (Subsection (5) states the time as 'at the same time and together with the return of allotment', a standard without a number.) |

### `sga1-rights.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 407 | s 66(4) a company must cancel a share warrant issued before 29 December 1967 that is unaccounted for by the ex ... | s 66(4) | A company must cancel any share warrant which is issued by a company before 29 December 1967 that is unaccounted for by the expiry of the 2‑year period mentioned in subsection (2) (The only period is 2 years (years, not days), and it is the trigger counted from 1 July 2015 per (2), not a deadline to cancel; the statute gives no days for the cancelling.) |

### `sga3-76f-76g.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 285 | s 76G(1) the company must reduce its share capital or its profits by the total amount of the purchase price | s 76G(1) | (c) reduce the amount of its share capital and profits proportionately where the shares were purchased or acquired out of both the capital and the profits of the company, by the total amount of the purchase price paid by the company for the shares cancelled. (No time phrase anywhere in s 76G; the duty has no stated period.) |

### `sgb1-s149b-appointment.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 367 | s 152(2) a public company must send a copy of the notice of an intended removal to the director | s 152(2) | immediately send a copy thereof to the director concerned ('immediately' is a standard without a number; no other period in s 152 concerns this duty.) |

### `sgb1-s156-interests.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 471 | s 156(1) a director must declare the nature of the interest | s 156(1) | must as soon as is practicable after the relevant facts have come to his or her knowledge — (a) declare the nature of his or her interest at a meeting of the directors of the company; or (b) send a written notice to the company ('as soon as is practicable' is a standard without a number (same in (2)); (7)'s 'first meeting' is another subsection's anchor.) |
| 504 | s 156(11) the secretary must record every declaration in the minutes | s 156(11) | The secretary of the company must record every declaration under this section in the minutes of the meeting at which it was made  |
| 518 | s 156(12) the directors must permit the chief executive officer to attend | s 156(12) | The directors of a company must permit a chief executive officer of the company who is not a director to attend a meeting of the board of directors where such attendance is necessary  |

### `sgb1-s157-duties.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 437 | s 157(1) a director must at all times act honestly and use reasonable diligence | s 157(1) | A director must at all times act honestly and use reasonable diligence in the discharge of the duties of his or her office. ('at all times' is a continuing standard, not a number; the only numbers in the section are the fine and the 12 months' imprisonment in (3)(b).) |

### `sgc1-s199.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 56 | s 199(1) a company must cause accounting and other records to be kept | s 199(1) | Every company must cause to be kept such accounting and other records as will sufficiently explain the transactions and financial position of the company // other time phrase: (2) The company must retain the records referred to in subsection (1) for a period of not less than 5 years from the end of the financial year (The 5 years is the retention period of (2), a different subsection's duty, and is years; (6)'s offence says only 'a default penalty'.) |
| 138 | s 199(2A) a public company or a subsidiary company of a public company must devise and maintain a system of in ... | s 199(2A) | Every public company and every subsidiary company of a public company must devise and maintain a system of internal accounting controls sufficient to provide a reasonable assurance that // other time phrase: (2) The company must retain the records referred to in subsection (1) for a period of not less than 5 years from the end of the financial year (No period for this duty; the 5 years in (2) is retention of records (another duty, years).) |
| 171 | s 199(3) a company must keep its accounting records open to inspection by the directors | s 199(3) | must be kept at the registered office of the company or at such other place as the directors think fit and must at all times be open to inspection by the directors // other time phrase: (2) The company must retain the records referred to in subsection (1) for a period of not less than 5 years from the end of the financial year ('at all times' is a standing condition, not a number; the 5 years in (2) is another subsection's retention period.) |

### `sgc1-s201-statement.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 213 | s 201(23) a company with an old financial year must attach a copy of the report to its return | s 201(23) | a company referred to in subsection (22) must, when lodging a return with the Registrar under section 197, attach a copy of the report prepared in accordance with section 201(5) in force immediately before 1 July 2015 // other time phrase: take reasonable steps to ensure that the financial statements are audited as required by this Part not less than 14 days before the annual g ... (Anchored to the lodging of the return under s 197; no number given here.) |

### `sgc1-s201.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 281 | s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements | s 201(9)(b) | cause to be attached to those financial statements the auditor’s report that is furnished to the directors under section 207(1A) // other time phrase: take reasonable steps to ensure that the financial statements are audited as required by this Part not less than 14 days before the annual general meeting of the company (The 14 days is in (9)(a) and governs getting the statements audited, not the attaching in (9)(b); (b) states no period.) |
| 343 | s 201(11) the directors of a subsidiary company must state the name of its ultimate parent corporation | s 201(11) | the directors of the company must state in, or in a note as a statement annexed to, the financial statements laid before the company at its annual general meeting the name of the corporation which is its ultimate parent corporation // other time phrase: take reasonable steps to ensure that the financial statements are audited as required by this Part not less than 14 days befor ... (No period for this duty; anchored to the statements laid at the AGM.) |

### `sgc1-s201a.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 214 | s 201A(7) a company with an old financial year must attach a copy of the accounts to its return | s 201A(7) | a company referred to in subsection (6) must, when lodging a return with the Registrar under section 197, attach a copy of the accounts or consolidated accounts so prepared // other time phrase: the written notice must be issued to the directors not less than 3 months before the end of the financial year (Anchored to the lodging of the return under s 197, no number. The 3 months in (3) is the relevant person's notice period (months, another person's act).) |

### `sgc1-s201b.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 52 | s 201B(1) a listed company must have an audit committee | s 201B(1) | Every listed company must have an audit committee. // other time phrase: the board of directors must, within 3 months of that event, appoint such number of new members as may be required to make up the minimum number of 3 members (A standing duty with no period; the 3 months in (4) is months and belongs to a different duty (replacing members after a vacancy).) |
| 203 | s 201B(6) the auditor must appear before the committee when required to do so | s 201B(6) | The auditor has the right to appear and be heard at any meeting of the audit committee and must appear before the committee when required to do so by the committee. // other time phrase: the board of directors must, within 3 months of that event, appoint such number of new members as may be required to make up the minimum number of 3 members ('when required to do so by the committee' is a trigger, not a number; no time phrase in the section concerns this duty (the 3 months in (4) is months, a different duty).) |
| 225 | s 201B(7) the chairperson must convene a meeting of the committee on the auditor's request | s 201B(7) | Upon the request of the auditor, the chairperson of the audit committee must convene a meeting of the committee to consider any matters the auditor believes should be brought to the attention of the directors or shareholders. // other time phrase: the board of directors must, within 3 months of that event, appoint such number of new members as may be required to make up the min ... ('Upon the request' is a trigger with no number; the 3 months in (4) is months and a different duty.) |
| 277 | s 201B(9) the directors of a listed company must describe the audit committee's functions in the statement | s 201B(9) | the directors must describe in the statement the nature and extent of the functions performed by the audit committee pursuant to subsection (5) // other time phrase: the board of directors must, within 3 months of that event, appoint such number of new members as may be required to make up the minimum number of 3 members (No period for this duty; the 3 months in (4) is months and a different duty.) |

### `sgc1-s203.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 147 | s 203(3) the company must furnish a copy of the last financial statements on request | s 203(3) | must, on a request being made by the member or debenture holder to the company, be furnished by the company without charge with a copy of the last financial statements // (3A) If default is made in complying with subsection (1) or (3), the company and every officer of the company who is in default shall // other time phrase: (6) The directors of the company must, within 14 days ... ('on a request' is a trigger with no number, and (3A) names no days of default. The 14 days in (1)(a), (4), (4A) and (6) belong to other subsections' duties.) |

### `sgc1-s203a.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 88 | s 203A(4) the company must send copies of the documents to the member who wishes to receive them | s 203A(4) | Copies of the documents referred to in section 203(1) must be sent to any member of the company who wishes to receive them. (No period in s 203A; the 14 days is in s 203(1), a different section's duty, and 203A(4) does not repeat it.) |
| 151 | s 203A(6A) the directors must ensure that the summary financial statements comply | s 203A(6A) | The directors of the company must ensure that the summary financial statements comply with the requirements referred to in subsections (5) and (6). (No time phrase in s 203A concerns this duty; (7)'s default offence names no days.) |

### `sgc2-s205-appointment.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 124 | s 205(2) the company must appoint an auditor at each annual general meeting | s 205(2) | A company must at each annual general meeting of the company appoint an accounting entity or accounting entities to be the auditor or auditors of the company // other time phrase: (1) The directors of a company must, within 3 months after incorporation of the company, appoint an accounting entity or accounting entities to be the auditor or auditors of the company (Anchored to each AGM, no number. The 3 months is in (1), months, and is the directors' duty to appoint the first auditor.) |
| 221 | s 205(5)(a) the company must send a copy of the notice of the removal resolution | s 205(5)(a) | it must immediately send a copy of the notice to the auditor concerned and to the Registrar // other time phrase: the auditor may, within 7 days after the receipt by the auditor of the copy of the notice, make representations in writing to the company ('immediately' is a standard without a number. The 7 days in (5)(b) is the auditor's time to make representations, another person's act.) |
| 285 | s 205(6) the company must send a copy of the representations | s 205(6) | Unless the Registrar on the application of the company otherwise orders, the company must send a copy of the representations as so requested // other time phrase: the company must, not less than 7 days before the adjourned meeting or the annual general meeting, send a copy of the notice to the accounting entity nominated ((6) states no period ((5)(b) says only 'prior to the meeting', no number). The 7 days is in (12) and belongs to a different duty (sending the nomination notice).) |
| 390 | s 205(8) the company must give written notice of the removal to the Registrar | s 205(8) | A company must, immediately after the removal of an auditor from office pursuant to subsection (4), give written notice of the removal to the Registrar // other time phrase: the auditor may, within 7 days after the receipt by the auditor of the copy of the notice, make representations in writing to the company ('immediately after' is a standard without a number; the 7 days in (5)(b) and (12) are other subsections' periods.) |

### `sgc2-s205a-exemption.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 303 | s 205B(4)(d) the directors must accompany the annual return with a statement | s 205B(4)(d) | the annual return of the company to be lodged with the Registrar must be accompanied by a statement by the directors / not later than one month before the end of that year (No period for the directors' statement; the one-month phrase in (6) is the members' written notice requiring an audit, a different person's act.) |
| 545 | s 205C(7) the company must attach a copy of the accounts to the return | s 205C(7) | must, when lodging a return with the Registrar under section 197, attach a copy of the accounts or consolidated accounts so prepared (Only 'when lodging a return': an event, no number of days; no other time phrase in 205C bears on this duty.) |

### `sgc2-s205aa-resignation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 195 | s 205AB(2) the Registrar must notify the auditor and the company whether it consents | s 205AB(2) | The Registrar must, as soon as practicable after receiving the application from an auditor under subsection (1), notify the auditor and the company whether it consents to the resignation of the auditor. (Non-numeric standard: 'as soon as practicable'.) |
| 379 | s 205AC(3)(a) the company that applies must give notice of the application to the auditor | s 205AC(3)(a) | the company must give notice of the application to the auditor of the company / if an application is made to the Court within 14 days, beginning on the date on which the company received the written statement (The 14 days is the time to apply to the Court (subsection (2)), and (1)'s 14 days is for sending copies to members; neither is the (3) notice duty; (4) default covers only subsection (1).) |
| 388 | s 205AC(3)(b) any other person who applies must give notice of the application to the company and the auditor | s 205AC(3)(b) | that person must give notice of the application to the company and the auditor of the company / if an application is made to the Court within 14 days, beginning on the date on which the company received the written statement (Same as (3)(a): the 14 days is the time to apply to the Court, a different act; no period for giving notice of the application.) |

### `sgc2-s206-208a-duties.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 149 | s 206(1)(c) the company must prepare the statement of the auditor's other emoluments | s 206(1)(c) | the company must immediately — (c) prepare or cause to be prepared a statement showing particulars of all emoluments paid to the auditor or other person and of the services in respect of which the payments have been made for the financial year immediately preceding the service of such notice; (d) forward a copy of the statement to all persons entitled to receive notice of gener ... (Non-numeric standard: 'immediately'; (2) default offence names no days.) |
| 158 | s 206(1)(d) the company must forward a copy of the statement | s 206(1)(d) | the company must immediately — (c) prepare or cause to be prepared a statement showing particulars of all emoluments paid to the auditor or other person and of the services in respect of which the payments have been made for the financial year immediately preceding the service of such notice; (d) forward a copy of the statement to all persons entitled to receive notice of gener ... (Non-numeric standard: 'immediately'; (2) default offence names no days.) |
| 167 | s 206(1)(e) the company must lay the statement before the company in general meeting | s 206(1)(e) | the company must immediately — (c) prepare or cause to be prepared a statement showing particulars of all emoluments paid to the auditor or other person and of the services in respect of which the payments have been made for the financial year immediately preceding the service of such notice; (d) forward a copy of the statement to all persons entitled to receive notice of gener ... (Non-numeric standard: 'immediately'; (2) default offence names no days.) |
| 206 | s 206(1A) the public company must review the auditor's fees and send the outcome | s 206(1A) | a public company must, under prescribed circumstances, undertake a review of the fees, expenses and emoluments of its auditor to determine whether the independence of the auditor has been compromised, and the outcome of the review must be sent to all persons entitled to receive notice of general meetings of the company ("immediately" is in (1); (1A) says "Without affecting subsection (1)" and names no period.) |
| 207 | s 206(1A) the public company must review the auditor's fees and send the outcome | s 206(1A) | a public company must, under prescribed circumstances, undertake a review of the fees, expenses and emoluments of its auditor to determine whether the independence of the auditor has been compromised, and the outcome of the review must be sent to all persons entitled to receive notice of general meetings of the company (No period in (1A); 'immediately' belongs to (1)(c)-(e), and (2) default names no days. This is the outer, last LEST; the inner LEST (line 206) is a separate site.) |
| 264 | s 207(1) the auditor must report to the members | s 207(1) | An auditor of a company must report to the members / in sufficient time to enable the company to comply with the requirements of section 203(1) in relation to that report ((1) states no period; 'in sufficient time' is in (1A), a different subsection, and is a non-numeric standard.) |
| 303 | s 207(1A) the auditor must furnish the report to the directors in sufficient time | s 207(1A) | must be furnished by the auditor to the directors of the company in sufficient time to enable the company to comply with the requirements of section 203(1) in relation to that report (Non-numeric standard: 'in sufficient time'.) |
| 672 | s 207(9) the auditor must report the matter in writing to the Registrar | s 207(9) | the auditor must immediately report the matter in writing to the Registrar (Non-numeric standard: 'immediately'.) |
| 746 | s 207(9A) the auditor must report the matter to the Minister | s 207(9A) | the auditor must immediately report the matter to the Minister (Non-numeric standard: 'immediately'.) |

### `sgd-acquisition.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1263 | s 215(1B) the transferee must state which of the alternative terms is to apply on a failure to elect | s 215(1B) | the transferee must state which of those terms is to apply to the acquisition of the shares of a dissenting shareholder where the dissenting shareholder fails to make the election within the time allowed under subsection (1A) / a dissenting shareholder is entitled to elect not later than the end of one month after the date on which the notice is given under (No period for the transferee's statement; the one-month period in (1A) is the dissenting shareholder's time to elect (and months).) |
| 1280 | s 215(2) the transferor company must supply the dissenting shareholder with the written statement | s 215(2) | the dissenting shareholder is entitled to require the transferor company by a written demand served on the transferor company, within one month from the date on which the notice was given, to supply the dissenting shareholder with a written statement of the names and addresses of all other dissenting shareholders (The one month (months) is the dissenting shareholder's time to serve the demand, not a time for the company to supply; no period for the company's duty.) |
| 1325 | s 215(4) the transferee must transmit the notice and pay, allot or transfer the consideration | s 215(4)(a) | transmit a copy of the notice to the transferor company / the transferee must, after the expiration of one month after the date on which the notice has been given (The period is an earliest-time wait ("after the expiration of one month", or "after 14 days after a statement has been supplied"), not a deadline to perform.) |
| 1330 | s 215(4) the transferee must transmit the notice and pay, allot or transfer the consideration | s 215(4)(b) | pay, allot or transfer to the transferor company the amount / the transferee must, after the expiration of one month after the date on which the notice has been given (The period is an earliest-time wait ('after the expiration of one month', months; or 14 days after a statement), not a deadline to perform; second RAND operand, last clause of the rule.) |
| 1341 | s 215(4) the transferor company must register the transferee as the holder of the shares | s 215(4) | and the transferor company must thereupon register the transferee as the holder of those shares. (Non-numeric standard: 'thereupon'.) |
| 1356 | s 215(5) the transferor company must pay the sums received into a separate bank account | s 215(5) | Any sums received by the transferor company under this section must be paid into a separate bank account (No period stated for this duty.) |
| 1365 | s 215(5) the transferor company must hold the sums and other consideration in trust | s 215(5) | any such sums and any other consideration so received must be held by the transferor company in trust for the several persons entitled to the shares in respect of which they were respectively received. (A continuing duty with no period; the rule's own comment puts a 10-year period in subsection (6), a different duty (years).) |
| 1403 | s 215(7)(a) the Official Receiver must deal with the moneys as if they were paid under section 197 | s 215(7)(a) | deal with any moneys received under subsection (6) (No period stated for the Official Receiver's duty.) |
| 1411 | s 215(7)(b) the Official Receiver must sell or dispose of the other consideration | s 215(7)(b) | sell or dispose of any other consideration received under (No period stated for the Official Receiver's duty ('in such manner as the Official Receiver thinks fit' is not a time).) |
| 1425 | s 215AA(6) the joint transferees must make the notice by all of them, signed for each company by a director of ... | s 215AA(6) | must be made by all of the joint transferees and, where one or more of them is a company, signed by a director of that company (No period in 215AA; the time limits sit in section 215(1) and (3), not in this requirement.) |

### `sgd-amalgamation-solvency.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 383 | s 215I(3) a director must take into account all liabilities of the amalgamating company | s 215I(3) | the directors must take into account all liabilities of the amalgamating company (including contingent liabilities) (No period stated anywhere in 215I for this duty.) |
| 407 | s 215I(4)(a) the board must have regard to the most recent financial statements and all other circumstances | s 215I(4)(a) | (a) must have regard to — (i) the most recent financial statements of the amalgamating company that comply with section 201(2) and (5), as the case may be (No period stated anywhere in 215I for this duty.) |
| 419 | s 215J(2) a director must take into account all liabilities of the amalgamated company | s 215J(2) | the directors must take into account all liabilities of the amalgamated company (including contingent liabilities) (No period stated anywhere in 215J for this duty.) |
| 444 | s 215J(3)(a) the board must have regard to the most recent financial statements and all other circumstances | s 215J(3)(a) | (a) must have regard to — (i) the most recent financial statements of the amalgamating company and the other amalgamating companies that comply with section 201(2) and (5), as the case may be (No period stated anywhere in 215J for this duty.) |

### `sgd-amalgamation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1200 | s 215C(3) a director who votes in favour must sign the declaration | s 215C(3) | Every director who votes in favour of the resolution and the making of the statements mentioned in subsection (2) must sign a declaration stating / not less than 21 days before the general meeting mentioned in subsection (1)(a) ((3) states no period; the 21 days in (4) and (5) is for the board's sending and the directors' notices, different duties; (6) offence names no days.) |
| 1334 | s 215D(6) a director who votes in favour must sign the declaration | s 215D(6) | Every director who votes in favour of the making of the solvency statement mentioned in subsection (5) must sign a declaration stating / not less than 21 days before the general meeting mentioned in subsection (1) or (2) (as the case may be) give written notice of the proposed ((6) states no period; the 21 days in (3) is the written notice to secured creditors, and (5) 'before the commencement of the general meeting' is the solvency statement, different duties; (7) names no days.) |
| 1355 | s 215F(1) the Registrar must issue the notice of amalgamation on receiving the documents and fees | s 215F(1) | Upon the receipt of the relevant documents and fees, the Registrar must — / (b) if the amalgamated company is a new company — issue a notice of amalgamation in such form as the Registrar may determine together with the notice of incorporation under section 19(4). (The trigger is "Upon the receipt"; no number of days is stated.) |
| 1359 | s 215F(1) the Registrar must issue the notice of amalgamation on receiving the documents and fees | s 215F(1) | Upon the receipt of the relevant documents and fees, the Registrar must — / (a) if the amalgamated company is the same as one of the amalgamating companies — issue a notice of amalgamation in such form as the Registrar may determine (Trigger event 'Upon the receipt', no number of days; ELSE branch, last clause of the rule.) |
| 1371 | s 215F(3) the Registrar must remove the amalgamating companies from the register | s 215F(3) | The Registrar must, as soon as practicable after the effective date of an amalgamation, remove the amalgamating companies, other than the amalgamated company, from the register. (Non-numeric standard: 'as soon as practicable'.) |
| 1383 | s 215F(4) the Registrar must issue the certificate of confirmation of amalgamation | s 215F(4) | Upon the application of the amalgamated company and payment of the prescribed fee, the Registrar must issue to the amalgamated company a certificate of confirmation of amalgamation. (Trigger event 'Upon the application', no number of days.) |
| 1424 | s 215K(2)(a) the Official Receiver must deal with the moneys as if they were paid under section 197 | s 215K(2)(a) | The Official Receiver must — (a) deal with any moneys received under subsection (1) as if the moneys were paid to the Official Receiver under section 197 / may, after the expiration of 2 years and must before the expiration of 10 years (No period for the Official Receiver; the 2 and 10 years (years) bind the person holding the money, a different person and duty (subsection (1)).) |
| 1438 | s 215K(2)(b) the Official Receiver must sell or dispose of the other consideration | s 215K(2)(b) | (b) sell or dispose of any other consideration received under subsection (1) in such manner as the Official Receiver thinks fit / may, after the expiration of 2 years and must before the expiration of 10 years (No period for the Official Receiver; the 2 and 10 years (years) bind the person holding the money, a different person and duty (subsection (1)).) |

### `sgd-compromise.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1017 | s 210(6) the company must annex a copy of the order to every copy of the constitution issued after the order | s 210(6) | a copy of every order made under subsection (3AB)(c) must be annexed to every copy of the constitution of the company issued after the order has been made // (7) The Court may, by order, exempt a company from compliance with the requirements of subsection (6) or determine the period during which the company must so comply. (No period stated for the annexing duty; subsection (7) lets the Court set a period but gives no number, and (9) says only 'makes default in complying with subsection (6) or (8)' with no days.) |
| 1032 | s 210(8)(a) a director must instruct the accountants or solicitors named in the resolution to report | s 210(8)(a) | instruct such accountants or solicitors or both as are named in the resolution to report on the proposals and forward their report or reports to the directors as soon as possible // at least 7 days before the date of any meeting ordered by the Court to be summoned as provided in subsection (1) (Non-numeric standard 'as soon as possible'; the 7 days is the (8)(b) duty to make the reports available for inspection, a different duty.) |
| 1089 | s 210(10B)(a) the Official Receiver must deal with the moneys as if they were paid under section 197 | s 210(10B)(a) | deal with any moneys received under subsection (10A)  |
| 1097 | s 210(10B)(b) the Official Receiver must sell or dispose of the other consideration | s 210(10B)(b) | sell or dispose of any other consideration received under subsection (10A) in such manner as the Official Receiver thinks fit  |
| 1113 | s 211(3) the company must furnish the person with a copy of the statement free of charge | s 211(3) | must on making application in the manner indicated by the notice be furnished by the company free of charge with a copy of the statement // Each director and each trustee for debenture holders must give notice to the company of such matters relating to the director or the trustee as may be necessary for the purposes of this section within 7 days of the receipt of a request in w ... (No period for the company's duty to furnish the copy; the 7 days in (4) is the director's and trustee's duty to give notice, a different duty.) |

### `sge-p10a-357-358.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 51 | s 357(1) a foreign corporate entity that intends to be registered must apply to reserve the name of the intend ... | s 357(1) | A foreign corporate entity which intends to be registered as a company limited by shares under this Act must apply to reserve the name of the intended company. (No period anywhere in s 357.) |

### `sge-p10a-359.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 77 | s 359(3) upon registration the Registrar must issue a notice of transfer of registration | s 359(3) | Upon registration of the foreign corporate entity, the Registrar must issue a notice of transfer of registration in the prescribed form // within 60 days after the issue of the notice of transfer of registration under subsection (3) ('Upon registration' is a non-numeric standard; the 60 days in (6) is the foreign corporate entity's duty to submit a deregistration document, a different duty.) |
| 162 | s 359(4) the Registrar must issue a certificate of confirmation of registration upon the application of the co ... | s 359(4) | A certificate of confirmation of registration must be issued by the Registrar upon the application of the company. ('upon the application' is a non-numeric standard; the 60 days in (6) and the 30 days in (9) concern other duties (deregistration document; appeal).) |

### `sge-p10a-360.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 49 | s 360(1) the Registrar must refuse to register a foreign corporate entity if not satisfied that the requiremen ... | s 360(1) | The Registrar must refuse to register a foreign corporate entity if the Registrar is not satisfied that the minimum requirements prescribed for registration have been met // within 30 days after the date of the decision, appeal to the Minister whose decision is final (No period for the refusal duty; the 30 days in (3) is the aggrieved person's appeal period, a different act.) |
| 114 | s 360(2) the Registrar must refuse to register a foreign corporate entity if satisfied of a ground in the subs ... | s 360(2) | The Registrar must refuse to register a foreign corporate entity if the Registrar is satisfied that // within 30 days after the date of the decision, appeal to the Minister whose decision is final (No period for the refusal duty; the 30 days in (3) is the aggrieved person's appeal period, a different act.) |

### `sge-p10a-362.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 118 | s 362(2) before making an order of revocation the Registrar must give notice and consider representations | s 362(2) | (c) consider the company’s written representations (if any) that are received by the Registrar within the time specified in the notice ("within the time specified in the notice" is the company's window for representations; no period is stated for the Registrar to consider them.) |
| 119 | s 362(2) before making an order of revocation the Registrar must give notice and consider representations | s 362(2) | (a) give the company written notice of the Registrar’s intention to revoke the registration; // (b) specify in the notice a period of at least 30 days within which the company may make written representations to the Registrar (The 'at least 30 days' is the minimum window the notice must give the company for its representations, not a deadline on the Registrar's duty to give the notice; only 'before making an order of revocation'.) |
| 218 | s 362(4) the Registrar must publish the notice of the order of revocation and serve a copy on the company | s 362(4) | (b) serve a copy of the notice of the order of revocation on the company which registration is revoked. (No period is stated in s 362(4).) |
| 219 | s 362(4) the Registrar must publish the notice of the order of revocation and serve a copy on the company | s 362(4) | (4) The Registrar must — (a) cause a notice of the order of revocation to be published in the Gazette; and // (3) At the expiration of the time mentioned in the notice mentioned in subsection (2), the Registrar may (No period for publication in the Gazette; the time in (3) governs when the Registrar may make the order of revocation, not this duty.) |

### `sgg-cessation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 174 | s 377(2) an authorised representative must lodge notice of the appointment of a liquidator when one is appoint ... | s 377(2) | (a) within 14 days after the commencement of the liquidation or the dissolution; or (b) within such further time as the Registrar in special circumstances allows, lodge or cause to be lodged with the Registrar notice of that fact and, when a liquidator is appointed, notice of such appointment. (The text does state 14 days here, from the commencement of the liquidation; see the last section of this file for why they are not given to this duty.) |

### `sgg-identity.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 47 | s 375(1)(b) the foreign company must cause its name and place of formation to be stated in legible romanised l ... | s 375(1)(b) | cause its name and the place where it is formed or incorporated to be stated in legible romanised letters // need only comply with subsection (3) after the expiration of 12 months after that date (No period for the (1)(b) duty; the 12 months in (4) is a transitional period (in months) for subsection (3) only.) |
| 97 | s 375(1)(c) the foreign company must cause notice that the liability of its members is limited to be given | s 375(1)(c) | if the liability of its members is limited (unless the last word of its name is the word “Limited” or “Berhad” or the abbreviation “Ltd.” or “Bhd.”), cause notice of that fact // need only comply with subsection (3) after the expiration of 12 months after that date (No period for the (1)(c) duty; the 12 months in (4) is a transitional period (in months) for subsection (3) only.) |
| 141 | s 375(3) the foreign company must cause its unique entity number to appear in a legible form on its business l ... | s 375(3) | (3) The unique entity number of a foreign company, issued by the Registrar, must appear in a legible form on all business letters, statements of account, invoices, official notices and publications of or purporting to be issued or signed by or on behalf of the company. // (4) Despite subsection (3), a foreign company incorporated before 3 January 2016 need only comply with subs ... (The only period is 12 months, a transitional grace period for companies incorporated before 3 January 2016 (months, not days); no day-count for the standing duty.) |

### `sgg-lodging.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 516 | s 370(1) the foreign company must have a registered office in Singapore open and accessible to the public | s 370(1) | must be open and accessible to the public for not less than 5 hours between the hours of 9 a.m. and 5 p.m. each business day (A standing opening-hours condition, not a deadline in days; the 21 days in (5) and (7) concern other duties.) |
| 592 | s 370(4) the foreign company must lodge the notice and the consent statement for the new authorised representa ... | s 370(4) | (4) On the appointment of a new authorised representative, the company must lodge a notice mentioned in section 368(1)(e) and a consent statement in respect of the new authorised representative with the Registrar. // on the expiration of a period of 21 days after the date of lodgment of the notice (No period for the lodging duty; the 21 days in (5) is when the retiring authorised representative ceases, a different matter.) |
| 656 | s 370(6)(a) the foreign company must appoint another authorised representative | s 370(6)(a) | (a) the foreign company must appoint another authorised representative; and // (7) Where a foreign company’s sole authorised representative dies, the company must, within 21 days after the death of the authorised representative, appoint another authorised representative. (No period in (6)(a); the 21 days is in (7), which is the duty on the sole authorised representative's death, a different subsection's duty.) |

### `sgg-registers.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 235 | s 380(2)(a) the foreign company must keep an index in convenient form of the names of its members | s 380(2)(a) | (a) keep an index in convenient form of the names of the members; // (b) within 14 days after the date on which any alteration is made in the register of members, make any necessary alteration in the index (The 14 days is the (2)(b) duty to alter the index; the (2)(a) duty to keep an index has no period.) |
| 262 | s 380(2)(c) the foreign company must keep the index at the same place as the register of members | s 380(2)(c) | (c) keep the index at the same place as the register of members. // (b) within 14 days after the date on which any alteration is made in the register of members, make any necessary alteration in the index (The 14 days is the (2)(b) duty to alter the index; the (2)(c) duty to keep the index at the same place has no period.) |

### `sgg-returns.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 783 | s 374 the foreign company must lodge the return when it lodges its financial statements | s 374 | A foreign company must, at the time when making a lodgment of // also lodge with the Registrar a return containing prescribed information relating to the keeping of the following registers (Non-numeric standard: lodge the return at the same time as the financial statements; no day-count.) |

### `sgh-address.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 309 | s 12E(1) rule: the Registrar's duty to exclude the residential address from public access | s 12E(1) | 12E.—(1) The Registrar must cause (No period anywhere in s 12E that concerns this duty.) |
| 326 | s 12E(3) rule: the Registrar's duty to cause the exclusion to resume | s 12E(3) | the Registrar must cause the exclusion from public access to resume if (No period stated; the duty is triggered by a notice of change of contact address or a Court direction, with no deadline.) |
| 344 | s 12E(4) rule: the Registrar's duty to exclude the residential address entered in the form | s 12E(4) | the Registrar must cause the individual’s residential address to be excluded from public access in respect of that document under section 12(2)(b) (No period stated; the only date in (4) is a commencement date that conditions the duty.) |
| 361 | s 12F(2) rule: the Registrar's duty to give the notice under subsection (3) | s 12F(2) | (2) Before causing the individual’s residential address to cease to be excluded from public access pursuant to section 12E(2), the Registrar must give a notice under subsection (3) to — // within 30 days after the date of receiving the notice under subsection (5), appeal to the Court ('Before causing' is a non-numeric standard; the 30 days in (7) is the individual's appeal period, a different act.) |
| 372 | s 12F(4) rule: the Registrar's duty to consider the representations | s 12F(4) | The Registrar must consider the representations (if any) given in response to the notice mentioned in subsection (2) and received within the period specified by the Registrar under subsection (3)(b). (The only period is one 'specified by the Registrar' for the individual's representations; no deadline on the Registrar's consideration.) |
| 385 | s 12F(5) rule: the Registrar's duty to give notice of the decision | s 12F(5) | the Registrar must before doing so give notice of the decision to // within 30 days after the date of receiving the notice under subsection (5), appeal to the Court ('before doing so' is a non-numeric standard; the 30 days in (7) is the individual's appeal period, a different act.) |
| 415 | s 12F(9) rule: the Registrar's duty to replace the contact address | s 12F(9) | the Registrar must replace the individual’s contact address contained in each register kept by the Registrar under section 12(1) with the new contact address // within 3 years after the Registrar causes the individual’s residential address to cease to be excluded (No period for the replacement duty; the 3 years (years, not days) in (8) bars the individual from providing a contact address, a different matter.) |

### `sgh-constitution.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 377 | s 22(2) rule: the subscriber's duty to make a declaration of the number of shares | s 22(2) | must, if the company is to have a share capital, make a declaration to the Registrar, either personally or through a registered qualified individual authorised by the subscriber, as to the number of shares; elsewhere in s 22: within 14 days after the occurrence of such change (No period for the declaration; the 14 days in s 22(1AA) is the company's duty to lodge a notice of change in the number of members, a different duty.) |

### `sgh-formation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 375 | s 17(9) rule: the Registrar's duty to issue the certificate of confirmation of incorporation | s 17(9) | Upon the application of a company and payment of the prescribed fee, the Registrar must issue to the company a certificate of confirmation of incorporation.; elsewhere in s 17: within 2 years of that date (No period for issuing the certificate; the 2 years in s 17(6) is a conversion duty of old guarantee companies (and in years).) |

### `sgh-incorporation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 357 | s 19(1)(a) rule: the person desiring incorporation's duty to submit the constitution and documents | s 19(1)(a) | submit to the Registrar the constitution of the proposed company and such other documents as may be prescribed (Section 19 states no period for this duty.) |
| 369 | s 19(1)(b) rule: the person desiring incorporation's duty to furnish the last day of the first financial year | s 19(1)(b) | furnish the Registrar with the last day of the proposed company’s first financial year and such other information as may be prescribed (Section 19 states no period for this duty.) |
| 379 | s 19(1)(c) rule: the person desiring incorporation's duty to pay the prescribed fee | s 19(1)(c) | pay the Registrar the prescribed fee (Section 19 states no period for this duty.) |
| 401 | s 19(2) rule: the duty to make the declaration to the Registrar | s 19(2) | must make a declaration to the Registrar that (Section 19 states no period for the declaration.) |
| 413 | s 19(3) rule: the Registrar's duty to register the company | s 19(3) | Upon receipt of the documents, information and payment referred to in subsection (1) and declaration mentioned in (Anchor 'upon receipt' only; no number of days stated.) |
| 429 | s 19(4) rule: the Registrar's duty to issue a notice of incorporation | s 19(4) | On the registration of the constitution the Registrar must issue in the prescribed manner a notice of incorporation in the prescribed form (Anchor 'on the registration' only; no number of days stated.) |
| 440 | s 19(7) rule: the Registrar's duty to issue the certificate of confirmation of incorporation | s 19(7) | Upon the application of a company and payment of the prescribed fee, the Registrar must issue to the company a certificate of confirmation of incorporation. (Anchor 'upon the application' only; no number of days stated.) |
| 470 | s 20(2) rule: the Registrar's duty to refuse to register the constitution | s 20(2) | the Registrar must refuse to register the constitution of a proposed company where the Registrar is satisfied that; elsewhere in s 20: within 30 days of the date of the decision, appeal to the Minister (The 30 days in s 20(3) is the aggrieved person's appeal period, not a deadline on the Registrar's duty.) |

### `sgh-part2-inspection.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 446 | s 8B(4)(d) the person in possession must permit the inspection | s 8B(4)(d) | during that period must permit a person who would be entitled to inspect any one or more of those books; to inspect at all reasonable times such of those books as that person would be so entitled to inspect; elsewhere in s 8B: until the end of the period of one month after the date on which it was issued (Standard 'at all reasonable times' has no number; the one month in s 8B(2) is how long a warrant stays in force (and in months).) |

### `sgh-part2-savings.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 82 | s 8E the advocate and solicitor who refuses to produce the document must give the name and address | s 8E | if the advocate and solicitor refuses to produce the document he or she is nevertheless obliged to give the (No period stated anywhere in s 8E.) |

### `sgh-rectification.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 326 | s 12B(1) the Registrar must rectify the register on receipt of the order | s 12B(1) | the Registrar must, upon receipt of the order, rectify the register accordingly (Anchor 'upon receipt of the order' only; no number of days stated.) |
| 339 | s 12B(2) the applicant company must file the fresh document | s 12B(2) | a fresh document, showing the rectification, must be filed by the applicant company with the Registrar together with a copy of the Court order, and a copy of the Court application (No period stated in s 12B for the filing.) |
| 363 | s 12D(2) the Registrar must give written notice before rectifying or updating the register | s 12D(2) | Before the Registrar rectifies or updates the register under subsection (1), the Registrar must, except under prescribed circumstances, give written notice to the company or person whose documents or particulars are to be rectified or updated; elsewhere in s 12D: being a date at least 30 days after the date of the notice (The 30 days is the minimum gap before the objection date the notice must state, a period for the recipient, not a deadline for giving the notice; the duty is anchored only 'before' rectifying.) |

### `sgh-registers.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 401 | s 12A(3) the Registrar must keep a record whenever the system or the registers are altered under subsection (2 ... | s 12A(3) | The Registrar must keep a record whenever the electronic transaction system or the registers are altered under subsection (2). (No period stated in s 12A.) |

### `sgh-returns.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 380 | s 14(5) rule: the Registrar's duty to register the order | s 14(5) | the order may be lodged with the Registrar and must be registered by the Registrar (No period stated in s 14.) |

### `sgi-constitution.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 186 | s 37(4) the specified company must submit a copy of its constitution to the Registrar | s 37(4) | A copy of the constitution of a specified company must be submitted to the Registrar, in accordance with section 19(1) (No period in s 37; s 19(1) itself states none for submission.) |
| 323 | s 40(1) the company must send a copy of the constitution to the member who requires it | s 40(1) | A company must, on being so required by any member, send to the member a copy of the constitution (if any) subject to payment of $5 or such lesser sum as is fixed by the directors. (Anchor 'on being so required' only; no number of days stated.) |

### `sgi-contracts-seal.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 291 | s 41(7) the person affixing the official seal must certify the date and the place | s 41(7) | the person affixing any such official seal must, in writing under his or her hand, certify on the instrument to which it is affixed the date on which and the place at which it is affixed (No period stated in s 41.) |

### `sgi-director-transactions.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 243 | s 25C(4)(a) the person liable under subsection (4) must account to the company for any gain | s 25C(4)(a) | is liable — (a) to account to the company for any gain the party or the director has made directly or indirectly by the transaction (A liability with no period stated in s 25C.) |
| 260 | s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage | s 25C(4)(b) | (b) to indemnify the company for any loss or damage resulting from the transaction (A liability with no period stated in s 25C.) |

### `sgi-name-changes.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 583 | s 29(3) the company must insert the conditions in its constitution if the Registrar so directs | s 29(3) | must, if the Registrar so directs, be inserted in the constitution of the company; elsewhere in s 29: within 30 days after the notice is given by the Registrar under subsection (8) (The 30 days in s 29(8A) is the appeal period to the Minister, a different act.) |
| 908 | s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name | s 29A(2)(a) | alter its constitution to reflect the change of name (No period stated in s 29A.) |
| 923 | s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special ... | s 29A(2)(b) | file the prescribed form with the Registrar, together with a copy of the special resolution authorising the change of name (No period stated in s 29A.) |

### `sgj-div4-substantial-shareholdings.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1026 | s 91(5) the Court must satisfy itself before making an order | s 91(5) | The Court must, before making an order under this section and in determining the terms of such an order, satisfy itself, so far as it can; elsewhere in s 91: within such time and subject to such conditions (if any) as the Court thinks fit (The 'within such time' in s 91(3) is for a sale order and is set by the Court; this is a pre-condition duty with no number.) |

### `sgj-div5-debentures.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 51 | s 93(1) the company must keep a register of holders of the debentures | s 93(1) | must keep a register of holders of the debentures at the registered office of the company or at some other place in Singapore; elsewhere in s 93: within 7 days after the register is first kept at a place other than the registered office lodge with the Registrar notice (The 7 days in s 93(2) is the separate duty to lodge notice of the register's place; s 93(1) is a continuing duty to keep the register.) |
| 137 | s 93(3) the company must keep the register open to inspection | s 93(3) | The register must except when duly closed be open to the inspection of the registered holder of any debentures and of any holder of shares in the company; elsewhere in s 93: not exceeding in the aggregate 30 days in any calendar year (The 30 days in s 93(4) caps the closure periods, not a deadline for this duty; the one month in s 93(7) is for copies and is in months.) |

### `sgj-div7-private-transfers.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 72 | s 126(2) a private company must lodge notice of a transfer of shares with the Registrar | s 126(2) | Where there has been a transfer of shares, a private company must lodge with the Registrar notice of that transfer of shares in the prescribed form. (Anchor 'where there has been a transfer' only; no number of days stated.) |
| 161 | s 128(1)(a) a private company must lodge a notice of transfer of shares on the transferor's request | s 128(1)(a) | on the request in writing of the transferor of — (a) any share in a private company — the company must lodge with the Registrar a notice of transfer of shares in the prescribed form (Anchor 'on the request in writing' only; no number of days stated.) |
| 170 | s 128(1)(b) a private company must enter the name of the transferee on the transferor's request | s 128(1)(b) | (b) any debenture or other interest in a private company — the company must enter in such register as the company considers appropriate, the name of the transferee (Anchor 'on the request in writing' only; no number of days stated.) |
| 223 | s 128(3) a private company must require delivery or production of the documents by written notice | s 128(3) | the private company must by written notice require the person having the possession, custody or control of the share certificate or debenture and the instrument of transfer thereof or either; to deliver or produce it or them to the office of the company within a stated period, being not less than 7 and not more than 28 days after the date of the notice (The 7 to 28 days is the delivery period the notice must give the third person, not a deadline for the company to send the notice; the company's own duty is anchored only 'on the request in writing'.) |
| 279 | s 128(6) the company must exhibit and advertise the list | s 128(6) | must be exhibited in the office of the company and must be advertised in such newspapers and at such times as the company thinks fit (Non-numeric standard: 'at such times as the company thinks fit'.) |

### `sgj-div7-public-transfers.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 115 | s 130AA(1) a public company must enter the name of the transferee on the transferor's request | s 130AA(1) | Duty: the company must enter in the appropriate register the name of the transferee in the same manner and subject to the same conditions as if the application for the entry were made by the transferee. Time phrase elsewhere: within a stated period, being not less than 7 and not more than 28 days after the date of the notice (subsection (2): the period the company's notice give ... (No period for the (1) duty; the 7-28 day window in (2) belongs to another person's delivery duty and is stated in the notice.) |
| 151 | s 130AA(2) a public company must require delivery or production of the documents by written notice | s 130AA(2) | Duty: the public company must by written notice require the person having the possession, custody or control of the share certificate or debenture and the instrument of transfer thereof or either of them to deliver or produce it or them to the office of the company. Time phrase: within a stated period, being not less than 7 and not more than 28 days after the date of the notice ... (The 7-28 day period binds the notice recipient, is specified in the notice, and is a range; nothing times the company's duty to give the notice.) |
| 206 | s 130AA(5) the company must exhibit and advertise the list | s 130AA(5) | Duty: must be exhibited in the office of the company and must be advertised in such newspapers and at such times as the company thinks fit. (Non-numeric standard: at such times as the company thinks fit.) |
| 355 | s 130AC(2) a company must accept the document as sufficient evidence of the grant | s 130AC(2) | Duty: must be accepted by the company, despite anything in its constitution, as sufficient evidence of the grant. The section has no time phrase. (No period stated anywhere in s 130AC.) |

### `sgj-div7-title.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 142 | s 123(2) the company must issue share certificates as the subsection requires | s 123(2) | Duty: Every share certificate must be under the common seal of the company or, in the case of a share certificate relating to shares on a branch register, the official seal of the company and must state as at the date of the issue of the certificate. Time phrase elsewhere: as at the date of the issue of the certificate (the date as at which the contents are stated, not a period ... (No period; the issue-date phrase fixes what the certificate must state, not when the company must act.) |
| 306 | s 125(1) the company must issue a duplicate certificate or document | s 125(1) | Duty: the company must on payment of a fee not exceeding $2 issue a duplicate certificate or document in lieu thereof to the owner on the owner’s application. Time phrase elsewhere: after the expiration of 14 days after the publication of the advertisement (subsection (2)(a): how long after the owner's own advertisement the owner intends to apply, a condition on the applicant's ... (The 14 days in (2)(a) is a wait on the owner before applying; s 125(1) states no period for issuing the duplicate.) |

### `sgj-part5-office-name.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 68 | s 142(1) the company must keep the registered office open for 3 hours on each business day | s 142(1) | Duty: must be open and accessible to the public for not less than 3 hours during ordinary business hours on each business day. Section's other time phrase: as from the date of its incorporation (the start of the duty to have a registered office, not a period). Subsection (2): If default is made in complying with subsection (1) (no number of days). (3 hours is a daily opening standard in hours, a recurring duty, not a deadline in days; business-day anchor; no period.) |

### `sgk-div8-register.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 90 | s 134(1) the Registrar must enter the particulars of the charge in the register | s 134(1) | Duty: The Registrar must keep a register of all the charges lodged for registration under this Division and must enter in the register with respect to those charges the following particulars. The section has no time phrase. (No period stated in s 134.) |
| 111 | s 134(2) the Registrar must issue to the company a notice of the registration of a charge | s 134(2) | Duty: The Registrar must issue a notice to the company concerned of the registration of a charge. The section has no time phrase. (No period stated in s 134.) |
| 141 | s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge | s 134(3) | Duty: Upon the application of the company and payment of the prescribed fee, the Registrar must issue to the company a certificate confirming the registration of the charge. The section has no time phrase. (Triggered on application and payment; no period stated in s 134.) |
| 179 | s 135(1) the company must cause the endorsement to be made | s 135(1) | Duty: The company must cause to be endorsed on every debenture forming one of a series of debentures, or certificate of debenture stock which is issued by the company and the payment of which is secured by a charge so registered. The section has no time phrase. (No period stated in s 135; (3) is an offence for delivering an unendorsed debenture with no number of days.) |
| 247 | s 136(1) the Registrar must enter the particulars of the statement in the register | s 136(1) | Duty: the Registrar must enter particulars of that statement in the register. Time phrase in the shown text: within the time required (from s 137, the Court's power to extend time for registering a charge, a different provision and a different person). (No period for the Registrar's entry; the only time phrase belongs to s 137 and concerns registration of a charge.) |
| 356 | s 138(1) the company must keep the instrument or a copy at its registered office | s 138(1) | Duty: Every company must cause the instrument creating any charge requiring registration under this Division or a copy thereof to be kept at the registered office of the company for as long as the charge to which the instrument relates remains in force. Time phrases elsewhere: for a period of 5 years after (subsection (1A)(b): years, and retention under section 199(2)); within ... (Continuing duty for as long as the charge is in force; no deadline; the 5 years is in years and the 3 days belongs to (3A).) |
| 452 | s 138(2) the company must keep a register of charges at its registered office | s 138(2) | Duty: Every company must keep at the registered office of the company a register of charges and enter therein all charges specifically affecting property of the company and all floating charges on the undertaking or any property of the company. Time phrases elsewhere: within 3 days of the person making the application (subsection (3A): furnishing copies on request, a different ... (No period for keeping the register; the 3 days is the (3A) copying duty and the 5 years is in years.) |

### `sgk-part9-consequences.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 52 | s 237(1) the company investigated must pay the expenses of the investigation | s 237(1) | Duty: must be paid by the company investigated or if the Minister so directs by the applicants or in part by the company and in part by the applicants. The section has no time phrase. (No period stated in s 237.) |
| 88 | s 237(2)(a) the applicants must make good the deficiency | s 237(2)(a) | Duty: the applicants must make good the deficiency up to the amount by which the security given by them under this Part exceeds the amount (if any) which they have under subsection (1) been directed by the Minister to pay. The section has no time phrase. (No period stated in s 237.) |

### `sgk-part9-declared.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 209 | s 231(1) the Minister must appoint inspectors for a declared company | s 231(1) | Duty: the Minister must appoint one or more inspectors to investigate the affairs of that company, and to report his or her opinion thereon to the Minister. Time phrase elsewhere: may specify the time or times and the manner in which the payment of the expenses must be made (subsection (5): when expenses are paid under a notification, a different duty, and unspecified). (No period for the appointment; the only time phrase concerns payment of expenses and names no number.) |

### `sgk-part9-inspectors.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 238 | s 233(1) the inspector must report to the Minister on the conclusion of the investigation | s 233(1) | Duty: on the conclusion of the investigation the inspector must report the inspector’s opinion on or in relation to the affairs that the inspector has been appointed to investigate together with the facts upon which the inspector’s opinion is based to the Minister. The section has no period in days. (Anchor is an event (conclusion of the investigation) with no number of days.) |
| 246 | s 233(1) the Minister must forward a copy of the report to the registered office | s 233(1) | Duty: a copy of the report must, subject to subsection (1B), be forwarded by the Minister to the registered office of the company. The section has no period in days. (No period stated for forwarding the copy.) |
| 258 | s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to | s 233(1A) | Duty: the Minister must give a copy of a report made under this Part to each person to whom in the opinion of the Minister the report ought to be given by reason that it relates to the affairs of that person to a material extent. The section has no period in days. (No period stated for giving the copy.) |
| 336 | s 233(3) the Minister must cause a prosecution to be instituted | s 233(3) | Duty: the Minister must cause a prosecution to be instituted accordingly. The section has no period in days. (No period stated for instituting the prosecution.) |
| 345 | s 233(3) the officer or agent must give the assistance on being required by the Minister | s 233(3) | Duty: all officers and agents of the company (other than the defendant in the proceedings) must on being required by the Minister to do so give all assistance in connection with the prosecution which they are reasonably able to give. The section has no period in days. (Triggered by the Minister's requirement, which states no number of days.) |
| 417 | s 236(1) the inspector must report on the affairs of the related corporation | s 236(1) | Duty: the inspector must report on the affairs of the other corporation so far as the inspector thinks the results of the investigation thereof are relevant to the investigation of the affairs of the company. Time phrase elsewhere: for such time as the inspector considers to be necessary for the purpose of the investigation (subsection (4)(b): how long the inspector may retain ...  |
| 455 | s 236(2) the officer or agent must produce the books and documents and give the assistance | s 236(2) | Duty: must, if required by an inspector appointed under this Part, produce to the inspector all books and documents in the officer’s or agent’s custody or power and must give to the inspector all assistance in connection with the investigation which he or she is reasonably able to give. Time phrase elsewhere: for such time as the inspector considers to be necessary for the purp ...  |
| 519 | s 236(4)(c) the inspector must permit the corporation to have access to the books and documents | s 236(4)(c) | Duty: must permit such corporation to have access at all reasonable times to all such books and documents so long as they are in his or her possession. (Non-numeric standard: at all reasonable times; so long as they are in his or her possession.) |

### `sgk-part9-ownership.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 76 | s 243(3) the Minister must appoint an inspector to conduct the investigation | s 243(3) | Duty: the Minister must appoint an inspector to conduct the investigation unless the Minister is satisfied that the application is vexatious. The section has no time phrase. (No period stated in s 243.) |
| 245 | s 244(3) a person must give the information required of the person under section 244 | s 244(3) | Duty: Any person who fails to give any information required of the person under this section. Subsection (1): to give such information to the Minister (no time stated). The section has no time phrase. (Offence text names no period, and the Minister's requirement in (1) states none.) |
| 466 | s 245(3)(c) the holder must notify the persons entitled to vote of the restrictions | s 245(3)(c) | Duty: being the holder of any of those shares, fails to notify the fact of their being subject to those restrictions to any person whom the firstmentioned person does not know to be aware of that fact but does know to be entitled, apart from those restrictions, to vote in respect of those shares whether as holder or proxy. The section has no period in days. (No period stated for the notification.) |

### `sgl-calling.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 389 | s 176(4) the company must pay the requisitionists and retain the sum | s 176(4) | Duty: any sum so paid must be retained by the company out of any sums due or to become due from the company by way of fees or other remuneration in respect of their services to such of the directors as were in default. Time phrases elsewhere: not later than 2 months after the receipt by the company of the requisition (subsection (1)); within 21 days after the date of the deposi ... (No period for retaining; this is the nested LEST (inside the HENCE, closing parenthesis on the line), so the person editing must keep the parenthesis.) |
| 390 | s 176(4) the company must pay the requisitionists and retain the sum | s 176(4) | Duty: Any reasonable expenses incurred by the requisitionists by reason of the failure of the directors to convene a meeting must be paid to the requisitionists by the company. Time phrases elsewhere: not later than 2 months after the receipt by the company of the requisition (subsection (1)); within 21 days after the date of the deposit of the requisition (subsection (3)): the ... (No period for paying the expenses; the 21 days and 2 months bind the directors' duty to convene, and the 3 months limits the requisitionists' own meeting.) |

### `sgl-circulation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 387 | s 183(1)(a) the company must give members notice of the resolution (no time limit) | s 183(1)(a) | (a) give to members of the company entitled to receive notice of the next annual general meeting notice of any resolution ... not less than 6 weeks before the meeting ... at the same time as notice of the meeting ... as soon as practicable thereafter (No period for the company's duty; the 6 weeks in (4)(a)(i) is the requisitionists' deposit time, and (3C) 'at the same time' / 'as soon as practicable' are non-numeric standards.) |
| 401 | s 183(1)(b) the company must circulate the statement to members (no time limit) | s 183(1)(b) | (b) circulate to members entitled to have notice of any general meeting sent to them any statement of not more than 1,000 words with respect to the matter referred to in any proposed resolution ... in the case of any other requisition — not less than one week before the meeting (No period for circulating the statement; the one week in (4)(a)(ii) is the requisitionists' deposit time (a precondition), not the company's deadline.) |
| 415 | s 183(4B) the directors must notify the specified person of the date of receipt (no time limit) | s 183(4B) | the directors must, without delay after it is first received by a director in legible form or a permitted alternative form, notify that person of the date when it was first so received (Non-numeric standard: 'without delay'.) |

### `sgl-minutes.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 368 | s 188(1)(b) the company must cause the minutes to be signed by the chairperson (no time limit) | s 188(1)(b) | (b) those minutes to be signed by the chairperson of the meeting at which the proceedings were had or by the chairperson of the next succeeding meeting ... to be entered in books kept for that purpose within one month of the date upon which the relevant meeting was held (The one month in (1)(a) governs entering the minutes in books, a different duty (and in months); (1)(b) signing has no period.) |
| 401 | s 188(3B) the company must ensure that the minutes are signed by a director (no time limit) | s 188(3B) | (3B) The company must ensure that minutes of the passing of a resolution mentioned in subsection (3A)(b) are signed by a director within a reasonable time after the resolution is passed. (Non-numeric standard: 'within a reasonable time'; the one month in (3A)(b) concerns entering the matters in the minute books.) |
| 414 | s 188(3C) the sole director must sign the minutes (no time limit) | s 188(3C) | must sign the minutes thereof within a reasonable time after the resolution is passed or the declaration is made (Non-numeric standard: 'within a reasonable time'.) |
| 428 | s 189(1) the company must keep the books at the registered office or the principal place of business in Singap ... | s 189(1) | must be kept by the company at the registered office or the principal place of business in Singapore of the company ... furnished within 14 days after the member has made a request in writing in that behalf to the company with a copy of any minutes specified in section 188(1) or (3A) (The 14 days in (2) is the period for furnishing a copy on request, a different duty (encoded by its own rule); keeping the books at a place has no period.) |

### `sgl-statutory.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 436 | s 174(6) the directors must cause the list of members to be produced and kept open and accessible (no time lim ... | s 174(6) | (6) The directors must cause a list showing the names and addresses of the members and the number of shares held by them respectively to be produced at the commencement of the meeting and to remain open and accessible to any member during the continuance of the meeting. ... to be lodged with the Registrar at least 7 days before the date of the statutory meeting (The duty is tied to the meeting itself (commencement, continuance), not a day-count; the 7 days in (2) and (5) concern the statutory report, a different duty.) |

### `sgl-written.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 613 | s 184C(1) the directors must send each member a copy of the text of the resolution (no time limit) | s 184C(1) | must send to each ... member, having the right to vote on that resolution at a general meeting, a copy of the text of the resolution ... the directors must comply with subsection (1) as respects every member at the same time and without delay (Subsection (1) states no period; 'at the same time and without delay' is in (2) and is a non-numeric standard.) |
| 629 | s 184D(2)(b) the directors must proceed to convene a general meeting for the resolution (no time limit) | s 184D(2)(b) | (b) the directors must proceed to convene a general meeting for the resolution. ... may, within 7 days after (The 7 days in (1) is the members' period to give the notice that triggers this duty, not the directors' period to convene.) |
| 662 | s 184F(1) the company must cause the record of the resolution to be entered in a book (no time limit) | s 184F(1) | the company must cause a record of the resolution, and the indication of each member’s agreement (or agreement on the member’s behalf) to it, to be entered in a book in the same way as minutes of proceedings of a general meeting of the company (No time phrase anywhere in s 184F; 'in the same way as minutes' is a manner, not a period (even if it imported s 188(1)(a)'s 'within one month', that is months, not days).) |

### `sgm-part10.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 203 | s 344(4) the Registrar must publish notice of the striking off in the Gazette (rule) | s 344(4) | At the expiration of the time mentioned in the notice, the Registrar may, unless cause to the contrary is previously shown, strike the name of the company off the register, and must publish notice thereof in the Gazette ... at the expiration of 60 days after the date of that notice (The 60 days in (2) is the show-cause wait before the Registrar may act (set in the notice), not a deadline for publishing; 'time mentioned in the notice' is not a number the statute fixes for this duty.) |
| 389 | s 344(7)(a) the Registrar must send the particulars to the Inland Revenue Authority of Singapore and the Centr ... | s 344(7)(a) | (7) The Registrar must ensure that — (a) such particulars of the company mentioned in subsection (1) and of the Registrar’s belief that the company is not carrying on business or is not in operation, as the Registrar may determine, is sent to — ... if an answer showing cause to the contrary is not received within 30 days after the date of the letter (No period for sending the particulars; the 30 days in (1) is the company's time to answer the letter, a different person's period.) |
| 413 | s 344(7)(b) the Registrar must publish the substance of the notices on the Authority's website (rule) | s 344(7)(b) | (b) the substance of the notices to be published in the Gazette referred to in subsections (2), (3) and (4) is also published on the Authority’s website. ... if an answer showing cause to the contrary is not received within 30 days after the date of the letter (No period for the website publication; the 30 days in (1) is the company's time to answer the letter.) |
| 479 | s 344A(3) the Registrar must send the letter informing the company, its directors, secretaries and members of ... | s 344A(3) | Upon receipt of the application, the Registrar must, if satisfied that the grounds and conditions (if any) referred to in subsection (1) have been satisfied, send to the company and its directors, secretaries and members a letter informing them of the application ... is not received within 30 days after the date thereof ('Upon receipt' is a trigger, not a period; the 30 days is the time given to the company and others to show cause, not the Registrar's deadline to send the letter.) |
| 556 | s 344A(5) the Registrar must strike off the name of the company from the register and publish a notice in the ... | s 344A(5) | If no person shows cause or sufficient cause within the period referred to in subsection (4)(b) as to why the name of the company should not be struck off the register, the Registrar must strike off the name of the company from the register and publish a notice in the Gazette ... may not strike a company’s name off the register under this section until after the expiration of 6 ... (The 60 days in (4) is a minimum wait before striking off, not a deadline; the show-cause period in (4)(b) is 'such period as may be prescribed'.) |
| 626 | s 344A(8)(a) the Registrar must send the particulars of the company and of the application to the Inland Reven ... | s 344A(8)(a) | (8) The Registrar must ensure that — (a) such particulars of the company and of the application mentioned in subsection (1), as the Registrar may determine, is sent to — ... is not received within 30 days after the date thereof (No period for sending the particulars; the 30 days in (3) is the time to show cause in response to the Registrar's letter.) |
| 650 | s 344A(8)(b) the Registrar must publish the substance of the notices on the Authority's website (rule) | s 344A(8)(b) | (b) the substance of the notices to be published in the Gazette referred to in subsections (4) and (5) is also published on the Authority’s website. ... is not received within 30 days after the date thereof ... until after the expiration of 60 days after the publication by the Registrar in the Gazette of a notice (No period for the website publication; the 30 days in (3) and 60 days in (4) concern other steps.) |
| 719 | s 344B(2)(a) the Registrar must send the company a notice that the application has been withdrawn (rule) | s 344B(2)(a) | Upon receipt of the notice mentioned in subsection (1), the Registrar must — (a) send to the company by ordinary post a notice that the application to strike the company’s name off the register has been withdrawn ... at any time before the name of the company has been struck off the register ('Upon receipt' is a trigger, not a period; 'at any time before ... struck off' in (1) is the applicant's window to withdraw.) |
| 732 | s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been with ... | s 344B(2)(b) | (b) publish a notice on the Authority’s website that the application to strike the company’s name off the register has been withdrawn ... at any time before the name of the company has been struck off the register (No period for the website notice; 'at any time before ... struck off' in (1) is the applicant's window to withdraw.) |
| 812 | s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection (rule) | s 344C(3)(a) | (a) must where applicable, give the applicant or applicants for striking the name of the company off the register notice of the objection ... not later than the date specified in the notice ('Upon receipt' is a trigger; 'not later than the date specified in the notice' in (1) is the objector's deadline, a different person's period.) |
| 825 | s 344C(3)(b) the Registrar must take into account the prescribed considerations (rule) | s 344C(3)(b) | (b) must, in deciding whether to allow the objection, take into account such considerations as may be prescribed ... not later than the date specified in the notice (No period for this duty; the date specified in the notice in (1) is the objector's deadline.) |
| 904 | s 344E(1) the Registrar must give the applicant notice of the decision (rule) | s 344E(1) | 344E.—(1) The Registrar must give notice to the applicant of the decision on an application under section 344D. ... the restoration takes effect as from the date that notice is sent (No period for giving notice; (2)(a) only fixes the date restoration takes effect (the date the notice is sent), not a deadline.) |
| 960 | s 344E(2)(b)(i) the Registrar must enter in the register a note of the date of the restoration (rule) | s 344E(2)(b)(i) | (b) the Registrar must — (i) enter in the register a note of the date on which the restoration takes effect ... the restoration takes effect as from the date that notice is sent (No period for entering the note; (2)(a) fixes the date restoration takes effect, not a deadline for the Registrar.) |
| 973 | s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published (rule) | s 344E(2)(b)(ii) | (ii) cause notice of the restoration to be published in the Gazette and on the Authority’s website ... the restoration takes effect as from the date that notice is sent (No period for publication; (2)(a) fixes the date restoration takes effect, not a deadline for the Registrar.) |

### `sgm-part5-div4.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 394 | s 190(1) a public company must keep a register of its members | s 190(1) | Every public company must keep a register of its members and enter therein — ... must, within 14 days after the date on which any alteration is made in the register of members, make any necessary alteration in the index ... the date at which any person who ceased to be a member during the previous 7 years so ceased to be a member ((1) states no period; the 14 days in (5) is for altering the index, a different duty, and the 7 years in (1)(c) is a scope of entries, not a deadline.) |
| 408 | s 190(5) a public company having more than 50 members must keep an index of the names of the members | s 190(5) | Every public company having more than 50 members must, unless the register of members is in such a form as to constitute in itself an index, keep an index in convenient form of the names of the members ... must, within 14 days after the date on which any alteration is made in the register of members, make any necessary alteration in the index  |
| 628 | s 192(2) a public company must open the register and index to inspection | s 192(2) | The register and index must be open to the inspection of any member without charge and of any other person on payment for each inspection of $1 or such less sum as the public company requires. ... to be sent to that person within a period of 21 days ... for one or more periods not exceeding 30 days in the aggregate in any calendar year (No period for inspection; the 21 days in (3) is for furnishing a copy on request, and the 30 days in (1) is the limit on closing the register, both different duties.) |
| 1248 | s 196(4) a public company must transmit a copy of every entry in its branch register | s 196(4) | The public company must transmit to the office at which its principal register is kept a copy of every entry in its branch register as soon as possible after the entry is made ... within 14 days after the opening of the office or of the change or discontinuance (Non-numeric standard: 'as soon as possible'; the 14 days in (2) is for lodging notice of the office with the Registrar, a different duty.) |
| 1259 | s 196(4) a public company must cause a duplicate of its branch register to be kept | s 196(4) | must cause to be kept at that office duly entered up from time to time a duplicate of its branch ... within 14 days after the opening of the office or of the change or discontinuance (No period for keeping the duplicate ('from time to time' is non-numeric; 'as soon as possible' governs the transmit limb); the 14 days in (2) is for lodging notice of the office.) |

### `sgm-part5-div4a.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 49 | s 196A(1) the Registrar must keep an electronic register of members of every private company | s 196A(1) | the Registrar must, in respect of every private company, keep and maintain an electronic register of members of that company. The only time phrase in the section is "On and after 3 January 2016", a commencement date, not a period for this duty. (No period stated; a start date is not a deadline.) |
| 254 | s 196A(5) the Registrar must update the electronic register of members | s 196A(5) | The Registrar must update the electronic register of members in accordance with any change that is required or authorised by any provision of this Act to be lodged with the Registrar. No period appears anywhere in the section for this duty. (No period stated for the Registrar's updating.) |

### `sgn-nominees.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 65 | s 386AKA(1) a company or foreign company must keep a register of nominee directors | s 386AKA(1) | must keep a register of its directors who are nominees (called in this Part the register of nominee directors) in the prescribed form and at the prescribed place. Elsewhere: "within 7 days after the company or foreign company is informed of any fact" (subsection (3)), which concerns entering facts in the register, not keeping it. (The 7 days in (3), (4) and (5) belong to different subsections' duties (entering and updating particulars); (1) states none.) |
| 684 | s 386ALA(1) a company or foreign company must keep a register of nominee shareholders | s 386ALA(1) | must keep a register of its shareholders who are nominees (called in this Part the register of nominee shareholders) in the prescribed form and at the prescribed place. Elsewhere: "within 7 days after the company or foreign company is informed of any fact and provided with any particulars" (subsection (2)), which concerns entering facts in the register, not keeping it. (The 7 days in (2), (3) and (4) belong to different subsections' duties; (1) states none.) |

### `sgn-notices.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 56 | s 386AG(1) a company or foreign company must take reasonable steps to find out and identify its registrable co ... | s 386AG(1) | must take reasonable steps to find out and identify the registrable controllers of the company or foreign company. Elsewhere: "must be given within such period as may be prescribed after the company or foreign company first knows the existence of" (subsection (3)(c)), which concerns giving notices under (2). (Standard is 'reasonable steps' with no number; the prescribed period in (3)(c) is for a different duty (giving notices).) |

### `sgn-register.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 382 | s 386AF(7)(a) a company or foreign company must ensure that its register contains the prescribed particulars | s 386AF(7)(a) | (a) contains such particulars of the company’s or foreign company’s registrable individual controllers and registrable corporate controllers as may be prescribed. Time phrases elsewhere: "not later than 30 days after the date of the company’s incorporation" (subsection (1)) and "not later than 60 days after that date" (subsection (2)), which concern when the register must first ... (The 30 and 60 days are the deadline to start keeping a register under (1) to (6), a different duty; (8) is a prescribed time, not a number.) |
| 397 | s 386AF(7)(aa) a company or foreign company must ensure that its register contains the note and particulars re ... | s 386AF(7)(aa) | (aa) contains the note and prescribed particulars required under section 386AFA(3), if applicable. Time phrases elsewhere: "not later than 30 days after the date of the company’s incorporation" (subsection (1)), which concerns when the register must first be kept; and "within the prescribed time" (subsection (8)). (30/60 days belong to (1) to (6), the duty to start keeping a register; (8) is a prescribed time, not a number.) |
| 414 | s 386AF(7)(b) a company or foreign company must ensure that its register is updated if any change occurs | s 386AF(7)(b) | (b) is updated if any change to the prescribed particulars mentioned in paragraph (a) or (aa) occurs. Time phrase elsewhere: "must enter the particulars in its register and update the register within the prescribed time and in the prescribed manner" (subsection (8)). (Prescribed time (subsection (8)) has no number in the Act; the 30/60 days in (1) to (6) are for starting the register.) |
| 432 | s 386AF(7)(c) a company or foreign company must ensure that its register is kept in the prescribed form and at ... | s 386AF(7)(c) | (c) is kept in such form and at such place as may be prescribed. Time phrases elsewhere: "not later than 30 days after the date of the company’s incorporation" (subsection (1)), which concerns when the register must first be kept; and "within the prescribed time" (subsection (8)). (A duty about form and place has no period; 30/60 days belong to (1) to (6); (8) is a prescribed time.) |
| 502 | s 386AF(9)(a) a company or foreign company must enter or update the particulars of a controller after the cont ... | s 386AF(9)(a) | enter the particulars of any controller in its register, or update the particulars of that controller in the register, after the particulars of that controller are confirmed by the controller. Time phrase elsewhere: "within the prescribed time and in the prescribed manner" (subsection (8)). ('After ... confirmed' is a trigger with no number; subsection (8) says only 'the prescribed time'.) |
| 515 | s 386AF(9)(b) a company or foreign company that does not receive the confirmation must enter or update the par ... | s 386AF(9)(b) | if the company or foreign company does not receive the controller’s confirmation, enter or update the particulars with a note indicating that the particulars have not been confirmed by the controller. Time phrase elsewhere: "within the prescribed time and in the prescribed manner" (subsection (8)). (No number stated; subsection (8) says only 'the prescribed time'.) |
| 797 | s 386AFA(3) a company or foreign company to which the section applies must enter the note and the prescribed p ... | s 386AFA(3) | Where this section applies, the company or foreign company must enter the following in its register of controllers. Time phrase elsewhere: "within the prescribed period after" (subsection (4)). (Subsection (4) gives 'the prescribed period', a period fixed elsewhere, with no number in the Act.) |

### `sgn-registrar.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 237 | s 386AN(2)(a) the Registrar must keep a central register of controllers | s 386AN(2)(a) | the Registrar must keep a central register of controllers consisting of the particulars contained in the registers kept by companies and foreign companies to which this Part applies. The only time phrase, "within the prescribed time" (subsection (3)), is the company's duty to lodge. (No period for the Registrar's duty; (3)'s prescribed time binds the company's lodging, a different person's duty.) |
| 256 | s 386AN(2)(b) the Registrar must require each company or foreign company to lodge the particulars and updates | s 386AN(2)(b) | the Registrar must require any company or foreign company to which this Part applies to lodge with the Registrar. The only time phrase, "within the prescribed time" (subsection (3)), is the company's duty to lodge once required. (No period for the Registrar's requiring; the prescribed time in (3) binds the company, and is not a number.) |
| 408 | s 386ANA(1) the Registrar must keep a central register of nominee directors and a central register of nominee ... | s 386ANA(1) | The Registrar must keep a central register of nominee directors and a central register of nominee shareholders consisting of the particulars contained in the registers kept by companies and foreign companies to which this Part applies. The only time phrase, "within the prescribed time" (subsection (3)), is the company's duty to lodge. (No period for the Registrar's duty; (3)'s prescribed time binds the company, and is not a number.) |

## Where an independent reader asked for a deadline: s 377(2)

`sgg-cessation.l4:174` at commit 1142117325 (line 176 at the commit that restored it, and the table above has the line now), s 377(2), the notice of the appointment of a liquidator.
The text (raw lines 24655-24661) says the authorised representative must, "(a) within 14 days after the commencement of the liquidation or the dissolution; or (b) within such further time as the Registrar in special circumstances allows, lodge or cause to be lodged with the Registrar notice of that fact and, when a liquidator is appointed, notice of such appointment".
The 14 days run from the commencement of the liquidation, and the rule `s 377(2)(a)` already carries them for the notice of that fact.
A liquidator may be appointed later than day 14, so the same clock cannot be met for the notice of the appointment, and the Registrar's further time is an input the module has no place for.
The `LEST` was dropped, not given a `WITHIN 14` (assumed, not ruled); a maintainer who reads (a) as binding the notice of the appointment too would add the `WITHIN` and an input for the further time.

Later the same day (decided by Claude on 2026-11-26, assumed, not ruled) the notice of the appointment of a liquidator was sorted as an ACHIEVEMENT, a thing done once, and given the s 52 input: the rule `s 377(2) an authorised representative must lodge notice of the appointment of a liquidator when one is appointed` carries `WITHIN `the period of all convenient speed, as found`` and its `LEST` again.
The notice of the appointment is read as not governed by the 14 days in (a) or the further time in (b) (assumed, not ruled), which is why it takes the s 52 input; a maintainer who reads (a) as binding it too would replace the input with the 14 days.
The 14 days of s 377(2)(a) run from the commencement of the liquidation or the dissolution, and they stay on their own rule, `s 377(2)(a)`, for the notice of that fact; they are not given to the notice of the appointment, which a liquidator's appointment after day 14 would make impossible to meet.
The further time the Registrar may allow under (b) is still an input the module has no place for.
