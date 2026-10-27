# Lei nº 8.213/1991 (Planos de Benefícios da Previdência Social): the keel

This is the shared notes file for the encoding of Lei nº 8.213, de 24 de julho de 1991, written by the keel agent `pb-g0` before four part agents (`pb1` to `pb4`) each encode one contiguous piece of the text.
The keel owns no provision: the Law has no interpretation section, so it writes the shared vocabulary and the Portuguese naming conventions only.
Its modules are `pb-core.l4` (the vocabulary) and `pb-core-tests-vocabulario.l4` (its tests).

**The source.**
The text is `lei-8213-1991.pt.txt`, a plain-text rendering made by a converter script from the compilation that Planalto publishes (`https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm`, retrieved 2026-10-21, 1766 lines).
It is not the official text and it is not marked up, and nothing in this encoding is verified against the official text.
Planalto's own footer says that only the text published in the Diário Oficial da União is official (line 1765).
Superseded wording that Planalto strikes through is kept in the file as `⟦STRUCK: ... ⟧` and is never encoded.
The amendment notes (`(Redação dada pela Lei nº ...)`) are part of the line you quote and are not provisions.
Regulations, other laws and amending acts that the text cites are not among the inputs: where a rule depends on one, its outcome is a plain input with a comment.

**The seat** that the pieces write for: a person insured under Brazil's Regime Geral de Previdência Social, or a dependant of one, asking whether they qualify for a benefit, how much it is, from when and for how long, and what they must do or declare.
The keel writes no seat layer and no `@export`.

**The target** is the stable `l4` 1.6.98 (a `main` build).
Everything below that says "compiles" or "accepted" was run on that binary on 2026-10-24; what was taken from `dialects.md` and not re-run is said to be so.

## Vocabulary

Every name in this table is declared in `pb-core.l4` and is reserved: a piece must not declare a second one with the same name, and must not call one of its own fields, inputs or rules after a constructor.
Types are in the first block, constructors under their type, then the constants and helpers.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Unidade de prazo` | enumeration | the unit of a time limit | arts. 49, I, a; 15, II; 103 |
| `em dias` | constructor of `Unidade de prazo` | a limit counted in days ("90 (noventa) dias") | art. 49, I, a |
| `em meses` | constructor of `Unidade de prazo` | a limit counted in calendar months ("12 (doze) meses") | art. 15, II |
| `em anos` | constructor of `Unidade de prazo` | a limit counted in calendar years ("10 (dez) anos") | art. 103 |
| `Prazo` | record: `quantidade` (NUMBER), `unidade` (`Unidade de prazo`) | a time limit | arts. 15, 49, 74, 103 and others |
| `Categoria de segurado` | enumeration | the category of an insured person | art. 11, I, II, V, VI, VII; art. 13 |
| `segurado empregado` | constructor of `Categoria de segurado` | art. 11, I ("como empregado", alíneas a to j) | art. 11, I |
| `segurado empregado doméstico` | constructor of `Categoria de segurado` | art. 11, II | art. 11, II |
| `segurado contribuinte individual` | constructor of `Categoria de segurado` | art. 11, V (alíneas a to h) | art. 11, V |
| `segurado trabalhador avulso` | constructor of `Categoria de segurado` | art. 11, VI | art. 11, VI |
| `segurado especial` | constructor of `Categoria de segurado` | art. 11, VII | art. 11, VII |
| `segurado facultativo` | constructor of `Categoria de segurado` | art. 13 | art. 13 |
| `Sexo` | enumeration | the sex on which ages and lengths of service turn | arts. 29 § 9, 48, 51, 52, 53, 56, 97, 98 |
| `masculino` | constructor of `Sexo` | "homem", "do sexo masculino" | arts. 48, 51 |
| `feminino` | constructor of `Sexo` | "mulher", "do sexo feminino" | arts. 48, 52 |
| `Regime de previdência` | enumeration | a scheme of social security the Law names | arts. 9, 12, 94 |
| `Regime Geral de Previdência Social` | constructor of `Regime de previdência` | the RGPS | art. 9, I |
| `Regime Facultativo Complementar de Previdência Social` | constructor of `Regime de previdência` | the optional complementary scheme | art. 9, II |
| `regime próprio de previdência social` | constructor of `Regime de previdência` | the scheme of servants and military, which excludes a person from the RGPS | arts. 12, 94 |
| `Parentesco com o segurado` | enumeration | how a dependant is related to the insured | art. 16 |
| `cônjuge` | constructor of `Parentesco com o segurado` | spouse | art. 16, I |
| `companheiro ou companheira` | constructor of `Parentesco com o segurado` | partner in a stable union | art. 16, I and § 3 |
| `filho` | constructor of `Parentesco com o segurado` | child | art. 16, I |
| `enteado` | constructor of `Parentesco com o segurado` | step-child, treated as a child under conditions | art. 16 § 2 |
| `menor sob tutela` | constructor of `Parentesco com o segurado` | minor under guardianship, treated as a child under conditions | art. 16 § 2 |
| `menor sob guarda judicial` | constructor of `Parentesco com o segurado` | minor in judicial custody, treated as a child under conditions | art. 16 § 2 |
| `pai ou mãe` | constructor of `Parentesco com o segurado` | parent ("os pais") | art. 16, II |
| `irmão` | constructor of `Parentesco com o segurado` | sibling | art. 16, III |
| `Classe de dependente` | enumeration | the class of dependants | art. 16 § 1 |
| `classe do inciso I do art. 16` | constructor of `Classe de dependente` | spouse, partner, child | art. 16, I |
| `classe do inciso II do art. 16` | constructor of `Classe de dependente` | parents | art. 16, II |
| `classe do inciso III do art. 16` | constructor of `Classe de dependente` | sibling | art. 16, III |
| `Parte` | enumeration | the persons and bodies that act or must act; the party of a regulative rule | arts. 14, 22, 125-A |
| `segurado` | constructor of `Parte` | the insured as a party (no article, so it never meets the input `o segurado`) | art. 10 |
| `dependente` | constructor of `Parte` | the dependant as a party | art. 10 |
| `empresa` | constructor of `Parte` | the firm, including what art. 14 sole paragraph equates to it | art. 14, I and sole paragraph |
| `empregador doméstico` | constructor of `Parte` | the household employer | art. 14, II |
| `INSS` | constructor of `Parte` | Instituto Nacional do Seguro Social | arts. 29-A, 125-A |
| `Previdência Social` | constructor of `Parte` | the social security system as the Law's actor ("a Previdência Social ajuizará ação regressiva") | arts. 22, 92, 120 |
| `Segurado` | record: `categoria`, `sexo`, `idade em anos completos` | the insured person | art. 10 |
| `Dependente` | record: `parentesco`, `idade em anos completos`, `emancipado`, `inválido`, `deficiência intelectual ou mental ou deficiência grave`, `dependência econômica comprovada` | a dependant, with the facts art. 16 reads | art. 16 |
| `Prestação` | enumeration | a benefit or service of the RGPS | art. 18; arts. 80, 124, III |
| `aposentadoria por invalidez` | constructor of `Prestação` | art. 18, I, a (also "aposentadoria por incapacidade permanente", F-3) | art. 18, I, a |
| `aposentadoria por idade` | constructor of `Prestação` | art. 18, I, b | art. 18, I, b |
| `aposentadoria por tempo de contribuição` | constructor of `Prestação` | art. 18, I, c (arts. 52 to 56 and 97 call it "por tempo de serviço", F-3) | art. 18, I, c |
| `aposentadoria especial` | constructor of `Prestação` | art. 18, I, d | art. 18, I, d |
| `auxílio-doença` | constructor of `Prestação` | art. 18, I, e (also "auxílio por incapacidade temporária", F-3) | art. 18, I, e |
| `salário-família` | constructor of `Prestação` | art. 18, I, f | art. 18, I, f |
| `salário-maternidade` | constructor of `Prestação` | art. 18, I, g | art. 18, I, g |
| `auxílio-acidente` | constructor of `Prestação` | art. 18, I, h | art. 18, I, h |
| `pensão por morte` | constructor of `Prestação` | art. 18, II, a | art. 18, II, a |
| `auxílio-reclusão` | constructor of `Prestação` | art. 18, II, b | art. 18, II, b |
| `serviço social` | constructor of `Prestação` | art. 18, III, b | art. 18, III, b |
| `reabilitação profissional` | constructor of `Prestação` | art. 18, III, c | art. 18, III, c |
| `abono de permanência em serviço` | constructor of `Prestação` | not on art. 18's live list (inciso I, i, is revoked) but named by arts. 80 and 124, III | arts. 80, 124, III |
| `Duração do benefício` | enumeration | how long a benefit lasts | arts. 42, 60, 71, 77 § 2 |
| `por prazo certo` | constructor of `Duração do benefício`, field `o prazo` (`Prazo`) | a fixed period | arts. 71, 77 § 2, V, b |
| `até uma data certa` | constructor of `Duração do benefício`, field `a data` (DATE) | until a date the facts fix | art. 77 § 2, II |
| `enquanto persistir a condição que o justifica` | constructor of `Duração do benefício` | while a condition lasts (incapacity, invalidity) | arts. 42, 60 |
| `vitalícia` | constructor of `Duração do benefício` | for life | art. 77 § 2, V, c, 6 |
| `Valores de referência` | record: `salário mínimo`, `limite máximo do salário-de-contribuição`, `limite mínimo do salário-de-contribuição` (NUMBERs, reais per month) | the three amounts the Law uses and does not fix | arts. 22, 29 § 2, 33, 48 § 4 |
| `YMD` | helper: `YMD y m d`, a DATE | the one date shim (the stable prelude has none) | toolchain, not the Law |
| `a data da Lei nº 8.213` | constant, DATE | 24 July 1991, the date in the title | title (line 5) |
| `a data de publicação da Lei nº 8.213 no Diário Oficial da União` | constant, DATE | 25 July 1991, the Diário Oficial da União edition that Planalto's footer names (F-1) | art. 155; the footer (line 1765) is read, not quoted |
| `a data de entrada em vigor da Lei nº 8.213` | constant, DATE | the date of publication | art. 155 |
| `prazo em dias`, `prazo em meses`, `prazo em anos` | helpers: NUMBER to `Prazo` | build a time limit | as `Prazo` |
| `o dia em que termina` `o prazo` `contado de` `a data de partida` | helper: `Prazo` and DATE to DATE | the last day on which an act is still in time | arts. 15, 49, 74, 103 |

## Naming conventions

All identifiers, `§` headings and any `@desc` text are Brazilian Portuguese, spelled properly, accents kept.
Accents compile in backticked type, constructor, field and rule names, in `§` headings, in `@ref` text and in `-- src:` quote lines (measured on 1.6.98; `srcrefs.py` accepted them).
Write no `@lang` line and no `@nlg:xx`.
Comments and notes are English, with an English gloss beside any Portuguese they quote.

### A rule

- A rule name is a backticked Portuguese phrase that **begins with the citation of the provision it encodes**: `` `art. 48 — o segurado tem direito à aposentadoria por idade` ``, `` `art. 15, inciso II — último dia da manutenção da qualidade de segurado` ``, `` `art. 77, § 2º, V, c — duração da pensão do cônjuge` ``.
  The dash is the em dash `—` with a space each side, never `--` (a `--` inside a name ends it).
- The citation prefix is how the pieces avoid each other: an article belongs to one piece only, so no two pieces can give two different rules one name, and a later module that imports all four pieces can use every name.
  A duplicate **rule** name across two imported modules is an error at the use (measured on 1.6.98 for `YMD`; the brief says the same of any name defined in two imported modules); a duplicate **constructor** name across two enumerations is accepted and resolved by the expected type (measured), so reusing one is legal but confusing and is not done.
- A rule is named in prefix style: the name, then its arguments, each a backticked parameter name (`` `art. 48 — … ` `o segurado` ``).
- A BOOLEAN rule reads as a clause that is true or false.
  An amount says its unit: `` `art. 61 — renda mensal do auxílio-doença, em reais` ``.
  A date rule starts with `data`: `` `art. 49 — data de início da aposentadoria por idade` ``.
- Pieces write the Law's layer-1 rules in the Law's own third person ("o segurado", "a segurada", "o dependente").
  The first-person questions ("Tenho direito à aposentadoria por idade?") belong to the seat layer, written later; a piece may put a one-line `@desc` on a `GIVEN` input to help that layer, and writes no `@export`.

### An input

- An input is a `GIVEN` parameter, **on every rule that reads it** (the stable build rejects a section `GIVEN`: `dialects.md`, not re-run here).
  Every parameter named in a `GIVEN` must appear in the rule's head, or the build says "The names in a type signature must match those in the definition" (measured).
- A BOOLEAN input is a full affirmative proposition with its verb: `` `o segurado cumpriu a carência exigida` ``.
  A negative fact is `NOT` of the affirmative input, never an input named "não ...".
- A NUMBER input ends with its unit: `em reais`, `em dias`, `em meses completos`, `em anos completos`.
- A DATE input starts with `a data`: `a data do requerimento`, `a data do óbito do segurado`.
  The events the pieces share are written the same way everywhere: `a data do requerimento`, `a data do óbito do segurado`, `a data do parto`, `a data do início da incapacidade`, `a data do afastamento da atividade`, `a data do desligamento do emprego`, `a data do recolhimento à prisão`, `a data da cessação das contribuições`.
- A judgment the Law hands to someone else is answered conditionally, as an input that says whose conclusion it is: `` `a perícia médica do INSS conclui que o segurado está incapaz para o seu trabalho` ``, `` `a autoridade judicial declara a morte presumida do segurado` ``.
  Never guess it, and never code it as `FALSE`.
- Record fields start at the complement and carry no `é`, `está`, `tem` or `possui`: the genitive `'s` already supplies the verb, so `` o dependente's `inválido` `` and not `` o dependente's `é inválido` `` (the Portuguese form of the genitive ruling in `drafting-patterns.md`).
- A fact about something outside your piece is an input with the **exact name** in the table below, and a comment `-- by reference: art. N, encoded by pbX`.
  Where your piece needs an outside fact that the table does not list, name it the way the Law words it, put the article in parentheses at the end, and list it in your own NOTES.md.

| the fact | exact name of the input | type | produced in | read in |
| --- | --- | --- | --- | --- |
| the insured person | `o segurado` | `Segurado` | core | all pieces |
| the dependant | `o dependente` | `Dependente` | core | pb1, pb3, pb4 |
| the reference amounts | `os valores de referência` | `Valores de referência` | core | pb1, pb2, pb3 |
| the person keeps the quality of insured | `o segurado mantém a qualidade de segurado (art. 15)` | BOOLEAN | pb1, art. 15 | pb2 (art. 55), pb3 (art. 73 sole paragraph), pb4 (art. 102) |
| the carência asked of this benefit was met | `o segurado cumpriu a carência exigida (arts. 24 a 27-A)` | BOOLEAN | pb1, arts. 24 to 27-A | pb2 (arts. 39, 42, 48, 52, 57), pb3 (arts. 59, 80) |
| the event is a work accident | `o evento é acidente do trabalho (arts. 19 a 21)` | BOOLEAN | pb1, arts. 19 to 23 | pb2 (arts. 28, 34, 44), pb3 (art. 61), pb4 (arts. 104, 118) |
| the person is a dependant of the insured | `a pessoa é dependente do segurado (art. 16)` | BOOLEAN | pb1, art. 16 | pb3 (arts. 74 to 80), pb4 (art. 110) |
| the class of a dependant | `a classe do dependente (art. 16, § 1º)` | `Classe de dependente` | pb1, art. 16 | pb3 (art. 76 § 2 names inciso I; the order of the classes applies to the pension) |
| the salário-de-benefício | `o salário-de-benefício em reais (art. 29)` | NUMBER | pb2, art. 29 | pb3 (art. 61), pb4 (art. 86 § 1) |
| the length of contribution or service | `o tempo de contribuição do segurado em meses completos` | NUMBER | an input | pb2 (arts. 29-C, 52 to 56), pb4 (arts. 96 to 98) |
| the count of monthly contributions | `o número de contribuições mensais` | NUMBER | an input | pb1 (arts. 24 to 27), pb3 (art. 77 § 2, V) |

The last two rows (length of contribution, count of monthly contributions) are inputs in every piece, because nobody computes them, and they must be spelled alike.
The read-in column is where this keel saw the term used, not a promise: a piece that does not need an input does not declare it.

### An enumeration constructor

- A constructor is the Law's own phrase, lower case, Portuguese, backticked: `` `auxílio-doença` ``, `` `segurado especial` ``.
- Do not repeat a constructor of the core in your own enumeration.
- Do not name a field, an input or a rule after any constructor.
  A field and a constructor with one name type-check on 1.6.98, but `dialects.md` records that the `unstable` build then reads the field and fails; the check is cheap to keep.
- Give each enumeration of your piece a name that is not a bare noun the other pieces could also use.
  The words `Segurado`, `Dependente`, `Prestação`, `Prazo`, `Parte`, `Sexo` and `Categoria de segurado` are the core's.
- The constructors of `Parte` have no article (`segurado`, `dependente`, `empresa`, `empregador doméstico`, `INSS`, `Previdência Social`), so a regulative rule reads `PARTY segurado MUST ...` and never meets the input `o segurado`.
  A rule with an input named `o segurado` (a `Segurado`) and `PARTY segurado` ran to `FULFILLED` in a throwaway module on 1.6.98.

### A question

- The questions are written in the seat layer, later, in the first person, as the insured or the dependant would ask them, in Portuguese, ending in `?`: "Tenho direito à aposentadoria por idade?", "Quanto vou receber de auxílio-doença por mês?", "A partir de quando recebo a pensão por morte?", "Por quanto tempo recebo o salário-maternidade?", "O que preciso declarar ou entregar?".
- A rule in a piece is named so that its question is obvious: whether (BOOLEAN), how much (reais), from when (date), for how long (`Duração do benefício`), what the person must do (a regulative rule over `Parte`).

### Amounts, percentages, days, months, years and dates

- **Money** is a NUMBER of reais (R$), centavos as decimals (`5_180.25`), per month unless the name says otherwise.
  The name says `em reais` when a bare number could be mistaken for something else.
  There is no money type.
  The Law's cruzeiro figures (art. 66: Cr$ 1.360,00, Cr$ 170,00, Cr$ 51.000,00; art. 133: Cr$ 100.000,00 and Cr$ 10.000.000,00) are historical: art. 134 has them readjusted with the benefits and the text itself notes "Atualizações decorrentes de normas de hierarquia inferior".
  Take the current figure as an input in reais, and quote the Cr$ figure in a comment only.
- **Percentages** are percent literals: `70%` is `0.7`, `91%` is `0.91`, `100%` is `1`.
  A percentage is stored as the fraction of one, never as `70`.
  A name for such a value says `percentual` or `coeficiente`.
  "1/12 (um doze avos)" is `1 DIVIDED BY 12`, written in brackets.
- **Days, months, years** are whole NUMBERs with the unit in the name.
  An age is `em anos completos` (complete years on the date the rule asks about).
  A length of contribution or service is `em meses completos`, because the carência is counted in months: 30 years of service is 360.
  Years of complete service ("cada novo ano completo de atividade", art. 53) are `FLOOR` of the months divided by 12.
- **A time limit** is a `Prazo`, built with `prazo em dias`, `prazo em meses` or `prazo em anos`.
  The last day on which an act is still in time is `o dia em que termina ... contado de ...`.
  The reading is inclusive: "até 90 (noventa) dias depois" is the date plus 90 days and the act on that day is in time, so a rule compares with `AT MOST` (tested against art. 49, I, a and art. 74, I).
  Business days (art. 22, "primeiro dia útil seguinte"; art. 41-A § 2, "do primeiro ao quinto dia útil") have no unit: no library holds a holiday calendar.
  Art. 41-A § 4 says what a dia útil is ("aquele de expediente bancário com horário normal de atendimento"); the piece takes the date as an input and says so.
- **Dates** are `DATE`, written `YMD ano mês dia` (`YMD 1991 7 24`).
  The core defines `YMD`; do not define your own, because a second definition makes every use an error (measured: "There are multiple definitions for the identifier YMD").
  It is `Date d m y` underneath, so an impossible date rolls over and is not refused: never write one.

### Where the source does not answer

- The stable build has no `REFUSE`, so a case the encoding does not cover returns a `MAYBE`, with `NOTHING` for "not covered", and the `NOTHING` is asserted in a test.
  Where the text names the absent outcome ("não será devido", "cessará"), the result type names it as a constructor instead.
- Never `FALSE`, never `0`, never a plausible default.
- Do not invent a three-valued answer type of your own (`sim`/`não`/`indeterminado`): the language has `MAYBE`.
- A power left to the Executive or to a regulation ("conforme dispuser o Regulamento", "nos termos do regulamento") is an input when a rule needs its outcome, and is listed in your NOTES.md.

## Defined terms

The Law has no interpretation section.
It defines about a dozen terms inline, in the articles that use them, and it points to outside instruments for several more.
Source lines are the lines of `lei-8213-1991.pt.txt`.
"By reference" below means: encoded by the piece named, and taken as an input by every other piece that needs it, under the exact name in the table in "Naming conventions" where there is one.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| Previdência Social: the RGPS and the Regime Facultativo Complementar | art. 9 (lines 87-89) | the core, `Regime de previdência`; by reference: encoded by piece pb1, art. 9 | pb1 encodes the sentence; the type is shared |
| beneficiários: segurados and dependentes | art. 10 (line 97) | the core, `Segurado`, `Dependente`; by reference: encoded by piece pb1, art. 10 | |
| segurado obrigatório, by category | art. 11, caput and incisos I, II, V, VI, VII (lines 101-142) | the core, `Categoria de segurado`; by reference: encoded by piece pb1, art. 11 | who falls in each category (alíneas, §§ 1 to 12) is pb1's; incisos III and IV are revoked (lines 115-116) |
| empregado doméstico | art. 11, II (line 114) | by reference: encoded by piece pb1, art. 11, II | |
| regime de economia familiar | art. 11 § 1 (line 149) | by reference: encoded by piece pb1, art. 11 § 1 | read by the definition of segurado especial |
| segurado facultativo | art. 13 (line 229) | the core, `Categoria de segurado`; by reference: encoded by piece pb1, art. 13 | |
| empresa; empregador doméstico; what is equated to a empresa | art. 14, I, II and sole paragraph (lines 231-235) | the core, `Parte`; by reference: encoded by piece pb1, art. 14 | |
| qualidade de segurado, kept (art. 15) and lost (art. 15 § 4) | art. 15 (lines 236-257) | by reference: encoded by piece pb1, art. 15 | input name `o segurado mantém a qualidade de segurado (art. 15)` |
| dependentes and their classes | art. 16, I to III and § 1 (lines 260-273) | the core, `Parentesco com o segurado`, `Classe de dependente`, `Dependente`; by reference: encoded by piece pb1, art. 16 | input name `a pessoa é dependente do segurado (art. 16)` |
| enteado, menor sob tutela, menor sob guarda judicial equated to a child | art. 16 § 2 (line 277) | by reference: encoded by piece pb1, art. 16 § 2 | |
| companheira, companheiro | art. 16 § 3 (line 278) | by reference: encoded by piece pb1, art. 16 § 3 | points to art. 226 § 3 of the Constitution, which is not among the inputs |
| the benefits and services | art. 18 (lines 309-334) | the core, `Prestação`; by reference: encoded by piece pb1, art. 18 | |
| acidente do trabalho | art. 19 (line 345) | by reference: encoded by piece pb1, art. 19 | input name `o evento é acidente do trabalho (arts. 19 a 21)` |
| doença profissional; doença do trabalho | art. 20, I and II (lines 351-352) | by reference: encoded by piece pb1, art. 20 | both point to a list made by the ministry, which is not among the inputs |
| what is equated to an acidente do trabalho | art. 21 (line 359) | by reference: encoded by piece pb1, art. 21 | |
| dia do acidente | art. 23 (line 396) | by reference: encoded by piece pb1, art. 23 | |
| período de carência | art. 24 (line 399) | by reference: encoded by piece pb1, arts. 24 to 27-A | input name `o segurado cumpriu a carência exigida (arts. 24 a 27-A)` |
| salário-de-benefício | art. 29 (line 466) | by reference: encoded by piece pb2, art. 29 | input name `o salário-de-benefício em reais (art. 29)`; the fator previdenciário formula is in an Anexo that is not in this text |
| salário-de-benefício of the segurado especial | art. 29 § 6 (line 476) | by reference: encoded by piece pb2, art. 29 § 6 | |
| inserção extemporânea no CNIS | art. 29-A § 4 (line 501) | by reference: encoded by piece pb2, art. 29-A | |
| dia útil | art. 41-A § 4 (line 665) | by reference: encoded by piece pb2, art. 41-A § 4 | see "business days" above |
| tempo de serviço | art. 55 (line 739) | by reference: encoded by piece pb2, art. 55 | |
| segurado de baixa renda; how its income is measured | art. 80 §§ 3 and 4 (lines 1093-1096) | by reference: encoded by piece pb3, art. 80 | the income threshold is that of art. 13 of Emenda Constitucional nº 20/1998, which is not among the inputs: an input |
| reabilitação profissional (what it comprises) | art. 89, sole paragraph (line 1185) | by reference: encoded by piece pb4, art. 89 | |
| exercício do direito de anular | art. 103-A § 2 (line 1315) | by reference: encoded by piece pb4, art. 103-A | |
| data da Lei; data de entrada em vigor | title (line 5); art. 155 (line 1760) | the core: `a data da Lei nº 8.213`, `a data de entrada em vigor da Lei nº 8.213` | F-1; art. 155 is pb3's, which cites the core constant |
| empresa de trabalho temporário | art. 11, I, b (line 105): "definida em legislação específica" | outside this text: an input for pb1 | |
| módulo fiscal | art. 11, V, a and VII, a, 1 (lines 131, 144) | outside this text: an input for pb1 | |
| agentes nocivos | art. 58 (line 774): defined by the Poder Executivo | outside this text: an input for pb2 | |
| Regulamento | arts. 17, 55 and others: "conforme dispuser o Regulamento" | outside this text: an input where a rule needs its outcome | |
| Plano de Custeio da Seguridade Social | arts. 15 § 4, 39, II | outside this text (Lei nº 8.212/1991): an input | |
| valores de referência (salário mínimo, limites do salário-de-contribuição) | not defined; used in arts. 22, 29 § 2, 33, 39, 48 § 4, 73 | the core, `Valores de referência`, as an input | the Law fixes none of the three; art. 41-A § 1 speaks of a "limite máximo do salário-de-benefício", and pb2 decides whether that is the same amount as the limite máximo do salário-de-contribuição of art. 29 § 2 |

## Instructions to the pieces

1. **Import** the core as `` IMPORT `pb-core` `` (the name has a hyphen, so it is backticked).
   `pb-core.l4` is the only module the pieces share, and a piece's own modules import only `pb-core` and each other.
   Do not copy, edit or re-declare anything in it.
   The core imports `prelude` and `daydate`, and their names (`add months`, `Date`, `Day`, `count`, `elem`, `sum`, `max`, `min` ...) reach your module through it.
2. **Strikethrough spans run over several lines.**
   A line that begins `⟦STRUCK:` and has no `⟧` opens a span that continues on the following lines until a `⟧`; a line that begins `⟦STRUCK:` and nothing else is such an opener.
   A `grep -v` on whole-line wrappers shows the inciso lines inside a span as live.
   Three cases found while reading: art. 60, where two struck caputs (lines 802-803) and two struck incisos (lines 805-808) sit just before the live caput on line 809; art. 86, which has seven opener lines (1119, 1123, 1124, 1125, 1127, 1131, 1134) of which only the one on line 1134 is live; and art. 74 § 2 (the two-year rule) and art. 101's first opener and its incisos, which are struck over several lines.
   List the live lines of the text with this command, which tracks the spans across lines (it printed 1157 live lines on this file; a version that deletes each `⟦STRUCK: ... ⟧` with a regular expression printed the same 1157 lines):
   ```
   python3 -I - lei-8213-1991.pt.txt <<'EOF'
   import sys
   depth = 0
   for n, line in enumerate(open(sys.argv[1], encoding='utf-8').read().split('\n'), 1):
       live, i = '', 0
       while i < len(line):
           if line.startswith('⟦STRUCK:', i):
               depth += 1
               i += 8
           elif line[i] == '⟧':
               depth = max(0, depth - 1)
               i += 1
           else:
               if depth == 0:
                   live += line[i]
               i += 1
       if live.strip():
           print(f'{n}\t{live.strip()}')
   EOF
   ```
   Read the live lines for your range before you choose what to encode.
   A line may be part live and part struck (`§ 4⟦STRUCK: º⟧ O dirigente ...` at line 152): the live part is what is law.
3. **Quote with `srcrefs.py quote` and paste its output untouched.**
   `srcrefs.py check` requires a quote to be one contiguous slice of the raw line, so you cannot delete a `⟦STRUCK: ... ⟧` from the middle of a quotation: quote the whole raw line as `quote` prints it, or start or stop at a word boundary outside the wrapper (both measured to pass on line 152; deleting the `º` from inside fails).
   A quotation may stop with ` …` (a space and an ellipsis), and may start in the middle of a line at a word boundary, which is how the core quotes the end of long lines.
   Never quote a wholly struck line.
   Run `python3 -I srcrefs.py check --refs <the text file> <your .l4 files>` and report the 0 problems.
4. **The section index lists struck openers too.**
   `SECTION-INDEX.txt` repeats an article where the text repeats its opener (art. 27-A twice, 86 three times, 101, 106, 126 and 151 twice).
   Give one coverage row per article (and per paragraph where they differ) and name the struck variants in the note of that row.
   These articles have **no live opener at all** (every opener is struck or revoked) and get a row `repealed or blank in this text`, with the reason, in their piece:
   - pb1: 7, 8
   - pb2: 30, 41
   - pb3: 64, 71-D, 79, 126-A, 127, 139, 140, 141, 144, 145, 146, 147, 148, 150, 152
   - pb4: 81, 82, 83, 84, 85, 87, 95, 123

   (Computed by the command above and a search for article openers that have a live line; 124-E and 124-F are live openers whose text is "(VETADO)" and so are `repealed or blank in this text` too.)
5. **Dates.**
   `a data da Lei nº 8.213` (24 July 1991) and `a data de entrada em vigor da Lei nº 8.213` (25 July 1991) are in the core.
   Art. 55 § 2 (pb2) and arts. 137, 138, 143 (pb3) say "data de vigência desta Lei" or "entrada em vigor desta Lei": use the core constant, do not take it as an input and do not define a second one.
   Art. 142 names "24 de julho de 1991" itself, so write that date out with `YMD 1991 7 24` and quote it.
   Where pb1's brief asks for the date of enactment, the title block is already carried by the core.
6. **Reserved words.**
   Every name in the Vocabulary table is the core's.
   Your rule names begin with an article citation (see "Naming conventions"), so they cannot meet another piece's.
   Your own types get specific names (`Pedido de pensão por morte`, not `Pensionista`) and your own constructors do not repeat the core's.
7. **Benefit names.**
   The Law calls the same benefit by two names (F-3).
   Use the constructor of the core in code (`auxílio-doença`, `aposentadoria por invalidez`, `aposentadoria por tempo de contribuição`) and write the other name in a comment.
   Where the live text says "auxílio por incapacidade temporária" (art. 60 §§ 11-F and 11-H, lines 853, 857; art. 101 caput, line 1263) or "aposentadoria por incapacidade permanente" (art. 43 § 6, line 693; art. 101 caput and § 1, lines 1263, 1271; art. 135-A, line 1637), the constructor is the same.
   Do not add a second constructor.
8. **What a rural worker is** is not a category: art. 48 § 1 defines the "trabalhadores rurais" by pointing to alínea a of inciso I, alínea g of inciso V, and incisos VI and VII of art. 11.
   pb2 takes that as an input or derives it from `Categoria de segurado` and its own facts; there is no constructor for it.
9. **Cross-piece facts** are inputs with the exact names in the table in "Naming conventions".
   Do not import another piece (you cannot see it) and do not re-derive its rule.
10. **Judgments left to someone else** (the perícia médica, the autoridade judicial, the Executive, the Regulamento) are conditional inputs, named as in "Naming conventions".
11. **Money.**
    The Law's cruzeiro figures are history; take the current amount as an input in reais.
    Art. 128 states R$ 5.180,25 (line 1591) and art. 134 readjusts the money values of the Law, so a rule that needs the current value takes it as an input and quotes R$ 5.180,25 in a comment.
12. **Dialect reminders for the stable build** (from `dialects.md` unless marked measured):
    - `GIVEN` on every rule; no section `GIVEN`.
    - No `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (but `LEST BREACH ... BECAUSE` is accepted: a `#TRACE` over `Parte` and a rule with `PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST BREACH BY ... BECAUSE "..."` ran to `FULFILLED` on 1.6.98 in a throwaway module).
    - No `TYPICALLY`, no `EVERY`, no sets (`SET OF`), no `@lang`, no `@nlg:xx`.
    - Bracket every `NOT`; keep every `#ASSERT` on one line; bracket arithmetic that crosses a line.
    - A rule applied inside `MUST (...)`, and a field read in an action's argument (`MAY Take Official (c's measure)`), are rejected: write the constructor, and compare in `PROVIDED`.
    - Do not compare a `DEONTIC` with `EQUALS`: assert a BOOLEAN and exercise the deontic with `#TRACE`.
    - `IMPORT` finds only files in your own folder.
13. **Tests.**
    Expected values are hand-written from the text and never copied from the encoding's output.
    A test of a dated rule is run on both sides of its date.
    Run `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (there is no main build to fetch offline; `L4_BIN` is itself a main build) and report the numbers it prints.
14. **The text is a compilation, not the law as it stands.**
    Arts. 48 and 52 to 56, for example, print an age of 65 and 60 and 30 and 25 years of service, and the text carries MP versions that Planalto shows as "Vigência encerrada".
    Encode the live text as it is printed and do not correct it from outside knowledge; say in your NOTES.md where the live text looks superseded by another provision of the same text, if you see it.
15. **Where each provision belongs** (from the brief): pb1, the title lines, Título I, Título II (arts. 1 to 9) and Título III Capítulo I and Capítulo II Seções I and II (arts. 10 to 27-A); pb2, Seção III, Seção IV and Seção V Subseções I to IV (arts. 28 to 58); pb3, Seção V Subseções V to IX (arts. 59 to 80) and Título IV (arts. 125 to 156); pb4, Seção V Subseções X to XII (arts. 81 to 87), Seções VI, VII and VIII (arts. 88 to 124-G).

## Coverage table

The keel has no range: the Law has no interpretation section and the keel owns no provision.
The table has no rows because there are no provisions to count: 0 provisions in range, 0 rows.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |

The keel's range contains no date of enactment and no commencement provision, so by the brief it does nothing about dates.
It departs from that in one place, on purpose: the core carries three constants, the date in the title (line 5), the date of publication (named by the footer, line 1765, which is not quoted) and the rule that the Law enters into force on it (art. 155, line 1760).
It does so because pb2 (art. 55 § 2) and pb3 (arts. 137, 138, 143) both read "a data de vigência desta Lei", and two pieces that cannot see each other could otherwise settle on 24 July and 25 July.
Art. 155 stays pb3's row; it cites the core constant (F-1).

## Fork register

Where I looked for ambiguity: the lists of art. 11, 13, 16, 18; the benefit names across arts. 18, 29, 52 to 56, 60, 88, 97, 101, 104, 129-A, 135-A; the dates (title, art. 142, art. 155, footer); every place that states an amount or a time limit; the strikethrough spans around arts. 60, 74, 77, 86 and 101.
Each row says who settled the reading.
Nobody outside this encoding has: all of them are the keel's choice and are to be reviewed.

| id | the question | readings seen | taken | text that licenses it |
| --- | --- | --- | --- | --- |
| F-1 | When does the Law enter into force? | (a) 24 July 1991, the date in the title; (b) 25 July 1991, the date of the DOU edition in Planalto's footer; (c) an input | (b), as a constant in the core. Art. 155 says "na data de sua publicação" and the Law prints no publication date. The footer is Planalto's, not the Law's: if it is not accepted, change the one constant `a data de publicação da Lei nº 8.213 no Diário Oficial da União` and nothing else moves. | art. 155 (line 1760); title (line 5). The footer (line 1765) is read but not quoted in the encoding, because it is Planalto's note and `STUB-SOURCE-LICENSE.md` treats such notes as probably unprotected, not established. Art. 142 (line 1693) names 24 July 1991 itself, for a different purpose (who is "inscrito" by then), and is not the commencement. |
| F-2 | A time limit in months or years from a day that the later month lacks (31 August plus 6 months). | (a) the last day of the shorter month (the `daydate` library: 28 February 2026); (b) the first day of the next month; (c) another day count | (a). The Law says nothing about it. Brazilian civil law may count it otherwise; that is not among the inputs and was not checked. The difference is at most three days and only for a starting day above 28. | arts. 15, 103 give the limits and no rule for the shorter month. Tested with a start on 31 August 2025 and on 29 February 2016. |
| F-3 | Does the Law mean one benefit or two by "aposentadoria por tempo de serviço" and "aposentadoria por tempo de contribuição"; by "auxílio-doença" and "auxílio por incapacidade temporária"; by "aposentadoria por invalidez" and "aposentadoria por incapacidade permanente"? | (a) one benefit with two names; (b) two benefits | (a), one constructor named as art. 18 names it. Art. 29 I applies the salário-de-benefício of art. 18 I, c to the benefit that arts. 52 to 56 and 97 call "por tempo de serviço"; art. 101 caput uses the new names while its § 1, I uses the old names ("aposentadoria por invalidez ou do auxílio-doença que a precedeu") for the same benefits. | art. 18, I, a, c, e (lines 311, 314, 317); art. 29, I (line 467); arts. 52-56, 97 (lines 734, 1246); art. 101 and § 1 (lines 1263, 1273). The text never says "são a mesma coisa". |
| F-4 | Is `abono anual` (art. 40), `seguro-desemprego` (art. 124 sole paragraph) or `pecúlio` (art. 18 III a, struck) a `Prestação`? | (a) yes; (b) no | (b). `Prestação` is art. 18's live list plus `abono de permanência em serviço`, which arts. 80 and 124, III still name. The abono anual is a payment that follows from other benefits and only art. 40 (pb2) states it; the seguro-desemprego is not a benefit of this Law; pecúlios are revoked. | art. 18 (lines 309-334); art. 40 (line 614); art. 124 (lines 1482-1490). |
| F-5 | Sex has two values. | (a) the two the text uses; (b) a third | (a). Every provision that turns on sex says "homem" or "mulher", "do sexo masculino" or "do sexo feminino". No third is invented; a person to whom neither applies is outside the encoding. | arts. 29 § 9, 48, 51, 52, 53, 56, 97, 98. |
| F-6 | What date is "idade em anos completos" on? | (a) the date of the request; (b) the date of the event the rule is about | (b) per rule: the date the rule asks about (request, death, birth ...). A rule that needs the age on another date takes it as a separate input. | art. 16 ("menor de 21 anos"), art. 48 ("completar 65 anos"), art. 77 § 2, V ("idade do beneficiário na data de óbito"). |
| F-7 | Which amounts are reference values? | (a) the three of the record; (b) also the "menor benefício de prestação continuada" of art. 11 § 9 | (a). The "menor benefício" is read by art. 11 only (pb1), and the Law does not say it equals the salário mínimo: pb1 takes it as its own input. | arts. 11 § 9 (lines 177, 197, 198); 22, 29 § 2, 33, 48 § 4. |
| F-8 | Are the inputs of arts. 22 and 41-A in business days? | (a) a unit `em dias úteis`; (b) none | (b). No library holds a holiday calendar, so the date is an input. | arts. 22 (line 390), 41-A §§ 2 to 4 (lines 663-665). |
| F-9 | How is a time limit in days counted from a date? | (a) the date plus N days is the last day, the day of the event not counted and the last day counted; (b) the date plus N minus 1 (the day of the event is day 1); (c) the day after the date plus N | (a). An act on the date plus N days is in time; an act the day after is not. | art. 49, I, a (line 727): "até essa data ou até 90 (noventa) dias depois dela"; art. 74, I (line 970): "em até 180 (cento e oitenta) dias após o óbito". Tested on a start of 10 January 2026 (90 days end on 10 April) and of 1 March 2026 (180 days end on 28 August; 90 days on 30 May). |

## What the stable binary does not accept

Measured on 1.6.98 on 2026-10-24, in throwaway files that were deleted:

- `YMD` is not defined: the core defines the one shim (it carries no `@ref`, because it is a toolchain shim and not law).
  A second definition in an importing module is an error at every use ("There are multiple definitions for the identifier YMD").
- A `GIVEN` parameter that the rule's head does not name is an error: "The names in a type signature must match those in the definition."
- Accents compile in every position used here (types, constructors, fields, rule names, `§` headings, `@ref` text, quote lines).
  Nothing was rejected for an accent.
- A `§` heading in an imported module does not hide its names from the importer; `Date`, `Day`, `add months` and `add years` are visible through ``IMPORT `pb-core` ``.
- Two enumerations with a constructor of one name are accepted, in one module or in two imported modules; the use is resolved by the expected type.
- `srcrefs.py check` rejects a quotation that leaves out the middle of a line with a struck wrapper (line 152), and accepts the whole raw line and a start after the wrapper.

Taken from `dialects.md` and not re-run: section `GIVEN` rejected; `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` rejected; `TYPICALLY` on a field rejected; sets, `EVERY`, `@lang`, `@nlg:xx` rejected; `WAIT UNTIL` spelled `WAITUNTIL`.

## What check.sh prints

Run on 2026-10-24 with `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, as the brief directs.
With the target `unstable`, `check.sh` skips its comparison with a second, main-build binary and says so; that comparison would in any case have compared 1.6.98 with itself, because `L4_BIN` is itself a main build (`--version` prints `1.6.98 (main, 7689b0d, 2026-10-19)`; its sha256, checked, is `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`).
Every module was run with that one build.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
pb-core-tests-vocabulario.l4                   0        47       0        0         0
pb-core.l4                                     0         0       0        0         0
TOTAL (2 modules)                              0        47       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <the text> pb-core.l4 pb-core-tests-vocabulario.l4`:

```
srcrefs check: 63 src: lines, 14 runs, 60 locators, 0 problems
```

The 47 satisfied assertions are the tests file's; `pb-core.l4` has none, because it has no rule (its helpers are exercised by the tests).
The quotation lines are all in `pb-core.l4`; the tests file has none.
`--strict` also reports 0 problems on `pb-core.l4`.
`l4 check` printed `Check succeeded.` for both modules and no warning about an `@ref` at the end of a file or after code.
A throwaway module that imported both modules and called the time-limit helper ran with no error or warning and was deleted.
