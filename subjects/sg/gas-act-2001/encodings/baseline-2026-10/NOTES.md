# Gas Act 2001 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the Act is applied, with the design defaults
ruled on 2026-10-18. No pipeline, no coverage table, no independent test pass, no human gate.
No `REFUSE`: where the encoding has no answer, a decision returns `NOTHING` and its comment
says why. Not for public use as advice.

This encoding replaces the first-pass encoding `naive-2026-10`. Its NOTES.md and L4 were read
for scope and pitfalls, and its hand-checked values were reused where they still held: the
s 13 reading, the 7-day and 24-hour earthworks rules, the 14-clear-day defence notice, the
s 47(4) presumption and the penalty figures. The L4 itself was written fresh. No encoding of
this Act was found among those moved to `solutions` on 2026-10-19 (the `solutions` working
copy was searched), so there was no moved encoding's NOTES.md to read.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 1 September
2025, with amendments up to Act 27 of 2024 shown, as deposited at
`../../registers/source-bundle/GA2001.txt`.

**Checks:** one module (`gas-consumer.l4`) and one case file (`gas-cases-consumer.l4`). The
case file is built by the scratchpad generator `gen_gas-act-2001_baseline.py`, with expected
values written by hand from the text. Result: 59 assertions satisfied, 0 errors, 0 warnings,
on the stable `l4` from VS Code extension 1.6.98. The module on its own also runs with no
errors or warnings.

To show the check can fail, a copy was run with one expected value changed (the s 47 fine on
$2,000 of gas, from 56000 to 55999). It gave 58 satisfied and 1 error.

## Seat

**The gas consumer: the owner or occupier of premises supplied with piped gas.** With them
come the members of the public whom the Act's prohibitions reach in the same everyday way: a
person who engages a gas fitter, digs near a gas pipe, builds over one or handles a meter.

Most of the Act is addressed to gas licensees and the Authority. A householder or small
business meets it when they get connected, pay or fail to pay, have the meter read or the
supply cut off, hire someone to work on the installation, or renovate near a pipe. The
licensees' duties come in only as what the consumer is owed (a connection, a repair, notice
before entry) and what may be done to them (a charge, a cut-off, an entry).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed, but no
  regulations, Gazette orders or exemptions were deposited. So these are asked as facts:
  - whether the Minister's date under s 6(1)(c), (d), (g) has passed;
  - whether a s 8 exemption applies;
  - whether a gas service worker licence covers the class of work (s 12(5));
  - whether an offence is prescribed as compoundable (s 92(2)).

  The penalty for an offence created by regulations is answered `NOTHING`.
- **The actors the text names.** Followed: the gas transporter, gas shipper, gas retailer
  (and "relevant" retailer), the Authority, the Minister, the prosecutor and the court.
- **Someone else's judgment answered conditionally.** Followed. These are inputs:
  - the transporter being "satisfied" a relocation is reasonable (s 30(2));
  - "circumstances beyond its control" and "danger to the public" (s 22(4));
  - "reasonable cause to believe" earthworks are needed for safety (s 32(5));
  - the court's permission (s 32(9));
  - whether an amount is "genuinely in dispute" (s 46(5)).
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.**
  Followed. "gas" (which leaves out LPG) and "consumer" are worked out. "Licensed gas service
  worker" is worked out, including the s 12(6) deeming. "Professional engineer with a
  practising certificate" (Professional Engineers Act 1991) is asked. "Earthworks" and "within
  the vicinity" are asked: the first has a long definition that a person can apply to their
  own work, and the second is not defined.
- **One case is the text's natural unit.** Followed: one supply, one activity, one worker, one
  connection request, one set of earthworks, one act of damage, one bill, one offence.
- **The Act's own terms, each with a plain gloss.** Followed, in comments beside each type and
  decision.
- **Operative sections in, machinery out.** Followed. Administration (ss 3 to 5), regulation
  making (s 96) and transitional provisions are out. **Departure:** some operative
  provisions are also out, because the consumer does not meet them or to stay within size:
  - licence grant, conditions and enforcement (ss 7 to 10, Part 4);
  - the foreign onshore-facility principal (s 6(3), (4)), which the first-pass encoding had.
    No individual meets it;
  - network duties, works and prices (ss 21, 24 to 28);
  - the Gazette-prescribed inspection responsibility (s 29(3) to (6));
  - the transporter's escape duties (ss 65, 66);
  - Parts 7 to 10.

## Why this scope

The seat decides it. The encoding takes the questions a gas consumer asks, roughly in the
order they meet them:

1. Is my gas covered at all, and am I a "consumer" (s 2)?
2. Do I need a licence to pass gas on to my tenants (s 6)?
3. Who may work on my gas installation, and do I commit an offence by hiring them (ss 11 to 13)?
4. Must the transporter connect me, and what can I be charged (ss 22, 23)?
5. Who pays to repair, move, remove or divert the pipes on my land (ss 29 to 31)?
6. May I dig near a pipe, and what happens if I damage one (ss 32, 32A, 32B)?
7. Must I report a damaged pipe, and who keeps my meter in order (ss 39, 44)?
8. Can my retailer cut me off for an unpaid bill (s 46)?
9. Will I be presumed to have tampered with the meter? May I reconnect myself, or connect a
   meter myself (ss 47, 49, 50)?
10. What gets my supply back (s 52)?
11. How much notice must I get before they come in (ss 53 to 60)?
12. What are the safety rules (s 64)?
13. Am I liable for my company's offence (s 89)?
14. What is the most I can be fined, or asked to pay to compound (ss 6, 31, 32, 32A, 32B, 47,
    49, 50, 61(4), 64, 91, 92)?

The s 32(6) duty is also written as a regulative rule, `my duty to notify after safety
earthworks` (written notice within 24 hours). It checks, but it is not traced.

## What the Act turns out to say

1. **Bottled LPG is not "gas" under this Act.** s 2: "gas" means natural gas and town gas,
   "but does not include liquefied petroleum gas". A kitchen on a gas cylinder is outside the
   Act. Asserted.

2. **A landlord may pass retailed gas on to tenants without a licence.** s 6(2)(b) allows
   selling gas, for use in premises the person has an interest in, that a gas retailer
   retailed for use there. Retailing as such needs a licence only from a date the Minister
   gazettes (s 6(1)(d)). That date was not deposited. Asserted.

3. **Hiring a professional engineer for gas work is an offence on the words of s 13.** s 11(1)
   lets a registered professional engineer with a practising certificate do gas service work
   without a gas service worker licence. But s 13 makes it an offence to engage "any person
   who is not a licensed gas service worker", with no matching carve-out.

   The other way round, a fitter licensed only for another class may not do the work
   (s 11(1)), yet engaging them is not a s 13 offence, because they are "a licensed gas
   service worker". This is the literal reading, carried over from the first-pass encoding;
   no case law was searched. Asserted.

4. **The connection charge is capped at what has not already been recovered from someone
   else.** s 22(2). The transporter need not connect where it cannot for reasons beyond its
   control or it would endanger the public (s 22(4)). Where a new or enlarged main is needed,
   it may wait until I agree to pay a reasonable amount (s 22(5)). It may also refuse while
   security it asked for is not given (s 23). Asserted.

5. **I pay for repairs to my service pipe only if I caused the damage and the transporter asks
   me to.** s 29(2)(a) requires both: my "intentional or negligent act" and the transporter
   requiring payment. Otherwise the transporter pays. Asserted.

6. **A gas service pipe must be moved on request, a gas main need not be.** s 30(2) obliges
   the transporter to relocate "the gas service pipe" only. I may ask about a gas main under
   (1), but nothing obliges the transporter to move it. A disused main or pipe must be removed
   at the transporter's expense at the owner's reasonable request. A leaseholder with at least
   7 years unexpired counts as an owner (s 30(3), (4)). Asserted.

7. **Building over a pipe without approval is an offence, and the owner then pays for the
   diversion.** s 31(1), (3)(a), (4). Where the owner did not build it, they still pay to the
   extent they benefit from the diversion. Asserted.

8. **Seven days' notice before digging, and the duties do not stop once work starts.** s 32(1)
   requires all three: notice, the pipe's location, and consultation. s 32(7) also punishes
   breach of the duties while working: the transporter's reasonable requirements, reasonable
   precautions and access (s 32(3)). It also punishes notice given more than 24 hours after
   safety works began (s 32(6)). The first-pass encoding did not reach s 32(3).

   Where the due diligence defence rests on information from the transporter, it is lost
   without the court's permission unless the prosecutor was told the source 14 clear days
   before the hearing (s 32(9)). The maximum is $100,000 or 5 years. Asserted.

9. **Damaging a pipe on land is an offence without fault; damaging a submarine pipeline needs
   at least negligence but carries double.** s 32A(1)(a), (b) state no mental element, and
   the only answer is the s 32A(4) defence. Hindering without damaging needs wilfulness or
   recklessness (s 32A(1)(c)). s 32B reaches negligence, and even an act "likely to damage"
   a submarine pipeline, for up to $2 million. Asserted.

10. **An occupier who knows of damage to a pipe must report it immediately.** s 39(1). Failing
    to is an offence, punished under s 91, and the supply can be cut until it is repaired
    (s 39(2)). Asserted (the offence).

11. **A meter lent or hired to me is the company's to keep in order, free of charge.** s 44(3).
    A meter I own is mine to keep in order (s 44(4)). Asserted (the lent meter).

12. **Before a cut-off for an unpaid bill, I get 28 days after a written demand and then 7
    days' notice, and a genuine dispute stops it.** s 46(1), (3), (5). The same applies to a
    deposit not given within 7 days of a written request (s 46(2)). Asserted (the bill).

13. **A broken meter seal plus custody presumes tampering.** s 47(4) presumes it "until the
    contrary is proved". The fine is up to $50,000 plus 3 times the value of the gas, or 5
    years, plus $250 a day (s 47(2)). Asserted.

14. **Reconnecting myself is a crime.** s 49 makes it $10,000 or 3 years, where the supply was
    cut off under the Act or a valid contract. Connecting or disconnecting a meter needs 48
    hours' notice to the right company: my shipper or retailer if one supplies me, otherwise
    the transporter (s 50). Asserted.

15. **Getting supply back needs both the default made good and the expenses paid, or moving
    out.** s 52(2). It only removes the company's excuse; it does not say it must reconnect.
    Asserted.

16. **Entry to read the meter needs 14 days' notice; to cut me off, 7; for a gas escape,
    none.** ss 53, 55, 58, 59 set their own periods. ss 54 and 56 set none, so s 60(1)(a)'s
    "14 days' notice" applies. That is a reading; regulations could provide otherwise, and
    none were deposited. Asserted (escape and meter reading).

17. **No naked flame near a known leak, with no exception.** s 64(7). Connecting an
    installation needs every outlet sealed and a gas-tightness test (s 64(2)). Asserted (the
    leak).

18. **A director is guilty of the company's offence unless they prove both no consent and due
    diligence.** s 89. Asserted.

19. **Unlicensed gas business carries no prison term; most consumer offences carry 12 months.**
    s 6(6): up to $1 million plus $25,000 a day, and no imprisonment. Offences with no penalty
    of their own (ss 11, 13, 31, 39, 40 to 42) fall to s 91: $10,000 or 12 months, plus $250 a
    day. Composition is at most $3,000, for prescribed offences only (s 92). Asserted.

## What would need doing before this is worth anything

- The regulations under s 96 were not deposited, and neither were the Gazette orders under
  ss 6(1) and 29(3) or the s 8 exemptions. They set the classes of gas service work, the
  compoundable offences, meter rules, entry rules under s 61(5), and inspection
  responsibility for gas installations. A consumer's real obligations largely sit there.
- The s 13 reading, the "14 clear days" reading and the s 60(1)(a) default for ss 54 and 56
  are readings; no case law was searched.
- Whether s 32A also reaches a submarine pipeline (it covers any gas pipe in a licensee's
  network) was not resolved. The encoding treats the two sections apart.
- The independent test pass, the coverage table and the human gates were not done.
