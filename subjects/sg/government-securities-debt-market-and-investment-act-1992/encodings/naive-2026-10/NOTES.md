# Government Securities (Debt Market and Investment) Act 1992 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021". The text also carries
annotations for Act 35 of 2021 (wef 31 January 2022) and, the latest annotated,
Act 5 of 2022 (wef 21 February 2022), which added Part 3A (RMGS). The deposit's
metadata records it as the current version as at 1 October 2026.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0113** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

Most of the Act is the Government's own plumbing: the Government Securities Fund
and its accounting (ss 3 to 10, 12, 13, 15, 15C), securities lending (s 11A) and
the Authority's record-keeping (ss 18, 22). Those are not encoded. This row takes
what a holder, depositor, pledgee or dealer meets: which instruments count as
"Government securities" (s 2), the two ceilings (ss 11, 15A), transfers and pledges
of book-entry securities (ss 18A, 19, 20(4), 21), interest and redemption (ss 23,
24, 24A), advance deposits (ss 27, 28), and primary dealers (ss 29A, 29B(4), 29D,
29E, 29F) with the offence ceilings for regulations (s 31(3)). Directions to
dealers (s 29C), the s 29D(3) financial-penalty formula (in a Gazette notification
not deposited) and the regulations themselves are not encoded.

## What the Act turns out to say

### 1. Only a record at the Authority wins; a transfer made any other way loses, whatever its date

s 20(1) lets book-entry securities be transferred or pledged "by any means" that
would work for certificated securities. But s 19(3) gives a transfer or pledge
made by entry in the Authority's records priority over any other transfer, pledge
or interest "effected or created in any other manner before, on or after the
date" of the entry. And s 20(4) says the Authority must not accept notice of a
transfer or pledge made otherwise, and any such notice "is void". A lender who
takes a pledge off the Authority's books cannot protect it by telling the
Authority. Asserted.

### 2. The Authority is not liable for following a depositor who had no right

s 21(1): the Authority "is not liable for conversion or for participation in any
breach of fiduciary duty" where it acted on its depositor's instructions "even if
the depositor had no right to dispose of" the securities; s 21(2) fully
discharges it. (Inference, not stated: the person with the real right must look
to the depositor, not the Authority.) Asserted.

### 3. Treasury Bills and RMGS are not "Government securities"

s 2 defines Government securities as instruments issued under the Act "other than
any Treasury Bill and any RMGS". So the half-yearly interest rule (s 23) and par
redemption (s 24) do not reach Treasury Bills; the Act leaves their terms to the
regulations and the Minister (s 14(b)). RMGS are redeemable at par (s 15B(1)) but
may be issued only to the Monetary Authority (s 15A(5)) and are not transferable
without the Minister's consent (s 15B(2)(a)). Asserted.

### 4. Interest stops at maturity, demanded or not; early redemption is a right only if the bond says so

s 24(3): after maturity all interest "ceases and determines, whether or not
payment of the principal sums has been demanded". A holder-redeemable security is
redeemed on the earlier of maturity and the date in a duly served notice
(s 24(1)(b)), with pro-rata half-yearly interest (s 23(2)). Otherwise early
redemption is only by invitation under s 24A, and the Authority "may refuse any
application ... without giving any reason" (s 24A(3)); the same is true of
applications to buy (s 30(2)(b), not encoded). The pro-rata basis is not stated;
days elapsed over days in the half-year is an inference. Asserted.

### 5. Dealing for others without appointment is a serious offence

s 29A(6): carrying on, or holding oneself out as carrying on, the business of
applying to buy or offering to redeem Government securities, Treasury Bills or
public debt securities on behalf of another person, without being a primary
dealer, is punishable by up to $125,000 or 3 years or both for an individual
($12,500 a day continuing), and up to $250,000 for others ($25,000 a day).
Failing an inspection requirement without reasonable excuse (s 29F(6)) is up to
$50,000 or 2 years ($5,000 a day). Regulations may be backed by up to $12,500 or
12 months for individuals and $25,000 otherwise (s 31(3)). Regulations may exempt
institutions from Part 7A (s 31(1)(g)). Asserted.

### 6. Tight clocks for dealers: 28, 21-28, 21 and 14 days

Before varying a dealer's conditions the Authority must allow at least 28 days
for representations, unless it considers that impracticable or undesirable
(s 29B(4)). Before any cancellation, suspension or penalty order the dealer must
be given a hearing period of at least 21 and at most 28 days (s 29D(5)). An
order does not take effect until 21 days after service, except a reprimand, which
takes effect on service (s 29D(7), (9)). Appeal lies to the Minister within 14
days, but not against a reprimand, and the Minister's decision is final
(s 29E(1)); only a cancellation is stayed pending appeal (s 29E(2)). Suspension
is capped at 6 months (s 29D(2)(a)). Reading "until the expiry of 21 days" as
effect from day 22 is an inference. Asserted.

### 7. The ceilings: $1,065 billion of borrowing, $580 billion of RMGS

s 11(2) forbids a loan if outstanding Government securities and Treasury Bills
would exceed $1,065,000,000,000, and s 15A(2) caps unredeemed RMGS at
$580,000,000,000, each unless Parliament resolves a higher amount with the
President's concurrence. Asserted (in billions).

### 8. Advance deposits

Interest runs from the day the deposit is effectively received, or the next
working day if a cheque cannot clear that day (s 27(2), (3)); repayment needs at
least 2 working days' notice (s 27(6)). Any power to invest is deemed to include
power to make advance deposits unless a contrary intention appears (s 28).
Asserted.

## What would need doing before this is worth anything

- The regulations made under s 31 (terms of issue, applications, primary dealer
  duties) and the s 29D(3) penalty formula were not retrieved; most of what a
  retail investor's bond actually says lives there.
- Savings Bonds and other retail products were not traced to this Act; the text
  deposited does not name them.
- Directions to primary dealers (s 29C) and the representation procedure in
  s 29B(5), (6) are not encoded.
- No case law or MAS guidance was searched.
