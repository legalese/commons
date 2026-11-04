# PROGRESS (kept current; compacted as work lands)

Session: sg-fwd-unstable. Started 2026-11-03.
Row: `subjects/sg/broadcasting-act-1994/encodings/unstable-multitemporal-2026-11/`.
Target: unstable. UNSTABLE-ONLY, forward-looking, do not deploy; not the answer of record.
Compactions seen: 0.

## Done (as of 00:25 +08, 2026-11-04)

- First round (23:00 to 23:55 on 3 November): modules, tests, findings 1 to 9, NOTES.md, encoding.json, SOURCE-LICENSE.md, report to team-lead. The Gazette deposits landed during the work; every quote has `src:` lines; `srcrefs.py --strict` 0 problems on the four modules that quote.
- Second round (after team-lead's four messages):
  - Every number re-run on the shelf build `unstable-20261101-8e19faa (unstable, 8e19faa, 2026-11-01)`: 274 assertions satisfied, 0 errors, 0 failed, 0 refused, 11 modules. All 34 files of the row, plus the tutorial's two examples and six early probes, give the same normalised diagnostics on the dev build and on the shelf build: no finding depends on the build.
  - Seat takes the KIND of receiver (television, radio, satellite dish) as a plain input; radio maps to "Broadcast sound receiver"; 10 new radio assertions in `sgbau-tests-seat.l4`; `batch/` regenerated with the kind (and an invalid kind refused at the boundary).
  - `WALKTHROUGH.md` (generated): `build-walkthrough.py` + `walkthrough-template.md` + `sgbau-walkthrough.l4` + `findings/alt-*.l4` + `findings/walkthrough-main-probe*.l4`. Steps 0 to 8, a radio step, eight ways of writing the rule on 15 pairs of days, the stable build's diagnostics verbatim, a closing table. Claims of the top section are checked by the script against what was printed.
  - NOTES.md: first paragraph "UNSTABLE-ONLY, FORWARD-LOOKING, DO NOT DEPLOY"; section on what ENCODING-GUIDE section 1 item 2 and section 5 require and how the row departs; binary section names the shelf build, dev build as footnote; walkthrough section; forks 11 to 13.
  - encoding.json: `target` `unstable`, `target_reason`, `deployable` false, `deployable_reason`, shelf build identity, dev footnote, walkthrough named.

## Not done

- Independent test pass (step 8 of the skill).
- Cutting WALKTHROUGH.md down for a lay reader (GM's job); the script rebuilds it on any day (today's date is written into the P13 pair).

## Stable row, re-read log

- 23:46: `sgba-sched.l4` mtime 22:12, `sgba-vintage.l4` 22:11, `sgba-nouns.l4` 22:22, `sgba-p1-defs.l4` 23:04: no version table for the First Schedule; one DATE input; window 25 Sep 2024 to 1 Oct 2026; NOTHING outside.
- 23:56: `sgba-nouns.l4` moved (23:47): it now declares `First Schedule version` with `takes effect on` and `published on` and a tie-break (latest published on or before the reading day, among those taking effect on or before the conduct day). `sgba-sched.l4` and `sgba-vintage.l4` unchanged, so no rule reads the table yet. NOTES.md comparison rows 11 to 14.
- 00:19: `sgba-sched.l4` (22:12), `sgba-vintage.l4` (22:11), `sgba-nouns.l4` (23:47): unchanged since 23:56.
- 00:40: per-finding shelf-versus-dev comparison (`findings/compare-builds.sh`, 25 identical, 0 different); walkthrough: glosses split to one sentence per line, "Judgement calls" section added (the hour, published not made, asking before the conduct).
- 00:55: team-lead's revision: top section, step captions and table headings reworded to the narrower claim (the licensing rule, as encoded, catches / the First Schedule, as encoded, lists); "How to read" says the page is about dates and not about liability, and that the Telecommunications Act is separate; the walkthrough helpers renamed `the licensing rule catches a television / a radio / a satellite dish`. The TVRO Regulations' holder rule was not examined, so the page says only that they are not encoded.
