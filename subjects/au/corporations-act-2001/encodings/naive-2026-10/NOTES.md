# Corporations Act 2001 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of the
finished naive encodings in `subjects/sg` (the `writing-l4-rules` skill was not
available in this session; `encoding.json` carries the shared method line). No
pipeline, no coverage table, no independent test pass, no human gate. NOT for public use.

**Edition:** Compilation No. 149, compilation date 19 September 2026, includes
amendments to Act No. 87, 2026 (register id C2026C00432), as deposited at
`../../registers/source-bundle/C2004A00818.txt` (retrieved 13 October 2026). The
compilation is in seven volumes; the deposit joins them.

**Checks:** one module (`ca-jarrah.l4`), one case file (`ca-cases-jarrah.l4`), 57
assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0011** in `subjects/au/requirements.jsonl`, priority 1, raised **7
times** by the Western Australian cradle-to-grave lives (kept in the workbench under
`scenarios/au/wa/`). All seven are Daniel's, and all are about his company, Jarrah
Legal Technologies Pty Ltd, or his later directorship and investing:

- **daniel d043** (15 March 2031): Jarrah registered, 70% Daniel, 10% Priya, 20% a sophisticated investor for $500,000. What does registration need; who is a director and what does he owe; is the placement exempt from disclosure? (ss 117, 180-184, 708, 1272C)
- **daniel d050** (1 September 2035): Series A, $5,000,000 for 25% from a fund that is a sophisticated investor. Is the issue exempt? (s 708(8), (11), s 254A)
- **daniel d064** (31 March 2042): a selective buy-back of the investor's shares; the shareholder approval; the solvency test (Part 2J.1, ss 257A, 257D, 254T)
- **daniel d065** (15 June 2043): Jarrah acquires Formly (ss 46, 50)
- **daniel d071** (30 June 2050): Jarrah sold to a listed buyer for $40,000,000. A takeover? (s 606)
- **daniel d073** (1 September 2051): a non-executive director of a listed company. What may a director who knows something not do with the shares? (ss 1043A, 674, 191)
- **daniel d081** (20 March 2056): angel investments in five start-ups as a sophisticated investor. What is he not protected from? (s 708(8))

The encoding takes those questions and the definitions, conditions and exceptions
needed to answer them: ss 9AC, 201B, 1272B, 1272C; ss 113(1), 114, 117, 201A; ss 180,
181, 183, 184; s 191; s 708(1), (5), (8), (9), (11) with s 113(3); s 254A(2); s 254T;
ss 257A to 257E with s 250MA; ss 46, 50; s 606(1); ss 674(2), 674A(3), (4), 676; ss
1042A, 1042C, 1042D, 1043A, 1043D. This is a seven-volume Act; everything else is left
out, notably the rest of s 708, what a prospectus must contain and liability for a
defective one, the s 611 exceptions (an input), relevant interest and voting power
(taken as given percentages), ss 257F to 257H beyond the s 257B table, insolvent
trading, the listing rules, and penalties.

The scenario does not say who Jarrah's directors are, how votes split after the Series
A, how many members Jarrah has in 2050, the fund's or Daniel's gross assets, or any
certificate date. The case file uses figures chosen by the encoder and labels them as
assumptions. The net assets and gross income amounts in s 708(8)(c) are set by
regulations the deposit does not contain; the case file passes hypothetical figures
as inputs.

## What the Act turns out to say

### 1. The $500,000 placement is the sophisticated-investor exemption, not the small-scale one

The scenario (d043, Chapter 4) puts the investor's 20% "under the small-scale
exemption". At exactly $500,000 the offer falls in s 708(8)(a): "the minimum amount
payable for the securities on acceptance ... is at least $500,000". Because it needs no
disclosure "because of any other subsection", s 708(5)(a) leaves it OUT of the
small-scale count of 20 investors and $2 million. A cheque of $499,999 without an
accountant's certificate would still need no disclosure, but under the small-scale
exemption, and only if the offer was personal (s 708(2)) and within the ceilings.
Money the company or an associate lent for the subscription is disregarded (s 708(9)),
so $500,000 of which $450,000 was lent by Daniel is not a sophisticated-investor offer.
Asserted.

### 2. The buy-back's "solvency test" is not s 254T

d064 cites s 254T for the solvency test. s 254T is about **dividends**: assets must exceed
liabilities by enough to pay the dividend, the payment must be fair and reasonable, and
it must not materially prejudice paying creditors. A buy-back has its own condition in
s 257A(a): it must "not materially prejudice the company's ability to pay its
creditors". There is no net-assets test for a buy-back. Both are asserted, separately.

### 3. A selective buy-back needs 75% with the seller's "yes" votes excluded, or every ordinary shareholder

s 257B's table puts a selective buy-back outside the 10/12 limit columns: it always
needs a s 257D resolution, lodgment of offer documents (s 257E) and 14 days' notice.
s 257D(1)(a) requires a special resolution, which s 250MA(b) sets at 75% of the votes
cast, "with no votes being cast in favour" by the seller or associates. The seller may
still vote **against**, and those votes count among the votes cast. On the encoder's
split (Daniel 525, Priya 75, investor 150, fund 250 of 1,000), the resolution passes
with the investor against (850 of 1,000), but fails if the fund votes against and the
investor stays out (600 of 850, about 70.6%). If the investor votes for it, limb (a) is
lost and only the unanimous route in (b) remains. Asserted (the s 257E and s 257F rules are encoded but not asserted).

### 4. Dealing on inside information is "a person's" offence, and trading windows are not in the Act

d073 asks what a director who knows something may not do. s 1043A(1) is addressed to
any person who possesses inside information and knows or ought reasonably to know it is
not generally available and is material. It forbids dealing or procuring, and s
1043A(2) forbids tipping. The Act says nothing about trading windows: a company's
window cannot make dealing on inside information lawful. Continuous disclosure (s
674(2)) is the **entity's** duty. A director is caught only through s 674A(3), as a
person "involved" in the entity's contravention, and s 674A(4) gives a defence for
someone who took all reasonable steps and then believed on reasonable grounds that the
entity was complying. Asserted.

### 5. A proprietary company that needs a prospectus is breaking s 113(3)

s 113(3) forbids a proprietary company "any activity that would require disclosure to
investors under Chapter 6D", except offers to existing shareholders or employees (and
CSF offers). Jarrah's Series A (d050) is safe only because the fund's $5,000,000 meets s
708(8)(a), and, on the encoder's assumed $100 million of gross assets, s 708(11)(b) as
well. A $300,000 offer to a stranger that is neither personal nor sophisticated would
breach s 113(3), though s 113(4) keeps the transaction valid. Asserted.

### 6. At $10 million of gross assets Daniel stops needing a certificate

For d081, s 708(8)(c) depends on a qualified accountant's certificate "no more than 6
months before the offer"; a seven-month-old certificate does not do (exactly six months
does), and the thresholds are in regulations. But s 708(11)(b) exempts any offer to "a
person who has or controls gross assets of at least $10 million". After the 2050 sale
Daniel very likely has that (an inference; the scenario gives no figure), so no offer to
him needs disclosure, whatever his certificate says. What he is "not protected from" is
investing without a prospectus. Asserted.

### 7. A de facto director is a director but not an "eligible officer"

s 9AC(1)(b) makes a person a director if they act as one or the board is accustomed to
follow their wishes (professional advice aside). The director identification number
duty in s 1272C attaches to an "eligible officer", which s 1272B(1)(a) limits to a
director who "is appointed". An investor who runs the board from outside owes the
directors' duties but need not hold a director ID. An appointed director without an ID
contravenes s 1272C unless a timely application is pending or they were appointed
without knowing. Asserted.

### 8. A sole director need not disclose interests to anyone

s 191(5): "This section does not apply to a proprietary company that has only 1
director." On the assumption that Daniel was Jarrah's sole director, s 191 never bit at
Jarrah. On a listed board (d073) it does, unless the interest is one of the s 191(2)(a)
kinds or a standing notice under s 192 covers it. Asserted.

### 9. Selling Jarrah is no takeover, and Formly becomes a related body corporate

s 606(1) applies only to a listed company or "an unlisted company with more than 50
members". Jarrah, unlisted and assumed to have far fewer members, can be bought outright
(d071). Note 3 to s 606(1) still catches an acquisition whose effect reaches a listed
company or one with more than 50 members (not encoded). Once Jarrah holds more than half
of Formly's votes or share capital, Formly is its subsidiary (s 46) and the two are
related bodies corporate (s 50). Exactly 50% is not "more than one-half". Asserted, except s 50, which is encoded but not asserted.

### 10. Registration is a lodgment, and ASIC "may" register

s 117 lists what the application must state. The applicant must hold the members' and
directors' written consents when the application is lodged (s 117(5)). s 118(1) then
says ASIC "may" give an ACN, register and issue a certificate. A proprietary company
needs at least one member (s 114), no more than 50 non-employee shareholders (s 113(1)),
and at least one director who ordinarily resides in Australia (s 201A(1)). A director
must be an individual of at least 18 (s 201B(1)). Asserted, except that ASIC's
discretion is not modelled.

## What would need doing before this is worth anything

- Read the Corporations Regulations for the s 708(8)(c) figures and the
  s 1272C(2)(a)(ii) application period, and replace the hypothetical inputs.
- Encode voting power and relevant interest (ss 608 to 610) and the s 611 table
  instead of taking them as inputs, and Note 3 to s 606(1).
- The rest of s 708 (notably (10) and (12)), s 708AA, s 727 and Part 6D.3, which
  together say when an offer that is not exempt is an offence.
- ss 257F to 257H, s 254Y, and the minimum holding, employee share and on-market
  buy-back definitions in s 9.
- The ASX Listing Rules are not law in this repository. Without them the s 674(2)
  trigger is an input.
- Search ASIC regulatory guides and case law on de facto directors, the business
  judgment rule and inside information.
- An independent test pass. Every expected value here was written by the encoder.
