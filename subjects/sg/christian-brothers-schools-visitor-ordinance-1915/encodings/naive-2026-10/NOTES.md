# Christian Brothers' Schools Visitor Ordinance 1915 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CBSVO1915.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31 December
2021". The body carries the annotations [72/59] (under s 2(4)) and [7/97] (under s 5).

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0230** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance (historical, private and spent
Acts). It asks what the Ordinance decides for a person or business it applies to; no
scenario has asked a sharper question yet. The Ordinance has five sections, so all of
it is encoded except the short title (s 1). The preamble is quoted for context only.
The content of s 48 of the Conveyancing and Law of Property Act 1886 is not encoded:
whether an instrument was filed or a power of attorney deposited under it is a stated
fact.

## What the Act turns out to say

### 1. A successor's attorney may sign a deed but may not witness its sealing

s 3(1) names who must be present when the seal is affixed: Byrne, Byrne's attorney
under a deposited power, or a duly qualified successor. A successor's attorney is not
in that list. The signing limb is wider, "his successor or his said attorney". A deed
sealed before a successor's deposited attorney and signed by him is therefore **not**
duly sealed on the literal words. Yet under s 3(2) his signature is still "sufficient
evidence of the due sealing". Reading "his said attorney" as the successor's attorney
is an inference. Asserted.

### 2. A successor needs three steps, and the Gazette is evidence of all three

s 2(4): a successor is not "duly qualified", and so not part of the Corporation,
"unless and until" (a) the Minister has approved under hand and seal, (b) the
instrument constituting him Visitor has been filed in the Supreme Court Registry, and
(c) a notification of the filing has appeared in the Gazette. A successor who has
filed but is not yet gazetted is not the Corporation. s 2(5) makes the notification
"sufficient evidence" of appointment and qualification, so a notification published
without the Minister's approval would still be evidence of qualification. Whether that
evidence can be rebutted is not encoded. Asserted.

### 3. The Gazette is "sufficient", not "conclusive", evidence

The sister Bishop of Singapore Ordinance 1911 (s 5) makes its Gazette notification
"conclusive evidence". This Ordinance says "sufficient evidence" (s 2(5)), and uses the
same phrase for a signature as evidence of sealing (s 3(2)). The difference in wording
is recorded; its legal effect is not decided here.

### 4. No power to sue or be sued, and no perpetual succession, in the text

s 2(3) gives powers to acquire, hold and dispose of property, the disposal powers
reaching only property "vested in the Corporation". Unlike the Bishop of Singapore
Ordinance 1911, it does not say the Corporation may sue and be sued, and the Ordinance
does not mention perpetual succession. Whether the general law supplies them is outside
the text. Asserted (sue or be sued is not among the powers the Ordinance confers).

### 5. Section 4 sweeps in movables, but only from the two named Directors

s 4 vests "all movable and immovable property situated in the Colony" held before the
Ordinance by the Director in Singapore of St Joseph's Institution or the Director in
Penang of St Xavier's Institution, whether or not the deed named the individual
Director. Property held by an individual Brother or a lay trustee is not caught.
"Heretofore" is read as before 17 December 1915 (an inference). Asserted.

### 6. The preamble recites a repeal that the body does not enact

The preamble says it is "expedient to repeal" the St. Joseph's and St. Xavier's
Incorporation Ordinance, 1902. The deposited 2020 Revised Edition contains no repeal
section; presumably it was omitted in revision as spent (an inference, not checked).
Not asserted.

### 7. Whose rights are saved

s 5 saves the rights of the Government, of any body politic or corporate, and of any
other person, except those mentioned in the Ordinance and those claiming through them.
Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886, on which both qualification
  and sealing depend, was not read.
- The 1915 text and the 1902 Ordinance were not retrieved, so the omitted repeal and
  any changes made by [72/59] and [7/97] are unknown.
- No Gazette notification of a Visitor, and no case law, was searched; whether a
  current Visitor is duly qualified is not known.
