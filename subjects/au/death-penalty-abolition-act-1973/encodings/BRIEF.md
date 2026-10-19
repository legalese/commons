# Encoding brief: the Death Penalty Abolition Act 1973 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Death Penalty Abolition Act 1973** (Act No. 100 of 1973), Commonwealth of Australia. The source is the compilation prepared on 19 April 2010 (amendments up to Act No. 37 of 2010), from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A00004.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person charged with, or convicted of, an offence** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Can I be sentenced to death for this offence; and if the law I am charged under provides for death, what is the penalty instead?"*

The whole operative Act is in scope: ss 3 (application), 4 (abolition), 5 (substitution of imprisonment for life) and 6 (death penalty must not be imposed). Sections 1-2 are machinery.

- s 4 and s 5 apply to offences under the laws of the Commonwealth and of the Territories and, so far as the Parliament's powers permit, Imperial Acts (s 3(2)).
- s 6 applies to those offences and also to offences under the laws of the States (s 3(3)).
- s 3(4): offences committed before, on or after commencement; the date of the offence does not matter.
- For a State offence, s 5 does not apply: the Act forbids the death penalty but does not say what penalty replaces it (that is for the State's law).
- For any other law (a foreign law, say), the Act does not answer.

## Inputs

- Which law creates the offence: Commonwealth, Territory, Imperial Act within the Parliament's powers, State, or other.
- Whether that law provides that a person is liable to death.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, give NOTHING (or `REFUSE`); never `FALSE`.
- `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dpa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
