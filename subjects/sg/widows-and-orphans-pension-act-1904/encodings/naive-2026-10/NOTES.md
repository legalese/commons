# Widows' and Orphans' Pension Act 1904 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/WOPA1904.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment annotated in the body is [8/1995] (the
Pension Fund Act 1995), and the Legislative History ends there.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0226** in `subjects/sg/requirements.jsonl`: Tier 3
of the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person it applies to; no scenario has asked a sharper
question yet.

The row covers who is a pensionable child, the 4% abatement and when it stops, what
happens when a contributor leaves the service, the family notices and the $25 fine,
which widows take nothing, when a widow's pension ends, how the pension is split
between lines of children, adopted children, and the arithmetic of the First
Schedule's own worked examples: ss 2, 4, 5, 12-14, 22, 23, 25, 27, 29-34, 38, 39.
Not encoded: the one-off options of ss 7 and 8, reduced-income and ill-health
contributions (ss 9-11), transfers abroad and to Malaysia (ss 15-20), the Crown Agents
and sterling rules, proof of life, minors' payees, the bar on assignment, the
President's final say (s 43), the pre-1955 saving (s 44), Rules II to V and F, and
Tables A, B and C. The table factors are passed in as numbers taken from the
Schedule's own examples.

## What the Act turns out to say

### 1. The scheme is closed: nobody appointed since 2 March 1961 is in it

The definition of "public servant" in s 2 excludes an officer who, on or after
2 March 1961, is appointed to a pensionable office. It also excludes one "not
restricted by law to one wife at a time". So the Act now decides things only for the
widows and children of officers who joined before 1961. This is read from the
definition. No assertion was written for it.

### 2. Two of the Schedule's own worked examples do not come out to the printed figure

Rule IX's example gives the single contribution as 400 × 4.06 ÷ .449 = $3,620. The
arithmetic gives $3,616.93. Rule X's example multiplies $2,376 by 2.226 and prints
$5,288. The product is $5,288.976, so the printed figure has been truncated, not
rounded. The encoding follows the rule as worded, and the cases assert both the
computed figures and that the printed ones are not reached. The Rule I examples (8%
accumulation to $112.58, × .554 = $62.37; $30 × 5.77 = $173.10) do agree. Asserted.

### 3. The Rule I(c) example breaks off without its final figure

The example ends "Pension at 31 March 1923" with no amount, in this deposit at least.
From the printed steps the figure is $330.27 − $38.30 − $119.60 = $172.37. It is
asserted as a hand computation. The missing figure may be lost to PDF extraction
(inference). Asserted.

### 4. A daughter's pension ends when she marries, but a son's does not

"Of a pensionable age" (s 2) means under 21 for a son, and under 21 *and never
married* for a daughter. s 29 stops a daughter's pension "on her attaining the age of
21 years or marrying under that age". A married son of 18 still counts. Asserted.

### 5. A marriage that lasted under a year, with no child, leaves the widow nothing unless the President relents

s 25(1)(c) bars a widow whose husband dies within 12 calendar months of the marriage
without issue. s 25(1)(a) bars one who married him after he had stopped contributing,
turned 65, retired or been removed. Only the first bar can be lifted by the President
(s 25(2)). Asserted.

### 6. Remarriage or bankruptcy ends a widow's pension, and her children take it

s 27(1): the pension ceases on her death, remarriage or bankruptcy, and she is then
"deemed to have died", so under s 35 the children take it. For bankruptcy the President
may still direct payment to her of any part not payable to children. Living abroad
does not end it. s 40 only lets payment be held back until proof of life is produced.
Asserted.

### 7. The pension is split by lines of children

A widow with no pensionable stepchildren takes all of it (s 30). With children of one
earlier marriage, each side takes one-half (s 33). With two or more earlier marriages,
"one-third or one-quarter, as the case may be" (s 34). Without a widow, each
marriage's children take a matching share of their mother's notional pension (ss 31,
32). Within a line the children share equally (s 38). The Rule VI(a) example ($150
among 3, then 2, then 1) is asserted. Reading "as the case may be" as one share per
line is an **inference**, and the text names no fraction smaller than a quarter.
Asserted.

### 8. Leaving the service: the bachelor gets his money back, the family man keeps the pension

A bachelor who retires, dies in service or is removed gets his contributions back
with 2½% compound interest (ss 13(2)(a), 14(a)). A widower without pensionable
children gets back only what he paid since his last wife died or his last child
ceased to qualify. On removal, but not on retirement, the refund is reduced by "any
sums due by him to the Government" (s 14). A married man who retires early may go on
contributing (s 12). If he is removed, his widow takes a pension on the rights acquired
so far (s 14(c)). Asserted.

### 9. Small duties, small fine

The family notices (s 22) are due within 6 months of entering the service and within
3 months of a marriage, decree, birth, daughter's marriage or death. After the
contributor dies the widow must give the notices herself. Each default carries a fine
of up to $25, deducted from salary or pension (s 23(1)). A wilful false statement can
forfeit all or any part of his rights (s 23(2)). Asserted, apart from s 23(2).

## What would need doing before this is worth anything

- Tables A, B and C are not encoded. Every pension figure depends on them, and they are
  column-laid tables in the PDF that would need careful transcription.
- Rules II to V (second wives, contributors who began while married or widowed) and F
  (transfers) are not encoded, and neither are ss 7 to 11 or 15 to 20.
- Whether anyone still draws under the Act, and at what amounts, was not checked.
- No case law or Presidential decisions under s 43 were searched.
