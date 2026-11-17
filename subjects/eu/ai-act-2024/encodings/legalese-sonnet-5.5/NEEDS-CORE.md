# NEEDS-CORE (all parts)

Status: **proposed, not landed.** Nothing below is in the keel modules (`aia-core.l4`, `aia-timeline.l4`, `aia-definitions.l4`, `aia-scope.l4`, `aia-literacy.l4`, `aia-annex-x.l4`). A part that found the keel lacking a type, a constructor or a field declared what it needed under its own prefix in its own module, so every module compiles as it stands; this file gathers the requests in one place so that a later change to the keel can take them in one go.
Taking a request into the keel would mean editing the part modules that carry the local copy and running the gate again; the merge did not do that.
Each section is the part's own `NEEDS-CORE.md`, unchanged; the same text is under `notes/<part>-NEEDS-CORE.md`.

## P0

Two things in the keel could not be called as a seat question needs them.
Neither stops the seat layer: each has a workaround in place, named below, and no keel function was copied or edited.

## 1. A version-dispatching `Art 111(2) the system is saved`

**What is missing.**
The keel offers the saving of Article 111(2), first sentence, as two functions, `Art 111(2) as enacted the system is saved` and `Art 111(2) as amended the system is saved` (aia-timeline.l4, lines 165 and 182).
Both return `BOOLEAN` and take the provision group, the route, the placement date and the significant-change flag.
No function takes `the date asked` and chooses between them.
The date functions of the same paragraph do dispatch (`Art 111(2) the date by which providers and deployers ... must comply` takes `the date asked`), which is why the gap is easy to miss.

**What the seat layer does instead.**
The seat question `Under Article 111(2), as <role>, is my high-risk AI system saved from the application of the Regulation?` (six operator seats) chooses the function itself, with `CONSIDER` on the keel's `Omnibus Art 4 the version in force` of the date asked.
It restates no rule and adds no condition: it only picks which of the two keel functions to call, and passes the group `Chapter III Sections 1 to 3`, the route, the placement date and the flag through.
That dispatch is the one piece of keel-shaped logic in layer 2.

**Request.**
A function `Art 111(2) the system is saved` whose first argument is `the date asked` and whose body is that dispatch, so that a seat only calls it.

**Who is affected.**
Every part agent that asks whether a legacy high-risk AI system is saved from its provisions has the same choice to make.

## 2. The Annex X act as a `STRING`

**What is missing.**
`Annex X the large-scale IT system is established by a listed legal act` takes the act as a `STRING`.
A seat can therefore ask the act only as free text.
An enumeration of the twelve acts would let a form offer a choice.

**What the seat layer does instead.**
The input `the act that establishes that large-scale IT system` is a `STRING` whose `@desc` lists the twelve spellings Annex X uses, and says to write `none` if the system is not a large-scale IT system component.

**The failure is silent.**
A misspelt act, an extra space or a different dash reads as "an act Annex X does not list", and the answer is `NOTHING` ("not covered") with no error.
The case files assert that an unlisted act gives `NOTHING`; they cannot tell a typo from a true "not listed".

**Request.**
A `DECLARE` of the twelve acts as constructors in aia-annex-x.l4, and a variant of the function that takes it.

## P1

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

## P8

Nothing is open for the keel's author.
One item is open for whoever finishes P8.

## The role questions of the manufacturer and person seats are not written yet

PLAN.md section 8 says the role question of the product manufacturer seat calls `Art 2(1)(e) the Regulation applies to the product manufacturer`, and that of the person seat calls `Art 2(1)(g) the Regulation applies to the affected person in the Union`.
Both functions are in the keel's `aia-scope.l4` (Articles 1 and 2), which was missing from the first folder and is now in this one, read-only.
The second pass (2026-11-17) was limited to three tasks and did not add the two questions, so `P8-seat-manufacturer.l4` and `P8-seat-person.l4` still assume the role (the file header says so) and carry no role question.
To add them, each of those two seats gains one question, `Under Article 74, as a product manufacturer, ...` and `Under Article 77, as a person affected by an AI system, ...`, calling the function with the plan's inputs, with its cases; nothing else in P8 changes.
