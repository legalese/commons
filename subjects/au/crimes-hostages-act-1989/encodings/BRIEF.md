# Encoding brief: the Crimes (Hostages) Act 1989 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Crimes (Hostages) Act 1989** (No. 26, 1989), Commonwealth of Australia, compilation No. 6 of 10 March 2016, with the International Convention Against the Taking of Hostages in its Schedule, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A03774.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person accused of hostage-taking** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is what I did hostage-taking under the Act, and an offence? Can I be charged in Australia? Can I be convicted when I have already been convicted abroad? What must happen before I am committed for trial? If the venue is changed, by when must I reappear?"*

In scope: s 6(2), s 7, s 8, s 9, s 10(1)-(2), s 12(1), and Article 12 of the Convention as s 9(1) applies it. Out of scope: ss 1-5, 6(1), 6A, 10(3), 11, 12(2)-(7), 13-15 and the rest of the Convention. The day the Convention entered into force for Australia is an input (s 13 provides for a certificate).

## Inputs

- s 7: whether I seized or detained another; whether I threatened to kill, injure or keep detaining them; whether I intended to compel an institution, organisation or person to act or abstain as a condition of release.
- The day of the act; the day the Convention entered into force for Australia.
- Where: in Australia; on an Australian ship or aircraft; elsewhere. Whether I was an Australian citizen then; whether I am present in Australia; whether the aim was to compel an Australian institution.
- Whether the Geneva Conventions apply to it in an armed conflict (Article 12); whether the act, I and the hostage are all of one State where I now am other than by extradition (s 9(2)-(3)).
- Whether I have been convicted abroad for the same conduct; whether the Attorney-General has consented; the day of any change of venue order.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`ch-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
