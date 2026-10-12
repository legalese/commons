# Roman Catholic Archbishop Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/RCAA1975.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The body carries no amendment annotation. The legislative history
lists Act 42 of 1975 (commenced 12 December 1975) and the 1985 Revised Edition
(Chapter 375). The arrangement of sections at the top of the deposit is one line out
of step with the body (it puts "Short title" against 2); this row follows the body.

**Checks:** one module (`rca-corporation.l4`), one case file
(`rca-cases-corporation.l4`), 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0246** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet. The
Act has seven sections, so this row takes all of them except the short title
(ss 2-7). For someone outside the Church it matters when buying, leasing, lending to
or suing the Corporation, for title to property once held by the Titular Roman
Catholic Bishop of Malacca, and for anyone who contracted with or worked for that
former Corporation.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here), what
"the respective estates and interests" in s 3 amount to, and how a pension or
gratuity is calculated under s 7(2).

## What the Act turns out to say

### 1. A power of attorney dies with its donor's tenure, and a deed signed under it fails

s 2(4): any power of attorney given by the Archbishop, Administrator Apostolic or
Vicar Capitular "shall cease to be valid when the donor ... ceases to administer the
affairs of the diocese". s 4(1) lets an attorney seal and sign only if "duly
authorised" by a deposited power. So a buyer or lender relying on a deposited power
from an Archbishop who has since resigned or died gets an instrument not executed as
s 4 requires. Asserted.

### 2. Who signs depends on whether the see is vacant

s 2(3) deems an Administrator Apostolic or Vicar Capitular a "successor in office"
only from the vacancy "until the formal assumption of office by his successor"; s 4(1)
lets them seal and sign "when the Archbishopric is vacant". A mortgage signed by an
Administrator Apostolic while an Archbishop is in office is not executed as s 4
requires. s 2(4) forbids "concurrent holders of any 2 of the offices" (read here as at
most one office filled at a time; an inference). Asserted.

### 3. The Gazette is conclusive

s 5: a Gazette notification of the appointment of an Archbishop, Administrator
Apostolic or Vicar Capitular "shall be conclusive evidence that such person was duly
authorised to exercise that office in Singapore". Gazettal is evidence, not a
condition of holding office (an inference from the wording). Asserted.

### 4. Movable property passed too, but only property in Singapore

s 3 vests "all movable and immovable properties of every description situate in
Singapore" held by the Bishop of Malacca immediately before 12 December 1975, however
the name was written on the title (with or without the bishop's own name or "resident
in the Straits Settlements"). Property in Malacca does not pass. The 1911 Bishop of
Singapore Ordinance, as quoted in its own naive row, vests only immovable property. Asserted.

### 5. The Corporation's capacities are general

s 2(1) makes it capable of holding and disposing of property, "of suing and being
sued and of performing all such acts and things as bodies corporate may lawfully
perform". Its seal "may consist of a rubber stamp" (s 2(2)). Signing alone is
"sufficient evidence" that the seal was duly affixed (s 4(2)), even if the witness to
the sealing was the wrong person. Asserted.

### 6. Old agreements bind the new Corporation, assignable or not; old staff must agree

s 7(1): every agreement of the former Corporation, "whether in writing or not" and
"whether or not" assignable, has effect as if the Corporation were a party. s 7(2):
an officer or employee transfers only "if that officer or employee so agrees", and
then service is continuous for pension and gratuities. s 7(1) is "subject to
subsection (2)", so employment is encoded under s 7(2) only (an inference). Unfinished
business may be completed (s 7(3)) and all rights and liabilities pass (s 7(4)).
Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is
  a bare fact here.
- The meaning of "concurrent holders of any 2 of the offices" (s 2(4)) is a reading,
  not checked against any authority.
- No case law or Gazette notifications under s 5 were searched.
