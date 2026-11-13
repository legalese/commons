# NEEDS-CORE (coa14): what the core lacks that this part needed

Written 2026-11-13 by part agent coa14. Nothing here is a request to change a type the core already has.

## 1. A statement of capital (proposed for the core; declared under this part's prefix in `coa14-nouns.l4`)

Six sections of my range require a statement of capital with the same content: ss 619(3), 621(3), 625(3), 627(3), 644(2) and 649(2) (23 lines of the range mention one). The content in each is: (a) the total number of shares of the company, (b) the aggregate nominal value of those shares, (ba) the aggregate amount (if any) unpaid on those shares, and (c) for each class of shares (i) prescribed particulars of the rights attached, (ii) the total number of shares of the class and (iii) the aggregate nominal value of shares of the class. Paragraph (d) is shown as a row of dots in all six.
s 652(1)(a) cites statements of capital delivered under ss 644, 649, 1028A and 1032A and under paragraph 7 of Schedule 4 to the 2015 Act, so the shape recurs outside my range.
The core has no such type, so I declared two under my prefix: `s 619(3) statement of capital` (fields `s 619(3)(a) states the total number of shares of the company`, `s 619(3)(b) states the aggregate nominal value of those shares`, `s 619(3)(ba) states the aggregate amount (if any) unpaid on those shares`, `s 619(3)(c) the entries for each class of shares`, `s 619(3) is stated with respect to the share capital at the moment the section names`; all BOOLEAN except the list) and `s 619(3)(c) class entry in a statement of capital` (three BOOLEAN fields for (c)(i) to (iii)).
What to hoist: one core type `Statement of capital` with those fields, so that the six sections here and any other part that requires one share it; then `coa14-nouns.l4` loses the two declarations and `s 619(3) the statement of capital states what the section requires` and its five wrappers change their type name only.
The fields are yes/no facts ("states the total number of shares") and not numbers, because the seam is what the statement says, not the capital's arithmetic; a part that wants to check the numbers needs a richer type than the one proposed.

## 2. Not needed

- A "greater of" fine: no penalty in lines 8206-8744 is the greater of two amounts (`grep -i 'greater of'` over the range: 0 lines). PLAN.md's note that the core has no constructor for it does not touch this range.
- A constructor for a fine without a stated limit, a level on the standard scale, the statutory maximum or imprisonment: the core's `Fine limit`, `Penalty`, `Period` and `Mode of conviction` carry every penalty in the range (ss 619(5), 621(5), 625(5), 627(8), 635(3), 636(3) to 640(3), 643(5), 644(9), 647(2), 656(5)).
