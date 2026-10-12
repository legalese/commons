# The Kwong-Wai-Shiu Free Hospital (Transfer of Undertaking and Dissolution) Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** informal consolidation, "version in force from 2/7/2017", as deposited
at `../../registers/source-bundle/TKWSFHTUDA2017.txt` (retrieved 1 October 2026,
"Current version as at 01 Oct 2026"). The deposit shows no amendment annotations.

**Checks:** one case file, 43 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0261** in `subjects/sg/requirements.jsonl`: Tier 4 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is ten sections long. A person or business meets it as a creditor, debtor,
contract counterparty, lessee, litigant, trustee or committee member of the old
hospital. This row takes ss 2, 3, 4, 5 and 6. Not encoded: commencement and the
transfer date (s 1 and s 2 — both set by Gazette notification, and neither date is in
the deposit); the employees (s 7 only preserves s 18A of the Employment Act); the
dissolution and repeal of the Ordinance (s 8); the saving of others' rights (s 9); and
the Income Tax Act amendment (s 10), which deletes "item 2" of Paragraph B of the First
Schedule without saying in the deposit what that item was.

## What the Act turns out to say

### 1. Property outside Singapore does not pass, but records do, and so do liabilities

s 2 defines "asset" as property of the transferor "in Singapore" on the eve of the
transfer date. "liability" has no such limit, and s 5 transfers "all records", which
are defined without any place limit either. Reading (an inference, the Act does not
say so in terms): land, money or plant held abroad stays outside the s 3 transfer,
while records kept abroad and debts owed abroad pass to the successor company. Asserted.

### 2. The Minister's ruling binds the successor company, and the Act names no one else

s 6(1) lets the Minister decide disputes over whether an asset, liability or record
was transferred, or whether a contract or document relates to one. s 6(2) makes the
determination "final and binding on the successor company". The Act does not say it
binds the creditor or counterparty on the other side. The encoding asserts only what
the Act makes binding. The power covers what was transferred, not whether a debt
exists at all (reading). Asserted.

### 3. The counterparty cannot treat the transfer itself as a breach, a default or a release

s 3(3): the transfer does not breach an anti-assignment clause or a duty of
confidence, does not terminate an agreement or trigger a termination right, does not
make a contract void or frustrated, does not release a surety "in whole or part", and
is not an event of default. s 3(4): a lessee need not attorn. These cover the transfer
alone; a right arising on some other ground is untouched (inference from "The
operation of this section does not"). Asserted.

### 4. Claims follow the transfer date

Before the transfer date the party is the transferor. From that date, pending
proceedings continue against the successor company, claims that could have been
brought may be brought against it, and judgments may be enforced against it
(s 3(2)(c)-(e)). For a liability that was not the transferor's on the eve of the
transfer date, the Act says nothing, and the encoding returns `not decided by this
Act`. Asserted.

### 5. Trustees and committee members go, with nothing for going

s 4(1) ends every trustee's and committee member's office on the transfer date. s 4(2)
gives them no payment or benefit "merely because" they stop. "Merely" leaves an
entitlement on another ground untouched (reading). Asserted.

### 6. The Registrar must register, on the successor company's application

s 3(5): the Registrar of Titles and other registering authorities "must" register the
transfer on the successor company's application lodged in registrable form. Assets
vest without any further conveyance (s 3(2)(a)). Asserted.

## What would need doing before this is worth anything

- The commencement notification and the transfer-date notification were not retrieved,
  so no date is encoded.
- Section 18A of the Employment Act, the old Kwong-Wai-Shiu Hospital Ordinance and
  item 2 of Paragraph B of the Income Tax Act's First Schedule were not read.
- No case law was searched on the reach of s 6(2) to parties other than the successor
  company.
