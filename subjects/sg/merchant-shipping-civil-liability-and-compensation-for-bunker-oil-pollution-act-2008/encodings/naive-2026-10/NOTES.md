# Merchant Shipping (Civil Liability and Compensation for Bunker Oil Pollution) Act 2008 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as shown in the finished naive rows (the skill itself was
not loadable in this session). No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/MSCLCBOPA2008.txt`. The page footer reads "version in
force from 1/4/2022"; the revised edition "incorporates all amendments up to and
including 1 December 2021". The latest amendment annotated is Act 25 of 2021 "wef
01/04/2022", at s 17(4).

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0105** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The people it applies to are shipowners, their insurers, crew,
salvors and clean-up contractors, and anyone who suffers loss from a bunker spill.

The Act has 29 sections, so most of the operative Part 2 is encoded: liability and
its exceptions (ss 2(3), 3, 4, 17(1)), channelling and environmental loss (s 5),
limitation (ss 6, 7(2), 14(3), 16), the time bar (s 11), compulsory insurance and
direct action (ss 12, 14, 17(2)), and the penalties. Not encoded: the limit figure
itself (s 6(2) takes it from s 136 of the Merchant Shipping Act 1995, which is not
in this deposit), SDR conversion and claims procedure (s 7(3) to (8)), ss 8 to 10,
s 13, s 15, s 17(3), (4), s 19(1) detention, ss 20 to 22, 24 to 26, 28, regulations
under s 12(4), joint liability (s 3(5)) and contributory negligence (s 3(7)).

## What the Act turns out to say

### 1. The insurer can limit when the owner cannot

s 6(4) takes away the owner's right to limit where the spill resulted from the
owner's act or omission "with intent" or "recklessly and in the knowledge" that
damage would probably result. But s 14(3) lets the insurer limit "whether or not"
that was so. A claimant suing the insurer directly is held to the limit even
where the owner would have to pay in full. The insurer's own defence under s 14(2) is
narrower: only the owner's "wilful misconduct". So reckless bunkering leaves the
insurer liable (up to the limit), and wilful misconduct lets it off entirely.
Asserted.

### 2. The owner is liable without fault, and almost no one else is

s 3 makes "the owner" liable, and s 2(1) defines owner to include "the registered
owner, bareboat charterer, manager and operator". s 5(1)(c) means the owner is not
liable "otherwise than under that section"; s 5(1)(d) and (2) protect servants and
agents, crew, consenting salvors, people taking preventive measures, and their
servants, unless they acted with intent or recklessly knowing damage would probably
result. A stranger gets no protection. Asserted.

### 3. Three narrow exceptions, and the owner must prove them

s 4: war or "an exceptional, inevitable and irresistible natural phenomenon"; damage
"due wholly" to someone who is not the owner's employee or agent "with intent to do
damage"; or "due wholly" to the negligence of the authority responsible for lights or
navigational aids. Each must be proved by the owner. Asserted.

### 4. Tanker spills of persistent oil go to the other Act

s 3(3): no liability under this Act for a ship covered by the Merchant Shipping
(Civil Liability and Compensation for Oil Pollution) Act 1998 "where that bunker oil
is also persistent hydrocarbon mineral oil". A non-persistent bunker spill from the
same ship stays here. Asserted.

### 5. Ships over 1,000 GT need insurance and a certificate to use a Singapore port

s 12(1) sets the threshold at gross tonnage "greater than 1,000", so exactly 1,000 is
outside. A foreign ship needs cover only to use a Singapore port or offshore facility;
a Singapore ship needs it for ports anywhere. Using a port without cover exposes the
master or the registered owner to a fine of up to $1 million (s 12(6)); not carrying or
producing the certificate, up to $20,000 (s 12(7)). Who may issue the certificate turns
on the flag (s 12(3)); for a non-Convention flag, the flag State's own certificate is
not enough unless regulations under s 12(4) recognise it. Asserted (regulations not
modelled).

### 6. Environmental harm is paid for only in money terms

s 5(3) confines liability for "impairment of the environment" to loss of profits and
the cost of reasonable reinstatement measures "actually taken or to be taken".
Asserted.

### 7. Two time limits, both binding

s 11: an action must be commenced within 3 years after the claim arose and within 6
years after the first occurrence. Asserted.

### 8. Other points asserted

Nothing applies to an occurrence before 21 November 2008 (s 2(3)); warships and
non-commercial government ships are outside Part 2 (s 17(1)); a mere threat
supports claims for preventive costs but not for contamination damage (s 3(2));
damage in another Convention country is covered only alongside liability in
Singapore (s 3(4), read with s 15(2) — the dependency is an inference from the two
provisions together); a limitation fund is shared in proportion to claims (s 7(2)(b));
a non-Convention judgment is enforceable only up to the s 6 limit (s 16); a detained
ship going to sea carries up to $50,000 or 2 years (s 19(2)).

## What would need doing before this is worth anything

- The limit amount needs s 136 of the Merchant Shipping Act 1995 and the 1976
  Limitation Convention as amended; here it is a bare parameter.
- "Persistent hydrocarbon mineral oil" and the scope of the 1998 Act were not read.
- Article 7 of the Bunker Convention (what the insurance must cover) was not read.
- No regulations (fees, compoundable offences, s 12(4) recognitions) or case law were
  searched.
