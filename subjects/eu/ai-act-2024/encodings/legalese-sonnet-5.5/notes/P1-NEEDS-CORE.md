# NEEDS-CORE (P1)

Status: written 2026-11-17 by part agent P1 from the core as supplied (`aia-core.l4`, read in full); each claim below was checked against that file.

## Parties the core's `Role` has no constructor for

`Role` has `Provider`, `Deployer`, `Authorised representative`, `Importer`, `Distributor`, `Product manufacturer`, `Operator`, `Notified body` and `Affected person` (`aia-core.l4`, `DECLARE Role`).
Several provisions of Articles 5 to 7 address someone else, and a rule's party must be a `Role`:

| provision | the text addresses | what P1 wrote instead |
| --- | --- | --- |
| Art 5(1) | whoever places on the market, puts into service or uses (no party named) | `Operator`, as the keel does for Art 111(1) |
| Art 5(2), (4) | a law enforcement authority using the system | `Operator` |
| Art 5(3) | a judicial authority or an independent administrative authority whose decision is binding | `Operator` |
| Art 5(4), (6) | the relevant market surveillance authority and the national data protection authority | `Operator` |
| Art 5(5) | a Member State | `Operator` |
| Art 5(6), (7), Art 6(5), Art 7(2) | the Commission | `Operator` |

Proposed, not landed: constructors `Law enforcement authority`, `Judicial or independent administrative authority`, `Market surveillance authority`, `National data protection authority`, `Member State` and `Commission` in `Role`.
What would make it true: a change to `aia-core.l4`.
Until then every such rule's `BECAUSE` text names the real party, and NOTES.md (`Jural relations (P1)`) says who it is.

## The scope module and the two role questions

`aia-scope.l4` is among the keel modules in the folder (`aia-annex-x`, `aia-core`, `aia-definitions`, `aia-scope`, `aia-timeline`).
The seat layers for the person and the product manufacturer could call `Art 2(1)(g) the Regulation applies to the affected person in the Union` and `Art 2(1)(e) the Regulation applies to the product manufacturer` from it (both are in `aia-scope.l4`); they do not, so the two role questions are not written (NOTES.md, `Seats (P1)`).
Proposed, not landed: the two questions, each with its case file.
What would make it true: a change to `P1-seat-person.l4` and `P1-seat-manufacturer.l4` and their case files, not a change to the core.

## A constant that does not fit a Chapter III provision that is not about one AI system

`the date to pass when no AI system is in question` (1 January 1900) with `Route Article 6(2) and Annex III` makes the keel treat the system as placed before Chapter III and saved by Article 111(2), so the gate answers FALSE on every date; with `Route neither` the keel has no date for Chapter III at all.
P1 passes `the date asked` as the placement date for Article 7 and Article 6(6) to (8) (fork F-7-gate).
Proposed, not landed: a second constant in the core, or a documented rule in PLAN.md section 7, for a Chapter III provision about no one AI system.
