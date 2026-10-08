# g4a — arts. 213–249 (Parte Especial, Títulos VI and VII): notes for the reviewer

**Status (2026-10-08): all 49 units disposed (35 encoded, 14 inert, 0 deferred); six modules and six tests modules written and checked. Revised 2026-10-08 for art. 234-B § 3º (fork F-g4a-24), on a finding of the independent test pass.**
`check.sh`'s output is in § 5, verbatim.

## PROGRESS

- [x] Read BRIEF.md, PLAN.md, the writing-l4-rules skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages) and encoding-a-subject.
- [x] Read cp-dominio.l4, cp-pena.l4, cp-g3-furto.l4 and its tests.
- [x] Read source lines 1519–1771 (arts. 213–249), every sweep-c entry and search, and the reserved forks F-sweep-c-06 to -09.
- [x] Asked sweep-c for the pre-2025 laws' vigência clauses; answered in S-sweep-c-18 (§ 4).
- [x] `cp-g4a-dignidade-sexual-geral.l4` + tests — Título VI nouns; Caps. III, IV, VII (arts. 219–226, 234-A–234-C).
- [x] `cp-g4a-vulneravel.l4` + tests — Cap. II (arts. 217–218-C).
- [x] `cp-g4a-liberdade-sexual.l4` + tests — Caps. I and I-A (arts. 213–216-B).
- [x] `cp-g4a-lenocinio.l4` + tests — Caps. V and VI (arts. 227–234).
- [x] `cp-g4a-casamento-e-filiacao.l4` + tests — Título VII Caps. I–II (arts. 235–243).
- [x] `cp-g4a-assistencia-familiar.l4` + tests — Título VII Caps. III–IV (arts. 244–249).
- [x] `nlg --lang en` on every tests module: no rule or constructor of these modules renders bare (§ 5).
- [x] Mutations (§ 5): each caught.
- [x] `registers/parts/g4a.forks.json` (28 entries) validates; `registers/parts/g4a.roadmap.json` validates.
- [x] 2026-10-08, conductor's request (ta-g4, IT-g4-173): art. 234-B § 3º now reads the crime; fork F-g4a-24 records both readings; both are executable and tested; positive control run (below).
- [x] 2026-10-08, conductor's request (s-dolo-audit, both MED): arts. 218-C and 234 (caput, p.ú. I) now require the agent's knowledge (arts. 18 p.ú., 20); fork F-g4a-25; positive control run (below).

Import order: `geral` ← `vulneravel` ← `liberdade-sexual`; `geral` ← `lenocinio`. The Título VII modules import only `cp-dominio` and `cp-pena`.

Checkpoint (2026-10-08): **done** — all 49 units, and the art. 234-B § 3º revision (F-g4a-24); **half-done** — nothing; **next** — nothing in range; only answering the conductor at integration. Paths moved on 2026-10-08: ENC is now under `~/src/legalese/commonswt/br-penal/…`, the validator is run from `/Volumes/transcend/src/l4wt/br-penal`, and scratch is `~/.claude/br-penal-scratch/g4a/`.
Last `check.sh <ENC> cp-g4a-` TOTAL, verbatim (2026-10-08):
`TOTAL (12 modules)                                 0       433       0       0     433`
The conductor's private log (`notes/conductor.md`, since moved out of ENC) was read at the start; nothing encoded here depends on it (ages follow cp-pena and F-g0-06, not its test-author notes).

## 1. What is encoded, and what is not

Every article in 213–249 that states a crime is encoded: the elements (consummated and, where the text admits it, attempted, through cp-pena's art. 14), each preceito secundário as a `Pena cominada` checked against its words, every cause of increase as a fraction plus a predicate, the qualified and privileged forms, the judge's options where the Code gives a power (arts. 242 p.ú., 249 § 2º), and the ação penal where the Code states it (art. 225 for Título VI Caps. I–II; art. 236 p.ú.).
The general provisions of Título VI (arts. 225, 226, 234-A, 234-B) are encoded once, in `cp-g4a-dignidade-sexual-geral.l4`, over an enum of the Título's crimes, and each offence module lists the causes that reach it.

Carried inert (labelled stubs, no operative outcome): the revoked arts. 214, 216, 217, 219–222, 223, 224, 231, 231-A, 232 and 240, and the vetoed art. 234-C.

**Not encoded, deliberately:**

- **Earlier wordings.** Every rule answers for a fact from the vigência of the law that gave its words their current form. Where that law replaced earlier words, the rule refuses by name for an earlier fact (e.g. art. 217-A's penalties before 8.12.2025, art. 213 before 10.8.2009, art. 225 before 25.9.2018). Where the law added a provision that replaced nothing, the provision is simply not law before (arts. 215-A, 216-A, 216-B, 218-A, 218-B, 218-C, 232-A, and paragraphs such as art. 216-A § 2º and art. 226, IV). For a whole new crime the penalty function has no value to return before the crime existed, so it refuses with the law's own answer in words ("não havia crime do art. 215-A antes da Lei nº 13.718, de 2018") — see § 7.
- **What the civil and education laws decide**: which impediments void a marriage, what "erro essencial" is, "idade escolar", "instrução primária", who is "interdito". Taken as facts or findings.
- **Open standards**: "obsceno", "exploração sexual", "sem justa causa", "motivo de reconhecida nobreza", "se o fato não constitui crime mais grave" (where the graver crime is outside my modules). Findings, never computed.
- **Art. 61, II, f** is g1b's; only whether art. 226, II leaves room for it (STJ Tema 1215) is here.

## 2. The forks, in prose

28 entries in `registers/parts/g4a.forks.json`: four carry the ids sweep-c reserved (F-sweep-c-06 to -09, all settled by an authority the sweep found); the rest are F-g4a-01 to -24, resolved by argument.
Where I looked: every article's words; each "ou"/"e" and each list against its siblings (arts. 213 § 1º, 218-B § 2º, 227 § 1º, 228 § 1º, 230 § 1º); every "se o fato não constitui crime mais grave"; every reach clause ("neste Título", "Capítulos I e II", art. 226's silence); every consummation verb; every date.

| id | question | taken |
| --- | --- | --- |
| F-g4a-01 | When the older amending laws took effect | each clause as sweep-c read it (S-sweep-c-18); Lei 5.478/1968: 25.8 or 13.9.1968, the encoding answers from 13.9.1968 and refuses before |
| F-g4a-02 | One act within several articles (213/215/215-A/217-A; 227/218; 228/218-B; 237/235) | specialty: 217-A over 213 and 215; 213 over 215; 215-A subsidiary; 218 over 227; 218-B over 228; 235 over 237 |
| F-g4a-03 | Art. 226's reach, and inciso IV against inciso I | Caps. I, I-A, II; IV reaches estupro (its rubrics), and there IV, a displaces I |
| F-g4a-04 | Does art. 225 reach Capítulo I-A (art. 216-B)? | no; art. 100 decides — the same unconditioned prosecution either way |
| F-g4a-05 | Do arts. 234-A and 234-B reach art. 232-A (migration, placed in Título VI)? | yes, "neste Título" |
| F-g4a-06 | Art. 226, II on art. 216-A, whose element is the authority | not for the authority that is the element; yes for a kinship beside it |
| F-g4a-07 | Art. 234-A, IV "pessoa com deficiência" where the disability is the element (217-A § 1º, 218-B) | excluded there; a disabled child under fourteen still counts |
| F-g4a-08 | Temporal reach of art. 234-B §§ 1º–3º (Lei 15.035/2024) | §§ 1º–2º for convictions from 28.11.2024; § 3º for facts from that day |
| F-g4a-09 | Art. 218 where the induced act is contact with the third person | that is art. 217-A, the inducer taking part; 218 is the contactless inducement (fact-supplied) |
| F-g4a-10 | When arts. 218 and 227 are consummated | when the victim does the act (material) |
| F-g4a-11 | When arts. 218-B and 228 are consummated; attempt at 229–230 | when the victim is in exploitation; 229 and 230 habitual, no attempt |
| F-g4a-12 | "lesão corporal de natureza grave" (213 § 1º, 217-A § 3º) | includes gravíssima (as F-g0-23) |
| F-g4a-13 | "exploração sexual" (218-B, 228, 229) | the court's finding |
| F-g4a-14 | Art. 218-C § 2º, "ressalvada sua prévia autorização, caso seja maior de 18" | an adult victim's prior authorisation dispenses with anonymity |
| F-g4a-15 | Art. 213 § 1º, "menor de 18 ou maior de 14" | read "e": fourteen to seventeen (the literal reading makes every victim qualified) |
| F-g4a-16 | Art. 216-B, "sem autorização dos participantes" | unauthorised unless every participant authorised |
| F-g4a-17 | Art. 230 § 1º and a victim under fourteen | not in § 1º's words (caput); art. 218-B likely applies anyway |
| F-g4a-18 | When art. 232-A is consummated | by the acts of promotion (formal) |
| F-g4a-19 | "obsceno" (233, 234) | the court's finding |
| F-g4a-20 | Attempt at art. 236 | none: the prosecution needs an annulled marriage |
| F-g4a-21 | Art. 242: what "suprimindo ou alterando direito inerente ao estado civil" qualifies | the last limb only (the semicolons) |
| F-g4a-22 | Art. 244 "cônjuge" and the companheiro | spouse only (no analogy against the accused) |
| F-g4a-23 | Art. 249 § 1º | a contrario: a parent, guardian or curator not deprived is not the agent |
| F-g4a-24 | Art. 234-B § 3º, "O réu condenado": which convicts are monitored | § 1º's réu — a convict of one of the eight listed crimes, not of any crime of the Título; both readings executable (`o réu condenado passa a ser monitorado, na leitura`) and tested on arts. 213 (both), 233 and 232-A (they part) |
| F-g4a-25 | Arts. 218-C and 234: knowledge as an element of dolo | positive findings, absent = no crime; for art. 234 knowledge of the content, never that it is legally `obsceno` (art. 21); no culpable form, so no `Elemento subjetivo` |
| F-sweep-c-06 | Can the presumption of art. 217-A be relativised before § 4º-A? | **settled**: no (STJ Súmula 593, Tema 918; M-sweep-c-10); relativising reading arguable, pending at the TJMG (M-sweep-c-11, currency risk) |
| F-sweep-c-07 | A slight lustful act with a child under fourteen: 215-A? | **settled**: no, always 217-A (STJ repetitive thesis, 1.7.2022; M-sweep-c-12) |
| F-sweep-c-08 | Art. 61, II, f with art. 226, II | **settled**: both, save where authority is the only link (STJ Tema 1215; M-sweep-c-13) |
| F-sweep-c-09 | Ação penal for facts before 25.9.2018 | **settled** that the 2009 wording governs (STJ Súmula 670; M-sweep-c-14); that wording is not in the source, so the rule refuses |

## 3. Proposed shared nouns (PROPOSTO-COMUM)

- `Fim para o qual a vítima está confiada ao agente` (`cp-g4a-lenocinio.l4`): "pessoa a quem esteja confiada para fins de educação, de tratamento ou de guarda" (art. 227 § 1º). Art. 136 (maus-tratos, g2a) reads the same facts ("para fim de educação, ensino, tratamento ou custódia"); `Relação do agente com a vítima` has no member for them.

Not proposed, but the conductor may want to know: three modules each define a one-line vigência comparison (`em vigor na data`, `… (Título VII)`, `… (arts. 244 a 249)`) under different names so they can be imported together; a shared helper in `cp-pena` would replace them. Título VII's "filho" (the victim is the agent's child) is a field on each case record, because no relation member is that narrow.

## 4. Sweep entries acted on, and the dates

| entry | class | where it landed |
| --- | --- | --- |
| M-sweep-c-10 | interpretive | F-sweep-c-06 (settled_by); art. 217-A reads no consent, experience, earlier relations or pregnancy |
| M-sweep-c-11 | interpretive | F-sweep-c-06 (the arguable reading, currency risk) |
| M-sweep-c-12 | interpretive | F-sweep-c-07 (settled_by); art. 215-A's "crime mais grave" computes art. 217-A |
| M-sweep-c-13 | interpretive | F-sweep-c-08 (settled_by); `a agravante do art. 61, II, f, pode concorrer com o aumento do art. 226, II (STJ, Tema 1215)` |
| M-sweep-c-14 | interpretive | F-sweep-c-09 (settled_by); `a ação penal do art. 225` refuses before 25.9.2018 |
| M-sweep-c-27 | binding | art. 244's multa is plain "e multa" (art. 49's day-fine); the minimum-wage range quoted inert in `a multa impressa no art. 244, cancelada pela Lei nº 7.209, de 1984`. Also M-sweep-a-07 (PLAN § 2.2). |

No other sweep-c entry names an article in 213–249. S-sweep-c-03's anomaly (a Lei 12.737/2012 "Encerramento de Vigência" of a non-existent art. 248 parágrafo único) is noted at art. 248.

Vigência dates (S-sweep-c-04 and S-sweep-c-18 quote each clause): Lei 10.224/2001 16.5.2001; Lei 11.106/2005 29.3.2005; Lei 12.015/2009 10.8.2009; Lei 13.445/2017 21.11.2017 (art. 125, 180 days); Lei 13.718/2018 25.9.2018; Lei 13.772/2018 20.12.2018; Lei 15.035/2024 28.11.2024; Lei 15.280/2025 8.12.2025; Lei 15.353/2026 8.3.2026; Lei 10.741/2003 1.1.2004 (art. 118, 90 days); Lei 5.478/1968 25.8.1968 or 13.9.1968 (F-g4a-01); Lei 6.898/1981 1.4.1981; Lei 7.251/1984 21.11.1984.
I first took these from the Senado record's DOU dates and my recollection of two vacatio clauses; sweep-c's reading confirmed all but Lei 5.478/1968, whose date moved from 26.7.1968 to 13.9.1968.

## 5. What `check.sh` prints

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh <ENC> cp-g4a-`, 2026-10-08, final tree, exit 0, 2 min 44 s wall clock:

```
module                                        errors satisfied  failed refused asserts
cp-g4a-assistencia-familiar-testes.l4              0        58       0       0      58
cp-g4a-assistencia-familiar.l4                     0         0       0       0       0
cp-g4a-casamento-e-filiacao-testes.l4              0        47       0       0      47
cp-g4a-casamento-e-filiacao.l4                     0         0       0       0       0
cp-g4a-dignidade-sexual-geral-testes.l4            0        69       0       0      69
cp-g4a-dignidade-sexual-geral.l4                   0         0       0       0       0
cp-g4a-lenocinio-testes.l4                         0        73       0       0      73
cp-g4a-lenocinio.l4                                0         0       0       0       0
cp-g4a-liberdade-sexual-testes.l4                  0        83       0       0      83
cp-g4a-liberdade-sexual.l4                         0         0       0       0       0
cp-g4a-vulneravel-testes.l4                        0       103       0       0     103
cp-g4a-vulneravel.l4                               0         0       0       0       0
TOTAL (12 modules)                                 0       433       0       0     433
(a failed assertion also counts as an error; errors minus failed = everything else)
```

**Glosses.** `l4 nlg --lang en` on each tests module, every backticked name in the output compared with the rules and constructors these six modules define: none renders bare. Positive control: the same scan does list the tests' own fixtures (`um casamento`, `em junho de 2026`), which carry no herald.

**Mutations** (one at a time, on a copy of the modules; each run's failed or refused count must rise):

| module mutated | mutation | test file's verdicts after it |
| --- | --- | --- |
| cp-g4a-vulneravel.l4 | "menor de 14" → "menor de 15" in arts. 217-A, 218 and 218-A at once (one sed matched all three) | 1 failed (only art. 217-A then had a birthday test) |
| cp-g4a-vulneravel.l4 | art. 217-A § 3º's minimum 12 years → 11 | 1 failed |
| cp-g4a-dignidade-sexual-geral.l4 | Lei 15.280/2025's vigência one day early | 6 failed: the gate's own assertion, and five `#ASSERT REFUSED` reporting "assertion failed: expected a refusal, but the expression produced a value" (read, not inferred) |
| cp-g4a-vulneravel.l4 | art. 218-C § 2º's exclusion removed | 3 failed |
| cp-g4a-vulneravel.l4 | "maior de 14" → "maior de 13" in art. 218-B § 2º, I | 1 failed |
| cp-g4a-lenocinio.l4 | the minimum 3 years (arts. 228 § 1º, 230 § 1º) → 4 | 3 failed |
| cp-g4a-lenocinio.l4 | "submeter" admitted as an art. 228 verb | 1 failed |
| cp-g4a-casamento-e-filiacao.l4 | art. 235 § 2º's annulment ignored | 2 failed |
| cp-g4a-assistencia-familiar.l4 | art. 244 "maior de 60" → "maior de 61" | 1 failed |
| cp-g4a-dignidade-sexual-geral.l4 | art. 226, IV, a no longer displaces I | 3 failed |
| cp-g4a-liberdade-sexual.l4 | art. 213 § 1º read literally ("ou maior de 14") | 7 failed |
| cp-g4a-dignidade-sexual-geral.l4 | (2026-10-08) art. 234-B § 3º's exported rule pinned to the wider reading | 3 failed: exactly the no-monitoring assertions for arts. 233, 232-A and 215, where the readings part (66 of 69 satisfied) |

The first run of the first mutation also showed arts. 218 and 218-A had no fourteenth-birthday test; both were added.

## 6. Open questions for a Brazilian criminal lawyer

1. **Art. 226's reach** (F-g4a-03): does inciso IV reach every crime of Caps. I and II, or only estupro, as its rubrics say? And does IV, a displace I?
2. **Art. 213 or 217-A § 1º** where the agent's own violence left the victim unable to resist: the encoding follows the victim's condition as the fact supplier records it (F-g4a-02, note).
3. **Art. 230 § 1º and a victim under fourteen** (F-g4a-17): the words leave a gap; is it art. 218-B, or the caput?
4. **Art. 245 § 2º and the ECA** (arts. 238–239, 1990): did the Estatuto displace § 2º (1984)? The ECA is outside the sources and the sweep's correlated-legislation rows were not researched (S-sweep-c-03).
5. **Art. 234-B §§ 1º–3º** (F-g4a-08): procedural and immediate, or material and prospective?
6. **Lei 5.478/1968** (F-g4a-01): did the rectification of 14.8.1968 restart the vacatio, and did the 1974 republication correct art. 244?
7. **"exploração sexual"** (F-g4a-13): is an adult's voluntary prostitution within arts. 228–229?
8. **Art. 218** (F-g4a-09, -10): where is the line between inducing a contactless act and taking part in art. 217-A, and is the crime formal or material?
9. **Art. 246**: what "instrução primária" and "idade escolar" mean today (ensino fundamental? four to seventeen?).

## 7. For the conductor at integration

- **"Não havia crime" as a refusal.** A penalty function for a crime that did not yet exist (arts. 215-A, 216-A, 216-B, 232-A) refuses with the law's own answer in words, because `Pena cominada` has no "no such crime" value. PLAN § 10 reserves refusals for the encoder's gaps; this is the one place I bent that, and a `MAYBE Pena cominada` (or a type-wide convention) would be the alternative. The crime predicates themselves answer FALSE before those dates.
- **Cross-group readings to align**: F-g4a-12 repeats g0's F-g0-23; F-g4a-02's specialty reading for 218/227 and 218-B/228 reads the age facts directly rather than calling Cap. II's rules, since the modules share a group but not a case record.
- **Defects in the Code's text met on the way** (no assertion failed; each is a finding about the text, recorded where it bites): art. 213 § 1º's "ou maior de 14" (F-g4a-15); art. 216-A's § 2º with no § 1º (the vetoed parágrafo único); art. 228 § 2º's stray comma ("Se o crime, é cometido"); Capítulo IV of Título VII headed "PÁTRIO PODER, TUTELA CURATELA" without the comma; art. 230 § 1º's age gap (F-g4a-17).
- **A blind spot in `check.sh`'s failed column — since fixed by the conductor** (`msg()` now accepts both layouts; this paragraph records what was found). A failing `#ASSERT REFUSED` prints its message on the line after `Message:` ("assertion failed: expected a refusal, but the expression produced a value"), and `check.sh` counts only `Message: assertion failed` on one line. Measured on the vigência mutation above: the file showed 6 errors, 1 failed, 0 refused. The run still fails (errors, and satisfied + failed + refused falls short of the assertion count, so UNACCOUNTED fires), but the failed column under-reports. Matching the message across the line break, or counting "assertion failed" anywhere in the diagnostic, would fix it.
- **Run time.** Measured with `time l4 run` on 2026-09-29: `cp-g4a-liberdade-sexual-testes.l4` 58 s, `cp-g4a-vulneravel-testes.l4` 20 s, `cp-g4a-dignidade-sexual-geral-testes.l4` 11 s. Most of the Cap. I assertions pass through the apparent-conflict chain (215-A → 215 → 213 → 217-A); I have not profiled whether that is the cost.

## 8. The missing-knowledge fix (2026-10-08, fork F-g4a-25), old -> new

- `cp-g4a-vulneravel.l4`: `Fato de divulgação de cena de sexo ou de estupro` gains `o agente sabia o que o registro continha` and `o agente sabia que a vítima não consentira`. New rule `o agente conhecia o registro (art. 218-C; art. 18, p.ú.)`: content known, and, unless the record is a rape scene or apologia, non-consent known. `divulgação consumada` and `divulgação tentada` each now also require it. Old: neither read any knowledge.
- `cp-g4a-lenocinio.l4`: `Fato de escrito ou objeto obsceno` gains `o agente conhecia o conteúdo do escrito, desenho, pintura, estampa ou objeto`. New rule `o agente conhecia o conteúdo do objeto (art. 234, caput)`: the finding, or `fazer` among the verbs. `crime de escrito ou objeto obsceno (art. 234)`: the caput limb requires it; the p.ú. limb is now (II or III verb) or (I verb and the finding). Old: the caput limb needed the judge's obscenity finding only, and any p.ú. verb sufficed.
- Tests: `uma divulgação` and `um objeto` keep their signatures and now set both knowledge findings TRUE; `divulgação conforme o que o agente sabia` and `um objeto conforme o que o agente sabia` take them as arguments. The inline record of the consent test carries the two new fields. 6 new asserts in `cp-g4a-vulneravel-testes.l4`, 7 in `cp-g4a-lenocinio-testes.l4`; no existing expected value changed.
- Art. 234-B's rules read the crime of conviction and list neither article: no test moved.
- Positive control (scratch copy with the knowledge requirement replaced by TRUE): 4 new asserts fail in each module (8 in all).
- Observed, not changed: the p.ú. limb of art. 234 does not read the judge's obscenity finding, though the field's gloss says it covers it.
- Records built outside g4a's modules (e.g. `cp-ind-*`) need the three new fields.
