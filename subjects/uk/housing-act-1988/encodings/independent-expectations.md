# Independent expectations: Housing Act 1988 ss 8, 21, 27-28

Written from BRIEF.md and the source text (ss 8, 21, 27, 28) only, before reading any `.l4` file.

## Date readings (from the brief)

- "N months from / after" date D: the same day number N months later; if that month has no such day, its last day.
- "two weeks from the date of the service": service + 14 days.
- "within the period of N months beginning with" day X: last permitted day is the day before the corresponding date N months later; if the later month has no corresponding date, the last day of that month.
- s 21(4B): the notice must be given after the last day of the four-month period beginning with the start day.
- s 21(4D)/(4E): proceedings may be begun on or before the last day of the six (four) month period.

## Readings and ambiguities

1. **s 8(4) in the pre-2025 version.** The merged text reads "Ground 14 ~~either or both of Grounds 7A and 14~~ (whether ~~with or~~ without other grounds or with any ground other than Ground 7A)". Taking the pre-2025 words: (4) applies to Ground 14 when 7A is not specified. If 7A is specified, (3A) governs (and, even if (4) were also read to apply, (3A) is always the later date). So any notice with 7A: periodic → the notice-to-quit date; fixed term → one month after service.
2. **(4A) "with any ground other than Ground 7A or 14"**: a (4A) ground together with Ground 14 is outside (4A); (4) then gives the date of service. A (4A) ground with a non-(4A) ground such as 8 is inside (4A).
3. **(4A)(b)** applies only to a periodic tenancy; the earliest date is the later of (a) and (b).
4. **(3A)(a)** periodic: the notice-to-quit date alone (no two-month floor).
5. **Grounds 3, 4, 8, 10-13, 15, 17** alone (no 7A, 14, or (4A) ground): (4B), service + 14.
6. **s 8(3)(c)** "not later than twelve months from the date of service": the latest day is service + 12 months (inclusive).
7. **Ground 7A window** is a date range: service on the day of conviction counts; service before the triggering day is not "within the period".
8. **s 21(1)(b)** "not less than two months' notice" (fixed term): the date specified must be on or after given + 2 months. For periodic, s 21(4)(a) the same, and (4)(b) not earlier than the notice-to-quit date. In England (4ZA) the date need not be the last day of a period.
9. **s 21(4E)(b)** "requires the date specified to be more than two months after the date the notice was given": the notice-to-quit date is strictly later than given + 2 months. Then (4E) displaces (4D) ("Subject to subsection (4E)"); last day = end of four months beginning with the date specified.
10. **s 27(1)/(2) "after 9th June 1988"**: an act on 9 June 1988 is outside; 10 June 1988 inside.
11. **s 27(8)(b)** is available only where liability would otherwise arise "by virtue only of the doing of acts or the withdrawal or withholding of services" (s 27(2)(b)), not for deprivation (s 27(1)) or an attempt (s 27(2)(a)).
12. **s 27(2)** requires that "as a result, the residential occupier gives up his occupation"; without that, no liability under (2).
13. **s 28** amount = value (a) − value (b); a s 27(7) reduction reduces it "to such amount as it thinks appropriate" (I expect the reduced amount, or the amount less the reduction, depending on the input shape; recorded per scenario below once I see the shape, with the expected arithmetic decided here: base 40,000, reduced by 10,000 → 30,000).
14. Amended (post-2025) s 8: the top-level goal gives NOTHING.

## A. Section 8 — earliest date (pre-2025)

| # | Grounds | Tenancy | Service | NTQ date | Expected earliest | Act |
|---|---|---|---|---|---|---|
| A1 | 7A | fixed | 15 Mar 2025 | – | 15 Apr 2025 | (3A)(b) "one month after the date on which the notice was served" |
| A2 | 7A | fixed | 31 Jan 2025 | – | 28 Feb 2025 | (3A)(b), month end |
| A3 | 7A | fixed | 31 Jan 2024 | – | 29 Feb 2024 | (3A)(b), leap year |
| A4 | 7A | periodic | 10 Mar 2025 | 9 Apr 2025 | 9 Apr 2025 | (3A)(a) notice to quit |
| A5 | 7A, 1 | periodic | 10 Mar 2025 | 9 Apr 2025 | 9 Apr 2025 | (3A) "whether with or without other grounds"; (4A) excluded by "other than Ground 7A or 14" |
| A6 | 7A, 14 | fixed | 10 Mar 2025 | – | 10 Apr 2025 | (3A)(b) |
| A7 | 7A, 8 | fixed | 30 Nov 2025 | – | 30 Dec 2025 | (3A)(b) |
| A8 | 14 | fixed | 10 Mar 2025 | – | 10 Mar 2025 | (4) "not earlier than the date of the service" |
| A9 | 14, 1 | periodic | 10 Mar 2025 | 30 Jun 2025 | 10 Mar 2025 | (4); (4A) excluded |
| A10 | 14, 8 | fixed | 10 Mar 2025 | – | 10 Mar 2025 | (4) |
| A11 | 1 | fixed | 10 Mar 2025 | – | 10 May 2025 | (4A)(a) two months |
| A12 | 2 | periodic | 10 Mar 2025 | 9 Apr 2025 | 10 May 2025 | (4A)(a) later than (b) |
| A13 | 16 | periodic | 10 Mar 2025 | 30 Jun 2025 | 30 Jun 2025 | (4A)(b) later than (a) |
| A14 | 9 | periodic | 10 Mar 2025 | 10 May 2025 | 10 May 2025 | equal |
| A15 | 5 | fixed | 31 Dec 2025 | – | 28 Feb 2026 | (4A)(a) month end |
| A16 | 6 | fixed | 31 Dec 2023 | – | 29 Feb 2024 | leap year |
| A17 | 7 | fixed | 30 Nov 2023 | – | 30 Jan 2024 | |
| A18 | 1, 8 | fixed | 10 Mar 2025 | – | 10 May 2025 | (4A) "with any ground other than Ground 7A or 14" |
| A19 | 8 | fixed | 10 Mar 2025 | – | 24 Mar 2025 | (4B) two weeks |
| A20 | 8, 10, 11 | periodic | 20 Feb 2024 | 20 Mar 2024 | 5 Mar 2024 | (4B); NTQ irrelevant |
| A21 | 12 | fixed | 25 Dec 2025 | – | 8 Jan 2026 | (4B) across year end |
| A22 | 3 | fixed | 10 Mar 2025 | – | 24 Mar 2025 | (4B) — 3 not a (4A) ground |
| A23 | 31 Aug 2025, ground 1 | fixed | 31 Aug 2025 | – | 31 Oct 2025 | (4A)(a) |

## B. Section 8 — latest date (12 months from service)

| # | Service | Expected |
|---|---|---|
| B1 | 15 Mar 2025 | 15 Mar 2026 |
| B2 | 29 Feb 2024 | 28 Feb 2025 |
| B3 | 31 Dec 2025 | 31 Dec 2026 |
| B4 | 28 Feb 2023 | 28 Feb 2024 |

## C. Ground 7A service windows (s 8(4C)-(4F))

| # | Condition | Trigger (appeal?) | Served | Expected | Act |
|---|---|---|---|---|---|
| C1 | 1 | conviction 10 Mar 2025 | 9 Mar 2026 | TRUE | (4D)(a) 12 months beginning with the day of conviction |
| C2 | 1 | conviction 10 Mar 2025 | 10 Mar 2026 | FALSE | |
| C3 | 3 | conviction 10 Mar 2025 | 10 Mar 2025 | TRUE | day of conviction is in the period |
| C4 | 5 | conviction 10 Mar 2025 | 9 Mar 2025 | FALSE | before the period |
| C5 | 1 | conviction 29 Feb 2024 | 28 Feb 2025 | TRUE | no 29 Feb 2025 → last day 28 Feb 2025 |
| C6 | 1 | conviction 29 Feb 2024 | 1 Mar 2025 | FALSE | |
| C7 | 3 | conviction 28 Feb 2023 | 27 Feb 2024 | TRUE | |
| C8 | 3 | conviction 28 Feb 2023 | 28 Feb 2024 | FALSE | |
| C9 | 1 | conviction 10 Mar 2024, appeal determined 1 Jun 2025 | 31 May 2026 | TRUE | (4D)(b) |
| C10 | 1 | as C9 | 1 Jun 2026 | FALSE | |
| C11 | 2 | finding 1 Jun 2025 | 31 May 2026 | TRUE | (4E)(a) |
| C12 | 2 | finding 1 Jun 2025 | 1 Jun 2026 | FALSE | |
| C13 | 2 | finding 1 Jun 2024, appeal withdrawn 15 Jan 2025 | 14 Jan 2026 | TRUE | (4E)(b) |
| C14 | 4 | closure order 1 Jun 2025 | 31 Aug 2025 | TRUE | (4F)(a) 3 months |
| C15 | 4 | closure order 1 Jun 2025 | 1 Sep 2025 | FALSE | |
| C16 | 4 | closure order 30 Nov 2025 | 28 Feb 2026 | TRUE | no 30 Feb → last day 28 Feb |
| C17 | 4 | closure order 30 Nov 2025 | 1 Mar 2026 | FALSE | |
| C18 | 4 | closure order 1 Jan 2025, appeal 10 Apr 2025 | 9 Jul 2025 | TRUE | (4F)(b) |
| C19 | 4 | as C18 | 10 Jul 2025 | FALSE | |

## D. Section 21 (England)

### D1 four-month bar (4B)/(4C)

| # | Tenancy began | Replacement / original began | s 5(2) | Given | Expected permitted | Act |
|---|---|---|---|---|---|---|
| D1a | 1 Jan 2025 | no | no | 30 Apr 2025 | FALSE | within 4 months beginning 1 Jan |
| D1b | 1 Jan 2025 | no | no | 1 May 2025 | TRUE | |
| D1c | 31 Oct 2024 | no | no | 28 Feb 2025 | FALSE | 31 Feb absent → period ends 28 Feb |
| D1d | 31 Oct 2024 | no | no | 1 Mar 2025 | TRUE | |
| D1e | 1 Jun 2025 (replacement), original 1 Jan 2025 | yes | no | 1 Jul 2025 | TRUE | (4B)(b) uses original |
| D1f | 1 Apr 2025 (replacement), original 1 Mar 2025 | yes | no | 30 Jun 2025 | FALSE | 4 months from 1 Mar ends 30 Jun |
| D1g | 1 Jan 2025 | no | yes | 15 Jan 2025 | TRUE | (4C) |
| D1h | 1 Jan 2025 | no | no | 15 Jan 2025 | FALSE | |

### D2 notice length (s 21(1)(b), (4)(a)-(b), (4ZA))

| # | Periodic | Given | Specified | NTQ date | Expected | |
|---|---|---|---|---|---|---|
| D2a | fixed | 15 Jan 2025 | 15 Mar 2025 | – | TRUE | exactly two months |
| D2b | fixed | 15 Jan 2025 | 14 Mar 2025 | – | FALSE | |
| D2c | periodic | 31 Dec 2024 | 28 Feb 2025 | 28 Feb 2025 | TRUE | month end; (4ZA) no period-end requirement |
| D2d | periodic | 31 Dec 2024 | 27 Feb 2025 | 27 Feb 2025 | FALSE | |
| D2e | periodic | 15 Jan 2025 | 15 Mar 2025 | 30 Apr 2025 | FALSE | (4)(b) |
| D2f | periodic | 15 Jan 2025 | 30 Apr 2025 | 30 Apr 2025 | TRUE | |

### D3 last day for proceedings ((4D)/(4E))

| # | Periodic | Given | Specified | NTQ date | Expected last day |
|---|---|---|---|---|---|
| D3a | fixed | 15 Jan 2025 | 15 Mar 2025 | – | 14 Jul 2025 (4D) |
| D3b | periodic | 15 Jan 2025 | 15 Mar 2025 | 15 Mar 2025 | 14 Jul 2025 (4D), NTQ not more than two months |
| D3c | periodic | 15 Jan 2025 | 30 Apr 2025 | 30 Apr 2025 | 29 Aug 2025 (4E) |
| D3d | periodic | 31 Jan 2025 | 31 May 2025 | 31 May 2025 | 30 Sep 2025 (4E), no 31 Sep |
| D3e | fixed | 31 Aug 2025 | 31 Oct 2025 | – | 28 Feb 2026 (4D) six months from 31 Aug: 28 Feb (no 31 Feb) |
| D3f | fixed | 1 Mar 2025 | 1 May 2025 | – | 31 Aug 2025 |

## E. Sections 27-28

| # | Facts | Expected |
|---|---|---|
| E1 | deprivation 1 May 2024, no defences, values 250,000 / 210,000, no reduction | liable, 40,000 |
| E2 | deprivation on 9 Jun 1988 | not liable |
| E3 | deprivation on 10 Jun 1988 | liable |
| E4 | as E1 but reinstated before final disposal (6)(a) | not liable |
| E5 | as E1 but reinstated by court order at occupier's request (6)(b) | not liable |
| E6 | deprivation; defendant believed with reasonable cause occupier had ceased to reside (8)(a) | not liable |
| E7 | deprivation; defendant had reasonable grounds for the acts (8)(b) | liable — (8)(b) only for acts/services cases |
| E8 | harassment acts with knowledge, occupier gives up occupation; (8)(b) reasonable grounds | not liable |
| E9 | harassment acts with knowledge, occupier gives up; no defence | liable |
| E10 | harassment acts with knowledge, occupier does NOT give up | not liable |
| E11 | harassment acts but no knowledge/reasonable cause to believe | not liable |
| E12 | attempt to deprive, occupier gives up | liable |
| E13 | attempt, occupier does not give up | not liable |
| E14 | withholding services persistently, with knowledge, gives up | liable |
| E15 | E1 with s 27(7) reduction of 10,000 | 30,000 |
| E16 | not liable case: amount | 0 or NOTHING (shape-dependent) |
| E17 | belief (8)(a) held but without reasonable cause | liable |

## F. Top-level goal

| # | Facts | Expected |
|---|---|---|
| F1 | s 8 amended version | NOTHING |
| F2 | s 8 pre-2025 (as A11) | JUST result with 10 May 2025 |
