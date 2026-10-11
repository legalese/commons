# Diplomatic and Consular Relations Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/DCRA2005.txt`. The deposit says it "incorporates
all amendments up to and including 1 December 2021 and comes into operation on
31 December 2021"; the retrieval metadata records it as the current version as at
1 October 2026. The only amendment annotated in the text is [27/2014] on s 5(9);
the Legislative History names Act 27 of 2014 (Family Justice Act 2014, s 55, in
force 1 January 2015) as the last amending Act.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0141** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is eight sections that give selected Articles of the two Vienna
Conventions (set out in full in the First and Second Schedules) the force of law.
An ordinary person or business meets it when the other side — a tenant, a debtor,
a driver in an accident, an employer of a domestic worker, the representative of
a foreign heir — belongs to a foreign embassy or consulate. This row takes:
who is immune from suit and prosecution (VCDR Arts 31, 37, 38; VCCR Arts 43,
57(2), 58(2), 71), waiver and enforcement (VCDR Arts 31(3), 32; VCCR Art 45;
ss 3(3), 4(5)), arrest (VCDR Art 29; VCCR Art 41; s 4(2)(b)), giving evidence
(VCDR Art 31(2); VCCR Art 44), taxes (VCDR Arts 34, 37; VCCR Arts 49, 66), social
security for a diplomat's private servant (VCDR Art 33), when immunity ends
(VCDR Art 39(2); VCCR Art 53), entry to premises (VCDR Arts 22, 30; VCCR Art
31(2); ss 3(2)(a), 4(2)(a)), a consular officer's powers over a deceased
national's estate (s 5) and the Minister's certificate (s 7).

Not encoded: reciprocity orders (s 6), regulations (s 8), archives, bags and
couriers, customs and baggage, premises taxes, personal services, third-State
transit, estate duty on a deceased member's movables, and the family of
administrative and technical staff as a separate role. The Act does not define
"permanently resident"; it is taken as a given fact.

## What the Act turns out to say

### 1. A diplomat's spouse who is a Singapore permanent resident has full immunity

VCDR Art 37(1) gives the household family of a diplomatic agent the privileges of
Arts 29 to 36 "if they are not nationals of the receiving State" — and s 3(2)(b)
makes "national" mean a citizen of Singapore. Every other limb (Art 37(2), (3),
(4), Art 38) excludes nationals **or permanent residents**. On the text, a PR
spouse of an ambassador is immune from prosecution; a PR embassy clerk is not.
Asserted.

### 2. A diplomat is immune for a private car accident; a consul is not even for an official one

A diplomatic agent's civil immunity has only three exceptions — private immovable
property, private succession, and private professional or commercial activity
(VCDR Art 31(1)) — so an unpaid private debt or a private car accident is covered.
A consul is immune only for "acts performed in the exercise of consular
functions" (VCCR Art 43(1)), and even then not in a civil action on a contract he
did not make as agent of the sending State, or a third-party claim for a
vehicle, vessel or aircraft accident (Art 43(2)). A consular employee who carries
on a private gainful occupation loses the immunity altogether (Art 57(2)(a), read
with s 4(6)). Administrative and technical staff of a mission are immune from
prosecution but not from civil suit for acts outside their duties (Art 37(2)).
Asserted.

### 3. A consul can be arrested for a grave crime; a diplomat never

VCDR Art 29: a diplomatic agent "shall not be liable to any form of arrest or
detention". VCCR Art 41(1): a consular officer may be arrested or detained pending
trial for "a grave crime and pursuant to a decision by the competent judicial
authority", and otherwise only "in execution of a judicial decision of final
effect". s 4(2)(b) fixes a grave crime as one punishable with imprisonment that
may extend to **5 years** or more severely. Asserted for a career consul at 3 and
7 years, with and without a judicial decision, and after final judgment. Art 58(2)
does not apply Art 41 to honorary consular officers (encoded, not asserted).

### 4. A Singapore-citizen honorary consul gets very little

Art 58(2) applies to honorary consular officers only Arts 42, 43, 44(3), 45 and 53
and para 1 of Art 55; Art 71(1) confines a local consular officer to
jurisdictional immunity and personal inviolability for official acts and the Art
44(3) privilege. So such a consul can be made to testify about private matters,
and is not exempt from tax on the consular pay (the encoding reads Art 71's
"only" as displacing Art 66 for a local — an inference). The family of an honorary officer gets nothing (Art
58(3)). Asserted (evidence and tax).

### 5. Police and any statutory inspector need the ambassador's consent — fire or not

s 3(2)(a) and s 4(2)(a) extend "agents" and "authorities" of the receiving State
to "any police officer and any person exercising a power of entry to any premises
under any written law". VCDR Arts 22(1) and 30(1): no entry to mission premises or
a diplomat's private residence without the head of mission's consent, with no
emergency exception. VCCR Art 31(2) protects only the part of consular premises
used exclusively for consular work, and consent "may ... be assumed in case of
fire or other disaster". Art 58(1) does not apply Art 31 to an honorary consular
post. Asserted.

### 6. Waiver must be express, and enforcement needs a second waiver

VCDR Art 32 and VCCR Art 45: waiver by the sending State "must always be express"
(and, for consular staff, communicated in writing); a waiver by the head of
mission counts as the State's (ss 3(3), 4(5)). Starting proceedings bars immunity
against a directly connected counter-claim. Waiver for civil proceedings does not
waive immunity from execution of the judgment. Asserted.

### 7. A diplomat employing a local or uncovered domestic worker carries the employer's social security duties

VCDR Art 33(2), (3): the exemption reaches only a private servant in the sole
employ of a diplomatic agent who is neither a national nor a permanent resident
and is covered by the sending or a third State's scheme; otherwise the diplomat
"shall observe the obligations which the social security provisions of the
receiving State impose upon employers". The Act does not name a Singapore scheme;
that the CPF Act is the relevant one is an inference. Private servants who are not
local are exempt from tax on their pay (Art 37(4)). Asserted.

### 8. The Act enacts the Conventions selectively

s 3(1) gives force to VCDR Arts 1, 22, 23, 24 and 27 to 40 only — not Art 41 (the
duty to respect local laws), nor Arts 25 and 26. s 4(1) omits VCCR Art 42
(notification of a consular officer's arrest), Arts 46 and 47, para 3 of Art 31,
Art 59 and Art 63 — although Art 71(1), which is enacted, refers to "the
obligation laid down in Article 42". What the omissions mean in practice (the
Conventions may still bind Singapore internationally) is not something the text
says. Not asserted.

### 9. Consular officers can take a grant for an absent heir, and the Minister's certificate ends the argument

s 5(1): for a State named by order under s 5(12), where a non-resident national is
executor or entitled to a grant and has not applied (personally or by attorney),
"the court must make to the consular officer such grant", subject to postponement
(s 5(2)). Under s 5(4) the consular officer can receive money due to the
non-resident and give a valid discharge, but no one need pay him who knows that
someone in Singapore is expressly authorised to receive it (s 5(5)). s 7: a
certificate by or on behalf of the Minister "is conclusive evidence" on entitlement
to any privilege or immunity. Asserted.

## What would need doing before this is worth anything

- No s 5(12) orders, s 6 reciprocity orders or s 8 regulations were retrieved; any
  of them can change who has what.
- "Permanently resident", "member of the family forming part of the household" and
  "official functions" are taken as given facts; case law on each was not searched.
- Several readings are inferences and labelled so in the `.l4`: that a local
  consular officer keeps the Art 43(2) carve-outs, that a person immune for an act
  cannot be arrested for it, that a local diplomatic agent may decline evidence
  only on official acts, and that Art 71 displaces Art 66 for a local honorary
  consul.
- Family of administrative and technical staff, honorary consular post premises
  taxes, customs, and estate duty on movables are not encoded.
