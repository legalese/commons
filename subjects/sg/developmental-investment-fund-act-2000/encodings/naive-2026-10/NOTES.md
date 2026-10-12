# Developmental Investment Fund Act 2000 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
31 January 2022), as deposited at `../../registers/source-bundle/DIFA2000.txt`. The
latest amending Act annotated is Act 35 of 2021 (Government Borrowing (Miscellaneous
Amendments) Act 2021, in force 31 January 2022). The source metadata records the
version as current at 1 October 2026.

**Checks:** one module, one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0167** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The surviving Act is short (ss 1-9 and 17-20; Part 3, ss 10-16, was repealed by Act
35 of 2021), so the scope is nearly all of it: ss 2, 3, 4, 5, 6(1), 6(2)(a), 8, 9,
17(3), (4) and 18. Not encoded: s 1; s 6(2)(b), (c) (prudent-investor and
developmental-objective duties, not decidable on facts); s 7 beyond a flag; s 17(1),
(2); s 19 beyond its effect; s 20 (no regulations were retrieved). The Financial
Procedure Act 1966 and the Penal Code 1871, to which ss 4(2), 17(4) and 19 refer, were
not read.

## What the Act turns out to say

### 1. It decides almost nothing for a person or business

The Act gives no one a right, creates no offence or penalty, and sets no application
procedure. A business meets it only as a possible investee: s 4(1) lets the Fund buy
securities in, help form, or invest in property for, a "developmental purpose". There
is no head for an outright grant or subsidy, nor for a ministry's running costs — the
moneys may be applied for the listed purposes "only". Asserted.

### 2. Land must be in Singapore; technology need not be

s 2 "developmental purpose" (c) is "to reclaim or develop any land in Singapore or to
commercially exploit or apply any scientific knowledge or technology". Reclaiming land
abroad is not a developmental purpose (nor is a survey preparatory to it, under (d));
commercialising a technology is, wherever it happens. s 4(1)(c) separately allows
investment in funds or property "whether within or outside Singapore", but still only
for a developmental purpose. Asserted.

### 3. For account moneys, only the responsible Minister may authorise a payment

s 5(2) keeps the Minister for Finance "overall responsible" even after an account is
assigned under s 6(1). But s 9(2) says no payment from an account may be made "unless
the payment is authorised by the responsible Minister in charge of that account" — read
literally, the Minister for Finance's own authorisation does not suffice there. Whether
a court would read s 9(2) that way is not known; the literal reading is what is
encoded. Asserted.

### 4. A statutory-board officer appointed accounting officer becomes a public servant

s 17(3): the accounting officer for an account must be "a public officer or an officer of
any public authority" — so not a private fund manager or private accountant. s 17(4):
an officer of a public authority so appointed is deemed a public officer for the
Financial Procedure Act 1966 (whose s 20 then applies to him or her) and "a public
servant for the purposes of the Penal Code 1871". What follows from that under the Penal
Code was not read. Asserted for the appointment and the deeming.

### 5. Investments escape s 7(3) of the Financial Procedure Act; incidental costs do not

s 4(2) disapplies s 7(3) of the Financial Procedure Act 1966 for applications under
s 4(1)(a), (b) and (c) only; s 19 applies that Act to the Fund otherwise. So brokerage
(s 4(1)(d)) and Fund expenses (s 4(1)(e)) remain subject to it. What s 7(3) says was not
read. Asserted.

### 6. Net income nets realised gains and losses into income

s 3(3): net income from investments is the income received plus any realised profit or
minus any realised loss, and s 3(1)(d) pays it into the Fund. A large realised loss can
make it negative; the Act does not say what then happens. The financial year ends on
31 March (s 2). Asserted.

## What would need doing before this is worth anything

- Read the Financial Procedure Act 1966 (ss 7(3) and 20) and the Penal Code 1871
  provisions on public servants, to say what ss 4(2), 17(4) and 19 actually do.
- Retrieve any regulations made under s 20 (prescribed investments) and any s 6(1)
  orders.
- Check the literal reading of s 9(2) against practice or authority.
- The "developmental purpose" categories are encoded as sample aims, not as a test a new
  fact pattern can be run through.
