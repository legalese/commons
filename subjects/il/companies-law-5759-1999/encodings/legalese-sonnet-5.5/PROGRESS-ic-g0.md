# PROGRESS: ic-g0 (keel agent), Israeli Companies Law 5759-1999, lines 1-262

Status on 2026-10-25: the keel is written and checked. `NOTES.md` is the guide for the six part agents; this file records what was done and why.

## Done

- Read the brief, both skills (the two `SKILL.md` files, `dialects.md`, `source-locators.md`, `drafting-patterns.md`, source-patterns page 1 in full and the entries on "includes", offices as parties, one type with alternatives, deeming, repealed sections, determinations as records), `ENCODING-GUIDE.md`, the example seat layer, `check.sh`.
- Read the whole range, lines 1-262: title block and table of contents (1-153), the Part 1 heading (155), section 1 (157-261), 89 definition lines defining 94 terms.
- Sampled sections 4-7, 46-50 and 87-89, the units the Law uses (shekels, percent, days), the commencement section (377, src:3358-3359), the signature block (src:3549), section 249ב (src:1680) for fork F4.
- Probed the stable binary 1.6.98: Hebrew names compile, `YMD` as a rule, `5%`, names with ` - `, `:` and an en dash, a Hebrew deontic with `צד`, date comparison with the shim, `srcrefs.py` on lines with `|` in the markup.
- Wrote `ic-core.l4` (9 types, the `YMD` shim), five layer-1 modules (`ic-core-company-kinds`, `-securities`, `-people`, `-meetings`, `-deals`; 59 rules and one stub, 16 module-level types) and five test files (256 assertions, expected values written from the text).
- Wrote `NOTES.md` with the required headings, a 107-row coverage table (every non-blank line of src:1-261 falls in some row, checked by script), a 94-term defined-terms table, 17 forks, and the rule-signature table the pieces read.
- Checked: `check.sh` (0 errors, 0 failed, 0 refused), `srcrefs.py check --refs` and `--strict` (0 problems), no name defined twice (script over the non-test modules), a throwaway file importing all five modules and calling one rule from each (7 assertions satisfied, then deleted), no warnings, no dangling `@ref`.

## Decisions and the section that licenses each

- Core types, each licensed by section 1: `צד` (parties; also section 46), `סוג אדם` (מספר זהות, מען), `קרבה` (קרוב), `משרה` (דירקטור, נושא משרה), `דין ההתאגדות` and `עובדות על חברה` (חברה, חברה ציבורית, חברה פרטית, חברת איגרות חוב, plus the plain inputs for public-benefit company, government company and reporting corporation), `קשר לחברה` (בעל מניה מהותי, בעל ענין, שליטה), `הצבעה` (מנין קולות), `מסמך שהרשם הוציא` (יום ההתאגדות, תעודת התאגדות).
- Types used only by my own rules stay in the layer-1 modules, beside the rule.
- Rules take the defined term as their name; facts records are named `עובדות על …`; constructors of `צד` are in the definite form so that they cannot meet a rule name.
- Eight rows are `fork` (F1 twice, F2 to F7 once each, in the register of 17 entries): the readings taken are recorded with the text that licenses each.
- Pointers to other pieces' sections (60, 87, 110, 154, 240, 270, 308, 312, 323, Part 9 chapter 1A, Fourth Schedule) are plain inputs, named for the section; the table in "Instructions to the pieces", item 10, lists them for the pieces.
- No date value is defined: the range has only the year in the title. Passing (src:3549) and commencement (src:3358-3359) belong to `ic6`.

## Next

Nothing in the keel's own range is left. If a part agent finds a name clash or a missing shared type, the keel is where it is fixed, and every piece must then take the new copy.
