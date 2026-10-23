# EU AI Act serious-incident reporting: answers decided from the source alone

Written 2026-10-24 BEFORE opening anything in `encodings/solo-2026-10/`.
Sources read: `registers/source-bundle/eu-ai-act-2024-1689.txt` (cited `A:line`) and `eu-omnibus-2026-1744.txt` (cited `O:line`).
Seat: the provider.
Not legal advice.

## 0. Conventions I fix before answering

- **Day count.** "not later than N days after the provider ... becomes aware" (A:1731, 1733, 1734): the awareness day is day 0, so the last day on which a report is in time is awareness + N calendar days; awareness + N + 1 is late.
  The text does not say calendar or working days.
  Regulation (EEC, Euratom) No 1182/71 (periods, dates and time limits) would roll a deadline falling on a Saturday, Sunday or holiday to the next working day, but it is not deposited, so I do not apply it (ambiguity F1).
- **Art 52(1) "within two weeks"** = 14 days, same convention; anchor is the earlier of "requirement is met" and "it becomes known that it will be met" (A:1313).
- **"shall apply from D"** (A:2199-2206, O:617-631): applies on D and after; does not apply on D-1.
- **"by 2 August 2027"** (Art 111(3), A:2160): compliance required on 2 Aug 2027 and after; not before (ambiguity F6).
- Article 73 is in **Chapter IX** (A:1715 heading, A:1728), not Chapter III.

## (a) Article 73 clocks (provider of a high-risk AI system)

Trigger: a serious incident, Art 3(49) (A:537-545): death or serious harm to health (a); serious and irreversible disruption of critical infrastructure (b); infringement of Union-law fundamental-rights obligations (c); serious harm to property or environment (d).

| route | provision | outer limit after awareness | also |
|---|---|---|---|
| general | 73(2), A:1731 | 15 days | "immediately after" causal link or reasonable likelihood; "take account of severity" (no number) |
| widespread infringement (Art 3(61)) or 3(49)(b) critical infrastructure | 73(3), A:1733 | 2 days | "immediately" |
| death of a person | 73(4), A:1734 | 10 days | "immediately after ... established, or as soon as it suspects" |
| death AND critical infrastructure / widespread | 73(3)+(4) both "notwithstanding paragraph 2" | 2 days (both apply; meeting both needs 2) | ambiguity F3 |
| serious harm to health, not death | 73(2) | 15 days | |
| initial incomplete report | 73(5), A:1735 | permitted "where necessary to ensure timely reporting"; it meets the clock; complete report: **no period stated** | |
| investigation after reporting | 73(6), A:1736 | "without delay": **no period stated** | |

Day-count cells (awareness date -> last day in time; next day late):

| clock | awareness | last day in time | first late day |
|---|---|---|---|
| 15 | 2028-02-14 | 2028-02-29 (leap day) | 2028-03-01 |
| 15 | 2028-02-15 | 2028-03-01 | 2028-03-02 |
| 15 | 2028-02-29 | 2028-03-15 | 2028-03-16 |
| 15 | 2028-01-31 | 2028-02-15 | 2028-02-16 |
| 15 | 2027-12-20 | 2028-01-04 | 2028-01-05 |
| 15 | 2028-08-31 | 2028-09-15 | 2028-09-16 |
| 10 | 2028-02-19 | 2028-02-29 | 2028-03-01 |
| 10 | 2028-02-29 | 2028-03-10 | 2028-03-11 |
| 10 | 2027-12-25 | 2028-01-04 | 2028-01-05 |
| 10 | 2028-01-31 | 2028-02-10 | 2028-02-11 |
| 2 | 2028-02-27 | 2028-02-29 | 2028-03-01 |
| 2 | 2028-02-28 | 2028-03-01 | 2028-03-02 |
| 2 | 2028-02-29 | 2028-03-02 | 2028-03-03 |
| 2 | 2027-12-30 | 2028-01-01 | 2028-01-02 |
| 2 | 2028-01-31 | 2028-02-02 | 2028-02-03 |
| 2 | 2029-02-28 | 2029-03-02 | 2029-03-03 |
| 2 | 2029-02-27 | 2029-03-01 | 2029-03-02 |

Exclusions:
- 73(9), A:1740: Annex III system, provider subject to equivalent Union reporting law -> only 3(49)(c) incidents are notified; a death from such a system: **no Art 73 duty**.
- 73(10), A:1741: medical-device systems (MDR/IVDR) -> only 3(49)(c), and to the national competent authority the Member State chose.
- Not a high-risk AI system -> no Art 73 duty.
- Section B Annex I products: Art 2(2) (A:419; as amended O:136) -> only 6(1), (60a), 102-109/112 apply -> no Art 73 duty. As amended, machinery moved from Section A to Section B (O:636-640) -> no Art 73 duty for machinery AI as amended.
- Art 111(2) grace: system placed on the market / put into service before 2 Aug 2026 (enacted, A:2159) or before the Chapter III application date (amended, O:606) -> the Regulation applies only if significantly changed in design from that date (public-authority systems: by 2 Aug 2030).

Anchor ambiguity F2: "after the provider or, where applicable, the deployer, becomes aware". Reading A: clock runs from the earlier of provider's and deployer's awareness. Reading B: "where applicable, the deployer" is the Art 26(5) fallback where the deployer itself reports (A:1023). I take reading A for the provider's clock when a deployer was aware first.

Recipient (73(1), A:1730): market surveillance authorities of the Member States where the incident occurred.

## (b) Article 55(1)(c) (provider of a GPAI model with systemic risk)

- To whom: the AI Office and, as appropriate, national competent authorities (A:1369). AI Office = the Commission (Art 3(47), A:533).
- By when: "without undue delay". **No number of days stated.** The answer must be "no period stated", not 15/10/2.
- What: relevant information about serious incidents and possible corrective measures; also keep track of and document.
- Classification (Art 51, A:1304-1309): systemic risk if (a) high impact capabilities, or (b) Commission decision.
  Presumption 51(2): cumulative training compute **greater than** 10^25 FLOP (XHTML superscript, per the formulas sidecar; text file flattens to "1025").
  - exactly 10^25 FLOP -> not presumed.
  - 10^25 + 1 FLOP -> presumed.
  - 2 x 10^25 -> presumed.
  - 10^24 -> not presumed; still systemic risk if Commission designates (51(1)(b), 52(4)).
  - meets 51(1)(a), 52(2) arguments rejected -> systemic risk (52(3)).
  - meets 51(1)(a), arguments pending -> classified (51(1) "shall be classified ... if it meets"), ambiguity F7.
- Art 52(1) notification to the Commission: without delay and within two weeks (14 days) after requirement met or known it will be met.
  - met 2025-08-02 -> last day 2025-08-16; 2025-08-17 late.
  - met 2028-02-18 -> 2028-03-03 (leap year); 2028-03-04 late.
  - met 2027-02-18 -> 2027-03-04; 2027-03-05 late.
  - known-will-be-met 2027-02-10, met 2027-02-20 -> anchor 2027-02-10 -> 2027-02-24.
- When it applies (Art 113(b), A:2204): Chapter V from 2 Aug 2025.
  - model placed on the market on/after 2 Aug 2025: duty from 2 Aug 2025 (and from placing).
  - model placed before 2 Aug 2025: Art 111(3) (A:2160) "take the necessary steps in order to comply ... by 2 August 2027". I read: duty bites from 2 Aug 2027 (F6).
  - 2025-08-01: no duty (Chapter V not yet applicable).
- Not systemic risk -> no 55(1)(c) duty (Art 53 duties only).

## (c) The Omnibus 2026/1744 (read every point of Art 1, 1-43; Arts 2-4)

In force: published 24.7.2026 (O:8); enters into force third day following (O:764) = **27 July 2026** (same date as new 113(d), O:631).
Points touching the scope:

| point | line | change | effect on a provider's report |
|---|---|---|---|
| 1(31)(b) | O:416-430 | Art 75(1) replaced: AI Office exclusively competent for AI systems based on GPAI models where model and system come from the same provider or same undertaking, except (i) Annex I products, (ii) Annex III point 2, (iii) law-enforcement/border/financial under 74(6), (iv) Annex III point 8 justice; and (b) systems constituting or integrated into a VLOP/VLOSE | decides who is AI-Office-supervised |
| 1(31)(c) | O:434 | **Art 75(1a) inserted**: such providers of high-risk AI systems report serious incidents **to the AI Office**; Art 73(2)-(9) apply mutatis mutandis; AI Office transmits to MSA where provider/legal representative is situated | recipient changes; clocks unchanged (15/2/10) |
| 1(32) | O:455-535 | Arts 75a-75d inserted; **75c(4)(a)**: for operators under 75(1), infringement of any applicable provision, *including those not listed in Art 99(4)*, subject to fines as in 99(4); 75c(5) periodic penalties up to 5%/day; 75c(8) 5-year limitation | creates a fine ceiling for an AI-Office-supervised provider's failure to report under 73 |
| 1(38)(a) | O:591 | Art 99(1) replaced: Member State penalties "may also include administrative fines", "any infringement", SMCs | still no Union ceiling for 73 |
| 1(38)(b) | O:595 | 99(4)(da) inserted: Art 25(2),(4) | not reporting |
| 1(38)(c) | O:600 | 99(6a): SMCs get the lower of amount/percentage in 99(4),(5) | |
| 1(39)(a) | O:606 | 111(2) grace now keyed to the Chapter III application date | |
| 1(40) | O:613-631 | 113(a) replaced (Art 5 points), **113(c) replaced**: Chapter III Sections 1-3 from 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I); (d) Arts 102-110 from 27 Jul 2026. 113(b) unchanged | Art 73 date (see below) |
| 1(2)(a), 1(41) | O:136, 636-640 | Art 2(2) replaced; machinery to Section B | no 73 for machinery AI |
| 1(21) | O:315 | 56(6) replaced (Commission assesses codes covering 53 and 55) | reliance on codes under 55(2) |
| 1(11), 1(30), 1(37) | O:243, 407, 580 | 17(2), 72(3), 97 | no change to reporting duty |
| 1(4) | O:152-163 | 3(14) amended; 3(14a) SME, 3(14b) SMC | SME/SMC for fines |

**Not amended:** Arts 3(49), 3(61), 16, 20, 26, 51, 52, 53, 55, 73, 101, 111(3), 113(b).
The brief's "Article 75(1a)" claim (arXiv paper) **is** in the deposited Omnibus (O:434).

Dates of application (provider of a NEW system placed on the market after the relevant date; no 111(2) grace):

| question | vintage | 2026-08-01 | 2026-08-02 | 2026-08-03 | 2027-12-01 | 2027-12-02 | 2028-08-01 | 2028-08-02 | 2028-08-03 |
|---|---|---|---|---|---|---|---|---|---|
| Art 73, Annex III system | enacted (113 general, A:2199) | no | yes | yes | yes | yes | yes | yes | yes |
| Art 73, Annex III system | amended | no | no | no | no | yes | yes | yes | yes |
| Art 73, Annex I §A system | enacted (113(c) "6(1) and corresponding obligations", 2 Aug 2027) | no | no | no | yes | yes | yes | yes | yes |
| Art 73, Annex I §A system | amended | no | no | no | no | no | no | yes | yes |
| Art 55, model placed on/after 2 Aug 2025 | both | yes | yes | yes | yes | yes | yes | yes | yes |
| Art 55, model placed before 2 Aug 2025 | both (111(3)) | no | no | no | yes | yes | yes | yes | yes |
| Art 101 fine available | both (113(b) excepts 101 -> general date) | no | yes | yes | yes | yes | yes | yes | yes |

Ambiguity F4 (as amended): Art 73 is in Chapter IX, so by the letter it stays on the general date 2 Aug 2026; the amended 113(c) delays only Chapter III Sections 1-3.
Reading A (letter): Art 73 applies from 2 Aug 2026. Reading B (systemic): "high-risk AI system" exists only by Art 6 (Chapter III Section 1), so Art 73 has no subject before 2 Dec 2027 / 2 Aug 2028.
They converge in effect: under reading A, every system placed on the market before the Chapter III date gets the amended 111(2) grace (O:606), so no new-system Art 73 duty arises before 2 Dec 2027 / 2 Aug 2028 either. I assert reading B.

Recipient by vintage (incident on 2028-08-03, new Annex III system, incident in Member State X):

| provider | enacted | amended |
|---|---|---|
| Annex III system, not GPAI-based | MSA of X | MSA of X |
| Annex III system built on own GPAI model (same provider) | MSA of X | AI Office (75(1a)) |
| same, but Annex III point 2 (critical infrastructure) | MSA of X | MSA of X (exception (ii)) |
| system integrated into a VLOP/VLOSE | MSA of X | AI Office |
| GPAI-SR under 55(1)(c) | AI Office (+ NCAs as appropriate) | unchanged |

## (d) Penalties

| failure | vintage | provision | ceiling |
|---|---|---|---|
| Art 73 report, MSA-supervised provider | enacted | 99(1) Member State rules; 73 is NOT listed in 99(4) (A:2012-2026; Art 16 list A:872-896 does not include 73) | **no ceiling stated in the Regulation** |
| same | amended | 99(1) replaced (O:591), still no 73 entry | **no ceiling stated** |
| Art 73 report, AI-Office-supervised provider (75(1)) | amended | 75c(4)(a) (O:502) -> 99(4) | max(EUR 15 000 000, 3% turnover); SME: min (99(6)); SMC: min (99(6a)) |
| same | enacted | 75c does not exist; 99(1) | no ceiling stated |
| Art 55 (and 52) | both | 101(1)(a) (A:2079-2081) | max(EUR 15 000 000, 3% turnover); no SME/SMC rule; only from 2 Aug 2026 |

Worked figures:
- 101, turnover EUR 1 000 000 000 -> EUR 30 000 000.
- 101, turnover EUR 100 000 000 -> EUR 15 000 000.
- 101, turnover EUR 500 000 000 -> EUR 15 000 000 (3% = 15M exactly).
- 101, SME turnover EUR 10 000 000 -> EUR 15 000 000 (no SME lower-of).
- 101, incident failure on 2026-08-01 -> no Commission fine available (Art 101 not applicable).
- 75c/99(4), non-SME turnover EUR 1 000 000 000 -> EUR 30 000 000; turnover 100M -> 15M.
- 75c/99(4), SME turnover EUR 40 000 000 -> EUR 1 200 000.
- 75c/99(4), SMC turnover EUR 200 000 000 -> EUR 6 000 000.
- Art 73 enacted / MSA-supervised -> no ceiling (a NOTHING-type answer, not 0, not 15M).
- Rejected reading: 16(c) -> 17(1)(i) (QMS must include reporting *procedures*) -> 99(4)(a). That fines a missing procedure, not a missing report (F5).
- Art 99(5) (EUR 7.5M / 1%) is for incorrect information "in reply to a request"; not a failure to report.

## (e) Deployers

- Art 26(5) (A:1023): deployer identifying a serious incident must immediately inform first the provider, then importer/distributor and the MSAs; if it cannot reach the provider, Art 73 applies to the deployer mutatis mutandis. Bears on the provider only via the 73(2)-(4) anchor (F2).
- Art 20(2) (A:951): provider aware of an Art 79(1) risk must immediately investigate and inform the competent MSAs: "immediately", **no period stated**; it is not the Art 73 report.

## Ambiguity register

- F1 day counting: calendar days, awareness = day 0; Reg 1182/71 weekend roll not applied (not deposited).
- F2 anchor: earlier of provider's and deployer's awareness (reading A) vs provider's own (reading B). I take A.
- F3 death + critical infrastructure: 2 days (both paragraphs bind) vs 10 (death is lex specialis). I take 2.
- F4 as-amended Art 73 date: B (2 Dec 2027 / 2 Aug 2028); A converges via 111(2).
- F5 Art 73 penalty: no ceiling (reading 1) vs 99(4) via 16(c)/17(1)(i) (reading 2). I take 1.
- F6 111(3): duty from 2 Aug 2027 (grace) vs duty from 2 Aug 2025 with steps due 2027. I take the former.
- F7 52(2) pending arguments: classified until Commission accepts. I take classified.
- F8 75c(4) refers to "Article 99(3) to (7)": I read it as including the inserted 99(6a) (SMC lower-of).
