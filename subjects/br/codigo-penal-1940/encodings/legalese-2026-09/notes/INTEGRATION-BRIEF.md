# Integration brief: making twelve groups one encoding

Written by the conductor on 2026-09-30, for the integrator agent.

ENC is this directory.
Read `BRIEF.md` and `PLAN.md` (§§ 0, 1, 2, 6, 8 and 12) first; every convention there still holds.
The binary is `/Users/mengwong/.claude/br-penal-toolchain/l4`; leave `JL4_LIBRARY_PATH` unset.
Never run `cabal`, never commit, and never push.
Your scratch directory is `/private/tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/452e2526-ee93-4276-9db4-448804aa5ac6/scratchpad/integrator/`.
**Do not read `~/.claude/br-penal-oracle/`.** It holds the independent test cases, which are still to be scored against your result.

## Where things stand

Twelve encoder groups (g1a–g6b) and the ontology pass (g0) have written 168 modules.
Each group's modules check on their own: `check.sh` over all of them reports 0 errors and 5,455 satisfied out of 5,455 (g1b and g1c have since added a few).
While they worked, no group could import another's modules, so they share nothing except `cp-dominio.l4` and `cp-pena.l4`, and they have DUPLICATED what they needed.
No module yet imports all of them. `cp-codigo-penal.l4`, the composer, does not exist; the pipeline's sidecar names it as the encoding's main module.

## What to do, in this order

Keep everything green after EVERY step: run `L4=… ENC/check.sh ENC <prefix>` for each group you touched, and read the numbers.
Satisfied must never fall, and failed, refused and UNACCOUNTED must stay 0.
Never edit an expected value to make a test pass. If a hoist changes an answer, the two copies were not the same function: stop, record it in `notes/integration.md`, and keep them separate under distinct names.

### 1. Hoist the duplicated helpers into `cp-pena.l4`

Measured by grep on 2026-09-30:
- `as causas que incidem` is defined in g2a, g2b, g3, g3b, g5 and g6a;
- `a causa se incide` is in g2b;
- the heavier-penalty helpers appear as `a mais grave das penas` in g2b, g3, g5 and cp-g3-furto, `a mais grave de duas penas (cominadas)` in g2a, g3 and g3b, `a mais grave das duas penas cominadas` in g6a, `a mais grave das penas cominadas` in g2a, g3b and g6a, `a mais grave de todas (as penas)` in g2b and g5, and `a mais grave das penas (art. 70)` in g1b, whose art. 70 version may differ ON PURPOSE.

Compare the definitions. Where copies agree, keep ONE in `cp-pena.l4`, citing F-g0-18 (the "heaviest" measure), and delete the copies.
Every module's import of `cp-pena` already exists, so call sites need only a rename where the names differ.
Where copies disagree, find out why before unifying.

### 2. Hoist the shared nouns into `cp-dominio.l4`

Every `PROPOSTO-COMUM` comment marks a candidate: `grep -n PROPOSTO-COMUM cp-g*.l4` found 28 on 2026-09-30. The known clusters are:

- **The stage of the execution (art. 14).** The same enum is spelled five ways: g1a `Execução do crime`, g2b `Execução do crime`, g3b `Etapa da execução`, g5 `Estágio da execução`, g6b `Execução`; `cp-g3-furto` carries loose fields. Make one; `cp-pena`'s art. 14 rules should read it.
- **`Elemento subjetivo`** (dolo or culpa): g1a, g2a, g4b.
- **Reincidência and prior convictions:** g1b's `Condenação anterior`, `Natureza da infração anterior`, `Espécie aplicada`; g1c's `Natureza da infração`, `Condenação`, `o dia em que a pessoa completa os anos`. g1c reads as inputs what g1b computes.
- **`Razão da condição do sexo feminino`** (art. 121-A § 1º, g2b), needed by g2a, art. 129 § 13 and art. 92 II.
- **`com o emprego de arma`** (g2b), **`Profissão de saúde`** (g4b), **`Fim para o qual a vítima está confiada ao agente`** (g4a; art. 136 reads the same facts), **`Cargo do ofendido`** (g2b).
- **`Entidade da administração pública`** (g6a) replaces `cp-dominio`'s boolean `ocupa cargo em comissão ou função de direção ou assessoramento`, whose gloss folds in art. 327 § 2º's list. On the Code's list, an autarquia is NOT reached (F-g6a-02). Check every reader of the old boolean.
- **`Grupo criminoso`** lacks a member for associação criminosa (art. 288); g3 used a boolean instead (F-g3-14).

A noun that is genuinely local stays local. Say so in your notes rather than hoisting it.

### 3. One reading of art. 327

g6a owns art. 327 and exports `funcionário público para os efeitos penais (art. 327)`, which takes the vínculo and the date of the fact.
g2b has its own copy, `…(art. 327, caput e § 1º)` in cp-g2b-comum, and g6b's art. 351 § 4º reads the facts directly (F-g6b-14).
Replace both with g6a's rule. Cross-group imports are allowed now; the parallel-writing reason for forbidding them is over.
Prefer moving art. 327 into a small shared module, e.g. `cp-g6a-funcionario-publico.l4` imported as-is, over making g2b import all of g6a.

### 4. The composer, `cp-codigo-penal.l4`

Write it as `@lang pt`, IMPORT `prelude`, `cp-dominio`, `cp-pena`, then every non-test module in Code order (Parte Geral, then Títulos I–XII), and nothing else: no rules, no directives.
Then run `l4 check cp-codigo-penal.l4`. This is the first time all modules meet, and it is where the collisions surface.

- Two enums sharing a constructor name give "multiple definitions for the identifier". g2b alone listed `coação`, `abuso`, `calúnia`, `difamação`, `injúria`, `entrar`, `permanecer`, `governador`, `prefeito` and the eight 149-A verbs. Rename the less central one with a qualifying word, update its module and tests, and keep a list.
- Two rules with the same name are the duplicates of steps 1–3 that you missed.

Repeat until `l4 check cp-codigo-penal.l4` reports 0 errors. Then run `check.sh` over `cp-` and confirm the whole tree is still green.

### 5. Roadmap titles

The conductor's mechanical extraction took the WRONG source line for many unit titles: often the line before the article, not its nomen juris.
Encoders corrected some of these by hand (g1a 3, g2a 6, g6a 3, g6b ~16, g5 7, g3 6, g1b 2, g4b 1).
Re-derive every title in `registers/parts/*.roadmap.json` from the source: the rubric line directly above each article, where the article has one.
Where your derivation differs from an encoder's correction, keep the encoder's and note the difference. Where an article has no rubric (e.g. arts. 144–145), use the article's own first words and say so.
Validate every part with `node /Users/mengwong/src/legalese/l4wt/br-penal/etc/go/lib/register-validate.mjs encoding-roadmap <part> <ENC>/registers/source-bundle.json`, run from `/Users/mengwong/src/legalese/l4wt/br-penal`.
If you renamed or moved modules, update each unit's `modules` paths too; they must resolve.

### 6. Do NOT

- Do not change any rule's logic, any fork's reading, or any test's expectation, except the mechanical renames above.
- Do not wire the cross-group inputs the encoders left as findings (g1c's reincidência from g1b, art. 73 to g1a's art. 20 § 3º, and the like). List them in your notes instead; wiring them is a later pass.
- Do not touch `registers/*.json` outside the roadmap parts, or anything under `notes/` except your own `notes/integration.md`.

## Report

Write `notes/integration.md`:
- every hoist, with the copies it replaced and the check that shows the answers did not move;
- every rename, and why;
- the composer's final `l4 check` output;
- the full-tree `check.sh` TOTAL, verbatim;
- what you left undone, and why.

Then reply with those last two lines and the list of renames.
