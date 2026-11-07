# Family Provision Act 1970 (NT) -- baseline encoding, the family member who claims

UNOFFICIAL. Not an official version of the Family Provision Act 1970 (NT). Copyright in Northern Territory legislation is
owned by the Northern Territory. Quoted under the Northern Territory copyright policy of 8 October 1996 (see
SOURCE-LICENSE.md).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The one date helper is in a small module
(`nfp-dates.l4`, built-in date functions only, no daydate), the rules in `nfp-rules.l4`, and the family member's questions
in `nfp-seat.l4`, which imports the rules and restates none. The cases are in `nfp-cases.l4`. The Act is short (22
sections), so the whole of its operative claims machinery is encoded; what is left out is listed under Scope.

## Edition

- **Act:** Family Provision Act 1970 (NT), reprint REPF002, headed "As in force at 17 March 2004", as deposited at
  `../../registers/source-bundle/Family-Provision-Act-1970-NT-current-reprint-REPF002.txt` (text sha256 41b14615...dc3324,
  LF line endings), retrieved from legislation.nt.gov.au on 6 November 2026, where the register lists it as the current
  reprint and the Act as in force. See finding 7 on the date.
- **Numbers set elsewhere:** none. The Act fixes its one period (12 months, ss 9(1), 20(1)); it has no regulations and no
  amounts.
- **Borrowed terms asked as facts:** "spouse", "de facto partner", "child", "stepchild", "grandchild", "parent" (the
  Interpretation Act and the Status of Children Act; not deposited); whether a court "would ... have power to make an
  order requiring the deceased person to pay maintenance" (s 7(7)(c), the family law); "intestate" (s 61(1) of the
  Administration and Probate Act 1969); the s 96 notices of that Act (s 21(b)); s 35 of the Wills Act 2000 (s 13(2), (3)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `nfp-dates.l4` | 0 | 0 | 0 | 0 |
| `nfp-rules.l4` | 0 | 0 | 0 | 0 |
| `nfp-seat.l4` | 0 | 0 | 0 | 0 |
| `nfp-cases.l4` | 0 | 0 | 81 | 81 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; each
relationship in s 7(1) and one outside it; each s 7(7) head, and a nominal contribution against a more than nominal one;
the s 9 last day and the day after (15 / 16 March 2026 for a grant on 15 March 2025); a filing on the day of the grant
and the day before; a grant on 29 February (last day 28 February, 1 March late); an extended time on its last day and the
day after; s 9(4) with the estate distributed, late and in time; s 20 on the last day and the day after; the regulative
rule at 365 and 366 days, and a `#TRACE` showing the residual permission to seek an extension.

## Seat

**The family member who claims** (`nfp-seat.l4`): the spouse or de facto partner, a former spouse or former de facto
partner, a child (including one born after the death), stepchild or grandchild, or a parent of a person who has died,
left out of the will or left too little by it or by the intestacy rules. "Am I entitled to apply?", "By what day must I
apply?", "Is my application in time?", "Must I serve the administrator?", "Can the Court order provision for me?", "Can
it come out of property the deceased appointed by will, or property already distributed?", "Can I sue the administrator
for distributing?", "How does the order take effect?", "Can it be changed or increased?", "Can I mortgage my provision?",
"What must I give back if the presumed dead person is alive?". No seat for the Court, the administrator, the Public
Trustee or the beneficiaries who bear the provision; a beneficiary seat (ss 11, 15) would be a further layer.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own one period.
- **The actors the text names.** Followed: the applicant, the administrator, the Court, the persons beneficially entitled.
- **Judgments answered conditionally.** Followed: "the Court is satisfied" (ss 8(1), 13(1), 17(2)), "in the opinion of the
  Court" (s 8(3)), "special circumstances" (s 13(1)(c)(ii)), "a proper distribution" (s 20(2)), "other than a nominal
  contribution" (s 7(7)(b)) and the Court's extension of time (s 9(2)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "maintained by the deceased person immediately
  before his death" (s 7(7)) is worked out from facts; "administration" (s 4(1), (2)) is glossed in the `@desc`s;
  relationships are asked.
- **One case.** One claimant against one deceased person's estate.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 4(1) (administration, administrator, deceased person, will) and 4(2) in the `@desc`s; 7(1)-(4), (7), (8); 8(1),
(2) (in the `@desc`), (3); 9(1)-(5); 10(1); 13(1)-(3); 14; 16; 17(1)-(4); 19; 20; 21; 22(1) (in the `@desc` of the s 8
question). ss 8(4) (one application treated as made for all) and 10(2) (the Court may order wider service) hand the
matter wholly to the Court and are not computed.

**Regulative rule:** one. s 9(1) as the applicant's duty: `PARTY the applicant MUST file the application WITHIN` the days
from the grant to the last day, `HENCE FULFILLED`, `LEST PARTY the applicant MAY apply to the Court to extend the time`
(s 9(2), (3)(b)). Run by EVALTRACE inside `Is my application in time`, which takes plain dates; s 9(4) then decides
whether the permission can still be used. No exported question takes a DEONTIC or an EVENT.

**Out, and why:**
- ss 1-3 (title, commencement, repeal of the 1929 and 1931 Ordinances) and s 6 (transitional): machinery.
- s 5: the Act applies to every estate; s 5(2) (estates distributed before 17 March 1971, judged under the repealed 1929
  Ordinance) is not encoded, the old Ordinance not being deposited.
- s 11 (form of the order; the burden borne by the beneficiaries in proportion) and s 15 (commutation and exoneration of a
  beneficiary's share): the beneficiary's seat, not the claimant's.
- s 12 (class fund): the Court's and the trustee's machinery; see finding 4.
- s 18 (certified copy endorsed on the grant): a duty of the Court only.
- s 22(2), (3) (the testator's signed statement as evidence): rules of evidence for the Court.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "is not entitled ... unless" (s 7(2)-(4)), "shall not be regarded as having been maintained ... unless"
(s 7(7)), "if the Court is satisfied" (s 8(1)), "where" (s 13(1), s 10(1)), "shall not" (s 17(3), s 20(2)) and "is of no
force or effect unless" (s 19) give `JUST FALSE` (or a "no:" constructor). `NOTHING` is answered for a relationship
s 7(1) does not list (*the list is not closed with "only"*, F2) and for s 10(1) where there is no administrator
(*silent*, F5). The "not begun" constructor of s 9 (*silent*, F8), the s 17 "no power on this application" constructor
and the two s 20 "gives no power" / "does not speak" constructors (*limited by its own wording*, F9) are the same kind,
said in words.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 9(1), s 20(1) "within ... 12 months after the date on which administration ... has been granted" --
  `the day 12 months after` -- the day of the grant excluded, the last day the same day a year on; a grant on 29 February
  ends on 28 February -- 1 March. The NT Interpretation Act rule on periods is not deposited.
- **F2** s 7(1) a relationship not listed -- `s 7 -- I am entitled to apply` -- `NOTHING` (the list is not closed with
  "only") -- `JUST FALSE`, since the section reads as the whole list of those entitled.
- **F3** s 7(1)(b), (2)(a) "a former spouse or de facto partner" -- same -- a former spouse or a former de facto partner
  -- "former" governing "spouse" only (a current de facto partner is already in (a)).
- **F4** s 7(7)(b) "maintaining that other person or making a contribution ..., being a contribution that ... can be
  regarded as other than a nominal contribution" -- `s 7(7) -- I was maintained by the deceased immediately before the
  death` -- the "other than nominal" test qualifies the contribution only -- qualifying maintaining too.
- **F5** s 10(1) with no administrator -- `Must I serve notice of my application on the administrator` -- `NOTHING` --
  `JUST FALSE` (there is no one to serve).
- **F6** s 16 on a partial intestacy -- `s 16 -- how the order takes effect` -- a codicil for the property the will
  disposes of and a change to the intestacy rules for the rest -- s 16(2) only where the deceased "died intestate" as to
  the whole estate.
- **F7** s 17(3) "An order shall not be made under subsection (1) increasing a provision" -- `s 17 -- what the Court may do
  to the order` -- an increase sought where s 17(2) applies is answered by s 17(2) ("such other order as is just") and not
  barred -- s 17(3) read as barring any increase (finding 5).
- **F8** s 9(1) an application filed before any grant -- `s 9 -- whether my application is in time` -- "the 12 months have
  not begun" -- in time (nothing in s 9 forbids an early application).
- **F9** s 20(1) a distribution made after the administrator had notice -- `s 20 -- provision out of distributed property`
  -- "section 20 does not speak to" it -- the Court cannot order provision out of it.
- **F10** s 14 money and other property both received -- `s 14 -- what my undertaking requires` -- both (a) and (b), the
  total the most that can be required (property may be restored instead of its value) -- one limb only.
- **F11** s 9(4) "after the estate ... has been lawfully and fully distributed" -- `s 9 -- whether my application is in
  time` -- asked as at the day of the question -- as at the day the Court hears the extension.
- **F12** s 17(1) "any person beneficially entitled to, or interested in, a part of the estate" -- `Can the Court change
  the order made for me` -- the claimant, who by s 16 takes as under a codicil, may be such a person and apply -- only the
  will's or the intestacy's own takers (finding 9).

## What the Act turns out to say

1. **s 7 has no subsections (5) and (6).** The reprint runs (1), (2), (3), (4), (7), (8). The endnotes list amendments to
   s 7 but no repeal of (5) or (6). Not encoded; recorded.
2. **A grandchild's standing turns on the parents, not on the deceased.** s 7(3)(b) entitles a grandchild whose living
   parent was not maintaining them, whether or not the deceased maintained them; and a grandchild maintained by the
   deceased but also by a living parent is not entitled. s 7(7) defines only maintenance "by the deceased person", so the
   parent's maintenance is asked in its ordinary sense. Asserted.
3. **s 20 does not help a claimant who needed an extension.** s 20(1) lets the Court reach property already distributed
   only for "an application ... made within 12 months after the date on which administration was granted". An application
   in time only because the Court extended the time (s 9(2)) cannot reach property distributed before the administrator
   had notice of it, and s 21(a) protects the administrator against an action for it. Asserted (filed the day after the
   last day).
4. **s 12(3) refers to itself.** "a reference in subsection (3) to the persons for whose benefit moneys are held in trust
   as a class fund" sits in subsection (3); the words it means are in subsection (2). Probably a drafting slip for
   "subsection (2)". Not encoded (s 12 is out of scope).
5. **s 17(3) bars an increase only under s 17(1).** s 17(2) lets the Court, where it is satisfied the person has
   otherwise come to have means, "discharge, vary or suspend its order or make such other order as is just"; s 17(3) does
   not reach it. Encoded as written (F7), though s 17(2)'s trigger (more means) makes an increase unlikely. Asserted.
6. **"Aboriginal" is defined but never used.** s 4(1) defines "Aboriginal"; no operative provision of the reprint uses
   the word. Not encoded.
7. **The reprint's date.** The heading says "As in force at 17 March 2004", but endnote 5 records general amendments by
   the Interpretation Legislation Amendment Act 2018 to ss 1, 4, 5, 6, 13, 16 and 21. Which version the text is should be
   checked against the register's history before this is relied on.
8. **s 15's heading is garbled.** "Exoneration of Act under this part of estate from provision" (probably "of any part of
   estate"). Not encoded (s 15 is the beneficiary's).
9. **Who may apply to vary.** s 17(1) and (2) give the application to the administrator or a person "beneficially
   entitled to, or interested in, a part of the estate", not in terms to the person the order is for; but s 16 makes the
   order operate as a codicil, which arguably makes that person one (F12). Asked as a choice.
10. **No time before the grant.** s 9(1) runs from the grant in the Territory (or the sealing of an outside grant, s 4(2));
    the Act says nothing about an application made before any grant (F8).

## Before this is worth relying on

- Check the text against the authorised PDF of reprint REPF002 and the register's version history (finding 7).
- The Interpretation Act (NT) rule for reckoning periods (F1), and the meaning of "de facto partner" and "child".
- A lawyer's view on findings 2, 3, 5 and 9 and forks F2-F4, F6-F9, F12; an independent test pass and a human gate.
