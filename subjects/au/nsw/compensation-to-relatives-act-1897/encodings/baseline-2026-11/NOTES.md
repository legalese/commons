# Compensation to Relatives Act 1897 (NSW) -- baseline encoding, the relative of the person who died

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 15 June 2018). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the relative's bar
while the executor has six months, s 6B; the plaintiff's particulars, s 6), each run by `EVALTRACE` inside an exported
question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No
pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The whole operative Act (ss 3-8) is encoded. The
time limit for the action is not in this Act: it is in the Limitation Act 1969 (NSW), a separate subject
(`subjects/au/nsw/limitation-act-1969/`). Caps and limits on damages for a death come from other Acts (civil liability,
motor accidents, workers compensation) and are not here.

## Edition

- **Act:** Compensation to Relatives Act 1897 No 31, corpus document `nsw_legislation:2018-06-15/act-1897-031` (in force
  15 June 2018), deposited at `../../registers/source-bundle/act-1897-031.txt` (sha256 e3e85545...6a625f as committed),
  taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot
  challenge. Not the authorised text.
- **Not deposited:** the Property (Relationships) Legislation Amendment Act 1999 (s 8), the Interpretation Act 1987
  s 21C (de facto partner), the Probate and Administration Act 1898 (administrator), and the pension Acts of s 3(3)(c).
  What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cra-dates.l4` | 0 | 0 | 0 | 0 |
| `cra-claims.l4` | 0 | 0 | 0 | 0 |
| `cra-cases.l4` | 0 | 0 | 77 | 77 |

Every expected value was worked by hand from the text, with the edges: the last day of the six months after the death
and the day after (s 6B), across a short February and a year end; no executor; an action already brought (s 5);
particulars on the day of the statement of claim, the day after and the day before (s 6); each relationship in ss 4 and
7, a de facto partner each side of s 8, and a relationship outside the list; each limb of s 3(1), with a serious
indictable offence and a dead wrongdoer; each s 3(2) cost, reasonable and not; each s 3(3) sum; each condition of
s 6A(2); unrecovered costs equal to, and one dollar over, the amount recovered; shares of 0, 100 and 101 per cent.

## Seat

**The relative**: the spouse (legally married or de facto), brother, sister, half-brother, half-sister, parent or child
(as s 7 widens "parent" and "child") of a person whose death was caused by a wrongful act, neglect or default, for whose
benefit the action is brought. Every exported question is one that person would ask ("Is someone liable for my
relative's death?", "Can I claim?", "Can I bring the action myself, and from when?", "Have I given the defendant the
particulars?", "Can the funeral and headstone costs be recovered?", "Will this insurance or super be taken into
account?", "What happens to a payment into court?", "How much do I receive?"). The executor or administrator, who
normally brings the action, is not given a seat of their own: the Act puts no duty or liability on them beyond what a
relative bringing the action under s 6B meets (s 6, encoded from the seat of whoever is "the plaintiff on the record").
The defendant meets the same rules from the other side; a defendant seat could be added. Officials (the court, the jury)
get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets no numbers except the six months
  in s 6B.
- **The actors the text names.** Followed: the executor or administrator, the persons for whose benefit the action is
  brought, the plaintiff on the record, the defendant, the jury, the judge (s 6D), the wrongdoer and the wrongdoer's
  executor (s 6C).
- **Judgments answered conditionally.** Followed: whether the death was caused by a wrongful act and whether the dead
  person could have sued (the general law of torts), reasonableness of funeral and headstone costs, the jury's view of
  sufficiency (s 6A), and the shares the jury directs (s 4(1)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 7's "parent", "child", "spouse", "executor"
  and "administrator" are worked out or glossed; "de facto partner" (Interpretation Act 1987 s 21C), "in loco parentis"
  and "replacing" (s 3(3)(c)) are asked.
- **One case.** One death, one action (s 5).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (the cause of action; funeral, cremation and headstone costs; sums not taken into account); s 4 (who brings
the action and for whom; more than one spouse; division of the amount recovered); s 5 (one action); s 6 (particulars);
s 6A (payment into court); s 6B (a relative's own action); s 6C (survival against the wrongdoer's estate; damages paid
in the order of the wrongdoer's debts, as a comment); s 6D (judge without jury); s 6E (application: in comments, since no
fact under it changes an answer, fork F7); s 7 (definitions); s 8 (past events and the 1999 amendments).

**Out, and why:** s 1 (name), s 2 and the Schedule (repeal of an 1847 Act): machinery. s 6E(2) (actions commenced
before or after the 1928 amending Act): spent. The amount of damages itself is the jury's ("such damages as they may
think proportioned to the injury"), not computed. The limitation period (Limitation Act 1969) and the caps and
deductions in other Acts are separate subjects.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4(1) "for the benefit of the spouse, brother, sister, half-brother, half-sister, parent, and child" --
  `the action is for the benefit of` (used by `Can I claim for my relative's death` and `Can I bring the action myself`)
  -- a relationship outside the list (a former spouse, a step-sibling, an aunt, a cousin, a fiance) answers `NOTHING`,
  because the list is not closed with "only" -- the list is exhaustive, as it is usually read, answering `JUST FALSE`.
- **F2** s 8 -- `the action is for the benefit of` -- the "amendments made ... by the Property (Relationships)
  Legislation Amendment Act 1999" are read as those that brought de facto partners in; a de facto partner whose relative
  was killed by an act before they took effect answers `JUST FALSE` (a flat "do not operate to confer") -- s 8 reaches
  only de facto partners within the 1999 definition, and a de facto partner brought in by a later amendment (the present
  s 7(4)(b), pointing to Interpretation Act s 21C) is outside s 8.
- **F3** s 6A(3) "except under the order of a judge" -- `Can money paid into court be paid out to me` -- with an order,
  `JUST TRUE` (as far as the order goes) -- `NOTHING`, the order and not the Act deciding.
- **F4** s 3(3)(c) "any Act ... amending or replacing any such Act" -- `Will this money be taken into account` -- whether
  a modern pension Act replaces a listed one is asked as a fact -- worked out here (not possible without the pension
  Acts' histories, which are not deposited).
- **F5** s 6B(1) "within six months after the death" -- `the last day of the six months after`, `From what day may I
  bring the action myself`, `Can I bring the action myself` -- the six months end on the same day of the month six months
  after the death, or that month's last day where shorter (31 August -> end of February); the executor has the whole of
  that last day and a relative may sue from the next day -- the Interpretation Act 1987's counting rules (not deposited)
  might give another end day in a short month.
- **F6** s 6 "together with the declaration" -- `Have I delivered the section 6 particulars` -- particulars delivered on
  the same day count, and those delivered earlier count too (they are with the defendant when the declaration arrives);
  a later day does not -- earlier delivery is not "together with".
- **F7** s 6E(1), (3) -- `Is someone liable for my relative's death` -- where the matter arose, anyone's nationality and
  whether the wrongdoer is the Crown are not asked, because the Act applies in every case -- ask them, to show the Act's
  reach.
- **F8** s 3(2) "reasonable expenses ... may be recovered" -- `Can this funeral or headstone cost be recovered` -- a cost
  the court finds unreasonable, or another kind of cost, answers `NOTHING` (a grant limited in its own words) -- `JUST
  FALSE` for an unreasonable cost.
- **F9** s 4(1) "after deducting the costs not recovered from the defendant" -- `How much is left to divide among the
  relatives`, `How much do I receive` -- unrecovered costs larger than the amount recovered answer `NOTHING` (the Act is
  silent on the shortfall) -- zero to divide.
- **F10** s 6B(1) with s 5 -- `Can I bring the action myself` -- once an action has been brought (by the executor at any
  time, or by another relative), a relative cannot bring another (`JUST FALSE`) -- s 6B lets a relative sue after six
  months even if the executor sues later, the two actions then merging.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 3(1) | the wrongdoer | liability to an action | `Is someone liable for my relative's death` |
| s 4(1), 6B(1) | the executor or administrator; then the relatives | power to sue; the relatives' power arises after six months or with no executor | SHANT rule (absent power modelled as a bar) |
| s 5 | everyone | disability: no second action | `Can I bring the action myself` |
| s 6 | the plaintiff on the record | duty with a deadline (together with the declaration) | MUST rule, WITHIN 0 |
| s 6A(1) | the defendant | privilege to pay into court in one sum | comment |
| s 6A(2) | the defendant | right to the verdict on the sufficiency issue | `Does the defendant win the issue of the payment into court` |
| s 6A(3) | the relatives | disability: no payment out without a judge's order | `Can money paid into court be paid out to me` |

## What the Act turns out to say

1. **The Act has no time limit of its own.** Apart from the executor's six months in s 6B, it sets no deadline for the
   claim; the limitation period is in the Limitation Act 1969. A relative reading this Act alone would not learn when the
   claim is barred.
2. **The beneficiary list is closed in practice but not in words.** s 4(1) names the beneficiaries without "only", and
   s 7 widens "parent" and "child" with "include". Step-siblings, former spouses and other relatives are not named.
   Under the corpus rulings this is `NOTHING` (fork F1); asserted.
3. **s 8 may be out of step with s 7(4).** s 8 speaks of the 1999 amendments, but s 7(4)(b) now points to the
   Interpretation Act 1987 s 21C, which suggests a later amendment rewrote the definition of spouse (not checked: the
   deposited text has no history notes). Whether s 8 still bars a de facto partner's claim for an act before the 1999
   amendments took effect, when the right now comes through later wording, is open. Fork F2; asserted on the reading
   taken.
4. **s 3(3)(c) names five pension Acts from 1908 to 1945**, all long repealed. Whether today's pensions (for example
   under the Social Security Act 1991 or the Veterans' Entitlements Act 1986) are paid under an Act "replacing" one of
   them is a real question the Act does not answer. Fork F4.
5. **The machinery is nineteenth-century.** "Declaration", "attorney", "payment into court", "verdict" and "British
   subject" (s 6E(1)) are kept by the Act; s 7(1) maps "declaration" onto any statement of the cause of action and s 6D
   maps the jury onto a judge, but "payment into court" (s 6A) has no modern gloss in the Act. The encoding uses the
   Act's words.
6. **s 6 has no consequence.** The plaintiff "shall be required" to deliver particulars together with the declaration,
   but the Act says nothing about what happens if they are late or incomplete. The regulative rule's `LEST BREACH` marks
   the failure; the consequence is for the court's rules.
7. **s 6B and s 5 can race.** After six months a relative may sue; s 5 allows only one action. If the executor sues on
   the same day as a relative, or later, the Act does not say which action lies. Fork F10.
8. **Shares and costs.** s 4(1) deducts "the costs not recovered from the defendant" before division, but says nothing
   where they exceed the recovery. Fork F9; asserted (`NOTHING`).

## Questions (exported)

`cra-claims.l4` (11), in the Act's order: `Is someone liable for my relative's death` (ss 3(1), 6C(1)), `Can I claim for
my relative's death` (ss 3(1), 4, 7, 8), `From what day may I bring the action myself` (s 6B(1)), `Can I bring the
action myself` (ss 4(1), 5, 6B, with the SHANT rule), `Have I delivered the section 6 particulars` (ss 6, 6B(2), 7(1),
with the MUST rule), `Can this funeral or headstone cost be recovered` (s 3(2)), `Will this money be taken into account`
(s 3(3)), `Does the defendant win the issue of the payment into court` (ss 6A(2), 6D), `Can money paid into court be
paid out to me` (s 6A(3)), `How much is left to divide among the relatives` (s 4(1)), `How much do I receive` (ss 4(1),
6D).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Check the amendment history of s 7(4) and s 8 (finding 3).
- Have a lawyer review the forks, especially F1 (the beneficiary list), F2 (s 8) and F10 (s 6B and s 5).
- Link the encoding to the Limitation Act 1969 baseline for the time limit, and to the civil liability and motor
  accidents encodings for damages.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
