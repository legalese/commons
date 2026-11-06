# Health Complaints Act 2016 (Vic) -- baseline encoding, the person who complains and the general health service provider

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Six files:

- `hca-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`), in the shape of the
  Coroners Act 2008 encoding's;
- `hca-rules.l4` -- the law both seats use: the s 3 definitions (health service, general health service, party), the heads
  of ss 5, 6 and 7 and the routes to the Commissioner, the s 8 last day, the Schedule 2 general code of conduct clause by
  clause, the provider's duties with deadlines as one regulative rule (ss 35, 39, 41, 52, 58) with its trace helper, and the
  table of offences and penalties;
- `hca-seat.l4` -- 33 exported questions of the person who complains;
- `hca-seat-provider.l4` -- 18 exported questions of the general health service provider;
- `hca-cases.l4`, `hca-cases-provider.l4` -- the cases, the second with mirror cases (the same facts from both seats).

## Edition

- **Act:** Health Complaints Act 2016, Act No. 22/2016, Version No. 011, incorporating amendments as at 22 October 2025 (the
  register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/health-complaints-act-2016.txt` (sha256 6ca242a9...81cbe3 as committed), a plain-text
  conversion of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act fixes its own periods (3, 6 and 12 months, 12 weeks, 10 and 20 business days, 28 days)
  and penalties in penalty units. Not deposited, so each is an input or left as units: the Health Complaints Regulations
  (prescribed services under s 3 "health service" (j), a prescribed general code of conduct (s 154(2)), other prescribed
  codes, prescribed offences for ss 87, 91, 96); the complaint handling standards made under s 133 (Schedule 1's interim
  standards are not encoded); the value of a penalty unit (Monetary Units Act 2004); public holidays for business days.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hca-dates.l4` | 0 | 0 | 0 | 0 |
| `hca-rules.l4` | 0 | 0 | 0 | 0 |
| `hca-seat.l4` | 0 | 0 | 0 | 0 |
| `hca-seat-provider.l4` | 0 | 0 | 0 | 0 |
| `hca-cases.l4` | 0 | 0 | 179 | 179 |
| `hca-cases-provider.l4` | 0 | 0 | 86 | 86 |

Every expected value was worked by hand from the text, with the edges: the 12 months of s 8 on the last day and the next,
from 29 February 2028 (28 February 2029); the 3 months of s 5(2)(c) from 30 November 2026 (28 February 2027) with the
provider resolving inside and outside them; the 6 months of s 31 from 31 August 2027 (29 February 2028); the 10 business
days of s 15(2) and s 61 at 9 and 10, and a longer period set; the 20 business days of ss 35(2), 41(2) at 20 and 21; the 12
months of s 39(2); the regulative rule done on the last day, done the day after, still open on the last day and late the
day after, with and without a reasonable excuse; the 12 weeks of s 90 across February; the 28 days of s 101 from service
and from reasons; every s 14 ground; each code clause on both sides; mirror cases from both seats.

## Seats

**The person who complains** (`hca-seat.l4`): first the person who received or sought the health service, and with them
the two others the Act lets complain, another person (s 6, often family) and the person's carer (s 7). "Was it a health
service, and a general one?", "Can I complain to the provider?", "Can I complain to the Commissioner now, and by when?",
"Must I confirm in writing?", "Am I a party?", "Can the Commissioner refuse, decline, take it up again, go on after I
withdraw, refer it, or hold back a notice from me?", "Can conciliation begin, what can I say about it, can it be used in
court?", "What must I be given?", "Can the Commissioner investigate, was I given enough notice of the hearing, can I have
the report?", "Am I protected, is it an offence to treat me so, may I have a lawyer, is it a reasonable excuse?", "Did the
provider break the code of conduct?", and the penalties.

**The general health service provider** (`hca-seat-provider.l4`), the further seat the guide welcomes: the Act puts the
code of conduct, the Commissioner's notices and the prohibition orders on this person, the unregistered practitioner (or a
registered one working outside their profession). "Am I covered?", "Does my practice break the code?", "Have I done what
the Commissioner required in time, and was the time set lawful?", "Can my name be published?", "Can an interim prohibition
order or prohibition order be made against me, until when, and by when may I go to VCAT?", "May I provide this service?",
and the penalties. Both seats draw on `hca-rules.l4`, so they cannot disagree about the law; mirror cases assert that they
agree. Registered practitioners are dealt with under the National Law (s 26) and are not given a seat here.

No seat for the Commissioner, the Minister, a National Board, the Disability Services Commissioner, VCAT or the Advisory
Council: their beliefs, satisfaction and decisions are asked as facts; their duties to the person (ss 13, 28, 38, 44, 49,
61) are encoded as what the person must be given.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; the regulations,
  standards and penalty-unit value it relies on are not deposited and are inputs or left in units.
- **The actors the text names.** Followed: the complainant, the person who received or sought the service, another
  person, the carer, the health service provider, the general health service provider, the Commissioner, a National Board,
  Ahpra, the Disability Services Commissioner, VCAT.
- **Judgments answered conditionally.** Followed: "unreasonable", "unreasonable or inappropriate", "reasonably believes",
  "is satisfied", "public interest", "serious risk", "safe and ethical", "appropriate", "reasonable excuse" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "health service", "general health service",
  "party", "code of conduct" (as Schedule 2) are worked out; "health profession" (National Law), "carer" (Carers
  Recognition Act 2012), "duty of candour" (Health Services Act 1988), "relevant law" matters, "prescribed offence" are
  asked.
- **One case.** One complaint about one health service, or one provider's practice.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The focus: complaints about health services, and the general code of conduct for unregistered practitioners. Parts 2 to 8
are encoded where they give the person a fact test, with s 3 and Schedule 2.

**In:** ss 3(1) (health service, general health service, party, code of conduct, general code of conduct, relevant law,
relevant notice or information), 5, 6, 7, 8, 9, 11, 14, 15(2), 21, 22, 23, 24, 25, 26(2), 28, 29, 30, 31, 35, 36, 38, 39,
40, 41, 42, 43, 44, 45, 49(1), (2), 51(3), 52, 58, 61(1), 76, 77, 78, 79, 80, 81 (penalty), 82, 83(1), (2), 87(1), (2), 90,
91, 91A, 93, 95, 95A, 96, 98, 101, 102, 154, Schedule 2 clauses 1 to 17, and the penalties of ss 35, 39, 41, 43, 52, 58,
68, 70, 80, 81, 93, 98, 102, 129, 150.

**Regulative rule:** one, over five acts. ss 35(3), 39(3), 41(3), 52, 58: the health service provider MUST give the
written response, the report on the undertaking, the documents, or the response to an investigation or follow up report
WITHIN the days from the notice to the last day allowed, LEST breach; run by EVALTRACE inside `Have I done what the
Commissioner required in time`, which takes only dates and yes/no facts. A reasonable excuse turns lateness into no
offence for ss 39, 52, 58 (fork F13).

**Out, and why:**
- ss 1, 2, 4 (purposes, commencement; the health service principles are named in the s 5(1)(c) input, not tested).
- ss 10, 12, 13, 15(1), (3), 16 to 20, 27, 32 to 34, 37, 46 to 48, 49(3), 50, 51(1), (2), (4), 53 to 57, 59, 60, 61(2),
  62 to 67, 69, 71 to 75: the Commissioner's procedure and powers, with no fact test for the person beyond what is asked
  (s 13(3) notice and s 20 decision could be added as "what must I be given").
- ss 68, 70, 72, 73 (warrants and hearing notices): in only through the penalty table and the ss 77, 78 excuse.
- ss 84 to 86, 88, 89, 92, 94, 97, 99, 100 (public health warnings, revocation, correction, publication, variation of
  orders): the Commissioner's; s 88(2) (a warning statement must be revoked where no contravention is found) could be added
  for the provider.
- Parts 9 to 12 (inquiries, complaint data review, the Commissioner's office, protocols, standards, the Advisory Council):
  machinery. Schedule 1 (interim complaint handling standards) is a standard for providers, applying until standards are
  made under s 133; whether any have been made is not deposited, so it is out.
- ss 148 to 153 (disclosure by the Commissioner and staff), 155 to 159: machinery, or the Commissioner's discretion.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 5(2)(a), 6(2)(a), 7(2)(a) "if it would be unreasonable or inappropriate to resolve the matter by making a
  complaint under subsection (1)" -- `Can I complain to the Commissioner` -- an input stated by the complainant -- a
  judgment for the Commissioner alone.
- **F2** "within 3 months" (s 5(2)(c)), "more than 12 months after" (s 8(1)), "not be more than 12 months after" (s 39(2)),
  "6 months following" (s 31(5)) -- `the date` n `months after` -- the same day of the month n months later, or that
  month's last day where it is shorter (29 February 2028 plus 12 months is 28 February 2029), the last day included -- 1
  March 2029 (rolling over), or the last day excluded.
- **F3** ss 6, 7 -- `a head of ss 5(1), 6(1), 7(1)` -- a carer may complain under s 6 as "a person" as well as under s 7,
  so has the code-of-conduct route of s 6(2)(b), which s 7(2) lacks -- a carer has only s 7.
- **F4** s 15(2) "not reached within 10 business days after" -- `Can the Commissioner decline for want of an agreed
  description` -- open once 10 complete business days have passed -- open only on the 11th.
- **F5** s 61(1) "at least 10 business days before the date on which the hearing is to commence" -- `Was I given enough
  notice of the hearing` -- business days after the day of notice and before the hearing day -- counting one end.
- **F6** s 79(1) "represented by another person", (2) "If the Commissioner so authorises, ... by an Australian legal
  practitioner" -- `May I be represented` -- a lawyer without authorisation or a s 79(3) occasion: JUST FALSE, (2) limiting
  (1) -- JUST TRUE under (1) (finding 7).
- **F7** s 154(2), s 3 "general health service provider" -- the code questions -- Schedule 2 is the general code (no
  prescribed general code was deposited or found named in the text) -- a prescribed code replaces it.
- **F8** Schedule 2 cl 13(3) and cl 16 "should" -- `cl 12, 13 -- contravened`, `cl 14 to 17 -- contravened` -- not kept
  alone: NOTHING (*limited by its own wording*) -- a contravention like the "must"s.
- **F9** s 83(1) "Before publishing ..., the Commissioner must give ... a reasonable opportunity to make ... submissions" --
  `Can my name be published for not responding` -- no opportunity yet: JUST FALSE -- the duty does not limit the s 82 power.
- **F10** ss 91A, 95A "must give a written notice ... must invite" -- the two order questions -- not done: JUST FALSE for an
  order under s 90(1A) or 95(1A) -- a procedural duty that does not bar the order.
- **F11** s 90(1) "for up to 12 weeks", (3) "takes effect on the service" -- `When does the interim order end at the latest`
  -- the day 84 days after the day of service -- 83 days (the day of service counted).
- **F12** s 101(2)(b) reasons requested and not yet given or refused -- `Can I still apply to VCAT` -- JUST TRUE (the later
  day has not come) -- the 28 days from service still run.
- **F13** ss 35(3), 41(3) "must comply" with no "without reasonable excuse", against ss 77, 78 "It is a reasonable excuse
  ... to refuse or fail to ... do any other thing that the person is required to do by or under Part 2, 3, 4 or 5" --
  `what became of it, by dates` -- the excuse counts only for ss 39, 52, 58 -- it counts for ss 35, 41 too (finding 8).
- **F14** s 8(1) "more than 12 months after the provision of the health service was completed" -- `Can I complain to the
  Commissioner` -- counted to the day the person would complain, for every route including (b) and (d) -- route (d) (the
  provider's handling) runs from the handling.
- **F15** s 80(2) "because the other person -- (a) intends to make, makes or has made a complaint" -- `Is it an offence to
  treat me so` -- without the "because": JUST FALSE for s 80 -- NOTHING (other law may apply; s 80 is silent).
- **F16** Schedule 2 cl 5(2)(a) "ensure that appropriate first aid is available to deal with any adverse event" -- `cl 5 --
  contravened` -- a standing duty, breached with or without an event -- engaged only "when an adverse event occurs" (cl 5(1)).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 ("health service", "general health service", "party") answer plain
TRUE/FALSE; the "if" conditions of ss 14, 15(2), 21, 24, 45, 51(3)(b), 82, 87, the "must not ... unless" of ss 40, 91, 96,
the "is not entitled ... more than 12 months" of s 8(1), the "must be no more than" of ss 35(2), 41(2) and "must not be
more than" of s 39(2), the "must not disclose" of s 43(1) and "is not admissible" of s 43(3), and the "must not" of s 102
give `JUST FALSE`. `NOTHING` is answered where a grant does not reach the person (ss 5(1), 6(1), 7(1), 11, 21, 43, 51(3),
61, 76, 77, 78, 80) (*limited by its own wording*), where the Act sets no limit (ss 52, 58) or grants nothing (s 102) or
does not speak (s 43(3) for agreements) (*silent*), and for the two "should" clauses (F8).

## What the Act turns out to say

1. **The 12 months run from the service, whatever the complaint.** s 8(1) bars a complaint to the Commissioner under
   ss 5(2), 6(2) or 7(2) "more than 12 months after the provision of the health service was completed". That includes a
   complaint about how the provider handled the person's complaint (ss 5(2)(d), 6(2)(d), 7(2)(c)), which may happen months
   later. Encoded as written (F14).
2. **"General" is about the service, not the person.** A "general health service" is "a health service that is not a
   health profession service", the practice of a National Law profession. A registered practitioner doing something
   outside their profession (a nurse offering naturopathy) provides a general health service and is bound by the code and
   open to prohibition orders for it. Asserted.
3. **s 14(f) reaches almost any claim.** The Commissioner may refuse or stop dealing with a complaint if "the subject
   matter of the complaint comes within the jurisdiction of a court, tribunal or other body". Read literally, any matter on
   which a negligence claim could be brought qualifies, which would let the Commissioner refuse nearly any complaint about
   harm. Encoded as written, as an input. Asserted.
4. **s 6(1)(e)(ii) was not updated for the duty of candour.** It lets another person complain about how the provider dealt
   with "a complaint ... made by another person under section 5(1)(a), (b), (c) or (d)"; s 5(1)(da) (duty of candour),
   inserted in 2022, is not listed, nor is (e). A family member cannot complain to the provider about how it handled the
   patient's duty-of-candour complaint. Said in the input's description.
5. **Going to the provider first can use up the 12 months.** Route (c) to the Commissioner opens only when the provider has
   not resolved the complaint within 3 months; if the person complained to the provider late in the 12 months, the route
   opens after s 8(1) has closed, and only the Commissioner's s 8(2) discretion remains. Asserted.
6. **Conciliation agreements have no consent exception.** s 43(1) forbids a party to disclose "anything said or done in a
   conciliation or any agreement reached in a conciliation"; the consent exception in (2) covers only "anything said or
   done", so an agreement cannot be disclosed even with everyone's consent (an undertaking can, s 43(4)). And s 43(3)
   makes inadmissible only "anything said or done", not the agreement. Asserted.
7. **s 79(1) and (2).** (1) lets a person be "represented by another person in relation to any process"; (2) lets them be
   represented by a lawyer "If the Commissioner so authorises". A lawyer is another person, so (2) means something only if
   it limits (1) for lawyers. Encoded so (F6). Asserted.
8. **Reasonable excuses with nothing to excuse.** ss 77 and 78 say self-incrimination and privilege are "a reasonable
   excuse" for not doing what Parts 2 to 5 require; the offences of ss 35(3) and 41(3) ("must comply with the requirements
   of the notice") have no "without reasonable excuse", unlike ss 39(3), 52, 58, 68, 70. Encoded with the excuse counting
   only where the offence says so (F13). Asserted.
9. **"General health warning statement".** s 87(3) and (4) speak of a "general health warning statement"; the defined term
   (s 3) is "general health service warning statement". A slip; read as the defined term.
10. **s 94(4) missed by the 2018 amendments.** No. 38/2018 extended interim prohibition orders to a person under a
    Disability Service Safeguards Act 2018 order (s 90(1A)) and changed "general health service provider" to "person" in
    ss 90(2), (3), 94(2)(a), (3)(a), 99 and 100(4), but s 94(4) still says a revocation "takes effect on the service of the
    order on the general health service provider". For a s 90(1A) person who is not a general health service provider, the
    revocation's effect is not tied to service. Not encoded (s 94 is out); recorded.
11. **"the Commission".** ss 90(1A) and 95(1A) speak of a copy "given to the Commission" and a period "specified by the
    Commission"; this Act has a Commissioner, not a Commission. Probably a slip carried from the Disability Service
    Safeguards Act 2018; encoded as the Commissioner.
12. **Two "should"s in a code of "must"s.** Schedule 2 cl 13(3) (a reasonable time before a sexual relationship with a
    former client) and cl 16 (indemnity insurance) say "should". Whether falling short contravenes the code, for ss 45(e),
    87, 91 and 96, is not said (F8). Asserted as NOTHING.
13. **Conversion.** s 7(1)(ab) prints without the indent of its neighbours; ss 27 and 51(2)(c) break mid-sentence; the text is
    otherwise as the Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Health Complaints Regulations (prescribed services, codes and offences), any complaint handling standards made under
  s 133, and the penalty unit value, none deposited.
- A lawyer's view on findings 3, 4, 6, 7, 8 and forks F3, F6, F8, F10, F13 and F14, an independent test pass and a human
  gate.
