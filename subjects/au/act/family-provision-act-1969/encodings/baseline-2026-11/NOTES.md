# Family Provision Act 1969 (ACT) -- baseline encoding, the family member claiming provision and the beneficiary answering the claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. The Act is short (ss 1-22), so every operative section is encoded
except those listed under Scope. This is the first encoding of the Act; nothing existed to extend.

Six files:

- `fpa-dates.l4` -- the dates (built-in date functions only, no daydate): the calendar month count for "6 months after".
- `fpa-rules.l4` -- the rules both seats share: the s 9 time limit as a regulative rule
  (`PARTY the applicant MUST file the application WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE ...`), run by
  EVALTRACE, and the s 20 (2) bar on taking provision out of distributed property. Nothing exported.
- `fpa-claimant.l4` -- the claimant's 17 exported questions.
- `fpa-beneficiary.l4` -- the beneficiary's 5 exported questions.
- `fpa-cases-claimant.l4`, `fpa-cases-beneficiary.l4` -- the worked cases (the second also holds the mirror cases).

## Edition

- **Act:** Family Provision Act 1969 (ACT), A1969-15, Republication No 12 (R12), effective 12 December 2023, last amended by
  A2023-57, as deposited at `../../registers/source-bundle/A1969-15.txt` (converted from the ACT Legislation Register's
  DOCX, which the register marks as an unauthorised version; the authorised text is the register's PDF). The text comes
  from the ACT register itself, not from the Open Australian Legal Corpus.
- **Numbers set elsewhere:** none. The Act sets its own (6 months in ss 9 and 20, 2 years in s 7). There are no
  regulations under it.
- **Borrowed terms, not deposited:** "domestic partner" (Legislation Act 2001 s 169), "domestic relationship" (Domestic
  Relationships Act 1994 s 3), "spouse", "civil union partner", "civil partner", "child" (Legislation Act dictionary),
  "intestate" (Administration and Probate Act 1929 s 44 (1)), the s 64 notice for claims (same Act), the counting of
  time (Legislation Act 2001 s 151 and following). Each is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 9 last day for a 31 August grant put at 1 March) was run once in a scratch copy and
showed as "assertion failed"; the copy was deleted.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `fpa-dates.l4` | 0 | 0 | 0 | 0 |
| `fpa-rules.l4` | 0 | 0 | 0 | 0 |
| `fpa-claimant.l4` | 0 | 0 | 0 | 0 |
| `fpa-beneficiary.l4` | 0 | 0 | 0 | 0 |
| `fpa-cases-claimant.l4` | 0 | 0 | 91 | 91 |
| `fpa-cases-beneficiary.l4` | 0 | 0 | 24 | 24 |

Every exported question has cases, with the edges: a de facto partnership of exactly 2 years and of 1.9; a domestic
relationship of exactly 2 years and of 1.99; each limb of the s 7 (9) partner definition; each of s 7 (7) (a), (b),
(c); each limb of s 7 (3) and s 7 (4), met and failed; a person under two paragraphs; none of the listed relatives;
the s 9 last day for a grant on the 10th, the 30th and the 31st (a short February, a leap February) and across a year
end; filing on the day of the grant, before it, on the last day and the day after; an extension, filed on its last day
and the day after; an "extension" to a day before the 6 months end; s 20 distributions on the last day of the 6 months
and the day after, with and without notice and vesting; s 21 with and without the s 64 notice; s 11 shares, whole,
fractional (a third, unrounded), excluded and not computable.

**Mirror cases.** The s 20 question is asked on the same facts from both seats (three cases), and the answers agree,
because both call the one rule in `fpa-rules.l4`.

## Seats

**1. The family member claiming provision** (`fpa-claimant.l4`): the partner, the person in a domestic relationship of 2
years or more, the child, the stepchild, the grandchild or the parent of a deceased person who wants (more) provision out
of the estate. "May I apply?", "Under which paragraph?", "Can the court order provision for me?", "By when must I
apply?", "Can I still get more time?", "Must I serve the administrator?", "Can my provision be increased?", "Must I be
told if someone tries to cut it?", "Can it come out of appointed property, or property already handed out?", "Can I sue
the administrator?", "Must I give an undertaking?", "How does the order take effect?", "Can I borrow against it?", "Can
the deceased's letter of reasons be used?".

**2. The beneficiary answering the claim** (`fpa-beneficiary.l4`): the individual who takes under the will or on
intestacy and whose share bears the provision. "Can I apply to have the order cut?", "Whom must I serve?", "How much
comes out of my share?", "Can I be ordered to pay a lump sum instead?", "Can property already given to me be taken?".
It defines none of the claimant module's names.

The Supreme Court, the administrator (as an office), the public trustee and guardian and the trustee of a class fund get
no seat. What the court may do is asked as a fact ("if the court is satisfied that ..."); what the administrator must do
is encoded as what the claimant may rely on (ss 20, 21).

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed; the Act sets its own.
- **The actors the text names.** Followed: the applicant, the deceased, the administrator, the persons beneficially
  entitled, the legatee, devisee or beneficiary, the Supreme Court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: the court's satisfaction under
  s 8 (2), s 9A (3), s 13 (1) (c); its direction under s 14; its "otherwise orders" under s 11 (2); its extension under
  s 9 (2); whether a distribution was "properly made" for a dependant (s 20 (2) (a)); whether the estate has been
  "lawfully and fully distributed" (s 9 (4)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "partner" (s 7 (9)), "maintained
  ... immediately before ... death" (s 7 (7), fork F3), "previous order" (s 9A (1)), the date of an ACT grant for a
  sealed grant (s 4). Asked: see Edition.
- **One case is the text's natural unit.** Followed: one claimant (or one beneficiary) and one estate.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (Scope).

## Scope

**In.** s 4 (a sealed grant dates from sealing, as the date of the grant); s 7 whole (with s 7 (8) in the `@desc` of
"child"); s 8 (1), (2) (s 8 (3) criteria listed in the `@desc`); s 9 whole; s 9A (1)-(4); s 10 (1) (s 10 (2) named in
the `@desc`); s 11 (2), (3); s 13 (1) (s 13 (2), (3) as part of the court's judgment, in the `@desc`); s 14; s 15 (1)
(s 15 (2) named); s 16; s 19; s 20; s 21; s 22 (2) (s 22 (1), (3) named).

**Out, and why.**
- ss 1-3 (name, dictionary, notes): no facts to apply; the dictionary's terms are used where the sections use them.
- s 8 (4) (the court may treat one application as made for all eligible persons), s 9A (5) (further orders), s 11 (1)
  (what the order must specify), s 12 (class fund, its trustee and investment), s 18 (certified copy endorsed on the
  grant): the court's and the trustee's machinery; nothing the claimant must do or can rely on by a date.
- The amount of provision: wholly the court's discretion ("such provision as that court thinks fit"); not encodable
  beyond the s 8 (2) gate.
- The Administration and Probate Act 1929 (intestacy rules, s 64 notices), the Wills Act 1968 s 26, the Domestic
  Relationships Act 1994 and the Legislation Act 2001: other instruments.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 7 (1) (b) "a person (other than a partner ...)" with a short domestic relationship and also a failed s 7 (2)-(4)
  head -- `the s 7 answer for` -- the text's no from s 7 (2)-(4) (JUST FALSE) wins over the NOTHING of a limit in the
  list's wording -- NOTHING.
- **F2** "6 months after the date" (s 9 (1)), "more than 6 months after the date" (s 20 (2) (b) (i)) -- `fpa-dates.l4`,
  every date question -- calendar months, the starting day left out, the last day the same day of the month 6 months on
  or the month's last day; not moved off a weekend or public holiday -- the Legislation Act 2001 counting rules (not
  deposited), which may move a last day that falls on a non-working day.
- **F3** s 7 (7) "shall not be regarded as having been maintained ... unless" -- `was maintained by the deceased under s 7
  (7)` -- any of (a)-(c) is enough -- they are necessary only, and actual maintenance must still be shown.
- **F4** s 9 (1), an application filed before the grant -- `s 9 -- am I in time to apply` -- counted as filed on the day
  of the grant (in time) -- premature (the 6 months run "after" the grant).
- **F5** s 10 (1), s 9A (4), a duty whose "if" is unmet (no application) -- `s 10 -- must I serve the administrators`,
  `ss 9A, 10 -- whom must I serve` -- no duty (FALSE, an empty list) -- NOTHING.
- **F6** s 16 (2) "property of a deceased person who died intestate" -- `s 16 -- how my order takes effect` -- asked
  property by property: property passing on a partial intestacy takes s 16 (2) -- s 16 (2) only where the whole estate
  is intestate.
- **F7** s 20 (2), the closing words "and the property that was so distributed has vested in possession of any person"
  -- `s 20 (2) bars the distributed property` -- they attach to (b) only -- they attach to (a) and (b) both (then a
  distribution for a dependant that has not vested would not be protected).
- **F8** s 19 "of no force or effect unless ... made with the permission of the Supreme Court", once met -- `s 19 -- is
  my dealing with the provision effective` -- NOTHING (s 19 no longer bars it; the general law decides) -- JUST TRUE.
- **F9** s 11 (2) "(other than the person or persons in whose favour an order ... is ... made)" -- `s 11 -- my share of
  the burden` -- such a person bears none (JUST 0) -- NOTHING.
- **F10** s 11 (3), successive interests in settled property -- the same function -- NOTHING (the settled property's
  proportion is charged on its corpus, not apportioned to the person) -- the person's share computed on the value of the
  whole settled property.
- **F11** s 9 (2), (3), an extension to a day before the 6 months end -- `s 9 -- am I in time to apply` -- ignored (an
  extension never shortens) -- the court's day governs.
- **F12** s 7 (4) (b) "not survived by any partner or any of the children" -- `meets s 7 (4)` -- neither a partner nor any
  child survived -- not survived by a partner, or not survived by all the children.
- **F13** s 9A (2) by a person who is neither the administrator nor a beneficiary -- `s 9A (2) -- can I apply to cut a
  provision order` -- NOTHING-kind (a grant limited in its own wording) -- JUST FALSE. The same reading for s 15 (1)
  when the person takes no share or no order is made, and for s 22 (2) when the statement is not signed, dated and
  reasoned.

Sites decided without a fork line: s 7 (2), (3), (4) "is not entitled ... unless" answer the text's no; s 7 (9) and
s 9A (1) "means" answer FALSE outside the definition; s 8 (2) "shall only make an order ... if satisfied", s 9A (3) "if
the court is satisfied" and s 13 (1) "If" answer the text's no; s 9 (4) "shall not be made", s 20 (2) "shall not direct"
and s 21 "An action does not lie" are flat negatives (the text's no).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` answers in ss 7, 8, 9A (2), 11, 15, 19, 21 and 22. The questions answer with a
MAYBE BOOLEAN (or a MAYBE NUMBER for s 11): NOTHING is the NOTHING answer, JUST FALSE the text's no. The rulings it
follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The s 7 (1) list is not closed with "only", so a person who is none of the listed relatives, or falls short of a limit in
a paragraph's own wording (a domestic relationship under 2 years), gets NOTHING (ruling (c)). The 6 months the text
fixes in s 9 (1) answer out of time after the last day (ruling (a)).

## What the Act turns out to say

1. **A short de facto relationship can still found a claim.** A domestic partner of under 2 years who is the parent of
   the deceased's child is a "partner" (s 7 (9) (b) (iii)). Asserted (the 1-year case).
2. **The partner definition starts from "domestic partner".** s 7 (9) (a) requires the person to have been the
   deceased's domestic partner "at any time", and (b) (i) then adds the spouse or civil partner. Whether a spouse who
   never lived with the deceased is a "domestic partner" turns on the Legislation Act 2001 s 169, not deposited; the
   encoding asks it as a fact, so a spouse who answers "no" gets NOTHING. Asserted as answered.
3. **s 7 (1) (b) reaches beyond couples.** A "domestic relationship" (Domestic Relationships Act 1994 s 3) includes a
   personal relationship in which one adult gives the other personal or financial commitment and support, so a carer or
   companion of 2 or more years may claim. Asserted (the carer cases).
4. **A parent may claim as of right only where the deceased left neither a partner nor any child** (s 7 (4) (b), fork
   F12); on the text a surviving grandchild does not shut the parent out. Asserted for a surviving child and a
   surviving partner.
5. **s 7 (7) is written as necessary conditions only** ("shall not be regarded ... unless"); read as sufficient (fork
   F3). Its (c), a court's power to order maintenance, can make a person "maintained" who received nothing. Asserted
   (the stepchild case on (c)).
6. **The claim period and the administrator's safe window meet exactly.** A claim must be filed within 6 months after the
   grant (s 9 (1)); a distribution is protected under s 20 (2) (b) only if made "more than 6 months after" the grant. A
   distribution on the last day of the claim period is not protected; one on the next day can be, if no notice of a claim
   had been given and the property has vested. Asserted (10 and 11 September 2026; 28 February and 1 March 2027).
7. **An extension can be sought after time has run, without any outer limit but one**: s 9 (3) (b) allows it "whether or
   not the time ... has ended", and s 9 (4) bars it only once the estate is lawfully and fully distributed. Asserted.
8. **s 20 (2)'s closing words are ambiguous** between (b) only and (a) and (b) (fork F7).
9. **s 13 cites the Wills Act 1968 inconsistently**: s 13 (2) (c) "section 26 (2)", s 13 (3) (c) "subsection 26 (3)";
   and s 13 (3) (a) ends without "and" where s 13 (2) (a) has it. Style only; no effect on the encoding.
10. **The section numbers jump** (s 4 to s 7; s 7 (4) to (7); s 16 to s 18): ss 5, 6, 17 and s 7 (5), (6) were repealed
   (endnote 4). Nothing is missing from the deposited text.
11. **A beneficiary who also has a provision order bears none of the others' provision** (s 11 (2), fork F9). Asserted.

## Before this is worth relying on

- The Legislation Act 2001 (ACT) (domestic partner, s 169; counting time, fork F2) and the Domestic Relationships Act
  1994 s 3, not deposited.
- A lawyer's view on forks F3, F6, F7, F10 and F12, and on findings 2 and 5; an independent test pass and a human gate.
