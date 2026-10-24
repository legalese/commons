# Criminal Damage Act 1971 (1971 c. 48), England and Wales: the legalese-sonnet-5.5 encoding

Status: `draft`.
Review: `not_reviewed`. No domain expert has read this encoding against the text.

Method: a single Sonnet 5.5 agent working alone from `BRIEF.md`, with the stable `l4` 1.6.98 and the two L4 skills, with no ontology agent, fleet, integrator, independent test author or subagents.
The source is `ukpga-1971-48.txt`, a plain-text rendering made by a converter script from the legislation.gov.uk XML (version 2008-10-01).
It is not the official text and is not marked up; nothing here is "verified against the official text".
The text is the revised Act as at 2008-10-01; any later amendment is not in it and is not encoded.
`SOURCE-LICENSE.md` points at `../../SOURCE-LICENSE.md`.

## Seat

The seat is a person who may be accused of an offence under the Criminal Damage Act 1971 (the person suspected or charged), asking what the Act makes of what they did or are alleged to have done, and the most that can follow.
It is the seat the brief fixed, and it fits the Act: the Act is almost wholly a criminal statute, so the person to whom it is applied is the person it would punish.
The seat layer is `cda-seat.l4` (27 questions, each with `@export` and `@desc`, grouped under `§` headings in the order of the Act) and `cda-cases-seat.l4` (80 worked cases).
Every question builds the records the layer-1 modules expect from the person's own answers and calls the module's rule; no rule is restated and no layer-1 module changed to suit the seat.
The questions that ask a layer-1 rule about property take plain facts about the thing and the people connected with it.
The one choice the seat declares, `What the thing is`, only sorts a thing into physical kinds a witness could name (an ordinary thing, money, a tamed or captive creature, a wild creature in possession and so on); whether the thing is "property" is still worked out by s 10(1) in `cda-s10-interpretation.l4`.
Other persons' connections with the property are asked as "someone else": one set of answers is enough because the Act asks whether property belongs to any other person.
A field a rule never reads is given a fixed placeholder with a comment saying so (for example the accused's own connection with the property in the s 1(1) question).
Where section 5 does not apply to a limb (s 1(2), s 2(b), s 3(b)) only the recognised-lawful-excuse input is asked.
Provisions addressed to officials (s 6, s 7(2)) are asked only for what they mean to the person: what can be done to them and whether a rule of law protects them.
There is no seat for an official.

## Jural relations

Hohfeld's correlatives: a claim is matched by a duty, a privilege by a no-right, a power by a liability, an immunity by a disability.
The Act names no party that holds the claim to which each offence's duty corresponds; the holder is given as "the State (the prosecuting authority)" by analysis, and the table says so.

| Provision | Holder (right, privilege, power, immunity) | Bearer (duty, no-right, liability, disability) | Relation | L4 rule |
|---|---|---|---|---|
| s 1(1) | The State (by analysis; not named in the Act) | The person | Claim / duty not to destroy or damage property belonging to another, intending or reckless, without lawful excuse | `a person commits an offence under section 1(1)` |
| s 1(2) | The State (by analysis) | The person | Claim / duty not to destroy or damage any property, intending or reckless as to danger to life, without lawful excuse | `a person commits an offence under section 1(2)` |
| s 1(3) | none named | The charging authority | Duty to charge an offence under s 1 by fire as arson; the Act names no claim-holder | `an offence under section 1 must be charged as arson` |
| s 2 | The State (by analysis) | The person | Claim / duty not to make a threat, intending it to be feared, to destroy or damage property | `a person commits an offence under section 2` |
| s 3 | The State (by analysis) | The person | Claim / duty not to have anything in custody or control intending to use it to destroy or damage property | `a person commits an offence under section 3` |
| s 4 | The sentencing court (by analysis) | The person | Power / liability: the court may impose up to the ceiling on conviction on indictment | `the most that can follow` |
| s 5(2) | The person | The State (the prosecuting authority) | Immunity / disability: the person is treated as having a lawful excuse for the offences to which s 5 applies | `section 5(2) treats the accused as having a lawful excuse for` |
| s 5(5) | The person | The State | Saving: defences recognised by law keep their immunity | `5(5): a lawful excuse or defence recognised by law apart from section 5(2) is left in place` |
| s 5(1), (3), (4) | none | none | Scope, a counting rule and a definition | `section 5 applies to`, `a belief counts for the purposes of section 5`, `5(4): ...` |
| s 6(1) | A justice of the peace | The person with the thing in custody, control or premises | Power / liability: the justice may grant a warrant to search for and seize | `a justice of the peace may grant a warrant authorising any constable to search for and seize the thing` |
| s 6(2) | A constable authorised under s 6 | The person | Power / liability: entry by force and search of premises, and seizure | `the constable may enter the premises ...`, `the constable may seize the thing` |
| s 6(3) | none | none | Applies the Police (Property) Act 1897 to what the police take; the relation lies in that Act | `the law governing property that has come into the possession of the police under section 6` |
| s 7(2) | A magistrates' court | The person | Power / liability: no rule of law about a dispute of title takes away the court's power to try; the person has no immunity from trial on that ground | `the effect of a rule of law about a dispute of title on the jurisdiction of magistrates' courts` |
| s 9, first part | The party who asks, or the court that orders | The person (and the person's spouse or civil partner) | Claim / duty: the person must answer or comply although it may incriminate; the privilege against self-incrimination is withdrawn in those proceedings | `whether the person is excused from answering or complying` |
| s 9, second part | The person (and the spouse or civil partner, unless married after) | The court and the prosecution | Immunity / disability: the statement cannot be received against them | `the admissibility of the statement or admission` |
| s 10(1) to (5) | none | none | Definitions | `a thing is property within section 10(1)`, `property belongs to a person with this connection under section 10(2) to (4)`, `destruction or damage within the Act` |
| s 11(1) | The person | The State | Immunity / disability: the common law offence of arson no longer exists, so the person cannot be charged with it | `the status of the common law offence of arson` |
| s 11(9) | The Secretary of State | Local statutory provisions (and those subject to them) | Power / liability to amendment or repeal by order. Not encoded (inert) | none |
| s 11(11) | none | none | A saving: the old enactment keeps operating for earlier offences | `the effect of the repeal of an enactment about procedure or jurisdiction` |
| s 11(2) to (8), (10); s 12(1), (2), (3), (6); Schedule | none | none | Commencement, short title, extent, repeals and amendments of other enactments | `the Act is in force on`, `whether the provisions of sections 1 to 10 extend to` |

## What is encoded and what is not

Encoded (layer 1): the elements of the offences in ss 1 to 3 (conduct, circumstances, state of mind, "without lawful excuse"), the definitions in s 10, the deemed lawful excuses and the saving of other defences in s 5, the penalties in s 4 (ceilings on indictment), the consequences of ss 6, 7(2) and 9 for the person, the abolition of common law arson (s 11(1)), the saving for repealed procedural enactments (s 11(11)), the commencement date (s 12(1)) and the extent (s 12(3), (6)).
Not encoded: the short title, the amendments to other Acts (s 11(6), (7)), the repeals (s 11(8) and the Schedule), the Secretary of State's order-making power (s 11(9), (10)), and the content of other enactments the text refers to (the Police (Property) Act 1897, the Visiting Forces Act 1952, the Firearms Act 1968).
Not in the text and so not encoded: penalties on summary conviction, the meaning of "reckless", "intending", "knowing", "believed" and "reasonable" (the Act defines none), who may consent to damage, and anything about attempts, aiding and abetting or procedure for trial.
Each unit the text sets is one act or one set of facts per question; a charge with more than one act would be asked several times.

## Coverage table

Line numbers are lines of `ukpga-1971-48.txt`.
Dispositions: `encoded`, `inert` (with a reason), `repealed or blank in this text`, `not applicable`.

| Provision | Lines | Disposition | Where / reason |
|---|---|---|---|
| Title, chapter, long title, date of enactment | 1-4 | encoded | `cda-s11-s12-extent.l4`: the bracketed date `[14th July 1971]` is read as the day the Act was passed (rule `the day the Act was passed`); the long title is read by `whether the provisions of sections 1 to 10 extend to` (forks F7, F9). |
| s 1 heading | 5 | not applicable | A heading with no operative text; it is quoted with s 1(1) in `cda-s1-s3-offences.l4`. |
| s 1(1) | 6 | encoded | `cda-s1-s3-offences.l4`: `a person commits an offence under section 1(1)`. |
| s 1(2) | 7-10 | encoded | `cda-s1-s3-offences.l4`: `a person commits an offence under section 1(2)`. |
| s 1(3) | 11 | encoded | `cda-s1-s3-offences.l4`: `an offence under section 1 must be charged as arson`, `the offences committed under section 1`. |
| s 2 | 12-16 | encoded | `cda-s1-s3-offences.l4`: `a person commits an offence under section 2`, 2(a), 2(b). |
| s 3 | 17-21 | encoded | `cda-s1-s3-offences.l4`: `a person commits an offence under section 3`, 3(a), 3(b). |
| s 4(1) | 22-23 | encoded | `cda-s4-punishment.l4`: `section 4(1) applies to`. |
| s 4(2) | 24 | encoded | `cda-s4-punishment.l4`: `section 4(2) applies to`, `the ceiling in years in section 4(2)`, `the most that can follow`. |
| s 5(1) | 26 | encoded | `cda-s5-lawful-excuse.l4`: `section 5 applies to` (fork F2). |
| s 5(2) | 27-31 | encoded | `cda-s5-lawful-excuse.l4`: `section 5(2) treats the accused as having a lawful excuse for`, with limbs (a), (b), (b)(i), (b)(ii). |
| s 5(3) | 32 | encoded | `cda-s5-lawful-excuse.l4`: `a belief counts for the purposes of section 5`. |
| s 5(4) | 33 | encoded | `cda-s5-lawful-excuse.l4`: `5(4): the purpose was to protect a right or interest in property`. |
| s 5(5) | 34 | encoded | `cda-s5-lawful-excuse.l4`: `5(5): ... is left in place`, `the accused has a lawful excuse for` (fork F3). |
| s 6(1) | 36-39 | encoded | `cda-s6-s9-proceedings.l4`: `a justice of the peace may grant a warrant ...`; the justice's judgments are stated inputs (fork F12). Encoded for what it means to the person: what can be done to them. |
| s 6(2) | 40 | encoded | `cda-s6-s9-proceedings.l4`: `the constable may enter the premises ...`, `the constable may seize the thing`. |
| s 6(3) | 41 | encoded | `cda-s6-s9-proceedings.l4`: `the law governing property that has come into the possession of the police under section 6`. The Police (Property) Act 1897 itself is not an input and is not encoded. |
| s 7(1) | 43 | repealed or blank in this text | The text shows only dots (`(1) . . . .`): the subsection has been repealed. |
| s 7(2) | 44 | encoded | `cda-s6-s9-proceedings.l4`: `the effect of a rule of law about a dispute of title on the jurisdiction of magistrates' courts`. |
| s 8 | 45 | repealed or blank in this text | The text shows the section number followed only by dots: the section has been repealed. |
| s 9 | 46-50 | encoded | `cda-s6-s9-proceedings.l4`: `whether the person is excused from answering or complying` (first part) and `the admissibility of the statement or admission` (second part). |
| s 10(1) | 52-55 | encoded | `cda-s10-interpretation.l4`: `a thing is property within section 10(1)` and its (a) and (b) rules. |
| s 10(2) | 56-59 | encoded | `cda-s10-interpretation.l4`: `property belongs to a person with this connection under section 10(2) to (4)`. |
| s 10(3) | 60 | encoded | The same rule: the right to enforce a trust (field `a right to enforce a trust to which it is subject`). |
| s 10(4) | 61 | encoded | The same rule: the corporation sole, vacancy or not. |
| s 10(5) | 62 | encoded | `cda-s10-interpretation.l4`: `destruction or damage within the Act`. |
| s 11(1) | 64 | encoded | `cda-s11-s12-extent.l4`: `the status of the common law offence of arson`. |
| s 11(2) to (5) | 65-68 | repealed or blank in this text | The text shows only dots in each of the four subsections. |
| s 11(6) | 69 | inert | Amends the Visiting Forces Act 1952 by adding this Act to a list of offences against property in the case of which a member of a visiting force is in certain circumstances not liable to be tried by a United Kingdom court. The effect belongs to the 1952 Act, which is not an input, and it concerns visiting forces only, a status outside the seat. |
| s 11(7) | 70 | inert | Amends Schedule 1 to the Firearms Act 1968 so that offences under section 1 of this Act are among those to which the firearms provision in section 17(2) of that Act relates. The consequence belongs to the Firearms Act 1968, which is not an input, and nothing in this Act's text says what it is. |
| s 11(8) | 71 | inert | Repeals the enactments listed in the Schedule. Once in force the repeals leave no rule to apply to a person's conduct; the repealed enactments are not inputs. The repealed law is not modelled. |
| s 11(9) | 72-73 | inert | Gives the Secretary of State a power to amend or repeal local statutory provisions by order. A power over statutory text, not a rule about conduct; it decides nothing a person in the seat could ask. The definition of `local statutory provision` that follows (line 73) is part of the same inert machinery. |
| s 11(10) | 74 | inert | Says that such an order is made by statutory instrument subject to annulment by either House of Parliament. Order-making machinery. |
| s 11(11) | 75 | encoded | `cda-s11-s12-extent.l4`: `the effect of the repeal of an enactment about procedure or jurisdiction`. |
| s 12(1) | 77 | encoded | `cda-s11-s12-extent.l4`: `the first day the Act is in force`, `the Act is in force on` (fork F7). |
| s 12(2) | 78 | inert | Gives the Act's short title. Nothing turns on it for a person in the seat; the module headers use the name. |
| s 12(3) | 79 | encoded | `cda-s11-s12-extent.l4`: `whether the provisions of sections 1 to 10 extend to`. |
| s 12(4), (5) | 80-81 | repealed or blank in this text | The text shows only dots in each of the two subsections. |
| s 12(6) | 82 | encoded | Read with s 12(3) in the same rule: it extends Part II of the Schedule and s 11(8) to Scotland and s 11(2), Part III and s 11(8) to Scotland and Northern Ireland, none of which is sections 1 to 10, so it does not change the answer for those sections. |
| Schedule (Repeals), heading and "Sections 11 and 12." | 83-84 | not applicable | A heading and a cross-reference to the sections that give the Schedule effect. |
| Schedule Part I (England and Wales only) | 85-112 | inert | A table of enactments repealed in part or whole for England and Wales (the Malicious Damage Act 1861 among them). The repeals take effect through s 11(8) and leave no rule to apply to a person's conduct; the repealed enactments are not inputs and are not modelled. |
| Schedule Part II (England, Wales and Scotland) | 113-126 | inert | A table of further repeals extending to Scotland. Same reason as Part I. |
| Schedule Part III (United Kingdom) | 127-131 | inert | A table of repeals extending to the whole United Kingdom. Same reason as Part I. |

Summary: 43 rows. encoded 28, inert 9, repealed or blank in this text 4, not applicable 2.

## Fork register

Each fork is an ambiguity in the text, the readings seen, the reading taken and the text that licenses it.
"Looked at" notes say where I searched when nothing was found.

**F1. "Any such property" in s 1(1).**
Readings: (a) property belonging to another (the antecedent, "any property belonging to another"); (b) any property.
Taken: (a).
The inputs `intending to destroy or damage any such property` and `reckless as to whether any such property would be destroyed or damaged` are separate from the s 1(2)(a) inputs for "any property", so that a person who meant to damage something else but damaged another's property is not an offender under s 1(1) unless they were reckless about the property that was damaged.
Licence: s 1(1), "any property belonging to another ... any such property"; s 1(2)(a) says "any property" where it means any.

**F2. What "other than one involving a threat ... in a way which he knows is likely to endanger the life of another or involving an intent ... so to destroy or damage property" excludes from s 5.**
Readings: (a) exactly the life-endangering limbs, s 2(b) and s 3(b); (b) any offence under s 2 or s 3 that happens, on its facts, to involve a threat or intent of that kind, including a s 2(a) or s 3(a) offence done knowing it is likely to endanger life; (c) "so" refers to destroying or damaging property in any way, which would exclude all of s 3.
Taken: (a).
Licence: the clause describes the s 2(b) threat ("in a way which he knows is likely to endanger the life") and the s 3(b) intent word for word; s 5(2)(b) speaks of "a charge of an offence under section 3 above, [where the person] intended to use ... something to destroy or damage it", which would be pointless if all of s 3 were excluded (against (c)).
Cost of the alternative: reading (b) would need a fact (knowing it likely to endanger life) in the s 2(a) and s 3(a) questions and would make `section 5 applies to` depend on facts, not on the offence.

**F3. The "lawful excuse" that is not deemed by s 5(2).**
The Act does not say what other lawful excuses or defences exist (s 5(2) opening words, s 5(5)).
Taken: one stated fact, `a lawful excuse or defence recognised by law apart from section 5(2)`, which excuses every limb.
Licence: s 5(5), "This section shall not be construed as casting doubt on any defence recognised by law as a defence to criminal charges."
Looked at: ss 1 to 3 for any list of excuses, and s 10; there is none.

**F4. Co-owned property is "property belonging to another".**
Readings: (a) property belongs to every person with a connection under s 10(2) to (4), so property the accused shares with another belongs to the other too; (b) "another" excludes property the accused also owns.
Taken: (a).
Licence: s 10(2), "any person ... having in it any proprietary right or interest"; the Act has no exclusion for the accused's own interest.
The same reading makes joint property satisfy both s 2(a) and s 2(b).

**F5. "That other or a third person" (s 2(a)) and "some other person" (s 3(a)).**
Taken: any person other than the accused; in the s 3(b) question the user's connection is asked separately and may overlap with the other persons asked about for 3(a).
Licence: the words themselves.

**F6. The consent belief in s 5(2)(a).**
The belief is about persons "whom he believed to be entitled to consent", so whether they were in fact entitled is not asked; the two beliefs ("had so consented", "would have so consented") are alternatives.
Taken: two stated beliefs, either of which suffices; only whether each is honestly held is read (s 5(3)).
Licence: s 5(2)(a) and (3).

**F7. When the Act comes into force.**
Section 12(1) says "at the expiration of the period of three months beginning with the day in which it is passed".
Readings of the date it was passed: the text gives one date, `[14th July 1971]`, under the long title; it does not say that this is the date of Royal Assent.
Taken: that date is the day the Act was passed; three months beginning with 14 July 1971 end on 13 October 1971; the Act is in force from 14 October 1971.
The rule adds three months to the day it was passed with `add months` (library `daydate`), and the result is tested against 14 October 1971, written by hand (`cda-tests-extent.l4`).
Licence: lines 4 and 77.

**F8. Penalties.**
Section 4 states a ceiling "on conviction on indictment" in each subsection and nothing about summary conviction.
Taken: the summary route returns the explicit value `no maximum is stated in this text for that mode of conviction` (never 0 or FALSE); section 4 states ceilings, not tariffs, so the rule says "the most that can follow", not the sentence.
"Arson under section 1" is life for both 1(1) arson and 1(2) arson; "an offence under section 1(2) (whether arson or not)" is life for 1(2) by fire or not; every other offence in the Act is ten years.
One act amounting to two offences takes the heavier ceiling; the Act says nothing about cumulating sentences.

**F9. England and Wales.**
No operative sentence says that the Act extends to England and Wales.
Taken: the Act extends there by the long title ("An Act to revise the law of England and Wales ...") and by the contrast with s 12(3), "this Act does not extend to Scotland or Northern Ireland"; sections 1 to 10 are not within s 12(4) to (6) (blank, and about the Schedule and s 11).
Licence: lines 3 and 79 to 82.

**F10. Property "belonging to himself or another" in s 5(2)(b).**
The property protected is not the property damaged, so s 10(2) is not applied to it.
Taken: a stated fact, `purpose of protecting property belonging to the accused or another`.
Licence: s 5(2)(b) speaks of the purpose, "in order to protect property belonging to himself or another".

**F11. Words of state of mind and judgment.**
"Intending", "reckless", "knows", "believed" and "reasonable" are not defined in the text.
Taken: each is a stated fact the person gives; nothing decides one for them; recklessness is a single fact, not split into tests from other law.
Looked at: s 10 (definitions) and s 5(3) (belief only).

**F12. Judgments handed to officials (s 6(1)).**
"If it is made to appear ... that there is reasonable cause to believe" is the justice's judgment.
Taken: conditional inputs (information on oath laid; reasonable cause to believe), asked of the person as facts about the justice's side.

**F13. Section 7(2) and section 9.**
Whether a rule of law is "a rule of law ousting the jurisdiction of magistrates' courts", whether proceedings are for "the recovery or administration of any property" and whether a statement was made "as aforesaid" are legal characterisations; each is a stated fact.
The provision's exceptions are explicit values (`section 7(2) says nothing about this`, `section 9 says nothing about this`) so that outside the section's reach the rule returns "not covered" and not FALSE.

**F14. Ownerless property and s 1(2).**
Section 1(2) covers "any property, whether belonging to himself or another".
Taken: property within s 10(1) that no one is connected with is within s 1(2) (it is not excluded by "belonging"); it is not within s 1(1), s 2 or s 3.

**F15. Offences by fire.**
Section 1(3) only says how an offence under s 1 by fire "shall be charged".
Taken: the arson constructors exist only inside an offence under s 1; fire without an offence is not an offence.
Looked at: s 4 (arson mentioned in s 4(1) only).

## What the text turns out to say

Each finding ends "Asserted." where a test or case file asserts it.

1. Section 5 does not apply to s 1(2), s 2(b) or s 3(b): an honest belief that the owner consented, or an honest belief that property needed protecting, is no deemed lawful excuse for them.
   Asserted (`cda-tests-lawful-excuse.l4`, `cda-tests-offences.l4`, `cda-cases-seat.l4`).
2. A belief need only be honestly held, not justified, and this includes the belief in s 5(2)(b)(ii) that the means were "reasonable": the person's belief about reasonableness is tested, not reasonableness itself.
   Asserted (`cda-tests-lawful-excuse.l4`).
3. Section 4 states penalties on conviction on indictment only; for summary conviction the text states none.
   Asserted (`cda-tests-punishment.l4`, `cda-cases-seat.l4`).
4. "Arson under section 1" and "an offence under section 1(2) (whether arson or not)" carry life; every other offence carries a term not exceeding ten years; s 1(1) other than by fire is ten years.
   Asserted (`cda-tests-punishment.l4`, `cda-cases-seat.l4`).
5. A wild creature or carcass that has not been reduced into possession (or whose possession was lost or abandoned) and is not being reduced is not property although tangible ("if, but only if").
   Asserted (`cda-tests-definitions.l4`, `cda-cases-seat.l4`).
6. Section 10(1)(b) excludes wild mushrooms and wild "flowers, fruit or foliage"; it does not exclude the plant: a wild tree itself, as distinct from its flowers, fruit or foliage, is property.
   Asserted (`cda-tests-definitions.l4`).
7. Property belongs to every person with custody or control, a proprietary right or interest, a charge, a right to enforce a trust, or (corporation sole) title; an equitable interest arising only from an agreement to transfer or grant an interest does not count by itself, though a charge or custody alongside it does.
   Asserted (`cda-tests-definitions.l4`, `cda-cases-seat.l4`).
8. Property the accused shares with another is "property belonging to another" (fork F4).
   Asserted (`cda-tests-definitions.l4`, `cda-tests-offences.l4`, `cda-cases-seat.l4`).
9. Altering only the contents of a computer or storage medium is not damage; impairing its physical condition is (s 10(5)).
   Asserted (`cda-tests-definitions.l4`, `cda-tests-offences.l4`, `cda-cases-seat.l4`).
10. One act can amount to offences under both s 1(1) and s 1(2); the Act does not make them alternatives.
    Asserted (`cda-tests-offences.l4`, `cda-cases-seat.l4`).
11. Fire alone is no offence: s 1(3) governs only how an offence under s 1 is charged.
    Asserted (`cda-tests-offences.l4`, `cda-cases-seat.l4`).
12. Section 1(2) reaches property that no one is connected with; section 1(1) does not.
    Asserted (`cda-tests-offences.l4`).
13. Section 2 requires an intention that the other would fear the threat, not an intention to carry it out.
    Asserted (`cda-tests-offences.l4`, `cda-cases-seat.l4`).
14. Section 3 requires no particular kind of thing in custody and no imminent use: only custody or control and the intention.
    Asserted (`cda-tests-offences.l4`).
15. In s 3(b) "the user's property" counts as well as the accused's own.
    Asserted (`cda-tests-offences.l4`, `cda-cases-seat.l4`).
16. The Act has no operative sentence extending it to England and Wales; the long title and s 12(3) do the work (fork F9).
    Asserted (`cda-tests-extent.l4`, `cda-cases-seat.l4`).
17. The Act comes into force on 14 October 1971 on the reading in fork F7; the abolition of common law arson in s 11(1) runs from then and the text is silent about earlier acts.
    Asserted (`cda-tests-extent.l4`, `cda-cases-seat.l4`).
18. A statement or admission made in answering or complying in the civil proceedings s 9 names cannot be used against the maker or, unless they married or became civil partners afterwards, against the spouse or civil partner.
    Asserted (`cda-tests-proceedings.l4`, `cda-cases-seat.l4`).
19. Section 6(2) lets an authorised constable seize anything he believes to have been used or to be intended for use as described, not only the thing the warrant names.
    Asserted (`cda-tests-proceedings.l4`, `cda-cases-seat.l4`).
20. Section 7(1) and section 8 and s 11(2) to (5) and s 12(4), (5) are blank in this text.
    Not asserted: nothing to assert; recorded in the coverage table.

## What the stable binary does not accept

Met in this run, with the binary 1.6.98 (`darwin-arm64`):

- `Date` is not in the prelude: a date constructor needs `IMPORT daydate` (`Date d m y`, day first). Without it the error is "I could not find a definition for the identifier Date".
- `length` is not in the prelude. Lists are handled with `CONSIDER ... WHEN EMPTY / x FOLLOWED BY xs`, `any`, `elem` and `append`.
- A record inside a `LIST` needs its own parentheses: `LIST (R OF a, b), (R OF c, d)`; unparenthesised, the constructor reports too many arguments.
- `l4 run` exits 0 when an assertion fails (a file holding only `#ASSERT 1 EQUALS 2` exited 0 and printed `assertion failed` as an Error diagnostic); `check.sh` reads the diagnostics instead.

Avoided on the word of the brief, not tested here: `REFUSE`, `#ASSERT REFUSED` and `BECAUSE`; a section-level `GIVEN`; `TYPICALLY`; `YMD`; sets; `@lang`; `@nonexhaustive`; opaque `DECLARE`; `IMPORT` of a module from another folder.
Every `NOT` is parenthesised, every `#ASSERT` is on one line, and `JL4_LIBRARY_PATH` was left unset.

## What check.sh prints

Run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` with `l4` 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`; exit status 0.
This is a point-in-time record: nothing re-runs it after the deposit.

```
module                                    errors satisfied  failed  refused  expected
cda-cases-seat.l4                              0        80       0        0         0
cda-fixtures.l4                                0         0       0        0         0
cda-nouns.l4                                   0         0       0        0         0
cda-s1-s3-offences.l4                          0         0       0        0         0
cda-s10-interpretation.l4                      0         0       0        0         0
cda-s11-s12-extent.l4                          0         0       0        0         0
cda-s4-punishment.l4                           0         0       0        0         0
cda-s5-lawful-excuse.l4                        0         0       0        0         0
cda-s6-s9-proceedings.l4                       0         0       0        0         0
cda-seat.l4                                    0         0       0        0         0
cda-tests-definitions.l4                       0        41       0        0         0
cda-tests-extent.l4                            0        20       0        0         0
cda-tests-lawful-excuse.l4                     0        68       0        0         0
cda-tests-offences.l4                          0       178       0        0         0
cda-tests-proceedings.l4                       0        27       0        0         0
cda-tests-punishment.l4                        0        34       0        0         0
TOTAL (16 modules)                             0       448       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Also run, each reporting nothing wrong:

- `python3 -I srcrefs.py check --refs <the raw text file> <all .l4 files>`: 0 problems (also passes `--strict`).
- `l4 check` over every file, searched for `is at the end of the file|follows code on its line` and for warnings: none.

## What would need doing before the encoding is worth relying on

- A domain expert (a criminal lawyer) must read it against the Act and against the law that gives the Act's words their meaning; none has.
- The text is a plain-text rendering as at 2008-10-01; it must be checked against the official text and any later amendment applied.
- The terms the Act does not define (reckless, intending, knowing, believe, reasonable, lawful excuse beyond s 5) take their meaning from case law that is outside the inputs; the encoding takes each as a stated fact.
- Penalties on summary conviction, and the mode of trial, are outside the text: they would come from other instruments.
- The Police (Property) Act 1897, the Visiting Forces Act 1952 and the Firearms Act 1968 are named but not encoded.
- The commencement date (fork F7) rests on reading the bracketed date as the day the Act was passed; the official text of the Act should confirm it.
- The seat's `What the thing is` choice and the aggregated "someone else" answers are modelling devices; a user-interface review should confirm they read naturally to a lay person.
- The questions in the seat should be tried by someone who is not the author.
