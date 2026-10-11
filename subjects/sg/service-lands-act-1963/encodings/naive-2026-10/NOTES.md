# Service Lands Act 1963 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SLA1963.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". It carries no amendment annotations; its Legislative History ends
with the 2013 Revised Edition (operation 31 August 2013). The Arrangement of
Sections is column-shifted in the deposit; the body (s 1 short title, s 2 removal of
unlawful occupants) is what was followed.

**Checks:** one module (`sla-ejectment.l4`), one case file
(`sla-cases-ejectment.l4`), 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0154** in `subjects/sg/requirements.jsonl`: tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The Act has two sections, so it is encoded whole except s 1
(the short title). What makes an occupation "unlawful", who the Federal Lands
Commissioner now is, and whether any land is in fact used for Malaysian forces are
questions the text does not answer, and are not encoded.

## What the Act turns out to say

### 1. The Act still speaks only of the forces of Malaysia

s 2(1) applies the section to "lands used or to be used for the purposes of any
military, naval or air forces of Malaysia", and the long title speaks of "any
Malaysian forces". The 2020 Revised Edition keeps those words. Land used by the
Singapore Armed Forces, or by any other foreign force, is outside the section on its
words. (That Singapore left Malaysia in 1965, and that the Act dates from Singapore's
time in it, is background not stated in the deposit.) Asserted.

### 2. Once the Court is satisfied, the warrant is mandatory

The summons is discretionary ("may issue a summons"), and so is the summary hearing.
But s 2(3) says that if the Court "is satisfied of the truth" of the information it
"shall by warrant" require the police "forthwith to dispossess and remove" the
occupier. No discretion to refuse, and no grace period, appears in the text.
Asserted.

### 3. The occupier can lose the land, its growing crops and its buildings, with no word on compensation

Possession is taken "together with all crops growing thereon and all buildings and
other immovable property upon and affixed to the land". The Act says nothing about
compensation, appeal, or what becomes of movable belongings or crops already
harvested; the encoding reads those as outside the warrant's words, and labels that
as an inference. Asserted.

### 4. Only the Commissioner can start it, and the hearing can proceed in absence

The information must come from "the Federal Lands Commissioner or a person authorised
by him"; a private landowner or another agency acting on its own account cannot use
this procedure. If the occupier does not appear, the Court may proceed "on proof of
service of the summons" — without that proof, it may not. Asserted.

### 5. Any police officer holding the warrant may execute it

s 2(3) ends: the warrant "may be executed by any police officer into whose hands the
warrant may come, whether or not it is addressed to him". A bailiff, a Commissioner's
officer who is not a police officer, or a soldier is not named. Possession is taken
"on behalf of the Federal Lands Commissioner". Asserted.

## What would need doing before this is worth anything

- Find out whether any land in Singapore is still held or used for Malaysian forces,
  and who (if anyone) now acts as the Federal Lands Commissioner; without that the
  Act may have no field of operation, and the text cannot say.
- Read the general law on what "unlawful occupation" means and on summary procedure
  in a Magistrate's Court, which the Act leaves unstated.
- Check whether other Singapore legislation (for instance on State land or on
  military lands) has displaced this procedure in practice.
- No case law was searched.
