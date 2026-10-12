# Reciprocal Enforcement of Commonwealth Judgments (Repeal) Act 2019 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act No. 24 of 2019, informal consolidation, as deposited at
`../../registers/source-bundle/RECJRA2019.txt` (page furniture: "version in force
from 1/3/2023"). The one amendment annotated is Act 40 of 2019 (wef 1 March 2023),
against s 2(2)(d). The deposit does not give the appointed date; s 1 leaves it to a
Gazette notification, which was not retrieved. The arrangement of sections at the
top of the deposit is out of step with the body; the body's numbers are used.

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**Requirement REQ-0259** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet. For a judgment creditor or an award holder that comes down
to one question: after the repeal, does the old law still reach my judgment or
award? The Act has five sections and this row takes all of them: commencement
(s 1), the repeal and its four savings (s 2), the repeal of Part II of the
Reciprocal Enforcement of Foreign Judgments Act and the saving of its s 10 (s 3),
the deletion of s 33(2) of the International Arbitration Act and its saving (s 4),
and the Minister's two-year regulation power (s 5).

Not encoded, because not deposited with this Act: what any saved provision
actually says (ss 2A, 3(1), (2), (3), (5) and 4 of the repealed Act; s 10 of the
REFJA and s 33(2) of the International Arbitration Act as they stood before the
appointed date). The encoding says only *whether* each provision continues to
apply. The appointed date, the s 5 notifications under the repealed Act, the REFJA
s 3 orders and any s 5 regulations were not retrieved.

## What the Act turns out to say

### 1. The saving keys on when the judgment was obtained, not when it is registered

s 2(2)(a): ss 2A and 3(1) and (2) of the repealed Act "continue to apply to a
judgment obtained before" the appointed date. Nothing ties registration to that
date, so an English judgment from before the repeal can still be registered under
the old Act afterwards; one obtained a day after the appointed date cannot, under
this Act at all. Whatever time limit s 3(1) itself sets was not deposited here.
s 4(2) does the same for arbitral awards, keyed on the date the award was *made*.
Asserted.

### 2. UK superior courts are saved automatically; every other Commonwealth court needs a live notification

s 2(2)(a)(i) saves judgments of "a superior court of the United Kingdom" without
more. (ii) saves other Commonwealth courts only where specified "in a notification
under section 5 of the repealed Act that was in force immediately before that
date". A court whose notification had lapsed or been revoked before the appointed
date is outside (ii), and a UK court that is not a superior court is outside (i).
Asserted.

### 3. An existing registration survives even where paragraph (a) would not reach the judgment

s 2(2)(b) keeps ss 2A and 3(3) alive for "a judgment registered under section 3(1)
and (2) of the repealed Act, including those provisions as applied by paragraph
(a)". A judgment registered while its court's notification stood keeps s 3(3) even
though the notification had lapsed by the appointed date. A registration made after
the appointed date is treated as saved only if it went through (a); that it has no
other footing is an inference. Asserted.

### 4. Section 3(5) is saved only for judgments that are still registrable

s 2(2)(c) applies ss 2A and 3(5) to "a judgment mentioned in paragraph (a)
registrable under the repealed Act". A judgment within (a) that is not registrable
(for whatever reason the old Act gave) keeps ss 3(1) and (2) but not s 3(5).
Asserted.

### 5. Singapore judgments keep the old s 4 if obtained before the appointed date

s 2(2)(d): s 4 of the repealed Act "continues to apply to a judgment obtained in the
General Division of the High Court before that date". The deposit does not say what
s 4 provided. Asserted.

### 6. Two cross-Act savings, each with three conditions

s 3(2) keeps s 10 of the REFJA for an order under its s 3 that was made before the
appointed date, extended Part I to a part of the Commonwealth to which the repealed
Act applied, and was in force immediately before that date — all three. s 4(2)
keeps s 33(2) of the International Arbitration Act for a foreign award made before
the appointed date and registrable under the repealed Act (including through
s 2(2)). Asserted.

### 7. The Minister's power to add savings lasts two years

s 5: "For a period of 2 years after the appointed date" the Minister may prescribe
further saving or transitional provisions consequent on the Act. Counting in whole
months, 23 is inside and 24 outside; how the last day is counted is an inference.
Asserted.

## What would need doing before this is worth anything

- The repealed Act (Cap. 264), s 10 of the REFJA (Cap. 265, 2001 Ed.) and s 33(2) of
  the International Arbitration Act (Cap. 143A, 2002 Ed.) as they stood before the
  appointed date are needed to say what the saved provisions require.
- The commencement notification (the appointed date), the s 5 notifications under
  the repealed Act and the REFJA s 3 orders were not retrieved.
- Any regulations under s 5 were not searched for.
- No case law was searched.
