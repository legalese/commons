# PROGRESS -- dg10 (Subchapters XIII to XVI, src:1632-1934)

State at the end: everything in the brief is written and the gates below pass.
NOTES.md has its ten headings, all filled; the coverage table in it is generated between its markers.

## What is in this folder

- Layer 1 (7 modules): `dg10-sos-service.l4` (the passages that ss 321(b), 376(b), 381(d) and 382(c) share), `dg10-suits.l4` (ss 321-330), `dg10-close-status.l4` (ss 341-349), `dg10-close-governance.l4` (ss 350-356), `dg10-pbc.l4` (ss 361-368), `dg10-foreign-qualification.l4` (ss 371-380), `dg10-foreign-withdrawal-and-suits.l4` (ss 381-385).
- Tests of layer 1 (849 assertions): `dg10-tests-suits.l4` (170), `dg10-tests-close.l4` (276), `dg10-tests-pbc.l4` (105), `dg10-tests-foreign.l4` (298).
- Layer 2: `dg10-seat.l4` (165 questions, each with `@export` and `@desc`, under four `§§` groups) and `dg10-cases-seat.l4` (665 worked cases, every question at least once, 53 of them `NOTHING` cases).
- `NOTES.md` and this file.

## Gates at the end

- `L4=<stable l4> L4_TARGET=unstable ./check.sh`: exit 0; 14 modules, 0 errors, 1514 assertions satisfied, 0 failed, 0 refused (the table is in NOTES.md, "What check.sh prints").
- `python3 -I srcrefs.py check --refs <text> dg10-*.l4`: 313 src: lines, 265 runs, 291 locators, 0 problems.
- Coverage (`inputs/tools/mkcov.py`): 246 rows (96 encoded, 44 fork, 106 inert), 0 non-blank lines of 1632-1934 named by no row.
- `l4 check` over every `dg10-*.l4`: no `end of the file` or `follows code`.
- No top-level name defined in two of my modules; none redefines a name in `dg-core.l4`; no scratch file left in the folder.

## How I worked (so a compacted context can resume)

- The brief: `.../scratchpad/td/dg/dg10/BRIEF.md`.
- Working tools live in `inputs/tools/` (not part of the deposit): `expand.py` (turns `-- @Q` placeholders into mechanical `-- src:N` quote lines), `mkcov.py` (rebuilds the coverage table from `coverage.tsv`), `chk.sh` (run one file with the srcrefs check), `qx.py`, `qsig.py`, `qbody.py`, `qcov.py` (expand `@Qn` question placeholders in the case sources `cases/b*.src`; list a question's inputs and body; check every question has a case), and `notes/` (the sections of NOTES.md before they were spliced in).
- Rule names begin with the section locator (`s 321(a) ...`), so the coverage script can find them.

## Decisions taken

- Fork register F1-F35 is in NOTES.md; the numbers are fixed in the code comments and in `coverage.tsv`.
- Seat readings per subchapter, the percentage inputs, the single "least approving class" question and the plaintiff's-voice questions in Subchapter XIII are mine, labelled "assumed, not ruled" in NOTES.md ("Before this is worth relying on").
- One expectation in the worked cases failed on its first run and was then corrected: for s 350, where the board is not controlled by the agreement, I had written `JUST FALSE`; after the failure I reread the sentence and the F14 comment, judged the text silent there, and changed the expectation to `NOTHING`. No other assertion failed when first evaluated (the s 354 cases were rewritten before they were evaluated, because I had misread that question's first input and the file did not compile).
- One bare `NOT` in `dg10-foreign-withdrawal-and-suits.l4` (s 382(b)) was bracketed to meet the brief's rule; behaviour unchanged.

## Dialect lessons

- A mixfix call whose last argument is a genitive expression must have that argument bracketed.
- `l4 check` prints one parse error at a time.
