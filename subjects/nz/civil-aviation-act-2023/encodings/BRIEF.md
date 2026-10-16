# Encoding brief: the Civil Aviation Act 2023 (New Zealand), domestic carriage and passenger delay, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Civil Aviation Act 2023**: New Zealand, Public Act 2023 No 10. The source is the version as at 23 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2023_10.txt` (sha256 `e2eb3eee20f8475142659f0a4b15f9d6830934eb981edf3f69aaa8541e4e2e0d`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**What the conversion loses.** Paragraph labels. Within the scope below, nothing computable is lost.

## Scope: passenger compensation for delay in domestic carriage (Part 5, the subpart on carriage by air within New Zealand)

- **Application**: s 270 (departure and destination in New Zealand with no agreed stopping place outside it; not international carriage), s 271 (combined carriage: only the air part), s 272 (excluded flights: a single flight returning to its departure point, and flights excluded by regulations).
- **Who is liable**: s 273 (contracting and actual carriers), s 275 (successive carriers: the one performing the stage where the delay occurred).
- **Liability for delay**: s 274 (liable, unless the delay arose from weather, air traffic control instructions, lawful orders, force majeure, or saving life), s 276 (no liability if all necessary measures were taken or impossible).
- **Limit**: s 277 (the lesser of the damage proved and 10 times the sum paid; raised by special contract), s 278 (no contracting out, except for stricter duties or better remedies), s 279 (no limit for intentional or reckless damage).
- **Time limits**: s 281(2) (contribution proceedings within 2 years after judgment), s 283 (actions within 2 years after the later of arrival, or — if no arrival — the day it ought to have arrived or the carriage stopped).

International carriage (the Montreal and Warsaw Conventions under ss 257-268) is out of scope.

## The top-level goal, and the goals under it

Top level: *for a passenger's claim for delay: does the domestic subpart apply, which carrier is liable, is the carrier liable at all, what is the most it must pay, and by when must the action be brought?*

1. **Application and carriers**: ss 270-273, 275.
2. **Liability and its limit**: ss 274, 276-279.
3. **Time limits**: ss 281(2), 283.

Inputs, not worked out: the contract's places and stopping places, the flight's route, the carriers and stages, the cause of the delay, the measures taken, the damage proved, the sum paid, any special contract, the carrier's intent or recklessness, and the dates.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`caa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
