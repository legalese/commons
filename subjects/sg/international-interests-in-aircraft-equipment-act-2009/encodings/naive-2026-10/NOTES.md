# International Interests in Aircraft Equipment Act 2009 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, deposited at
`../../registers/source-bundle/IIAEA2009.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The latest amendment annotated in the body is 40/2019 (s 5).

**Checks:** one module, one case file, 59 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0104**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to. No scenario has asked a sharper question yet.

The Act itself has six sections. Its substance is the Cape Town Convention (First
Schedule) and Aircraft Protocol (Second Schedule), which s 3 gives the force of law,
and the insolvency remedy in s 4. The people it decides things for are airlines,
lessors, financiers, buyers of aircraft and engines, and the liquidators and
judicial managers of an insolvent operator. This row takes:

- which equipment is covered (Protocol Art I(2));
- when the Convention applies (Convention Arts 3, 4 and Protocol Art IV(1));
- how an international interest is constituted (Art 7, Protocol Art VII) and what
  counts as default (Art 11);
- priority (Arts 29, 30(1), 39(3) and Protocol Art XIV);
- de-registration and export, and the notice safe harbour (Protocol Art IX(2), (4));
- the Act's own insolvency rules (s 2(1) "commencement of insolvency proceedings" and s 4).

Not encoded: the International Registry's machinery, assignments, relief pending
final determination, jurisdiction (including s 5), vesting and redemption, surplus
distribution, the final clauses, and the Third Schedule consolidated text, which
s 3(3) makes an aid to interpretation only. **Singapore's declarations are not in
the deposit.** s 3(1)(b) applies the treaty "to Singapore as described in the
declarations", so anything they add or withhold is missing here.

## What the Act turns out to say

### 1. The Act fixes the waiting period at 30 days, and lets the parties contract out

Protocol Art XI Alternative A leaves the "waiting period" to the declaring State's
declaration (Art XI(3)). s 4(14) sets the deadline itself: the earlier of 30 days
after the insolvency proceedings commence and the day the creditor would have been
entitled to possession anyway. s 4(2)(c) disapplies the section where the debtor and
creditor "have by written agreement excluded" it. Protocol Art IV(3) also lets the
parties exclude Art XI in writing. Asserted.

### 2. Section 4 asks for less than the Protocol: an opportunity, not possession

Protocol Art XI(2) Alternative A says the administrator or debtor "shall ... give
possession" of the aircraft object. s 4(3) says it "must ... give an opportunity to
the creditor to take possession". The duty also applies only if "the aircraft object
is in Singapore". The debtor side may keep the object only if, by the deadline, it
has both agreed to perform all future obligations and cured every default other than
the insolvency itself (s 4(4)). If it then fails to perform, the creditor may take
possession "immediately" (s 4(5)). Asserted.

### 3. Who counts as a Singapore debtor depends on what kind of debtor it is

s 4(2)(a) asks a company or firm only whether it is "incorporated or registered in
Singapore". It asks a natural person whether they are domiciled in Singapore or have
their principal place of business there. A foreign-incorporated airline with its
main base in Singapore is therefore outside s 4. The interest must also be
registered (s 4(2)(b)). Asserted.

### 4. The deadline also limits who is bound

s 4(13): subsections (3) to (8) do not apply to an insolvency administrator
"appointed on or after" the s 4(14) date. An administrator appointed on day 30 is
not bound by them; one appointed on day 29 is. Only the insolvency administrator is
indemnified for the reasonable costs of preserving the object (s 4(8)). A debtor
preserving it itself is not named. Asserted.

### 5. Small aircraft fall outside the Act entirely

An airframe is covered only if it is type certified for "at least eight (8) persons
including crew" or goods "in excess of 2750 kilograms". The figures for a helicopter
are five persons or more than 450 kg. A jet engine needs at least 1750 lb of thrust,
and a turbine or piston engine at least 550 rated take-off shaft horsepower. Military,
customs and police equipment is excluded (Protocol Art I(2)(b), (e), (l)). A
seven-seat aircraft certified for 2,750 kg of goods is not an aircraft object: a cargo limit of exactly 2,750 kg
is not "in excess of" it. Asserted.

### 6. Registration beats knowledge

A registered interest has priority over one registered later and over any
unregistered interest, "even if" its holder knew of the other (Art 29(1), (2)). A
buyer under a registered sale takes free of an unregistered interest even with actual
knowledge (Protocol Art XIV(1)), but subject to anything registered at the time of
acquisition (XIV(2)). An interest registered between the buyer's acquisition and the
registration of the sale fits neither paragraph. This encoding returns "left to the
applicable law" for that case, **an inference**. In insolvency an interest is effective
only if registered *before* commencement (Art 30(1)). Asserted.

### 7. Smaller rules

- A non-consensual right outranks an international interest "if and only if" its
  category was declared before the interest was registered (Art 39(3); s 4(15)).
  Asserted.
- The manufacturer's serial number, the manufacturer's name and the model
  designation are "necessary and sufficient" to identify the object (Protocol
  Art VII). A security agreement must also let the secured obligations be determined,
  though no sum need be stated (Art 7(d)). Asserted.
- A creditor may not de-register or export the aircraft without the prior written
  consent of any higher-ranking registered interest holder (Protocol Art IX(2)). Ten
  working days' written notice of a sale or lease is deemed reasonable (IX(4)). The
  parties cannot vary either rule (Art IV(3)). Asserted.
- Commencement under s 2(1) is the date of an *application* (bankruptcy, interim
  order, compromise, judicial management order), the deemed commencement of a winding
  up, or the lodgment of notice of appointment of an interim judicial manager.
  Asserted for three kinds.
- An engine's ownership is "not affected by its installation on or removal from an
  aircraft" (Protocol Art XIV(3)). Not asserted: it has no input that changes the
  answer.

## What would need doing before this is worth anything

- Retrieve Singapore's declarations under the Convention and Protocol. Without them
  the Art 39 categories, the Art 54 remedy restrictions and the Art XXX elections that
  switch on Arts X, XI, XII and XIII are unknown.
- Registry machinery, assignments, Art 13 interim relief and jurisdiction are not
  encoded.
- Time is entered as plain day numbers. There is no calendar, no working-day count
  and no timing within a day for registrations.
- No case law (for example on s 4 or Art XI) was searched.
