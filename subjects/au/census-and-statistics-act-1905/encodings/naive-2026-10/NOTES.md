# Census and Statistics Act 1905 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions (the skill itself was not available in this session; the finished naive
encodings in `subjects/sg` were followed). No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** Compilation No. 9, compilation date 1 October 2020 (includes amendments
up to Act No. 64, 2020), register id C2020C00296, as deposited at
`../../registers/source-bundle/C1905A00015.txt` (retrieved 13 October 2026 as the
current compilation).

**Checks:** one module (`csa-census.l4`), one case file (`csa-cases-census.l4`),
54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0021** in `subjects/au/requirements.jsonl` (priority 1), raised
**3 times** by the Western Australian cradle-to-grave scenarios:

- Chloe **c049** (2026-08-10, census night; Chloe 23, Liam 27): "Must they complete
  it?" (ss 8, 14).
- Jake **k047** (2031-06-30, census night at his sister's; s 14; no question stated).
- Daniel **d048** (2032-06-30, a business survey from the Bureau of Statistics to
  Jarrah): "Must a company answer?" (s 14).

The encoding takes when the Census is taken (s 8), the ways the Statistician may ask
(ss 10, 11), the offence of not complying (s 14) with its daily repetition and joinder
(s 14 Note 2, ss 21, 22), false answers (s 15), the penalties (ss 14, 15, 19, 20), and
the protections a person answering would ask about: entry to premises (s 18), officer
secrecy (s 19), the 99-year bar (s 19A) and transfer to the Archives (s 8A). Not
encoded: ss 6, 7, 9 (beyond being a purpose), 12, 13 (beyond its effect on s 19), 16,
17, 19B, 27. The Census day (proclamation), other Census years and classes of
premises (regulations), the s 10(2) instrument, the value of a penalty unit (Crimes
Act 1914) and who is a "person" are INPUTS.

## What the Act turns out to say

### 1. Not filling in the Census form is not, by itself, an offence

s 14(1) makes it an offence only where "the person is served a direction under
subsection 10(4) or 11(2)" and fails to comply. The Census form itself is required by
**notifiable instrument** under s 10(2), and a collector's request is made under
s 10(3) or 11(1); neither is a direction under s 10(4) or 11(2). So for c049 the
answer to "Must they complete it?" is: they are *required* (if an s 10(2) instrument
covers their class), but no offence is committed until the Statistician serves a
written direction, personally or by post, and the period it gives runs out. The
scenario's question treats the duty as arising on census night; the text puts the
penalty later. Asserted.

### 2. A company asked to complete a business survey is in the same position

A business survey is a collection for s 9, not s 8. The s 10(2) instrument is
available only "for the purposes of section 8", so for d048 the Statistician can only
request (no offence) or direct under s 10(4) or 11(2) (offence on non-compliance).
Whether a company is a "person" is not stated in this Act; that is left as an INPUT
(inference: the Acts Interpretation Act 1901, not deposited, would decide it).
Asserted for the methods; the company point is not asserted.

### 3. The penalty is one penalty unit, but it repeats daily

s 14: "Penalty: One penalty unit"; strict liability (s 14(2)). Note 2 and s 21 make
the obligation continue after the period, with an offence "in respect of each day
until the person complies", and s 22 lets the charges be joined with one penalty up
to the sum of the separate maximums. The encoding counts one offence for each day
after the period has run (an inference about where counting starts). The dollar value
of a penalty unit is an INPUT; the case file uses a hypothetical 100. Asserted.

### 4. Religion is the one question that may be left unanswered

s 14(3): s 14(1) "does not apply in relation to a person's failure to answer a
question, or to supply particulars, relating to the person's religious beliefs". The
defendant bears an evidential burden. Asserted.

### 5. Lying is an offence on every method, refusing only on two

s 15 (10 penalty units) reaches anyone "required, requested or directed" under
s 10(2), (3) or (4) or s 11(1) or (2) who knowingly gives false or misleading
information. So a false answer on the Census form without any direction is an
offence, though leaving it blank is not. Asserted.

### 6. A direction must give at least 14 days and explain s 14

ss 10(4), 11(2) require a period "not less than 14 days"; ss 10(5), 11(3) require the
notice to "set out the effect of the provisions of section 14". The Act does not say
what a defective notice does; the encoding treats it as not a direction, so no s 14
offence. Inference. Asserted on that inference.

### 7. Census years and the 99-year bar

s 8(1): 1981 "and in every fifth year thereafter", plus prescribed times: 2026 and
2031 (c049, k047) are Census years; 2032 (d048) is not. s 19A: for 99 years from the
Census day, officers cannot be required to, and must not voluntarily, give Census
form information to an Agency or a court or tribunal. s 18 entry powers exclude
dwelling-houses, flats and home units, and parts separately used for residence or
sleeping. s 8A: forms from 2001 on go to the Archives only with consent. Asserted.

## What would need doing before this is worth anything

- The compilation is of 1 October 2020; the events run to 2032. Later amendments
  would need checking against the register.
- The Census day proclamation and the s 10(2) notifiable instrument for 2026 were not
  retrieved; whether Chloe's class of persons is covered is an input.
- The Crimes Act 1914 (penalty unit value, s 4K), the Criminal Code (ss 6.1, 13.3) and
  the Acts Interpretation Act 1901 (meaning of "person") were not read.
- The reading of a defective direction (finding 6) and the start of daily counting
  (finding 3) are inferences that case law might settle; none was searched.
