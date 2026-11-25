# Brief: the DOJ/FTC Antitrust Guidelines for the Licensing of Intellectual Property (2017)

Target compiler: `main` (the stable `l4`); the encoding is also checked with the newest `unstable` build.
Label: **AGENCY ENFORCEMENT POLICY, NOT LAW.**
The guidelines state when the U.S. Department of Justice and the Federal Trade Commission will, or will not, challenge a licensing arrangement; they do not state what a court must hold.

## The question

For an intellectual property licensing arrangement, what do the agencies say they will do with it: is a restraint in the antitrust "safety zone" of section 4.3, which mode of analysis applies, and what do sections 2 to 6 say of the particular restraints?

## What to encode

- **4.3, the safety zone.** Condition (1), not facially anticompetitive (n.59); condition (2), the licensor and its licensees collectively account for no more than twenty percent of each relevant market significantly affected (exactly twenty is inside); the rule that goods markets alone are considered unless that would be inadequate; the criteria for technology and research and development markets when share data are unavailable or inaccurate (four or more independently controlled technologies or entities besides the parties'); what the zone does not apply to (n.58; transfers given a merger analysis, n.86).
- **Parts 2 and 3**: rule of reason against per se, and "facially anticompetitive"; the market definitions; market power.
- **4.1 and 4.2** where they state rules.
- **Part 5**: every test or "will ... unless" rule. Where the text only lists considerations, a typed list of factors the caller supplies and a report of which are present, never a weighing.
- **The ten Examples** as fixtures where they are definite; NOTES records each Example's disposition.
- Background goes in the coverage table as `inert`.

## Forks expected

How "collectively account for" is computed; what counts as "facially anticompetitive"; whether each of several affected markets must pass. Each is to be labelled "assumed, not ruled", with a fixture that tells the readings apart.

## Status to record

The guideline is in force: the DOJ's index of guidelines and policy statements (updated 17 November 2025) lists it, as read on 2026-11-25 by the session that wrote this brief.
The 2000 Collaborations Among Competitors guidelines were withdrawn on 11 December 2024, reported from a search summary of an FTC press release that could not be fetched.
NOTES must say which facts were read at source and which were only reported.

## Source

`../../registers/source-bundle/2017-ip-licensing-guidelines.txt`, with `[pdf page N of 38]` markers; provenance and hashes in the `.meta.json` beside it; licensing in `../../SOURCE-LICENSE.md` (a work of the U.S. Government, 17 USC 105).

## Rules of the work

- Nouns first (types only), then rule modules in the guideline's order, then tests. An `@ref` with section and `[pdf page N]` on every rule.
- A case the text does not answer is `NOTHING` from a `MAYBE` (`main` has no `REFUSE`); impossible inputs answer `NOTHING`. Shares in percent points.
- Result types are named for what the agencies do, keeping the text's modal; never "illegal" or "lawful".
- Tests from the text, both sides of every threshold; a `-red` file of positive controls, counted in `expected_red`.
- Fetch nothing; a fact the text does not give is an open question in NOTES. Short quotations only.
- Deliverables: the modules, `NOTES.md` (status, both builds' `check.sh` output, scope, coverage table, fork register, open questions, withdrawn and superseded guidelines), `encoding.json`, `check.sh`, `fetch-main-l4.sh`, this brief.
