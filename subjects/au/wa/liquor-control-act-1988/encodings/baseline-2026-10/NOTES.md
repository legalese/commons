# Liquor Control Act 1988 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. There was no earlier encoding of this Act.

## Edition

- **The Act:** the WA Legislation consolidation, deposited at
  `../../registers/source-bundle/mrdoc_49727.txt` (retrieved 2026-09-07). Its
  compilation table runs to the Liquor Control Amendment Act 2025 (No. 20 of 2025).
  Part 3 of that Act came into operation on 1 July 2026.
- **Regulations:** none. The Liquor Control Regulations 1989 are not deposited. Three
  things they settle are left open:
  - the further forms of proof of age (s 126(1)(b)(i)(IV)), offered as one choice;
  - the circumstances in which consent-based supply is barred (s 122A(3)(e)), an input;
  - which offences an infringement notice may be given for (s 167(2)(a)). The
    modified penalty is answered on the assumption that a notice is given.

## Checks

- One module (`lca-juveniles.l4`) and one case file (`lca-cases-juveniles.l4`).
- **45 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98.
- The case file is built by `gen_wa_liquor-control-act-1988_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.

## Seat

**The young person**: someone who is, or may be, a "juvenile" (under 18), asking
"May I buy and drink alcohol now?". The Act is mostly licensing and addresses
licensees, but its one life event (Chloe turning 18) asks what changes for her.
Division 9 is where the Act reaches the young person directly. The decisions are
phrased as that person asks them:

- `Am I a juvenile`;
- `May I buy and drink alcohol here now`;
- `Is it an offence for me to be on licensed premises` (and on regulated premises);
- `Is it an offence for me to buy or get liquor here`, `... to have liquor here`,
  `... to drink here`;
- `Is it lawful for this person to give me alcohol here`;
- `Can I be required to show evidence of my age`, `Does this count as evidence of my age`,
  `Can my ID be confiscated`;
- `What is the most I can be fined`, `What would an infringement notice ask me to pay`.

Where Division 9 addresses someone else, the encoding says what it means for the young
person:

- the licensee or the supplier: whether the person who gave me a drink broke the law,
  their maximum fine, and whether they can say they thought I was 18;
- the authorised person: when I can be asked my age, made to show ID, made to leave,
  or have my ID taken;
- the employer: whether I may be employed to serve liquor.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The
  regulations are not deposited, so what they settle is an input or left open (see
  Edition).
- **The actors the text names.** Followed: the juvenile, the responsible adult, the
  parent or guardian, the licensee and manager, the authorised person, and the
  Director.
- **A judgment handed to someone else is answered conditionally.** Followed. These
  are all inputs:
  - the authorised person's knowledge or reasonable suspicion;
  - the Director's approvals;
  - the seller's reasonable belief;
  - whether someone is "drunk";
  - whether the supplier is able to supervise.
- **The Act's definitions worked out; borrowed terms asked.** Followed for "juvenile"
  (from the date of birth) and "responsible adult" (from who the companion is).
  "Licensed premises", "regulated premises" and "unlicensed premises" are asked as the
  kind of place. Regulated premises rest on a long list in s 122(1) that the person
  can usually answer.
- **One case is the text's natural unit.** Followed: one young person at one place on
  one occasion.
- **The Act's own terms, each glossed.** Followed in comments.
- **Operative sections in; machinery out.** Partly departed from, for size: only
  Division 9 and s 167 are in. Licensing, the s 119 offences that bind everyone,
  banned drinkers and barring are out, because they are not the young person's
  question.

## The lives

- **Chloe, c025 (14 March 2021): turns 18.** The decision is
  `May I buy and drink alcohol here now`, from her date of birth (14 March 2003) and
  the date:
  - on her birthday, at licensed premises: yes;
  - the day before: no;
  - the day before, at home: no juvenile offence of hers.

  `Am I a juvenile` gives TRUE on 13 March 2021 and FALSE on 14 March 2021.

## Why this scope

The brief asked for a small baseline (25-45 assertions) from the young person's seat
only: the juvenile offences (buying, drinking on licensed premises, being on premises),
supply to a juvenile including by a parent at home, proof of age and false ID, and the
penalties that fall on the juvenile. That is Part 4 Division 9 (ss 120-126) and the
infringement-notice rule in s 167. Of s 120 only the limbs a young person can state
are encoded: (1)(b) living there, (1)(f) a lawful business, and (2) passing through.
The club, reception, transport and Director-approved-area limbs ((1)(a), (c), (d),
(e)) are left out. The accompanied and meal parts of (1)(c) are reached through
s 121(5)(a). The penalties are those printed in the deposited text. Chloe's 2021
event took place before the amendments of No. 20 of 2025, which touched these
sections (for example s 121, s 123, s 126). The figures in force in 2021 were not
read.

## What the Act turns out to say

1. **The line is the 18th birthday, and the Act says nothing about 29 February.**
   "juvenile means a person under the age of 18 years" (s 3(1)). On 14 March 2021
   Chloe is not a juvenile and none of the Division 9 offences can touch her; the day
   before, all of them can. Asserted.

2. **A parent lets a juvenile be in the pub, not drink there.** Being "accompanied by,
   and under the supervision of, a responsible adult" excuses being on licensed
   premises (s 121(5)(a)(i)). But s 123(1)(c) makes it an offence for the juvenile to
   consume liquor on licensed premises, whoever is with them, and the parent cannot
   lawfully supply it there (ss 121(1), 122A(2)). Asserted.

3. **An adult friend is not a responsible adult, and a parent who is not supervising
   does not count.** A responsible adult is an adult who is a parent, step-parent,
   spouse, de facto partner, legal guardian or person in loco parentis (s 125(2)(b)),
   and s 121(5)(a)(i) also needs supervision. An older friend does not qualify, nor
   does a spouse who is under 18. Asserted (friend; unsupervised parent).

4. **On regulated premises, a parent does not help at all.** s 122(3) excuses only
   being there "for the purpose of obtaining a meal" (and the s 122(4) cases: living
   there, a lawful business, passing through, training, non-liquor work). The
   responsible-adult exception in s 121(5) has no counterpart. Asserted.

5. **An out-of-bounds declaration overrides the parent and the meal.** s 121(8) shields
   from removal only juveniles who live there, are carrying on a business, are passing
   through, are on an approved course, or work there. A juvenile with a parent, or
   there for a meal, can be required to leave a declared area. Not leaving is a
   $3 000 offence (s 121(7)). Asserted.

6. **A road is "regulated premises" for buying but not for drinking.** s 122(1)(g)
   makes a road (with its footpath and vehicles on it) regulated premises "for the
   purpose only of" the sale or supply to, and purchase or obtaining by, a juvenile.
   So buying or getting liquor on a road is a s 123(1)(a) offence. Drinking or
   carrying it there is caught by s 123(2) instead (possession in a place the public
   can go). Asserted (buying on a road).

7. **At home, a juvenile commits no juvenile offence by drinking.** s 123 reaches only
   licensed or regulated premises and places the public can go. Whether the drink
   was lawfully given is a question about the supplier, not the juvenile. Asserted.

8. **The s 122A(3) limits bind the consenting adult, not the parent.** A parent or
   guardian may supply on unlicensed premises outright (s 122A(2)(a)). The bars
   (someone is drunk, no supervision, prescribed circumstances) apply only to someone
   relying on the parent's consent (s 122A(2)(b), (3)). So the Act does not stop a
   parent giving a drunk juvenile more at home; it does stop a family friend. The
   maximum for unlawful supply is $10 000. Asserted.

9. **"Drunk" in s 122A drops the licensed-premises limb.** s 122A(1) uses only
   s 3A(1)(b) and (c), noticeably impaired and reasonably attributed to liquor,
   because the s 3A definition otherwise requires being on licensed or regulated
   premises. Not asserted (drunkenness is an input).

10. **"Unlicensed premises" is undefined; a parent handing a drink on a footpath is
    caught by s 122(2).** INFERENCE: s 122A's "unlicensed premises" is any place that
    is not licensed premises. But on regulated premises, and on a road for supply,
    s 122(2) forbids anyone to supply a juvenile, with a $15 000 maximum and no parent
    exception. So a lawful supply under s 122A is one at a home or another public
    place such as a park. Asserted (parent on a road: not lawful; parent at home:
    lawful).

11. **The seller can say they thought I was 18 only if I was at least 16.** s 125(1)(b)
    needs a belief on reasonable grounds and a juvenile "of or above the age of 16
    years". Asserted.

12. **At 16 a juvenile may serve liquor with meals, under four conditions.** s 121(11)
    needs the Director's approval, supervision at all times, and a prescribed training
    course being assessed or completed. Otherwise employing a juvenile to sell, supply
    or serve liquor is a $15 000 offence for the employer (s 121(10)). Asserted (15
    no, 16 yes).

13. **Proof of age is a closed list, and a photo of your card is not on it.** A current
    photo driver's licence, passport, or WA photo card, a prescribed form, or digital
    evidence in its original digital form or by QR code (s 126(1)(b)(i), (2C)) all
    count. "a digital photograph of a physical card" does not count. Asserted (digital
    yes; photo of card, student card no).

14. **A suspected fake can be confiscated, unless it is a passport or digital.** s 126(2a)
    excludes (1)(b)(i)(II), the passport, and s 126(2D) excludes digital evidence. I
    need not hand over my phone (s 126(2E)). Asserted.

15. **A fake ID is an offence in itself, and going back in within 24 hours is another.**
    Producing evidence "false or misleading in any material respect" is an offence
    with no reasonable-excuse escape (s 126(2)(b)); re-entering within 24 hours is
    separately an offence (s 126(4)). Each carries $3 000. Asserted.

16. **The juvenile's fines.** Getting an adult to buy on licensed premises: $2 000
    (s 121(3), both commit it). Every other juvenile offence: $3 000. An infringement
    notice, where the offence is prescribed, asks for 10% (s 167(3)), so $300 or
    $200, payable within 28 days (s 167(2A)(b), (4)). Asserted ($2 000; $300).

## What would need doing before this is worth anything

- Deposit the Liquor Control Regulations 1989 for the prescribed proof-of-age forms,
  the s 122A(3)(e) circumstances, and the list of offences open to infringement
  notices.
- Read the penalty figures in force in 2021 (before No. 20 of 2025) if Chloe's event
  is to be answered as at its date.
- Decide whether "unlicensed premises" in s 122A includes regulated premises (finding
  10). No case law was searched.
- Add s 119 (offences that bind everyone, juvenile or not), which a young person
  drinking in a park also meets, and the remaining limbs of s 120.

## Q&A layer (seat and situations as parameters)

Added on 6 November 2026 (batch qa1), on Michael's approval of the design of the graffiti encoding's seat layer
(`subjects/au/wa/graffiti-vandalism-act-2016/encodings/baseline-2026-10/`, its D2, D4 and D8). The layer is
`lca-qa.l4`, and its cases are in `lca-qa-cases.l4`. It imports `prelude` and `lca-juveniles`. The baseline's files are
unchanged: the layer adds to them and replaces nothing.

**Roles.** Every exported question takes `my role` IS A `Role` first ("Which of these describes you"). A question about
another role answers `does not arise for you` without reading any other input.

- `I am a young person (under 18, or about to turn 18)`: the baseline's seat. Its 25 questions are the baseline's 25
  exports, each calling the baseline function.
- `I am a parent, guardian or other adult with a young person`: Division 9 binds "a person" who:
  - supplies liquor to a juvenile (ss 121(1)(c), 122(2), 122A);
  - buys liquor for a juvenile at their request (s 121(3));
  - accompanies a juvenile as a responsible adult (ss 121(5)(a)(i), (9), 122(3)(b));
  - sends a juvenile for liquor (s 124).

  9 questions.
- `I hold a licence, manage licensed premises, or sell or serve liquor`: bound by ss 121(1), (4), (10) and 122(2), with
  the s 125(1)(b) and (c) defences. The licensee, a manager and their staff are also "authorised persons" (s 3(1)), so
  the s 126 powers are theirs. 11 questions.

The Director, inspectors and the police are not seats. A police officer is an authorised person too, but appears only
as what s 126 means for the young person.

**Situation inputs.** Each one is a BOOLEAN placed second. FALSE gives `does not arise for you`.

| Name | Role | Questions that take it |
|---|---|---|
| `the area is declared out of bounds to juveniles now` (the baseline's own input) | young person | 2: can I be made to leave (s 121(6)-(8)); have I committed an offence by not leaving (s 121(7)) |
| `an authorised person has asked my age, or for evidence of it` | young person | 5: show evidence (s 126(1)(b)(i)); does it count (s 126(2C)); made to leave (s 126(1)(b)(ii)); confiscation (s 126(2a), (2D)); offence in answering (s 126(2)) |
| `I have been required to leave, or removed from, the premises` | young person | 1: going back in within 24 hours (s 126(4)) |
| `someone has given or sold me alcohol, or offered to` | young person | 3: is it lawful (ss 121(1), 122(2), 122A); the supplier's fine; the seller's s 125(1)(b) belief |
| `I was sent to get liquor` (the baseline's own input) | young person | 1: s 124 |
| `I work, or want to work, selling, supplying or serving liquor` | young person | 1: s 121(10), (11) |
| `I have given, or would give, alcohol to a person under 18` | adult | 3: may I give it here (ss 121(1), 122(2), 122A); s 125(1)(b) belief; buying at their request (s 121(3)) |
| `I am, or will be, with a person under 18 on licensed or regulated premises` | adult | 4: am I a responsible adult (s 125(2)(b)); their presence (s 121(4), (5)); leaving them behind (s 121(9)); regulated premises (s 122(3)(b)) |
| `I have sent, or would send, a person under 18 to get liquor` | adult | 1: s 124 |
| `liquor has been, or may be, sold or supplied to a person under 18 at my business` | licensee or seller | 3: ss 121(1), 122(2); s 125(1)(b); s 125(1)(c) |
| `a person under 18 is, or wants to be, on my licensed premises` | licensee or seller | 1: s 121(4), (5) |
| `I employ, or would employ, a person under 18 to sell, supply or serve liquor` | licensee or seller | 1: s 121(10), (11) |
| `I suspect a person on the premises is under 18` | licensee or seller | 5: s 126(1)(a), (1)(b)(i), (2C), (1)(b)(ii), (2a) |

The `@desc` texts are in `lca-qa.l4`, and in `encoding.json` under `qa_layer.situation_parameters`.

**Decisions.**

- QA1. **Two of the baseline's inputs became situations.** `the area is declared out of bounds to juveniles now` and
  `I was sent to get liquor` are what ss 121(6)-(8) and 124 turn on.
  - Each is placed second, with the baseline's name and `@desc`.
  - Where the situation holds, the baseline is called with the input as given. So the answers are the baseline's, and
    the situation-false cases show that nothing else is read.
- QA2. **Several facts are TRUE by a question's own terms:**
  - for the adult's s 124 question, that the young person was sent;
  - for the licensee's s 126 questions, that the authorised person suspects the person is under 18 (that is the
    situation);
  - for the adult's s 125(2)(b) and s 121(4) questions, that the adult is 18 or over (the role).

  Each is passed as TRUE, with a comment in the code.
- QA3. **The adult's and the licensee's s 121(4)-(5) questions reuse the young person's.** s 121(4) makes the licensee,
  a permitting employee or agent, and the juvenile each commit an offence on the same facts, and s 121(5) excepts them
  all alike. So the baseline's `Is it an offence for me to be on licensed premises` decides the question; the licensee's
  version adds the employee's permission (s 121(4)(b)). The baseline's `Reason` and `Evidence` choices are worded as
  the young person would say them, and the `@desc` says so.
- QA4. **The adult's and the licensee's companion choices** are their own enumerations (`How I am related to the young
  person`, `Who is with the young person`), mapped onto the baseline's `Companion`, listing every value with no
  OTHERWISE.
- QA5. **Fork, s 122(2) and the licensee as such.** On regulated premises, and on a road, the licensee's question
  answers no for `the licensee` and `the manager supervising the premises at the time`. s 122(2) names "a person who
  sells or supplies, or permits", not the licensee as s 121(1)(a) does. A licensee who permitted the sale chooses
  `a person who permitted it`. The other reading, that the licensee always permits what is done on their premises,
  would answer yes. Asserted on the first reading.
- QA6. **The licensee's sale question covers ss 121(1) and 122(2) only.** For a sale at another public place or a
  private place it answers no, and its text names only those sections. s 122A is asked from the adult's seat.
- QA7. **The penalty tables of the new roles are new helpers.** `the most an adult can be fined for` and `the most a
  licensee or seller can be fined for` take the figures printed in the deposited text, as the baseline's table does for
  the young person.

**Not covered for the new roles.**

- **The adult:**
  - s 120(1) clubs, receptions and the like;
  - s 121(1)(d), "any person who permits", beyond its fine;
  - s 122(2)(b), permitting drinking or possession on regulated premises, beyond its fine;
  - s 119 and the offences that bind everyone;
  - the regulations' s 122A(3)(e) circumstances, which are an input.
- **The licensee or seller:**
  - s 121(2), permitting a juvenile to drink, and s 121(6) declaring an area out of bounds, beyond their fines;
  - s 121(7) and (7a), removing a juvenile;
  - s 125(1)(a), the family and lodger defences;
  - s 126(3)-(5), removal and re-entry, from the licensee's seat;
  - approvals under ss 126A and 126B;
  - licensing itself, and s 115.

**Cases.** `lca-qa-cases.l4` has 287 assertions. All 287 are satisfied, with 0 errors and 0 warnings, on the stable
`l4` of VS Code extension 1.6.98 with `JL4_LIBRARY_PATH` unset. They are:

- 90 cases that ask each of the 45 questions for the two roles it is not about, with every other input ASSUMEd;
- 31 cases that ask each question with a situation input, for its own role, with the situation FALSE and every later
  input ASSUMEd (13 for the young person, 8 for the adult, 10 for the licensee or seller);
- 57 young-person cases against values worked by hand, most taken from the baseline's cases (c025, Chloe turning 18,
  among them), and the same 57 again against the baseline export's own answer on the same facts;
- 23 adult cases and 29 licensee or seller cases, worked by hand from the text.

**Negative controls.** Each of these fails, as it should:

- an adult question with the situation TRUE and an ASSUMEd relation;
- a wrong expected value for the licensee.

**Other checks.**

- The parameter script (`check_params.py`, in the batch scratchpad) checked that:
  - `my role` is first in each of the 45 questions;
  - each of the 13 situation inputs is second, and identical in name, type and `@desc` wherever it occurs;
  - each role branch reads its situation input first;
  - no input is DEONTIC or EVENT.
- No input name carries two `@desc` texts.
- `l4 check lca-qa.l4` succeeds.
- `lca-juveniles.l4` and `lca-cases-juveniles.l4` (45 of 45) still run with no error or warning.
