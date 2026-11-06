# Racial Discrimination Act 1975 (Cth) -- baseline encoding, the person discriminated against

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`rda-dates.l4`,
built-in date functions only, no daydate), the rules and the exported questions in one module (`rda-claims.l4`, as the Age
Discrimination Act baseline does), and the worked cases in `rda-cases.l4`.

The focus asked for: the provisions a claimant meets in a racial discrimination claim, with two settings in view: a group
claim by members of a community against a public body over policing and public services (ss 9, 10, 18, 18A, the Crown
bound by s 6, and the representative complaint and court routes of the AHRC Act), and an employment claim (s 15,
victimisation, the s 27(2) offence). The Act is short, so Part II and Part IIA are encoded whole, with the claims machinery
the Act sends the claimant to (its s 20 note: "see Part IIB of the Australian Human Rights Commission Act 1986").

## Edition

- **Act:** Racial Discrimination Act 1975, Compilation No. 19, compilation date 13 December 2022 (includes amendments up to
  Act No. 85, 2022; register id C2022C00366), the latest compilation when retrieved on 13 October 2026, deposited at
  `../../registers/source-bundle/C2004A00274.txt`.
- **Australian Human Rights Commission Act 1986**, ss 3(1) ("unlawful discrimination", "representative application"),
  46P, 46PB, 46PE, 46PF(1)(b), 46PH, 46PO, 46POA(1), 46POB(3) and 46PSA only: Compilation No. 58, compilation date
  18 September 2026 (includes amendments up to Act No. 87, 2026; register id C2026C00416), deposited at
  `subjects/au/australian-human-rights-commission-act-1986/registers/source-bundle/C2004A03366.txt`.
- **Federal Court of Australia Act 1976**, Part IVA ss 33C(1), 33E, 33J, 33ZB, 33ZE only (representative proceedings, the
  group route s 46PO's note points to): Compilation No. 59, compilation date 11 December 2024 (register id C2024C00819), deposited at
  `subjects/au/federal-court-of-australia-act-1976/registers/source-bundle/C2004A01586.txt`.
- **Acts Interpretation Act 1901**, ss 2G(2) and 36 only (counting the 24 months and the 60 days): Compilation No. 39,
  compilation date 28 March 2026 (register id C2026C00117), deposited at `subjects/au/acts-interpretation-act-1901/registers/source-bundle/C1901A00002.txt`.
- **Numbers set elsewhere:** the penalty unit, Crimes Act 1914 s 4AA (Compilation No. 167, compilation date 27 August 2026,
  register id C2026C00368, deposited at `subjects/au/crimes-act-1914/registers/source-bundle/C1914A00012.txt`): "$330 (subject to indexation under
  subsection (3))". s 4AA(3) indexes it on 1 July 2026 and every third 1 July after, and the indexed amount is published by
  notifiable instrument (s 4AA(1A)), which is not deposited; so the s 27(2) answer stays in penalty units and the $330 base
  is named in its question text. No regulation sets a number the encoding needs.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 46PO(2) last day moved by one day) was run once in a scratch copy, since deleted, and
showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `rda-dates.l4` | 0 | 0 | 0 | 0 |
| `rda-claims.l4` | 0 | 0 | 0 | 0 |
| `rda-cases.l4` | 0 | 0 | 191 | 191 |

Every exported question has cases, with the edges: each element of s 9(1) and s 9(1A) missing in turn; s 9(3), s 8(1),
s 8(2) and both together; s 10(3) for an Aboriginal person, a Torres Strait Islander, a special measure and a general law;
immigrant status where s 5 reaches and where it does not (ss 12(2), 15(3)); every actor and act of s 15 and the mismatches;
s 15(4) and (5); s 18A with each condition missing and with reasonable steps; every head of s 18AA; s 27(2) for a natural
person and a body corporate; each s 18C(2) place and private; good faith with and without a s 18D head; a complaint lodged
on the last day of the 24 months and the day after, from 15 March 2024, from 29 February 2024 (last day 28 February
2026) and from 28 February 2022 (last day 29 February 2024, AIA s 2G(2)); a court application on day 0, day 60 and day 61
after the notice, across 29 February 2028 (day 60 is 1 March 2028), with day 60 a Sunday (15 December 2027: Monday
14 February 2028 in time, 15 February not, AIA s 36(2)), with day 60 a holiday, and over Christmas (25 and 28 December
holidays: 29 December 2026); every ground of termination that needs or does not need leave; every head of s 46PSA(6) and
(7); s 8 over ss 14(2), 16 and 17; the Crown under s 6(2); each element of FCA Act s 33C(1), and a Part IVA group member
and representative party.

**No mirror cases.** One seat.

## Seat

**The person discriminated against** (`rda-claims.l4`): the individual to whom the Act is applied and who may bring a
claim under it: the worker or job seeker; the member of a community or group treated differently by a public body, a law
or a business because of race, colour, descent or national or ethnic origin; the person victimised for complaining; the
group member in a representative complaint or application. "Was what was done to me unlawful?", "Does s 10 give me the
same right?", "Is the employer or the State answerable for what its employee did?", "Can I complain, and for my whole
community?", "By when?", "Can I go to court, and do I need leave?", "What can the court order?", "Will I have to pay
costs?".

The Act speaks to the person who discriminates ("It is unlawful for a person ..."); the encoding turns that into what it
means for the person in the seat. The Commission, the President and the court get no seat: their satisfactions, opinions
and orders are asked as facts. No second seat (respondent) was written: the respondent's questions are the same rules
asked the other way, and the focus is the claimant.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed, with additions, each listed under Edition: the
  claimant's questions "where do I complain, by when, and what then?" are answered only in the Australian Human Rights
  Commission Act 1986, to which the Act's s 20 note sends them, so its complaint and court provisions are brought in (as
  the Age Discrimination Act baseline did); the group route of Part IVA of the Federal Court of Australia Act 1976, to
  which s 46PO's note and s 46PO(5) point and which the focus (class actions) names; the Acts Interpretation Act 1901's
  rules for counting months and days, which fix the last days; and the Crimes Act 1914 penalty unit. Nothing else from
  those Acts is.
- **The actors the text names.** Followed: the person, the employer, the principal, the employment agency, the
  organisation of employers or employees, the supplier, the trade union, the Commission, the President, the court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether an act impairs a human right
  on an equal footing (s 9(1), (1A)(c)); whether a requirement is reasonable (s 9(1A)(a)); whether a measure is a special
  measure (s 8(1), Article 1(4)); whether an act is reasonably likely to offend (s 18C(1)(a)); whether it was said or done
  reasonably and in good faith (s 18D); whether the principal has established reasonable steps (ss 18A(2), 18E(2));
  whether a complaint is reasonably arguable (AHRC Act s 46P(1A)); the President's ground of termination; the court's
  further time, satisfaction and costs findings.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: Aboriginal and Torres Strait
  Islander (s 3(1)); the two-or-more-reasons rules (ss 18, 18B); "not in private" (s 18C(2)); victimisation (s 18AA(2));
  "unlawful discrimination" and "representative application" (AHRC Act s 3(1)). Asked: "special measure" (the
  Convention); "registered charity" (ACNC Act); "human right or fundamental freedom" and Article 5; "immigrant";
  "relative" and "associate" are folded into the reason inputs.
- **One case is the text's natural unit.** Followed: one act towards one person (or one group, for s 18C and the
  representative complaint).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In.** Racial Discrimination Act 1975: s 3(1) (Aboriginal, Torres Strait Islander, employment, dispose, services,
vehicle), s 3(3), (4) (glossed), s 5 (immigrants), s 6(1) (the Crown bound, in the s 18A description), s 6(2) (the Crown
not prosecuted, in the crime question), s 6A(2), Part II whole (ss 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A, 18AA),
Part IIA whole (ss 18B, 18C, 18D, 18E), s 26, s 27(2). AHRC Act, FCA Act Part IVA, AIA and Crimes Act: as under Edition.

**Out, and why.**
- ss 1, 2, 4, 6B, 7, 18F, Part III (the Commission's functions), ss 27(1), (1A), 27F, Part VI (the Commissioner),
  ss 44, 45, 45A, 47 and the Schedule: machinery, offences against officials, or text that does not answer a claimant's
  question. s 6A(1) and (3) (concurrent State laws, double prosecution) are not a claimant's question; s 6A(2) is.
- The Convention in the Schedule is quoted by s 9(2) and s 10(2) for "rights of a kind referred to in Article 5" and by
  s 8(1) for special measures: both are asked as facts, with Article 5's rights listed in the `@desc`.
- AHRC Act s 46P(1B) ("The complaint must set out, as fully as practicable, the details of the alleged acts, omissions or
  practices"): a requirement of form the claimant meets in writing the complaint, which answers no question of entitlement
  or time; a complaint short of it may be amended (s 46PA). Not encoded.
- AHRC Act: the President's inquiry and conciliation (ss 46PD, 46PF other than (1)(b), 46PI-46PN), amendment and withdrawal
  of complaints (ss 46PA, 46PG), the rest of s 46PB and 46PC, interim injunctions (s 46PP), representation (s 46PQ), the
  other s 46POB rules (separate applications, settlement), and the Commission's assistance (ss 46PT-46PV): procedure the
  claimant does not decide, or that adds no answer. The court's further time under s 46PO(2) and its leave under (3A)(a)
  are the court's: asked or reported, not decided.
- Part IVA of the Federal Court of Australia Act 1976 other than ss 33C(1), 33E, 33J, 33ZB and 33ZE: s 33B (causes of
  action after the 1991 amendment commenced; every claim here is later), s 33G (cross-vesting only) and the court's
  management of the proceeding (ss 33D, 33F, 33H, 33K-33ZD, 33ZF-33ZJ): procedure the group member does not decide.
- The Acts Interpretation Act 1901 and the Crimes Act 1914 beyond ss 2G(2), 36 and s 4AA(1).
- No requirement-ledger entry exists for this Act, and none was raised: no scenario life has reached it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 9(1A) -- `s 9 -- what was done to me` -- an unreasonable requirement that meets (1A)(a)-(c) is unlawful under
  s 9 without asking s 9(1)'s own "purpose or effect" element again, since (1A)(c) states the same impairment for the
  group -- (1A) only supplies the "distinction based on race" element, and s 9(1)'s impairment must be shown for the
  person too.
- **F2** s 8(1), (2) -- every Part II question -- a special measure or a charity provision is answered first, even where
  the section's own elements are not met ("This Part does not apply") -- answer the section's elements first.
- **F3** s 18C(1) "otherwise than in private" -- `ss 18B, 18C, 18D -- offensive behaviour because of race` -- an act none
  of the s 18C(2) heads covers and no other fact shows to be public: NOTHING ("does not reach it", a scope limit with no
  "only") -- JUST FALSE (the act was done in private, so s 18C's condition fails).
- **F4** AHRC Act s 46P(1), (2) -- `AHRC Act s 46P, RDA s 6A(2) -- can I complain` -- a complaint that does not allege
  unlawful discrimination, or is not lodged by or for a person aggrieved: NOTHING (s 46P grants a right to lodge and is
  limited by its own wording; the list in (2) is not closed with "only") -- JUST FALSE ("unlawful discrimination means").
- **F5** AHRC Act s 46PB(2) "must" -- `AHRC Act s 46PB -- it may be a representative complaint` -- a complaint that does not
  identify the class or specify the complaints and relief: FALSE -- NOTHING, or TRUE once amended (s 46PA allows amendment
  with leave).
- **F6** AHRC Act s 46PO(2) "within 60 days after the date of issue" -- `AHRC Act s 46PO(2) -- the last day to apply to the
  court`, `AHRC Act s 46PO -- can I go to court` and the regulative rule -- the day of issue excluded (AIA s 36(1) item 6),
  so the 60th day after is the last day; an application on the day of issue is in time; a 60th day that is a Saturday, a
  Sunday or a holiday (an input list: public holidays where the application is made, days the registry is closed) moves on
  to the next day that is none of those (AIA s 36(2), (3)), and every day up to it is in time -- only the 60th day and
  the moved-on day in time, not the rest days between (the text names only those two).
- **F7** AHRC Act s 46PH(1)(b) "more than 24 months after the alleged acts ... took place" -- `AHRC Act s 46PH(1)(b) -- the
  last day before the complaint is late` -- the 24 months begin after the day of the act (AIA s 36(1) item 6) and end
  immediately before the corresponding day 24 months on, or at the end of that month if it has no such day (AIA s 2G(2)):
  28 February 2022 gives 29 February 2024, 29 February 2024 gives 28 February 2026; AIA s 36(2) is not applied, since
  lodging has no last day (the Act allows a complaint at any time; s 46PH(1)(b) only opens a discretion to end it); a
  continuing practice counted from the latest day it occurred (the `@desc` says so) -- the period read as starting on the
  day of the act, s 36(2) applied to a weekend last day, or counting from the first occurrence.
- **F8** s 15(1), (2), (3) -- `s 15 -- employment` -- each subsection is matched to its own actor and acts; an employer's
  worse treatment of a job seeker that is not a refusal to employ, and an agency's dismissal, are "does not reach it"
  under s 15 (s 9 may still) -- read the subsections across actors.
- **F9** s 14(1) "is invalid" -- `s 14(1) -- the union rule is invalid` -- a rule that does not keep people out by race (or
  immigrant status): NOTHING -- JUST FALSE ("is invalid" read as a "means"-like test).
- **F10** ss 26, 27(2) -- `ss 26, 27(2) -- is it a crime` -- conduct that is not victimisation: "no ... under the Act"
  (s 26 is a flat negative); the s 27(1) offence (hindering officials) is not asked -- NOTHING, leaving room for s 27(1).
- **F11** s 8(1), (2) over ss 16 and 17 -- `s 16 -- advertisements`, `s 17 -- inciting or assisting` -- s 8 applies to them
  as to the rest of Part II: advertising, inciting or assisting "in relation to the application of" a special measure, or
  an act done to give effect to a charity provision, is not unlawful -- s 8 reaches only the underlying act, so ss 16 and
  17 need no exception of their own (their "unlawful act" element already fails when the underlying act is excepted).

Sites decided without a fork line: ss 11, 12, 13, 14(2), 16, 17 outside their elements, and s 46PO(4) when the court is
not satisfied, answer NOTHING (prohibitions or grants limited by their own wording); s 10(1), ss 18A(1), 18E(1),
s 18AA(2), s 18C(1)(a), (b), s 46PO(1) and s 46PSA(2) when their "if" fails, ss 8(1), 8(2), 9(3), 12(3), 15(4), 15(5),
18A(2), 18D, 46P(3), 46POA(1), 46PSA(5), (7), RDA ss 6(2) and 6A(2) (flat negatives) and FCA Act s 33C(1) (a "where"
condition) answer the text's no.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. Most questions answer with a choice from a list rather than a MAYBE BOOLEAN:
the answers marked "does not reach it" are the NOTHING answers, and the answers beginning "no" or "not unlawful" are the
text's no (JUST FALSE). The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The period of s 46PO(2) is the regulative rule (`DO apply WITHIN 60`, `LEST BREACH`), run by EVALTRACE inside the question;
outside it the answer is "only if the court allows further time" (the period's no, softened by the court's power to extend).

## What the Act turns out to say

1. **"Descent" is in s 9 and s 18 only.** s 9(1) and (1A) and the s 18 reasons rule name "race, colour, descent or national
   or ethnic origin"; s 10, the specific sections (ss 11-15), and Part IIA (ss 18B, 18C) name only "race, colour or
   national or ethnic origin". A worker dismissed because of descent alone is outside s 15 and must rely on the general
   s 9 (which s 9(4) keeps open). Noted in the s 15 comment; not separately asserted.
2. **The immigrant extension in s 5 is patchy.** It adds "is or has been an immigrant" to ss 11, 12(1), 13, 14 and 15(1),
   (2) and to s 18, but not to s 9, s 10, s 12(2), s 15(3) or Part IIA. A union keeping someone out of work because they
   are an immigrant is not caught by s 15(3), though an employer or agency doing the same is caught by s 15(1), (2).
   Asserted (ss 12(2), 15(3)).
3. **A person of both Aboriginal and Torres Strait Islander descent is not "Aboriginal".** s 3(1) defines Aboriginal as a
   descendant of an indigenous inhabitant of Australia "but does not include a Torres Strait Islander". s 10(3) names
   both, so nothing turns on it there, but any reader of "Aboriginal" alone elsewhere should note it. Asserted (both
   descents count for s 10(3)).
4. **Three group routes, with different consent rules.** A representative complaint to the Commission needs no consent of
   the class members (AHRC Act s 46PB(4)); a representative application to the court under s 46PO needs every member's
   written consent (s 46POA(1)); a Federal Court group proceeding under Part IVA of the Federal Court of Australia Act 1976
   is expressly not a "representative application" (s 3(1)), so s 46POA does not apply to it; it needs 7 or more claims
   against the same person from the same, similar or related circumstances with a substantial common issue (FCA Act
   s 33C(1)); no group member's consent is needed (s 33E(1)) unless the member is a government, a Minister, a public body or
   an officer (s 33E(2)); a member may opt out before the date the court fixes (s 33J) and is otherwise bound (s 33ZB); and
   s 46PO(5) lets every group member benefit from the orders. A community-wide claim after a terminated complaint is
   therefore most naturally a Part IVA proceeding, which is still an application under s 46PO(1): the 60 days and leave
   still apply, and only the Federal Court hears it. Asserted.
5. **The costs rule is new and its reach is outside the text.** s 46PSA was substituted from 2 October 2024 by the
   Australian Human Rights Commission Amendment (Costs Protection) Act 2024 (No. 89, 2024); its application provision
   (Sch 1 item 7) is not in the compilation, so which proceedings it governs cannot be read from the deposited text. As
   worded, a claimant who loses to a respondent with a significant power or resource advantage (a State, a large employer)
   cannot be ordered to pay that respondent's costs unless the claim was vexatious or without reasonable cause, or the
   claimant's unreasonable conduct caused them (s 46PSA(5), (6)). Asserted.
6. **Leave is the rule, not the exception.** Under s 46PO(3A) every application to court needs the court's leave unless the
   President terminated the complaint as raising an issue of public importance (s 46PH(1)(h)) or as having no reasonable
   prospect of settlement by conciliation (s 46PH(1B)(b)). A complaint terminated as lodged more than 24 months after the
   act can still go to court, with leave. Asserted.
7. **Any step under a State law shuts the federal door for good.** RDA s 6A(2) deems a person who "made a complaint,
   instituted a proceeding or taken any other action" under a State or Territory law furthering the Convention never to
   have been entitled to complain under the AHRC Act about the same act, whatever happened to the State matter. Asserted.
8. **s 8(1)'s special-measures exception has its own exception.** A law letting another person manage an Aboriginal or
   Torres Strait Islander person's property without consent is caught by s 10 even if it is a special measure (s 8(1),
   s 10(3)). Asserted.
9. **s 18AA and s 27(2) are the same conduct twice, one word apart.** Victimisation is both unlawful under Part II (so it
   can be complained of as "unlawful discrimination", AHRC Act s 3(1)(b)) and an offence; s 18AA(2)(f) says "given" where
   s 27(2)(f) says "furnished". Every other unlawful act under Parts II and IIA is not an offence (s 26). Asserted.
10. **The State is answerable but cannot be prosecuted.** The Act binds the Crown (s 6(1)), so a State is answerable for
   its police (s 18A) and may be the respondent to a complaint, but "This Act does not make the Crown liable to be
   prosecuted for an offence" (s 6(2)): victimisation by the State itself is unlawful but not prosecuted, while the
   officer who did it may be. Asserted.

## Before this is worth relying on

- The application provision of the Costs Protection Act 2024 and the indexed penalty unit (Crimes Act 1914 s 4AA(1A)
  notifiable instrument), neither deposited; a holiday calendar for the place of filing (holidays are an input).
- A lawyer's view on forks F1, F3, F6, F7, F8 and F11 and on findings 1, 4 and 5; an independent test pass and a human gate.
- A respondent's seat (employer, State) if wanted, drawing on the same rules.
