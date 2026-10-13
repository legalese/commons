# Transfer of Land Act 1893 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** the compilation published on legislation.wa.gov.au (mrdoc 49493,
retrieved 7 September 2026), deposited at
`../../registers/source-bundle/mrdoc_49493.txt`. The deposit names no compilation
number. Its compilation table ends with the Petroleum Legislation Amendment Act 2024
Pt 5 Div 13 (other than s 424(4)), in force 28 May 2026. The last reprint it lists is
Reprint 11 as at 8 January 2016. The uncommenced provisions table lists the Transfer
of Land Amendment Act 2003 ss 43, 46, 56 and 57, the Community Titles Act 2018 s 253,
the Petroleum Legislation Amendment Act 2024 s 424(4) and the Evidence Act 2025
s 492(2). None of them is shown or encoded.

**Checks:** one module (`tla-title.l4`) and one case file (`tla-cases-title.l4`):
58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This encoding answers requirement **au/wa:REQ-0007** (priority 1). The three Western
Australian cradle-to-grave lives raise it **7 times**:

- Chloe **c052**, 2028-05-15: settlement of the Byford land, the mortgage, title
  registered. "What makes the title indefeasible; what does the lender register?"
  (ss 68, 105).
- Chloe **c081**, 2040-04-28: the Baldivis townhouse in a community titles scheme,
  $1,300,000 (s 68).
- Chloe **c087**, 2052-08-25: her father Graham dies. He and Sue hold the Armadale
  house "as joint tenants" (s 60).
- Chloe **c096**, 2083-02-09: Liam dies, and the apartment passes by survivorship
  (s 60).
- Jake **k076**, 2045-03-20: settlement of his strata apartment (s 68).
- Daniel **d074**, 2052-11-03: his father Giuseppe dies, owning a house in Reggio
  Calabria (s 60).
- Daniel **d093**, 2078-11-15: Daniel dies, and the house passes to Priya by
  survivorship (s 60).

The scope is those provisions and what is needed to answer the lives' questions:

- when an instrument is registered, what registration passes, and priority
  (ss 52(2), 53, 58);
- the exceptions to paramountcy (s 68(1), (1A));
- notice of unregistered interests (s 134);
- recovery actions, compensation and fraud (ss 199, 201, 202 in comment, 214A);
- the mortgage's signature rules and effect, and the default-notice-sale sequence
  (ss 105, 105AA, 106-108);
- "no survivorship" (s 61);
- the survivor's route onto the register (s 227) and the executor's (s 187).

**Not encoded:**

- bringing land under the Act;
- Crown land, meaning s 68(2)-(4) and every Crown land qualification;
- leases, easements and covenants beyond s 68(1A);
- caveats;
- sale proceeds, foreclosure and the mortgagee's other remedies (ss 109-119);
- the conditional tenure land qualification to ss 106-108;
- the Registrar's powers and fees;
- electronic conveyancing beyond s 105AA;
- the Community Titles Act 2018 and Strata Titles Act 1985, which c081 and k076 also
  ask about.

The approved forms are not in the deposit. "Fraud" (s 68) and "the person entitled"
(s 227) are not defined, so both are inputs.

The scenarios do not say how Chloe and Liam, or Daniel and Priya, are registered.
Where a life says "by survivorship", joint proprietorship is assumed. Graham and Sue
are stated to be joint tenants. The signatures on the Byford mortgage are assumed.

## What the Act turns out to say

### 1. Section 60 does not say "survivorship"

Four of the seven events (c087, c096, d074, d093) cite s 60 for survivorship. The
section says only that persons "registered as joint proprietors of land shall be
deemed to be entitled to the same as joint tenants". It also says that tenants in
common may take one certificate or separate certificates for their shares. That the
survivor takes the whole is the general-law incident of a joint tenancy. That is an
inference; it is not in the deposited text.

What the Act does supply is the procedure in **s 227**. On the death of a joint
proprietor, the Commissioner, on the application of "the person entitled" and proof
of the death, may direct the survivor's registration. The survivor then becomes "the
transferee" and is "deemed its proprietor". s 227 asks for no probate. So Sue (c087),
Chloe (c096) and Priya (d093) each go onto the register by s 227, not through
Graham's, Liam's or Daniel's will and executor. Asserted, on the joint-proprietorship
assumption above.

### 2. Giuseppe's Calabria house is outside the Act altogether (d074)

s 227 applies only to a person "registered" as joint proprietor under this Act. A
house in Reggio Calabria is not land under the operation of this Act, and Giuseppe is
not said to be a joint owner. The Act says nothing about it. Asserted: no s 227
registration.

### 3. "No survivorship" restricts dealing, and does not say it ends survivorship

Under s 61(3), once the Registrar has signed the words, "it shall not be lawful for
any persons other than the proprietors registered to transfer or otherwise deal with
the property" without an order of the Supreme Court or the Commissioner. The section
does not say that the words turn a joint tenancy into a tenancy in common. Asserted
as written.

### 4. What makes the title indefeasible, and what still binds it (c052, c081, k076)

Under s 68(1), the registered proprietor holds "except in case of fraud" subject to
the encumbrances notified on the certificate, "but absolutely free from all other
encumbrances whatsoever". There are two exceptions: a prior registered certificate,
and land included by wrong description (which binds a proprietor who is not a
purchaser for value).

s 68(1A) then binds the land "despite subsection (1)", even though none of these is
notified on the certificate:

- reservations in the grant;
- adverse possession;
- public rights of way;
- easements by enjoyment or user;
- **"any unpaid rates"**;
- mining leases;
- a prior unregistered lease of **not more than 5 years** to a tenant **in actual
  possession**.

An option in such a lease is not valid against a later registered interest unless
the lease is registered or caveated.

Under s 134, knowledge of an unregistered interest or a trust "shall not of itself be
imputed as fraud". Under s 53(2), priority between instruments goes by time of
registration, "notwithstanding any actual or constructive notice". Asserted.

Whether a strata company's or community corporation's unpaid contributions (k076,
c081) are "rates" in s 68(1A) is not answered by this Act. Not asserted.

### 5. What the lender registers is a security, not a transfer (c052)

Under s 106(1), a registered mortgage "shall ... have effect as a security but shall
not operate as a transfer of the land". Under s 58, nothing makes the land liable to
a mortgage until it is registered.

s 105(3)-(5) adds a trap that overrides s 58. Suppose the only counterpart lodged
bears the lender's signature and not the owner's. Then the registered mortgage is
"not valid or binding against the proprietor of the land" unless the owner signed a
counterpart before registration. s 105AA bars electronic lodgment unless the lender
holds a counterpart signed by the owner. Asserted.

### 6. Default to sale takes two months, both of which the mortgage can change

Under s 106(1), the default must continue for one month, "or such other period of
time as may therein for that purpose be expressly fixed", before notice. Under s 108,
it must continue a further month after service, again unless the mortgage fixes
another period.

Under s 106(2), service is proper only if the notice is delivered personally, sent by
registered post to the address in the Register or the known current address, left in
a conspicuous place on the land, or sent in an electronic way the regulations
prescribe. Ordinary post is not proper service. Under s 107, a written demand for
money payable on demand replaces the notice. Asserted.

### 7. The State pays when the wrongdoer cannot

s 199 bars every action to recover land from the registered proprietor except six
listed cases. A person deprived by fraud may recover from the fraudster, but not from
a later transferee bona fide for value (ss 199(d), 202). Under s 201(3), damages may
be recovered from the State (the Registrar as nominal defendant) if the person liable
is dead, bankrupt or cannot be found, or if a bona fide transfer has capped their
liability under s 201(2). Under s 214A, a title procured by fraud is void against the
parties to the fraud "whether or not anyone is convicted". Asserted.

## What would need doing before this is worth anything

- The general law of survivorship, and the case law on "fraud" in s 68, decide the
  questions the lives actually ask. Neither is in the Act, and no case law was
  searched.
- Caveats (Part IV Div 3), leases and easements, and the mortgagee's remedies after
  sale (ss 109-119) are untouched.
- The Community Titles Act 2018 and Strata Titles Act 1985 parts of c081 and k076
  belong to other encodings.
- The Transfer of Land Regulations and the Registrar's requirements under s 182A
  (approved forms, prescribed electronic service) were not retrieved.
- The scenarios should state how each property is registered. This encoding assumes
  joint proprietorship where a life says "by survivorship".
