# Encoding brief: the Superannuation (Pension Increases) Act 1961 (Cth), in L4

## The subject

**Superannuation (Pension Increases) Act 1961** (Act No. 86 of 1961, as amended), Commonwealth of Australia, deposited at `../registers/source-bundle/C1961A00086.txt` (CC BY 4.0).

## Seat

**The prescribed pensioner, or the widow** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level: *"What increase in my annual pension am I entitled to, and from when?"* Section 4 (increases) and s 7(1) (from the first fortnightly payment after commencement); the definitions in s 3 that the computation needs.

- s 4(1): increase = the prescribed amount × the additional unit entitlement (adjusted unit entitlement less actual unit entitlement, where the adjusted exceeds the actual).
- s 3 "the prescribed amount": (a) £32 10s (32.5 pounds); (b) where the actual unit contribution is less than the actual unit entitlement (and s 52 did not apply): £32 10s × contribution ÷ entitlement; (c) and (d): proportions that depend on the 1922 Act's scales and on other pension amounts, taken as an input fraction of £32 10s (for (d), the fraction combines its proportion with any (b) or (c) proportion).
- s 4(2): reduced by any increase under s 11 of the Superannuation Act 1957, not below nil.
- s 4(4): a widow gets five-eighths of the increase her husband would have had.
- s 4(6): no increase for a child's pension, or a pension under ss 53, 57 (unless State Fund contributions) or 58 of the 1922 Act.

## Inputs

The unit figures (adjusted entitlement, actual entitlement, actual contribution), which case of "the prescribed amount" applies (and its fraction for (c)/(d)), any 1957 increase, whether the person is a widow, whether the pension is excluded, and the first fortnightly payment date after commencement.

## Rules that matter

- Amounts are in pounds, as the Act gives them.
- A failing assertion is a finding. Never edit an expected value to match the code.
