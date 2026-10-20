# Superannuation Industry (Supervision) Act 1993 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive encodings (the `writing-l4-rules` skill was not available in
this session). No pipeline, no coverage table, no independent test pass, no human
gate. NOT for public use.

**Edition:** Compilation No. 131, compilation date 10 August 2026, includes
amendments up to Act No. 49, 2026 (register id C2026C00361, in 2 volumes), as
deposited at `../../registers/source-bundle/C2004A04633.txt`.

**Checks:** one module (`sis-members.l4`), one case file
(`sis-cases-members.l4`), 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0007** in `subjects/au/requirements.jsonl` (priority 1), raised
**8 times** by the three Western Australian cradle-to-grave lives: Chloe c041 (first
payslip, "Part 7 (choice of fund; stapled fund)"), c04a (insurance inside super at
23, s 68AAA), c082 (binding nominations and their lapse, s 59(1A), reg 6.17A),
c090 (60 and still working: which condition of release?); Jake k094 (60, permanent
incapacity); Daniel d074 (his father's super, s 59), d085 (a non-lapsing
nomination, s 59(1A)), d093 (the super to Priya by nomination, s 59).

This encoding takes ss 10 and 10A (dependant, spouse, child, interdependency
relationship, legal personal representative), s 59 (the trustee-consent rule and
the binding nomination in (1A)), s 62 (the sole purpose test), s 29WA (undirected
contributions go to MySuper), s 64 (remitting deductions from pay) and ss 68AA,
68AAA-68AAF (insurance inside super). RSE licensing, covenants, investment rules,
successor-fund transfers of elections, the conditions of the s 68AAE and s 68AAF
exceptions, penalties and Parts 8 to 32 are not encoded.

## What the Act turns out to say

### 1. Most of what the lives ask is not in this Act at all

The conditions of release, preservation age, the "65" the life cites, what counts
as permanent incapacity, the form of a nomination notice and its three-year lapse
are all in the Superannuation Industry (Supervision) Regulations 1994, which are not
deposited. The Act only empowers them: s 31(2)(g) and (h) (preservation and payment
standards), s 59(1A) ("by notice given ... in accordance with the regulations",
"subject to ... any conditions contained in the regulations"), s 10 ("permanent
incapacity" if the member "is taken, under the regulations" to suffer it), s 62
("an age not less than the age specified in the regulations"). Each of these enters
the encoding as an INPUT. So c082's question "does a super nomination lapse?", c090's
and k094's "what lets them draw?" cannot be answered from this Act. Asserted only on
stated inputs: at 60 and still working, a benefit on attaining the regulations' age
is a permitted purpose if that age is 60, and not if it is 65; a benefit on
retirement is not available to someone who has not retired.

### 2. "Part 7" is not choice of fund, and nothing here sets the 11%

The life cites "Part 7 (choice of fund; stapled fund)" for the first payslip. Part 7
of this Act is "Provisions applying only to regulated superannuation funds" (the
sole purpose test, lending and borrowing limits, insurance). Choice of fund and the
stapled fund are in Part 3A of the Superannuation Guarantee (Administration) Act
1992, to which this Act's own s 29R(4) and the notes to s 68A point; the life itself cites
that Act's ss 16 and 19 for the 11%. What this Act does say about the payslip: an undirected contribution goes into
the fund's MySuper product (s 29WA), and a direction after 31 March 2013 not in
writing, or of which the trustee holds no copy, is taken not to have been given.
s 64 requires an amount deducted from pay to reach the fund within 28 days after the
end of the month of deduction (so by 28 March 2024 for a February 2024 deduction);
it is about deductions, not the employer's own guarantee contribution. Asserted.

### 3. A binding nomination is a permission to the fund, not a right of the member

s 59(1A): the governing rules "may" permit a member "to require a trustee" to pay
the death benefit "to ... the legal personal representative or a dependant or
dependants". If the rules do not take up the permission, there is no binding
nomination. The nominee must be a dependant (spouse, child, interdependency
relationship, or a dependant in the ordinary sense: the definition says "includes")
or the legal personal representative. A friend cannot be bound in, though a friend
who is the executor can receive as legal personal representative. Priya (d093),
Maria (d074) and Liam (c082) qualify as spouses; the encoding reads a legally
married spouse as a spouse in the ordinary sense, since the s 10 definition only
adds registered and de facto partners (an inference). Asserted.

### 4. The holder of an enduring power of attorney is a "legal personal representative"

s 10 defines legal personal representative to include "a person who holds an
enduring power of attorney granted by a person", alongside the executor and the
administrator. An ordinary power of attorney does not count. This is wider than the
ordinary sense of the phrase, and it sits next to the attorney appointments the
lives make in c082 and d085. Asserted.

### 5. Under 25, no insurance by default; at 25, a MySuper member gets it by default

s 68AAC bars a fund from providing a benefit by insurance to a member "under the age
of 25 years" who has not elected it in writing; s 68AAA does the same after 16
months of inactivity, and s 68AAB below a $6,000 balance never reached since
1 November 2019. An election under s 68AAB(2) counts for s 68AAC, and vice versa.
None of them apply to funds of six or fewer members (s 68AAD). For a MySuper member
not barred, s 68AA(1) requires death and permanent incapacity cover by insurance,
which the member may decline (s 68AA(5)). Chloe at 23 (c04a), with no election, gets
no cover; electing gets it; at 25 she gets it by default unless she opts out. Her
balance is not stated in the scenario; the case uses $15,000, an inference from
about 31 months of contributions at $641.67. Asserted.

### 6. The dangerous occupation exception does not save an inactive account

ss 68AAB(4)(e) and 68AAC(4)(e) exempt a member covered by the dangerous occupation
exception (s 68AAF); s 68AAA(6) has no paragraph (e). A firefighter under the
exception keeps default cover at 22 or on a low balance, but loses it after 16
months of inactivity like anyone else. Asserted.

### 7. A death benefit may go only to the legal personal representative or dependants

Every death purpose in s 62(1)(a)(iv), (v) and (b)(iii), (iv) requires the benefit
to be "provided to the member's legal personal representative, to any or all of the
member's dependants, or to both". A death benefit paid directly to a non-dependant is
not a purpose for which a regulated fund may be maintained. Death before retirement
(or before the regulations' age) is a core purpose; death after it is ancillary.
Benefits on ceasing work "on account of ill-health" (Jake, k094) are an ancillary
purpose. Asserted.

### 8. A self managed fund escapes the trustee-consent rule

s 59(1) forbids rules letting a non-trustee exercise a discretion without trustee
consent, but only for "a superannuation entity other than a self managed
superannuation fund". s 59(1A) speaks of "a superannuation entity" without that
exception. Asserted for s 59(1).

## What would need doing before this is worth anything

- Deposit and encode the Superannuation Industry (Supervision) Regulations 1994:
  Schedule 1 conditions of release, preservation age,
  permanent incapacity, reg 6.17A (binding nominations and their lapse), the
  interdependency matters under s 10A(3). Without them c082, c090 and k094 cannot be
  answered.
- Encode the Superannuation Guarantee (Administration) Act 1992 (ss 16, 19, 23,
  Part 3A) for c041's amount and choice of fund.
- The s 68AAE and s 68AAF exceptions are taken as inputs; their conditions (QE day
  excess contributions, actuarial certification, election to APRA) are not encoded.
- The ordinary-sense meaning of "dependant" (financial dependence) comes from case
  law, which was not searched.
- The ITAA 1997 Div 302 tax treatment of the death benefit (d093) is a separate
  subject.
