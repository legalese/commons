FLEET_DIR = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full
L4_BIN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4  (sha256 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475; leave JL4_LIBRARY_PATH unset; run it under `nice -n 15`; at most two l4 processes at once; stop only processes you started, by PID, never by pattern)

# ASSIGNMENT: INTEGRATOR (prefix `int-`)

Nine encoders (G1 to G9) have each encoded one group of the Charities (Jersey) Law 2014 in L4, in parallel, in FLEET_DIR/deposit/.
Each re-ran green when I (the fleet lead) re-ran it in a clean copy: 5,235 assertions satisfied in all, plus 133 that are meant to fail and are refused (G2 14, G3 12, G4 14, G5 16, G6 24, G7 15, G8 19, G9 19, each in its `gN-tests-red.l4`; G1 has no red module).
No group imports another group, by design: every fact one group needs from another is a `GIVEN` under a standard name (PLAN section (c), integration points IP1 to IP35).

YOU turn nine groups into one row.
Your WORK directory is FLEET_DIR/work/integrator/ (create it).
You write in DEPOSIT only files with the prefix `int-`, plus `check.sh`, `check-traces.py`, `srcrefs.py`, `encoding.json`, `SOURCE-LICENSE.md`, `NOTES.md`, `README.md` (a short one, for a human), `coverage-all.tsv`, and a single ADDITIVE edit allowance for `domain.l4` (below).
**Develop each `int-` module in WORK and copy it into DEPOSIT only once it checks clean there**: three Opus test authors are taking snapshots of DEPOSIT while you work, and a half-written module in DEPOSIT would land in their snapshots.

## Read first
1. FLEET_DIR/BRIEF.md in full (the cleanroom rules and the rulings bind you as well).
2. The two skills' parts the brief names, especially encoding-a-subject steps 9 and 11, `references/canon-deposit.md`, and `assets/check.sh`.
3. FLEET_DIR/phase1/PLAN.md sections (b), (c) in full, (d), (e), 9 and 10, and the head of (f).
4. In each of the nine FRAGMENT-Gk.md files in DEPOSIT: the sections "Nouns requests for the INTEGRATOR", "Standard inputs consumed and functions exported", and the fork register (`grep -n '^\*\*F' FRAGMENT-Gk.md`); read the rest of a FRAGMENT where a wiring question needs it.
5. FLEET_DIR/deposit/domain.l4.
6. Then the exported rules of the group modules you wire (open them; do not rely on the FRAGMENT's list alone).

## What to do
1. **Wire the integration points.** Write `int-` modules that import the group modules they wire (imports across groups are allowed in YOUR modules, and only in yours) and supply each group's `GIVEN` inputs from the deciding group's functions.
   The table is PLAN section (c): IP1 to IP35.
   The ones that need most care: IP2 to IP4 (the vintage of the text, the office of the Minister, whether a unit of the Law is in force on a day; G7 and G1), IP5 to IP7 (the entity and the registered charity records), IP8 to IP11 (charity test, purposes), IP12 to IP14 (misconduct, contravention), IP15 to IP18 and IP22 to IP24 (what bars or permits registration; G4, G6, G3), IP19 to IP21 (required steps notices, organized religion, reportable matters), IP25 to IP29, IP30 (penalties), IP31 to IP35 (the readings of "year" and of a term of imprisonment, which several groups must take from ONE value, and the date a notice is served).
   Where the PLAN's input name and the encoder's actual exported name differ, the encoder's file governs; adapt in your wrapper.
   Do NOT edit any `g1-` to `g9-` module, test or fragment: if you find a defect in one, record it under "Defects found in group modules" in NOTES with the file, rule and a failing example, and tell me in your final report.
2. **Headline end-to-end functions** (`@export` with `@desc` on every `GIVEN` where the language allows; a function-typed parameter cannot be exported), each wrapped so that it answers REFUSE (a named reason) when the unit of the Law it rests on is not in force on the day (IP4):
   (a) may this application be granted (Article 11(4) with the charity test, the Jersey and address requirements, the name, the fitness bars of Article 19(9)(c) and the court order of Article 20(1)(c), the completeness of the application);
   (b) is this entity a registered charity on this day, and what does the register hold about it;
   (c) what follows from this contravention or this reportable matter (the Commissioner's powers: required steps notice, deregistration, application to the court; the governors' duties);
   (d) the offence and the penalty for this act, with the officer-of-a-body liability of Article 37 and the cap in Schedule 2 paragraph 4(3)(f);
   (e) which text of the Law is in force on a day (the vintage, the Minister, paragraph (ba) of Article 2(1)) and which Parts, Articles and Schedules are in force;
   (f) who may appeal to the Tribunal against which decision, and by when (Article 33 with the dates fixed by Article 38).
   Each returns an answer or a named REFUSE with a reason, never a default.
3. **Integration tests** in `int-tests-*.l4`: at least twenty whole scenarios that cross three or more groups (for example: an entity applies; the charity test is met; a governor has a reported fitness issue that bars the grant; the application is refused; the refusal is appealed within the period; or: a charity registered under the 2019 text fails to file its annual return, a required steps notice is served and not complied with, the Commissioner deregisters, the deregistration has the effects of Article 17, and an offence under Article 21 is priced).
   Decide each expected value BY HAND from the source text and write it down before you run; never copy what the code printed.
   A failing assertion is a finding: keep it failing in `int-tests-red.l4`, count it, list it.
4. **The cross-group consistency register** (a section of NOTES, and the most valuable thing you do): list every question that two or more groups answered, and where they answered it differently or by a different convention.
   Examine first: the day-counting convention for periods (is the day of the event inside the period? G3's F3.4 takes it as not counted; read G5, G6, G7, G8 and G9 and the `daydate` library's functions the way each group uses them); the meaning of "year" (IP33: G3 and G5 must take one value); the unit of a term of imprisonment (IP35: G6, G7, G8, G9); how each group decides "a registered charity" (the historic section is excluded: T7, T16); "Minister" (T3, T4); inclusive or exclusive limits ("not more than", "at least", "more than"); and what each group does when the Law says "the Commissioner is satisfied" or "in the opinion of".
   Do not silently harmonise: record both, wire the fleet default of the brief, and where the two differ in an answer give the alternative a callable function and a test.
5. **Nouns requests:** move each into `domain.l4` ONLY if the change is purely additive: a NEW type is allowed; a new field on an existing record is NOT (it breaks every construction of that record), and a new constructor on an existing enumeration is NOT unless you have checked that no existing `CONSIDER` becomes non-exhaustive.
   Otherwise define the noun in an `int-` module.
   List every edit to domain.l4 (its sha256 now is af1703908b8f62922ed36a9984104231b93b41703deec7c1e45f1fef84399d66) and, if you edit it, re-run ALL nine groups' check and show zero regressions (the numbers above).
6. **check.sh** (from the skill's `assets/check.sh`, with `expected_failed` set to the per-file counts above and your own), which also: verifies `domain.l4` by sha256 (updated if you edit it); verifies the l4 binary by sha256; fails on any warning; runs `srcrefs.py check --refs` over every module as the encoders did (see their FRAGMENTS, section "check"); and runs **`check-traces.py`**, one script you write that checks every `#TRACE` in every module against its `-- EXPECT:` comment (the encoders each wrote their own trace checker in FLEET_DIR/work/g1..g9: read them and unify).
   A deontic cannot be `#ASSERT`ed, so without this the traces guard nothing.
   PROVE the trace checker works with a positive control: copy a module into WORK, change one `-- EXPECT:` to a wrong value, and show the checker fails.
   Report any `#TRACE` with no EXPECT comment.
7. **NOTES.md** (prose one sentence per line): what is encoded and what is not (the subordinate legislation R&O.19/2018, R&O.59/2018 and R&O.60/2018 is out of scope: say so); the layout and the import graph (generate it from the files' IMPORT lines); a coverage summary (counts per group and disposition) with the full coverage table generated by script from the nine FRAGMENTS into `coverage-all.tsv` (columns: provision, disposition, module, group) and compared with FLEET_DIR/phase1/coverage.tsv (851 rows; list every disposition that changed and every row that is missing or extra); a fork INDEX (every fork id, its group, a line on the reading taken) generated by script, pointing at the FRAGMENTs for detail, with the total count; the cross-group consistency register; a consolidated register of source contradictions (each once, the provisions, the discriminating case, and which groups found it; cross-check against FLEET_DIR/work/hunt/CONTRADICTIONS.md ONLY IF the brief allows you to read it, otherwise leave that to the launching session); consolidated open questions for a domain expert; consolidated "what the sources do not answer"; the answer table (the headline scenarios from the integration tests, with article citations); what `check.sh` prints; the defects found in group modules; and an empty section headed "Provenance of this run (to be written by the launching session)".
   Do not claim anything is verified beyond what the encoders say they checked.
   Do not claim a domain expert has read it.
8. **encoding.json and SOURCE-LICENSE.md** per `references/canon-deposit.md`: status `draft`, id `legalese-full-2026-10`, the module list in dependency order, `expected_red` per file, `not_reviewed` saying no domain expert has read it against the Law.
   SOURCE-LICENSE.md: start from FLEET_DIR/inputs/SOURCE-LICENSE.md (OSAL-J v1.0; the attribution is a licence condition and must be kept verbatim), and add that the Law's page was fetched on 2026-10-14 and fetched again on 2026-10-26, that the extracted body text of the two fetches is byte-identical (943 lines), and that the newest point-in-time version is the one of 02 Oct 2026.

## Constraints
- No git. Write only the files listed. The cleanroom binds you.
- Three Opus agents are writing independent tests in OTHER directories (FLEET_DIR/work/ind-a, ind-b, ind-c). Do not look in them. Do not rename any exported name of a group module; if your wiring truly needs one renamed, say so in your final report instead.
- Read the diagnostics, not the exit code. No module may emit a warning.
- There is no token or time budget: be thorough. If you must stop at a boundary, say exactly what is left, in NOTES and in your final report.

## Final report
Files written; exactly what check.sh printed (all modules, with the trace result and the hash results); the positive control for the trace checker; the integration scenarios and their results; the cross-group consistency register in summary; defects found in group modules; nouns requests resolved and how; anything you could not wire and why; peeked: nothing, or what.
