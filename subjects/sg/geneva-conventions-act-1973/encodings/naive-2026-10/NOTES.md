# Geneva Conventions Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021"; the latest amendment annotated is
Act 40 of 2019 (in s 6(2), commenced 2 January 2021). Part IV is omitted from the
deposit "as having had its effect".

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0127** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

For an ordinary person or business, the Act's reach is Part 3: the ban on using the
red cross and related emblems (ss 8 to 11). Part 2 (grave breaches and the trial
safeguards for protected prisoners of war and internees, ss 3 to 7) is encoded too,
because it is the rest of the operative Act and is short. The four Conventions and the
Protocol in the Schedules (most of the deposit's length) are not encoded, except the
four Articles that list the grave breaches s 3 punishes. Also not encoded: the
Minister's certificate under s 3(4), subordinate military courts (s 3(5)), the
contents and proof of a s 4 notice, the assignment and payment of counsel (s 5(3),
(4)), and inspectors' investigative powers (s 10A(2), (3)).

## What the Act turns out to say

### 1. A pharmacy, clinic or brand cannot use a red cross without the Minister's authority

s 8 forbids using "for any purpose in Singapore" the red cross, red crescent, red
crystal or red lion and sun emblem, or the words "Red Cross" or "Geneva Cross",
"without the Minister's authority". s 9 adds the Swiss Arms cross, colourable
imitations of it and of the four emblems, and words "so nearly resembling" Red Cross
as to refer to the emblem. Any contravention is an offence under s 10: up to $10,000
or 6 months or both, **and** the goods bearing the mark are forfeited. With the
Minister's authority there is no offence. Asserted.

### 2. s 9 has no "in Singapore"; s 8 does

s 8 is limited to use "in Singapore". s 9 says "for any purpose whatsoever", with no
place. Read literally, the encoding makes using an *imitation* of the red cross outside
Singapore an offence, while using the *genuine* red cross emblem outside Singapore is
not caught by s 8. Whether a court would read a territorial limit into s 9 is an
inference question the text does not answer. Asserted (on the literal reading).

### 3. Grave breaches are punishable whoever and wherever

s 3(1) applies to "any person, whatever his or her citizenship or nationality, who,
whether in or outside Singapore" commits, aids, abets or procures a grave breach. Wilful
killing of a protected person carries life imprisonment; any other grave breach up to
14 years. What counts as a grave breach differs by Convention: property destruction is
listed in the First, Second and Fourth (Arts 50, 51, 147) but not the Third (Art 130);
hostage-taking and unlawful deportation or confinement only in the Fourth (Art 147).
Only the High Court can try it (s 3(3) excludes Magistrates' and District Courts), and
only on proceedings by or on behalf of the Public Prosecutor. Asserted.

### 4. A protected prisoner of war cannot be tried for anything without 3 weeks' notice and 14 days' counsel

s 4: the court must not proceed until notice was served on the Protecting Power "not
less than 3 weeks previously" (taken as 21 days). This applies to a prisoner of war
for **any** offence, but to an internee only if the court can sentence to death or to
2 years or more. s 5: anyone tried under s 3, and any prisoner of war, must be
represented by counsel instructed at least 14 days before trial. Asserted.

### 5. Appeal within 10 days, counted from a different event

s 6: a protected prisoner of war or internee sentenced to death or to 2 years or more
may appeal, and "despite section 377(2) of the Criminal Procedure Code 2010" the notice
must be given within 10 days after receiving notice that the Protecting Power has been
notified of the conviction and sentence. Asserted.

### 6. The Minister may credit remand time and move a POW to military custody

s 7(1): the Minister may deduct up to the time spent in custody before sentence. s 7(2):
after an aggregate of at least 3 months in custody, a prisoner of war may be moved to
SAF custody. Both are discretions ("It is lawful for the Minister"); the encoding
gives only the ceiling and the eligibility. Asserted.

### 7. Officers, inspectors and the Public Prosecutor

s 10(2): an officer of a body corporate or society who consented or connived is guilty
as well as the body. s 10A(4): refusing, answering falsely, failing to comply with, or
wilfully obstructing an inspector, "without lawful excuse", is an offence with the same
$10,000 or 6 months maximum. s 11: no Part 3 proceedings without the Public
Prosecutor's consent. Asserted.

## What would need doing before this is worth anything

- No authorisations given by the Minister under ss 8 and 9 (for example to the
  Singapore Red Cross Society or to medical services) were looked for; who holds one
  decides almost every real case.
- The meaning of "colourable imitation" and the territorial reach of s 9 need case law,
  none of which was searched.
- The Conventions themselves (who is a "protected person", Article 2 on when a
  Convention applies) are not encoded; s 3 here takes protection as an input.
- Regulations or orders under s 5(4) (counsel's fees and assignment) were not retrieved.
