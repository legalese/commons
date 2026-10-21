# Vandalism Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
incorporates all amendments up to and including 1 December 2021 and comes into
operation on 31 December 2021. No later amendment is annotated.

**Checks:** two case files: `va-cases-vandalism.l4` 55 assertions satisfied, `va-cases-seat.l4` 41 assertions satisfied; 0 errors, 0 warnings (stable l4, VS Code extension 1.6.98).

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. The Act is eight short
sections, so this row encodes every operative one: the definition (s 2), the
offence and punishment (s 3), production of written authority on demand (s 4),
seizure (s 5), arrestable and non-bailable (s 6), the presumption on receiving
stolen public property (s 7) and revocation of a secondhand goods dealer's licence
(s 8). The arrangement of sections at the head of the deposit is numbered one out
of step with the body; the body's numbers are used.

Not encoded: what ss 325(1) and 330(1) of the Criminal Procedure Code 2010 say (the
caning is "subject to" them; here a single input flag), what "arrestable" and
"non-bailable" entail, and the content of s 411 of the Penal Code 1871.

## What the Act turns out to say

### 1. Caning is mandatory, and the exception is narrow

s 3: on conviction the offender "shall also ... be punished with caning with not
less than 3 strokes and not more than 8 strokes". The only exception is a **first
conviction** for marking with "pencil, crayon, chalk or other delible substance",
or for posting a notice or hanging a flag. Marking in paint, or stealing, destroying
or damaging public property, attracts mandatory caning even on a first conviction;
a second poster offence does too. The fine (up to $2,000) and imprisonment (up to
3 years) are alternatives to each other; the caning is in addition. Asserted.

### 2. Damaging private property is not vandalism under this Act

Paragraph (b) of the definition is "stealing, destroying or damaging any **public**
property". Private property comes in only through paragraph (a): marking, posting
and flag-hanging without the owner's or occupier's written consent. (Whether
damaging private property is an offence under some other law was not read.)
Asserted.

### 3. Written permission cures paragraph (a), not paragraph (b)

Paragraph (a) is qualified by "without the written authority" (public property) or
"without the written consent of the owner or occupier" (private property).
Paragraph (b) carries no such qualifier, so the encoding treats damaging public
property as vandalism even with written authority. That is a literal reading; the
text does not say whether authorised destruction (say, a demolition) is meant to be
caught. Asserted.

### 4. Failing to show the permission slip is itself arrestable and non-bailable

s 4: the written authority or consent must be produced on demand to police,
Special Constabulary, Auxiliary Police, or the military police of the SAF or of a
lawfully present armed force; failure is an offence with a fine of up to $500. s 6
makes "every offence" under the Act arrestable and non-bailable, which on its words
includes this $500 offence. A private security guard or a town council officer is
not on the s 4(1) list, and neither can seize under s 5. Asserted.

The duty reaches **paragraph (a) conduct only**. s 4(1) speaks of "the written
authority or the written consent ... required under paragraph (a)" of the
definition; paragraph (b) (stealing, destroying or damaging public property) needs
no authority or consent, so there is nothing to produce and no s 4(2) offence.
Encoded as `must produce the written authority or consent` (conduct and demander)
from 21 October 2026. Asserted.

s 5 seizure is a separate power: it needs no demand and no paragraph (a) conduct,
only a s 4(1) person who reasonably believes either that an offence under the Act
was committed in respect of the article or thing, or that it is or contains
evidence of one. The two beliefs are separate inputs from 21 October 2026 (they
were one). Asserted.

### 5. Receivers of stolen public property are presumed to know

s 7 reverses the burden in a prosecution under s 411 of the Penal Code 1871 where
the stolen property is public property: knowledge and dishonesty are presumed
"until the contrary is proved". s 8 makes revocation of a secondhand goods dealer's
licence or exemption mandatory ("shall") on such a conviction. Asserted.

### 6. "Public property" is wider than the Singapore Government

It includes property of "the government of any Commonwealth or foreign country",
any statutory body or authority, and any armed force lawfully present in Singapore.
Asserted.

## What would need doing before this is worth anything

- Read ss 325(1) and 330(1) of the Criminal Procedure Code 2010 and replace the
  input flag with their actual conditions.
- Check whether "causes any such act to be done" and "attempts" carry the same
  caning rule; the encoding treats all three forms of the offence alike, as s 3's
  wording suggests.
- No case law on authorised destruction of public property or on the delible /
  indelible line was searched.


## Seat

The seat is **the person accused of vandalism**: the one who did, tried to do, or caused someone else to do the act,
and the person the Act is applied to. `va-seat.l4` phrases the rules in `va-vandalism.l4` as that person's questions
("Is what I did vandalism", "Must I be caned", "Must I show my written permission") and changes none of them; each question
is marked `@export` so it can be deployed to Legalese Cloud and asked from a form. `va-cases-seat.l4` checks every
question against hand-checked values (41 assertions; for the s 4 group, 10 with the situation gate answered yes and 5
with it answered no).

The defaults ruled on 2026-10-18:
- **The Act alone:** followed; no subsidiary legislation is needed for its numbers.
- **The actors the text names:** followed (owners, the s 4(1) officers, the court).
- **Judgments handed to others answered conditionally:** followed; the officer's reasonable belief (s 5) and the
  Criminal Procedure Code exclusions from caning are asked as facts.
- **The Act's definitions worked out:** followed (act of vandalism, public property, s 4(1) person).
- **One case is the natural unit:** followed; one act.
- **The Act's terms with plain glosses:** glosses are in the seat layer's comments and the form's wording.
- **Operative sections in, machinery out:** followed, with one departure: ss 7-8 address a receiver of stolen public
  property and the court, not the accused vandal; they stay in the rules underneath but are not asked in the seat layer.

19 October 2026.

## Situation gate

The three s 4 questions, under `§ If I am asked to show written permission`, only arise if an officer has asked the
person to show written permission. Until 21 October 2026 the website gated that group in its own data; the gate is now
in the encoding. Each of the three takes a first input, `was asked to show written permission`, with the @desc "Has a
police officer or military police officer asked you to show written permission for what you wrote, posted or
displayed?".

**Result type: MAYBE, for all three.** Where the gate is FALSE the answer is `NOTHING` (the situation does not arise);
where it is TRUE the answer is `JUST` the rule's answer. FALSE-when-not-asked would be safe for "Must I show my
written permission" and the s 4(2) offence (with no demand there is no duty and nothing to fail), but wrong for the
fine question (a NUMBER has no honest "no"; 0 would misstate s 4(2)). One result type across the group keeps the form
simple: NOTHING always means "this does not arise for you".

The gate's wording names police and military police; the demander input still offers a private security guard, a town
council officer and the property owner, so that a person who was asked by one of them learns the answer is no.

"Can they take the article from me" (s 5) is **not** gated: seizure does not depend on any demand. It sits under
`§ What can happen to me`, with only what s 5 needs (who wants to take it, and the two beliefs).

## Finding: the first seat layer misread s 4 as handing over the article

The seat layer of 19 October 2026, and the first version of the gate (21 October 2026), phrased s 4 as "Do I have to
hand over the article". s 4(1) is about producing **the written authority or written consent required under
paragraph (a)**, not any article; the article comes in only under s 5 (seizure), which is a separate power. The rules
underneath (`failing to produce is an offence`) were not about articles, but they missed the paragraph (a) limit and
folded s 5's two beliefs into one. Corrected on 21 October 2026, checked against VA1966.txt (ss 4 and 5):
- the s 4 questions are now "Must I show my written permission to this officer?", "Have I committed an offence by not
  showing my written permission?" and "What is the most I can be fined for not showing it?", with new function names;
- s 4 is limited to paragraph (a) conduct, so each s 4 question (except the fine) takes "What you did";
- s 5 is out from behind the gate and takes the two s 5 beliefs separately;
- the gate's wording is about showing written permission.

**Breaking change for the deployment `sg-vandalism-act-1966`:** redeploy from `va-seat.l4` under the same name. The
three s 4 questions are renamed and gain inputs (the gate, and the conduct); "Can they take the article from me" keeps
its name but its single belief input becomes two. The website's own gate for this group can go.

21 October 2026.
