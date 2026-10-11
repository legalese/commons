# Tokyo Convention Act 1971 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/TCA1971.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021"; the latest amending Act annotated in
the body is 32/2018, which brought in the Montreal Protocol of 2014.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0124** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to. No scenario has asked a sharper
question yet. For an ordinary person the Act matters in one place: on a flight, when
someone misbehaves and the crew, the other passengers or an air marshal step in.

The Act is short, so nearly all of it is encoded: ss 2, 3, 4, 5(2) to (5), (7) to (9),
6(1), 6A and 6B. Not encoded: the Minister's Gazette declarations of Convention and
Protocol countries and the joint-operator notifications under s 2(4) (all taken as
given facts), s 5(6) (air marshals bound by bilateral agreements), the list of acts of
unlawful interference in s 5(11) (taken as a given fact), the rules for authenticating
and proving depositions (s 6(2), (3)), the consular officer's power to inquire (s 6(4))
and the regulation-making power (s 7).

## What the Act turns out to say

### 1. Nobody on board can be sued for treatment that follows action taken under the Act, and nothing in s 6A asks for good faith

s 6A: "No liability shall lie" against the commander, crew, a passenger, an air
marshal, the owner or operator, or the person on whose behalf the flight was performed,
"on account of any treatment undergone by a person against whom any action has been
taken under this Act". Nothing in s 6A itself requires good faith or reasonableness.
That limit can only come from the words "taken under this Act", which bring in the
reasonable-grounds tests of s 5. That reading is an inference. Ground staff are not on
the list. Asserted.

### 2. A passenger may restrain someone without asking the captain, but only for safety, never for good order

s 5(4): any crew member or passenger may, "without being authorised by the
commander", take measures they reasonably believe are "immediately necessary" to
protect the aircraft or the persons or property on board. Unlike the commander's own
power in s 5(2), keeping "good order and discipline" alone is not enough. An air
marshal acting alone (s 5(5)) is held to a narrower test: the threat must be unlawful
interference or a serious offence. Property is not mentioned in s 5(5), though it is
in s 5(4). Asserted.

### 3. The captain can make the crew help, but can only ask passengers and air marshals

s 5(3): the commander may "require or authorise" a crew member, but may only
"request or authorise (but not require)" a passenger or an air marshal. Asserted.

### 4. Singapore law follows its own aircraft everywhere, and reaches foreign aircraft that land here with the offender on board

s 3(1) makes an act on a Singapore-controlled aircraft in flight abroad an offence if it
would be one in Singapore. s 3(2) does the same for any other aircraft, but only if it
"subsequently lands in Singapore with the person ... still on board". An aircraft
leased without crew counts as Singapore-controlled when the lessee's principal place of
business is in Singapore. If the lessee has no place of business, its permanent
residence counts instead (s 2(1)). Prosecution needs the Public Prosecutor's consent
unless the offence is under the Air Navigation Act 1966 (s 3(4)). Arrest and remand do
not need it (s 3(5)). Asserted.

### 5. "In flight" begins when the doors close, and after a forced landing in Singapore it lasts until a police officer arrives

s 2(2): an aircraft is in flight from the closing of all external doors after
embarkation until a door is opened for disembarkation. After a forced landing abroad
it lasts until the local authorities take over. After one in Singapore it lasts until
"a police officer arrives at the place of landing". It also covers any time the
aircraft is on the sea or land outside every country's territorial limits. Asserted.

### 6. A captain who puts someone off and does not report it commits an offence, with a fine of up to $1,000

s 5(9): a commander who disembarks a person (from a Singapore-controlled aircraft
anywhere, or from any aircraft in Singapore) must report it, with the reasons, to the
local authority and to the consulate of the person's country. The same applies to a
commander who intends to deliver a suspect to the police. Failing "without reasonable
cause" carries a fine not exceeding $1,000. Restraint may not continue after landing
unless the local authority is notified (s 5(7)). Asserted.

### 7. Smaller points

- For extradition, an offence is treated as committed in the Convention country of
  registration, but in the lessee's country or the landing country only if that
  country is also a Protocol country (s 4(1)). Asserted.
- A deposition from a witness who cannot be found in Singapore is admissible if taken
  on oath before a District Judge or Magistrate in Singapore, or before a consular
  officer or foreign judicial officer abroad, whether or not the accused was present
  (s 6(1)). Asserted.
- The Act authorises nothing in respect of political offences, or action based on
  discrimination, except to protect safety (s 6B). Asserted.

## What would need doing before this is worth anything

- The Gazette lists of Convention and Protocol countries were not retrieved, so each is
  a bare fact here.
- What counts as a "serious offence" is not defined in the Act. It is left as the
  commander's opinion (s 5(2)(b)).
- Whether s 6A's immunity really depends on the s 5 tests being met (finding 1) is a
  question for case law, and no cases were searched.
- The Air Navigation Act 1966, the Police Force Act 2004 (air marshals) and the
  Extradition Act 1968 were not read.
