# Brief: the DOJ/FTC Antitrust Guidelines for International Enforcement and Cooperation (2017)

Target compiler: `main` (the stable `l4`); the encoding is also checked with the newest `unstable` build.
Label: **AGENCY ENFORCEMENT POLICY, NOT LAW.**
The guidelines state how the U.S. Department of Justice and the Federal Trade Commission apply the antitrust laws to conduct involving foreign commerce, weigh foreign jurisdictions' interests, and cooperate with foreign authorities; they do not state what a court must hold.
The text itself says it replaces the 1995 Antitrust Enforcement Guidelines for International Operations (read at source, 1 [pdf page 4]); the 1995 text is not to be read, and NOTES must say so.

This brief is the subject part of the coordinator's task; the common brief (`BRIEF-COMMON.md`) and the Phase 2 brief (`BRIEF-PHASE2.md`) of the batch, written by the parent session, apply with it, and the Phase 2 brief wins where they differ.

## The question

For a business engaged in international activities, what do the agencies say they will do: does the FTAIA leave the conduct within the reach of the Sherman Act and the FTC Act, what do comity and a foreign government's involvement change, and what do the agencies say they will do with information and remedies when they cooperate with a foreign authority?

## What to encode

- **Chapter 3**: 3.1, conduct involving import commerce; 3.2, non-import foreign commerce and the FTAIA's two requirements (the direct, substantial and reasonably foreseeable effect, and "gives rise to"); 3.3, U.S. government financing or purchasing. Where the agencies' view and the courts' readings differ, record both as the text puts them, without resolving them.
- **Chapter 4**: the comity factors of 4.1 as a report that weighs nothing; 4.2.1 to 4.2.4 (foreign sovereign immunity, foreign sovereign compulsion, act of state, petitioning of sovereigns).
- **Chapter 2**: only the statements that are tests; the rest inert, with a reason. Dated figures (thresholds, penalty limits, sunset dates) are left out.
- **Chapter 5**: the rules, with the text's modals; the rest inert.
- **Annex 1**: inert.
- **No foreign law.**
- The Illustrative Examples as fixtures where they are definite; NOTES records each Example's disposition.

## Forks expected

Each to be labelled "assumed, not ruled", with a fixture that tells the readings apart where one can:

- how conduct is classed as import or non-import commerce;
- the FTAIA findings, which are supplied by the caller, never computed;
- how the courts' differing readings are represented;
- what counts as a rule in chapter 5.

## Status to record

The guideline is in force: the DOJ's index of guidelines and policy statements (updated 17 November 2025) lists it, as read on 2026-11-25 by the session that deposited the source (the `in_force_check` field of the `.meta.json`).
NOTES must say which facts about withdrawn or superseded documents were read at source and which were only reported.

## Source

`../../registers/source-bundle/2017-international-enforcement-cooperation-guidelines.txt`, with `[pdf page N of 55]` markers; provenance and hashes in the `.meta.json` beside it; licensing in `../../SOURCE-LICENSE.md` (a work of the U.S. Government, 17 USC 105).

## Rules of the work

- Nouns first (types only), then rule modules in the guideline's order, then tests. An `@ref` with section and `[pdf page N]` on every rule.
- A case the text does not answer is `NOTHING` from a `MAYBE` (`main` has no `REFUSE`). Where the text tells "not yet determined" from "found not to be so", use two values.
- Result types are named for what the agencies (or whoever the sentence names) say, keeping the text's modal and speaker; never "illegal" or "lawful".
- Tests from the text, both sides of every distinction it draws; a `-red` file of positive controls, counted in `expected_red`.
- Fetch nothing; a fact the text does not give is an open question in NOTES. Short quotations only, swept against the source by script.
- Every section, subsection, list item with a rule of its own, Example and footnote appears once in the coverage table.
- Deliverables: the modules, `NOTES.md` (status, both builds' `check.sh` output, seat, scope, coverage table, fork register, open questions, withdrawn and superseded documents), `encoding.json`, `check.sh`, `fetch-main-l4.sh`, this brief.
- Work only in the worktree; commit locally; never push.
