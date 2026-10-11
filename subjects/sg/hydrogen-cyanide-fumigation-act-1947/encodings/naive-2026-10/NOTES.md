# Hydrogen Cyanide (Fumigation) Act 1947 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/HCFA1947.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021. Its metadata calls it the current version as at 1 October 2026. The
only amendment annotated in the body is [40/2019], against s 4.

**Checks:** one module (`hcfa-fumigation.l4`), one case file, 54 assertions
satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0090**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to. No scenario has asked a sharper question yet.

The Act has six sections, so nearly all of it is encoded: ss 2(1), (3), (4), 3,
4(d) to (f), 5(1), (3), (5) and 6. Not encoded: the list of things the regulations
may cover (s 2(2)), except as a comment; the procedure for annulling regulations (s
2(5)); how an inquiry or formal investigation is run (s 4(a) to (c)); and s 5(2) and
(4). The regulations made under s 2 were not retrieved, so this row cannot say what a
fumigator actually has to do.

## What the Act turns out to say

### 1. The Act sets no fumigation rules of its own, and none at all for open-air work

Every operational requirement (licensing, supervision, how the gas is generated,
disposal of residues, re-entry tests) is something the regulations *may* do (s
2(2)). The Act itself requires none of it. And s 2(3) says the regulations "shall not
apply to any such fumigation carried out in the open air". So hydrogen cyanide
fumigation of timber stacked in a yard is outside the regulations completely.
Asserted.

### 2. The open-air exclusion does not reach the duty to report an accident

The exclusion in s 2(3) covers only "Regulations made under this section". The s 3
duty to notify the Minister of an accident that "occasions loss of human life or
personal injury" has no such limit. So an open-air fumigator who injures someone must
still report it, and faces a fine of up to $200 if they do not. Damage to property
alone triggers no duty. Asserted.

### 3. The duty falls on whoever had the fumigation done "by his agent"

s 3(1) puts the duty on "the person by whom, or by whose agent, the fumigation was
carried out". So a fumigation company is liable for a fumigation carried out by its
workers. Whether a building owner who hires an independent fumigator is that
fumigator's principal is not settled by the text. This row treats the owner as
outside the duty. **That is an inference.** Asserted on that reading.

### 4. The fines are tiny and have not been revised

Breaking the regulations carries a fine of up to $500 per offence (s 2(4)). Failing
to report an accident carries up to $200 (s 3(2)). Ignoring a summons from a formal
investigation, or impeding it, carries up to $100. A failure to furnish a return or
produce a document carries up to $100 for each day it continues (s 4(e)). Nothing in
the Act carries imprisonment. In the defence of reasonable excuse under s 4(e),
"proof of which shall lie on him": the burden is on the accused. A person entitled to
expenses commits no offence by ignoring a summons until those expenses have been
tendered. Asserted.

### 5. A Coroner must stop and wait for the Minister unless one person died and 48 hours' notice was given

s 5(1): an inquest into a death from a reportable fumigation accident must be
adjourned unless someone is present on the Minister's behalf. The exception is when
no more than one person died and the Coroner gave the Minister at least 48 hours'
notice. Then adjourning is not "imperative". With two deaths there is no exception.
The adjourned inquiry needs at least 4 days' written notice to the Minister (s 5(3)).
Asserted.

### 6. The Act can be stretched to any other fumigant by ministerial order

s 6 lets the Minister apply all or some of the Act to "any substance other than
hydrogen cyanide". Without an order, a methyl bromide fumigation is outside the Act.
The words of s 3 do not repeat "with hydrogen cyanide". **Reading s 3 as limited to
fumigations the Act reaches is an inference** from the long title and from s 6. It is
the reading encoded. An order applying only some provisions is modelled as applying
all of them. Asserted on those readings.

## What would need doing before this is worth anything

- Retrieve the regulations made under s 2, and any s 6 orders. They are where the
  real duties of a fumigator are, and where it is decided which other gases are
  covered.
- Settle who counts as the "agent" in s 3(1). This decides whether a property owner
  or a shipowner who hires a fumigator bears the reporting duty.
- Encode partial s 6 orders, and the conduct of inquiries in s 4(a) to (c).
- No case law was searched.
