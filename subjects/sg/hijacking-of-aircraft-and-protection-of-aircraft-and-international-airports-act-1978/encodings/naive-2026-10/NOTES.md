# Hijacking of Aircraft and Protection of Aircraft and International Airports Act 1978 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else (the skill was not loadable in this session, so the
conventions of the finished naive rows were followed). No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation; the deposit's page
footer reads "version in force from 1/7/2025". The latest amendment annotated is
Act 3 of 2021 (Guns, Explosives and Weapons Control Act 2021) wef 1 July 2025, to
the definition of "act of violence"; most of the text carries annotations to Act 10
of 2022 wef 1 September 2022. The arrangement of sections at the top of the deposit
is out of step with the body (it numbers "Interpretation" 3 and "Hijacking" 4); this
row follows the body.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is **REQ-0123** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet. This row takes what a passenger, airline or airport business meets:
when an aircraft is in flight or in service (s 2(2)), hijacking (s 3), violence tied
to a hijacking (s 4), sabotage (s 5), false information (s 6(3), (4)), airport
violence and disruption (s 7(1), (2)(a)(i), (b)), credible threats (s 8(1)),
penalties (s 9), officer liability (s 9A(2), (5)), the Public Prosecutor's consent
(s 10) and extradition (s 11(1), (5), (6)). Not encoded: ss 5A to 5D (aircraft as a
weapon, BCN weapons, nuclear material) except as entries in s 8(1) and s 9; s 6(1),
(2) (air navigation facilities); s 7(2)(a)(ii) and (4); s 8(2) beyond its penalty;
s 9A(1) and s 9B; s 11(2) to (4) and s 12. Whether conduct is "unlawful", or an "act of
violence", turns on other written law (s 2(1)) and is taken as a given fact.

## What the Act turns out to say

### 1. A credible threat to hijack is caught; a threat to feed false information to the crew is not

s 8(1) lists the offences a threat to commit is itself an offence: ss 3, 5(1) or (2),
5A(1), 5B(1), 5C(1), 6(1) and 7(1) or (2). It leaves out s 5D(1) (transporting BCN
weapons) and s 6(3) (false information), though s 8(2), on helping an offender evade
justice, lists both. And the threat must be made "under circumstances which indicate
the threat to be credible", so a remark nobody could take seriously is outside s 8(1).
(Whether some other law catches it was not looked at.) Asserted.

### 2. An individual convicted of almost any offence under the Act is liable to life imprisonment, and a company to a $1 million fine

s 9(1): for every offence other than under s 8, an individual is liable "to
imprisonment for life" and any other person "to a fine not exceeding $1 million". No
fine is provided for an individual under s 9(1). A credible threat (s 8(1)) carries up
to $500,000 or 10 years or both; assisting an offender (s 8(2)) up to $500,000 or 7
years or both; a company faces up to $1 million throughout. Whether life imprisonment
is fixed or a maximum this Act does not say. Asserted.

### 3. Hijacking reaches anyone, anywhere, but control taken by stealth alone is outside the words

s 3(1) applies "whatever the nationality or citizenship of the person, whatever the
State in which the aircraft is registered and whether the aircraft is in Singapore or
elsewhere", and covers seizure "by any technological means" as well as force or
threats. (The subsection carries an Act 10 of 2022 annotation; that the technological
limb came in then is an inference.) A foreigner hacking a foreign airliner abroad is caught. Control
taken by none of the three listed means (stealth or persuasion only) is not hijacking
on a literal reading. Asserted.

### 4. Military, customs and police aircraft are carved out unless there is a Singapore link

ss 3(2), 5(5), 5A(3), 5B(3), 5C(3), 5D(4) and 6(6) exclude aircraft "used in military,
customs or police service" unless the act is in or over Singapore, the person is a
Singapore citizen, or the aircraft is in Singapore's own military, customs or police
service. A foreigner seizing a foreign military aircraft abroad is outside the Act;
a Singapore citizen doing the same is inside. s 7(1) has no such carve-out. Asserted.

### 5. "In service" is wider than "in flight", and the difference decides s 5(1)(b)

s 2(2): an aircraft is in flight from the closing of its external doors after
embarkation until one opens for disembarkation (and after a forced landing until the
authorities take over); it is in service from pre-flight preparation until 24 hours
after landing. Sabotage during pre-flight preparation is an offence under s 5(1)(a).
But s 5(1)(b) catches an endangering act of violence on board only "an aircraft in
flight", so the same violence before the doors close is outside it. The 24th hour is
taken to be inside the period, which is an inference. Asserted.

### 6. False information needs no "unlawfully", but the accused may prove belief or good faith

s 6(3) drops the word "unlawfully" that ss 3, 5 and 7(2) use: intentionally
communicating information "false, misleading or deceptive in a material particular"
that endangers or is likely to endanger an aircraft in flight is the offence. s 6(4)
gives a defence the accused must prove: reasonable belief that it was true, or good
faith in lawful employment that includes communicating information. Asserted.

### 7. Airport violence needs a device, substance or weapon

s 7(1) and (2) both require the act to be done "by means of any device, substance or
weapon" at "an aerodrome serving international civil aviation". A bare-handed assault
is outside s 7(1). Disruption of an airport's services (s 7(2)(b)) is an offence only
if it endangers or is likely to endanger the airport's safe operation or people there.
Treating a drone as a "device" is an inference. Asserted.

### 8. Officers are liable for a company's offence even if the company is not convicted

s 9A(2): an officer, or a manager in a position to influence the conduct, who
consented, connived, conspired, was knowingly concerned, or knew or ought reasonably to
have known and failed to take all reasonable steps, is "guilty of that same offence".
s 9A(5): this "applies whether or not the corporation is convicted". An LLP is a
corporation for this purpose (s 9A(6)). Asserted.

### 9. Arrest and charge come before the Public Prosecutor's consent; trial does not

s 10: no prosecution without the Public Prosecutor's written consent, but a person may
be arrested, a warrant issued, a charge laid, and remand or bail ordered without it.
Every offence under the Act, except officer liability under s 9A(2) or 9B(2), is an
extradition offence and is "deemed not to be an offence of a political character"
(s 11(1), (5), (6)). Asserted.

## What would need doing before this is worth anything

- ss 5A to 5D, s 6(1), s 7(2)(a)(ii), s 8(2), s 9B and s 12 are not encoded beyond
  their place in the threat list and penalty table.
- "Unlawfully" and "act of violence" are inputs; they depend on the Penal Code 1871,
  the Arms Offences Act 1973 and the other laws named in s 2(1), none of which was read.
- Penal Code provisions on attempts and abetment, which s 11(6) assumes, were not read.
- No case law or Air Navigation Act 1966 definition of "aerodrome" was retrieved.
