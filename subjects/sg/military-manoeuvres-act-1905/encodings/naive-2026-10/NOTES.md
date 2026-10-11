# Military Manoeuvres Act 1905 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
28/10/2022), as deposited at `../../registers/source-bundle/MMA1905.txt`. The cover
says the edition incorporates amendments up to 1 December 2021; the latest amendment
annotated in the body is Act 24 of 2022 wef 28/10/2022 (s 7). The arrangement of
sections at the top of the deposit is one line out of step with the body; the body's
numbering is followed.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0136**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act has 14 sections, so
nearly all of it is encoded: ss 2 to 7 and 9 to 14. Not encoded: the Minister's
proclamation power (s 8), which is taken as a given fact ("declared"); the content of
any rules made under s 11 (none was retrieved); arbitration procedure beyond the
reference to 2 arbitrators; the amount of any compensation.

## What the Act turns out to say

### 1. Compensation does not depend on fault, and is "full"

s 4(1): "Full compensation" is paid for injury, damage or interference "arising from
putting in force any of the provisions of this Act, whether or not occasioned by the
acts or defaults of the forces". It covers expenses reasonably incurred protecting
persons and property, and damage to a highway by "excessive weight or extraordinary
traffic". Fault is not an input to the encoding. Asserted (as the route a loss takes).

### 2. The deadline to claim is set by the notice, not by the Act, when there is a notice

s 4(2): claims must reach the secretary to the Armed Forces Council within the period
named in the notice, or, with no notice, within one month of the conclusion. The notice
must name a date "not earlier than one month from the conclusion" (s 2(1)(b)). So where
a notice was given, a claim sent within a month but after the date named is out of time
on the words. Sending in a claim is itself "a submission to arbitration" if the amount
is not agreed (s 5(1)). Asserted.

### 3. Homes, schools, places of worship, factories and shops are off limits

s 3(1) lets troops pass over, encamp and build non-permanent works on "any land", but
s 3(2) authorises no entry on a dwelling house and its curtilage, a place of worship
or school and ground attached to them, a factory, store or business premises. Water may
be taken, but damming must not interfere with any trade or industry, and a private or
public supply must still meet the needs shown by those entitled. Asserted.

### 4. Small exercises need no notice, but only for 48 hours

s 2(1): more than 500 troops requires a month's written notice, a period of at most 3
months, and posting in every village at least 14 days ahead (s 2(2)). At 500 or fewer,
no notice is needed, but then the manoeuvres "shall not extend beyond a period of 48
hours" (s 2(3)). On a declared manoeuvring ground the Armed Forces Council may proceed
without notice (s 9(1)(a)); that the 48-hour cap does not apply there is an
**inference**, labelled in the encoding. Asserted.

### 5. The s 6 offences are confined to a "manoeuvring ground"

Interfering with manoeuvres, entering or remaining in a camp or moving a flag without
authority, or maliciously cutting a forces' wire, is an offence ($2,000 or 6 months or
both, arrest without warrant) only "within a manoeuvring ground and during the
continuance" of manoeuvres. Whether land merely within a s 2 notice counts as a
manoeuvring ground is not said; the encoding takes the words literally (an
**inference** about scope). Accidental damage and authorised entry are not offences.
Asserted.

### 6. Firing-ground rules touching fishing need Parliament; rules touching swimming do not

s 11(4): rules affecting a "public right" must be approved by resolution of Parliament
before they come into force, and "public right" means "any right of navigation,
anchoring or fishing". A rule excluding swimmers or walkers needs no such approval on
the words. Firing-ground occupiers get compensation as an annual rent while the land
stays a firing ground (s 13(1)), in addition to s 4 compensation (s 12), if they claim
in writing within 2 months of the land being used as a firing ground (s 14(1)); none is
granted for a building begun after the rules were posted (s 14(2)). Warning by red flag
needs at least 24 hours (s 10(1)(a)). Asserted.

## What would need doing before this is worth anything

- No rules under s 11, proclamations under s 8, or case law were retrieved.
- "One month" and "2 months" are modelled as numbers of months, not calendar dates.
- The two inferences (48-hour cap on a manoeuvring ground; what is a "manoeuvring
  ground" for s 6) need a lawyer's reading.
- The Act still refers to "every village" and to the Arbitration Act; whether those
  references are read as modern equivalents was not checked.
