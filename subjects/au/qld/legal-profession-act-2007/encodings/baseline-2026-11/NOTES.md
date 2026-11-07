# Legal Profession Act 2007 (Qld), Part 3.4: baseline encoding for the client (costs agreements)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is **costs agreements**: when a costs agreement with a law practice is valid, when it is void and what the law practice may then recover, conditional ("no win, no fee") agreements, uplift fees and their cap, contingency fees, cooling-off and setting aside. Around them are the rules a client meets on the way: whether Part 3.4 applies, what must be disclosed and what follows a failure to disclose, reports, interest, bills, when the law practice may sue, and costs assessment.

It is written in layers:

- **`lpa-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the client", "the law practice", "the costs assessor", "the Supreme Court or the tribunal"). Each rule is preceded by the words of the section it encodes. Two regulative rules (`DEONTIC`): the s 332(2) duty to give an itemised bill within 28 days after the request (MUST), and the s 329(1) / s 332(4) bar on starting recovery proceedings until 30 days after the bill (SHANT).
- **`lpa-dates.l4`**, small date helpers on the stable prelude's date primitives. The `daydate` library is not imported and no `YMD` is defined. The date readings are stated at its top.
- **`lpa-seat.l4`**, the client's seat: 16 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a retainer runs. It builds the core's inputs from plain answers and restates no rule. Inputs with the same meaning carry the same name in every question.
- **`lpa-cases-client.l4`**, the cases.

No earlier encoding of this Act existed. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Legal Profession Act 2007** (Qld) (act-2007-024), in force from 1 July 2025, the current version on the retrieval date, as deposited at `../../registers/source-bundle/act-2007-024.txt` (retrieved 2026-11-06, unofficial HTML conversion).

Not deposited, and so taken from the Act's own fallback or asked as facts:

- the **Legal Profession Regulation** (2017 or its successor): the s 300 "disclosure threshold amount" and "detailed disclosure threshold amount" are the Act's fallback figures ($1,500 and $3,000), which apply "if no amount is prescribed". A prescribed amount would change the disclosure answers. The maximum rate of interest on unpaid costs (s 321(3)) is an input. Circumstances prescribed under s 311(1)(f) are not encoded.
- the **Uniform Civil Procedure Rules 1999** (deposited beside this Act, not read here): the way a costs application is made (s 335(10)) and the late-application decision under s 335(6), which is answered conditionally.

## Checks

| Module | Run | Result |
|---|---|---|
| `lpa-dates.l4` | `l4 run` | 0 errors, 0 warnings |
| `lpa-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `lpa-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `lpa-cases-client.l4` | `l4 run` | 0 errors, 0 warnings; **104 assertions written, 104 satisfied** |

In addition, 2 `#TRACE`s carry an `-- expect:` line (proceedings started on day 29 after the bill; the itemised bill given on day 29 after the request), each ending in the breach expected. Both were read and match.
`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07). Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seat

**The client**: the person to whom or for whom a law practice provides legal services (s 328(10), s 334), for example a person who retains a law practice to bring a personal injury or compensation claim. They ask:

- "Does Queensland's costs law apply to my matter?"
- "What must my lawyer tell me about costs? Must it explain an uplift fee in writing before I sign? It did not tell me: need I pay?"
- "Can I get a report on my matter or my costs, and must I pay for it?"
- "Is my costs agreement void, which rules does it break, and what can the law practice still recover?"
- "What is the most uplift fee I can be charged? Can I still cool off? Can I have the agreement set aside?"
- "When can my lawyer sue me for the bill? By when must I get my itemised bill? Can it charge me interest?"
- "By when must I apply for a costs assessment? Will the assessor go by my agreement? Who pays for the assessment?"

There is **no second seat**. The law practice is the party the text puts duties on, and a seat for it is welcome later as `lpa-seat-law-practice.l4` over the same core. An associated third party payer (for example an insurer or employer that has agreed to pay the law practice) is treated in the core only where s 322(6) makes it a client for s 328; a payer seat is also possible. The costs assessor, the court, QCAT, the law society and the commissioner are not seats; their decisions appear as conditional answers or as facts the client states.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** The regulation is not deposited; the Act's fallback amounts are used and the interest cap is an input (above).
- **The actors the text names:** the client, the law practice (including a law practice it retains, such as a barrister), the associated third party payer, the costs assessor, the Supreme Court or the tribunal (QCAT).
- **Judgments left to others are answered conditionally, as inputs:** a principal's decision "on reasonable grounds" (s 311(1)(b)); whether the costs agreement is "not fair or reasonable" (s 328); the costs assessor being "satisfied" (ss 340(1)(c)-(e), 342(2)(b)); whether to deal with a late costs application (s 335(6)); whether a matter is "likely" to involve proceedings (litigious matter) and the "likely" total of legal costs.
- **The Act's own definitions are worked out from facts:** sophisticated client (s 300 with s 311(1)(c)-(d)); conditional costs agreement and uplift fee (s 300); the application of Part 3.4 (ss 302-304). Borrowed terms are asked as facts: the s 311(1)(c) kinds of client (Corporations Act terms), a scale of costs, business days.
- **One case:** one client, one law practice, one matter and its costs agreement.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (below).

## Scope

**In** (Part 3.4):

- Division 1: s 300 (definitions: costs agreement, conditional costs agreement, uplift fee, sophisticated client, the two threshold amounts, litigious matter).
- Division 2: ss 302-304 (application by first instructions, by agreement or notice, displacement; s 304(3) re-application not encoded).
- Division 3: s 307A, s 307B(1), s 308(1)-(2), s 311(1)(b)-(e) (which disclosure, and the exceptions); s 313 (uplift fee disclosure); s 316(1)-(2), (4)-(5) (effect of failure to disclose); s 317 (progress and costs reports).
- Division 4: s 321 (interest).
- Division 5 (the focus): s 322(1)-(5) (form, offer route, no exclusion of assessment), s 323 (conditional costs agreements, cooling-off and its effect), s 324 (uplift fees, the 25% cap and discounts), s 325 (contingency fees, transfer of interest), s 326 (enforcement), s 327 (void agreements and what may be recovered or must be repaid), s 328(1), (4)-(6), (10) (setting aside).
- Division 6: s 329(1), (3) (no proceedings until 30 days after the bill; a regulative rule), s 332(1)-(2), (4)-(6) (itemised bill on request, within 28 days, free; a regulative rule).
- Division 7: s 335(1), (5)-(6) (the client's costs application and its 12 months), s 338 (no recovery proceedings while an assessment is under way), s 340 (assessment by the agreement), s 342(2)-(3) (costs of the assessment), s 344 (contracting out by a sophisticated client, as it bears on s 322(5)).

**Out, and why:**

- **Division 8, s 347 (the cap on claim-related costs for a speculative personal injury claim).** The cap is a formula printed as an image, which the deposited text does not convert (`[Formula image not converted: ...]`). The encoder has not seen the formula and does not guess it. See finding 1.
- s 299 (purposes), s 301 (third party payer definitions, beyond s 322(6)), ss 305-307 (where instructions are given, the substantial-connection regulation, costs under two laws): definitions or rules for a later pass.
- The content of a disclosure (ss 307B(2), 308(4)-(8)), s 309 (disclosure where another law practice is retained), ss 310-310A (when and how disclosure is made: "as soon as practicable", no day to compute), s 311(3)-(5), s 312 (settlement disclosure), ss 314-315 (form; ongoing disclosure), s 316(3), (6)-(7), s 318 (associated third party payers): duties of the law practice without a date or amount to compute, or a payer's case.
- ss 319-320 (basis of recovery, security for costs): s 319 appears only as the s 327(2) fallback (scale, else fair and reasonable value).
- s 322(6) beyond s 328, s 323(4)(a) (agreements between law practices), s 328(2)-(3), (7)-(9A) (what the court may weigh, adjournment, costs of the hearing): the court's matters.
- ss 329(2), 330-331, 333 (court order to sue sooner; the form, signing and service of bills; the statement of rights; interim bills): the bill is taken as properly given.
- ss 334, 335(2)-(4), (7)-(11), 336-337, 339, 341, 343 (third party payers' and law practices' applications, notice of an application, the assessment criteria, referral for discipline): the assessor's and the law practices' matters; s 341 is named in an answer only.
- Division 9 (application to incorporated legal practices; imputed knowledge): machinery.
- The rest of the Act (admission, practising certificates, trust money, insurance, the fidelity fund, complaints and discipline): outside the focus.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

Most questions answer with a constructor whose words say what the Act does, not a bare yes or no. Where they say no, the text does: an unmet "if" (ss 302-303, 313(1), 316(1), 321(1)(b), 324(4) for the cap's existence), a flat negative ("is not required", s 313(2); "must not charge", s 317(2); "can not provide", s 322(5)), a period the text fixes (ss 321(1)(b), 332(2), 335(5), the cooling-off period).

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 313, `the law practice must disclose the uplift fee in writing first (s 313)`: no uplift fee answers `JUST FALSE` (an unmet "if"); the other reading is `NOTHING` (the section is silent on agreements without one).
2. s 324(4), `the most uplift fee allowed (s 324(4)-(5))`: a matter that is not litigious answers `NOTHING` (no cap set by s 324(4)); there is no number to give, so a `JUST FALSE` reading has no place, but a reviewer may prefer an explicit "no cap" constructor.
3. s 332(1), `the s 332 answer`: the right to ask for an itemised bill is not cut off when the s 335(5) 12 months have run, although s 332(1) gives it to "any person who is entitled to apply for an assessment"; the other reading ends the right with the 12 months (except where s 335(6) might apply).
4. s 329(1), s 332(4)-(5): "until at least 30 days after" the bill is read as allowing proceedings on the 30th day after it; the other reading (30 clear days) moves every date one day later.
5. s 327(1), `the s 327 answer`: an agreement with no Division 5 contravention answers "not void under s 327(1) on these facts" (the relative clause "that contravenes" read as a condition); it does not say the agreement is valid for every purpose.

## What the Act turns out to say (findings)

1. **The s 347 cap is not in the deposited text.** Section 347(1) sets the most a law practice may charge and recover for a speculative personal injury claim "using the formula", but the formula is an image (`https://www.legislation.qld.gov.au/image/_442b410f-488b-4ef7-8b24-f2c37e078c19.gif`) and the conversion kept only a marker. The definitions of E, R and D survive. Before Division 8 can be encoded, the formula must be transcribed into an `act-2007-024.formulas.md` sidecar from the authorised PDF, as the encoding guide requires. For personal injury clients this is probably the most important number in Part 3.4.
2. **An uplift fee always makes the agreement conditional.** s 300 defines an uplift fee as additional legal costs "payable ... on the successful outcome of the matter", so any agreement with one is a conditional costs agreement, and all of s 323 (signature, advice statement, cooling-off) applies. The encoding derives it so. Asserted (V14 and the cooling-off case with an uplift fee only).
3. **The 25% cap applies only to litigious matters.** s 324(4) caps the uplift fee only "if a conditional costs agreement relates to a litigious matter". An uplift fee of 40% on non-litigious work breaks no Division 5 rule (though the agreement can still be set aside under s 328, and s 313 disclosure applies). Asserted (V3).
4. **The cap is measured on undiscounted fees.** s 324(5) makes the 25% a share of what the law practice "would have charged" without its discount, so a discount does not lower the cap. Asserted.
5. **A contingency fee costs the law practice everything; a bad uplift fee costs it only the uplift.** s 327(5) bars recovery of "any amount relating to the provision of legal services in the matter"; s 327(4) bars only the uplift fee. Where both are broken, the encoding gives the s 327(5) answer. Asserted (V7, V9).
6. **Sophisticated clients lose some protections, not all.** s 323(4)(b) lifts the signature, the advice statement and the cooling-off for a sophisticated client, but not writing, plain language or the statement of what counts as success; s 344 lets them contract out of assessment; s 335(6) gives them no late application. Asserted (V6, V10, s 335 case 3).
7. **A disclosure failure does not make the agreement void.** Division 3 is outside "this division" in s 327(1). The client's remedies are s 316 (need not pay until assessed; reduction on assessment) and s 328 (set aside), and the assessor may depart from the agreement under s 340(1)(c). Encoded so.
8. **s 325(2) "to the extent" (READING).** A costs agreement whose award-based part "adopts an applicable scale of costs" is treated as wholly outside s 325(1); an agreement that only partly adopts a scale needs the court's apportionment, which a yes/no input cannot give.
9. **s 332(4)-(5): "given" and "receiving" (READING).** s 332(4) counts 30 days from the date the person "is given" the bill; s 332(5) counts the 30 days for a request "after receiving" it. The encoding treats the two days as the same.
10. **s 342(2)(a): reduced by 15% of what? (READING).** The text does not name the base; the encoding measures the reduction against the legal costs put up for assessment. Asserted at exactly 15% and a cent under.
11. **Cooling-off counting (READING).** "A cooling-off period of not less than 5 clear business days" is read as running from the day after the agreement is made; a notice is within it if fewer than the agreement's number of business days have ended before the day it is given. Business days are the client's count, not computed (no holiday calendar is deposited).

## Before relying on it

- Transcribe the s 347 formula from the authorised PDF into a formulas sidecar, then encode Division 8 (speculative personal injury claims) with its cases.
- Deposit the Legal Profession Regulation and replace the fallback threshold amounts and the interest-rate input.
- Have a lawyer check readings 8-11 and the fork lines.
- Add a seat for the law practice, and the disclosure contents (ss 307B(2), 308(4)).
- An independent test pass, and the human gates.
