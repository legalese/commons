# Attorney-General (Additional Functions) Act 2014 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions (as shown by the finished example rows) and nothing else. No pipeline,
no coverage table, no independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1/7/2026, as deposited at `../../registers/source-bundle/AGAFA2014.txt`. The revised
edition incorporates amendments up to 1 December 2021; the latest amendment
annotated is Act 17 of 2026 (Skills and Workforce Development Agency Act 2026, in
force 1 July 2026).

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0158** in `subjects/sg/requirements.jsonl`: tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is five operative sections and a Schedule, so the row takes all of it:
the definitions (s 2), judicial review and follow-on claims (s 3), other court
proceedings (s 4), the fee (s 5) and the Schedule as it now stands. Not modelled:
the short title (s 1), the President's power to amend the Schedule (s 6), any fee
amount (the Act sets none), and the content of the Attorney-General's opinions on
conflict, public interest and public importance, which are taken as given facts.

The arrangement of sections at the top of the deposit is one out of step with the
body (it numbers "Short title" as 2). The encoding follows the body.

## What the Act turns out to say

### 1. If you sue a listed board, the State's lawyer may be on the other side, and that choice is unchallengeable under the Act

ss 3(2) and 4(2): any decision of the Attorney-General "to, or not to, represent a
relevant statutory board ... is final and conclusive". The Act gives the person on
the other side no say in, and no route to question, the Attorney-General appearing
for (say) HDB, the CPF Board or IRAS. Whether a court would still review the
decision under general law is not something the Act answers; not modelled.
Asserted.

### 2. Two different tests: "not contrary to the public interest" for judicial review, "a matter of public importance" for everything else

Both sections need the board's request, the responsible Minister's consent and the
Attorney-General's opinion that the Government and the board have no conflicting
interests. Then s 3(1)(f) asks only that representation be "not contrary to the
public interest"; s 4(1)(d) asks that the proceedings "concern a matter of public
importance". An ordinary contract suit against a board of no public importance is
one the Attorney-General may not take, however willing the board and Minister.
Asserted.

### 3. A follow-on money claim counts under s 3 only after a listed remedy, and an injunction is not one

s 3(1)(b) covers claims "for a liquidated sum, damages, equitable relief or
restitution" only if "a Mandatory Order, Prohibiting Order, Quashing Order or
declaration is made pursuant to the judicial review". The s 2 definition of
judicial review includes an application for an injunction, but an injunction is not
in the s 3(1)(b) list. A damages claim following a judicial review that produced
only an injunction is therefore "other proceedings" under s 4 and needs the stricter
public-importance opinion. (That reading is the encoder's; the text does not say so
in terms.) Asserted.

### 4. Only the 25 scheduled boards; being a statutory board is not enough

s 2 defines a statutory board broadly ("a body corporate or unincorporate
established by or under any public Act to perform or discharge a public function"),
but only those "specified in the Schedule" are relevant. The Schedule lists 25:
items 1-24 with item 3 deleted (Act 14 of 2022, from 1 August 2022) and 5A
(Communicable Diseases Agency, from 1 April 2025) and 6A (Gambling Regulatory
Authority, from 1 August 2022) added. Item 23, Skills and Workforce Development
Agency, is annotated Act 17 of 2026 from 1 July 2026. The list includes the
Presidential Elections Committee. The deposit does not say what item 3 was. The
bodies used as "not listed" examples (Singapore Tourism Board, JTC Corporation,
Enterprise Singapore, a town council) were chosen by the encoder. Asserted.

### 5. The board pays, not you

s 5: the Attorney-General may require the board to pay "a fee of such reasonable
amount as the Attorney-General determines", and the fee "is to be a charge on the
funds of that statutory board". No figure is set, and the Act does not make the fee
recoverable from the other party (costs between litigants are outside this Act and
not modelled). Asserted.

### 6. Old decisions count too

s 2: an "administrative decision" includes one made "before, on or after 1 January
2015" (the commencement date), but only "under any public Act"; a decision under a
private Act is outside the definition. Asserted (the two-limb test only; dates are
not modelled).

## What would need doing before this is worth anything

- The meaning of "final and conclusive" against judicial review of the
  Attorney-General's own decision needs case law; none was searched.
- The Schedule should be checked against the 2026 amending Act for what item 23
  replaced, and item 3's former occupant found in an earlier version.
- How "instrument of legislative character" and judicial review "instituted by any
  person" apply when the board is itself the applicant is not addressed.
- No scenario has asked a question of this Act yet; REQ-0158's question should be
  sharpened when one does.
