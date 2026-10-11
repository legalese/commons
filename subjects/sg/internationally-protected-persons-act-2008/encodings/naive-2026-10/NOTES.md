# Internationally Protected Persons Act 2008 — naive encoding

**Method: naive.** Straight from the deposited text. The `writing-l4-rules`
skill was not loadable in the session that wrote this row, so the conventions of
the finished example rows were followed instead. No pipeline, no coverage table,
no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation
31 December 2021), informal consolidation "version in force from 1/7/2025", as
deposited at `../../registers/source-bundle/IPPA2008.txt`. The latest amendments
annotated are Act 3 of 2021 wef 01/07/2025 (First Schedule) and Act 17 of 2022
wef 01/07/2022 (s 11, extradition). Section numbers follow the body of the
deposit; its arrangement of sections is one out of step.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0125** in `subjects/sg/requirements.jsonl`: Tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. It asks what the
Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. This row takes who is protected (s 3(1)), relevant premises
(s 2), the offences abroad and their Schedules (ss 4, 5, 7), threats (s 6), the
presumption of knowledge (s 8), the duty to tell the police (s 9) and the Public
Prosecutor's consent (s 12). Not encoded: the Minister's certificate (s 3(2)),
mutual legal assistance (s 10), extradition (s 11), amendment of the Schedules
(s 13), limb (b) of s 7 (premises and vehicles), limbs (b) to (d) of the s 9(4)
definition, and the punishments of the scheduled offences themselves, which live
in Acts not retrieved.

## What the Act turns out to say

### 1. Anyone in Singapore who knows something must tell the police at once, with no excuse written in

s 9(1): "every person in Singapore" with information they know or believe may be
of material assistance in preventing a relevant offence, or in securing someone's
apprehension, prosecution or conviction in Singapore, commits an offence if they
fail "to disclose the information immediately to a police officer". The maximum
is a $50,000 fine or 5 years or both. The text gives no reasonable-excuse
defence. Asserted.

### 2. Good-faith disclosure overrides contract and professional rules

s 9(2), (3): no criminal or civil proceedings lie for a good-faith disclosure,
and the discloser is not in breach of "any restriction upon the disclosure of
information imposed by law, contract or rules of professional conduct". Asserted
(as a single flag; what the shield does without good faith is not stated).

### 3. The relevant offence for s 9 can happen in Singapore and needs no knowledge

s 9(4)(a) covers "an offence specified in the First Schedule committed to or in
relation to an internationally protected person", with no place or knowledge
requirement. So information about a planned rape or murder of a visiting foreign
minister in Singapore triggers the duty, though s 4 itself only reaches acts
outside Singapore. Asserted (limb (a) only).

### 4. Knowledge is presumed; the accused must prove ignorance

s 8 presumes, once the act is proved, that the accused knew the victim was
protected or that the premises or vehicle were relevant, "unless the contrary is
proved", for each of ss 4 to 7. The encoding takes the accused's proof of lack of
knowledge as the only way out. Asserted for ss 4 to 7.

### 5. Simple hurt, simple assault and plain outrage of modesty are not scheduled

The First Schedule lists murder, culpable homicide, grievous hurt, kidnapping,
wrongful confinement, rape, hostage-taking, s 354A outrage of modesty and others,
but not Penal Code ss 323, 352 or 354, nor criminal intimidation (s 506). The
Second Schedule lists mischief and explosion offences but not criminal trespass
or theft. Items 2 and 3 of the First Schedule were deleted by Act 3 of 2021 wef
1 July 2025; the deposit does not say what they were. The descriptions of the
unlisted sections are general knowledge of the Penal Code, which was not
retrieved (inference). Asserted.

### 6. The family tests differ, and a trade minister abroad is not automatically protected

s 3(1)(b) protects a Head of State's, head of government's or foreign minister's
family member who is "accompanying" them; (d) protects a diplomat's family
member who "forms part of the person's household". Each fails the other's test.
Paragraph (a) names only heads of State, heads of government and foreign
ministers, so another minister abroad is protected only under (c), if entitled
to special protection. INFERENCE: a paragraph (a) office-holder may also qualify
under (c). Asserted.

### 7. A threat carries the lesser of 7 years and the threatened offence's term, with no fine cap

s 6(1): imprisonment up to 7 years or the term for the threatened offence,
"whichever is the lesser"; (2): 7 years where no term is prescribed. Neither
subsection caps the fine. Threats are caught "in or outside Singapore". READING
TAKEN: the "likely to endanger" words qualify only threats against premises and
vehicles, as in s 5; the other reading is open. Asserted.

### 8. Nothing proceeds without the Public Prosecutor

s 12: no prosecution under the Act "except by or with the consent of the Public
Prosecutor". Asserted.

## What would need doing before this is worth anything

- The Penal Code and the other scheduled Acts were not retrieved, so the
  punishments the extraterritorial offences borrow, and the term caps used in
  s 6, are not encoded.
- The fork in s 6 and s 7 (whether "likely to endanger" also limits threats
  against persons) needs a reasoned decision or a case.
- s 9(4)(b) to (d), s 7(b), s 10 and s 11 are not encoded.
- No case law or subsidiary legislation was searched.
