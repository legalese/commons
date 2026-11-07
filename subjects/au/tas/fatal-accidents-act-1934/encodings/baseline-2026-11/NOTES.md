# Fatal Accidents Act 1934 (Tas) -- baseline encoding, the member of the family

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The one date helper is in a small module
(`tfa-dates.l4`, built-in date functions only, no daydate), the rules in `tfa-rules.l4`, and the family member's questions
in `tfa-seat.l4`, which imports the rules and restates none. The cases are in `tfa-cases.l4`. The shape follows the
Limitation Act 1974 (Tas) baseline beside it in `subjects/au/tas/limitation-act-1974/encodings/baseline-2026-11/`.

## Edition

- **Act:** Fatal Accidents Act 1934 (Tas), No. 30 of 1934, consolidated version published 2019-10-31 and current at point
  in time 2026-11-06, as deposited at `../../registers/source-bundle/act-1934-030.txt` (text sha256 baa67c17...a1a4e426),
  retrieved from legislation.tas.gov.au on 6 November 2026. It includes the 2008 amendments (No. 18 of 2008: "partner",
  the $250 000 estate threshold in s 10(1)(b)) and No. 23 of 2009 (s 7, "Australian legal practitioner").
- **Numbers set elsewhere:** none. The Act fixes its own numbers ($250 000, 6 months) and has no regulations.
- **Borrowed terms asked as facts:** "personal relationship" (Relationships Act 2003, not deposited); "spouse", "child",
  "stepchild" and the other relatives (undefined); whether the death was caused by a "wrongful act, neglect or default"
  and whether the deceased could have sued (the common law, the court's findings); "executor or administrator"; the
  jury's findings (sufficiency, shares); the "reasonable cost" of a headstone.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tfa-dates.l4` | 0 | 0 | 0 | 0 |
| `tfa-rules.l4` | 0 | 0 | 0 | 0 |
| `tfa-seat.l4` | 0 | 0 | 0 | 0 |
| `tfa-cases.l4` | 0 | 0 | 88 | 88 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; every
relationship s 3 names, and a partner whose relationship began after the wrongful act; the last day of the executor's 6
months and the day after (10 / 11 July 2025 for a death on 10 January 2025; 28 February / 1 March 2026 for a death on 31
August 2025), a death on 31 August 2023 (6 months ending on 29 February 2024) and one across the year end; particulars
the same day, the day before and the day after the statement of claim; an estate passing to the family of exactly
$250 000 and of $250 001; a headstone above, at and below its reasonable cost; costs not recovered above the amount
recovered.

## Seat

**The member of the family** (`tfa-seat.l4`): the spouse, partner, parent, stepparent, grandparent, child, stepchild,
grandchild, brother, sister, half-brother or half-sister of a person whose death was caused by a wrongful act, neglect
or default -- the person for whose benefit the action is brought (s 5), and who brings it in his or her own name where
s 8 allows (and is then "the plaintiff on the record", s 7). "Am I a member of the family?", "Can an action be brought
for my benefit?", "From when can I bring it myself?", "Can I bring it on this day?", "Have I given the particulars?",
"Is the insurance or super taken off our damages?", "How much of the estate counts?", "Can we get back the funeral,
the headstone, the hospital bills?", "How much of the amount recovered is mine?", "Does the defendant win the issue on
the money paid into court?". No seat for the executor or administrator (an official role under the Act, acting for the
family), the defendant, an insurer, the court or the jury: their findings are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers.
- **The actors the text names.** Followed: the member of the family, the executor or administrator, the plaintiff on the
  record, the defendant and the defendant's Australian legal practitioner, the jury.
- **Judgments answered conditionally.** Followed: "wrongful act, neglect or default", whether the deceased could have
  sued, "reasonable cost", whether the jury "think the sum sufficient" and the shares "the jury ... find and direct" are
  inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "member of the family" and "partner" (s 3) are
  worked out from the relationship and the timing; "personal relationship" is asked.
- **One case.** One death, one member of the family.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In: the whole Act** apart from the machinery: ss 2(2) (in the description of s 4), 3, 4, 5, 6(1), 7, 8, 9, 10.

**Regulative rules:** two, run by EVALTRACE inside exported questions that take only plain facts.
- s 8(1) with s 5: while there is an executor or administrator, `PARTY a member of the family SHANT bring the action in
  my own name WITHIN` the days to the end of the 6 months after the death, `LEST BREACH ... BECAUSE` the action is the
  executor's; run in `Can I bring the action in my own name on this day`.
- s 7: `PARTY the plaintiff MUST deliver the statement of claim HENCE PARTY the plaintiff MUST deliver full particulars
  WITHIN 0 ... LEST BREACH ... BECAUSE` the particulars were not delivered with it; run in `Have I delivered the
  particulars section 7 requires`.

**Out, and why:**
- s 1 (short title), s 2(1) (the Crown is bound): machinery. s 3A, s 6(2), (3) and Schedule 1 are repealed or omitted.
- **The time limit is not in this Act.** It is in the Limitation Act 1974 (Tas) s 5A(3) (3 years from the date of
  discoverability, 6 if a judge extends it) and s 5B (no limit for a death arising from the abuse of a minor), encoded at
  `subjects/au/tas/limitation-act-1974/encodings/baseline-2026-11/` (`By when must I commence my injury or death
  action`). Not restated here; the `@export` text of `Can an action be brought for my benefit for this death` points to it.
- How the jury assess the damages "proportioned to the injury" (s 5) is the common law's, not this Act's: only what the
  Act adds or takes away (s 10) and how the amount is divided (s 5) are encoded.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 8(1) "within 6 months after the death" -- `the corresponding day ... months after`, `s 8(1) -- the last day of
  the 6 months after` -- the 6 months end on the same day of the month 6 months later (or that month's last day if it is
  shorter), the day of the death excluded; a member of the family may sue from the next day -- the period ending the day
  before the corresponding day (the Acts Interpretation Act 1931 (Tas), not deposited, governs).
- **F2** s 8(1) "If in any case there is no executor or administrator" -- `s 8(1) -- I may bring the action in my own
  name on that day` -- read on the day the member of the family brings the action -- read at the death, so that an
  executor appointed later does not take back the 6 months.
- **F3** s 7 "together with the statement of claim" -- `s 7 -- I have delivered the particulars required` -- the same day
  (WITHIN 0); particulars delivered before the statement of claim are not matched -- "together with" read as with the
  same document, or as allowing earlier delivery.
- **F4** s 7 "shall be required ... to deliver" -- same -- before the statement of claim is delivered, NOTHING (the duty
  has not arisen: a missing event); once delivered without full particulars the same day, JUST FALSE (a bare "shall" not
  done) -- the court's power to order particulars later treated as curing it.
- **F5** s 10(2) "hospital and medical expenses incurred as a result of the wrongful act causing his death" --
  `s 10(2) -- the damages that may be awarded for the expense` -- other hospital and medical expenses get JUST 0 from
  s 10(2) -- NOTHING (a limit in the text's own wording, the general damages of s 5 possibly reaching them).
- **F6** s 10(2) "the reasonable cost of erecting a headstone" -- same -- the lower of the amount paid and the reasonable
  cost as the court would find it -- the reasonable cost even where less was paid.
- **F7** s 5 "after deducting the costs not recovered from the defendant ... divided ... in such shares as the jury ...
  find and direct" -- `s 5 -- my part of the amount recovered` -- the shares entered as the amounts the jury directed,
  the costs borne in proportion, never below nothing -- the jury's shares applied after the deduction as fixed sums, or
  the costs borne otherwise.
- **F8** s 6 "Not more than one action ... shall lie" -- `ss 4, 5, 6 -- an action lies for my benefit` and the s 8
  questions -- any earlier action under the Act for the same death bars another, whoever brought it -- "the same
  subject-matter of complaint" read more narrowly (for example a different defendant).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3, the "whenever" of s 4 (rule (c)), the flat negatives "not more than one
action ... shall lie" (s 6) and "shall not be taken into account" (s 10(1)), the "except so far as" of s 10(1)(b), and
the "if" conditions of ss 8(1), 9(2) and 10(2) give `JUST FALSE` (or `JUST 0` for an amount). `NOTHING` is answered for
a payment s 10(1) does not name and an expense s 10(2) does not name (*the text is silent*), and for s 7 before the
statement of claim (a missing event, F4).

## What the Act turns out to say

1. **A partner is fixed at the wrongful act, a spouse is not.** "partner" is someone in a personal relationship "at the
   time when a wrongful act, neglect or default occurred", but "spouse" carries no time. A person who married the
   deceased between a slow-acting wrongful act (an asbestos exposure, say) and the death is a member of the family; a
   partner whose relationship began in the same gap is not. Asserted.
2. **The list is closed.** "means" -- aunts, uncles, nieces, nephews, cousins and in-laws are not members of the family,
   though siblings and half-siblings are (since 2003). Asserted.
3. **"Personal relationship" brings in caring relationships.** Under the Relationships Act 2003 (not deposited) a
   "personal relationship" is a significant relationship or a caring relationship, so a non-relative carer who lived in
   a caring relationship with the deceased may be a "partner" and so a member of the family. Asked as a fact; the
   `@desc` says so. Not asserted.
4. **The $250 000 is for the whole family.** s 10(1)(b) speaks of "such portion of the estate ... as passes to the
   members of his family", not each member's part; the threshold is not indexed and has stood since 2008. Asserted at
   $250 000 and $250 001.
5. **Only the headstone has to be reasonable.** s 10(2) qualifies the headstone with "reasonable cost" but not the funeral
   or cremation, or the hospital and medical expenses (which must instead result from the wrongful act). Asserted (F6).
6. **No time limit in the Act.** The Act gives the executor 6 months (s 8) but leaves the limitation period to the
   Limitation Act 1974 s 5A and s 5B. A family member who waits out the 6 months still has to sue within those 3 years.
7. **The Act still speaks of a jury.** ss 5 and 9 give the shares and the sufficiency of a payment in to "the jury"; the
   actor is kept as the text names it, and the `@desc` adds "(or court)". s 9's payment into court predates the current
   rules' offers of compromise; encoded as written.
8. **s 8(1) counts from the death, not the grant.** An executor appointed late (probate several months after the death)
   may have little or none of the 6 months left before a family member can sue in his or her own name (F2).
9. **"Grandparent" and "grandchild" but not "step-grandparent"; "stepparent" and "stepchild" but no half-relations other
   than siblings.** Encoded as the list reads.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The Acts Interpretation Act 1931 (Tas) rule for reckoning "6 months after" (F1) and the Relationships Act 2003 (Tas)
  for "personal relationship" (finding 3), if deposited.
- A lawyer's view on forks F2, F3, F5-F8 and findings 1, 5 and 8; an independent test pass and a human gate.
