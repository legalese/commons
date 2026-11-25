# DOJ/FTC Antitrust Policy Statement on Sharing of Cybersecurity Information (2014): coverage row, notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
This is a policy statement by the Department of Justice and the Federal Trade Commission about how they analyse the sharing of cyber threat information among private entities, especially competitors.
The text has no sentence about its own legal force (checked by search for the words "force", "binding" and "legal advice" on 2026-11-26; `check.sh` repeats the search); the label above is this repository's.
Nothing in this row says what a court must hold.

## 1. Status and what was checked

Status: `draft`, version 0.1.0, written 2026-11-26.
This is a **coverage row**: it records what the statement says, part by part, and encodes none of it in L4 (section 2).
Checked: the whole text (9 pdf pages, 21 footnotes) was read; the table in section 3 was built from it; `check.sh` checks the table and the quotations against the deposited text (section 5, which also says what it cannot catch); an adversarial review by a fresh agent found twelve discrepancies, all dispositioned in section 8.
Not checked: the extraction against the PDF beyond spot checks; anything outside the text; no domain expert has read it.
No L4 was written, so no compiler was run and no assertion exists.

## 2. Scope: what a coverage row is, and why there is no L4

The request (relayed 2026-11-25 as trigger word TRUSTBUSTER) was to ‘add a coverage row for the 2014 cybersecurity statement’, in the same method as the merger and IP rows.
The statement states no number, no threshold and no list of conditions that decides a case.
It states a framework (the rule of reason, borrowed from the 2000 Collaboration Guidelines), applies three considerations to cyber threat information (the purpose, the nature of the information, the likelihood of harm), and states a conclusion ("properly designed sharing of cyber threat information should not raise antitrust concerns").
Guidance on what makes sharing safe is spread through the text: the safeguards of pdf page 6, the conditions of the EPRI letter on pdf page 8, footnote 19's concern, and the one limit stated as such in footnote 21 (fork C1).
An encoding of those parts would be small: the defined term, a typed list of the three considerations and the factors of B11, and the limit.
It is not made here, because the instruction was a coverage row.
So the table marks those parts `deferred`, and `deferred` here means "outside this row's scope", not "the text resists encoding".

## 3. Coverage table

Dispositions are the skill's four: `encoded`, `inert` (states no test), `out-of-scope`, `deferred`.
Page numbers are the `[pdf page N of 9]` markers of the deposited text; they count pdf pages, and in this document pages 2 to 9 carry the same printed numbers in their footers while page 1 has none.
The body rows are the statement's parts in order; the 21 footnotes follow, one row each.

| id | pdf page | part | disposition | note |
| --- | --- | --- | --- | --- |
| B1 | 1 | Executive Summary, first paragraph: cyber threats are growing; sharing technical cyber threat information is one defence; some entities hesitate to share with competitors | inert | Background. States no test. |
| B2 | 1 | Executive Summary, second paragraph: the agencies explain their "analytical framework for information sharing" and say they "do not believe that antitrust is – or should be – a roadblock to legitimate cybersecurity information sharing"; cyber threat information is "very different" from competitively sensitive information | deferred | A position: the framework and the contrast between the two kinds of information. Deferred by this row's scope (section 2), not because the text resists encoding. "Legitimate" is fork C7. |
| B3 | 1 | Executive Summary, third paragraph: the Division's October 2000 business review letter to EPRI, and "it remains the Agencies’ current analysis that properly designed sharing of cybersecurity threat information is not likely to raise antitrust concerns" | deferred | The statement's bottom line, with its qualifier "properly designed" (fork C1) and its modal "not likely to raise" (fork C3). Page 1 says EPRI's proposal included real-time exchange; page 8 says the program "eventually might" (fork C9). |
| B4 | 2-3 | Section 1, first paragraph, every sentence but the one that introduces the defined term of B5: the President's view, the national strategy, the 2013 Executive Order, the agencies' commitment; it speaks of sharing "between the government and industry, and among industry participants" | inert | Policy background. States no test. Who shares is fork C8. |
| B5 | 2-3 | Section 1, first paragraph, the sentence that begins "In particular": sharing incident or threat reports, indicators, threat signatures and alerts, called collectively "cyber threat information" | deferred | The statement's operative defined term (the Agencies, the Division and the Department are also defined, as names). With footnotes 5 to 7 it would be the nouns module of an encoding. Its reach is fork C6. |
| B6 | 3 | Section 1, second paragraph: some private-to-private sharing already happens, through formal exchanges such as ISACs, with security benefits | inert | Background. States no test. |
| B7 | 3-4 | Section 1, third paragraph: the agencies "do not believe that antitrust is – or should be – a roadblock to legitimate cybersecurity information sharing"; the sharing of cyber threat information is "highly unlikely to lead to a reduction in competition" and "would not be likely to raise antitrust concerns"; the statement is issued to decrease uncertainty | deferred | A position, repeating B2 and B3 in other words (fork C3). The reason for issuing the statement is inert. |
| B8 | 4-5 | Section 2.a, first paragraph: the sources of the framework (the agencies' guidelines, business review letters, advisory opinions); the primary concern is the sharing of competitively sensitive information "such as recent, current, and future prices, cost data, or output levels"; the joint Collaboration Guidelines are a good overview | deferred | The primary concern as a typed list of variables. The business review and advisory opinion mechanics are inert (fork C10). |
| B9 | 5 | Section 2.a, second paragraph: information sharing is typically examined under the rule of reason; the "central question" is "whether the relevant agreement likely harms competition by increasing the ability or incentive profitably to raise price above or reduce output, quality, service, or innovation below what likely would prevail in the absence of the relevant agreement"; the nature of the agreement may show the lack of harm; business purposes are taken into account; where harm seems likely the agencies will "analyze the agreement in more depth to evaluate countervailing efficiencies" | deferred | The mode of analysis, and the one sentence of the statement shaped like a test (the central question; B15 reuses its terms). Borrowed from the 2000 Collaboration Guidelines (fork C2). |
| B10 | 5-6 | Section 2.a, the lead-in and block quotation of the Collaboration Guidelines: information sharing may be procompetitive; the concern depends on the nature of the information; price, output, costs and strategic planning are more likely to raise concern than less sensitive variables; current and future plans more than historical information | deferred | Two ordered factors. Quoted from a document the agencies reportedly withdrew in December 2024 (fork C2). |
| B11 | 6 | Section 2.a, last paragraph: the agencies consider the extent to which competitively sensitive information likely would be disclosed to competitors; risk is lower when it is less sensitive; "the nature and detail of the information disclosed and the context in which information is shared are highly relevant"; appropriate safeguards make collusion less likely | deferred | Factors to be reported when present, never weighed: the extent of disclosure, the information's sensitivity, its nature and detail, the context, the safeguards. |
| B12 | 6 | Section 2.b, introduction: the framework "applies irrespective of industry" | deferred | A statement of scope. |
| B13 | 6-7 | Section 2.b, "First": sharing can improve efficiency and help secure networks; "It appears that this sharing is virtually always likely to be done in an effort to protect networks"; where it is not part of a conspiracy "of the type that typically harms competition", the rule of reason analysis would consider the valuable purpose | deferred | The first of three considerations. Its condition (not part of a conspiracy) matches the limit in footnote 21. |
| B14 | 7 | Section 2.b, "Second": the nature of the information; "Cyber threat information typically is very technical in nature", a threat signature is "like a digital fingerprint", and sharing it is "very different" from sharing current or future prices, output or business plans | deferred | The second consideration. The signature and DoS examples are illustrations, not tests. |
| B15 | 7-8 | Section 2.b, "Finally": whether the exchange is likely to harm competition; cyber threat information "covers a limited category of information" and sharing it "appears unlikely in the abstract" to raise price or reduce output, quality, service or innovation; "this type of analysis is intensely fact-driven" | deferred | The third consideration, with its own caution. The paragraph runs on, with no break, into the EPRI narrative (B16). |
| B16 | 8-9 | Section 2.b, the same paragraph continued: the EPRI business review letter of 2 October 2000: what EPRI proposed to exchange (best practices and information about cybersecurity vulnerabilities), and the Division's quoted conclusion that "the proposed interdictions on price, purchasing and future product innovation discussions" would suffice if the information exchanged is limited to physical and cybersecurity issues | deferred | The only place the text describes a design it found sufficient (limits on subject matter and interdictions on price, purchasing and future product discussions). B17 draws its conclusion from it with "Thus". Footnote 19 is its counterpart (a concern if the exchange is a cover). |
| B17 | 9 | Section 2.b, last paragraph: the letter's analysis "remains very current" and "the Agencies’ guidance establishes that properly designed sharing of cyber threat information should not raise antitrust concerns" | deferred | The bottom line again, with a further modal ("should not raise"; fork C3). |
| n.1 | 2 | footnote | inert | A cite to a White House page. |
| n.2 | 2 | footnote | inert | Describes Justice Department cybercrime units. |
| n.3 | 2 | footnote | inert | A cite to the February 2013 Executive Order. |
| n.4 | 2-3 | footnote | inert | Reports the 2011 legislative proposal's definition of a cybersecurity threat; the statement does not adopt it as its own term (fork C5). |
| n.5 | 3 | footnote | deferred | Defines "indicators"; part of the nouns of B5. |
| n.6 | 3 | footnote | deferred | Defines "threat signatures"; part of the nouns of B5. |
| n.7 | 3 | footnote | deferred | Defines "alerts"; part of the nouns of B5. |
| n.8 | 3 | footnote | inert | A cite to the ISAC Council. |
| n.9 | 4 | footnote | inert | Cites the 2000 Collaboration Guidelines, the 1996 Healthcare Statements and the 1995 IP Licensing Guidelines (fork C2). |
| n.10 | 4 | footnote | inert | How to ask the Division for a business review letter: a firm concerned about "a specific proposed program" may use the business review process (fork C10). |
| n.11 | 4 | footnote | inert | How the FTC gives advisory opinions, with one example. |
| n.12 | 5 | footnote | inert | Cites the 2000 Collaboration Guidelines, the Healthcare Statements and the 1995 IP Licensing Guidelines for the concern about price coordination. |
| n.13 | 5 | footnote | inert | Cites the Collaboration Guidelines and the Healthcare Statements, and the Gypsum case for the proposition that information sharing can be procompetitive. |
| n.14 | 5 | footnote | inert | A pin cite for the rule of reason sentences. |
| n.15 | 6 | footnote | inert | Cites the Collaboration Guidelines and the Gypsum case; it glosses Gypsum as "examining whether the information exchanged has a legitimate purpose, or is more likely to be used for collusive purposes", the nearest the text comes to saying what "legitimate" means (fork C7). |
| n.16 | 7 | footnote | inert | Explains what a denial of service attack is. |
| n.17 | 7 | footnote | inert | Says the agencies "understand that many companies have antitrust compliance programs"; a statement of understanding, an extra ground and not a condition (fork C5). |
| n.18 | 8 | footnote | inert | Cites the EPRI letter. |
| n.19 | 9 | footnote | inert | Cites the EPRI letter again ("Id. at 3-4") and three other business review letters on exchanges of technical information; one of them records the Department's note that it "would be concerned if parties, under the guise of a Year 2000 remedial program, exchanged price or other competitively-sensitive information". |
| n.20 | 9 | footnote | inert | Cites a 2014 speech by a Deputy Assistant Attorney General that says "it remains the Antitrust Division’s current analysis that properly designed sharing of cyber-security threat information is not likely to raise antitrust concerns": the sentence of page 1 with "the Antitrust Division’s" for "the Agencies’" (fork C3). |
| n.21 | 9 | footnote | deferred | The one limit the statement states as such: "if an information sharing arrangement is being used as a cover to fix prices, allocate markets, or otherwise limit competition, antitrust issues could arise". |

Counts, computed from the table by `check.sh`: 38 rows (17 body rows, 21 footnote rows); encoded 0, inert 20, out-of-scope 0, deferred 18.

## 4. Fork register

Every entry is "assumed, not ruled": it is this session's reading, and the other readings are listed.

| id | text | readings | taken |
| --- | --- | --- | --- |
| C1 | the phrase "properly designed sharing of cyber threat information" (pdf page 9); page 1 reads "properly designed sharing of cybersecurity threat information"; page 4 states the same conclusion without "properly designed" | (a) "properly designed" is a condition of the conclusion, to be met by the facts; (b) it describes the kind of sharing the agencies have in mind; (c) its content is the sum of the guidance in the text: the three considerations, the safeguards of pdf page 6, the conditions of the EPRI letter of pdf page 8, footnote 19's concern and the limit in footnote 21. The text never defines it | none taken; an encoding would take "properly designed" as an input and say so |
| C2 | the framework of section 2.a is quoted from the 2000 Collaboration Guidelines (pdf pages 4 to 6) | (a) the statement's framework stands on its own quoted text; (b) the statement's framework rests on a document the agencies have withdrawn (reported, section 6), so its present weight is unclear | none taken; recorded as an open question |
| C3 | several wordings of one conclusion: "is not likely to raise antitrust concerns" (pdf page 1), "highly unlikely to lead to a reduction in competition" and "would not be likely to raise antitrust concerns" (pdf page 4), "appears unlikely in the abstract" (pdf page 7, about the likelihood of harm), "should not raise antitrust concerns" (pdf page 9); footnote 20 gives the page 1 sentence in a Division speech with "the Antitrust Division’s" for "the Agencies’" | (a) one position in several voices; (b) several different strengths, and the Division and the Agencies are not the same speaker | (a) for the table; any encoding must pick, and keep the text's own modal in each result |
| C4 | the row's scope | (a) coverage row only; (b) a small typed encoding of B5, B13 to B17 and footnote 21 | (a), by the instruction; the table marks the parts (b) would encode as `deferred` |
| C5 | footnotes 4 and 17 | (a) `inert`: footnote 4 reports a proposal's definition the statement does not adopt, and footnote 17 states an understanding as an extra ground; (b) `deferred`: the statement leans on both | (a) |
| C6 | how far "cyber threat information" reaches: it is introduced by "such as" and "(collectively" (pdf pages 2 to 3); the Executive Summary names "such as threat signatures, indicators, and alerts" (pdf page 1); the title and several passages say "cybersecurity information" (pdf pages 1 to 3); the EPRI program exchanged best practices and information about vulnerabilities (pdf page 8) | (a) a closed list of four kinds; (b) an open list; (c) whatever "cybersecurity information" covers | none taken; an encoding would take the category as the caller's finding |
| C7 | "legitimate" in "legitimate cybersecurity information sharing" (pdf pages 1 and 3) is undefined; the nearest gloss is footnote 15's account of Gypsum (pdf page 6) | (a) legitimate means within the three considerations; (b) legitimate means Gypsum's purpose test | none taken |
| C8 | who shares: the text speaks of sharing "between the government and industry, and among industry participants" (pdf page 2) and of private-to-private sharing (pdf page 3), while the antitrust concern is sharing with competitors | (a) the conclusion covers private-to-private sharing only; (b) it covers any sharing | none taken |
| C9 | a slip in the text: pdf page 1 says the EPRI proposal was "to exchange certain cybersecurity information, including exchanging actual real-time cyber threat and attack information"; pdf page 8 says the program "eventually might include a discussion and analysis of actual real time cyber threat and attack information" | (a) the real-time exchange was part of the proposal; (b) it was a possible later addition | none taken; recorded, because the statement leans on the EPRI letter |
| C10 | the business review route: footnote 10 says a firm concerned about "a specific proposed program" may use the business review process (pdf page 4); the statement states no clearance of its own and calls the analysis "intensely fact-driven" (pdf page 8) | (a) the conclusion is general guidance and a firm with a specific program may seek a letter; (b) the statement expects firms with a specific program to seek one | none taken |

## 5. Checks

`./check.sh` runs with the system `python3 -I` and nothing else, and exits non-zero on any failure.
It checks: the sha256 of the deposited text against its `.meta.json`; that the footnote rows are exactly n.1 to n.21, once each; that every disposition is one of the four; that the counts line in section 3 equals the table; that the page given for each footnote row is the page on which that footnote's text begins, computed from the text; that every quotation of five words or more in a table row occurs on a page that row cites; that every quotation of five words or more anywhere in this file occurs in the text; that double quotes are balanced on each line; that the text has none of the words "force", "binding" or "legal advice".
It cannot catch: a wrong disposition; a wrong page for a body row that has no quotation; a quotation of fewer than five words, or in curly or single quotes; a quotation that differs from the text only in letter case or in curly-versus-straight punctuation (both sides are normalised); a quotation that sits on a cited page but is attributed to the wrong paragraph; pages cited in sections 4 and 6; a sentence of the text that no row covers.
Completeness of the table was checked by the adversarial review (section 8), not by the script.

## 6. Withdrawn and superseded documents

What the text itself says (read at source): the statement cites, in footnote 9 (pdf page 4), the 2000 Antitrust Guidelines for Collaborations Among Competitors, the 1996 Statements of Antitrust Enforcement Policy in Health Care and the 1995 Antitrust Guidelines for the Licensing of Intellectual Property, and quotes the first at pdf pages 5 and 6; footnote 12 (pdf page 5) cites all three again.
The 2017 IP Licensing Guidelines say they replace the 1995 ones (their note 1, pdf page 3, read at source in the deposit of that subject), so the third of footnote 9's documents has been replaced.
The statement has no sentence saying it replaces a document.
What was only reported: the 2000 Collaboration Guidelines were withdrawn by the FTC and DOJ on 11 December 2024, as an FTC press release says (https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-doj-withdraw-guidelines-collaboration-among-competitors); this session could not fetch it because ftc.gov refuses automated clients, and knows it from a search summary only.
The status of the 1996 Healthcare Statements was not checked.
A search of the saved copy of the DOJ index page of guidelines and policy statements on 2026-11-26 found neither the Collaboration Guidelines nor the Healthcare Statements listed; that is consistent with the reported withdrawal of the first but is not evidence of it, and says nothing of the second.
That the statement itself remains listed: the same saved copy, retrieved on 2026-11-25 from https://www.justice.gov/atr/guidelines-and-policy-statements-0, lists it and says "Updated November 17, 2025".
Whether the agencies have issued a successor statement was not searched for.

## 7. Open questions for a domain expert

1. What follows for this statement from the withdrawal of the Collaboration Guidelines it quotes (fork C2)?
2. Does "properly designed" have a settled meaning in agency practice (fork C1)?
3. Has a successor to this statement been issued, and does the FTC publish the same text as the one on justice.gov?
4. Is the conclusion of pdf page 9 meant to be weaker or stronger than the page 1 statement of the agencies' "current analysis", and does it matter that the Division speech of footnote 20 says the same of the Division alone (fork C3)?
5. Was real-time exchange part of the EPRI proposal, or a later possibility (fork C9)?

## 8. Adversarial review

A fresh agent that had not seen the row, working from the text, reviewed this row on 2026-11-26 and reported twelve findings.
All were checked against the text by the author before any change; each is listed with what was done.
1. Footnote 1 was given pdf page 3; it is on page 2. Fixed; `check.sh` now computes every footnote page from the text, so this class of slip fails the check.
2. Section 5 said the script checked "every page cited". It only checked the range. Fixed: the script now checks footnote pages and quotations against cited pages, and section 5 lists what it still cannot catch.
3. B16 (the EPRI narrative) was `inert`; the conclusion is drawn from it with "Thus" and it is the only description of a design the text found sufficient. Agreed and changed to `deferred`; fork C5 no longer mentions it. Footnote 4 was missing from C5 and was added.
4. C1 and section 2 said the only guidance is the three considerations and "one limit". The text gives more (the safeguards, the EPRI conditions, footnote 19). Fixed in C1 and section 2; footnote 21 is described as the one limit stated as such.
5. C3 missed wordings of the conclusion on pages 4 and 7 and footnote 20's Division speech. Added.
6. Missing forks: the reach of the defined term (C6), "legitimate" (C7), who shares (C8), the EPRI real-time slip (C9) and the business review route (C10). Added.
7. B4, B8 and B9 miscounted sentences and paragraphs. Rewritten from the text: B4 covers every sentence of the first paragraph of section 1 but the one that introduces the term; B8 is the first paragraph of section 2.a and B9 the second.
8. B9 omitted the "central question" and B11 the "context in which information is shared". Added.
9. The text said the page markers are not printed page numbers; pages 2 to 9 are printed 2 to 9. Fixed.
10. Footnote 12 also cites the 1995 IP guidelines and the Healthcare Statements, and the text has no sentence saying the statement replaces anything. Section 6 now says both; the cheap index check was made and is reported in section 6.
11. BRIEF.md cited a section 8 that did not exist and said the review had been run before it had; `encoding.json` said the result was ‘set by the last run’. Fixed: this section now exists, and `encoding.json` states its counts.
12. Cosmetics: B5's "one defined term", dropped hedges ("It appears that", "typically"), "innovation" in B16, "Id. at 3-4" in footnote 19, the Healthcare Statements in footnote 13. All fixed.
