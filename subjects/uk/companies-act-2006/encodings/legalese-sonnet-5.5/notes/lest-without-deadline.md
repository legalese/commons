# Dead `LEST` clauses: dropped, or given the deadline the text states (Companies Act 2006 (UK))

Status: decided by Claude on 2026-11-26 (assumed, not ruled); every row below is a proposal for a maintainer to confirm or reverse, and each can be restored from the commit before it.

## What was found and what was done

Running `l4 run` (unstable, a50cbd0) over every module in this folder reported `lint/lest-without-deadline` at 92 places in 35 modules: a `MUST` (or `MAY`) with neither `WITHIN` nor `BEFORE` whose `LEST` can therefore never be reached (the lint's own wording: "time alone never takes it to this LEST").
Each such `LEST` was read against the statute lines its rule cites and against the rest of its section.
A `WITHIN n` was to be added where the text states a period of whole days or weeks for that very duty; otherwise the `LEST` goes.
The result: 87 `LEST` clauses dropped and 5 rules given `WITHIN 14`.
A dropped `LEST` line is replaced by a one-line comment of the same line number, so every `file:line` that cites a later line still holds, and a closing parenthesis that followed the `BECAUSE` string moves to the line above.
Dropping an unreachable `LEST` changes no result: the obligation still waits for its action however long it takes, as before.
The one visible difference is that a `#TRACE` which ends with the obligation still open prints it without the `LEST` it used to carry.

An independent reader read 60 of these 92 sites (all 48 whose section holds any time phrase, and 12 of the others) against the statute text itself, and a scan of the whole section of the other 32 found no number of days or weeks.
It challenged five sites, and all five were accepted: they are the rules given `WITHIN 14` below.

## Rules given `WITHIN 14`

In each, the duty is to give notice to the registrar of the place where a document is kept, the duty's own subsection states no period, and an offence subsection says that default "for 14 days" is an offence.
The rule for s 859Q(3) already reads the same words as a `WITHIN 14`, counted from the day the duty arises (fork F-P2 in `coa19-NOTES.md`), and these five now do too.
The text names no event from which the 14 days run, so `WITHIN 14` counts from when the duty is armed (assumed, not ruled).

| module:line | rule | section | statute words (offence subsection) |
| ----------- | ---- | ------- | ---------------------------------- |
| coa15-ch4.l4:1057 | s 702(5) the company's duty to give notice to the registrar of the place | s 702(5) | s 703(1), raw line 9253: "(1) If default is made in complying with section 702(2), (3) or (4) or default is made for 14 days in complying with section 702(5), or an inspection required under section 702(6) is refused, an offence is committed by—" |
| coa15-ch5.l4:722 | s 720(3) the company's duty to give notice to the registrar of the place | s 720(3) | s 720(5), raw line 9439: "(5) If default is made for 14 days in complying with subsection (3), or an inspection under subsection (4) is refused, an offence is committed by—" |
| coa18-part22-notice.l4:1011 | s 805(5) the company must give notice to the registrar of the place at which the reports are kept | s 805(5) | s 806(1), raw line 10916: "(1) If default is made for 14 days in complying with section 805(5) (notice to registrar of place at which reports made available for inspection) an offence is committed by—" |
| coa18-part22-register.l4:179 | s 809(2) the company must give notice to the registrar of the place where the register is kept | s 809(2) | s 809(4), raw line 10952: "(4) If default is made in complying with subsection (1), or a company makes default for 14 days in complying with subsection (2), an offence is committed by—" |
| coa3-part8-inspection.l4:74 | s 114(2) the company must give notice to the registrar of the place (duty) | s 114(2) | s 114(5), raw line 1543: "(5) If a company makes default for 14 days in complying with subsection (2), an offence is committed by—" |

The `#TRACE` directives of these five rules were run on both builds after the change.
Four are unchanged (notice on day 1, 2 or 3 reads `FULFILLED`).
`coa15-tests-ch4.l4` had two traces for s 702(5), a notice on day 20 and a wait to day 40, expected `FULFILLED` and `RESIDUAL` because the duty had no period; they now read `BREACH` and `BREACH`, so that file has three: a notice on day 10 (`FULFILLED`), on day 20 (`BREACH`) and none by day 40 (`BREACH`).

## Dropped

Each row gives the module and the line the `LEST` was on, the rule, the section, and the statute words the decision rests on (copied from the text, with `/` for a line break in the quotation); "other time phrase" is a period the section states elsewhere, with the reason it is not this duty's.

### `coa1-part2-formation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 102 | s 8(2) the subscriber's duty | s 8(2) | The memorandum must be in the prescribed form and must be authenticated by each subscriber. (No period in the cited text or anywhere in s 8.) |
| 855 | s 14 the registrar's duty | s 14 | If the registrar is satisfied that the requirements of this Act as to registration are complied with, he shall register the documents delivered to him. (No period stated; s 14 is a single sentence.) |

### `coa1-part3-constitution.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 77 | s 18(2) the company's duty to register articles | s 18(2) | Unless it is a company to which model articles apply by virtue of section 20 (default application of model articles in case of limited company), it must register articles of association. (No period stated anywhere in s 18.) |
| 295 | s 23(1) the company's duty to give notice of the restriction | s 23(1) | the company must give notice of that fact to the registrar (No period stated anywhere in s 23.) |
| 325 | s 23(2) the company's duty to give notice of the removal | s 23(2) | the company must give notice of that fact to the registrar (No period stated anywhere in s 23.) |
| 375 | s 24(2) the company's duty to deliver a statement of compliance | s 24(2) | the company must deliver with that document a statement of compliance (Non-numeric standard: 'with that document' (simultaneity); no number of days in s 24.) |
| 827 | s 31(2) the company's duty to give notice, and the registrar's duty to register it | s 31(2) | on receipt of the notice, the registrar shall register it (Non-numeric standard 'on receipt'; no period in s 31. This is the inner Registrar LEST, whose closing parenthesis ends the HENCE group: keep the ')' when deleting.) |
| 828 | s 31(2) the company's duty to give notice, and the registrar's duty to register it | s 31(2) | it must give notice to the registrar (No period for the company's notice; (2)(c) 'not effective until entry of that notice on the register' is a consequence, not a deadline.) |
| 938 | s 32(1) the company's duty | s 32(1) | A company must, on request by any member, send to him the following documents (No period; (3) 'If a company makes default in complying with this section' gives no number of days.) |
| 1294 | s 36(1) the company's duty on each copy issued | s 36(1) | Every copy of a company's articles issued by the company must be accompanied by (No period; (4) 'for each occasion on which copies are issued' is a fine unit, not a deadline.) |

### `coa1-part4-capacity.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 580 | s 45(2) the company's duty to engrave its name on its common seal | s 45(2) | A company which has a common seal shall have its name engraved in legible characters on the seal. (No period stated anywhere in s 45.) |
| 833 | s 49(6) the duty of the person affixing the official seal | s 49(6) | The person affixing the official seal must certify in writing on the deed or other document to which the seal is affixed the date on which, and place at which, it is affixed. (No period stated anywhere in s 49.) |

### `coa10-revision.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 338 | s 456(7) the applicant's duty to inform the registrar | s 456(7) | the applicant must send to the registrar for registration a copy of the court order ('On the conclusion of proceedings on an application under this section' is a trigger event, not a number of days. This LEST ends its WHEN branch; the OTHERWISE branch follows.) |
| 343 | s 456(7) the applicant's duty to inform the registrar | s 456(7) | give notice to the registrar that the application has failed or been withdrawn ('On the conclusion of proceedings on an application under this section' is a trigger event, not a number of days.) |

### `coa13-regulative.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 86 | s 578(2) the duty to repay the money received from applicants | s 578(2) | If any of the money is not repaid within 48 days after the first making of the offer, the directors of the company are jointly and severally liable to repay it, with interest at the rate for the time being specified under section 17 of the Judgments Act 1838 (c. 110) from the expiration of the 48th day. (The 48 days of s 578(3) are the time for the company's repayment (the rule's own WITHIN 48); the directors' liability to repay with interest states no period, so that step has no deadline.) |

### `coa15-ch1.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 751 | s 665(2) the registrar must issue a certificate of incorporation | s 665(2) | The registrar must issue a certificate of incorporation altered to meet the circumstances of the case. (No period stated anywhere in s 665.) |
| 978 | s 669(1) the company must transfer an amount to a reserve fund | s 669(1) | an amount equal to the value of the shares must be transferred out of profits available for dividend to a reserve fund and is not then available for distribution (No period stated anywhere in s 669.) |

### `coa15-ch3.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 178 | s 686(3) the company must pay for the shares on redemption | s 686(3) | the shares must be paid for on redemption (Non-numeric standard 'on redemption'; (2) allows a later date by agreement, no number of days.) |

### `coa15-ch4.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 90 | s 691(2) the company must pay for the shares on purchase | s 691(2) | the shares must be paid for on purchase (Non-numeric standard 'on purchase'; no period in s 691.) |
| 611 | s 696(2) the company must make the copy or memorandum available to members | s 696(2) | must be made available to members / at the company's registered office for not less than 15 days ending with the date of the meeting  |
| 987 | s 702(2) the company must keep the copy or memorandum available for inspection | s 702(2) | The company must keep available for inspection / until the end of the period of ten years beginning with (Ten years is a retention period in years (subsection (3)), not a deadline for this duty; no period in days.) |

### `coa15-ch5.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 354 | s 714(1) the directors must make a statement | s 714(1) | The company's directors must make a statement in accordance with this section. (No period stated anywhere in s 714.) |
| 934 | s 720B(3) the registrar must register the documents | s 720B(3) | The registrar must register the documents delivered to him under subsection (1) on receipt. / Within 15 days after the passing of the resolution (Non-numeric standard 'on receipt'; the 15 days in (1) is the company's delivery duty, a different person and subsection.) |
| 1157 | s 721(4) the court must make an order cancelling or confirming the resolution | s 721(4) | the court must make an order either cancelling or confirming the resolution / must be made within five weeks after the passing of the resolution (The five weeks in (2) is the time for the member or creditor to apply; the text gives the court no period.) |

### `coa15-ch6.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 68 | s 724(4) the company must be entered in its register of members | s 724(4) | Where shares are held by the company, the company must be entered in its register of members ... as the member holding the shares. (No period stated anywhere in s 724.) |

### `coa15-ch7.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 28 | s 733(1) the company must transfer the amount to the capital redemption reserve | s 733(1) | In the following circumstances a company must transfer amounts to a reserve (No period stated anywhere in s 733.) |

### `coa16-part19-register.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 391 | s 745(1) the company must comply with the request or apply to the court | s 745(1) | If it applies to the court it must notify the person making the request. / it must within five working days either (Subsection (2) states no period for the notification; the five working days in (1) is in working days and governs comply-or-apply. This is the inner notify LEST, whose closing parenthesis ends the HENCE group: keep the ')' when deleting.) |

### `coa16-part20-minimum-capital.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 464 | s 767(3) the company must comply with its obligations, failing which the directors must indemnify | s 767(3) | the directors of the company are jointly and severally liable to indemnify any other party to the transaction / fails to comply with its obligations in connection with the transaction within 21 days from being called on to do so (The 21 days are the time for the company's performance (the rule's own WITHIN 21); the directors' liability to indemnify states no period, so that step has no deadline.) |

### `coa18-part22-notice.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 865 | s 804(1) the company that is required under section 803 must exercise its powers in the manner specified | s 804(1) | must exercise those powers in the manner specified in the requests (No period stated; (2) 'If default is made in complying with subsection (1)' gives no number of days.) |

### `coa18-part22-register.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 33 | s 808(1) the company must keep a register of the information received | s 808(1) | "The company must keep a register of information received by it in pursuance of a requirement imposed under section 793"; time phrase elsewhere: "within three days of the receipt, enter in the register" (subsection (2), the duty to enter the information, not the duty to keep the register); subsection (5) says only "If default is made in complying with this section" (No period for keeping the register; the three days in (2) belong to the separate entering duty.) |
| 233 | s 810(1) the company must keep an index of the names entered in the register | s 810(1) | "the company must keep an index of the names entered in it"; time phrase elsewhere: "within ten days after the date on which any entry or alteration is made in the register" (subsection (2), the duty to make entries or alterations in the index, not the duty to keep an index); subsection (5) says only "If default is made in complying with this section" (No period for keeping the index; the ten days in (2) belong to the separate duty to update it.) |
| 589 | s 815(2) the company must restore an entry deleted in contravention of subsection (1) | s 815(2) | "the company must restore it as soon as reasonably practicable" (Non-numeric standard: as soon as reasonably practicable; no number of days anywhere in the section.) |

### `coa18-part24.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 198 | s 853BA the company must deliver a statement that its intended future activities are lawful | s 853BA | "it must at the same time deliver to the registrar a statement that the intended future activities of the company are lawful" (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 244 | s 853C(2) the company must give notice to the registrar of the change in its principal business activities | s 853C(2) | "The company must give notice to the registrar of the change at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 286 | s 853CA(2) the company must deliver a notice under section 87 with the confirmation statement | s 853CA(2) | "The company must deliver a notice under section 87 at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 319 | s 853CB(2) the company must deliver a notice under section 88B with the confirmation statement | s 853CB(2) | "The company must deliver a notice under section 88B at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 352 | s 853D(2) the company must deliver a statement of capital with the confirmation statement | s 853D(2) | "The company must deliver a statement of capital to the registrar at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 468 | s 853E(2) the company must deliver a statement of the trading status of its shares with the confirmation state ... | s 853E(2) | "The company must deliver to the registrar a statement dealing with the matters mentioned in subsection (4) at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 512 | s 853F(3) the non-traded company must deliver the shareholder information with the confirmation statement | s 853F(3) | "The company must deliver the information falling within subsection (5) to the registrar at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |
| 588 | s 853G(4) the traded company must deliver the shareholder information with the confirmation statement | s 853G(4) | "The company must deliver the information falling within subsection (6) to the registrar at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; the 5% in (6)(a) is a shareholding threshold, not a period.) |
| 646 | s 853H(2) the company must deliver a statement of the fact that Part 21A does not apply to it with the confirm ... | s 853H(2) | "The company must deliver to the registrar a statement of the fact that it is a company to which Part 21A does not apply at the same time as it delivers the confirmation statement." (Non-numeric standard: at the same time as the confirmation statement; no number of days.) |

### `coa19-regulative.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 49 | s 859K(3)(a) the person must, on ceasing to act, give notice to the registrar | s 859K(3)(a) | "the person must, on so ceasing— (a) give notice to the registrar of that fact"; time phrase elsewhere: "within 7 days of the order or of the appointment under those powers" (subsection (2), the duty on obtaining the order or making the appointment, not on ceasing to act)  |

### `coa22-part31-ch1.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1530 | s 1009(2) the director's duty to secure that the company's application is withdrawn | s 1009(2) | "must secure that the company's application is withdrawn forthwith" (Non-numeric standard: forthwith.) |

### `coa22-part31-ch3.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 1611 | s 1033(5)(c) the company's duty to give notice to the registrar | s 1033(5)(c) | "(c) the company must give notice to the registrar of the change"; time phrase elsewhere: "(a) the company must change its name within 14 days after the date of the restoration" (the duty to change the name, a different duty from giving notice); subsection (6) says only "If the company fails to comply with subsection (5)(a) or (c)" (The 14 days attach to paragraph (a), changing the name, not to the notice in (c); no period stated for (c).) |

### `coa25-names-ch1.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 339 | s 1195(2) the applicant must request the view of the department or body and submit a statement | s 1195(2) | "(3) He must submit to the Secretary of State a statement that such a request has been made and a copy of any response received from the specified body." (This is the INNER LEST (s 1195(3) breach, inside the HENCE of the outer MUST); no period anywhere in s 1195. The outer LEST is the separate site at :341.) |
| 341 | s 1195(2) the applicant must request the view of the department or body and submit a statement | s 1195(2) | "(2) Where such a requirement applies, the applicant must request the specified department or other body (in writing) to indicate whether (and if so why) it has any objections to the proposed name." (This is the OUTER LEST (s 1195(2) breach, last line of the rule); no period anywhere in s 1195. The inner LEST is the separate site at :339.) |

### `coa25-names-ch2.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 465 | s 1202(1) the person must state the information on the document | s 1202(1) | "A person to whom this Chapter applies must state the information required by this Chapter, in legible characters, on all— (a) business letters"; time phrase elsewhere: "immediately given, by written notice" (subsection (2), the separate duty to give information to a person who asks) (No period for the duty to state the information on documents; 'immediately' in (2) belongs to a different duty and is non-numeric anyway.) |
| 474 | s 1202(2) the person must give the information to a person who asks | s 1202(2) | "must secure that the information required by this Chapter is immediately given, by written notice, to any person with whom anything is done or discussed in the course of the business and who asks for that information" (Non-numeric standard: immediately; no number of days.) |
| 487 | s 1204(1) the person must display the notice in the premises | s 1204(1) | "must, in any premises— (a) where the business is carried on, and (b) to which customers of the business or suppliers of goods or services to the business have access, display in a prominent position" (No time phrase anywhere in the section; the duty is a continuing display obligation with no period.) |

### `coa25-notices-courts.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 130 | s 1154(1) the person specified in subsection (2) must give the registrar notice of the appointment | s 1154(1) | "Notice must be given to the registrar of the appointment in relation to a company of— (a) a judicial factor (in Scotland)"  |

### `coa25-records.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 349 | s 1135(2) the company must keep electronic records capable of reproduction in hard copy form | s 1135(2) | "Where the records are kept in electronic form, they must be capable of being reproduced in hard copy form." (A standing capability requirement, not an act with a time limit; no period in the section.) |
| 361 | s 1138(1) the company must take adequate precautions against falsification | s 1138(1) | "Where company records are kept otherwise than in bound books, adequate precautions must be taken— (a) to guard against falsification, and (b) to facilitate the discovery of falsification." (A standing duty of care, not an act with a time limit; no period in the section.) |

### `coa25-service.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 166 | s 1139(4) the person issuing out the process must send a copy to the registered office | s 1139(4) | "Where process is served on a company under this subsection, the person issuing out the process must send a copy of it by post to the company's registered office." (No period in the subsection or elsewhere in the section.) |

### `coa25-valuation.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 148 | s 1150(4) the valuer must state in the report what is required | s 1150(4) | "Where the consideration or part of it is valued by a person other than the valuer himself, the latter's report must state that fact and shall also— (a) state the former's name" (No period anywhere in s 1150.) |

### `coa29-sch2-part3.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 72 | sch 2 part 3 para 2 the Panel must have regard to the considerations before disclosing to an overseas body | sch 2 part 3 para 2 | "In determining whether to disclose information to a person or body in accordance with this Part of this Schedule, the Panel must have regard to the following considerations" (A duty to have regard when deciding; no period in the paragraph.) |

### `coa29-sch5.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 629 | sch 5 para 12(1) the company must make the document or information available so that the recipient can read it ... | sch 5 para 12(1) | "must be made available in a form, and by a means, that the company reasonably considers will enable the recipient— (a) to read it, and (b) to retain a copy of it." (A standard of form, not an act with a time limit; the 28 days in para 14 concerns a different duty.) |
| 642 | sch 5 para 13(1) the company must notify the intended recipient of the document or information on the website | sch 5 para 13(1) | "The company must notify the intended recipient of— (a) the presence of the document or information on the website"; time phrase elsewhere: "the period of 28 days beginning with the date on which the notification required under paragraph 13 is sent" (paragraph 14, how long the document stays on the website, counted from this notice, not a time to give it) (No period for giving the notification; the 28 days in para 14(1)(b) run after it and belong to the availability duty.) |
| 653 | sch 5 para 14(1) the company must keep the document or information available on the website throughout the per ... | sch 5 para 14(1) | "The company must make the document or information available on the website throughout— (a) the period specified by any applicable provision of the Companies Acts, or (b) if no such period is specified, the period of 28 days beginning with the date on which the notification required under paragraph 13 is sent to the person in question."  |

### `coa3-part8-inspection.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 494 | s 120(1) the company must inform the person of the most recent date of alteration (duty) | s 120(1) | "When a person inspects the register, or the company provides him with a copy of the register or any part of it, the company must inform him of the most recent date (if any) on which alterations were made to the register" (The duty is triggered by an inspection or copy request and states no period; no time phrase in the section.) |

### `coa3-part8-members.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 143 | s 113(1) the company must keep a register of its members (duty) | s 113(1) | (1) Every company must keep a register of its members. // a daily default fine not exceeding one-tenth of level 3 on the standard scale (No period for the duty; the daily default fine in (8) is a penalty rate for continued contravention, not a deadline.) |

### `coa3-part9-rights.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 511 | s 149(2) the company must accompany the copy of the notice with the statement (duty) | s 149(2) | (2) The copy of the notice must be accompanied by a statement that— (No period anywhere in the section; the accompaniment is simultaneous with sending the copy, with no number of days.) |
| 685 | s 152(2) the member must inform the company to what extent he is exercising the rights (duty) | s 152(2) | (2) A member who exercises such rights but does not exercise all his rights, must inform the company to what extent he is exercising the rights. (No period stated in the section; (4) only gives the company a presumption if the member does not inform it.) |
| 705 | s 152(3) the member must inform the company of the ways in which he is exercising the rights (duty) | s 152(3) | (3) A member who exercises such rights in different ways must inform the company of the ways in which he is exercising them and to what extent they are exercised in each way. (No period stated in the section.) |
| 836 | s 153(2) the company must act under the section on a request that meets the conditions (duty) | s 153(2) | (2) A company is required to act under any of those sections if it receives a request in relation to which the following conditions are met— // (g) the request complies with any other requirements of the section in question as to contents, timing and otherwise. (No period for the company's duty to act; 'timing' in (g) refers to the requirements of the other sections (314, 338, 338A, 342, 527), with no number here; 100 persons and 100 pounds are not periods.) |

### `coa30-regulative.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 57 | sch 10 para 2(4) the notice of refusal | sch 10 para 2(4) | (4) Where the Secretary of State refuses an application for a recognition order he must give the applicant a written notice to that effect— // the period of three months beginning with the date on which the revocation order is made (No period for the refusal notice. The three-month phrases are in para 3(2) and 3(5), different duties (effective date of a revocation order; representations by affected persons), and are months anyway.) |
| 68 | sch 10 para 3(3) the duties before revoking | sch 10 para 3(3) | (3) Before revoking a recognition order the Secretary of State must— (a) give written notice of his intention to do so to the recognised body, // within the period of three months beginning with the date of service or publication of the notice under sub-paragraph (3) (Operand (a) of a three-way RAND, each operand a self-contained PARTY..MUST..HENCE..LEST. 'Before revoking' is an anchor with no number; the three-month phrase in para 3(5) is the recipient's time to make representations (different person, and months).) |
| 73 | sch 10 para 3(3) the duties before revoking | sch 10 para 3(3) | (b) take such steps as he considers reasonably practicable for bringing the notice to the attention of the members of the body, // Before revoking a recognition order the Secretary of State must— (Operand (b) of the RAND. 'Before revoking' is an anchor with no number; 'reasonably practicable' is a non-numeric standard; para 3(5)'s three months belongs to the recipients' representations.) |
| 78 | sch 10 para 3(3) the duties before revoking | sch 10 para 3(3) | (c) publish the notice in such manner as he thinks appropriate for bringing it to the attention of any other persons who are in his opinion likely to be affected. // Before revoking a recognition order the Secretary of State must— (Operand (c), the last of the RAND. 'Before revoking' is an anchor with no number; no period is stated for publication; para 3(5)'s three months belongs to the recipients.) |
| 97 | sch 10 para 3(11) the duties on making the order | sch 10 para 3(11) | (11) On making an order revoking a recognition order in respect of a body the Secretary of State must— (a) give written notice of the making of the order to the body, (Operand (a) of a three-way RAND. 'On making' is an anchor with no number; the three-month phrases elsewhere in para 3 concern the effective date and representations, not this notice.) |
| 102 | sch 10 para 3(11) the duties on making the order | sch 10 para 3(11) | (b) take such steps as he considers reasonably practicable for bringing the making of the order to the attention of the members of the body, // On making an order revoking a recognition order in respect of a body the Secretary of State must— (Operand (b) of the RAND. 'On making' is an anchor with no number; 'reasonably practicable' is a non-numeric standard.) |
| 107 | sch 10 para 3(11) the duties on making the order | sch 10 para 3(11) | (c) publish a notice of the making of the order in such manner as he thinks appropriate for bringing it to the attention of any other persons who are in his opinion likely to be affected. // On making an order revoking a recognition order in respect of a body the Secretary of State must— (Operand (c), the last of the RAND. 'On making' is an anchor with no number; no period is stated for publication.) |
| 130 | sch 10 para 20ZA the duty to pay the costs | sch 10 para 20ZA | (2) B must pay the costs incurred by— (No period for payment of the costs anywhere in para 20ZA.) |
| 141 | sch 12 para 4 the duty to pay the costs | sch 12 para 4 | 4 (1) The registered third country auditor must pay any of the costs of maintaining any relevant arrangements which the arrangements provide are to be paid by it. (No period; when payment is due is left to the arrangements, which the statute does not set out.) |
| 160 | sch 13 para 9(3) the duty to endorse a copy | sch 13 para 9(3) | (3) Any person wishing in any legal proceedings to cite an instrument made by the body may require the body to cause a copy of it to be endorsed with such a certificate as is mentioned in this paragraph. (No period for endorsing the copy. The only time phrase nearby is para 10(1), 'at least once in each calendar year', which is the body's separate reporting duty.) |
| 179 | sch 13 para 10(3) the duty to lay the report | sch 13 para 10(3) | (3) The Secretary of State must lay before Parliament copies of each report received by him under this paragraph. // at least once in each calendar year for which the delegation order is in force (No period for laying the reports; the calendar-year phrase in 10(1) is the body's duty to make a report to the Secretary of State, a different person's duty.) |

### `coa5-derivative-claims.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 136 | s 261(1) the member's duty to apply for permission to continue the claim | s 261(1) | (1) A member of a company who brings a derivative claim under this Chapter must apply to the court for permission (in Northern Ireland, leave) to continue it. (No period anywhere in s 261.) |
| 717 | s 266(4)(a) the applicant's duty to serve the application on the company | s 266(4)(a) | (4) If the application is not refused under subsection (3)— (a) the applicant must serve the application on the company, (No period anywhere in s 266; the anchor is only the court's not refusing the application under (3).) |

### `coa5-director-supplementary.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 122 | s 248(1) the company's duty to cause minutes to be recorded | s 248(1) | (1) Every company must cause minutes of all proceedings at meetings of its directors to be recorded. // (2) The records must be kept for at least ten years from the date of the meeting. (No period for recording the minutes. The ten years in (2) is a retention period (years) for the separate duty to keep the records, not a deadline for (1).) |

### `coa5-service-contracts.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 368 | s 231(2) the company's duty to ensure the terms are set out or recorded | s 231(2) | (2) The company must, unless the contract is in writing, ensure that the terms of the contract are either— // recorded in the minutes of the first meeting of the directors of the company following the making of the contract. (Anchored to the first directors' meeting after the contract, which is an event, not a number of days; no period stated.) |

### `coa8-regulative.l4`

| line | rule | section | statute words and reason |
| ---- | ---- | ------- | ------------------------ |
| 49 | s 369(2) the director in default shall make good and compensate | s 369(2) | (a) to make good to the company the amount of the unauthorised donation or expenditure, with interest, // in respect of the period beginning with the date when the donation was made or the expenditure was incurred (Operand (a) of a two-way RAND. The 'period' in (5) is the interest accrual period, not a deadline for making good.) |
| 53 | s 369(2) the director in default shall make good and compensate | s 369(2) | (b) to compensate the company for any loss or damage sustained by it as a result of the unauthorised donation or expenditure having been made. (Operand (b), the last of the RAND. No period stated for compensating.) |
| 121 | s 373(1) the company shall provide the group with the information | s 373(1) | (1) Where proceedings have been brought under section 370 in the name of a company by an authorised group, the group is entitled to require the company to provide it with all information relating to the subject matter of the proceedings (No period for providing the information; (2) only lets the court order it if the company refuses.) |
| 137 | s 386(1) the company shall keep adequate accounting records | s 386(1) | (1) Every company must keep adequate accounting records. (Continuing duty with no period in s 386.) |
| 171 | s 394 the directors shall prepare individual accounts for the financial year | s 394 | The directors of every company must prepare accounts for the company for each of its financial years unless the company is exempt from that requirement under section 394A. (No period in s 394; the filing period belongs to other sections not shown.) |
| 185 | s 414A(1) the directors shall prepare a strategic report for the financial year | s 414A(1) | (1) The directors of a company must prepare a strategic report for each financial year of the company. // immediately before the end of the period for filing accounts and reports for the financial year in question (No period for preparing. The phrase in (5) names an unnumbered filing period as the time an offender must have been a director, and the period itself is set elsewhere.) |
| 204 | s 412(5) the director shall give notice to the company | s 412(5) | to give notice to the company of such matters relating to himself as may be necessary for the purposes of regulations under this section. // any person who is or has at any time in the preceding five years been a director of the company (No period for giving the notice. 'preceding five years' (years) fixes who owes the duty, not when to perform it; (6) makes default an offence with no number of days.) |
| 220 | s 414(1) a director shall sign the annual accounts on behalf of the board | s 414(1) | (1) A company's annual accounts must be approved by the board of directors and signed on behalf of the board by a director of the company. (No period in s 414.) |
