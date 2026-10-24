# Internal Revenue Code of 1986 (26 U.S.C.)

What is deposited, and the terms it was deposited under, are in [`SOURCE-LICENSE.md`](SOURCE-LICENSE.md) and in `registers/source-bundle/*.meta.json`. How this subject connects to the Social Security Act and SNAP is in [`../README.md`](../README.md).

## Encodings

- **[`encodings/baseline-2026-10/`](encodings/baseline-2026-10/)** (24 October 2026). The individual taxpayer's federal income tax for taxable year 2026, from the seat of the individual. It covers:
  - who must file (s 6012);
  - filing status (ss 1, 2, 6013, 7703);
  - gross income to taxable income (ss 61, 62, 63, 151, 152), with the deduction for seniors;
  - the 2026 rate tables, from Rev. Proc. 2025-32;
  - the Child Tax Credit (s 24) and the EITC (s 32);
  - taxable Social Security benefits (s 86);
  - self-employment tax (ss 1401-1402, s 164(f)).

  It has a seat-neutral core with three regulative rules and a seat layer of seven `@export` questions. NOTES.md records eleven findings. The first is that for 2026 the s 6012 filing thresholds turn on how "exemption amount" is read, now that s 6012(f) has lapsed.
