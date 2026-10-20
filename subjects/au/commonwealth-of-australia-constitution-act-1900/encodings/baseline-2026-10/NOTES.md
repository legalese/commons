# Commonwealth of Australia Constitution Act 1900 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. Every
question is published with `@export`, and every input carries a `@desc`, ready
for Legalese Cloud. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

**Edition:** Commonwealth of Australia Constitution Act (The Constitution),
Compilation No. 6, compilation date 29 July 1977, includes amendments up to Act
No. 84, 1977 (register id C2013Q00005, registered 18 November 2021), as
deposited at `../../registers/source-bundle/C2004Q00685.txt`. No regulation or
other instrument sets a number or date for the encoded sections.

**Checks:** one module (`const-candidate.l4`) and one case file
(`const-cases-candidate.l4`): 43 assertions, 43 satisfied, 0 errors, 0 warnings,
with the stable `l4` from VS Code extension 1.6.98. The case file is generated
by `gen_commonwealth-of-australia-constitution-act-1900_baseline.py`
(scratchpad). Its expected values were written by hand from the text. There was
no earlier encoding of this Act to replace.

## Seat

**The would-be candidate**: the person who wants to be chosen as a senator or a
member of the House of Representatives. In the lives, this is Daniel in 2040, an
Australian by birth who is also Italian by descent. Sections 16, 34 and 44 are
written about that person ("Any person who ... shall be incapable of being
chosen"). The House that would decide a dispute (s 47) and the court in which a
common informer sues (s 46) appear only as what can happen to the person. The
decisions are `Am I incapable of being chosen under section 44`, `Am I capable
of being chosen`, `Would my place become vacant` and `What could I be made to
pay for sitting while incapable`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed. No instrument sets a number here. Section 34 applies only "Until the
  Parliament otherwise provides". The Parliament's replacement (Commonwealth
  Electoral Act 1918 s 163, per that Act's baseline encoding) belongs to another
  Act, so whether it has provided, and whether the person meets its tests, are
  asked as facts.
- **The actors the text names.** Followed: the person, the Queen's Ministers,
  the Crown, the Public Service of the Commonwealth, and a foreign power.
- **A judgment the law hands to someone else, answered conditionally.**
  Followed. Whether a person is a citizen of a foreign power is a matter for that
  power's law. The encoding asks whether a renunciation **has taken effect under
  that law**. It does not guess the answer.
- **The Act's own definitions worked out; borrowed terms asked.** Followed. The
  s 44 limbs, the proviso to (iv), the "more than twenty-five persons" test and
  the s 34 age are worked out. These are asked: "office of profit under the
  Crown", "undischarged bankrupt", "subject of the Queen", "elector" and
  "foreign power".
- **One case is the text's natural unit.** Followed: one person, one House, on
  one day.
- **The Act's own terms, each with a plain gloss.** Followed.
- **Operative sections in; machinery out.** Followed. Out of scope: the oath
  (s 42), resignation and absence (ss 19, 20, 37, 38), disputed elections
  (s 47) and allowances (s 48).

**Departure, stated plainly.** The High Court has held that a person who has
taken all reasonable steps to renounce, and whom the foreign law makes it
impossible to free, is not disqualified (Sykes v Cleary; Re Canavan [2017]
HCA 45). That gloss is case law, not text, and is **not** encoded. The encoding
reads the text: a person who is still a citizen under the foreign law is
disqualified. The fixture `a citizen whose foreign law forbids renunciation`
shows where the gloss would change the answer. The case law on **when** the
test applies (from nomination) is also not encoded. The text gives no date, so
the facts are taken as at the day asked about.

## The lives

- **daniel d060** (15 March 2040, the Italian consulate): "Is a dual citizen
  capable of being chosen?" `Am I disqualified by foreign allegiance` is TRUE
  before his renunciation takes effect under Italian law, and FALSE once it has.
  `Am I capable of being chosen` for the House of Representatives is FALSE on
  15 March, and TRUE on 23 June 2040 (his d061 nomination), given the Electoral
  Act s 163 qualifications.
- **Consistency with the Commonwealth Electoral Act 1918 baseline.** That
  encoding asks `I am incapable of being chosen under section 44 of the
  Constitution` as a borrowed fact. This encoding's `Am I incapable of being
  chosen under section 44` gives that answer: TRUE for Daniel in March, FALSE at
  nomination. Both are asserted.

## Why this scope

The life event turns on s 44(i), and the would-be candidate meets all five
limbs of s 44 on the qualification checklist. So the whole of s 44 is in, with
its proviso. Sections 16, 34 and 43 make up the rest of "capable of being
chosen". Sections 45 and 46 tell the person what follows if they are chosen and
then fall within s 44. Nothing else in the Constitution bears on standing.

## What the Act turns out to say

1. Section 44(i) asks whether the person "is" a subject or citizen of a foreign
   power. Under the text, birth in Australia does not help, and nor does a
   renunciation that has not taken effect. Daniel is incapable on 15 March 2040
   and capable once Italy's renunciation takes effect. Asserted.
2. Section 44(i) has three separate limbs: an acknowledgment of allegiance,
   obedience or adherence; being a subject or citizen; and being entitled to a
   subject's or citizen's rights or privileges. Each disqualifies on its own.
   Asserted.
3. Section 44(ii) turns on what the offence is **punishable** by (one year or
   longer), not on the sentence imposed. It lasts only while the person "is
   under sentence, or subject to be sentenced". An offence with a 6-month
   maximum does not disqualify. A served sentence for a 10-year offence does
   not either. Asserted.
4. The proviso to s 44(iv) saves Ministers of State and Commonwealth reservists
   (pay as an officer or member of the forces "whose services are not wholly
   employed by the Commonwealth"). It does not save a full-time member of the
   forces. A Crown pension disqualifies unless it is paid as an officer or
   member of the Queen's navy or army. Asserted.
5. Section 44(v) saves an interest held only as a member of an incorporated
   company of "more than twenty-five persons". A 25-member company does not
   qualify for the saving; a 26-member company does. Asserted.
6. Section 34 sets 21 years, elector status, 3 years' residence and being a
   subject of the Queen, but only "Until the Parliament otherwise provides".
   Once the Parliament has provided, a 20-year-old who meets its tests is
   qualified. Asserted.
7. Section 43 stops a sitting senator from being chosen for the House of
   Representatives, and a sitting member from being chosen for the Senate.
   Asserted.
8. Section 45 vacates a member's place for any s 44 disability, for taking the
   benefit of a bankruptcy or insolvency law, or for a fee or honorarium for
   services to the Commonwealth or in the Parliament. Asserted.
9. Section 46 as written makes a person who sits while incapable liable to
   £100 for each day, to anyone who sues. Ten days is £1,000. The section opens
   "Until the Parliament otherwise provides"; whether it has is not in this
   deposit. Asserted (as written).

## What would need doing before this is worth anything

- A decision on whether to encode the case-law glosses (reasonable steps;
  irremediable impediment; the time of choosing being nomination; what an
  "office of profit" and an "indirect pecuniary interest" are). Each changes
  answers. They need an owner's ruling and the judgments deposited.
- The law the Parliament has made in place of s 34 (Electoral Act s 163) and
  of s 46 (if any). These should be linked rather than asked.
- Italian Law 91/1992 art 11, or another foreign law, to answer whether a
  renunciation has taken effect. This encoding cannot answer it.
- The standard pipeline: coverage table, independent test pass, human gates.
