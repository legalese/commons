# Intellectual Property Office of Singapore Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (incorporating amendments up to 1 December 2021,
in operation 31 December 2021), informal consolidation marked "version in force
from 1/5/2024", deposited at `../../registers/source-bundle/IPOSA2001.txt`. The
latest amendment annotated in the body is Act 22 of 2021 wef 01/05/2024 (Third
Schedule item 5); the deposit's metadata records it as current as at 3 October 2026.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0176** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

Most of the Act sets up and finances a statutory board. This row takes what a member
of the public or a business can meet: the definitions of intellectual property agent
and adviser (s 2), the shield for errors in information the Office supplies (s 11),
misuse of the Office's symbol (s 29), the officers' enforcement powers, the offences
they reach and obstruction (s 30, Third Schedule), liability of directors and
partners (s 31), composition (s 33) and the secrecy offence (s 36). Not encoded:
constitution and the First Schedule, functions and powers (ss 6, 7), staff, finance
(ss 13-20), the 2001 transfers (ss 21-27), prosecution by Office officers (s 34,
noted only), rule-making, and the offences in the other IP Acts that the Third
Schedule merely lists.

## What the Act turns out to say

### 1. The Office is not liable for its own register errors, if made in good faith

s 11(2): where the Office supplies information to the public under a written law,
neither it nor its officers is liable for loss "by reason of any error or omission of
whatever nature ... or however caused if made in good faith and in the ordinary course"
of duty. A business relying on a search of the patent or trade mark records bears the
loss of a good-faith error. The Act is silent outside the shield; the encoding does not
decide that the Office is liable there. s 6(3) separately makes the Office's functions
unenforceable in court. Asserted.

### 2. A director is caught on proof; a partner is caught unless he proves otherwise

s 31(1) makes a director, manager or secretary guilty alongside the company only where
the offence "is proved" to involve their consent, connivance or neglect. s 31(5) makes
every partner of a guilty partnership guilty "other than a partner who is proved to
have been ignorant of or to have attempted to prevent" it. The burden runs the other
way. Asserted.

### 3. The Office's officers enforce offences in five other IP Acts

s 30(1) gives the identity, information and attendance powers for offences under this
Act "or any written law set out in the Third Schedule": listed sections of the Patents,
Trade Marks, Registered Designs and Geographical Indications Acts, and Part 9 Division
2 of the Copyright Act 2021 (added wef 1 May 2024). s 34 lets an authorised Office
officer prosecute those offences with the Public Prosecutor's authorisation. Each power
needs the officer to declare the office and produce the identification card; an
attendance order must be in writing and reaches only persons within Singapore.
Asserted.

### 4. Obstruction: a refusal can be excused, a wilful lie cannot, an honest slip is no offence

s 30(2)(b) punishes one who "wilfully mis-states or without lawful excuse refuses" to
give information. The lawful excuse qualifies only the refusal; obstructing or failing
to comply with a lawful demand has no excuse written in. Maximum $10,000 or 6 months
or both. Asserted.

### 5. Leaking is fined less but jailed longer than misusing the logo

Misusing the Office's symbol (s 29(2)) and obstruction (s 30(2)) carry a fine up to
$10,000 or 6 months. Disclosing information obtained in office (s 36(2)) carries a
fine up to $2,000 but imprisonment up to 12 months. An identical symbol is an offence
without any proof of confusion. Composition is capped at $1,000 and, since Act 7 of
2022, the money goes to the Consolidated Fund, not the Office (s 33(3)). Asserted.

### 6. Copyright advice makes you an adviser, never an agent

s 2 limits "intellectual property agent" to acting for another on patents, trade marks,
registered designs and geographical indications. Copyright is absent; "intellectual
property adviser" covers advice on "any intellectual property". Asserted.

### 7. The deposit's arrangement of sections is out of step with the body

In the .txt the arrangement for Part 5 runs "13. Bank accounts ... 14. Minister's
approval ..." while the body has s 13 Funds and property, s 14 Application of moneys
and s 15 Bank accounts. The body's numbering was followed. (Inference: an extraction
artefact of the two-column PDF layout.) Not asserted.

## What would need doing before this is worth anything

- The offences listed in the Third Schedule were not read in their own Acts.
- No compoundable-offence regulations under s 33 were retrieved, so which offences are
  "prescribed as compoundable" is a bare input.
- No case law on s 11(2) or s 31 was searched.
