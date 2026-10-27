# NOTES: Decreto-Lei 4.657/1942 (Lei de Introdução às normas do Direito Brasileiro, LINDB), row `legalese-sonnet-5.5`

Status: draft, 2026-10-21. `not_reviewed`: no domain expert has read this encoding against the statute.
Method: a single Sonnet 5.5 agent working alone from `BRIEF.md`, with no other encoding of this law consulted.

## 0. Read this first

- **Target: `unstable`.** The encoding uses `@lang en`, `REFUSE`, `#ASSERT REFUSED ... BECAUSE` and `YMD`, which a `main` build does not read, so `check.sh` was run with `L4_TARGET=unstable` and its main step was skipped. Nothing here claims to read on `main`.
- **The source is a converter rendering, not the official text.** `../../registers/source-bundle/lindb-1942.pt.txt` is a plain-text rendering of Planalto's compiled page, made by a converter script. Only the Diário Oficial text is official, and Planalto's own footer (raw line 112) says so. Nothing in this encoding is verified against the official text; every quotation was checked only against the rendering.
- **The rendering carries a converter marker.** Raw line 33 (art. 7 par. 6) reads `§ 6⟦STRUCK: º⟧`, which is the converter wrapping a struck-through ordinal sign. The encoding reads that paragraph as par. 6 and does not use the struck character.
- **The text is Portuguese only.** The encoding states the rules in English, and every English reading of a Portuguese phrase is the encoder's. The text does not say which language version has authority (fork F-L).
- **What the text answers and what it does not.** The LINDB answers commencement (art. 1) and the effect of one law on another (arts. 2 and 6). It is silent on how to count a period in general, on rest days, holidays and recess, on deemed service, on the moment of day a law binds, on what a time word means, and on subordinate legislation. For every silent item the encoding gives a named `REFUSE`, never a borrowed convention.

## 1. What is encoded and what is not

Encoded, by module (all four start with `@lang en`; only `br-interpretation-time.l4` is meant to be reused on its own, and it imports only `prelude` and `daydate`):

| Module | Provisions | What it computes |
|---|---|---|
| `br-interpretation-time.l4` | art. 1, art. 7 par. 6, art. 19 sole paragraph, and the items the text is silent on | the point N days, months or years after a day; the day an enactment begins to bind (own provision, place, corrections); whether a day falls inside a period counted from a day; rest days as an input; every silent item as a named REFUSE |
| `br-lindb-life-of-a-law.l4` | arts. 2 to 6 | how long a law lasts and when a later law revokes an earlier; non-revival; no excuse by ignorance; the sources for a silent law; the ends a judge attends to; what a law in force leaves alone |
| `br-lindb-conflict-of-laws.l4` | arts. 7 to 19 | which country's law governs, which authority is competent, when a foreign judgment is executed, and the consular acts of arts. 18 and 19 |
| `br-lindb-public-law.l4` | arts. 20 to 30 | duties to consider consequences and circumstances, the compromise of art. 26, compensation, personal liability of the agent, public consultation, and the binding force of instruments |

Not encoded, with the reason in the coverage table (section 5): the standards the text leaves to the decider (`proportional`, `equitable`, `efficient`, `abnormal or excessive`, `indispensable`) are inputs, not computed; art. 26 par. 1 I and art. 30 caput have no test; the phrase `preferably by electronic means` has no stated consequence.
Not encoded because the text is silent: see section 8.

The six must-encode items of the brief are met as follows.

| Item | What the text gives | Where |
|---|---|---|
| 1. Commencement | art. 1 caput, pars. 1, 3, 4 give a rule; art. 1 gives a day and no moment | `the day an enactment begins to bind`, `the day the term of art. 1 ends for`, answer table section 3 |
| 2. Counting of periods | only two forms appear: `N dias depois de` an event (arts. 1, 7 par. 6) and `contados da data` (art. 19 sole paragraph). No general rule | `the day N days after`, `... months after`, `... years after` give a point; `the last day of a period of N ... counted from` REFUSES; `the day ... falls inside a period of N days counted from` answers where every reading agrees |
| 3. Rest days, holidays, recess | no provision | an input list read by `the last day of a period, allowing for days of rest`; a last day on the list is REFUSED |
| 4. Deemed service | no provision | `the day a document is treated as served` REFUSES |
| 5. Repeal | art. 2 pars. 1 to 3 (what revokes; non-revival); art. 6 (the perfect act, the acquired right and res judicata are respected). No savings clause as such; no rule on repeal and re-enactment | `what art. 2 par. 1 and par. 2 say happens to the earlier law`, `a revoked law is restored ...`, `art. 6 requires a law in force to respect it`; `what was done under a repealed text stands after its re-enactment` REFUSES |
| 6. Meanings of time words | no definition of day, week, month or year | `the number of days the text says is in` REFUSES for week, month and year; day is the unit of date arithmetic only by ordinary meaning (fork F3) |


## 2. Files

- `br-interpretation-time.l4`, `br-lindb-life-of-a-law.l4`, `br-lindb-conflict-of-laws.l4`, `br-lindb-public-law.l4`: the modules, in reading order.
- `tests-time.l4` (180 assertions), `tests-life-of-a-law.l4` (73), `tests-conflict-of-laws.l4` (141), `tests-public-law.l4` (119): every expected value was decided from the text before the file was run.
- `tests-rejected-readings.l4` (8): readings the encoding rejects, written as the expectations they would give. All 8 fail by design; `check.sh` counts them (`expected_failed` is 8 for that file) and `encoding.json` says the same under `expected_red`.
- `check.sh`, `srcrefs.py`, `quote-lines.py`: the self-check from the skill, the locator checker, and the quotation tool. Quotation lines (`-- src:N | ...`) are never typed: they are expanded from the raw file by `quote-lines.py expand`, with Planalto's editorial notes dropped, and checked by `quote-lines.py check`.
- `BRIEF.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, this file.

## 3. Answer table for the worked cases

Wording used below: a **point** reading is `the day N units after D`; a **last day** is the last day of a period `counted from` D. The text gives the point reading for `depois de` and says nothing for `counted from` beyond art. 19's 90 days. None of the periods in the first table (three years, five years, thirty days, two years, one year, one month) appears in the text as a period; the text has 45 days, three months, 90 days and one year, each in its own article. On the six worked periods the text is therefore silent. So for each case the encoding answers the point reading by the pattern of art. 1 and art. 7 par. 6 (fork F1, F3), and REFUSES the last day (fork F2).

| Period | Counted from | Point reading (`N units after`) | Last day, `counted from` | Start not counted / start is the first day | Why |
|---|---|---|---|---|---|
| three years | 2025-07-16 | 2028-07-16 | REFUSED | 2028-07-16 / 2028-07-15 | F3 same day number; F2 whether the start counts |
| five years | 2025-01-15 | 2030-01-15 | REFUSED | 2030-01-15 / 2030-01-14 | as above |
| five years | 2025-09-01 | 2030-09-01 | REFUSED | 2030-09-01 / 2030-08-31 | as above |
| thirty days | 2026-01-01 | 2026-01-31 | REFUSED | 2026-01-31 / 2026-01-30 | F1 D plus N; F2 |
| two years | 2024-02-28 | 2026-02-28 | REFUSED | 2026-02-28 / 2026-02-27 | 28 February exists in 2026 |
| one year | 2024-02-29 | REFUSED | REFUSED | REFUSED / REFUSED | 2025 has no 29 February; the text does not say what to do (F3). Neither the 28th nor 1 March is chosen |
| one month | 2025-01-31 | REFUSED | REFUSED | REFUSED / REFUSED | February 2025 has no 31st (F3) |

The 'start not counted / start is the first day' column comes from the named, non-default functions `the last day of N ... counted from, if the starting day is not counted` and `... is the first day`. They exist so a reader can see what each reading would give. The encoding does not choose between them.

Commencement cases. The input is the day of OFFICIAL publication: the text says `oficialmente publicada` and gives no rule for a law that is passed but not published.

| Case | From what day | From what moment of that day | Section and function |
|---|---|---|---|
| An Act published 2026-03-10 that says nothing about commencement, binding throughout Brazil | 2026-04-24 (45 days after 2026-03-10) | REFUSED: art. 1 gives a day, not a moment (F-1g) | art. 1 caput (src:10); `the day an enactment begins to bind` with `nothing about when it comes into force`; `the second of the commencement day from which a law binds` REFUSES |
| The same Act, in a foreign State that admits Brazilian law | 2026-06-10 (three months after 2026-03-10) | REFUSED (F-1g) | art. 1 par. 1 (src:11); a State that does not admit it gives REFUSED (F-1d) |
| An Act that says it comes into force on a day to be fixed later, the day being fixed as 2026-06-01 | 2026-06-01 | REFUSED (F-1g) | art. 1 caput «Salvo disposição contrária» (src:10); `that the day is to be fixed later` with the fixed day. If no day has been fixed the answer is REFUSED. Forks F-1a, F-1b |
| Subordinate legislation made 2026-03-10 that says nothing about commencement | REFUSED | REFUSED | art. 1 speaks of `a lei`; the text has no rule on subordinate legislation (F-1h). `the day subordinate legislation comes into force` REFUSES |

Other answers the tests pin down, with the text that decides each:

| Question | Answer | Text |
|---|---|---|
| Is the 90-day window of art. 19 sole paragraph open on the 1st and on the 89th day after a publication day? | Yes on 2026-03-11 and 2026-06-07 for a publication on 2026-03-10; REFUSED on 2026-03-10 and 2026-06-08 (the two boundary days); no outside them | art. 19 sole paragraph (src:67); F2 |
| A last day that is a rest day, or two or three in a row (2026-03-14, 2026-03-15; with the Friday a holiday, three) | REFUSED in every case; a last day not on the list is returned unchanged | no provision; F-R |
| When is a foreign divorce of a Brazilian recognised (judgment 2025-03-10, no preceding separation)? | not before 2026-03-10; on 2026-03-10 REFUSED; after, yes | art. 7 par. 6 (src:33); F-7b |
| Is a correction published on the day the law is to begin binding a restart (par. 3) or a new law (par. 4)? | REFUSED | art. 1 pars. 3 and 4 (src:14, 15); F-1f |


## 4. Fork register

A fork is a place where the text allows more than one reading. Each row says what the readings are, which one the encoding takes (or that it REFUSES), the text that licenses it, and where the choice is tested.
Where the encoding REFUSES, no reading is taken, and the refusal names the reason.

**Why F1 is answered and F2 is refused.** The asymmetry is the wording and nothing else. «quarenta e cinco dias depois de oficialmente publicada» (src:10) puts the period after the event, so the publication day is not one of the days after it, and the point 45 days after is a single day. «contados da data da publicação desta lei» (src:67) names the start of a count, and a count that starts from a date may begin with that date as its first day or with the day after it; the text says neither. That is my reading of ordinary Portuguese, not a rule the text states, and Q-1 asks a domain expert to confirm it.

| ID | Question | Readings seen | Taken | Text that licenses the choice | Tested in |
|---|---|---|---|---|---|
| F1 | Does N days after D count D? | (a) the Nth day after D is D plus N, D not counted; (b) D plus N minus 1, D counted as the first day; (c) D plus N plus 1, N full days must pass | (a) | art. 1 caput, «quarenta e cinco dias depois de oficialmente publicada» (src:10). The text does not say how to count; `depois de` places the days after the event. | tests-time (45 days across month, year, leap boundaries); (b) and (c) in tests-rejected-readings |
| F2 | In a period `counted from` D, does D count, and so is the last day D plus N or D plus N minus 1? | (a) D not counted: last day D plus N; (b) D counted: last day D plus N minus 1 | REFUSED for the last day; membership answers only where both readings agree and REFUSES on D and D plus N | art. 19 sole paragraph, «contados da data da publicação desta lei» (src:67). The text says neither. | tests-time (every `last day of a period ... counted from`, the six reading functions, membership with n of 1, 2, 3, 10, 90) |
| F3 | What is a month, a year? What is one month after the 31st, one year after 29 February? | (a) calendar month, same day number, no such day where the month is short; (b) clamp to the end of the month (what daydate's `add months` does); (c) roll into the next month; (d) fixed length, 30 days and 365 days | (a), REFUSED where the month has no such day. daydate's clamp is not used | art. 1 par. 1 «três meses depois de oficialmente publicada» (src:11); art. 7 par. 6 «depois de 1 (um) ano da data da sentença» (src:33). The text defines no time word; (a) is the ordinary meaning, not something the text says. (b) and (c) invent a rule the text does not give. | tests-time (31 January, 29 February, 30 November, 31 March, year wrap); (d) in tests-rejected-readings |
| F-R | Does a rule moving a last day off a rest day apply to months and years or only days; what of several rest days in a row? | none: the text has no such rule | the rest days are an input; a last day on the list is REFUSED, in days, months or years alike, one or several in a row | no provision. The question does not arise because the text has nothing to apply. | tests-time (a weekend, Friday holiday making three, empty list, composed with a 5-day period) |
| F-S | When is a document treated as served? | none | REFUSED | no provision | tests-time |
| F-W | What does a period of weeks mean? | none: the text never uses weeks | REFUSED | no provision | tests-time (1 week, 2 weeks) |
| F-L | Which language version has authority? | the text is Portuguese only and is silent | not decided; English readings are the encoder's | no provision. Planalto's footer says only the Diário Oficial text is official (raw line 112). | Q-5 |
| F-1a | Does an enactment's own commencement provision displace the 45 days? | (a) yes; (b) no, 45 days always | (a) | art. 1 caput «Salvo disposição contrária» (src:10) | tests-time (fixed day; day to be fixed later) |
| F-1b | May such a provision name a day before the official publication? | yes or no | REFUSED | art. 1 caput: the text lets a contrary provision displace the 45 days and does not say whether the day may precede publication | tests-time |
| F-1c | Does an own provision displace the three months abroad? | yes or no | REFUSED | art. 1 caput allows a contrary provision; par. 1 does not say so | tests-time |
| F-1d | Who admits Brazilian law abroad, and how? | the text does not say | the place is an input with three values (throughout Brazil; abroad and admitted; abroad and not admitted). Not admitted gives REFUSED | art. 1 par. 1 «quando admitida» (src:11) | tests-time |
| F-1e | Does a correction under par. 3 move a day the enactment fixed for itself? | yes or no | no: it moves only the term of art. 1 | art. 1 par. 3 «o prazo deste artigo e dos parágrafos anteriores começará a correr da nova publicação» (src:14) speaks of the term of the article | tests-time |
| F-1f | A correction published on the very day the law is to begin binding: par. 3 (before) or par. 4 (already in force)? | depends on the moment of that day | REFUSED. A correction strictly before restarts the term; strictly after is a new law | art. 1 pars. 3 and 4 (src:14, 15). The text gives no moment. | tests-time (before, on, after; two corrections; out of order; abroad) |
| F-1g | From what moment of the commencement day does a law bind? | start of the day; the moment of publication; unspecified | REFUSED. `the law binds at some moment of` the day is TRUE from that day; `the law binds throughout` the day is REFUSED on it and TRUE after | art. 1 caput gives a day and no moment (src:10) | tests-time |
| F-1h | When does subordinate legislation come into force? | by analogy with art. 1; some other rule | REFUSED | art. 1 speaks of «a lei»; nothing in the text reaches subordinate legislation | tests-time |
| F-1i | What publication starts the term? | the official publication; the passing | the day of official publication is the input | art. 1 caput «oficialmente publicada» (src:10) | not tested separately; it is the shape of the input |
| F-1j | Which republications are `destinada a correção`? | the text does not say | the caller lists the days of republications that are corrections; the encoding does not judge purpose | art. 1 par. 3 (src:14) | tests-time |
| F-2a | Are the three grounds of par. 1 sufficient, and are they the only grounds? | sufficient only; or sufficient and exhaustive | each sufficient; with the caput, they are the grounds there are, so a later law with none and nothing alongside gives the answer `art. 2 lists no ground for revoking the earlier law` | art. 2 caput «terá vigor até que outra a modifique ou revogue» (src:16); par. 1 (src:17) | tests-life-of-a-law |
| F-2b | A later law with a ground of par. 1 and also establishing provisions alongside the existing ones: par. 1 or par. 2? | par. 1 prevails; par. 2 prevails | REFUSED | art. 2 par. 1 (src:17) and par. 2 «não revoga nem modifica a lei anterior» (src:18) | tests-life-of-a-law |
| F-2c | Which date makes a law `posterior`? | publication; commencement; enactment | the caller supplies a boolean `it is later than the earlier law` | art. 2 par. 1 (src:17) | tests-life-of-a-law |
| F-2d | When does a law meant to be temporary cease? | not said | REFUSED | art. 2 caput speaks only of «Não se destinando à vigência temporária» (src:16) | tests-life-of-a-law |
| F-2e | Whose provision is `disposição em contrário` in par. 3? | the revoking law's; any law's | the caller supplies whether a provision restores the revoked law | art. 2 par. 3 (src:19) | tests-life-of-a-law |
| F-2f | Is incompatibility partial or whole? | either | a boolean the caller supplies | art. 2 par. 1 «quando seja com ela incompatível» (src:17) | tests-life-of-a-law |
| F-2g | What does repeal and re-enactment do to what was done under the old text? | not said; there is no savings clause as such | REFUSED. Art. 6 is the nearest provision and covers what a law in force respects | no provision | tests-life-of-a-law |
| F-4 | Are analogy, custom and general principles ranked? | ranked in that order; unranked; cumulative | unranked: the text names three sources and gives no order | art. 4 (src:21) | tests-life-of-a-law |
| F-5 | Must the judge attend to both ends, or either? | both; either | both: `e` joins the ends the judge attends to | art. 5 (src:22) | tests-life-of-a-law |
| F-6 | Does «inalterável, a arbítrio de outrem» qualify the term fixed beforehand as well as the condition? | both; the condition only | REFUSED where the readings differ (a term fixed beforehand that another person can alter); otherwise answered | art. 6 par. 2 (src:25) | tests-life-of-a-law |
| F-6b | A thing that is none of a perfect act, res judicata or an acquired right | takes immediate effect; not said | takes immediate effect: the caput lists the three as the exceptions | art. 6 caput (src:23) | tests-life-of-a-law |
| F-7a | In par. 2, is the `país` of the spouses nationality or domicile? | nationality; domicile | the caller supplies a country; the rule also requires that it not be Brazil, because the paragraph is about foreigners | art. 7 par. 2 «país de ambos os nubentes» (src:29) | tests-conflict-of-laws |
| F-7b | In par. 6, on the anniversary day of the judgment, is a year `depois`? | yes; no | REFUSED on the day; FALSE before; TRUE after | art. 7 par. 6 «depois de 1 (um) ano da data da sentença» (src:33) | tests-conflict-of-laws |
| F-7c | Par. 6 with a judgment of 29 February | 28 February or 1 March | REFUSED on every day, including days years later, because F3 gives no anniversary. This is more cautious than the membership rule of art. 19, which answers where every reading agrees; it is a known limitation | art. 7 par. 6; F3 | tests-conflict-of-laws |
| F-7e | Par. 7: a person within both the head-of-family extension and the guardian extension, with different domiciles | either prevails | REFUSED; abandonment leaves the person's own domicile | art. 7 par. 7 «Salvo o caso de abandono» (src:34) | tests-conflict-of-laws |
| F-7f | Par. 8: a person with a residence elsewhere than where found | residence; where found | REFUSED when they differ; the place found when there is no residence | art. 7 par. 8 «no lugar de sua residência ou naquele em que se encontre» (src:35) | tests-conflict-of-laws |
| F-7g | Par. 1 for a marriage celebrated outside Brazil; par. 3 for spouses with the same domicile | not said | REFUSED | art. 7 pars. 1 and 3 (src:28, 30) | tests-conflict-of-laws |
| F-11 | Par. 2 against par. 3 for a foreign government's seat building | par. 2 prevails; par. 3 prevails | par. 3 first: the paragraph names the seat building specifically. An organisation of a foreign government is not within par. 3. This is an encoding choice, not the text's | art. 11 pars. 2 and 3 (src:47, 48) | tests-conflict-of-laws; the other reading in tests-rejected-readings |
| F-12 | Are the two grounds of art. 12 caput the only ones? | exhaustive; not | the predicate is named `... on a ground listed in art. 12 caput`: TRUE when one holds, REFUSED otherwise | art. 12 caput «quando for o réu domiciliado no Brasil ou aqui tiver de ser cumprida a obrigação» (src:49) | tests-conflict-of-laws |
| F-17 | Art. 17: are sovereignty, public order and good morals cumulative or alternative? | all three at once; any one | any one | art. 17 «a soberania nacional, a ordem pública e os bons costumes» (src:62). The list names what a foreign law may not offend, and a law that offends one of them is within the sense. | tests-conflict-of-laws; the other reading in tests-rejected-readings |
| F-20 | Art. 20 sole paragraph: does `inclusive em face das possíveis alternativas` require the alternatives to be addressed? | yes; only where there are any | yes: a third required element | art. 20 sole paragraph (src:69) | tests-public-law |
| F-22 | Art. 22 par. 2: are the four things to be considered all required? | all; any | all: it is a list of what is considered, not of grounds | art. 22 par. 2 (src:76) | tests-public-law |
| F-24 | Art. 24 sole paragraph: are the three kinds of general orientation cumulative? | cumulative; alternatives | alternatives: `e ainda` adds a third kind, which needs both repetition and wide public knowledge | art. 24 sole paragraph «e ainda as adotadas por prática administrativa reiterada e de amplo conhecimento público» (src:82) | tests-public-law |
| F-26 | Art. 26: `a partir de sua publicação oficial`: does the publication day count? | yes; no | effects begin at some moment of the publication day, so from that day in the weak sense; in force throughout only from the next day; REFUSED on the day for `throughout` | art. 26 caput «a partir de sua publicação oficial» (src:84); F-1g | tests-public-law |
| F-28 | Art. 28: are intent and gross error the only grounds of personal liability? | exhaustive; not | named `... on a ground listed in art. 28 caput`; FALSE means no listed ground, not exoneration | art. 28 caput «em caso de dolo ou erro grosseiro» (src:96) | tests-public-law |
| F-30a | Art. 30 sole paragraph: `Os instrumentos previstos no caput deste artigo` after an `inclusive` list: only the three named? | only those; any | REFUSED for an instrument the caput does not name | art. 30 caput «inclusive por meio de regulamentos, súmulas administrativas e respostas a consultas» (src:106) | tests-public-law |
| F-30b | Art. 30 sole paragraph: on the day of the revision | earlier instrument binds; does not | REFUSED on the day; binds before; does not after | art. 30 sole paragraph «até ulterior revisão» (src:107) | tests-public-law |

**Where I looked for ambiguity.** In every article I checked: lists joined by `e` or `ou` (cumulative or alternative); `quando` and `em caso de` lists (whether they are exhaustive); `salvo` clauses (what they except, and whose provision); every period and time word; the verbs `poderá`, `deverá`, `será` (permission or duty); cross-references (`dos parágrafos anteriores`, `desta lei`, `do mesmo Decreto-lei`); and which provisions are repealed or vetoed. The register above is what I found. It is not claimed to be complete.

## 5. Coverage table

Dispositions: `encoded` (a function in a module carries it); `inert` (nothing in the text can be tested, with the reason); `repealed or blank in this text` (the text marks it revoked or vetoed); `not applicable` (page furniture, signatures, notes). `src:N` is the raw line of `../../registers/source-bundle/lindb-1942.pt.txt`.

Counts: 108 rows: 79 encoded, 5 inert, 8 repealed or blank in this text, 16 not applicable.

| Provision | src | Disposition | Where, and any fork |
|---|---|---|---|
| Page header: Del4657compilado, Presidência da República, Casa Civil, Subchefia para Assuntos Jurídicos | 1-4 | not applicable | Planalto page furniture, not statute text. |
| Title line: DECRETO-LEI Nº 4.657, DE 4 DE SETEMBRO DE 1942. | 5 | not applicable | Names the instrument. The date 4 September 1942 is not an input to any rule; the text does not say when the Decreto-Lei itself came into force. |
| Page labels: Vigência, (Regulamento) | 6-7 | not applicable | Link labels the converter kept. |
| Short title: Lei de Introdução às normas do Direito Brasileiro (with Planalto's note on Lei nº 12.376/2010) | 8 | not applicable | A title. |
| Enacting formula: O Presidente da Republica ... decreta: | 9 | not applicable | The authority recited is not an input to any rule. |
| Art. 1 caput: a law begins to bind throughout the country 45 days after official publication, unless it says otherwise | 10 | encoded | br-interpretation-time: `the day the term of art. 1 ends for`, `the day an enactment begins to bind`, `the day an enactment fixes for itself`. Forks F1, F-1a, F-1b, F-1g. Moment of the day REFUSED. |
| Art. 1 par. 1: abroad, where Brazilian law is admitted, binding force begins three months after official publication | 11 | encoded | br-interpretation-time: `the day the term of art. 1 ends for` (place enum). Forks F3, F-1c, F-1d. A State that does not admit it gives a REFUSE. |
| Planalto's second line of Vide notes to par. 1 | 12 | not applicable | Note-only line. |
| Art. 1 par. 2 | 13 | repealed or blank in this text | (Revogado pela Lei nº 12.036, de 2009). |
| Art. 1 par. 3: a new publication to correct the text, before the law is in force, restarts the term | 14 | encoded | br-interpretation-time: `the day art. 1 and its corrections fix for`. Forks F-1e, F-1f, F-1j. |
| Art. 1 par. 4: corrections to a text already in force are a new law | 15 | encoded | br-interpretation-time: `a correction counts as a new law`. Fork F-1f. |
| Art. 2 caput: a law not meant to be temporary lasts until another modifies or revokes it | 16 | encoded | br-lindb-life-of-a-law: `the law is in force on`. Forks F-2d, F-1g. A temporary law's end is REFUSED. |
| Art. 2 par. 1: a later law revokes the earlier when it says so, is incompatible, or regulates the whole matter | 17 | encoded | br-lindb-life-of-a-law: `a ground listed in art. 2 par. 1 exists`, `what art. 2 par. 1 and par. 2 say happens to the earlier law`. Forks F-2a, F-2b, F-2c, F-2f. |
| Art. 2 par. 2: a new law alongside existing provisions neither revokes nor modifies | 18 | encoded | br-lindb-life-of-a-law: `what art. 2 par. 1 and par. 2 say happens to the earlier law`. Fork F-2b (both apply: REFUSED). |
| Art. 2 par. 3: a revoked law is not restored by the revoking law ceasing, unless a provision says so | 19 | encoded | br-lindb-life-of-a-law: `a revoked law is restored when the revoking law loses force`. Fork F-2e. |
| Art. 3: nobody is excused from complying by alleging ignorance of the law | 20 | encoded | br-lindb-life-of-a-law: `alleging that one does not know the law excuses compliance` MEANS FALSE. |
| Art. 4: where the law is silent, the judge decides by analogy, custom and general principles of law | 21 | encoded | br-lindb-life-of-a-law: `the sources art. 4 names for a case on which the law is silent`, `art. 4 names the source`. Fork F-4 (not ranked). |
| Art. 5: in applying the law the judge attends to its social ends and the demands of the common good | 22 | encoded | br-lindb-life-of-a-law: `the judge applied the law as art. 5 requires` (both ends required, fork F-5). What the social ends or the common good are is the caller's judgment, not computed. |
| Art. 6 caput: a law in force has immediate and general effect, respecting the perfect juridical act, acquired right and res judicata | 23 | encoded | br-lindb-life-of-a-law: `art. 6 requires a law in force to respect it`, `a law in force takes immediate effect on`. Fork F-6b. |
| Art. 6 par. 1: a perfect juridical act is one already consummated under the law in force when done | 24 | encoded | br-lindb-life-of-a-law: `it is a perfect juridical act`. |
| Art. 6 par. 2: acquired rights: those the holder or another for the holder can exercise, and those whose exercise starts at a fixed term or an unalterable condition | 25 | encoded | br-lindb-life-of-a-law: `it is an acquired right`. Fork F-6 (REFUSED where the reading matters). |
| Art. 6 par. 3: res judicata is a judicial decision from which no appeal lies | 26 | encoded | br-lindb-life-of-a-law: `it is res judicata`. |
| Art. 7 caput: the law of the country of domicile governs the start and end of personality, name, capacity and family rights | 27 | encoded | br-lindb-conflict-of-laws: `the country whose law governs personality, name, capacity and family rights, for a person domiciled in`. |
| Art. 7 par. 1: a marriage celebrated in Brazil: Brazilian law on diriment impediments and formalities | 28 | encoded | br-lindb-conflict-of-laws: `the country whose law governs the diriment impediments and the formalities of celebration ...`. A marriage celebrated elsewhere is REFUSED (fork F-7g). |
| Art. 7 par. 2: the marriage of foreigners may be celebrated before the diplomatic or consular authorities of the country of both spouses | 29 | encoded | br-lindb-conflict-of-laws: `art. 7 par. 2 allows the marriage of foreigners ...`. Fork F-7a. |
| Art. 7 par. 3: spouses with different domiciles: invalidity governed by the law of the first conjugal domicile | 30 | encoded | br-lindb-conflict-of-laws: `the country whose law governs the invalidity of a marriage ...`. Same domicile: REFUSED (fork F-7g). |
| Art. 7 par. 4: property regime: the law of the spouses' domicile, and if it differs, of the first conjugal domicile | 31 | encoded | br-lindb-conflict-of-laws: `the country whose law governs the regime of property ...`. |
| Art. 7 par. 5: a foreigner married who naturalises may, with the spouse's express consent, ask the judge to note partial community of property when the naturalisation decree is delivered | 32 | encoded | br-lindb-conflict-of-laws: `art. 7 par. 5 allows a request ...`. |
| Art. 7 par. 5, last words: third parties' rights respected and the adoption given to the registry | 32 | inert | Conditions on what the judge does with the request, not on the right to ask. Nothing in the text says what follows if they are not met, so there is no test to write. |
| Art. 7 par. 6, first sentence: a foreign divorce of a Brazilian spouse is recognised only after 1 year from the judgment, unless it was preceded by a judicial separation of equal term | 33 | encoded | br-lindb-conflict-of-laws: `the waiting rule of art. 7 par. 6 is met on`. Forks F3, F-7b, F-7c. The anniversary day is REFUSED. |
| Art. 7 par. 6, first sentence, last words: the conditions for the efficacy of foreign judgments are obeyed | 33 | encoded | br-lindb-conflict-of-laws: art. 15 is encoded as its own predicate (`the foreign judgment meets the requirements of art. 15`); the two are not combined, the caller asks both. Open question Q-3. |
| Art. 7 par. 6, second sentence: the Superior Tribunal de Justica may re-examine earlier homologations on request | 33 | encoded | br-lindb-conflict-of-laws: `art. 7 par. 6 allows the Superior Tribunal de Justica to re-examine the decision`. Open question Q-3. |
| Art. 7 par. 7: save abandonment, the head of the family's domicile extends to the other spouse and unemancipated children, and the guardian's to those in their charge | 34 | encoded | br-lindb-conflict-of-laws: `the domicile of the person under art. 7 par. 7`. Fork F-7e. |
| Art. 7 par. 8: a person with no domicile is domiciled where they reside or are found | 35 | encoded | br-lindb-conflict-of-laws: `the domicile of a person who has none, with a residence ...`. Fork F-7f. |
| Art. 8 caput: the law of the country where property is situated qualifies it and governs relations to it | 36 | encoded | br-lindb-conflict-of-laws: `the country whose law governs property` (constructor `property in general`). |
| Art. 8 par. 1: movables the owner brings or means to carry elsewhere: the law of the owner's domicile | 37 | encoded | br-lindb-conflict-of-laws: same function, constructor `a movable the owner brings or means to carry to other places`. |
| Art. 8 par. 2: a pledge: the law of the domicile of the person in whose possession the thing is | 38 | encoded | br-lindb-conflict-of-laws: same function, constructor `a thing in pledge`. |
| Art. 9 caput: obligations are qualified and governed by the law of the country where constituted | 39 | encoded | br-lindb-conflict-of-laws: `the country whose law qualifies and governs an obligation constituted in`. |
| Art. 9 par. 1: an obligation to be performed in Brazil that needs an essential form: that form is observed, admitting the foreign law's peculiarities on extrinsic requirements | 40 | encoded | br-lindb-conflict-of-laws: `the essential form of Brazilian law is observed under art. 9 par. 1`, `art. 9 par. 1 admits a peculiarity of the foreign law`. |
| Art. 9 par. 2: a contract obligation is deemed constituted where the proponent resides | 41 | encoded | br-lindb-conflict-of-laws: `the country in which an obligation resulting from a contract is deemed constituted ...`. |
| Art. 10 caput: succession is governed by the law of the country of the deceased's or missing person's domicile, whatever the nature and situation of the assets | 42 | encoded | br-lindb-conflict-of-laws: `the country whose law governs a succession`. |
| Art. 10 par. 1: foreigners' assets in Brazil: Brazilian law, for a Brazilian spouse or children or their representative, unless the personal law is more favourable to them | 43 | encoded | br-lindb-conflict-of-laws: same function. Rejected reading in `tests-rejected-readings.l4`. |
| Art. 10 par. 2: the law of the domicile of the heir or legatee governs capacity to succeed | 44 | encoded | br-lindb-conflict-of-laws: `the country whose law governs the capacity to succeed ...`. |
| Art. 11 caput: organisations for collective ends obey the law of the State where constituted | 45 | encoded | br-lindb-conflict-of-laws: `the country whose law governs an organisation constituted in`. |
| Art. 11 par. 1: no branch, agency or establishment in Brazil before the constitutive acts are approved by the Brazilian Government; they stay subject to Brazilian law | 46 | encoded | br-lindb-conflict-of-laws: `art. 11 par. 1 forbids a branch, agency or establishment in Brazil`, `the country whose law an organisation with a branch in Brazil is subject to`. |
| Art. 11 par. 2: foreign governments and the organisations they constitute, direct or invest with public functions may not acquire immovables or property susceptible to expropriation | 47 | encoded | br-lindb-conflict-of-laws: `art. 11 par. 2 forbids the acquisition`. Fork F-11. |
| Art. 11 par. 3: foreign governments may acquire the buildings needed for the seat of diplomatic representatives or consular agents | 48 | encoded | br-lindb-conflict-of-laws: `art. 11 par. 3 allows the acquisition`, combined in `a foreign government or its organisation may acquire the property in Brazil`. Fork F-11. |
| Art. 12 caput: the Brazilian judicial authority is competent when the defendant is domiciled in Brazil or the obligation is to be performed here | 49 | encoded | br-lindb-conflict-of-laws: `the Brazilian judicial authority is competent on a ground listed in art. 12 caput`. Fork F-12 (does not claim the two grounds are the only ones). |
| Art. 12 par. 1: only the Brazilian judicial authority may hear actions about immovables in Brazil | 50 | encoded | br-lindb-conflict-of-laws: `only the Brazilian judicial authority may hear the action, under art. 12 par. 1`. |
| Art. 12 par. 2: letters rogatory from a competent foreign authority are carried out once the exequatur is granted, in the Brazilian form, observing the foreign law on the object of the measures | 51 | encoded | br-lindb-conflict-of-laws: `the Brazilian judicial authority carries out the letter rogatory ...`, `the country whose law governs the form ...`, `the country whose law governs the object ...`. |
| Art. 13: proof of facts abroad: the law of the place on burden and means, but Brazilian courts do not admit proofs Brazilian law does not know | 52 | encoded | br-lindb-conflict-of-laws: `the country whose law governs the burden and the means of proving ...`, `a Brazilian court admits the means of proof ...`. |
| Art. 14: if the foreign law is not known, the judge may require proof of its text and force | 53 | encoded | br-lindb-conflict-of-laws: `art. 14 allows the judge to require ...`. |
| Art. 15 caput: a foreign judgment is executed in Brazil if it meets the following requirements | 54 | encoded | br-lindb-conflict-of-laws: `the foreign judgment meets the requirements of art. 15` (all five). |
| Art. 15 a): given by a competent judge | 55 | encoded | br-lindb-conflict-of-laws: first conjunct. |
| Art. 15 b): parties served, or default legally verified | 56 | encoded | br-lindb-conflict-of-laws: second conjunct (either limb). |
| Art. 15 c): res judicata and the formalities for execution in the place where given | 57 | encoded | br-lindb-conflict-of-laws: third conjunct (both limbs). |
| Art. 15 d): translated by an authorised interpreter | 58 | encoded | br-lindb-conflict-of-laws: fourth conjunct. |
| Art. 15 e): homologated by the Supremo Tribunal Federal | 59 | encoded | br-lindb-conflict-of-laws: fifth conjunct, as the text names the STF. Open question Q-3 (art. 7 par. 6 names the STJ). |
| Art. 15 sole paragraph | 60 | repealed or blank in this text | (Revogado pela Lei nº 12.036, de 2009). |
| Art. 16: renvoi: the foreign law's own provision is applied, ignoring any remission to another law | 61 | encoded | br-lindb-conflict-of-laws: `a foreign law's remission to another law is considered` MEANS FALSE. |
| Art. 17: foreign laws, acts, judgments and declarations of will have no efficacy in Brazil when they offend national sovereignty, public order and good morals | 62 | encoded | br-lindb-conflict-of-laws: `art. 17 denies ... efficacy in Brazil` (any one of the three). Fork F-17. |
| Art. 18 caput: for Brazilians the Brazilian consular authorities may celebrate marriage and other civil-registry and notarial acts, including birth and death registration of the children of a Brazilian born in the consulate's country | 63 | encoded | br-lindb-conflict-of-laws: `the Brazilian consular authority is competent under art. 18 caput for` (five act constructors). Acts concerning others: REFUSED. |
| Art. 18 par. 1: consular authorities may also celebrate consensual separation and divorce of Brazilians, with no minor or incapable children, the term requirements observed, and the deed recording the property, maintenance and name provisions | 64 | encoded | br-lindb-conflict-of-laws: `art. 18 par. 1 allows the consular authority to celebrate` (seven conditions). |
| Art. 18 par. 2: a duly constituted lawyer is indispensable, by subscribing the petition with both parties, or with one if the other has their own lawyer; the lawyer's signature on the deed is not needed | 65 | encoded | br-lindb-conflict-of-laws: `the assistance of a lawyer required by art. 18 par. 2 is given`, `the lawyer's signature on the public deed is required` MEANS FALSE. |
| Art. 19 caput: acts indicated in art. 18 celebrated by Brazilian consuls while the Decreto-Lei was in force are valid if they met every legal requirement | 66 | encoded | br-lindb-conflict-of-laws: `art. 19 caput validates the act`. Open question Q-4 (the period is not given). |
| Art. 19 sole paragraph: where the consular authorities refused under art. 18, the person may renew the request within 90 days counted from the publication of 'this law' | 67 | encoded | br-lindb-conflict-of-laws: `art. 19 sole paragraph allows the request to be renewed on` using `the day ... falls inside a period of 90 days counted from` of br-interpretation-time. Forks F2, Q-4. Both boundary days REFUSED. |
| Art. 20 caput: no decision on abstract legal values without considering the practical consequences | 68 | encoded | br-lindb-public-law: `art. 20 caput is breached by a decision where`. What counts as an abstract value is the caller's judgment. |
| Art. 20 sole paragraph: the motivation shows the necessity and adequacy of the measure, including against the possible alternatives | 69 | encoded | br-lindb-public-law: `art. 20 sole paragraph is met by a motivation where`. Fork F-20. |
| Art. 20 sole paragraph: Planalto's amendment note | 70 | not applicable | Note-only line. |
| Art. 20 caput, the three spheres (administrative, controlling, judicial) | 68 | inert | No rule in arts. 20 to 30 turns on which of the three spheres a decision belongs to, so the sphere is not an input; the predicates are meant to be asked only about decisions in them. |
| Art. 21 caput: a decision that invalidates an act, contract, adjustment, process or administrative norm must expressly indicate its legal and administrative consequences | 71 | encoded | br-lindb-public-law: `art. 21 caput is breached by a decision where`. |
| Art. 21 sole paragraph: where appropriate, the conditions for a proportional and equitable regularisation; no abnormal or excessive burden or loss on those affected | 72 | encoded | br-lindb-public-law: `art. 21 sole paragraph is breached by a decision where`. 'Proportional', 'equitable', 'abnormal', 'excessive' are caller-supplied booleans; whether a given burden is abnormal is not decided here. |
| Art. 22 caput: in interpreting public-management norms, the manager's real obstacles and difficulties and the demands of the public policies in their charge are considered, without prejudice to the rights of the administered | 73 | encoded | br-lindb-public-law: `art. 22 caput is breached by an interpretation where`. |
| Art. 22 par. 1: a decision on regularity of conduct or validity of an act considers the practical circumstances that imposed, limited or conditioned the agent's action | 74 | encoded | br-lindb-public-law: `art. 22 par. 1 is breached by a decision where`. |
| Art. 22 par. 1: Planalto's amendment note | 75 | not applicable | Note-only line. |
| Art. 22 par. 2: in applying sanctions, the nature and gravity of the infraction, the damage to the administration, the aggravating or attenuating circumstances and the agent's antecedents are considered | 76 | encoded | br-lindb-public-law: `art. 22 par. 2 is breached by the application of a sanction where` (all four required, fork F-22). |
| Art. 22 par. 3: sanctions already applied to the agent are counted in the dosimetry of other sanctions of the same nature for the same fact | 77 | encoded | br-lindb-public-law: `art. 22 par. 3 is breached by the dosimetry of a sanction where`. |
| Art. 22 par. 3: Planalto's amendment note | 78 | not applicable | Note-only line. |
| Art. 23 caput: a decision establishing a new interpretation or orientation on an indeterminate-content norm, imposing a new duty or conditioning of a right, provides a transition regime when indispensable | 79 | encoded | br-lindb-public-law: `art. 23 caput is breached by a decision where`. 'Indispensable' is a caller-supplied boolean. |
| Art. 23 sole paragraph | 80 | repealed or blank in this text | (VETADO). |
| Art. 24 caput: review of a completed act takes into account the general orientations of the time; no declaring fully constituted situations invalid by a later change of general orientation | 81 | encoded | br-lindb-public-law: `art. 24 caput forbids declaring the situation invalid where`, `art. 24 caput is breached by a review where`. A change on the very day the production was completed is REFUSED. |
| Art. 24 sole paragraph: what counts as general orientations | 82 | encoded | br-lindb-public-law: `it is a general orientation under art. 24 sole paragraph`. Fork F-24. |
| Art. 25 | 83 | repealed or blank in this text | (VETADO). |
| Art. 26 caput: the administrative authority may conclude a compromise to eliminate irregularity, legal uncertainty or a contentious situation, after hearing the legal organ and where appropriate public consultation, with reasons of relevant general interest, observing the legislation; effects from official publication | 84 | encoded | br-lindb-public-law: `art. 26 caput allows the administrative authority to conclude a compromise where`, `the compromise produces effects at some moment of`, `the compromise produces effects throughout`. Fork F-26. |
| Art. 26 caput: Planalto's amendment notes | 85 | not applicable | Note-only line. |
| Art. 26 par. 1 (lead-in): the compromise | 86 | encoded | br-lindb-public-law: introduces the items below. |
| Art. 26 par. 1 (lead-in): Planalto's amendment note | 87 | not applicable | Note-only line. |
| Art. 26 par. 1, I: will seek a proportional, equitable, efficient legal solution compatible with the general interests | 88 | inert | It states an aim ('buscara', will seek) and attaches no consequence to missing it; every adjective in it is a standard left to the decider. A predicate over it would only restate the caller's opinion. |
| Art. 26 par. 1, II | 89 | repealed or blank in this text | (VETADO). |
| Art. 26 par. 1, III: no permanent exoneration from a duty or conditioning of a right recognised by a general orientation | 90 | encoded | br-lindb-public-law: `art. 26 par. 1 is breached by a compromise where`. |
| Art. 26 par. 1, IV: must provide clearly the parties' obligations, the deadline and the sanctions | 91 | encoded | br-lindb-public-law: same function. |
| Art. 26 par. 2 | 92 | repealed or blank in this text | (VETADO). |
| Art. 27 caput: the decision may impose compensation for undue benefits or abnormal or unjust losses resulting from the process or the conduct of those involved | 93 | encoded | br-lindb-public-law: `art. 27 caput allows the decision to impose compensation where`. |
| Art. 27 par. 1: the decision on compensation is reasoned, the parties heard beforehand on whether, how and, where it arises, how much | 94 | encoded | br-lindb-public-law: `art. 27 par. 1 is met by a decision on compensation where`. |
| Art. 27 par. 2: a procedural compromise may be made to prevent or regulate compensation | 95 | encoded | br-lindb-public-law: `art. 27 par. 2 allows a procedural compromise where`. |
| Art. 28 caput: the public agent answers personally for decisions or technical opinions in case of intent or gross error | 96 | encoded | br-lindb-public-law: `the public agent answers personally on a ground listed in art. 28 caput where`. Fork F-28 (the grounds are not said to be the only ones). |
| Art. 28 pars. 1, 2, 3 | 97-99 | repealed or blank in this text | (VETADO) each. |
| Art. 29 caput: a normative act issued by an administrative authority, other than of mere internal organisation, may be preceded by public consultation, which will be considered in the decision | 100 | encoded | br-lindb-public-law: `art. 29 caput allows a public consultation before the act where`, `art. 29 caput is breached by a decision where`. |
| Art. 29 caput: preferably by electronic means | 100 | inert | A preference with no consequence stated for not following it, so there is nothing to test. |
| Art. 29 caput, par. 1, par. 2: Planalto's amendment and Vigencia notes | 101, 103, 105 | not applicable | Note-only lines. |
| Art. 29 par. 1: the convocation contains the draft act and fixes the deadline and other conditions, observing specific legal and regulatory norms if any | 102 | encoded | br-lindb-public-law: `art. 29 par. 1 is met by a convocation where`. The reference to 'specific norms, if any' is not encoded: the text does not name them. |
| Art. 29 par. 2 | 104 | repealed or blank in this text | (VETADO). |
| Art. 30 caput: public authorities must act to increase legal security in applying norms, including by regulations, administrative precedents and answers to consultations | 106 | inert | A duty to 'act to increase' legal security has no test: nothing says how much or by when, so no input could settle compliance. The three instruments it names are used by the sole paragraph. |
| Art. 30 sole paragraph: the instruments bind the organ or entity they are directed to, until further revision | 107 | encoded | br-lindb-public-law: `an instrument of art. 30 caput binds, on`. Forks F-30a, F-30b. The revision day itself is REFUSED. |
| Place and date: Rio de Janeiro, 4 September 1942, 121st of Independence and 54th of the Republic | 108 | not applicable | Signature block. |
| Signatures: Getúlio Vargas, Alexandre Marcondes Filho, Oswaldo Aranha | 109-111 | not applicable | Signature block. |
| Planalto's disclaimer: this text does not replace the one published in the DOU of 9.9.1942, rectified on 8.10.1942 and on 17.6.1943 | 112 | not applicable | Page furniture. It records that the Decreto-Lei itself was republished with corrections; no rule here uses that. |
| Final asterisk | 113 | not applicable | A character the converter kept. |


## 6. What `check.sh` prints

Command: `L4_TARGET=unstable L4=<L4_BIN> ./check.sh`, with `JL4_LIBRARY_PATH` unset. `L4_BIN` is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`. The first line goes to standard error; the rest is standard output.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
br-interpretation-time.l4                      0         0       0        0         0
br-lindb-conflict-of-laws.l4                   0         0       0        0         0
br-lindb-life-of-a-law.l4                      0         0       0        0         0
br-lindb-public-law.l4                         0         0       0        0         0
tests-conflict-of-laws.l4                      0       141       0        0         0
tests-life-of-a-law.l4                         0        73       0        0         0
tests-public-law.l4                            0       119       0        0         0
tests-rejected-readings.l4                     8         0       8        0         8
tests-time.l4                                  0       180       0        0         0
TOTAL (9 modules)                              8       513       8        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit status 0. Read it as follows. The `errors` column for `tests-rejected-readings.l4` is 8 and its `failed` is 8, matching `expected` 8; every other module has 0 errors, 0 failed, 0 refused. `satisfied` is one per `#ASSERT` line (180 + 73 + 141 + 119 = 513). The modules show 0 satisfied because they contain no `#ASSERT`.

The other checks, run over every `*.l4` in one call each:

```
srcrefs check: 91 src: lines, 32 runs, 138 locators, 0 problems
quote-lines check: 91 quote lines, 0 problems
```

No `@lang en` module has a line `is at the end of the file` or `follows code on its line` diagnostic. The only diagnostic left on each file is the linter Hint that a module that declares nothing is English and the line can go; it is harmless, and `@lang en` is required by the brief.

## 7. Findings, and edits to test expectations

The brief says a failing assertion is a finding and an expectation must never be edited to match the code. Two expectation lines were edited during the run, and one code gap was found. They are stated plainly here.

1. **`tests-conflict-of-laws.l4`, art. 7 par. 6 block, one line edited.** I wrote `the waiting rule of art. 7 par. 6 is met on (2025-03-11) (2025-03-10) FALSE TRUE` and asserted TRUE. The two booleans are `one or both spouses are Brazilian` and `a judicial separation for an equal term came first`, so the line said no spouse is Brazilian. The rule REFUSES in that case, because the sentence is about divorces of Brazilians, and the assertion came back `refused`. The line's own comment shows the separation path was the case I meant, so it was a mis-specified test, not a wrong rule. I changed it to `TRUE TRUE` (a Brazilian spouse, a preceding separation, the day after the judgment, expected TRUE), and added the original `FALSE TRUE` as a `#ASSERT REFUSED ... BECAUSE` with the text's reason. The expected value for the case I meant never changed; the argument I typed did.
2. **`tests-time.l4`, membership with a period of `0 days`, one `BECAUSE` string edited.** The assertion expected a refusal and got one, but with the message `a period counted after a day is a whole number of units, none of them negative`. Zero is not negative, so the message was wrong for that input. That is a finding against the code's wording. I added a separate named refusal for membership, `a period counted from a day has at least one whole day`, and updated the `BECAUSE` to it. The expectation (a refusal) was never edited; the string naming the reason was. The same new refusal now answers `2.5 days` and a negative period in the membership function. A duplicate zero test I added while doing this was removed.
3. **`the day N years after` accepted `1.5`.** `tests-time.l4` asserted a refusal for `1.5 years` (a period is a whole number of units, from the text's use of whole units only) and it returned a date. That was a code gap: `years after` lacked the whole-number guard that `days after` and `months after` have. The code was fixed; the expectation was not edited.
4. **NOT precedence.** The type checker rejected two expressions of the form `NOT a OR b` in `br-lindb-public-law.l4` (it reads them as `NOT (a OR b)`). Both were bracketed as `(NOT a) OR b`, which is what I meant, and a third of the same shape was bracketed with them; no test expectation was involved.
5. **Every `#ASSERT REFUSED` now carries a `BECAUSE`.** A bare `#ASSERT REFUSED` passes for any refusal. Fifty-one in `tests-time.l4`, nine in `tests-life-of-a-law.l4` and three in `tests-conflict-of-laws.l4` had none at first. I chose each message from the design before looking at the output, and they all matched on the first run, apart from item 2.

Not claimed: that the 513 passing assertions test the statute. They test that the encoding does what I read the text to say. Q-1 to Q-6 are where a reader with the statute should push.

## 8. What the source does not answer

- Whether the publication day counts in a period `counted from` it (F2), and whether a period `after` an event excludes the event day (F1, my reading only).
- What a month or a year is, and what follows for a start on the 31st or on 29 February (F3).
- Anything about rest days, holidays, recess, deemed service, or weeks (F-R, F-S, F-W).
- From what moment of the commencement day a law binds (F-1g), and when subordinate legislation comes into force (F-1h).
- Which language version has authority (F-L).
- What repeal and re-enactment do to what was done under the old text; there is no savings clause as such (F-2g).
- Who admits Brazilian law abroad (F-1d); what happens to a law fixed to begin before it is published (F-1b).

## 9. Open questions for a domain expert

- **Q-1.** Is `45 dias depois de oficialmente publicada` counted as the 45th day after publication (publication day not counted), as F1 reads it? The encoding consulted no other statute and no doctrine, so it does not know what Brazilian practice says.
- **Q-2.** Does a period `contados da data` count the date? (F2.) If the answer is fixed, the six reading functions in `br-interpretation-time.l4` are already written for either.
- **Q-3.** Art. 15 e) names the Supremo Tribunal Federal for homologation; art. 7 par. 6 names the Superior Tribunal de Justica. Both are in the rendering and the text does not reconcile them. The encoding carries each as written.
- **Q-4.** Art. 19 caput speaks of acts celebrated `na vigência do Decreto-lei nº 4.657`, and the sole paragraph of 90 days counted from the publication of `desta lei`. The text does not identify the law, and the window long ago expired. The encoding takes both as inputs. Is art. 19 still live?
- **Q-5.** Which language version of the LINDB has authority? The rendering is Portuguese only.
- **Q-6.** The rendering keeps `(Vigência)` labels on art. 18 pars. 1 and 2 and art. 29. They may mark a commencement note. The encoding ignored them because they are not text of the provisions; was that right?
- **Q-7.** Raw line 112 records that the Decreto-Lei was itself rectified on 8 October 1942 and 17 June 1943. The encoding does not use that, but it is the same situation as art. 1 pars. 3 and 4.

## 10. Rejected readings

`tests-rejected-readings.l4` holds eight expectations the encoding rejects, so that a reviewer can see what each rejected reading would have said: 45 days as D plus 44 and as D plus 46 (F1); three months as 90 days and a year as 365 days and two years as 730 days (F3); art. 17 as cumulative (F-17); art. 11 par. 2 over par. 3 (F-11); art. 10 par. 1 ignoring the more-favourable personal law. Each fails because the encoding gives the other answer, and `check.sh` expects exactly eight.

## 11. Provenance

- Source: Planalto's compiled text of 2026-10-21, as a converter rendering; see `SOURCE-LICENSE.md` and `../../SOURCE-LICENSE.md`. `text_sha256` of the rendering: `817da9966e25ae0a485ad241a045e3f2b26b042b5c0f24521eb0ca39aebdbeb0` (from the `.meta.json` in the inputs; I did not recompute it).
- Tools: `srcrefs.py` and `quote-lines.py` are in this directory.
- Independence: I did not read `commons`, `commonswt`, `canon`, any other `interp-wave` run, or anything under `~/.claude/` except the two named skills.
