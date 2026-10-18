# Encoding brief: the Immigration, Asylum and Nationality Act 2006 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Immigration, Asylum and Nationality Act 2006** (2006 c. 13), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 2 December 2025, deposited at `../registers/source-bundle/ukpga-2006-13.txt` (Crown copyright, Open Government Licence v3.0).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Most of the Act amends other Acts: appeals, information powers, nationality. The provisions that work by themselves for a person are the **employment of illegal workers**, ss 15-25. Top level: *an employer employed someone. Was the employment contrary to s 15; is the employer liable to a civil penalty or excused; what are the dates on a penalty notice and for an appeal; and is an offence under s 21 committed, with what maximum sentence?*

1. **Employment contrary to s 15** (ss 15(1), 24, 25):
   - an adult (16 or over on the day) subject to immigration control;
   - with no leave, or leave that is invalid, has ceased, or carries a condition preventing the employment;
   - immigration bail is treated as leave, and its employment restriction as a condition (s 24);
   - employment means under a contract of service or apprenticeship.
2. **The civil penalty** (ss 15(2)-(6), 16, 17(4A)-(4E)):
   - the penalty may be given, and is excused under s 15(3) unless s 15(4) applies;
   - the amount is at most the prescribed maximum (an input);
   - the earliest pay-by date that may be specified (s 15(6)(c));
   - whether an appeal may be brought (s 17(4A)) and its last day (s 17(4B)-(4E)).
3. **The offence** (ss 21, 22(1)-(1A)):
   - whether the employer commits an offence under s 21(1) (knowing) or (1A) (reasonable cause to believe), with a body's knowledge attributed under s 22;
   - the maximum imprisonment on indictment and on summary conviction (s 21(2), (4)).

Left out on purpose: everything outside ss 15-25 (appeals, information, fingerprinting, accommodation, nationality, refugee construction, deprivation of citizenship), ss 18-20, 22(2)-(4) and 23, and the content of the prescribed requirements (an input).

## Inputs, not worked out

- The employee's date of birth and immigration position on the day.
- Whether the employer complied with the prescribed requirements, and whether it knew the employment was contrary to s 15.
- The prescribed maximum.
- The dates of the penalty notice and of the objection decision, and the end of the prescribed s 16(5)(b) period.
- The "general limit in a magistrates' court" (England and Wales), and the date of conviction.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"Adult": "has attained the age of 16"**, on the 16th birthday. A 29 February birthday falls on 28 February in a non-leap year (the `add years` reading).
- **s 15(6)(c), "a date, at least 28 days after the date specified in the notice as the date on which it is given"**: the earliest pay-by date is the given date + 28.
- **s 17(4B), "within the period of 28 days beginning with the relevant date"**: ends on the relevant date + 27.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`iana-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
