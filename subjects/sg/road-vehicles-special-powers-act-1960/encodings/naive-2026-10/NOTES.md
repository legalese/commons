# Road Vehicles (Special Powers) Act 1960 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021), informal
consolidation in force from 14/4/2026. The latest amendment annotated is Act 5 of
2026 (in force 14 April 2026), which added s 4(8) and s 7.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**REQ-0094** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining Singapore
Acts, ordered by everyday-life relevance. It asks what the Act decides for a person
or business it applies to. No scenario has asked a sharper question yet. The Act has
seven sections and a Schedule, so this row takes all of it: the duty to stop and the
power to search (s 3), seizure and forfeiture (s 4), the duty to identify the driver
(s 5), penalties (s 6) and the scheduled offences. Not encoded: s 1, s 7 (the
Minister may amend the Schedule by Gazette order), what a "special authorisation"
under the Public Order and Safety (Special Powers) Act 2018 is (here it is an input),
and the elements of each scheduled offence (each is named by its provision).

## What the Act turns out to say

### 1. A car can be forfeited with nobody convicted, and without any court order at all

s 4(1): on proof that the vehicle was used in, to reach, or to escape from a
scheduled offence, and on the Attorney-General's written application, the court "is
to" order forfeiture, "notwithstanding that no person may have been convicted". And
under s 4(4), if there is no prosecution, a seized vehicle "must be forfeited at the
expiry of one month from the date of seizure unless a claim ... is made before that
date". No order is needed for that. Asserted.

### 2. The new protection for an owner whose car was taken without consent reaches only court orders

s 4(8) (Act 5 of 2026): a court "need not" order forfeiture if the offender was not
the owner and used the vehicle without the owner's consent. It applies "Despite
subsections (1) and (6)" and speaks of "a court". It does not mention s 4(4). Reading
that as written, an owner who does not claim within the month still loses the car.
That is an inference from the wording, and it is encoded that way. Asserted.

### 3. A claim must be in writing, made in person or by an agent authorised in writing

s 4(4): the claim is "written notice to the Commissioner of Police", given
"personally or by that person's agent authorised in writing". An agent with only oral
authority does not make a claim. Asserted. The Commissioner may then release the car
or refer the matter to a Magistrate (s 4(5)). The Magistrate "is to" forfeit if the
use is proved. Without that proof the Magistrate only "may" release (s 4(6)).
Asserted for the forfeiture side.

### 4. If the vehicle is returned, that is usually all you get

s 4(7): in proceedings about a seizure, nobody is entitled to costs, damages or other
relief beyond return of the vehicle, "unless such seizure was made without reasonable
or probable cause". Asserted.

### 5. Withholding the driver's identity costs twenty times more under a special authorisation

s 6(1): failing to stop (s 3(1)) or to identify the driver after a scheduled offence
(s 5(1)) carries up to $1,000 or 6 months, or both. s 6(2): the same failure under
s 5(2), while a Public Order and Safety special authorisation has effect, carries up
to $20,000 or 2 years, or both. Both duties fall on the owner and on anyone who "was
or should have been in control", not on a passenger. A person has a defence if they
could not have known the information with reasonable diligence, or circumstances
beyond their control made it impossible to give it before they were charged (s 5(3)).
What they do give can be used in evidence against them, "Notwithstanding anything in
any other written law" (s 5(4)). Asserted.

### 6. The scheduled offences are about drugs, weapons, gangs, violence and property, not driving

The Schedule lists, among others, Misuse of Drugs Act ss 5, 6, 7 and 8(a)
(possession), but not s 8(b) (consumption). It also lists Penal Code murder,
kidnapping and rioting, and the whole of Penal Code Chapter 17. Chapter 17 is
"Offences against property", so theft is included; that heading was read in the
deposited Penal Code, not here. Neither Penal Code s 279 (rash driving) nor any Road
Traffic Act offence is listed. Attempt, abetment, and conspiracy under s 120B to
commit a listed offence are themselves scheduled (Schedule para 1(k) and para 2).
Asserted.

### 7. Search after a chase does not need a road

s 3(2) allows a search (a) of a vehicle "on any road", or (b) "upon the overtaking"
of a vehicle whose driver failed to stop when required. Limb (b) does not mention a
road. Either way, the officer must suspect on reasonable grounds a scheduled-offence
article or a special-authorisation target. The duty to stop arises only on a request
by a police officer "in uniform" (s 3(1)). Asserted.

## What would need doing before this is worth anything

- The Public Order and Safety (Special Powers) Act 2018 was not read; when a special
  authorisation "has effect" and what counts as its target are inputs here.
- The Schedule is encoded only for sample offences. The repealed Betting and Common
  Gaming Houses Act entries and the Gambling Control Act sections were not checked
  against those Acts.
- What happens to a vehicle after a s 4(8) refusal to forfeit is not stated in the
  text and is not encoded.
- No case law on s 4 forfeiture or s 4(8) was searched.
