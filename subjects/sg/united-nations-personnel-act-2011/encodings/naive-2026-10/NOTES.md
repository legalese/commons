# United Nations Personnel Act 2011 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1/7/2025, as
deposited at `../../registers/source-bundle/UNPA2011.txt`. The latest amendment
annotated is Act 3 of 2021 w.e.f. 01/07/2025 (Schedule items deleted); Act 17 of
2022 w.e.f. 01/07/2022 is annotated on ss 11 and 12. The arrangement of sections at
the top of the deposit is one number out of step with the body; the body's numbers
are used. The Schedule tables are column-shifted in the `.txt`, so descriptions were
matched to section numbers by order of appearance.

**Checks:** one case file, `unpa-cases-offences.l4`, 56 assertions satisfied, 0
errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0126**: Tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. This row takes
what bears on a person: who counts as a UN worker and what as a UN operation (s 3),
the offences reaching acts abroad (ss 4, 5, 7), threats (s 6), the presumption of
knowledge (s 8), the duty to tell the police (s 9), which foreign offences found
extradition (ss 11(9), 12(8)), the Public Prosecutor's consent (s 13) and the two
Schedules. Not encoded: the Minister's certificate (s 3(5)), mutual legal assistance
(s 10), the Gazette machinery of ss 11 and 12, the power to amend the Schedules
(s 14), and the punishments of the scheduled offences, which live in other Acts not
read here.

## What the Act turns out to say

### 1. Everyone in Singapore must tell the police, at once, on pain of 5 years

s 9(1): "Every person in Singapore" with information they know or believe may help
prevent a relevant offence, or bring someone to justice in Singapore for one, commits
an offence by failing to disclose it "immediately to a police officer": a fine up to
$50,000, up to 5 years, or both. The "relevant offence" of s 9(4)(a) and (b) is any
First Schedule offence against a UN worker or Second Schedule offence against UN
premises or vehicles — with no knowledge requirement, no endangerment requirement,
and no requirement that it happen abroad. A bystander in Singapore who knows of a
rape of a UN worker in Singapore is caught. Good-faith disclosure is shielded from
suit and from confidentiality duties under law, contract or professional rules
(s 9(2), (3)). Asserted.

### 2. The armed-conflict exclusion is joined by "and"

s 3(4) excludes an operation that is a Chapter VII enforcement action, in which UN
workers are combatants, "and" to which the law of international armed conflict
applies. Read literally, all three must hold. A Chapter VII enforcement action
without combat, or a combat operation to which armed-conflict law does not apply,
stays a UN operation. The encoding reads it literally; a court might read the "and"
otherwise (this is a reading, not something the text says). Asserted.

### 3. Knowing the victim is a UN worker is presumed

ss 4 to 7 all require knowledge — that the victim is a UN worker, or the premises or
vehicle a UN worker's — but s 8 presumes it once the act is proved, "unless the
contrary is proved". The accused carries the burden. Asserted (knowledge is modelled
as "has not proved ignorance").

### 4. Not every attack counts: the Schedules are a closed list

The First Schedule lists murder, culpable homicide, grievous hurt, wrongful
confinement, kidnapping and abduction, hostage-taking, rape and sexual assault,
s 354A outrage of modesty, and corrosive or explosive substance offences, among
others. Simple hurt, theft and criminal intimidation are in neither Schedule, so
ss 4 to 6 do not reach them (the names are ordinary descriptions; the deposit is
silent about them). Premises and vehicles are protected only against mischief
offences (Penal Code ss 426 to 440), and under s 5 only when the act "is likely to
endanger the person or liberty of the UN worker". Asserted.

### 5. A threat costs at most 7 years, or less if the threatened act carries less

s 6: threatening a scheduled act against a known UN worker (or UN premises or
vehicle, if likely to endanger the worker) "in order to compel any person to do or
abstain from doing any act" is an offence anywhere in the world. Imprisonment is
capped at the lesser of 7 years and the term for the threatened offence, or 7 years
if that offence prescribes no term; no cap on the fine is stated. Without the aim to
compel, there is no s 6 offence. Asserted.

### 6. Peacebuilding operations are a separate extradition track

s 3(3) adds peacebuilding and emergency humanitarian operations to "UN operation"
(commenced later than the rest, on 23 May 2011). For extradition, s 11(9) excludes
offences that count "by virtue only of section 3(3)", and s 12(8) covers exactly
those — but only for Protocol countries. An offence against a worker in a
peacebuilding mission therefore founds extradition only for a country party to the
Optional Protocol. Asserted.

### 7. The Act reaches abroad, not home

ss 4 and 5 apply only to acts "outside Singapore"; inside Singapore the scheduled Act
applies directly (an inference: the text does not say so). No prosecution under this
Act may begin without the Public Prosecutor (s 13). Asserted.

## What would need doing before this is worth anything

- The punishments of the scheduled offences (Penal Code and others) were not read;
  the s 6 cap cases use hypothetical terms.
- The literal reading of s 3(4) should be checked against the Convention text (not
  deposited) and any Singapore commentary.
- The duplicated "(b)" in ss 6(1) and 7 was read as the closing words of limb (b);
  the printed Act should be checked.
- The s 3(5) certificate, s 10 mutual assistance and the Gazette machinery of ss 11
  and 12 are not modelled.
- No case law or subsidiary legislation was searched.
