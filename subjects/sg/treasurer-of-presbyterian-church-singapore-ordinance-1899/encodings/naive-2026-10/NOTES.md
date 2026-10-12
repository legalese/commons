# Treasurer of Presbyterian Church, Singapore Ordinance 1899 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/TPCSO1899.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 8.
The Ordinance is dated 29 December 1899.

**Checks:** one module (`tpc-corporation.l4`), one case file
(`tpc-cases-corporation.l4`), 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0244** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has eight sections and two Schedules, so this row takes
all of it except the short title (ss 2-8). For someone outside the congregation it
matters when buying, leasing or lending against the Corporation's land, and for the
holders of the 31 building leases on the First Schedule land.

Not encoded: the content of s 48 of the Conveyancing and Law of Property Act 1886
(whether a power of attorney was "deposited" under it is a stated fact); the terms of
the 1879 indenture and the 1892 Statutory Land Grant beyond what the preamble recites;
the boundaries in the Schedules (only areas and dates); what "the office of the
Minister of the Colony" in s 4(1) refers to today.

## What the Act turns out to say

### 1. A new Treasurer is not the Corporation until four steps are done, ending in the Gazette

s 2(1) makes Francis Warrack "and his successors ... duly qualified as hereinafter
provided" the Corporation. s 4(1) says no successor is duly qualified "unless and
until" an extract of the Board of Managers' minutes appointing him, "certified as
correct by the Chairman of the Board", has been filed "in the office of the Minister
of the Colony", "and unless and until a notification of such filing has appeared in
the Gazette". So a Treasurer appointed, certified and filed but not yet gazetted is
not the Corporation; nor is one whose extract was never certified, even if gazetted.
s 4(2) separately makes the notification "sufficient evidence" of appointment and
qualification, so a gazetted person is presumptively qualified though on the facts
he may not be. Asserted.

### 2. The 2020 Revised Edition still files appointments with "the Minister of the Colony"

s 4(1) keeps the wording "the office of the Minister of the Colony". The deposit does
not say which office that is now. That it is a revision substitution for a colonial
office is an inference, not something the text says; the encoding treats filing as a
bare fact.

### 3. Execution of deeds, and the gap between s 3(1) and s 3(2)

s 3(1) needs the Corporation's seal, affixed in the presence of the Treasurer or "his
attorney duly authorised by a power of attorney deposited under section 48 of the
Conveyancing and Law of Property Act 1886", and the signature of the Treasurer or
such an attorney. s 3(2): "Such signing shall be sufficient evidence of the due
sealing". So a deed sealed before the Chairman but signed by the Treasurer fails
s 3(1), yet its signature is sufficient evidence of due sealing. An undeposited
attorney qualifies under neither. Asserted.

s 3 speaks of the successor "for the time being in the said office of Treasurer" and
does not repeat "duly qualified". This encoding reads s 3 with s 2(1) and treats a
Treasurer not yet gazetted as unable to execute: an inference, flagged here because
the opposite reading is open on the words. Asserted on that reading.

### 4. The old trustees were removed and the two-trustee minimum overridden

s 5(1) removes "the persons now trustees" of the 14 February 1879 indenture and the
16 August 1892 Statutory Land Grant; s 5(2) appoints the Corporation "sole trustee"
of both "notwithstanding" their provisions against fewer than 2 trustees, and cancels
their powers of appointing new trustees. Asserted.

### 5. Two kinds of estate on two sets of trusts

s 6 vests the First Schedule land (3085.7 m2 at North Bridge Road and 1063.7 m2, both
bounded by "Cross Street, now called Bras Basah Road") "for the respective residues
of the said terms of 999 years", subject to the head-lease rents and covenants and to
"the said 31 indentures of leases", on the trusts of the 1879 indenture. s 7 vests the
Second Schedule land (7208.5 m2 bounded by "Orchard Road, now called Stamford Road")
"for an estate in fee simple" on the trusts of the 1892 Grant. Counting 999 years from
the Schedule's years (1828, 1832) gives 2827 and 2831: arithmetic on the Schedule's
figures, not a date the Ordinance states. Asserted.

### 6. The preamble's reverter and ground rents, and a narrow saving clause

The preamble recites 31 building leases "for terms of 99 years" at "the yearly rent of
$2 on each" (31 x $2 = $62 a year), and the 1892 Grant's proviso that the church land
"should forthwith revert to Her Majesty" if public worship ceases "for the space of 2
years" or the buildings are not maintained or kept in repair for their purpose. These
are recitals, not enactments; that the reverter still binds is an inference from s 7
(trusts of the Grant) and s 8. s 8 saves the rights of the Government and everyone
"other ... than such as are trustees" of the two instruments, so only the old
trustees' rights are touched. Asserted.

### 7. No power to sue or be sued

s 2(3) lets the Corporation acquire and hold property of every description, and
dispose (sell, convey, mortgage, demise, surrender and so on) only of property
"vested in the Corporation". The Ordinance contains no words about suing or being
sued; whether the general law supplies the capacity is not encoded. Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; "deposited" is a
  bare input.
- The 1879 indenture and the 1892 Statutory Land Grant were not retrieved; their trusts,
  sale powers and the reverter are known only from the preamble.
- Whether the 31 building leases (99-year terms; the order of the recitals suggests Dunman
  granted them before the 1879 conveyance, an inference, and no date is given) have expired,
  and whether the First Schedule land is still held by the Corporation, is outside the
  text.
- No Gazette notifications, case law or later legislation were searched; who now holds
  the office, and what "the Minister of the Colony" means today, are unknown here.
- The evidential effect of "sufficient evidence" in ss 3(2) and 4(2) against contrary
  proof is not modelled.
