# Encoding brief: the Carer Recognition Act 2010 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Carer Recognition Act 2010** (No. 123, 2010), Commonwealth of Australia, as made, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2010A00123.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the carer**: the individual who gives care, support and assistance to another (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the carer's words: *"Am I a carer under this Act? Must the government agency dealing with me have regard to the Statement for Australia's Carers, and consult carers about care supports? Can I enforce any of this, or challenge a decision because the agency did not comply?"*

In scope: s 4 (the definitions of public service agency, public service care agency and associated provider, so far as they decide what an agency must do), s 5 (meaning of carer), ss 7-9 (the agencies' and providers' obligations) and s 10 (no legally enforceable rights). Out of scope: s 6 and Schedule 1 (the Statement's text, which is inert principle), s 8(3)-(4) (annual reporting), ss 11-12.

## Inputs

- What I provide: personal care, support and assistance to another individual who needs it because of disability, a medical condition (including a terminal or chronic illness), a mental illness, or being frail and aged (both).
- Whether I do it under a contract of service or for services, as voluntary work for a charitable, welfare or community organisation, or as part of a course of education or training.
- Whether the body I deal with is a public service agency, whether it is responsible for care supports (a public service care agency), or an associated provider (under a contract or funding arrangement, direct or through a subcontract, with a public service care agency for care supports, not with a State or Territory).

## Rules that matter

- s 5(3): being a relative, guardian or co-resident does not of itself make someone a carer; the encoding asks for the care actually given.
- Encode isomorphically, with an `@ref` on every rule.
- `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`carer-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
