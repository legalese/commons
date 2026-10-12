# Government Technology Agency Act 2016 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/GTAA2016.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment annotated is S 461/2020 (Variable Capital
Companies consequential amendments, in force 15 June 2020). The other is Act 5 of 2018
(Public Sector (Governance) Act 2018). The retrieval record calls it the current
version as at 1 October 2026.

**Checks:** one module, one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0171** in `subjects/sg/requirements.jsonl`: tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to. No scenario has asked a sharper
question yet.

Most of the Act sets up GovTech as a statutory board. This row takes the provisions an
outsider, an employee or contractor, a board member or an essential-service company
can actually meet: ss 2, 9, 12(2), 21(1)(g), 31, 43, 44, 61, 62, 65, 67, 68, 69 and 71.
These are not encoded: functions and general powers (ss 5 to 8), appointment and terms
of members, meetings, the seal, committees and delegation, personnel, finance, s 70
(which mirrors s 69 for associations and partnerships), and the 2016 transfer from
IDA (Parts 10 and 11).

## What the Act turns out to say

### 1. GovTech can give orders to a Ministry, but only advice to a private company

s 62 lets the Agency, with the Minister's authorisation, "implement, or direct the
public sector body responsible ... to implement" security, mitigation or recovery
measures. Part 8 reaches private "public entities". These are bodies corporate, not
public authorities, that provide an essential service and receive Government support
(s 2). That reach takes several steps: a responsible Minister's request on two
conditions (s 65), arrangements the responsible Minister approves, and a Gazette
declaration (s 66). Even then s 67 gives the Agency powers only to recommend, audit,
"advise" and report. It gets no power to direct. Asserted.

### 2. Permission is no defence to a look-alike symbol

s 9(2)(a) makes it an offence to use a symbol identical to the Agency's "without the
prior written permission of the Agency". Para (b), using one that "so resembles" it as
to be likely to deceive or confuse, has no permission exception. Read literally,
written permission protects an identical copy but not a confusing look-alike. The
maximum is $5,000 or 6 months or both. Asserted on the literal reading.

### 3. The protection is wider than the secrecy duty

s 43 binds the Chief Executive, members, employees, delegates and committee members.
By s 2 "employee" includes anyone "otherwise engaged to perform duties in the Agency",
so a contractor engaged that way is bound too. The duty covers information they would
not otherwise have had. It allows five exceptions, including authorisation and a court
order. The maximum is $2,000 or **12 months**: a lower fine than the symbol offence but
twice the prison term. s 44 also protects "any other person acting under the direction
of the Agency" who acts in good faith and with reasonable care. On this reading a vendor
working under direction is protected but not bound by secrecy. Asserted.

### 4. Composition is capped at $2,000, and in practice at $1,000 for secrecy

s 68 caps a composition at the lower of half the maximum fine and $2,000. That is
$2,000 for the symbol offence ($5,000 / 2 = $2,500, capped) and $1,000 for a secrecy
breach. Only offences "prescribed as a compoundable offence" can be compounded. No
regulations were retrieved, so whether either offence is prescribed is unknown.
Asserted (the cap only).

### 5. Officers answer for the company's offence even if it is never convicted

s 69(2) makes an officer, or a manager in a position to influence the conduct, guilty
of the same offence if they consented, connived or conspired, were knowingly concerned,
or knew or ought to have known and failed to take all reasonable steps. Under s 69(5)
this applies "whether or not the corporation is convicted". Asserted.

### 6. Smaller points

- s 71(5)(c): registered post takes effect 2 days after posting "even if it is returned
  undelivered". Email must go to the address the person last gave for service (s 71(7)).
  The section does not apply to court documents (s 71(6)). Asserted.
- s 12(2)(c): a prison sentence of 6 months or more disqualifies a member unless he or
  she has received a free pardon. s 21(1)(g): missing 3 consecutive meetings without
  approval ends membership. s 31: the quorum is the higher of one-third and 3. With 17
  members that means 6 must be present. Asserted.
- A Town Council is excluded from "public authority" (s 2), and "public sector" is the
  Government and all public authorities. That a Town Council is therefore outside the
  Agency's public-sector powers is an **inference**. Encoded that way.
- s 75(1) speaks of the "Info-communications Development **Agency** of Singapore",
  whereas s 74 defines the transferor as the "Authority". This looks like a slip in the
  text. Not encoded.
- s 5(4): the functions impose no duty "enforceable by proceedings before any court".
  Not encoded.

## What would need doing before this is worth anything

- Retrieve any regulations under s 73, especially any prescribing compoundable offences.
- Check the s 9(2)(b) reading (permission and look-alikes) against case law or practice
  on the identical provisions in other statutory-board Acts.
- Confirm the Town Council inference, and whether any public entity has ever been
  declared under s 66(3).
- No case law, Gazette notifications or GovTech publications were searched.
