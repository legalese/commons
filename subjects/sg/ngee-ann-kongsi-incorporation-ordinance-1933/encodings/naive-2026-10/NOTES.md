# Ngee Ann Kongsi (Incorporation) Ordinance 1933 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of the
finished naive rows (the `writing-l4-rules` skill was not available in this session).
No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 April 2022), deposited at `../../registers/source-bundle/NAKIO1933.txt`. The
revised edition "incorporates all amendments up to and including 1 December 2021";
the latest amendment annotated in the body is Act 25 of 2021 wef 01/04/2022
(s 20(1), (2)).

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0240** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

This row takes what an applicant, member, Committee member, buyer or lessee of
Kongsi land, or beneficiary of its donations would meet: membership eligibility and
re-application (s 3(2), (4), First Schedule), eligibility for and expulsion from the
Committee (s 7(11), (13)), who may be President (s 9(1), (2), (4)), the Committee
quorum (s 10(1)), requisitioned extraordinary general meetings (s 13), notice and
quorum at general meetings (ss 14(2), 16(1), (1A)), land dealings (s 20(1), (6)), and
the compulsory donations and ring-fenced sale proceeds (s 20A(1)-(3), (5)).

Not encoded: the recitals and the first Committee (s 8), ex-officio membership
(s 7(2)-(5A)), retirement rotation and the lunar-calendar dates (ss 7(6)-(7), 11(2),
12(1)), casual vacancies (s 7(9), (10)), Honorary Past Presidents (s 9A), Gazette
publication (s 9B), accounts (s 11), records and the seal (ss 17, 18), vesting
(s 19 and the Second Schedule), the court procedure (s 20(2)-(5)), the bank-account
duty and Ministerial powers (s 20A(4), (6), (7)), subsidiaries (s 20B) and rules
(s 21).

## What the Act turns out to say

### 1. Three-quarters of the Kongsi's net income must be given away, mostly to education

s 20A(1): each accounting period the Committee "shall ... set apart 75% of the net
income" and, by the end of the next period, donate 25% to Ngee Ann Polytechnic, 40%
to other educational institutions "as the Minister may approve", and 10% to other
charitable purposes in Singapore. The Minister in question is the Minister for
education (s 20A(8)). On a net income of 800,000, that is 200,000, 320,000 and 80,000:
600,000 in all. Asserted.

### 2. Sale proceeds are ring-fenced, and unspent proceeds become income the next period

s 20A(3): money from selling investment assets or land, or withdrawing investment
deposits, may be used only to buy investment assets or land or make investment
deposits, not even for operating expenses. But under s 20A(2) the net income formula
adds back, as C, the preceding period's proceeds not reinvested by the end of the
current period, so unspent proceeds fall into the 75% donation. The deposit prints
the formula as "A − B þ C"; the "þ" is read as a mis-rendered plus sign (an
inference from the definitions). The ring-fence is asserted; the add-back is encoded
in the formula but its timing is not modelled.

### 3. Christians are kept out of membership by the declaration, not by the section

s 3(2)(a) asks only for age 21, two years' ordinary residence and membership of the
Teochew Community of one of the Eight Districts. Religion comes in through s 3(2)(b),
which requires signing the First Schedule declaration, whose words are "being a
non-Christian". Treating a Christian as unable to make the declaration is an
inference. For the Committee, s 7(11)(a) does say it outright: a candidate must
profess the religions "(other than the Christian religion)" of the community, be 22,
and have been a member for 6 months. Asserted.

### 4. Election to membership is discretionary, and a rejection needs no reasons

Eligibility is necessary but never sufficient: the Committee elects those it "in its
absolute discretion" considers desirable (s 3(1)), "may, but shall not be bound to,"
give reasons for a rejection (s 3(3)), and a rejected applicant must wait until 6
months from the date of his previous **application**, not the rejection, before
applying again (s 3(4)). The re-application wait is asserted. The discretion is
described, not encoded.

### 5. Kongsi land cannot be sold, mortgaged or leased beyond 3 years without the High Court

s 20(1): any sale, exchange, mortgage, lease longer than a tenancy of 3 years, or
other alienation, and any purchase of land out of the Kongsi's funds, needs the
permission of the General Division of the High Court, and the application needs a
prior general-meeting resolution. The Attorney-General may oppose (s 20(4)). A buyer,
lessee or person taking an exchange under the decree holds free of the Ordinance's
trusts, but a mortgagee does not (s 20(6)). Accepting a gift of land is outside
s 20(1) as worded. Asserted.

### 6. The members' levers: 10 signatures, 20 days, 7 clear days, 20 (or 10) present

Ten members, or five Committee members, can requisition an extraordinary general
meeting (s 13(1)). The two thresholds are alternatives and the text gives no way to
combine them, so four Committee members and nine ordinary members are not enough. If
the meeting is not held within 20 days of receipt, the requisitionists may convene it
themselves (s 13(4)). Notice takes "7 clear days" (s 14(2), read as excluding the
days of service and of the meeting, an inference). Twenty members form a quorum, or
any ten once 30 minutes have passed (s 16(1), (1A)). Asserted.

### 7. Officers: aged 25, and no consecutive second term as President or Treasurer

s 9(2): no officer under 25. s 9(4): a person elected President or Honorary
Treasurer "for 2 years" may not hold that office "for the next ensuing 2 years".
Expulsion from the Committee needs two-thirds of those **attending** a specially
called meeting, and is void unless the member was first given an opportunity to
explain (s 7(13)). The Committee's quorum is 7 (s 10(1)). Asserted.

### 8. The first Committee's term ends before the Ordinance was made

s 8 lets the first Committee hold office "until 25 January 1933, or until the second
annual general meeting ... whichever shall be the later date", but the Ordinance is
dated 10 March 1933, so the first limb had already passed. The text is reproduced as
deposited; not encoded.

## What would need doing before this is worth anything

- The Kongsi's rules under s 21 (conditions of membership, method of election,
  student support under s 6(e)) were not retrieved; they may narrow everything above.
- The lunar-calendar deadlines (ss 7(7), 11(2), 12(1)) need a calendar conversion
  before they can be encoded.
- "Clear days" and "after 30 minutes" were read by ordinary usage; no authority was
  checked.
- s 20B (subsidiaries' significant proposals) and the Minister's enforcement powers
  under s 20A(6), (7) are not encoded.
- No case law was searched.
