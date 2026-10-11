# Countervailing and Anti-Dumping Duties Act 1996 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited at
`../../registers/source-bundle/CADDA1996.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amending Act annotated in the text is [21/2008] (s 30(5)).
The legislative history lists Act 21 of 2008 (Mental Health (Care and Treatment) Act
2008, in force 1 March 2010) as the last amendment.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0098**: Tier 2 of the remaining Singapore Acts, ordered
by everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to. No scenario has asked a sharper question yet.

The Act runs two parallel procedures, countervailing duty (Part 2) and anti-dumping
duty (Part 3), and most of it is the Minister's procedure. This row takes the parts an
importer, a foreign exporter or a Singapore producer can test against figures and
dates:

- who is an interested party;
- the dumping margin and the amount of duty;
- whether a petition has enough support for an investigation to start;
- the 5% home-market sales test;
- termination for a de minimis margin or a negligible volume;
- how long an investigation may take;
- when provisional measures may start and how long they may last;
- what happens to provisional duty at the final determination;
- retroactive duty;
- the five-year sunset;
- review by the Tribunal;
- exchange-rate movements, double counting and the secrecy offence.

Not encoded:

- the subsidy definition (s 2(2)-(5));
- how normal value and export price are built, beyond the 5% test (ss 15-18);
- the Minister's duties to publish and notify;
- undertakings, beyond one deadline;
- the grounds for review;
- administration and the Tribunal's constitution;
- confidential information and facts available;
- everything the Act leaves to regulations, none of which were retrieved.

Wherever the Act turns on the Minister's judgment (injury, causation, public interest,
"special circumstances"), that judgment is an input.

## What the Act turns out to say

### 1. The two halves of the Act fix different numbers

The Parts on anti-dumping and countervailing duty use the same words almost section
by section. Where they differ is in which figures the Act sets itself and which it
leaves to regulations:

- **De minimis and negligible volume.** For anti-dumping duty the Act fixes them in
  s 24(3): a margin "less than 2%, expressed as a percentage of the export price" is
  de minimis, and a country's share of imports under 3% is negligible. For
  countervailing duty, s 10(3) leaves both to "the prescribed percentage".
- **How long provisional measures last.** Here it is the other way round. The
  countervailing limit is in the Act: "must in no case exceed 4 months" (s 8(4)). The
  anti-dumping limit is "such period as may be prescribed" (s 22(4)).
- **A resumed investigation.** When an undertaking is broken and an anti-dumping
  investigation resumes, the final determination is due "within 120 days" of the
  preliminary one (s 25(9)(c)). Section 11(9)(c), its countervailing counterpart,
  says "within the prescribed period".

The 2%, the 3%, the 4 months and the 120 days are asserted. The prescribed figures
could not be encoded.

### 2. Producers who stay silent help defeat a petition

Before an investigation can start, the petition must pass two tests (s 19(8), and
s 4(8) in the same words):

- **(a)** producers supporting it must account for more than 50% of the output of the
  producers who express a view either way;
- **(b)** they must account for at least 25% of the whole domestic industry's output.

A producer who says nothing counts only in (b). Suppose supporters hold 20% of output,
opponents 5%, and the remaining 75% stay silent. The petition passes (a) and fails (b).
An exact tie between supporters and opponents fails (a). Asserted.

### 3. Provisional duty: the importer keeps the lower figure, and some findings refund it all

When the final determination is made, goods that bore provisional measures are dealt
with as follows (s 23(5)-(7), and s 9(5)-(7) in the same words):

- **If the final duty is higher** than the provisional duty or security, only the
  provisional amount is collected.
- **If the final duty is lower**, only the final duty is collected and the excess is
  refunded or released.
- **If the finding is threat of injury**, duty falls on those goods only if the
  Minister also finds that, without the provisional measures, there would have been
  material injury.
- **If the finding is material retardation of an industry**, that is not listed in
  s 23(5), so the whole provisional amount is refunded under s 23(7).

Asserted.

### 4. Downstream users and consumers are not interested parties unless the Minister says so

The list of interested parties in s 2(1) is:

- **(a)** producers, exporters and importers of the subject goods;
- **(b)** associations a majority of whose members are such producers, exporters or
  importers;
- **(c)** the exporting government;
- **(d)** Singapore producers of the like goods;
- **(e)** associations a majority of whose members produce the like goods in
  Singapore;
- **(f)** "any other person the Minister considers appropriate".

A Singapore manufacturer that uses the goods as an input, or a consumer body, comes in
only under (f). That matters because only "an interested party" has "the right of
review by the Tribunal" (ss 13(1), 27(1)). The application must be filed within 30
days. The Tribunal may only "affirm the determination or remit the matter to the
Minister". It cannot set its own rate. Asserted.

### 5. Retroactive duty reaches back 90 days, but never past initiation

Anti-dumping duty may be imposed on goods imported within 90 days before provisional
measures, "but in no case earlier than the date of the initiation of the
investigation" (s 23(8)). Two conditions must both be met:

- either there is a history of injurious dumping, or the importer "was or should have
  been aware" of it; and
- the injury comes from massive imports in a short time.

The countervailing version (s 9(8)) asks for something different. The injury must be
"difficult to repair", and the subsidies must be inconsistent with GATT 1994 and the
Subsidies Agreement. It says nothing about what the importer knew. Asserted.

### 6. Duties expire after five years unless a review keeps them

Duties "must not be collected on imports made after 5 years from the date of
publication of the notice of the final determination". The exception is where a
review finds that ending them would be likely to lead to recurrence (ss 12(7), 26(7)).
Asserted.

### 7. The secrecy offence is smaller than what regulations may impose

A person who discloses material obtained under the Act commits an offence unless the
Minister authorised the disclosure or it was made for the purposes of the Act
(s 45(1)). The penalty is a fine of up to $5,000, imprisonment of up to one year, or
both (s 45(2)). Asserted.

Section 46(2)(i) lets regulations create offences carrying up to $10,000 or 3 years.
That is more than the Act's own offence. Not asserted, because no regulations were
retrieved.

### 8. Drafting points noticed, not asserted

- **Section 25(10)** refers to an investigation "completed under subsection (5)". The
  parallel s 11(10) says "subsection (4)".
- **Section 25(11)** covers determinations under "(9) or (10)". Section 11(11) covers
  only (9).
- **Section 46(2)(h)** names "the Agreement on Countervailing and Subsidies Measures".
  Section 2(1) defines "Agreement on Subsidies and Countervailing Measures".

Reading these as slips is an inference.

The encoding also does two things the Act does not spell out, both inferences:

- it treats the dumping margin as zero when the export price is not below normal
  value;
- it counts days from initiation.

## What would need doing before this is worth anything

- Retrieve the regulations made under s 46. They fix the countervailing thresholds,
  the anti-dumping provisional period, review periods, what counts as a "producer" and
  as "undertakings", and the non-market-economy method (ss 3(4), 18).
- Encode normal-value construction (s 15(2), (4)-(7)) and export-price construction
  (s 16) as a calculation, with worked examples from published Singapore
  determinations, if any exist.
- Have someone check the s 25(10) and s 25(11) cross-references against the 1996 Act
  and the 2004 amendment.
- No Tribunal decisions or Gazette notices were searched.
