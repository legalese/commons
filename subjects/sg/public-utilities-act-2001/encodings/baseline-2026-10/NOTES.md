# Public Utilities Act 2001 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design defaults
ruled on 2026-10-18. No `REFUSE`: where the encoding does not cover a case it returns
`NOTHING` and says why in a comment. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 29 May 2026
(amendments to Act 8 of 2026 shown), as deposited at
`../../registers/source-bundle/PUA2001.txt`.

**Checks:** two modules (`pua-my-supply.l4`, `pua-offences.l4`) and two case files, run with
the stable `l4` of VS Code extension 1.6.98: `pua-cases-my-supply.l4` 28 assertions,
`pua-cases-offences.l4` 32; 60 satisfied, 0 errors, 0 warnings. The case files are generated
by `gen_public-utilities-act-2001_baseline.py` (scratchpad) with expected values written by
hand from the text.

This encoding replaces the one moved to solutions on 2026-10-19 and the first-pass encoding
`naive-2026-10`. The first pass was read for scope and pitfalls, and everything it covered is
covered here: Part 5 penalties, the due-diligence defence and s 56A, s 45A, ss 40G and 40H,
s 57, ss 44E and 44J, s 59, s 25 and s 68B. Its hand-checked values were re-read against the
text and kept where still right (the 300 mm tier, the s 50(6) split, the 7-day and 14-day
windows, the composition sums). With 60 assertions against its 92, it tests fewer cases of
each.

## Seat

**The consumer.** In s 2 that is "a person who is supplied with water or whose premises are
for the time being connected for the purpose of a supply of water". In practice it is the
owner or occupier of premises the Board supplies. The same person is the one the Part 5
offences are applied to when they dig near, connect to, draw from or work on the water
system. Most of the Act gives the Public Utilities Board its powers: to supply, to cut off, to
enter, to recover. Read from the consumer's side, each power becomes a question: `May the
Board cut off my supply`, `How much notice must I be given before the Board enters my
premises`, `What can I recover from the Board`, `May a warrant issue to seize and sell my
goods`, `Can I get my overpayment refunded`, `What is the most I can be fined`, `May I engage
this person for the work`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers brought in.** Followed. No
  instrument is deposited: no tariff, waterborne-tax or water-conservation-tax order, no
  late-payment charge, no regulations naming who is "responsible" for maintenance and tank
  security (ss 45(8), 45A(7)), no list of compoundable offences (s 59(2)), and no order
  excluding works from "regulated works". The amounts are left out and the encoding says so.
  The rest are asked as facts (`I am the person responsible for the security of the
  installation`, `the offence is prescribed as compoundable`).
- **The actors the text names.** Followed: the Board, the consumer, the owner, the
  occupier, the licensed plumber, the professional engineer, the authorised officer, the
  Minister, the court.
- **A judgment handed to someone else answered conditionally.** Followed. The Board's
  opinion that I am responsible for misuse or waste (s 23(2)), its view that immediate action
  is necessary (s 24B), its satisfaction that there was an overpayment (s 68B(3)(c)) and the
  Minister's declaration under s 24(3) are inputs. Where the Act gives the Board a power
  ("may"), the answer says the Board *may* act ("the Board may cut off my supply, if it
  thinks fit"), never that it will.
- **The Act's own definitions worked out, borrowed terms asked as facts.** Followed:
  "consumer", "occupier" (with its lodger exception), "storage tank" (with its flushing-cistern
  exception), "limited WSI design works", "regulated works" and "5% controller" are worked out
  from facts. "Lodger", "professional engineer" (Professional Engineers Act 1991), "licensed
  plumber" and "master meter" are asked as facts.
- **One case is the text's natural unit.** Followed: one premises' supply, one entry, one
  unpaid bill, one offence, one storage tank, one engagement, one excavation.
- **The Act's own terms, each with a plain gloss.** Followed in comments that quote the
  statutory words above each `§§`. Enum constructors carry the section they come from.
- **Operative sections in scope, machinery out.** Followed: the Board's constitution and
  finances, Parts 6 and 7, and regulation-making powers are out. **Two departures:**
  - ss 44A, 44E and 44J (notice by a 5% controller of a designated water entity) are kept,
    though they reach the consumer only as an investor. The first pass covered them, and this
    encoding replaces it.
  - In `What is the most I can be asked to pay to compound the offence`, `NOTHING` means the
    Act offers no composition for that offence, not "not covered". That is a true answer, and
    the comment says so. In `What can I recover from the Board` it keeps its usual meaning:
    s 24A(2) sends compensation for the Board's temporary occupation to Part 3A, which is not
    encoded.

## Why this scope

These are the provisions a household or small-business consumer meets:

- whether they are a consumer and the occupier (s 2);
- when the supply can be cut off and what brings it back (ss 21(3), 22(3), 23, 34(2), 37(2));
- the Board's people at the door (ss 24, 24A, 24B, 31, 32, 55B);
- what can be claimed when the supply fails or works affect them (ss 21(5), 22(4), 23(3),
  24A(7), 27(2), 28, 38(2));
- the unpaid bill (s 25) and the refund (s 68B);
- the occupier's own duties (ss 34, 37(1));
- the offences they can commit and what each costs (Part 5, ss 26, 33, 39, 40G, 40H, 41, 55,
  58);
- the defences (ss 47(2), 47A(3), 50(6), 56A);
- their storage tank (s 45A);
- whom they may engage for plumbing (ss 40G, 40H);
- digging (s 57) and composition (s 59).

Left out:

- tariffs and taxes (ss 20, 20A), whose amounts are set by orders that are not deposited;
- the late-payment charge (s 35), relocation approvals (s 26 beyond its offence), obstruction
  notices (s 33 beyond its offence) and capital contributions (s 36);
- Part 3A compensation and owner-initiated acquisition;
- plumber licensing procedure and the duties of plumbers and engineers (ss 40I to 40Q);
- approved suppliers' conditions (ss 41(3) to 44);
- the 12%, 30% and indirect controller approvals and special administration (ss 44F to 44M);
- the evidential presumptions in s 50(3) to (5);
- s 56 (company officers) and s 68A procedure.

## What the Act turns out to say

1. **The Board answers for almost nothing when the water stops.** s 27(2) excludes liability
   for "any failure, interruption, suspension or restriction of any supply of water". ss
   21(5), 22(4) and 23(3) exclude it for a refusal or cut-off. Entry for surveys and pipe
   checks costs the Board nothing (ss 24(1), 31(3)). There are three exceptions: a
   proportionate abatement of the bill when the Board reduces supply because water is short
   (s 28), "reasonable compensation" when its works interrupt ways or drains (s 38(2)), and the
   consumer's costs of complying with a s 24A(5) or (6) notice (s 24A(7)). Asserted for
   interruption, abatement and the Part 3A gap.
2. **The notice before entry depends on why the Board comes.** To survey or inspect an
   occupied dwelling it needs consent or 6 hours' notice (s 24(2)). To lay pipes or meters it
   needs 14 days' written notice (s 24A(3)). To use land within 100 metres of its works it
   needs 7 days (s 32(2)). In an emergency it needs none, despite those sections (s 24B), and
   an authorised officer investigating needs none (s 55B). Asserted.
3. **A cut-off needs a ground, and then is still the Board's choice.** The grounds are
   premises built unlawfully, ruinous, or with an unsatisfactory installation; security not
   given within 7 days of a notice; default in paying; misuse or waste continuing past a
   notice; or a wasting pipe left unreported. Each is a "may". To get the supply back the
   consumer must both make good the default and pay the expenses of disconnecting and
   reconnecting (s 37(2)). Day 7 after service is taken as in time, which is an inference.
   Asserted.
4. **An unpaid bill can end in a daytime break-in and an auction.** Seven days after a
   demand notice a warrant may issue for seizure and sale (s 25(2)). The holder "may break open
   in the daytime any house or building" (s 25(3)). Goods are auctioned after 7 days from
   seizure unless the debt is paid (s 25(6)). A surplus unclaimed for 12 months from the sale
   is lost (s 25(8)). The day of the notice is not counted, which is an inference. Asserted,
   except the break-in, which is read but not asserted.
5. **The occupier answers for a reconnected supply unless they prove otherwise.** Where a
   cut-off supply is found reinstated and in use, the occupier "is deemed, until the contrary
   is proved, to have authorised such user" (s 37(1)): $10,000 and $250 a day, with no
   imprisonment. A lodger is not an occupier (s 2). Asserted.
6. **Refunds are barred except as s 68B allows.** A claim must be made "within 5 years
   starting on the date" of the overpayment, in the Board's form, and the Board must be
   satisfied. The fifth anniversary is taken as the first day out of time, and 29 February is
   taken to fall on 1 March in a common year; both are inferences. Asserted.
7. **Damaging a big water main is five times the fine and twelve times the term.** s 47A(1):
   $40,000 or 3 months, but $200,000 or 3 years if the main "is 300 mm or more in diameter",
   "whether wilfully or otherwise". 299 mm and 300 mm fall on opposite sides. Asserted.
8. **The due-diligence defence is not for the employer, and not for every offence.**
   ss 47(2) and 47A(3) give it "but this defence is not available to any person who may be
   liable by virtue of section 56A". s 50(6) gives it for s 50(1), (2)(b) and (2)(d), so
   meter tampering has it and meter interference (s 50(2)(c)) does not. Under s 56A the
   employer escapes only by proving both no consent or connivance and no neglect. Asserted.
9. **Supplying drinking water without approval carries the longest term.** s 41(2) allows 5
   years. Four offences carry a fine only: s 26(6) $20,000, s 34(2) $5,000, s 37(1) $10,000
   and s 55(3) $5,000. Offences with no penalty of their own fall to s 58: $10,000 or 12
   months and $250 a day. Asserted for those named in the case file.
10. **A house tank on its own meter needs only the general security duty.** s 45A(3) lifts
    the locking, checking, records and reporting duties from residential premises that do not
    take their supply through a master meter. A condominium behind a master meter keeps them
    all. A flushing cistern is not a "storage tank" (s 2), and NEWater tanks are outside
    s 45A. Asserted.
11. **A pump or a tank in the design takes it away from the plumber.** "Limited WSI design
    works" (s 2) has neither, and a licensed plumber or a professional engineer may do it
    (s 40G(6), (9)). With a pump or tank, the owner may engage "only" a professional engineer
    (s 40H). A professional engineer who is not a plumber may not do sanitary works.
    Asserted.
12. **Before digging, all three steps.** s 57(1) requires the Board's plans, trial trenches
    and the Board's other requirements, all done "first". Missing any one is an offence
    carrying $50,000 or 3 years. Asserted.
13. **The 5% notice binds only those who crossed on or after 1 April 2020.** The notice is
    due within 7 days. There are two defences: unawareness with notice within 14 days of
    learning of it, or an associate's increase with no arrangement and notice within 7 days.
    An individual faces $500,000 or 3 years (s 44J). Asserted.
14. **Composition is $10,000 for tank offences and $3,000 for prescribed ones.** Under s 59(1),
    no other offence can be compounded. Asserted.
15. **The deposit's arrangement of sections is displaced against its body** from about s 24
    on. For example, it prints "Recovery of moneys due to Board" against 24B. This encoding
    follows the body, as the cross-references in ss 47(2) and 47A(3) to "section 56A" do. Read,
    not asserted.

## What would need doing before this is worth anything

- A Singapore utilities-law reader should check every assertion against the text, especially
  the time computations in findings 3, 4 and 6, which rest on readings of "within 7 days
  from" and "within 5 years starting on" without the Interpretation Act.
- The tariff, waterborne-tax and water-conservation-tax orders, the late-payment charge, and
  the regulations under ss 45(8), 45A(7) and 59(2) should be fetched. Each would turn an input
  here into a computed answer.
- Part 3A compensation (ss 40A to 40F, Fourth Schedule) is the consumer's main money claim
  against the Board and is not encoded.
- The s 50(3) to (5) presumptions (a hole in the meter cover, a broken seal or cut AMI wires
  is prima facie evidence of tampering) bear directly on a consumer charged with meter
  offences and are not encoded.
- No cases or PUB guidance were searched.
