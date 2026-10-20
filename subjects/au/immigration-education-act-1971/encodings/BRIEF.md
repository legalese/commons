# Encoding brief: the Immigration (Education) Act 1971 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Immigration (Education) Act 1971** (No. 3, 1971), Commonwealth of Australia, compilation No. 11 of 19 April 2021, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1971A00003.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the migrant seeking English tuition** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the migrant's words: *"Am I eligible for English tuition under the Act? Must the Minister provide it to me? By when must I register with a provider and start a course, and when does my eligibility end?"*

In scope: s 3 (visa commencement day), ss 4A, 4B(1), 4C(1)-(2), (5), 4D(1)-(2), (5) (extensions as inputs). Out of scope: ss 1-2, 4, 4E-13 (provision of courses, citizenship courses, implementation, delegation, reports, regulations). Which temporary visas are specified, vocational English and the extensions are inputs.

## Inputs

- My status: in Australia on a permanent visa; on a specified temporary visa; a former permanent visa or entry permit holder now a citizen; under 18 with a parent who holds or held a permanent visa or entry permit; none.
- Whether I have vocational English; my date of birth; my visa commencement day.
- For s 4B: whether I paid or am exempt from the visa application charge; whether I held another permanent visa in Australia before; whether the regulations exclude me.
- The day I registered with a provider, and started an approved course; any extensions granted (in days) to register, to start, and for tuition; the day asked about.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`ie-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
