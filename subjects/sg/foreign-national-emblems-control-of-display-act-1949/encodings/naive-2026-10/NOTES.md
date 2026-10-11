# Foreign National Emblems (Control of Display) Act 1949 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FNECDA1949.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on 31 December
2021; it carries annotations of Act 29 of 2022 with effect from 1 August 2023, the
latest amendment annotated. The Arrangement of Sections at the top of the deposit is
out of step with the body; the body's numbering (ss 1 to 8) is followed.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0131** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet. The Act
has eight sections, so this row encodes ss 2 to 8: the definitions, the ban (s 3), the
exceptions and exemptions (ss 4, 5), police powers (ss 6, 7) and offences, penalties and
the Public Prosecutor's consent (s 8). Not encoded: the contents of any Ministerial order
or permit, what "display" means (undefined), and whether the exequatur clause in
s 4(a)(i) reaches diplomats as well as consuls.

## What the Act turns out to say

### 1. Flying your own country's flag where the street can see it is an offence

s 3(1) bars displaying any foreign national emblem "in public or at or within any
school", and s 3(2) counts a display as public if it is "visible from" a road, street,
footway or place the public has access to. The s 4 exceptions are only for accredited
diplomats and consuls, recognised Commonwealth and Irish government representatives,
international-organisation officials, and ships and aircraft. A foreign resident's own
national flag in a window facing the street, or a Singaporean waving a foreign team's
flag on a street, is caught unless the Minister has exempted it under s 5. The same flag
inside a flat out of public view is not. Asserted.

### 2. Portraits of foreign leaders, past or present, count as emblems

s 2 extends "foreign national emblem" to "any likeness or resemblance however
reproduced" of a national leader or former national leader of any state, and to the
leader or former leader of a political organisation claiming to be a national movement.
A flag that merely purports to be a foreign state's counts too, and "state" includes a
dependency or part of a state but excludes Singapore. A film star's likeness or a club
scarf does not count. Asserted.

### 3. A tuition centre is a school

"school" means any premises "where persons are habitually taught whether in one or more
classes". A display "at or within" one is caught whether or not it can be seen from the
street, so a poster of a former foreign leader in a tuition centre is an offence.
Asserted.

### 4. The diplomatic exception covers only the diplomat's own flag

s 4(a) covers "the display of any foreign national emblem of the state of which he is a
national". A consul flying a third country's flag over the consulate gets no exception.
Asserted.

### 5. A permit protects only within its conditions, and occupiers are liable too

The Minister may exempt a display by Gazette order or written permit and regulate its
manner and period (s 5). A display that goes beyond a permit's conditions is an offence
under s 8(1)(a). An owner, tenant, lessee, occupier or person in charge who "knowingly
permits" an unlawful display on or from the premises also commits an offence
(s 8(1)(b)). Asserted.

### 6. The penalties are small, a company cannot be imprisoned, and the PP must consent

An individual faces a fine of up to $500, up to 6 months' imprisonment, or both. A body
corporate faces a fine of up to $1,000 only (s 8(1)). No prosecution may be brought
without the Public Prosecutor's prior written consent (s 8(2)). Asserted.

### 7. Police entry: "reasonable cause" is written for schools only

s 7 lets a police officer enter "any premises where any foreign national emblem is
displayed contrary to" the Act, "or any school in which he has reasonable cause to
believe" an offence has been committed. Read literally (this reading is an inference
from the sentence's structure), entry to premises other than a school requires an
unlawful display actually to be there, while entry to a school needs only reasonable
cause. Arrest without warrant needs reasonable cause (s 6). Asserted as read.

## What would need doing before this is worth anything

- No Ministerial order under s 5 was looked for. A standing Gazette exemption, for
  instance for national days or sporting events, would change finding 1 a great deal.
- "Display" is not defined. Whether wearing a shirt with a likeness on it, or holding a
  phone screen, is a display has not been tested.
- The s 4(a)(i) exequatur clause may qualify only consular representatives. The encoding
  treats the category as one.
- A breach of a permit condition by a display that s 3 would not otherwise catch (for
  instance, in private) is not modelled, though s 8(1)(a) can be read to reach it.
- No case law or prosecution history was searched.
