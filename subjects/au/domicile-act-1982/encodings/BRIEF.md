# Encoding brief: the Domicile Act 1982 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Domicile Act 1982** (No. 1, 1982), Commonwealth of Australia, compilation No. 4 of 25 January 2019, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A02560.txt` (CC BY 4.0). It commenced on 1 July 1982 (endnote 3).

## Seat

The encoding is written from the seat of **the person whose domicile is in question** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"At this date, can I have a domicile of my own? As a child, whose domicile do I take? Do I keep it after I stop being a child? Have I acquired a domicile of choice in this country? Does my domicile follow my husband's, and does my domicile of origin revive if I give up my domicile of choice?"*

In scope: s 4 (child), s 5(1)-(2) (before and after commencement), ss 6-10. Out of scope: s 3 (object and application; the encoding assumes the question arises under Commonwealth or applicable Territory law), s 5(3) (jurisdiction), s 11 (union: the closest connection is a finding), s 12 (evidence), s 13 (regulations).

## Inputs

- The time asked about; my date of birth; whether I am or have been married; whether I cannot acquire a domicile because of mental incapacity (s 8(2)).
- Where my principal home is (with one parent, both, neither); whether my parents live separately and apart; whether I have another living parent; whether the parent whose domicile I follow has died.
- Whether I was adopted, by 2 parents or 1, and whether the adoption has been rescinded.
- Whether I had a domicile under s 9(1) or (2) when I ceased to be a child.
- Whether I reside in the country, and whether I intend to make my home there indefinitely.

## Rules that matter

- Where the Act does not answer (before 1 July 1982, mental incapacity, cases left to the common law), the answer is NOTHING, never FALSE.
- A person attains 18 on the 18th anniversary of birth.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dom-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
