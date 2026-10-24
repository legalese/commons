# Mississippi individual income tax (Title 27, ch. 7) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `msit.l4`: the statute's terms (taxable income, the rate on taxable income over $10,000, the personal and additional exemptions, the optional standard deduction) and the exported questions, each calling those rules. One case file, `msit-cases.l4`; expected values worked out by hand. **No regulative rule:** the deposited sections state no duty with a deadline for the taxpayer (the filing duty and due date are in ss 27-7-41 and 27-7-50, not deposited).

There was no earlier encoding of this subject.

## Edition and sources

The official Mississippi Code of 1972 is published under contract by LexisNexis; its public access platform presented a CAPTCHA at indexing (2026-09-23), and the Secretary of State asserts copyright in "the laws of Mississippi" (see `../../SOURCE-LICENSE.md`). It was not used. The text was taken from the Legislature's own bill documents (billstatus.ls.state.ms.us), deposited 2026-10-24:

- **s 27-7-5 (rates)**: House Bill 1 of 2025, the "Build Up Mississippi Act", as sent to the Governor and approved on 27 March 2025. Section 1 amends s 27-7-5; Section 2 (uncodified in the bill text) sets the reductions from 2031.
- **s 27-7-21 (exemptions)**: as brought forward unchanged by House Bill 1996 of 2026 (died in committee).
- **s 27-7-17 (deductions)**: as brought forward unchanged by House Bill 866 of 2026 (died in committee).

A bill that brings a section forward reprints it as it stood when the bill was introduced (January 2026). The Legislature's code-section indexes for 2025 and 2026 list no enacted amendment of these sections since; see finding 4 for the limits of that check.

## Checks

- `msit-cases.l4`: 29 assertions written, 29 satisfied, 0 errors, 0 warnings.
- `msit.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The individual Mississippi resident**, or the married couple living together: "How much Mississippi income tax do I owe? What exemptions and standard deduction may I take?"

Defaults: the Act with its own figures; the actors it names (the taxpayer, the spouse, the commissioner, the Legislative Budget Office); judgments and figures left to others (whether the Working Cash-Stabilization Reserve Fund is full, the revenue and appropriation figures of HB 1 Section 2) answered conditionally, as the reduction in effect, asked as a fact; borrowed terms (gross income, business deductions, itemized deductions, IRC s 152 dependants) asked as facts; one case is one return for one calendar year.

## Scope

In: s 27-7-5(1) as amended by HB 1 (2025) and HB 1 Section 2; s 27-7-21(a) to (h); s 27-7-17(3)(b).

Out: nonresidents and part-year residents (ss 27-7-21(i), 27-7-17(3)(c)); years before 2024; fiscal years spanning a rate change (s 27-7-5(4)); business deductions and itemized deductions in detail (s 27-7-17(1), (2), (3)(a)); gross income (s 27-7-15, not deposited); credits; withholding; filing.

## Link to the federal encoding

Dependants are those under IRC s 152 (s 27-7-21(e)), and s 27-7-17 cites the Internal Revenue Code throughout: `subjects/us/internal-revenue-code-of-1986/`. Inputs here.

## What the Act turns out to say

1. **One rate above $10,000.** Since 2023 nothing is levied on the first $10,000 of taxable income (s 27-7-5(1)(a)(i)6 and (1)(b)(i)); everything above is taxed at one rate, falling from 4.7% (2024) to 4.4% (2025), 4% (2026), 3.75% (2027), 3.5% (2028), 3.25% (2029) and 3% (2030 on). Asserted for every year.
2. **The 2031 reductions are ambiguous in two ways.** HB 1 Section 2(2) says "the tax imposed under Section 27-7-5(b)(ii)" (the paragraph is s 27-7-5(1)(b)(ii); the subsection number is missing) "shall be reduced by" 0.2%, 0.25% or 0.3%. Whether that is percentage points off the rate (3% to 2.8%) or a percentage of the tax (3% to 2.994%) is not said. The bill's title speaks of reducing "the tax on all taxable income", and Section 2(4) eliminates the tax when the rate reaches 0%, which fits percentage points; the encoding reads it so and asks the total reduction in effect as a fact.
3. **The repeal clause is gone.** HB 1 deleted the old statement that the Legislature would consider further cuts and that the individual income tax "shall stand repealed" if the rate reached zero; Section 2(4) now provides that the tax "shall be eliminated" at 0%.
4. **How current the reprints are rests on the Legislature's own indexes.** Its code-section index for s 27-7-5 in 2025 lists HB 1 ("Approved by Governor") and two bills that died; for 2026, three bills that died. For ss 27-7-17 and 27-7-21 there is no 2025 index (no bill touched them) and the 2026 indexes list only the bills that died, including the two whose reprints are used. That is good evidence that the reprints are current, but it is the Legislature's bill record, not the Code.
5. **Head of family and the first dependant.** s 27-7-21(d) gives the head of family $9,500 and the $1,500 dependant exemption "only to the extent of dependents in excess of the one (1) dependent needed to qualify". Asserted.
6. **The Internal Revenue Code of 1954.** s 27-7-21(d), (e) still define "head of family" and "dependent" by reference to "the Internal Revenue Code of 1954, as amended", a name the federal code has not carried since 1986.
7. **Conversion.** The Legislature's HTML marks deletions and insertions with hidden struck and underlined text. Where an underline runs across paragraphs, the deposit may not label all of the new text as inserted (for example parts of HB 1 Section 2(1)); Section 2 is new in its entirety. The struck text that HB 1 removed is not encoded.

## Before relying on it

- Deposit ss 27-7-15 (gross income), 27-7-41 and 27-7-50 (filing) from the Legislature's documents or the Code, if the owner accepts the source.
- Confirm with the Department of Revenue that the 2031 reduction is in percentage points.
- An independent test pass.
