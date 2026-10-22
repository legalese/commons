# PROGRESS: br4, Capítulos XII a XIV of the Lei das Sociedades por Ações (arts. 138 to 174), lines 1233-1554

Written by the piece agent `br4` on 2026-10-22.

## State

- Finished: layer 1 (eight modules and their tests), layer 2 (`br4-seat.l4` and `br4-cases-seat.l4`), NOTES.md.
- Last full gate, run after the final edit: `L4=<stable 1.6.98 l4> L4_TARGET=unstable ./check.sh` printed `TOTAL (19 modules) 0 1443 0 0`: 0 errors, 1443 satisfied, 0 failed, 0 refused.
  The 1443 are 774 in the eight layer-1 test files and 669 in `br4-cases-seat.l4`.
- `srcrefs.py check --refs` on the eight layer-1 modules: 0 problems each.
- Whole range read: 38 live article openers in 1233-1554 (arts. 138 to 174, plus 165-A); 40 whole lines in the range are struck and are skipped, not encoded.

## Done

- br4-administracao (arts. 138-139) + br4-tests-administracao: 31 assertions satisfied.
- br4-conselho-de-administracao (arts. 140-142) + br4-tests-conselho-de-administracao: 101 assertions satisfied.
- br4-diretoria (arts. 143-144) + br4-tests-diretoria: 31 assertions satisfied.
- br4-administradores (arts. 145-152) + br4-tests-administradores: 122 assertions satisfied.
- br4-deveres (arts. 153-160) + br4-tests-deveres: 158 assertions satisfied.
- br4-conselho-fiscal (arts. 161-165-A) + br4-tests-conselho-fiscal: 139 assertions satisfied.
- br4-aumento-de-capital (arts. 166-172) + br4-tests-aumento-de-capital: 155 assertions satisfied.
- br4-reducao-de-capital (arts. 173-174) + br4-tests-reducao-de-capital: 37 assertions satisfied.
- br4-seat.l4: 215 exported questions in eight groups (7, 25, 7, 33, 47, 42, 45, 9); br4-cases-seat.l4: 669 assertions satisfied.
- Last change before the final gate: art. 161, §§ 5º e 6º ("poderão ser reeleitos") was made a constant TRUE, the reading fork F7(b) takes at arts. 140, III and 143, III, where an earlier draft had let an estatuto ban stand.

## Decisions taken

See NOTES.md `## Fork register` (F1 to F18, each with the provision that licenses it).

## Files written

br4-administracao.l4, br4-tests-administracao.l4, br4-conselho-de-administracao.l4, br4-tests-conselho-de-administracao.l4, br4-diretoria.l4, br4-tests-diretoria.l4, br4-administradores.l4, br4-tests-administradores.l4, br4-deveres.l4, br4-tests-deveres.l4, br4-conselho-fiscal.l4, br4-tests-conselho-fiscal.l4, br4-aumento-de-capital.l4, br4-tests-aumento-de-capital.l4, br4-reducao-de-capital.l4, br4-tests-reducao-de-capital.l4, br4-seat.l4, br4-cases-seat.l4, NOTES.md, PROGRESS.md.
