# Betting Control Act 1954 (WA) — baseline encoding

## Method

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as
advice.

There was no earlier encoding of this Act.

## Edition

The compilation incorporating amendments to the Gambling Legislation Amendment
Act 2024 (No. 53 of 2024), as deposited at
`../../registers/source-bundle/mrdoc_48877.txt` (retrieved 7 September 2026).

The deposit's uncommenced provisions table lists most of the TAB (Disposal) Act
2019 (No. 21 of 2019) as "To be proclaimed". Part 1A (wagering licences, inserted
by s 47 of that Act) is in force; s 23 still names RWWA.

No regulations are deposited, so the following are asked as facts:

- the Betting Control Regulations' rules on telephone and internet betting with a
  bookmaker (s 12(3b));
- the prescribed prohibited events or contingencies (s 4(1));
- whether betting on an event is permitted by another State's or Territory's law
  (s 27A(1));
- social gambling and permitted gaming (borrowed from the Gaming and Wagering
  Commission Act 1987, s 23(1)(e)).

## Checks

One module (`bca-gambler.l4`, 17 exported questions) and one case file
(`bca-cases-gambler.l4`). 39 assertions satisfied, 0 errors, 0 warnings, with
the stable `l4` from VS Code extension 1.6.98 (`runcases.py`: written 39,
satisfied 39, errors 0).

## Seat

**The gambler**: the individual in WA who bets on races and other events, by app,
at the TAB, with a bookmaker or with friends, and the child who wants to. Most of
the Act addresses operators: the wagering licensee, bookmakers, RWWA, racing clubs,
licensed premises. But it also lays offences directly on "a person" who bets
(ss 23, 24, 27A) and on a child (s 22), which the Interactive Gambling Act 2001
does not. The encoding asks what the Act makes of my bet, what I can be fined,
what an operator may not do to me, and what a court can order against bookmakers
betting with me.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed.
  - The fines are in the Act.
  - No regulations are deposited; what they would decide is asked as a fact (see
    Edition).
- **The actors the text names.** Followed: RWWA (the TAB), the wagering licensee,
  a bookmaker (licensed under the Act), an "authorised person" under s 27A, the
  Magistrates Court, the stewards and the Commission.
  - Two operators the text does not name are added because the gambler meets them:
    - "an unlicensed bookmaker" (the s 24(1)(b) description);
    - "a friend or workmate, privately" (for s 23(1)(e)).
- **A judgment the law hands to someone else is answered conditionally.**
  Followed:
  - the Magistrates Court's satisfaction under s 25(1) and its opinion that I
    have not reformed (s 25(2));
  - "apparently" under 18 or drunk (s 21);
  - whether the bookmaker takes the bet as the Act allows.
- **The Act's own definitions worked out; borrowed terms asked as facts.**
  - Worked out: "interstate or offshore bet", "authorised person" and
    "permitted event or contingency" (all s 27A(1)).
  - "Bookmaker" (s 4(1)) is the choice of operator.
  - Asked as facts: social gambling and permitted gaming (Gaming and Wagering
    Commission Act 1987), metropolitan region (Planning and Development Act 2005).
- **One case is the text's natural unit.** Followed: one bet.
  - Simplification: limb (c) of "interstate or offshore bet" ("with a person who
    is outside the State") is read as the operator being licensed outside WA
    (interstate or offshore). The encoder's reading.
- **The Act's own terms, each with a plain gloss.** Followed in comments and
  `@desc` lines.
- **Operative sections in; machinery out.** Followed. Out:
  - licensing (Parts 1A and 2, except as glosses);
  - levies and totalisator finance (Part 3);
  - race fields;
  - operators' and premises' duties;
  - search, evidence and discipline;
  - the Commission, regulations and transitional Part 6.

## The lives

- **jake k080** (1 September 2045, aged 39): Lotto on Saturdays, the casino on
  paydays, then betting apps. *Is this betting lawful?* The scenario does not say
  which apps or events; the encoder takes three.
  - The TAB app on a race at Ascot: lawful. Asserted.
  - An app licensed in the Northern Territory on an AFL match in Melbourne:
    `uncertain`. It is no offence under s 27A, but ss 23(1) and 24(1)(b), read
    literally, reach it (see finding 2). Asserted.
  - An offshore site the Commission has not exempted, which he knows is
    unlicensed: an offence under s 27A(2), with a fine of up to $10,000. Asserted.

  Lotto (Lotteries Commission Act 1990) and the casino (Casino Control Act 1984)
  fall under other Acts. The online-supply side (which apps may lawfully be offered
  to him at all) is the Interactive Gambling Act 2001 baseline's.
  - His daughter Ruby (12) betting on the TAB app, or asking him to put a bet on,
    is the encoder's illustration: she commits an offence (s 22, up to $2,000),
    and he does if he places it (s 22A, up to $10,000). Asserted.

## Why this scope

The plan entry cites "Part 2 — other licences, approvals and permits". Part 2 is
bookmakers' licensing, which reaches the gambler only through the definition of
"bookmaker" (a licence holder) and the racecourse rules in s 12. The question the
event asks, "which gambling is lawful", is answered in Part 4: ss 22, 23, 24 and
27A. So those are the core, with Part 2 used for the definition and s 12. Part 4's
other provisions that fall on the individual are in, as are what an operator may
not do to them (ss 10J(2), 21), the s 25 order and s 32 disputes.

## What the Act turns out to say

1. **The gambler can commit offences under this Act, unlike under the
   Interactive Gambling Act.**
   - Betting in WA outside the permitted channels: s 23(1), up to $100,000.
   - Betting with an unlicensed bookmaker: s 24(1)(b), up to $100,000.
   - Betting with a licensed bookmaker otherwise than in accordance with the Act:
     s 24(1)(c), up to $100,000.
   - Making an interstate or offshore bet with an operator one knows is not
     authorised, or on an event that is not permitted: s 27A(2), (2A), up to
     $10,000 each.

   This is consistent with the Interactive Gambling Act baseline, whose finding 1
   is that the player commits no offence under *that* Act. Asserted.
2. **Interstate betting apps are not clearly lawful on the text.**
   - s 4(1) "bookmaker" requires "a current bookmaker's licence", and a "licence"
     is one "issued under this Act". So an app licensed only in another State is
     not a "bookmaker".
   - s 23(1)(d) excuses only the totalisator, a fixed odds bet with RWWA and a
     bookmaker.
   - s 24(1)(b) reaches betting with a person carrying on business as a bookmaker
     without a current bookmaker's licence.
   - Yet s 27A treats a person licensed in another State as an "authorised
     person", and makes an interstate bet an offence only when the operator is not
     authorised or the event is not permitted. That implies the rest are not
     offences.

   The encoding does not guess which reading a court would take. Such bets come out
   `uncertain`, with the literal reading's $100,000 as the most they expose one to.
   A bet with an interstate app on an event *in* WA is not an "interstate or
   offshore bet" at all (s 27A(1)(a)), so s 27A gives it no shelter. Asserted.
3. **A fixed odds bet with a wagering licensee is not named in s 23(1)(d).**
   - s 23(1)(d)(ii) names "a fixed odds bet with RWWA", but Part 1A (in force)
     licenses a wagering licensee to conduct fixed odds betting.
   - Most of the TAB (Disposal) Act 2019 is uncommenced. Presumably it would
     extend s 23 (an inference; the uncommenced text is not deposited).
   - A wagering licensee's totalisator bet is lawful under s 23(1)(d)(i).

   Asserted (`uncertain` for fixed odds, lawful for the totalisator).
4. **"Offshore bet" in s 27A(2) is undefined.** The defined term is "interstate
   or offshore bet". The encoding reads (2) as using the defined term; read
   narrowly, (2) would reach only bets placed outside Australia. Asserted on the
   encoder's reading.
5. **Children are offenders, and so is the adult who helps.**
   - A person under 18 who bets with a racecourse totalisator, a licensed
     bookmaker or RWWA, or asks someone to place or collect a bet, commits an
     offence: s 22, up to $2,000.
   - An adult who knowingly places a bet or collects winnings for someone
     apparently under 18 commits one too: s 22A, up to $10,000.
   - s 22 does not name the wagering licensee, nor interstate or offshore
     operators. A child's bet with them is not a s 22 offence (an inference from
     silence; not asserted).

   Asserted for the TAB and the s 22A fine.
6. **WA has a court-ordered betting exclusion, s 25.**
   - The Magistrates Court, if satisfied that "by excessive betting" a person is
     likely to be impoverished so that they "or any member of the family ... is in
     want", may order that no bookmaker bet with them for up to one year.
   - The order is renewable while the person has not reformed.
   - RWWA, totalisator operators and bookmakers must honour it after notice
     (s 25(3)).
   - The Act does not say who may ask for the order.
   - The person named commits no offence by betting. Anyone who places a bet for
     them commits one: s 23(2), up to $20,000.

   This bears on jake k081, where Chloe "finds none in WA" (that event is not in
   this Act's plan entry). The Casino Control Act baseline is right that the
   casino Act has no family application, but this Act has a court order against
   betting. It does not reach the casino or online apps licensed elsewhere. Asserted
   for the one-year limit, renewal, the silence on applicants and the lack of an
   offence on the person named.
7. **Operators may not knowingly take bets from a person apparently under 18 or
   drunk** (s 21(1), (3)). The wagering licensee may not give credit (s 10J(2)).
   s 29 says the same for RWWA by reference to s 63 of the RWWA Act (not
   deposited). Asserted.
8. **Some offences carry no stated penalty.** Taking a child or liquor into a
   place where a totalisator is operating, and placing a TAB bet for a barred
   person (s 21(2)(b)-(d)), carry no penalty of their own. The s 30(1)(b) general
   maximum of $5,000 applies. Asserted for liquor.
9. **Disputes with a racecourse bookmaker go first to the stewards.** An appeal
   lies to the Commission within 3 days (metropolitan racecourse) or 7 days
   (elsewhere). The undisputed part of a bet must be paid (s 32(3)). Asserted.
10. **On conviction for betting contrary to the Act, money found on the offender
    and proved to be from that betting must be forfeited** (s 28(2)). Asserted.

## What would need doing before this is worth anything

- Deposit the regulations made under s 33 (not deposited; their title and year
  are not in the deposit). The Act points to them for the telephone and internet
  betting rules for bookmakers (s 12(3b)), the prohibited events (s 4(1)) and the
  prescribed Rules of Betting (s 30).
- Deposit the Gaming and Wagering Commission Act 1987, for social gambling and
  permitted gaming (s 23(1)(e)).
- Settle the interstate-app question in finding 2 with authority (case law or the
  regulator's published position). Until then the encoding's most common modern
  case comes out `uncertain`.
- Check the uncommenced TAB (Disposal) Act 2019 provisions, and whether a wagering
  licence has been granted, before relying on findings 3 and 7.
- An independent test pass and the two human gates.
