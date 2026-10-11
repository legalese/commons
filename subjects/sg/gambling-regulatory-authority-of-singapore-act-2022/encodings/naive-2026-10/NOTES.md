# Gambling Regulatory Authority of Singapore Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 14 of 2022, informal consolidation, "version in force from 30/10/2024",
as deposited at `../../registers/source-bundle/GRASA2022.txt`. The only amendment
annotated in the deposit is Act 29 of 2024 (wef 30/10/2024), to s 5(1)(d) and (5). The
deposit has no legislative history table.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0148** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is institutional. It continues the Casino Regulatory Authority as the Gambling
Regulatory Authority of Singapore (s 3) and sets out its constitution, procedure and
finances. It licenses nothing: the licensing of gambling is in the Gambling Control Act
2022 and the Casino Control Act 2006. So this row takes what a member of the public, a
business, a would-be member or an insider actually meets: the s 2 meaning of "gambling",
the symbol offence (s 8), disqualification, term, resignation and loss of seat (ss 11,
16, 18, 20), quorum and resolutions (ss 23, 25), secrecy (s 34), protection from
liability (s 35), compounding (s 43), liability of a corporation's officers (s 44) and
service of documents on an individual (s 46).

Not encoded: functions and powers (ss 5, 6), Ministerial directions (s 7), appointment
mechanics (ss 9, 10, 12 to 15, 17), presiding and execution of documents (ss 24, 26),
committees and delegation (ss 27 to 30), personnel and finance (ss 31 to 33, 36 to 42),
unincorporated associations and partnerships (s 45, which mirrors s 44), service on
partnerships and bodies corporate (s 46(3), (4)), regulations (s 47), the amendments to
the Casino Control Act, Gambling Duties Act, Singapore Totalisator Board Act and other
Acts (Part 8), and the savings (Part 9).

## What the Act turns out to say

### 1. The permission exception in the symbol offence covers only identical symbols

s 8(2)(a) makes it an offence to use a symbol identical with the Authority's "without the
prior written permission of the Authority". Paragraph (b), using a symbol that "so
resembles" it as to deceive or cause confusion, has no permission exception. Read
literally, a confusingly similar symbol is an offence even with permission. Whether a
court would read the permission into (b) is not decided here. The maximum is $10,000 or
6 months or both, plus up to $250 a day (or part day) for a continuing offence after
conviction. Asserted.

### 2. An insider who leaks faces two years' jail but only a $2,000 fine

s 34 forbids a member, employee, delegate, subdelegate, the Chief Executive or a committee
member from disclosing information they hold only because of the role, except for the
Authority's functions, with its prior authorisation, for proceedings for an offence under
the Act, under a court order, in disclosing interests, or as an Act requires or allows.
The penalty is "a fine not exceeding $2,000 or to imprisonment for a term not exceeding 2
years or to both", which pairs a low fine with a long prison term. If the offence is
prescribed as compoundable, s 43 caps the composition at the lower of half the maximum
fine and $2,000, which here is $1,000. Asserted.

### 3. Silence is a vote in favour

s 25(4) presumes that a member present has "agreed to, and ... voted in favour of" a
resolution unless he or she expressly dissents or votes against. So a resolution passes
if nobody dissents, or if a majority votes for it, and on a tie the presiding member's
casting vote decides (s 25(2)). The encoding reads "a majority of the members who are
entitled to vote" as a majority of those present and entitled. That is an inference: the
words could also mean all members entitled to vote, whether present or not. Asserted.

### 4. Quorum is one-third, with a floor of 3, and the Act does not say how to round

s 23(1): "one-third the number of members or 3 members, whichever is higher". The
Authority has 5 to 17 members (s 9). With 10 members one-third is 3⅓. The encoding
requires at least one-third, so 3 of 10 is not a quorum and 4 is (an inference). With 5
members the floor of 3 applies. Asserted.

### 5. The liability shield needs reasonable care as well as good faith

s 35 protects members, staff, delegates and anyone acting under the Authority's direction
only for acts done "in good faith and with reasonable care". Section 48(4) inserted the
same words "and with reasonable care" into s 192 of the Casino Control Act 2006.
Asserted for s 35. The amendment to s 192 was read but not encoded.

### 6. Officers are liable whether or not the company is convicted

s 44(2): an officer, or a manager able to influence the company's conduct, is guilty of
the company's offence if he or she consented, connived or conspired, was knowingly
concerned, or "knew or ought reasonably to have known" of the offence and failed to take
all reasonable steps to prevent or stop it. Under s 44(5) this applies "whether or not the
corporation is convicted". "Corporation" includes a limited liability partnership.
Asserted.

### 7. A posted notice is served two days later, even if it comes back

s 46(6)(c): service by post takes effect "2 days after the day the document was posted
(even if it is returned undelivered)". Email and electronic notice need the person's prior
consent (s 46(7)), and a summons cannot be served by electronic notice (s 46(5)). Affixing
a copy at the person's home or business address is always available (s 46(2)(d)).
Asserted.

### 8. Disqualification from membership, term and losing the seat

s 11(2) disqualifies undischarged bankrupts and people in an arrangement with creditors,
Judges and judicial officers, anyone sentenced to imprisonment "for a term of 6 months or
more" who has no free pardon, disqualified company directors, and people who lack mental
capacity or are under a mental health order. A term is 3 years or a shorter period set in
the instrument (s 18). A resignation takes effect when the Minister receives it or at a
later time it names (s 16(2)). Missing 3 consecutive meetings without the Authority's
approval ends membership (s 20(1)(g)), and no compensation is payable for losing office
(s 20(2)). Asserted, except s 20(2).

### 9. "Gambling" includes games that are only partly chance

s 2 defines gambling to include lotteries, games of chance ("which includes a game that is
partly a game of chance and partly a game requiring skill") and betting or bookmaking, but
not social gambling. Social gambling takes its meaning from the Gambling Control Act 2022,
which was not read for this row. The definition says "includes", so it is not exhaustive.
Asserted.

## What would need doing before this is worth anything

- Read the Gambling Control Act 2022 meaning of "social gambling" to give s 2 its full
  effect.
- Find out which offences, if any, are prescribed as compoundable under s 43. No
  regulations were retrieved.
- Settle the readings of "majority of the members who are entitled to vote" (s 25(3)) and
  how to round the quorum (s 23(1)).
- Encode s 45 (unincorporated associations and partnerships) and service on firms and
  companies (s 46(3), (4)).
- No case law was searched.
