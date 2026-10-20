# Business Names Registration Act 2011 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. There was no first-pass encoding of this Act to replace.

It is kept consistent with the ABN Act baseline beside it
(`subjects/au/a-new-tax-system-australian-business-number-act-1999/encodings/baseline-2026-10/`).
This Act's s 4(2) borrows ABN entitlement. Here that entitlement is asked as a fact,
and the ABN baseline works it out. The 28-day silence rule (s 34) is read the same
way as the ABN Act's s 13.

## Edition

- **The Act:** Compilation No. 10, compilation date 1 July 2026 ("Includes
  amendments: Act No. 57, 2026"; register id C2026C00334). Deposited at
  `../../registers/source-bundle/C2011A00126.txt` (retrieved 2026-10-13).
- **Crimes Act 1914**, s 4AA (penalty unit) and s 4B(3) (bodies corporate) only:
  Compilation No. 167, compilation date 27 August 2026 (register id C2026C00368).
  Deposited at `subjects/au/crimes-act-1914/registers/source-bundle/C1914A00012.txt`.
  s 4AA sets $330 "subject to indexation", and indexation fell due on 1 July 2026.
  The deposit gives the formula but not its result, so the dollar value of a penalty
  unit is an input. The case file uses $330 only as an illustration.
- **Not deposited:**
  - the Business Names Registration (Fees) Act 2011 (only its metadata is in
    Commons), so no fee amount is encoded;
  - the Minister's instruments under ss 26, 27(1) and 28(1) (identical names,
    undesirable names, restricted words) and any regulations under s 18(2)(h). What
    they decide is asked as a fact.

## Checks

- One module (`bn-registration.l4`) and one case file (`bn-cases-registration.l4`).
- **40 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98.
- The case file is built by `gen_business-names-registration-act-2011_baseline.py`
  in the session scratchpad. Every expected value was written by hand from the text.
- One assertion was deliberately inverted in a scratch copy. The runner reported
  it as failing (39 of 40), so the runner does catch a wrong expectation.

Facts the life does not state are **assumptions**, labelled in the case file:

- that Jarrah trades under a name other than its full company name (written here as
  "Jarrah Legal"). The life says only that it got "a business name";
- that the name is clear of conflicts, undesirable kinds and restricted words;
- that Jarrah has its ABN and pays the fee;
- that no one involved in Jarrah's management has a disqualifying conviction.

## Seat

**The business owner**: the entity carrying on a business under a name. In the
life this is Daniel's company, Jarrah Legal Technologies Pty Ltd. The Act's duties
fall on "an entity" (s 5), so the company is the one asking, and Daniel asks for
it. His own record matters only through s 32(1)(b) and (e), as a person involved
in the company's management.

Where the Act speaks to ASIC or the Minister (ss 24, 25, 30, 33, 34, 47, 49, 55),
the encoding says what it means for the owner:

- ASIC must register the name;
- the application is taken to be refused, or the owner may treat it as refused;
- ASIC may cancel the name, and must first give notice and time.

The 2026-10-18 defaults:

- **The Act alone, plus instruments that set its numbers.** Followed. The Crimes
  Act's penalty unit and five-times rule for bodies corporate are brought in,
  because they turn the Act's "30 penalty units" into a fine. The instruments that
  would set fees and name rules are not deposited, so what they decide is asked.
- **The actors the text names.** Followed: the entity, ASIC, the Minister, the
  holder of a name, a notified successor, a person involved in management.
- **Judgments handed to someone else are answered conditionally.** Followed. These
  are all inputs:
  - ASIC's satisfaction (ss 24, 47);
  - the Minister's determinations (ss 27(2), 28(2A), 32(3));
  - the Minister's rules on what is identical, undesirable or restricted.
- **The Act's own definitions are worked out; borrowed terms are asked.**
  Followed:
  - worked out: "business" (s 4), "carrying on a business" (s 3), "available"
    (s 25) and "disqualified" (s 32);
  - asked: ABN entitlement, corporation, government body, notified State/Territory
    register, and disqualification under Corporations Act s 206B.
- **One case is the text's natural unit.** Followed: one entity and one name.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed, with a size limit (25–40
  assertions). Left out:
  - the s 20 display duty and s 21, except their penalties;
  - most cancellation grounds;
  - review;
  - Part 10;
  - the register's public face.

## The lives

- **Daniel, d043 (2031, age 34):** Jarrah Legal Technologies Pty Ltd is registered
  with ASIC, with an ABN and a business name. Decisions asked:
  - `Must I register the business name`. Trading as "Jarrah Legal" before
    registration: "yes: I must register it, or I commit the s 18(1) offence". So too
    while it is still setting up, before its first client. Once registered: "no:
    the name is registered to me". Trading only under "Jarrah Legal Technologies Pty
    Ltd": "no: it is my own name".
  - `Is the business name available to me`: "available" on the assumed facts.
  - `What happens to my application for the name`: ASIC must register it once Jarrah
    has its ABN. Until then, ASIC need not register it, although Jarrah may apply
    while its ABN application is pending.
  - `Does this record disqualify me`: Daniel, no convictions, does not.
  - `Most penalty units for the offence`: Jarrah, as a body corporate, faces up to
    150 penalty units for trading under an unregistered name.

## Why this scope

The event asks one question, and the seat puts it: must I register a business name?
The answer turns on:

- what a business is (s 4, through the ABN);
- the s 18 exceptions;
- the two grace periods (ss 31(6), 54(1)(b)).

Around that question, the encoding covers what an ordinary owner then meets:

- whether the name can be had (s 25);
- whether the owner is disqualified (s 32);
- when ASIC must register (s 24), and what an unpaid fee or a silent ASIC means
  (ss 30, 34);
- how long registration lasts, how to renew, and when an expired or unused name can
  be taken away (ss 33, 47, 49, 55);
- the duty to keep details current (s 35);
- what documents must show (s 19), and what the offences cost.

## What the Act turns out to say

1. **Only a business needs a registered name, and a business must be something that
   would earn an ABN** (s 4(2)). s 4(1)(a) lists "employment", but an employee is not
   entitled to an ABN (see the ABN baseline), so (2) takes it out again. An employee
   using a nickname at work commits no offence. Asserted.
2. **Setting up counts.** "Carrying on a business includes doing anything in the
   course of the commencement or termination of the business" (s 3). Jarrah needs
   the name registered before its first client, not after. Asserted.
3. **The own-name exception exists only for individuals, corporations and
   partnerships** (s 18(2)(a)-(c)). For a partnership, the name must consist of all
   the partners' names. A trust trading under its trustee's name has no exception.
   Asserted.
4. **A company trading under its full registered name needs no business name**
   (s 18(2)(b)). Jarrah needs one only because it trades under another name (an
   assumption about the life). Asserted.
5. **The offence is strict liability** (s 18(3)), with an evidential burden on the
   exceptions (the s 18(2) note). The maximum is 30 penalty units, and five times
   that, 150, for a body corporate (Crimes Act s 4B(3)). At the pre-indexation $330,
   that is $9,900 for an individual. Asserted.
6. **There are two windows in which trading under an unregistered name is not an
   offence:**
   - 3 months after notifying ASIC of the holder's consent (s 31(6));
   - the review period after a cancellation (s 54(1)(b)), 4 months unless ASIC sets
     a longer one.

   Asserted for the first.
7. **Invoices, receipts, orders, cheques and offers must show the business name and,
   if you have one, the ABN.** Other business documents need only the name (s 19(2),
   (3)). Asserted.
8. **A name is not available if it is identical or nearly identical to another's**,
   or held, or claimed first, or undesirable, or restricted (s 25). The holder's
   consent with a request to cancel makes it available (s 31(3)). The Minister can
   lift undesirability and restrictions for one entity (ss 27(2), 28(2A)). Asserted.
9. **ASIC must register once satisfied of four things:** an ABN, the fee paid, the
   name available, and the entity not disqualified (s 24(1)). An entity may apply
   while its ABN is pending (s 23(2)(a)(ii)) and keeps its priority (s 29(2)). But
   registration itself needs the ABN. Asserted.
10. **Disqualification.** These disqualify the entity:
    - a person disqualified from managing corporations for a conviction;
    - a dishonesty conviction punishable by at least 3 months;
    - a foreign conviction punishable by more than 12 months.

    The conviction may be the entity's or that of a person involved in its
    management (s 32(1)). For a conviction, the period is 5 years from conviction
    or from release (s 32(2)). A local non-dishonesty offence does not disqualify,
    however serious. The encoding asks the s 206B ban as a single "currently" fact,
    because its period is set by that Act. Asserted.
11. **An unpaid fee kills the application after 10 business days** (s 30). 28
    days of silence lets the applicant treat it as refused and get the fee back
    (s 34(2), (4)). Time spent waiting on ASIC's requests does not count (s 34(5)).
    "Within 28 days" is read as in the ABN baseline. Asserted.
12. **Registration is for 1 or 3 years.** An alternative period, which only a
    company aligning with its review date or an owner aligning with another of its
    names can ask for, is capped at 18 or 42 months (ss 33(2)-(5), 55(7)). Asserted.
13. **Renewal opens 2 months before expiry, and a name does not lapse on expiry**
    (ss 55(8), 49(5)). It stays registered until ASIC cancels it. Cancellation can
    take effect no earlier than the later of 3 months after expiry and 6 weeks after
    a s 49(3) notice. So renewal remains open after expiry. Without a s 49(3) notice,
    the encoding reads that there is no cancellation date (an inference). Asserted.
14. **Unused names can be cancelled** (s 47). The conditions are: no trading under
    the name now or in the past 3 months; ASIC not satisfied that exceptional
    circumstances explain it; and at least 28 days' notice. Government bodies are
    exempt. Asserted.
15. **Changes to registered details must be notified within 28 days of becoming
    aware** (s 35). Asserted.
16. **Registration gives no property in the name** (s 17(2)). This is not
    encoded as a decision. A registered business name is no defence to a trade mark
    action, and a court may order it cancelled (s 51).

## What would need doing before this is worth anything

- An independent test pass, and a human gate.
- The Minister's instruments on identical, nearly identical, undesirable and
  restricted names (ss 26-28). That is where availability really turns, and they
  are asked as facts here.
- The Business Names Registration (Fees) Act 2011 and its fee amounts, once
  deposited.
- The indexed penalty unit after 1 July 2026 (Crimes Act s 4AA(1A) notifiable
  instrument).
- The s 20 display duty, s 21, the other cancellation grounds (ss 42-46, 48,
  50-51) and review (Part 7), if the seat needs them.
- Part 10, for partnerships, associations, trusts with several trustees and joint
  ventures: who carries the duties.
