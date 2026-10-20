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
