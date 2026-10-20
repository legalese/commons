# Encoding brief: the War Crimes Act 1945 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**War Crimes Act 1945** (No. 48, 1945), Commonwealth of Australia, compilation No. 5 of 23 May 2018, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1945A00048.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person accused of a war crime** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the accused's words: *"Is what I am said to have done a serious crime, and a war crime, under the Act? Can I be charged? What is the most I can get? Is it a defence that the laws of war permitted it, or that I was ordered to do it?"*

In scope: s 5 (war), s 6, s 7, s 9(1), s 10, s 11, s 16, s 17(2). Out of scope: ss 1-4, 8, 9(2)-(3), 12-15, 17(3)-(5), 18 onwards (procedure, venue, alternative verdicts). Whether an act was an offence under the law then in force in part of Australia (allowing any defence under that law) is an input.

## Inputs

- The act: a listed violent offence or a variant or complicity in one; deportation or internment in a death camp, slave labour camp or like place, or complicity; another act. Whether it was such an offence under the law then in force in part of Australia.
- The connection with the war or occupation (hostilities; occupation; a war or occupation policy; on behalf of a power at war; persecution or genocide in a country at war or occupied; only incidental or remote).
- Whether it was in Europe; the day it was done; whether it involved the wilful killing of a person.
- Whether I am an Australian citizen or resident.
- Whether the act was permitted by the laws, customs and usages of war, and whether it was a crime against humanity under international law.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`wc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
