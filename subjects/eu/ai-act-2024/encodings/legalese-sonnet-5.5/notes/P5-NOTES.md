# NOTES (P5): Articles 40 to 49, Annexes V, VI, VIII and IX of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744

Status, written 2026-11-17 by part agent P5 (run dst-aia-P5, model Sonnet 5.5):
the source is the Publications Office consolidation of 27.7.2026, a plain-text rendering with no legal effect, so nothing here is verified against the official text.
Commencement is IN, assumed, not ruled.
Chapter III Section 5 (Articles 40 to 49) is dated by the general date of Article 113 (2 August 2026), assumed, not ruled (keel fork F-113-groups).
Every Annex of this part takes the group of the Article that gives it effect, assumed, not ruled.
Seam S14 is wired: every function that takes one high-risk AI system's route, placement date and design change asks the keel's Article 2(2) function (the reach is fork F-S14-reach, assumed, not ruled).
Every rule of this part is unreviewed by a lawyer.
Where this file says a check was run, the command is named; where it says a fact is in the text, the line number of the consolidated text is given.

How each kind of claim below was checked:
line numbers and quotations by `python3 -I srcrefs.py check --refs` and `--strict` over the six layer-1 modules (255 quote lines, 136 runs, 143 locators, 0 problems);
assertion counts and the agreement of two builds by `check.sh` with L4 = 1.6.110 and L4_MAIN = 1.6.109 (the section "What check.sh prints" gives its output unedited);
trace outcomes by running every `#TRACE` on both builds with `work/traces.py` and comparing each with the `-- EXPECT` comment above it (241 traces, 0 differences);
coverage rows by `work/gen/coverage.py`, which segments the text itself and asserts that every non-blank line of the three ranges falls in exactly one row;
quotations in the fork register by `work/gen/verify_quotes.py`, which looks each quoted fragment up in the consolidated and the base text, and each quotation from the Guide and the brief in the file it names;
the list of regulative rules and the count of sites by `work/gen/rules.py` and by grepping the `-- FALSE-kind`, `-- NOTHING-kind` and `-- S14-kind` comments of the layer-1 modules.

Where the brief and PLAN.md differ the brief governs.
I took the brief's rulings as printed: the grant ruling of 2026-11-12, the periods ruling of 2026-11-05 (rules (a), (b), (c)), and the two split sites left to the part.
I did not change an answer to match another part, and I could not see another part.

Files (all under this directory):
layer 1: `P5-section-5.l4`, `P5-art-40-41-42.l4`, `P5-art-43-annex-vi.l4`, `P5-art-44-45-46.l4`, `P5-art-47-48-annex-v.l4`, `P5-art-49-annex-viii-ix.l4`;
tests: `P5-tests-art-40-41-42.l4`, `P5-tests-art-43-annex-vi.l4`, `P5-tests-art-44-45-46.l4`, `P5-tests-art-47-48-annex-v.l4`, `P5-tests-art-49-annex-viii-ix.l4`, `P5-tests-section-5-gap.l4` (the required special file);
seats: `P5-seat-<slug>.l4` and `P5-cases-seat-<slug>.l4` for provider, deployer, rep, manufacturer, gpai, notified, person;
`NOTES.md`, `PROGRESS.md`.
There is no `NEEDS-CORE.md`: nothing in this part needed a change to the keel or the core.


## Coverage (P5)

Built by `work/gen/coverage.py` from the text itself: one row per article heading, paragraph, subparagraph, point, annex item and Section heading; a `▼M1` marker line or a footnote line is folded into the row it opens or closes; the two deleted points of Annex VIII Section B are one row each.
Every non-blank line of 636-748, 1783-1799 and 1840-1886 falls in exactly one row (the script stops if one falls in none or in two).
A row's disposition is `inert` (reason 1 or 2 only), `fork` (the row holds a line a fork of the register is about; the row names the fork and the rule that encodes the chosen reading), `repealed or blank in this text`, or `encoded`.
The keel's forks F-113-groups and F-111-2-nothing, and my F-P5-saving, reach every row of this part and are not repeated on each row.
The L4 names are the layer-1 functions and rules whose `@ref` quote lines cite the row's lines; a replaced or deleted passage also lists the as-enacted functions, which cite the base text.

Summary: **151 rows**: encoded 93, fork 33, inert 23 (reason 1: 19, reason 2: 4, reason 3: 0), repealed or blank in this text 2.

Audit: the three ranges hold 177 non-blank lines and the rows cover 177 of them (every one, once); a first pass that counted one unit per line group gave 163 units, and 12 of them were marker, footnote or dash lines that belong to a neighbouring row, so the table has 151 rows (163 before, 151 after).

| lines | unit | disposition | note | L4 names |
| --- | --- | --- | --- | --- |
| 636-636 | Chapter III Section 5 heading (line 636) | inert | reason 1 (not operative: a heading) |  |
| 637-637 | Chapter III Section 5 heading (line 637) | inert | reason 1 (not operative: a heading) |  |
| 638-639 | Art 40 heading | inert | reason 1 (not operative: a heading) |  |
| 640-640 | Art 40(1) first subparagraph | fork | F-40-42-limits | `Art 40(1) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2`; `Art 40(1) the general-purpose AI model is presumed to be in conformity with the obligation set out in Chapter V, Sections 2 and 3` |
| 641-641 | Art 40(2) first subparagraph | encoded |  | `Art 40(2) the Commission must issue standardisation requests covering all requirements set out in Section 2`; `Art 40(2) the Commission must issue standardisation requests covering obligations set out in Chapter V, Sections 2 and 3`; `Art 40(2) the standardisation request must also ask for deliverables on reporting and documentation processes`; `Art 40(2) the Commission must consult the Board and relevant stakeholders`; `Art 40(2) the Commission's duty to issue standardisation requests`; `Art 40(2) the Commission's duty to ask for deliverables on reporting and documentation processes`; `Art 40(2) the Commission's duty to consult the Board and relevant stakeholders` |
| 642-642 | Art 40(2) second subparagraph | encoded |  | `Art 40(2) the Commission must specify that standards have to be clear and consistent`; `Art 40(2) the Commission's duty to specify that standards have to be clear and consistent` |
| 643-643 | Art 40(2) third subparagraph | encoded |  | `Art 40(2) the Commission must request the European standardisation organisations to provide evidence of their best efforts`; `Art 40(2) the Commission's duty to request evidence of best efforts` |
| 644-648 | Art 40(2) fourth subparagraph | encoded |  | `Art 40(2) as amended the Commission must request standardisation deliverables to facilitate joint compliance and presumption of conformity`; `Art 40(2) the Commission must request standardisation deliverables to facilitate joint compliance and presumption of conformity`; `Art 40(2) the Commission's duty to request standardisation deliverables` |
| 649-649 | Art 40(3) first subparagraph | encoded |  | `Art 40(3) the participants in the standardisation process must seek to promote investment and innovation in AI`; `Art 40(3) the duty of the participants in the standardisation process` |
| 650-651 | Art 41 heading | inert | reason 1 (not operative: a heading) |  |
| 652-652 | Art 41(1) first subparagraph | fork | F-41-1 | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 653-653 | Art 41(1) first subparagraph point (a) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 654-654 | Art 41(1) first subparagraph point (a)(i) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 655-655 | Art 41(1) first subparagraph point (a)(ii) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 656-656 | Art 41(1) first subparagraph point (a)(iii) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 657-657 | Art 41(1) first subparagraph point (a)(iv) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 658-658 | Art 41(1) first subparagraph point (b) | encoded |  | `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| 659-659 | Art 41(1) second subparagraph | encoded |  | `Art 41(1) the Commission must consult the advisory forum`; `Art 41(1) the Commission's duty to consult the advisory forum` |
| 660-660 | Art 41(1) third subparagraph | inert | reason 2 (machinery): Art 41(1) third subparagraph: the committee procedure for adopting the implementing acts (Art 98(2)) |  |
| 661-661 | Art 41(2) first subparagraph | encoded |  | `Art 41(2) the Commission must inform the committee that it considers the conditions to be fulfilled`; `Art 41(2) the Commission's duty to inform the committee` |
| 662-662 | Art 41(3) first subparagraph | fork | F-40-42-limits | `Art 41(3) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2`; `Art 41(3) the general-purpose AI model is presumed to comply with the obligation set out in Chapter V, Sections 2 and 3` |
| 663-663 | Art 41(4) first subparagraph | encoded |  | `Art 41(4) the Commission must assess the harmonised standard`; `Art 41(4) the Commission must repeal the implementing act or the part of it that covers the same requirements`; `Art 41(4) the Commission's duty to assess the harmonised standard`; `Art 41(4) the Commission's duty to repeal the implementing act` |
| 664-664 | Art 41(5) first subparagraph | fork | F-41-5 | `Art 41(5) the provider of the high-risk AI system must duly justify that it has adopted technical solutions at least equivalent to the requirements`; `Art 41(5) the provider of the general-purpose AI model must duly justify that it has adopted technical solutions at least equivalent to the obligations`; `Art 41(5) the provider has met the duty to duly justify the technical solutions`; `Art 41(5) the provider's duty to duly justify the technical solutions adopted` |
| 665-665 | Art 41(6) first subparagraph | encoded |  | `Art 41(6) the Member State must inform the Commission with a detailed explanation`; `Art 41(6) the Commission must amend the implementing act establishing the common specification`; `Art 41(6) the Member State's duty to inform the Commission`; `Art 41(6) the Commission's duty to amend the implementing act` |
| 666-667 | Art 42 heading | inert | reason 1 (not operative: a heading) |  |
| 668-668 | Art 42(1) first subparagraph | fork | F-40-42-limits | `Art 42(1) the high-risk AI system is presumed to comply with the relevant requirements laid down in Article 10(4)` |
| 669-669 | Art 42(2) first subparagraph | fork | F-40-42-limits | `Art 42(2) the high-risk AI system is presumed to comply with the cybersecurity requirement set out in Article 15` |
| 670-672 | Art 42(3) first subparagraph | fork | F-42-3-where | `Art 42(3) as amended the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15`; `Art 42(3) the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15` |
| 673-674 | Art 43 heading | inert | reason 1 (not operative: a heading) |  |
| 675-675 | Art 43(1) first subparagraph | encoded |  | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 676-676 | Art 43(1) first subparagraph point (a) | encoded |  | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 677-677 | Art 43(1) first subparagraph point (b) | encoded |  | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 678-678 | Art 43(1) second subparagraph | fork | F-43-1 | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 679-679 | Art 43(1) second subparagraph point (a) | fork | F-43-1 | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 680-680 | Art 43(1) second subparagraph point (b) | fork | F-43-1, F-43-1b | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 681-681 | Art 43(1) second subparagraph point (c) | fork | F-43-1 | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 682-682 | Art 43(1) second subparagraph point (d) | fork | F-43-1 | `Art 43(1) the conformity assessment procedure the provider is to follow`; `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| 683-683 | Art 43(1) third subparagraph | encoded |  | `Art 43(1) the body that carries out the conformity assessment procedure of Annex VII`; `Art 43(1) the provider's permission to choose any of the notified bodies`; `Art 43(1) the market surveillance authority's duty to act as a notified body` |
| 684-684 | Art 43(2) first subparagraph | encoded |  | `Art 43(2) the conformity assessment procedure the provider is to follow`; `Art 43(2) the provider's duty to follow the procedure based on internal control` |
| 685-686 | Art 43(3) first subparagraph | encoded |  | `Art 43(3) first subparagraph as enacted the conformity assessment procedure the provider is to follow`; `Art 43(3) first subparagraph as amended the conformity assessment procedure the provider is to follow`; `Art 43(3) first subparagraph the conformity assessment procedure the provider is to follow`; `Art 43(3) first subparagraph as enacted the requirements set out in Section 2 apply to the high-risk AI system and are part of that assessment`; `Art 43(3) first subparagraph as amended the requirements set out in Section 2 apply to the high-risk AI system and are part of that assessment`; `Art 43(3) first subparagraph the requirements set out in Section 2 apply to the high-risk AI system and are part of that assessment`; `Art 43(3) first subparagraph as enacted the point of Annex VII applies`; `Art 43(3) first subparagraph as amended the point of Annex VII applies`; `Art 43(3) first subparagraph the point of Annex VII applies`; `Art 43(3) first subparagraph as amended the assessment of the quality management system set out in Article 17 is also undertaken`; `Art 43(3) first subparagraph the assessment of the quality management system set out in Article 17 is also undertaken`; `Art 43(3) the provider's duty to follow the relevant conformity assessment procedure` |
| 687-687 | Art 43(3) second subparagraph | fork | F-43-3-power | `Art 43(3) second subparagraph as enacted the notified body has the power to control the conformity of the high-risk AI system with the requirements set out in Section 2`; `Art 43(3) second subparagraph as amended the notified body has the power to assess the conformity of the high-risk AI system with the requirements set out in Section 2`; `Art 43(3) second subparagraph the notified body has the power to assess the conformity of the high-risk AI system with the requirements set out in Section 2`; `Art 43(3) as amended second subparagraph the date by which the notified body must apply for designation`; `Art 43(3) the date by which the notified body must apply for designation`; `Art 43(3) the notified body has met the duty to apply for designation by 28 January 2028`; `Art 43(3) the notified body's permission to assess the conformity of the high-risk AI system`; `Art 43(3) the duty of the notified body to apply for designation` |
| 688-688 | Art 43(3) third subparagraph | fork | F-43-3-opt | `Art 43(3) third subparagraph as enacted the product manufacturer may use the option not to have a third-party conformity assessment`; `Art 43(3) third subparagraph as amended the product manufacturer may use the option not to have a third-party conformity assessment`; `Art 43(3) third subparagraph the product manufacturer may use the option not to have a third-party conformity assessment`; `Art 43(3) third subparagraph as amended the classification of the product as a high-risk AI system affects the choice of the conformity assessment procedure`; `Art 43(3) third subparagraph the classification of the product as a high-risk AI system affects the choice of the conformity assessment procedure`; `Art 43(3) third subparagraph as amended the manufacturer is required to choose a third-party conformity assessment procedure only because the product includes a high-risk AI system as a safety component`; `Art 43(3) third subparagraph the manufacturer is required to choose a third-party conformity assessment procedure only because the product includes a high-risk AI system as a safety component`; `Art 43(3) the product manufacturer's permission to use the option not to have a third-party conformity assessment` |
| 689-690 | Art 43(3) fourth subparagraph | encoded |  | `Art 43(3) as amended fourth subparagraph the conformity assessment procedure the provider is to follow`; `Art 43(3) fourth subparagraph the conformity assessment procedure the provider is to follow` |
| 691-691 | Art 43(4) first subparagraph | encoded |  | `Art 43(4) the high-risk AI system must undergo a new conformity assessment procedure`; `Art 43(4) the provider's duty to have the high-risk AI system undergo a new conformity assessment procedure` |
| 692-692 | Art 43(4) second subparagraph | encoded |  | `Art 43(4) the changes do not constitute a substantial modification` |
| 693-693 | Art 43(5) first subparagraph | inert | reason 2 (machinery): Art 43(5): the Commission's power to amend Annex VI by delegated act |  |
| 694-694 | Art 43(6) first subparagraph | inert | reason 2 (machinery): Art 43(6): the Commission's power to amend Article 43(1) and (2) by delegated act |  |
| 695-696 | Art 44 heading | inert | reason 1 (not operative: a heading) |  |
| 697-697 | Art 44(1) first subparagraph | encoded |  | `Art 44(1) the certificate must be drawn up in a language which can be easily understood by the relevant authorities of the Member State in which the notified body is established`; `Art 44(1) the notified body's duty to draw up the certificate in a language which can be easily understood` |
| 698-698 | Art 44(2) first subparagraph | fork | F-44-2-both, F-44-2-extension, F-44-2-supplement, F-44-2-period | `Art 44(2) the longest period in years that a certificate may indicate`; `Art 44(2) the period the certificate indicates is within the limit`; `Art 44(2) the validity of a certificate may be extended for a further period`; `Art 44(2) the supplement to a certificate remains valid`; `Art 44(2) the notified body's permission to extend the validity of a certificate` |
| 699-699 | Art 44(3) first subparagraph | fork | F-44-3-unless | `Art 44(3) the notified body must suspend or withdraw the certificate issued or impose restrictions on it`; `Art 44(3) the notified body must give reasons for its decision`; `Art 44(3) the notified body's duty to suspend or withdraw the certificate or impose restrictions`; `Art 44(3) the notified body's duty to give reasons for its decision` |
| 700-700 | Art 44(3) second subparagraph | encoded |  | `Art 44(3) an appeal procedure against decisions of the notified bodies must be available` |
| 701-702 | Art 45 heading | inert | reason 1 (not operative: a heading) |  |
| 703-703 | Art 45(1) first subparagraph | encoded |  | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 704-704 | Art 45(1) first subparagraph point (a) | encoded |  | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 705-705 | Art 45(1) first subparagraph point (b) | encoded |  | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 706-706 | Art 45(1) first subparagraph point (c) | encoded |  | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 707-707 | Art 45(1) first subparagraph point (d) | encoded |  | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 708-708 | Art 45(1) first subparagraph point (e) | fork | F-45-1-e | `Art 45(1) the notified body must inform the notifying authority of the item`; `Art 45(1) the notified body's duty to inform the notifying authority` |
| 709-709 | Art 45(2) first subparagraph | encoded |  | `Art 45(2) the notified body must inform the other notified bodies of the item`; `Art 45(2) the notified body's duty to inform the other notified bodies` |
| 710-710 | Art 45(2) first subparagraph point (a) | fork | F-45-1-e | `Art 45(2) the notified body must inform the other notified bodies of the item`; `Art 45(2) the notified body's duty to inform the other notified bodies` |
| 711-711 | Art 45(2) first subparagraph point (b) | fork | F-45-1-e | `Art 45(2) the notified body must inform the other notified bodies of the item`; `Art 45(2) the notified body's duty to inform the other notified bodies` |
| 712-712 | Art 45(3) first subparagraph | fork | F-45-1-e | `Art 45(3) the notified body must provide the other notified body with relevant information on the kind of results`; `Art 45(3) the notified body's duty to provide the other notified bodies with relevant information` |
| 713-713 | Art 45(4) first subparagraph | encoded |  | `Art 45(4) the notified body must safeguard the confidentiality of the information that it obtains, in accordance with Article 78`; `Art 45(4) the notified body's duty to safeguard confidentiality` |
| 714-715 | Art 46 heading | inert | reason 1 (not operative: a heading) |  |
| 716-716 | Art 46(1) first subparagraph | fork | F-46-1 | `Art 46(1) the market surveillance authority may authorise the placing on the market or the putting into service of a specific high-risk AI system within the territory of its Member State`; `Art 46(1) the authorisation must be for a limited period while the necessary conformity assessment procedures are being carried out`; `Art 46(1) the completion of the conformity assessment procedures must be undertaken without undue delay`; `Art 46(1) the market surveillance authority's permission to authorise` |
| 717-717 | Art 46(2) first subparagraph | fork | F-46-2 | `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into service without the authorisation`; `Art 46(2) the use of the high-risk AI system must be stopped with immediate effect`; `Art 46(2) all the results and outputs of the use must be immediately discarded`; `Art 46(2) the authority's permission to put the system into service without the authorisation`; `Art 46(2) the deployer's duty to stop the use with immediate effect`; `Art 46(2) the deployer's duty to discard all the results and outputs immediately` |
| 718-718 | Art 46(3) first subparagraph | encoded |  | `Art 46(3) the condition for issuing the authorisation is met`; `Art 46(3) the market surveillance authority must inform the Commission and the other Member States of the authorisation`; `Art 46(3) the obligation to inform covers the information`; `Art 46(3) the market surveillance authority's duty to inform the Commission and the other Member States` |
| 719-719 | Art 46(4) first subparagraph | fork | F-46-4 | `Art 46(4) the authorisation is deemed justified` |
| 720-720 | Art 46(5) first subparagraph | encoded |  | `Art 46(5) the duty of the paragraph applies`; `Art 46(5) the Commission's duties after an objection` |
| 721-721 | Art 46(6) first subparagraph | encoded |  | `Art 46(6) the authorisation must be withdrawn by the market surveillance authority of the Member State concerned`; `Art 46(6) the market surveillance authority's duty to withdraw the authorisation` |
| 722-722 | Art 46(7) first subparagraph | encoded |  | `Art 46(7) the derogation of this Article applies to the high-risk AI system` |
| 723-724 | Art 47 heading | inert | reason 1 (not operative: a heading) |  |
| 725-725 | Art 47(1) first subparagraph | fork | F-47-1-form, F-47-1-period, F-47-1-request | `Art 47(1) the provider must draw up an EU declaration of conformity for the high-risk AI system`; `Art 47(1) the declaration is in a form the paragraph names`; `Art 47(1) the provider must keep the declaration at the disposal of the national competent authorities`; `Art 47(1) the declaration must identify the high-risk AI system for which it has been drawn up`; `Art 47(1) a copy of the declaration must be submitted to the relevant national competent authorities`; `Art 47(1) the provider's duty to draw up an EU declaration of conformity`; `Art 47(1) the provider's duty to keep the declaration at the disposal of the national competent authorities`; `Art 47(1) the provider's duty to submit a copy upon request` |
| 726-726 | Art 47(2) first subparagraph | encoded |  | `Art 47(2) the declaration must state that the high-risk AI system concerned meets the requirements set out in Section 2`; `Art 47(2) the declaration must contain the information set out in Annex V`; `Art 47(2) the declaration must be translated into a language that can be easily understood by the national competent authorities of the Member States in which the high-risk AI system is placed on the market or made available`; `Art 47(2) the provider's duty to state in the declaration that the system meets the requirements of Section 2`; `Art 47(2) the provider's duty to include the information set out in Annex V`; `Art 47(2) the provider's duty to translate the declaration` |
| 727-727 | Art 47(3) first subparagraph | encoded |  | `Art 47(3) a single declaration must be drawn up in respect of all Union law applicable to the high-risk AI system`; `Art 47(3) the declaration must contain all the information required to identify the Union harmonisation legislation to which it relates`; `Art 47(3) the provider's duty to draw up a single declaration` |
| 728-728 | Art 47(4) first subparagraph | encoded |  | `Art 47(4) the provider assumes responsibility for compliance with the requirements set out in Section 2`; `Art 47(4) the provider must keep the declaration up-to-date`; `Art 47(4) the provider's duty to keep the declaration up-to-date` |
| 729-729 | Art 47(5) first subparagraph | inert | reason 2 (machinery): Art 47(5): the Commission's power to amend Annex V by delegated act |  |
| 730-731 | Art 48 heading | inert | reason 1 (not operative: a heading) |  |
| 732-732 | Art 48(1) first subparagraph | encoded |  | `Art 48(1) the CE marking is subject to the general principles set out in Article 30 of Regulation (EC) No 765/2008` |
| 733-733 | Art 48(2) first subparagraph | fork | F-48-2 | `Art 48(2) a digital CE marking must be used`; `Art 48(2) the digital CE marking may be used`; `Art 48(2) the provider's duty to use a digital CE marking` |
| 734-734 | Art 48(3) first subparagraph | encoded |  | `Art 48(3) where the CE marking must be affixed`; `Art 48(3) the provider's duty to affix the CE marking` |
| 735-735 | Art 48(4) first subparagraph | fork | F-48-4-affix | `Art 48(4) the CE marking must be followed by the identification number of the notified body`; `Art 48(4) the person may affix the identification number of the notified body`; `Art 48(4) the identification number must also be indicated in the promotional material`; `Art 48(4) the provider's duty to follow the CE marking with the identification number`; `Art 48(4) the permission to affix the identification number of the notified body`; `Art 48(4) the provider's duty to indicate the identification number in the promotional material` |
| 736-736 | Art 48(5) first subparagraph | encoded |  | `Art 48(5) the CE marking must indicate that the high-risk AI system also fulfils the requirements of the other Union law`; `Art 48(5) the provider's duty to indicate in the CE marking that the system also fulfils the requirements of the other Union law` |
| 737-738 | Art 49 heading | inert | reason 1 (not operative: a heading) |  |
| 739-739 | Art 49(1) first subparagraph | fork | F-49-1-rep, F-49-before | `Art 49(1) the registration in the EU database is required`; `Art 49(1) who must register themselves and their system`; `Art 49(1) the registration was made before the placing on the market or the putting into service`; `Art 49(1) the provider must register themselves and their system`; `Art 49(1) the authorised representative must register themselves and the system`; `Art 49(1) the duty to register before placing on the market or putting into service` |
| 740-740 | Art 49(2) first subparagraph | fork | F-49-1-rep, F-49-before, F-49-2-saving | `Art 49(2) the registration in the EU database is required`; `Art 49(2) who must register themselves and the AI system`; `Art 49(2) the registration was made before the placing on the market or the putting into service`; `Art 49(2) the provider must register themselves and the AI system`; `Art 49(2) the authorised representative must register themselves and the AI system`; `Art 49(2) the duty to register before placing on the market or putting into service` |
| 741-741 | Art 49(3) first subparagraph | fork | F-49-before, F-49-3-acts | `Art 49(3) the deployer must register themselves, select the system and register its use in the EU database`; `Art 49(3) the registration was made before the putting into service or the use`; `Art 49(3) the deployer's duty to register before putting into service or using` |
| 742-742 | Art 49(4) first subparagraph | fork | F-49-4-areas, F-49-4-gate, F-49-4-bearer | `Art 49(4) the high-risk AI system is one of those referred to in points 1, 6 and 7 of Annex III in the areas of law enforcement, migration, asylum and border control management`; `Art 49(4) the registration must be in a secure non-public section of the EU database`; `Art 49(4) the information item is included in the restricted registration`; `Art 49(4) the provider's duty to register in the secure non-public section` |
| 743-743 | Art 49(4) first subparagraph point (a) | encoded |  | `Art 49(4)(a) the Section A point is within the restricted registration`; `Art 49(4) the information item is included in the restricted registration` |
| 744-744 | Art 49(4) first subparagraph point (b) | fork | F-49-4-b-point-9 | `Art 49(4)(b) as enacted the Section B point is within the restricted registration`; `Art 49(4)(b) as amended the Section B point is within the restricted registration`; `Art 49(4) the information item is included in the restricted registration` |
| 745-745 | Art 49(4) first subparagraph point (c) | encoded |  | `Art 49(4)(c) the Section C point is within the restricted registration`; `Art 49(4) the information item is included in the restricted registration` |
| 746-746 | Art 49(4) first subparagraph point (d) | encoded |  | `Art 49(4)(d) the Annex IX point is within the restricted registration`; `Art 49(4) the information item is included in the restricted registration` |
| 747-747 | Art 49(4) second subparagraph | encoded |  | `Art 49(4) the person has access to the restricted sections of the EU database` |
| 748-748 | Art 49(5) first subparagraph | fork | F-49-4-gate | `Art 49(5) the high-risk AI system must be registered at national level` |
| 1783-1784 | Annex V heading | inert | reason 1 (not operative: a heading) |  |
| 1785-1785 | Annex V introduction | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1786-1786 | Annex V point 1 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1787-1787 | Annex V point 2 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1788-1788 | Annex V point 3 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1789-1789 | Annex V point 4 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1790-1790 | Annex V point 5 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1791-1791 | Annex V point 6 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1792-1792 | Annex V point 7 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1793-1793 | Annex V point 8 | encoded |  | `Annex V the declaration must contain the point`; `Annex V the provider's duty to include the point in the declaration` |
| 1794-1795 | Annex VI heading | inert | reason 1 (not operative: a heading) |  |
| 1796-1796 | Annex VI point 1 | encoded |  | `Annex VI point 1 the provider has carried out the conformity assessment procedure based on internal control` |
| 1797-1797 | Annex VI point 2 | encoded |  | `Annex VI point 2 the provider has verified the quality management system`; `Annex VI point 2 the provider's duty to verify the quality management system` |
| 1798-1798 | Annex VI point 3 | encoded |  | `Annex VI point 3 the provider has examined the technical documentation`; `Annex VI point 3 the provider's duty to examine the technical documentation` |
| 1799-1799 | Annex VI point 4 | encoded |  | `Annex VI point 4 the provider has verified the design and development process and the post-market monitoring`; `Annex VI point 4 the provider's duty to verify the design and development process and the post-market monitoring` |
| 1840-1841 | Annex VIII heading | inert | reason 1 (not operative: a heading) |  |
| 1842-1842 | Annex VIII Section A heading | inert | reason 1 (not operative: a heading) |  |
| 1843-1843 | Annex VIII Section A introduction | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1844-1844 | Annex VIII Section A point 1 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1845-1845 | Annex VIII Section A point 2 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1846-1846 | Annex VIII Section A point 3 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1847-1847 | Annex VIII Section A point 4 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1848-1848 | Annex VIII Section A point 5 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1849-1849 | Annex VIII Section A point 6 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1850-1850 | Annex VIII Section A point 7 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1851-1851 | Annex VIII Section A point 8 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1852-1852 | Annex VIII Section A point 9 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1853-1853 | Annex VIII Section A point 10 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1854-1854 | Annex VIII Section A point 11 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1855-1855 | Annex VIII Section A point 12 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1856-1856 | Annex VIII Section A point 13 | encoded |  | `Annex VIII Section A the information at the point must be provided and kept up to date`; `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` |
| 1857-1857 | Annex VIII Section B heading | inert | reason 1 (not operative: a heading) |  |
| 1858-1858 | Annex VIII Section B introduction | encoded |  | `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1859-1859 | Annex VIII Section B point 1 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1860-1860 | Annex VIII Section B point 2 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1861-1861 | Annex VIII Section B point 3 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1862-1862 | Annex VIII Section B point 4 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1863-1863 | Annex VIII Section B point 5 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1864-1864 | Annex VIII Section B point 6 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1865-1867 | Annex VIII Section B point 7 (deleted) | repealed or blank in this text | the text shows `▼M1 DELETED` and a dash line where the point stood; the text as enacted is encoded in the as-enacted functions and Art 49(4)(b) still names point 9 | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1868-1868 | Annex VIII Section B point 8 | encoded |  | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1869-1871 | Annex VIII Section B point 9 (deleted) | repealed or blank in this text | the text shows `▼M1 DELETED` and a dash line where the point stood; the text as enacted is encoded in the as-enacted functions and Art 49(4)(b) still names point 9 | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date`; `Annex VIII Section B as amended the information at the point must be provided and kept up to date`; `Annex VIII Section B the information at the point must be provided and kept up to date` |
| 1872-1872 | Annex VIII Section C heading | inert | reason 1 (not operative: a heading) |  |
| 1873-1873 | Annex VIII Section C introduction | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1874-1874 | Annex VIII Section C point 1 | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1875-1875 | Annex VIII Section C point 2 | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1876-1876 | Annex VIII Section C point 3 | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1877-1877 | Annex VIII Section C point 4 | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1878-1878 | Annex VIII Section C point 5 | encoded |  | `Annex VIII Section C the information at the point must be provided and kept up to date`; `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |
| 1879-1880 | Annex IX heading | inert | reason 1 (not operative: a heading) |  |
| 1881-1881 | Annex IX introduction | fork | F-49-4-gate, F-IX-bearer | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| 1882-1882 | Annex IX point 1 | encoded |  | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| 1883-1883 | Annex IX point 2 | encoded |  | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| 1884-1884 | Annex IX point 3 | encoded |  | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| 1885-1885 | Annex IX point 4 | encoded |  | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| 1886-1886 | Annex IX point 5 | encoded |  | `Annex IX the information at the point must be provided and kept up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |

Inert rows, by reason:

- Reason 1 (not operative: a heading): the 19 heading rows above (Chapter III Section 5, Articles 40 to 49, Annexes V, VI, VIII and IX, and Annex VIII Sections A, B and C).
- Reason 2 (machinery), lines 660-660, Art 41(1) third subparagraph: Art 41(1) third subparagraph: the committee procedure for adopting the implementing acts (Art 98(2)).
- Reason 2 (machinery), lines 693-693, Art 43(5) first subparagraph: Art 43(5): the Commission's power to amend Annex VI by delegated act.
- Reason 2 (machinery), lines 694-694, Art 43(6) first subparagraph: Art 43(6): the Commission's power to amend Article 43(1) and (2) by delegated act.
- Reason 2 (machinery), lines 729-729, Art 47(5) first subparagraph: Art 47(5): the Commission's power to amend Annex V by delegated act.
- Reason 3: none (no row of this part is shown repealed or blank except the two deleted points, which have their own disposition).

## Fork register (P5)

Every ambiguity of this part, the readings I saw, the one I took, and the text that licenses it.
Each entry names the rule that encodes the chosen reading; the coverage table points here by the id.
The quotations were checked against the consolidated text and the base text by `work/gen/verify_quotes.py`, which also looks up the quotations from the Guide, the brief and the keel notes that the entries below rely on (109 fragments in all, 0 not found).

Inherited from the keel, not mine to change:

- **F-113-groups** (keel; assumed, a call for a lawyer): Art 113 as amended dates six sets of provisions and no point of it dates Chapter III Section 5, so the second paragraph's general date (2 August 2026) reaches Articles 40 to 49; the Annexes follow the Article that gives them effect.
  The other reading: Section 5 follows Sections 1 to 3 (2 December 2027, 2 August 2028).
  Shown in `P5-tests-section-5-gap.l4`; recorded as marginal reading M-1.
- **F-111-2-nothing** (keel): a system saved by Art 111(2) gets `NOTHING` from every function of this part that takes the system's facts, not `JUST FALSE`.
  Counted under Split sites (iii).

Mine:

- **F-P5-saving**: a provision addressed to a provider, an authorised representative, a deployer or a product manufacturer of one high-risk AI system passes the system's route, placement date and design change to the keel's applicability function (so Art 111(2) may save it); a provision addressed to a notified body, the Commission, a market surveillance authority or a Member State passes the core's constants, because those are not operators (Art 3(8)).
  Art 49(2), 49(4), 49(5) and Annex IX pass the date only (F-49-2-saving, F-49-4-gate).
  The other reading: apply Art 111(2) to every provision of this part.
  Encoded in `P5-section-5.l4` (`Art 40 to 49 the provisions apply to the high-risk AI system on the date asked`).

- **F-40-42-limits** (Art 40(1), Art 41(3), Art 42(1), Art 42(2); consolidated lines 640, 662, 668, 669).
  Readings: (a) these presumptions are limited by a relative clause ("which are in conformity with", "that have been trained and tested", "that have been certified") or by "to the extent that" or "in so far as"; none is gated by "where", "when" or "upon", so rule (b) of the periods ruling does not reach them, and a system outside the limit gets NOTHING (rule (c): a scope limit with no "only").
  (b) a system outside the limit is not presumed to comply: JUST FALSE, read like the "Where" of Art 42(3).
  Taken: (a) NOTHING (the periods ruling, item (c), the Guide's line 93).
  Licensed by: "which are in conformity with harmonised standards" ... "to the extent that those standards cover those requirements or obligations" (Art 40(1)); "which are in conformity with the common specifications" ... "to the extent those common specifications cover those requirements or those obligations" (Art 41(3)); "that have been trained and tested on data reflecting the specific geographical, behavioural, contextual or functional setting" (Art 42(1)); "in so far as the cybersecurity certificate or statement of conformity or parts thereof cover those requirements" (Art 42(2)).
  Encoded in: `Art 40(1) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2`, `Art 40(1) the general-purpose AI model is presumed ...`, `Art 41(3) ...` (both), `Art 42(1) ...`, `Art 42(2) ...`.
  Reading rests on: a presumption limited by a relative clause, "to the extent that" or "in so far as" (not gated by "where", "when" or "upon").
  None of the four provisions has a "where", "when" or "upon" gate, so rule (b) of the periods ruling does not reach them; the limit is a scope limit with no "only", and outside it the answer is `NOTHING`.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (c) (inputs/ENCODING-GUIDE.md line 93): “(c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`”.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “Everywhere else it answers `NOTHING`”.
- **F-41-1** (Art 41(1) first subparagraph; consolidated line 652).
  Readings: (a) where the conditions are not all fulfilled the Commission may not adopt common specifications: JUST FALSE.
  (b) the sentence does not speak: NOTHING.
  Taken: (a) JUST FALSE (ruling of 2026-11-05 reading (b): "where" gates a "may").
  Licensed by: "The Commission may adopt, implementing acts establishing common specifications ... where the following conditions have been fulfilled".
  Encoded in: `Art 41(1) the Commission may adopt implementing acts establishing common specifications`.
  Split site: a "may" gated by "where".
  The gate is "where the following conditions have been fulfilled" on a "may" and the answer when it fails is `JUST FALSE`.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  The brief leaves this group (a "may" gated by "where", "when" or "upon") as the Guide's rulings give it and calls it a question for a lawyer; it holds 3 sites (F-41-1, F-43-3-opt, F-46-1) and 5 functions.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (3) (BRIEF.md line 34): “"may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer)”.
- **F-41-5** (Art 41(5); consolidated line 664).
  Readings: (a) a provider that has not duly justified has not met the duty: JUST FALSE.
  (b) "duly" is a judgment the text does not settle: NOTHING.
  Taken: (a) JUST FALSE, case by case; "duly" is a plain input.
  Licensed by: "shall duly justify that they have adopted technical solutions that meet the requirements ... to a level at least equivalent thereto".
  Encoded in: `Art 41(5) the provider has met the duty to duly justify the technical solutions`.
  Split site: a bare "must" not done.
  The duty is a bare "shall duly justify" that the provider has not met, and no ruling covers it: the Guide leaves it to the encoder, with one fork line.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “an "unless" or "except" once it is met; a bare "must" not done”.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule”.
  Marginal: listed as M-9 under Marginal readings for a lawyer, because the Guide gives no answer for this site; the answer, `JUST FALSE`, is the encoder's, and "duly" stays a plain input.
- **F-42-3-where** (Art 42(3) as amended; consolidated line 671).
  Readings: (a) the "Where" gate fails (the system is outside the scope of Regulation (EU) 2024/2847, or the conditions of its Article 12(1) are not fulfilled): JUST FALSE, the deeming does not apply on these facts (the periods ruling, rule (b)); a deeming rule is neither a duty nor a "may", so neither the duty line nor the grant ruling of 2026-11-12 sends it to a lawyer.
  (b) NOTHING: the text does not say that such a system fails to comply (the In-short paragraph's "Everywhere else it answers NOTHING").
  Taken: (a) JUST FALSE (the periods ruling, item (b), the Guide's line 93).
  Licensed by: "Where high-risk AI systems fall within the scope of Regulation (EU) 2024/2847 and the conditions laid down in Article 12(1) of that Regulation are fulfilled, such systems shall be deemed to comply with the cybersecurity requirements set out in Article 15".
  Encoded in: `Art 42(3) as amended the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15`, reached through its dispatcher `Art 42(3) the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15`.
  Split site: a deeming rule gated by "where" (neither a duty nor a "may").
  The gate is "Where high-risk AI systems fall within the scope ... and the conditions ... are fulfilled" on a deeming rule, and when it fails the answer is `JUST FALSE`.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  The function is the provision's own question and is not named for a grant, so the brief's limit (1) does not move it to `NOTHING` and its limit (3) ("may" functions gated by "where") does not apply; the brief keeps `JUST FALSE` there.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (2) (BRIEF.md line 34): “Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (3) (BRIEF.md line 34): “"may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer)”.
  The other reading, `NOTHING`, rests on the In-short paragraph's last line for the case the text does not speak to; the periods ruling is the more specific line and I followed it.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “Everywhere else it answers `NOTHING`”.
- **F-43-1** (Art 43(1) second subparagraph; consolidated lines 678, 679, 680, 681, 682).
  Readings: (a) points (a) to (d) are alternatives: the provider follows Annex VII where any one holds.
  (b) points (a) to (d) are cumulative.
  Taken: (a) alternatives.
  Licensed by: points (a) to (d) of the second subparagraph are separated by semicolons with nothing joining them; the first subparagraph says "shall opt for one of" and the second says "shall follow" Annex VII where a point holds.
  Encoded in: `Art 43(1) the conformity assessment procedure the provider is to follow`.
- **F-43-1b** (Art 43(1) second subparagraph point (b); consolidated line 680).
  Readings: (a) point (b) is the case where a harmonised standard exists and the provider has not applied it or has applied only part of it.
  (b) point (b) also covers a provider that has applied no standard where none exists (the case of point (a)).
  Taken: (a) the question is put to the provider in the words of point (b).
  Licensed by: "the provider has not applied, or has applied only part of, the harmonised standard".
  Encoded in: `Art 43(1) the conformity assessment procedure the provider is to follow`.
- **F-43-3-power** (Art 43(3) second subparagraph; consolidated line 687).
  Readings: (a) a notified body not shown to have been assessed has no such power: JUST FALSE.
  (b) the sentence does not speak: NOTHING.
  Taken: (b) NOTHING: a "provided that" on a grant (the grant ruling).
  Licensed by: "shall be entitled to control the conformity ... provided that the compliance of those notified bodies ... has been assessed in the context of the notification procedure" (as enacted); "shall have the power to assess ... which is evidenced through the assessment as part of the existing notification" (as amended).
  Encoded in: `Art 43(3) second subparagraph the notified body has the power to assess the conformity of the high-risk AI system with the requirements set out in Section 2`.
  Split site: a grant limited in its own wording.
  The power is limited by a "provided that" (as enacted) or by "evidenced through the assessment as part of the existing notification" (as amended), and the case falls outside the limit: `NOTHING`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
- **F-43-3-opt** (Art 43(3) third subparagraph; consolidated line 688).
  Readings: (a) a manufacturer that has not applied the standards may not use the option: JUST FALSE.
  (b) the sentence does not speak where the "provided that" gate fails: NOTHING; a missing option ("Where ... provides") is JUST FALSE.
  Taken: "Where" fails: JUST FALSE (ruling (b)); "provided that" fails: NOTHING (grant ruling); "only if" fails: JUST FALSE.
  Licensed by: "Where a legal act ... enables the product manufacturer to opt out ..., provided that that manufacturer has applied ..., that manufacturer may use that option only if it has also applied ...".
  Encoded in: `Art 43(3) third subparagraph as enacted the product manufacturer may use the option not to have a third-party conformity assessment` and its as-amended twin, joined by the dispatcher `Art 43(3) third subparagraph the product manufacturer may use the option not to have a third-party conformity assessment`.
  Split site: a "may" gated by "where", "provided that" and "only if".
  "Where a legal act ... enables" (as enacted) and "Where Union harmonisation legislation ... provides" (as amended): no such option gives `JUST FALSE`.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (3) (BRIEF.md line 34): “"may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer)”.
  "provided that that manufacturer has applied ...": a "provided that" on a grant gives `NOTHING`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
  "may use that option only if it has also applied ...": the text closes the gate itself, so `JUST FALSE`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, first sentence (inputs/ENCODING-GUIDE.md line 86): “a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except")”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (2) (BRIEF.md line 34): “Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”.
- **F-44-2-both** (Art 44(2) first sentence; consolidated line 698).
  Readings: (a) a system covered by both Annexes (Art 43(3) fourth subparagraph) has both limits and the shorter binds: 4 years.
  (b) the longer limit: 5 years.
  Taken: (a) the shorter, 4 years.
  Licensed by: "shall not exceed five years for AI systems covered by Annex I, and four years for AI systems covered by Annex III" (a system covered by both is within both clauses).
  Encoded in: `Art 44(2) the longest period in years that a certificate may indicate`.
- **F-44-2-extension** (Art 44(2) second sentence; consolidated line 698).
  Readings: (a) no request by the provider: NOTHING; no re-assessment: NOTHING (the grant rule for both).
  (b) "At the request of the provider" is read like "upon request", a gate on a "may": no request gives JUST FALSE (the periods ruling, rule (b)); "based on a re-assessment" is a basis the text does not close with "only": no re-assessment gives NOTHING.
  Taken: request missing: NOTHING; re-assessment missing: NOTHING (both: the grant rule, because the gate words are not "where", "when" or "upon").
  Licensed by: "At the request of the provider, the validity of a certificate may be extended for further periods" ... "based on a re-assessment in accordance with the applicable conformity assessment procedures".
  Encoded in: `Art 44(2) the validity of a certificate may be extended for a further period`.
  Split site: a "may" with two gates.
  "At the request of the provider" is a gate on a "may" that is not "where", "when" or "upon", so the grant rule gives `NOTHING` when there is no request.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
  "based on a re-assessment" is a basis the text does not close with "only": `NOTHING` when there is no re-assessment.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  The nearest line of the Guide that gives `JUST FALSE` is the delegated-definitions ruling's item (c), which names "when", "upon" and "whenever"; it does not name "at the request of", and I did not extend it.
  Relies on the Guide, section 5, the delegated-definitions ruling of 2026-11-05, item (c) (inputs/ENCODING-GUIDE.md line 94): “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”.
  Marginal: listed as M-8 under Marginal readings for a lawyer, because "at the request of" fits no line of the Guide exactly; read like "upon request" it would give `JUST FALSE`.
- **F-44-2-supplement** (Art 44(2) last sentence; consolidated line 698).
  Readings: (a) where the certificate is not valid the supplement does not remain valid (the text's own "provided that" read as "if"): JUST FALSE.
  (b) NOTHING.
  Taken: (a) JUST FALSE.
  Licensed by: "Any supplement to a certificate shall remain valid, provided that the certificate which it supplements is valid".
  Encoded in: `Art 44(2) the supplement to a certificate remains valid`.
  Split site: a statement whose "provided that" is unmet.
  "provided that the certificate which it supplements is valid" is the text's own condition on whether a supplement remains valid, a status and not a grant, and I read "provided that" as a plain variant of "if": `JUST FALSE` when it is not met.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, first sentence (inputs/ENCODING-GUIDE.md line 86): “a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except")”.
  The brief keeps `JUST FALSE` "for a bar, a duty or the provision's own question", which is what this function is.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (2) (BRIEF.md line 34): “Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”.
  Marginal: listed as M-8 under Marginal readings for a lawyer, because the Guide names "while", "until" and "except" as plain variants of "if" and does not name "provided that".
- **F-44-2-period** (Art 44(2) first sentence; consolidated line 698).
  Readings: (a) the period the certificate indicates runs from its first day of validity to its last day of validity, both included, and it does not exceed the limit where the last day is at most the day before the anniversary of the first day that falls the limit's number of years later (1 January 2026 to 31 December 2030 is five years); a first day of 29 February has its anniversary on 1 March in a common year (the library's date arithmetic), so the last day is 28 February.
  (b) the anniversary itself is the last permitted day.
  (c) the caller counts whole years: withdrawn, because a certificate valid for five years and six months would be passed as five.
  Taken: (a) the day before the anniversary is the last day; the period is computed from the two dates (the flat negative "shall not exceed", the Guide's line 86).
  Licensed by: "Certificates shall be valid for the period they indicate, which shall not exceed five years for AI systems covered by Annex I, and four years for AI systems covered by Annex III".
  Encoded in: `Art 44(2) the period the certificate indicates is within the limit`.
  Reading rests on: a flat negative over a period computed from two dates.
  "shall not exceed" is a flat negative: a period over the limit gets `JUST FALSE`; the end day (the day before the anniversary) is the encoder's reading, not a ruling.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, first sentence (inputs/ENCODING-GUIDE.md line 86): “a flat negative ("does not", "shall not", "may not")”.
- **F-44-3-unless** (Art 44(3) first sentence; consolidated line 699).
  Readings: (a) once the provider has taken appropriate corrective action and compliance is ensured within the deadline, the duty falls away: JUST FALSE (the text's own "unless").
  (b) the duty is never lifted.
  Taken: (a) JUST FALSE, decided case by case.
  Licensed by: "suspend or withdraw the certificate issued or impose restrictions on it, unless compliance with those requirements is ensured by appropriate corrective action".
  Encoded in: `Art 44(3) the notified body must suspend or withdraw the certificate issued or impose restrictions on it`.
  Split site: an "unless" once it is met.
  The Guide lists "unless" among the words that give `JUST FALSE`, and also lists an "unless" once it is met among the questions it leaves to the encoder; I took `JUST FALSE`, with this fork line.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, first sentence (inputs/ENCODING-GUIDE.md line 86): “a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except")”.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “an "unless" or "except" once it is met; a bare "must" not done”.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule”.
  Marginal: listed as M-9 under Marginal readings for a lawyer, because the Guide's two lines point at the same answer but the second leaves it to the encoder.
- **F-45-1-e** (Art 45(1)(e), 45(2)(a), 45(2)(b), 45(3); consolidated lines 708, 710, 711, 712).
  Readings: (a) "on request" / "upon request" gates a duty: no request gives JUST FALSE (rule (c) of the periods ruling of 2026-11-05).
  (b) no request gives NOTHING.
  Taken: (a) JUST FALSE where no request has been made.
  Licensed by: "(e) on request, conformity assessment activities performed within the scope of their notification"; "and, upon request, of quality system approvals which it has issued"; "and, upon request, of the certificates and/or supplements thereto which it has issued"; "negative and, on request, positive conformity assessment results".
  Encoded in: `Art 45(1) the notified body must inform the notifying authority of the item`, `Art 45(2) the notified body must inform the other notified bodies of the item`, `Art 45(3) the notified body must provide the other notified body with relevant information on the kind of results`.
  Split site: a duty gated by "upon request" or "on request".
  Art 45(2)(a) and 45(2)(b) say "upon request": "upon" counts as "where", and a failed "where" gives `JUST FALSE`.
  Relies on the Guide, section 5, the delegated-definitions ruling of 2026-11-05, item (c) (inputs/ENCODING-GUIDE.md line 94): “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  Art 45(1)(e) and Art 45(3) say "on request", which the Guide does not name; I read it like "upon request", and the Guide leaves "a duty whose "if" or "where" is unmet" to the encoder.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “a duty whose "if" or "where" is unmet”.
  Relies on the Guide, section 5, the "Questions with no convention" ruling (the maintainer, typed 2026-11-05T10:25:24Z) (inputs/ENCODING-GUIDE.md line 95): “Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule”.
  Marginal: listed as M-8 under Marginal readings for a lawyer, because "on request" (Art 45(1)(e) and Art 45(3)) fits no line of the Guide exactly; the other reading is `NOTHING`.
- **F-46-1** (Art 46(1); consolidated line 716).
  Readings: (a) no duly justified request, or a reason outside the exceptional reasons listed: JUST FALSE.
  (b) a different reason: NOTHING (the list limits the grant in its own wording and is not closed by "only").
  Taken: no request: JUST FALSE ("upon" gate, ruling (b)); different reason: NOTHING.
  Licensed by: "By way of derogation from Article 43 and upon a duly justified request, any market surveillance authority may authorise ... for exceptional reasons of public security or the protection of life and health of persons, environmental protection or the protection of key industrial and infrastructural assets".
  Encoded in: `Art 46(1) the market surveillance authority may authorise the placing on the market or the putting into service of a specific high-risk AI system within the territory of its Member State`.
  Split site: a "may" gated by "upon" and a list of reasons.
  "upon a duly justified request": "upon" counts as "where", and a failed "where" gives `JUST FALSE`.
  Relies on the Guide, section 5, the delegated-definitions ruling of 2026-11-05, item (c) (inputs/ENCODING-GUIDE.md line 94): “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  The brief leaves this group as the Guide's rulings give it and calls it a question for a lawyer (3 sites, 5 functions; see F-41-1).
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (3) (BRIEF.md line 34): “"may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer)”.
  "for exceptional reasons of ..." is a list of reasons not closed with "only": a different reason gives `NOTHING`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
- **F-46-2** (Art 46(2); consolidated line 717).
  Readings: (a) no situation of urgency: NOTHING; authorisation not requested without undue delay: NOTHING (the grant rule for both).
  (b) "In a duly justified situation of urgency" is a gate on a "may" read like "where": no urgency gives JUST FALSE (the periods ruling, rule (b)); "provided that" on a grant: not requested gives NOTHING.
  Taken: no urgency: NOTHING ("In a duly justified situation" is not "where", "when" or "upon"); not requested: NOTHING ("provided that" on a grant).
  Licensed by: "In a duly justified situation of urgency ... may put a specific high-risk AI system into service without the authorisation ..., provided that such authorisation is requested during or after the use without undue delay".
  Encoded in: `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into service without the authorisation`.
  Split site: a "may" gated by "In a duly justified situation" and "provided that".
  "In a duly justified situation of urgency" is a gate on a "may" that is not "where", "when" or "upon", so the grant rule gives `NOTHING` when there is no such situation.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
  "provided that such authorisation is requested" is a "provided that" on a grant: `NOTHING` when it is not requested.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
  Marginal: listed as M-8 under Marginal readings for a lawyer, because "In a duly justified situation of urgency" fits no line of the Guide exactly; read like "where" it would give `JUST FALSE`.
- **F-46-4** (Art 46(4); consolidated line 719).
  Readings: (a) an objection raised by a Member State or the Commission within the 15 calendar days makes the "where" fail: JUST FALSE (the periods ruling, rule (b)); no objection and the 15 days still running: NOTHING (the "where" has neither failed nor been met); no objection and the 15 days run: JUST TRUE; the days are counted from the date of receipt and the date asked, and have run from the date of receipt plus 15 days.
  (b) the window includes the fifteenth day, so JUST TRUE only from the date of receipt plus 16 days.
  (c) while the window is open the "where" is not yet fulfilled: JUST FALSE.
  (d) the caller counts the days: withdrawn.
  Taken: (a) objection: JUST FALSE; window open: NOTHING; window run: JUST TRUE; the date of receipt plus 15 days is the first day on which the authorisation is deemed justified.
  Licensed by: "Where, within 15 calendar days of receipt of the information referred to in paragraph 3, no objection has been raised by either a Member State or the Commission" ... "that authorisation shall be deemed justified".
  Encoded in: `Art 46(4) the authorisation is deemed justified`.
  Split site: a deeming rule gated by "where" and a period of 15 calendar days.
  An objection raised within the period makes the "where" fail on a deeming rule that is neither a duty nor a "may": `JUST FALSE`.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
  While the 15 days are still running with no objection the "where" has neither failed nor been met, so no line of the Guide gives `JUST FALSE` and the answer is `NOTHING`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “Everywhere else it answers `NOTHING`”.
- **F-47-1-form** (Art 47(1) first sentence; consolidated line 725).
  Readings: (a) "written machine readable, physical or electronically signed" lists three forms, any one of which will do; a declaration in none of them: NOTHING (list not closed).
  (b) the forms are cumulative.
  Taken: (a) any one of the three; none of them: NOTHING.
  Licensed by: "The provider shall draw up a written machine readable, physical or electronically signed EU declaration of conformity".
  Encoded in: `Art 47(1) the declaration is in a form the paragraph names`.
- **F-47-1-period** (Art 47(1) first sentence, second limb; consolidated line 725).
  Readings: (a) the ten years run to the day before the tenth anniversary of the placement date (the placement day is the first day of the first year): inside it JUST TRUE, after it JUST FALSE (the periods ruling, rule (a)); the function computes the last day from the date asked and the placement date, so a system placed on 1 January 2028 is outside the period on 1 October 2038 (ten years and nine months) and on the tenth anniversary itself; a placement on 29 February has its tenth anniversary on 1 March in a common year (the library's date arithmetic), so the last day is 28 February; a date asked before the placement date is inside the period, as the function always answered (it has never tested the lower end).
  (b) the tenth anniversary itself is the last day (the period ends on the day that bears the placement date ten years later).
  (c) the caller counts whole years since placement: withdrawn, because a caller can only honestly pass 10 for ten years and nine months and the function then answers JUST TRUE.
  Taken: (a) the day before the tenth anniversary is the last day (a period the text fixes in its own words, the Guide's line 93).
  Licensed by: "keep it at the disposal of the national competent authorities for 10 years after the high-risk AI system has been placed on the market or put into service".
  Encoded in: `Art 47(1) the provider must keep the declaration at the disposal of the national competent authorities` and `Art 47(1) the provider's duty to keep the declaration at the disposal of the national competent authorities`.
  Reading rests on: a period the text fixes in its own words, computed from two dates.
  "for 10 years after" is a period the text fixes in its own words: outside it the answer is `JUST FALSE`; the end day (the day before the tenth anniversary) is the encoder's reading, not a ruling.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (a) (inputs/ENCODING-GUIDE.md line 93): “(a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`”.
- **F-47-1-request** (Art 47(1) third sentence; consolidated line 725).
  Readings: (a) "upon request" gates the duty to submit a copy: no request gives JUST FALSE (the periods rule (c)).
  (b) NOTHING.
  Taken: (a) JUST FALSE where no authority has requested a copy.
  Licensed by: "A copy of the EU declaration of conformity shall be submitted to the relevant national competent authorities upon request".
  Encoded in: `Art 47(1) a copy of the declaration must be submitted to the relevant national competent authorities`.
  Split site: a duty gated by "upon request".
  "upon" counts as "where", and a failed "where" gives `JUST FALSE`.
  Relies on the Guide, section 5, the delegated-definitions ruling of 2026-11-05, item (c) (inputs/ENCODING-GUIDE.md line 94): “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”.
  Relies on the Guide, section 5, the periods ruling of 2026-11-05, item (b) (inputs/ENCODING-GUIDE.md line 93): “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”.
- **F-48-2** (Art 48(2); consolidated line 733).
  Readings: (a) two propositions: a digital CE marking must be used for a system provided digitally; and it may be used only if it can easily be accessed through the interface or by a machine-readable code or other electronic means.
  (b) one proposition.
  Taken: (a) two propositions.
  Licensed by: "a digital CE marking shall be used, only if it can easily be accessed via the interface from which that system is accessed or via an easily accessible machine-readable code or other electronic means".
  Encoded in: `Art 48(2) a digital CE marking must be used`, `Art 48(2) the digital CE marking may be used`.
- **F-48-4-affix** (Art 48(4) second sentence; consolidated line 735).
  Readings: (a) the notified body, the provider under its instructions, or the authorised representative under its instructions may affix; without the instructions the sentence does not speak: NOTHING.
  (b) the provider may affix it in any case: JUST TRUE.
  Taken: (a) NOTHING without the notified body's instructions (a limit on a grant in its own wording).
  Licensed by: "The identification number of the notified body shall be affixed by the body itself or, under its instructions, by the provider or by the provider’s authorised representative".
  Encoded in: `Art 48(4) the person may affix the identification number of the notified body`.
  Split site: a grant limited in its own wording.
  "by the body itself or, under its instructions, by the provider or by the provider's authorised representative" limits who may affix the number, and the case without the instructions falls outside the limit: `NOTHING`.
  Relies on the Guide, section 5, "Rulings on negatives and legal effects", the "In short" paragraph, second sentence (inputs/ENCODING-GUIDE.md line 87): “limits a grant or prohibition in its own wording and the case falls outside the limit”.
  Relies on the brief (BRIEF.md; not in the Guide copy), the grant ruling of 2026-11-12, limit (1) (BRIEF.md line 34): “A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails”.
- **F-49-1-rep** (Art 49(1) and Art 49(2); consolidated lines 739, 740).
  Readings: (a) the registrant is the authorised representative where one applies, else the provider: exactly one is bound.
  (b) both are bound.
  Taken: (a) exactly one is bound.
  Licensed by: "the provider or, where applicable, the authorised representative shall register themselves and their system" (Art 49(1)); "that provider or, where applicable, the authorised representative shall register themselves and that system" (Art 49(2)).
  Encoded in: `Art 49(1) the provider must register themselves and their system` and `Art 49(1) the authorised representative must register themselves and the system` (and the Art 49(2) pair); `Art 49 the authorised representative`.
- **F-49-before** (Art 49(1), (2), (3); consolidated lines 739, 740, 741).
  Readings: (a) "Before placing on the market" is read at the granularity of a day: a registration on the placing day counts as in time.
  (b) it must be strictly before the placing day.
  Taken: (a) a registration on the day is in time.
  Licensed by: "Before placing on the market or putting into service a high-risk AI system".
  Encoded in: `Art 49(1) the registration was made before the placing on the market or the putting into service`, `Art 49(2) ...`, `Art 49(3) the registration was made before the putting into service or the use`.
- **F-49-2-saving** (Art 49(2); consolidated line 740).
  Readings: (a) the paragraph is about a system its provider has concluded is NOT high-risk (Art 6(3)), so Art 111(2), which speaks of high-risk AI systems, is not applied: the date only.
  (b) apply the saving as for high-risk systems.
  Taken: (a) the date only.
  Licensed by: "an AI system for which the provider has concluded that it is not high-risk according to Article 6(3)".
  Encoded in: `Art 49(2) the provider must register themselves and the AI system`.
- **F-49-3-acts** (Art 49(3); consolidated line 741).
  Readings: (a) "register themselves, select the system and register its use" is one act of registering.
  (b) three acts, each with its own deadline.
  Taken: (a) one act, one deadline.
  Licensed by: "shall register themselves, select the system and register its use in the EU database".
  Encoded in: `Art 49(3) the deployer must register themselves, select the system and register its use in the EU database`.
- **F-49-4-areas** (Art 49(4); consolidated line 742).
  Readings: (a) the points (1, 6, 7 of Annex III) and the areas (law enforcement, migration, asylum and border control) are both required.
  (b) the areas merely describe the three points.
  Taken: (a) both required.
  Licensed by: "referred to in points 1, 6 and 7 of Annex III, in the areas of law enforcement, migration, asylum and border control management".
  Encoded in: `Art 49(4) the high-risk AI system is one of those referred to in points 1, 6 and 7 of Annex III in the areas of law enforcement, migration, asylum and border control management`.
- **F-49-4-gate** (Art 49(4), Art 49(5), Annex IX; consolidated lines 742, 748, 1881).
  Readings: (a) these pass the date only (the restricted section and who may see it do not depend on one system's history; testing in real world conditions happens before any placing on the market).
  (b) pass the system's facts and apply Art 111(2).
  Taken: (a) the date only.
  Licensed by: no text speaks to Art 111(2) here.
  Encoded in: `Art 49(4) ...`, `Art 49(5) ...`, `Annex IX ...`.
- **F-49-4-bearer** (Art 49(4) first subparagraph; consolidated line 742).
  Readings: (a) the text names no bearer for where the registration is made; the person who registers is the provider (or the authorised representative), so the rule is the provider's and has no time limit: no breach path.
  (b) no rule.
  Taken: (a) the provider's rule, no breach path.
  Licensed by: "the registration referred to in paragraphs 1, 2 and 3 of this Article shall be in a secure non-public section".
  Encoded in: `Art 49(4) first subparagraph` rule.
- **F-49-4-b-point-9** (Art 49(4)(b) as amended; consolidated line 744).
  Readings: (a) point 9 of Section B is deleted by the Omnibus, so the reference to it has nothing to refer to: NOTHING ("repealed or blank").
  (b) the paragraph still names point 9 and so still lists whatever point 9 held: JUST TRUE.
  Taken: (a) NOTHING for points 7 and 9.
  Licensed by: "(b) Section B, points 1 to 5, and points 8 and 9 of Annex VIII;" against consolidated lines 1865 and 1869 ("▼M1 DELETED").
  Encoded in: `Art 49(4)(b) as amended the Section B point is within the restricted registration`.
- **F-S14-reach** (Art 2(2) (consolidated line 41, outside my ranges) with Articles 40 to 49 and Annexes V, VI and VIII).
  Readings: (a) the functions addressed to an operator of one high-risk AI system (a provider, an authorised representative, a deployer or a product manufacturer, in the provision's own steps) ask Art 2(2) and answer JUST FALSE where it does, and the functions addressed to anyone else (the Commission, the participants in the standardisation process, a notified body, a market surveillance authority, a Member State), the general-purpose AI model limbs, the twins that a dispatcher calls, the two definitions that take no date, Art 49(2), Art 49(4), Art 49(5) and Annex IX do not ask it.
  (b) every function of this part asks it, because Art 2(2) is a list closed by "only" over the whole Regulation.
  (c) none asks it, because Art 2(2) is a statement about operators and each function of this part has its own gate.
  Taken: (a) the operator's functions ask it.
  Licensed by: "only Article 6(1), Article 60a and Articles 102 to 112 shall apply" (Art 2(2) as amended, consolidated line 41); the keel's own row for Art 2(2) makes it an immunity of the operator of such a system "from every provision not listed" and a disability of "the authorities that would enforce those provisions" (inputs/KEEL-NOTES.md line 125).
  Encoded in: `Art 40 to 49 Art 2(2) cuts the provision off from the high-risk AI system` (in `P5-section-5.l4`), called first by every layer-1 function with a `-- S14-kind` branch.
- **F-IX-bearer** (Annex IX; consolidated line 1881).
  Readings: (a) Annex IX does not say who provides the information; Art 60(4)(c) (another part) points at the provider or prospective provider; the question is put to the provider.
  (b) no bearer.
  Taken: (a) the provider (assumed; the bearer is another part's).
  Licensed by: "The following information shall be provided and thereafter kept up to date with regard to testing in real world conditions".
  Encoded in: `Annex IX the information at the point must be provided and kept up to date`.

Forks in the seat layer: none.
A seat question's inputs are the layer-1 inputs; where a layer-1 input is a constructor of a type the seat could have fixed (the person who affixes the number, the duty of Art 46(5), the point of Annex V, the part of the registration), the seat fixes it in the question and says so in the question's name.

## Jural relations (P5)

One row per provision (or group of provisions with the same relation) of this part; each relation is stated once, neutrally, from the side that holds it, with the other side named only where the text names it.
A provision that creates no relation (a definition, a counting rule, a statement of what a procedure is) is listed once as `none`.
Where the text names no bearer or no holder the row says `none named`, and the rule is written for the party the text does name or the one the context fixes (the fork register says where I chose).

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind | L4 rule or function |
| --- | --- | --- | --- | --- |
| Art 40(1) | provider of a high-risk AI system or general-purpose AI model in conformity with a published harmonised standard (a presumption in their favour) | none named | presumption | `Art 40(1) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2`; `Art 40(1) the general-purpose AI model is presumed to be in conformity with the obligation set out in Chapter V, Sections 2 and 3` |
| Art 40(2) first to fourth subparagraphs | none named (the European standardisation organisations are the addressees of the requests) | the Commission (duty) | duty | `Art 40(2) the Commission's duty to issue standardisation requests`; `Art 40(2) the Commission's duty to ask for deliverables on reporting and documentation processes`; `Art 40(2) the Commission's duty to consult the Board and relevant stakeholders`; `Art 40(2) the Commission's duty to specify that standards have to be clear and consistent`; `Art 40(2) the Commission's duty to request evidence of best efforts`; `Art 40(2) the Commission's duty to request standardisation deliverables` |
| Art 40(3) | none named | participants in the standardisation process (duty to seek to promote investment and innovation) | duty | `Art 40(3) the duty of the participants in the standardisation process` |
| Art 41(1) first subparagraph | the Commission (power to adopt implementing acts establishing common specifications) | none named | power | `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` |
| Art 41(1) second subparagraph, 41(2), 41(4) | none named | the Commission (duties to consult the advisory forum, to inform the committee, to assess the standard, to repeal the implementing act) | duty | `Art 41(1) the Commission's duty to consult the advisory forum`; `Art 41(2) the Commission's duty to inform the committee`; `Art 41(4) the Commission's duty to assess the harmonised standard`; `Art 41(4) the Commission's duty to repeal the implementing act` |
| Art 41(3) | provider in conformity with the common specifications (a presumption in their favour) | none named | presumption | `Art 41(3) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2`; `Art 41(3) the general-purpose AI model is presumed to comply with the obligation set out in Chapter V, Sections 2 and 3` |
| Art 41(5) | none named | provider of a high-risk AI system or general-purpose AI model that does not comply with the common specifications (duty to duly justify) | duty | `Art 41(5) the provider's duty to duly justify the technical solutions adopted` |
| Art 41(6) | none named | a Member State (duty to inform the Commission); the Commission (duty to amend the implementing act) | duty | `Art 41(6) the Member State's duty to inform the Commission`; `Art 41(6) the Commission's duty to amend the implementing act` |
| Art 42(1), 42(2), 42(3) | provider of a high-risk AI system trained and tested on the data of the setting, certified under a cybersecurity scheme, or within Regulation (EU) 2024/2847 (a presumption or deemed compliance in their favour) | none named | presumption | `Art 42(1) the high-risk AI system is presumed to comply with the relevant requirements laid down in Article 10(4)`; `Art 42(2) the high-risk AI system is presumed to comply with the cybersecurity requirement set out in Article 15`; `Art 42(3) the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15` |
| Art 43(1) first and second subparagraphs | none named | provider (duty to opt for Annex VI or Annex VII, or to follow Annex VII) | duty | `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` |
| Art 43(1) third subparagraph | provider (privilege to choose any notified body) | none named; the market surveillance authority is under a duty to act as a notified body for law-enforcement, immigration and asylum authorities and Union bodies | privilege; duty | `Art 43(1) the provider's permission to choose any of the notified bodies`; `Art 43(1) the market surveillance authority's duty to act as a notified body` |
| Art 43(2), 43(3) first subparagraph, 43(3) fourth subparagraph | none named | provider (duty to follow Annex VI, or the procedure the Section A legislation requires) | duty | `Art 43(2) the provider's duty to follow the procedure based on internal control`; `Art 43(3) the provider's duty to follow the relevant conformity assessment procedure` |
| Art 43(3) second subparagraph (first and second sentences) | notified body notified under the Section A legislation (power to control or assess the conformity) | none named | power | `Art 43(3) the notified body's permission to assess the conformity of the high-risk AI system` |
| Art 43(3) second subparagraph (last sentence, as amended only) | none named (the designation is made under Section 4, another part) | notified body notified under the Section A legislation (duty to apply for designation by 28 January 2028) | duty with a deadline | `Art 43(3) the duty of the notified body to apply for designation` |
| Art 43(3) third subparagraph | product manufacturer (privilege to use the option not to have a third-party assessment, within the limits of the text) | none named | privilege | `Art 43(3) the product manufacturer's permission to use the option not to have a third-party conformity assessment` |
| Art 43(4) | none named | provider (duty to have a system undergo a new assessment after a substantial modification) | duty | `Art 43(4) the provider's duty to have the high-risk AI system undergo a new conformity assessment procedure` |
| Art 43(5), 43(6) | the Commission (power to amend Annex VI and Art 43(1), (2) by delegated act) | none named | power (inert, reason 2: no rule) | none |
| Annex VI point 1 | none (it defines the procedure) | none | none | `Annex VI point 1 the provider has carried out the conformity assessment procedure based on internal control` |
| Annex VI points 2 to 4 | none named | provider (duty to verify the quality management system, to examine the technical documentation, to verify the design and development process) | duty | `Annex VI point 2 the provider's duty to verify the quality management system`; `Annex VI point 3 the provider's duty to examine the technical documentation`; `Annex VI point 4 the provider's duty to verify the design and development process and the post-market monitoring` |
| Art 44(1) | the relevant authorities of the Member State in which the notified body is established (the certificate is to be understandable to them) | notified body (duty) | duty | `Art 44(1) the notified body's duty to draw up the certificate in a language which can be easily understood` |
| Art 44(2) first and last sentences | none (the period of validity and the validity of a supplement are rules about a certificate) | none | none | `Art 44(2) the longest period in years that a certificate may indicate`; `Art 44(2) the supplement to a certificate remains valid` |
| Art 44(2) second sentence | notified body (power to extend the validity of a certificate at the provider's request) | none named | power | `Art 44(2) the notified body's permission to extend the validity of a certificate` |
| Art 44(3) first and second sentences | none named (the decision concerns the provider's certificate) | notified body (duty to suspend, withdraw or restrict unless corrected; duty to give reasons) | duty | `Art 44(3) the notified body's duty to suspend or withdraw the certificate or impose restrictions`; `Art 44(3) the notified body's duty to give reasons for its decision` |
| Art 44(3) last paragraph | the persons against whom a notified body decides (an appeal procedure must be available) | none named | right (no bearer named) | `Art 44(3) an appeal procedure against decisions of the notified bodies must be available` |
| Art 45(1), 45(2), 45(3) | the notifying authority (45(1)); the other notified bodies (45(2), 45(3)) | notified body (duty to inform, upon request in the cases the text says) | duty | `Art 45(1) the notified body's duty to inform the notifying authority`; `Art 45(2) the notified body's duty to inform the other notified bodies`; `Art 45(3) the notified body's duty to provide the other notified bodies with relevant information` |
| Art 45(4) | none named (the persons whose information is obtained) | notified body (duty to safeguard confidentiality in accordance with Article 78) | duty | `Art 45(4) the notified body's duty to safeguard confidentiality` |
| Art 46(1) | market surveillance authority (power to authorise the placing on the market or putting into service) | none named | power | `Art 46(1) the market surveillance authority's permission to authorise` |
| Art 46(2) first sentence part | law-enforcement or civil protection authority acting as deployer (privilege to put a system into service without the authorisation, provided that it is requested) | none named | privilege | `Art 46(2) the authority's permission to put the system into service without the authorisation` |
| Art 46(2) last sentence | none named (the persons on whom the system was used) | the deployer authority (duties to stop the use and to discard the results and outputs where the authorisation is refused) | duty | `Art 46(2) the deployer's duty to stop the use with immediate effect`; `Art 46(2) the deployer's duty to discard all the results and outputs immediately` |
| Art 46(3) | none named | market surveillance authority (duty to inform the Commission and the other Member States) | duty | `Art 46(3) the market surveillance authority's duty to inform the Commission and the other Member States` |
| Art 46(4) | the authorising Member State (the authorisation is deemed justified after 15 days without objection) | a Member State or the Commission that did not object in time (disability to object) | immunity | `Art 46(4) the authorisation is deemed justified` |
| Art 46(5) | the operators concerned (right to be consulted and to present their views) | the Commission (duty to enter into consultations, to consult the operators, to decide) | right; duty | `Art 46(5) the Commission's duties after an objection` |
| Art 46(6) | the Commission (its consideration that the authorisation is unjustified leads to withdrawal) | market surveillance authority of the Member State concerned (duty to withdraw) | duty | `Art 46(6) the market surveillance authority's duty to withdraw the authorisation` |
| Art 46(7) | none | market surveillance authority (no power under Art 46 for a product under the Section A legislation) | disability | `Art 46(7) the derogation of this Article applies to the high-risk AI system` |
| Art 47(1) to 47(4) and Annex V | national competent authorities (the declaration is kept at their disposal, copied on request, in a language they understand) | provider (duties to draw up, keep ten years, submit on request, state, include the Annex V information, translate, keep up to date; assumes responsibility) | duty; liability | `Art 47(1) the provider's duty to draw up an EU declaration of conformity`; `Art 47(1) the provider's duty to keep the declaration at the disposal of the national competent authorities`; `Art 47(1) the provider's duty to submit a copy upon request`; `Art 47(2) the provider's duty to state in the declaration that the system meets the requirements of Section 2`; `Art 47(2) the provider's duty to include the information set out in Annex V`; `Art 47(2) the provider's duty to translate the declaration`; `Art 47(3) the provider's duty to draw up a single declaration`; `Art 47(4) the provider's duty to keep the declaration up-to-date`; `Annex V the provider's duty to include the point in the declaration` |
| Art 47(5) | the Commission (power to amend Annex V by delegated act) | none named | power (inert, reason 2: no rule) | none |
| Art 48(1) | none (the marking is subject to the general principles of Article 30 of Regulation (EC) No 765/2008) | none named | none | `Art 48(1) the CE marking is subject to the general principles set out in Article 30 of Regulation (EC) No 765/2008` |
| Art 48(2), 48(3), 48(4) first and third sentences, 48(5) | none named | provider (duties to use a digital CE marking, to affix the marking, to follow it with the notified body's number, to indicate the number in promotional material, to indicate other Union law) | duty | `Art 48(2) the provider's duty to use a digital CE marking`; `Art 48(3) the provider's duty to affix the CE marking`; `Art 48(4) the provider's duty to follow the CE marking with the identification number`; `Art 48(4) the provider's duty to indicate the identification number in the promotional material`; `Art 48(5) the provider's duty to indicate in the CE marking that the system also fulfils the requirements of the other Union law` |
| Art 48(4) second sentence | notified body (affixes the number itself); the provider and the authorised representative (under the notified body's instructions) | none named | privilege | `Art 48(4) the permission to affix the identification number of the notified body` |
| Art 49(1), 49(2) | none named (the EU database of Article 71 is the place) | provider, or where applicable the authorised representative (duty to register before placing on the market or putting into service) | duty with a deadline | `Art 49(1) the duty to register before placing on the market or putting into service`; `Art 49(2) the duty to register before placing on the market or putting into service` |
| Art 49(3) | none named | deployer that is a public authority, a Union institution, body, office or agency or a person acting on their behalf (duty to register before putting into service or using) | duty with a deadline | `Art 49(3) the deployer's duty to register before putting into service or using` |
| Art 49(4) first subparagraph | none named | provider (duty to register in the secure non-public section, with only the information listed) | duty | `Art 49(4) the provider's duty to register in the secure non-public section` |
| Art 49(4) second subparagraph | the Commission and the national authorities referred to in Article 74(8) (access to the restricted sections) | everyone else (no access) | privilege; no-right | `Art 49(4) the person has access to the restricted sections of the EU database` |
| Art 49(5) | none named | none named (high-risk AI systems of point 2 of Annex III are to be registered at national level) | none | `Art 49(5) the high-risk AI system must be registered at national level` |
| Annex VIII Sections A and B; Annex IX | none named | provider (duty to provide the information and keep it up to date); for Annex IX the provider or prospective provider (F-IX-bearer) | duty | `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date`; `Annex VIII Section B the provider's duty to provide the information at the point and keep it up to date`; `Annex IX the provider's duty to provide the information at the point and keep it up to date` |
| Annex VIII Section C | none named | deployer (duty to provide the information and keep it up to date) | duty | `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` |

## Marginal readings for a lawyer (P5)

The brief takes two readings as the status quo and leaves them to a lawyer: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Every `JUST FALSE` branch of layer 1 rests on (a) and every `NOTHING` branch of the kind "limited by its own wording" rests on (b); both lists follow, generated from the comments in the layer-1 modules (file stem, line, function, the words relied on).
The notable ones come first.

- **M-1 (Section 5 is dated by the general date; the gap).** Read literally, Art 113 as amended gives Chapter III Section 5 (Articles 40 to 49 and the Annexes of this part) the date of 2 August 2026 while the Section 2 requirements that its provisions serve apply only from 2 December 2027 (Annex III systems) or 2 August 2028 (Annex I systems).
  So on 1 September 2027 a provider of an Annex III system to be placed on the market on 3 December 2027 is already under Art 49(1) (register before placing on the market), Art 47 (draw up an EU declaration stating that the system meets the requirements of Section 2) and Art 43(2) (follow Annex VI), while the requirements themselves are not yet in force.
  The other reading: Section 5 follows Sections 1 to 3.
  `P5-tests-section-5-gap.l4` (20 assertions) shows both answers for the same facts and says what the literal reading does; this file does not say it is the intended law.
  Keel fork F-113-groups.
- **M-2 (Annex VIII Section B point 9 against Art 49(4)(b)).** The Omnibus deletes points 7 and 9 of Annex VIII Section B (consolidated lines 1865 and 1869), but Art 49(4)(b) still lists "points 1 to 5, and points 8 and 9" (line 744) among the information that a restricted registration includes.
  As amended, point 9 has nothing to refer to.
  Taken: `NOTHING` for points 7 and 9 (repealed or blank), `JUST TRUE` for points 1 to 5 and 8, `JUST FALSE` for point 6 (the paragraph says "only the following information").
  The other reading: the paragraph keeps whatever point 9 held (`JUST TRUE`).
  Fork F-49-4-b-point-9; seat question `Under Annex VIII Section B point 9` returns NOTHING as amended.
- **M-3 (who registers).** Art 49(1) and (2) bind "the provider or, where applicable, the authorised representative".
  Taken: exactly one is bound, the representative where one applies, else the provider; the other reading is that both are bound.
  The two seats (provider, rep) are asked the same facts and answer in complement (`-- MIRROR pair-49-1a`, `pair-49-1b`, `pair-49-2a`, `pair-49-2b`).
  Fork F-49-1-rep.
- **M-4 (a day counts as in time).** "Before placing on the market" is read at the granularity of a day: a registration on the placing day is in time.
  The other reading: strictly before.
  Fork F-49-before.
- **M-5 (two limits on a certificate).** A system covered by both Annexes has two limits in Art 44(2) (five years, four years); the shorter binds.
  Fork F-44-2-both.
- **M-6 (the notified body's power as enacted and as amended).** As enacted a notified body notified under the Section A legislation "shall be entitled to control the conformity" provided that its compliance with Article 31(4), (5), (10) and (11) has been assessed; as amended it "shall have the power to assess" it, provided that the same is "evidenced through the assessment as part of the existing notification", and shall apply for designation by 28 January 2028.
  Both are named for a power and answer `NOTHING` where the "provided that" gate fails (the grant ruling); the other reading is `JUST FALSE`.
  Fork F-43-3-power.
- **M-7 (the reach of Article 2(2); fork F-S14-reach, assumed, not ruled).** Article 2(2) says that for a high-risk AI system under Article 6(1) related to products covered by the legislation listed in Section B of Annex I "only Article 6(1), Article 60a and Articles 102 to 112 shall apply".
  Taken: the 93 functions of this part that take the system's route, placement date and design change (59 `MAYBE` functions and 34 regulative rules: the steps of a provider, an authorised representative, a deployer or a product manufacturer) ask the keel's `Art 2(2)` function through `Art 40 to 49 Art 2(2) cuts the provision off from the high-risk AI system` (60 of them first thing in their own body, the other 33 through the function they call).
  Where it answers `JUST FALSE` they answer `JUST FALSE` (a yes or no function), `NOTHING` (a function that answers with a procedure, a body, a place or a registrant) or `FULFILLED` (a regulative rule); where it answers `NOTHING` or `JUST TRUE` they answer on their own provision.
  Not asked (105 of the 198 functions and rules of this part): the Commission's powers and duties (Articles 40(2), 41(1), (2), (4), (6)), the participants in the standardisation process (Article 40(3)), what Article 46(1), (3), (4), (5), (6) gives the market surveillance authorities, the Commission and the Member States, the notified body's own administration (Article 43(3) second subparagraph and designation, Articles 44 and 45), the general-purpose AI model limbs (Articles 40(1), 41(3), 41(5)), the as-enacted and as-amended twins that a dispatcher calls (the dispatcher asks), the two definitions that take no date (Annex VI point 1, and Art 43(4) "the changes do not constitute a substantial modification"), Art 49(2) (a system the provider has concluded is not high-risk), Art 49(4), Art 49(5) and Annex IX.
  The other readings: every function of this part asks (Article 2(2) is a list closed by "only" over the whole Regulation, so a notified body's certificate duties and the Commission's powers would be cut too), or none does (Article 2(2) is about operators and each function has its own gate).
  The keel's own row for Art 2(2) makes it an immunity of the operator and a disability of the authorities that would enforce the provisions not listed (inputs/KEEL-NOTES.md line 125), which supports the first reading but does not say whether a notified body's duties about a system's certificate (Article 44) are cut too.
  An Annex takes the Article that gives it effect (Annex V with Article 47, Annex VI with Article 43, Annex VIII with Article 49), the same assumption as the group (F-113-groups).
- **M-8 (four sites that fit no line of the Guide exactly).** The Guide's rulings name "where", "when", "upon" and "whenever", "if" and its plain variants, and these four sites use other words.
  "At the request of the provider" (Art 44(2)) and "In a duly justified situation of urgency" (Art 46(2)) gate a "may": taken `NOTHING` (the grant rule); read like "upon" or "where" they would be `JUST FALSE` (F-44-2-extension, F-46-2).
  "provided that the certificate which it supplements is valid" (Art 44(2)) gates a status: taken `JUST FALSE` (a plain variant of "if"); the other reading is `NOTHING` (F-44-2-supplement).
  "on request" gates two duties to inform (Art 45(1)(e), Art 45(3)): taken `JUST FALSE` (read like "upon request"); the other reading is `NOTHING` (F-45-1-e).
- **M-9 (two sites the Guide leaves to the encoder).** The Guide's "Questions with no convention" ruling names a bare "must" not done and an "unless" or "except" once it is met, and gives no answer for either; each gets one fork line.
  Art 41(5), the duty to duly justify, not met: taken `JUST FALSE` (F-41-5); Art 44(3), the duty to suspend or withdraw once corrective action ensures compliance: taken `JUST FALSE` (F-44-3-unless); the other reading for both is `NOTHING`.

Reading (a), every `JUST FALSE` branch (74 branches):

| module | line | function | the words relied on |
| --- | --- | --- | --- |
| 40-41-42 | 104 | `Art 40(2) the Commission must issue standardisation requests covering obligations set out in Chapter V, Sectio` | "as applicable" (a condition the text introduces; the Commission's judgment is the input) |
| 40-41-42 | 127 | `Art 40(2) the Commission must consult the Board and relevant stakeholders` | "When preparing a standardisation request" |
| 40-41-42 | 140 | `Art 40(2) the Commission must specify that standards have to be clear and consistent` | "When issuing a standardisation request to European standardisation organisations" |
| 40-41-42 | 282 | `Art 41(1) the Commission may adopt implementing acts establishing common specifications` | "where the following conditions have been fulfilled" (reading (b), fork F-41-1) |
| 40-41-42 | 295 | `Art 41(1) the Commission must consult the advisory forum` | "When drafting the common specifications" |
| 40-41-42 | 308 | `Art 41(2) the Commission must inform the committee that it considers the conditions to be fulfilled` | "Before preparing a draft implementing act" |
| 40-41-42 | 365 | `Art 41(4) the Commission must assess the harmonised standard` | "Where a harmonised standard is adopted by a European standardisation organisation and proposed to the Commission" |
| 40-41-42 | 380 | `Art 41(4) the Commission must repeal the implementing act or the part of it that covers the same requirements` | "When reference to a harmonised standard is published ... or parts thereof which cover the same requirements" |
| 40-41-42 | 404 | `Art 41(5) the provider of the high-risk AI system must duly justify that it has adopted technical solutions at` | "Where providers ... do not comply with the common specifications" |
| 40-41-42 | 416 | `Art 41(5) the provider of the general-purpose AI model must duly justify that it has adopted technical solutio` | "Where providers ... do not comply with the common specifications" |
| 40-41-42 | 435 | `Art 41(5) the provider has met the duty to duly justify the technical solutions` | "they shall duly justify that they have adopted technical solutions that meet the requirements ... to a level at least equivalent thereto" (a bare "shall" not done, case  |
| 40-41-42 | 449 | `Art 41(6) the Member State must inform the Commission with a detailed explanation` | "Where a Member State considers that a common specification does not entirely meet the requirements" |
| 40-41-42 | 464 | `Art 41(6) the Commission must amend the implementing act establishing the common specification` | "if appropriate" (the Commission's judgment is the input) |
| 40-41-42 | 622 | `Art 42(3) as amended the high-risk AI system is deemed to comply with the cybersecurity requirement set out in` | "Where high-risk AI systems fall within the scope ... and the conditions ... are fulfilled" (a "where" gate on a deeming rule: rule (b); fork F-42-3-where) |
| 43-annex-vi | 363 | `Art 43(3) the notified body has met the duty to apply for designation by 28 January 2028` | "by 28 January 2028" (no application by that date) |
| 43-annex-vi | 380 | `Art 43(3) third subparagraph as enacted the product manufacturer may use the option not to have a third-party ` | "Where a legal act listed in Section A of Annex I enables the product manufacturer to opt out" (a "where" gate on a "may": reading (b), fork F-43-3-opt) |
| 43-annex-vi | 385 | `Art 43(3) third subparagraph as enacted the product manufacturer may use the option not to have a third-party ` | "that manufacturer may use that option only if it has also applied harmonised standards or, where applicable, common specifications" |
| 43-annex-vi | 395 | `Art 43(3) third subparagraph as amended the product manufacturer may use the option not to have a third-party ` | "Where Union harmonisation legislation listed in Section A of Annex I provides the product manufacturer with an option" (a "where" gate on a "may": reading (b), fork F-43 |
| 43-annex-vi | 400 | `Art 43(3) third subparagraph as amended the product manufacturer may use the option not to have a third-party ` | "that manufacturer may use that option only if it has also applied harmonised standards or, where applicable, common specifications" |
| 43-annex-vi | 432 | `Art 43(3) third subparagraph as amended the classification of the product as a high-risk AI system affects the` | "does not affect the choice of the conformity assessment procedure"  -- VERSION as amended |
| 43-annex-vi | 464 | `Art 43(3) third subparagraph as amended the manufacturer is required to choose a third-party conformity assess` | "are not required to choose a conformity assessment procedure involving third-party conformity assessment only because the product includes a high-risk AI system as a saf |
| 43-annex-vi | 544 | `Art 43(4) the high-risk AI system must undergo a new conformity assessment procedure` | "in the event of a substantial modification" (reading (a): a failed "if" within the provision) |
| 43-annex-vi | 768 | `Annex VI point 2 the provider has verified the quality management system` | "The provider verifies that the established quality management system is in compliance with the requirements of Article 17" (a bare statement of a step, not done) |
| 43-annex-vi | 787 | `Annex VI point 3 the provider has examined the technical documentation` | "The provider examines the information contained in the technical documentation" (a bare statement of a step, not done) |
| 43-annex-vi | 806 | `Annex VI point 4 the provider has verified the design and development process and the post-market monitoring` | "The provider also verifies that the design and development process of the AI system and its post-market monitoring ... is consistent with the technical documentation" (a |
| 44-45-46 | 71 | `Art 44(2) the period the certificate indicates is within the limit` | "shall not exceed"; the last day is the day before the anniversary (fork F-44-2-period) |
| 44-45-46 | 104 | `Art 44(2) the supplement to a certificate remains valid` | "provided that the certificate which it supplements is valid" (fork F-44-2-supplement) |
| 44-45-46 | 121 | `Art 44(3) the notified body must suspend or withdraw the certificate issued or impose restrictions on it` | "Where a notified body finds that an AI system no longer meets the requirements" (a "where" gate on a duty: reading (b)) |
| 44-45-46 | 123 | `Art 44(3) the notified body must suspend or withdraw the certificate issued or impose restrictions on it` | "unless compliance ... is ensured by appropriate corrective action" (fork F-44-3-unless) |
| 44-45-46 | 227 | `Art 45(1) the notified body must inform the notifying authority of the item` | "on request" (a gate on a duty: fork F-45-1-e) |
| 44-45-46 | 257 | `Art 45(2) the notified body must inform the other notified bodies of the item` | "upon request" (a gate on a duty: fork F-45-1-e) |
| 44-45-46 | 261 | `Art 45(2) the notified body must inform the other notified bodies of the item` | "upon request" (a gate on a duty: fork F-45-1-e) |
| 44-45-46 | 290 | `Art 45(3) the notified body must provide the other notified body with relevant information on the kind of resu` | "on request" (a gate on a duty: fork F-45-1-e) |
| 44-45-46 | 385 | `Art 46(1) the market surveillance authority may authorise the placing on the market or the putting into servic` | "upon a duly justified request" (a gate on a "may": reading (b), split site (ii), fork F-46-1) |
| 44-45-46 | 459 | `Art 46(2) the use of the high-risk AI system must be stopped with immediate effect` | "If the authorisation referred to in paragraph 1 is refused" |
| 44-45-46 | 478 | `Art 46(2) all the results and outputs of the use must be immediately discarded` | "If the authorisation referred to in paragraph 1 is refused" |
| 44-45-46 | 493 | `Art 46(3) the condition for issuing the authorisation is met` | "shall be issued only if the market surveillance authority concludes" |
| 44-45-46 | 518 | `Art 46(3) the obligation to inform covers the information` | "This obligation shall not cover sensitive operational data in relation to the activities of law-enforcement authorities" |
| 44-45-46 | 537 | `Art 46(4) the authorisation is deemed justified` | "Where, within 15 calendar days ..., no objection has been raised" (reading (b); paragraph 5 then applies) |
| 44-45-46 | 561 | `Art 46(5) the duty of the paragraph applies` | "Where, within 15 calendar days ..., objections are raised ..., or where the Commission considers ..." (a "where" gate on a duty: reading (b)) |
| 44-45-46 | 573 | `Art 46(6) the authorisation must be withdrawn by the market surveillance authority of the Member State concern` | "Where the Commission considers the authorisation unjustified" (a "where" gate on a duty: reading (b)) |
| 44-45-46 | 594 | `Art 46(7) the derogation of this Article applies to the high-risk AI system` | "only the derogations from the conformity assessment established in that Union harmonisation legislation shall apply" |
| 47-48-annex-v | 88 | `Art 47(1) the provider must keep the declaration at the disposal of the national competent authorities` | "for 10 years after the high-risk AI system has been placed on the market or put into service" (rule (a)); the last day is the day before the tenth anniversary (fork F-47 |
| 47-48-annex-v | 124 | `Art 47(1) a copy of the declaration must be submitted to the relevant national competent authorities` | "upon request" (a gate on a duty: fork F-47-1-request) |
| 47-48-annex-v | 195 | `Art 47(3) a single declaration must be drawn up in respect of all Union law applicable to the high-risk AI sys` | "Where high-risk AI systems are subject to other Union harmonisation legislation which also requires an EU declaration of conformity" (a "where" gate on a duty: reading ( |
| 47-48-annex-v | 214 | `Art 47(3) the declaration must contain all the information required to identify the Union harmonisation legisl` | the second sentence belongs to the single declaration of the first (a "where" gate: reading (b)) |
| 47-48-annex-v | 414 | `Annex V the declaration must contain the point` | "Where an AI system involves the processing of personal data" (a "where" gate: reading (b)) |
| 47-48-annex-v | 418 | `Annex V the declaration must contain the point` | "Where applicable" (a "where" gate: reading (b)) |
| 47-48-annex-v | 519 | `Art 48(2) the digital CE marking may be used` | "only if it can easily be accessed via the interface ... or via an easily accessible machine-readable code or other electronic means" |
| 47-48-annex-v | 566 | `Art 48(4) the CE marking must be followed by the identification number of the notified body` | "Where applicable" (a "where" gate on a duty: reading (b)) |
| 47-48-annex-v | 633 | `Art 48(5) the CE marking must indicate that the high-risk AI system also fulfils the requirements of the other` | "Where high-risk AI systems are subject to other Union law which also provides for the affixing of the CE marking" (a "where" gate on a duty: reading (b)) |
| 49-annex-viii-ix | 62 | `Art 49(1) the registration in the EU database is required` | "with the exception of high-risk AI systems referred to in point 2 of Annex III" |
| 49-annex-viii-ix | 106 | `Art 49(1) the registration was made before the placing on the market or the putting into service` | "Before placing on the market or putting into service" (the date has passed with no registration in time) |
| 49-annex-viii-ix | 143 | `Art 49(1) the authorised representative must register themselves and the system` | "where applicable, the authorised representative" (fork F-49-1-rep) |
| 49-annex-viii-ix | 188 | `Art 49(2) the registration was made before the placing on the market or the putting into service` | "Before placing on the market or putting into service" (the date has passed with no registration in time) |
| 49-annex-viii-ix | 211 | `Art 49(2) the authorised representative must register themselves and the AI system` | "where applicable, the authorised representative" (fork F-49-1-rep) |
| 49-annex-viii-ix | 240 | `Art 49(3) the deployer must register themselves, select the system and register its use in the EU database` | "with the exception of high-risk AI systems listed in point 2 of Annex III" |
| 49-annex-viii-ix | 266 | `Art 49(3) the registration was made before the putting into service or the use` | "Before putting into service or using" (the date has passed with no registration in time) |
| 49-annex-viii-ix | 306 | `Art 49(4)(a) the Section A point is within the restricted registration` | "shall include only the following information" |
| 49-annex-viii-ix | 315 | `Art 49(4)(b) as enacted the Section B point is within the restricted registration` | "shall include only the following information" |
| 49-annex-viii-ix | 326 | `Art 49(4)(b) as amended the Section B point is within the restricted registration` | "shall include only the following information" |
| 49-annex-viii-ix | 335 | `Art 49(4)(c) the Section C point is within the restricted registration` | "shall include only the following information" |
| 49-annex-viii-ix | 344 | `Art 49(4)(d) the Annex IX point is within the restricted registration` | "shall include only the following information" |
| 49-annex-viii-ix | 384 | `Art 49(4) the person has access to the restricted sections of the EU database` | "Only the Commission and national authorities referred to in Article 74(8) shall have access" |
| 49-annex-viii-ix | 450 | `Annex VIII Section A the information at the point must be provided and kept up to date` | "Where submission of information is carried out by another person on behalf of the provider" (reading (b)) |
| 49-annex-viii-ix | 452 | `Annex VIII Section A the information at the point must be provided and kept up to date` | "where applicable" (reading (b)) |
| 49-annex-viii-ix | 454 | `Annex VIII Section A the information at the point must be provided and kept up to date` | "where applicable" (reading (b)) |
| 49-annex-viii-ix | 456 | `Annex VIII Section A the information at the point must be provided and kept up to date` | "this information shall not be provided for high-risk AI systems in the areas of law enforcement or migration, asylum and border control management referred to in Annex I |
| 49-annex-viii-ix | 458 | `Annex VIII Section A the information at the point must be provided and kept up to date` | "A URL for additional information (optional)": not required |
| 49-annex-viii-ix | 500 | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date` | "Where submission of information is carried out by another person" (reading (b)) |
| 49-annex-viii-ix | 502 | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date` | "where applicable" (reading (b)) |
| 49-annex-viii-ix | 536 | `Annex VIII Section B as amended the information at the point must be provided and kept up to date` | "Where submission of information is carried out by another person" (reading (b)) |
| 49-annex-viii-ix | 538 | `Annex VIII Section B as amended the information at the point must be provided and kept up to date` | "where applicable" (reading (b)) |
| 49-annex-viii-ix | 614 | `Annex VIII Section C the information at the point must be provided and kept up to date` | "where applicable" (reading (b)) |

Reading (b), the `NOTHING` branches that rest on the text limiting a grant, a duty or a scope in its own wording, on silence, on a list left open, or on a point the text no longer has (94 branches; the 100 date-and-saving branches of every function are not listed, they are the keel's reading):

| module | line | function | why `NOTHING` |
| --- | --- | --- | --- |
| 40-41-42 | 46 | `Art 40(1) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2` | limited by its own wording: "shall be presumed ... to the extent that those standards cover those requirements" |
| 40-41-42 | 64 | `Art 40(1) the general-purpose AI model is presumed to be in conformity with the obligation set out in Chapter ` | limited by its own wording: "shall be presumed ... to the extent that those standards cover those requirements or obligations" |
| 40-41-42 | 172 | `Art 40(2) the Commission must request standardisation deliverables to facilitate joint compliance and presumpt` | silent: the fourth subparagraph is not in the text as enacted |
| 40-41-42 | 334 | `Art 41(3) the high-risk AI system is presumed to be in conformity with the requirement set out in Section 2` | limited by its own wording: "shall be presumed ... to the extent those common specifications cover those requirements" |
| 40-41-42 | 350 | `Art 41(3) the general-purpose AI model is presumed to comply with the obligation set out in Chapter V, Section` | limited by its own wording: "shall be presumed ... to the extent those common specifications cover those requirements or those obligations" |
| 40-41-42 | 431 | `Art 41(5) the provider has met the duty to duly justify the technical solutions` | limited by its own wording: the duty arises only where the provider does not comply; here it complies |
| 40-41-42 | 461 | `Art 41(6) the Commission must amend the implementing act establishing the common specification` | silent: the sentence follows the Member State's information; without it the text says nothing |
| 40-41-42 | 581 | `Art 42(1) the high-risk AI system is presumed to comply with the relevant requirements laid down in Article 10` | limited by its own wording: "that have been trained and tested on data reflecting the specific geographical, behavioural, contextual or functional setting" |
| 40-41-42 | 606 | `Art 42(2) the high-risk AI system is presumed to comply with the cybersecurity requirement set out in Article ` | limited by its own wording: "in so far as the cybersecurity certificate or statement of conformity or parts thereof cover those requirements" |
| 40-41-42 | 641 | `Art 42(3) the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15` | silent: paragraph 3 is not in the text as enacted |
| 43-annex-vi | 66 | `Art 43(1) the conformity assessment procedure the provider is to follow` | limited by its own wording: "For high-risk AI systems listed in point 1 of Annex III" (a scope limit with no "only": ruling of 2026-11-05, (c)) |
| 43-annex-vi | 75 | `Art 43(1) the conformity assessment procedure the provider is to follow` | silent: the provider has applied neither, and none of points (a) to (d) is stated to hold |
| 43-annex-vi | 96 | `Art 43(1) the body that carries out the conformity assessment procedure of Annex VII` | limited by its own wording: "For the purposes of the conformity assessment procedure referred to in Annex VII" |
| 43-annex-vi | 121 | `Art 43(2) the conformity assessment procedure the provider is to follow` | limited by its own wording: "high-risk AI systems referred to in points 2 to 8 of Annex III" |
| 43-annex-vi | 135 | `Art 43(3) first subparagraph as enacted the conformity assessment procedure the provider is to follow` | limited by its own wording: "For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 144 | `Art 43(3) first subparagraph as amended the conformity assessment procedure the provider is to follow` | limited by its own wording: "For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 174 | `Art 43(3) first subparagraph as enacted the requirements set out in Section 2 apply to the high-risk AI system` | limited by its own wording: "to those high-risk AI systems" (those covered by the Section A legislation) |
| 43-annex-vi | 183 | `Art 43(3) first subparagraph as amended the requirements set out in Section 2 apply to the high-risk AI system` | limited by its own wording: "to those high-risk AI systems" (those covered by the Section A legislation) |
| 43-annex-vi | 215 | `Art 43(3) first subparagraph as enacted the point of Annex VII applies` | limited by its own wording: "For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 218 | `Art 43(3) first subparagraph as enacted the point of Annex VII applies` | list not closed: the sentence names points 4.3, 4.4, 4.5 and the fifth paragraph of point 4.6; it does not say the others do not apply |
| 43-annex-vi | 227 | `Art 43(3) first subparagraph as amended the point of Annex VII applies` | limited by its own wording: "For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 231 | `Art 43(3) first subparagraph as amended the point of Annex VII applies` | list not closed: the sentence names points 3, 4.3, 4.4, 4.5, the fifth paragraph of point 4.6 and point 5; it does not say the others do not apply |
| 43-annex-vi | 262 | `Art 43(3) first subparagraph as amended the assessment of the quality management system set out in Article 17 ` | limited by its own wording: "For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 280 | `Art 43(3) first subparagraph the assessment of the quality management system set out in Article 17 is also und` | silent: the text as enacted does not name the assessment of the quality management system of Article 17 |
| 43-annex-vi | 293 | `Art 43(3) second subparagraph as enacted the notified body has the power to control the conformity of the high` | limited by its own wording: "notified bodies which have been notified under those legal acts" |
| 43-annex-vi | 296 | `Art 43(3) second subparagraph as enacted the notified body has the power to control the conformity of the high` | limited by its own wording: "provided that the compliance of those notified bodies with requirements laid down in Article 31(4), (5), (10) and (11) has been assessed" (a grant: fork F-43-3-power) |
| 43-annex-vi | 306 | `Art 43(3) second subparagraph as amended the notified body has the power to assess the conformity of the high-` | limited by its own wording: "notified bodies which have been notified under the Union harmonisation legislation listed in Section A of Annex I" |
| 43-annex-vi | 310 | `Art 43(3) second subparagraph as amended the notified body has the power to assess the conformity of the high-` | limited by its own wording: "provided that the compliance of those notified bodies ... has been assessed ..., which is evidenced through the assessment as part of the existing notification" (a grant:  |
| 43-annex-vi | 341 | `Art 43(3) the date by which the notified body must apply for designation` | limited by its own wording: "such notified bodies which have been notified under the Union harmonisation legislation in Section A of Annex I" |
| 43-annex-vi | 343 | `Art 43(3) the date by which the notified body must apply for designation` | silent: the text as enacted has no such sentence |
| 43-annex-vi | 357 | `Art 43(3) the notified body has met the duty to apply for designation by 28 January 2028` | limited by its own wording: no duty on these facts (the date asked, or the body, is outside the sentence) |
| 43-annex-vi | 364 | `Art 43(3) the notified body has met the duty to apply for designation by 28 January 2028` | limited by its own wording: the date "28 January 2028" has not yet passed, so the duty is not yet breached |
| 43-annex-vi | 382 | `Art 43(3) third subparagraph as enacted the product manufacturer may use the option not to have a third-party ` | limited by its own wording: "provided that that manufacturer has applied all harmonised standards covering all the relevant requirements" (a grant: fork F-43-3-opt) |
| 43-annex-vi | 397 | `Art 43(3) third subparagraph as amended the product manufacturer may use the option not to have a third-party ` | limited by its own wording: "provided that that manufacturer has applied harmonised standards to ensure compliance with all the relevant requirements" (a grant: fork F-43-3-opt) |
| 43-annex-vi | 433 | `Art 43(3) third subparagraph as amended the classification of the product as a high-risk AI system affects the` | limited by its own wording: the sentence speaks of "a product" classified "in accordance with Article 6(1)" |
| 43-annex-vi | 451 | `Art 43(3) third subparagraph the classification of the product as a high-risk AI system affects the choice of ` | silent: the sentence is not in the text as enacted |
| 43-annex-vi | 465 | `Art 43(3) third subparagraph as amended the manufacturer is required to choose a third-party conformity assess` | limited by its own wording: "if this is not required by the Union harmonisation legislation": where the legislation requires it, the sentence does not speak |
| 43-annex-vi | 484 | `Art 43(3) third subparagraph the manufacturer is required to choose a third-party conformity assessment proced` | silent: the sentence is not in the text as enacted |
| 43-annex-vi | 498 | `Art 43(3) as amended fourth subparagraph the conformity assessment procedure the provider is to follow` | limited by its own wording: "Where a high-risk AI system is both covered by the Union harmonisation legislation listed in Section A of Annex I and it falls within one of the categories listed in Annex |
| 43-annex-vi | 517 | `Art 43(3) fourth subparagraph the conformity assessment procedure the provider is to follow` | silent: the fourth subparagraph is not in the text as enacted |
| 43-annex-vi | 541 | `Art 43(4) the high-risk AI system must undergo a new conformity assessment procedure` | limited by its own wording: "High-risk AI systems that have already been subject to a conformity assessment procedure" (a scope limit with no "only") |
| 43-annex-vi | 558 | `Art 43(4) the changes do not constitute a substantial modification` | limited by its own wording: the exclusion reaches only changes of a learning system that were pre-determined and documented; for any other change Art 3(23) decides |
| 44-45-46 | 37 | `Art 44(1) the certificate must be drawn up in a language which can be easily understood by the relevant author` | limited by its own wording: "Certificates issued by notified bodies in accordance with Annex VII" (a scope limit with no "only") |
| 44-45-46 | 56 | `Art 44(2) the longest period in years that a certificate may indicate` | limited by its own wording: the sentence names AI systems covered by Annex I and by Annex III only |
| 44-45-46 | 70 | `Art 44(2) the period the certificate indicates is within the limit` | limited by its own wording: no limit on these facts |
| 44-45-46 | 87 | `Art 44(2) the validity of a certificate may be extended for a further period` | limited by its own wording: "At the request of the provider" (a gate on a "may" that is not "where", "when" or "upon": the ruling of 2026-11-12 in BRIEF.md; fork F-44-2-extension) |
| 44-45-46 | 90 | `Art 44(2) the validity of a certificate may be extended for a further period` | limited by its own wording: "based on a re-assessment" (a grant: fork F-44-2-extension) |
| 44-45-46 | 136 | `Art 44(3) the notified body must give reasons for its decision` | limited by its own wording: "its decision" (there is no decision to give reasons for) |
| 44-45-46 | 231 | `Art 45(1) the notified body must inform the notifying authority of the item` | limited by its own wording: "any ... issued" / "any refusal" / "any circumstances" / "any request": nothing of that kind has occurred |
| 44-45-46 | 265 | `Art 45(2) the notified body must inform the other notified bodies of the item` | limited by its own wording: "which it has refused, suspended or withdrawn": nothing of that kind has occurred |
| 44-45-46 | 284 | `Art 45(3) the notified body must provide the other notified body with relevant information on the kind of resu` | limited by its own wording: "the other notified bodies carrying out similar conformity assessment activities covering the same types of AI systems" (a scope limit with no "only") |
| 44-45-46 | 388 | `Art 46(1) the market surveillance authority may authorise the placing on the market or the putting into servic` | limited by its own wording: "for exceptional reasons of ..." (a limit on the grant: fork F-46-1) |
| 44-45-46 | 433 | `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into servic` | limited by its own wording: "law-enforcement authorities or civil protection authorities may" (a scope limit with no "only") |
| 44-45-46 | 435 | `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into servic` | limited by its own wording: "In a duly justified situation of urgency ... or in the case of specific, substantial and imminent threat" (a gate on a "may" that is not "where", "when" or "upon": the rul |
| 44-45-46 | 438 | `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into servic` | limited by its own wording: "provided that such authorisation is requested during or after the use without undue delay" (a grant: fork F-46-2) |
| 44-45-46 | 505 | `Art 46(3) the market surveillance authority must inform the Commission and the other Member States of the auth` | limited by its own wording: "any authorisation issued" (nothing issued: the sentence does not speak) |
| 44-45-46 | 519 | `Art 46(3) the obligation to inform covers the information` | silent: the sentence names only sensitive operational data |
| 44-45-46 | 540 | `Art 46(4) the authorisation is deemed justified` | limited by its own wording: the 15 calendar days have not yet passed, so the authorisation is not yet deemed justified or unjustified |
| 44-45-46 | 595 | `Art 46(7) the derogation of this Article applies to the high-risk AI system` | silent: the paragraph speaks only of systems related to Section A products |
| 47-48-annex-v | 67 | `Art 47(1) the declaration is in a form the paragraph names` | list not closed: the sentence names three forms and does not say that no other form will do (fork F-47-1-form) |
| 47-48-annex-v | 237 | `Art 47(4) the provider assumes responsibility for compliance with the requirements set out in Section 2` | limited by its own wording: "By drawing up the EU declaration of conformity" (no declaration drawn up: the sentence does not speak) |
| 47-48-annex-v | 257 | `Art 47(4) the provider must keep the declaration up-to-date` | limited by its own wording: "as appropriate" |
| 47-48-annex-v | 496 | `Art 48(2) a digital CE marking must be used` | limited by its own wording: "For high-risk AI systems provided digitally" (a scope limit with no "only") |
| 47-48-annex-v | 516 | `Art 48(2) the digital CE marking may be used` | limited by its own wording: "For high-risk AI systems provided digitally" (a scope limit with no "only") |
| 47-48-annex-v | 591 | `Art 48(4) the person may affix the identification number of the notified body` | limited by its own wording: "under its instructions" (a limit on a grant: fork F-48-4-affix) |
| 47-48-annex-v | 611 | `Art 48(4) the identification number must also be indicated in the promotional material` | limited by its own wording: there is no identification number to indicate ("Where applicable") |
| 47-48-annex-v | 614 | `Art 48(4) the identification number must also be indicated in the promotional material` | limited by its own wording: "any promotional material which mentions that the high-risk AI system fulfils the requirements for CE marking" (a scope limit with no "only") |
| 49-annex-viii-ix | 60 | `Art 49(1) the registration in the EU database is required` | limited by its own wording: "a high-risk AI system listed in Annex III" (a scope limit with no "only") |
| 49-annex-viii-ix | 83 | `Art 49(1) who must register themselves and their system` | limited by its own wording: the registration is not required on these facts (the Boolean function above says whether JUST FALSE or NOTHING) |
| 49-annex-viii-ix | 107 | `Art 49(1) the registration was made before the placing on the market or the putting into service` | limited by its own wording: the date of placing on the market has not yet passed, so the duty is not yet breached |
| 49-annex-viii-ix | 108 | `Art 49(1) the registration was made before the placing on the market or the putting into service` | limited by its own wording: no registration is required on these facts |
| 49-annex-viii-ix | 158 | `Art 49(2) the registration in the EU database is required` | limited by its own wording: "an AI system for which the provider has concluded that it is not high-risk according to Article 6(3)" (a scope limit with no "only") |
| 49-annex-viii-ix | 172 | `Art 49(2) who must register themselves and the AI system` | limited by its own wording: the registration is not required on these facts |
| 49-annex-viii-ix | 189 | `Art 49(2) the registration was made before the placing on the market or the putting into service` | limited by its own wording: the date has not yet passed, so the duty is not yet breached |
| 49-annex-viii-ix | 190 | `Art 49(2) the registration was made before the placing on the market or the putting into service` | limited by its own wording: no registration is required on these facts |
| 49-annex-viii-ix | 236 | `Art 49(3) the deployer must register themselves, select the system and register its use in the EU database` | limited by its own wording: "deployers that are public authorities, Union institutions, bodies, offices or agencies or persons acting on their behalf" (a scope limit with no "only") |
| 49-annex-viii-ix | 238 | `Art 49(3) the deployer must register themselves, select the system and register its use in the EU database` | limited by its own wording: "a high-risk AI system listed in Annex III" (a scope limit with no "only") |
| 49-annex-viii-ix | 267 | `Art 49(3) the registration was made before the putting into service or the use` | limited by its own wording: the date has not yet passed, so the duty is not yet breached |
| 49-annex-viii-ix | 268 | `Art 49(3) the registration was made before the putting into service or the use` | limited by its own wording: no registration is required of this deployer on these facts |
| 49-annex-viii-ix | 294 | `Art 49(4) the registration must be in a secure non-public section of the EU database` | limited by its own wording: "For high-risk AI systems referred to in points 1, 6 and 7 of Annex III, in the areas of ..." (a scope limit with no "only") |
| 49-annex-viii-ix | 307 | `Art 49(4)(a) the Section A point is within the restricted registration` | limited by its own wording: Section A of Annex VIII has no such point |
| 49-annex-viii-ix | 316 | `Art 49(4)(b) as enacted the Section B point is within the restricted registration` | limited by its own wording: Section B of Annex VIII as enacted has no such point |
| 49-annex-viii-ix | 324 | `Art 49(4)(b) as amended the Section B point is within the restricted registration` | repealed or blank in this text: points 7 and 9 of Section B are deleted by the Omnibus (consolidated lines 1865 and 1869); the paragraph still names point 9 |
| 49-annex-viii-ix | 327 | `Art 49(4)(b) as amended the Section B point is within the restricted registration` | limited by its own wording: Section B of Annex VIII as amended has no such point |
| 49-annex-viii-ix | 336 | `Art 49(4)(c) the Section C point is within the restricted registration` | limited by its own wording: Section C of Annex VIII has no such point |
| 49-annex-viii-ix | 345 | `Art 49(4)(d) the Annex IX point is within the restricted registration` | limited by its own wording: Annex IX has no such point |
| 49-annex-viii-ix | 363 | `Art 49(4) the information item is included in the restricted registration` | limited by its own wording: the paragraph speaks of systems referred to in points 1, 6 and 7 of Annex III in those areas (a scope limit with no "only") |
| 49-annex-viii-ix | 406 | `Art 49(5) the high-risk AI system must be registered at national level` | limited by its own wording: "High-risk AI systems referred to in point 2 of Annex III" (a scope limit with no "only") |
| 49-annex-viii-ix | 448 | `Annex VIII Section A the information at the point must be provided and kept up to date` | limited by its own wording: Section A has no such point |
| 49-annex-viii-ix | 498 | `Annex VIII Section B as enacted the information at the point must be provided and kept up to date` | limited by its own wording: Section B as enacted has no such point |
| 49-annex-viii-ix | 532 | `Annex VIII Section B as amended the information at the point must be provided and kept up to date` | repealed or blank in this text: points 7 and 9 of Section B are deleted by the Omnibus (consolidated lines 1865 and 1869) |
| 49-annex-viii-ix | 534 | `Annex VIII Section B as amended the information at the point must be provided and kept up to date` | limited by its own wording: Section B as amended has no such point |
| 49-annex-viii-ix | 612 | `Annex VIII Section C the information at the point must be provided and kept up to date` | limited by its own wording: Section C has no such point |
| 49-annex-viii-ix | 636 | `Annex IX the information at the point must be provided and kept up to date` | limited by its own wording: Annex IX has no such point |

### Reading a result: FALSE and NOTHING (P5)

In this part `JUST TRUE` and `JUST FALSE` are answers the text gives in its own words, and `NOTHING` is "the text does not say".
`JUST FALSE` is returned where the text states a flat negative ("shall not exceed", "shall not be provided", "only the Commission ... shall have access"), where it closes a gate itself ("only if", "unless"), where a period is fixed in its own words and the case lies outside it ("for 10 years after"), and where a "where", "when" or "upon" gate on a duty, a "may" or a deeming rule fails (the periods ruling of 2026-11-05, rule (b), with the delegated-definitions ruling, item (c): split sites (ii) and (iv), listed under Split sites), where an "on request" gate on a duty fails (read like "upon": M-8), where "provided that" gates the validity of a supplement (M-8), and where Article 2(2) cuts a provision off from a high-risk AI system under Article 6(1) with Section B products (a list closed by "only": seam S14, M-7).
`NOTHING` is returned in seven cases:
before the group applies (Art 113's general date, 2 August 2026, has not come);
when Art 111(2) saves the system (the keel's reading, fork F-111-2-nothing, which I did not change);
where the text limits a grant or a power in its own wording and the case falls outside the limit, with no "only" closing the gate (a "provided that" on a grant, a scope limit such as "notified bodies which have been notified under those legal acts", a list of reasons not closed with "only");
where the text is silent (for example Annex VIII Section B point 9 as amended, which the text no longer has);
where the question names a point that the Annex does not have;
where the gate on a "may" is "at the request of" or "in a duly justified situation" (not "where", "when" or "upon": the grant rule, M-8);
where a function that answers with a value and not a yes or no (a procedure, a body, a place, who registers) is cut off by Article 2(2): there is no `JUST FALSE` for a value (S14).
In the seat layer a reader takes `JUST TRUE` as "yes", `JUST FALSE` as "no, the text says so", and `NOTHING` as "this Regulation, read in this part, does not answer on those facts".
A seat question never negates a layer-1 answer: where the layer-1 function is a duty the question asks "must I", where it is a permission it asks "may I", where it is a status it asks "is" or "does".
Every no-branch of layer 1 carries a `-- FALSE-kind (the text says no in its own words): "..."` comment and every not-covered branch a `-- NOTHING-kind (<why>)` comment (counts under Marginal readings); the Article 2(2) branch of a function carries `-- S14-kind`.
A dispatcher branch carries `-- VERSION as enacted` or `-- VERSION as amended`.

## Seams (P5)

Taken (inputs, because another part answers):

| seam | what I take | input name (type) | where it is used |
| --- | --- | --- | --- |
| S1 | whether and how the AI system is high-risk | layer 1: `the route to high-risk` (`Route to high-risk`); seat layer: `the route by which the AI system is high-risk` (the plan's name, with its `@desc`) | every function that passes the system's facts to the keel's applicability function (59 functions, 34 rules) |
| S9 | whether a standard is a harmonised standard | the borrowed fact `the standard is a harmonised standard as defined in Article 2(1), point (c), of Regulation (EU) No 1025/2012` (BOOLEAN), passed to the keel's `Art 3(27) the standard is a harmonised standard` | `Art 40(1)`, both limbs (the high-risk AI system and the general-purpose AI model) |
| S13 | the three time and history facts | `the date asked` (DATE), `the date the AI system was placed on the market or put into service` (DATE), `the AI system has been significantly changed in its design since the date of application of Chapter III` (BOOLEAN), with the plan's `@desc` | every provision addressed to an operator of one system (the date asked alone for the others) |
| S14 | whether Article 2(2) cuts a provision off from a high-risk AI system under Article 6(1) with Section B products | the keel's `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products`, called through my helper `Art 40 to 49 Art 2(2) cuts the provision off from the high-risk AI system` (in `P5-section-5.l4`) with the date asked, the route (S1) and two plain BOOLEAN inputs, `the products are covered by Union harmonisation legislation listed in Section B of Annex I` and `the requirements for high-risk AI systems under this Regulation have been integrated in that Union harmonisation legislation`; the `Article reference` is built from the Article number, the letter "" and the paragraph (0 where the Annex's Article is meant) | the 93 functions and rules that take the system's facts (59 `MAYBE` functions, 34 regulative rules; fork F-S14-reach, marginal reading M-7): 60 have a `-- S14-kind` branch (50 answer `JUST FALSE`, 6 `NOTHING`, 4 `FULFILLED`) and the other 33 reach it through the function they call; the two Section B inputs sit after the first four system facts in every one of them and in its seat question |

Provided (S6, asked by Article 16 and Article 71, from Articles 43, 47, 48, 49):

- Article 43: `Art 43(1) the conformity assessment procedure the provider is to follow`, `Art 43(2) ...`, `Art 43(3) first subparagraph ...` (the procedure to follow, as a `MAYBE` of the type `Art 43 procedure`), and Annex VI's `has carried out` functions.
- Article 47: `Art 47(1) the provider must draw up an EU declaration of conformity for the high-risk AI system` (a duty).
- Article 48: the CE marking duties (`Art 48(2)` to `Art 48(5)`) and `Art 48(3) where the CE marking must be affixed`.
- Article 49: `Art 49(1) the registration was made before the placing on the market or the putting into service`, and its Art 49(2) and Art 49(3) twins.
- The plan's S6 inputs (`the conformity assessment procedure of Article 43 has been completed`, `the EU declaration of conformity of Article 47 has been drawn up`, `the CE marking of Article 48 has been affixed`, `the AI system has been registered under Article 49`) are facts about what the provider has done; no function of this part returns them, because Articles 43, 47 and 48 state what the provider must do, not when it counts as done.
  The receiving part keeps them as inputs; the lead wires them to the duties above, and the registration in time is the one that has a function (`Art 49(1) ... was made before ...`, with `the registration has been made` and `the date on which the registration was made` as its own inputs).

Seams the plan lacks (borrowed facts, each a plain BOOLEAN, NUMBER, DATE or STRING input of this part; the answering provision is named, not the part):

- Annex III: `the high-risk AI system is listed in Annex III`, `the high-risk AI system falls within one of the categories listed in Annex III`, `the point of Annex III under which the high-risk AI system is listed` (NUMBER); used by Art 43(1) and (2), Art 49(1), (3), (4), (5).
- Annex I Section A: `the high-risk AI system is covered by the Union harmonisation legislation listed in Section A of Annex I`, `the high-risk AI system is related to a product covered by ...`, `the AI system is covered by Annex I` and `... by Annex III`; used by Art 43(3), Art 44(2), Art 46(7).
- Article 6: `the product is classified as a high-risk AI system in accordance with Article 6(1)` (Art 43(3) third subparagraph), `the provider has concluded that the AI system is not high-risk according to Article 6(3)` (Art 49(2)).
- Annex VII and Section 4 (notified bodies): `the point of Annex VII` (STRING), `the conformity assessment procedure of Annex VII is carried out`, `the certificate is issued by a notified body in accordance with Annex VII`, `the compliance of the notified body with the requirements laid down in Article 31(4), (5), (10) and (11) has been assessed in the context of the notification procedure`, `the notified body has applied for designation in accordance with Section 4 of this Chapter`.
- Section 2 and Articles 10(4), 15, 17, 72: `the high-risk AI system has been trained and tested ...`, `the cybersecurity certificate or statement of conformity ... cover the cybersecurity requirement set out in Article 15`, `the provider has verified that the established quality management system is in compliance with the requirements of Article 17`, `the provider has verified that the design and development process ... post-market monitoring as referred to in Article 72 ...`.
- Other instruments and provisions: `the conditions laid down in Article 12(1) of Regulation (EU) 2024/2847 are fulfilled`, `the person is a national authority referred to in Article 74(8)`, and the bearer of Annex IX, which Art 60(4)(c) (another part) points at (F-IX-bearer).

The keel's functions I call (found by grep over the layer-1 modules): `Omnibus Art 4 the version in force`, `Art 113 the provision group applies` and `Art 3(27) the standard is a harmonised standard`, with the core's `Role` type and constants for the group and the route; I call no other `Art 3(N)` function: the role of a party is fixed by the seat and by the rule's `PARTY`, not asked again.

## Split sites (P5)

(i) **An unmet element of an infringement: 0 sites.** Articles 40 to 49 and the four Annexes name no infringement and no prohibited practice; their breach paths are the missed deadlines of Art 43(3) and Art 49(1) to (3), which are not elements of an infringement.

(ii) **A "may" gated by "where", "when", "upon", "on application" and the like: 5 sites; 3 answered `JUST FALSE` (a "where" or "upon" gate: the periods ruling, rule (b), and the delegated-definitions ruling, item (c)) and 2 answered `NOTHING` (a gate in other words: the grant rule); the other reading of the 3 is `NOTHING` (the grant ruling).**

- Art 41(1) first subparagraph, "where the following conditions have been fulfilled": `JUST FALSE`; `Art 41(1) the Commission may adopt implementing acts establishing common specifications`; fork F-41-1.
- Art 43(3) third subparagraph, "Where a legal act listed in Section A of Annex I enables the product manufacturer to opt out" (as enacted), "Where Union harmonisation legislation ... provides the product manufacturer with an option" (as amended): `JUST FALSE`; the two `Art 43(3) third subparagraph ... the product manufacturer may use the option` functions and their dispatcher; fork F-43-3-opt.
- Art 46(1), "upon a duly justified request": `JUST FALSE`; `Art 46(1) the market surveillance authority may authorise ...`; fork F-46-1.
- Art 44(2) second sentence, "At the request of the provider": `NOTHING`; `Art 44(2) the validity of a certificate may be extended for a further period`; fork F-44-2-extension (M-8).
- Art 46(2), "In a duly justified situation of urgency": `NOTHING`; `Art 46(2) the law-enforcement or civil protection authority may put a specific high-risk AI system into service ...`; fork F-46-2 (M-8).

The brief calls the first group ("where", "when" or "upon" on a "may") a question for a lawyer and leaves its answer as the Guide's rulings give it: 3 sites and 5 functions (the Art 41(1) function; the as-enacted and as-amended Art 43(3) third subparagraph functions with their dispatcher; the Art 46(1) function).
Where the same "may" also carries a "provided that" gate or a limit in its own wording, the function answers `NOTHING` there, by the grant ruling of 2026-11-12 (8 gates in 6 forks: F-43-3-power, F-43-3-opt, F-44-2-extension (two), F-46-1, F-46-2 (two), F-48-4-affix); the group of "entitled"-named functions has one member, `Art 43(3) second subparagraph as enacted ...` (the as-enacted "shall be entitled to control"), which I named for a power and which answers `NOTHING` where the gate fails (F-43-3-power).
A "may" whose gate is closed by the text ("only if": `Art 43(3) third subparagraph ... may use that option only if it has also applied ...`, `Art 48(2) the digital CE marking may be used`) answers `JUST FALSE`, which the brief keeps.
A duty whose "upon request" or "on request" gate fails answers `JUST FALSE` (Art 45(1)(e), 45(2)(a), 45(2)(b), 45(3), 47(1): F-45-1-e, F-47-1-request); an "unless" once met and a bare "must" not done are decided case by case (F-44-3-unless, F-41-5).

(iii) **A system saved by Art 111(2), or a group not yet applicable: `NOTHING` (the keel's reading, F-111-2-nothing in the keel's fork register; I did not decide it again).** 59 functions of this part answer `MAYBE` and take the placement date, so they can answer `NOTHING` because Art 111(2) saves the system; 34 regulative rules pass the same facts and read that `NOTHING` as nothing owed (`FULFILLED`); the 74 other `MAYBE` functions pass the date only and answer `NOTHING` only before 2 August 2026.
For a system under Article 6(1) with Section B products Article 2(2) is asked before Art 111(2) (seam S14): where it cuts the provision off the function answers `JUST FALSE`, `NOTHING` or `FULFILLED` whether or not Art 111(2) would have saved the system.

(iv) **A deeming rule, a presumption or a validity rule gated by "where", "when" or "upon" that is neither a duty nor a "may": 2 sites, both answered `JUST FALSE` where the gate fails (the periods ruling, rule (b)); the other reading is `NOTHING`.**

- Art 42(3) as amended, "Where high-risk AI systems fall within the scope of Regulation (EU) 2024/2847 and the conditions laid down in Article 12(1) of that Regulation are fulfilled ... shall be deemed to comply": `JUST FALSE` where either fact fails; `Art 42(3) as amended ...` and its dispatcher `Art 42(3) the high-risk AI system is deemed to comply with the cybersecurity requirement set out in Article 15`; fork F-42-3-where.
- Art 46(4), "Where, within 15 calendar days of receipt ..., no objection has been raised ... shall be deemed justified": `JUST FALSE` where an objection was raised; `NOTHING` while the 15 days are still running with no objection, which is the "where" neither failed nor met; `Art 46(4) the authorisation is deemed justified`; fork F-46-4.
The presumptions of Art 40(1), 41(3), 42(1) and 42(2) are not of this shape: each is limited by a relative clause, "to the extent that" or "in so far as", not by "where", "when" or "upon", and answers `NOTHING` outside its limit (the periods ruling, item (c); fork F-40-42-limits).
The supplement of Art 44(2) ("provided that", `JUST FALSE`, F-44-2-supplement) is a status gated by "provided that", not by "where", and the second subparagraph of Art 43(4) is a flat negative with no gate; neither is of this shape.

## Rules with no breach path (P5)

A regulative rule that is a `MUST` with no time limit and no stated consequence cannot be shown breached: a late action still reads `FULFILLED`.
I did not invent a deadline or a consequence the text does not state.
53 of the 65 regulative rules of this part are such `MUST` rules; 8 are `MAY` rules (a permission cannot be breached); 4 have a time limit and a trace that reaches `BREACH`.

The rules with a breach path, and their traces (each on both builds, outcome read against its `-- EXPECT` comment):

- `Art 43(3) the duty of the notified body to apply for designation` (`P5-art-43-annex-vi.l4` line 690): the limit is the computed `WITHIN (Day <last day>) MINUS (Day <date asked>)`; a trace whose act comes after the last day, or that waits past it, reads `BREACH`, and one on or before it reads `FULFILLED`; asked on a date after the last day, every trace reads `BREACH` (a trace cannot know an earlier act), and the function that says whether the act was done in time (`... has met the duty ...`, `... was made before ...`) answers that case.
- `Art 49(1) the duty to register before placing on the market or putting into service` (`P5-art-49-annex-viii-ix.l4` line 659): the limit is the computed `WITHIN (Day <last day>) MINUS (Day <date asked>)`; a trace whose act comes after the last day, or that waits past it, reads `BREACH`, and one on or before it reads `FULFILLED`; asked on a date after the last day, every trace reads `BREACH` (a trace cannot know an earlier act), and the function that says whether the act was done in time (`... has met the duty ...`, `... was made before ...`) answers that case.
- `Art 49(2) the duty to register before placing on the market or putting into service` (`P5-art-49-annex-viii-ix.l4` line 681): the limit is the computed `WITHIN (Day <last day>) MINUS (Day <date asked>)`; a trace whose act comes after the last day, or that waits past it, reads `BREACH`, and one on or before it reads `FULFILLED`; asked on a date after the last day, every trace reads `BREACH` (a trace cannot know an earlier act), and the function that says whether the act was done in time (`... has met the duty ...`, `... was made before ...`) answers that case.
- `Art 49(3) the deployer's duty to register before putting into service or using` (`P5-art-49-annex-viii-ix.l4` line 709): the limit is the computed `WITHIN (Day <last day>) MINUS (Day <date asked>)`; a trace whose act comes after the last day, or that waits past it, reads `BREACH`, and one on or before it reads `FULFILLED`; asked on a date after the last day, every trace reads `BREACH` (a trace cannot know an earlier act), and the function that says whether the act was done in time (`... has met the duty ...`, `... was made before ...`) answers that case.

The `MUST` rules with no breach path (provision, rule):

- `Art 40(2) the Commission's duty to issue standardisation requests` (`P5-art-40-41-42` line 191).
- `Art 40(2) the Commission's duty to ask for deliverables on reporting and documentation processes` (`P5-art-40-41-42` line 199).
- `Art 40(2) the Commission's duty to consult the Board and relevant stakeholders` (`P5-art-40-41-42` line 207).
- `Art 40(2) the Commission's duty to specify that standards have to be clear and consistent` (`P5-art-40-41-42` line 215).
- `Art 40(2) the Commission's duty to request evidence of best efforts` (`P5-art-40-41-42` line 223).
- `Art 40(2) the Commission's duty to request standardisation deliverables` (`P5-art-40-41-42` line 231).
- `Art 40(3) the duty of the participants in the standardisation process` (`P5-art-40-41-42` line 242).
- `Art 41(1) the Commission's duty to consult the advisory forum` (`P5-art-40-41-42` line 493).
- `Art 41(2) the Commission's duty to inform the committee` (`P5-art-40-41-42` line 501).
- `Art 41(4) the Commission's duty to assess the harmonised standard` (`P5-art-40-41-42` line 509).
- `Art 41(4) the Commission's duty to repeal the implementing act` (`P5-art-40-41-42` line 517).
- `Art 41(6) the Member State's duty to inform the Commission` (`P5-art-40-41-42` line 525).
- `Art 41(6) the Commission's duty to amend the implementing act` (`P5-art-40-41-42` line 533).
- `Art 41(5) the provider's duty to duly justify the technical solutions adopted` (`P5-art-40-41-42` line 551).
- `Art 43(1) the provider's duty to opt for a conformity assessment procedure or to follow the procedure of Annex VII` (`P5-art-43-annex-vi` line 601).
- `Art 43(1) the market surveillance authority's duty to act as a notified body` (`P5-art-43-annex-vi` line 637).
- `Art 43(2) the provider's duty to follow the procedure based on internal control` (`P5-art-43-annex-vi` line 652).
- `Art 43(3) the provider's duty to follow the relevant conformity assessment procedure` (`P5-art-43-annex-vi` line 667).
- `Art 43(4) the provider's duty to have the high-risk AI system undergo a new conformity assessment procedure` (`P5-art-43-annex-vi` line 729).
- `Annex VI point 2 the provider's duty to verify the quality management system` (`P5-art-43-annex-vi` line 822).
- `Annex VI point 3 the provider's duty to examine the technical documentation` (`P5-art-43-annex-vi` line 837).
- `Annex VI point 4 the provider's duty to verify the design and development process and the post-market monitoring` (`P5-art-43-annex-vi` line 852).
- `Art 44(1) the notified body's duty to draw up the certificate in a language which can be easily understood` (`P5-art-44-45-46` line 155).
- `Art 44(3) the notified body's duty to suspend or withdraw the certificate or impose restrictions` (`P5-art-44-45-46` line 175).
- `Art 44(3) the notified body's duty to give reasons for its decision` (`P5-art-44-45-46` line 184).
- `Art 45(1) the notified body's duty to inform the notifying authority` (`P5-art-44-45-46` line 310).
- `Art 45(2) the notified body's duty to inform the other notified bodies` (`P5-art-44-45-46` line 321).
- `Art 45(3) the notified body's duty to provide the other notified bodies with relevant information` (`P5-art-44-45-46` line 332).
- `Art 45(4) the notified body's duty to safeguard confidentiality` (`P5-art-44-45-46` line 340).
- `Art 46(2) the deployer's duty to stop the use with immediate effect` (`P5-art-44-45-46` line 635).
- `Art 46(2) the deployer's duty to discard all the results and outputs immediately` (`P5-art-44-45-46` line 649).
- `Art 46(3) the market surveillance authority's duty to inform the Commission and the other Member States` (`P5-art-44-45-46` line 658).
- `Art 46(5) the Commission's duties after an objection` (`P5-art-44-45-46` line 669).
- `Art 46(6) the market surveillance authority's duty to withdraw the authorisation` (`P5-art-44-45-46` line 683).
- `Art 47(1) the provider's duty to draw up an EU declaration of conformity` (`P5-art-47-48-annex-v` line 272).
- `Art 47(1) the provider's duty to keep the declaration at the disposal of the national competent authorities` (`P5-art-47-48-annex-v` line 285).
- `Art 47(1) the provider's duty to submit a copy upon request` (`P5-art-47-48-annex-v` line 299).
- `Art 47(2) the provider's duty to state in the declaration that the system meets the requirements of Section 2` (`P5-art-47-48-annex-v` line 312).
- `Art 47(2) the provider's duty to include the information set out in Annex V` (`P5-art-47-48-annex-v` line 325).
- `Art 47(2) the provider's duty to translate the declaration` (`P5-art-47-48-annex-v` line 338).
- `Art 47(3) the provider's duty to draw up a single declaration` (`P5-art-47-48-annex-v` line 352).
- `Art 47(4) the provider's duty to keep the declaration up-to-date` (`P5-art-47-48-annex-v` line 366).
- `Annex V the provider's duty to include the point in the declaration` (`P5-art-47-48-annex-v` line 432).
- `Art 48(2) the provider's duty to use a digital CE marking` (`P5-art-47-48-annex-v` line 649).
- `Art 48(3) the provider's duty to affix the CE marking` (`P5-art-47-48-annex-v` line 667).
- `Art 48(4) the provider's duty to follow the CE marking with the identification number` (`P5-art-47-48-annex-v` line 683).
- `Art 48(4) the provider's duty to indicate the identification number in the promotional material` (`P5-art-47-48-annex-v` line 717).
- `Art 48(5) the provider's duty to indicate in the CE marking that the system also fulfils the requirements of the other Union law` (`P5-art-47-48-annex-v` line 731).
- `Art 49(4) the provider's duty to register in the secure non-public section` (`P5-art-49-annex-viii-ix` line 726).
- `Annex VIII Section A the provider's duty to provide the information at the point and keep it up to date` (`P5-art-49-annex-viii-ix` line 746).
- `Annex VIII Section B the provider's duty to provide the information at the point and keep it up to date` (`P5-art-49-annex-viii-ix` line 762).
- `Annex VIII Section C the deployer's duty to provide the information at the point and keep it up to date` (`P5-art-49-annex-viii-ix` line 777).
- `Annex IX the provider's duty to provide the information at the point and keep it up to date` (`P5-art-49-annex-viii-ix` line 786).

The `MAY` rules (no breach path possible):

- `Art 41(1) the Commission's permission to adopt implementing acts establishing common specifications` (`P5-art-40-41-42` line 485).
- `Art 43(1) the provider's permission to choose any of the notified bodies` (`P5-art-43-annex-vi` line 621).
- `Art 43(3) the notified body's permission to assess the conformity of the high-risk AI system` (`P5-art-43-annex-vi` line 679).
- `Art 43(3) the product manufacturer's permission to use the option not to have a third-party conformity assessment` (`P5-art-43-annex-vi` line 714).
- `Art 44(2) the notified body's permission to extend the validity of a certificate` (`P5-art-44-45-46` line 165).
- `Art 46(1) the market surveillance authority's permission to authorise` (`P5-art-44-45-46` line 605).
- `Art 46(2) the authority's permission to put the system into service without the authorisation` (`P5-art-44-45-46` line 621).
- `Art 48(4) the permission to affix the identification number of the notified body` (`P5-art-47-48-annex-v` line 698).

## Versions (P5)

One row per `▼M1` passage of this part (the brief's table: consolidated lines 645-647, 671, 686-689, 1866, 1870).
Wherever the Omnibus changes a date, a duty, an addressee or a permission I encoded both texts, each in its own function with no gate, and a dispatcher on `Omnibus Art 4 the version in force`.

| consolidated lines | provision | what the Omnibus changed | encoded | why |
| --- | --- | --- | --- | --- |
| 645-647 | Art 40(2) fourth subparagraph | inserted: the Commission shall request standardisation deliverables to facilitate joint compliance and the presumption of conformity | amended text only, with a dispatcher that answers `NOTHING` as enacted | there is no as-enacted text to encode; the dispatcher says so (`Art 40(2) fourth subparagraph, both versions`) |
| 671 | Art 42(3) | inserted: high-risk AI systems within Regulation (EU) 2024/2847 whose Article 12(1) conditions are fulfilled shall be deemed to comply with Article 15 | amended text only, with a dispatcher that answers `NOTHING` as enacted | as above (`Art 42(3), both versions`) |
| 686-689 | Art 43(3) first subparagraph | replaced: adds the assessment of the quality management system of Article 17 and points 3 and 5 of Annex VII to the points that apply (as enacted 4.3, 4.4, 4.5 and the fifth paragraph of 4.6) | both | the set of Annex VII points that apply changed (base line 1214) |
| 686-689 | Art 43(3) second subparagraph | replaced: "entitled to control" becomes "have the power to assess", with a further fact (evidenced through the existing notification) and a new last sentence (apply for designation by 28 January 2028) | both | a power, a fact and a date changed (base line 1215) |
| 686-689 | Art 43(3) third subparagraph | replaced: the manufacturer's option turns on "harmonised standards to ensure compliance with all the relevant requirements" (as enacted "all harmonised standards covering all the relevant requirements"), and two sentences are added on the classification under Article 6(1) and on third-party assessment | both | a permission and its gate changed (base line 1216) |
| 686-689 | Art 43(3) fourth subparagraph | new: a system both in Section A of Annex I and in Annex III follows the Section A legislation's procedure | amended text only, dispatcher `NOTHING` as enacted | no as-enacted text to encode |
| 1865-1867 | Annex VIII Section B point 7 | deleted (the short summary of the grounds for considering the system not high-risk) | both | the as-enacted function lists it, the amended one answers `NOTHING` for it; Art 49(4)(b) never named it |
| 1869-1871 | Annex VIII Section B point 9 | deleted (the Member States in which the system was placed on the market, put into service or made available) | both | as above; Art 49(4)(b) still names it (M-2) |

The as-enacted text of Art 43(3) is base-text lines 1214-1216 (`eu-ai-act-2024-1689.txt`); Annex VIII Section B as enacted is base-text lines 2600-2619.
The as-enacted branch of every dispatcher is unreachable through the keel's gate (this part's group applies from 2 August 2026), so the as-enacted functions are tested directly, with no date and no gate.

## Seats (P5)

One pair of files per seat that this part's ranges address.
Each seat file imports the layer-1 modules and the keel's, calls their functions and restates no rule; each question has `@export` and `@desc` and sits under a `§` heading in the text's order; the shared inputs carry the plan's exact `@desc`.
Each question is named `Under <provision>, as <role>, ...`; a duty is asked as "must I", a permission as "may I", a status as "is" or "does", and where a layer-1 function is a bar the question is the bar.
Audit: every question was listed beside the layer-1 function it calls (by script, from the final seat files) and read for direction (a permission or a yes title over a bar or an exemption function, or the reverse) and for subject ("must I" against "have I"; "does the authority" against a provider's duty).
Seat audit (second pass): 144 questions read, 0 retitled (direction 0, subject 0)
Read and left as they are, because neither class applies: the two person-seat questions of Art 46(2) name the refusal in their title ("whose authorisation was refused") and also ask it as an input (`the authorisation referred to in paragraph 1 is refused`), so a person who answers no gets a title that says the opposite of their answer.
Two layer-1 functions only restate a definition and take no date (`Annex VI point 1 ...`, `Art 43(4) the changes do not constitute a substantial modification`): their seat questions still ask `the date asked`, for uniformity, and say in a comment that the answer does not depend on it; the first returns a plain BOOLEAN in layer 1, so its seat question wraps it in `JUST` to give a `MAYBE BOOLEAN` like the others.
A seat question whose layer-1 function asks Art 2(2) (seam S14) takes the two Section B inputs, each with its own `@desc`: the first asks whether the AI system is related to a product covered by the legislation listed in Section B of Annex I and says that it matters only if the system is high-risk because of Article 6(1) with Annex I; the second asks whether the requirements have been integrated in that legislation and says that Article 2(2) makes it matter only for Articles 57 to 59, so that it does not change the answer to the question.
Both default to no in the cases, so every case that existed keeps its meaning; each such question has one added case with the route Article 6(1) with Annex I and the Section B products present, in which the answer is `JUST FALSE` (`NOTHING` where the question answers with a value): 92 questions in all (provider 72, deployer 10, authorised representative 3, product manufacturer 4, notified body 1, person 2, general-purpose AI model provider 0).
Every seat also asks the applicability question `Under Article 40, as <role>, does General apply on the date asked?`, which calls the keel's function for the `General` group.
Mirror cases (`-- MIRROR pair-...` in the case files): provider and notified body on the extension of a certificate (`pair-44-2`); provider and deployer on the consultation of Art 46(5) (`pair-46-5`); deployer and person on the stopping of the use and the discarding of the results after a refusal (`pair-46-2-stop`, `pair-46-2-discard`); provider and authorised representative on who registers (`pair-49-1a`, `pair-49-1b`, `pair-49-2a`, `pair-49-2b`); provider, authorised representative and notified body on who may affix the notified body's number (`pair-48-4`); provider and person on access to the restricted sections (`pair-49-4-access`).

| seat | slug | questions (incl. the applicability question) | assertions in its case file | note |
| --- | --- | --- | --- | --- |
| a person affected by an AI system | person | 4 | 21 | Art 46(2) stop and discard after a refusal; Art 49(4) access to the restricted sections |
| a provider of an AI system | provider | 97 | 595 | Articles 40 to 49 and Annexes V, VI, VIII, IX as addressed to a provider |
| a deployer of an AI system | deployer | 12 | 76 | Art 46(2), (5); Art 49(3); Annex VIII Section C |
| an importer | importer | 0 | 0 | none: no provision of this part's ranges addresses an importer (the word does not occur in lines 636-748, 1783-1799, 1840-1886) |
| a distributor | distributor | 0 | 0 | none: no provision of this part's ranges addresses a distributor (the word does not occur in those lines) |
| an authorised representative | rep | 5 | 30 | Art 48(4) affixing the number under instructions; Art 49(1), (2) registration |
| a product manufacturer | manufacturer | 5 | 33 | Art 43(3) first and third subparagraphs |
| a provider of a general-purpose AI model | gpai | 4 | 15 | Art 40(1), 41(3), 41(5): the general-purpose AI model limbs; date only, a model has no route to high-risk |
| a notified body | notified | 17 | 80 | Art 43(3) second subparagraph; Art 44; Art 45; Art 48(4) |
| total | | 144 | 850 | |

A market surveillance authority, the Commission, a notifying authority and a Member State have no seat; what Articles 41, 43(3), 46 and 49(4) give them appears only as what it means to one of the seats (what the deployer must do after a refusal, who may see the restricted sections).

## What the text turns out to say (numbered findings)

1.
   Chapter III Section 5 (Articles 40 to 49) is dated by no point of Art 113 as amended, so it is reached by the general date, 2 August 2026, while the Section 2 requirements it serves are dated 2 December 2027 (Annex III) and 2 August 2028 (Annex I).
   On 1 September 2027 Art 43(2), Art 47(2) and Art 49(1) apply to a system to be placed on the market on 3 December 2027 and Section 2 does not (M-1; `P5-tests-section-5-gap.l4`).
2.
   Art 43(3) as amended differs from the text as enacted in three places that change answers: the notified body's power gains a fact ("evidenced through the assessment as part of the existing notification") and a deadline (apply for designation by 28 January 2028: from 29 January 2028 the function `... has met the duty to apply for designation ...` answers `JUST FALSE` if no application was made, and a rule trace reads `BREACH`); the manufacturer's option turns on "harmonised standards to ensure compliance with all the relevant requirements" instead of "all harmonised standards covering all the relevant requirements"; and a fourth subparagraph sends a system that is both in Section A of Annex I and in Annex III to the Section A procedure.
3.
   Annex VIII Section B loses points 7 and 9 and Art 49(4)(b) still names point 9 (M-2); Art 49(4)(a) excepts points 6, 8 and 9 of Section A.
4.
   Art 44(2) fixes two limits (five years for Annex I, four for Annex III) and a system covered by both has both (F-44-2-both); the extension sentence has two conditions, a request ("At the request of the provider") and a re-assessment, and neither is closed by the text with "only" nor is either "where", "when" or "upon", so each gives `NOTHING` when it is missing (F-44-2-extension, M-8).
5.
   Art 46(2) lets a law-enforcement or civil protection authority put a system into service; this part encodes such an authority as a deployer (the text calls it neither), and the last sentence puts two duties on it (stop the use with immediate effect, discard all the results and outputs) that benefit no named person; the person seat asks them as a person on whom the system was used.
6.
   Art 46(7) is a flat "only the derogations ... established in that Union harmonisation legislation shall apply" for a product under the Section A legislation: the Art 46 derogation does not apply to it (`JUST FALSE`); for any other system the paragraph is silent (`NOTHING`).
7.
   Art 47(1) fixes a period in its own words (ten years after the placing on the market), computed from the date asked and the placement date: the last day is the day before the tenth anniversary, so a declaration asked about ten years and nine months after is outside it (`JUST FALSE`; F-47-1-period); the form of the declaration (written machine readable, physical or electronically signed) is a list the text does not close (`NOTHING` for a declaration in none of them).
8.
   Art 48(4) lets the notified body affix its own number, or the provider or the authorised representative do it "under its instructions"; without the instructions the sentence does not speak (`NOTHING`), which makes the provider's and the representative's questions answer `NOTHING` where the notified body's answers `JUST TRUE`.
9.
   Art 49(1) to (3) fix the time of registration ("before placing on the market", "before putting into service or using") but name no consequence of a late registration, so the encoding's only `BREACH` is the missed date; a registration made on the placing day is read as in time (F-49-before).
10.
    Art 49(4) is two sentences with different force: the first (registration in a secure non-public section with "only the following information") is a duty with a closed list and answers `JUST FALSE` for a point outside the list; the last ("Only the Commission and national authorities referred to in Article 74(8) shall have access") is a flat "only" and answers `JUST FALSE` for everyone else.
11.
    Annex VIII Section A point 12 ("this information shall not be provided for high-risk AI systems in the areas of law enforcement or migration, asylum and border control management referred to in Annex III, points 1, 6 and 7") is a flat negative inside a list item: for those systems the instructions for use are not provided (`JUST FALSE`), for the others they are; point 13 is "(optional)" and so not required.
12.
    Annex IX does not say who provides the information; Art 60(4)(c), in another part, makes the provider or prospective provider the one who has registered the testing with the information specified in Annex IX.
    The encoding puts the duty on the provider (F-IX-bearer) and asks the point as an input.
13.
    Article 2(2) lists the provisions that apply to a high-risk AI system under Article 6(1) related to Section B products ("only Article 6(1), Article 60a and Articles 102 to 112"); none of Articles 40 to 49 is on the list, so for such a system the operator's steps in this part (the harmonised standards and common specifications presumptions, conformity assessment, the EU declaration of conformity, the CE marking, registration, and the Annexes that serve them) do not apply on any date from 2 February 2025 (seam S14, M-7), whatever Art 113 and Art 111(2) say for other systems.

What the text does not answer (for the report): who bears Annex IX; whether a registration on the placing day is in time (F-49-before); whether Section 5 follows the general date or Sections 1 to 3 (M-1); what Art 49(4)(b) means by point 9 of Section B once that point is deleted (M-2); whether the registrant under Art 49(1) and (2) is the provider, the authorised representative, or both (M-3); whether the duty to discard the results of use under Art 46(2) binds the authority that used the system or anyone else.

What the stable binary does not accept, or accepts silently (probes run on 1.6.110 on 2026-11-17 on scratch files that were deleted afterwards; the other rules of the brief were followed, not re-measured):
- Loud: an `#ASSERT` whose `EQUALS` is on a second line is a parse error (`parse/unexpected-EQUALS`), so every assertion here is one line.
- Loud: `JUST x's field` is `check/not-a-function` followed by `check/type-mismatch`; write `JUST (x's field)`.
- Loud: `AFTER 3 WITHIN 5` in a rule is `parse/unexpected-identifier`; the deadline rules write `WITHIN (Day <date>) MINUS (Day <date asked>)` instead, which both builds read the same way.
- Silent: `NOT a AND b` parses as `NOT (a AND b)`; with a = TRUE and b = FALSE it is TRUE, so every `NOT` here is parenthesised.
- Silent: a trace difference between the two builds is not seen by `check.sh`; every `#TRACE` carries a `-- EXPECT FULFILLED` or `-- EXPECT BREACH` comment and `work/traces.py` compared all of them on both builds.
- Silent: the as-enacted branch of a dispatcher is dead through the gate for every group that applies on or after 27 July 2026 (this part's group applies from 2 August 2026), so each as-enacted function has no date and no gate and is tested directly; the dispatcher calls it.
- Followed from the brief without re-measuring: no `REFUSE`, sets, `TYPICALLY`, section `GIVEN` or opaque `DECLARE`; `WAITUNTIL` for `WAIT UNTIL`; `Date d m y` for `YMD`; leave `JL4_LIBRARY_PATH` unset.

## What check.sh prints

`L4=/…/l4-main-110 L4_MAIN=/…/l4-main-109 ./check.sh` run in this directory (target `main`: every module is run with both builds, and the four counts must match; exit status 0), unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
aia-annex-x.l4                                 0         0       0        0         0 |      0         0       0        0  same
aia-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
aia-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
aia-scope.l4                                   0         0       0        0         0 |      0         0       0        0  same
aia-timeline.l4                                0         0       0        0         0 |      0         0       0        0  same
P5-art-40-41-42.l4                             0         0       0        0         0 |      0         0       0        0  same
P5-art-43-annex-vi.l4                          0         0       0        0         0 |      0         0       0        0  same
P5-art-44-45-46.l4                             0         0       0        0         0 |      0         0       0        0  same
P5-art-47-48-annex-v.l4                        0         0       0        0         0 |      0         0       0        0  same
P5-art-49-annex-viii-ix.l4                     0         0       0        0         0 |      0         0       0        0  same
P5-cases-seat-deployer.l4                      0        76       0        0         0 |      0        76       0        0  same
P5-cases-seat-gpai.l4                          0        15       0        0         0 |      0        15       0        0  same
P5-cases-seat-manufacturer.l4                  0        33       0        0         0 |      0        33       0        0  same
P5-cases-seat-notified.l4                      0        80       0        0         0 |      0        80       0        0  same
P5-cases-seat-person.l4                        0        21       0        0         0 |      0        21       0        0  same
P5-cases-seat-provider.l4                      0       595       0        0         0 |      0       595       0        0  same
P5-cases-seat-rep.l4                           0        30       0        0         0 |      0        30       0        0  same
P5-seat-deployer.l4                            0         0       0        0         0 |      0         0       0        0  same
P5-seat-gpai.l4                                0         0       0        0         0 |      0         0       0        0  same
P5-seat-manufacturer.l4                        0         0       0        0         0 |      0         0       0        0  same
P5-seat-notified.l4                            0         0       0        0         0 |      0         0       0        0  same
P5-seat-person.l4                              0         0       0        0         0 |      0         0       0        0  same
P5-seat-provider.l4                            0         0       0        0         0 |      0         0       0        0  same
P5-seat-rep.l4                                 0         0       0        0         0 |      0         0       0        0  same
P5-section-5.l4                                0         0       0        0         0 |      0         0       0        0  same
P5-tests-art-40-41-42.l4                       0       142       0        0         0 |      0       142       0        0  same
P5-tests-art-43-annex-vi.l4                    0       224       0        0         0 |      0       224       0        0  same
P5-tests-art-44-45-46.l4                       0       160       0        0         0 |      0       160       0        0  same
P5-tests-art-47-48-annex-v.l4                  0       181       0        0         0 |      0       181       0        0  same
P5-tests-art-49-annex-viii-ix.l4               0       276       0        0         0 |      0       276       0        0  same
P5-tests-section-5-gap.l4                      0        20       0        0         0 |      0        20       0        0  same
TOTAL (31 modules)                             0      1853       0        0           |      0      1853       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline this run replaced: `check.sh` run on this directory with only the keel's four modules (`aia-annex-x.l4`, `aia-core.l4`, `aia-definitions.l4`, `aia-timeline.l4`) printed `TOTAL (4 modules)                              0         0       0        0` (every module 0 errors, 0 assertions, the same on both builds; the keel's tests are not in this deposit, and PLAN.md says the keel's own run was 14 modules and 666 assertions).
The deposit now holds 31 modules (the five keel modules, `aia-scope.l4` among them since the follow-up pass, and mine) and 1853 assertions satisfied on both builds.
