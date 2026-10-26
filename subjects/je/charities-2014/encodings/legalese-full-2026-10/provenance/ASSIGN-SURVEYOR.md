FLEET_DIR = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full
L4_BIN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/bin/l4  (sha256 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475; leave JL4_LIBRARY_PATH unset; run it under `nice -n 15`; at most two l4 processes at once; stop only processes you started, by PID, never by pattern)

# ASSIGNMENT: SURVEYOR

You are the SURVEYOR of a fleet that encodes the whole of the Charities (Jersey) Law 2014 in L4. Nine ENCODERS (G1 to G9) will each encode one group, in parallel, from your plan; an INTEGRATOR will then compose their groups; independent test authors and a contradiction hunt will check the result. You work first, alone. What you write decides whether the nine groups fit together, so precision matters more than length.

## Read first
1. FLEET_DIR/BRIEF.md in full (scope, sources, time, vintages, forks in the R4 shape, the cleanroom).
2. In FLEET_DIR/skills: encoding-a-subject/SKILL.md steps 1 to 4 (the coverage table, nouns before rules), and writing-l4-rules/SKILL.md enough to design types.
3. The whole Law: FLEET_DIR/inputs/charities-jersey-law-2014-2026-10-02.txt (about 940 lines; read all of it, slowly, twice: once for structure, once looking for what does not fit), cross-checked against the PDF text layer where a number or punctuation matters. Then the amending instruments in FLEET_DIR/inputs/amending/ (read the passages that concern this Law only; grep for "Charities (Jersey) Law").

## The group map (decided by the fleet lead; keep the numbering; you may propose a change with a reason, in section (b))

| group | scope | prefix | words |
| --- | --- | --- | --- |
| G1 | Articles 1 and 2 (interpretation; definition of entity and related terms) | `g1-` | 1,950 |
| G2 | Articles 3 to 7 (the Commissioner and its functions; the charity test, charitable purposes, public benefit) | `g2-` | 1,550 |
| G3 | Articles 8 to 10 (the register, the restricted section, public access) | `g3-` | 1,530 |
| G4 | Articles 11 and 12 (application to register; name of charity) | `g4-` | 1,350 |
| G5 | Articles 13 and 14 (effects of registration; powers of the court over a registered charity) | `g5-` | 1,490 |
| G6 | Articles 15 to 20 (deregistration; effects of deregistration; governors' duties, reportable matters, fitness orders) | `g6-` | 2,250 |
| G7 | Articles 21 to 25 (use of the expressions "charity", "charitable"), Articles 37 to 43 (Part 9), and the endnotes (commencement and amendment history: the temporal axis) | `g7-` | 2,300 |
| G8 | Articles 26 to 36 (information and enforcement; the Charity Tribunal and appeals) | `g8-` | 2,330 |
| G9 | Schedules 1 and 2 (the Commissioner; the Tribunal) | `g9-` | 2,015 |

## What you write

1. **FLEET_DIR/phase1/PLAN.md**, with these sections in this order and with exactly these headings:
   - `## 0. How to read this plan` (short).
   - `## (a) Coverage skeleton`: one row per Article AND per lettered or numbered paragraph that carries its own rule, definition, power, duty, prohibition, offence, number or time limit, in the Law's own numbering, for the whole Law, Schedules included. Columns: id, provision, first words (by script, from the source), gloss (your own words), disposition proposed (`encoded` / `inert` / `refused` / `out-of-scope`), module proposed, group, reason (a real reason for every row that is not `encoded`). Also write the same table as FLEET_DIR/phase1/coverage.tsv (tab-separated, header `id	provision	first_words	gloss	disposition	module	group	reason`). Then `### Reasons for every inert, refused and out-of-scope row` and `### Judgement calls in the dispositions`.
   - `## (b) Group map`: for each group `### Gk: <title>`: the provisions, the modules proposed (names, with the group prefix), what each module holds, the types it needs from domain.l4, the rules it exports (with the exact names you propose, unique across the fleet), what it takes as inputs, and anything specific the encoder should look at. Keep each group's modules to what one encoder can finish.
   - `## (c) Integration points`: a table `| id | what is shared | decided by | consumed by | carried by |` with ids `IP1`, `IP2`, ... Every fact that one group decides and another consumes (for example "the entity is a registered charity on the day", "the Commissioner is satisfied", "a Part is in force on the day", "who is the Minister on the day", "the entity meets the charity test") is one row with ONE standard `GIVEN` name and ONE type (in domain.l4). Encoders will use these names exactly, so the integrator can wire them mechanically.
   - `## (d) Periods register`: every period, term, limit and time-bound in the Law, with the Article, the kind (a deadline; a retention period; a term of office; a minimum notice; a backward-looking period; a sentence), the counting question it raises, and the group that owns it.
   - `## (e) Terminology`: every defined term (Article 1, Article 2 and those defined in place), where defined, what the encoding does with it, and which Jersey French or other-statute terms ("fidéicommis", "Loi of 1862", "fidéicommissaires") are inputs.
   - `## (f) First-read contradictions and traps`: `### T1:` ... each with the provisions, the groups affected, the discriminating case and your suggested handling. Look hard: cross-references that point at the wrong place or at a number that was renumbered (read the Table of Renumbered Provisions); definitions that are circular or disagree with their use; a power and a prohibition that collide; paragraphs of a list whose connective ("and"/"or") the text leaves open; "entity" categories that overlap; the Schedule 1 paragraphs that begin "subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017"; and the commencement text. Read the endnotes as carefully as the Articles.
   - `## (g) Forks`: the ambiguities you can already see, each as a candidate fork in the R4 shape of the brief (id, provision, readings, discriminating case), grouped by owner group.
   - `## 8. The domain nouns`: what FLEET_DIR/deposit/domain.l4 holds and why.
   - `## 9. What the sources do not answer`.
   - `## 10. Notes for the integrator`.
2. **FLEET_DIR/deposit/domain.l4**: the shared nouns, written once. It imports `prelude` (and `daydate` if it needs it) and nothing else; it starts with no `@lang` line; it type-checks with no warning (run `L4_BIN check`). Put in it the types that two or more groups use (the kinds of entity, the person/party roles, a `Registered charity` record, the standard-input types of section (c), and the like), with `@desc` on fields. Do not put rules in it. Do not over-reach: a type used by one group stays in that group's module. Write a one-paragraph comment at the top saying what it is for.
3. Nothing else. In particular do not write group modules and do not write tests.

## Working rules
- Quote mechanically: use `srcrefs.py quote` for "first words" and for any quotation, never memory.
- The map above is decided; the module names and the standard names are yours to decide, and they must be unique across the fleet (put the Article number or the distinguishing noun in the name).
- A power of the Minister, the Commissioner, the court or the Tribunal (to make an Order, to require, to deregister, to direct, to appoint, to disqualify) is a regulative `MAY` rule typed by who acts and what is done; its procedural preconditions are computable conditions; the CONTENT of an Order is an input. Mark nothing `inert` merely because no Order appears in the sources. Rows that only describe who sits on a body or restate another statute may be `inert`.
- Every period gets a row in (d) and a fork candidate in (g).
- Be exhaustive in (a): the encoders and the test authors work from it, and a provision missing from it will be missed by everyone.
- There is no token or time limit. Do not stop at a boundary short of the whole Law.

## Final report
Files written; the number of coverage rows by disposition; the number of integration points, periods, terms, traps and candidate forks; anything in the Law you could not classify and why; the result of `L4_BIN check` on domain.l4; `peeked`: nothing, or what you opened by accident.
