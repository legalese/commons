# International Development Association Act 2002 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else (the skill was not loaded in this session, so the
conventions of the finished naive rows were followed). No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/IDAA2002.txt`. The cover says it incorporates "all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021; the deposit's footer reads "Informal Consolidation – version in
force from 23/12/2022". The latest amendment annotated in the body is
`[Act 34 of 2022 wef 23/12/2022]`, on s 4(1) to (3); s 4(1) also carries
`[10/2004]`. The Legislative History (not part of the Act) lists the International
Development Association (Amendment) Act 2022 (Act 34 of 2022, in force 23 December
2022) as its latest entry. The arrangement of sections and the body agree.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0177** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is short: ten sections, mostly about Government finance. What reaches a
person is in the Schedule, Article VIII of the Agreement, which s 8(1) gives the
force of law "Despite anything to the contrary in any other written law". This row
takes the subscription limits (s 4(2), (3)), the notes the Minister may issue in
place of payment (s 5(1)), s 9, and Article VIII ss 3, 4, 8 and 9 with the s 8(2)
limits. Not encoded: acceptance (s 3), the Consolidated Fund charges (ss 4(1), 5(2),
6(2), 7), the loan power (s 6(1)), ss 8(3) and 10, and Article VIII ss 1, 2, 5, 6, 7
and 10 (quoted or described in comments only).

## What the Act turns out to say

### 1. Anyone except a member can sue the Association, on any claim, where it has a presence

Article VIII s 3 is not an immunity with exceptions. It says actions may be brought
"only in a court of competent jurisdiction in the territories of a member in which
the Association has an office, has appointed an agent for the purpose of accepting
service or notice of process, or has issued or guaranteed securities". It sets no
limit on the kind of claim. A supplier owed the price of goods, an employee claiming
wages, or someone hurt on its premises may sue, as may a bondholder, if the venue
condition is met. (The Asian Development Bank Act 1966 row's Schedule, by contrast,
confines suits to claims on that Bank's borrowing, guarantees and securities
dealings.) Whether the Association has an office or agent in Singapore is not in the
deposit; it is a parameter. Asserted.

### 2. A member, or anyone acting for or deriving a claim from one, can never sue

Article VIII s 3: "No actions shall, however, be brought by members or persons
acting for or deriving claims from members." The Schedule as deposited carries no
general waiver article, so nothing in the deposit lifts this bar. Asserted.

### 3. A Singapore citizen working for the Association pays tax on the salary

Article VIII s 9(b) bars tax on salaries paid to Executive Directors, Alternates,
officials or employees "who are not local citizens, local subjects, or other local
nationals". A local national gets no exemption at all, with no declaration by the
member needed. Governors, named in s 8, are not named in s 9(b). Asserted ("officials"
in s 9(b) is read to include the "officers" of s 8, an inference).

### 4. The s 8(2) read-down has two limbs, not three

Article VIII s 9(a) makes the Association "immune from all taxation and from all
customs duties" and from "liability for the collection or payment of any tax or
duty". s 8(2) says this is not to be construed as (a) entitling it to import goods
duty-free "without any restriction on their subsequent sale in Singapore" or (b)
exempting it from taxes "which are no more than charges for services rendered". It
does not exclude taxes forming part of the price of goods sold. On the words, such a
tax falls within "all taxation" and the encoding treats it as exempt; whether the
immunity reaches a tax that is legally the seller's is not settled by the text
(inference). Asserted.

### 5. An Association-guaranteed bond is less protected from tax than an Association-issued one

Article VIII s 9(c) forbids a tax on a security the Association **issues** whose
sole jurisdictional basis is the place or currency of issue or payment, or the
location of an Association office. s 9(d), for a security it **guarantees**, names
only the office location. Either is barred if the tax discriminates solely because
of the Association. Asserted.

### 6. Officials are immune only for official acts, and only until the Association waives

Article VIII s 8(i): immunity "with respect to acts performed by them in their
official capacity except when the Association waives this immunity". The
immigration, alien registration and national service immunities in (ii) go only to
those "not being local nationals". Consultants and experts are not named. Asserted.

### 7. Before final judgment the property cannot be touched; by the State, never

Article VIII s 3 bars "seizure, attachment or execution before the delivery of final
judgment"; s 4 bars "search, requisition, confiscation, expropriation or any other
form of seizure by executive or legislative action". Asserted.

### 8. The Government's stake is capped at US$1 million, and each top-up needs its own resolution

s 4(2): the total subscription "must not exceed the sum of one million United States
dollars unless increased with the approval of Parliament signified by resolution".
s 4(3), annotated `[Act 34 of 2022 wef 23/12/2022]`: any additional subscription on any occasion "must be
authorised by, and must not exceed the maximum amount specified in, a resolution of
Parliament for that occasion". The two are encoded as separate tests (inference on
how "Subject to subsection (3)" joins them). s 5(1) lets the Minister issue notes in
place of payment only if they are non-interest bearing, non-negotiable, payable at
par on demand, acceptable to the Association, and the President concurs. The
Companies Act 1967 does not apply to the Association or its securities (s 9).
Asserted.

## What would need doing before this is worth anything

- The Agreement beyond Article VIII, and the membership resolution, were not
  deposited or read; whether the Agreement has a waiver provision elsewhere is
  unknown.
- Whether the Association has an office or agent in Singapore, or has issued or
  guaranteed securities here, was not checked.
- Whether "all taxation" reaches GST or other taxes passed on in the price of goods
  sold to the Association was not resolved.
- Any regulations under s 10, Schedule amendments under s 8(3), or resolutions of
  Parliament under s 4 were not searched; no case law was searched.
