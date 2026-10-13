# Competition and Consumer Act 2010 (Cth) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else (the skill was not loaded in this session; the finished
naive encodings in `subjects/sg` were followed). No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** Compilation No. 166, compilation date 27 August 2026 (includes amendments
up to Act No. 76, 2026), register id C2026C00389, as deposited at
`../../registers/source-bundle/C2004A00109.txt`. The deposit's metadata warns that a
version in force from 16 September 2026 had no registered compilation when it was
fetched, so amendments from that date may be missing.

**Checks:** one module (`cca-acl-mergers.l4`), one case file
(`cca-cases-acl-mergers.l4`), 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0018** in `subjects/au/requirements.jsonl` (priority 1), raised
**5 times** by the three Western Australian cradle-to-grave scenarios:

- Chloe **c070** (2032-05-20): a new laptop fails in month three and the retailer
  repairs it. What guarantees apply, and who chooses the remedy?
- Jake **k064** (2037-02-06): debts of $41,000, and collectors call. What may a
  collector do?
- Daniel **d045** (2031-07-10): Jarrah's standard software terms. Is a liability cap
  an unfair term in a small-business contract? Are the consumer guarantees excluded?
- Daniel **d056** (2039-02-11): a competitor trades as JARRA. Is it misleading conduct?
- Daniel **d065** (2043-06-15): Jarrah acquires Formly Pty Ltd. Must the acquisition
  be notified to the ACCC?

The Act fills four volumes. This encoding takes only what those events ask about,
plus the definitions and exceptions needed to answer them. That means: who is a
consumer (Sch 2 s 3); the guarantee of acceptable quality (s 54); remedies against a
supplier of goods and who chooses them (ss 259–263); the bar on contracting out and
the business-to-business limitation (ss 64, 64A); unfair terms (ss 23, 24, 26, 27);
s 18; s 50; the Schedule's reach as Commonwealth law (ss 131, 131A); and when an
acquisition must be notified under Part IVA (ss 51ABB, 51ABD, 51ABE(2), 51ABJ,
51ABO, 51ABP, 51ABS, 51ABT, 51ABV(6)).

Not encoded: Part IV, the rest of Part IVA, the other guarantees, services remedies,
manufacturers' liability, penalties, the s 25 examples, and the ACL as a law of
Western Australia (that comes through the Fair Trading Act 2010 (WA), which is not
deposited).

## What the Act turns out to say

### 1. The Act does not say whether Formly is notifiable. The Minister's instrument does

s 51ABO makes an acquisition notifiable if it is put into effect "on or after 1
January 2026" and it "occurs in circumstances determined under subsection 51ABP(1)"
or falls in a class determined under s 51ABQ(1). Both are made by the Minister "by
legislative instrument". s 51ABP(2) says the circumstances must turn on "a specified
threshold" (value, turnover, concentration or assets), but no figure appears in the
Act. So the scenario's answer for d065, "not notifiable at this size", cannot be
checked against this text. Whether a threshold is met is an INPUT here. Formly's size
is not given either. The control exception (s 51ABS(1)) does not save the deal:
Jarrah takes control of Formly. Neither does the Chapter 6 entity exception (s 51ABT),
which covers only listed companies, unlisted companies with more than 50 members, and
listed schemes. If notice is required and not given, the acquisition "is stayed"
(s 51ABE(2)). Asserted, with the threshold as an input.

### 2. Every contract Jarrah makes for a supply is a small business contract, whoever the customer is

s 23(4)(b) needs only "at least one party" that employs "fewer than 100 persons" or
has turnover under $10,000,000. Jarrah had three employees in July 2031, so its
standard terms are small business contracts even with a bank as the customer. There
is no limit on the contract's value in this compilation. A term in a standard form
contract is void if it is unfair (s 23(1)). Proposing an unfair term is itself a
contravention, and each such term counts separately (s 23(2A), (2B)). Of the three
limbs of "unfair" (s 24(1)), the second, that the term is not reasonably necessary, is
presumed. Jarrah must prove the cap is necessary (s 24(4)). A contract alleged to be
standard form is presumed to be one (s 27(1)). Asserted.

### 3. For a business customer paying $40,000 or less, the guarantees apply and the cap cannot exclude them

A person acquires goods or services "as a consumer" if the price is $40,000 or less,
whatever their kind (s 3(1)(a), (3)(a)). The $40,000 can be raised by regulation (an
input). "Goods" includes "computer software" (s 2). A term that excludes, restricts
or modifies the guarantees is void to that extent (s 64(1)). The only exception is
s 64A, for non-household supplies: liability may be limited to supplying the services
again, or the cost of that (for goods: repair, replacement or their cost). Even that
fails if the customer shows reliance is "not fair or reasonable" (s 64A(3)). Read
this way, a cap at the subscription fee is not one of the s 64A forms (an inference
about the cap's wording; the scenario does not give it), so it is void as against the
guarantees. A business customer paying more than $40,000 for software not of a
household kind does not acquire it as a consumer, and then s 64 does not bite.
Asserted.

### 4. For Chloe's laptop, the retailer chooses the remedy, unless the failure is major

Whatever the price, a laptop is goods "of a kind ordinarily acquired for personal ...
use" (s 3(1)(b)), so the s 54 guarantee applies. A failure in month three is presumably
not "durable" quality (an inference; s 54(2)(e)). If the failure can be remedied and is
not major, the consumer "may require the supplier to remedy" it (s 259(2)(a)). The
supplier then chooses repairing, replacing or refunding (s 261). The consumer gets the
choice only when the failure is major or cannot be remedied (s 259(3)), or when the
supplier fails to remedy in a reasonable time (s 259(2)(b)). On rejection, the
supplier must refund or replace "in accordance with an election made by the consumer"
(s 263(4)). An unsafe fault is always major (s 260(1)(e)). Rejection is lost after
the "rejection period" (s 262), but compensation for the drop in value is not
(s 259(3)(b)). So the retailer's repair in c070 is the remedy the Act lets the
retailer pick. Asserted.

### 5. Jake's collectors may fall outside s 50 as Commonwealth law

s 50(1) bars "physical force, or undue harassment or coercion" in connection with
"the payment for goods or services". But s 131A(1) says the Division that applies
Schedule 2 as Commonwealth law "does not apply ... to the supply ... of services that
are financial services, or of financial products". The scenario gives Jake two credit
cards (k048). If the $41,000 is credit card debt, s 50 does not reach its collection
as Commonwealth law, and the ASIC Act would be the place to look. That is an
inference; the ASIC Act is not deposited. The ACCC/ASIC debt collection guideline
that k064 names is not part of the Act. Asserted for the Act's side.

### 6. s 54(6) takes both limbs

Goods do not fail to be of acceptable quality if "(a) the consumer ... causes them to
become of unacceptable quality, or fails to take reasonable steps ...; and (b) they
are damaged by abnormal use". As written, a consumer's neglect without abnormal use
does not take the goods out of the guarantee. Asserted.

### 7. s 18 is one line, and it stops at financial services

"A person must not, in trade or commerce, engage in conduct that is misleading or
deceptive or is likely to mislead or deceive." Whether JARRA is likely to mislead is a
judgement and an input here. Part 2-1 does not apply, as Commonwealth law, to conduct
in relation to financial services (s 131A(2)(a)). Asserted.

## What would need doing before this is worth anything

- The Minister's notification thresholds instrument (s 51ABP) and any class
  determinations (ss 51ABQ, 51ABRA, 51ABRB, 51ABS(6)) need to be deposited and encoded.
  Without them, d065 cannot be answered.
- The ASIC Act's financial services provisions (s 12DJ and the unfair terms
  provisions) are needed for Jake's credit card debts. So is the Fair Trading Act 2010
  (WA), which applies the ACL as WA law.
- The prescribed amount for s 3(1)(a)(ii), if any, should be checked in the
  Competition and Consumer Regulations.
- Every evaluative test (acceptable quality, major failure, unfair, misleading, undue
  harassment) is an input. No case law was read.
- "Corporation", "financial services", "control" (Corporations Act s 50AA) and
  "voting power" are inputs. The extensions in ss 5, 6 and 131(2) are not modelled.
