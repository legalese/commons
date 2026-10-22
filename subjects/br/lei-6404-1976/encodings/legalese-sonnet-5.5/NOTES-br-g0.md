# NOTES: br-core, the keel of the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976)

Written on 2026-10-22 by the keel agent `br-g0`, for the seven part agents br1 to br7 who will import `br-core.l4` and read this file as their guide.
Read the section "Instructions to the pieces" first: its first item is a trap that makes a piece encode repealed law as live law.

**What is in this folder from the keel.**
`br-core.l4` (the shared vocabulary), `br-core-tests-prazo.l4` and `br-core-tests-vocabulario.l4` (tests), this `NOTES.md` and `PROGRESS.md`.
`check.sh` and `srcrefs.py` were already here and are unchanged.
There are no `br-core-<topic>.l4` interpretation modules, because the Law has no interpretation section (see "Coverage table").

**The source.**
`lei-6404-1976.pt.txt` (2,593 lines, sha256 `e1d5cb82760883604700cd70a4dfb50e73cff2a83a9b8936340aac13a9a5a1e3`) is a plain-text rendering, made by a converter script, of Planalto's compiled text retrieved on 2026-10-21 (`l6404consol.htm`).
It is not the official text: Planalto's own footer says only the text published in the Diário Oficial da União is official.
Nothing in this encoding is verified against the official text, and no note here claims it is.
Line numbers in this file and in every `src:N` locator are lines of that text file.

**The seat.**
Every piece writes for the seat named in the brief: an acionista, minority shareholders included, of a company (sociedade anônima), asking what the Law gives them, what it requires of them, and what the company, its managers and its controlling shareholder may do in relation to them.
The keel writes no seat layer and no `@export`.
The core's records are shaped so that a person in that seat can state every field (a shareholder knows whether the company has a conselho de administração, how many shares of which kind they hold, and what the minutes record about votes).

**The target.**
The stable `l4` 1.6.98, which prints `1.6.98 (main, 7689b0d, 2026-10-19)` and has sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`, the digest the brief names.
That binary is the `main` build, so the `main` dialect is satisfied by construction and `check.sh` is run with `L4_TARGET=unstable`, which skips a second run that would compare `main` with itself.
`JL4_LIBRARY_PATH` was never set.

**Dates are data.**
The keel's range is empty, so the keel builds no date constant and no commencement rule.
Where the dates are, so the pieces do not both build them or both miss them: the enactment date, 15 December 1976, is in the title block at line 5 ("LEI No 6.404, DE 15 DE DEZEMBRO DE 1976"), which belongs to br1's range (lines 1 to 371).
The entry into force is Art. 295, line 2555 ("60 (sessenta) dias após a sua publicação"), and the only publication date in the text is the footer at line 2592 ("DOU de 17.12.1976 (suplemento)"); both belong to br7's range (lines 2326 to 2593).
Art. 296 (line 2562) counts a year from the entry into force.
Neither br1 nor br7 may define a name the other defines: br1 names the enactment date, br7 names the publication date and the entry into force, and each takes the other's as a plain DATE input if it needs it.

## Vocabulary

Every type and every enumeration constructor in `br-core.l4`.
"Licensed by" gives the article and the source line of the quoted text above the declaration.
The three records are fact bundles: no field is a conclusion of the Law.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Tipo de companhia` | enumeration (2) | whether a company is open or closed | Art. 4, line 27 |
| `companhia aberta` | constructor | its securities are admitted to trading in the securities market | Art. 4, line 27 |
| `companhia fechada` | constructor | its securities are not | Art. 4, line 27 |
| `Perfil da companhia` | record (5 fields) | the facts about a company that choose between branches of the Law in two or more pieces: `o tipo da companhia` (`Tipo de companhia`), `a companhia tem conselho de administração`, `a companhia tem conselho fiscal permanente`, `a companhia tem capital autorizado`, `a companhia é de economia mista` (all BOOLEAN) | Arts. 4, 138, 161, 168, 235, lines 27, 1236, 1427, 1497, 2116 |
| `Espécie de ação` | enumeration (3) | the three kinds of share | Art. 15, line 88 |
| `ações ordinárias` | constructor | ordinary shares | Art. 15, line 88 |
| `ações preferenciais` | constructor | preferred shares | Art. 15, line 88 |
| `ações de fruição` | constructor | fruition shares, which replace fully amortised shares (Art. 44, § 5º) | Art. 15, line 88 |
| `Forma da ação` | enumeration (4) | the forms a share can take | Arts. 20, 21, 22 parágrafo único, 34, 112, lines 151, 153, 156, 233, 919 |
| `ações nominativas` | constructor | registered shares | Arts. 20, 21, lines 151, 153 |
| `ações endossáveis` | constructor | endorsable shares (F4) | Arts. 21, 112, lines 153, 919 |
| `ações ao portador` | constructor | bearer shares | Art. 22 parágrafo único, line 156 |
| `ações escriturais` | constructor | book-entry shares, kept in a deposit account with no certificate | Art. 34, line 233 |
| `Participação do acionista` | record (5 fields) | a shareholder's holding of one kind and form of share: `a espécie das ações`, `a forma das ações`, `a quantidade de ações do acionista` (NUMBER), `as ações do acionista estão integralizadas` (BOOLEAN), `as ações do acionista têm valor nominal` (BOOLEAN) | Arts. 11, 15, 20, 21, lines 70, 88, 151, 153 |
| `Valor mobiliário` | enumeration (4) | the securities the Law itself creates and gives the shareholder a preference to subscribe | Art. 109, IV, line 833 |
| `ações` | constructor | shares | Art. 109, IV, line 833 |
| `partes beneficiárias` | constructor | beneficiary parts | Art. 109, IV, line 833 |
| `debêntures` | constructor | debentures | Art. 109, IV, line 833 |
| `bônus de subscrição` | constructor | subscription warrants | Art. 109, IV, line 833 |
| `Espécie de assembleia` | enumeration (3) | the meetings of shareholders | Arts. 18 parágrafo único, 131, lines 145, 1106 |
| `assembleia-geral ordinária` | constructor | the annual meeting on the matters of Art. 132 | Art. 131, line 1106 |
| `assembleia-geral extraordinária` | constructor | every other general meeting | Art. 131, line 1106 |
| `assembleia especial` | constructor | the meeting of the holders of a class | Art. 18 parágrafo único, line 145 |
| `Votação em assembleia` | record (5 fields, all NUMBER) | the counts the quorums are stated in: `o total de votos que podem ser dados`, `os votos dos titulares presentes`, `os votos a favor`, `os votos contra`, `os votos em branco` | Arts. 125, 129, 136, lines 1070, 1095, 1154 |
| `Parte` | enumeration (21) | the persons and bodies the Law names and that two or more pieces speak of; the type of `PARTY` in a regulative rule | see the constructors |
| `a companhia` | constructor | the company | Art. 4, line 27 and throughout |
| `o acionista` | constructor | any shareholder, from the seat | Art. 10, line 63 |
| `o acionista controlador` | constructor | the controlling shareholder | Art. 116, line 942 |
| `o acionista minoritário` | constructor | a shareholder who is not the controlling shareholder (F5) | Art. 276, § 1º, line 2388, for its own article only |
| `o administrador` | constructor | a conselheiro or a diretor | Art. 145, line 1320 |
| `o conselheiro de administração` | constructor | a member of the conselho de administração | Art. 145, line 1320 |
| `o diretor` | constructor | a member of the diretoria | Art. 145, line 1320 |
| `o membro do conselho fiscal` | constructor | a member of the conselho fiscal | Art. 161, line 1427 |
| `a assembleia-geral` | constructor | the general meeting as an organ | Art. 123, line 1034 |
| `o conselho de administração` | constructor | the board | Art. 138, line 1236 |
| `a diretoria` | constructor | the executive board | Art. 138, line 1236 |
| `o conselho fiscal` | constructor | the supervisory board | Art. 161, line 1427 |
| `o fundador` | constructor | a founder of the company | Art. 86, line 706 |
| `o subscritor` | constructor | a subscriber of shares | Art. 10, line 63 |
| `o debenturista` | constructor | a debenture holder | Art. 68, line 561 |
| `o agente fiduciário` | constructor | the trustee of the debenture holders | Art. 68, line 561 |
| `o liquidante` | constructor | the liquidator | Art. 210, line 1989 |
| `o auditor independente` | constructor | the independent auditor | Art. 142, IX, line 1299 |
| `a Comissão de Valores Mobiliários` | constructor | the securities regulator, the CVM | Art. 11, § 3º, line 73 |
| `a instituição financeira` | constructor | a financial institution acting for the company (custody, certificates, deposit) | Art. 27, line 190 |
| `o credor` | constructor | a creditor of the company | Art. 58, line 416 |
| `Prazo` | sum type with a number (3) | the one way a time limit is written | Arts. 137 IV, 81 parágrafo único, 108 parágrafo único, 124 § 1º II, lines 1220, 672, 826, 1049 |
| `prazo em dias` | constructor, field `quantidade de dias` | a limit counted in days | Art. 137, IV, line 1220 |
| `prazo em meses` | constructor, field `quantidade de meses` | a limit counted in months | Art. 81, parágrafo único, line 672 |
| `prazo em anos` | constructor, field `quantidade de anos` | a limit counted in years | Art. 108, parágrafo único, line 826 |

### The rules in the core

They are the only rules in the core, and none is a provision of the Law: they carry the counting convention F1 and F2, so that all seven pieces count a time limit in one way.
Each has a test in `br-core-tests-prazo.l4`.

| rule | takes | gives | what it does |
| --- | --- | --- | --- |
| `YMD ano mês dia` | three NUMBERs, year first | DATE | the date, written year first; the stable prelude has no `YMD`, and no piece defines its own |
| `o termo final do prazo` | `a data de início` (DATE), `o prazo` (`Prazo`) | DATE | the last day on which an act is still in time, counting forward from the event |
| `o ato foi praticado dentro do prazo` | `a data do ato`, `a data de início`, `o prazo` | BOOLEAN | the act is on or after the start date and on or before the last day |
| `a data limite de antecedência` | `a data do evento` (DATE), `o prazo` | DATE | the latest day on which an act still leaves the whole `Prazo` before the event ("com 21 dias de antecedência") |
| `o ato respeitou a antecedência` | `a data do ato`, `a data do evento`, `o prazo` | BOOLEAN | the act is on or before that latest day |

### Canonical names for the facts that several pieces ask

A fact that two or more pieces need is asked under one name, with one type, so that the seat layer asks it once.
The first nine are the fields of the three records; use the record, or the same name and type as a plain input.
The `@desc` is the wording a seat layer uses; a piece that writes `@desc` uses it as it stands.

| canonical name | type | `@desc` (the question to the shareholder) |
| --- | --- | --- |
| `o tipo da companhia` | `Tipo de companhia` | A sua companhia é aberta (seus valores mobiliários são negociados no mercado) ou fechada? |
| `a companhia tem conselho de administração` | BOOLEAN | A sua companhia tem conselho de administração? |
| `a companhia tem conselho fiscal permanente` | BOOLEAN | O conselho fiscal da sua companhia funciona de modo permanente? |
| `a companhia tem capital autorizado` | BOOLEAN | O estatuto da sua companhia autoriza aumentar o capital sem reformar o estatuto? |
| `a companhia é de economia mista` | BOOLEAN | A sua companhia é uma sociedade de economia mista? |
| `a espécie das ações` | `Espécie de ação` | De que espécie são as ações a que a pergunta se refere? |
| `a forma das ações` | `Forma da ação` | Qual é a forma dessas ações? |
| `a quantidade de ações do acionista` | NUMBER | Quantas ações dessa espécie e forma o acionista tem? |
| `as ações do acionista estão integralizadas` | BOOLEAN | O preço de emissão dessas ações foi pago por inteiro? |
| `as ações do acionista têm valor nominal` | BOOLEAN | Essas ações têm valor nominal? |
| `o total de votos que podem ser dados` | NUMBER | Quantos votos podem ser dados na assembleia, somando os de todas as ações com direito a voto? |
| `os votos dos titulares presentes`, `os votos a favor`, `os votos contra`, `os votos em branco` | NUMBER | Quantos votos estavam presentes, a favor, contra e em branco? |
| `o acionista é acionista controlador (art. 116)` | BOOLEAN | O acionista é acionista controlador? (este é o termo do art. 116, não um julgamento a fazer aqui) |

## Naming conventions

1. **Language, spelling and quoting.**
   Identifiers, `@desc` and `@export` text and `§` headings are Brazilian Portuguese, worded as the shareholder would be asked.
   Use the modern orthography in names: `assembleia`, not the `assembléia` of the 1976 text, and `assembleia-geral` with the hyphen, though the live text also writes `assembleia geral` without it.
   The quoted `-- src:N |` lines keep the source's spelling exactly.
   Back-tick every name with a space, an accent or punctuation, and every module name that has a hyphen: ``IMPORT `br-core` ``.
   Do not strip accents; they compile on the stable binary.
   File names are ASCII, and a piece's file names begin with its id (`br1-`, `br2-`, and so on) so that module names stay unique when the seven folders are put together.
2. **Rules.**
   A rule's name is a Portuguese clause that says what it decides, in lower case, as the Law would put it, and it ends with the provision in parentheses: `` `o acionista pode retirar-se da companhia (art. 137)` ``.
   Citations are written `(art. 4)`, `(art. 4-A, § 2º)`, `(art. 137, inciso II, alínea b)`, `(arts. 20 e 21)`; use `§ 2º` and `parágrafo único`, Roman numerals for incisos, a lower-case letter for alíneas.
   Every article belongs to one piece, so the citation makes a name unique across the seven pieces; two rules for one provision differ in what they decide.
   **Everything a piece defines (a rule, a type, an enumeration constructor) ends with a citation like this.**
   A name in the Vocabulary table has none, because it belongs to the core, and a piece never repeats one.
   Fields of a record and the names inside a `WHERE` are free.
   This is the control against the failure that cannot be seen from inside one piece: a seat layer imports several pieces, and a name defined in two imported modules cannot be used at all (measured on the stable binary: "There are multiple definitions for the identifier").
3. **Inputs.**
   An input (a `GIVEN` parameter) is a plain Portuguese phrase in the third person, in lower case, naming one fact: a statement for a yes/no fact (`o acionista votou contra a deliberação`), `a quantidade de ...` for a count, `o valor de ... em reais` for money, `a fração de ...` for a fraction, `a data de ...` for a date, `a espécie`, `a forma`, `o tipo` for an enumeration.
   Take a record as one `GIVEN` where there are many facts, and use the core's three records where they fit.
   A fact in the canonical table above is asked under its canonical name.
4. **Enumeration constructors.**
   A lower-case Portuguese noun phrase, never a bare adjective (`ações ordinárias`, not `ordinária`), because two enumerations may not share a constructor name on the stable binary: a use of the shared name is reported as ambiguous.
   Persons and bodies begin with the definite article, o or a (`o administrador`, `a diretoria`).
   A piece's own constructors end with a citation (rule 2).
5. **Questions.**
   A question to the shareholder is a rule written in a seat layer; the keel and the pieces do not write seat layers, but when one is written, a question's rule name begins with a capital letter and has no citation (`Posso retirar-me da companhia se votei contra a deliberação`), and its `@export` text is the question in the first person ending in `?`, with the citation in it: `Posso exercer o direito de retirada se votei contra a deliberação (art. 137)?`.
   Each input's `@desc` is one sentence, worded to the shareholder (`Você votou contra a deliberação?`), and says the unit when there is one.
   This follows the Employment Act seat example in `inputs/`, where the question rule is ``DECIDE `How many days of notice am I owed` IS`` with the citation only in the `@export` text.
   That example's own inputs are in the first person (`my contract sets the notice`) and are mapped onto the objective layer's third-person inputs inside a `WHERE`; the pieces' inputs stay third person, so that one piece serves every seat.
6. **Amounts of money.**
   A NUMBER in reais, with `_` as the thousands separator: Art. 294-B's "R$ 500.000.000,00" is written `500_000_000`.
   The unit is in the name (`em reais`); there is no currency type, because the stable prelude has none.
   A sum in an older currency is named for it (`em cruzeiros`, Art. 298).
   Counts of shares and votes are whole NUMBERs.
7. **Percentages and fractions.**
   A fraction is a NUMBER in which 1 is the whole, and it is written with the postfix `%`: `10%` is 0.1, `25%` is a quarter, `50%` is "metade", `5%` is 0.05.
   Never store `10` to mean ten per cent, which silently makes a threshold a hundred times too big.
   An exact ratio is written with `DIVIDED BY` in brackets, `(2 DIVIDED BY 3)` for "dois terços", because NUMBER is rational and exact; never `0.6667`.
   "0,1 (um décimo)" (Art. 46, § 2º) is `10%`.
   **Test a threshold by multiplying, never by dividing.**
   "No mínimo 10% das ações" is `parte AT LEAST 10% TIMES total`, "mais da metade" is `parte ABOVE 50% TIMES total`, "metade, no mínimo" is `parte AT LEAST 50% TIMES total`.
   A division would fail on an empty total; `br-core-tests-vocabulario.l4` has the pattern with numbers.
8. **Days, months, years and time limits.**
   A time limit is a `Prazo` (`` `prazo em dias` 30 ``, `` `prazo em meses` 6 ``, `` `prazo em anos` 2 ``), never a bare number of days, so that months and years are counted in one way.
   Use `o termo final do prazo` to count forward from an event, `o ato foi praticado dentro do prazo` to test an act against it, and `a data limite de antecedência` and `o ato respeitou a antecedência` to count backwards ("com 21 dias de antecedência no mínimo").
   A count of fiscal years ("exercícios consecutivos", Art. 111, § 1º, line 915) is a plain NUMBER named `a quantidade de exercícios ...`; it is not a `Prazo`.
   The counting convention is a fork, F1 and F2, and it is assumed, not taken from this Law.
9. **Dates.**
   A DATE, built with `YMD ano mês dia` from the core (year first, as in ISO 8601).
   `Date dia mês ano` (day first) is what the shim wraps; do not write it by hand, and do not define `YMD` in a piece.
   `DATE PLUS n` adds `n` days.
10. **A fact about something outside a piece.**
    Pieces cannot import each other, so a term that another piece defines is taken as a plain input whose name is the defined term followed by the defining article in parentheses, with the type in the "Defined terms" table (a BOOLEAN for a yes/no term, a core enumeration, or a NUMBER): `` `o acionista é acionista controlador (art. 116)` ``.
    The piece never re-encodes the other piece's test, and never guesses it.
    The same holds for a judgment the Law leaves to someone else: the CVM (`a CVM autorizou a redução do quórum (art. 136, § 2º)`), the estatuto (`o estatuto dispõe de modo diverso (art. 129, § 1º)`, for every "salvo disposição em contrário do estatuto"), the registry or a court.
    "O estatuto" is not defined by the Law; what it says is always a fact the shareholder supplies.
11. **A case the Law does not answer.**
    The stable binary has no `REFUSE`.
    A rule that can be asked a case the text leaves out, or leaves to someone else's judgment, gives a `MAYBE`: `JUST` the answer when the text answers, `NOTHING` when it does not, and the piece asserts the `NOTHING` (`#ASSERT regra caso EQUALS NOTHING`).
    Never `FALSE`, never `0`, never a plausible default, and no home-made `Indeterminado` enumeration.
12. **Headings.**
    `§` headings are unique across the seven pieces because they begin with the article range: `` § `Arts. 106 a 108: Obrigação de realizar o capital` ``.
    No section `GIVEN` (the stable binary rejects it: see "What the stable binary does not accept").
13. **Regulative rules.**
    `PARTY` is a value of the core's `Parte`; the action type is the piece's own, with a citation in every constructor name.
    Name no input inside an action (it degrades on the stable binary); compare with `PROVIDED`.
    Write `LEST BREACH BECAUSE "..."`, the one `BECAUSE` that is accepted.
14. **Citations in the code.**
    Every rule carries `@ref art. N (src:A-B)` above it, with quote lines made by `python3 -I srcrefs.py quote RAW A B` from the raw text file (the raw file, not a stripped copy), amendment notes included.
    `python3 -I srcrefs.py check --refs RAW FILE...` must report 0 problems.

## Defined terms

Every term the text defines, by a defining sentence, a definitional "considera-se" or "entende-se", or a deeming rule.
It was built by searching the live text for those forms (`entende-se`, `considera-se`, `consideram-se`, `é a operação`, `consiste`, `denominados`, `para os efeitos`, `para fins`, `presume-se`, `São coligadas`, and the like) and by reading the articles around each hit, not by reading every line, so a definition that uses none of those forms may be missing.
The first words of "encoded in" say the kind: **core+brN** (the core declares the type or field, and piece brN encodes the test that decides it from facts), **piece only** (the named piece alone encodes it), **scoped brN** (the text limits the definition to its own article or paragraph, and brN encodes it there), **delegated** (the Law does not define it; it leaves it to the CVM or the estatuto).
A few rows are not definitions in the strict sense and say so in the note: a description (art. 1), a term the Law uses without defining (classe de ações, sociedade de economia mista).
"Input elsewhere" gives the canonical input name for the pieces that need the term but do not encode it.
The Law has no interpretation section, so none of these is encoded by the keel.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| companhia ou sociedade anônima | Art. 1, line 14 | piece only: br1, art. 1 | a description (capital in shares, liability limited to the issue price), not a test |
| companhia aberta, companhia fechada | Art. 4, line 27 | core+br1: `Tipo de companhia`; br1 encodes the test at art. 4 | every other piece takes the canonical input `o tipo da companhia` |
| ações em circulação no mercado | Art. 4-A, § 2º, line 36 | piece only: br1, art. 4-A, § 2º | read only inside br1 |
| espécies de ações (ordinárias, preferenciais, de fruição) | Art. 15, line 88 | core+br1: `Espécie de ação`; br1, art. 15 | other pieces take `a espécie das ações` |
| classe de ações | Arts. 15, § 1º, 16, 17, lines 90, 95, 121 | piece only: br1, arts. 15 to 19 | not defined: the Law says only that a kind of share may have several classes, in the cases of those articles; its label is a plain input, `a classe das ações (art. 15, § 1º)`, STRING; read again in br2 (art. 84, line 688) and br3 (art. 110-A, lines 845 to 905; art. 136, lines 1158, 1160, 1176) |
| resgate | Art. 44, § 1º, line 310 | piece only: br1, art. 44, § 1º | |
| amortização | Art. 44, § 2º, line 311 | piece only: br1, art. 44, § 2º | |
| reembolso | Art. 45, line 317 | piece only: br1, art. 45 | read again in br3 (lines 857, 1187, 1206), br6 (2050, 2098, 2232, 2275, 2322) and br7 (2359, 2566); input elsewhere: `o valor do reembolso em reais (art. 45)`, NUMBER |
| partes beneficiárias | Art. 46, line 335 | core+br1: `Valor mobiliário`; br1, art. 46 | |
| debêntures | Art. 52, line 376 | core+br2: `Valor mobiliário`; br2, art. 52 | |
| garantia flutuante | Art. 58, § 1º, line 417 | piece only: br2, art. 58, § 1º | |
| debênture subordinada | Art. 58, § 4º, line 422 | piece only: br2, art. 58, § 4º | |
| propriedade das debêntures dispersa | Art. 71, § 10, line 597 | piece only: br2, art. 71, § 10 | "nenhum debenturista detiver, direta ou indiretamente, mais de metade das debêntures" |
| bônus de subscrição | Art. 75, line 638 | core+br2: `Valor mobiliário`; br2, art. 75 | |
| fundadores (na subscrição particular, todos os subscritores) | Art. 88, line 718 | core+br2: `Parte` (`o fundador`); br2, art. 88 | |
| voto abusivo | Art. 115, line 928 | piece only: br3, art. 115 | "considerar-se-á abusivo o voto exercido com o fim de causar dano" |
| acionista controlador | Art. 116, lines 942 to 944 | core+br3: `Parte` (`o acionista controlador`); br3 encodes the test at art. 116 | read in br1 (lines 31, 33, 36), br4 (1277), br6 (2127); input elsewhere: `o acionista é acionista controlador (art. 116)`, BOOLEAN |
| assembleia regular (todos os acionistas presentes) | Art. 124, § 4º, line 1059 | piece only: br3, art. 124, § 4º | a deeming rule |
| acionista presente a distância | Art. 127, parágrafo único, line 1091 | piece only: br3, art. 127 | |
| assembleia-geral ordinária, extraordinária | Art. 131, line 1106 | core+br3: `Espécie de assembleia`; br3, art. 131 | |
| maioria absoluta de votos | Art. 129, line 1095 | piece only: br3, art. 129 | "não se computando os votos em branco"; the same words are used in Art. 45, § 4º (br1, line 327); input elsewhere: the piece computes it from `Votação em assembleia` itself |
| liquidez e dispersão no mercado | Art. 137, II, a) and b), lines 1212, 1213 | piece only: br3, art. 137, II | |
| administração; administradores | Arts. 138, 145, lines 1236, 1320 | core+br4: `Parte` (`o administrador`, `o conselho de administração`, `a diretoria`); br4, arts. 138 and 145 | read in all pieces |
| conselheiro independente | Art. 140, § 2º, line 1267 | delegated: "nos termos e nos prazos definidos pela Comissão de Valores Mobiliários" | br4 takes `o conselheiro é independente (art. 140, § 2º)`, BOOLEAN; line 1266 is the superseded wording (Medida Provisória nº 1.040, 2021), struck |
| conselho fiscal permanente | Art. 161, line 1427 | core+br4: field `a companhia tem conselho fiscal permanente`; br4, art. 161 | |
| capital autorizado | Art. 168, line 1497 | core+br4: field `a companhia tem capital autorizado`; br4, art. 168 | |
| exercício social | Art. 175, line 1559 | piece only: br5, art. 175 | read in br3 (line 1111), br4 (1454, 1492), br7 (2389, 2557); input elsewhere: `a data do término do exercício social (art. 175)`, DATE |
| reservas de capital | Art. 182, § 1º, line 1712 | piece only: br5, art. 182, § 1º | read in br1 (lines 81, 84, 141) and br4 (1492); input elsewhere: `a verba é reserva de capital (art. 182, § 1º)`, BOOLEAN |
| ajustes de avaliação patrimonial | Art. 182, § 3º, line 1725 | piece only: br5, art. 182, § 3º | |
| reservas de lucros | Art. 182, § 4º, line 1726 | piece only: br5, art. 182, § 4º | |
| valor justo | Art. 183, § 1º, line 1748 | piece only: br5, art. 183, § 1º | |
| ajustes de exercícios anteriores | Art. 186, § 1º, line 1802 | piece only: br5, art. 186, § 1º | |
| demonstração dos fluxos de caixa; demonstração do valor adicionado | Art. 188, I and II, lines 1843, 1847 | piece only: br5, art. 188 | |
| lucro líquido do exercício | Art. 191, line 1866 | piece only: br5, art. 191 | read in br1 (line 132), br3 (1113), br4 (1363), br6 (2271); input elsewhere: `o lucro líquido do exercício em reais (art. 191)`, NUMBER |
| lucro realizado | Art. 197, § 1º, line 1900 | piece only: br5, art. 197, § 1º | |
| dividendo obrigatório | Art. 202, line 1931 | piece only: br5, art. 202 | read in br3 (lines 1162, 1217), br4 (1363, 1364), br7 (2542); input elsewhere: `o dividendo obrigatório em reais (art. 202)`, NUMBER |
| transformação | Art. 220, line 2035 | piece only: br6, art. 220 | |
| incorporação | Art. 227, line 2078 | piece only: br6, art. 227 | |
| fusão | Art. 228, line 2083 | piece only: br6, art. 228 | |
| cisão | Art. 229, line 2088 | piece only: br6, art. 229 | the four operations are read in br3 (arts. 136 and 137), br2 (art. 231), br7: those pieces take `a deliberação é de incorporação (art. 227)` and its three siblings, BOOLEAN |
| sociedade de economia mista | Art. 235, line 2116 | core+br6: field `a companhia é de economia mista`; br6, arts. 235 to 240 | the text says they are subject to the Law; it does not define them; br3 reads it at line 911 (Art. 110-A, § 14) |
| coligadas | Art. 243, § 1º, line 2145 | piece only: br6, art. 243, § 1º | read in br1 (line 33), br2 (550), br3 (911, 1213), br4 (1392, 1394), br5 (1691); input elsewhere: `a sociedade é coligada (art. 243, § 1º)`, BOOLEAN |
| controlada | Art. 243, § 2º, line 2146 | piece only: br6, art. 243, § 2º | same readers as coligadas; input `a sociedade é controlada (art. 243, § 2º)`, BOOLEAN |
| influência significativa | Art. 243, §§ 4º, 5º, lines 2151, 2153 | piece only: br6, art. 243, §§ 4º and 5º | § 5º presumes it from 20% of the votes |
| investimento relevante | Art. 247, parágrafo único, lines 2186 to 2188 | piece only: br6, art. 247, parágrafo único | 10% (line 2187) of the patrimônio líquido for one coligada or controlada, 15% (line 2188) for all together; Art. 248, § 1º (line 2201) uses the phrase again "nos casos deste artigo", for its own article |
| subsidiária integral | Art. 251, line 2226 | piece only: br6, art. 251 | |
| alienação de controle | Art. 254-A, § 1º, line 2254 | piece only: br6, art. 254-A, § 1º | |
| grupo de sociedades; sociedade de comando; filiadas | Art. 265, § 1º, lines 2331, 2332 | piece only: br7, art. 265 | read in br2 (line 424), br3 (1166, 1218); input elsewhere: `a sociedade participa de grupo de sociedades (art. 265)`, BOOLEAN |
| grupo sob controle brasileiro | Art. 269, parágrafo único, line 2352 | scoped br7: "Para os efeitos do número VII" | |
| grupo constituído | Art. 271, line 2361 | piece only: br7, art. 271 | |
| minoritários (da filiada) | Art. 276, § 1º, line 2388 | scoped br7: "para os efeitos deste artigo" | not the general meaning of "minoritário" (F5) |
| consórcio | Art. 278, §§ 1º, line 2399 | piece only: br7, art. 278 | no legal personality (§ 1º, line 2400) |
| sociedade em comandita por ações | Art. 280, line 2417 | piece only: br7, art. 280 | |
| companhia de menor porte | Art. 294-B, line 2545 | piece only: br7, art. 294-B | "receita bruta anual inferior a R$ 500.000.000,00"; the Law's other small-company threshold is Art. 294 (line 2517, R$ 78.000.000,00), which defines no term |
| valores mobiliários | not defined (used from Art. 4, line 27) | delegated: the CVM's securities law, not this Law | the core lists only the four kinds Art. 109, IV names (`Valor mobiliário`) |
| partes relacionadas (critérios de relevância) | not defined (Art. 110-A, § 12, II, line 901) | delegated: "a serem definidos pela Comissão de Valores Mobiliários" | br3 takes it as an input |

## Instructions to the pieces

1. **Strip the struck text properly before you read, quote or count.**
   A `⟦STRUCK: ... ⟧` span can run over several lines: a line that is just `⟦STRUCK:` opens a span that closes at a `⟧` many lines later.
   Measured on the text file: 501 spans open and 501 close, and 67 of them are multi-line.
   A filter that drops only the lines that begin with `⟦STRUCK` shows the inside of those 67 as live law; for example the superseded `Art. 289` of line 2452 and `Art. 294` of line 2516, both struck.
   This command removes every span and keeps the line count, so line numbers still match the source: `perl -Mutf8 -CSD -0777 -pe 's/⟦STRUCK:(.*?)⟧/"\n" x ($1 =~ tr|\n||)/gse' lei-6404-1976.pt.txt > live.txt` (run it on your own copy, in a folder you may write to).
   What is outside the spans is live, including stray fragments such as a lone `a` before a struck `⟦STRUCK: ) pessoa ...⟧` (line 547).
   The amendment notes ("(Redação dada pela Lei nº ...)") stay in the live text; they sometimes sit alone on the line after the sentence.
   Quote from the raw file with `srcrefs.py quote`, never from `live.txt`; the locators count raw lines, and the live copy has the same numbers.
2. **Article numbers, computed from the live text on 2026-10-22.**
   Live article headings: br1 51, br2 53, br3 35, br4 38, br5 31, br6 57, br7 40 (305 in all, counting `4-A`, `16-A` and the like as their own).
   Eight article numbers have no live opener because the whole article is struck or repealed: 32 and 33 (br1), 60 (br2), 181 and 185 (br5), 241, 242 and 254 (br6, whose live Art. 254-A replaces 254).
   Each is a row of `repealed or blank in this text` in the piece's coverage table.
   `SECTION-INDEX.txt` has two rows that point into struck spans and are not live: `Art. 289` at line 2452 and `Art. 294` at line 2516 (br7).
   Count a heading only where the live text has an opener line.
3. **Spelling traps in the text that defeat a search.**
   Amendments write the ordinal as the letter o, not `º`: `Art. 4o`, `§ 1o`, `Art. 4o-A`; some write the degree sign, `§ 1°` (line 814); line 804 has `Art. 104.A companhia` with no space; line 2227 has `§ lº` with a letter l for the digit 1.
   Search with a class such as `[ºo°]`.
4. **Import the core and redefine nothing in it.**
   The first lines of a module are `IMPORT prelude` and ``IMPORT `br-core` ``.
   Do not declare a type, a constructor or a rule that the Vocabulary table lists, and do not define `YMD`; the stable prelude has none and the core supplies it.
   Do not import another piece.
5. **Use the core's types where they fit, and declare your own only for what is in your articles.**
   A fact that is in the canonical table is asked under its canonical name and type.
   Name everything you define with a citation (Naming conventions, 2).
6. **Write every time limit as a `Prazo`.**
   Count forward and backwards with the core's four rules, and test a threshold by multiplying.
   If a provision counts differently, say so in your own notes and encode that provision's counting yourself, with a citation in the name.
7. **Take what another piece defines as an input.**
   The "Defined terms" table says, for each term, which piece encodes it and, for the terms others read, the canonical input name.
   If you meet a term this table does not list that is defined outside your articles, name the input after the term and the defining article, and say so in your notes.
8. **Return `MAYBE` and assert `NOTHING`** for a case the text does not answer.
9. **Stay inside the stable dialect** (see "What the stable binary does not accept").
   The cheapest check is `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, which must show 0 errors, 0 failed and 0 refused.
10. **Dates.**
    Your range may hold a date the notes above assign to you (br1: the enactment date, line 5; br7: the publication date, line 2592, and Art. 295's entry into force, line 2555).
    If your range has none, say so in your notes and build nothing.
11. **Do not edit `br-core.l4`.**
    The seven pieces are written at the same time against one copy of it, so an edit would change what the others compile against.
12. **Check the article in every `@ref` label yourself.**
    `srcrefs.py check` compares the quoted text with the raw file; it does not compare the article named in the label with the heading above the quoted line.
    The core's own label `27 (src:262)` passed the gate while line 262 is in Art. 39 (Art. 27 is at line 190), and was caught only by listing the governing article of every `src:` line.
    Do that before you finish: for each `src:N`, walk up from line N of the live text to the nearest `Art.` heading and compare.
13. **A misspelt `IMPORT` is a warning, not a failure.**
    See "What the stable binary does not accept": `check.sh` shows it as errors and `l4 check` does not.
    If it is wrong for you, tell the coordinator, and in the meantime work around it in your own module with a note, rather than shadowing a name.

## Coverage table

The keel's range is empty: the Law has no interpretation section, so the keel encodes no provision, and its table has no rows.
There are 0 headings in the range and 0 rows below.
The vocabulary the keel does write is licensed by the lines quoted above each declaration in `br-core.l4`, and listed in "Vocabulary".

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |

## Fork register

Each fork is a place where the keel read the text, or the lack of it, one way and could have read it another.
"Reading taken" is what the core does.

| id | the question | readings seen | reading taken, and why | text that licenses each |
| --- | --- | --- | --- | --- |
| F1 | How is a time limit in days counted? | (a) the event day is day 0 and day N is the last day in time; (b) the event day is day 1; (c) the limit runs to the end of the Nth day after | (a): `DATE PLUS n`. The text has no counting rule; the Código Civil's rule, which says the same, is not deposited here, so it is not imported. All seven pieces count alike | none in this text: every limit says only "no prazo de N dias", "dentro de N dias" or "a contar de" (lines 35, 672, 826, 1220) |
| F2 | How are months and years counted when the target day does not exist, and how does `YMD` treat an impossible date? | (a) stop at the last day of the shorter month; (b) roll into the next month; (c) the day after | (a) for `add months` and `add years` (31 Aug + 6 months is 28 Feb 2027; 29 Feb 2024 + 1 year is 28 Feb 2025), because that is what `daydate` does and it is the least surprising. `YMD` itself inherits `Date`'s leniency (`YMD 2023 2 29` is 1 March 2023, reported nowhere) | none in this text; asserted as conventions in `br-core-tests-prazo.l4`, marked F2 |
| F3 | Which forms of share are still lawful? | (a) only nominativas (Art. 20: "As ações devem ser nominativas", reworded by Lei 8.021/1990, line 151); (b) nominativas, endossáveis, ao portador and escriturais, as Arts. 21, 22 parágrafo único, 26, 38, 112 and 292 still name them | the core names all four and decides none: the restriction is a rule of br1 (Art. 20 against Arts. 21 and 22) and br3 (Art. 112), each of which records its reading. The Arts. 32 and 33, which governed endossáveis and ao portador, are struck and marked repealed by the same Lei 8.021 | lines 151 (Art. 20), 153, 156, 187, 250, 919, 2493 (live) against lines 220 and 230 (struck), 231 ("Revogado pela Lei nº 8.021") |
| F4 | What is "nominativas endossáveis" (Art. 112) and "endossável" (Art. 21)? | (a) one form, the endossável share; (b) two forms, nominativa and endossável | (a): `ações endossáveis`. Art. 21 says "forma nominativa ou endossável" and Art. 112 lists "nominativas endossáveis e escriturais"; with the heading above Art. 112 ("Não Exercício de Voto pelas Ações ao Portador", line 918) this reads as every form but ao portador. br3 may read it differently and say so | lines 153, 156, 919 |
| F5 | Who is "o acionista minoritário"? | (a) any shareholder who is not the controlador of Art. 116; (b) a holder under a percentage threshold (Arts. 4-A, 141 and 161, § 2º give a right to holders of 10% of the shares in circulation or of the capital, or "0,1 (um décimo)"); (c) the meaning of Art. 276, § 1º, "todos os sócios da filiada, com exceção da sociedade de comando e das demais filiadas" | (a) as the role in `Parte`, because the Law never defines the general term: the thresholds are rights of particular articles, which the pieces encode, and Art. 239 gives "a minoria" a seat on the board of a sociedade de economia mista without saying who that is. Art. 276, § 1º is scoped by its own words ("para os efeitos deste artigo") and is br7's, not the general meaning | lines 34 to 36, 942, 1271, 1429, 2129, 2388 |
| F6 | One type for persons and organs, or two? | (a) `Parte` holds both; (b) `Parte` for persons and `Órgão` for bodies | (a): a regulative rule has one `PARTY` type, and the text allocates powers and duties to organs and persons alike (Art. 123: "compete ao conselho de administração, se houver, ou aos diretores"; Art. 210: "deveres do liquidante") | lines 1034, 1989 |
| F7 | Is "has nominal value" a fact of the company or of the shares? | (a) of the company; (b) of the shares | (b): the estatuto says whether the shares have nominal value (Art. 11, caput) and a company may have shares with and without it (Art. 167, § 3º), so the fact is a field of `Participação do acionista` | lines 70, 71, 1495 |
| F8 | Which securities does `Valor mobiliário` hold? | (a) every "valor mobiliário" the Law mentions; (b) the four kinds Art. 109, IV lists | (b): "valores mobiliários" in general is a CVM notion the Law does not define; cédulas (Art. 72), certificates of deposit (Art. 43) and commercial paper are a piece's own types | line 833 |
| F9 | Who decides the open/closed test, the keel or br1? | (a) the core carries only the type; (b) the core carries the test | (a): the test (securities "admitidos à negociação no mercado de valores mobiliários") is Art. 4, br1's provision | line 27 |
| F10 | Do the votes of a plural-voting class count in a quorum stated in percentages of shares or capital? | (a) as votes; (b) one per share | the core decides nothing: Art. 110-A, § 9º says a quorum "com base em percentual de ações ou do capital social" disregards plural voting, which is br3's rule; `Votação em assembleia` holds votes, so a piece that tests a share quorum uses `a quantidade de ações do acionista`, not the vote counts | line 887 |
| F11 | Do the enactment and entry-into-force dates belong in the core? | (a) in the core; (b) in the pieces that own the lines | (b): lines 5 and 2555 to 2592 are in br1's and br7's ranges, and the brief puts a date with the piece whose range contains it | lines 5, 2555, 2592 |

## What the stable binary does not accept

Measured on the stable `l4` 1.6.98 (`1.6.98 (main, 7689b0d, 2026-10-19)`) on 2026-10-22.
The 58 numbered probes in `writing-l4-rules/references/dialect-probes/` were each run through `l4 check` with that binary: 56 exit non-zero.
Probes 49 and 50 (`IMPORT hierarchy`, ``IMPORT `negation-as-failure` ``) exit 0 and print `Module not found` as a warning; `dialects.md` calls both rejected (see the import trap below).
The pieces that need the detail read `references/dialects.md` ("write instead" column); the ones that matter most for this Law, with the probe number in brackets:

- `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (02, 03, 04): return a `MAYBE` and assert `NOTHING`; `LEST BREACH ... BECAUSE` is accepted.
- `@lang` (01), `@infixl` (45), `@nonassertable` (46), `@nonexhaustive` (47) and an unknown annotation (48): leave them out.
- `@nlg:pt` is not one of the 58 and is not rejected: it degrades to an untagged `@nlg` whose text begins `:pt` (`dialects.md`, row on `degrades-nlg-language-tag`), so leave it out too.
- A section `GIVEN` followed by a second rule, a directive or a `§§` heading (06 to 12): put a `GIVEN` on every rule that reads the input.
- `TYPICALLY` on a field or a `GIVEN` (13 to 16): leave it out and put the presumed value in the `@desc`.
- An opaque `DECLARE T` with no body (17): give the type one field.
- `SET OF`, `setFromList`, `UNION` (18 to 22): use a `LIST OF` and `elem`.
- `YMD` (05): use the core's `YMD`.
- `RULES EFFECTIVE DATE` (36, 37) and the temporal built-ins (38 to 40, 57, 58): take the version date as an input.
- `EVERY`, `WHOSE` (28 to 30): one obligation for one named party.
- An `AFTER` window on an obligation (32, 33) and `WITHIN ... OF THE DEADLINE` (31): not accepted.
- `WAIT UNTIL` in a `#TRACE` (55) is spelled `WAITUNTIL`; `IS INTEGER` (54) is `ISINTEGER`; `MUST DO` (56) is `MUST`.
- `NOT a AND b` reads as `NOT (a AND b)`: always bracket a `NOT`.
- A field read inside an action (51), and a rule applied inside `MUST (...)` (42): use `PROVIDED`.
- Two spellings that compile and answer differently, so nothing warns you (`dialects.md`): an input named inside an action (`MUST Pay Borrower creditor 10`) matches any payload on `main`, so paying a stranger fulfils the obligation, and a `LEST` after `MAY` is ignored, so a lapsed `MAY` is `FULFILLED`.
  Compare with `PROVIDED payee EQUALS creditor`, and make inaction that should be a breach a `MUST`.

Found while writing the core, and not in `dialects.md`:

- A case pattern with fields is `WHEN `prazo em dias` n THEN ...` (the constructor, then the bound names). `WHEN `prazo em dias` WITH `quantidade de dias` THEN ...` is a parse error: "unexpected WITH".
- Two enumerations that share a constructor name compile, and the error comes at the first use: "There are multiple definitions for the identifier ... and I do not have sufficient information to make a choice between them". That is why every constructor is a full noun phrase and every name a piece defines carries a citation.
- A multi-word type name needs back-ticks where it constructs a record: `` `Perfil da companhia` WITH ... ``.
- **An unresolved `IMPORT` fails neither `l4 check` nor `l4 run`.**
  Measured with stand-in files whose second line was ``IMPORT `br-corre` ``: both verbs exit 0 and print `Warning | [Import Resolution] Module not found: br-corre`, and `l4 run` still prints the result of an `#EVAL` that does not need the module; `check.sh` counted 9 errors for the same kind of file.
  Read the `check.sh` table, and search the output for `Module not found`; never trust an exit status.
- `daydate` on this binary has `add months` and `add years` (they stop at the last day of a shorter month, and accept a negative count), has `DATE PLUS n` and `DATE MINUS n` in days, and has no `YMD`.

## What check.sh prints

Run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` in this folder on 2026-10-22, with `L4_BIN` the stable binary above:

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
br-core-tests-prazo.l4                         0        29       0        0         0
br-core-tests-vocabulario.l4                   0        39       0        0         0
br-core.l4                                     0         0       0        0         0
TOTAL (3 modules)                              0        68       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

That is 0 errors, 0 failed and 0 refused, and 68 assertions satisfied (29 on the time limits, 39 on the shared types and conventions).
No assertion is meant to fail, so no module has an expected failure.
`python3 -I srcrefs.py check --refs lei-6404-1976.pt.txt br-core.l4` printed `40 src: lines, 10 runs, 40 locators, 0 problems`.
`l4 check` on `br-core.l4` prints `Check succeeded.`, and the output of `l4 run` on each of the three modules contains no line with the word "warning".
Each of the three modules was imported by its own three-line throwaway file in this folder, run with `l4 run`, and the three files were deleted afterwards.
The first evaluated `` `o termo final do prazo` (YMD 2026 4 10) (`prazo em dias` 30) `` and printed `DATE OF 10, 5, 2026`, and the third evaluated `` `[teste] a quantidade do prazo` (`prazo em meses` 6) `` and printed `6`, so both names came from the imported module.
The second imports `br-core-tests-prazo`, which defines no name of its own, so its evidence is that the output has no `Module not found` line; the same search finds 5 such lines in a control file that imports a module that does not exist.
