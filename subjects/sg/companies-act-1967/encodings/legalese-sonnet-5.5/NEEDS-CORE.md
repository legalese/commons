# NEEDS-CORE (all parts)

Status: **proposed, not landed.** Nothing below is in `sg-core.l4`. Each part that found the core lacking a type, a constructor or a function declared what it needed under its own provision label in its own module, so every module compiles as it stands; this file gathers the requests so that one person can settle them once.
Taking a request into the core would mean editing the part modules that carry the local copy and running the gate again; the merge did not do that.
Each section is the part's own `NEEDS-CORE.md`, unchanged; the same text is under `notes/<part>-NEEDS-CORE.md`.

## sga3

Written 2026-11-18. One request: the keel counts "N units after a day" (convention P1: the day of the event is not counted) and has no function for a period "beginning with" or "ending with" a named day, where the day named is day 1.
The text uses that wording in 16 rules of this range (see fork F-P1 in NOTES.md for the list): "the 6 months beginning with the day on which that contravention occurs" (s 76I(3)), "15 days ending with the date of the meeting" (s 76D(7)(a), s 76DA(4)(a)), "the period of 20 days ending with the resolution date" and "of 30 days" (s 78B(3), s 78C(3)), "the 6 weeks beginning with the resolution date" (ss 78B(4)(b), 78C(4)(b), 78D(2), 78E), "15 days beginning with the date" (s 78C(3)(c), s 78E, s 78F(4)) and "90 days beginning with the date the order is made" (s 78I(3)).

## What this part does now

It calls the keel's `period: the last day of a period after` and `period: the latest day for an act a period before` with the count less one, so the named day is day 1:
- "N days beginning with D": the last day is D plus (N minus 1) days.
- "N days ending with D": the first day is D minus (N minus 1) days.
- "N weeks": the same, in days (7 a week).
- "N months beginning with D": the keel steps D forward N months, which clamps to the last day of a short month (convention P4). The period ends the day before the same date N months on. When the step clamped (D is the 29th, 30th or 31st and the later month is shorter), subtracting one day from the clamped date is wrong by a day. The code tests the round trip: it steps the clamped date back N months and, if that returns D, takes the clamped date less one day, otherwise the clamped date itself. The tests: 15 January 2026 gives 14 July 2026; 31 August 2026 gives 28 February 2027; 31 December 2026 gives 30 June 2027; 28 February 2026 gives 27 August 2026 (`sga3-tests-76h-76k.l4`, the `s 76I(3)` assertions).

This is written out in `sga3-76h-76k.l4` for months, and as plain day counts elsewhere, so a reviewer finds it in each rule and a part that gets the keel function can drop its copy.

## What is asked

Two functions in `sg-periods.l4`, with the same arguments as the existing ones:
- `period: the last day of a period beginning with` (a day, a count, a unit): the last day of the period whose first day is the day given; counts the day given as day 1; for months, the round-trip rule above.
- `period: the first day of a period ending with` (a day, a count, a unit): the first day of the period whose last day is the day given.
Each with the convention recorded as a new P-line (P10) and a fork line in the keel's NOTES.md, because the Act does not say how a period "beginning with" a day is counted and the Interpretation Act 1965 is not among the sources.

## Why it matters

A part that counts "6 months beginning with the 31st" by "plus 6 months, minus 1 day" is wrong by a day in every month that is shorter than the start month, and no assertion on an ordinary date shows it (finding 1 in NOTES.md).
No type, constructor or other function is lacking.

## sgd

The core's `Party` (`sg-core.l4`, line 26) cannot be extended from another module, so this part declared small types of its own under its `s ...` prefix and uses them.
Each item below says what is wanted, what this part has instead, and where it is used, so that the lead can hoist it and this part can drop its own.

1. **A `Party` constructor `Official Receiver`, with no name.**
   The Official Receiver is an office of the State, like `Registrar` and `Court`, which the core already carries without a name.
   Instead: ``DECLARE `s 210(10B) party` IS ONE OF `s 210(10B) the Official Receiver` `` in `sgd-compromise.l4`.
   Used by the six rules `s 210(10B)(a)`, `s 210(10B)(b)` (`sgd-compromise.l4`), `s 215(7)(a)`, `s 215(7)(b)` (`sgd-acquisition.l4`), `s 215K(2)(a)` and `s 215K(2)(b)` (`sgd-amalgamation.l4`).

2. **A `Party` constructor `Board of directors`, `HAS` the name of the company.**
   Several provisions put a duty on "the board of directors of each amalgamating company" as a body, distinct from "a director" (which is the core's `Director`).
   Instead: ``DECLARE `s 215C party` IS ONE OF `s 215C the board of directors of an amalgamating company` HAS `s 215C the name of the amalgamating company` IS A STRING`` in `sgd-amalgamation.l4`.
   Used by the seven rules `s 215C(2)(a)`, `s 215C(2)(b)`, `s 215C(2)(c)`, `s 215C(4)`, `s 215D(5)`, `s 215I(4)(a)` and `s 215J(3)(a)`.

3. **A record `Penalty` for an offence provision's penalty**, so that every part's penalty functions share one shape.
   Instead: ``DECLARE `s 210(9) penalty` HAS`` four fields, in `sgd-compromise.l4`: the highest fine in Singapore dollars, the longest imprisonment in months, whether the text allows both the fine and the imprisonment, and whether the person is also liable to a default penalty.
   Used by the five functions `the most the person may be sentenced to on conviction` of ss 210(9), 211(5), 212(3), 215I(6) and 215J(5).
   The default-penalty flag is a flag only: its amount is not encoded (PLAN section 4 gives `s 4(1) "default penalty"` to a later wave).
   Sections 215C(6) and 215D(7) state no penalty (finding 6 in `NOTES.md`), so they do not use it.

## sge

One item: a `Party` constructor for a body that is not yet a company.
Rules before registration (s 357(1), s 358(1)) bind a foreign corporate entity: a body corporate incorporated outside Singapore that intends to be registered.
The core's `Party` has `Individual`, `Company`, `Director`, `Officer`, `Secretary`, `Member`, `Creditor`, `Auditor`, `Registrar`, `Minister`, `Court` and `Authority`, and none of them fits a body that becomes a company only on the date of registration (s 361(1)(a)).
`sge-p10a-357-358.l4` therefore declares a small type of its own, `s 357 party`, with one constructor `s 357 the foreign corporate entity` carrying the entity's name, and uses it for the two rules of ss 357(1) and 358(1).
Wanted constructor: `ForeignCorporateEntity HAS `the name of the foreign corporate entity` IS A STRING` (a body corporate incorporated outside Singapore), so that those two rules can use the core's `Party`.
After registration the rules use the core's `Company`, `Registrar`, `Individual` and `Officer` as they are.

Not a missing type but a keel question, recorded in NOTES.md finding 4: the keel's `s 4(1) "private company"` has three limbs (lines 1622 to 1631 of the text) and none for a company registered by transfer, which s 359(3)(c) ("where applicable, a private company") would need; this encoding takes the fact as an input.

## sgg

What the keel's core (`sg-core.l4`) lacks for Division 2 of Part 11 (foreign companies), and what this part declares in its place.

## The party type has no foreign company and no authorised representative

`Party` in `sg-core.l4` has twelve constructors: `Individual`, `Company`, `Director`, `Officer`, `Secretary`, `Member`, `Creditor`, `Auditor`, `Registrar`, `Minister`, `Court`, `Authority`.
Its own comment on `Company` is "a company incorporated under the Act", which a foreign company is not, and none of the twelve is an authorised representative of a foreign company.
Division 2 has 32 regulative rules, and their bearers are:

- the foreign company, in 25 rules (ss 368(1), 370(1), 370(4), 370(6)(a), 370(7), 372(1), 372(4), 373(6), 373(7), 374, 375(1)(b), 375(1)(c), 375(3), 377(1), 378(5) twice, 379(1)(a), 379(1)(b), 379(2)(a), 379(2)(b), 379(3), 380(2)(a), 380(2)(b), 380(2)(c) and 380(4));
- a director of the foreign company, in 1 rule (s 368A(1));
- an authorised representative of the foreign company, in 4 rules (ss 368A(2), 377(2)(a), 377(2)(b) and 377(2) for the notice of a liquidator's appointment);
- a director or an authorised representative, in 2 rules that take the party as an input (ss 368A(4) and 372(1A)).

This part declares its own types in `sgg-scope.l4`:

- `s 365 party`, four constructors: `s 365 the foreign company`, `s 365 a director of the foreign company`, `s 365 an authorised representative of the foreign company`, `s 365 an officer of the foreign company`, each with a name field.
- `s 365 role`, five constructors, used by the offence functions to say who the person is: `s 365 role: the foreign company`, `s 365 role: a director of the foreign company, or an equivalent person`, `s 365 role: an authorised representative of the foreign company`, `s 365 role: an officer of the foreign company`, `s 365 role: someone else`.
  "Or an equivalent person" is in the constructor because ss 373(18) and (18A) name "every director or equivalent person".

## What would let the part drop its own types

Proposed, not landed: a core `Party` constructor for a foreign company, one for an authorised representative of a foreign company, and a core role type for offence provisions.
With those, `s 365 party` and `s 365 role` would be replaced by the core names, and the regulative rules above would change their party type only; no rule's conditions, which come from the text, would change.

## Why this part did not edit the core

The keel's modules are read-only to a part agent, and the parts are written in separate sandboxes, so a type declared in this part cannot be seen by another part.
A part that needs the same people would have to declare its own, which is the reason to settle the constructors once in the core.

Parts with no request: sga1, sga2, sgb1, sgb2, sgc1, sgc2, sgf.

## Wave 2 (added at the wave-2 merge)

Status: **proposed, not landed.** The parts of wave 2 used the hoisted core (the keel's `Party`, `Penalty` and period functions above). A part that still found the core lacking something declared what it needed under its own provision label in its own module, so every module compiles as it stands; the requests are the part's own `NEEDS-CORE.md`, unchanged, and the same text is under `notes/<part>-NEEDS-CORE.md`.

### sgk

What my ranges (Part 4 Division 8, Parts 8, 8A and 9 of the Companies Act 1967) needed from `sg-core.l4` and did not find.
Nothing in `sg-core.l4` was edited; each item below was met by declaring a type or constructor under my own label (`s 231 party`, `s 231 act`), so the files work as they stand and the lead can hoist the constructors at the merge.
The core's `Party` was read on 2026-11-18; the names it has are Individual, Company, Director, Officer, Secretary, Member, Creditor, Auditor, Registrar, Minister, Court, Authority, `Official Receiver`, `Board of directors`, `Foreign corporate entity`, `Foreign company` and `Authorised representative`.

#### 1. An Inspector constructor in `Party` (wanted)

Part 9 has an inspector appointed by the Minister to investigate a company's affairs (ss 231 to 239, 243, 246).
The inspector is the bearer of three regulative rules of mine: `s 233(1) the inspector must report to the Minister on the conclusion of the investigation`, `s 236(1) the inspector must report on the affairs of the related corporation` and `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents`.
The core has the Registrar, the Minister and the Court as constructors with no name field, and glosses `Official Receiver` as "an office of the State; carries no name"; an inspector is the same kind of office.
Wanted: `Inspector` (no name), documented as "an inspector appointed by the Minister under Part 9 (ss 231, 232, 243), or whose powers s 246 extends to Singapore".
Met by: the constructor `s 231 an inspector appointed under Part 9` of `s 231 party` in `sgk-part9-declared.l4`.

#### 2. An "officer or agent" constructor in `Party` (wanted)

Part 9 puts duties on "every officer and agent of a corporation": two regulative rules of mine have that party (`s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` and `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`), and s 239(2) is a decision function about the same person; s 229 defines the phrase to include a director, banker, solicitor or auditor, a former one, a person employed or appointed, a person who has the corporation's property, owes it money or can give information about it, and a person reasonably suspected of being one.
The core's `Officer` is glossed "an officer of a corporation (a director, the secretary, an executive)", which is narrower, and has no agent.
Wanted: `Officer or agent` with `the name of the officer or agent` (a STRING), glossed with s 229.
Met by: the constructor `s 231 an officer or agent of a corporation` of `s 231 party`.

#### 3. Why my own party type repeats Company, Foreign company and Individual

A regulative rule has one `Party` type in its `DEONTIC` result, and the rules of Part 9 mix the Minister, inspectors, officers or agents, ordinary persons, companies and foreign companies, so `s 231 party` also carries `s 231 a person`, `s 231 a company` and `s 231 a foreign company`.
These repeat the core's Individual, Company and `Foreign company`; with items 1 and 2 hoisted into the core, `s 231 party` and `s 231 act` can be dropped from `sgk-part9-declared.l4` and the Part 9 rules re-pointed at the core's `Party`.
The Division 8 modules already use the core's `Party` (Company, Individual, Registrar) and need nothing.
The act type `s 231 act` is mine and stays: each rule's act is specific to its provision.

#### 4. Not wanted in the core, noted for the lead

- A committee of an approved exchange, or a body, panel or committee advising the Minister (s 244(5), (6)): no regulative rule of mine has one as its party (the duty in s 244(6) is a decision function over facts, `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244`), so no constructor is requested.
- The Public Prosecutor (s 245(5)): asked as a fact (`the Public Prosecutor has consented to the prosecution`), not a party.
- A role type for offence provisions: PLAN.md section 3A notes that one was proposed by a wave-1 part and is not in the core; I did not need one, and each offence function takes the person's facts and the fact that the person is not the company.

Wave-2 parts with no request: sgh, sgi, sgj, sgl, sgm, sgn, sgo.
