# Administration and Probate Act 1935 (Tas) -- baseline encoding, survival of claims and claims on an estate

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus asked for was **survival**: s 27 (rights
of action by and against personal representatives), which is encoded whole. Around it, the claims machinery a person
with a claim on an estate meets: s 28, s 29, s 43(1), Part VII (ss 54 to 61) and s 65. The rest of the Act (grants of
representation, devolution, administration of assets, resealing) is out; reasons below.

- `tasap-dates.l4`: the dates (built-in date functions only, no daydate): "n months after" and "n months before" a day.
- `tasap-survival.l4`: s 27, with the one regulative rule (s 27(5)(b)).
- `tasap-claims.l4`: ss 28, 29, 43(1), 54 to 61, 65.
- `tasap-survival-cases.l4`, `tasap-claims-cases.l4`: the worked cases.

The duty with a deadline -- taking proceedings in tort against a dead wrongdoer's estate not later than 6 months after
the grant of probate or letters of administration, or the extended time a judge allows (s 27(5)(b), (6)) -- is a
regulative rule (`PARTY ... MUST ... WITHIN ... LEST BREACH`) run by EVALTRACE inside an exported question that takes only
plain facts.

## Edition

- **Act:** Administration and Probate Act 1935 (Tas), No. 38 of 1935, Royal Assent 18 October 1935. The deposited text is
  the consolidated version published 2024-07-18, current on Tasmanian Legislation Online at point in time 2026-11-06:
  `../../registers/source-bundle/act-1935-038.txt` (text sha256
  4dbaa7c748574cae6341293475315f0b51d43b67491b8cd2ee1a89d581610ad9). An unofficial plain-text conversion; the authorised
  version is the one on the site.
- **Dates used, from the history notes in the text:** 15 December 2005 (No. 76 of 2005, s 4, inserting s 27(3A)-(3C),
  "Applied: 15 Dec 2005"); 18 December 2006 (No. 43 of 2006, s 4, amending s 27(1) and omitting s 27(2), "Applied:
  18 Dec 2006").
- **Numbers set elsewhere:** the amount prescribed for s 20A(1) of the Public Trustee Act 1930 (s 54(10)) is not
  deposited; it is asked as a fact ("is the estate small?"). No regulation under this Act sets a number the encoding needs.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 29 charge asserted as 2 where it is 1) was run once in a scratch file in this folder,
since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tasap-dates.l4` | 0 | 0 | 0 | 0 |
| `tasap-survival.l4` | 0 | 0 | 0 | 0 |
| `tasap-claims.l4` | 0 | 0 | 0 | 0 |
| `tasap-survival-cases.l4` | 0 | 0 | 60 | 60 |
| `tasap-claims-cases.l4` | 0 | 0 | 49 | 49 |

Every exported question has cases, with the edges: a death on 17 and on 18 December 2006; s 27(4) for a claim against and
(not) for a claim of the dead person; each limb of s 27(3A) failing alone; a named disease and the s 27(3B)(b) catch-all
each way; a proceeding ended on 14 and on 15 December 2005; damages with and without the dust rule, death not caused by
the wrong, breach of promise; a cause of action arising exactly 12 months before the death and the day before (also
across 29 February); the 6 months' last day and the day after; 31 August plus 6 months (28 February, and 29 February in
a leap year); an extension's last day and the day after, and one ending before the 6 months; proceedings before the
grant; the regulative rule alone on day 0, the last day and the day after; distress on the last day of the 6 months
after a tenancy ends and the day after; s 29 deductions equal to, above and one dollar under the value; the executor's
year on the anniversary and the day after (and from 29 February); every s 54(7) range at both ends and one day outside,
with a month-end clamp; each Part VII outcome.

**No mirror cases.** One seat per question.

## Seat

**The individual a death or an estate claim touches.** s 27 from two sides (`tasap-survival.l4`):

- the **personal representative or family** of a person who has died, bringing or continuing that person's claim for
  the estate: "Does the claim survive?", "What can the estate recover?", "Does a dust-disease claim keep its damages for
  pain and suffering?";
- a **person with a claim against someone who has died**: "Does my claim survive their death?", "Can I still sue the
  estate?", "By when must I take proceedings?";
- the **person who owed rent or a rent-charge** to someone who has died (s 27(7), (8)): "Can the executor distrain on
  me?".

The claims machinery (`tasap-claims.l4`): the **creditor or other person with a claim against the estate** (ss 29, 54
to 61), the **beneficiary or next of kin** waiting for distribution (s 43(1)), the **person defrauded** by the hiding of a
will (s 65), and the **person who paid or handed property to the executor or administrator** (s 28). No official gets a
seat: what a judge would allow is asked as a fact; the Registrar's and the Court's own steps are left out.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Fatal Accidents Act 1934, the Limitation
  Act 1974, the Civil Liability Act 2002 and the Public Trustee Act 1930 are not brought in: their effects are asked as
  facts or noted.
- **The actors the text names.** Followed: the deceased, the personal representative (executor or administrator), the
  estate, the person with a claim, the judge, the Registrar, legatees and next-of-kin, the person liable to a rent-charge,
  the lessee or tenant, the executor in his own wrong, the person defrauded.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether a judge has extended the
  6 months (s 27(5)(b), (6)) and to when; the damages a court would assess (s 27(3)); good faith (s 28); intent to defraud
  (s 29, s 65); full valuable consideration (s 29).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "dust-related condition"
  (s 27(3B)), "personal representative" (s 3, in the glosses). Asked: "cause of action", "tort", "pending", "arose",
  "distress", "rent-charge", "in good faith", the s 20A(1) amount.
- **One case is the text's natural unit.** Followed: one death and one claim; one estate and one claim on it.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed: s 1, s 2, s 3(5), (6), s 53, s 67, s 68 out.

## Scope

**In.**
- **s 27 (the focus), whole:** (1) survival; (3) damages for the estate; (3A)-(3C) the dust-related condition rule; (4)
  a person liable who dies before or at the damage; (5), (6) conditions and time for proceedings in tort against an
  estate; (7), (8) distress by a personal representative; (9) causes of action under the Fatal Accidents Act 1934 brought
  within the "against the estate" rules. (2) is omitted from the text (finding 1).
- **s 28** (protection of a person who pays under a grant), **s 29** (executor in his own wrong), **s 43(1)** (the
  executor's year), **Part VII**: s 54(7) (the closing day's range), ss 55, 56(3), 57, 60 (what follows for a claim after
  the closing day; s 61 and s 59 noted in the comments), **s 65** (a will kept back or hidden).

**Out, and why.**
- Part I (s 1, s 2, s 3 definitions other than as used), Part II (devolution of real estate on the personal
  representative): no question a claimant asks.
- Part III Division I (ss 7-25: who may take a grant, renunciation, limited and special grants): the Court's choices about
  who administers, not a claim. s 20 (continuing proceedings after a temporary administration is revoked) is the Court's
  discretion alone.
- s 26 (inventory "when lawfully required"), s 30, s 31: the personal representative's position, not a claimant's.
- Part IV (ss 32-42, Schedule II: assets, trust for sale, order of application of assets, assent, powers of management
  and appropriation): the administration of a solvent or insolvent estate; Schedule II Part I applies the law of
  bankruptcy, not deposited. s 43(2), (3) (a judge's leave to postpone realisation or carry on a business).
- Part V (repealed 2011; intestacy now in the Intestacy Act 2010). Part VI (ss 47A-53: resealing grants made elsewhere).
- Part VII: s 54(1)-(6), (8), (9) (how the personal representative advertises and files; the Registrar's Claims Book) are
  in the descriptions; s 58 (stay when administration proceedings begin) and s 59 (errors in the account) noted, not
  asked.
- Part VIII: s 62A (pre-1935 wills), s 64 (the Court's general power), s 66 (savings), s 67, s 68 (rules, transitional).
- The Fatal Accidents Act 1934, the Limitation Act 1974 (encoded beside this Act at
  `subjects/au/tas/limitation-act-1974/`), the Civil Liability Act 2002 and the Testators Family Maintenance Act 1912 bear
  on the same claims; not this Act.
- No requirement ledger exists for Tasmania, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 27(1) "after the commencement of this section", with s 27(2) omitted from 18 December 2006 --
  `s 27(1) -- does the claim survive the death` -- a death on or after 18 December 2006 is answered under the text as it
  now stands; an earlier one is not answered (NOTHING-kind), because the omitted s 27(2) is not deposited -- answer every
  death after the 1943 substitution under the current text.
- **F2** s 27(1) "causes of action ... subsisting against him ... vested in him" -- the same function -- no cause of
  action at the death (and s 27(4) not met): the text's own limit, NOTHING-kind -- the text's no.
- **F3** s 27(3A) "damages ... may be recovered if" -- `the s 27(3A) answer`, `s 27(3) -- how much can the estate
  recover` -- when the three conditions hold, the damages assessed for pain and suffering are recoverable -- "may" read
  as a discretion in the court whether to allow them.
- **F4** s 27(3C) "unless -- (a) judgment has been given ...; or (b) the proceeding has been settled or withdrawn" --
  `ended before s 27(3A) commenced` -- judgment, settlement or withdrawal before 15 December 2005 -- at any time, which
  would stop s 27(3A) applying to the very judgment it governs (finding 3).
- **F5** s 27(3) -- `s 27(3) -- how much can the estate recover` -- the amounts are the court's assessment apart from
  s 27(3), which only takes heads out; the funeral expenses assessed are recoverable; where the death was not caused by
  the wrong, everything assessed (other than exemplary damages) is kept -- the funeral sum a discretion of the court;
  s 27(3) read as also fixing what is assessed.
- **F6** s 27(5) "a cause of action in tort", s 27(9) -- `s 27(5) -- can I take proceedings against the estate` -- a
  claim under the Fatal Accidents Act 1934 is treated like a claim in tort; a claim of another kind is outside s 27(5),
  which says nothing about it (NOTHING-kind) -- s 27(9) read as bringing in only the survival of those claims, not the
  s 27(5) bar; or the text's no on s 27(5) for claims not in tort.
- **F7** "12 months before", "6 months ... after", "within 6 months after", "months after the last of such
  publications", "one year from the death" -- `the corresponding day ... months from` -- the same day of the month; where
  the month is too short, its last day (31 August + 6 months = 28 or 29 February); the period runs to the end of that
  day -- 1 March; or a period ending the day before.
- **F8** s 27(5)(b) "or such extended time as a judge may allow" -- `the s 27(5) last day` -- the later of the 6-month
  day and the end of the extension -- the extension as stated, even if it ends sooner.
- **F9** s 27(5)(b) proceedings "taken not later than 6 months ... after the date of the grant" -- the s 27(5) question --
  proceedings taken before any grant are in time (counted as day 0) -- premature, a question for the rules of court.
- **F10** s 28(1), (2) -- `s 28 -- am I protected for a payment under the grant` -- a payment after the grant was revoked
  is no longer "under a representation" (NOTHING-kind) -- s 28(1)'s "notwithstanding any defect or circumstance
  whatsoever" protects it too, where the payer did not know of the revocation.
- **F11** s 29 "to the extent of ... after deducting" -- `s 29 -- how much is the person charged` -- deductions larger
  than the value leave 0 -- a negative balance owed back to the person.
- **F12** s 54(7) -- `s 54(7) -- is the closing day for claims one the Act allows` -- where notices went both interstate
  and to London, the London range (4 to 8 months) -- both ranges at once (4 months only).
- **F13** s 54(10) with s 56(3) -- `Part VII -- what is left of my claim after the closing day` -- for a small estate
  (s 54(4) not applying), a claimant outside Tasmania gets no s 56(3) exception for an unpublished notice -- s 56(3)
  unchanged, so the exception still applies and a small estate's personal representative is never released as to
  interstate claimants (finding 4).
- **F14** s 56(3) "resident in any other State or New Zealand, where the advertisement has not been published as
  aforesaid" -- the same function -- the exception turns on the claimant's residence and the missing notice alone -- only
  where the personal representative had reason to believe the claimant lived there (the s 54(4) trigger).

Sites decided without a fork line: s 27(3B) is a "means" definition (FALSE when no limb holds); the "if" of s 27(3A),
s 27(8), s 29 and s 65 failing, the "unless" of s 27(5) failing and the "so long as" of s 27(7) failing are the text's no;
s 43(1) "not bound ... before" is a flat negative; s 54(7) is a period the text fixes ("not less than ... nor more than").

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

Most questions answer with a choice from a list: the answers marked "(the text's no)" are the JUST FALSE answers and the
answers marked "NOTHING-kind" are the NOTHING answers. One question answers NOTHING directly: `s 27(5) -- by when must I
take proceedings against the estate` (no grant, so no date yet). The two s 29 and the s 65 BOOLEAN answers are FALSE only
where the text's "if" fails. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The s 27(5)(b) period is the regulative rule (`MUST take proceedings against the estate WITHIN` the days from the grant
to the last day, `LEST BREACH`), run by EVALTRACE inside the question; outside it the answer is "out of time (the text's
no)", with the judge's power under s 27(6) to extend the 6 months, even after it has expired, noted.

## What the Act turns out to say

1. **s 27(2) is gone, and the consolidation does not say what it said.** It was omitted by No. 43 of 2006 (applied
   18 December 2006), which also amended s 27(1); the deposited text keeps only the history note. In the other States'
   versions of this section the matching subsection excepts defamation and similar claims from survival. As the text now
   stands, every cause of action survives. Deaths before 18 December 2006 are not answered. Asserted.
2. **A tort claim against a dead wrongdoer's estate has a short second clock, with no relief on the first limb.** Unless
   proceedings were pending at the death, s 27(5)(b) needs the cause of action to have arisen no earlier than 12 months
   before the death, and proceedings to be taken within 6 months after the grant (a judge may extend the 6 months, even
   after it ends, s 27(6)). Nothing lets a court relax the 12 months before the death, so a claim that arose 13 months
   before an unexpected death, with no proceedings yet, cannot be brought against the estate in tort. The ordinary
   limitation periods (Limitation Act 1974) run alongside. Asserted (the 12-month edge each way, the 6-month last day and
   the day after).
3. **s 27(3C) read literally defeats itself.** s 27(3A) "applies ... unless (a) judgment has been given in relation to
   the proceeding; or (b) the proceeding has been settled or withdrawn." Read at any time, s 27(3A) could never apply to
   the judgment in the very proceeding it is about. Read here as ended before 15 December 2005, when (3A) commenced (fork
   F4). Asserted (14 and 15 December 2005).
4. **s 54(10) and s 56(3) do not fit.** s 54(10) excuses a small estate from the interstate and overseas notices of
   s 54(4) but leaves s 56(3) unchanged, whose exception for claimants living interstate or overseas "where the
   advertisement has not been published as aforesaid" would then keep every such claim alive against the executor. Read
   as no exception for a small estate (fork F13). Asserted.
5. **s 54(7) says nothing of a closing day out of range.** The Act fixes the range but not what follows from a notice
   naming a day outside it (whether s 55 and s 56(3) still operate). The question says only whether the day is in range.
6. **Distress for rent.** s 27(7) and (8) let a personal representative distrain as the deceased could have. Whether
   distress for rent is still available in Tasmania under other law (for example residential tenancy law) was not checked;
   the answers say only what s 27 allows.
7. **s 27(3)(c) and s 27(3A)(c) use different tests.** (3)(c) applies where the death was "caused by" the wrong;
   (3A)(c) is met where the condition was only "a contributing factor" to the death. Both are asked as facts; where the
   death was not caused by the wrong, (3)(c) takes nothing out and (3A) is not needed. Asserted.
8. **Stale terms.** s 27(3)(b) still provides for "a breach of promise to marry" (a cause of action abolished in most of
   Australia; whether it survives in Tasmania was not checked), and s 54(4) still sends overseas notices to the London
   Gazette. Encoded as written.
9. **s 27(9) and the Fatal Accidents Act.** s 27(9) brings causes of action under the Fatal Accidents Act 1934 within the
   rules on causes of action against estates; s 27(5) speaks only of "a cause of action in tort". Encoded as reaching
   them (fork F6).

## Before this is worth relying on

- The text of the former s 27(2) and of No. 43 of 2006 (finding 1); the commencement of the 1943 substitution of s 27
  (7 Geo. VI No. 33) for older deaths.
- The Acts Interpretation Act 1931 (Tas) on counting months and periods (fork F7); the Limitation Act 1974 and the
  Fatal Accidents Act 1934 read with s 27(5) and (9); the Civil Liability Act 2002 read with s 27(3).
- The amount prescribed for s 20A(1) of the Public Trustee Act 1930 (s 54(10)); the current law on distress for rent
  (finding 6).
- A lawyer's view on forks F1, F4 to F6, F9, F10, F13 and F14; an independent test pass and a human gate.
