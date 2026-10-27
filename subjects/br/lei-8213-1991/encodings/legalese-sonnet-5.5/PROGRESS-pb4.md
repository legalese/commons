# PROGRESS (pb4, arts. 81 to 124-G, src:1106-1539)

Last updated 2026-10-24. Status: layer 1, layer 2, tests and NOTES.md are written and check clean; the review pass is the last step.

## Files written (all in this folder)
- Layer 1 (nouns): `pb4-tipos.l4`
- Layer 1 (rules, in the order of the Law): `pb4-auxilio-acidente.l4` (art. 86), `pb4-servicos.l4` (arts. 88-93), `pb4-contagem-reciproca.l4` (arts. 94-99), `pb4-exame-e-prazos.l4` (arts. 100-108), `pb4-pagamento.l4` (arts. 109-117-A), `pb4-acidente-e-acumulacao.l4` (arts. 118-124), `pb4-administracao.l4` (arts. 124-A to 124-G)
- Tests of layer 1: `pb4-tests-auxilio-acidente.l4`, `pb4-tests-servicos.l4`, `pb4-tests-contagem-reciproca.l4`, `pb4-tests-exame-e-prazos.l4`, `pb4-tests-pagamento.l4`, `pb4-tests-acidente-e-acumulacao.l4`, `pb4-tests-administracao.l4`
- Layer 2: `pb4-seat.l4` (100 questions, 13 groups), `pb4-cases-seat.l4`
- `NOTES.md` (all required headings), this file

## Sections done
All 54 articles of the range: 81 to 87 (Subseções X to XII: wholly revoked, rows only; art. 86 encoded), 88 to 93, 94 to 99, 100 to 124-G.

## Sections in progress / next
Nothing in progress. If the folder is regenerated: the seat and cases came from a generator that is not kept, so edit the `.l4` files directly.

## Decisions taken (with the text that licenses each)
See NOTES.md, Fork register F-1 to F-23. The ones that change a result: F-7 (art. 96 IV formula), F-9 (art. 101 s1), F-15 (art. 115 II), F-16 (art. 115 s2), F-18 (art. 124 p.u.), F-19 (art. 124-B III v s5).

## Toolchain facts found
`NOT (x) OR y` on one line is read as NOT ((x) OR y); `JUST 2%` is (JUST 2)%; EXPONENT is floating point; multi-line calls inside brackets need WHERE. Listed under "What the stable binary does not accept".
