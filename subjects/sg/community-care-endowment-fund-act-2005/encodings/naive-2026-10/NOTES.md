# Community Care Endowment Fund Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/CCEFA2005.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". No later amendment is annotated. The SSO metadata reads "Current
version as at 01 Oct 2026".

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

The Act is requirement **REQ-0164** in `subjects/sg/requirements.jsonl`: Tier 3 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person or business it applies to. No scenario has
yet asked a sharper question.

This row covers what a person seeking help, a donor, a social service organisation,
or someone questioned by the auditor actually meets:

- who the Fund's income may help (s 6(1))
- how money may be paid out (ss 5(4), 6(2), 11)
- gifts (s 5(3))
- the income left after making good capital losses and paying expenses (ss 3(3), 5(5), 8)
- the financial year (s 9)
- who may audit (s 12(1), (2))
- the two offences (ss 13, 15) and their fines
- liability of officers and partners (s 16)
- composition (s 17)
- removal of Council members (Schedule para 1(3))

Not encoded:

- establishment and administration as such (ss 3(1), (2), 4, 7)
- the Minister's accounts and annual report (ss 10, 14)
- the auditor's access and report contents (s 12(3)–(6))
- regulation-making (s 18)
- the Council's procedure (Schedule paras 2–5)

No regulations were retrieved.

## What the Act turns out to say

### 1. The Act gives nobody a right to help

The Act sets out objects (s 6(1)), and under s 6(2) the Minister "may" authorise
income to be paid out. Grants to individuals or families are given "through
organisations" (s 6(2)(a)). A grant paid straight to an individual is allowed only if
it is a purpose "as may be prescribed" (s 6(2)(c)). How anyone applies is left to
regulations (s 18(b)), and none were read. Every payment needs the approval of the
Minister or an authorised officer (s 11). Asserted (a direct grant fails unless it is
prescribed, and any payment fails without approval).

### 2. A donor cannot direct that a gift be spent

s 5(3): "Despite the terms of any gift or bequest", every gift or bequest for the
Fund is paid in as capital. s 5(4) says capital may be used only for investment. So
only the income a gift earns is ever spent. The donor's terms make no difference.
Asserted.

### 3. Capital losses and running costs come out of the help budget first

s 5(5): a "permanent diminution" of capital must be made good from income "before
paying out any income". s 8: all administration expenses, "including the cost of
auditing", are paid out of income. The Act does not say which comes first, or what
happens when income falls short. This encoding deducts both and floors the result at
nil, which is an inference. Asserted with figures (for example, $1,000,000 income, a
$250,000 loss to make good and $100,000 of expenses leave $650,000).

### 4. Who may be helped: citizens, PRs and family members living in Singapore

s 6(1)(a) and (c) cover "citizens and permanent residents of Singapore and their
family members living in Singapore" who are in financial or other difficulties. This
row reads "living in Singapore" as qualifying only the family members, the nearest
antecedent. On that reading a citizen abroad is not excluded by the words. That is an
inference. In (b), on children's developmental issues, it is read as qualifying the
family. "Family member" is not defined. A foreigner with no such family tie falls
outside the objects. Asserted, on this reading.

### 5. Two small offences, both fine-only

The fines:

- **Failing to give the auditor information** without reasonable excuse, or
  hindering, obstructing or delaying the auditor: up to $1,000 (s 13(2)).
- **Knowingly** making a false statement, or giving a document known to be false in a
  material particular, to the Minister, an authorised officer, the auditor or the
  auditor's delegate: up to $5,000 (s 15).

Neither offence carries imprisonment. Unlike some Acts, s 13 does not put the burden
of the excuse on the accused.

s 15 does not list the organisations through which grants reach individuals. A false
statement made only to such an organisation is not within the words unless its staff
are authorised officers, and the Act does not say whether they are.

Compounding is capped at $500, and only for offences "prescribed as compoundable"
(s 17). None were seen. Asserted.

### 6. Officers, partners and committee members share the offence

s 16 makes an officer, partner or committee member guilty alongside the body
corporate, partnership or unincorporated association if the offence was committed
with their "consent or connivance" or is "attributable to any neglect" on their
part. "Body corporate" includes a limited liability partnership. Asserted.

### 7. The Community Assistance Fund is gone from the text

The long title says the Act also terminates "the charitable trust known as the
Community Assistance Fund". The Comparative Table shows that s 19 of the 2006 Edition
was "Omitted as having had effect". The terms of that termination are not in the
deposit. Not asserted.

### 8. The arrangement is out of step with the body

In the deposit's arrangement of sections, the heading "Composition of offences" is
split across a page break. That makes it look as though s 17 is Regulations and s 18
is the Schedule. In the body, s 17 is Composition of offences and s 18 is
Regulations. This row follows the body.

## What would need doing before this is worth anything

- Retrieve the regulations under ss 17 and 18. They decide how people apply for
  help, the payment procedure, and whether any offence is compoundable. ComCare
  schemes in practice are probably run under them or under administrative policy, so
  this Act on its own says very little about who actually gets help.
- Settle the reading of "living in Singapore" in s 6(1), and the meaning of "family
  member".
- Check whether staff of social service organisations disbursing ComCare grants are
  "authorised officers" (s 2, s 15).
- Read the 2006 Edition s 19 for the termination of the Community Assistance Fund.
