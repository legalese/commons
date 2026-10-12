# Civil List and Gratuity Act 1970 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
6/3/2026"), deposited as `CLGA1970.txt`. The revised edition incorporates amendments
up to 1 December 2021; the latest annotation is the Schedule resolution S 130/2026,
in force 6 March 2026. **The Schedule is column-shifted in the .txt deposit**: the
six figures were matched to the six items by order of appearance, not by line
position (see the module header).

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0161** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The honest answer is: almost nobody. The Act pays the President, and,
after a President's death, may pay his dependants. It is short enough to encode nearly
whole: ss 2-6, 10, 12, 13 and the Schedule. Not encoded: s 1, s 5(3) and s 7 beyond
comments, the repealed ss 8, 9 and 11, and the amount of any gratuity (the Act leaves
it to resolution of Parliament).

## What the Act turns out to say

### 1. Read literally, the acting President's allowance is not paid while the office is vacant

s 2(3) directs the acting President's allowance to whoever exercises the President's
functions "pursuant to Article 22N or 22O of the Constitution". But that allowance is
a Class 1 item, and s 2(5) says no Class 1 payment "shall be made in respect of any
period during which the office of the President is vacant". Classes 2-4 (staff,
household, special services) are not barred. Whether Article 22N or 22O deals with a
vacancy is a question for the Constitution, which was not read; if either does, the two
subsections pull against each other. Asserted on the literal reading.

### 2. The Schedule, matched by order, gives a privy purse of $1,568,900 and a whole civil list of $14,794,400

Privy purse $1,568,900; entertainment allowance $73,000; acting President's allowance
$4,500 (Class 1, together $1,646,400); salaries of personal staff $7,318,000 (Class 2);
expenses of household $4,542,000 (Class 3); special services $1,288,000 (Class 4).
These are yearly sums (s 2(1)), varied by Parliament by resolution (s 7); the
Legislative History lists a resolution almost every year since 1974, the latest
S 130/2026 from 6 March 2026. Because the .txt is column-shifted, the pairing is an
inference from order, and should be checked against the PDF. Asserted.

### 3. A gratuity can be assigned to pay a wife's maintenance, but not attached for it

s 12(a) lets a gratuity be assigned or transferred to satisfy a debt due to the
Government or a court order for "periodical sums" towards the maintenance of the
"wife, or former wife or minor child". s 12(b) lets it be attached, sequestered or
levied upon only for "a debt due to the Government". So a maintenance creditor can
take an assignment but cannot enforce by attachment; a bank or private judgment
creditor can do neither. A husband, an adult child and a lump-sum order are not named.
Asserted.

### 4. The death gratuity is discretionary, unpriced, and goes to the personal representative only if there are no dependants

s 10: where a President or former President dies after 1 July 1970, there "may" be
paid to his dependants, or if there are none to his legal personal representative, a
gratuity "of such amount as Parliament may by resolution determine". s 13 charges it on
the Pension Fund; the civil list itself comes from the Consolidated Fund (s 3). The
pension provisions (ss 8, 9, 11) were repealed by Act 20 of 2012, which renamed the Act
from the Civil List and Pension Act; that s 12 still speaks of "the former President to
whom the gratuity has been granted" while s 10 pays only on death looks like a remnant
of the pension scheme (inference). Asserted.

### 5. Class 1 accrues daily and is paid monthly; a change of holder is split, but the Act gives no formula

s 4: Class 1 sums "accrue from day to day" and are payable on the last day of each
month or another day the Minister determines. s 6 requires "such adjustments and
distribution ... as the circumstances of the case may require" on a change of holder.
The encoding splits by days held, using a 365- or 366-day year as a parameter; both
the divisor and the split are inferences. s 5(2) lets an unneeded part of "any class"
be moved to another class with the Minister's approval; read literally that includes
Class 1. Asserted.

## What would need doing before this is worth anything

- The Schedule pairing should be checked against `CLGA1970.pdf`.
- Articles 22N and 22O of the Constitution should be read to settle finding 1.
- The resolutions fixing any gratuity, and S 130/2026 itself, were not retrieved.
