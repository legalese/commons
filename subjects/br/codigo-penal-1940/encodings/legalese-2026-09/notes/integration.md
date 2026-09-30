# Integration log

Three narrow integration agents append here in turn.
The general rules are `notes/INTEGRATION-BRIEF.md`'s: the tree stays green after every step, no logic or expectation changes, record everything.

Evidence convention: "green" means `check.sh` over every group the step touched gave exactly the baseline in `scratchpad/integ/baseline-per-shard.txt` (modules, errors, satisfied, failed, refused, asserts), with no UNACCOUNTED row.
The tree has no `#EVAL`, so the assertions are the only verdicts; an answer that moved on a tested case would show as a failed assertion.

## integ-shared (2026-09-30): the 19 duplicated names of the shared layer

Scope: the three duplicated types, the six cause and heaviest-penalty helpers, the seven law-date constants, and three other rules.
The 63 constructor collisions are the next agent's.

### Step 3 — `cp-vigencias.l4` (DONE, green)

New module `cp-vigencias.l4`: `@lang pt`, IMPORT prelude and daydate, and nothing else.
It holds one constant per law whose vigência more than one group declared.
Every copy gave the same date, so there was no finding to stop on:

| constant | date | copies removed |
| --- | --- | --- |
| `a vigência da Lei Complementar nº 225, de 2026` | 9.1.2026 | cp-g3-comum, cp-g6a-comum |
| `a vigência da Lei nº 10.741, de 2003` | 1.1.2004 | cp-g1b-circunstancias, cp-g4a-assistencia-familiar |
| `a vigência da Lei nº 11.106, de 2005` | 29.3.2005 | cp-g2b-sequestro-escravidao, cp-g4a-dignidade-sexual-geral |
| `a vigência da Lei nº 12.015, de 2009` | 10.8.2009 | cp-g3-comum, cp-g4a-dignidade-sexual-geral |
| `a vigência da Lei nº 12.737, de 2012` | 2.4.2013 | cp-g2b-segredos, cp-g5-falsidade-documental |
| `a vigência da Lei nº 14.994, de 2024` | 10.10.2024 | cp-g2a-homicidio, cp-g2b-honra |
| `a vigência da Lei nº 15.358, de 2026` | 25.3.2026 | cp-g1c-efeitos-e-reabilitacao, cp-g2b-constrangimento-ameaca, cp-g3-comum |

Each removed block was replaced by a one-line comment pointing at `cp-vigencias.l4`, and each of those twelve modules gained `IMPORT \`cp-vigencias\``.
Modules that read a constant through another module needed nothing: `IMPORT` is transitive (probe: a module importing B, which imports C, reads C's constant; both assertions satisfied).
Each constant's `@ref` gathers every copy's sources; the comment above it names the modules that read it, checked against the call sites.
The copies' English glosses were article-specific ("the day art. 147-C came into force"); the hoisted gloss names the law.

Evidence: check.sh over cp-g1b-, cp-g1c-, cp-g2a-, cp-g2b-, cp-g3-, cp-g4a-, cp-g5-, cp-g6a- after the edit (run started after the last module write, 11:16:38):
g1b 389, g1c 486, g2a 509, g2b 507, g3 578, g4a 422, g5 467, g6a 442 satisfied; 0 errors, 0 failed, 0 refused, 0 unaccounted; every row equal to the baseline.

**Finding, not changed: three readings of Lei nº 9.983/2000's first day.**
The law entered into force "noventa dias após a data de sua publicação" (DOU 17.7.2000); whether the count includes the publication day decides between 15 and 16.10.2000 (S-sweep-c-15).
- cp-g5-comum and cp-g6a-funcionario-publico refuse a fact of 15.10.2000 and agree on every other day (g5: `o primeiro dia possível …` 15.10, `o primeiro dia certo …` 16.10; g6a: `a véspera …` 14.10, `a vigência certa …` 16.10).
- cp-g2b-segredos declares `a vigência da Lei nº 9.983, de 2000` as 15.10.2000 and treats that day as in force.
The names differ, so nothing collides; the disagreement is on one day and belongs to the conductor.

### Step 2 — the cause and heaviest-penalty helpers, into `cp-pena.l4` (DONE, green)

Every copy was read and diffed by body, not by name.
Two new sections in `cp-pena.l4`, before `Ação penal`: "As causas que incidem (art. 68, terceira fase)" and "A pena mais grave entre as formas presentes (fork F-g0-18)"; the header lists them.

| hoisted rule | copies it replaced (identical bodies) |
| --- | --- |
| `a causa, se incide` (BOOLEAN, cause → MAYBE cause) | cp-g2a-homicidio, cp-g3b-comum, cp-g5-comum, cp-g6a-comum; cp-g2b-comum's `a causa se incide` (no comma) |
| `as causas que incidem` (LIST OF MAYBE cause → LIST) | cp-g2a-homicidio, cp-g2b-comum, cp-g3b-comum, cp-g5-comum, cp-g6a-comum |
| `a mais grave de duas penas cominadas` (larger maximum, then larger minimum; F-g0-18) | `a mais grave das penas` in cp-g2b-comum, cp-g3-furto, cp-g5-comum; `a mais grave de duas penas cominadas` in cp-g2a-homicidio, cp-g3b-comum; `a mais grave de duas penas` in cp-g3-comum; `a mais grave das duas penas cominadas` in cp-g6a-comum |
| `a mais grave das penas cominadas` (base, LIST → the left fold of the rule above) | cp-g2a-homicidio, cp-g3b-comum, cp-g6a-comum; `a mais grave de todas` in cp-g2b-comum; `a mais grave das penas` (list form) in cp-g3-comum |
| `a pena, se presente` | cp-g5-outras-falsidades, cp-g5-estado-democratico |
| `as penas que incidem` | cp-g5-outras-falsidades; `as penas presentes` in cp-g5-estado-democratico |

Each removed definition left a one-line pointer; the encoders' comments above it stay where they were.
Call sites renamed (code lines only): `a causa se incide` → `a causa, se incide` (g2b, 15 sites); `a mais grave das penas` → `a mais grave de duas penas cominadas` (cp-g3-furto's local fold, cp-g5-comum's `a mais grave dentre`); `a mais grave de todas` → `a mais grave das penas cominadas` (cp-g2b-honra, cp-g2b-sequestro-escravidao); `as penas presentes` → `as penas que incidem` (cp-g5-estado-democratico, 2 sites).

**Kept separate, renamed, because they are different functions under the same name:**
- cp-g4b-comum's `a causa, se incide` returns a LIST (`LIST c` or `EMPTY`), not a MAYBE, and g4b's modules `append` it. Renamed `a causa em lista, se incide` (g4b, 12 sites, 2 of them in cp-g4b-comum-testes).
- cp-g3-comum's `as causas que incidem` takes a LIST OF `Causa candidata` (built by `quando incide`), not a LIST OF MAYBE. Renamed `as causas candidatas que incidem` (g3, 10 sites).
- cp-g1b-concurso-de-crimes' `a mais grave das penas (art. 70)` compares `Pena aplicada a um crime` values by species, then length (F-g1b-27): art. 70's "penas cabíveis", not F-g0-18. Untouched, as the brief expected.

**Left in place, not colliding (WHERE-local or single-module):** WHERE-local folds and cause helpers in cp-g3-furto (`a mais grave de todas`, `a causa se incide`), cp-g4a-dignidade-sexual-geral (`a causa se incide`), cp-g3-roubo and cp-g3-extorsao (`a mais grave`); and cp-g5-comum's `a mais grave de todas as penas` (LIST → MAYBE, g5 only).
A WHERE-local definition may shadow an imported name of the same spelling: probe, a local `o dobro de` inside `f` wins inside `f`, the imported one is used outside, both assertions satisfied.
**Except when the local definition is recursive and has the imported rule's type:** its recursive call is then ambiguous. The full-tree run after this step caught it: cp-g5-moeda-falsa's WHERE-local `as penas que incidem` (art. 292) gave "There are multiple definitions for the identifier `as penas que incidem` and I do not have sufficient information to make a choice between them" at its two recursive calls (2 errors; its tests 94 errors, 88 UNACCOUNTED). Its body was identical to the hoisted rule, so the local copy was deleted and the call resolves to cp-pena's; the module then checked clean. The other WHERE-local helpers listed above have names the hoist did not take, so they cannot meet this.
Evidence: `fulltree.sh` after the step (169 modules, cp-vigencias included) gave every group its baseline except g5, where cp-g5-moeda-falsa was red as described above: `TOTAL (169 modules) errors=96 satisfied=5387 failed=0 refused=0 asserts=5475 unaccounted_modules=1`, the 96 errors and 88 missing verdicts all in that module and its tests.
After the repair, check.sh over cp-g5- gave 16 modules, 0 errors, 467 satisfied, 0 failed, 0 refused, 467 asserts, no UNACCOUNTED: the baseline.
Further near-duplicates of the attempt machinery, not in this scope and not colliding: `as causas com a da tentativa` (cp-g6a-comum) = `as causas, com a da tentativa se tentado` (cp-g4b-comum); `os limites da pena com as causas e a tentativa` (cp-g3-comum) = `os limites com as causas e a tentativa` (cp-g5-comum). Same bodies, different names; a later tidy could hoist them.

### Step 1 — the three duplicated types (DONE, green)

**`Elemento subjetivo`: hoisted into `cp-dominio.l4`.**
cp-g2a-comum and cp-g4b-comum declared the same enum, `dolo` | `culpa` (the court's finding under art. 18, as input); one declaration now lives in cp-dominio, with g4b's glosses, and both copies are gone (pointer comments left).
cp-g1a-crime's `Elemento subjetivo` was a different type with the same name: a record of the facts art. 18 classifies (`o agente quis o resultado`, `o agente assumiu o risco de produzi-lo`, `modalidades de culpa`), whose classification `a modalidade do crime (art. 18)` has a third member, `nem dolo nem culpa`.
It keeps its shape, renamed `Relação do agente com o resultado` (g1a, 8 sites), with a comment at the declaration.
The constructors `dolo` and `culpa` now reach every module; cp-g1a-erro-testes has a mixfix parameter named `culpa`, which a probe showed shadows the constructor cleanly (3 of 3 satisfied).
For a later wiring pass: g2a's and g4b's rules take the dolo/culpa finding as input, while g1a's art. 18 derives it; nothing connects them yet.

**`Execução do crime`: hoisted into `cp-dominio.l4`, and g6b's `Execução` unified onto it.**
cp-g2b-comum's `Execução do crime` and cp-g6b-comum's `Execução` were the same record, two booleans with the same field names (`execução iniciada`, `consumação impedida por circunstâncias alheias à vontade do agente`), which are exactly cp-pena's `crime tentado (art. 14, II)` parameters.
One declaration now lives in cp-dominio under g2b's name; both copies are gone; g6b's 72 uses of the bare type name `Execução` became `` `Execução do crime` `` (10 files; every bare token in g6b was the type, none in a comment).
cp-g1a-crime's `Execução do crime` was a different record: `até onde chegou` (an enum with a payload that separates art. 15's desistência from arrependimento) plus art. 17's and Súmulas 145 STF / 567 STJ's facts.
It keeps its shape, renamed `Curso da execução` (g1a, 22 sites in cp-g1a-crime, cp-g1a-concurso and their tests).

**The other spellings of the stage of execution: NOT unified; left for the next agent.**
They cannot go onto the hoisted record by renames: they are four-member enums, and "consumada" versus "abandonada" is not a function of the record's two booleans without the offence's own elements, so mapping one to the other is a logic change.

| type | module | members |
| --- | --- | --- |
| `Etapa da execução` | cp-g3b-comum | `execução consumada`, `execução interrompida por circunstâncias alheias à vontade do agente`, `execução abandonada pelo agente`, `execução não iniciada` |
| `Estágio da execução` | cp-g5-comum | `execução completa`, `execução interrompida por circunstâncias alheias à vontade do agente`, `execução abandonada pela vontade do agente`, `execução não iniciada` |
| `Estágio da execução` | cp-g6a-casos (test support) | `executado`, `interrompido por circunstâncias alheias`, `abandonado pelo agente`, `não iniciado` |

g3b and g5 compute art. 14 from them identically (`consumado` = the other elements AND the first member; `tentado` = the other elements AND `crime tentado` over "not the fourth member", "the first", "the second"), but the members do not mean the same thing:
g3b's first member includes "any result it names", and its third covers the agent who "gave it up, or prevented the result" (both limbs of art. 15);
g5's first member is "the agent carried the conduct through to the end", and its third is "gave it up of the agent's own will", which its comment calls art. 15's desistência only.
An arrependimento eficaz (conduct completed, result prevented) is therefore the third member for g3b and arguably the first for g5.
Unifying the two enums is one rename of two constructors, and no current test would move, but it would make one input mean two things; that is a ruling, not a mechanical step.
Meanwhile the next agent will meet two constructor collisions here (`execução interrompida por circunstâncias alheias à vontade do agente`, `execução não iniciada`, g3b and g5), and one TYPE collision the inventory does not list: `Estágio da execução` is declared by both cp-g5-comum and cp-g6a-casos.
The inventory was generated over non-test modules without the `*-casos.l4` fixtures; `names.py` over every non-test module adds `Estágio da execução` and fourteen test-fixture names (`Ana`, `Beatriz`, `Carla`, `Davi`, `Davi como agente`, `em junho de 2026`, `em outubro de 2026`, `nenhum vínculo`, `o particular`, `um cargo público`, `um fato`, `um fato em`, `um fato em junho`, `um fato em outubro`).
cp-g3-furto's loose execution fields (brief § 2) were not touched.

**`Imputação do resultado`: two concepts, NOT hoisted; g4b's renamed.**
cp-g1a-crime's is art. 13's causation OUTCOME (four members: imputable; not, the conduct is no cause; not, the omission is not relevant; not, a supervening cause, but the earlier acts are).
cp-g4b-comum's is an art. 19 INPUT: how an aggravating result stands to the agent (caused at least culposamente without being wanted; wanted or its risk taken on, fork F-g4b-02; not caused even culposamente).
g4b's is renamed `Imputação do resultado agravador (art. 19)` (3 sites), with a comment at the declaration. For a later wiring pass: g1a also encodes art. 19 (`o agente responde pelo resultado que agrava especialmente a pena (art. 19)`) from its own inputs.

### Step 4 — the other same-named rules (DONE, green)

**`a execução foi iniciada`** — cp-g1a-crime's reads g1a's record (now `Curso da execução`); cp-g5-comum's reads g5's `Estágio da execução` enum (the "tentar" offences, arts. 359-L and 359-M). Different functions: g5's renamed `a execução foi iniciada, segundo o estágio da execução` (3 sites). g3b's WHERE-local of the same name is local and untouched.

**`o agente tem com a vítima a relação`** — the same body (`elem r` over the victim's `relações com o agente`, FALSE for no natural-person victim) over two different records: cp-g1b-circunstancias' `Crime em julgamento` (art. 61) and cp-g3-disposicoes-gerais' `Fato contra o patrimônio` (arts. 181–183). Hoisting one rule over `MAYBE Vítima` would change every call's arguments, which is not a rename; kept separate, g3's renamed `o agente tem com a vítima a relação (arts. 181 a 183)` (13 sites, all in cp-g3-disposicoes-gerais).

### Step 4, continued — art. 327: FOUR readings, only one of them the owner's; NOT unified (finding for the conductor)

g6a's owner is `funcionário público para os efeitos penais (art. 327)` v `a data do fato`, in `cp-g6a-funcionario-publico.l4`, which imports only prelude, daydate, cp-dominio and cp-pena, so any group may import it.
The copies were read against it, and none is the same function, so none was redirected to it: that would change answers, which the brief forbids.

The source (`subjects/br/codigo-penal-1940/source/codigo-penal-1940.txt`, line 2255): "§ 1º - Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal, e quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de atividade típica da Administração Pública. (Incluído pela Lei nº 9.983, de 2000)".
The readings differ on WHEN each limb of § 1º counts:

| rule | module | caput | § 1º, paraestatal | § 1º, contracted company |
| --- | --- | --- | --- | --- |
| `funcionário público para os efeitos penais (art. 327)` v d (OWNER) | cp-g6a-funcionario-publico | always | always | only under Lei 9.983 (FALSE to 14.10.2000, REFUSE on 15.10.2000, TRUE from 16.10.2000) |
| `o agente é funcionário público (art. 327)` ag d | cp-g5-comum | always | only under Lei 9.983 (same gate) | only under Lei 9.983 |
| `funcionário público para os efeitos penais (art. 327, caput e § 1º)` v | cp-g2b-comum | always | always | always (no date argument) |
| `funcionário pelos fatos do art. 327` v | cp-g6b-justica-exercicio-arbitrario-a-desobediencia (art. 351 § 4º; F-g6b-14) | always | always | always (no date argument) |

So a paraestatal employee's fact before 15.10.2000 is a funcionário for g6a, g2b and g6b and not for g5; a contracted-company worker's fact before 15.10.2000 is one for g2b and g6b and not for g6a or g5.
Which reading is right is the conductor's (and, for § 1º's first limb, a question of what the source's "Incluído pela Lei nº 9.983" marker covers); redirecting the copies to the owner is then a logic change to make deliberately, with tests at 14, 15 and 16.10.2000.
g6a-comum's own `o agente é funcionário público (art. 327)` a (on an `Ato do agente`) calls the owner and is g6a's.

Rename, to separate the two same-named rules: cp-g5-comum's becomes `o agente é funcionário público (art. 327, § 1º desde a Lei nº 9.983)` (see step 4 evidence).
Measured: L4 resolves same-named rules by argument type (probe: `f` on a NUMBER in one import and on a STRING in another, both calls satisfied), and reports "There are multiple definitions for the identifier" only when the types coincide. These two differ in arity, so they would not have collided in the composer; the rename is for the reader and for the rendered prose, which would otherwise print one name for two readings.

### Final full-tree run (integ-shared)

Steps 1 and 4 were checked by this run, which started at 12:55:02, after the last `.l4` write (12:54:42); no `.l4` was edited after it.
`fulltree.sh` now includes the `cp-vigencias` prefix.
Every group equal to its baseline row: g0 124, g1a 276, g1b 389, g1c 486, g2a 509, g2b 507, g3 578, g3b 331, g4a 422, g4b 533, g5 467, g6a 442, g6b 411; cp-dominio, cp-pena and cp-vigencias 0 assertions, 0 errors.

    TOTAL (169 modules) errors=0 satisfied=5475 failed=0 refused=0 asserts=5475 unaccounted_modules=0

169 = the baseline's 168 modules plus `cp-vigencias.l4`.
`names.py` over the non-test, non-`casos` modules (the inventory's scope) now reports 61 duplicated names, down from 82: the 19 of this scope, plus `dolo` and `culpa`, which the `Elemento subjetivo` hoist took with it. No new duplicate appeared.

### Left for the next agents

- **Constructor collisions (next agent):** the 61 names above. Two of them touch the stage of execution (`execução interrompida por circunstâncias alheias à vontade do agente`, `execução não iniciada`, g3b and g5): read Step 1's table before renaming them, since unifying those enums is a ruling, not a rename.
- **A type collision the inventory misses:** `Estágio da execução` in cp-g5-comum and cp-g6a-casos. Whether `*-casos.l4` modules go into the composer decides whether it matters; the same applies to the fourteen fixture names listed in Step 1.
- **Stage of execution:** four representations remain (cp-dominio's `Execução do crime`, g1a's `Curso da execução`, g3b's `Etapa da execução`, g5's and g6a-casos' `Estágio da execução`); cp-pena's `crime tentado (art. 14, II)` reads three booleans; cp-dominio's record carries two of them under the same names (the third is each offence's elements), and the other three representations need a conversion.
- **Art. 327:** four temporal readings of § 1º (Step 4, continued). The copies were NOT redirected to g6a's owner rule, because every redirect changes answers for some facts before 16.10.2000. For the conductor.
- **Lei nº 9.983/2000's first day:** cp-g2b-segredos takes 15.10.2000 as in force; g5 and g6a refuse that day (Step 3).
- **Wiring, not done (brief § 6):** g2a's and g4b's dolo/culpa input versus g1a's art. 18 classification; g4b's `Imputação do resultado agravador (art. 19)` versus g1a's art. 19 rule.
- **Near-duplicates outside this scope, not colliding:** the attempt helpers listed at the end of Step 2; WHERE-local copies of the heaviest-penalty fold and the cause helper in cp-g3-furto and cp-g4a-dignidade-sexual-geral.


### Art. 327 ruling (g6a, 2026-09-30)

**The ruling (conductor):** art. 327's caput answers for any date; § 1º — BOTH limbs — refuses by name for a fact before Lei nº 9.983/2000's vigência (16.10.2000), and 15.10.2000 refuses as the uncertain day (S-sweep-c-15). Recorded as fork F-g6a-23.

**Owner rule changed** (`cp-g6a-funcionario-publico.l4`): `equiparado a funcionário público (art. 327, § 1º)` now reads the two § 1º facts first and then `o art. 327, § 1º, na redação da Lei nº 9.983, de 2000, rege o fato` (TRUE from 16.10.2000; refused on 15.10.2000; refused before, as `o art. 327, § 1º, anterior à Lei nº 9.983, de 2000, não está codificado`). A person with neither § 1º fact is FALSE on any date and never reaches a refusal; an official under the caput is TRUE on any date. The Lei nº 9.983 gate for provisions that law ADDED (`a Lei nº 9.983, de 2000, vigia na data do fato`: FALSE before, refused on 15.10.2000) is unchanged.

**Copies redirected to the owner, local readings deleted:**
- g2b: `funcionário público para os efeitos penais (art. 327, caput e § 1º)` deleted from `cp-g2b-comum`; its 4 call sites (`cp-g2b-domicilio` 1, `cp-g2b-honra` 2, `cp-g2b-sequestro-escravidao` 1) call `funcionário público para os efeitos penais (art. 327)` with the fact's date.
- g5: `o agente é funcionário público (art. 327, § 1º desde a Lei nº 9.983)` deleted from `cp-g5-comum`; 6 call sites (`cp-g5-moeda-falsa` 2, `-falsidade-documental`, `-fraudes-em-certames`, `-outras-falsidades`, `-papeis-publicos`) and 8 test lines call the owner with the agent's vínculo.
- g6b: `funcionário pelos fatos do art. 327` deleted from `cp-g6b-justica-exercicio-arbitrario-a-desobediencia`; its 1 call site (art. 351 § 4º) calls the owner with the fact's date.
- g2b's `cp-g2b-segredos`: its own `a vigência da Lei nº 9.983, de 2000` (15.10.2000, taken as in force) is deleted; art. 153 § 1º-A and its ação penal read g6a's `a Lei nº 9.983, de 2000, vigia na data do fato`, with the facts before the gate so a fact without the § 1º-A elements or without prejuízo is answered on 15.10.2000.
Each module that now calls g6a's rule has `IMPORT `cp-g6a-funcionario-publico``; no name collides: each of those modules checks with 0 errors below.

**Assertions whose expectation moved** (flipped, not deleted; each carries a comment saying what it was):

| test module | assertion | was | now |
| --- | --- | --- | --- |
| cp-g6a-peculato-a-concussao-testes | `crime de peculato (art. 312)` `a apropriação pelo terceirizado na véspera` (14.10.2000) | NOT | REFUSED BECAUSE "a redação do art. 327, § 1º, anterior à Lei nº 9.983, de 2000 (em vigor em 16.10.2000), não está codificada" |
| cp-g5-moeda-falsa-testes | art. 327 status of `o empregado da paraestatal` on 14.10.2000 | NOT | REFUSED BECAUSE (same message) |
| cp-g5-moeda-falsa-testes | art. 327 status of `o empregado da paraestatal` on 1.1.1999 | NOT | REFUSED BECAUSE (same message) |
| cp-g2b-segredos-testes | `crime de divulgação de segredo (art. 153)` `o vazamento no dia da lei` (15.10.2000) | TRUE | REFUSED BECAUSE "não está estabelecido se a Lei nº 9.983, de 2000, entrou em vigor em 15.10.2000 (contagem da LC nº 95/1998) ou em 16.10.2000" |
| cp-g2b-segredos-testes | `a vigência da Lei nº 9.983, de 2000` EQUALS YMD 2000 10 15 | TRUE | the constant is deleted; now `#ASSERT REFUSED `a Lei nº 9.983, de 2000, vigia na data do fato` (YMD 2000 10 15)` |

Reworded, same verdict: cp-g5-moeda-falsa-testes, the status of `o empregado da paraestatal` on 15.10.2000 stays REFUSED; its BECAUSE now carries the owner's message instead of g5's.

**Post-2000 twins, so the logic stays tested:** g6a `a apropriação pelo terceirizado no dia` and (new) `a apropriação pelo empregado de paraestatal no dia` (16.10.2000, crime); g5's existing 16.10.2000 and June 2026 lines; g2b-segredos (new) `o vazamento no dia seguinte` (16.10.2000, crime) and the gate TRUE on 16.10.2000.
**Added under the ruling (g6a):** the paraestatal limb refused on 14.10.2000; an official (caput) answered and a private person with neither link FALSE on 14.10.2000; the new gate asserted on 14, 15 and 16.10.2000.

**check.sh, foreground, after the change:**

    g2b  TOTAL (13 modules)                                 0       509       0       0     509
    g5   TOTAL (16 modules)                                 0       467       0       0     467
    g6a  TOTAL (13 modules)                                 0       449       0       0     449
    g6b  TOTAL (10 modules)                                 0       411       0       0     411

g2b +2 and g6a +7 are the added assertions; g5 and g6b equal their baselines. Every other assertion in the four groups kept its expectation: the table above is every assertion that failed or refused after the change and before the flips.

**Mutation control on the owner rule** (scratch copies; the harness now also copies `cp-vigencias.l4`, which `cp-g6a-comum` imports since integration — without it the control showed one import error): unmutated control 142/142 satisfied, 0 errors; § 1º ungated — caught (3 failed); earlier dates FALSE instead of refused — caught (3 failed); gate boundary exclusive — caught (3 refused); only the contracted limb gated, the old reading — caught (1 failed).

**Left for the owning groups (other groups' fork parts were not edited):** F-g6b-14's rationale still says art. 327 "is not imported" and names the deleted reader; its site anchor now resolves to the comment at art. 351 § 4º that records the deletion. F-g5-01's rationale still says the § 1º limbs count "only for a fact under Lei nº 9.983/2000" (before, they now refuse), and its note asks for a cross-check assertion that the redirect makes unnecessary; its anchor resolves to `cp-g5-comum.l4`'s header comment, which now records the deletion. Both taken readings (§ 1º reaches beyond Capítulo I, and beyond Título XI) still hold. g6a's fork F-g6a-22 no longer lists art. 327 § 1º, and F-g6a-23 records the ruling.
