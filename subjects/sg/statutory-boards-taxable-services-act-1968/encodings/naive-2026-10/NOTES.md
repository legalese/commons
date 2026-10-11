# Statutory Boards (Taxable Services) Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1 April 2024), deposited at `../../registers/source-bundle/SBTSA1968.txt`. The
revised edition incorporates amendments up to 1 December 2021; the latest
amendment annotated is Act 4 of 2008, marked "wef 01/04/2024" on s 3(2A) and s 4A.

**Checks:** one case file, 45 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0150**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. It asks what the Act decides for a person or business it
applies to; no scenario has asked a sharper question yet. The Act is seven short
sections, so this row encodes all of the operative part: ss 2, 3(1) to (4), 4, 4A,
5 and 6. Not encoded: s 3(5) (orders go to Parliament), s 7 (rule-making), and the
content of the fee-recovery laws that s 4(2) borrows. No Gazette order under s 3
was retrieved, so no actual tax rate or list of taxable services is known here.

## What the Act turns out to say

### 1. The Act fixes no tax rate, except one: 50% on commercial electricity, paid by the owner

Section 3(1) leaves both the list of taxable services and the rate to a Minister's
order in the Gazette. The single figure in the Act is s 3(2): an order may impose an
**additional tax at 50%** of the electricity charges for specified commercial
buildings, and that tax "shall be paid by the owners", not by the tenants who use the
power. "Owners" takes its Property Tax Act 1960 meaning. Asserted ($1,000 of
electricity gives $500; $2,480 gives $1,240; a tenant or resident is not liable).

### 2. Flats inside a commercial building are caught too

s 3(3)(b): a commercial building "is deemed to include any part of the building
which is used for residential purposes". Electricity to a residential part of a
specified commercial building attracts the same 50%. Asserted.

### 3. A 2008 amendment that started in 2024, with a validation clause reaching back

s 3(2A) (recovery fees and late-payment charges in the order) and s 4A came from
the Statutes (Miscellaneous Amendments) Act 2008, which the Legislative History says
was passed on 22 January 2008 but commenced on **1 April 2024**. s 4A deems every
late-payment charge collected for the Government before that commencement "always
to have been validly collected" and says no legal proceedings "shall lie or be
instituted or maintained" over any such collection. So a person charged a late fee
before 1 April 2024 cannot sue to get it back on the ground that it lacked authority.
This row takes 1 April 2024 as the commencement date. Asserted (31 March 2024 is
validated; 1 April 2024 is not, and from that date s 3(2A) authorises the charge if
an order prescribes it).

### 4. Private licensees count as "statutory boards"

s 2: "statutory board" includes a public telecommunication licensee, a gas licensee
and a market support services licensee under the Electricity Act 2001. Their
specified services can be taxed under this Act like a real statutory board's. A
company holding none of those licences is outside the Act. The Legislative History
lists amendments by the Telecommunications Act 1999 and the Gas Act 2001 but names no
Electricity Act amendment; which Act added the market support licensee was not
traced. Asserted.

### 5. Government fees collected by a board count as the board's services

s 3(4): services for which a board collects fees "on behalf of the Government" are
deemed to be the board's services, so they can be specified as taxable. "Services"
also includes letting an apparatus or appliance (s 2), such as a meter. Asserted.

### 6. The board collects, but the money is the Government's

s 4(1): the board assesses and collects "on behalf of the Government", in a manner it
determines with the Minister's approval; s 4(2) lets it use its own fee-recovery
powers, subject to rules; s 5 sends all of it to the Consolidated Fund. s 6 lets the
Minister exempt any person or class by order. There are no offences or penalties in
the Act. Asserted.

## What would need doing before this is worth anything

- The Gazette orders under s 3 (which services, what rate, which commercial
  buildings, what late charges) were not retrieved. Without them the encoding
  cannot say whether any real bill is taxed.
- The fee-recovery provisions of each board's own Act (s 4(2)) were not read.
- The "subject to any rules" qualification in s 4(2) is modelled as an all-or-nothing
  bar; rules could restrict the powers only partly.
- No case law was searched.
