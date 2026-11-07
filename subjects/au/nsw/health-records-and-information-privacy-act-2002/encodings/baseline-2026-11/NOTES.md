# Health Records and Information Privacy Act 2002 (NSW) -- baseline encoding, the individual whose health information it is

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 27 May 2024). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer; case-by-case sites listed in the fork
register). Five regulative rules (a private sector person answering a request for access, s 27(1), and for amendment,
s 34(1); nominating a doctor after a refusal and the organisation then giving the doctor access, s 30(3), (5), the
second under `HENCE`; complaining to the Privacy Commissioner in time, s 42(3); applying to the Tribunal in time,
s 48(2)), each run by `EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a person meets who
brings or answers a claim about their health information: getting their records (for a medical negligence or other
claim), having them corrected, how long they must be kept, whether a use or disclosure was allowed, and the complaint
route to the Privacy Commissioner and NCAT with its time limits and damages caps.

## Edition

- **Act:** Health Records and Information Privacy Act 2002 No 71, corpus document
  `nsw_legislation:2024-05-27/act-2002-071` (in force 27 May 2024), deposited at
  `../../registers/source-bundle/act-2002-071.txt` (text sha256 b0ac18f0...c558469 as recorded in its `.meta.json`), taken
  from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot
  challenge. Not the authorised text.
- **Not deposited:** the Health Records and Information Privacy Regulation (prescribed fees, exempt health information,
  prescribed circumstances); the Privacy and Personal Information Protection Act 1998 (Part 5 internal review and NCAT
  review for public sector agencies, with its own time limits and damages); the Government Information (Public Access)
  Act 2009 (access conditions for public sector agencies, s 22(3)); the State Records Act 1998; the Interpretation Act
  1987 (counting time); the Crimes (Sentencing Procedure) Act 1999 (the value of a penalty unit); the Commonwealth
  Privacy Act 1988 (small business operator, agency); the commencement proclamations (Schedule 1, s 21, Part 6 and
  s 28 commenced on 1 September 2004 for most organisations, but that date is not in the deposited text, so whether
  conduct or information falls before or after it is asked).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hrip-claims.l4` | 0 | 0 | 0 | 0 |
| `hrip-claims-cases.l4` | 0 | 0 | 164 | 164 |

Every expected value was worked by hand from the text, with the edges: an answer on the 45th day and the 46th, across a
year end and through 29 February 2028 (ss 27, 34); being still within the 45 days on the last day and taken to have
refused the day after (ss 27(6), 34(5)); a fee notice on the 45th day and the 46th (s 27(4)); a doctor nominated on the
21st and 22nd day, and given access on the 21st and 22nd day after the nomination (s 30); a complaint on the last day of
6 months from 31 August (28 February, and 29 February in a leap year) and the day after, and with a later time allowed
before and after the six months (s 42(3)); an NCAT application on the 28th and 29th day, with a recommended day after
and before the report, and on the recommended day itself (s 48(2)); retention from 29 February (s 25); each s 29 ground
made out and not, the s 30 split between a threat to the individual and to another person, a public sector agency
relying on a ground; damages for a body corporate and others and with each s 54(2) condition failing; a fee at and one
cent over a prescribed maximum.

## Seat

**The individual whose health information it is**: a patient, client or former patient of a health service, or anyone
whose health information an organisation holds; under Part 6 the complainant. Where the individual cannot act, their
authorised representative asks the same questions (ss 7, 8). Every exported question is one that person would ask
("Must they give me my records?", "By when must they answer?", "Can I nominate a doctor?", "Must they correct my file?",
"How long must my records be kept?", "Were they allowed to disclose it?", "By when must I complain?", "Can I go to NCAT,
and by when?", "How much can NCAT award me?", "Can I be fined for missing conciliation?"). The organisation, the Privacy
Commissioner, the Tribunal and officials get no seat: their duties are encoded as what the individual must be given and
by when (for example the organisation's 45 days to answer, s 27(1), as "Has my access request been answered in time?").

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, but the regulation is not deposited: the
  prescribed maximum fee, prescribed exempt information and prescribed circumstances are asked. The Act's own numbers
  (45, 21, 28 and 7 days, 6 months, 7 years, age 25, $40,000 and $10,000, 10, 50 and 100 penalty units) are encoded.
- **The actors the text names.** Followed: the individual, the authorised representative, the organisation (public
  sector agency or private sector person), the health service provider, the nominated registered medical practitioner,
  the Privacy Commissioner, the Commonwealth Privacy Commissioner, the Tribunal.
- **Judgments answered conditionally.** Followed: whether a s 29 ground holds, whether a requested form of access is
  unreasonable or inappropriate (s 28(3)), what the organisation is satisfied of (s 34(3)), whether information is in
  fact deficient (HPP 8), whether a use or disclosure ground's conditions are met (HPP 10, 11), capacity (s 7), the
  Commissioner's satisfaction (s 43(2)), the Tribunal's satisfaction of loss or harm (s 54(2)(b)), reasonable excuse
  (s 46(3)) and reasonable practicability (HPP 8(3)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** "Personal information" (s 5), "health information" (s 6),
  "authorised representative" and "child" (s 8), "private sector person" and "public sector agency" (s 4, as a choice)
  are worked out; "small business operator" and "agency" (Commonwealth Privacy Act), "group practice" (s 16(3), glossed),
  "registered medical practitioner" and the excluded classes of s 5(3)(b)-(o) are asked.
- **One case.** One individual and one organisation, about one body of health information or one piece of conduct.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 5, 6 (personal and health information); ss 7, 8 (capacity and authorised representatives); ss 4, 11, 14, 17,
21, 42(1), (2), (5) (who is bound and where to complain); HPP 7 with ss 19(3), 22(3), 23, 29, 30(1), (2) (access);
s 27(1), (2), (4), (6) (answering an access request, fees); s 28 (form of access); s 30(3), (5) (doctor nominated);
HPP 8(1), (2), (3), (4) with ss 20, 23, 34, 35(1) (amendment, notations); s 25(1) (retention); HPP 10(1), (2), HPP 11(1),
(2) with s 16(1) (use and disclosure); s 42(3) (time to complain); s 43(2) (Commissioner declining); s 46(3), (4), s 60(5)
(conciliation and representation); s 48 (applying to NCAT); s 52(3) with s 53 (costs); s 54(1)(a), (2) (damages); s 70
(intimidation); s 73 (fees).

**Out, and why:**
- ss 1-3, 9, 10, 12, 13, 18, 19(1), (2), (4), (5), 22(1), (2), 24, 74-78, Schedule 2: machinery, interpretation and
  transition.
- s 15 (news media), s 17A (Multicultural NSW translation): narrow exemptions; a claimant against a news medium or the
  translation service is outside this encoding.
- s 25(2)-(5), ss 31, 32, 35(2)-(4), 36, 37: steps the organisation takes (disposal records, identity checks, informing
  of alternative arrangements, notifying recipients of a notation), with no number or right the individual exercises
  beyond those encoded.
- Part 5 (health privacy codes) and s 62 (Commissioner's exemptions): a code or direction may modify the HPPs; whether
  one applies is not knowable from the deposited text. The answers assume none applies.
- ss 43(1), (3), 44, 45, 46(1), (2), (5)-(7), 47, 49-51, 54(1)(b)-(f), (3), Part 7 (ss 58-67): the Commissioner's and
  Tribunal's procedure and open powers; s 47 enters only as the report that opens s 48.
- ss 68, 69, 75A(3): offences by public sector officials, traffickers and identifier misusers, prosecuted by the State;
  the individual has no step to take under them.
- s 71 (no civil cause of action) and s 72 (protection from liability): stated as finding 9, not asked.
- HPP 1-6, 9, 12-15: duties on collection, notice, security, accuracy, identifiers, anonymity, transfers and linkage
  that ground a complaint but turn wholly on reasonableness; HPP 10(3)-(5), 11(3)-(6) (named agencies, ministerial
  briefing, onward use, emergency holding limits).
- Complaints against public sector agencies beyond the route: the internal review and NCAT review are in Part 5 of the
  PPIP Act (s 21), not deposited.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 25(1), 27(1), (4), 30(3), (5), 34(1), 42(3), 48(2) -- every date question -- periods are counted from the
  day after the event (Interpretation Act 1987 s 36(1), not deposited); a period of months or years ends on the same day
  of the month, or that month's last day where shorter -- the day of the event counts; or a period from 29 February or
  31 August ends on 1 March.
- **F2** the same provisions -- the last day is not moved when it falls on a weekend or public holiday -- it moves to the
  next business day under the Interpretation Act 1987 s 36(2).
- **F3** ss 4, 17, 21 -- `Where do I take my health privacy complaint` -- conduct of ICAC, the NSW Police Force, LECC
  and the Crime Commission in their administrative and educative functions goes to internal review under s 21 (the
  Inspectors and their staff are treated alike) -- the Inspectors are not "public sector agencies" and have no route.
- **F4** s 27(1), (2), (4) -- `Has my access request been answered in time` -- a written fee notice under s 27(4) given
  within 45 days counts as a response -- only providing or refusing access is a response (s 27(2)), so a fee notice
  leaves the organisation taken to have refused after 45 days.
- **F5** s 27(4) "need not provide access until 7 days after payment" -- `The day access can no longer be held back
  after I pay` -- the answer is the 7th day after payment, the first day access can be required; no later deadline is
  read in -- access must be given by that day.
- **F6** HPP 8(1), s 34(3) -- `Must they correct my health information` -- for a private sector person s 34(3)'s
  satisfaction is a complete answer to HPP 8(1); for a public sector agency HPP 8(1) turns on whether the information is
  in fact deficient -- s 34(3) gives only a power to refuse a request, and HPP 8(1) still binds a private sector person
  whose information is in fact deficient.
- **F7** s 25(1)(b) "until the individual has attained the age of 25 years" -- `Until when must my records be kept` --
  the duty ends on the 25th birthday (28 February for a 29 February birthday) -- the day after; or 1 March.
- **F8** HPP 10(1), 11(1) -- `Were they allowed to use or disclose my health information` -- each paragraph's own
  conditions are asked as one fact, and a use or disclosure for the primary purpose is `NOTHING` (HPP 10 and 11 are
  silent on it) -- each condition asked separately; or the primary purpose answered `JUST TRUE`.
- **F9** s 46(3) "without reasonable excuse" -- `The largest fine for missing conciliation` -- with a reasonable excuse
  (or no written notice) the maximum is 0 -- `NOTHING`, leaving the excuse to the court.
- **F10** s 48(2)(b) "the day ... recommended ... as the day after which an application may be made" -- `Is my NCAT
  application in time` -- an application on or before the recommended day is too early -- the recommendation only moves
  the last day, and an earlier application is in time.
- **F11** s 43(2)(f) "is satisfied that the person has made a complaint ... to the Commonwealth Privacy Commissioner" --
  `Can the Commissioner decline my complaint` -- the Commonwealth complaint, as the individual states it, is taken as the
  Commissioner's satisfaction -- the Commissioner's satisfaction asked separately.
- **F12** s 7(3) with s 8 -- `Can this person act for me` -- a capable individual's express authority lets any
  authorised representative act; a person who is not an authorised representative cannot act under s 7 even with it
  (s 26(2) still lets the individual authorise another person to have access in their place) -- s 7(3) lets the
  individual authorise anyone.
- **F13** s 70 -- `The largest fine for pressuring me` -- an attempt counts the same as a success, and an application
  under PPIP Act Part 5 counts only where it concerns an HPP or health privacy code; the answer is 0 where s 70 creates
  no offence -- `NOTHING` for conduct outside s 70.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags and follows these rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
> The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
> Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

> - **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.


Applied here: "means" definitions (ss 5(1), 6, 8(1)), flat exclusions (s 5(3) "does not include", s 14 "Nothing in this
Act applies", s 17 "does not apply", s 42(5), s 48(3) "cannot apply", s 46(4) "not entitled ... except"), "if", "only
if" and "unless" conditions (s 7(3), s 8(1)(c), s 27(4), s 35(1), s 43(2), s 48(1), s 54(2), HPP 8(2), (3), HPP 10(1),
11(1)) and periods the text fixes (ss 27(1), 30(3), (5), 34(1), 42(3), 48(2)) answer no when they fail; a public sector
agency's access conditions (s 22(3), pointing outside the sources), retention by anyone other than a private health
service provider (HPP 5 and the State Records Act), a use or disclosure for the primary purpose (silent) and a fee for
an unlisted matter (s 73(1), a list not closed with "only") answer `NOTHING`; the sites with no convention each have a
fork line above (F4, F5, F8, F9, F10, F13).

## What the Act turns out to say

1. **The damages caps are $40,000 against a body corporate and $10,000 against anyone else** (s 54(1)(a)), and only for
   conduct after the first 12 months of Schedule 1 and where NCAT is satisfied of financial loss or psychological or
   physical harm (s 54(2)). This is the private sector route only; a claim against a public sector agency goes through
   Part 5 of the PPIP Act (s 21), whose remedies are not deposited. Asserted.
2. **NCAT is reachable only through a Privacy Commissioner's report.** s 48(1) allows an application "only if the
   complaint was the subject of a report ... under section 47", and s 47 reports follow only the further-investigation
   course of s 45(1)(b). A complaint the Commissioner declines (s 43), finds no prima facie case on (s 44), conciliates
   (s 46) or treats as resolved (s 45(1)(c)) never reaches the Tribunal. Asserted (no report: `JUST FALSE`).
3. **Silence is refusal after 45 days** for a private sector person, for access (s 27(6)) and amendment (s 34(5)); a
   notation can then be required (s 35(1)). Asserted, on the 45th and 46th days.
4. **s 30 is narrower than s 29(a).** s 29(a) lets access be refused for a serious threat to the life or health "of the
   individual or any other person"; the doctor route of s 30 applies only where the threat is to the individual. Asserted.
5. **A public sector agency cannot rely on HPP 8(4)** to refuse an amendment: s 20 applies HPP 8 "despite HPP 8 (4)".
   A private sector person keeps the s 23 and HPP 8(4) exemptions. Asserted.
6. **Information collected before Schedule 1 commenced** is reachable by access and amendment only if it is one of the
   kinds in s 19(3)(a)-(h), and a private sector person need give only "an accurate summary" of information collected
   before s 28 commenced (s 28(4)), "despite anything to the contrary in this Part or HPP 7". Asserted.
7. **A child's records may be kept for less than 7 years after the last service.** s 25(1)(b) keeps information
   collected while under 18 only "until the individual has attained the age of 25 years", whatever the date of the last
   service; information collected at 19 from the same person is kept 7 years from the last service. Asserted (a child's
   records kept to 25, four years after a service at 20).
8. **The complainant can be fined.** s 46(3) makes failing, without reasonable excuse, to comply with a written notice to
   appear in conciliation an offence: 10 penalty units, 50 for a body corporate, and it binds complainant and respondent
   alike. Asserted.
9. **No civil cause of action.** s 71(1) bars the Act from giving rise to or being taken into account in any civil cause
   of action; its remedies are only those under its own procedures. Not asked; it bears on a negligence claim that
   relies on a breach of the HPPs.
10. **s 48(2)(b) is worded as a starting day as well as a deadline** ("the day after which an application may be made").
    Read as making an earlier application premature (fork F10). Asserted on the recommended day and the day after.
11. **The commencement of Schedule 1 is not in the Act.** ss 19, 21(3), 28(4), 42(5) and 54(2)(a) all turn on it, and
    s 54(2)(a)'s "12-month period following the date on which Schedule 1 commences" cannot be computed from the deposited
    text; Schedule 2 cl 3 adds a later commencement for State owned corporations brought in by the 2024 amendments.
    Asked as facts.
12. **s 42(3) lets the Privacy Commissioner allow "such later time"** with no limit and no condition, and does not say
    whether it may be allowed after the 6 months have run. The answer for a late complaint is "late, but the
    Commissioner may allow a later time". Asserted.

## Questions (exported)

`hrip-claims.l4` (29), in the Act's order: `Is this my health information under the Act` (ss 5, 6); `Can this person
act for me` (ss 7, 8); `Where do I take my health privacy complaint` (ss 4, 11, 14, 17, 21, 42); `Must they give me
access to my health information` (HPP 7, ss 19(3), 22, 23, 29, 30); `The last day to answer my access request`; `Has my
access request been answered in time` (rule) (s 27(1), (6)); `The day access can no longer be held back after I pay`
(s 27(4)); `In what form will I get access` (s 28); `The last day to nominate a doctor`; `Where does my doctor
nomination stand` (rule, with HENCE) (s 30); `Must they correct my health information` (HPP 8, ss 20, 23, 34(3)); `The
last day to answer my amendment request`; `Has my amendment request been answered in time` (rule) (s 34(1), (5)); `Can
I make them add my statement to the record` (HPP 8(2), s 35); `Can I have the recipients told of the correction` (HPP
8(3)); `Until when must my records be kept` (s 25(1)); `Were they allowed to use or disclose my health information`
(HPP 10, 11, s 16); `The last day to complain`; `Is my complaint in time` (rule) (s 42(3)); `Can the Commissioner
decline my complaint` (s 43(2)); `The largest fine for missing conciliation` (s 46(3)); `Can I be represented before
the Commissioner` (ss 46(4), 60(5)); `Can I apply to NCAT` (s 48(1), (3)); `The last day to apply to NCAT`; `Is my NCAT
application in time` (rule) (s 48(2)); `Can I be ordered to pay the inquiry costs` (s 52); `The most NCAT can award me in
damages` (s 54); `The largest fine for pressuring me` (s 70); `Can they charge me this fee` (s 73).

Situations: the access group arises once a request is made, the s 30 questions only after a refusal for a threat to
the individual's own life or health; the amendment group once a correction is sought; the Part 6 group only for a
complaint against a private sector person (`Where do I take my health privacy complaint` answers which route applies),
the NCAT questions only after a Privacy Commissioner's report, the conciliation questions only once a written notice to
appear is given; s 70 only where someone has pressed the individual.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation and
  whether the Act has been amended since 27 May 2024.
- Deposit the Health Records and Information Privacy Regulation (fees, exempt information, prescribed circumstances),
  the PPIP Act (public sector review, which s 21 borrows) and the GIPA Act (s 22(3)); deposit the Interpretation Act 1987
  and settle forks F1 and F2; record the commencement dates.
- Have a lawyer review the forks, especially F4 (fee notice as a response), F6 (amendment) and F10 (premature NCAT
  application).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
