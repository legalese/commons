# Encoding brief: the Epidemiological Studies (Confidentiality) Act 1981 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Epidemiological Studies (Confidentiality) Act 1981** (No. 148, 1981), Commonwealth of Australia, compilation No. 4 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A02525.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person who helps conduct a study**: who conducts, supervises or assists in it (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"May I record or pass on what I learned about someone through the study? What is the most I can be punished? Can a court make me produce it? Must I take an oath of secrecy?"*

In scope: s 3 (prescribed study, assisting, affairs), ss 4-11. Out of scope: s 3A (the Criminal Code's fault rules), s 12 (application to earlier information, which is assumed), s 13.

## Inputs

- The study: the Vietnam Veterans Study, a Commonwealth study declared by regulation, or another study.
- My part: conducting, supervising or assisting (in any capacity, paid or not: s 9), or only as a subject or someone who gave information about a subject (s 3(2)).
- How I got the information: by assisting in the study; by access to another study's document under a s 5 authorisation; otherwise. Whether it concerns another person's affairs.
- What I do: make a record; divulge or communicate; give a person assisting another prescribed study access to a document. Whether it is for the purpose of conducting the study.
- To whom (s 7); whether the access follows the Minister's written authorisation (s 5); whether it is published non-identifying conclusions, statistics or procedures (s 11); whether the Minister requires an oath (s 10).

## Rules that matter

- The penalty is imprisonment for 6 months or 10 penalty units.
- Where the Act does not say whether a court can compel production, the answer is NOTHING.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`esc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
