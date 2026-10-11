# Government Contracts Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, deposited at
`../../registers/source-bundle/GCA1966.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021; the SSO metadata calls it the current version as at 1 October 2026.
The latest amendment annotated in the body is [5/2018] (s 2(3), by the Public Sector
(Governance) Act 2018, in force 1 April 2018).

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0115** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Act has six sections, so the row covers all of it: ss 2 to 5 and
s 6(1). Left out: the short title (s 1), the s 6(2) saving for written law on State
land, what "in accordance with ... the Constitution" requires (taken as a given
fact), the general law of agency and ostensible authority (which the Act does not
mention), and whether s 2 also applies to a grant or lease that s 6(1) governs.

## What the Act turns out to say

### 1. A contract not made under the Act does not bind the Government at all

s 4: "No contracts, made after 15 March 1967, shall be binding upon the Government,
unless entered into in accordance with this Act and the Constitution." For a
business, the consequence of dealing with the wrong signer is not a defect to be
cured but no binding contract. A contract made on or before 15 March 1967 is outside
s 4 altogether; the Act neither bars nor validates it. Asserted.

### 2. A general authorisation stops strictly below its value, and the Act sets no value

s 2(1): a public officer may sign if authorised in writing by the Minister for
Finance "specially in any particular case, or generally for all contracts below a
certain value". A contract exactly at the limit falls outside a general authorisation,
and so (via s 4) does not bind. The figure is the Minister's, not the Act's. A
Minister may sign without any authorisation. Asserted.

### 3. The officer you dealt with is shielded, unless he pledged his own credit

s 5: no public officer "shall be liable to be sued personally upon any contract which
he makes in that capacity", but he is personally liable where he "expressly pledges
his personal credit" or contracts "otherwise than as the agent of the Government".
The Act does not say what remedy the other party has where the contract fails under
s 4 and the officer is shielded under s 5; that is left to the general law, which is
not encoded. Asserted (the s 5 rule only).

### 4. Contracts made abroad: any authorised "person", no value limit, and only within the Singapore courts' reach

s 3 deems contracts made outside Singapore by "a person either generally or
specially authorised in writing" by the Minister for Finance to be Government
contracts "so far as they come within the jurisdiction of the courts in Singapore".
It names a person, not a public officer, and attaches no value ceiling to a general
authorisation, so a private agent generally authorised can make a contract above any
limit. It does not mention Ministers. INFERENCE (not in the text): that s 3 is the only
route by which a contract made abroad is "in accordance with this Act", so that a
Minister signing abroad without the Minister for Finance's written authorisation
makes a contract s 4 does not let bind the Government. Asserted, as an inference.

### 5. Oral contracts escape the s 2 formalities

s 2(1) requires the Government's name and an authorised signer only "if reduced to
writing". INFERENCE: an oral contract made in Singapore is therefore "in accordance
with this Act" whoever made it. Asserted, as an inference.

### 6. Seconded staff count; other statutory board staff do not; State land needs a Collector

s 2(3) (added in 2018) deems a statutory body employee seconded to the Government a
public officer during the secondment, so he can be authorised; an employee who is not
seconded cannot. s 2(2) lets the Minister name the office rather than the person, and
Gazette publication is optional ("may"). s 6(1): grants and leases of State land, and
Foreshores Act 1920 leases, "shall be signed by a Collector of Land Revenue", not a
Minister or an officer authorised under s 2. Asserted.

## What would need doing before this is worth anything

- The two inferences (findings 4 and 5) need checking against case law on s 4 and its
  Malayan predecessor (the 1949 Ordinance named in the legislative history); none was
  searched.
- The interaction of ss 4 and 5 with the general law of agency and restitution,
  and with any other written law on suing the Government, is not encoded.
- No Minister for Finance authorisation instrument was retrieved, so no actual value
  limit is known.
