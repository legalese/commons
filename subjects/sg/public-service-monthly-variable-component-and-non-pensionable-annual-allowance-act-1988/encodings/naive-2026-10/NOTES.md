# Public Service (Monthly Variable Component and Non-pensionable Annual Allowance) Act 1988 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example naive rows (the `writing-l4-rules` skill was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** 2020 Revised Edition, deposited at
`../../registers/source-bundle/PSMVCNAAA1988.txt`. The deposit says it "incorporates
all amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". Its Legislative History lists no amending Act after Act 14 of 1988,
only the 1989 and 2014 Revised Editions, and a predecessor, the Public Service
(Variation of 1984 Annual Wage Increases) Act 1987 (Act 19 of 1987).

**Checks:** one case file, 36 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0199** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act has four sections, so the row covers all of its operative text (ss 2, 3 and
4). Not encoded: what any order under s 3(1) says (none was retrieved, so every rate
and amount in the cases is a stated fact, not a figure from an order); which
statutory bodies have been designated by Gazette notification; and how the Pensions
Act 1956 and the Parliamentary Pensions Act 1978 compute a pension once s 4 has
handed them a figure.

## What the Act turns out to say

### 1. A public servant's promised pay can be cut by Gazette, whatever the contract or collective agreement says

s 3(3): any term or condition of employment in the public service "(including any
collective agreement)" imposing a liability to pay the monthly variable component
or the 13th month allowance "in excess of the rates or amount specified in the
order is, to the extent of the excess, void". A $500 promise against a $300 order
leaves $300 enforceable and $200 void, whether the promise is in a contract, a
collective agreement or a scheme of service. Asserted.

### 2. The cut lasts only while the order does

The excess is void "so long as the order remains in force". With no order in force,
nothing is void and the full promise is enforceable again. Asserted.

### 3. The pension is computed as though there had been no cut — but only a cut, and only under two Acts

s 4: pensions, gratuities and other allowances under the Pensions Act 1956 and the
Parliamentary Pensions Act 1978 "must be computed as if the monthly variable
component applicable to that person had not been reduced by virtue of any order".
A reduction from $500 to $300 (or to nothing) is disregarded; an order that
**raises** the component is not undone, since s 4 speaks only of reduction.
Benefits under any other law or scheme get no such protection from this Act.
s 4 does not mention the 13th month allowance at all. Asserted.

### 4. "Public service" reaches statutory bodies only once the Minister designates them

s 2: public service is service under the Government, and includes public office
holders, Members of Parliament, and service under a statutory body or authority
"designated by the Minister by notification in the Gazette". Employees of an
undesignated statutory body are outside the Act, and so is the private sector.
s 3(2) binds only "the Government and any designated statutory body or authority"
to give effect to an order. Asserted.

### 5. The "monthly variable component" is defined by history

s 2 defines it as "the aggregate of the annual wage increases for the years 1982 to
1984 payable pursuant to the recommendations of the National Wages Council". The
deposit does not say whether the term is used in that sense in public-sector pay
today; that would need sources outside the deposit. Not asserted.

### 6. What happens when an order raises pay is an inference

s 3(3) voids only an excess over the order; it says nothing about an order that
specifies more than a term promises. s 3(2) requires the Government and designated
bodies to "give effect to the order". The encoding reads that, as an **inference**,
to mean the employer pays the order's figure — up or down — while the order is in
force (`the amount the employer pays`). Asserted, as an inference.

## What would need doing before this is worth anything

- Retrieve the orders made under s 3(1), and the Gazette notifications designating
  statutory bodies under s 2(b), and check whether any is in force.
- Confirm the s 3(2) inference in finding 6 against an order or official guidance.
- Connect s 4 to encodings of the Pensions Act 1956 and the Parliamentary Pensions
  Act 1978, so that the protected figure flows into an actual pension computation.
- No case law was searched.
