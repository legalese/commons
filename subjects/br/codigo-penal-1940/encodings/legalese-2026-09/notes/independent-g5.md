# Independent test pass — ta-g5: Título X (arts. 289–311-A), Título XII (arts. 359-I–359-U), Disposições Finais (arts. 360–361)

Test author ta-g5, 2026-09-30 (phase 2).
The cases were written on 2026-09-29 from the source text alone, before the encoding existed for the author to read: `~/.claude/br-penal-oracle/cases/ta-g5.json`, sha256 `fd67bfdc852bf06f607824981e901e274442d65c572929b6292cc5900a3e47b2`, re-checked unchanged at the start and at the end of phase 2.
No expected value was changed to match the encoding.
Every case is now EXPOSED (`~/.claude/br-penal-oracle/EXPOSURE.md`, section "ta-g5").

## Files

| file | cases | directives |
| --- | --- | --- |
| `cp-ind-g5-moeda-falsa.l4` | IT-g5-001–033, 169 | 34 |
| `cp-ind-g5-papeis-publicos.l4` | IT-g5-034–051 | 18 |
| `cp-ind-g5-falsidade-documental.l4` | IT-g5-052–123, 168 | 73 |
| `cp-ind-g5-outras-falsidades.l4` | IT-g5-124–157 | 34 |
| `cp-ind-g5-fraudes-em-certames.l4` | IT-g5-158–167 | 10 |
| `cp-ind-g5-estado-democratico.l4` | IT-g5-170–227 | 54 (4 not expressible) |
| `cp-ind-g5-disposicoes-finais.l4` | IT-g5-228–232 | 0 (5 not expressible) |

Each case is one directive, directly under its comment line `-- IT-g5-NNN: <question>` with the question copied verbatim from the JSON; a script checked all 232 ids, the verbatim questions, one directive per case, and that refuse cases use `#ASSERT REFUSED` (one exception, IT-g5-127, below).
Undated cases are dated 1 June 2026 (`um fato em junho`), after every law that touched these articles, and the execution is complete unless the case says otherwise; each file says so at its top.

## Counts

| | n |
| --- | --- |
| cases | 232 |
| expressed as a directive | 223 |
| not expressible | 9 |
| satisfied | 212 |
| failed | 10 |
| refused (a plain `#ASSERT` whose expression refused) | 1 (IT-g5-203) |
| refuse cases satisfied as `#ASSERT REFUSED` | 0 of 3 (115, 123, 226 all failed; 127 is expressed differently, below) |
| disagreements (failed + refused) | 11 |

| class | n | ids |
| --- | --- | --- |
| (E) the encoding departs from the text | 5 | 008, 100, 113, 115, 123 |
| (F) a genuine ambiguity, recorded as a fork | 4 | 005 (F-sweep-c-11), 117 (F-sweep-c-12), 150 (F-g5-20), 224 (F-g5-29) |
| (S) stale: a later sweep finding | 2 | 203 (M-sweep-c-09 / F-sweep-c-05), 226 (S-sweep-c-17) |
| (T) the case misread the text | 0 | |
| (R) a conductor's strict ruling | 0 | |

Three of the five (E) are on cases marked arguable (100, 115, 123).
In each, the encoding took the other reading **without recording a fork**, which the brief requires of every ambiguity; the defect is at least the missing fork, and the answer may survive once one is written.
The other two (008, 113) are on cases marked certain.

## check.sh, verbatim

Run over all seven files from 17:37 to 17:53 SGT on 2026-09-30 (`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-ind-g5-`); `cp-ind-g5-estado-democratico.l4` was re-run alone at 22:57, after a comment-only edit, with the same line. Exit status 1, as expected with failures.

```
module                                        errors satisfied  failed refused asserts
cp-ind-g5-disposicoes-finais.l4                    0         0       0       0       0
cp-ind-g5-estado-democratico.l4                    2        51       2       1      54
cp-ind-g5-falsidade-documental.l4                  5        68       5       0      73
cp-ind-g5-fraudes-em-certames.l4                   0        10       0       0      10
cp-ind-g5-moeda-falsa.l4                           2        32       2       0      34
cp-ind-g5-outras-falsidades.l4                     1        33       1       0      34
cp-ind-g5-papeis-publicos.l4                       0        18       0       0      18
TOTAL (7 modules)                                 10       212      10       1     223
(a failed assertion also counts as an error; errors minus failed = everything else)
```

## Disagreements

| id | articles | expected (ta-g5) | the encoding's answer | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g5-005 | art. 289 | TRUE: a gross counterfeit that did deceive is still "falsificar" (arguable) | FALSE once the judge's grossness finding is set | F | F-sweep-c-11, settled by STJ Súmula 73 (M-sweep-c-19), the alternative the case named. |
| IT-g5-008 | art. 289 § 1º; art. 18 p.ú. | FALSE: Joaquim kept notes he received as genuine and never suspected; no dolo | TRUE: § 1º present | E | `moeda falsa do art. 289, § 1º` (`cp-g5-moeda-falsa.l4`) is met by `guardar` + counterfeit + legal tender + apt to deceive; no fact of the record says the agent knew. The good-faith flag is read only to carve the circulation verbs out (F-g5-04). No g5 record carries `Elemento subjetivo` (it is in `cp-dominio`), no fork and no PLAN convention presumes dolo. |
| IT-g5-100 | arts. 297; 301 § 1º | art. 301 § 1º only (specialty; arguable) | both: the 301 § 1º form is present and `crime de falsificação de documento público (art. 297)` is TRUE | E | No fork weighs art. 301 § 1º against arts. 297/298 (fork register searched for "301, § 1", "especialidade", "specialty"); the encoder applied specialty for the privileged good-faith forms (F-g5-04, F-g5-09) but not here. |
| IT-g5-113 | arts. 304; 301 § 1º | detenção, 3 meses a 2 anos, sem multa | `JUST` reclusão, 1 a 5 anos, multa cumulativa | E | `a pena cominada ao uso de documento falso (art. 304)` takes `a mais grave de todas as penas` over every falsity of arts. 297–302 the paper embodies; a certificate forged to obtain public office always also meets art. 298 (or 297), so 301 § 1º's pena is never the one borrowed. Same root as 100. The fixture records the certificate's issuer as not public (the case is silent); recorded as public, the answer would be art. 297's, still not 301 § 1º's. |
| IT-g5-115 | arts. 304; 297 | REFUSE: the Code does not say whether the forger who uses his own forgery answers for both (arguable) | TRUE AND TRUE: both crimes made out on the same agent | E | The encoding models absorption at the level of the crime predicate (Súmula 17's finding removes art. 297 and art. 304, F-sweep-c-12), so two TRUE predicates are its answer to the concurso question; no fork or finding covers the forger's own use (STJ: post factum impunível), where the brief's rule is REFUSE. (True on 2026-09-30; fork F-g5-32 followed on 2026-10-08. See "Second look" below.) |
| IT-g5-117 | art. 297 § 2º; art. 171 | TRUE on the text (arguable, Súmula 17) | FALSE once the judge's exhaustion finding is set | F | F-sweep-c-12, settled by STJ Súmula 17 (M-sweep-c-20), the alternative the case named. |
| IT-g5-123 | arts. 305; 298 p.ú. | REFUSE: the card's equiparação is "para fins do disposto no caput" of art. 298 only (arguable) | TRUE, private-document branch | E | `crime de supressão de documento (art. 305)` accepts `cartão de crédito ou débito` as a private document. F-g5-14 covers the card only before Lei 12.737/2012; no fork reads the equiparação's limit to art. 298's caput, in contrast with art. 297 § 2º's "para os efeitos penais" (F-g5-11). |
| IT-g5-150 | art. 311 §§ 1º, 2º I | TRUE: § 1º's third reaches the official of § 2º I (arguable) | FALSE: no cause | F | F-g5-20 takes "excetoInciso1" and records "todasAsFormas" (the case's reading) as double counting; the case's alternative named exactly this. |
| IT-g5-203 | art. 359-M-A; art. 2º p.ú. | TRUE: 359-M-A reaches Mário (8.1.2023 facts, final judgment) | REFUSED: application suspended since 9.5.2026 in the STF's 8-January executions | S | M-sweep-c-09, F-sweep-c-05. The fixture sets the STF-execution flag TRUE: the case is one of the STF's 8-January convictions, and the penalty is applied now, after 9.5.2026. |
| IT-g5-224 | arts. 359-T; 359-L | FALSE: 359-T does not shelter a violent attempt to abolish the constitutional order (arguable) | TRUE: `excluído pelo art. 359-T` once the demonstration circumstance is set | F | F-g5-29 (`achadoDoJuiz`, delegated to the fact): one fact-supplied flag removes every Título XII crime, including art. 359-L's own conduct. Worth the conductor's attention: nothing limits the flag. |
| IT-g5-226 | Título XII; arts. 1º–2º | REFUSE: the source prints "(Vigência)" with no date | FALSE: `o Título XII rege o fato` is FALSE on 15.10.2021; in force from 1.12.2021 | S | S-sweep-c-17 (Lei 14.197/2021, art. 5º). Stale by design; the phase-1 reply flagged it. |

## (E) findings, ranked

1. **Art. 301 § 1º's privilege can never apply (IT-g5-113, certain; IT-g5-100).**
   A certificate forged to obtain public office always also meets art. 297 or art. 298.
   Nothing makes the special provision displace the general one, and art. 304 borrows the heaviest penalty present, so both forger and user get reclusão (2–6 or 1–5 years) where the text prescribes detenção, 3 months to 2 years.
   The fix is a specialty fork (like F-g5-04 and F-g5-09) and an art. 304 that borrows the pena of the form the paper specifically is.
2. **No subjective element in g5's records (IT-g5-008, certain).**
   Art. 289 § 1º convicts someone who keeps counterfeit notes he received as genuine and never suspected.
   Art. 18 p.ú. requires dolo, and the encoding's own § 2º treats knowledge ("depois de conhecer a falsidade") as a fact the record carries.
   Only art. 289 § 1º was tested; the same shape probably holds for every possession verb in the range (art. 291 "possuir ou guardar", art. 293 § 1º I "usa, guarda, possui ou detém", art. 294, art. 311 § 2º II). That is an inference from the rules' shape, not a measurement.
3. **Use of a forgery by the forger himself (IT-g5-115).** Both crimes stand, with no fork, although the encoding treats absorption at the predicate level elsewhere (Súmula 17). (As of 2026-09-30; see "Second look" below.)
4. **A credit card under art. 305 (IT-g5-123).** Treated as a private document although art. 298 p.ú. limits the equiparação to art. 298's caput; no fork. Low stakes.

## Not expressible (9)

| id | articles | reason |
| --- | --- | --- |
| IT-g5-211 | 359-M-A, 359-M-B, art. 68 | No rule composes the 359-M-B reduction with the 359-M-A concurso; the concurso rule takes the quantities the judge already fixed for each crime, which fits the expected order but does not state it. |
| IT-g5-214 | 359-O | Vetoed; carried only as the string "(VETADO)", so no rule answers "does it define an offence". |
| IT-g5-220 | Título XII, Cap. V | Vetoed; carried only as a string. |
| IT-g5-223 | 359-T, art. 163 | 359-T's rule reads only Título XII facts, and g3's `Fato de dano` has no field for a demonstration; the structure agrees with the expected FALSE, but no directive can state it. |
| IT-g5-228–230 | art. 360 | Inert string; no rule for the revocation or the ressalvas. |
| IT-g5-231–232 | art. 361 | Inert string; no date value or gate for 1.1.1942. |

## Expressed, but weaker than they look

- **IT-g5-127** (art. 306 p.ú.: the judge chooses the species) is a refuse case written **without** `#ASSERT REFUSED`: no rule picks a species, so nothing can refuse. It asserts instead that g1b's art. 59, I options for art. 306 p.ú. are exactly reclusão with multa and detenção with multa, which is the encoding's way of leaving the choice to the judge. If refuse cases must be `#ASSERT REFUSED`, reclassify it as not expressible.
- **IT-g5-169** (art. 7º, I, b): g1a's record takes the art. 7º class as an input, so the fixture supplies "contra a fé pública"; the directive checks only that inciso I is unconditional whatever happened abroad.
- **IT-g5-201, 205, 210** pass partly by construction: `Crime do Capítulo II do Título XII` has no member for art. 359-R (201); "mandatory" shows only as the cause applying, with no judge's option (205); the violence's penalty is never computed here (210).
- Agreement on exposed material is not evidence (EXPOSURE.md): IT-g5-194 and IT-g5-226, and the "dobro is +1/1" convention behind IT-g5-172.

## Agreement worth recording

On cases marked arguable, the encoding took the case's reading, independently of any exposure: IT-g5-018 (art. 289 § 4º takes § 3º's 3–15 years, F-g5-02), IT-g5-076 (art. 297 § 1º reaches § 3º), IT-g5-095 (art. 301 § 2º's lucro fine reaches the caput), IT-g5-116 (art. 304 does not carry art. 297 § 1º's increase, F-g5-13), IT-g5-199 (under 359-M-A, 12 + 4 years gives 14 to 16, art. 70 p.ú.'s cap applied).
IT-g5-088 (the declaração de hipossuficiência) agrees on the text alone: the encoding has no fact for "subject to verification", so the STJ line is not tested.

## Observations that are not failures

- Art. 311 § 1º reads only the act's circumstance ("no exercício da função pública"), never the agent's status.
- Art. 311-A's pena rule returns the caput's penalty even where no crime is made out; arts. 306, 309 and 311 return NOTHING. The directives conjoin the pena with the crime predicate.
- Arts. 307, 308 and 310 export no case-level pena rule (PLAN § 5, item 5), only a `limites` rule that answers whether or not the crime is made out.

## How it was done

Four subagents wrote one slice each (arts. 289–295; 296–305; 306–311-A; Título XII and 360–361), each running `check.sh` on its own files.
The two files with directives but no genuine failure (`cp-ind-g5-papeis-publicos.l4`, `cp-ind-g5-fraudes-em-certames.l4`) each got one planted false assertion, which failed, and was then removed and the file re-run.
ta-g5 re-read the rules behind every (E) claim, searched `registers/fork-register.json` for a fork covering each, moved 21 explanatory comments so that each `-- IT-g5-NNN:` line sits directly above its directive (non-comment lines checked identical before and after), and re-ran `check.sh` over all seven files for the output above.

## Re-run after fix round (ta-g5 rerun, 2026-10-09)

The encoders' fix round (F-g5-31 to F-g5-34) made knowledge fields required, and F-g5-29 now makes art. 359-T REFUSE on violent conduct.
No expected value was changed.
Only fixtures were: 31 sites, all to supply a new knowledge field (2 builders gained a parameter).
`cases/ta-g5.json` was not edited.

### check.sh before and after

"Before" is the files as left by the 2026-09-30 pass, run against today's encoding.

| module | before (errors / satisfied / failed / refused / asserts) | after |
| --- | --- | --- |
| `cp-ind-g5-disposicoes-finais.l4` | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |
| `cp-ind-g5-estado-democratico.l4` | 4 / 48 / 4 / 2 / 54 | 1 / 51 / 1 / 2 / 54 |
| `cp-ind-g5-falsidade-documental.l4` | 5 / 68 / 5 / 0 / 73 | 2 / 71 / 2 / 0 / 73 |
| `cp-ind-g5-fraudes-em-certames.l4` | 7 / 3 / 7 / 0 / 10 | 0 / 10 / 0 / 0 / 10 |
| `cp-ind-g5-moeda-falsa.l4` | 1 / 0 / 0 / 0 / 34, UNACCOUNTED 34 (does not typecheck) | 1 / 33 / 1 / 0 / 34 |
| `cp-ind-g5-outras-falsidades.l4` | 1 / 0 / 0 / 0 / 34, UNACCOUNTED 34 (does not typecheck) | 1 / 33 / 1 / 0 / 34 |
| `cp-ind-g5-papeis-publicos.l4` | 6 / 12 / 6 / 0 / 18 | 0 / 18 / 0 / 0 / 18 |
| TOTAL | 24 / 131 / 22 / 2 / 223 (68 asserts unaccounted) | 5 / 216 / 5 / 2 / 223, UNACCOUNTED 0 |

Agreeing: 131 of 223 before (68 produced no verdict), 216 of 223 after.
On 2026-09-30 it was 212 of 223.

### Fixtures changed (31 sites)

| kind | n | where |
| --- | --- | --- |
| a new required Boolean field in a record builder | 2 builders, 6 call sites | moeda-falsa (art. 291 `o agente sabia que o objeto era destinado...`; both call sites TRUE), outras-falsidades (art. 306 `o agente sabia que a marca ou sinal era falsificado`; cases 124, 125, 126, 128 all TRUE) |
| a knowledge member added to a circumstance list | 25 | papeis-publicos 038, 039, 041, 045, 048, 051; fraudes-em-certames 158, 159, 160, 162, 163, 164, 165, 166, 167 (9); moeda-falsa 006, 012; outras-falsidades 149, 150, 151; falsidade-documental 054, 107, 114; estado-democratico: the shared `ind espionagem` list (cases 180, 183) and case 186 |

Rule 2: every knowledge field was set to "knowing", which keeps each case's original facts.
The case says so outright in 006, 012, 038, 045, 054, 114 and 125; every other site is a case silent on knowledge (forgers, leakers, vendors, Zacarias, Abílio), set to knowing and logged here.
No field was set to FALSE and no "ignorava" member was used: the error and ignorance cases (008, 011, 047, 153, 185) needed no knowledge member and were not touched.
159 and 167 (expected NOT) got the member too, which is consistent with their facts; they pass for the reasons they passed before.

### Positive control

The two builders went from a missing-input error to typechecking, and the circumstance-list edits turned the failed assertions of those modules green (totals in the table above); 159 and 167 were already passing.
Explicitly: in a scratch copy of outras-falsidades, case 125 (Estela, who used a forged mark "sabendo") with the new field flipped to FALSE failed IT-g5-125, besides the existing IT-g5-150; the scratch file was deleted.

### Disagreements (7: 5 failed, 2 refused)

| id | expected | got | one line |
| --- | --- | --- | --- |
| IT-g5-005 | TRUE | FALSE | unchanged: F-sweep-c-11, Súmula 73 grossness finding |
| IT-g5-115 | REFUSE | TRUE and TRUE | unchanged: no REFUSE for the forger who uses his own forgery; exposed to g5 (2026-10-08) and still disagrees, so NOT fixed. **This row's "got" was out of date when written**; see "Second look" below |
| IT-g5-117 | TRUE | FALSE | unchanged: F-sweep-c-12, Súmula 17 |
| IT-g5-150 | TRUE | FALSE | unchanged: F-g5-20 |
| IT-g5-203 | TRUE | REFUSED | unchanged: M-sweep-c-09 / F-sweep-c-05 |
| IT-g5-224 | FALSE | REFUSED | CHANGED: was TRUE (the exclusion applied). Now 359-L's crime predicate REFUSES on violent conduct plus the finding (F-g5-29, fork text printed in the diagnostic). The expected FALSE is not met; the case is marked arguable. For the conductor. |
| IT-g5-226 | REFUSE | FALSE | unchanged: S-sweep-c-17, vigência from 1.12.2021 |

### Now agreeing, with how to score them

| id | before | now | score |
| --- | --- | --- | --- |
| IT-g5-008 | TRUE (no knowledge field) | FALSE, agrees with expected | fixed (relayed to g5, 2026-10-08): the knowledge member F-g5-31 to 34 added |
| IT-g5-100 | both crimes | agrees | fixed (relayed to g5) |
| IT-g5-113 | wrong pena | agrees | fixed (relayed to g5) |
| IT-g5-123 | TRUE | agrees (REFUSED) | fixed (relayed to g5) |

The ADI refusal message did not appear in any cp-ind-g5 expectation: no assertion pins its wording, and no output changed in a way that a g5 assertion reads.
The art. 359-T change touched exactly one: IT-g5-224, above.

### Odd

The first `check.sh` run took about 10 minutes under load.
`git status` shows other edits in the tree (`notes/g3.md`, `registers/parts/g3.forks.json`, `cp-g*` files) that are not mine.

### Conductor triage of the 2026-10-09 re-run (IT-g5-224)

IT-g5-224 (violent invasion of the Congress seat; does art. 359-T exclude art. 359-L?) expected FALSE (the crime stands) and used to agree.
It now gets REFUSED, by the conductor's ruling on F-g5-29 (2026-10-08): with the finding plus violence or grave threat on the record, the encoding names both readings and does not pick one.
Class F (recorded fork), not E: the test author marked the case "arguable" and its `alternative` field states the opposite reading; the encoding now records that disagreement instead of resolving it.
Expected value unchanged; this is a deliberate loss of an agreement in exchange for an honest refusal.

## Second look, 2026-10-11

Only IT-g5-115.
It was told to g5 on 2026-10-08 (EXPOSURE.md), so its agreement is the fix working, not independent evidence.
No expected value changed and `cases/ta-g5.json` was not edited.

**What the 2026-10-09 re-run row got wrong.**
It reported the encoding as "TRUE and TRUE" with "no fork or finding" on the forger's own use.
Fork F-g5-32 had landed in a62b67d7 on 2026-10-08 15:33 (+0800), before that re-run (b887f7b6, 2026-10-09 01:03), and the exported art. 304 rule already left the forger's use out.
The assertion was red for a different reason: the fixture `o uso 115` gave `, com:` EMPTY, so the user had neither the knowledge finding (F-g5-34) nor the authorship finding, `uso do art. 304` was FALSE, and so was the crime.
Measured on 2026-10-11 with an `#EVAL` of the old fixture in a scratch copy: `uso do art. 304` FALSE and `crime de uso de documento falso (art. 304)` FALSE.
The re-run's "got" column repeated the 2026-09-30 triage text and was not re-measured.

| id | expected | at the re-run, as reported | measured before this look | now | result |
| --- | --- | --- | --- | --- | --- |
| IT-g5-115 | REFUSE | TRUE and TRUE | art. 297 TRUE, art. 304 FALSE (post factum taken by F-g5-32; the fixture lacked the user's authorship, so it was FALSE on knowledge first) | art. 297 TRUE, art. 304 REFUSED by name | agrees; scored **fixed**, not an independent agreement |

**Decision: a refusal, in the existing fork F-g5-32 (no new fork).**
The Code does not say whether the forger who uses his own forgery answers for the use as well.
The case's own `alternative` makes taking the post factum line conditional on "a fork citing the ruling".
No ruling is in the sweep register (the nearest entry, M-sweep-c-20, is Súmula 17 and Tema 933 on a falsity spent in estelionato or descaminho) or in the source, none was retrieved, and this look asserts nothing about what the STJ or STF hold on the question.
So F-g5-32, which already records exactly this question and its two readings, changed from `resolved` (post factum taken) to `open`, with a third entry `recusaEnquantoAberto` as `taken`, as at F-g2b-01.
`crime de uso de documento falso (art. 304)` now refuses only when every other element is made out and the user is also the author or a participant of the forgery; it answers FALSE where the use was not begun or made, or the judge found the falsity spent (Súmula 17), and TRUE for a user who did not forge.
No new field was needed: `o agente do uso é autor ou partícipe da falsificação do papel` already existed.

**Fixture changed (one site).**
`o uso 115` in `cp-ind-g5-falsidade-documental.l4` now carries `(LIST `o agente do uso é autor ou partícipe da falsificação do papel`)` where `, com:` was EMPTY.
The case says Túlio forged the licence and then used it.

**check.sh, before and after** (`L4=~/.claude/br-penal-toolchain/l4-1008`):

| module | before | after |
| --- | --- | --- |
| cp-ind-g5-falsidade-documental | 2 / 71 / 2 / 0 / 73 | 1 / 72 / 1 / 0 / 73 |
| cp-g5-falsidade-documental-testes (the encoder's) | 0 / 144 / 0 / 0 / 144 | 0 / 148 / 0 / 0 / 148 |

The one failure left in the independent module is IT-g5-117 (Súmula 17, F-sweep-c-12), unchanged.
The other six cp-ind-g5 modules do not import the changed module and were not re-run, so the cp-ind-g5 totals are 4 / 217 / 4 / 2 / 223 (the 2026-10-09 re-run had 5 / 216 / 5 / 2 / 223).
`cp-codigo-penal.l4`, which imports every module, typechecks with 0 errors.

**Positive control** (scratch copies of the tree; the two reversions reproduce the previous behaviour):
reverting the rule to the old conjunction with `NOT absorvido` (post factum) turned the two `#ASSERT REFUSED` in the tests module red and IT-g5-115 red (the independent module went 1 -> 2 failed); counting the forger's use (reading `ambos`) did the same; removing the first branch's guard turned five older assertions red and the three new non-refusal assertions to refused.
