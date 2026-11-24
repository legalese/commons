# A Singapore household's income tax and employee CPF, YA 2026: notes for a reviewer

## 1. What this is

A calculator for one or two resident adults and their children: the income tax for the year of assessment, the employee's CPF, and the net income, for income year 2025 (YA 2026) or 2026 (YA 2027).
It is a **thin layer**.
It builds, for each adult, the facts that the Income Tax Act encoding asks for, takes the employee CPF from the CPF encoding, and adds up.
The law is in the two encodings it composes: `../legalese-aswathy/` (Income Tax Act 1947) and `../../../central-provident-fund-act-1953/encodings/baseline-2026-10/` (Central Provident Fund Act 1953).
This row was written on 2026-11-24 to turn those two into a calculator that can be tested against outside referees, and `FINDINGS.md` records how it fares against two of them.

**Seat:** the individual who is taxed, here the household.
**Status:** `draft`. No domain expert has read it against the Acts (gate HG1 not sought).
An independent test pass was run (section 7).
The method is in `BRIEF.md`.

## 2. What is encoded, and what is not

Encoded: the Second Schedule's rates for a resident individual (Table 3, YA 2024 and later); s 38; the reliefs of s 39 that a household can state; the cap of s 39A; the Fifth Schedule (child relief, the working mother's child relief, the $50,000 and 100% limits); the parenthood rebate of s 42A with its carry-forward; and the employee's share of CPF under the First Schedule, as in force in 2025 and 2026, for ordinary and additional wages.
The rates and the reliefs are stated in the two encodings that are copied in; this row's own module, `sg-household.l4`, builds their inputs and adds up, and decides a few things itself, listed in section 2a.

Not covered, and the answer is "not covered" (`NOTHING`), never a guess: a non-resident adult; a permanent resident in the first two years (graduated CPF rates, First Schedule paragraphs 1A to 1D); any income year but 2025 and 2026, and a year of pay that is not twelve months, **for a foreign employee as for anyone else** (checked first; fixed 2026-11-24); a share of a child's relief or rebate that no division could give (fork H2).
Not covered, and **cannot be said by this module because it has no input for it**, so the caller must not use it for them: more than one employer; the employees of a paragraph 6 or 7 body; a taxable pension (fork H5); a child under articles (s 39(2)(e)(iii)); adoption or marriage as the route to a parenthood rebate; the conditions of s 39(2)(c), (d) and (o); the spouse and sibling top-up cliff of s 39(3AA), which no module of the Income Tax Act encoding has, so the top-up inputs must be given after it.
Left out and said so: employment expenses, donations (s 37); a trade's own deductions (the figure is given after them); taxable pensions in "earned income" (s 2, fork H5); the self-employed's CPF (the encoding has `cpf-self-employed.l4`; the household does not call it); the Comptroller's discretionary remissions; any Budget rebate that is not in the Act's text.
**No personal income tax rebate for YA 2026 is in the Act as at 6 Oct 2026**: the text mentions a rebate in s 42A (children), in the headings of the company provisions (for example s 92K, a listing rebate), in a note on the Additional Petrol Duty Rebate for taxi and private-hire drivers' payments, and in a Foreign Worker Levy Rebate, and none of these is a rebate of a resident individual's tax on income. A personal rebate for a year would come, if at all, from the Minister's power in s 92(2A) to remit the tax of a class of persons by order, which is outside the Act's text and therefore outside this row.
IRAS's pages list personal rebates for YA 2024 and YA 2025 only, and none for YA 2026.

## 2a. What the household layer decides itself

`sg-household.l4` builds the facts the two copied encodings ask for.
Where it does more than carry an input across, it is here, with the provision and what the household cannot say as a result:

| where | what the layer does | what it cannot say |
|---|---|---|
| s 39(2)(e)(i), below 16 (fork H4) | counts a child by birth year: born in the year 16 years before the income year or later | a child born on 1 January of that year is 16 from the first moment of the income year, so the words exclude her, and she is counted (a one-day cohort; the same shape as fork I3 of the Income Tax Act row) |
| the order of a mother's children (fork H3) | counts the children within s 39(2)(e)(i), (ii), (iv), maintained and unmarried, in list order | it is a second copy of the limbs in `an eligible child for YA` of the copied module, without paras 3 to 3B; a later change there must be made here too; a child under articles ((iii)) cannot be stated |
| s 39(2)(c), (d) | fixes the payments to a former spouse at nil and the spouse's infirmity at false | a separated spouse's payments, a disabled spouse |
| s 39(2)(o) | fixes the suspension or withdrawal of an SRS account at false | an account suspended at 31 December |
| s 39(2)(k), (11) | course fees and the domestic worker levy at nil, as the Act says for the years covered | nothing |
| s 42A | states a rebate for a child born in the income year, born on 1 July, not adopted before marriage, by her position in the household's list (s 42A(11) counts siblings in the household at the birth) | a rebate by adoption or by marriage (s 42A(1)(b) to (d)) |
| the shares of a child's relief and rebate (fork H2) | answers `NOTHING` unless each share is from 0 to 1 and is 1 for a sole adult | nothing: it is a check of the household's own input, not of the Act |

## 3. Modules

| module | what it holds |
|---|---|
| `sg-household.l4` | the household's facts and result; builds each adult's `Individual relief facts`, `Child facts` and `My year of work`; adds the two adults up |
| `ita-types.l4`, `ita-rates.l4`, `ita-reliefs.l4` | copied: the Income Tax Act encoding (section 6) |
| `cpf-contributions.l4`, `cpf-wages-year.l4` | copied: the CPF encoding (section 6) |
| `sg-household-tests.l4` | 71 assertions on hand-worked cases, including the cliffs, the cases IRAS's examples raised and the checks of the shares |
| `sg-household-tests-properties.l4` | Table 3 written out as one BRANCH, tied to the encoding by evaluation at every band edge |
| `sg-household-tests-proofs.l4` | the solver's proofs about that table: for every chargeable income, no negative tax, no more tax on more income, no jump (unstable only: `l4 prove`) |
| `tests-independent.l4`, `tests-independent-supplement.l4` | the independent test pass (section 7): cases 1 to 70, and eight supplementary cases written after reading the module's input types |
| `sg-household-tests-iras.l4` | IRAS's published worked examples as assertions, figures only (section 7, `FINDINGS.md` section 4) |
| `check.sh` | runs everything with both builds, proves, and checks the copies |

## 4. Coverage of the provisions in scope

| provision | disposition |
|---|---|
| ITA s 38 | encoded (copied `ita-reliefs.l4`) |
| ITA s 39(1) earned income relief | encoded; age by 31 December, fork I3 (corrected 2026-11-24) |
| ITA s 39(2)(a), (c), (d) spouse reliefs | (a) encoded, the spouse being the other adult of a married couple (fork H1); (c) and (d)'s conditions are fixed off (section 2a) |
| ITA s 39(2)(e), Fifth Schedule paras 1, 3, 3B, 4 | encoded, with provisos (v) and (vi); (iii) is not asked; shares are inputs (fork H2); "below 16 at any time" (fork H4) |
| Fifth Schedule para 5 (1A), (1AB), (3), para 6(2) | encoded: the working mother's child relief; the mother is named for each child; the order counts the children within s 39(2)(e) (fork H3); the $50,000 for one child counts every claimant's qualifying child relief (para 6(2), "all individuals") |
| ITA s 39(2)(ga), (10A), (10B), (6) | encoded: employee CPF (from the CPF encoding) with life insurance premiums, $5,000 rule |
| ITA s 39(2)(g), (h) (YA 2025 or before), (ha), (haa), (hb) | not reached: the household has no self-employed CPF |
| ITA s 39(2)(i), (j) parents and siblings | encoded; facts are inputs, two-dependant limit; shared relief takes the larger amount when any claimant lives with the dependant (s 39(2)(i)(vii)(B)) |
| ITA s 39(2)(k), (12), (12A), (12B), (12C) course fees | encoded as nil from YA 2026 (s 39(12C)) |
| ITA s 39(2)(m), (n), (2A), (2B) NSman | encoded; certification is a fact; one $750 at most for a wife and a parent, none to a parent with an NSman relief of his or her own |
| ITA s 39(2)(o) SRS | encoded; the cap is an input |
| ITA s 39(2)(p) grandparent caregiver | encoded; the caregiver's income is an input |
| ITA s 39(3), (3A) CPF top-ups | encoded; the prescribed limits are inputs; s 39(3AA), the $8,000 cliff on the spouse's or sibling's income, is in no module of the Income Tax Act encoding and must be applied by the caller |
| ITA s 39(11) domestic worker levy | nil (YA 2024 and before) |
| ITA s 39A $80,000 cap | encoded |
| ITA s 42(1), Second Schedule Table 3 | encoded; proved monotone and without a jump |
| ITA s 42A parenthood rebate | encoded with s 42A(3) carry-forward; the brought-forward balance is an input |
| ITA s 40A to 40D, 43 (non-residents) | not covered |
| CPFA s 7(1), (2); First Schedule paras 1, 2, 4A, 5 | encoded in `cpf-wages-year.l4` (the 2025 table from SSO's version as at 1 Jan 2025) |
| CPFA Exemption Order 2018 para 3 (neither citizen nor permanent resident) | encoded: the employer is exempt from contributing, so the employee's CPF is nil and the tax is computed as usual (the BRIEF said so loosely until 2026-11-24, when the independent pass found the difference) |

## 5. Fork register

The forks of the two copied encodings (I1 to I9 of the Income Tax Act row, W1 to W5 of the CPF row) stand as they are in their own NOTES.md; I3 was corrected on 2026-11-24.
The ones below are the household layer's.

| fork | text | readings | taken |
|---|---|---|---|
| H1 | s 39(2)(a), (i), (j) and Fifth Schedule 3B: "whose income was not more than $8,000" (the Act does not define "income" for these tests) | income of every kind, tax-exempt income included (IRAS's published position); or assessable income only | every kind: earned and property income plus the adult's tax-exempt income. Discriminating case: B3 in the tests (a spouse with no work whose bank interest is $9,000) |
| H2 | Fifth Schedule para 4 and s 42A(2C): where more than one individual may claim, the relief or rebate is "apportioned in such manner as appears to the Comptroller to be reasonable" (para 4) or as they agree (s 42A(2C)) | any split; the household's own choice; one split for both, or one for each | an input for each child, **two** of them: the first adult's share of the qualifying child relief and the first adult's share of the parenthood rebate, each from 0 to 1 (IRAS's published example splits them differently). The referees differ: Lexifina's model gives the child relief to the higher earner, PolicyEngine-SG to the first adult. Cases C8, H2. A share outside 0 to 1, or not 1 for a sole adult, gives `NOTHING` (cases E4 to E7) |
| H3 | Fifth Schedule para 5(1A), (1AB): "the first eligible child", "the second", "the third or a subsequent": ranked by the Comptroller (para 7(b)); para 1 is "subject to" paras 3 to 3B, which bar a child with income over $8,000 from the deduction, yet speaks of "eligible children" | the order of birth among the children who can be claimed at all; or among those the Schedule leaves with a deduction | the children are listed oldest first, and a mother's order is the number of her children within s 39(2)(e) (maintained, unmarried, and below 16, in full-time instruction or incapacitated) up to and including this one, **counting a child whom para 3 or 3B bars from a deduction**. This is the reading of IRAS's published example; the Act is silent. Discriminating case: H1 in the tests. Stillborn siblings (para 5(1B)) are not modelled |
| H4 | s 39(2)(e)(i): "being below 16 years of age at any time during the year preceding the year of assessment" | a child who turns 16 during the year qualifies; or only a child under 16 at the end of the year | the first, which is what the words say. A child born in 2009 qualifies for YA 2026 (case C2). Lexifina's model reads "age under 16" at year end and so disagrees (`FINDINGS.md`). The module has only the birth year, so a child born on 1 January 2009 (16 from the first moment of 2025, never below 16 in it) is counted too |
| H5 | s 2 "earned income" includes "any pension on which tax is payable under section 10(1)(e)" | include taxable pensions in earned income, or not | not asked: earned income is wages and trade income. A taxable pension would raise the earned income relief cap |
| H6 | the Act has no rule that rounds tax, chargeable income or relief | exact to the cent; or the dollar | exact. IRAS's notices and Lexifina's model drop the cents, so comparisons allow the dollar (`FINDINGS.md`) |
| H7 | s 39(4), (4B): one dependant provision per person; but a spouse may be the subject of claims under (a), (c) and (d) | each spouse claims for the other where the other's income is low | each spouse may claim, so the answer is the same whichever spouse's return is read. It makes no difference to tax when both have income under $8,000 (neither pays tax) |
| H8 | the CPF relief of s 39(2)(ga)(ii), (10A)(c) | the employee's share; or the total contributions | the employee's share the First Schedule makes recoverable, per (10A)(c) |

## 6. Copied modules

The skill's rule: another encoding's modules are copied in, byte for byte, never referenced; a change is made in the source encoding and copied again.
`check.sh` compares each copy with its source.

| copy | source | commit it was copied at | sha256 |
|---|---|---|---|
| `ita-types.l4` | `../legalese-aswathy/ita-types.l4` | 6479e7db2 | 2e949404b42834b45d1ce4b94d88a616d62a662baf4d6d444e7becff5d7e381c |
| `ita-rates.l4` | `../legalese-aswathy/ita-rates.l4` | 6479e7db2 | 336a2951f0f5b9be96fd0797b9b816edcedce5564d9f9d043c21318d910a0109 |
| `ita-reliefs.l4` | `../legalese-aswathy/ita-reliefs.l4` | e43c9d577 | 2496778393caa0995670a7e5a441e35ab13ded74674fcde407913555d7acc9c0 |
| `cpf-contributions.l4` | `../../../central-provident-fund-act-1953/encodings/baseline-2026-10/cpf-contributions.l4` | d54a7aa04 | 906ae82cda05ec09e9797161e23dab73772b786e73be01859dd89e8d246bb842 |
| `cpf-wages-year.l4` | `../../../central-provident-fund-act-1953/encodings/baseline-2026-10/cpf-wages-year.l4` | d71fb9f30 | 093c00580c6dbbae1dc0db43c09e85b0e8a23da62bf22f418c64b145e0c4841e |

## 7. Checks

Run: `L4=<unstable l4> L4_MAIN=<main l4> ./check.sh`.
The target is `main`: the stable `l4` reads everything but `sg-household-tests-proofs.l4`, which is for `l4 prove` and exists only on the unstable build.
Builds: `unstable-20261124-9d26421` (9d26421) and the stable `1.6.112` (main, e4f4bf3); run on 2026-11-24 on the tree this folder was committed in.
`check.sh` prints, per module, errors / assertions satisfied / assertions failed with each build; the result:

| module | unstable | main |
|---|---|---|
| `sg-household-tests.l4` | 0 / 71 / 0 | 0 / 71 / 0 |
| `sg-household-tests-properties.l4` | 0 / 53 / 0 | 0 / 53 / 0 |
| `tests-independent.l4` | 0 / 204 / 0 | 0 / 204 / 0 |
| `tests-independent-supplement.l4` | 0 / 26 / 0 | 0 / 26 / 0 |
| `sg-household-tests-iras.l4` | 0 / 174 / 0 | 0 / 174 / 0 |
| the six other modules | 0 / 0 / 0 | 0 / 0 / 0 |
| **total** | **528 satisfied** | **528 satisfied** |

`sg-household-tests-proofs.l4`: five obligations, **5 proved, 0 refuted, 0 unknown** (`l4 prove`, unstable only).
All five copied modules are byte for byte the ones they were copied from.
The Income Tax Act encoding (its `check.sh`: 19 modules, 739 assertions satisfied, with both builds) and the CPF encoding (8 modules, 90 satisfied, with both builds, counted the same way) that this folder copies from pass on the same two builds.
`l4 run` exits 1 on a failed assertion with the unstable build and 0 with the stable one (measured 2026-11-24 on `#ASSERT 1 EQUALS 2`); `check.sh` reads the diagnostics, not the exit code.

**Positive controls** (each check was shown able to fail): the tests file with the C13 repair taken out fails C13; each of the Income Tax Act repairs of 2026-11-24, reverted alone, fails the assertions added for it (the NSman claims 2, the $50,000 limit 1, shared parent relief 2, proviso (vi) 2); the CPF module with the year and the length checked after the residence status fails the three foreign-employee cases; the household with the share check taken out fails E4 to E7; `check.sh` exits 1 when a copy is edited, when an expected count is wrong, and 2 when the main build is missing.

**The independent pass** (`tests-independent.l4`, cases 1 to 70, expected figures written from the two Acts by a session that had not read the module, frozen with a checksum before the module was read; `independent-expectations.md`, `INDEPENDENT-TEST-REPORT.md`, which is a point-in-time record and begins with what has changed since; only the expectations file is deposited of the five files the checksums name): all of cases 1 to 70 that the inputs can state are satisfied (204 assertions), case 51 only after the module took a separate share for the rebate (it could not be stated before: the author reported that, and fork H2 now has two shares).
Eight supplementary cases were written after reading the module's input types (`tests-independent-supplement.l4`, 26 assertions, all satisfied).
One disagreement was found, and it was in the brief, not the code: the author took a foreign employee to be "not covered" from the BRIEF's words; Exemption Order para 3 exempts the employer from contributing for such an employee, so the module's nil CPF and ordinary income tax is right for 2025 and 2026 (a review then found that the module gave the same answer for any year and any length of pay, which is fixed in the CPF row), and the supplement's S7 was changed from "not covered" to the worked figures (1,880 tax, nil CPF, net 58,120) with the reason written beside it; the BRIEF now says so.
The author's own account, including a correction to the claim that some figures were worked before its script ran, is in the report.
What the independent cases cannot show: case 59 (the 7% limit on life insurance is the household's arithmetic before the module; the input is the premium already capped), case 70 (a taxable pension has no input), and the 31 December birthday (both the author's model and the module read age by birth year).

**IRAS's worked examples** (`sg-household-tests-iras.l4`, 174 assertions, figures only): `FINDINGS.md` section 4 lists the three faults they found in the Income Tax Act encoding (now fixed there), the one fork they raised (H3), and the one open disagreement (an employee CPF figure for a man aged 64, not derivable from the page).

## 8. Open questions for a domain expert

1. H1: does "income" in the $8,000 tests of s 39(2)(a) and (i) include tax-exempt income?
2. H4: does a child who turns 16 during the income year qualify for the qualifying child relief?
3. I3 (Income Tax Act row): the person whose birthday is 31 December is exactly 55 or 60 that night and is given the higher band here.
4. The WMCR cap of Fifth Schedule para 5(3), "100% of her earned income": it is applied to both regimes together here, as the text says "under sub-paragraphs (1A) and (1AB)".
5. Whether the CPF Board's handling of additional wages above the annual ceiling matches W1 of the CPF row (the employee's share on that part is nil).
6. H3: does a child whom Fifth Schedule para 3B bars from a deduction still count in the order of the mother's eligible children for para 5(1A)(c) to (e)?
7. The employee CPF relief IRAS publishes for a man aged 64 in 2025 on $250,000 ($7,650, which is the 65 to 70 band for the whole year): is it an age convention, a rounded illustration, or a fact the page omits?
8. s 39(3AA): the spouse's or sibling's income test for the CPF top-up relief is in no module of the Income Tax Act encoding; should the encoding carry it, so that the household's top-up inputs are the amounts before the test?
9. `@export` and `@desc` entry points for Commons' Interact form: this row has none yet; the seat questions would be `the household's position` and its fields.
