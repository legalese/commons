# A New Tax System (Australian Business Number) Act 1999 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. There was no first-pass encoding of this Act to replace.

## Edition

- **The Act:** Compilation No. 32, compilation date 30 June 2026 ("Includes
  amendments: Act No. 57, 2026"; register id C2026C00290). Deposited at
  `../../registers/source-bundle/C2004A00467.txt` (retrieved 2026-10-13).
- **A New Tax System (Goods and Services Tax) Act 1999**, s 9-20 only (the meaning
  of "enterprise", which s 41 of this Act borrows): Compilation No. 96, compilation
  date 1 January 2026 ("Includes amendments: Act No. 72, 2025"). Deposited at
  `subjects/au/a-new-tax-system-goods-and-services-tax-act-1999/registers/source-bundle/C2004A00446.txt`.
- No regulations set a number this encoding needs. The plan names none.

## Checks

- One module (`abn-registration.l4`) and one case file (`abn-cases-registration.l4`).
- **68 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98.
- The case file is built by
  `gen_a-new-tax-system-australian-business-number-act-1999_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.
- One assertion was deliberately inverted in a scratch copy. The runner reported
  it as failing (67 of 68), so the runner does catch a wrong expectation.

Facts the lives do not state are **assumptions**, labelled in the case file:

- that Jake rides as a contractor, not an employee, and expects a profit. Whether he
  is an employee is a Fair Work Act question; here it is a fact;
- that Jarrah's application satisfied the Registrar;
- that the approved form asked for details of Jarrah's associates.

## Seat

**The person carrying on an enterprise.** In the lives this is Jake, riding for a
delivery platform with an ABN, and Daniel, founding Jarrah Legal Technologies Pty
Ltd. For Daniel, the entity entitled to the ABN is the company. So the company is
"you" in s 8(2), and Daniel asks on its behalf. A separate case asks about Daniel
personally, as a director.

These are the people the Act addresses as "you" (s 41: "it applies to entities
generally"). Where the Act speaks to the Registrar (ss 10, 13, 15, 18, 19), the
encoding says what it means for them: the Registrar must register them, may cancel
their ABN, must give reasons, must allow at least 14 days.

The 2026-10-18 defaults:

- **The Act alone, plus instruments that set its numbers.** Followed. No instrument
  sets a number this encoding needs.
- **The actors the text names.** Followed: you, the Registrar, partners and
  committee members (s 16), and religious practitioners and institutions (s 5A).
- **Judgments handed to someone else are answered conditionally.** Followed. The
  Registrar's satisfaction is an input everywhere it appears (ss 10, 18, 19).
- **The Act's own definitions are worked out; borrowed terms are asked.**
  **Departed from for "enterprise".** s 41 borrows "enterprise" from GST Act s 9-20.
  The default would ask it as a fact. But "am I an enterprise?" is the whole of the
  question this seat brings, and the caller asked for the definition and its
  exclusions. So s 9-20(1)-(2) is worked out from facts. The terms inside it stay
  borrowed and are asked: employee, withholding payment, charity, and the other
  bodies in (d)-(h). So are the other borrowed terms: "connected with the indirect
  tax zone", "limited registration entity", partnership, associate, approved form.
  The Act's own "business" and "carrying on" are worked out.
- **One case is the text's natural unit.** Followed: one entity and the activity it
  relies on.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. Left out:
  - representatives (ss 9A, 10A, 11A, 18(1A));
  - s 17;
  - the register and access to it (ss 24-27, 29A);
  - s 30;
  - the administration provisions.

## The lives

- **Jake, k040 (6 March 2027, age 20):** rides for a delivery platform on an
  e-bike, with an ABN. Decision: `What is my ABN entitlement`. On contract the answer
  is "entitled: I carry on an enterprise in Australia". As an employee, or riding
  for fun, he is not entitled. Buying the bike before his first delivery is enough,
  because carrying on includes commencement. Also asked for him:
  - `What happens to my application for an ABN`;
  - `Must I tell the Registrar about the change`;
  - `Can my ABN registration be cancelled` (after he stops riding).
- **Daniel, d043 (15 March 2031, age 34):** Jarrah Legal Technologies Pty Ltd is
  registered with ASIC, and gets an ABN and a business name. Decision:
  `What is my ABN entitlement`, answered "entitled: a Corporations Act company is
  entitled to an ABN". This holds even before Jarrah trades. Also asked:
  - `What happens to my application for an ABN` (with associates' details);
  - whether Daniel, as a director paid fees, is personally entitled (no);
  - whether a change in Jarrah's details is Daniel's duty to notify (no; it is
    Jarrah's).

## Why this scope

The two events ask one question, put by s 8: am I entitled to an ABN? Answering it
needs the meaning of "enterprise", which lives in the GST Act. Around that, the
encoding covers what an ordinary person in this seat then meets:

- how to apply and when the Registrar must register them (ss 9-11);
- what to do if the Registrar sits on the application (s 13);
- the two continuing duties (ss 14-16);
- when the ABN can be taken away and given back (ss 18-19);
- what they can object to (s 21);
- the offence they could commit with the number (s 23(1)).

Representatives, the register's public face and government entities are not
questions this seat asks.

## What the Act turns out to say

1. **A company registered under the Corporations Act is entitled to an ABN whether
   or not it carries on any enterprise** (s 8(2) stands alone). Jarrah is entitled
   the day it is registered, before it trades. Asserted.
2. **A limited registration entity is not entitled even if it is a Corporations Act
   company.** s 8(3) begins "However" and is read as overriding both (1) and (2).
   Asserted.
3. **An employee's work is not an enterprise.** s 41 takes "occupation as an
   employee" out of "business", and GST Act s 9-20(2)(a) takes out activity "as an
   employee". Jake riding as the platform's employee would not be entitled. Asserted.
4. **A company director paid fees is not, by that alone, carrying on an
   enterprise.** Director's fees are withholding payments under s 9-20(4). There is
   one exception: an office accepted in the course of the person's own enterprise.
   The exception is read as rescuing only the withholding-payment limb (an
   inference). Asserted.
5. **"No reasonable expectation of profit" excludes only individuals and
   partnerships made up mostly of individuals.** A company or a trust running a
   loss-making business still carries on an enterprise. Asserted.
6. **Starting up counts.** "Carrying on an enterprise includes doing anything in the
   course of the commencement or termination of the enterprise" (s 41). Jake buying
   his bike before the first delivery is entitled. Asserted.
7. **A religious practitioner's vocational activity belongs to the institution**
   (s 5A), unless done as an employee or agent. Asserted.
8. **s 10 says only when the Registrar must register you.** It never says the
   Registrar must refuse. The other outcomes are therefore "the Registrar need not
   register me". (A refusal must come with reasons, s 13(1); that is not encoded.)
   Asserted.
9. **The TFN cannot be compelled** (s 9(3)). Asserted.
10. **After 28 days of silence you may treat the application as refused, and so
    object.** Days spent waiting on information the Registrar asked for do not count
    (s 13(2)-(4)). "Within 28 days" is read as: the right arises once more than 28
    counted days have passed (an inference). Asserted.
11. **Registration, and cancellation, can both be backdated** (ss 11(2), 18(3),
    (6)). Asserted.
12. **The duty to notify changes falls on each partner of a partnership and each
    committee member of an unincorporated association.** It does not fall on a
    company's directors under this Act (s 16). Daniel is not personally bound to
    notify Jarrah's changes under s 14. Whether he could be liable for Jarrah's
    breach under the Taxation Administration Act 1953 is not encoded. Asserted.
13. **A request for information must give at least 14 days** (s 15(2)). The
    encoding treats a shorter request as not yet binding. That is an inference: the
    Act does not say what follows from a short period. Asserted.
14. **Cancellation is always discretionary ("may").** Stopping the enterprise does
    not end the ABN of itself. When the Registrar cancels on his own initiative, he
    must give reasons; when you asked for the cancellation, he need not (s 18(2),
    (5)). Asserted.
15. **Reinstatement is mandatory once the Registrar is satisfied the registration
    should not have been cancelled.** It runs from the day of cancellation (s 19).
    Asserted.
16. **Using a number that is not your own ABN carries up to 2 years' imprisonment**
    (s 23(1)). A cancelled ABN is no longer "your" ABN (s 18 note 1; s 41 "ABN").
    Asserted.

## What would need doing before this is worth anything

- An independent test pass, and a human gate.
- A check of the s 9-20 exclusions against ATO rulings on what makes a business,
  and on hobby and profit expectation. These are asked as facts here, and they are
  where real cases turn.
- A decision on whether to bring in the GST Act's definitions of "limited
  registration entity" (Div 146) and "connected with the indirect tax zone"
  (s 9-25), which are asked as facts here.
- The penalties for breaching ss 14-15 (Taxation Administration Act 1953 s 8C) and
  the Part IVC objection time limits, which belong to that Act's encoding.
- Representatives (ss 9A-11A, 18(1A)), if a seat ever asks about them.
