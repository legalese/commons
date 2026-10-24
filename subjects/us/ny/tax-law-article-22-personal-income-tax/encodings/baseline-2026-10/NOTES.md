# New York Tax Law, Article 22 (personal income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A question that can reach a case outside the encoding answers `not covered` with the reason, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the statute's own terms in `ny-pit.l4`. The taxpayer's questions are in `ny-pit-seat.l4`, which IMPORTs the core and calls its rules; nothing is restated. Each question has `@export` and every input a `@desc`.

There was no earlier encoding of this Article to keep.

## Edition

NYSenate.gov Open Legislation, retrieved 24 October 2026, each section at its "most recent revision": s 601 (2025-07-11), s 601-a (2014-09-22), s 605 (2018-04-27), s 606 (2026-10-23), s 611 (2014-09-22), s 612 (2026-09-04), s 613 (2020-04-17), s 614 (2018-04-27), s 616 (2014-09-22), s 651 (2022-12-16), s 652 (2014-09-22). Deposited at `../../registers/source-bundle/ny-tax-law-art22-selected.txt`, with its `.meta.json` (URL, revision date and sha256 of each page).

Nothing else is brought in. Tax years **2026 and 2027** are encoded, because those are the years whose tables are fixed in the text (s 601(a)(1)(B)(vii), (viii) and the matching paragraphs of (b) and (c)).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ny-pit.l4`, `ny-pit-seat.l4` | `ny-pit-cases.l4` | 75 written, 75 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. One `#TRACE` shows a breach (the return filed on day 120 against a 105-day deadline), with its expected result in an `-- expect:` comment, because a breached `EVALTRACE` can be asserted neither way in the stable `l4`. Every expected value was worked by hand from the text.

## Seat

**The resident individual taxpayer**: "Am I a New York resident? Must I file? By when? How much tax do I pay, and what credits do I get back?"

Provisions addressed to officials are encoded as what they mean to that person: the department recomputes on the standard deduction if it is larger (s 613); refundable credits are paid out "as an overpayment, without interest" (s 606(c-1)(2), (d)(2)).

The 2026-10-18 defaults:

- **The Act alone.** Article 22 only. No instrument sets a number these sections need, except the s 614(f) cost-of-living adjustment, which is an input (finding 2).
- **The actors the text names:** the taxpayer, the department (commissioner), the comptroller.
- **Judgments handed to others are answered conditionally:** the s 606(d)(1) "reversion event" (a certification by the commissioner of temporary and disability assistance) is an input.
- **The Act's own definitions are worked out from facts:** resident (s 605(b)(1)), New York AGI (s 612), New York taxable income (s 611), the deduction (s 613), the standard deduction (s 614), exemptions (s 616), household gross income and household (s 606(b)(3)), qualifying child for the Empire State child credit (s 606(c-1)(1-a)(D)). **Borrowed federal terms are asked as facts:** federal AGI, whether a federal return is required, filing status, the dependants under IRC s 151(c), the federal earned income credit (IRC s 32), the part of social security included under IRC s 86.
- **One case:** one return for one tax year.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** accounting periods and methods (s 605(a)), s 601-a's indexing machinery (its effect is an input), administration.

## Regulative rules

Three, in `ny-pit.l4`:

1. `my duty to file and pay` (ss 651(a), 652(a)): the taxpayer MUST make and file the return, and MUST pay the tax due, each WITHIN the days from 31 December to 15 April (105 days for 2026), joined by RAND, each with `LEST BREACH ... BECAUSE`.
2. `the department's duty to recompute on the standard deduction` (s 613): where the elected itemized deduction is smaller, the department MUST recompute and notify (no time is set).
3. `the comptroller's duty to pay my excess credit` (s 606(c-1)(2), (d)(2)): where refundable credits exceed the tax, the comptroller MUST pay the excess as an overpayment (no time is set).

The s 652(b) deadline for a tax the commissioner computed is a date function, since "whichever is later" is a choice between two dates rather than a party's act.

## Scope

**In:** s 605(b)(1) (resident individual), s 651(a)(1) (resident filing requirement), ss 651(a) and 652(a) (due date and payment), s 652(b) (commissioner-computed tax), s 612(a) with (c)(3), (3-a), (3-c) computed and all other modifications as inputs, s 611(a), s 613, s 614(a)-(f), s 616(a), s 601(a), (b), (c) paragraph (1)(B)(vii) and (viii), s 606(b) (household credit), s 606(c-1)(1-a)(B)-(E) and (2) (Empire State child credit 2026-2027), s 606(d)(1), (2) (earned income credit).

**Out:** nonresidents and part-year residents (s 601(e), s 651(a)(3), Part III: `not covered`); resident estates and trusts; the tax table benefit recapture (s 601(d), (d-1): New York AGI over $100,000 is `not covered`); the separate tax on lump sum distributions (s 603: `not covered`); s 611(b) and s 651(b) on spouses' separate determinations beyond filing status; the itemized deduction (s 615, an input); the (3-b) disability exclusion; the (c-1)(1) credit for 2028 on and the (c-1)(4), (5) supplemental payments; s 606(d-1) enhanced EIC and every other s 606 credit (child and dependent care, real property tax circuit breaker, and so on); the tie-breakers of (c-1)(1-a)(F); the New York City and Yonkers taxes (Article 30 and others).

Read with the federal Internal Revenue Code encoding, `subjects/us/internal-revenue-code-of-1986/` (being encoded by another session on 2026-10-24): every federal figure here (AGI, filing status, the EIC, IRC s 86 social security, IRC s 151(c) dependants) is an input that encoding could supply. Cross-folder IMPORT is not possible in the stable `l4`.

## What the Article turns out to say

1. **New York starts from federal AGI** (s 612(a)) and borrows the federal filing status (ss 601, 651(b)), the dependants (s 616(a)), and the federal EIC (s 606(d)). The state rules on top are its own: the $20,000 pension subtraction from age 59½ (s 612(c)(3-a)), the full subtraction of federally taxable social security (s 612(c)(3-c)) and of New York and federal government pensions (s 612(c)(3)). Asserted.
2. **The standard deduction in the text is not the one in force.** Section 614 states $7,500 / $15,000 / $10,500 / $7,500 / $3,000, but s 614(f) says that from 2018 these are "adjusted by the cost of living adjustment prescribed in section six hundred one-a ... for tax years two thousand thirteen through two thousand seventeen". Section 601-a leaves the computation to the commissioner and rounds each increase down to a multiple of $50; the adjusted amounts appear nowhere in the deposited text. The increase is therefore an input. The cases use hypothetical increases (500, 700, 1,050) and the unadjusted amounts. Asserted.
3. **Section 614(e) read literally would give every resident $3,000.** It applies to "a resident individual whose federal exemption amount is zero". The federal exemption amount has been zero for everyone since tax year 2018 under IRC s 151(d)(5) (unverified (general knowledge); the IRC deposit should confirm it). Section 614(a) separately excludes an individual "claimed as a dependent by another New York state taxpayer", so the encoding reads (e) as the dependant's deduction. This is an interpretive choice, not tested against any ruling. Asserted as encoded.
4. **The taxpayer and spouse get no New York exemption.** Section 616(a) allows $1,000 only "for each exemption for which he is entitled to a deduction ... under section one hundred fifty-one(c)", which is the dependants' subsection. Asserted.
5. **The 2026 and 2027 rate cuts are in the text, and so is their end.** For 2026 the bottom rate is 3.90% (s 601(c)(1)(B)(vii)); for 2027 to 2032 it is 3.80% (viii); from 2033 (ix) the table keeps 3.80% at the bottom, but the top rates above $2,155,350 (joint) return to 8.82%. Asserted for 2026 and 2027.
6. **The printed tax figures are rounded.** At the top of the 3.90% row, $8,500 gives $331.50, while the next row starts from "$332 plus". The encoding computes from each row as printed, so the step at a row boundary is the rounding, never more than 50 cents. Asserted ($8,500 = $331.50).
7. **The recapture starts at $100,000 of New York AGI at the earliest.** Every s 601(d-1) fraction has a numerator of the excess of New York AGI over at least $100,000. Section 601-a(b)(2) also indexed "the dollar amount in the numerator of the fractions in subsection (d)" for 2013-2017, so the real starting point may be higher; the encoding stops at $100,000 to be safe. Asserted.
8. **The Empire State child credit for 2026 and 2027 is a flat $1,000 or $500 a child, and refundable.** It is $1,000 for each qualifying child aged three or younger and $500 for each aged four to sixteen (s 606(c-1)(1-a)(B)). It is reduced by $16.50 "for each one thousand dollars" of federal AGI over $110,000 (joint), $75,000 (single, head of household, surviving spouse) or $55,000 (married filing separately). The encoding reads "each one thousand dollars" as each whole $1,000; a reading that counts a part of $1,000 would differ by at most $16.50. The excess is refunded without interest ((c-1)(2)). Asserted.
9. **"Qualified surving spouse"** is misspelled in s 606(c-1)(1-a)(C)(ii); the encoding takes it as surviving spouse. Asserted (the surviving-spouse threshold is $75,000).
10. **The New York EIC is 30% of the federal EIC less the household credit** (s 606(d)(1)), and the excess over tax is refunded ((d)(2)). The rate falls to 20% from a "reversion event" certified by the OTDA commissioner if federal TANF funding is materially cut. Asserted.
11. **Household credit for a married couple filing separately.** Household gross income is the couple's combined federal AGI "irrespective of whether joint or separate New York income tax returns are filed", and the separate filer gets one-half (s 606(b)(3)(C)). The table's "number of exemptions ... (or in the case of a husband and wife, taxpayers)" is read as counting both spouses. Interpretive. Asserted as encoded.
12. **An extension of time to file does not extend the time to pay** (s 652(a): "determined without regard to any extension of time for filing the return"). Asserted (the due date takes no extension).
13. **From 2028 the Empire State child credit returns to s 606(c-1)(1)**, which is 33% of the federal child tax credit under IRC s 24 "as it existed immediately prior to the enactment of Public Law 115-97", or $100 a child if greater. That needs a pre-2018 IRC s 24 computation and is not encoded.

## Access

The section pages answered `curl` with HTTP 200 under the honest User-Agent. A Python `urllib` client with the same User-Agent got HTTP 403 from Cloudflare. That is a client-fingerprint refusal, not a challenge; no other User-Agent was tried. The Open Legislation API host timed out and was not used. See `SOURCE-LICENSE.md`.

## What would need doing before this is worth relying on

- **The s 614(f) adjusted standard deductions**, from a deposited Department of Taxation and Finance publication (for example the IT-201 instructions), so they need not be inputs.
- **The recapture (s 601(d-1))**, to cover New York AGI over $100,000.
- **Nonresidents and part-year residents** (s 601(e), Part III), and s 615 itemized deductions.
- **The federal inputs** from the IRC encoding, once one exists.
- **An independent test pass**, and a check of findings 3, 8 and 11 against Department guidance or rulings (none were read).
