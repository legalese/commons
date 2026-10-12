# Boy Scouts Association Act 1926 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021" and came into operation on
31 December 2021. The legislative history lists one amending law after the 1926
Ordinance, Ordinance 37 of 1952 (Law Revision (Penalties Amendment)), in force
30 April 1955. Every other entry is a revised edition.

**Checks:** one case file, 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0228** in `subjects/sg/requirements.jsonl`. It sits in
Tier 4 of the remaining Singapore Acts, which are ordered by how much they touch
everyday life. The requirement asks what the Act decides for a person or business it
applies to. No scenario has asked a sharper question yet. The Act has seven sections,
and this row encodes every operative one (ss 2-7). What it leaves out is what the Act
hands to the Association's own constitution, by-laws and rules: who is recognised as a
boy scout, which badges are "specifically adopted", and what authority a scout may
exercise. None of those documents is in the deposit, so each is taken as a fact.

## What the Act turns out to say

### 1. Only the Association may sell a scout badge, and that includes scouts and second-hand sales

s 3: "No person, other than the Association, shall sell or expose for sale" an
adopted badge, token or emblem. The Association is the only exception. A scout selling
spare badges to another scout contravenes it. So does a collector reselling an old
badge, because the text draws no line between new and second-hand. Merely exposing a
badge for sale is enough. Asserted.

### 2. The words "boy scouts" are reserved, not just a link with the Association

s 6 forbids forming, organising, working in connection with, or being "concerned in"
any body that, without due authority under the Royal Charter, "claims or purports to be
'boy scouts', or otherwise to be connected with the Association". A body that calls
itself "boy scouts" is caught even if it claims no link with the Association. The
offence reaches volunteers ("work in connection with") as well as founders. A club that
does not use the name and claims no connection is outside it. Asserted.

### 3. Wearing a badge is an offence only for a non-scout, in public, and in a way that passes as a scout

s 4 needs all four: the person is not a boy scout, wears, carries or bears the badge
publicly, does so "in such a manner as to convey the impression that he is a boy
scout", and the badge is an adopted one. Wearing a badge at home, or a collector
displaying badges at an exhibition, is not caught. A former scout is no longer
"recognised" (s 2), so he is caught if he wears his old badge to pass as a scout.
Asserted.

### 4. Lookalike badges reach s 5 but not ss 3 and 4

Only s 5 extends to a badge "purporting or appearing to be such". Sections 3 and 4
speak only of a badge "specifically adopted ... under the by-laws or rules". On the
text, then, selling or wearing an imitation badge contravenes neither. That reading is
an inference from the difference in wording, and no case was searched. A scout who uses
a lookalike badge to claim authority does contravene s 5. Asserted.

### 5. Section 5 binds scouts, not impostors

s 5 begins "No boy scout shall". It forbids seeking or attempting to enforce or exercise
authority by virtue of a badge "otherwise than in accordance with and as authorised by"
the Association's by-laws or rules. A non-scout who uses a badge to claim authority is
outside s 5, though he is caught by s 4 if he wears it publicly to pass as a scout.
"Boy scout" includes "all officers of the Association" (s 2), so officers are bound by
s 5 and exempt from s 4. Asserted.

### 6. The only penalty is a fine of up to $200

s 7: any contravention is an offence, tried summarily "before a Magistrate's Court",
with liability "to a fine not exceeding $200". The section provides no imprisonment.
The legislative history shows the penalties were last amended by Ordinance 37 of 1952.
Asserted.

### 7. The Association is defined by a 1912 Royal Charter

s 2 defines the Association as "the Boy Scouts Association incorporated under the
Royal Charter granted on 4 January 1912". The deposit names no Singapore body. How the
definition maps onto any scouting organisation operating in Singapore today is not
answered by the text and was not researched. Not asserted.

## What would need doing before this is worth anything

- Retrieve the Association's constitution, by-laws and rules. The Act's content turns on
  them: they decide who is a scout, which badges are protected, and what authority a
  scout may exercise.
- Establish which body the 1912-charter definition reaches in Singapore today.
- Search for case law on s 3 (second-hand sales) and on whether imitation badges fall
  under ss 3 and 4.
- The pronoun "he" in ss 4 and 5 and the word "boy" were not tested against the
  Interpretation Act. No gender question is encoded.
