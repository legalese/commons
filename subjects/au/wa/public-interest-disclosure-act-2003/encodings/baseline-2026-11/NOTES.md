# Public Interest Disclosure Act 2003 (WA) -- baseline encoding, the person who makes a disclosure

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`pid-dates.l4`,
built-in date functions only, no daydate), the rules and the 20 exported questions in `pid-discloser.l4`, and the worked
cases in `pid-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act sits in the claims set (employment) because it gives a
person who suffers reprisal for a public interest disclosure a claim in tort or under the Equal Opportunity Act 1984
(s 15), a Supreme Court injunction (s 15A) and, in the public service, relocation (s 15B), and because the immunity of
s 13 is the answer to a claim or discipline brought against the discloser. The claimant here is therefore the informant,
and the encoding follows a disclosure from what counts as public interest information (s 3) and an appropriate disclosure
to a proper authority (s 5), through the authority's duties the informant waits on (ss 7, 8, 10, 11, 12) and the route to
a journalist (s 7A), to the protections and claims (Part 3) and the offences around them (ss 14, 16, 24). Two duties with
deadlines are regulative rules run by EVALTRACE inside exported questions: the proper authority's (s 10(1), notify the
informant within 3 months) and the informant's own (s 17(1)(a), supply requested information within the period
specified).

The whole Act is small (27 sections); everything operative that touches the informant is in, and Part 4 and the
machinery are out (below).

## Edition

- **Act:** Public Interest Disclosure Act 2003 (WA), Act No. 29 of 2003, as compiled on the Western Australian
  Legislation website when retrieved on 7 September 2026, including amendments up to the Local Government Legislation
  Amendment Act 2016 (No. 26 of 2016, in operation 21 January 2017): `../../registers/source-bundle/mrdoc_29657.txt`. The
  Act other than ss 1 and 2 commenced on 1 July 2003 (compilation table), the date s 15(6) turns on.
- **Numbers set elsewhere:** none needed. The Act fixes its own periods (3 months, 6 months) and penalties. The Public
  Interest Disclosure Regulations 2003 are not deposited: declared public authorities (s 3 public authority (g)),
  prescribed classes and declared proper authorities (s 5(3)(i)) and declared persons (s 12) are asked as facts. Schedule 1
  to the Parliamentary Commissioner Act 1971 (s 5(3)(g)) is not deposited and is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 10(1) last day for a disclosure on 15 January 2026 asserted to be 16 April 2026) was
run once in a scratch file, since deleted, and showed "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pid-dates.l4` | 0 | 0 | 0 | 0 |
| `pid-discloser.l4` | 0 | 0 | 0 | 0 |
| `pid-cases.l4` | 0 | 0 | 173 | 173 |

Every exported question has cases, with the edges: month arithmetic at month ends, 28 and 29 February and the year end;
the s 10(1) notice on the disclosure day, the day before the last day, the last day and the day after, and after a
30 November disclosure; the regulative rules alone on day 0, the last day and the day after; the s 7A(2)(b) six months on
the last day and the day after, completed on each; each s 7A(2) ground alone, (d) by s 10(1) and by s 10(4), and with s 10
inapplicable; the s 17(1)(a) period on the last day and the day after, across a month end, with and without excuse; each
s 5(3) paragraph alone and several together (s 5(4)), and recipients that fail; each ground of s 13 failing in turn, the
forfeiture with each kind of relief; each paragraph of the detrimental action definition; s 15(6) on 30 June and 1 July
2003; each route under s 15(4); each ground of s 16(1) and s 16(3); each conduct in the penalty table.

**No mirror cases.** One seat.

## Seat

**The person who makes a disclosure, the informant** (`pid-discloser.l4`): "any person" (s 5(1)), most often a public
sector employee or contractor's employee, who discloses public interest information and may suffer reprisal for it.
"Is what I know public interest information?", "To whom may I disclose it?", "Am I protected?", "Must it be investigated,
and by when must I be told what is happening?", "When can I go to a journalist?", "Can I sue for victimisation, get an
injunction, be relocated?", "Can my identity be revealed?", "Can I lose my protection?", "Could my disclosure be an
offence?".

The proper authority, the Public Sector Commissioner, the Supreme Court, the employing authority and the Commissioner for
Equal Opportunity get no seat: their opinions and decisions (a ground for refusing to investigate, "satisfied that the
grounds are established", the Court being satisfied, relief from forfeiture) are asked as facts. The person a disclosure
is about, and the employer sued under s 15, are parties the Act gives rights or duties to; no seat was written for them
(see "Before this is worth relying on").

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number this encoding
  needs; the regulations that fill out definitions are not deposited and are asked as facts.
- **The actors the text names.** Followed: the informant, the proper authority (with each one s 5(3) names), the
  journalist, the employing authority, the perpetrator and the perpetrator's employer, the Supreme Court, the Commissioner
  for Equal Opportunity.
- **Judgments handed to someone else are answered conditionally.** Followed. "if it considers that" (s 8(2)), "is
  satisfied" (ss 15A(2), 15B(3)), "reasonable grounds" (s 5(2), s 16(3)(d)), "reasonable excuse" (s 17(1)(a)) and the
  court's relief (s 17(2)) are inputs.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: public interest information
  (s 3), appropriate disclosure (s 5(2)), proper authority (s 5(3), s 7), detrimental action (s 3, an "includes"
  definition), act of victimisation (s 15(1)), public service employee (s 15B(1)). Asked: improper conduct (undefined,
  finding 1), public authority, public officer and public sector contractor (long "means" lists, stated by the person as
  a choice glossed with the list), offence under a written law, judicial officer, legal professional privilege, the
  Schedule 1 officers of the Parliamentary Commissioner Act 1971.
- **One case is the text's natural unit.** Followed: one disclosure by one person; for s 15, one act of victimisation.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 3 (public interest information, detrimental action; public authority, public officer, public sector
contractor as choices); s 5 (all of it: (1), (2), (3), (4), (5)(a), (6A) and (6) in the answers); s 6; s 7A; s 7; s 8;
s 10; s 11 (as the limit on the content of a s 10 report); s 12(1), (3), (4), (5A); s 13; s 14 (in the penalty table);
s 15A; s 15B; s 15; s 16(1), (2), (3A), (3); s 17; s 18A; s 23(1)(a) (the designated officer as a recipient) and
s 23(1)(b) (named in the s 15B answer); s 24; s 25 (named in the s 13 answer).

**Out, and why.**
- ss 1, 2, 4, 26, 27, 28 and Schedule 1: machinery (short title, commencement, Crown bound, regulations, review,
  amendments omitted under the Reprints Act).
- s 9: the proper authority's duty to act on a matter, and s 9(2), the right to make a submission, which belongs to the
  person a disclosure is about (a different seat). Nothing in s 9 is for the informant to state or decide.
- s 11(3) (information the Corruption, Crime and Misconduct Act 2003 ss 151-153 forbids): another Act; not encoded beyond
  the s 11 caveat in the report answer.
- s 12(2) (a disclosure to the Parliamentary Commissioner is treated as a complaint for s 26 of the Parliamentary
  Commissioner Act 1971): another Act's procedure.
- Part 4 (ss 18-22): the Public Sector Commissioner's functions, code, guidelines and reports. Administration.
- s 23 other than (1)(a) and (1)(b): the principal executive officer's internal duties (procedures, reporting to the
  Commissioner).
- How much may be recovered in tort under s 15, and the time limit for suing: the Act does not say; the measure of
  damages is the general law and the period is the Limitation Act 2005 (WA), not deposited for this encoding (finding 4).
- No requirement-ledger entry exists for this Act in `subjects/au/wa/requirements.jsonl`, and none was raised: no
  scenario life has reached it. The undeposited Public Interest Disclosure Regulations 2003 would be the first thing to
  raise if one does.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 10(1) "3 months", s 7A(2)(b) "6 months", from a day with no counterpart in the later month (30 November plus
  3 months; 31 August plus 6 months) -- `plus months` (pid-dates.l4) -- the last day of that month (28 or 29 February) --
  the first day of the next month.
- **F2** s 10(1) "not more than 3 months after the disclosure is made" -- `s 10(1) -- have I been told in time` -- notice on
  the day 3 months on is in time; the next day is late -- the 3 months ending the day before.
- **F3** s 7A(2)(b) "has not completed an investigation ... within the period ending 6 months after the disclosure was
  made" -- `s 7A -- may I go to a journalist` -- completion on the day 6 months on is within; ground (b) opens the next
  day -- the period ending the day before.
- **F4** s 18A and s 13 -- `s 13 -- am I protected for making my disclosure` -- a disclosure to a journalist under
  s 7A(2) is answered "uncertain" (NOTHING-kind): s 18A makes the journalist discloser "a person who makes a disclosure
  of public interest information" for Part 3, but s 13 protects only "an appropriate disclosure of public interest
  information to a proper authority under section 5" -- s 18A carries s 13 to the journalist disclosure (the purpose of
  inserting s 18A with s 7A in 2012). Finding 2.
- **F5** s 7A(2)(d) "has not complied with section ... 10(4)" -- `s 7A -- may I go to a journalist` -- once the
  investigation is complete and the informant has asked, a final report not yet given counts as non-compliance (s 10(4)
  fixes no period) -- non-compliance only after a reasonable time.
- **F6** s 8(1) "must investigate ... if the disclosure relates to" (a duty whose "if" is unmet) -- `s 8 -- must my
  disclosure be investigated` -- NOTHING-kind (the Act does not say the authority may not investigate) -- the text's no.
- **F7** s 5(6) "Nothing in this Act entitles a person to disclose information that would otherwise be the subject of
  legal professional privilege" -- `s 13 -- am I protected for making my disclosure` -- no protection under this Act for
  the privileged information (the text's no) -- s 13's immunity still attaching to a disclosure the Act does not entitle.
- **F8** s 15(1) "because or substantially because" -- `s 15 -- can I sue for victimisation` -- detrimental action for
  some other reason is not an act of victimisation (the text's no: the section defines the act) -- NOTHING-kind (a
  scope limit, leaving other causes of action open).
- **F9** s 15B(2) "may apply ... on the grounds that (a) ... and (b) ..." -- `s 15B -- can I be relocated` -- without both
  grounds, NOTHING-kind -- the text's no.
- **F10** s 17(1)(a) "within such period ... as is specified" -- `s 17(1)(a) -- did I help the investigation in time` --
  the period is given in days from the request; the day that many days on is the last day -- counting from the day after
  the request.
- **F11** s 13, the order of failing grounds -- `s 13 -- am I protected for making my disclosure` -- a disclosure to
  someone else first, then not public interest information, then s 24(2), then s 5(2), then s 5(6), then forfeiture --
  all grounds reported together.
- **F12** s 15(4) "cannot subsequently" -- `s 15 -- can I sue for victimisation` -- one fact, "already took the other route
  about this act"; withdrawal of the first proceeding does not reopen the second -- a withdrawn proceeding not counting.
- **F13** s 5(3)(c) "the public authority concerned" and (h) "that authority" -- `s 5(3) -- made to a proper authority` --
  one recipient, the officer designated under s 23(1)(a) by the authority the information concerns or whose sphere it
  falls in -- two recipients, distinguished.
- **F14** s 15A(1) "A person who believes ... may apply" -- `s 15A -- can I get an injunction` -- a person who does not
  believe there is a reprisal is answered NOTHING-kind (a scope limit with no "only") -- the text's no.
- **F15** s 16(1) protects "anyone as a person who has made an appropriate disclosure" -- `s 16(1) -- can my identity be
  revealed` -- a disclosure that is not appropriate is answered NOTHING-kind -- the text's no.
- **F16** s 24(1) -- `s 24 -- is my disclosure an offence` -- a statement made honestly, or not to a proper authority, is
  answered NOTHING-kind (s 24 does not reach it; other laws may) -- the text's no.

Sites decided without a fork line: the "means" definitions (public interest information) and "if, and only if" (s 5(2))
answer the text's no when they fail; each paragraph of s 5(3) is a "where" condition (ruling (b) of 2026-11-05), so a
recipient no paragraph names is the text's no; "do not apply" (ss 8(4), 10(5), 12(4)(a), 16(3A), 17(2A)), "does not
include" (s 7), "does not affect" (s 6), "is not protected" (s 24(2)), "cannot subsequently" (s 15(4)), "no proceeding
may be taken" (s 15(6)), "does not authorise ... unless" (s 15B(4)) and "must not ... unless" (s 16(1), (3)) answer the
text's no; "it is a defence ... to prove" (s 15(3)) answers the text's no for the employer claim when proved (ruling (b)
of the delegated-definitions ruling); "If the employing authority is satisfied" (s 15B(3)) and "If the Supreme Court ...
is satisfied" (s 15A(2)) answer the text's no when unmet; the "includes" definition of detrimental action answers
NOTHING-kind for harm it does not list.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags in the s 6, s 7A, s 8 (F6), s 13 (F4), s 15, s 15A (F14), s 15B (F9), s 16(1)
(F15) and s 24 (F16) questions. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (s 10(1)'s 3 months, s 7A(2)(b)'s 6 months, s 17(1)(a)'s period specified) are answered as
periods: outside each, the consequence the text gives (non-compliance opening s 7A(2)(d); ground (b); forfeiture). Two
are regulative rules (`MUST ... WITHIN`, `LEST BREACH`) run by EVALTRACE inside the questions.

## What the Act turns out to say

1. **"improper conduct" is not defined.** Paragraph (a) of public interest information, the widest head, rests on a
   term the Act never defines.
   Asked as a fact. Asserted (it counts when stated).
2. **A disclosure to a journalist may not carry the s 13 immunity.** s 18A deems a person who discloses to a journalist
   under s 7A(2) to be "a person who makes a disclosure of public interest information" for Part 3. That plainly reaches
   ss 14, 15, 15A, 15B and 16(3), which speak of "a disclosure of public interest information under this Act". But s 13
   (and s 16(1)) protect "an appropriate disclosure of public interest information to a proper authority under
   section 5", and a journalist is not a proper authority. Whether s 18A gives the journalist discloser immunity from
   civil and criminal liability is unclear on the text (fork F4). Asserted as "uncertain".
3. **The offence and the tort use different causation tests.** s 14(1) makes it an offence to take detrimental action
   "because anyone has made, or intends to make" a disclosure; s 15(1) makes it an act of victimisation if done "because
   or substantially because" of one. Conduct with mixed motives can be a tort without being the offence. Encoded as
   written (the s 15 input offers "because, or substantially because").
4. **The tort claim has no measure and no time limit in the Act.** s 15(1) says only that victimisation "may be dealt
   with as a tort", against the perpetrator or their employer (s 15(2)), with the employer's three-limb defence (s 15(3)).
   The damages and the limitation period come from elsewhere. Asserted (the claim lies; no amount is given).
5. **A Minister has no proper authority of their own in s 5(3)(g).** Paragraph (g) excludes members of Parliament,
   Ministers, judicial officers and Schedule 1 officers. A disclosure about a Minister that is not an offence, misuse of
   resources or a matter of administration goes, if anywhere, to the Presiding Officer under (f) (a Minister being a
   member of Parliament) or to the designated officer of the authority under (h). Asserted for a member of Parliament
   (the Public Sector Commissioner is not a proper authority; the Presiding Officer is).
6. **Going to the Chief Justice or a Presiding Officer opens the journalist route after 6 months.** s 7 takes them out of
   "proper authority" for ss 8 to 10, so they have no duty to investigate or to notify. s 7A(2) uses "the proper
   authority to which the disclosure was made" in the s 5(3) sense, so (b), an investigation not completed within
   6 months, opens whether or not anyone was bound to investigate; (d) is excluded by its "if applicable". Asserted.
7. **The informant's identity is protected only for an appropriate disclosure; the subject's for any disclosure.**
   s 16(1) protects the identity of a person who made "an appropriate disclosure"; s 16(3) protects a person "in respect
   of whom a disclosure ... has been made under this Act", with no "appropriate". And s 16(3) binds the informant too:
   telling others who the disclosure is about is an offence ($24,000 or 2 years) unless an exception applies, besides
   forfeiting s 13 under s 17(1)(b). Asserted.
8. **Anonymity changes the informant's rights in five places.** An anonymous informant is not told why an investigation
   is refused (s 8(4)), gets no s 10 notice or report (s 10(5)) or s 12(4) report (s 12(5A)), is not warned before an
   identifying disclosure (s 16(3A)), and cannot forfeit protection by failing to assist (s 17(2A)), though disclosing
   elsewhere still forfeits it. With s 10 out of reach, s 7A(2)(d) cannot open for an anonymous informant. Asserted.
9. **The section numbering runs out of order** (7A before 7, 15A and 15B before 15, 18A before 18), from the 2012
   amendments. No effect on the law; the encoding follows the text's order within each question.

## Before this is worth relying on

- An independent test pass, and a lawyer's look at forks F4 (s 18A and s 13), F5 (s 10(4) with no period) and F7 (s 5(6)).
- The Public Interest Disclosure Regulations 2003 deposited, so that declared public authorities and the prescribed
  classes of s 5(3)(i) can be worked out rather than asked; and Schedule 1 to the Parliamentary Commissioner Act 1971.
- The limitation period for a s 15 tort claim, from the Limitation Act 2005 (WA), linked in a register rather than
  guessed.
- Seats for the person a disclosure is about (ss 9(2), 16(3)) and for the employer sued under s 15 (the s 15(3) defence),
  as further seat layers over these rules.
- The Public Sector Commissioner's code and guidelines (ss 20, 21) are not law in this deposit and are not encoded.
