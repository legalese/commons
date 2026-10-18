# Encoding brief: the Housing Act 1988 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Housing Act 1988** (1988 c. 50), England and Wales. The source is the revised text on legislation.gov.uk, point in time 29 June 2026, deposited at `../registers/source-bundle/ukpga-1988-50.txt` (Crown copyright, Open Government Licence v3.0).

The revised text runs two versions of several provisions together: the text before, and the text after, the amendments made by the Renters' Rights Act 2025. In s 8, the original (3)(b) refers to "(3A) to (4B)", and the amended text to "(4) to (4AA)" with a table of notice periods. That table is lost in the conversion. Section 21 is printed in full.

The encoding takes the s 8 version as an input:

- for the version **before** the 2025 amendments, the notice periods in s 8(3A)-(4B) are computed;
- for the version **as amended**, the encoding refuses, because its table is not in the source.

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level: *a landlord of an assured tenancy wants possession, or has evicted the tenant. For a s 8 notice, what are the earliest and latest days for proceedings, and was a Ground 7A notice served in time; for a s 21 notice (England), was it given at a permitted time with enough notice, and by when must proceedings begin; and for unlawful eviction, is the landlord liable for statutory damages, and how much?*

1. **Section 8 notices** (s 8(1)(a), (3)(b)-(c), (3A), (4), (4A), (4B), (4C)-(4F); pre-2025 version):
   - the earliest day the notice may specify for proceedings;
   - the last day to begin proceedings (12 months from service);
   - whether a Ground 7A notice was served within its period.
2. **Section 21 notices, England** (s 21(1)(b), (4)(a)-(b), (4ZA), (4B)-(4E), (6)-(7)):
   - whether the notice was given after the first four months of the tenancy (or of the original tenancy, for a replacement tenancy);
   - whether the date it specifies is late enough;
   - the last day to begin proceedings.
3. **Damages for unlawful eviction** (ss 27(1)-(3), (6)-(8), 28(1)): liability (with the reinstatement and belief defences), and the amount. The amount is the difference between two valuations, which are inputs, less any reduction the court makes.

Left out on purpose:
- security of tenure, fixing the terms of statutory periodic tenancies, and demotion (ss 5-6A);
- the grounds themselves (Schedule 2, which are inputs);
- rent increases (ss 13-14, where the two versions are run together);
- Part I chapters II-VI apart from s 21;
- Parts II-V.

## Inputs, not worked out

- **The s 8 notice:** the version, the date of service, the grounds specified, whether the tenancy is periodic or fixed-term, and (for a periodic tenancy) the earliest day a landlord's notice to quit served the same day could end it.
- **Ground 7A:** the condition relied on, and the date of conviction, finding or closure order (or of the final determination of an appeal).
- **The s 21 notice:** the tenancy start (or original tenancy start), whether it is periodic, the date given, the date specified, and the notice-to-quit date.
- **Unlawful eviction:** the acts, the occupier giving up occupation, reinstatement, the defendant's beliefs, the two valuations, and any reduction.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"Twelve months from the date of service", "one month after", "two months from", "two months after"**: the corresponding date that many months later, or the last day of that month if it has none.
- **"The expiry of the period of two weeks from the date of the service"**: service + 14.
- **"Within the period of N months beginning with" day X**: on or before the day before the corresponding date N months later, or the last day of that month if it has none.
- **s 21(4B), "may not be given ... within the period of four months beginning with the day on which the tenancy began"**: the notice must be given after the last day of that period.
- **s 21(4D)-(4E), "may not be begun after the end of the period of six (four) months beginning with" the date**: the last day of that period.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ha88-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
