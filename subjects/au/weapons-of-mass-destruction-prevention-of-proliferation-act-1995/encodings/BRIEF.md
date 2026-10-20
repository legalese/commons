# Encoding brief: the Weapons of Mass Destruction (Prevention of Proliferation) Act 1995 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Weapons of Mass Destruction (Prevention of Proliferation) Act 1995** (No. 38, 1995), Commonwealth of Australia, compilation No. 8 of 6 November 2018, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A04891.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person who supplies goods, exports goods or provides services** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is what I am doing an offence because it may help a weapons of mass destruction program? What is the most I can get? Are my goods forfeited? Until when does a prohibition notice from the Minister bind me?"*

In scope: s 6(3), ss 9-11, s 12 (the Minister's written all-clear, as an input), s 13 (a permit, as an input), s 14(2), (4), (6), s 17(1). Out of scope: ss 1-5, 6(1)-(2), (4), 7-8A, 13 (the Minister's decision), 14(1), (3), (5), 15-16, 17(2) onwards.

## Inputs

- My dealing: supplying goods to another person; exporting goods that are not prohibited exports under the Customs Act; providing services to another person.
- Who and where: acting in Australia or an external Territory; abroad as an Australian citizen, resident or body incorporated in Australia; abroad, anyone else.
- Whether I believe or suspect on reasonable grounds that it may help a WMD program.
- Whether a permit authorises it and I keep its conditions; whether the Minister told me in writing there is no reason to believe or suspect so (s 12).
- A s 14 notice (none; prohibiting; allowing only on conditions), whether I comply with its conditions, whether I know of the contravention, when it was given and whether revoked; the day I deal.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`wmd-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
