# Minister for Finance (Incorporation) Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text. The `writing-l4-rules` skill
was not available in the session that wrote this row, so its conventions were
followed as the finished example rows show them. No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/MFIA1959.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The body carries no amendment annotations; the Legislative History's
last entry for this Act is the 2014 Revised Edition.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0185** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet. The Act is eight short sections, so the whole operative text
(ss 2-8) is encoded. For a person or business it answers a few narrow questions: whom
to sue, how a deed from the Minister for Finance must be executed, and when property
changes hands without a conveyance.

## What the Act turns out to say

### 1. The President can move property between the Corporation and public bodies by order, with no conveyance

s 5(2) lets the President vest in the Corporation any property "for the time being
vested in any public officer or authority"; s 5(3) does the reverse. Either way the
property moves "without any conveyance, assignment or transfer whatever", for "the
like title, estate or interest and on the like tenure". Neither subsection reaches
property held by a private person. The encoding asserts both directions, that an
order not yet in operation changes nothing, and that an order cannot take a private
person's property. Asserted.

### 2. A tenant of moved property gets a new landlord, and s 8 does not stop it

s 8 saves the rights of everyone "except such as are mentioned in this Act and those
claiming by, from or under them". A tenant of land moved by a s 5 order claims under
the officer, authority or Corporation named in the order, so the saving does not
protect the tenant from the change; s 5 keeps the tenure itself unchanged (a lease
with 37 years left still has 37). A private landowner with no claim through anyone
named is untouched. Treating the Government as not "mentioned" is an inference: it
appears only in s 8 itself. Asserted.

### 3. The Corporation is sued in its own name, whoever is Minister

s 2(1) makes "the Minister for the time being charged with the responsibility for
finance" a body corporate named "Minister for Finance"; s 2(2) says it "may sue and be
sued in its name" and has "perpetual succession". A claim about property vested in it
goes against the Corporation, not the individual Minister. Asserted.

### 4. A deed needs the seal, the current Minister present, and the current Minister's signature

s 4(1): the seal is affixed "in the presence of the Minister for the time being
charged with the responsibility for finance", who must sign; the signature is
"sufficient evidence" that the seal was duly affixed and is lawful. Until a seal is
provided, a stamp inscribed "Minister for Finance" serves (s 2(2)). s 4(2) disapplies
s 11 of the Registration of Deeds Act 1988 to any instrument "purporting" to be so
executed; what s 11 requires was not read. Asserted.

### 5. A Gazette notification settles who the Minister is

s 7: a Gazette notification that a Minister is charged with finance is "conclusive
evidence". Without one, the Act is silent; the encoding's "to be proved by ordinary
evidence" is an inference. Asserted.

### 6. s 6 passes on the Chief Secretary's liabilities from any source; s 5(1) passes property only from one

s 5(1) vests only property held "under the provisions of the Chief Secretary
Incorporation Ordinance". s 6 passes rights and liabilities held "by virtue of" that
Ordinance "or otherwise". Asserted.

### 7. s 3's powers are powers over property

s 3 lets the Corporation acquire, hold, convey, mortgage, demise and "otherwise
dispose of, or deal with" property "upon such terms as to the Corporation seem fit".
It says nothing about borrowing or guarantees; the encoding reads s 3 as not
conferring them, without deciding whether any other law does. Asserted.

## What would need doing before this is worth anything

- Section 11 of the Registration of Deeds Act 1988 was not read, so the practical
  effect of s 4(2) on registering a deed from the Corporation is unknown here.
- No President's order under s 5(2) or (3) was retrieved; which property the
  Corporation actually holds is not known to this row.
- Whether a Second Minister for Finance can be "the Minister for the time being
  charged with the responsibility for finance" for s 4(1) is not decided.
- No case law was searched.
