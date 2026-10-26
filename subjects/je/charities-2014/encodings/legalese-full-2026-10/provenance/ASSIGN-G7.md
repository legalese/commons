FLEET_DIR = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full
L4_BIN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4  (sha256 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475; leave JL4_LIBRARY_PATH unset; run it under `nice -n 15`; at most two l4 processes at once; stop only processes you started, by PID, never by pattern)

# ASSIGNMENT: ENCODER for group G7 (Use of the expressions 'charity', 'charitable'; miscellaneous provisions; commencement and amendment history; Articles 21 to 25, Articles 37 to 43, and the endnotes)

You are ENCODER G7 in a fleet that encodes the Charities (Jersey) Law 2014 in L4. Your scope: Articles 21 to 25, Articles 37 to 43, and the endnotes. Your module prefix: `g7-` (every file you write in DEPOSIT starts with it, or is FRAGMENT-G7.md).

WORK = FLEET_DIR/work/g7/ (create it)

## Read, in this order
1. FLEET_DIR/BRIEF.md in full, including "Rules after the survey" (it overrides the PLAN where they differ) and the cleanroom rules.
2. The skills in FLEET_DIR/skills: encoding-a-subject (steps 1-7, 9, 11) and writing-l4-rules with its references and all of source-patterns/ (especially 04, 05, 08, 11). Also FLEET_DIR/inputs/pattern-r4.l4.
3. FLEET_DIR/phase1/slice-G7.md: the parts of the survey that concern you (your coverage rows, your group, the integration points that name you, your periods, the terminology, the traps, your forks, what the sources do not answer, the notes for the integrator). The whole survey is FLEET_DIR/phase1/PLAN.md (2,200 lines, mostly the coverage table); open it where the slice is not enough.
4. The source: every provision of your scope in FLEET_DIR/inputs/charities-jersey-law-2014-2026-10-02.txt, checked against FLEET_DIR/inputs/charities-jersey-law-2014-official-pdf-text-layer.txt wherever a number, a list or a connective matters, and the endnotes for any note marker on your provisions.
5. FLEET_DIR/deposit/domain.l4 (the shared nouns; read-only).

## What you write (all in FLEET_DIR/deposit/, prefix `g7-`)
- The modules of your group. PLAN section (b) proposes names and contents for them; change them if the text says so. No module starts with `@lang en`. Each imports only prelude, daydate, domain and modules of your OWN group; each has `@ref` on every rule and `§`/`§§` headings that follow the Law's own Parts and Articles.
- Tests, in modules of their own (`g7-tests-*.l4`), with expected values decided from the SOURCE before you run: both sides of every threshold, every date edge on both sides, every route through each list, one case per branch of each rule, every offence and its penalty. Tests that are MEANT to fail go in `g7-tests-red.l4` and are counted.
- FLEET_DIR/deposit/FRAGMENT-G7.md, containing: (1) coverage: one row per provision of your scope, in the Law's numbering, with disposition (`encoded` / `inert` / `refused` / `out-of-scope`), module and rule; nothing `deferred`; where you change a disposition from the PLAN, say why; (2) the fork register in the R4 shape of the brief (one record `Interpretation of ...` unique to your group; each fork: id, provision, readings and the text that licenses each, the reading taken and why, the field and constructors that carry it, the discriminating case and its test), including one fork for every kind of period you meet; (3) an answer table of the headline scenarios with the Article cited; (4) nouns requests for the INTEGRATOR; (5) the standard inputs you consume (the IP ids, exact `GIVEN` names) and the functions you export (exact names), so wiring is mechanical; (6) contradictions in the source, found by a deliberate separate pass after encoding; (7) open questions for a domain expert; (8) what the sources do not answer.
- In WORK only: scratch files, probes, scripts, and your copy of the check script.

## Group notes
- Part 6: the prohibition of unauthorised use of the expression 'charity' and related terms (21), excepted foreign charities (22), the expression 'Jersey charity' (23), the power to restrict use of 'charitable' in soliciting funds (24) and to require registered charities to identify themselves (25). Several contraventions are offences (imprisonment for 2 years and a fine): encode the prohibitions and the penalty as data.
- Part 9: offences by bodies corporate and others (37), service of notices (38), Regulations and Orders (39), savings and transitional provisions (40), and Articles 41 and 42 (enabling powers: 'The States may by Regulations amend ...'), and citation (43). Articles 41 and 42 are encoded as `MAY` rules of the States (ruling 4 of the brief); the enactments they would amend are out of scope.
- THE TEMPORAL AXIS IS YOURS. From the endnotes, R&O.17/2018 and the other instruments in inputs/amending, encode: which Parts and Articles are in force on a given day (staged commencement, with the renumbering the endnotes record); who 'the Minister' is on a given day and which Law defines 'Comptroller' on a given day; whether Article 2(1)(ba) is in force on a given day; whether the two 'subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017' additions to Schedule 1 are in force on a given day. Each is a function of the day (or of a vintage) with a test on both sides of every date. Export them with the standard names of PLAN section (c) so other groups' inputs can be wired to them. Where the instruments do not show a fact (for example the exact wording of an earlier 'Minister' definition), say so and answer silence; do not guess.

## Working rules
- Other encoders are writing their modules into the same DEPOSIT at the same moment. Write only files with your prefix and FRAGMENT-G7.md. Never edit another group's file or domain.l4.
- The brief's rules all bind you: isomorphic encoding, REFUSE where the source does not answer, the diagnostics not the exit code, the R4 shape for forks, the cleanroom. Read the DIAGNOSTICS of every `l4 run`: no warning may remain in your modules.
- A discretion is an input; a duty, power or prohibition is a regulative rule typed by role and act (PARTY/MUST/MAY/SHANT), not an enumeration of Article-named actions. An offence is a prohibition with its penalty as data.
- Copy `FLEET_DIR/skills/encoding-a-subject/assets/check.sh` into your WORK directory, adapt it to run only your group's modules (`DEPOSIT/g7-*.l4`), and report what it prints. Run `srcrefs.py check --refs` over every module you write (RAW is the Law's text file) and report the result.
- When you have finished, do a second, separate pass AGAINST YOUR OWN MODULES for contradictions in the source (the brief's "REPORT EVERY CONTRADICTION"), and a re-read of every number in your tests against the source.
- There is no token or time budget: be thorough. But if you find the scope cannot be finished in one context, stop at a clean boundary and say exactly what is left in FRAGMENT-G7.md and in your final report.

## Final report
The brief's final-report format (files; exactly what your check script printed; coverage by disposition; forks; contradictions; failing or refused assertions; what the sources do not answer; peeked), with the coverage count of `deferred` rows stated as 0 or explained.
