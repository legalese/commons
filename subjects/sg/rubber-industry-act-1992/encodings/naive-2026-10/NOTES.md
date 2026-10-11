# Rubber Industry Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/RIA1992.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amending Act annotated in the body is 40/2019 (s 13(1)).
The arrangement of sections at the top of the deposit is one number out of step with
the body; the encoding follows the body.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0117**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act is short (28
sections), so the row takes the whole licensing regime as a trader meets it:
ss 2-4, 6, 7, 10-12, 20, 22-24. Not encoded: the Board's market and arbitration
powers (s 14), Ministerial directions (s 15), entry and seizure (ss 16, 17), immunity
(s 18), the Rubber Fund (s 19), prosecution machinery (ss 21, 25), the Tribunal's
constitution (s 13), regulations and by-laws (ss 26, 27). Licence fees and conditions
are prescribed by regulations that were not retrieved. The s 28 exemption is a bare
input.

## What the Act turns out to say

### 1. Two appeal routes, two clocks, and only one can be extended

Refusal to grant a licence (s 4), new or varied conditions (s 5) and refusal to renew
(s 6) go to the **Minister**, within "one month of being notified", and the
Minister's decision "is final" (s 7). Revocation, suspension, a Board fine, a
security deposit, a warning or a costs order (s 11(1)) go to the **Appeal Tribunal**,
within **14 days** of receiving the notice (s 12(2)); the Tribunal "may extend any
limit of time" (s 12(7)). Nothing in s 7 allows the Minister's month to be extended.
So an appeal against revocation lodged on day 20 is late unless extended, though it
would have been in time against a refusal to renew. Asserted.

### 2. The Board can fine $25,000 itself, the same as the criminal maximum

Operating without a licence carries on conviction a fine up to $25,000 or 2 years
(s 3(3)), and needs the Public Prosecutor's consent to try (s 22). Against a
*licensee*, s 11(1)(d) lets the Board impose its own fine "not exceeding $25,000,
which is recoverable in the same manner as a judgment debt", plus a deposit or bank
guarantee up to $25,000 and a costs order up to $5,000, after a hearing (s 11(2)).
Execution is stayed while the 14-day appeal window runs or an appeal is pending
(s 11(4)). Asserted (caps, the hearing condition and the stay).

### 3. A past breach alone does not trigger s 11

The Board must be satisfied the licensee "is contravening, or has contravened and is
likely again to contravene". A finished breach not likely to recur does not open
s 11 (it may still be ground to refuse renewal under s 6(2)). Asserted.

### 4. Malaysian shipping licences count, but only for shipping and only with reciprocity

s 3(4) disapplies the licensing requirement for a person who **ships** rubber for
export under a Malaysian Rubber Board licence, and s 3(5) keeps that alive only "so
long as reciprocal arrangements exist". It does not cover packing, dealing, treating
or storing. Asserted.

### 5. Sole traders must be registered; dishonest managers bar a company

The Board "must refuse" an applicant without satisfactory evidence of being fit and
proper, or where the applicant or a company officer "holding a managerial or executive
position" has a conviction for dishonesty, fraud or moral turpitude, or on public
interest (s 4(3)). A non-incorporated person may not be licensed unless registered
under the Business Names Registration Act 2014 (s 4(4)). Asserted. Licences run one
year at a time (s 4(2)); encoded as a constant, not asserted.

### 6. Gaps the text leaves

- Futures trading and manufactured rubber goods are outside the Act: "deal" excludes
  commodity futures contracts, and "rubber" excludes "any manufactured article made
  wholly or partly of rubber" (s 2). Asserted.
- The s 10(1) inspection duty lists packing, dealing, treating, storing and
  manufacturing technically specified rubber, but not **shipping** for export, though
  s 9 (display of licence) includes shipping. Asserted.
- The duties to display the licence (s 9) and to comply with conditions (s 5(3)) are
  not stated to be offences, and s 23(1)'s general penalty ($5,000 or 3 months) applies
  only to an offence "for which no penalty is expressly provided". Whether breaching
  them is an offence at all is not answered by the Act; the encoding does not assert
  it either way. Breach of conditions is a s 11 ground.
- s 6(1) says a renewal application "must be made ... one month before the expiry";
  reading that as "at least one month before" is an inference.
- s 2 spells the Para rubber plant "Heavea brasiliensis" (sic), as deposited.

## What would need doing before this is worth anything

- The Rubber Industry Regulations (fees, conditions, compoundable offences) were not
  retrieved.
- Whether the s 3(5) reciprocal arrangements with Malaysia still exist is a fact the
  text cannot answer.
- The Tribunal's power to extend time is modelled only as an input; its effect on the
  s 11(4) stay is not.
- No case law was searched.
