# Protection from Eviction Act 1977 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the eviction position for` (`pea-goal.l4`). For one occupier it answers:

- whether the owner must use court proceedings to recover possession, and whether the letting is excluded;
- if a notice to quit was given: whether it meets s 5, and the earliest day it can take effect;
- if the landlord's conduct is in question: whether it is an offence under s 1, whether a financial penalty may be imposed, the maximum, and the Schedule A1 dates.

Three goals sit under it:

1. **Eviction only by court proceedings** (`pea-eviction.l4`):
   - s 2 (forfeiture);
   - s 3(1), (2B), (2C);
   - the s 3A exclusions;
   - s 8(1)-(2).
2. **Notices to quit** (`pea-notice-to-quit.l4`):
   - s 5(1) in both printed versions of (b);
   - (1ZA)-(1ZB);
   - (1A)-(1C).
3. **The offence and the financial penalty** (`pea-penalty.l4`):
   - s 1(1)-(3C);
   - s 1A(1)-(3);
   - Schedule A1 paras 1, 4(2), 5 and 10(2).

As the user asked, this covers only the sections those goals need. The rest of the Act was left out on purpose (see the table).

Dates are computed as the Act words them. The UK has no general next-working-day rule, so no date moves for a weekend or bank holiday.

## Seat

The encoding is written from the seat of **the residential occupier (tenant or licensee)**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Can I be evicted without a court order; is the notice to quit I was given (or want to give) valid, and from when; and if my landlord evicted or harassed me, can the council fine them, up to how much, and when?"

The facts it asks for are ones that person can state, or findings made about them.

The penalty goal (s 1A, Sch A1) states the council's powers and deadlines. For the occupier these are the remedies available against the landlord, and the dates by which they must be used.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| s 1(1)-(3C) | encoded (goal 3) |
| s 1(4)-(6) | out of scope: penalties on conviction, liability of officers |
| s 1(7) | out of scope: a bar on conviction, not on the penalty |
| s 1A(1)-(3) | encoded (goal 3) |
| s 1A(4)-(10) | out of scope: guidance and regulation-making powers |
| s 2 | encoded (goal 1) |
| s 3(1), (2), (2B), (2C) | encoded (goal 1) |
| s 3(2A) | folded into (2B): a restricted-contract licence is a licence |
| s 3(3) | out of scope: statutory tenancies under the Rent Acts |
| s 3A | encoded (goal 1); paras (2)-(3) are one input each |
| s 4 | out of scope: agricultural employees |
| s 5(1), (1ZA)-(1ZB), (1A)-(1C) | encoded (goal 2); the version of (1)(b) is an input |
| s 5(1ZC)-(1ZD), (2)-(3) | out of scope: these are definitions and powers; the prescribed information is an input |
| s 5A | out of scope |
| ss 6-7 | out of scope: prosecution, service |
| s 8(1)-(2), (4) | encoded; (5)-(6) variation is folded into the "before the Housing Act 1988" input |
| ss 9-13 | out of scope |
| Sch A1 paras 1, 4(2), 5, 10(2) | encoded (goal 3) |
| Sch A1 other paragraphs | out of scope: contents of notices, withdrawal, recovery, proceeds |
| Schs 1-3 | out of scope |

## Forks (readings taken)

- **F1, s 5(1)(b): two printed versions.** The revised text prints both the original (b), four weeks, and the (b) substituted by the Renters' Rights Act 2025, which applies (1ZA). The version is an input, `Section 5 version`, and the two are never merged.
- **F2, "given not less than 4 weeks before the date on which it is to take effect".** The date of effect is at least the day of giving + 28. The common-law rule that a periodic tenancy ends at the end of a period is not part of this Act and is not encoded.
- **F3, "not less than two months before".** The date of effect is on or after the corresponding date two months later, or the last day of that month if it has none: given 31 December, the earliest date is 28 February.
- **F4, s 5(1ZA)(a)(i).** An agreed period longer than two months is not an agreement "not exceeding two months", so (ii) applies. An agreement not made with all joint tenants is invalid (1ZB), so (ii) applies.
- **F5, s 3(2C).** The saving for tenancies from before the Housing Act 1988 applies to tenancies only, so an excluded licence is excluded whenever it was granted. Section 3A(8) (hostels) applies to licences only.
- **F6, ss 2 and 3 for statutorily protected tenancies.** Section 3 does not apply to them, so the goal answers FALSE for "this Act requires proceedings" under s 3. Their own Acts protect them. Section 2 applies to any dwelling lease.
- **F7, s 1(3B).** The defence of reasonable grounds answers s 1(3A) only. Where intent is proved under s 1(3), the defence does not help.
- **F8, Sch A1 para 1(2).** For conduct continuing beyond the first day of sufficient evidence, the notice may be given at any time while it continues, or within six months beginning with its last day. While the conduct continues there is no last day, and the answer is NOTHING.
- **F9, "the period of 28 days beginning with the day after" day X.** It ends on X + 28. The final notice comes "after the end of" the period for representations, so on X + 29 at the earliest.

- **F10, s 8(2) is for Part I only.** A service occupier with exclusive possession is a tenant for ss 1-4 only. For s 5 (Part II) they are a licensee, so s 5 applies only under a periodic licence, with four weeks' notice. This was changed after the independent pass (N38).
- **Known limits (from the independent pass).**
  - Several s 3A limbs are single input booleans.
  - The (1ZA)(a)(i) agreed period is taken in days only.
  - `agreed with all the tenants` must be TRUE for a sole tenant.
  - The HA 1988 s 5(1) pointer (a landlord's notice under an assured tenancy has no effect) is not applied.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18:

- 7 modules: 193 assertions satisfied, 0 failed, 0 other errors;
- 69 are the encoder's (`pea-tests.l4`);
- 124 are independent (`tests-independent.l4`).

The independent pass found one disagreement, N38, which was fixed in the encoding. No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** from which date, and for which tenancies, does the Renters' Rights Act 2025 version of s 5(1)(b) apply?
- **F3:** confirm the corresponding-date reading of "two months before" for a notice given at the end of a month.
