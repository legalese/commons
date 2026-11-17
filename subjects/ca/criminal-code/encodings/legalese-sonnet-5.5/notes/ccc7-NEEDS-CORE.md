# NEEDS-CORE.md (ccc7: Criminal Code (Canada), Part VI, ss 183 to 196.1)

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
