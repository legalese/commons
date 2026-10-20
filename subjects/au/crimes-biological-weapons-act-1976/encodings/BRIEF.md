# Encoding brief: the Crimes (Biological Weapons) Act 1976 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Crimes (Biological Weapons) Act 1976** (No. 11 of 1977), Commonwealth of Australia, compilation No. 9 of 11 May 2018, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A01649.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person who develops, produces, stockpiles, acquires or retains biological agents, toxins or weapons, or is charged** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is what I do unlawful, and what is the most I can get? Is my material forfeited, and how long can the police hold it after seizure? Can I be committed for trial? Can an analyst's certificate be used against me, and by when must I ask for the analyst to be called?"*

In scope: s 5, s 8, s 9(1)-(2), s 10(3)-(4), s 12(4), (6)(a). Out of scope: ss 1-4, 6-7, s 9(3)-(4), s 10(1)-(2), (5), s 11, s 12(1)-(3), (5), (6)(b), s 13, and the Convention in the Schedule (whose terms carry their meaning into s 8 but are not separately encoded).

## Inputs

- Whether I am a natural person or a corporation; whether I am an Australian citizen; whether I act in Australia (or an external Territory) or outside it.
- What I hold: agents or toxins with no peaceful justification; weapons, equipment or means of delivery for them; agents or toxins justified for peaceful purposes. Whether I develop, produce, stockpile, acquire or retain it.
- The day it was seized; whether a prosecution was instituted within the 60 days.
- Whether the Attorney-General has consented in writing.
- Whether I was given the analyst's certificate with reasonable notice; the day of the hearing at which I want the analyst called.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`cbw-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
