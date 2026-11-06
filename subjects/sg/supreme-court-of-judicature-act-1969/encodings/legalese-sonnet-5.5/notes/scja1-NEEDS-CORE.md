# NEEDS-CORE.md (scja1)

Nothing here blocks scja1: every file compiles and runs against the core as the keel wrote it, and every type or constructor scja1 needed beyond the core is defined in its own module under its own section label (`s 19 matter`, `s 22(3) manner of receiving further evidence`, `s 27(2) step`, `s 28A(2) provision`, `s 29B(3) step`, and the others listed in `NOTES.md`).
These are suggestions for the merge, in the order I would take them.

1. **One shared input for the ground "every issue already decided".**
   `s 17C(1)(a)` and `s 22B(1)(b)` (scja1) each ask the same question as a plain `BOOLEAN` input named for their own section: "every issue in the appeal has already been decided in an earlier matter in which the appellant was involved, and the appeal therefore has no merit".
   `PLAN.md` difficulty 7 says `s 38(1)(b)` and `s 56(1)(b)` (scja2) ask it too.
   The core holds the shared nouns (the keel's notes say so), not questions, so it cannot hold the question itself.
   If the lead wants one question in the merged seat instead of four, the hoist is a shared seam name that the four asking functions take; the wording is the one above, and scja1's two inputs are at `scja1-part3-div2-procedure.l4` (`s 17C(1)(a) every issue ...`) and `scja1-part3-div4.l4` (`s 22B(1)(b) every issue ...`).
2. **One shared input for the public holidays.**
   `s 10B(1)` and `s 29B(2)(b)` (scja1) take `the public holidays` as a list of dates asked of the person.
   `PLAN.md` difficulty 2 says scja2 counts periods too (`ss 41(10)(b)` and `59(10)(b)`), so the merged seat may want to ask for the holidays once.
3. **The time of extraction (optional).**
   `s 29B(2)(a)` speaks of "the time at which the judgment or order ... is extracted"; the core's `Decision` records `date the judgment or order was extracted` as a date.
   A request made on the day of extraction therefore answers `NOTHING` (section "What the text turns out to say", finding 7).
   If the lead wants that case decided, the core would need a time of day on `Decision`; I did not ask for one.
4. **A member of `Kind of Judge` for a person who is not a Judge (optional).**
   `s 2 Judge` (scja1) answers `JUST TRUE` for every member of the core's `Kind of Judge` (`scja-core.l4`: the Chief Justice, the Vice-President and Justices of the Court of Appeal, the President and Judges of the Appellate Division, a Judge of the High Court, a Judicial Commissioner, a Senior Judge, an International Judge).
   Its `OTHERWISE JUST FALSE` branch ("means") is therefore not reachable from a `Judge` record: a District Judge cannot be entered as an office.
   If the lead wants "is a District Judge a Judge under the Act?" to be askable, the core would add a member such as `another office`; I did not edit the core.
