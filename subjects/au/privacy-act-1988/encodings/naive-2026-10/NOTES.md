# Privacy Act 1988 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of the
finished naive encodings in `subjects/sg` (the `writing-l4-rules` skill was not
available in this session). No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** Compilation No. 104, compilation date 4 June 2026, includes amendments to
Act No. 75, 2025 (register id C2026C00227), as deposited at
`../../registers/source-bundle/C2004A03712.txt` (retrieved 13 October 2026).

**Checks:** one module (`pa-privacy.l4`), one case file (`pa-cases-privacy.l4`), 50
assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0009** in `subjects/au/requirements.jsonl`, priority 1, raised **7
times** by the three Western Australian cradle-to-grave lives (now kept in the
workbench under `scenarios/au/wa/`):

- **chloe c043** (10 June 2024): a credit card at 21; what may a credit reporting body hold?
- **chloe c044** (1 July 2024): marketing calls and texts; can she stop them? (APP 7)
- **jake k048** (2 March 2031): two credit cards at 24 (Part IIIA)
- **jake k064** (6 February 2037): debts of $41,000 and collectors; defaults listed
- **jake k075** (31 May 2042): the debt agreement completes; what stays on the credit file, and for how long?
- **daniel d044** (1 June 2031): Jarrah's first three employees; "no Privacy Act yet" under $3 million turnover (s 6D)
- **daniel d052** (3 April 2036): above $3 million; 1,200 users' email addresses breached; eligible? who must be told? by when? (Part IIIC)

The encoding takes those questions and the definitions, conditions and exceptions
needed to answer them: ss 6C, 6D, 6DA, 6EA; APP 7; ss 6N, 6Q, 20C, 20V, 20W, 20X
(items 4 and 5), 21D; ss 26WE, 26WF, 26WG, 26WH, 26WK, 26WL. The other APPs, s 6E,
the s 7B exemptions, use and disclosure by credit reporting bodies, access and
correction, credit providers' own use of credit information, bankruptcies and
personal insolvency agreements, and the Part IIIC exceptions and Commissioner's
directions are not encoded.

What a lender must assess before issuing a card (c043, k048) is the National Consumer
Credit Protection Act 2009, not this Act. The National Personal Insolvency Index
(k075) is the Bankruptcy Act 1966.

The scenarios give no turnover figures, default dates, notice dates or the day the
debt agreement was made. The case file uses figures and dates chosen by the encoder,
each on the side of the line the scenario states, and labels them as assumptions.

## What the Act turns out to say

### 1. A completed debt agreement stays on the file until it ends, not for "five years"

k075 expects "five years". Under s 20X(1), item 5, a debt agreement that ends under
s 185N of the Bankruptcy Act is kept for "whichever of the following periods ends
later": "the period of 5 years that starts on the day on which the agreement is
made" and "the period that ends on the day on which the agreement ends". The five
years run from the **making**, not from completion. Jake's agreement was proposed on
20 April 2037 and completed on 31 May 2042, so it ran just over five years. If it was
made on 20 April 2037 (the encoder's assumption), the retention period ends on the
day it completes and the information may go from 1 June 2042. If it was made on 1 July
2037, the five years govern until 1 July 2042. Either way the body then has one month
to destroy or de-identify the information (s 20V(2)). A terminated agreement
(item 4) is kept for the later of five years from the making and two years from the
termination. Asserted.

### 2. No section sets a number of days to notify a breach; the 30 days is for an assessment

d052 asks "by when?". Section 26WH requires a "reasonable and expeditious assessment",
and only "all reasonable steps to ensure that the assessment is completed within 30
days". That applies only where the entity has reasonable grounds to *suspect* a breach
but not to *believe* one. Once it believes, s 26WK requires a statement to the
Commissioner "as soon as practicable", and s 26WL requires notification of the
individuals "as soon as practicable after the completion of the preparation of the
statement". The individuals notified may be everyone whose information it was, only
those at risk, or, if neither is practicable, everyone through publication on the
website (s 26WL(2)). With 1,200 known email addresses, notifying each user is
practicable. Asserted (the assessment trigger, the statement and the route).

### 3. Above $3 million once means never again exempt

Section 6D(4)(a): an entity is not a small business operator if it "carries on a business
that has had an annual turnover of more than $3,000,000 for a financial year that has
ended" since it started. The test is any year, not the last year. Jarrah, once
above $3 million (d052), stays inside the Act even if turnover falls back to $2.5
million and its business is again a "small business" under s 6D(1). The limit is
inclusive: turnover of exactly $3,000,000 is still small. Asserted.

### 4. Jarrah's first year is judged on the current year, and the formula for that is missing

In June 2031 Jarrah had not traded in the previous financial year, so s 6D(2) asks
whether its turnover "for the current year" is $3,000,000 or less. For a business carried on
for only part of a year, s 6DA(2) gives "the amount worked out using the formula:". The
formula is **not in the deposit**: the text goes straight on to s 6E. Part-year turnover
is therefore an input. With turnover under the limit Jarrah is a small business
operator and not an organisation (s 6C(1)), so the APPs do not bind it (d044 is right).
That changes if it trades in personal information for a benefit without consent
(s 6D(4)(c), (7)), or if it registers a choice to be treated as an organisation (s 6EA).
Asserted. (The employee records exemption in s 7B(3) would matter to an employer that is bound by
the Act. It is not encoded.)

### 5. APP 7 gives way on calls and texts

APP 7.8: "This principle does not apply to the extent that" the Do Not Call Register
Act 2006 or the Spam Act 2003 apply. Whether they apply to a given call or message
is a question for those Acts, so it is an input here. The encoder's inference is that
they cover Chloe's telemarketing calls and texts (c044), and that her remedy there lies
in those Acts. Where APP 7 does govern, for example a catalogue by post, an organisation that
collected the information from her may market to her only while she has not asked it
to stop (7.2(d)). It must give effect to her request "within a reasonable period" and
"must not charge" (7.7). A small business operator is not an organisation, so APP 7
does not reach its mailings at all. Asserted.

### 6. What a credit file may hold, and the steps before a default is listed

Credit information is the closed list in s 6N, "other than sensitive information".
A credit reporting body may not collect identification information on its own
(s 20C(3)(c)). An overdue payment is default information only if it is at least 60
days overdue, a written notice requesting payment has been given, recovery is not
statute-barred, and the amount is at least $150 or any higher amount prescribed by
regulation (s 6Q(1)). The prescribed amount is an input. The credit provider may
list it only after a written notice of intention to disclose and "at least 14 days"
(s 21D(3)(d)), and never for anything before the individual turned 18
(s 21D(3)(a)). Default information is kept for five years from the day the body
collects it (s 20W item 4), so Jake's k064 default stays on his file into 2042.
Payment information about a paid default is kept for five years from the collection
of the default (item 5). Payment does not shorten that period on the text. Asserted,
except the payment point.

### 7. Whether 1,200 email addresses is "serious harm" is not answered by the Act

Section 26WE(2) turns on whether "a reasonable person would conclude" that serious harm is
likely. Section 26WG lists matters to weigh, among them the kind and sensitivity of the
information, security measures, who has the information and "any other relevant
matters". It does not say whether email addresses alone qualify. That is an input, and
both answers are asserted. Remedial action in time takes the event out entirely
(s 26WF). Asserted.

## What would need doing before this is worth anything

- The s 6DA(2) part-year formula has to be recovered from the authorised compilation:
  it was lost when the deposit was converted to text.
- The Privacy Regulations (any higher default amount under s 6Q(1)(d)(ii), prescribed
  small business operators under s 6E) and the registered CR code were not retrieved.
- The rest of Part IIIA (use and disclosure by credit reporting bodies, ban periods,
  access and correction, credit providers' use of credit eligibility information),
  the Part IIIC exceptions and directions, and the other twelve APPs are not encoded.
- The day Jake's debt agreement was made, Jarrah's turnover, and the dates of Jake's
  defaults are not in the scenarios. The case file uses assumptions.
- No OAIC guidance, determination or case law was read.
