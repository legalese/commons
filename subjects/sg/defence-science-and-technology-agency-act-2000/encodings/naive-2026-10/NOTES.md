# Defence Science and Technology Agency Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DSTAA2000.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The last amending Act in its Legislative History is Act 5 of 2018
(Public Sector (Governance) Act 2018, s 57, in force 1 April 2018).

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0165** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

Most of the Act sets up a statutory board. This row takes only the provisions that
bind or protect a person: the employee's duty to stay on and the strike ban (s 11),
personal immunity (s 12), the Government's share of a transferred employee's pension
(s 24(4)), the symbol offence (s 31), secrecy (s 32), director disqualification and
quorum (First Schedule paras 10, 12(2)), and the duty to answer the auditor (Second
Schedule paras 8, 9). Not encoded: incorporation and the seal, board size, functions
and powers, ministerial directions, delegation, the Chief Executive, the financial
provisions, the 2000 transfer of property, contracts and proceedings, the other
transferred-employee protections, the annual report, regulations, and the rest of the
Schedules.

## What the Act turns out to say

### 1. An Agency employee can be ordered not to quit, and leaving anyway is a crime carrying 3 years

s 11(2): if the Minister thinks it "necessary for the public safety, defence or
security of Singapore", the Minister may require any employee to stay employed "for
such period as the Minister may determine". The decision "is final and is not subject
to appeal or review in any court" (s 11(3)). Leaving before the period ends is an
offence under s 11(5), with a fine of up to $2,000, up to 3 years' imprisonment, or
both. No reasonable-excuse defence is written. An employee who has not been told to
stay may resign freely. Asserted.

### 2. Strikes are banned, and so is any concerted go-slow

s 11(4): an employee "must not go on strike or instigate or incite others to take part
in or otherwise act in furtherance of any industrial action". "Industrial action" in
s 11(6) covers any concerted action that limits or delays work. The encoding treats
joining a go-slow or work-to-rule as acting "in furtherance" of it, which is a
reading of the sentence. A refusal by one person acting alone is neither a strike nor
industrial action, because both definitions need a body of persons acting in
combination. Only an Agency employee is caught: an outsider who urges Agency staff to
strike commits no offence under this section. Asserted.

### 3. Anyone, including a supplier, can be made to answer the auditor, unless the matter is secret

Second Schedule para 8: the auditor "may require any person" to give information
they hold or can access. This is not limited to the Agency's staff. The exception is
information on transactions the Permanent Secretary to the Ministry of Defence has
declared secret. Para 9 makes a failure without reasonable excuse, or any
hindrance, an offence. The fine is up to $1,000 plus $100 for each day or part of a
day the offence continues after conviction, so 30 days gives $4,000. There is no
imprisonment. The encoding reads "without reasonable excuse" as qualifying only the
failure to comply, not the hindrance. Asserted.

### 4. Secrecy binds former staff for life and covers other people's affairs too

s 32(1) applies to a person who "is or has been" a director, officer, employee or
agent, and covers information about "the affairs of the Agency or of any other
person". A supplier's tender price is therefore covered. The duty has no end date.
The exceptions are performing one's duties, a court's lawful requirement, and
disclosure required or allowed by written law. The maximum is $2,000 or 12 months.
s 32(3) adds that information the Minister certifies as secret "is not required to be
disclosed to Parliament or any other person". Asserted (s 32(1), (2)).

### 5. A past composition with creditors disqualifies a director, with no time limit

First Schedule para 10(b) bars anyone who "is an undischarged bankrupt **or has made**
any arrangement or composition with his or her creditors". The words set no time
limit, so on a literal reading an arrangement made decades ago still bars the
person. A conviction for dishonesty disqualifies whatever the sentence. Any prison
sentence of 6 months or more also disqualifies. In both cases a free pardon removes
the bar. Asserted.

### 6. The pension apportionment sentence is garbled

s 24(4) makes the Government liable for "such portion of any pension ... as the same
bears to the proportion which" Government emoluments bear to total emoluments. The
encoding reads this as pension × Government emoluments ÷ total emoluments. On that
reading $30,000 with $600,000 of Government and $400,000 of Agency emoluments gives
$18,000. Asserted.

### 7. The symbol offence needs no intent and no registration

s 31: the Agency has the exclusive right to "any symbol or representation that it
may select or devise". Using one that is identical, or confusingly similar, is an
offence with a maximum of $10,000 or 6 months. Neither intent nor registration is
required by the words. This is the largest fine in the Act. Asserted.

### 8. Quorum: one-third or 3, with the rounding left unsaid

First Schedule para 12(2): "one-third of the total number of directors or 3 directors,
whichever is the higher". When the total is not divisible by 3, the Act does not say
how to round. The encoding requires at least one-third to be present, which in
effect rounds up, so 4 of 13 is not a quorum. Whether the Chairperson counts in the
total is also unsaid. Asserted.

### 9. Immunity protects the individual, not the Agency

s 12 bars suits "personally" against directors, officers, employees and persons
acting under the Agency's direction, for good-faith acts in executing written law.
The Agency itself can still be sued (s 3(a)). Asserted (s 12).

## What would need doing before this is worth anything

- No regulations under s 33, and no case law on s 11 or s 32, were retrieved.
- The Public Sector (Governance) Act 2018 now governs directions, the Chief
  Executive's appointment and the board's proceedings. It was not read.
- The readings in findings 2, 3, 6 and 8 need a lawyer's view.
- The Official Secrets Act and other laws that may reach outsiders who disclose
  Agency information were not read.
