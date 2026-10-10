# Independent test pass — ta-g4: Títulos VI–IX (arts. 213–288-A)

Test author ta-g4, 2026-09-30 (phase 2).
The cases were written on 2026-09-29 from the source text alone, before the encoding existed for the author to read: `~/.claude/br-penal-oracle/cases/ta-g4.json`, last written 2026-09-29 19:09:01 SGT, sha256 `5af0398aed751ed07438aaf98515834410affb2e7aafc4228ca3828730e902a5`, taken during phase 2 and re-checked unchanged at its end.
No expected value was changed to match the encoding.
Every case is now EXPOSED (`~/.claude/br-penal-oracle/EXPOSURE.md`, section "ta-g4").

## Files

| file | cases | directives |
| --- | --- | --- |
| `cp-ind-g4-liberdade-sexual-e-vulneravel.l4` | IT-g4-001–093 | 93 |
| `cp-ind-g4-disposicoes-gerais-e-lenocinio.l4` | IT-g4-094–173 | 80 |
| `cp-ind-g4-familia.l4` | IT-g4-174–243 | 68 (2 not expressible) |
| `cp-ind-g4-perigo-comum-e-transportes.l4` | IT-g4-244–322 | 78 (1 not expressible) |
| `cp-ind-g4-saude-publica.l4` | IT-g4-323–384 | 62 |
| `cp-ind-g4-paz-publica.l4` | IT-g4-385–408 | 24 |

Each case is one directive, under its comment line `-- IT-g4-NNN: <question>`, with the question copied verbatim from the JSON.
A script checked all 408 ids: each labelled exactly once, a directive under every label except the three not expressible, every refuse case as `#ASSERT REFUSED` and no other case so, and the question verbatim. There are 405 `#ASSERT` lines.
Undated facts are dated 29 September 2026, the day the source was fetched, which is after every vigência these modules check.
The exception is IT-g4-042 (art. 234-B § 1º), with the fact on 10.1.2025 and the first-instance conviction on 1.6.2026.

## Counts

| | n |
| --- | --- |
| cases | 408 |
| directives | 405 |
| satisfied | 396 |
| failed | 8 |
| refused where a value was expected | 1 |
| not expressible | 3 |

| class | n | ids |
| --- | --- | --- |
| (E) the encoding departs from the text | 1 | 173 |
| (F) a genuine ambiguity, recorded as a fork | 5 | 060 (F-g4a-09), 097 (F-g4a-03), 107 (F-g4a-03), 162 (F-g0-08), 407 (F-g4b-22) |
| (S) stale: a later sweep finding | 3 | 216 (M-sweep-c-27), 283 (M-sweep-c-31, F-sweep-c-17), 351 (M-sweep-c-03, F-g4b-12) |
| (T) the case misread the text | 0 | |
| (R) a conductor's strict ruling | 0 | |

Seven of the nine disagreements are on cases marked arguable in phase 1 (097, 107, 162, 173, 216, 351, 407).
In six of them the encoding took a reading the case's own `alternative` named; in the seventh, 407, it took "no minimum", close to the case's reading B ("two suffice").
The two on cases marked certain are 060 (F) and 283 (S).

## check.sh, verbatim

```
module                                        errors satisfied  failed refused asserts
cp-ind-g4-disposicoes-gerais-e-lenocinio.l4        4        76       4       0      80
cp-ind-g4-familia.l4                               1        67       1       0      68
cp-ind-g4-liberdade-sexual-e-vulneravel.l4         1        92       1       0      93
cp-ind-g4-paz-publica.l4                           1        23       1       0      24
cp-ind-g4-perigo-comum-e-transportes.l4            0        77       0       1      78
cp-ind-g4-saude-publica.l4                         1        61       1       0      62
TOTAL (6 modules)                                  8       396       8       1     405
(a failed assertion also counts as an error; errors minus failed = everything else)
```

`check.sh` exits 1, as it must with failures present.

Every failed or refused assertion is one of the nine in the table below; each module's error count is its failed count, so no module has an error other than a failed assertion.

## Disagreements

| id | articles | expected (ta-g4) | the encoding's answer | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g4-060 | art. 218 | TRUE: inducing a 12-year-old to satisfy an adult man sexually is art. 218 (certain) | FALSE: an induced act with contact goes to art. 217-A, the inducer taking part in it | F | F-g4a-09, taken `contatoEhEstuproDeVulneravel` (the other reading, `sempreArt218`, is the case's); the contact flag is read at `cp-g4a-vulneravel.l4:285` ("REACH (fork F-g4a-09)"). The case read art. 218's words alone and did not weigh it against art. 217-A. |
| IT-g4-097 | art. 226, I and IV, a (art. 215 by two agents) | REFUSE: the text gives 1/4 (I) and 1/3–2/3 (IV, a) and does not choose (arguable) | one cause, 1/4 fixed (art. 226, I) | F | F-g4a-03, taken `capitulosAnterioresIVParaEstupro`: inciso IV reaches only estupro (`cp-g4a-dignidade-sexual-geral.l4:385`), so art. 215 gets inciso I (`:415`). The case's alternative named this reading. |
| IT-g4-107 | art. 226, I (art. 228 by two persons) | REFUSE: the text does not say whether art. 226 reaches Capítulo V (arguable) | FALSE | F | F-g4a-03: `o art. 226 alcança o crime` (`:373`) admits only Capítulos I, I-A and II; `tituloInteiro` is the recorded other reading. |
| IT-g4-162 | art. 234-A, IV (victim 60 years and 2 months) | REFUSE: the Code does not define "idosa" (arguable) | TRUE | F | F-g0-08, taken `sessentaOuMais`: `idoso` is 60 or more (`cp-pena.l4:910`), the Estatuto reading the case named as its alternative. |
| IT-g4-173 | art. 234-B, § 3º (conviction under art. 233) | REFUSE: "o réu condenado" may be any convict of the Título, or only of the crimes § 1º lists (arguable) | TRUE | E | `o réu condenado passa a ser monitorado por dispositivo eletrônico (art. 234-B, § 3º)` (`cp-g4a-dignidade-sexual-geral.l4:644`) never reads the crime. F-g4a-08 is about § 3º's reach in time only; no fork addresses its reach by crime, and sweep-c has no entry on art. 234-B. (Superseded: fork F-g4a-24 on 2026-10-08, then a refusal on 2026-10-11; see "Second look" below.) |
| IT-g4-216 | art. 244 (the multa) | "de uma a dez vezes o maior salário mínimo vigente no País" (arguable; the alternative named Lei nº 7.209/1984, art. 2º) | the multa is art. 49's day-fine: 360 dias-multa at five minimum wages each (1,800 minimum wages) fits art. 244's pena | S | M-sweep-c-27 (binding, "substituted"); `cp-g4a-assistencia-familiar.l4:171-181` keeps the printed words as an inert string; PLAN § 2.2. |
| IT-g4-283 | art. 259, intentional form | reclusão, 2 to 5 years, and multa (certain) | REFUSE: "a forma dolosa do art. 259 foi revogada … pela Lei nº 9.605/1998" | S | M-sweep-c-31 (interpretive) opened F-sweep-c-17, taken `revogadoSalvoCulposa` (`cp-g4b-perigo-comum.l4:1245-1247`). The constant `pena do art. 259, caput` still equals the preceito's words. |
| IT-g4-351 | art. 273, § 1º-B, I | reclusão, 10 to 15 years, and multa: the text (arguable; Tema 1003 named) | reclusão, 1 to 3 years, and multa | S | M-sweep-c-03 (binding): STF Tema 1003 restores the original penalty for § 1º-B, I; F-g4b-12 (settled by the STF) and F-g4b-13. |
| IT-g4-407 | art. 288-A (a two-man "esquadrão") | REFUSE: the article sets no minimum number of members (arguable) | a value: every conjunct of the rule holds on the facts, so TRUE | F | F-g4b-22, taken `semNumeroMinimo`; `tresOuMaisPorAnalogia` and `quatroOuMaisComoOrganizacao` recorded. The value is inferred from the rule, not shown by an `#EVAL`: at the load of the time a re-run for a probe took about 1.5 hours. |

## (E) findings

There is **one**.

**Art. 234-B § 3º monitors anyone convicted of any Título VI crime, by a reading no fork records (IT-g4-173).**
The paragraph says only "O réu condenado passará a ser monitorado por dispositivo eletrônico".
It sits under a caput about every process for a crime "definido neste Título", and immediately after § 1º, which lists eight articles (213, 216-B, 217-A, 218-B, 227, 228, 229 and 230).
Whether "o réu condenado" is any convict of the Título or only the § 1º convict is not answered by the text; the brief's rule for that is REFUSE, or a fork.
The encoding takes the widest reading and records no fork.
The rule does not read the crime at all, so it also monitors a conviction for ato obsceno (art. 233, tested) and, by reading the rule rather than by an assertion, for escrito obsceno (art. 234) and for promoção de migração ilegal (art. 232-A), which is in `Crime contra a dignidade sexual` and, by F-g4a-05's literal reading of "neste Título", within the Título's general provisions.
Monitoring is a restriction on the convicted person, and on the narrow reading it would not apply to any of these.
The repair is a fork with both readings, and a refusal (or the narrower reading) outside § 1º's list until someone rules.

Nothing else in the 405 directives is an (E).
The other eight disagreements are recorded forks (5) or sweep findings the encoders implemented as the brief requires (3).

## Agreement worth recording

These are the points ta-g4's phase-1 reply named as most likely to be encoded wrong.
That list was in the conductor's conversation, not in the file the encoders read (EXPOSURE.md), so agreement on it is evidence except where marked.

- **Art. 213 § 1º's "menor de 18 ou maior de 14"** is read as a band (F-g4a-15, `conjuntivo`): IT-g4-012, a victim of 30, stays in the caput. Not exposed; this agreement counts. IT-g4-011 (14 years and 6 months is "maior de 14") agrees too, but rests on the exposed "maior de N" convention.
- **The 2025–2026 penalties**: art. 217-A caput 10–18 with multa (IT-g4-050), §§ 3º and 4º, arts. 218, 218-A, 218-B, 218-C, and art. 266 reclusão 2–4 with multa (IT-g4-317).
- **Art. 258's asymmetry**: an intentional fire with a light injury gets no increase (IT-g4-279), a culpable one gets half (9 months to 3 years, IT-g4-280). Whether the doubling also reaches the fine (IT-g4-278) is not expressible; see below.
- **The relationship lists differ by article**: padrasto is not in art. 227 § 1º (IT-g4-113); tio and descendente are not in art. 228 § 1º (IT-g4-124, 125); art. 228 § 1º carries no multa without lucro (IT-g4-122).
- **Art. 266 § 1º does not reach "perturbar" a telemático service** (IT-g4-319), and **art. 285 keeps art. 258 off art. 267** (IT-g4-328).
- Arguable cases where the encoding independently took the case's reading: a "gravíssima" result qualifies as "lesão corporal de natureza grave" (IT-g4-008, F-g4a-12); the art. 218-C § 2º "ressalvada sua prévia autorização" dispenses with anonymity (IT-g4-091, 092, F-g4a-14); the death of a patient under art. 282 does not also double the penalty through arts. 285 and 258 (IT-g4-376, F-g4b-09).

## Expressed, but weaker than they look

- **The deciding fact is an input**, so agreement tests the fact modelling more than the rule: IT-g4-032 (a teacher's ascendancy over a student), 089–092 (journalistic, anonymised, authorised), 131 (voluntary adult prostitution is not "exploração sexual", F-g4a-13), 200 (registration after a judicial adoption: no art. 242 conduct recorded), 239 (a custodial mother "subtracts" no one), 250 (a private car is not in art. 250 § 1º II), 293–294 (cable car and bus as "estrada de ferro"), 314 (a gym's generator is not a public-utility service), 321–322 (telecom equipment), 324 (one infection is no epidemic), 338 (irrigation water is not potable), 373 (a psychologist has no member in the professions list), 381 ("only once" is not habitual), 405 (the militia's finality is `com a finalidade de praticar qualquer dos crimes previstos neste Código` IS FALSE, `cp-g4b-paz-publica.l4:570`).
- **Through another route**: IT-g4-108 passes because art. 226 does not reach Capítulo V (F-g4a-03), not for the double-counting reason the case gave; IT-g4-148 passes on F-g4a-05's literal reading.
- **Substitutions** where no rule answers the question as worded: "which penalty applies" in IT-g4-015 and 057 is asserted as art. 213 not applying, art. 217-A applying, and art. 217-A's penalty; IT-g4-062 likewise for arts. 218 and 227. IT-g4-048 is asserted as the victim staying vulnerable with her consent and § 4º-A governing, since the record has no field for maturity or family approval. IT-g4-216 is asserted as a probe (a 1,800-minimum-wage fine does not fit), since the encoding has no rule that states the fine's limits in money. The ação penal cases compose g1c's art. 100 rule with g4a's art. 225 rule (018, 036, 041, 059, 094, 095) or use art. 100 alone (408). Where no case-level pena rule exists, the penalty is asserted on the `pena do art. N` constant: IT-g4-185, 190, 195, 206, 227, 232 and 236 (arts. 236, 237, 239, 243, 246, 247 and 248), IT-g4-191, 196 and 237 (arts. 238, 241 and 249, each together with the crime predicate), and IT-g4-130, 151 and 154 (arts. 229, 233 and 234).
- **Exposed** (EXPOSURE.md, conventions row), so agreement is not evidence: "maior de N" on 011, 014, 075, 115 and 212; `from: null` on 034 and 399; "dobro as +1/1" on 277, 282, 295, 320, 321, 325 and 384.

## Not expressible (3)

| id | articles | reason |
| --- | --- | --- |
| IT-g4-203 | art. 242, p.ú. | Expected REFUSE ("will the judge refrain?"). The encoding returns the judge's options (PLAN § 2.4), `aplicar a pena` and `deixar de aplicar a pena`, and no rule refuses. Consistent with the case; IT-g4-202 asserts the option to refrain is there. |
| IT-g4-242 | art. 249, § 2º | The same, for art. 249 § 2º's options; IT-g4-241 asserts the option. |
| IT-g4-278 | art. 258 | "Is the multa also doubled?" (expected no). No rule says whether art. 258's doubling reaches the fine: a cause changes only the custodial range and `multa` is a conjunction (PLAN § 2.2.1). g4b wrote "alcança também a multa" rules for arts. 250 § 1º, 251 § 2º and 266 § 2º, and F-g4b-03's foreclosure of `somentePrivativa` points at art. 258's "a pena privativa de liberdade", so the encoding is consistent with the case but never states it. |

## How it was done

ta-g4 wrote `cp-ind-g4-familia.l4` and four subagents wrote one file or pair each (arts. 213–218-C; 225–234-B; 250–266; 267–288-A), each reading its modules and fork entries first and classifying its own disagreements.
ta-g4 then re-read the rule and the fork or sweep entry behind every disagreement, confirmed that each cited fork and sweep id exists with the reading reported, and searched the fork register and sweep-c for anything on art. 234-B § 3º's reach by crime (nothing; F-g4a-05 and F-g4a-08 are the only forks naming art. 234-B).
Positive controls: in `cp-ind-g4-familia.l4` and `cp-ind-g4-perigo-comum-e-transportes.l4`, a temporary copy with four expectations flipped failed exactly those four and nothing else, and was deleted; each of the other four files has at least one genuine failure, so its assertions demonstrably can fail.
`check.sh` was run over all six files, one module at a time, for the output above (started 17:52 SGT on 2026-09-30).
While it ran, one comment was edited (IT-g4-278's label, so that each id labels exactly once); no directive changed, so the verdicts stand.

## Re-run after fix round (2026-10-09)

Before the re-run, four of the six modules did not typecheck, because their fixture builders lacked the new knowledge fields; they produced no verdicts at all (UNACCOUNTED = all their assertions).
No expected value was changed. Only builders gained fields.

| module | before (errors / satisfied / failed / refused / asserts) | after |
| --- | --- | --- |
| disposicoes-gerais-e-lenocinio | 1 / 0 / 0 / 0 / 80 (does not typecheck) | 4 / 76 / 4 / 0 / 80 |
| familia | 1 / 67 / 1 / 0 / 68 | unchanged |
| liberdade-sexual-e-vulneravel | 3 / 0 / 0 / 0 / 93 (does not typecheck) | 1 / 92 / 1 / 0 / 93 |
| paz-publica | 1 / 23 / 1 / 0 / 24 | unchanged |
| perigo-comum-e-transportes | 3 / 0 / 0 / 0 / 78 (does not typecheck) | 0 / 77 / 0 / 1 / 78 |
| saude-publica | 6 / 0 / 0 / 0 / 62 (does not typecheck) | 1 / 61 / 1 / 0 / 62 |

Agreeing: 90 of 405 before (only the two modules that compiled), 396 of 405 after. UNACCOUNTED is 0 everywhere.

**Fixtures changed (13 builder sites, 4 files, one kind: a new required knowledge field).**
- `o agente conhecia o conteúdo do escrito, desenho, pintura, estampa ou objeto` IS TRUE on the art. 234 builder (1 site; the case is silent, so knowing).
- `o agente sabia o que o registro continha` IS TRUE and `o agente sabia que a vítima não consentira` on the three art. 218-C builders (3 sites). The second is `NOT con` in the builder that takes the victim's consent as an argument, and TRUE in the two that fix it FALSE; the case is silent on knowledge, so the agent knows.
- `conhecimento da qualidade da coisa negociada` on the arts. 253 (`perigo-comum`, 3 sites: `sabia`, all dolosos) and 270, 272, 273, 274/275, 277, 278 (`saude-publica`, 6 sites). Where the builder takes the fact's `Dados comuns` as an argument (arts. 270, 272, 273), the field is derived from it: `sabia` when its `elemento subjetivo` is `dolo`, `ignorava a qualidade da coisa negociada, por culpa` otherwise, because a culposo case is one where the agent did not know; the other three sites fix `o caso doloso`, so `sabia`. All the culposo rows still agree.
- Case silent on knowledge everywhere: no case describes ignorance except through the culposo form, so "knowing" keeps the original facts.

**Positive control.** A scratch copy of the disposições module with the art. 234 `conhecia` field flipped to FALSE failed IT-g4-152 (a new red beside the four already red); the copy was deleted.

**Disagreements (9, all already triaged above; none new).** Each is still the same disagreement as in the triage table.

| id | expected | got | why |
| --- | --- | --- | --- |
| IT-g4-097 | REFUSE | a value | F-g4a-03, art. 215 gets inciso I only |
| IT-g4-107 | REFUSE | FALSE | F-g4a-03, art. 226 does not reach Capítulo V |
| IT-g4-162 | REFUSE | TRUE | F-g0-08, idoso is 60 or more |
| IT-g4-173 | REFUSE | FALSE | F-g4a-24 (2026-10-08): § 3º monitors only § 1º's eight crimes; art. 233 is not one. Told to g4a (EXPOSURE.md), so this is a fix that moved the answer from TRUE to FALSE, **not** a fix that agrees: the case still expects REFUSE. Superseded 2026-10-11: now REFUSED, see "Second look" below. |
| IT-g4-060 | art. 218 TRUE | FALSE | F-g4a-09, contact goes to art. 217-A |
| IT-g4-216 | the printed words (a fine fits or not) | substituted | M-sweep-c-27 |
| IT-g4-283 | reclusão 2 to 5 with multa | REFUSE | F-sweep-c-17, dolosa form revoked |
| IT-g4-351 | reclusão 10 to 15 | 1 to 3 | STF Tema 1003 |
| IT-g4-407 | REFUSE | a value (TRUE) | F-g4b-22 |

Of the IT-g4-173 row, the "got" was measured with an `#EVAL` of the same expression in the scratch copy: FALSE. The other "got" columns repeat the earlier triage and were not re-measured (the assertions fail the same way).

Anything odd: `check.sh` run without the module filter took more than the 120 s tool limit when the machine was loaded; run per module it takes seconds each.

## Second look, 2026-10-11

Only IT-g4-173.
It was told to g4a on 2026-10-08 and again now (EXPOSURE.md), so its agreement is the fix working, not independent evidence.
No expected value changed; `cases/ta-g4.json` was not edited, and no cp-ind-g4 file was touched.

| id | expected | the first fix (2026-10-08) | now | class | result |
| --- | --- | --- | --- | --- | --- |
| IT-g4-173 | REFUSE | FALSE: fork F-g4a-24 took the narrow reading (§ 1º's eight crimes) | REFUSED, by name, with both readings in the message | was E, then F | agrees; scored **fixed**, not an independent agreement |

**Why a refusal and not a recorded fork whose reading is taken.**
The text of § 3º names no crime, and nothing in the sources decides which convicts it reaches: the sweep did not search § 3º's reach (a grep of `sweep-c.external-modifications.json` on 2026-10-11 finds art. 234-B only in the vigência search for Lei nº 15.035/2024), and the Senado XML only records and dates that law's additions.
The narrow reading rested on the definite article, the common enactment of §§ 1º to 3º and the restrictive reading of a burden on liberty; those are arguments, and the fork itself recorded that a court could still take the wider reading.
The BRIEF's rule is "Where the source does not answer, REFUSE", and the conductor took that position on F-g5-29 on 2026-10-08 (name both readings, do not pick one).
The refusal is narrow: the rule answers where the readings agree (a crime § 1º lists: yes; before 28.11.2024, without a conviction, or acquitted on appeal: no) and refuses only for a Título VI crime outside § 1º's list when everything else holds.
Changed files: `cp-g4a-dignidade-sexual-geral.l4` (the exported rule), `cp-g4a-dignidade-sexual-geral-testes.l4`, `registers/parts/g4a.forks.json` (F-g4a-24 now `open`), `registers/parts/g4a.roadmap.json` (one note), `notes/g4a.md`.

**check.sh, before and after** (`L4=~/.claude/br-penal-toolchain/l4-1008`, one prefix at a time):

| module | before | after |
| --- | --- | --- |
| cp-ind-g4-disposicoes-gerais-e-lenocinio | 4 / 76 / 4 / 0 / 80 | 3 / 77 / 3 / 0 / 80 |
| cp-ind-g4-liberdade-sexual-e-vulneravel (imports the changed module) | 1 / 92 / 1 / 0 / 93 | 1 / 92 / 1 / 0 / 93 |
| cp-g4a-dignidade-sexual-geral-testes (the encoder's) | 0 / 69 / 0 / 0 / 69 | 0 / 73 / 0 / 0 / 73 |

The three failures left in the first row are IT-g4-097, 107 and 162 (read from the run's line numbers: 203, 268, 590), unchanged.
The other four cp-ind-g4 modules do not import the changed module and were not re-run.
Across the six cp-ind-g4 modules the totals are therefore 397 satisfied, 7 failed, 1 refused where a value was expected, of 405 (the 2026-10-09 re-run had 396 and 8).
