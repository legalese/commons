# Science Centre Act 1970 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/ScCA1970.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amending Act annotated in the text is Act 5 of 2018
(the Public Sector (Governance) Act 2018), at ss 2, 7, 8, 9, 10, 16, 17, 18 and 20.

**Checks:** one module (`sca-board.l4`), one case file (`sca-cases-board.l4`),
52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0203** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is short (twenty sections, three of them repealed) and institutional. It
creates the Science Centre Board and makes it run the Science Centre. The answer to
the requirement is that it decides almost nothing for a visitor or business
directly: what reaches them is the Board's power to control access and charge fees
(s 6(i)), the ceiling on penalties in regulations (s 20(2)), the Minister's approval
of property deals (s 6(d)), how a sealed deed is proved (s 12) and the protection of
Board members (s 11). This row takes those, plus the financial year (s 2), the
Board's numbers and temporary appointments (s 4), the acting chief executive
(s 7(2)), delegation (s 10), the Fund (ss 14, 15), estimates (s 18) and investment
(s 19). Not encoded: the short title (s 1), incorporation (s 3), the duty in s 5
beyond its use in s 6, the general powers in s 6(a)-(c), (f), (g), the chief
executive's appointment and staff (s 7(1), (3)), Ministerial directions and
information (s 9), grants (s 13), the share issue to the Minister for Finance
(s 13A) beyond a comment, and the Minister's power to make regulations (s 20(1)).
No regulations made under s 20 were retrieved.

## What the Act turns out to say

### 1. The Board sets the admission fee; the Act sets no ceiling and asks no one

s 6(i) gives the Board power "to regulate and control public access to the Science
Centre and charge fees for such access". There is no cap, no exemption, and no
approval step in the Act, whereas acquiring or disposing of property under s 6(d)
needs "the approval of the Minister". Charging or raising a fee is encoded as not
needing the Minister. The estimates under s 18, which the Minister may approve or
disallow item by item, are the only route in the Act by which the Minister touches
revenue. Asserted.

### 2. A breach of the Centre's rules can only ever be a fine of $1,000

s 20(2) lets regulations make a contravention an offence and provide "a penalty not
exceeding a fine of $1,000". Imprisonment is not mentioned, so a regulation that
provided for it, or for a larger fine, would go beyond s 20(2). Asserted.

### 3. Members are shielded from suit; the Act says nothing of employees

s 11(1) bars any "action, suit, prosecution or proceedings" against "any member of
the Board" for acts done bona fide in executing the Act. Employees are not named.
Where a member is exempt "by reason only of this section", s 11(2) makes the Board
liable only as it would be if the member were its employee or agent. Whether staff
are protected by some other Act (the Public Sector (Governance) Act 2018, for
instance) was not read. Asserted for s 11 only.

### 4. The Board may delegate to any employee, but not to a single member

s 10(2) allows delegation to a committee, "the chairperson of that committee or any
employee of the Board". A Board member acting alone, unless chairing a committee,
is not on the list; an outside contractor is not either. Committees may include
non-members (s 10(1)). Asserted.

### 5. The Board need not be full to act, and temporary officers come from different pools

s 4(1)(c) wants 7 to 15 members besides the Chairperson and Deputy, but s 4(7) says
"The Board may act despite any vacancy". A temporary member may be "any person"
(s 4(3)); a temporary Chairperson or Deputy must be "any member of the Board"
(s 4(4)). Both need a temporary incapacity or absence from Singapore. s 2 makes the
temporary officers count as Chairperson and Deputy, so a deed sealed before a
temporary Deputy and one other member, both signing, carries the s 12 presumption;
one sealed before the chief executive does not. Asserted.

### 6. The commencement note names a section 23 the Act no longer has

The long-title note reads "25 September 1970: Except section 23; 1 April 1972:
Section 23", repeated in the Legislative History. The 2020 Revised Edition ends at
s 20; no s 23 appears and the Comparative Table maps only one deleted provision
(2013 Ed. s 10(3)). What s 23 was, and when it went, cannot be told from the
deposit. Not encoded.

### 7. Smaller points

The financial year begins on 1 April (s 2). All moneys received "must forthwith" be
paid into the Science Centre Fund (s 14), which may be spent "solely" on the Board's
administration and on carrying out the Act's purposes (s 15); paying staff salaries
and buying an exhibit are read as within those, a gift to an unrelated charity as
outside them (inference from the wording). The Board chooses the bank (s 14) and
invests under the standard investment power of statutory bodies (s 19), without the
Minister's approval. s 6(d) is read as one approval governing both acquisition and
disposal, since both sit in the one paragraph after the approval words. Asserted.

## What would need doing before this is worth anything

- Any regulations made under s 20 (the rules a visitor actually meets) were not
  retrieved or read.
- The Public Sector (Governance) Act 2018 provisions the Act defers to (ss 7, 9, 20)
  and s 33A of the Interpretation Act 1965 were not read.
- The history of the missing s 23 was not traced to the earlier editions.
- No case law was searched.
