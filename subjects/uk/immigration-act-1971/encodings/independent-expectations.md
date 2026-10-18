# Independent expectations: Immigration Act 1971 (ss 1-3ZA, 3C, 24, 24B, 28)

Written from BRIEF.md and the revised text (point in time 5 January 2026) only,
before any `.l4` file was opened. Each scenario gives inputs, the expected
answer, and the Act's words relied on.

## Readings adopted

- **R1 "within N months after X" (s 28(1)(a))**: last day = the corresponding
  date N months later. If that month has no corresponding date (31st, 30th,
  29 Feb), the last day of that month (corresponding date rule, Dodds v Walker).
  So 31 Aug 2025 + 6 months = 28 Feb 2026; 29 Feb 2024 + 3 years = 28 Feb 2027.
- **R2 "within the period of N months beginning with X" (s 28(1A)(a))**: the
  period includes X, so it is the period of N months *after* the day before X:
  last day = (X − 1 day) + N months, clamped as in R1. 15 Jan 2025 + 6m → 14 Jul
  2025; 31 Aug 2025 → 28 Feb 2026; 1 Sep 2023 → 29 Feb 2024; 30 Nov 2023 + 3m
  → 29 Feb 2024. Alternative reading (corresponding date then minus one day,
  31 Aug → 27 Feb) rejected: it would make the 6-month period beginning with
  31 Aug shorter than the one beginning with 29 Aug. Flagged as ambiguity A1.
- **R3 s 28(1)(a) extended route**: on or before both (offence + 3 years) and
  (certified date + 2 months), i.e. the earlier of the two; overall last day is
  the later of the six-month day and that extended day (brief).
- **R4 s 28(1A)(a)(ii)**: the three-month period counts only "if that period
  expires after the end of" the six-month period; either way the overall last
  day is the later of the two ends (brief).
- **R5 s 3C**: applies if leave is limited, application date ≤ expiry day, and
  the application is not decided on or before expiry day. On a day d after
  expiry the leave is extended if (d is before the decision day, i.e. still
  undecided) or (d is on or before the last day of appeal/review rights) or an
  appeal/review is pending; and the applicant has not left on or before d
  (it "lapse[s] if the applicant leaves" — from the day of departure).
  On or before the expiry day the leave is not *extended* (it is original leave).
- **R6 decision day without appeal rights**: on the decision day the
  application is decided, so (2)(a) is not met; with no appeal/review right the
  leave is not extended on that day. Ambiguity A2 (an encoding might treat the
  decision day as still covered).
- **R7 transitional readings**: s 24(G1) — offence committed before Sch 22
  para 24(2) Sentencing Act 2020 commencement → E&W summary max is six months;
  on/after → the general limit (an input, e.g. 12 months). s 24B(4) — offence
  committed before s 281(5) CJA 2003 commencement → E&W 6 months instead of
  51 weeks. (Commencement on the offence date counts as "not before".)
- **R8 offences outside s 24(3)** (C1, s 24(1)(b), s 24B): no extended limit
  under s 28(1); an encoding should say not applicable (NOTHING / FALSE /
  REFUSE), not compute a date.

## Goal 1: right of abode and need for leave

| # | Inputs | Expected | Act |
|---|---|---|---|
| 1 | British citizen | right of abode: yes | s 2(1)(a) "he is a British citizen" |
| 2 | Commonwealth citizen, pre-1983 right, still Commonwealth citizen | RoA: yes | s 2(1)(b)(i)-(ii) |
| 3 | Commonwealth citizen with pre-1983 right, ceased to be Commonwealth citizen (then regained) | RoA: no | s 2(1)(b)(ii) "has not ceased ... in the meanwhile" |
| 4 | Commonwealth citizen without pre-1983 right | RoA: no | s 2(1)(b)(i) |
| 5 | Irish citizen only | RoA: no | s 2(1) — Irish citizenship is not a route |
| 6 | Foreign national | RoA: no | s 2(1) |
| 7 | British citizen | needs leave: no | s 1(1), s 3(1) "where a person is not a British citizen" |
| 8 | Pre-1983 Commonwealth citizen with RoA | needs leave: no | s 2(2) treated as British citizen; s 1(1) |
| 9 | Irish citizen, none of 3ZA(2)-(4) | needs leave: no | s 3ZA(1) |
| 10 | Irish citizen subject to deportation order (3ZA(2)) | needs leave: yes | s 3ZA(1), (2) |
| 11 | Irish citizen, exclusion directions issued, notice given, not withdrawn | yes | s 3ZA(3)(a)-(c) |
| 12 | Irish citizen, directions issued but notice NOT given | no | s 3ZA(3)(b) |
| 13 | Irish citizen, directions issued, notice given, withdrawn | no | s 3ZA(3)(c) |
| 14 | Irish citizen, excluded person under s 8B | yes | s 3ZA(4) |
| 15 | Irish citizen within (2), arriving on local journey from CTA | yes | s 3ZA(5) "section 1(3) does not permit" |
| 16 | Irish citizen not within (2)-(4), local journey | no | s 3ZA(1), s 1(3) |
| 17 | Foreign national, local journey from CTA | no | s 1(3) "nor shall a person require leave to enter ... on so arriving" |
| 18 | Foreign national, not a local journey | yes | s 3(1)(a) |
| 19 | Commonwealth citizen without RoA, not local journey | yes | s 3(1)(a) |
| 20 | Irish citizen who is also British citizen, subject to deportation order facts | no (RoA) | s 3(1) |

## Goal 2: s 3C continuation of leave

Base: limited leave expires 31 Mar 2025; application 20 Mar 2025;
decision 10 Jun 2025; last day of in-country appeal/review rights 24 Jun 2025;
no departure; no pending appeal.

| # | Variation | Day | Expected | Act |
|---|---|---|---|---|
| 21 | base | 15 Apr 2025 | extended | s 3C(1), (2)(a) undecided |
| 22 | base | 31 Mar 2025 (expiry day) | not extended (original leave) | s 3C(1)(c) "the leave expires" |
| 23 | base | 1 Apr 2025 | extended | s 3C(2)(a) |
| 24 | base | 10 Jun 2025 (decision day) | extended (appeal could be brought) | s 3C(2)(b)/(d)(i) |
| 25 | base | 24 Jun 2025 (last day of rights) | extended | s 3C(2)(b) |
| 26 | base | 25 Jun 2025 | not extended | s 3C(2) none applies |
| 27 | application made 31 Mar 2025 (expiry day) | 15 Apr 2025 | extended | s 3C(1)(b) "before the leave expires" = on/before last day |
| 28 | application made 1 Apr 2025 | 15 Apr 2025 | not extended | s 3C(1)(b) |
| 29 | decision 25 Mar 2025 (before expiry) with rights to 8 Apr | 2 Apr 2025 | not extended | s 3C(1)(c) "expires without the application ... having been decided" |
| 30 | decision 31 Mar 2025 (expiry day), rights to 14 Apr | 5 Apr 2025 | not extended | s 3C(1)(c) |
| 31 | departure 1 May 2025 | 1 May 2025 | not extended | s 3C(3) lapses if the applicant leaves |
| 32 | departure 1 May 2025 | 30 Apr 2025 | extended | s 3C(2)(a) |
| 33 | departure 1 May 2025 | 15 May 2025 | not extended | s 3C(3) |
| 34 | decision 10 Jun, no appeal/review rights (last day of rights none / before decision) | 10 Jun 2025 | not extended (R6) | s 3C(2)(a) "neither decided" |
| 35 | decision 10 Jun, no rights | 9 Jun 2025 | extended | s 3C(2)(a) |
| 36 | undecided (no decision yet) | 1 Jan 2026 | extended | s 3C(2)(a) |
| 37 | departure after rights end (1 Jul) | 20 Jun 2025 | extended | s 3C(2)(b) |
| 38 | leave expires 29 Feb 2024; application 29 Feb 2024; undecided | 1 Mar 2024 | extended | s 3C(1)(b) |
| 39 | leave expires 29 Feb 2024; application 1 Mar 2024 | 2 Mar 2024 | not extended | s 3C(1)(b) |

## Goal 3: offences

### Which offence

| # | Facts | Expected | Act |
|---|---|---|---|
| 40 | knowingly enters in breach of a deportation order | A1 committed | s 24(A1) |
| 41 | enters in breach of deportation order, not knowingly | A1 not committed | s 24(A1) "knowingly" |
| 42 | requires leave, knowingly enters without leave | B1 committed | s 24(B1) |
| 43 | Irish citizen outside 3ZA(2)-(4), knowingly enters without leave | B1 not committed (does not require leave) | s 24(B1)(a), s 3ZA(1) |
| 44 | only limited leave, knowingly remains beyond | C1 committed | s 24(C1) |
| 45 | limited leave, remains beyond, does not know | C1 not committed | s 24(C1)(b); s 24(1A) "first knows" |
| 46 | B1 + journey by water from France + dangerous act in relevant period | E1A committed | s 24(E1A) |
| 47 | B1 + water journey from Spain + dangerous act | E1A not committed | s 24(E1A)(b) |
| 48 | B1 + water journey from Belgium, no dangerous act | E1A not committed | s 24(E1A)(c) |
| 49 | not British, limited leave, knowingly fails to observe condition | s 24(1)(b) committed | s 24(1)(b) |
| 50 | requires leave, works while disqualified, knows | s 24B committed | s 24B(1) |
| 51 | works while disqualified, neither knows nor has reasonable cause | not committed | s 24B(1)(b) |
| 52 | works while disqualified, reasonable cause to believe | committed | s 24B(1)(b) |
| 53 | British citizen working | not committed (not subject to immigration control) | s 24B(8) |

### Maximum imprisonment

General limit input 12 months; Sch 22 para 24(2) SA 2020 treated as in
force before the offence unless stated; s 281(5) CJA 2003 not in force before
the offence unless stated.

| # | Offence | Mode / jurisdiction | Expected | Act |
|---|---|---|---|---|
| 54 | A1 | indictment | 5 years | s 24(F1)(d)(i) |
| 55 | B1 | indictment | 4 years | (F1)(d)(ii) |
| 56 | C1 | indictment | 4 years | (F1)(d)(ii) "(B1) to (E1)" |
| 57 | D1 | indictment | 4 years | (F1)(d)(ii) |
| 58 | E1 | indictment | 4 years | (F1)(d)(ii) |
| 59 | E1A with A1 | indictment | 6 years | (F1)(d)(iii) |
| 60 | E1A with B1 / D1 / E1 | indictment | 5 years | (F1)(d)(iv) |
| 61 | A1 | summary E&W, after commencement | general limit (12 months) | (F1)(a) |
| 62 | A1 | summary E&W, offence before commencement | 6 months | (G1) |
| 63 | B1 | summary Scotland | 12 months | (F1)(b) |
| 64 | B1 | summary NI | 6 months | (F1)(c) |
| 65 | E1A | summary E&W, after commencement | general limit | (F1)(a) "any of subsections (A1) to (E1A)" |
| 66 | s 24(1)(b) | summary, every jurisdiction | 6 months | s 24(1) |
| 67 | s 24(1)(b), (1)(c) | indictment | none (summary only) | s 24(1) "punishable on summary conviction" |
| 68 | s 24B | summary E&W, s 281(5) in force | 51 weeks | s 24B(3)(a) |
| 69 | s 24B | summary E&W, offence before s 281(5) | 6 months | s 24B(4) |
| 70 | s 24B | summary Scotland / NI | 6 months | s 24B(3)(b) |
| 71 | s 24B | indictment | none | s 24B(3) "liable on summary conviction" |

### s 28(1)(a) last day (England and Wales), extended limit offences

| # | Offence date | Certified evidence date | Expected last day | Why |
|---|---|---|---|---|
| 72 | 15 Jan 2024 | 1 Mar 2024 | 15 Jul 2024 | 6m route later than cert+2m (1 May 2024) |
| 73 | 15 Jan 2024 | 10 Jun 2025 | 10 Aug 2025 | cert+2m < 3y end |
| 74 | 15 Jan 2024 | 1 Dec 2026 | 15 Jan 2027 | capped at 3 years (cert+2m = 1 Feb 2027) |
| 75 | 15 Jan 2024 | 15 Nov 2026 | 15 Jan 2027 | both equal |
| 76 | 15 Jan 2024 | 14 Nov 2026 | 14 Jan 2027 | cert+2m one day short of 3y |
| 77 | 15 Jan 2024 | 20 Dec 2026 | 15 Jan 2027 | 3y cap |
| 78 | 31 Aug 2025 | 31 Dec 2025 | 28 Feb 2026 | both routes give 28 Feb (R1 clamp) |
| 79 | 31 Aug 2023 | 1 Sep 2023 | 29 Feb 2024 | 6m route, leap clamp |
| 80 | 29 Feb 2024 | 1 Jan 2027 | 28 Feb 2027 | 3y cap clamped; cert+2m = 1 Mar 2027 |
| 81 | 29 Feb 2024 | 31 Dec 2026 | 28 Feb 2027 | cert+2m clamped = 28 Feb 2027 |
| 82 | 30 Jun 2025 | 31 Oct 2025 | 31 Dec 2025 | ext (31 Dec) later than 6m (30 Dec) |
| 83 | 1 Jun 2023 | 31 Dec 2023 | 29 Feb 2024 | cert+2m clamped into leap Feb |
| 84 | C1 / s 24(1)(b) / s 24B | any | no extended limit | s 24(3) lists A1, B1, D1, E1, E1A, (1)(c) only |
| 85 | s 24(1)(c) | 15 Jan 2024 / 10 Jun 2025 | 10 Aug 2025 | s 24(3) includes (1)(c) |

### s 28(1A)(a) last day (England and Wales)

| # | Offence date | First arrest | Expected | Why |
|---|---|---|---|---|
| 86 | 15 Jan 2025 | 1 Mar 2025 | 14 Jul 2025 | 6m period beginning with 15 Jan ends 14 Jul; 3m ends 31 May |
| 87 | 15 Jan 2025 | 1 Jun 2025 | 31 Aug 2025 | 3m period ends later |
| 88 | 15 Jan 2025 | 15 Apr 2025 | 14 Jul 2025 | equal ends |
| 89 | 15 Jan 2025 | 16 Apr 2025 | 15 Jul 2025 | 3m one day later |
| 90 | 31 Aug 2025 | 1 Sep 2025 | 28 Feb 2026 | R2 |
| 91 | 1 Sep 2023 | 2 Sep 2023 | 29 Feb 2024 | R2 leap |
| 92 | 1 Jul 2023 | 30 Nov 2023 | 29 Feb 2024 | 3m beginning 30 Nov → 29 Feb (leap) |
| 93 | 1 Jul 2024 | 30 Nov 2024 | 28 Feb 2025 | non-leap |
| 94 | 1 Mar 2024 | 1 Mar 2024 | 31 Aug 2024 | 6m |

## Ambiguities

- A1: month arithmetic for "beginning with" at month ends (R2).
- A2: decision day with no appeal/review right (R6).
- A3: certified evidence date after the three-year end — formula R3 still
  yields the three-year day; whether laying before the certified date is
  "not more than two months after" it is not tested.
- A4: whether s 281(5) CJA 2003 is actually in force (it has never been
  commenced as of writing, so the 6-month reading currently applies); treated
  as an input.
- A5: s 3C on the expiry day itself — original leave, not "extended"; an
  encoding may answer either "leave continues" or "not extended by s 3C".
