# NEEDS-CORE -- mlr5

What part `mlr5` wanted from the core `mlr-core.l4` and did not find.
`mlr-core.l4` is read-only to this part, and a constructor cannot be added to another module's type, so each need below is met by a small type of this part's own, and is recorded here for the lead to hoist.

## 1. A constructor `medium risk` in `Level of risk`

- **Wanted:** a third rating between `high risk` and `low risk`.
  The core's `Level of risk` (core line 206) has `high risk`, `low risk` and `neither high nor low risk`.
- **Where the text needs it:** Schedule 4, the item that asks for "the number of firms subject to the supervision of the supervisory authority which the authority considers to be (a) high risk; (b) medium risk; (c) low risk" (lines 3215-3218).
  Limb (b) names "medium risk" in the Schedule's own words.
- **What this part did:** declared `sch 4 risk rating` (`sch 4 high risk`, `sch 4 medium risk`, `sch 4 low risk`) in `mlr5-sch4.l4` and used it for that item only (`sch 4 item 6 the limb that counts firms of that rating`).
- **Why not reuse `neither high nor low risk`:** the text names "medium risk" as a rating the supervisory authority applies, and the core has no constructor of that name.
  Whether `neither high nor low risk` means the same is a reading for the lead; this part did not make it.
- **If the lead hoists it:** `sch 4 item 6 the limb that counts firms of that rating` and the seat question "Under schedule 4 item 6, ..." would take the core's type; the three assertions on item 6 in `mlr5-tests-sch4.l4` (lines 150-152) and the three cases of that question in `mlr5-cases-seat.l4` name the constructors and would change with it.

Nothing else was needed from the core.
This part read `Form of customer` (Schedule 5), `Part of the United Kingdom` (Schedules 3A and 6B) and `reg 1(2) the date these Regulations came into force` (Schedule 7).
