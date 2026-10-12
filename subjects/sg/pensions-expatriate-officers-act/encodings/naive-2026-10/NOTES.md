# Pensions (Expatriate Officers) Act — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate.

**Edition:** 1985 Revised Edition (Chapter 226), informal consolidation, "version in
force from 30/3/1987", deposited as `../../registers/source-bundle/PEOA1976.txt`.
Original enactment Act 17 of 1976, commenced 1 October 1976. The legislative history
in the deposit lists no amendment after the 1985 Revised Edition.

**Checks:** one case file, 33 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0197** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person it applies to; no scenario has asked a sharper question yet.

The Act has three sections, and s 1 is the short title, so nothing is scoped out of
the Act itself: ss 2 and 3 are encoded whole. What is not encoded is everything the
Act points at: the 1976 Public Officers' Pension (Singapore) Agreement, the 1964
Public Officers Agreement, the pension the United Kingdom pays, and the three
Singapore laws it disapplies. None of them is in the deposit, so whether the 1964
Agreement applied to someone, and whether the UK has assumed responsibility for his
pension, are taken as given facts.

## What the Act turns out to say

### 1. The Act grants nothing; it only switches Singapore pension law off

s 3 is the only operative provision, and all it does is make "the law relating to
pensions" "cease to apply" to an officer, his widow, child or legal personal
representative once the United Kingdom has assumed responsibility for paying the
pension under the 1976 Agreement. What the person then receives, and from whom, is
in the Agreement, not in the Act. The encoding can say only whether the Singapore
law stops applying. Asserted.

### 2. Becoming a citizen later does not stop you being an "officer"

The s 2 definition has two limbs joined by "or". The first looks only at 1 April 1971:
anyone covered by the 1964 Agreement who "was not a citizen of Singapore on 1st April
1971" is an officer, even if he later naturalised and retired a citizen. The second
limb catches a citizen of 1971 who retired or died in service "after that date" and
was not a citizen at that time. Read strictly, retiring on 1 April 1971 itself is not
"after" it, and a 1971 citizen who has lost citizenship but is still serving is not
yet an officer. Asserted.

### 3. The Act commenced in October 1976, but nothing ceased until 1 January 1978

The Act commenced on 1 October 1976. s 3 takes effect "With effect from 1st January
1978", which the footnote explains as "The appointed day for the purpose of the
Agreement, as mutually arranged" between the two Governments. On any date before
that, s 3 leaves the Singapore law in place. Asserted at 1 October 1976, 31 December
1977 and 1 January 1978.

### 4. The list of laws is closed, and only four kinds of person are reached

"Law relating to pensions" *means* the Retirement from the Public Service
(Compensation) Ordinance 1956, the Pensions Act [Cap. 225] and its regulations, and
the Widows' and Orphans' Pension Act [Cap. 350]. Any other law, such as the Central
Provident Fund Act (named in the tests only as a law the list leaves out), is not
touched. s 3 reaches the officer, "his widow or child" and "his legal personal
representative", and no other dependant. Asserted.

### 5. Two readings were chosen where the text is open

"In respect of whom" the UK has assumed responsibility is read as attaching to the
person claiming, not only to the officer. That is an inference: the text could be
read either way. Whether "widow" includes a widower is not settled by this text and
is not encoded.

## What would need doing before this is worth anything

- The 1976 Agreement and the 1964 Public Officers Agreement would have to be retrieved
  before "who is covered" or "what is paid" could be answered.
- The cross-references to Cap. 225 and Cap. 350 are 1985-edition references; whether
  they map to the current Pensions Act and Widows' and Orphans' Pension Act was not
  checked.
- No case law or Parliamentary material was searched.
