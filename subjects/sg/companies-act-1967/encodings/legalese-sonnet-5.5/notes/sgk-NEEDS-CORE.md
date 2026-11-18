# NEEDS-CORE (sgk)

What my ranges (Part 4 Division 8, Parts 8, 8A and 9 of the Companies Act 1967) needed from `sg-core.l4` and did not find.
Nothing in `sg-core.l4` was edited; each item below was met by declaring a type or constructor under my own label (`s 231 party`, `s 231 act`), so the files work as they stand and the lead can hoist the constructors at the merge.
The core's `Party` was read on 2026-11-18; the names it has are Individual, Company, Director, Officer, Secretary, Member, Creditor, Auditor, Registrar, Minister, Court, Authority, `Official Receiver`, `Board of directors`, `Foreign corporate entity`, `Foreign company` and `Authorised representative`.

## 1. An Inspector constructor in `Party` (wanted)

Part 9 has an inspector appointed by the Minister to investigate a company's affairs (ss 231 to 239, 243, 246).
The inspector is the bearer of three regulative rules of mine: `s 233(1) the inspector must report to the Minister on the conclusion of the investigation`, `s 236(1) the inspector must report on the affairs of the related corporation` and `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents`.
The core has the Registrar, the Minister and the Court as constructors with no name field, and glosses `Official Receiver` as "an office of the State; carries no name"; an inspector is the same kind of office.
Wanted: `Inspector` (no name), documented as "an inspector appointed by the Minister under Part 9 (ss 231, 232, 243), or whose powers s 246 extends to Singapore".
Met by: the constructor `s 231 an inspector appointed under Part 9` of `s 231 party` in `sgk-part9-declared.l4`.

## 2. An "officer or agent" constructor in `Party` (wanted)

Part 9 puts duties on "every officer and agent of a corporation": two regulative rules of mine have that party (`s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` and `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`), and s 239(2) is a decision function about the same person; s 229 defines the phrase to include a director, banker, solicitor or auditor, a former one, a person employed or appointed, a person who has the corporation's property, owes it money or can give information about it, and a person reasonably suspected of being one.
The core's `Officer` is glossed "an officer of a corporation (a director, the secretary, an executive)", which is narrower, and has no agent.
Wanted: `Officer or agent` with `the name of the officer or agent` (a STRING), glossed with s 229.
Met by: the constructor `s 231 an officer or agent of a corporation` of `s 231 party`.

## 3. Why my own party type repeats Company, Foreign company and Individual

A regulative rule has one `Party` type in its `DEONTIC` result, and the rules of Part 9 mix the Minister, inspectors, officers or agents, ordinary persons, companies and foreign companies, so `s 231 party` also carries `s 231 a person`, `s 231 a company` and `s 231 a foreign company`.
These repeat the core's Individual, Company and `Foreign company`; with items 1 and 2 hoisted into the core, `s 231 party` and `s 231 act` can be dropped from `sgk-part9-declared.l4` and the Part 9 rules re-pointed at the core's `Party`.
The Division 8 modules already use the core's `Party` (Company, Individual, Registrar) and need nothing.
The act type `s 231 act` is mine and stays: each rule's act is specific to its provision.

## 4. Not wanted in the core, noted for the lead

- A committee of an approved exchange, or a body, panel or committee advising the Minister (s 244(5), (6)): no regulative rule of mine has one as its party (the duty in s 244(6) is a decision function over facts, `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244`), so no constructor is requested.
- The Public Prosecutor (s 245(5)): asked as a fact (`the Public Prosecutor has consented to the prosecution`), not a party.
- A role type for offence provisions: PLAN.md section 3A notes that one was proposed by a wave-1 part and is not in the core; I did not need one, and each offence function takes the person's facts and the fact that the person is not the company.
