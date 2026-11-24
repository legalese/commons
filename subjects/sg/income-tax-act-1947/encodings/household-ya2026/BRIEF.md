# Brief: a Singapore household's income tax and employee CPF, YA 2026

Target compiler: `main` (the stable `l4`); the encoding is also checked with the newest `unstable` build.
Seat: the individual who is taxed: one or two adults living together and their children.

## The question

For a household, what is the income tax for the year of assessment, the employee's CPF, and the net income, for income year 2025 (YA 2026), and for 2026 (YA 2027)?

## Scope

A resident individual, or a married couple who are both resident, with:
- wages paid month by month, ordinary wages and additional wages (bonuses), for an employee who is a citizen or a permanent resident past the second anniversary month, or who is neither (a foreign employee: the employer is exempt from contributing, Central Provident Fund (Exemption) Order 2018 para 3, so the employee's CPF is nil and the income tax is computed as usual; amended 2026-11-24 after the independent test pass read the Order);
- trade income and rent (figures after their own deductions), and tax-exempt income that matters only for the $8,000 tests;
- children: qualifying child relief, the working mother's child relief, the parenthood rebate;
- the reliefs of the Income Tax Act 1947 s 39 that depend on facts a household can state (earned income, spouse, children, CPF and life insurance, parents, siblings, NSman, SRS, CPF top-ups, grandparent caregiver), the $80,000 cap of s 39A, the Second Schedule rates;
- the employee's share of CPF under the First Schedule of the Central Provident Fund Act 1953, as in force in 2025 and 2026.

Not covered (the answer is "not covered", never a guess): a non-resident adult; a permanent resident in the first two years; employment expenses and donations; taxable pensions in "earned income"; the self-employed's CPF; Budget rebates and remissions that are not in the Act's text; any income year but 2025 and 2026.
A taxable pension has no input, so the household cannot state one and the module never answers "not covered" for it: it is simply not asked.

## Sources

- `../source/ITA1947.txt`: the Income Tax Act 1947, SSO's current version as at 06 Oct 2026. The Second Schedule (Table 3 applies to a year of assessment from 2024), s 39 and s 39A, s 42A, the Fifth Schedule, and "earned income" in s 2.
- `../../../central-provident-fund-act-1953/registers/source-bundle/CPFA1953.txt`: the Central Provident Fund Act 1953, version in force from 1 July 2026: the First Schedule (paragraph 1 is the 2026 table), paragraphs 2 to 5 (additional wages, the applicable amount of $102,000, the Ordinary Wage Ceiling).
- The First Schedule as in force in 2025 (paragraph 1 "with effect from 1 January 2025"): SSO's version as at 1 Jan 2025, https://sso.agc.gov.sg/Act/CPFA1953. The 2025 employee figures are in `../../../central-provident-fund-act-1953/encodings/baseline-2026-10/NOTES.md` ("Added 2026-11-24").
- Referees (outside, not sources of law): IRAS's published tables and worked examples; Lexifina's Singapore model; PolicyEngine-SG. They test the encoding; none of them decides what the Act says.

## Deliverables

`sg-household.l4` (the module), `sg-household-tests.l4` (hand-worked cases), `tests-independent.l4` and `tests-independent-supplement.l4` (written from the sources by someone who had not seen the module; the supplement after reading its input types), `sg-household-tests-iras.l4` (IRAS's published worked examples, figures only), `NOTES.md` (scope, the coverage of provisions, forks, answer table, checks), `FINDINGS.md` (this encoding against Lexifina's Singapore model and PolicyEngine-SG), the copied modules (see NOTES.md, "Copied modules"), `check.sh`.

## Rules that matter

1. The Act's words decide. Where the Act is silent (for example, whether "income" in the $8,000 tests includes tax-exempt income), the reading taken is a labelled fork in NOTES.md with a discriminating case.
2. Every expected value in a test is worked from the Act's text. No test value comes from a referee, and none is edited to match what the code computed.
3. The household module builds the facts the Income Tax Act encoding and the CPF encoding ask for and adds up; the rates and reliefs live in those two. What it decides itself is listed in NOTES.md section 2a.
