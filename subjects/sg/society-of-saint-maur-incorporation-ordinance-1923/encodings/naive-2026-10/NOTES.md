# Society of Saint Maur Incorporation Ordinance 1923 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition (amendments up to 1 December 2021, in operation 31
December 2021), informal consolidation, "version in force from 25/3/2024", deposited
at `../../registers/source-bundle/SSMIO1923.txt`. The latest amendment annotated is
Act 7 of 2024, the Society of Saint Maur Incorporation (Amendment) Act 2024, in force
25 March 2024. It rewrote ss 2-5, repealed s 6, added s 7 and deleted the three
Schedules. The arrangement of sections at the top of the deposit is one line out of
step with its headings, so this row follows the section numbers in the body.

**Checks:** one case file, 46 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0251** in `subjects/sg/requirements.jsonl`: Tier 4 of
the remaining Singapore Acts, ordered by how often the Act touches everyday life. The
requirement asks what the Act decides for a person or business it applies to. No
scenario has asked a sharper question yet. For someone dealing with the Corporation
the Ordinance decides three things. Is the woman acting as the Corporation qualified?
Is a deed it executes duly sealed? Under what name can it be sued, or contracted
with? The operative text is short, so all of it is encoded: ss 2-5, 7 and 8. Left out
are the preamble, s 1, the repealed s 6, the deleted Schedules, and everything in s 48
of the Conveyancing and Law of Property Act 1886 except whether a power of attorney
was deposited under it.

## What the Act turns out to say

### 1. A signature is evidence of due sealing even where the sealing itself was not proper

s 5(2) deems an instrument duly sealed only if two limbs are both met. The seal must
be affixed in the Lady Superior's presence or by her deposited attorney, **and** the
instrument must be signed by her or by that attorney. The same subsection then says
the signing "shall be and be taken as sufficient evidence that the seal ... was duly
and properly affixed". So a deed sealed in a clerk's presence and then signed by the
Lady Superior fails the deeming rule, yet its signature is sufficient evidence that
it passes. The encoding holds both results side by side and does not resolve them.
Asserted.

### 2. Qualification takes three steps, but the Gazette alone proves all three

s 3: no successor is qualified "unless and until" her appointment has been notified
to the Minister, the Minister has approved it, **and** the approval has been
gazetted. s 4: the Gazette notice is "sufficient evidence" that she was duly
appointed "and is duly qualified". A successor whose approval was gazetted but who
was never notified to the Minister is therefore not qualified on the encoding, while
her Gazette notice is still sufficient evidence that she is. The Act does not call
that evidence conclusive, and this row does not decide whether it can be rebutted.
Asserted.

### 3. The named founder needed none of it

s 2 makes "the said Euphrasie Labordenave and her successors ... duly qualified as
hereinafter provided" the corporation. s 3 imposes its conditions only on a
"successor". The first holder was the Corporation by being named. Asserted.

### 4. A Penang office, held "for Singapore"

Since the 2024 amendment, s 2 defines the corporation sole as the holder of the
office of "Lady Superior in Penang of the Society of Saint Maur appointed for
Singapore". The Penang office is kept, while the 2024 Act took "in Penang" out of the
corporate name. The encoding treats "appointed ... for Singapore" as a single fact
about the appointment. It does not try to say what a Penang office held for Singapore
means. Not separately asserted.

### 5. An undeposited power of attorney counts for nothing

An attorney may affix the seal, or sign, only if she is "duly authorised by a Power
of Attorney deposited under section 48" of the Conveyancing and Law of Property Act
1886. An attorney whose power was never deposited meets neither limb, so a deed she
seals and signs is not deemed duly sealed. Mixed execution does pass: sealed in the
Lady Superior's presence and signed by a deposited attorney, or sealed by the
attorney and signed by the Lady Superior. Asserted.

### 6. No ministerial control over property; the old name still works

Under s 5(4) the Corporation may buy, hold, sell, mortgage, lease and otherwise
dispose of property "upon such terms as to the Corporation shall seem fit", and under
s 5(3) it may sue and be sued in all courts. No provision of the Ordinance makes any
of this subject to the Minister. The Minister appears only in approving the Lady
Superior's appointment. Trading for profit and unsecured borrowing are not conferred
by this Ordinance; whether other law confers them is not decided here. s 7 reads any
reference to "The Lady Superior of the Convent of the Holy Infant Jesus in Penang" as
the new name, "The Lady Superior of the Convent of the Holy Infant Jesus". It says
the change does not render proceedings defective, and that proceedings that could
have been brought under the old name may be brought under the new one. s 8 leaves the
rights of everyone else untouched, unless they are "mentioned in this Ordinance" or
claim through someone who is. Asserted.

## What would need doing before this is worth anything

- s 7(1) runs "as from the date of publication in the Gazette" of the 2024 Act. That
  date is not in the deposit; the deposit gives only commencement (25 March 2024). The
  encoding takes "after publication" as an input.
- s 8 and the Government: the Minister is mentioned in s 3. Whether that brings the
  Government within s 8's exception was not decided. The test treats a person who is
  not mentioned and claims through no one as unaffected.
- The "Lady Superior for the time being" in s 5(2) is taken as given. Whether an
  appointee who is not yet qualified under s 3 counts as her is an open question,
  and it was not modelled.
- s 48 of the Conveyancing and Law of Property Act 1886 was not read.
- No Gazette notifications or case law were searched.
