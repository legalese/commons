# National Research Fund Act 2006 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/NRFA2006.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. Its Legislative History lists only Act 17 of 2006 (commenced
22 August 2006) and the 2007 Revised Edition (Chapter 201A); no amending Act is
annotated.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0193** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is short (18 sections) and mostly sets up a Government fund and its Board.
A person or business meets it only when applying for, receiving or handling money
from the Fund. This row takes: what counts as "research and development activities"
(s 3), who the Fund may pay (s 5(2)) and the Board's authorisation (s 7(2)), the
secrecy offence (s 14), forgery and false statements (s 15), liability of officers
and partners (s 16), disclosure of members' interests (s 17), and the Board's term and
two reporting deadlines (ss 9(2), 9(3)(f), (g), 12(2)). Not encoded: what is paid
into the Fund (s 4), its objects (s 5(1)), its investments (s 5(3)), expenses and
withdrawals beyond s 7(2), the Board's other functions, the Council (s 10), accounts
and audit (ss 11-13), s 16(6) and regulations (s 18).

## What the Act turns out to say

### 1. Lying to get a grant carries a quarter of the prison term for leaking an applicant's secrets

Both s 14 (a person exercising functions under the Act who discloses protected
information) and s 15 (forgery, or a knowingly false statement in an application for a
grant or financial assistance) carry a fine of up to $5,000. But the maximum prison
term is 2 years under s 14 and 6 months under s 15. Asserted.

### 2. The list of things that are "not research" only removes them from one limb

s 3(2) says market research, testing, routine software development, reverse
engineering and the rest "must not be taken to be systematic, investigative or
experimental activities". That disqualifies them from s 3(1)(a). Nothing in the text
removes them from s 3(1)(b), which covers "other activities" carried on for a purpose
related to, or incidental or conducive to, a paragraph (a) project. Read literally,
market research or testing done for a genuine research project is still a research
and development activity. This is an inference from the wording; the cross-reference
in s 3(2)(i) to s 3(1)(b)(v) suggests the drafters saw the overlap. Encoded on the
literal reading and asserted both ways (excluded standing alone, included when related).

### 3. The recipient may be anywhere; the research must touch Singapore

s 5(2)(a) lets the Fund assist any public authority, enterprise, educational
institution or other person "(whether in Singapore or elsewhere)". But the activity
they undertake must be a research and development activity, and s 3(1) requires it to
be carried on "wholly or partly within Singapore". An overseas recipient qualifies; a
project carried on wholly abroad does not. Asserted.

### 4. An enterprise exploiting research needs the Board's favourable opinion on two counts

Under s 5(2)(b) the Board must think the enterprise "profitable and efficient or
capable of becoming profitable and efficient" and with "reasonable prospects for
profitability, development, expansion, growth or providing viable employment".
Profitable but inefficient is not enough (unless capable of becoming both). Every
payment also needs the Board's authorisation (s 7(2)). Asserted.

### 5. Honest mistakes are not offences, and officers answer for their companies

s 15(b) catches a false statement only where the maker "knows or believes [it] to be
false or does not believe [it] to be true". Under s 16 an officer, partner, or officer
of an unincorporated association is guilty alongside the entity where the offence was
committed with their consent or connivance or is attributable to their neglect; a
limited liability partnership counts as a body corporate, and a person purporting to
act as an officer is caught. Asserted.

### 6. Members must disclose conflicts, but no offence attaches

s 17 requires a Board or Council member with a direct or indirect pecuniary interest
that could conflict with their functions to disclose it at a meeting, recorded in the
minutes. The Act creates no offence or consequence for failing to do so. Asserted (the
duty only).

## What would need doing before this is worth anything

- No regulations under s 18 or NRF grant conditions were retrieved; in practice the
  terms of a grant come from those, not from this Act.
- The literal reading of s 3(2) (finding 2) needs testing against any case law or the
  Board's own practice.
- The `the recipient is outside Singapore` parameter in s 5(2)(a) is deliberately
  inert: it documents that location does not matter.
- No case law was searched.
