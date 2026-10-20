# Interactive Gambling Act 2001 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

**Edition:** Compilation No. 24, compilation date 14 October 2024, includes amendments to Act No. 38, 2024 (register id
C2024C00646), as deposited at `../../registers/source-bundle/C2004A00851.txt` (retrieved 13 October 2026).
The Interactive Gambling (National Self-exclusion Register) Rules 2022 are **not deposited**, nor are the Minister's
determinations of conditions (ss 8AA(2), 8A(2), (4), (6), 8B(2), 8BA(2), 8BB(2), 15C(4A)(d)) or the regulations under
ss 8C, 8D(1A) and 69A. Whatever they set is an input: whether the conditions for an exclusion are met, whether the
identification procedure has been carried out, whether a support service is listed. The period within which the
operator must register me is set by the Rules; the encoding says so and does not compute it.

**Checks:** one module (`iga-gambler.l4`, 24 exported questions), one case file (`iga-cases-gambler.l4`). 68 assertions
satisfied, 0 errors, 0 warnings, with the stable `l4` from VS Code extension 1.6.98.

There was no earlier encoding of this Act.

## Seat

**The gambler**: the individual in Australia who buys lottery tickets, bets or plays online, and who may put themselves
on the National Self-exclusion Register (BetStop). Almost every operative provision addresses a provider ("A person
commits an offence if ... the person intentionally provides ..."; "A licensed interactive wagering service provider must
not ..."), or the Register operator. The encoding asks what each means for the gambler: whether the service may be
offered to me, whether I commit any offence (I do not), what an app may take from me, whether and for how long I can be
registered, how I come off, and what the betting companies must stop doing and pay me once I am on.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The Rules and the determinations are not
  deposited, so every condition or procedure they supply is an input (see Edition).
- **The actors the text names.** Followed: the provider, the licensed interactive wagering service provider, the
  Register operator, the nominated support person, the registered individual.
- **A judgment handed to someone else is answered conditionally.** Followed: the Minister's or the regulations'
  conditions for each exclusion; the identification procedure; the s 15D small telephone bookmaker test (turnover under
  $30 million, racecourse presence), asked as one fact; "the Register operator is aware" (s 61JM).
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed for gambling service, wagering
  service, prohibited and regulated interactive gambling service, telephone betting, excluded wagering, gaming and lottery
  services, place-based betting, trade promotion, in-play betting, illegal interactive gambling service and licensed
  interactive wagering service. Borrowed terms asked as facts: carriage, broadcasting and datacasting services; a State
  or Territory licence; ordinarily resident; statutory declaration.
- **One case is the text's natural unit.** Followed: one service, one application, one registration, one account.
  Simplifications: s 8BA(1)(b)(iii) (equipment not shared with another provider) is taken as met; "provided over the
  internet, a phone, broadcasting or datacasting" is one fact for the five limbs of s 5(1)(b).
- **The Act's own terms, each with a plain gloss.** Followed in comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed. ACMA complaints and investigations, industry codes, the Register
  operator's appointment, information handling, the levy and the reviews are out.
- **Periods.** The stable `l4` has no date arithmetic the encoding could rely on, so months and days are counted by the
  caller (months since registration came into force; days since the application, that day being day 0).

## The lives

- **jake k080** (1 September 2045, 39): Lotto on Saturdays, the casino on paydays, then betting apps. *Is it lawful to
  provide this gambling service to me?* Lotto bought online from the licensed State lottery: lawful (excluded lottery
  service, regulated, licensed). The casino floor: outside the Act (not provided over a carriage service; the Casino
  Control Act 1984 is the WA law). Pre-match AFL and racing bets on a licensed app: lawful. In-play bets on the same app
  online: prohibited. An offshore online casino: prohibited. *Do I commit an offence?* No. *May the app take my credit card
  or crypto, or give me credit?* No; a debit card yes.
- **jake k081** (8 May 2046): Chloe finds no family exclusion order; Jake registers on BetStop and self-excludes from the
  casino. *Can my sister put me on the Register?* No, only I can apply (s 61JA(1)); she can be my nominated support person
  with her consent. *Can I be registered for 12 months?* Yes. *What does it cover?* Licensed betting apps and phone
  bookmakers; not Lotto, the casino or gaming machines. *What must the apps do?* Stop taking my bets, stop marketing to me,
  close my account and pay out the balance (after any running bets resolve), and never reopen it. *When does it end, and
  can I come off early?* At 12 months, with 14 days' warning to me and Chloe; I may apply to come off only after 3 months,
  in writing, with a statutory declaration of counselling. The casino self-exclusion is Crown's program, not this Act.

## Why this scope

The two events turn on ss 15 and 15AA (what may be offered) and Part 7B (the plan entry notes that the scenario facts
cite "Part 7A", which is the advertising prohibition; BetStop is Part 7B). To answer "which online gambling is lawful"
the s 5(3) exclusions and their definitions (ss 8AA-8E, 10B) must be worked out, so they are in. Part 2B is in because
k080 asks what an app may offer, and credit and credit cards are what the Act says it may not. The rest of Part 7B that
reaches the gambler directly (duration, removal, marketing, accounts, inducements) is in. Part 2A, Parts 3-6, Part 7A and
the information, levy and review parts of Part 7B are out.

## What the Act turns out to say

1. **The player commits no offence.** Every offence and civil penalty in ss 15, 15AA, 15C and Part 7B is laid on the
   person who provides the service (or, elsewhere, on internet service providers and advertisers). Using a prohibited
   offshore casino is not an offence by the customer under this Act. Asserted.
2. **"Lawful" means licensed and of an excluded kind.** A gambling service provided as a business over the internet, a
   phone, broadcasting or datacasting is prohibited unless it falls in a s 5(3) exclusion. The excluded kinds (telephone
   betting, racing, pre-match sport and other-event wagering, licensed venue gaming and betting, non-instant lotteries)
   are "regulated interactive gambling services" (s 8E), and those may be provided only with a State or Territory licence
   (s 15AA). Asserted.
3. **In-play online betting is prohibited, but by live phone call it is regulated.** s 8A(3)(b) and (5)(b) exclude in-play
   betting from excluded wagering, but a telephone betting service (wholly by live voice call, s 8AA) is excluded in its
   own right. Asserted.
4. **Online casinos, pokies and poker, and online instant scratchies, are prohibited.** A game of chance is excluded only
   on equipment at a licensed venue (s 8B), and s 8D(2) takes electronic scratch and instant lotteries out of the
   excluded lottery service. Asserted.
5. **Betting apps may not take credit cards, credit-card-funded wallets or digital currency, nor give credit** (s 15C).
   The s 15D exception is for credit only, and only for small telephone bookmakers dealing wholly by voice. Asserted.
6. **BetStop covers only licensed wagering.** The Register reaches a "licensed interactive wagering service" (s 61GB):
   regulated, wagering, Australian customer, licensed. Online lotteries, venue gaming and the casino floor are outside
   it. Asserted.
7. **Only the gambler can register; family cannot.** s 61JA(1): "An individual may apply ... for the individual to be
   registered". A family member can be one of up to five nominated support persons, with consent. Asserted.
8. **The period: at least 3 whole months, whole years, or life.** No minimum number of years is stated, and the Act sets
   no minimum age (both inferences from silence; the Rules may add requirements). Asserted for months, life and the
   five-person limit.
9. **A life registration can be ended.** s 61JF(6) makes a life registration subject to s 61JK, so it too can be removed on
   my application, after the first 3 months, in writing, with a statutory declaration of counselling within the last 3
   months. Removal takes effect at the start of the eighth day unless I withdraw. Asserted.
10. **Second registrations have no 3-month lock.** s 61JK(2) bars an application in the first 3 months "unless the
    individual was previously registered before that time". Asserted.
11. **Closing my account: I am paid the balance less deductible debts, never less than nothing; it is never reopened.**
    ss 61MB, 61MC; a pending bet postpones closure until it is resolved; s 61MB(9) keeps any debt recoverable. Asserted.
12. **Marketing.** Once registered I may not be sent electronic messages, telemarketing calls or direct marketing
    material, and my details may not be passed on for marketing by a provider I have or had an account with. Material
    that only promotes the provider is caught only if sent by post or a like service (s 61LC(2)(b)). Asserted for
    electronic messages and for material that only promotes the provider.
13. **s 69A only permits regulations** making agreements with illegal services void and barring suits to recover
    winnings; none is deposited, so whether they exist is not answered. Asserted as what s 69A permits.

## What would need doing before this is worth anything

- Deposit the Interactive Gambling (National Self-exclusion Register) Rules 2022: the registration period, the manner
  of applying, the identification procedure, any further eligibility, and the listed support services.
- Deposit the Minister's determinations of conditions and of sporting events (ss 8A, 8AA, 10A, 15C(4A)(d)) and the
  regulations under ss 8C, 8D(1A) and 69A.
- Encode the providers' defences (ss 15(3), 15AA(5), 15C(5), (5A); Part 7B due diligence), which may matter to a gambler
  asking why a provider was not penalised.
- The WA side of k080 and k081 (Casino Control Act 1984 s 25, Betting Control Act 1954) is not this Act.
- No ACMA decision, case law or BetStop guidance was read.
