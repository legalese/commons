# Wills Act 1968 (ACT) -- baseline encoding, the person claiming under or about a will

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. For a wills Act that is the person who claims under a will, or
about one: whether the will (or a change to it) was validly made, whether the Supreme Court can save it (s 11A), correct
it (s 12A) or make one for someone without capacity (Part 3A), and by when to apply; what a later marriage or a divorce
did to it; whether it was revoked or revived; and whether a gift lapses for want of 30 days' survival or passes to the
children of a beneficiary who died first. No encoding of this Act existed; nothing was replaced.

Three modules: `wills-dates.l4` (date arithmetic, built-in date functions only, no daydate), `wills-claims.l4` (the rules,
one regulative rule and the 19 exported questions), `wills-cases.l4` (the worked cases). The one duty with a deadline,
to apply for rectification within 6 months (s 12A (3)), is a regulative rule (`MUST ... WITHIN ... HENCE FULFILLED LEST
BREACH ... BECAUSE`) run by EVALTRACE inside the question; no question takes a DEONTIC or an EVENT.

## Edition

- **Act:** Wills Act 1968 (ACT), A1968-11, Republication No 22 (R22), effective 23 February 2026, last amended by A2026-4,
  as deposited at `../../registers/source-bundle/A1968-11.txt` (converted from the register's DOCX, which the register
  marks as an unauthorised version; the authorised text is the register's PDF). An ACT register text, not the Open
  Australian Legal Corpus.
- **Numbers set elsewhere:** none. The commencement of Part 2A (6 October 1983, Ord1983-46) is taken from the
  republication's endnotes for s 15H.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 12A last day for 10 January 2025 asserted to be 10 July 2025) was run once in a
scratch copy and showed as "assertion failed" (153 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wills-dates.l4` | 0 | 0 | 0 | 0 |
| `wills-claims.l4` | 0 | 0 | 0 | 0 |
| `wills-cases.l4` | 0 | 0 | 154 | 154 |

Every exported question has cases with hand-worked values, edges included: a death on 7 and on 8 November 1991; Part 2A
for a death on 6 and on 7 October 1983; every s 8 route; one witness, two, three, two present but one signing, the
signature in each place s 10 allows and one it does not; every route to formal validity and each answer of s 11A; every
answer of s 12; the s 12A last day for a start on the 10th, the 31st of August (to 28 February), the 29th and 30th of
August before a leap February, and across a year end; an application on the last day, the day after, before probate;
the s 12A (4) window on its last day and the day after; s 12A (5) on the day before and the day each protection begins,
with each kind of knowledge; every s 12B combination; each Part 3A answer; every s 20 and s 20A answer; each s 21 route
and each kind of destruction that does not revoke; s 22 both ways; s 31C on the 30th and 31st day after the death,
across a leap February, still alive before and after the 30 days; s 31 and s 31B shares for children, grandchildren and a
sole survivor, and each s 31 condition failing.

**No mirror cases.** One seat.

## Seat

**The person claiming under or about a will** (`wills-claims.l4`): a beneficiary or would-be beneficiary, a member of the
will-maker's family, the executor named in the will, the former spouse or partner, and the person who applies to the
Supreme Court -- for rectification, for a will for someone without testamentary capacity, or a child asking to make or
revoke a will. "Is the will valid?", "Does the change count?", "By when must I apply for rectification?", "Did the
marriage revoke the will?", "Does the gift to the former spouse survive the divorce?", "Does the gift lapse?", "What is
my share?".

The Supreme Court and the registrar get no seat: what the court must be satisfied of is an input with three values
(not yet decided, satisfied, not satisfied), and the answer says what follows from each. The will-maker is not a second
seat: the questions a will-maker would ask (s 8, s 9, s 20, s 21, s 22) are the same questions, worded for whoever asks.
The personal representative's protection (s 12A (5)) is encoded for what it means to the claimant.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed; no instrument sets a number used here.
- **The actors the text names.** Followed: the testator (glossed "will-maker"), the beneficiary, the original
  beneficiary and issue (s 31, s 31B), the former spouse, civil union partner or civil partner (s 20A), the personal
  representative (s 12A), the child (s 8A, s 8B), the Supreme Court and the registrar.
- **Judgments handed to someone else are answered conditionally.** Followed. The court's satisfaction under s 8A (2),
  s 8B (2), s 11A, s 16E and s 20A (2) (a) is an input; the rectification grounds of s 12A (1), (2) are left to the court
  (the question asks only whether the application is in time); "contrary intention" (ss 20, 31, 31B, 31C) and "apparent
  on the face of the will" (s 10) are asked as facts.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: the s 9 requirements, termination
  (s 20A (4)), personal representative's protection (s 12A (5)), the s 31 and s 31B shares. Asked: "child" (Legislation
  Act 2001; asked as the age, fork F5), "testamentary capacity", "domicile", "habitually resided", "civil union",
  "civil partnership", "international will" (the convention's annex is in schedule 1 but asked as one fact).
- **One case is the text's natural unit.** Followed: one will (or one provision of it), one deceased.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed: s 32 and s 33 (deposit of wills), s 16G (registrar's custody),
  s 16H (separate representation) and the leave procedure of s 16B-16D beyond what the answer names are out.

## Scope

**In.** s 8, s 8A, s 8B, s 9, s 10, s 11A, s 12, s 12A, s 12B, s 15C, s 15D (1) (a), (b), s 15H, s 16 (1), (6), (7),
s 16A (1), (3), s 16B (1), s 16C (1), s 16E, s 16F, s 16I, s 16K (as one fact), s 20, s 20A, s 21, s 22 (1), (3), s 31,
s 31B, s 31C, s 35 (2). Folded into the answers' and inputs' words: ss 13, 14, 15, 18, 19 (a witness's ignorance,
incompetence, benefit, being a creditor or executor does not invalidate the will, so none is asked), s 9 (2), s 10 (3),
s 20A (3) (family provision unaffected), s 22 (3), s 31C (4).

**Out, and why.**
- s 5, s 7, s 11, s 14A, s 17: general powers to dispose and to appoint; nothing a claimant asks turns on them beyond
  the questions encoded.
- s 15A, s 15B, s 15E-15G, s 15D (1) (c), (2): the choice-of-law machinery of Part 2A (which system of law, which
  version, what is formal) and the special rules for revoking wills and powers of appointment. The question asks
  whether the will followed the law of a connected place as one fact.
- s 16 (2)-(5) (guardians, evidence in proceedings), s 16A (2), (4)-(7), s 16B (2), s 16C (2), s 16D, s 16G, s 16H:
  court procedure and the registrar's custody.
- s 16J, s 16L, s 16M and schedule 1's articles: the international-will procedure, asked as one fact.
- ss 23-30A, s 31A: rules of construction (later conveyances, the will speaking from death, residuary and general
  devises, words of limitation, "die without issue", change of sex, trustees, intermediate income, illegitimacy). They
  shape what a gift means, not whether a person can claim; each could be added as its own question.
- s 31 (3) and s 31B (3): remoter issue taking a deceased grandchild's share (NOTHING here, fork F8).
- s 12A (1), (2) (the grounds for rectification): decided by the court; the question is whether the application is in
  time.
- s 32, s 33, Part 5 apart from s 35 (2): machinery.
- s 35 (1) (s 31A for wills made or republished after 24 March 1989): s 31A is out.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 12A (3), (4), (5) (b) "a period of N months commencing on the day" -- `the last day of`, the s 12A questions --
  that day counts, so the period ends the day before the same date N months on, or on the last day of a month that has
  no such date (31 August to 28 February) -- the period ends on the same date (Legislation Act 2001 s 151, not
  deposited), or on the day before the month's last day.
- **F2** s 12A (5) (a) "a period of 1 month had elapsed since an advertisement was published", (b) (ii) "a period of 7
  days had elapsed since the day" -- `s 12A (5) -- is the personal representative protected` -- the day of publication
  (or of leave) is excluded, so the month has elapsed from the day after the same date a month on (notice 1 March:
  protected from 2 April), and the 7 days from the 8th day after (leave 1 August: from 9 August) -- the period counted
  as in s 12A (4) ("commencing on the day"), which would protect from 1 April; see finding 2.
- **F3** s 31 (1) (c), s 31B (1) (b) "survive the testator for a period of 30 days", s 31C (1) (b) "survive ... by 30
  days" -- `survived the death on ... by 30 days` -- the 30 days are the 30 days after the day of death, and the person
  must be alive at the end of the 30th (a death on 31 March after a death on 1 March does not survive) -- 30 periods of 24
  hours from the moment of death, or a death on the 30th day counting as survival.
- **F4** s 35 (2) "wills taking effect after 7 November 1991" -- `s 35 -- do the 1991 provisions apply to the will` --
  a will takes effect on the death -- on its making.
- **F5** s 8 "child" -- `s 8 -- does my age stop the will being valid` -- a person under 18 (Legislation Act 2001, not
  deposited), asked as the age when the will was made -- another age.
- **F6** s 12A (3) -- `s 12A -- can I apply for rectification` -- an application made before the day time began (before
  probate) is not barred: s 12A (3) bars only applications "after the expiration" of the period -- premature.
- **F7** s 12A (4) "within the period of 4 months commencing on the day" -- `s 12A (4) -- the day the notice asks me to
  apply by` -- a notice published outside the 4 months (or before time began) is not a s 12A (4) notice: NOTHING, and
  s 12A (5) (a) does not protect -- the notice still starts the 1 month.
- **F8** s 31 (2), s 31B (1)-(3) "nearest issue" -- `the issue share for` -- the nearest issue are children (of the
  original beneficiary, or of the will-maker); a more remote descendant gets NOTHING (out) -- grandchildren as nearest
  issue where no child is alive.
- **F9** s 12 (1), (2) -- `s 12 -- does the change to the will count` -- signatures that are neither near the change nor
  at a memorandum referring to it: not settled by s 12 (an enumerated "not settled" answer of the NOTHING kind), since
  (2) is a deeming rule with no "only" -- counts if signed and witnessed anywhere on the will; or does not count.
- **F10** s 12 (1) "made in a will after the execution" -- the same function -- whether the change was made after
  execution is asked as a fact (the general law's presumption about undated changes is not encoded) -- presume after.
- **F11** s 20A (4) "is taken to be terminated if" -- `s 20A -- what the divorce did to the provision for the former
  partner` -- a separation, or an ending not in (4), is not a termination: "s 20A does not apply" (the text's no, an
  "if" list) -- NOTHING (a deeming list, not closed by "only").
- **F12** s 16A (1) "for a person who does not have testamentary capacity" -- `Part 3A -- can the court make a will for
  someone without capacity` -- a person with capacity is outside Part 3A ("not under Part 3A", a scope limit, NOTHING
  kind) -- a flat no.
- **F13** s 31B (1) "unless a contrary intention appears" -- `s 31B -- my share of a gift to the will-maker's issue` --
  a contrary intention displaces the presumption: NOTHING (the will decides) -- a share of 0.
- **F14** s 31 (1) "If ... then" -- `s 31 -- my share of my parent's gift` -- when a condition fails, s 31 gives the
  claimant nothing: JUST 0 (an "if" list, the text's no); where the gift then goes (s 31C, s 25, the general law) is not
  answered -- NOTHING.
- **F15** s 9 "Subject to this Act" and Part 2A -- `is the will valid as to form` -- the routes are tried in the order
  s 9, s 16, international will, s 16F, s 16I, Part 2A, then s 11A; a will-maker still alive is treated as within s 15H
  (they will die after 6 October 1983) -- Part 2A only once the death has happened.
- **F16** s 12B "is admissible to the extent that" -- `s 12B -- can the evidence be used` -- outside the three
  conditions s 12B does not decide (NOTHING; the general law does); the closing "is not admissible" is the text's no --
  a clear will read as JUST FALSE.
- **F17** s 21 (b) (i) "by a subsequent valid will" -- `s 21 -- has the will been revoked` -- whether the later will
  revokes this one (expressly or by inconsistency) is asked as a fact -- every later valid will revokes.

Sites decided without a fork line: s 8 (1) ("is not valid"), s 9 (1) and s 12 (1) ("not valid ... unless"), s 16A (3)
("must not ... unless"), s 16E ("must refuse leave ... unless"), s 21 ("is not revoked except"), s 22 (1) ("is not
revived unless"), s 35 (2) ("only") are the text's own no: FALSE or the enumerated "not" answer.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

Most questions answer with a choice from a list, a date or a share, not a MAYBE BOOLEAN. Three answer NOTHING in some
cases: s 12A (4) (a notice outside the 4 months, fork F7), s 12B (outside its three conditions, fork F16), s 31 and s 31B
(more remote descendants, fork F8; s 31B with a contrary intention, fork F13). Two enumerated answers are of the NOTHING
kind: s 12's "not settled" (fork F9) and Part 3A's "not under Part 3A" (fork F12). The rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The duty with a deadline is the regulative rule: outside the 6 months the answer is "out of time" (ruling (a)), and
what follows (leave) is the text's own.

## What the Act turns out to say

1. **s 12A (4) has no main verb.** "A personal representative ... may, within the period of 4 months ..., by public
   notice of his or her intention to distribute ... and requiring any person ... to do so within that period of 1
   month." The sense (may give public notice) is clear; the words are missing. Read as "may give public notice". For
   the reviewer.
2. **The notice of s 12A (4) and the protection of s 12A (5) (a) are a day apart.** The notice asks for applications
   within "1 month commencing on the day" it was published and announces distribution after that month; the
   protection needs "a period of 1 month [to have] elapsed since" publication. With the day of publication counted in
   the first and out of the second (forks F1, F2), a notice of 1 March asks for applications by 31 March, but a
   distribution on 1 April is not protected by (a) and one on 2 April is. Asserted. Read the same way both times, the gap
   closes.
3. **s 12 (1) (b) speaks of "the person who signs the will by the direction of the testator"** in a paragraph about
   signing the alteration -- words carried over from s 9 (1) (c). Read as the person who signs the alteration.
4. **The notice to apply does not shorten the time to apply.** s 12A (4)'s 1-month notice only protects the personal
   representative (s 12A (5) (a)); an application stays in time for the whole 6 months of s 12A (3), and s 12A (6)
   keeps the right to recover property already distributed. Asserted (the s 12A (5) answers name s 12A (6)).
5. **s 8 (2) names marriage and civil union, not civil partnership,** while s 20 and s 20A cover all three. A child in a
   civil partnership is not within s 8 (2) on its words (whether a child can enter one is for the Domestic Relationships
   Act 1994, not deposited). Encoded as written (the input names marriage or civil union).
6. **s 31C (3) keeps a gift alive to keep the estate from the Territory.** The 30-day rule does not apply where its
   effect would be that the estate passes to the Territory (Administration and Probate Act 1929 s 49CA). Asserted.
7. **Separation does not touch a will.** s 20A applies only on divorce, nullity, a recognised foreign annulment, or the
   statutory ending of a civil union or civil partnership; a separated spouse keeps every gift until one of those
   happens (s 20A (4)). Asserted (fork F11). The former spouse's family provision claim is kept either way (s 20A (3)).
8. **The deposited text has a letter "l" for the numeral 1** in "(l) A child may apply" (s 8A) and "subsection (l) (a)",
   "(l) (b)" (s 20A (2)). The deposit was not altered; the reading is (1).
9. **s 16I's definition reads "a will executed in accordance with a law of the Territory, or another place for a person
   who ... did not have testamentary capacity"**: the comma lets it be read as any will under ACT law. Read as a will for
   a person without capacity, under the law of the ACT or another place.
10. **s 35 dates the 1991 rules by when a will takes effect,** so a will made in 1985 by someone who died in 2000 is
    under the current s 9, s 11A, s 20A and s 31C (fork F4). Asserted (7 and 8 November 1991).

## Before this is worth relying on

- The Legislation Act 2001 (ACT) for "child", "domestic partner" and the counting of periods (forks F1-F3, F5), not
  deposited.
- The Administration and Probate Act 1929 (ss 49CA, 87B, 87C, 88) for the starting days of s 12A and the s 31C (3)
  exception, and the Family Provision Act 1969 (encoded separately in Commons, not linked here: the stable `l4`
  imports only within a folder).
- The construction rules (ss 23-30A, 31A) and remoter issue (s 31 (3), s 31B (3)).
- A lawyer's view on forks F2, F3, F9, F11, F14 and on findings 1-3 and 5; an independent test pass and a human gate.
