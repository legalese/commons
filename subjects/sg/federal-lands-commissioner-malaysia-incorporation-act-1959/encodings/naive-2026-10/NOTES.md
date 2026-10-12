# Federal Lands Commissioner, Malaysia (Incorporation) Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FLCMIA1959.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021" and came into operation on 31
December 2021. Its Legislative History lists no amendment after Ordinance 71 of 1959
and G.N. No. S (N.S.) 179/1959, apart from the 1970, 1985 and 2020 Revised Editions.

**Checks:** one case file, 47 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0233** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to. No scenario has asked a sharper question yet.

The Act is short (11 sections). The people it touches are those who deal with the
Corporation over Singapore property held for the Government of Malaysia: buyers,
lessees, mortgagees and litigants. This row encodes ss 3(2), 4-9 and 11. It leaves out
s 1 (short title), s 2 (definitions, used in comments only), s 3(1) (the incorporation
itself) and s 10 (a deeming that the Act is a private Act for the Registration of Deeds
Act 1988, with nothing to decide).

## What the Act turns out to say

### 1. Liabilities pass more widely than property

s 7(1) vests in the Corporation only property "in Singapore" that was vested in the
Chief Secretary, Federation of Malaya, immediately before 27 February 1959 "under the
provisions of" the 1955 Ordinance. s 8 passes the Chief Secretary's rights, powers and
liabilities "by virtue of the [Ordinance] or otherwise", with no Singapore limit. So a
counterparty's claim against the Chief Secretary passed to the Corporation whatever its
source, while property the Chief Secretary held otherwise than under the Ordinance did
not vest under s 7(1). Asserted.

### 2. A deed only has to purport to be executed under s 5(1) to escape the Registration of Deeds Act s 11

The evidential benefit in s 5(1) needs the seal affixed in the Commissioner's presence
and the Commissioner's signature: then "such signing shall be sufficient evidence" that
the seal was duly affixed and is the lawful seal. But s 5(2) disapplies s 11 of the
Registration of Deeds Act 1988 to "any instrument purporting to be executed under
subsection (1)". This row did not read what s 11 of that Act requires, because that Act
is not in this row's deposit. Asserted.

### 3. Only the Malaysia Gazette proves the appointment

s 6 makes a notification "in the Malaysia Gazette" conclusive evidence that a person
was duly appointed Commissioner. A notification in the Singapore Government Gazette, or
a letter of appointment, gets no such effect under s 6. The Act is silent on what weight
such evidence has otherwise. Asserted.

### 4. The President can still add property by order

s 7(2) is not spent: the President may by order vest in the Corporation any property
"for the time being vested in any officer or person for the purposes of the Government
of Malaysia". It vests when the order comes into operation, without conveyance, on the
same title and tenure. Asserted.

### 5. The Corporation may acquire anything but dispose only of what is vested in it

s 4 gives an unqualified power to contract and acquire, but the power to convey,
charge, mortgage, demise or otherwise dispose reaches only property "vested in the
Corporation". Asserted.

### 6. The stamp, the officer and the saving

Until a seal is provided, a stamp inscribed "the Federal Lands Commissioner" may serve
as the seal (s 3(2)). The row treats the stamp as no longer usable once a seal exists:
that is an inference, as the text does not say so. For the Land Acquisition Act 1966 the
Corporation is deemed a company, and its officer is a person both appointed by the
Corporation and authorised by the Minister (s 9). s 11 leaves untouched everyone's rights
except those "mentioned in this Act and those claiming by, from or under them". Asserted.

## What would need doing before this is worth anything

- Read s 11 of the Registration of Deeds Act 1988 to learn what s 5(2) actually spares.
- Read the Land Acquisition Act 1966 to see what being "deemed to be a company" lets
  the Corporation do there (finding 6 records only the deeming).
- No President's orders under s 7(2), and no case law, were searched.
- Who counts as "mentioned in this Act" under s 11 is left to the user as a flag.
