# Prevention of Pollution of the Sea Act 1990 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/PPSA1990.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021"; its metadata calls it the current version as at 1 October 2026.
The latest amendment annotated in the text is Act 26 of 2017 (Prevention of
Pollution of the Sea (Amendment) Act 2017, in force 8 September 2017).

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0110**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. A person meets
it by tipping rubbish into the water from a jetty or a boat (s 5); a business meets
it by running a depot, refinery, shipyard or bunkering hose on the shore (ss 3, 4),
or by owning, managing or acting as agent for a ship in Singapore waters.

The Act has 35 sections plus the 5A, 10A, 10B, 13A and 33A insertions. This row
takes the meaning of "oily mixture" and "master" (s 2(1)), oil from land or a
transfer apparatus and its defences (ss 3, 4), throwing pollutants (s 5), discharges
from ships with their exceptions and defences (ss 6, 7, 10, 10A, 10B), the
government-ship exemption (s 26(1)), reporting a ship's discharge (s 15), the ship
owner's removal costs (ss 17, 18), eight offences' penalties, the continuing fine for
ignoring a reception-facility direction (s 11(6)) and composition (s 33). Not
encoded: sediments from land (s 5A), the elements of s 8, the noxious-cargo
notification (s 9), reception facilities beyond s 11(6), record books and their
evidence (ss 12 to 14 beyond the s 14(3) penalty), land-side reporting (s 16),
removal costs from land and from persons (ss 19 to 21), the Part 6 enforcement
machinery and the Minister's exemptions (s 26(2), (3)). No regulations were
retrieved, so whatever is "prescribed" — the reporting circumstances, the
compoundable offences, the ballast water management standard, the noxious
substances — is unknown here.

## What the Act turns out to say

### 1. A Singapore ship's garbage offence stops at Singapore's waters; its oil offence does not

s 6(1) catches refuse, garbage, plastics and the like only "from any ship into
Singapore waters". s 7(1) catches oil "from a Singapore ship into any part of the sea
or from any ship into Singapore waters", and ss 10 and 10A reach the same way. On the
Act's own text a Singapore ship dumping garbage on the high seas commits no s 6
offence; one pumping oily bilge off Africa commits a s 7 offence. (Regulations under
s 34(2)(i) may give regulations extraterritorial effect; none were read.) Asserted.

### 2. An approved anti-pollution discharge is excused for an oily mixture, not for oil

s 7(2)(c) excuses a discharge "for the purpose of combating specific pollution
incidents" approved by the appointed authority, but only "in the case of an oily
mixture". The same exception in s 10(2)(c) for noxious liquid substances has no such
limit. Asserted.

### 3. The person who throws rubbish into the water faces the same maximum as a ship

s 5 makes "any person" who puts or throws oil, refuse, garbage, plastics, waste
matter, a carcase, noxious liquid substances, packaged marine pollutants or trade
effluent into Singapore waters liable to $20,000 or 6 months — the same as a ship's
garbage offence under s 6. Sediments, ballast water and sewage are not in s 5's list.
Oil discharged from land or a ship carries a $1,000 minimum and a $1 million maximum
or 2 years (ss 3, 7). Asserted.

### 4. Who is liable under s 3 is not quite settled by the text

s 3(a) names the occupier "or if the discharge is caused by the act of another person
who is in that place without the permission ... of the occupier, that person". Yet
s 4(2) separately gives the occupier a defence where a trespasser caused the
discharge, as though the occupier might still be charged. The encoding names the
trespasser as the person liable and keeps s 4(2) as the occupier's defence. The
refinery-effluent defence (s 4(3)) is lost if the shore was fouled, unless the court
is satisfied the fouling was not from that place's effluent (s 4(4)). Asserted.

### 5. The master, owner and agent each commit the ship offence; a pilot does not

ss 6, 7, 10 and 10A make "the master, the owner and the agent of the ship" each
guilty. "Master" excludes a pilot (s 2(1)). s 8 (oil residues not retained) names only
the master and owner, with a fine of up to $1 million and no imprisonment. Asserted.

### 6. The ship owner pays for the clean-up, unless the civil liability regime applies

ss 17 and 18 make the owner liable for the appointed authority's reasonable removal
costs where the pollutant is discharged into Singapore waters or drifts in; owners of
several ships are jointly and severally liable where the costs cannot be separated.
s 18(4) excludes oil and oily mixtures where the Merchant Shipping (Civil Liability
and Compensation for Oil Pollution) Act 1998 applies, and bunker oil under the 2008
bunker oil Act. Neither section names sediments or ballast water. Asserted (joint and several liability is not).

### 7. Reporting falls back from the master to the owner, with knowledge defences

The master must report without delay (s 15(1)) unless unable (s 15(2)). If the master
is unable or the ship is abandoned, the owner, charterer, manager, operator or agent
must report (s 15(3)), with defences of not being aware of the occurrence, or not
knowing or suspecting the master's inability (s 15(5)). $5,000. Asserted.

## What would need doing before this is worth anything

- The regulations under ss 6(5), 7(4), 10(4), 10A(3), 15 and 34 were not retrieved:
  they decide which discharges are lawful in practice (by inference from s 34(1)(a), the MARPOL
  discharge limits), what "prescribed circumstances" for reporting are, and which offences are
  compoundable.
- The s 3(a) / s 4(2) tension (finding 4) needs case law; none was searched.
- s 10B's defences are for the accused to prove on a balance of probabilities;
  the encoding treats them, like the exceptions, as simply defeating the offence.
- No cases were searched.
