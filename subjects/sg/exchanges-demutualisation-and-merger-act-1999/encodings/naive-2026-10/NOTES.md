# Exchanges (Demutualisation and Merger) Act 1999 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
21/3/2022 to 20/10/2026), deposited at `../../registers/source-bundle/EDMA1999.txt`.
The revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated in the body is Act 4 of 2022, in force 21 March 2022.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0112** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is a one-off transitional statute that merged SES, SIMEX and SCCS under a
holding company on 1 December 1999. This row takes what the old members and
seat-holders received (s 6), the share cancellation and re-creation and the
30-day notice (ss 3(1), 4, 5), the requirements the offer and issue escape
(ss 4(5), 8(3), 8(4), 9), what the special purpose company may do with its
shares and their proceeds (ss 8(1A), 8(2), 10, 11) and the deemed Trustees Act
track record (s 12). Not encoded: the recitals, the Minister's designations
(s 3(2)), the transfer of assets (s 7), and the Minister's choice of share value
and offer size, which are taken as inputs. No Gazette notification or Minister's
notice was retrieved.

## What the Act turns out to say

### 1. The liquidation exception takes away shares, not seats

s 6(1) and (3)(a) exclude shares held by an SES or SIMEX shareholder "in
involuntary liquidation as at 4 November 1998" (s 6(1) names Associated Asian
Securities (Pte) Limited). s 6(3)(b), the $170,000 per SIMEX seat, has no such
exception. A liquidated SIMEX shareholder that also owned a seat still received
the seat's value. Asserted.

### 2. One SES share was worth $6 million; a SIMEX seat was worth more than a SIMEX share

s 6 gives $6 million in holding company shares for each SES share, $115,000 for
each SIMEX share and $170,000 for each SIMEX seat. s 4 records that 34 SES shares
and 40 SIMEX shares were in issue, so (by arithmetic, not stated in the Act) the
SES shareholders' total was at most $204 million and SIMEX shareholders' $4.6
million; the number of seats is not given. No fraction of a share could be
allotted (s 6(2), (4)); that the count is rounded down is an inference. Asserted.

### 3. The special purpose company can never vote its shares

s 11(2)(b): it must "not exercise or control the exercise of the votes" attached
to the shares. Unlike disposals and charges (s 11(2)(c)) and rights issues or
scrip dividends (s 8(1A)), no Minister's approval lifts this. A sale on the
Minister's s 8(2) direction needs no further approval because it is "otherwise
permitted under this Act". Shares it took up under s 8(1) or (1A) are ignored for
take-over thresholds (s 11(1)). Asserted.

### 4. The trustee deeming runs out after the first two years

s 12 deems the holding company to meet the old Trustees Act tests (equity of $30
million, dividends in each of the relevant 3 years, a profit in the preceding
year) for the years before and including the first investment year. Because "the
relevant 3 years" roll forward, an investment two years later already needs a
real dividend and a real profit in the year after the first investment year, and
one four years later needs three real years. s 12 applies the Schedule "as in
force immediately before 15 December 2004"; whether that still matters to any
trustee the deposit does not say. Asserted.

### 5. The prospectus exemptions are not the same for every issue

s 8(3) lifts the Securities and Futures Act prospectus requirements only for the
single offer to the special purpose company and its later sales; s 9 lifts the
Companies Act statement in lieu of prospectus for issues under s 6 or 8. The s 6
allotment to members is covered by s 9 but not by s 8(3). The s 4 reduction needs
no special resolution (s 4(5)). Asserted.

### 6. The arrangement of sections is one line out of step

The deposit's arrangement lists "2. Short title", "3. Interpretation" and so on,
one ahead of the body; and the commencement note refers to "sections 19(a), (b)
and (c) and 20(d) ..." though the revised edition has only 13 sections. This row
follows the body. Not asserted.

## What would need doing before this is worth anything

- The Gazette notifications under ss 3(2), 6(5)(a) and 7(2) and the Minister's
  notices under s 8 were not retrieved; the share value and offer terms are inputs.
- The Trustees Act 1967 Schedule as in force before 15 December 2004, and its
  other conditions, were not read.
- No question has yet been put to this Act by a scenario; the scope is a guess at
  what a former member, a trustee or the special purpose company would ask.
