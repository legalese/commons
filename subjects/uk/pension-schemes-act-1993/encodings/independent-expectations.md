# Independent expectations — PSA 1993 early leavers and cash equivalent transfers

Written from BRIEF.md and the Act (revised text, point in time 31 July 2026) only, before any `.l4` file was opened.

## Readings adopted

- **R1 (qualifying service, brief).** Earlier counting days are subtracted from the start of the latest period ("adjusted start"). A period of N months is met if the end of service is on or after the last day of the N months beginning with the adjusted start. 30 days is met if end >= adjusted start + 29.
- **R2 (no corresponding date).** Where the corresponding date does not exist (e.g. 29 February in a common year), I follow the corresponding-date rule as applied by the courts (Dodds v Walker): a period of N months "beginning with" day X is the period of N months *after* day X-1, ending on the corresponding date of X-1, or the last day of the month if none. So 24 months beginning 29 Feb 2020 end on **28 Feb 2022** (not 27 Feb, which a "clamp then subtract one" calculation gives). Flagged as ambiguity A1; I test it once.
- **R3 (s 95(1A)(b)).** "the date that falls one year before the member attains normal pension age": the corresponding date one year earlier; a 29 February NPA date gives 28 February of the previous year (A2).
- **R4 (s 95(1A)(a), s 99(2)).** "within the period of 3/6 months beginning with D": on or before the day before the corresponding date.
- **R5 (s 99(3)).** The period of 3 months after the conclusion ends on the corresponding date. The extension applies where the s 99(2) deadline is earlier than that end; the result is then the end of the 3 months. Where the 3-month end is the day after the s 99(2) last day, the extension still applies (the s 99(2) "date before which" equals that day, which is earlier than the *end* of that day) — A3.
- **R6 (s 99(7)).** "within six months of the date mentioned in (2)(a) or (b)" is read as the s 99(2) six-month period (R4). It refers to the dates in (2)(a)/(b) only, so a s 99(3) extension does **not** prevent the duty to notify where the transfer is carried out after six months (A4).
- **R7.** "terminated before normal pension age": termination on the day the member attains NPA is not before NPA.
- **R8.** s 98(1) loss applies only to rights under s 94(1) (non-money-purchase); money purchase rights (s 94(2)) have no s 95(1A) deadline and are not lost under s 98(1).

## Goal 1 — early leavers (ss 71, 101AA, 101AB)

Defaults unless stated: NPA 65, reaching NPA on 1 Jan 2050, no earlier counting days, not all money purchase, relevant service not before s 36 PA 2014, no personal-pension transfer-in.

### Two years' qualifying service — s 71(1)(a), (7): "at least 2 years' qualifying service"
| # | Service | Earlier days | Expected SSB |
|---|---|---|---|
| L1 | 1 Jan 2020 – 31 Dec 2021 | 0 | yes (exactly 2 years) |
| L2 | 1 Jan 2020 – 30 Dec 2021 | 0 | no |
| L3 | 1 Jan 2025 – 6 Mar 2026 | 300 (adj start 7 Mar 2024) | yes |
| L4 | 1 Jan 2025 – 5 Mar 2026 | 300 | no |
| L5 | 1 Jun 2024 – 27 Apr 2025 | 400 (adj 28 Apr 2023) | yes |
| L6 | 1 Jun 2024 – 26 Apr 2025 | 400 | no |
| L7 | 29 Feb 2020 – 28 Feb 2022 | 0 | yes |
| L8 | 29 Feb 2020 – 27 Feb 2022 | 0 | **no** under R2 (A1; clamp-minus-one gives yes) |
| L9 | 1 Mar 2020 – 28 Feb 2022 | 0 | yes (24 months beginning 1 Mar 2020 end 28 Feb 2022) |
| L10 | 1 Mar 2020 – 27 Feb 2022 | 0 | no |

### 30 days, money purchase — s 71(1)(aa), (10), (11)
"at least 30 days' qualifying service and ... all of it would necessarily be money purchase benefit"; (11) "does not apply ... if any period of relevant service began before" s 36 PA 2014 commencement.
| # | Facts | Expected SSB |
|---|---|---|
| L11 | 1 Mar 2026 – 30 Mar 2026, all MP | yes (30 days) |
| L12 | 1 Mar 2026 – 29 Mar 2026, all MP | no |
| L13 | 1 Mar 2026 – 30 Mar 2026, not all MP | no |
| L14 | 1 Mar 2026 – 30 Mar 2026, all MP, relevant service before s 36 | no (s 71(11)) |
| L15 | 20 Mar 2026 – 31 Mar 2026, 18 earlier days, all MP | yes (adj 2 Mar; +29 = 31 Mar) |
| L16 | same, 17 earlier days | no |
| L17 | 1 Jan 2020 – 31 Dec 2021, all MP, relevant service before s 36 | yes (2-year route unaffected by (11)) |

### Personal pension transfer-in — s 71(1)(b)
| L18 | 1 Mar 2026 – 7 Mar 2026, transfer in from personal pension | yes |
| L19 | same without the transfer | no |

### Before normal pension age — s 71(1) "terminated before normal pension age"; s 101AA(1)(a)
| L20 | 1 Jan 2020 – 1 Jan 2025, reaches NPA 1 Jan 2025 | no SSB; no cash transfer sum/refund right |
| L21 | same, reaches NPA 2 Jan 2025 | SSB yes |
| L22 | 1 Jan 2020 – 2 Jan 2025, NPA reached 1 Jan 2025 | no SSB, no refund right |

### Three-month condition; cash transfer sum / refund right — s 101AA(1)-(2), 101AB(1)
"the three month condition is satisfied, but ... he does not have relevant accrued rights"; "amounts to at least three months".
| L23 | 1 Jan 2026 – 31 Mar 2026 | no SSB; refund right yes |
| L24 | 1 Jan 2026 – 30 Mar 2026 | no SSB; refund right no |
| L25 | 1 Mar 2026 – 31 Mar 2026, 59 earlier days (adj 1 Jan 2026) | refund right yes |
| L26 | same, 58 earlier days | refund right no |
| L27 | 1 Jan 2020 – 31 Dec 2021 (SSB) | refund right no (has relevant accrued rights) |
| L28 | 1 Mar 2026 – 30 Mar 2026 all MP (SSB under aa) | refund right no |
| L29 | 1 Jan 2026 – 31 Mar 2026 all MP, relevant service before s 36 | SSB no; refund right yes |
| L30 | 1 Jan 2026 – 31 Mar 2026 with personal pension transfer-in | SSB yes; refund right no |

### Refund amount — s 101AB(4)
"the aggregate of (a) employee contributions ... (b) ... employee contributions to that other scheme, so far as they (i) relate to the transfer payment, and (ii) do not, in aggregate, exceed the amount of the transfer payment."
| L31 | ee 5000, transfer-related 3000, transfer payment 2000 | 7000 |
| L32 | ee 5000, TR 1500, TP 2000 | 6500 |
| L33 | ee 5000, TR 2000, TP 2000 | 7000 |
| L34 | ee 1234.56, no transfer (0, 0) | 1234.56 |
| L35 | ee 0, TR 800, TP 500 | 500 |

### Latest age for SSB — s 71(3)
"no greater than (a) the age of 65, or (b) if ... normal pension age is greater than 65, normal pension age."
| L36 | NPA 60 | 65 |
| L37 | NPA 65 | 65 |
| L38 | NPA 67 | 67 |
| L39 | NPA 68 (SSB case) | 68 |

## Goal 2 — cash equivalent transfers (ss 94, 95(1A), 98, 99)

### Application deadline — s 95(1A)
"(a) within the period of 3 months beginning with the guarantee date ..., and (b) if ... not flexible benefits, by no later than the date that falls one year before the member attains normal pension age."
| # | Facts | Last day to apply |
|---|---|---|
| T1 | GD 15 Jan 2026, flexible, NPA reached 1 Jan 2050 | 14 Apr 2026 |
| T2 | GD 15 Jan 2026, non-flexible, NPA 1 Jan 2050 | 14 Apr 2026 |
| T3 | GD 15 Jan 2026, non-flexible, NPA reached 1 Mar 2027 | 1 Mar 2026 (one year before) |
| T4 | GD 15 Jan 2026, flexible, NPA 1 Mar 2027 | 14 Apr 2026 |
| T5 | GD 15 Jan 2026, non-flexible, NPA 14 Apr 2027 | 14 Apr 2026 (both the same) |
| T6 | GD 15 Jan 2026, non-flexible, NPA 13 Apr 2027 | 13 Apr 2026 |
| T7 | GD 15 Jan 2026, non-flexible, NPA 29 Feb 2028 | 14 Apr 2026 (one year before = 28 Feb 2027, later) |
| T8 | GD 15 Jan 2027, non-flexible, NPA 29 Feb 2028 | 28 Feb 2027 (R3, A2) |

### Loss of right — s 98(1)
"loses that right if no application ... is made within the period required by section 95(1A)".
| T9 | T1 facts, applied 14 Apr 2026 | not lost |
| T10 | T1 facts, applied 15 Apr 2026 | lost |
| T11 | T3 facts, applied 1 Mar 2026 | not lost |
| T12 | T3 facts, applied 2 Mar 2026 | lost |
| T13 | money purchase, any application date (e.g. a year later) | not lost (R8) |
| T14 | T1 facts, applied on GD | not lost |

### Trustees' deadline — s 99(2)
"(a) ... other than money purchase benefits, within 6 months beginning with the guarantee date ...; (b) ... money purchase ... within 6 months beginning with the date of the application".
| T15 | DB, GD 15 Jan 2026, applied 1 Mar 2026 | 14 Jul 2026 |
| T16 | MP, applied 10 Mar 2026 | 9 Sep 2026 |
| T17 | MP, applied 1 Jan 2026 | 30 Jun 2026 |
| T18 | DB, GD 1 Mar 2026 | 31 Aug 2026 |

### Forfeiture extension — s 99(3)
"... earlier than the end of the period of 3 months after the conclusion ... they must instead do so before the end of that period of 3 months."
| T19 | DB GD 15 Jan 2026; proceedings concluded 10 Jun 2026 | 10 Sep 2026 |
| T20 | same, concluded 1 Apr 2026 | 14 Jul 2026 (3-month end 1 Jul is earlier; no extension) |
| T21 | same, concluded 14 Apr 2026 | 14 Jul 2026 |
| T22 | same, concluded 15 Apr 2026 | 15 Jul 2026 (R5, A3) |
| T23 | MP applied 10 Mar 2026, concluded 30 Nov 2026 | 28 Feb 2027 (no 30 Feb: last day of Feb) |
| T24 | MP applied 10 Mar 2026, concluded 1 Dec 2026 | 1 Mar 2027 |
| T25 | forfeiture proceedings but no forfeiture apprehended (condition (b) false) | 14 Jul 2026 for T19 facts |

### Notify the Regulator — s 99(7)
"have not done what is needed ... within six months of the date mentioned in paragraph (a) or (b) of subsection (2)".
| T26 | DB GD 15 Jan 2026, carried out 14 Jul 2026 | no |
| T27 | same, carried out 15 Jul 2026 | yes |
| T28 | MP applied 10 Mar 2026, carried out 9 Sep 2026 | no |
| T29 | MP applied 10 Mar 2026, carried out 10 Sep 2026 | yes |
| T30 | T19 facts (extended to 10 Sep), carried out 1 Sep 2026 | yes (A4: s 99(7) looks only at the (2)(a)/(b) date) |
| T31 | T19 facts, carried out 10 Jul 2026 | no |

## Ambiguities
- **A1** 29 Feb starts / months with no corresponding date (L8, T23): Dodds v Walker last-day-of-month approach adopted.
- **A2** 29 Feb NPA date minus one year (T8): 28 Feb.
- **A3** s 99(3) boundary where 3-month end is exactly the day after the s 99(2) last day (T22).
- **A4** Whether a s 99(3) extension suspends s 99(7) notification (T30): text says no.
- **A5** Applications made before the guarantee date are outside the "period beginning with the guarantee date" on a literal reading; not tested, since in practice impossible.
- **A6** Ongoing (unconcluded) forfeiture proceedings: s 99(3) end date unknown — the deadline is not computable; an encoding should refuse rather than return the s 99(2) date. Tested only if the encoding's shape allows.
