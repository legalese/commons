# Encoding brief: the Defence (Parliamentary Candidates) Act 1969 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Defence (Parliamentary Candidates) Act 1969** (No. 60, 1969), Commonwealth of Australia, compilation No. 9 of 1 July 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1969A00060.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the member of the Defence Force who wants to stand for election** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"How do I leave the Defence Force to stand? By when must I apply to come back? If I lose and do not apply, what happens? Does my time away count? Must I repay my gratuity?"*

In scope: s 6 (the declared date), ss 7-9, ss 10-12 (reinstatement, so far as they concern the time limit, rank and long service leave), ss 13-14, s 17. Out of scope: ss 1-5, 15-16, 18-22 (machinery, travel and removals, service of notice, delegation, regulations).

## Inputs

- My service: a permanent officer; a permanent enlisted member; a Reserve member on continuous full-time service; another member.
- Whether the Chief of the Defence Force is satisfied I intend to stand; whether I have left under the Act.
- The declared date (the Minister's notice under s 6); whether I was elected.
- The day I applied for reinstatement; whether the Chief allowed a further period.
- The day the Chief served notice requiring me to apply (ss 13-14).
- Whether I have been reinstated; the gratuity or bounty paid to me on leaving.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dpc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
