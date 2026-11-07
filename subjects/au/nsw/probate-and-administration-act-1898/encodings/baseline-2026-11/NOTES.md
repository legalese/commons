# Probate and Administration Act 1898 (NSW) -- baseline encoding, the person with a claim on a deceased estate

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 28 September 2020). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Six regulative rules (the executor's three
months to prove or renounce, s 75(1)(a); the bar on distributing free of claims before six months and the notice's time,
s 92(1); the claimant's three months to take proceedings, s 93(1); the two months to serve process on the NSW Trustee or
a trustee company, s 93(3), (4); the executor's month after the time fixed and month after the Registrar's notice to file
accounts, s 87(1), (2)), each run by `EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a person with a claim
on an estate meets. The Act is now mostly the machinery of grants: the claims a family member most often brings
(family provision, and the shares on intestacy) are in the Succession Act 2006 (NSW), a separate subject
(`subjects/au/nsw/succession-act-2006/`), and are not here.

## Edition

- **Act:** Probate and Administration Act 1898 No 13, corpus document `nsw_legislation:2020-09-28/act-1898-013` (in
  force 28 September 2020), deposited at `../../registers/source-bundle/act-1898-013.txt` (sha256 d9f1dd60...bc0561e2
  as committed), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Probate and Administration Regulation (a rate under s 84A(1) and an amount under s 101 may be
  prescribed; the Act's own figures are used, and a prescribed figure would change the answers); the Succession Act 2006
  provisions s 92(2) cites; the Births, Deaths and Marriages Registration Act 1995 s 50; the penalty unit value (s 87(3)
  is answered in penalty units); the court rules that fix the time for accounts and the form of notices. What they
  decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pa-dates.l4` | 0 | 0 | 0 | 0 |
| `pa-claims.l4` | 0 | 0 | 0 | 0 |
| `pa-cases.l4` | 0 | 0 | 118 | 118 |

Every expected value was worked by hand from the text, with the edges: month ends across short Februaries and a leap
year (fork F1); the last day of each period and the day after (s 75 three months, s 92 six months and the notice's time,
s 93 three and two months, s 85(3) three years, s 87 two months); a notice of 29 and of 30 days (s 92(1)(c)); proving a
day late; a minor executor; $15,000 and one cent over (s 101); maintenance equal to and just over the share; a will rate,
a Court rate and the cash rate plus 2%; appropriation equal to and over the legacy; estate equal to and one dollar under
the debts; every class of Sch 3 Pt 2.

## Seat

**The person with a claim on the estate** of someone who has died leaving property in New South Wales: a beneficiary
under the will or on intestacy (including a legatee, a devisee and a dependant who survives), a family member who wants
the estate administered or the will proved, or a creditor of the person who died. Every exported question is one that
person would ask ("Can I be granted administration?", "The executor has done nothing: from what day can I go to the
Court?", "Can I lodge a caveat?", "Can the executor pay me maintenance now?", "From what day can the executor
distribute, and is my claim then lost?", "The executor disputes my claim: by when must I sue, and can my claim be
barred?", "Can I apply to the Court for my legacy, and at what rate does interest run?", "Can I still challenge the
accounts?", "Can the commission be paid, or reduced?", "What happens if the executor files no accounts?", "Is the
estate solvent, and in what order are the gifts used to pay the debts?"). The executor or administrator, who carries
most of the Act's duties, is not given a seat here; one could be added beside this one from the same rules. Officials
(the Court, the Registrar, district agents) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, with the Act's own figures where the
  regulation that may substitute them is not deposited: $15,000 (s 101) and 2% over the cash rate (s 84A(3)).
- **The actors the text names.** Followed: the executor, the administrator, the NSW Trustee and Guardian, trustee
  companies, the claimant, the beneficiary, the creditor, the Court, the Registrar.
- **Judgments answered conditionally.** Followed: the Court's view of fitness (s 63), of prosecution of a claim (s 93(2)),
  of a just and reasonable or excessive commission (ss 86, 86A); whether interest is payable on a legacy at all (the will
  and the general law); "wholly or substantially dependent" (s 92A) -- all inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "minor" (s 3), "spouse" including a de facto
  spouse (s 32G), "solvent" (s 46C(3)) and "relevant rate" (s 84A(3)) are worked out; "next of kin", "de facto
  relationship" (Interpretation Act 1987 s 21C) and "person interested" are asked.
- **One case.** One estate, one claimant.
- **The Act's terms, glossed.** Followed in the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In** (encoded as exported questions): ss 3 ("minor"), 32G, 63 (administration on intestacy); s 75(1) (the executor
who does not prove the will); s 42(2)(b) (14 days' notice of an application); s 101 (small estates to the Registrar);
s 144(1) (caveats); s 40B(3), (4) (grants on presumption of death); s 81B(1) (undisclosed property); s 92A(1), (2), (5)
(maintenance distributions); ss 92, 95, 40B(4) and Sch 5 cl 8 (distribution after notice; following the assets);
s 93 (disputed claims barred); s 84 (application for a legacy); s 84A (interest on legacies); s 85(3) (allowed accounts as
a release); s 86(1), (2) (commission); s 86A (reduction of commission); s 87 (accounts not filed); s 46C(2), (3) and
Sch 3 Pt 2 (solvency and the order of assets).

**Out**, and why:

- ss 1, 2, 152A, 153, 154, 155 and the First and Fifth Schedules (except Sch 5 cl 8): machinery and transitional.
- ss 30, 31 (custody and official copies of wills), 33, 40, 40A (jurisdiction), 41, 42(1), (3)-(5), 151, 152: court
  procedure with no claimant decision in it.
- ss 40C, 40D, 81, 90, 91 (a grant revoked because the person was alive; effects of revocation; indemnity for payments
  under a grant): rare, and the seat is the person presumed dead or the payer.
- ss 44-48, 61, 62 (vesting of the estate in the executor or the NSW Trustee; distribution on intestacy under the
  Succession Act Ch 4): they describe where property sits and point elsewhere; no question the claimant can act on.
- ss 46A, 46B, 46D, 46E, 52-59, 83 (assets for debts; general powers; income of settled residue; divesting land;
  dower; partition; business of an intestate; acknowledgments): estate management for the executor and the Court.
  s 53 (a spouse bound to take the value instead of partition) could be added for the spouse.
- ss 64-68 (administration bonds; surety's relief), 69-74A, 75A-80 (renunciation, minors, attorneys, administrators
  pending suit, special administrators, delegation): the administrator's and surety's seat.
- ss 81A, 85(1)-(2), (4), (5) (the executor's duties to disclose assets and file accounts): the executor's seat; they
  appear here only through s 81B, s 85(3) and s 87.
- s 82 (creditors in equal degree; no retainer): in comments only, because of finding 3.
- ss 89, 94, 97 (orders for distribution; lease liabilities; deemed residence): the executor's or a landlord's seat.
- Divisions 4 (apart from s 101), 5 (resealing foreign grants) and 7 (apart from s 144): registry procedure.
- Sch 3 Pt 1 (insolvent estates): it hands the order to the law of bankruptcy, not deposited.

## Forks (the reading taken, and the other)

Each line: provision -- function -- answer taken -- other reading.

- **F1** ss 75(1)(a), 85(3), 87, 92(1)(a), 93 periods of months -- `plus months` (all date questions) -- the period ends on
  the same day of the month that many months later, or that month's last day where shorter; the period includes that
  whole day -- the Interpretation Act 1987's counting rules (not deposited) might give another end day in a short month.
- **F2** s 63 "not being minors" -- `Can I be granted administration` -- read over the whole list, (d) included: a
  minor answers `JUST FALSE` -- "not being minors" qualifies only (a)-(c).
- **F3** s 75(1)(a) -- `Can I apply because the executor has not proved the will` -- the three months run from the 18th
  birthday of an executor who was a minor at the death; an executor who proves a day late has still neglected "within
  three months", so the Court may act (`JUST TRUE`) -- proving before the application cures the neglect.
- **F4** s 75(1) "upon the application of (i) ... (ii) ... (iii)" -- same -- someone outside the list answers `NOTHING`
  (a grant limited in its own wording) -- `JUST FALSE`.
- **F5** s 92(1)(b)-(d) "after the expiration of a specified time"; "not less than 30 days after the notice is given" --
  `From what day can the executor distribute under section 92`, `What section 92 means for my claim` -- the notice's time
  ends on a day it names, at least 30 days after the day of notice, and has expired from the next day; a notice of fewer
  days cannot support a s 92 distribution at all (`NOTHING` date; unprotected) -- the 30 days counted inclusively, or
  the time expiring at the start of its last day.
- **F6** s 92(2) "or the distribution was not made in the circumstances described in ... section 28 ... 125 ... 126 ...
  Part 4.4 of the Succession Act 2006" -- `What section 92 means for my claim` -- read as reaching only claims under those
  Succession Act provisions, which lose the protection where the distribution did not meet that provision's own conditions
  -- the literal reading (finding 2), under which nearly every distribution is "not made in those circumstances" and no
  executor is protected.
- **F7** s 84A(1) "unless the will or instrument otherwise provides, or the Court otherwise orders" -- `What rate of
  interest is payable on my legacy` -- where both set a rate, the Court's order is taken -- the will's rate.
- **F8** s 85(3) -- `Can I still challenge the allowed accounts`, `From what day do allowed accounts operate as a
  release` -- before the release the order is only prima facie evidence, so a challenge answers `JUST TRUE`; the release
  operates from the day after three years -- from the third anniversary itself.
- **F9** s 87(1), (2) -- `What can happen if the executor files no accounts` -- an executor who files late but before any
  Registrar's notice still answers "the Registrar must notify" (the neglect "within one month" has happened) -- late
  filing ends s 87.
- **F10** s 93(2), (3) -- `Can my disputed claim be barred` -- s 93(2) applies after the three months whether or not
  proceedings were commenced in time (the notice calls on the claimant "to take proceedings ... and to prosecute"); the
  s 93(3), (4) route applies only where proceedings were not commenced within the three months, and is met only by
  serving process within the two months (commencing without serving is barred) -- commencing within the two months is
  enough.
- **F11** s 46C(3) "sufficient ... for the payment in full of the debts and liabilities" -- `Is the estate solvent` -- the
  estate's value at least the debts and liabilities -- funeral, testamentary and administration expenses counted too.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 63 | spouse, next of kin, any fit person | eligibility for a discretionary grant | `Can I be granted administration` |
| s 75(1)(a) | the executor named | duty with a deadline (3 months) | MUST rule |
| s 75(1) | a person interested, a creditor | power to apply | `Can I apply because the executor has not proved the will` |
| s 144(1) | any person | power, until the grant | `Can I lodge a caveat` |
| s 40B(3), (4) | the executor | prohibition (no leave; caveat) | `Can the estate presumed dead be distributed` |
| s 81B(1) | the executor | prohibition | `Can the executor complete the transfer to me` |
| s 92A | the executor | privilege to pay maintenance early | `Can the executor pay me maintenance now` |
| s 92(1), (2) | the executor | immunity after a conforming distribution | SHANT rule (the bar before the first protected day) |
| s 95 | the claimant | right to follow assets preserved | part of `What section 92 means for my claim` |
| s 93(1), (2) | the claimant | duty (on notice) to take proceedings in 3 months; liability to a bar | MUST rule |
| s 93(3), (4) | the claimant | duty to serve process in 2 months; claim extinguished | MUST rule |
| s 84 | the legatee or devisee | power to apply after a written request | `Can I apply to the Court for my legacy` |
| s 84A | the legatee | right to interest at the relevant rate | `What rate of interest is payable on my legacy` |
| s 85(3) | the executor | immunity (release) after 3 years | `Can I still challenge the allowed accounts` |
| s 86(2) | the executor | disability: no commission | `Can the executor be paid commission` |
| s 87 | the executor | duty with deadlines; liability to contempt or a fine | two MUST rules |

## What the Act turns out to say

1. **The Act no longer holds the main family claims.** Shares on intestacy (s 62(2)) and family provision (the note to
   s 42) are in the Succession Act 2006. Yet s 92A(3) still speaks of "an order under the Family Provision Act 1982",
   an Act the Succession Act replaced: in this 2020 text the cross-reference is stale (a possible drafting error, unless
   a savings provision keeps it alive).
2. **s 92(2) read literally protects almost no one.** It removes the protection where "the distribution was not made in
   the circumstances described in" Succession Act ss 28(2)(a) or (b), 125, 126 or Part 4.4. Nearly every distribution
   is "not made in" those (claim-specific) circumstances. The encoding reads the words as reaching only claims under
   those provisions (fork F6). A lawyer should confirm.
3. **s 82(1) and s 46C(1) pull apart.** s 82(1) treats "all the creditors of every description" as "standing in equal
   degree", "any statute or law to the contrary notwithstanding"; s 46C(1) (added in 1930) administers an insolvent
   estate by the bankruptcy rules, with funeral, testamentary and administration expenses first (Sch 3 Pt 1). The later,
   specific provision is taken to govern insolvent estates, and s 82 is left in comments.
4. **s 92(1)(c) mixes a period and a point.** "The time specified in the notice is not less than 30 days after the
   notice is given" reads the "time" as a moment; the notice in (b) specifies a period. Fork F5.
5. **The figures may have moved.** s 101's $15,000 and s 84A's rate can be replaced by regulation; the regulation is not
   deposited, so the answers use the Act's figures.
6. **s 87(3) fines in penalty units** whose dollar value is set in another Act (not deposited): answered as 20 units.
7. **s 63 gives no order among spouse and next of kin.** It names who is eligible; any priority between them comes from
   the rules or the Court, not this Act.
8. **The text is the version of 28 September 2020.** Amendments since are missing.

## Before relying on it

- Check the current text on legislation.nsw.gov.au, and deposit the Probate and Administration Regulation for ss 84A and
  101.
- A lawyer's view on forks F2, F5, F6 and F10, and on findings 1-3.
- An independent test pass, and an executor seat beside this one.
