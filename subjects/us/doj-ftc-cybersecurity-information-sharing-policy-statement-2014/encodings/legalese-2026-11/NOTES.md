# DOJ/FTC Antitrust Policy Statement on Sharing of Cybersecurity Information (2014): coverage row, notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
This is a policy statement by the Department of Justice and the Federal Trade Commission about how they analyse the sharing of cyber threat information among competitors.
The text carries no sentence about its own legal force (checked by search for "force", "binding" and "legal advice" on 2026-11-26); the label above is this repository's.
Nothing in this row says what a court must hold.

## 1. Status and what was checked

Status: `draft`, version 0.1.0, written 2026-11-26.
This is a **coverage row**: it records what the statement says, part by part, and encodes none of it in L4 (section 2).
Checked: the whole text (9 pdf pages, 21 footnotes) was read; the table in section 3 was built from it; `check.sh` verifies the table's counts, every footnote number, every quotation and every page cited against the deposited text and its recorded hash (section 5).
Not checked: the extraction against the PDF beyond spot checks; anything outside the text; no domain expert has read it.
No L4 was written, so no compiler was run and no assertion exists.

## 2. Scope: what a coverage row is, and why there is no L4

The request (relayed 2026-11-25 as trigger word TRUSTBUSTER) was to ‘add a coverage row for the 2014 cybersecurity statement’, in the same method as the merger and IP rows.
The statement states no number, no threshold and no list of conditions that decides a case.
It states a framework (the rule of reason, borrowed from the 2000 Collaboration Guidelines), applies three considerations to cyber threat information (the purpose, the nature of the information, the likelihood of harm), and states a conclusion ("properly designed sharing ... should not raise antitrust concerns") with one limit (footnote 21).
A reviewer should know that an encoding of those parts is small: the defined term, a typed list of the three considerations, and the limit.
It is not made here, because the instruction was a coverage row.
So the table marks those parts `deferred`, and `deferred` here means "outside this row's scope", not "the text resists encoding".

## 3. Coverage table

Dispositions are the skill's four: `encoded`, `inert` (states no test), `out-of-scope`, `deferred`.
Page numbers are the `[pdf page N of 9]` markers of the deposited text, which are not the printed page numbers.
The body rows are the statement's parts in order; the 21 footnotes follow, one row each.

| id | pdf page | part | disposition | note |
| --- | --- | --- | --- | --- |
| B1 | 1 | Executive Summary, first paragraph: cyber threats are growing; sharing technical cyber threat information is one defence; some entities hesitate to share with competitors | inert | Background. States no test. |
| B2 | 1 | Executive Summary, second paragraph: the agencies "explain their analytical framework for information sharing" and say they "do not believe that antitrust is – or should be – a roadblock to legitimate cybersecurity information sharing"; cyber threat information is "very different" from competitively sensitive information | deferred | A position: the framework and the contrast between the two kinds of information. Deferred by this row's scope (section 2), not because the text resists encoding. |
| B3 | 1 | Executive Summary, third paragraph: the Division's October 2000 business review letter to EPRI, and "it remains the Agencies’ current analysis that properly designed sharing of cybersecurity threat information is not likely to raise antitrust concerns" | deferred | The statement's bottom line, with its qualifier "properly designed" (fork C1) and its modal "not likely to raise" (fork C3). |
| B4 | 2 | Section 1, first paragraph to its second sentence: the President's view, the agencies' commitment, the 2013 Executive Order | inert | Policy background. States no test. |
| B5 | 2-3 | Section 1, first paragraph, last sentence: sharing incident or threat reports, indicators, threat signatures and alerts, called collectively "cyber threat information" | deferred | The statement's one defined term; with footnotes 5 to 7 it would be the nouns module of an encoding. |
| B6 | 3 | Section 1, second paragraph: some private-to-private sharing already happens, through formal exchanges such as ISACs, with security benefits | inert | Background. States no test. |
| B7 | 3-4 | Section 1, third paragraph: the agencies "do not believe that antitrust is – or should be – a roadblock"; cyber threat information sharing "is highly unlikely to lead to a reduction in competition" and "would not be likely to raise antitrust concerns"; the statement is issued "to decrease uncertainty" | deferred | A position, repeating B2 and B3 in other words (fork C3). The reason for issuing the statement is inert. |
| B8 | 4-5 | Section 2.a, first two paragraphs: the sources of the framework (the agencies' guidelines, business review letters, advisory opinions); the primary concern is the sharing of competitively sensitive information "such as recent, current, and future prices, cost data, or output levels" | deferred | The primary concern as a typed list of variables. The business review and advisory opinion mechanics are inert. |
| B9 | 5 | Section 2.a, third paragraph: information sharing is typically examined under the rule of reason; the nature of the agreement may show the lack of harm; business purposes are taken into account; where harm seems likely the agencies will "analyze the agreement in more depth to evaluate countervailing efficiencies" | deferred | The mode of analysis. It is borrowed from the 2000 Collaboration Guidelines (fork C2). |
| B10 | 5-6 | Section 2.a, block quotation of the Collaboration Guidelines: information sharing may be procompetitive; the concern depends on the nature of the information; price, output, costs and strategic planning are more likely to raise concern than less sensitive variables; current and future plans more than historical information | deferred | Two ordered factors. Quoted from a document the agencies reportedly withdrew in December 2024 (fork C2). |
| B11 | 6 | Section 2.a, last paragraph: the agencies consider the extent to which competitively sensitive information likely would be disclosed to competitors; risk is lower when it is less sensitive; safeguards that prevent or minimise disclosure make collusion less likely | deferred | Three factors, to be reported when present, never weighed. |
| B12 | 6 | Section 2.b, introduction: the framework "applies irrespective of industry" | deferred | A statement of scope. |
| B13 | 6-7 | Section 2.b, "First": sharing can improve efficiency and help secure networks; it is "virtually always likely to be done in an effort to protect networks"; where it is not part of a conspiracy "of the type that typically harms competition", the rule of reason analysis would consider the valuable purpose | deferred | The first of three considerations. Its conditional (not part of a conspiracy) matches the limit in footnote 21. |
| B14 | 7 | Section 2.b, "Second": the nature of the information; cyber threat information is technical, a threat signature is "like a digital fingerprint", and sharing it is "very different" from sharing current or future prices, output or business plans | deferred | The second consideration. The signature and DoS examples are illustrations, not tests. |
| B15 | 7-8 | Section 2.b, "Finally": whether the exchange is likely to harm competition; cyber threat information "covers a limited category of information" and sharing it "appears unlikely in the abstract" to raise price or reduce output, quality, service or innovation; "this type of analysis is intensely fact-driven" | deferred | The third consideration, with its own caution that the analysis is fact-driven. |
| B16 | 8-9 | Section 2.b, the EPRI business review letter of 2 October 2000: what EPRI proposed to exchange, the interdictions on price, purchasing and future product discussions, and the Division's quoted conclusion | inert | A precedent narrative about one letter. The position it supports is B17. |
| B17 | 9 | Section 2.b, last paragraph: the letter's analysis "remains very current" and "the Agencies’ guidance establishes that properly designed sharing of cyber threat information should not raise antitrust concerns" | deferred | The bottom line again, with a third modal ("should not raise"; fork C3). |
| n.1 | 3 | footnote | inert | A cite to a White House page. |
| n.2 | 2 | footnote | inert | Describes Justice Department cybercrime units. |
| n.3 | 2 | footnote | inert | A cite to the February 2013 Executive Order. |
| n.4 | 2-3 | footnote | inert | Reports the 2011 legislative proposal's definition of a cybersecurity threat; the statement does not adopt it as its own term. |
| n.5 | 3 | footnote | deferred | Defines "indicators"; part of the nouns of B5. |
| n.6 | 3 | footnote | deferred | Defines "threat signatures"; part of the nouns of B5. |
| n.7 | 3 | footnote | deferred | Defines "alerts"; part of the nouns of B5. |
| n.8 | 3 | footnote | inert | A cite to the ISAC Council. |
| n.9 | 4 | footnote | inert | Cites the 2000 Collaboration Guidelines, the 1996 Healthcare Statements and the 1995 IP Licensing Guidelines (fork C2). |
| n.10 | 4 | footnote | inert | How to ask the Division for a business review letter. |
| n.11 | 4 | footnote | inert | How the FTC gives advisory opinions, with one example. |
| n.12 | 5 | footnote | inert | Cites to the three documents of footnote 9 for the concern about price coordination. |
| n.13 | 5 | footnote | inert | Cites the Collaboration Guidelines and the Gypsum case for the proposition that information sharing can be procompetitive. |
| n.14 | 5 | footnote | inert | A pin cite for the rule of reason sentence. |
| n.15 | 6 | footnote | inert | A pin cite for the block quotation, and the Gypsum case. |
| n.16 | 7 | footnote | inert | Explains what a denial of service attack is. |
| n.17 | 7 | footnote | inert | Says the agencies "understand that many companies have antitrust compliance programs"; a statement of understanding, not a condition. |
| n.18 | 8 | footnote | inert | Cites the EPRI letter. |
| n.19 | 9 | footnote | inert | Cites the rest of the EPRI letter and three other business review letters on exchanges of technical information. |
| n.20 | 9 | footnote | inert | Cites a 2014 speech that repeats the Division's current analysis. |
| n.21 | 9 | footnote | deferred | The one stated limit: "if an information sharing arrangement is being used as a cover to fix prices, allocate markets, or otherwise limit competition, antitrust issues could arise". |

Counts, computed from the table by `check.sh`: 38 rows (17 body rows, 21 footnote rows); encoded 0, inert 21, out-of-scope 0, deferred 17.

## 4. Fork register

Every entry is "assumed, not ruled": it is this session's reading, and the other readings are listed.

| id | text | readings | taken |
| --- | --- | --- | --- |
| C1 | "properly designed sharing of cyber threat information" (pdf pages 1 and 9) | (a) "properly designed" is a condition of the conclusion, to be met by the facts; (b) it is a description of the kind of sharing the agencies have in mind. The text never says what makes a design proper; the only guidance is the three considerations and footnote 21 | none taken; an encoding would take "properly designed" as an input and say so |
| C2 | the framework of section 2.a is quoted from the 2000 Collaboration Guidelines (pdf pages 4 to 6) | (a) the statement's framework stands on its own quoted text; (b) the statement's framework rests on a document the agencies have withdrawn (reported, section 6), so its present weight is unclear | none taken; recorded as an open question |
| C3 | three modals for one conclusion: "is not likely to raise antitrust concerns" (pdf page 1), "would not be likely to raise antitrust concerns" (pdf page 4), "should not raise antitrust concerns" (pdf page 9) | (a) one position in three voices; (b) three different strengths | (a) for the table; any encoding must pick, and keep the text's own modal in each result |
| C4 | the row's scope | (a) coverage row only; (b) a small typed encoding of B5, B13 to B15, B17 and footnote 21 | (a), by the instruction; the table marks the parts (b) would encode as `deferred` |
| C5 | footnote 17 and the EPRI narrative (B16) | (a) `inert`: they state an understanding and one precedent, not a rule; (b) `deferred`: the statement leans on both | (a) |

## 5. Checks

`./check.sh` runs with the system `python3 -I` and nothing else.
It checks: the footnote rows are exactly n.1 to n.21, once each; every disposition is one of the four; the counts line in section 3 equals the table; every quotation of five words or more in this file (in double quotes) occurs in the source text, after whitespace, hyphen and dash normalisation; every pdf page cited is between 1 and 9; and the sha256 of the deposited text equals the one recorded in its `.meta.json`.
It exits non-zero on any failure.
It is a check of this file against the text, not of any encoding.

## 6. Withdrawn and superseded documents

What the text itself says (read at source): the statement cites, in footnote 9, the 2000 Antitrust Guidelines for Collaborations Among Competitors, the 1996 Statements of Antitrust Enforcement Policy in Health Care and the 1995 Antitrust Guidelines for the Licensing of Intellectual Property, and quotes the first at pdf pages 5 and 6.
The 2017 IP Licensing Guidelines say they replace the 1995 ones (their note 1, pdf page 3, read at source in the deposit of that subject), so footnote 9's third document has been replaced.
The statement says it replaces nothing.
What was only reported: the 2000 Collaboration Guidelines were withdrawn by the FTC and DOJ on 11 December 2024, as an FTC press release says (https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-doj-withdraw-guidelines-collaboration-among-competitors); this session could not fetch it because ftc.gov refuses automated clients, and knows it from a search summary only.
The status of the 1996 Healthcare Statements was not checked.
That the statement itself remains listed: the DOJ's index page of guidelines and policy statements (https://www.justice.gov/atr/guidelines-and-policy-statements-0) lists it, as read on 2026-11-25 in a saved copy of the page that says "Updated November 17, 2025".
Whether the agencies have issued a successor statement was not searched for.

## 7. Open questions for a domain expert

1. What follows for this statement from the withdrawal of the Collaboration Guidelines it quotes (fork C2)?
2. Does "properly designed" have a settled meaning in agency practice (fork C1)?
3. Has a successor to this statement been issued, and does the FTC publish the same text as the one on justice.gov?
4. Is the conclusion of pdf page 9 ("should not raise antitrust concerns") meant to be weaker or stronger than the page 1 statement of the agencies' "current analysis" (fork C3)?
