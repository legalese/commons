# Public Interest Disclosures Act 2022 (NSW) -- baseline encoding, the public official who makes a disclosure

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 30 October 2023). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the agency's progress
updates every three months, s 59(3); the discloser's 28 days to apply for internal review, s 60(2)(a)), each run by
`EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except
in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a person bringing or
answering a claim meets: whether a disclosure is protected (Part 2), the protections and the claims for damages,
injunctions and costs (Part 3), and the discloser's rights while the disclosure is dealt with (Part 5).

## Edition

- **Act:** Public Interest Disclosures Act 2022 No 14, corpus document `nsw_legislation:2023-10-30/act-2022-014` (in
  force 30 October 2023), deposited at `../../registers/source-bundle/act-2022-014.txt` (text sha256 05414c3d...e0dcbb
  as recorded in the meta file), taken from the Open Australian Legal Corpus (collected 10 March 2025) because
  legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Not deposited:** the Public Interest Disclosures Regulation 2022 (which may declare persons to be or not to be public
  officials, agencies and integrity agencies, ss 14(2), 16(3), 19(j)); the Independent Commission Against Corruption Act
  1988 ("corrupt conduct"); the Crimes (Sentencing Procedure) Act 1999 (the value of a penalty unit); the Interpretation
  Act 1987 (counting periods); the Limitation Act 1969. What they decide is asked as a fact or left out.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was checked to fail).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pid-dates.l4` | 0 | 0 | 0 | 0 |
| `pid-disclosures.l4` | 0 | 0 | 0 | 0 |
| `pid-protections.l4` | 0 | 0 | 0 | 0 |
| `pid-dealing.l4` | 0 | 0 | 0 | 0 |
| `pid-cases.l4` | 0 | 0 | 207 | 207 |

Every expected value was worked by hand from the text, with the edges: the last day of the s 28 investigation period
and the day after (6 and 12 months, a 31 August start ending in February, a leap February); the last day of three
months for a progress update and the day after; the 28th day for internal review and the 29th, across a year end;
three years for a prosecution from 29 February; each s 14 category and each regulation declaration; each kind of serious
wrongdoing, trivial and not; each recipient, an oral disclosure to a Minister, a member of Parliament as maker; each
limb of s 26(2)-(4); each s 28 condition failing alone; mandatory, witness, wilfully false and determined disclosures in
combination; each detriment and each s 32(3) exclusion; each limb of s 31(4); each bar on s 35 damages; each limb of
ss 37, 38, 40, 41, 49, 59(5), 61, 62, 64 and 65.

## Seat

**The discloser**: the public official who makes, or is thinking of making, a disclosure about serious wrongdoing, and
who (or someone close to whom) may suffer detrimental action because of it. A witness, who need not be a public official
(s 22), and anyone else who suffers detrimental action (s 35 "the other person or a third person", s 37(1)(d), s 62(1)
"a person") ask the same questions. Every exported question is one that person would ask ("Am I a public official?",
"Is what I am reporting serious wrongdoing?", "What kind of public interest disclosure did I make?", "From what day may I
go to a journalist?", "Was what was done to me detrimental action?", "Is the person liable to me in damages?", "Can I get
an injunction?", "Can I be made to pay costs?", "Am I protected from liability?", "Must the agency deal with my
disclosure?", "Is my update overdue?", "Can I apply for internal review, and by when?", "Can I recover from the agency?",
"Can my identity be revealed?", "Must I help the investigation?"). The person who took detrimental action meets ss 33,
35 and 37 from the other side; a seat for them could be added. Agencies, integrity agencies, the Ombudsman, the
Attorney General, Ministers and courts get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets its own numbers (6 and 12
  months, 3 months, 28 days, 3 years, 200 and 100 penalty units); the Regulation is not deposited, and its declarations
  are asked as facts (s 14(2)).
- **The actors the text names.** Followed: the maker, the agency, the head of the agency, disclosure officers, the
  manager, Ministers, members of Parliament, journalists, the person taking detrimental action, the employer, the
  Attorney General, the Supreme Court, the reviewer.
- **Judgments answered conditionally.** Followed: honest belief on reasonable grounds (s 26(1)), significant
  implications (s 26(3)), reasonableness of management action (s 31), triviality (Dictionary), "substantially true"
  (s 28), what the defendant has proved (ss 35(4), 62(3)), what the other party has shown on costs (s 38(2)), the
  public interest (s 64(2)(i)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "public official", "serious wrongdoing",
  "detriment", "detrimental action", "reasonable management action", the investigation period and the three kinds of
  public interest disclosure are worked out; "corrupt conduct" (ICAC Act), "journalist" (Evidence Act), "anonymous" as
  a fact, are asked. **Departure:** the questions in Parts 3 and 5 take the kind of disclosure (the answer of "What kind
  of public interest disclosure did I make") as an input, rather than asking its 25 facts again; the form should ask
  that question first.
- **One case.** One disclosure (and, for Part 3, one detrimental action).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 13, 14, 20 (Part 1 key terms, as they decide the answers); Part 2 whole (ss 21-29); Part 3 whole (ss 30-41;
s 34, agency referrals, as a comment only); Part 5 ss 49, 50 (as a fact), 55(3) (as a fact), 59, 60, 61, 62, 64, 65,
66 (as the s 35(5) and s 37(6) defence); s 7(2)(b) (no protection for failing a duty to disclose).

**Out, and why:** ss 1-6, 8-12 (name, commencement, objects, Crown, legal personality, relationship with other Acts):
machinery, or a fact under them changes no answer here. ss 15-19 (manager, agency, head, disclosure officer, integrity
agency): asked as facts through the recipient and position lists. Part 4 (agency policies): duties on agencies with no
fact the discloser states (s 18(2), the fallback disclosure officer where a policy is missing, is folded into "another
disclosure officer"). ss 51-58 (how agencies pass on, refer and investigate): agency machinery. s 63 (regulations).
Part 6 (Steering Committee, Ombudsman), Part 7 ss 79-83, 86-90 (application, delegation, contracts, information sharing,
proceedings, review, repeals): machinery. ss 84-85 (offences of false statements and of influencing or impeding):
mentioned in comments; the maximum penalties (100 penalty units, and 2 years for s 84) are not computed. Schedule 1
(savings and transitional: disclosures made before the 1994 Act was repealed stay under it; remade disclosures):
every case here assumes a disclosure made under this Act. The value of a penalty unit, the limitation period for the
damages claims and the meaning of "corrupt conduct" are in other Acts.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 28(2), 33(6), 59(3), 60(2)(a) -- `the day plus months`, `From what day may I go to a member of Parliament or
  a journalist`, `By what day must a prosecution be started`, `By what day must I get my next progress update`, `By
  what day must I apply for internal review` -- a period of months "from" or "after" a day leaves that day out and ends
  on the same day of the month later (or the last day of a shorter month); 28 days "after the day" ends 28 days later --
  the Interpretation Act 1987's counting rules (not deposited) might give another end day in a short month.
- **F2** ss 24(3), 21(2), 29 -- `What kind of public interest disclosure did I make` -- a head of agency's determination
  makes a disclosure voluntary even if wilfully false, until revoked (s 29(8)-(9) would be idle otherwise), and even if
  made orally to a Minister, but does not turn a witness or mandatory disclosure into a voluntary one (it is a public
  interest disclosure already) -- s 21(2) prevails over a determination; or s 24(3) bars a determination too.
- **F3** s 21(2) "to the extent that" -- `What kind of public interest disclosure did I make` -- a wilfully false or
  misleading disclosure is not a public interest disclosure at all -- only the false or misleading part loses the
  status, the rest keeping it.
- **F4** s 31(3)-(4) -- `Was it reasonable management action`, `Is the person liable to me in damages` -- action that is
  not management action at all, and listed action that is not itself reasonable, are `JUST FALSE`; reasonable management
  action of a kind not listed is `NOTHING` (the list says "includes") -- unlisted reasonable management action is
  reasonable management action (`JUST TRUE`).
- **F5** s 37(1) -- `Can I apply for an injunction` -- an applicant outside (c)-(d), or conduct that is not even
  possibly a detrimental action offence, is `NOTHING` (a grant limited in its own words) -- `JUST FALSE`, the list of
  applicants being exhaustive.
- **F6** s 38(1) "unless" -- `Can I be ordered to pay the other side's costs` -- once vexatiousness or an unreasonable act
  is shown, `NOTHING` (the ordinary costs rules decide) -- `JUST TRUE`.
- **F7** s 59(3) "at intervals of not more than 3 months throughout the duration of the investigation" -- `Is my
  progress update overdue` -- the first interval runs from the day the investigation began -- from the day the agency
  first told the maker it would investigate (s 59(2)(b)), or from the day of the decision to investigate.
- **F8** s 61(1) -- `Who pays me damages under section 62` -- where the agency is not a "responsible agency" (not aware,
  or neither related nor associated) the answer is `NOTHING` (a scope limit with no "only") -- `JUST` no one, there being
  no s 61(2) duty to fail.
- **F9** s 64(4)-(5) -- `Does section 64 stop my identity being revealed` -- the answer is about s 64 alone; the ICAC,
  Ombudsman and LECC Acts prevail, and other restrictions still apply -- ask them as facts.
- **F10** s 28(1)(e)(i) "has not, at the end of the investigation period, received" -- `the section 28 conditions are
  met` -- a disclosure to a member of Parliament or a journalist on or before the last day of the period does not meet
  (e)(i) -- the condition looks only at what was received by the end of the period, whenever the later disclosure is
  made.
- **F11** s 26(3) "a grievance about a matter relating to the employment or former employment of an individual" --
  `the disclosure complies with section 26` -- any individual's employment, not only the maker's -- the maker's only.
- **F12** s 60(2)(a) -- `Can I apply for internal review` -- an application made before the applicant is told of the
  decision is not out of time -- it is premature and invalid.
- **F13** s 40(1) "the maker of a public interest disclosure" -- `Am I protected from this liability` -- a disclosure
  that is not a public interest disclosure answers `NOTHING` (other laws, such as the ICAC Act Part 8A, may protect) --
  `JUST FALSE`.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 33(1) | anyone | duty not to take detrimental action (offence) | comment; `By what day must a prosecution be started` |
| s 35(1) | the person who takes detrimental action | liability in damages | `Is the person liable to me in damages` |
| s 36 | the court | power to order the employer to pay | `Can the employer be ordered to pay` |
| s 37(1) | the discloser, a person at risk | power to apply for an injunction | `Can I apply for an injunction` |
| s 38(1) | the claimant | immunity from costs | `Can I be ordered to pay the other side's costs` |
| s 40(1) | the maker | immunity from civil, criminal and disciplinary liability | `Am I protected from this liability` |
| s 41(4) | the maker with an undertaking | immunity (evidence inadmissible) | `Can my disclosure of past conduct be used against me` |
| s 49(1) | the agency | duty to deal with the disclosure | `Must the agency deal with my disclosure as voluntary` |
| s 59(3) | the agency | duty with a deadline (3 months) | MUST rule, `Is my progress update overdue` |
| s 60(1)-(2) | the maker | power to apply within 28 days | DO rule, `Can I apply for internal review` |
| s 62(1) | the agency or the State | liability in damages | `Who pays me damages under section 62` |
| s 64(1) | public officials and agencies | duty not to disclose identity | `Does section 64 stop my identity being revealed` |
| s 65 | the public official | duty to assist when asked | `Must I help with the investigation` |

## What the Act turns out to say

1. **No time limit for the damages claims.** ss 35 and 62 set no limitation period, and say the liability "is not
   liability in tort" (ss 35(10), 62(8)); the period comes from the Limitation Act 1969 for an action on a statutory
   liability, which a discloser reading this Act alone would not learn. Only the prosecution has a limit (3 years,
   s 33(6)).
2. **A determination and s 21(2) pull against each other.** s 29(1) deems a disclosure voluntary "even if" it would not
   otherwise be; s 21(2) says a wilfully false disclosure is not a public interest disclosure; s 29(8)-(9) lets the head
   revoke for wilful falsity, with effect from the start. The encoding lets the determination stand until revoked (fork
   F2; asserted).
3. **s 24(3) is written over both limbs of s 24(1).** Literally a determination under s 29 cannot make a witness,
   mandatory, or oral-to-a-Minister disclosure voluntary, which is hard to square with "even if". Fork F2.
4. **The journalist route opens only after the period ends.** s 28(1)(e)(i) can be met only once the 6 (or 12) months
   have ended without the required information, so the first day is the day after; a s 55(3) decision (e)(ii) opens it
   at once. Fork F10; asserted.
5. **Costs immunity does not reach the claim against the agency.** s 38 protects a person who institutes proceedings
   "under section 35 or 37"; a claim under s 62 against the agency or the State has no such protection. Asserted
   (`NOTHING` outside ss 35, 37).
6. **The identity duty has no sanction in this Act.** s 64(1) says identifying information "is not to be disclosed",
   but no penalty or remedy follows in the Act; a breach may itself be detrimental action (s 32), which is where the
   remedy lies.
7. **Information rights belong to voluntary disclosers only.** s 59 binds an agency "dealing with a voluntary public
   interest disclosure"; a witness or mandatory discloser has no right to updates or reasons. Asserted (`NOTHING`).
8. **The reversed onus shapes the claim.** ss 35(4), 33(4), 37(7) and 62(3) put the proof of the mental element, or of
   compliance, on the defendant; the questions ask what the other side "has proved", and an unproven suspicion also
   takes management action outside s 31 (s 31(4)(d)), so listed management action not shown to be for risk reduction
   leaves the person liable. Asserted.
9. **Witnesses need not be public officials.** s 22 has no maker requirement, so a member of the public who answers an
   investigator's request makes a public interest disclosure and gets s 40 protection (to the extent of s 40(2)).
   Asserted.

## Questions (exported)

`pid-disclosures.l4` (4): `Am I a public official` (s 14), `Is what I am reporting serious wrongdoing` (s 13, the
Dictionary), `From what day may I go to a member of Parliament or a journalist` (s 28(1)(e)(i), (2)), `What kind of
public interest disclosure did I make` (ss 21-29).

`pid-protections.l4` (10): `Was it detrimental action` (s 32), `Was it reasonable management action` (s 31), `By what day
must a prosecution be started` (s 33(6)), `Is the person liable to me in damages` (ss 31, 32, 35), `Can the employer be
ordered to pay` (s 36), `Can I apply for an injunction` (s 37), `Can the injunction order this` (s 37(2), (4), (6)), `Can
I be ordered to pay the other side's costs` (s 38), `Am I protected from this liability` (ss 7(2), 40, 41(1)), `Can my
disclosure of past conduct be used against me` (s 41).

`pid-dealing.l4` (8): `Must the agency deal with my disclosure as voluntary` (s 49), `By what day must I get my next
progress update` (s 59(3)), `Is my progress update overdue` (s 59(3), (5), with the MUST rule), `By what day must I apply
for internal review` (s 60(2)(a)), `Can I apply for internal review` (s 60, with the DO rule), `Who pays me damages under
section 62` (ss 61, 62), `Does section 64 stop my identity being revealed` (s 64), `Must I help with the investigation`
(s 65).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Public Interest Disclosures Regulation 2022 and bring its declarations in.
- Have a lawyer review the forks, especially F2 (determinations), F4 (reasonable management action) and F10 (s 28).
- Link the damages questions to the Limitation Act 1969 baseline for the time limit (finding 1).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
