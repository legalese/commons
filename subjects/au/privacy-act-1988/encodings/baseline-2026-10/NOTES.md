# Privacy Act 1988 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**Edition:** Compilation No. 104, compilation date 4 June 2026, includes amendments to Act No. 75, 2025 (register id
C2026C00227), as deposited at `../../registers/source-bundle/C2004A03712.txt` (retrieved 13 October 2026), with the
s 6DA(2) formula from `../../registers/source-bundle/C2004A03712.formulas.md`, transcribed by hand on 21 October 2026
from the Word rendering of the same compilation (the text deposit had lost it).
The Privacy Regulation 2013 and the Privacy (Credit Reporting) Code 2014 are **not deposited**. The one number they could
set that this encoding needs, a default amount higher than $150 (s 6Q(1)(d)(ii)), is an input. The matters they add to
notices (APP 12.9(c), 13.3(c), ss 21C, 21P) and the manner of access to a credit report (s 20R(4)) are not encoded.

**Checks:** one module (`pa-individual.l4`, 31 exported questions), one case file (`pa-cases-individual.l4`). 77 assertions
satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98.

This encoding replaces the first-pass encoding `naive-2026-10`. It covers everything that encoding covered, reuses its
hand-checked dates and figures, and adds APP 12, APP 13, s 7B(3), ss 20K, 20R, 20T, 21C, 21P and the Part V complaint gate.

## Seat

**The individual whose personal information is held**: the borrower (Chloe and Jake taking credit cards), the debtor (Jake
with collectors and a debt agreement), the customer being marketed to (Chloe), the user whose email address is breached
(Jarrah's 1,200 users), and the employee whose records an employer holds (Jarrah's first three staff). The Act's
obligations fall on entities, and nearly every section addresses one of them. But every right it creates belongs to the
individual: to be told, to see, to correct, to opt out, to have a file cleaned, to complain. Each exported question is
asked as that person would ask it ("Must the holder give me access…", "Must I be told about a data breach…", "Will the
Information Commissioner investigate my complaint…").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Regulation and the CR code are not
  deposited, so the prescribed default amount is an input and the code's matters are left out.
- **The actors the text names.** Followed: APP entity, organisation, agency, small business operator, credit provider,
  credit reporting body, the Commissioner, the respondent.
- **A judgment handed to someone else is answered conditionally.** Followed. Examples: "a reasonable person would conclude"
  serious harm is likely (s 26WE); the entity "is satisfied" information is wrong (APP 13.1, s 20T(2)); an APP 12.3 ground
  (several turn on the entity's reasonable belief); the Commissioner considering it "not appropriate" to complain to the
  respondent first (s 40(1A)). Each is an input.
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed for small business, small business
  operator, organisation, APP entity, credit information, default information, eligible data breach and at risk.
  Departure: annual turnover (s 6DA(1)) is a dollar input, because it is the holder's accounting figure. The s 6DA(2)
  part-year formula is encoded on its own (from the formula sidecar), taking the amount earned in the part and the days. Whether the Do Not Call Register Act 2006 or the Spam Act 2003 applies is asked as
  a fact (APP 7.8).
- **One case is the text's natural unit.** Followed: one holder, one request, one overdue payment, one debt agreement, one
  incident, one complaint. Simplification: one business per holder.
- **The Act's own terms, each with a plain gloss.** Followed in the comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed. The Commissioner's functions, determinations, enforcement and
  penalties are out. Where a provision addresses only the entity (s 26WK statement, s 26WH assessment), the encoding
  answers what it means for the individual: whether a statement goes to the Commissioner, and whether the individual is
  told yet.

## The lives

- **chloe c043** (2024, 21): a credit card; a credit report pulled. *Must the lender name the credit reporting body?*
  (s 21C: yes). *Must the card issuer give me access, and by when?* (APP 12: yes, within a reasonable period). *Is my
  credit report free?* (s 20R(5): yes, on a first request in 3 months).
- **chloe c044** (2024, 21): marketing calls and texts. *May this business use my information to market to me?* (APP 7:
  not reached when the Do Not Call Register Act or the Spam Act applies; forbidden once she has asked to stop.) *Must it
  stop when I ask?*
- **daniel d044** (2031, 35): Jarrah's first three employees, "no Privacy Act yet". *Is Jarrah a small business
  operator?* (yes, first-year turnover under $3 million). *Is it bound by the APPs?* (no, unless it opts in under s 6EA).
  *Does APP 13 protect its customers?* (no). Asked from the employees' seat, *Do the APPs protect my employee record?*
  (no, even after 2036: s 7B(3)).
- **daniel d052** (2036, 39): above $3 million; 1,200 users' email addresses breached. *Is it an eligible data breach?*
  (yes, if a reasonable person would conclude serious harm is likely). *Must I be told, and how?* (directly, if I am at
  risk, as soon as practicable after the statement to the Commissioner is prepared). *Will the Commissioner investigate
  my complaint?* (only after I have complained to Jarrah).
- **jake k048** (2031, 24): two credit cards. *How long does the application enquiry stay on my file?* (s 20W: 5 years
  from the information request). *Is a second credit report within 3 months free?* (no; s 20R(6) limits the charge).
  *Must a refusal be explained?* (s 21P).
- **jake k064** (2037, 30): debts of $41,000; collectors call. *Is my overdue payment default information?* (s 6Q). *May
  it be listed?* (s 21D: 14 days after notice of intention). *How long does it stay?* (5 years from collection). *Will
  the Commissioner take my complaint about a correction straight away?* (yes: s 40(1B)).
- **jake k075** (2042, 35): the debt agreement completes. *Has the retention period for my debt agreement ended?*
  (s 20X item 5: the later of 5 years from the making and the day it ends).

## Why this scope

The plan entry names s 6D, Part IIIA, Part IIIC and APP 7. The seat adds what an ordinary person in it can actually
*use*: access (APP 12) and correction (APP 13), the same two rights against a credit reporting body (ss 20R, 20T), the
fraud ban (s 20K), the two notices a borrower is owed (ss 21C, 21P), and the gate to the Commissioner (ss 36, 40, 41).
Part IIIA is a code of nearly a hundred sections. Only the provisions the lives turn on, and the individual's own
rights, are taken: what a file may hold, when a default may be listed, how long things stay, and how to see and fix the
file. The use and disclosure rules for bureaus and credit providers (ss 20E-20N, 21G-21N) govern entities among
themselves and are left out. The new statutory tort in Schedule 2 is a separate cause of action and is left for its own
encoding.

## What the Act turns out to say

1. **Above $3 million once means never again exempt.** s 6D(4)(a) excludes anyone whose business "has had an annual
   turnover of more than $3,000,000 for a financial year that has ended" since it started. Jarrah, above the line in
   2036, stays bound when turnover falls back to $2.5 million, although its business is again a "small business" under
   s 6D(1). Exactly $3,000,000 is still small. Asserted.
2. **Jarrah's first year is judged on the current year, annualised.** s 6D(2) applies when the business was not carried
   on in the previous year. The s 6DA(2) formula, lost from the text deposit and now transcribed from the Word rendering,
   is the amount the business would have turned over had the part been a whole year, times the days in the whole year
   over the days in the part. A business started on 1 February 2031 (an assumption: 150 days) that earns $150,000 has an
   annual turnover of $365,000; $600,000 in 73 days is exactly $3,000,000 and still small; $600,001 is not. The holder
   fixtures still take the current-year figure as an input. Asserted (d044).
3. **The employees get nothing from the Act even once Jarrah is bound.** s 7B(3) exempts an employer's act "directly
   related to" the employment relationship and an employee record. Jarrah's staff are outside the APPs in 2031 because
   Jarrah is a small business operator. In 2036 they are outside them because of s 7B(3). Asserted.
4. **Access and correction deadlines differ by who holds the information.** An agency must respond "within 30 days".
   An organisation must respond "within a reasonable period" (APP 12.4, 13.5). An agency may not charge for access. An
   organisation may charge for giving access, not excessively, but never for the request. Nobody may charge for
   correction. Asserted.
5. **A credit report is free once every three months, and due within 10 days.** s 20R(3), (5). A second request within
   3 months may carry a charge that "must not be excessive". A bureau satisfied that the file is wrong must correct it
   within 30 days, or a longer period the individual agreed to in writing (s 20T(2)). Asserted.
6. **A complaint about a credit report can go straight to the Commissioner.** s 40(1A) bars investigation until the
   complainant has complained to the respondent. s 40(1B) lifts the bar for complaints about access to or correction of
   credit reporting information (ss 20R, 20T, 21T, 21V). The Commissioner may decline a complaint made more than 12 months
   after the complainant became aware (s 41(1)(c)). That is a "may": the encoding says so and does not guess. Asserted.
7. **No section sets a number of days to tell me of a breach; the 30 days is for an assessment.** s 26WH's 30 days
   applies only while the entity merely *suspects*. Once it believes, the statement to the Commissioner is due "as soon
   as practicable" (s 26WK), and notification "as soon as practicable after the completion of the preparation of the
   statement" (s 26WL(3)). Asserted.
8. **Whether I am told directly depends on whether I am at risk.** s 26WL(2) lets the entity notify everyone or only
   those at risk. The encoder reads the "or" as a choice where both are practicable. An individual at risk is then told
   directly either way. One not at risk may or may not be told. If neither is practicable, the statement goes on the
   website. Remedial action that makes serious harm to me unlikely removes the duty to tell me (s 26WF(2)). Asserted, on
   the encoder's reading.
9. **Whether 1,200 email addresses is "serious harm" is not answered by the Act.** s 26WG lists matters to weigh and
   ends with "any other relevant matters". This is an input, and both answers are asserted.
10. **A completed debt agreement stays until it ends, not for "five years from completion".** s 20X(1) item 5: the later
    of "5 years that starts on the day on which the agreement is made" and "the period that ends on the day on which the
    agreement ends". Jake's agreement, if made on 20 April 2037, may go from 1 June 2042. If made on 1 July 2037, it may
    go from 1 July 2042. The bureau then has one month to destroy or de-identify it (s 20V(2)). Asserted.
11. **APP 7 gives way on calls and texts.** APP 7.8 disapplies the principle "to the extent that" the Do Not Call
    Register Act 2006 or the Spam Act 2003 apply. The encoder infers (not asserted as law) that Chloe's telemarketing
    calls and texts fall under those Acts, so her remedy lies there. For a catalogue by post, APP 7 forbids marketing
    once she has asked to stop. Asserted.
12. **A default needs 60 days, a written demand, $150, and 14 days' warning.** s 6Q(1) and s 21D(3)(d). Nothing from
    before 18 may be listed (s 21D(3)(a)). A default stays for five years from the day the bureau collects it (s 20W).
    Asserted.

## What would need doing before this is worth anything

- Wire the s 6DA(2) annualisation into the holder fixtures (today the current-year turnover is entered already annualised).
- Deposit the Privacy Regulation 2013 (any prescribed higher default amount; matters prescribed for refusal notices;
  s 6E prescriptions) and the registered CR code (manner of access; extra notice matters).
- Encode the APP 12.3 grounds one by one, and the rest of APP 1-11 that an individual can rely on (collection notices in
  APP 5, use and disclosure in APP 6, cross-border disclosure in APP 8).
- Encode the credit provider side of access and correction (ss 21T-21V), ban-period extensions (s 20K(4)), the Part IIIC
  exceptions (ss 26WN-26WQ), the rest of s 41, and the statutory tort in Schedule 2.
- The scenarios do not give the day Jake's debt agreement was made, Jarrah's turnover figures, or the dates of Jake's
  defaults. The cases use the encoder's assumptions, labelled as such.
- Read OAIC guidance and determinations, especially on "reasonable period", "serious harm" and the s 26WL choice between
  notifying everyone and notifying only those at risk.
