# NOTES — br/codigo-penal-1940, encoding row `legalese-2026-09`

## 0. Verification status, 2026-10-11

**Status: `draft`, `not_reviewed`.**
No lawyer has read this encoding against the Código Penal.
The fidelity gate HG1 (a domain expert signs the encoding against the source) was waived.
It was not signed.
The outward-facing gate HG2 is not sought.
Pipeline status: the `l4-ide` pipeline's deposit-path run over this encoding ended COMPLETE with HG1 waived (section 10).

What was run, on the files as they stand:

- Every one of the 241 `.l4` files was run with `l4 run`, one module at a time, under `nice`, with `JL4_LIBRARY_PATH` unset, so the binary used its own embedded standard library.
- The binary is `l4-1008`, a cabal build of l4-ide made on 9 October 2026.
  The commit it was built from was not recorded.
- An older binary, built from l4-ide `unstable` at `73a953821` on 29 September 2026, gave identical per-group totals wherever both were run.
- The composer `cp-codigo-penal.l4` imports all 85 group modules and the three shared modules, and it type-checks.
- The totals of the final check, and of a run by the author of this file, are in section 5.1.
- The tree has no `#EVAL`.
  The `#ASSERT` lines (7,873 by `grep -c '^#ASSERT'` on 2026-10-11, of which 308 are `#ASSERT REFUSED`) are the only verdicts.

A satisfied assertion shows that the encoding agrees with the expectation its author derived from the text; it does not show that the expectation is right.
The encoders wrote the 5,769 assertions in the `-testes` modules.
Only the `cp-ind-*` files (section 5.2) were written by someone who had not seen the encoding, and they are red on purpose where the encoding and the independent author disagree.
So the whole tree does not exit 0.

## 1. What this is, and its scope

An L4 encoding of Brazil's Código Penal, Decreto-Lei nº 2.848 of 7 December 1940, arts. 1 to 361: the Parte Geral and the Parte Especial.
The text encoded is Planalto's compiled text, fetched on 2026-09-29, whose inline citations run through Lei nº 15.517/2026 (dated 22 September 2026, per the research register).
Identifiers, comments and quotations are Portuguese; English glosses are attached for the renderer.
L4 is a typed functional language for rules; its manual is under `doc/` in the `legalese/l4-ide` repository.

The roadmap, `registers/encoding-roadmap.json`, has one unit per article: 434 units by script, and 434 article openers in `../../source/codigo-penal-1940.txt`.

| disposition | units | meaning |
| --- | --- | --- |
| `encoded` | 398 | a rule answers whether the facts make out the provision, or what it computes |
| `inert` | 25 | the text is carried, but no decision reads it |
| `out-of-scope` | 11 | revoked; a labelled stub keeps the numbering gap readable |
| `deferred` | 0 | |

The 25 inert units:

- Arts. 38, 39 and 40 (rights of a prisoner, work of a prisoner, a pointer to special legislation) and art. 85 (an instruction to the sentencing court, whose conditions belong to the Lei de Execução Penal).
  They gate no decision.
- Nineteen revoked or vetoed articles, each a labelled stub: arts. 214, 216, 217, 219 to 224, 231, 231-A, 232, 234-C (vetoed), 240, 279, 281, 359-O, 359-Q and 359-U (vetoed).
- Arts. 360 (a revocation clause with a saving for special legislation) and 361 (the Code's own vigência clause, 1 January 1942).

The 11 out-of-scope units are arts. 185 and 187 to 196.
Art. 185 was revoked by Lei nº 10.695/2003 and arts. 187 to 196 by Lei nº 9.279/1996, and `cp-g3b-propriedade-imaterial.l4` carries a labelled stub for each.
The two dispositions are not used consistently for revoked matter: these 11 are `out-of-scope`, and the 19 revoked or vetoed stubs above are `inert`.

What "encoded" means.
Every punishing provision, each caput and each paragraph that states its own penalty, has a predicate saying whether the facts make out the crime, with consummated and attempted forms where an attempt is possible.
It also has its penalty (species, minimum, maximum and fine, as the preceito secundário states them), each cause of increase or decrease as the fraction the Code states with a predicate saying whether it applies, and the ação penal where the article states one.
The Parte Geral articles are rules over the facts they name.
The judge's choice of a number inside a range is not encoded: a range stays a range, and an open standard ("motivo fútil") is an input finding named in the Code's words.

What is not done:

- Special legislation is not encoded.
  Four special laws that now define crimes are refused by name: Lei 10.826/2003 art. 16 § 1º III, Lei 9.605/1998 art. 61, Lei 11.343/2006 art. 35 and Lei 13.260/2016 (`notes/g4b.md`, § 1).
- The Código de Processo Penal and the Lei de Execução Penal are not encoded; where the Code points to them the answer is an input or a refusal.
- The wording an article had before a later law re-wrote it is not encoded (sections 2.3 and 7).

## 2. How it is built, and how to read it

### 2.1 The twelve encoder groups

After a first pass (group g0) that wrote the shared modules and the conventions, twelve encoders worked in parallel, each on a range of articles.
A module name starts with `cp-` and its group.

| group | prefix | articles | where in the Code | modules | tests | units |
| --- | --- | --- | --- | --- | --- | --- |
| g1a | `cp-g1a-` | 1–31 | Parte Geral, Títulos I–IV | 6 | 6 | 31 |
| g1b | `cp-g1b-` | 32–76 | Parte Geral, Título V, Caps. I–III (penalties) | 8 | 7 | 45 |
| g1c | `cp-g1c-` | 77–120 | Parte Geral, Título V Caps. IV–VII, Títulos VI–VIII (including prescription) | 8 | 7 | 45 |
| g2a | `cp-g2a-` | 121–137 | Parte Especial, Título I (pessoa), Caps. I–IV | 7 | 6 | 20 |
| g2b | `cp-g2b-` | 138–154-B | Título I, Caps. V–VI (honra, liberdade individual) | 7 | 6 | 24 |
| g3 | `cp-g3-` | 155–183-A | Título II (patrimônio) | 11 | 10 | 33 |
| g3b | `cp-g3b-` | 184–212 | Títulos III–V (propriedade imaterial, organização do trabalho, sentimento religioso e mortos) | 4 | 3 | 29 |
| g4a | `cp-g4a-` | 213–249 | Títulos VI–VII (dignidade sexual, família) | 6 | 6 | 49 |
| g4b | `cp-g4b-` | 250–288-A | Títulos VIII–IX (incolumidade pública, paz pública) | 8 | 8 | 40 |
| g5 | `cp-g5-` | 289–311-A, 359-I–361 | Título X (fé pública), Título XII (Estado Democrático de Direito), Disposições Finais | 8 | 7 | 40 |
| g6a | `cp-g6a-` | 312–337-D | Título XI (Administração Pública), Caps. I, II, II-A | 7 | 5 | 34 |
| g6b | `cp-g6b-` | 337-E–359-H | Título XI, Caps. II-B, III, IV | 5 | 5 | 44 |

"Tests" counts `-testes` modules; "modules" counts the other `cp-gN-*.l4` files except four fixtures (`cp-g1b-casos.l4`, `cp-g3-casos.l4`, `cp-g5-casos.l4`, `cp-g6a-casos.l4`) that hold no assertions.

### 2.2 The shared modules and the rest of the directory

- `cp-dominio.l4` declares the shared nouns (`Pessoa`, `Agente`, `Vítima`, `Coisa`, `Documento`, `Fato`, `Elemento subjetivo` and others); it holds no rule and no assertion.
- `cp-pena.l4` holds the penalty machinery and the Parte Geral articles every group needs: arts. 10, 11, 14, 32, 43, 49, 53, art. 33 caput and § 1º, and art. 58 caput; its tests are `cp-g0-pena-testes.l4`.
- `cp-vigencias.l4` holds the day each amending law came into force, for the seven laws that more than one group needed.
- `cp-codigo-penal.l4` is the composer and the main module.
  It has no rule and no directive; it imports the three shared modules and the 85 group modules in the Code's order, and leaves out the `-testes` and `-casos` modules.
- `cp-gN…-testes.l4` is one tests module per module (76, plus `cp-g0-pena-testes.l4`), written by the encoders from the text; `cp-ind-gN-*.l4` are the 71 independent test files (section 5.2).
- `notes/gN.md` is each group's record: what it encoded, its forks in prose, its questions for a lawyer.
  `notes/independent-gN.md` and `notes/integration*.md` record the independent test pass and the integration pass.
  The probe files in `notes/cp-g0-sondas/` and `notes/cp-g1b-sondas/` include several that fail on purpose, each as evidence for a trap in `PLAN.md` § 12.
- `registers/` holds the roadmap, the fork register, the register of later norms and court decisions (`external-modifications.json`), the source bundle, and `parts/`, the per-group files they were merged from.
  The registers name modules as `jl4/examples/legal/br-codigo-penal/encodings/legalese-2026-09/<file>`, the path used while the work was done inside l4-ide; the same files are here at `subjects/br/codigo-penal-1940/encodings/legalese-2026-09/<file>`.
- `BRIEF.md` and `PLAN.md` are the specification the groups worked from: `PLAN.md` § 0 is the group map, § 2 the penalty representation, § 10 the vigência convention, § 12 the traps.

### 2.3 Conventions a reader must know

- **Finding an article.** The `§` headings follow the Code's numbering (``§§§ `Art. 155 — Furto` ``).
  Each rule carries `@ref CP art. 155, § 4º, II` and, above it, the article's words copied from the source.
  Names are regular: `crime de furto (art. 155)`, `pena do art. 155, § 4º` (a constant equal to the preceito secundário), `incide o aumento do art. 155, § 1º`.
- **Language.** Identifiers are the Code's own Portuguese words, and every module starts with `@lang pt` (checked by `grep -L`).
  Each of the 830 exported rules has an English gloss in `@nlg:en` before its body (checked by script).
  The brief required one on every record field too; that was not audited.
  The renderer's connective words ("with", "where", "is") are English in both languages; that is the renderer, not the encoding.
- **Nouns before rules.** Facts a witness could testify to (the thing was movable, the victim was 13) are record fields supplied as input; whether they make out an offence is a rule.
  Ages are never stored: a rule takes a birth date and the date the provision names.
- **Where the source does not answer, `REFUSE`.**
  A rule returns a named refusal rather than `FALSE`, `0` or a plausible default (138 `REFUSE` expressions in the non-test modules, by `grep`).
  A recorded fork is different: the encoding took one reading of an ambiguous text and kept the others on file.
- **Vigência.** A rule answers only for facts dated within the vigência of the text encoded.
  For an article re-written by a later law, every penalty rule first checks the fact's date and, before the law took effect, refuses by name ("a redação do art. 155 anterior à Lei nº 15.397, de 2026, não está codificada"), because the earlier wording is not in the source.
  A paragraph a later law added simply does not apply to earlier facts.
  No module uses the `RULES EFFECTIVE DATE` axis (`grep` finds none).
  The rule is `PLAN.md` § 10.
- **Penalties.** A length of time is a `Duração`, one exact number of months (a year is 12, a day 1/30).
  A penalty is a `Pena cominada` record with `espécie`, `mínimo`, `máximo` and `multa`, always built with `WITH` so that two bounds cannot be swapped.
  A cause is the fraction added: "o dobro" is 1 and "o triplo" is 2.
  A period the Code states in days is counted in days (`o último dia do prazo em dias`), not as months.
  `PLAN.md` § 2 gives the rest.
- **Forks.** Each ambiguity has an id (`F-g2a-02`, or `F-sweep-b-19` where the research on later norms reserved it), cited in a comment at the rule.
  The register entry gives the readings, the one taken, how the choice is expressed (section 6), and tests that exhibit the difference.

## 3. The source and its terms

The text encoded is `../../source/codigo-penal-1940.txt`, 2,675 lines, one source paragraph per line, extracted from Planalto's compiled HTML fetched on 2026-09-29.
Its SHA-256 is `899c987e…3272a`, pinned in `../../source/SHA256SUMS` and `registers/source-bundle.json`; it was re-computed on 2026-10-11 and matches.
Revoked matter that Planalto shows struck through is wrapped `⟦STRUCK: …⟧` (6 spans).
Planalto's page says that only the Diário Oficial text is official.
`../../source/README.md` records how the files were made.

**Was LexML's structured XML any use?**
No, because there was none to use.
LexML defines a full-text XML schema, but no instance of the Código Penal in it was found anywhere LexML leads: its record offers three `text/html` copies, the Senado's open-data API returns metadata and not text, and the viewer normas.leg.br publishes `text/html`.
The Code was therefore converted to plain text at once and its structure recovered by pattern, which cost three missed article numbers on the first pass.
The one structured source that helped was the Senado's metadata (`senado-dadosabertos-527942.xml`): 164 later norms that touched a dispositivo, with dates.
Planalto's inline `(Vide …)` pointers number 38 and were inventoried as V1 to V38.

`SOURCE-LICENSE.md` records the terms.
The statute's text is not protected by copyright (Lei 9.610/1998 art. 8º IV), so it may be quoted.
Whether Planalto's editorial notes are protected is not settled; the encoding quotes the statute and not the notes.

## 4. How it was made, honestly

The work was done by language models (Claude Opus 5.5 for the first pass, Claude Sonnet 5.5 for later fixes and tests), directed by one conducting session.
The project's maintainer ruled on the questions the agents raised, and the rulings are dated in the notes.
The brief forbade reading any other encoding of this Code or of any other penal code; that was an instruction to the agents, and nothing in the tree checks it.

1. **Source.** The text was fetched, extracted and checked for completeness (every article number from 1 to 361 present).
2. **Ontology pass.** One agent wrote `cp-dominio.l4`, `cp-pena.l4`, `PLAN.md` and the worked example for art. 155, and measured the toolchain's traps.
3. **Research on later norms.** Three agents, for arts. 1–120, 121–212 and 213–361, swept the `(Vide …)` pointers, the Senado's metadata, later amending laws and court decisions (section 4.1).
4. **Twelve parallel encoders**, as in section 2.1, each writing modules, tests, a roadmap part, a fork part and a note, and each reading the research for its range.
5. **Integration.** Duplicated types, helpers and law dates were hoisted into the shared modules, the composer was written, and one cross-group question was ruled (art. 327; `notes/integration.md`).
6. **Independent tests.** Six test authors, separate agents who had not seen the encoding, wrote 2,148 cases from the source text alone, before the encoding existed, each with an expected answer and an arguable flag.
   The cases were then turned into the `cp-ind-*` assertions and every disagreement was classified (section 5.2).
7. **Fix round.** Encoders (mostly Sonnet agents) changed the encoding where a disagreement showed a defect.
   The test authors then re-ran their files, changing only fixtures to supply fields the encoding had made required, and never an expected value.
8. **Knowledge-requirement audit.** The independent pass showed that some crimes of possession or dealing convicted without reading whether the agent knew the quality of the thing (art. 18, parágrafo único; art. 20).
   An audit of the rest of the Code found 13 provisions in six groups with the same defect: arts. 175, 184 § 2º, 218-C, 234, 253, 270 § 1º, 272, 273, 276, 277, 278, 334-A § 1º IV–V and 337-M.
   Each now requires a local knowledge finding (forks F-g3-32, F-g3b-26, F-g4a-25, F-g4b-29, F-g6a-24, F-g6b-24); the same defect in Título X and art. 359-K is F-g5-34.
9. **Mutation testing.** Each encoder broke its own rules one change at a time on a scratch copy and checked that a test failed.
   The counts are in each `notes/gN.md` (20 changes in g1b, 49 in g1c, 24 in g3b, 21 in g6a, 43 in g6b) and are uneven: g4b ran 6, and g3's first pass covered only two modules.
   A later mutation pass over g3's other modules led to 54 gap assertions being added (`notes/g3.md` § 12).

### 4.1 The register of later norms and court decisions

`registers/external-modifications.json` has 126 entries from 51 searches (26 by publisher page, 9 web searches, 8 agency indexes, 5 court dockets, 3 manual).

| class | entries | meaning |
| --- | --- | --- |
| `binding` | 21 | a ruling or law struck, stayed, read down, restricted, substituted or added to a provision |
| `interpretive` | 100 | chooses between readings of the text; the encoder opened or settled a fork |
| `prospective` | 5 | not yet law (pending vetoes, bills, suspended rulings) |

Of the 21 binding entries, 7 read down, 6 substituted, 3 added, 2 struck, 2 restricted and 1 stayed a provision (the register's `binding_effect`).
Fifteen entries carry `currency_risk: true`, meaning the situation may have changed since 2026-09-29.
**The `disposition` field was not updated after the encoders acted.**
92 entries still say `deferred`, the value the sweep gave them; 26 say `no-effect`, 6 `subsumed`, 2 `scoped-out`, and none says `encoded`.
What each encoder did with each entry is in the table of sweep entries in its `notes/gN.md` and in the forks' `settled_by` field.

## 5. Results

### 5.1 The encoders' own tests

Assertions in the `-testes` modules by `grep -c '^#ASSERT'` on 2026-10-11, 5,769 in all:

| g0 | g1a | g1b | g1c | g2a | g2b | g3 | g3b | g4a | g4b | g5 | g6a | g6b |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 124 | 276 | 407 | 486 | 528 | 509 | 646 | 345 | 449 | 579 | 537 | 452 | 431 |

The final check, `check.sh` over all 241 files on 2026-10-11 with `l4-1008` under `nice -n 15`, gave 7,873 assertions: 7,818 satisfied, 42 failed, 13 refused, none unaccounted, and every one of the 55 that are not satisfied is in a `cp-ind-*` file.
A second run the same day, by the author of this file, covered all 241 files again, one module at a time, and gave the same per-module counts.
The 170 files that are not independent tests gave 0 errors, 0 failed, 0 refused, and 5,769 of 5,769 assertions satisfied.
The 71 `cp-ind-*` files gave 2,049 satisfied, 42 failed and 13 refused of 2,104 (section 5.2).
Every assertion produced a verdict: satisfied, failed and refused add up to 7,873, the number of `#ASSERT` lines.

### 5.2 The independent tests, and why part of the tree is red

The six independent authors wrote 2,148 cases; 2,104 could be expressed as an assertion and 44 could not (the encoding leaves the point to the judge, or has no field for the fact).
The encoding agrees with 2,049 of the 2,104.
The other 55 are disagreements, kept as failing or refused assertions in the `cp-ind-*` files, and each is triaged.
The classes: **E** the encoding departs from the text; **T** the test author misread the text; **F** a recorded fork took the other reading; **S** a later sweep entry or court ruling changed the answer; **R** the strict vigência ruling (section 7, limit 1).

| files | articles | cases | expressed | not expressible | agree | disagree | E | T | F | S | R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cp-ind-g1-*` | 1–120 | 339 | 333 | 6 | 311 | 22 | 0 | 0 | 11 | 4 | 7 |
| `cp-ind-g2-*` | 121–154-B | 383 | 380 | 3 | 372 | 8 | 0 | 0 | 5 | 3 | 0 |
| `cp-ind-g3-*` | 155–212 | 401 | 391 | 10 | 386 | 5 | 0 | 0 | 2 | 3 | 0 |
| `cp-ind-g4-*` | 213–288-A | 408 | 405 | 3 | 397 | 8 | 0 | 0 | 5 | 3 | 0 |
| `cp-ind-g5-*` | 289–311-A, 359-I–361 | 232 | 223 | 9 | 217 | 6 | 0 | 0 | 4 | 2 | 0 |
| `cp-ind-g6-*` | 312–359-H | 385 | 372 | 13 | 366 | 6 | 0 | 1 | 1 | 3 | 1 |
| total | | 2,148 | 2,104 | 44 | 2,049 | 55 | 0 | 1 | 28 | 18 | 8 |

The table is the latest section of each `notes/independent-gN.md`, as committed on 2026-10-11, and it matches the run in section 5.1.
Two E rows were closed in the last fix round: IT-g4-173 (art. 234-B § 3º) and IT-g5-115 (art. 304, the forger who uses the paper they forged).
Both agree now because the encoding refuses where the text does not decide (forks F-g4a-24 and F-g5-32, now open); the encoders had been told of both cases, so those agreements are fixes and not independent evidence.
Where the test author marked a case arguable, the encoding usually took the reading the case named as its alternative.

## 6. Forks

`registers/fork-register.json` has 423 forks, counted by script.
By kind: 316 statutory-wording, 40 encoding-placement, 34 vagueness, 33 fact-convention.
By status: 365 resolved, 47 settled, 11 open.
By how the choice is expressed (`taken.mechanism`): 354 `encoded` (one reading in the code), 65 `fact-supplied` (an input field carries the choice), 4 `TYPICALLY` (both readings run, one is the default).
`resolved` means an encoder took one reading on argument; `settled` means an authority (a court ruling or súmula) settled it, named in `settled_by`; `open` means no reading of the law was taken.
By the register's `divergence` field, 312 forks are `observable` (the readings give different answers on a test), 54 `none`, 42 `unassessed`, 5 `extensionally-equivalent`, and 10 have no value.
By owner: 25 forks start `F-g0`, 23 `F-g1a`, 33 `F-g1b`, 30 `F-g1c`, 34 `F-g2a`, 21 `F-g2b`, 34 `F-g3`, 26 `F-g3b`, 25 `F-g4a`, 29 `F-g4b`, 34 `F-g5`, 24 `F-g6a`, 24 `F-g6b`, and 61 are `F-sweep-*` ids that the research reserved (19, 24 and 18 for its three parts).

To find the fork behind a rule, read the comment above the rule, which cites the id, or search the register for the rule's name in `site.anchor`.
In the register, `taken` says which reading the code follows and why, and `witnesses` names tests that exhibit the difference.

### 6.1 The eleven open forks

An open fork is one where the encoder took no reading of the law.
Seven of the eleven refuse where the readings part (F-g1c-09, F-g2a-23, F-g2b-01, F-sweep-b-06, F-g4a-24, F-g5-32, F-g6b-04); the others leave the choice to the caller or follow the text as printed.

- F-g0-27 (returns the options and says neither): after art. 155 § 2º, must the judge grant one of the three options?
- F-g1a-13 (left unsaid): in arts. 21, 24 § 2º, 26 p.ú., 28 § 2º and 29 § 1º, once the requirements are met, must the judge reduce?
- F-g1c-09 (refuses): art. 83, for a convict who is not a repeat offender but has no good record, is the fraction one third or one half?
- F-g1c-30 (the day is an input): art. 117, VI, "pela reincidência", on which day does the interruption fall?
- F-g2a-23 (refuses for an anencephalic foetus after 12.4.2012): does the ADPF 54 read-down reach art. 125?
- F-g2b-01 (refuses): can a legal person be the victim of calúnia, difamação or injúria?
- F-sweep-b-06 (refuses where the readings differ): are art. 151 caput and § 1º I and IV displaced by the postal and telecommunications laws?
- F-g4a-24 (refuses where the readings part): does "o réu condenado" in art. 234-B § 3º mean any convict of Título VI, or only a convict of the eight crimes § 1º lists?
- F-g5-32 (refuses): does the forger who uses the paper they forged answer for the use of art. 304 as well?
- F-g3b-10 (encoded as printed): is art. 201 (paralisação de trabalho de interesse coletivo) still operative beside the right to strike?
- F-g6b-04 (refuses and names the conflict): when 2% of a contract exceeds art. 49's largest fine (above about R$ 135 million), does art. 337-P's floor or art. 49's ceiling give way?

### 6.2 The forks with the widest effect

By the number of provisions the register's `site.provisions` lists, among forks whose `divergence` is `observable`:

- F-g1c-19 (12 provisions): the date that decides which wording governs an earlier fact is the date of the crime; with F-g1c-26 it is the fork behind the strict gate of section 7, limit 1.
- F-g3-03 (9): the day each amending law came into force, computed from its own vigência clause.
- F-g0-08 (7): "idoso" is sixty or more, not more than sixty (arts. 147-A, 149-A, 155 § 4º-C, 171 § 4º, 203, 207, 234-A).
- F-g0-06 (7): "maior de N anos" starts on the Nth birthday, the age convention behind every "maior de".
- F-g4b-01 (7): the danger in arts. 250 ff. must be a common danger, not a danger to one person.
- F-sweep-c-05 (7): how arts. 359-L, 359-M, 359-M-A and 359-M-B combine (section 7, limit 9).

## 7. Known limits

These are the limits a reviewer should read first.
Each gives where the evidence is.

1. **The vintage pass was not done.**
   The strict vigência rule means a provision that a later law re-wrote refuses for every earlier fact, because the earlier wording is not in the source.
   Every prescription period passes through art. 115 (Lei 15.160/2025, in force 4 July 2025), so **no prescription is computable for a fact dated before 4 July 2025**, and art. 111, V likewise refuses before 9 July 2022.
   In `cp-g1c-prescricao-testes.l4`, 49 of 129 assertions are `#ASSERT REFUSED` and 43 of those give art. 115's earlier wording as the reason (by `grep`); `notes/g1c.md` § 10 measured 36 of 119 on 2026-09-30, before post-amendment twins were added.
   The rule-version arms for court rulings refuse the same way: art. 51 before ADI 3.150 and ADI 7.032, and art. 59 for a sentence before ADPF 1.107 (6 May 2024).
   So do art. 92, II before 10 October 2024, art. 92 § 2º from 10 October 2024 to 6 August 2026, and every penalty rule for an article re-written in 2025 or 2026 (art. 155 before 4 May 2026, for example).
   Evidence: `PLAN.md` § 10; `notes/g1c.md` §§ 8 and 10; `notes/g1b.md` (table of sweep entries); `notes/independent-g1.md` (the seven R rows); fork F-g1c-19.
2. **Art. 30 with art. 312.**
   A non-official participant in peculato cannot be charged with it: art. 30's rule takes "elementar do crime" as an input and no rule composes it with art. 312.
   Evidence: `notes/independent-g6.md` § 5, item 4 (IT-g6-023); `notes/g1a.md` § 1.
3. **Art. 234 parágrafo único never reads the judge's finding that the object is obscene.**
   The caput limb requires the finding and the paragraph's limb does not, though the field's gloss says it covers it.
   Evidence: `cp-g4a-lenocinio.l4`, `crime de escrito ou objeto obsceno (art. 234)` (line 800); `notes/g4a.md` § 8, last bullet.
4. **The vocabulary for intent is split.**
   `Elemento subjetivo` in `cp-dominio.l4` (line 337) is `dolo` or `culpa`; group g1a classifies the same thing with a third value, `nem dolo nem culpa`, over its own `Relação do agente com o resultado` (`cp-g1a-crime.l4` lines 414 and 448).
   Knowledge of the quality of a thing is a local finding in each group (section 4, item 8).
   Nothing connects them, and unifying them is a later ruling (`notes/integration.md`, Step 1).
5. **The stage of execution is represented four ways.**
   They are `Execução do crime` (`cp-dominio.l4` line 355), `Curso da execução` (`cp-g1a-crime.l4` line 198), `Etapa da execução` (`cp-g3b-comum.l4` line 29) and `Estágio da execução` (`cp-g5-comum.l4` line 40), and `cp-g6a-casos.l4` declares a second type named `Estágio da execução` for its fixtures.
   The enums differ for an effective repentance (arrependimento eficaz), so unifying them changes answers (`notes/integration.md`, Step 1).
6. **61 names are defined more than once**, mostly constructors for the verbs of different articles.
   They are not errors, because L4 resolves a name by its type, but an expression with no type to go on gets "multiple definitions" (`notes/integration.md`, Step 3).
7. **A dead constant.**
   `a vigência da Lei nº 15.181, de 2025` (`cp-g3-comum.l4` line 45) is read nowhere (`notes/g3.md` § 12).
8. **One research entry is filed as `no-effect` though it has an effect.**
   `M-sweep-a-43` says the Código de Trânsito's own licence suspension displaces art. 57 for the crimes of that code, which this encoding does not cover.
   Its disposition is `no-effect` because the register's schema requires an `interpretive` entry disposed `encoded` or `deferred` to name a fork, and this entry routes to none (`routing.fork_ids` is empty; schema rule at `external-modifications.schema.json` line 235).
   Art. 57 is encoded as printed, with a comment in `cp-g1b-cominacao.l4` at art. 57.
9. **Lei 15.402/2026 (arts. 359-M-A and 359-M-B) is a currency risk.**
   The law has been in force since 8 May 2026.
   On 9 May 2026 Min. Alexandre de Moraes suspended its application, not erga omnes, in the STF's own execution proceedings about 8 January 2023, and the encoding refuses in that class.
   Four ADIs (7966 to 7969) are pending; ADI 7985 was denied seguimento on 17 July 2026 and is on agravo regimental.
   Evidence: `registers/external-modifications.json` M-sweep-c-09 and search S-sweep-c-22 (status as of 30 September 2026); fork F-sweep-c-05.
10. **STF decisions that could not be fetched.**
    The STF's portal answered HTTP 403 to every method the research tried.
    The coverage notes list what the researchers knew of and did not retrieve: RE 597.270 (known only through an acórdão of the Tribunal de Justiça do Distrito Federal citing it), RE 453.000, Súmula Vinculante 56, and Súmulas 608, 611 and 723; Súmula 608 is cited by number only (fork F-g1c-23).
    ADPF 54 is quoted from that court's reproduction, ADPF 442 and ADPF 1207 rest on press reports of October 2025, and the texts of the despachos in ADIs 7968 and 7969 and of the decision in ADI 7985 were not obtained.
    Evidence: searches S-sweep-a-06, S-sweep-a-08, S-sweep-b-05, S-sweep-c-22.
11. **Laws after the research.**
    For arts. 213 to 361 the research found no law amending the Code after Lei 15.517/2026, but it probed by sequential numbering: a law numbered beyond Lei 15.545 or Lei Complementar 242, or not yet posted by 29 September 2026, is not covered.
    Pending vetoes VET 20/2026 (art. 157 § 3º I) and VET 52/2026 (art. 157 § 2º-A III, e) are not law (M-sweep-b-05, M-sweep-b-06; search S-sweep-c-05).
12. **The independent pass is only partly independent.**
    During the fix round the encoders were told of some cases, and agreement on those proves nothing; each `notes/independent-gN.md` marks them (17 exposed cases in g1, of which 15 agree; 15 in g2, of which 13 agree).
    Many other agreements are decided by an input: in g2, 91 of 369 agreements turn on a finding supplied as input ("mal injusto e grave"), which shows that the encoding routes the finding and not that it reads the threshold.
    Fixtures were changed during the fix round, though no expected value was (`notes/independent-g1.md` § 6, `notes/independent-g2.md`).
13. **Mutation coverage is uneven** (section 4, item 9), and no lawyer has read the encoding (section 0).

## 8. Questions for a Brazilian criminal lawyer

Each group's note has its full list under "Open questions for a Brazilian criminal lawyer"; the questions below are the ones that decide an answer.
Each names the module and the rule where the encoding takes a position, and the fork.

1. Art. 273 § 1º-B, V (`cp-g4b-saude-publica-alimentos-e-medicamentos.l4`, `a hipótese do art. 273, § 1º-B, V`): the STJ Corte Especial (AI no HC 239.363/PR, 26.2.2015) declared the penalty unconstitutional and named no substitute, so the encoding refuses it where inciso V is the only hypothesis; is that right? (F-sweep-c-16)
2. Art. 29 with art. 351 (`cp-g6b-justica-exercicio-arbitrario-a-desobediencia.l4`, `de pessoa legalmente presa … que não o agente (art. 351)`): a prisoner who instigates a third party to free the prisoner: does the prisoner take part in the third party's crime of art. 351, or is the prisoner's own escape, being atypical without violence, outside it? (F-g6b-23)
3. Art. 155 § 1º (`cp-g3-furto.l4`, `incide o aumento do art. 155, § 1º`): does STJ Tema 1087 still hold now that Lei 15.397/2026 made the increase "de metade"? (F-sweep-b-19)
4. Art. 155 § 2º (`cp-g3-furto.l4`, `as opções do juiz pelo art. 155, § 2º`): once the accused is primário and the thing is of small value, must the judge grant one of the three options, and may two be combined? (F-g0-27)
5. Arts. 213 § 1º and 217-A (`cp-pena.l4`, `maior de`): is a victim on the fourteenth birthday "maior de 14", "menor de 14", or neither? (F-g0-06)
6. Arts. 21, 24 § 2º, 26 p.ú., 28 § 2º, 29 § 1º (`cp-g1a-imputabilidade.l4`, `as causas de diminuição cabíveis (arts. 26 e 28)`): once the requirements are met, must the judge reduce the penalty? (F-g1a-13)
7. Art. 20 § 1º (`cp-g1a-erro.l4`, `o efeito do erro (art. 20)`): where a putative justification comes from an avoidable error and the crime has no culposo form, is the agent unpunished, or punished for the doloso crime with art. 21's reduction? (F-g1a-14)
8. Arts. 23 II and 25, ADPF 779 (`cp-g1a-ilicitude.l4`, `a situação de legítima defesa (art. 25)`): does the read-down bind from the merits judgment of 1.8.2023 or from the earlier interim order? (F-g1a-06)
9. Art. 83 (`cp-g1c-livramento-condicional.l4`, `a fração exigida para a pena (art. 83)`): which fraction for a convict who is not a repeat offender but has no good record? (F-g1c-09)
10. Art. 101 (`cp-g1c-acao-penal.l4`, `a ação penal do crime complexo (art. 101)`): what does Súmula 608 STF say, and what does it still reach after art. 225's rewrite, given that its text could not be fetched? (F-g1c-23)
11. Art. 117, VI (`cp-g1c-prescricao.l4`, `a prescrição da pretensão executória`): does the reincidência interrupt on the day of the new crime or when its conviction becomes final? (F-g1c-30)
12. Art. 115 (`cp-g1c-prescricao.l4`, `os prazos de prescrição são reduzidos de metade (art. 115)`): which decision is "a sentença" when the conviction first comes on appeal? (F-g1c-26)
13. Art. 67 (`cp-g1b-circunstancias.l4`, `a agravante é preponderante (art. 67)`): which circumstances "resultam dos motivos determinantes do crime, da personalidade do agente e da reincidência", and does anything direct the judge when both sides have one? (F-g1b-18)
14. Art. 122 § 7º with art. 121 § 2º, IX (`cp-g2a-suicidio.l4`, `o crime pelo qual responde o agente (art. 122)`; `cp-g2a-homicidio.l4`, `incide o aumento do art. 121, § 4º, segunda parte`): when the victim was under fourteen, does § 2º IX also qualify the homicide? (F-g2a-19, F-g2a-03)
15. Art. 129 §§ 9º and 13 (`cp-g2a-lesao-corporal.l4`, `lesão corporal do art. 129, § 9º`): is the resulting inversion (slight domestic injury with a two-year minimum, serious injury with sixteen months) the law? (F-g2a-09)
16. Art. 145 with art. 140 § 2º (`cp-g2b-honra.l4`, `a ação penal do art. 145`): for injúria real whose violence caused a slight injury, is the action public and unconditional (art. 100) or conditional on representação by analogy with Lei 9.099/1995 art. 88? (F-g2b-06)
17. Art. 141 § 2º (`cp-g2b-honra.l4`, `a vigência do art. 141, § 2º`): from which day does it apply: 30.5.2021, 30.4.2021 or 23.1.2020? (F-g2b-04)
18. Art. 147-A § 1º, II (`cp-g2b-constrangimento-ameaca.l4`, `contra mulher por razões da condição de sexo feminino (art. 147-A, § 1º, II)`): does it still apply after Lei 14.994/2024 revoked the paragraph it cites? (F-sweep-b-24)
19. Art. 157 (`cp-g3-roubo.l4`, `a forma do roubo que governa`): with a restricted firearm and a serious injury, does § 2º-B (12 to 20 years) or § 3º I (7 to 18) govern? (F-g3-09)
20. Art. 158 § 4º (`cp-g3-extorsao.l4`, `incide o aumento do art. 158, § 4º`): the encoding follows the enacted words (any organização criminosa); will courts narrow it to the ultraviolent organisation, as the neighbouring provisions say? (F-sweep-b-22)
21. Art. 182, I (`cp-g3-disposicoes-gerais.l4`, `em prejuízo do cônjuge desquitado ou judicialmente separado (art. 182, I)`): after STF Tema 1053, would a court extend the immunity to a divorced ex-spouse, which the encoding denies? (F-sweep-b-23)
22. Art. 201 (`cp-g3b-organizacao-do-trabalho.l4`, `paralisação de trabalho de interesse coletivo do art. 201`): was it received by CF art. 9º, or is it displaced by Lei 7.783/1989? (F-g3b-10)
23. Art. 184 § 4º (`cp-g3b-propriedade-imaterial.l4`, `o disposto nos §§ 1º, 2º e 3º não se aplica (art. 184, § 4º)`): is a single private copy of a whole work, without profit, still the caput's crime? (F-g3b-03)
24. Art. 226 (`cp-g4a-dignidade-sexual-geral.l4`, `o art. 226 alcança o crime`): does inciso IV reach every crime of Caps. I and II, or only estupro, as its rubrics say? (F-g4a-03)
25. Art. 234-B § 3º (`cp-g4a-dignidade-sexual-geral.l4`, `o réu condenado passa a ser monitorado, na leitura`): is "o réu condenado" any convict of Título VI, or only a convict of the eight crimes § 1º lists? (F-g4a-24)
26. Art. 273 § 1º-B, I (`cp-g4b-saude-publica-alimentos-e-medicamentos.l4`, `a hipótese do art. 273, § 1º-B, I (Tema 1003 STF)`): does Tema 1003's restored penalty reach every verb of § 1º applied to an unregistered product, as the encoding says on a search summary and not the court's text? (F-g4b-12)
27. Art. 259 (`cp-g4b-perigo-comum.l4`, `a forma dolosa do art. 259 foi revogada pela Lei nº 9.605, de 1998, não codificada`): is the intentional form revoked by Lei 9.605/1998 art. 61? (F-sweep-c-17)
28. Art. 289 § 4º (`cp-g5-moeda-falsa.l4`, `pena do art. 289, § 4º`): does "nas mesmas penas" mean § 3º's (3 to 15 years) or the caput's (3 to 12)? (F-g5-02)
29. Art. 304 (`cp-g5-falsidade-documental.l4`, `o uso é absorvido pela falsificação (post factum impunível)`): does the forger who uses the paper they forged answer for one crime or two? (F-g5-32)
30. Arts. 359-M-A and 359-M-B (`cp-g5-estado-democratico.l4`, `a regra de aplicação da pena do Capítulo II (art. 359-M-A)`): is dating them by the day the penalty is applied (lex mitior) right, and what governs meanwhile in the suspended STF executions? (F-sweep-c-05)
31. Art. 359-T (`cp-g5-estado-democratico.l4`, `excluído pelo art. 359-T`): may the finding ever clear a crime whose element is violence or grave threat? (F-g5-29)
32. Art. 327 § 1º (`cp-g6a-funcionario-publico.l4`, `o art. 327, § 1º, na redação da Lei nº 9.983, de 2000, rege o fato`): before Lei 9.983/2000, was an employee of an entidade paraestatal a funcionário público for the penal law, and was the law in force on 15.10.2000? (F-g6a-23, F-g6a-22)
33. Art. 337-E (`cp-g6b-licitacoes.l4`, `os elementos do art. 337-E estão reunidos`): do the courts still require a specific intent to harm the treasury and an actual loss, as under Lei 8.666/1993 art. 89, which the text does not state? (F-g6b-02)
34. Arts. 359-C and 359-G (`cp-g6b-financas-publicas.l4`): which period is "os dois últimos quadrimestres", and is the term's last day inside "os cento e oitenta dias anteriores"? (F-g6b-18, F-g6b-20)

## 9. How to run

Prerequisite: a built `l4` from l4-ide `unstable`. The tree was run with two builds: `l4-1008` (9 October 2026) and one from `73a953821` (29 September 2026).
Leave `JL4_LIBRARY_PATH` unset, so that the binary uses its own embedded standard library.
Do not point an `l4` at a standard library newer than itself: it fails as a cascade of "could not find a definition", not as a version error.
No released `l4` from `legalese/prereleases` was tried.

```
cd subjects/br/codigo-penal-1940/encodings/legalese-2026-09
L4=/path/to/l4 nice -n 15 ./check.sh . cp-g1b-     # one group's modules and tests
L4=/path/to/l4 nice -n 15 ./check.sh . cp-g        # the 166 group files; exits 0
L4=/path/to/l4 nice -n 15 ./check.sh . cp-ind-     # the independent tests; exits 1 by design
L4=/path/to/l4 nice -n 15 ./check.sh               # the whole tree, 241 modules; exits 1 by design
/path/to/l4 run cp-g1b-multa-testes.l4             # one module
/path/to/l4 nlg --lang en cp-g1b-multa-testes.l4   # the English glosses
/path/to/l4 check cp-codigo-penal.l4               # the composer
```

`check.sh` runs `l4 run` on each module and prints errors, satisfied, failed and refused assertions against the number of `#ASSERT` lines.
It reads the diagnostics and not the exit code, because `l4 run` exits 0 when an assertion fails.
It counts a refused assertion in its own column and treats it as not passing, and prints UNACCOUNTED if a module produced fewer verdicts than it has assertions.
It exits 0 only when every module has no errors, no failures, no refusals and nothing unaccounted.
The `cp-ind-*` files are red where the encoding disagrees with the independent author: 55 assertions by the table in section 5.2.

Run one `l4` process at a time.
The composer imports every module, so it is the largest single check.
With the 29 September binary it took about 12.5 CPU minutes (`notes/integration.md`); with `l4-1008`, `l4 run` of the composer took 10 seconds.
On 2026-10-11 the whole tree, 241 modules run one after another with `l4-1008` at `nice -n 15`, took about 4.5 minutes (266 s) on an Apple M4 machine under a load average of 2.5 to 5.7.
Every module but the composer took 0 to 2 s.

## 10. The pipeline run

The private `l4-ide` pipeline (`go.sh`) was run over this encoding on 11 October 2026 (run `2026-10-10-c475842a-001`, `l4-1008`, the 169 component modules, HG1 waived on the record).
It ended COMPLETE: the journal chain verifies and all 526 recorded artifacts still hash as recorded.
A COMPLETE verdict is completeness of accounting, not a statement that the encoding is right.

| stage | verdict | what it says |
| --- | --- | --- |
| `p1-ingest` | PASS | the source bundle validates |
| `p2-sweep` | PASS | the register of later norms validates, with its joins to the source bundle |
| `p3-encode` | PASS | `l4 check` accepts all 169 modules |
| `p3-check` | PASS | no `ELSE IF` site (24 were converted to `BRANCH` after the first run), no AND/OR column warning; the temporal-closure check is NOT CHECKED because the census of dated arms is 0 (section 2.3) |
| `p4-forks` | PASS | 423 forks, internally coherent; fork-register completeness is carried by HG1 |
| `p5-gate` | PASS | the cross-file joins over the three registers hold |
| `p6-tests` | PASS | 5,769 assertions satisfied |
| `p7-dmn` | DEGRADED | the emit-only arm reaches only `cp-dominio.l4`, which has no decision to export |
| `p8-verify` | DEGRADED | 166 findings over 1,565 analysed decisions (below) |
| `p8-diff` | SKIPPED | no comparison against another encoding was declared |

The first run, on the content before the conversion to `BRANCH`, reported the 24 `ELSE IF` sites as a `p3-check` finding; they are fixed.
The 166 `p8-verify` findings are 158 `vacuous-guard` (a condition already implied by the ones it is conjoined with), 4 `unsat` and 4 `dead-branch`.
The `unsat` ones are four rules written deliberately as the constant `FALSE` so that a list the Code closes stays visibly closed (arts. 21, 28 I, 28 II and 88); the `dead-branch` ones are those constants as limbs of the rule for arts. 26 to 28.
123 of the `vacuous-guard` findings are in one rule, `a bordo, aplica-se a lei brasileira (art. 5º)`, whose arms test enumerated values of the same two fields; the verifier reads each equality as an unrelated atom.
The other 35 are in 11 modules and have not been read.
`l4 verify` is propositional: a finding is a property of the Boolean skeleton, and silence is not a proof of consistency.

No projection leg is declared.
`l4 export dmn` on `cp-g3-furto.l4` reports 38 blocking and 58 lossy gaps (the `REFUSE` convention and the partial functions have no DMN form), and `l4 export catala` refuses because `a pena cominada com as causas` (`cp-pena.l4`, line 740) is recursive.
