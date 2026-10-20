# Encoding brief: the Diplomatic and Consular Missions Act 1978 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Diplomatic and Consular Missions Act 1978** (No. 98, 1978), Commonwealth of Australia, compilation No. 5 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A01897.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person who displays a sign, flag or insignia, or makes a representation**, about a diplomatic or consular presence in Australia (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is my sign or claim caught by the Act? Can the Federal Court restrain me by injunction? Can my sign be taken down under a warrant, and until when can that warrant be in force?"*

In scope: s 4(1), (2), (2A), (2B), (5), (6), s 5(1) and (5). Out of scope: s 3A, s 4(3)-(4), (7), s 5(2)-(4), (6)-(7), s 6 (certificates, which are evidence), s 7.

## Inputs

- The mission the conduct concerns: a diplomatic or consular mission of a country established in Australia with the Commonwealth's consent; a designated overseas mission of a foreign territory; none.
- My conduct: displaying a sign, flag or insignia (or causing or permitting it); making or publishing a representation (or causing or permitting it).
- Whether the premises are the mission's office or a member's residence; whether the sign or representation states, implies or is reasonably capable of being taken to imply another mission representing that country or territory.
- Whether I act for a designated overseas mission in an authorised capacity (or at its staff's request); whether I act for a consented diplomatic or consular mission in that capacity (or at a member's request).
- The Court's findings: that I have engaged in the conduct; that I am likely to.
- The day a removal warrant was issued, if any.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dcm-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
