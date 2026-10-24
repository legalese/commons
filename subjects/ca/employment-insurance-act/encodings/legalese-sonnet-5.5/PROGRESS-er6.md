# PROGRESS: piece er6 (Employment Insurance Regulations, lines 1709-2536 of SOR-96-332.txt)

Working log, kept on disk because the context may be compacted.
After a compaction: re-read this file, NOTES.md and the text, not the summary.

## State

Everything the brief asks for is written and ran clean on 2026-10-24.
Nothing is in progress.
The last full run is the table in NOTES.md under "What check.sh prints".

## Sections done (all of lines 1709-2536)

- Part VI (reg 93): `er6-part-vi-alternate-access.l4`, tests `er6-tests-part-vi.l4`
- Part VII (regs 94 to 95): `er6-part-vii-transitional.l4`, tests `er6-tests-part-vii.l4`
- Schedule I: `er6-nouns.l4`, `er6-schedule-i-regions.l4`, tests `er6-tests-schedule-i.l4`
- Schedules II to II.94: `er6-schedule-ii-pilot-regions.l4`, `er6-schedule-ii-pilot-tables.l4`, tests `er6-tests-schedule-ii.l4`
- Schedule III: `er6-schedule-iii-interim-provisions.l4`, tests `er6-tests-schedule-iii.l4`
- Related Provisions (with Schedule 10): `er6-related-provisions.l4`, tests `er6-tests-related-provisions.l4`
- Amendments Not in Force: no module; all `inert` rows in the coverage table
- Layer 2: `er6-seat.l4` (66 questions, A1 to E19) and `er6-cases-seat.l4` (183 cases, every question has at least one)
- `NOTES.md` with all ten required headings

## Decisions taken (with the text that licenses each)

- Names carry the instrument: `reg N(M) ...` for the body; `Regs Sch I s 2(1) ...`, `Regs Sch II.2 ...`, `Regs Sch III Part II s 19(2) ...` for schedules; `Regs related provision 2022 c 10 s 350.1(1) ...` for related provisions. Many schedule and related-provision section numbers (12, 19, 22, 23, 34, 55, 225 ...) shadow real regulations that other pieces encode.
- Schedule I is a geography test over `er6 Place` (province, census division, census subdivision, metropolitan area, agglomeration, "east of London"), one BOOLEAN rule per region, because the text defines each region by what it consists of (Schedule I ss 2 to 14).
- Dates are data: reg 95(1) to (5) carried as DATE values and `Period of days` with @ref (the brief's "Dates are data"); the interim Schedule III rules are gated on them.
- Gating by date: a transitional or interim provision returns the law's own answer outside its window (FALSE, or NOTHING for a number or a date), never a refusal (forks F14, F9).
- Amendments Not in Force are `inert` and are merged nowhere (brief). The keel assigned "long-tenured worker" (reg 77.9994) to this piece; it is in an amendment not in force, so inert.
- Reg 350.1(2)'s four definitions are encoded (a Related Provision that still decides which earnings rules apply).
- The maximum weekly insurable earnings of Schedule III are an input; the tests use $750, which the Act's Schedule II item 1 (interim section 4(2), source line 3252 of the Act, piece ei6) gives. An earlier draft used the invented figure 1000; it was replaced once the Act's figure was found. The Act's subsection names no year.
- Schedule II.6 "Price Edward Island": NOTHING for the region of Prince Edward Island (fork F13).

## Measured on the binary

- A chain of 62 `PLUS` terms did not finish type-checking in 60 s (over five minutes in a test file); `sum (map ... (LIST ...))` over the same terms runs in under 3 s.
- `MIN` and `MAX` do not exist; `minimum` is ambiguous; the list-length function is `count`, not `length`.
- A constructor with a field is built by application and matched as `WHEN ctor n THEN`.

## Files written (all in this folder)

- `NOTES.md`, `PROGRESS.md`
- `er6-nouns.l4`, `er6-part-vi-alternate-access.l4`, `er6-part-vii-transitional.l4`, `er6-schedule-i-regions.l4`, `er6-schedule-ii-pilot-regions.l4`, `er6-schedule-ii-pilot-tables.l4`, `er6-schedule-iii-interim-provisions.l4`, `er6-related-provisions.l4`
- `er6-seat.l4`, `er6-cases-seat.l4`
- `er6-tests-part-vi.l4`, `er6-tests-part-vii.l4`, `er6-tests-schedule-i.l4`, `er6-tests-schedule-ii.l4`, `er6-tests-schedule-iii.l4`, `er6-tests-related-provisions.l4`
- Not deposited: the generator scripts in `inputs/er6-gen/` (they read the raw text and write the tables, quotes, region rules, seat and cases).

## Peeked

Nothing forbidden was opened.
Outside my range I read only what the cross-references needed: lines of `SECTION-INDEX.txt` by section number, the first one or two lines of Act ss 7, 9, 18, 21 to 23.3, and Act lines 3244 to 3256 (the Act's interim section 4); and I ran `grep -n "maximum weekly insurable earnings"` over both text files (5 and 4 matching lines), which is outside the SECTION-INDEX route the brief prescribes but inside the inputs.
