# Public Trustee Act 1915 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the other naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation. The deposit says it
"incorporates all amendments up to and including 1 December 2021"; it also shows
Act 25 of 2021 (wef 1 April 2022) and Act 31 of 2022 (wef 1 November 2022)
annotated.

**Checks:** two case files, 92 assertions satisfied (54 in `pta-cases-trusts.l4`, 38 in
`pta-cases-small-estates.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**6 of the 527 Singapore Acts** deposited here cite it. This row takes the rules with
decision content that a trustee, beneficiary, executor or family member meets: which
trusts the Public Trustee may decline or must refuse (s 4(4), (5)), small estates
(s 6(1)), appointment as trustee and the beneficiaries' notice (s 7), next of kin and
transfer of an estate (s 8(2), (4)), the income deadline (s 12A(4)), the Investment
Board quorum (s 13(7)), the Consolidated Fund's liability (s 17), unclaimed funds
(s 21) and the audit of trust accounts (s 22). Officers, delegation, minors'
litigation representation, the Common Fund's investment and income formula, the
Reserve Fund, fees and rules are not encoded.

## What the Act turns out to say

### 1. Any trustee or beneficiary can force an audit of any trust, not only the Public Trustee's

s 22(1) is not confined to trusts the Public Trustee holds: on application by "any
trustee or beneficiary", the condition and accounts of "any trust" are audited by a
solicitor or public accountant agreed with the trustees or, failing agreement, by the
Public Trustee or its appointee. Not within 12 months of a previous audit without the
court's permission, and never by a trustee or beneficiary (s 22(2)). Costs fall on
the estate unless the Public Trustee directs otherwise (s 22(7), (8)). A wilful
material falsehood in the accounts, report or certificate is an offence, up to 2
years' imprisonment (s 22(10)). Asserted.

### 2. The Government stands behind the Public Trustee's breaches, with one gap

s 17: the Consolidated Fund makes good any liability the Public Trustee would bear
personally as a private trustee, except where neither it nor any officer contributed
**and** none could by reasonable diligence have averted it, in which case "neither the
Public Trustee nor the Consolidated Fund shall be subject to any liability". So a
loss nobody in the office caused or could have prevented falls on the trust. Asserted.

### 3. Small value is never a reason to refuse; some trusts must always be refused

s 4(4) lets the Public Trustee decline any trust, but not "on the ground only of the
small value of the trust property". s 4(5) forbids accepting a trust carrying on a
business (unless rules authorise it), a deed of arrangement for creditors, or an
estate the Public Trustee knows or believes insolvent. For small estates (s 6(1)),
the Public Trustee **must** administer where the value is below the prescribed amount
and the beneficiaries are of small means, unless it sees good reason to refuse. The
prescribed amount is set by rules not retrieved; it is a parameter. "Less than" is
encoded strictly. Asserted.

### 4. Appointment needs written consent, but notice failures do not matter

s 7(4): no appointment has effect without the Public Trustee's written consent, but
s 7(6) lets it act "as if" it had consented once it knows of the appointment
(treating that as giving the appointment effect is an inference). An instrument
directing against the Public Trustee blocks its appointment as a new or additional
trustee unless the court orders otherwise (s 7(8)). Beneficiaries notified have 21
days to apply to the court to prohibit it (s 7(10)), yet failure to give notice "does
not invalidate the appointment" (s 7(11)). Asserted.

### 5. Family come first for letters of administration

s 8(2): as between the Public Trustee and the widower, widow or next of kin, the
family "is to be preferred, unless good cause is shown to the contrary". An executor
wanting to hand an estate over must get the Public Trustee's written consent before
applying (s 8(4)). Asserted.

### 6. Unclaimed money waits 7 years, then a late claimant loses the interest

s 21: undistributable funds go to the Unclaimed Estates Account for 7 years, then
with interest to the Consolidated Fund; an established later claim is paid "without
interest". Common Fund income must reach each estate within 45 days of the end of the
basis period (s 12A(4)), and the Investment Board's quorum is the chairperson and 2
others (s 13(7)). Asserted.

## What would need doing before this is worth anything

- The Public Trustee rules (prescribed amount for small estates, authorised classes
  of trust, fees, audit costs) were not retrieved.
- The income formula in s 12A(2) is garbled in the text deposit (the fraction is
  split across lines) and was not encoded; the PDF should be checked before it is.
- No case law on s 17 or s 22 was searched.

## Small estates (added 12 October 2026 for REQ-0279)

Module `pta-small-estates.l4`, cases `pta-cases-small-estates.l4`. Source: Act s 6 and the
Public Trustee Rules (R 1, informal consolidation in force from 1 April 2022), deposited at
`registers/source-bundle/PTA1915-R1.txt`.

1. **The answer: no, not under s 6(1). The prescribed amount is $5,000, not $50,000.**
   Rule 7A reads: "For the purposes of section 6(1) of the Act, the prescribed amount is
   $5,000." (inserted by S 864/2014 wef 31 December 2014). The figure was read in the .txt
   deposit and again in a fresh `pdftotext` extraction of the deposited PDF; both give
   "$5,000", and the heading and text of rule 9(1) ("Estate less than $5,000") repeat it, so
   this is not a garbled extraction. The ledger's expected $50,000 is not what the deposited
   Rules say. An intestate estate of $38,000 is not "less than the prescribed amount", so
   the Public Trustee has neither the duty nor (on this route) the power to take it on
   application under s 6(1), and rule 9(1) says it "shall refuse the application".
2. **"Less than" is strict.** An estate of exactly $5,000 is outside; $4,999.99 is inside.
   The test is the "gross capital value", proved "to the satisfaction of the Public Trustee".
3. **Within the limit the duty is mandatory, with three outs.** The Public Trustee "must
   administer" if the applicant could apply to court for an administration order, the
   beneficiaries appear to be "persons of small means", and it sees no "good reason for
   refusing". "Small means" and "good reason" are not defined; they are inputs.
4. **"Without a grant" is an inference.** s 6(2) vests the trust property in the Public
   Trustee "by virtue of this Act" on its signed and sealed declaration. The Act never says
   "without a grant"; reading the vesting as dispensing with probate or letters is labelled
   an inference in the module.
5. **The court route has no value limit.** Under s 6(6), on administration proceedings
   already instituted, the court may order the Public Trustee to administer where the small
   value makes it more economical or it is "expedient" for any other reason, after
   considering the Public Trustee's views (s 6(7)); s 6(8) then treats it as if the
   undertaking under s 6(2) had been given. That is the only route under s 6 for $38,000, and
   it needs a court.
6. **What the full answer needs from elsewhere.** The ledger's "$50,000" probably comes from a
   different instrument (an inference: perhaps the Public Trustee's administration of small
   estates under the Probate and Administration Act or related rules, none of which was read
   here). The Intestate Succession Act decides who takes the $38,000. A refusal under rule 9
   does not stop the Public Trustee acting under other powers if duly appointed (rule 9(3)).
   No case law on "small means" or "good reason" was searched.
7. The earlier module `pta-trusts.l4` keeps its own s 6(1) rule with the amount as a parameter
   (its cases use $50,000 as an illustrative figure); it was not rewritten.
