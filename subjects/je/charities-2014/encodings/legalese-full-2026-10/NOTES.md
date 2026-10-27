# NOTES: the Charities (Jersey) Law 2014 (L.41/2014), the whole Law, in L4

## 0. Status, and how to read this file

Status: draft.
This is an encoding of the whole Charities (Jersey) Law 2014 in L4, made by a fleet of nine group encoders and one integrator, all of them AI agents, in October 2026, and tested by three independent test authors, also AI agents.
Two groups (G2 and G7) were repaired on 2026-10-27 after the independent testing, and the integrator rewired and re-ran everything on the same day (sections 3.6 and 12).
No domain expert (a Jersey charity lawyer, or anyone who knows the Jersey Charity Commissioner's practice) has read any module of it against the Law.
The group encoders checked their own modules against the text of the Law as they say in their FRAGMENT files (`FRAGMENT-G1.md` to `FRAGMENT-G9.md`, kept beside this file).
The integrator checked the wiring between the groups and the six headline functions, and ran the independent authors' tests against the repaired groups, and nothing more; this file does not claim that anything is verified beyond what the encoders and the integrator say they checked.
It is not legal advice and it is not the law: the Law is the text on jerseylaw.je, and that site itself says its contents are for information purposes only.
Every number in this file is a point-in-time record taken with one `l4` build (sha256 `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`) and one `domain.l4` (sha256 `af1703908b8f62922ed36a9984104231b93b41703deec7c1e45f1fef84399d66`); `check.sh` re-checks both hashes.
In this file prose has one sentence to a line, so that a search returns whole sentences; tables and code are left as they are.

## 1. Scope: what is encoded and what is not

Encoded: the Charities (Jersey) Law 2014 (L.41/2014) as consolidated on jerseylaw.je, "Showing the law from 02 Oct 2026 to Current".
That is the Title, the Long title, Articles 1 to 43 in nine Parts, Schedule 1 (Jersey Charity Commissioner), Schedule 2 (Charity Tribunal), and the endnotes (the Table of Legislation History, the Table of Renumbered Provisions and the Table of Endnote References).
The survey divided the Law into 851 provisions (rows of `phase1/coverage.tsv`), and the nine groups together cover every one of them (section 4).
The text has nine point-in-time versions (from 1 January 2019, 31 May 2019, 16 December 2019, 1 January 2020, 2 March 2021, 12 April 2023, 27 February 2024 at 9.30 a.m., 16 October 2025 and 2 October 2026), and the Law was brought into force in three stages (21 November 2014, 1 May 2018, 1 January 2019).
Both facts are encoded (section 3): a headline function asked about a day before a unit of the Law it rests on came into force, or before the first consolidated text, refuses with a named reason.

Not encoded:

- The subordinate legislation made under the Law is out of scope: R&O.19/2018, R&O.59/2018 (the Charities (Additional Information) (Jersey) Order 2018) and R&O.60/2018 (the Charities (Restricted Section of Register) (Jersey) Order 2018).
  None of the three is among the sources.
  Every Order and every set of Regulations that the Law empowers is an input wherever a rule needs its content (section 9 lists them); no Order or Regulations is assumed to exist.
  Where a test or a chain in `int-tests-*.l4` supplies one (a due date for the annual return, a time limit for appeals), it is an illustration and says so in a comment.
- The other enactments the Law mentions are not encoded: the Trusts (Jersey) Law 1984, the Companies (Jersey) Law 1991, the Foundations (Jersey) Law 2009, the Non-Profit Organizations (Jersey) Law 2008, the Loi (1862), the Revenue Administration (Jersey) Law 2019, the Income Tax (Jersey) Law 1961, the Dormant Bank Accounts (Jersey) Law 2017 beyond the words Schedule 1 borrows, the Interpretation (Jersey) Law 1954, and the others named in the FRAGMENTs.
  What those Laws decide (whether a body is a company, whether an act is an offence under one of them, how a period is counted) is an input or a fork.
- The nine texts differ only where the amendment history says (the definition of "Minister", the definition of "Comptroller", sub-paragraph (ba) of Article 2(1), and two phrases of Schedule 1); the encoding does not model any other difference, because no other is shown by the sources.
  There is no text before 1 January 2019 among the sources, so every function that depends on the text refuses for an earlier day; and the text of 2 October 2026 is read for every later day (the consolidation runs "to Current").
- The licence of the source text is in `SOURCE-LICENSE.md`.

## 2. Layout and the import graph

The deposit is one directory.
Its files, by kind:

- `domain.l4`: the shared nouns, written once by the survey and never edited (sha256 pinned in `check.sh`).
- `g1-*.l4` to `g9-*.l4`: the nine groups' modules, 102 of them (rule modules, `*-nouns`, `*-interpretation` or `*-readings`, fixtures, and `*-tests-*` modules; each group's `g<k>-tests-red.l4`, except G1, which has none, holds the assertions its author expects to fail).
  G1 is Articles 1 and 2; G2 Articles 3 to 7; G3 Articles 8 to 10; G4 Articles 11 and 12; G5 Articles 13 and 14; G6 Articles 15 to 20; G7 Articles 21 to 25, 37 to 43 and the endnotes (commencement, the nine texts); G8 Articles 26 to 36; G9 Schedules 1 and 2.
- `int-*.l4`: the 27 modules of the integration layer (section 3): the wiring and the six headline functions (`int-readings`, `int-commencement`, `int-vintage`, `int-nouns`, `int-wiring`, `int-h-text`, `int-h-application`, `int-h-register`, `int-h-contravention`, `int-h-offence`, `int-h-appeal`), and the tests (`int-tests-*`, including `int-tests-fixtures.l4`, which holds the shared test data and has no assertion, `int-tests-red.l4`, which holds the kept-failing assertions, and `int-tests-repairs.l4`, which tests what changed after the independent testing).
- `ind-a-*.l4`, `ind-b-*.l4`, `ind-c-*.l4`: the 32 modules of the three independent test authors, merged into the row (section 12): topical tests, fixtures, and each author's `ambiguous` and `disagree` files.
- `FRAGMENT-G1.md` to `FRAGMENT-G9.md`: each group's own record: coverage rows, fork register, answer table, nouns requests, standard inputs consumed and functions exported, contradictions, open questions, what the sources do not answer, and what its check printed.
  They are kept as the groups wrote them; this file merges their sections and points back to them.
- `check.sh`, `check-traces.py`, `srcrefs.py`: the self-check (section 11).
  `srcrefs.py` is byte-identical to the encoding-a-subject skill's `assets/srcrefs.py`.
- `coverage-all.tsv`: the 851 coverage rows, generated from the nine fragments (section 4).
- `encoding.json`, `SOURCE-LICENSE.md`, `README.md`, `NOTES.md` (this file).

The import graph below is generated from the `IMPORT` lines of the files.
A group module imports only `prelude`, `daydate`, `domain` and modules of its own group, and `check.sh` fails if one does not; only `int-` and `ind-` modules import across groups.
The modules are listed in dependency order (dependencies first), which is also the order of `modules` in `encoding.json`.

Modules by group: G1 7, G2 12, G3 14, G4 11, G5 12, G6 12, G7 13, G8 12, G9 9, domain 1, ind-a 10, ind-b 12, ind-c 10, int 27; 162 in all.

| module | group | imports (other than prelude and daydate) |
| --- | --- | --- |
| domain | domain | (none) |
| g1-interpretation | G1 | (none) |
| g1-art1-defined-terms | G1 | domain, g1-interpretation |
| g1-art2-entity | G1 | domain, g1-interpretation, g1-art1-defined-terms |
| g1-art2-governor-misconduct | G1 | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity |
| g1-tests-art1 | G1 | domain, g1-interpretation, g1-art1-defined-terms |
| g1-tests-art2-entity | G1 | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity |
| g1-tests-art2-governor-misconduct | G1 | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct |
| g2-nouns | G2 | domain |
| g2-art3-4-commissioner | G2 | domain, g2-nouns |
| g2-art6-purposes | G2 | domain, g2-nouns |
| g2-art7-public-benefit | G2 | domain, g2-nouns |
| g2-art5-charity-test | G2 | domain, g2-nouns, g2-art6-purposes, g2-art7-public-benefit |
| g2-fixtures | G2 | domain, g2-nouns |
| g2-readings | G2 | domain, g2-nouns |
| g2-tests-art3-4 | G2 | domain, g2-nouns, g2-readings, g2-art3-4-commissioner |
| g2-tests-art5 | G2 | domain, g2-nouns, g2-readings, g2-fixtures, g2-art6-purposes, g2-art7-public-benefit, g2-art5-charity-test |
| g2-tests-art6 | G2 | domain, g2-nouns, g2-readings, g2-fixtures, g2-art6-purposes |
| g2-tests-art7 | G2 | domain, g2-nouns, g2-readings, g2-fixtures, g2-art7-public-benefit |
| g2-tests-red | G2 | domain, g2-nouns, g2-readings, g2-fixtures, g2-art3-4-commissioner, g2-art6-purposes, g2-art7-public-benefit, g2-art5-charity-test |
| g3-nouns | G3 | domain |
| g3-art8-register | G3 | domain, g3-nouns |
| g3-art9-restricted-section | G3 | domain, g3-nouns, g3-art8-register |
| g3-art10-public-access | G3 | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section |
| g3-fixtures | G3 | domain, g3-nouns |
| g3-tests-art10-public-access | G3 | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, g3-fixtures |
| g3-tests-art8-address | G3 | domain, g3-nouns, g3-art8-register, g3-fixtures |
| g3-tests-art8-historic | G3 | domain, g3-nouns, g3-art8-register, g3-fixtures |
| g3-tests-art8-register | G3 | domain, g3-nouns, g3-art8-register, g3-fixtures |
| g3-tests-art8-retention | G3 | domain, g3-nouns, g3-art8-register, g3-fixtures |
| g3-tests-art8-time | G3 | domain, g3-nouns, g3-art8-register, g3-fixtures |
| g3-tests-art9-restricted-section | G3 | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-fixtures |
| g3-tests-readings | G3 | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, g3-fixtures |
| g3-tests-red | G3 | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, g3-fixtures |
| g4-interpretation | G4 | (none) |
| g4-nouns | G4 | domain |
| g4-art11-application | G4 | domain, g4-interpretation, g4-nouns |
| g4-art11-decision | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application |
| g4-art12-name | G4 | domain, g4-interpretation, g4-nouns |
| g4-tests-fixtures | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-art12-name |
| g4-tests-art11-application | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-tests-fixtures |
| g4-tests-art11-decision | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-tests-fixtures |
| g4-tests-art12-name | G4 | domain, g4-interpretation, g4-nouns, g4-art11-decision, g4-art12-name, g4-tests-fixtures |
| g4-tests-forks | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-art12-name, g4-tests-fixtures |
| g4-tests-red | G4 | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-art12-name, g4-tests-fixtures |
| g5-interpretation | G5 | domain |
| g5-nouns | G5 | domain |
| g5-art13-effects | G5 | domain, g5-interpretation, g5-nouns |
| g5-art13-reporting | G5 | domain, g5-interpretation, g5-nouns |
| g5-art14-court-powers | G5 | domain, g5-interpretation, g5-nouns |
| g5-tests-fixtures | G5 | domain, g5-interpretation, g5-nouns |
| g5-tests-art13-effects | G5 | domain, g5-interpretation, g5-nouns, g5-art13-effects, g5-tests-fixtures |
| g5-tests-art13-reporting | G5 | domain, g5-interpretation, g5-nouns, g5-art13-reporting, g5-tests-fixtures |
| g5-tests-art14 | G5 | domain, g5-interpretation, g5-nouns, g5-art14-court-powers |
| g5-tests-forks | G5 | domain, g5-interpretation, g5-nouns, g5-art13-effects, g5-art13-reporting, g5-art14-court-powers, g5-tests-fixtures |
| g5-tests-properties | G5 | domain, g5-interpretation, g5-nouns, g5-art13-reporting, g5-tests-fixtures |
| g5-tests-red | G5 | domain, g5-interpretation, g5-nouns, g5-art13-effects, g5-art13-reporting, g5-art14-court-powers, g5-tests-fixtures |
| g6-interpretation | G6 | domain |
| g6-art15-16-deregistration | G6 | domain, g6-interpretation |
| g6-art17-after-deregistration | G6 | domain, g6-interpretation, g6-art15-16-deregistration |
| g6-art18-governor-duties | G6 | domain, g6-interpretation |
| g6-art20-court-orders | G6 | domain, g6-interpretation |
| g6-art19-reportable-matters | G6 | domain, g6-interpretation, g6-art18-governor-duties, g6-art20-court-orders |
| g6-tests-art15-16 | G6 | domain, g6-interpretation, g6-art15-16-deregistration |
| g6-tests-art17 | G6 | domain, g6-interpretation, g6-art15-16-deregistration, g6-art17-after-deregistration |
| g6-tests-art18 | G6 | domain, g6-interpretation, g6-art18-governor-duties |
| g6-tests-art19 | G6 | domain, g6-interpretation, g6-art18-governor-duties, g6-art20-court-orders, g6-art19-reportable-matters |
| g6-tests-art20 | G6 | domain, g6-interpretation, g6-art20-court-orders |
| g6-tests-red | G6 | domain, g6-interpretation, g6-art15-16-deregistration, g6-art17-after-deregistration, g6-art18-governor-duties, g6-art20-court-orders, g6-art19-reportable-matters |
| g7-interpretation | G7 | domain |
| g7-art21-23-expressions | G7 | domain, g7-interpretation |
| g7-art24-25-powers | G7 | domain, g7-interpretation |
| g7-art37-43-final | G7 | domain, g7-interpretation |
| g7-vintages | G7 | domain, g7-interpretation |
| g7-commencement | G7 | domain, g7-interpretation, g7-vintages |
| g7-tests-commencement | G7 | domain, g7-interpretation, g7-vintages, g7-commencement |
| g7-tests-fixtures-expressions | G7 | domain, g7-interpretation, g7-art21-23-expressions |
| g7-tests-expression-traces | G7 | domain, g7-interpretation, g7-art21-23-expressions, g7-tests-fixtures-expressions |
| g7-tests-expressions | G7 | domain, g7-interpretation, g7-art21-23-expressions, g7-vintages, g7-tests-fixtures-expressions |
| g7-tests-powers-final | G7 | domain, g7-interpretation, g7-art24-25-powers, g7-art37-43-final |
| g7-tests-red | G7 | domain, g7-interpretation, g7-vintages, g7-commencement, g7-art21-23-expressions, g7-art24-25-powers, g7-art37-43-final, g7-tests-fixtures-expressions |
| g7-tests-vintages | G7 | domain, g7-interpretation, g7-vintages |
| g8-nouns | G8 | domain |
| g8-penalties | G8 | domain, g8-nouns |
| g8-art26-demand | G8 | domain, g8-nouns, g8-penalties |
| g8-art27-28-required-steps | G8 | domain, g8-nouns, g8-art26-demand |
| g8-art29-31-information | G8 | domain, g8-nouns, g8-penalties |
| g8-art32-36-appeals | G8 | domain, g8-nouns |
| g8-tests-fixtures | G8 | domain, g8-nouns |
| g8-tests-art26 | G8 | domain, g8-nouns, g8-penalties, g8-art26-demand, g8-tests-fixtures |
| g8-tests-art27-28 | G8 | domain, g8-nouns, g8-art26-demand, g8-art27-28-required-steps, g8-tests-fixtures |
| g8-tests-art29-31 | G8 | domain, g8-nouns, g8-penalties, g8-art29-31-information, g8-tests-fixtures |
| g8-tests-art32-36 | G8 | domain, g8-nouns, g8-art26-demand, g8-art27-28-required-steps, g8-art32-36-appeals, g8-tests-fixtures |
| g8-tests-red | G8 | domain, g8-nouns, g8-penalties, g8-art26-demand, g8-art27-28-required-steps, g8-art29-31-information, g8-art32-36-appeals, g8-tests-fixtures, g8-tests-art26, g8-tests-art27-28, g8-tests-art29-31, g8-tests-art32-36 |
| g9-interpretation | G9 | domain |
| g9-common | G9 | domain, g9-interpretation |
| g9-sched1-commissioner | G9 | domain, g9-interpretation, g9-common |
| g9-sched2-tribunal | G9 | domain, g9-interpretation, g9-common |
| g9-tests-periods | G9 | domain, g9-interpretation, g9-common |
| g9-tests-red | G9 | domain, g9-interpretation, g9-common, g9-sched1-commissioner, g9-sched2-tribunal |
| g9-tests-sched1 | G9 | domain, g9-interpretation, g9-common, g9-sched1-commissioner |
| g9-tests-sched2 | G9 | domain, g9-interpretation, g9-common, g9-sched2-tribunal |
| g9-tests-t20 | G9 | domain, g9-interpretation, g9-common, g9-sched1-commissioner, g9-sched2-tribunal |
| ind-a-tests-fixtures | ind-a | domain, g1-interpretation, g1-art2-entity |
| ind-a-tests-ambiguous | ind-a | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity, g2-nouns, g2-readings, g2-art7-public-benefit, g3-nouns, g3-art8-register, g7-interpretation, g7-vintages, ind-a-tests-fixtures |
| ind-a-tests-art1 | ind-a | domain, g1-interpretation, g1-art1-defined-terms, g7-interpretation, g7-vintages, ind-a-tests-fixtures |
| ind-a-tests-art11-12 | ind-a | domain, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-art12-name, ind-a-tests-fixtures |
| ind-a-tests-art2 | ind-a | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct, g7-interpretation, g7-vintages, ind-a-tests-fixtures |
| ind-a-tests-art3-7 | ind-a | domain, g2-nouns, g2-readings, g2-art3-4-commissioner, g2-art5-charity-test, g2-art6-purposes, g2-art7-public-benefit, g1-art1-defined-terms, g7-interpretation, g7-vintages, ind-a-tests-fixtures |
| ind-a-tests-art8-10 | ind-a | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, ind-a-tests-fixtures |
| ind-a-tests-commencement | ind-a | domain, g7-interpretation, g7-commencement |
| ind-a-tests-disagree | ind-a | domain, g3-nouns, g3-art8-register, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, ind-a-tests-fixtures |
| ind-a-tests-readings | ind-a | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct, g2-nouns, g2-readings, g2-art3-4-commissioner, g2-art5-charity-test, g2-art6-purposes, g2-art7-public-benefit, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, g4-interpretation, g4-nouns, g4-art11-application, g4-art11-decision, g4-art12-name, ind-a-tests-fixtures |
| ind-b-tests-fixtures-g2 | ind-b | domain, g2-nouns, g2-readings, g2-art5-charity-test, g2-art6-purposes, g2-art7-public-benefit |
| ind-b-tests-fixtures-g7 | ind-b | domain, g7-interpretation, g7-art21-23-expressions, g7-art24-25-powers, g7-commencement, g7-vintages |
| ind-b-tests-ambiguous | ind-b | domain, g2-nouns, g2-readings, g2-art5-charity-test, g2-art7-public-benefit, g7-interpretation, g7-art21-23-expressions, ind-b-tests-fixtures-g2, ind-b-tests-fixtures-g7 |
| ind-b-tests-fixtures-g5 | ind-b | domain, g5-interpretation, g5-nouns, g5-art13-effects, g5-art13-reporting, g5-art14-court-powers |
| ind-b-tests-art13-14 | ind-b | domain, g5-interpretation, g5-nouns, g5-art13-effects, g5-art13-reporting, g5-art14-court-powers, ind-b-tests-fixtures-g5 |
| ind-b-tests-fixtures-g6 | ind-b | domain, g6-interpretation, g6-art15-16-deregistration, g6-art17-after-deregistration, g6-art18-governor-duties, g6-art19-reportable-matters, g6-art20-court-orders |
| ind-b-tests-art15-17 | ind-b | domain, g6-interpretation, g6-art15-16-deregistration, g6-art17-after-deregistration, ind-b-tests-fixtures-g6 |
| ind-b-tests-art18-20 | ind-b | domain, g6-interpretation, g6-art18-governor-duties, g6-art19-reportable-matters, g6-art20-court-orders, ind-b-tests-fixtures-g6 |
| ind-b-tests-art21-25 | ind-b | domain, g7-interpretation, g7-art21-23-expressions, g7-art24-25-powers, ind-b-tests-fixtures-g7 |
| ind-b-tests-art5-7 | ind-b | domain, g2-nouns, g2-readings, g2-art5-charity-test, g2-art6-purposes, g2-art7-public-benefit, ind-b-tests-fixtures-g2 |
| ind-b-tests-commencement-vintages | ind-b | domain, g7-interpretation, g7-commencement, g7-vintages, ind-b-tests-fixtures-g7 |
| ind-b-tests-disagree | ind-b | domain, g2-nouns, g2-readings, g2-art5-charity-test, g2-art6-purposes, g2-art7-public-benefit, g7-interpretation, g7-art21-23-expressions, g7-vintages, ind-b-tests-fixtures-g2, ind-b-tests-fixtures-g7 |
| ind-c-tests-fixtures-g8 | ind-c | domain, g8-nouns |
| ind-c-tests-ambiguous | ind-c | domain, g2-nouns, g2-readings, g2-art6-purposes, g2-art7-public-benefit, g2-art5-charity-test, g8-nouns, g8-art29-31-information, ind-c-tests-fixtures-g8, g7-interpretation, g7-vintages, g9-interpretation, g9-common, g9-sched1-commissioner, g9-sched2-tribunal |
| ind-c-tests-art26-31 | ind-c | domain, g8-nouns, g8-penalties, g8-art26-demand, g8-art27-28-required-steps, g8-art29-31-information, ind-c-tests-fixtures-g8 |
| ind-c-tests-art32-36 | ind-c | domain, g8-nouns, g8-art32-36-appeals, ind-c-tests-fixtures-g8 |
| ind-c-tests-art37-43 | ind-c | domain, g7-interpretation, g7-art37-43-final, g2-nouns, g2-art6-purposes |
| ind-c-tests-art5-7 | ind-c | domain, g2-nouns, g2-readings, g2-art6-purposes, g2-art7-public-benefit, g2-art5-charity-test |
| ind-c-tests-commencement-vintages | ind-c | domain, g7-interpretation, g7-vintages, g7-commencement, g2-readings |
| ind-c-tests-sched1 | ind-c | domain, g9-interpretation, g9-common, g9-sched1-commissioner |
| ind-c-tests-sched2 | ind-c | domain, g9-interpretation, g9-common, g9-sched2-tribunal |
| ind-c-tests-traces | ind-c | domain, g2-nouns, g2-art7-public-benefit, g2-art5-charity-test, g2-art6-purposes, g8-nouns, g8-art26-demand, g8-art29-31-information, g8-art27-28-required-steps, g8-art32-36-appeals, ind-c-tests-fixtures-g8, g9-interpretation, g9-common, g9-sched1-commissioner, g9-sched2-tribunal, g2-readings |
| int-commencement | int | domain, g7-interpretation, g7-vintages, g7-commencement |
| int-nouns | int | domain, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct, g2-nouns, g6-art19-reportable-matters, g8-nouns |
| int-readings | int | domain, g1-interpretation, g2-nouns, g3-nouns, g4-interpretation, g5-interpretation, g6-interpretation, g7-interpretation, g8-nouns, g9-interpretation |
| int-vintage | int | domain, g7-interpretation, g7-vintages |
| int-wiring | int | domain, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct, g1-interpretation, g2-nouns, g2-art5-charity-test, g2-art6-purposes, g6-interpretation, g3-nouns, g3-art8-register, g4-nouns, g4-art12-name, g5-nouns, g5-art13-reporting, g6-art20-court-orders, g6-art19-reportable-matters, g7-interpretation, g7-vintages, g7-art37-43-final, g8-nouns, g8-art27-28-required-steps, int-readings, int-nouns |
| int-h-appeal | int | domain, g4-nouns, g7-interpretation, g7-art37-43-final, g8-nouns, g8-art32-36-appeals, int-readings, int-nouns, int-commencement, int-vintage, int-wiring |
| int-h-application | int | domain, g2-nouns, g3-nouns, g4-nouns, g4-interpretation, g4-art11-application, g4-art11-decision, g5-nouns, g6-art19-reportable-matters, g6-art20-court-orders, g7-interpretation, int-readings, int-nouns, int-commencement, int-vintage, int-wiring |
| int-h-register | int | domain, g3-nouns, g3-art8-register, g3-art9-restricted-section, g3-art10-public-access, g5-nouns, g8-nouns, g8-art27-28-required-steps, int-readings, int-nouns, int-commencement, int-vintage, int-wiring |
| int-h-contravention | int | domain, g1-art2-entity, g1-art2-governor-misconduct, g3-nouns, g4-nouns, g4-art11-decision, g4-art12-name, g5-nouns, g5-art14-court-powers, g6-interpretation, g6-art15-16-deregistration, g6-art17-after-deregistration, g6-art18-governor-duties, g6-art19-reportable-matters, g6-art20-court-orders, g7-interpretation, g7-vintages, g7-art21-23-expressions, g8-nouns, g8-art27-28-required-steps, g9-sched1-commissioner, int-readings, int-nouns, int-commencement, int-vintage, int-wiring, int-h-register |
| int-h-offence | int | domain, g3-nouns, g3-art10-public-access, g6-interpretation, g6-art19-reportable-matters, g6-art20-court-orders, g7-interpretation, g7-art21-23-expressions, g7-art37-43-final, g8-nouns, g8-art26-demand, g8-art29-31-information, g8-penalties, g9-interpretation, g9-common, g9-sched2-tribunal, int-readings, int-nouns, int-commencement, int-vintage, int-wiring |
| int-h-text | int | domain, g1-art1-defined-terms, g7-interpretation, g7-vintages, g7-commencement, g9-common, g9-interpretation, g9-sched1-commissioner, int-readings, int-commencement |
| int-tests-fixtures | int | domain, g1-art1-defined-terms, g1-art2-entity, g1-art2-governor-misconduct, g2-nouns, g3-nouns, g4-nouns, g5-nouns, g6-art18-governor-duties, g6-art19-reportable-matters, g6-art20-court-orders, g6-art15-16-deregistration, g7-art21-23-expressions, g7-art37-43-final, g8-nouns, int-nouns, int-readings, int-h-register, int-h-contravention, int-h-application |
| int-tests-appeal | int | domain, g4-nouns, g8-nouns, int-readings, int-nouns, int-h-application, int-h-appeal, int-tests-fixtures |
| int-tests-application | int | domain, g2-nouns, g3-nouns, g4-nouns, g4-interpretation, g4-tests-fixtures, g5-nouns, g6-art19-reportable-matters, g6-art20-court-orders, g7-interpretation, int-readings, int-nouns, int-wiring, int-h-application, int-tests-fixtures |
| int-tests-chains | int | domain, g5-nouns, g5-art13-reporting, g6-art17-after-deregistration, g6-art19-reportable-matters, g8-nouns, int-readings, int-nouns, int-wiring, int-h-register, int-h-contravention, int-h-offence, int-tests-fixtures |
| int-tests-commencement | int | domain, g7-interpretation, g7-vintages, g7-commencement, int-commencement |
| int-tests-consistency | int | domain, g2-nouns, g2-readings, g2-art5-charity-test, g3-nouns, g3-art8-register, g4-nouns, g4-art12-name, g5-nouns, g5-art13-reporting, g6-art20-court-orders, g7-interpretation, g7-art21-23-expressions, g8-nouns, g8-art26-demand, g8-penalties, g9-interpretation, g9-sched2-tribunal, int-readings, int-nouns, int-wiring, int-h-offence, int-tests-fixtures |
| int-tests-contravention | int | domain, g5-nouns, g6-art15-16-deregistration, g6-art17-after-deregistration, g6-art19-reportable-matters, g6-art20-court-orders, g8-nouns, int-readings, int-nouns, int-h-register, int-h-contravention, int-tests-fixtures |
| int-tests-counting | int | domain, g3-nouns, g3-art8-register, g4-nouns, g4-art11-application, g5-nouns, g5-art14-court-powers, g6-art15-16-deregistration, g6-art17-after-deregistration, g7-interpretation, g7-vintages, g8-nouns, g8-art26-demand, g8-art32-36-appeals, g9-common, int-readings, int-nouns, int-wiring, int-tests-fixtures |
| int-tests-decisions | int | domain, g3-nouns, g3-art9-restricted-section, g4-nouns, g4-art12-name, g5-nouns, g5-art13-effects, g6-art15-16-deregistration, g8-nouns, g8-art26-demand, g8-art27-28-required-steps, g8-art32-36-appeals, g9-interpretation, g9-sched1-commissioner, int-readings, int-nouns, int-h-application, int-tests-fixtures |
| int-tests-offence | int | domain, g6-art19-reportable-matters, g7-art21-23-expressions, g7-art37-43-final, g8-nouns, int-readings, int-nouns, int-h-offence, int-tests-fixtures |
| int-tests-readings | int | domain, g1-interpretation, g2-readings, g3-fixtures, g4-tests-fixtures, g5-interpretation, g6-interpretation, g7-interpretation, g8-tests-fixtures, g9-interpretation, int-readings |
| int-tests-red | int | domain, g6-art20-court-orders, g7-interpretation, g7-art21-23-expressions, g8-nouns, g8-art26-demand, g8-penalties, g9-interpretation, g9-sched2-tribunal, int-readings, int-nouns, int-wiring, int-h-offence, int-tests-fixtures |
| int-tests-register | int | domain, g2-nouns, g3-nouns, g5-nouns, g8-nouns, int-readings, int-nouns, int-wiring, int-h-register, int-tests-fixtures |
| int-tests-repairs | int | domain, g2-nouns, g2-readings, g2-art6-purposes, g3-nouns, g4-nouns, g6-art19-reportable-matters, g7-interpretation, g7-art21-23-expressions, g7-art37-43-final, g8-nouns, int-readings, int-nouns, int-wiring, int-h-text, int-h-application, int-h-offence, int-tests-fixtures |
| int-tests-vintage-matrix | int | domain, g1-interpretation, g1-art1-defined-terms, g1-art2-entity, g7-interpretation, g7-vintages, g7-commencement, g9-interpretation, g9-sched1-commissioner, int-readings, int-h-text |
| int-tests-wiring | int | domain, g2-nouns, g2-readings, g3-nouns, g4-nouns, g4-art11-application, g4-art11-decision, g5-nouns, g6-art17-after-deregistration, g7-art21-23-expressions, g8-nouns, g8-art26-demand, g8-art27-28-required-steps, g8-art29-31-information, g8-tests-fixtures, int-readings, int-nouns, int-wiring, int-h-application, int-h-offence, int-tests-fixtures |

## 3. The integration layer

The integration layer is the 27 modules whose names begin `int-`.
It wires the nine groups to one another through the integration points IP1 to IP35 of the survey's plan, and it answers six headline questions.
A group module never imports another group's module; only `int-` modules (and the independent authors' `ind-` modules) do (`check.sh` checks this).

### 3.1 The six headline functions

Each headline takes `Readings of the fleet` (the reading taken at each of the 137 forks, see section 5) and the day, and each `@export` has a sentence and a `@desc` on every `GIVEN`.
Each headline first asks the gate (section 3.2) whether every unit of the Law its answer rests on was in force on the day, and refuses by name when one was not.

| headline | function (module) | what it answers | units the answer rests on (Articles as now numbered) |
| --- | --- | --- | --- |
| (a) may an application be granted | `Int (a) may the application be granted` (`int-h-application`) | whether the application includes what Article 11(2) requires and complies with 19(5), whether each of the six matters of 11(4) holds, which duty arises (register, refuse, neither, or the bar of 19(9)(c) or 20(1)(c)), the Commissioner's decision as a subject and an outcome (IP27) | 2, 5, 6, 7, 8, 11, 12, 19, 20 |
| (b) registered charity on a day, and what the register holds | `Int (b) is the entity a registered charity and what does the register hold` (`int-h-register`) | whether the entity is a registered charity (Article 1), the section it is entered in, the entries Article 8(3) requires for a registered charity or 8(5) for a formerly registered one, the public elements of the restricted section (9(1)), whether the recorded standing agrees with the dated entries | 1, 2, 5, 8, 9, 10 |
| (c) what follows from a contravention or a reportable matter | `Int (c) what follows from the contravention`, and four regulative rules: `Int (c) the Commissioner may serve a required steps notice`, `Int (c) the Commissioner may deregister the entity`, `Int (c) the court may exercise its powers on the Commissioner's application`, `Int (c) the governor must report the reportable matter` (`int-h-contravention`) | whether a provision was contravened (IP13), whether the conduct is misconduct (2(10)), which governors engage in misconduct (18(4)), the reportable matters of each governor (19(1)), the grounds for a required steps notice (27(1)), whether a ground of 16(1) exists, whether the court's powers are exercisable (14(1)), who is acting as the Commissioner (IP28), the effects of a deregistration (17) | 2, 5, 12, 14, 16, 17, 18, 19, 20, 22, 27 |
| (d) offence and penalty | `Int (d) the offence and the penalty for the act` (`int-h-offence`) | whether an act is an offence, the penalty (months of imprisonment and fine), whether an officer is also guilty (37(1)), the penalty of the officer, whether every penalty is within the cap of Schedule 2 paragraph 4(3)(f) | by the act: 21, 22, 23, 37 and Schedule 2 for a statement; 19, 37, Sch 2 for acting after reporting; 20, 37, Sch 2 for a disqualification order; 26, 37, Sch 2 for a demand or false information; 29, 10, 37, Sch 2 for disclosure |
| (e) which text and which units on a day | `Int (e) the text of the Law in force on`, `Int (e) the text of the Law in force at` (an instant), `Int (e) the units of the Law in force on` (`int-h-text`) | the vintage, the office "Minister" names, the Law that defines "Comptroller", whether (ba) is in Article 2(1), whether Schedule 1 carries the Dormant Bank Accounts words; the Parts, Articles and Schedules in force | none (it reports commencement) |
| (f) who may appeal what, and by when | `Int (f) who may appeal the decision`, `Int (f) was the appeal brought in time` (`int-h-appeal`) | the right of appeal (33), the third-party grounds at two times (33(5), IP9), the date the notice was served (38, IP34), the last day to appeal (36(2)) | 5, 12, 32, 33, 36, 38 |

Headline (e) itself refuses only for a day before 1 January 2019 and for 27 February 2024 (the text changed at 9.30 a.m. on that day; ask by instant).

### 3.2 The gate, the readings, the text of the Law

The gate is `Int the answer if every unit is in force` (`int-commencement`).
It takes a list of units (an Article as now numbered, or a Schedule), and returns the answer unless one is not in force on the day; then it refuses on the first such unit in the order listed, with a message of the form "Article N of the Charities (Jersey) Law 2014 (Part P) was not in force on the day asked: it came into force on <date>".
The stage of each Article is read from group G7's own commencement data (`Commencement: the unit of the Law is in force on`) by a script and written into `int-commencement.l4`; The integrator also read the Table of Legislation History independently and the two agree: Parts 1 to 3, Article 32, Articles 38 to 43 and the Schedules from 21 November 2014; Parts 4, 5 and 7 and Articles 33 to 37 from 1 May 2018; Part 6 (Articles 21 to 25) from 1 January 2019.
Group G7 registers the oddities of that Table (fork F7.3, F7.9); the gate takes G7's favoured readings.

`Readings of the fleet` (`int-readings`) holds one `Interpretation of ...` record per group.
Two of its readings are shared by several groups and are set once for all of them: the meaning of "year" for the annual return (IP33, groups G3 and G5) and the unit of a term of imprisonment (IP35, groups G6, G7, G8 and G9).
`Int the favoured readings of the fleet` gives the readings every group marks TYPICALLY; `Int the readings of the fleet are consistent` is the check that the shared readings are one value; a function per group replaces one field when a caller wants the other reading of a fork.

The text of the Law on a day is `Endnotes: the vintage of the text on` (group G7).
For 27 February 2024 it refuses, and `Int the answer under every text of the Law in force on` (`int-vintage`) answers a question about that day only if the two texts give the same answer, with a named refusal otherwise.
The regulative rules of headline (c) use the first form and so refuse on that day.

### 3.3 Cases and nouns

A headline that needs facts the groups keep apart takes one case record that bundles them (`int-nouns`, `int-h-*`): `Application in the case`, `Register entry in the case`, `Contravention case`, `Offence case`, `Appeal case`, `Body in the case`, `Person in the case`, `Notice served in the case`, `Notice of a decision in the case`, `Deregistration in the case`.
`domain.l4` is not edited (its sha256 is unchanged); every noun the groups asked for is defined in an `int-` module (section 3.5).

### 3.4 Where each integration point is wired

| IP | what is shared | wired by | tested in |
| --- | --- | --- | --- |
| IP1 | the day | the `day` argument of every headline (a DATE, not a `TODAY`) | every `int-tests-*` |
| IP2 | which of the nine texts | `Endnotes: the vintage of the text on` (G7), called by every headline; `int-vintage` for 27 February 2024 | `int-tests-vintage-matrix` |
| IP3 | the office "Minister" names | `Int IP3 the office of the Minister` (G1 `Art 1 the Minister under the text of`); read by G2 under reading B of F2.3 | `int-tests-consistency` (D), `int-tests-vintage-matrix` |
| IP4 | whether a unit is in force | the gate (section 3.2) | `int-tests-commencement` (144 assertions), the day scenarios of every headline |
| IP5 | the entity as Article 2 leaves it | `Int IP5 the entity` (G1 `Art 2 the body as an entity`, with the governors found by G6, IP21) | `int-tests-register`, `int-tests-wiring` |
| IP6 | whether the entity is a registered charity | `Int IP6 ...` = G1 `Art 1 the entity is a registered charity`; the recorded standing is kept as an input and compared with the dated entries (`the recorded standing agrees with the entries`) | `int-tests-register`, `int-tests-wiring`, `int-tests-consistency` (C) |
| IP7 | what the register holds | `Int IP7 the registered charity` (G3 data; the date deregistered from G6; the organized-religious flag from G8) | `int-tests-register` |
| IP8 | whether the charity test is met | `Int IP8 ...` = G2 `Art 5`; read by G4 (11(4)(a), with G4's input "will meet on registration"), G6 (16(1)(a)), G8 (27(1)(b)) | `int-tests-application`, `int-tests-contravention` |
| IP9 | the charity test at two times | headline (f) evaluates IP8 on the facts at each time | `int-tests-appeal` (F4) |
| IP10 | met only by virtue of an Order under 5(3) | `Int IP10 ...` = G2 `Art 5(3)`; read by G3 8(3)(i) | `int-tests-register` (B6) |
| IP11 | a purpose within Article 6(1)(c) | `Int IP11 ...` = G2 `Art 6`; read by G8 28(1)(a) | `int-tests-wiring` (the 2 x 2 of F2.5 and F8.3) |
| IP12 | misconduct | G1 `Art 2(10)` with the contraventions of IP13 | `int-tests-contravention`, `int-tests-chains` |
| IP13 | whether a provision was contravened | `Int IP13 ...` maps each kind of contravention to the group that decides the provision (12(7), 19(2), 19(4), 19(10), 20(6)); a breach shown by a `#TRACE` is passed in by naming the rule (`a duty or prohibition was breached, as a trace of the rule shows`) | `int-tests-contravention`, `int-tests-chains`; mutation M06 |
| IP14 | misconduct of a governor | G6 `Art 18(4)`, read by G8 27(1)(c) | `int-tests-contravention` (C2) |
| IP15, IP16 | the requirements of 11(4)(c) and (d) | G4 `Art 11(4)(c)` and `(d)`, read by G5 13(6)(d) and G8 27(1)(e) | `int-tests-wiring` (with fork F8.14) |
| IP17 | a principal address in Jersey | `Int IP17 ...` = G3 `Art 8(4)`, read by G4 11(4)(d) | `int-tests-wiring`, `int-tests-application` (A6) |
| IP18 | a name is undesirable | `Int IP18 ...` = G4 `Art 12(1)`, read by G4, G5 13(6)(b) and G8 33(5)(b) at two times | `int-tests-application` (A7), `int-tests-appeal` |
| IP19 | the required steps notices served | `Int IP19 ...` = G8 `Art 27(2)` with the date of service of IP34; read by G1, G3 8(3)(k), G6 16(1)(c) | `int-tests-chains`, `int-tests-contravention` (C4) |
| IP20 | an organized religious charity | G8 `Art 28`, read by G3 8(3)(h) and G6 19(9)(e)(i) | `int-tests-register` (B3) |
| IP21 | the reportable matters of a governor | `Int IP21 ...` = G6 `Art 19(1)` for each governor of the entity | `int-tests-contravention` (C5), `int-tests-chains` |
| IP22, IP23, IP24 | 19(5) complied with; 19(9)(c) bars the grant; the court has ordered that the entity must not be registered | `Int IP22`, `IP23`, `IP24` (G6), read by G4 | `int-tests-application` (A2, A3, A8) |
| IP25 | information in a public part of the register | G3 `Art 10(3)` through the body, the matter and the Commissioner's designation, read by G8 29(1) | `int-tests-wiring` (IP25 chain) |
| IP26 | an excepted foreign charity | G7 `Art 22`, read by G1 2(10)(b) and G7 21(5), (6) | `int-tests-contravention` (C7), `int-tests-wiring` |
| IP27 | the Commissioner's decisions | G3, G4, G5, G6, G8 produce a subject and an outcome; G8 Article 33 and G9 Schedule 1 paragraph 4(3) consume it | `int-tests-decisions` (24 assertions) |
| IP28 | someone is acting as the Commissioner | G9 `Sch 1 para 4(5)`, returned by headline (c) and conjoined with G5's court-powers fact | `int-tests-contravention` (C3); mutation M04 |
| IP29 | an Order under 13(9) applies | split: limb (b) for G4's 11(2)(e)(ii), limb (c) for G3's 8(3)(m); G5's composite is kept as the alternative | `int-tests-wiring`, `int-tests-application` (A13, A14); `int-tests-red` (seam 2) |
| IP30 | the penalty an offence carries | the owning group's penalty, carried to an officer by G7 37(1) and checked against the cap by G9 | `int-tests-offence` |
| IP31 | the kinds of order the court may make | no wiring: the shared type `Order of the court over a charity` of `domain.l4` is used by G5 (14(3)) and G6 (17(9)) | by type: both modules check against the one declaration |
| IP32 | why an entity was deregistered | G6 `Art 16 the basis of deregistration`, returned among the effects in headline (c) | `int-tests-contravention` (C4) |
| IP33 | the meaning of "year" | one value set in G3 and G5 by `Int the readings of the fleet` | `int-tests-readings`, `int-tests-consistency` (A); mutation M11 |
| IP34 | the date a notice was served | `Int IP34 ...` = G7 `Art 38` on the dates sent and received and any Order; used for required steps notices, the deregistration notice and the notice of a decision | `int-tests-chains`, `int-tests-appeal` (F2); mutations M01b, M12b |
| IP35 | the unit of a term of imprisonment | one value set in G6, G7, G8 and G9 | `int-tests-readings`, `int-tests-consistency` (B); mutation M10; `int-tests-red` (seam 1) |

### 3.5 Nouns requests, and how each was resolved

`domain.l4` was not edited: its sha256 is the one the integrator started with, so the zero-regression re-run that an edit would have required did not arise.
The rule was that `domain.l4` may be changed only additively: a new type is allowed, a new field on an existing record is not (it breaks every construction of that record), and a new constructor on an existing enumeration is not unless no `CONSIDER` becomes non-exhaustive.
Every request in the nine fragments falls into one of three kinds.

Resolved by wiring in an `int-` module (no change to `domain.l4`):

- G4 request 4 and G3's use of it (IP29 should be two facts): `Int IP29 an Order under Article 13(9)(b) applies` for G4 and `(c) applies` for G3, with G5's composite kept as the alternative (section 6.10).
- G4 request 5, G5 request 1 and G8 request 9 (the outcome and subject of the Commissioner's decisions, IP27): each producer's decision is passed to G8's Article 33 and G9's Schedule 1 paragraph 4(3); `int-tests-decisions.l4` runs every producer through both.
  The two subjects G5 asked to add (the prior permission of 13(5)(b) and the permission of 13(11)(b)) are not added to the enumeration; they are read as "any other matter", so a registered charity has no appeal and the Attorney General has one (33(4)); `int-tests-decisions.l4` asserts this for the prior permission of 13(5)(b), and the permission of 13(11)(b) takes the same path.
- G6's requests about dates of notices and `date deregistered`, G6's `Governor` with `reportable matters`, and G6's record of a governor's conduct (IP21, IP34, Article 18(4)): `Int IP34 ...` sets the date of the deregistration from the notice, `Int IP21 ...` fills each governor's reportable matters, `Governor conduct in the case` carries the conduct (`int-wiring`, `int-h-contravention`).
- G3 request 8, G6 and G7's `Interpretation` fields for the shared year and unit (IP33, IP35): one value set in all groups by `Int the readings of the fleet`.
- G7 request 4 (a standard input missing from the plan): `the entity is wholly or mainly managed or controlled in or from within Jersey` is a field of the act `a statement about an entity` in `int-h-offence`.
- G3 request 4 (a producer for `the registered charity`, IP7): `Int IP7 the registered charity` in `int-h-register`.

Kept in the group (the group's stand-in stays and the integrator uses it where a wire needs it): G1 requests 1 to 3; G2 N3 to N6; G3 requests 1, 2, 5 to 7; G4 requests 1 to 3, 7, 8; G5 requests 3 to 5; G6 (the nouns of Articles 17, 19 and 20, and `Party after deregistration`); G7 requests 1 to 3, 5, 7; G8 request 3; G9 requests 1 and 2.
The groups' stand-ins are not merged into one type per concept (one act type for the Law, one annual-return record, one application record), because every merge would change a record or an enumeration that a group's tests construct or match.

Not done, because `domain.l4` could be changed only additively: a field added to `Purpose`, `Entity`, `Governor` or `Registered charity` (G2 N1 and N2, G3 request 3, G3 request 2 and G4 request 2 for previous registered names, G5 request 2 for the financial year end); a constructor added to `Legal actor` (G6, G7 request 1, G9 request 1; `Legal actor` is matched exhaustively in G2) or to the subjects of a decision (G5 request 1); a unit field on `Penalty provided` (G7 request 6, G8 request 5; defect X2).
Where such a fact crosses groups, the owning group's own input record carries it (G3's `Facts for the annual return entry (Article 8(3)(j))` for the financial year end, G3's `Facts for the items of Article 8(3)` for previous registered names, `Facts for the principal address (Article 8(4))` for the governors' addresses), and the integrator's case records pass it on.
The renames asked for by G8 request 1 and 2 and G1 request 5 (the constructor `the registered charity`; fields that begin with "is" or "has") are not the integrator's to make (defects X6 and X8).

### 3.6 After the independent testing: what was rewired (2026-10-27)

Two groups were repaired after the independent tests found defects (section 13.1).
G2 gave `Facts about a purpose under Article 6` a tenth field (the object of improving the conditions of life, a MAYBE BOOLEAN, default NOTHING), gave `Interpretation of Articles 3 to 7` a thirteenth (fork F2.13, default: the Commissioner's staff are bound as the Commissioner is), added `interp` as the last input of nine rules, made the charity test answer FALSE for a body that is not an entity, and added a constructor to `Limb of the charity test that decides it`.
G7 made a Part's stages come from every Article the Part held (Part 9 now has three stages) and added `the entity` as the first input of four rules of Article 21, with a guard on every Article 21 and 23 rule whose text names an entity.
What the integrator rewired:

- `int-readings.l4` (generated from the interpretation records) now sets the thirteenth field of the G2 reading, from the reading G2 marks TYPICALLY; `int-tests-fixtures.l4` (generated) now sets the tenth field of the shared Article 6 facts to NOTHING.
- No other `int-` module changed.
  None of them calls a rule whose signature changed: headline (a) reaches G2 through `Art 5`, `Art 5(3)` and `Art 6 ... advancement of religion`, whose inputs are unchanged, and it passes G1's derived `kinds of entity`, so a body with none is refused as a non-entity without further wiring.
- The new input of headline (a) comes from the caller, inside the record `Purpose with the facts Article 6 reads` of each purpose of the body in the case (default NOTHING); a purpose of head (i) without it is refused by name (`int-tests-repairs.l4`, R1).
- F2.13 is a field of `Readings of the fleet` like any other fork; `who` for the rules of Articles 7 and 5(5) is the caller's fact (section 6.13).
- `int-tests-repairs.l4` tests what changed through the headlines (48 assertions at that point, scenarios R1 to R6 of section 10.8; section 3.7 adds R7): a recreational purpose with and without the object; a partnership applicant; a staff determination on both readings of F2.13; Part 9 and the original Article 41 in headline (e) on both readings of F7.9; a non-entity saying it is a charity at headline (d); and the gate of headline (a) on 30 April and 1 May 2018.
- At the end of this rewiring the integration modules held 586 assertions, including the 538 of the first pass, and all of them passed on the repaired groups; section 3.7 gives the count after F2.14.

### 3.7 After the comparison: fork F2.14, Article 6(2)(e) (2026-10-27)

Group G2 added a fourteenth fork, F2.14: whether Article 6(2)(e) ("paragraph (1)(n) includes relief given by the provision of accommodation or care") adds an operand to head (n) of Article 6(1), or only says that relief of those in need can be given by accommodation or care.
The label of the default is "default ruled by the owner (Meng), 2026-10-27; the widening reading stays callable".
Reading A (the default) is declaratory: relief given by accommodation or care is within head (n) only as relief of those in need.
Reading B widens: the provision of accommodation or care is within head (n) without more, and B stays callable as `the interpretation of Articles 3 to 7 with F2.14 read as B`.
G2 gave `Facts about a purpose under Article 6` an eleventh field, `the purpose is the provision of accommodation or care` (a BOOLEAN, TYPICALLY FALSE), gave `Interpretation of Articles 3 to 7` a fourteenth, `how Article 6(2)(e) is read`, and added `interp` as the last input of `Art 6(2)(e) paragraph (1)(n) includes the purpose, as relief given by accommodation or care` and of `Art 6(2) a clarification brings the purpose within a head`.
What the integrator rewired:

- `int-readings.l4` (generated) now sets the fourteenth field of the G2 reading from the reading G2 marks TYPICALLY; `int-tests-fixtures.l4` (generated) now sets the eleventh field of the shared Article 6 facts to FALSE.
- No other `int-` module needed a change.
  No `int-` rule calls `Art 6(2)` or `Art 6(2)(e)` directly (checked by searching the `int-` modules): headline (a) reaches Article 6 through `Art 5 the entity meets the charity test` and `Art 6 the entity has a purpose within the advancement of religion` (`int-wiring.l4`), whose inputs did not change, with the reading taken from `Readings of the fleet`.
- The new fact comes from the caller, inside the record `Purpose with the facts Article 6 reads` of each purpose of the body in the case, as the tenth field does; the default of the record is FALSE, not NOTHING, because G2 declares it a plain BOOLEAN, so a row that leaves it out takes FALSE and reading B then agrees with reading A.
  The integrator did not derive it from anything.
- The one test module that built the facts record by hand, `int-tests-repairs.l4` (R1), gained the field set to FALSE, and an import of `g2-art6-purposes` for the purpose-level assertions of R7 (an `int-` module may import across groups).
- `int-tests-repairs.l4` has a seventh scenario, R7 (18 assertions, section 10.8), run at the purpose level (`Art 6(1) the purpose is a charitable purpose`) and through headline (a); the expected values were decided from the text of Articles 5(1)(b), 6(1)(n), 6(2)(e) and 7(3)(a) before the module was run.
- The fork is not wired from anywhere else: no other group's rule depends on Article 6(2)(e) (checked by searching the modules for `accommodation or care` and `6(2)(e)`), so there is no entry for it in the consistency register of section 6.

## 4. Coverage

The survey divided the Law into 851 provisions (rows of `phase1/coverage.tsv`: the Title, the Long title, the commencement note, each Article and each paragraph, sub-paragraph and definition that is a rule, each Schedule paragraph and the endnote tables).
Each group's fragment has a coverage table with one row per provision of its scope, naming the disposition (`encoded`, `inert`, `refused`, `out-of-scope`, `deferred`), the module and the rule that carries it.
`coverage-all.tsv` is those nine tables read by a script (`gen_coverage_all.py` in the integrator's working directory, not deposited), with the columns `provision`, `disposition`, `module`, `group`, and a fifth, `id`, the survey's key, which the script needs because the provision text is not unique (for example every definition of Article 1 is a row).
The comparison with the survey's table is below.
The module column names a deposit file for every row (checked by the script).
`encoded` means a rule or data in a module decides it; `inert` means a heading, pointer or definition that carries no rule of its own and is kept as quoted text; `refused` means the encoding answers by naming a refusal; `out-of-scope` means a row whose own enactment is not encoded (the group holds a stub that quotes the line).

Coverage tables read from the nine fragments: 851 rows (the survey's phase1/coverage.tsv has 851).

| group | rows | encoded | inert | refused | out-of-scope | deferred | other |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | 113 | 76 | 25 | 0 | 12 | 0 | 0 |
| G2 | 90 | 81 | 9 | 0 | 0 | 0 | 0 |
| G3 | 82 | 82 | 0 | 0 | 0 | 0 | 0 |
| G4 | 73 | 73 | 0 | 0 | 0 | 0 | 0 |
| G5 | 58 | 58 | 0 | 0 | 0 | 0 | 0 |
| G6 | 99 | 99 | 0 | 0 | 0 | 0 | 0 |
| G7 | 129 | 110 | 18 | 1 | 0 | 0 | 0 |
| G8 | 104 | 96 | 6 | 0 | 2 | 0 | 0 |
| G9 | 103 | 80 | 22 | 1 | 0 | 0 | 0 |
| all | 851 | 755 | 80 | 2 | 14 | 0 | 0 |

The survey's own dispositions, for comparison: encoded 745, inert 82, refused 1, out-of-scope 23, deferred 0.

Rows in the survey and in no fragment: 0.

Rows in a fragment and not in the survey: 0.

Ids that occur twice among the fragments: 0.

Rows whose group differs from the survey's: 0.

Rows whose module column names something that is not a .l4 file of the deposit: 0.

Rows whose disposition differs from the survey's: 17.

| id | survey | fragment | group |
| --- | --- | --- | --- |
| 4(3) | inert | encoded | G2 |
| 4(3)(a) | inert | encoded | G2 |
| 4(3)(b) | inert | encoded | G2 |
| 4(3)(c) | inert | encoded | G2 |
| 41 | out-of-scope | encoded | G7 |
| 41(1) | out-of-scope | encoded | G7 |
| 41(1)(a) | out-of-scope | encoded | G7 |
| 41(1)(b) | out-of-scope | encoded | G7 |
| 41(1)(c) | out-of-scope | encoded | G7 |
| 41(2) | out-of-scope | encoded | G7 |
| 42 | out-of-scope | encoded | G7 |
| 42(a) | out-of-scope | encoded | G7 |
| 42(b) | out-of-scope | encoded | G7 |
| Sch 1 | encoded | inert | G9 |
| Sch1 2(4) | encoded | inert | G9 |
| Sch 2 | encoded | inert | G9 |
| Sch2 4(3)(e) | inert | refused | G9 |

`coverage-all.tsv` has 851 data rows.

## 5. Fork index

A fork is a place where the Law's words allow more than one reading and the encoding takes one, marks it `TYPICALLY` in a field of its group's `Interpretation of ...` record, and keeps the others callable with a test.
The index below is generated by a script (`forkindex.py`, in the integrator's working directory) from the nine fragments' fork registers and the nine interpretation records.
There are 137 forks: G1 8, G2 14, G3 13, G4 12, G5 14, G6 24, G7 14, G8 19, G9 19.
The thirteenth fork of G2, F2.13, was added on 2026-10-27 after the independent testing.
The fourteenth, F2.14 (does Article 6(2)(e) add an operand to head (n), or only say that relief of those in need can be given by accommodation or care?), was added on 2026-10-27 after a comparison with an independent encoding of Articles 5 to 7, once the encoders had finished: default ruled by the owner (Meng), 2026-10-27; the widening reading stays callable.
Each fork is carried by exactly one field of its group's record, and no field is without a fork (checked by the script).
The question column is the text of the fork's heading in the group's fragment; G7 writes its headings without text, so for its rows the question is the phrase that names the field of its record in the fork's section (`Field and constructors`), put as an indirect question in the form of the G6 rows, and for the five forks whose field is a noun phrase (F7.3, F7.5, F7.6, F7.7, F7.8) the script holds the question and stops if the fragment's phrase changes.
The script also stops, naming the fork and the column, on an empty cell in any row; the table as deposited after the second pass had fourteen empty question cells (every G7 row), and a reader found them.
The reading taken is the constructor the field is marked `TYPICALLY`, which is what `Int the favoured readings of the fleet` uses.
Each fork's discriminating case, the text that licenses each reading, and the reasons for the choice are in the group's fragment, section "Fork register" (section 2 of each fragment, in G6 section (2)), under the heading with the fork's id.

| id | group | the question | the reading taken |
| --- | --- | --- | --- |
| F1.1 | G1 | does "(a) to (h)" reach the inserted sub-paragraph (ba)? | the ranges follow the letters of the amended list, so (ba) is inside (a) to (h) |
| F1.2 | G1 | do the words "in relation to ..." in 2(10)(b) govern every limb (i) to (vi)? | every limb (i) to (vi) needs the offence to be in relation to a charity or an equivalent entity |
| F1.3 | G1 | what is the constitutional Law of a body incorporated "under, but not by," an enactment? | none, because Article 2(5) names no Law for sub-paragraphs (g) and (h) |
| F1.4 | G1 | which cases of the lists in 2(4) to 2(7) apply to a body in more than one kind? | every case of Article 2(4) to (7) that applies |
| F1.5 | G1 | is information "published" on the publisher's opinion or on the manner's likelihood? | the opinion of the person publishing |
| F1.6 | G1 | does "in relation to Jersey" in 2(1)(e) qualify (iii) only, or each of (i) to (iii)? | only the Royal Charter in sub-paragraph (iii) |
| F1.7 | G1 | is the standing of a "registered charity" read when the conduct occurred or when the question is asked? | when the conduct in Article 2(10) occurred |
| F1.8 | G1 | does sub-paragraph (g) overlap (c), (d) and (f)? | as written, so a foundation or an incorporated 1862 association is also within (g) |
| F2.1 | G2 | all of its purposes with no purposes, and with ancillary purposes alone | at least one charitable purpose is required, and an ancillary purpose counts only beside one |
| F2.2 | G2 | acting in that capacity | the person must be permitted to act as a Minister, a member of the States Assembly or an equivalent |
| F2.3 | G2 | a Minister or "the Minister" | any Minister of the Government of Jersey |
| F2.4 | G2 | within a reasonable time and "as soon as practicable" (periods P1 and P2) | by an input judgement that the time taken was reasonable or practicable |
| F2.5 | G2 | a philosophical-belief purpose: (p) or (c)? | paragraph (1)(p), by the analogy that Article 6(2)(f) states |
| F2.6 | G2 | how the days of a period measured from an event are counted (periods P1 and P2 under F2.4's second reading) | the day of the event is not counted, so the day after it is the first day |
| F2.7 | G2 | Before issuing or amending guidance (period P3) | the consultation and the report must fall on an earlier day than the day the guidance is issued or amended |
| F2.8 | G2 | do the examples in 4(3) add to 4(2)? | the examples illustrate Article 4(2) and are bound by its conditions |
| F2.9 | G2 | so far appears to him or her to be reasonably practicable | each limb binds so far as it appeared reasonably practicable |
| F2.10 | G2 | what follows from a determination of public benefit made in breach of the duties on its maker | the determination does not answer the question |
| F2.11 | G2 | the promotion of equality and diversity | a purpose must promote both equality and diversity |
| F2.12 | G2 | which guidance do Articles 5(6) to 5(8) apply to? | the guidance under Article 5(4), including the guidance on public benefit that Article 7(4) requires it to contain |
| F2.13 | G2 | is a member of the Commissioner's staff, exercising the Commissioner's function, bound as the Commissioner is? | a member of staff exercising a function of the Commissioner under Schedule 1 paragraph 4(3) is bound as the Commissioner is |
| F2.14 | G2 | does Article 6(2)(e) add an operand to head (n)? | Article 6(2)(e) is declaratory: relief given by accommodation or care is within paragraph (1)(n) only as relief of those in need |
| F3.1 | G3 | Article 8(6): from when do the ten years of retention run? | from the day the Commissioner receives or makes each copy |
| F3.2 | G3 | Article 8(3)(j): which year is "the most recent year"? | the calendar year |
| F3.3 | G3 | Article 10(4): does "a particular registered charity" include a deregistered entity? | a registered charity is an entity entered in the general or the restricted section only |
| F3.4 | G3 | Every period of years: is the day of the event counted? | the day of the event is not counted, so the last day of the period is the anniversary |
| F3.5 | G3 | Adding a year to a date that does not exist in the target year | the date moves back to the last day of the month |
| F3.6 | G3 | The day on which an entry in a section takes effect | on the day of the entry |
| F3.7 | G3 | Article 8(3)(j): which year is the most recent, on the day asked? | the latest year that has ended before the day asked |
| F3.8 | G3 | Article 8(3)(k): is a notice noted once it has been complied with? | every notice that has been served |
| F3.9 | G3 | Article 8(4)(a): which entities are within "a company, foundation, or other entity required by its constitutional Law to have a registered office or business address in Jersey"? | an entity that its constitutional Law requires to have a registered office or business address in Jersey |
| F3.10 | G3 | Article 8(4)(b), (c): main premises that are a private dwelling house | Article 8(4)(b) does not apply, so Article 8(4)(c) is reached |
| F3.11 | G3 | Article 8(5)(b): "if the entity was registered in the general section" | the section the entity was entered in immediately before deregistration |
| F3.12 | G3 | Article 9(2): who must meet the condition? | whoever makes the request, an applicant for registration or a registered charity |
| F3.13 | G3 | Article 8(3)(a): does it reach sub-paragraph (ba) of Article 2(1)? | Article 8(3)(a) reaches only the sub-paragraphs it names |
| F4.1 | G4 | the 12 months preceding the application | the twelve months ending on the day before the application |
| F4.2 | G4 | the date of "the application" | the day the application is lodged |
| F4.3 | G4 | an application that does not comply | no duty to register or to refuse arises while the application does not comply |
| F4.4 | G4 | the duty to register against the bars on granting | a bar on granting the application displaces the duty to register |
| F4.5 | G4 | is a formerly registered charity "another registered charity" | a formerly registered charity is not another registered charity |
| F4.6 | G4 | a year before 29 February | a year before 29 February is 28 February |
| F4.7 | G4 | which names of another charity Article 12(1)(a) compares | its registered name and its alternative registered names |
| F4.8 | G4 | a previous registered name of the charity itself | a previous registered name is not one of its registered names |
| F4.9 | G4 | counting the period for the Commissioner's decision | the period starts the day after the date of the application |
| F4.10 | G4 | reasonable time and as soon as practicable, for the guidance | as a determination the caller supplies |
| F4.11 | G4 | the payee who is a governor | a payee who was a governor when the payment was made |
| F4.12 | G4 | applies or should be applied in Article 11(4)(f) | a ground of mandatory refusal applies, or a ground of discretionary refusal should be applied |
| F5.1 | G5 | promptly (13(6)); period P8, a standard of promptness | an input judgement that the report was made promptly |
| F5.2 | G5 | the year to which the return relates (13(7), 13(9)(a)); period P9, a reporting period; integration point IP33 | the calendar year |
| F5.3 | G5 | any Order under paragraph (7), (8) or (9) (13(10)); trap T18 | the Order under paragraph (7) as extended by paragraph (8) |
| F5.4 | G5 | misconduct in the administration of the charity (14(1)(a)) | misconduct within Article 2(10) that bears on the administration of the charity |
| F5.5 | G5 | is a return sent on the due date timely? (13(8)); period P10, a deadline | timely if sent on or before the due date |
| F5.6 | G5 | the day deregistration takes effect (13(1)); the period of registration | outside: registered up to the day before deregistration takes effect |
| F5.7 | G5 | a purpose that is not charitable (13(2)) | any purpose that is not a charitable purpose under Article 6, a purely ancillary purpose included |
| F5.8 | G5 | paragraphs (a) and (b) of 13(5), joined by "or" | either the original condition, or after a prior permission and a cessation the different condition |
| F5.9 | G5 | the first day of a period fixed by the court (14(3)(a), (b), (g)); a period fixed by an order | the first day named is the first day of the period |
| F5.10 | G5 | counting the days when "promptly" is a number of days (13(6), readings B and C of F5.1) | the day of the event is not counted: the last prompt day is the event day plus the number of days |
| F5.11 | G5 | the anniversary of a registration made on 29 February (13(7), reading C of F5.2) | the last day of February (the day is clamped, as daydate add years does) |
| F5.12 | G5 | the three purposes of an order under 14(2) | at least one of the three purposes |
| F5.13 | G5 | when a matter "arises" for the annual return (13(7)) | the date of the event or proposal |
| F5.14 | G5 | which statement a payment is judged by (13(11)(a)) | the statement in force on the day of the payment |
| F6.7 | G6 | which governors Article 18(2) binds | only the governors of unincorporated bodies within Article 2(1)(i) |
| F6.8 | G6 | what the reasonable time of Article 18(4)(d)(ii) qualifies | the reasonable time qualifies only the failure to take proper steps |
| F6.24 | G6 | whether assisting another governor is misconduct only if that governor engages in misconduct | the assisting or encouraging is misconduct only if the other governor engages in misconduct |
| F6.9 | G6 | whether a disqualification that has ended is a reportable matter | a disqualification counts although it has ended |
| F6.10 | G6 | when the ban of Article 19(10) starts | the ban starts on the report to the Commissioner |
| F6.11 | G6 | whether acting in breach of Article 19(2) or (4) is an offence | Article 19(11) reaches only paragraph (10) |
| F6.12 | G6 | how a report is judged prompt under Article 19(2) | promptness is a determination supplied as an input |
| F6.14 | G6 | how the fifteen years of Article 20(5) are counted | the last day is the anniversary, and 29 February falls back to 28 February |
| F6.15 | G6 | how the duty in Article 19(9)(e)(i) stands against Article 28(3) | Article 28(3) prevails and no duty to require removal arises for an organized religious charity |
| F6.16 | G6 | how a term of imprisonment of one year or two years is measured | calendar months |
| F6.20 | G6 | whether a declaration given on the day of the application is in time | a declaration given on the day of the application is in time |
| F6.21 | G6 | from when a governor who has been notified is in breach of Article 19(4) | the governor is in breach from the day after the notification |
| F6.22 | G6 | whether the last day named in a time limit is inside the permission | the day named is the last day of the permission |
| F6.23 | G6 | whose view of expediency lets a person apply under Article 20(3) | only the applicant's own view that it is expedient |
| F6.1 | G6 | what follows where the entity has not complied with Article 15(2) | no duty arises under Article 15(3) |
| F6.2 | G6 | how Article 16(2) relates to the procedure of Article 16(1) | Article 16(2) governs alone and the duty arises on satisfaction with no prior notice |
| F6.13 | G6 | whether the time for objections must be reasonable | the time specified must be reasonable or the deregistration is not authorised |
| F6.17 | G6 | when the Commissioner may deregister after giving the preliminary notice | the Commissioner may deregister only after the last day for objections |
| F6.19 | G6 | when the entity has failed to comply with a required steps notice | the notice has not been complied with once the time it names has ended without the steps taken |
| F6.3 | G6 | which notice Articles 17(2)(c) and 17(4) mean | the notice by which the Commissioner deregisters |
| F6.4 | G6 | the date before which property must have been acquired to be remaining property | acquired before the date from which the termination takes effect |
| F6.5 | G6 | when the ten years of Article 17(1)(a) start | the ten years run from the date of the deregistration notice |
| F6.6 | G6 | how long the bar on assigning the registered number lasts | the bar on assigning the registered number has no end |
| F6.18 | G6 | how the ten years of Article 17(1)(a) are counted | the last day is the anniversary, and 29 February falls back to 28 February |
| F7.1 | G7 | how a day on which a text takes effect at a stated time is treated | a question about that day alone is refused |
| F7.2 | G7 | how “7 days after it is made” is counted | the day of making is left out |
| F7.3 | G7 | which numbering the commencement table speaks in | the table is in the original numbers |
| F7.4 | G7 | how the strict and the knowing offences combine for one act | both offences are made out |
| F7.5 | G7 | whether the wording of the advantage limb of the knowing offences is kept as printed or harmonised | the wording differs as printed |
| F7.6 | G7 | which bodies are within Article 37(1) | only partnerships and bodies corporate |
| F7.7 | G7 | on which date a notice is served | the date of receipt |
| F7.8 | G7 | in what unit a term of imprisonment is counted | calendar months |
| F7.9 | G7 | how a Part brought into force in two stages is treated | in force when all its Articles are |
| F7.10 | G7 | how capacity is paired with the kind of body in Article 37(1) | capacity as printed for each kind of body |
| F7.11 | G7 | how the day named as the day of commencement is counted | the named day is the first day in force |
| F7.12 | G7 | whether Article 22 defines an excepted foreign charity outside Article 21 | Article 22 defines the term wherever the Law uses it |
| F7.13 | G7 | whether adapting Articles 21 to 23 under Article 24(3)(a) can carry their imprisonment | the cap of Article 24(4) applies to every offence of the Regulations |
| F7.14 | G7 | whether an Order under Article 2(2) can make consequential amendments of other provisions of the Law | only Regulations can make consequential amendments of this Law |
| F8.1 | G8 | when does the one year of Article 26(5)(a) start? | the year of Article 26(5) runs from the day the document is provided or retained |
| F8.2 | G8 | what is "as soon as practicable" in Article 26(6)? | promptness under Article 26(6) is a judgement the caller supplies |
| F8.3 | G8 | does Article 28(1)(a) "by virtue of Article 6(1)(c)" reach a philosophical-belief purpose? | only a purpose within Article 6(1)(c) counts under Article 28(1)(a) |
| F8.4 | G8 | is the list of appealable decisions in Article 33 closed? | the list of appealable decisions in Article 33 is closed |
| F8.5 | G8 | on what ground is a decision of the tribunal appealed to the court? | a decision of the tribunal is appealed to the court only on the ground in Article 35(1) |
| F8.6 | G8 | from when does an appeal time limit under Article 36(2) run? | an appeal time limit under Article 36(2) runs from the notice of the decision |
| F8.7 | G8 | how is a period fixed by a notice counted (Articles 26(1)(a), (b) and 27(2))? | the day of service is not counted in a period fixed by a notice |
| F8.8 | G8 | in what unit is a term of imprisonment measured in Articles 26(7), 26(10) and 29(1)? | calendar months |
| F8.9 | G8 | does the one year end on the anniversary of the day it starts, or on the day before? | the year of Article 26(5) ends on the anniversary of the day it starts |
| F8.10 | G8 | what is a year from 29 February in Article 26(5)(a)? | a year of Article 26(5) from 29 February ends on 28 February |
| F8.11 | G8 | which consents does Article 29(1) require? | Article 29(1) requires both consents |
| F8.12 | G8 | is the first day counted in an appeal time limit under Article 36(2)? | the day of the anchor is not counted in an appeal time limit |
| F8.13 | G8 | who is excluded from appealing under Article 33(5)? | any applicant for registration or registered charity is excluded from appealing under Article 33(5) |
| F8.14 | G8 | does Article 27(1) "if the Commissioner believes that" make the belief alone the ground? | the Commissioner's belief alone is the ground under Article 27(1) |
| F8.15 | G8 | may a notice on any ground of Article 27(1) require a governor to be suspended, removed or replaced? | only a notice under Article 27(1)(c) or (d) may require a governor to be suspended, removed or replaced |
| F8.16 | G8 | does Article 33(2)(a) "a decision to deregister the charity" reach a deregistration granted on the charity's own application? | Article 33(2)(a) reaches a deregistration granted on the charity's own application |
| F8.17 | G8 | when must a person have been a governor to fall within Article 26(2)(b)? | a governor at any time of an entity registered at any time falls within Article 26(2)(b) |
| F8.18 | G8 | how do the two grounds of Article 33(5) combine with the two times? | each ground of Article 33(5) must hold at both times |
| F8.19 | G8 | which charity does Article 26(4)(a) speak of? | the registered charity of Article 26(4)(a) is a charity registered now |
| F9.1 | G9 | at least 2 weeks before appointing (Sch 1 1(3), src:760; Sch 2 1(3), src:818; P29, P38) | the appointment is 14 or more days after the notice |
| F9.2 | G9 | being not more than 6 years (Sch 1 1(5), src:762; Sch 2 1(5), src:820; P30, P39) | the end date is the day the term expires |
| F9.3 | G9 | resigns ... by giving not less than 3 months' notice in writing to the Minister (Sch 1 3(1)(a), src:780) and "one month's notice" (Sch 2 2(1)(a), src:826; P31, P40) | the office ends when the notice period runs out, the months being clamped |
| F9.4 | G9 | absent ... for a period longer than 4 consecutive weeks (Sch 1 3(2)(a), src:784) and "8 consecutive weeks" (Sch 2 2(2)(a), src:830; P32, P41) | the days of absence are counted, the first and the last included |
| F9.5 | G9 | not more than 2 weeks after terminating the appointment (Sch 1 3(3), src:788; Sch 2 2(3), src:834; P33, P42) | the 14th day after the termination day is in time |
| F9.6 | G9 | completes 12 years (whether consecutive or in aggregate) of service (Sch 1 3(4)(c), src:792; Sch 2 2(4)(c), src:838; P34, P43) | twelve calendar years measured in days from the first day of service |
| F9.7 | G9 | in no case later than 4 months after the end of that year (Sch 1 4(9), src:808; Sch 2 3(4), src:843; P36, P44) | the months are added and the day is clamped to the end of the month |
| F9.8 | G9 | the decision under Article 15(3) on whether to refuse to deregister a charity (Sch 1 4(3)(b), src:798; trap T17) | both outcomes of the decision are reserved |
| F9.9 | G9 | subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017 (Sch 1 2(4)(a), src:776, and 4(7), src:806; trap T22) | the Fund bears the cost in place of the annual income of the States |
| F9.10 | G9 | as soon as practicable (Sch 1 4(9) and (10), src:808 and src:809; Sch 2 3(4) and (5), src:843 and src:844; P37, P44) | as soon as practicable is a judgement supplied as an input |
| F9.11 | G9 | service as a designated relevant person (Sch 1 3(4)(c), src:792, with 4(4) and (5), src:800 to src:804) | service as a designated relevant person does not count |
| F9.12 | G9 | a report "in each calendar year" for a year in which the office was held only in part (Sch 1 4(8), src:807; Sch 2 3(3), src:842; P35, P44) | a report is required for the part of the year in which the office was held |
| F9.13 | G9 | a penalty not exceeding imprisonment for a term of 2 years and a fine (Sch 2 4(3)(f), src:857; P45, IP35) | calendar months |
| F9.14 | G9 | Before appointing a person ... the Minister must seek the views (Sch 1 1(2), src:759; Sch 2 1(2), src:817) | the views were sought on an earlier day than the day of the appointment |
| F9.15 | G9 | (b) the vice-chair, if the chair is absent; or (c) if both the chair and vice-chair are absent (Sch 2 4(1), src:846 to src:849) | a vacant office counts as absent |
| F9.16 | G9 | the decision on entry in the restricted section (Sch 1 4(3)(a), src:797; Articles 9(6) and (7), src:280 to src:286; 11, src:298) | it is not reserved because it is not a decision under Article 11 |
| F9.17 | G9 | the person becomes a member of the States (Sch 1 3(4)(b), src:791; Sch 2 2(4)(b), src:837) | only becoming a member during the appointment ends it |
| F9.18 | G9 | at least one member of staff to serve as the responsible officer against "the responsible officer" (Sch 2 3(2), src:841, and 3(3) to (5), src:842 to src:844) | the one member of staff the Minister has named is the responsible officer |
| F9.19 | G9 | after satisfying himself or herself that the person has been absent ... for a period longer than (Sch 1 3(2)(a), src:784; Sch 2 2(2)(a), src:830) | the Minister's satisfaction and the absence longer than the number of weeks are both required |

Total: 137 forks.

## 6. The cross-group consistency register

This register lists the questions that two or more groups answered, and where they answered them differently or by a different convention.
Nothing is silently harmonised.
Where two answers differ, both are recorded here, the fleet default of the brief is wired (each group's `TYPICALLY` reading, collected by `Int the favoured readings of the fleet`), and the other reading is a callable function with a test.
The tests are `int-tests-counting.l4`, `int-tests-consistency.l4`, `int-tests-vintage-matrix.l4`, `int-tests-wiring.l4`, `int-tests-decisions.l4` and `int-tests-red.l4`.
Each expected value was decided by hand from the Law before the module was run.
Items 6.1 to 6.4 and 6.9 hold seams that remain open; 6.5 to 6.8 and 6.10 to 6.13 are cases where the groups agree or where the integrator records which group decides.

### 6.1 How a period of days is counted

The groups took two conventions, and each applies where the Law's words put it.
The `daydate` functions `add years` and `add months` clamp to the last day of a month in every group that uses them (29 February falls back to 28 February).

| family | the rule | taken by (fork) | the other reading |
| --- | --- | --- | --- |
| (1) after an event | the day of the event is not counted; the last day is the event day plus N; a period of years ends on the anniversary | G3 (F3.4: retention of 8(6)); G6 (F6.18: the ten years of 17(1)(a); F6.14: the fifteen years of 20(5)); G8 (F8.7, F8.9, F8.10, F8.12: a period fixed by a notice, retention of a document, 28 days from the notice of a decision); G7 (F7.2: "7 days after it is made"); G9 (F9.1, F9.5, F9.7: two weeks before an appointment or after a termination; notice periods); G4 (F4.9: the period for the Commissioner's decision starts the day after the date of the application); G2 (F2.6); G5 (F5.10) | each fork is a field of its group's `Interpretation` record; the other reading is a callable function and a test in the group's own test files |
| (2) from a named day | the named day is counted | G9 (F9.2: a term of office; F9.4: an absence); G5 (F5.9: a period fixed by an order of the court); G7 (F7.11: the day named as the day of commencement is the first day in force) | as above |
| (3) backward from an event | the day of the event is outside the period | G4 (F4.1: the 12 months preceding an application); G3 (F3.7: the most recent year) | as above |

The two forward families differ by one day for the same arithmetic, by design: "retain for 10 years after deregistering" runs to the anniversary and discards the day after (15 June 2026 to 15 June 2036, discard from 16 June 2036), while "the period for which the person is appointed expires" counts the first day (a term of 6 years from 15 June 2026 ends on 15 June 2032 as a latest end date).
`int-tests-counting.l4` (21 assertions) runs one anchor day through every group that counts: 15 June 2026, 29 February 2024 and 30 November 2026.
There is no fleet-wide switch between the families: each fork is separate, so a reader who prefers the other reading of one fork sets that fork's field in `Readings of the fleet`.
Two periods in the Law that look alike and are counted differently are therefore the Law's wording, not an inconsistency of the encoding; whether the Law's wording was meant to differ is an open question (section 8).
The Interpretation (Jersey) Law 1954, which might settle some of these, is not among the sources.

### 6.2 "Year" (IP33)

Group G3 (Article 8(3)(j): "the most recent year"; forks F3.2, F3.7) and group G5 (Article 13(7), 13(9)(a): "the year to which the return relates"; fork F5.2) each carry a field for the meaning of the year.
`Int the readings of the fleet` sets both from one value, and `Int the readings of the fleet are consistent` is FALSE for a record in which they differ (tested).
The fleet default is the calendar year; the other readings, the charity's own financial year and the twelve months from each anniversary of registration, are callable.
With a 30 June year end asked on 1 February 2027, the financial reading counts a return for the year to 30 June 2026 as sent, and the calendar reading does not (the most recent calendar year is 2026 and no return for it has been sent).
Schedule 1 paragraph 4(8) and Schedule 2 paragraph 3(3) say "calendar year" in terms; they are not governed by IP33.

### 6.3 The unit of a term of imprisonment (IP35)

Groups G6 (Articles 19(11), 20(6)), G7 (Articles 21(9), 23(7), 37(1)), G8 (Articles 26(7), 26(10), 29(1)) and G9 (the cap of Schedule 2 paragraph 4(3)(f)) each have a field for the unit, and `Int the readings of the fleet` sets all four from one value.
The fleet default is calendar months.
On that reading a term of 2 years from 2 October 2026 ends on 2 October 2028, 731 days later (2028 has a 29 February), and all four groups accept it.
On the days reading G6, G7 and G8 take "2 years" as 730 days and refuse 731, and G9's cap, which reads the 24 months stored in `Penalty provided`, converts them to days from the day the term would run (731 from 2 October 2026, 730 from 2 October 2025) and compares with 730.
So on the days reading the very penalty that three groups call the maximum is over the cap of the same "2 years".
That seam is recorded, not repaired: `int-tests-red.l4` holds four assertions (seam 1) that state what the Law says and fail on the days reading, with four positive controls on the calendar-months reading that pass.
The cause lies in the shared record: `Penalty provided` in `domain.l4` stores a term in months only, so a model that counts in days has to carry the days outside it (G7 does, G8 keeps 90 and 730 as constants).
The amount of "level 3 on the standard scale" is not in the sources; G6, G7 and G8 use the same constructors of `domain.l4` for a fine of a level and for a fine with no maximum stated, so they agree on what is not known.

### 6.4 "A registered charity"

Article 1 defines it as an entity entered for the time being in the general or the restricted section.
The groups decide it in different ways.

| group | how it decides "a registered charity" |
| --- | --- |
| G1 (Article 1) | the standing is the general or the restricted section and the body is an entity within Article 2(1), so the answer depends on the text of the Law (before sub-paragraph (ba) a Jersey NPO body corporate is no entity) |
| G3 (Articles 8 to 10) | the dated entries of the entity in the register decide the section; the historic section is for formerly registered charities, to which Article 8(5) applies and Article 8(3) does not |
| G4 (Article 12(7)), G8 (Article 26(2)) | the standing on the register alone, whatever the text says about the kind of entity |
| G5, G6 | a BOOLEAN input `the entity is a registered charity`; G5 ends the Article 13 regime the day before a deregistration takes effect (F5.6); G6 lends Article 14 to the deregistered entity as if it were still registered (17(9)) |

The fleet default: headline functions pass every group the value of G1's `Art 1 the entity is a registered charity` (`Int IP6 ...`); the standing the register records is an input, and headline (b) compares it with the dated entries (`the recorded standing agrees with the entries`).
The historic section is excluded everywhere the integrator tested it: the entity of scenario B5 is on the register and is not a registered charity (trap T7), a formerly registered company that calls itself a charity commits the strict offence of Article 21(1) (chain 1, step 6), and the Commissioner's designation under Article 10(4) has no effect on a historic-section matter (trap T16, fork F3.3).
Where the groups differ is a body that the register records in the general section and that the text in force does not make an entity: an NPO body corporate asked about in the text of 12 April 2023 has no kind of entity, so G1 says it is not a registered charity, and G8's Article 26(2) says it is.
That is `int-tests-red.l4`, seam 3 (one assertion), with a positive control on the text of 16 October 2025 where the groups agree.
A caller who calls a G4 or G8 function directly, and not through a headline, gets the standing-only answer.
Since the repairs of 2026-10-27, groups G2 and G7 also read an empty `kinds of entity` as "not an entity": G2 answers FALSE to the charity test (Article 5(1): "An entity meets the charity test if ..."), and G7 applies the prohibitions of Articles 21 and 23 only to a body within Article 2(1).
Groups G3, G4, G5 and G6 read the kinds for what they need (the note of status, the Jersey-entity test, which governors are bound), and G8 and G9 do not read them; no guard of the G2 or G7 kind was added to any of those, and the integrator did not examine whether one is needed.

### 6.5 "Minister"

Group G1 gives the office that the definition of "Minister" names in each text (IP3); group G2 reads "a Minister" in Article 5(2)(a) generically (the reading taken, any Minister of the Government of Jersey) or as the defined term (reading B of F2.3); every other group types the Minister's acts by the role `the Minister` and does not resolve the office.
By the sources the office is the Chief Minister in the text of 1 January 2019 (inferred: R&O.40/2019 shows the words it replaced), the Minister for External Relations from 31 May 2019, the Minister for External Relations and Financial Services from 2 March 2021, the Chief Minister from 12 April 2023, the Minister for External Relations from 27 February 2024 (9.30 a.m.), and the Chief Minister again from 2 October 2026.
`int-tests-vintage-matrix.l4` (81 assertions) checks, for every text, the answers of G1, G7 and G9 against the sources: the office, the Law that defines "Comptroller", sub-paragraph (ba), and the Dormant Bank Accounts words of Schedule 1; the three groups agree for all nine texts and all refuse before the first.
With reading B of F2.3, a constitution that expressly permits the Minister for External Relations to control the entity defeats the charity test in the texts where that office is the defined Minister (16 October 2025) and not in the text of 12 April 2023 (tested).

### 6.6 Inclusive and exclusive limits

Each group registered a fork or a reading where a limit's wording is open, and the integrator tested the boundary of the two limits that two groups state in terms: Article 20(5) (an order "not exceeding 15 years" may end on the anniversary and not a day later; G6) and Schedule 2 paragraph 1(1) ("at least 4 and not more than 8" members; 4 and 8 are inside, 3 and 9 outside; G9).
The periods "at least 3 months", "at least 2 weeks before" and "within 28 days" are counted by the conventions of section 6.1.
No other limit was tested at its boundary by the integrator.

### 6.7 "The Commissioner is satisfied", "in the opinion of", "believes"

Every group takes a judgement of this kind as an input and none computes one (each group's section 8 says so: groups G2, G3, G4, G5, G6, G8 and G9 in terms).
The shape of the input differs: a single BOOLEAN in most groups, a record of per-ground opinions for a name (G4: `Opinion of the Commissioner on a name`), a record of who determined and what was found for public benefit (G2: `Determination of public benefit`).
The integrator reads the groups' own statements and did not test this item; it is listed so that a domain expert can say whether any judgement should be a computed rule.
Fork F8.14 (G8) asks one related question: whether the Commissioner's belief alone is a ground for a required steps notice under Article 27(1)(e) (the reading taken) or the belief must be borne out; both readings are callable and tested (IP15, IP16 in `int-tests-wiring.l4`).

### 6.8 The two retention duties (Article 8(6) and Article 17(1)(a))

The Law has two ten-year retention duties over overlapping material, neither with a stated start (trap T14).
On the readings taken, group G3 (F3.1, reading A) runs the ten years of 8(6) from the receipt of the copy, and group G6 (F6.5) runs those of 17(1)(a) from the date of the deregistration notice; the day of the event is not counted in either, and both give the last day on the anniversary (15 June 2026 gives 15 June 2036, tested).
So for a copy of a required steps notice served in 2015 on a charity deregistered in 2030 the copy may be discarded from 2025 under 8(6) and the information is kept to 2040 under 17(1)(a).
The groups' alternatives are callable (F3.1 readings B and C; F6.5 readings B and C).

### 6.9 Where a group's boolean and its regulative rule differ

Group G5's `Art 14(1) the powers of the court are exercisable on the application` (a BOOLEAN with its own `@export`) takes no input for whether anyone is acting as the Commissioner (IP28), while G5's regulative rule `Art 14(1) the court may exercise the powers on the application` does.
Headline (c) conjoins the two (`someone is acting as the Commissioner AND ...`), so the answer of headline (c) is the regulative rule's; a caller who uses the BOOLEAN alone gets an answer that ignores a vacancy in the office.
Listed as a defect (section 13).

### 6.10 The Order under Article 13(9) (IP29)

PLAN named one fact, "an Order under Article 13(9) applies to the registered charity".
Article 11(2)(e)(ii) (G4) reads limb (b) of Article 13(9) (a statement of intentions) and Article 8(3)(m) (G3) reads limb (c) (entry on the register).
Group G5 produces a composite that is TRUE if the Order requires or provides anything under (a), (b) or (c).
For an Order that requires only payment details (limb (a)) the composite is TRUE and the limb-(b) fact is FALSE, so wired from the composite an application without a draft statement of intentions would be reported as incomplete.
The integrator wires G4 from limb (b) and G3 from limb (c) (`Int IP29 an Order under Article 13(9)(b) applies`, `(c) applies`) and keeps the composite as the alternative; `int-tests-application.l4` (A13, A14), `int-tests-wiring.l4` and `int-tests-red.l4` (seam 2) test the three.
Mutation M03b (wiring G4 from the composite) is killed by A13.

### 6.11 The Commissioner's decisions (IP27)

Groups G3 (Article 9(6)), G4 (Articles 11, 12), G5 (Article 13), G6 (Articles 15, 16) and G8 (Articles 26, 27) each produce a decision as a subject and an outcome; G8 (Article 33) reads which are appealable and by whom, and G9 (Schedule 1 paragraph 4(3)) reads which a member of staff may not take.
`int-tests-decisions.l4` (24 assertions) runs every producer's output through both consumers.
A producer that picked the other outcome constructor would silently turn an appealable decision into "no appeal is given by Part 8" (G8's FRAGMENT, nouns request 9); all the producers tested agree with the consumers on the readings taken.
The decisions that the Law leaves outside Article 33's closed list (a refusal to deregister on application; the prior permission of 13(5)(b); a charity's refused request for the restricted section) get "no appeal is given by Part 8" for a registered charity and a right of appeal for the Attorney General under 33(4).

### 6.12 The date a notice is served (IP34, Article 38)

Article 38 is only a power to make an Order about service (fork F7.7 of G7), yet Articles 8(3)(k), 26, 27, 33 and 36(2) turn on the date a notice was "served", and Articles 17(4) and 36(2)(b) speak of the "giving" of a notice.
The fleet default is the date of receipt, wired once (`Int IP34 ...`) into the required steps notices (IP19), the deregistration notice and the notice of a decision (for the appeal period); the other reading, the date of sending, is G7's `the interpretation with the other reading of F7.7` (tested in `int-tests-chains.l4`: a notice sent on 8 May and received on 10 May 2020 is served on 10 May, or on 8 May on the other reading, and a 30-day period ends on 9 June or 7 June).
If the notice has not been received, the default reading refuses with a named reason (the notice "has not been received, so on the reading taken it has not been served"); mutations M01b and M12b rely on that.
Whether Articles 17(4) and 36(2)(b) read "giving" as "service" is not answered by the Law (open question, section 8).

### 6.13 Staff exercising the Commissioner's function (F2.13 and Schedule 1 paragraph 4(3))

Two groups speak of members of the Commissioner's staff, and they answer different questions.
Group G9 (Schedule 1 paragraph 4(3)) says which decisions the Commissioner's staff may not take (Articles 11, 15(3) and 16); G8 and G9 read the decision through IP27.
Group G2 (fork F2.13, added on 2026-10-27) says whether a member of staff who exercises a function of the Commissioner under that authority is bound by Articles 7(2), 7(3) and 5(5) as the Commissioner is.
The two do not conflict, and the integrator does not wire one from the other: `who` is the caller's fact (the constructor `a member of the Commissioner's staff` for an authorized act, `any person` otherwise), and G2 itself says that the choice of constructor is the caller's.
The fleet default is reading A of F2.13 (staff are bound), which the fleet lead ruled by assumption on 2026-10-27 ("assumed, not ruled", revertable).
`int-tests-repairs.l4` (R3) runs both readings through headline (a): a staff finding of public benefit for a company that benefits only identified persons fails the charity test on reading A and stands on reading B, while the same finding made by the Commissioner fails on both.
G2's note asks that any other group which attaches a duty to the Commissioner be set from the same view of paragraph 4(3), for example the Commissioner's belief of Article 27(1)(b); G8 takes that belief as an input and has no fork on it, so nothing else was set.

## 7. Consolidated register of contradictions, tensions and slips in the source

Each item once, with the provisions, the case that discriminates, the groups that found it (by their own item numbers: `C` numbers in G1, G2, G4 and G7; plain numbers in G3, G5, G8 and G9; the bullets of G6 in order) and where the encoding handles it.
These were found by the groups in separate passes after their modules were green; the integrator did not repeat the passes.
The cross-check against the list of contradictions that another agent of the fleet kept (`work/hunt/CONTRADICTIONS.md` in the fleet's working directory) is left to the launching session: the brief (rule 8) forbids the integrator to read other agents' findings, and the integrator did not read it.
Whether a pair is a real contradiction in the Law, a drafting slip or a deliberate asymmetry is for a domain expert (section 8).
"Fork" means a field of `Readings of the fleet` with a callable other reading and a test.

### 7.1 Conflicts that change an answer

| id | provisions | the conflict | the case that discriminates | found by | handled by |
| --- | --- | --- | --- | --- | --- |
| S1 | 11(4), 11(5), 19(9)(c), 20(1)(c) | The duty to register meets two bars the six matters do not mention, and 11(5) ("if not so satisfied") does not repeat the condition that 11(4) puts on the duty to register | all six matters satisfied and a fitness issue undetermined: MUST register and MUST NOT grant; a missing copy of the constitution together with an undesirable name | G4 C1, C2; G6 bullet 1 | forks F4.4 and F4.3; IP23 and IP24 are inputs wired from G6; headline (a) scenarios A2, A3, A4 |
| S2 | 11(4)(a), 5(1)(b) | "or will do so on registration" has no counterpart in the limbs of 5 | an applicant whose constitution will be amended on registration | G2 C5 | G4 takes it as a finding beside IP8; not wired from G2 |
| S3 | 2(1)(ba), 8(3)(a)(i), 8(3)(a)(ii), 2(3)(a) | R&O.56/2025 inserted (ba) and amended nothing else, so 8(3)(a) ("(f) to (j)"; "(e), (g), (h) or (j)") does not mention it; an Order under 2(2) cannot reach 2(3) | a body corporate NPO that is also the sole trustee of a trust; a sub-paragraph added at the end of 2(1) | G1 C7, C9; G3 2 | forks F1.1, F3.13; chain 3 tests that (ba) draws no "also within (a)" note and no enactment details |
| S4 | 2(5), 2(1)(e), 8(4)(a) | 2(5) names a constitutional Law for five of the twelve kinds, and says "by (but not under)" for (e); 8(4)(a) asks whether the constitutional Law requires a registered office | a body incorporated under, but not by, an enactment that requires an office | G1 C3; G3 3 | forks F1.3, F3.9; the requirement is an input |
| S5 | 2(1)(g), (c), (d), 8(3)(a)(i) | (g) excludes only the Companies (Jersey) Law 1991, so a foundation and an 1862 association are within (g) as well; 8(3)(a)(i) says "the sub-paragraph" | a foundation | G1 C4 | fork F1.8 |
| S6 | 22(1), 2(10)(b) | 22(1) defines an excepted foreign charity "for the purpose of Article 21"; 2(10)(b) imports it "within the meaning of Article 22" | a conviction in relation to an excepted foreign charity | G1 C8; G7 C1 | fork F7.12; headline (c) scenario C7 |
| S7 | 2(10)(b), 4(c), 19(1)(g), 22, Part 6 | Provisions in force from 1 May 2018 cite Article 22, which comes into force on 1 January 2019 (trap T30) | a conviction on 1 July 2018 in relation to an excepted foreign charity | G6 bullet 11; G7 C7 | headline (c) refuses for a day before 1 January 2019 (Article 22 is in its list of units); the other headlines refuse for want of a text |
| S8 | 1, 10(4), 8(6), 26(4)(a), 33(5), 14(1)(a), 17(9) | "Registered charity" ("for the time being", general or restricted section) is used where the historic section, a formerly registered entity, or a past time is meant; "historic section" is not defined in Article 1 | a historic-section matter that would endanger a person; a document demanded of a formerly registered entity and an employee asked for an explanation; "is or has been misconduct" against "would have been misconduct if not deregistered" | G1 C11, C14; G3 4, 9; G8 1 | forks F3.3, F8.19, F1.7; section 6.4 |
| S9 | 33(5) | The exclusion of "a registered charity" removes the charity most likely to have an interest in the applicant's name; the two grounds "at both the time of the application and the time of the appeal (a) or (b)" group two ways; "the registered name of the applicant" at the time of the application is a name that does not yet exist | a registered charity with a similar name; a test failed at one time and a name undesirable at the other | G8 2, 3, 13 | forks F8.13, F8.18; the name is read as the proposed name; headline (f) scenario F4 |
| S10 | 8(6), 17(1)(a), 8(3)(k), 8(6)(c) | Two ten-year retention duties over overlapping material with no start; 8(3)(k) enters a notice served on the charity or a governor, 8(6)(c) retains only a notice served on the charity | a notice served in 2015 on a charity deregistered in 2030 | G3 5, 6; G6 bullet 6 | forks F3.1, F6.5; section 6.8 |
| S11 | 16(1), 16(2), 17(2)(c), 17(4), 17(3), 17(1)(a), 17(5), 17(6), 13(1) | Both 16(1) and 16(2) reach a charity that has ceased to exist and fails the test; "the notice under Article 16(1) or (2)" does not pick out one of the two notices of 16(1); a retrospective deregistration "for all purposes" against the later "after deregistering", "before it was deregistered", "immediately before deregistration" and 13(1) | a preliminary notice on 1 March, a deregistration notice on 1 April, a past date of 1 January 2025 and an act on 15 March; a past date more than ten years before the notice; an amendment of the purposes made between the past date and the notice | G6 bullets 3, 4, 5; G5 6 | forks F6.2 to F6.5, F5.6 |
| S12 | 15(3), 16, 33(1)(b), 33(2)(a), 9(2), 9(7), 11, Sch 1 4(3)(a), (b) | A refusal to deregister on application is not among the decisions 33(2)(a) makes appealable (and is named by one outcome in Sch 1 4(3)(b)); 33(1)(b) treats a refusal of the restricted section as a refusal to register, while Schedule 1 4(3)(a) reserves "the decision under Article 11"; a charity in the general section may request the restricted section (9(2)) but 33 does not list its refused request; a deregistration the charity applied for is a decision "to deregister" | a charity applies to deregister and is refused; staff decide a request for the restricted section; staff deregister an entity on its own application | G6 bullet 13; G8 5, 6; G9 3, 4 | forks F8.4, F8.16, F9.8, F9.16; IP27 and `int-tests-decisions.l4` |
| S13 | 34(1), 35(1) | Two statements of "the ground" of two appeals; the second is narrower | a decision wrong in law but not unreasonable | G8 4 | fork F8.5 |
| S14 | 28(3), 19(9)(e)(i), 27(4), 27(2), 28(1), 28(2)(a), 6(2)(f), 28(1)(a) | 28(3) voids a requirement to suspend or remove a governor for an organized religious charity, which 19(9)(e)(i) makes a duty; 27(4) names only (1)(c) and (d) notices while 27(2) and 28(3) are wider; "categorized" (28(1)) against "status" (28(2)(a)); 6(2)(f) puts a philosophical-belief purpose within (p), so on one reading no humanist body can be categorized under 28(1)(a) | the governor of an organized religious charity with a disqualifying reportable matter; a humanist association | G6 bullet 2; G8 7, 8, 15; G2 C4 | forks F6.15, F8.15, F8.3, F2.5 (tested together in `int-tests-wiring.l4`) |
| S35 | 7(1), 5(5), Sch 1 4(3) | Article 7(1) and the second limb of 5(5) name the Commissioner, the tribunal and the court (and, for 5(5), a registered charity and a governor) and not the Commissioner's staff, while Schedule 1 4(3) lets staff exercise any function of the Commissioner: read literally, a staff determination escapes 7(3)(b) | a member of staff, authorized under paragraph 4(3), finds that an entity that benefits only one named natural person provides public benefit | G2 C10 (found by the independent test authors; ind-c D2 and ind-b A-14) | fork F2.13 (added 2026-10-27); section 6.13 |
| S15 | 13(10), 13(8), 13(11)(a), 13(9)(b), 11(2)(e)(ii), 8(3)(m), 13(9)(c) | 13(10) names an Order under (8), which creates none; "a statement"/"that statement"/"current intentions"; 11(2)(e)(ii) says 13(9)(b), 8(3)(m) says 13(9)(c); an applicant is not yet "the registered charity" those provisions speak of | an Order made under (a) alone; a statement provided on the day of a payment | G5 1, 5, 9; G4 C5, C7 | forks F5.3, F5.14; IP29 split (section 6.10) |
| S16 | 13(2), 5(1)(a)(ii), 6(5), 14(2), 14(1), 13(5)(b), 13(4)(b), 33(2)(e), 14(3)(a)(i), 25 | 13(2) strikes a provision for a purpose "that is not charitable" while 5(1)(a)(ii) accepts a purely ancillary purpose; 14(2) joins three aims by "and" although 14(1)(b) needs no misconduct; 13(5)(b) presupposes a permission no provision confers; 13(4)(b) and 33(2)(e) describe an approval regime the Law does not state; a court may forbid a charity to hold itself out as a charity while an Order under 25 may require registered charities to say they are one | a purely ancillary purpose added by amendment; an order under 14(1)(b) with no misconduct | G5 2, 3, 4, 11, 12 | forks F5.7, F5.12; 13(5)(b) encoded as the Commissioner's MAY, marked "presupposed, conferred by no provision" |
| S17 | 18(4)(c), 1 ("misconduct"), 19(8), 19(10), 19(11), 19(4), 19(5), 20 (heading), 20(3) to (6), 17(9), 14(1) | 18(4)(c) makes a governor's misconduct depend on another governor's and Article 1 sends "misconduct" of a governor to 18(4); 19(8) forbids acting while in breach but only 19(10) has an offence (19(11)); the duty to declare (19(4)) is triggered by a notification nobody must give, and the charity must state in the return (19(5)) that it holds the declarations; the heading of Article 20 says "governor", paragraphs (3) to (6) say "a person"; 17(9) lends Article 14 powers to the court but changes the applicant (not the Commissioner) | governors who only assist each other; an unreported bankruptcy and the governor acts; a charity files its return without notifying its governors; the Commissioner wishes to protect the property of a deregistered entity | G6 bullets 7, 8, 9, 10, 12 | forks F6.24, F6.11, F6.21; 17(9) encoded as the text says (a test asserts that the Commissioner is not an applicant) |
| S18 | 2(10)(b), 18(4)(a) | "in relation a registered charity" (missing "to"); 2(10)(b)(vi) says "clauses (i) to (v)", and the Law has no other name for that level (it says "sub-paragraphs" for the lettered level), so that is an observation and not shown to be a slip; 18(4)(a) says "an offence, mentioned in Article 2(10)" which can be read without the connection to a charity | an offence under 2(10)(b)(ii) to (vi) not in relation to a charity | G1 C1, C2, C16 | fork F1.2 |
| S19 | 9(2), 9(2)(a), 9(2)(b), 11(1) | The lead-in lets "an applicant for registration, or a charity registered in the general section" request the restricted section; (a) and (b) say "the applicant"; 11(1) defines "the applicant" | a charity already in the general section that meets the funding condition | G3 1 | fork F3.12 |
| S20 | 21(1) to (6), 23(1), 23(2), 21(2)(b)(ii), 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii), 24(3)(a), 24(4), 37(1) | A statement can make out both a strict and a knowing offence; "or other advantage" is in one limb and not in three alike; 24(3)(a) lets Regulations adapt offences that carry imprisonment while 24(4) caps the penalty at "no greater than a fine"; 37(1) names three kinds of body while 2(1) makes other kinds offenders | a statement made knowing it is untrue to a donor; Regulations adapting 21(9) wholesale; a committee member of an unincorporated association; a director of an LLP | G7 C2, C4, C5, C9 | forks F7.4, F7.5, F7.13, F7.6, F7.10; trap T26 tested in scenario D3 |
| S21 | 26(1), 26(10), 26(9), 30, 31 | The power to demand serves one purpose, the offence of false information two; an application's information is asked under 11(2)(f)(ii), which has no offence; 26(9) excepts "proceedings under paragraph (7)"; 30 obliges disclosure only for some functions while 31 permits it for any | false information in an application with no 26(1) demand behind it | G8 9, 11, 16 | encoded as written; no fork |
| S22 | 2(2), 39(1), 39(2) | An Order under 2(2) may add sub-paragraphs, but 39(1) bars "an amendment of this Law" from an Order's ancillary provisions and 39(2) extends the power "by Regulations" only | an Order under 2(2) that also amends 8(3)(a)(ii) | G7 C3 | fork F7.14 |
| S23 | 11(8)(a)(ii), 36(2)(b), 11(3)(a), 11(2)(e)(iv) | Two Order-making powers over notification of decisions; Regulations and an Order may add to the same list; 11(2)(e)(iv) says "prescribed by the Minister by Order" and no Article confers the power (the style of the whole Law) | an Order and Regulations that differ | G8 12; G4 D2 | inputs; nothing to decide without the instruments |
| S24 | 12(1), 12(7)(b)(ii), 33(5)(b), 19(6), 11(2), 13(7), 13(9)(a), 8(3)(j), Sch 1 4(8), Sch 2 3(3) | "Undesirable" is defined "for the purpose of Article 11(4)(e)" and used for a name in a context; "complete" (19(6)) is not "includes what 11(2) requires"; "the year to which the return relates" against "the most recent year" against "calendar year" | a name used for a trading activity; an application complete under 19(6) and short of 11(2) | G4 C3, C4; G5 10 | the opinion on a name in its context is an input; the two notions of completeness are kept apart; forks F5.2, F3.2 and IP33 |

### 7.2 Commencement, the Table of Legislation History and service of notices

| id | provisions | the conflict | the case that discriminates | found by | handled by |
| --- | --- | --- | --- | --- | --- |
| S25 | the Table of Legislation History, Articles 32, 38 to 44, Parts 8 and 9, R&O.17/2018 | The Table names "Articles 32, 38, 39, 40, 42, 43 and 44" and the Law now ends at Article 43; Parts 8 and 9 are each brought into force in two stages, so "Part 8 is in force" has no single day; the survey's account of the 2019 remainder differs from R&O.17/2018 Article 2 | present Article 41 on 1 January 2018; Part 8 on 1 June 2015 | G7 C6, C8, C14 | forks F7.3, F7.9; the gate takes G7's favoured readings; one assertion in `g7-tests-red.l4` states the survey's claim and fails |
| S26 | 17(4), 36(2)(b), 1, 8(3)(k), 26, 27, 38 | "giving of the notice" against "served" against "service"; Article 38 only empowers an Order | an act done on the day between sending and receipt | G7 C13 | fork F7.7; IP34; section 6.12 |
| S27 | L.1/2017, R&O.136/2019, R&O.40/2019, R&O.29/2021 | The date 16 December 2019 for L.1/2017 rests on the Table alone (the Act that appointed it is not among the sources); the survey's inferences about "Minister" in 2021 and about Schedule 3 of L.13/2019 are now shown by the instruments | the Dormant Bank Accounts words from 16 December 2019 | G7 C15, C16 | `g7-vintages.l4` records for each row whether the date is shown by the sources |

### 7.3 Drafting slips and terminology with no effect on an answer

| id | where | the slip | found by |
| --- | --- | --- | --- |
| S28 | 4(4) | "so far appears" for "so far as appears" (in the consolidated text and in the official PDF alike) | G2 C1 |
| S29 | 7(4); 14(3)(b); 14(1) and (2); 42(a); 27(2); 31(d); Schedule 2 1(8); Schedule 1 4(12) | a comma before a verb; "(whether a specified or indefinite period)"; "the powers set out in paragraph (2)" where (2) is one general power; "by reference the test itself"; "in Commissioner's opinion"; "the Attorney General, the Bailiff or the court" (a redundancy); "as Minister sees fit"; "Directions under paragraph (11)" for sub-paragraph | G2 C6; G5 7, 8; G7 C11; G8 18, 17; G9 10, 2 |
| S30 | 5(6), 5(4), 5(5), 11(6)(b) | "guidance" where the neighbours say "the guidance"; 11(6)(b) extends 5(6) to (8) to other guidance, which would be superfluous | G2 C3 (fork F2.12) |
| S31 | 5(1)(b), 7(1), 4(2), 4(1)(d) | 5(1)(b) and 7(1) put the question differently; 4(2) speaks of "a charity" and "an entity with charitable purposes" where the Law defines only "registered charity"; 4(1)(d), 5(4), 7(4) are three provisions about the same guidance and agree | G2 C2, C8, C7 |
| S32 | 1 | "council member" is defined and never used; "tribunal" is "the Charity Tribunal established by Article 32" and Schedule 2 is headed "Charity Commission tribunal" | G1 C10, C12; G9 1 |
| S33 | Schedule 1, Schedule 2 | "position" and "vacates that position" against "office"; independence (Sch 1 2(2)) against the Minister's powers of appointment, termination and direction; "not more than 6 years" (1(5)) that cannot be completed because the 12-year mark (3(4)(c)) comes first (trap T21, tested) | G9 6, 8, 9 |
| S34 | endnote [4], Article 31; L.13/2019 Schedule 3; R&O.40/2019 Schedule 2 1(e) | the Table of Endnote References says the editorial change is in 31(c) but the marker stands at the end of 31(f), and (a) and (b) still read "for purpose of"; L.13/2019 Schedule 3 is headed "(Article 29(2))" and the Article that says "Schedule 3 has effect" is 28(2); R&O.40/2019 cites "Article 1(1)" and Article 1 has no paragraph (1) | G8 10; G1 C15; G7 C12 |

### 7.4 Statements of the survey or of an assignment that the encoders corrected

These are not contradictions in the Law.
The survey said that the Law creates no offence the Commissioner could commit; Article 29(1) makes it an offence for "a person who receives information under or for the purposes of this Law" to disclose it without consent, and on its words the Commissioner is such a person (G9 item 7; the inert disposition stands).
An assignment cited "4(7)" for the copy to the Minister, where the Law's provision is 5(7) (G2 C9).
The survey's disposition for Articles 41 and 42 (out of scope) was changed by ruling to encoded as powers of the States to make Regulations (G7), and the survey's reading of the 2019 remainder was corrected by R&O.17/2018 (G7 C14).

## 8. Consolidated open questions for a domain expert

These are the groups' questions, merged by topic and stated once, with the group question numbers in brackets (for example G6 q12 is the twelfth question of group G6) and the fork where there is one.
Where a question has a fork, the reading taken is in section 5 and the other reading is callable.
The full text of each question is in the group's FRAGMENT, in its section "Open questions for a domain expert".

### 8.1 Who and what is covered (Articles 1 and 2)

- Is sub-paragraph (g) meant to overlap (c) and (d) (G1 q1, F1.8)?
  Does "in relation to Jersey" in 2(1)(e) qualify only the Royal Charter, and does "enactment" there include a United Kingdom Act that does not extend to Jersey (G1 q2, F1.6)?
- Is the constitutional Law of a body incorporated "under, but not by," an enactment that enactment, and what is the constitutional Law of a (ba) body and of an unincorporated body (G1 q3, F1.3)?
  Which Law requires a registered office or business address in Jersey, and of whom; does every Jersey company and foundation have one (G3 q4)?
- For a company that is the sole trustee of a charitable trust, are its directors governors of the charity, and do both the trust deed and the memorandum and articles make up its constitution (G1 q4, F1.4)?
- Must an offence under 2(10)(b)(ii) to (vi) be in relation to a charity, and does 18(4)(a) read "an offence mentioned in Article 2(10)" with or without that connection (G1 q5, F1.2)?
  Is a contravention by a charity that has since been deregistered "misconduct" (G1 q6, F1.7)?
- Was the Order of 2025 meant to put (ba) inside "(a) to (h)", and should 8(3)(a)(i) and (ii) be read as covering it (G1 q7, F1.1)?
  Is it intended that an Order adding a sub-paragraph at the end of 2(1) cannot create a Jersey entity (G1 q9)?
- Is "published" the publisher's honest opinion or an objective test (G1 q8, F1.5)?
  Has the Commissioner published a model constitution under 2(8)(b)(i), and where (G1 q10)?

### 8.2 The charity test (Articles 3 to 7)

- Is a philosophical-belief purpose within 6(1)(p) only, or also within (c) for Article 28 (G2 q1, F2.5; and G8's fork F8.3)?
- Does 5(6) to (8) bind the Commissioner's other guidance (G2 q2, F2.12)?
- Does a determination of public benefit made in breach of 7(2) or 7(3) stand, fall or neither, and is a breach of 5(5) different (G2 q3, F2.10)?
- Is "a Minister" in 5(2)(a) any Minister (G2 q4, F2.3)?
- Must the constitution say "permits", or does a provision that requires a Minister to be a governor count as expressly permitting it (G2 q5)?
- Does a purely ancillary purpose count alone, and does an entity with no purposes pass (G2 q6, F2.1)?
- Is "the promotion of equality and diversity" one head that either idea satisfies, or two ideas to be joined (G2 q7, F2.11)?
- Is "so far as practicable" in 4(4) a limb-by-limb qualification (G2 q8, F2.9)?
  Does 4(3) widen the Commissioner's powers (G2 q9, F2.8)?
- In days, what is a "reasonable time" in 5(7) and "as soon as practicable" in 5(8), and how are the days counted (G2 q10, F2.4, F2.6)?
- In 7(2)(a), are the benefit to members and the disbenefit to the public two comparisons or one (G2 q11)?
- What does "or will do so on registration" in 11(4)(a) add to 5(1)(b)'s applicant limb (G2 q12)?
- Does a function exercised by a member of the Commissioner's staff under Schedule 1 paragraph 4(3) carry the duties that Articles 7(1) and 5(5) attach to the Commissioner (G2 q13, F2.13)?
- Does Article 6(2)(e) add an operand to head (n) of Article 6(1), so that the provision of accommodation or care is within the head with nobody shown to be in need, or does it only say that relief of those in need can be given by accommodation or care (F2.14)?
  Label: default ruled by the owner (Meng), 2026-10-27; the widening reading stays callable.
  History: the declaratory default was first recommended by the general manager when the owner delegated the call ("what's this about Article 6.2.e? i probably don't mind one way or the other so i am happy to take your recommendation."); the owner then ruled in his own words, below.
  The owner's words, as FRAGMENT-G2.md records them: "I agree with your declaratory reading [...] it is of limited import because a commercial care home would still need to meet the public benefit test" ([...] marks words elided from the quotation; they are not part of the ruling).
- Is the omission, in Article 6(2)(e), of the words "to the persons mentioned in that paragraph" deliberate (G2 q14, F2.14)?
  If it is deliberate, the clause widens head (n) and reading B is the better one; if it is not, reading A.
  This is a question and not an answer: the default stands as the owner's ruling until an expert says otherwise.
  The words are those of a corresponding section of an English statute, and FRAGMENT-G2.md (fork F2.14, "Evidence from other statutes") records where they come from and what was and was not checked; the integrator opened none of it.

### 8.3 The register, the restricted section, public access (Articles 8 to 10)

- What is "the most recent year" for the annual-return entry of 8(3)(j): the calendar year, the charity's financial year, or the year from registration; which year is current on a given day; what is entered before a charity's first year has ended (G3 q1, q2; F3.2, F3.7)?
  What is "the year to which the return relates" in 13(7), and what is the year of a charity whose financial year is not the calendar year (G5 q2, F5.2)?
- When do the ten years of 8(6) start, and does the Commissioner keep a registered charity's constitution for as long as it is registered (G3 q3, F3.1)?
  Do 8(6) and 17(1)(a) overlap, and from when does each run (G6 q6)?
- Who chooses which governor's address is entered as the principal address under 8(4)(c) (G3 q5)?
  Can a charity run from a private dwelling house register, and is "main premises" what the charity says or what the Commissioner finds (G3 q12, F3.10)?
- Does an alternative registered name (12(5)) count as a name "under which the entity was registered" for 8(5)(b) (G3 q6)?
  After a charity changes its registered name, may it still use its previous name as "one of its registered names" (G4, F4.8)?
- What does "approved by the Commissioner" in 8(3)(e) and (f) require (G3 q7)?
  What are the criteria, time and effect of approval or permission under 13(3)(b), 13(4)(b), 13(5)(b) and 13(11)(b), and which permission does 13(5)(b) refer to and who may give it (G5 q3)?
- Is a charity ever moved from the restricted section back to the general section, and by what act (G3 q8)?
- What do the Orders say: R&O.59/2018, R&O.60/2018, and any Order under 8(5)(e), 8(6)(d), 9(1)(d) and 10(2) (G3 q9)?
  What is the funding condition of the restricted section, does a prescribed description of persons replace "the general public", and what do the Order's definitions of soliciting and of a donation say (G3 q13)?
- Does a copy of a required steps notice entered under 8(3)(k) disclose the name of a restricted-section charity (G3 q10)?
  Can the Commissioner protect a matter of a deregistered entity under 10(4); if a summary of reasons in the historic section endangers a person, what is the remedy (G3 q11, F3.3)?

### 8.4 Registration and names (Articles 11 and 12)

- On 11(5): does the duty to refuse arise for an application that does not comply with 11(2), the Regulations or 19(5) when the six matters are not found (F4.3 reading C), or does the Commissioner wait for a complete application (reading A) (G4)?
- On 11(4), 19(9)(c) and 20(1)(c): which prevails, and is refusal under 11(5) available while a fitness issue is undetermined (G4, F4.4; G6 q15)?
- On 11(2)(e)(ii): which twelve months and counted from which date (F4.1, F4.2); does "any governor of the entity" mean a governor when the payment was made or on the date of the application (F4.11); are payments by a third party to a governor within "any payment made to any governor" (G4)?
- On 12(1)(a): are the alternative and previous registered names of another charity "the name" of that charity (F4.7), and is a deregistered charity "another registered charity" (F4.5) (G4)?
- Does the definition of "undesirable" in 12(1), "for the purpose of Article 11(4)(e)", apply to a name used in a context under 12(7)(b)(ii) (G4)?
  What is "related" in 12(7)(b)(i)?
  Is there any consequence of breaching 12(7) other than misconduct under 2(10)(a)(i)?
- What does an Order under 11(8)(a)(i) say happens to a decision made after the period (G4)?
  Do Regulations under 11(3)(a) and an Order under 11(2)(e)(iv) overlap, and which prevails (G4)?

### 8.5 Annual returns, changes and the court (Articles 13 and 14)

- Does 13(2) strike a provision that would let a registered charity add a purely ancillary purpose (G5 q1, F5.7)?
- Is a return sent on the day an Order fixes as its due date timely (G5 q2, F5.5)?
- Does "promptly" in 13(6) have an accepted number of days in the Commissioner's guidance (G5 q4, F5.1)?
- Is an order of the court under 14(3)(a)(i) forbidding a registered charity to call itself a charity compatible with an Order under Article 25 (G5 q5)?
- Is "misconduct in the administration" (14(1)(a)) limited to conduct that bears on the administration (G5 q6, F5.4)?
- If a deregistration is retrospective, is an amendment made in the interval affected by 13(2) (G5 q7)?
- Who is "a person to whom the order was directed" in 14(4) where an order is directed at "the charity or a governor" jointly (G5 q8)?

### 8.6 Deregistration, governors, reportable matters (Articles 15 to 20)

- On 15(3): what may the Commissioner do where the entity does not supply the information requested under 15(2) (G6 q1, F6.1)?
  Is there a time within which the Commissioner must decide an application (G6 q2)?
- On 16(1): must the Commissioner wait until the time named for objections has run out (G6 q3, F6.17); does an unreasonable time invalidate the deregistration (F6.13); must the Commissioner consider the objections?
  On 16(2): is a preliminary notice required for an entity that no longer exists, and to whom must the written notice be given if nobody purports to be a governor (G6 q4, F6.2)?
- On 17(2) to (6): from which instant is a retrospectively deregistered entity "deregistered" for property, for the ten years of retention, for the preserved purposes (G6 q5, F6.3 to F6.5)?
  Is the bar on reassigning a registered number permanent (G6 q7, F6.6)?
  Is it intended that the Commissioner may not apply to the court to protect the property of a deregistered entity (17(9)) (G6 q8)?
- On 18(2): is the standard of care meant for governors of every registered charity or only of unincorporated bodies (G6 q9, F6.7)?
  On 18(4)(c) and (d)(ii): is encouraging another governor to engage in misconduct itself misconduct, and does "within a reasonable time" qualify the concealment as well (G6 q10, F6.24, F6.8)?
- On 19: does a disqualification that has ended still count (q11, F6.9); how many days is "promptly" and from when does the clock run (q12, F6.12); who must notify the governor that the charity is preparing its annual return (q13, F6.21); is acting while in breach of 19(2) or (4) meant to be an offence (q14, F6.11); does the Commissioner's duty to require removal extend to an organized religious charity (q16, F6.15); from which report does the ban of 19(10) start (q17, F6.10)?
- Are "one year" and "2 years" in 19(11) and 20(6) twelve and twenty-four calendar months or 365 and 730 days, and what is the maximum fine (G6 q18, F6.16)?
  May the Commissioner apply under 20(3) on the Attorney General's view of expediency, and the converse (G6 q19, F6.23)?
  How are the fifteen years of 20(5) counted and from which day (G6 q20, F6.14)?

### 8.7 Commencement, offences and the text (Articles 21 to 25, 37 to 43, the endnotes)

- **Ruled 2026-10-27, no longer open:** a question about a day before 1 January 2019 that depends on the text of the Law is refused, because no text before that day is among the sources; "Minister", "Comptroller" and the kinds of entity are not reconstructed by reversing the amendments the endnotes list (the independent authors ia-AMB1 to 4, ib-V02 and ic-V-08 had expected such an answer, for example "Chief Minister"). Ruled by the repository's owner, Meng, on 2026-10-27: "agree with refusing pre-2019 questions."
- Did the Law as enacted place the original Article 41 in Part 9 (G7 assumed it from its position between the original Articles 40 and 42; if it stood elsewhere the days for Part 9 revert to those of the present Articles)?
- Is the day named in the Table the first day on which a provision is in force?
  Does "7 days after it is made" leave the day of making out?
  Which Jersey time is meant by "9.30 a.m." (taken: the zone Europe/Jersey, which is GMT on 27 February) (G7)?
- Is a Part brought into force in two stages "in force" when any, or all, of its Articles are (G7, F7.9)?
  What did the original Articles 41 and 44(3) provide?
  Did the Act appointing 16 December 2019 for L.1/2017 bring Article 30(3) into force on that day?
  Can the States still make regulations under 40(3) after 1 January 2019?
- Is the date of service of a notice the date of sending or of receipt, and has an Order been made under Article 38 (G7, F7.7)?
- Is an unincorporated association or a trust within 37(1), and are the directors of a limited liability partnership officers of a body corporate (G7, F7.6, F7.10)?
  Does "in connection with any of its activities in Jersey" (21(5), 21(6)) cover a statement made outside Jersey about activities carried on in Jersey?
  Does the awareness of 21(4)(a) and 21(6)(a) have to cover both limbs together?
  Is the omission of "or other advantage" in 21(4), 21(6) and 23(2) intended (F7.5)?
  Does an offence of both kinds by one act give two convictions, and can the penalties be cumulated (F7.4)?
- Does 22(1) define an excepted foreign charity for 2(10)(b) (F7.12)?
  Can Regulations under Article 24 attach imprisonment to an offence adapted from 21(9) (F7.13)?
  Can an Order under 2(2) make consequential amendments of other provisions of the Law (F7.14)?
  What is a "supervisory body" in 41(2) (defined in a Law that is not among the sources)?

### 8.8 Information, demands, appeals (Articles 26 to 36)

- Who must supply the copy under 26(6) (the passive sentence); is a claimed lien (26(3)) a "reasonable excuse" under 26(7) (G8 q1, q2)?
- Against whom may the tribunal award costs under 34(3)(b) (G8 q3)?
  Does an appeal suspend the decision appealed (G8 q4)?
  What happens if the Commissioner never decides an application (no deemed refusal is provided) (G8 q5)?
- What are the time limits and the provisions on notice that the Minister may prescribe under 36(2), and which reading of F8.6 would an Order displace (G8 q6)?
- May a notice under 27(2) specify a period or only a date (G8 q7)?
  When is the status of an organized religious charity lost (G8 q8)?
  What does the Law mean by an "employee" of a registered charity in 26(4)(a) (G8 q9, F8.19)?
- G8 asks for a ruling on each of its nineteen forks, in particular F8.11 (which consents), F8.13 (who is excluded from 33(5)) and F8.18 (the two grounds and the two times) (G8 q10).

### 8.9 The Schedules

- Does the Minister's duty to appoint (Sch 1 1(1)) arise only while the office is vacant, and is there a time limit (G9 q1)?
- When an instrument fixes a period of appointment, does its end date mean the day the period expires or the last day of service; is a period of exactly six years and a day forbidden (G9 q2, F9.2)?
- Does a resignation on notice take effect when the notice runs out or when it is given, and how are months added at the end of a month, clamped or rolled (G9 q3, F9.3)?
- Under Sch 1 3(2) and Sch 2 2(2): must a ground exist in fact, or is the Minister's satisfaction enough (F9.19)?
  For the absence ground, are the first and the last day of the absence both counted (F9.4) (G9 q4)?
- Is a day on which a notice is presented to the States counted in the "2 weeks before appointing" and "2 weeks after terminating", and does the Interpretation (Jersey) Law 1954 settle "clear days", "month" and "year" (G9 q5, F9.1, F9.5)?
- How is "12 years (whether consecutive or in aggregate)" reckoned for broken service, and does service as a relevant person designated under 4(4) count (G9 q6, F9.6, F9.11)?
- "Subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017": does an Order displace the States' liability or only reimburse; who pays if the Fund cannot; on what day did L.1/2017 come into force (G9 q7, F9.9)?
- May a person already a member of the States be appointed, and does the appointment then expire at once (G9 q8, F9.17)?
  Who owes the annual report for a year in which the office changes hands, and is the tribunal's report published (G9 q9, F9.12)?
  How is a relevant person designated under Sch 1 4(4), and how long may the "temporary basis" last (G9 q10)?
- Who names the responsible officer where several members of staff are available; is there a quorum for a sitting in practice; have Regulations under Sch 2 4(3) been made (G9 q11, F9.18)?
  Does the vacancy of the office of chair or vice-chair count as absence for Sch 2 4(1) (G9 q12, F9.15)?
- Is the decision on entry in the restricted section one that staff may make (F9.16), and is the decision to deregister on the entity's own application reserved from staff (F9.8) (G9 q13)?

### 8.10 Questions that arise between groups

- Is a different meaning intended by the Law's two conventions for counting a period of days (section 6.1), where the same arithmetic gives dates one day apart?
- Which prevails when a group's regulative rule and its BOOLEAN differ because the BOOLEAN ignores that someone must be acting as the Commissioner (section 6.9)?
- Is "a registered charity" in Articles 12(7) and 26(2) meant to need an entity within Article 2(1), as in Article 1 (section 6.4)?
- Which of Article 8(6) and Article 17(1)(a) governs a copy of a notice that both cover (section 6.8)?

## 9. Consolidated: what the sources do not answer

Each is a place where the encoding takes an input, gives a named refusal, or states its assumption, and never supplies a plausible value.

- **The text of the Law before 1 January 2019, and after 2 October 2026.** The nine consolidated texts begin on 1 January 2019; the enacted text of 2014 is not among the sources, and the consolidation runs "to Current".
  Every function that depends on the text refuses for an earlier day, and the text of 2 October 2026 is read for every later day; an amendment after that date is not known (G1 item 1, G2, G3 12, G5 11, G6 1, G7, G8 6, G9 3 and 12).
  The sources show no difference between the texts in any Article other than Article 1, Article 2(1) and Schedule 1 (G1 item 2, G3 12, G8 6); that conclusion rests on the Table of Endnote References and the amending instruments, not on the texts.
  The definition of "Minister" from 1 January 2019 to 30 May 2019 is inferred (R&O.40/2019 shows the words it replaced), the date 16 December 2019 for L.1/2017 rests on the Table alone, and endnote [4] (an editorial change to Article 31) is undated (G7, G8 7).
  Whether the consolidated text is exactly the enacted text outside the amended provisions is not known: the licence note says "for information purposes only" (G7, G8 10).
- **Which Part the original Article 41 stood in.** The sources show the Table of Renumbered Provisions ("41 spent, omitted") and no text of the Law as enacted; G7 places it in Part 9 by its position between the original Articles 40 and 42 (assumed, not ruled), and Part 9 is in force from 1 January 2019 on reading A of F7.9 because of it.
- **The text of "Minister", "Comptroller" and the kinds of entity before 1 January 2019.** The endnotes list the later amendments, so the earlier words could be reconstructed by reversing them; the fleet lead's triage of 2026-10-27 left that reading (reading B) unbuilt, so the encoding refuses for those days (section 12), and the repository's owner ruled the same day that the refusal stands (section 8.7).
- **Every Order and every set of Regulations the Law empowers.** None is among the sources, so each is an input where a rule needs its content.
  The powers named by the groups are: Article 2(2) (any Order other than R&O.56/2025), 5(3), 6(3), 8(3)(n), 8(5)(e), 8(6)(d), 9(1)(d), 9(2), 9(3), 10(2), 11(2)(e)(iv), 11(3), 11(7), 11(8), 13(6)(h), 13(7) to (10), 13(12), 16(1)(d), 19(1)(h), 21(8), 22(2)(a)(ii), 22(4), 22(5), 23(4), 24(1) to (4), 25(1), 27(5), 28(1), 31(f), 36(2), 38, 39, 40(2), 40(3), 41(2), 42 and Schedule 2 paragraph 4(3).
  The three instruments made under the Law (R&O.19/2018, R&O.59/2018, R&O.60/2018) are out of scope.
- **The other enactments**: the Trusts, Companies, Foundations, Non-Profit Organizations, Revenue Administration, Income Tax, financial-services and Dormant Bank Accounts Laws, the Loi (1862), and the Interpretation (Jersey) Law 1954.
  Whether a body is of a kind they define, who its officers are, whether an act is an offence under one of them, and what they say about reckoning a period are inputs or forks.
  The Interpretation (Jersey) Law 1954 would settle how a period, a month and a year are counted, and every counting convention in the encoding is a fork for that reason.
- **Amounts and terms**: the amount of "level 3 on the standard scale" (the standard scale of fines is not among the sources) and any maximum for "a fine" (G6 5, G7, G8 1); the time in days of "promptly", "a reasonable time" and "as soon as practicable" wherever the Law gives none (G2, G5, G6 4).
- **Time limits the Law does not state**: for establishing the register and entering the items (8(1), 8(3), 8(5)); for the Commissioner's decisions under 11, 12 and 15(3) (unless an Order under 11(8)(a)(i) fixes one for 11); for the duties of 15(2), 17(6), 18(1), 18(2), 19(7), 19(9)(a); for the Minister's duty to appoint; for a notice under 26(1) to name a time.
  A MUST with no time stands until done and cannot be breached by delay; the encoding says so and invents no deadline.
- **Judgements as inputs**: "satisfied", "believes", "in the opinion of", "approved by", "fit and proper", "unfit", "proportionate", "expedient in the public interest", "reasonable", "substantial", "related", "too similar", "offensive", "analogous", "purely ancillary or incidental", "a reasonable degree" of public benefit, and the like (G1 item 5, G2, G3 8, G4, G5 8, G6 8, G8 8, G9 11).
- **How a notice is served** (Article 38 is only a power to make an Order) and what an Order under it says (G7, G8 5).
- **Who prosecutes** the offences, the procedure of the court and tribunal beyond what the Articles state, and the status of statements under 26(9) outside the proceedings it mentions (G5 13, G6 11, G8 8, 9).
- **Consequences the Law does not state**: of a determination made in breach of 5(5), 7(2) or 7(3) (G2); of breaching 12(7), 13(4) to (7) or 13(11)(a) other than as misconduct (G4, G5 13); of a failure to comply with a requirement under 12(6); of an appeal on the decision appealed; of a refusal to deregister, and whether it is appealable; of the Commissioner never deciding an application (G4, G6 12, G8).
- **Facts of the world**: whether the Commissioner's guidance of 5(4) exists or has been laid before the States; who holds the office of Commissioner and who acts when the holder cannot (Schedule 1 4(5), G9); whether an Order under Article 38 or under 20(1) of the Dormant Bank Accounts Law exists; the model constitutions published under 2(8)(b)(i) (G1 item 8, G2).
- **Jersey time**: whether the 9.30 a.m. of 27 February 2024 is Jersey time (assumed, not ruled; G7).

## 10. The answer table: headline scenarios

Each row is a scenario of an `int-tests-*.l4` module.
Each expected answer was decided by hand from the Law before the module was run, and the assertions that state it pass (section 11).
"The Commissioner must register" and similar answers are what the encoding computes on the facts of the scenario and on the readings taken; they are not an opinion that a court would agree (no domain expert has read this).
The facts the Law leaves to a judgement (public benefit, the Commissioner's opinion on a name, and so on) are inputs of the scenario.
All the scenarios of headline (a) to (d) and (f) are asked on 2 October 2026 unless a row gives another day.

### 10.1 Headline (a): may an application be granted (`int-tests-application.l4`)

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| A1 | a Jersey company advancing education, a complete application lodged 1 June 2026, a registered office in Jersey, a name with no objection, the declarations stated, no bar | the Commissioner must register the applicant; the application may be granted; the entity is a company and a Jersey entity; the principal address is the registered office | 6(1)(b), 2(1)(f), 2(3)(a), 8(4)(a), 11(4), 12(1), 19(5), 19(6) |
| A2 | as A1, and a governor has reported a matter that is not yet determined | the six matters hold but the Commissioner must not yet grant the application (the bar postpones the duty); with the matter determined and complied with the application may be granted; on reading B of F4.4 the duty to register stands (the Commissioner must register the applicant), and on reading C the question refuses by name because the Law's bars conflict | 11(4), 19(9)(c); F4.4 |
| A3 | as A1, and the court ordered on 3 March 2026 that the entity must not be registered | the Commissioner must not register the applicant; asked on 2 March 2026 (before the order) the application may be granted | 20(1)(c), 20(2)(b), 11(4) |
| A4 | as A1, without the copy of the constitution | the application does not include what Article 11(2) requires; no duty to register or to refuse arises; no decision | 11(2)(b), 11(4), 11(5); F4.3 |
| A5 | as A1, with a purpose of advancing a political party | the entity does not meet the charity test; the Commissioner must refuse to register the applicant | 6(5), 5(1)(a), 11(4)(a), 11(5) |
| A6 | a company established abroad, no activity in or from Jersey | its kind is "substantially similar", it is not a Jersey entity, 11(4)(c) is not met; the Commissioner must refuse | 2(1)(j), 2(3), 11(4)(c) |
| A7 | the name is the registered name of another charity | the name is undesirable; the Commissioner must refuse | 12(1)(a), 11(4)(e) |
| A8 | as A1 but the application does not state that it holds the declarations | 19(5) is not complied with; no duty arises | 19(5), 19(6), 11(4) |
| A9, A10 | asked on 30 April 2018 and on 1 June 2018 | refused: Article 8 (Part 4) was not in force, it came into force on 1 May 2018; and, on 1 June 2018, no text of the Law before 1 January 2019 is among the sources | R&O.17/2018 (the Table of Legislation History) |
| A11 | asked on 27 February 2024 (the text changed at 9.30 a.m.) for a company applicant | answered (neither text differs on a company applicant): may be granted | R&O.10/2024 |
| A12 | an NPO body corporate established in Jersey | on 15 October 2025 it is no entity, not a Jersey entity, and the Commissioner must refuse; on 16 October 2025 it falls within (ba), is a Jersey entity and the application may be granted | 2(1)(ba), 2(3)(a); R&O.56/2025 |
| A13 | as A1 with an Order that requires only payment details in the annual return | the application includes what Article 11(2) requires, and may be granted | 11(2)(e)(ii), 13(9)(a); IP29 |
| A14 | as A1 with an Order that requires a statement of intentions | the application is short of Article 11(2) (no draft statement) and no duty arises | 11(2)(e)(ii), 13(9)(b); IP29 |

### 10.2 Headline (b): registered charity and the register (`int-tests-register.l4`)

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| B1 | a charity entered in the general section on 1 March 2019, no notice | a registered charity; section general; the entries the Commissioner must make are the seven of 8(3)(a), (b), (c), (e), (f), (g), (j); the principal address is the registered office; the historic section and the restricted section's public elements are empty; the recorded standing agrees with the entries | 1, 8(2), 8(3), 8(4)(a) |
| B2 | a required steps notice served on the charity | the entries include the note of the notice and the date it was served | 8(3)(k) |
| B3 | an organized religious charity | the entries include the note that it is one | 8(3)(h), 28 |
| B4 | entered in the restricted section on 1 June 2022 | a registered charity in the restricted section, whose public elements are the number, the matters of 8(3)(a), (e), (f), (j) and the summary of reasons; asked on 31 May 2022 it is still in the general section and the recorded standing disagrees with the entries | 9(1) |
| B5 | deregistered into the historic section on 1 June 2025 | not a registered charity; section historic; nothing is owed under 8(3); the entries of 8(5) are the former number, the name(s), a summary of the reason and the dates; asked on 31 May 2025 it is a registered charity in the general section | 1, 8(5); trap T7 |
| B6 | meets the test only by virtue of an Order under 5(3) | the register holds the text of the constitution provision | 5(2), 5(3), 8(3)(i) |
| B7, B8 | asked on 30 April 2018 and on 1 June 2018; a recorded standing that disagrees with the dated entries | refused as in A9 and A10; the answer says the standing disagrees | R&O.17/2018 |

### 10.3 Headline (c): what follows from a contravention (`int-tests-contravention.l4`)

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| C1 | nothing has gone wrong | no contravention, no misconduct, no governor in misconduct, no ground for a notice, no ground to deregister, the court's power not open (nothing appears to the court to be amiss), someone is acting as the Commissioner, no deregistration effects | 2(10), 14(1), 16(1), 27(1) |
| C2 | a governor reported a matter on 1 March 2026 and acted on 1 April 2026 without permission | a provision was contravened (19(10)); the charity's conduct is misconduct; the governor engages in misconduct; the Commissioner may believe misconduct by the charity and by a governor; the court's powers are exercisable on the Commissioner's application; on 28 February 2026 none of this | 19(10), 2(10)(a)(i), 18(4)(a), 27(1)(a), (c), 14(1) |
| C3 | the office of Commissioner is vacant | nobody is acting as the Commissioner and the court's power on the Commissioner's application is not open; with a relevant person designated it is | Sch 1 4(5), 14(1); IP28 |
| C4 | a required steps notice (sent 10 January, received 12 January 2026, 30 days) was not complied with; a preliminary notice of 1 May 2026; deregistration notice received 15 June 2026 | a ground of 16(1)(c) exists on 15 June 2026 and not on 1 February 2026; the power to deregister is open on 15 June and not on 15 May; the basis is the failure to comply; the deregistration is not retrospective; the date deregistered is 15 June 2026 and the information is retained to 15 June 2036 | 16(1)(c), 17(1)(a), 17(2), 17(3), 38 |
| C5 | a governor subject to a disqualification order of 2024 to 2028 | a reportable matter; the duty to report (19(2)) stands until the governor reports to the charity and to the Commissioner; a governor with nothing to report has no duty; a name that is not a governor is a refusal | 19(1)(b), 19(2) |
| C6 | asked on 31 December 2018 and on 30 April 2018 | refused: Article 22 (Part 6) came into force on 1 January 2019; Article 12 (Part 4) on 1 May 2018 | 22, 12; trap T30 |
| C7 | an offence of dishonesty in relation to an entity not on the register | misconduct if the entity is an excepted foreign charity (established in the United Kingdom, entitled to call itself a charity there, managed from there) and not if established under Jersey law | 2(10)(b)(v), 22 |

### 10.4 Headline (d): offence and penalty (`int-tests-offence.l4`)

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| D1 | an unregistered Jersey company calls itself a charity | an offence (strict); a fine of level 3 and no imprisonment; within the cap; no officer in question | 21(3), 21(10), Sch 2 4(3)(f) |
| D2 | the director, knowing it is untrue and to induce a gift of property, makes the company say so | two offences are made out (level 3; 24 months and a fine on F7.4); the director who connived is also guilty and takes the body's penalty (level 3) | 21(3)(b), 21(4), 37(1) |
| D3 | the connivance of the trustee of an unincorporated association | not within 37(1) as written: the officer is not guilty, no penalty | 37(1); trap T26 |
| D4 | a governor acts on 1 April 2026 after reporting on 1 March, without permission and without reasonable excuse | an offence, 12 months and a fine; not on 28 February 2026; not with a reasonable excuse | 19(10), 19(11) |
| D5 to D7 | contravening a disqualification order; failing to comply with a requirement; giving false information for an application | 24 months and a fine (no offence if the order is not contravened); 3 months and a fine of level 3; 24 months and a fine | 20(6), 26(7), 26(10) |
| D8 | asked on 31 December 2018 and on 30 April 2018 | refused: Article 21 (Part 6) came into force on 1 January 2019; Article 19 (Part 5) on 1 May 2018 | 21, 19 |

### 10.5 Headline (e): which text and which units (`int-tests-vintage-matrix.l4`, `int-tests-commencement.l4`)

| day | answer | provisions |
| --- | --- | --- |
| 31 December 2018 | refused: no text of the Law before 1 January 2019 is among the sources | the Table of Legislation History |
| 1 January to 30 May 2019 | the text of 1 January 2019; "Minister" is the Chief Minister (inferred); "Comptroller" is defined by the Income Tax (Jersey) Law 1961 | Article 1; R&O.40/2019 |
| 31 May 2019 | the text of 31 May 2019; the Minister for External Relations | R&O.40/2019 |
| 16 December 2019 | the text of 16 December 2019; Schedule 1 carries the Dormant Bank Accounts words | L.1/2017; Sch 1 2(4)(a), 4(7) |
| 1 January 2020 | the text of 1 January 2020; "Comptroller" is defined by the Revenue Administration (Jersey) Law 2019 | L.13/2019, R&O.136/2019 |
| 2 March 2021 | the Minister for External Relations and Financial Services | R&O.29/2021 |
| 12 April 2023 | the Chief Minister | R&O.28/2023 |
| 27 February 2024 | by day: refused, because the text changed at 9.30 a.m.; by instant: the text of 12 April 2023 until 9.29.59 and the text of 27 February 2024 from 9.30.00 (the Minister for External Relations) | R&O.10/2024 |
| 16 October 2025 | sub-paragraph (ba) of Article 2(1) is in the text | R&O.56/2025 |
| 2 October 2026 and later | the text of 2 October 2026; the Chief Minister | R&O.102/2026 |
| units in force | Parts 1 to 3, Article 32, Articles 38 to 43 and the Schedules from 21 November 2014; Articles 8 to 20, 26 to 31 and 33 to 37 from 1 May 2018; Articles 21 to 25 from 1 January 2019 | R&O.17/2018, Table of Legislation History |

### 10.6 Headline (f): who may appeal what, and by when (`int-tests-appeal.l4`, `int-tests-decisions.l4`)

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| F1 | the applicant of A5 is refused and appeals | a right of appeal under 33(1)(a); the person may appeal | 33(1)(a) |
| F2 | a notice sent 5 October and received 7 October 2026; an Order allowing 28 days | served on 7 October (receipt); the last day is 4 November 2026; lodged on 4 November in time, on 5 November out of time; with no Order the time cannot be judged (a named refusal) and no last day is given | 36(2), 38; F7.7, F8.6, F8.12 |
| F3 | a registered charity, and the Attorney General | the charity has a right of appeal against a deregistration (33(2)(a)) and none against a refused request for the restricted section; the Attorney General may appeal any decision (33(4)) | 33(2), 33(4); trap T12 |
| F4 | a third party with an interest in the name appeals a decision to register | no right unless the charity test failed at both times (IP9); then 33(5)(a) | 33(5) |
| F5 | asked on 30 April 2018 | refused: Article 12 (Part 4) is the first in the list not in force | R&O.17/2018 |
| decisions | each decision produced by G3, G4, G5, G6 and G8 | 33(1)(a), (b), 33(2)(a) to (e), 33(3) and 33(4) are reached from the outcome each producer chooses; the prior permission of 13(5)(b), the refusal to deregister on application and a refused request for the restricted section give a charity "no appeal is given by Part 8"; the Commissioner's staff may not take the decisions under 11, 15(3) and 16 | 33, Sch 1 4(3) |

### 10.7 Chains across the headlines (`int-tests-chains.l4`)

| chain | steps | answers |
| --- | --- | --- |
| 1 | Gorey Schools Limited, registered in the general section on 1 March 2019; an illustrative Order makes the annual return for 2019 due on 31 March 2020 | 2 March 2019: a registered charity with the seven entries of 8(3); 28 February 2019: not yet entered. 1 April 2020: the duty of 13(7) is breached (a trace), which is a contravention (IP13) and misconduct (2(10)(a)(i)); the Commissioner may believe it (27(1)(a)). 10 May 2020: a required steps notice sent 8 May is served on 10 May (receipt), its 30 days end on 9 June (7 June on the other reading of F7.7). 15 July 2020: the notice is not complied with, the power to deregister is open and used, the date deregistered is 15 July 2020, the information is retained to 15 July 2030. 16 July 2020: in the historic section and no longer a registered charity; the entries of 8(5). 1 August 2020: the former charity still says it is a charity, an offence of Article 21 at level 3, and its director who connived is also guilty (37(1)) |
| 2 | a conviction for that offence | a reportable matter of the director (19(1)(f)), built from headline (d)'s own answer |
| 3 | an NPO body corporate entered in the general section on 1 December 2025 | a registered charity in the text of 2 October 2026 (and not before 16 October 2025 under the earlier text); the note of status names (ba) and requires neither "also within (a)" nor enactment details; the principal address is the main premises |

### 10.8 What changed after the independent testing, and fork F2.14 (`int-tests-repairs.l4`)

Each expected answer was decided by hand from the Law before the module was run, and all 48 assertions of R1 to R6 held on the first run.
The 18 assertions of R7 (fork F2.14, added later the same day) held on the first run that compiled; the first attempt did not compile, because the facts record that R1 builds by hand lacked the new eleventh field.

| id | facts | answer | provisions |
| --- | --- | --- | --- |
| R1 | a Jersey company whose only purpose is to run a sports hall open to the public (head (i)), application otherwise as A1 | the object of improving the conditions of life stated true: the test is met and the Commissioner must register; stated false: the purpose is not charitable and the Commissioner must refuse; not stated and 6(2)(d) met: refused by name ("Article 6(1)(i) was not given whether the facilities or activities have the object of improving the conditions of life"); not stated and 6(2)(d) not met on either alternative: not charitable, the Commissioner must refuse (not a refusal to answer); for persons in need with the object stated: met | 6(1)(i), 6(2)(d), 5(1)(a), 11(4)(a), 11(5) |
| R2 | a partnership applies with the same charitable purpose as A1 | `kinds of entity` is empty, the charity test is not met, the Commissioner must refuse; a company with such a purpose is accepted (A1) | 2(1)(i), 5(1), 11(4)(a) |
| R3 | a member of the Commissioner's staff finds public benefit for a company that benefits only identified natural persons; every other duty is met | reading A of F2.13 (taken): staff are bound, the finding does not make the entity one that provides public benefit, the test fails and the Commissioner must refuse; reading B: the finding stands, the test is met and the Commissioner must register; the same finding by the Commissioner fails on both readings | 7(1), 7(3)(b), 5(5), Sch 1 4(3) |
| R4 | the units of the Law in force, headline (e), on 30 April 2018, 1 May 2018, 31 December 2018 and 1 January 2019 | Parts: 1, 2, 3 on 30 April 2018; 1, 2, 3, 4, 5, 7, 8 on 1 May 2018 and on 31 December 2018; all nine on 1 January 2019 (Part 9 is held back by the original Article 41, stage 3); on reading B of F7.9 Parts 8 and 9 are in force from 2014 (1, 2, 3, 8, 9 on 30 April 2018); Articles in force: 14, 38, 43; present Article 41 in force from 2014 | Table of Legislation History; R&O.17/2018 Articles 1 and 2 |
| R5 | a partnership, an NPO body corporate and a Jersey company, none on the register, say they are a charity in connection with their Jersey activities | the partnership: no offence, no penalty; the Jersey company: the strict offence of 21(3), level 3; the NPO body corporate: no offence on 15 October 2025 (no entity before (ba)), the strict offence at level 3 on 16 October 2025 | 21(3), 21(5), 21(10), 2(1)(ba); R&O.56/2025 |
| R6 | headline (a), a complete application, on 30 April 2018, 1 May 2018 and 1 January 2019 | 30 April 2018: refused, Article 8 (Part 4) was not in force; 1 May 2018: refused, no text of the Law before 1 January 2019 is among the sources; 1 January 2019: answered (may be granted) | R&O.17/2018; IP4 |
| R7 | a Jersey company whose only purpose is to provide residential accommodation and care, recorded under no head, with nobody shown to be in need (the eleventh fact TRUE, the need-qualified seventh fact FALSE) | at the purpose level: not a charitable purpose on reading A of F2.14 (taken), a charitable purpose on reading B; with neither fact, not charitable on either; with the need-qualified fact TRUE, charitable on both. Through headline (a) with the public benefit determination in favour: A, the test is not met and the Commissioner must refuse; B, the test is met and the Commissioner must register. Through headline (a) with the Commissioner's determination that no public benefit is provided: the test is not met on B either (the purpose is charitable, public benefit is not shown) and the Commissioner must refuse. A care home for persons in need, with public benefit shown: registered on both readings | 5(1)(b), 6(1)(n), 6(2)(e), 7(3)(a), 11(4)(a); F2.14 (default ruled by the owner (Meng), 2026-10-27; the widening reading stays callable) |

## 11. Tests, and what `check.sh` prints

### 11.1 What `check.sh` prints

This is the full output of `check.sh` run in the deposit on 2026-10-27, after the repairs of G2 and G7, the merge of the independent tests and the rewiring for fork F2.14 (Article 6(2)(e)), with the fleet's `l4` (the run took between five and ten minutes, depending on what else the machine was running).
It was run again in a clean copy of the deposit, with the same result (section 11.8).
The columns are, for each module: error diagnostics, assertions satisfied, assertions failed, assertions refused, warnings, and the number of failures and of refusals the module is meant to have.
A failed assertion is also an error and a refused assertion is also a warning; the run is red for any other error, any refusal or warning beyond the module's own, and any failed count other than the module's own.
The hash results are the first lines, the shape check, the `srcrefs` check and the trace check follow the table.

```
check.sh of /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/deposit
l4 binary: /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/7d96192f-aaa4-44f5-ac28-10f6e3777fd5/scratchpad/je-full/deposit/../bin/l4 (sha256 matches the fleet's binary 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475)
domain.l4: sha256 matches the pin (af1703908b8f62922ed36a9984104231b93b41703deec7c1e45f1fef84399d66)

module                                    errors satisfied  failed  refused  warnings  exp.fail exp.refuse
domain.l4                                      0         0       0        0         0         0         0
g1-art1-defined-terms.l4                       0         0       0        0         0         0         0
g1-art2-entity.l4                              0         0       0        0         0         0         0
g1-art2-governor-misconduct.l4                 0         0       0        0         0         0         0
g1-interpretation.l4                           0         0       0        0         0         0         0
g1-tests-art1.l4                               0        74       0        0         0         0         0
g1-tests-art2-entity.l4                        0       185       0        0         0         0         0
g1-tests-art2-governor-misconduct.l4           0       147       0        0         0         0         0
g2-art3-4-commissioner.l4                      0         0       0        0         0         0         0
g2-art5-charity-test.l4                        0         0       0        0         0         0         0
g2-art6-purposes.l4                            0         0       0        0         0         0         0
g2-art7-public-benefit.l4                      0         0       0        0         0         0         0
g2-fixtures.l4                                 0         0       0        0         0         0         0
g2-nouns.l4                                    0         0       0        0         0         0         0
g2-readings.l4                                 0         0       0        0         0         0         0
g2-tests-art3-4.l4                             0        30       0        0         0         0         0
g2-tests-art5.l4                               0       171       0        0         0         0         0
g2-tests-art6.l4                               0       126       0        0         0         0         0
g2-tests-art7.l4                               0        82       0        0         0         0         0
g2-tests-red.l4                               16         0      16        0         0        16         0
g3-art10-public-access.l4                      0         0       0        0         0         0         0
g3-art8-register.l4                            0         0       0        0         0         0         0
g3-art9-restricted-section.l4                  0         0       0        0         0         0         0
g3-fixtures.l4                                 0         0       0        0         0         0         0
g3-nouns.l4                                    0         0       0        0         0         0         0
g3-tests-art10-public-access.l4                0        50       0        0         0         0         0
g3-tests-art8-address.l4                       0        28       0        0         0         0         0
g3-tests-art8-historic.l4                      0        26       0        0         0         0         0
g3-tests-art8-register.l4                      0       129       0        0         0         0         0
g3-tests-art8-retention.l4                     0        26       0        0         0         0         0
g3-tests-art8-time.l4                          0        44       0        0         0         0         0
g3-tests-art9-restricted-section.l4            0       103       0        0         0         0         0
g3-tests-readings.l4                           0        43       0        0         0         0         0
g3-tests-red.l4                               12         0      12        0         0        12         0
g4-art11-application.l4                        0         0       0        0         0         0         0
g4-art11-decision.l4                           0         0       0        0         0         0         0
g4-art12-name.l4                               0         0       0        0         0         0         0
g4-interpretation.l4                           0         0       0        0         0         0         0
g4-nouns.l4                                    0         0       0        0         0         0         0
g4-tests-art11-application.l4                  0        83       0        0         0         0         0
g4-tests-art11-decision.l4                     0        82       0        0         0         0         0
g4-tests-art12-name.l4                         0        34       0        0         0         0         0
g4-tests-fixtures.l4                           0         0       0        0         0         0         0
g4-tests-forks.l4                              0       210       0        0         0         0         0
g4-tests-red.l4                               14         0      14        0         0        14         0
g5-art13-effects.l4                            0         0       0        0         0         0         0
g5-art13-reporting.l4                          0         0       0        0         0         0         0
g5-art14-court-powers.l4                       0         0       0        0         0         0         0
g5-interpretation.l4                           0         0       0        0         0         0         0
g5-nouns.l4                                    0         0       0        0         0         0         0
g5-tests-art13-effects.l4                      0        92       0        0         0         0         0
g5-tests-art13-reporting.l4                    0       127       0        0         0         0         0
g5-tests-art14.l4                              0        82       0        0         0         0         0
g5-tests-fixtures.l4                           0         0       0        0         0         0         0
g5-tests-forks.l4                              0        41       0        0         0         0         0
g5-tests-properties.l4                         0         4       0        0         0         0         0
g5-tests-red.l4                               16         0      16        0         0        16         0
g6-art15-16-deregistration.l4                  0         0       0        0         0         0         0
g6-art17-after-deregistration.l4               0         0       0        0         0         0         0
g6-art18-governor-duties.l4                    0         0       0        0         0         0         0
g6-art19-reportable-matters.l4                 0         0       0        0         0         0         0
g6-art20-court-orders.l4                       0         0       0        0         0         0         0
g6-interpretation.l4                           0         0       0        0         0         0         0
g6-tests-art15-16.l4                           0        64       0        0         0         0         0
g6-tests-art17.l4                              0        76       0        0         0         0         0
g6-tests-art18.l4                              0        59       0        0         0         0         0
g6-tests-art19.l4                              0       167       0        0         0         0         0
g6-tests-art20.l4                              0        60       0        0         0         0         0
g6-tests-red.l4                               24         0      24        0         0        24         0
g7-art21-23-expressions.l4                     0         0       0        0         0         0         0
g7-art24-25-powers.l4                          0         0       0        0         0         0         0
g7-art37-43-final.l4                           0         0       0        0         0         0         0
g7-commencement.l4                             0         0       0        0         0         0         0
g7-interpretation.l4                           0         0       0        0         0         0         0
g7-tests-commencement.l4                       0       389       0        0         0         0         0
g7-tests-expression-traces.l4                  0         0       0        0         0         0         0
g7-tests-expressions.l4                        0       695       0        0         0         0         0
g7-tests-fixtures-expressions.l4               0         0       0        0         0         0         0
g7-tests-powers-final.l4                       0        95       0        0         0         0         0
g7-tests-red.l4                               15         0      15        0         0        15         0
g7-tests-vintages.l4                           0       250       0        0         0         0         0
g7-vintages.l4                                 0         0       0        0         0         0         0
g8-art26-demand.l4                             0         0       0        0         0         0         0
g8-art27-28-required-steps.l4                  0         0       0        0         0         0         0
g8-art29-31-information.l4                     0         0       0        0         0         0         0
g8-art32-36-appeals.l4                         0         0       0        0         0         0         0
g8-nouns.l4                                    0         0       0        0         0         0         0
g8-penalties.l4                                0         0       0        0         0         0         0
g8-tests-art26.l4                              0       182       0        0         0         0         0
g8-tests-art27-28.l4                           0       101       0        0         0         0         0
g8-tests-art29-31.l4                           0        97       0        0         0         0         0
g8-tests-art32-36.l4                           0       197       0        0         0         0         0
g8-tests-fixtures.l4                           0       399       0        0         0         0         0
g8-tests-red.l4                               19         0      19        0         0        19         0
g9-common.l4                                   0         0       0        0         0         0         0
g9-interpretation.l4                           0         0       0        0         0         0         0
g9-sched1-commissioner.l4                      0         0       0        0         0         0         0
g9-sched2-tribunal.l4                          0         0       0        0         0         0         0
g9-tests-periods.l4                            0       170       0        0         0         0         0
g9-tests-red.l4                               19         0      19        0         0        19         0
g9-tests-sched1.l4                             0       230       0        0         0         0         0
g9-tests-sched2.l4                             0       203       0        0         0         0         0
g9-tests-t20.l4                                0        18       0        0         0         0         0
ind-a-tests-ambiguous.l4                       4         0       4        5         5         4         5
ind-a-tests-art1.l4                            0        32       0        0         0         0         0
ind-a-tests-art11-12.l4                        0        70       0        0         0         0         0
ind-a-tests-art2.l4                            0       115       0        0         0         0         0
ind-a-tests-art3-7.l4                          0        95       0        0         0         0         0
ind-a-tests-art8-10.l4                         0       125       0        0         0         0         0
ind-a-tests-commencement.l4                    0        28       0        0         0         0         0
ind-a-tests-disagree.l4                        2         0       2        0         0         2         0
ind-a-tests-fixtures.l4                        0         0       0        0         0         0         0
ind-a-tests-readings.l4                        0        70       0        0         0         0         0
ind-b-tests-ambiguous.l4                       2         0       2        0         0         2         0
ind-b-tests-art13-14.l4                        0       126       0        0         0         0         0
ind-b-tests-art15-17.l4                        0        87       0        0         0         0         0
ind-b-tests-art18-20.l4                        0       141       0        0         0         0         0
ind-b-tests-art21-25.l4                        0       100       0        0         0         0         0
ind-b-tests-art5-7.l4                          0       134       0        0         0         0         0
ind-b-tests-commencement-vintages.l4           0        51       0        0         0         0         0
ind-b-tests-disagree.l4                        0         0       0        1         1         0         1
ind-b-tests-fixtures-g2.l4                     0         0       0        0         0         0         0
ind-b-tests-fixtures-g5.l4                     0         0       0        0         0         0         0
ind-b-tests-fixtures-g6.l4                     0         0       0        0         0         0         0
ind-b-tests-fixtures-g7.l4                     0         0       0        0         0         0         0
ind-c-tests-ambiguous.l4                       8         0       8        4         4         8         4
ind-c-tests-art26-31.l4                        0       123       0        0         0         0         0
ind-c-tests-art32-36.l4                        0        65       0        0         0         0         0
ind-c-tests-art37-43.l4                        0        28       0        0         0         0         0
ind-c-tests-art5-7.l4                          0       110       0        0         0         0         0
ind-c-tests-commencement-vintages.l4           0       125       0        0         0         0         0
ind-c-tests-fixtures-g8.l4                     0         0       0        0         0         0         0
ind-c-tests-sched1.l4                          0        91       0        0         0         0         0
ind-c-tests-sched2.l4                          0        53       0        0         0         0         0
ind-c-tests-traces.l4                          0         0       0        0         0         0         0
int-commencement.l4                            0         0       0        0         0         0         0
int-h-appeal.l4                                0         0       0        0         0         0         0
int-h-application.l4                           0         0       0        0         0         0         0
int-h-contravention.l4                         0         0       0        0         0         0         0
int-h-offence.l4                               0         0       0        0         0         0         0
int-h-register.l4                              0         0       0        0         0         0         0
int-h-text.l4                                  0         0       0        0         0         0         0
int-nouns.l4                                   0         0       0        0         0         0         0
int-readings.l4                                0         0       0        0         0         0         0
int-tests-appeal.l4                            0        20       0        0         0         0         0
int-tests-application.l4                       0        49       0        0         0         0         0
int-tests-chains.l4                            0        41       0        0         0         0         0
int-tests-commencement.l4                      0       144       0        0         0         0         0
int-tests-consistency.l4                       0        35       0        0         0         0         0
int-tests-contravention.l4                     0        30       0        0         0         0         0
int-tests-counting.l4                          0        21       0        0         0         0         0
int-tests-decisions.l4                         0        24       0        0         0         0         0
int-tests-fixtures.l4                          0         0       0        0         0         0         0
int-tests-offence.l4                           0        20       0        0         0         0         0
int-tests-readings.l4                          0        10       0        0         0         0         0
int-tests-red.l4                               6         6       6        0         0         6         0
int-tests-register.l4                          0        27       0        0         0         0         0
int-tests-repairs.l4                           0        66       0        0         0         0         0
int-tests-vintage-matrix.l4                    0        81       0        0         0         0         0
int-tests-wiring.l4                            0        30       0        0         0         0         0
int-vintage.l4                                 0         0       0        0         0         0         0
int-wiring.l4                                  0         0       0        0         0         0         0
TOTAL (162 modules)                          157      7844     157       10        10       157        10
of which the group modules g1- to g9- (102): satisfied 5471, failed 135 (expected 135)
of which the integration modules int- (27): satisfied 604, failed 6 (expected 6)
of which the independent authors' modules ind- (32): satisfied 1769, failed 16 (expected 16), refused 10 (expected 10)
(a failed assertion is also an error and a refused assertion is also a warning; any other error, any refusal or warning beyond the module's expected_refused, and any failed count other than its expected_failed, make the run red)
@ref notices (follows code on its line / end of the file): 0

shape: every module has a plain name and starts without @lang en, and no group module imports another group's
srcrefs check: 1727 src: lines, 889 runs, 1668 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g1-tests-art2-entity.l4                            3         3         0      3     0          0
g2-tests-art3-4.l4                                11        11         0     11     0          0
g2-tests-art5.l4                                  28        28         0     28     0          0
g2-tests-art6.l4                                   3         3         0      3     0          0
g2-tests-art7.l4                                  20        20         0     20     0          0
g3-tests-art10-public-access.l4                    9         9         0      9     0          0
g3-tests-art8-historic.l4                          4         4         0      4     0          0
g3-tests-art8-register.l4                          7         7         0      7     0          0
g3-tests-art8-retention.l4                        17        17         0     17     0          0
g3-tests-art9-restricted-section.l4               15        15         0     15     0          0
g4-tests-art11-application.l4                     40        40         0     40     0          0
g4-tests-art11-decision.l4                        39        39         0     39     0          0
g4-tests-art12-name.l4                            34        34         0     34     0          0
g4-tests-forks.l4                                  4         4         0      4     0          0
g5-tests-art13-effects.l4                         29        29         0     29     0          0
g5-tests-art13-reporting.l4                       43        43         0     43     0          0
g5-tests-art14.l4                                 25        25         0     25     0          0
g6-tests-art15-16.l4                              43        43         0     43     0          0
g6-tests-art17.l4                                 40        40         0     40     0          0
g6-tests-art18.l4                                 11        11         0     11     0          0
g6-tests-art19.l4                                 67        67         0     67     0          0
g6-tests-art20.l4                                 34        34         0     34     0          0
g7-tests-expression-traces.l4                     87        87         0     87     0          0
g7-tests-powers-final.l4                          44        44         0     44     0          0
g8-tests-art26.l4                                 37        37         0     37     0          0
g8-tests-art27-28.l4                              15        15         0     15     0          0
g8-tests-art29-31.l4                              14        14         0     14     0          0
g8-tests-art32-36.l4                              46        46         0     46     0          0
g9-tests-sched1.l4                                65        65         0     65     0          0
g9-tests-sched2.l4                                66        66         0     66     0          0
ind-a-tests-art11-12.l4                           16        16         0     16     0          0
ind-a-tests-art2.l4                                1         1         0      1     0          0
ind-a-tests-art3-7.l4                              1         1         0      1     0          0
ind-a-tests-art8-10.l4                             8         8         0      8     0          0
ind-c-tests-traces.l4                             33        33         0     33     0          0
int-tests-chains.l4                                5         5         0      5     0          0
int-tests-contravention.l4                        12        12         0     12     0          0
TOTAL                                            976       976         0    976     0          0
check-traces: all 976 guarded trace(s) behaved as expected

check.sh: GREEN
(a green run is the integrator's: it says nothing about whether a domain expert agrees with any reading in NOTES.md; no domain expert has read this encoding against the Law)
```

### 11.2 The numbers, read

The group modules (102) hold 5471 assertions satisfied and 135 failed, all failures in the groups' red files (G2 16, G3 12, G4 14, G5 16, G6 24, G7 15, G8 19, G9 19; G1 has none).
G2 has 16 declared red: 14 at the first pass, 15 after the repairs of the independent testing, and 16 after fork F2.14 (FRAGMENT-G2.md: 15 fork readings answered as their other reading answers them, and one control).
The satisfied counts of G2 and G7 grew with the repairs (the first pass: 5,235 satisfied and 133 failed over the group modules).
The integration modules (27) hold 604 assertions satisfied and 6 failed (`int-tests-red.l4`).
The independent authors' modules (32) hold 1769 assertions satisfied, 16 failed and 10 refused, the last two only in their `ambiguous` and `disagree` files (section 12).
In all, 162 modules: 7844 assertions satisfied, 157 failed (expected 157), 10 refused (expected 10), 10 warnings (one per refusal).
No module has a refusal or a warning beyond the ten that are the authors' findings.
`srcrefs.py check --refs` over all modules finds 0 problems (1727 quotation lines, 889 runs, 1668 locators); the integration and independent modules quote nothing and carry no locator.
The `#TRACE` check covers 976 traces (the groups', the integrator's and the independent authors') and finds all of them guarded by an `-- EXPECT:` comment and all as expected.
These are the integrator's numbers and the groups' own; they say that the modules run and the tests pass, not that the readings are right.

### 11.3 The trace checker, and its positive control

A regulative rule (`MUST`, `MAY`, `SHANT`) run against a list of events yields a value that `#ASSERT` cannot compare, and `l4 run` prints it and exits 0 whatever it printed; so the traces guard nothing unless something reads them.
`check-traces.py` reads the `-- EXPECT:` comment above each `#TRACE` (the kinds `FULFILLED`, `BREACH` with text that must occur in the result, `STANDING` with text) and compares it with the result `l4 run --json` gives for that line.
It fails for a wrong result, for a trace with no `EXPECT` comment (reported as UNGUARDED), for an `EXPECT` comment that no trace claims, and for a run that does not start or prints no result.
The nine group encoders each ran a copy of one script (`work/g1/check-traces.py` to `work/g9/check-traces.py` are byte-identical, md5 `3dc03fb11d878b5f3c9e439094a756f2`, also the fleet's `inputs/templates/check-traces.py`); the integrator kept that behaviour so that the group traces are guarded exactly as their encoders guarded them, and changed only the docstring and the default of `--sidecar` (now none: no trace of this encoding needs a sidecar).
It reports no trace without an `EXPECT` comment.

The positive control, run on 2026-10-27: a copy of `int-tests-chains.l4` with its first `-- EXPECT: BREACH Article 13(7)` changed to `-- EXPECT: FULFILLED` fails; a copy with the comment `-- EXPECT: STANDING MAY` deleted fails with the trace reported as UNGUARDED; the unaltered module passes.
The copies were made beside the other modules so that their imports resolve, run, and deleted.

```
== control 1: copy of int-tests-chains.l4 with its first -- EXPECT: BREACH Article 13(7) changed to -- EXPECT: FULFILLED
module                                        traces in-module   sidecar     ok   bad  unguarded
zz-control-wrong-expect.l4:61: expected FULFILLED (comment line 60), got: DEONTIC BREACHED: /   BREACH /   BY `a registered charity` /   BECAUSE "Article 13(7): the annual return was not sent by the due date set by the Order"
zz-control-wrong-expect.l4                         5         5         0      4     1          0
TOTAL                                              5         5         0      4     1          0
check-traces: FAILED, 1 trace(s) did not behave as expected, 0 problem(s) with the expectations themselves (stale sidecar rows, EXPECT comments that no trace claims)
exit status: 1

== control 2: copy of int-tests-chains.l4 with the comment -- EXPECT: STANDING MAY deleted
module                                        traces in-module   sidecar     ok   bad  unguarded
zz-control-no-expect.l4:156: UNGUARDED: #TRACE with no EXPECT comment and no sidecar row
zz-control-no-expect.l4                            5         4         0      4     0          1
TOTAL                                              5         4         0      4     0          1
check-traces: 1 trace(s) have no expectation
exit status: 1

== control 3: the unaltered module int-tests-chains.l4, for comparison
module                                        traces in-module   sidecar     ok   bad  unguarded
int-tests-chains.l4                                5         5         0      5     0          0
TOTAL                                              5         5         0      5     0          0
check-traces: all 5 guarded trace(s) behaved as expected
exit status: 0
```

The checker also earned its place on the integrator's own code: it flagged the first version of the governor's duty to report (defect X9 in section 13), whose traces had passed for the wrong reason.

### 11.4 Kept-failing assertions: `int-tests-red.l4`

`int-tests-red.l4` holds six assertions that state what the Law says and fail on the readings taken, and six positive controls that pass.
Every one of the six was predicted before the module was run, and the run was read (not counted): the six failing lines are exactly the six intended, and the six controls are satisfied.

| seam | assertions that fail | what the Law says | why they fail | control that passes |
| --- | --- | --- | --- | --- |
| 1 (IP35) | four: G6 Article 20(6), G7 Articles 21(9) and 23(7), G8 Articles 26 and 29, G9 Schedule 2 paragraph 4(3)(f) | a term of exactly 2 years beginning on 2 October 2026 (731 days) is within a maximum of 2 years | on the days unit three groups take 2 years as 730 days and G9 converts 24 months from the start day to 731 days and compares with 730 | the same four on the calendar-months reading |
| 2 (IP29) | one: G5's composite fact equals the limb-(b) fact | whether an Order under Article 13(9)(b) applies is one question | for an Order of limb (a) alone the composite is TRUE and the limb fact FALSE | the equality holds for an Order of limb (b) |
| 3 (registered charity) | one: G1's answer equals G8's | whether an entity is a registered charity is one question | for an NPO body corporate entered in the general section and asked about in the text of 12 April 2023, G1 says no and G8 says yes | the equality holds in the text of 16 October 2025 |

### 11.5 Mutation testing of the wiring (not a gate)

To ask whether the integration tests would notice a wrong wire, sixteen one-line changes were made to a copy of the integration modules, one at a time, and the test modules that should notice were run on each.
A mutant is killed if a listed module has an error, a refused assertion or a warning.
The harness (`mut_run2.py`) and its output are in the integrator's working directory and are not deposited.
After two additions to the tests, all sixteen are killed.
The mutation run was made on the first pass's modules, before the repairs of G2 and G7; the repairs changed no mutated line (only the generated `int-readings.l4` and `int-tests-fixtures.l4` gained a field), and it was not re-run.

| mutant | killed by |
| --- | --- |
| M01b IP34: the date of service of a notice is the date sent | `int-tests-chains`, `int-tests-contravention` (the date of receipt left out refuses by name) |
| M02 the gate of headline (c) omits Article 22 | `int-tests-contravention` (C6) |
| M03b IP29: Article 11(2)(e)(ii) read from G5's composite fact | `int-tests-application` (A13); the first run of this mutant SURVIVED, and A13 and A14 were added |
| M04 IP28 left out of the court's power | `int-tests-contravention` (C3) |
| M05 IP6: every entity is a registered charity | `int-tests-register`, `int-tests-chains` |
| M06 IP13: no contravention counts | `int-tests-contravention`, `int-tests-chains` |
| M07 IP17: every entity has a principal address in Jersey | `int-tests-wiring` (not `int-tests-application`) |
| M08 IP21: governors carry no reportable matters | `int-tests-contravention` (C5), `int-tests-chains` |
| M09 IP25: the Commissioner's designation is ignored | `int-tests-wiring` (not `int-tests-offence`) |
| M10 IP35: group G8 does not take the fleet's unit | `int-tests-consistency` (not `int-tests-readings`) |
| M11 IP33: group G3 does not take the fleet's year | `int-tests-consistency` |
| M12b IP34: the date of service of a notice of a decision is the date sent | `int-tests-appeal` (F2), `int-tests-chains` |
| M13 IP20: no charity is an organized religious charity | `int-tests-register` (B3) |
| M14 IP26: no entity is an excepted foreign charity | `int-tests-contravention` (C7); the first run of this mutant SURVIVED, and C7 was added |
| M15 IP9: the charity test at the time of the application is read at the time of the appeal | `int-tests-appeal` (F4) |
| M16 the gate of headline (a) omits Article 8 | `int-tests-application` (A9) |

After the rewiring for fork F2.14, two mutants of the G2 rule (made on copies of all the modules, one change each, and not of the integration layer, so they are outside the sixteen) asked whether R7 of `int-tests-repairs.l4` notices a wrong reading:

| mutant | killed by |
| --- | --- |
| M17 reading B of Article 6(2)(e) ignores the new eleventh fact (B becomes A) | the four assertions that hold only on B: the purpose-level assertion, and the charity test, the Commissioner's duty to register and the grant in headline (a) |
| M18 reading A of Article 6(2)(e) also reads the new eleventh fact (A becomes B) | the three assertions that hold only on A: the purpose-level assertion, and the charity test and the Commissioner's duty to refuse in headline (a) |

The other eleven assertions of R7 hold under both mutants, as they should: they are the cases on which the two readings agree.

Two things the table does not say: the first batch counted only errors, so M01 and M12 looked like survivors until refusals were counted (a refusal is a Warning, not an error); and mutation testing of the group modules is the groups' own (for example G3's fragment, section 9.3).

### 11.6 What changed after a first run

The expected values were decided before each run, and the runs were read.
These are the departures, all in the integrator's own modules except the one noted:

- Scenario A1 first failed because the fixtures were wrong, not the Law: the application needed `procedure under Regulations under Article 11(3)(b) followed` TRUE (defect X5), and a clear set of findings carried "will meet the charity test on registration" TRUE, which masked the test of IP8.
- Scenario C3 first failed because group G5's BOOLEAN ignores IP28 (defect X1); headline (c) now conjoins it.
- The first version of `int-tests-appeal.l4` expected Article 5 to be the first Article not in force on 30 April 2018; Article 5 is in Part 3 (21 November 2014), and the first in the list that was not in force is Article 12; the expectation was corrected from the Table of Legislation History, not from the output.
- A Part map in the generator of `int-commencement.l4` was wrong and was corrected from the Law's headings (P1 Articles 1 and 2, P2 3 and 4, P3 5 to 7, P4 8 to 17, P5 18 to 20, P6 21 to 25, P7 26 to 31, P8 32 to 36, P9 37 to 43).
- The first versions of the governor's duty traces passed for the wrong reason (defect X9).

### 11.7 What the tests do not cover

The integration tests cover the six headlines on the scenarios of section 10 and the wiring of every integration point at least once (section 3.4).
They do not run every fork on both readings through every headline: the groups' own tests do that for their forks, and the integrator's only for the forks that cross groups (F2.5 with F8.3, F2.13, F2.14, F4.4, F7.7, F7.9, F8.14, the shared year and unit, and the counting conventions).
No test calls a headline for every one of the ten values of `Vintage of the text` except headline (e).

### 11.8 The clean-copy run

The deposit, the fleet's `inputs` and `bin` were copied side by side into a fresh directory (`work/integrator/clean3/` in the fleet's working directory: `deposit/`, `inputs`, `bin`) and `check.sh` was run there, with nothing else in sight.
The copy was made after the last module, test and checker had changed, and before `NOTES.md`, `README.md` and `encoding.json` received their final figures, none of which `check.sh` reads; every other file of the deposit is byte-identical to the copy.
It ended GREEN in 9 minutes 29 seconds, and its output is identical line for line to the output of section 11.1 from the module table to the last line (only the path on the first two lines differs): 162 modules, 7,844 assertions satisfied, 157 failed (expected 157), 10 refused (expected 10), 10 warnings, `srcrefs` 0 problems, 976 traces guarded and as expected.

## 12. Independent tests

Three independent test authors, `ind-a`, `ind-b` and `ind-c`, each decided a set of scenarios from the Law alone, before opening any module of the deposit, any fragment, `domain.l4` or the plan, and then wrote them as L4 tests.
Their frozen expectations are in `work/ind-a/expectations.md`, `work/ind-b/expectations.md` and `work/ind-c/expectations.md` of the fleet's working directory, with their own timestamps; their test modules are `ind-a-tests-*.l4`, `ind-b-tests-*.l4` and `ind-c-tests-*.l4` of this deposit.
They tested the groups as the encoders had deposited them: each author's snapshot holds `domain.l4`, the nine fragments and the 102 group modules, and no `int-` module.
They found defects, two groups were repaired on 2026-10-27 (G2 and G7, section 13), and the tests were merged into the row on the same day.

### 12.1 What was decided before the encoding was opened

| author | scenarios decided before opening the encoding | the author's own timestamps | articles |
| --- | --- | --- | --- |
| ind-a | 328 scenario lines (some lines carry two or three cases) | the expectations file was closed at 2026-10-26T16:12:13Z (UTC) "before any encoding file was opened" | 1 to 12 and commencement |
| ind-b | 405 rows, 14 ambiguous rows and 61 rows of a regulative catalogue (who must, may or shall not do what), "completed before opening the deposit: 2026-10-27"; the snapshot of the deposit it then worked against was taken at 2026-10-26T16:13:45Z | the file says "Written 2026-10-26/27" | 5 to 7, 13 to 25 and the vintages |
| ind-c | 405 rows | started 2026-10-26T16:06:43Z, finished 2026-10-26T16:12:11Z, "nothing in DEPOSIT, `phase1/` (other than the assignment) or `domain.l4` was opened or listed before this line"; a note was appended at 2026-10-26T16:46:23Z, after the encoding was opened, and changes nothing above it | 5 to 7, 26 to 43, the Schedules, the vintages |

The scenario counts are the fleet lead's, read from the authors' files; the integrator did not recount them.
Tests the authors wrote AFTER they opened the encoding are labelled post-hoc below (section 12.4) and are not independent evidence.

### 12.2 What passes, and what does not

Every topical module of each author passes on the repaired groups.
The assertions below are those of `check.sh`: satisfied, failed, refused (the last two only in the `ambiguous` and `disagree` files).

| author | topical modules (assertions satisfied) | satisfied | `disagree` file | `ambiguous` file |
| --- | --- | --- | --- | --- |
| ind-a | art1 32, art11-12 70, art2 115, art3-7 95, art8-10 125, commencement 28, readings 70 | 535 | 2 failed, 0 refused | 4 failed, 5 refused |
| ind-b | art13-14 126, art15-17 87, art18-20 141, art21-25 100, art5-7 134, commencement-vintages 51 | 639 | 0 failed, 1 refused | 2 failed, 0 refused |
| ind-c | art26-31 123, art32-36 65, art37-43 28, art5-7 110, commencement-vintages 125, sched1 91, sched2 53, traces 0 | 595 | none: its 5 assertions all hold since the repairs and were moved (section 12.3) | 8 failed, 4 refused |

Totals over the three authors: 1769 assertions satisfied in the topical modules; 16 failed and 10 refused in the `disagree` and `ambiguous` files (every one of them kept, counted and listed below).
The 59 traces of the authors (`ind-a` 26 and `ind-c` 33) are guarded by `-- EXPECT:` comments and all behave as expected (section 11.3).

### 12.3 Every assertion that did not pass, with its provision, classification and disposition

Classification as the assignment sets it: (i) now passes because of a repair and was moved out of the `disagree` file into a topical file as a regression test; (ii) still fails and the author believes the encoding is wrong, so it stays in the author's `disagree` file; (iii) the Law is ambiguous, so it stays in the author's `ambiguous` file.
Dispositions: repaired, fork kept, design, open.
The authors' wording is kept; the fleet lead's triage (`work/triage/FINDINGS.md`) is the source of the dispositions.

| id | author | provision | the author's finding (their words) | class | disposition |
| --- | --- | --- | --- | --- | --- |
| E6-2d4 | ind-b | 6(1)(i), src:176 | "recreational facilities open to the public at large WITHOUT the object of improving the conditions of life: not within (i). The only way to say 'recreational facilities' to this encoding is the head (i); it has no fact for the object of 6(1)(i)." | (i) | repaired (G2 R1, FRAGMENT-G2 section 11.2); moved to `ind-b-tests-art5-7.l4` |
| V-20 | ind-b | 5(1), src:145 | "a body that is not an 'entity' (no kind of Article 2(1); ...) cannot meet the charity test, whatever its purposes." | (i) | repaired (G2 R2, FRAGMENT-G2 section 11.2); moved to `ind-b-tests-art5-7.l4` |
| V-18 | ind-b | 21(5), and Articles 21 and 23 generally | "B (an NPO body corporate under Jersey law, within none of 2(1)(c)-(h)) on 2025-10-15 is not an 'entity' at all (...), so 21(5), which binds 'An entity that is not a registered charity and is neither a Jersey entity nor an excepted foreign charity', does not reach it." | (i) | repaired (G7 R2, FRAGMENT-G7 section 10); moved to `ind-b-tests-art21-25.l4` |
| D1 | ind-c (post-hoc) | Part 9, src:876-880, 917-918, 725 | "Part 9 was brought into force in three stages, not two ... The encoding itself puts the original 41 in Part 9 (...) and in stage 3, but computes a Part's stages from the PRESENT Articles only, so Part 9 has two stages and, on its own reading F7.9 A (...), is wholly in force from 1 May 2018." | (i) | repaired (G7 R1, FRAGMENT-G7 section 10); moved to `ind-c-tests-commencement-vintages.l4` |
| D2 | ind-c (post-hoc) | Sch 1 4(3), 7(1), 5(5), src:796, 203, 157 | "a member of the Commissioner's staff, exercising the Commissioner's function, is bound as the Commissioner is ... The encoding answers FALSE for `a member of the Commissioner's staff` (a domain.l4 constructor) in both places, so a staff determination that an entity benefiting one named person provides public benefit stands." | (i) | repaired as a fork (G2 R3, F2.13, default: staff are bound; FRAGMENT-G2 section 11.2; assumed, not ruled); moved to `ind-c-tests-art5-7.l4` |
| DIS-1 | ind-a | 11(4), src:878-879, R&O.17/2018 Art 1(a) | "Article 11 (Part 4) came into force on 1 May 2018. An application lodged on 30 April 2018 is not one the Commissioner must register under Article 11(4), however complete it is. G4's exported duty does not read the day: it answers 'must register'." | (ii) | design: no group gates itself on commencement (IP4), the six headlines do; confirmed by `int-tests-repairs.l4` R6 (headline (a) refuses on 30 April 2018: Article 8 was not in force) |
| DIS-2 | ind-a | 8(3)(j), src:234, 392-393 | "Which year is 'the most recent year' is not defined by the Law: the year of an annual return and its timing are left to an Order under Article 13(7) and (8). Expected: the encoding cannot answer ... so it should refuse. The encoding (F3.2 and F3.7 defaults) assumes the calendar year that ended last and answers." | (ii) | fork kept (F3.2, F3.7; the other readings are callable; IP33) |
| V-02 | ind-b | 1 ("Minister"), R&O.40/2019, endnote [1] | "on 21 November 2014 the Law is in force (C-02), and Article 1 says 'Minister' means the Chief Minister: R&O.40/2019 substitutes another office 'for Chief Minister', and endnote [1] lists no amendment of Article 1 before R&O.40/2019." (the assertion refuses) | (ii) | open: not repaired; no text before 1 January 2019 is among the sources and `domain.l4` has no as-enacted text; the derivation (reading B) is not built (triage ib-V02) |
| AMB-1 to AMB-4 | ind-a | 1 ("Minister", "Comptroller"), 2(1) before 1 January 2019, src:26, 12 | "on 2014-11-21 'Minister' means the Chief Minister, because R&O.40/2019 Sch 2 para 1(e) substitutes FOR the words 'Chief Minister' and the Table of Legislation History lists no earlier amendment. The encoding REFUSES (no consolidated text before 1 January 2019 is among the sources)." (four assertions: the Minister on 2014-11-21 and on 2018-05-01, the Comptroller on 2014-11-21, the kinds of entity on 2018-05-01) | (iii) | open (as V-02) |
| AMB-5, AMB-6 | ind-a | 2(1)(d), (c), (g), src:55-56, 62 | "a foundation is within (d) only ... an incorporated 1862 association is within (c) only. The encoding (F1.8 reading 'as written', taken) also puts it in (g)." | (iii) | fork kept (F1.8; triage ia-AMB5/6) |
| AMB-7 | ind-a | 8(3)(a)(ii), src:225 composed with 2(1)(g) | "the note of status of a registered foundation needs no Article 8(3)(a)(ii) details (...). Composed with G1's favoured reading the foundation is also (g), and G3 then requires (g) details for it." | (iii) | fork kept (F1.8 flows into G3; triage ia-AMB5/6/7) |
| AMB-8 | ind-a | 8(4)(a), src:240 | "a company's principal address is its registered office ... whatever the caller says about what its constitutional Law requires. The encoding (F3.9 reading A, taken) reads the requirement into 'company' too, so with the requirement given as FALSE it falls through to 8(4)(b) and (c)." | (iii) | fork kept (F3.9; triage ia-AMB8) |
| AMB-9 | ind-a | 7(3)(a), src:211 | "where the Commissioner presumed a charitable purpose to be for the public benefit (forbidden by 7(3)(a)), public benefit is not established: FALSE. The encoding (F2.10 reading A, taken) REFUSES: ..." | (iii) | fork kept (F2.10; triage ia-AMB9) |
| A-10 | ind-b | 21(3), 23(1) | "an unregistered Jersey entity that calls itself a 'Jersey charity' also refers to itself as a 'charity': contravenes 21(3) as well as 23(1). Reading B (the encoding's): only 23(1) is contravened, because 'Jersey charity' is the expression Article 23 regulates." | (iii) | fork kept (triage ib-A10) |
| A-14 | ind-b (post-hoc) | 7(1), 7(3)(b), src:203, 212 | "an entity that benefits only one named natural person does not provide public benefit, whoever determines the question. Reading B (the encoding's): Article 7(1) applies 7(3)(b) only to the Commissioner, the tribunal and the court, so a finding by anyone else stands." | (iii) | fork F2.13 now covers the Commissioner's staff (repaired); a finding by `any person` stays ambiguous |
| S1.1-13 | ind-c (pre-committed) | Sch 1 1(5), src:762 | "reading B (C-MONTH ROLLOVER): six years from 29 February 2024 run to 1 March 2030, so a term expiring on 1 March 2030 is not more than 6 years. The encoding offers no rollover reading of the 6 years." | (iii) | open: no alternative reading offered |
| S1.3-01, S2.2-01 | ind-c (pre-committed) | Sch 1 3(1)(a), Sch 2 2(1)(a), src:780, 826 | "(C-NOTICE, clear months): notice given 15 January 2026 for 15 April 2026 is too short ... No reading of F9.3 counts clear months." (and the same for one month) | (iii) | open: no alternative reading offered |
| V-08, S1.2-04b and the (ba), Comptroller rows | ind-c (the first pre-committed, the rest post-hoc) | 1, 2(1)(ba), Sch 1 2(4)(a) before 1 January 2019, src:931-943 | "Reading A: before 1 January 2019 the text of these definitions is known from the instruments that later changed them ... Reading B (the brief's rule, and the encoding's): no consolidated version before 1 January 2019 is among the sources, so the answer is a refusal. All four rows REFUSE." | (iii) | open (as V-02) |
| S1.3-11b | ind-c (post-hoc) | Sch 1 3(4)(c), src:792 | "service in whole-year stretches adds by calendar length ... The encoding (F9.6 A) counts the DAYS of 12 calendar years from the earliest first day of service, so where the stretches straddle a different number of 29 Februaries than the 12 years from that day, the expiry moves a day: 29 February 2028 (a day early) and 2 March 2027 (a day late)." (two assertions) | (iii) | open: no alternative reading offered |
| A7-01b | ind-c (post-hoc) | 7(1), 7(3)(b), src:203, 212 | "public benefit (Article 5(1)(b)) cannot be benefit to one identified natural person whoever asks the question; 7(3)(b) says what follows from the meaning of the public. Other reading (the encoding's): 7(3)(b) binds only the bodies 7(1) names, so another determiner's finding stands." | (iii) | ambiguity kept (as A-14; F2.13 covers staff only) |
| A31-01 | ind-c (pre-committed) | 29(1), 31(a), src:677 | "Reading B: a governor who passes information to the Commissioner so that the Commissioner can discharge a function is within 31(a), so no offence. Reading A (ind-c's default, and the encoding's): 31(a) needs a disclosure by or on behalf of the Commissioner, so without consent it is an offence. The encoding has no reading B." | (iii) | open: no alternative reading offered |
| A39-06 | ind-c (pre-committed) | 6(3), 6(4)(b), 39(2), src:200, 737 | "Reading B: 39(2) gives the power of 6(3) the power to make consequential amendments of other provisions, 6(5) included. Reading A (ind-c's default, and the encoding's): the specific limit of 6(4)(b) prevails. The encoding offers no reading B." | (iii) | open: no alternative reading offered |

In the `disagree` files the author's assertion was written unedited; the only edit to any assertion of the three authors for any reason other than an added argument is the one named in section 12.5 (E6-2d4).
The `ambiguous` files fail or refuse by design: each asserts the reading the author took, and the encoding takes the other (or offers none).
`check.sh` lists their counts: ind-a `ambiguous` 4 failed and 5 refused, ind-a `disagree` 2 failed, ind-b `ambiguous` 2 failed, ind-b `disagree` 1 refused, ind-c `ambiguous` 8 failed and 4 refused.

### 12.4 Tests written after the author opened the encoding (post-hoc: not independent evidence)

- **ind-a, `ind-a-tests-readings.l4`, all 70 assertions.**
  The file's own provenance note: "these expected values were decided at STEP 5, after the fork registers (FRAGMENT-G1 to G4) had been read and after a probe had re-run ind-a's scenarios under each reading."
  Each value is what the text gives when read the way the reading says; the file tests the other readings of the forks of Articles 1 to 12.
- **ind-b, row A-14** (one assertion, in `ind-b-tests-ambiguous.l4`): "added after opening"; the expectations file lists it under "Added AFTER opening the encoding (step 3), so not independent of it".
- **ind-c, 15 assertions labelled POST-HOC or POST-HOC-CERTAIN in the author's files:** the five "POST-HOC-CERTAIN rows" at the end of `ind-c-tests-commencement-vintages.l4` (instants and the 27 February 2024 rows); D1 (two assertions) and D2 (three), both now moved into topical files; in `ind-c-tests-ambiguous.l4` the (ba) and Comptroller rows of the vintages section (two), the twelve-years-in-aggregate rows (two) and A7-01b (one).
  The expectations file records that rows added later are tagged in the test modules and not in it.

### 12.5 Every fixture line the integrator touched

The authors' fixtures built the OLD G2 records (a nine-field `Facts about a purpose under Article 6`, a twelve-field `Interpretation of Articles 3 to 7`) and called G2 and G7 rules whose signatures then changed.
The integrator adapted them mechanically with one script (`adapt_ind.py`, in the integrator's working directory, not deposited), which makes these kinds of edit and no other; no expected value, polarity, `REFUSED`/`BECAUSE` text or assertion keyword was changed.
Line numbers are those of the author's file as snapshotted (`work/ind-X/snapshot/`).

- **F: the tenth field of the facts of Article 6(1)(i).**
  Every construction `Facts about a purpose under Article 6` WITH ... got the field `the facilities or activities have the object of improving the conditions of life for the persons for whom they are primarily intended` set to `JUST TRUE`; the field is read only for a purpose under head (i).
  The task said "NOTHING / the default reading"; the integrator chose `JUST TRUE` because the authors' frozen rows for every recreational purpose that is meant to be charitable state the object (ind-a S6.1-09 and S6.2d-02: "object of improving conditions of life" and "with the object of improving conditions of life"; ind-b E6-2d1 to E6-2d3: "with the object of improving conditions of life", and E6-i: "assumed in the head"; ind-c A6-22 to A6-24: "object of improving conditions of life") or give a positive expectation for head (i) that presupposes it (ind-a S6.2d-03, "primarily for disabled persons -> (i)"), and the rows that are meant NOT to be charitable fail 6(2)(d) whatever the object is.
  With `NOTHING`, as the task literally said, the repaired encoding refuses by name (the signal G2 intends for a missing field) for ten assertions: nine that hold with the object stated (ind-a-tests-art3-7 3, ind-b-tests-art5-7 3, ind-c-tests-art5-7 3) and E6-2d4, whose row says the object is absent; the integrator ran that variant first and kept its output (`out/run-ind-adapted.txt` in the working directory).
  Lines: ind-a-tests-art3-7: 26, 40; ind-a-tests-readings: 52, 151, 152 (two of them inside `#ASSERT` lines); ind-b-tests-fixtures-g2: 26, 205, 220, 237, 249; ind-b-tests-art5-7: 244, 245 (inside `#ASSERT` lines); ind-c-tests-art5-7: 28.
- **I: the thirteenth field of the interpretation.**
  Each positional `Interpretation of Articles 3 to 7` OF twelve values got a thirteenth, `F2.13 A`, the default reading.
  Lines: ind-a-tests-readings: 112, 113; ind-b-tests-art5-7: 241, 242 (all in `#ASSERT` lines).
- **A: the new last input `interp` of nine G2 exports and rules.**
  A call of `Art 7 the determination complies with the duties on its maker`, `Art 5(5) the person must have regard to the guidance`, `Art 7(1) Articles 7(2) and 7(3) apply to the person`, `Art 7(3) the determination is permitted`, `Art 7(3)(a) ...` or `Art 7(3)(b) ...` got ` `the favoured interpretation of Articles 3 to 7` ` as its last input.
  Lines (all calls inside `#ASSERT` or `#TRACE` lines): ind-a-tests-art3-7: 187, 189, 190, 191, 192, 194, 286, 287, 288, 289, 290, 292, 294, 295, 297; ind-b-tests-art5-7: 62, 63, 65, 66, 67, 68, 69, 70, 201, 202, 203, 205, 206, 234, 235, 236; ind-c-tests-art5-7: 251, 252, 253, 254, 255, 256, 257, 359, 360, 366, 367, 368, 369, 370; ind-c-tests-traces: 88, 93; ind-c-tests-disagree (before its move): 42, 44.
- **E: the new first input `the entity` of four G7 exports.**
  A call of `Art 21(1) the statement contravenes paragraph (1)` or `Art 21(2) the statement contravenes paragraph (2)` got the entity ` `ind-b7 a Jersey company` ` first (the entity the sibling assertions of the same rows use).
  Lines of ind-b-tests-art21-25: 16, 24, 26, 28, 32, 34, 36, 38, 98.
- **M: imports.** `IMPORT `g2-readings`` was added to ind-c-tests-traces (the favoured interpretation of Articles 3 to 7 is defined there), and the imports a moved block needs were added to ind-b-tests-art5-7, ind-b-tests-art21-25, ind-c-tests-art5-7 and ind-c-tests-commencement-vintages.
- **X: the one assertion line whose fixture reference changed beyond an added argument.**
  E6-2d4 (ind-b-tests-disagree, line 24 of the snapshot): the assertion line named `ind-b recreation facts` NOTHING (JUST TRUE), a fixture that, after F, states the object true, while the row is "WITHOUT the object".
  The line now names `ind-b recreation facts without the object` NOTHING (JUST TRUE), a new fixture appended to ind-b-tests-fixtures-g2 that is the same record with the object `JUST FALSE`; the original line is kept above it as a comment (`-- AS AUTHORED ...`).
  The polarity (NOT), the provision and the expected value are the author's.
- **V: moves.** E6-2d4 and V-20 were moved from ind-b-tests-disagree to ind-b-tests-art5-7, V-18 to ind-b-tests-art21-25, ind-c D1 to ind-c-tests-commencement-vintages and ind-c D2 (with its two fixture definitions) to ind-c-tests-art5-7, verbatim with their comments, under a heading that says where they came from.
  `ind-c-tests-disagree.l4` is empty after the moves and is not carried into the deposit; its original count was 5.
  The header comments of the other `disagree` files still state the authors' original counts; `check.sh` holds the current ones.

### 12.5a The second adaptation, for fork F2.14 (2026-10-27)

G2 then added an eleventh field to `Facts about a purpose under Article 6` and a fourteenth to `Interpretation of Articles 3 to 7` (fork F2.14, Article 6(2)(e); section 3.7), and the fixtures were adapted again by the same script, extended with two kinds of edit and no other.
Nothing in section 12.5 above was undone, and no expected value, polarity, `REFUSED`/`BECAUSE` text or assertion keyword was changed.
Line numbers in this section are those of the files as deposited, after both adaptations, because the first kind inserts lines.

- **G: the eleventh field of the facts of Article 6.**
  Every construction `Facts about a purpose under Article 6` WITH ... got a line `the purpose is the provision of accommodation or care` IS FALSE, and the one-line constructions inside `#ASSERT` lines got the same field in the same position.
  FALSE and not TRUE because the field is a plain BOOLEAN whose declared default is FALSE (`g2-nouns.l4`), and because G2 states that reading B of F2.14 is reading A or this field: with the field FALSE the two readings agree on every input, so the adaptation cannot change an answer under either reading.
  The authors' frozen rows on Article 6(2)(e) (ind-a S6.1-14, ind-b E6-2e, ind-c A6-27) are each "relief of elderly people in need" by providing accommodation or care, so they state the need element and none states the provision of accommodation or care without it; the need-qualified field (the seventh) is left as each author wrote it.
  Lines inserted: ind-a-tests-art3-7: 28, 44; ind-a-tests-readings: 54; ind-b-tests-fixtures-g2: 28, 209, 226, 245, 259, 279; ind-c-tests-art5-7: 30.
  Lines edited in place (the field appended inside an `#ASSERT` line): ind-a-tests-readings: 153, 154; ind-b-tests-art5-7: 244, 245.
- **I: the fourteenth field of the interpretation.**
  Each positional `Interpretation of Articles 3 to 7` OF thirteen values got a fourteenth, `F2.14 A`, the default reading.
  Lines: ind-a-tests-readings: 114, 115; ind-b-tests-art5-7: 241, 242 (all in `#ASSERT` lines).
- **What the adaptation did to the results.**
  Every independent module has the same errors, satisfied, failed and refused counts after the second adaptation as before it, and in the five modules that are not wholly green (the `ambiguous` and `disagree` files) the status of each of their 26 assertions is the same line for line (16 failed and 10 refused, both before and after).
  No independent assertion changed its result because of F2.14.
  ind-a S6.1-14, a care home for elderly people in need (`ind-a-tests-art3-7.l4`), sets the need-qualified field TRUE and holds; with the new field FALSE it cannot differ between the two readings of F2.14.

### 12.6 What the merge shows

The independent tests found five defects that the groups' own tests had missed (the object of Article 6(1)(i), the charity test for a non-entity, Articles 21 and 23 for a non-entity, Part 9 and the original Article 41, and staff exercising the Commissioner's function), all now repaired, and a sixth point (the text before 1 January 2019) that the fleet lead left open.
They also confirmed, by the topical modules, that the rest of the encoding answers as three authors working from the Law alone expected, on 1769 assertions, apart from the ambiguities listed above.
Which of those assertions were decided before the encoding was opened is stated in section 12.1; the post-hoc ones (section 12.4) are 80 of them (70 of ind-a, 10 of ind-c, the last including the five moved from `ind-c-tests-disagree.l4`) and are not independent evidence.

## 13. Defects found in group modules

The integrator did not edit any group module, test or fragment.
Each item below was found while wiring or testing the integration layer, is reported here and in the integrator's final report, and has not been repaired.
The items marked "seam" are failures of two modules to agree and are held as failing assertions in `int-tests-red.l4` (section 11.4).

| id | where | what | evidence | effect |
| --- | --- | --- | --- | --- |
| X1 | G5 `g5-art14-court-powers.l4` | `Art 14(1) the powers of the court are exercisable on the application` (a BOOLEAN with its own `@export`) takes no input for whether anyone is acting as the Commissioner (IP28), while the regulative rule `Art 14(1) the court may exercise the powers on the application` takes it | the signatures at lines 89 and 133 of the module | a caller who uses the BOOLEAN alone gets an answer that ignores a vacancy in the office of Commissioner; headline (c) conjoins IP28 itself (mutation M04 shows the test notices) |
| X2 | seam: G6, G7, G8, G9 and `domain.l4` (IP35) | on the days unit G6, G7 and G8 take "2 years" as 730 days and G9's cap converts the stored 24 months to days from the start day (731 from 2 October 2026) and compares with 730; `Penalty provided` stores months only | `int-tests-red.l4` seam 1: four failing assertions, four controls passing | the penalty three groups call the maximum is over the cap of the same "2 years" on the days reading; no effect on the default (calendar months) |
| X3 | seam: G5, G4, G3 (IP29) | G5's `Art 13(9) an Order under Article 13(9) applies to the registered charity` is one fact for three limbs; G4 needs limb (b) and G3 limb (c) | `int-tests-red.l4` seam 2 (one failing assertion); `int-tests-application.l4` A13, A14 | wired from the composite, an application with an Order of limb (a) alone and no draft statement would be reported as incomplete; the integration layer wires limb-specific facts and keeps the composite as the alternative |
| X4 | seam: G1 against G4 and G8 | "a registered charity": G1 needs an entity within Article 2(1) as well as the standing; G4 (12(7)) and G8 (26(2)) read the standing alone | `int-tests-red.l4` seam 3 (one failing assertion, one control passing) | a body that the register records in the general section but the text in force makes no entity (an NPO body corporate in the text of 12 April 2023) is a registered charity to G8 and not to G1; headline functions pass G1's answer |
| X5 | G4 `g4-art11-decision.l4`, `g4-nouns.l4` | the compliance test of Article 11(4) needs the field `procedure under Regulations under Article 11(3)(b) followed` to be TRUE, and no Regulations are among the sources | line 165 of the module; the integrator's fixtures set it TRUE | a caller who leaves it FALSE gets "no duty to register or to refuse arises because the application does not comply" with no hint of why; a trap, not an error of reading |
| X6 | `domain.l4` with G3, G6, G8 | the constructor `the registered charity` of `Recipient of a required steps notice` has the name of the standard `GIVEN` of IP7, `the registered charity` : `Registered charity` | `domain.l4` line 184; G3 `g3-nouns.l4` line 138; G8's nouns request 1 | in a module that declares the `GIVEN` the parameter hides the constructor; the integrator's modules name the parameters otherwise |
| X7 | G7, G8 (a test fixture), G9 | three modules export the same name, `the favoured interpretation`, for three different types | `g7-interpretation.l4` line 94, `g8-tests-fixtures.l4` line 13, `g9-interpretation.l4` line 149 | a module that imports two of them needs a typed constant to choose (the integrator's tests do this) |
| X8 | `domain.l4` (G1 nouns request 5, G8 nouns request 2) | record fields whose names begin with "is" or "has" (`is a natural person`, `is a Jersey entity`, `has been complied with` and others) against the repository's naming ruling | the groups' own nouns requests | none on any answer; `domain.l4` is read-only to the integrator |

The groups' own red files (`g2-tests-red.l4` to `g9-tests-red.l4`, 134 failing assertions by design) hold the expectations their authors say the readings taken do not meet.
The integrator ran them and recorded their counts in `check.sh`; it did not review them one by one.

### 13.1 Repaired

| id | found by | where | what | repair | date, and where it is recorded |
| --- | --- | --- | --- | --- | --- |
| X9 | the integrator (`check-traces.py`) | integrator, `int-h-contravention.l4` | the first version of `Int (c) the governor must report the reportable matter` took a `Governor` record and its two traces passed for the wrong reason: the record built by hand had no reportable matters, so the duty did not bind | the function takes the governor's name and finds the matters itself (IP21) | 2026-10-27, first pass; section 11.3 |
| ic-D1 | ind-c | G7 | Part 9 omitted the original Article 41 (stage 3, 1 January 2019), so on reading A of F7.9 Part 9 was in force from 1 May 2018 | a Part's stages now come from every Article it held | 2026-10-27, FRAGMENT-G7 section 10 (R1) |
| ic-D2, ib-A14 | ind-c, ind-b | G2 | staff exercising the Commissioner's function under Schedule 1 4(3) were not bound by Articles 7(3)(b) and 5(5) | fork F2.13, default: staff are bound (assumed, not ruled) | 2026-10-27, FRAGMENT-G2 sections 11.1 and 11.2 (R3) |
| ib-E6-2d4 | ind-b | G2 | the object of Article 6(1)(i) had no fact | a tenth field of the facts (the object, a MAYBE BOOLEAN, default NOTHING); a purpose of head (i) needs it | 2026-10-27, FRAGMENT-G2 section 11.2 (R1) |
| ib-V20 | ind-b | G2 | a non-entity (no kind of Article 2(1)) met the charity test | `Art 5` and `Art 5(3)` answer FALSE for it | 2026-10-27, FRAGMENT-G2 section 11.2 (R2) |
| ib-V18 | ind-b | G7 | Articles 21 and 23 applied to a body that is not an entity | a guard `the body is an entity within Article 2(1)` on each binding predicate | 2026-10-27, FRAGMENT-G7 section 10 (R2) |

### 13.2 Found by the independent testing and not repaired

- **The text of "Minister", "Comptroller" and the kinds of entity before 1 January 2019** (ind-a AMB-1 to AMB-4, ind-b V-02, ind-c V-08 and the (ba) and Comptroller rows): the authors expect an answer derived by reversing the amendments the endnotes list; the encoding refuses.
  The fleet lead's triage left it unrepaired because the `domain.l4` vintage enumeration has no as-enacted text and the sources hold none; the repository's owner ruled on 2026-10-27 that the refusal stands (section 8.7).
- **G4's duty ignores the day** (ind-a DIS-1): by design (IP4); the headline gate answers (`int-tests-repairs.l4`, R6).
- **"The most recent year" answered with the calendar year** (ind-a DIS-2) and the other ambiguities of the authors: forks kept (section 12.3).

### 13.3 Notes from the repairs

- G2's repair left four rules unguarded for a non-entity on purpose (`Art 5(1)(a)`, `Art 5(1)(b)`, `Art 7 the entity provides public benefit` and `Art 6 ... advancement of religion`), with its reasons in FRAGMENT-G2 section 11.2 (`Art 5(2) the bar applies to the entity` takes the constitution facts, not the entity); the headlines reach only the guarded `Art 5` and `Art 5(3)`.
- A caller that does not fill the new tenth field gets a named refusal for a purpose of head (i); that is the intended signal (FRAGMENT-G2 section 11.2).
- G7's type `Treatment of a Part brought into force in two stages` and its two values keep their names although Part 9 now has three stages (FRAGMENT-G7 section 10).

## 14. What is not wired, and what is not done

- **IP13 is stated, not computed.**
  A breach that a `#TRACE` of a regulative rule shows is passed to headline (c) by naming the rule (`a duty or prohibition was breached, as a trace of the rule shows`), because L4 cannot evaluate a regulative rule inside a function.
  The contraventions that are values (a name that is not permitted, a governor in breach of 19(2) or 19(4), acting after reporting, contravening a disqualification order) are decided by the group that owns the provision.
- **IP28 is applied to the court's power on the Commissioner's application and returned as a field of headline (c); it is not applied to the Commissioner's other powers** (deregistering under 16(1), serving a notice under 27(2)), because the groups' rules for those do not take it.
- **The second limb of Article 11(4)(a), "or will do so on registration",** is a finding supplied to group G4, and is not wired from group G2.
- **Only the six headlines are gated by commencement and by the text of the Law.**
  A caller who calls a group's function directly bypasses the gate, as the groups' own tests do.
  Articles 3 and 4 (the Commissioner's establishment, functions and powers), Article 5(4) to (8) (guidance), Articles 23 to 25, 30, 31, 34, 35, 39 to 43 and the Schedules are encoded by the groups and exported where they decide something, but no headline reaches them; they are used by the headlines only through the facts they produce.
- **The fork alternatives are reached through `Readings of the fleet`.**
  The functions that replace one reading of the fleet (`Int fx the readings with the reading of ...`) are in `int-tests-fixtures.l4`, a test module, and the generated replace-one-field functions of the case records are there too; a user of the headlines who wants another reading imports that module or writes the record in full (records have no update operator).
- **The `@export` functions were not exercised through `l4 export` or the service.**
  The integrator checked that every `GIVEN` of every `@export` has a `@desc` (13 exports) and that every module runs without a warning; it did not build a service from them.
- **No domain expert has read anything.**
  No claim in this file or in `README.md` is that the encoding is correct, only that its modules run, that its tests pass, and that the readings are the ones the groups say they took.
- **The newest text of the Law is of 2 October 2026.**
  A later amendment is not encoded; neither are the subordinate instruments (section 1).
- **The four G2 rules left unguarded for a non-entity** (section 13.3) are not guarded by the integration layer either; headline (a) reaches only the guarded `Art 5` and `Art 5(3)`.
- **F2.13 is not wired from Schedule 1 paragraph 4(3).**
  `who` (the Commissioner's staff, or any person) is the caller's fact (section 6.13), and no other group's rule that attaches a duty to the Commissioner (for example Article 27(1)(b)) takes the fork.
- **The new tenth field of the facts of Article 6(1)(i)** comes from the caller inside `Purpose with the facts Article 6 reads`, with the default NOTHING; headline (a) does not derive it.
- **The new eleventh field of the facts of Article 6** (`the purpose is the provision of accommodation or care`, fork F2.14) likewise comes from the caller inside `Purpose with the facts Article 6 reads`, with the default FALSE; headline (a) does not derive it, and F2.14 is not wired from any other group.
- **The text before 1 January 2019** is not reconstructed from the amending instruments (section 13.2).

## 15. Provenance of this run

Written by the launching session (IL-hvac, running Claude Sonnet 5.5) on 2026-10-27, after the integrator's second pass.
Everything below is a record of what was done and how it was measured; none of it is a claim that the encoding is right.

### 15.1 Who asked for it, and the hold on it

The task is the trigger word ALMSHOUSE in the general manager's table: encode the whole Charities (Jersey) Law 2014 afresh as the row `legalese-full-2026-10` by the recipe used for the HVAC whole-Law row, with a register of the places where the Law reads two ways, and compare it with the July corpus and with the Articles 5 to 7 cleanroom.
It was fired on 2026-10-14 (04:32Z) and fired again by Meng on 2026-10-26 (about 14:40Z, "Let's just fire ALMSHOUSE now."), which is the run recorded here.
Meng's instruction reached this session through the general manager, not directly.
The conditions of the task were that the row be committed to a local branch of a commons worktree only, with no push to the shared repository, no email and no publication.
Whether and when the row is pushed is for the repository's owner to decide.
On 2026-10-27 the owner had it pushed to `main` (Meng, through the general manager: "go ahead and push the charities encoding to public commons.").

### 15.2 What happened, and when

- **2026-10-14, first attempt.** The Law was fetched and hashed, the two skills were copied and cleaned (15.4), a blind contradiction hunt and a survey were run, and nine encoders were launched at about 05:50Z.
  All nine failed at launch with "You've hit your weekly limit" before writing anything, so nothing from that launch is in the row except the survey, the hunt and the cleaned skills.
- **2026-10-26, second attempt.** The compiler was refreshed (15.5), the Law was fetched again and found unchanged (15.3), and the nine encoders were relaunched at 14:25Z.
  They reported between 15:33Z and 15:56Z, and each was re-run by the launching session in a clean copy with matching figures.
  Three independent test authors were launched at about 15:58Z and reported between 16:48Z and 16:52Z.
  The integrator worked from about 15:59Z to 17:53Z.
  The launching session triaged every finding (section 15.8), and two encoders (G2 and G7) were sent repairs, which they reported at 18:10Z and 18:37Z.
  The overlap reader reported at 18:25Z, the comparer at 19:13Z, and the integrator's second pass (rewiring, merging the independent tests) at 19:14Z.
  The launching session re-ran the final `check.sh` in a clean copy; section 11.1 gives its output and section 15.9 says what it showed.
- **2026-10-27, after the push.** Fork F2.14 was added and a few lines were corrected; section 15.13 says what changed.

### 15.3 The source

The Law's text is the page https://www.jerseylaw.je/laws/current/l_41_2014 "Showing the law from 02 Oct 2026 to Current", with the official PDF text layer and the eight amending instruments listed in `source/`.
The page was fetched on 2026-10-14 (HTTP 200, 527,245 bytes, sha256 1634539a20330776eb2aa614b9d0801285e15985fb040b56bc41c8ddfb3df13a) and again on 2026-10-26 (HTTP 200, 527,254 bytes, sha256 fa9047d8acb3d8abb48b7fc1a75e06f6713fb2e50d164c5ad869dc864a7b58fe).
The HTML differs between the two fetches only in page boilerplate (stylesheet identifiers and script tokens); the paragraph text extracted by the same script is byte-identical, 943 lines.
The page lists nine point-in-time versions; the newest is the one of 2 October 2026, on both days.
The licence is the Open States Assembly Licence – Jersey v1.0 and its attribution is a condition (see `SOURCE-LICENSE.md`).

### 15.4 What the fleet was and was not allowed to read (the cleanroom)

The fleet was briefed not to read the July corpus (`paper/case-studies/charities-jersey-2014` in the l4-ide repository), the Articles 5 to 7 cleanroom row, or any other encoding of this Law, and to read only `doc/reference/` and `doc/concepts/` of the l4-ide documentation.
The two published skills could not be given as they stand, because they quote and model the cleanroom row's Articles 1, 6 and 7 (including its ambiguity identifiers A1 and A3 and its `PublicBenefitFinding`), and the tutorials and courses teach from this Law.
A clean copy of the two skills was made: 12 sections were rewritten by a Sonnet 5.5 agent with invented analogues (a Harbour Safety Act 2011 and a Library Lending Act 2016), checked by the launching session with a search and a diff for any remaining identifying text.
What remains, and is disclosed here:
(1) two of the invented ambiguities, H1 and H3 in the rewritten skills, mirror the shapes of Article 6(2)(c) and Article 6(1)(p) of this Law, so the encoders of Group 2 may have been steered towards those questions;
(2) other entries of the skill still cite example paths for Singapore and United States encodings, which are not Jersey and which the brief forbade the encoders to open;
(3) the cost of the rewriting agent counts toward the row (section 15.10).
The launching session read the July corpus and the cleanroom only after the encoders, the test authors and the integrator had finished, for the comparison (`COMPARISON.md`).
The encoders, the test authors, the integrator and the overlap reader were under the same brief.
The launching session searched the sub-agents' recorded tool calls for the names of the forbidden sources (the cleanroom, the case-study directory, `jl4/examples`, `doc/courses`, `doc/tutorials`, the third-party wiki): seven agents had a call that mentions one, and in every case the call was the agent writing a sentence of its own (a "peeked: nothing" statement, a fragment, a script) or grepping the brief's own rule; none was a read, glob or search of a forbidden path.
The search is crude: it matches the text of the arguments, and it cannot see anything an agent was told by a peer or recalled from training.

### 15.5 The compiler

The fleet used the prerelease `unstable-20261026-6325439` for macOS arm64 from `legalese/prereleases` (tarball sha256 `de01e0ae10771faa0d3dd2529d513bfe229a1ed3d6b274739dccd9709cb8d598`, matched against the release's `SHA256SUMS`; the binary's sha256 is `18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475`).
It is an ancestor of `origin/unstable` at `65adfc2de` and no file under `jl4-core`, `jl4/app` or `l4-cli` differs between the two.
The survey and the hunt of 2026-10-14 used an earlier snapshot (store build `jl4-0.1-dca2f841`, sha256 `75625e2ec214d6c4585925b32f0f877e856476c987e59749eca4efb56f445cc3`); `domain.l4` and the R4 pattern file check clean on both with identical output.
Every module of the row was run only with the first binary named.

### 15.6 Models, effort, and who did what

| role | model | notes |
| --- | --- | --- |
| launching session (briefs, triage, verification, this section) | Claude Sonnet 5.5 | also did unrelated work in the same session |
| skill rewriter, surveyor | Claude Sonnet 5.5 | 2026-10-14; the surveyor was launched at high effort |
| contradiction hunter | Claude Opus 5.5 | 2026-10-14; blind; high effort |
| nine group encoders G1 to G9 | Claude Sonnet 5.5 | launched 2026-10-14 (failed at launch) and 2026-10-26 (the run recorded here, no effort setting, so the session default) |
| integrator (two passes), overlap reader, comparer | Claude Sonnet 5.5 | 2026-10-26 and 27 |
| independent test authors ind-a, ind-b, ind-c | Claude Opus 5.5 | 2026-10-26 |
Opus 5.5 was used for the two roles the recipe names (the contradiction hunt and the independent test authors) so that they would make different mistakes from the Sonnet encoders; Meng had ruled the same for the HVAC row.
The 2026-10-14 survey and hunt ran at high effort and the 2026-10-26 agents at the default, so this row is not effort-comparable with the HVAC row.

### 15.7 What the survey and the hunt found, and how they overlap

- The survey (`survey/PLAN.md`, 2,233 lines) wrote a coverage table of 851 provisions (745 encoded, 82 inert, 23 out of scope, 1 refused at survey time), 35 integration points, 48 periods, 96 defined terms, 30 first-read traps and 68 candidate forks.
  After encoding, the coverage is 755 encoded, 80 inert, 2 refused and 14 out of scope (17 dispositions changed; `coverage-all.tsv`).
- The blind hunt (`hunt/CONTRADICTIONS.md`) found 55 contradictions, gaps and slips: 8 that block a decision, 40 that change an outcome, 7 cosmetic; 387 quotations in it were verified by script against the Law's text.
- `OVERLAP.md` compares the hunt, the survey's 30 traps and the 118 contradiction items the encoders recorded. Strictly counted, of the hunt's 55 findings 20 were found by both the survey and an encoder, 1 by the survey only, 7 by an encoder only, 8 in part only, and 19 by neither; of the 8 findings that block a decision, H1 to H4 were found by both lists and H5 to H8 by neither. Eight matches cover only one limb of a bundled finding; demoting them changes "both" from 20 to 14.
  The matching of one item to another is the overlap reader's judgement, and it is the least certain part of that file.

### 15.8 The independent tests, the findings, and the repairs

Three Opus authors decided their scenarios from the Law alone and froze them before opening the encoding (section 12.1 gives the timestamps, and `INDEPENDENT-ind-a-expectations.md`, `-b-` and `-c-` are their frozen expectation files).
Across the three, the pre-committed scenarios passed on the groups as deposited except for the disagreements in section 12.3.
The launching session read each disagreement against the Law's text (`TRIAGE.md`) and sent repairs only where the text settled the question: G2 (the object of improving the conditions of life in Article 6(1)(i); a body that is not an entity cannot meet the charity test; the Commissioner's staff acting under Schedule 1 paragraph 4(3) are bound as the Commissioner is, kept as fork F2.13 with the old behaviour callable) and G7 (the original Article 41 in Part 9's commencement stages; an "is an entity" check in Articles 21 and 23).
Two things were not repaired, by decision of the launching session ("assumed, not ruled"): the refusal for every day before the first consolidated text of 1 January 2019 (two authors expected "Chief Minister" and similar answers by reversing the amendments listed in the endnotes; the encoding refuses because no text before 2019 is among the sources), and the readings the authors called ambiguous, which are kept as forks.
Each repair is a separate change recorded in the group's fragment (section "Changes after independent testing"), so any of them can be reverted alone.
On 2026-10-27 the repository's owner ruled that the refusal before 1 January 2019 stands (section 8.7); the ambiguous readings remain forks.

### 15.9 What was run, and what it shows

The integrator ran `check.sh` in the deposit and in a clean copy; section 11.1 gives its output.
The launching session ran it again in a clean copy of its own (copy of the deposit, with `inputs` and `bin` beside it).
It was green with exit 0 (this is the run of 2026-10-26/27 before fork F2.14; section 15.13 gives the run after it): 162 modules; 7,787 assertions satisfied; 156 failed, equal to the 156 expected; 10 refused, equal to the 10 expected, with 10 warnings that are exactly those refusals; 1,724 quotation lines (887 runs, 1,666 locators) with 0 problems; 976 guarded traces, all as expected; and the hashes of the binary and of `domain.l4` matched their pins. These are the same totals as the integrator's.
The row was then copied into the commons worktree and `check.sh` was run from there, where it finds the Law's text in `../../source/` (the only change to `check.sh` for the commons layout); that run's totals are recorded in the commit message.
Each group's check was also re-run by the launching session in a clean copy with `tools/verify.sh`, and the figures matched each encoder's report, for G1 to G9 before the repairs and for G2 and G7 after.
A green `check.sh` shows that the modules run without a warning, that the stated tests hold, that every quotation and locator matches the Law's text, that every guarded trace behaves as its `EXPECT` comment says, and that the hashes match.
It does not show that any reading is the right one, and no domain expert has read the encoding against the Law.

### 15.10 Cost

Billing for the run was by subscription; the figures below are the tokens recorded in the sub-agent transcripts, priced at the published API list rates of 2026-10-27 (https://platform.claude.com/docs/en/about-claude/pricing, Sonnet 5.5 at $2 input, $2.50 five-minute cache write, $4 one-hour cache write, $0.10 cache read, $10 output per million tokens; Opus 5.5 at $4, $5, $8, $0.20, $20), by `tools/cost.py` with `tools/RATES-2026-10-27.json`.
Fleet sub-agents at those rates: **$257.71** in all, of which Sonnet 5.5 $195.32 (2,493 requests) and Opus 5.5 $62.39 (375 requests).
By role: the nine group encoders $134.39 (their repairs and the nine launches of 2026-10-14 that failed at launch, about $1.4 in all, are included); the three independent test authors $57.08; the integrator, two passes, $34.25; the comparer $13.36; the surveyor $6.89; the contradiction hunter $5.31; the overlap reader $4.45; the skill rewriter $1.98.
Tokens recorded: Sonnet 1,307.8 million cache reads, 14.2 million one-hour and 1.75 million five-minute cache writes, 0.35 million output tokens; Opus 184.7 million cache reads, 2.58 million one-hour and 0.54 million five-minute cache writes, 0.10 million output tokens.
Cache reads are $167.72 of the $257.71 (65%) and output tokens $5.61, so the list figure tracks how long the agents ran and how much context they carried, not the size of the Law.
The figure is a valuation, not a measure of what the subscription was charged or of the share of a weekly allowance used; the latter was not measured.
It counts the sub-agents only: the launching session's own tokens, which also covered unrelated work, are not included.
These are the figures at the time of the first commit; section 15.13 gives the total after fork F2.14.

### 15.11 Not done

- No domain expert (a Jersey charity lawyer, or anyone who knows the Commissioner's practice) has read any module.
- The subordinate legislation made under the Law (R&O.19/2018, R&O.59/2018, R&O.60/2018) is not encoded.
- The text before 1 January 2019 is not reconstructed.
- The row has been on `main` of the commons since 2026-10-27 (section 15.1).
  The launching session has sent no message about it to anyone outside the session group; what the general manager or the owner has sent is not recorded here.
- The `@nlg` natural-language generation, projections to other formats, and a web wizard were not made; the cleanroom has a DMN projection and golden files and this row has neither (`COMPARISON.md` section 8).

### 15.12 The record of the run

- `NOTES.md` (this file), `README.md`, `coverage-all.tsv`, `encoding.json`, `SOURCE-LICENSE.md`.
- `survey/PLAN.md`, `survey/coverage.tsv`, `hunt/CONTRADICTIONS.md`.
- `OVERLAP.md`, `COMPARISON.md`, `TRIAGE.md`.
- `INDEPENDENT-ind-a-expectations.md`, `INDEPENDENT-ind-b-expectations.md`, `INDEPENDENT-ind-c-expectations.md`.
- `provenance/BRIEF.md` and `provenance/ASSIGN-*.md`: the brief and every assignment the agents were given, as sent.
- `tools/`: the scripts used (`verify.sh`, `cost.py`, the rate card, `extract_law.py`).

### 15.13 Later changes (2026-10-27, after the push)

The row was on `main` at 27c1db980 when these changes were made; they are one commit on top of it.

- **Fork F2.14, Article 6(2)(e).**
  A comparison with the Articles 5 to 7 cleanroom (its ambiguity A2) raised the question whether Article 6(2)(e) adds an operand to head (n) or only says that relief of those in need can be given by accommodation or care.
  The comparison first said that this row widened head (n); that was wrong, because the only operand of `Art 6(2)(e)` was a fact that already names the need, so the code was declaratory in substance and could not express the other reading.
  G2 registered the question as fork F2.14 (14 forks in G2, 137 in all), with reading A (declaratory) as the default and reading B (widening) callable, tested and with its own red assertion (sections 3.7 and 8.2; `FRAGMENT-G2.md`, fork F2.14 and section 11.5).
  The owner ruled the default on 2026-10-27 ("default ruled by the owner (Meng), 2026-10-27"; his words are in section 8.2 and the fragment, with the middle of the quotation elided).
  The integrator rewired the integration layer and adapted the independent authors' fixtures mechanically (section 12.5a); no independent assertion changed its result.
  The comparer corrected `COMPARISON.md` (sections 4.2 and 5, rows Q3 and D10) and recounted the agreement with the cleanroom's 25 worlds: it is unchanged, 192 of 200 (96.0%) under the favoured readings and 199 of 200 with F2.1 and F2.10 read as their second readings, and reading B of F2.14 changes none of the 200 because none of the cleanroom's worlds sets an accommodation-or-care fact.
- **The totals after F2.14**, from `check.sh` run in the commons layout from the row directory on the day of the commit: 162 modules; 7,844 assertions satisfied (group modules 5,471; integration 604; independent 1,769); 157 failed on purpose, equal to the 157 expected; 10 refused on purpose, equal to the 10 expected; 1,727 quotation lines, 889 runs and 1,668 locators with 0 problems; 976 guarded traces, all as expected.
  G2 now holds 409 satisfied assertions (it held 370) and 16 declared red (it held 15).
- **Lines corrected in the same commit.**
  Section 15.11 said nothing had been pushed; the row is on `main` (section 15.1).
  The `encodings_note` of `subject.json` and the header of `FRAGMENT-G4.md` said the same, and now say when they were true.
  The fork index in section 5 had an empty question cell for every G7 fork, because the generator did not read G7's bare fork headings; the cells are filled and the generator now stops on an empty cell (section 5).
  Section 7, row S18, and `FRAGMENT-G1.md` C2 called "clauses (i) to (v)" in Article 2(10)(b)(vi) a slip; the Law has no other name for that level (it says "sub-paragraphs" for the lettered level), so it is recorded as an observation and not as a slip.
  The totals quoted in sections 15.2 and 15.9 are those of the first run and are marked as such.
- **Cost of this round**, same method and rates as section 15.10: the fleet sub-agents now total **$279.00** (Sonnet 5.5 $216.61 over 2,705 requests, Opus 5.5 $62.39 over 375 requests), which is $21.29 more than the $257.71 of section 15.10: the G2 encoder about $4.22, the integrator $8.29 and the comparer $8.78.
