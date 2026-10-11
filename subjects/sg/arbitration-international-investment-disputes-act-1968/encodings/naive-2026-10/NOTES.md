# Arbitration (International Investment Disputes) Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text, following the `writing-l4-rules`
conventions as the example rows show them (the skill itself was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 April 2022), as deposited at `../../registers/source-bundle/AIIDA1968.txt`. The deposit
says it "incorporates all amendments up to and including 1 December 2021 and comes into
operation on 31 December 2021". The latest amendment annotated in the body is [Act 25 of
2021 wef 01/04/2022], on ss 5 and 6.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0143** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The person it applies to is an investor or a State holding, or resisting, an award of
the International Centre for Settlement of Investment Disputes (ICSID). The Act has ten
sections; nearly all the substance is in the Convention set out in the Schedule. This row
takes registration and enforcement (ss 2(2), 3, 4, 5), the exclusion of the Arbitration
Act 2001 (s 8), the immunities and tax exemptions given the force of law (s 9), and, from
the Convention, who may claim (Articles 25 to 27), the tribunal's size and nationality
rules (Articles 37 to 39), the post-award deadlines and stays (Articles 49 to 52),
finality (Article 53) and conciliation costs (Article 61(1)).

Not encoded: rule-making (s 6; the Rules of Court were not retrieved), the Consolidated
Fund (s 7), amending the Schedule (s 10), the Centre's organs and panels (Articles 1 to
17), conciliation procedure (Articles 28 to 35), the conduct of the arbitration
(Articles 40 to 48), replacement and disqualification (Articles 56 to 58), fees (Articles
59, 60, 61(2)), place of proceedings and the final clauses (Articles 62 to 75). The
interest rate on a registered award is not in the Act.

## What the Act turns out to say

### 1. Only Articles 18 to 24 are given the force of law; the rest of the Convention is just set out

s 9(1) gives "the force of law" to Articles 18, 19, 20, 21(a) (with Article 22 as it
applies to 21(a)), 23(1) and 24, and to nothing else. The Convention as a whole is
defined by reference to the Schedule (s 2(1)) and is used by ss 4 to 6 for what an award
is, its certification and stays, but the Act has no provision giving Articles 25 to 75
force of law. The rules in this row taken from those Articles encode the Convention's text;
that a Singapore court applies them as domestic law in their own right is not something
the Act says. Even within s 9, Article 21(b) (immigration, alien registration and
national-service privileges) and Article 23(2) (official communications) are left out.
Not asserted (a structural point).

### 2. Registration is a right, for the unpaid balance plus costs, and nothing if fully paid

s 4(1): any person seeking recognition or enforcement "shall be entitled" to registration in
the General Division of the High Court, subject to proving prescribed matters. s 4(2) adds
"the reasonable costs of and incidental to registration"; s 4(3) registers only the balance
if partly paid and refuses registration if wholly paid. On a 1,000,000 award with 400,000
paid and 5,000 costs, the registered sum is 605,000. Asserted.

### 3. Only the money is enforceable as a judgment, and the Government is protected

s 5 gives a registered award the force of a High Court judgment "as respects the pecuniary
obligations which it imposes": proceedings may be taken on it, the registered sum "shall
carry interest", and the court has the same control. A non-money order (restoring
property, say) gets no such effect. s 3 binds the Government, "but not so as to make an
award enforceable against the Government in a manner in which a judgment would not be
enforceable against the Government"; Article 55 likewise preserves State immunity from
execution. Asserted.

### 4. The Arbitration Act 2001 does not apply, and there is no appeal

s 8 excludes the Arbitration Act 2001 from proceedings "pursuant to the Convention", so
there is no setting aside under that Act. Article 53(1): the award "shall not be subject to
any appeal or to any other remedy except those provided for in this Convention" —
interpretation (Article 50), revision (Article 51) and annulment (Article 52). Asserted.

### 5. The deadlines run from despatch of certified copies, and a supplementary decision restarts two of them

s 2(2) and Article 49(1): the award is rendered on the date certified copies are despatched.
A supplementary decision or rectification must be requested within 45 days (Article 49(2)),
and if one is made the revision and annulment periods run from that decision. Revision:
within 90 days of discovering a decisive fact, and within 3 years, if the fact was unknown
to the tribunal and the applicant and the ignorance not negligent (Article 51). Annulment:
within 120 days, on five grounds only — improper constitution, manifest excess of powers,
corruption, serious departure from a fundamental rule of procedure, no reasons. An error of
law is not a ground. For corruption the 120 days run from discovery, capped at 3 years, so
an application 500 days after the award can be in time. Asserted.

### 6. Asking for a stay gets one automatically, except on interpretation

Articles 51(4) and 52(5): if the applicant for revision or annulment requests a stay in the
application, "enforcement shall be stayed provisionally" until the tribunal or committee
rules. Article 50(2) on interpretation gives only a discretion. Asserted.

### 7. A dual national of the host State cannot claim; a local company can, by agreement

Article 25(2)(a): an individual must hold another Contracting State's nationality on both
the consent and the registration dates, and must not hold the host State's nationality on
either. Article 25(2)(b): a company needs foreign nationality only at consent, and a host
State company counts if, "because of foreign control", the parties agreed to treat it as
foreign. Once given, consent cannot be withdrawn unilaterally (Article 25(1)); consent is
exclusive of other remedies unless stated (Article 26); the investor's home State may not
take up the claim unless the host State fails to comply with the award, informal settlement
exchanges aside (Article 27). Asserted.

### 8. The arbitrators must mostly be neutrals, unless the parties picked every one

Article 37(2)(b): three arbitrators by default. Article 38: after 90 days (or the agreed
period) without a tribunal, the Chairman appoints on request, and not a national of either
State. Article 39: a majority must be nationals of neither State, unless the sole arbitrator
or each member was appointed by agreement. Asserted.

### 9. Arbitrators sitting in Singapore are not taxed here for that reason alone

Article 24(3), which has the force of law: no tax on arbitrators' or conciliators' fees "if
the sole jurisdictional basis for such tax is the location of the Centre or the place where
such proceedings are conducted or the place where such fees or allowances are paid".
Secretariat salaries are untaxed except for local nationals (Article 24(2)). The Centre's
own exemption (Article 24(1)) is cut back by s 9(2): no duty-free import for unrestricted
resale, and no relief from taxes built into prices or charges for services. Persons
appearing in proceedings, including counsel and witnesses, share the arbitrators' immunity
for acts in their functions unless the Centre waives it (Articles 21(a), 22); a certified
waiver statement is conclusive (s 9(3)). Asserted.

## What would need doing before this is worth anything

- The Rules of Court made under s 6 (notice, proof, service, stay) were not retrieved;
  registration practice depends on them.
- No Singapore case on registration or on the status of the unenacted Articles was read.
- The 3-year limits are modelled as a yes/no fact, not counted from dates.
- Interest on a registered award (s 5(b)) runs at a rate set elsewhere, not encoded.
