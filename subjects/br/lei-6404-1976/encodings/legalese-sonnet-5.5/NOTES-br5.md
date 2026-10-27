# NOTES: piece br5 of the Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976), Capítulos XV e XVI

Written by the piece agent `br5` on 2026-10-22 for lines 1555-1957 of `lei-6404-1976.pt.txt` (Arts. 175 to 205).

## Seat

The seat is the one the brief fixes: a shareholder (acionista), including a minority shareholder, of a company (sociedade anônima), asking what the Law gives them, what it requires of them, and what the company, its managers and its controlling shareholder may do in relation to them.
`br5-seat.l4` asks 76 questions, grouped under five `§` headings in the text's order: Arts. 175 to 177, 178 to 188, 189 to 192, 193 to 200 and 201 to 205.
`br5-cases-seat.l4` holds 186 assertions, and a script confirmed that every question has at least one.
Every input is a plain fact the shareholder can state, with a Portuguese `@desc` worded to them, and every `@export` text carries its citation.
The records and enumerations that layer 1 expects are built in each question's `WHERE`; the seat restates no rule.
The canonical facts that several pieces ask are asked under their canonical names and with the keel's wording: `o tipo da companhia`, `a espécie das ações`, `a forma das ações`, `a quantidade de ações do acionista`, `as ações do acionista estão integralizadas` and `as ações do acionista têm valor nominal` (compared by script with the table in `KEEL-NOTES.md`).
The canonical facts about the company's organs and capital (`a companhia tem conselho de administração`, `a companhia tem conselho fiscal permanente`, `a companhia tem capital autorizado`, `a companhia é de economia mista`) are not asked, because no provision of this range turns on them.
Art. 202, § 4º speaks of a conselho fiscal "em funcionamento", which Art. 161 lets be permanent or installed only in the exercícios when shareholders ask (I read the first line of Art. 161, in piece br4's range), so that input is its own (`o conselho fiscal está em funcionamento`) and not the canonical "permanent" fact.
Where the text gives the shareholder a claim, privilege, power or immunity, the questions take the other side's facts as plain inputs; where it puts a duty or a liability on the shareholder the paired question is asked (Art. 201, § 2º, "Sou obrigado a restituir o dividendo que recebi", and Art. 202, § 3º, "A assembleia pode reduzir o dividendo ... se eu me opuser").
No question names the controlling shareholder: no provision of Arts. 175 to 205 addresses the acionista controlador, and the only mention of a majority or a minority is Art. 202, § 1º (src:1937), which forbids estatuto criteria that subject minority shareholders to the arbitrariness of the majority.
There is no seat for an official: what the text asks of the CVM (Art. 176, § 7º; Art. 177, § 5º; Art. 184-A) is in layer 1 only, and the CVM's act enters as a plain input where a rule depends on it (for example `a CVM disciplinou de forma diversa o registro da destinação dos lucros`).
The seat is coarser than layer 1 in three places, on purpose, because a shareholder cannot list eighteen items of a note.
- The notes to the statements (Art. 176, § 5º) and the statement of accumulated profits (Art. 186) ask the items that always arise one by one, and ask a single question for the items that arise only if the company had the thing ("for each of them that exists, does the note give it?"), answering for all of them at once.
  In the notes, the relevance of an investment (Art. 247, parágrafo único) is therefore not asked: each conditional item is treated as existing.
- The statement of the result (Art. 187) is asked inciso by inciso, not item by item.
- Art. 205, § 3º takes the date the meeting fixed only if the meeting fixed one; a shareholder whose meeting fixed none is told to repeat the declaration date, which the rule does not read in that case (a case asserts it).
26 of the 116 layer-1 rules are not reached by any seat question, directly or through another rule that a question calls.
They tell the preparer how to classify, present or value items in the statements, or concern holders of partes beneficiárias or the CVM, and a shareholder would read their result and not ask for it.
They are cited as: art. 176, § 3º; art. 176, § 4º; art. 177, § 2º; art. 177, § 5º; art. 178; art. 178, § 1º; art. 178, § 1º, inciso II; art. 178, § 2º, inciso III; art. 178, § 3º; art. 182; art. 182, § 1º; art. 182, § 3º; art. 182, § 4º; art. 182, § 5º; art. 183, inciso III; art. 183, inciso VIII; art. 183, § 1º; art. 183, § 1º, alínea d; art. 183, § 2º; art. 186, § 1º; art. 186, § 2º; art. 188, inciso II; art. 200, parágrafo único.
All of them are in layer 1 and in the coverage table; the brief says the seat never decides what layer 1 leaves out, and a reviewer who wants a question for any of them can add one without touching layer 1.

## Jural relations

Where the text is passive and names no holder, the cell says so and no holder is invented.
"Kind" gives the Hohfeldian pair in the order holder / bearer; "duty only" means the text states the duty and names nobody who may demand it.
Layer 1 states each relation once, as a rule; the seat asks it from the shareholder's side.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| Art. 175, caput | none | none | none (the length and end date of the exercício) | `o exercício social tem a duração que a lei estabelece (art. 175)`, `o exercício social está de acordo com o art. 175` |
| Art. 175, parágrafo único | the company, at its constitution and when it alters its estatuto | no one named | privilege / no-right (a different duration is allowed) | `a duração do exercício social é permitida (art. 175, parágrafo único)` |
| Art. 176, caput | not named in the text | the diretoria | duty only (to have the statements prepared, from the books, and clear) | `a diretoria fez elaborar as demonstrações financeiras que a lei exige (art. 176)`, `a demonstração financeira é exigida da companhia (art. 176)` |
| Art. 176, § 1º | not named in the text | not named (passive: "serão publicadas") | duty only (to publish with the previous exercício's figures) | `as demonstrações foram publicadas com os valores do exercício anterior (art. 176, § 1º)` |
| Art. 176, § 2º | the company | no one named | privilege / no-right (to group accounts and aggregate small balances within limits) | `a agregação de pequenos saldos é permitida (art. 176, § 2º)` |
| Art. 176, §§ 3º and 4º | not named in the text | not named (passive) | duty only | `o registro da destinação dos lucros nas demonstrações está de acordo com a lei (art. 176, § 3º)`, `as demonstrações foram complementadas como a lei exige (art. 176, § 4º)` |
| Art. 176, § 5º | not named in the text | not named (passive: "devem") | duty only (the notes) | `as notas explicativas trazem tudo o que a lei exige (art. 176, § 5º)` |
| Art. 176, § 6º | a closed company with equity under R$ 2.000.000,00 on the balance-sheet date | no one named | privilege / no-right (not obliged to prepare and publish the cash-flow statement) | `a demonstração financeira é exigida da companhia (art. 176)` |
| Art. 176, § 7º (with § 3º) | the CVM | the companies concerned | power / liability (may regulate the record of the destination of profits differently) | `o registro da destinação dos lucros nas demonstrações está de acordo com a lei (art. 176, § 3º)`, which takes the CVM's act as an input |
| Art. 177, caput and §§ 1º, 2º | not named in the text | not named (passive) | duty only (the books; a note on a change of method; tax-law provisions only in auxiliary records) | `a escrituração da companhia está de acordo com a lei (art. 177)`, `a modificação de método contábil foi indicada em nota como a lei exige (art. 177, § 1º)`, `a disposição da lei tributária ou de legislação especial foi observada como a lei exige (art. 177, § 2º)` |
| Art. 177, § 3º | not named in the text | the open company | duty only (to observe the CVM's norms and be audited by independent auditors registered with the CVM) | `as demonstrações da companhia aberta estão de acordo com o art. 177, § 3º` |
| Art. 177, § 4º | not named in the text | the administrators and legally qualified accountants | duty only (to sign) | `as demonstrações financeiras foram assinadas como a lei exige (art. 177, § 4º)` |
| Art. 177, § 5º | not named in the text | the CVM | disability (its norms must follow the international standards) | `a norma da CVM sobre demonstrações financeiras está de acordo com o art. 177, § 5º` |
| Art. 177, § 6º | a closed company | no one named | privilege / no-right (may opt for the CVM's norms for open companies) | `a companhia pode optar por observar as normas da CVM para companhias abertas (art. 177, § 6º)` |
| Arts. 178, §§ 1º and 2º (the groups); 179 and 180 (the classes); 182, §§ 1º to 4º (what counts as a reserve or adjustment); 183, § 1º (fair value); 186, § 1º (an adjustment); 187, § 1º (the result) | none | none | none (definitions) | `o grupo do ativo em que a conta é classificada (art. 179)`, `o grupo do passivo exigível em que a obrigação é classificada (art. 180)`, `a verba é reserva de capital (art. 182, § 1º)`, `o resultado do exercício em reais (art. 187, § 1º)` and the like |
| Arts. 178 (the duty to classify and arrange), 182 (capital account, treasury shares), 183, caput and incisos I to VIII, § 2º (valuation, diminution), 184, incisos I to III, 186, 187, 188 (contents of the statements) | not named in the text | not named (passive: "serão classificadas", "serão avaliados", "discriminará", "indicarão"); the preparers | duty only | the corresponding rules of `br5-balanco.l4` and `br5-demonstracoes-contas.l4` |
| Art. 183, § 3º | not named in the text | the company | duty only (to analyse periodically whether the values can be recovered) | `a companhia cumpriu o dever de analisar a recuperação dos valores do imobilizado e do intangível (art. 183, § 3º)` |
| Art. 183, § 4º | the company | no one named | privilege / no-right (may value fungible stock at market value when that is the accepted custom) | `o estoque pode ser avaliado pelo valor de mercado (art. 183, § 4º)` |
| Art. 184-A | the CVM | the companies concerned | power / liability (special norms of valuation and accounting); inert, nothing encoded | none |
| Art. 186, § 2º | not named in the text | not named | duty (to show the dividend per share) and privilege (to include the statement in that of changes in equity) | `a demonstração de lucros ou prejuízos acumulados indica o dividendo por ação (art. 186, § 2º)`, `a demonstração de lucros ou prejuízos acumulados pode ser incluída na das mutações do patrimônio líquido (art. 186, § 2º)` |
| Art. 189, caput | none | none | none (order of deductions) | `o resultado do exercício depois das deduções em reais (art. 189)` |
| Art. 189, parágrafo único | not named in the text | the company | duty only (the loss is absorbed "obrigatoriamente", in order) | `a absorção do prejuízo do exercício (art. 189, parágrafo único)` |
| Art. 190 | none (the entitlements are created by the estatuto, which the Law does not itself state) | none | none (computation of the participations) | `as participações estatutárias dos empregados, dos administradores e das partes beneficiárias (art. 190)` |
| Art. 190, parágrafo único | as Art. 201 | as Art. 201 | the relations of Art. 201, §§ 1º and 2º, for the administrators' and beneficiary parts' participations; none for the employees | `os parágrafos do art. 201 se aplicam ao pagamento (art. 190, parágrafo único)` |
| Art. 191 | none | none | none (definition of net profit) | `o lucro líquido do exercício em reais (art. 191)` |
| Art. 192 | not named (the ordinary general meeting is the addressee) | the organs of administration | duty only (to present the proposal on the destination of the net profit) | `a proposta de destinação do lucro líquido foi apresentada como a lei exige (art. 192)` |
| Art. 193, caput | not named in the text | the company | duty only (5% to the legal reserve, up to 20% of the capital) | `o menor valor que a companhia deve aplicar na reserva legal no exercício em reais (art. 193)` |
| Art. 193, § 1º | the company | no one named | privilege / no-right (may leave the reserve unformed above 30%) | `a companhia pode deixar de constituir a reserva legal no exercício (art. 193, § 1º)` |
| Art. 193, § 2º | not named (whoever the integrity of the capital protects) | the company | immunity / disability (the reserve only offsets losses or raises the capital) | `o uso da reserva legal é permitido (art. 193, § 2º)` |
| Art. 194 | the company, by its estatuto | the shareholders (their share of the profit is affected; not named) | power / liability (to create reserves on three conditions) | `o estatuto pode criar a reserva (art. 194)` |
| Art. 195, caput | the general meeting, on the administration's proposal | the shareholders (not named) | power / liability (contingency reserve) | `a assembleia-geral pode destinar parte do lucro líquido à reserva para contingências (art. 195)` |
| Art. 195, §§ 1º and 2º | not named in the text | the organs of administration (the proposal); the company (the reversal) | duty only | `a proposta da reserva para contingências indica a causa e justifica a constituição (art. 195, § 1º)`, `a reserva para contingências deve ser revertida no exercício (art. 195, § 2º)` |
| Art. 195-A | the general meeting, on the administration's proposal | the shareholders (not named) | power / liability (tax-incentive reserve, which may be left out of the dividend base) | `a assembleia-geral pode destinar o valor à reserva de incentivos fiscais (art. 195-A)`, `o valor que pode ser excluído da base do dividendo obrigatório em reais (art. 195-A)` |
| Art. 196, caput and §§ 1º, 2º | the general meeting, on the administration's proposal | the shareholders (not named) | power / liability (to retain profit under a capital budget); the limits of the budget are duties of the administration | `a assembleia-geral pode reter parcela do lucro líquido (art. 196)`, `o orçamento de capital está de acordo com a lei (art. 196, § 1º)`, `o orçamento de capital pode ser aprovado nessa assembleia (art. 196, § 2º)`, `o orçamento de capital pode ser revisado anualmente (art. 196, § 2º)` |
| Art. 197, caput | the general meeting, on the administration's proposal | the shareholders (not named) | power / liability (reserve of profits to be realized) | `a assembleia-geral pode destinar o valor à reserva de lucros a realizar (art. 197)` |
| Art. 197, § 1º | none | none | none (definition of the realized part) | `a parcela realizada do lucro líquido em reais (art. 197, § 1º)` |
| Art. 197, § 2º | not named in the text | the company | disability (the reserve only pays the mandatory dividend) | `o uso da reserva de lucros a realizar é permitido (art. 197, § 2º)` |
| Art. 198 | the shareholders entitled to the mandatory dividend (implied: the text speaks of the dividend, not of who is protected) | the general meeting | immunity / disability (statutory reserves and retention may not be approved to the prejudice of the dividend) | `a destinação às reservas estatutárias e a retenção respeitam o dividendo obrigatório (art. 198)` |
| Art. 199 | not named in the text | the general meeting (and the company, which may not hold more) | duty (to resolve on the excess once the cap is reached) and disability (the cap) | `a assembleia-geral deve deliberar sobre a aplicação do excesso (art. 199)`, `a aplicação do excesso das reservas de lucros é permitida (art. 199)` |
| Art. 200, caput | not named in the text | the company | disability (capital reserves only for the listed uses) | `o uso da reserva de capital é permitido (art. 200)` |
| Art. 200, parágrafo único | the company | no one named | privilege / no-right | `a reserva da venda de partes beneficiárias pode ser destinada ao resgate delas (art. 200, parágrafo único)` |
| Art. 201, caput | not named in the text | the company | disability (dividends only from the listed sources) | `a fonte do dividendo é permitida (art. 201)` |
| Art. 201, § 1º | the company (its cash) | the administrators and the members of the conselho fiscal, jointly | claim / duty (to restore what was distributed against the Law); the criminal action is reserved by the text and not encoded | `os administradores e fiscais respondem solidariamente pela reposição do dividendo (art. 201, § 1º)`, `a importância a repor à caixa social em reais (art. 201, § 1º)` |
| Art. 201, § 2º | the shareholder who received in good faith | the company | immunity / disability (it cannot require the return); the company's claim against a recipient in bad faith is implied, not stated | `o acionista é obrigado a restituir o dividendo recebido (art. 201, § 2º)` |
| Art. 202, caput | the shareholders ("Os acionistas têm direito") | the company (implied) | claim / duty (the mandatory dividend) | `o dividendo obrigatório em reais (art. 202)`, `o dividendo obrigatório é devido por inteiro no exercício (art. 202)` |
| Art. 202, inciso I | none | none | none (the base of the mandatory dividend) | `o lucro líquido ajustado para o dividendo obrigatório em reais (art. 202, inciso I)`, `o dividendo obrigatório se o estatuto for omisso em reais (art. 202, inciso I)` |
| Art. 202, inciso II | the company | the shareholders | power / liability (may limit the payment to the realized profit, the difference going to the reserve of Art. 197) | `o dividendo a pagar quando se limita ao lucro realizado (art. 202, inciso II)` |
| Art. 202, inciso III | the shareholders (implied) | the company | claim / duty (realized profits are added to the first dividend declared after the realization) | `o valor a acrescer ao primeiro dividendo declarado depois da realização em reais (art. 202, inciso III)` |
| Art. 202, § 1º | the company, by its estatuto; the minority shareholders (named) are protected | the shareholders; the estatuto | power / liability, limited by an immunity / disability (no criterion may subject the minority to arbitrariness) | `o critério do estatuto para o dividendo é válido (art. 202, § 1º)` |
| Art. 202, § 2º | the shareholders (not named) | the general meeting | immunity / disability (the floor of 25% of the adjusted profit) | `o dividendo fixado ao alterar o estatuto omisso respeita o mínimo (art. 202, § 2º)` |
| Art. 202, § 3º | the general meeting (to reduce the dividend or retain all the profit); each shareholder present (by opposing) | the shareholders; the general meeting | power / liability, and immunity / disability once any shareholder present opposes | `a assembleia-geral pode deliberar dividendo inferior ao obrigatório ou reter todo o lucro (art. 202, § 3º)` |
| Art. 202, § 4º, first limb | the organs of administration | the shareholders | power / liability (the dividend ceases to be mandatory when they inform the ordinary meeting that it is incompatible with the financial situation) | `o dividendo obrigatório é devido no exercício (art. 202, § 4º)` |
| Art. 202, § 4º, opinion | not named (the meeting is the addressee) | the conselho fiscal, if in operation | duty only (to give an opinion) | `o conselho fiscal cumpriu o dever de dar parecer (art. 202, § 4º)` |
| Art. 202, § 4º, statement | the CVM (the addressee) | the administrators of an open company | duty only (to send the statement within five days) | `os administradores cumpriram o dever de enviar a exposição à Comissão de Valores Mobiliários no prazo (art. 202, § 4º)`, `o último dia para os administradores enviarem a exposição à Comissão de Valores Mobiliários (art. 202, § 4º)` |
| Art. 202, § 5º | the shareholders (implied) | the company | claim / duty (the special reserve is paid as dividend when the situation allows) | `o valor da reserva especial a pagar como dividendo em reais (art. 202, § 5º)` |
| Art. 202, § 6º | the shareholders (implied) | the company | claim / duty (undestined profits are distributed as dividends) | `os lucros não destinados que devem ser distribuídos como dividendos em reais (art. 202, § 6º)` |
| Art. 203 | the preferred shareholders with priority | the company | claim / duty (the fixed or minimum dividend, with arrears if cumulative) and immunity / disability against Arts. 194 to 197 and 202 | `o dividendo fixo ou mínimo devido ao acionista preferencial em reais (art. 203)` |
| Art. 204, caput | the organs of administration, if the estatuto authorizes | the company | power / liability (to declare a dividend from the half-yearly balance sheet) | `os órgãos de administração podem declarar dividendo à conta do balanço semestral (art. 204)` |
| Art. 204, § 1º | the company, under its estatuto | no one named | privilege / no-right, limited by a cap | `a companhia pode distribuir dividendos em períodos menores (art. 204, § 1º)` |
| Art. 204, § 2º | the estatuto (it may authorize) and the organs of administration | the company | power / liability (interim dividends) | `o estatuto pode autorizar o dividendo intermediário à conta da fonte (art. 204, § 2º)` |
| Art. 205, caput | the person registered as owner or usufructuary on the declaration date | the company | claim / duty (payment of the dividend) | `a pessoa é quem recebe o dividendo declarado (art. 205)` |
| Art. 205, § 1º | the company | the shareholder | privilege / no-right (may pay by registered cheque sent by post, or by credit to the shareholder's current account) | `o dividendo pode ser pago por esse meio (art. 205, § 1º)` |
| Art. 205, § 2º | the holders of shares in bank custody or deposit (the depositary delivers to them) | the company (to pay the institution) and the depositary institution (to deliver) | duty only | `a quem a companhia paga o dividendo (art. 205, § 2º)` |
| Art. 205, § 3º | the shareholders; the general meeting (may fix another term) | the company; the shareholders (liable to the meeting's term) | claim / duty (payment within 60 days and within the exercício); power / liability (the meeting's different term) | `o último dia para pagar o dividendo (art. 205, § 3º)`, `o dividendo foi pago no prazo (art. 205, § 3º)` |

## Coverage table

<!-- COVERAGE-BEGIN -->

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Art. 175, caput | src:1559 | fork | br5-exercicio-social: `o exercício social tem a duração que a lei estabelece (art. 175)`, `o exercício social está de acordo com o art. 175` | one year read as 12 months; the end date is fixed by the estatuto (a plain input); fork F-175 |
| Art. 175, parágrafo único | src:1560 | encoded | br5-exercicio-social: `a duração do exercício social é permitida (art. 175, parágrafo único)` | other duration only at constitution and when the estatuto is altered |
| Art. 176, caput e incisos I a V | src:1564-1570 | encoded | br5-demonstracoes: `a demonstração financeira é exigida da companhia (art. 176)`, `a diretoria fez elaborar as demonstrações financeiras que a lei exige (art. 176)` | inciso V only for the open company; "com clareza" is a plain input |
| Art. 176, § 1º | src:1571 | encoded | br5-demonstracoes: `as demonstrações foram publicadas com os valores do exercício anterior (art. 176, § 1º)` |  |
| Art. 176, § 2º | src:1572 | fork | br5-demonstracoes: `a agregação de pequenos saldos é permitida (art. 176, § 2º)` | "não ultrapassem 0,1" read as at most a tenth; fork F-176-2 |
| Art. 176, § 3º | src:1573 | encoded | br5-demonstracoes: `o registro da destinação dos lucros nas demonstrações está de acordo com a lei (art. 176, § 3º)` | together with § 7º |
| Art. 176, § 4º | src:1574 | encoded | br5-demonstracoes: `as demonstrações foram complementadas como a lei exige (art. 176, § 4º)` |  |
| Art. 176, § 5º, incisos I a IV (alíneas a a i) | src:1613-1626 | fork | br5-demonstracoes: `as notas explicativas trazem tudo o que a lei exige (art. 176, § 5º)` | six items arise only when the company has the thing; each carries an exists/indicated pair; fork F-176-5 |
| Art. 176, § 6º | src:1629-1630 | encoded | br5-demonstracoes: `a demonstração financeira é exigida da companhia (art. 176)` | BELOW 2.000.000 of the equity at the balance date, closed company, cash-flow statement only |
| Art. 176, § 7º | src:1633 | encoded | br5-demonstracoes: `o registro da destinação dos lucros nas demonstrações está de acordo com a lei (art. 176, § 3º)` | the CVM may regulate the § 3º record differently; whether it did is a plain input |
| Art. 177, caput | src:1635 | encoded | br5-demonstracoes: `a escrituração da companhia está de acordo com a lei (art. 177)` |  |
| Art. 177, § 1º | src:1636 | encoded | br5-demonstracoes: `a modificação de método contábil foi indicada em nota como a lei exige (art. 177, § 1º)` |  |
| Art. 177, § 2º | src:1647 | encoded | br5-demonstracoes: `a disposição da lei tributária ou de legislação especial foi observada como a lei exige (art. 177, § 2º)` |  |
| Art. 177, § 2º, incisos I e II | src:1648-1649 | repealed or blank in this text | br5-demonstracoes: comment only | both read "(revogado)" in the live text, src:1648-1649 |
| Art. 177, § 3º | src:1650 | fork | br5-demonstracoes: `as demonstrações da companhia aberta estão de acordo com o art. 177, § 3º` | MAYBE: NOTHING for a closed company; fork F-177-3 |
| Art. 177, § 4º | src:1651 | encoded | br5-demonstracoes: `as demonstrações financeiras foram assinadas como a lei exige (art. 177, § 4º)` |  |
| Art. 177, § 5º | src:1652 | encoded | br5-demonstracoes: `a norma da CVM sobre demonstrações financeiras está de acordo com o art. 177, § 5º` | binds the CVM; not a seat question |
| Art. 177, § 6º | src:1653 | fork | br5-demonstracoes: `a companhia pode optar por observar as normas da CVM para companhias abertas (art. 177, § 6º)` | MAYBE: NOTHING for an open company; fork F-177-3 |
| Art. 177, § 7º | src:1657-1658 | repealed or blank in this text | br5-demonstracoes: comment only | "(Revogado pela Lei nº 11.941, de 2009)", src:1657-1658 |
| Art. 178, caput | src:1662 | encoded | br5-balanco: `as contas do balanço estão classificadas e agrupadas como a lei exige (art. 178)` | both limbs required |
| Art. 178, § 1º, incisos I e II | src:1663-1672 | encoded | br5-balanco: `o ativo está disposto em ordem decrescente de liquidez (art. 178, § 1º)`, `o grupo do ativo é não circulante (art. 178, § 1º, inciso II)` | the groups themselves are the core vocabulary `Grupo do ativo (art. 178, § 1º)` |
| Art. 178, § 2º, incisos I a III | src:1673-1686 | fork | br5-balanco: `o patrimônio líquido em reais (art. 178, § 2º, inciso III)` | fork F-178: treasury shares and accumulated losses enter as deductions; the groups are in the vocabulary |
| Art. 178, § 3º | src:1687 | encoded | br5-balanco: `os saldos não compensáveis foram classificados como a lei exige (art. 178, § 3º)` | no duty where the company may offset |
| Art. 179, caput | src:1689 | fork | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | one function for the caput and incisos I to IV and VI; fork F-179 orders the tests |
| Art. 179, inciso I | src:1690 | encoded | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | cash, prepaid expenses, rights due within the dividing term |
| Art. 179, inciso II | src:1691 | fork | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | rights due after it, and related-party loans outside the ordinary business; fork F-179 on the overlap with III |
| Art. 179, inciso III | src:1692 | encoded | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | permanent holdings and rights not for the activity |
| Art. 179, inciso IV | src:1694 | encoded | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | tangible goods for the activity, including operations that transfer benefits, risks and control |
| Art. 179, inciso V | src:1697 | repealed or blank in this text | br5-balanco: comment only | "(Revogado pela Lei nº 11.941, de 2009)", src:1697 |
| Art. 179, inciso VI | src:1698 | encoded | br5-balanco: `o grupo do ativo em que a conta é classificada (art. 179)` | intangible assets for the activity, including purchased goodwill |
| Art. 179, parágrafo único | src:1699 | fork | br5-balanco: `o prazo que separa o circulante do longo prazo em meses (art. 179, parágrafo único)` | the longer of the exercício that follows and the operating cycle; fork F-179-2 |
| Art. 180 | src:1704 | fork | br5-balanco: `o grupo do passivo exigível em que a obrigação é classificada (art. 180)` | same dividing term as Art. 179, parágrafo único; fork F-179-2 |
| Art. 181 | src:1705-1709 | repealed or blank in this text | br5-balanco: comment only | "(Revogado pela Lei nº 11.941, de 2009)" under the heading "Resultados de Exercícios Futuros", src:1709 |
| Art. 182, caput | src:1711 | encoded | br5-balanco: `o capital social realizado em reais (art. 182)`, `a conta do capital social está discriminada como a lei exige (art. 182)` |  |
| Art. 182, § 1º, alíneas a e b | src:1712-1714 | encoded | br5-balanco: `a verba é reserva de capital (art. 182, § 1º)` | canonical name that other modules ask for as an input |
| Art. 182, § 1º, alíneas c e d | src:1717-1718 | repealed or blank in this text | br5-balanco: comment only | both read "(revogada)", src:1717-1718 |
| Art. 182, § 2º | src:1719 | encoded | br5-balanco: `a verba é reserva de capital (art. 182, § 1º)` | folded into the same rule as its fifth fact; the monetary correction it speaks of belonged to the repealed Art. 185 (NOTES.md, What the text turns out to say) |
| Art. 182, § 3º | src:1725 | encoded | br5-balanco: `a contrapartida é ajuste de avaliação patrimonial (art. 182, § 3º)` | three cumulative conditions |
| Art. 182, § 4º | src:1726 | encoded | br5-balanco: `a conta é reserva de lucros (art. 182, § 4º)` |  |
| Art. 182, § 5º | src:1727 | encoded | br5-balanco: `as ações em tesouraria foram destacadas como a lei exige (art. 182, § 5º)` |  |
| Art. 183, caput e inciso I (alíneas a e b) | src:1729-1736 | fork | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)` | fair value, or cost brought down to the probable realization value when lower; fork F-183 |
| Art. 183, inciso II | src:1737 | fork | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)` | cost, or market value when lower; fork F-183 |
| Art. 183, inciso III | src:1738 | fork | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)`, `o custo de aquisição da participação depois de receber ações ou quotas bonificadas em reais (art. 183, inciso III)`, `a participação no capital social de outra sociedade é avaliada pelo custo de aquisição (art. 183, inciso III)` | provision only when the loss is proved permanent; the carve-out "ressalvado o disposto nos artigos 248 a 250" is the plain input `a participação é avaliada pelo método da equivalência patrimonial` (Arts. 248 to 250 live in piece br6); fork F-183-248 |
| Art. 183, inciso IV | src:1739 | fork | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)` | provision is a plain input; fork F-183 |
| Art. 183, inciso V | src:1740 | encoded | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)` | cost less accumulated depreciation, amortization or exhaustion |
| Art. 183, inciso VI | src:1742 | repealed or blank in this text | br5-balanco: comment only | "(revogado)", src:1742 |
| Art. 183, inciso VII | src:1743 | encoded | br5-balanco: `o valor do elemento do ativo no balanço em reais (art. 183)` | cost less accumulated amortization |
| Art. 183, inciso VIII | src:1744 | encoded | br5-balanco: `o elemento do ativo deve ser ajustado a valor presente (art. 183, inciso VIII)` | long-term operations always; the others when the effect is relevant |
| Art. 183, § 1º, alíneas a a c | src:1748-1751 | encoded | br5-balanco: `o valor justo de matéria-prima, bem destinado à venda ou investimento em reais (art. 183, § 1º)` |  |
| Art. 183, § 1º, alínea d (itens 1 a 3) | src:1752-1755 | fork | br5-balanco: `o valor justo do instrumento financeiro em reais (art. 183, § 1º, alínea d)` | the three methods are alternatives joined by "ou" and are not ranked; fork F-183-1d |
| Art. 183, § 2º | src:1760-1763 | encoded | br5-balanco: `a conta em que se registra a diminuição de valor (art. 183, § 2º)`, `a diminuição de valor do imobilizado e do intangível foi registrada como a lei exige (art. 183, § 2º)` | tests in the order a, b, c; no fact gives NOTHING |
| Art. 183, § 3º | src:1768-1770 | fork | br5-balanco: `a companhia cumpriu o dever de analisar a recuperação dos valores do imobilizado e do intangível (art. 183, § 3º)`, `a perda de valor do capital aplicado deve ser registrada (art. 183, § 3º, inciso I)` | fork F-183-3 on the "ou" between incisos I and II |
| Art. 183, § 4º | src:1771 | encoded | br5-balanco: `o estoque pode ser avaliado pelo valor de mercado (art. 183, § 4º)`, and the stock kind in `o valor do elemento do ativo no balanço em reais (art. 183)` | a faculty; MAYBE: NOTHING for stock that is not fungible goods for sale |
| Art. 184, incisos I e II | src:1773-1775 | encoded | br5-balanco: `o valor da obrigação no balanço em reais (art. 184, inciso I)`, `o valor em moeda nacional da obrigação em moeda estrangeira (art. 184, inciso II)` | inciso II only with a parity clause; otherwise NOTHING |
| Art. 184, inciso III | src:1780 | encoded | br5-balanco: `a obrigação deve ser ajustada a valor presente (art. 184, inciso III)` |  |
| Art. 184-A | src:1786 | inert | br5-balanco: comment only | machinery: a regulation-making power of the CVM ("estabelecerá ... normas especiais de avaliação e contabilização") that sets no figure or condition of its own; whatever norms the CVM issues are not in the text |
| Art. 185 | src:1787-1795 | repealed or blank in this text | br5-balanco: comment only | the heading "Correção Monetária" (src:1787) and the caput and §§ 1º to 3º are struck (src:1790-1795) |
| Art. 186, caput e incisos I a III | src:1798-1801 | fork | br5-demonstracoes-contas: `a demonstração de lucros ou prejuízos acumulados discrimina o que a lei exige (art. 186)` | six items arise only if the company had the thing (fork F-186); the monetary correction is in the live text although Art. 185 is repealed |
| Art. 186, § 1º | src:1802 | encoded | br5-demonstracoes-contas: `o valor é ajuste de exercício anterior (art. 186, § 1º)` | "apenas": change of criterion or correction of an error of a particular earlier exercício, not attributable to later facts |
| Art. 186, § 2º | src:1803 | encoded | br5-demonstracoes-contas: `o montante por ação do capital social em reais (art. 186, § 2º)`, `a demonstração de lucros ou prejuízos acumulados indica o dividendo por ação (art. 186, § 2º)`, `a demonstração de lucros ou prejuízos acumulados pode ser incluída na das mutações do patrimônio líquido (art. 186, § 2º)` | per-share figure is NOTHING when there are no shares |
| Art. 187, caput e incisos I a VII | src:1806-1821 | encoded | br5-demonstracoes-contas: `a demonstração do resultado do exercício discrimina o que a lei exige (art. 187)` | nineteen fields, one pair for the participations of inciso VI; the per-share figure of inciso VII uses the Art. 186, § 2º function |
| Art. 187, § 1º | src:1822-1824 | encoded | br5-demonstracoes-contas: `o resultado do exercício em reais (art. 187, § 1º)` | accrual basis: revenues earned less the corresponding costs, expenses, charges and losses; the figure Art. 189 starts from |
| Art. 187, § 2º | src:1826 | repealed or blank in this text | br5-demonstracoes-contas: comment only | "(Revogado)", src:1826 |
| Art. 188, caput e inciso I | src:1841-1846 | encoded | br5-demonstracoes-contas: `a demonstração dos fluxos de caixa indica o mínimo que a lei exige (art. 188, inciso I)` | the change in cash and at least three flows |
| Art. 188, inciso II | src:1847 | encoded | br5-demonstracoes-contas: `a demonstração do valor adicionado indica o mínimo que a lei exige (art. 188, inciso II)`, `a parcela da riqueza não distribuída em reais (art. 188, inciso II)` |  |
| Art. 188, incisos III e IV | src:1850-1854 | repealed or blank in this text | br5-demonstracoes-contas: comment only | both read "(Revogado pela Lei nº 11.941, de 2009)" (src:1850, 1854); the struck wording is not encoded |
| Art. 189, caput | src:1860 | encoded | br5-lucro: `o resultado do exercício depois das deduções em reais (art. 189)` | result minus accumulated losses minus tax provision, before any participation |
| Art. 189, parágrafo único | src:1861 | fork | br5-lucro: `a absorção do prejuízo do exercício (art. 189, parágrafo único)` | waterfall accumulated profits, other profit reserves, legal reserve; fork F-189 |
| Art. 190, caput | src:1863 | fork | br5-lucro: `as participações estatutárias dos empregados, dos administradores e das partes beneficiárias (art. 190)` | successive participations; fractions are the estatuto's (inputs); fork F-190 |
| Art. 190, parágrafo único | src:1864 | encoded | br5-lucro: `os parágrafos do art. 201 se aplicam ao pagamento (art. 190, parágrafo único)` | MAYBE: NOTHING for the employees' participation, which the paragraph does not name |
| Art. 191 | src:1866 | encoded | br5-lucro: `o lucro líquido do exercício em reais (art. 191)` | result after Art. 189 minus the three participations |
| Art. 192 | src:1868 | fork | br5-lucro: `a proposta de destinação do lucro líquido foi apresentada como a lei exige (art. 192)` | duty of the administration; ordinary general meeting from the core's Espécie de assembleia; the proposal goes to the ordinary general meeting only; fork F-192 |
| Art. 193, caput | src:1872 | fork | br5-reservas: `a importância a aplicar na reserva legal em reais (art. 193)`, `o limite da reserva legal em reais (art. 193)` | 5% of the net profit, ceiling 20% of the capital; fork F-193 (no profit puts nothing) |
| Art. 193, § 1º | src:1873 | fork | br5-reservas: `a companhia pode deixar de constituir a reserva legal no exercício (art. 193, § 1º)`, `o menor valor que a companhia deve aplicar na reserva legal no exercício em reais (art. 193)` | "exceder" read strictly (exactly 30% does not exceed); fork F-193 |
| Art. 193, § 2º | src:1874 | encoded | br5-reservas: `o uso da reserva legal é permitido (art. 193, § 2º)` | offset losses or increase capital only |
| Art. 194 | src:1876-1879 | encoded | br5-reservas: `o estatuto pode criar a reserva (art. 194)` | three cumulative conditions |
| Art. 195, caput | src:1881 | fork | br5-reservas: `a assembleia-geral pode destinar parte do lucro líquido à reserva para contingências (art. 195)` | loss "julgada provável" is a plain input; fork F-195 |
| Art. 195, § 1º | src:1882 | encoded | br5-reservas: `a proposta da reserva para contingências indica a causa e justifica a constituição (art. 195, § 1º)` |  |
| Art. 195, § 2º | src:1883 | encoded | br5-reservas: `a reserva para contingências deve ser revertida no exercício (art. 195, § 2º)` | either trigger suffices ("ou") |
| Art. 195-A | src:1886-1887 | encoded | br5-reservas: `a assembleia-geral pode destinar o valor à reserva de incentivos fiscais (art. 195-A)`, `o valor que pode ser excluído da base do dividendo obrigatório em reais (art. 195-A)` | exclusion from the dividend base is a faculty ("poderá") |
| Art. 196, caput | src:1889 | encoded | br5-reservas: `a assembleia-geral pode reter parcela do lucro líquido (art. 196)` |  |
| Art. 196, § 1º | src:1890 | fork | br5-reservas: `o orçamento de capital está de acordo com a lei (art. 196, § 1º)` | up to 5 exercises unless a longer investment project; fork F-196 |
| Art. 196, § 2º | src:1892 | fork | br5-reservas: `o orçamento de capital pode ser aprovado nessa assembleia (art. 196, § 2º)`, `o orçamento de capital pode ser revisado anualmente (art. 196, § 2º)` | "poderá" governs both verbs, so annual revision is a permission that arises only when the budget lasts longer than one exercise; otherwise NOTHING (fork F-196-2) |
| Art. 197, caput | src:1899 | fork | br5-reservas: `o excesso do dividendo obrigatório sobre o lucro realizado em reais (art. 197)`, `a assembleia-geral pode destinar o valor à reserva de lucros a realizar (art. 197)` | at most the excess of the mandatory dividend over the realized part; fork F-197 |
| Art. 197, § 1º | src:1900-1903 | encoded | br5-reservas: `a parcela realizada do lucro líquido em reais (art. 197, § 1º)` | equity-method result is an input out of range (Art. 248, piece br6) |
| Art. 197, § 2º | src:1904 | encoded | br5-reservas: `o uso da reserva de lucros a realizar é permitido (art. 197, § 2º)`, `o valor realizado em dinheiro que se considera integrante da reserva de lucros a realizar em reais (art. 197, § 2º)` | first-realized-in-cash rule for Art. 202, inciso III |
| Art. 198 | src:1906 | fork | br5-reservas: `a destinação às reservas estatutárias e a retenção respeitam o dividendo obrigatório (art. 198)` | fork F-198 (which profit is left) |
| Art. 199 | src:1911 | fork | br5-reservas: `o saldo das reservas de lucros sujeito ao limite em reais (art. 199)`, `o excesso das reservas de lucros sobre o capital social em reais (art. 199)`, `a assembleia-geral deve deliberar sobre a aplicação do excesso (art. 199)`, `a aplicação do excesso das reservas de lucros é permitida (art. 199)` | fork F-199; retention and the special reserve count under the cap; the three named reserves do not |
| Art. 200, caput e incisos I a V | src:1913-1918 | fork | br5-reservas: `o uso da reserva de capital é permitido (art. 200)` | incisos I and V carry a condition; Art. 17, § 5º is an input out of range (piece br1); fork F-17 |
| Art. 200, parágrafo único | src:1919 | encoded | br5-reservas: `a reserva da venda de partes beneficiárias pode ser destinada ao resgate delas (art. 200, parágrafo único)` |  |
| Art. 201, caput | src:1923 | fork | br5-dividendos: `a fonte do dividendo é permitida (art. 201)` | capital reserve only for the Art. 17, § 5º preferred shares (an input out of range, piece br1); fork F-17 |
| Art. 201, § 1º | src:1924 | fork | br5-dividendos: `os administradores e fiscais respondem solidariamente pela reposição do dividendo (art. 201, § 1º)`, `a importância a repor à caixa social em reais (art. 201, § 1º)` | the criminal action "que no caso couber" is not encoded (criminal law, outside the range); fork F-201-1 |
| Art. 201, § 2º | src:1925 | fork | br5-dividendos: `o acionista é obrigado a restituir o dividendo recebido (art. 201, § 2º)` | presumption of bad faith; rebuttal is a plain input; fork F-201 |
| Art. 202, caput e inciso I | src:1931-1934 | fork | br5-dividendos: `o dividendo obrigatório em reais (art. 202)`, `o lucro líquido ajustado para o dividendo obrigatório em reais (art. 202, inciso I)`, `o dividendo obrigatório se o estatuto for omisso em reais (art. 202, inciso I)` | half of the adjusted profit; alíneas a and b; Art. 195-A exclusion as optional fourth term; fork F-202 |
| Art. 202, inciso II | src:1935 | encoded | br5-dividendos: `o dividendo a pagar quando se limita ao lucro realizado (art. 202, inciso II)` | faculty; allowed only if the difference is recorded as reserve of profits to be realized |
| Art. 202, inciso III | src:1936 | encoded | br5-dividendos: `o valor a acrescer ao primeiro dividendo declarado depois da realização em reais (art. 202, inciso III)` |  |
| Art. 202, § 1º | src:1937 | encoded | br5-dividendos: `o critério do estatuto para o dividendo é válido (art. 202, § 1º)` | the minority-arbitrariness test is a plain input |
| Art. 202, § 2º | src:1939 | fork | br5-dividendos: `o dividendo fixado ao alterar o estatuto omisso respeita o mínimo (art. 202, § 2º)` | MAYBE: NOTHING outside the case the paragraph speaks of; floor is AT LEAST 25%; fork F-202-2 |
| Art. 202, § 3º | src:1941-1943 | fork | br5-dividendos: `a assembleia-geral pode deliberar dividendo inferior ao obrigatório ou reter todo o lucro (art. 202, § 3º)`, `o dividendo obrigatório é devido por inteiro no exercício (art. 202)` | one opposing shareholder present blocks it; fork F-202-3 |
| Art. 202, § 4º | src:1944 | fork | br5-dividendos: `o dividendo obrigatório é devido no exercício (art. 202, § 4º)`, `o conselho fiscal cumpriu o dever de dar parecer (art. 202, § 4º)`, `o último dia para os administradores enviarem a exposição à Comissão de Valores Mobiliários (art. 202, § 4º)`, `os administradores cumpriram o dever de enviar a exposição à Comissão de Valores Mobiliários no prazo (art. 202, § 4º)` | 5-day term counted by the core (event day 0); fork F-202-4 |
| Art. 202, § 5º | src:1945 | encoded | br5-dividendos: `o valor da reserva especial a pagar como dividendo em reais (art. 202, § 5º)` |  |
| Art. 202, § 6º | src:1946 | fork | br5-dividendos: `os lucros não destinados que devem ser distribuídos como dividendos em reais (art. 202, § 6º)` | fork F-202-6 |
| Art. 203 | src:1948 | fork | br5-dividendos: `o dividendo fixo ou mínimo devido ao acionista preferencial em reais (art. 203)` | MAYBE: NOTHING for ordinary shares and preferred shares without priority; fork F-203 |
| Art. 204, caput | src:1950 | encoded | br5-dividendos: `os órgãos de administração podem declarar dividendo à conta do balanço semestral (art. 204)` |  |
| Art. 204, § 1º | src:1951 | fork | br5-dividendos: `a companhia pode distribuir dividendos em períodos menores (art. 204, § 1º)` | each half-year against the Art. 182, § 1º capital reserves; fork F-204 |
| Art. 204, § 2º | src:1952 | encoded | br5-dividendos: `o estatuto pode autorizar o dividendo intermediário à conta da fonte (art. 204, § 2º)` |  |
| Art. 205, caput | src:1954 | fork | br5-dividendos: `a pessoa é quem recebe o dividendo declarado (art. 205)` | MAYBE: NOTHING for endossáveis and ao portador (core fork F3); fork F-205 |
| Art. 205, § 1º | src:1955 | encoded | br5-dividendos: `o dividendo pode ser pago por esse meio (art. 205, § 1º)` | MAYBE: NOTHING for any other means |
| Art. 205, § 2º | src:1956 | encoded | br5-dividendos: `a quem a companhia paga o dividendo (art. 205, § 2º)` | Arts. 41 and 43 are inputs out of range (piece br1) |
| Art. 205, § 3º | src:1957 | fork | br5-dividendos: `o último dia para pagar o dividendo (art. 205, § 3º)`, `o dividendo foi pago no prazo (art. 205, § 3º)` | 60 days, or the meeting's date, capped by the end of the exercício; fork F-205-3 |

Rows: 110 (encoded: 59, fork: 41, inert: 1, repealed or blank in this text: 9).

<!-- COVERAGE-END -->

The section index lists 31 live article openers for br5, and a count of the `Art.` openers in the live text of the range gives the same number; Arts. 181 and 185 have no live opener (their text is struck and only "(Revogado ...)" remains in the live text), so 33 article numbers appear in the table, counted by script.
The table has 110 rows, one for each provision of the range (a caput, a paragraph, an inciso or alínea, or a run of them the text treats together): 59 `encoded`, 41 `fork`, 9 `repealed or blank in this text` and 1 `inert`; none is `deferred`.
A `fork` row is encoded in layer 1 like an `encoded` one; it is marked `fork` because the text does not settle the reading, and its note names the register entry and says which reading was taken.
The one `inert` row is Art. 184-A, a regulation-making power of the CVM that sets no figure or condition of its own (the allowed reason: machinery).

## Fork register

Where a module comment cites a fork it uses the ID below.
The forks that no module comment cites are recorded here and in the coverage rows only: F-176-5, F-177-3, F-179-2, F-183-248, F-183-1d, F-192, F-195, F-196, F-197, F-201-1, F-17, F-202-2, F-202-3, F-203, F-regulative, F-seat.
Where the text decides the point in so many words, no fork is recorded.
Each coverage row with the disposition `fork` names its entry here and says which reading was taken.

| id | provision | the ambiguity and the readings seen | the reading taken | the text that licenses it |
| --- | --- | --- | --- | --- |
| F-175 | Art. 175, caput | What "1 (um) ano" is as a duration. Seen: twelve months; 365 days. | Twelve months, counted in whole months. | "O exercício social terá duração de 1 (um) ano e a data do término será fixada no estatuto" (src:1559). A case asserts twelve months with the end date fixed. |
| F-176-2 | Art. 176, § 2º | "não ultrapassem 0,1 (um décimo)": at most a tenth, or strictly less than a tenth. | At most a tenth: exactly a tenth is allowed. | "não ultrapassem" (src:1572) forbids only passing the tenth. Asserted at 100 of 1,000 (allowed) and 101 (not). |
| F-176-5 | Art. 176, § 5º | Whether every item the notes list is owed by every company. | Six items arise only if the company has the thing and are encoded as pairs ("it exists", "the notes give it"); the other items are always owed. | Items b and i carry the condition in words ("quando relevantes"; "que tenham, ou possam vir a ter, efeito relevante", src:1619, 1626). Items c, e, g and h (new valuations, long-term obligations, options granted, prior-year adjustments) are conditional by their nature: with none of them there is nothing to indicate. The text does not say so in words. |
| F-177-3 | Art. 177, §§ 3º and 6º | What § 3º says of a closed company. Seen: no duty; not covered. | NOTHING for a closed company in § 3º; § 6º gives a closed company the option and says NOTHING for an open one. | § 3º names "companhias abertas" only (src:1650); § 6º says "As companhias fechadas poderão optar" (src:1653). |
| F-178 | Art. 178, § 2º, III; Art. 182, §§ 3º and 5º | How treasury shares and accumulated losses enter the equity total. Seen: added; deducted. | Both are deductions; the adjustments of Art. 182, § 3º carry their own sign. | § 5º: "deverão ser destacadas no balanço como dedução da conta do patrimônio líquido" (src:1727); the adjustments are "aumentos ou diminuições" (src:1725); a loss is a deduction by its nature. |
| F-179 | Art. 179 | An account that fits two classes, and one that fits none. | Tests in order: a tangible asset for the activity (IV); an intangible one (VI); a permanent holding (III); cash and prepaid expenses (I); a related-party loan or sale outside the ordinary business (II, whatever its term); another right with a term (I within the dividing term, II after it); a right with no term and not for the activity (III). Where a right could be both II and III, II is taken because it is the one that speaks of the term. If no fact applies: NOTHING. | The incisos classify and the text gives no order (src:1689-1698); the order is read from what each inciso excludes. |
| F-179-2 | Art. 179, parágrafo único; Art. 180 | The dividing term where the operating cycle is longer than the exercício. | The dividing term is the longer of the exercício that follows and the cycle. | "a classificação no circulante ou longo prazo terá por base o prazo desse ciclo" (src:1699); Art. 180 sends its own classification to the same paragraph (src:1704). |
| F-183 | Art. 183, incisos I b, II and IV | "quando este for inferior" and the provisions for loss. | A provision is a plain input; "when lower" is the lower of the two figures. | Inciso I b "ajustado ao valor provável de realização, quando este for inferior" (src:1736); II "deduzido de provisão para ajustá-lo ao valor de mercado, quando este for inferior" (src:1737); IV likewise (src:1739). |
| F-183-248 | Art. 183, inciso III | "ressalvado o disposto nos artigos 248 a 250": how to carry a rule that lives in another piece. | A separate rule, `a participação no capital social de outra sociedade é avaliada pelo custo de aquisição (art. 183, inciso III)`, takes the outcome of Arts. 248 to 250 as a plain input; the valuation function is meant to be given the item-III constructor only for a holding that rule says is at cost. | src:1738. Art. 248 values by the equity method "os investimentos em coligadas ou em controladas e em outras sociedades que façam parte de um mesmo grupo ou estejam sob controle comum" (read in piece br6's range, first line only). Asserted for the new rule; the carve-out itself is not modelled. |
| F-183-1d | Art. 183, § 1º, alínea d | Three methods for an instrument with no active market, joined by "ou". Seen: ranked in the order listed; a free choice. | A free choice by the preparer (an input); none is ranked. | Items 1), 2) and 3) are joined by "ou" and ranked by nothing (src:1753-1755). |
| F-183-3 | Art. 183, § 3º | The "ou" between incisos I and II. Seen: alternatives of one another; each owed under its own trigger. | I is owed when its trigger is present; II is owed when the analysis shows that the criteria need revising (an input). | "a fim de que sejam: I – registradas as perdas ... ou ... ; ou II – revisados e ajustados os critérios" (src:1769-1770). |
| F-186 | Art. 186 | Whether every item of the statement is owed by every company, and the monetary correction. | Items that arise only if the company had the thing (a dividend, a reversal, an adjustment and so on) carry an "existed" / "shown" pair; the monetary correction of the opening balance is required only if the company applied one, because Art. 185, which governed it, is repealed. | Art. 186, inciso I still lists "a correção monetária do saldo inicial" (src:1799) while Art. 185 is struck (src:1788-1795). |
| F-189 | Art. 189, parágrafo único | "pelas reservas de lucros e pela reserva legal, nessa ordem": whether "reservas de lucros" includes the legal reserve. | It means the profit reserves other than the legal reserve, which the text lists after it. | "pelos lucros acumulados, pelas reservas de lucros e pela reserva legal, nessa ordem" (src:1861). |
| F-190 | Art. 190 | A result of zero or less. | It bears no participation and stays a loss; the first participation is taken on the result Art. 189 leaves. | "com base nos lucros que remanescerem" (src:1863): with no profit there is nothing to take it from. Asserted. |
| F-192 | Art. 192 | Which meeting receives the proposal. | The ordinary general meeting only. | "apresentarão à assembléia-geral ordinária" (src:1868). |
| F-193 | Art. 193, caput and § 1º | A net profit of zero or less; "exceder de 30%". | A profit of zero or less puts nothing in the reserve; exactly 30% does not exceed. | "5% ... do lucro líquido" (src:1872) presupposes a profit; "exceder de 30%" (src:1873) says passing it. Asserted at the boundary. |
| F-195 | Art. 195 | "perda julgada provável, cujo valor possa ser estimado". | Both are plain inputs: the judgment is the administration's and the meeting's, and the Law supplies no test. | src:1881. |
| F-196 | Art. 196, § 1º | "até 5 (cinco) exercícios, salvo ... projeto de investimento". | At most five exercícios; no cap for a budget that executes a longer investment project. | src:1890. Asserted at 5 (allowed) and 6 (not), and at 6 with a longer project. |
| F-196-2 | Art. 196, § 2º | "poderá ser aprovado ... e revisado anualmente": a duty or a permission. | A permission, arising only for a budget that lasts more than one exercício; for a budget of one exercício or less the paragraph says NOTHING. | "poderá" governs both verbs (src:1892). An earlier draft of this rule read "deve" and was corrected after re-reading the text in the last pass; its two assertions were rewritten from the text. |
| F-197 | Art. 197, caput | "poderá ... destinar": how much. | At most the excess of the mandatory dividend over the realized part of the net profit. | src:1899. Asserted at the excess (allowed) and one more (not). |
| F-198 | Art. 198 | Which profit the statutory reserves and the retention must leave the mandatory dividend. | The net profit left once the reserves the Law puts first (legal and contingency, Art. 202, inciso I) are taken out must still cover the mandatory dividend after the statutory reserves and the retention are taken out too. | "não poderão ser aprovadas, em cada exercício, em prejuízo da distribuição do dividendo obrigatório (artigo 202)" (src:1906). Asserted at equality and one over. |
| F-199 | Art. 199 | Which reserves count under the cap; what "Atingindo esse limite" means. | The legal, statutory, retained-profit and special reserves (the last of Art. 202, § 5º) count; the contingency, tax-incentive and to-be-realized reserves do not; the limit is reached when adding to the reserves would take them above the capital. | "exceto as para contingências, de incentivos fiscais e de lucros a realizar, não poderá ultrapassar o capital social" (src:1911). The special reserve is not among the three exceptions, so it counts. |
| F-201-1 | Art. 201, § 1º | The criminal action the paragraph reserves. | No rule: the text reserves it ("sem prejuízo da ação penal que no caso couber") without a condition the encoding could compute; the civil liability to restore is encoded. | src:1924. |
| F-201 | Art. 201, § 2º | Who may rebut the presumption of bad faith, and how. | The presumption is rebuttable and whether it was rebutted is a plain input. | The text states the presumption and says nothing of rebuttal (src:1925). Asserted. |
| F-17 | Arts. 200, inciso V, and 201 | The cross-reference to "artigo 17, § 5º". | Both inputs are asked for what the words describe (the advantage of a dividend from the capital reserve is assured), keeping the citation the text gives; the live paragraph with that content is Art. 17, § 6º. | src:1918 and 1923 cite § 5º. In the live Art. 17 that content is § 6º (src:141) and § 5º is about taking part in capital increases (src:140); the old § 5º, with the content, is struck (src:129). Found while verifying the cross-references; see "What the text turns out to say", finding 1. |
| F-202 | Art. 202, inciso I and the lead-in | The base of the mandatory dividend, and Art. 195-A. | Net profit, less the sum put in the legal reserve, less the sum put in the contingency reserve, plus the reversal of that reserve from earlier exercícios, less (optionally) the part of the tax-incentive reserve the company excludes under Art. 195-A; when the estatuto is silent the dividend is half of that base, and a base of zero or less gives nothing. | src:1931-1934. Art. 195-A says the part "poderá ser excluída da base de cálculo do dividendo obrigatório (inciso I do caput do art. 202 desta Lei)" (src:1886-1887), which Art. 202 itself does not mention. Asserted. |
| F-202-2 | Art. 202, § 2º | When the floor of 25% applies. | Only where the estatuto was silent and the meeting resolves to alter it to introduce a norm on the matter; for any other case NOTHING. | "Quando o estatuto for omisso e a assembléia-geral deliberar alterá-lo" (src:1939). Asserted at 250 (respects it) and 249 (does not). |
| F-202-3 | Art. 202, § 3º | How many opposing shareholders block the reduction. | One: the opposition of any shareholder present blocks it. | "desde que não haja oposição de qualquer acionista presente" (src:1941). Asserted. |
| F-202-4 | Art. 202, § 4º | What lifts the duty, and how the five days run. | The administration's information to the ordinary meeting lifts the duty for that exercício; the conselho fiscal's opinion and the statement to the CVM are separate duties on which the text does not make the exemption depend; the five days run from the meeting with the meeting date as day 0 and the fifth day inside (core forks F1 and F2). | src:1944. Asserted, including the last day. |
| F-202-6 | Art. 202, § 6º | "Os lucros não destinados": which profits. | The net profit of the exercício less the six destinations of Arts. 193 to 197 (legal, statutory, contingency, tax-incentive, retention, profits to be realized); accumulated profits and reversals are not added. | src:1946: "Os lucros não destinados nos termos dos arts. 193 a 197". Asserted. |
| F-203 | Art. 203 | "inclusive os atrasados, se cumulativos". | Arrears are added only if the dividend is cumulative; shares with no priority, and shares that are not preferred, are not covered (NOTHING). | src:1948. Asserted. |
| F-204 | Art. 204, § 1º | "cada semestre do exercício social". | The two halves of the exercício; the cap (the capital reserves of Art. 182, § 1º) applies to each half. | src:1951. |
| F-205 | Art. 205, caput | "ações nominativas": which forms of share are covered. | Nominativas and escriturais; for endossáveis and ao portador NOTHING. | src:1954. The live Art. 20 says shares "devem ser nominativas" (src:151) while other Articles still name the other forms (core fork F3 in `KEEL-NOTES.md`). Asserted. |
| F-205-3 | Art. 205, § 3º | "dentro do exercício social": which exercício; how the 60 days run. | The exercício in which the dividend is declared; 60 days from the declaration with the declaration day as day 0 and the sixtieth day inside; the last day is the earlier of the term (60 days, or the date the meeting fixes) and the end of the exercício. | src:1957; core forks F1 and F2. Asserted. |
| F-regulative | the duties of the range | PARTY / MUST rules or compliance functions. | Compliance functions: a rule says whether a duty was met (for example `a diretoria fez elaborar as demonstrações financeiras que a lei exige (art. 176)`). The two time limits (Art. 202, § 4º and Art. 205, § 3º) are functions of dates that use the core's `Prazo`. | The duties are of a company and its organs, and what matters is what was done. `check.sh` cannot see a `#TRACE` outcome: its own header says "It does NOT see a different #TRACE outcome". No `#TRACE` is in this encoding. |
| F-seat | the seat | Where the seat is coarser than layer 1. | The notes (Art. 176, § 5º) and the statement of accumulated profits (Art. 186) ask the conditional items as one; Art. 187 is asked inciso by inciso; see "Seat". | A shareholder cannot list eighteen items of a note. |

## Cross-references out of my ranges

Seven places in the text cite a provision outside the range by number: Art. 247 (src:1619), Art. 243 (src:1691), Arts. 248 to 250 (src:1738), Art. 248 (src:1901), Art. 17 twice (src:1918 and 1923) and Arts. 41 and 43 (src:1956); the table has 9 rows because it also lists two dependencies the text names without a number (the conselho fiscal of Art. 161 and the priority of the preferred shares of Art. 17) and counts Art. 243 a second time for the controlled company of Art. 202, § 3º.
Each input carries a comment `-- out of range: ...` in the module that declares it, and in the seat above the question that asks it.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| Art. 176, § 5º, IV, b | Art. 247, parágrafo único (what makes an investment relevant) | br6 | `há investimentos relevantes em outras sociedades` (layer 1; the seat treats each conditional item as existing) |
| Art. 179, II | Art. 243, §§ 1º and 2º (coligada, controlada) | br6 | `o direito deriva de venda, adiantamento ou empréstimo a coligada, controlada, diretor, acionista ou participante no lucro e não é negócio usual na exploração do objeto` |
| Art. 183, III | Arts. 248 to 250 (holdings valued by the equity method) | br6 | `a participação é avaliada pelo método da equivalência patrimonial` |
| Art. 197, § 1º, I | Art. 248 (the net positive equity-method result) | br6 | `o resultado líquido positivo da equivalência patrimonial em reais` |
| Art. 200, V; Art. 201 | Art. 17, § 6º of the live text, cited by both as § 5º (preferred shares paid from the capital reserve) | br1 | `a vantagem do dividendo à conta de reserva de capital é assegurada às ações preferenciais (art. 17, § 5º)`, `o dividendo é o das ações preferenciais de que trata o art. 17, § 5º` |
| Art. 202, § 3º, II | Art. 243, § 2º (controlada) | br6 | `a companhia fechada é controlada por companhia aberta` |
| Art. 202, § 4º | Art. 161 (a conselho fiscal that works permanently or only when installed; the text says "em funcionamento") | br4 | `o conselho fiscal está em funcionamento` |
| Art. 203 | Art. 17, inciso I and § 4º (priority in a fixed or minimum dividend; cumulative only if the estatuto says so) | br1 | `as ações têm prioridade a dividendo fixo ou mínimo`, `os dividendos são cumulativos` |
| Art. 205, § 2º | Arts. 41 and 43 (shares in bank custody or in deposit) | br1 | `as ações estão em custódia bancária (art. 41)`, `as ações estão em depósito (art. 43)` |

To write these rows I read text outside my range, only as far as each reference needed: the first lines of Arts. 161, 243 (the caput and §§ 1º to 4º), 247 (the caput and incisos I and II), 248 and 250; the section-index line (the first seventy characters of the opener) of Arts. 17, 41, 43, 46, 52, 116, 132, 133, 161, 243, 247 and 248; Art. 17 (src:121-141, about thirty lines) and the lines around Art. 20 (src:150-153), found by a keyword scan of lines 1 to 371 for "fixo ou mínimo", "mínimo", "cumulativ" and "prioridade na distribuição".

## Needs from the core

Nothing the core lacks, and no promotion is requested.
Used from the core: `Tipo de companhia` (`companhia aberta`, `companhia fechada`) and the canonical input `o tipo da companhia`; `Espécie de ação` (`ações ordinárias`, `ações preferenciais`) and `Forma da ação` (`ações nominativas`, `ações escriturais`, `ações endossáveis`, `ações ao portador`); the record `Participação do acionista` with its canonical fields; `Espécie de assembleia` (`assembleia-geral ordinária`, `assembleia-geral extraordinária`, `assembleia especial`); `Parte` (`o acionista`, `a instituição financeira`); and the time functions `o termo final do prazo`, `o ato foi praticado dentro do prazo`, `prazo em dias` and `YMD`, with the core's counting convention (the event day is day 0, and day N is the last day in time; forks F1 and F2).
The local enumerations in `br5-vocabulario.l4` carry specific names ending in a citation (for example `Uso de reserva (art. 193, § 2º)`, shared by Arts. 193, 197, 199 and 200 inside this piece), so nothing collides at the merge; none needs to be promoted.
The core's `o prazo` is a rule parameter, not a top-level name, and the local bindings called `o prazo` in this piece's `WHERE` clauses do not redefine anything.

## What the text turns out to say

1. Arts. 200, inciso V, and 201 cite "artigo 17, § 5º" for the preferred shares whose estatuto lets them receive their cumulative priority dividend from the capital reserves (src:1918, 1923).
   In the live text of Art. 17 that content is § 6º (src:141); the live § 5º is about taking part in capital increases (src:140); and the old § 5º, which had the content, is struck (src:129).
   The two cross-references are therefore stale against the live numbering.
   The inputs keep the citation the text gives and describe the fact by its content; the behaviour that depends on them (a capital reserve may pay dividends only where that advantage is assured) is asserted, the stale number is not a behaviour and is not.
2. The converter left a live "I" at the start of src:1929, directly before the struck "I - importância destinada à formação de reservas para contingências"; which appears to be the numeral "II" of the old inciso II, split by the strike wrapper.
   The live Art. 202 begins at src:1931.
   The stray "I" is a fragment of struck text and is not read.
3. Art. 185 (monetary correction) is repealed (src:1788-1795), yet Art. 182, § 2º still registers "o resultado da correção monetária do capital realizado" as a capital reserve (src:1719) and Art. 186, inciso I still lists "a correção monetária do saldo inicial" (src:1799).
   The encoding keeps both: the result of the monetary correction is the fifth fact of `a verba é reserva de capital (art. 182, § 1º)`, and the monetary correction of the opening balance is required in the statement only if the company applied one.
   Asserted.
4. Art. 176 lists five statements but binds them unevenly: inciso V only for an open company (in its own words, "se companhia aberta"), and inciso IV is waived by § 6º for a closed company with equity under R$ 2.000.000,00 (src:1629).
   Both incisos III and IV end with "; e" (src:1567, 1569), a leftover of the amendments that carries no meaning.
   Asserted at R$ 1.999.999 (not owed) and R$ 2.000.000 (owed at exactly the threshold, "inferior a" being strict).
5. Art. 199 excludes only three reserves from the cap (contingency, tax-incentive and profits to be realized, src:1911); the legal reserve, the statutory reserves and the retention of Art. 196 count, and so, by the reading F-199, does the special reserve of Art. 202, § 5º.
   Asserted.
6. Art. 195-A reaches into Art. 202: the base of the mandatory dividend is defined in Art. 202, inciso I (src:1932-1934), which does not mention the tax-incentive reserve, and Art. 195-A (src:1886-1887) adds that the part allocated "poderá ser excluída" from it.
   Asserted.
7. Art. 203 names Arts. 194 to 197 and 202 (src:1948) and not Art. 193 or Art. 195-A.
   The rule `o dividendo fixo ou mínimo devido ao acionista preferencial em reais (art. 203)` computes what is owed and models no conflict with any reserve, so the omission changes no result here.
8. Art. 205 speaks only of "ações nominativas" (src:1954), while the live Art. 20 says shares "devem ser nominativas" (src:151) and other Articles still name endossáveis, ao portador and escriturais (core fork F3).
   The reading is nominativas and escriturais, with NOTHING for the others.
   Asserted.
9. Art. 196, § 2º reads "poderá ser aprovado ... e revisado anualmente, quando tiver duração superior a um exercício social" (src:1892): "poderá" governs both verbs, so annual revision is a permission and not a duty.
   An earlier draft encoded a duty; it was found by re-reading, and its assertions were rewritten from the text.
   Asserted.
10. Art. 202, § 4º lifts the mandatory dividend on the administration's information to the ordinary meeting alone (src:1944); the opinion of the conselho fiscal and the statement to the CVM are further duties and the text makes no exemption depend on them.
    Asserted.
11. Art. 202, § 3º is blocked by the opposition of any one shareholder present (src:1941).
    Asserted.
12. Four provisions carry "Vide" notes to later instruments the text does not reproduce: Art. 183, inciso VIII and Art. 184, inciso III (Lei nº 12.973, de 2014; src:1744, 1780) and Arts. 202 and 203 (Medida Provisória nº 608, de 2013 and Lei nº 12.838, de 2013; src:1931, 1948).
    They are not encoded: the encoding follows the text of the compilation only.
13. The range holds no enactment, commencement or transitional provision (Art. 205 is the last article of Chapter XVI), so no date is built.
14. The text is a plain-text rendering of Planalto's compilation, retrieved on 2026-10-21; its own `meta.json` says "Not official" and that in-force status was not separately verified.
    Nothing here has been checked against the Diário Oficial da União.

## What the stable binary does not accept

Sorted by how each one shows itself: the loud ones raise a diagnostic, the silent ones return a different answer with no diagnostic at all.
Every item was run against `l4` 1.6.98 in this session, each probe in its own file with a control, because a parse error stops the whole file.
Silent:
- `NOT x OR y` parses as `NOT (x OR y)`, not as `(NOT x) OR y`.
  With `x` and `y` both TRUE the probe `NOT x OR y` gives FALSE, no diagnostic.
  This was the cause of ten failing assertions in an early draft of the statements module; every such condition is written `((NOT x) OR y)`.
Loud:
- A percent literal followed by another argument is a parse error: `scale2 10% 5` gives "unexpected 5".
  As the last argument it parses (`scale2 5 10%`), and bracketed it parses anywhere (`scale2 (10%) 5`); the tests bracket every percent literal.
- A nested `ELSE IF` whose `THEN` is aligned with the outer `IF` fails with "incorrect indentation (got 10, should be greater than 10)"; the staircase layout, with the inner `THEN` and `ELSE` aligned under the inner `IF`, parses.
- An `#ASSERT` that continues on a second line is a parse error ("unexpected TRUE" at the continuation); each `#ASSERT` here is on one line.
Not limits, found while checking: a negative literal parses (`f -5`, `f (-5)` and `-4` as an expected value were all accepted), and a number written without a separator (`2000000`) equals the same number written `2_000_000`, so the separators in this encoding are for the reader.
The dialect limits the brief lists (no `REFUSE`, section `GIVEN`, `TYPICALLY`, `SET OF`, `EVERY`, `@lang` or `@nlg`) are not used: a search of the non-comment lines of every `br5-*.l4` finds none of them, nor `BECAUSE`, `PARTY`, `MUST` or `#TRACE`.

## What check.sh prints

The brief prescribes `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
With the target `unstable` the script skips the comparison with a second build, because `L4_BIN` is itself the stable 1.6.98 binary the brief names; the first line says so.
The run below is the last one, made after every `.l4` file was final.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
br-core.l4                                     0         0       0        0         0
br5-balanco.l4                                 0         0       0        0         0
br5-cases-seat.l4                              0       186       0        0         0
br5-demonstracoes-contas.l4                    0         0       0        0         0
br5-demonstracoes.l4                           0         0       0        0         0
br5-dividendos.l4                              0         0       0        0         0
br5-exercicio-social.l4                        0         0       0        0         0
br5-lucro.l4                                   0         0       0        0         0
br5-reservas.l4                                0         0       0        0         0
br5-seat.l4                                    0         0       0        0         0
br5-tests-balanco.l4                           0       122       0        0         0
br5-tests-demonstracoes-contas.l4              0        67       0        0         0
br5-tests-demonstracoes.l4                     0        75       0        0         0
br5-tests-dividendos.l4                        0       121       0        0         0
br5-tests-exercicio-social.l4                  0        12       0        0         0
br5-tests-lucro.l4                             0        42       0        0         0
br5-tests-reservas.l4                          0        97       0        0         0
br5-vocabulario.l4                             0         0       0        0         0
TOTAL (18 modules)                             0       722       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Per module: the layer-1 tests assert 12 (Art. 175), 75 (Arts. 176, 177), 122 (Arts. 178 to 185), 67 (Arts. 186 to 188), 42 (Arts. 189 to 192), 97 (Arts. 193 to 200) and 121 (Arts. 201 to 205), 536 in all, and the seat's cases assert 186.
Each test and case file ends with assertions written equal to assertions satisfied (counted by script from `#ASSERT` lines).
The instrument was checked with a positive control once, during the work: a deliberately false assertion appended to a copy of the dividends tests fails as it should, and the copy was deleted.
No assertion is expected to fail: the `expected` column is 0 for every module.
Two further checks were run on the final files: `python3 -I srcrefs.py check --refs <text> br5-*.l4` printed `srcrefs check: 308 src: lines, 134 runs, 162 locators, 0 problems`, and the keel's item 12 (every `@ref` article compared with the governing `Art.` of each cited line, `inputs/work/check_refs_articles.py`) printed `checked 308 (label, line) pairs, 0 mismatches`.

## Before this is worth relying on

No part of this is legal advice, and a reviewer who knows Brazilian company law has not yet read it.
The expected values in the tests were written by hand from the text, but the same author wrote the encoding and the expectations; no second reader has checked them.
The duties are compliance functions: there are no PARTY / MUST rules and no `#TRACE` check, so nothing here simulates a sequence of acts in time, and `check.sh` could not have seen a trace.
The forks that change a result and most deserve a reviewer's ruling are F-179 (the order in which an account is sorted into a class), F-183-3 (the "ou" of the recoverability analysis), F-186 (the conditional items and the monetary correction), F-189, F-190, F-198 and F-199 (how profits and reserves are counted), F-202 (the base of the mandatory dividend and the optional Art. 195-A exclusion), F-202-4 (what lifts the duty), F-205 (which forms of share are covered) and F-17 (the stale reference to Art. 17).
Several inputs are judgments the Law leaves to someone else (that the statements express the position "com clareza", that a loss is "julgada provável", that an estatuto criterion exposes the minority to arbitrariness, that an investment is relevant); they are plain facts the asker states, and the encoding does not decide them.
The classification of an asset (Art. 179) and the valuation of an element (Art. 183) were encoded from lists that give no order; a human reading of those two is the most useful single check.
26 layer-1 rules have no seat question (see "Seat"); the seat is therefore thinner than layer 1 on how the statements are presented and valued.
The text is a compilation rendered by a converter as of 2026-10-21, not official and not a historical vintage, and the "Vide" notes point to later instruments that are not encoded.
I checked the permission verbs of the range against the rules that encode them (32 lines of the live text matched the pattern I used, which covers poderá, poderão, podem, pode, poderia and facultad), reading each against its rule; that check found one error, Art. 196, § 2º, now corrected.
The cross-references were checked the same way, and that check found the stale reference to Art. 17.
Neither check is a proof that no other modal verb or reference is misread.
