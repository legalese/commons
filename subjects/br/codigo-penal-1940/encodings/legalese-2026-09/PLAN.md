# PLAN — conventions for the L4 encoding of the Código Penal

**Status (2026-09-29): written by the ontology pass (g0), after `cp-dominio.l4`, `cp-pena.l4` and the worked example `cp-g3-furto.l4` were landed and checked.**
Every claim below about what `L4_BIN` does was measured on it (`/Users/mengwong/.claude/br-penal-toolchain/l4`, built from `legalese/l4-ide` unstable `73a953821`) and names the probe or test that showed it.
The probes are in `notes/cp-g0-sondas/`; run any of them with `L4_BIN run` or `L4_BIN nlg --lang en` from that directory. Some fail on purpose: each is the evidence for a trap.
This file overrides the brief's section "The per-offence contract".
Where it and the brief disagree on anything else, the brief wins; tell the conductor.

## 0. The group map (conductor, 2026-09-29, after g0)

g0 wrote this plan for six encoder groups; the conductor split them into **twelve** before launch.
Where the text below says "g1", "g2", "g3", "g4" or "g6", read the group that now owns the article:

| group | prefix | articles | roadmap part | sweep to read |
| --- | --- | --- | --- | --- |
| g1a | `cp-g1a-` | 1–31 | `g1a.roadmap.json` | `sweep-a` |
| g1b | `cp-g1b-` | 32–76 (arts. 33 §§ 2º–4º, 58 p.ú. and 68 included) | `g1b.roadmap.json` | `sweep-a` |
| g1c | `cp-g1c-` | 77–120 | `g1c.roadmap.json` | `sweep-a` |
| g2a | `cp-g2a-` | 121–137 | `g2a.roadmap.json` | `sweep-b` |
| g2b | `cp-g2b-` | 138–154-B | `g2b.roadmap.json` | `sweep-b` |
| g3 | `cp-g3-` | 155–183-A (owns `cp-g3-furto*.l4`) | `g3.roadmap.json` | `sweep-b` |
| g3b | `cp-g3b-` | 184–212 | `g3b.roadmap.json` | `sweep-b` |
| g4a | `cp-g4a-` | 213–249 | `g4a.roadmap.json` | `sweep-c` |
| g4b | `cp-g4b-` | 250–288-A | `g4b.roadmap.json` | `sweep-c` |
| g5 | `cp-g5-` | 289–311-A, 359-I–361 | `g5.roadmap.json` | `sweep-c` |
| g6a | `cp-g6a-` | 312–337-D | `g6a.roadmap.json` | `sweep-c` |
| g6b | `cp-g6b-` | 337-E–359-H | `g6b.roadmap.json` | `sweep-c` |

Your forks file is `registers/parts/<group>.forks.json` and your notes `notes/<group>.md`.
A module may import only its own group's modules; the rule in § 1 about "another group" means any of the twelve.
`check.sh` now also counts **refused** assertions and compares satisfied + failed + refused with the number of `#ASSERT` lines (trap T5 below), and fails on either.

## 1. Files, imports, and what you may touch

| file | owner | what it is |
| --- | --- | --- |
| `cp-dominio.l4` | g0, read-only to all | the shared nouns: `DECLARE` only |
| `cp-pena.l4` | g0, read-only to all | the penalty machinery, and the Parte Geral articles listed in § 9 |
| `cp-g0-pena-testes.l4` | g0 | tests of `cp-pena.l4` |
| `cp-g3-furto.l4`, `cp-g3-furto-testes.l4` | g3 (written by g0) | art. 155, the worked pattern |

Your own files are `cp-gN-<assunto>.l4`, split along the Code's structure (a Capítulo, or a run of related articles), each under about 1,500 lines.
Their tests are `cp-gN-<assunto>-testes.l4`, one per module, importing the module under test.
ASCII in file names; `<assunto>` in Portuguese without accents, e.g. `cp-g2-homicidio.l4`, `cp-g6-peculato-e-concussao.l4`.

Every module opens exactly like this:

```
@lang pt
IMPORT prelude
IMPORT daydate
IMPORT `cp-dominio`
IMPORT `cp-pena`
```

`daydate` only if you use dates; the rest always.
A tests module adds `IMPORT` of its own module.
You may import your own group's modules; **never another group's**: the groups are written at the same time, and a module you import may not exist yet, or may change under you.

`check.sh` prints, per module, errors, assertions satisfied and assertions failed.
Run it as `L4=<L4_BIN> ENC/check.sh ENC cp-gN-`.
Read § 12, trap T5, before you trust its zeros.

## 2. How a penalty is represented, and why

### 2.1 `Duração` — one exact number of months

A length of time is `Duração`, a record with one field, `em meses`: an exact rational number of months, with a year as 12 months and a day as 1/30 of a month.
Build it from the words of the preceito with `anos n`, `meses n` and `dias n`:

| the Code says | write |
| --- | --- |
| "de 1 (um) a 6 (seis) anos" | `anos 1`, `anos 6` |
| "de quinze dias a seis meses" | `dias 15`, `meses 6` |
| "de 20 (vinte) a 40 (quarenta anos)" | `anos 20`, `anos 40` |

Why this and not days, or a years/months/days record:

- L4 numbers are exact rationals: `(1 DIVIDED BY 3) TIMES 3 EQUALS 1` holds, and so does "two thirds of six years is four years" (`cp-g0-pena-testes.l4`, § Duração). The causes of increase and decrease are fractions, and one number keeps the fraction arithmetic exact with no rounding drift.
- `EQUALS` is right on it: `anos 1 EQUALS meses 12` holds. A years/months/days record would compare the components, and one year would not equal twelve months.
- Art. 109 compares a maximum against year thresholds; one number compares directly. Use `` `a duração excede` a b `` and `` `a duração é inferior a` a b ``, or compare `em meses`.
- The 30-day month is the dosimetry convention for taking a fraction of a quantity. The calendar comes in only when a term is served (art. 10): `` `o último dia do prazo` d `o primeiro dia` `` splits the Duração into calendar months and loose days (fork F-g0-03).
- Art. 11 drops fractions of a day. The arithmetic keeps them, and the court's final quantity goes through `` `desprezadas as frações de dia` `` (when in the calculation: fork F-g0-04).

To read one back: `` `em anos, meses e dias` d `` gives `anos completos`, `meses restantes`, `dias restantes`.

### 2.2 `Pena cominada` — one per preceito secundário

```
`pena do art. 155, § 4º` MEANS
    `Pena cominada` WITH
        `espécie` IS `reclusão`
        `mínimo`  IS anos 2
        `máximo`  IS anos 8
        multa     IS `multa cumulativa`
        `além da pena correspondente à violência` IS FALSE
```

- **Always `WITH`, never positional `OF`.** `mínimo` and `máximo` are the same type, so a swapped `OF` type-checks and answers wrongly.
- `espécie`: `reclusão`, `detenção`, or `reclusão ou detenção` — the last only where the preceito itself leaves the species to the judge (arts. 235 § 1º, 306 parágrafo único).
- `multa`: "e multa" is `multa cumulativa`; "ou multa" is `multa alternativa`; "ou multa, ou ambas as penas" (art. 180 § 3º) is `multa alternativa ou cumulativa`; nothing is `sem multa`. "além da multa" (arts. 158 § 3º, 321 parágrafo único) is `multa cumulativa`.
- A preceito that still prints an amount in réis (arts. 129 § 5º, 153, 154, 299) or in minimum wages (art. 244) is read through Lei nº 7.209/1984, art. 2º (sweep entries M-sweep-a-07 and M-sweep-b-07, both binding): "São canceladas, na Parte Especial do Código Penal …, quaisquer referências a valores de multas, substituindo-se a expressão multa de por multa" (the "Vide Lei nº 7.209" markers V25, V26 and V32 sit at arts. 153, 154 and 299; art. 129 § 5º has none). Write the member its conjunction names, and say so in a comment and in your notes. That law's text is outside the source bundle; its art. 2º was checked on 2026-09-29 through a search whose results quote it. g2a meets one (art. 129 § 5º), g2b two (arts. 153, 154) and g5 one (art. 299).
- M-sweep-a-07 reads art. 2º as reaching art. 244's "de uma a dez vezes o maior salário mínimo vigente no País" too; g4a cites it there.
- `além da pena correspondente à violência`: TRUE where the preceito adds "além da pena correspondente à violência" or "sem prejuízo da (pena) correspondente à violência". A separate paragraph saying the same (arts. 146 § 2º, 147-A § 2º) is its own rule; mark the preceito TRUE and cite both.
- Art. 146-A caput is the one preceito with no custodial penalty ("Pena - multa"). Use `` `Preceito secundário` ``'s constructor `somente pena de multa` there. Everywhere else a preceito is a `Pena cominada`; a function that must take any preceito (g1c's prescrição) takes `Preceito secundário`, whose other constructor wraps a `Pena cominada`.
- A preceito that points elsewhere ("Pena - a cominada à falsificação ou à alteração", art. 304; "aplica-se a pena do artigo anterior", art. 126 parágrafo único) is a function returning the pena it points at. One that changes a limit is shape 2 in § 2.2.1.
- "se o fato não constitui crime mais grave" is a condition of the preceito, not a field. Whether the fact is a graver crime needs the whole Code, so take it as an input finding (`delegated-to-fact` in your forks), never as FALSE.

#### 2.2.1 The shapes a preceito takes, and how each is written

Every row was checked against the source line it names (line numbers in `SOURCE/codigo-penal-1940.txt`).
Each has an illustration that runs, in `cp-g0-pena-testes.l4` § `As formas de um preceito secundário`; those are shapes, not encodings of the articles, which are their groups'.

| shape | the Code (article, line) | write |
| --- | --- | --- |
| 1. the species left to the judge | "Pena - reclusão ou detenção, de um a três anos, e multa." (art. 306 parágrafo único, 2129); "é punido com reclusão ou detenção, de um a três anos" (art. 235 § 1º, 1710) | `` `espécie` IS `reclusão ou detenção` ``. Never pick one: a single species silently forces reclusão's regimes. |
| 2. a paragraph that changes one bound | "O máximo da reclusão é elevado a doze anos e multa" (art. 290 parágrafo único, 2028; caput 2027: "de dois a oito anos") | `` `a pena cominada com outro máximo` (`pena do art. 290, caput`) (anos 12) `` — minimum two years, the caput's. `` `a pena cominada com outro mínimo` `` is the twin. Never a fresh `Pena cominada` literal: it retypes the bound the paragraph did not touch, and the two drift. |
| 2a. a paragraph that changes the fine's conjunction | "As penas aplicam-se cumulativamente e em dobro" (art. 146 § 1º, 920; caput 918: "ou multa") | `` `a pena cominada com outra multa` pc `multa cumulativa` ``, and the doubling as a cause (§ 2.3), applied by `` `a pena cominada com a causa` ``. |
| 3. fractions of increase up to double or triple | "Aumenta-se a pena de metade até o dobro" (art. 359-I § 1º, 2576); "até o dobro … e até o triplo" (art. 135-A parágrafo único, 838); "triplicada" (art. 135 parágrafo único, 834); "aplica-se em triplo a pena" (art. 141 § 2º, 896) | a cause, § 2.3: `` entre metade `o dobro` ``, `` `até` `o triplo` ``, `` fixa `o triplo` ``. The fraction is what is ADDED: `o dobro` is 1 and `o triplo` is 2. "de metade até o dobro" on 3 to 8 years gives 4 years 6 months to 16 years, not 24. |
| 4. the violence's penalty as well | "…, além da pena correspondente à violência." (art. 359-L, 2613; also arts. 359-J, 359-M, 359-P); "sem prejuízo da pena correspondente à violência" (art. 230 § 2º, 1659) | `` `além da pena correspondente à violência` IS TRUE ``; where a separate paragraph says it (arts. 146 § 2º, 147-A § 2º, 161 § 2º, 208 and 209 parágrafo único, 329 § 2º, 351 § 2º), `` `a pena cominada com a pena correspondente à violência` pc ``. Never a number: the range is untouched, and the other penalty is the other offence's, computed by that offence's rule. |
| 5. the fine's limits | "A multa, prevista em cada tipo legal de crime, tem os limites fixados no art. 49 e seus parágrafos deste Código." (art. 58, 276) | never a number in your preceito. `` `a multa aplicada cabe na pena cominada (art. 58)` m pc sm `` checks a fine against it: FALSE under `sem multa`, else art. 49's limits. Printed réis and salário amounts: the bullet above. |
| 6. a fine, or both | "Pena - detenção, de um mês a um ano, ou multa, ou ambas as penas." (art. 180 § 3º, 1376) | `` multa IS `multa alternativa ou cumulativa` ``. |
| 6a. no fine, among neighbours that have one | "Pena - reclusão, de oito a quinze anos.." (art. 159, 1196, the double stop is the source's; its §§ 1º–3º likewise have none) | `` multa IS `sem multa` ``. Read each preceito's own words; do not copy a neighbour's. |
| 7. a preceito that depends on the fact | "de um a cinco anos, e multa, se o documento é público, e … de um a três anos, e multa, … se o documento é particular" (art. 299, 2097; art. 305, 2122 likewise); "de três a seis anos, e multa, no caso de dolo, ou detenção, de seis meses a dois anos, no caso de culpa" (art. 254, 1812) | a function from the fact to a `Pena cominada`: `BRANCH` on the fact, one complete `Pena cominada` per arm, each with its own species and multa. |

A cause changes only the custodial range: `` `a pena cominada com a causa` `` leaves `multa` as it was, because `multa` is a conjunction, not a number.
Where a paragraph's words reach the fine too ("As penas aplicam-se … em dobro", art. 146 § 1º, plural), whether the number of dias-multa is also doubled is a fork for that article's encoder: record the readings and take one, and cross-refer to F-g0-28, which records only that the shared machinery does not decide it.

### 2.3 Causes of increase and decrease — ranges, never a chosen number

A cause is `` `Causa de aumento ou de diminuição` ``: a direction and a `` `Fração da causa` ``.

| the Code says | write |
| --- | --- |
| "aumenta-se de metade" | `` `causa de aumento` (fixa metade) `` |
| "diminuída de um a dois terços" | `` `causa de diminuição` (entre `um terço` `dois terços`) `` |
| "aumentada de 1/3 (um terço) até a metade" | `` `causa de aumento` (entre `um terço` metade) `` |
| "aumentada até o dobro" | `` `causa de aumento` (`até` `o dobro`) `` |
| "aplica-se a pena em dobro", "é duplicada" | `` `causa de aumento` (fixa `o dobro`) `` |
| "em triplo", "triplicada" | `` `causa de aumento` (fixa `o triplo`) `` |
| "de sexta parte", "de quarta parte", "da terça parte" | `` fixa `um sexto` ``, `` fixa `um quarto` ``, `` fixa `um terço` `` |
| "de 1/3 (um terço) ao dobro" | `` entre `um terço` `o dobro` `` |
| "de metade até o dobro" (art. 359-I § 1º) | `` entre metade `o dobro` `` — at most double, never `o triplo` |
| "até o triplo" (art. 135-A parágrafo único) | `` `até` `o triplo` `` |

The fractions are fractions of increase: `o dobro` is 1 (the penalty doubles) and `o triplo` is 2.
"até X" states only the ceiling; its floor is `NOTHING` and is treated as 0, the infimum (fork F-g0-09).

Each cause is a named constant beside its paragraph, and a separate predicate says whether it applies:

```
@ref CP art. 155, § 1º
GIVETH A `Causa de aumento ou de diminuição`
@nlg:en the increase of one half for theft during the night-time rest
`aumento do art. 155, § 1º` MEANS `causa de aumento` (fixa metade)

@ref CP art. 155, § 1º
GIVEN f IS A `Fato de furto`
GIVETH A BOOLEAN
@nlg:en the night-time increase applies
`incide o aumento do art. 155, § 1º` f MEANS ...
```

Never pre-multiply a penalty. The machinery applies a cause:

- to a quantity the judge has reached: `` `o intervalo com a causa` q c `` gives the range the judge chooses in; `` `o intervalo com as causas` q cs `` applies several in cascade (fork F-g0-10);
- to a pena cominada: `` `a pena cominada com a causa` pc c `` and `` `a pena cominada com as causas` pc cs `` give its outer limits, an increase at its largest fraction on the maximum and a decrease at its smallest — the "pena em abstrato" arts. 109 ff. read;
- where the judge fixes the quantity inside the range, Súmula 443 STJ (M-sweep-a-40) asks for concrete reasons, not a count of the causes: nothing the machinery can compute, and nothing it pre-empts;
- the attempt: `` `diminuição pela tentativa (art. 14, parágrafo único)` ``, or `` `a pena cominada à tentativa (art. 14, parágrafo único)` pc ``. Where your article punishes the attempt as the consummated crime (the "tentar" offences, arts. 352, 359-L, 359-M), do not apply it.

Art. 68, parágrafo único (the judge may apply only one of several Parte Especial causes) is g1b's. Your functions return every cause that applies; they never choose.

### 2.4 What the judge decides stays with the judge

A range stays a range; a power stays a list of options; an open standard ("pequeno valor", "relevante valor social ou moral", "motivo fútil") is an input finding with the Code's words in its name.
See `` `as opções do juiz pelo art. 155, § 2º` ``: it returns the three options and never picks one.

## 3. Naming scheme

All names are Portuguese, the Code's own words wherever it has them, in backticks when they have spaces.

| thing | pattern | art. 155 example |
| --- | --- | --- |
| the case record | `Fato de <crime>` | `` `Fato de furto` `` |
| its checkbox enums | `Circunstância do <crime>`, `Natureza da coisa subtraída`, ... | `` `Circunstância do furto` `` |
| the offence, exported | `crime de <crime> (art. N)` | `` `crime de furto (art. 155)` `` |
| consummated / attempted | `<crime> consumado (art. N, caput; art. 14, I)`, `<crime> tentado (art. N, caput; art. 14, II)` | `` `furto consumado (art. 155, caput; art. 14, I)` `` |
| an element or limb | the Code's words, then the citation | `` `coisa alheia móvel (art. 155, caput e § 3º)` ``, `` `com emprego de chave falsa (art. 155, § 4º, III)` `` |
| a qualified form, as a predicate | `<crime> qualificado do art. N, § X` | `` `furto qualificado do art. 155, § 4º` `` |
| a qualified form, as a value | `<crime> qualificado (art. N, § X)` | `` `furto qualificado (art. 155, § 5º)` `` |
| a pena cominada | `pena do art. N[, § X]` | `` `pena do art. 155, caput` ``, `` `pena do art. 155, § 4º-A` `` |
| the pena for a case, exported | `a pena cominada ao <crime> (art. N)` | `` `a pena cominada ao furto (art. 155)` `` |
| a cause, as a value | `aumento do art. N, § X[, inciso]`, `diminuição do art. N, § X` | `` `aumento do art. 155, § 4º-C, II` `` |
| whether it applies | `incide o aumento do art. N, § X` | `` `incide o aumento do art. 155, § 11` `` |
| the causes for a case, exported | `as causas de aumento do <crime> (art. N)` | `` `as causas de aumento do furto (art. 155)` `` |
| the outer limits with causes, exported | `os limites da pena do <crime> com as causas (art. N)` | `` `os limites da pena do furto com as causas (art. 155)` `` |
| a privileged form's options | `as opções do juiz pelo art. N, § X` | `` `as opções do juiz pelo art. 155, § 2º` `` |
| the ação penal, where the article states it | `a ação penal do art. N` | art. 155 states none |

Every rule that is exported, or that another module will call, has a **prefix** name (§ 8.2 says why).

Enum constructors are global to the module and everything it imports. Two enums cannot share a constructor name: the use is ambiguous (`cp-g0-sonda-construtor-2.l4`, "There are multiple definitions for the identifier reclusão").
Before you name a constructor, search `cp-dominio.l4` and `cp-pena.l4` for it: `fraude`, `morte`, `reclusão`, `tutor`, `gestante` and the like are taken.
`A` alone is not a usable type name (`cp-g0-sonda-construtor-1.l4`: "unexpected A").

## 4. `§` headings and `@ref`

One module's heading tree follows the Code:

```
§ `Título II — Dos crimes contra o patrimônio`
§§ `Capítulo I — Do furto`
§§§ `Art. 155 — Furto`
§§§§ `Art. 155, § 4º — furto qualificado`
§§§§§ `Art. 155, § 4º-A`
```

Use the Code's heading words after the dash where it has them.
`@ref` goes on every rule, above its `GIVEN` (or above `GIVETH` for a constant), in the form `@ref CP art. 155, § 4º, II`.
Several places: `@ref CP art. 155, caput; art. 14, II`.
Name the wording's source where it changed recently: `@ref CP art. 155, § 4º (redação da Lei nº 15.397/2026)`.
An authority that settles a reading goes in the `@ref` too: `@ref CP art. 155, § 1º; STJ, Tema 1087 (REsp 1.890.981/SP, 3ª Seção, j. 25.5.2022)`.
`@ref` above `GIVEN` attaches to the rule: measured with `l4 ast` (`cp-g0-sonda-ref.l4`), where it lands in the `Decide`'s own annotation.
Quote the article's words in a comment above the rule, copied from `SOURCE/codigo-penal-1940.txt`, never retyped.

## 5. The per-offence contract

For every punishing provision — each caput, and each paragraph that states its own preceito — write:

1. the case record, `Fato de <crime>`, embedding `cp-dominio` records and adding the facts only your article names (§ 6);
2. the predicate that the elements are made out, `@export`ed with `@desc` on its `GIVEN` and `@nlg:en`, split into consummated and attempted where an attempt is possible (art. 14 via `cp-pena`);
3. its pena cominada, a `Pena cominada` constant named `pena do art. N, § X`, with a test that compares it with the preceito's words (§ 11);
4. each cause of increase and decrease as a constant plus an `incide ...` predicate, and an exported function listing those that apply;
5. an exported function giving the pena cominada that applies to a case, choosing among the qualified forms present (the heaviest, fork F-g0-18) and gated by vigência (§ 10);
6. where the article states it, the ação penal as a `Ação penal` value from `cp-pena` (`ação penal pública incondicionada`, `... condicionada à representação do ofendido`, `... condicionada à requisição do Ministro da Justiça`, `ação penal privada`).
   Where the article is silent, write nothing: the general rule is art. 100, g1c's.

`cp-g3-furto.l4` does all six (it has no ação penal, since art. 155 states none; arts. 181–183 are g3's).

## 6. Nouns, and reaching another Título's concepts

`cp-dominio.l4` has: `Pessoa`, `Relação do agente com a vítima`, `Condição da vítima`, `Vínculo com a administração pública` (the facts art. 327 reads), `Grupo criminoso`, `Agente`, `Vítima`, `Coisa`, `Documento`, `Meio empregado`, `Resultado`, `Circunstância do fato`, `Fato`.
Its header gives the membership test; its comments say what each record is for.

- **Checkbox facts are lists of enums.** L4 has no record-update syntax, so a record of twenty booleans makes every test spell out twenty flags. A list names only what happened: `` `meios empregados` IS LIST fraude ``; `EMPTY` means none. Test with `elem`.
- **Ages are never stored.** Use `` `a idade em anos completos` p d ``, `` `menor de` n p d ``, `` `maior de` n p d ``, `` idoso p d ``, `` `criança` p d ``, `` adolescente p d `` from `cp-pena`, with the date the provision names: the fact's date (`` f's fato's `data do fato` ``), or the sentence's where it says "na data da sentença" (arts. 65 I, 115). The arguments are a `Pessoa` and a `DATE`, so they cannot be swapped silently. Forks F-g0-01, F-g0-06, F-g0-08, F-g0-24 record how each threshold is read.
- **A victim that may be a legal person** is a `MAYBE Vítima`; `NOTHING` means the one who suffered the crime is not a natural person.
- **The grade of an injury** is the `Resultado` the medical report gives (fork F-g0-07). g2a encodes art. 129 §§ 1º–2º from the findings; nobody else calls it.
- **A concept another group defines** is reached through the noun, never through the other group's rule. Art. 157 needs "coisa alheia móvel": g3 reads `Coisa`'s `alheia` and `móvel`, as art. 155 does. Art. 312 needs "funcionário público": g6 encodes art. 327 over `Vínculo com a administração pública`, and anyone else who needs the status reads those same facts, with a comment naming art. 327 and a note for the conductor.
- **A noun you need that is not there**: declare it in your module with `-- PROPOSTO-COMUM: <why other groups will need it>`, and list it in your notes. The conductor hoists it. Do not edit `cp-dominio.l4`.

## 7. The case record and its tests

- Build test cases from named parts, one line per case: a builder function whose parameters are all of different types (so a swapped argument does not type-check), plus named `Agente`, `Vítima`, `Coisa` and `Fato` values. `cp-g3-furto-testes.l4`, § Casos de base, is the model: `` `um furto` e ag v c pv ns cs fa cq ``.
- Construct records over several lines, one field per line. On one line, `LIST x, next IS ...` swallows the comma into the list (`cp-g0-sonda-lista-virgula.l4`, "unexpected IS"; parenthesised, `cp-g0-sonda-lista-virgula-2.l4`), and a nested `WITH` swallows the outer record's later fields. Parenthesise a list on a one-line record: `` `meios empregados` IS (LIST fraude), resultados IS EMPTY ``.

## 8. Where the English glosses go — measured

The probes are `cp-g0-sonda-nlg-posicao.l4`, `cp-g0-sonda-nlg-posicao-2.l4`, `cp-g0-sonda-nlg-lacunas.l4`, `cp-g0-sonda-mixfix-a/b/c.l4` and `cp-g0-sonda-campos.l4.txt`, run with `L4_BIN nlg --lang en`.
`nlg` renders only what a directive exercises, so a module with no `#EVAL` or `#ASSERT` renders nothing; check your glosses through your tests module's rendering.

### 8.1 Placements

| where | result |
| --- | --- |
| rule herald on its own line after `GIVETH`, immediately above the definition | **attaches** |
| rule herald above `GIVEN` | **silently dead**: no diagnostic, rule renders bare |
| rule herald trailing the definition line | **silently dead** |
| herald with `@export`, `@ref`, `@desc` above `GIVEN` and the herald after `GIVETH` | **attaches** |
| `DECIDE … IF` with the herald above `DECIDE` | **attaches** |
| constant (`name MEANS value`) with a herald and **no** `GIVETH` line | **silently dead** |
| constant with a `GIVETH` line and the herald below it | **attaches** |
| record field herald on its own line **below** the field | **attaches**, including below a field line that ends in a `-- comment` |
| record field herald trailing the field's own line | **does not reach the field** (it goes to the type) |
| enum constructor herald below, or trailing | **attaches** |
| parameter herald trailing its `GIVEN` line | describes the parameter; the rule still renders bare |
| untagged `@nlg` beside `@nlg:en` | `--lang en` takes `:en`; no flag or `--lang pt` takes the untagged one |

### 8.2 Mixfix: the gloss does not survive import

| rule shape | in its own module | from a module that imports it |
| --- | --- | --- |
| prefix, `` `nome` a b `` | attaches | **attaches** |
| parameter-first mixfix, ``a `supera` b`` | attaches | **bare**, `` `_ supera _` with 3 and 2 `` |
| keyword-first mixfix, `` `de` x `até` y `` | **bare** | **bare** |

No diagnostic in any bare case.
So: **every rule that is exported, or that another module calls, has a prefix name.**
Mixfix is fine for a test-local helper whose gloss nobody needs.

### 8.3 Slots

`%x%` in a herald is replaced by the argument only for a **one-word** parameter of a **prefix** rule.
A multi-word backticked parameter (`%o agente%`) prints literally, and in mixfix rules slots print the parameter's name, not the argument (`cp-g0-sonda-nlg-lacunas.l4`).
Write glosses as plain sentences with no slots; the renderer appends "with <arguments>".
A literal `%` in a gloss rendered correctly in the one probe that tried it (`cp-g0-sonda-nlg-lacunas.l4`, "50% applies"), but `%` is the slot delimiter; write "fifty per cent" rather than find out otherwise.

## 9. Parte Geral articles encoded in `cp-pena.l4`

| article | extent | where |
| --- | --- | --- |
| art. 10 | whole | § Art. 10 — `o último dia do prazo` |
| art. 11 | whole | § Art. 11 — `desprezadas as frações de dia`, `desprezadas as frações da moeda` |
| art. 14 | whole | § Art. 14 — `crime consumado (art. 14, I)`, `crime tentado (art. 14, II)`, the attempt's reduction |
| art. 32 | whole | § Art. 32 — `Espécie de pena` |
| art. 33 | **caput and § 1º only** | § Art. 33 — the species and their regimes; §§ 2º–4º are g1b's |
| art. 43 | whole | § Art. 43 — `Pena restritiva de direitos` |
| art. 49 | whole | § Art. 49 — `Multa aplicada` and its limits |
| art. 53 | whole | § Art. 53 — `Pena cominada` and its limits test |
| art. 58 | **caput only** | § Art. 58 — `a multa aplicada cabe na pena cominada (art. 58)`; the parágrafo único (the substitutive multa) is g1b's |

Art. 68's third phase is machinery here (§ 2.3), cited to art. 68; the article is g1b's.
In `registers/parts/g1a.roadmap.json` arts. 10, 11 and 14, and in `g1b.roadmap.json` arts. 32, 43, 49 and 53, are `encoded` with `cp-pena.l4`; in `g1b.roadmap.json` arts. 33, 58 and 68 stay `deferred` with a reason saying exactly what is left for g1.
`Ação penal` (the enum) and the age helpers are in `cp-pena.l4` too; they encode no article.

## 10. Vigência: which facts your text answers for

The source is the text as amended through Lei nº 15.517/2026, and much of the Parte Especial was re-written in 2025–2026.
A harsher law does not reach an earlier fact, and the text it replaced is not in the source.
So, for each article whose penalty was re-written by a law whose vigência you can establish:

- the definition of the crime answers for any date if its words did not change;
- every rule yielding a penalty checks the fact's date against the vigência and, before it, returns a named refusal (`REFUSE`, in return position, never stored in a value):

```
@ref CP art. 155 in the wording before Lei nº 15.397/2026 — not encoded
GIVEN a IS A TYPE
GIVETH AN a
@nlg:en the wording of art. 155 before Lei 15.397 of 2026 is not encoded
`a redação do art. 155 anterior à Lei nº 15.397, de 2026, não está codificada` MEANS
    REFUSE "a redação do art. 155 anterior à Lei nº 15.397, de 2026 (em vigor em 4.5.2026), não está codificada"
```

- a paragraph a later law **added** simply does not apply before its vigência: that is the law's own answer, an ordinary condition, not a refusal (art. 155 § 10 before 23.9.2026).

Vigência dates come from the sweep file covering your range (§ 0): each sweep checked every 2025–2026 amending law's vigência clause and records it as a search. The Senado XML gives each law's publication date, and the law's own final article says when it takes effect.
Measured for art. 155: Lei nº 15.397/2026, art. 4º, in force on publication, DOU 4.5.2026; Lei nº 15.517/2026, in force on publication, DOU 23.9.2026; Lei nº 15.358/2026, in force 25.3.2026 (notes/g0.md lists the searches).

## 11. Tests

- One tests module per module. Expected values come from the text, worked by hand, never from the code.
- Every pena cominada is compared with its preceito's words: `` #ASSERT `pena do art. 155, § 4º` EQUALS `reclusão, de` 2 `a` 8 `anos, e multa` ``.
- Both sides of every threshold: ages on the birthday and the day before; counts at N and N−1; the vigência date and the day before.
- Every qualified form present and absent; every cause present and absent; each cause's fraction asserted against the words.
- Several forms at once, and a cause on the attempt, where the article allows them.
- **Assert every gate directly** as well as through the rules behind it (§ 12, T5).
- Before you trust a clean run, break the code once and watch a test fail: g0's run mutated eleven things one at a time (the § 1º fraction, the Tema 1087 condition, the § 4º IV count, idoso's threshold, art. 10's first day, the vigência boundary, § 9º's privilege, the larger factor of a cause; then, for § 2.2.1, a one-bound change that also moved the other bound, art. 58 admitting a fine under `sem multa`, and `o triplo` as a multiplier) and each was caught — the vigência one only after the gate got its own assertion (T5).

## 11a. The P2 sweep and reserved fork ids

Three sweep agents write `registers/parts/sweep-{a,b,c}.external-modifications.json` and `sweep-{a,b,c}.forks-proposed.json`; the brief says what each encoder owes them.
Two points learned doing it for art. 155:

- **A reserved id replaces yours.** Where a sweep entry reserves a fork id (`routing.fork_ids`) for a question you have already written as `F-gN-…`, rename your fork to the reserved id, take the sweep's reading ids where they fit, and put the entry id in `settled_by.external_modification` (if an authority settled it) or `cross_refs`. g0 did this for four forks: F-g0-15 → F-sweep-b-17, F-g0-16 → F-sweep-b-19, F-g0-17 → F-sweep-b-18, F-g0-22 → F-sweep-b-21. It created F-sweep-b-20 new.
- **Checking the references.** `register-validate.mjs fork-register <your forks, wrapped> <sweep file>` checks your references into the sweep, and also reports every fork the sweep reserved that your file does not contain. The second list is mostly other encoders' forks: read it for the ids on your own articles, and ignore the rest until the conductor merges.

## 12. Traps met, each with the probe that showed it

**T1. A mixfix keyword segment that is also a parameter name breaks the definition.**
Portuguese makes this easy: "a", "e", "de", "o" are words of the preceito and favourite one-letter names.
`` `reclusão, de` a `a` b `anos, e multa` `` with parameters `a` and `b` gives "The names in a type signature must match those in the definition … the corresponding name in the definition is a", then errors at every call.
Name parameters with more than one letter (`` `o mínimo em anos` ``), and no parameter anywhere in the module the same as a keyword segment (`cp-g3-furto-testes.l4`, first run: 48 errors; standalone, `cp-g0-sonda-segmento-a.l4`, and the repair, `cp-g0-sonda-segmento-a-2.l4`).

**T2. Heralds on mixfix rules are lost on import, and on keyword-first mixfix always.** § 8.2; `cp-g0-sonda-mixfix-a/b/c.l4`.

**T3. A herald above `GIVEN`, trailing the definition line, or on a constant with no `GIVETH` is dead, with no diagnostic.** § 8.1.

**T4. A genitive used as an unparenthesised operand of a mixfix operator breaks a multi-line boolean chain, and the error points at the next line.**
`` (pc's `mínimo` `excede` q) `` followed by a line starting `AND` gives "unexpected AND" on that line (`cp-g0-sonda-not-4.l4`, `cp-g0-sonda-not-6.l4`).
`` ((pc's `mínimo`) `excede` q) `` parses (`cp-g0-sonda-not-5.l4`).
It is not `NOT`'s fault: `NOT (a)` then `AND b` parses (`cp-g0-sonda-not-1.l4`).
Parenthesise every genitive beside a mixfix keyword, or use a prefix function.

**T5. A plain `#ASSERT` whose expression REFUSES is a Warning, and `check.sh` counts it nowhere.**
It prints "assertion refused" at `DiagnosticSeverity_Warning`; `check.sh` counts Error lines and "assertion failed".
Measured by mutating art. 155's vigência gate from `AT LEAST` to `GREATER THAN`: the test for the first day of vigência refused, and `check.sh` printed `0 errors, 109 satisfied, 0 failed` and exited 0, one satisfied fewer than before and nothing else.
Guard every gate with an assertion that fails loudly (`` #ASSERT `o fato está sob a redação codificada do art. 155` `o furto no dia da vigência` ``), and compare your satisfied count with your `#ASSERT` count (`grep -c '^#ASSERT'`).
`check.sh` now has that "refused" column and an `asserts` column, and fails on a refusal or on an assertion that produced no verdict (conductor, 2026-09-29; control: a module with one satisfied, one failed and one refused assertion exits 1). Still assert every gate directly: a refusal inside a rule that no assertion reaches is invisible to any counter.

**T6. `not` is not a function.** Write `NOT` (`cp-g3-furto.l4`, first check: "I could not find a definition for the identifier not").

**T7. `NOT` in the middle of a chain: parenthesise its operand when more follows on the next line.**
`` "x" ... NOT a `` then `AND b` did evaluate as `(NOT a) AND b` (`cp-g0-sonda-not-2.l4`), but g0 parenthesised every such `NOT` rather than depend on it.

**T8. Record construction on one line swallows commas.** § 7; `cp-g0-sonda-lista-virgula.l4`.

**T9. `add months` clamps.** `` `add months` (YMD 2026 1 31) 1 `` is 28 February 2026 (`cp-g0-sonda-add-months.l4`). `o último dia do prazo` handles this for art. 10; do not add months to a date yourself.

**T10. `IMPORT prelude` prints a warning that a copy of `prelude` in `~/.local/share/jl4/libraries` is shadowed.**
The embedded copy is the one used, which is what the brief wants (`JL4_LIBRARY_PATH` unset). It is noise, not a defect.
