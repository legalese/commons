# Australian Passports Act 2005 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. This encoding replaces the first-pass encoding `naive-2026-10`. It covers
everything that one covered and keeps its hand-checked values where they are still
right. It adds what the naive encoding could not reach without the two
Determinations: special circumstances, validity periods and fees. Finding 1 replaces
one of the naive encoding's assumptions with a value worked out from the text.
Finding 6 corrects an omission.

## Edition

- **The Act:** Compilation No. 21, compilation date 8 November 2025 ("Includes
  amendments: Act No. 60, 2025"; register id C2025C00643). Deposited at
  `../../registers/source-bundle/C2005A00005.txt` (retrieved 2026-10-13).
- **Australian Passports Determination 2015:** Compilation No. 7, compilation date
  13 June 2026 ("Includes amendments: F2026L00715"; register id F2026C00500).
  Deposited at
  `subjects/au/australian-passports-determination-2015/registers/source-bundle/F2015L01223.txt`
  (retrieved 2026-10-19). Used:
  - s 10 (special circumstances);
  - ss 15-16 (concurrent documents);
  - s 17 (maximum validity);
  - ss 18-19 (ceasing to be valid);
  - s 27(1)(a), (k), (l) and s 28A (waivers);
  - s 31 (the 2005 Determination for earlier applications).
- **Australian Passports (Application Fees) Determination 2015:** Compilation No. 5,
  compilation date 26 November 2024 ("Includes amendments: F2024L01494"; register id
  F2024C01230). Deposited at
  `subjects/au/australian-passports-application-fees-determination-2015/registers/source-bundle/F2015L01222.txt`
  (retrieved 2026-10-19). Used:
  - s 5 (application fees, items 1-6);
  - s 6 (additional fees);
  - s 7 (indexation).

  The s 7 formula is an image the text deposit does not carry. It is transcribed by hand
  from the Word rendering of the same compilation (fetched 2026-10-21) in
  `subjects/au/australian-passports-application-fees-determination-2015/registers/source-bundle/F2015L01222.formulas.md`
  and encoded as `What is the indexation factor for the calendar year`. The CPI numbers are
  not deposited, so the September-year sums are **inputs** to it, and the fee question
  still takes the yearly factors.

## Checks

- One module (`apa-passports.l4`) and one case file (`apa-cases-passports.l4`).
- **70 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98 (re-run 2026-10-21 after the s 7 formula was encoded; one
  redundant fee-item case gave way to the indexation-factor case).
- The case file is built by `gen_australian-passports-act-2005_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.

Facts the lives do not state are **assumptions**, labelled in the case file:

- that both parents had parental responsibility and consented. Chloe's scenario says
  "with both parents' consent"; for Jake, Oliver and Anjali it is assumed;
- Anjali's application date after her citizenship by descent was approved (1 Sep 2027,
  the date the citizenship baseline assumes);
- the indexation factors, which are illustrative, not the published ones.

## Seat

**The passport applicant; for a child, the child and the people whose consent s 11
requires.** Every life event asks the same thing: "Can I (or my child) get a
passport, and whose consent is needed?" Jake at 19 asks it for himself. The decisions
are phrased as the applicant asks them: `Am I a child`, `Does this person have
parental responsibility for me`, `Does s 11 stop my passport`, `What happens to my
application for a passport`, `How long can my passport be valid`, `What will my
passport cost`, `Can I have the decision reviewed`.

Where the Act speaks to the Minister (ss 8, 11, 12-17, 19, 19A), the encoding says
what it means for the applicant. The outcome is one of these:

- the application may not be processed, and the fee is kept;
- it is not a valid application;
- no entitlement (the applicant is not a citizen);
- the Minister must not issue;
- entitled, but the Minister may refuse;
- entitled.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed.
  - The Passports Determination sets the special circumstances, the concurrent-document
    circumstances, the validity periods and the waivers.
  - The Fees Determination sets the fees. Its parent Act, the Australian Passports
    (Application Fees) Act 2005, imposes them; it is deposited, but it was not needed
    for the amounts.
  - Not deposited: the pre-2015 text of s 11 and the 2005 Determination (see finding 7).
- **The actors the text names.** Followed: the applicant, the people with parental
  responsibility, the Minister, the competent authority (only through its request), and
  the court.
- **A judgment handed to someone else is answered conditionally.** Followed. Each one
  is an input named for whoever makes it: the Minister's satisfaction (s 8, s 11(2)(b),
  (c)), the Minister's view (s 11(2)(d), Determination s 10(3)(i)), the Minister's
  suspicion (s 19A), and a competent authority's request (ss 12-16). Where the Act
  gives a discretion (ss 13-16), the applicant is told only that the Minister **may**
  refuse. The encoding does not guess how the Minister will exercise it. This departs
  from the naive encoding, which took the Minister's choice as an input.
- **The Act's definitions worked out from facts; borrowed terms asked as facts.**
  Followed.
  - Worked out: "child" (s 6(1)), "parental responsibility" (s 11(5)), the special
    circumstances (Determination s 10), validity (s 20), and whether a request still
    counts (s 19).
  - Asked as facts: "parent", "parenting order", "family violence order", "child
    welfare law" and "reportable offender".
- **One case is the text's natural unit.** Followed: one application.
- **The Act's own terms, with a gloss.** Followed. Each input carries a plain `@desc`.
- **Operative sections in scope, machinery out.** Followed. Cancellation, suspension
  and surrender (ss 22-26) are operative, but they are left out because no life event
  meets them.

## The lives

- **chloe c013** (2011-06-01): Chloe, 8, gets her first passport, for Bali. "Who may
  apply for a child's passport; whose consent is needed?" Asked by `Does s 11 stop my
  passport` (both parents consent: no) and `What happens to my application for a
  passport` (entitled). The fee is asked by `What will my passport cost`, which answers
  that it is not set by the deposited edition, and `Does the 2015 Determination govern
  my application` answers no.
- **jake k012** (2016-06-15): Jake, 9, gets a passport for a school trip. He is
  entitled, and `What is the latest expiry date of my passport` gives 15 Jun 2021.
- **jake k035** (2026-05-10): Jake, 19, applies for a passport for Bali (s 8). He is not
  a child, so no-one's consent is needed. His 2016 passport has expired, so s 17 does
  not stand in the way, and he is entitled. His passport may run 10 years. Its fee is
  $398 indexed by the 2025 and 2026 factors.
- **chloe c068** (2031-06-10): Oliver, 0, applies, with Chloe and Liam consenting. He
  is entitled, to a 5-year passport.
- **daniel d036** (2027-06-14): Anjali is born in London. Before her citizenship by
  descent is approved she has no entitlement. After approval she is entitled. If only
  one parent consents, s 11(2)(d) cannot help her, but Determination s 10(3)(i) can.
  Her fee is the child fee plus the overseas fee ($288 in 2024 values).

## Why this scope

The lives ask about ss 8 and 11. To answer them, the encoding needs:

- "child" and "parental responsibility";
- the refusal grounds as they reach the applicant;
- when an earlier passport stops being valid (for s 17);
- the Determination's special circumstances, validity periods and fees, because the
  seat asks "how long will it last, and what will it cost?".

Review (ss 48-49) stays from the naive encoding, because whether a decision can be
challenged is what a refused applicant asks next.

Left out:

- travel-related documents;
- who the competent authorities are and on what grounds they request;
- cancellation, suspension and surrender;
- the offences;
- information handling;
- names;
- refunds;
- the machinery.

## What the Act turns out to say

1. **Jake's 2016 passport ran out in 2021, and the Determination says so.** The naive
   encoding had to assume when it expired. Under Determination s 17 item 2, a passport
   issued to a child is valid for at most 5 years. Issued on 15 Jun 2016, it could not
   run past 15 Jun 2021. So at 19, s 17 does not stop Jake's new passport. One caveat:
   the compilation is the 2026 text, and s 17 was amended in 2015 and 2017. Asserted.

2. **Anjali cannot use the return-home exception, but a special circumstance can serve
   her.** s 11(2)(d) needs a child who "departed Australia less than 12 months before".
   Anjali, born in London, has never departed. Determination s 10(3)(i), however, covers
   a child outside Australia where "the Minister considers that there is a need for the
   child to travel internationally". It does not require an earlier departure. So if
   Priya withheld consent, (i) is open to Anjali and (d) is not. A child who left 6
   months earlier can use (d); one who left 12 months earlier cannot ("less than").
   Asserted.

3. **Before her citizenship is approved, Anjali has no entitlement at all.** s 7(1)
   entitles "an Australian citizen", and s 8 requires the Minister to be satisfied of
   citizenship. Consent from both parents does not change this. Asserted.

4. **One parent can block, and the exceptions are narrow.** The family-crisis exception
   needs the non-consenting parent to be unreachable within a reasonable period. A
   reachable parent who refuses keeps the bar. A family violence order against that
   parent is a special circumstance (Determination s 10(3)(f)). It falls away if the
   Minister has court documents showing proceedings that may affect the child's travel
   or parental responsibility (s 10(2)). Asserted.

5. **At 75 the Determination says 5 years, and its own note says 5 or 10.** Item 4 of
   the s 17 table caps a passport issued to a person "75 or over" at 5 years. Note 1
   says such a person "may pay for a 5 year passport or a 10 year passport". The Fees
   Determination charges $398 for the 10-year one (item 1). The encoding follows the
   table for validity (`up to` 5) and the note for which fee may be paid. Asserted on
   both readings.

6. **A request under s 13 lets the Minister refuse, too.** The naive encoding listed
   the discretionary requests as those under ss 14 and 16. s 13(2) ("the Minister may
   refuse") belongs with them. Asserted.

7. **Chloe's 2011 application is not governed by this Determination, nor perhaps by
   this s 11.** Determination s 31 keeps the 2005 Determination for applications lodged
   before its repeal, and the 2015 Determination commenced on 1 Oct 2015. The deposited
   fee compilation gives amounts only from 2024. s 11 was amended in 2015 (No 122,
   2015). c013 is therefore answered on the text deposited, and her fee is "not set by
   the deposited edition". Asserted.

8. **The fees never fall, and an overseas child pays $87 more.** Under Fees
   Determination s 5(1)(b)(i), a year whose indexation factor is below 1 keeps the
   previous year's fee. The overseas fee is $178 for an adult and $87 for a child, and
   a 16- or 17-year-old pays the child rate "regardless of the period of validity".
   Asserted, except the 16-17 rate.

9. **The fee for an application not processed is kept, though the Determination
   allows refunds.** s 19A(2) says the fee "is not refundable". Determination s 28(2)
   lets the Minister refund "a fee" in exceptional circumstances. The Act should
   prevail (an inference). Refunds are not encoded. Not asserted.

10. **Issuing a passport to a child cannot be reviewed; refusing to waive a fee can.**
    s 48(a)(ii) excludes the issue to a child. s 48(b) excludes a refusal after a
    s 11(3) declaration, and a refusal because of s 12(2). s 48(i) makes a refusal to
    waive reviewable. Asserted.

11. **A married 17-year-old needs no-one's consent, and read literally, the two
    "parent" limbs of s 11(5) are alternatives.** A married 17-year-old is not a
    "child" (s 6(1)). Under s 11(5), a parent loses parental responsibility for passport
    purposes only when orders under both the Family Law Act 1975 and the Family Court
    Act 1997 (WA) have removed it. Asserted.

12. **After a refusal/cancellation request, only the "exceptional circumstances" waiver
    is barred.** Determination s 28A excludes s 27(1)(l), s 27(2) and s 28. The other
    waiver grounds, such as (a) and (k), remain. Asserted for (l).

13. **The fee indexation factor is a ratio of two CPI years, to three places.** Fees
    Determination s 7(1), from the sidecar: index number for the most recent September
    year / index number for the past September year, each the sum of four quarterly All
    Groups CPI numbers; (2) works it to 3 decimal places, rounding up from 5. Illustrative
    sums of 552.2 and 534.0 give 1.034. Asserted.

## What would need doing before this is worth anything

- Retrieve the s 11 text in force in June 2011 and the Australian Passports
  Determination 2005, and re-run c013 against them.
- Deposit the CPI index numbers (the s 7 formula is now in hand), so that the fees for
  2025 onward are amounts, not inputs.
- Retrieve the fee amounts in force in 2011 and 2016.
- Join this encoding to the citizenship baseline, so that the date of Anjali's approval
  decides s 8 instead of an input.
- Check the s 11(5)(a)/(aa) reading against the Family Law Act 1975 and the Family
  Court Act 1997 (WA).
- Settle the 75-and-over tension (finding 5) against departmental practice.
- No case law was searched.
