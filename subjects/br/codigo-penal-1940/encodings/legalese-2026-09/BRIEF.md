# Encoding brief: Código Penal (Brazil, 1940), in L4

You are one of a team producing an L4 encoding of the Brazilian Penal Code from its source text: an ontology pass (g0), then encoders working in parallel on disjoint ranges of articles, alongside three sweep agents and a set of independent test authors.
This brief is the whole specification, shared by all of them; your own task message adds only your role and scope.
Read it fully before opening the source.

## The subject

**Código Penal — Decreto-Lei nº 2.848, de 7 de dezembro de 1940**, as amended through Lei nº 15.517 de 2026 (Planalto's compiled text, fetched 2026-09-29).
Parte Geral (arts. 1–120, wholly re-enacted by Lei nº 7.209/1984): the application of penal law, the theory of the crime, imputability, participation, the penalties and their calculation, suspension, parole, effects of conviction, security measures, the penal action, and extinction of punishability including prescription.
Parte Especial (arts. 121–361): the offences, in twelve Títulos arranged by protected legal interest.

## Sources — read these and nothing else

`SOURCE` = `/Users/mengwong/src/legalese/commonswt/br-penal/subjects/br/codigo-penal-1940/source/`

- `SOURCE/codigo-penal-1940.txt` — **the text you encode from.** One source paragraph per line. Every quotation you put in the encoding is copied from this file, never retyped from memory.
  Text wrapped `⟦STRUCK: …⟧` is revoked matter that Planalto shows struck through; it is not law.
  Inline notes such as `(Redação dada pela Lei nº …)` record amendments already applied to the text.
- `SOURCE/vide-index.tsv` — the 33 `(Vide …)` pointers, numbered V1–V33, each with its line.
- `SOURCE/senado-dadosabertos-527942.xml` — the Senado's metadata of every later norm that touched a dispositivo, with dates. Your P2 sweep starts here. `grep` it; it is one long line.
- `SOURCE/README.md` — how these were obtained.

The source is Portuguese and so is the encoding. There is no official English text; do not import one.

**Cleanroom.** Do not read other encodings of this Code, or of any other penal code, in canon or elsewhere. Do not read `~/src/legalese/pc-encode`. Your guide to L4 is the skills below; your guide to the law is the source.

## Where you write

`ENC` = `/Users/mengwong/src/legalese/commonswt/br-penal/subjects/br/codigo-penal-1940/encodings/legalese-2026-09/`

Every file you create is under `ENC`, named with **your group prefix** (your task message gives it: `cp-g0-`, `cp-g1-`, … `cp-g6-`), ASCII only.
**Do not edit a file another group owns.** Two exceptions, both owned by the ontology pass and read-only to everyone after it: `cp-dominio.l4` and `cp-pena.l4`.
If you need a shared noun that is not there, declare it in your own module, mark the declaration with a comment `-- PROPOSTO-COMUM: <why other groups will need it>`, and list it in your notes file. The conductor hoists it at integration. Duplicated nouns are expected and cheap to fix; two agents editing one file is not.

## Language — pinned

- **Identifiers are Portuguese**: the Code's own words wherever the Code has a word (`` `furto qualificado` ``, `` `funcionário público` ``, `` `emprego de arma` ``). Diacritics are fine in backticked names.
- **Every module starts with `@lang pt`**, before its `IMPORT`s.
- **English glosses**: an `@nlg:en` on every `@export`ed rule and on every record field. An untagged `@nlg` (Portuguese, under `@lang pt`) is welcome wherever the identifier alone does not read as a sentence.
- **Placement is where heralds go wrong silently.** Follow `writing-l4-rules`: a rule's herald on its own line immediately above the definition body; a record field's on its own line below the field. Do not put a herald on a line of its own above `GIVEN` — it captures backwards onto whatever precedes it, with no diagnostic.
  **Verify it:** for each module, run `L4_BIN nlg --lang en <module>` and read the output. A herald that did not attach leaves the bare Portuguese name, and nothing else tells you.
  Measured on this binary: `nlg --lang en` renders the English heralds, but the connective frame ("with", "where", "is") is English in both languages; that is the renderer, not your defect.

## House rules

- **Isomorphic.** A reviewer holding the source beside your module checks it article by article. One article → one recognisable place; keep the Code's numbering in `§` section headings (`§ \`Art. 155 — Furto\``) and cite with `@ref` on every rule, in the form `@ref CP art. 155, § 4º, II`.
- **Nouns before rules.** Facts a witness could testify to (the thing was movable, the victim was 13, a weapon was used) are record fields, supplied as input. Whether they make out an offence is a rule.
- **Inputs as `GIVEN`**, threading a record. `ASSUME` is deprecated for inputs.
- **`BRANCH IF … IF … OTHERWISE`, never `ELSE IF` chains.**
- **Where the source does not answer, `REFUSE "…"`** — never `FALSE`, `0` or a plausible default. Where the source names an absent case, `MAYBE`/`NOTHING`. Do not invent an `Established`/`Rejected`/`Unresolved` enum.
- **Judgement stays with the judge.** Where the Code hands a court a range or a discretion ("de um terço até a metade", "o juiz pode deixar de aplicar a pena", art. 59's circumstances), encode the range or the power, not a number the Code never chose.
- **Several modules, split along the Code's own structure** (Capítulo, or a run of related articles). A module over ~1,500 lines cannot be reviewed article by article.
- **Read** `/Users/mengwong/src/legalese/l4-ide/skills/writing-l4-rules/SKILL.md`, its `references/gotchas.md`, `references/drafting-patterns.md` and every page of `references/source-patterns/` **before you write L4**, and `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/SKILL.md` for the workflow. They are the house style and they record traps that were measured, not guessed.

## The per-offence contract

The ontology pass (g0) fixes the exact types and names in `ENC/PLAN.md` and `ENC/cp-pena.l4`, and encodes art. 155 (furto) in full as the worked pattern. **Once g0 is done, `PLAN.md` overrides anything in this section.** In outline, every punishing provision — each caput, and each paragraph that states its own cominação (a qualified or privileged form) — gets:

1. a predicate that its elements are made out, `@export`ed with `@desc` and `@nlg:en`;
2. its **pena cominada**: the species (reclusão / detenção), minimum and maximum, and multa (none, cumulative, or alternative), in `cp-pena.l4`'s types;
3. its **causas de aumento e de diminuição** as the fractions the Code states, which the third phase of art. 68 applies — as predicates plus fractions, not pre-multiplied penalties;
4. where the Code states it for the offence, the **ação penal** (pública incondicionada, condicionada à representação, privada).

## Tests — from the source

Each group writes tests module(s) `cp-gN-…-testes.l4`. The Code prints no worked examples, so expected values come from reading the text: each element present and absent, both sides of every threshold (ages 14, 18, 60, 70; values; durations), each qualified and privileged form, each cause of increase, and the pena cominada of each provision checked against the words of its preceito secundário.

- **A failing assertion is a finding.** Never change an expected value to match what the code computed. If the text and the encoding disagree, find out which is wrong and say so in your notes.
- Assertion count is not quality. Test what the text decides.

## Registers — your part of the pipeline deposit

Under `ENC/registers/parts/`, you own exactly these (the conductor merges them):

1. **`gN-….roadmap.json`** — already written, one unit per article in your scope, every one `deferred`. Move each to `encoded` (with `modules`), `inert` (quoted, not operative — e.g. a definition you fold into a rule, a vigência clause), or `out-of-scope` (with a reason of real length) **as you land it**, not at the end.
   Any unit still `deferred` at the end must carry its specific reason in place of the starting text `NOT YET ENCODED …`.
   Validate: `node /Volumes/transcend/src/l4wt/br-penal/etc/go/lib/register-validate.mjs encoding-roadmap <file> <ENC>/registers/source-bundle.json` — run it from `/Volumes/transcend/src/l4wt/br-penal` so the relative paths resolve.
2. **`gN.forks.json`** — a JSON array of fork **entries** in the shape of `…/etc/go/spec/schemas/fork-register.schema.json` `$defs.entry` (read the schema and `…/spec/schemas/fixtures/fork-register.valid.json`). Id them `F-gN-01`, `F-gN-02`, …. Every ambiguity you met: the readings, the one you took, why, with the text that licenses each. A fork settled by the STF or STJ carries `settled_by`. "None found" is not believable; if you found few, say where you looked.
3. **The P2 sweep is not yours; reading it is.** Three sweep agents research what has happened to the Code since it was printed (STF rulings, binding súmulas, STJ súmulas, prospective amendments) and write `ENC/registers/parts/sweep-a.external-modifications.json` (Parte Geral, arts. 1–120), `sweep-b…` (arts. 121–212) and `sweep-c…` (arts. 213–361). Each is an object `{ "searches": [...], "entries": [...], "dispositions": [...] }` in the shape of `…/etc/go/spec/schemas/external-modifications.schema.json`, with entries `M-sweep-a-01…`.
   **Before you finish, read the sweep file covering your range** (if it is not there yet, check again at the end). For every `binding` entry on your articles, the text was struck, suspended or read down: encode that — a rule-version arm, a fork, or a `REFUSE` where the reading-down leaves no answer — and cite the entry id in a comment. For every `interpretive` entry, open or settle the fork it bears on, and put the entry id in the fork's `settled_by.external_modification`. List every entry id you acted on in your notes file. Encoders write no external-modifications file.
   **Reserved fork ids.** A sweep entry that opens a fork names a reserved id such as `F-sweep-b-03` in its `routing.fork_ids`, and describes the fork in `ENC/registers/parts/sweep-b.forks-proposed.json` (readings, citations, quote). If the article is yours, **create that fork in your own forks file under exactly that reserved id**, with your `site` and your `taken`, so the sweep's reference resolves. A binding entry that strikes, stays or reads down a provision names a proposed `routing.rule_version_arm`; implement it, and record in your notes where it landed.
4. **`ENC/notes/gN.md`** — your record for the reviewer: what you encoded and what you did not; the forks in prose; proposed shared nouns (`PROPOSTO-COMUM`); what `check.sh` prints for your modules, verbatim; open questions for a Brazilian criminal lawyer; and a **PROGRESS** section you update after each Capítulo, so that if your context is compacted you can resume from the file rather than from memory.

## The self-check — read diagnostics, not exit codes

`L4=<L4_BIN> ENC/check.sh ENC cp-gN-` runs your modules and prints errors, satisfied and failed assertions. `l4 run` exits 0 when an `#ASSERT` fails; the script reads the diagnostics. Run it after every Capítulo. Report its numbers, never "it's green".

## Toolchain

`L4_BIN` = `/Users/mengwong/.claude/br-penal-toolchain/l4`, built from `legalese/l4-ide` unstable `73a953821` (sha256 in `SHA256` beside it). Do not use any other `l4`.
Leave `JL4_LIBRARY_PATH` **unset**: the standard library is compiled into the binary and matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`; `L4_BIN nlg --lang en FILE` renders the English glosses.
Useful libraries: `prelude` (always import it), `daydate` for dates.
**Never run `cabal`**, and never edit anything under `/Users/mengwong/src/legalese/l4-ide` or `/Users/mengwong/src/legalese/l4wt/` or `/Volumes/transcend/src/l4wt/`. Do not commit or push anything; the conductor does that.

## When you finish

Reply with: modules written; the roadmap tally (encoded / inert / out-of-scope / deferred); `check.sh`'s TOTAL line verbatim; the number of forks; the sweep entry ids you acted on; any failing assertion you believe is a finding about the Code; and anything the conductor must decide at integration.
