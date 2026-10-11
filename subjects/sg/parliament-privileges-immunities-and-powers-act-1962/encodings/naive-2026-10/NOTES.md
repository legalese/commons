# Parliament (Privileges, Immunities and Powers) Act 1962 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions as the example rows show them (the skill itself was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/PPIPA1962.txt`. The page footer reads "version in force
from 9/3/2025". The cover says the edition "incorporates all amendments up to and
including 1 December 2021 and comes into operation on 31 December 2021"; later
amendments are annotated in the body, [Act 25 of 2021 wef 01/04/2022] on s 7(1) and
[Act 5 of 2025 wef 09/03/2025] on ss 34 and 40, the latest annotated.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0139** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The person who meets this Act is a publisher or journalist, a witness summoned before a
committee, someone in the public gallery, someone who offers a Member an inducement, or
a Member and the Member's family. So the row takes the Member's immunity and its
suspension (ss 5, 6, 20(2), (3)), protection of Parliamentary publications (ss 7, 8),
exemption from service, arrest and process (ss 9 to 11), summonses and warrants
(ss 13, 25, 26), witnesses (ss 15 to 17, 31(m)), Parliament's punishments (ss 20, 21(2),
22(2)), a suspended Member's pay (s 29(3)), offences and penalties (ss 31, 35, 36), the
referral bar (s 37), and the death gratuity for a Member who never held office
(s 11A(1), (2)(a), (3)(a), (6)).

Not encoded: s 3 (the privileges of the UK House of Commons "at the establishment of the
Republic of Singapore", imported wholesale and not set out in the Act), Parliament's and
the Speaker's internal powers (ss 4, 12, 14, 18, 19, 23, 24, 27, 28, 30), the President's
affairs-of-State certificate (s 16(1), (3)), ss 32 to 34 beyond their penalty, ss 38 to
40, and in s 11A the office-holder's commuted sum and the office-holder paragraphs. The
Standing Orders and the Parliamentary Pensions Act 1978 were not retrieved.

## What the Act turns out to say

### 1. The death gratuity's commutation factor multiplies an annual figure

s 11A(6) defines the Member's commuted sum as "the commutation factor of 175.14"
multiplied by the lower of two-thirds of annual salary and an accrual of 1/30 of annual
salary per completed year (1/360 per further month). Read literally, a Member with a
$15,000 monthly salary and 25 years' service gets 175.14 × $120,000 = $21,016,800, over
a hundred years' salary. *Inference, not in the text:* a factor of this size looks
calibrated to a monthly pension, not an annual one; the encoding follows the words.
Because the commuted sum dwarfs one year's salary at any service of 9 years or more, the
"whichever is the higher" comparison in s 11A(2)(a) always picks the commuted sum.
Asserted (the literal figures).

### 2. A Member's civil immunity can be switched off, but not the criminal one

s 6(1) protects a Member from civil and criminal proceedings for what is said in
Parliament. Under s 20(2), after a finding of abuse of privilege, Parliament may by
resolution suspend the immunity "insofar as they relate to liability to civil
proceedings", and s 20(3) then exposes the Member to civil suit. Criminal immunity is
untouched. Asserted.

### 3. A witness's evidence is shielded, except from perjury and offences under this Act

s 17: nothing said in evidence before Parliament or a committee founds proceedings
against the witness, nor is it admissible against him, except in proceedings for an
offence under s 191 of the Penal Code 1871 (false evidence) or under this Act. Refusing
a lawful or relevant question is an offence unless the refusal "is based on privilege or
is excused" (s 31(m)); a witness has the same privilege as in court (s 16(2)). Asserted.

### 4. Parliament itself may fine up to $50,000 and imprison to the end of the session

s 20(1) and (4) let Parliament fine a Member or a stranger up to $50,000 and commit them
to prison "for a term not extending beyond the current session". The menus differ:
suspension and reprimand "in his place" are for Members, exclusion and reprimand "at the
Bar of the House" for strangers, and expulsion only for a Member on a select committee's
report (s 21(2)). The penalties a court may impose are far lower: s 36 caps them at
$10,000 or 7 years for the s 35 inducement offence, $7,000 or 3 years for s 31(d), (o),
(p), (q), and $5,000 or 2 years for everything else. No court prosecution may begin
without Parliament's referral to the Public Prosecutor (s 37). Asserted.

### 5. A publisher of an authorised report can have a prosecution or suit stopped on 24 hours' notice

s 7: a defendant who gives 24 hours' written notice and produces a certificate of the
Speaker or the Clerk that the publication was authorised by Parliament obtains an
immediate stay, and the proceedings are "deemed to be finally determined". For an
extract or abstract, s 8 requires the court to be satisfied it was published "bona fide
and without malice". Asserted.

### 6. Service of a summons is strict, and only after due service can a warrant issue

ss 13(3), 25(3): a summons is served by delivering a copy to the person or by leaving it
at his usual or last known abode in Singapore "with some adult person". Email,
letterbox and a child do not suffice. s 26(1): the Speaker may issue a warrant for a
person who does not attend only "upon being satisfied that the summons was duly served".
Asserted.

### 7. Inside the precincts while Parliament sits, no civil or criminal process may be served

s 11, except for a contravention of the Act itself. s 10 adds that a Member going to, at
or returning from a sitting cannot be arrested on a civil matter. Asserted.

### 8. A Member's offence after a dissolution must be raised within 21 days

s 22(2): after prorogation or dissolution, Parliament may not take cognizance of a
Member's offence unless complaint is lodged within 21 days of the commencement of the
next Parliament. Asserted.

## What would need doing before this is worth anything

- Section 3 imports the UK House of Commons' privileges "at the establishment of the Republic of Singapore"; none of
  that is encoded, and it is likely where most contested questions would be decided.
- The Standing Orders (which govern suspension under s 19 and the Speaker's orders under
  s 31(a)) and the Parliamentary Pensions Act 1978 (which s 11A depends on) were not
  retrieved.
- s 11A's office-holder paragraphs, the office-holder's commuted sum, the deduction of
  sums already received, and the 20 May 2011 cut-off are not encoded; "within one year"
  in s 11A(1)(b) is read as 12 whole months.
- No Committee of Privileges reports or case law were searched.
