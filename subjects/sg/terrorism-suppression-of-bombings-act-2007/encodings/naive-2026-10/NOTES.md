# Terrorism (Suppression of Bombings) Act 2007 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/7/2022), as deposited at `../../registers/source-bundle/TSBA2007.txt`. The deposit's
legislative history lists the latest amendment as Act 17 of 2022 (Extradition
(Amendment) Act 2022), in force 1 July 2022, which recast s 6(3), (6) and (8).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0121** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The Act has eight sections, so nearly all of it is encoded:
the s 2 definitions of a lethal device and the four kinds of protected target, the
s 3 offence with its exclusions and punishments, the s 4 duty to disclose, the s 7
reach abroad, the ss 5 and 6 deeming for Convention countries, and the s 8 consent.
Not encoded: the workings of mutual legal assistance and of the Extradition Act 1968
(only the deeming), s 6(4) and (6) (how notifications interact), and what "material
assistance", "extensive destruction" or "major economic loss" mean, which are taken as
findings of fact.

## What the Act turns out to say

### 1. Every conviction carries death or life imprisonment, and nothing in between

s 3(1)(e) and (f): an offender who "had intended to cause death or serious bodily
injury" where "death is caused" is "punished with death"; "in any other case" with
"life imprisonment". The text gives no alternative and no lower range. A bomber who
meant only extensive destruction causing major economic loss, and who kills a guard
anyway, gets life rather than death, because the death limb needs the intent to kill
or seriously injure. Asserted.

### 2. Everyone in Singapore must tell the police immediately, with no stated excuse

s 4(1): "Every person in Singapore" with information they know or believe "may be of
material assistance" in preventing another person's terrorist bombing offence, or in
bringing another person to justice in Singapore for one, commits an offence by failing
to disclose it "immediately to a police officer": a fine up to $50,000, imprisonment
up to 5 years, or both. The text gives no defence of reasonable excuse and no
exception for legal privilege. The duty is about "another person", so it does not
make anyone report themselves. A good-faith disclosure under s 4 cannot found criminal
or civil proceedings (s 4(2)) and is not a breach of any restriction imposed "by law,
contract or rules of professional conduct" (s 4(3)). Asserted.

### 3. Privately owned places count if the public can get in, even by paying

s 2: a "place of public use" is anywhere "accessible or open to members of the
public, whether continuously, periodically or occasionally, and whether for free or on
payment of a charge". Public transport and infrastructure facilities are covered
"whether publicly or privately owned", and a foreign minister's car used on official
business is a "State or government facility". A private home or an office closed to
the public is none of the four, so s 3 does not reach a bombing there. (That other
laws would is an inference; none was read.) Asserted.

### 4. The offence reaches anyone anywhere, but the duty to disclose does not

s 7: "Every person who, outside Singapore" commits what would be a terrorist bombing
offence in Singapore is deemed to have done it in Singapore. There is no nationality
condition. "Terrorist bombing offence" (s 2) covers the s 3 offence and conspiracy,
incitement, attempt and abetment of it, but not the s 4 failure to disclose, which in
any case applies only to a person "in Singapore". Asserted.

### 5. Soldiers in armed conflict are outside s 3; riots are not armed conflict

s 3(2) excludes armed forces' activities during an armed conflict governed by
international humanitarian law, and military forces' official activities governed by
other international law. s 2: "armed conflict" excludes "riots, isolated and sporadic
acts of violence", so armed forces bombing during riots fall back within s 3.
"Military forces of a State" include civilians who direct the armed forces, and
civilians supporting them only "if ... under the formal command, control and
responsibility" of those forces. A contractor outside that command has no exclusion.
Asserted.

### 6. The political-offence objection is removed, and s 6(1) uses an undefined term

s 5(1) and s 6(7)(b) deem a "relevant offence" of a foreign or Convention country "not
to be an offence of a political character". Under s 6(8)(b) a foreign offence counts
even where the Singapore equivalent would need an intent or aggravating circumstance
that the foreign description lacks. Under s 6(2) and (5) a Gazette notification may
apply the Extradition Act 1968 to a Convention country with no treaty, or with a treaty
that does not cover these offences. Asserted. s 6(1) deems "Every terrorism bombing
offence" an extradition offence. The Act defines only "terrorist bombing offence", so
"terrorism" looks like a slip. Reading it as the defined term is an inference, and
s 6(1) is not encoded as a rule.

## What would need doing before this is worth anything

- The Convention itself, the Mutual Assistance in Criminal Matters Act 2000 and the
  Extradition Act 1968 were not read; ss 5 and 6 are encoded only as deeming.
- The general criminal law on conspiracy, incitement, attempt and abetment, which
  fills in the s 2 list, was not read.
- No case law or prosecutorial practice was searched, including on "material
  assistance" and on whether privilege survives s 4.
