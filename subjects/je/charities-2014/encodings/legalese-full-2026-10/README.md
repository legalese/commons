# The Charities (Jersey) Law 2014 in L4 (draft)

This directory holds an encoding, in the L4 programming language for law, of the whole Charities (Jersey) Law 2014 (L.41/2014) as it reads on jerseylaw.je from 2 October 2026.
It was made in October 2026 by a fleet of AI agents: nine encoders, each taking part of the Law, and an integrator who joined the parts.
Three independent test authors then tested it from the Law alone, and two of the nine groups were repaired after their findings.
No lawyer has read it against the Law yet: treat it as a draft, not as legal advice.

Status on 2026-10-27: on `main` of the commons, pushed on the repository owner's instruction of that day.
It is still a draft: no lawyer has read it.

## What it answers

The integration layer (the `int-` files) answers six questions, each as an `@export` function that takes the day you are asking about:

1. May an application for registration be granted, and what must the Commissioner do (`Int (a) may the application be granted`)?
2. Is an entity a registered charity on a given day, and what does the register hold about it (`Int (b) is the entity a registered charity and what does the register hold`)?
3. What follows from a contravention of the Law or a reportable matter (`Int (c) what follows from the contravention`, with four rules for the Commissioner's, the court's and a governor's duties and powers)?
4. What offence does an act make out, and what penalty does it carry, including the officer who connived and the cap in Schedule 2 (`Int (d) the offence and the penalty for the act`)?
5. Which text of the Law is in force on a day or at an instant, and which Parts, Articles and Schedules are (`Int (e) ...`)?
6. Who may appeal which decision to the Charity Tribunal, and by when (`Int (f) ...`)?

A question asked about a day on which the Articles it rests on were not yet in force, or before the first consolidated text of 1 January 2019, is refused with a named reason and not answered.
Where the Law can be read more than one way (136 places, called forks) the encoding takes one reading and keeps the others callable; NOTES.md lists them all.

## How to run it

You need the `l4` binary the fleet used (its sha256 is in `check.sh`), and you should leave `JL4_LIBRARY_PATH` unset.
`l4 run int-tests-chains.l4` runs one whole history across the headlines; `l4 run <any module>.l4` runs the tests of a module.
`./check.sh` runs everything (about seven minutes), checks the two hashes, the quotations against the Law's text, the traces and the shape of the import graph, and prints GREEN or RED.
It expects `../bin/l4` beside this directory, or the `L4` environment variable; in the commons set `L4` to the prerelease `unstable-20261026-6325439` (darwin-arm64) from `legalese/prereleases`, whose binary hash is pinned in `check.sh`. It finds the Law's text in `../../source/` (or in `RAW`).

## What is here

- `NOTES.md`: scope, layout, the integration points, coverage, the 136 forks, the places where the groups disagree, the contradictions found in the Law, the open questions for an expert, the answer table, what `check.sh` prints, and the defects found.
  Read this first.
- `domain.l4`: the shared nouns.
- `g1-*.l4` to `g9-*.l4`: the nine groups' modules and tests, and `FRAGMENT-G1.md` to `FRAGMENT-G9.md`, their own records.
- `int-*.l4`: the integration layer and its tests.
- `ind-a-*.l4`, `ind-b-*.l4`, `ind-c-*.l4`: the independent test authors' tests, merged into the row; NOTES.md section 12 says which were decided before the encoding was opened and which were not.
- `check.sh`, `check-traces.py`, `srcrefs.py`: the self-check.
- `coverage-all.tsv`: the 851 provisions of the Law, each with its disposition and module.
- `encoding.json`, `SOURCE-LICENSE.md`.
- `OVERLAP.md`, `COMPARISON.md`, `TRIAGE.md`: how the hunt, the survey and the encoders' contradiction lists overlap; the comparison with the July corpus and the Articles 5 to 7 cleanroom; and the triage of the independent authors' and the integrator's findings.
- `INDEPENDENT-ind-a-expectations.md`, `-b-`, `-c-`: the independent authors' expectations as they froze them, before opening the encoding.
- `survey/`, `hunt/`: the survey plan and coverage table, and the blind contradiction hunt.
- `provenance/`, `tools/`: the brief and every assignment the agents were given, and the scripts used (these name scratch directories of the run; they are a record, not a toolchain).
- `../../source/`: the sources (the Law's page twice, the PDF, the text extracts, the amending instruments).

## Limits

The subordinate legislation made under the Law is not encoded, nor are the other enactments it mentions; what they decide is an input.
Any amendment after 2 October 2026 is not known.
Some tests are meant to fail or to refuse: they state what the Law seems to say where the readings taken do not deliver it, or the reading an independent author took where the Law is ambiguous, and `check.sh` lists the number of failures and of refusals it expects for each file.
The source text is licensed under the Open States Assembly Licence – Jersey v1.0; see `SOURCE-LICENSE.md` for the attribution that licence requires.
