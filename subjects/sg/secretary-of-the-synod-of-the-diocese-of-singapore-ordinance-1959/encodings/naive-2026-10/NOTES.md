# Secretary of the Synod of the Diocese of Singapore Ordinance 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SSDSO1959.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 6.
The Ordinance is dated 26 March 1959.

**Checks:** one module (`ssd-corporation.l4`), one case file
(`ssd-cases-corporation.l4`), 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0250** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections and a Schedule, so this row takes all of
it except the short title and the recitals (ss 2-6 and the Schedule). For someone
outside the Synod it matters when buying, leasing or lending against the
Corporation's land, when suing it or being sued by it, and for title to the twenty
church sites in the Schedule.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here); the
Bishop of Singapore Ordinance 1911, under which the scheduled lands were held before;
the lot numbers and areas in the Schedule (only the estate in each item and the terms
of its two leases are encoded); the Synod's own rules for appointing its Secretary.

## What the Act turns out to say

### 1. The Schedule still lists a lease that, on its printed term, ended in 1976

Item 11 (St. Matthew's School and Parsonage, 184 Neil Road, T.S. 23 lot 145-12) is
"Leasehold No. 4841 for a term of 30 years from 1-1-1947". Thirty years from 1 January
1947 runs to the end of 1976. The 2020 Revised Edition reprints it unchanged. s 5(2)
vests the land only "for the respective estates, rights and interests for which the
same are held", so the Ordinance gave the Corporation no more than that lease. That
the lease has ended is arithmetic on the Schedule's own figures plus general law; the
deposit says nothing about renewal. The other lease (item 1, lot 20-4 at St. Andrew's
Cathedral) is "for a term of 999 years from 10 November 1951". Asserted (year by year,
boundary years not asked).

### 2. The signatures prove due sealing even without the Standing Committee's resolution

s 3(1) forbids fixing the seal "except by the authority of a Resolution of the
Standing Committee" and "in the presence of a member of the Standing Committee duly
authorised as witness in that resolution". s 3(2) adds sealing before the Secretary or
an attorney under a power deposited under s 48 of the 1886 Act, and signature by that
person and by the authorised witness. s 3(3) then makes "such signing" "sufficient
evidence that the said seal was duly and properly affixed". So a transfer sealed with
no resolution at all, or while the witness was out of the room, fails s 3 yet carries
sufficient evidence that it passed. Reading "such signing" as both s 3(2) signatures
is an inference from "such". "Sufficient", not "conclusive". Asserted.

### 3. The Corporation may sue and be sued on anything, not just its property

s 2(4): "The Corporation may sue or be sued in respect of its property and otherwise
in all courts of justice." The words "and otherwise" set it apart from the Bishop of
Singapore Ordinance 1911, whose Corporation may sue and be sued only "in respect of
such property". Disposal is narrower: s 2(3) allows selling, mortgaging, demising and
so on only of property "vested in the Corporation" and "upon such terms as to the
Standing Committee ... seem fit", with the Standing Committee's minutes "sufficient
evidence of such terms". Treating that as requiring the Standing Committee to have
approved the terms is an inference from the words. Asserted.

### 4. A new Secretary is not the Corporation until the Gazette says so

s 2(1) makes Roland Keith Hudson "and his successors ... duly qualified as hereinafter
provided" the Corporation. s 4(1): no successor is "duly qualified" "unless and until"
an extract from the Synod's Minutes appointing him, certified by the Bishop of
Singapore (or "in his absence a Commissary appointed by the Bishop or the Archbishop of
Canterbury during a vacancy in the See"), is published in the Gazette. s 4(2) makes
publication "sufficient evidence" of appointment and qualification, so a gazetted
person never appointed, or certified by the wrong person, has the evidence without
the qualification. The 2020 Revised Edition still names Hudson, the 1959 Secretary.
Asserted.

### 5. Who may certify is grammatically open

"A Commissary appointed by the Bishop or the Archbishop of Canterbury during a vacancy"
may mean a Commissary appointed by either (encoded: the Bishop's Commissary when the
Bishop is absent, the Archbishop's Commissary when the See is vacant), or may let the
Archbishop certify in person during a vacancy. The first reading is encoded; under it
the Archbishop certifying in person does not qualify the successor. This is a fork the
text does not settle. Asserted under the encoded reading.

### 6. Only scheduled land moved, and everyone else's rights are saved

s 5(1) divests the Bishop of Singapore of the lands in the Schedule; s 5(2) vests them
in the Corporation "as trustee for the Synod of the Diocese of Singapore". Land the
Bishop held that is not scheduled stays where it was. s 6 saves the rights of "the
Government, all bodies politic and corporate, and all others except such as are
mentioned in this Ordinance and those claiming by, from or under them". Asserted.

### 7. The Schedule table is column-shifted in the deposit

The estates were matched to items by order. Item 20 is "Pt. Grant No. 67", which
says neither freehold nor leasehold, and is encoded as "part of a grant". Item 10
prints two figures in the area column, "614.7" and "68,644.8", against lots 460-2 and
460-3; which area belongs to which lot is not certain from the text extract and areas
are not encoded. Item 5's area, "1,392", and item 7's, "647", carry no decimal, unlike
the rest. Estates asserted for items 1, 5, 11, 12, 20 and a non-item.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- The PDF of the Schedule should be checked against this text extract, especially
  items 10, 18 and 20, before any area or lot is relied on.
- No Gazette notifications, land titles or later legislation were searched: whether
  the item 11 lease was renewed or the land was otherwise dealt with is unknown here,
  as is who the current Secretary is.
- The evidential effect of ss 2(3), 3(3) and 4(2) ("sufficient evidence") against
  contrary proof is not modelled.
- The certifier fork in s 4(1) (finding 5) needs a reader with the Synod's practice.
