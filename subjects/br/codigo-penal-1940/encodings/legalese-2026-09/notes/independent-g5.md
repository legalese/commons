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
| IT-g5-115 | arts. 304; 297 | REFUSE: the Code does not say whether the forger who uses his own forgery answers for both (arguable) | TRUE AND TRUE: both crimes made out on the same agent | E | The encoding models absorption at the level of the crime predicate (Súmula 17's finding removes art. 297 and art. 304, F-sweep-c-12), so two TRUE predicates are its answer to the concurso question; no fork or finding covers the forger's own use (STJ: post factum impunível), where the brief's rule is REFUSE. |
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
3. **Use of a forgery by the forger himself (IT-g5-115).** Both crimes stand, with no fork, although the encoding treats absorption at the predicate level elsewhere (Súmula 17).
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
