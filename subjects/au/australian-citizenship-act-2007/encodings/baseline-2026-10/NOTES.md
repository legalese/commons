# Australian Citizenship Act 2007 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design
defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export` and a `@desc` on each
input. This encoding replaces the first-pass encoding `naive-2026-10`. It covers
everything that one covered and keeps its hand-checked values where they are still
right. Finding 1 below corrects one of them.

## Edition

- **The Act:** Compilation No. 37, compilation date 4 June 2026 ("Includes
  amendments: Act No. 75, 2025"; register id C2026C00236). Deposited at
  `../../registers/source-bundle/C2007A00020.txt` (retrieved 2026-09-22).
- **Australian Citizenship Regulation 2016:** Compilation No. 23, compilation date
  1 July 2026 (register id F2026C00596). Deposited at
  `subjects/au/australian-citizenship-regulation-2016/registers/source-bundle/F2016L01916.txt`
  (retrieved 2026-10-19). Used: s 6 (registration), s 9 (prescribed reasons for not
  pledging), s 10 (pledge arrangements), s 16 and Schedule 3 (fees).
- **Australian Citizenship (Transitionals and Consequentials) Act 2007:** Compilation
  No. 5, compilation date 1 July 2015 (register id C2015C00383). Deposited at
  `subjects/au/australian-citizenship-transitionals-and-consequentials-act-2007/registers/source-bundle/C2007A00021.txt`.
  Used: Schedule 3 items 1 and 4.

## Checks

- One module (`aca-citizenship.l4`) and one case file (`aca-cases-citizenship.l4`).
- **66 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS Code
  extension 1.6.98.
- The case file is built by `gen_australian-citizenship-act-2007_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.

Facts the lives do not state are **assumptions**, labelled in the case file:

- Graham's and Sue's citizenship;
- that Chloe, Jake and Oliver lived in Australia for their first ten years;
- Priya's application date (1 Mar 2030) and approval date (15 May 2030);
- when the London year ended;
- Anjali's approval date (1 Sep 2027), and that she applied alone.

## Seat

**The child born in or outside Australia, and the applicant for conferral.** These
are the people the Act is applied to in every event the lives cite. They ask "Am I a
citizen?", "Am I eligible?" and "What must I do?". The citizen who asks whether they
could renounce (s 33) shares the seat. Parents appear only as facts about the child.

Where a provision speaks to the Minister (ss 17, 24, 25, 33), the encoding says what
it means for the person: the Minister must approve, may approve, may refuse, or must
not approve.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed.
  - The Regulation sets the registration manner, the prescribed reasons, the pledge
    arrangements and the fees.
  - The Transitionals Act is also brought in. It is not a regulation, but Schedule 3
    item 4 sets the date from which s 12(1)(a) applies. Without it the lives' births
    are answered wrongly (finding 1).
  - The 1948 Act is not deposited. Its answers are inputs.
- **The actors the text names.** Followed: the person, a parent, the Minister, the
  person before whom the pledge is made.
- **A judgment handed to someone else is answered conditionally.** Followed. Each one
  is an input named for the Minister's satisfaction ("the Minister is satisfied of
  good character", "the Minister applied s 22(9) or (11)"). Because of s 24(2), an
  eligible applicant is told only that the Minister **may** approve.
- **The Act's definitions worked out from facts; borrowed terms asked as facts.**
  Followed.
  - Worked out: "permanent resident" (s 5) and the general residence requirement
    (s 22).
  - Asked as facts: "permanent visa", "unlawful non-citizen", "ordinarily resident",
    "enemy alien" and "national".
- **One case is the text's natural unit.** Followed: one birth, one application.
- **The Act's own terms, with a gloss.** Followed. Each input carries a plain `@desc`.
- **Operative sections in scope, machinery out.** Followed. Personal identifiers,
  evidence, review, delegation and the regulation-making power are out.
  - Departure: the s 46 fee is in, through Schedule 3. It is a number the applicant
    must pay to apply at all.

## The lives

- **chloe c000** (born KEMH, 14 Mar 2003). *Am I a citizen by birth under s 12?* No,
  not at birth. Her citizenship then is a 1948 Act question (input). She is a citizen
  under s 12(1)(b) from her tenth birthday in 2013, and under s 4(1) today.
- **chloe c062** (Oliver, 5 Sep 2030). *Is Oliver a citizen by birth?* Yes, under
  s 12(1)(a).
- **jake k000** (born KEMH, 30 Aug 2006). As Chloe: not under s 12 at birth; under
  s 12(1)(b) from 2016.
- **jake k051** (Ruby, Armadale, 22 Jan 2033, parents unmarried). *Is Ruby a citizen
  by birth?* Yes. Marriage is irrelevant.
- **daniel d000** (born KEMH, 9 Apr 1996). *Am I a citizen by birth under s 12?* No,
  never. His citizenship rests on s 4(1)(b) and the 1948 Act.
- **daniel d036** (Anjali, London, 14 Jun 2027). Three questions:
  - *Am I eligible by descent?* Yes.
  - *Must the Minister approve?* Yes, once satisfied of identity, with no bar.
  - *Am I a citizen on the day I was born?* No. She becomes one on the approval day.

  Registration follows approval. The fee is $380.
- **daniel d040** (Luca, Perth, 2 Feb 2030). *Is Luca a citizen by birth?* Yes.
- **daniel d041** (Priya, citizen 20 Jul 2030). Questions asked:
  - *Do I satisfy the general residence requirement?*
  - *Am I eligible?*
  - *May the Minister approve me?*
  - *Must I pledge?*
  - *On what day do I become a citizen?* The pledge day.
  - *Must I give up my other citizenship?* No.
  - *What is the fee?* $595.

## Why this scope

The plan entry names ss 12, 16, 21, 22 and 26, and the deposited Regulation for
prescribed matters. Those sections need the definitions and the following steps
before they answer the lives:

- the definitions (ss 4, 5);
- the Minister's decisions (ss 17, 24);
- the day citizenship begins (ss 19, 19A, 20, 28);
- the pledge's timing and form (ss 26(2)-(6), 27, Regulation s 10);
- cancellation (s 25(3), Regulation s 9).

Renunciation (s 33) is in because the brief's seat names it. No life renounces
Australian citizenship (finding 9).

Left out:

- adoption, abandoned children and Hague adoptions;
- s 16(3) (births before 26 January 1949);
- the other conferral routes, s 21(3)-(8), except as pledge exemptions and fee items;
- the special residence and defence service requirements;
- children applying with a parent;
- resumption, revocation and cessation;
- the content of the citizenship test. The s 23A determination is "not a legislative
  instrument" (s 23A(7)) and was not retrieved.

## What the Act turns out to say

### 1. Chloe, Jake and Daniel are not citizens "by birth (s 12)" at birth. The Transitionals Act says so

The lives cite s 12 for births in 1996, 2003 and 2006. The deposited Transitionals Act
Schedule 3 item 4(1) says: "Paragraph 12(1)(a) of the new Act applies to a person born
on or after the commencement day" (1 July 2007). So none of the three was a citizen
under s 12(1)(a).

Their citizenship at birth is a question for the 1948 Act (ss 4(2), 5(3)). Today it
rests on s 4(1)(b): a citizen under the 1948 Act immediately before 1 July 2007 who
has not ceased to be one.

This corrects the naive encoding, which gave all three s 12 citizenship and flagged
the point only as an unread question. Asserted.

### 2. Chloe and Jake do reach s 12 at ten. Daniel never does

Item 4(2) applies s 12(1)(b) to a person born before 1 July 2007 who had not, by
then, been ordinarily resident in Australia for the 10 years from birth.

- Chloe's tenth year ended in 2013 and Jake's in 2016. Both become s 12 citizens then,
  on the assumed facts.
- Daniel's ended in April 2006, before the Act. Item 4(2) does not reach him, so his
  Australian citizenship rests only on the 1948 Act.

Asserted.

### 3. Anjali is not a citizen at birth. She becomes one on the day the Minister approves, and registration is a database entry

s 16 makes her **eligible**. Daniel is a citizen, not by descent, so the two-year
condition does not apply. She is under 18, so no character test applies.

s 17(2): the Minister **must** approve once satisfied of identity, with no security
or cessation bar. There is no residual discretion.

s 19: she becomes a citizen "on the day on which the Minister approves".

s 18 and Regulation s 6: registration is "making a record ... and including the
record on a data storage system kept by the Department". It follows approval. It is
not something done at Australia House, as the life puts it, and it is not the step
that confers citizenship. Asserted.

### 4. Priya's London year sits on the 12-month line, and nothing in the lives says which side

s 22(1A) treats absences as presence only if "the total period of the absence or
absences was not more than 12 months". One day over, and none of the absence counts.

She left on 9 Jan 2027 for "a year". Applying in 2030, she meets the requirement if
she was back within 12 months and fails if not. Asserted both ways (from the naive
encoding).

### 5. Had she applied soon after London, only the spouse discretion would have saved her

s 22(1B) forgives only "not more than 90 days" abroad in the final 12 months: 90
passes, 100 fails. On the assumed dates, a mid-2028 application had 221 days abroad,
so it fails.

It succeeds only if the Minister applies s 22(9) (spouse of a citizen, permanent
resident while abroad, close and continuing association). If the Minister does,
s 24(5) also lifts the rule that she must be in Australia at the decision. Asserted.

### 6. Priya became a citizen on the day she pledged, not on approval

s 26(1): an applicant aged 16 or over must pledge unless incapacitated or covered by
s 21(6)-(8). s 28(1): a person required to pledge becomes a citizen "on the day on
which the person makes the pledge". A pledge before approval "is of no effect"
(s 26(2)).

The pledge must use a Schedule 1 form (s 27(1)) and be made before the Minister or an
authorised person (s 27(3)). Regulation s 10 adds two arrangements: it must be made in
public "if it is reasonably practicable", and the presiding officer must read the
Schedule 1 address aloud.

The Act does not say what follows from a pledge made outside those arrangements. The
encoding reports only whether they were met (inference). Asserted.

### 7. Missing the 12-month pledge window is excused only on the Regulation's terms

s 25(3) lets the Minister cancel an approval if the person has not pledged within 12
months of notice, unless the reason is prescribed. Regulation s 9 prescribes three:

- a s 26(3) delay determination;
- being overseas for treatment not available in Australia, unexpected
  hospitalisation, caring for the critically ill, or a funeral;
- a government administrative error.

The last two count only with "a signed statement" and "written evidence" (s 9(5)).
Being overseas without them is not a prescribed reason. Asserted.

### 8. The Act asks nothing about what Priya gives up

Nothing in ss 21-28 makes renouncing another citizenship a condition of conferral.
Her loss of Indian citizenship is Indian law. This reads what the provisions leave
out. Asserted.

### 9. s 33 cannot help anyone in the lives, and it cannot leave a person stateless

s 33 is renunciation of **Australian** citizenship. Daniel's 2040 renunciation (of
Italian citizenship, for s 44 of the Constitution) and Priya's loss of Indian
citizenship are foreign law.

Under s 33 the Minister **must** approve an adult who was a foreign national at
application (s 33(3)(a)), or a person whose country of birth or residence bars its
citizenship to Australians (s 33(3)(b)). The Minister must **not** approve without
identity, against "the interests of Australia", or unless the person is or will
immediately become a foreign national (s 33(7)). In wartime the Minister may refuse a
foreign national.

An adult who will acquire a foreign citizenship only once released from Australian
citizenship is outside s 33(3)(a). Nothing obliges the Minister either way. The fee
is $320. Asserted.

### 10. On the 2026 fee schedule Priya pays $595, Anjali $380. One fee item never applies

Regulation Schedule 3 sets these fees:

- item 2: $380 for a s 16 application ($160 for later siblings applying together,
  item 1);
- item 14: $595 for a general-criteria conferral application;
- item 13: $85 with a pensioner concession card;
- item 18: $365 for a re-application after sitting the test;
- item 15: nil for a child under 16 applying with a parent.

Item 17 ($40) excludes "an application mentioned in item ... 13". Item 13 already
takes every concession-card, general-criteria application outside items 5-9 and 15.
So item 17 appears never to set the fee, although Regulation s 17(4) still refers to
it. That is an inference from the order of exclusions.

The fees are those compiled at 1 July 2026. The 2027 and 2030 applications would pay
whatever the schedule then says. Asserted for the 2026 schedule.

### 11. Eligible is not approved

s 24(2): "The Minister may refuse to approve the person becoming an Australian
citizen despite the person being eligible". For conferral the encoding can say only
that the Minister **may** approve. For descent (s 17(2)) it can say **must**.
Asserted.

## What would need doing before this is worth anything

- Deposit and encode the Australian Citizenship Act 1948, as in force over time. The
  three pre-2007 births could then be answered rather than taken as inputs.
- The scenario facts need:
  - Graham's and Sue's citizenship;
  - Priya's application date;
  - the end of the London year;
  - whether Anjali applied with a sibling.
- The lives' "by birth (s 12)" for Chloe, Jake and Daniel should be corrected to
  "under the 1948 Act (s 4(1)(b))". For Chloe and Jake, add "and s 12(1)(b) from their
  tenth birthdays".
- The s 23A test determination, the s 5(2) determination and the fee schedule in
  force in 2027 and 2030 were not retrieved.
- "12 months" in s 22(1A) is a yes/no input. How it is counted in days was not
  settled.
- s 22(4A), the special residence requirements and the child-with-parent rules were
  not modelled.
- No case law or departmental policy was searched.
