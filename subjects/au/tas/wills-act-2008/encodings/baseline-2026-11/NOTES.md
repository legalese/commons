# Wills Act 2008 (Tas) -- baseline encoding, the person claiming under or against the will

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The date helpers are in a small module
(`twa-dates.l4`, built-in date functions only, no daydate), the rules in `twa-rules.l4`, and the claimant's questions in
`twa-seat.l4`, which imports the rules and restates none. The cases are in `twa-cases.l4`. The shape follows the Fatal
Accidents Act 1934 (Tas) baseline in `subjects/au/tas/fatal-accidents-act-1934/encodings/baseline-2026-11/`.

## Edition

- **Act:** Wills Act 2008 (Tas), No. 58 of 2008, consolidated version published 2021-11-23 and current at point in time
  2026-11-06, as deposited at `../../registers/source-bundle/act-2008-058.txt` (text sha256 7d9576a7...d93c549), retrieved
  from legislation.tas.gov.au on 6 November 2026. It includes No. 37 of 2012 (Part 5A, international wills) and No. 18
  of 2021 (the Tribunal in place of the Guardianship and Administration Board).
- **Numbers set elsewhere:** none. The Act fixes its own numbers (18 years, 2 witnesses, 30 days, 3 and 6 months) and has
  no regulations in force (the Wills Regulations 1997 were rescinded by s 70).
- **Borrowed terms asked as facts:** "marriage", divorce and nullity (Family Law Act 1975 (Cth)); "deed of relationship",
  "registered relationship", "significant relationship" (Relationships Act 2003); who would share on an intestacy
  (Intestacy Act 2010, not deposited); "internal law" of another place (s 60); "contrary intention", "clerical error",
  "instructions", "dependent"; every finding the Court or the Tribunal makes.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `twa-dates.l4` | 0 | 0 | 0 | 0 |
| `twa-rules.l4` | 0 | 0 | 0 | 0 |
| `twa-seat.l4` | 0 | 0 | 0 | 0 |
| `twa-cases.l4` | 0 | 0 | 158 | 158 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; ages 17
and 18; 1, 2 and 3 witnesses, and 2 present together but only 1 signing; exactly 2 attesting witnesses (never saved by
s 12(2)(a), "more than 2"); the last day of the 6 months after a grant and the day after (15 / 16 July 2025; 28 February
/ 1 March 2026 after a grant on 31 August 2025); the last day of the 3 months after a death and the day after (10 / 11
April 2025; 28 February / 1 March 2026 after 30 November 2025; 29 February 2024 after 30 November 2023; across the year
end from 31 October 2025); days 1, 30 and 31 after the will-maker's death, the same day, the day before, and day 30
across 29 February 2024 (16 / 17 March 2024); a residue in halves and quarters, and in thirds.

## Seat

**The person claiming under or against the will of a person who has died** (`twa-seat.l4`): a beneficiary, a member of
the family, a person who would share on an intestacy, a former spouse or registered partner, a witness who was given a
gift, the child or grandchild of a beneficiary who died first, a dependant awaiting a gift. "Could the will give this
away?", "Was the will validly made?", "Can an unsigned document count?", "Is my gift void because I witnessed it, and
can I keep it?", "Was the will revoked, by what was done to it, by marriage, by divorce?", "Does the change count?",
"Was it revived?", "Is the Tribunal's statutory will valid?", "By when must I apply to rectify, and can the Court
rectify?", "Is the executor protected for what was paid out?", "Does the gift fail because the beneficiary died within
30 days, and where does it go?", "Do I take my parent's share?", "What fraction do I take now?", "May I see the will?",
"Can I be paid maintenance in the first 30 days, and how much comes off my share?". No seat for the will-maker in life,
the personal representative, the Court, the Tribunal or the Registrar: their findings are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers.
- **The actors the text names.** Followed: the testator (glossed "the will-maker"), the beneficiary, the witnesses, the
  personal representative, the Court, the Registrar, the Tribunal.
- **Judgments answered conditionally.** Followed: "satisfied beyond reasonable doubt" (ss 10, 42), "thinks this is
  necessary" (s 42(3)), the Court's extension (s 13(3)), its s 14 findings, "satisfied from the state of the will"
  (s 15(1)(e)), a "contrary intention ... established" (s 17(4)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "minor" (s 4) is worked out from the age; when "a
  marriage ends" (s 17(5)) from how it ended; the rest are asked.
- **One case.** One will, one person asking about one benefit.
- **The Act's terms with plain glosses.** Followed, in each `@desc` ("testator": the will-maker; "attest": witness).
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In** (the provisions a claimant meets): ss 6, 7, 8(1)-(3), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20(4), (5), 31 (with
s 39), 42(1)-(4), 45, 49, 55, 56(2), 60(1), 63(1), (3), (4), 64(1)-(4); s 4's definitions where they are used.

**Regulative rules:** two, run by EVALTRACE inside exported questions that take only plain facts.
- s 13(2): once probate is granted, `PARTY the applicant MUST apply to the Court to take the gift as if section 12 did
  not apply WITHIN` the days to the end of the 6 months, `LEST BREACH ... BECAUSE`; run in `Can the Court let me keep my
  gift as a witness`.
- s 42(2): `PARTY the applicant MUST apply to the Court to rectify the will WITHIN` the days to the end of the 3 months
  after the death, `LEST BREACH ... BECAUSE`; run in `Can the Court rectify the will on my application`.

**Out, and why:**
- ss 1-3, 65-71 and Schedules 1-4: machinery (title, commencement, purpose, rules of court, regulations,
  administration, repeals).
- s 5 (which wills the Act applies to): transitional. The Act commenced on a day proclaimed, and the date is not in the
  deposited text; the encoding assumes a will made, and a will-maker who died, after commencement. A will made before
  it may still be governed by the Wills Act 1992 for some sections.
- ss 8(4)-(7) and 9 (powers of appointment exercised by will; a witness's incompetence or ignorance does not matter):
  they add nothing a claimant must state, so no input is asked for them.
- s 20(1)-(3), (6) and ss 21-30, 32-38, 40, 41: the applications to the Court or the Tribunal for a will for a living
  minor or a living person lacking capacity, and what the Court, the Registrar and the Tribunal must do. They are
  proceedings for a living person, not a claim on an estate; their outcome reaches the claimant through s 20(4), (5),
  s 31 and s 39, which are in. s 37(2) (a person who regains capacity may revoke a statutory will) is covered by s 15.
- Part 4 apart from ss 45, 49, 55 and 56(2) (ss 43, 44, 46-48, 50-54, 56(1), (3) as an input, 57-59): rules for
  construing the will's own words, which the Court applies to the text of a particular will; they turn on wording the
  person cannot state as a plain fact.
- ss 61, 62 and Part 5A with Schedule 5 (which foreign law applies; the Convention form of an international will): s 60
  is in, and conformity with a foreign law (or the Convention) is asked as one fact.
- s 42(5), s 63(2) (duties to the Court), s 14(3) (evidence; in the `@export` text), s 64(2), (3) (the personal
  representative's protection; in the `@export` text).
- The family provision claim (Testator's Family Maintenance Act 1912) and the intestacy rules (Intestacy Act 2010) are
  other Acts, not deposited.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 13(2), 42(2), (4) "6 months after", "within 3 months after", "at least 3 months after" -- `the corresponding
  day ... months after` and the s 13 and s 42 functions -- the period ends on the same day of the month 3 or 6 months
  later (or that month's last day if shorter), the day of the event excluded; "at least 3 months after" is reached on
  that day -- the period ending the day before the corresponding day (the Acts Interpretation Act 1931 (Tas), not
  deposited, governs).
- **F2** s 13(2) "is not to be made more than 6 months after that date" -- `ss 13(2), (3) -- I may apply on that day` --
  "that date" is the date of the grant of probate -- the date of the death (finding 1).
- **F3** ss 49, 55, 64 "within 30 days after the death", "survive the testator for 30 days", "within that 30-day period"
  -- `s 49 -- ...`, `s 55 -- ...`, `s 64(1) -- ...` -- days 1 to 30 after the day of the death; a beneficiary dying on the
  same day as the will-maker is outside s 49 (NOTHING); the s 64 period runs from the day of the death to day 30 -- the
  day of the death counted as day 1, or a same-day death treated as within 30 days.
- **F4** s 20(4)(a) "one of the attesting witnesses must be the Registrar" -- `ss 7, 20 -- the will-maker could make the
  will` -- a Court-authorised minor's will without the Registrar as a witness is not valid (JUST FALSE, a bare "must"
  not done) -- valid if s 8 is otherwise met, (4)(c) naming only a breach of the order's conditions as invalidating.
- **F5** s 16(4) "expressed to be made in contemplation of marriage generally or the registration of a deed of
  relationship" -- `s 16 -- the will is revoked as to my benefit ...` -- either general expression saves the will from
  either a marriage or a registration -- each saving only against its own kind of event.
- **F6** s 17(5) "a marriage ends -- (a) ... (b) ... (c)" -- `s 17 -- the ending revokes my benefit` -- read as saying when
  a marriage ends, so a separation without a divorce has not ended it (JUST FALSE) -- an open list (NOTHING).
- **F7** s 45(1) "other than the exercise of a power of appointment" -- `s 45 -- the failed gift falls into the residue`
  -- NOTHING for the exercise of a power of appointment (the section does not speak) -- JUST FALSE.
- **F8** s 18(1) "unless the alteration is executed in accordance with Division 2 of this Part or Division 2 of Part 3"
  -- `s 18 -- the effect of the alteration` -- an alteration under a Court order for a minor (Part 3 Division 1) counts
  only if signed and witnessed as s 8 requires, as s 20(4)(a) also demands -- such an alteration counting by force of
  the order (finding 5).
- **F9** s 31 with s 39 -- `s 31 -- the Tribunal's statutory will is valid` -- JUST TRUE where there is no prior will, on
  the footing that the Tribunal's order was properly made (its s 33 findings are not facts this seat can state) --
  NOTHING until those findings are asked.
- **F10** s 56(2) "passes to the part that does not fail ... proportionately" -- `s 56(2) -- my fraction after the failed
  parts pass` -- my new fraction is mine x all / (all - failed), and NOTHING if every part fails -- the failed part
  divided equally rather than in proportion.
- **F11** s 42(3) "but not if the final distribution of the estate has been made" -- `ss 42(2), (3) -- my application to
  rectify is in time` -- bars only an extension; an application within the 3 months stands though the estate was
  distributed (finding 7) -- barring any application after a final distribution, as s 13(3) does.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "is not valid", "is not valid unless", "is not valid if" (ss 7, 8, 20(4)), "may not" (ss 6(4), 11), "only"
(s 15(1)), "is not revoked" (ss 15(2), 16(2)-(4), 17(2)), "is invalid if" (s 31), "Nothing ... authorises" (s 63(3)),
the "where" and "if" conditions of ss 10, 12, 14, 42(1), 49, 55, 64(1), "does not apply if" (ss 17(4), 45(2), 49(2),
55(3)), "but only if" (s 17(5)(c)) and the periods of ss 13(2), 42(2), 49 and 64(1) give `JUST FALSE`. `NOTHING` is
answered for a document that does not purport to embody testamentary intentions (s 10, a scope limit), the end of an
unregistered relationship (s 17, silent), a revival by any other means (s 19, an open list), an application before the
death and a personal representative outside s 42(4) (silent), a power of appointment under s 45 ("other than", F7), a
death on or before the will-maker's under s 49 (a scope limit), a contrary intention or every part failing under
s 56(2), and a person s 63(1) does not list (open list; s 63(4)).

## What the Act turns out to say

1. **s 13(2)'s "that date" has no date before it.** "An application ... may be made before the grant of probate of the
   will but ... is not to be made more than 6 months after that date." The only candidate is the (date of the) grant;
   read so (F2). A possible drafting slip.
2. **Only the witness's own gift is void, but a spouse still spoils the saving.** s 12(1) voids a gift "to a person who
   attests" (and those claiming under that person), not a gift to the witness's spouse; yet under s 12(2)(a) a witness
   who is the spouse of a beneficiary does not count as independent. Asserted (a gift to me when only my spouse
   witnessed stands).
3. **Separation and unregistered relationships do not revoke.** s 17 acts only on a divorce, a decree of nullity, a
   recognised foreign dissolution or annulment, or the revocation of a registered deed. s 4's "spouse" includes a
   person in a significant relationship, but the end of an unregistered one revokes nothing under s 17. Asserted (JUST
   FALSE for a separation, F6; NOTHING for an unregistered relationship).
4. **s 20(5)'s "deceased minor".** "A will made by a deceased minor according to the law relating to wills of minors of
   the place where the deceased was resident" does not say whether the person was a minor at death or only when making
   the will; the `@desc` asks about a will-maker who died under 18. Not asserted beyond that reading.
5. **s 18(1) names Division 2 of Part 3 but not Division 1 or 3.** A Court-authorised alteration for a minor (s 20(1))
   and a Tribunal alteration of a statutory will (s 36) are not among the alterations s 18(1) validates; s 20(4)(a)
   requires the minor's alteration to be executed as the law requires anyway (F8). The Tribunal's s 36 alteration has
   no execution rule of its own.
6. **The last day of s 42(2) is also the first day of s 42(4).** On the day 3 months after the death an application for
   rectification is still in time and a distribution that day is protected (if the personal representative knew of no
   application). Asserted.
7. **s 42(3) and s 13(3) treat a final distribution differently.** For a witness's application, "no application may be
   made after the final distribution"; for rectification, the final distribution only stops an extension. A
   rectification application within the 3 months after a quick final distribution is in time. Asserted (F11).
8. **s 31 looks only for a prior "will".** The Tribunal must be satisfied that the person has made no "will or any
   purported will" (ss 30(4), 33(c)), but s 31 invalidates the statutory will only for a prior "will"; a purported will
   found later counts only if it is a will (for example under s 10). Not asserted.
9. **s 33(f) reads "alteration of revocation"**, a slip for "or"; and the Tribunal under s 30 may only make a will
   (alteration and revocation are ss 36, 37). Not encoded (out of scope).
10. **s 60 saves the form, not the age.** A will signed in accordance with a foreign law is "properly executed", but a
    will made by a minor is still "not valid" under s 7 unless an exception applies. Asserted.
11. **s 64's 30 days and s 49's 30 days line up.** A dependant's maintenance before the gift becomes absolute comes off
    the share if he or she survives the 30 days, and is an administration expense if not. Asserted.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The commencement date (s 5), the Acts Interpretation Act 1931 (Tas) for reckoning months and days (F1, F3), the
  Relationships Act 2003 (Tas) and the Intestacy Act 2010 (Tas), if deposited.
- A lawyer's view on the forks, chiefly F2, F4, F5, F6, F8 and F11, and on findings 1, 3, 4 and 5; an independent test
  pass and a human gate.
