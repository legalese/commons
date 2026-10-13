# Encoding brief: Israel's HVAC work-licensing Law and its Fees Regulations, in L4

You are producing an L4 encoding of an Israeli statute and its fee regulations, from the
Hebrew sources, in English L4. This brief is the whole specification. Read it fully before
opening any source.

You are the ONLY encoder: no ontology agent, no section fleet, no integrator, no independent
test author, no refuters. You do all of it in one context, and you are responsible for
checking your own work with the diagnostics (see "Rules that matter").

## The subject

**חוק הסדרת העיסוק בעבודה במערכת קירור או מיזוג אוויר, התשפ״ה–2025** — the Regulation of
Engagement in Work on Refrigeration or Air-Conditioning Systems Law 5785-2025 (Sefer HaChukim
3349 p. 182), and the **Fees Regulations** made under its ss. 59–60.

The Fees Regulations exist in THREE vintages, and all three are in scope:

| vintage | source | where |
| --- | --- | --- |
| the DRAFT | the SimpLEX screenshot, Figure 4 of Schwartz, Bar-Siman-Tov & Gelbard (2025) | `inputs/fig4-simplex-screenshot.png` (crop), `inputs/fig4-page34-400dpi.png` (whole page) |
| AS MADE | Kovetz HaTakanot 11951, 9 July 2025 | `inputs/kovetz-hatakanot-11951-p2116.pdf` + `.txt` |
| AS AMENDED | the 5786 amendment, Kovetz HaTakanot 12383 | `inputs/takanot-12383.pdf` + `.txt`; consolidated text in `inputs/regulations-fees.wiki` (Hebrew Wikisource rev 3011135, unofficial) |

The screenshot shows only PART of the draft. What it does not show, you do not know. Say so.

The Law itself is in `inputs/sefer-hachukim-3349-pp182-209.pdf` (+ `.txt`, the official
gazette issue) and `inputs/law.wiki` (Wikisource rev 2947808, unofficial, easier to read).
The bill as tabled is `inputs/knesset-bill-25_ls2_5256851.pdf` if you need it.
`inputs/revisions.json` records the Wikisource revisions. `inputs/fig4-en-p28-28.png` is the
English page of the paper that carries the figure's caption.

All inputs are under `INPUTS_DIR` (given in your task). Read them there and nowhere else.
Quote Hebrew from these files mechanically (copy it); never reconstruct it from memory.

## Scope — pinned, do not widen or narrow

From the Law: **ss. 2, 3, 6 and the Second Schedule, 7, 8, 9, 16, 17, 63.** From the Fees
Regulations: **every regulation, in all three vintages.** Plus the **SimpLEX test table**
in the screenshot (the four rows headed תרחישי בדיקה לבחינות מקצועיות, and the worked
example beneath it), transcribed and run.

## Deliverables, all under your `DEPOSIT` directory (given in your task)

1. `.l4` modules with ASCII filenames. Decompose as you see fit (the skill's advice: a nouns
   module first, then modules that follow the source's own structure, then tests). Every
   module starts with `@lang en`. Source language is English; identifiers are English backtick
   names that read like the statute. `@nlg:he` Hebrew heralds are welcome but optional.
2. A tests module that (a) transcribes the SimpLEX table's rows as `#ASSERT`s against the
   DRAFT, in the table's own outcome words, and (b) runs the same scenarios against the
   other two vintages, asserting what each vintage actually answers. If some expectations are
   meant to fail against a vintage, keep them in their own file and say how many.
3. `NOTES.md`: what is encoded, what is not, a coverage table (every in-scope provision, with
   its disposition), a **fork register** (every ambiguity you met, the readings you saw, the
   one you took and why), and a table of the fee for each service under each vintage as YOU
   read the sources, with the regulation cited per cell.
4. `check.sh` that runs every module with the pinned binary and prints per-module error
   counts and assertion tallies. Start from the skill's `assets/check.sh`.
5. `encoding.json` and `SOURCE-LICENSE.md`, in the shape `references/canon-deposit.md` of the
   `encoding-a-subject` skill gives (status `draft`; say in `not_reviewed` that no domain
   expert has read it against the source). The row name is `legalese-sonnet-5.5`; the method
   is a single Sonnet 5.5 agent working alone from this brief.

## Rules that matter

- **Follow the two skills.** Read, before writing any L4:
  `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md` (steps 1-7, 9, 11;
  there is no step 8 here, and you do not deposit into a repository) and
  `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md`, then its
  `references/drafting-patterns.md`, `references/source-patterns/` (all of it, especially
  04-dates-and-periods and 11-when-the-encoding-cannot-answer). Documentation is under
  `/Users/mengwong/src/legalese/l4-ide/doc/`.
- **Encode isomorphically.** A reader holding the Hebrew beside your module checks it line by
  line. Cite the section or regulation on every rule (`@ref` or a comment).
- **Three vintages are three answers, not one.** A fee lookup takes the vintage as an input.
  Where a vintage is silent on a service, the answer is that it is silent (`MAYBE`/`NOTHING`
  or `REFUSE`), never a number borrowed from another vintage.
- **Where the sources do not answer, `REFUSE "…"`** — never `FALSE`, never `0`, never a
  plausible default. A gap is a finding, not a bug. Do not invent a home-made three-valued
  type; the language has `MAYBE` and `REFUSE`.
- **An assertion that fails is a finding.** Never edit an expected value to match what the
  code computed. Report it. Take expected values from the sources, not from your code.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails or
  refuses; the failure is a `DiagnosticSeverity_Error` line and a refusal is a Warning. Never
  report "green" for a result you did not see in the output; report the numbers `check.sh`
  prints.
- **Dates** need `IMPORT daydate` (`YMD y m d`, `add months`, `add years`, `DATE_YEAR`).
  Arithmetic on dates without it produces an ambiguous-operator error, not a date.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task). Leave `JL4_LIBRARY_PATH` UNSET: the standard
library is compiled into the binary and always matches it. `L4_BIN check FILE` typechecks;
`L4_BIN run FILE` also evaluates every `#EVAL`/`#ASSERT`; `L4_BIN nlg --lang he FILE` renders
Hebrew heralds. `l4` has no `--version` flag; the binary's identity is recorded in your task.
Run the binary by its absolute path; do not rely on `l4` being on PATH.

## HARD CLEANROOM RULE — the whole comparison depends on it

Three L4 encodings of this exact subject already exist (an English one with notes, tests and
a Hebrew twin, and a third from a collaborator). **You must not read, grep, list or otherwise
inspect any of them.** Concretely, do NOT open or search:

- anything under `/Users/mengwong/src/legalese/commons/`, `/Users/mengwong/src/legalese/commonswt/`,
  `/Users/mengwong/src/legalese/canon/`, `/Users/mengwong/src/legalese/il/`, or any other
  clone, worktree or copy of those repositories on any volume (including under `/Volumes/`)
- any directory under `/Volumes/transcend/claude-tmp/` other than your own `WORKDIR`
- anything under `~/.claude/` other than the two skills named above
  (no `~/.claude/projects`, no `memory/` directory, no `~/.claude/thermostat-oracle`,
  no `~/.claude/tmp`)
- `/Users/mengwong/src/legalese/l4-ide/jl4/examples/` and `/Users/mengwong/src/legalese/l4-ide/specs/`
  may be read ONLY for L4 syntax and idiom, and ONLY after you have confirmed by the
  filename that the file is not about this Law, refrigeration, air-conditioning, Israel,
  SimpLEX or this Law's fee regulations; do not search them for those words
- do not search any filesystem for `hvac*`, `simplex*`, `kirur*`, `מיזוג`, `קירור`, or this
  Law's name

You may read: `INPUTS_DIR`, the two skills and their references, the l4-ide `doc/` tree, and
other encodings that are NOT about this subject. Your context may also contain an index of
someone's notes that mentions this subject; do not follow it.
If you open a forbidden file by accident: stop reading it, and say so in your final report
under `peeked`. An honest admission costs nothing; a silent peek destroys the comparison.

## Final report (your last message)

Return: (1) the list of files you wrote; (2) exactly what `check.sh` printed; (3) your
coverage table summary (counts per disposition); (4) the forks you took; (5) any failing or
refused assertion and what it means; (6) anything the sources do not answer; (7) `peeked`:
nothing, or what you opened by accident.
