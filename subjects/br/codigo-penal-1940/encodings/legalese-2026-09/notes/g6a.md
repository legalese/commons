# g6a — arts. 312–337-D: notes for the reviewer

**Status (2026-09-30): all 34 units encoded; notes being finished.** Parte Especial, Título XI, Capítulos I, II and II-A.

## PROGRESS

Last updated 2026-09-30, after the usage-limit stop.

- [x] Read BRIEF, PLAN, the skills, `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`, arts. 312–337-D in the source, sweep-c (entries, searches, proposed forks) and M-sweep-b-11.
- [x] All 34 roadmap units ENCODED, in six modules plus `cp-g6a-comum.l4` (shared machinery and every vigência date) and `cp-g6a-casos.l4` (test fixtures). Roadmap part validates.
- [x] Vigência dates confirmed by sweep-c S-sweep-c-15; Lei 9.983/2000's first day (15 or 16.10.2000) is uncertain and 15.10.2000 is refused by name (F-g6a-22).
- [x] M-sweep-c-28 (Lei 10.684/2003 art. 9º for art. 337-A) encoded.
- [x] Forks: `registers/parts/g6a.forks.json`, 27 entries (5 reserved F-sweep-c-*, 22 F-g6a-*); validates; every cross-ref resolves against sweep-c or sweep-b.
- [x] Positive control: 21 single mutations, all caught; two unmutated controls fully satisfied (`scratchpad/g6a/mutar-2.txt`).
- [x] Herald check: `nlg --lang en` on the five test modules, 442 lines; 0 of the 322 rules defined in g6a's modules and `cp-pena.l4` render as a bare name.
- [x] The reviewer's sections of these notes (below).
- Half-done: nothing inside a module; every file parses.
- Last check.sh TOTAL (2026-09-30, after the conductor's check.sh fix): `TOTAL (13 modules)                                 0       442       0       0     442`
- Next: nothing owed inside the range. The report to the lead is the last step.

## Plan of modules

| module | articles |
| --- | --- |
| `cp-g6a-funcionario-publico.l4` | 327 (caput, § 1º, § 2º) — imported by every other g6a module |
| `cp-g6a-peculato-a-concussao.l4` | 312, 313, 313-A, 313-B, 314, 315, 316 |
| `cp-g6a-corrupcao-passiva-a-sigilo.l4` | 317, 318, 319, 319-A, 320, 321, 322, 323, 324, 325, 326 |
| `cp-g6a-usurpacao-a-corrupcao-ativa.l4` | 328, 329, 330, 331, 332, 333 |
| `cp-g6a-descaminho-a-sonegacao.l4` | 334, 334-A, 335, 336, 337, 337-A |
| `cp-g6a-administracao-estrangeira.l4` | 337-B, 337-C, 337-D |

Each has a `-testes.l4` beside it.

## 1. What is encoded, and what is not

Every article of Título XI, Capítulos I, II and II-A: arts. 312 to 337-D, 34 roadmap units, all `encoded`.
For each punishing provision: the case record, the elements, consummated and attempted where the conduct can be begun and stopped (fork F-g6a-05), the pena cominada of every preceito, every cause of increase as a constant plus an `incide …` predicate, and exported functions for the crime, the pena for a case, the causes and the outer limits.
None of these articles states its ação penal, so none is written (art. 100 is g1c's).

**Two definitions other groups need.** Art. 327: `funcionário público para os efeitos penais (art. 327)` takes the person's `Vínculo com a administração pública` and the date of the fact, so the contracted-company limb of § 1º is gated on Lei nº 9.983/2000. Art. 337-D: `funcionário público estrangeiro (art. 337-D)`. At integration, groups that now read the `cp-dominio` facts directly (art. 155 § 11, IV and others) should call the first.

**Shared machinery, `cp-g6a-comum.l4`.** `Ato do agente` (agent, the art. 327 § 2º bodies, the act, and how far the execution went: begun, completed, stopped from outside), which every g6a case record embeds. Art. 14, I is the elements plus a completed conduct; art. 14, II the elements with the conduct begun, not completed and stopped from outside. The article's facts record the conduct undertaken, so an attempt says which crime was attempted. The module also holds every vigência date (one constant per law), the heaviest-penalty fold and the cause-list helpers.

**Temporal scope (PLAN § 10), with the dates of sweep-c S-sweep-c-15.**

| law | in force | what it did | encoded as |
| --- | --- | --- | --- |
| Lei nº 8.137/1990 | 28.12.1990 | art. 316 § 1º re-worded; art. 318's pena | § 1º refused whole before; art. 318's pena refused before |
| Lei nº 9.127/1995 | 17.11.1995 | art. 332 re-worded | refused whole before |
| Lei nº 9.983/2000 | 15 or 16.10.2000 | added arts. 313-A, 313-B, 325 §§ 1º–2º, 327 § 1º's second limb, 337-A | not law before 15.10; refused ON 15.10 (F-g6a-22); law from 16.10 |
| Lei nº 10.467/2002 | 12.6.2002 | added Capítulo II-A | not a crime before |
| Lei nº 10.684/2003 | 31.5.2003 | art. 9º (M-sweep-c-28) | a benefit: reaches earlier acts |
| Lei nº 10.763/2003 | 13.11.2003 | arts. 317 and 333 penas | penas refused before; definitions answer for any date |
| Lei nº 11.466/2007 | 29.3.2007 | added art. 319-A | not a crime before |
| Lei nº 13.008/2014 | 27.6.2014 | art. 334 re-worded, art. 334-A created | both refused before (the old art. 334 held both crimes) |
| Lei nº 13.964/2019 | 23.1.2020 | art. 316 caput's pena | pena refused before; definition answers for any date |
| LC nº 225/2026 | 9.1.2026 | art. 337-A §§ 5º–6º; Lei nº 10.684 art. 9º § 3º | exclusions reach acts from that day on (F-g6a-19) |

**Not encoded, deliberately.** Concurso between crimes (the absorption of a falsity exhausted in descaminho, F-sweep-c-12, is g5's to create); jurisdiction and venue (M-sweep-c-24); Súmula 560 STF (M-sweep-c-18); Lei nº 9.430/1996, art. 83, which no sweep read.

## 2. Forks, in prose

`registers/parts/g6a.forks.json`, 27 entries: the five sweep-c reserved ids for this range, and F-g6a-01 to -22.

| id | question | taken |
| --- | --- | --- |
| F-sweep-c-01 | art. 319 and judges' interpretive positions (ADPF 881, pending) | `tipoOrdinario`: the type on its terms; the ADPF fact carried and deliberately not read |
| F-sweep-c-02 | art. 331: every disrespect, or only grave and evident contempt | ADPF 496 ementa item 5, as the judge's finding |
| F-sweep-c-10 | insignificância in Título XI | **settled**: Súmula 599, save descaminho (Tema 157) and cigarette contraband (Tema 1143). Created here, since g6a owns art. 312; g6b cross-refers |
| F-sweep-c-14 | art. 330 and orders to stop in ostensive policing | **settled** by STJ Tema 1060: typical |
| F-sweep-c-15 | art. 337-A before the credit is definitively constituted | not a crime (SV 24 extended; resolved, not settled: the link is an MPF enunciado) |
| F-g6a-01 | art. 327 § 1º's equiparação on the victim's side | reaches both sides |
| F-g6a-02 | art. 327 § 2º's list of bodies | closed: an autarquia is not in it |
| F-g6a-03 | art. 327 § 2º's reach | Capítulo I only; each author personally |
| F-g6a-04 | Capítulo I articles that do not name the agent (313, 314, 315, 318, 319, 319-A, 325 § 1º, 326) | a funcionário, by the chapter's heading |
| F-g6a-05 | which crimes have an attempted form | commissive intentional ones; not the culpable form or the omissions |
| F-g6a-06 | art. 312: does "em proveito próprio ou alheio" qualify appropriation | yes, both verbs |
| F-g6a-07 | art. 312 § 2º's "crime de outrem" | any crime of another, certified as fact |
| F-g6a-08 | art. 312 § 3º (and art. 337-A § 1º) on the very day of the other event | refused by name |
| F-g6a-09 | art. 313-B p.ú. "As penas": the fine too? | custodial range only; open question |
| F-g6a-10 | "se o fato não constitui crime mais grave" (arts. 314, 325, 337) | the judge's finding; reaches art. 325 § 1º, not § 2º |
| F-g6a-11 | arts. 316–317 "antes de assumi-la" | reaches one not yet an official |
| F-g6a-12 | art. 318 "(art. 334)" after art. 334-A was created | reaches contrabando of art. 334-A |
| F-g6a-13 | art. 322 and the abuse-of-authority statutes | encoded as printed; revocation arguable, unresearched |
| F-g6a-14 | art. 323 "cargo público" | holders of a cargo only |
| F-g6a-15 | arts. 326 and 335 against arts. 337-I, 337-J, 337-K (g6b) | encoded as printed; displacement for integration |
| F-g6a-16 | art. 329 § 2º article-wide | yes; extensionally the same |
| F-g6a-17 | arts. 334/334-A § 3º's reach | the whole article, § 1º included |
| F-g6a-18 | art. 335 "procurar afastar" | the attempt is the crime, no reduction |
| F-g6a-19 | art. 337-A § 5º for earlier acts | only acts from LC nº 225/2026's vigência |
| F-g6a-20 | art. 337-A § 1º and Lei nº 10.684/2003 art. 9º | two independent grounds (M-sweep-c-28) |
| F-g6a-21 | art. 337-A § 4º's readjusted ceiling | a parameter; refused by name if asked of the encoding |
| F-g6a-22 | Lei nº 9.983/2000's first day in force | 15.10.2000 refused; from 16.10.2000 in force |

Where the forks were looked for: every preceito secundário (species, bounds, fine conjunction), every "ou"/"e" chain, every cross-reference, every date, the chapter headings, and the overlaps with g6b's Capítulo II-B.

## 3. Sweep entries acted on

| entry | class | what g6a did |
| --- | --- | --- |
| M-sweep-c-02 (V33) | interpretive | fork F-sweep-c-01 created at art. 319 |
| M-sweep-c-05 | interpretive | fork F-sweep-c-02 created at art. 331 |
| M-sweep-c-15, -16, -17 | interpretive | fork F-sweep-c-10 created; insignificância encoded at arts. 334 and 334-A only |
| M-sweep-c-18 | interpretive, no-effect | checked; Súmula 560 not modelled (module header of art. 334) |
| M-sweep-c-20 | interpretive | read; F-sweep-c-12 is g5's to create (lowest article 297); noted at art. 334 |
| M-sweep-c-22 | interpretive | fork F-sweep-c-14 created at art. 330 |
| M-sweep-c-23 | interpretive | fork F-sweep-c-15 created at art. 337-A |
| M-sweep-c-24 | interpretive, no-effect | checked; jurisdiction súmulas not modelled |
| M-sweep-c-28 | **binding** (added) | Lei nº 10.684/2003 art. 9º encoded beside art. 337-A § 1º: suspension, extinction by payment, persistent-debtor exclusion |
| M-sweep-b-11 | binding (sweep-b's, art. 168-A) | cross-referenced from F-g6a-19 and F-g6a-20 |
| S-sweep-c-15 | search | every vigência date in `cp-g6a-comum.l4` and the art. 327 module |

M-sweep-c-01 (Lei nº 7.209/1984, art. 2º) was checked: no preceito in arts. 312–337-D prints a multa amount (S-sweep-c-14 agrees; art. 337-A § 3º's R$ 1.510,00 is a payroll ceiling).

## 4. PROPOSTO-COMUM

- `Entidade da administração pública` (art. 327 module): the kind of body a commissioned post is in. It replaces `cp-dominio`'s `ocupa cargo em comissão ou função de direção ou assessoramento`, whose gloss folds § 2º's list into the fact; g6a does not read that boolean.
- `a mais grave das duas penas cominadas` / `a mais grave das penas cominadas` and `a causa, se incide` / `as causas que incidem` / `as causas com a da tentativa` (`cp-g6a-comum.l4`): what `cp-g3-furto.l4` writes in `WHERE` blocks; candidates for `cp-pena.l4`.
- The Lei nº 10.684/2003 art. 9º predicates: arts. 168-A (g3) and 337-A should share one (M-sweep-c-28).
- `Relação da conduta com a função` (arts. 316, 317, 331) and `Ato do agente` are g6a-internal; `Vínculo com a administração pública estrangeira` is used only by Capítulo II-A.

## 5. What `check.sh` prints

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-g6a-`, 2026-09-30:

```
module                                        errors satisfied  failed refused asserts
cp-g6a-administracao-estrangeira-testes.l4         0        26       0       0      26
cp-g6a-administracao-estrangeira.l4                0         0       0       0       0
cp-g6a-casos.l4                                    0         0       0       0       0
cp-g6a-comum.l4                                    0         0       0       0       0
cp-g6a-corrupcao-passiva-a-sigilo-testes.l4        0       112       0       0     112
cp-g6a-corrupcao-passiva-a-sigilo.l4               0         0       0       0       0
cp-g6a-descaminho-a-sonegacao-testes.l4            0       100       0       0     100
cp-g6a-descaminho-a-sonegacao.l4                   0         0       0       0       0
cp-g6a-funcionario-publico.l4                      0         0       0       0       0
cp-g6a-peculato-a-concussao-testes.l4              0       135       0       0     135
cp-g6a-peculato-a-concussao.l4                     0         0       0       0       0
cp-g6a-usurpacao-a-corrupcao-ativa-testes.l4       0        69       0       0      69
cp-g6a-usurpacao-a-corrupcao-ativa.l4              0         0       0       0       0
TOTAL (13 modules)                                 0       442       0       0     442
(a failed assertion also counts as an error; errors minus failed = everything else)
```

**Positive control.** Every test module passed on its first run, so 21 single mutations were made to scratch copies, one at a time, each breaking something the text decides (the § 2º list, the 9.983 gate and its uncertain day, § 3º's same day, the proveito limb, a penalty bound, the heaviest-penalty fold, the attempt reduction, § 1º of art. 317, art. 318's crime, art. 325's subsidiarity, art. 329's threat, art. 331's gravity, art. 333's gate, art. 334's ceiling, art. 334-A's refusal, art. 335's "procurar afastar", art. 337-A's § 5º and § 3º, art. 337-D, and Lei nº 10.684's § 3º). All 21 were caught, and two unmutated controls were fully satisfied. The harness's first version captured only stdout and scored every run as caught with 0 of N satisfied; that run proved nothing and was repaired before the result above.

**English.** `nlg --lang en` renders 442 lines for the five test modules, one per assertion; no rule of g6a's modules renders as its bare name.

## 6. Open questions for a Brazilian criminal lawyer

1. Does art. 327 § 1º's equiparação make an equated person a "funcionário público" as victim of resistance, disobedience, desacato and active corruption? (F-g6a-01)
2. Does art. 327 § 2º reach an officer holding a commissioned post in an autarquia? (F-g6a-02)
3. Are arts. 326 and 335 displaced by arts. 337-I, 337-J and 337-K for licitações? (F-g6a-15)
4. Does art. 322 survive the abuse-of-authority statutes? (F-g6a-13)
5. Does art. 313-B's "As penas são aumentadas" raise the number of dias-multa? (F-g6a-09)
6. Does STJ Tema 157's insignificância for "crimes tributários federais" reach art. 337-A? (F-sweep-c-10, notes)
7. Is art. 337-A typified before the definitive constitution of the credit? (F-sweep-c-15)
8. Does Lei nº 9.430/1996, art. 83, condition Lei nº 10.684/2003, art. 9º, for art. 337-A? (F-g6a-20)
9. A repair of the damage on the very day the sentence becomes final (art. 312 § 3º): before or after? (F-g6a-08)
10. Which of these crimes admit an attempt, in particular disobedience and desacato in writing? (F-g6a-05)
11. Was Lei nº 9.983/2000 in force on 15.10.2000? (F-g6a-22)

## 7. For the conductor at integration

- Arts. 326/335 and g6b's arts. 337-I/337-J/337-K overlap (F-g6a-15); g6b has been told.
- Replace `cp-dominio`'s `ocupa cargo em comissão ou função de direção ou assessoramento` with `Entidade da administração pública` (§ 4).
- Groups that read the art. 327 facts directly should call `funcionário público para os efeitos penais (art. 327)`.
- Arts. 168-A and 337-A should share the Lei nº 10.684/2003 art. 9º predicate.
- `notes/conductor.md` was read at the start, before it was withdrawn. One fork note cited a test author's expectation from it; that note has been removed, and no reading in the encoding rests on it.
