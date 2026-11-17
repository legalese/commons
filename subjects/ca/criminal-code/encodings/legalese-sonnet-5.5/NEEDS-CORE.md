# NEEDS-CORE (all parts)

Status: **proposed, not landed.** Nothing below is in `ccc-core.l4`. Each part that found the core lacking a type, a constructor or a field declared what it needed under its own prefix in its own module, so every module compiles as it stands; this file gathers the parts' requests in one place so that a later change to the core can take them in one go.
Taking a request into the core would mean editing the part modules that carry the local copy and running the gate again; the merge did not do that.
Each section is the part's own `NEEDS-CORE.md`, unchanged; the same text is under `notes/<part>-NEEDS-CORE.md`.

## ccc1

The core's `Party` (`ccc-core.l4`, line 49) has no constructor for four persons that Part I, sections 25.1 to 25.4 and 29, put a duty on or give a power to.
A part cannot extend a type from another module, so `ccc1` declared small types of its own under its prefix and used those.
Each line below gives the constructor wanted, the text that names the person, and where `ccc1` declares its own stand-in.
These were checked against the files on 2026-11-16: the text lines are in `inputs/R.S.C.-1985-c.-C-46.txt`; the declarations are the lines named.

| constructor wanted in `Party` | text | `ccc1`'s stand-in |
| --- | --- | --- |
| `a senior official` | line 652: "senior official means a senior official who is responsible for law enforcement and who is designated under subsection (5)" | `s 25.2 a senior official`, `ccc1-s25-reports.l4:21` |
| `a competent authority` | line 647: "competent authority means, with respect to a public officer or a senior official, ..." | `s 25.2 a competent authority`, `ccc1-s25-reports.l4:22` |
| `a person who executes a process or warrant` | line 747: "It is the duty of every one who executes a process or warrant to have it with him ..." | `s 29 a person who executes a process or warrant`, `ccc1-s26-33-force.l4:121` |
| `a person who arrests a person` | line 749: "It is the duty of every one who arrests a person, whether with or without a warrant, to give notice ..." | `s 29 a person who arrests a person, whether with or without a warrant`, `ccc1-s26-33-force.l4:122` |

Two things the lead should know before hoisting:

- `ccc1-s25-reports.l4:20` also declares `s 25.2 a public officer`, although the core already has `a public officer`: the three persons of section 25.2 are one declared type there, so that the three are one `DECLARE`.
  If the core gains the first two constructors, that type can go, and the `PARTY` lines can name the core's constructors (the `PARTY` lines of `s 25.1(6)`, `s 25.2`, `s 25.3(1)` and `s 25.4(1)`).
- No other constructor, type or function is wanted from the core.
  Everything else `ccc1` needs from section 2 is read as an input typed `MAYBE BOOLEAN` and named `s 2 <term>: ...`, or is the core's own `s 2 peace officer` and `s 2 public officer`, which the seat layer calls.

## ccc2

Written 2026-11-13. Each item is a type or constructor the core (`ccc-core.l4`) lacks, defined by this part under its own prefix so that nothing waits on the keel.

## 1. `Party` has no constructor for the officials named in s 67

Section 67 applies to "(a) a justice, mayor or sheriff, or the lawful deputy of a mayor or sheriff, (b) a warden or deputy warden of a prison, or (c) the institutional head of a penitentiary ... or that person's deputy" who receives notice of a riotous assembly of twelve or more persons.
The core's `Party` has `a justice` (read from `ccc-core.l4`) and no constructor for a mayor, a sheriff, the lawful deputy of a mayor or sheriff, a warden, a deputy warden, the institutional head of a penitentiary, or that head's deputy.

What this part did: `ccc2-riots.l4` declares `s 67 office`, nine constructors (`s 67(a) a justice`, `s 67(a) a mayor`, `s 67(a) a sheriff`, `s 67(a) the lawful deputy of a mayor or sheriff`, `s 67(b) a warden of a prison`, `s 67(b) a deputy warden of a prison`, `s 67(c) the institutional head of a penitentiary`, `s 67(c) the deputy of the institutional head of a penitentiary`, `s 67 another office`).
The decision functions `s 67 the person must go to that place` and `s 67 the person must command silence and make the proclamation` take an `s 67 office`.
The regulative rule `s 67 the duty of the person who receives notice` is typed ``DEONTIC `s 67 office` `s 67 act` ``, so its party type is this part's `s 67 office` and not the core's `Party`; the office is a `GIVEN` of the rule, and a `#TRACE` prints the input's name (`office`) in the residual instead of the value.

If the lead hoists these into the core: add the seven constructors to `Party`, retype the rule as `DEONTIC Party ...` with the office as a `Party` value, and delete `s 67 office`.
Nothing else in this part depends on it, and no seat question is about these officials (the section binds an official; the person meets it as the thirty minutes of s 68(b)).

## 2. Nothing else

No other core type or constructor is missing.
Every other name this part uses comes from the core as supplied: `Punishment`, `Imprisonment`, `Fine`, `Length of time` and its constants, `Mode of proceeding`, `Class of offence`, `Provision of the Code`, and the `Party` constructors `the accused` and `the Governor in Council`.

## ccc3

What this part wanted from the core (`ccc-core.l4`) and did not find.
No layer-1 rule of this part is blocked by it: each item is handled locally, under this part's prefix, and the lead may hoist it.

1. **`Party` constructors for the officials of Part II.1.**
   The core's `Party` (the constructors from `the accused` to `the Correctional Service of Canada` and the like) has no constructor for the Minister of Public Safety and Emergency Preparedness, the Minister of Foreign Affairs, the Minister of Citizenship and Immigration, the Commissioner of the Royal Canadian Mounted Police, the Director of the Canadian Security Intelligence Service, or a judge of the Federal Court (it has `the Minister of Justice`, `the Governor in Council`, `a judge` and `the court`).
   This part does not need a `Party` for them: `s 83.031(1) Public Safety Minister` takes "the person is the Minister of Public Safety and Emergency Preparedness" as a plain fact, and every other function that turns on one of these officials takes the fact it needs as a plain input.
   Wanted, if a later part compares a `Party` with these offices: constructors named for them.
2. **Nothing else.**
   `Punishment`, `Imprisonment`, `Fine`, `Length of time`, `Class of offence`, `Provision of the Code` and `Party` were enough for every offence, penalty and period of this range.

## ccc4

What this part defines in its own module because the core lacks it, so that the lead can hoist it at the merge (PLAN section 1: "A type or constructor the core lacks is defined in the part's own module under its own prefix and recorded in `NEEDS-CORE.md`").
Status 2026-11-16: read from `ccc4-s99-108-trafficking-and-others.l4` and the core `ccc-core.l4`; nothing here is planned work.

## Constants of type `Length of time`

The core has `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years` and `fourteen years` (`ccc-core.l4:208-214`) and has no three-year or one-year constant.
This part needs two, and defines them under its own prefix (`ccc4-s99-108-trafficking-and-others.l4:19` and `:23`):

| name in this part | definition | used by |
| --- | --- | --- |
| `s 99(2) three years` | `Length of time` OF 3, 0, 0, FALSE | the minimum punishment of a first offence in s 99(2), s 100(2) and s 103(2) |
| `s 102(2) one year` | `Length of time` OF 1, 0, 0, FALSE | the minimum punishment in s 102(2)(a) |

If the core gains `three years` and `one year`, the two names above can be deleted from this module and the callers renamed; until then they stay, and nothing else in the module depends on them.

## Types

This part declares 22 types of its own in layer 1 (7 in `ccc4-s84-definitions.l4`, 1 in `ccc4-s85-98-use-possession.l4`, 2 in `ccc4-s99-108-trafficking-and-others.l4`, 12 in `ccc4-s109-110-3-prohibition-orders.l4`), each named with its section label (for example `s 84(1) kind of thing`, `s 109 act of the court or of a justice`), and one in the seat layer (`ccc4 seat: the penalty of the offence`).
None is asked of the core.

## A function PLAN expects of this part and this part did not write

`s 110.1 an emergency prohibition order has been made` (PLAN section 6, ccc4 row: ss 110.4 to 113, ccc5, ask for it, `MAYBE BOOLEAN`).
It is not defined here; see "Seams (ccc4)" in `NOTES.md` for what is written instead and why the lead should join it at the merge.

## ccc5

Nothing in `ccc5-*.l4` was blocked by the core: every type used is `ccc-core.l4`'s (`Party`, `Punishment`, `Imprisonment`, `Class of offence`, `Length of time`, `Province or territory`, `Provision of the Code`) or declared under the `s N` prefix in this part.
Three constructors would make the encoding closer to the text, and the lead may wish to hoist them (none is needed for the checks to pass):

1. **`Party`: "the Attorney General of the province"** as its own constructor. `s 110.4(2)(b)` and `s 117.0104(2)(b)` answer "the Attorney General of the province in which the application was made" with the core's `the Attorney General or Solicitor General of the province`, which is section 2's wording for the same office ("Attorney General ... means the Attorney General or Solicitor General of the province"). Fork FM-19 in `NOTES.md`.
2. **`Party`: `a firearms officer`, `a chief firearms officer`, `the Registrar of Firearms`, `a provincial minister`.** Sections 110.4 to 117.14 name these persons as applicants, as holders of a power or as the persons a thing is surrendered to. This part takes them as plain facts ("Is the applicant a firearms officer?") and does not use them as actors of a regulative rule, so no declaration of its own was needed.
3. **`Party`: `an analyst`** (section 117.13, certificate of an analyst); the same remark.

## ccc6

Constructors that this part wanted in the core and did not find, for the lead to hoist.
Read against `ccc-core.l4` as it stands in this folder on 2026-11-16 (`DECLARE Party`, line 49).

## `Party` (ccc-core.l4, line 49)

The regulative rules of ss 164 to 164.3 (`ccc6-seizure.l4`) name three parties the core's `Party` has no constructor for.
This part declared a type of its own for them, `ss 164 to 164.3 party` (`ccc6-seizure.l4`, line 131), because a constructor cannot be added to a core type from another module.

| constructor wanted in `Party` | where this part uses it | the text |
| --- | --- | --- |
| the custodian of a computer system | `s 164.1(5.1) the custodian's duty to delete the intimate image` (`ccc6-seizure.l4`, lines 349-355), MUST `s 164.1(5.1) delete the material` WITHIN 48 | s 164.1(5.1) (src:3321), s 164.1(1) |
| a person who claims an interest in the thing forfeited | the `s 164.3(1)` rule (PARTY at `ccc6-seizure.l4`, line 529) | s 164.3(1) (src:3347) |
| the applicant for relief from forfeiture | the `s 164.3(3)` rule (PARTY at `ccc6-seizure.l4`, line 564): the applicant "shall cause notice ... to be served on the Attorney General" | s 164.3(3) (src:3351) |

Also named in the text, not used as a party of a rule: the occupier of the premises (s 164(2), "issue a summons to the occupier of the premises", src:3268); the rule's party is the judge, so the occupier is named only in the act's text.

The fourth constructor of `ss 164 to 164.3 party`, `ss 164 to 164.3 the judge`, is not a gap: the core's `a judge` ("a judge of the court that the provision in question names") would serve, and this part kept one type for the four parties of the section.

## Nothing else

No other core type lacked a constructor or a field this part needed: `Punishment`, `Length of time`, `Class of offence`, `Provision of the Code` and `Province or territory` are used in layer 1 as the keel declared them (grep of the `ccc6-*.l4` modules, 2026-11-16).

## ccc7

Each entry names a type, constructor or helper that ccc7 needed and the core (`ccc-core.l4`) lacks.
ccc7 declared its own, under the label of the section that needed it, so that nothing collides at the merge; the lead may hoist any of them.
Status of every claim below: checked against `ccc-core.l4` as it sits in this folder (read in full on 2026-11-13, not re-derived from PLAN.md).

## 1. A `Provision of the Code` cannot name an Act, or a paragraph

- **Wanted:** a record that carries the Act as well as the section and subsection, and a field for a paragraph.
- **Why:** the core record is `Provision of the Code HAS section IS A NUMBER, subsection IS A STRING` (`ccc-core.l4`, near the end of the file).
  Section 183 "offence" lists provisions of the Criminal Code in paragraph (a) and provisions of fourteen other Acts in paragraphs (b) to (k), so a table over the core record cannot say which Act a row belongs to.
  The core record also has no paragraph field.
- **What ccc7 did:** `s 183 statute` (one constructor per Act the text names, plus `s 183 an Act that is none of those`) and `s 183 provision of an Act` (statute, section, subsection) in `ccc7-s183-offence.l4`; `s 183 provision of the Criminal Code` turns a core record into one.
  The one paragraph the list names, 202(1)(e), is carried as the subsection string "(1)(e)" (fork F3 in NOTES.md).
- **If hoisted:** `s 183 statute` and `s 183 provision of an Act` are used by ccc7-s184-applications, ccc7-s185-applications, ccc7-s186-authorizations, ccc7-s195-notification and the seat layer; renaming them is a find-and-replace across those files.

## 2. `Party` lacks five actors Part VI names

- **Wanted:** `the Minister of Public Safety and Emergency Preparedness` (ss 195, 196), `the person who was the object of the interception` (ss 196, 196.1), `an agent of the state` (s 184.1(4)), `a police officer` as s 183 defines it (distinct from the core's `a peace officer`), and `the party intending to adduce the intercepted communication` (s 189(5)).
- **Why:** the core `Party` (`ccc-core.l4`, section "Who") has `the accused`, `the prosecutor`, `a judge`, `a peace officer`, `the Attorney General or Solicitor General of the province` and others, but none of these five.
- **What ccc7 did:** `s 183 party under Part VI` in `ccc7-s183-base.l4`, ten constructors, used only by the regulative rules of ccc7 (ss 184.1(3), 187, 189(5), 195, 196, 196.1).
  It repeats `the accused`, `the prosecutor`, `a judge` and `the Attorney General of the province` under the `s 183` label because a constructor of the core's `Party` cannot be mixed with them in one type.

## 3. `Length of time` has no hours

- **Wanted:** an hours field, or a separate `Length of hours`.
- **Why:** s 188(2) gives an emergency authorization "for a period of up to thirty-six hours", and the core's `Length of time` counts years, months and days.
- **What ccc7 did:** the function takes the period as a NUMBER of hours (`s 188(2) the judge may give an authorization for a period of up to thirty-six hours`); the limit 36 sits in that function.

## 4. Three-valued helpers every part will want

- **Wanted:** the four helpers of `ccc7-s183-base.l4`: `s 183 as a three-valued answer` (a BOOLEAN to a MAYBE BOOLEAN), `s 183 three-valued all of`, `s 183 three-valued any of` and `s 183 three-valued not`, written once in the core.
- **Why:** every decision function in every part combines JUST TRUE, JUST FALSE and NOTHING by the same Kleene rules (PLAN.md R4: "a caller must never turn NOTHING into FALSE").
  `ccc-core.l4` is "DECLARE and constants only: no rules", so they cannot live there as it stands; this is a request for a shared helper module.
- **What ccc7 did:** kept them in its own base module under the `s 183` label.
  Stable-binary trap met while writing them: `NOT a AND b` parses as `NOT (a AND b)`, which made the `any of` helper answer wrongly until every `NOT` was bracketed; the helper's tests caught it (NOTES.md, "What the stable binary does not accept").

## 5. No gap found in `Imprisonment`, `Fine`, `Punishment`, `Class of offence` or `Mode of proceeding`

Part VI states every penalty as imprisonment on indictment (5 years or 2 years) and "an offence punishable on summary conviction" with no penalty; the core types carry both limbs (`Class of offence` has the "both" constructor), so nothing is requested.
The summary-conviction penalty comes from s 787(1), an input (`s 787(1) the general penalty for an offence punishable on summary conviction`, type `Punishment`), per PLAN.md section 6, ccc7, the one seam this part asks.

## ccc8

What this part wanted from `ccc-core.l4` and `ccc-definitions.l4` and did not find, for the lead to hoist at the merge. Nothing here blocks a check: each item has a stand-in under this part's own prefix.

## Party constructors

The core `Party` has no constructor for a practitioner, a pharmacist or an association, so these regulative rules declare local party types under their section label:

- `s 204 party` (ccc8-part7-pari-mutuel.l4): a person or association that uses or operates a pari-mutuel system; an association operating one. Wanted in core `Party`: `a person or association using a pari-mutuel system`, `an association operating a pari-mutuel system`.
- `s 241.2 party` and `s 241.31 party` (ccc8-part8-maid.l4): a medical practitioner or nurse practitioner; a person responsible for preliminary assessments; a pharmacist or pharmacy technician. Wanted in core `Party`: `a medical practitioner or nurse practitioner`, `a pharmacist or pharmacy technician`, `a person responsible for preliminary assessments`.
- The other regulative rules in this part use the core `Party` (`the accused`, `the court`, `a judge`, `a peace officer`) as it is.

## One constructor declared in two enumerations (finding F-4 in NOTES.md)

`ccc-definitions.l4` declares `a person in a capacity that is none of those` in both `s 2 peace officer capacity` and `s 2 public officer capacity`. The stable binary then cannot resolve the bare name ("There are multiple definitions for the identifier"), so nothing outside the keel can pass either constructor. Wanted: rename one, for example `a person in a capacity that is none of those named in the definition of peace officer`.

## Nothing else

No type, constant or constructor of the core was missing for the modules, and no core name was copied: every top-level name of ccc8-* begins with the label of its provision (`s N ...`) or, for the seat, with "Under section N," ("Under sections 197 to 269.1," for the one record type and its helper).

## ccc9

Each item is a type or constructor the core (`ccc-core.l4`) lacks and this range could use. None blocks the encoding: each has a stated workaround, in use.

1. **`Party` has no constructor for an unnamed person** ("every one", "a person", "no person", "any person"). Sections 273.3(1), 276.03(1), 276.07(1), 276.11(1), 278.18(1), 278.27(1) ("A person shall not publish ...", "No person shall ...") and 278.16(6), 278.25(5) ("must not be used in any other proceedings") bind anyone, not only the accused. The regulative rules name `the accused` as the bearer (`PARTY \`the accused\` SHANT ...`) and the seat asks the question of the person in the seat, so a rule that binds a journalist reads as binding the accused. A constructor such as `a person` (or `any person`) would let a part name the bearer the text names.
2. **`Party` has no constructor for "the judge, provincial court judge or justice" taken together.** The range names that trio 38 times (on 32 lines; grep of lines 5032-5568) (the application procedure of ss 276.01 to 276.1 and 278.3). The rules take the presiding officer as an input of type `Party` (`PARTY presiding`, fork F24) and the traces use `a judge`. A constant for the trio, or a constructor `the presiding officer`, would let the rules name the bearer without an input.

## ccc10

The keel's files are read-only; each item below is declared under a ccc10 prefix in the module that needs it, and is listed here for the lead to hoist at the merge.

1. **`Party` has no "any person".** ss 278.32(1) and 278.36(1) ("A person shall not publish ...") name no particular bearer. Wanted constructor: `any person`. Declared instead: `s 278.32(1) the bearer of the prohibition` (one constructor, `s 278.32(1) any person`) and `s 278.36(1) the bearer of the prohibition`; the same will be needed wherever a prohibition falls on everyone.
2. **`Decision on the charge` has no "a discharge after a finding of guilt".** s 278.98(1)(c) lists "discharged, after having been found guilty" beside acquittal, finding of guilt, a verdict of not criminally responsible and a verdict of unfit; the core's type has the other four but not this one (a conditional or absolute discharge is a `Kind of sentence`). Declared instead: `s 278.98(1) the decision`, with the five paragraphs and `s 278.98(1) a decision of another kind`.
3. **Periods the core lacks** (the core has six months, ninety days, two years less a day, two years, five years, ten years, fourteen years): one year, four years, seven years. They are written inline in each rule, `` `Length of time` OF 4, 0, 0, FALSE ``, with a ruler comment, and not declared as constants, so that no ccc10 name stands for a period used in another provision. Wanted constants: `one year`, `four years`, `seven years`.
4. **No type for who gave consent.** ss 283(2), 318(3), 319(6.1), 320(7) require "the consent of the Attorney General"; the core has the party `the Attorney General`, and the rules here take the fact that the consent was given as a BOOLEAN (whether the person who consented is the Attorney General in the proceeding is s 2 "Attorney General", an input).
5. **No court by province, and no "judge" for a court named in `Party`.** s 320(8) names the Court of Quebec, the Superior Court of Justice, the Court of Queen’s Bench (for four provinces), the Supreme Court (for six provinces and territories) and the Nunavut Court of Justice. The core's `Party` has `the court`, `a court of criminal jurisdiction` and `a superior court of criminal jurisdiction` but not these. Declared instead: `s 320(8) the court` (five constructors, one per paragraph). The plan asks for a `Party` for ccc3's seam; the constructors wanted are `the court of s 320(8)` and `a judge of the court of s 320(8)`.
6. **`Kind of homicide offence`, `Kind of sentence` and the other enumerations were not needed.** No ccc10 rule uses them.

## ccc11

Constructors of the core's `Party` that this part wanted and the core lacks. A constructor cannot be added to a core type from another module, so this part declared a small type of its own under its prefix for each and uses it in its regulative rules; the lead may hoist them into `Party` at the merge and replace the part's types.

| wanted in `Party` | used by (the text) | declared here as |
| --- | --- | --- |
| `a person` (an unnamed person: "No person shall ...") | `s 320.36(1)` and `s 320.36(2)` (the prohibitions on using a bodily substance or its results otherwise than as the section allows; lines 6478, 6480) | `s 320.36 party` with the constructor `s 320.36 any person` (`ccc11-general.l4`) |
| `a person who takes samples of blood` (a qualified medical practitioner or a qualified technician, by 320.28(6)) | `s 320.28(8)` ("A person who takes samples of blood under this section shall cause one of the samples to be retained"; line 6389) | `s 320.28 party` with the constructor `s 320.28 a person who takes samples of blood under section 320.28` (`ccc11-investigation.l4`) |

Not needed: a type or constructor for any other part of the range. `Provision of the Code`, `Imprisonment`, `Fine`, `Punishment`, `Length of time`, `Mode of proceeding` and `Class of offence` carry everything the punishments and the offences name; the occasion (first, second, subsequent) is this part's own enumeration (`s 320.19 occasion`), because the core has no such type and only this part and the sentencing parts (ccc26) turn on it. The lead may hoist it.

## ccc13

Things the part needed from the core or the keel and did not have.
The lead hoists them at the merge; until then they are declared here and used under the `ccc13` prefix.

## 1. Three-valued helpers (hoist)

`ccc13 all of`, `ccc13 any of` and `ccc13 not`, in `ccc13-logic.l4`.
Every part that joins `MAYBE BOOLEAN` answers needs the same three.
Kleene's rules: `all of` answers JUST FALSE if any answer is JUST FALSE, otherwise NOTHING if any is NOTHING, otherwise JUST TRUE; `any of` is the dual; `not` swaps JUST TRUE and JUST FALSE and leaves NOTHING alone.
Tests: `ccc13-tests-logic.l4`.

## 2. A constructor that says no, for the terms the Code says "includes" (request)

The keel's `s 2 testamentary instrument` and the enum `s 2 testamentary instrument kind` have a last constructor for a document that is none of those; because the Code says a testamentary instrument "includes" a list, the keel's function answers NOTHING for it.
A caller that needs a no from it (`s 380(1)(a)`, `s 430(3)`, `s 430(4)`) cannot get one.
This part took a plain yes/no from the person at the seat (fork F13) and left layer 1 taking the answer as a `MAYBE BOOLEAN`.
Request: a constructor of the kind enum that the keel's function maps to JUST FALSE ("what the person judges not to be one"), for this term and any other "includes" term that a caller must be able to answer no.

## 3. Duplicate constructors (note)

The keel's enums repeat constructors such as `a thing that is none of those`; a module that uses one needs `GIVETH A <type>` on the constant, or the name is ambiguous.
Suggest the keel prefix them by type.

## ccc14

Written by part agent `ccc14` on 2026-11-16.
Each item is a type, a constructor or a helper this part needed and the core (`ccc-core.l4`) lacks.
This part defined each under its own prefix, so that nothing collides at the merge; the lead may hoist them into the core and then delete the local copy.
Nothing here changes an answer.

## 1. Constructors of `Party` the core lacks

The core's `Party` names the actors of section 2 (offender, victim, peace officer, judge, the Attorney General, the clerk of the court and so on).
Two regulative rules of this part need an actor the core has no constructor for.
Each is a one-constructor type declared in the module that uses it.

| local type | its one constructor | used by | why the core does not have it |
| --- | --- | --- | --- |
| `s 462.42 party` (`ccc14-part122-forfeiture.l4`) | `s 462.42 a person who claims an interest in property that is forfeited to Her Majesty` | `s 462.42(1) the right to apply` (a MAY, WITHIN 30 days of the forfeiture) | "a person who claims an interest in the property" in subsection (1) names a class of claimants, not an office |
| `s 462.48 party` (`ccc14-part122-disclosure.l4`) | `s 462.48 a person to whom information or documents have been disclosed or provided pursuant to subsection (15) or an order made under subsection (3)` | `s 462.48(15) the prohibition on further disclosure` (a SHANT) | "No person to whom information or documents have been disclosed ..." names any recipient, not an office |

If the lead hoists a general constructor (for example `any person`, or `a person who claims an interest in property`), the two local types can go and the two rules can take the core's `Party`.

## 2. An actor the core already has, used for a class

"Every person who executes a warrant" (`s 462.32(4)(b)`, `s 462.321(4)(c)`) is encoded with the core's `a peace officer`, because subsection (1) of each section speaks of "a warrant authorizing a person named in the warrant or a peace officer" to search and seize (ss 462.32(1) and 462.321(1)), so a peace officer is one of the two persons who execute it.
The core has no constructor for "a person named in the warrant"; the rule says what it says about whoever executes, and `a peace officer` stands for them.
If the lead adds such a constructor, those two rules take it.

## 3. Helpers that belong to no provision (hoist candidates)

| name | module | what it does |
| --- | --- | --- |
| `ccc14 both answers hold` | `ccc14-helpers.l4` | strong Kleene AND of two `MAYBE BOOLEAN` answers: a `JUST FALSE` decides it, otherwise a `NOTHING` stays `NOTHING` |
| `ccc14 either answer holds` | `ccc14-helpers.l4` | strong Kleene OR: a `JUST TRUE` decides it, otherwise a `NOTHING` stays `NOTHING` |
| `ccc14 seat includes answer`, `ccc14 seat means answer` | `ccc14-seat.l4` | the seat layer's reading of a yes to an "includes" definition (`JUST TRUE`; a no is `NOTHING`) and of a yes to a "means" definition (`JUST TRUE`; a no is `JUST FALSE`) |
| `ccc14 seat form of the charge`, `ccc14 seat class of the offence`, `ccc14 seat longest term`, `ccc14 seat indictable limb`, `ccc14 seat punishment limbs`, `ccc14 seat the longest term on indictment` | `ccc14-seat.l4` | pure conversions of the seat's plain inputs into the core's `Imprisonment`, `Punishment` and class-of-offence shapes |

## 4. Not a core gap, but the lead will meet it

On the stable builds (1.6.110 and 1.6.109) a `DEONTIC` value cannot be compared in `#ASSERT`, so every regulative rule of this part is run with `#TRACE` and its outcome is written beside the trace; the same duty is also encoded as a decision function that is asserted.
`check.sh` does not see a different `#TRACE` outcome; the traces of this part were compared by hand between the two builds (NOTES.md, "Checks").

## ccc18

Written 2026-11-16 by `work/mknotes.py` from the declarations in the modules (nothing typed twice).

`ccc-core.l4` declares one actor type, `Party`.
Eight bearers of duties and powers that the text of lines 10275-10956 names in its own words are not among its constructors (checked by searching `ccc-core.l4` for each phrase: no hit).
Each is declared in the part's own module as a one-constructor type under its section label, so that no name collides at the merge, and is used only in the regulative rule of that provision (fork F1).
No bearer is invented: the nearest core constructor (`a public officer`, `a peace officer`, `the keeper of a prison`) would name an actor the text does not.

| local type | constructor wanted in `Party` (the text's words) | module:line |
| --- | --- | --- |
| `s 490.021(6) party` | `s 490.021(6) the person who served the notice` | ccc18-soira-notice:223 |
| `s 490.02903(3) party` | `s 490.02903(3) the person who served the notice` | ccc18-soira-foreign:110 |
| `s 490.02911(3) party` | `s 490.02911(3) a police service` | ccc18-soira-foreign:910 |
| `s 490.02915(1) party` | `s 490.02915(1) the person in charge of the place` | ccc18-soira-itoa:624 |
| `s 490.03(1) party` | `s 490.03(1) the Commissioner of the Royal Canadian Mounted Police or a person authorized by the Commissioner` | ccc18-soira-offences:51 |
| `s 490.5(3) party` | `s 490.5(3) the applicant` | ccc18-forfeiture:452 |
| `s 490.81(4) party` | `s 490.81(4) a person appointed to manage property` | ccc18-forfeiture:781 |
| `s 492(1) party` | `s 492(1) the person who executes the warrant` | ccc18-weapons-evidence:404 |

If the lead hoists a constructor into `Party`, the local type and its constructor in the named module are deleted and the regulative rule names the core's constructor; no other change is needed.

No other type, constructor or constant was needed: every other name this part uses is declared in `ccc-core.l4` (`Party`, `Process document`, `Provision of the Code`, `Punishment`, `Length of time`, `Province or territory` and the `no imprisonment is stated` / `no fine is stated` constructors) or under this part's own labels.

## ccc19

Written by part agent `ccc19` (2026-11-13). Two constructors that `Party` in `ccc-core.l4` lacks and that s 492.3 (line 11019) names:

- `counsel representing the Attorney General of Canada` ("by counsel representing the Attorney General of Canada")
- `a person acting on behalf of the prosecutor or the Attorney General of Canada` ("by any person acting on behalf of the prosecutor or the Attorney General of Canada")

`Party` has `the prosecutor` and `the Attorney General of Canada` but not these two. They are not needed as actors of any regulative rule here (the only party of s 492.3's duty is `the court`); they appear as the answers of `s 492.3 who took the action`, a small enumeration declared in `ccc19-s492-27-to-3.l4` under this part's prefix (`s 492.3 the prosecutor`, `s 492.3 counsel representing the Attorney General of Canada`, `s 492.3 a person acting on behalf of the prosecutor or the Attorney General of Canada`, `s 492.3 someone else`). If the lead hoists the two constructors into `Party`, that enumeration can be replaced by `Party`; nothing else in this part needs a core change.

## ccc20

Each item is a type or constructor the keel's `ccc-core.l4` lacks and that this part needed.
The part did not edit the core; where a constructor was missing it declared a small type of its own, with the section label first, and uses that.
Checked against `ccc-core.l4` as supplied to this run: `grep -n -i -E 'custody|any one|private'` returns only the outcome `detention in custody` (line 141) and a comment (line 154), and the `Party` list (lines 49 to 85) has no private arrester and no custodian.

1. **An hours unit for `Length of time`.**
   `Length of time` (ccc-core.l4, line 174) has `years`, `months`, `days` and `less a day`, and no hours.
   Section 503(1)(a) and (b) count a period of 24 hours (and s 503(2) says when it begins).
   The part takes the 24 hours as a plain `NUMBER` of hours in `s 503(1) the person was taken before a justice as paragraph (a) or (b) requires` and `s 503(2) the hours that run against the 24-hour period` (ccc20-part16-taking-before-justice.l4).
   Wanted: an `hours` field (or a `Length of time` constructor in hours) so that the 24 hours can be a `Length of time`.

2. **A `Party` for "any one other than a peace officer" who arrests.**
   Section 494(3): "Any one other than a peace officer who arrests a person without warrant shall forthwith deliver the person to a peace officer."
   `Party` has `a peace officer` and no constructor for a private arrester.
   The part declares `s 494(3) the actor` and `s 494(3) the act` (ccc20-part16-arrest.l4, lines 77 and 81) for the regulative rule, so the rule's actor is local to this part.
   Wanted: a `Party` constructor such as `a person who is not a peace officer`.

3. **A `Party` for "the person having the custody of an accused".**
   Section 525(1) puts a duty on "the person having the custody of an accused", and s 527(3) addresses an order to "the person who has custody of the prisoner".
   `Party` has `the keeper of a prison` and no constructor for whoever has custody.
   The part declares `s 525(1) the actor` and `s 525(1) the act` (ccc20-part16-failure-and-delay.l4, lines 514 and 517) for the regulative rule.
   Wanted: a `Party` constructor such as `the person having the custody of an accused`.

## ccc23

What layer 1 of this part wanted from the core and did not find. Nothing here blocks the part: each item is asked as a plain boolean fact in the function that needs it, and the lead can hoist the type later and wrap the inputs.

1. Constructors for `Party` (the core's type for who takes part in a proceeding). The core already has `the accused`, `the offender`, `the victim`, `the prosecutor`, `a Review Board`, `a justice`, `a peace officer`, `a court of appeal`, `the Attorney General` and `a witness`, which this part's regulative rules use (`PARTY a Review Board`). The core lacks the people this Part names and no other part is likely to spell differently:
   - `an appellant` and `a respondent` (672.72 to 672.78: "the appellant must give notice of appeal within fifteen days", "the appellant must provide the court of appeal and the respondent with a certified transcript");
   - `the person in charge of a hospital` (672.56, 672.81(1.4), (2), 672.1(1) "hospital");
   - `a medical practitioner` (672.16(2), 672.2, 672.51(8));
   - `the Minister` of 672.68(1) (the Minister of Public Safety and Emergency Preparedness, or the minister of a province, in the dual status offender provisions);
   - `the chairperson of a Review Board` (672.43, 672.48(3), 672.85: layer 1 answers who is one through the seam `s 672.1(1) the issuer is the chairperson of a Review Board`).
   Layer 1 asks each of these as a plain boolean fact in the function that needs it.
2. A core record for "the days between two dates counted in months" is not needed: `add months` and `Day` cover it, and 672.81(1) is tested at the boundary on both sides. Noted only because 672.81 is the one place this part measures calendar months.

Nothing else was missing. The keel's `Provision of the Code` record (section number and subsection) was enough for the twelve sections of 672.81(1.3)(b) and s 163.1 of 672.501(2).

## ccc25

Types and constructors that the core (`ccc-core.l4`) lacks and that Parts XXII.1 and XXII.2 name.
None of them blocks the encoding: each is worked around as stated, and the workaround is the thing to remove if the lead adds the constructor.

1. `Party`: `a police officer`. Sections 715.47(1), 715.47(2), 715.57 name "a police officer" (lines 15061, 15066, 15134). Worked around with the core's `a peace officer` (fork F6 in NOTES.md); section 2 defines "peace officer" and not "police officer".
2. `Party`: `a candidate for appointment as an independent monitor` (section 715.35, line 14952). Worked around with a type of this part's own, `s 715.35 party`, whose constructor is `s 715.35 a candidate for appointment as an independent monitor`; the rule `s 715.35 the candidate's duty to notify the prosecutor` uses it. If the core adds the constructor, that type and constructor can go.
3. `Party`: `a person authorized under the rules and practices referred to in subsection 715.55(3)` (section 715.55(1), line 15122). Worked around with a plain BOOLEAN input on `s 715.55(1) the person may, on request or on their own initiative, convene or cause to be convened a conference`; the Party is not given a constructor, so the regulative rule covers only `a judge` and `a justice`.
4. `Party`: `a department or agency of a government in Canada` and `a member of a department or agency, or an agent` (sections 715.59(1), 715.6(1)(c) and (2)). Worked around with constructors of this part's own enumerations (`s 715.6(1)(c)(i) ...`) and a BOOLEAN input; no regulative rule names them, because no duty or permission is given to them as actors (the text says what records "may be kept" and "may be made available").
5. `Party`: `a police force` (section 715.58(1)) and `an insurance company` (section 715.58(3)). Worked around with BOOLEAN inputs; the permissions that name an actor name `a peace officer`.
6. `Party`: `a justice` is described in the core as "a justice of the peace or a provincial court judge", and `a provincial court judge` is a separate constructor too. `s 715.55(1)` tests `a judge` and `a justice` only, so a provincial court judge must be passed as `a justice` (fork F24).

## ccc26

What part ccc26 wanted from the core (`ccc-core.l4`) and did not find.
Each item says what stands in for it in this part, so that the lead can hoist the wanted name and delete the stand-in.
Nothing in this file changes `ccc-core.l4`; this part defined only names that begin with `s <label>`.

## 1. An order on `Length of time`

Wanted: a comparison of two `Length of time` values (at most, less than), with the text's own rule for months and for "less a day".
Why: the text compares a term with a stated length in s 730(1) ("fourteen years"), s 731(1)(b) ("two years"), s 732(1)(a) and (b) ("ninety days or less"), s 732.2(5)(e) ("one year") and s 736(1) ("two years"); each of those functions calls the stand-in below (checked by grep over the layer-1 modules).
The core has `Length of time` (years, months, days, a "less a day" flag) and constants such as `ninety days` and `two years less a day`, but no order.
Stand-in: `s 716 the first period is at most the second period` in `ccc26-interpretation.l4`, answering `MAYBE BOOLEAN`.
A month is put at 28 to 31 days, so the answer is `JUST TRUE` or `JUST FALSE` when every calendar agrees and `NOTHING` when the calendar decides (three months against ninety days: 89 to 92 days).
It is exact when the two months counts are equal or both periods are in days.
If the core takes the comparison, it should keep the three-valued answer: a caller must not read `NOTHING` as no.

## 2. A `Party` for the minister of justice of a territory

Wanted: a constructor of `Party` for "the minister of justice of a territory".
Why: s 732.1(8), (9) and (11) name "the Attorney General of a province or the minister of justice of a territory".
Stand-in: `` `the Attorney General` `` (the core's `Party`, "as s 2 defines it"), used in `s 732.1(11) the Attorney General's duty to cause the samples to be destroyed` in `ccc26-probation.l4`.
The duty of s 732.1(11) also falls on "a person authorized by the Attorney General or minister"; this part does not name that person as a party: the duty is stated for the Attorney General alone.

## ccc28

Each item below is something the core (`ccc-core.l4`) does not declare and the range needed.
Each is declared in this part's own modules under the section label, as the brief requires, so that the lead can hoist it or leave it.
Checked against `ccc-core.l4` on 2026-11-17: it has no constructor for a sheriff, a person remanded, an applicant, a subject of habeas corpus or any writ, and no comparison of two `Length of time` values.

1. **Parties missing from `Party`** (a regulative rule needs a `Party` type, and each of these acts or bears a duty in the text):
   - the person to whom the offender is remanded for assessment (ss 752.1(2) and 753.01(2): "shall file a report"): declared as `s 752.1(2) party` with the constructor `s 752.1(2) the person to whom the offender is remanded`;
   - the applicant for an order reducing or terminating long-term supervision (s 753.2(4): "must give notice ... to the Attorney General"): `s 753.2(4) party`, `s 753.2(4) the applicant`;
   - the sheriff to whom a writ of fieri facias is delivered (s 772(1): "shall execute the writ"; also named in ss 766(3) and 773): `s 772 party`, `s 772 the sheriff to whom the writ is delivered`;
   - the person who is the subject of a writ of habeas corpus (s 774.1: "must appear in court in person"): `s 774.1 party`, `s 774.1 the person who is the subject of a writ of habeas corpus`.
2. **The extraordinary writs** (s 774 and s 784): a type with `certiorari`, `habeas corpus`, `mandamus`, `procedendo` and `prohibition`.
   Declared as `s 774 writ`, with a sixth constructor `s 774 another writ` for a case outside the five.
3. **A comparison of two `Length of time` values** (ss 752, 753.1(3), 755(2), 777(2)): the core declares the type and its constants but no "at least".
   Written as `s 752 the length of time is at least` in `ccc28-part24-s752.l4` and written again as `s 777(2) the length of time is at least` in `ccc28-part26-extraordinary-remedies.l4`, because every module of this part imports the core only.
4. **A `one year` constant** (`Length of time OF 1, 0, 0, FALSE`): the core has `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years` and `fourteen years` and no `one year`; this part writes the record inline where it needs a year.

## ccc29

Nothing here blocks anything: the part compiles and its tests are green without the core changing.
The items are types this part declared for itself, under its own prefix, because the core lacks them or has a type it did not use; the lead may hoist or merge them.
Each claim was checked on 2026-11-17 against `ccc-core.l4` (the `Party` type is declared at line 49, its constructors at lines 57-78; `Province or territory` at line 29) and against the part's modules.

## Party constructors the core lacks

The core's `Party` already has every constructor this part uses from it: `a justice`, `a provincial court judge`, `the court`, `the clerk of the court`, `the keeper of a prison`, `the prosecutor`, `the informant`, `the Attorney General of Canada`.
It has no constructor for the following, which this part declared for itself.

| wanted | the text | declared here |
| --- | --- | --- |
| `the minister of justice of a territory` | s 810.3(1), (2) and (4): "the Attorney General of a province or the minister of justice of a territory" (the core has `the Minister of Justice`, line 81, which is not a territory's minister) | a constructor of `s 810.3 designating authority` (`ccc29-xxviii-3-peace-810-21.l4` line 112), beside `s 810.3 the Attorney General of a province` and `s 810.3 a person authorized by the Attorney General or minister` |
| `the Attorney General of a province` | the same | the same type, `s 810.3 the Attorney General of a province`; it is also used as a regulative actor (`PARTY` of two rules in the same module); the core's `the Attorney General` (line 58, "as s 2 defines it, which varies with the proceeding") exists and could stand for it; the reason this part declared its own is not recorded |
| `the appellant`, `the respondent` | ss 813 to 840 | `s 815 party` with `s 815 the appellant` and `s 815 the respondent` (`ccc29-xxviii-4-appeal-812.l4` line 233); the kinds of appellant in s 813 are `s 813 appellant` (line 96) |

## Duplicate of a core type

The core's `Province or territory` (13 constructors) and this part's `s 812(1) province or territory` (13 constructors, `ccc29-xxviii-4-appeal-812.l4` line 26) name the same thirteen provinces and territories.
This part uses its own in modules 4, 5 and 7 (`ccc29-xxviii-4-appeal-812.l4`, `ccc29-xxviii-5-appeal-829.l4`, `ccc29-xxviii-7-schedules.l4`) and not in the seat.
The reason for declaring it is not recorded; it is a duplicate, not a need.
If the lead prefers one type, replace `s 812(1) province or territory` by the core's in those three files.

## Used without a constructor

"The person having the custody of the appellant" (ss 816(1.1) and 819(1)) names no office; the regulative rules use the core's `the keeper of a prison` for it (marginal reading M-1 in NOTES.md).

## ccc30

Written by part agent `ccc30` on 2026-11-13. Nothing below was added to `ccc-core.l4` (it is read-only in this sandbox). Each item is declared in the part's own module under its own prefix and used there.

1. **`Party`: a constructor for the person a demand, order or summons is addressed to.**
   Wanted: `the person to whom a demand, order or summons is addressed` (the Forms print "To (name of person)", "To A.B.", "To (name of financial institution, person or entity)").
   Why the existing constructors do not do: it is not `the accused` (a preservation demand or a production order goes to a third party, and Forms 5.041 and 5.061 go to a person who may have been found not criminally responsible), not `the offender` (same reason), not `a witness`, and not `an organization` (it may be an individual).
   Declared here as `forms 1 to 23 addressee` (one constructor, `forms 1 to 23 the person to whom the demand, order or summons is addressed`) in `ccc30-forms-actors.l4`. Used by the regulative rules of Forms 5.005, 5.0091, 5.041 and 5.061.
2. **`Process document`: members for the documents Forms 5.001 to 5.0091, 5.1 to 5.3, 8, 12 and 15 to 23 prescribe**, if the lead wants `forms 1 to 23 the process document the form prescribes` to answer them rather than `NOTHING`: a preservation demand, a preservation order, a keep-account-open order, a production order, a non-disclosure order, a warrant for committal, a warrant for a witness, a surety declaration, a report to a justice. The register answers `NOTHING` for them today (silent: the core's list has no member), which is the honest answer and is asserted.

## ccc31

The keel's files are read-only here, so none of these was added; each was met by the workaround named, and the lead may hoist the constructor into the core at the merge (the workaround is then a one-word change in the part's module).

## `Party` (the regulative actor)

- `the sheriff` (Forms 27 and 34: the warrant and the writ are addressed "To the sheriff of (territorial division)"). Workaround: `a peace officer` (a sheriff is a peace officer by paragraph (a) of the definition in s 2, line 140). Used in `form 27 the duties of the sheriff and the keeper` and `form 34 the duties of the sheriff`.
- `the keeper, administrator or warden of a prison, hospital or other place` (Forms 49 and 50: "the keeper (administrator, warden) of the (prison, hospital or other appropriate place)"). Workaround: `the keeper of a prison`. Used in `form 49 the duties of the peace officers and the keeper` and `form 50 the duty of the keeper`.
- `the addressee of an order to disclose income tax information` (Form 47, "To A.B., of , (office or occupation)"). Workaround: `a public officer`. Used in `form 47 the duty of the addressee`.
- `the chairperson of a Review Board` (the signatory of Forms 48.1, 49 and 50). Not used in a rule (the signature lines are wording).
- `a fingerprint examiner` (Forms 44 and 45, "a fingerprint examiner designated as such for the purposes of section 667"). Not used (the Forms are certificates: inert).
- `a person who collects information at a registration centre` and `the Canadian Forces Provost Marshal` (Forms 52 and 53, paragraph 5; Forms 52 to 54, paragraph 3). Not used (the functions take "the person is subject to the order" as the fact).

## A helper for counting a period

- `forms 24-54 the first day after a period that begins on a day` and `forms 24-54 the day falls within a period that begins on a day`, in `ccc31-forms-periods.l4`, count a `Length of time` from a day (fork F16 of NOTES.md). Other parts that count a term of years, months and days from a date will need the same; the lead may hoist it into the core (or a library module) under a name without the `forms 24-54` prefix.

## Nothing else

No type or constructor beyond these was needed: the `Provision of the Code` record carried the section tests of Forms 29, 29.1 and 32, and `Length of time` carried every period.

## ccc32

Part ccc32 declared these in its own modules, under its own prefix, because `ccc-core.l4` (read-only here) lacks them. The lead may hoist them into the core at the merge; each is a one-line change at the use site.

## Parties (the core's `Party` type)

| wanted constructor | used as | declared instead, in | why a core constructor would be better |
| --- | --- | --- | --- |
| `the Miscarriage of Justice Review Commission` | the party bound by the duties of Part XXI.1 as replaced by 2024, c. 33, s. 3 (ss 696.3(1), 696.4(1) and (5), 696.5(2) and (6), 696.6(1) and (7)) | `ccc32-nif-xxi1.l4`: `s 696.1 (not in force) the Commission` (type `s 696.1 (not in force) party`) | one cast for every regulative rule across parts; the Commission is also the party of ss 696.71 to 696.8 (other parts: ccc24 for the in-force Part XXI.1 held by the Minister) |
| `a medical practitioner or nurse practitioner` | the party bound by 2021, c. 2, s. 4 (medical assistance in dying, request made before royal assent) | `ccc32-related-2.l4`: `2021 c 2 s 4 a medical practitioner or nurse practitioner` (type `2021 c 2 s 4 party`) | the same people are the parties of ss 241.1 to 241.4 (ccc8) |
| `the relevant Attorney General` | the person the Commission must notify, with the applicant (ss 696.4(5), 696.5(2), (6), 696.6(7)) | not declared: the notice duties are encoded with the Commission as the only duty-bearer and the Attorney General named in the action's words | the core has `the Attorney General`; "the relevant Attorney General" is not defined in the text the part holds |
| `the applicant` (for review) | the person the Commission's duties run to | not declared: the applicant is the accused (the seat), named in the action's words | the core has `the accused` and `the offender`; an applicant may be neither (a person found not criminally responsible) |

## Records and enumerations

None needed. `Provision of the Code`, `Province or territory`, `Mode of proceeding`, `Class of offence`, `Punishment`, `Imprisonment`, `Fine`, `Length of time` and the constants `ten years` and `six months` are used as the core gives them (`Length of time` is read for `ten years` in s 264.01(4); `six months` is used only in tests).

## A suggestion, not a need

A second, FUTURE text of a provision (the "AMENDMENTS NOT IN FORCE" band) is carried here by the marker `(not in force)` in each name, because the core has no notion of a provision's version. If the merge wants one answer for "this section as it reads today" and "as it will read", a `Version of a provision` type in the core (in force, not in force with the amending provision named) would let a caller ask for either; this part has not built it.
