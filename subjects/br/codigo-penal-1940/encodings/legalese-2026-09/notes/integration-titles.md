# Roadmap titles: re-derived from the source

Integration step 5 of `notes/INTEGRATION-BRIEF.md`, done 2026-09-30 by the `integ-titles` agent.
Only the `title` field of `registers/parts/*.roadmap.json` changed; 45 lines in seven parts, and no other field, file or register.
The merged `registers/encoding-roadmap.json` was **not** regenerated, so it still carries the old titles until `registers/merge-parts.py` is run again.

## Counts

| class | units |
| --- | ---: |
| same: the title already is the rubric printed directly above the article (a trailing amendment note ignored) | 318 |
| fixed: the generator's title was wrong, replaced with the derived one | 45 |
| encoder-kept: an encoder had changed the title; kept as the encoder left it | 71 |
| ambiguous: recorded and left as it was | 0 |
| **total** | **434** |

The 71 encoder-kept units split as follows: 40 agree with the derivation exactly, 15 agree in substance (both say the article has no rubric of its own, in different words), and 16 differ (table below).

All twelve parts validate after the change: `node etc/go/lib/register-validate.mjs encoding-roadmap <part> …/registers/source-bundle.json`, run from `l4wt/br-penal`, printed `register-validate: ok` and exited 0 for each.
As a positive control, the same validator run on a copy of `g4a` with one unit's `title` deleted exits 1 with `FAIL .units[0].title: is required`.

## Method

The article's opening line is found by its number in `source/codigo-penal-1940.txt` (for the 85 units in g1c and g5 whose `anchor` is no longer a line reference), and checked against `anchor` where it is one; all 349 line anchors matched.
From that line the derivation walks upward, skipping blank lines and bare amendment notes: `(Incluído …)`, `(Redação dada …)`, `(Vide …)`, `(Revogado …)` on a line of their own, and the link text `Vigência` that the extraction leaves on a line of its own.
The first line it reaches decides the unit:

- a rubric: at most 250 characters, not a `§`, `Art`, `Parágrafo`, `Pena -`, roman-numeral inciso or letter alínea, not starting lower-case, not ending in `:`, `;` or `,`, and not a heading.
  The title is that line with its trailing amendment note and final full stop removed.
- a heading: `PARTE`, `TÍTULO`, `CAPÍTULO`, `SEÇÃO`, the all-caps name line(s) printed under one, or an all-caps `DISPOSIÇÕES …` line.
- anything else is the end of the previous article's text.

Where the line reached is a heading or text, the article has no rubric of its own and the title is `(sem rubrica: <the article's first eight words> …)`.
This includes an article whose rubric is shared with the article before it (arts. 55–57, 64, 78, 90, 94–95, 106, 144–145, 186, 191, 195, 216), as the brief directs.
For a revoked or vetoed article with no rubric, whose own text is only the note, the title is `(sem rubrica: revogado pela Lei …)` or `(sem rubrica: vetado)`.
Arts. 14 and 18 both open "Diz-se o crime:", so their titles run on into inciso I to tell them apart.

"Encoder-corrected" was measured, not taken from the notes: a unit counts as encoder-corrected when its title at `HEAD` differs from the title in `2472da9`, the commit that generated the twelve parts.
That finds 71 units, including seven in g1c that `notes/g1c.md` does not mention (arts. 79, 80, 91-A, 92, 108, 118, 119), and in g6b arts. 337-P, 338-A, 350, 355, 359-B, 359-D–359-F and 359-H, which `notes/g6b.md` does not list.
Conversely, the brief lists g1a's arts. 14, 18 and 29 as encoder corrections, but `notes/g1a.md` says they were reported and **left as generated**, and `notes/g2b.md` says the same of arts. 144–145; all five are counted as fixed here.

### Three readings worth knowing

- **Art. 281**: its rubric is printed in capitals (`COMÉRCIO, POSSE OU USO DE ENTORPECENTE …`, line 1966) directly above the article, with no `TÍTULO`/`CAPÍTULO` over it, so it is read as a rubric, not a heading.
  g4b's sentence-case title agrees with it.
- **Arts. 359-O, 359-Q, 359-U**: the line in the rubric's position reads `(VETADO)` (lines 2632, 2642, 2664); it is read as a vetoed rubric, which is g5's title.
- **Art. 141**: `Disposições comuns` (line 885) is printed in mixed case in the rubric's position, so it counts as the rubric; the title was already that.

## Every change

The source line is the rubric's line, or, where there is no rubric, the article's opening line.

| unit | old title | new title | source line |
| --- | --- | --- | --- |
| g1a art. 14 | Relevância da omissão (Incluído pela Lei nº 7.209, de 11.7.1984) | (sem rubrica: Diz-se o crime: I - consumado …) | 85 (article; no rubric above it) |
| g1a art. 18 | Crime impossível (Redação dada pela Lei nº 7.209, de 11.7.1984) | (sem rubrica: Diz-se o crime: I - doloso …) | 98 (article; no rubric above it) |
| g1a art. 29 | DO CONCURSO DE PESSOAS | (sem rubrica: Quem, de qualquer modo, concorre para o crime …) | 150 (article; no rubric above it) |
| g1b art. 32 | DAS ESPÉCIES DE PENA | (sem rubrica: As penas são) | 161 (article; no rubric above it) |
| g1b art. 55 | Penas restritivas de direitos | (sem rubrica: As penas restritivas de direitos referidas nos incisos …) | 272 (article; no rubric above it) |
| g1b art. 56 | Penas restritivas de direitos | (sem rubrica: As penas de interdição, previstas nos incisos I …) | 273 (article; no rubric above it) |
| g1b art. 57 | Penas restritivas de direitos | (sem rubrica: A pena de interdição, prevista no inciso III …) | 274 (article; no rubric above it) |
| g1b art. 64 | Reincidência | (sem rubrica: Para efeito de reincidência) | 316 (article; no rubric above it) |
| g1c art. 78 | Requisitos da suspensão da pena | (sem rubrica: Durante o prazo da suspensão, o condenado ficará …) | 367 (article; no rubric above it) |
| g1c art. 90 | Extinção | (sem rubrica: Se até o seu término o livramento não …) | 415 (article; no rubric above it) |
| g1c art. 94 | Reabilitação | (sem rubrica: A reabilitação poderá ser requerida, decorridos 2 (dois) …) | 466 (article; no rubric above it) |
| g1c art. 95 | Reabilitação | (sem rubrica: A reabilitação será revogada, de ofício ou a …) | 471 (article; no rubric above it) |
| g1c art. 106 | Perdão do ofendido | (sem rubrica: O perdão, no processo ou fora dele, expresso …) | 512 (article; no rubric above it) |
| g2b art. 144 | Retratação | (sem rubrica: Se, de referências, alusões ou frases, se infere …) | 909 (article; no rubric above it) |
| g2b art. 145 | Retratação | (sem rubrica: Nos crimes previstos neste Capítulo somente se procede …) | 910 (article; no rubric above it) |
| g2b art. 147-B | (Incluído pela Lei nº 14.188, de 2021) | Violência psicológica contra a mulher | 947 (rubric) |
| g2b art. 147-C | (Incluído pela Lei nº 14.188, de 2021) | (sem rubrica: Ameaçar alguém, por palavra, escrito ou gesto, ou …) | 954 (article; no rubric above it) |
| g2b art. 154-A | Vigência | Invasão de dispositivo informático | 1049 (rubric) |
| g2b art. 154-B | Vigência | Ação penal | 1082 (rubric) |
| g3b art. 186 | Usurpação de nome ou pseudônimo alheio | (sem rubrica: Procede-se mediante) | 1419 (article; no rubric above it) |
| g3b art. 187 | Violação de privilégio de invenção ⟦STRUCK: | Violação de privilégio de invenção | 1426 (rubric) |
| g3b art. 189 | Usurpação ou indevida exploração de modelo ou desenho privilegiado ⟦STRUCK: | Usurpação ou indevida exploração de modelo ou desenho privilegiado | 1430 (rubric) |
| g3b art. 191 | Falsa declaração de depósito em modelo ou desenho | (sem rubrica: revogado pela Lei nº 9.279, de 14.5.1996) | 1434 (article; no rubric above it) |
| g3b art. 194 | Marca com falsa indicação de procedência ⟦STRUCK: | Marca com falsa indicação de procedência | 1442 (rubric) |
| g3b art. 195 | Marca com falsa indicação de procedência ⟦STRUCK: | (sem rubrica: revogado pela Lei nº 9.279, de 14.5.1996) | 1444 (article; no rubric above it) |
| g3b art. 196 | Concorrência desleal ⟦STRUCK: | Concorrência desleal | 1447 (rubric) |
| g4a art. 214 | (Incluído pela Lei nº 12.015, de 2009) | (sem rubrica: revogado pela Lei nº 12.015, de 2009) | 1533 (article; no rubric above it) |
| g4a art. 216 | Importunação sexual (Incluído pela Lei nº 13.718, de 2018) | (sem rubrica: revogado pela Lei nº 12.015, de 2009) | 1541 (article; no rubric above it) |
| g4a art. 218-A | Parágrafo único. (VETADO). (Incluído pela Lei nº 12.015, de 2009) | Satisfação de lascívia mediante presença de criança ou adolescente | 1580 (rubric) |
| g4a art. 218-B | (Redação dada pela Lei nº 15.280, de 2025) | Favorecimento da prostituição ou de outra forma de exploração sexual de criança ou adolescente ou de vulnerável | 1584 (rubric) |
| g4a art. 218-C | § 2o Incorre nas mesmas penas: (Incluído pela Lei nº 12.015, de 2009) | Divulgação de cena de estupro ou de cena de estupro de vulnerável, de cena de sexo ou de pornografia | 1594 (rubric) |
| g4a art. 223 | DISPOSIÇÕES GERAIS | (sem rubrica: revogado pela Lei nº 12.015, de 2009) | 1614 (article; no rubric above it) |
| g4a art. 224 | DISPOSIÇÕES GERAIS | (sem rubrica: revogado pela Lei nº 12.015, de 2009) | 1615 (article; no rubric above it) |
| g4a art. 228 | § 3º - Se o crime é cometido com o fim de lucro, aplica-se também multa. | Favorecimento da prostituição ou outra forma de exploração sexual | 1642 (rubric) |
| g4a art. 231 | Pena - reclusão, de 3 (três) a 6 (seis) anos, e multa. (Redação dada pela Lei nº 12.015, de 2009) | Tráfico internacional de pessoa para fim de exploração sexual | 1660 (rubric) |
| g4a art. 231-A | (Revogado pela Lei nº 13.344, de 2016) (Vigência) | (sem rubrica: revogado pela Lei nº 13.344, de 2016) | 1663 (article; no rubric above it) |
| g4a art. 232 | (Revogado pela Lei nº 13.344, de 2016) (Vigência) | (sem rubrica: revogado pela Lei nº 12.015, de 2009) | 1665 (article; no rubric above it) |
| g4a art. 234-B | II – (VETADO); (Incluído pela Lei nº 12.015, de 2009) | (sem rubrica: Os processos em que se apuram crimes definidos …) | 1695 (article; no rubric above it) |
| g4a art. 234-C | (Incluído pela Lei nº 15.035, de 2024) | (sem rubrica: vetado) | 1701 (article; no rubric above it) |
| g4a art. 247 | Pena - detenção, de quinze dias a um mês, ou multa. | (sem rubrica: Permitir alguém que menor de dezoito anos, sujeito …) | 1754 (article; no rubric above it) |
| g4b art. 266 | Vigência | Interrupção ou perturbação de serviço telegráfico, telefônico, informático, telemático ou de informação de utilidade pública | 1876 (rubric) |
| g4b art. 272 | Pena - detenção, de dois meses a um ano. | Falsificação, corrupção, adulteração ou alteração de substância ou produtos alimentícios | 1917 (rubric) |
| g4b art. 273 | Pena - detenção, de 1 (um) a 2 (dois) anos, e multa. (Redação dada pela Lei nº 9.677, de 2.7.1998) | Falsificação, corrupção, adulteração ou alteração de produto destinado a fins terapêuticos ou medicinais | 1925 (rubric) |
| g4b art. 282 | Pena - detenção, de dois meses a um ano. | Exercício ilegal da medicina, medicina veterinária, arte dentária ou farmacêutica | 1968 (rubric) |
| g4b art. 288-A | (Incluído dada pela Lei nº 12.720, de 2012) | Constituição de milícia privada | 2006 (rubric) |

## Encoder-kept titles that differ from the derivation

Kept as the encoders left them, per the brief.
The derived title is what this pass would have written.

| unit | encoder's title (kept) | derived | source line |
| --- | --- | --- | --- |
| g1c art. 79 | Requisitos da suspensão da pena | (sem rubrica: A sentença poderá especificar outras condições a que …) | 373 |
| g1c art. 80 | Requisitos da suspensão da pena | (sem rubrica: A suspensão não se estende às penas restritivas …) | 374 |
| g1c art. 91-A | Efeitos genéricos e específicos | (sem rubrica: Na hipótese de condenação por infrações às quais …) | 427 |
| g1c art. 92 | Efeitos genéricos e específicos | (sem rubrica: São também efeitos da condenação) | 435 |
| g1c art. 108 | Extinção da punibilidade | (sem rubrica: A extinção da punibilidade de crime que é …) | 531 |
| g1c art. 118 | Causas interruptivas da prescrição | (sem rubrica: As penas mais leves prescrevem com as mais …) | 586 |
| g1c art. 119 | Causas interruptivas da prescrição | (sem rubrica: No caso de concurso de crimes, a extinção …) | 587 |
| g2a art. 126 | Aborto provocado por terceiro, com o consentimento da gestante | (sem rubrica: Provocar aborto com o consentimento da gestante) | 718 |
| g2a art. 128 | Aborto necessário; aborto no caso de gravidez resultante de estupro | (sem rubrica: Não se pune o aborto praticado por médico) | 723 |
| g3 art. 170 | Aplicação do art. 155, § 2º, aos crimes do Capítulo V | (sem rubrica: Nos crimes previstos neste Capítulo, aplica-se o disposto …) | 1280 |
| g3 art. 171-A | Fraude com ativos virtuais, valores mobiliários ou ativos financeiros (sem rubrica no texto) | (sem rubrica: Organizar, gerir, ofertar ou distribuir carteiras ou intermediar …) | 1318 |
| g3 art. 181 | Isenção de pena (Disposições gerais) | (sem rubrica: É isento de pena quem comete qualquer dos …) | 1392 |
| g3 art. 182 | Ação penal condicionada à representação (Disposições gerais) | (sem rubrica: Somente se procede mediante representação, se o crime …) | 1395 |
| g3 art. 183 | Exceções aos arts. 181 e 182 (Disposições gerais) | (sem rubrica: Não se aplica o disposto nos dois artigos …) | 1399 |
| g3 art. 183-A | Aumento de pena nos crimes contra instituições financeiras e prestadores de segurança privada | (sem rubrica: Nos crimes de que trata este Título, quando …) | 1403 |
| g6b art. 355 | Patrocínio infiel; parágrafo único: Patrocínio simultâneo ou tergiversação | Patrocínio infiel | 2516 |

Two patterns account for all but one:

- **g1c titles an article with no rubric by the rubric it shares with the article before** (79–80 under art. 77's, 91-A and 92 under art. 91's, 108 under art. 107's, 118–119 under art. 117's).
  Following the brief, this pass gave the generator's titles of the same kind in g1c (arts. 78, 90, 94, 95, 106) the `(sem rubrica: …)` form, so **g1c now mixes the two conventions**.
- **g2a and g3 give an article with no rubric a descriptive title in their own words** (126, 128, 170, 171-A, 181–183-A), without marking it as not the Code's, except 171-A, which says `(sem rubrica no texto)`.
  Art. 128's is built from the rubrics printed on its two incisos (`Aborto necessário`, `Aborto no caso de gravidez resultante de estupro`).

The one other: art. 355's title adds the rubric printed on its parágrafo único (`Patrocínio simultâneo ou tergiversação`).

The 15 that agree in substance, each saying in its own words that the article has no rubric: g1b art. 44, g1b art. 66, g5 art. 295, g5 art. 308, g5 art. 310, g5 art. 359-M-A, g5 art. 359-M-B, g5 art. 359-T, g5 art. 360, g5 art. 361, g6a art. 319-A, g6b art. 337-P, g6b art. 343, g6b art. 346, g6b art. 349-A.

The 40 that agree exactly: g2a art. 121-A, g2a art. 121-B, g2a art. 122, g2a art. 135-A, g4b art. 281, g5 art. 298, g5 art. 306, g5 art. 359-I, g5 art. 359-J, g5 art. 359-K, g5 art. 359-L, g5 art. 359-M, g5 art. 359-N, g5 art. 359-O, g5 art. 359-P, g5 art. 359-Q, g5 art. 359-R, g5 art. 359-U, g6a art. 313-B, g6a art. 337-C, g6b art. 337-E, g6b art. 337-F, g6b art. 337-G, g6b art. 337-H, g6b art. 337-I, g6b art. 337-J, g6b art. 337-K, g6b art. 337-L, g6b art. 337-M, g6b art. 337-N, g6b art. 337-O, g6b art. 338-A, g6b art. 350, g6b art. 359-B, g6b art. 359-C, g6b art. 359-D, g6b art. 359-E, g6b art. 359-F, g6b art. 359-G, g6b art. 359-H.

## Left alone, and worth a later pass

- **33 titles still end in an amendment note**, such as `Lugar do crime (Redação dada pela Lei nº 7.209, de 1984)` (g1a art. 6).
  They are the rubric, so they were classed "same" and not touched; the titles this pass wrote carry no note, and g6b's encoder stripped theirs from arts. 359-B–359-H, so the parts now mix both forms.
- **Three conventions for "no rubric"** are in use: this pass's `(sem rubrica: <first words> …)`, g1b's `(sem rubrica própria; sob "<rubric>", art. N)`, and g5, g6a and g6b's `(sem epígrafe …)` / `(sem rubrica no texto: <paraphrase>)`.
- **85 anchors are no longer line references**: g1c and g5 replaced `source/codigo-penal-1940.txt:<line>` with a description such as `Art. 77 — Requisitos da suspensão da pena`.
  The validator accepts them; this pass did not touch them.
