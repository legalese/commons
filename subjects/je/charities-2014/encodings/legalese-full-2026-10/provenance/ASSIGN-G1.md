FLEET_DIR = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full
L4_BIN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4  (sha256 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475; leave JL4_LIBRARY_PATH unset; run it under `nice -n 15`; at most two l4 processes at once; stop only processes you started, by PID, never by pattern)

# ASSIGNMENT: ENCODER for group G1 (Interpretation and the definition of entity; Articles 1 and 2)

You are ENCODER G1 in a fleet that encodes the Charities (Jersey) Law 2014 in L4. Your scope: Articles 1 and 2. Your module prefix: `g1-` (every file you write in DEPOSIT starts with it, or is FRAGMENT-G1.md).

WORK = FLEET_DIR/work/g1/ (create it)

## Read, in this order
1. FLEET_DIR/BRIEF.md in full, including "Rules after the survey" (it overrides the PLAN where they differ) and the cleanroom rules.
2. The skills in FLEET_DIR/skills: encoding-a-subject (steps 1-7, 9, 11) and writing-l4-rules with its references and all of source-patterns/ (especially 04, 05, 08, 11). Also FLEET_DIR/inputs/pattern-r4.l4.
3. FLEET_DIR/phase1/slice-G1.md: the parts of the survey that concern you (your coverage rows, your group, the integration points that name you, your periods, the terminology, the traps, your forks, what the sources do not answer, the notes for the integrator). The whole survey is FLEET_DIR/phase1/PLAN.md (2,200 lines, mostly the coverage table); open it where the slice is not enough.
4. The source: every provision of your scope in FLEET_DIR/inputs/charities-jersey-law-2014-2026-10-02.txt, checked against FLEET_DIR/inputs/charities-jersey-law-2014-official-pdf-text-layer.txt wherever a number, a list or a connective matters, and the endnotes for any note marker on your provisions.
5. FLEET_DIR/deposit/domain.l4 (the shared nouns; read-only).

## What you write (all in FLEET_DIR/deposit/, prefix `g1-`)
- The modules of your group. PLAN section (b) proposes names and contents for them; change them if the text says so. No module starts with `@lang en`. Each imports only prelude, daydate, domain and modules of your OWN group; each has `@ref` on every rule and `§`/`§§` headings that follow the Law's own Parts and Articles.
- Tests, in modules of their own (`g1-tests-*.l4`), with expected values decided from the SOURCE before you run: both sides of every threshold, every date edge on both sides, every route through each list, one case per branch of each rule, every offence and its penalty. Tests that are MEANT to fail go in `g1-tests-red.l4` and are counted.
- FLEET_DIR/deposit/FRAGMENT-G1.md, containing: (1) coverage: one row per provision of your scope, in the Law's numbering, with disposition (`encoded` / `inert` / `refused` / `out-of-scope`), module and rule; nothing `deferred`; where you change a disposition from the PLAN, say why; (2) the fork register in the R4 shape of the brief (one record `Interpretation of ...` unique to your group; each fork: id, provision, readings and the text that licenses each, the reading taken and why, the field and constructors that carry it, the discriminating case and its test), including one fork for every kind of period you meet; (3) an answer table of the headline scenarios with the Article cited; (4) nouns requests for the INTEGRATOR; (5) the standard inputs you consume (the IP ids, exact `GIVEN` names) and the functions you export (exact names), so wiring is mechanical; (6) contradictions in the source, found by a deliberate separate pass after encoding; (7) open questions for a domain expert; (8) what the sources do not answer.
- In WORK only: scratch files, probes, scripts, and your copy of the check script.

## Group notes
- Article 1 is a list of definitions. Most point elsewhere (to Article 2, to Article 6, to Article 8, to another statute). Encode a definition as a typed noun or a computable rule where it decides an outcome; where it only points, carry the pointer as an `@ref` and an input, and say which. Defined terms that name another statute's concept (company, foundation, trust, fidéicommis, property, regulated financial services business) are INPUTS.
- Article 2(1) lists the kinds of `entity`, (a) to (j), including (ba), the NPO body corporate inserted by R&O.56/2025 from 16 October 2025 under the power in Article 2(2). Whether (ba) is part of the definition on a given day is a vintage question: take it as a `GIVEN` from the temporal group (standard name in PLAN section (c)); do not decide it here. Article 2(2) is a power of the Minister to amend the list by Order: encode it as a `MAY` rule; the CONTENT of an Order is an input.
- Articles 2(3) to 2(10) define `Jersey entity`, `constitution`, `constitutional Law`, `purpose`, `governor` and `misconduct`. Read how each is USED by the other Parts (the PLAN's terminology section lists the uses) and shape your types so that other groups can take them as inputs.
- The definition of `Minister` has changed repeatedly (a vintage fact owned by the temporal group G7); here it is a role.

## Working rules
- Other encoders are writing their modules into the same DEPOSIT at the same moment. Write only files with your prefix and FRAGMENT-G1.md. Never edit another group's file or domain.l4.
- The brief's rules all bind you: isomorphic encoding, REFUSE where the source does not answer, the diagnostics not the exit code, the R4 shape for forks, the cleanroom. Read the DIAGNOSTICS of every `l4 run`: no warning may remain in your modules.
- A discretion is an input; a duty, power or prohibition is a regulative rule typed by role and act (PARTY/MUST/MAY/SHANT), not an enumeration of Article-named actions. An offence is a prohibition with its penalty as data.
- Copy `FLEET_DIR/skills/encoding-a-subject/assets/check.sh` into your WORK directory, adapt it to run only your group's modules (`DEPOSIT/g1-*.l4`), and report what it prints. Run `srcrefs.py check --refs` over every module you write (RAW is the Law's text file) and report the result.
- When you have finished, do a second, separate pass AGAINST YOUR OWN MODULES for contradictions in the source (the brief's "REPORT EVERY CONTRADICTION"), and a re-read of every number in your tests against the source.
- There is no token or time budget: be thorough. But if you find the scope cannot be finished in one context, stop at a clean boundary and say exactly what is left in FRAGMENT-G1.md and in your final report.

## Final report
The brief's final-report format (files; exactly what your check script printed; coverage by disposition; forks; contradictions; failing or refused assertions; what the sources do not answer; peeked), with the coverage count of `deferred` rows stated as 0 or explained.
