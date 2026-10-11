# Payment and Settlement Systems (Finality and Netting) Act 2002 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 9/3/2025, as
deposited at `../../registers/source-bundle/PSSFNA2002.txt`. The latest amendment
annotated is Act 5 of 2025 (wef 9 March 2025), on s 19(2) and (2A). The arrangement
of sections at the top of the deposit is out of step with the body; the body's
numbers are followed.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0111**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act protects
"payment and settlement systems" (long title); the persons it binds are participants, operators, settlement institutions and
collateral holders of a designated system. This row takes designation and
revocation (ss 3, 4), holding out (s 4A), Part 2 finality against insolvency
(ss 6, 7, 8(3)-(4), 12), netting on insolvency (s 13), foreign insolvency orders
(s 14), the information and notification duties (ss 15A, 15B, 16), composition
(s 17), protection from liability (s 17C), approval of Rules (s 19A), the
direction offence (s 20A(6)) and the Authority's own exemption (s 5(2)).

Not encoded: the s 2 definitions beyond what the rules use, the Authority's
restrictions under s 5(1), the IRDA sections disapplied by ss 9 and 10, the net sum
under s 11, preservation of underlying rights (s 15), attribution to corporations
and partnerships (ss 17A, 17B), ss 18 to 20, exemptions (s 20B) and the deemed
designation of the old MAS system (s 21). No regulations or Gazette orders were
retrieved, so which systems are designated and which offences are compoundable are
not known here.

## What the Act turns out to say

### 1. A final settlement cannot be undone, by anyone, on any ground in the general law

Where a designated system's Rules make a transfer, netting or settlement "final and
irrevocable", s 7(2) says that "despite anything to the contrary in any written law
or rule of law" it "must not be reversed, repaid or set aside", and no court may
order its rectification or stay. s 8 makes the system's own actions prevail over the
insolvency distribution rules and bars office holders and courts from interfering.
Asserted.

### 2. The shield lasts one business day after insolvency, then falls away

s 12: Part 2 does not apply to a transfer order "entered into a designated system
after the expiry of one business day after" a bankruptcy, judicial management or
winding up order, a judicial management resolution, or a voluntary winding up
resolution. The encoding counts the event's own business day as 0, so entry on day
0 or 1 is protected and day 2 is not; that count is an inference from the wording.
Part 2 applies to insolvency proceedings only in respect of a participant (s 6(2),
(3)). Asserted.

### 3. Netting under s 13 does not reach judicial management

s 13 lets the operator net all obligations "incurred up to and including one
business day after" a bankruptcy or winding up order or a voluntary winding up
resolution, and the netting is "not voidable". Judicial management is not in the
list, although it is in ss 12 and 16. Asserted.

### 4. Two notification duties, with different excuses

A participant, operator, settlement institution or collateral holder that becomes,
"or is likely to become", insolvent must tell the Authority (s 15B; fine up to
$200,000), unless it has already told the Authority under another law the
Authority administers. A participant must separately tell the operator of a
bankruptcy, judicial management or winding up order or resolution (s 16; fine up to
$20,000). Under s 16 it has not contravened if it took reasonable steps or the
operator already knew. The Authority itself is exempt when acting in any of these
roles (s 5(2)). Asserted.

### 5. The Authority can revoke without a hearing on insolvency grounds

s 4(2) requires the operator to be heard before revocation, but s 4(3) excuses the
hearing where the operator or settlement institution is being wound up, has made a
compromise with creditors, or has a receiver or judicial manager. s 4(4): revocation
never avoids a transaction already cleared or settled. Asserted.

### 6. Penalties are steep, and compounding is capped at half

Holding out as an operator or settlement institution: $100,000 or 2 years, plus
$10,000 a day (s 4A). Implementing or amending Rules without written approval:
$200,000 plus $20,000 a day (s 19A), though Rules in place before 6 June 2018 are
deemed approved. Failing to obey a written direction: $150,000 plus $15,000 a day
(s 20A(6)). Information offences run from $15,000 (careless) to $150,000, and the
individual answerable for compliance faces $125,000, or 12 months as well if wilful
(s 15A). The Authority may compound a prescribed offence for "half of the amount of
the maximum fine" (s 17); whether the daily fine counts is not said, and the
encoding halves the base fine only. Asserted.

### 7. Protection from liability covers the system side, not participants

s 17C protects operators, settlement institutions and collateral holders, and their
officers and employees, for acts done "with reasonable care and in good faith".
Participants are not in the list. Asserted.

## What would need doing before this is worth anything

- The Gazette orders designating systems, and the regulations prescribing
  compoundable offences and further notifiable events, were not retrieved.
- The IRDA provisions disapplied by ss 9, 10 and 11 were not read, so their effect is
  not encoded.
- The business-day count under ss 12 and 13 is an inference and has not been checked
  against any decided case.
- No case law was searched.
