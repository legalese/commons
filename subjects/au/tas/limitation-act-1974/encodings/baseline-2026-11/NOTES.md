# Limitation Act 1974 (Tas) -- baseline encoding, the claimant

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`tla-dates.l4`,
built-in date functions only, no daydate), the rules in `tla-rules.l4`, and the claimant's questions in `tla-seat.l4`,
which imports the rules and restates none. The cases are in `tla-cases.l4`. The shape follows the Limitation Act 1981
(NT) baseline in `subjects/au/nt/`.

## Edition

- **Act:** Limitation Act 1974 (Tas), No. 98 of 1974, consolidated version published 2024-07-18 and current at point in
  time 2026-11-06, as deposited at `../../registers/source-bundle/act-1974-098.txt` (text sha256 af438489...6fada09),
  retrieved from legislation.tas.gov.au on 6 November 2026. It includes the Limitation Amendment Act 2017 (No. 52 of
  2017, applied 1 July 2018: ss 5A(3)-(6) as substituted, 5B, 26A, 38A) and No. 48 of 2019 (s 5C, applied 1 May 2020).
- **Numbers set elsewhere:** none. The Act fixes its own periods; it has no regulations. One day is taken from the
  history notes: 1 July 2018, the commencement of the Limitation Amendment Act 2017 ("amendment day", s 38A(1)) and of
  s 5B (s 5C(1)).
- **Borrowed terms asked as facts:** when a right of action "accrued" (the common law); the date of discoverability's
  "ought to have known" (a judgment, entered as a date); "sexual abuse", "serious physical abuse", "psychological abuse"
  (ss 5B, 5C, undefined); "infant", "minor", "child" (finding 3); "mental disorder"; whether another enactment
  prescribes a period (s 38); whether an amount is "recoverable as an overpayment" (s 25D(3)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
a deliberately wrong assertion was run once in a scratch file to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tla-dates.l4` | 0 | 0 | 0 | 0 |
| `tla-rules.l4` | 0 | 0 | 0 | 0 |
| `tla-seat.l4` | 0 | 0 | 0 | 0 |
| `tla-cases.l4` | 0 | 0 | 132 | 132 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the last
day to commence and the day after (9 / 10 March 2023 for personal injury, 1 / 2 July 2025 otherwise); periods from 29
February; s 38A(3) at 30 June and 1 July 2015; s 5C settlements on 30 June and 1 July 2018; s 26A incapacity of 27 and
28 days, beginning on the last day and the day after, two overlapping spells in both orders and one inside another; a
minor's spell running to the day before the 18th birthday; accrual on the 18th birthday and the day before; a payment by
another person liable on the last day and the day after; s 5C(7) half of an odd total.

## Seat

**The claimant** (`tla-seat.l4`): the individual to whom a right of action accrues and who brings or proposes to bring
the action -- the injured person, the family member suing under the Fatal Accidents Act 1934, the personal representative
suing for an estate, the survivor of child abuse, a party to a contract or deed, a creditor, a beneficiary of a trust or
an estate, a person who paid a tax that was not owed. "By when must I start my action?", "Can I still start it on this
day?", "Am I under disability?", "Is my clock stopped?", "Can a judge give me 6 years?", "Can I sue at any time for abuse
I suffered as a child?", "Can I reopen my old settlement?", "Did their acknowledgement or payment give me more time?",
"Can I get back the tax?". One question (s 35) is asked by the same individual when answering a claim with a
counterclaim. No seat for the court, the person sued, an institution, an insurer, the Crown Solicitor or The Public
Trustee: the court's judgments and orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; none is borrowed.
- **The actors the text names.** Followed: the plaintiff, the defendant (intended or prospective), the parent, the legal
  representative, the personal representative, the trustee and beneficiary, the judge and court, The Public Trustee.
- **Judgments answered conditionally.** Followed: "just and reasonable" (s 5A(5), s 5C(6)), "interest(s) of justice"
  (s 5C(2)), "as it thinks fit" (s 8(4)), "reasonable diligence" (s 32), "ought to have known" (s 2(1), s 5A(6)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "date of discoverability" for a personal
  representative (s 5A(6)), disability (s 2(2), (3)), "capable parent", "legal representative", "close relationship" and
  "relevant person" (s 26A), "child abuse" and "previously settled relevant right of action" (s 5C(1)) are worked out from
  facts.
- **One case.** One cause of action, of one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 2(1) (date of discoverability, personal injury), (2), (3); ss 4(1)(a), (d), (3), (4), (5); 5A; 5B; 5C; 8(2),
(4), (7); 24; 25; 25C; 25D(2), (3), (5); 25E; 26(1), (1A), (2); 26A; 27(1); 29(4); 30; 31(5), (7), (8); 32(1); 35; 38;
38A(3). s 5B(3), s 26(3) and s 27(2)-(8) (who is served, the form of the notice) are in the descriptions of the questions
they bear on.

**Regulative rule:** one. The time bar ("shall not be brought after the expiration of", "must not be brought after") as
what the plaintiff must do to keep the action: `PARTY the plaintiff MUST commence the action WITHIN` the days to the last
day, `LEST BREACH ... BECAUSE` the period has expired. Run by EVALTRACE inside `Can I still commence my injury or death
action on this day` and `Can I still commence my action on this day`, which take only plain dates.

**Out, and why:**
- ss 1, 3, 37, 38A(1), (2), (4), 39, 40 and Schedule 1: commencement, cross-reference, Crown, transitional and repeal
  machinery. s 38A(2) only confirms that the 2017 amendments reach old injuries; s 38A(4) and s 39 concern actions begun
  before 2018 or 1975.
- ss 4(1)(b), (c), (2), (6), 6, 7, 9: recognizances, awards, accounts, penalties (2 years, brought by informers rather
  than claimants), conversion of goods, contribution (left to the Wrongs Act 1954) and equitable relief (by analogy only):
  not in the claims focus; the main question answers "not answered by this encoding" for "another kind of claim".
- s 8(1), (3), (5), (6): admiralty claims in rem and salvage. Part II Division 3 apart from ss 24 and 25 (ss 10-23A, land,
  rent, mortgages, options), s 26(4) (land, 30 years), s 29(1)-(3), (5), s 31(1)-(4), (6), (9), (10) (land and mortgages,
  part payments of rent or interest, settled-estate successors): land and mortgage law, not claims.
- s 25D(1): money paid before the commencement of the Limitation Amendment Act 1993, whose date the deposited text does
  not give and which depends on the repealed law.
- s 26(5) (penalties) falls with s 4(6). s 28 (war): not reasonably encodable as a plain fact about the claimant without a
  period input; left out. s 32(2) (innocent purchasers): protects third parties' property, not the claimant's time.
- Part IIIA (ss 32A-32D, choice of law): it tells a Tasmanian court to apply another place's limitation law, which is
  outside this Act; a claim governed by another place's law should use that place's encoding.
- s 33 (arbitration), s 34 (Land Titles Act foreclosure), s 36 (acquiescence): machinery or savings.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "N years from the date" (ss 4, 8, 24, 25, 26) and "3 years commencing on the date of discoverability" (s 5A(3),
  (5)) -- `the anniversary`, `the last day of ... years commencing on` -- "from" excludes the day, so the last day is the
  anniversary; "commencing on" includes it, so the last day is the day before the anniversary; from 29 February into a
  year without one, 28 February in both cases -- both counted the same way (the Acts Interpretation Act 1931 (Tas) rule,
  not deposited, may be read as excluding the day in both).
- **F2** s 38A(3) "more than 3 years before that day" -- `s 5A(5) -- a judge may extend my period to 6 years` -- before
  1 July 2015 -- on or before 1 July 2015.
- **F3** "infant" (s 2(2)), "minor" (ss 5B, 26A), "child" (s 5C) -- `the s 26 last serial`, `the minor spell of` -- under 18;
  the disability ends on the 18th birthday and a minor's spell's last day is the day before -- the day before the birthday
  as the end.
- **F4** s 26A(3), (4)(b) -- `the last serial after spells` -- the suspended days are added to the last day, so a spell
  containing 29 February adds a day; overlapping spells are counted once; a spell of incapacity that lasts 28 days or more
  is suspended from its first day -- the period recounted in years from the end of the suspension; or only the days after
  the 28th suspended.
- **F5** s 26A(3) -- same -- a spell that began before the date of discoverability counts from that date; one that begins
  on the last day counts, one that begins after it does not; an incapacity that has not ended counts (assumed to reach 28
  days), leaving no last day -- the 28 days required to have passed before the suspension is recognised.
- **F6** s 5A(3) "negligence, nuisance or breach of duty" -- `the time limit for the injury claim` -- every action for
  damages including personal injuries, intentional wrongs such as assault included, takes s 5A -- an intentional wrong is
  not a "breach of duty" and takes s 4(1)(a), 6 years from accrual.
- **F7** s 26(1) for a person who was both an infant and incapable at accrual -- `the s 26 last serial` -- the disability
  ceases when the later of the two ends -- when the first ends.
- **F8** s 29(4) with s 26 -- `the general time limit for` -- the fresh period is the Part II period from the
  acknowledgement or payment, and never shortens the time already given; s 26 is not reapplied at that day -- disability on
  the acknowledgement day extending the fresh period.
- **F9** s 32(1) with s 5A -- `the injury period start` -- the 3 years run from the later of the date of discoverability and
  the discovery of the fraud or mistake -- s 32 read as not reaching a period that already runs from discoverability.
- **F10** s 31(8) "made after the expiration of the period" -- `the general time limit for` -- a payment on the last day
  is not after the expiration -- the period read as expiring at the start of the last day.
- **F11** s 5C(6), (7) -- `s 5C(6), (7) -- the most ...` -- an agreement solely about the child abuse: the whole amount;
  one that expressly indicates a part: that part -- the court free to find the part itself in both.
- **F12** s 27(1) "deemed to have ceased to be a person under a disability" -- the injury time limit does not take a
  notice to proceed -- s 27 does not end a s 26A suspension, which turns on being a "relevant person" -- the notice ending
  the s 26A(4)(b) suspension too.
- **F13** s 8(2) and s 5A(3) for injuries on board a ship caused by another ship's fault -- `the time limit for` -- s 8(2),
  2 years, for the ship kind -- s 5A, 3 years from discoverability, for an action in personam (finding 10).
- **F14** s 25D(2) "12 months from the date on which the money was paid" -- `the time limit for` -- the same day a year
  later -- the day before.
- **F15** s 8(4) -- `the time limit for` -- an extension is entered as the day the court fixes and never shortens the 2
  years.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "while" of s 2(2) and s 26A(4), the "means" definitions of s 5C(1), "shall not be brought after" and
"must not be brought after" (the time bar), "may not be granted" (s 38A(3)), "is not maintainable ... unless" (s 25C(1))
and "cannot seek to recover" (s 5C(5)) give `JUST FALSE`. `NOTHING` is answered for s 5B where the facts fall outside its
grant (*limited by its own wording*; s 5A then governs), for s 5C(5) before any order (*limited by its own wording*),
before accrual, where another Act decides (s 38), for an overpayment (s 25D(3), *points outside the text*), and for a kind
of claim outside the encoding.

## What the Act turns out to say

1. **Two ways of counting in one Act.** s 4 and the other Part II periods run "from the date on which the cause of action
   accrued", but s 5A(3) and (5) run "3 years [or 6] commencing on the date of discoverability". If "commencing on"
   includes the day, the personal injury period ends one day before the anniversary, a day earlier than every other
   period in the Act (F1). Asserted (9 March 2023 for discoverability on 10 March 2020).
2. **A minor's personal injury claim gets no s 26 extension.** s 26(1A) takes every s 5A and s 5B cause of action out of
   s 26, so an injured child in the custody of a capable parent has no extension at all: the 3 years run from the date of
   discoverability, with the parent's knowledge counted as the child's (s 26A(5)). Only a child with no capable parent is
   protected, by the s 26A suspension. Asserted (born 2010, injured 2020: 31 May 2031 without a capable parent).
3. **"Infant", "minor" and "child"** are three undefined words for the same idea (ss 2(2), 5B, 26A, 5C). The age of
   majority is set outside this Act and is not deposited; all three are read as under 18 (F3).
4. **s 5A(6) mixes actual and constructive knowledge.** For a personal representative, (a) uses only what the deceased
   "knew", while (b) and (c) use what the representative "knew or ought to have known"; (b) and (c) together reduce to the
   later of the appointment and the representative's knowledge. Encoded as written. Asserted.
5. **The death action has no seriousness limb.** s 2(1) date of discoverability (c) applies "in the case of personal
   injury" only, so for a Fatal Accidents Act action the date is when the death and its cause were (or ought to have been)
   known. Asked as a date; noted in the `@desc`.
6. **An acknowledgement or payment revives even an expired debt.** s 29(4) has no requirement that the acknowledgement or
   payment come before the period expires, and ss 31(6), (8) and 39(1) speak of acknowledgements and payments "made after
   the expiration of the period". Encoded: it restarts time against its maker even after expiry. Asserted.
7. **s 27 is headed for the mentally disordered but reaches infants,** and it speaks of service on the "father or
   guardian" and the "Crown Solicitor" (s 27(3)(a)). Its deeming ("ceased to be a person under a disability") fits s 26,
   but not s 26A, which turns on being a "relevant person" (F12). Asserted for s 26 only.
8. **s 5C does not reach a claim settled before the period expired.** A "previously settled relevant right of action"
   needs a settlement "after a limitation period ... had expired"; a survivor who settled within time before 1 July 2018
   is outside s 5C, though the same claim unsettled would now have no limitation period (s 5B). Asserted.
9. **Small drafting slips in s 5C:** "interest of justice" in (2) and "interests of justice" in (3); "a relevant court" in
   (2) and "the Court" in (3); in s 2(3)(b) a full stop before the omitted paragraph (c). No effect on the encoding.
10. **s 8 and s 5A overlap.** s 8(2) gives 2 years for a claim "against a vessel or her owners" for "personal injuries
    suffered by any person on board her" caused by another vessel's fault, and s 8(7) takes Part III away; s 8(1) excludes
    "the foregoing provisions of this Division" (which, since 2005, include ss 5A-5C) only for claims in rem. For an
    action in personam both s 8(2) and s 5A(3) could apply; the Act does not say which prevails (F13). Asserted for the
    ship kind as 2 years.
11. **s 26(1)'s "less number of years" is inert in scope.** The only shorter periods are s 4(6) penalties (out) and s 8
    (to which Part III does not apply) and s 25D (which "cannot be extended", s 25E). Not asserted.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The Acts Interpretation Act 1931 (Tas) rule for reckoning periods (F1, F14) and the Age of Majority Act 1973 (Tas) for
  "infant", "minor" and "child" (F3).
- Encode s 28 (war), s 4(6) penalties, Part IIIA, and the land and mortgage provisions if wanted.
- A lawyer's view on findings 1, 2, 6, 8 and 10 and forks F4-F6, F9, F12, F13; an independent test pass and a human gate.
