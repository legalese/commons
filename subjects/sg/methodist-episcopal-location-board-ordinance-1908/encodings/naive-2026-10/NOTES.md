# Methodist Episcopal Location Board Ordinance 1908 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MELBO1908.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The amendment annotations in the body are "[15/1954]" under
s 2(1), "[15/1954; S(NS) 177/59]" under s 4(1) and "[7/97]" under s 6.

**Checks:** one module (`melbo-corporation.l4`), one case file
(`melbo-cases-corporation.l4`), 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0238** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections and a Schedule, so this row takes all of
it except the short title and the preamble (ss 2-6 and the Schedule). For someone
outside the Church it matters when buying, leasing or lending against the
Corporation's land, and for title to the 25 parcels in the Schedule.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here); the
Schedule's land descriptions, boundaries and areas, and the names in its third column
(whether a person is "specified in the third column" is a stated fact).

## What the Act turns out to say

### 1. s 5 divests executors; s 6, read literally, saves them

s 5(1) divests the persons in the third column of the Schedule "or their executors or
administrators". s 6 then says nothing in the Ordinance affects the rights "of other
person or persons than are specified in the third column of the Schedule". Executors
and administrators are not specified in the third column. Each section is encoded on
its own words: an executor's estate in Schedule land is vested in the Corporation by
s 5, and s 6 says his rights are not affected. The text does not resolve this.
Asserted.

### 2. An appointed Secretary is not the Corporation until the Gazette says so

s 4(1): no successor is "duly qualified" "unless and until" an extract from the
Trustees' minutes appointing him, "certified as correct by the Chairman of the Board",
is filed in the office of the Minister "and unless and until a notification of such
filing has appeared in the Gazette". All four steps are required. s 4(2) makes the
notification "sufficient evidence of the appointment" and of qualification, so a
person gazetted on an uncertified extract, or never appointed, still has sufficient
evidence on his side. "Sufficient", not "conclusive"; contrary proof is not modelled.
"The Board" whose Chairman certifies is not identified; it is read as the Trustees (an
inference). Asserted.

### 3. s 3 does not require the Secretary to be duly qualified

s 3(1) lets deeds be sealed before, and signed by, "his successor for the time being in
the office of Secretary of the Trustees" or a deposited attorney. Unlike s 2(1) it does
not say "duly qualified". On the words, a Secretary appointed but not yet gazetted can
execute a valid deed for a Corporation of which s 4 says he is not yet a member. The
literal reading is encoded. An attorney whose power was never deposited under s 48 of
the 1886 Act cannot execute; a deed sealed before a Trustee but signed by the
Secretary fails s 3(1), yet s 3(2) makes the signature "sufficient evidence of the due
sealing". Asserted.

### 4. No power to sue or be sued

s 2(3) lets the Corporation acquire and hold property "of every description" and sell,
mortgage, demise or otherwise dispose of property "vested in the Corporation". The
Ordinance contains no clause about suing or being sued. Whether the general law of
corporations supplies one is outside the text. Asserted (the Ordinance does not grant
it).

### 5. A Singapore statute still vesting land in Penang and Province Wellesley, on leases long run out

The 2020 Revised Edition keeps all 25 Schedule items: items 1-16 under "LAND IN
SINGAPORE", 17-21 under "LAND IN PENANG", 22-25 under "LAND IN PROVINCE WELLESLEY".
Two leaseholds ran out long before the edition: item 8 (Methodist Girls School,
"99 years from 1 September 1840", ending in 1939) and item 2 (Stamford Road and
Armenian Street, "99 years from 31 January 1859", ending in 1958); the end years are the
encoder's arithmetic. Items 2 and 3 are vested subject to the mortgage of 12 June 1907,
items 17-19 subject to that of 17 May 1907. Asserted.

### 6. The 1954 amendment left two names for one office

s 2(1) still defines the Corporation as Cherry's successors "in the office of Secretary
of the said Board of Building and Location", but gives the Corporation the name "The
Secretary of the Trustees of the Methodist Church in Singapore", and ss 3 and 4 speak
only of the Secretary of the Trustees. The encoding follows s 4 for who is appointed.
Not separately asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- No Gazette notifications, land registers or later legislation (including any
  Malaysian law on the Penang and Province Wellesley parcels) were searched; the
  current state of title to the Schedule land is unknown here.
- The tension between ss 5(1) and 6 over executors, and the s 2(1)/s 4 naming of the
  office, need a lawyer's reading.
- The evidential effect of ss 3(2) and 4(2) ("sufficient evidence") against contrary
  proof is not modelled.
