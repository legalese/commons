# Choice of Law (Limitation Periods) Act 1993 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 8 January 2010). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). One regulative rule (the other place's
limitation period, as s 5 applies it) run by `EVALTRACE` inside an exported question that takes only plain facts. No
REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The whole operative Act (ss 3-7) is encoded. The
Limitation Act 1969 (NSW), the time limits a NSW-governed claim meets, is a separate subject
(`subjects/au/nsw/limitation-act-1969/`).

## Edition

- **Act:** Choice of Law (Limitation Periods) Act 1993 No 94, corpus document `nsw_legislation:2010-01-08/act-1993-094`
  (in force 8 January 2010), deposited at `../../registers/source-bundle/act-1993-094.txt` (sha256 bbeabf57...835b7fd as
  committed), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the proclamation commencing the Act (s 2) and any proclamation declaring that the Act applies in
  relation to New Zealand (s 7(1)). Both dates are inputs. The cases use illustrative dates (commencement 1 March 1994,
  New Zealand declaration 1 July 1995) that are **not** the real ones.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `col-limitation.l4` | 0 | 0 | 0 | 0 |
| `col-cases.l4` | 0 | 0 | 55 | 55 |

Every expected value was worked by hand from the text, with the edges: proceedings instituted on the commencement day and
the day before (s 4); on the day the New Zealand declaration takes effect and the day before (s 7(2)); a declaration made
by the commencing proclamation (s 7(1)); a cause of action arising before commencement (s 4); the last day of the other
place's period, the day before and the day after, and a period running across 29 February; each limb of the s 3
definition; each place and each forum; a failed condition meeting an open one.

## Seat

**The claimant**: a person bringing a claim before a New South Wales court (or an arbitrator) where the claim is governed
by the law of another place. Every exported question is one the claimant would ask ("Does this Act apply to my
proceedings?", "Is that law a limitation law?", "Will the court apply the other place's time limit?", "Does that time
limit stop my claim?", "How must the court decide whether to extend my time?"). The duties in ss 5 and 6 are the court's;
they are encoded as what they mean for the claimant. The defendant answering the claim meets the same rules from the
other side; no second seat is written because the Act puts no duty or liability on the defendant of its own. Officials
(the court, the Minister) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the two proclamations are not deposited, so
  their dates are inputs.
- **The actors the text names.** Followed: the court (including an arbitrator), the courts of the other place, the
  Minister (s 8, out).
- **Judgments answered conditionally.** Followed: which law governs the claim (general choice-of-law rules), whether the
  court is exercising a discretion, and "as far as practicable" (s 6) are left to the court; the first two are inputs, the
  third is stated in the answer (fork F4).
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 3 "limitation law" and "court" are worked out;
  "substantive law", "State", "Territory" and the other place's period and its counting are asked.
- **One case.** One claim, in one set of proceedings.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (court, limitation law); s 4 (application to causes of action and proceedings); s 5 (limitation law as
substantive law); s 6 (discretions under a limitation law); s 7 (New Zealand), all of them.

**Out, and why:** s 1 (name); s 2 (commencement: machinery, though its date is asked as an input for s 4); s 8 (the
Minister's review and report: machinery, addressed to the Minister, and its 5-year and 12-month periods ended in the
1990s). Which law governs a claim (the "substantive law") is not in the Act at all: it is the common law of choice of law,
asked as a fact. The other place's limitation law itself (its period, its counting rules, its extension powers) is that
place's law: the last day it allows is asked as a fact.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4 "instituted before the commencement", s 7(2) "instituted ... before that declaration takes effect" --
  `Does this Act apply to my proceedings` -- proceedings instituted on that day are not "before" it, so the Act applies --
  the day itself is excluded.
- **F2** s 3 "court includes arbitrator" with ss 5, 6 "a court of the State" -- `is a court of the State` -- an arbitrator
  in an arbitration held in NSW is a court of the State; an arbitrator elsewhere answers `NOTHING` -- every arbitrator
  (wherever seated) is one, or an arbitrator is one only where NSW law governs the arbitration.
- **F3** ss 4, 7(2) "proceedings instituted" for an arbitration -- `Does this Act apply to my proceedings` -- the day the
  arbitration was commenced is used as the day proceedings were instituted -- arbitrations are not "proceedings" and ss 4,
  7(2) never exclude them.
- **F4** s 6 "as far as practicable" -- `Must the court use the discretion as that place's courts do` -- `JUST TRUE` is the
  direction, to the extent the court finds practicable -- an input for practicability, answering `JUST FALSE` where it is
  not practicable at all.
- **F5** s 5 with the other place's period -- `Does the other place's time limit stop my claim` (the s 5 rule) -- the last
  day that law allows (with any extension granted) is asked; proceedings instituted on that day are in time -- the
  period's counting worked out here (it is the other place's law, not this Act's).
- **F6** s 6 -- `Must the court use the discretion as that place's courts do` -- applied to a discretion under a listed
  place's limitation law whether or not that place's law governs the claim, as the words say -- only where s 5 brings that
  law in.
- **F7** ss 5, 6 "a place, being another State, a Territory or New Zealand" -- every s 5 and s 6 question -- a claim
  governed by NSW law or by the law of a country other than New Zealand fails the "if" and answers `JUST FALSE` ("this
  section gives no direction"), under the ruling for "if" conditions -- `NOTHING`, treating the list as the Act's scope.

## What the Act turns out to say

1. **"A court of the State" and an arbitrator.** s 3 says "court includes arbitrator", but ss 5 and 6 need "a court of the
   State". The Act never says what makes an arbitrator "of the State". Fork F2; asserted (`NOTHING` for an arbitration
   held outside NSW).
2. **Arbitrations and the application rules.** s 3 distinguishes "a proceeding on, or the arbitration of, the claim", but
   ss 4 and 7(2) speak only of "proceedings instituted". Read strictly, the transitional cut-offs would never apply to an
   arbitration. Fork F3.
3. **s 6 is wider than s 5.** s 5 brings in a place's limitation law only when that place's substantive law governs the
   claim; s 6 applies whenever a NSW court exercises a discretion under a listed place's limitation law, without that
   condition. In practice s 6 bites after s 5; read literally it is wider. Fork F6; asserted on the literal words.
4. **The Act chooses no law.** It assumes the claim is governed by another place's law and only says that place's
   limitation law goes with it. Which law governs is left entirely to the general law, so the claimant's first question
   ("which place's law governs my claim?") is an input here.
5. **"Despite section 4" in s 7(2).** s 4 excludes only proceedings instituted before commencement; s 7(2) adds a later
   cut-off for New Zealand claims. Nothing in s 4 conflicts with s 7(2), so the "despite" appears to be for caution (it
   overrides s 4's extension to earlier causes of action only so far as those proceedings were instituted before the
   declaration). Asserted: an NZ claim instituted the day before the declaration takes effect is outside the Act.
6. **No time-bound duty on the claimant.** The Act imposes no deadline on the claimant itself; the deadline comes from the
   other place's limitation law, which s 5 makes the court apply. The regulative rule models that period as a `MUST` with
   a `LEST BREACH`; jurally the claimant is under no duty but is liable to have the claim barred. The only time-bound duty
   in the Act is the Minister's review (s 8), which is out.
7. **The corpus version is dated 8 January 2010**, the last change the corpus records, and the s 7(1) wording ("published
   on the NSW legislation website") appears to come from a later general amendment on publishing proclamations (not
   checked: the history notes are not in the deposited text). Whether the New
   Zealand declaration has been made is not in the deposited text.

## Questions (exported)

`col-limitation.l4` (5), in the Act's order: `Is it a limitation law` (s 3), `Does this Act apply to my proceedings`
(ss 4, 7), `Will the court apply the other place's limitation law` (s 5), `Does the other place's time limit stop my
claim` (ss 4, 5, with the regulative rule), `Must the court use the discretion as that place's courts do` (s 6).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the commencement proclamation and any New Zealand declaration, and replace the date inputs with them.
- Have a lawyer review the forks, especially F2 and F3 (arbitrations) and F6 (the reach of s 6).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
