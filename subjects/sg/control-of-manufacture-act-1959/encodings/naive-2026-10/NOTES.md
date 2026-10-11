# Control of Manufacture Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 9 March 2025, as
deposited at `../../registers/source-bundle/CMA1959.txt`. The latest amendment
annotated is Act 5 of 2025 (Electronic Gazette and Legislation Act 2025), in s 4(2),
(3). The arrangement of sections at the top of the deposit is out of step with the
body by one. This row follows the body's numbers.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0097**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to. No scenario has asked a sharper question yet. The Act is
short, so this row takes nearly everything a manufacturer meets: what counts as
specified goods and as manufacture (s 2, Schedules), the duty to register (s 3), the
exemption power (s 14(1)), registration and the protection for existing manufacturers
(s 5), revocation and its deadlines (s 6), information demands (s 7), offences, fines
and composition (ss 8, 9, 14(3)) and liability for a servant (s 11). Not encoded:
the Registrar's appointment (s 4), entry and inspection (s 10), the annual duty
(s 12, no order retrieved), varying the First Schedule (s 13), other written law
(s 15), rules (s 16) and laying before Parliament (s 17). No rules, orders or forms
made under the Act were retrieved, so the application form, information and fee are
unknown.

## What the Act turns out to say

### 1. Six goods, and only six, need a licence to make

Registration is required only for the goods in the two Schedules: beer and stout,
cigars, drawn steel products and chewing gum (First Schedule), and cigarettes and
matches (Second Schedule). Wine is not listed; nor is anything else. Chewing gum
that is a health product (an oral dental gum or a therapeutic product under the
Health Products Act 2007) is carved out. Reading s 2's "includes" as confining the
Act to the Schedules is an inference, supported by s 8(1), which penalises only
manufacture of "goods specified in the First or Second Schedule". Asserted.

### 2. The $50,000 offence can be compounded for $1,000

Making specified goods for sale without registration carries a fine of up to $50,000
plus $1,000 for each day it continues after conviction (s 8(1)). Breaching a
condition carries up to $10,000 plus $1,000 a day (s 8(2)). Yet s 9 lets the
Registrar compound "any offence under this Act" for a sum "not exceeding $1,000",
the same ceiling as the information offences in s 8(3). No offence carries
imprisonment. Asserted.

### 3. The protection for existing manufacturers covers the First Schedule only

s 5(3): a person who was already making the goods in Singapore, or had made
substantial preparations, immediately before the goods were added to the First
Schedule, and who applies within 6 months, "shall not be refused", and no condition
may be imposed. The Minister may not then withhold consent to transfer that
registration (s 5(6)). The subsection names only the First Schedule, so a cigarette
or match maker (Second Schedule) has no such protection. s 13 likewise lets the
Minister vary only the First Schedule. Asserted.

### 4. Revocation runs to three clocks that meet on day 21

The Registrar may revoke, after notice, for misrepresentation, breach of a condition,
or stopping manufacture for a continuous 3 months (s 6(1)). Failing a minimum-quantity
notice counts as stopping (s 6(6)); exceeding a Minister's production cap counts as
breaching a condition (s 14(3)). The Registrar must notify within 7 days of the
decision (s 6(2)); the manufacturer may appeal within 14 days of that notice
(s 6(3)); the revocation takes effect 21 days after the decision unless an appeal is
brought, and then on its determination (s 6(4)). A manufacturer notified on the last
permitted day has until day 21, the day revocation takes effect. The day arithmetic
is asserted; the coincidence is an observation.

### 5. Two appeals, two final forums

A refusal or a condition goes to the Minister, "whose decision shall be final"
(s 5(4)). A revocation goes to the General Division of the High Court, also final
(s 6(3)). Asserted.

### 6. The Registrar may not ask for a secret process

s 7(2): the power to demand information about the conditions of registration does
not extend to "any secret process", and what is supplied is confidential unless the
use is for the Act or the manufacturer consents in writing (s 7(3)). Asserted.

### 7. Vicarious liability reaches only registered goods

s 11 makes an employer liable for an agent's or servant's acts "in connection with
the manufacture of the goods ... in respect of which he is registered". Read
literally, it does not reach an unregistered maker's staff. Asserted on that literal
reading.

## What would need doing before this is worth anything

- Whether the "mechanical power" words in the definition of "manufacture" qualify
  limb (c) only, as encoded, or all three limbs, needs the official print or case law.
  It decides whether a hand-made batch of beer for sale needs registration.
- The rules, the s 12 duty order and any s 14(1) exemptions were not retrieved.
- Day counts ignore calendar rules (Interpretation Act computation of time).
- No case law or Registrar practice was searched.
