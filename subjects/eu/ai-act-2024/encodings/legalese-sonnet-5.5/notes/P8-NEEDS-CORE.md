# NEEDS-CORE (P8)

Nothing is open for the keel's author.
One item is open for whoever finishes P8.

## The role questions of the manufacturer and person seats are not written yet

PLAN.md section 8 says the role question of the product manufacturer seat calls `Art 2(1)(e) the Regulation applies to the product manufacturer`, and that of the person seat calls `Art 2(1)(g) the Regulation applies to the affected person in the Union`.
Both functions are in the keel's `aia-scope.l4` (Articles 1 and 2), which was missing from the first folder and is now in this one, read-only.
The second pass (2026-11-17) was limited to three tasks and did not add the two questions, so `P8-seat-manufacturer.l4` and `P8-seat-person.l4` still assume the role (the file header says so) and carry no role question.
To add them, each of those two seats gains one question, `Under Article 74, as a product manufacturer, ...` and `Under Article 77, as a person affected by an AI system, ...`, calling the function with the plan's inputs, with its cases; nothing else in P8 changes.
