# Health Records (Privacy and Access) Act 1997 (ACT) -- baseline encoding, the consumer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The brief asked for the ACT's health complaints and health records law, as an equivalent of the health records Acts named
for other jurisdictions. The ACT has no separate health complaints Act: complaints are made to the Human Rights Commission
under the Human Rights Commission Act 2005, and this Act supplies the grounds (s 18). So this Act is the ACT's health
records law, and it is the first step in most medical negligence and injury claims: getting one's own records, and
controlling the medical reports an insurer or employer wants.

This is the first encoding of the Act; nothing existed to extend. Three files: the dates (`hrpa-dates.l4`, built-in date
functions only, no daydate), the rules and the 32 exported questions (`hrpa-consumer.l4`), and the worked cases
(`hrpa-cases.l4`). Four duties with deadlines are regulative rules (`PARTY ... MUST ... WITHIN ... HENCE ... LEST BREACH
... BECAUSE`), run by EVALTRACE inside exported questions that take only plain facts: the record keeper's answer within 2
weeks (s 13 (2)); access by the 30-day or fee day (s 13B (2), s 13BA (2)); the record to the nominated provider within 2
weeks (s 16B (2)); and the copy or summary to the new provider (principles 12.1, 12.2).

## Edition

- **Act:** Health Records (Privacy and Access) Act 1997 (ACT), A1997-125, Republication No 32 (R32), effective 16 November
  2025, last amended by A2025-29, as deposited at `../../registers/source-bundle/A1997-125.txt` (converted from the
  register's DOCX, which the register marks as an unauthorised version; the authorised text is the register's PDF). The
  date of commencement, 1 February 1998 (s 10 (1) (d)), is from the deposited text's legislation history (endnote 3).
- **Numbers set elsewhere:** the fees the Minister determines under s 34 (not deposited): whether a fee is payable, and
  whether it was paid, are asked. No regulation under s 36 is deposited (s 36 (2) (a) could extend a time by up to 21
  days; none is applied). The penalty unit values ($160 individual, $810 corporation) are those the republication's
  note states at its date (Legislation Act 2001 s 133, not deposited; fork F11). The Legislation Act 2001 (ACT) counting
  rules (s 151, s 151C) are not deposited (fork F2). "Young person" is borrowed from the Children and Young People Act
  2008 s 12 (not deposited) and asked as a status.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 13 answer day put one day late) was run once in a scratch copy in this folder, since
deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hrpa-dates.l4` | 0 | 0 | 0 | 0 |
| `hrpa-consumer.l4` | 0 | 0 | 0 | 0 |
| `hrpa-cases.l4` | 0 | 0 | 197 | 197 |

Every exported question has cases, with the edges: an opinion recorded on 31 January 1998 and on 1 February 1998; each
bar to access on its own, and confidential material from each kind of giver; each person who may ask; writing required
for each kind of requester, and the parent who consented within 12 months; the answer on the 14th day and the 15th; the
access day with no fee, with the fee paid so that 1 week after payment falls before, on, and after the 30th day, and
with the fee unpaid; a s 9 agreement later and earlier than the Act's day; access refused by notice in time and after
time; access after a fee notice paid, late, for an adult (deemed refusal) and for a child or young person (s 13BA, not
listed in s 13D); access with no fee notice on the 30th day (fork F14); the evidence bar with and without a timely
answer; a refusal of only part of the record (s 13 (5)); a consent void under s 26 (2) or s 27 (3), and the signers
those subsections do not reach; an objection to a nominee on the 14th and 15th day and one s 16D (4) forbids; each valid and invalid signer of a
consent; a health status report that is not one (outside the ACT, for the person's own care); destruction on the 7-year
anniversary and the day after, the 25th birthday, and a 29 February birthday and last service; a transfer request on the
14th and 15th day after the notice; a fee notice on the 7th and 8th day; urgent services with and without a fee.

**No mirror cases.** One seat.

## Seat

**The consumer** (`hrpa-consumer.l4`): "an individual who uses, or has used, a health service, or in relation to whom a
health record has been created" (dictionary), and the people the Act lets act for one (a person with parental
responsibility, a guardian, the legal representative or, if none, an immediate family member of a consumer who has
died). Typically the patient getting their records before a medical negligence or injury claim, or the injured person
whose insurer or employer wants a medical report. "Can I see my record?", "By when must I be answered?", "Is the record
keeper taken to have refused me?", "Can they get a report about me without my consent?", "Must my record be sent to my
new doctor, and by when?", "When may my record be destroyed?", "Can I complain?".

The record keeper, the health service provider, the health services commissioner, the Human Rights Commission, the
director-general and the courts get no seat. What they must do is encoded as what the consumer must be given and by when;
what they believe, consider or are satisfied of is asked as a fact. No second seat was written: the record keeper's
duties are all met by the consumer's questions, and a record keeper's seat would be an official's in the public-sector
case.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument is deposited; the s 34 fee is asked.
- **The actors the text names.** Followed: the consumer and those who act for one, the record keeper, the health service
  provider, the collector, the nominated provider, the health services commissioner, the commission, the Magistrates and
  Supreme Courts.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: the record keeper's belief of a
  significant risk (s 15) and of a nominee's unsuitability (s 16D), its satisfaction that a reporter can be identified
  (s 14A (b) (ii)) and with evidence of identity (s 13B (4)); whether arrangements were unreasonable (s 13D (b)-(d));
  sufficient interest (s 31 (2)); the young person's maturity (s 10A).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "health status report", "subject to
  confidentiality" (s 17), "child" (under 12), "consumer" (who acts), "factual matter" (as a choice with its list).
  Asked: "young person", "legally incompetent person" (as a status), "law of the Territory" (glossed: not this Act or the
  common law), "registration board", urgent health services.
- **One case is the text's natural unit.** Followed: one request for access (one part of one record, for s 10), one
  report, one transfer.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (Scope).

## Scope

**In.** s 7 whole; Part 3 (not whole: the parts left out are listed below): s 9, s 10 (1)-(3), (7), (8), s 10A, s 12,
s 13 (with (5), a refusal of part of the record), s 13A, s 13B, s 13BA (2), (6), s 13C, s 13D,
s 14, s 14A, s 15, s 16A, s 16B, s 16D, s 17; s 18; ss 20-23 (maximum penalties only); ss 25-27 (who acts, and the void consents of s 26 (2) and s 27 (3)); ss 31, 32;
schedule 1 principle 4.1 cl 2, 3; principle 6 cl 4; principle 7 cl 3; principle 10 cl 2 (c), cl 7; principle 11 cl 2,
3 (b), 5, 6; principles 12.1 and 12.2 cl 2-4; dictionary terms as listed above.

**Out, and why.**
- ss 1-5, 4A, 4B, 34, 36, 37: machinery. s 6 (lawful authority as a defence to contravening a principle): no question the
  consumer asks; a contravention is asked as a fact for s 18.
- s 8 (a provider may allow access outside Part 3): a permission to the provider, no deadline or fact for the consumer.
- s 10 (4)-(6) (the record keeper's choice of explainer; the commissioner's referral): reflected in s 13C and the s 13D
  answer for a referral; not a separate question.
- s 11 (access as a term of the contract for a health service; void exclusions): it repeats the s 10 right as a
  contractual term and s 11 (8) makes it subject to s 10; the s 10 question answers the same. s 11 (7) (void terms) is
  named here only.
- s 13BA (3)-(5) (a young person's meeting or consent before access): the record keeper's options; no deadline.
- s 16 (the record keeper's offer of a discussion) and s 16C (the nominee's functions): discretions; they appear only as
  the "offer" fact in s 16A.
- s 13D (a) (ii) (a failure to disclose under s 13A is a deemed refusal): not run as a separate rule; s 13A has no
  deadline, so there is no day from which to say it has failed.
- s 24 (representatives in prosecutions), s 29 (good-faith protection for acting on a defective notice or consent), s 30
  (unqualified record keeper), s 33 (court orders under other laws): about the record keeper's or a defendant's
  liability, not the consumer's questions.
- The offence elements of ss 20-23 (and the s 23 (3) defence): only the maximum penalty is encoded; the conduct is a
  choice the consumer states.
- Schedule 1 principles 1, 2, 3, 4.2, 4.3, 5, 6 cl 1-3, 7 cl 1, 2, 4, 8, 9, 10 cl 1-6, 8-12, 11 cl 4, 7-15, 12.1 and
  12.2 cl 5-9: duties of collectors and record keepers with no deadline, or turning on judgments of reasonableness and
  necessity; their breach is a ground of complaint asked as a fact in the s 18 question. Principle 11 cl 7 (a copy to the
  stated provider within 30 days after the request period if the consumer does not ask) is named in the export text of
  the principle 11 request question.
- The Human Rights Commission Act 2005 (how and when a complaint is made): another instrument.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 10 (1) (d) "if the record was created on or after the date of commencement" -- `s 10 -- may I see this part of
  my health record` -- read per part of the record (the dictionary's "record" includes any part), by the day the part was
  created -- read per whole record, so an opinion added after 1998 to a record begun earlier would be outside.
- **F2** "within 2 weeks after the day", "not later than 30 days after the day", "1 week after" (ss 13, 13B, 13BA, 16B,
  principles 11, 12) -- every date question -- the day itself excluded, last day = day + n; not moved off a weekend or
  public holiday -- Legislation Act 2001 s 151C moving the last day to the next working day (not deposited).
- **F3** principle 4.1 cl 3 (b) "the day the consumer turns 25", "7 years after the day" -- `principle 4.1 -- the first
  day my record may be destroyed for age or time` -- a 29 February anniversary in a common year is 1 March -- 28 February.
- **F4** s 10 (1) (b) "to the extent that it contains personal health information relating to the consumer, any other
  health record" -- the s 10 question -- outside it, NOTHING-kind (a grant limited in its own wording) -- JUST FALSE.
- **F5** s 12 (2) "A request must" (a bare "must" not done, decided case by case) -- `s 12 -- is my request properly made`
  -- a request missing a requirement does not start the s 13 clock -- the clock runs and the record keeper must still
  answer.
- **F6** s 13B (4), s 13BA (6) "need not provide access" -- `s 13D -- is access taken to have been refused` -- not a
  refusal; it relieves the giving of access only, so it is checked after the s 13 (2) answer day (a record keeper that
  gave no answer at all in 2 weeks is taken to have refused) and before the access day -- a failure to answer or to give
  access in time that is still a deemed refusal; or, the other way, the evidence bar also excusing the answer where the
  only answer open was access itself (no fee determined, no ground to refuse).
- **F7** principle 10 cl 7 (a) (i) "a child or young person who does not have sufficient maturity" -- `principle 10 cl 7
  -- is my consent to disclosure valid` -- every child under 12 consents through the person with parental
  responsibility -- a mature child under 12 signs personally.
- **F8** principle 10 cl 7 and s 7 (4), a deceased consumer with no legal representative -- both consent questions --
  the immediate family member signs, under (a) (iii) "in any other case, by the consumer" and the dictionary's
  "consumer" (d), as for access (s 13B (3) (c) (ii) (B)) -- no valid signer, s 27 (2) giving the dead consumer's powers
  to the legal representative only.
- **F9** s 16B (3) (a) "a notice under section 16D" -- `s 16B -- must my nominee get the record` -- an objection s 16D (4)
  forbids, or one given after the 2 weeks, is not such a notice, so the duty stands -- any objection notice excuses.
- **F10** principles 12.1 and 12.2 cl 2 (a) "not later than 7 days after" -- `principle 12 -- by when must my record reach
  my new provider` -- a fee notice after the 7 days does not displace cl 2 (b)'s 30 days -- a late fee notice still
  defers the duty until payment.
- **F11** ss 20-23, the value of a penalty unit -- `ss 20-23 -- the most they can be fined` -- $160 and $810, from the
  republication's note -- the current Legislation Act s 133 values, which may change after 16 November 2025.
- **F12** s 13D, an answer that is itself late -- `s 13D -- is access taken to have been refused` -- the late answer is
  reported first (taken to be refused under s 13), even if it is a refusal notice -- the refusal notice reported first.
- **F13** principle 4.1 cl 3 (b) (i), (ii), "when the information is collected" -- the principle 4.1 questions -- one age
  at collection per record, as the consumer states it -- each piece of information tested apart (a record with
  information from both before and after 18 would have two days).
- **F14** s 13 (2) (d) (i) against s 13B (2) (b) / s 13BA (2) (b) -- `s 13D -- is access taken to have been refused`,
  `ss 13B, 13BA -- by when must I be given access` -- read as written: where no fee notice is given, access itself is
  the answer due within 2 weeks, so a record keeper that gives no access (and no notice) by then is taken to have
  refused (s 13D (a) (i)), and the 30 days of s 13B (2) (b) never extend it; a promise of access without a fee is not an
  answer s 13 (2) lists -- s 13B (2) (b) as the specific rule: access with no fee notice may be given up to the 30th day,
  reading s 13 (2) (d) (i) as access "in accordance with" s 13B, with no deemed refusal until day 31 (finding 12).
- **F15** s 13D (a), which lists ss 13, 13A, 13B and 13C but not s 13BA -- `s 13D -- is access taken to have been
  refused` -- late access to a child or young person under s 13BA (2) is a breach the text does not deem a refusal
  (NOTHING-kind) -- s 13BA read in as the children's twin of s 13B, so late access is a deemed refusal (finding 11).

Sites decided without a fork line: the "means" definitions (health status report, child, legal representative) and the
"if" conditions of s 7 (3), s 13A (1), s 16A (1), s 17 (2), (3), principle 7 cl 3 answer the text's no when they fail;
the flat negatives of s 7 (1), (2), s 14A, s 15, s 17 (1), s 16D (4), s 32 (3), principle 4.1 cl 2 and principle 6 cl 4
answer the text's no; the s 18 and s 31 grants answer NOTHING outside them.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` answers at F4, s 18, s 31 and s 32 (outside s 31), and the ss 20-23 question for
conduct outside the offences. Most questions answer with a choice from a list rather than a MAYBE BOOLEAN: the answer
marked "NOTHING-kind" is the NOTHING answer, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (14 days in principle 11 cl 3 (b)) answer the text's no outside the period (ruling (a)).

## What the Act turns out to say

1. **s 25 and s 10A disagree about a mature young person.** s 25 (b) says a child's or young person's rights are "not
   exercisable by the consumer on the consumer's own behalf"; s 10A (b) (i) gives a young person of sufficient maturity
   the right of access "personally". s 25 opens "Subject to this Act", so s 10A is read as prevailing for access.
   Asserted.
2. **s 12 (2) (d) does not require a written request from an immediate family member of a deceased consumer**, though it
   does from the legal representative, and the dictionary makes the family member the "consumer" where there is no legal
   representative (s 13B (3) (c) (ii) (B) expects such requests). Probably an oversight when the family member was added.
   Asserted.
3. **The two consent rules treat young people differently.** s 7 (4) has every child or young person consent through the
   person with parental responsibility; principle 10 cl 7 lets a young person of sufficient maturity sign personally.
   A mature 16-year-old can therefore authorise disclosure of their record to a lawyer (s 13A) but not a health status
   report for an insurer. Asserted.
4. **s 7 (4) (b) says "health service report"**, a term the Act does not define; the defined term is "health status
   report". A likely drafting slip; encoded as "health status report" (and by the definition such a report is always
   prepared by a health service provider, so the consent must always name one).
5. **Principle 12.2 cl 9 defines "health record" by reference to "the first provider"**, a term used in 12.1 but not in
   12.2, which speaks of "the first practice". Copied from 12.1; encoded as the first practice's record.
6. **s 32 (3) excludes appeals about "an interim restraining order under section 31"**, but s 31 never mentions interim
   restraining orders (only "any other order ... the court considers appropriate"). Encoded as asked.
7. **Fees can stop the clock indefinitely.** Under s 13B (2) (a) and principles 11 cl 5 and 12 cl 3, no last day runs
   until a stated fee is paid; the Act sets no time for payment. Asserted (the unpaid-fee cases).
8. **A request properly made but answered late cannot be cured by a later refusal notice**: the s 13 duty is breached on
   the 15th day and access is taken to be refused (fork F12). Asserted.
9. **Principle 4.1 cl 3 (b) turns on the consumer's age when "the information is collected"**, but destruction is of the
   record; a record holding information from both childhood and adulthood has two different days (fork F13).
10. **Neither s 18 nor s 31 sets a time limit**; the Human Rights Commission Act 2005 governs complaints.
11. **s 13D (a) does not list s 13BA.** Late access to a child or young person (or the parent acting for one) breaches
    s 13BA (2), which sets the same days as s 13B (2), but s 13D (a) deems a refusal only for ss 13, 13A, 13B and 13C.
    Probably an oversight when s 13BA was split from s 13B. Encoded as NOTHING-kind (fork F15). Asserted.
12. **s 13 (2) (d) (i) and s 13B (2) (b) conflict.** Unless a fee notice is given, s 13 (2) (d) (i) requires access
    within 2 weeks; s 13B (2) (b) allows 30 days where no fee notice was given. s 13 (2) (d) (i) also says access "in
    accordance with section 13A", which is now the disclosure-by-consent section; s 13B (giving access) was probably
    meant, a cross-reference left behind by renumbering. Read as written (fork F14). Asserted.
13. **s 16A (3) (a) lapses a nomination when the record keeper gives "a notice under section 16B"**, but s 16B provides
    for no notice; s 16D (the objection notice) was probably meant. Since the lapse is asked as a fact, the answer quotes
    the text's words and flags the slip.
14. **s 26 (2) and s 27 (3) void a guardian's or a legal representative's consent given against the person's earlier
    wishes, but not a consent by an immediate family member** of a deceased consumer with no legal representative, who
    is "the consumer" under the dictionary's (d), nor by a person with parental responsibility. Asserted.

## Before this is worth relying on

- The s 34 fee determination, and the Legislation Act 2001 (ACT) for counting time (fork F2) and penalty units (F11), not
  deposited.
- The Children and Young People Act 2008 s 12 ("young person") and the Human Rights Commission Act 2005 (how and when to
  complain).
- A lawyer's view on forks F1, F6, F8, F9, F12, F13, F14 and F15, and on findings 1-6 and 11-14; an independent test pass and a human gate.
