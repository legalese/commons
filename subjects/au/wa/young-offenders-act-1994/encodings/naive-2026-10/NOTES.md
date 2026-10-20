# Young Offenders Act 1994 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 49140,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_49140.txt`. The deposit names no compilation
number. Its compilation table ends with the Community Protection (Offender Reporting)
Amendment Act 2024 Pt 3 Div 2 Subdiv 4 (in force 31 December 2025); the last reprint
listed is Reprint 7 as at 1 June 2018. The uncommenced provisions table lists, among
others, the Young Offenders and Prisons Legislation Amendment Act 2024 Pt 3 (to be
proclaimed); it is not shown in the deposit and not encoded.

**Checks:** one module (`yoa-diversion.l4`), one case file
(`yoa-cases-diversion.l4`), 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **au/wa:REQ-0010** (priority 1), raised **4 times**, all by Jake Harding's
life (`au/wa/cradle-to-grave-jake`, born 2006-08-30):

- **k022** (2021-11-20, aged 15): after taking a phone case and earbuds worth $89 from a
  shop (k021), "What may police do with a 15-year-old instead of charging him, and which
  court if they charge?" The police refer him to a juvenile justice team.
- **k023** (2022-02-14): the team — an apology, restitution, community work. "What does a
  completed action plan do to the matter?"
- **k036** (2026-11-20, aged 20): "Does a juvenile justice team outcome leave a record that
  can be spent?"
- **k082** (2047-03-04, aged 40): a job form asks about convictions. "Must he disclose the
  2021 matter?"

The ledger lists s 7, ss 22-23, ss 24-30 and s 30. This encoding takes those questions
and what they need: who is a young person (ss 3, 4), cautions (ss 22A-23), referral to a
team (ss 25, 27, 29), the team's proceedings (ss 30-32), the effect of completing the
terms (s 33), the police's options (s 41), the Department's record (s 14), and — for the
court path Jake does not take — when a conviction is recorded (s 55). Not encoded: which
court (the Children's Court of Western Australia Act 1988 s 19, a separate subject); the
contents of Schedules 1 and 2 (an input); bail and custody (Part 4); sentencing beyond
s 55; and the Spent Convictions Act 1988, which k036 and k082 also cite.

## What the Act turns out to say

### 1. The sections the scenario cites for the outcome are the wrong ones

The scenario cites "ss 29-30 (effect of completing the action plan)" and "s 30 (no
conviction recorded)". In this compilation s 29 is "First offenders usually should be
referred to team" and s 30 is "Role of responsible adult". The effect of completing the
team's terms is **s 33**, and recording a conviction is **s 55**. Both are encoded; the
ledger entry's provision list should be read with that correction. Asserted (s 33, s 55).

### 2. A completed plan does not end the matter; it makes a later charge fail

The scenario says "no charge, no conviction". s 33(1): referral "does not prevent a charge
from being subsequently laid". s 33(2): if the young person "has complied with the terms",
a court hearing the charge "must dismiss the charge without determining it". s 33(3): if
he only partly complied, the court is to have regard to the steps he took. The protection
is real, but it works at the court door, not by extinguishing the matter. Asserted.

### 3. "Nothing recorded" is not what the Act says

The scenario's k036 says "nothing was recorded" and the abridged text says "nothing
recorded". s 14(1): the chief executive officer "is to keep records of every young person
who is ... dealt with under this Act for an offence", including (s 14(2)(d)(i)) how "terms
specified by a juvenile justice team ... have been, complied with". s 15(3)(b) lets the
CEO tell a person with "a proper interest" how an alleged offender was dealt with by a
team. What the Act does not create is a court finding of guilt or a conviction: s 55
operates only when a court "finds a young person guilty" (the "no finding, no conviction"
reading is an inference). So there is a departmental record but no conviction — whether
there is anything to spend or disclose is for the Spent Convictions Act 1988 and the job
form's wording, not this Act. Asserted (s 14; s 55 on a finding of guilt).

### 4. The caution test looks backwards, and it ranks a caution only above a charge

k022's title says "a caution is not enough for a second offence of the night". s 23(1)
displaces the preference for a caution only "because of the number of previous offences
with which the person has been charged or for which the person has been dealt with under
this Part". Two offences the same night, neither yet charged or dealt with, are not that
(an inference from the words; the scenario's reason is not the Act's test). But s 23
prefers a caution "in preference to laying a charge"; a referral under s 27 is made
"instead of laying a charge", so s 23 does not forbid referring rather than cautioning, and
s 29(1) requires the discretion to favour referral for a young person who "has not
previously offended". The police's choice is open to them; their stated reason is not
the statutory one. Asserted (ss 22, 23, 27, 29).

### 5. A first-offender preference that past diversion does not use up

s 29(2): a young person is not "taken to have previously offended against the law merely
because" he was cautioned, given an infringement notice, accepted responsibility, or
agreed to or complied with a team's terms. A second matter after a caution still gets the
s 29(1) preference. Asserted.

### 6. A Weapons Act offence can go to a team but cannot be cautioned

s 22(3)(b) bars a caution for offences under the Weapons Act 1999 s 6(1), 6A(1) or (2) or
6B(1) or (2); s 25(1) bars referral only for Schedule 1 and Schedule 2 offences. Asserted.

### 7. The team needs a responsible adult — or an independent 17-year-old

s 30(1): the team can only proceed if a responsible adult is present and agrees; s 30(3)
lets it dispense with that for an "independent young person", who under s 3 must have
"reached the age of 17 years". At 15 Jake cannot be one. A victim who is present has a veto
over the disposal (s 31(2)). Asserted.

### 8. Once a young person, always a young person for that offence

s 4: if the offence was committed before 18, the Act "applies to the person as a young
person for purposes connected with that offence". At 40 (k082) Jake is still a young
person for the 2021 matter. Asserted (age in completed years from the scenario's dates).

### 9. In court, a conviction is the exception for ordinary offences

Had Jake been charged and found guilty, s 55(2): for an offence outside Schedules 1 and 2
without a custodial sentence, "the court is not to record a conviction unless it is
satisfied that there are exceptional reasons". Even unrecorded, he would be deemed convicted
for consequential orders, licence disqualification under a road law and appeals, "but not
for any other purpose" (s 55(4)). Asserted.

## What would need doing before this is worth anything

- Schedules 1 and 2 encoded as lists, so that "is this a Schedule offence?" is decided
  rather than input. Plain stealing is assumed not to be one; only Criminal Code s 378(2)
  (motor vehicle, aggravated) was seen in Schedule 2.
- Whether an infringement notice can be given for stealing (s 25(2)) depends on other
  written laws and regulations not retrieved; the scenario's facts do not say.
- The regulations under s 14(3) on destroying records were not retrieved.
- The Children's Court of Western Australia Act 1988 s 19 (which court) and the Spent
  Convictions Act 1988 (k036, k082) need their own encodings for the lives' questions to be
  fully answered.
- No WA Police guidance on cautioning, and no case law, was searched.
