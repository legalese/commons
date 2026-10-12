# Presbyterian Church of England Mission Ordinance 1903 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PCEMO1903.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 6;
the legislative history ends with Act 7 of 1997 (Statutes (Miscellaneous Amendments)
Act 1997, in force 1 October 1997).

**Checks:** one module (`pcemo-corporation.l4`), one case file
(`pcemo-cases-corporation.l4`), 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0242** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has six sections, so this row takes all of them except
the short title (ss 2-6), together with the term, rent and purpose of each parcel the
preamble recites, since s 5 vests "each of the pieces of land mentioned in the
preamble". For someone outside the Mission it matters when buying, leasing or lending
against the Corporation's land, and for title to those parcels.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact here), the
other conditions of the recited leases and grants, and the internal governance of the
Foreign Missions Committee.

## What the Act turns out to say

### 1. A successor is not the Corporation until the Gazette says so — and the Gazette proves more than the steps behind it

s 4(1): no successor "shall be deemed to be duly qualified" until an extract of the
Foreign Missions Committee's minutes appointing him, "certified as correct by the
Convenor", has been filed "in the office of the Minister", and "a notification of
such filing has appeared in the Gazette". All four steps are required; a successor
filed but not gazetted is not the Corporation. Yet s 4(2) makes the notification
"sufficient evidence of the appointment and that the person named therein is duly
qualified", so a notification issued on an uncertified extract is still sufficient
evidence of qualification. "Sufficient", not "conclusive". Mr Cook, named in s 2(1),
needed none of the steps. Asserted.

### 2. The Ordinance gives no power to sue or be sued

s 2(3) lets the Corporation acquire and hold property of every description, and sell,
mortgage, demise or otherwise dispose only of property "vested in the Corporation".
Unlike the Bishop of Singapore Ordinance 1911, it says nothing about suing or being
sued. Whether the general law supplies that capacity is outside the text. Asserted
(the Ordinance empowers no such thing).

### 3. Signing proves due sealing, even when the sealing was wrong

s 3(1) requires the seal to be affixed in the presence of Mr Cook, his successor, or
an attorney under a power "deposited under section 48 of the Conveyancing and Law of
Property Act 1886", and signed by one of them. s 3(2): "Such signing shall be
sufficient evidence of the due sealing". A mortgage sealed before a church elder but
signed by a qualified successor fails s 3(1), yet its signature is sufficient
evidence of due sealing. An attorney with an undeposited power cannot execute.
Treating a successor not yet gazetted as unable to execute is a reading of ss 2(1)
and 4 together; s 3 itself does not repeat "duly qualified". Asserted.

### 4. Two of the seven parcels were leases that, on the preamble's own figures, ran out in 1939

s 5 vests each parcel "for an estate in fee simple, or for the residue of the term of
years under which the same is held, as the case may be, free from all trusts
whatever". The Prinsep Street leases Nos. 241 and 242 were made in 1840 "for the terms
of 99 years", so (by arithmetic, not by any words of the Ordinance) the residue vested
in 1903 ended in 1939. Leases Nos. 1646 and 1918 were for 999 years, from 1880 and
1885, running to 2879 and 2884. The two Statutory Land Grants "for ever" and the
Kallang allotments are treated as fee simple; for the grants that is an inference from
"for ever". The preamble's "20 several allotments" at Kallang matches its lot ranges
(114-128 and 149-153: 15 + 5). Asserted.

### 5. "Free from all trusts" does not, on this reading, free lease No. 1646 from the Government's reverter

Lease No. 1646 (Upper Tanglin) was granted on condition that it be used for the
Chinese Mission and "should it be used for any other purpose it would revert to
Government". s 5 strips trusts; s 6 provides that nothing in the Ordinance "shall
affect the rights of the Government". The encoding treats the reverter as surviving.
That is an inference from ss 5 and 6 together. Asserted.

### 6. The saving clause does not save the people the Ordinance names

s 6 saves the rights of the Government and of other persons "except those mentioned
in this Ordinance, and those claiming by, from or under them". The preamble mentions
the London Missionary Society, the Foreign Missions Committee, and the Kallang vendors
Foo Teng Quee and Ong Sam Leong, so their rights, and the rights of anyone claiming
through them, are not saved. The Government is read as saved regardless, because it is
named first and separately; that is a reading of the punctuation. Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- The recited leases and grants were not retrieved; only the terms the preamble states
  are encoded, and whether the purpose restrictions on Grants Nos. 2675 and 3772 are
  Government rights saved by s 6 is not decided here.
- No Gazette notifications of later Senior Missionaries, land-title records, or later
  legislation (for example any transfer of these lands to a successor church body)
  were searched; whether the Corporation still holds any of the parcels is unknown here.
- The evidential effect of "sufficient evidence" in ss 3(2) and 4(2) against contrary
  proof is not modelled.
