# Human Rights Act 2019 (Queensland) -- baseline encoding, the individual affected by a public entity

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The dates are in `hrq-dates.l4` (built-in
date functions only, no daydate), the rules in `hrq-core.l4`, the individual's exported questions in `hrq-seat.l4`
(each calls a rule in `hrq-core.l4`), and the worked cases in `hrq-cases.l4`. The layout follows the Victorian Charter's
baseline (`subjects/au/vic/charter-of-human-rights-and-responsibilities-act-2006/encodings/baseline-2026-11/`), which
this Act closely resembles; nothing is imported from it (IMPORT does not reach another subject's folder).

Focus: the provisions a claimant meets. For a person injured, held or harmed by a Queensland public entity, the Act
does three things: it makes it unlawful for a public entity to act incompatibly with human rights or to decide without
proper consideration of them (s 58); it lets that unlawfulness ride as a further ground on relief the person can seek
apart from the Act, with no damages of its own (s 59); and it gives a complaint to the Queensland Human Rights
Commissioner, after a complaint to the entity and a 45-business-day wait, ideally within a year (Part 4, Division 2).
It also requires every Queensland statute in the person's case to be read compatibly with human rights so far as
possible (s 48), and puts on a party the duty to notify the Attorney-General and the commission (s 52).

## Edition

- **Act:** Human Rights Act 2019 (Qld), Act No. 5 of 2019, the version in force from 2023-09-20, current on
  2026-11-06, deposited at `../../registers/source-bundle/act-2019-005.txt` (text sha256 5f7bf859...dc09c per its
  `.meta.json`), a plain-text conversion of the Queensland Legislation HTML "whole" view. Not the authorised (PDF)
  version, and not checked against it.
- **Numbers and dates set elsewhere:** the commencement (s 2, "a day to be fixed by proclamation"; the proclamation is
  not deposited), so every question that turns on it asks whether the act, decision or proceeding was before it.
  The value of a penalty unit (Penalties and Sentences Act 1992, not deposited): s 100's penalty is given in units.
- **Not deposited, and asked as facts:** the regulations under s 9(1)(j), (4)(c) (prescribed entities) and s 97; the
  approved forms (s 104); the Acts Interpretation Act 1954 ("business day", "Act", "child", counting periods); the
  Statutory Instruments Act 1992; the Public Sector Act 2022 s 276 ("government entity"); the Local Government Act 2009
  and the City of Brisbane Act 2010 (councillors and employees); the Guardianship and Administration Act 2000
  ("impaired capacity"); the Information Privacy Act 2009 ("personal information"); the meaning of "discrimination" in
  the Anti-Discrimination Act 1991 (deposited beside this subject with its own baseline, not importable); the other law
  that gives the person a claim.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed
`assertion failed` as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hrq-dates.l4` | 0 | 0 | 0 | 0 |
| `hrq-core.l4` | 0 | 0 | 0 | 0 |
| `hrq-seat.l4` | 0 | 0 | 0 | 0 |
| `hrq-cases.l4` | 0 | 0 | 256 | 256 |

Every exported question has cases, with the edges: every kind of entity in s 9 with and without the fact its head
needs, each exclusion beating an inclusion (a regulation excluding a department and a s 60 entity), a court deciding a
case and acting administratively; the s 10(3) listed functions against a finding; each limb of ss 16, 17, 25, 26(2), 29,
30, 31, 33 and 37 alone, together and not met, including a person not arrested with every other fact set against them,
and a child detained without charge (s 33(1) but never s 33(2), which reaches only an accused child);
each s 58 exclusion beating an unjustified limit, and (a), (b) and both; the 45th business day itself and the next day,
with and without public holidays; the 1-year last day and the day after, from 29 February; the both-periods window
closing on its last day (a complaint to the entity on 7 April 2026 for a contravention of 10 June 2025) and one day
over (8 April); an override provision the day before it commenced, on its 5th anniversary and the day after, an
earlier expiry day and the day before it, and from 29 February 2024; each s 52 combination of court, referral and
parties, and each combination of notices given; a s 78 direction complied with on the day of the notice, on the last
day and the day after, and not at all; an anonymity direction kept and broken.

## Seat

**The individual** (`hrq-seat.l4`): an individual affected by an act or decision (including a failure to act) of a
Queensland public entity -- a prisoner (including in a privately run prison), a person held by police, a child in
State care or youth detention, a patient in a public hospital, a tenant of a funded housing provider, a person hurt by a
council or a State agency -- who may complain to the Queensland Human Rights Commissioner and may have a claim of their
own apart from the Act (judicial review, false imprisonment, battery, negligence, a compensation statute). "Do I have
human rights?", "Is the body a public entity?", "Which of my rights did what happened limit?", "Was the act unlawful?",
"Can I add a human rights ground to my claim, and get damages?", "Must the court read the statute compatibly with my
rights?", "Must I notify the Attorney-General and the commission?", "Can I complain to the commissioner, from when and by
when?", "What happens to my complaint?".

The Act puts its duties on public entities (s 58), Parliament, the courts, Ministers and the commissioner; officials get
no seat. A public entity's own seat is not written: the same s 58 answers tell it whether an act would be unlawful, and
a second seat would add only mirror cases. The duties the Act puts on the individual -- notice as a party (s 52),
complying with a direction to give information (s 78(5)), not disclosing contrary to an anonymity direction (s 100(2)),
attending conciliation in person (s 82) -- are encoded from the individual's seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: no deposited instrument sets a number the
  encoding uses; the commencement proclamation and the regulations are not deposited and are asked.
- **The actors the text names.** Followed: the individual (complainant), the public entity (respondent), the
  commissioner and the commission, the court or tribunal, the Supreme Court, the Attorney-General, the State, the
  referral entities and the NDIS commissioner.
- **Judgments answered conditionally.** Each judgment is asked as "whether a court would find" or "whether the
  commissioner considers": functions of a public nature outside s 10(3), performing them for the State, administrative
  capacity, cruel, inhuman or degrading, unlawful or arbitrary, promptly and without unreasonable delay, reasonably
  necessary, humanity and dignity, fair hearing, reasonable and demonstrably justifiable (s 13), private nature, could
  not reasonably have acted differently, proper consideration, exceptional circumstances (s 65(2)), more appropriately
  dealt with (s 73(6)), the individual can not complain (s 64(2)), reasonable excuse. None is decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: public entity (s 9 with s 10(3)), compatible
  with human rights (s 8), who has human rights (s 11), human rights complaint (s 63), statutory provision (schedule 1),
  address for service (s 102). Asked: government entity, councillor, registered provider, child, impaired capacity,
  discrimination, personal information, business day's public holidays.
- **One case.** One act, failure or decision of one public entity, as it affected one individual; for ss 48, 49 and
  52, one proceeding; for Part 4, one complaint.
- **The Act's terms with plain glosses.** Followed, in every `@desc`.
- **Operative sections in; machinery out.** See Scope.

## Scope

**In:** s 8; s 9 (every head, inclusion and exclusion) with s 10(3) (the listed public functions; s 10(1), (2) as a
finding); s 11; s 7 and Part 2 (every right in ss 15-37 named; ss 16, 17, 25, 26(2), 29, 30, 31(1)-(3), 33 and 37 limb by
limb); s 13 (as the finding s 8(b) needs); s 45(1), (2) and s 46 (effect and life of an override declaration, for
s 48); s 48 (with (4), (5)); s 49 (referral); s 52 (notice: a regulative rule); s 54(b) (in the s 48 answer); s 58
(with (2)-(6)); s 59; s 60(3) via s 9(3); ss 63-65, 66(2)(b), 67, 69-73, 75, 76, 78, 82-84, 86-90, 99, 100, 102;
s 108(2) (proceedings, and acts and decisions, before the commencement).

**Regulative rules:** three, each run by EVALTRACE inside an exported question that takes only plain facts.
- s 52(1): I MUST give notice in the approved form to the Attorney-General RAND to the commission (or to the one s 52(2)
  leaves). No WITHIN (the Act sets no time) and no LEST (the Act says nothing of what follows a failure).
- s 78(5): I MUST give the commissioner the information directed WITHIN the days from the notice to the last day stated,
  LEST BREACH (enforceable as a court order once filed, s 78(7), (8); the commissioner may refuse to continue,
  s 70(2)(a)). The last day stated counts as in time (asserted).
- s 100(2): I SHANT disclose information identifying a protected person, LEST BREACH (an offence, maximum 35 penalty
  units for an individual). Built only where a direction covers the information and I have no reasonable excuse.

**Out, and why:**
- The other Part 2 rights limb by limb (ss 15, 18-24, 26(1), 26(3), 27, 28, 32, 34-36): further from injury and custody
  claims (s 26(1) protects families as a unit, s 26(3) gives a right to a name and birth registration); each is
  named in `Human right` (s 26 as a whole) and reaches s 58 through the "limits a human right" finding. Encoding them limb by limb is the
  next step if a scenario needs it.
- Part 3, Division 1 (ss 38-42, scrutiny of Bills and subordinate legislation), ss 43, 44, 47 (how Parliament makes an
  override), ss 50, 51 (the Attorney-General's and the commission's power to intervene), s 53 (the Supreme Court's
  declaration procedure; its effect, s 54(b), is in), ss 55-57 (the Minister's and committee's response), s 60(1), (2)
  (the entity's own request): duties and powers of Parliament, courts, the Minister and the commission that change
  nothing the person can claim.
- Part 4, Division 1 (ss 61, 62, functions and powers), s 66(1), (2)(a), s 68, s 74, s 77, ss 79, 80, s 85 (how the
  commissioner and the referral entities work; ss 66(2)(b), 73, 75 and 76 are in for what they mean to the person),
  Division 3 and Part 5 reporting (ss 91-98), s 101, s 103 (deemed address), ss 104, 105: machinery.
- s 81 (the commissioner may direct a person, the complainant included, to take part in a conciliation conference,
  enforceable as a court order once filed): a power of the commissioner, not a duty the Act itself puts on the person.
  The person's duty comes from a direction once given, and the Act sets no content, time or consequence for it beyond
  filing and enforcement as a court order (s 81(2), (3)), which is the court's own law (not deposited). Unlike s 78(5),
  which the Act states as "must comply", there is nothing to write as a regulative rule; it would be the next step if a
  scenario reaches a direction.
- ss 1-6, 12, 14, 106, 107, s 108(1), (3): no rule a person applies (s 12 is reflected in the s 59 answers' sense that
  other rights and remedies stay).
- The other law that gives the claim (negligence, false imprisonment, judicial review; the Civil Liability Act 2003,
  the Limitation of Actions Act 1974 and the Anti-Discrimination Act 1991 have their own baselines beside this subject):
  asked as a fact.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 65(1)(b) "business days" -- `is a business day`, `the business day after` -- a weekday that is not a public
  holiday, the holidays supplied as a list -- the Acts Interpretation Act 1954 (not deposited) may also exclude special
  holidays, bank holidays or the days between Christmas and New Year.
- **F2** s 70(1)(d) "within 1 year after the alleged contravention ... happened" -- `s 70(1)(d) -- the last day`,
  `the anniversary` -- the year runs from the day after and ends at the end of the anniversary; for 29 February, 28
  February -- the year ends the day before the anniversary; or the anniversary of 29 February is 1 March.
- **F3** s 11(1) "All individuals in Queensland have human rights" -- `s 11 -- has human rights` -- for an individual
  outside Queensland, not answered (NOTHING kind) -- read as closed ("only individuals in Queensland"), which would
  answer no.
- **F4** s 9(1)(a), (b), (d), (2)(a) borrowed terms -- `Kind of entity` -- the person picks the kind -- the borrowed
  definitions (not deposited) may include or exclude bodies the person would not expect.
- **F5** s 9(4)(a), (b) "except when acting in an administrative capacity" -- `s 9 -- public entity` -- the exception
  lifts the exclusion only; the court, tribunal or Assembly then needs a head, taken as (f) (an entity established under
  an Act performing functions of a public nature), so a court acting administratively but not in a public function is
  "not shown" -- the exception makes it a public entity by itself.
- **F6** s 16 -- `s 16 -- limbs limited` -- the first limb (the right to life) is limited where a court would so find
  (asked); the second needs a death -- the first read as narrowly as the second.
- **F7** s 29(4), (5), (7) -- `s 29 -- limbs limited` -- each limb only for a person arrested or detained; (5) only on a
  criminal charge; (7) only where the person applied; (5)(c) "not complied with" taken to reach (b) (a right) as well as
  (a) (a duty) -- (5)(c) reaching only (a).
- **F8** s 30(1) "deprived of liberty" -- `s 30 -- limbs limited` -- reaches care and treatment settings as well as
  custody (asked) -- custody only.
- **F9** s 8 "compatible with human rights if" -- `s 8 -- compatible with human rights` -- the two limbs read as the whole
  test, so an unjustified limit is "not compatible" -- an "if" that does not close, leaving other ways to be compatible.
- **F10** s 58(2)-(4), s 108(2)(b), s 9 -- `s 58 -- unlawful` -- the first reason found, in the order s 9, s 108(2)(b),
  s 58(4), (3), (2), is the one given -- the reasons are cumulative (the "not unlawful" answer is the same; only the
  reason shown differs).
- **F11** s 59(1) "on the ground that the act or decision was, other than because of section 58, unlawful" --
  `s 59 -- a human rights ground` -- whether the person's other claim is such a ground is asked -- a claim in negligence
  (breach of a duty of care) may not be a claim that the act was "unlawful", and then s 59 adds nothing to it.
- **F12** s 45(2) "expires 5 years after the day on which the provision commences or on an earlier day stated" --
  `s 45(2) -- the last day of an override provision`, `s 45 -- an override declaration is in force` -- in force to the
  end of the 5th anniversary of commencement; expired on an earlier stated day itself -- expired on the anniversary
  itself (as the Victorian Charter's "expires on the 5th anniversary"); or in force on the earlier stated day.
- **F13** schedule 1 "statutory provision means an Act or statutory instrument" -- `a statutory provision` -- a Queensland
  Act and an instrument made under one -- "Act" read more widely (the Acts Interpretation Act 1954 is not deposited).
- **F14** s 52 -- `s 52(1) -- my duty to notify` -- no WITHIN and no LEST -- court rules or practice directions (not
  deposited) may fix a time.
- **F15** s 65(1)(b) "at least 45 business days have elapsed since the complaint ... was made" --
  `s 65(1)(b) -- the earliest day` -- counted from the day after; the earliest day is the calendar day after the 45th
  business day -- the 45th business day itself.
- **F16** s 67(1) a bare "must" not met -- `ss 67, 102 -- form of complaint` -- "no", with the requirement (Meng's
  case-by-case rule) -- the commissioner may treat a defective complaint as made and ask for more (s 77(2)(c)).
- **F17** s 72(2) "a human rights complaint the commissioner refuses to deal with under section 70(1)(c)" --
  `ss 71, 72 -- after refusal` -- covers a refusal to deal and to continue to deal under s 70(1)(c) -- only a refusal
  "to deal", so a refusal to continue under (c) bars a further complaint.
- **F18** s 78(3) "The notice must state the purpose for making the request" -- `s 78 -- must I give the information` --
  a notice without its purpose imposes no duty -- the defect does not excuse compliance.
- **F19** s 82(1) "must attend ... in person unless" -- `s 82 -- must I attend in person` -- once an "unless" is met, no
  duty to attend in person (Meng's case-by-case rule) -- the "unless" only lifts "in person", leaving a duty to take part
  by another means.
- **F20** s 90(1) "may publish information about a human rights complaint that the commission has finished dealing
  with" -- `s 90 -- publication` -- before then, not answered (NOTHING kind: a grant limited in its own wording, with no
  "only") -- read as closed, so the commissioner may not publish before the commission has finished.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 11(2) and s 59(5) say "only"; s 63 is a "means"-like definition; s 9(4), s 54, s 58(2)-(4), s 59(3),
s 72(1)(b), s 86, s 88(6) and s 108(2) are flat negatives; s 8, s 49(1), (2), s 52(1), s 59(1), s 65(1) ("only if"),
s 73(6) ("only"), s 83(1) ("only"), s 99(1) and s 100(2) ("unless") are conditions: each gives a "no" constructor with
its section. s 9(1)-(3) and s 64(1) do not close their lists: a body or person in none of them is "not shown"
(NOTHING kind, as an explicit constructor), as are an individual outside Queensland (s 11(1)), the s 88 report in a
proceeding other than one about a contravention of the Act (s 88(6)), and publication about a complaint still open
(s 90(1)). s 58(1) says only what is unlawful: where its
limbs are not met the answer is worded "s 58(1) not met on these facts", never "lawful". The Part 2 questions list the
limbs the facts meet; an empty list means no limb on these facts. s 70(1)(d) is a discretion ("may refuse"): outside the
year the answer is the discretion, not a bar. Meng's case-by-case sites: F16, F18, F19.

## What the Act turns out to say

1. **No claim and no damages of its own.** s 59(1), (5): a s 58 ground rides only on relief the person can seek apart
   from the Act; s 59(3): no damages "on the ground of unlawfulness arising under section 58"; s 59(6): damages
   otherwise available are kept. So for an injury claim the Act never adds money. Asserted.
2. **Whether a negligence claim is a ground "that the act or decision was ... unlawful" is not in the text** (F11). It
   is the most important open question for this seat.
3. **The commencement day is not in the Act.** s 2 leaves it to proclamation (not deposited), and s 108(2) makes it the
   line for acts, decisions and proceedings. Every such question asks the person whether it was before; a deposit of
   the proclamation would let it be computed.
4. **s 33(1) has no "reasonably necessary" exception; s 30(2) has one; and s 33(1) does not reach a convicted child.**
   A detained accused or uncharged child must be segregated from all detained adults, with no exception in the text;
   a convicted child held with adults is protected only by s 33(3) and s 30(1). Asserted.
5. **The commissioner's report is inadmissible only in a proceeding about a contravention of this Act.** s 86 makes
   anything said or done in conciliation inadmissible in "any criminal, civil or administrative proceeding"; s 88(6)
   covers the report only "in a proceeding in relation to a contravention of this Act". Whether the report can be used
   in, say, a negligence claim is left open by the text. Asserted ("not answered").
6. **The 45-business-day wait and the 1-year limit run from different days and can collide.** The year runs from the
   contravention (s 70(1)(d)); the wait from the complaint to the entity (s 65(1)(b)). A person who complains to the
   entity in roughly the last nine weeks of the year cannot complain to the commissioner in time without the
   commissioner either accepting early for exceptional circumstances (s 65(2)) or declining to refuse as late. Asserted:
   for a contravention on 10 June 2025, a complaint to the entity on 7 April 2026 leaves the window open on its last
   day, 8 April closes it.
7. **s 72(2) speaks of a refusal "to deal with" under s 70(1)(c), but s 70(1) covers refusing "to deal or to continue to
   deal"** (F17).
8. **s 9(4)(a), (b) exclude courts and the Assembly "except when acting in an administrative capacity", but no head of
   s 9(1) names them.** A court acting administratively becomes a public entity only through another head (F5).
9. **s 45(2) expires the provision containing the declaration, not only the declaration**, and counts from the
   provision's commencement. Where an Act declares an override for a provision of another Act, the overridden provision
   does not expire; the encoding treats the declaration as no longer in force once the containing provision expires
   (F12).
10. **s 29(5)(c) speaks of "complied with" for a right.** (a) is a duty, (b) a right; (c) requires release if "(a) or
    (b) is not complied with". Taken to reach (b) (F7).
11. **The complainant is the individual, not the person who makes the complaint.** Schedule 1: "complainant ... means the
    individual who is the subject of the complaint", while s 64(1)(b), (c) let an agent or an authorised person make it.
    So s 82's duty to attend in person falls on the individual even where an agent complained, and s 65's "the person
    has made a complaint to the public entity" leaves open whether an agent must itself have complained to the entity.
12. **s 70(1)(d) counts from when the contravention "happened".** For a continuing act or failure (an ongoing detention or
    a continuing refusal of treatment) the day is not fixed by the text; the encoding takes the day the person gives.
13. **"Child" is not defined in this Act** (ss 26, 33, 82); it is asked.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit the commencement proclamation, the Human Rights Regulation (if any prescribes entities), the Acts
  Interpretation Act 1954 and the Public Sector Act 2022, and work F1, F4, F13 and finding 3 out from them.
- A lawyer's view on findings 2, 5, 7, 9, 10 and 11 and forks F2, F5, F9, F11, F12 and F17 (several turn on case law
  that is not deposited), an independent test pass and a human gate.
- Encode the remaining Part 2 rights limb by limb if a scenario life needs them.
