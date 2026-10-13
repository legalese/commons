## 10. Provenance of this run (added by the launching session, not by the encoder)

Everything above this heading was written by the encoder.
This section was added afterwards by the Claude Code session that launched and checked the run, on 2026-10-13.

**How the row was made.**
One Claude Sonnet 5.5 agent (Agent tool, `model: sonnet`, default effort), working alone in a cleanroom from `BRIEF.md` in this directory, which is THERMOSTAT's brief for this subject with the paths updated.
No ontology agent, no section fleet, no integrator, no independent test author, no refuters.
Its transcript runs 2026-10-13 09:19Z to 10:06Z (17:19 to 18:06 +08), 47 minutes.
The transcript records 242 requests, all on `claude-sonnet-5-5`, 40,221 output tokens, 2,501,346 cache-write and 103,908,000 cache-read tokens, with a peak context of 671,177 tokens.
Dollar cost is not computed here.

**The binary.**
`/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-41dd7a67/bin/l4`, built 2026-10-13 16:13 from l4-ide `unstable`, sha256 `2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187`.
`l4` has no `--version`, so the hash is the identity.
`JL4_LIBRARY_PATH` was unset.

**What the launching session re-ran, rather than taking from the encoder's report.**
`check.sh` with that binary printed the same table the encoder reported: 13 modules, 281 assertions satisfied (72 in `hvac-tests-fees.l4`, 187 in `hvac-tests-law.l4`, 22 in `hvac-tests-simplex.l4`), 0 refused, and 7 failed in `hvac-tests-red.l4`, all 7 expected.
The `#ASSERT` directive counts in those four files are 72, 187, 22 and 7, so no assertion is double-counted or missing.
No module emits a warning.
The 19 `#TRACE` directives are not counted by `check.sh`; the encoder says it read their results, and the launching session did not re-read them.

**Checked against the sources by the launching session.**
Section 4's as-made and as-amended columns, cell by cell, against Kovetz HaTakanot 11951 and 12383 (194, 40 on top of the exam fee, 284 for receiving a licence, 398 for the foreign-expert request, 158 for the theory exam, the objection fee reaching the theory exam only, and no commencement provision in 12383).
The draft column was checked only for 273, 40 and 398, against our own notes of the screenshot, not against the image.
Section 8 was probed: a licence given 2025-09-01 ends 2030-03-31, and one given 2025-01-15 ends 2030-01-15.

**Cleanroom, and what it was not.**
The brief forbade reading any other encoding of this subject.
The encoder's transcript was audited afterwards: its Read, Glob and Grep calls touch only its own `inputs/` and `crops/` directories and the `encoding-a-subject` and `writing-l4-rules` skills, and no tool call names `commons`, `commonswt`, `canon` or `il`.
It read no `example-brief.md`; its one read of `canon-deposit.md` is the only skill file it opened that names this subject's `legalese` row.
Three leaks were not closed: the launching session's memory index, which names this subject, was in the encoder's context; the encoder reports that the harness reset its working directory repeatedly into two directories the brief forbids (not checked here); and `canon-deposit.md` points at our `legalese` row as a worked example.
The encoder reports it followed none of them, and its transcript shows no read through any of them.

**Tooling kept with the row.**
The `.l4` files are generated: `build/build.py` expands `@@Q` placeholders in `build/src/*.l4.in` into mechanically quoted Hebrew comments using `build/quote.py`, and `build/make_notes.py` with `build/notes_template.md` produced the first nine sections of this file.
They read `inputs/` and write `deposit/` in the encoder's working directory, so they do not run from here without recreating that layout.
Edit the `.l4.in` files and regenerate, not the `.l4` files.

**Not done.**
No independent test pass: the 288 assertions share the encoder's one reading of the sources.
No Hebrew `@nlg:he` heralds (the brief made them optional).
No domain expert has read this row; gate HG1 is not sought.
