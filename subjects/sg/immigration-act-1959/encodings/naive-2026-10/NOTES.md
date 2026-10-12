# Immigration Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 31
of 2023, Act 5 of 2025 and Act 16 of 2026).

**Checks:** three case files, 190 assertions satisfied, 0 errors, 0 warnings (90 + 59 + 41).

## Why this Act, and why scoped

**48 of the 527 Singapore Acts** deposited here cite it, mostly for s 2
definitions (25) and s 3 (10). This row takes who may enter and stay, how status
is lost, and the offences a member of the public or an employer is most likely
to meet: overstaying, harbouring, employing, marriages of convenience.

**Not encoded:** visas, arrival procedure and carriers' passenger information,
removal and detention, information sharing, cross-border railway pre-clearance,
and most enforcement powers.

## What the Act turns out to say

### 1. HIV infection alone makes a foreigner a prohibited immigrant

s 8(3)(ba): "any person suffering from Acquired Immune Deficiency Syndrome or
infected with the Human Immunodeficiency Virus" is in a prohibited class. The
text has no qualification. A prohibited immigrant may enter only with a special
pass under the regulations (s 8(2)(b)); whatever administrative practice is, the
statute still lists HIV. Asserted.

### 2. Prohibition is inherited

s 8(3)(n): "the family and dependants of a prohibited immigrant" are themselves a
prohibited class. No class of their own is needed. Asserted.

### 3. Disbelief in government is a ground of exclusion

s 8(3)(i): a person "who disbelieves in or is opposed to established government"
is a prohibited immigrant. The class reaches belief, not action, and s 14(3) then
**requires** the Controller to cancel any permit the person holds. Asserted.

### 4. Overstay day 91 is mandatory prison and caning

s 15(3): overstaying up to 90 days is a fine of up to $4,000 or up to six months.
From day 91 the person "**shall** ... be punished with imprisonment ... and **shall
also** be punished with caning with not less than 3 strokes". The same structure
applies to a former citizen who stays more than 24 hours (s 11A(6)), and unlawful
entry carries mandatory imprisonment and caning from the first day (s 6(3)(a)).
Asserted at days 90 and 91.

### 5. A landlord needs all three checks to escape the negligence charge

s 57(1)(d) makes harbouring an offence if knowing, reckless, or negligent. Giving
shelter raises a presumption of recklessness or negligence (s 57(7)), and a pass
is no defence without due diligence (s 57(7A)). Due diligence is any **two** of
three checks against the recklessness charge, but **all three** against
negligence (s 57(7C)): inspecting the pass, matching it to the passport, and
checking validity with the Controller or the named employer. A landlord who did
the first two escapes the six-month presumptive minimum but is still liable for
negligent harbouring. Asserted.

### 6. The marriage-broker is guilty where the couple are not

s 57C(1): a party to a marriage commits the offence only if they knew of the
immigration purpose **and** gratification passed. s 57C(2): a person who
**arranges** such a marriage with the intention of giving an immigration
advantage commits the same 10-year offence with **no gratification element**. An
unpaid introduction for a pass is an offence by the introducer and not by the
couple. Asserted.

### 7. Section 12 endorses a wife, not a husband

s 12: the Controller may endorse "the name or names of the **wife** or child" on a
permit, pass or certificate. A female permit-holder has no s 12 route to endorse a
husband, and s 6(1)(b) lets only an endorsed person enter on someone else's permit.
Asserted.

### 8. The only reviewable ground is procedure, and the main procedural right is removed

s 39A excludes all judicial review, including habeas corpus ("an Order for Review of
Detention") and "any other suit or action", "except in regard to ... compliance with
any procedural requirement". s 39B then says no one need be given an opportunity
to be heard. Asserted.

### 9. Permanent residents abroad lose their status automatically

s 11(1A): a PR outside Singapore without a valid re-entry permit **must** apply for
one within a prescribed period (in regulations, not retrieved). s 14A: if they do
not, or are refused, the entry permit is **cancelled automatically**. The duty
continues even if they come back on a visit pass (s 11(1C)). Asserted.

### 10. Smaller things worth recording

- **s 8(3)(d):** an imprisonment sentence in **any** country, unpardoned, makes a
  person excludable if the Controller deems them undesirable; a fine does not.
- **s 9(1A):** an entry ban made on economic, social or educational grounds does not
  catch someone abroad who already holds a re-entry permit or pass; one made for
  security or health does. Citizens are never caught (s 9(2)).
- **s 9AA:** the person subject to a no-boarding directive need not be told
  (s 9AA(6)); the carrier's offence is strict liability.
- **s 57(1)(ka):** giving false information for a pass, even unknowingly, is a strict
  liability offence ($4,000); knowingly, $8,000 or 12 months.
- **s 57(8):** an immigration offender found at any non-residential premises makes
  the occupier presumptively a knowing employer.
- **s 57A:** a construction principal contractor faces a minimum $15,000 fine **per
  offender found** on site, $30,000 per offender on a second conviction.
- **s 57(1A):** employing more than five offenders at once adds caning.

## What would need doing before this is worth anything

- **Retrieve the Immigration Regulations**: the PR re-entry period, the passes for
  prohibited immigrants, and the compoundable offences are there.
- **No case law was searched.** Sentencing practice on s 15 and s 57 is extensive.
- Finding 1 should be read with current administrative practice on HIV, which this
  row does not have.

## A citizen's spouse: passes and permanent residence (added 12 October 2026 for REQ-0286)

Module `imm-spouse-passes-and-pr.l4`, cases `imm-cases-spouse-passes-and-pr.l4` (41 assertions; the first six are the
requirement's own question). The question (Haziq scenario, event h033) asks on what basis a citizen's Malaysian spouse is
given a long-term visit pass, and on what basis and after how long she may be granted permanent residence. "She" is read
as the Malaysian spouse.

### 1. The Act does not answer the first half: the long-term visit pass is not in it

The Act never mentions a long-term visit pass, a spouse's pass or any class of pass. s 2 defines "pass" only as "a pass
issued under the regulations entitling the holder thereof to remain, or enter and remain, temporarily in Singapore", and
s 55(1)(c) leaves "passes (including classes of passes)", their issue, validity, conditions and cancellation to
regulations. The basis of an LTVP is therefore the Immigration Regulations (not retrieved) and ICA's practice under them.
The ledger's assumption ("LTVP as a citizen's spouse") may be right as practice, but nothing in the deposit says so.
Asserted only as far as the Act goes: the instrument is the s 55 regulations, and a pass is never permanent.

### 2. Permanent residence: an entry permit the Controller *may* issue, with no period and no spousal criterion

s 10(1): "A non-citizen who wishes to be a permanent resident of Singapore must apply for an entry permit in such form and
manner as the Controller requires." s 10(2): on that application "and on payment of the prescribed fee, the Controller
**may** issue" it. s 2: a "permanent resident of Singapore" is "the holder of a valid entry permit". The grant is
discretionary in every case and of right in none. Asserted: the Malaysian spouse and an unmarried foreigner on the same
facts get the same footing (`discretionary`), and twenty years of marriage does not make it `as of right`.

### 3. "After how long": the Act states no period

No minimum residence, marriage length or other qualifying time appears in s 10 or anywhere else in the Act. The encoding
records the Act's minimum as 0 years; that is a statement about the statute, not about how long ICA in fact takes or
expects. The ledger's "published framework" is policy, not law, and is not in the deposit.

### 4. What else the Act does say about the spouse

- **Entry (ss 6(1)(c), 7(1)):** the citizen needs no permit or pass; the spouse must hold her own valid pass (or permit).
- **Prohibited immigrants (s 8):** marriage exempts the spouse from nothing. Class (a) catches a person unable to show
  means of support for self and dependants or definite employment, or likely to become a charge on the public. A
  prohibited immigrant may enter only on a pass issuable to prohibited immigrants under the regulations (s 8(2)(b)). If
  she held an entry permit while a prohibited immigrant, s 14(3) says the Controller "must cancel" it (inference: so it
  would not be issued).
- **Visas (ss 9B, 9C, 10(2)):** a non-citizen needs a Singapore visa to travel unless her passport is from a country the
  Minister has approved. Whether Malaysia is approved is not in the Act. If a visa is needed, the Controller **must**
  grant one with the entry permit, valid until the permit is cancelled. A visa is not permission to enter (s 9C(1)).
- **Conditions (s 10(3) to (4A)):** the Controller may impose conditions on the entry permit at issue and vary them at any
  time, "whether or not" entitled to cancel; notice must be given individually, or for a class by publication on a
  prescribed website or in the Gazette where individual notice is impracticable.
- **s 12 does not help:** it endorses a *wife* on the holder's own permit, pass or certificate. A citizen husband
  ordinarily holds none, and a citizen wife cannot endorse a husband (finding 7 above).
- **s 57C(6):** a pass and an entry permit for the spouse (or her child or parent) are each an "immigration advantage",
  so a marriage made to obtain one is within the marriage-of-convenience offence (finding 6 above).
- **Cancellation of the pass** is by the regulations (s 55(1)(c)(i)), not s 14, which speaks of permits and certificates.

### 5. What a full answer needs

The Immigration Regulations (the long-term visit pass class, its eligibility, conditions and cancellation, and the
prescribed fees for passes and entry permits); the Minister's list of visa-exempt countries under s 9B(2); and ICA's
published criteria for spouses of citizens (LTVP and PR), which are policy. No case law was searched; s 39A in any event
excludes judicial review except on procedure.
