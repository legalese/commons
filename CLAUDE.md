# CLAUDE.md — `legalese/commons`

Notes for a coding assistant working in this repository.
It holds **law**: sources, and L4 encodings of them.
The tools — the L4 language, the `l4` binary, the pipeline — live in [`legalese/l4-ide`](https://github.com/legalese/l4-ide).

## Before you encode anything

**Load the L4 skills.** They do not live in this repository, so a session started here has neither unless the L4 plugin is installed:

```
/plugin marketplace add legalese/l4-plugin
/plugin install l4-computational-law@legalese
```

It carries two skills:

- **`encoding-a-subject`** — the workflow for encoding a whole Act, regulation or contract and filing it here: the brief, a coverage table, nouns before rules, tests taken from the source, a self-check, an independent test pass, and this repository's layout.
  **Start here for any request to "encode" something.**
- **`writing-l4-rules`** — the language itself.

If `/skills` does not list `encoding-a-subject`, the installed plugin predates it; read it at [`skills/encoding-a-subject/`](https://github.com/legalese/l4-ide/tree/unstable/skills/encoding-a-subject) in l4-ide.

**Get a current `l4`.** The plugin's `scripts/install-l4.sh` installs the release it was built against; otherwise take the newest archive from [`legalese/prereleases`](https://github.com/legalese/prereleases/releases).
`l4` has no `--version`; the archive's `BUILD-INFO.txt` names the commit.
A binary older than the skills rejects constructs the skills tell you exist, and the error reads like your mistake.
Leave `JL4_LIBRARY_PATH` unset.

## Whose seat, and the other design choices (ruled 2026-10-18)

**Every encoding is written from the seat of the individual to whom the law is applied** — the employee, the vehicle owner, the accused, the heir, the applicant — never the regulator, the court, the insurer or the department.
Decisions are phrased as that person would ask them ("Must I …?", "Am I …?", "What can I be made to pay?"), and the facts are ones that person could state.
Where a provision addresses only an official, encode what it means for the individual: what may be done to them, what they must be given, by when.
Record the seat in the encoding's NOTES.md.

**Every other design choice takes the recommended default**, the one Legalese Studio's Design stage would recommend:

- the Act alone, with the instruments that set its numbers or dates brought in;
- the actors the text names;
- a judgment the law hands to someone else answered conditionally ("X, if the officer is satisfied that …"), never guessed;
- the Act's own definitions worked out from facts, borrowed terms asked as facts;
- one case is the text's natural unit (one employment, one vehicle, one act);
- the Act's own terms, each with a plain gloss;
- the operative sections in scope; the machinery (boards, powers to make regulations, commencement) out.

These rulings exist so that any row here can be taken into Legalese Studio and run through Resolve, Refine and Test with the owner confirming the design rather than remaking it.

## Longer encodings stay, and get a seat layer (ruled 2026-10-21)

**A seat encoding never replaces a longer one.** Where an Act already has a longer encoding (a whole-Act or multi-module encoding, a first pass, a named encoding), keep it.
Meet the seat rule by adding a **seat layer** in the same encoding folder: a `<prefix>-seat.l4` module that IMPORTs the longer modules and asks the individual's questions, with `@export` and `@desc` on each, as the Employment Act, Road Traffic Act and Penal Code encodings in `subjects/sg/` do.
A layer has to live in the same folder, because the stable `l4` resolves IMPORT only within the importing file's folder and the libraries.
Write a separate shorter baseline (`encodings/baseline-<date>/`) only where no longer encoding exists. Where both already exist, both stay: neither deletes the other.
Legalese Commons' Interact form needs seat questions with `@export`/`@desc`, from a baseline or a seat layer.

**More than one seat (ruled 2026-10-21).** The individual's seat comes first and is required. Further seat layers are welcome for any other party the text puts duties or liabilities on — the employer, the landlord, the seller, the business — each as its own module beside the first (`<prefix>-seat-<party>.l4`), drawing on the same longer modules so the seats cannot disagree about the law.
Officials still get no seat: not the regulator, the court or the department.
Each seat layer keeps its own names (two layers must never define the same one) and records its seat in NOTES.md. The first example is `subjects/sg/employment-act-1968/encodings/naive-2026-10/` (employee and employer).

## Where things go

The layout is ruled in [`docs/directory-conventions.md`](docs/directory-conventions.md) (rulings of 2026-08-05; the ISO spelling ruled again 2026-09-26).

In short: `subjects/<jurisdiction>/<slug>/` for the law, with `<jurisdiction>` an ISO 3166 code in lowercase (`sg`, `il`, `us/ca`); `subjects/contracts/<genre>/<slug>/` for contract forms; and each encoding as its own row at `encodings/<row>/`, with an `encoding.json`, a `NOTES.md` and a `SOURCE-LICENSE.md` beside the `.l4`.
The `encoding-a-subject` skill's `references/canon-deposit.md` walks through it.

Before creating a subject, check whether the law already has one: a second encoding of a law is a new row beside the others, and rows are equal.

**Where to commit.** Members of the `legalese` GitHub organisation commit straight to `main` (ruled 2026-09-26).
**Contributions from outside Legalese are welcome**, by the standard GitHub route: fork this repository, commit to a branch of your fork, and open a pull request against `main`.

## Worked examples to read first

- `subjects/il/hvac-work-licensing-2025/encodings/legalese/` — a Law and its fee regulations in three vintages, with a scope statement, a fork register, a table of every fee in each vintage, and a test file that is meant to fail and says how many times.
- `subjects/sg/child-support/` — a subject whose primary source is an announcement rather than a statute, and says so.

## The requirement ledger

Singapore's encoding priority comes from the requirement ledger, `subjects/sg/requirements.jsonl`.
It is described in [`docs/ledger/LEDGER.md`](docs/ledger/LEDGER.md), and
[`docs/ledger/NOTE-TO-ENCODER.md`](docs/ledger/NOTE-TO-ENCODER.md) says how to take work from it.
`python docs/ledger/check-ledger.py` validates it and prints the open queue.

## Only law lives here

Commons holds the law and its encodings. Tools, consoles, pipelines and simulations are kept in a
separate repository; nothing under `subjects/` depends on them.

## When the encoding exists

[`PIPELINE.md`](PIPELINE.md) describes the l4-ide pipeline that takes a finished encoding to its projections (DMN, BPMN, a web wizard) and the two human gates.
You do not need it to produce a good encoding.
