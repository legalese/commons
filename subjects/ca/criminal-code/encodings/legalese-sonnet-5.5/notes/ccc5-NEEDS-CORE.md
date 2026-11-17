# NEEDS-CORE (ccc5)

Nothing in `ccc5-*.l4` was blocked by the core: every type used is `ccc-core.l4`'s (`Party`, `Punishment`, `Imprisonment`, `Class of offence`, `Length of time`, `Province or territory`, `Provision of the Code`) or declared under the `s N` prefix in this part.
Three constructors would make the encoding closer to the text, and the lead may wish to hoist them (none is needed for the checks to pass):

1. **`Party`: "the Attorney General of the province"** as its own constructor. `s 110.4(2)(b)` and `s 117.0104(2)(b)` answer "the Attorney General of the province in which the application was made" with the core's `the Attorney General or Solicitor General of the province`, which is section 2's wording for the same office ("Attorney General ... means the Attorney General or Solicitor General of the province"). Fork FM-19 in `NOTES.md`.
2. **`Party`: `a firearms officer`, `a chief firearms officer`, `the Registrar of Firearms`, `a provincial minister`.** Sections 110.4 to 117.14 name these persons as applicants, as holders of a power or as the persons a thing is surrendered to. This part takes them as plain facts ("Is the applicant a firearms officer?") and does not use them as actors of a regulative rule, so no declaration of its own was needed.
3. **`Party`: `an analyst`** (section 117.13, certificate of an analyst); the same remark.
