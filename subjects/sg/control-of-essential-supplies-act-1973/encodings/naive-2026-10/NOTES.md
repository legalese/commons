# Control of Essential Supplies Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions as the finished example rows show them, and nothing else. No pipeline,
no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CESA1973.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021. The last amendment its Legislative History annotates is Act 15 of
2010 (Criminal Procedure Code 2010), in force 2 January 2011.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0096** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act is short (30 sections). This row takes what a trader or a shopper meets:
- what makes an article controlled (ss 2, 5)
- licences and the appeal to the Minister (s 7)
- the trading offences (ss 14 to 19)
- storage away from licensed premises, and unclaimed seized goods (s 20)
- unlawful possession (s 21)
- the owner's payment when the Controller takes the goods (s 11(2)(b))
- penalties, and the liability of directors and employers (s 22)
- composition (s 29)

Not encoded: appointment of officers (ss 3, 4), the regulation-making power (s 6),
the Controller's information, entry, arrest and seizure powers (ss 8 to 10) beyond
noting that obstruction is an offence, sale of perishable seized goods (s 12),
delegation (ss 13, 24), the court's confiscation power (s 26), and protection of
informers (s 30). No order under s 5 and no regulation was retrieved.

## What the Act turns out to say

### 1. The Act does nothing until the President declares an article

Every offence turns on a "controlled article", which s 2 defines as an article or
food declared by an order under s 5. A rationed article counts as controlled. No
order was retrieved, so this row cannot say whether rice, fuel or anything else is
controlled today. Asserted (only as the definition).

### 2. A repeat offender's fine doubles, but the prison term does not, and a company's fine never rises

s 22(1): an individual faces up to $10,000 or 2 years or both; on a second or later
conviction, up to $20,000 or 2 years. s 22(2): a body corporate faces a flat $20,000,
whether it is a first or a later conviction, and no prison term. Directors and
officers fall under s 22(1) as individuals. Asserted.

### 3. The buyer of a rationed article commits the offence too

s 18(1): without authority, licence, permit or coupon, "a person must not obtain or
attempt to obtain" a rationed article, as well as a retailer not supplying it.
Asserted.

### 4. The Controller need give no reason, and the Minister's decision is final

s 7(5): the Controller may vary, suspend, revoke or refuse to renew a licence or
permit "without assigning any reason". s 7(6) allows an appeal to the Minister,
"whose decision is final". On the words, a refusal to *issue a permit* is in neither
limb of s 7(6). That gap is my reading of the text, not something it states.
Asserted.

### 5. A seller may demand only immediate payment, a time for payment or delivery, or a deposit

s 19: any other condition of sale is an offence unless the Controller permits it.
Tying (buy another product too) and a minimum purchase are therefore offences.
Asserted.

### 6. The burden of proof shifts to the defendant

- s 20(3): it is enough to prove the defendant's article was found away from licensed
  or approved premises.
- s 21: possession raising a reasonable suspicion is an offence unless the defendant
  satisfies the court otherwise.
- s 22(4)(b): directors are deemed guilty when the company is convicted, unless they
  prove they did not know or took reasonable precautions.
- s 22(5): a person answers for a partner, agent or employee, with the same defence.
- s 25 adds a general reversal for licence-based defences.

Asserted, except s 25.

### 7. Smaller figures

- s 11(2)(b): where a maximum price is fixed by law, the Controller may pay the owner
  that price less certified expenses capped at 25%.
- s 20(4): goods removed in a search may be sold if "not claimed within 2 weeks". I
  read that as a sale from day 15; that day count is an inference.
- s 29: composition up to $2,000, but only for offences prescribed as compoundable.

Asserted.

### 8. An employee who sells is not named in s 16(1)

s 16(1) reaches an unlicensed person selling on their own behalf, as a director or
officer of a company, or as a partner of a firm. An employee who is none of these is
not named. The employer may still be liable under s 22(5), and s 21 or another
provision may catch the employee. The encoding follows the words of s 16 alone, and
says so. Asserted.

## What would need doing before this is worth anything

- Retrieve any orders in force under s 5 and the regulations under ss 6 and 29.
  Without them, nothing here applies to any actual article.
- The CPC 2010 cross-references in ss 10 and 22 were not followed.
- No case law was searched, including on "reasonable cause" in s 15 and "reasonable
  suspicion" in s 21.
- The reading of s 7(6) for permits, and of s 16(1) for employees, needs a lawyer's
  view.
