# Little Sisters of the Poor Ordinance 1957 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/LSPO1957.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The only amendment annotation in the body is "[7/97]" under s 5.
The Ordinance is dated 1 November 1957. The arrangement of sections at the top of the
deposit is shifted by the PDF extraction; section numbers here follow the body.

**Checks:** one case file, 42 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0237** in `subjects/sg/requirements.jsonl`: tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Ordinance
decides for a person or business it applies to; no scenario has asked a sharper
question yet. The Ordinance has five sections, so all of it is in scope except the
short title (s 1). For someone outside the Congregation it matters when dealing
with the Corporation's property and checking that its deeds were executed by the
right person. Not encoded: the recitals, the content of s 48 of the Conveyancing and
Law of Property Act 1886 (whether a power of attorney was "deposited" is a stated
fact), and how the office is filled.

## What the Act turns out to say

### 1. The Ordinance promises an appointment procedure it never gives

s 2(1) incorporates Reverend Mother Hedwige and her successors "duly authorised and
appointed as hereinafter provided". Nothing after it provides how a successor is
authorised or appointed. The only later word on appointment is s 4, which is about
proof: a Gazette notification of the appointment is "conclusive evidence that such
person was duly authorised to exercise the said office". The encoding treats the
holder as whoever is in office and duly authorised, and the Gazette as conclusive
proof of authorisation; without a notice the Ordinance is silent, so the encoding
says "not conclusively proved", not "not authorised". Asserted.

### 2. There is no stand-in during a vacancy, so no one can execute a deed under s 3

s 3(1) requires sealing "in the presence of the Reverend Mother Superior for the time
being or her attorney" and signing by the same. No deputy is named for a vacancy
(sibling ordinances such as the Brothers of St. Gabriel Ordinance 1950 name one).
Reading "her attorney" as the attorney of the holder for the time being, which is an
inference, nobody qualifies while the office is vacant: a deed executed then, even by
a deposited attorney, does not meet s 3. A former Reverend Mother Superior never
qualifies. Asserted.

### 3. A deed needs the seal, a qualified witness and a qualified signer

s 3(1) requires all three. An attorney qualifies only under a power of attorney
"deposited under section 48 of the Conveyancing and Law of Property Act 1886"; one
whose power was not deposited never does. The witness and the signer may be
different qualified persons (the Reverend Mother Superior witnessing and her
attorney signing), an inference from the separate "or" in each limb. s 3(2): the
signing is "sufficient evidence" that the seal was duly affixed and is the lawful
seal, so the encoding asks only about the seal and the signer for that. Asserted.

### 4. The Corporation is given no express power to sue or be sued

s 2(3) lets the Corporation acquire, hold and enjoy property of every description,
and sell, convey, assign, surrender, mortgage, demise, transfer "or otherwise
dispose of" property "vested in the Corporation". Unlike some sibling ordinances,
there is no clause on suing or being sued, and none on borrowing. The encoding
returns "not granted by the Ordinance" for those; whether the general law of
corporations supplies the capacity is outside the text. Disposal of property not
vested in the Corporation is not empowered. "Exchange" is not listed and is treated
as falling under "otherwise dispose of" (an inference). Asserted.

### 5. The office named is for Malaya, in a Singapore statute

The Corporation's name is "Reverend Mother Superior of the Little Sisters of the
Poor in Malaya" (s 2(1)), and the recitals speak of the Home "at Number 999 Thomson
Road in the Colony of Singapore and in Penang in the Federation of Malaya", the
Congregation having been "constituted at Rennes in France in the year 1839". The
2020 Revised Edition keeps all of this, including the first holder's name. Not
asserted (nothing turns on it in the encoding).

### 6. Everyone else's rights are saved

s 5: nothing in the Ordinance affects the rights of the Government, bodies politic
and corporate "and all others except such as are expressly mentioned in this
Ordinance, and those claiming by, from or under them". Asserted.

## What would need doing before this is worth anything

- s 48 of the Conveyancing and Law of Property Act 1886 was not read; what makes a
  power of attorney "deposited" is taken as given.
- The vacancy gap (finding 2) and whether a predecessor's power of attorney survives
  her leaving office need a lawyer's reading or case law; none was searched.
- Whether the general law gives the Corporation capacity to sue and be sued, and
  whether the Interpretation Act reads "Malaya" and "the Colony of Singapore" in a
  current Singapore sense, were not checked.
