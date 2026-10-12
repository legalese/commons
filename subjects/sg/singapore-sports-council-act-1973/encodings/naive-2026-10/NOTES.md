# Singapore Sports Council Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021), informal
consolidation "version in force from 1/4/2026", as deposited at
`../../registers/source-bundle/SSCA1973.txt`. The latest amendment annotated is
Act 4 of 2026, with effect from 1 April 2026. The arrangement of sections at the
top of the deposit is out of step with the body for Part 5; the body was followed.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0215** in the Singapore requirement ledger: Tier 3 of
the remaining Singapore Acts, ordered by everyday-life relevance. It asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act sets up a statutory board and says almost nothing to the public directly.
This row takes what a person can meet: what counts as "sports" (s 2) and the
Council's functions (s 8); membership, the Chairperson and the Deputy (ss 4, 4A);
quorum, who presides and the casting vote (s 6); fees for facilities (s 9(g));
borrowing (s 20); payments to members (ss 5, 21(2)); protection for bona fide acts
(s 23); and the financial year and the audited-statements deadline (Schedule
paras 1 and 4). Not encoded: the 1973 transfers (ss 11-13), the Chief Executive
Officer and staff (ss 14, 15), Ministerial directions (s 10), the rest of the
powers in s 9, s 20A, investment (s 21(3)), regulations (s 24) and the budget
(Schedule paras 2, 3).

## What the Act turns out to say

### 1. Since 1 April 2026, chess, bridge and e-sports are "sports" — and e-sports is not defined

Act 4 of 2026 added "mind sport": "a competitive game based on intellectual skill
rather than physical skill, such as chess or bridge"; and "sports" now "includes
mind sports and e-sports". "E-sports" has no definition. On the words, a
competitive pub quiz league is a mind sport and so within "sports"; a solo sudoku
puzzle is not, because it is not competitive. That the quiz league counts is the
encoding's reading of the definition, not something the Act says. Asserted.

### 2. Section 23 protects members and employees, not the Council

s 23 says nothing done by the Council, a member or an employee in good faith to
carry out the Act will "subject any such member or employee to any action,
liability, claim or demand". The Council itself is not named as protected, so a
claim against the Council as a body corporate (which "may ... sue and be sued",
s 3(2)) is not barred by s 23. The encoding takes that reading. Asserted.

### 3. Every fee for a Council facility needs the Minister twice over

s 9(g): the Council may impose fees for services and for the use of its facilities,
and set the amount of each, only "with the approval of the Minister" — the approval
covers both the fee and its amount. Asserted.

### 4. Quorum is the higher of 5 or half the Council, and the presider breaks ties

s 6(2) (amended by Act 4 of 2026): "5 members or half of the total number of
members ... (whichever is the higher)". With 11 members, half is 5.5; the encoding
requires 6 (rounding up is an inference). With 25 members, 13. A tie is broken by
the presider's casting vote "in addition to his or her original vote" (s 6(5)).
Asserted.

### 5. The Chief Executive Officer may sit on the Council but never chair it

s 4(2) allows one member to be the Chief Executive Officer; s 4A excludes the CEO
from being Chairperson or Deputy Chairperson, and the Chairperson from being Deputy.
The Council has 7 to 25 members, each for at most 3 years; a replacement serves only
the unexpired term (s 4(5)). Asserted.

### 6. Members can be paid, but never profits

s 5 allows salaries, fees and allowances the Minister determines; s 21(2) forbids any
payment "by way of dividend, bonus or otherwise by way of profit to its members".
Loans from the Government need no approval; loans from anyone else and bond issues
need the Minister's written approval; a temporary overdraft is limited to the two
purposes in s 20(2). Asserted.

### 7. Housekeeping

The financial year runs 1 April to 31 March (Schedule para 1); the audited
statements, signed by the Chairperson and the Chief Executive Officer, must reach
the Minister by 31 October (para 4). Asserted.

## What would need doing before this is worth anything

- No regulations under s 24 (use of the National Stadium and other facilities) were
  retrieved; that is where a facility user's rights and duties would actually be.
- The amending Act 4 of 2026 itself was not read; only its annotations.
- No case law on s 23 or on comparable statutory-board immunity clauses was searched.
- The meaning of "e-sports" and the edge of "competitive game" are untested.
