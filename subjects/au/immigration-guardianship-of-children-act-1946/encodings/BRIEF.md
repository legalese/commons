# Encoding brief: the Immigration (Guardianship of Children) Act 1946 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Immigration (Guardianship of Children) Act 1946** (No. 45, 1946), Commonwealth of Australia, compilation No. 14 of 14 October 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1946A00045.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the child who enters Australia to settle, and the adult who brings, cares for or deals with them** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in their words: *"Is this child a non-citizen child under the Act? Is the Minister the child's guardian, and until when? May the child leave Australia? Is what I do an offence? By when must I ask the Minister to reconsider a decision, and by when must the Minister decide?"*

In scope: s 4 (relative, parent), s 4AAA, s 4AA (as a direction already made), s 6, s 6A, s 9, s 11 (an exemption, as an input), s 11A(2)-(4). Out of scope: ss 1-3, 4AAB, 4AAC, 4A, 5, 7, 8, 10, 11A(1), (5)-(6), 12.

## Inputs

- Whether the child entered Australia as a non-citizen; the child's date of birth; the day asked about; whether the child intends, or is intended, to become a permanent resident.
- With whom the child entered: a parent; a relative aged 21 or over other than a parent; an intending adoptive parent; another adult aged 21 or over; no one. Whether an adoption class visa was in force on entry and the adult will live with the child in a declared State or Territory.
- Whether the Minister has directed that the child is the Minister's ward; whether the child has left Australia permanently; whether the Minister has exempted the child.
- My act: helping the child leave without the Minister's consent; removing or enticing the child from the custodian; knowingly harbouring or concealing the child; none. Whether I have a lawful excuse.
- The day the decision came to my notice; the day the Minister received my request.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`igc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
