# Census Act 1973 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `CA1973.txt`. The deposit says it
incorporates all amendments up to and including 1 December 2021 and came into
operation on 31 December 2021. Its Legislative History lists Act 15 of 2010 (the
Criminal Procedure Code 2010) as the last amending Act, then the 2013 Revised
Edition. The arrangement of sections at the top of the deposit is one number out of
step with the body (it lists "Occupier to allow access" as s 9). This row follows the
body's numbers.

**Checks:** one case file, 54 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

It is **REQ-0128** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the
Act decides for a person or business it applies to; no scenario has asked a sharper
question yet. This row takes what a household, a hotel or institution, or an employer
meets when a census is taken, what may be done with their answers, and the offences:
ss 7(2), 8, 10, 11, 13, 14, 17, 18, 19, 20, 21, 22, 23 and the two Schedules. Not
encoded: the power to direct a census (s 3), appointments (ss 4-6), the forces and
people not living in a house (s 12), Government employees' duty to help (s 15), the
internal flow of schedules (s 16), the Minister's duty about trade secrets (s 17(5)),
rules (s 24), amendment of the Schedules (s 25) and the transitional provision (s 26).

## What the Act turns out to say

### 1. Your census answers can go to the CPF Board, but the Board cannot use them against you

s 18(1) lets the Superintendent, "despite section 17", disclose an individual's
particulars on a confidential basis to a public authority in the Second Schedule. The
only one listed is the Central Provident Fund Board. It needs a written request from a
gazetted responsible officer, the information must be something the Board could have
got under another law, and anything the census itself got from a competent authority
under s 13 needs that authority's written consent. s 18(3) then forbids anyone at the
Board to use it "for the purpose of enforcing any obligation or liability", and s 18(4)
makes onward disclosure without the Superintendent's written approval an offence
($1,000 or one month). Asserted.

### 2. Information flows the other way too, except tax and MAS data

s 13 lets the Superintendent direct a First Schedule authority (again only the CPF
Board, for information under the CPF Act 1953) to hand over particulars "despite the
provisions of any written law", with no breach of confidence. s 13(3) carves out
anything obtained under a tax law or a law the Monetary Authority of Singapore
administers. Asserted.

### 3. Only written consent lets your answers out

s 17(4): an individual's particulars may not be disclosed "without the previous
consent in writing" except for industry statistics (unless the Minister exempts the
industry), unidentifiable data once the Minister thinks enough time has passed,
proceedings for an offence under this Act, and general information obtainable
elsewhere. Oral consent, an exempted industry, or proceedings for some other offence do
not qualify. s 23 goes further: a census entry is not admissible in any civil or
criminal proceedings, except a prosecution under this Act of the person who made the
entry. Asserted.

### 4. Most offences carry $1,000 or a month; impersonating an officer carries six months and no fine

Refusing a necessary question, a knowingly false statement, obstruction, removing
census marks within 6 months, non-compliance with the Act, and passing on information
known to have been unlawfully disclosed (s 20); an officer's misconduct, including
taking a payment from anyone other than an authorised Government officer (s 19): all
$1,000 or one month or both. s 21 gives impersonation imprisonment up to 6 months and
names no fine. No prosecution without the Public Prosecutor's consent (s 22). The words
"necessary", "knowingly", "before the expiry of 6 months" and "to his or her
knowledge" each leave a non-offence on the other side; the encoding asserts four of
them. Asserted.

### 5. The officer can come back for a year, or longer, never shorter

s 10(4): on the Superintendent's direction an officer may revisit to check or correct a
schedule "before or within one year (or such longer period as may be prescribed)".
The encoding reads a prescribed period shorter than a year as having no effect, because
the text says "longer". An occupier who cannot fill in the schedule complies by keeping
it unfilled and handing it back (s 10(3)). Asserted.

### 6. Hotels, boarding houses and clubs fill in for their guests; employers only on requisition

s 11 lists hospitals, prisons, police stations, lock-ups, public, charitable,
religious and educational institutions, hotels, boarding houses, lodging houses and
clubs. That serviced apartments, workers' dormitories and office buildings are outside
the list is an inference from the list, asserted as such. An employer is bound to act
as an enumerator only on a signed written requisition, and only for employees living
in a factory or workshop or of a gazetted class (s 14). Asserted.

## What would need doing before this is worth anything

- No census notification under s 3, rules under s 24, or Gazette notification of
  responsible officers or employee classes was retrieved; "the time mentioned" in a
  schedule and any prescribed checking period are inputs.
- s 20(e) ("refuses or neglects to comply with any of the provisions of this Act")
  makes breach of ss 8, 10, 11 and 14 an offence; the encoding treats that link as a
  conduct label, not a derivation from each duty.
- Whether a person may decline to deal with an officer who will not produce the s 7(2)
  letter of appointment is not said by the Act and is not encoded.
- No case law was searched.
