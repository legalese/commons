# National University of Singapore (Corporatisation) Act 2005 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/NUSCA2005.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021. The latest amendment annotated in the body is [40/2018] (s 7(2));
the First Schedule carries [S 633/2007]. SSO marked the retrieval "Current version as
at 03 Oct 2026".

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0194** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

Most of the Act is about the State and the company: the Minister's frameworks,
directions and trustees, and the 2006 vesting of property. This row takes what a
person meets: the consent rule and its consequence for anyone contracting with the
company (s 7), the limit on public money (s 8), the information offence (s 9),
student bodies (ss 10, 19), transferred staff and pending discipline (ss 13, 14, 16,
17), where a former Academic Staff Provident Fund (ASPF) member's money went (s 18 and
First Schedule paras 1(2), 5, 6, 11, 13, 15, 23, 24, 33-41, 46, 48), and the Register
of Graduates (s 20, Second Schedule). Not encoded: ss 3-6 beyond the consent list,
the vesting and land-registration machinery (s 12(1)-(9)), the continuation of
contracts and proceedings (ss 12(10), (11), 15), the ASPF notice and its deemed
service (paras 2-4), accounts and audit (paras 11(2), 12), mortgage transfers (paras
25-29), disclosure (paras 30, 31) and the evidence rule (para 49).

## What the Act turns out to say

### 1. A deal the Minister did not consent to beforehand is void, not merely irregular

s 7(1) requires "the prior written consent of the Minister" for admitting or removing
a member of the company, disposing of the whole or substantially the whole of its
undertaking or property, a voluntary winding up, any change to the constituent
documents, and removing a trustee. s 7(3): an act or agreement in contravention "has
no effect and is unenforceable at law". A buyer of substantially all of NUS's
property, without that consent, gets nothing enforceable. The Act says nothing about
ratification; the encoding reads "prior" as leaving a later consent ineffective (an
inference). Selling a single building and appointing a trustee are outside the list.
Asserted.

### 2. "Uncontactable" can be read two ways, and the ASPF money follows the reading

First Schedule para 1(2) treats a person as uncontactable if they have no CPF account
and the company "is not in possession of any of" the nationality, identification and
date-of-birth details "necessary for the opening of a CPF account", despite
reasonable efforts. Literally that means holding none of them; for its purpose,
lacking any one would stop a CPF account being opened. Both readings are encoded and
differ for a person whose nationality is known but whose identification is not. An
uncontactable person's money stayed with the company as trustee (paras 40, 41) and
could later be claimed (para 46). Asserted.

### 3. Members aged 55 could take their money; silence sent it to CPF

On 28 December 2007 (s 18(3)) the ASPF was dissolved. A member 55 or over on that
date could choose payment to themselves, conditional on having or setting aside the
s 15(6) CPF Act sum (para 5(b)); one who did not tell the company "in the manner and
by the date specified" had the money moved to the CPF Board (para 6). Under-55s went
to CPF (para 13(b)). Uncontactability outranks death: a "deceased relevant person" is
defined as one "who is not uncontactable", so an uncontactable person who died is
dealt with under paras 40-45, not 33-39. That an opt-out who failed the para 5(b)
condition fell back to CPF is an inference. Asserted.

### 4. A deeming rule may give cash payers a CPF right that para 24 seems to deny

Para 7 deems every Part V Assurance premium paid before 28 December 2007 "whether using
ASPF moneys or cash" to have been paid with ASPF moneys. Para 23 then lets a person
who "used ASPF moneys" pay future premiums from the CPF ordinary account, and para 24
says "to avoid doubt" that one who "did not ... use" them may not. Whether para 7's
deeming counts as "use" is not said. Both readings are encoded and they differ for a
cash payer. Asserted.

### 5. Anyone can be made to hand over information, and the excuse covers only one limb

s 9(2) lets the Minister or an authorised person require "any person", not only the
company, to provide information in their possession or access. s 9(4): failing to
comply "without reasonable excuse", or otherwise hindering, obstructing or delaying,
is an offence with a fine not exceeding $1,000 and no imprisonment. On a literal
reading the excuse attaches only to the failure to comply; that is this encoding's
reading, not a decided point. Asserted.

### 6. Staff kept their terms, their seniority, and their exposure to discipline

s 13(1) moved every employee on 1 April 2006 "on terms no less favourable", with the
old scheme continuing until the company drew up its own (s 13(2)); s 14(2) counts
service with the old university as service with the company. Pending disciplinary
proceedings against a transferred employee or a student had to be completed by the
company (s 16), and the company may punish misconduct committed before the transfer
(s 17). Asserted.

### 7. Student bodies are societies; graduates are on a three-part Register

s 10 applies the Societies Act 1966 to student bodies under the constituent documents,
subject to Gazette exemptions; s 19 deems the NUS Students' Union constituted that
way. The Second Schedule keeps a Register of Graduates in Part A (University of
Singapore), Part B (the statutory NUS before 1 April 2006) and Part C (the corporatised
University); anyone on it "may receive" papers the Board determines. Asserted.

## What would need doing before this is worth anything

- The ASPF provisions are spent in practice (dissolution was on 28 December 2007), but
  money held for uncontactable persons may still be claimable under para 46; nobody
  checked whether any remains.
- The constituent documents, the accountability agreement under s 4 and any Gazette
  exemption under s 10(2) were not retrieved.
- No case law was searched on s 7(3) or on para 1(2).
- The 30-day count in para 20 (to 27 January 2008, the date paras 35 and 42 name) was
  checked by hand, not encoded.
