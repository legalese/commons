# Medical (Therapy, Education and Research) Act 1972 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `../../registers/source-bundle/MTERA1972.txt`.
The deposit says it "incorporates all amendments up to and including 1 December 2021
and comes into operation on 31 December 2021"; its page footer reads "Informal
Consolidation – version in force from 1/5/2023". The latest amending Act in its
Legislative History is Act 11 of 2023 (Healthcare Services (Amendment) Act 2023,
commenced 1 May 2023), annotated against s 2, s 2A, s 12 and s 15. Section numbers
follow the body: the arrangement at the top of the deposit is out of step.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0184**: tier 3 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. For a person
the answer is: whether and how they can give their body (or a part of it) or authorise
their own post-mortem, how to revoke a gift, and what their family, a hospital and the
Director-General may do with their body after death. The Act has 17 sections and one
Schedule, so nearly all of it is encoded: ss 3 to 5, 7 to 10, 12 to 17 and the
Schedule. Not encoded: the short title, definitions beyond their effect, the
appointment of designated officers (s 2A), the gazetting of approved institutions
(s 2B), the examination a gift authorises (s 6), the donee's duty to remove a part
"without unnecessary mutilation" and the custody of the remainder (s 11(2), (3)), and
the Coroners Act 2010 and Interpretation Act 1965 provisions that s 16 points to (not
read for this row).

## What the Act turns out to say

### 1. An unclaimed body can be used without anyone's consent after 24 hours

Where a body "has not been claimed from an approved hospital or from an institution
maintained on public funds, for more than 24 hours after death", the Director-General
may authorise in writing its use for education, research, therapy or transplantation
(s 12), or its post-mortem (s 15). Unlike ss 4 and 5, neither section mentions the
deceased's contrary wishes. Exactly 24 hours is not enough. Under s 2,
"Director-General" includes a designated officer of an approved hospital or a public
officer authorised in writing by the Director-General of Health. Asserted.

### 2. The family acts in strict order, and only an equal or senior objection counts

After death or immediately before it, a person in the Schedule may give the body or
authorise a post-mortem "when persons in prior classes are not available": spouse,
then adult child, parent, adult sibling, guardian, and anyone obliged to dispose of the
body (ss 4, 14). The gift is barred by actual notice of the deceased's contrary
indications or of opposition from "the same class or a prior class"; an adult child's
objection does not stop the spouse. A minor child and a friend are not in the Schedule.
The donee must refuse on the same notice (s 5). Asserted.

### 3. A gift of one's own body needs 18 years, sound mind, and writing or two witnesses

s 3: anyone "not mentally disordered" and 18 or above. s 8: in writing at any time, or
orally before 2 or more witnesses during a last illness. An oral gift made while well is
not a valid form. A post-mortem authority under s 13 has the same capacity and form.
Revocation is open "at any time" by a signed statement delivered to the donee, an oral
statement before 2 or more persons communicated to the donee, or a written document
found on the donor's person or in the donor's effects (s 9). Asserted.

### 4. An individual can receive a part only for his or her own treatment

s 7(c): a specified individual may be a donee only "for therapy or transplantation
needed by the individual"; approved hospitals and schools may take for education,
research, science, therapy or transplantation (s 7(a), (b)). A gift naming no donee may
be accepted only by the designated officer of the approved hospital where the death
occurred or to which the body was taken, and only for the s 7(a) or (b) purposes
(s 10(2)). The Act lists no other purpose; the encoding's "commercial sale" test case
fails because it is not listed, not because the Act forbids it in terms (inference).
Asserted.

### 5. No offences, but lawfulness depends on a doctor or the Coroner

The Act creates no offence and no penalty. s 16(1) declares removal and use under
s 3, 4 or 12, and a post-mortem under Part 3, lawful; s 16(2) allows it only by a
registered medical practitioner satisfied that the death was determined and certified,
or where the Coroner has ordered release of the body under s 22(3)(c) of the Coroners
Act 2010. Read literally, limb (b) does not say who performs the removal; the encoding
follows the words. s 17 leaves the Coroner's power to direct a post-mortem untouched by
ss 3, 4, 13, 14 and 15, so a family refusal does not bind the Coroner. Asserted.

### 6. The arrangement and s 2 carry traces of the 2023 amendment

The arrangement of sections at the top of the deposit is shifted (it numbers
"Appointment of designated officers" as 1), and s 2 shows a definition "[Deleted by Act
11 of 2023 wef 01/05/2023]" without saying what it was. Not asserted.

## What would need doing before this is worth anything

- The Human Organ Transplant Act and any other statute governing organ donation in
  Singapore were not read; how this Act sits beside them is unknown here.
- The Gazette notifications under s 2B (which institutions are approved) were not
  retrieved.
- Coroners Act 2010 s 22(3)(c) and Interpretation Act 1965 s 2A were not read.
- "Adult" in the Schedule is not defined in this Act; the encoding takes it as given.
- No case law was searched.
