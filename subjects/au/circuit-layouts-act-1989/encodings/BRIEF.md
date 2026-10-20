# Encoding brief: the Circuit Layouts Act 1989 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Circuit Layouts Act 1989** (No. 28, 1989), Commonwealth of Australia, the compilation prepared on 12 October 2012, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A03776.txt` (CC BY 4.0). Part II commenced on a day fixed by Proclamation; the day is not in the deposited text and is an input.

## Seat

The encoding is written from the seat of **the person who copies a circuit layout, makes an integrated circuit to it, or commercially exploits it in Australia** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is this layout protected, and until when? Does what I am doing infringe the EL rights? Can an action be brought against me, can damages be awarded or only an account of profits, and until when can I be sued?"*

In scope: s 5 (eligible layout, eligible person, protection period), ss 6-7, s 10(b), s 11, s 17, s 19, ss 20-25 (the exceptions; s 25 as one input), s 27(2)-(3), s 28. Out of scope: ownership and dealings (ss 16, 18, 44-45), procedure and exclusive licensees (ss 26, 29-41, 43, 47), s 42, s 46 (groundless threats), s 48.

## Inputs

- The day the layout was made; the year it was first commercially exploited (if any); whether its making involved a creative contribution; whether it was commonplace; whether the maker was an eligible person when it was made; whether it was first commercially exploited in Australia or an eligible foreign country.
- My act: copying the layout; making an integrated circuit to it; commercially exploiting the layout, a copy or a circuit in Australia. The day I do it. Whether I have the owner's licence; whether I know or ought reasonably to know I am not licensed.
- My purpose: trade or another; my private use; research or teaching; evaluating or analysing the layout. Whether private copies are exploited or distributed to the owner's prejudice (s 21(2)).
- s 20: whether I acquired the circuit innocently; whether I have since become aware or could reasonably be expected to; whether I pay equitable remuneration.
- s 24: whether I acquired it through the owner's own or licensed commercial exploitation. s 25: whether I act for the Commonwealth for defence or security after it failed to obtain a licence.
- s 27(3): whether I was not aware and had no reasonable grounds to suspect the act infringed.
- The day Part II commenced.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`cla-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
