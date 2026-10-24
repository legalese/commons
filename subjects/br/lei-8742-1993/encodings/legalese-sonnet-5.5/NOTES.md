# NOTES — Lei nº 8.742, de 7 de dezembro de 1993 (Lei Orgânica da Assistência Social, LOAS)

Encoding `legalese-sonnet-5.5`: the whole Law, in two layers, for the stable `l4` 1.6.98 (the brief's dialect `main`).
Draft by a model; no domain expert has read it against the source (see "Before this is worth relying on").

**The source.**
`lei-8742-1993.pt.txt` (534 lines) is a plain-text rendering, made by a converter script, of a compiled text of the Law (its header names the Presidência da República, Casa Civil, and says "Texto compilado"; its date of retrieval is not recorded in the inputs).
It is not the official text: its own last lines say "Este texto não substitui o publicado no DOU de 8.12.1993".
Nothing here is "verified against the official text".
Superseded wording that the compilation shows struck through is kept in the file as `⟦STRUCK: …⟧`; no struck wording is encoded.
Every quotation in the `.l4` files is a `-- src:N | …` line produced by `srcrefs.py quote` from that file, and `python3 -I srcrefs.py check --refs` reports 0 problems.

**Two layers.**
Layer 1 (`lo-nouns`, `lo-datas`, `lo-cap1-2-principios`, `lo-cap3-organizacao`, `lo-bpc-concessao`, `lo-bpc-manutencao`, `lo-eventuais-servicos`, `lo-auxilio-inclusao`, `lo-cap5-financiamento`, `lo-cap6-gerais`) is the law from nobody's seat, with a test module for each part.
Layer 2 (`lo-seat.l4`, `lo-cases-seat.l4`) is the thin seat layer: 82 questions over layer 1, and at least one case for each.

## Seat

**The seat: a person or family who needs social assistance and asks whether they qualify for the benefits, services and programmes the Law provides (in particular the continuous cash benefit, "benefício de prestação continuada", BPC, and the eventual benefits), how much, for how long, and what they must do or declare.**
Why this seat: the Law is the organic law of social assistance, and its operative core is what a needy family can claim (arts. 20 to 26-H, 37, 40 to 40-C) and what it must do to keep it (arts. 20 §§ 8, 12, 12-A; 21 to 21-B).
The Law has no second private party with duties of its own: the other party of every claim is a public body (the INSS, the Union, the States, the Federal District, the Municipalities, a Council, the Public Prosecution Service).
Under the Commons rule "there is never a seat for an official", so there is one seat.

How the seat layer was built:

- It imports the layer-1 modules and calls their rules; it restates none.
  Each question has `@export` and `@desc`, takes plain inputs (yes/no, number, date, a choice from a list of the nouns module), and builds the layer-1 records in a `WHERE`.
  A record field the called rule never reads gets a fixed placeholder, with a comment (questions on art. 20 §§ 2º-A/6º and on art. 26-A § 3º).
- Questions are grouped under `§§` headings in the order of the text; a heading whose group only arises in some situations says so in a comment ("Arises only for someone who already receives the BPC …").
- Questions are phrased as the person asks ("Tenho direito …?", "Posso …?", "Preciso …?", "Até que dia devo …?"), in Brazilian Portuguese.
- The facts about the other party on which a claim depends are inputs: whether the INSS assessment was done (art. 20 § 6º), whether the first payment was made in time (art. 37), the day the INSS or the Ministry found the accumulation (art. 26-B § 3º).
- Where the person also owes something, the paired question exists: declare the income (§ 8º), register in the CPF and the CadÚnico and keep them (§ 12), submit biometrics (§§ 12-A, 12-B), regularise the CadÚnico within 45 or 90 days (art. 21-B), submit to the review every 2 years (art. 21 caput); and what can be done to the person: cessation (21 § 1º), cancellation (§ 2º), suspension (21-A, 21-B § 2º), blocking of the credit (21-B § 1º), consignation of debts (40-C).
- Defaults of `COMMONS-CLAUDE.md` followed: the Act alone; the actors the text names; a judgment handed to someone else is a conditional input (the INSS assessment, the Ministry's recognition, the CNAS deliberations, "baixa renda nos termos do regulamento"); the Act's own definitions worked out from facts (art. 3, art. 20 § 1º, § 2º, § 10); borrowed terms asked as facts (the minimum wage, the regulation's widened limit, Lei nº 8.213 art. 139 § 1º); one case = one person/family/benefit; the Act's own terms, each with a plain gloss in a comment; the operative sections in, the machinery out.
- Departures: none from the defaults.
  One choice to note: the BPC question takes the family as numbers (people under the roof, their income, three exclusions) and not as a list; the question "Esta pessoa conta como membro da minha família?" answers who counts.

**Machinery (left out of layer 1, each with a reason in the coverage table):**
art. 5 (directives of organisation); art. 6 caput and §§ 1 to 5 (objectives and identity of the Suas); art. 6-B caput, §§ 3 and 4; art. 6-E; art. 6-F §§ 3 to 5; arts. 7, 8, 10, 11; art. 9 §§ 1 and 2; arts. 12 II and IV, 12-A, 13 II, IV, VI, 14 VI, VII, 15 VI, VII (competences to co-finance, monitor, support); arts. 16 to 18 (the Councils and the CNAS); art. 19 caput and I to XIV (competences of the federal body); art. 20 § 6-A; art. 23 § 1º; art. 24 §§ 1 and 2; arts. 24-A and 24-B sole paragraphs; art. 26; art. 26-D sole paragraph; art. 26-G; art. 27; art. 28 §§ 1 and 3; art. 29 caput; arts. 30-A to 30-C; arts. 32 §§ 1 and 2, 33 §§ 1 and 2; art. 35 §§ 1 and 2; art. 39; art. 40 § 1º; art. 40-B § 1º; art. 42.
The provisions that decide something for an entity (arts. 3, 6-B §§ 1 and 2, 9, 30, 36) are encoded in layer 1 but have no seat question, because they decide nothing the person in this seat would ask.

## Jural relations

Hohfeld: a claim is paired with a duty; a privilege is the other party's no-right; a power is the other party's liability (being subject to it); an immunity is the other party's disability.
A relation is stated once, in layer 1, under a neutral name; layer 2 takes the other party's facts as inputs.

| section | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule (layer 1) |
|---|---|---|---|
| art. 1º | the citizen: claim to social assistance that needs no prior contribution | the State: duty ("dever do Estado") | `art. 1º — o direito à assistência social depende de contribuição prévia do beneficiário` (FALSE) |
| arts. 2º, 4º I and II | none (statement of objectives and principles) | none | `art. 2º, caput e incisos — objetivos…`, `art. 2º, parágrafo único…`, `art. 4º — princípios…` (typed lists) |
| art. 3º | none (definition of the entities) | none | `art. 3º, caput`, `§ 1º`, `§ 2º`, `§ 3º` |
| art. 4º, III | the person asked to prove need: immunity from humiliating proof | whoever demands the proof: disability | `art. 4º, III — a comprovação de necessidade exigida é vedada` |
| art. 4º, IV | the person: claim to equal access to attendance, urban and rural alike | the Public Power that attends: duty | `art. 4º, IV — o acesso ao atendimento observa a igualdade de direitos` |
| art. 4º, V | the public: claim to be told of benefits, resources and criteria | the Public Power: duty to publicise | `art. 4º, V — a divulgação é ampla` |
| art. 6º-A | none (definition of the two types of protection) | none | `art. 6º-A, incisos I e II — tipos de proteção social…` |
| art. 6º-B §§ 1º, 2º | the entity: power to be recognised as bound to the Suas, once the requirements are met | the Ministry: liability to recognise (its judgement is an input) | `art. 6º-B, § 2º — a entidade cumpre os requisitos…`, `art. 6º-B, § 1º — a entidade é vinculada ao Suas` |
| art. 6º-C | the person: claim to protection in the Cras, the Creas or a non-profit entity | the municipality / State / region managing the unit: duty | `art. 6º-C, caput — unidades em que a proteção é ofertada precipuamente` (§§ 1 to 3 carried as text) |
| art. 6º-D | the user: claim to premises fit for the services, with private reception and accessibility | the unit and its managers: duty | `art. 6º-D — as instalações observam o que a Lei exige` |
| art. 6º-F § 1º | the low-income family: power to register in the CadÚnico at the Cras, the Creas or electronically | the Cras, the Creas and the federal managers: liability to the registration | `art. 6º-F, § 1º — lugares em que a família de baixa renda pode inscrever-se…` |
| art. 6º-F § 2º | the Federal Government: power to make registration mandatory for access to a programme | the person: liability (a duty to register when the regulation says so) | `art. 6º-F, § 2º — a inscrição… é obrigatória…` |
| art. 6º-F § 6º | the managing bodies: power to check the data in other databases | the person: liability (the data are checked) | `art. 6º-F, § 6º — … checagem em outras bases de dados` |
| art. 9º caput | the Council: power to inscribe (the entity may operate only after prior inscription) | the entity: liability (it may not operate before the inscription) | `art. 9º, caput — a entidade pode funcionar` |
| art. 9º § 4º | the entity: power to appeal to the Councils | the Councils: liability to the appeal | `art. 9º, § 4º — a entidade pode recorrer aos Conselhos…` |
| arts. 12 I, 12 III, 13 I, III, V, 14 I to V, 15 I to V | the person/family: claim to the BPC, eventual benefits, services, poverty projects and emergency aid | the Union (BPC; emergencies), the States, the Federal District, the Municipalities: duty | `arts. 12 a 15 — entes federados que respondem pela prestação` |
| art. 19, sole paragraph | the person or family in vulnerability or risk: claim to health care, and immunity from the proof of domicile or SUS registration | the health service: duty to give the care, and disability to demand the proof | `art. 19, parágrafo único — a atenção integral à saúde pode ser condicionada…` |
| art. 20 caput | the applicant (65 or more, or with disability): claim to one minimum wage a month | the Union, through the INSS: duty to grant and pay (arts. 12 I, 29 sole §, 35) | `art. 20, caput — valor mensal…`, `art. 20, caput — idoso…`, `art. 20 — direito ao benefício…` |
| art. 20 § 1º | none (counting rule: who is family) | none | `art. 20, § 1º — vínculo que a Lei exige…`, `art. 20, § 1º — membro da família do requerente` |
| art. 20 §§ 2º, 10 | none (definition of disability and of long term) | none | `art. 20, §§ 2º e 10 — pessoa com deficiência` |
| art. 20 §§ 2º-A, 6º | the INSS: power to make the grant to a person with disability depend on the assessment | the applicant with disability: liability to the assessment (the applicant's claim to be assessed, with the INSS's duty to see to it, is in art. 20 § 6º and art. 40-B) | `art. 20, §§ 2º-A e 6º — a concessão… está sujeita à avaliação`, `art. 40-B, caput — a avaliação provisória foi feita por quem a Lei indica` |
| art. 20 § 3º | the applicant: claim if the per capita income is at most 1/4 of the minimum wage | the INSS: duty | `art. 20, §§ 3º e 3º-A — renda…per capita`, `art. 20, §§ 3º, 11 e 11-A — limite…` |
| art. 20 § 3º-A, § 9º, § 14 | none (counting rules: what enters the income) | none | `art. 20, §§ 3º-A, 9º e 14 — soma dos rendimentos computados`, `art. 20, § 9º…`, `art. 20, § 14…`, `art. 20, § 3º-A — a dedução é admitida…` |
| art. 20 § 4º | the INSS: privilege not to grant while another benefit is received (bar) | the applicant: no-right to the grant while receiving it | `art. 20, § 4º — o outro benefício recebido impede a concessão` |
| art. 20 § 5º | the applicant: immunity from losing the right by living in a long-stay institution | the INSS: disability | `art. 20, § 5º — o acolhimento… prejudica o direito` (FALSE) |
| art. 20 § 7º | the applicant: claim to be referred to the nearest municipality with the structure | the INSS / the Municipality: duty | `art. 20, § 7º — fica assegurado o encaminhamento…` |
| art. 20 § 8º | the INSS: claim to the declaration of income | the applicant or legal representative: duty to declare, and to follow the regulation's procedures | `art. 20, § 8º — a renda familiar mensal foi declarada por quem a Lei indica` |
| art. 20 § 11, § 11-A, art. 20-B | the applicant: claim that the regulation's widening (up to 1/2) and its factors be applied | the Executive (regulation) and the INSS: duty to apply the scales | `art. 20, §§ 3º, 11 e 11-A — limite…`, `art. 20-B, § 2º — fatores aplicáveis…` |
| art. 20 § 12 | the INSS: claim that the CPF and CadÚnico registrations be made and kept, for grant, maintenance and review | the applicant/beneficiary: duty to register and keep the registrations | `art. 20, § 12 — as inscrições exigidas foram feitas`, `art. 20, § 12 — fases do benefício…` |
| arts. 20 §§ 12-A, 12-B | the INSS and the identity registries: claim to the biometric record | the applicant (or the legal guardian): duty to submit it | `arts. 20, §§ 12-A e 12-B — de quem se exige o registro biométrico` |
| art. 20 § 15 | each family member who meets the requirements: claim | the INSS: duty (no one-per-family cap) | `art. 20, § 15 — direito do membro da família…` |
| art. 20 § 16 | the applicant with AIDS: claim to an infectologist in the expert examination | the INSS expert service: duty | `art. 20, § 16 — a perícia médica deve contar com…` |
| art. 20-B §§ 1º, 3º, 4º | none (inputs of the regulation) | none | plain input `Ampliação regulamentar do limite de renda` |
| art. 21 caput | the INSS: power to review the benefit every 2 years | the beneficiary: liability to the review | `art. 21, caput — dia em que o benefício deve ser revisto`, `…a revisão está atrasada` |
| art. 21 § 1º | the INSS: power to stop paying when the conditions are overcome or on death | the beneficiary: liability | `art. 21, § 1º — o pagamento do benefício cessa` |
| art. 21 § 2º | the INSS: power to cancel for irregularity | the beneficiary: liability | `art. 21, § 2º — o benefício é cancelado` |
| art. 21 § 3º | the beneficiary with disability: immunity from suspension or cessation for those developments | the INSS: disability | `art. 21, § 3º — o fato constitui motivo de suspensão ou cessação` |
| art. 21 § 4º | the former beneficiary: claim to a new grant when the requirements are met (the cessation is no bar) | the INSS: duty to grant it | `art. 21, § 4º — a cessação não impede nova concessão` |
| art. 21 §§ 5º, 6º | the beneficiary with permanent impairment: immunity from periodic expert evaluation / review | the INSS: disability (except suspicion of fraud or error, § 5º) | `art. 21, § 5º…`, `art. 21, § 6º…` |
| art. 21-A caput, § 2º | the órgão concedente: power to suspend when the person with disability does paid work; the apprentice: immunity from suspension up to 24 months (§ 2º) | the beneficiary with disability: liability to suspension; the órgão concedente: disability to suspend the apprentice within 24 months | `art. 21-A — o benefício é suspenso pelo órgão concedente` |
| art. 21-A § 1º | the beneficiary: power to ask for the continuation of the suspended benefit without a new expert examination | the INSS: liability | `art. 21-A, § 1º — pode ser requerida a continuidade…` |
| art. 21-B caput, I, II | the INSS and the bank: claim that the CadÚnico be regularised in 45 or 90 days | the beneficiary: duty | `art. 21-B, caput…`, `…incisos I e II — prazo em dias…`, `…último dia…` |
| art. 21-B §§ 1º, 2º | the INSS: power to block the credit (30 days after the notice, without knowledge) and to suspend (knowledge proven) | the beneficiary: liability | `art. 21-B, § 1º — o crédito… é bloqueado`, `art. 21-B, § 2º — o benefício é suspenso` |
| art. 21-B § 3º | the beneficiary: power to regularise until the end of the suspension without loss of payment | the INSS: liability | `art. 21-B, § 3º — a regularização feita nesse dia prejudica…` |
| art. 22 caput, § 1º | the person/family: claim to eventual benefits for birth, death, temporary vulnerability, public calamity | the States, the Federal District, the Municipalities: duty (they fix the grant and the amount) | `art. 22, caput — o evento dá origem…`, `art. 22, § 1º — valor do benefício eventual` |
| art. 22 § 2º | the CNAS: power to propose subsidiary benefits of up to 25% of the minimum wage per child of up to 6 years | the States, the Federal District and the Municipalities: liability to the proposal (they decide whether to institute the benefit, § 1º) | `art. 22, § 2º — valor máximo…` |
| art. 22 § 3º | the payer (State, Federal District, Municipality): privilege not to pay the subsidiary benefit together with those of Leis 10.954/2004 and 10.458/2002 | the person: no-right to receive both | `art. 22, § 3º — o benefício eventual subsidiário pode ser cumulado…` |
| art. 23 § 2º | the groups named: claim to support programmes | the organisers of the services: duty | `art. 23, § 2º — o grupo é destinatário de programa de amparo…` |
| arts. 24-A, 24-B | the family / the individual: claim to the Paif / the Paefi | the Cras / the Creas: duty | `arts. 24-A e 24-B — serviços de proteção…` |
| art. 24-C §§ 1º, 2º | children and adolescents in work: claim to the Peti | the federated entities: duty | `art. 24-C, § 1º…`, `art. 24-C, § 2º…` |
| art. 26-A caput, §§ 1º to 4º | the person with moderate or severe disability who receives (or received) the BPC and starts to work: claim to the auxílio-inclusão | the INSS (operates and pays, art. 26-F), the Ministry of Citizenship (manages) | `art. 26-A — direito ao auxílio-inclusão` and its helpers |
| art. 26-B | the beneficiary: claim to 50% of the BPC from the application (or from the month of the finding); the INSS: power to grant automatically (§ 2º) and to suspend the BPC on the application (§ 1º) | the INSS: duty to pay / the beneficiary: liability to the suspension | `art. 26-B, …` rules |
| art. 26-C | the INSS: privilege not to pay the auxílio-inclusão together with the BPC, pensions or unemployment insurance | the beneficiary: no-right to receive both | `art. 26-C — o auxílio-inclusão pode ser pago em conjunto…` |
| art. 26-D | the INSS: power to stop paying | the beneficiary: liability | `art. 26-D — o pagamento do auxílio-inclusão cessa` |
| art. 26-E | the beneficiary: immunity from contribution deductions; the INSS: privilege not to pay an annual bonus | the INSS: disability to deduct contributions; the beneficiary: no-right to an annual bonus | `art. 26-E — …desconto de contribuição`, `…abono anual` |
| art. 30 | the Municipalities, States, Federal District: claim to the transfers once the Council, Fund and Plan exist | the Union: duty | `art. 30 — o repasse de recursos pode ser feito` and helpers |
| art. 31 | the person: claim that the rights of the Law be watched over | the Public Prosecution Service: duty | `art. 31 — órgão a que cabe zelar…` |
| art. 36 | the public authority: power to cancel the link to the Suas | the entity: liability (civil and criminal liability remains) | `art. 36 — a vinculação… é cancelada` |
| art. 37 caput | the applicant: claim to payment within 45 days after fulfilling the requirements | the INSS: duty | `art. 37, caput — último dia…`, `…o primeiro pagamento foi feito no prazo` |
| art. 37, sole paragraph | the applicant: claim to the same update as the INSS gives to late social-security benefits | the INSS: duty | `art. 37, parágrafo único — valor do primeiro pagamento…` |
| art. 40 caput, § 2º | the person over 70 or invalid: power to request the renda mensal vitalícia until 31 Dec 1995 | the INSS: liability to the request (it must process it) | `art. 40, caput…`, `art. 40, § 2º — é assegurado o direito de requerer…` |
| art. 40-A | the woman responsible for the family unit: claim to receive the monetary benefits of arts. 22, 24-C, 25 in preference | the paying body: duty | `art. 40-A — o benefício monetário é pago preferencialmente…` |
| art. 40-B | the applicant with disability: claim to the assessment by the federal medical expertise and the INSS social service; immunity (secrecy) as to the CID code | the INSS and the federal medical expertise: duty to assess; disability to disclose the CID code | `art. 40-B, caput …` rules, `art. 40-B, § 2º…` |
| art. 40-C | the INSS: power to consign debts from irregular receipt in the monthly value | the beneficiary: liability | `art. 40-C — o débito pode ser consignado…` |
| arts. 28, 41 | none (list of sources of financing; entry into force) | none | `art. 28, caput — fontes de financiamento…`; `lo-datas` |

## Coverage table

Dispositions: `encoded` (in layer 1, and in layer 2 where the person would ask), `inert` (left out, for one of: machinery, an amendment of another instrument, an amendment the source shows as not in force, a pure citation or title), `repealed or blank in this text`, and `fork` (the text does not settle the reading: the row says which reading was encoded, and the entry F-nn in the fork register has the readings seen).
A row that is encoded under a reading from the fork register has the disposition `fork`, not `encoded`; the `where` column names the module and the rule, and the note says what was encoded.
"Carried" below means the provision decides nothing, so layer 1 keeps it as a typed list or a verbatim string (`@@S`-made, `MEANS "…"`) with its `@ref`, and does not call it inert.
Provisions that depend on an instrument outside the text are encoded as far as the text goes and are also listed under "Dependencies".
Superseded wording shown struck through (`⟦STRUCK: …⟧`) is never encoded; the live line beside it is what each row cites.
Text lines: 534; section openers: 85 (42 distinct article numbers in the converter's count, plus the lettered articles below); headings: 15; the table has one row per section/heading and one per subsection wherever the disposition differs.

| provision | source lines | disposition | where | note |
|---|---|---|---|---|
| title block, header and `(Vide …)` lines | src:1-4, 6-13 | inert | none | pure citation or title: the publisher's header, "Texto compilado", "Mensagem de veto", the `(Vide Decreto nº 3.048…)`, `(Vide ADIN nº 2.228)` notes and the long title "Dispõe sobre a organização da Assistência Social" |
| date of the Law | src:5 | encoded | lo-datas: `data da Lei nº 8.742/1993` | 7 December 1993, carried as data; also src:530 |
| enacting formula | src:14 | inert | none | pure citation: "O PRESIDENTE DA REPÚBLICA, faço saber que o Congresso Nacional decreta e eu sanciono a seguinte lei" |
| title "LEI ORGÂNICA DA ASSISTÊNCIA SOCIAL" | src:15 | inert | none | pure title |
| heading CAPÍTULO I — Das Definições e dos Objetivos | src:16-17 | inert | lo-cap1-2-principios (`§` heading) | pure heading |
| art. 1º | src:18 | fork | lo-cap1-2-principios: `art. 1º — o direito à assistência social depende de contribuição prévia do beneficiário` | "não contributiva" ⇒ FALSE; the right/duty pair is in Jural relations; fork F-02 |
| art. 2º, caput, I (a to e), II, III | src:26-34, 19-25 | fork | lo-cap1-2-principios: `art. 2º, caput e incisos — objetivos…` | carried as a typed list of 7 objectives; fork F-02; superseded wording (src:19-25) not encoded |
| art. 2º, parágrafo único | src:35 | encoded | lo-cap1-2-principios: `art. 2º, parágrafo único — garantias…` | carried as a typed list of 3 guarantees |
| art. 3º, caput | src:37, 36 | fork | lo-cap1-2-principios: `art. 3º, caput — entidade ou organização de assistência social` | fork F-01 (non-profit scope); superseded wording src:36 not encoded |
| art. 3º, § 1º | src:38 | encoded | lo-cap1-2-principios: `art. 3º, § 1º — entidade de atendimento` | CNAS deliberations are an input |
| art. 3º, § 2º | src:39 | encoded | lo-cap1-2-principios: `art. 3º, § 2º — entidade de assessoramento` |  |
| art. 3º, § 3º | src:40 | encoded | lo-cap1-2-principios: `art. 3º, § 3º — entidade de defesa e garantia de direitos` |  |
| heading CAPÍTULO II — Dos Princípios e das Diretrizes; SEÇÃO I — Dos Princípios; SEÇÃO II — Das Diretrizes | src:41-44, 51-52 | inert | `§` headings | pure headings |
| art. 4º, caput, I, II | src:45-47 | encoded | lo-cap1-2-principios: `art. 4º — princípios que regem a assistência social` | carried as a typed list of 5 principles |
| art. 4º, III | src:48 | encoded | lo-cap1-2-principios: `art. 4º, III — a comprovação de necessidade exigida é vedada` | seat: art. 4º III question |
| art. 4º, IV | src:49 | encoded | lo-cap1-2-principios: `art. 4º, IV — o acesso ao atendimento observa a igualdade de direitos` |  |
| art. 4º, V | src:50 | encoded | lo-cap1-2-principios: `art. 4º, V — a divulgação é ampla` |  |
| art. 5º, caput, I to III | src:53-56 | inert | none | machinery: directives of organisation (decentralisation, popular participation, primacy of the State); they address the federated entities and create no claim, duty or decision for the person |
| heading CAPÍTULO III — Da Organização e da Gestão | src:57-58 | inert | `§` heading | pure heading |
| art. 6º, caput, I to VII | src:61-68, 59-60 | inert | none | machinery: the Suas and its seven objectives (shared management, co-financing, network integration, levels of management, work management, integrated management, surveillance); superseded src:59-60 not encoded |
| art. 6º, § 1º | src:69 | inert | none | machinery: the actions offered in the Suas aim at protecting family, maternity, childhood, adolescence and old age, territory-based; a purpose of the system |
| art. 6º, § 2º | src:70 | inert | none | machinery: who makes up the Suas (federated entities, Councils, entities) |
| art. 6º, § 3º | src:71 | inert | none | machinery: which ministry coordinates the National Policy |
| art. 6º, §§ 4º, 5º | src:72-73 | inert | none | machinery: the visual identity of the Suas, set by the coordinating body |
| art. 6º-A, caput, I, II | src:74-76 | encoded | lo-cap3-organizacao: `art. 6º-A, incisos I e II — tipos de proteção social que se aplicam à situação` | seat: which type of protection applies |
| art. 6º-A, parágrafo único | src:77 | encoded | lo-cap3-organizacao: `art. 6º-A, parágrafo único — a vigilância socioassistencial` | carried definition (string) |
| art. 6º-B, caput | src:78 | fork | lo-cap3-organizacao: `art. 6º-C, caput — unidades em que a proteção é ofertada precipuamente` is the reading taken; art. 6º-B caput itself has no rule | the network ("rede socioassistencial") through which the protections are offered, directly by public bodies or by bound entities; it overlaps art. 6º-C caput, which says where, and is not modelled separately (only art. 6º-C is): fork F-21 |
| art. 6º-B, § 1º | src:79 | encoded | lo-cap3-organizacao: `art. 6º-B, § 1º — a entidade é vinculada ao Suas` | the Ministry's recognition is an input |
| art. 6º-B, § 2º, I to III | src:80-83 | encoded | lo-cap3-organizacao: `art. 6º-B, § 2º — a entidade cumpre os requisitos…` | cumulative; reuses art. 3º |
| art. 6º-B, § 3º | src:84 | inert | none | machinery: agreements between bound entities and the public power, full State funding within installed capacity and budget |
| art. 6º-B, § 4º | src:85 | inert | none | machinery: reporting from the local managing body to the Ministry |
| art. 6º-C, caput | src:86 | encoded | lo-cap3-organizacao: `art. 6º-C, caput — unidades em que a proteção é ofertada precipuamente` | seat: where the protection is offered |
| art. 6º-C, §§ 1º to 3º | src:87-89 | encoded | lo-cap3-organizacao: `art. 6º-C, § 1º — o Cras`, `§ 2º — o Creas`, `§ 3º — os Cras e os Creas…` | carried definitions (strings) |
| art. 6º-D | src:90 | encoded | lo-cap3-organizacao: `art. 6º-D — as instalações observam o que a Lei exige` | seat: premises of the Cras/Creas |
| art. 6º-E, caput, parágrafo único | src:91-93 | inert | none | machinery: use of co-financing funds to pay staff of the reference teams, and how the teams are formed |
| art. 6º-F, caput | src:96, 94-95 | encoded | lo-cap3-organizacao: `art. 6º-F, caput — o Cadastro Único…` | carried (string); superseded src:94-95 not encoded |
| art. 6º-F, § 1º | src:97 | encoded | lo-cap3-organizacao: `art. 6º-F, § 1º — lugares em que a família de baixa renda pode inscrever-se…` | "baixa renda" and the electronic route are inputs |
| art. 6º-F, § 2º | src:102, 98-101 | encoded | lo-cap3-organizacao: `art. 6º-F, § 2º — …obrigatória para o acesso…` | "poderá ser obrigatória… em regulamento": input; superseded src:98-101 not encoded |
| art. 6º-F, § 3º | src:104, 103 | inert | none | machinery: interoperability of CadÚnico data with the CNIS, between public bodies |
| art. 6º-F, § 4º | src:106, 105 | inert | none | machinery: which management bodies may read the CNIS data, under an adhesion term with a secrecy clause |
| art. 6º-F, § 5º | src:108, 107 | inert | none | machinery: civil society may cooperate in identifying people to register, under the regulation |
| art. 6º-F, § 6º | src:111-112, 109-110 | encoded | lo-cap3-organizacao: `art. 6º-F, § 6º — as informações… checagem em outras bases de dados` | constant TRUE (the data are checked); the Executive act is out of text |
| art. 7º | src:113 | inert | none | machinery: entities observe the norms issued by the CNAS |
| art. 8º | src:114 | inert | none | machinery: each level of government fixes its own policy |
| art. 9º, caput | src:115 | encoded | lo-cap3-organizacao: `art. 9º, caput — a entidade pode funcionar` | entity-facing; no seat question |
| art. 9º, § 1º | src:116 | inert | none | machinery: regulation-making power (criteria for entities operating in more than one municipality or State) |
| art. 9º, § 2º | src:117 | inert | none | machinery: inspection power of the Councils |
| art. 9º, § 3º | src:118-122 | repealed or blank in this text | none | wholly struck, with "(Revogado pela Lei nº 12.101, de 2009)" and "Rejeitada" notes |
| art. 9º, § 4º | src:123 | encoded | lo-cap3-organizacao: `art. 9º, § 4º — a entidade pode recorrer aos Conselhos…` | entity-facing |
| art. 10 | src:124 | inert | none | machinery: power of the federal entities to make agreements with entities in line with Council-approved Plans |
| art. 11 | src:125 | inert | none | machinery: division of coordination and execution among the levels of government |
| art. 12, caput, I | src:126-127 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — entes federados que respondem pela prestação` | the Union answers for the BPC |
| art. 12, II | src:129, 128 | inert | none | machinery: co-financing of management, services, programmes and projects, by automatic transfer; superseded src:128 not encoded |
| art. 12, III | src:130 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | emergency actions, with the States, the Federal District and the Municipalities |
| art. 12, IV | src:131 | inert | none | machinery: monitoring and evaluation of the policy |
| art. 12-A, caput, I to III, §§ 1º, 2º, 4º | src:132-137, 139 | inert | none | machinery: financial support by the IGD (the management index) to the other levels, including that part of the funds supports the Councils |
| art. 12-A, § 3º | src:138 | repealed or blank in this text | none | "(VETADO)" |
| art. 13, caput, I | src:140, 143, 141-142 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | the States fund the Municipalities for the eventual benefits; superseded src:141-142 not encoded |
| art. 13, II | src:144 | inert | none | machinery: co-financing at regional or local level |
| art. 13, III | src:145 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | emergency actions |
| art. 13, IV | src:146 | inert | none | machinery: stimulus and support to municipal associations and consortia |
| art. 13, V | src:147 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | regional services |
| art. 13, VI | src:148 | inert | none | machinery: monitoring and evaluation |
| art. 14, caput, I | src:149, 151, 150 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | the Federal District funds the eventual benefits; superseded src:150 not encoded |
| art. 14, II | src:152 | fork | lo-cap3-organizacao: `arts. 12 a 15 — …` | fork F-07 ("auxílios natalidade e funeral") |
| art. 14, III | src:153 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | poverty-confronting projects |
| art. 14, IV | src:154 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | emergency actions |
| art. 14, V | src:155 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | the services of art. 23 |
| art. 14, VI, VII | src:156-157 | inert | none | machinery: co-financing and monitoring |
| art. 15, caput, I | src:158, 160, 159 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | the Municipalities fund the eventual benefits; superseded src:159 not encoded |
| art. 15, II | src:161 | fork | lo-cap3-organizacao: `arts. 12 a 15 — …` | fork F-07 |
| art. 15, III | src:162 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | poverty-confronting projects |
| art. 15, IV | src:163 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | emergency actions |
| art. 15, V | src:164 | encoded | lo-cap3-organizacao: `arts. 12 a 15 — …` | the services of art. 23 |
| art. 15, VI, VII | src:165-166 | inert | none | machinery: co-financing and monitoring |
| art. 16, caput, I to IV | src:168-172, 167 | inert | none | machinery: the deliberative bodies of the Suas (the Councils); superseded src:167 not encoded |
| art. 16, parágrafo único | src:173 | inert | none | machinery: the managing body must give the Councils infrastructure and pay councillors' travel |
| art. 17, caput, §§ 1º to 4º | src:174-179, 181, 180 | inert | none | machinery: institution, composition (18 members), mandate and secretariat of the CNAS; the State, district and municipal Councils; superseded src:180 not encoded |
| art. 18, caput, I, II, III, IV, V, VI, VIII to XIV | src:182-184, 194-196, 198, 200-206, 185-193, 197 | inert | none | machinery: competences of the CNAS (approve the policy, norm the services, oversee certification, convene the conference, approve the budget, set transfer criteria, oversee the FNAS, publish decisions); superseded src:185-193, 197 not encoded |
| art. 18, VII | src:199 | repealed or blank in this text | none | "(Vetado.)" |
| art. 18, parágrafo único | src:207-210 | repealed or blank in this text | none | struck, "(Revogado pela Medida Provisória nº 446, de 2008)" and "(Revogado pela Lei nº 12.101, de 2009)" |
| art. 19, caput, I to XIV | src:211-225 | inert | none | machinery: competences of the federal coordinating body (coordinate, propose, provide funds for the BPC, budget, transfer, report, advise, train, study, keep the register of entities, articulate, issue acts, submit programmes) |
| art. 19, parágrafo único | src:226-227 | encoded | lo-cap3-organizacao: `art. 19, parágrafo único — a atenção integral à saúde pode ser condicionada…` | seat: health care without proof of domicile or SUS registration; `(Vide ADI 6085)` src:227 is a citation |
| heading CAPÍTULO IV; SEÇÃO I — Do Benefício de Prestação Continuada | src:228-231 | inert | `§` headings | pure headings |
| art. 20, caput | src:246, 232-245 | fork | lo-bpc-concessao: `art. 20, caput — valor mensal…`, `art. 20, caput — idoso com 65 anos ou mais`, `art. 20 — direito ao benefício de prestação continuada` | minimum wage is an input; superseded src:232-245 (70 years, old family definition…) not encoded; fork F-03 |
| art. 20, § 1º | src:247 | encoded | lo-bpc-concessao: `art. 20, § 1º — vínculo que a Lei exige…`, `art. 20, § 1º — membro da família do requerente` | a stepparent counts only if one parent is absent |
| art. 20, § 2º | src:252, 248-251 | encoded | lo-bpc-concessao: `art. 20, §§ 2º e 10 — pessoa com deficiência` | superseded src:248-251 not encoded |
| art. 20, § 2º-A | src:253-254 | encoded | lo-bpc-concessao: `art. 20, §§ 2º-A e 6º — a concessão… está sujeita à avaliação` | "nos termos de regulamento": input |
| art. 20, § 2º-B | src:255-256 | repealed or blank in this text | none | "(VETADO)" |
| art. 20, § 3º, caput | src:261, 257-260, 262-266 | fork | lo-bpc-concessao: `art. 20, §§ 3º e 3º-A — renda…per capita`, `art. 20, §§ 3º, 11 e 11-A — limite…` | 1/4 of the minimum wage, "igual ou inferior"; superseded src:257-260, 262-266 not encoded; fork F-04 |
| art. 20, § 3º, I, II | src:267-269 | repealed or blank in this text | none | "I – (revogado)" and "II - (VETADO)" |
| art. 20, § 3º-A | src:270-271 | fork | lo-bpc-concessao: `art. 20, §§ 3º-A, 9º e 14 — soma dos rendimentos computados`, `art. 20, § 3º-A — a dedução é admitida…` | "ato do Poder Executivo federal" is out of text; fork F-20 |
| art. 20, § 4º | src:273, 272 | encoded | lo-bpc-concessao: `art. 20, § 4º — o outro benefício recebido impede a concessão` | superseded src:272 not encoded |
| art. 20, § 5º | src:275, 274 | encoded | lo-bpc-concessao: `art. 20, § 5º — o acolhimento… prejudica o direito` | superseded src:274 not encoded |
| art. 20, § 6º | src:277, 276 | fork | lo-bpc-concessao: `art. 20, §§ 2º-A e 6º…`, `art. 20, caput e § 6º — requisito de idade ou de deficiência avaliada` | overlaps art. 40-B: fork F-08; superseded src:276 not encoded |
| art. 20, § 6º-A | src:278 | inert | none | machinery: the INSS may make partnerships to carry out the social assessment under its social service |
| art. 20, § 7º | src:279 | encoded | lo-bpc-concessao: `art. 20, § 7º — fica assegurado o encaminhamento…` |  |
| art. 20, § 8º | src:280 | fork | lo-bpc-concessao: `art. 20, § 8º — a renda familiar mensal foi declarada por quem a Lei indica` | fork F-20 |
| art. 20, § 9º | src:283, 281-282 | encoded | lo-bpc-concessao: `art. 20, § 9º — o valor recebido não é computado…`, and in the sum | superseded src:281-282 not encoded |
| art. 20, § 10 | src:284 | encoded | lo-bpc-concessao: `art. 20, §§ 2º e 10 — pessoa com deficiência` | 2 years |
| art. 20, § 11 | src:285 | encoded | lo-bpc-concessao: `art. 20, §§ 3º, 11 e 11-A — limite…` | other proof of misery "conforme regulamento": the plain input `Ampliação regulamentar do limite de renda` |
| art. 20, § 11-A | src:286-287 | fork | lo-bpc-concessao: `art. 20, §§ 3º, 11 e 11-A — limite…` | widening up to 1/2, per the regulation; "(Vigência)" marker: fork F-05 |
| art. 20, § 12 | src:289, 288 | encoded | lo-bpc-concessao: `art. 20, § 12 — as inscrições exigidas foram feitas`, `…fases do benefício…` | superseded src:288 not encoded |
| art. 20, § 12-A | src:290-291 | fork | lo-bpc-concessao: `arts. 20, §§ 12-A e 12-B — de quem se exige o registro biométrico` | no consequence is stated for not submitting it (fork F-13) |
| art. 20, § 12-A, former parágrafo único | src:292-294 | repealed or blank in this text | none | struck, "(Revogado pela Lei nº 15.077, de 2024)" |
| art. 20, § 12-B | src:295-296 | encoded | lo-bpc-concessao: `arts. 20, §§ 12-A e 12-B…` |  |
| art. 20, § 13 | src:297-299 | repealed or blank in this text | none | wholly struck (consent to access bank data) |
| art. 20, § 14 | src:300 | fork | lo-bpc-concessao: `art. 20, § 14 — o benefício de outro membro da família não é computado na renda` | "acima de 65": fork F-06 |
| art. 20, § 15 | src:301 | encoded | lo-bpc-concessao: `art. 20, § 15 — direito do membro da família quando outro membro… recebe` |  |
| art. 20, § 16 | src:302 | encoded | lo-bpc-concessao: `art. 20, § 16 — a perícia médica deve contar com… infectologia` |  |
| art. 20-A, caput, §§ 1º to 4º | src:303-335 | repealed or blank in this text | none | wholly struck, "(Revogado pela Lei nº 14.176, de 2021)" on every part |
| art. 20-B, caput, I to III | src:336-340 | encoded | lo-bpc-concessao: `art. 20-B, § 2º — fatores aplicáveis à pessoa`, and the input | the three factors are the constructors of `Fator de ampliação do limite de renda` |
| art. 20-B, § 1º | src:341-342 | encoded | plain input `Ampliação regulamentar do limite de renda` (lo-nouns) | graded scales are "definidas em regulamento" (out of text) |
| art. 20-B, § 2º | src:343 | encoded | lo-bpc-concessao: `art. 20-B, § 2º — fatores aplicáveis à pessoa` |  |
| art. 20-B, § 3º | src:344-345 | encoded | plain input `grau da deficiência` (lo-nouns, `Grau da deficiência`) and `Ampliação…` | the biopsychosocial instrument of Lei nº 13.146 is out of text |
| art. 20-B, § 4º | src:346-347 | encoded | lo-nouns: plain input `Ampliação regulamentar do limite de renda` | the value of the health spending is set by a joint act (out of text) |
| art. 21, caput | src:348 | fork | lo-bpc-manutencao: `art. 21, caput — dia em que o benefício deve ser revisto`, `…a revisão está atrasada` | fork F-15 |
| art. 21, § 1º | src:349 | fork | lo-bpc-manutencao: `art. 21, § 1º — o pagamento do benefício cessa` | fork F-09 |
| art. 21, § 2º | src:350 | encoded | lo-bpc-manutencao: `art. 21, § 2º — o benefício é cancelado` |  |
| art. 21, § 3º | src:351 | fork | lo-bpc-manutencao: `art. 21, § 3º — o fato constitui motivo de suspensão ou cessação` | "entre outras" ⇒ "o texto não responde" for other facts; fork F-17 |
| art. 21, § 4º | src:353, 352 | encoded | lo-bpc-manutencao: `art. 21, § 4º — a cessação não impede nova concessão` | superseded src:352 not encoded |
| art. 21, § 5º | src:355, 354 | encoded | lo-bpc-manutencao: `art. 21, § 5º — … dispensado de avaliação médico-pericial periódica` | superseded src:354 not encoded |
| art. 21, § 6º | src:356 | encoded | lo-bpc-manutencao: `art. 21, § 6º — a revisão… é dispensada` |  |
| art. 21-A, caput | src:357 | encoded | lo-bpc-manutencao: `art. 21-A — o benefício é suspenso pelo órgão concedente` | elderly beneficiaries: outside the text |
| art. 21-A, § 1º | src:358 | encoded | lo-bpc-manutencao: `art. 21-A, § 1º — pode ser requerida a continuidade…` |  |
| art. 21-A, § 2º | src:359 | fork | lo-bpc-manutencao: `art. 21-A — …` | fork F-10 |
| art. 21-B, caput, I, II | src:363-368, 360-362 | fork | lo-bpc-manutencao: `art. 21-B, caput — o beneficiário deve regularizar…`, `…incisos I e II — prazo em dias…`, `…último dia…` | 24 months, 45/90 days, 50,000: fork F-11; superseded src:360-362 (48 months) not encoded |
| art. 21-B, § 1º | src:369-370 | fork | lo-bpc-manutencao: `art. 21-B, § 1º — o crédito do benefício é bloqueado` | fork F-12 |
| art. 21-B, § 2º | src:371-372 | encoded | lo-bpc-manutencao: `art. 21-B, § 2º — o benefício é suspenso` |  |
| art. 21-B, § 3º | src:373-374 | fork | lo-bpc-manutencao: `art. 21-B, § 3º — a regularização feita nesse dia prejudica…` | fork F-12 |
| heading SEÇÃO II — Dos Benefícios Eventuais | src:375-376 | inert | `§` heading | pure heading |
| art. 22, caput | src:381, 377-380 | fork | lo-eventuais-servicos: `art. 22, caput — o evento dá origem a benefício eventual` | superseded src:377-380 not encoded; fork F-17 |
| art. 22, § 1º | src:382 | encoded | lo-eventuais-servicos: `art. 22, § 1º — valor do benefício eventual, em reais` | grant and amount fixed by State/DF/Municipality: inputs |
| art. 22, § 2º | src:383 | encoded | lo-eventuais-servicos: `art. 22, § 2º — valor máximo do benefício eventual subsidiário por criança, em reais` | 25% of the minimum wage, up to 6 years |
| art. 22, § 3º | src:384 | encoded | lo-eventuais-servicos: `art. 22, § 3º — o benefício eventual subsidiário pode ser cumulado…` | Leis 10.954/2004 and 10.458/2002 are out of text |
| heading SEÇÃO III — Dos Serviços | src:385-386 | inert | `§` heading | pure heading |
| art. 23, caput | src:392, 387-391 | encoded | lo-eventuais-servicos: `art. 23, caput — os serviços socioassistenciais` | carried definition (string); superseded src:387-391 not encoded |
| art. 23, § 1º | src:393 | inert | none | machinery: regulation-making power ("O regulamento instituirá os serviços socioassistenciais") |
| art. 23, § 2º, I to III | src:394-397 | fork | lo-eventuais-servicos: `art. 23, § 2º — o grupo é destinatário de programa de amparo…` | "entre outros": other groups not covered; fork F-17 |
| heading SEÇÃO IV — Dos Programas de Assistência Social | src:398-399 | inert | `§` heading | pure heading |
| art. 24, caput | src:400 | encoded | lo-eventuais-servicos: `art. 24, caput — os programas de assistência social` | carried definition (string) |
| art. 24, § 1º | src:401 | inert | none | machinery: the Councils define the programmes |
| art. 24, § 2º | src:403, 402 | inert | none | machinery: articulation of the programmes for the elderly and for the integration of persons with disability with the BPC; superseded src:402 not encoded |
| art. 24-A, caput | src:404 | encoded | lo-eventuais-servicos: `arts. 24-A e 24-B — serviços de proteção que se aplicam à situação` |  |
| art. 24-A, parágrafo único | src:405 | inert | none | machinery: regulation-making power (guidelines of the Paif) |
| art. 24-B, caput | src:406 | encoded | lo-eventuais-servicos: `arts. 24-A e 24-B — …` |  |
| art. 24-B, parágrafo único | src:407 | inert | none | machinery: regulation-making power (guidelines of the Paefi) |
| art. 24-C, caput | src:408 | encoded | lo-eventuais-servicos: `art. 24-C, caput — o Programa de Erradicação do Trabalho Infantil (Peti)` | carried definition (string) |
| art. 24-C, § 1º | src:409 | encoded | lo-eventuais-servicos: `art. 24-C, § 1º — a criança ou o adolescente está no objetivo de retirada…` | under 16; apprentices from 14 excepted |
| art. 24-C, § 2º | src:410 | fork | lo-eventuais-servicos: `art. 24-C, § 2º — os dados da criança ou do adolescente devem ser inseridos no Cadastro Único…` | fork F-16 |
| heading SEÇÃO V — Dos Projetos de Enfrentamento da Pobreza | src:411-412 | inert | `§` heading | pure heading |
| art. 25 | src:413 | encoded | lo-eventuais-servicos: `art. 25 — os projetos de enfrentamento da pobreza` | carried definition (string) |
| art. 26 | src:414 | inert | none | machinery: the incentive to the projects rests on articulation mechanisms among governmental and non-governmental bodies |
| heading Seção VI — Do Auxílio-Inclusão | src:415-417 | inert | `§` heading | pure heading; the line "(Incluído pela Lei nº 14.176, de 2021) (Vigência)" under it is a citation, and the "(Vigência)" marker itself is discussed in fork F-14 |
| art. 26-A, caput, I a III | src:418-424 | fork | lo-auxilio-inclusao: `art. 26-A, caput — pessoa com deficiência moderada ou grave`, `art. 26-A, caput, inciso I…`, `art. 26-A — direito ao auxílio-inclusão` | the grade of disability is an input; fork F-03 |
| art. 26-A, caput, IV | src:425-426 | encoded | lo-auxilio-inclusao: `art. 26-A — direito ao auxílio-inclusão` (calls art. 20) |  |
| art. 26-A, § 1º | src:427-429 | fork | lo-auxilio-inclusao: `art. 26-A, § 1º — recebeu o benefício nos 5 anos imediatamente anteriores…` | fork F-13 |
| art. 26-A, § 2º | src:430 | encoded | lo-auxilio-inclusao: `art. 26-A, §§ 2º e 4º — renda familiar considerada…` |  |
| art. 26-A, § 3º | src:431 | encoded | lo-auxilio-inclusao: `art. 26-A, § 3º — renda familiar considerada para manter o benefício…` |  |
| art. 26-A, § 4º, I, II | src:432-434 | encoded | lo-auxilio-inclusao: `art. 26-A, §§ 2º e 4º — …` |  |
| art. 26-B, caput | src:435-436 | encoded | lo-auxilio-inclusao: `art. 26-B, caput — valor mensal do auxílio-inclusão, em reais`, `arts. 26-B, caput e § 3º — dia a partir do qual…` | 50% of the BPC |
| art. 26-B, § 1º | src:437 | encoded | lo-auxilio-inclusao: `art. 26-B, § 1º — o requerimento autoriza a suspensão…` |  |
| art. 26-B, § 2º | src:438 | encoded | lo-auxilio-inclusao: `art. 26-B, § 2º — o INSS concede o auxílio-inclusão automaticamente` |  |
| art. 26-B, § 3º | src:439 | encoded | lo-auxilio-inclusao: `arts. 26-B, caput e § 3º…`, `art. 26-B, § 3º — o titular deve ser notificado…` |  |
| art. 26-C, caput, I to III | src:440-444 | encoded | lo-auxilio-inclusao: `art. 26-C — o auxílio-inclusão pode ser pago em conjunto…` |  |
| art. 26-D, caput, I, II | src:445-448 | encoded | lo-auxilio-inclusao: `art. 26-D — o pagamento do auxílio-inclusão cessa` |  |
| art. 26-D, parágrafo único | src:449 | inert | none | machinery: regulation-making power (the procedure to verify the criteria) |
| art. 26-E | src:450-451 | encoded | lo-auxilio-inclusao: `art. 26-E — …desconto de contribuição`, `…abono anual` |  |
| art. 26-F | src:452-453 | encoded | lo-auxilio-inclusao: `art. 26-F — órgão a que compete a gestão…`, `…operacionalização e o pagamento…` |  |
| art. 26-G, caput | src:454-455 | inert | none | machinery: the expense is charged to the budget of the Ministry |
| art. 26-G, § 1º | src:456 | inert | none | machinery: the Executive must match the number of auxílio-inclusão benefits to the existing budget appropriations; it is a duty of budget administration addressed to the Executive and states no rule for the person; whether it could cap grants is not said, which is the open question of fork F-14 (no cap is encoded) |
| art. 26-G, § 2º | src:457 | inert | none | machinery: the regulation names the body that evaluates the impact of the benefit |
| art. 26-H | src:458-459 | encoded | lo-auxilio-inclusao: `art. 26-H — último dia do prazo de 10 anos…` | the publication date of the Seção is an input |
| heading CAPÍTULO V — Do Financiamento da Assistência Social | src:460-461 | inert | `§` heading | pure heading |
| art. 27 | src:462 | inert | none | machinery: the Funac is transformed into the FNAS (an institutional change of a fund) |
| art. 28, caput | src:463 | encoded | lo-cap5-financiamento: `art. 28, caput — fontes de financiamento…` | typed list of 6 sources |
| art. 28, § 1º | src:465, 464 | inert | none | machinery: the body that manages the Fund, under the Council's guidance; superseded src:464 not encoded |
| art. 28, § 2º | src:466 | fork | lo-datas: `art. 28, § 2º — último dia do prazo do Poder Executivo para dispor sobre o FNAS` | 180 days from publication: a date, not machinery; fork F-19 |
| art. 28, § 3º | src:467 | inert | none | machinery: financing by co-financing of the three federated entities |
| art. 28-A | src:468 | repealed or blank in this text | none | wholly struck, "(Revogado pela Lei nº 13.813, de 2019)" |
| art. 29, caput | src:469 | inert | none | machinery: automatic transfer of the Union's funds to the FNAS |
| art. 29, parágrafo único | src:470 | encoded | lo-cap6-gerais: `arts. 29, parágrafo único, e 35, caput — órgãos que executam e operam…` | the INSS is the body that executes and maintains the BPC |
| art. 30, caput, I to III | src:471-474 | encoded | lo-cap5-financiamento: `art. 30, caput — as condições para os repasses estão cumpridas` | entity-facing; no seat question |
| art. 30, parágrafo único | src:475 | encoded | lo-cap5-financiamento: `art. 30, parágrafo único — …`, `art. 30 — o repasse de recursos pode ser feito` | from the fiscal year 1999 |
| art. 30-A, caput, parágrafo único | src:476-477 | inert | none | machinery: co-financing by automatic transfers between funds |
| art. 30-B | src:478 | inert | none | machinery: control by the entity that uses the Fund's resources |
| art. 30-C, caput, parágrafo único | src:479-481 | inert | none | machinery: annual management report by the receiving entities to the transferring entity |
| heading CAPÍTULO VI — Das Disposições Gerais e Transitórias | src:482-483 | inert | `§` heading | pure heading |
| art. 31 | src:484 | encoded | lo-cap6-gerais: `art. 31 — órgão a que cabe zelar…` | |
| art. 32, caput | src:485 | fork | lo-datas: `art. 32 — último dia do prazo…` | 60 days from publication; fork F-19 |
| art. 32, §§ 1º, 2º | src:486-487 | inert | none | machinery: content of the bill and the commission that drafts it (transitional) |
| art. 33, caput | src:488 | fork | lo-datas: `art. 33 — último dia do prazo de 120 dias…`, `…já está extinto em` | 120 days from the promulgation (7 Dec 1993); the repeal of two Decretos-Lei is an amendment of other instruments; fork F-19 |
| art. 33, §§ 1º, 2º | src:489-490 | inert | none | machinery: installation of the CNAS and transfer of the CNSS assets (transitional) |
| art. 34 | src:491 | fork | lo-datas: `art. 34 — fim do prazo máximo do papel supletivo da União` | 12 months from publication; fork F-19 |
| art. 35, caput | src:492 | encoded | lo-cap6-gerais: `arts. 29, parágrafo único, e 35, caput…` | |
| art. 35, § 1º | src:494-495, 493 | inert | none | machinery: regulation-making power (forms of proof, suspension, guardianship, accreditation, payment, inspection); superseded src:493 not encoded |
| art. 35, § 2º | src:496-497 | inert | none | machinery: federal bodies make their databases available, under an Executive act |
| art. 36 | src:499, 498 | encoded | lo-cap6-gerais: `art. 36 — a vinculação… é cancelada`, `…a responsabilidade civil e penal permanece` | entity-facing; superseded src:498 not encoded |
| art. 37, caput | src:503, 500-502 | fork | lo-bpc-concessao: `art. 37, caput — último dia para o primeiro pagamento`, `…o primeiro pagamento foi feito no prazo` | 45 days, inclusive: fork F-15; superseded src:500-502 not encoded |
| art. 37, parágrafo único | src:504 | encoded | lo-bpc-concessao: `art. 37, parágrafo único — valor do primeiro pagamento…` | the INSS criterion is an input |
| art. 38 | src:505-507 | repealed or blank in this text | none | struck, "(Revogado pela Lei nº 12.435, de 2011)" |
| art. 39 | src:508 | inert | none | machinery: the CNAS may propose to the Executive a change of the income limits of art. 20 § 3º and art. 22 caput; finding 2 |
| art. 40, caput | src:509 | encoded | lo-cap6-gerais: `art. 40, caput — o benefício previdenciário está extinto` | the extinction of three social-security benefits is also an effect on another instrument (Lei nº 8.213); encoded because it answers a question a person would ask |
| art. 40, § 1º | src:511, 510 | inert | none | machinery: transitional (the Executive must arrange the transfer of beneficiaries from social security to social assistance without interruption); superseded src:510 not encoded |
| art. 40, § 2º | src:512 | fork | lo-cap6-gerais: `art. 40, § 2º — é assegurado o direito de requerer a renda mensal vitalícia`; lo-datas: `art. 40, § 2º — último dia…` | spent since 31 Dec 1995 but encoded; fork F-18 |
| art. 40-A | src:513 | encoded | lo-cap6-gerais: `art. 40-A — o benefício monetário é pago preferencialmente…` | |
| art. 40-B, caput | src:517-518, 514-516 | fork | lo-bpc-concessao: `art. 40-B, caput — …` (four rules) | fork F-08; superseded src:514-516 not encoded |
| art. 40-B, § 1º | src:521-523, 519-520 | inert | none | machinery: the INSS may make partnerships for the social assessment (same power as art. 20 § 6º-A); superseded src:519-520 not encoded |
| art. 40-B, § 2º | src:524-525 | encoded | lo-bpc-concessao: `art. 40-B, § 2º — a avaliação médica pode ser feita por telemedicina…` | the regulation's conditions are an input |
| art. 40-C | src:526-527 | encoded | lo-bpc-manutencao: `art. 40-C — o débito pode ser consignado…` | the regulation is an input |
| art. 41 | src:528 | encoded | lo-datas: `art. 41 — data de entrada em vigor da Lei nº 8.742/1993` | in force on the date of publication (8 Dec 1993, src:533) |
| art. 42 | src:529 | inert | none | an amendment of other instruments: "Revogam-se as disposições em contrário" repeals contrary provisions of other laws |
| closing lines: place, date, signatures | src:530-532 | inert | none | pure citation: place and date (the date itself is in lo-datas), the President and the Minister who sign |
| footer "Este texto não substitui o publicado no DOU de 8.12.1993" and the stray asterisk | src:533-534 | encoded | lo-datas: `data da publicação da Lei nº 8.742/1993` | src:533 gives the date of publication (8 Dec 1993); src:534 is a stray character |

**Counts.**
Articles in the text (lettered siblings counted separately): 71 (68 have a live opening line; arts. 20-A, 28-A and 38 are wholly struck).
Every one has at least one row (checked by script against the first column).
Headings (CAPÍTULO, SEÇÃO, Seção): 14; each is in a row.
Source lines: 534; every line is inside some row's `source lines` (checked by script; no line is in two rows).
The table has 214 rows: 98 `encoded`, 33 `fork`, 72 `inert`, 11 `repealed or blank in this text`.
The 33 `fork` rows carry 20 of the 21 register entries; F-14 (the "(Vigência)" marker on Seção VI and the budget clause of art. 26-G § 1º) is carried by two `inert` rows, because neither encodes a reading.

## Fork register

Where I looked for ambiguity: date at which each condition is tested; cumulative or alternative conditions; overlaps between provisions; every deference to a regulation, an order or another law that is not among the inputs; every "poderá", "entre outros", "até", "acima de", "igual ou inferior" and "mais de"; the cross-references to provisions that were rewritten; the `(Vigência)`, `(Regulamento)` and `(Vide …)` notes.

| id | provision | readings seen | reading taken | text that licenses it |
|---|---|---|---|---|
| F-01 | art. 3º caput | (a) "sem fins lucrativos" qualifies all three kinds of entity, so a for-profit organisation of defence of rights is not an entity of the Law; (b) it qualifies only attendance and advisory, and "as que atuam na defesa e garantia de direitos" may be for profit | (a) | the caput is "aquelas sem fins lucrativos que… bem como as que atuam…"; art. 6º-C speaks of "entidades sem fins lucrativos de assistência social de que trata o art. 3º"; the struck wording (src:36) placed "sem fins lucrativos" after "prestam", which was reading (b), and was replaced. Asserted. |
| F-02 | arts. 1º, 2º, 4º I-II | (a) statements of aims are claims the person can enforce; (b) they are programme statements | (b) for the aims, which are carried as typed lists; the operative bits are rules (art. 1º "não contributiva", art. 4º III prohibition, IV equality, V publicity) | "Art. 2º A assistência social tem por objetivos"; "Art. 4º … rege-se pelos seguintes princípios" |
| F-03 | arts. 20, 26-A (date of testing) | the age, the disability, the income and the registrations could be tested at the application, at the decision, at each payment | the facts are taken as of the moment the question is asked; the text fixes a date only in art. 26-A II ("no momento do requerimento"), art. 26-A § 1º (5 years before the activity), art. 21-B (24 months; the notification) and art. 37 (the day the requirements were fulfilled), which are encoded | no provision says when age or income is measured |
| F-04 | art. 20 caput, § 3º | the income limit is (a) the only criterion of "não possuir meios", (b) one of several cumulative criteria | (b): cumulative with age or disability, the § 4º bar, the § 12 registrations, and, for disability, the § 6º assessment | § 3º opens "Observados os demais critérios de elegibilidade definidos nesta Lei, terão direito…" |
| F-05 | art. 20 §§ 11, 11-A, 20-B | (a) the regulation may widen the limit; (b) the widened limit applies by itself; plus the "(Vigência)" marker that the compilation prints on art. 20 § 2º, § 11, § 11-A and art. 20-B (src:252, 285, 287, 337-347), which the text does not explain | the widened limit that applies to the person is a plain input; below 1/4 it does not widen (stays 1/4); above 1/2 it is cut at 1/2; the provisions are encoded as in force | § 11-A "poderá ampliar… para até 1/2 (meio) salário-mínimo"; the regulation is not among the inputs. Asserted. |
| F-06 | art. 20 § 14 | the family member's benefit is not counted when the holder is (a) "acima de 65" (more than 65) or (b) 65 or more (as in the caput) | (a): at exactly 65 it is counted | § 14: "idoso acima de 65 (sessenta e cinco) anos"; caput: "65 (sessenta e cinco) anos ou mais". Asserted. |
| F-07 | arts. 14 II, 15 II vs. art. 22 | "efetuar o pagamento dos auxílios natalidade e funeral" still stands in two live lines though art. 22 caput now speaks of benefits "em virtude de nascimento, morte…" | read as the same benefits: the Federal District and the Municipalities pay the eventual benefits for birth and death | arts. 14 I and 15 I, rewritten in 2011, speak of "os benefícios eventuais de que trata o art. 22" |
| F-08 | art. 20 § 6º vs. art. 40-B caput | both say who assesses the disability: "médicos peritos e assistentes sociais do INSS" vs. "perícia médica federal e serviço social do INSS" | one requirement of fact (the medical and social assessment done); art. 20 caput/§ 6º is the condition of the grant, and art. 40-B adds who performs it while the instrument is not regulated and the mandatory, secret CID record | the text says nothing about which prevails |
| F-09 | arts. 21 § 1º, § 2º, 21-A, 21-B §§ 1º, 2º | cessation, cancellation, suspension and blocking may overlap; no rank | each answered on its own; several may hold at once | no provision ranks them |
| F-10 | art. 21-A § 2º | after the 2 years of concurrent receipt by an apprentice: (a) the caput suspends; (b) nothing is said | (a) the caput applies | "limitado a 2 (dois) anos o recebimento concomitante"; 24 months in, 25 out. Asserted. |
| F-11 | art. 21-B I, II | "Municípios de pequeno porte" is not defined; II gives "acima de 50.000 habitantes" for medium, large and metropolis | small = 50,000 inhabitants or fewer | the complement of II. Asserted. |
| F-12 | art. 21-B § 1º, § 3º | (a) "em 30 dias após o envio" blocks on the 30th day or (b) after it; the "prazo de suspensão" has no length in the text | (a) from day 30; the last day of the suspension period is an input | § 1º; § 3º "até o final do prazo de suspensão". Asserted. |
| F-13 | art. 26-A § 1º; art. 20 §§ 12-A | (a) "poderá ainda ser concedido" is a right to the benefit once the facts hold; (b) a discretion of the INSS; "5 anos imediatamente anteriores" read as the last receipt within 5 years before the start of the activity; biometrics "será solicitado" has no stated consequence if not submitted | (a); the 5-year window is [start − 5 years, start], both ends in; no consequence is added for biometrics | caput "terá direito"; § 1º "poderá ainda ser concedido, nos termos do inciso I". Asserted (window). |
| F-14 | Seção VI "(Vigência)"; art. 26-G § 1º | the compilation prints "(Vigência)" on the Seção VI heading and on arts. 26-A to 26-H (9 lines in src:415-459), and art. 26-G § 1º says the Executive will match the number of benefits to the budget | encoded as in force and without a cap on grants | no provision gives a cap; any cap would be invented |
| F-15 | art. 37 caput; art. 21 caput | "em até 45 dias" counted from when the requirements are fulfilled, inclusive or not; "a cada 2 anos" overdue on or after the anniversary | the 45th day is in time, the 46th is late; the review is overdue the day after the 2-year anniversary | "em até quarenta e cinco dias". Asserted. |
| F-16 | art. 24-C §§ 1º, 2º | § 1º limits the withdrawal objective to under 16; § 2º speaks of all children and adolescents "em situação de trabalho" | § 2º as written: every child or adolescent in work is entered, apprentices included | the two paragraphs differ in subject |
| F-17 | art. 22 caput; art. 23 § 2º; art. 21 § 3º | the list in art. 22 caput is closed ("em virtude de…"); the lists of art. 23 § 2º and art. 21 § 3º are open ("entre outros") | art. 22: other events do not give rise to an eventual benefit; arts. 23 § 2º and 21 § 3º: other groups or facts: "o texto não responde" | the words "entre outros" / "entre outras" appear only in the latter |
| F-18 | art. 40 § 2º | "maior de setenta anos" is more than 70; "inválido" is a status the person states; the three alternative requirements of Lei nº 8.213 art. 139 § 1º are out of text | more than 70 (71 or more) or invalid, plus the input | wording; the date of 31 Dec 1995 has passed (so a request today is out of time). Asserted. |
| F-19 | arts. 28 § 2º, 32, 33, 34 | counted from "publicação" (8 Dec 1993) except art. 33, which counts from "promulgação" (7 Dec 1993) | the two dates are used as the words say | the Law's date (src:5, 530) and the DOU footer (src:533). Asserted. |
| F-20 | art. 20 § 8º vs. §§ 3º-A, 9º, 14 | the income "deverá ser declarada" by the applicant, but § 3º-A says the Executive act sets how the income is calculated and forbids deductions "não previstas em lei" | the calculation follows § 3º-A, § 9º and § 14 literally; deductions are admitted only if a law provides them | the text of § 3º-A |
| F-21 | arts. 6º-B caput and 6º-C caput | both say where and by whom the protections are offered: 6º-B caput "pela rede socioassistencial, de forma integrada, diretamente pelos entes públicos e/ou pelas entidades… vinculadas ao Suas", 6º-C caput "precipuamente no Centro de Referência de Assistência Social (Cras) e no Centro de Referência Especializado de Assistência Social (Creas)" | art. 6º-C is modelled (where the protection is offered); the network of art. 6º-B caput is not modelled, and nothing in layer 1 depends on it | neither line ranks the other, and "precipuamente" (mainly) leaves room for the wider network |

## Dependencies on instruments outside the text

The Law cites many other instruments (the `Vide` notes). None is among the inputs, so each fact that depends on one is a plain input, and the comment `-- out of text: <instrument> <provision>` sits above its declaration in layer 1 (16 such comments in the layer-1 modules, plus the ones in `lo-seat.l4`).

| your provision | the provision it depends on | the input you made |
|---|---|---|
| art. 20 caput, § 3º, § 11-A; art. 22 § 2º; art. 26-A I a); art. 26-B | Constituição Federal art. 7º IV and the yearly decree that fixes the minimum wage | `salário-mínimo` / `valor do salário-mínimo` (reais per month) |
| art. 20 § 3º-A | the Executive act that sets how the family income is calculated | none: the formula of § 3º-A, § 9º, § 14 is followed literally (fork F-20) |
| art. 20 § 4º | Constituição art. 6º sole paragraph and art. 203 VI; Lei nº 10.835/2004 art. 1º caput and § 1º | the constructor `transferência de renda do parágrafo único do art. 6º…` of `Outro benefício recebido` |
| art. 20 §§ 2º-A, 6º, 12, 12-A | the regulation of the assessment, of the registrations and of the biometric record; Lei nº 13.146/2015 art. 2º §§ 1º, 2º | `avaliação médica e social da deficiência realizada`; `inscrição no Cadastro de Pessoas Físicas`; `inscrição no Cadastro Único`; `impossibilidade de registro biométrico` |
| art. 20 §§ 11, 11-A; art. 20-B §§ 1º, 3º, 4º | the regulation (graded scales); the biopsychosocial instrument of Lei nº 13.146 art. 2º §§ 1º, 2º; the joint act on the value of health spending | `Ampliação regulamentar do limite de renda` (widened limit as a fraction of the minimum wage) |
| art. 21 § 4º | the regulation (requirements for a new grant) | `requisitos definidos em regulamento atendidos` |
| art. 21-A § 1º | the rules of the unemployment insurance (the period of payment) | `ainda corre o prazo de pagamento do seguro-desemprego` |
| art. 21-B | the Cadastro Único; the notification channels | `inscrito no Cadastro Único`, `meses desde a última atualização do cadastro`, `população do município`, `dia da efetiva notificação`, `último dia do prazo de suspensão` |
| art. 22 § 1º | the laws of the States, the Federal District and the Municipalities and the criteria of their Councils | `há valor definido pelo Estado, pelo Distrito Federal ou pelo Município`, `valor definido, em reais` |
| art. 22 § 3º | Lei nº 10.954/2004; Lei nº 10.458/2002 | `recebe benefício instituído pela Lei nº 10.954/2004`, `… nº 10.458/2002` |
| art. 26-A caput | Lei nº 13.146/2015 art. 94 and the assessment of the grade of disability | `Grau da deficiência` |
| art. 26-H | the date of publication of the Seção VI (Lei nº 14.176/2021) | `dia da publicação da Seção VI` |
| art. 37 parágrafo único | the INSS criterion for updating late first payments of social-security benefits | `índice de atualização` |
| art. 40 § 2º | Lei nº 8.213/1991 art. 139 § 1º I to III | `atende a um dos requisitos dos incisos I, II ou III do § 1º do art. 139 da Lei nº 8.213/1991` |
| art. 40-B | the regulation of the assessment instrument of Lei nº 13.146 art. 2º §§ 1º, 2º; the regulation on telemedicine | `instrumento de avaliação… já regulamentado`; `situação e requisitos definidos em regulamento atendidos` |
| art. 40-C | the regulation of the consignation | `o regulamento permite a consignação no caso` |
| art. 3º §§ 1º to 3º | the deliberations of the CNAS (art. 18 I and II) | `respeita as deliberações do Conselho Nacional de Assistência Social…` |
| art. 6º-B § 2º III | the registry system of art. 19 XI | `integra o sistema de cadastro de entidades` |
| art. 6º-F §§ 1º, 2º | the regulation (low income; electronic registration; mandatory registration) | `família de baixa renda nos termos do regulamento`, `o regulamento admite a inscrição por meio eletrônico`, `o regulamento torna a inscrição obrigatória para o programa` |
| art. 19 parágrafo único | "situações de vulnerabilidade ou risco social e pessoal, nos termos desta Lei" (the SUS registration rules are outside) | `família ou indivíduo em situação de vulnerabilidade ou risco social e pessoal, nos termos da Lei` |
| art. 21-A § 1º | the unemployment-insurance rules | `ainda corre o prazo de pagamento do seguro-desemprego` |

## What the text turns out to say

Each finding ends "Asserted." where a case or test asserts it.

1. Art. 1º makes social assistance "não contributiva": no contribution is a condition of any right in the Law. Asserted (`lo-tests-cap1-2`, `lo-cases-seat`).
2. Art. 39 lets the CNAS propose changes of the income limits "definidos no § 3º do art. 20 e caput do art. 22", but art. 22 caput, as rewritten in 2011, no longer states any income limit (the 1/4 of the struck wording is gone): the cross-reference is dangling. Not asserted (nothing to compute).
3. The income limit of art. 20 § 3º is "igual ou inferior a 1/4" of the minimum wage: a per capita income exactly at the limit has the right; the struck 2011 wording (src:257, "inferior a 1/4") would have excluded it, and the struck 2020 wording (src:258) set 1/2. Asserted.
4. A regulation can widen the limit only "para até 1/2": a widened fraction above 1/2 is cut at 1/2, one below 1/4 does not widen. Asserted.
5. A family with no member has no per capita income; since art. 20 § 1º makes the applicant a member, the text does not answer for such a family: the encoding returns "o texto não permite responder", but a person who already fails age or disability gets "não há direito" without needing the income. Asserted.
6. Art. 20 § 14 excludes the benefit of a family member "acima de 65 anos" (more than 65) while the caput gives the right at "65 anos ou mais": at exactly 65 the family member's benefit counts in the income. Asserted.
7. "Desatualizado há mais de 24 meses" (art. 21-B): a cadastro updated exactly 24 months ago needs no regularisation. Asserted.
8. Art. 21-B gives 45 days to small municipalities and 90 to those "acima de 50.000 habitantes": 50,000 is 45 days, 50,001 is 90. Asserted.
9. An apprentice with disability keeps the BPC only while concurrent receipt does not pass 24 months; the text stops there, and the encoding applies the suspension of the caput from month 25. Asserted.
10. Art. 21-A speaks only of the "pessoa com deficiência": the text does not say what happens to an elderly beneficiary who works. Asserted ("o texto não responde").
11. The auxílio-inclusão requires a paid activity with remuneration "limitada a 2 (dois) salários-mínimos": 2,000 (with the test minimum wage of 1,000) is in, 2,001 is out; and the remuneration is left out of the family income only when the monthly total is "igual ou inferior" to the same limit. Asserted.
12. The income test of the auxílio-inclusão (art. 26-A IV) is the BPC maintenance test (art. 20), with the family income worked out as §§ 2º to 4º say: the person's own pay (up to 2 minimum wages) and another member's auxílio-inclusão are not counted. Asserted.
13. Art. 26-A § 1º extends the auxílio-inclusão to someone who received the BPC in the 5 years immediately before the activity and had it suspended under art. 21-A: a last receipt exactly 5 years before the start counts, a day earlier does not. Asserted.
14. The first payment of the BPC is due "em até quarenta e cinco dias" after the applicant fulfils the requirements: the 45th day is in time; late payment is updated by the INSS criterion (out of text). Asserted.
15. Eventual benefits are those for birth, death, temporary vulnerability and public calamity; the amount is set by the State, the Federal District or the Municipality; the one figure in the text is the ceiling of 25% of the minimum wage per child "de até 6 anos" (6 included) for the subsidiary benefits. Asserted.
16. Arts. 14 II and 15 II still say the Federal District and the Municipalities pay "os auxílios natalidade e funeral", which art. 22 no longer names. Not asserted (fork F-07).
17. The Peti aims to withdraw from work children and adolescents under 16, "ressalvada a condição de aprendiz, a partir de 14": a 14-year-old apprentice is out, a 13-year-old apprentice is in. Asserted.
18. The CPF and the Cadastro Único are requirements of the grant, the maintenance and the review of the BPC (art. 20 § 12), not only of the grant. Asserted.
19. Art. 33 counts 120 days from the "promulgação" (7 Dec 1993) while arts. 28 § 2º, 32 and 34 count from the "publicação" (8 Dec 1993): the Conselho Nacional de Serviço Social is extinct from 7 April 1994, not 8 April. Asserted.
20. Art. 40-A leaves out the BPC: the preference for the woman responsible for the family unit applies to the benefits of arts. 22, 24-C and 25 only. Asserted.
21. Art. 40 § 2º gave the right to request the renda mensal vitalícia to those older than 70 or invalid until 31 December 1995; the date has passed. Asserted.
22. Art. 19, sole paragraph, buried in the list of competences of the federal body, gives a person or family in vulnerability or risk health care without proof of domicile or of SUS registration; outside that situation the text says nothing. Asserted.
23. Seven provisions are wholly struck or repealed (arts. 20-A, 28-A, 38; art. 20 § 13; art. 9º § 3º; art. 18 sole paragraph; the former sole paragraph of art. 20 § 12-A), art. 20 § 3º I reads "(revogado)", and four are "(VETADO)" or "(Vetado)" (art. 12-A § 3º; art. 18 VII; art. 20 §§ 2º-B, 3º II): eleven coverage rows. Not asserted.
24. For a family that is not of "baixa renda" the text says nothing about where it may register in the Cadastro Único (art. 6º-F § 1º): NOTHING. Asserted.
25. Nothing in art. 20 § 12-A says what follows if the applicant does not submit the biometric record (only § 12-B makes it mandatory for the legal guardian when the applicant cannot): no consequence is encoded.

## What the stable binary does not accept

Checked on 1.6.98 (the brief's dialect `main`), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.

- `YMD` is rejected: a probe file with `IMPORT prelude`, `IMPORT daydate` and `#EVAL YMD 1993 12 7` made `l4 check` report an error at the `YMD` token (probe deleted).
  Every date is written `Date dia mês ano`.
- No `@lang`, `@nlg:xx`, `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section `GIVEN`, `TYPICALLY`, `EVERY`, sets, `IMPORT hierarchy`, `RULES EFFECTIVE DATE` or the temporal built-ins are used.
  "Not covered" is `NOTHING` or an enumeration constructor, asserted.
- Accented letters, `º`, `§` and the em dash inside backticked names compile on the stable binary everywhere I used them (identifiers, `@export`/`@desc` text, `§` headings, comments), and `srcrefs.py` accepts the accented `-- src:N |` lines.
  Nothing was rejected because of an accent.
- `MAYBE (LIST OF …)` and `MAYBE DATE` as result types compile, and so do enumerations as inputs of an `@export`ed function.
  I did not deploy anything, so how Legalese Cloud presents a `MAYBE` or a list result is untested.
- Backticked names of up to 330 characters compile (the longest is a field of `Entidade de assistência social` in `lo-nouns`/`lo-cap1-2-principios`; measured by script over all `lo-*.l4` code lines).
- `NOT` is always parenthesised and no `#ASSERT` continues onto a second line (checked by script: no `#ASSERT` line ends in `AND`, `OR`, `EQUALS`, `IS` or `THEN`).
  The income sums that cross lines are chains of `MINUS` (for example in `art. 20, §§ 3º-A, 9º e 14 — soma dos rendimentos computados, em reais` and in `art. 26-A, §§ 2º e 4º — renda familiar considerada para o auxílio-inclusão`).
- `check.sh` was run with `L4_TARGET=unstable` (the binary is already the stable one), so the second-compiler comparison was skipped, as the brief says.

## What check.sh prints

Command: `L4=<stable l4> L4_TARGET=unstable ./check.sh` in this folder.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
lo-auxilio-inclusao.l4                         0         0       0        0         0
lo-bpc-concessao.l4                            0         0       0        0         0
lo-bpc-manutencao.l4                           0         0       0        0         0
lo-cap1-2-principios.l4                        0         0       0        0         0
lo-cap3-organizacao.l4                         0         0       0        0         0
lo-cap5-financiamento.l4                       0         0       0        0         0
lo-cap6-gerais.l4                              0         0       0        0         0
lo-cases-seat.l4                               0       149       0        0         0
lo-datas.l4                                    0         0       0        0         0
lo-eventuais-servicos.l4                       0         0       0        0         0
lo-nouns.l4                                    0         0       0        0         0
lo-seat.l4                                     0         0       0        0         0
lo-tests-auxilio-inclusao.l4                   0        50       0        0         0
lo-tests-bpc-concessao.l4                      0       112       0        0         0
lo-tests-bpc-manutencao.l4                     0        58       0        0         0
lo-tests-cap1-2.l4                             0        30       0        0         0
lo-tests-cap3.l4                               0        35       0        0         0
lo-tests-cap5-cap6.l4                          0        43       0        0         0
lo-tests-eventuais.l4                          0        31       0        0         0
TOTAL (19 modules)                             0       508       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

No assertion failed or was refused, so there is no failing test to explain.
`python3 -I srcrefs.py check --refs lei-8742-1993.pt.txt lo-*.l4` printed `207 src: lines, 121 runs, 152 locators, 0 problems`.

## Before this is worth relying on

1. A person who knows Brazilian social-assistance law should read each module beside the text; nothing automated replaces it.
2. The minimum wage, the regulation's widened income limit (arts. 20 § 11-A, 20-B), the INSS update criterion (art. 37 sole paragraph), the regulation on consignation (art. 40-C), on telemedicine (art. 40-B § 2º) and on low income (art. 6º-F) are inputs; the questions are only as good as the answers supplied.
   The Decreto nº 6.214/2007 and the other instruments cited in the `Vide` notes should be encoded or supplied.
3. The text is a compilation, not the DOU text, and its retrieval date is not recorded in the inputs; the "(Vigência)" markers (art. 20 § 2º, § 11, § 11-A, art. 20-B, Seção VI and arts. 26-A to 26-H) are carried without being explained, and which parts apply and from when is not settled here (forks F-05, F-14).
4. Who counts in the family (art. 20 § 1º) is asked as numbers in the main BPC and auxílio-inclusão questions; the person must use the family-membership question to get the number right.
5. Case values use a test minimum wage (R$ 1,000) and test dates; no expected value was taken from an official calculator.
6. The deployment of `lo-seat.l4` to Legalese Cloud was not tried: the number of inputs of the BPC and auxílio-inclusão questions (16 and 24 inputs) may need splitting for the website's form.
7. Entities (arts. 3, 6-B, 9, 30, 36) are encoded for what they decide but have no seat; a second seat for an entity or a manager is possible over the same modules, but the Commons rule allows no seat for an official.

## Checked after the run

This section was added by the session that ran the agent, after the run; the sections above are the agent's.

- `L4=<L4_BIN> L4_MAIN=<L4_BIN> ./check.sh` in this folder, with `JL4_LIBRARY_PATH` unset, on the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19): `TOTAL (19 modules) 0 508 0 0 | 0 508 0 0`; exit status 0; every main column reads `same`.
  The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
  The agent ran `check.sh` with `L4_TARGET=unstable`, as its brief said, so the output printed above under "What check.sh prints" is from that run.
- `srcrefs.py check --refs` against `../../registers/source-bundle/lei-8742-1993.pt.txt`: `srcrefs check: 207 src: lines, 121 runs, 152 locators, 0 problems`.
- `srcrefs.py check --strict`: `srcrefs check: 207 src: lines, 121 runs, 152 locators, 10 problems`. These findings are counted here and have not been reviewed one by one.
- 82 `@export` seat questions; 214 coverage rows (98 encoded, 33 fork, 72 inert, 11 repealed or blank).
- Paths in the agent's files that named its run folder (`inputs/...`) were rewritten on copying to name the deposited text in `../../registers/source-bundle/`; the agent's brief is kept verbatim as `BRIEF.md`, and the paths in it are the run's own.
- The agent looked in the stable build's install folder (for its `package.json`, to find the build number), ran a recursive `grep` over that folder and the skills, and counted a string in its own transcript file with `grep -c`; the lead's transcript scan found these. It read nothing outside the run's scratchpad.
