# International Organisations (Immunities and Privileges) Act 1948 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
6/1/2025"), deposited at `../../registers/source-bundle/IOIPA1948.txt`. The latest
amendment annotated is S 4/2025 wef 06/01/2025, which added the OECD to the First
Schedule.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0142** in `subjects/sg/requirements.jsonl`. That is Tier 2
of the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet. For an ordinary person or business the practical question is
"can I sue this organisation, or this person who works for it?"

The Act is short, with six sections and two Schedules, so it is encoded nearly whole:
ss 2 to 5 and both Schedules. Left out: s 1 (short title), s 6 (the Minister's power to
amend the First Schedule), the evidential rule in ss 2(4) and 3(2) (a Gazette list
conclusively proves who was on it), s 4(a) (reading "governing body" for the UN), and
everything the Act borrows from the law of diplomatic immunity without stating it.

## What the Act turns out to say

### 1. Being named in the Act gives an organisation nothing by itself

The First Schedule names the International Tribunal for the Law of the Sea, the Bank for
International Settlements and (since S 4/2025) the OECD. But s 2(1) only says that s 2
"applies to" them. Immunities come from an order under s 2(2), which "may" provide
them "to such extent as may be specified in the order". Whether a given organisation
can be sued in Singapore therefore depends on an order this row did not retrieve.
Asserted: OECD with no order has no immunity.

### 2. A programme officer can be sued over a private debt; a delegate cannot

Part 3 of the Second Schedule gives "other officers and employees" immunity only "in
respect of things done or omitted to be done in the course of the performance of
official duties". Part 2 gives representatives, committee members, high officers and
persons on missions "the like immunity from suit and legal process as is accorded to
an envoy", with no official-duties limit in this Act. The extent of that envoy immunity
is not stated in the Act. The encoding treats Part 2 holders as immune whatever the
claim is about, and that reading comes from diplomatic law, not from this Act. Asserted.

### 3. Families are covered up to age 20, but only an officer's family

Part 4 extends Part 2 to an entitled officer's "wife or husband and children under the
age of 21 years". It also covers a representative's or committee member's official staff
"accompanying him as such". The order can exclude Part 4 (s 2(2)). Part 4 names officers,
not persons on missions. The encoding reads that as leaving a missioner's family
uncovered, but that is an **inference**. Asserted: a child aged 20 is covered, a child
aged 21 is not, and an aide left at home is not covered.

### 4. No export-duty exemption is possible, and customs conditions bind

Part 1 item 3 grants relief from taxes and rates "other than import, export or excise
duties". Item 4 then restores only import and excise duties, only on goods "directly
imported ... for its official use", and "subject to compliance with such conditions as
the Director-General of Customs may prescribe". Export duty is excluded and never
restored. Asserted.

### 5. The order may not go further than a treaty requires

The proviso to s 2(2) forbids conferring immunities "greater in extent than those which,
at the time of the making of the order, are required" by an international agreement.
Asserted as a test on two inputs: was it conferred, and was it required. The Act does
not say what happens to an order that breaches the proviso.

### 6. Lists, conferences, the ICJ and reciprocity

The President "shall" gazette a list of Part 2 holders but only "may" list Part 3 holders
(s 2(3)(a)). At a conference in Singapore attended by Singapore and foreign governments,
a foreign representative counts as an envoy, and listed staff as his retinue, only if
named on a published list, and publishing a list is discretionary (s 3(1)). For the UN,
an order may reach ICJ judges, registrars, suitors and their agents, counsel and
advocates (s 4(b)). The President may decline or withdraw immunities from a Power that
does not reciprocate (s 5). The Act contains no waiver provision; this is a reading of
the text's silence. Asserted, except the waiver point.

## What would need doing before this is worth anything

- The orders made under s 2(2) and s 2(1)(a), and the Gazette lists, were not retrieved.
  Without them no real organisation or person can be placed in a Part.
- The law of diplomatic immunity, which fixes the extent of Part 2, Part 4 and s 3
  status, is not encoded.
- No case law was searched.
- The Part 2 tax relief ("the like exemption or relief from taxes as is accorded to such
  an envoy") is not encoded, because its extent lies outside the Act.
