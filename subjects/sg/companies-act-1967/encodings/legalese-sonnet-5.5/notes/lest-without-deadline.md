# Dead `LEST` clauses: dropped, or given the deadline the text states (Companies Act 1967 (Singapore, 2020 Revised Edition))

Status: decided by Claude on 2026-11-26 (assumed, not ruled); every row below is a proposal for a maintainer to confirm or reverse, and each can be restored from the commit before it.

## What was found and what was done

Running `l4 run` (unstable, a50cbd0) over every module in this folder reported `lint/lest-without-deadline` at 205 places in 67 modules: a `MUST` (or `MAY`) with neither `WITHIN` nor `BEFORE` whose `LEST` can therefore never be reached (the lint's own wording: "time alone never takes it to this LEST").
Each such `LEST` was read against the statute lines its rule cites and against the rest of its section.
A `WITHIN n` was to be added where the text states a period of whole days or weeks for that very duty; otherwise the `LEST` goes.
The result: all 205 `LEST` clauses dropped; no duty carries a period of days or weeks in the text (one, s 377(2), names 14 days that cannot run for it: see the last section).
A dropped `LEST` line is replaced by a one-line comment of the same line number, so every `file:line` that cites a later line still holds, and a closing parenthesis that followed the `BECAUSE` string moves to the line above.
Dropping an unreachable `LEST` changes no result: the obligation still waits for its action however long it takes, as before.
The one visible difference is that a `#TRACE` which ends with the obligation still open prints it without the `LEST` it used to carry.

An independent reader read 181 of these 205 sites (all 168 whose section holds any time phrase, and 13 of the others) against the statute text itself, and a scan of the whole section of the other 24 found no number of days or weeks.
It challenged one site, s 377(2); that was not accepted, and the last section says why.

## Each dropped clause is kept in its comment

Each of the 205 comments begins `-- no LEST:`, so `grep -rn -e '-- no LEST:' .` in this folder finds every site without the git history.
The comment says that the section states no time for the duty, so that a breach needs a standard of time from outside the section, and it names the general one: the Interpretation Act 1965 s 52, under which a thing for which no time is prescribed "is to be done with all convenient speed".
It then carries the dropped `LEST` clause word for word (`dropped clause: LEST BREACH BY … BECAUSE "…"`), copied from the commit before the drop and checked against it byte for byte; for the 7 clauses whose closing parenthesis moved to the line above, the comment carries the clause without it.
Not every site wants that standard: a duty that must hold throughout ("keep a register", "act honestly at all times") is broken at any moment it stops holding, not when a period runs out, and L4 has no form for such a duty yet.
Sorting the 205 into duties to do a thing once, which can take a `WITHIN` whose length is found under s 52, and duties that must hold throughout, which stay as they are, is a later pass (decided by Claude on 2026-11-26, assumed, not ruled).

## Dropped

Each row gives the module and the line the `LEST` was on, the rule, the section, and the statute words the decision rests on (copied from the text, with `/` for a line break in the quotation); "other time phrase" is a period the section states elsewhere, with the reason it is not this duty's.

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

## Where an independent reader asked for a deadline and the drop stands

`sgg-cessation.l4:174`, s 377(2), the notice of the appointment of a liquidator.
The text (raw lines 24655-24661) says the authorised representative must, "(a) within 14 days after the commencement of the liquidation or the dissolution; or (b) within such further time as the Registrar in special circumstances allows, lodge or cause to be lodged with the Registrar notice of that fact and, when a liquidator is appointed, notice of such appointment".
The 14 days run from the commencement of the liquidation, and the rule `s 377(2)(a)` already carries them for the notice of that fact.
A liquidator may be appointed later than day 14, so the same clock cannot be met for the notice of the appointment, and the Registrar's further time is an input the module has no place for.
The `LEST` was dropped, not given a `WITHIN 14` (assumed, not ruled); a maintainer who reads (a) as binding the notice of the appointment too would add the `WITHIN` and an input for the further time.
