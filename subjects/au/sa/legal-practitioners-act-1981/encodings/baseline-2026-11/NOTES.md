# Legal Practitioners Act 1981 (SA), Schedule 3 -- baseline encoding, the client (costs agreements)

> **Edition.** The texts encoded here come from the official South Australian register (legislation.sa.gov.au), not
> from the Open Australian Legal Corpus: the register answered without a bot challenge on 6 November 2026. They are the
> register's *unauthorised* RTF renderings: the Act at version 1.9.2026 and the Legal Practitioners Regulations 2014 at
> version 1.7.2020. The authorised versions are the PDFs. Check legislation.sa.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`lpc-core.l4`) holds every rule, with three regulative rules (cl 31(1) with
cl 34(4)-(5), a prohibition on suing within 30 days of the bill; cl 34(2), the duty to give an itemised bill within 21
days; cl 37(4), the client's 6 months to apply for adjudication) run by `EVALTRACE` inside functions that take only plain
facts. The seat layer (`lpc-seat.l4`) restates none of the rules. Dates sit in one small module (`lpc-dates.l4`,
built-in date functions only, no daydate). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. Answers
are named outcomes (enumerations), numbers or dates, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used; where the
text says no in its own words the outcome is a "no: ..." naming the clause, and where a clause does not reach the case
the outcome says that the clause "does not apply", which follows the 2026-11-04 and 2026-11-05 rulings in substance. No
pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Legal Practitioners Act 1981, register version 1.9.2026 (as at 1 September 2026), deposited at
  `../../registers/source-bundle/legal-practitioners-act-1981.txt` (text sha256 b0ad6e5a...b22e658bf per its
  `.meta.json`). Section 41 and Schedule 3 (inserted by Act 44/2013 s 61 from 1 July 2014; cl 25(2)(c)(ii) deleted and
  cl 26(1a) inserted by Act 70/2017 from 1 March 2018; cl 18(7) and cl 30 amended by Act 49/2019 from 1 July 2020;
  cl 30(3) by Act 51/2025 from 1 September 2026).
- **Regulations that set its numbers:** Legal Practitioners Regulations 2014, register version 1.7.2020, deposited at
  `subjects/au/sa/legal-practitioners-regulations-2014/registers/source-bundle/legal-practitioners-regulations-2014.txt`
  (text sha256 e8961518...f13f3eb0 per its `.meta.json`): reg 58 (substantial connection, in the `@desc`), reg 60 (a
  further exception to disclosure), reg 61 (the interest cap), reg 62 (cl 25 reaches associated third party payers).
  They prescribe no amount for cl 13(1)(a), no kind of matter for cl 25(2)(d), so $1 500 and the Act's list apply.
- **Not deposited, so inputs:** the Reserve Bank's Cash Rate Target (reg 61(2)); the scale of costs and the fair and
  reasonable value of work (cll 21(b), (c), 29(2), 30(5)).
- **Coverage dates.** Matters first instructed on or after 1 July 2014 (44/2013 Schedule, transitional cl 9(1)); an
  earlier matter answers `not covered`, asserted. The uplift rules are the ones in force since 1 March 2018 (the
  Migration Act bar); an agreement made before then is not distinguished.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpc-dates.l4` | 0 | 0 | 0 | 0 |
| `lpc-core.l4` | 0 | 0 | 0 | 0 |
| `lpc-seat.l4` | 0 | 0 | 0 | 0 |
| `lpc-cases.l4` | 0 | 0 | 147 | 147 |

Negative control (in a scratch copy): with the cl 26(4)(b) 25% changed to 26% and the cl 13(1)(a) $1 500 to $1 499, the
cases failed exactly the 4 predicted assertions ($1 500 disclosure; the two uplift maxima of $40 000 and $12 345; the
$10 000.01 uplift on $40 000).

Every expected value was worked by hand from the text, with the edges: 30 June and 1 July 2014; a notice on the 28th
and the 29th day after being told of the right (cl 4(4)); $1 500 and $1 500.01; an uplift fee of exactly 25% and one
cent over; 4 and 5 cooling-off business days and the 5th and 6th business day; the 29th and 30th day after a bill, for
interest and for proceedings; the 21st and 22nd day after a request for an itemised bill; the last day of the 6 months
at month ends and 29 February 2024; a reduction of exactly 15% and of 14.99%; a rate exactly at and just over the Cash
Rate Target plus 2. Cash Rate Target figures are invented test figures.

## Seat

**The client (required): the person who retains a law practice for a matter and has to pay for it**, typically someone
injured who signs a no win, no fee (conditional) costs agreement for a compensation claim (`lpc-seat.l4`, 24
questions). Every question is one that person would ask: "Does the South Australian costs law apply to my matter?",
"Must my lawyer tell me the costs?", "My lawyer didn't tell me: what follows?", "Can my agreement be no win, no fee?",
"Can it have an uplift fee, and how much at most?", "Can my lawyer take a percentage of my compensation?", "Is my
agreement void?", "Can I still cool off?", "What must be repaid?", "Can it be set aside?", "Can I be charged interest,
and at what rate?", "By when must I get the itemised bill?", "When can my lawyer sue me?", "By when must I apply for
adjudication?", "Who pays the costs of the adjudication?". Provisions addressed to the law practice or the Supreme Court
are encoded as what they mean for the client: a bar on suing, a refund, a cap, a date.

An associated third party payer (someone who owes the law practice the client's costs) stands where the client stands
for cl 25 (cl 24(6), reg 62) and may use the same questions; no separate seat. No seat for the law practice here (a
second layer would be welcome), and none for the Supreme Court, the Commissioner or the Society.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: Regulations regs 58, 60, 61, 62 brought in;
  the Cash Rate Target and the scale or fair value are inputs.
- **The actors the text names.** Followed: client, law practice, associated third party payer, principal, barrister,
  Supreme Court, Commissioner.
- **Judgments answered conditionally.** Followed: "reasonable grounds" (cl 13(1)(b)(iii)), "significant" risk
  (cl 26(4)(a)), "satisfied that the agreement is not fair and reasonable" (cl 30(1)), "just and fair" (cl 37(5)), the
  cl 47(1)(c)-(e) findings, "satisfied that the law practice failed to comply with Part 3" (cl 49(2)(b)), "likely to
  exceed" (cl 13(1)(a)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: cl 1 "sophisticated client" (from cl 13(1)(c),
  (d)), "conditional costs agreement", "uplift fee", "litigious matter" (asked with the definition in the `@desc`),
  "business day" (the client counts them); borrowed: the Corporations Act kinds of company, "criminal matter", "pro
  bono", the Cash Rate Target.
- **One case:** one matter, one law practice, one costs agreement, one bill.
- **The Act's terms with plain glosses:** in the `@desc`s ("law practice" glossed as your lawyer's firm, "uplift fee" as
  extra costs if you win, "conditional" as no win, no fee).
- **Machinery out:** cll 7 (regulation power, used through reg 58), 10(3), (7), 33(5), 52 (regulation powers), 53
  (imputation), s 41 (application only).

## Scope

**In:** Schedule 3 cll 1-2 (definitions, as used), 3-5 (application; reg 58 in the `@desc`), 9, 11(2), 12, 13
(whether costs must be disclosed; reg 60), 18 (what follows a failure to disclose), 19 (reports), 23 (interest; reg 61),
Part 5 in full (cll 24-30: making costs agreements, conditional agreements, uplift fees, contingency fees, effect, void
agreements and their consequences, setting aside), 31 and 34 (when the law practice may sue; itemised bills), 37(4)-(5)
(the client's 6 months), 44 (stay), 47 (the agreement as the measure), 49 (costs of the adjudication), 51 (contracting
out).

**Out, and why:**

- cl 8 (a matter that moves between this Schedule and another jurisdiction's law over time): rare, and it needs the
  history of the matter by period; left for a second pass.
- cll 10, 14, 15, 16, 17, 20 (the content, form and timing of each disclosure): they are the law practice's checklist;
  their only consequence for the client is cl 18, which is encoded with "the law practice failed to disclose something
  Part 3 required" as the input. A disclosure question per paragraph would add little.
- cl 21 and 22 (the basis on which costs are recoverable; security): used inside cl 29; no separate question.
- cll 32, 33 (form and signing of bills): the client is asked only whether a bill was given; a bill not in accordance
  with them is treated as no bill (cl 31(1)).
- cl 35 (interim bills) and cl 37(1)-(3), (6)-(9), cll 38-43, 45, 46, 48, 50 (who else may apply, the court's powers and
  criteria, referral): the court's process; the client's questions about them are the time limit, the measure (cl 47)
  and the costs (cl 49).
- The rest of the Act (admission, practising certificates, trust money, the Fidelity Fund, discipline): not claims
  machinery. Part 5 (claims against the Fidelity Fund) would be a separate encoding.

## Forks (the text does not say; one reading taken)

- **F1** "within 6 months after" (cl 37(4)): the same day of the month six months later, or that month's last day where
  shorter (31 August 2023 to 29 February 2024; 31 August 2025 to 28 February 2026). Asserted.
- **F2** "until at least 30 days after the law practice has given a bill" (cll 31(1), 34(4), (5)): the 30th day after
  the day the bill was given is the first day proceedings may begin (bill on 1 March, proceedings from 31 March).
  Asserted.
- **F3** "within 21 days after the date on which the request is made" (cl 34(2)): the 21st day after is the last day.
  Asserted.
- **F4** "unpaid 30 days or more after the practice has given a bill" (cl 23(1)): interest from the 30th day after.
  Asserted.
- **F5** cl 13(1)(a) "not likely to exceed $1 500": exactly $1 500 is within the exception. Asserted.
- **F6** "a cooling-off period of not less than 5 clear business days" (cl 25(3)(e)): counted from the first business
  day after the day the agreement was made; today falls within it while the business days counted up to today are no
  more than the period. The client counts the business days, so no holiday calendar is needed. Asserted.
- **F7** cl 4(4) "after the period of 28 days after the law practice discloses": a notice on the 28th day is in time.
  Asserted.
- **F8** cl 49(2)(a) "reduced by 15% or more": measured against the costs as billed; exactly 15% counts. Asserted.
- **F9** cl 26(4)(b) "25% of the legal costs (excluding disbursements) otherwise payable": the base excludes the uplift
  fee itself; exactly 25% is allowed. Asserted.
- **F10** an "uplift" in an agreement that is not conditional is not an uplift fee within cl 1 (which ties it to the
  successful outcome), so cl 26 is not reached and such an agreement is tested by the other rules only. The other
  reading voids it under cll 26(1), 29(1). Asserted.
- **F11** cl 29(3) for an agreement void under cl 26: the agreement amount that caps recovery excludes the uplift fee
  (cl 29(4)); for any other void agreement it includes it. Asserted.
- **F12** cl 49(4) is read as overriding cl 49(2) ("However"), and only where the client is the applicant. Asserted.
- **F13** where several defects make an agreement void, the answer names the one with the harshest consequence first
  (cl 27, then cl 26), then the clauses in order. Any one makes it void (cl 29(1)); the order only chooses the message.

## What the Act turns out to say (findings)

1. **cl 25(2)(c) jumps from (i) to (iii).** Subparagraph (ii) was deleted by Act 70/2017 s 12(1) from 1 March 2018
   (legislative history), and (i) still ends "the Family Law Act 1975;" with no "or". Harmless; asserted as a list of
   two Acts.
2. **cl 4(1)(c)(ii) reads "sublause (2)(b)".** A typing slip in the register's text for "subclause". Not encoded.
3. **A Crown-held corporation is not a "sophisticated client".** Reg 60 frees it from disclosure under cl 13(1)(f), but
   cl 1 defines a sophisticated client only by cl 13(1)(c) and (d). So a no win, no fee agreement with such a
   corporation still needs its signature, the independent advice statement and a 5-day cooling-off period (cl 25(5)
   relieves sophisticated clients only), and it may still ask the court to hear a late adjudication application.
   Asserted (the 4-day cooling-off agreement is void).
4. **cl 15 is not in Part 5.** A failure to give the uplift fee estimate and reasons before entering the agreement does
   not make the agreement void (cl 29(1) speaks of "this Part", Part 5); it engages cl 18 instead (pay only after
   adjudication; set aside; reduction). The agreement's own uplift requirements (cl 26(2), (3)) do void it.
5. **The interest cap moves with the bill.** reg 61 fixes the cap at the Cash Rate Target "as at the relevant date",
   the date the bill was issued, so two bills in one matter can carry different caps.
6. **The Regulations deposit is older than the Act's** (1 July 2020 against 1 September 2026); it was the current
   version on the register on 6 November 2026, but later prescribed amounts (cl 13(1)(a)) or excluded matters
   (cl 25(2)(d)) would change the answers.
7. **cl 30(10) and cl 36 define "client" as "a person to whom or for whom legal services are or have been provided",
   while cl 1 says "includes"**: the closed definition governs setting aside and adjudication. Not separately encoded.

## Before relying on it

Check the texts against the authorised PDFs and any later Regulations; have a lawyer review the forks (especially F2,
F6, F10 and F13); add the law practice's seat and cll 8, 14-17, 35, 38-39; take the Cash Rate Target from the Reserve
Bank's series; run an independent test pass.
