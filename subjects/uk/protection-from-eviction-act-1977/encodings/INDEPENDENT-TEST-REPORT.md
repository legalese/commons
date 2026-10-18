# Independent test report — Protection from Eviction Act 1977

Expected values were fixed in `independent-expectations.md` from BRIEF.md and the revised text (1 May 2026) before any `.l4` module was read. `pea-tests.l4` was not read. Tests are in `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 1 | 123 | 1 |
| every other module | 0 | (pea-tests 69) | 0 |

**124 assertions: 123 pass, 1 fails.** The single error is the failed assertion; there are no other errors.

What the passing tests cover:
- **Goal 1:** every exclusion in s 3A, the hostel rule (licences only), the s 3(2C) saving for tenancies but not licences, s 8(2), and s 2 with and without a lawful resident.
- **Goal 2:** both versions of s 5(1)(b). The 4-week day across February in 2027 and 2028. The two-month day from 29, 30 and 31 Dec, 31 Jul, 30 Apr, 31 Oct and 29 Feb 2028. Agreed periods under (1ZA)(a)(i), including over two months, exactly two months, and a joint tenancy without every tenant's agreement. (1A), (1B)(a)/(b) and (1C).
- **Goal 3:** s 1(2), (3), (3A)/(3B), s 1A(1)-(3).
- **Schedule A1:** para 1(1) month-end cases (31 Aug 2026 -> 28 Feb 2027, 31 Aug 2027 -> 29 Feb 2028, 29 Aug 2027 -> 28 Feb 2028, 31 Dec 2026 -> 30 Jun 2027, 30 Dec 2026 -> 29 Jun 2027), para 1(2) with continuing conduct, and paras 4(2), 5 and 10(2).
- **The `@export default` goal.**

## Failure

### L271 — N38: s 5 applied to a service occupier

- **Scenario:** the occupancy kind is `exclusive possession under employment`, and the notice is not marked as ending a periodic licence. Is s 5 engaged?
- **Expected:** FALSE.
- **Encoding:** TRUE. In `s 5 applies to`, `periodicIfLicence` is `OTHERWISE TRUE` for every kind except `a licence`. The amended-version earliest-day rule also treats this kind as a tenancy (`isTenancy`).
- **Act:** s 8(2) deems such a person a tenant only "for the purposes of Part I of this Act". Section 5 is in Part II and speaks of "premises let ... as a dwelling" (s 5(1)) or "a periodic licence" (s 5(1A)). A service occupier who is not a tenant is a licensee, so s 5 reaches him only through (1A), if the licence is periodic.
- **View:** the Act supports the expected value. The fix is to treat `exclusive possession under employment` like `a licence` in s 5: periodic only, with 4 weeks.

## Remarks on the encoding (tests pass, but worth noting)

1. **Several limbs are folded into single input booleans,** so they cannot be tested and the user must apply the law:
   - s 3A(2) and (3): the "both immediately before grant and at the end" timing, the purpose-built block test, and the s 3A(4) rule that any one joint landlord counts;
   - s 3A(5)(a): storage areas and means of access are not "accommodation";
   - s 3A(7D)(a)/(b);
   - s 3(2C)(a)/(b) together with the s 8(5) rent-variation rule, all in `entered into before the Housing Act 1988`. The 15 Jan 1989 boundary and s 8(5)(a)/(b) are left to the user.

   This is acceptable as inputs, but nothing in the encoding computes the boundary.
2. **The (1ZA)(a)(i) agreed period is taken in days only.** An agreement for "one month" (the natural form) cannot be expressed exactly; the user must convert it, and 30 or 31 days gives a different day from the corresponding-date method. Consider taking months as well.
3. **`agreed with all the tenants` must be TRUE for a sole tenant.** If a sole tenant's agreement is entered with the flag left FALSE, the result silently falls back to two months. The field could be "a joint tenancy where not all tenants agreed", or carry a clear @desc.
4. **s 1(7) is not encoded** (no conviction once a penalty is imposed). Neither is any check that a proposed amount is at most £40,000 (s 1A(3)) or Sch A1 para 10(6); only the constant exists. These are small and in scope for goal 3.
5. **s 3(3) (death of a statutory tenant) is not encoded.** s 3(2A) is subsumed by (2B), which is fine.
6. **A statutorily protected tenancy gives FALSE** for "court proceedings required". This is defensible ("this Act does not require it"), and the @desc says so. A reader of the boolean alone may take it as "self-help is lawful", so a REFUSE or a separate flag would be clearer.
7. **A landlord's notice under an assured tenancy (RRA version) gets the (1ZA)(b) 4 weeks.** That is right on s 5 alone. The Act's own note points to HA 1988 s 5(1) (such a notice is of no effect), which the encoding does not surface.
8. **s 2 does not check that the occupancy is a lease (kind `a tenancy`);** a licence with the forfeiture flag set would still trigger it. This is minor.
9. **The date arithmetic matches the brief in every case tried,** including the "no corresponding day -> last day of month" rule for 6-month periods. Note that the 6-month rule is implemented as "day differs after clamping -> no day before". This is correct for clamped month-ends only because `add months` clamps.

## Change after the pass (encoder)

- **N38 fixed.** `s 5 applies to` now treats `exclusive possession under employment` like a licence: s 5 applies only if the licence is periodic. The same applies to the RRA two-month rule, which is now only for `a tenancy` (NOTES F10). The independent assertion now passes.
- **Remark 8 adopted.** s 2 now requires the occupancy to be a tenancy (a lease).
- **Remarks 1, 2, 3, 6 and 7 are recorded in NOTES.md as known limits.** Remark 4 (s 1(7), the £40,000 check, para 10(6)) is left out on purpose: s 1(7) bars a conviction, not the penalty, and the amount is the authority's choice up to the constant.
- After the change, `check.sh` shows 7 modules: 193 assertions satisfied, 0 failed, 0 errors (69 encoder, 124 independent).
