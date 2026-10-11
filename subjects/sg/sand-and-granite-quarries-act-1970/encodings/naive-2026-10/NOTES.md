# Sand and Granite Quarries Act 1970 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SGQA1970.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on 31 December
2021; the latest amendment annotated in the text is Act 5 of 2025 (wef 9 March 2025),
on the Licensing Officer (ss 2, 3).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0118**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act has 24 short
sections, so the row covers nearly all of it: ss 2, 4, 5, 7, 8, 9, 10, 12, 14, 16 to
20, 22 and 23. Not encoded: the appointment of the Licensing Officer (s 3), security
(s 6) beyond its use to recover expenses, the direction powers on waste, safety and
blasting (ss 11, 13) beyond their enforcement through ss 17 and 18, the power of
entry (s 15), the saving of other prosecutions (s 21) and regulations (s 24). No
regulations, fee schedule or exemption order was retrieved.

## What the Act turns out to say

### 1. A sand quarry needs manual labour; a granite quarry does not

s 2 defines a "granite quarry" by extraction "whether the processes are executed by
manual labour or mechanical means", but a "sand quarry" as land "on which persons are
employed in manual labour" in getting or preparing sand, gravel or earth. On the
words, a sand pit worked without anyone employed in manual labour is not a sand
quarry, and the licence requirement in s 4 does not reach it. Whether a machine
operator counts as "employed in manual labour" the text does not say; the encoding
takes it as a given fact. Asserted.

### 2. Every refusal is unreasoned, and some decisions cannot be appealed at all

s 5(2) lets the Licensing Officer grant, renew or refuse "without any reason ... being
assigned", and suspend or revoke on breach of a condition "without compensation and
without notice". s 5(8) gives an appeal to the Minister, final, within one month,
but only against a refusal to grant or renew, a suspension or a revocation. Nothing
in the text gives an appeal against the conditions attached to a grant or a refusal
of consent to transfer (s 5(6)). Asserted.

### 3. Discretion to refuse, duty to refuse

A licence is never a right (s 5(1)), but three things bar a grant: an applicant who
refuses information "shall" be refused (s 5(3)); a granite licence needs a site plan
certified by the Chief Surveyor (s 5(7)), a sand licence does not; and the Licensing
Officer must be satisfied the quarry is unlikely to cause nuisance or damage to
neighbours, to depreciate neighbouring value or amenity, or to endanger health, life
or property (s 8). A licence runs for at most 12 months unless it expressly provides
otherwise (s 5(4)). Asserted.

### 4. The penalties are small, and a notice default carries no daily fine

Unlicensed quarrying is $5,000 plus $100 a day continuing after conviction (s 4(2)).
Most other offences are $1,000 plus $50 a day (ss 9(2), 14, 18). Obstructing an
officer is $1,000 or up to one year in prison, the only imprisonment in the Act
(s 16); read literally, "or" means not both. Defaulting on a notice, order or
direction is $1,000 under s 17(1) with no daily sum, and since that penalty is
"expressly provided", s 18's daily sum does not reach it (a reading, not stated in
terms). Attempts and abetments carry the same punishment (s 19). Asserted.

### 5. Who owns the machines is presumed to run the quarry

In a prosecution under s 4, sand apparatus on land is prima facie evidence that its
owner or controller uses the land as a sand quarry, and granite extraction equipment
the same for a granite quarry (s 4(3)). The presumption falls on the equipment's
owner or controller, not the landowner. Asserted.

### 6. The licensee answers for anyone who appears to work there, and the landowner for an abandoned pit

s 20 makes the licensee liable to the same pecuniary penalty for an agent's or
servant's act in the course of the business, deems anyone who "appears to be
employed" at the quarry a servant, and states no due-diligence defence. A disused
quarry dangerous to the public must be kept reasonably fenced; if there is no
licensee, the owner of the land commits the offence (s 14). Unpaid costs of works the
Licensing Officer does in default (ss 7, 9) may be taken from the security or, unpaid
7 days after demand, recovered as if a fine (s 22(2)). Asserted.

## What would need doing before this is worth anything

- The Sand and Granite Quarries regulations (fees, s 5(5)) and any s 23 exemption
  orders were not retrieved; the Act may now be largely dormant in practice, but that
  is an inference the deposit cannot confirm.
- No case law was searched, including on "manual labour" in s 2 and the reach of
  the s 5(8) appeal.
- The renewal of a licence is not separately modelled against s 8, which speaks only
  of grant.
