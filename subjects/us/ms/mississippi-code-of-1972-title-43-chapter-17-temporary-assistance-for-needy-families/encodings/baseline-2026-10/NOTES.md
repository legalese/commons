# Mississippi TANF (Miss. Code s 43-17-5) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `mstanf.l4`: the section's terms (the dependent child's budget, the family cap, the denial categories, work activity, exemptions, sanctions) and the exported questions for the parent or caretaker relative, each calling those rules. Three duties with deadlines are regulative rules: notifying a child's 30-day absence within the five-day period (subs. (3)(h)); the job search skills workshop within 60 days of applying (subs. (6)(b)); vaccinations within 30 days of notice, failing which the Department must impose the 25% sanction (subs. (5)). One case file, `mstanf-cases.l4`; expected values worked out by hand.

There was no earlier encoding; this is a new subject.

## Edition and source

The official Code (LexisNexis) was not used (see `../../SOURCE-LICENSE.md`). s 43-17-5 is taken from **House Bill 121 of the 2026 Regular Session, as introduced** (billstatus.ls.state.ms.us), deposited 2026-10-24. The bill set out the whole section "as amended", proposing to double the monthly amounts in subsection (1); it died in committee on 3 February 2026. In its text the struck words are the law in force and the underlined words the failed proposal; the encoding uses the struck amounts. The Legislature's code-section indexes for s 43-17-5 list 19 bills in 2025 and 19 in 2026, all of which died; so the section as reprinted in January 2026 appears to be current. The indexes are the Legislature's bill record, not the Code.

The Department of Human Services' regulations and the 1988 standard of need, which fix the actual payment within the maximums, are not deposited.

## Checks

- `mstanf-cases.l4`: 37 assertions written, 37 satisfied, 0 errors, 0 warnings. One `#TRACE` (no notice of a child's absence by day 5) prints `BREACH` by the parent or caretaker relative, as its `-- expect:` comment says.
- `mstanf.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The parent or caretaker relative** who applies for, or receives, TANF: "How much can my family get? Will we be denied? Am I exempt from work? How many hours? What happens if I miss a requirement?"

Defaults: the section alone (the Department's regulations not deposited, the grant before sanctions an input); the actors it names (the parent or caretaker relative, the recipient, the Department, the county department); judgments left to the Department (work eligibility, good cause, waiver of the family cap, physician's certificates) asked as facts; one case is one family.

## Scope

In: s 43-17-5(1), (3), (4)(f), (5), (6)(a) to (e).

Out: subsections (2) (electronic benefits), (4)(a) to (e) in detail (who must attend school), (6)(f), (g), (7) to (14); s 43-17-6 (drug testing, asked as part of one fact); fair hearings.

## Links

TANF is Title IV-A of the Social Security Act (`subjects/us/social-security-act/`, 42 U.S.C. 601-619); the 60-month limit in subs. (3)(b) mirrors 42 U.S.C. 608(a)(7). SSI recipients are denied (subs. (3)(n)); SSI is Title XVI.

## What the Act turns out to say

1. **$200, $36, $24.** The most a family's budget may receive is $200 for the first member, $36 for the second and $24 for each additional member: $260 a month for a parent and two children. Proposals in 2025 (HB 134, HB 568, SB 2688) and 2026 (HB 121) to raise the amounts all died. Asserted.
2. **The actual amount is not in the statute.** The county department fixes it "with due regard to the resources and necessary expenditures of the family", under the Department's rules, at not "less than the Standard of Need in effect for 1988". Neither figure is deposited, so the encoding answers only the maximum.
3. **Two 25% sanctions.** Subs. (4)(f) cuts "twenty-five percent (25%) of the family grant" for a child aged 6 to 12 who misses school, and subs. (5) sanctions "the family's TANF benefits by twenty-five percent (25%)" for missing vaccinations; the text does not say whether two such sanctions are each 25% of the original grant or compound. The encoding takes each of the grant before sanctions ($260 less 65 less 65 = 130).
4. **The 24-month work rule and exemptions.** Subs. (3)(j) denies TANF to a parent who "has not engaged in an allowable work activity ... once the parent or caretaker relative has received TANF assistance under the program for twenty-four (24) months"; the exemptions are in subs. (6)(b). The encoding asks whether the person is in work activity "or exempt", reading (3)(j) with (6)(b); read alone, (3)(j) has no exemption.
5. **The five-day period.** Subs. (3)(h) runs "the five-day period that begins with the date that it becomes clear" the child will be absent for 30 days, so that date is day one and the period ends on the fifth day (day 4 counted from 0). Asserted.
6. **No time for the vaccination sanction.** Subs. (5) says the Department "shall sanction ... for the next payment month", a month the text does not date; the regulative rule gives the Department's duty no deadline.
7. **The family cap.** Subs. (1) limits benefits to children "existing or conceived at the time the caretaker relative initially applies", unless the Department waives it or the child is born after twelve consecutive months off TANF. Asserted.

## Before relying on it

- Deposit the Department of Human Services' TANF regulations (the standard of need and payment rules) and s 43-17-6.
- Confirm with the Code or the Department that s 43-17-5 has not been amended since January 2026.
- An independent test pass.
