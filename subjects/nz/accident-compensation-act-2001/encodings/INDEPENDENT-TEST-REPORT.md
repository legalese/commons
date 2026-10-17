# Independent test report: Accident Compensation Act 2001 (NZ)

Tester: an independent pass. I wrote `independent-expectations.md` (E01–E262) from `../source/ACC2001.txt` before opening any `.l4` file. Only then did I read `acc-types`, `acc-cover`, `acc-claims-disputes`, `acc-entitlements`, `acc-levies-offences` and `acc-goal`. I did not read `acc-tests.l4`. No `acc-*.l4` file was edited.

Run with `L4=~/.local/bin/l4 ./check.sh`, then `l4 run tests-independent.l4 | grep -i warning`.

## Counts

| | |
|---|---|
| Assertions in `tests-independent.l4` | 315 |
| Satisfied | **308** |
| Failed | **7** |
| `#ASSERT REFUSED` | 0. None of my REFUSE expectations could be put to the encoding: every one of them is an *input* there, not a refusal (see below) |
| Other errors | 0 |
| Warnings | 0 |
| `acc-tests.l4` (encoder's own) | 215 satisfied, 0 failed |

The 315 assertions cover about 200 of the 262 expectations. The rest are listed under "Inexpressible".

**One fixture correction, declared.** The first run had an 8th failure: the goal case for E143 (expected weekly compensation $720). My shared earnings fixture set the minimum weekly earnings to $920 for a full-time earner. That makes the $900 52-week figure a cl 42 case, and the Act's answer becomes $736, not $720. That was my fixture error, not the encoding's. I changed the fixture's minimum to $500 so the scenario is the one E143 describes. **No expected value was changed.** The change is commented in the test file.

## Disagreements (7)

| # | Test | Scenario | Expected (Act) | Encoding | Who is right |
|---|---|---|---|---|---|
| 1 | E53 | NZ-resident suffers a treatment injury overseas on 30 June 2005 | no cover: s 22(3) gives overseas treatment-injury cover only for injury suffered **on or after 1 July 2005** | cover | **The Act.** `has cover` treats an overseas injury as covered if the person is resident. It does not encode s 22(3)–(4): the 1 July 2005 date, an equivalently qualified provider, and residence when the treatment was given. |
| 2 | E55 | Mental injury from a Schedule 3 act done overseas to a person not ordinarily resident at the time | no cover (s 21(2)(b)(ii)) | cover | **The Act.** The s 21 branch of `has cover` checks only the 1 April 2002 date. It ignores where the act was done and residence when it was done. `Injury facts` has no field for residence *at the time of the act*: the only residence field is residence when the injury was suffered, which s 21(3) declares irrelevant. |
| 3 | E66 | Work-related mental injury from an event overseas to a person not ordinarily resident when it occurred | no cover (s 21B(2)(c)(ii)) | cover | **The Act.** The s 21B branch checks only the 1 October 2008 date. `a qualifying event for work-related mental injury` exists but is not wired into `has cover`. The s 21B(2)(c) place and residence limb is not encoded anywhere. |
| 4 | E69 | NZ citizen, NZ is the permanent home, absent 5 months, present 150 days in the prior 12 months | ordinarily resident | not ordinarily resident | **The Act** (moderate confidence). The encoding requires more than 183 days' presence for anyone absent 1–6 months. Section 17(3) is a deeming rule: it says when a person *has* a permanent place of residence. It is not a precondition. Section 17(2) denies residence only past 6 months. Otherwise the s 17(1)(a) question (is NZ the permanent place of residence?) decides. On the encoding's reading, a recent returnee on a two-week holiday can lose cover under s 22. |
| 5 | E237 | Levy unpaid exactly 210 days after the due date | no 10% penalty yet | 1 penalty round | **The Act** (off-by-one; moderate confidence). Section 250(4) applies the penalty if the amount "has not been paid within 210 days after the due date". On day 210 it is still within the period, so the first penalty attaches from day 211. The encoding's `LESS THAN 210` should be `AT MOST 210`. The same boundary question arises at each 180-day step. |
| 6 | E90 (goal) | Employee at work, work-related mental injury (s 21B) from witnessing a moving-vehicle crash | work-related personal injury: s 35(1)(b) excludes work-related mental injury from "motor vehicle injury" | motor vehicle injury, so the Motor Vehicle Account pays | **The Act.** `a motor vehicle injury` looks only at the vehicle involvement, and `the class of` in the goal passes no harm. Section 35(1)(b) is not encoded. |
| 7 | E137 (goal) | Covered non-earner (not a potential earner) | weekly compensation after 5 weeks = 0: no cl 32 entitlement without being an earner | `NOTHING` | **The Act**, mildly. The goal returns `NOTHING` ("not computed") for every non-employee. For a self-employed person or shareholder-employee that is honest, because cls 37–40 are not encoded. For a non-earner the Act's answer is known and is nil. A `JUST 0` branch for `a non-earner` (and `a potential earner` under 6 months) would fix it. |

## Inexpressible expectations

The encoding has no input or function for the following, so I could not assert them. These are all still in `independent-expectations.md`.

- **Accident and personal injury:**
  - E20: a labour injury not in Schedule 3A (no variant for it).
  - E24, E25: scabies, malaria and arthropod-borne disease (s 25(2)(b)–(c)).
  - E31, E32: spectacles, hearing aids and wear and tear to prostheses (s 26(1)(e), (5)).
  - E29, E57: "other" mental injury. Only `none` stands in for it.
- **Cover:**
  - E56: s 21 residence at the time of the act, as distinct from at the injury.
  - E59: an offender incapable of forming intent.
  - E107, E108: clinical trials (s 32(4)–(6)) and transmitted infections (s 32(7)).
  - E115: non-physical stress (s 30(5)).
  - E117: s 30(2A) is a Corporation **"may decline"** discretion. The encoding makes "risk significantly greater" a *necessary condition*, which turns a discretion into a rule. I did not assert it because the Act gives no fixed answer, but this is a simplification.
- **Ordinary residence:** E73 and E78 are only expressible by pre-cooking the flags. E78 (a part day counts as a whole day) is left to the caller.
- **Accounts:**
  - E99: the foreign representative's employee, s 227(3)(b). The comment in `acc-cover` mentions it but the code does not handle it.
  - E100: cl 43 deemed earners go to the Earners' Account.
- **Dates:** E111–E113. There is no function for s 36 or s 38 dates.
- **Weekly compensation:**
  - E145, E146: cl 36 (non-permanent employees divide by 52, adjusted).
  - E149: the minimum weekly earnings figure. It is an input, not a REFUSE.
  - E167, E168: the s 114 one-month trigger and the liability-period day count. The caller supplies the days.
  - E169: the base rate. It is an input.
- **Lump sums:**
  - E173: the regulation amount between 10% and 80% is an input, not a REFUSE.
  - E177, E178: cl 55 transitional limits.
  - E175 (second limb): cl 62 payment to the estate.
  - E180: cl 57(2), mental injury under 16.
  - E181: cl 61(7), one reassessment per 12 months.
  - E182: cl 60(2), deduction of an earlier lump sum.
- **Fatal:**
  - E185: the per-spouse split. There is only a total.
  - E191: remarriage.
  - E196: cl 71(5).
  - E197: cl 75(3).
- **Disentitlements:**
  - E200–E202: the s 119(3)–(4) exceptions (mental injury from a covered injury, s 21 and s 21B mental injury, assisted dying). The `Disentitlement` variant cannot express them, so the encoding bars these claimants.
  - E206–E209: the s 122 conditions (maximum penalty of 2 years, imprisonment versus home detention versus community sentence, and the s 122(2) family bar) are folded into one variant.
  - E212: s 127(3), assessment abroad.
- **Levies:**
  - E231 (second limb): s 173 interest on refunds over $1,000.
  - E242: the s 224(2) five-year limit.
  - E244: the s 255(2) $20 floor.
  - E245: s 236.
  - E246: the s 171(2) 5% activity rule.
- **Proceedings:**
  - E257: s 318, gradual-process proceedings begun before 1993.
  - E258: the s 317 bar does not apply when the injury is not covered.
- **REFUSE items:** E149, E169, E173 and E260–E262 (minimum earnings, base rate, lump-sum regulations, levy rates, NZ superannuation age, cost amounts). The encoding treats every one of these as a caller-supplied input rather than refusing. That is a legitimate design, but it means the brief's REFUSE rule is only exercised once, by s 37 when there is neither a treatment date nor an incapacity date.

## What the encoding misses or simplifies (beyond the failures)

1. **The goal always passes `for a work injury: FALSE`** to `the class of injury`. Through the goal, a treatment injury from treatment for a work injury therefore goes to the Treatment Injury Account, contrary to s 228(3) and s 28(5). The lower-level function gets this right when called directly (E98 passes).
2. **The goal applies the cl 34 permanent-employee formula to every employee.** A non-permanent employee (cl 35–36: divide by 52, with adjustments) gets the permanent-employee figure (divide by weeks worked), which overstates part-year casual earnings.
3. **Cl 42 is applied without cl 42(7)** (the Corporation must be satisfied the claimant would have stayed a full-time earner) **and without cl 42(1)(c)**. The second is harmless because weekly compensation starts after week 1.
4. **The "1 month" in s 25(1)(d)–(e) is fixed at 30 days** (declared fork F1). A 31-day period inside a 31-day month is arguably "not exceeding 1 month". The encoder declared this choice, so I did not assert against it.
5. **Section 17 encoding** uses `months absent = 0` as the only path on which "NZ is their permanent home" matters, and ignores that input otherwise (see disagreement 4).
6. **Section 23** treats a non-resident's injury on "the ship or aircraft" as a single boolean. This is adequate, but the gangway and air-bridge timing in s 23(3) is left to the caller.
7. **Section 121 bars lump sums while in prison** (declared fork F7). This matches my reading that Part 3 is "not required" while imprisoned.
8. **Survivors' weekly compensation**: the cl 74 cap is applied as a flat cap on the total, rather than a pro rata reduction of each share. The total is right, but individual shares are not available.
9. **Cl 66(5)** takes a single "care ends" date. The caller must already have worked out the latest of the four events.

## Verdict

The arithmetic and the deadline functions are sound. All the date limits in Parts 3, 5 and 6, the cl 32/34/42/46/51 weekly-compensation chain, cl 47, cl 52, s 114 (both statutory examples reproduce), lump sums, fatal grants and offence maxima agree with my independent expectations.

The real defects are in **cover**. Section 22(3) and the place and residence limbs of ss 21 and 21B are missing, so the encoding over-grants cover abroad. Section 35(1)(b) is missing as well. Section 17 is a disputed reading that under-grants. The rest are boundary or presentation issues: s 250's day 210, and `NOTHING` versus 0 for non-earners.

## Triage by the encoder (2026-10-12)

All seven disagreements were accepted as encoding errors and fixed. After the fixes this file passes 315/315 with no changes to expected values. The only plumbing edit is that the `tf` fixture sets the new `Treatment facts` field, `the treatment was for a work-related injury`, to FALSE.

| item | outcome |
| --- | --- |
| s 22(3)-(4), E53 | fixed; residence reading recorded as fork F8 |
| s 21(2)(b)(ii), E55 | fixed; fork F9 |
| s 21B(2)(c), E66 | fixed; fork F9 |
| s 17(3), E69 | fixed: an absence of 6 months or less with NZ the permanent home, or more than 183 days present |
| s 250(4), E237 | fixed: first penalty on day 211 |
| s 35(1)(b), E90 | fixed: `the vehicle involvement that counts under s 35` |
| E137 | fixed: a non-earner gets JUST 0 |
| "misses" 1 (s 228(3) through the goal) | fixed: new `Treatment facts` field, read by the goal |
| "misses" 2 (cl 34 applied to every employee) | not changed; stated in NOTES §1 and as an open question |
| "misses" 3-9 | left as declared simplifications or caller inputs; F1 and F7 were already forks |
| REFUSE items | indexed and regulated figures stay caller inputs, as the brief states |

## Change after the pass: Legislation Act s 55 (2026-10-17)

At the user's direction the encoder applied Legislation Act 2019 s 55 to the deadlines for lodging a claim (s 53), deciding claims (ss 54-57), deciding the need for a rehabilitation plan (s 75), applying for review (s 135), the review decision (s 144), paying review costs (s 148), appealing (s 151) and seeking leave (s 162), the Corporation's list for the Registrar (s 152), recovering levies (s 226), a ceasing employer's notice (s 232), laying a charge (s 336) and an estate's application (s 120); not the s 146 deemed decision, whose date is tied to the 3 months. 4 of the independent author's assertions, written before that change, expect the unextended date where the deadline falls on a non-working day; they now fail by design and are counted as expected failures. No expected value was edited. `check.sh`: `tests-independent.l4` 311 satisfied, 4 failed.
