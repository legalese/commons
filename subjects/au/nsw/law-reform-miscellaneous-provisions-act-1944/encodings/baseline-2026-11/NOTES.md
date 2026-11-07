# Law Reform (Miscellaneous Provisions) Act 1944 (NSW) -- baseline encoding, the claimant (survival of actions)

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 7 December 2007). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The whole operative Act is encoded: it is one
section (s 2) in one Part. No regulative rule is written: the Act puts no duty with a deadline on anyone (the time
limits for a surviving claim are in the Limitation Act 1969, a separate subject at `subjects/au/nsw/limitation-act-1969/`).

## Edition

- **Act:** Law Reform (Miscellaneous Provisions) Act 1944 No 28, corpus document `nsw_legislation:2007-12-07/act-1944-028`
  (in force 7 December 2007), deposited at `../../registers/source-bundle/act-1944-028.txt` (sha256
  a22f51a5c9dfd57fb30997d037f617691b9909e1b2d556ebdc60e0d95cf6aa81 as committed), taken from the Open Australian
  Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the authorised
  text.
- **Not deposited:** the Act's commencement (1944; whether a death came after it is an input), the Compensation to
  Relatives Act 1897 text (deposited as a subject, not encoded), and s 4 of the Law Reform (Miscellaneous Provisions)
  (De Facto Relationships) Amendment Act 1984, which s 3 continues. Section 12B of the Dust Diseases Tribunal Act 1989
  is deposited under `subjects/au/nsw/dust-diseases-tribunal-act-1989/`; it was read to word the two inputs it needs,
  and is not encoded here (the stable `l4` cannot import across subjects).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lrmp-survival.l4` | 0 | 0 | 0 | 0 |
| `lrmp-cases.l4` | 0 | 0 | 60 | 60 |

Every expected value was worked by hand from the text, with the edges: each kind the s 2(1) proviso excepts, in both
directions; the proviso against the open questions (it wins); a death before commencement; no cause of action at the
death; s 2(4) with each of its two conditions failing, and asked from the estate side (where it does not apply); every
kind of damages with the death caused and not caused by the wrong; the dust-disease exception with each of its two
conditions failing, and against a head it does not touch; breach of promise to marry against every other head; every
Act s 2(5) and (6) name, and one they do not.

## Seat

**The claimant** where someone has died: either the executor or administrator (or the family member acting) for the
estate of a person who died with a claim, or a person whose claim is against someone who has died. Every exported
question is one that person would ask ("Does the claim survive the death?", "Can the estate recover this kind of
damages?", "Is my claim treated as existing against them although they died before I suffered the damage?", "Does the
estate's claim cut down the family's own claim, or rights under the motor accidents Acts?"). The person answering a
claim against an estate (the estate's representative) meets the same rules from the other side; no second seat is
written. Officials (the court) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets no numbers. The s 12B facts of the
  Dust Diseases Tribunal Act 1989 (which s 2(7) makes this section subject to) are asked as inputs.
- **The actors the text names.** Followed: the person who dies, their estate, dependants (s 2(5)).
- **Judgments answered conditionally.** Nothing in s 2 is left to anyone's judgment; whether the wrong caused the death,
  and whether a cause of action existed, are facts asked.
- **The Act's definitions worked out; borrowed terms asked.** The Act defines nothing. "Cause of action", "exemplary
  damages", "defamation", "seduction", "dust-related condition" and the rest are asked.
- **One case.** One cause of action, and one death.
- **The Act's terms with plain glosses.** Followed, in each `@desc` and in the enumerations.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 2(1) (survival, and the proviso's exceptions), s 2(2) (the damages for the estate), s 2(4) (damage at or after
the wrongdoer's death), s 2(5) (Compensation to Relatives Act 1897), s 2(6) (motor accidents Acts), s 2(7) (the dust
diseases exception, as facts). That is the whole of Part 2.

**Out, and why:** s 1 (name); s 3 (continues a savings and transitional provision of a 1984 amending Act whose text is
not deposited: machinery); s 2(3) and Part 3 (s 4) are repealed. Who is the estate's representative, how a surviving
claim is brought, and its time limit are in other Acts (Probate and Administration Act 1898, Limitation Act 1969).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 2(1) "on the death of any person after the commencement of this Act" -- `Does the claim survive the death` --
  a death before commencement answers `NOTHING` (a scope limit with no "only") -- `JUST FALSE`, as a period the text
  fixes.
- **F2** s 2(1) "causes of action subsisting against or vested in the person" -- `Does the claim survive the death` -- no
  cause of action at the death (and none deemed by s 2(4)) answers `NOTHING` -- `JUST FALSE`, there being nothing to
  survive.
- **F3** s 2(5) second limb, with s 2(1) -- `Does the claim survive the death` -- a Compensation to Relatives Act claim is
  a "cause of action" within s 2(1) both ways; s 2(5) confirms the "against" direction -- s 2(5)'s express extension of
  only the "against" part implies such a claim does not survive for a dependant's own estate.
- **F4** s 2(2) -- `Can the estate recover these damages` -- a head s 2(2) does not touch is "not cut down" (recoverable
  if the cause of action gives it) rather than "recoverable": s 2(2) only limits -- read it as granting those heads.
- **F5** s 2(2)(b) -- `Can the estate recover these damages` -- "damage to the estate flowing from a breach of promise to
  marry" asked of another kind of claim answers "this Act does not settle it" -- "not cut down", as ordinary loss to the
  estate. For a breach of promise every other head is "left out", the person classifying the loss.
- **F6** s 2(2)(c) "where the death ... has been caused by the act or omission" -- `Can the estate recover these damages`
  -- funeral expenses and other losses or gains because of a death the wrong did not cause answer "this Act does not
  settle it" -- "left out" (a failed "where" condition), though the "where" governs the exclusion, not a grant.
- **F7** s 2(7) with Dust Diseases Tribunal Act 1989 s 12B(2) -- `Can the estate recover these damages` -- only s 2(2)(d)
  is lifted, and only where the claim is for a dust-related condition and the person's own proceedings were pending
  before the Tribunal at death -- s 12B(1)'s purpose words ("whose death has been caused by a dust-related condition")
  as a further condition; it is met whenever (d) is in play here, since (d) itself needs the death caused by the wrong.

## What the Act turns out to say

1. **The proviso stops the subsection, not the claim.** s 2(1)'s proviso says "this subsection shall not apply" to
   defamation, seduction, enticement of a spouse and Property (Relationships) Act Div 2 Pt 3 claims. The Act does not
   say those claims die; it leaves them to the general law (under which personal actions die with the person). The
   encoding answers `JUST FALSE` to "does the claim survive under this Act". Asserted.
2. **s 2(4) helps only the person claiming against an estate.** It deems a cause of action "subsisting against" a person
   who died before or with the damage. It gives nothing to the estate of a person who dies before their own damage is
   suffered. Asserted (`NOTHING` from the estate side).
3. **s 2(2)(a)(ii) presupposes a shortened life.** The "lost years" are the time the person "would have survived but for
   the act or omission"; where the wrong did not cause the death there are none, but the head is excluded on its words
   whether or not the death was caused. Asserted both ways.
4. **The Acts s 2(6) names are old.** The 2007 text names the Motor Vehicles (Third Party Insurance) Act 1942, the
   Transport Accidents Compensation Act 1987 and the Motor Accidents Act 1988, all since repealed or replaced (the Motor
   Accidents Compensation Act 1999 and the Motor Accident Injuries Act 2017 are not named). Whether the current text
   names them was not checked: the official site could not be fetched. Another Act answers `NOTHING`. Asserted.
5. **s 2(5) names only dependants' rights.** It says estate rights are additional to the Compensation to Relatives Act
   dependants' rights; it says nothing about obligations against estates under that Act beyond applying the "against"
   part (fork F3).
6. **No commencement date in the text.** s 2(1) turns on a death "after the commencement of this Act", but the deposited
   text gives no date (s 1(2), presumably commencement, is repealed). It is asked as a yes/no fact.
7. **The corpus version is dated 7 December 2007.** Later amendments (if any) are missing; in particular the reference to
   s 12B of the Dust Diseases Tribunal Act 1989 and the Acts in s 2(6) should be checked against the current text.

## Questions (exported)

`lrmp-survival.l4` (4), in the Act's order:
`Is my claim deemed to have existed against them before they died` (s 2(4)),
`Does the claim survive the death` (s 2(1), (4), (5)),
`Can the estate recover these damages` (s 2(1), (2), (7)),
`Does the estate's claim cut down rights under that Act` (s 2(5), (6)).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation,
  especially s 2(6) and s 2(7).
- Have a lawyer review the forks, especially F2 (no cause of action at death), F3 (relatives' claims) and F6 (s 2(2)(c)
  where the wrong did not cause the death).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
