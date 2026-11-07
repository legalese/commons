# Workforce Inspectorate Victoria Act 2020 (Vic), formerly the Wage Theft Act 2020 -- baseline encoding, the worker who reports underpayment

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Three modules and the cases:

- `wiv-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`) and the three
  commencement days the answers turn on (1 July 2021, 12 December 2025, 17 December 2025);
- `wiv-rules.l4` -- the law the questions share: the repealed provisions and the section of the Wage Theft Amendment Act
  2025 that repealed each, with the does-not-arise answers; the s 3 meaning of worker; the s 69A meanings of detriment and
  threat; the s 77 circumstances; the s 71(2) duty of an agency as one regulative rule with its trace helper; the table of
  offences and penalties;
- `wiv-seat.l4` -- 22 exported questions of the worker;
- `wiv-cases.l4` -- the cases.

The Act is small now (about 33,000 characters of body text, most of it side notes for repealed provisions), so what is
left of it is encoded whole except the machinery listed under Scope.

## Edition

- **Act:** Workforce Inspectorate Victoria Act 2020, Act No. 21/2020, Version No. 005, incorporating amendments as at 17
  December 2025 (the register's current version when read on 7 November 2026), deposited at
  `../../registers/source-bundle/workforce-inspectorate-victoria-act-2020.txt` (sha256 428c5cb3...55eba8 as committed), a
  plain-text conversion of the Word file the owner saved by hand on 7 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Former name:** the Wage Theft Act 2020, renamed by s 34 of the Wage Theft Amendment Act 2025 (No. 35/2025).
- **Numbers set elsewhere:** the Act states its own penalties (levels with their maxima in brackets) and its commencement
  days are in the endnotes. Not deposited, so inputs or left in units: regulations under s 79 (prescribed workplace
  entitlements matters, prescribed public construction; none is known to have been made) and under s 83 (transitional);
  the value of a penalty unit (Monetary Units Act 2004); the Sentencing Act 1991 (fines for bodies corporate and fines in
  place of imprisonment); the Project Development and Construction Management Act 1994 (the meaning of public
  construction); the Interpretation of Legislation Act 1984 (the effect of a repeal on earlier conduct).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (two
deliberately wrong assertions were run once in a scratch file, since deleted, and showed as "assertion failed"). The
output prints each diagnostic twice; the counts below are of distinct assertions.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wiv-dates.l4` | 0 | 0 | 0 | 0 |
| `wiv-rules.l4` | 0 | 0 | 0 | 0 |
| `wiv-seat.l4` | 0 | 0 | 0 | 0 |
| `wiv-cases.l4` | 0 | 0 | 154 | 154 |

Every expected value was worked by hand from the text, with the edges: the repeal on 12 December 2025 and the day before;
the Act's first day, 1 July 2021, and the day before; the functions of s 20(1)(ha) (12 December 2025) and (ia), (ib) (17
December 2025) on their first day and the day before; s 69A on 17 and 16 December 2025; the s 71(2) time on the last
specified day and the day after, answered on the day of the request, still running on the last day and late the day
after, across the new year and into a leap-year February (15 February 2028 plus 14 days is 29 February 2028); each kind of
detriment and each exclusion; each s 69A(1) head; each s 77(2) circumstance; the s 70(2) carve-out with and without
correct information and where it is not practicable; every penalty for a natural person and a body corporate; every
repealing section.

## Seat

**A worker who reports underpayment** (`wiv-seat.l4`): a person who is or was employed (paid or voluntary) or engaged
as an independent contractor, who has complained or is thinking of complaining to the Workforce Inspectorate Victoria
(formerly the Wage Inspectorate Victoria) about underpayment, or about public construction, and who may suffer for it.
"Is it still an offence for my employer to withhold my wages, and can an inspector come in?" (it does not arise, since
12 December 2025), "Am I a worker?", "Can the Inspectorate advise me, take my complaint, refer it, pass on what I told
it?", "Must the agency it referred my complaint to answer it, and has it in time?", "Can the Minister direct it?",
"Must it act fairly?", "Who answers if its people harm me?", "Is what was done to me an offence?", "Could I commit an
offence by what I give it?", the penalties, and the new name.

No second seat. The Act now puts duties on almost no one but officials: the Inspectorate and its Commissioner (no seat),
a government agency asked under s 71 (an official), its staff under s 77 (officials). The one duty on the public at large
is s 69A, a prohibition the worker's questions already answer; an employer seat would add little now that Part 2 is
repealed.

No seat for the Inspectorate, the Commissioner, the Minister, the Governor in Council or an agency: their judgments
("as appropriate", "satisfied ... in the public interest", "reasonable belief") are asked as facts; their duties that
touch the worker (ss 22, 71(2), 77) are encoded as what the worker can expect.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act states its own penalties; the
  regulations and the penalty-unit value are not deposited and are inputs or left in units.
- **The actors the text names.** Followed: the worker (s 3), the person who causes or threatens detriment (s 69A), the
  Workforce Inspectorate Victoria, the Commissioner and Acting Commissioner, the Minister, government agencies and bodies,
  the person who obtains information (s 77), the court and VCAT.
- **Judgments answered conditionally.** Followed: "reasonably necessary", "reasonably required", "as appropriate",
  "satisfied that it is in the public interest", "necessarily or reasonably done", "good faith", "reasonable belief",
  "contrary intention", "reckless", "material particular", "practicable" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "worker" (s 3), "detriment" and "threatens"
  (s 69A(3), (6)) are worked out; "workplace" beyond its "includes" and "does not include", "public construction within
  the meaning of the Project Development and Construction Management Act 1994", "government agency or body", "prescribed
  workplace entitlements matters" are asked.
- **One case.** One worker, and one complaint or one thing done to them.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The focus: what is left of the Act after the Wage Theft Amendment Act 2025, from the seat of a worker who reports
underpayment, with the repeals encoded as does-not-arise answers that name the amending Act.

**In:** the repeals (s 1(a), s 5, Part 2 (ss 6 to 18), s 20(1)(c) to (e), s 21(2), Part 4 (ss 32 to 62), Part 5 Division
1 (ss 63 to 65), ss 66 to 69, Part 5 Division 3 (the former ss 71 to 73), ss 76, 78), each with the repealing section of
No. 35/2025 and its commencement; s 2(2) (commencement on 1 July 2021, for the earliest answer); s 3 (worker, workplace,
public construction); s 20(1)(ha), (ia), (ib), (k) (the functions that reach a worker); s 22; s 24(1); s 69A; s 70;
s 71; s 75; s 77; ss 80, 81; the penalties of ss 69A, 70 and 77.

**Regulative rule:** one. s 71(2): the government agency or body MUST provide the notification or information WITHIN the
days the Inspectorate specified, LEST breach; run by EVALTRACE inside `Has the agency answered the Inspectorate in time`,
which takes only dates and yes/no facts, with the referral, the request and the 17 December 2025 commencement worked out
before the duty arises.

**Out, and why:**
- ss 1(b) to (d), 2(1), 4 (purposes, proclamation, Crown): machinery.
- s 19 (establishment, body corporate), s 20(1)(a), (b), (f) to (i), (ic), (id), (j), (l), (2), s 21 (functions and
  powers stated generally, with no fact test for a worker; (ic), (id) appear in the s 77 circumstance and in s 71).
- s 23 (staff), s 24(2), (3) (reports to the Minister), ss 25 to 30 (the Commissioner's appointment, terms, vacancy,
  removal, acting appointment, functions), s 31 (delegation; read only in the s 77(3) input): an official's office.
- s 74 (validity of acts despite a defective appointment): could be added as "is the decision about my complaint
  invalid because of the Commissioner's appointment?" (no, on its grounds).
- s 79 (regulations), s 82 (the sitting Commissioner continues), s 83 (transitional regulations; repealed on the second
  anniversary of its commencement, 12 December 2027): machinery.
- The repealed provisions themselves: their text is not in the deposited version.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 2 and the endnotes ("came into operation on 1 July 2021: section 2(2)") -- `what the Act says now about a
  repealed provision on` -- every former provision in force from 1 July 2021 to 11 December 2025 -- some provisions may
  have been proclaimed earlier under s 2(1); the endnotes record only s 2(2).
- **F2** s 3 "workplace ... does not include a part of any premises that is the domestic home of a person" -- `s 3 --
  worker` -- work done only in that part: JUST FALSE -- such work may still be "in relation to" a workplace elsewhere.
- **F3** s 20(1)(ha) (from 12 December 2025), (ia), (ib) (from 17 December 2025) -- the advice, complaint and referral
  questions -- a day before the function commenced: NOTHING (the earlier version is not deposited and may have had a
  like function) -- JUST FALSE.
- **F4** s 69A(1)(a), (c), (e), (f) "a complaint to Workforce Inspectorate Victoria" -- `Is it an offence to do this to me
  because I complained` -- any complaint, including one about underpayment -- only a complaint the Inspectorate has a
  function to receive, which since 12 December 2025 is one regarding public construction (s 20(1)(ia)) (finding 3).
- **F5** s 69A, inserted by No. 57/2025 s 30 from 17 December 2025 -- the same -- conduct before that day: JUST FALSE (the
  offence did not exist) -- NOTHING (a repealed provision may have covered it; finding 2).
- **F6** s 80 "as far as it relates to any period after that commencement" -- `Does the old name in my document now mean
  the new one` -- a period from 12 December 2025 inclusive is after the commencement -- from 13 December 2025. The
  commencement of "Part 2 of the Wage Theft Amendment Act 2025" is taken as 12 December 2025, the day ss 4 to 34 and 40
  commenced (endnotes); which sections form its Part 2 is not in the deposit.
- **F7** s 69A(6) -- `s 69A(6) -- detriment` -- the person picks the one kind that best describes what was done; an
  employment kind is JUST FALSE even where it was also harassment -- harassment in connection with employment is still
  detriment under (a)(ii) (finding 4).
- **F8** s 71(2) "within a reasonable time, as specified by the Workforce Inspectorate Victoria" -- `Has the agency
  answered the Inspectorate in time`, `By when must the agency answer the Inspectorate` -- the specified time governs,
  counted in plain days from the request, the last day inside; no time specified: an explicit "reasonable time" answer,
  not decided -- a reasonable time is a separate limit on what may be specified.
- **F9** s 71(2) "A government agency or body that receives a request" -- the same -- no referral or no request: no duty
  (the duty's own "that receives a request" unmet) -- NOTHING.
- **F10** s 24(1) "except in relation to the following" -- `Can the Minister direct the Inspectorate about this` -- an
  excepted function: JUST FALSE -- NOTHING (the Minister may have another power elsewhere).
- **F11** s 70(2) "without indicating the respect in which it is false or misleading and, if practicable, providing
  correct information" -- `Is it an offence for me to give this to the Inspectorate` -- both done (or correct
  information not practicable): JUST FALSE -- NOTHING.
- **F12** s 69A(3) "A person threatens ... if" -- the s 69A question -- a threat with neither intent nor recklessness:
  JUST FALSE -- NOTHING.
- **F13** s 77(3) "The Commissioner may disclose" with s 31 (delegation of the Commissioner's functions under this Act)
  -- `May the Inspectorate pass on information about me` -- the Commissioner or a delegate -- the Commissioner only.
- **F14** s 20(1)(k) "to refer matters, as appropriate, to other bodies" -- `Can the Inspectorate refer my complaint to
  another body` -- any body, if the Inspectorate considers it appropriate -- government bodies only, as in (ib).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definition of "worker" (s 3), the "if" definition of a threat (s 69A(3)), the flat negatives
of "workplace ... does not include" (s 3) and "detriment ... does not include" (s 69A(6)(b)), the "unless" of ss 77(1) and
80, the "except" of s 24(1), and the repeals (a provision repealed by its own amending Act's words, on and after the day of
repeal) give `JUST FALSE` or a does-not-arise answer. `NOTHING` is answered where a function or prohibition does not reach
the case (ss 20(1)(ha), (ia), (k), 22, 24(1) for a direction that is not general, 69A outside its "because", 70 without the
belief or knowledge, 77 for information not obtained under this Act, 80 for an earlier period, 81 before the change)
(*limited by its own wording*), for harm outside the open list of s 69A(6)(a) "detriment includes" (*open list*), where
the Act is silent (the fines of ss 69A and 77 for a body corporate, of s 70 for anyone else) (*silent*), and for conduct
while a repealed provision was in force (*outside the sources*).

## What the Act turns out to say

1. **The Act no longer touches wage theft directly.** Since 12 December 2025 there is no wage theft offence (Part 2, ss 6
   to 18, repealed by s 7 of No. 35/2025), no inspectors' powers (Part 4, ss 32 to 62, s 20), and no proceedings division
   (Part 5 Division 1, s 21). For a worker underpaid on or after that day the Act's answer is that the offence and the
   powers do not arise. Asserted. Other law (the Fair Work Act 2009 of the Commonwealth, the Long Service Leave Act 2018)
   is not encoded here.
2. **Underpayment before 12 December 2025.** The deposited version does not carry the repealed text, and whether a
   repealed offence still reaches conduct of that time turns on the Interpretation of Legislation Act 1984 and on any
   transitional regulations under s 83 (which may be retrospective to the day of Royal Assent, 2 September 2025, s 83(2)(a)),
   none deposited. Answered "not answered here", naming the amending Act. Asserted.
3. **The protection outruns the function.** s 69A protects a person who has made, or is considering, "a complaint to
   Workforce Inspectorate Victoria", of any kind, but since 12 December 2025 the only function of receiving complaints is
   for public construction (s 20(1)(ia)); a worker's underpayment complaint is still "a complaint" in s 69A's words.
   Encoded on that reading (F4). Asserted with the underpayment complainant who is harassed.
4. **Dismissal is not detriment.** s 69A(6)(b) excludes discrimination, disadvantage or adverse treatment in or in
   connection with employment, dismissal, prejudice in employment and disciplinary proceedings: the reprisal an employer
   is most likely to take against a worker who complains is not an offence under s 69A. Harassment at work falls under
   both (a)(ii) "intimidation or harassment" and (b)(i) "adverse treatment in connection with employment"; the encoding
   lets the person choose the kind (F7). Asserted.
5. **s 69A came from the labour hire Act, not the wage theft Act.** It was inserted by s 30 of the Labour Hire Legislation
   Amendment (Licensing) Act 2025 (No. 57/2025) from 17 December 2025, five days after the Wage Theft Amendment Act 2025
   repealed ss 66 to 69 in the same Division. Before 17 December 2025 the encoding answers no (F5). Asserted.
6. **Two sections 71.** The new s 71 (Division 2A, inserted by s 37 of No. 35/2025 from 17 December 2025) reuses the
   number of the former s 71 in Division 3, repealed by s 27 of the same Act from 12 December 2025. The repeal answer for
   "Part 5 Division 3 (the former ss 71 to 73)" means the old one; the s 71 questions mean the new one.
7. **Penalties.** s 70 gives a fine for a body corporate and imprisonment only for anyone else; ss 69A and 77 give one
   figure with no separate one for a body corporate; the converted text of s 70 prints its penalty lines without the
   word "Penalty:" (as the Word file has it, or a conversion artefact; read as the penalty). Where the Act gives no figure
   the answer is empty (Sentencing Act 1991, not deposited). Asserted.
8. **No right to be told.** s 71 lets the Inspectorate ask an agency what it did with a referred complaint, and s 20(1)(id)
   lets it report to the Minister; nothing requires anyone to tell the person who complained. Recorded in the s 71
   question's description.
9. **Confidentiality covers only "this Act".** s 77(1) binds information obtained "under this Act"; the Inspectorate
   also has functions "under any other Act" (ss 20(1)(l), 22, 30(1)(b), 31), whose information s 77 does not reach.
   s 77(1) says "obtains ... in performing the person's functions or exercising the person's powers", (2) "acquired in
   performing a function or exercising a power", (3) "acquired in carrying out a function": read as the same. Asserted
   as NOTHING.
10. **Functions without powers.** s 20(1)(a), (b), (j) still speak of "rights and obligations under this Act" and of
    promoting, monitoring and enforcing "compliance with this Act and the regulations", but after the repeals the Act
    imposes almost no obligations on employers and gives no enforcement powers; s 20(1)(b) has little left to enforce.
    Out of scope; recorded.
11. **Deposit metadata.** The subject's `.meta.json` records `landing_read_at_utc` as "2026-11-07T2026-11-07T06:25:32ZZ",
    a doubled timestamp. Not changed here (the deposit is not this encoding's to alter).

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The repealed text (Version No. 004 or earlier) for conduct before 12 December 2025; the Interpretation of Legislation
  Act 1984 on the effect of a repeal; any regulations under ss 79 and 83; the penalty unit value; the Sentencing Act 1991.
- A lawyer's view on findings 2, 3, 4 and 9 and forks F3, F4, F5, F7, F8; an independent test pass; a human gate.
- A link from the Fair Work Act 2009 encodings for the general protections a dismissed worker has instead of s 69A.
