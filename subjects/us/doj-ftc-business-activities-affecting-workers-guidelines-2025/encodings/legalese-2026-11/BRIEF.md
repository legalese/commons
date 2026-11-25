# Brief: the DOJ/FTC Antitrust Guidelines for Business Activities Affecting Workers (2025)

This is the subject's part of the brief, as given to the builder on 2026-11-25 (16:24 UTC).
The common brief and the Phase 2 brief that govern every row of this batch are not in this repository; this file restates what binds this row.

Target compiler: `main` (the stable `l4`); the encoding is also checked with the newest `unstable` build.
Label: **AGENCY ENFORCEMENT POLICY, NOT LAW.**
The guidelines say how the U.S. Department of Justice and the Federal Trade Commission identify and assess business practices affecting workers; they do not state what a court must hold.
The text says it "has no force or effect of law" and that it replaces the Antitrust Guidance for Human Resource Professionals (2016): both are to be read at source and quoted briefly in NOTES.

## What to encode

The parent session's first reading; the text overrides it.

- **The general principles**: the focus on an agreement between businesses that harms competition for workers; that it need not be explicit or written; the kinds of evidence the agencies consider (a list: report which are present, never weigh them); the "compete for workers" test; that some agreements are illegal regardless of effect and others need a deeper analysis, keeping which is which exactly as the text says, with the subordinate-and-collateral qualification of the footnote on that point.
- **Sections 1 to 5**: wage-fixing and no-poach agreements and the substance-over-form rule; franchise no-poach agreements; sharing competitively sensitive information, including through a third party or an algorithm; non-competes and penalties for leaving; the other restrictive conditions. Each as a typed fact pattern whose result is what the text says, keeping every "may".
- **Section 6** (independent contractors) and **section 7** (false earnings claims) as rules; **section 8** (reporting) inert. Section 8 holds agency contact details: do not reproduce them in NOTES or comments.
- **Criminal against civil**: what the text says the DOJ may do, and where it says civil liability only (the Criminal Antitrust Anti-Retaliation Act mention), encoded only as stated.

## Forks expected

What makes two businesses "compete for workers"; how the agreement is supplied (a finding by the caller, never inferred); whether "illegal regardless of effect" is a result type of its own; how a list that "is not exhaustive" is represented.
Each is to be labelled "assumed, not ruled" and recorded in NOTES.

## Status to record

The DOJ's index of guidelines and policy statements lists the document, dated January 16, 2025, as read on 2026-11-25 by the session that wrote this brief.
NOTES must say which facts were read at source and which were only reported.

## Source

`../../registers/source-bundle/2025-business-activities-affecting-workers-guidelines.txt` (5,608 words, 13 pdf pages, with `[pdf page N of 13]` markers); provenance and hashes in the `.meta.json` beside it; licensing in `../../SOURCE-LICENSE.md`.
Read all of it, footnotes included, before designing.

## Rules of the work

- Layout: `wk-nouns.l4`; `wk-agreements.l4` (general principles, sections 1 and 2); `wk-information.l4` (section 3); `wk-restrictive-terms.l4` (sections 4 and 5); `wk-contractors-and-claims.l4` (sections 6 and 7); `wk-tests.l4`; `wk-tests-boundaries.l4`; `wk-tests-red.l4`. A compact row: roughly 120 to 200 assertions in all.
- Nouns first (types only), then rules in the text's order, then tests. An `@ref` with section and `[pdf page N]` on every rule.
- A case the text does not answer is `NOTHING` from a `MAYBE` (`main` has no `REFUSE`).
- Results keep the text's modal and its speaker; never "illegal", "unlawful" or "lawful" as a conclusion: "the agencies state ...".
- Tests from the text, both sides of every distinction; a `-red` file of positive controls, counted in `expected_red`.
- Fetch nothing; a fact the text does not give is an open question in NOTES. Short quotations only, swept mechanically against the source.
- Work only in the row's folder; the one edit outside it is the subject's `subject.json` note, changed to say the row exists if it still says nothing is encoded. Commit locally; the parent session pushes.
- Deliverables: the modules, `NOTES.md` (status and what was checked; both builds' `check.sh` output; scope; coverage table; fork register; open questions; withdrawn and superseded guidelines, read against reported; the label), `encoding.json`, `check.sh`, `fetch-main-l4.sh`, this brief.
