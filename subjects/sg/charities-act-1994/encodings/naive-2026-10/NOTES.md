# Charities Act 1994 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 25 of
2021).

**Checks:** two case files, 72 assertions satisfied (27 in `cha-cases-governance.l4`, 45 in `cha-cases-ipc.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**14 of the 527 Singapore Acts** deposited here cite it. This row takes what a
charity's board members and donors meet: registration, the cost of an ordered audit,
cy-près and disqualification. The Commissioner and Council, accounts and reports,
the protective powers, fund-raising, institutions of a public character and the
Schedule of exempt charities are not encoded.

## What the Act turns out to say

### 1. Board members pay personally for a late audit

s 13(2): if a required audit is not done within 10 months after the year end, the
Commissioner may appoint an auditor. s 13(3): the cost is paid by "the governing board
members ... who shall be personally liable, jointly and severally". The charity's funds
are used only if recovery from the board is not practical. Asserted.

### 2. Missing a filing deadline can mean prison

s 7(8): register within 3 months of establishment, and notify any change in governing
instruments or particulars within 7 days. Default carries up to $10,000 **or 3 years**,
plus $100 a day. Asserted.

### 3. Collecting-box money goes cy-près automatically

s 20(3): proceeds of collecting boxes, lotteries, competitions, entertainments and
sales are "conclusively presumed" to belong to unidentifiable donors. If the purpose
fails, they go cy-près without any advertisement or inquiry. A named donor's gift does
not. s 19 lists when a purpose has failed; a board simply preferring another cause is
not one. Asserted.

### 4. Who may not serve

s 28(1): disqualified are:
- anyone convicted anywhere of a dishonesty, terrorism, terrorism-financing or
  money-laundering offence, until the conviction is spent
- undischarged bankrupts
- anyone in an undischarged composition with creditors
- anyone disqualified under the Companies Act

Under s 28(3), a bankrupt or Companies Act disqualification can be overridden for a
charity that is a company, if Companies Act permission is held. Asserted.

## What would need doing before this is worth anything

- The audit thresholds are in the Charities (Accounts and Annual Report) Regulations,
  which were not retrieved.
- The IPC approval criteria and tax-deduction-receipt rules (Part 9) are in regulations; see the section below.
- No case law was searched.

## Institutions of a public character (added 12 October 2026 for REQ-0292)

Module `cha-ipc.l4`, cases `cha-cases-ipc.l4` (45 assertions). Raised by the Haziq
scenario, event h072: a newly registered charity wants donations to it to be
tax-deductible -- what status, granted by whom, on what conditions?

1. **The status is "institution of a public character" (IPC); registration alone is not
   enough.** s 40: an IPC is "a registered charity or an exempt charity in Singapore" that
   is (a) approved as an IPC "on the application of the charity", or (b) deemed one "under
   any written law". A newly registered charity that has not been approved is not an IPC.
   The link to tax: Income Tax Act 1947 s 37(3)(c)(ii) deducts a multiple of a donation of
   money to "any institution of a public character", and that Act's s 2 takes the meaning
   from the Charities Act (read in the ITA deposit; not encoded beyond a pointer). Asserted.
2. **Who grants it: the Minister, the Commissioner of Charities, or a Sector
   Administrator** (s 40(a)). A Sector Administrator is appointed by the Minister (s 41) and
   approves IPCs only if appointed for that purpose and only "from among such class or
   classes of institutions as the Minister or Commissioner may determine" (s 41(b)). The
   Comptroller of Income Tax is not an approving authority. The charity must apply.
   Asserted.
3. **On what conditions: the Act does not say.** s 42(1)(a) leaves "the manner and
   criteria" for approval, extension and revocation to regulations made by the Minister,
   as it does the use of donations, the issue of tax deduction receipts and donation
   records (s 42(1)(c)). Those regulations were not retrieved, so the substantive
   conditions (and any period of approval) are not encoded. The only statutory conditions
   are being a registered or exempt charity, applying, and approval by one of the three.
   The ledger gave no expected answer; this row cannot give the full one.
4. **Deductibility of a particular donation turns on the Income Tax Act**, not on this Act:
   s 37(3A) sets the multiple (2.5 times for donations from 1 January 2016 to 31 December
   2026, per the ITA deposit), (3B) requires the donor to give the information the
   Comptroller specifies, and (3C) to (3G) deal with conditional donations and benefits to
   the donor. Not encoded here.
5. **Losing it.** For a contravention of the IPC regulations the regulations may provide
   that the Minister, Commissioner or Sector Administrator revokes the approval (s 42(2)(a));
   that it is an offence carrying up to $10,000 or 3 years or both, plus $100 a day
   (s 42(2)(b)); and, for a tax-deduction-receipt contravention that is not an offence, a
   financial penalty of the higher of $100 and 0.4 x the donations that ought not to be
   deductible (s 42(2)(c)), recoverable as a debt (3), remissible by the Commissioner (4),
   and paid net into the Consolidated Fund (5). These operate only so far as the
   regulations adopt them -- s 42(2) says the regulations "may provide for" them. Asserted.
6. **Delegation.** Regulations may let the Commissioner delegate functions to a Sector
   Administrator, except powers under ss 22, 23, 24, 26, 27 and 31 (s 42(1)(e)). Asserted.
7. **Claiming IPC status falsely is an offence** (s 49): the institution, and anyone acting
   for it unless they prove the holding out was without their knowledge or consent; up to
   $10,000 or 3 years or both, plus $100 a day. Asserted.

Needs for a full answer: the regulations under s 42 (inferred to be the Charities
(Institutions of a Public Character) Regulations -- not in the deposit, not verified), the
Gazette notices of Sector Administrators' sectors, the Commissioner's IPC policy or
guidance, and the Income Tax Act 1947 s 37 and its rules for the deduction itself. No case
law was searched.
