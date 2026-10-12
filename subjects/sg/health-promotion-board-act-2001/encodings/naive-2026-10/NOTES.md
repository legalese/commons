# Health Promotion Board Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/HPBA2001.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amending Act annotated in the text is Act 11 of 2019
(at s 11(1)); Act 5 of 2018 is annotated throughout.

**Checks:** one module (`hpba-board.l4`), one case file (`hpba-cases-board.l4`),
52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0172** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is institutional. It creates the Board, lists its functions and powers, and
moved five Government departments and their staff into it on 1 April 2001. This row
takes the parts with decision content: who the Board serves and whether that can be
enforced (s 11(1)(g), (3)), what needs the Minister (ss 12(b), (c), 22, 41), terms
and meetings (ss 7, 9), protection from liability (s 16), the financial year (s 18),
the transferred staff (ss 31-33), and the offences and composition (ss 38-40). Not
encoded: the seal (s 4), constitution and appointments (ss 5, 6, 8), committees and
delegation (ss 13, 14), staff (s 15), estimates and funds (ss 19-25), the transfer
of property, contracts and proceedings (ss 30, 34-36), the saving (s 42) and the
Schedule beyond naming its departments.

## What the Act turns out to say

### 1. The Board serves school children, but no one can sue for the service

s 11(1)(g) makes it a function of the Board "to provide healthcare services
(including medical, dental, health-screening and immunisation services) to school
children" and others as the Board thinks fit. s 11(3) then says nothing in s 11
imposes "any form of duty or liability enforceable by proceedings before any court".
So for the ordinary person the Act's answer to REQ-0172 is: it describes a service,
and grants no right to it. Asserted.

### 2. Nothing in the Act makes the services free

s 12(h) lets the Board "charge fees or commissions for services rendered by the
Board or for the use of any of its facilities", with no ceiling, schedule or
exemption, and no Minister's approval. Whether school health services are free is
not decided by this Act. Asserted (no approval needed); the rest is a reading of
silence.

### 3. Wrong health information from the Board is not actionable if given in good faith

s 16(2): where the Board supplies information to the public as a service, neither it
nor its employees are liable for loss caused by "any error or omission of whatever
nature ... or however caused" if made in good faith and in the ordinary course of
duties. This protects the Board itself, not only individuals (s 16(1)). That the
dietary guidelines and nutritional information of s 11(1)(f) are such a service is
an inference. Asserted.

### 4. Secrecy is punished more by prison than by fine; the symbol the other way

Breach of secrecy (s 39) carries a fine up to $2,000 but imprisonment up to 12
months; misusing the Board's symbol (s 38) up to $10,000 but 6 months. The secrecy
duty binds anyone who "is or has been" a member, officer, employee, agent or
committee member, and yields to duty, a court, or a written law. The symbol offence
mentions no intent. Composition is capped at $1,000 and only for offences
"prescribed as" compoundable (s 40); the Act prescribes none itself. Asserted.

### 5. Transferred staff kept their service, and the Government pays its share of the pension

s 31(1) moved Government staff of the five Schedule departments on terms "no less
favourable"; s 32(2) counts their Government service as service with the Board;
s 32(4) makes the Government pay the Board a portion of the pension. The sentence in
s 32(4) is tangled ("as the same bears to the proportion which ..."); it is encoded
as pension times Government emoluments over total emoluments, which is an inference.
s 33 bars claims under the Pensions Act 1956 for abolition of office caused by the
Board's creation. Asserted.

### 6. The Minister must approve property, companies, non-Government borrowing and regulations

ss 12(b), (c), 22 and 41. Contracts, fees, staff loans and borrowing from the
Government need no approval. Quorum is 5 and the presiding member has a casting
vote on top of a deliberative one (s 9); terms are at most 3 years (s 7). Asserted.

## What would need doing before this is worth anything

- No regulations made under s 41 were retrieved, so which offences are compoundable,
  and any fees, are unknown.
- The other written laws under which the Board carries out functions (s 11(1)(j))
  were not identified; those are where any duty on the public would sit.
- The reading of s 32(4) needs a pensions lawyer or an authority.
- No case law was searched.
